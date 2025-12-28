"""
Tzar Engine - Core module (part 14).
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
# $func464
# ----------------------------------------------------------
def func464(arg0):
    v11 = load32(arg0)
    v16 = load32(arg0 + 12)
    v12 = load32(arg0 + 4)
    v8 = load32(arg0 + 8)
    v6 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # $label6
        while True:  # $label7
            if not load8u(9142916):
                if v11:
                    while True:  # $label0
                        v3 = load32((v16 + (v2 << 2)))
                        v5 = ((load32(load32((v16 + (v2 << 2)))) * (load32(v3 + 4) + 2)) << 2)
                        v4 = (((load32(load32((v16 + (v2 << 2)))) * (load32(v3 + 4) + 2)) << 2) + v4)
                        if load32(v3 + 56):
                            v3 = (v4 + v5)
                            v1 = (((v4 + v5) - v8) if (u32(v3) > u32((v1 + v8))) else v1)
                        v2 = (v2 + 1)
                        if ((v2 + 1) != v11):
                            continue
                        break
                v13 = (load32(9684256) & 511)
                store32(9684256, ((load32(9684256) & 511) + 1))
                v7 = func26((v1 + v8))
                store32(((v13 << 2) + 9682208), func26((v1 + v8)))
                if v11:
                    while True:  # $label5
                        v3 = load32((v16 + (v14 << 2)))
                        v15 = load32(load32((v16 + (v14 << 2))) + 4)
                        v4 = load32(v3)
                        v9 = (load32(load32((v16 + (v14 << 2))) + 4) * load32(v3))
                        v17 = load32(v3 + 36)
                        v5 = (v4 << 2)
                        v18 = load32(v3 + 40)
                        v1 = 1
                        while True:  # $label1
                            if ((u32(v15) < u32(16384)) & (u32(v4) <= u32(16383))):
                                break
                            while True:  # $label3
                                while True:  # $label2
                                    # TODO: i32.div_u
                                    v4 = v1
                                    if (v9 - (v1 * v1)):
                                        break
                                    if (u32(v4) >= u32(16384)):
                                        break
                                    v4 = v1
                                    break
                                    break
                                v4 = 16384
                                v2 = (v1 + 1)
                                if ((v1 + 1) == 16384):
                                    break
                                # TODO: i32.div_u
                                v19 = v2
                                if (v9 == (v2 * v2)):
                                    v4 = v2
                                    if (u32(v19) < u32(16384)):
                                        break
                                v1 = (v1 + 2)
                                continue
                                break
                            raise Unreachable()
                            break
                        if v5:
                            # TODO: memory.fill
                        v2 = (v5 + v10)
                        v9 = ((v15 + 2) * v5)
                        v1 = 0
                        if v5:
                            while True:  # $label4
                                store8((v7 + ((v1 + v2) + ((load32(v3) * load32(v3 + 4)) << 2))), 0)
                                store8((v7 + ((v2 + (v1 | 1)) + ((load32(v3) * load32(v3 + 4)) << 2))), 0)
                                v1 = (v1 + 2)
                                if ((v1 + 2) != v5):
                                    continue
                                break
                        v10 = (v9 + v10)
                        v14 = (v14 + 1)
                        if ((v14 + 1) != v11):
                            continue
                        break
                store32(v6 + 12, v13)
                store32(v6 + 8, v7)
                store32(v6 + 4, v12)
                store32(v6, v8)
                if v12:
                    break
                break
            while True:  # $label8
                v15 = load32(9684260)
                if load32(9684260):
                    break
                if not load8u(9142918):
                    break
                break
            if v11:
                while True:  # $label18
                    v3 = load32((v16 + (v14 << 2)))
                    v4 = load32(load32((v16 + (v14 << 2))) + 4)
                    v1 = load32(v3)
                    v7 = (load32(load32((v16 + (v14 << 2))) + 4) * load32(v3))
                    v10 = (v3 + load32(v3 + 36))
                    v2 = 1
                    while True:  # $label9
                        if ((u32(v4) < u32(16384)) & (u32(v1) <= u32(16383))):
                            break
                        while True:  # $label11
                            while True:  # $label10
                                # TODO: i32.div_u
                                v1 = v2
                                if (v7 - (v2 * v2)):
                                    break
                                if (u32(v1) >= u32(16384)):
                                    break
                                v1 = v2
                                break
                                break
                            v1 = 16384
                            v4 = (v2 + 1)
                            if ((v2 + 1) == 16384):
                                break
                            # TODO: i32.div_u
                            v5 = v4
                            if (v7 == (v4 * v4)):
                                v1 = v4
                                if (u32(v5) < u32(16384)):
                                    break
                            v2 = (v2 + 2)
                            continue
                            break
                        raise Unreachable()
                        break
                    v13 = (load32(9684256) & 511)
                    store32(9684256, ((load32(9684256) & 511) + 1))
                    v9 = (v7 << 2)
                    v5 = func26((v7 << 2))
                    store32(((v13 << 2) + 9682208), func26((v7 << 2)))
                    while True:  # $label16
                        while True:  # $label14
                            while True:  # $label13
                                while True:  # $label12
                                    v10 = load32(v3 + 32)
                                    # br_table (load32(v3 + 32) - 23)
                                    break
                                    break
                                v8 = 0
                                v4 = 0
                                v12 = 0
                                v1 = 0
                                v2 = 0
                                if not v7:
                                    break
                                while True:  # $label15
                                    if load8u((v5 + (v2 | 3))):
                                        v8 = (v8 + load8u((v2 + v5)))
                                        v12 = (v12 + load8u((v5 + (v2 | 2))))
                                        v4 = (v4 + load8u((v5 + (v2 | 1))))
                                        v1 = (v1 + 1)
                                    v2 = (v2 + 4)
                                    if (u32(v9) > u32((v2 + 4))):
                                        continue
                                    break
                                break
                                break
                            v8 = 0
                            if (v10 != 27):
                                break
                            if not load8u(9142916):
                                break
                            v2 = 0
                            if not v7:
                                break
                            while True:  # $label17
                                # TODO: i32.div_u
                                store8((load8u((v5 + (v2 | 2))) + (load8u((v5 + (v2 | 1))) + load8u((v2 + v5)))), 3)
                                v2 = (v2 + 4)
                                if (u32((v2 + 4)) < u32(v9)):
                                    continue
                                break
                            v10 = load32(v3 + 32)
                            break
                            break
                        # TODO: i32.div_u
                        # TODO: i32.div_u
                        # TODO: i32.div_u
                        v8 = (v12 + (v1 << 16))
                        break
                    v1 = load32((v3 + (48 if load8u(9142918) else 56)))
                    v4 = load32(v3 + 16)
                    v20 = load64(v3)
                    v2 = load32(v3 + 28)
                    v21 = load64(v3 + 8)
                    store64(v6 + 32, load64(v3 + 20))
                    store64(v6 + 40, v21)
                    store32(v6 + 48, v10)
                    store32(v6 + 52, v8)
                    store32(v6 + 56, v1)
                    store32(v6 + 60, v2)
                    store32((v6 - -64), v13)
                    store32(v6 + 16, v5)
                    store64(v6 + 20, v20)
                    store32(v6 + 28, v4)
                    a_b()
                    store32(9684260, (load32(9684260) + v9))
                    v14 = (v14 + 1)
                    if ((v14 + 1) != v11):
                        continue
                    break
            if v15:
                break
            break
        a_b()
        break
    G.global0 = (v6 + 80)
    v1 = load32(arg0 + 12)
    if load32(arg0 + 12):
    hf(af(v1), af(arg0), 0)
    a_l()
    raise Unreachable()
    return 0

# ----------------------------------------------------------
# $func465
# ----------------------------------------------------------
def func465(arg0, arg1, param2):
    v29 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v22 = load32(arg0 + 2324)
    v37 = load32(arg0 + 172)
    v5 = load8u((load32(arg0 + 2352) + 10321))
    v10 = load32(arg0 + 2312)
    v26 = load32(arg0 + 2328)
    v12 = load32(arg0 + 2320)
    v13 = load32(arg0 + 2316)
    v16 = load32(arg0 + 320)
    v33 = load32(arg0 + 176)
    if (load32(arg0 + 160) == 2):
        func273(0, 0, 0, 0, arg0, (arg0 + 172))
    while True:  # $label98
        while True:  # $label95
            while True:  # $label96
                while True:  # $label2
                    while True:  # $label0
                        if not load32(arg0 + 180):
                            break
                        v15 = load32(arg0 + 308)
                        if (load32(arg0 + 308) >= load32(arg0 + 316)):
                            break
                        v27 = load32(arg0 + 176)
                        while True:  # $label3
                            while True:  # $label1
                                v8 = (load32(arg0 + 184) + (v15 << 2))
                                v4 = load8u((load32(arg0 + 184) + (v15 << 2)))
                                if not load8u((load32(arg0 + 184) + (v15 << 2))):
                                    break
                                if (u32(v4) <= u32(2)):
                                    break
                                v6 = load32(arg0 + 172)
                                v2 = load32(arg0 + 2324)
                                v3 = ((load32(arg0 + 2312) + ((load32(arg0 + 172) * load32(arg0 + 2324)) << 4)) + (v15 << 4))
                                if (load32(arg0 + 2352) == 1):
                                    if (v15 > 0):
                                    if load8u(v8 + 2):
                                    if (v27 > 0):
                                    if not load8u(v8 + 2):
                                        break
                                    break
                                v7 = load8u(v8 + 1)
                                v11 = (v15 << 3)
                                v14 = load32(arg0 + 2328)
                                v6 = ((v6 * load32(arg0 + 2328)) << 3)
                                v9 = ((v15 << 3) + (((v6 * load32(arg0 + 2328)) << 3) + load32(arg0 + 2320)))
                                v11 = ((load32(arg0 + 2316) + v6) + v11)
                                v6 = load8u(v8 + 3)
                                if (v15 > 0):
                                    v17 = (v4 + 4)
                                if load8u(v8 + 2):
                                if (v27 > 0):
                                    v17 = (v4 + 4)
                                if not load8u(v8 + 2):
                                    break
                                break
                            v15 = (v15 + 1)
                            if ((v15 + 1) < load32(arg0 + 316)):
                                continue
                            break
                        break
                    v8 = ((v22 * v37) << 4)
                    v38 = (v5 * v22)
                    v11 = (v10 - (v5 * v22))
                    v3 = ((v26 * v37) << 3)
                    v34 = (((v5 & 0xFFFFFFFF) >> 1) * v26)
                    v26 = (v12 - (((v5 & 0xFFFFFFFF) >> 1) * v26))
                    v27 = (v13 - v34)
                    while True:  # $label4
                        if not load32(arg0 + 584):
                            break
                        v7 = load32(arg0 + 308)
                        v2 = load32(arg0 + 316)
                        if (load32(arg0 + 308) >= load32(arg0 + 316)):
                            break
                        v6 = (arg0 + 596)
                        while True:  # $label7
                            v22 = (load32(arg0 + 188) + (v7 * 800))
                            v10 = load8u((load32(arg0 + 188) + (v7 * 800)) + 796)
                            if (u32(load8u((load32(arg0 + 188) + (v7 * 800)) + 796)) >= u32(4)):
                                v14 = load32(arg0 + 2328)
                                v9 = ((load32(arg0 + 2328) * load32(arg0 + 172)) << 3)
                                v12 = load32(arg0 + 2320)
                                v13 = load32(arg0 + 2316)
                                v4 = load32(arg0 + 592)
                                v15 = load32(arg0 + 588)
                                v2 = 0
                                while True:  # $label5
                                    v15 = (v6 + (v15 << 2))
                                    v17 = (load32(v15) - load32((v6 + (v4 << 2))))
                                    store32((v6 + (v15 << 2)), ((load32(v15) - load32((v6 + (v4 << 2)))) & 2147483647))
                                    v4 = (load32(arg0 + 588) + 1)
                                    v15 = ((load32(arg0 + 588) + 1) if (v4 != 55) else 0)
                                    store32(arg0 + 588, ((load32(arg0 + 588) + 1) if (v4 != 55) else 0))
                                    v4 = (load32(arg0 + 592) + 1)
                                    v4 = ((load32(arg0 + 592) + 1) if (v4 != 55) else 0)
                                    store32(arg0 + 592, ((load32(arg0 + 592) + 1) if (v4 != 55) else 0))
                                    store8((v2 + v29), ((((((v17 << 1) >> 24) * v10) & 0xFFFFFFFF) >> 8) ^ 128))
                                    v2 = (v2 + 1)
                                    if ((v2 + 1) != 64):
                                        continue
                                    break
                                v2 = 0
                                v10 = (v7 << 3)
                                v22 = load8u(v22 + 796)
                                v4 = load32(arg0 + 592)
                                v15 = load32(arg0 + 588)
                                while True:  # $label6
                                    v15 = (v6 + (v15 << 2))
                                    v13 = (load32(v15) - load32((v6 + (v4 << 2))))
                                    store32((v6 + (v15 << 2)), ((load32(v15) - load32((v6 + (v4 << 2)))) & 2147483647))
                                    v4 = (load32(arg0 + 588) + 1)
                                    v15 = ((load32(arg0 + 588) + 1) if (v4 != 55) else 0)
                                    store32(arg0 + 588, ((load32(arg0 + 588) + 1) if (v4 != 55) else 0))
                                    v4 = (load32(arg0 + 592) + 1)
                                    v4 = ((load32(arg0 + 592) + 1) if (v4 != 55) else 0)
                                    store32(arg0 + 592, ((load32(arg0 + 592) + 1) if (v4 != 55) else 0))
                                    store8((v2 + v29), ((((((v13 << 1) >> 24) * v22) & 0xFFFFFFFF) >> 8) ^ 128))
                                    v2 = (v2 + 1)
                                    if ((v2 + 1) != 64):
                                        continue
                                    break
                                v2 = load32(arg0 + 316)
                            v7 = (v7 + 1)
                            if ((v7 + 1) < v2):
                                continue
                            break
                        break
                    v22 = (v8 + v11)
                    v26 = (v3 + v26)
                    v27 = (v3 + v27)
                    v39 = (v16 - 1)
                    while True:  # $label8
                        if not load32(arg1 + 44):
                            break
                        v7 = (v33 << 4)
                        v6 = ((v33 << 4) + 16)
                        while True:  # $label9
                            if v33:
                                v4 = v22
                                v3 = v27
                                v2 = v26
                                break
                            v2 = (load32(arg0 + 2320) + v3)
                            v3 = (load32(arg0 + 2316) + v3)
                            v4 = (load32(arg0 + 2312) + v8)
                            break
                        v15 = 0
                        store32(arg1 + 28, v2)
                        store32(arg1 + 24, v3)
                        store32(arg1 + 20, v4)
                        v4 = 0
                        store32(arg1 + 104, 0)
                        v2 = (v6 - (v5 if (v33 < v39) else 0))
                        v3 = load32(arg1 + 88)
                        v35 = ((v6 - (v5 if (v33 < v39) else 0)) if (v2 < v3) else load32(arg1 + 88))
                        while True:  # $label10
                            if not load32(arg0 + 2392):
                                break
                            if (v15 >= v35):
                                break
                            while True:  # $label13
                                v4 = (v35 - v15)
                                v2 = 0
                                v17 = 0
                                while True:  # $label16
                                    while True:  # $label41
                                        while True:  # $label37
                                            while True:  # $label36
                                                while True:  # $label35
                                                    while True:  # $label18
                                                        while True:  # $label17
                                                            while True:  # $label14
                                                                if arg0:
                                                                    while True:  # $label11
                                                                        if (v15 < 0):
                                                                            break
                                                                        if (v4 <= 0):
                                                                            break
                                                                        v14 = (v4 + v15)
                                                                        v6 = load32(arg1 + 88)
                                                                        if ((v4 + v15) > load32(arg1 + 88)):
                                                                            break
                                                                        v30 = load32(arg1)
                                                                        while True:  # $label12
                                                                            if load32(arg0 + 2400):
                                                                                break
                                                                            v3 = load32(arg0 + 2388)
                                                                            if not load32(arg0 + 2388):
                                                                                v2 = func134(1, 144)
                                                                                store32(arg0 + 2388, func134(1, 144))
                                                                                if not v2:
                                                                                    break
                                                                                if load32(arg0 + 2404):
                                                                                    break
                                                                                v3 = func58((load32(arg1 + 88) * load32(arg1)), 1)
                                                                                store32(arg0 + 2404, func58((load32(arg1 + 88) * load32(arg1)), 1))
                                                                                while True:  # $label15
                                                                                    if v3:
                                                                                        store32(arg0 + 2412, 0)
                                                                                        store32(arg0 + 2408, v3)
                                                                                        break
                                                                                    if not func99(arg0, 1, 8400):
                                                                                        break
                                                                                    v3 = load32(arg0 + 2408)
                                                                                    break
                                                                                v7 = load32(arg0 + 2392)
                                                                                if not load32(arg0 + 2392):
                                                                                    break
                                                                                if not v3:
                                                                                    break
                                                                                v2 = load32(arg0 + 2388)
                                                                                v8 = load32(arg0 + 2396)
                                                                                v5 = load32(52304)
                                                                                if (load32(52304) != load32(52312)):
                                                                                    store32(9687564, 337)
                                                                                    store32(9687560, 338)
                                                                                    store32(9687556, 339)
                                                                                    store32(9687552, 340)
                                                                                    store32(9687548, 341)
                                                                                    store32(9687544, 342)
                                                                                    store32(9687540, 343)
                                                                                    store32(52312, v5)
                                                                                    store32(9687536, 0)
                                                                                store32(v2 + 136, v3)
                                                                                v3 = load32(arg1)
                                                                                store32(v2, load32(arg1))
                                                                                v5 = load32(arg1 + 4)
                                                                                store32(v2 + 4, load32(arg1 + 4))
                                                                                if (v3 <= 0):
                                                                                    break
                                                                                if (v5 <= 0):
                                                                                    break
                                                                                while True:  # $label33
                                                                                    while True:  # $label19
                                                                                        if (u32(v8) < u32(2)):
                                                                                            break
                                                                                        v3 = (load8u(v7) & 3)
                                                                                        store32(v2 + 8, (load8u(v7) & 3))
                                                                                        store32(v2 + 12, (((load8u(v7) & 0xFFFFFFFF) >> 2) & 3))
                                                                                        v5 = (((load8u(v7) & 0xFFFFFFFF) >> 4) & 3)
                                                                                        store32(v2 + 16, (((load8u(v7) & 0xFFFFFFFF) >> 4) & 3))
                                                                                        if (u32(v3) > u32(1)):
                                                                                            break
                                                                                        if (u32(v5) > u32(1)):
                                                                                            break
                                                                                        if (u32(load8u(v7)) > u32(63)):
                                                                                            break
                                                                                        v3 = (v2 + 24)
                                                                                        if (v2 + 24):
                                                                                            # TODO: memory.fill
                                                                                        v8 = (v8 - 1)
                                                                                        store32(v3 + 52, 262)
                                                                                        store32(v3 + 48, 263)
                                                                                        store32(v3 + 44, 264)
                                                                                        store32(v3 + 40, 0)
                                                                                        store32((v2 - -64), v2)
                                                                                        store32(v2 + 24, load32(arg1))
                                                                                        store32(v2 + 28, load32(arg1 + 4))
                                                                                        store32(v2 + 96, load32(arg1 + 72))
                                                                                        store32(v2 + 100, load32(arg1 + 76))
                                                                                        store32(v2 + 104, load32(arg1 + 80))
                                                                                        store32(v2 + 108, load32(arg1 + 84))
                                                                                        store32(v2 + 112, load32(arg1 + 88))
                                                                                        while True:  # $label23
                                                                                            while True:  # $label21
                                                                                                while True:  # $label22
                                                                                                    while True:  # $label20
                                                                                                        # br_table load32(v2 + 8)
                                                                                                        break
                                                                                                        break
                                                                                                    break
                                                                                                    break
                                                                                                a_c()
                                                                                                raise Unreachable()
                                                                                                break
                                                                                            while True:  # $label24
                                                                                                v3 = func134(1, 288)
                                                                                                if not func134(1, 288):
                                                                                                    break
                                                                                                v5 = (v7 + 1)
                                                                                                store64(v3, 8589934592)
                                                                                                func453()
                                                                                                while True:  # $label29
                                                                                                    if v2:
                                                                                                        v14 = load32(v2)
                                                                                                        store32(v3 + 100, load32(v2))
                                                                                                        v7 = load32(v2 + 4)
                                                                                                        store32(v3 + 8, (v2 + 24))
                                                                                                        store32(v3 + 104, v7)
                                                                                                        store32(v2 + 28, v7)
                                                                                                        store32(v2 + 24, v14)
                                                                                                        store32((v2 - -64), v2)
                                                                                                        store32(v3, 0)
                                                                                                        while True:  # $label25
                                                                                                            if not func153(load32(v2), load32(v2 + 4), 1, v3, 0):
                                                                                                                break
                                                                                                            while True:  # $label31
                                                                                                                while True:  # $label32
                                                                                                                    while True:  # $label30
                                                                                                                        while True:  # $label27
                                                                                                                            while True:  # $label26
                                                                                                                                if (load32(v3 + 192) != 1):
                                                                                                                                    break
                                                                                                                                if (load32(v3 + 196) != 3):
                                                                                                                                    break
                                                                                                                                if (load32(v3 + 120) > 0):
                                                                                                                                    break
                                                                                                                                v5 = load32(v3 + 164)
                                                                                                                                if (load32(v3 + 164) <= 0):
                                                                                                                                    break
                                                                                                                                v14 = load32(v3 + 168)
                                                                                                                                v7 = 0
                                                                                                                                while True:  # $label28
                                                                                                                                    v8 = (v14 + (v7 * 548))
                                                                                                                                    if load8u(load32((v14 + (v7 * 548)) + 4)):
                                                                                                                                        break
                                                                                                                                    if load8u(load32(v8 + 8)):
                                                                                                                                        break
                                                                                                                                    if load8u(load32(v8 + 12)):
                                                                                                                                        break
                                                                                                                                    v7 = (v7 + 1)
                                                                                                                                    if (v5 != (v7 + 1)):
                                                                                                                                        continue
                                                                                                                                    break
                                                                                                                                break
                                                                                                                                break
                                                                                                                            store32(v2 + 132, 0)
                                                                                                                            v8 = load32(v3 + 100)
                                                                                                                            v7 = load32(v2)
                                                                                                                            if (load32(v3 + 100) > load32(v2)):
                                                                                                                                break
                                                                                                                            v51 = (load32(v3 + 104) * i32(v8))
                                                                                                                            v8 = (v7 & 65535)
                                                                                                                            v7 = func58(((load32(v3 + 104) * i32(v8)) + (i32((v7 & 65535)) + (i32(v7) << 4))), 4)
                                                                                                                            store32(v3 + 16, func58(((load32(v3 + 104) * i32(v8)) + (i32((v7 & 65535)) + (i32(v7) << 4))), 4))
                                                                                                                            if v7:
                                                                                                                                break
                                                                                                                            store32(v3 + 20, 0)
                                                                                                                            # br_table load32(v3)
                                                                                                                            break
                                                                                                                            break
                                                                                                                        store32(v2 + 132, 1)
                                                                                                                        store32(v3 + 20, 0)
                                                                                                                        v7 = func58((load32(v3 + 104) * load32(v3 + 100)), 1)
                                                                                                                        store32(v3 + 16, func58((load32(v3 + 104) * load32(v3 + 100)), 1))
                                                                                                                        if v7:
                                                                                                                            break
                                                                                                                        # br_table load32(v3)
                                                                                                                        break
                                                                                                                        break
                                                                                                                    store32(v3 + 20, ((v7 + (i32(v51) << 2)) + (v8 << 2)))
                                                                                                                    break
                                                                                                                store32(v2 + 20, v3)
                                                                                                                break
                                                                                                                break
                                                                                                            store32(v3, 1)
                                                                                                            break
                                                                                                        func191(v3)
                                                                                                        break
                                                                                                    a_c()
                                                                                                    raise Unreachable()
                                                                                                    break
                                                                                                a_c()
                                                                                                raise Unreachable()
                                                                                                break
                                                                                            break
                                                                                        if 5601:
                                                                                            break
                                                                                        break
                                                                                    v4 = load32(load32(arg0 + 2388) + 20)
                                                                                    if load32(load32(arg0 + 2388) + 20):
                                                                                    else:
                                                                                    break
                                                                                    break
                                                                                while True:  # $label34
                                                                                    v3 = load32(arg0 + 2388)
                                                                                    if (load32(load32(arg0 + 2388) + 16) != 1):
                                                                                        store32(arg0 + 2416, 0)
                                                                                        break
                                                                                    v4 = (v6 - v15)
                                                                                    break
                                                                                v14 = (v4 + v15)
                                                                            if (v6 < v14):
                                                                                break
                                                                            v31 = load32(v3 + 112)
                                                                            while True:  # $label40
                                                                                if not load32(v3 + 8):
                                                                                    v2 = load32(arg0 + 2392)
                                                                                    v6 = load32(v3)
                                                                                    v7 = (load32(v3) * v15)
                                                                                    v8 = ((load32(arg0 + 2392) + (load32(v3) * v15)) + 1)
                                                                                    if (u32(((load32(arg0 + 2392) + (load32(v3) * v15)) + 1)) > u32((v2 + load32(arg0 + 2396)))):
                                                                                        break
                                                                                    if not load32(((load32(v3 + 12) << 2) + 9687552)):
                                                                                        break
                                                                                    v2 = load32(arg0 + 2412)
                                                                                    while True:  # $label38
                                                                                        if (v4 <= 0):
                                                                                            break
                                                                                        v5 = (v4 & 1)
                                                                                        v7 = (load32(arg0 + 2408) + v7)
                                                                                        if (v4 != 1):
                                                                                            v9 = (v4 & -2)
                                                                                            v4 = 0
                                                                                            while True:  # $label39
                                                                                                v8 = (v6 + v8)
                                                                                                v2 = (v6 + v7)
                                                                                                v8 = (v6 + v8)
                                                                                                v7 = (v2 + v6)
                                                                                                v4 = (v4 + 2)
                                                                                                if ((v4 + 2) != v9):
                                                                                                    continue
                                                                                                break
                                                                                        if not v5:
                                                                                            break
                                                                                        v2 = v7
                                                                                        break
                                                                                    store32(arg0 + 2412, v2)
                                                                                    break
                                                                                if not load32(v3 + 20):
                                                                                    break
                                                                                while True:  # $label77
                                                                                    while True:  # $label72
                                                                                        while True:  # $label49
                                                                                            while True:  # $label42
                                                                                                while True:  # $label43
                                                                                                    v9 = load32(v3 + 20)
                                                                                                    if load32(v3 + 20):
                                                                                                        v10 = load32(v9 + 104)
                                                                                                        if (v14 <= load32(v9 + 104)):
                                                                                                            v12 = 1
                                                                                                            if (load32(v9 + 108) >= v14):
                                                                                                                break
                                                                                                            if not load32(v3 + 132):
                                                                                                                func188()
                                                                                                                if not load32(v3 + 132):
                                                                                                                    break
                                                                                                                v10 = load32(v9 + 104)
                                                                                                            v13 = load32(v9 + 112)
                                                                                                            v16 = load32(v9 + 100)
                                                                                                            v4 = (v13 // load32(v9 + 100))
                                                                                                            v12 = (load32(v9 + 112) - ((v13 // load32(v9 + 100)) * v16))
                                                                                                            v23 = load32(v9 + 148)
                                                                                                            v24 = load32(v9 + 16)
                                                                                                            while True:  # $label44
                                                                                                                v25 = (v14 * v16)
                                                                                                                v3 = (v13 >= (v14 * v16))
                                                                                                                if not (v13 >= (v14 * v16)):
                                                                                                                    v2 = load32(v9 + 152)
                                                                                                                    if load32(v9 + 152):
                                                                                                                    else:
                                                                                                                    v2 = 0
                                                                                                                    if (0 >= load32(v9 + 164)):
                                                                                                                        break
                                                                                                                    v17 = (load32(v9 + 168) + (v2 * 548))
                                                                                                                v20 = (v10 * v16)
                                                                                                                if ((v10 * v16) >= v13):
                                                                                                                    if (v10 >= v14):
                                                                                                                        while True:  # $label46
                                                                                                                            while True:  # $label45
                                                                                                                                if (load32(v9 + 120) > 0):
                                                                                                                                    break
                                                                                                                                v7 = load32(v9 + 164)
                                                                                                                                if (load32(v9 + 164) <= 0):
                                                                                                                                    break
                                                                                                                                v6 = load32(v9 + 168)
                                                                                                                                v5 = 0
                                                                                                                                while True:  # $label47
                                                                                                                                    v2 = (v6 + (v5 * 548))
                                                                                                                                    if load8u(load32((v6 + (v5 * 548)) + 4)):
                                                                                                                                        break
                                                                                                                                    if load8u(load32(v2 + 8)):
                                                                                                                                        break
                                                                                                                                    if load8u(load32(v2 + 12)):
                                                                                                                                        break
                                                                                                                                    v5 = (v5 + 1)
                                                                                                                                    if (v7 != (v5 + 1)):
                                                                                                                                        continue
                                                                                                                                    break
                                                                                                                                break
                                                                                                                                break
                                                                                                                            a_c()
                                                                                                                            raise Unreachable()
                                                                                                                            break
                                                                                                                        while True:  # $label51
                                                                                                                            while True:  # $label48
                                                                                                                                if v3:
                                                                                                                                    break
                                                                                                                                if load32(v9 + 48):
                                                                                                                                    break
                                                                                                                                v18 = (v9 + 24)
                                                                                                                                while True:  # $label73
                                                                                                                                    while True:  # $label50
                                                                                                                                        while True:  # $label62
                                                                                                                                            while True:  # $label65
                                                                                                                                                if not (v12 & v23):
                                                                                                                                                    v2 = load32(v9 + 152)
                                                                                                                                                    if load32(v9 + 152):
                                                                                                                                                    else:
                                                                                                                                                    v2 = 0
                                                                                                                                                    if (0 >= load32(v9 + 164)):
                                                                                                                                                        break
                                                                                                                                                    v17 = (load32(v9 + 168) + (v2 * 548))
                                                                                                                                                while True:  # $label58
                                                                                                                                                    while True:  # $label59
                                                                                                                                                        while True:  # $label60
                                                                                                                                                            while True:  # $label61
                                                                                                                                                                if v17:
                                                                                                                                                                    v5 = load32(v9 + 44)
                                                                                                                                                                    if (load32(v9 + 44) >= 32):
                                                                                                                                                                        func135(v18)
                                                                                                                                                                        v5 = load32(v9 + 44)
                                                                                                                                                                    v51 = load64(v9 + 24)
                                                                                                                                                                    v10 = (load32(v17) + ((i32(((load64(v9 + 24) & 0xFFFFFFFF) >> i32((v5 & 63)))) & 255) << 2))
                                                                                                                                                                    v2 = load8u((load32(v17) + ((i32(((load64(v9 + 24) & 0xFFFFFFFF) >> i32((v5 & 63)))) & 255) << 2)))
                                                                                                                                                                    if (u32(load8u((load32(v17) + ((i32(((load64(v9 + 24) & 0xFFFFFFFF) >> i32((v5 & 63)))) & 255) << 2)))) >= u32(9)):
                                                                                                                                                                        v5 = (v5 + 8)
                                                                                                                                                                        v10 = ((v10 + (load16u(v10 + 2) << 2)) + ((i32(((v51 & 0xFFFFFFFF) >> i32(((v5 + 8) & 63)))) & ((-1 << (v2 - 8)) ^ -1)) << 2))
                                                                                                                                                                    else:
                                                                                                                                                                    v3 = ((v2 & 255) + v5)
                                                                                                                                                                    store32(load8u(((v10 + (load16u(v10 + 2) << 2)) + ((i32(((v51 & 0xFFFFFFFF) >> i32(((v5 + 8) & 63)))) & ((-1 << (v2 - 8)) ^ -1)) << 2))) + 44, ((v2 & 255) + v5))
                                                                                                                                                                    v2 = load16u(v10 + 2)
                                                                                                                                                                    if (u32(load16u(v10 + 2)) <= u32(255)):
                                                                                                                                                                        store8((v13 + v24), v2)
                                                                                                                                                                        v13 = (v13 + 1)
                                                                                                                                                                        v12 = (v12 + 1)
                                                                                                                                                                        if ((v12 + 1) < v16):
                                                                                                                                                                            break
                                                                                                                                                                        v2 = (v4 + 1)
                                                                                                                                                                        v12 = 0
                                                                                                                                                                        if (v4 >= v14):
                                                                                                                                                                            v4 = v2
                                                                                                                                                                            break
                                                                                                                                                                        if (v2 & 15):
                                                                                                                                                                            v4 = v2
                                                                                                                                                                            break
                                                                                                                                                                        v4 = v2
                                                                                                                                                                        break
                                                                                                                                                                    v11 = 1
                                                                                                                                                                    if (u32(v2) > u32(279)):
                                                                                                                                                                        break
                                                                                                                                                                    v7 = (v2 - 256)
                                                                                                                                                                    if (u32((v2 - 256)) >= u32(4)):
                                                                                                                                                                        v3 = (((v2 - 258) & 0xFFFFFFFF) >> 1)
                                                                                                                                                                        v7 = (func39(v18, (((v2 - 258) & 0xFFFFFFFF) >> 1)) + (((v2 & 1) | 2) << v3))
                                                                                                                                                                        v51 = load64(v9 + 24)
                                                                                                                                                                        v3 = load32(v9 + 44)
                                                                                                                                                                    v5 = (load32(v17 + 16) + ((i32(((v51 & 0xFFFFFFFF) >> i32((v3 & 63)))) & 255) << 2))
                                                                                                                                                                    v2 = load8u((load32(v17 + 16) + ((i32(((v51 & 0xFFFFFFFF) >> i32((v3 & 63)))) & 255) << 2)))
                                                                                                                                                                    if (u32(load8u((load32(v17 + 16) + ((i32(((v51 & 0xFFFFFFFF) >> i32((v3 & 63)))) & 255) << 2)))) >= u32(9)):
                                                                                                                                                                        v3 = (v3 + 8)
                                                                                                                                                                        v5 = ((v5 + (load16u(v5 + 2) << 2)) + ((i32(((v51 & 0xFFFFFFFF) >> i32(((v3 + 8) & 63)))) & ((-1 << (v2 - 8)) ^ -1)) << 2))
                                                                                                                                                                    else:
                                                                                                                                                                    v2 = ((v2 & 255) + v3)
                                                                                                                                                                    store32(load8u(((v5 + (load16u(v5 + 2) << 2)) + ((i32(((v51 & 0xFFFFFFFF) >> i32(((v3 + 8) & 63)))) & ((-1 << (v2 - 8)) ^ -1)) << 2))) + 44, ((v2 & 255) + v3))
                                                                                                                                                                    v5 = load16u(v5 + 2)
                                                                                                                                                                    if (v2 >= 32):
                                                                                                                                                                        func135(v18)
                                                                                                                                                                    while True:  # $label52
                                                                                                                                                                        if (u32(v5) >= u32(4)):
                                                                                                                                                                            v2 = (((v5 - 2) & 0xFFFFFFFF) >> 1)
                                                                                                                                                                            v5 = (func39(v18, (((v5 - 2) & 0xFFFFFFFF) >> 1)) + (((v5 & 1) | 2) << v2))
                                                                                                                                                                        if ((v5 + 1) >= 121):
                                                                                                                                                                            break
                                                                                                                                                                        v2 = load8u((v5 + 13840))
                                                                                                                                                                        v2 = (((((load8u((v5 + 13840)) & 0xFFFFFFFF) >> 4) * v16) - (v2 & 15)) + 8)
                                                                                                                                                                        break
                                                                                                                                                                    v2 = (1 if (v2 <= 1) else (((((load8u((v5 + 13840)) & 0xFFFFFFFF) >> 4) * v16) - (v2 & 15)) + 8))
                                                                                                                                                                    if (v13 < (1 if (v2 <= 1) else (((((load8u((v5 + 13840)) & 0xFFFFFFFF) >> 4) * v16) - (v2 & 15)) + 8))):
                                                                                                                                                                        break
                                                                                                                                                                    v6 = (v7 + 1)
                                                                                                                                                                    if ((v7 + 1) > (v20 - v13)):
                                                                                                                                                                        break
                                                                                                                                                                    v5 = (v13 + v24)
                                                                                                                                                                    v11 = ((v13 + v24) - v2)
                                                                                                                                                                    while True:  # $label53
                                                                                                                                                                        if (v6 < 8):
                                                                                                                                                                            break
                                                                                                                                                                        while True:  # $label57
                                                                                                                                                                            while True:  # $label56
                                                                                                                                                                                while True:  # $label55
                                                                                                                                                                                    while True:  # $label54
                                                                                                                                                                                        # br_table (v2 - 1)
                                                                                                                                                                                        break
                                                                                                                                                                                        break
                                                                                                                                                                                    break
                                                                                                                                                                                    break
                                                                                                                                                                                break
                                                                                                                                                                                break
                                                                                                                                                                            break
                                                                                                                                                                        v10 = load32(v11)
                                                                                                                                                                        if not (v5 & 3):
                                                                                                                                                                            v2 = v6
                                                                                                                                                                            break
                                                                                                                                                                        store8(v5, load8u(v11))
                                                                                                                                                                        v10 = rotl(v10, 24)
                                                                                                                                                                        v11 = (v11 + 1)
                                                                                                                                                                        v5 = (v5 + 1)
                                                                                                                                                                        if not ((v5 + 1) & 3):
                                                                                                                                                                            v3 = v6
                                                                                                                                                                            v2 = v7
                                                                                                                                                                            break
                                                                                                                                                                        store8(v5, load8u(v11))
                                                                                                                                                                        v2 = (v7 - 1)
                                                                                                                                                                        v10 = rotl(v10, 24)
                                                                                                                                                                        v11 = (v11 + 1)
                                                                                                                                                                        v5 = (v5 + 1)
                                                                                                                                                                        if not ((v5 + 1) & 3):
                                                                                                                                                                            v3 = v7
                                                                                                                                                                            break
                                                                                                                                                                        store8(v5, load8u(v11))
                                                                                                                                                                        v8 = (v7 - 2)
                                                                                                                                                                        v10 = rotl(v10, 24)
                                                                                                                                                                        v11 = (v11 + 1)
                                                                                                                                                                        v5 = (v5 + 1)
                                                                                                                                                                        if ((v5 + 1) & 3):
                                                                                                                                                                            break
                                                                                                                                                                        v3 = v2
                                                                                                                                                                        v2 = v8
                                                                                                                                                                        break
                                                                                                                                                                        break
                                                                                                                                                                    if (v2 >= v6):
                                                                                                                                                                        break
                                                                                                                                                                    if (u32(v7) > u32(2147483646)):
                                                                                                                                                                        break
                                                                                                                                                                    v3 = 0
                                                                                                                                                                    v10 = 0
                                                                                                                                                                    if (u32(v7) >= u32(3)):
                                                                                                                                                                        v2 = (v6 & -4)
                                                                                                                                                                        v7 = 0
                                                                                                                                                                        while True:  # $label63
                                                                                                                                                                            store8((v5 + v10), load8u((v10 + v11)))
                                                                                                                                                                            v8 = (v10 | 1)
                                                                                                                                                                            store8((v5 + (v10 | 1)), load8u((v8 + v11)))
                                                                                                                                                                            v8 = (v10 | 2)
                                                                                                                                                                            store8((v5 + (v10 | 2)), load8u((v8 + v11)))
                                                                                                                                                                            v8 = (v10 | 3)
                                                                                                                                                                            store8((v5 + (v10 | 3)), load8u((v8 + v11)))
                                                                                                                                                                            v10 = (v10 + 4)
                                                                                                                                                                            v7 = (v7 + 4)
                                                                                                                                                                            if ((v7 + 4) != v2):
                                                                                                                                                                                continue
                                                                                                                                                                            break
                                                                                                                                                                    v2 = (v6 & 3)
                                                                                                                                                                    if not (v6 & 3):
                                                                                                                                                                        break
                                                                                                                                                                    while True:  # $label64
                                                                                                                                                                        store8((v5 + v10), load8u((v10 + v11)))
                                                                                                                                                                        v10 = (v10 + 1)
                                                                                                                                                                        v3 = (v3 + 1)
                                                                                                                                                                        if ((v3 + 1) != v2):
                                                                                                                                                                            continue
                                                                                                                                                                        break
                                                                                                                                                                    break
                                                                                                                                                                a_c()
                                                                                                                                                                raise Unreachable()
                                                                                                                                                                break
                                                                                                                                                            # TODO: memory.copy
                                                                                                                                                            break
                                                                                                                                                            break
                                                                                                                                                        store8(v5, load8u(v11))
                                                                                                                                                        v2 = (v7 - 3)
                                                                                                                                                        v10 = rotl(v10, 24)
                                                                                                                                                        v5 = (v5 + 1)
                                                                                                                                                        v11 = (v11 + 1)
                                                                                                                                                        v3 = v8
                                                                                                                                                        break
                                                                                                                                                    if (v3 < 5):
                                                                                                                                                        break
                                                                                                                                                    break
                                                                                                                                                v8 = ((v2 & 0xFFFFFFFF) >> 2)
                                                                                                                                                v21 = (((v2 & 0xFFFFFFFF) >> 2) & 7)
                                                                                                                                                v3 = 0
                                                                                                                                                v7 = 0
                                                                                                                                                if (u32((v8 - 1)) >= u32(7)):
                                                                                                                                                    v36 = (v8 & 1073741816)
                                                                                                                                                    v28 = 0
                                                                                                                                                    while True:  # $label66
                                                                                                                                                        v8 = (v7 << 2)
                                                                                                                                                        store32((v5 + (v7 << 2)), v10)
                                                                                                                                                        store32((v5 + (v8 | 4)), v10)
                                                                                                                                                        store32((v5 + (v8 | 8)), v10)
                                                                                                                                                        store32((v5 + (v8 | 12)), v10)
                                                                                                                                                        store32((v5 + (v8 | 16)), v10)
                                                                                                                                                        store32((v5 + (v8 | 20)), v10)
                                                                                                                                                        store32((v5 + (v8 | 24)), v10)
                                                                                                                                                        store32((v5 + (v8 | 28)), v10)
                                                                                                                                                        v7 = (v7 + 8)
                                                                                                                                                        v28 = (v28 + 8)
                                                                                                                                                        if ((v28 + 8) != v36):
                                                                                                                                                            continue
                                                                                                                                                        break
                                                                                                                                                if v21:
                                                                                                                                                    while True:  # $label67
                                                                                                                                                        store32((v5 + (v7 << 2)), v10)
                                                                                                                                                        v7 = (v7 + 1)
                                                                                                                                                        v3 = (v3 + 1)
                                                                                                                                                        if ((v3 + 1) != v21):
                                                                                                                                                            continue
                                                                                                                                                        break
                                                                                                                                                break
                                                                                                                                            v3 = (v2 & -4)
                                                                                                                                            if ((v2 & -4) >= v2):
                                                                                                                                                break
                                                                                                                                            v7 = (v2 + (v3 ^ -1))
                                                                                                                                            v10 = 0
                                                                                                                                            v8 = (v2 & 3)
                                                                                                                                            if (v2 & 3):
                                                                                                                                                while True:  # $label68
                                                                                                                                                    store8((v3 + v5), load8u((v3 + v11)))
                                                                                                                                                    v3 = (v3 + 1)
                                                                                                                                                    v10 = (v10 + 1)
                                                                                                                                                    if ((v10 + 1) != v8):
                                                                                                                                                        continue
                                                                                                                                                    break
                                                                                                                                            if (u32(v7) < u32(3)):
                                                                                                                                                break
                                                                                                                                            while True:  # $label69
                                                                                                                                                store8((v3 + v5), load8u((v3 + v11)))
                                                                                                                                                v7 = (v3 + 1)
                                                                                                                                                store8((v5 + (v3 + 1)), load8u((v7 + v11)))
                                                                                                                                                v7 = (v3 + 2)
                                                                                                                                                store8((v5 + (v3 + 2)), load8u((v7 + v11)))
                                                                                                                                                v7 = (v3 + 3)
                                                                                                                                                store8((v5 + (v3 + 3)), load8u((v7 + v11)))
                                                                                                                                                v3 = (v3 + 4)
                                                                                                                                                if ((v3 + 4) != v2):
                                                                                                                                                    continue
                                                                                                                                                break
                                                                                                                                            break
                                                                                                                                        v13 = (v6 + v13)
                                                                                                                                        v12 = (v6 + v12)
                                                                                                                                        if (v16 <= (v6 + v12)):
                                                                                                                                            while True:  # $label71
                                                                                                                                                v12 = (v12 - v16)
                                                                                                                                                v2 = v4
                                                                                                                                                v4 = (v4 + 1)
                                                                                                                                                while True:  # $label70
                                                                                                                                                    if (v2 >= v14):
                                                                                                                                                        break
                                                                                                                                                    if (v4 & 15):
                                                                                                                                                        break
                                                                                                                                                    break
                                                                                                                                                if (v12 >= v16):
                                                                                                                                                    continue
                                                                                                                                                break
                                                                                                                                        if (v13 >= v25):
                                                                                                                                            break
                                                                                                                                        if not (v12 & v23):
                                                                                                                                            break
                                                                                                                                        v2 = load32(v9 + 152)
                                                                                                                                        if load32(v9 + 152):
                                                                                                                                        else:
                                                                                                                                        v2 = 0
                                                                                                                                        if (0 >= load32(v9 + 164)):
                                                                                                                                            break
                                                                                                                                        v17 = (load32(v9 + 168) + (v2 * 548))
                                                                                                                                        break
                                                                                                                                    v2 = load32(v9 + 40)
                                                                                                                                    v3 = load32(v9 + 36)
                                                                                                                                    if (u32(load32(v9 + 40)) > u32(load32(v9 + 36))):
                                                                                                                                        break
                                                                                                                                    if load32(v9 + 48):
                                                                                                                                        store32(v9 + 48, 1)
                                                                                                                                        break
                                                                                                                                    v5 = 0
                                                                                                                                    if (v2 == v3):
                                                                                                                                        v5 = (load32(v9 + 44) > 64)
                                                                                                                                    store32(v9 + 48, v5)
                                                                                                                                    if v5:
                                                                                                                                        break
                                                                                                                                    if (v13 < v25):
                                                                                                                                        continue
                                                                                                                                    break
                                                                                                                                break
                                                                                                                            v11 = 0
                                                                                                                            break
                                                                                                                        v4 = load32(v9 + 40)
                                                                                                                        v2 = load32(v9 + 36)
                                                                                                                        if (u32(load32(v9 + 40)) <= u32(load32(v9 + 36))):
                                                                                                                            while True:  # $label74
                                                                                                                                if load32(v9 + 48):
                                                                                                                                    break
                                                                                                                                if (v2 != v4):
                                                                                                                                    break
                                                                                                                                break
                                                                                                                            v4 = (load32(v9 + 44) > 64)
                                                                                                                            store32(v9 + 48, (load32(v9 + 44) > 64))
                                                                                                                            while True:  # $label75
                                                                                                                                if not v11:
                                                                                                                                    if not v4:
                                                                                                                                        break
                                                                                                                                    if (v13 >= v20):
                                                                                                                                        break
                                                                                                                                v12 = 0
                                                                                                                                while True:  # $label76
                                                                                                                                    # br_table load32(v9)
                                                                                                                                    break
                                                                                                                                    break
                                                                                                                                store32(v9, (5 if v4 else 3))
                                                                                                                                break
                                                                                                                                break
                                                                                                                            store32(v9 + 112, v13)
                                                                                                                            break
                                                                                                                        break
                                                                                                                    a_c()
                                                                                                                    raise Unreachable()
                                                                                                                a_c()
                                                                                                                raise Unreachable()
                                                                                                                break
                                                                                                            break
                                                                                                        a_c()
                                                                                                        raise Unreachable()
                                                                                                    a_c()
                                                                                                    raise Unreachable()
                                                                                                    break
                                                                                                v12 = func275(v9, load32(v9 + 16), load32(v9 + 100), load32(v9 + 104), v14, 277)
                                                                                                break
                                                                                            break
                                                                                            break
                                                                                        a_c()
                                                                                        raise Unreachable()
                                                                                        break
                                                                                    a_c()
                                                                                    raise Unreachable()
                                                                                    break
                                                                                if not 3953:
                                                                                    break
                                                                                break
                                                                            while True:  # $label78
                                                                                if (v14 >= v31):
                                                                                    store32(arg0 + 2400, 1)
                                                                                    break
                                                                                if not load32(arg0 + 2400):
                                                                                    break
                                                                                break
                                                                            v4 = load32(arg0 + 2388)
                                                                            if load32(arg0 + 2388):
                                                                                func190(load32(v4 + 20))
                                                                                store32(v4 + 20, 0)
                                                                            store32(arg0 + 2388, 0)
                                                                            v4 = load32(arg0 + 2416)
                                                                            if (load32(arg0 + 2416) <= 0):
                                                                                break
                                                                            v2 = load32(arg1 + 76)
                                                                            v3 = load32(arg1 + 84)
                                                                            v7 = (load32(arg1 + 76) + (load32(arg0 + 2408) + (load32(arg1 + 84) * v30)))
                                                                            v16 = (load32(arg1 + 80) - v2)
                                                                            v23 = (load32(arg1 + 88) - v3)
                                                                            v6 = 0
                                                                            v10 = 0
                                                                            v31 = 0
                                                                            v25 = (G.global0 - 256)
                                                                            G.global0 = (G.global0 - 256)
                                                                            v2 = (v4 // 25)
                                                                            while True:  # $label79
                                                                                if (u32(v4) > u32(100)):
                                                                                    break
                                                                                if not v7:
                                                                                    break
                                                                                if (v16 <= 0):
                                                                                    break
                                                                                if (v23 <= 0):
                                                                                    break
                                                                                v6 = 1
                                                                                v42 = (v23 - 1)
                                                                                v36 = (v16 - 1)
                                                                                v4 = ((((v16 - 1) & 0xFFFFFFFF) >> 1) if (((v2 << 1) | 1) > v16) else v2)
                                                                                v13 = ((((v23 - 1) & 0xFFFFFFFF) >> 1) if (((v4 << 1) | 1) > v23) else ((((v16 - 1) & 0xFFFFFFFF) >> 1) if (((v2 << 1) | 1) > v16) else v2))
                                                                                if (((((v23 - 1) & 0xFFFFFFFF) >> 1) if (((v4 << 1) | 1) > v23) else ((((v16 - 1) & 0xFFFFFFFF) >> 1) if (((v2 << 1) | 1) > v16) else v2)) <= 0):
                                                                                    break
                                                                                v6 = 0
                                                                                v20 = (v16 << 1)
                                                                                v19 = (v13 << 1)
                                                                                v2 = (v20 * ((v13 << 1) + 2))
                                                                                v9 = func58(1, (((v16 << 1) + (v20 * ((v13 << 1) + 2))) + 4094))
                                                                                if not func58(1, (((v16 << 1) + (v20 * ((v13 << 1) + 2))) + 4094)):
                                                                                    break
                                                                                v24 = (0 - v13)
                                                                                v4 = (v19 | 1)
                                                                                v12 = (v9 + (((v19 | 1) * v16) << 1))
                                                                                v11 = ((v9 + (((v19 | 1) * v16) << 1)) - v20)
                                                                                # TODO: memory.fill
                                                                                # TODO: memory.fill
                                                                                v17 = (v2 + v9)
                                                                                v18 = (v4 * v4)
                                                                                v28 = 255
                                                                                v3 = 0
                                                                                v14 = 255
                                                                                v4 = v7
                                                                                while True:  # $label81
                                                                                    v6 = v3
                                                                                    v8 = v14
                                                                                    v2 = 0
                                                                                    while True:  # $label80
                                                                                        v5 = load8u((v2 + v4))
                                                                                        store8((v25 + load8u((v2 + v4))), 1)
                                                                                        v21 = (v5 > v6)
                                                                                        v3 = (v5 if (v5 > v6) else v3)
                                                                                        v31 = (v5 if v21 else v31)
                                                                                        v21 = (v5 < v8)
                                                                                        v14 = (v5 if (v5 < v8) else v14)
                                                                                        v28 = (v5 if v21 else v28)
                                                                                        v6 = (v6 if (v5 < v6) else v5)
                                                                                        v8 = (v8 if (v5 > v8) else v5)
                                                                                        v2 = (v2 + 1)
                                                                                        if ((v2 + 1) != v16):
                                                                                            continue
                                                                                        break
                                                                                    v4 = (v4 + v30)
                                                                                    v10 = (v10 + 1)
                                                                                    if ((v10 + 1) != v23):
                                                                                        continue
                                                                                    break
                                                                                v8 = (v3 - v14)
                                                                                v5 = (v17 + v20)
                                                                                v6 = -1
                                                                                v2 = 0
                                                                                v4 = 0
                                                                                while True:  # $label83
                                                                                    if load8u((v4 + v25)):
                                                                                        v2 = (v2 + 1)
                                                                                        if (v6 >= 0):
                                                                                            v3 = (v4 - v6)
                                                                                            v8 = ((v4 - v6) if (v3 < v8) else v8)
                                                                                    else:
                                                                                    v3 = v6
                                                                                    while True:  # $label82
                                                                                        v6 = (v4 | 1)
                                                                                        if not load8u((v25 + (v4 | 1))):
                                                                                            v6 = v3
                                                                                            break
                                                                                        v2 = (v2 + 1)
                                                                                        if (v3 < 0):
                                                                                            break
                                                                                        v3 = (v6 - v3)
                                                                                        v8 = ((v6 - v3) if (v3 < v8) else v8)
                                                                                        break
                                                                                    v4 = (v4 + 2)
                                                                                    if ((v4 + 2) != 256):
                                                                                        continue
                                                                                    break
                                                                                v3 = (v8 << 2)
                                                                                v6 = ((v8 * 12) >> 2)
                                                                                v8 = ((v8 << 2) - ((v8 * 12) >> 2))
                                                                                v21 = (v5 + 2046)
                                                                                v4 = 1
                                                                                while True:  # $label85
                                                                                    v5 = (v4 << 1)
                                                                                    while True:  # $label84
                                                                                        if (v4 <= v6):
                                                                                            break
                                                                                        if (v3 <= v4):
                                                                                            break
                                                                                        break
                                                                                    v14 = (((((v3 - v4) * v6) // v8) & 0xFFFFFFFF) >> 2)
                                                                                    store16((v21 + (v4 << 1)), (((((v3 - v4) * v6) // v8) & 0xFFFFFFFF) >> 2))
                                                                                    store16((v21 - v5), (0 - v14))
                                                                                    v4 = (v4 + 1)
                                                                                    if ((v4 + 1) != 1024):
                                                                                        continue
                                                                                    break
                                                                                store16(v21, 0)
                                                                                # TODO: i32.div_u
                                                                                v18 = v18
                                                                                while True:  # $label86
                                                                                    if (v2 < 3):
                                                                                        break
                                                                                    if (v23 <= v24):
                                                                                        break
                                                                                    v10 = (v13 + 2)
                                                                                    v40 = (v16 & 1)
                                                                                    v43 = (v16 & -2)
                                                                                    v44 = (v20 - 2)
                                                                                    v20 = (v13 ^ -1)
                                                                                    v5 = (v16 - v13)
                                                                                    v41 = (v13 - 1)
                                                                                    v8 = (v13 + 1)
                                                                                    v45 = ((v13 + 1) & -2)
                                                                                    v46 = (v8 & 1)
                                                                                    v47 = (v12 + (v36 << 1))
                                                                                    v48 = (v17 + (v8 << 1))
                                                                                    v49 = (v12 + ((v8 + v13) << 1))
                                                                                    v50 = ((v16 - 2) == v19)
                                                                                    v2 = v9
                                                                                    v3 = v7
                                                                                    while True:  # $label94
                                                                                        v14 = 0
                                                                                        v4 = 0
                                                                                        v6 = 0
                                                                                        if v36:
                                                                                            while True:  # $label87
                                                                                                v19 = (v4 << 1)
                                                                                                v14 = (load8u((v3 + v4)) + (v14 & 65535))
                                                                                                v32 = ((load8u((v3 + v4)) + (v14 & 65535)) + load16u((v11 + v19)))
                                                                                                v19 = (v2 + v19)
                                                                                                store16((v12 + (v4 << 1)), (((load8u((v3 + v4)) + (v14 & 65535)) + load16u((v11 + v19))) - load16u((v2 + v19))))
                                                                                                store16(v19, v32)
                                                                                                v32 = (v4 | 1)
                                                                                                v19 = ((v4 | 1) << 1)
                                                                                                v14 = (load8u((v3 + v32)) + (v14 & 65535))
                                                                                                v32 = ((load8u((v3 + v32)) + (v14 & 65535)) + load16u((v11 + v19)))
                                                                                                v19 = (v2 + v19)
                                                                                                store16((v12 + ((v4 | 1) << 1)), (((load8u((v3 + v32)) + (v14 & 65535)) + load16u((v11 + v19))) - load16u((v2 + v19))))
                                                                                                store16(v19, v32)
                                                                                                v4 = (v4 + 2)
                                                                                                v6 = (v6 + 2)
                                                                                                if ((v6 + 2) != v43):
                                                                                                    continue
                                                                                                break
                                                                                        if v40:
                                                                                            v6 = (v4 << 1)
                                                                                            v4 = (load16u((v6 + v11)) + (v14 + load8u((v3 + v4))))
                                                                                            v6 = (v2 + v6)
                                                                                            store16((v12 + (v4 << 1)), ((load16u((v6 + v11)) + (v14 + load8u((v3 + v4)))) - load16u((v2 + v6))))
                                                                                            store16(v6, v4)
                                                                                        v14 = (v2 + (v16 << 1))
                                                                                        v19 = ((v2 + (v16 << 1)) == v12)
                                                                                        v4 = 0
                                                                                        v6 = 0
                                                                                        if (v13 <= v24):
                                                                                            while True:  # $label88
                                                                                                store16((v17 + (v4 << 1)), (((v18 * ((load16u((v12 + ((v13 - v4) << 1))) + load16u((v12 + ((v4 + v41) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                                v11 = (v4 | 1)
                                                                                                store16((v17 + ((v4 | 1) << 1)), (((v18 * ((load16u((v12 + ((v13 - v11) << 1))) + load16u((v12 + ((v4 + v13) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                                v4 = (v4 + 2)
                                                                                                v6 = (v6 + 2)
                                                                                                if ((v6 + 2) != v45):
                                                                                                    continue
                                                                                                break
                                                                                            if v46:
                                                                                                store16((v17 + (v4 << 1)), (((v18 * ((load16u((v12 + ((v13 - v4) << 1))) + load16u((v12 + ((v4 + v41) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                            while True:  # $label89
                                                                                                v4 = v8
                                                                                                if (v8 >= v5):
                                                                                                    break
                                                                                                v6 = v8
                                                                                                if not v40:
                                                                                                    store16(v48, (((v18 * ((load16u(v49) - load16u(v12)) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                                    v6 = v10
                                                                                                v4 = v5
                                                                                                if v50:
                                                                                                    break
                                                                                                while True:  # $label90
                                                                                                    store16((v17 + (v6 << 1)), (((v18 * ((load16u((v12 + ((v6 + v13) << 1))) - load16u((v12 + ((v6 + v20) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                                    v4 = (v6 + 1)
                                                                                                    store16((v17 + ((v6 + 1) << 1)), (((v18 * ((load16u((v12 + ((v4 + v13) << 1))) - load16u((v12 + ((v6 - v13) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                                    v6 = (v6 + 2)
                                                                                                    if ((v6 + 2) != v5):
                                                                                                        continue
                                                                                                    break
                                                                                                v4 = v5
                                                                                                break
                                                                                            if (v4 < v16):
                                                                                                while True:  # $label91
                                                                                                    store16((v17 + (v4 << 1)), (((v18 * (((load16u(v47) << 1) - (load16u((v12 + ((v44 - (v4 + v13)) << 1))) + load16u((v12 + ((v4 + v20) << 1))))) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                                    v4 = (v4 + 1)
                                                                                                    if ((v4 + 1) != v16):
                                                                                                        continue
                                                                                                    break
                                                                                            v4 = 0
                                                                                            while True:  # $label93
                                                                                                while True:  # $label92
                                                                                                    v11 = (v4 + v7)
                                                                                                    v6 = load8u((v4 + v7))
                                                                                                    if (v31 <= load8u((v4 + v7))):
                                                                                                        break
                                                                                                    if (v6 <= v28):
                                                                                                        break
                                                                                                    v6 = (load16s((v21 + ((load16u((v17 + (v4 << 1))) - (v6 << 2)) << 1))) + v6)
                                                                                                    v6 = ((load16s((v21 + ((load16u((v17 + (v4 << 1))) - (v6 << 2)) << 1))) + v6) if (v6 > 0) else 0)
                                                                                                    store8(v11, (255 if (v6 >= 255) else ((load16s((v21 + ((load16u((v17 + (v4 << 1))) - (v6 << 2)) << 1))) + v6) if (v6 > 0) else 0)))
                                                                                                    break
                                                                                                v4 = (v4 + 1)
                                                                                                if ((v4 + 1) != v16):
                                                                                                    continue
                                                                                                break
                                                                                            v7 = (v7 + v30)
                                                                                        v3 = (((v30 if (v24 < v42) else 0) if (v24 >= 0) else 0) + v3)
                                                                                        v11 = v2
                                                                                        v2 = (v9 if v19 else v14)
                                                                                        v24 = (v24 + 1)
                                                                                        if ((v24 + 1) != v23):
                                                                                            continue
                                                                                        break
                                                                                    break
                                                                                v6 = 1
                                                                                break
                                                                            G.global0 = (v25 + 256)
                                                                            if not v6:
                                                                                break
                                                                            break
                                                                        v2 = (load32(arg0 + 2408) + (v15 * v30))
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
                                        a_c()
                                        raise Unreachable()
                                        break
                                    a_c()
                                    raise Unreachable()
                                    break
                                store64(arg0 + 2404, 0)
                                v4 = load32(arg0 + 2388)
                                if load32(arg0 + 2388):
                                    func190(load32(v4 + 20))
                                    store32(v4 + 20, 0)
                                store32(arg0 + 2388, 0)
                                break
                            v4 = 0
                            store32(af(v4) + 104, 0)
                            if not v4:
                                break
                            break
                        v2 = load32(arg1 + 84)
                        if (v15 < load32(arg1 + 84)):
                            v3 = (v2 - v15)
                            if ((v2 - v15) & 1):
                                break
                            store32(arg1 + 20, (load32(arg1 + 20) + (load32(arg0 + 2324) * v3)))
                            v7 = (load32(arg0 + 2328) * (v3 >> 1))
                            store32(arg1 + 24, ((load32(arg0 + 2328) * (v3 >> 1)) + load32(arg1 + 24)))
                            store32(arg1 + 28, (load32(arg1 + 28) + v7))
                            while True:  # $label97
                                if not v4:
                                    v4 = 0
                                    break
                                v4 = (v4 + (load32(arg1) * v3))
                                store32(arg1 + 104, (v4 + (load32(arg1) * v3)))
                                break
                            v15 = v2
                        if (v15 >= v35):
                            break
                        v3 = load32(arg1 + 76)
                        store32(arg1 + 20, (load32(arg1 + 76) + load32(arg1 + 20)))
                        v7 = (v3 >> 1)
                        store32(arg1 + 24, ((v3 >> 1) + load32(arg1 + 24)))
                        store32(arg1 + 28, (load32(arg1 + 28) + v7))
                        if v4:
                            store32(arg1 + 104, (v3 + v4))
                        store32(arg1 + 8, (v15 - v2))
                        store32(arg1 + 16, (v35 - v15))
                        store32(arg1 + 12, (load32(arg1 + 80) - v3))
                        break
                    v2 = call_table(load32(arg1 + 44))
                    if (load32(arg0 + 168) != (v37 + 1)):
                        break
                    if (v33 >= v39):
                        break
                    # TODO: memory.copy
                    arg1 = (0 - v34)
                    # TODO: memory.copy
                    # TODO: memory.copy
                    break
                    break
                a_c()
                raise Unreachable()
                break
            a_c()
            raise Unreachable()
            break
        v2 = func99(arg0, 3, 8467)
        break
    G.global0 = (v29 - -64)
    return v2

# ----------------------------------------------------------
# $func466
# ----------------------------------------------------------
def func466(arg0, arg1):

# ----------------------------------------------------------
# $func467
# ----------------------------------------------------------
def func467(arg0, arg1, arg2):
    return e()

# ----------------------------------------------------------
# $ze
# Export: ze
# ----------------------------------------------------------
def ze(arg0):
    """Export: ze"""
    while True:  # $label0
        if not arg0:
            break
        v21 = load32(9142440)
        if (load32(9142440) > 0):
            while True:  # $label12
                v3 = 0
                while True:  # $label11
                    v2 = 0
                    v25 = 0.0
                    v26 = 0.0
                    while True:  # $label1
                        v17 = ((load32(9142440) * v3) + v5)
                        v22 = (((load32(9142440) * v3) + v5) + load32(9147288))
                        v1 = load8u((((load32(9142440) * v3) + v5) + load32(9147288)))
                        v7 = i32(load8u((((load32(9142440) * v3) + v5) + load32(9147288))))
                        v12 = ((i32(load8u((((load32(9142440) * v3) + v5) + load32(9147288)))) + 128) if (v7 < 0) else v7)
                        if (u32(((i32(load8u((((load32(9142440) * v3) + v5) + load32(9147288)))) + 128) if (v7 < 0) else v7)) <= u32(15)):
                            v7 = load32(load32(GAME_STATE) + 24)
                            break
                        break
                    v16 = (((v12 & 0xFFFFFFFF) >> 4) - 1)
                    v4 = ((v1 & 0xFFFFFFFF) >> 7)
                    while True:  # $label2
                        v10 = load32((load32(9561728) + (v17 << 2)))
                        if (load32((load32(9561728) + (v17 << 2))) < 4):
                            v1 = (((v1 << 4) | ((((v1 << 24) + 1879048192) & 0xFFFFFFFF) >> 28)) & 255)
                            v9 = ((u32((((v1 << 4) | ((((v1 << 24) + 1879048192) & 0xFFFFFFFF) >> 28)) & 255)) < u32(14)) & ((10965 & 0xFFFFFFFF) >> v1))
                            break
                        v9 = 1
                        v1 = (((v10 << 1) & 6) | v4)
                        if not (((v10 << 1) & 6) | v4):
                            v1 = load32(load32(GAME_STATE) + 24)
                            v16 = (5 if (v1 == 2) else (4 if (load32(load32(GAME_STATE) + 24) == 3) else 7))
                            break
                        v16 = (v1 - 1)
                        break
                    v13 = load32(9140332)
                    v1 = load32((load32(9140332) + (v16 << 2)))
                    v7 = load32(load32((load32(9140332) + (v16 << 2))))
                    while True:  # $label3
                        if not load32(v1 + 20):
                            break
                        v2 = load32(v1 + 28)
                        if (load32(v1 + 28) != 2147483647):
                            break
                        while True:  # $label4
                            v14 = load8u(9142916)
                            if load8u(9142916):
                                v2 = load32(59152)
                                store32(59152, (load32(59152) + 1))
                                v8 = load32(9568052)
                                break
                            v8 = load32(9568052)
                            v2 = ((load32(9140308) + v7) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                            break
                        v15 = v7
                        store32(v1 + 28, v2)
                        v11 = load32(v1 + 4)
                        v18 = load32(9568048)
                        store32(9568048, (load32(9568048) + 1))
                        store32(((v18 << 2) + 9563952), v1)
                        store32(9568052, (((v15 * (v11 + 2)) << 2) + v8))
                        if not v14:
                            break
                        v8 = load32(9568056)
                        store32(v1 + 56, load32(9568056))
                        store32(9568056, (v8 + ((v11 * load32(v1)) << 2)))
                        break
                    v14 = (v5 << 5)
                    v15 = (v3 << 5)
                    v2 = ((((v5 << 5) % v7) + v2) + (((v3 << 5) % v7) * v7))
                    v18 = load32(v1 + 32)
                    while True:  # $label5
                        if v9:
                            v4 = 0
                            break
                        while True:  # $label6
                            v1 = (((v10 % 4) << 1) | v4)
                            if not (((v10 % 4) << 1) | v4):
                                v1 = load32(load32(GAME_STATE) + 24)
                                break
                            break
                        v1 = load32(((5 if (v1 == 2) else (4 if (load32(load32(GAME_STATE) + 24) == 3) else 7)) + ((v1 - 1) << 2)))
                        v4 = load32(load32(((5 if (v1 == 2) else (4 if (load32(load32(GAME_STATE) + 24) == 3) else 7)) + ((v1 - 1) << 2))))
                        v10 = 0
                        v9 = 0
                        while True:  # $label7
                            if not load32(v1 + 20):
                                break
                            v9 = load32(v1 + 28)
                            if (load32(v1 + 28) != 2147483647):
                                break
                            while True:  # $label8
                                v13 = load8u(9142916)
                                if load8u(9142916):
                                    v9 = load32(59152)
                                    store32(59152, (load32(59152) + 1))
                                    v8 = load32(9568052)
                                    break
                                v8 = load32(9568052)
                                v9 = ((load32(9140308) + v4) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                break
                            v19 = v4
                            store32(v1 + 28, v9)
                            v11 = load32(v1 + 4)
                            v20 = load32(9568048)
                            store32(9568048, (load32(9568048) + 1))
                            store32(((v20 << 2) + 9563952), v1)
                            store32(9568052, (((v19 * (v11 + 2)) << 2) + v8))
                            if not v13:
                                break
                            v8 = load32(9568056)
                            store32(v1 + 56, load32(9568056))
                            store32(9568056, (v8 + ((v11 * load32(v1)) << 2)))
                            break
                        v8 = (v12 & 15)
                        v12 = (load32(v1 + 32) == 23)
                        v11 = ((13 - (v12 & 15)) if (load32(v1 + 32) == 23) else v8)
                        v13 = (((v14 % v4) + v9) + ((v15 % v4) * v4))
                        v14 = (v2 if v12 else (((v14 % v4) + v9) + ((v15 % v4) * v4)))
                        v15 = (v4 // 32)
                        v1 = (v1 + (load32(v1 + 44) << 2))
                        v8 = load32((v1 + (load32(v1 + 44) << 2)))
                        while True:  # $label9
                            if not load32(v1 + 20):
                                break
                            v10 = load32(v1 + 28)
                            if (load32(v1 + 28) != 2147483647):
                                break
                            while True:  # $label10
                                v19 = load8u(9142916)
                                if load8u(9142916):
                                    v10 = load32(59152)
                                    store32(59152, (load32(59152) + 1))
                                    v4 = load32(9568052)
                                    break
                                v4 = load32(9568052)
                                v10 = ((load32(9140308) + v8) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                break
                            v20 = v8
                            store32(v1 + 28, v10)
                            v9 = load32(v1 + 4)
                            v23 = load32(9568048)
                            store32(9568048, (load32(9568048) + 1))
                            store32(((v23 << 2) + 9563952), v1)
                            store32(9568052, (((v20 * (v9 + 2)) << 2) + v4))
                            if not v19:
                                break
                            v4 = load32(9568056)
                            store32(v1 + 56, load32(9568056))
                            store32(9568056, (v4 + ((v9 * load32(v1)) << 2)))
                            break
                        v2 = (v13 if v12 else v2)
                        v26 = i32(((v10 + ((v8 * v11) << 5)) + ((load32((((v17 % 24) << 2) + 9824)) << 5) & 32)))
                        v4 = ((v8 // 32) << 16)
                        v25 = i32(v14)
                        break
                    v8 = (0 if v12 else (v15 << 8))
                    v1 = (load32(9142400) + (v17 << 4))
                    storef32((load32(9142400) + (v17 << 4)), i32(v2))
                    storef32(v1 + 4, v25)
                    storef32(v1 + 8, v26)
                    storef32(v1 + 12, i32(((v8 + ((v7 // 32) if (v18 != 23) else 0)) + v4)))
                    store8(v22, v16)
                    v3 = (v3 + 1)
                    if ((v3 + 1) != v21):
                        continue
                    break
                v5 = (v5 + 1)
                if ((v5 + 1) != v21):
                    continue
                break
        while True:  # $label13
            v2 = load32(9140328)
            if not load32(9140328):
                break
            v1 = 0
            v3 = load32(9142440)
            v5 = (load32(9142440) * v3)
            v3 = 0
            if (u32(v2) >= u32(4)):
                v4 = (v2 & -4)
                while True:  # $label14
                    v7 = (v3 << 2)
                    v6 = ((((v5 * load32(load32((((v3 << 2) | 12) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + ((((((v5 * load32(load32((v7 + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + v6) + (((v5 * load32(load32(((v7 | 4) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)) + (((v5 * load32(load32(((v7 | 8) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)))
                    v3 = (v3 + 4)
                    v24 = (v24 + 4)
                    if ((v24 + 4) != v4):
                        continue
                    break
            v2 = (v2 & 3)
            if not (v2 & 3):
                break
            while True:  # $label15
                v6 = ((((v5 * load32(load32(((v3 << 2) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + v6)
                v3 = (v3 + 1)
                v1 = (v1 + 1)
                if ((v1 + 1) != v2):
                    continue
                break
            break
        if load32(9681936):
            break
        v3 = func26(16)
        v5 = (v6 << 2)
        store32(func26(16) + 4, (v6 << 2))
        store32(v3, func26((-1 if (u32(v5) > u32(1073741823)) else (v6 << 4))))
        store64(v3 + 8, 206158430208)
        store32(9681936, v3)
        break
    v1 = 0
    v7 = load32(9142440)
    if (load32(9142440) > 0):
        while True:  # $label19
            v5 = (v1 + 1)
            v3 = 0
            while True:  # $label18
                while True:  # $label17
                    while True:  # $label16
                        v2 = load32(9142440)
                        v6 = load8s((load32(9147288) + ((load32(9142440) * v3) + v1)))
                        if (load8s((load32(9147288) + ((load32(9142440) * v3) + v1))) >= 0):
                            if (load32(load32((load32(9140332) + ((v6 & 255) << 2))) + 32) == 23):
                                break
                        v6 = load32(9142840)
                        v3 = (v3 + 1)
                        v2 = (((v3 + 1) * (v2 + 2)) + v5)
                        v4 = entities[load32((load32(9142840) + ((((v3 + 1) * (v2 + 2)) + v5) << 2)))]
                        if (load32(((load8u(entities[load32((load32(9142840) + ((((v3 + 1) * (v2 + 2)) + v5) << 2)))].sub_state) * 404) + ENTITY_TYPES) + 264) == 4):
                            v2 = (((load32(9142440) + 2) * v3) + v5)
                            v6 = load32(9142840)
                        v2 = (v6 + (v2 << 2))
                        if (load32((v6 + (v2 << 2))) != 1):
                            break
                        store32(v2, 0)
                        v2 = (load32(9142440) + 2)
                        store32((v6 + (((((load32(9142440) + 2) + v3) * v2) + v5) << 2)), 0)
                        break
                        break
                    v6 = load32(9142840)
                    v2 = (v2 + 2)
                    v3 = (v3 + 1)
                    v4 = (load32(9142840) + ((((v2 + 2) * (v3 + 1)) + v5) << 2))
                    if not load32((load32(9142840) + ((((v2 + 2) * (v3 + 1)) + v5) << 2))):
                        store32(v4, 1)
                        v2 = (load32(9142440) + 2)
                    v2 = (((v2 + v3) * v2) + v5)
                    v4 = load32((v6 + ((((v2 + v3) * v2) + v5) << 2)))
                    if (u32(load32((v6 + ((((v2 + v3) * v2) + v5) << 2)))) >= u32(3)):
                        v6 = (load32(9142440) + 2)
                        v2 = ((((load32(9142440) + 2) + v3) * v6) + v5)
                        v6 = load32(9142840)
                    store32((v6 + (v2 << 2)), 1)
                    break
                if (v3 != v7):
                    continue
                break
            v1 = v5
            if (v5 != v7):
                continue
            break
    if not arg0:
    return func115(0, 0, load32(9142440), 0, 0)

# ----------------------------------------------------------
# $func470
# ----------------------------------------------------------
def func470(arg0, arg1):
    v7 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v2 = load32(ENTITIES)
    arg1 = entities[arg0]
    v5 = load16u(arg1 + 116)
    v6 = load16u(arg1 + 118)
    while True:  # $label0
        v3 = load32(9142840)
        arg1 = (load32(9142440) + 2)
        v4 = (v6 + (load32(9142440) + 2))
        if (load32((load32(9142840) + ((v5 + (((v6 + (load32(9142440) + 2)) + 1) * arg1)) << 2)) + 4) != 1):
            break
        if (load32((((v5 + ((v4 + 3) * arg1)) << 2) + v3) + 12) != 1):
            break
        arg1 = 0
        v3 = (load32(PLAYERS) + (load16u((v2 + (arg0 * 132)) + 110) * 286704))
        v2 = (load32(((load32(PLAYERS) + (load16u((v2 + (arg0 * 132)) + 110) * 286704)) + 284192)) << 2)
        v3 = load32((v3 + 284196))
        if (u32((load32(((load32(PLAYERS) + (load16u((v2 + (arg0 * 132)) + 110) * 286704)) + 284192)) << 2)) <= u32(load32((v3 + 284196)))):
            # TODO: i32.div_u
            v4 = v2
            v4 = (v3 if (u32(v4) <= u32(1)) else v2)
            v8 = ((v6 << 16) | v5)
            while True:  # $label1
                arg1 = (arg1 + 1)
                if (arg1 != v4):
                    continue
                break
        arg1 = 0
        while True:  # $label2
            if load8u(9142917):
                break
            arg0 = load32(9299880)
            if load32(9299880):
                arg0 = (arg0 - 1)
                store32(9299880, (arg0 - 1))
                arg1 = load32((load32(9299872) + (arg0 << 2)))
                break
            arg1 = load32(9163776)
            arg0 = (load32(9163776) + 1)
            store32(9163776, (load32(9163776) + 1))
            v2 = load32(9163784)
            if (u32(arg0) < u32(load32(9163784))):
                break
            store32(v7, v2)
            a_b()
            store32(9163784, (load32(9163784) + 40000))
            break
        # TODO: f32.demote_f64
        break
    G.global0 = (v7 + 16)

# ----------------------------------------------------------
# $func471
# ----------------------------------------------------------
def func471(arg0, arg1):
    v6 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v11 = ((arg1 & 0xFFFFFFFF) >> 16)
    v14 = (((arg1 & 0xFFFFFFFF) >> 16) + 3)
    v12 = (v11 + 2)
    v13 = (v11 + 1)
    v8 = (arg1 & 65535)
    v15 = ((arg1 & 65535) + 2)
    v7 = entities[arg0]
    arg1 = load32(9142440)
    while True:  # $label6
        arg0 = v8
        v8 = (v8 + 1)
        while True:  # $label0
            if (u32(arg1) <= u32(v11)):
                break
            if (u32(arg0) >= u32(arg1)):
                break
            while True:  # $label1
                arg1 = load32((load32(9142840) + ((v8 + (v13 * (arg1 + 2))) << 2)))
                if (u32(load32((load32(9142840) + ((v8 + (v13 * (arg1 + 2))) << 2)))) < u32(3)):
                    break
                arg1 = entities[arg1]
                v5 = load8u(entities[arg1].sub_state)
                v2 = ((load8u(entities[arg1].sub_state) * 404) + ENTITY_TYPES)
                if (load32(((load8u(entities[arg1].sub_state) * 404) + ENTITY_TYPES) + 264) != 4):
                    break
                v9 = load32(PLAYERS)
                v10 = load16u(v7 + 110)
                v4 = players[load16u(v7 + 110)]
                v2 = (load32(v2 + 312) * load32((players[load16u(v7 + 110)] + 284188)))
                # TODO: i32.div_u
                v2 = ((load32(v2 + 312) * load32((players[load16u(v7 + 110)] + 284188))) if (u32(v2) < u32(100)) else 100)
                v3 = load16u(arg1 + 110)
                v4 = load32(v4 + 278556)
                if load32(v4 + 278556):
                    v4 = (v4 + ((load8u(v7 + 122) + (v3 * 255)) << 2))
                    store32((v4 + ((load8u(v7 + 122) + (v3 * 255)) << 2)), (load32(v4) + v2))
                v3 = load32(((v9 + (v3 * 286704)) + 278564))
                if load32(((v9 + (v3 * 286704)) + 278564)):
                    v3 = (v3 + (((v10 * 255) + v5) << 2))
                    store32((v3 + (((v10 * 255) + v5) << 2)), (load32(v3) + v2))
                if (load8u(arg1 + 125) == 3):
                    break
                v3 = (arg1 - -64)
                v5 = load32(arg1 + 64)
                if (u32(v2) >= u32(load32(arg1 + 64))):
                    store32(v3, 0)
                    break
                store32(v3, (v5 - v2))
                if not load32(arg1 + 92):
                    break
                if load8u(9147141):
                    break
                store32(v6 + 32, v2)
                a_b()
                break
            arg1 = load32(9142440)
            break
        while True:  # $label2
            if (u32(arg1) <= u32(v13)):
                break
            if (u32(arg0) >= u32(arg1)):
                break
            while True:  # $label3
                arg1 = load32((load32(9142840) + ((v8 + (v12 * (arg1 + 2))) << 2)))
                if (u32(load32((load32(9142840) + ((v8 + (v12 * (arg1 + 2))) << 2)))) < u32(3)):
                    break
                arg1 = entities[arg1]
                v5 = load8u(entities[arg1].sub_state)
                v2 = ((load8u(entities[arg1].sub_state) * 404) + ENTITY_TYPES)
                if (load32(((load8u(entities[arg1].sub_state) * 404) + ENTITY_TYPES) + 264) != 4):
                    break
                v9 = load32(PLAYERS)
                v10 = load16u(v7 + 110)
                v4 = players[load16u(v7 + 110)]
                v2 = (load32(v2 + 312) * load32((players[load16u(v7 + 110)] + 284188)))
                # TODO: i32.div_u
                v2 = ((load32(v2 + 312) * load32((players[load16u(v7 + 110)] + 284188))) if (u32(v2) < u32(100)) else 100)
                v3 = load16u(arg1 + 110)
                v4 = load32(v4 + 278556)
                if load32(v4 + 278556):
                    v4 = (v4 + ((load8u(v7 + 122) + (v3 * 255)) << 2))
                    store32((v4 + ((load8u(v7 + 122) + (v3 * 255)) << 2)), (load32(v4) + v2))
                v3 = load32(((v9 + (v3 * 286704)) + 278564))
                if load32(((v9 + (v3 * 286704)) + 278564)):
                    v3 = (v3 + (((v10 * 255) + v5) << 2))
                    store32((v3 + (((v10 * 255) + v5) << 2)), (load32(v3) + v2))
                if (load8u(arg1 + 125) == 3):
                    break
                v3 = (arg1 - -64)
                v5 = load32(arg1 + 64)
                if (u32(v2) >= u32(load32(arg1 + 64))):
                    store32(v3, 0)
                    break
                store32(v3, (v5 - v2))
                if not load32(arg1 + 92):
                    break
                if load8u(9147141):
                    break
                store32(v6 + 16, v2)
                a_b()
                break
            arg1 = load32(9142440)
            break
        while True:  # $label4
            if (u32(arg1) <= u32(v12)):
                break
            if (u32(arg0) >= u32(arg1)):
                break
            while True:  # $label5
                arg1 = load32((load32(9142840) + ((v8 + (v14 * (arg1 + 2))) << 2)))
                if (u32(load32((load32(9142840) + ((v8 + (v14 * (arg1 + 2))) << 2)))) < u32(3)):
                    break
                arg1 = entities[arg1]
                v5 = load8u(entities[arg1].sub_state)
                v2 = ((load8u(entities[arg1].sub_state) * 404) + ENTITY_TYPES)
                if (load32(((load8u(entities[arg1].sub_state) * 404) + ENTITY_TYPES) + 264) != 4):
                    break
                v9 = load32(PLAYERS)
                v10 = load16u(v7 + 110)
                v4 = players[load16u(v7 + 110)]
                v2 = (load32(v2 + 312) * load32((players[load16u(v7 + 110)] + 284188)))
                # TODO: i32.div_u
                v2 = ((load32(v2 + 312) * load32((players[load16u(v7 + 110)] + 284188))) if (u32(v2) < u32(100)) else 100)
                v3 = load16u(arg1 + 110)
                v4 = load32(v4 + 278556)
                if load32(v4 + 278556):
                    v4 = (v4 + ((load8u(v7 + 122) + (v3 * 255)) << 2))
                    store32((v4 + ((load8u(v7 + 122) + (v3 * 255)) << 2)), (load32(v4) + v2))
                v3 = load32(((v9 + (v3 * 286704)) + 278564))
                if load32(((v9 + (v3 * 286704)) + 278564)):
                    v3 = (v3 + (((v10 * 255) + v5) << 2))
                    store32((v3 + (((v10 * 255) + v5) << 2)), (load32(v3) + v2))
                if (load8u(arg1 + 125) == 3):
                    break
                v3 = (arg1 - -64)
                v5 = load32(arg1 + 64)
                if (u32(v2) >= u32(load32(arg1 + 64))):
                    store32(v3, 0)
                    break
                store32(v3, (v5 - v2))
                if not load32(arg1 + 92):
                    break
                if load8u(9147141):
                    break
                store32(v6, v2)
                a_b()
                break
            arg1 = load32(9142440)
            break
        if (arg0 != v15):
            continue
        break
    G.global0 = (v6 + 48)

# ----------------------------------------------------------
# $fe
# Export: fe
# ----------------------------------------------------------
def fe(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
    """Export: fe"""
    while True:  # $label0
        if (u32(load32(PLAYER_COUNT)) <= u32(arg1)):
            break
        if (arg0 == load32(38624)):
            arg0 = (load32(39056) if (arg11 == 3) else (load32(38632) if (arg11 == 2) else (load32(38628) if (arg11 == 1) else arg0)))
        if (load32(38604) == arg0):
            arg0 = (load32(38616) if (arg11 == 3) else (load32(38612) if (arg11 == 2) else (load32(38608) if (arg11 == 1) else arg0)))
        arg0 = ((load32(38620) if (arg0 == load32(38560)) else arg0) if arg11 else arg0)
        arg0 = func34(((load32(38620) if (arg0 == load32(38560)) else arg0) if arg11 else arg0), arg1, arg2, arg3, ((arg4 if (arg0 == 7) else 0) if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) == 1) else arg4), 1)
        if not func34(((load32(38620) if (arg0 == load32(38560)) else arg0) if arg11 else arg0), arg1, arg2, arg3, ((arg4 if (arg0 == 7) else 0) if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) == 1) else arg4), 1):
            break
        arg1 = load32(ENTITIES)
        arg2 = entities[arg0]
        store32(entities[arg0].defense, arg6)
        store32(arg2 + 52, arg5)
        if arg7:
            store32(arg2 + 64, arg7)
        if arg8:
            store32((arg1 + (arg0 * 132)) + 68, arg8)
        arg0 = (arg1 + (arg0 * 132))
        store32((arg1 + (arg0 * 132)) + 72, arg10)
        store32(arg0 + 84, arg9)
        break

# ----------------------------------------------------------
# $ee
# Export: ee
# ----------------------------------------------------------
def ee(arg0, arg1, arg2):
    """Export: ee"""
    v8 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    func182()
    arg0 = (arg0 + 1)
    store32(PLAYER_COUNT, (arg0 + 1))
    store16(9147208, 1)
    v3 = load32(PLAYERS)
    if load32(PLAYERS):
    else:
    v14 = (i32(arg0) * 286704)
    v3 = (load32(PLAYER_COUNT) if i32(((v14 & 0xFFFFFFFF) >> 32)) else i32((i32(arg0) * 286704)))
    arg0 = func26((load32(PLAYER_COUNT) if i32(((v14 & 0xFFFFFFFF) >> 32)) else i32((i32(arg0) * 286704))))
    # TODO: memory.fill
    store32(PLAYERS, arg0)
    store8((arg0 + 283974), 255)
    store16(arg0 + 283972, 65535)
    store32(v8 + 16, arg2)
    v10 = load32(GAME_STATE)
    store32(load32(GAME_STATE) + 24, arg1)
    store32(v10, arg2)
    store8(9681940, 1)
    v6 = load32(PLAYER_COUNT)
    v3 = (load32(PLAYER_COUNT) * v6)
    v5 = func26((load32(PLAYER_COUNT) * v6))
    # TODO: memory.fill
    store32(9143004, v5)
    arg0 = func26(v3)
    # TODO: memory.fill
    store32(9143012, arg0)
    while True:  # $label0
        if not v3:
            break
        arg2 = 0
        arg0 = 0
        if (u32(v3) >= u32(4)):
            v7 = (v3 & -4)
            arg1 = 0
            while True:  # $label1
                store8((arg0 + v5), (load32(((arg0 << 2) + 9147392)) != 0))
                v4 = (arg0 | 1)
                store8((v5 + (arg0 | 1)), (load32(((v4 << 2) + 9147392)) != 0))
                v4 = (arg0 | 2)
                store8((v5 + (arg0 | 2)), (load32(((v4 << 2) + 9147392)) != 0))
                v4 = (arg0 | 3)
                store8((v5 + (arg0 | 3)), (load32(((v4 << 2) + 9147392)) != 0))
                arg0 = (arg0 + 4)
                arg1 = (arg1 + 4)
                if ((arg1 + 4) != v7):
                    continue
                break
        arg1 = (v3 & 3)
        if not (v3 & 3):
            break
        while True:  # $label2
            store8((arg0 + v5), (load32(((arg0 << 2) + 9147392)) != 0))
            arg0 = (arg0 + 1)
            arg2 = (arg2 + 1)
            if ((arg2 + 1) != arg1):
                continue
            break
        break
    arg1 = func26(v3)
    # TODO: memory.fill
    store32(9143008, arg1)
    if (u32(v6) >= u32(2)):
        arg0 = (v6 - 1)
        v12 = ((v6 - 1) & -4)
        v11 = (arg0 & 3)
        v13 = (u32((v6 - 2)) < u32(3))
        arg2 = 1
        while True:  # $label5
            v7 = (arg2 * v6)
            v4 = 0
            arg0 = 1
            if not v13:
                while True:  # $label3
                    store8((arg1 + (arg0 + v7)), (arg0 == arg2))
                    v9 = (arg0 + 1)
                    store8((arg1 + ((arg0 + 1) + v7)), (arg2 == v9))
                    v9 = (arg0 + 2)
                    store8((arg1 + ((arg0 + 2) + v7)), (arg2 == v9))
                    v9 = (arg0 + 3)
                    store8((arg1 + ((arg0 + 3) + v7)), (arg2 == v9))
                    arg0 = (arg0 + 4)
                    v4 = (v4 + 4)
                    if ((v4 + 4) != v12):
                        continue
                    break
            v4 = 0
            if v11:
                while True:  # $label4
                    store8((arg1 + (arg0 + v7)), (arg0 == arg2))
                    arg0 = (arg0 + 1)
                    v4 = (v4 + 1)
                    if ((v4 + 1) != v11):
                        continue
                    break
            arg2 = (arg2 + 1)
            if ((arg2 + 1) != v6):
                continue
            break
    arg0 = func26(v3)
    # TODO: memory.fill
    store32(9143016, arg0)
    arg2 = func26(v3)
    # TODO: memory.fill
    store32(9143012, arg2)
    while True:  # $label6
        if not v3:
            break
        arg1 = 0
        arg0 = 0
        if (u32(v3) >= u32(4)):
            v7 = (v3 & -4)
            v6 = 0
            while True:  # $label7
                store8((arg0 + arg2), (load8u((arg0 + v5)) ^ 1))
                v4 = (arg0 | 1)
                store8((arg2 + (arg0 | 1)), (load8u((v4 + v5)) ^ 1))
                v4 = (arg0 | 2)
                store8((arg2 + (arg0 | 2)), (load8u((v4 + v5)) ^ 1))
                v4 = (arg0 | 3)
                store8((arg2 + (arg0 | 3)), (load8u((v4 + v5)) ^ 1))
                arg0 = (arg0 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v7):
                    continue
                break
        v3 = (v3 & 3)
        if not (v3 & 3):
            break
        while True:  # $label8
            store8((arg0 + arg2), (load8u((arg0 + v5)) ^ 1))
            arg0 = (arg0 + 1)
            arg1 = (arg1 + 1)
            if ((arg1 + 1) != v3):
                continue
            break
        break
    store32(v8, v10)
    store32(v8 + 4, load32(9142428))
    G.global0 = (v8 + 32)
    return v8

# ----------------------------------------------------------
# $ge
# Export: ge
# ----------------------------------------------------------
def ge(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
    """Export: ge"""
    arg5 = players[arg0]
    arg4 = (100 if arg4 else 0)
    store32(players[arg0] + 286688, (100 if arg4 else 0))
    store32(arg5 + 286684, arg4)
    store32(arg5 + 283908, arg0)
    store32(arg5 + 283868, load32(9561460))
    # TODO: memory.copy
    arg0 = load32(GAME_STATE)
    store32((arg5 + 284000), load32(load32(GAME_STATE) + 40))
    arg0 = load32(arg0 + 36)
    store32(arg5 + 283960, 3)
    store32((arg5 + 284136), arg0)
    store8((arg5 + 283974), arg3)
    store8((arg5 + 283973), arg2)
    store8(arg5 + 283972, arg1)
    store32((arg5 + 283860), arg9)
    store32((arg5 + 283856), arg8)
    store32((arg5 + 283852), arg7)
    store32(arg5 + 283848, arg6)
    while True:  # $label0
        if not arg10:
            break
        arg0 = (arg10 & 3)
        if (u32(arg10) >= u32(4)):
            arg1 = (arg10 & -4)
            arg10 = 0
            while True:  # $label1
                store16((arg5 + (v11 << 1)), load32(((v11 << 2) + 9147392)))
                arg2 = (v11 | 1)
                store16((arg5 + ((v11 | 1) << 1)), load32(((arg2 << 2) + 9147392)))
                arg2 = (v11 | 2)
                store16((arg5 + ((v11 | 2) << 1)), load32(((arg2 << 2) + 9147392)))
                arg2 = (v11 | 3)
                store16((arg5 + ((v11 | 3) << 1)), load32(((arg2 << 2) + 9147392)))
                v11 = (v11 + 4)
                arg10 = (arg10 + 4)
                if ((arg10 + 4) != arg1):
                    continue
                break
        if not arg0:
            break
        arg10 = 0
        while True:  # $label2
            store16((arg5 + (v11 << 1)), load32(((v11 << 2) + 9147392)))
            v11 = (v11 + 1)
            arg10 = (arg10 + 1)
            if ((arg10 + 1) != arg0):
                continue
            break
        break

# ----------------------------------------------------------
# $vc
# Export: vc
# ----------------------------------------------------------
def vc():
    """Export: vc"""
    v0 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    func231(v0)
    store32(v0 + 12, 1)
    func186((v0 + 44), v0, 78, 0)
    G.global0 = (v0 + 48)

# ----------------------------------------------------------
# $func476
# ----------------------------------------------------------
def func476(arg0, arg1):
    while True:  # $label0
        v2 = load32(ENTITIES)
        arg1 = entities[arg0]
        if (load8u(entities[arg0].unit_class) == 3):
            break
        if (load8u(arg1 + 129) != 7):
            break
        arg0 = (v2 + (arg0 * 132))
        v2 = load32((v2 + (arg0 * 132)) + 88)
        if not load32((v2 + (arg0 * 132)) + 88):
            break
        v3 = load32(9142440)
        store32(arg0 + 80, 0)
        store32(arg0 + 88, 0)
        store8(arg1 + 129, 0)
        # TODO: i32.div_u
        arg0 = v3
        break

# ----------------------------------------------------------
# $wa
# Export: wa
# ----------------------------------------------------------
def wa(arg0, arg1):
    """Export: wa"""
    v4 = load32(PLAYERS)
    while True:  # $label0
        v5 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v2 = 1
        while True:  # $label1
            if (arg0 == load32((v4 + (v2 * 286704)) + 284616)):
                v3 = v2
                break
            v2 = (v2 + 1)
            if ((v2 + 1) != v5):
                continue
            break
        break
    store32((v4 + (v3 * 286704)) + 284604, arg1)

# ----------------------------------------------------------
# $fd
# Export: fd
# ----------------------------------------------------------
def fd():
    """Export: fd"""
    v0 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v1 = players[load32(CURRENT_PLAYER)]
    store64(v0 + 16, load64(v0 + 32))
    store64(v0 + 24, load64(v0 + 40))
    v2 = load32((v1 + 284000))
    v3 = load32((v1 + 284136))
    v4 = load32(v1 + 283980)
    store32(v0, load32(v1 + 283976))
    v1 = (v3 + v4)
    store32(v0 + 4, (v2 if (u32(v1) > u32(v2)) else (v3 + v4)))
    G.global0 = (v0 + 48)

# ----------------------------------------------------------
# $cd
# Export: cd
# ----------------------------------------------------------
def cd(arg0, arg1):
    """Export: cd"""
    arg1 = ((9684460 if (arg1 == 1) else 9684476) if arg1 else 9684444)
    store32(((9684460 if (arg1 == 1) else 9684476) if arg1 else 9684444) + 8, 0)
    v2 = load32(arg1 + 4)
    if (u32(arg0) >= u32(load32(arg1 + 4))):
        v2 = (load32(arg1 + 12) + (arg0 + v2))
        store32(arg1 + 4, (load32(arg1 + 12) + (arg0 + v2)))
        v3 = load32(arg1)
        v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
        if v3:
        store32(arg1, v2)
    while True:  # $label0
        if not arg0:
            break
        v6 = (arg0 & 1)
        v3 = load32(arg1)
        v2 = 0
        if (arg0 != 1):
            v7 = (arg0 & -2)
            arg0 = 0
            while True:  # $label1
                v4 = (v2 << 2)
                v5 = load32(((v2 << 2) + 9147392))
                v8 = load32(arg1 + 8)
                store32(arg1 + 8, (load32(arg1 + 8) + 1))
                store32((v3 + (v8 << 2)), v5)
                v4 = load32(((v4 | 4) + 9147392))
                v5 = load32(arg1 + 8)
                store32(arg1 + 8, (load32(arg1 + 8) + 1))
                store32((v3 + (v5 << 2)), v4)
                v2 = (v2 + 2)
                arg0 = (arg0 + 2)
                if ((arg0 + 2) != v7):
                    continue
                break
        if not v6:
            break
        arg0 = load32(((v2 << 2) + 9147392))
        arg1 = load32(arg1 + 8)
        store32(arg1 + 8, (load32(arg1 + 8) + 1))
        store32((v3 + (arg1 << 2)), arg0)
        break

# ----------------------------------------------------------
# $_c
# Export: _c
# ----------------------------------------------------------
def _c(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
    """Export: _c"""
    v10 = load32(9568088)
    store32(load32(9568088) + 36, arg6)
    store32(v10 + 32, arg5)
    store32(v10 + 16, arg4)
    store32(v10 + 12, arg3)
    store32(v10 + 8, arg2)
    store32(v10 + 4, arg1)
    store32(v10, arg0)
    store8(v10 + 45, arg8)
    store32(v10 + 28, arg7)
    store8(v10 + 44, arg9)

# ----------------------------------------------------------
# $za
# Export: za
# ----------------------------------------------------------
def za(arg0):
    """Export: za"""
    v2 = load32(PLAYER_COUNT)
    store32(PLAYER_COUNT, arg0)
    v7 = (i32(arg0) * 286704)
    v1 = (-1 if i32(((v7 & 0xFFFFFFFF) >> 32)) else i32((i32(arg0) * 286704)))
    v5 = func26((-1 if i32(((v7 & 0xFFFFFFFF) >> 32)) else i32((i32(arg0) * 286704))))
    # TODO: memory.fill
    v1 = load32(PLAYERS)
    while True:  # $label3
        while True:  # $label1
            v2 = (v2 if (u32(arg0) > u32(v2)) else arg0)
            if (v2 if (u32(arg0) > u32(v2)) else arg0):
                if (u32(v2) >= u32(4)):
                    v6 = (v2 & -4)
                    arg0 = 0
                    while True:  # $label0
                        v4 = (v3 * 286704)
                        # TODO: memory.copy
                        v4 = ((v3 | 1) * 286704)
                        # TODO: memory.copy
                        v4 = ((v3 | 2) * 286704)
                        # TODO: memory.copy
                        v4 = ((v3 | 3) * 286704)
                        # TODO: memory.copy
                        v3 = (v3 + 4)
                        arg0 = (arg0 + 4)
                        if ((arg0 + 4) != v6):
                            continue
                        break
                v2 = (v2 & 3)
                if not (v2 & 3):
                    break
                arg0 = 0
                while True:  # $label2
                    v6 = (v3 * 286704)
                    # TODO: memory.copy
                    v3 = (v3 + 1)
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != v2):
                        continue
                    break
                break
            if not v1:
                break
            break
        break
    store32(PLAYERS, v5)

# ----------------------------------------------------------
# $qd
# Export: qd
# ----------------------------------------------------------
def qd(arg0):
    """Export: qd"""
    v7 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    if load8u(9142916):
        v1 = load32(PLAYER_COUNT)
        v12 = (v1 * 3)
        v2 = func26((-1 if (u32((v1 * 3)) > u32(1073741823)) else (load32(PLAYER_COUNT) * 12)))
        while True:  # $label0
            if not v1:
                break
            v6 = load32(CURRENT_PLAYER)
            v10 = (load32(CURRENT_PLAYER) * v1)
            v11 = load32(9143012)
            v8 = load32(9143004)
            v3 = load32(PLAYERS)
            if not arg0:
                arg0 = 0
                while True:  # $label1
                    v9 = (v2 + (v4 << 2))
                    v5 = (v3 + (arg0 * 286704))
                    store32((v2 + (v4 << 2)), ((load16u((v3 + (arg0 * 286704)) + 283972) | (load8u((v5 + 283974)) << 16)) | -16777216))
                    store32(v9 + 4, load8u((v8 + ((load32(v5 + 283908) * v1) + v6))))
                    store32(v9 + 8, load8u((v11 + (load32(v5 + 283908) + v10))))
                    v4 = (v4 + 3)
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != v1):
                        continue
                    break
                break
            store32(v2, ((load16u(v3 + 283972) | (load8u((v3 + 283974)) << 16)) | -16777216))
            store32(v2 + 4, load8u((v8 + ((load32(v3 + 283908) * v1) + v6))))
            store32(v2 + 8, load8u((v11 + (load32(v3 + 283908) + v10))))
            arg0 = 1
            if (v1 == 1):
                break
            v4 = 3
            while True:  # $label2
                v5 = (v2 + (v4 << 2))
                if (arg0 != v6):
                else:
                store32((-16776961 if load8u((v8 + (v6 + (arg0 * v1)))) else -16711936), -65536)
                v9 = (v3 + (arg0 * 286704))
                store32(v5 + 4, load8u((v8 + ((load32((v3 + (arg0 * 286704)) + 283908) * v1) + v6))))
                store32(v5 + 8, load8u((v11 + (load32(v9 + 283908) + v10))))
                v4 = (v4 + 3)
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v1):
                    continue
                break
            break
        store32(v7 + 4, v12)
        store32(v7, v2)
    G.global0 = (v7 + 16)
    return af(v2)

# ----------------------------------------------------------
# $func488
# ----------------------------------------------------------
def func488(arg0, arg1):
    arg0 = entities[arg0]
    if (load8u(entities[arg0] + 129) == 7):
        store8(arg0 + 129, 0)
    func202(arg0, 0, 0)
    func29(arg0, 1)

# ----------------------------------------------------------
# $func489
# ----------------------------------------------------------
def func489(arg0, arg1, arg2, arg3, arg4):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg4 = 0
    while True:  # $label0
        arg0 = load8u(entities[arg0].sub_state)
        if (load32(((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES) + 212) != 1):
            break
        v5 = load32(arg2)
        v6 = load32(arg3)
        v7 = (load32(9142440) + 2)
        if (u32((load32((load32(9142840) + ((load32(arg2) + (((load32(arg3) + (load32(9142440) + 2)) + 1) * v7)) << 2)) + 4) - 3)) > u32(-3)):
            break
        store32(arg1 + 12, v5)
        store32(arg1 + 8, v6)
        if func167((arg1 + 12), (arg1 + 8), 1, 1, load32(((arg0 * 404) + ENTITY_TYPES) + 216)):
            store32(arg2, load32(arg1 + 12))
            store32(arg3, load32(arg1 + 8))
            break
        arg4 = 1
        break
    G.global0 = (arg1 + 16)
    return arg4

# ----------------------------------------------------------
# $func492
# ----------------------------------------------------------
def func492(arg0, arg1):
    v2 = load32(arg1 + 24)
    if not load32(arg1 + 24):
        v2 = func26(16)
        store64(func26(16), 0)
        store64(v2 + 8, 0)
        store32(arg1 + 24, v2)
    if not load32(v2 + 12):
        v3 = func26(16)
        store32(func26(16) + 4, 16)
        store32(v3, func26(64))
        store64(v3 + 8, 4294967296)
        store32(v2 + 12, v3)
        while True:  # $label1
            while True:  # $label0
                v2 = load32(load32(arg1 + 24) + 12)
                v3 = load32(load32(load32(arg1 + 24) + 12) + 8)
                if (load32(load32(load32(arg1 + 24) + 12) + 8) != load32(v2 + 4)):
                    v4 = load32(v2)
                    break
                v4 = (load32(v2 + 12) + v3)
                store32(v2 + 4, (load32(v2 + 12) + v3))
                v5 = load32(v2)
                v4 = func26((-1 if (u32(v4) > u32(1073741823)) else (v4 << 2)))
                if v3:
                    # TODO: memory.copy
                if v5:
                    v3 = load32(v2 + 8)
                store32(v2, v4)
                break
            store32(v2 + 8, (v3 + 1))
            store32((v4 + (v3 << 2)), 0)
            v6 = (v6 + 1)
            if ((v6 + 1) != 16):
                continue
            break
    arg1 = load32(load32(arg1 + 24) + 12)
    v2 = load32(arg0 + 8)
    if (u32(load32(arg0 + 8)) >= u32(16777216)):
        v2 = load32(((load32(arg1) + (v2 << 2)) - 67108864))
    v3 = load32(arg0 + 36)
    while True:  # $label7
        while True:  # $label6
            while True:  # $label5
                while True:  # $label4
                    while True:  # $label3
                        while True:  # $label2
                            # br_table load32(arg0 + 28)
                            break
                            break
                        store32((load32(arg1) + (v3 << 2)), v2)
                        return
                        break
                    arg0 = (load32(arg1) + (v3 << 2))
                    store32((load32(arg1) + (v3 << 2)), (load32(arg0) + v2))
                    return
                    break
                arg0 = (load32(arg1) + (v3 << 2))
                store32((load32(arg1) + (v3 << 2)), (load32(arg0) - v2))
                return
                break
            arg0 = (load32(arg1) + (v3 << 2))
            store32((load32(arg1) + (v3 << 2)), (load32(arg0) * v2))
            return
            break
        arg0 = (load32(arg1) + (v3 << 2))
        # TODO: i32.div_u
        store32(load32(arg0), v2)
        break

# ----------------------------------------------------------
# $func493
# ----------------------------------------------------------
def func493(arg0, arg1):
    v2 = load32(ENTITIES)
    arg1 = entities[arg0]
    store8(entities[arg0] + 126, 0)
    # TODO: i32.div_u
    store32(load32(arg1 + 52) + 52, ((load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 296) * load32((players[load16u(arg1 + 110)] + 284144))) - 100))
    while True:  # $label0
        if not load32(arg1 + 92):
            break
        if load32(9140316):
            if (load32(9140320) != load32((v2 + (arg0 * 132)) + 28)):
                break
        break

# ----------------------------------------------------------
# $func495
# ----------------------------------------------------------
def func495(arg0, arg1, param2):
    v9 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v4 = load32(ENTITIES)
    while True:  # $label0
        if (u32(load32(9142848)) < u32((load32(load32(GAME_STATE) + 72) * 2400))):
            func29((v4 + (arg0 * 132)), 1)
            break
        while True:  # $label1
            v3 = (arg0 * 132)
            v2 = (v4 + (arg0 * 132))
            if (load8u((v4 + (arg0 * 132)) + 125) == 3):
                break
            if not load8u(v2 + 128):
                break
            v4 = (v4 + (arg0 * 132))
            store8((v4 + (arg0 * 132)) + 127, 0)
            while True:  # $label2
                v5 = load32(v4 + 40)
                if not load32(v4 + 40):
                    break
                if load8u(9142916):
                    store32(v9 + 20, v5)
                    store32(v9 + 16, 0)
                    a_b()
                    break
                v4 = load16u(v4 + 110)
                store32(v9 + 4, v5)
                store32(v9, (v4 + 16))
                a_b()
                break
            store8(v2 + 128, 0)
            v4 = load32(ENTITIES)
            break
        v10 = (v3 + v4)
        v2 = (v4 + (arg1 * 132))
        if (load8u((v4 + (arg1 * 132)) + 125) == 3):
            func29(v10, 1)
            break
        v8 = (v4 + (arg1 * 132))
        v5 = load16u((v4 + (arg1 * 132)) + 112)
        v6 = (v4 + (arg0 * 132))
        if (load8u((v4 + (arg0 * 132)) + 125) == 1):
            v3 = load16u(v6 + 114)
            v2 = load16u(v8 + 114)
            while True:  # $label4
                while True:  # $label3
                    v8 = load16u(v6 + 112)
                    if (v5 != load16u(v6 + 112)):
                        break
                    if (u32(v2) > u32(v3)):
                        break
                    if (u32(v2) < u32(v3)):
                        break
                    v8 = 0
                    break
                    break
                v8 = (1 if (u32(v5) > u32(v8)) else (-1 if (u32(v5) < u32(v8)) else 0))
                break
            v3 = (1 if (u32(v2) > u32(v3)) else (-1 if (u32(v2) < u32(v3)) else 0))
            v7 = 6
            v3 = (((v3 * 3) + v8) + 4)
            if (u32((((v3 * 3) + v8) + 4)) <= u32(8)):
                v7 = load8u((v3 + 10184))
            v3 = (v4 + (arg0 * 132))
            store8((v4 + (arg0 * 132)) + 124, v7)
            if (arg0 != arg1):
            v2 = load32(((load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            while True:  # $label5
                if (load8u(v6 + 125) == 3):
                    break
                v5 = load32(v3 + 44)
                if load32(v3 + 44):
                    v10 = load32(9142848)
                    v2 = load32(9215884)
                    store32((load32(9215884) + (v5 << 4)) + 4, 40)
                    store32((v2 + (load32(v3 + 44) << 4)) + 8, load32((v4 + (arg0 * 132)) + 28))
                    store32((v2 + (load32(v3 + 44) << 4)) + 12, arg1)
                    store32((v2 + (load32(v3 + 44) << 4)), (v10 + 28))
                    break
                store32(v3 + 44, ((Ua(700, 40, load32((v4 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
                break
            store32((v4 + (arg1 * 132)) + 104, arg0)
            break
        v3 = load16u(v8 + 114)
        while True:  # $label8
            while True:  # $label7
                while True:  # $label6
                    v11 = load32(load32(GAME_STATE) + 48)
                    if load32(load32(GAME_STATE) + 48):
                        if not load8u(9147152):
                            break
                    v6 = load32(9142440)
                    break
                    break
                v6 = load32(9142440)
                v7 = load16u((load32(9147376) + (((load32(9142440) * v3) + v5) << 1)))
                if (v11 == 2):
                    if (u32(v7) > u32(1)):
                        break
                    break
                if not v7:
                    break
                break
            func80(i32(v5), i32(v3), load32(9142580), 32.0, i32((v6 * 96)))
            break
        v5 = (G.global0 - 32)
        G.global0 = (G.global0 - 32)
        store8(v2 + 127, 5)
        while True:  # $label9
            if not load8u(9142916):
                break
            v3 = load32(v2 + 40)
            if not load32(v2 + 40):
                break
            store32(v5 + 20, v3)
            store32(v5 + 16, -11842741)
            a_b()
            break
        while True:  # $label10
            v3 = load16u(v2 + 112)
            v6 = ((load16u(v2 + 112) << 5) - load32(9142952))
            v6 = load16u(v2 + 114)
            v7 = ((load16u(v2 + 114) << 5) - load32(9142956))
            if ((((((load16u(v2 + 112) << 5) - load32(9142952)) * v6) + (((load16u(v2 + 114) << 5) - load32(9142956)) * v7)) - 1) > 9000000):
                break
            v11 = load32(39888)
            while True:  # $label11
                v12 = load32(load32(GAME_STATE) + 48)
                if not load32(load32(GAME_STATE) + 48):
                    break
                if load8u(9147152):
                    break
                v7 = load16u((load32(9147376) + (((load32(9142440) * v6) + v3) << 1)))
                if (v12 == 2):
                    if (u32(v7) > u32(1)):
                        break
                    break
                if not v7:
                    break
                break
            store32(v5 + 8, v6)
            store32(v5 + 4, v3)
            store32(v5, v11)
            a_b()
            break
        func119(v5, v2, 0, 1)
        store8(v2 + 125, 10)
        func63(1738, v2, 20, 0, load32((players[load16u(v2 + 110)] + 284220)))
        func77(v2)
        G.global0 = (v5 + 32)
        store32((v4 + (arg1 * 132)) + 104, 0)
        if (arg0 == arg1):
            break
        v2 = load8u((v4 + (arg0 * 132)) + 129)
        if ((load8u((v4 + (arg0 * 132)) + 129) & 254) == 14):
            arg0 = func301(load16u(v8 + 112), load16u(v8 + 114), load16u((v4 + (arg0 * 132)) + 110), (-1 if (v2 != 15) else load8u((v4 + (arg1 * 132)) + 122)))
            if func301(load16u(v8 + 112), load16u(v8 + 114), load16u((v4 + (arg0 * 132)) + 110), (-1 if (v2 != 15) else load8u((v4 + (arg1 * 132)) + 122))):
                break
            func29(v10, 1)
            break
        func29(v10, 1)
        break
    G.global0 = (v9 + 32)
    return (v5 + 16)

# ----------------------------------------------------------
# $func497
# ----------------------------------------------------------
def func497(arg0):
    while True:  # $label0
        v1 = load8u(arg0 + 129)
        if ((load8u(arg0 + 129) & 254) != 14):
            break
        v1 = func301(load16u(arg0 + 112), load16u(arg0 + 114), load16u(arg0 + 110), (-1 if (v1 != 15) else load8u(entities[load32(arg0 + 32)].sub_state)))
        if not func301(load16u(arg0 + 112), load16u(arg0 + 114), load16u(arg0 + 110), (-1 if (v1 != 15) else load8u(entities[load32(arg0 + 32)].sub_state))):
            break
        store32(arg0 + 32, v1)
        break
    return 0

# ----------------------------------------------------------
# $nd
# Export: nd
# ----------------------------------------------------------
def nd(arg0):
    """Export: nd"""
    while True:  # $label0
        if not arg0:
            break
        v1 = load32(9681936)
        if not load32(9681936):
            break
        if load32(v1 + 8):
            arg0 = 0
            while True:  # $label1
                func38(load32((load32(v1) + ((arg0 << 2) | 12))))
                arg0 = (arg0 + 4)
                v1 = load32(9681936)
                if (u32((arg0 + 4)) < u32(load32(load32(9681936) + 8))):
                    continue
                break
        store32(v1 + 8, 0)
        break
    return load32(9147288)

# ----------------------------------------------------------
# $func501
# ----------------------------------------------------------
def func501(arg0):
    while True:  # $label0
        if not arg0:
            break
        v1 = load32(ENTITIES)
        v2 = entities[arg0]
        if load8u((load32(9143004) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(entities[arg0] + 110))))):
            break
        while True:  # $label1
            # br_table (load8u(v2 + 125) - 4)
            break
            break
        while True:  # $label2
            v1 = load8u((v1 + (arg0 * 132)) + 122)
            if (load8u((v1 + (arg0 * 132)) + 122) == load32(38552)):
                break
            if (load32(38892) == v1):
                break
            if (load32(38816) == v1):
                break
            if (load32(38872) == v1):
                break
            if (load32(38584) == v1):
                break
            if (load32(38796) != v1):
                break
            break
        store32((9681808 if load8u(9681824) else 9681812), arg0)
        break

# ----------------------------------------------------------
# $nb
# Export: nb
# ----------------------------------------------------------
def nb(arg0):
    """Export: nb"""
    v1 = entities[load32(9173808)]
    arg0 = load32((players[load16u(entities[load32(9173808)] + 110)] + 284340))
    v2 = (load32(9681804) + ((arg0 * load32((players[load16u(entities[load32(9173808)] + 110)] + 284340))) * ((load8u(9163792) + 1) & 255)))
    store32(9681804, (load32(9681804) + ((arg0 * load32((players[load16u(entities[load32(9173808)] + 110)] + 284340))) * ((load8u(9163792) + 1) & 255))))
    while True:  # $label0
        v1 = load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 124)
        if (u32(load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 124)) >= u32(v2)):
            v1 = arg0
            if (u32(v2) >= u32(arg0)):
                break
        store32(9681804, v1)
        break

# ----------------------------------------------------------
# $ob
# Export: ob
# ----------------------------------------------------------
def ob(arg0, arg1):
    """Export: ob"""
    if arg1:
        arg0 = ((load32(9681816) + arg0) & 3)
        store32(9681816, ((load32(9681816) + arg0) & 3))
        return arg0
    arg0 = ((load32(9681820) + arg0) & 3)
    store32(9681820, ((load32(9681820) + arg0) & 3))
    return arg0

# ----------------------------------------------------------
# $func504
# ----------------------------------------------------------
def func504(arg0):
    while True:  # $label1
        while True:  # $label0
            arg0 = load32(entities[load32(9173808)].z)
            if not load32(entities[load32(9173808)].z):
                break
            if (u32(load32(arg0 + 8)) < u32(3)):
                break
            arg0 = load32(arg0)
            if load32(load32(arg0)):
                break
            store32(9681804, load32(arg0 + 4))
            store32(9681808, load32(arg0 + 8))
            store32(9681812, load32(arg0 + 12))
            store32(9681816, load32(arg0 + 16))
            v1 = load32(arg0 + 20)
            break
            break
        store32(9681804, 50)
        store32(9681808, 0)
        store32(9681812, 0)
        store32(9681816, 0)
        break
    store32(9681820, v1)

# ----------------------------------------------------------
# $func505
# ----------------------------------------------------------
def func505(arg0, arg1, param2):
    v6 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # $label0
        v4 = load32(ENTITIES)
        v8 = entities[arg0]
        v3 = load32(entities[arg0].z)
        if not load32(entities[arg0].z):
            break
        v2 = load32(v3 + 8)
        if (u32(load32(v3 + 8)) < u32(3)):
            break
        v7 = load32(v3)
        if load32(load32(v3)):
            break
        v10 = (v4 + (arg0 * 132))
        v5 = load16u((v4 + (arg0 * 132)) + 88)
        v9 = load32(v7 + 8)
        v15 = (load32(v7 + 8) == arg1)
        v11 = load32((v7 + (16 if (load32(v7 + 8) == arg1) else 20)))
        v12 = load32(PLAYERS)
        v13 = load16u((v4 + (arg1 * 132)) + 110)
        v16 = (load32(PLAYERS) + (load16u((v4 + (arg1 * 132)) + 110) * 286704))
        if (load8u(v10 + 125) == 1):
            while True:  # $label1
                while True:  # $label2
                    if (v2 == 7):
                        store32(v3 + 8, 6)
                        v2 = (v5 << 2)
                        if (load32(((v5 << 2) + (v6 + 16))) == 2147483647):
                            break
                        v3 = (((v12 + (v13 * 286704)) + v2) + 283848)
                        v2 = load16u((v4 + (arg0 * 132)) + 108)
                        break
                    v2 = (v4 + (arg0 * 132))
                    v3 = load16u((v4 + (arg0 * 132)) + 108)
                    if not load16u((v4 + (arg0 * 132)) + 108):
                        break
                    v17 = 0.800000012
                    v2 = (v12 + (load16u(v2 + 110) * 286704))
                    if (load32((((v12 + (load16u(v2 + 110) * 286704)) + (load32(39108) << 2)) + 281808)) != 1):
                        v17 = (0.800000012 if (load32(((v2 + (load32(39168) << 2)) + 281808)) == 1) else 0.75)
                    if (load32(((v6 + 16) + (v5 << 2))) == 2147483647):
                        break
                    while True:  # $label3
                        v2 = (v4 + (v9 * 132))
                        v9 = (v4 + (load32(v7 + 12) * 132))
                        v14 = (load16u((v4 + (v9 * 132)) + 112) - load16u((v4 + (load32(v7 + 12) * 132)) + 112))
                        v2 = (load16u(v2 + 114) - load16u(v9 + 114))
                        # TODO: f64.promote_f32
                        v18 = (((sqrt(i32((((load16u((v4 + (v9 * 132)) + 112) - load16u((v4 + (load32(v7 + 12) * 132)) + 112)) * v14) + ((load16u(v2 + 114) - load16u(v9 + 114)) * v2)))) * (v17 * i32(load32(v7 + 4)))) / 500.0) + 0.5)
                        if (((((sqrt(i32((((load16u((v4 + (v9 * 132)) + 112) - load16u((v4 + (load32(v7 + 12) * 132)) + 112)) * v14) + ((load16u(v2 + 114) - load16u(v9 + 114)) * v2)))) * (v17 * i32(load32(v7 + 4)))) / 500.0) + 0.5) < 4294967296.0) & (v18 >= 0.0)):
                            break
                        break
                    v2 = 0
                    v7 = ((v12 + (v13 * 286704)) + (v5 << 2))
                    v5 = (((v12 + (v13 * 286704)) + (v5 << 2)) + 283848)
                    store32((((v12 + (v13 * 286704)) + (v5 << 2)) + 283848), ((load32(v5) + v3) + v2))
                    v3 = (v7 + 281676)
                    break
                store32(v3, (load32(v3) + v2))
                break
            v2 = (v4 + (arg0 * 132))
            store16((v4 + (arg0 * 132)) + 108, 0)
            store32(v10 + 88, ((load8u((v4 + (arg1 * 132)) + 122) << 16) + v11))
            while True:  # $label4
                if not load32(v2 + 92):
                    break
                if load32(9140316):
                    if (load32(9140320) != load32((v4 + (arg0 * 132)) + 28)):
                        break
                break
            v3 = load32(v8 + 20)
        else:
        if (v2 == 7):
            store32(v3 + 8, 6)
        v2 = (v4 + (arg1 * 132))
        v7 = (v4 + (arg1 * 132))
        while True:  # $label6
            while True:  # $label5
                v2 = load32(v2 + 56)
                if not load32(v2 + 56):
                    break
                v5 = load32(9215884)
                v9 = load32(entities[v2].target_x)
                if (load32((load32(9215884) + (load32(entities[v2].target_x) << 4)) + 12) != arg1):
                    break
                if (load32((v5 + ((v9 << 4) | 4))) == 60):
                    break
                break
            store32(v7 + 56, arg0)
            v2 = arg0
            break
        while True:  # $label7
            v14 = load32(((v6 + 16) + (v11 << 2)))
            v5 = load32(((load32(PLAYERS) + (load16u((v4 + (arg0 * 132)) + 110) * 286704)) + 284344))
            if (u32(load32(((v6 + 16) + (v11 << 2)))) < u32(load32(((load32(PLAYERS) + (load16u((v4 + (arg0 * 132)) + 110) * 286704)) + 284344)))):
                break
            if (arg0 != v2):
                break
            v2 = (v4 + (arg0 * 132))
            v9 = (load16u(v2 + 108) + v5)
            store16((v4 + (arg0 * 132)) + 108, (load16u(v2 + 108) + v5))
            if (v14 != 2147483647):
                store64(v6 + 8, 0)
                store64(v6, 0)
                v3 = (v11 << 2)
                store32((v6 + (v11 << 2)), v5)
                v5 = load32(load32(load32(v8 + 20)) + 4)
                v11 = load16u(v2 + 108)
                if (u32(load32(load32(load32(v8 + 20)) + 4)) <= u32(load16u(v2 + 108))):
                    v3 = (((v12 + (v13 * 286704)) + v3) + 283848)
                    store32((((v12 + (v13 * 286704)) + v3) + 283848), (load32(v3) + (v11 - v5)))
                v9 = load16u(v2 + 108)
            else:
            v3 = load32(load32(v3) + 4)
            if (u32(load32(load32(v3) + 4)) <= u32((v9 & 65535))):
                store16(v2 + 108, v3)
                while True:  # $label8
                    if not load32((v4 + (arg0 * 132)) + 92):
                        break
                    if load32(9140316):
                        if (load32(9140320) != load32((v4 + (arg0 * 132)) + 28)):
                            break
                    break
                store32(v7 + 56, 0)
                store8(v10 + 125, 0)
                break
            if not load32((v4 + (arg0 * 132)) + 92):
                break
            if load32(9140316):
                if (load32(9140320) != load32((v4 + (arg0 * 132)) + 28)):
                    break
            break
        if (load8u(v10 + 125) == 1):
            v2 = (v4 + (arg0 * 132))
            v3 = load32(((load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32):
                if (load8u(v10 + 125) == 3):
                    break
            v8 = load32(v2 + 44)
            if load32(v2 + 44):
                v10 = load32(9142848)
                v3 = load32(9215884)
                store32((load32(9215884) + (v8 << 4)) + 4, 60)
                store32((v3 + (load32(v2 + 44) << 4)) + 8, load32((v4 + (arg0 * 132)) + 28))
                store32((v3 + (load32(v2 + 44) << 4)) + 12, arg1)
                store32((v3 + (load32(v2 + 44) << 4)), (v10 + 40))
                break
            store32(v2 + 44, ((Ua(1000, 60, load32((v4 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
            break
        store32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)), (load32(9142848) + 40))
        break
    G.global0 = (v6 + 32)
    return call_table(v3)

# ----------------------------------------------------------
# $func506
# ----------------------------------------------------------
def func506(arg0):
    v1 = 1
    while True:  # $label0
        v2 = load32(ENTITIES)
        v3 = load32(arg0 + 32)
        v4 = entities[load32(arg0 + 32)]
        v5 = load8u(entities[load32(arg0 + 32)].unit_class)
        if (load8u(entities[load32(arg0 + 32)].unit_class) == 3):
            break
        if load8u((load32(9143004) + (load16u(arg0 + 110) + (load32(PLAYER_COUNT) * load16u(v4 + 110))))):
            break
        while True:  # $label1
            # br_table (v5 - 4)
            break
            break
        while True:  # $label2
            arg0 = load8u((v2 + (v3 * 132)) + 122)
            if (load8u((v2 + (v3 * 132)) + 122) == load32(38552)):
                break
            if (load32(38892) == arg0):
                break
            if (load32(38816) == arg0):
                break
            if (load32(38872) == arg0):
                break
            if (load32(38584) == arg0):
                break
            if (load32(38796) != arg0):
                break
            break
        v1 = 0
        break
    return v1

# ----------------------------------------------------------
# $func508
# ----------------------------------------------------------
def func508(arg0, arg1, arg2):
    if arg2:
        while True:  # $label4
            while True:  # $label0
                arg0 = entities[load32((arg1 + (v5 << 2)))]
                v6 = load8u(entities[load32((arg1 + (v5 << 2)))].sub_state)
                v3 = ((load8u(entities[load32((arg1 + (v5 << 2)))].sub_state) * 404) + ENTITY_TYPES)
                v4 = load8u(9147152)
                if (0 if load8u(9147152) else load8u(((load8u(entities[load32((arg1 + (v5 << 2)))].sub_state) * 404) + ENTITY_TYPES) + 332)):
                    break
                while True:  # $label1
                    if v4:
                        break
                    if (load32(v3 + 264) == 1):
                        if (u32(load32(arg0 + 84)) < u32(load32(v3 + 112))):
                            break
                    v4 = load16u(arg0 + 110)
                    v3 = load32(PLAYERS)
                    while True:  # $label2
                        if not load32(9147132):
                            break
                        if (load32(9142440) != 4096):
                            break
                        if (load32(9671152) != v6):
                            break
                        if (u32(load32((v3 + (v4 * 286704)) + 283976)) > u32(1)):
                            break
                        break
                    v3 = load32(((v3 + (v4 * 286704)) + 278568))
                    if not load32(((v3 + (v4 * 286704)) + 278568)):
                        break
                    while True:  # $label3
                        # br_table (load8u(arg0 + 125) - 4)
                        break
                        break
                    v4 = (v3 + (((v4 * 255) + v6) << 2))
                    store32((v3 + (((v4 * 255) + v6) << 2)), (load32(v4) + 1))
                    break
                break
            v5 = (v5 + 1)
            if ((v5 + 1) != arg2):
                continue
            break

# ----------------------------------------------------------
# $ya
# Export: ya
# ----------------------------------------------------------
def ya(arg0):
    """Export: ya"""
    if load8u(9142388):
        store8(9561848, arg0)
        xa()

# ----------------------------------------------------------
# $ca
# Export: ca
# ----------------------------------------------------------
def ca(arg0):
    """Export: ca"""
    v1 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
    store32(9561732, arg0)
    store32(9561728, v1)
    return v1

# ----------------------------------------------------------
# $func516
# ----------------------------------------------------------
def func516(arg0, arg1):
    v12 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if (load8u(arg1 + 125) == 3):
            break
        while True:  # $label9
            while True:  # $label5
                while True:  # $label6
                    while True:  # $label4
                        while True:  # $label3
                            while True:  # $label2
                                while True:  # $label1
                                    # br_table load32(arg0 + 8)
                                    break
                                    break
                                v5 = load32(arg0 + 20)
                                v6 = load32(arg0 + 28)
                                v4 = load32(arg0 + 24)
                                v8 = load32(arg0 + 40)
                                arg0 = load32(9147324)
                                store32(9147324, load32(9147316))
                                v3 = load32(9147320)
                                v2 = load32(9147312)
                                store32(9147320, load32(9147312))
                                arg0 = (arg0 ^ (arg0 << 11))
                                v2 = ((v2 ^ (((v2 & 0xFFFFFFFF) >> 19) ^ (((arg0 ^ (arg0 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg0)
                                store32(9147316, ((v2 ^ (((v2 & 0xFFFFFFFF) >> 19) ^ (((arg0 ^ (arg0 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg0))
                                arg0 = (v3 ^ (v3 << 11))
                                arg0 = ((((((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ arg0) ^ v2)
                                store32(9147312, ((((((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ arg0) ^ v2))
                                arg0 = (v4 + (arg0 % v8))
                                break
                                break
                            v2 = load32(arg0 + 36)
                            store64(v12 + 8, load64(arg0 + 72))
                            store64(v12, load64(arg0 + 64))
                            v4 = func300(v2, v12, arg1)
                            break
                            break
                        v5 = load32(arg0 + 104)
                        if not load32(arg0 + 104):
                            break
                        v6 = load32(arg0 + 96)
                        v8 = load16u(arg1 + 114)
                        v9 = load16u(arg1 + 112)
                        v11 = load32(ENTITIES)
                        v7 = load32(arg1 + 28)
                        v2 = 2147483647
                        arg0 = 0
                        while True:  # $label7
                            v3 = load32((v6 + (arg0 << 2)))
                            if (v7 != load32((v6 + (arg0 << 2)))):
                                v3 = (v11 + (v3 * 132))
                                v10 = ((load16u((v11 + (v3 * 132)) + 114) - v8) << 1)
                                v10 = ((load16u(v3 + 112) - v9) << 1)
                                v10 = ((((load16u((v11 + (v3 * 132)) + 114) - v8) << 1) * v10) + (((load16u(v3 + 112) - v9) << 1) * v10))
                                v10 = (v2 > v10)
                                v2 = (((((load16u((v11 + (v3 * 132)) + 114) - v8) << 1) * v10) + (((load16u(v3 + 112) - v9) << 1) * v10)) if (v2 > v10) else v2)
                                v4 = (load32(v3 + 28) if v10 else v4)
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v5):
                                continue
                            break
                        break
                        break
                    v5 = load32(9140300)
                    if not load32(9140300):
                        break
                    v6 = load16u(arg1 + 114)
                    v8 = load16u(arg1 + 112)
                    v9 = load32(ENTITIES)
                    v11 = load32(arg1 + 28)
                    v2 = 2147483647
                    arg0 = 0
                    while True:  # $label8
                        v3 = load32(((arg0 << 2) + 8451904))
                        if (v11 != load32(((arg0 << 2) + 8451904))):
                            v3 = (v9 + (v3 * 132))
                            v7 = ((load16u((v9 + (v3 * 132)) + 114) - v6) << 1)
                            v7 = ((load16u(v3 + 112) - v8) << 1)
                            v7 = ((((load16u((v9 + (v3 * 132)) + 114) - v6) << 1) * v7) + (((load16u(v3 + 112) - v8) << 1) * v7))
                            v7 = (v2 > v7)
                            v2 = (((((load16u((v9 + (v3 * 132)) + 114) - v6) << 1) * v7) + (((load16u(v3 + 112) - v8) << 1) * v7)) if (v2 > v7) else v2)
                            v4 = (load32(v3 + 28) if v7 else v4)
                        arg0 = (arg0 + 1)
                        if ((arg0 + 1) != v5):
                            continue
                        break
                    break
                if not v4:
                    break
                v2 = entities[v4]
                arg0 = load16u(entities[v4] + 114)
                break
            v5 = load16u(v2 + 112)
            v8 = ((load8u(arg1 + 122) * 404) + ENTITY_TYPES)
            v9 = load16u(arg1 + 110)
            if func56(load16u(v2 + 112), arg0, ((load8u(arg1 + 122) * 404) + ENTITY_TYPES), load16u(arg1 + 110), 0, 0, 1, 1, 0):
                v2 = v5
                v3 = arg0
                break
            v4 = load32(9142440)
            v2 = 0
            while True:  # $label11
                while True:  # $label10
                    v6 = v2
                    v2 = (v2 << 2)
                    v3 = (load32((((v2 << 2) | 4) + 8611904)) + arg0)
                    if (u32(v4) <= u32((load32((((v2 << 2) | 4) + 8611904)) + arg0))):
                        break
                    v2 = (load32((v2 + 8611904)) + v5)
                    if (u32(v4) <= u32((load32((v2 + 8611904)) + v5))):
                        break
                    if ((v2 | v3) < 0):
                        break
                    if func56(v2, v3, v8, v9, 0, 0, 1, 1, 0):
                        break
                    v4 = load32(9142440)
                    break
                v2 = (v6 + 2)
                if (u32(v6) < u32(5198)):
                    continue
                break
            break
            break
        arg0 = load32(arg1 + 20)
        if load32(arg1 + 20):
            store32(arg0 + 8, 0)
        store32(arg1 + 32, 0)
        store8(arg1 + 129, 0)
        if load32(arg1 + 36):
        while True:  # $label12
            v5 = load8u(arg1 + 125)
            if (load8u(arg1 + 125) == 13):
                break
            if not load8u(59181):
                break
            arg0 = load32(arg1 + 44)
            if not load32(arg1 + 44):
                break
            v6 = load32(9215884)
            if (load32((load32(9215884) + (arg0 << 4)) + 12) == 1):
                break
            if (v5 == 7):
                break
            if load32((v6 + ((arg0 << 4) | 4))):
                break
            arg0 = (load8u(arg1 + 124) << 3)
            break
        arg0 = load32(arg1 + 44)
        if load32(arg1 + 44):
            store32((load32(9215884) + (arg0 << 4)), 0)
        store32(arg1 + 44, 0)
        if (load8u(arg1 + 125) == 13):
            store16(arg1 + 114, v3)
            store16(arg1 + 112, v2)
            break
        v5 = ((load8u(arg1 + 122) * 404) + ENTITY_TYPES)
        if load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 216):
            v4 = load32(9142840)
            v8 = load16u(arg1 + 114)
            v9 = load16u(arg1 + 112)
            v6 = 0
            while True:  # $label14
                v6 = (v6 + 1)
                v11 = ((v6 + 1) + v9)
                arg0 = 0
                while True:  # $label13
                    arg0 = (arg0 + 1)
                    v7 = (load32(9142440) + 2)
                    store32((v4 + ((v11 + ((((arg0 + 1) + v8) + ((load32(9142440) + 2) * load32(v5 + 208))) * v7)) << 2)), load32(v5 + 212))
                    v7 = load32(v5 + 216)
                    if (u32(arg0) < u32(load32(v5 + 216))):
                        continue
                    break
                if (u32(v6) < u32(v7)):
                    continue
                break
        store16(arg1 + 114, v3)
        store16(arg1 + 112, v2)
        if (load8u(arg1 + 125) == 13):
            break
        v5 = ((load8u(arg1 + 122) * 404) + ENTITY_TYPES)
        if load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 216):
            v3 = (v3 & 65535)
            v6 = (v2 & 65535)
            v4 = load32(9142840)
            v2 = 0
            while True:  # $label16
                v2 = (v2 + 1)
                v8 = ((v2 + 1) + v6)
                arg0 = 0
                while True:  # $label15
                    arg0 = (arg0 + 1)
                    v9 = (load32(9142440) + 2)
                    store32((v4 + ((v8 + ((((arg0 + 1) + v3) + ((load32(9142440) + 2) * load32(v5 + 208))) * v9)) << 2)), load32(arg1 + 28))
                    v9 = load32(v5 + 216)
                    if (u32(arg0) < u32(load32(v5 + 216))):
                        continue
                    break
                if (u32(v2) < u32(v9)):
                    continue
                break
        func118(arg1)
        func92(arg1, 0.0, 0.0)
        func29(arg1, 1)
        break
    G.global0 = (v12 + 16)
    return func60(arg1, 1.0)

# ----------------------------------------------------------
# $func517
# ----------------------------------------------------------
def func517(arg0, arg1, param2):
    v13 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v4 = load32(ENTITIES)
    v14 = entities[arg1]
    while True:  # $label3
        v5 = (v4 + (arg0 * 132))
        v3 = load8u((v4 + (arg0 * 132)) + 125)
        if (load8u((v4 + (arg0 * 132)) + 125) == 1):
            v2 = ((load8u(v14 + 122) * 404) + ENTITY_TYPES)
            v8 = load32(((load8u(v14 + 122) * 404) + ENTITY_TYPES) + 220)
            v10 = load16u(v14 + 114)
            v15 = (load32(((load8u(v14 + 122) * 404) + ENTITY_TYPES) + 220) + load16u(v14 + 114))
            v3 = load32(v2 + 216)
            v12 = load16u(v14 + 112)
            v6 = (load32(v2 + 216) + load16u(v14 + 112))
            v9 = load16u(v5 + 114)
            while True:  # $label1
                while True:  # $label0
                    v7 = load16u(v5 + 112)
                    v2 = (u32(load16u(v5 + 112)) < u32(v12))
                    if (u32(load16u(v5 + 112)) < u32(v12)):
                        break
                    if (v6 <= v7):
                        break
                    if (u32(v9) < u32(v10)):
                        break
                    if (v9 >= v15):
                        break
                    v2 = ((v8 // 2) + v10)
                    v8 = (-1 if (v2 < v9) else (((v8 // 2) + v10) != v9))
                    v2 = ((v3 // 2) + v12)
                    break
                    break
                v8 = (1 if (u32(v9) < u32(v10)) else (-1 if (v9 >= v15) else 0))
                break
            v7 = (1 if v2 else (-1 if (v6 <= v7) else 0))
            v3 = 6
            v2 = (((v8 * 3) + v7) + 4)
            if (u32((((v8 * 3) + v7) + 4)) <= u32(8)):
                v3 = load8u((v2 + 10184))
            v2 = (v4 + (arg0 * 132))
            store8((v4 + (arg0 * 132)) + 124, v3)
            while True:  # $label2
                v2 = ((load8u(v2 + 122) * 72) + 9263856)
                if load32(((load8u(v2 + 122) * 72) + 9263856) + 12):
                    break
                break
            v6 = (v4 + (arg0 * 132))
            v2 = load32(((load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32):
            if (load8u(v5 + 125) == 3):
                break
            v3 = load32(v6 + 44)
            if load32(v6 + 44):
                v2 = load32(9142848)
                v8 = load32(9215884)
                store32((load32(9215884) + (v3 << 4)) + 4, 46)
                store32((v8 + (load32(v6 + 44) << 4)) + 8, load32((v4 + (arg0 * 132)) + 28))
                store32((v8 + (load32(v6 + 44) << 4)) + 12, arg1)
                store32((v8 + (load32(v6 + 44) << 4)), (v2 + 1))
                break
            store32(v6 + 44, ((Ua(25, 46, load32((v4 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
            break
        while True:  # $label4
            if (load8u(v14 + 125) != 3):
                v15 = (v4 + (arg1 * 132))
                v11 = (v4 + (arg0 * 132))
                if (u32(load32((v4 + (arg1 * 132)) + 84)) < u32(load32((v4 + (arg0 * 132)) + 84))):
                    break
            v2 = (v4 + (arg0 * 132))
            if load32((v4 + (arg0 * 132)) + 96):
                break
            arg0 = (v4 + (arg1 * 132))
            arg0 = func208(load16u((v4 + (arg1 * 132)) + 112), load16u(arg0 + 114), load16u(v2 + 110), load32(v2 + 84))
            if func208(load16u((v4 + (arg1 * 132)) + 112), load16u(arg0 + 114), load16u(v2 + 110), load32(v2 + 84)):
                break
            func29(v5, 1)
            break
            break
        v6 = load32(v11 + 96)
        if not load32(v11 + 96):
            v10 = load32(PLAYERS)
            v7 = load16u(v11 + 110)
            v12 = load32((players[load16u(v11 + 110)] + 284304))
            if (v3 == 8):
                store8(v5 + 125, 1)
                v3 = 1
            v9 = (v4 + (arg0 * 132))
            v8 = load32((v4 + (arg0 * 132)) + 72)
            if (u32(v12) > u32(load32((v4 + (arg0 * 132)) + 72))):
                v2 = load32(((load8u(v9 + 122) * 72) + 9263856))
                if (load32(((load8u(v9 + 122) * 72) + 9263856)) != load32(v9 + 48)):
                    v7 = load16u(v11 + 110)
                    v10 = load32(PLAYERS)
                    v3 = load8u(v5 + 125)
                v2 = load32(((v10 + (v7 * 286704)) + 284156))
                if (v3 == 1):
                    func63(func37(v5, v2, 0.0, 0), v5, 46, arg1, v2)
                    break
                # TODO: i32.div_u
                store32(load32(9142848), (v2 + 25))
                break
            v3 = (v4 + (arg1 * 132))
            v2 = (load16u(v9 + 112) - load16u((v4 + (arg1 * 132)) + 112))
            v2 = (load16u(v9 + 114) - load16u(v3 + 114))
            v3 = (v10 + (v7 * 286704))
            v2 = load32(((v10 + (v7 * 286704)) + 284096))
            if (((((load16u(v9 + 112) - load16u((v4 + (arg1 * 132)) + 112)) * v2) + ((load16u(v9 + 114) - load16u(v3 + 114)) * v2)) - 1) > (load32(((v10 + (v7 * 286704)) + 284096)) * v2)):
                func117(v5, arg1, 46)
                break
            store32(v9 + 72, (v8 - v12))
            v2 = (v3 + 281668)
            store32((v3 + 281668), (load32(v2) + v12))
        while True:  # $label5
            arg0 = ((load8u((v4 + (arg0 * 132)) + 122) * 72) + 9263856)
            if load32(((load8u((v4 + (arg0 * 132)) + 122) * 72) + 9263856) + 12):
                arg0 = (v4 + (arg1 * 132))
                break
            break
        while True:  # $label13
            while True:  # $label11
                while True:  # $label12
                    v2 = load32(v11 + 84)
                    if (u32(load32(v11 + 84)) > u32(load32(v15 + 84))):
                        v8 = (v4 + (arg1 * 132))
                        v7 = load16u((v4 + (arg1 * 132)) + 114)
                        v6 = load16u(v8 + 112)
                        while True:  # $label8
                            while True:  # $label7
                                while True:  # $label6
                                    arg0 = load32(load32(GAME_STATE) + 48)
                                    if load32(load32(GAME_STATE) + 48):
                                        if not load8u(9147152):
                                            break
                                    v3 = load32(9142440)
                                    break
                                    break
                                v3 = load32(9142440)
                                v2 = load16u((load32(9147376) + (((load32(9142440) * v7) + v6) << 1)))
                                if (arg0 == 2):
                                    if (u32(v2) > u32(1)):
                                        break
                                    break
                                if not v2:
                                    break
                                break
                            func80(i32(v6), i32((v7 - 1)), load32(9142584), 32.0, i32((v3 * 96)))
                            v7 = load16u(v8 + 114)
                            v6 = load16u(v8 + 112)
                            break
                        while True:  # $label9
                            arg0 = ((v6 << 5) - load32(9142952))
                            arg0 = ((v7 << 5) - load32(9142956))
                            if ((((((v6 << 5) - load32(9142952)) * arg0) + (((v7 << 5) - load32(9142956)) * arg0)) - 1) > 9000000):
                                break
                            v2 = load32(39892)
                            while True:  # $label10
                                arg0 = load32(load32(GAME_STATE) + 48)
                                if not load32(load32(GAME_STATE) + 48):
                                    break
                                if load8u(9147152):
                                    break
                                v3 = load16u((load32(9147376) + (((load32(9142440) * v7) + v6) << 1)))
                                if (arg0 == 2):
                                    if (u32(v3) > u32(1)):
                                        break
                                    break
                                if not v3:
                                    break
                                break
                            store32(v13 + 8, v7)
                            store32(v13 + 4, v6)
                            store32(v13, v2)
                            a_b()
                            break
                        v2 = (v4 + (arg1 * 132))
                        arg0 = (load32(v2 + 80) + 100)
                        store32((v4 + (arg1 * 132)) + 80, (load32(v2 + 80) + 100))
                        arg0 = load32((players[load16u(v2 + 110)] + 284008))
                        # TODO: i32.div_u
                        if (u32((load32(v15 + 84) * 100)) >= u32((1 if (u32(arg0) <= u32(1)) else load32((players[load16u(v2 + 110)] + 284008))))):
                            func198(v14)
                        if load32(v11 + 96):
                            break
                        func291(v5, 46, arg1, 1400)
                        break
                    if v6:
                        store8(v5 + 125, 0)
                    if load32(v11 + 96):
                        break
                    arg0 = (v4 + (arg1 * 132))
                    func117(v5, func208(load16u((v4 + (arg1 * 132)) + 112), load16u(arg0 + 114), load16u(v11 + 110), v2), 46)
                    break
                if not load32(v11 + 96):
                    break
                break
            func29(v5, 1)
            break
        if not load32((v4 + (arg1 * 132)) + 92):
            break
        if load32(9140316):
            if (load32(9140320) != load32((v4 + (arg1 * 132)) + 28)):
                break
        break
    G.global0 = (v13 + 16)
    return func28(1, 1)

# ----------------------------------------------------------
# $func518
# ----------------------------------------------------------
def func518(arg0, arg1, arg2, arg3, arg4):
    while True:  # $label0
        arg2 = load32(ENTITIES)
        arg1 = load32(arg1)
        arg3 = (not load32(((load8u(entities[load32(arg1)].sub_state) * 404) + ENTITY_TYPES) + 304) & arg4)
        if not (not load32(((load8u(entities[load32(arg1)].sub_state) * 404) + ENTITY_TYPES) + 304) & arg4):
            break
        arg0 = load32((arg2 + (arg0 * 132)) + 44)
        if not load32((arg2 + (arg0 * 132)) + 44):
            break
        arg2 = load32(9215884)
        if (load32((load32(9215884) + (arg0 << 4)) + 4) != 46):
            break
        store32((arg2 + ((arg0 << 4) | 12)), arg1)
        break
    return arg3

# ----------------------------------------------------------
# $func519
# ----------------------------------------------------------
def func519(arg0):
    while True:  # $label1
        while True:  # $label0
            v2 = load32(ENTITIES)
            v3 = load32(arg0 + 32)
            v4 = entities[load32(arg0 + 32)]
            if (load8u(entities[load32(arg0 + 32)].unit_class) == 3):
                v1 = load32(arg0 + 84)
                break
            v1 = load32(arg0 + 84)
            if (u32(load32(arg0 + 84)) > u32(load32(v4 + 84))):
                break
            break
        v2 = (v2 + (v3 * 132))
        v1 = func208(load16u((v2 + (v3 * 132)) + 112), load16u(v2 + 114), load16u(arg0 + 110), v1)
        if not func208(load16u((v2 + (v3 * 132)) + 112), load16u(v2 + 114), load16u(arg0 + 110), v1):
            return 1
        store32(arg0 + 32, v1)
        break
    return 0

# ----------------------------------------------------------
# $func521
# ----------------------------------------------------------
def func521(arg0, arg1):
    v6 = load32(ENTITIES)
    v4 = entities[arg0]
    if (load8u(entities[arg0].unit_class) != 3):
        v7 = load16u(v4 + 110)
        v8 = load32(PLAYERS)
        while True:  # $label0
            arg1 = load32(v4 + 20)
            if not load32(v4 + 20):
                arg1 = func26(16)
                store32(func26(16) + 4, 17)
                v2 = func26(68)
                store32(arg1 + 12, 1)
                store32(arg1, v2)
                store32(v4 + 20, arg1)
                # TODO: memory.fill
                store32(arg1 + 8, 17)
                break
            v2 = load32(arg1 + 4)
            if (u32(load32(arg1 + 4)) > u32(16)):
                break
            v3 = load32(arg1 + 8)
            if (u32(v2) <= u32((load32(arg1 + 8) + 17))):
                v5 = ((v2 + load32(arg1 + 12)) + 17)
                store32(arg1 + 4, ((v2 + load32(arg1 + 12)) + 17))
                v2 = load32(arg1)
                v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                if v3:
                    # TODO: memory.copy
                if v2:
                store32(arg1, v5)
                arg1 = load32(v4 + 20)
            # TODO: memory.fill
            break
        while True:  # $label1
            v5 = (v8 + (v7 * 286704))
            if (load32((((v8 + (v7 * 286704)) + (load32(39128) << 2)) + 281808)) != 1):
                break
            arg1 = load32(arg1)
            v9 = load64(load32(arg1) + 16)
            store64(arg1 + 12, load64(arg1 + 8))
            v2 = load32(arg1 + 24)
            store64(arg1 + 20, v9)
            store64(arg1 + 4, load64(arg1))
            store32(arg1 + 28, v2)
            v9 = load64(9147316)
            v2 = load32(9147312)
            store32(9147316, load32(9147312))
            v3 = load32(9147324)
            store64(9147320, v9)
            v3 = (v3 ^ (v3 << 11))
            v2 = ((v2 ^ (((v2 & 0xFFFFFFFF) >> 19) ^ (((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8))) ^ v3)
            store32(9147312, ((v2 ^ (((v2 & 0xFFFFFFFF) >> 19) ^ (((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8))) ^ v3))
            store32(arg1, (load32((((v2 % 19) << 2) + 9682096)) + 1))
            if (load32(9671124) != 95):
                break
            if (load32(9173808) != load32((v6 + (arg0 * 132)) + 28)):
                break
            break
        while True:  # $label2
            if (load32(((v5 + (load32(39132) << 2)) + 281808)) != 1):
                break
            arg1 = load32(load32(v4 + 20))
            v9 = load64(load32(load32(v4 + 20)) + 40)
            store64(arg1 + 36, load64(arg1 + 32))
            v10 = load64(arg1 + 48)
            store64(arg1 + 44, v9)
            v2 = load32(arg1 + 56)
            store64(arg1 + 52, v10)
            store32(arg1 + 60, v2)
            v9 = load64(9147316)
            v2 = load32(9147312)
            store32(9147316, load32(9147312))
            v3 = load32(9147324)
            store64(9147320, v9)
            v3 = (v3 ^ (v3 << 11))
            v2 = ((v2 ^ (((v2 & 0xFFFFFFFF) >> 19) ^ (((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8))) ^ v3)
            store32(9147312, ((v2 ^ (((v2 & 0xFFFFFFFF) >> 19) ^ (((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8))) ^ v3))
            store32(arg1 + 32, (load32((((v2 % 19) << 2) + 9682096)) + 1))
            if (load32(9671124) != 96):
                break
            if (load32(9173808) != load32((v6 + (arg0 * 132)) + 28)):
                break
            break
        arg1 = load32((players[load16u(v4 + 110)] + 284236))

# ----------------------------------------------------------
# $func522
# ----------------------------------------------------------
def func522(arg0, arg1):
    while True:  # $label0
        if not arg0:
            break
        arg0 = load32(9213808)
        if not load32(9213808):
            break
        if not load8u(9163792):
            break
        arg1 = load32(9140316)
        store32(9140316, (load32(9140316) + 1))
        arg0 = entities[load32((((arg1 % arg0) << 2) + 9173808))]
        while True:  # $label1
            arg1 = load32(9140320)
            if not load32(9140320):
                break
            v2 = load32(ENTITIES)
            v3 = load32(entities[arg1].flags)
            if not load32(entities[arg1].flags):
                break
            break
        arg0 = load32(arg0 + 28)
        store32(9140320, load32(arg0 + 28))
        break

# ----------------------------------------------------------
# $tb
# Export: tb
# ----------------------------------------------------------
def tb(arg0):
    """Export: tb"""
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # $label10
        arg0 = load32(9681844)
        if not load32(9681844):
            arg0 = 0
            while True:  # $label0
                v3 = ((arg0 * 404) + ENTITY_TYPES)
                v1 = (load32(((arg0 * 404) + ENTITY_TYPES) + 236) + 10)
                v3 = load32(v3 + 180)
                if load32(v3 + 180):
                    v1 = (load32(v3 + 68) + v1)
                else:
                v7 = (0 + (v1 + v2))
                v2 = (arg0 | 1)
                if ((arg0 | 1) != 255):
                    v2 = ((v2 * 404) + ENTITY_TYPES)
                    v1 = (load32(((v2 * 404) + ENTITY_TYPES) + 236) + 10)
                    arg0 = (arg0 + 2)
                    v2 = load32(v2 + 180)
                    if load32(v2 + 180):
                        v1 = (load32(v2 + 68) + v1)
                    else:
                    v2 = (0 + (v1 + v7))
                    continue
                break
            arg0 = 0
            store32(9681848, v7)
            v4 = func26((-1 if (u32(v7) > u32(1073741823)) else (v7 << 2)))
            store32(9681844, func26((-1 if (u32(v7) > u32(1073741823)) else (v7 << 2))))
            while True:  # $label9
                v2 = ((v8 * 404) + ENTITY_TYPES)
                v3 = load32(((v8 * 404) + ENTITY_TYPES) + 180)
                v1 = (v4 + (arg0 << 2))
                store32((v4 + (arg0 << 2)), v8)
                store32(v1 + 4, (load32(v2 + 144) * -48))
                store32(v1 + 8, load32(v2 + 84))
                store32(v1 + 12, load32(v2 + 196))
                store32(v1 + 16, load32(v2 + 264))
                v6 = (arg0 + 5)
                while True:  # $label1
                    if not v3:
                        store32((v4 + (v6 << 2)), 0)
                        break
                    store32((v4 + (v6 << 2)), load32(v3 + 8))
                    break
                store32(0 + 24, load32(v3 + 12))
                v1 = load32(v2 + 236)
                store32(v1 + 28, load32(v2 + 236))
                arg0 = (arg0 + 8)
                while True:  # $label2
                    if not v1:
                        break
                    v10 = (v1 & 3)
                    v2 = load32(v2 + 232)
                    v11 = 0
                    while True:  # $label3
                        if (u32(v1) < u32(4)):
                            v1 = 0
                            break
                        v13 = (v1 & -4)
                        v1 = 0
                        v12 = 0
                        while True:  # $label4
                            v6 = (v4 + (arg0 << 2))
                            v9 = (v1 << 2)
                            store32((v4 + (arg0 << 2)), load32((v2 + (v1 << 2))))
                            store32(v6 + 4, load32((v2 + (v9 | 4))))
                            store32(v6 + 8, load32((v2 + (v9 | 8))))
                            store32(v6 + 12, load32((v2 + (v9 | 12))))
                            v1 = (v1 + 4)
                            arg0 = (arg0 + 4)
                            v12 = (v12 + 4)
                            if ((v12 + 4) != v13):
                                continue
                            break
                        break
                    if not v10:
                        break
                    while True:  # $label5
                        store32((v4 + (arg0 << 2)), load32((v2 + (v1 << 2))))
                        v1 = (v1 + 1)
                        arg0 = (arg0 + 1)
                        v11 = (v11 + 1)
                        if ((v11 + 1) != v10):
                            continue
                        break
                    break
                while True:  # $label6
                    if not v3:
                        store64((v4 + (arg0 << 2)), 0)
                        arg0 = (arg0 + 2)
                        break
                    store32((v4 + (arg0 << 2)), load32(v3 + 68))
                    v2 = (arg0 + 1)
                    v1 = 0
                    if load32(v3 + 68):
                        while True:  # $label7
                            arg0 = v2
                            store32((v4 + (v2 << 2)), load32((v3 + (v1 << 2)) + 28))
                            v2 = (arg0 + 1)
                            v1 = (v1 + 1)
                            if (u32((v1 + 1)) < u32(load32(v3 + 68))):
                                continue
                            break
                    store32((v4 + (v2 << 2)), load32(v3 + 112))
                    arg0 = (arg0 + 2)
                    v1 = 0
                    if not load32(v3 + 112):
                        break
                    while True:  # $label8
                        store32((v4 + (arg0 << 2)), load32((v3 + (v1 << 2)) + 72))
                        arg0 = (arg0 + 1)
                        v1 = (v1 + 1)
                        if (u32((v1 + 1)) < u32(load32(v3 + 112))):
                            continue
                        break
                    break
                v8 = (v8 + 1)
                if ((v8 + 1) != 255):
                    continue
                break
            arg0 = load32(players[load32(CURRENT_PLAYER)] + 283960)
            store32(v5, v4)
            store32(v5 + 4, v7)
            store32(v5 + 8, arg0)
            a_b()
            break
        v2 = load32(players[load32(CURRENT_PLAYER)] + 283960)
        store32(v5 + 16, arg0)
        store32(v5 + 20, load32(9681848))
        store32(v5 + 24, v2)
        a_b()
        break
    G.global0 = (v5 + 32)
    return (v5 + 16)

# ----------------------------------------------------------
# $func526
# ----------------------------------------------------------
def func526(arg0, arg1):
    if not arg0:
        arg0 = load32(9213808)
        if load8u(9147210):
            func41(10, 9173808, arg0, 0, 0)
            return
        v2 = (arg0 << 2)
        arg1 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy

# ----------------------------------------------------------
# $lb
# Export: lb
# ----------------------------------------------------------
def lb():
    """Export: lb"""
    v0 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store32(v0, load32(9681804))
    store32(v0 + 4, load32(9681808))
    store32(v0 + 8, load32(9681812))
    store32(v0 + 12, load32(9681816))
    store32(v0 + 16, load32(9681820))
    v1 = load32(9213808)
    while True:  # $label0
        if load8u(9147210):
            func41(33, 9173808, v1, v0, 5)
            break
        v3 = (v1 << 2)
        v2 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
        if v1:
            # TODO: memory.copy
        break
    G.global0 = (v0 + 32)

# ----------------------------------------------------------
# $func531
# ----------------------------------------------------------
def func531(arg0, arg1, arg2):
    if arg2:
        v3 = load32(ENTITIES)
        arg0 = 0
        while True:  # $label0
            v4 = (v3 + (load32((arg1 + (arg0 << 2))) * 132))
            if (load8u((v3 + (load32((arg1 + (arg0 << 2))) * 132)) + 125) != 3):
                func304(v4)
                v3 = load32(ENTITIES)
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break

# ----------------------------------------------------------
# $func533
# ----------------------------------------------------------
def func533(arg0, arg1):
    v2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v3 = load32(ENTITIES)
    v4 = entities[arg1]
    while True:  # $label0
        v6 = (v3 + (arg0 * 132))
        if (load8u((v3 + (arg0 * 132)) + 125) == 3):
            break
        if not load8u(v6 + 128):
            break
        v5 = (v3 + (arg0 * 132))
        store8((v3 + (arg0 * 132)) + 127, 0)
        while True:  # $label1
            v7 = load32(v5 + 40)
            if not load32(v5 + 40):
                break
            if load8u(9142916):
                store32(v2 + 20, v7)
                store32(v2 + 16, 0)
                a_b()
                break
            v5 = load16u(v5 + 110)
            store32(v2 + 4, v7)
            store32(v2, (v5 + 16))
            a_b()
            break
        store8(v6 + 128, 0)
        break
    while True:  # $label2
        if (load32(38528) != load8u(v4 + 122)):
            break
        if (u32(load32(9142848)) < u32((load32(load32(GAME_STATE) + 72) * 2400))):
            break
        func78(v4, load16u((v3 + (arg0 * 132)) + 110), 0, 0)
        if not load32((v3 + (arg1 * 132)) + 92):
            break
        v4 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32((v3 + (arg1 * 132)) + 28)):
                break
        break
    func29((v3 + (arg0 * 132)), 1)
    G.global0 = (v2 + 32)

# ----------------------------------------------------------
# $_b
# Export: _b
# ----------------------------------------------------------
def _b():
    """Export: _b"""
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store16(9147213, 1)
    store8(9147124, 1)
    v0 = load32(9142848)
    store32(59160, load32(9142848))
    while True:  # $label0
        if load8u(9147152):
            break
        while True:  # $label1
            if not load8u(9147212):
                break
            if load32(9147132):
                break
            # TODO: i32.div_u
            store32(v0, 10)
            break
        func52((207 if load8u(9143020) else 0), 0)
        a_b()
        while True:  # $label2
            if not load8u(9147210):
                break
            if not load8u(9142388):
                break
            if not load8u(9147125):
                break
            func344()
            break
        if not load32(9147132):
            while True:  # $label3
                v3 = load32(PLAYERS)
                v5 = load32(CURRENT_PLAYER)
                v1 = players[load32(CURRENT_PLAYER)]
                v0 = load32(players[load32(CURRENT_PLAYER)] + 283896)
                if load32(players[load32(CURRENT_PLAYER)] + 283896):
                    break
                v0 = 0
                if load32(v1 + 283900):
                    break
                v4 = (v1 + 283896)
                v6 = (v1 + 283900)
                v7 = (v3 + (v5 * 286704))
                v1 = 0
                while True:  # $label6
                    while True:  # $label4
                        v0 = load32(((v7 + (v1 << 2)) + 284636))
                        if not load32(((v7 + (v1 << 2)) + 284636)):
                            break
                        v8 = load32(v0 + 8)
                        if not load32(v0 + 8):
                            break
                        v9 = load32(v0)
                        v0 = 0
                        while True:  # $label5
                            v10 = load32((v9 + (v0 << 2)))
                            if not load32((v9 + (v0 << 2))):
                                v0 = (v0 + 1)
                                if (v8 != (v0 + 1)):
                                    continue
                                break
                            break
                        v1 = entities[v10]
                        v4 = ((load8u(entities[v10].sub_state) * 404) + ENTITY_TYPES)
                        v0 = (((load32(((load8u(entities[v10].sub_state) * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1) + load16u(v1 + 112))
                        store32(v4, (((load32(((load8u(entities[v10].sub_state) * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1) + load16u(v1 + 112)))
                        store32(v6, (load16u(v1 + 114) + ((load32(v4 + 220) & 0xFFFFFFFF) >> 1)))
                        break
                        break
                    v1 = (v1 + 1)
                    if ((v1 + 1) != 255):
                        continue
                    break
                v0 = 0
                break
            while True:  # $label7
                if load8u(9142917):
                    break
                v1 = (v3 + (v5 * 286704))
                v3 = load32((v3 + (v5 * 286704)) + 283900)
                store32(v2, (v0 << 5))
                store32(v2 + 4, (v3 << 5))
                v0 = load32(v1 + 284624)
                if not load32(v1 + 284624):
                    break
                if load8u(9142917):
                    break
                func44(entities[v0], 0)
                break
            la()
            break
        store32(CURRENT_PLAYER, 0)
        break
    G.global0 = (v2 + 16)

# ----------------------------------------------------------
# $func540
# ----------------------------------------------------------
def func540(arg0, arg1, arg2):
    if arg2:
        v6 = load32(9215884)
        v7 = load32(ENTITIES)
        while True:  # $label3
            v4 = 12
            while True:  # $label2
                while True:  # $label1
                    while True:  # $label0
                        arg0 = (v7 + (load32((arg1 + (v3 << 2))) * 132))
                        # br_table load32((v6 + (load32((v7 + (load32((arg1 + (v3 << 2))) * 132)) + 44) << 4)) + 4)
                        break
                        break
                    store8(arg0 + 123, 0)
                    store32(arg0 + 32, 0)
                    store32(arg0 + 116, load32(arg0 + 112))
                    v4 = 6
                    v5 = load32(arg0 + 20)
                    if not load32(arg0 + 20):
                        break
                    if (u32(load32(v5 + 8)) < u32(3)):
                        break
                    if (u32((load32(load32(v5)) - 1)) > u32(1)):
                        break
                    store32(v5 + 8, 0)
                    break
                    break
                func29(arg0, 1)
                v6 = load32(9215884)
                v7 = load32(ENTITIES)
                v4 = 6
                break
            store8(arg0 + 129, v4)
            v3 = (v3 + 1)
            if ((v3 + 1) != arg2):
                continue
            break

# ----------------------------------------------------------
# $ma
# Export: ma
# ----------------------------------------------------------
def ma(arg0, arg1, arg2, arg3, arg4):
    """Export: ma"""
    store8(9561804, (arg3 != 0))
    store8(9561803, (arg2 != 0))
    store8(9561802, (arg1 != 0))
    store8(9561800, (arg0 != 0))
    store8(9561801, (arg4 != 0))

# ----------------------------------------------------------
# $ne
# Export: ne
# ----------------------------------------------------------
def ne(arg0):
    """Export: ne"""
    v1 = load32(9681976)
    if load32(9681976):
        store32(9681976, 0)
    v1 = func26(524288000)
    # TODO: memory.fill
    store32(9687220, v1)
    store32(9681976, v1)
    store32(9687228, 4)
    store32(9687224, ((arg0 * 60) + 16))
    store32(v1, arg0)

# ----------------------------------------------------------
# $qe
# Export: qe
# ----------------------------------------------------------
def qe(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
    """Export: qe"""
    if (u32(arg9) <= u32(254)):
        v20 = (not load32(((arg9 * 404) + ENTITY_TYPES) + 264) & (u32(arg11) > u32(1)))
    v22 = (arg6 * arg7)
    # TODO: i32.div_u
    v19 = (arg6 * arg7)
    v17 = load32(9687232)
    while True:  # $label4
        if (arg11 == 1):
            while True:  # $label3
                while True:  # $label2
                    while True:  # $label0
                        while True:  # $label1
                            # br_table (arg10 - 6)
                            break
                            break
                        v16 = (arg1 * arg2)
                        break
                        break
                    v16 = (arg1 * arg2)
                    if not (arg1 * arg2):
                        break
                    arg2 = 0
                    if (u32(v16) >= u32(4)):
                        v18 = (v16 & -4)
                        arg12 = 0
                        while True:  # $label5
                            v13 = (arg2 << 2)
                            v14 = (v17 + (arg2 << 2))
                            if (load32((v17 + (arg2 << 2))) == -16712192):
                                store32(v14, 0)
                            v14 = (v17 + (v13 | 4))
                            if (load32((v17 + (v13 | 4))) == -16712192):
                                store32(v14, 0)
                            v14 = (v17 + (v13 | 8))
                            if (load32((v17 + (v13 | 8))) == -16712192):
                                store32(v14, 0)
                            v13 = (v17 + (v13 | 12))
                            if (load32((v17 + (v13 | 12))) == -16712192):
                                store32(v13, 0)
                            arg2 = (arg2 + 4)
                            arg12 = (arg12 + 4)
                            if ((arg12 + 4) != v18):
                                continue
                            break
                    arg12 = (v16 & 3)
                    if not (v16 & 3):
                        break
                    while True:  # $label6
                        v13 = (v17 + (arg2 << 2))
                        if (load32((v17 + (arg2 << 2))) == -16712192):
                            store32(v13, 0)
                        arg2 = (arg2 + 1)
                        v15 = (v15 + 1)
                        if ((v15 + 1) != arg12):
                            continue
                        break
                    break
                    break
                v16 = (arg1 * arg2)
                if not (arg1 * arg2):
                    break
                arg2 = 0
                while True:  # $label8
                    while True:  # $label7
                        v15 = (arg2 << 2)
                        arg12 = (v17 + (arg2 << 2))
                        v13 = load8u((v17 + (arg2 << 2)))
                        if (load8u((v17 + (arg2 << 2))) == load8u(arg12 + 1)):
                            if (v13 == load8u((v17 + (v15 | 2)))):
                                break
                        store32(arg12, 0)
                        break
                    arg2 = (arg2 + 1)
                    if ((arg2 + 1) != v16):
                        continue
                    break
                break
            if not v16:
                break
            v15 = 0
            arg2 = 0
            if (u32(v16) >= u32(4)):
                v18 = (v16 & -4)
                arg12 = 0
                while True:  # $label9
                    v13 = (arg2 << 2)
                    v14 = (v17 + (arg2 << 2))
                    if (load32((v17 + (arg2 << 2))) == -16711936):
                        store32(v14, 0)
                    v14 = (v17 + (v13 | 4))
                    if (load32((v17 + (v13 | 4))) == -16711936):
                        store32(v14, 0)
                    v14 = (v17 + (v13 | 8))
                    if (load32((v17 + (v13 | 8))) == -16711936):
                        store32(v14, 0)
                    v13 = (v17 + (v13 | 12))
                    if (load32((v17 + (v13 | 12))) == -16711936):
                        store32(v13, 0)
                    arg2 = (arg2 + 4)
                    arg12 = (arg12 + 4)
                    if ((arg12 + 4) != v18):
                        continue
                    break
            arg12 = (v16 & 3)
            if not (v16 & 3):
                break
            while True:  # $label10
                v13 = (v17 + (arg2 << 2))
                if (load32((v17 + (arg2 << 2))) == -16711936):
                    store32(v13, 0)
                arg2 = (arg2 + 1)
                v15 = (v15 + 1)
                if ((v15 + 1) != arg12):
                    continue
                break
            break
        if (arg10 != 22):
            break
        v13 = (arg1 * arg2)
        if not (arg1 * arg2):
            break
        arg2 = 0
        while True:  # $label11
            arg12 = load32(9687232)
            v15 = (arg2 << 2)
            v18 = (load32(9687232) + (arg2 << 2))
            v16 = (v15 | 2)
            v15 = (v15 | 1)
            # TODO: i32.div_u
            arg12 = 3
            store8((load8u((arg12 + (v15 | 2))) + (load8u((arg12 + (v15 | 1))) + load8u(v18))), 3)
            store8((load32(9687232) + v15), arg12)
            store8((load32(9687232) + v16), arg12)
            arg2 = (arg2 + 1)
            if ((arg2 + 1) != v13):
                continue
            break
        break
    arg12 = -1
    while True:  # $label16
        while True:  # $label12
            if not v22:
                break
            if (arg1 <= 0):
                break
            v15 = v19
            v14 = 0
            v16 = -1
            while True:  # $label15
                v13 = 0
                v18 = (v19 * v24)
                if ((v19 * v24) < (v18 + v19)):
                    while True:  # $label14
                        arg2 = v18
                        while True:  # $label13
                            if load32((v17 + (((arg1 * arg2) + v13) << 2))):
                                v23 = (arg2 % v19)
                                v21 = ((arg2 % v19) if (u32(v21) < u32(v23)) else v21)
                                v16 = (v23 if (u32(v16) > u32(v23)) else v16)
                                v14 = (v13 if (u32(v13) > u32(v14)) else v14)
                                arg12 = (v13 if (u32(arg12) > u32(v13)) else arg12)
                            arg2 = (arg2 + 1)
                            if ((arg2 + 1) != v15):
                                continue
                            break
                        v13 = (v13 + 1)
                        if ((v13 + 1) != arg1):
                            continue
                        break
                v15 = (v15 + v19)
                v24 = (v24 + 1)
                if ((v24 + 1) != v22):
                    continue
                break
            break
            break
        v16 = -1
        v14 = 0
        break
    v23 = ((v21 - v16) + 1)
    v24 = ((v14 - arg12) + 1)
    if v20:
        arg2 = (((v22 * v23) * v24) << 2)
        v25 = func26((((v22 * v23) * v24) << 2))
        # TODO: memory.fill
    while True:  # $label17
        if not v22:
            arg2 = load32(9687232)
            break
        v17 = 0
        arg2 = load32(9687232)
        v26 = (v14 + 1)
        if not ((arg12 < (v14 + 1)) & v20):
            break
        v27 = load32(9687236)
        v28 = (v21 + 1)
        v14 = (v21 + 1)
        v15 = 0
        while True:  # $label20
            v13 = (v17 * v19)
            v20 = ((v17 * v19) + v16)
            if (((v17 * v19) + v16) < (v13 + v28)):
                while True:  # $label19
                    v29 = (arg1 * v20)
                    v13 = arg12
                    while True:  # $label18
                        v18 = ((v13 + v29) << 2)
                        if load8u((v27 + ((v13 + v29) << 2))):
                            v21 = (v15 + v25)
                            # TODO: i32.div_u
                            v30 = 3
                            store8((load8u((arg2 + (v18 | 2))) + (load8u((arg2 + (v18 | 1))) + load8u((arg2 + v18)))) + 2, 3)
                            store16(v21, ((v30 & 255) * 257))
                            store8(v21 + 3, load8u((arg2 + (v18 | 3))))
                        v15 = (v15 + 4)
                        v13 = (v13 + 1)
                        if ((v13 + 1) < v26):
                            continue
                        break
                    v20 = (v20 + 1)
                    if ((v20 + 1) != v14):
                        continue
                    break
            v14 = (v14 + v19)
            v17 = (v17 + 1)
            if ((v17 + 1) != v22):
                continue
            break
        break
    if arg2:
        store32(9687232, 0)
    arg1 = load32(9687236)
    if load32(9687236):
        store32(9687236, 0)
    arg2 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    v15 = load32(9687224)
    arg1 = load32(9687220)
    v13 = (arg2 << 2)
    store32((load32(9687220) + (arg2 << 2)), v24)
    v19 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (v19 << 2)), (v22 * v23))
    v19 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    # TODO: i32.div_u
    store32(arg4, (arg12 - arg11))
    arg4 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    # TODO: i32.div_u
    store32(arg5, (v16 - arg11))
    arg4 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg4 << 2)), arg6)
    arg4 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg4 << 2)), arg7)
    arg4 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg4 << 2)), arg3)
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), arg9)
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), arg10)
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), (v15 - v13))
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), 0)
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), arg8)
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), arg11)
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), arg0)
    arg0 = load32(9687228)
    store32(9687228, (load32(9687228) + 2))
    store32((arg1 + (arg0 << 2)) + 4, 0)
    if v25:
    return arg2

# ----------------------------------------------------------
# $func547
# ----------------------------------------------------------
def func547(arg0):
    arg0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v1 = load32(9173808)
    store32(arg0 + 12, load32(9173808))
    while True:  # $label0
        if load8u(9147210):
            func41(3, (arg0 + 12), 1, 0, 0)
            break
        v2 = func26(4)
        store32(func26(4), v1)
        break
    G.global0 = (arg0 + 16)

# ----------------------------------------------------------
# $func548
# ----------------------------------------------------------
def func548(arg0, arg1, arg2, arg3, arg4):
    arg1 = load32(arg1)
    arg2 = entities[load32(arg1)]
    return ((not load8u(((load8u(entities[load32(arg1)].sub_state) * 404) + ENTITY_TYPES) + 352) | (arg0 == arg1)) | not load16u(arg2 + 110))

# ----------------------------------------------------------
# $hb
# Export: hb
# ----------------------------------------------------------
def hb(arg0):
    """Export: hb"""
    while True:  # $label0
        if not load8u(9142905):
            break
        if not load8u(9147127):
            func361()
        v9 = load32(9681680)
        if load32(9681680):
            store32(9681680, 0)
        v9 = load32(PLAYER_COUNT)
        arg0 = (load32(PLAYER_COUNT) * arg0)
        v13 = func26((-1 if (u32(arg0) > u32(1073741823)) else ((load32(PLAYER_COUNT) * arg0) << 2)))
        store32(9681680, func26((-1 if (u32(arg0) > u32(1073741823)) else ((load32(PLAYER_COUNT) * arg0) << 2))))
        if (u32(v9) < u32(2)):
            break
        v17 = load32(38528)
        v20 = load32(9561720)
        v15 = load32(9143004)
        v16 = load32(PLAYERS)
        v21 = load8u(9147127)
        v18 = 1
        while True:  # $label33
            v10 = 1
            while True:  # $label1
                while True:  # $label2
                    if (load32((v16 + (v10 * 286704)) + 283944) == v18):
                        break
                    v10 = (v10 + 1)
                    if ((v10 + 1) != v9):
                        continue
                    break
                v10 = v9
                break
            v3 = (v16 + (v10 * 286704))
            v19 = ((v16 + (v10 * 286704)) + 278556)
            if v21:
                arg0 = (v13 + (v11 << 2))
                store32((v13 + (v11 << 2)), load32(v3 + 283884))
                store32(arg0 + 4, load32(v3 + 283888))
                v11 = (v11 + 2)
            v4 = (v13 + (v11 << 2))
            store32((v13 + (v11 << 2)), load32(v3 + 283892))
            store32(v4 + 4, load32(v3 + 284608))
            v8 = (v11 + 2)
            v22 = (v3 + 284608)
            v12 = (v3 + 281784)
            arg0 = load32((v3 + 281784))
            v5 = (load32((v3 + 281784)) * 255)
            v14 = (arg0 * v9)
            v1 = 0
            v2 = 0
            while True:  # $label5
                while True:  # $label3
                    if not load8u((v15 + (v1 + v14))):
                        break
                    v7 = ((v16 + (v1 * 286704)) + 278568)
                    arg0 = 0
                    while True:  # $label4
                        if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) != 1):
                            v2 = (load32((load32(v7) + ((arg0 + v5) << 2))) + v2)
                        v6 = (arg0 | 1)
                        if ((arg0 | 1) == 255):
                            break
                        if (load32(((v6 * 404) + ENTITY_TYPES) + 264) != 1):
                            v2 = (load32((load32(v7) + ((v5 + v6) << 2))) + v2)
                        arg0 = (arg0 + 2)
                        continue
                        break
                    raise Unreachable()
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32((v13 + (v8 << 2)), v2)
            v8 = (v11 + 3)
            v23 = (v3 + 278568)
            v7 = load32((v3 + 278568))
            v1 = 0
            v2 = 0
            while True:  # $label9
                v6 = (v1 * 255)
                arg0 = 0
                while True:  # $label8
                    while True:  # $label6
                        if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) == 1):
                            break
                        if (arg0 == v17):
                            break
                        v2 = (load32((v7 + ((arg0 + v6) << 2))) + v2)
                        break
                    v5 = (arg0 | 1)
                    if ((arg0 | 1) != 255):
                        while True:  # $label7
                            if (load32(((v5 * 404) + ENTITY_TYPES) + 264) == 1):
                                break
                            if (v5 == v17):
                                break
                            v2 = (load32((v7 + ((v5 + v6) << 2))) + v2)
                            break
                        arg0 = (arg0 + 2)
                        continue
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32((v13 + (v8 << 2)), v2)
            v6 = load32(v12)
            v7 = (load32(v12) * v9)
            v8 = load32(v19)
            v1 = 0
            v2 = 0
            while True:  # $label11
                if load8u((v15 + (v1 + v7))):
                    v14 = (v1 * 255)
                    arg0 = 0
                    while True:  # $label10
                        v5 = (v8 + ((arg0 + v14) << 2))
                        v2 = (load32((v8 + ((arg0 + v14) << 2)) + 16) + (load32(v5 + 12) + (load32(v5 + 8) + (load32(v5 + 4) + (load32(v5) + v2)))))
                        arg0 = (arg0 + 5)
                        if ((arg0 + 5) != 255):
                            continue
                        break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            v6 = (v6 * 255)
            v1 = 0
            v5 = 0
            while True:  # $label14
                while True:  # $label12
                    if not load8u((v15 + (v1 + v7))):
                        break
                    v8 = ((v16 + (v1 * 286704)) + 278564)
                    arg0 = 0
                    while True:  # $label13
                        if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) == 1):
                            v5 = (load32((load32(v8) + ((arg0 + v6) << 2))) + v5)
                        v14 = (arg0 | 1)
                        if ((arg0 | 1) == 255):
                            break
                        if (load32(((v14 * 404) + ENTITY_TYPES) + 264) == 1):
                            v5 = (load32((load32(v8) + ((v6 + v14) << 2))) + v5)
                        arg0 = (arg0 + 2)
                        continue
                        break
                    raise Unreachable()
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32(v4 + 24, v5)
            store32(v4 + 20, (v2 - v5))
            store32(v4 + 16, v2)
            v24 = (v11 + 7)
            v6 = (load32(v12) * v9)
            v25 = (v3 + 278564)
            v7 = load32((v3 + 278564))
            v1 = 0
            v2 = 0
            while True:  # $label16
                if load8u((v15 + (v1 + v6))):
                    v8 = (v1 * 255)
                    arg0 = 0
                    while True:  # $label15
                        v5 = (v7 + ((arg0 + v8) << 2))
                        v2 = (load32((v7 + ((arg0 + v8) << 2)) + 16) + (load32(v5 + 12) + (load32(v5 + 8) + (load32(v5 + 4) + (load32(v5) + v2)))))
                        arg0 = (arg0 + 5)
                        if ((arg0 + 5) != 255):
                            continue
                        break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            v1 = 0
            v5 = 0
            while True:  # $label19
                while True:  # $label17
                    if not load8u((v15 + (v1 + v6))):
                        break
                    v8 = (v1 * 255)
                    arg0 = 0
                    while True:  # $label18
                        if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) == 1):
                            v5 = (load32((v7 + ((arg0 + v8) << 2))) + v5)
                        v14 = (arg0 | 1)
                        if ((arg0 | 1) == 255):
                            break
                        if (load32(((v14 * 404) + ENTITY_TYPES) + 264) == 1):
                            v5 = (load32((v7 + ((v8 + v14) << 2))) + v5)
                        arg0 = (arg0 + 2)
                        continue
                        break
                    raise Unreachable()
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32((v13 + (v24 << 2)), v2)
            store32(v4 + 36, v5)
            store32(v4 + 32, (v2 - v5))
            store32(v4 + 40, load32(v3 + 283956))
            arg0 = (v3 + 281676)
            v1 = (v3 + 281640)
            store32(v4 + 44, (load32((v3 + 281676)) + load32((v3 + 281640))))
            store32(v4 + 48, load32(v1))
            store32(v4 + 52, load32(arg0))
            arg0 = (v3 + 281680)
            v1 = (v3 + 281644)
            store32(v4 + 56, (load32((v3 + 281680)) + load32((v3 + 281644))))
            store32(v4 + 60, load32(v1))
            store32((v4 - -64), load32(arg0))
            arg0 = (v3 + 281684)
            v1 = (v3 + 281656)
            v2 = (v3 + 281648)
            v5 = (v3 + 281660)
            v7 = (v3 + 281652)
            store32(v4 + 68, (load32((v3 + 281684)) + (load32((v3 + 281656)) + (load32((v3 + 281648)) + (load32((v3 + 281660)) + load32((v3 + 281652)))))))
            store32(v4 + 72, load32(v7))
            store32(v4 + 76, load32(v5))
            store32(v4 + 80, load32(v2))
            store32(v4 + 84, load32(v1))
            store32(v4 + 88, load32(arg0))
            arg0 = (v3 + 281688)
            v1 = (v3 + 281664)
            store32(v4 + 92, (load32((v3 + 281688)) + load32((v3 + 281664))))
            store32(v4 + 96, load32(v1))
            store32(v4 + 100, load32(arg0))
            store32(v4 + 104, load32((v3 + 281636)))
            store32(v4 + 108, load32((v3 + 281744)))
            store32(v4 + 112, load32((v3 + 281672)))
            store32(v4 + 116, load32((v3 + 281668)))
            store32(v4 + 120, load32((v3 + 281748)))
            arg0 = 0
            v2 = 0
            while True:  # $label22
                while True:  # $label20
                    if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) & -5):
                        break
                    if (arg0 == v17):
                        break
                    v2 = (load32(((v3 + (arg0 << 2)) + 278576)) + v2)
                    break
                v1 = (arg0 | 1)
                if ((arg0 | 1) != 255):
                    while True:  # $label21
                        if (load32(((v1 * 404) + ENTITY_TYPES) + 264) & -5):
                            break
                        if (v1 == v17):
                            break
                        v2 = (load32(((v3 + (v1 << 2)) + 278576)) + v2)
                        break
                    arg0 = (arg0 + 2)
                    continue
                break
            store32(v4 + 124, v2)
            v6 = (v11 + 32)
            arg0 = load32(v12)
            v5 = (load32(v12) * 255)
            v8 = (arg0 * v9)
            v1 = 0
            v2 = 0
            while True:  # $label25
                while True:  # $label23
                    if not load8u((v15 + (v1 + v8))):
                        break
                    v12 = ((v16 + (v1 * 286704)) + 278568)
                    arg0 = 0
                    while True:  # $label24
                        if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) == 1):
                            v2 = (load32((load32(v12) + ((arg0 + v5) << 2))) + v2)
                        v7 = (arg0 | 1)
                        if ((arg0 | 1) == 255):
                            break
                        if (load32(((v7 * 404) + ENTITY_TYPES) + 264) == 1):
                            v2 = (load32((load32(v12) + ((v5 + v7) << 2))) + v2)
                        arg0 = (arg0 + 2)
                        continue
                        break
                    raise Unreachable()
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32((v13 + (v6 << 2)), v2)
            v5 = load32(v23)
            v1 = 0
            v2 = 0
            while True:  # $label27
                v12 = (v1 * 255)
                arg0 = 0
                while True:  # $label26
                    if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) == 1):
                        v2 = (load32((v5 + ((arg0 + v12) << 2))) + v2)
                    v7 = (arg0 | 1)
                    if ((arg0 | 1) != 255):
                        if (load32(((v7 * 404) + ENTITY_TYPES) + 264) == 1):
                            v2 = (load32((v5 + ((v7 + v12) << 2))) + v2)
                        arg0 = (arg0 + 2)
                        continue
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32(v4 + 132, v2)
            store32(v4 + 136, load32((v3 + 281740)))
            store32(v4 + 140, load32((v3 + 281724)))
            store32(v4 + 144, load32((v3 + 281728)))
            store32(v4 + 148, load32((v3 + 281732)))
            store32(v4 + 152, load32((v3 + 281736)))
            store32(v4 + 156, load32((v3 + 281692)))
            store32(v4 + 160, load32((v3 + 281696)))
            store32(v4 + 164, load32((v3 + 281700)))
            store32(v4 + 168, load32((v3 + 281704)))
            store32(v4 + 172, load32((v3 + 281708)))
            store32(v4 + 176, load32((v3 + 281712)))
            store32(v4 + 180, load32((v3 + 281716)))
            store32(v4 + 184, load32((v3 + 281720)))
            while True:  # $label28
                arg0 = load32(v22)
                if load32(v22):
                    if (arg0 == v20):
                        break
                break
            store32((v13 + ((v11 + 47) << 2)), (load8u(v3 + 286697) != 0))
            arg0 = load32((v3 + 278572))
            store32(v4 + 192, load32(load32((v3 + 278572)) + 8))
            store32(v4 + 196, load32(v3 + 283944))
            store32(v4 + 200, load32(arg0))
            v1 = 0
            v2 = func26(1020)
            # TODO: memory.fill
            v12 = (v9 * v10)
            v7 = (v11 + 51)
            while True:  # $label30
                if load8u((v15 + (v1 + v12))):
                    v10 = (v1 * 255)
                    v5 = load32(v25)
                    arg0 = 0
                    while True:  # $label29
                        v6 = (v2 + (arg0 << 2))
                        store32((v2 + (arg0 << 2)), (load32(v6) + load32((v5 + ((arg0 + v10) << 2)))))
                        v6 = (arg0 + 1)
                        v8 = (v2 + ((arg0 + 1) << 2))
                        store32((v2 + ((arg0 + 1) << 2)), (load32(v8) + load32((v5 + ((v6 + v10) << 2)))))
                        v6 = (arg0 + 2)
                        v8 = (v2 + ((arg0 + 2) << 2))
                        store32((v2 + ((arg0 + 2) << 2)), (load32(v8) + load32((v5 + ((v6 + v10) << 2)))))
                        arg0 = (arg0 + 3)
                        if ((arg0 + 3) != 255):
                            continue
                        break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32((v13 + (v7 << 2)), v2)
            store32(v4 + 216, (v3 + 280616))
            store32(v4 + 212, (v3 + 279596))
            store32(v4 + 208, (v3 + 278576))
            v1 = 0
            v10 = func26(1020)
            # TODO: memory.fill
            v7 = (v11 + 55)
            while True:  # $label32
                if load8u((v15 + (v1 + v12))):
                    v2 = (v1 * 255)
                    v5 = load32(v19)
                    arg0 = 0
                    while True:  # $label31
                        v6 = (v10 + (arg0 << 2))
                        store32((v10 + (arg0 << 2)), (load32(v6) + load32((v5 + ((arg0 + v2) << 2)))))
                        v6 = (arg0 + 1)
                        v8 = (v10 + ((arg0 + 1) << 2))
                        store32((v10 + ((arg0 + 1) << 2)), (load32(v8) + load32((v5 + ((v2 + v6) << 2)))))
                        v6 = (arg0 + 2)
                        v8 = (v10 + ((arg0 + 2) << 2))
                        store32((v10 + ((arg0 + 2) << 2)), (load32(v8) + load32((v5 + ((v2 + v6) << 2)))))
                        arg0 = (arg0 + 3)
                        if ((arg0 + 3) != 255):
                            continue
                        break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32((v13 + (v7 << 2)), v10)
            store32(v4 + 224, load32(v3 + 283908))
            store32(v4 + 228, load32(v3 + 283960))
            arg0 = load32(v3 + 284616)
            if load32(v3 + 284616):
            else:
            store32(arg0, load32(v3 + 284628))
            store32(v4 + 236, v3)
            store32(v4 + 240, ((load8u((v3 + 283974)) | (load8u((v3 + 283973)) << 8)) | (load8u(v3 + 283972) << 16)))
            v11 = (v11 + 61)
            v18 = (v18 + 1)
            if ((v18 + 1) != v9):
                continue
            break
        break
    return v13

# ----------------------------------------------------------
# $ka
# Export: ka
# ----------------------------------------------------------
def ka(arg0, arg1):
    """Export: ka"""
    v3 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v4 = load32(9561696)
    while True:  # $label2
        v6 = load32(9561704)
        if load32(9561704):
            while True:  # $label0
                while True:  # $label1
                    v5 = ((v2 << 2) + v4)
                    if (u32(load32(((v2 << 2) + v4) + 4)) >= u32(arg0)):
                        break
                    v2 = (load32(v5 + 8) + v2)
                    if (u32((load32(v5 + 8) + v2)) < u32(v6)):
                        continue
                    break
                v2 = 0
                break
            arg0 = 0
            while True:  # $label3
                v5 = ((arg0 << 2) + v4)
                if (u32(load32(((arg0 << 2) + v4) + 4)) >= u32(arg1)):
                    break
                arg0 = (load32(v5 + 8) + arg0)
                if (u32((load32(v5 + 8) + arg0)) < u32(v6)):
                    continue
                break
        arg0 = 0
        break
    store32(v3 + 4, (arg0 - v2))
    store32(v3, (v4 + (v2 << 2)))
    G.global0 = (v3 + 16)

# ----------------------------------------------------------
# $func557
# ----------------------------------------------------------
def func557(arg0, arg1, arg2):
    func290(entities[load32(arg1)])

# ----------------------------------------------------------
# $func558
# ----------------------------------------------------------
def func558(arg0):
    store32(9143000, 0)
    arg0 = load32(CURRENT_PLAYER)
    v1 = load32(PLAYERS)
    v2 = load32(9213820)
    if load32(9213820):
        func47(entities[v2])
        store32(9213820, 0)
    func45()
    while True:  # $label0
        arg0 = load32((((v1 + (arg0 * 286704)) + (load32(38452) << 2)) + 284636))
        if not load32((((v1 + (arg0 * 286704)) + (load32(38452) << 2)) + 284636)):
            break
        v2 = load32(arg0 + 8)
        if not load32(arg0 + 8):
            break
        v1 = 0
        while True:  # $label1
            v3 = load32((load32(arg0) + (v1 << 2)))
            if load32((load32(arg0) + (v1 << 2))):
                func44(entities[v3], 0)
                v2 = load32(arg0 + 8)
            v1 = (v1 + 1)
            if (u32((v1 + 1)) < u32(v2)):
                continue
            break
        break

# ----------------------------------------------------------
# $func559
# ----------------------------------------------------------
def func559(arg0, arg1):
    arg1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    store8(9163792, arg0)
    while True:  # $label0
        if arg0:
            break
        if load32(9684820):
            v6 = 2
            arg0 = load32(9684820)
            # TODO: i32.div_u
            v7 = 8
            v4 = func26((8 << 2))
            # TODO: i32.div_u
            store32(arg0 + 4, 6)
            store32(v4, -1)
            if arg0:
                while True:  # $label1
                    arg0 = (v4 + (v6 << 2))
                    v5 = load32(9684812)
                    v8 = (v3 << 2)
                    v2 = (load32(9684812) + (v3 << 2))
                    store32((v4 + (v6 << 2)), load32((load32(9684812) + (v3 << 2))))
                    store32(arg0 + 4, load32((v5 + (v8 | 4))))
                    store32(arg0 + 8, load32(v2 + 8))
                    v5 = load32(v2 + 12)
                    store32(arg0 + 16, 0)
                    store32(arg0 + 12, v5)
                    v5 = load32(v2 + 16)
                    store32(arg0 + 24, 0)
                    store32(arg0 + 20, v5)
                    func38(load32(v2 + 20))
                    v6 = (v6 + 7)
                    v3 = (v3 + 6)
                    if (u32((v3 + 6)) < u32(load32(9684820))):
                        continue
                    break
            arg0 = load32(9213808)
            while True:  # $label2
                if load8u(9147210):
                    func41(5, 9173808, arg0, v4, v7)
                    break
                v3 = (arg0 << 2)
                v2 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                if arg0:
                    # TODO: memory.copy
                break
            store32(9684820, 0)
        while True:  # $label3
            if not load32(9671176):
                break
            if load32(9671192):
                arg0 = 0
                while True:  # $label4
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
        store32(40604, -1)
        if not load32(9684792):
            break
        store32(9684792, 0)
        arg0 = load32(9684796)
        if load8u(9142916):
            store32(arg1 + 32, arg0)
            a_b()
            break
        store32(arg1 + 24, arg0)
        store64(arg1 + 16, -4602115869219225600)
        store64(arg1 + 8, 0)
        store64(arg1, 0)
        a_b()
        break
    G.global0 = (arg1 + 48)
