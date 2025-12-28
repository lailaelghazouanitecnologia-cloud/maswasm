"""
Tzar Engine - Core module (part 8).
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
# $func274
# ----------------------------------------------------------
def func274(arg0, arg1):
    while True:  # $label7
        while True:  # $label2
            while True:  # $label1
                v3 = load32(arg0 + 8)
                if (arg1 <= load32(load32(arg0 + 8) + 88)):
                    while True:  # $label0
                        v5 = load32(arg0 + 108)
                        v8 = load32(v3 + 40)
                        v7 = load32(((v3 + 84) if (u32(load32(load32(v3 + 40) + 12)) < u32(2)) else (arg0 + 108)))
                        v7 = (load32(arg0 + 108) if (v5 > v7) else load32(((v3 + 84) if (u32(load32(load32(v3 + 40) + 12)) < u32(2)) else (arg0 + 108))))
                        if ((load32(arg0 + 108) if (v5 > v7) else load32(((v3 + 84) if (u32(load32(load32(v3 + 40) + 12)) < u32(2)) else (arg0 + 108)))) >= arg1):
                            break
                        if (load32(arg0 + 192) != 1):
                            break
                        v2 = (arg0 + 196)
                        if (load32((arg0 + 196)) != 3):
                            break
                        v5 = v7
                        v4 = (load32(arg0 + 16) + (v7 * load32(arg0 + 100)))
                        v9 = load32(v3)
                        v3 = (load32(v8 + 136) + (load32(v3) * v5))
                        v6 = (load32(v8 + 136) + (load32(v3) * v5))
                        v12 = load32(v2 + 16)
                        v10 = load32(v2 + 8)
                        while True:  # $label3
                            v2 = load32(v2 + 4)
                            if load32(v2 + 4):
                                if (arg1 <= v5):
                                    break
                                if (v10 <= 0):
                                    break
                                v15 = ((8 & 0xFFFFFFFF) >> v2)
                                v13 = ((-1 << ((8 & 0xFFFFFFFF) >> v2)) ^ -1)
                                v14 = ((-1 << v2) ^ -1)
                                v17 = (v10 & -2)
                                v18 = (v10 & 1)
                                while True:  # $label6
                                    v11 = 0
                                    v2 = 0
                                    v16 = 0
                                    if (v10 != 1):
                                        while True:  # $label5
                                            if not (v11 & v14):
                                                v2 = load8u(v4)
                                                v4 = (v4 + 1)
                                            store8(v6, ((load32((v12 + ((v2 & v13) << 2))) & 0xFFFFFFFF) >> 8))
                                            while True:  # $label4
                                                if ((v11 | 1) & v14):
                                                    v2 = ((v2 & 0xFFFFFFFF) >> v15)
                                                    break
                                                v2 = load8u(v4)
                                                break
                                            v4 = (v4 + 1)
                                            store8(v6 + 1, ((load32((v12 + ((v2 & v13) << 2))) & 0xFFFFFFFF) >> 8))
                                            v11 = (v11 + 2)
                                            v2 = ((v2 & 0xFFFFFFFF) >> v15)
                                            v6 = (v6 + 2)
                                            v16 = (v16 + 2)
                                            if ((v16 + 2) != v17):
                                                continue
                                            break
                                    if v18:
                                        if not (v11 & v14):
                                            v2 = load8u(v4)
                                            v4 = (v4 + 1)
                                        store8(v6, ((load32((v12 + ((v2 & v13) << 2))) & 0xFFFFFFFF) >> 8))
                                        v6 = (v6 + 1)
                                    v5 = (v5 + 1)
                                    if ((v5 + 1) != arg1):
                                        continue
                                    break
                                break
                            break
                        v5 = load32(v8 + 12)
                        if not load32(v8 + 12):
                            break
                        if not load32(((v5 << 2) + 9687552)):
                            break
                        v5 = load32(v8 + 140)
                        v4 = (arg1 - v7)
                        if ((arg1 - v7) & 1):
                            v7 = (v7 + 1)
                            v5 = v3
                        else:
                        v2 = v3
                        if (v4 != 1):
                            v3 = v5
                            while True:  # $label8
                                v3 = (v2 + v9)
                                v2 = (v3 + v9)
                                v7 = (v7 + 2)
                                if ((v7 + 2) != arg1):
                                    continue
                                break
                        store32(v8 + 140, v3)
                        break
                    store32(arg0 + 108, arg1)
                    store32(arg0 + 116, arg1)
                    return call_table(load32(((load32(v8 + 12) << 2) + 9687552)))
                a_c()
                raise Unreachable()
                break
            a_c()
            raise Unreachable()
            break
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()
    return 3488

# ----------------------------------------------------------
# $func275
# ----------------------------------------------------------
def func275(arg0, arg1, arg2, arg3, arg4, arg5):
    v19 = load32(arg0 + 120)
    v8 = load32(arg0 + 56)
    v6 = load32(arg0 + 112)
    v13 = (v6 // arg2)
    v15 = (load32(arg0 + 112) - ((v6 // arg2) * arg2))
    v28 = load32(arg0 + 148)
    while True:  # $label0
        while True:  # $label7
            v10 = (arg2 * arg4)
            v9 = (v6 >= (arg2 * arg4))
            if not (v6 >= (arg2 * arg4)):
                v7 = load32(arg0 + 152)
                if load32(arg0 + 152):
                else:
                v7 = 0
                if (0 >= load32(arg0 + 164)):
                    break
                v14 = (load32(arg0 + 168) + (v7 * 548))
            if (arg4 > load32(arg0 + 108)):
                v7 = (arg2 * arg3)
                if ((arg2 * arg3) >= v10):
                    v25 = (arg0 + 124)
                    v16 = (arg0 + 24)
                    v26 = (arg1 + (v10 << 2))
                    arg3 = (arg1 + (v6 << 2))
                    while True:  # $label37
                        while True:  # $label38
                            while True:  # $label11
                                while True:  # $label1
                                    if v9:
                                        break
                                    v17 = (v25 if (v19 > 0) else 0)
                                    v27 = (v13 if v8 else 16777216)
                                    v20 = (arg0 + 120)
                                    v30 = (v19 + 280)
                                    v29 = (arg1 + (v7 << 2))
                                    v31 = (arg0 + 136)
                                    v22 = (arg0 - -64)
                                    v10 = arg3
                                    while True:  # $label34
                                        while True:  # $label26
                                            while True:  # $label9
                                                while True:  # $label4
                                                    while True:  # $label30
                                                        while True:  # $label28
                                                            while True:  # $label25
                                                                while True:  # $label6
                                                                    while True:  # $label3
                                                                        while True:  # $label2
                                                                            if (v13 >= v27):
                                                                                if not load32(arg0 + 56):
                                                                                    break
                                                                                store64(v22, load64(v16))
                                                                                store64(v22 + 24, load64(v16 + 24))
                                                                                store64(v22 + 16, load64(v16 + 16))
                                                                                store64(v22 + 8, load64(v16 + 8))
                                                                                store32(arg0 + 96, ((arg3 - arg1) >> 2))
                                                                                if (load32(arg0 + 120) > 0):
                                                                                    func456(v25, v31)
                                                                                v27 = (v13 + 8)
                                                                            if not (v15 & v28):
                                                                                v6 = load32(arg0 + 152)
                                                                                if load32(arg0 + 152):
                                                                                else:
                                                                                v6 = 0
                                                                                if (0 >= load32(arg0 + 164)):
                                                                                    break
                                                                                v14 = (load32(arg0 + 168) + (v6 * 548))
                                                                            if not v14:
                                                                                break
                                                                            if load32(v14 + 28):
                                                                                v6 = load32(v14 + 24)
                                                                                break
                                                                            if (load32(arg0 + 44) >= 32):
                                                                                func135(v16)
                                                                            while True:  # $label8
                                                                                if load32(v14 + 32):
                                                                                    v32 = load64(arg0 + 24)
                                                                                    v6 = load32(arg0 + 44)
                                                                                    v8 = (v14 + ((i32(((load64(arg0 + 24) & 0xFFFFFFFF) >> i32((load32(arg0 + 44) & 63)))) & 63) << 3))
                                                                                    v9 = load32((v14 + ((i32(((load64(arg0 + 24) & 0xFFFFFFFF) >> i32((load32(arg0 + 44) & 63)))) & 63) << 3)) + 36)
                                                                                    v7 = (load32((v14 + ((i32(((load64(arg0 + 24) & 0xFFFFFFFF) >> i32((load32(arg0 + 44) & 63)))) & 63) << 3)) + 36) + v6)
                                                                                    v6 = load32(v8 + 40)
                                                                                    while True:  # $label5
                                                                                        if (v9 <= 255):
                                                                                            store32(arg0 + 44, v7)
                                                                                            store32(arg3, v6)
                                                                                            v6 = 0
                                                                                            break
                                                                                        store32(arg0 + 44, (v7 - 256))
                                                                                        if (u32(v6) <= u32(255)):
                                                                                            break
                                                                                        break
                                                                                    v7 = load32(arg0 + 40)
                                                                                    v8 = load32(arg0 + 36)
                                                                                    if (u32(load32(arg0 + 40)) > u32(load32(arg0 + 36))):
                                                                                        break
                                                                                    if load32(arg0 + 48):
                                                                                        break
                                                                                    if (v7 == v8):
                                                                                        if (load32(arg0 + 44) > 64):
                                                                                            break
                                                                                    if v6:
                                                                                        break
                                                                                    break
                                                                                v32 = load64(arg0 + 24)
                                                                                v7 = load32(arg0 + 44)
                                                                                v6 = (load32(v14) + ((i32(((load64(arg0 + 24) & 0xFFFFFFFF) >> i32((load32(arg0 + 44) & 63)))) & 255) << 2))
                                                                                v8 = load8u((load32(v14) + ((i32(((load64(arg0 + 24) & 0xFFFFFFFF) >> i32((load32(arg0 + 44) & 63)))) & 255) << 2)))
                                                                                if (u32(load8u((load32(v14) + ((i32(((load64(arg0 + 24) & 0xFFFFFFFF) >> i32((load32(arg0 + 44) & 63)))) & 255) << 2)))) >= u32(9)):
                                                                                    v7 = (v7 + 8)
                                                                                    v6 = ((v6 + (load16u(v6 + 2) << 2)) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v7 + 8) & 63)))) & ((-1 << (v8 - 8)) ^ -1)) << 2))
                                                                                else:
                                                                                store32(load8u(((v6 + (load16u(v6 + 2) << 2)) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v7 + 8) & 63)))) & ((-1 << (v8 - 8)) ^ -1)) << 2))) + 44, ((v8 & 255) + v7))
                                                                                v8 = load32(arg0 + 36)
                                                                                v7 = load32(arg0 + 40)
                                                                                v6 = load16u(v6 + 2)
                                                                                break
                                                                            if (u32(v7) > u32(v8)):
                                                                                break
                                                                            if load32(arg0 + 48):
                                                                                break
                                                                            if (v7 == v8):
                                                                                if (load32(arg0 + 44) > 64):
                                                                                    break
                                                                            if (v6 <= 255):
                                                                                if load32(v14 + 20):
                                                                                    v6 = (load32(v14 + 24) | (v6 << 8))
                                                                                    break
                                                                                v7 = load32(arg0 + 44)
                                                                                v8 = (load32(v14 + 4) + ((i32(((v32 & 0xFFFFFFFF) >> i32((load32(arg0 + 44) & 63)))) & 255) << 2))
                                                                                v9 = load8u((load32(v14 + 4) + ((i32(((v32 & 0xFFFFFFFF) >> i32((load32(arg0 + 44) & 63)))) & 255) << 2)))
                                                                                if (u32(load8u((load32(v14 + 4) + ((i32(((v32 & 0xFFFFFFFF) >> i32((load32(arg0 + 44) & 63)))) & 255) << 2)))) >= u32(9)):
                                                                                    v7 = (v7 + 8)
                                                                                    v8 = ((v8 + (load16u(v8 + 2) << 2)) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v7 + 8) & 63)))) & ((-1 << (v9 - 8)) ^ -1)) << 2))
                                                                                else:
                                                                                v7 = ((v9 & 255) + v7)
                                                                                store32(load8u(((v8 + (load16u(v8 + 2) << 2)) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v7 + 8) & 63)))) & ((-1 << (v9 - 8)) ^ -1)) << 2))) + 44, ((v9 & 255) + v7))
                                                                                v11 = load16u(v8 + 2)
                                                                                if (v7 >= 32):
                                                                                    func135(v16)
                                                                                    v32 = load64(arg0 + 24)
                                                                                    v7 = load32(arg0 + 44)
                                                                                v8 = (load32(v14 + 8) + ((i32(((v32 & 0xFFFFFFFF) >> i32((v7 & 63)))) & 255) << 2))
                                                                                v12 = load8u((load32(v14 + 8) + ((i32(((v32 & 0xFFFFFFFF) >> i32((v7 & 63)))) & 255) << 2)))
                                                                                if (u32(load8u((load32(v14 + 8) + ((i32(((v32 & 0xFFFFFFFF) >> i32((v7 & 63)))) & 255) << 2)))) >= u32(9)):
                                                                                    v7 = (v7 + 8)
                                                                                    v8 = ((v8 + (load16u(v8 + 2) << 2)) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v7 + 8) & 63)))) & ((-1 << (v12 - 8)) ^ -1)) << 2))
                                                                                    v12 = load8u(((v8 + (load16u(v8 + 2) << 2)) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v7 + 8) & 63)))) & ((-1 << (v12 - 8)) ^ -1)) << 2)))
                                                                                v18 = load16u(v8 + 2)
                                                                                v8 = (v7 + (v12 & 255))
                                                                                v7 = (load32(v14 + 12) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v7 + (v12 & 255)) & 63)))) & 255) << 2))
                                                                                v9 = load8u((load32(v14 + 12) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v7 + (v12 & 255)) & 63)))) & 255) << 2)))
                                                                                if (u32(load8u((load32(v14 + 12) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v7 + (v12 & 255)) & 63)))) & 255) << 2)))) >= u32(9)):
                                                                                    v8 = (v8 + 8)
                                                                                    v7 = ((v7 + (load16u(v7 + 2) << 2)) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v8 + 8) & 63)))) & ((-1 << (v9 - 8)) ^ -1)) << 2))
                                                                                else:
                                                                                v8 = ((v9 & 255) + v8)
                                                                                store32(load8u(((v7 + (load16u(v7 + 2) << 2)) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v8 + 8) & 63)))) & ((-1 << (v9 - 8)) ^ -1)) << 2))) + 44, ((v9 & 255) + v8))
                                                                                v9 = load32(arg0 + 40)
                                                                                v12 = load32(arg0 + 36)
                                                                                if (u32(load32(arg0 + 40)) > u32(load32(arg0 + 36))):
                                                                                    break
                                                                                if load32(arg0 + 48):
                                                                                    break
                                                                                v7 = load16u(v7 + 2)
                                                                                if ((v9 == v12) & (v8 > 64)):
                                                                                    break
                                                                                v6 = ((((v11 << 16) | (v6 << 8)) | v18) | (v7 << 24))
                                                                                break
                                                                            if (u32(v6) <= u32(279)):
                                                                                v12 = (v6 - 256)
                                                                                if (u32((v6 - 256)) >= u32(4)):
                                                                                    v7 = (((v6 - 258) & 0xFFFFFFFF) >> 1)
                                                                                    v12 = (func39(v16, (((v6 - 258) & 0xFFFFFFFF) >> 1)) + (((v6 & 1) | 2) << v7))
                                                                                    v32 = load64(arg0 + 24)
                                                                                v7 = load32(arg0 + 44)
                                                                                v6 = (load32(v14 + 16) + ((i32(((v32 & 0xFFFFFFFF) >> i32((load32(arg0 + 44) & 63)))) & 255) << 2))
                                                                                v8 = load8u((load32(v14 + 16) + ((i32(((v32 & 0xFFFFFFFF) >> i32((load32(arg0 + 44) & 63)))) & 255) << 2)))
                                                                                if (u32(load8u((load32(v14 + 16) + ((i32(((v32 & 0xFFFFFFFF) >> i32((load32(arg0 + 44) & 63)))) & 255) << 2)))) >= u32(9)):
                                                                                    v7 = (v7 + 8)
                                                                                    v6 = ((v6 + (load16u(v6 + 2) << 2)) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v7 + 8) & 63)))) & ((-1 << (v8 - 8)) ^ -1)) << 2))
                                                                                else:
                                                                                v7 = ((v8 & 255) + v7)
                                                                                store32(load8u(((v6 + (load16u(v6 + 2) << 2)) + ((i32(((v32 & 0xFFFFFFFF) >> i32(((v7 + 8) & 63)))) & ((-1 << (v8 - 8)) ^ -1)) << 2))) + 44, ((v8 & 255) + v7))
                                                                                v6 = load16u(v6 + 2)
                                                                                if (v7 >= 32):
                                                                                    func135(v16)
                                                                                while True:  # $label10
                                                                                    if (u32(v6) >= u32(4)):
                                                                                        v7 = (((v6 - 2) & 0xFFFFFFFF) >> 1)
                                                                                        v6 = (func39(v16, (((v6 - 2) & 0xFFFFFFFF) >> 1)) + (((v6 & 1) | 2) << v7))
                                                                                    if ((v6 + 1) >= 121):
                                                                                        break
                                                                                    v6 = load8u((v6 + 13840))
                                                                                    v6 = (((((load8u((v6 + 13840)) & 0xFFFFFFFF) >> 4) * arg2) - (v6 & 15)) + 8)
                                                                                    break
                                                                                v9 = (1 if (v6 <= 1) else (((((load8u((v6 + 13840)) & 0xFFFFFFFF) >> 4) * arg2) - (v6 & 15)) + 8))
                                                                                v6 = load32(arg0 + 40)
                                                                                v7 = load32(arg0 + 36)
                                                                                if (u32(load32(arg0 + 40)) > u32(load32(arg0 + 36))):
                                                                                    break
                                                                                if load32(arg0 + 48):
                                                                                    break
                                                                                if (v6 == v7):
                                                                                    if (load32(arg0 + 44) > 64):
                                                                                        break
                                                                                if (((arg3 - arg1) >> 2) < v9):
                                                                                    break
                                                                                v8 = (v12 + 1)
                                                                                if ((v12 + 1) > ((v29 - arg3) >> 2)):
                                                                                    break
                                                                                v7 = v8
                                                                                v18 = 0
                                                                                v23 = 0
                                                                                v6 = arg3
                                                                                v12 = (arg3 - (v9 << 2))
                                                                                while True:  # $label17
                                                                                    while True:  # $label18
                                                                                        while True:  # $label14
                                                                                            while True:  # $label12
                                                                                                if (v6 & 3):
                                                                                                    break
                                                                                                if (v9 > 2):
                                                                                                    break
                                                                                                if (v7 < 4):
                                                                                                    break
                                                                                                while True:  # $label13
                                                                                                    if (v9 == 1):
                                                                                                        v9 = load32(v12)
                                                                                                        v32 = i32(load32(v12))
                                                                                                        v32 = ((i32(load32(v12)) << 32) | v32)
                                                                                                        break
                                                                                                    v32 = load64(v12)
                                                                                                    v9 = i32(load64(v12))
                                                                                                    break
                                                                                                if (v6 & 4):
                                                                                                    store32(v6, v9)
                                                                                                    v7 = (v7 - 1)
                                                                                                    v32 = rotl(v32, 32)
                                                                                                    v12 = (v12 + 4)
                                                                                                    v6 = (v6 + 4)
                                                                                                if (v6 & 7):
                                                                                                    break
                                                                                                v11 = ((v7 & 0xFFFFFFFF) >> 1)
                                                                                                v24 = (((v7 & 0xFFFFFFFF) >> 1) & 7)
                                                                                                v9 = 0
                                                                                                if (u32((v11 - 1)) >= u32(7)):
                                                                                                    v21 = (v11 & 2147483640)
                                                                                                    while True:  # $label15
                                                                                                        v11 = (v9 << 3)
                                                                                                        store64((v6 + (v9 << 3)), v32)
                                                                                                        store64((v6 + (v11 | 8)), v32)
                                                                                                        store64((v6 + (v11 | 16)), v32)
                                                                                                        store64((v6 + (v11 | 24)), v32)
                                                                                                        store64((v6 + (v11 | 32)), v32)
                                                                                                        store64((v6 + (v11 | 40)), v32)
                                                                                                        store64((v6 + (v11 | 48)), v32)
                                                                                                        store64((v6 + (v11 | 56)), v32)
                                                                                                        v9 = (v9 + 8)
                                                                                                        v23 = (v23 + 8)
                                                                                                        if ((v23 + 8) != v21):
                                                                                                            continue
                                                                                                        break
                                                                                                if v24:
                                                                                                    while True:  # $label16
                                                                                                        store64((v6 + (v9 << 3)), v32)
                                                                                                        v9 = (v9 + 1)
                                                                                                        v18 = (v18 + 1)
                                                                                                        if ((v18 + 1) != v24):
                                                                                                            continue
                                                                                                        break
                                                                                                if not (v7 & 1):
                                                                                                    break
                                                                                                v7 = ((v7 << 2) & -8)
                                                                                                store32((v6 + ((v7 << 2) & -8)), load32((v7 + v12)))
                                                                                                break
                                                                                                break
                                                                                            if (v7 <= v9):
                                                                                                break
                                                                                            if (v7 <= 0):
                                                                                                break
                                                                                            v9 = 0
                                                                                            if (u32(v7) >= u32(4)):
                                                                                                v24 = (v7 & -4)
                                                                                                while True:  # $label19
                                                                                                    v11 = (v9 << 2)
                                                                                                    store32((v6 + (v9 << 2)), load32((v11 + v12)))
                                                                                                    v21 = (v11 | 4)
                                                                                                    store32((v6 + (v11 | 4)), load32((v12 + v21)))
                                                                                                    v21 = (v11 | 8)
                                                                                                    store32((v6 + (v11 | 8)), load32((v12 + v21)))
                                                                                                    v11 = (v11 | 12)
                                                                                                    store32((v6 + (v11 | 12)), load32((v11 + v12)))
                                                                                                    v9 = (v9 + 4)
                                                                                                    v23 = (v23 + 4)
                                                                                                    if ((v23 + 4) != v24):
                                                                                                        continue
                                                                                                    break
                                                                                            v7 = (v7 & 3)
                                                                                            if not (v7 & 3):
                                                                                                break
                                                                                            while True:  # $label20
                                                                                                v11 = (v9 << 2)
                                                                                                store32((v6 + (v9 << 2)), load32((v11 + v12)))
                                                                                                v9 = (v9 + 1)
                                                                                                v18 = (v18 + 1)
                                                                                                if ((v18 + 1) != v7):
                                                                                                    continue
                                                                                                break
                                                                                            break
                                                                                            break
                                                                                        a_c()
                                                                                        raise Unreachable()
                                                                                        break
                                                                                    # TODO: memory.copy
                                                                                    break
                                                                                arg3 = (arg3 + (v8 << 2))
                                                                                while True:  # $label21
                                                                                    v15 = (v8 + v15)
                                                                                    if ((v8 + v15) < arg2):
                                                                                        break
                                                                                    if not arg5:
                                                                                        while True:  # $label22
                                                                                            v13 = (v13 + 1)
                                                                                            v15 = (v15 - arg2)
                                                                                            if ((v15 - arg2) >= arg2):
                                                                                                continue
                                                                                            break
                                                                                            break
                                                                                        raise Unreachable()
                                                                                    while True:  # $label24
                                                                                        v15 = (v15 - arg2)
                                                                                        v6 = v13
                                                                                        v13 = (v13 + 1)
                                                                                        while True:  # $label23
                                                                                            if (arg4 <= v6):
                                                                                                break
                                                                                            if (v13 & 15):
                                                                                                break
                                                                                            break
                                                                                        if (arg2 <= v15):
                                                                                            continue
                                                                                        break
                                                                                    break
                                                                                if (u32(arg3) > u32(v29)):
                                                                                    break
                                                                                if (v15 & v28):
                                                                                    v6 = load32(v20 + 32)
                                                                                    if load32(v20 + 32):
                                                                                    else:
                                                                                    v6 = 0
                                                                                    if (0 >= load32(v20 + 44)):
                                                                                        break
                                                                                    v14 = (load32(v20 + 48) + (v6 * 548))
                                                                                if (v19 <= 0):
                                                                                    break
                                                                                if (u32(arg3) <= u32(v10)):
                                                                                    break
                                                                                v6 = load32(v17)
                                                                                while True:  # $label27
                                                                                    v7 = load32(v10)
                                                                                    store32((v6 + ((((load32(v10) * 506832829) & 0xFFFFFFFF) >> load32(v17 + 4)) << 2)), v7)
                                                                                    v10 = (v10 + 4)
                                                                                    if (u32((v10 + 4)) < u32(arg3)):
                                                                                        continue
                                                                                    break
                                                                                break
                                                                            if (v6 >= v30):
                                                                                break
                                                                            if (v19 <= 0):
                                                                                break
                                                                            if (u32(arg3) > u32(v10)):
                                                                                v7 = load32(v17)
                                                                                while True:  # $label29
                                                                                    v8 = load32(v10)
                                                                                    store32((v7 + ((((load32(v10) * 506832829) & 0xFFFFFFFF) >> load32(v17 + 4)) << 2)), v8)
                                                                                    v10 = (v10 + 4)
                                                                                    if (u32((v10 + 4)) < u32(arg3)):
                                                                                        continue
                                                                                    break
                                                                            v6 = (v6 - 280)
                                                                            if (((v6 - 280) & 0xFFFFFFFF) >> load32(v17 + 8)):
                                                                                break
                                                                            v6 = load32((load32(v17) + (v6 << 2)))
                                                                            break
                                                                            break
                                                                        a_c()
                                                                        raise Unreachable()
                                                                        break
                                                                    a_c()
                                                                    raise Unreachable()
                                                                    break
                                                                a_c()
                                                                raise Unreachable()
                                                                break
                                                            a_c()
                                                            raise Unreachable()
                                                            break
                                                        a_c()
                                                        raise Unreachable()
                                                        break
                                                    a_c()
                                                    raise Unreachable()
                                                    break
                                                store32(arg3, v6)
                                                break
                                            v6 = (arg3 + 4)
                                            v15 = (v15 + 1)
                                            if (arg2 > (v15 + 1)):
                                                arg3 = v6
                                                break
                                            v7 = (v13 + 1)
                                            while True:  # $label31
                                                if not arg5:
                                                    break
                                                if (arg4 <= v13):
                                                    break
                                                if (v7 & 15):
                                                    break
                                                break
                                            v15 = 0
                                            while True:  # $label32
                                                if (v19 <= 0):
                                                    break
                                                if (u32(v6) <= u32(v10)):
                                                    break
                                                v13 = load32(v17)
                                                while True:  # $label33
                                                    v8 = load32(v10)
                                                    store32((v13 + ((((load32(v10) * 506832829) & 0xFFFFFFFF) >> load32(v17 + 4)) << 2)), v8)
                                                    v8 = (u32(arg3) > u32(v10))
                                                    v10 = (v10 + 4)
                                                    if v8:
                                                        continue
                                                    break
                                                break
                                            arg3 = v6
                                            v13 = v7
                                            break
                                        if (u32(arg3) < u32(v26)):
                                            continue
                                        break
                                    break
                                arg2 = load32(arg0 + 40)
                                v6 = load32(arg0 + 36)
                                if (u32(load32(arg0 + 40)) > u32(load32(arg0 + 36))):
                                    break
                                while True:  # $label39
                                    while True:  # $label36
                                        while True:  # $label35
                                            if not load32(arg0 + 48):
                                                v10 = 0
                                                if (arg2 == v6):
                                                    v10 = (load32(arg0 + 44) > 64)
                                                store32(arg0 + 48, v10)
                                                if load32(arg0 + 56):
                                                    break
                                                break
                                            v10 = 1
                                            store32(arg0 + 48, 1)
                                            if not load32(arg0 + 56):
                                                break
                                            break
                                        arg2 = (u32(arg3) < u32(v26))
                                        v6 = ((u32(arg3) < u32(v26)) & (v10 != 0))
                                        if not (((u32(arg3) < u32(v26)) & (v10 != 0)) if arg2 else 1):
                                            break
                                        if v6:
                                            store32(arg0, 5)
                                            store64(v16, load64(arg0 + 64))
                                            store64(v16 + 24, load64(arg0 + 88))
                                            store64(v16 + 16, load64(arg0 + 80))
                                            store64(v16 + 8, load64(arg0 + 72))
                                            store32(arg0 + 112, load32(arg0 + 96))
                                            v10 = 1
                                            if (load32(arg0 + 120) <= 0):
                                                break
                                            func456((arg0 + 136), v25)
                                            return 1
                                        if (u32(arg3) >= u32(v26)):
                                            break
                                        break
                                    if v10:
                                        break
                                    break
                                if arg5:
                                store32(arg0, 0)
                                store32(arg0 + 112, ((arg3 - arg1) >> 2))
                                return 1
                                break
                            v10 = 0
                            while True:  # $label40
                                # br_table load32(arg0)
                                break
                                break
                            store32(arg0, 3)
                            break
                        return v10
                        break
                    a_c()
                    raise Unreachable()
                a_c()
                raise Unreachable()
            a_c()
            raise Unreachable()
            break
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()
    return 3160

# ----------------------------------------------------------
# $func276
# ----------------------------------------------------------
def func276(arg0, arg1, arg2, arg3, arg4):
    v7 = (G.global0 - 128)
    G.global0 = (G.global0 - 128)
    store64(v7 + 120, 0)
    store64(v7 + 112, 0)
    store64(v7 + 104, 0)
    store64(v7 + 96, 0)
    store64(v7 + 88, 0)
    store64(v7 + 80, 0)
    store64(v7 + 72, 0)
    store64(v7 + 64, 0)
    while True:  # $label13
        while True:  # $label3
            while True:  # $label18
                while True:  # $label10
                    while True:  # $label12
                        while True:  # $label5
                            while True:  # $label2
                                while True:  # $label1
                                    while True:  # $label0
                                        if arg3:
                                            if not arg2:
                                                break
                                            if not ((arg0 if arg4 else 0) if (arg0 | arg4) else 1):
                                                break
                                            if (arg1 <= 0):
                                                break
                                            if (arg3 > 0):
                                                while True:  # $label4
                                                    v6 = load32((arg2 + (v5 << 2)))
                                                    if (load32((arg2 + (v5 << 2))) > 15):
                                                        break
                                                    v6 = ((v7 - -64) + (v6 << 2))
                                                    store32(((v7 - -64) + (v6 << 2)), (load32(v6) + 1))
                                                    v5 = (v5 + 1)
                                                    if ((v5 + 1) != arg3):
                                                        continue
                                                    break
                                            else:
                                            if (0 == arg3):
                                                break
                                            store32(v7 + 4, 0)
                                            v6 = load32(v7 + 68)
                                            if (load32(v7 + 68) > 2):
                                                break
                                            store32(v7 + 8, v6)
                                            v5 = load32(v7 + 72)
                                            if (load32(v7 + 72) > 4):
                                                break
                                            v6 = (v5 + v6)
                                            store32(v7 + 12, (v5 + v6))
                                            v5 = load32(v7 + 76)
                                            if (load32(v7 + 76) > 8):
                                                break
                                            v6 = (v5 + v6)
                                            store32(v7 + 16, (v5 + v6))
                                            v5 = load32(v7 + 80)
                                            if (load32(v7 + 80) > 16):
                                                break
                                            v6 = (v5 + v6)
                                            store32(v7 + 20, (v5 + v6))
                                            v5 = load32(v7 + 84)
                                            if (load32(v7 + 84) > 32):
                                                break
                                            v6 = (v5 + v6)
                                            store32(v7 + 24, (v5 + v6))
                                            v5 = load32(v7 + 88)
                                            if (load32(v7 + 88) > 64):
                                                break
                                            v6 = (v5 + v6)
                                            store32(v7 + 28, (v5 + v6))
                                            v5 = load32(v7 + 92)
                                            if (load32(v7 + 92) > 128):
                                                break
                                            v6 = (v5 + v6)
                                            store32(v7 + 32, (v5 + v6))
                                            v5 = load32(v7 + 96)
                                            if (load32(v7 + 96) > 256):
                                                break
                                            v6 = (v5 + v6)
                                            store32(v7 + 36, (v5 + v6))
                                            v5 = load32(v7 + 100)
                                            if (load32(v7 + 100) > 512):
                                                break
                                            v6 = (v5 + v6)
                                            store32(v7 + 40, (v5 + v6))
                                            v5 = load32(v7 + 104)
                                            if (load32(v7 + 104) > 1024):
                                                break
                                            v6 = (v5 + v6)
                                            store32(v7 + 44, (v5 + v6))
                                            v5 = load32(v7 + 108)
                                            if (load32(v7 + 108) > 2048):
                                                break
                                            v6 = (v5 + v6)
                                            store32(v7 + 48, (v5 + v6))
                                            v5 = load32(v7 + 112)
                                            if (load32(v7 + 112) > 4096):
                                                break
                                            v6 = (v5 + v6)
                                            store32(v7 + 52, (v5 + v6))
                                            v5 = load32(v7 + 116)
                                            if (load32(v7 + 116) > 8192):
                                                break
                                            v6 = (v5 + v6)
                                            store32(v7 + 56, (v5 + v6))
                                            v5 = load32(v7 + 120)
                                            if (load32(v7 + 120) > 16384):
                                                break
                                            v13 = (v5 + v6)
                                            store32(v7 + 60, (v5 + v6))
                                            v5 = 0
                                            if (arg3 > 0):
                                                while True:  # $label7
                                                    if arg4:
                                                        while True:  # $label6
                                                            v6 = load32((arg2 + (v5 << 2)))
                                                            if (load32((arg2 + (v5 << 2))) > 0):
                                                                v8 = (v7 + (v6 << 2))
                                                                v6 = load32((v7 + (v6 << 2)))
                                                                if (load32((v7 + (v6 << 2))) >= arg3):
                                                                    break
                                                                store32(v8, (v6 + 1))
                                                                store16((arg4 + (v6 << 1)), v5)
                                                            v5 = (v5 + 1)
                                                            if ((v5 + 1) != arg3):
                                                                continue
                                                            break
                                                            break
                                                        raise Unreachable()
                                                    if (arg3 != 1):
                                                        v6 = (arg3 & -2)
                                                        while True:  # $label8
                                                            v10 = (v5 << 2)
                                                            v9 = load32((arg2 + (v5 << 2)))
                                                            if (load32((arg2 + (v5 << 2))) > 0):
                                                                v9 = (v7 + (v9 << 2))
                                                                store32((v7 + (v9 << 2)), (load32(v9) + 1))
                                                            v10 = load32((arg2 + (v10 | 4)))
                                                            if (load32((arg2 + (v10 | 4))) > 0):
                                                                v10 = (v7 + (v10 << 2))
                                                                store32((v7 + (v10 << 2)), (load32(v10) + 1))
                                                            v5 = (v5 + 2)
                                                            v8 = (v8 + 2)
                                                            if ((v8 + 2) != v6):
                                                                continue
                                                            break
                                                    if not (arg3 & 1):
                                                        break
                                                    arg2 = load32((arg2 + (v5 << 2)))
                                                    if (load32((arg2 + (v5 << 2))) <= 0):
                                                        break
                                                    arg2 = (v7 + (arg2 << 2))
                                                    store32((v7 + (arg2 << 2)), (load32(arg2) + 1))
                                                    break
                                                v13 = load32(v7 + 60)
                                            v6 = (1 << arg1)
                                            v16 = 1
                                            if (v13 == 1):
                                                if not arg4:
                                                    v11 = v6
                                                    break
                                                arg2 = (load16u(arg4) << 16)
                                                v5 = v6
                                                while True:  # $label9
                                                    arg1 = (v5 - 1)
                                                    store32((arg0 + ((v5 - 1) << 2)), arg2)
                                                    arg3 = (v5 > 1)
                                                    v5 = arg1
                                                    if arg3:
                                                        continue
                                                    break
                                                v11 = v6
                                                break
                                            v14 = 1
                                            arg3 = 0
                                            v9 = 0
                                            if (arg1 <= 0):
                                                break
                                            if not arg0:
                                                v5 = 1
                                                while True:  # $label11
                                                    arg2 = (v16 << 1)
                                                    v16 = ((v16 << 1) - load32(((v7 - -64) + (v5 << 2))))
                                                    if (((v16 << 1) - load32(((v7 - -64) + (v5 << 2)))) < 0):
                                                        break
                                                    v14 = (arg2 + v14)
                                                    arg2 = (arg1 != v5)
                                                    v5 = (v5 + 1)
                                                    if arg2:
                                                        continue
                                                    break
                                                break
                                            v15 = 2
                                            v12 = 1
                                            while True:  # $label17
                                                v18 = (v16 << 1)
                                                v19 = ((v7 - -64) + (v12 << 2))
                                                arg2 = load32(((v7 - -64) + (v12 << 2)))
                                                v16 = ((v16 << 1) - load32(((v7 - -64) + (v12 << 2))))
                                                if (((v16 << 1) - load32(((v7 - -64) + (v12 << 2)))) < 0):
                                                    break
                                                if (arg2 > 0):
                                                    if ((v15 - 1) & v6):
                                                        break
                                                    v20 = (v12 & 255)
                                                    v17 = (1 << (v12 - 1))
                                                    v10 = (arg2 + v9)
                                                    while True:  # $label16
                                                        arg2 = (arg0 + (arg3 << 2))
                                                        v8 = ((load16u((arg4 + (v9 << 1))) << 16) | v20)
                                                        v5 = v6
                                                        while True:  # $label14
                                                            v5 = (v5 - v15)
                                                            store32((arg2 + ((v5 - v15) << 2)), v8)
                                                            if (v5 > 0):
                                                                continue
                                                            break
                                                        v8 = v17
                                                        while True:  # $label15
                                                            arg2 = v8
                                                            v8 = ((v8 & 0xFFFFFFFF) >> 1)
                                                            if (arg2 & arg3):
                                                                continue
                                                            break
                                                        arg3 = ((((arg2 - 1) & arg3) + arg2) if arg2 else arg3)
                                                        v9 = (v9 + 1)
                                                        if ((v9 + 1) != v10):
                                                            continue
                                                        break
                                                    store32(v19, 0)
                                                    v9 = v10
                                                v14 = (v14 + v18)
                                                v15 = (v15 << 1)
                                                arg2 = (arg1 == v12)
                                                v12 = (v12 + 1)
                                                if not arg2:
                                                    continue
                                                break
                                            break
                                        a_c()
                                        raise Unreachable()
                                        break
                                    a_c()
                                    raise Unreachable()
                                    break
                                a_c()
                                raise Unreachable()
                                break
                            a_c()
                            raise Unreachable()
                            break
                        a_c()
                        raise Unreachable()
                        break
                    if (arg1 <= 14):
                        break
                    v17 = v6
                    break
                    break
                v22 = (v6 - 1)
                v10 = -1
                v15 = 2
                v12 = arg0
                v13 = arg1
                v17 = v6
                while True:  # $label27
                    v11 = 0
                    v23 = (v16 << 1)
                    v18 = (v13 + 1)
                    v21 = ((v7 - -64) + ((v13 + 1) << 2))
                    arg2 = load32(((v7 - -64) + ((v13 + 1) << 2)))
                    v16 = ((v16 << 1) - load32(((v7 - -64) + ((v13 + 1) << 2))))
                    if (((v16 << 1) - load32(((v7 - -64) + ((v13 + 1) << 2)))) < 0):
                        break
                    if (arg2 > 0):
                        v20 = (1 << v13)
                        v24 = (v15 - 1)
                        v19 = (v18 - arg1)
                        v25 = ((v18 - arg1) & 255)
                        v26 = (1 << v19)
                        while True:  # $label26
                            while True:  # $label22
                                while True:  # $label23
                                    while True:  # $label21
                                        v11 = (arg3 & v22)
                                        if (v10 != (arg3 & v22)):
                                            v5 = v18
                                            v8 = v26
                                            arg2 = v26
                                            v10 = v19
                                            if (v13 <= 13):
                                                while True:  # $label20
                                                    while True:  # $label19
                                                        arg2 = (v8 - load32(((v7 - -64) + (v5 << 2))))
                                                        if ((v8 - load32(((v7 - -64) + (v5 << 2)))) <= 0):
                                                            arg2 = v5
                                                            break
                                                        v8 = (arg2 << 1)
                                                        arg2 = 15
                                                        v5 = (v5 + 1)
                                                        if ((v5 + 1) != 15):
                                                            continue
                                                        break
                                                    break
                                                v10 = (arg2 - arg1)
                                                arg2 = (1 << (arg2 - arg1))
                                            v17 = (arg2 + v17)
                                            if arg0:
                                                break
                                            v6 = arg2
                                            v10 = v11
                                            break
                                        if arg0:
                                            break
                                        break
                                        break
                                    v5 = (arg0 + (v11 << 2))
                                    store8((arg0 + (v11 << 2)), (arg1 + v10))
                                    v5 = (v12 + (v6 << 2))
                                    store16(v5 + 2, ((((((v12 + (v6 << 2)) if arg0 else v12) - arg0) & 0xFFFFFFFF) >> 2) - v11))
                                    v6 = arg2
                                    v10 = v11
                                    v12 = v5
                                    break
                                if (v6 & v24):
                                    break
                                arg2 = (v9 + 1)
                                v8 = (v12 + (((arg3 & 0xFFFFFFFF) >> arg1) << 2))
                                v9 = ((load16u((arg4 + (v9 << 1))) << 16) | v25)
                                v5 = v6
                                while True:  # $label24
                                    v5 = (v5 - v15)
                                    store32((v8 + ((v5 - v15) << 2)), v9)
                                    if (v5 > 0):
                                        continue
                                    break
                                v9 = arg2
                                break
                            v8 = v20
                            while True:  # $label25
                                arg2 = v8
                                v8 = ((v8 & 0xFFFFFFFF) >> 1)
                                if (arg2 & arg3):
                                    continue
                                break
                            v5 = load32(v21)
                            store32(v21, (load32(v21) - 1))
                            arg3 = ((((arg2 - 1) & arg3) + arg2) if arg2 else arg3)
                            if (v5 > 1):
                                continue
                            break
                    v14 = (v14 + v23)
                    v15 = (v15 << 1)
                    v13 = v18
                    if (v18 != 15):
                        continue
                    break
                v13 = load32(v7 + 60)
                break
            v11 = (v17 if (((v13 << 1) - 1) == v14) else 0)
            break
        G.global0 = (v7 + 128)
        return v11
        break
    a_c()
    raise Unreachable()
    return 4694

# ----------------------------------------------------------
# $func277
# ----------------------------------------------------------
def func277(arg0, arg1, arg2):
    v6 = load32(9142440)
    v7 = (load32(9142440) + 2)
    v8 = load32(39056)
    v9 = load32(38632)
    v10 = load32(38628)
    v11 = load32(38624)
    v12 = load32(38616)
    v13 = load32(38612)
    v14 = load32(38608)
    v15 = load32(38604)
    v16 = load32(38472)
    v17 = load32(38600)
    v18 = load32(ENTITIES)
    v19 = load32(9142840)
    while True:  # $label2
        while True:  # $label1
            while True:  # $label0
                v4 = (v5 << 3)
                v3 = (load32(((v5 << 3) + 9172)) + arg1)
                if (u32(v6) <= u32((load32(((v5 << 3) + 9172)) + arg1))):
                    break
                v4 = (load32((v4 + 9168)) + arg0)
                if (u32(v6) <= u32((load32((v4 + 9168)) + arg0))):
                    break
                if ((v3 | v4) < 0):
                    break
                v3 = load32((((v4 + (((v3 + v7) + 1) * v7)) << 2) + v19) + 4)
                if (u32(load32((((v4 + (((v3 + v7) + 1) * v7)) << 2) + v19) + 4)) < u32(3)):
                    break
                v3 = (v18 + (v3 * 132))
                if (load16u((v18 + (v3 * 132)) + 110) != arg2):
                    break
                v4 = 1
                v3 = load8u(v3 + 122)
                if (v17 == load8u(v3 + 122)):
                    break
                if (v3 == v16):
                    break
                if (v3 == v15):
                    break
                if (v3 == v14):
                    break
                if (v3 == v13):
                    break
                if (v3 == v12):
                    break
                if (v3 == v11):
                    break
                if (v3 == v10):
                    break
                if (v3 == v9):
                    break
                if (v3 == v8):
                    break
                break
            v4 = 0
            break
        store8((v5 + 9147328), v4)
        v5 = (v5 + 1)
        if ((v5 + 1) != 8):
            continue
        break

# ----------------------------------------------------------
# $func278
# ----------------------------------------------------------
def func278(arg0, arg1):
    if not arg0:
        return 0
    while True:  # $label2
        while True:  # $label0
            if arg0:
                if (u32(arg1) <= u32(127)):
                    break
                while True:  # $label1
                    if not load32(load32(G.global3 + 96)):
                        if ((arg1 & -128) == 57216):
                            break
                        break
                    if (u32(arg1) <= u32(2047)):
                        store8(arg0 + 1, ((arg1 & 63) | 128))
                        store8(arg0, (((arg1 & 0xFFFFFFFF) >> 6) | 192))
                        break
                    if not (((arg1 & -8192) != 57344) & (u32(arg1) >= u32(55296))):
                        store8(arg0 + 2, ((arg1 & 63) | 128))
                        store8(arg0, (((arg1 & 0xFFFFFFFF) >> 12) | 224))
                        store8(arg0 + 1, ((((arg1 & 0xFFFFFFFF) >> 6) & 63) | 128))
                        break
                    if (u32((arg1 - 65536)) <= u32(1048575)):
                        store8(arg0 + 3, ((arg1 & 63) | 128))
                        store8(arg0, (((arg1 & 0xFFFFFFFF) >> 18) | 240))
                        store8(arg0 + 2, ((((arg1 & 0xFFFFFFFF) >> 6) & 63) | 128))
                        store8(arg0 + 1, ((((arg1 & 0xFFFFFFFF) >> 12) & 63) | 128))
                        break
                    break
                store32(G.global3 + 28, 25)
            else:
            break
            break
        store8(arg0, arg1)
        break
    return 1

# ----------------------------------------------------------
# $func280
# ----------------------------------------------------------
def func280(arg0):
    while True:  # $label3
        while True:  # $label1
            while True:  # $label0
                v1 = load32(9568064)
                v2 = ((load32(9568068) - load32(9568064)) >> 7)
                v3 = (((load32(9568068) - load32(9568064)) >> 7) + 1)
                if (u32((((load32(9568068) - load32(9568064)) >> 7) + 1)) < u32(33554432)):
                    v1 = (load32(9568072) - v1)
                    v4 = ((load32(9568072) - v1) >> 6)
                    v3 = (33554431 if (u32(v1) >= u32(2147483520)) else (((load32(9568072) - v1) >> 6) if (u32(v3) < u32(v4)) else v3))
                    if (33554431 if (u32(v1) >= u32(2147483520)) else (((load32(9568072) - v1) >> 6) if (u32(v3) < u32(v4)) else v3)):
                        if (u32(v3) >= u32(33554432)):
                            break
                    else:
                    v1 = 0
                    v4 = (v1 + (v3 << 7))
                    v3 = func226((v1 + (v2 << 7)), arg0)
                    v5 = (func226((v1 + (v2 << 7)), arg0) + 128)
                    arg0 = load32(9568068)
                    v6 = load32(9568064)
                    if (load32(9568068) == load32(9568064)):
                        break
                    while True:  # $label2
                        v1 = (v3 - 128)
                        store64((v3 - 128), 0)
                        store32(v1 + 8, 0)
                        v2 = (arg0 - 128)
                        store32(v1, load32((arg0 - 128)))
                        store32(v1 + 4, load32(v2 + 4))
                        store32(v1 + 8, load32(v2 + 8))
                        store32(v2 + 8, 0)
                        store64(v2, 0)
                        store32(v1 + 20, 0)
                        store64(v1 + 12, 0)
                        store32(v1 + 12, load32(v2 + 12))
                        store32(v1 + 16, load32(v2 + 16))
                        store32(v1 + 20, load32(v2 + 20))
                        store32(v2 + 20, 0)
                        store64(v2 + 12, 0)
                        # TODO: memory.copy
                        v3 = v1
                        arg0 = v2
                        if (v2 != v6):
                            continue
                        break
                    store32(9568072, v4)
                    v3 = load32(9568068)
                    store32(9568068, v5)
                    arg0 = load32(9568064)
                    store32(9568064, v1)
                    if (arg0 == v3):
                        break
                    while True:  # $label4
                        v1 = (v3 - 128)
                        v2 = load32((v3 - 128) + 12)
                        if load32((v3 - 128) + 12):
                            store32((v3 - 112), v2)
                        v2 = load32(v1)
                        if load32(v1):
                            store32((v3 - 124), v2)
                        v3 = v1
                        if (v1 != arg0):
                            continue
                        break
                    break
                func42()
                raise Unreachable()
                break
            func68()
            raise Unreachable()
            break
        store32(9568072, v4)
        store32(9568068, v5)
        store32(9568064, v3)
        break
    if arg0:
    return af(arg0)

# ----------------------------------------------------------
# $func281
# ----------------------------------------------------------
def func281(arg0, arg1, arg2):
    while True:  # $label3
        while True:  # $label1
            while True:  # $label0
                v4 = load32(arg0 + 4)
                v8 = load32(arg0)
                v3 = ((load32(arg0 + 4) - load32(arg0)) >> 5)
                v5 = (((load32(arg0 + 4) - load32(arg0)) >> 5) + 1)
                if (u32((((load32(arg0 + 4) - load32(arg0)) >> 5) + 1)) < u32(134217728)):
                    v6 = (load32(arg0 + 8) - v8)
                    v7 = ((load32(arg0 + 8) - v8) >> 4)
                    v5 = (134217727 if (u32(v6) >= u32(2147483616)) else (((load32(arg0 + 8) - v8) >> 4) if (u32(v5) < u32(v7)) else v5))
                    if (134217727 if (u32(v6) >= u32(2147483616)) else (((load32(arg0 + 8) - v8) >> 4) if (u32(v5) < u32(v7)) else v5)):
                        if (u32(v5) >= u32(134217728)):
                            break
                    else:
                    v6 = 0
                    v7 = load32(arg1)
                    arg1 = load32(arg2)
                    v3 = (v6 + (v3 << 5))
                    store64((v6 + (v3 << 5)) + 8, 0)
                    store32(v3 + 4, arg1)
                    store32(v3, v7)
                    store64(v3 + 16, 0)
                    store64(v3 + 24, 0)
                    arg2 = func26(16)
                    store32(func26(16) + 12, arg1)
                    store32(arg2 + 8, v7)
                    store64(arg2, 0)
                    arg1 = (arg2 + 16)
                    store32(v3 + 28, (arg2 + 16))
                    store32(v3 + 24, arg1)
                    store32(v3 + 20, arg2)
                    arg2 = (v6 + (v5 << 5))
                    arg1 = (v3 + 32)
                    if (v4 == v8):
                        break
                    while True:  # $label2
                        v3 = (v3 - 32)
                        v4 = (v4 - 32)
                        store64((v3 - 32), load64((v4 - 32)))
                        store32(v3 + 8, load32(v4 + 8))
                        store32(v3 + 12, load32(v4 + 12))
                        store32(v3 + 16, load32(v4 + 16))
                        store32(v4 + 16, 0)
                        store64(v4 + 8, 0)
                        store32(v3 + 20, load32(v4 + 20))
                        store32(v3 + 24, load32(v4 + 24))
                        store32(v3 + 28, load32(v4 + 28))
                        store32(v4 + 28, 0)
                        store64(v4 + 20, 0)
                        if (v4 != v8):
                            continue
                        break
                    store32(arg0 + 8, arg2)
                    arg2 = load32(arg0 + 4)
                    store32(arg0 + 4, arg1)
                    v4 = load32(arg0)
                    store32(arg0, v3)
                    if (arg2 == v4):
                        break
                    while True:  # $label4
                        arg0 = (arg2 - 32)
                        arg1 = load32((arg2 - 32) + 20)
                        if load32((arg2 - 32) + 20):
                            store32((arg2 - 8), arg1)
                        arg1 = load32((arg2 - 24))
                        if load32((arg2 - 24)):
                            store32((arg2 - 20), arg1)
                        arg2 = arg0
                        if (arg0 != v4):
                            continue
                        break
                    break
                func42()
                raise Unreachable()
                break
            func68()
            raise Unreachable()
            break
        store32(arg0 + 8, arg2)
        store32(arg0 + 4, arg1)
        store32(arg0, v3)
        break
    if v4:
    return af(v4)

# ----------------------------------------------------------
# $func282
# ----------------------------------------------------------
def func282(arg0, arg1, arg2, arg3, arg4, arg5):
    v6 = load32(arg2 + 220)
    v10 = load32(arg2 + 216)
    v16 = load32(arg2 + 372)
    while True:  # $label2
        while True:  # $label7
            if arg5:
                v13 = (arg1 + v6)
                v17 = (arg0 + v10)
                while True:  # $label0
                    if (v10 <= 0):
                        break
                    if (v6 <= 0):
                        break
                    v14 = load32(9142440)
                    v11 = (load32(9142440) + 2)
                    v21 = ((load32(9142440) + 2) * load32(arg2 + 208))
                    v12 = load32(9142840)
                    v7 = arg0
                    while True:  # $label6
                        v8 = (v7 + 1)
                        v15 = (v7 - arg0)
                        arg5 = arg1
                        while True:  # $label4
                            if (u32(v7) < u32(v14)):
                                while True:  # $label3
                                    while True:  # $label1
                                        if not load8u((v16 + (v15 + ((arg5 - arg1) * v10)))):
                                            arg5 = (arg5 + 1)
                                            break
                                        if (u32(arg5) >= u32(v14)):
                                            break
                                        if ((arg5 | v7) < 0):
                                            break
                                        arg5 = (arg5 + 1)
                                        v18 = load32((v12 + ((((v21 + (arg5 + 1)) * v11) + v8) << 2)))
                                        if (u32(load32((v12 + ((((v21 + (arg5 + 1)) * v11) + v8) << 2)))) > u32(2)):
                                            break
                                        if (u32(load32((v12 + (((arg5 * v11) + v8) << 2)))) > u32(2)):
                                            break
                                        if (u32(load32((v12 + ((((arg5 + v11) * v11) + v8) << 2)))) > u32(2)):
                                            break
                                        v19 = (not v18 | v19)
                                        v20 = (v20 + (v18 == 1))
                                        break
                                    if (arg5 < v13):
                                        continue
                                    break
                                break
                            while True:  # $label5
                                if not load8u((v16 + (v15 + ((arg5 - arg1) * v10)))):
                                    arg5 = (arg5 + 1)
                                    if (v13 > (arg5 + 1)):
                                        continue
                                    break
                                break
                            break
                            break
                        v7 = v8
                        if (v8 < v17):
                            continue
                        break
                    break
                arg5 = ((v19 ^ 1) | (u32(v20) < u32((((v6 * v10) // 2) - 1))))
                v9 = (((v19 ^ 1) | (u32(v20) < u32((((v6 * v10) // 2) - 1)))) ^ 1)
                if (arg5 & 1):
                    break
                if arg3:
                    break
                break
            v9 = 1
            if not arg3:
                break
            v13 = (arg1 + v6)
            v17 = (arg0 + v10)
            break
        v9 = 1
        if (v10 <= 0):
            break
        if (v6 <= 0):
            break
        v7 = arg0
        while True:  # $label11
            arg3 = (v7 + 1)
            v12 = (v7 - arg0)
            v14 = load32(9140332)
            v15 = load32(9147288)
            v6 = load32(9142840)
            arg5 = arg1
            while True:  # $label10
                while True:  # $label8
                    if not load8u((v16 + (v12 + ((arg5 - arg1) * v10)))):
                        arg5 = (arg5 + 1)
                        break
                    v11 = load32(9142440)
                    if (arg4 != load32(arg2 + 212)):
                        v8 = (v11 + 2)
                        arg5 = (arg5 + 1)
                        store32((v6 + (((((v11 + 2) + (arg5 + 1)) * v8) + arg3) << 2)), arg4)
                        store32((v6 + ((((load32(9142440) + 2) * arg5) + arg3) << 2)), arg4)
                        break
                    v9 = (v11 + 2)
                    v8 = (arg5 + 1)
                    v9 = (v6 + (((((v11 + 2) + (arg5 + 1)) * v9) + arg3) << 2))
                    while True:  # $label9
                        arg5 = load8s((v15 + ((arg5 * v11) + v7)))
                        if (load32(load32((v14 + (((load8s((v15 + ((arg5 * v11) + v7))) ^ ((arg5 & 0xFFFFFFFF) >> 7)) & 255) << 2))) + 32) != 23):
                            store32(v9, 0)
                            store32((v6 + ((((load32(9142440) + 2) * v8) + arg3) << 2)), 0)
                            break
                        store32(v9, 1)
                        store32((v6 + ((((load32(9142440) + 2) * v8) + arg3) << 2)), 1)
                        break
                    arg5 = v8
                    break
                if (arg5 < v13):
                    continue
                break
            v7 = arg3
            if (arg3 < v17):
                continue
            break
        v9 = 1
        break
    return (v9 & 1)

# ----------------------------------------------------------
# $func283
# ----------------------------------------------------------
def func283(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    v9 = load32(arg2 + 216)
    v14 = load32(arg2 + 208)
    while True:  # $label1
        while True:  # $label0
            if not arg5:
                break
            if (v9 <= 0):
                break
            v8 = (arg0 + v9)
            v13 = (load32(arg2 + 220) + arg1)
            if (arg1 < (load32(arg2 + 220) + arg1)):
                v11 = load32(9142440)
                v15 = (load32(9142440) + 2)
                v16 = ((load32(9142440) + 2) * v14)
                v17 = load32(9142840)
                v7 = arg0
                while True:  # $label2
                    if (u32(v7) >= u32(v11)):
                        break
                    v10 = (v7 + 1)
                    arg5 = arg1
                    while True:  # $label3
                        if (arg5 == v13):
                            v7 = v10
                            if (v10 < v8):
                                continue
                            break
                        if (u32(arg5) >= u32(v11)):
                            break
                        if ((arg5 | v7) < 0):
                            break
                        arg5 = (arg5 + 1)
                        if (u32(load32((v17 + ((v10 + ((v16 + (arg5 + 1)) * v15)) << 2)))) <= u32(2)):
                            continue
                        break
                    break
                break
            arg5 = arg0
            while True:  # $label4
                arg5 = (arg5 + 1)
                if ((arg5 + 1) < v8):
                    continue
                break
            break
        v12 = 1
        if not arg3:
            break
        if (v9 <= 0):
            break
        v11 = (load32(arg2 + 220) + arg1)
        if ((load32(arg2 + 220) + arg1) <= arg1):
            break
        v12 = (arg0 + v9)
        arg5 = arg0
        while True:  # $label10
            v7 = (arg5 + 1)
            v10 = (arg5 - arg0)
            arg5 = arg1
            while True:  # $label9
                while True:  # $label6
                    if (arg4 != load32(arg2 + 212)):
                        while True:  # $label5
                            if arg6:
                                if not load8u((load32(arg2 + 372) + (v10 + ((arg5 - arg1) * v9)))):
                                    break
                            arg5 = (arg5 + 1)
                            arg3 = (load32(9142440) + 2)
                            store32((load32(9142840) + ((v7 + (((arg5 + 1) + ((load32(9142440) + 2) * v14)) * arg3)) << 2)), arg4)
                            break
                            break
                        arg5 = (arg5 + 1)
                        arg3 = (load32(9142440) + 2)
                        arg3 = (load32(9142840) + ((v7 + (((arg5 + 1) + (load32(9142440) + 2)) * arg3)) << 2))
                        if (u32(load32((load32(9142840) + ((v7 + (((arg5 + 1) + (load32(9142440) + 2)) * arg3)) << 2)))) > u32(2)):
                            break
                        store32(arg3, 0)
                        break
                    while True:  # $label7
                        if not arg6:
                            arg3 = (arg5 + 1)
                            break
                        arg3 = (arg5 + 1)
                        v8 = (load32(9142440) + 2)
                        v8 = load32((load32(9142840) + ((v7 + (((arg5 + 1) + (load32(9142440) + 2)) * v8)) << 2)))
                        if (u32(load32((load32(9142840) + ((v7 + (((arg5 + 1) + (load32(9142440) + 2)) * v8)) << 2)))) < u32(3)):
                            break
                        if load8u((load32(arg2 + 372) + (v10 + ((arg5 - arg1) * v9)))):
                            break
                        break
                    v13 = load32(9142840)
                    arg5 = (load32(9142440) + 2)
                    v8 = (load32(9142840) + (((((load32(9142440) + 2) + arg3) * arg5) + v7) << 2))
                    while True:  # $label8
                        if (load32((v13 + (((arg3 * arg5) + v7) << 2))) != 1):
                            store32(v8, 0)
                            break
                        store32(v8, 1)
                        break
                    arg5 = arg3
                    break
                if (arg5 != v11):
                    continue
                break
            arg5 = v7
            if (v7 < v12):
                continue
            break
        v12 = 1
        break
    return v12

# ----------------------------------------------------------
# $func284
# ----------------------------------------------------------
def func284(arg0):
    v2 = load32(9568064)
    if (load32(9568064) != load32(9568068)):
        while True:  # $label26
            v11 = 0
            v12 = (v2 + (v15 << 7))
            v2 = load32(v12)
            if (load32((v2 + (v15 << 7)) + 4) != load32(v12)):
                while True:  # $label12
                    while True:  # $label0
                        v4 = (v2 + (v11 * 196))
                        v5 = load32((v2 + (v11 * 196)) + 56)
                        if not load32((v2 + (v11 * 196)) + 56):
                            break
                        v6 = (v5 - 1)
                        v2 = load32(v4 + 48)
                        v9 = (load32(PLAYER_COUNT) + 1)
                        if (u32((load32(PLAYER_COUNT) + 1)) >= u32(v5)):
                            v10 = (v2 + (v6 << 2))
                            while True:  # $label1
                                if not v6:
                                    v3 = 0
                                    break
                                v7 = 0
                                v1 = 0
                                v3 = 0
                                if (u32((v5 - 2)) >= u32(3)):
                                    v13 = (v6 & -4)
                                    v5 = 0
                                    while True:  # $label2
                                        v8 = (v1 << 2)
                                        v3 = (load32((v2 + ((v1 << 2) | 12))) + (load32((v2 + (v8 | 8))) + (load32((v2 + (v8 | 4))) + (load32((v2 + v8)) + v3))))
                                        v1 = (v1 + 4)
                                        v5 = (v5 + 4)
                                        if ((v5 + 4) != v13):
                                            continue
                                        break
                                v5 = (v6 & 3)
                                if not (v6 & 3):
                                    break
                                while True:  # $label3
                                    v3 = (load32((v2 + (v1 << 2))) + v3)
                                    v1 = (v1 + 1)
                                    v7 = (v7 + 1)
                                    if ((v7 + 1) != v5):
                                        continue
                                    break
                                break
                            v7 = load32(v10)
                            v5 = (u32(v3) > u32(((v6 & 0xFFFFFFFF) >> 1)))
                            store32(v10, (u32(v3) > u32(((v6 & 0xFFFFFFFF) >> 1))))
                            v1 = load32(v4 + 56)
                            if (u32(v9) > u32(load32(v4 + 56))):
                                while True:  # $label4
                                    if (load32(v4 + 52) == v1):
                                        v3 = (load32(v4 + 60) + v1)
                                        store32(v4 + 52, (load32(v4 + 60) + v1))
                                        v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                                        if v1:
                                            # TODO: memory.copy
                                        v1 = load32(v4 + 56)
                                        store32(v4 + 48, v3)
                                        v2 = v3
                                    store32(v4 + 56, (v1 + 1))
                                    store32((v2 + (v1 << 2)), v5)
                                    v1 = load32(v4 + 56)
                                    if (u32(load32(v4 + 56)) < u32(v9)):
                                        continue
                                    break
                            store32((v2 + (load32(PLAYER_COUNT) << 2)), v7)
                            break
                        store32(v4 + 56, v6)
                        v1 = arg0
                        if (u32(v6) <= u32(arg0)):
                            break
                        while True:  # $label5
                            v1 = (v1 + 1)
                            store32((v2 + (v1 << 2)), load32((v2 + ((v1 + 1) << 2))))
                            if (u32(v1) < u32(load32(v4 + 56))):
                                continue
                            break
                        break
                    while True:  # $label6
                        v5 = load32(v4 + 72)
                        if not load32(v4 + 72):
                            break
                        v6 = (v5 - 1)
                        v13 = (v4 - -64)
                        v2 = load32((v4 - -64))
                        v9 = (load32(PLAYER_COUNT) + 1)
                        if (u32((load32(PLAYER_COUNT) + 1)) >= u32(v5)):
                            v10 = (v2 + (v6 << 2))
                            while True:  # $label7
                                if not v6:
                                    v3 = 0
                                    break
                                v7 = 0
                                v1 = 0
                                v3 = 0
                                if (u32((v5 - 2)) >= u32(3)):
                                    v14 = (v6 & -4)
                                    v5 = 0
                                    while True:  # $label8
                                        v8 = (v1 << 2)
                                        v3 = (load32((v2 + ((v1 << 2) | 12))) + (load32((v2 + (v8 | 8))) + (load32((v2 + (v8 | 4))) + (load32((v2 + v8)) + v3))))
                                        v1 = (v1 + 4)
                                        v5 = (v5 + 4)
                                        if ((v5 + 4) != v14):
                                            continue
                                        break
                                v5 = (v6 & 3)
                                if not (v6 & 3):
                                    break
                                while True:  # $label9
                                    v3 = (load32((v2 + (v1 << 2))) + v3)
                                    v1 = (v1 + 1)
                                    v7 = (v7 + 1)
                                    if ((v7 + 1) != v5):
                                        continue
                                    break
                                break
                            v7 = load32(v10)
                            v5 = (u32(v3) > u32(((v6 & 0xFFFFFFFF) >> 1)))
                            store32(v10, (u32(v3) > u32(((v6 & 0xFFFFFFFF) >> 1))))
                            v1 = load32(v4 + 72)
                            if (u32(v9) > u32(load32(v4 + 72))):
                                while True:  # $label10
                                    if (load32(v4 + 68) == v1):
                                        v3 = (load32(v4 + 76) + v1)
                                        store32(v4 + 68, (load32(v4 + 76) + v1))
                                        v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                                        if v1:
                                            # TODO: memory.copy
                                        v1 = load32(v4 + 72)
                                        store32(v13, v3)
                                        v2 = v3
                                    store32(v4 + 72, (v1 + 1))
                                    store32((v2 + (v1 << 2)), v5)
                                    v1 = load32(v4 + 72)
                                    if (u32(load32(v4 + 72)) < u32(v9)):
                                        continue
                                    break
                            store32((v2 + (load32(PLAYER_COUNT) << 2)), v7)
                            break
                        store32(v4 + 72, v6)
                        v1 = arg0
                        if (u32(v6) <= u32(arg0)):
                            break
                        while True:  # $label11
                            v1 = (v1 + 1)
                            store32((v2 + (v1 << 2)), load32((v2 + ((v1 + 1) << 2))))
                            if (u32(v1) < u32(load32(v4 + 72))):
                                continue
                            break
                        break
                    v11 = (v11 + 1)
                    v2 = load32(v12)
                    if (u32((v11 + 1)) < u32(((load32(v12 + 4) - load32(v12)) // 196))):
                        continue
                    break
            v2 = load32(v12 + 12)
            if (load32(v12 + 12) != load32(v12 + 16)):
                v11 = 0
                while True:  # $label25
                    while True:  # $label13
                        v4 = (v2 + (v11 * 196))
                        v5 = load32((v2 + (v11 * 196)) + 56)
                        if not load32((v2 + (v11 * 196)) + 56):
                            break
                        v6 = (v5 - 1)
                        v2 = load32(v4 + 48)
                        v9 = (load32(PLAYER_COUNT) + 1)
                        if (u32((load32(PLAYER_COUNT) + 1)) >= u32(v5)):
                            v10 = (v2 + (v6 << 2))
                            while True:  # $label14
                                if not v6:
                                    v3 = 0
                                    break
                                v7 = 0
                                v1 = 0
                                v3 = 0
                                if (u32((v5 - 2)) >= u32(3)):
                                    v13 = (v6 & -4)
                                    v5 = 0
                                    while True:  # $label15
                                        v8 = (v1 << 2)
                                        v3 = (load32((v2 + ((v1 << 2) | 12))) + (load32((v2 + (v8 | 8))) + (load32((v2 + (v8 | 4))) + (load32((v2 + v8)) + v3))))
                                        v1 = (v1 + 4)
                                        v5 = (v5 + 4)
                                        if ((v5 + 4) != v13):
                                            continue
                                        break
                                v5 = (v6 & 3)
                                if not (v6 & 3):
                                    break
                                while True:  # $label16
                                    v3 = (load32((v2 + (v1 << 2))) + v3)
                                    v1 = (v1 + 1)
                                    v7 = (v7 + 1)
                                    if ((v7 + 1) != v5):
                                        continue
                                    break
                                break
                            v7 = load32(v10)
                            v5 = (u32(v3) > u32(((v6 & 0xFFFFFFFF) >> 1)))
                            store32(v10, (u32(v3) > u32(((v6 & 0xFFFFFFFF) >> 1))))
                            v1 = load32(v4 + 56)
                            if (u32(v9) > u32(load32(v4 + 56))):
                                while True:  # $label17
                                    if (load32(v4 + 52) == v1):
                                        v3 = (load32(v4 + 60) + v1)
                                        store32(v4 + 52, (load32(v4 + 60) + v1))
                                        v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                                        if v1:
                                            # TODO: memory.copy
                                        v1 = load32(v4 + 56)
                                        store32(v4 + 48, v3)
                                        v2 = v3
                                    store32(v4 + 56, (v1 + 1))
                                    store32((v2 + (v1 << 2)), v5)
                                    v1 = load32(v4 + 56)
                                    if (u32(load32(v4 + 56)) < u32(v9)):
                                        continue
                                    break
                            store32((v2 + (load32(PLAYER_COUNT) << 2)), v7)
                            break
                        store32(v4 + 56, v6)
                        v1 = arg0
                        if (u32(v6) <= u32(arg0)):
                            break
                        while True:  # $label18
                            v1 = (v1 + 1)
                            store32((v2 + (v1 << 2)), load32((v2 + ((v1 + 1) << 2))))
                            if (u32(v1) < u32(load32(v4 + 56))):
                                continue
                            break
                        break
                    while True:  # $label19
                        v5 = load32(v4 + 72)
                        if not load32(v4 + 72):
                            break
                        v6 = (v5 - 1)
                        v13 = (v4 - -64)
                        v2 = load32((v4 - -64))
                        v9 = (load32(PLAYER_COUNT) + 1)
                        if (u32((load32(PLAYER_COUNT) + 1)) >= u32(v5)):
                            v10 = (v2 + (v6 << 2))
                            while True:  # $label20
                                if not v6:
                                    v3 = 0
                                    break
                                v7 = 0
                                v1 = 0
                                v3 = 0
                                if (u32((v5 - 2)) >= u32(3)):
                                    v14 = (v6 & -4)
                                    v5 = 0
                                    while True:  # $label21
                                        v8 = (v1 << 2)
                                        v3 = (load32((v2 + ((v1 << 2) | 12))) + (load32((v2 + (v8 | 8))) + (load32((v2 + (v8 | 4))) + (load32((v2 + v8)) + v3))))
                                        v1 = (v1 + 4)
                                        v5 = (v5 + 4)
                                        if ((v5 + 4) != v14):
                                            continue
                                        break
                                v5 = (v6 & 3)
                                if not (v6 & 3):
                                    break
                                while True:  # $label22
                                    v3 = (load32((v2 + (v1 << 2))) + v3)
                                    v1 = (v1 + 1)
                                    v7 = (v7 + 1)
                                    if ((v7 + 1) != v5):
                                        continue
                                    break
                                break
                            v7 = load32(v10)
                            v5 = (u32(v3) > u32(((v6 & 0xFFFFFFFF) >> 1)))
                            store32(v10, (u32(v3) > u32(((v6 & 0xFFFFFFFF) >> 1))))
                            v1 = load32(v4 + 72)
                            if (u32(v9) > u32(load32(v4 + 72))):
                                while True:  # $label23
                                    if (load32(v4 + 68) == v1):
                                        v3 = (load32(v4 + 76) + v1)
                                        store32(v4 + 68, (load32(v4 + 76) + v1))
                                        v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                                        if v1:
                                            # TODO: memory.copy
                                        v1 = load32(v4 + 72)
                                        store32(v13, v3)
                                        v2 = v3
                                    store32(v4 + 72, (v1 + 1))
                                    store32((v2 + (v1 << 2)), v5)
                                    v1 = load32(v4 + 72)
                                    if (u32(load32(v4 + 72)) < u32(v9)):
                                        continue
                                    break
                            store32((v2 + (load32(PLAYER_COUNT) << 2)), v7)
                            break
                        store32(v4 + 72, v6)
                        v1 = arg0
                        if (u32(v6) <= u32(arg0)):
                            break
                        while True:  # $label24
                            v1 = (v1 + 1)
                            store32((v2 + (v1 << 2)), load32((v2 + ((v1 + 1) << 2))))
                            if (u32(v1) < u32(load32(v4 + 72))):
                                continue
                            break
                        break
                    v11 = (v11 + 1)
                    v2 = load32(v12 + 12)
                    if (u32((v11 + 1)) < u32(((load32(v12 + 16) - load32(v12 + 12)) // 196))):
                        continue
                    break
            v15 = (v15 + 1)
            v2 = load32(9568064)
            if (u32((v15 + 1)) < u32(((load32(9568068) - load32(9568064)) >> 7))):
                continue
            break

# ----------------------------------------------------------
# $func285
# ----------------------------------------------------------
def func285(arg0, arg1):
    v7 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v8 = load32(PLAYERS)
    v6 = load16u(arg0 + 110)
    while True:  # $label0
        v3 = load8u(arg0 + 122)
        if (load8u(arg0 + 122) == load32(38608)):
            break
        if (v3 == load32(38612)):
            break
        break
    v2 = (load32(39056) if (load32(38616) == v3) else arg1)
    v4 = (load32(38632) + ((load32(39056) if (load32(38616) == v3) else arg1) * 36))
    v5 = ((arg1 * 404) + ENTITY_TYPES)
    v9 = (load32(((load32(38632) + ((load32(39056) if (load32(38616) == v3) else arg1) * 36)) + 269380)) + load32(((arg1 * 404) + ENTITY_TYPES) + 92))
    store32(load32(38628) + 52, (load32(((load32(38632) + ((load32(39056) if (load32(38616) == v3) else arg1) * 36)) + 269380)) + load32(((arg1 * 404) + ENTITY_TYPES) + 92)))
    v10 = (load32((v4 + 269384)) + load32(v5 + 100))
    store32(arg0 + 60, (load32((v4 + 269384)) + load32(v5 + 100)))
    if load8u(((v3 * 404) + ENTITY_TYPES) + 334):
        v3 = load32(arg0 + 84)
        store32(arg0 + 52, (load32(arg0 + 84) + v9))
        store32(arg0 + 60, ((((v3 + 1) & 0xFFFFFFFF) >> 1) + v10))
    # TODO: i32.div_u
    # TODO: i32.div_u
    store32(((load32(arg0 + 64) * 100) * load32(arg0 + 68)) + 64, 100)
    store32(arg0 + 68, (load32((v4 + 269392)) + load32(v5 + 108)))
    v3 = load32(v5 + 120)
    if (u32(load32(v5 + 120)) > u32(load32(arg0 + 76))):
        if not load32(arg0 + 72):
            v3 = load32(v5 + 120)
        store32(arg0 + 76, v3)
        store32(arg0 + 72, v3)
    v3 = ((v8 + (v6 * 286704)) + 281808)
    v5 = load8u(arg0 + 122)
    v4 = (((v8 + (v6 * 286704)) + 281808) + (load8u(arg0 + 122) << 2))
    store32((((v8 + (v6 * 286704)) + 281808) + (load8u(arg0 + 122) << 2)), (load32(v4) - 1))
    store8(arg0 + 122, v2)
    v2 = (v3 + ((v2 & 255) << 2))
    store32((v3 + ((v2 & 255) << 2)), (load32(v2) + 1))
    v3 = load8u(arg0 + 122)
    v2 = load32(((load8u(arg0 + 122) * 72) + 9263856))
    while True:  # $label2
        if (v3 == load32(38600)):
            func277(load16u(arg0 + 112), load16u(arg0 + 114), load16u(arg0 + 110))
            while True:  # $label1
                if not load8u(9147329):
                    break
                if not load8u(9147334):
                    break
                v2 = load32(9142464)
                store8(arg0 + 124, (load16u(arg0 + 114) % 5))
                break
                break
            while True:  # $label3
                if not load8u(9147331):
                    break
                if not load8u(9147332):
                    break
                v2 = load32(9142468)
                store8(arg0 + 124, (load16u(arg0 + 112) % 7))
                break
                break
            store8(arg0 + 124, 0)
        break
    while True:  # $label4
        if not load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264):
            if load16u(arg0 + 108):
                store32(arg0 + 88, 0)
                store16(arg0 + 108, 0)
            if not load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4):
                store8(arg0 + 123, 0)
                store32(arg0 + 32, 0)
                store32(arg0 + 116, load32(arg0 + 112))
                break
            func29(arg0, 1)
            break
        break
    if (load8u(arg0 + 129) == 8):
    v3 = (v6 * 286704)
    func144(((v6 * 286704) + v8), load32(arg0 + 28), 1)
    while True:  # $label5
        v2 = load32((((v3 + v8) + (v5 << 2)) + 284636))
        if not load32((((v3 + v8) + (v5 << 2)) + 284636)):
            break
        v3 = load32(v2 + 8)
        if not load32(v2 + 8):
            break
        v4 = load32(arg0 + 28)
        v9 = load32(v2)
        v2 = 0
        while True:  # $label6
            v10 = (v9 + (v2 << 2))
            if (v4 != load32((v9 + (v2 << 2)))):
                v2 = (v2 + 1)
                if ((v2 + 1) != v3):
                    continue
                break
            break
        if (v2 < 0):
            break
        store32(v10, 0)
        break
    while True:  # $label7
        if not load8u(9142916):
            break
        v2 = load32(arg0 + 40)
        if not load32(arg0 + 40):
            break
        v3 = load8u(arg0 + 122)
        v4 = load16u(arg0 + 110)
        store32(v7 + 4, v2)
        store32(v7, (v3 | (v4 << 16)))
        a_b()
        break
    v2 = (v8 + (v6 * 286704))
    v6 = (load32(((arg1 * 404) + ENTITY_TYPES) + 280) - load32(((v5 * 404) + ENTITY_TYPES) + 280))
    arg1 = ((load32(((arg1 * 404) + ENTITY_TYPES) + 280) - load32(((v5 * 404) + ENTITY_TYPES) + 280)) + load32(v2 + 283976))
    store32((v8 + (v6 * 286704)) + 283976, ((load32(((arg1 * 404) + ENTITY_TYPES) + 280) - load32(((v5 * 404) + ENTITY_TYPES) + 280)) + load32(v2 + 283976)))
    if (v6 < 0):
        store8(v2 + 286700, 1)
    v2 = (v2 + 281748)
    if (u32(arg1) > u32(load32((v2 + 281748)))):
        store32(v2, arg1)
    while True:  # $label8
        if not load32(arg0 + 92):
            break
        arg1 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32(arg0 + 28)):
                break
        break
    G.global0 = (v7 + 16)
    return func28((arg1 != 0), 1)

# ----------------------------------------------------------
# $func286
# ----------------------------------------------------------
def func286(arg0):
    func277(load16u(arg0 + 112), load16u(arg0 + 114), load16u(arg0 + 110))
    while True:  # $label0
        if not load8u(9147329):
            break
        if not load8u(9147334):
            break
        store8(arg0 + 124, (load16u(arg0 + 114) % 5))
        return
        break
    while True:  # $label1
        if not load8u(9147331):
            break
        if not load8u(9147332):
            break
        store8(arg0 + 124, (load16u(arg0 + 112) % 7))
        return
        break

# ----------------------------------------------------------
# $func287
# ----------------------------------------------------------
def func287(arg0):
    while True:  # $label2
        while True:  # $label0
            while True:  # $label1
                v3 = load8u(arg0 + 123)
                if (load8u(arg0 + 123) != 1):
                    v1 = load32(9215884)
                    v2 = load32(arg0 + 44)
                    v4 = load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4)
                    if ((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) != 1) & (v3 != 3)):
                        break
                    if (v4 == 1):
                        break
                    break
                break
            v2 = load8u(entities[load32(arg0 + 32)].sub_state)
            v1 = 4
            if (v2 == load32(38528)):
                break
            v1 = 0
            if (v2 == load32(38504)):
                break
            v1 = 1
            if (v2 == load32(38448)):
                break
            v1 = 2
            if (v2 == load32(38500)):
                break
            v1 = 3
            if (v2 == load32(38508)):
                break
            break
        v1 = 4
        if (load8u(arg0 + 129) == 10):
            break
        v1 = 5
        if (v3 == 4):
            break
        v2 = load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4)
        if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 4):
            break
        v1 = 6
        if (v3 == 6):
            break
        if (v2 == 6):
            break
        v1 = 7
        if (v3 == 60):
            break
        if (v2 == 60):
            break
        v1 = (8 if (load8u(arg0 + 125) == 8) else -1)
        break
    return v1

# ----------------------------------------------------------
# $func288
# ----------------------------------------------------------
def func288(arg0, arg1, arg2):
    v3 = (G.global0 - 96)
    G.global0 = (G.global0 - 96)
    while True:  # $label0
        arg0 = load32(arg0 + 24)
        if not load32(arg0 + 24):
            break
        v4 = load32(arg0 + 4)
        if not load32(arg0 + 4):
            break
        if not load32(v4 + 8):
            break
        # TODO: f64.promote_f32
        v6 = arg2
        # TODO: f64.promote_f32
        v7 = arg1
        arg0 = 0
        while True:  # $label3
            while True:  # $label1
                v5 = load32((load32(v4) + ((arg0 << 2) | 4)))
                if not load32((load32(v4) + ((arg0 << 2) | 4))):
                    break
                while True:  # $label2
                    if load8u(9142916):
                        store32(v3 + 88, v5)
                        store64(v3 + 80, 0)
                        storef64(v3 + 72, v6)
                        storef64(v3 + 64, v7)
                        a_b()
                        break
                    store64(v3 + 32, 0)
                    store32(v3 + 48, v5)
                    # TODO: f64.promote_f32
                    storef64(v3 + 40, i32((load32(9142848) * 25)))
                    storef64(v3 + 16, v7)
                    storef64(v3 + 24, v6)
                    a_b()
                    break
                if not load8u(9142916):
                    break
                store32(v3 + 4, v5)
                store32(v3, (load32(9142848) * 25))
                a_b()
                break
            arg0 = (arg0 + 2)
            if (u32((arg0 + 2)) < u32(load32(v4 + 8))):
                continue
            break
        break
    G.global0 = (v3 + 96)

# ----------------------------------------------------------
# $func289
# ----------------------------------------------------------
def func289(arg0, arg1, arg2):
    v3 = load8u(arg0 + 122)
    while True:  # $label3
        while True:  # $label1
            while True:  # $label0
                if not load16u(arg0 + 108):
                    break
                while True:  # $label2
                    # br_table (v3 + -64)
                    break
                    break
                if (v3 == 10):
                    break
                break
            break
            break
        arg1 = (not load8u(9142916) | arg1)
        while True:  # $label5
            while True:  # $label4
                v4 = load32(arg0 + 20)
                if not load32(arg0 + 20):
                    break
                if (u32(load32(v4 + 8)) < u32(3)):
                    break
                if load32(load32(v4)):
                    break
                v4 = ((v3 * 72) + 9263856)
                if not load32(((v3 * 72) + 9263856) + 68):
                    break
                break
                break
            while True:  # $label9
                while True:  # $label6
                    while True:  # $label8
                        while True:  # $label7
                            v4 = load32(arg0 + 88)
                            # br_table (load32(arg0 + 88) & 65535)
                            break
                            break
                        break
                        break
                    v4 = ((v4 & 0xFFFFFFFF) >> 16)
                    if (((v4 & 0xFFFFFFFF) >> 16) == load32(38984)):
                        break
                    if (load32(38528) == v4):
                        break
                    break
                    break
                break
                break
            break
        break
    v3 = load32(((v3 * 72) + 9263908))
    arg1 = ((load32(((v3 * 72) + 9263908)) != load32(arg0 + 48)) | arg1)
    if (((load32(((v3 * 72) + 9263908)) != load32(arg0 + 48)) | arg1) == 1):
    return arg1

# ----------------------------------------------------------
# $func290
# ----------------------------------------------------------
def func290(arg0):
    if load16u(arg0 + 120):
        func119(0, arg0, 0, 1)
        v2 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        if load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 216):
            v5 = load32(9142840)
            v6 = load16u(arg0 + 114)
            v7 = load16u(arg0 + 112)
            while True:  # $label1
                v4 = (v4 + 1)
                v8 = ((v4 + 1) + v7)
                v1 = 0
                while True:  # $label0
                    v1 = (v1 + 1)
                    v3 = (load32(9142440) + 2)
                    store32((v5 + ((v8 + ((((v1 + 1) + v6) + ((load32(9142440) + 2) * load32(v2 + 208))) * v3)) << 2)), load32(v2 + 212))
                    v3 = load32(v2 + 216)
                    if (u32(v1) < u32(load32(v2 + 216))):
                        continue
                    break
                if (u32(v3) > u32(v4)):
                    continue
                break
        v1 = load32(38428)
        store8(arg0 + 122, load32(38428))
        if load16u(arg0 + 108):
            store32(arg0 + 88, 0)
            store16(arg0 + 108, 0)
        v4 = (((v1 & 255) * 404) + ENTITY_TYPES)
        if load32((((v1 & 255) * 404) + ENTITY_TYPES) + 216):
            v5 = load32(9142840)
            v6 = load16u(arg0 + 114)
            v7 = load16u(arg0 + 112)
            v2 = 0
            while True:  # $label3
                v2 = (v2 + 1)
                v8 = ((v2 + 1) + v7)
                v1 = 0
                while True:  # $label2
                    v1 = (v1 + 1)
                    v3 = (load32(9142440) + 2)
                    store32((v5 + ((v8 + ((((v1 + 1) + v6) + ((load32(9142440) + 2) * load32(v4 + 208))) * v3)) << 2)), load32(arg0 + 28))
                    v3 = load32(v4 + 216)
                    if (u32(v1) < u32(load32(v4 + 216))):
                        continue
                    break
                if (u32(v2) < u32(v3)):
                    continue
                break
        store32(load32(arg0 + 24), 0)
        store16(arg0 + 120, 0)
        store32(9143000, 0)
        while True:  # $label4
            if not load32(arg0 + 92):
                break
            v1 = load8u(9147141)
            if load32(9140316):
                if (load32(9140320) != load32(arg0 + 28)):
                    break
            break
        func29(arg0, 1)

# ----------------------------------------------------------
# $func291
# ----------------------------------------------------------
def func291(arg0, arg1, arg2, arg3):
    if (load8u(arg0 + 125) == 1):
        func63(0, arg0, arg1, arg2, arg3)
        return
    # TODO: i32.div_u
    store32(load32(9142848), (arg3 + 25))

# ----------------------------------------------------------
# $func292
# ----------------------------------------------------------
def func292(arg0):
    v1 = 1
    while True:  # $label0
        v4 = load32(load32(GAME_STATE) + 48)
        if not load32(load32(GAME_STATE) + 48):
            break
        if load8u(9147152):
            break
        while True:  # $label1
            v1 = load32(CURRENT_PLAYER)
            if not load32(CURRENT_PLAYER):
                break
            if not load8u((load32(9143012) + (load16u(arg0 + 110) + (load32(PLAYER_COUNT) * v1)))):
                break
            v1 = 1
            if (load8u(arg0 + 125) != 3):
                break
            break
        v2 = load8u(arg0 + 122)
        v5 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        v3 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 216)
        if not load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 216):
            return 0
        v1 = 0
        v6 = load32(v5 + 220)
        if not load32(v5 + 220):
            break
        v7 = load32(9142440)
        v8 = load32(9147376)
        v9 = load16u(arg0 + 114)
        v10 = load16u(arg0 + 112)
        v11 = load32(((v2 * 404) + ENTITY_TYPES) + 372)
        arg0 = 0
        v2 = 1
        if (v4 == 2):
            while True:  # $label4
                v12 = (arg0 + v10)
                while True:  # $label3
                    while True:  # $label2
                        if not load8u((v11 + ((v1 * v3) + arg0))):
                            break
                        v4 = load16u((v8 + (((v7 * (v1 + v9)) + v12) << 1)))
                        if load32(v5 + 260):
                            if (u32(v4) <= u32(1)):
                                break
                            return v2
                        if not v4:
                            break
                        return v2
                        break
                    v1 = (v1 + 1)
                    if ((v1 + 1) != v6):
                        continue
                    break
                arg0 = (arg0 + 1)
                v2 = (u32((arg0 + 1)) < u32(v3))
                v1 = 0
                if (arg0 != v3):
                    continue
                break
                break
            raise Unreachable()
        while True:  # $label7
            v5 = (arg0 + v10)
            while True:  # $label6
                while True:  # $label5
                    if not load8u((v11 + ((v1 * v3) + arg0))):
                        break
                    if not load16u((v8 + (((v7 * (v1 + v9)) + v5) << 1))):
                        break
                    return v2
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v6):
                    continue
                break
            arg0 = (arg0 + 1)
            v2 = (u32((arg0 + 1)) < u32(v3))
            v1 = 0
            if (arg0 != v3):
                continue
            break
        break
    return (v1 & 1)

# ----------------------------------------------------------
# $func293
# ----------------------------------------------------------
def func293(arg0):
    v1 = 1
    while True:  # $label0
        v4 = load32(load32(GAME_STATE) + 48)
        if not load32(load32(GAME_STATE) + 48):
            break
        if load8u(9147152):
            break
        while True:  # $label1
            v1 = load32(CURRENT_PLAYER)
            if not load32(CURRENT_PLAYER):
                break
            if not load8u((load32(9143012) + (load16u(arg0 + 110) + (load32(PLAYER_COUNT) * v1)))):
                break
            v1 = 1
            if (load8u(arg0 + 125) != 3):
                break
            break
        v2 = load8u(arg0 + 122)
        v5 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        v3 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 216)
        if not load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 216):
            return 0
        v1 = 0
        v5 = load32(v5 + 220)
        if not load32(v5 + 220):
            break
        v6 = load32(9142440)
        v7 = load32(9147376)
        v8 = load16u(arg0 + 114)
        v9 = load16u(arg0 + 112)
        v10 = load32(((v2 * 404) + ENTITY_TYPES) + 372)
        arg0 = 0
        v2 = 1
        if (v4 == 2):
            while True:  # $label4
                v4 = (arg0 + v9)
                while True:  # $label3
                    while True:  # $label2
                        if not load8u((v10 + ((v1 * v3) + arg0))):
                            break
                        if (u32(load16u((v7 + (((v6 * (v1 + v8)) + v4) << 1)))) <= u32(1)):
                            break
                        return v2
                        break
                    v1 = (v1 + 1)
                    if ((v1 + 1) != v5):
                        continue
                    break
                arg0 = (arg0 + 1)
                v2 = (u32((arg0 + 1)) < u32(v3))
                v1 = 0
                if (arg0 != v3):
                    continue
                break
                break
            raise Unreachable()
        while True:  # $label7
            v4 = (arg0 + v9)
            while True:  # $label6
                while True:  # $label5
                    if not load8u((v10 + ((v1 * v3) + arg0))):
                        break
                    if not load16u((v7 + (((v6 * (v1 + v8)) + v4) << 1))):
                        break
                    return v2
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v5):
                    continue
                break
            arg0 = (arg0 + 1)
            v2 = (u32((arg0 + 1)) < u32(v3))
            v1 = 0
            if (arg0 != v3):
                continue
            break
        break
    return (v1 & 1)

# ----------------------------------------------------------
# $func294
# ----------------------------------------------------------
def func294(arg0):
    while True:  # $label0
        if not load32(arg0 + 92):
            break
        v1 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32(arg0 + 28)):
                break
        break

# ----------------------------------------------------------
# $func295
# ----------------------------------------------------------
def func295(arg0, arg1):
    while True:  # $label0
        v3 = load8u(arg0 + 122)
        if (load8u(arg0 + 122) == load32(38500)):
            break
        v2 = load16u(arg0 + 110)
        arg1 = (load32(PLAYER_COUNT) * arg1)
        v4 = load32(9143004)
        while True:  # $label1
            v5 = load16u(arg0 + 120)
            if load16u(arg0 + 120):
            else:
            if not load8u(((v5 if load8u((v4 + (arg1 + v2))) else v2) + (v2 + arg1))):
                v2 = 0
                if (load8u(arg0 + 127) != 6):
                    break
                if not load8u(arg0 + 128):
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
        if (load32(arg0 + 64) == -1):
            break
        arg0 = ((v3 * 404) + ENTITY_TYPES)
        if (load32(((v3 * 404) + ENTITY_TYPES) + 264) == 2):
            break
        if (load32(arg0 + 188) != 55):
            break
        if (load32(38560) == v3):
            break
        if (load32(38620) == v3):
            break
        v2 = (load32(38564) != v3)
        break
    return v2

# ----------------------------------------------------------
# $func296
# ----------------------------------------------------------
def func296(arg0, arg1):
    v3 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    store8(arg0 + 128, arg1)
    while True:  # $label0
        arg1 = load16u(arg0 + 112)
        v2 = ((load16u(arg0 + 112) << 5) - load32(9142952))
        v2 = load16u(arg0 + 114)
        v4 = ((load16u(arg0 + 114) << 5) - load32(9142956))
        if ((((((load16u(arg0 + 112) << 5) - load32(9142952)) * v2) + (((load16u(arg0 + 114) << 5) - load32(9142956)) * v4)) - 1) > 9000000):
            break
        v5 = load32(39860)
        while True:  # $label1
            v6 = load32(load32(GAME_STATE) + 48)
            if not load32(load32(GAME_STATE) + 48):
                break
            if load8u(9147152):
                break
            v4 = load16u((load32(9147376) + (((load32(9142440) * v2) + arg1) << 1)))
            if (v6 == 2):
                if (u32(v4) > u32(1)):
                    break
                break
            if not v4:
                break
            break
        store32(v3 + 40, v2)
        store32(v3 + 36, arg1)
        store32(v3 + 32, v5)
        a_b()
        break
    v4 = load8u(9142916)
    arg1 = (8 if load8u((load32(9143004) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(arg0 + 110))))) else (11 if load8u(9142916) else 3))
    store8(arg0 + 127, (8 if load8u((load32(9143004) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(arg0 + 110))))) else (11 if load8u(9142916) else 3)))
    while True:  # $label2
        v2 = load32(arg0 + 40)
        if not load32(arg0 + 40):
            break
        if v4:
            store32(v3 + 20, v2)
            arg1 = (arg1 << 4)
            store32(v3 + 16, ((((load32(((arg1 << 4) + 1748)) << 8) + load32((arg1 + 1744))) + (load32((arg1 + 1752)) << 16)) + (load32((arg1 + 1756)) << 24)))
            a_b()
            break
        store32(v3 + 4, v2)
        store32(v3, arg1)
        a_b()
        break
    store8(arg0 + 129, 0)
    arg1 = load32(9215884)
    while True:  # $label3
        v2 = load32(arg0 + 44)
        if not load32(arg0 + 44):
            v2 = 1
            break
        v2 = ((v2 << 2) | 1)
        if load32((arg1 + (((v2 << 2) | 1) << 2))):
            break
        if (load8u(arg0 + 123) != 6):
            break
        store8(arg0 + 123, 0)
        store32(arg0 + 32, 0)
        store32(arg0 + 116, load32(arg0 + 112))
        break
    if (load32((arg1 + (v2 << 2))) == 6):
        func29(arg0, 1)
    G.global0 = (v3 + 48)

# ----------------------------------------------------------
# $func297
# ----------------------------------------------------------
def func297(arg0, arg1):
    v3 = load8u(arg0 + 122)
    v2 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 136)
    # TODO: i32.div_u
    v4 = (100 if (load32(((players[load16u(arg0 + 110)] + (load32(39216) << 2)) + 281808)) == 1) else v2)
    v2 = load32(arg0 + 16)
    if not load32(arg0 + 16):
        v2 = func26(16)
        store32(func26(16) + 4, v4)
        store32(v2, func26((-1 if (u32(v4) > u32(1073741823)) else (v4 << 2))))
        store64(v2 + 8, 4294967296)
        store32(arg0 + 16, v2)
    while True:  # $label0
        if (load32(((v3 * 404) + ENTITY_TYPES) + 264) != 1):
            break
        if load32(v2 + 8):
            break
        v2 = load32(arg0 + 16)
        break
    arg0 = load32(v2 + 8)
    if (u32(v4) > u32(load32(v2 + 8))):
        while True:  # $label1
            if (load32(v2 + 4) != arg0):
                v5 = load32(v2)
                v3 = arg0
                break
            v3 = (load32(v2 + 12) + arg0)
            store32(v2 + 4, (load32(v2 + 12) + arg0))
            v6 = load32(v2)
            v5 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
            if arg0:
                # TODO: memory.copy
            v3 = arg0
            if v6:
                v3 = load32(v2 + 8)
            store32(v2, v5)
            break
        store32(v2 + 8, (v3 + 1))
        store32((v5 + (v3 << 2)), arg1)
    return (u32(arg0) < u32(v4))

# ----------------------------------------------------------
# $func298
# ----------------------------------------------------------
def func298(arg0, arg1, arg2, arg3):
    v24 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v24 + 12, arg3)
    v29 = arg0
    v16 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v26 = load32(v24 + 12)
    while True:  # $label0
        v33 = arg1
        v22 = load32(arg1)
        if not load32(arg1):
            v22 = 1
            v29 = (v16 + 7)
            break
        store32(v33, 0)
        break
    store32(v16 + 48, 0)
    store64(v16 + 40, 0)
    store32(v16 + 12, 0)
    store32(v16 + 8, arg2)
    while True:  # $label6
        while True:  # $label2
            arg1 = (v16 + 8)
            while True:  # $label1
                if (load8u(7784) != 49):
                    break
                if not arg1:
                    break
                store32(arg1 + 24, 0)
                arg0 = load32(arg1 + 32)
                if not load32(arg1 + 32):
                    store32(arg1 + 40, 0)
                    store32(arg1 + 32, 417)
                    arg0 = 417
                if not load32(arg1 + 36):
                    store32(arg1 + 36, 418)
                arg3 = call_table(arg0)
                if not call_table(arg0):
                    break
                store32(arg1 + 28, arg3)
                store32(arg3 + 56, 0)
                store32(arg3, arg1)
                store32(arg3 + 4, 16180)
                arg0 = -2
                while True:  # $label3
                    if not arg1:
                        break
                    if not load32(arg1 + 32):
                        break
                    v12 = load32(arg1 + 36)
                    if not load32(arg1 + 36):
                        break
                    arg2 = load32(arg1 + 28)
                    if not load32(arg1 + 28):
                        break
                    if (load32(arg2) != arg1):
                        break
                    if (u32((load32(arg2 + 4) - 16180)) > u32(31)):
                        break
                    while True:  # $label5
                        while True:  # $label4
                            v5 = load32(arg2 + 56)
                            if load32(arg2 + 56):
                                if (load32(arg2 + 40) != 15):
                                    break
                            store32(arg2 + 40, 15)
                            store32(arg2 + 12, 5)
                            break
                            break
                        store32(arg2 + 56, 0)
                        v12 = load32(arg1 + 32)
                        store32(arg2 + 40, 15)
                        store32(arg2 + 12, 5)
                        if not v12:
                            break
                        break
                    if not load32(arg1 + 36):
                        break
                    arg2 = load32(arg1 + 28)
                    if not load32(arg1 + 28):
                        break
                    if (load32(arg2) != arg1):
                        break
                    if (u32((load32(arg2 + 4) - 16180)) > u32(31)):
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
                if not arg0:
                    break
                store32(arg1 + 28, 0)
                break
            break
        if arg0:
            break
        store32(v16 + 24, 0)
        store32(v16 + 20, v29)
        arg0 = 0
        while True:  # $label185
            if not arg0:
                store32(v16 + 24, v22)
                v22 = 0
            if not load32(v16 + 12):
                store32(v16 + 12, v26)
                v26 = 0
            v12 = 0
            v20 = (G.global0 - 16)
            G.global0 = (G.global0 - 16)
            v23 = -2
            while True:  # $label7
                v10 = (v16 + 8)
                if not (v16 + 8):
                    break
                if not load32(v10 + 32):
                    break
                if not load32(v10 + 36):
                    break
                v4 = load32(v10 + 28)
                if not load32(v10 + 28):
                    break
                if (load32(v4) != v10):
                    break
                v5 = load32(v4 + 4)
                if (u32((load32(v4 + 4) - 16180)) > u32(31)):
                    break
                v14 = load32(v10 + 12)
                if not load32(v10 + 12):
                    break
                arg0 = load32(v10)
                if not load32(v10):
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
                while True:  # $label37
                    while True:  # $label36
                        while True:  # $label177
                            while True:  # $label174
                                while True:  # $label43
                                    while True:  # $label52
                                        arg1 = -3
                                        v8 = 1
                                        while True:  # $label41
                                            while True:  # $label35
                                                while True:  # $label74
                                                    while True:  # $label163
                                                        while True:  # $label16
                                                            while True:  # $label15
                                                                while True:  # $label14
                                                                    while True:  # $label13
                                                                        while True:  # $label65
                                                                            while True:  # $label62
                                                                                while True:  # $label94
                                                                                    while True:  # $label83
                                                                                        while True:  # $label159
                                                                                            while True:  # $label157
                                                                                                while True:  # $label100
                                                                                                    while True:  # $label133
                                                                                                        while True:  # $label137
                                                                                                            while True:  # $label140
                                                                                                                while True:  # $label143
                                                                                                                    while True:  # $label147
                                                                                                                        while True:  # $label151
                                                                                                                            while True:  # $label88
                                                                                                                                while True:  # $label153
                                                                                                                                    while True:  # $label77
                                                                                                                                        while True:  # $label31
                                                                                                                                            while True:  # $label38
                                                                                                                                                while True:  # $label29
                                                                                                                                                    while True:  # $label39
                                                                                                                                                        while True:  # $label27
                                                                                                                                                            while True:  # $label26
                                                                                                                                                                while True:  # $label40
                                                                                                                                                                    while True:  # $label76
                                                                                                                                                                        while True:  # $label75
                                                                                                                                                                            while True:  # $label78
                                                                                                                                                                                while True:  # $label82
                                                                                                                                                                                    while True:  # $label49
                                                                                                                                                                                        while True:  # $label33
                                                                                                                                                                                            while True:  # $label32
                                                                                                                                                                                                while True:  # $label24
                                                                                                                                                                                                    while True:  # $label42
                                                                                                                                                                                                        while True:  # $label44
                                                                                                                                                                                                            while True:  # $label22
                                                                                                                                                                                                                while True:  # $label21
                                                                                                                                                                                                                    while True:  # $label20
                                                                                                                                                                                                                        while True:  # $label19
                                                                                                                                                                                                                            while True:  # $label18
                                                                                                                                                                                                                                while True:  # $label45
                                                                                                                                                                                                                                    while True:  # $label46
                                                                                                                                                                                                                                        while True:  # $label63
                                                                                                                                                                                                                                            while True:  # $label61
                                                                                                                                                                                                                                                while True:  # $label12
                                                                                                                                                                                                                                                    while True:  # $label59
                                                                                                                                                                                                                                                        while True:  # $label58
                                                                                                                                                                                                                                                            while True:  # $label11
                                                                                                                                                                                                                                                                while True:  # $label56
                                                                                                                                                                                                                                                                    while True:  # $label55
                                                                                                                                                                                                                                                                        while True:  # $label10
                                                                                                                                                                                                                                                                            while True:  # $label47
                                                                                                                                                                                                                                                                                while True:  # $label48
                                                                                                                                                                                                                                                                                    while True:  # $label8
                                                                                                                                                                                                                                                                                        while True:  # $label9
                                                                                                                                                                                                                                                                                            while True:  # $label17
                                                                                                                                                                                                                                                                                                while True:  # $label23
                                                                                                                                                                                                                                                                                                    while True:  # $label34
                                                                                                                                                                                                                                                                                                        while True:  # $label25
                                                                                                                                                                                                                                                                                                            while True:  # $label28
                                                                                                                                                                                                                                                                                                                while True:  # $label30
                                                                                                                                                                                                                                                                                                                    # br_table (v5 - 16180)
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
                                                                                                                                                                                                                                                                                                if (u32(arg2) >= u32(14)):
                                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                                if not arg3:
                                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                                arg1 = (arg2 + 8)
                                                                                                                                                                                                                                                                                                v5 = (arg0 + 1)
                                                                                                                                                                                                                                                                                                v8 = (arg3 - 1)
                                                                                                                                                                                                                                                                                                v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                                                                                                if (u32(arg2) <= u32(5)):
                                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                                arg0 = v5
                                                                                                                                                                                                                                                                                                arg3 = v8
                                                                                                                                                                                                                                                                                                arg2 = arg1
                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                            if (u32(arg2) >= u32(32)):
                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                            if not arg3:
                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                            arg1 = (arg0 + 1)
                                                                                                                                                                                                                                                                                            v5 = (arg3 - 1)
                                                                                                                                                                                                                                                                                            v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                                                                                            if (u32(arg2) <= u32(23)):
                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                            arg0 = arg1
                                                                                                                                                                                                                                                                                            arg3 = v5
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        if (u32(arg2) >= u32(16)):
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        if not arg3:
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        arg1 = (arg2 + 8)
                                                                                                                                                                                                                                                                                        v5 = (arg0 + 1)
                                                                                                                                                                                                                                                                                        v8 = (arg3 - 1)
                                                                                                                                                                                                                                                                                        v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                                                                                        if (u32(arg2) <= u32(7)):
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        arg0 = v5
                                                                                                                                                                                                                                                                                        arg3 = v8
                                                                                                                                                                                                                                                                                        arg2 = arg1
                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                    v7 = load32(v4 + 12)
                                                                                                                                                                                                                                                                                    if not load32(v4 + 12):
                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                    while True:  # $label50
                                                                                                                                                                                                                                                                                        if (u32(arg2) >= u32(16)):
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        if not arg3:
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        arg1 = (arg2 + 8)
                                                                                                                                                                                                                                                                                        v5 = (arg0 + 1)
                                                                                                                                                                                                                                                                                        v8 = (arg3 - 1)
                                                                                                                                                                                                                                                                                        v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                                                                                        if (u32(arg2) > u32(7)):
                                                                                                                                                                                                                                                                                            arg0 = v5
                                                                                                                                                                                                                                                                                            arg3 = v8
                                                                                                                                                                                                                                                                                            arg2 = arg1
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        if not v8:
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
                                                                                                                                                                                                                                                                                    while True:  # $label51
                                                                                                                                                                                                                                                                                        if not (v7 & 2):
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        if (v6 != 35615):
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        if not load32(v4 + 40):
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
                                                                                                                                                                                                                                                                                    while True:  # $label53
                                                                                                                                                                                                                                                                                        if (v7 & 1):
                                                                                                                                                                                                                                                                                            if not ((((v6 << 8) & 65280) + ((v6 & 0xFFFFFFFF) >> 8)) % 31):
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
                                                                                                                                                                                                                                                                                    if not (v7 & (u32(v5) >= u32(v5))):
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
                                                                                                                                                                                                                                                                                if not v8:
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
                                                                                                                                                                                                                                                                            while True:  # $label54
                                                                                                                                                                                                                                                                                if not (v6 & 512):
                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                if not (load8u(v4 + 12) & 4):
                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                store16(v20 + 12, v6)
                                                                                                                                                                                                                                                                                store32(v4 + 28, func43(load32(v4 + 28), (v20 + 12), 2))
                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                            store32(v4 + 4, 16182)
                                                                                                                                                                                                                                                                            arg2 = 0
                                                                                                                                                                                                                                                                            v6 = 0
                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                        if (u32(arg2) > u32(31)):
                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    if not arg3:
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    arg1 = (arg0 + 1)
                                                                                                                                                                                                                                                                    v5 = (arg3 - 1)
                                                                                                                                                                                                                                                                    v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                                                                    if (u32(arg2) > u32(23)):
                                                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                                                        arg3 = v5
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    v8 = (arg2 + 8)
                                                                                                                                                                                                                                                                    if not v5:
                                                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                                                        arg3 = 0
                                                                                                                                                                                                                                                                        arg2 = v8
                                                                                                                                                                                                                                                                        arg1 = v12
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    arg1 = (arg0 + 2)
                                                                                                                                                                                                                                                                    v5 = (arg3 - 2)
                                                                                                                                                                                                                                                                    v6 = ((load8u(arg0 + 1) << v8) + v6)
                                                                                                                                                                                                                                                                    if (u32(arg2) > u32(15)):
                                                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                                                        arg3 = v5
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    v8 = (arg2 + 16)
                                                                                                                                                                                                                                                                    if not v5:
                                                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                                                        arg3 = 0
                                                                                                                                                                                                                                                                        arg2 = v8
                                                                                                                                                                                                                                                                        arg1 = v12
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    arg1 = (arg0 + 3)
                                                                                                                                                                                                                                                                    v5 = (arg3 - 3)
                                                                                                                                                                                                                                                                    v6 = ((load8u(arg0 + 2) << v8) + v6)
                                                                                                                                                                                                                                                                    if (u32(arg2) > u32(7)):
                                                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                                                        arg3 = v5
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    arg2 = (arg2 + 24)
                                                                                                                                                                                                                                                                    if not v5:
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
                                                                                                                                                                                                                                                                while True:  # $label57
                                                                                                                                                                                                                                                                    if not (load8u(v4 + 21) & 2):
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    if not (load8u(v4 + 12) & 4):
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    store32(v20 + 12, v6)
                                                                                                                                                                                                                                                                    store32(v4 + 28, func43(load32(v4 + 28), (v20 + 12), 4))
                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                store32(v4 + 4, 16183)
                                                                                                                                                                                                                                                                arg2 = 0
                                                                                                                                                                                                                                                                v6 = 0
                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                            if (u32(arg2) > u32(15)):
                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                        if not arg3:
                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                        arg1 = (arg0 + 1)
                                                                                                                                                                                                                                                        v5 = (arg3 - 1)
                                                                                                                                                                                                                                                        v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                                                        if (u32(arg2) > u32(7)):
                                                                                                                                                                                                                                                            arg0 = arg1
                                                                                                                                                                                                                                                            arg3 = v5
                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                        arg2 = (arg2 + 8)
                                                                                                                                                                                                                                                        if not v5:
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
                                                                                                                                                                                                                                                    while True:  # $label60
                                                                                                                                                                                                                                                        if not (load8u(v4 + 21) & 2):
                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                        if not (load8u(v4 + 12) & 4):
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
                                                                                                                                                                                                                                                if not (load32(v4 + 20) & 1024):
                                                                                                                                                                                                                                                    v5 = arg2
                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                v5 = v6
                                                                                                                                                                                                                                                if (u32(arg2) > u32(15)):
                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                            if not arg3:
                                                                                                                                                                                                                                                arg3 = 0
                                                                                                                                                                                                                                                v6 = v5
                                                                                                                                                                                                                                                arg1 = v12
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                            v8 = (arg0 + 1)
                                                                                                                                                                                                                                            v7 = (arg3 - 1)
                                                                                                                                                                                                                                            v6 = ((load8u(arg0) << arg2) + v5)
                                                                                                                                                                                                                                            if (u32(arg2) > u32(7)):
                                                                                                                                                                                                                                                arg0 = v8
                                                                                                                                                                                                                                                arg3 = v7
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                            arg2 = (arg2 + 8)
                                                                                                                                                                                                                                            if not v7:
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
                                                                                                                                                                                                                                        while True:  # $label64
                                                                                                                                                                                                                                            if not (arg1 & 512):
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                            if not (load8u(v4 + 12) & 4):
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                            store16(v20 + 12, v6)
                                                                                                                                                                                                                                            store32(v4 + 28, func43(load32(v4 + 28), (v20 + 12), 2))
                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                        v6 = 0
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    v8 = (arg2 + 8)
                                                                                                                                                                                                                                    if not v5:
                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                        arg3 = 0
                                                                                                                                                                                                                                        arg2 = v8
                                                                                                                                                                                                                                        arg1 = v12
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    arg1 = (arg0 + 2)
                                                                                                                                                                                                                                    v5 = (arg3 - 2)
                                                                                                                                                                                                                                    v6 = ((load8u(arg0 + 1) << v8) + v6)
                                                                                                                                                                                                                                    if (u32(arg2) > u32(15)):
                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                        arg3 = v5
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    v8 = (arg2 + 16)
                                                                                                                                                                                                                                    if not v5:
                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                        arg3 = 0
                                                                                                                                                                                                                                        arg2 = v8
                                                                                                                                                                                                                                        arg1 = v12
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    arg1 = (arg0 + 3)
                                                                                                                                                                                                                                    v5 = (arg3 - 3)
                                                                                                                                                                                                                                    v6 = ((load8u(arg0 + 2) << v8) + v6)
                                                                                                                                                                                                                                    if (u32(arg2) > u32(7)):
                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                        arg3 = v5
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    arg2 = (arg2 + 24)
                                                                                                                                                                                                                                    if not v5:
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
                                                                                                                                                                                                                            if not load32(v4 + 16):
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
                                                                                                                                                                                                                        while True:  # $label67
                                                                                                                                                                                                                            while True:  # $label66
                                                                                                                                                                                                                                if not load32(v4 + 8):
                                                                                                                                                                                                                                    if (u32(arg2) < u32(3)):
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                store32(v4 + 4, 16206)
                                                                                                                                                                                                                                v6 = ((v6 & 0xFFFFFFFF) >> (arg2 & 7))
                                                                                                                                                                                                                                arg2 = (arg2 & -8)
                                                                                                                                                                                                                                v5 = load32(v4 + 4)
                                                                                                                                                                                                                                continue
                                                                                                                                                                                                                                break
                                                                                                                                                                                                                            if not arg3:
                                                                                                                                                                                                                                break
                                                                                                                                                                                                                            arg3 = (arg3 - 1)
                                                                                                                                                                                                                            v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                            arg0 = (arg0 + 1)
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        arg1 = (arg2 + 8)
                                                                                                                                                                                                                        store32(v4 + 8, (v6 & 1))
                                                                                                                                                                                                                        v5 = 16193
                                                                                                                                                                                                                        while True:  # $label72
                                                                                                                                                                                                                            while True:  # $label71
                                                                                                                                                                                                                                while True:  # $label70
                                                                                                                                                                                                                                    while True:  # $label69
                                                                                                                                                                                                                                        while True:  # $label68
                                                                                                                                                                                                                                            # br_table ((((v6 & 0xFFFFFFFF) >> 1) & 3) - 1)
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
                                                                                                                                                                                                                    while True:  # $label73
                                                                                                                                                                                                                        arg2 = (arg2 & -8)
                                                                                                                                                                                                                        if (u32((arg2 & -8)) > u32(31)):
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        if not arg3:
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        arg1 = (arg2 + 8)
                                                                                                                                                                                                                        v5 = (arg0 + 1)
                                                                                                                                                                                                                        v8 = (arg3 - 1)
                                                                                                                                                                                                                        v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                        if (u32(arg2) > u32(23)):
                                                                                                                                                                                                                            arg0 = v5
                                                                                                                                                                                                                            arg3 = v8
                                                                                                                                                                                                                            arg2 = arg1
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        if not v8:
                                                                                                                                                                                                                            arg0 = v5
                                                                                                                                                                                                                            arg3 = 0
                                                                                                                                                                                                                            arg2 = arg1
                                                                                                                                                                                                                            arg1 = v12
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        v5 = (arg2 + 16)
                                                                                                                                                                                                                        v8 = (arg0 + 2)
                                                                                                                                                                                                                        v7 = (arg3 - 2)
                                                                                                                                                                                                                        v6 = ((load8u(arg0 + 1) << arg1) + v6)
                                                                                                                                                                                                                        if (u32(arg2) > u32(15)):
                                                                                                                                                                                                                            arg0 = v8
                                                                                                                                                                                                                            arg3 = v7
                                                                                                                                                                                                                            arg2 = v5
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        if not v7:
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
                                                                                                                                                                                                                        if not v7:
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
                                                                                                                                                                                                                arg1 = (arg1 if (u32(arg1) < u32(arg3)) else arg3)
                                                                                                                                                                                                                arg1 = ((arg1 if (u32(arg1) < u32(arg3)) else arg3) if (u32(arg1) < u32(v13)) else v13)
                                                                                                                                                                                                                if not ((arg1 if (u32(arg1) < u32(arg3)) else arg3) if (u32(arg1) < u32(v13)) else v13):
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
                                                                                                                                                                                                        if not v8:
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
                                                                                                                                                                                                    if not ((u32(v5) < u32(30)) & (u32(arg1) <= u32(29))):
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
                                                                                                                                                                                                if (u32(load32(v4 + 108)) < u32(load32(v4 + 96))):
                                                                                                                                                                                                    break
                                                                                                                                                                                                break
                                                                                                                                                                                                break
                                                                                                                                                                                            if not v13:
                                                                                                                                                                                                break
                                                                                                                                                                                            store8(v14, load32(v4 + 68))
                                                                                                                                                                                            store32(v4 + 4, 16200)
                                                                                                                                                                                            v13 = (v13 - 1)
                                                                                                                                                                                            v14 = (v14 + 1)
                                                                                                                                                                                            v5 = load32(v4 + 4)
                                                                                                                                                                                            continue
                                                                                                                                                                                            break
                                                                                                                                                                                        v5 = load32(v4 + 12)
                                                                                                                                                                                        if not load32(v4 + 12):
                                                                                                                                                                                            v5 = 0
                                                                                                                                                                                            break
                                                                                                                                                                                        while True:  # $label79
                                                                                                                                                                                            if (u32(arg2) > u32(31)):
                                                                                                                                                                                                v8 = arg0
                                                                                                                                                                                                break
                                                                                                                                                                                            if not arg3:
                                                                                                                                                                                                break
                                                                                                                                                                                            arg1 = (arg2 + 8)
                                                                                                                                                                                            v8 = (arg0 + 1)
                                                                                                                                                                                            v7 = (arg3 - 1)
                                                                                                                                                                                            v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                            if (u32(arg2) > u32(23)):
                                                                                                                                                                                                arg3 = v7
                                                                                                                                                                                                arg2 = arg1
                                                                                                                                                                                                break
                                                                                                                                                                                            if not v7:
                                                                                                                                                                                                arg0 = v8
                                                                                                                                                                                                arg3 = 0
                                                                                                                                                                                                arg2 = arg1
                                                                                                                                                                                                arg1 = v12
                                                                                                                                                                                                break
                                                                                                                                                                                            v7 = (arg2 + 16)
                                                                                                                                                                                            v8 = (arg0 + 2)
                                                                                                                                                                                            v9 = (arg3 - 2)
                                                                                                                                                                                            v6 = ((load8u(arg0 + 1) << arg1) + v6)
                                                                                                                                                                                            if (u32(arg2) > u32(15)):
                                                                                                                                                                                                arg3 = v9
                                                                                                                                                                                                arg2 = v7
                                                                                                                                                                                                break
                                                                                                                                                                                            if not v9:
                                                                                                                                                                                                arg0 = v8
                                                                                                                                                                                                arg3 = 0
                                                                                                                                                                                                arg2 = v7
                                                                                                                                                                                                arg1 = v12
                                                                                                                                                                                                break
                                                                                                                                                                                            arg1 = (arg2 + 24)
                                                                                                                                                                                            v8 = (arg0 + 3)
                                                                                                                                                                                            v9 = (arg3 - 3)
                                                                                                                                                                                            v6 = ((load8u(arg0 + 2) << v7) + v6)
                                                                                                                                                                                            if (u32(arg2) > u32(7)):
                                                                                                                                                                                                arg3 = v9
                                                                                                                                                                                                arg2 = arg1
                                                                                                                                                                                                break
                                                                                                                                                                                            if not v9:
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
                                                                                                                                                                                        while True:  # $label80
                                                                                                                                                                                            arg1 = (v5 & 4)
                                                                                                                                                                                            if not (v5 & 4):
                                                                                                                                                                                                break
                                                                                                                                                                                            if (v13 == v18):
                                                                                                                                                                                                break
                                                                                                                                                                                            arg1 = (v14 - arg0)
                                                                                                                                                                                            v5 = load32(v4 + 28)
                                                                                                                                                                                            while True:  # $label81
                                                                                                                                                                                                if load32(v4 + 20):
                                                                                                                                                                                                    break
                                                                                                                                                                                                break
                                                                                                                                                                                            arg0 = func89(v5, arg1, arg0)
                                                                                                                                                                                            store32(func43(v5, arg1, arg0) + 28, func89(v5, arg1, arg0))
                                                                                                                                                                                            store32(v10 + 48, arg0)
                                                                                                                                                                                            v5 = load32(v4 + 12)
                                                                                                                                                                                            arg1 = (load32(v4 + 12) & 4)
                                                                                                                                                                                            break
                                                                                                                                                                                        if not arg1:
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
                                                                                                                                                                            if (u32(arg2) <= u32(2)):
                                                                                                                                                                                if not arg3:
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
                                                                                                                                                                    if (u32(v5) <= u32(18)):
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
                                                                                                                                                                        if (u32((v5 - 16)) >= u32(3)):
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
                                                                                                                                                                if (u32((load32(v4 + 100) + load32(v4 + 104))) > u32(v5)):
                                                                                                                                                                    v21 = ((-1 << load32(v4 + 88)) ^ -1)
                                                                                                                                                                    v17 = load32(v4 + 80)
                                                                                                                                                                    while True:  # $label103
                                                                                                                                                                        v9 = arg2
                                                                                                                                                                        v8 = arg3
                                                                                                                                                                        v7 = arg0
                                                                                                                                                                        while True:  # $label87
                                                                                                                                                                            v15 = (v6 & v21)
                                                                                                                                                                            v11 = load8u((v17 + ((v6 & v21) << 2)) + 1)
                                                                                                                                                                            if (u32(load8u((v17 + ((v6 & v21) << 2)) + 1)) <= u32(arg2)):
                                                                                                                                                                                arg1 = arg2
                                                                                                                                                                                break
                                                                                                                                                                            while True:  # $label89
                                                                                                                                                                                if not v8:
                                                                                                                                                                                    break
                                                                                                                                                                                v11 = (load8u(v7) << v9)
                                                                                                                                                                                v7 = (v7 + 1)
                                                                                                                                                                                v8 = (v8 - 1)
                                                                                                                                                                                arg1 = (v9 + 8)
                                                                                                                                                                                v9 = (v9 + 8)
                                                                                                                                                                                v6 = (v6 + v11)
                                                                                                                                                                                v15 = ((v6 + v11) & v21)
                                                                                                                                                                                v11 = load8u((v17 + (((v6 + v11) & v21) << 2)) + 1)
                                                                                                                                                                                if (u32(arg1) < u32(load8u((v17 + (((v6 + v11) & v21) << 2)) + 1))):
                                                                                                                                                                                    continue
                                                                                                                                                                                break
                                                                                                                                                                            arg0 = v7
                                                                                                                                                                            arg3 = v8
                                                                                                                                                                            break
                                                                                                                                                                        while True:  # $label90
                                                                                                                                                                            arg2 = load16u((v17 + (v15 << 2)) + 2)
                                                                                                                                                                            if (u32(load16u((v17 + (v15 << 2)) + 2)) <= u32(15)):
                                                                                                                                                                                v8 = (v5 + 1)
                                                                                                                                                                                store32(v4 + 108, (v5 + 1))
                                                                                                                                                                                store16((v4 + (v5 << 1)) + 116, arg2)
                                                                                                                                                                                arg2 = (arg1 - v11)
                                                                                                                                                                                v6 = ((v6 & 0xFFFFFFFF) >> v11)
                                                                                                                                                                                v5 = v8
                                                                                                                                                                                break
                                                                                                                                                                            while True:  # $label96
                                                                                                                                                                                while True:  # $label98
                                                                                                                                                                                    while True:  # $label93
                                                                                                                                                                                        while True:  # $label92
                                                                                                                                                                                            while True:  # $label91
                                                                                                                                                                                                # br_table (arg2 - 16)
                                                                                                                                                                                                break
                                                                                                                                                                                                break
                                                                                                                                                                                            arg2 = (v11 + 2)
                                                                                                                                                                                            if (u32((v11 + 2)) > u32(arg1)):
                                                                                                                                                                                                while True:  # $label95
                                                                                                                                                                                                    if not arg3:
                                                                                                                                                                                                        break
                                                                                                                                                                                                    arg3 = (arg3 - 1)
                                                                                                                                                                                                    v6 = ((load8u(arg0) << arg1) + v6)
                                                                                                                                                                                                    arg0 = (arg0 + 1)
                                                                                                                                                                                                    arg1 = (arg1 + 8)
                                                                                                                                                                                                    if (u32((arg1 + 8)) < u32(arg2)):
                                                                                                                                                                                                        continue
                                                                                                                                                                                                    break
                                                                                                                                                                                            arg2 = (arg1 - v11)
                                                                                                                                                                                            arg1 = ((v6 & 0xFFFFFFFF) >> v11)
                                                                                                                                                                                            if not v5:
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
                                                                                                                                                                                        if (u32((v11 + 3)) > u32(arg1)):
                                                                                                                                                                                            while True:  # $label97
                                                                                                                                                                                                if not arg3:
                                                                                                                                                                                                    break
                                                                                                                                                                                                arg3 = (arg3 - 1)
                                                                                                                                                                                                v6 = ((load8u(arg0) << arg1) + v6)
                                                                                                                                                                                                arg0 = (arg0 + 1)
                                                                                                                                                                                                arg1 = (arg1 + 8)
                                                                                                                                                                                                if (u32((arg1 + 8)) < u32(arg2)):
                                                                                                                                                                                                    continue
                                                                                                                                                                                                break
                                                                                                                                                                                        arg2 = ((arg1 - v11) - 3)
                                                                                                                                                                                        arg1 = ((v6 & 0xFFFFFFFF) >> v11)
                                                                                                                                                                                        v6 = ((((v6 & 0xFFFFFFFF) >> v11) & 0xFFFFFFFF) >> 3)
                                                                                                                                                                                        break
                                                                                                                                                                                        break
                                                                                                                                                                                    arg2 = (v11 + 7)
                                                                                                                                                                                    if (u32((v11 + 7)) > u32(arg1)):
                                                                                                                                                                                        while True:  # $label99
                                                                                                                                                                                            if not arg3:
                                                                                                                                                                                                break
                                                                                                                                                                                            arg3 = (arg3 - 1)
                                                                                                                                                                                            v6 = ((load8u(arg0) << arg1) + v6)
                                                                                                                                                                                            arg0 = (arg0 + 1)
                                                                                                                                                                                            arg1 = (arg1 + 8)
                                                                                                                                                                                            if (u32((arg1 + 8)) < u32(arg2)):
                                                                                                                                                                                                continue
                                                                                                                                                                                            break
                                                                                                                                                                                    arg2 = ((arg1 - v11) - 7)
                                                                                                                                                                                    arg1 = ((v6 & 0xFFFFFFFF) >> v11)
                                                                                                                                                                                    v6 = ((((v6 & 0xFFFFFFFF) >> v11) & 0xFFFFFFFF) >> 7)
                                                                                                                                                                                    break
                                                                                                                                                                                v8 = ((arg1 & 127) + 11)
                                                                                                                                                                                break
                                                                                                                                                                            arg1 = 0
                                                                                                                                                                            if (u32((v5 + v8)) > u32(v19)):
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
                                                                                                                                                                            if (u32(v9) >= u32(3)):
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
                                                                                                                                                                        if (u32(v5) < u32(v19)):
                                                                                                                                                                            continue
                                                                                                                                                                        break
                                                                                                                                                                if not load16u(v4 + 628):
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
                                                                                                                                                        while True:  # $label104
                                                                                                                                                            if (u32(arg3) < u32(6)):
                                                                                                                                                                break
                                                                                                                                                            if (u32(v13) < u32(258)):
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
                                                                                                                                                            while True:  # $label130
                                                                                                                                                                while True:  # $label112
                                                                                                                                                                    while True:  # $label131
                                                                                                                                                                        if (u32(v6) <= u32(14)):
                                                                                                                                                                            v11 = (((load8u(arg2) << v6) + v11) + (load8u(arg2 + 1) << (v6 + 8)))
                                                                                                                                                                            v6 = (v6 + 16)
                                                                                                                                                                            arg2 = (arg2 + 2)
                                                                                                                                                                        arg3 = (v38 + ((v11 & v45) << 2))
                                                                                                                                                                        arg0 = load8u((v38 + ((v11 & v45) << 2)) + 1)
                                                                                                                                                                        v6 = (v6 - load8u((v38 + ((v11 & v45) << 2)) + 1))
                                                                                                                                                                        v11 = ((v11 & 0xFFFFFFFF) >> arg0)
                                                                                                                                                                        while True:  # $label110
                                                                                                                                                                            while True:  # $label105
                                                                                                                                                                                while True:  # $label108
                                                                                                                                                                                    while True:  # $label111
                                                                                                                                                                                        arg0 = load8u(arg3)
                                                                                                                                                                                        if not load8u(arg3):
                                                                                                                                                                                            store8(v7, load8u(arg3 + 2))
                                                                                                                                                                                            v7 = (v7 + 1)
                                                                                                                                                                                            break
                                                                                                                                                                                        if (arg0 & 16):
                                                                                                                                                                                            v13 = load16u(arg3 + 2)
                                                                                                                                                                                            while True:  # $label106
                                                                                                                                                                                                arg0 = (arg0 & 15)
                                                                                                                                                                                                if not (arg0 & 15):
                                                                                                                                                                                                    arg1 = arg2
                                                                                                                                                                                                    break
                                                                                                                                                                                                while True:  # $label107
                                                                                                                                                                                                    if (u32(arg0) <= u32(v6)):
                                                                                                                                                                                                        arg1 = arg2
                                                                                                                                                                                                        break
                                                                                                                                                                                                    arg1 = (arg2 + 1)
                                                                                                                                                                                                    v11 = ((load8u(arg2) << v6) + v11)
                                                                                                                                                                                                    break
                                                                                                                                                                                                v6 = ((v6 + 8) - arg0)
                                                                                                                                                                                                v13 = ((v11 & ((-1 << arg0) ^ -1)) + v13)
                                                                                                                                                                                                break
                                                                                                                                                                                            arg0 = ((v11 & 0xFFFFFFFF) >> arg0)
                                                                                                                                                                                            if (u32(v6) <= u32(14)):
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
                                                                                                                                                                                                if not (arg0 & 64):
                                                                                                                                                                                                    arg3 = ((v37 + (load16u(arg3 + 2) << 2)) + ((v11 & ((-1 << arg0) ^ -1)) << 2))
                                                                                                                                                                                                    arg0 = load8u(((v37 + (load16u(arg3 + 2) << 2)) + ((v11 & ((-1 << arg0) ^ -1)) << 2)) + 1)
                                                                                                                                                                                                    v6 = (v6 - load8u(((v37 + (load16u(arg3 + 2) << 2)) + ((v11 & ((-1 << arg0) ^ -1)) << 2)) + 1))
                                                                                                                                                                                                    v11 = ((v11 & 0xFFFFFFFF) >> arg0)
                                                                                                                                                                                                    arg0 = load8u(arg3)
                                                                                                                                                                                                    if not (load8u(arg3) & 16):
                                                                                                                                                                                                        continue
                                                                                                                                                                                                    break
                                                                                                                                                                                                break
                                                                                                                                                                                            v13 = 4865
                                                                                                                                                                                            arg2 = arg1
                                                                                                                                                                                            break
                                                                                                                                                                                        if not (arg0 & 64):
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
                                                                                                                                                                                while True:  # $label113
                                                                                                                                                                                    arg3 = (arg0 & 15)
                                                                                                                                                                                    if (u32((arg0 & 15)) <= u32(v6)):
                                                                                                                                                                                        arg0 = v6
                                                                                                                                                                                        break
                                                                                                                                                                                    v11 = ((load8u(arg1) << v6) + v11)
                                                                                                                                                                                    arg0 = (v6 + 8)
                                                                                                                                                                                    if (u32(arg3) <= u32((v6 + 8))):
                                                                                                                                                                                        break
                                                                                                                                                                                    v11 = ((load8u(arg1 + 1) << arg0) + v11)
                                                                                                                                                                                    arg0 = (v6 + 16)
                                                                                                                                                                                    break
                                                                                                                                                                                arg2 = (arg1 + 2)
                                                                                                                                                                                arg1 = (v11 & ((-1 << arg3) ^ -1))
                                                                                                                                                                                v6 = (arg0 - arg3)
                                                                                                                                                                                v11 = ((v11 & 0xFFFFFFFF) >> arg3)
                                                                                                                                                                                while True:  # $label128
                                                                                                                                                                                    v17 = (arg1 + v15)
                                                                                                                                                                                    arg0 = (v7 - v43)
                                                                                                                                                                                    if (u32((arg1 + v15)) > u32((v7 - v43))):
                                                                                                                                                                                        while True:  # $label114
                                                                                                                                                                                            v5 = (v17 - arg0)
                                                                                                                                                                                            if (u32((v17 - arg0)) <= u32(v46)):
                                                                                                                                                                                                break
                                                                                                                                                                                            if not load32(v14 + 7108):
                                                                                                                                                                                                break
                                                                                                                                                                                            v13 = 4158
                                                                                                                                                                                            break
                                                                                                                                                                                            break
                                                                                                                                                                                        while True:  # $label115
                                                                                                                                                                                            while True:  # $label117
                                                                                                                                                                                                if not v9:
                                                                                                                                                                                                    arg3 = (v8 + (v41 - v5))
                                                                                                                                                                                                    if (u32(v5) >= u32(v13)):
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
                                                                                                                                                                                                    if (u32(v15) < u32(7)):
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
                                                                                                                                                                                                if (u32(v5) > u32(v9)):
                                                                                                                                                                                                    arg3 = (v8 + (v42 - v5))
                                                                                                                                                                                                    v5 = (v5 - v9)
                                                                                                                                                                                                    if (u32(v13) <= u32((v5 - v9))):
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
                                                                                                                                                                                                    if (u32(v15) >= u32(7)):
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
                                                                                                                                                                                                    if (u32(v9) >= u32((v13 - v5))):
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
                                                                                                                                                                                                    if (u32(v9) >= u32(8)):
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
                                                                                                                                                                                                if (u32(v5) >= u32(v13)):
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
                                                                                                                                                                                                if (u32(v15) < u32(7)):
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
                                                                                                                                                                                        while True:  # $label125
                                                                                                                                                                                            if (u32(v13) < u32(3)):
                                                                                                                                                                                                break
                                                                                                                                                                                            arg0 = 0
                                                                                                                                                                                            arg1 = (v13 - 3)
                                                                                                                                                                                            # TODO: i32.div_u
                                                                                                                                                                                            v5 = (4 & 3)
                                                                                                                                                                                            if (4 & 3):
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
                                                                                                                                                                                            if (u32(arg1) < u32(9)):
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
                                                                                                                                                                                                if (u32((v13 - 12)) > u32(2)):
                                                                                                                                                                                                    continue
                                                                                                                                                                                                break
                                                                                                                                                                                            break
                                                                                                                                                                                        if not v13:
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
                                                                                                                                                                                        if (u32((v13 - 3)) > u32(2)):
                                                                                                                                                                                            continue
                                                                                                                                                                                        break
                                                                                                                                                                                    if not v13:
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
                                                                                                                                                                            if (u32(arg2) >= u32(v36)):
                                                                                                                                                                                break
                                                                                                                                                                            if (u32(v7) < u32(v28)):
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
                                                                                                                                                        while True:  # $label132
                                                                                                                                                            v19 = load32(v4 + 80)
                                                                                                                                                            v15 = ((-1 << load32(v4 + 88)) ^ -1)
                                                                                                                                                            v11 = (load32(v4 + 80) + ((v6 & ((-1 << load32(v4 + 88)) ^ -1)) << 2))
                                                                                                                                                            v9 = load8u((load32(v4 + 80) + ((v6 & ((-1 << load32(v4 + 88)) ^ -1)) << 2)) + 1)
                                                                                                                                                            if (u32(load8u((load32(v4 + 80) + ((v6 & ((-1 << load32(v4 + 88)) ^ -1)) << 2)) + 1)) <= u32(arg2)):
                                                                                                                                                                v7 = arg2
                                                                                                                                                                break
                                                                                                                                                            while True:  # $label134
                                                                                                                                                                if not v5:
                                                                                                                                                                    break
                                                                                                                                                                v9 = (load8u(arg1) << v8)
                                                                                                                                                                arg1 = (arg1 + 1)
                                                                                                                                                                v5 = (v5 - 1)
                                                                                                                                                                v7 = (v8 + 8)
                                                                                                                                                                v8 = (v8 + 8)
                                                                                                                                                                v6 = (v6 + v9)
                                                                                                                                                                v11 = (v19 + (((v6 + v9) & v15) << 2))
                                                                                                                                                                v9 = load8u((v19 + (((v6 + v9) & v15) << 2)) + 1)
                                                                                                                                                                if (u32(v7) < u32(load8u((v19 + (((v6 + v9) & v15) << 2)) + 1))):
                                                                                                                                                                    continue
                                                                                                                                                                break
                                                                                                                                                            break
                                                                                                                                                        v15 = load16u(v11 + 2)
                                                                                                                                                        while True:  # $label135
                                                                                                                                                            v8 = load8u(v11)
                                                                                                                                                            if (u32(((load8u(v11) - 1) & 255)) > u32(14)):
                                                                                                                                                                v11 = v9
                                                                                                                                                                v9 = 0
                                                                                                                                                                arg0 = arg1
                                                                                                                                                                arg3 = v5
                                                                                                                                                                break
                                                                                                                                                            arg3 = v5
                                                                                                                                                            arg0 = arg1
                                                                                                                                                            while True:  # $label136
                                                                                                                                                                arg2 = v7
                                                                                                                                                                v21 = ((-1 << (v8 + v9)) ^ -1)
                                                                                                                                                                v17 = (v19 + (((((v6 & ((-1 << (v8 + v9)) ^ -1)) & 0xFFFFFFFF) >> v9) + v15) << 2))
                                                                                                                                                                v11 = load8u((v19 + (((((v6 & ((-1 << (v8 + v9)) ^ -1)) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1)
                                                                                                                                                                if (u32(v7) >= u32((v9 + load8u((v19 + (((((v6 & ((-1 << (v8 + v9)) ^ -1)) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1)))):
                                                                                                                                                                    v8 = v7
                                                                                                                                                                    break
                                                                                                                                                                while True:  # $label138
                                                                                                                                                                    if not arg3:
                                                                                                                                                                        break
                                                                                                                                                                    v11 = (load8u(arg0) << arg2)
                                                                                                                                                                    arg0 = (arg0 + 1)
                                                                                                                                                                    arg3 = (arg3 - 1)
                                                                                                                                                                    v8 = (arg2 + 8)
                                                                                                                                                                    arg2 = (arg2 + 8)
                                                                                                                                                                    v6 = (v6 + v11)
                                                                                                                                                                    v17 = (v19 + ((((((v6 + v11) & v21) & 0xFFFFFFFF) >> v9) + v15) << 2))
                                                                                                                                                                    v11 = load8u((v19 + ((((((v6 + v11) & v21) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1)
                                                                                                                                                                    if (u32((v9 + load8u((v19 + ((((((v6 + v11) & v21) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1))) > u32(v8)):
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
                                                                                                                                                        if not (v8 & 255):
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
                                                                                                                                                    while True:  # $label139
                                                                                                                                                        if not v8:
                                                                                                                                                            arg1 = load32(v4 + 68)
                                                                                                                                                            break
                                                                                                                                                        v5 = arg2
                                                                                                                                                        arg1 = arg0
                                                                                                                                                        if (u32(arg2) < u32(v8)):
                                                                                                                                                            while True:  # $label141
                                                                                                                                                                if not arg3:
                                                                                                                                                                    break
                                                                                                                                                                arg3 = (arg3 - 1)
                                                                                                                                                                v6 = ((load8u(arg1) << v5) + v6)
                                                                                                                                                                arg0 = (arg1 + 1)
                                                                                                                                                                arg1 = (arg1 + 1)
                                                                                                                                                                v5 = (v5 + 8)
                                                                                                                                                                if (u32((v5 + 8)) < u32(v8)):
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
                                                                                                                                                while True:  # $label142
                                                                                                                                                    v19 = load32(v4 + 84)
                                                                                                                                                    v15 = ((-1 << load32(v4 + 92)) ^ -1)
                                                                                                                                                    v11 = (load32(v4 + 84) + ((v6 & ((-1 << load32(v4 + 92)) ^ -1)) << 2))
                                                                                                                                                    v9 = load8u((load32(v4 + 84) + ((v6 & ((-1 << load32(v4 + 92)) ^ -1)) << 2)) + 1)
                                                                                                                                                    if (u32(load8u((load32(v4 + 84) + ((v6 & ((-1 << load32(v4 + 92)) ^ -1)) << 2)) + 1)) <= u32(arg2)):
                                                                                                                                                        v7 = arg2
                                                                                                                                                        break
                                                                                                                                                    while True:  # $label144
                                                                                                                                                        if not v5:
                                                                                                                                                            break
                                                                                                                                                        v9 = (load8u(arg1) << v8)
                                                                                                                                                        arg1 = (arg1 + 1)
                                                                                                                                                        v5 = (v5 - 1)
                                                                                                                                                        v7 = (v8 + 8)
                                                                                                                                                        v8 = (v8 + 8)
                                                                                                                                                        v6 = (v6 + v9)
                                                                                                                                                        v11 = (v19 + (((v6 + v9) & v15) << 2))
                                                                                                                                                        v9 = load8u((v19 + (((v6 + v9) & v15) << 2)) + 1)
                                                                                                                                                        if (u32(v7) < u32(load8u((v19 + (((v6 + v9) & v15) << 2)) + 1))):
                                                                                                                                                            continue
                                                                                                                                                        break
                                                                                                                                                    break
                                                                                                                                                v15 = load16u(v11 + 2)
                                                                                                                                                while True:  # $label145
                                                                                                                                                    v8 = load8u(v11)
                                                                                                                                                    if (u32(load8u(v11)) >= u32(16)):
                                                                                                                                                        v11 = v9
                                                                                                                                                        break
                                                                                                                                                    arg3 = v5
                                                                                                                                                    arg0 = arg1
                                                                                                                                                    while True:  # $label146
                                                                                                                                                        arg2 = v7
                                                                                                                                                        v21 = ((-1 << (v8 + v9)) ^ -1)
                                                                                                                                                        v17 = (v19 + (((((v6 & ((-1 << (v8 + v9)) ^ -1)) & 0xFFFFFFFF) >> v9) + v15) << 2))
                                                                                                                                                        v11 = load8u((v19 + (((((v6 & ((-1 << (v8 + v9)) ^ -1)) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1)
                                                                                                                                                        if (u32(v7) >= u32((v9 + load8u((v19 + (((((v6 & ((-1 << (v8 + v9)) ^ -1)) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1)))):
                                                                                                                                                            v8 = v7
                                                                                                                                                            break
                                                                                                                                                        while True:  # $label148
                                                                                                                                                            if not arg3:
                                                                                                                                                                break
                                                                                                                                                            v11 = (load8u(arg0) << arg2)
                                                                                                                                                            arg0 = (arg0 + 1)
                                                                                                                                                            arg3 = (arg3 - 1)
                                                                                                                                                            v8 = (arg2 + 8)
                                                                                                                                                            arg2 = (arg2 + 8)
                                                                                                                                                            v6 = (v6 + v11)
                                                                                                                                                            v17 = (v19 + ((((((v6 + v11) & v21) & 0xFFFFFFFF) >> v9) + v15) << 2))
                                                                                                                                                            v11 = load8u((v19 + ((((((v6 + v11) & v21) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1)
                                                                                                                                                            if (u32((v9 + load8u((v19 + ((((((v6 + v11) & v21) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1))) > u32(v8)):
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
                                                                                                                                            while True:  # $label149
                                                                                                                                                if not v9:
                                                                                                                                                    arg0 = arg1
                                                                                                                                                    arg3 = v5
                                                                                                                                                    break
                                                                                                                                                v8 = arg2
                                                                                                                                                arg3 = v5
                                                                                                                                                v7 = arg1
                                                                                                                                                while True:  # $label150
                                                                                                                                                    if (u32(arg2) >= u32(v9)):
                                                                                                                                                        arg0 = arg1
                                                                                                                                                        break
                                                                                                                                                    while True:  # $label152
                                                                                                                                                        if not arg3:
                                                                                                                                                            break
                                                                                                                                                        arg3 = (arg3 - 1)
                                                                                                                                                        v6 = ((load8u(v7) << v8) + v6)
                                                                                                                                                        arg0 = (v7 + 1)
                                                                                                                                                        v7 = (v7 + 1)
                                                                                                                                                        v8 = (v8 + 8)
                                                                                                                                                        if (u32((v8 + 8)) < u32(v9)):
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
                                                                                                                                while True:  # $label156
                                                                                                                                    arg1 = load32(v4 + 72)
                                                                                                                                    v5 = (v18 - v13)
                                                                                                                                    if (u32(load32(v4 + 72)) > u32((v18 - v13))):
                                                                                                                                        while True:  # $label154
                                                                                                                                            arg1 = (arg1 - v5)
                                                                                                                                            if (u32((arg1 - v5)) <= u32(load32(v4 + 48))):
                                                                                                                                                break
                                                                                                                                            if not load32(v4 + 7108):
                                                                                                                                                break
                                                                                                                                            store32(v10 + 24, 4158)
                                                                                                                                            store32(v4 + 4, 16209)
                                                                                                                                            v5 = load32(v4 + 4)
                                                                                                                                            continue
                                                                                                                                            break
                                                                                                                                        while True:  # $label155
                                                                                                                                            v5 = load32(v4 + 52)
                                                                                                                                            if (u32(load32(v4 + 52)) < u32(arg1)):
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
                                                                                                                                v7 = (arg1 if (u32(arg1) < u32(v13)) else v13)
                                                                                                                                store32(v4 + 68, (v8 - (arg1 if (u32(arg1) < u32(v13)) else v13)))
                                                                                                                                v9 = (v7 - 1)
                                                                                                                                v8 = 0
                                                                                                                                v11 = (v7 & 7)
                                                                                                                                if not (v7 & 7):
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
                                                                                        if (u32(v9) >= u32(7)):
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
                                                                        arg1 = (load32(v4 + 68) if (u32(arg3) > u32(v5)) else arg3)
                                                                        if (load32(v4 + 68) if (u32(arg3) > u32(v5)) else arg3):
                                                                            while True:  # $label161
                                                                                v7 = load32(v4 + 36)
                                                                                if not load32(v4 + 36):
                                                                                    break
                                                                                v11 = load32(v7 + 16)
                                                                                if not load32(v7 + 16):
                                                                                    break
                                                                                v9 = load32(v7 + 24)
                                                                                v5 = (load32(v7 + 20) - v5)
                                                                                if (u32(load32(v7 + 24)) <= u32((load32(v7 + 20) - v5))):
                                                                                    break
                                                                                v8 = load32(v4 + 20)
                                                                                break
                                                                            while True:  # $label162
                                                                                if not (v8 & 512):
                                                                                    break
                                                                                if not (load8u(v4 + 12) & 4):
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
                                                                while True:  # $label167
                                                                    if (load8u(v4 + 21) & 8):
                                                                        v5 = 0
                                                                        if not arg3:
                                                                            break
                                                                        while True:  # $label165
                                                                            arg1 = load8u((arg0 + v5))
                                                                            while True:  # $label164
                                                                                v8 = load32(v4 + 36)
                                                                                if not load32(v4 + 36):
                                                                                    break
                                                                                v9 = load32(v8 + 28)
                                                                                if not load32(v8 + 28):
                                                                                    break
                                                                                v7 = load32(v4 + 68)
                                                                                if (u32(load32(v4 + 68)) >= u32(load32(v8 + 32))):
                                                                                    break
                                                                                store32(v4 + 68, (v7 + 1))
                                                                                store8((v7 + v9), arg1)
                                                                                break
                                                                            v5 = (v5 + 1)
                                                                            if (arg1 if (u32(arg3) > u32((v5 + 1))) else 0):
                                                                                continue
                                                                            break
                                                                        while True:  # $label166
                                                                            if not (load8u(v4 + 21) & 2):
                                                                                break
                                                                            if not (load8u(v4 + 12) & 4):
                                                                                break
                                                                            store32(v4 + 28, func43(load32(v4 + 28), arg0, v5))
                                                                            break
                                                                        arg0 = (arg0 + v5)
                                                                        arg3 = (arg3 - v5)
                                                                        if not arg1:
                                                                            break
                                                                        break
                                                                    arg1 = load32(v4 + 36)
                                                                    if not load32(v4 + 36):
                                                                        break
                                                                    store32(arg1 + 28, 0)
                                                                    break
                                                                store32(v4 + 4, 16187)
                                                                store32(v4 + 68, 0)
                                                                break
                                                            while True:  # $label171
                                                                if (load8u(v4 + 21) & 16):
                                                                    v5 = 0
                                                                    if not arg3:
                                                                        break
                                                                    while True:  # $label169
                                                                        arg1 = load8u((arg0 + v5))
                                                                        while True:  # $label168
                                                                            v8 = load32(v4 + 36)
                                                                            if not load32(v4 + 36):
                                                                                break
                                                                            v9 = load32(v8 + 36)
                                                                            if not load32(v8 + 36):
                                                                                break
                                                                            v7 = load32(v4 + 68)
                                                                            if (u32(load32(v4 + 68)) >= u32(load32(v8 + 40))):
                                                                                break
                                                                            store32(v4 + 68, (v7 + 1))
                                                                            store8((v7 + v9), arg1)
                                                                            break
                                                                        v5 = (v5 + 1)
                                                                        if (arg1 if (u32(arg3) > u32((v5 + 1))) else 0):
                                                                            continue
                                                                        break
                                                                    while True:  # $label170
                                                                        if not (load8u(v4 + 21) & 2):
                                                                            break
                                                                        if not (load8u(v4 + 12) & 4):
                                                                            break
                                                                        store32(v4 + 28, func43(load32(v4 + 28), arg0, v5))
                                                                        break
                                                                    arg0 = (arg0 + v5)
                                                                    arg3 = (arg3 - v5)
                                                                    if not arg1:
                                                                        break
                                                                    break
                                                                arg1 = load32(v4 + 36)
                                                                if not load32(v4 + 36):
                                                                    break
                                                                store32(arg1 + 36, 0)
                                                                break
                                                            store32(v4 + 4, 16188)
                                                            break
                                                        v7 = load32(v4 + 20)
                                                        if (load32(v4 + 20) & 512):
                                                            while True:  # $label172
                                                                if (u32(arg2) > u32(15)):
                                                                    v5 = arg0
                                                                    break
                                                                if not arg3:
                                                                    break
                                                                arg1 = (arg2 + 8)
                                                                v5 = (arg0 + 1)
                                                                v8 = (arg3 - 1)
                                                                v6 = ((load8u(arg0) << arg2) + v6)
                                                                if (u32(arg2) > u32(7)):
                                                                    arg3 = v8
                                                                    arg2 = arg1
                                                                    break
                                                                if not v8:
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
                                                            while True:  # $label173
                                                                if not (load8u(v4 + 12) & 4):
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
                                        if not v5:
                                            break
                                        if not load32(v4 + 20):
                                            break
                                        while True:  # $label175
                                            if (u32(arg2) > u32(31)):
                                                arg1 = arg0
                                                break
                                            if not arg3:
                                                break
                                            v8 = (arg2 + 8)
                                            arg1 = (arg0 + 1)
                                            v7 = (arg3 - 1)
                                            v6 = ((load8u(arg0) << arg2) + v6)
                                            if (u32(arg2) > u32(23)):
                                                arg3 = v7
                                                arg2 = v8
                                                break
                                            if not v7:
                                                arg0 = arg1
                                                arg3 = 0
                                                arg2 = v8
                                                arg1 = v12
                                                break
                                            v7 = (arg2 + 16)
                                            arg1 = (arg0 + 2)
                                            v9 = (arg3 - 2)
                                            v6 = ((load8u(arg0 + 1) << v8) + v6)
                                            if (u32(arg2) > u32(15)):
                                                arg3 = v9
                                                arg2 = v7
                                                break
                                            if not v9:
                                                arg0 = arg1
                                                arg3 = 0
                                                arg2 = v7
                                                arg1 = v12
                                                break
                                            v8 = (arg2 + 24)
                                            arg1 = (arg0 + 3)
                                            v9 = (arg3 - 3)
                                            v6 = ((load8u(arg0 + 2) << v7) + v6)
                                            if (u32(arg2) > u32(7)):
                                                arg3 = v9
                                                arg2 = v8
                                                break
                                            if not v9:
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
                                        while True:  # $label176
                                            if not (v5 & 4):
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
                    while True:  # $label182
                        while True:  # $label178
                            if not load32(v4 + 44):
                                if (v13 == v18):
                                    break
                                if (u32(load32(v4 + 4)) > u32(16208)):
                                    break
                            while True:  # $label181
                                arg2 = (v18 - v13)
                                while True:  # $label180
                                    while True:  # $label179
                                        arg0 = load32(v10 + 28)
                                        v12 = load32(load32(v10 + 28) + 56)
                                        if not load32(load32(v10 + 28) + 56):
                                            v5 = 1
                                            v12 = call_table(load32(v10 + 32))
                                            store32(1 + 56, call_table(load32(v10 + 32)))
                                            if not v12:
                                                break
                                        arg3 = load32(arg0 + 44)
                                        if not load32(arg0 + 44):
                                            store64(arg0 + 48, 0)
                                            arg3 = (1 << load32(arg0 + 40))
                                            store32(arg0 + 44, (1 << load32(arg0 + 40)))
                                        if (u32(arg2) >= u32(arg3)):
                                            store32(arg0 + 52, 0)
                                            break
                                        v5 = load32(arg0 + 52)
                                        arg3 = (arg3 - v5)
                                        v12 = (u32(arg2) > u32(arg3))
                                        arg3 = ((arg3 - v5) if (u32(arg2) > u32(arg3)) else arg2)
                                        if v12:
                                            arg2 = (arg2 - arg3)
                                            store32(arg0 + 52, arg2)
                                            break
                                        v5 = 0
                                        arg2 = (load32(arg0 + 52) + arg3)
                                        v12 = load32(arg0 + 44)
                                        store32(arg0 + 52, ((load32(arg0 + 52) + arg3) if (arg2 != load32(arg0 + 44)) else 0))
                                        arg2 = load32(arg0 + 48)
                                        if (u32(load32(arg0 + 48)) >= u32(v12)):
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
                        while True:  # $label183
                            if not (load8u(v4 + 12) & 4):
                                break
                            if (v13 == v18):
                                break
                            arg3 = (load32(v10 + 12) - arg0)
                            v12 = load32(v4 + 28)
                            while True:  # $label184
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
            if not v23:
                arg0 = load32(v16 + 24)
                continue
            break
        store32(v24 + 12, (load32(v24 + 12) - (load32(v16 + 12) + v26)))
        arg0 = load32(v16 + 28)
        while True:  # $label186
            if ((v16 + 7) != v29):
                store32(v33, arg0)
                break
            v22 = ((1 if (v23 == -5) else v22) if arg0 else v22)
            break
        while True:  # $label187
            arg1 = (v16 + 8)
            if not (v16 + 8):
                break
            if not load32(arg1 + 32):
                break
            arg0 = load32(arg1 + 36)
            if not load32(arg1 + 36):
                break
            arg2 = load32(arg1 + 28)
            if not load32(arg1 + 28):
                break
            if (load32(arg2) != arg1):
                break
            if (u32((load32(arg2 + 4) - 16180)) > u32(31)):
                break
            arg3 = load32(arg2 + 56)
            if load32(arg2 + 56):
                arg2 = load32(arg1 + 28)
                arg0 = load32(arg1 + 36)
            store32(arg1 + 28, 0)
            break
        while True:  # $label189
            while True:  # $label188
                # br_table (v23 + 5)
                break
                break
            if (v22 != (0 - load32(v16 + 24))):
                break
            break
        break
    G.global0 = (v16 - -64)
    G.global0 = (v24 + 16)
    return call_table(arg0)

# ----------------------------------------------------------
# $func299
# ----------------------------------------------------------
def func299(arg0, arg1):
    v3 = load32(PLAYER_COUNT)
    if load32(PLAYER_COUNT):
        while True:  # $label9
            while True:  # $label0
                v2 = load32(arg0 + 48)
                v4 = (v5 << 2)
                if not load32((load32(arg0 + 48) + (v5 << 2))):
                    if not load32((v2 + (v3 << 2))):
                        break
                    if not load32((load32(9142420) + v4)):
                        break
                v2 = 0
                v7 = load32(PLAYERS)
                v8 = load32(arg0 + 32)
                if (u32(load32(arg0 + 32)) <= u32(3)):
                    while True:  # $label7
                        while True:  # $label5
                            while True:  # $label4
                                while True:  # $label2
                                    while True:  # $label3
                                        while True:  # $label1
                                            # br_table (v8 - 1)
                                            break
                                            break
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if load32(((v2 * 404) + ENTITY_TYPES) + 264):
                                            break
                                        if (load32(v3 + 268) == 1):
                                            break
                                        if not load32(v3 + 92):
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
                            v6 = load32((((v7 + (v5 * 286704)) + (v2 << 2)) + 284636))
                            if not load32((((v7 + (v5 * 286704)) + (v2 << 2)) + 284636)):
                                break
                            v3 = 0
                            v4 = load32(v6 + 8)
                            if not load32(v6 + 8):
                                break
                            while True:  # $label6
                                v9 = load32((load32(v6) + (v3 << 2)))
                                if load32((load32(v6) + (v3 << 2))):
                                    v4 = load32(v6 + 8)
                                v3 = (v3 + 1)
                                if (u32((v3 + 1)) < u32(v4)):
                                    continue
                                break
                            break
                        v2 = (v2 + 1)
                        if ((v2 + 1) != 255):
                            continue
                        break
                        break
                    raise Unreachable()
                v2 = load32((((v7 + (v5 * 286704)) + (v8 << 2)) + 284620))
                if not load32((((v7 + (v5 * 286704)) + (v8 << 2)) + 284620)):
                    break
                v3 = 0
                v4 = load32(v2 + 8)
                if not load32(v2 + 8):
                    break
                while True:  # $label8
                    v6 = load32((load32(v2) + (v3 << 2)))
                    if load32((load32(v2) + (v3 << 2))):
                        v4 = load32(v2 + 8)
                    v3 = (v3 + 1)
                    if (u32((v3 + 1)) < u32(v4)):
                        continue
                    break
                break
            v5 = (v5 + 1)
            v3 = load32(PLAYER_COUNT)
            if (u32((v5 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break

# ----------------------------------------------------------
# $func300
# ----------------------------------------------------------
def func300(arg0, arg1, arg2):
    while True:  # $label0
        v6 = load32(PLAYER_COUNT)
        if not load32(PLAYER_COUNT):
            break
        v11 = load32(arg1)
        v12 = (load32(arg1) + (v6 << 2))
        v13 = load16u(arg2 + 114)
        v14 = load16u(arg2 + 112)
        v15 = load32(arg2 + 28)
        v16 = load32(ENTITIES)
        v17 = load32(PLAYERS)
        v18 = load32(9142420)
        arg1 = 2147483647
        if (u32(arg0) <= u32(3)):
            v7 = load32(38764)
            v8 = load32(38456)
            v9 = (arg0 - 1)
            while True:  # $label10
                while True:  # $label1
                    arg0 = (v3 << 2)
                    if not load32((v11 + (v3 << 2))):
                        if not load32(v12):
                            break
                        if not load32((arg0 + v18)):
                            break
                    arg0 = 0
                    while True:  # $label9
                        while True:  # $label6
                            while True:  # $label5
                                while True:  # $label2
                                    while True:  # $label3
                                        while True:  # $label4
                                            # br_table v9
                                            break
                                            break
                                        if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) == 1):
                                            break
                                        break
                                        break
                                    if not load32(((arg0 * 404) + ENTITY_TYPES) + 264):
                                        break
                                    break
                                    break
                                arg2 = ((arg0 * 404) + ENTITY_TYPES)
                                if load32(((arg0 * 404) + ENTITY_TYPES) + 264):
                                    break
                                if (load32(arg2 + 268) == 1):
                                    break
                                if not load32(arg2 + 92):
                                    break
                                if (arg0 == v8):
                                    break
                                if (arg0 == v7):
                                    break
                                break
                            arg2 = load32((((v17 + (v3 * 286704)) + (arg0 << 2)) + 284636))
                            if not load32((((v17 + (v3 * 286704)) + (arg0 << 2)) + 284636)):
                                break
                            v10 = load32(arg2 + 8)
                            if not load32(arg2 + 8):
                                break
                            v19 = load32(arg2)
                            arg2 = 0
                            while True:  # $label8
                                while True:  # $label7
                                    v4 = load32((v19 + (arg2 << 2)))
                                    if not load32((v19 + (arg2 << 2))):
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
            while True:  # $label11
                arg2 = (arg0 << 2)
                if not load32((v11 + (arg0 << 2))):
                    if not load32(v12):
                        break
                    if not load32((arg2 + v18)):
                        break
                arg2 = load32((((v17 + (arg0 * 286704)) + v4) + 284636))
                if not load32((((v17 + (arg0 * 286704)) + v4) + 284636)):
                    break
                v7 = load32(arg2 + 8)
                if not load32(arg2 + 8):
                    break
                v8 = load32(arg2)
                arg2 = 0
                while True:  # $label13
                    while True:  # $label12
                        v3 = load32((v8 + (arg2 << 2)))
                        if not load32((v8 + (arg2 << 2))):
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
