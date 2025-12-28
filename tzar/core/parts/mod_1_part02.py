"""
Tzar Engine - Core module (part 2).
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
# $func689
# ----------------------------------------------------------
def func689(arg0, arg1, param2):
    v9 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v21 = load32(ENTITIES)
    v7 = entities[arg0]
    v12 = load16u(entities[arg0] + 114)
    v17 = load16u(v7 + 112)
    v23 = load8u(v7 + 122)
    while True:  # $label0
        if not load8u(9216060):
            break
        v14 = load16u(v7 + 110)
        if not load16u(v7 + 110):
            break
        v4 = (v21 + (load32((load32(9142840) + ((v17 + ((load32(9142440) + 2) * (v12 + 1))) << 2)) + 4) * 132))
        if (load32(39064) != load8u((v21 + (load32((load32(9142840) + ((v17 + ((load32(9142440) + 2) * (v12 + 1))) << 2)) + 4) * 132)) + 122)):
            break
        while True:  # $label1
            v10 = load32(PLAYERS)
            v6 = players[v14]
            v2 = load32(players[v14] + 283848)
            if (load32(players[v14] + 283848) == 2147483647):
                break
            store32((v6 + 283848), (load32(v4 + 52) + v2))
            v2 = 1
            store8(v6 + 286701, 1)
            v3 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            v5 = (v3 - 1)
            v11 = ((v3 - 1) & 1)
            v14 = (load32((v10 + (v14 * 286704)) + 283908) * v3)
            v10 = load32(PLAYERS)
            v8 = load32(9143016)
            if (v3 != 2):
                v24 = (v5 & -2)
                v3 = 0
                while True:  # $label2
                    if load8u((v8 + (v2 + v14))):
                        store8((v10 + (v2 * 286704)) + 286701, 1)
                    v5 = (v2 + 1)
                    if load8u((v8 + ((v2 + 1) + v14))):
                        store8((v10 + (v5 * 286704)) + 286701, 1)
                    v2 = (v2 + 2)
                    v3 = (v3 + 2)
                    if ((v3 + 2) != v24):
                        continue
                    break
            if not v11:
                break
            if not load8u((v8 + (v2 + v14))):
                break
            store8((v10 + (v2 * 286704)) + 286701, 1)
            break
        v2 = (v6 + 281640)
        store32((v6 + 281640), (load32(v2) + load32(v4 + 52)))
        if load8u(9142917):
            break
        if (load32(CURRENT_PLAYER) != load16u(v7 + 110)):
            break
        a_b()
        break
    while True:  # $label3
        if (arg1 == 1):
            break
        if not load8u(59181):
            break
        if (load8u(v7 + 125) == 7):
            break
        v2 = (load8u((v21 + (arg0 * 132)) + 124) << 3)
        break
    while True:  # $label5
        while True:  # $label4
            v18 = (v21 + (arg0 * 132))
            v3 = load8u((v21 + (arg0 * 132)) + 129)
            # br_table (load8u((v21 + (arg0 * 132)) + 129) - 5)
            break
            break
        while True:  # $label6
            while True:  # $label7
                v2 = load8u(v18 + 123)
                # br_table load8u(v18 + 123)
                break
                break
            if (v2 == 69):
                break
            if (v2 != 35):
                break
            break
        if not (arg1 & 1):
            break
        while True:  # $label8
            if (v3 != 9):
                break
            v2 = load32((v21 + (arg0 * 132)) + 32)
            if not load32((v21 + (arg0 * 132)) + 32):
                break
            break
        v2 = func106(v7, load8u(entities[v2].sub_state), -1, -1)
        if not func106(v7, load8u(entities[v2].sub_state), -1, -1):
            break
        store32((v21 + (arg0 * 132)) + 32, v2)
        store8(v18 + 123, 6)
        break
    while True:  # $label19
        while True:  # $label10
            while True:  # $label14
                while True:  # $label9
                    v2 = load8u(v18 + 123)
                    if load8u(v18 + 123):
                        break
                    if not load16u(v18 + 108):
                        break
                    v11 = 0
                    v2 = (v21 + (arg0 * 132))
                    v3 = load32((v21 + (arg0 * 132)) + 32)
                    if not load32((v21 + (arg0 * 132)) + 32):
                        break
                    v4 = load32(v2 + 88)
                    if not load32(v2 + 88):
                        break
                    while True:  # $label11
                        while True:  # $label12
                            v2 = load8u(v7 + 122)
                            # br_table (load8u(v7 + 122) + -64)
                            break
                            break
                        if (v2 != 10):
                            break
                        break
                    while True:  # $label13
                        v3 = entities[v3]
                        # br_table (load8u(entities[v3].unit_class) - 4)
                        break
                        break
                    v2 = 3
                    v3 = load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 192)
                    v4 = (v4 & 65535)
                    if ((load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 192) != ((v4 & 65535) if (v4 != 3) else 0)) & (v3 != 4)):
                        break
                    store8(v18 + 123, 3)
                    break
                    break
                if v2:
                    break
                v11 = 0
                break
                break
            v5 = ((v23 * 404) + 9568320)
            while True:  # $label20
                while True:  # $label18
                    while True:  # $label16
                        while True:  # $label17
                            while True:  # $label15
                                v6 = v2
                                v14 = (v2 & 255)
                                v2 = (((v2 & 255) * 40) + 9671200)
                                v3 = load32((((v2 & 255) * 40) + 9671200) + 28)
                                if load32((((v2 & 255) * 40) + 9671200) + 28):
                                    if call_table(v3):
                                        break
                                v3 = v5
                                v4 = load32(v2 + 4)
                                # br_table (load32(v2 + 4) + 2)
                                break
                                break
                            break
                            break
                        v3 = ((players[load16u(v7 + 110)] + (v4 << 2)) + 283984)
                        break
                    v4 = load32(v3)
                    break
                v2 = load8u(v18 + 123)
                if (v14 != load8u(v18 + 123)):
                    continue
                break
            v11 = (4 if ((v6 & 255) == 69) else v4)
            break
        v3 = (v21 + (arg0 * 132))
        v2 = load32((v21 + (arg0 * 132)) + 32)
        if (load32((v21 + (arg0 * 132)) + 32) == load32(v3 + 28)):
            break
        while True:  # $label21
            if v2:
                break
            v4 = load32(((v23 * 404) + ENTITY_TYPES) + 216)
            if not load32(((v23 * 404) + ENTITY_TYPES) + 216):
                break
            v2 = (v21 + (arg0 * 132))
            v14 = (v21 + (arg0 * 132))
            v10 = load16u(v2 + 116)
            v5 = 0
            v6 = 1
            while True:  # $label24
                while True:  # $label22
                    if (v10 == (v5 + v17)):
                        v8 = load16u(v14 + 118)
                        v2 = 0
                        while True:  # $label23
                            if ((v2 + v12) == v8):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v4):
                                continue
                            break
                    v5 = (v5 + 1)
                    v6 = (u32((v5 + 1)) < u32(v4))
                    if (v4 != v5):
                        continue
                    break
                    break
                break
            if (v6 & 1):
                break
            break
        v24 = v3
        v28 = ((v23 * 404) + ENTITY_TYPES)
        v14 = load32(((v23 * 404) + ENTITY_TYPES) + 208)
        v6 = ((load8u(v7 + 122) * 404) + ENTITY_TYPES)
        if load32(((load8u(v7 + 122) * 404) + ENTITY_TYPES) + 216):
            v3 = (v6 + 216)
            v5 = (v6 + 208)
            v10 = load32(9142840)
            v8 = load16u(v7 + 114)
            v13 = load16u(v7 + 112)
            v4 = 0
            while True:  # $label26
                v4 = (v4 + 1)
                v15 = ((v4 + 1) + v13)
                v2 = 0
                while True:  # $label25
                    v2 = (v2 + 1)
                    v16 = (load32(9142440) + 2)
                    store32((v10 + ((v15 + ((((v2 + 1) + v8) + ((load32(9142440) + 2) * load32(v5))) * v16)) << 2)), load32(v6 + 212))
                    v16 = load32(v3)
                    if (u32(v2) < u32(load32(v3))):
                        continue
                    break
                if (u32(v4) < u32(v16)):
                    continue
                break
        while True:  # $label30
            v2 = load32(v24 + 32)
            if load32(v24 + 32):
                while True:  # $label27
                    v4 = load32(ENTITIES)
                    v13 = entities[v2]
                    if (load8u(entities[v2].unit_class) != 3):
                        if not load8u(v13 + 128):
                            break
                        if not load8u((load32(9143004) + (load16u(v7 + 110) + (load32(PLAYER_COUNT) * load16u((v4 + (v2 * 132)) + 110))))):
                            break
                    break
                    break
                while True:  # $label28
                    if (u32(v11) < u32(2)):
                        break
                    while True:  # $label29
                        v2 = (v4 + (v2 * 132))
                        v4 = load8u((v4 + (v2 * 132)) + 122)
                        v6 = ((load8u((v4 + (v2 * 132)) + 122) * 404) + ENTITY_TYPES)
                        v16 = load32(((load8u((v4 + (v2 * 132)) + 122) * 404) + ENTITY_TYPES) + 216)
                        v10 = load16u(v2 + 112)
                        v19 = (load32(((load8u((v4 + (v2 * 132)) + 122) * 404) + ENTITY_TYPES) + 216) + load16u(v2 + 112))
                        if ((load32(((load8u((v4 + (v2 * 132)) + 122) * 404) + ENTITY_TYPES) + 216) + load16u(v2 + 112)) > v10):
                            v8 = load16u(v2 + 114)
                            v20 = (load16u(v2 + 114) + load32(v6 + 220))
                            if ((load16u(v2 + 114) + load32(v6 + 220)) > v8):
                                break
                        v6 = 1
                        break
                        break
                    v22 = load32(((v4 * 404) + ENTITY_TYPES) + 372)
                    v6 = 2147483647
                    v4 = v10
                    while True:  # $label32
                        v25 = (v4 - v10)
                        v2 = (v4 - v17)
                        v26 = ((v4 - v17) * v2)
                        v2 = v8
                        while True:  # $label31
                            v15 = (v2 - v12)
                            v15 = (((v2 - v12) * v15) + v26)
                            v15 = ((load8u((v22 + (v25 + ((v2 - v8) * v16)))) != 0) & (v6 > v15))
                            v6 = ((((v2 - v12) * v15) + v26) if ((load8u((v22 + (v25 + ((v2 - v8) * v16)))) != 0) & (v6 > v15)) else v6)
                            v5 = (v4 if v15 else v5)
                            v3 = (v2 if v15 else v3)
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v20):
                                continue
                            break
                        v4 = (v4 + 1)
                        if ((v4 + 1) != v19):
                            continue
                        break
                    store32(v9 + 24, v3)
                    store32(v9 + 28, v5)
                    if (v6 == 2147483647):
                        break
                    v2 = (v17 - v5)
                    v2 = (v12 - v3)
                    if (((((v17 - v5) * v2) + ((v12 - v3) * v2)) - 1) > (v11 * v11)):
                        break
                    break
                    break
                v6 = 1
                v2 = func235((v9 + 28), (v9 + 24), v7, v13, 0)
                if (u32(v11) > u32(1)):
                    break
                if v2:
                    break
                v32 = load8u(v18 + 123)
                v33 = load16u(v7 + 112)
                v22 = load16u(v7 + 114)
                v25 = load32(((v23 * 404) + ENTITY_TYPES) + 212)
                v26 = ((load8u(v13 + 122) * 404) + ENTITY_TYPES)
                v4 = 2147483647
                v34 = load16u(v13 + 112)
                v15 = load16u(v13 + 112)
                v35 = load16u(v13 + 114)
                v16 = load16u(v13 + 114)
                v27 = 1
                v11 = 1
                while True:  # $label44
                    while True:  # $label43
                        v15 = (v15 + 1)
                        v16 = (v16 + 1)
                        while True:  # $label33
                            v5 = (v34 - v11)
                            v2 = load32(v26 + 216)
                            v3 = (v11 << 1)
                            v10 = (v5 + (load32(v26 + 216) + (v11 << 1)))
                            if ((v34 - v11) >= (v5 + (load32(v26 + 216) + (v11 << 1)))):
                                break
                            v6 = (v35 - v11)
                            v8 = load32(v26 + 220)
                            v3 = (v6 + (v3 + load32(v26 + 220)))
                            if ((v35 - v11) >= (v6 + (v3 + load32(v26 + 220)))):
                                break
                            v36 = (v10 - 1)
                            v37 = (v3 - 1)
                            v38 = (v2 + v15)
                            v29 = (v8 + v16)
                            v19 = 0
                            v3 = v5
                            while True:  # $label42
                                v10 = (v3 + 1)
                                v2 = (v3 - v33)
                                v30 = ((v3 - v33) * v2)
                                v31 = load32(9142840)
                                while True:  # $label37
                                    while True:  # $label34
                                        if (v3 == v36):
                                            break
                                        if (v3 == v5):
                                            break
                                        v2 = v6
                                        while True:  # $label36
                                            while True:  # $label35
                                                if ((v2 != v6) & (v2 != v37)):
                                                    break
                                                v8 = load32(9142440)
                                                if (u32(load32(9142440)) <= u32(v2)):
                                                    break
                                                if ((v2 | v3) < 0):
                                                    break
                                                if (u32(v3) >= u32(v8)):
                                                    break
                                                v8 = (v8 + 2)
                                                if (load32((v31 + ((v10 + (((v2 + ((v8 + 2) * v14)) + 1) * v8)) << 2))) != v25):
                                                    break
                                                v8 = (v2 - v22)
                                                v8 = (((v2 - v22) * v8) + v30)
                                                if ((((v2 - v22) * v8) + v30) >= v4):
                                                    break
                                                store32(v9 + 28, v3)
                                                store32(v9 + 24, v2)
                                                v19 = 1
                                                v4 = v8
                                                break
                                            v2 = (v2 + 1)
                                            if ((v2 + 1) != v29):
                                                continue
                                            break
                                        break
                                        break
                                    v13 = load32(9142440)
                                    v2 = v6
                                    while True:  # $label41
                                        while True:  # $label40
                                            while True:  # $label39
                                                while True:  # $label38
                                                    if (u32(v2) >= u32(v13)):
                                                        break
                                                    if ((v2 | v3) < 0):
                                                        break
                                                    if (u32(v3) < u32(v13)):
                                                        break
                                                    break
                                                break
                                                break
                                            v20 = (v2 + 1)
                                            v8 = (v13 + 2)
                                            if (v25 != load32((v31 + ((v10 + (((v2 + 1) + ((v13 + 2) * v14)) * v8)) << 2)))):
                                                break
                                            v8 = (v2 - v22)
                                            v8 = (((v2 - v22) * v8) + v30)
                                            if (v4 <= (((v2 - v22) * v8) + v30)):
                                                break
                                            store32(v9 + 28, v3)
                                            store32(v9 + 24, v2)
                                            v13 = load32(9142440)
                                            v19 = 1
                                            v4 = v8
                                            break
                                        v2 = v20
                                        if (v20 != v20):
                                            continue
                                        break
                                    break
                                v3 = v10
                                if (v10 != v38):
                                    continue
                                break
                            if v19:
                                break
                            break
                        v27 = (u32(v11) < u32(19))
                        v11 = (v11 + 1)
                        if ((v11 + 1) != 20):
                            continue
                        break
                    break
                if v27:
                    v6 = not v32
                    break
                func140(v7)
                break
            v2 = (v21 + (arg0 * 132))
            v5 = load16u((v21 + (arg0 * 132)) + 116)
            store32(v9 + 28, load16u((v21 + (arg0 * 132)) + 116))
            v10 = load16u(v2 + 118)
            store32(v9 + 24, load16u(v2 + 118))
            while True:  # $label45
                if (u32(v11) < u32(2)):
                    break
                v3 = load32(((v23 * 404) + ENTITY_TYPES) + 216)
                if not load32(((v23 * 404) + ENTITY_TYPES) + 216):
                    break
                v8 = (v11 * v11)
                v6 = 0
                v4 = 1
                while True:  # $label48
                    v2 = (v5 - (v6 + v17))
                    v11 = (((v5 - (v6 + v17)) * v2) - 1)
                    v2 = 0
                    while True:  # $label47
                        while True:  # $label46
                            v13 = (v10 - (v2 + v12))
                            if (v8 < (v11 + ((v10 - (v2 + v12)) * v13))):
                                v2 = (v2 + 1)
                                if (v3 != (v2 + 1)):
                                    continue
                                break
                            break
                        if (v4 & 1):
                            break
                        break
                        break
                    v6 = (v6 + 1)
                    v4 = (u32((v6 + 1)) < u32(v3))
                    if (v3 != v6):
                        continue
                    break
                break
            v6 = 1
            v2 = (load32(9142440) + 2)
            if (u32(load32((load32(9142840) + ((v5 + (((v10 + ((load32(9142440) + 2) * v14)) + 1) * v2)) << 2)) + 4)) < u32(3)):
                break
            v29 = load32(v28 + 208)
            v2 = ((v23 * 404) + ENTITY_TYPES)
            v30 = load32(((v23 * 404) + ENTITY_TYPES) + 212)
            v15 = load32(v2 + 216)
            v31 = load32(v9 + 24)
            v32 = load32(v9 + 28)
            v13 = 1
            while True:  # $label60
                v2 = ((v13 << 1) | 1)
                v8 = (v32 - v13)
                v33 = (((v13 << 1) | 1) + (v32 - v13))
                v16 = ((((v13 << 1) | 1) + (v32 - v13)) - 1)
                v11 = (v31 - v13)
                v19 = (v2 + (v31 - v13))
                v20 = ((v2 + (v31 - v13)) - 1)
                v2 = v8
                v4 = 2147483647
                while True:  # $label59
                    v3 = (v2 - v17)
                    v22 = ((v2 - v17) * v3)
                    v3 = v11
                    v5 = v11
                    while True:  # $label55
                        v34 = (v2 + v15)
                        if (v2 < (v2 + v15)):
                            while True:  # $label54
                                while True:  # $label50
                                    while True:  # $label49
                                        if (v2 == v8):
                                            break
                                        if (v3 == v11):
                                            break
                                        if (v3 == v20):
                                            break
                                        if (v2 != v16):
                                            break
                                        break
                                    v5 = load32(9142440)
                                    if (u32(load32(9142440)) <= u32(v3)):
                                        break
                                    if ((v2 | v3) < 0):
                                        break
                                    if (u32(v2) >= u32(v5)):
                                        break
                                    v25 = (v3 + v15)
                                    if (v3 < (v3 + v15)):
                                        v35 = (v5 + 2)
                                        v36 = ((v5 + 2) * v29)
                                        v26 = 0
                                        v37 = load32(ENTITIES)
                                        v38 = load32(9142840)
                                        v10 = v3
                                        while True:  # $label53
                                            v10 = (v10 + 1)
                                            v39 = (((v10 + 1) + v36) * v35)
                                            v5 = v2
                                            while True:  # $label51
                                                while True:  # $label52
                                                    v5 = (v5 + 1)
                                                    v27 = load32((v38 + (((v5 + 1) + v39) << 2)))
                                                    if (v30 != load32((v38 + (((v5 + 1) + v39) << 2)))):
                                                        if (v27 == -1):
                                                            break
                                                        if (load8u((v37 + (v27 * 132)) + 125) != 1):
                                                            break
                                                    if (v5 != v34):
                                                        continue
                                                    break
                                                v26 = (v10 >= v25)
                                                if (v10 != v25):
                                                    continue
                                                break
                                            break
                                        if not v26:
                                            break
                                    v5 = (v3 - v12)
                                    v5 = (((v3 - v12) * v5) + v22)
                                    if ((((v3 - v12) * v5) + v22) >= v4):
                                        break
                                    store32(v9 + 28, v2)
                                    store32(v9 + 24, v3)
                                    v4 = v5
                                    break
                                v3 = (v3 + 1)
                                if ((v3 + 1) < v19):
                                    continue
                                break
                                break
                            raise Unreachable()
                        while True:  # $label58
                            while True:  # $label57
                                while True:  # $label56
                                    if (v2 == v8):
                                        break
                                    if (v5 == v11):
                                        break
                                    if (v5 == v20):
                                        break
                                    if (v2 != v16):
                                        break
                                    break
                                v3 = load32(9142440)
                                if (u32(load32(9142440)) <= u32(v5)):
                                    break
                                if ((v2 | v5) < 0):
                                    break
                                if (u32(v2) >= u32(v3)):
                                    break
                                v3 = (v5 - v12)
                                v3 = (((v5 - v12) * v3) + v22)
                                if ((((v5 - v12) * v3) + v22) >= v4):
                                    break
                                store32(v9 + 28, v2)
                                store32(v9 + 24, v5)
                                v4 = v3
                                break
                            v5 = (v5 + 1)
                            if ((v5 + 1) < v19):
                                continue
                            break
                        break
                    v2 = (v2 + 1)
                    if ((v2 + 1) < v33):
                        continue
                    break
                if (v4 == 2147483647):
                    v13 = (v13 + 1)
                    if ((v13 + 1) != 20):
                        continue
                break
            break
        while True:  # $label61
            v5 = ((v23 * 404) + ENTITY_TYPES)
            v10 = load32(((v23 * 404) + ENTITY_TYPES) + 216)
            if not load32(((v23 * 404) + ENTITY_TYPES) + 216):
                break
            v3 = 0
            v8 = load32(v9 + 24)
            v11 = load32(v9 + 28)
            v4 = 1
            while True:  # $label64
                while True:  # $label62
                    v2 = 0
                    if (v11 == (v3 + v17)):
                        while True:  # $label63
                            if ((v2 + v12) == v8):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v10):
                                continue
                            break
                    v3 = (v3 + 1)
                    v4 = (u32((v3 + 1)) < u32(v10))
                    if (v3 != v10):
                        continue
                    break
                    break
                break
            v2 = load8u(v18 + 129)
            if not (v6 | (load8u(v18 + 129) != 5)):
                store8(v18 + 129, 0)
                v2 = 0
            while True:  # $label66
                while True:  # $label65
                    v3 = load8u(v18 + 123)
                    if (not load8u(v18 + 123) | v6):
                        break
                    if ((v3 == 6) & (v2 != 9)):
                        break
                    func140(v7)
                    break
                    break
                break
            if (v4 & 1):
                break
            break
        if (load8u(v18 + 129) == 6):
            break
        v2 = ((v23 * 404) + ENTITY_TYPES)
        v3 = ((v23 * 404) + ENTITY_TYPES)
        while True:  # $label67
            v11 = load32(v9 + 28)
            v4 = load32(v9 + 24)
            v2 = (v21 + (arg0 * 132))
            v18 = (v21 + (arg0 * 132))
            if func177(v17, v12, load32(v9 + 28), load32(v9 + 24), load32(v2 + 212), v14, (v9 + 20), (v9 + 16), load32(v5 + 216), ((v21 + (arg0 * 132)) + 56), (v2 + 130), 0):
                break
            v2 = load32(v24 + 32)
            if not load32(v24 + 32):
                break
            v6 = (v17 - v11)
            v6 = (v12 - v4)
            if (((((v17 - v11) * v6) + ((v12 - v4) * v6)) - 1) > 196):
                break
            v4 = load32(v9 + 24)
            while True:  # $label68
                v11 = load32(v9 + 28)
                if (load32(v9 + 28) != v17):
                    break
                if (v4 != v12):
                    break
                break
                break
            store32(v9 + 12, 0)
            break
        v6 = (v9 + 20)
        v10 = (v9 + 16)
        while True:  # $label78
            while True:  # $label69
                v8 = load32(v5 + 216)
                if not load32(v5 + 216):
                    break
                v24 = (v17 + 1)
                v13 = (v12 + 1)
                v5 = 0
                v15 = (load32(9142440) + 2)
                v16 = (v14 * (load32(9142440) + 2))
                v19 = load32(v3 + 212)
                v20 = load32(9142840)
                v22 = load32(v9 + 16)
                v25 = load32(v9 + 20)
                v14 = 0
                while True:  # $label72
                    v26 = ((v5 + v24) + v25)
                    v2 = 0
                    while True:  # $label71
                        while True:  # $label70
                            if (v19 == load32((v20 + ((v26 + ((((v2 + v13) + v22) + v16) * v15)) << 2)))):
                                v2 = (v2 + 1)
                                if (v8 != (v2 + 1)):
                                    continue
                                break
                            break
                        v14 = 1
                        break
                    v5 = (v5 + 1)
                    if ((v5 + 1) != v8):
                        continue
                    break
                if not v14:
                    break
                v2 = load32(v18 + 56)
                v18 = (((load32(v18 + 56) & 0xFFFFFFFF) >> 16) if v2 else v4)
                v4 = ((((load32(v18 + 56) & 0xFFFFFFFF) >> 16) if v2 else v4) + (load32(v9 + 16) - v12))
                v13 = ((v2 & 65535) if v2 else v11)
                v2 = (((v2 & 65535) if v2 else v11) + (load32(v9 + 20) - v17))
                v4 = ((((((load32(v18 + 56) & 0xFFFFFFFF) >> 16) if v2 else v4) + (load32(v9 + 16) - v12)) * v4) + ((((v2 & 65535) if v2 else v11) + (load32(v9 + 20) - v17)) * v2))
                v10 = 0
                v15 = (load32(9142440) + 2)
                v16 = ((load32(9142440) + 2) * load32(v28 + 208))
                v19 = load32(9142840)
                v20 = load32(v3 + 212)
                v11 = 55
                v28 = (v8 <= 0)
                while True:  # $label77
                    v2 = (v10 << 3)
                    v3 = (load32(((v10 << 3) + 8932)) + v12)
                    v5 = (load32((v2 + 8928)) + v17)
                    while True:  # $label75
                        while True:  # $label73
                            if v28:
                                break
                            v14 = (v5 + v8)
                            v2 = (v3 + v8)
                            v22 = ((v3 + v8) if (v2 > v3) else v3)
                            v24 = 1
                            v6 = v5
                            while True:  # $label74
                                v6 = (v6 + 1)
                                v2 = v3
                                while True:  # $label76
                                    if (v2 == v22):
                                        if (v6 < v14):
                                            continue
                                        if not v24:
                                            break
                                        break
                                    v2 = (v2 + 1)
                                    if (load32((v19 + (((((v2 + 1) + v16) * v15) + v6) << 2))) == v20):
                                        continue
                                    break
                                v24 = 0
                                if (v6 < v14):
                                    continue
                                break
                            break
                            break
                        v2 = (v3 - v18)
                        v2 = (v5 - v13)
                        v2 = (((v3 - v18) * v2) + ((v5 - v13) * v2))
                        v2 = (v2 < v4)
                        v4 = ((((v3 - v18) * v2) + ((v5 - v13) * v2)) if (v2 < v4) else v4)
                        v11 = (v10 if v2 else v11)
                        break
                    v10 = (v10 + 1)
                    if ((v10 + 1) != 8):
                        continue
                    break
                if (v11 == 55):
                    break
                v2 = (v11 << 3)
                v10 = ((v11 << 3) + 8932)
                v6 = (v2 + 8928)
                break
            while True:  # $label80
                while True:  # $label79
                    v3 = load32(v6)
                    if (u32((load32(v6) - 2)) < u32(-3)):
                        break
                    v2 = load32(v10)
                    if (load32(v10) > 1):
                        break
                    if (v2 < -1):
                        break
                    v4 = load32(9142440)
                    v6 = (v2 + v12)
                    if (u32(load32(9142440)) <= u32((v2 + v12))):
                        break
                    v5 = (v3 + v17)
                    if ((v6 | (v3 + v17)) < 0):
                        break
                    if (u32(v4) > u32(v5)):
                        break
                    break
                func140(v7)
                break
                break
            v5 = load32(((v23 * 404) + ENTITY_TYPES) + 260)
            if not load32(((v23 * 404) + ENTITY_TYPES) + 260):
                break
            v4 = load32(((load8u(v7 + 122) * 404) + ENTITY_TYPES) + 260)
            if load32(((load8u(v7 + 122) * 404) + ENTITY_TYPES) + 260):
                v4 = (32000 // v4)
            else:
            v40 = 1.0
            arg0 = (v21 + (arg0 * 132))
            v6 = load8u((v21 + (arg0 * 132)) + 124)
            v4 = 6
            v12 = (((v2 * 3) + v3) + 4)
            if (u32((((v2 * 3) + v3) + 4)) <= u32(8)):
                v4 = load8u((v12 + 10184))
            store8(arg0 + 124, v4)
            v12 = (arg1 == 1)
            v4 = func289(v7, ((arg1 == 1) | (v6 != (v4 & 255))), 0.0)
            while True:  # $label84
                while True:  # $label83
                    while True:  # $label82
                        while True:  # $label81
                            if v12:
                                break
                            if v4:
                                break
                            if load8u(9147124):
                                break
                            v4 = not load8u(9142916)
                            break
                            break
                        v40 = (32000.0 / v40)
                        func92(v7, ((32000.0 / v40) * i32(v3)), (v40 * i32(v2)))
                        v12 = load8u(9142916)
                        v4 = not load8u(9142916)
                        if (arg1 != 1):
                            break
                        if not v12:
                            break
                        break
                    if v4:
                        break
                    if (v6 == load8u(arg0 + 124)):
                        break
                    break
                break
            if not load8u(59181):
            store16(v7 + 112, (load16u(v7 + 112) + v3))
            store16(v7 + 114, (load16u(v7 + 114) + v2))
            arg0 = (players[load16u(v7 + 110)] + 281740)
            store32((players[load16u(v7 + 110)] + 281740), (load32(arg0) + 1))
            arg0 = load32(9215884)
            store32((load32(9215884) + (load32(v7 + 44) << 4)) + 12, (arg1 + 1))
            # TODO: i32.div_u
            store32(load32(9142848), ((32000 // v5) + 25))
            store8(v7 + 125, 1)
            arg0 = 0
            v2 = ((load8u(v7 + 122) * 404) + ENTITY_TYPES)
            if load32(((load8u(v7 + 122) * 404) + ENTITY_TYPES) + 216):
                v3 = load32(9142840)
                v4 = load16u(v7 + 114)
                v6 = load16u(v7 + 112)
                while True:  # $label86
                    arg0 = (arg0 + 1)
                    v5 = ((arg0 + 1) + v6)
                    arg1 = 0
                    while True:  # $label85
                        arg1 = (arg1 + 1)
                        v12 = (load32(9142440) + 2)
                        store32((v3 + ((v5 + ((((arg1 + 1) + v4) + ((load32(9142440) + 2) * load32(v2 + 208))) * v12)) << 2)), load32(v7 + 28))
                        v12 = load32(v2 + 216)
                        if (u32(arg1) < u32(load32(v2 + 216))):
                            continue
                        break
                    if (u32(arg0) < u32(v12)):
                        continue
                    break
            func118(v7)
            break
            break
        func140(v7)
        break
    G.global0 = (v9 + 32)
    return (arg0 + (load32(v7 + 44) << 4))

# ----------------------------------------------------------
# $func690
# ----------------------------------------------------------
def func690(arg0, arg1, arg2, arg3, arg4):
    v7 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg4 = 1
    while True:  # $label2
        v6 = load32(ENTITIES)
        v10 = entities[arg0]
        v8 = load8u(entities[arg0].sub_state)
        v9 = ((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES)
        if (load32(((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES) + 264) == 1):
            while True:  # $label0
                arg1 = load32(arg1)
                if load32(arg1):
                    arg1 = (v6 + (arg1 * 132))
                    v5 = ((load8u(arg1 + 122) * 404) + ENTITY_TYPES)
                    arg4 = (load16u((v6 + (arg1 * 132)) + 114) + ((load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 220) & 0xFFFFFFFF) >> 1))
                    break
                arg4 = load32(arg3)
                break
            arg1 = load32(arg2)
            v5 = (v6 + (arg0 * 132))
            store16((v6 + (arg0 * 132)) + 118, arg4)
            store16(v5 + 116, arg1)
            arg4 = 1
            arg1 = (load32(9142440) + 2)
            if (load32((load32(9142840) + ((load32(arg2) + (((load32(arg3) + ((load32(9142440) + 2) * load32(((v8 * 404) + ENTITY_TYPES) + 208))) + 1) * arg1)) << 2)) + 4) == load32(v5 + 28)):
                while True:  # $label1
                    arg0 = load32(v5 + 80)
                    if not load32(v5 + 80):
                        break
                    if (load32(v9 + 264) != 1):
                        break
                    func38(arg0)
                    store32(v5 + 80, 0)
                    break
                store16(v5 + 116, 0)
                store16(v5 + 118, 0)
                break
            if not load32(v5 + 92):
                break
            while True:  # $label3
                arg0 = (v6 + (arg0 * 132))
                arg1 = load32((v6 + (arg0 * 132)) + 80)
                if not load32((v6 + (arg0 * 132)) + 80):
                    break
                if (load32(v9 + 264) != 1):
                    break
                func38(arg1)
                store32(arg0 + 80, 0)
                break
            func203(v10)
            break
        if not load32(v9 + 260):
            break
        while True:  # $label4
            if (load32(arg1) != arg0):
                break
            store32(arg1, 0)
            if (load32((load32(9215884) + (load32((v6 + (arg0 * 132)) + 44) << 4)) + 4) != 6):
                break
            func304(v10)
            break
            break
        arg4 = 0
        while True:  # $label8
            while True:  # $label7
                while True:  # $label5
                    while True:  # $label6
                        arg0 = ((v8 * 404) + ENTITY_TYPES)
                        v5 = load32(((v8 * 404) + ENTITY_TYPES) + 212)
                        # br_table load32(((v8 * 404) + ENTITY_TYPES) + 212)
                        break
                        break
                    arg0 = load32(arg2)
                    arg1 = load32(arg3)
                    v6 = (load32(9142440) + 2)
                    if (u32((load32((load32(9142840) + ((load32(arg2) + (((load32(arg3) + (load32(9142440) + 2)) + 1) * v6)) << 2)) + 4) - 3)) < u32(-2)):
                        break
                    break
                    break
                if (load32(arg0 + 208) > 1):
                    break
                arg0 = load32(arg2)
                arg1 = load32(arg3)
                v6 = (load32(9142440) + 2)
                if (load32((load32(9142840) + ((load32(arg2) + (((load32(arg3) + (load32(9142440) + 2)) + 1) * v6)) << 2)) + 4) != 1):
                    break
                break
            store32(v7 + 12, arg0)
            store32(v7 + 8, arg1)
            arg4 = 1
            if not func167((v7 + 12), (v7 + 8), 1, v5, load32(((v8 * 404) + ENTITY_TYPES) + 216)):
                break
            store32(arg2, load32(v7 + 12))
            store32(arg3, load32(v7 + 8))
            break
        arg4 = 0
        break
    G.global0 = (v7 + 16)
    return arg4

# ----------------------------------------------------------
# $func691
# ----------------------------------------------------------
def func691(arg0):
    arg0 = load32(9213808)
    if load8u(9147210):
        func41(24, 9173808, arg0, 0, 0)
        return
    v2 = (arg0 << 2)
    v1 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
    if arg0:
        # TODO: memory.copy

# ----------------------------------------------------------
# $func692
# ----------------------------------------------------------
def func692(arg0):
    arg0 = load32(9213808)
    if load8u(9147210):
        func41(26, 9173808, arg0, 0, 0)
        return
    v2 = (arg0 << 2)
    v1 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
    if arg0:
        # TODO: memory.copy

# ----------------------------------------------------------
# $func699
# ----------------------------------------------------------
def func699(arg0):
    store32(9671124, 1)
    store32(9242200, 0)
    store32(9242100, 0)
    store16(9242105, 0)
    store64(9242208, 0)
    store32(9263072, 9242084)
    store32(9242596, 0)
    store32(9242496, 0)
    store8(9242108, 0)
    store16(9242501, 0)
    store64(9242604, 0)
    store32(9263076, 9242480)
    store32(9242728, 0)
    store32(9242628, 0)
    store8(9242504, 0)
    store16(9242633, 0)
    store64(9242736, 0)
    store32(9263080, 9242612)
    store32(9242992, 0)
    store32(9242892, 0)
    store8(9242636, 0)
    store16(9242897, 0)
    store64(9243000, 0)
    store32(9263084, 9242876)
    store32(9243156, 0)
    store32(9243256, 0)
    store8(9242900, 0)
    store16(9243161, 0)
    store64(9243264, 0)
    store32(9263088, 9243140)
    store32(9243288, 0)
    store32(9243388, 0)
    store8(9243164, 0)
    store16(9243293, 0)
    store32(9243400, 0)
    store32(9243396, 0)
    store32(9263092, 9243272)
    store32(9243520, 0)
    store32(9243420, 0)
    store8(9243296, 0)
    store16(9243425, 0)
    store64(9243528, 0)
    store32(9263096, 9243404)
    store32(9243784, 0)
    store32(9243684, 0)
    store8(9243428, 0)
    store16(9243689, 0)
    store64(9243792, 0)
    store32(9263100, 9243668)
    store32(9262792, 0)
    store32(9262692, 0)
    store8(9243692, 0)
    store16(9262697, 0)
    store64(9262800, 0)
    store32(9263104, 9262676)
    store8(9262700, 0)
    store32(9671120, 9)
    a_b()

# ----------------------------------------------------------
# $func700
# ----------------------------------------------------------
def func700(arg0):
    store32(9671124, 1)
    store32(9242332, 0)
    store32(9242232, 0)
    store16(9242237, 0)
    store64(9242340, 0)
    store32(9263072, 9242216)
    store32(9250780, 0)
    store32(9250680, 0)
    store8(9242240, 0)
    store16(9250685, 0)
    store64(9250788, 0)
    store32(9263076, 9250664)
    store8(9250688, 0)
    store32(9250120, 0)
    store32(9250020, 0)
    store16(9250025, 0)
    store64(9250128, 0)
    store32(9263080, 9250004)
    store32(9250648, 0)
    store32(9250548, 0)
    store8(9250028, 0)
    store16(9250553, 0)
    store64(9250656, 0)
    store32(9263084, 9250532)
    store8(9250556, 0)
    store32(9248832, 0)
    store32(9248932, 0)
    store16(9248837, 0)
    store64(9248940, 0)
    store32(9263088, 9248816)
    store32(9249360, 0)
    store32(9249460, 0)
    store8(9248840, 0)
    store16(9249365, 0)
    store32(9249472, 0)
    store32(9249468, 0)
    store32(9263092, 9249344)
    store32(9250252, 0)
    store32(9250152, 0)
    store8(9249368, 0)
    store16(9250157, 0)
    store64(9250260, 0)
    store32(9263096, 9250136)
    store32(9251044, 0)
    store32(9250944, 0)
    store8(9250160, 0)
    store16(9250949, 0)
    store64(9251052, 0)
    store32(9263100, 9250928)
    store32(9243684, 0)
    store8(9250952, 0)
    store32(9243784, 0)
    store16(9243689, 0)
    store64(9243792, 0)
    store32(9263104, 9243668)
    store32(9262792, 0)
    store32(9262692, 0)
    store8(9243692, 0)
    store16(9262697, 0)
    store64(9262800, 0)
    store32(9263108, 9262676)
    store8(9262700, 0)
    store32(9671120, 10)
    a_b()

# ----------------------------------------------------------
# $func701
# ----------------------------------------------------------
def func701(arg0):
    store32(9671124, 1)
    store32(9242464, 0)
    store32(9242364, 0)
    store16(9242369, 0)
    store64(9242472, 0)
    store32(9263072, 9242348)
    store32(9250912, 0)
    store32(9250812, 0)
    store8(9242372, 0)
    store16(9250817, 0)
    store64(9250920, 0)
    store32(9263076, 9250796)
    store8(9250820, 0)
    store32(9242860, 0)
    store32(9242760, 0)
    store16(9242765, 0)
    store64(9242868, 0)
    store32(9263080, 9242744)
    store32(9243124, 0)
    store32(9243024, 0)
    store8(9242768, 0)
    store16(9243029, 0)
    store64(9243132, 0)
    store32(9263084, 9243008)
    store32(9248964, 0)
    store32(9249064, 0)
    store8(9243032, 0)
    store16(9248969, 0)
    store64(9249072, 0)
    store32(9263088, 9248948)
    store32(9249492, 0)
    store32(9249592, 0)
    store8(9248972, 0)
    store16(9249497, 0)
    store32(9249604, 0)
    store32(9249600, 0)
    store32(9263092, 9249476)
    store32(9243552, 0)
    store8(9249500, 0)
    store32(9243652, 0)
    store16(9243557, 0)
    store64(9243660, 0)
    store32(9263096, 9243536)
    store32(9250516, 0)
    store32(9250416, 0)
    store8(9243560, 0)
    store16(9250421, 0)
    store64(9250524, 0)
    store32(9263100, 9250400)
    store32(9262792, 0)
    store32(9262692, 0)
    store8(9250424, 0)
    store16(9262697, 0)
    store64(9262800, 0)
    store32(9263104, 9262676)
    store8(9262700, 0)
    store32(9671120, 9)
    a_b()

# ----------------------------------------------------------
# $func702
# ----------------------------------------------------------
def func702(arg0):
    store32(9671124, 1)
    store32(9244972, 0)
    store32(9244872, 0)
    store16(9244877, 0)
    store64(9244980, 0)
    store32(9263072, 9244856)
    store32(9245104, 0)
    store32(9245004, 0)
    store8(9244880, 0)
    store16(9245009, 0)
    store64(9245112, 0)
    store32(9263076, 9244988)
    store32(9245236, 0)
    store32(9245136, 0)
    store8(9245012, 0)
    store16(9245141, 0)
    store64(9245244, 0)
    store32(9263080, 9245120)
    store32(9245368, 0)
    store32(9245268, 0)
    store8(9245144, 0)
    store16(9245273, 0)
    store64(9245376, 0)
    store32(9263084, 9245252)
    store32(9245400, 0)
    store32(9245500, 0)
    store8(9245276, 0)
    store16(9245405, 0)
    store64(9245508, 0)
    store32(9263088, 9245384)
    store8(9245408, 0)
    store32(9671120, 5)
    a_b()

# ----------------------------------------------------------
# $func703
# ----------------------------------------------------------
def func703(arg0):
    store32(9671124, 1)
    store32(9248272, 0)
    store32(9248172, 0)
    store16(9248177, 0)
    store64(9248280, 0)
    store32(9263072, 9248156)
    store32(9249856, 0)
    store32(9249756, 0)
    store8(9248180, 0)
    store16(9249761, 0)
    store64(9249864, 0)
    store32(9263076, 9249740)
    store8(9249764, 0)
    store32(9245236, 0)
    store32(9245136, 0)
    store16(9245141, 0)
    store64(9245244, 0)
    store32(9263080, 9245120)
    store32(9245368, 0)
    store32(9245268, 0)
    store8(9245144, 0)
    store16(9245273, 0)
    store64(9245376, 0)
    store32(9263084, 9245252)
    store32(9245400, 0)
    store32(9245500, 0)
    store8(9245276, 0)
    store16(9245405, 0)
    store64(9245508, 0)
    store32(9263088, 9245384)
    store8(9245408, 0)
    store32(9671120, 5)
    a_b()

# ----------------------------------------------------------
# $func704
# ----------------------------------------------------------
def func704(arg0):
    store32(9671124, 1)
    store32(9248404, 0)
    store32(9248304, 0)
    store16(9248309, 0)
    store64(9248412, 0)
    store32(9263072, 9248288)
    store32(9249988, 0)
    store32(9249888, 0)
    store8(9248312, 0)
    store16(9249893, 0)
    store64(9249996, 0)
    store32(9263076, 9249872)
    store8(9249896, 0)
    store32(9245236, 0)
    store32(9245136, 0)
    store16(9245141, 0)
    store64(9245244, 0)
    store32(9263080, 9245120)
    store32(9245368, 0)
    store32(9245268, 0)
    store8(9245144, 0)
    store16(9245273, 0)
    store64(9245376, 0)
    store32(9263084, 9245252)
    store32(9245400, 0)
    store32(9245500, 0)
    store8(9245276, 0)
    store16(9245405, 0)
    store64(9245508, 0)
    store32(9263088, 9245384)
    store8(9245408, 0)
    store32(9671120, 5)
    a_b()

# ----------------------------------------------------------
# $func705
# ----------------------------------------------------------
def func705(arg0):
    store32(9671124, 1)
    store32(9258304, 0)
    store32(9258204, 0)
    store16(9258209, 0)
    store64(9258312, 0)
    store32(9263072, 9258188)
    store32(9258436, 0)
    store32(9258336, 0)
    store8(9258212, 0)
    store16(9258341, 0)
    store64(9258444, 0)
    store32(9263076, 9258320)
    store32(9258568, 0)
    store32(9258468, 0)
    store8(9258344, 0)
    store16(9258473, 0)
    store64(9258576, 0)
    store32(9263080, 9258452)
    store32(9258700, 0)
    store32(9258600, 0)
    store8(9258476, 0)
    store16(9258605, 0)
    store64(9258708, 0)
    store32(9263084, 9258584)
    store8(9258608, 0)
    store32(9671120, 4)
    a_b()

# ----------------------------------------------------------
# $func706
# ----------------------------------------------------------
def func706(arg0):
    store32(9671124, 1)
    store32(9243916, 0)
    store32(9243816, 0)
    store16(9243821, 0)
    store64(9243924, 0)
    store32(9263072, 9243800)
    store32(9244048, 0)
    store32(9243948, 0)
    store8(9243824, 0)
    store16(9243953, 0)
    store64(9244056, 0)
    store32(9263076, 9243932)
    store32(9244180, 0)
    store32(9244080, 0)
    store8(9243956, 0)
    store16(9244085, 0)
    store64(9244188, 0)
    store32(9263080, 9244064)
    store32(9244444, 0)
    store32(9244344, 0)
    store8(9244088, 0)
    store16(9244349, 0)
    store64(9244452, 0)
    store32(9263084, 9244328)
    store32(9244608, 0)
    store32(9244708, 0)
    store8(9244352, 0)
    store16(9244613, 0)
    store64(9244716, 0)
    store32(9263088, 9244592)
    store32(9244740, 0)
    store32(9244840, 0)
    store8(9244616, 0)
    store16(9244745, 0)
    store32(9244852, 0)
    store32(9244848, 0)
    store32(9263092, 9244724)
    store8(9244748, 0)
    store32(9671120, 6)
    a_b()

# ----------------------------------------------------------
# $func707
# ----------------------------------------------------------
def func707(arg0):
    store32(9671124, 1)
    store32(9248008, 0)
    store32(9247908, 0)
    store16(9247913, 0)
    store64(9248016, 0)
    store32(9263072, 9247892)
    store32(9248536, 0)
    store32(9248436, 0)
    store8(9247916, 0)
    store16(9248441, 0)
    store64(9248544, 0)
    store32(9263076, 9248420)
    store32(9248800, 0)
    store32(9248700, 0)
    store8(9248444, 0)
    store16(9248705, 0)
    store64(9248808, 0)
    store32(9263080, 9248684)
    store32(9249724, 0)
    store32(9249624, 0)
    store8(9248708, 0)
    store16(9249629, 0)
    store64(9249732, 0)
    store32(9263084, 9249608)
    store8(9249632, 0)
    store32(9249096, 0)
    store32(9249196, 0)
    store16(9249101, 0)
    store64(9249204, 0)
    store32(9263088, 9249080)
    store8(9249104, 0)
    store32(9247248, 0)
    store32(9247348, 0)
    store32(9247360, 0)
    store16(9247253, 0)
    store32(9247356, 0)
    store32(9263092, 9247232)
    store32(9261604, 0)
    store32(9261504, 0)
    store8(9247256, 0)
    store16(9261509, 0)
    store64(9261612, 0)
    store32(9263096, 9261488)
    store8(9261512, 0)
    store32(9671120, 7)
    a_b()

# ----------------------------------------------------------
# $func708
# ----------------------------------------------------------
def func708(arg0):
    store32(9671124, 1)
    store32(9248140, 0)
    store32(9248040, 0)
    store16(9248045, 0)
    store64(9248148, 0)
    store32(9263072, 9248024)
    store32(9248668, 0)
    store32(9248568, 0)
    store8(9248048, 0)
    store16(9248573, 0)
    store64(9248676, 0)
    store32(9263076, 9248552)
    store8(9248576, 0)
    store32(9244312, 0)
    store32(9244212, 0)
    store16(9244217, 0)
    store64(9244320, 0)
    store32(9263080, 9244196)
    store32(9244576, 0)
    store32(9244476, 0)
    store8(9244220, 0)
    store16(9244481, 0)
    store64(9244584, 0)
    store32(9263084, 9244460)
    store32(9249228, 0)
    store32(9249328, 0)
    store8(9244484, 0)
    store16(9249233, 0)
    store64(9249336, 0)
    store32(9263088, 9249212)
    store8(9249236, 0)
    store32(9247380, 0)
    store32(9247480, 0)
    store32(9247492, 0)
    store16(9247385, 0)
    store32(9247488, 0)
    store32(9263092, 9247364)
    store8(9247388, 0)
    store32(9671120, 6)
    a_b()

# ----------------------------------------------------------
# $func709
# ----------------------------------------------------------
def func709(arg0):
    store32(9671124, 1)
    while True:  # $label0
        v2 = (v1 << 2)
        arg0 = ((load32(((v1 << 2) + 1072)) * 132) + 9216080)
        store32(((load32(((v1 << 2) + 1072)) * 132) + 9216080) + 116, 0)
        store32(arg0 + 16, 0)
        store16(arg0 + 21, 0)
        store64(arg0 + 124, 0)
        store32((v2 + 9263072), arg0)
        store8(arg0 + 24, (u32(v1) > u32(7)))
        v1 = (v1 + 1)
        if ((v1 + 1) != 28):
            continue
        break
    store32(9671120, 28)

# ----------------------------------------------------------
# $func710
# ----------------------------------------------------------
def func710(arg0):
    store32(9671124, 1)
    while True:  # $label0
        v2 = (v1 << 2)
        arg0 = ((load32(((v1 << 2) + 1184)) * 132) + 9216080)
        store32(((load32(((v1 << 2) + 1184)) * 132) + 9216080) + 116, 0)
        store32(arg0 + 16, 0)
        store16(arg0 + 21, 0)
        store64(arg0 + 124, 0)
        store32((v2 + 9263072), arg0)
        store8(arg0 + 24, (u32(v1) > u32(7)))
        v1 = (v1 + 1)
        if ((v1 + 1) != 30):
            continue
        break
    store32(9671120, 30)

# ----------------------------------------------------------
# $func711
# ----------------------------------------------------------
def func711(arg0):
    store32(9671124, 1)
    while True:  # $label0
        v2 = (v1 << 2)
        arg0 = ((load32(((v1 << 2) + 1312)) * 132) + 9216080)
        store32(((load32(((v1 << 2) + 1312)) * 132) + 9216080) + 116, 0)
        store32(arg0 + 16, 0)
        store16(arg0 + 21, 0)
        store64(arg0 + 124, 0)
        store32((v2 + 9263072), arg0)
        store8(arg0 + 24, (u32(v1) > u32(7)))
        v1 = (v1 + 1)
        if ((v1 + 1) != 28):
            continue
        break
    store32(9671120, 28)

# ----------------------------------------------------------
# $func717
# ----------------------------------------------------------
def func717(arg0, arg1):
    v4 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v5 = load32(ENTITIES)
    v6 = entities[arg0]
    v3 = load8u(entities[arg0].unit_class)
    if (load8u(entities[arg0].unit_class) != 3):
        while True:  # $label0
            if (load8u(v6 + 128) == 2):
                if not (arg1 & 1):
                    break
                v2 = (v5 + (arg0 * 132))
                v3 = load32((v5 + (arg0 * 132)) + 72)
                if load32((v5 + (arg0 * 132)) + 72):
                    v3 = (v3 - 1)
                    store32(v2 + 72, (v3 - 1))
                    v7 = (players[load16u(v2 + 110)] + 281668)
                    store32((players[load16u(v2 + 110)] + 281668), (load32(v7) + 1))
                    if v3:
                        break
                store8(v2 + 127, 0)
                v3 = load32(v2 + 40)
                if load32(v2 + 40):
                    if load8u(9142916):
                        store32(v4 + 20, v3)
                        store32(v4 + 16, 0)
                        a_b()
                        store8(v6 + 128, 0)
                        break
                    v2 = load16u(v2 + 110)
                    store32(v4 + 4, v3)
                    store32(v4, (v2 + 16))
                    a_b()
                store8(v6 + 128, 0)
                break
            if (v3 == 8):
                v2 = (v5 + (arg0 * 132))
                v7 = players[load16u(v2 + 110)]
                v3 = (load32(v2 + 72) + load32((players[load16u(v2 + 110)] + 284068)))
                store32((v5 + (arg0 * 132)) + 72, (load32(v2 + 72) + load32((players[load16u(v2 + 110)] + 284068))))
                v9 = load8u(v2 + 123)
                v7 = load32(((v7 + (load32(((load8u(v2 + 123) * 40) + 9671200) + 8) << 2)) + 283984))
                if (u32(load32(((v7 + (load32(((load8u(v2 + 123) * 40) + 9671200) + 8) << 2)) + 283984))) > u32(v3)):
                    break
                while True:  # $label1
                    if (u32(v3) <= u32(load32(v2 + 76))):
                        break
                    v3 = (v5 + (arg0 * 132))
                    store8((v5 + (arg0 * 132)) + 127, 0)
                    if not load8u(9142916):
                        break
                    v3 = load32(v3 + 40)
                    if not load32(v3 + 40):
                        break
                    store32(v4 + 36, v3)
                    store32(v4 + 32, 0)
                    a_b()
                    break
                v8 = (v5 + (arg0 * 132))
                v3 = load32((v5 + (arg0 * 132)) + 32)
                while True:  # $label2
                    v9 = ((v9 * 40) + 9671200)
                    if not load8u(((v9 * 40) + 9671200) + 17):
                        break
                    v10 = load32(ENTITIES)
                    v11 = entities[v3]
                    v12 = (load16u(entities[v3].rally_y) - load16u(v8 + 112))
                    v8 = (load16u(v11 + 114) - load16u(v8 + 114))
                    v8 = load32(v9 + 4)
                    if (((((load16u(entities[v3].rally_y) - load16u(v8 + 112)) * v12) + ((load16u(v11 + 114) - load16u(v8 + 114)) * v8)) - 1) <= (load32(v9 + 4) * v8)):
                        if (load8u((v10 + (v3 * 132)) + 125) != 3):
                            break
                    func29(v6, 1)
                    break
                    break
                store32(v2 + 72, (load32(v2 + 72) - v7))
                v2 = (players[load16u(v2 + 110)] + 281668)
                store32((players[load16u(v2 + 110)] + 281668), (load32(v2) + v7))
                store8(v6 + 125, 0)
                break
            v6 = (v5 + (arg0 * 132))
            v2 = load32((v5 + (arg0 * 132)) + 72)
            v7 = load32(v6 + 76)
            if (u32(load32((v5 + (arg0 * 132)) + 72)) < u32(load32(v6 + 76))):
                if (v3 != 9):
                    v2 = (load32(((load32(PLAYERS) + (load16u((v5 + (arg0 * 132)) + 110) * 286704)) + 284068)) + v2)
                    store32(v6 + 72, (load32(((load32(PLAYERS) + (load16u((v5 + (arg0 * 132)) + 110) * 286704)) + 284068)) + v2))
                if (u32(v2) < u32(v7)):
                    break
            store32(v6 + 72, v7)
            break
        while True:  # $label3
            v2 = load32(9684420)
            arg0 = (v5 + (arg0 * 132))
            if (load32(9684420) != load32((v5 + (arg0 * 132)) + 28)):
                break
            if not load32(arg0 + 92):
                break
            if load32(9140316):
                if (load32(9140320) != v2):
                    break
            break
        v5 = load32(9215884)
        v2 = (load32(9215884) + (load32(9671116) << 2))
        # TODO: i32.div_u
        store32(load32(v2), (load32((players[load16u(arg0 + 110)] + 284156)) + 25))
        store32((v5 + (load32(9671116) << 2)) + 12, (arg1 + 1))
    G.global0 = (v4 + 48)

# ----------------------------------------------------------
# $tc
# Export: tc
# ----------------------------------------------------------
def tc():
    """Export: tc"""
    v8 = load32(9671136)
    v6 = func26((-1 if (u32(v8) > u32(1073741823)) else (load32(9671136) << 2)))
    while True:  # $label0
        if (u32(v8) <= u32(3)):
            store32(9671136, 3)
            break
        v5 = load32(ENTITIES)
        v0 = 3
        v1 = 3
        while True:  # $label3
            while True:  # $label1
                v7 = (v1 * 132)
                v2 = (v5 + (v1 * 132))
                if (load8u((v5 + (v1 * 132)) + 125) == 3):
                    break
                if (v0 != v1):
                    if (u32(v0) >= u32(v1)):
                        break
                    while True:  # $label2
                        v3 = (v0 * 132)
                        v4 = (v5 + (v0 * 132))
                        if (load8u((v5 + (v0 * 132)) + 125) == 3):
                            v8 = load32(9671136)
                            v5 = load32(ENTITIES)
                            # TODO: memory.copy
                            store32((v3 + v5) + 28, v0)
                            store8((v5 + v7) + 125, 3)
                            store32((v6 + (v1 << 2)), v0)
                            v0 = (v0 + 1)
                            break
                        v0 = (v0 + 1)
                        if ((v0 + 1) != v1):
                            continue
                        break
                    v0 = v1
                    break
                store32((v6 + (v0 << 2)), v0)
                v0 = (v0 + 1)
                break
            v1 = (v1 + 1)
            if (u32((v1 + 1)) < u32(v8)):
                continue
            break
        store32(9671136, v0)
        if (u32(v0) < u32(4)):
            break
        v7 = load32(ENTITIES)
        v2 = 3
        while True:  # $label6
            v3 = (v7 + (v2 * 132))
            v1 = load32((v7 + (v2 * 132)) + 36)
            if load32((v7 + (v2 * 132)) + 36):
                store32(v3 + 36, load32((v6 + (v1 << 2))))
            while True:  # $label4
                v4 = load32(v3 + 16)
                if not load32(v3 + 16):
                    break
                if not load32(v4 + 8):
                    break
                v3 = load32(v4)
                v0 = 0
                while True:  # $label5
                    v1 = (v3 + (v0 << 2))
                    store32((v3 + (v0 << 2)), load32((v6 + (load32(v1) << 2))))
                    v0 = (v0 + 1)
                    if (u32((v0 + 1)) < u32(load32(v4 + 8))):
                        continue
                    break
                v0 = load32(9671136)
                break
            v2 = (v2 + 1)
            if (u32((v2 + 1)) < u32(v0)):
                continue
            break
        break
    store32(9215892, 4)
    if load32(PLAYER_COUNT):
        v7 = load32(PLAYERS)
        v4 = 0
        while True:  # $label10
            v2 = (v7 + (v4 * 286704))
            v1 = load32((v7 + (v4 * 286704)) + 281788)
            if load32((v7 + (v4 * 286704)) + 281788):
                store32(v1 + 8, 0)
            v1 = load32(v2 + 281792)
            if load32(v2 + 281792):
                store32(v1 + 8, 0)
            v1 = load32(v2 + 281796)
            if load32(v2 + 281796):
                store32(v1 + 8, 0)
            v0 = 0
            while True:  # $label7
                v3 = (v2 + (v0 << 2))
                store32(((v2 + (v0 << 2)) + 282828), 0)
                v1 = load32((v3 + 284636))
                if load32((v3 + 284636)):
                    store32(v1 + 8, 0)
                if load32((v3 + 285656)):
                    store32(v1 + 8, 0)
                v0 = (v0 + 1)
                if ((v0 + 1) != 255):
                    continue
                break
            v0 = 0
            v1 = load32(PLAYER_COUNT)
            while True:  # $label8
                v3 = load32(v2 + 281800)
                if not load32(v2 + 281800):
                    break
                if not v1:
                    break
                while True:  # $label9
                    store32((v3 + (v0 << 2)), 0)
                    v0 = (v0 + 1)
                    v1 = load32(PLAYER_COUNT)
                    if (u32((v0 + 1)) < u32(load32(PLAYER_COUNT))):
                        continue
                    break
                break
            store16(v2 + 286700, 0)
            v4 = (v4 + 1)
            if (u32((v4 + 1)) < u32(v1)):
                continue
            break
    v5 = 3
    if (u32(load32(9671136)) > u32(3)):
        while True:  # $label12
            v0 = entities[v5]
            func157(entities[v5])
            v1 = load32(v0 + 20)
            if load32(v0 + 20):
                store32(v1 + 8, 0)
            store32(v0 + 44, 0)
            if (load8u(v0 + 125) != 4):
                store8(v0 + 125, 0)
            store8(v0 + 123, 0)
            store16(v0 + 108, 0)
            store32(v0 + 88, 0)
            store32(v0 + 96, 0)
            while True:  # $label11
                if (load8u(v0 + 126) != 1):
                    break
                v1 = entities[load32(v0 + 28)]
                store8(entities[load32(v0 + 28)] + 126, 0)
                # TODO: i32.div_u
                store32(load32(v1 + 52) + 52, ((load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 296) * load32((players[load16u(v1 + 110)] + 284144))) - 100))
                if not load32(v1 + 92):
                    break
                if load32(9140316):
                    if (load32(9140320) != load32(v1 + 28)):
                        break
                break
            store64(v0 + 100, 0)
            store32(v0 + 56, 0)
            store16(v0 + 127, 0)
            store32(v0 + 32, -1)
            v1 = 8
            if (load8u(v0 + 129) != 8):
                store8(v0 + 129, 0)
                v1 = 0
            func144(players[load16u(v0 + 110)], load32(v0 + 28), 0)
            v5 = (v5 + 1)
            if (u32((v5 + 1)) < u32(load32(9671136))):
                continue
            break

# ----------------------------------------------------------
# $func719
# ----------------------------------------------------------
def func719(arg0, arg1, arg2):
    v6 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    if arg2:
        v11 = load32(arg0)
        arg0 = 0
        while True:  # $label9
            while True:  # $label0
                while True:  # $label1
                    v3 = entities[load32((arg1 + (arg0 << 2)))]
                    # br_table (load8u(entities[load32((arg1 + (arg0 << 2)))].unit_class) - 3)
                    break
                    break
                v8 = load8u(v3 + 128)
                v4 = load16u(v3 + 110)
                v5 = load32(PLAYERS)
                while True:  # $label2
                    v7 = (load32(38676) == load8u(v3 + 122))
                    if not (load32(38676) == load8u(v3 + 122)):
                        v9 = ((v5 + (v4 * 286704)) + 284176)
                        break
                    v9 = ((v5 + (v4 * 286704)) + 284312)
                    if not v8:
                        break
                    if (v11 != 2):
                        break
                    store8(v3 + 127, 0)
                    v5 = load32(v3 + 40)
                    if load32(v3 + 40):
                        if load8u(9142916):
                            store32(v6 + 20, v5)
                            store32(v6 + 16, 0)
                            a_b()
                            store8(v3 + 128, 0)
                            break
                        store32(v6 + 4, v5)
                        store32(v6, (v4 + 16))
                        a_b()
                    store8(v3 + 128, 0)
                    break
                    break
                v9 = load32(v9)
                if (u32(load32(v9)) > u32(load32(v3 + 72))):
                    break
                if (v11 == 2):
                    break
                while True:  # $label3
                    while True:  # $label4
                        if not v8:
                            func296(v3, (2 if v7 else 1))
                            if v7:
                                break
                            v4 = load16u(v3 + 110)
                            v5 = load32(PLAYERS)
                            break
                        if v7:
                            break
                        break
                    v8 = load32(((v5 + ((v4 & 65535) * 286704)) + 284204))
                    while True:  # $label7
                        while True:  # $label5
                            v13 = load32(9215892)
                            if not load32(9215892):
                                v5 = load32(v3 + 28)
                                break
                            v5 = load32(v3 + 28)
                            v4 = 0
                            v12 = load32(9142848)
                            v7 = load32(9215884)
                            while True:  # $label8
                                while True:  # $label6
                                    v10 = (v4 << 2)
                                    if (load32((v7 + ((v4 << 2) | 4))) != 21):
                                        break
                                    if (load32((v7 + (v10 | 8))) != v5):
                                        break
                                    v10 = (v7 + v10)
                                    if (u32(load32((v7 + v10))) > u32(v12)):
                                        break
                                    break
                                v4 = (v4 + 4)
                                if (u32((v4 + 4)) < u32(v13)):
                                    continue
                                break
                            break
                        break
                        break
                    # TODO: i32.div_u
                    store32(v12, (v8 + 25))
                    break
                v4 = (players[load16u(v3 + 110)] + 281668)
                store32((players[load16u(v3 + 110)] + 281668), (load32(v4) + v9))
                store32(v3 + 72, (load32(v3 + 72) - v9))
                if not load32(v3 + 92):
                    break
                v4 = load8u(9147141)
                if load32(9140316):
                    if (load32(9140320) != load32(v3 + 28)):
                        break
                break
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break
    G.global0 = (v6 + 32)

# ----------------------------------------------------------
# $func721
# ----------------------------------------------------------
def func721(arg0, arg1):
    arg1 = (G.global0 - 112)
    G.global0 = (G.global0 - 112)
    v2 = load32(ENTITIES)
    v3 = entities[arg0]
    v8 = load16u(v3 + 116)
    v5 = load16u(v3 + 118)
    while True:  # $label0
        v3 = load32(9142440)
        if (u32(load32(9142440)) <= u32(v5)):
            break
        if (u32(v3) <= u32(v8)):
            break
        if not load32(9142832):
            if not load32(load32(GAME_STATE) + 48):
                break
        arg0 = (v2 + (arg0 * 132))
        v9 = (v2 + (arg0 * 132))
        v3 = load32(CURRENT_PLAYER)
        arg0 = load16u(arg0 + 110)
        if (load32(CURRENT_PLAYER) == load16u(arg0 + 110)):
            store32(arg1 + 96, load32(39936))
            a_b()
            v3 = load32(CURRENT_PLAYER)
            arg0 = load16u(v9 + 110)
        while True:  # $label1
            if not load8u((load32(9143012) + ((load32(PLAYER_COUNT) * arg0) + v3))):
                v3 = -1
                break
            while True:  # $label2
                if not load32(load32(GAME_STATE) + 48):
                    break
                v3 = 0
                v10 = load32(9142836)
                v6 = load32(load32(9142836) + 964)
                if not load32(load32(9142836) + 964):
                    break
                while True:  # $label4
                    while True:  # $label3
                        v11 = load32(9142440)
                        v2 = load32(v10 + 960)
                        v4 = (v3 << 2)
                        v7 = load32((load32(v10 + 960) + ((v3 << 2) | 4)))
                        arg0 = (load32((load32(v10 + 960) + ((v3 << 2) | 4))) + v5)
                        if (u32(load32(9142440)) <= u32((load32((load32(v10 + 960) + ((v3 << 2) | 4))) + v5))):
                            break
                        v4 = load32((v2 + v4))
                        v2 = (load32((v2 + v4)) + v8)
                        if (u32(v11) <= u32((load32((v2 + v4)) + v8))):
                            break
                        if ((arg0 | v2) < 0):
                            break
                        if ((((v4 * v4) + (v7 * v7)) - 1) <= 64):
                            break
                        func258(v2, arg0)
                        break
                    v3 = (v3 + 2)
                    if (u32((v3 + 2)) < u32(v6)):
                        continue
                    break
                break
            v3 = 0
            if not load8u(59181):
                break
            while True:  # $label5
                if load8u(9142917):
                    break
                arg0 = load32(9299880)
                if load32(9299880):
                    arg0 = (arg0 - 1)
                    store32(9299880, (arg0 - 1))
                    v3 = load32((load32(9299872) + (arg0 << 2)))
                    break
                v3 = load32(9163776)
                arg0 = (load32(9163776) + 1)
                store32(9163776, (load32(9163776) + 1))
                v2 = load32(9163784)
                if (u32(arg0) < u32(load32(9163784))):
                    break
                store32(arg1 + 80, v2)
                a_b()
                store32(9163784, (load32(9163784) + 40000))
                break
            v7 = (v8 << 5)
            if load8u(9142916):
                v4 = (load32(9142440) * 96)
                arg0 = 0
                while True:  # $label6
                    v2 = load32(9142584)
                    if not load32(9142584):
                        break
                    if not load32(v2 + 20):
                        break
                    arg0 = load32(v2 + 28)
                    if (load32(v2 + 28) != 2147483647):
                        break
                    arg0 = load32(59152)
                    store32(59152, (load32(59152) + 1))
                    v6 = load32(9568052)
                    store32(v2 + 28, arg0)
                    v11 = load32(v2)
                    v10 = load32(v2 + 4)
                    v12 = load32(9568048)
                    store32(9568048, (load32(9568048) + 1))
                    store32(((v12 << 2) + 9563952), v2)
                    store32(9568052, (v6 + ((v11 * (v10 + 2)) << 2)))
                    v6 = load32(9568056)
                    store32(v2 + 56, load32(9568056))
                    store32(9568056, (v6 + ((v10 * load32(v2)) << 2)))
                    break
                v13 = i32(v4)
                v2 = (load32(9142848) * 25)
                v9 = load16u(v9 + 110)
                store32(arg1 + 76, v3)
                store32(arg1 + 72, 0)
                store32((arg1 - -64), 65535)
                store64(arg1 + 56, 0)
                store32(arg1 + 52, v2)
                store32(arg1 + 48, arg0)
                store64(arg1 + 40, 0)
                store64(arg1 + 32, 0)
                store64(arg1 + 24, 0)
                # TODO: f64.promote_f32
                storef64(arg1 + 16, ((((v13 * 0.5) / v13) + 0.25) if v4 else v13))
                store32(arg1 + 68, ((v9 << 16) | 54))
                storef64(arg1 + 8, i32((v5 << 5)))
                storef64(arg1, i32(v7))
                a_b()
                break
            break
        break
    G.global0 = (arg1 + 112)

# ----------------------------------------------------------
# $func723
# ----------------------------------------------------------
def func723(arg0, arg1):
    v2 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v6 = load32(ENTITIES)
    v7 = entities[arg0]
    while True:  # $label0
        if (u32(load32(9142848)) < u32((load32(load32(GAME_STATE) + 72) * 2400))):
            func29(v7, 1)
            break
        while True:  # $label1
            if (load8u(v7 + 125) == 3):
                break
            v3 = (v6 + (arg0 * 132))
            if not load8u((v6 + (arg0 * 132)) + 128):
                break
            store8(v3 + 127, 0)
            while True:  # $label2
                v8 = load32(v3 + 40)
                if not load32(v3 + 40):
                    break
                if load8u(9142916):
                    store32(v2 + 36, v8)
                    store32(v2 + 32, 0)
                    a_b()
                    break
                v4 = load16u(v3 + 110)
                store32(v2 + 20, v8)
                store32(v2 + 16, (v4 + 16))
                a_b()
                break
            store8(v3 + 128, 0)
            break
        v8 = load32(ENTITIES)
        v3 = entities[arg1]
        v4 = load16u(v3 + 114)
        v5 = load16u(v3 + 112)
        while True:  # $label4
            while True:  # $label3
                v10 = load32(load32(GAME_STATE) + 48)
                if not load32(load32(GAME_STATE) + 48):
                    break
                if load8u(9147152):
                    break
                v9 = load16u((load32(9147376) + (((load32(9142440) * v4) + v5) << 1)))
                if (v10 == 2):
                    if (u32(v9) > u32(1)):
                        break
                    break
                if not v9:
                    break
                break
            v5 = ((load8u(v3 + 122) * 404) + ENTITY_TYPES)
            func375(((v5 + ((load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1)) << 5), ((((load32(v5 + 220) & 0xFFFFFFFF) >> 1) + v4) << 5))
            break
        while True:  # $label5
            v6 = (v6 + (arg0 * 132))
            arg0 = load16u((v6 + (arg0 * 132)) + 112)
            v4 = ((load16u((v6 + (arg0 * 132)) + 112) << 5) - load32(9142952))
            v4 = load16u(v6 + 114)
            v5 = ((load16u(v6 + 114) << 5) - load32(9142956))
            if ((((((load16u((v6 + (arg0 * 132)) + 112) << 5) - load32(9142952)) * v4) + (((load16u(v6 + 114) << 5) - load32(9142956)) * v5)) - 1) > 9000000):
                break
            while True:  # $label6
                v9 = load32(load32(GAME_STATE) + 48)
                if not load32(load32(GAME_STATE) + 48):
                    break
                if load8u(9147152):
                    break
                v5 = load16u((load32(9147376) + (((load32(9142440) * v4) + arg0) << 1)))
                if (v9 == 2):
                    if (u32(v5) > u32(1)):
                        break
                    break
                if not v5:
                    break
                break
            store32(v2 + 8, v4)
            store32(v2 + 4, arg0)
            store32(v2, load32(((((load32(9142848) + arg0) & 1) << 2) + 57612)))
            a_b()
            break
        arg0 = (load32(((load8u((v8 + (arg1 * 132)) + 122) * 404) + ENTITY_TYPES) + 308) * load32((players[load16u(v6 + 110)] + 284224)))
        # TODO: i32.div_u
        break
    G.global0 = (v2 + 48)
    return func81(v7, 1, ((load32(((load8u((v8 + (arg1 * 132)) + 122) * 404) + ENTITY_TYPES) + 308) * load32((players[load16u(v6 + 110)] + 284224))) if (u32(arg0) < u32(100)) else 100), 1)

# ----------------------------------------------------------
# $func725
# ----------------------------------------------------------
def func725(arg0, arg1, arg2):
    while True:  # $label0
        arg0 = load32(ENTITIES)
        v5 = (arg0 + (load32(arg1) * 132))
        arg1 = load32((arg0 + (load32(arg1) * 132)) + 36)
        v3 = entities[load32((arg0 + (load32(arg1)]
        arg2 = load8u(entities[load32((arg0 + (load32(arg1)].sub_state)
        if (load8u(entities[load32((arg0 + (load32(arg1)].sub_state) == load32(38528)):
            break
        while True:  # $label1
            v4 = load8u(v5 + 122)
            if not load32(((load8u(v5 + 122) * 404) + ENTITY_TYPES) + 268):
                if not load8u(((arg2 * 404) + ENTITY_TYPES) + 335):
                    break
                func376(v5, v3)
                break
            v6 = (arg0 + (arg1 * 132))
            if not load32((arg0 + (arg1 * 132)) + 72):
                break
            while True:  # $label3
                while True:  # $label2
                    arg0 = load32(v6 + 24)
                    if not load32(v6 + 24):
                        break
                    arg1 = load32(arg0)
                    if not load32(arg0):
                        break
                    arg0 = load32(arg1)
                    if load32(arg1):
                        break
                    break
                arg1 = func26(16)
                v7 = ((arg2 * 404) + ENTITY_TYPES)
                arg2 = load32(((arg2 * 404) + ENTITY_TYPES) + 236)
                arg0 = (load32(((arg2 * 404) + ENTITY_TYPES) + 236) + 2)
                store32(func26(16) + 4, (load32(((arg2 * 404) + ENTITY_TYPES) + 236) + 2))
                arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                store32(arg1, func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2))))
                store64(arg1 + 8, 4294967296)
                if arg2:
                    v3 = 0
                    v4 = 0
                    while True:  # $label5
                        v8 = load32((load32(v7 + 232) + (v4 << 2)))
                        while True:  # $label4
                            if (load32(arg1 + 4) != v3):
                                arg2 = arg0
                                break
                            arg2 = (load32(arg1 + 12) + v3)
                            store32(arg1 + 4, (load32(arg1 + 12) + v3))
                            arg2 = func26((-1 if (u32(arg2) > u32(1073741823)) else (arg2 << 2)))
                            if v3:
                                # TODO: memory.copy
                            store32(arg1, arg2)
                            break
                        store32(arg1 + 8, (v3 + 1))
                        store32((arg2 + (v3 << 2)), v8)
                        v4 = (v4 + 1)
                        if (u32((v4 + 1)) < u32(load32(v7 + 236))):
                            v3 = load32(arg1 + 8)
                            arg0 = arg2
                            continue
                        break
                    arg0 = arg2
                v3 = load32(v6 + 24)
                if not load32(v6 + 24):
                    v3 = func26(16)
                    store64(func26(16), 0)
                    store64(v3 + 8, 0)
                    store32(v6 + 24, v3)
                store32(v3, arg1)
                v4 = load8u(v5 + 122)
                break
            v4 = load32(((v4 * 404) + ENTITY_TYPES) + 172)
            arg2 = load32(arg1 + 8)
            if load32(arg1 + 8):
                v3 = 0
                while True:  # $label6
                    if (load32((arg0 + (v3 << 2))) == v4):
                        break
                    v3 = (v3 + 1)
                    if ((v3 + 1) != arg2):
                        continue
                    break
            while True:  # $label7
                if (load32(arg1 + 4) != arg2):
                    v3 = arg0
                    break
                v3 = (load32(arg1 + 12) + arg2)
                store32(arg1 + 4, (load32(arg1 + 12) + arg2))
                v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                if arg2:
                    # TODO: memory.copy
                store32(arg1, v3)
                arg2 = load32(arg1 + 8)
                break
            store32(arg1 + 8, (arg2 + 1))
            store32((v3 + (arg2 << 2)), v4)
            break
        break

# ----------------------------------------------------------
# $func726
# ----------------------------------------------------------
def func726(arg0, arg1):
    v3 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v6 = ((arg0 & 0xFFFFFFFF) >> 16)
    v4 = (((arg0 & 0xFFFFFFFF) >> 16) << 5)
    v2 = (arg0 * v6)
    v10 = i32((((((arg0 & 0xFFFFFFFF) >> 16) << 5) | (((arg0 * v6) * v6) & 31)) - 16))
    v8 = (arg0 & 65535)
    v5 = ((arg0 & 65535) << 5)
    v11 = i32(((((arg0 & 65535) << 5) | ((arg0 * v2) & 31)) - 16))
    v2 = 0
    while True:  # $label0
        if load8u(9142917):
            break
        v2 = load32(9299880)
        if load32(9299880):
            v2 = (v2 - 1)
            store32(9299880, (v2 - 1))
            v2 = load32((load32(9299872) + (v2 << 2)))
            break
        v2 = load32(9163776)
        v7 = (load32(9163776) + 1)
        store32(9163776, (load32(9163776) + 1))
        v9 = load32(9163784)
        if (u32(v7) < u32(load32(9163784))):
            break
        store32(v3 + 16, v9)
        a_b()
        store32(9163784, (load32(9163784) + 40000))
        break
    while True:  # $label1
        v5 = (v5 - load32(9142952))
        v4 = (v4 - load32(9142956))
        if (((((v5 - load32(9142952)) * v5) + ((v4 - load32(9142956)) * v4)) - 1) > 9000000):
            break
        v5 = load32(39828)
        while True:  # $label2
            v7 = load32(load32(GAME_STATE) + 48)
            if not load32(load32(GAME_STATE) + 48):
                break
            if load8u(9147152):
                break
            v4 = load16u((load32(9147376) + (((load32(9142440) * v6) + v8) << 1)))
            if (v7 == 2):
                if (u32(v4) > u32(1)):
                    break
                break
            if not v4:
                break
            break
        store32(v3 + 8, v6)
        store32(v3 + 4, v8)
        store32(v3, v5)
        a_b()
        break
    while True:  # $label3
        if ((v10 < 4294967300.0) & (v10 >= 0.0)):
            break
        break
    arg0 = 0
    while True:  # $label4
        if ((v11 < 4294967300.0) & (v11 >= 0.0)):
            break
        break
    G.global0 = (v3 + 32)
    return func113(607, v2)

# ----------------------------------------------------------
# $fc
# Export: fc
# ----------------------------------------------------------
def fc(arg0):
    """Export: fc"""
    arg0 = 0
    while True:  # $label0
        v2 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v1 = 1
        v3 = (v2 - 1)
        v6 = ((v2 - 1) & 1)
        v4 = load32(PLAYERS)
        if (v2 != 2):
            v3 = (v3 & -2)
            v2 = 0
            while True:  # $label1
                v5 = (v4 + (v1 * 286704))
                if load32((v4 + (v1 * 286704)) + 284616):
                    arg0 = (arg0 + not load8u(v5 + 286696))
                v5 = (v4 + ((v1 + 1) * 286704))
                if load32((v4 + ((v1 + 1) * 286704)) + 284616):
                    arg0 = (arg0 + not load8u(v5 + 286696))
                v1 = (v1 + 2)
                v2 = (v2 + 2)
                if ((v2 + 2) != v3):
                    continue
                break
        if not v6:
            break
        v1 = (v4 + (v1 * 286704))
        if not load32((v4 + (v1 * 286704)) + 284616):
            break
        arg0 = (arg0 + not load8u(v1 + 286696))
        break
    return arg0

# ----------------------------------------------------------
# $func731
# ----------------------------------------------------------
def func731(arg0, arg1):
    while True:  # $label0
        if load8u(9147141):
            break
        if not arg0:
            break
        if not load8u(9163793):
            break
        arg0 = 0
        v2 = 40928
        v3 = 40
        while True:  # $label1
            while True:  # $label3
                while True:  # $label2
                    v4 = load32(PLAYERS)
                    v5 = load32(CURRENT_PLAYER)
                    # br_table load32(players[load32(CURRENT_PLAYER)] + 283960)
                    break
                    break
                v2 = 40784
                v3 = 36
                break
                break
            v2 = 40624
            v3 = 38
            break
        arg1 = load32(((arg1 << 2) + 9684832))
        while True:  # $label4
            if (arg1 != load32((v2 + (arg0 << 2)))):
                arg0 = (arg0 + 2)
                if (u32((arg0 + 2)) < u32(v3)):
                    continue
                break
            break
        arg0 = load32((v2 + ((arg0 << 2) | 4)))
        func45()
        while True:  # $label5
            arg1 = load32((((v4 + (v5 * 286704)) + (load32(((arg0 * 132) + 9216080) + 4) << 2)) + 284636))
            if not load32((((v4 + (v5 * 286704)) + (load32(((arg0 * 132) + 9216080) + 4) << 2)) + 284636)):
                break
            v2 = load32(arg1 + 8)
            if not load32(arg1 + 8):
                break
            arg0 = 0
            while True:  # $label6
                v3 = load32((load32(arg1) + (arg0 << 2)))
                if load32((load32(arg1) + (arg0 << 2))):
                    func44(entities[v3], 0)
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v2):
                    continue
                break
            break
        store32(9685860, (load32(9685860) + 1))
        break

# ----------------------------------------------------------
# $func732
# ----------------------------------------------------------
def func732(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if (load32(((arg0 * 404) + ENTITY_TYPES) + 368) == 55):
            store32(v1 + 12, arg0)
            arg0 = load32(9213808)
            if load8u(9147210):
                func41(2, 9173808, arg0, (v1 + 12), 1)
                break
            v3 = (arg0 << 2)
            v2 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if arg0:
                # TODO: memory.copy
            break
        func242(arg0)
        break
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $func734
# ----------------------------------------------------------
def func734(arg0, arg1):
    v2 = load32(ENTITIES)
    v3 = entities[arg0]
    arg0 = (v2 + (arg1 * 132))
    if not load8u(arg0 + 128):
        func296(arg0, 1)
    v3 = load32((players[load16u(v3 + 110)] + 284204))
    while True:  # $label2
        while True:  # $label0
            v6 = load32(9215892)
            if not load32(9215892):
                arg1 = load32((v2 + (arg1 * 132)) + 28)
                break
            arg1 = load32((v2 + (arg1 * 132)) + 28)
            arg0 = 0
            v5 = load32(9142848)
            v2 = load32(9215884)
            while True:  # $label3
                while True:  # $label1
                    v4 = (arg0 << 2)
                    if (load32((v2 + ((arg0 << 2) | 4))) != 21):
                        break
                    if (load32((v2 + (v4 | 8))) != arg1):
                        break
                    v4 = (v2 + v4)
                    if (u32(load32((v2 + v4))) > u32(v5)):
                        break
                    break
                arg0 = (arg0 + 4)
                if (u32((arg0 + 4)) < u32(v6)):
                    continue
                break
            break
        return
        break
    # TODO: i32.div_u
    store32(v5, (v3 + 25))

# ----------------------------------------------------------
# $func736
# ----------------------------------------------------------
def func736(arg0, arg1):
    v2 = load32(ENTITIES)
    arg1 = entities[arg0]
    func238(arg1, load16u(entities[arg0] + 110), arg0)
    func29(arg1, 1)
    while True:  # $label0
        if not load32(arg1 + 92):
            break
        arg1 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32((v2 + (arg0 * 132)) + 28)):
                break
        break

# ----------------------------------------------------------
# $func737
# ----------------------------------------------------------
def func737(arg0, arg1):
    v2 = ((arg1 * 404) + ENTITY_TYPES)
    v3 = load32(((arg1 * 404) + ENTITY_TYPES) + 236)
    if load32(((arg1 * 404) + ENTITY_TYPES) + 236):
        v7 = players[arg0]
        while True:  # $label5
            while True:  # $label0
                v9 = load32((load32(v2 + 232) + (v5 << 2)))
                v6 = load32(((v7 + (load32((load32(v2 + 232) + (v5 << 2))) << 2)) + 284636))
                if not load32(((v7 + (load32((load32(v2 + 232) + (v5 << 2))) << 2)) + 284636)):
                    break
                arg0 = 0
                v8 = load32(v6 + 8)
                if not load32(v6 + 8):
                    break
                while True:  # $label4
                    arg1 = load32((load32(v6) + (arg0 << 2)))
                    if load32((load32(v6) + (arg0 << 2))):
                        arg1 = entities[arg1]
                        store32(entities[arg1].speed, (load32(arg1 + 52) + load32(v2 + 92)))
                        store32(arg1 + 60, (load32(arg1 + 60) + load32(v2 + 100)))
                        store32(arg1 + 84, (load32(arg1 + 84) + load32(v2 + 112)))
                        v3 = load32(arg1 + 68)
                        while True:  # $label1
                            while True:  # $label2
                                # br_table (load8u(arg1 + 125) - 4)
                                break
                                break
                            v4 = load32(arg1 + 64)
                            # TODO: i32.div_u
                            store32((load32(arg1 + 64) * load32(v2 + 104)) + 64, ((1 if (u32(v3) <= u32(1)) else v3) + v4))
                            break
                        store32(arg1 + 68, (load32(v2 + 104) + v3))
                        v4 = load32(arg1 + 72)
                        while True:  # $label3
                            v3 = load32(v2 + 120)
                            if not load32(v2 + 120):
                                break
                            if v4:
                                break
                            v8 = load32(v6 + 8)
                            v4 = load32(arg1 + 72)
                            v3 = load32(v2 + 120)
                            break
                        store32(arg1 + 72, (v3 + v4))
                        store32(arg1 + 76, (load32(arg1 + 76) + v3))
                    arg0 = (arg0 + 1)
                    if (u32((arg0 + 1)) < u32(v8)):
                        continue
                    break
                v3 = load32(v2 + 236)
                break
            arg0 = (v7 + (v9 * 36))
            arg1 = ((v7 + (v9 * 36)) + 269380)
            store32(((v7 + (v9 * 36)) + 269380), (load32(arg1) + load32(v2 + 92)))
            arg1 = (arg0 + 269384)
            store32((arg0 + 269384), (load32(arg1) + load32(v2 + 100)))
            arg1 = (arg0 + 269396)
            store32((arg0 + 269396), (load32(arg1) + load32(v2 + 112)))
            arg1 = (arg0 + 269388)
            store32((arg0 + 269388), (load32(arg1) + load32(v2 + 104)))
            arg1 = (arg0 + 269392)
            store32((arg0 + 269392), (load32(arg1) + load32(v2 + 108)))
            arg0 = (arg0 + 269404)
            store32((arg0 + 269404), (load32(arg0) + load32(v2 + 120)))
            v5 = (v5 + 1)
            if (u32((v5 + 1)) < u32(v3)):
                continue
            break

# ----------------------------------------------------------
# $func738
# ----------------------------------------------------------
def func738(arg0, arg1):
    v2 = ((arg1 * 404) + ENTITY_TYPES)
    v3 = load32(((arg1 * 404) + ENTITY_TYPES) + 236)
    if load32(((arg1 * 404) + ENTITY_TYPES) + 236):
        v8 = players[arg0]
        while True:  # $label5
            v9 = load32((load32(v2 + 232) + (v5 << 2)))
            arg0 = ((load32((load32(v2 + 232) + (v5 << 2))) * 404) + ENTITY_TYPES)
            # TODO: i32.div_u
            v6 = 100
            # TODO: i32.div_u
            v10 = 100
            # TODO: i32.div_u
            v11 = 100
            # TODO: i32.div_u
            v12 = 100
            # TODO: i32.div_u
            v4 = 100
            while True:  # $label0
                v7 = load32(((v8 + (v9 << 2)) + 284636))
                if not load32(((v8 + (v9 << 2)) + 284636)):
                    break
                arg0 = 0
                v13 = load32(v7 + 8)
                if not load32(v7 + 8):
                    break
                while True:  # $label4
                    arg1 = load32((load32(v7) + (arg0 << 2)))
                    if load32((load32(v7) + (arg0 << 2))):
                        while True:  # $label1
                            while True:  # $label2
                                arg1 = entities[arg1]
                                # br_table (load8u(entities[arg1].unit_class) - 4)
                                break
                                break
                            store32(arg1 + 64, (load32(arg1 + 64) + v4))
                            break
                        store32(arg1 + 68, (load32(arg1 + 68) + v4))
                        store32(arg1 + 52, (load32(arg1 + 52) + v12))
                        store32(arg1 + 60, (load32(arg1 + 60) + v11))
                        store32(arg1 + 84, (load32(arg1 + 84) + v10))
                        v3 = load32(arg1 + 72)
                        while True:  # $label3
                            if not load32(v2 + 120):
                                break
                            if v3:
                                break
                            v13 = load32(v7 + 8)
                            v3 = load32(arg1 + 72)
                            break
                        store32(arg1 + 72, (v3 + v6))
                        store32(arg1 + 76, (load32(arg1 + 76) + v6))
                    arg0 = (arg0 + 1)
                    if (u32((arg0 + 1)) < u32(v13)):
                        continue
                    break
                v3 = load32(v2 + 236)
                break
            arg0 = (v8 + (v9 * 36))
            arg1 = ((v8 + (v9 * 36)) + 269388)
            store32(((v8 + (v9 * 36)) + 269388), (load32(arg1) + v4))
            arg1 = (arg0 + 269392)
            store32((arg0 + 269392), (load32(arg1) + v4))
            arg1 = (arg0 + 269380)
            store32((arg0 + 269380), (load32(arg1) + v12))
            arg1 = (arg0 + 269384)
            store32((arg0 + 269384), (load32(arg1) + v11))
            arg1 = (arg0 + 269396)
            store32((arg0 + 269396), (load32(arg1) + v10))
            arg0 = (arg0 + 269404)
            store32((arg0 + 269404), (load32(arg0) + v6))
            v5 = (v5 + 1)
            if (u32((v5 + 1)) < u32(v3)):
                continue
            break

# ----------------------------------------------------------
# $func739
# ----------------------------------------------------------
def func739(arg0, arg1):
    v2 = load32(PLAYERS)
    arg1 = ((arg1 * 404) + ENTITY_TYPES)
    v3 = load32(((arg1 * 404) + ENTITY_TYPES) + 212)
    if (load32(((arg1 * 404) + ENTITY_TYPES) + 212) == 4):
        arg1 = load32(arg1 + 92)
        arg0 = (v2 + (arg0 * 286704))
        store8((v2 + (arg0 * 286704)) + 286700, 1)
        arg0 = (arg0 + 284000)
        # TODO: i32.div_u
        store32((arg1 * load32(arg0)), 100)
        return
    arg0 = (((v2 + (arg0 * 286704)) + (v3 << 2)) + 283984)
    store32((((v2 + (arg0 * 286704)) + (v3 << 2)) + 283984), (load32(arg0) + load32(arg1 + 92)))

# ----------------------------------------------------------
# $func740
# ----------------------------------------------------------
def func740(arg0, arg1):
    v6 = load32(ENTITIES)
    v7 = entities[arg0]
    while True:  # $label0
        if (u32(load32(9142848)) >= u32((load32(load32(GAME_STATE) + 72) * 2400))):
            v9 = (v6 + (arg1 * 132))
            if (load8u((v6 + (arg1 * 132)) + 125) != 3):
                break
        func29(v7, 1)
        return
        break
    v4 = (v6 + (arg0 * 132))
    if (load8u((v6 + (arg0 * 132)) + 125) == 1):
        v2 = load16u(v4 + 114)
        v3 = (v6 + (arg1 * 132))
        v5 = load16u((v6 + (arg1 * 132)) + 114)
        while True:  # $label2
            while True:  # $label1
                v3 = load16u(v3 + 112)
                v4 = load16u(v4 + 112)
                if (load16u(v3 + 112) != load16u(v4 + 112)):
                    break
                if (u32(v2) < u32(v5)):
                    break
                if (u32(v2) > u32(v5)):
                    break
                v3 = 0
                break
                break
            v3 = (1 if (u32(v3) > u32(v4)) else (-1 if (u32(v3) < u32(v4)) else 0))
            break
        v2 = (1 if (u32(v2) < u32(v5)) else (-1 if (u32(v2) > u32(v5)) else 0))
        arg0 = (v6 + (arg0 * 132))
        v2 = (((v2 * 3) + v3) + 4)
        if (u32((((v2 * 3) + v3) + 4)) <= u32(8)):
        else:
        store8(load8u((v2 + 10184)) + 124, 6)
        arg0 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 276)
        func63(func37(v7, load32(((load8u(arg0 + 122) * 72) + 9263856) + 8), 0.0, 0), v7, 23, arg1, (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 276) if arg0 else 25))
        return (v6 + (arg0 * 132))
    v5 = ((load8u(v4 + 122) * 404) + ENTITY_TYPES)
    if load32(((load8u(v4 + 122) * 404) + ENTITY_TYPES) + 216):
        v2 = (v6 + (arg0 * 132))
        v10 = load16u((v6 + (arg0 * 132)) + 114)
        v11 = load16u(v2 + 112)
        v12 = load32(9142840)
        v2 = 0
        while True:  # $label4
            v2 = (v2 + 1)
            v13 = ((v2 + 1) + v11)
            v3 = 0
            while True:  # $label3
                v3 = (v3 + 1)
                v8 = (load32(9142440) + 2)
                store32((v12 + ((v13 + ((((v3 + 1) + v10) + ((load32(9142440) + 2) * load32(v5 + 208))) * v8)) << 2)), load32(v5 + 212))
                v8 = load32(v5 + 216)
                if (u32(v3) < u32(load32(v5 + 216))):
                    continue
                break
            if (u32(v2) < u32(v8)):
                continue
            break
    v2 = (v6 + (arg1 * 132))
    v10 = load8u((v6 + (arg1 * 132)) + 122)
    store8(v4 + 122, load8u((v6 + (arg1 * 132)) + 122))
    arg1 = (v6 + (arg0 * 132))
    store8((v6 + (arg0 * 132)) + 124, load8u(v2 + 124))
    store16(arg1 + 120, load16u(v2 + 110))
    v5 = load16u(v2 + 112)
    store16(arg1 + 112, load16u(v2 + 112))
    v9 = load16u(v2 + 114)
    store16(arg1 + 114, load16u(v2 + 114))
    v2 = load8u(v4 + 122)
    v4 = ((load8u(v4 + 122) * 404) + ENTITY_TYPES)
    if load32(((load8u(v4 + 122) * 404) + ENTITY_TYPES) + 216):
        v11 = ((v2 * 404) + 9568304)
        v12 = load32(9142840)
        v2 = 0
        while True:  # $label6
            v2 = (v2 + 1)
            v13 = ((v2 + 1) + v5)
            v3 = 0
            while True:  # $label5
                v3 = (v3 + 1)
                v8 = (load32(9142440) + 2)
                store32((v12 + ((v13 + ((((v3 + 1) + v9) + ((load32(9142440) + 2) * load32(v11))) * v8)) << 2)), load32(arg1 + 28))
                v8 = load32(v4 + 216)
                if (u32(v3) < u32(load32(v4 + 216))):
                    continue
                break
            if (u32(v2) < u32(v8)):
                continue
            break
    v3 = load16u(arg1 + 114)
    arg1 = load16u(arg1 + 112)
    while True:  # $label9
        while True:  # $label8
            while True:  # $label7
                v5 = load32(load32(GAME_STATE) + 48)
                if load32(load32(GAME_STATE) + 48):
                    if not load8u(9147152):
                        break
                v2 = load32(9142440)
                break
                break
            v2 = load32(9142440)
            v4 = load16u((load32(9147376) + (((load32(9142440) * v3) + arg1) << 1)))
            if (v5 == 2):
                if (u32(v4) > u32(1)):
                    break
                break
            if not v4:
                break
            break
        func80(i32(arg1), i32(v3), load32(9142788), 32.0, i32((v2 * 96)))
        break
    v5 = 2
    v4 = func26(16)
    v9 = ((v10 * 404) + ENTITY_TYPES)
    arg1 = load32(((v10 * 404) + ENTITY_TYPES) + 236)
    v2 = (load32(((v10 * 404) + ENTITY_TYPES) + 236) + 2)
    store32(func26(16) + 4, (load32(((v10 * 404) + ENTITY_TYPES) + 236) + 2))
    v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
    store32(v4, func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2))))
    store64(v4 + 8, 4294967296)
    while True:  # $label12
        if arg1:
            v3 = 0
            while True:  # $label11
                v10 = load32((load32(v9 + 232) + (v3 << 2)))
                v5 = (load32((load32(v9 + 232) + (v3 << 2))) - 270)
                if not ((u32((load32((load32(v9 + 232) + (v3 << 2))) - 270)) <= u32(31)) if ((1 << v5) & -1073741823) else 0):
                    while True:  # $label10
                        v5 = load32(v4 + 8)
                        if (load32(v4 + 8) != load32(v4 + 4)):
                            arg1 = v2
                            break
                        arg1 = (load32(v4 + 12) + v5)
                        store32(v4 + 4, (load32(v4 + 12) + v5))
                        arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
                        if v5:
                            # TODO: memory.copy
                        if v2:
                        store32(v4, arg1)
                        v2 = arg1
                        break
                    store32(v4 + 8, (v5 + 1))
                    store32((arg1 + (v5 << 2)), v10)
                    arg1 = load32(v9 + 236)
                v3 = (v3 + 1)
                if (u32((v3 + 1)) < u32(arg1)):
                    continue
                break
            v5 = load32(v4 + 4)
        else:
        arg1 = 0
        if (0 != v5):
            v3 = v2
            break
        v3 = (load32(v4 + 12) + v5)
        store32(v4 + 4, (load32(v4 + 12) + v5))
        v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
        if v5:
            # TODO: memory.copy
        if v2:
        store32(v4, v3)
        break
    store32(v4 + 8, (arg1 + 1))
    store32((v3 + (arg1 << 2)), 234)
    while True:  # $label13
        v2 = load32(v4 + 8)
        if (load32(v4 + 8) != load32(v4 + 4)):
            arg1 = v3
            break
        arg1 = (load32(v4 + 12) + v2)
        store32(v4 + 4, (load32(v4 + 12) + v2))
        arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
        if v2:
            # TODO: memory.copy
        store32(v4, arg1)
        break
    store32(v4 + 8, (v2 + 1))
    store32((arg1 + (v2 << 2)), 235)
    arg0 = (v6 + (arg0 * 132))
    v3 = load32((v6 + (arg0 * 132)) + 24)
    if not load32((v6 + (arg0 * 132)) + 24):
        v3 = func26(16)
        store64(func26(16), 0)
        store64(v3 + 8, 0)
        store32(arg0 + 24, v3)
    store32(v3, v4)
    func29(v7, 1)
    return af(v3)

# ----------------------------------------------------------
# $func743
# ----------------------------------------------------------
def func743(arg0):
    while True:  # $label0
        if not load32(9671176):
            break
        if load32(9671192):
            arg0 = 0
            while True:  # $label1
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
    if load32(9681456):
        v3 = load32(9681448)
        while True:  # $label3
            v5 = load32((v3 + (v4 << 2)))
            while True:  # $label2
                arg0 = load32(9671176)
                if (load32(9671176) != load32(9671172)):
                    v1 = load32(9671168)
                    break
                v1 = (load32(9671180) + arg0)
                store32(9671172, (load32(9671180) + arg0))
                v2 = load32(9671168)
                v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                if arg0:
                    # TODO: memory.copy
                if v2:
                    v3 = load32(9681448)
                    arg0 = load32(9671176)
                store32(9671168, v1)
                break
            store32(9671176, (arg0 + 1))
            store32((v1 + (arg0 << 2)), v5)
            v4 = (v4 + 1)
            if (u32((v4 + 1)) < u32(load32(9681456))):
                continue
            break
    while True:  # $label4
        v6 = i32(load32(9142860))
        v6 = loadf32(40616)
        v8 = loadf32(9671164)
        v7 = (((i32(load32(9142860)) - ((v6 * loadf32(40616)) / loadf32(9671164))) * 0.5) + ((v6 * i32(load32(9681444))) + i32(load32(9142956))))
        if (abs((((i32(load32(9142860)) - ((v6 * loadf32(40616)) / loadf32(9671164))) * 0.5) + ((v6 * i32(load32(9681444))) + i32(load32(9142956))))) < 2147483650.0):
            break
        break
    arg0 = -2147483648
    v7 = i32(load32(9142856))
    v6 = (((v6 * i32(load32(9681440))) + i32(load32(9142952))) + ((i32(load32(9142856)) - ((v6 * v7) / v8)) * 0.5))
    if (abs((((v6 * i32(load32(9681440))) + i32(load32(9142952))) + ((i32(load32(9142856)) - ((v6 * v7) / v8)) * 0.5))) < 2147483650.0):
        return func132(i32(v6), arg0)
    return func132(-2147483648, arg0)

# ----------------------------------------------------------
# $func745
# ----------------------------------------------------------
def func745(arg0, arg1):
    v3 = load32(ENTITIES)
    v4 = entities[arg0]
    if (load8u(entities[arg0].unit_class) != 3):
        while True:  # $label0
            arg1 = load32(v4 + 16)
            if not load32(v4 + 16):
                break
            if not load32(arg1 + 8):
                break
            while True:  # $label1
                v5 = (v3 + (load32((load32(arg1) + (v2 << 2))) * 132))
                v7 = load32((v3 + (load32((load32(arg1) + (v2 << 2))) * 132)) + 64)
                v6 = load32(v5 + 68)
                if (u32(load32((v3 + (load32((load32(arg1) + (v2 << 2))) * 132)) + 64)) < u32(load32(v5 + 68))):
                    arg1 = (v7 + 2)
                    store32((v5 - -64), ((v7 + 2) if (u32(arg1) < u32(v6)) else v6))
                    v3 = load32(ENTITIES)
                    arg1 = load32(v4 + 16)
                v2 = (v2 + 1)
                if (u32((v2 + 1)) < u32(load32(arg1 + 8))):
                    continue
                break
            break

# ----------------------------------------------------------
# $func746
# ----------------------------------------------------------
def func746(arg0, arg1, param2):
    v16 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v3 = load32(ENTITIES)
    v4 = entities[arg0]
    v6 = (v3 + (arg1 * 132))
    v12 = load8u((v3 + (arg1 * 132)) + 122)
    while True:  # $label3
        v11 = load8u(v4 + 125)
        if (load8u(v4 + 125) == 1):
            v2 = ((v12 * 404) + ENTITY_TYPES)
            v7 = load32(((v12 * 404) + ENTITY_TYPES) + 220)
            v8 = load16u(v6 + 114)
            v14 = (load32(((v12 * 404) + ENTITY_TYPES) + 220) + load16u(v6 + 114))
            v5 = load32(v2 + 216)
            v12 = load16u(v6 + 112)
            v6 = (load32(v2 + 216) + load16u(v6 + 112))
            v9 = load16u(v4 + 114)
            while True:  # $label1
                while True:  # $label0
                    v10 = load16u(v4 + 112)
                    v2 = (u32(load16u(v4 + 112)) < u32(v12))
                    if (u32(load16u(v4 + 112)) < u32(v12)):
                        break
                    if (v6 <= v10):
                        break
                    if (u32(v8) > u32(v9)):
                        break
                    if (v9 >= v14):
                        break
                    v2 = ((v7 // 2) + v8)
                    v13 = (-1 if (v2 < v9) else (((v7 // 2) + v8) != v9))
                    v2 = ((v5 // 2) + v12)
                    break
                    break
                v13 = (1 if (u32(v8) > u32(v9)) else (-1 if (v9 >= v14) else 0))
                break
            v11 = (1 if v2 else (-1 if (v6 <= v10) else 0))
            v5 = 6
            v2 = (((v13 * 3) + v11) + 4)
            if (u32((((v13 * 3) + v11) + 4)) <= u32(8)):
                v5 = load8u((v2 + 10184))
            v2 = (v3 + (arg0 * 132))
            store8((v3 + (arg0 * 132)) + 124, v5)
            while True:  # $label2
                v2 = ((load8u(v2 + 122) * 72) + 9263856)
                if load32(((load8u(v2 + 122) * 72) + 9263856) + 12):
                    break
                break
            v6 = (v3 + (arg0 * 132))
            v2 = load32(((load32((load32(9215884) + (load32((v3 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32((v3 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32):
            if (load8u(v4 + 125) == 3):
                break
            v5 = load32(v6 + 44)
            if load32(v6 + 44):
                v2 = load32(9142848)
                v7 = load32(9215884)
                store32((load32(9215884) + (v5 << 4)) + 4, 13)
                store32((v7 + (load32(v6 + 44) << 4)) + 8, load32((v3 + (arg0 * 132)) + 28))
                store32((v7 + (load32(v6 + 44) << 4)) + 12, arg1)
                store32((v7 + (load32(v6 + 44) << 4)), (v2 + 1))
                break
            store32(v6 + 44, ((Ua(25, 13, load32((v3 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
            break
        while True:  # $label5
            while True:  # $label4
                if (load8u(v6 + 125) == 3):
                    break
                v17 = (v3 + (arg1 * 132))
                v14 = load32((v3 + (arg1 * 132)) + 64)
                if (u32(load32((v3 + (arg1 * 132)) + 64)) >= u32(load32(v17 + 68))):
                    break
                if not load32(v17 + 36):
                    break
                break
            v2 = (v3 + (arg0 * 132))
            if load32((v3 + (arg0 * 132)) + 96):
                break
            arg0 = (v3 + (arg1 * 132))
            arg0 = func243(load16u((v3 + (arg1 * 132)) + 112), load16u(arg0 + 114), load16u(v2 + 110))
            if func243(load16u((v3 + (arg1 * 132)) + 112), load16u(arg0 + 114), load16u(v2 + 110)):
                break
            func29(v4, 1)
            break
            break
        v9 = (v3 + (arg0 * 132))
        v13 = load16u((v3 + (arg0 * 132)) + 110)
        v15 = load32(PLAYERS)
        while True:  # $label6
            v6 = load32(v9 + 96)
            if load32(v9 + 96):
                v2 = (v3 + (arg1 * 132))
                v11 = load16u((v3 + (arg1 * 132)) + 114)
                v18 = load16u(v2 + 112)
                break
            v10 = load32(((v15 + (v13 * 286704)) + 284164))
            if (v11 == 8):
                store8(v4 + 125, 1)
                v11 = 1
            v8 = (v3 + (arg0 * 132))
            v7 = load32((v3 + (arg0 * 132)) + 72)
            if (u32(v10) > u32(load32((v3 + (arg0 * 132)) + 72))):
                v2 = load32(((load8u(v8 + 122) * 72) + 9263856))
                if (load32(((load8u(v8 + 122) * 72) + 9263856)) != load32(v8 + 48)):
                    v13 = load16u(v9 + 110)
                    v11 = load8u(v4 + 125)
                    v15 = load32(PLAYERS)
                v2 = load32(((v15 + (v13 * 286704)) + 284156))
                if ((v11 & 255) == 1):
                    func63(func37(v4, v2, 0.0, 0), v4, 13, arg1, v2)
                    break
                # TODO: i32.div_u
                store32(load32(9142848), (v2 + 25))
                break
            v5 = (v3 + (arg1 * 132))
            v18 = load16u((v3 + (arg1 * 132)) + 112)
            v2 = (load16u(v8 + 112) - load16u((v3 + (arg1 * 132)) + 112))
            v11 = load16u(v5 + 114)
            v2 = (load16u(v8 + 114) - load16u(v5 + 114))
            v5 = (v15 + (v13 * 286704))
            v2 = load32(((v15 + (v13 * 286704)) + 284024))
            if (((((load16u(v8 + 112) - load16u((v3 + (arg1 * 132)) + 112)) * v2) + ((load16u(v8 + 114) - load16u(v5 + 114)) * v2)) - 1) > (load32(((v15 + (v13 * 286704)) + 284024)) * v2)):
                func117(v4, arg1, 13)
                break
            store32(v8 + 72, (v7 - v10))
            v2 = (v5 + 281668)
            store32((v5 + 281668), (load32(v2) + v10))
            break
        v8 = (v17 - -64)
        v2 = (load32(((v12 * 404) + ENTITY_TYPES) + 300) * load32(((v15 + (v13 * 286704)) + 284160)))
        # TODO: i32.div_u
        store32(1, (((load32(((v12 * 404) + ENTITY_TYPES) + 300) * load32(((v15 + (v13 * 286704)) + 284160))) if (u32(v2) < u32(100)) else 100) + v14))
        v10 = (v3 + (arg1 * 132))
        while True:  # $label9
            while True:  # $label8
                while True:  # $label7
                    v2 = load32(load32(GAME_STATE) + 48)
                    if load32(load32(GAME_STATE) + 48):
                        if not load8u(9147152):
                            break
                    v7 = load32(9142440)
                    break
                    break
                v7 = load32(9142440)
                v5 = load16u((load32(9147376) + (((load32(9142440) * (v11 & 65535)) + v18) << 1)))
                if (v2 == 2):
                    if (u32(v5) > u32(1)):
                        break
                    break
                if not v5:
                    break
                break
            func80(i32(v18), i32((v11 & 65535)), load32(9142552), 32.0, i32((v7 * 96)))
            v12 = load16u(v10 + 112)
            v2 = ((load16u(v10 + 112) << 5) - load32(9142952))
            v14 = load16u(v10 + 114)
            v2 = ((load16u(v10 + 114) << 5) - load32(9142956))
            if ((((((load16u(v10 + 112) << 5) - load32(9142952)) * v2) + (((load16u(v10 + 114) << 5) - load32(9142956)) * v2)) - 1) > 9000000):
                break
            v5 = load32(39864)
            while True:  # $label10
                v2 = load32(load32(GAME_STATE) + 48)
                if not load32(load32(GAME_STATE) + 48):
                    break
                if load8u(9147152):
                    break
                v7 = load16u((load32(9147376) + (((load32(9142440) * v14) + v12) << 1)))
                if (v2 == 2):
                    if (u32(v7) > u32(1)):
                        break
                    break
                if not v7:
                    break
                break
            store32(v16 + 8, v14)
            store32(v16 + 4, v12)
            store32(v16, v5)
            a_b()
            break
        while True:  # $label13
            while True:  # $label11
                while True:  # $label12
                    v2 = load32(v17 + 68)
                    if (u32(load32(v17 + 68)) <= u32(load32(v8))):
                        store32(v8, v2)
                        if v6:
                            store8(v4 + 125, 0)
                        if load32(v9 + 96):
                            break
                        func117(v4, func243(load16u(v10 + 112), load16u(v10 + 114), load16u(v9 + 110)), 13)
                        break
                    if load32(v9 + 96):
                        break
                    arg0 = load32(((load8u((v3 + (arg0 * 132)) + 122) * 404) + ENTITY_TYPES) + 276)
                    func291(v4, 13, arg1, (load32(((load8u((v3 + (arg0 * 132)) + 122) * 404) + ENTITY_TYPES) + 276) if arg0 else 25))
                    break
                if not load32(v9 + 96):
                    break
                break
            func29(v4, 1)
            break
        if not load32((v3 + (arg1 * 132)) + 92):
            break
        if load32(9140316):
            if (load32(9140320) != load32((v3 + (arg1 * 132)) + 28)):
                break
        break
    G.global0 = (v16 + 16)
    return func28(1, 1)

# ----------------------------------------------------------
# $func747
# ----------------------------------------------------------
def func747(arg0, arg1, arg2, arg3, arg4):
    arg2 = load32(ENTITIES)
    arg3 = load32(arg1)
    v5 = load32(((load8u(entities[load32(arg1)].sub_state) * 404) + ENTITY_TYPES) + 300)
    arg1 = not load32(((load8u(entities[load32(arg1)].sub_state) * 404) + ENTITY_TYPES) + 300)
    while True:  # $label0
        if not v5:
            break
        if not arg4:
            break
        arg0 = load32((arg2 + (arg0 * 132)) + 44)
        if not load32((arg2 + (arg0 * 132)) + 44):
            return 0
        arg1 = 0
        arg2 = load32(9215884)
        if (load32((load32(9215884) + (arg0 << 4)) + 4) != 13):
            break
        store32((arg2 + ((arg0 << 4) | 12)), arg3)
        arg1 = 1
        break
    return arg1

# ----------------------------------------------------------
# $func748
# ----------------------------------------------------------
def func748(arg0):
    while True:  # $label0
        while True:  # $label1
            v2 = load32(ENTITIES)
            v3 = load32(arg0 + 32)
            v1 = entities[load32(arg0 + 32)]
            if (load8u(entities[load32(arg0 + 32)].unit_class) != 3):
                if (u32(load32(v1 + 64)) < u32(load32(v1 + 68))):
                    break
                if not load32(arg0 + 96):
                    break
                break
            if load32(arg0 + 96):
                break
            break
        v1 = (v2 + (v3 * 132))
        v1 = func243(load16u((v2 + (v3 * 132)) + 112), load16u(v1 + 114), load16u(arg0 + 110))
        if not func243(load16u((v2 + (v3 * 132)) + 112), load16u(v1 + 114), load16u(arg0 + 110)):
            return 1
        store32(arg0 + 32, v1)
        break
    return 0

# ----------------------------------------------------------
# $hc
# Export: hc
# ----------------------------------------------------------
def hc(arg0, arg1, arg2):
    """Export: hc"""
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        v7 = load32(9561704)
        if not load32(9561704):
            break
        v5 = load32(9561696)
        while True:  # $label1
            while True:  # $label2
                v6 = ((v3 << 2) + v5)
                if (u32(load32(((v3 << 2) + v5) + 4)) >= u32(arg0)):
                    break
                v3 = (load32(v6 + 8) + v3)
                if (u32((load32(v6 + 8) + v3)) < u32(v7)):
                    continue
                break
            v3 = 0
            break
        arg1 = (arg1 + 10)
        arg0 = 0
        while True:  # $label3
            v6 = ((arg0 << 2) + v5)
            if (u32(arg1) > u32(load32(((arg0 << 2) + v5) + 4))):
                arg0 = (load32(v6 + 8) + arg0)
                if (u32((load32(v6 + 8) + arg0)) < u32(v7)):
                    continue
                break
            break
        if (u32(arg0) <= u32(v3)):
            break
        store32(v4 + 8, arg2)
        store32(v4 + 4, (arg0 - v3))
        store32(v4, (v5 + (v3 << 2)))
        break
    G.global0 = (v4 + 16)

# ----------------------------------------------------------
# $uc
# Export: uc
# ----------------------------------------------------------
def uc():
    """Export: uc"""
    v0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v0, load32(9561808))
    store32(v0 + 4, load32(9561816))
    G.global0 = (v0 + 16)

# ----------------------------------------------------------
# $fb
# Export: fb
# ----------------------------------------------------------
def fb(arg0, arg1):
    """Export: fb"""
    if (u32(arg0) <= u32(254)):
        while True:  # $label0
            if arg1:
                v2 = 48
                break
            v2 = -48
            break
        arg0 = ((arg0 * 404) + 9568240)
    else:
    return 0

# ----------------------------------------------------------
# $sb
# Export: sb
# ----------------------------------------------------------
def sb(arg0):
    """Export: sb"""
    v2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v1 = ((arg0 * 404) + ENTITY_TYPES)
    v4 = load32(((arg0 * 404) + ENTITY_TYPES) + 196)
    while True:  # $label1
        while True:  # $label0
            v5 = load32(v1 + 264)
            if (load32(v1 + 264) != 3):
                break
            v3 = load32(v1 + 180)
            if not load32(v1 + 180):
                break
            v1 = (v3 + 8)
            break
            break
        v1 = (v1 + 144)
        break
    v3 = -48
    arg0 = ((arg0 * 404) + ENTITY_TYPES)
    v6 = load32(((arg0 * 404) + ENTITY_TYPES) + 84)
    arg0 = load32(arg0 + 148)
    v1 = load32(v1)
    store32(v2 + 16, (v5 == 3))
    store32(v2 + 12, arg0)
    store32(v2 + 8, v6)
    store32(v2 + 4, (v1 * v3))
    store32(v2, v4)
    G.global0 = (v2 + 32)
    return v2

# ----------------------------------------------------------
# $func762
# ----------------------------------------------------------
def func762(arg0, arg1, arg2):
    arg2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v4 = load32(PLAYERS)
    v8 = load32(ENTITIES)
    v9 = load32(arg1)
    arg1 = load16u(entities[load32(arg1)] + 110)
    v3 = players[load16u(entities[load32(arg1)] + 110)]
    v6 = (players[load16u(entities[load32(arg1)] + 110)] + 283916)
    v5 = load32(v3 + 283916)
    while True:  # $label0
        if load32(arg0 + 4):
            if v5:
                break
            while True:  # $label1
                v10 = (v4 + (arg1 * 286704))
                arg0 = load32(arg0)
                v11 = (3 if (u32(arg0) >= u32(3)) else load32(arg0))
                arg0 = (((v4 + (arg1 * 286704)) + ((3 if (u32(arg0) >= u32(3)) else load32(arg0)) << 2)) + 283848)
                v3 = load32((((v4 + (arg1 * 286704)) + ((3 if (u32(arg0) >= u32(3)) else load32(arg0)) << 2)) + 283848))
                if (load32((((v4 + (arg1 * 286704)) + ((3 if (u32(arg0) >= u32(3)) else load32(arg0)) << 2)) + 283848)) == 2147483647):
                    break
                store32(arg0, (v3 + 1000))
                arg0 = 1
                store8(v10 + 286701, 1)
                v3 = load32(PLAYER_COUNT)
                if (u32(load32(PLAYER_COUNT)) < u32(2)):
                    break
                v7 = (v3 - 1)
                v12 = ((v3 - 1) & 1)
                arg1 = (load32((v4 + (arg1 * 286704)) + 283908) * v3)
                v4 = load32(PLAYERS)
                v5 = load32(9143016)
                if (v3 != 2):
                    v7 = (v7 & -2)
                    v3 = 0
                    while True:  # $label2
                        if load8u((v5 + (arg0 + arg1))):
                            store8((v4 + (arg0 * 286704)) + 286701, 1)
                        v13 = (arg0 + 1)
                        if load8u((v5 + ((arg0 + 1) + arg1))):
                            store8((v4 + (v13 * 286704)) + 286701, 1)
                        arg0 = (arg0 + 2)
                        v3 = (v3 + 2)
                        if ((v3 + 2) != v7):
                            continue
                        break
                if not v12:
                    break
                if not load8u((v5 + (arg0 + arg1))):
                    break
                store8((v4 + (arg0 * 286704)) + 286701, 1)
                break
            store32(v6, 1200)
            store32(v10 + 283920, v11)
            break
        if not v5:
            break
        store64(arg2 + 8, 0)
        store64(arg2, 0)
        store32((arg2 + (load32((v4 + (arg1 * 286704)) + 283920) << 2)), load32(v6))
        if func66(v3, arg2, 1, 1):
            break
        store32(v6, 0)
        break
    while True:  # $label3
        if not load32((v8 + (v9 * 132)) + 92):
            break
        arg0 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32((v8 + (v9 * 132)) + 28)):
                break
        break
    G.global0 = (arg2 + 16)

# ----------------------------------------------------------
# $func763
# ----------------------------------------------------------
def func763(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v1 + 12, 1)
    store32(v1 + 8, arg0)
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
# $sd
# Export: sd
# ----------------------------------------------------------
def sd(arg0):
    """Export: sd"""
    v5 = load32(PLAYER_COUNT)
    v1 = func26(((load32(PLAYER_COUNT) << 2) - -64))
    store32(func26(((load32(PLAYER_COUNT) << 2) - -64)) + 16, 558088)
    store64(v1 + 8, -9151314443236311040)
    store64(v1, -72056494543012096)
    v2 = load8u(9142916)
    store64(v1 + 56, 4294901760)
    store64(v1 + 48, -280379750529536)
    store64(v1 + 40, 37300399396394132)
    store32(v1 + 36, -1)
    store8(v1 + 35, 1)
    store32(v1 + 31, -130)
    store64(v1 + 23, -3452718337)
    v2 = (12 if v2 else 75)
    store8(v1 + 22, (12 if v2 else 75))
    store8(v1 + 21, v2)
    store8(v1 + 20, v2)
    while True:  # $label0
        if not v5:
            break
        v4 = load32(PLAYERS)
        if not arg0:
            v2 = 16
            while True:  # $label1
                v6 = (v4 + (v3 * 286704))
                v7 = load16u((v4 + (v3 * 286704)) + 283972)
                arg0 = (v1 + (v2 << 2))
                store8((v1 + (v2 << 2)) + 2, load8u((v6 + 283974)))
                store16(arg0, v7)
                store8(arg0 + 3, 255)
                v2 = (v2 + 1)
                v3 = (v3 + 1)
                if ((v3 + 1) != v5):
                    continue
                break
            break
        if load8u(9147152):
            v2 = 16
            while True:  # $label2
                v6 = (v4 + (v3 * 286704))
                v7 = load16u((v4 + (v3 * 286704)) + 283972)
                arg0 = (v1 + (v2 << 2))
                store8((v1 + (v2 << 2)) + 2, load8u((v6 + 283974)))
                store16(arg0, v7)
                store8(arg0 + 3, 255)
                v2 = (v2 + 1)
                v3 = (v3 + 1)
                if ((v3 + 1) != v5):
                    continue
                break
            break
        v8 = load32(9143004)
        v6 = load32(CURRENT_PLAYER)
        arg0 = load8u((v4 + 283974))
        v2 = load16u(v4 + 283972)
        store8(v1 + 67, 255)
        store8(v1 + 66, arg0)
        store16(v1 + 64, v2)
        v2 = 1
        if (v5 == 1):
            break
        arg0 = 17
        while True:  # $label4
            while True:  # $label3
                if (v2 == v6):
                    v4 = 0
                    v7 = 0
                    break
                v3 = load8u((v8 + (v6 + (v2 * v5))))
                v7 = (0 if load8u((v8 + (v6 + (v2 * v5)))) else -1)
                v4 = (-1 if v3 else 0)
                break
            v9 = 0
            v3 = (v1 + (arg0 << 2))
            store8((v1 + (arg0 << 2)), v4)
            store8(v3 + 1, v7)
            store8(v3 + 2, v9)
            store8(v3 + 3, 255)
            arg0 = (arg0 + 1)
            v2 = (v2 + 1)
            if ((v2 + 1) != v5):
                continue
            break
        break
    return v1

# ----------------------------------------------------------
# $yd
# Export: yd
# ----------------------------------------------------------
def yd(arg0):
    """Export: yd"""
    v1 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v2 = ((arg0 * 404) + ENTITY_TYPES)
    v3 = load32(((arg0 * 404) + ENTITY_TYPES) + 92)
    v5 = load64(v2 + 104)
    v4 = load32(v2 + 100)
    v2 = load32(v2 + 120)
    store32(v1 + 28, arg0)
    store32(v1 + 24, 0)
    store32(v1 + 20, v2)
    store32(v1 + 16, v2)
    store32(v1 + 4, v4)
    store64(v1 + 8, v5)
    store32(v1, v3)
    G.global0 = (v1 + 32)

# ----------------------------------------------------------
# $func770
# ----------------------------------------------------------
def func770(arg0, arg1, arg2):
    while True:  # $label0
        if not arg2:
            break
        if not load32(arg0):
            break
        arg0 = 0
        while True:  # $label29
            while True:  # $label12
                v12 = entities[load32((arg1 + (arg0 << 2)))]
                if (load8u(entities[load32((arg1 + (arg0 << 2)))] + 129) != 8):
                    v3 = 0
                    v4 = 0
                    v14 = 0
                    while True:  # $label1
                        if (load8u(v12 + 129) == 8):
                            break
                        if (load8u(v12 + 125) == 3):
                            break
                        v6 = 5
                        while True:  # $label8
                            while True:  # $label4
                                while True:  # $label2
                                    v7 = load8u(v12 + 122)
                                    if (load8u(v12 + 122) == load32(38604)):
                                        break
                                    if (load32(38624) == v7):
                                        break
                                    v15 = -1
                                    while True:  # $label3
                                        if (v7 == load32(38608)):
                                            v4 = 1
                                            break
                                        if (v7 == load32(38628)):
                                            break
                                        v6 = 4
                                        v14 = -1
                                        v3 = 1
                                        while True:  # $label7
                                            while True:  # $label5
                                                if (load32(38612) == v7):
                                                    break
                                                if (load32(38632) == v7):
                                                    break
                                                while True:  # $label6
                                                    if (load32(38616) == v7):
                                                        break
                                                    if (load32(39056) == v7):
                                                        break
                                                    v3 = 0
                                                    v15 = 0
                                                    break
                                                    break
                                                v14 = 1
                                                break
                                                break
                                            break
                                        v15 = 0
                                        break
                                        break
                                    v14 = 0
                                    v6 = 5
                                    break
                                    break
                                v15 = 1
                                break
                            v4 = 1
                            break
                        v9 = 2
                        v13 = load32(9142840)
                        v8 = load16u(v12 + 112)
                        v18 = (v14 + 1)
                        v17 = (v4 * v9)
                        v5 = (load32(9142440) + 2)
                        v16 = ((v7 * 404) + ENTITY_TYPES)
                        v10 = ((load32(9142440) + 2) * load32(((v7 * 404) + ENTITY_TYPES) + 208))
                        v11 = load16u(v12 + 114)
                        v19 = (v15 + 1)
                        v20 = (v3 * v9)
                        v16 = load32(v16 + 212)
                        if (load32((load32(9142840) + (((load16u(v12 + 112) + ((v14 + 1) + (v4 * v9))) + ((((load32(9142440) + 2) * load32(((v7 * 404) + ENTITY_TYPES) + 208)) + (load16u(v12 + 114) + ((v15 + 1) + (v3 * v9)))) * v5)) << 2))) != load32(v16 + 212)):
                            break
                        while True:  # $label9
                            v21 = (v9 + 1)
                            if ((v9 + 1) == v6):
                                break
                            if (load32((v13 + ((((v18 + (v4 * v21)) + v8) + ((((v19 + (v3 * v21)) + v11) + v10) * v5)) << 2))) != v16):
                                break
                            v21 = (v9 + 2)
                            if ((v9 + 2) == v6):
                                break
                            if (load32((v13 + ((((v18 + (v4 * v21)) + v8) + ((((v19 + (v3 * v21)) + v11) + v10) * v5)) << 2))) != v16):
                                break
                            v21 = (v9 + 3)
                            if ((v9 + 3) == v6):
                                break
                            if (load32((v13 + ((((v18 + (v4 * v21)) + v8) + ((((v19 + (v3 * v21)) + v11) + v10) * v5)) << 2))) != v16):
                                break
                            break
                        v18 = ((v14 << 1) | 1)
                        v15 = ((v15 << 1) | 1)
                        if (load32((v13 + ((((((v14 << 1) | 1) + v17) + v8) + ((((((v15 << 1) | 1) + v20) + v11) + v10) * v5)) << 2))) != v16):
                            break
                        while True:  # $label10
                            v14 = (v9 + 1)
                            if ((v9 + 1) == v6):
                                break
                            if (load32((v13 + ((((v18 + (v4 * v14)) + v8) + ((((v15 + (v3 * v14)) + v11) + v10) * v5)) << 2))) != v16):
                                break
                            v19 = (v9 + 2)
                            if ((v9 + 2) == v6):
                                break
                            if (load32((v13 + ((((v18 + (v4 * v19)) + v8) + ((((v15 + (v3 * v19)) + v11) + v10) * v5)) << 2))) != v16):
                                break
                            v19 = (v9 + 3)
                            if ((v9 + 3) == v6):
                                break
                            if (load32((v13 + ((((v18 + (v4 * v19)) + v8) + ((((v15 + (v3 * v19)) + v11) + v10) * v5)) << 2))) != v16):
                                break
                            break
                        v5 = (load32(9142440) + 2)
                        v7 = ((v7 * 404) + ENTITY_TYPES)
                        store32(((((v8 + v17) + ((((v11 + v20) + ((load32(9142440) + 2) * load32(((v7 * 404) + ENTITY_TYPES) + 208))) + 1) * v5)) << 2) + v13) + 4, load32(v7 + 212))
                        while True:  # $label11
                            if (v6 == v14):
                                break
                            v5 = (load32(9142440) + 2)
                            store32((((((v4 * v14) + v8) + (((((v3 * v14) + v11) + ((load32(9142440) + 2) * load32(v7 + 208))) + 1) * v5)) << 2) + v13) + 4, load32(v7 + 212))
                            v5 = (v9 + 2)
                            if ((v9 + 2) == v6):
                                break
                            v5 = (load32(9142440) + 2)
                            store32((((((v4 * v5) + v8) + (((((v3 * v5) + v11) + ((load32(9142440) + 2) * load32(v7 + 208))) + 1) * v5)) << 2) + v13) + 4, load32(v7 + 212))
                            v6 = (v9 + 3)
                            if (v6 == (v9 + 3)):
                                break
                            v3 = (load32(9142440) + 2)
                            store32((((((v4 * v6) + v8) + (((((v3 * v6) + v11) + ((load32(9142440) + 2) * load32(v7 + 208))) + 1) * v3)) << 2) + v13) + 4, load32(v7 + 212))
                            break
                        store8(v12 + 129, 8)
                        if not load32(v12 + 92):
                            break
                        v3 = load8u(9147141)
                        if load32(9140316):
                            if (load32(9140320) != load32(v12 + 28)):
                                break
                        break
                    break
                v3 = 0
                v6 = 0
                v15 = 0
                v13 = (G.global0 - 112)
                G.global0 = (G.global0 - 112)
                while True:  # $label13
                    if (load8u(v12 + 129) != 8):
                        break
                    if (load8u(v12 + 125) == 3):
                        break
                    v14 = load8u(v12 + 122)
                    v19 = ((load8u(v12 + 122) * 404) + ENTITY_TYPES)
                    v8 = 5
                    while True:  # $label20
                        while True:  # $label16
                            while True:  # $label14
                                if (load32(38604) == v14):
                                    break
                                if (load32(38624) == v14):
                                    break
                                v18 = -1
                                while True:  # $label15
                                    if (v14 == load32(38608)):
                                        v6 = 1
                                        break
                                    if (v14 == load32(38628)):
                                        break
                                    v8 = 4
                                    v15 = -1
                                    v3 = 1
                                    while True:  # $label19
                                        while True:  # $label17
                                            if (load32(38612) == v14):
                                                break
                                            if (load32(38632) == v14):
                                                break
                                            while True:  # $label18
                                                if (load32(38616) == v14):
                                                    break
                                                if (load32(39056) == v14):
                                                    break
                                                v3 = 0
                                                v18 = 0
                                                break
                                                break
                                            v15 = 1
                                            break
                                            break
                                        break
                                    v18 = 0
                                    break
                                    break
                                v15 = 0
                                v8 = 5
                                break
                                break
                            v18 = 1
                            break
                        v6 = 1
                        break
                    v7 = 2
                    v10 = load32(v19 + 212)
                    v4 = load32(9142840)
                    v21 = (v6 * v7)
                    v11 = load16u(v12 + 112)
                    v24 = ((v6 * v7) + load16u(v12 + 112))
                    v23 = (v3 * v7)
                    v9 = load16u(v12 + 114)
                    v25 = ((v3 * v7) + load16u(v12 + 114))
                    v5 = (load32(9142440) + 2)
                    v16 = ((load32(9142440) + 2) * load32(v19 + 208))
                    if (load32(v19 + 212) != load32((load32(9142840) + ((((v6 * v7) + load16u(v12 + 112)) + (((((v3 * v7) + load16u(v12 + 114)) + ((load32(9142440) + 2) * load32(v19 + 208))) + 1) * v5)) << 2)) + 4)):
                        break
                    while True:  # $label21
                        v17 = (v7 + 1)
                        if ((v7 + 1) == v8):
                            break
                        if (load32((((((v6 * v17) + v11) + (((((v3 * v17) + v9) + v16) + 1) * v5)) << 2) + v4) + 4) != v10):
                            break
                        v17 = (v7 + 2)
                        if ((v7 + 2) == v8):
                            break
                        if (load32((((((v6 * v17) + v11) + (((((v3 * v17) + v9) + v16) + 1) * v5)) << 2) + v4) + 4) != v10):
                            break
                        v17 = (v7 + 3)
                        if ((v7 + 3) == v8):
                            break
                        if (load32((((((v6 * v17) + v11) + (((((v3 * v17) + v9) + v16) + 1) * v5)) << 2) + v4) + 4) != v10):
                            break
                        break
                    v17 = (v15 + 1)
                    v20 = (v18 + 1)
                    if (load32((v4 + (((((v15 + 1) + v21) + v11) + (((((v18 + 1) + v23) + v9) + v16) * v5)) << 2))) != v10):
                        break
                    while True:  # $label22
                        v22 = (v7 + 1)
                        if ((v7 + 1) == v8):
                            break
                        if (load32((v4 + ((((v17 + (v6 * v22)) + v11) + ((((v20 + (v3 * v22)) + v9) + v16) * v5)) << 2))) != v10):
                            break
                        v22 = (v7 + 2)
                        if ((v7 + 2) == v8):
                            break
                        if (load32((v4 + ((((v17 + (v6 * v22)) + v11) + ((((v20 + (v3 * v22)) + v9) + v16) * v5)) << 2))) != v10):
                            break
                        v22 = (v7 + 3)
                        if ((v7 + 3) == v8):
                            break
                        if (load32((v4 + ((((v17 + (v6 * v22)) + v11) + ((((v20 + (v3 * v22)) + v9) + v16) * v5)) << 2))) != v10):
                            break
                        break
                    v17 = ((v15 << 1) | 1)
                    v18 = ((v18 << 1) | 1)
                    if (load32((v4 + ((((((v15 << 1) | 1) + v21) + v11) + ((((((v18 << 1) | 1) + v23) + v9) + v16) * v5)) << 2))) != v10):
                        break
                    while True:  # $label23
                        v15 = (v7 + 1)
                        if ((v7 + 1) == v8):
                            break
                        if (load32((v4 + ((((v17 + (v6 * v15)) + v11) + ((((v18 + (v3 * v15)) + v9) + v16) * v5)) << 2))) != v10):
                            break
                        v20 = (v7 + 2)
                        if ((v7 + 2) == v8):
                            break
                        if (load32((v4 + ((((v17 + (v6 * v20)) + v11) + ((((v18 + (v3 * v20)) + v9) + v16) * v5)) << 2))) != v10):
                            break
                        v20 = (v7 + 3)
                        if ((v7 + 3) == v8):
                            break
                        if (load32((v4 + ((((v17 + (v6 * v20)) + v11) + ((((v18 + (v3 * v20)) + v9) + v16) * v5)) << 2))) != v10):
                            break
                        break
                    v10 = (load32(9142440) + 2)
                    v5 = ((v14 * 404) + ENTITY_TYPES)
                    store32((((v24 + (((v25 + ((load32(9142440) + 2) * load32(((v14 * 404) + ENTITY_TYPES) + 208))) + 1) * v10)) << 2) + v4) + 4, load32(v12 + 28))
                    while True:  # $label24
                        if (v8 == v15):
                            break
                        v10 = (load32(9142440) + 2)
                        store32((((((v6 * v15) + v11) + (((((v3 * v15) + v9) + ((load32(9142440) + 2) * load32(v5 + 208))) + 1) * v10)) << 2) + v4) + 4, load32(v12 + 28))
                        v10 = (v7 + 2)
                        if ((v7 + 2) == v8):
                            break
                        v10 = (load32(9142440) + 2)
                        store32((((((v6 * v10) + v11) + (((((v3 * v10) + v9) + ((load32(9142440) + 2) * load32(v5 + 208))) + 1) * v10)) << 2) + v4) + 4, load32(v12 + 28))
                        v8 = (v7 + 3)
                        if (v8 == (v7 + 3)):
                            break
                        v3 = (load32(9142440) + 2)
                        store32((((((v6 * v8) + v11) + (((((v3 * v8) + v9) + ((load32(9142440) + 2) * load32(v5 + 208))) + 1) * v3)) << 2) + v4) + 4, load32(v12 + 28))
                        break
                    while True:  # $label25
                        v3 = load32(v12 + 12)
                        if not load32(v12 + 12):
                            break
                        v8 = load32(load32(v3))
                        if not load32(load32(v3)):
                            break
                        if not load32(v12 + 40):
                            break
                        v4 = load32(v19)
                        v3 = 0
                        if load8u(9142916):
                            while True:  # $label26
                                if not v4:
                                    break
                                if not load32(v4 + 20):
                                    break
                                v11 = load8u(v12 + 124)
                                v3 = load32(v4 + 28)
                                if (load32(v4 + 28) == 2147483647):
                                    v3 = load32(59152)
                                    store32(59152, (load32(59152) + 1))
                                    v9 = load32(9568052)
                                    store32(v4 + 28, v3)
                                    v7 = load32(v4)
                                    v6 = load32(v4 + 4)
                                    v5 = load32(9568048)
                                    store32(9568048, (load32(9568048) + 1))
                                    store32(((v5 << 2) + 9563952), v4)
                                    store32(9568052, (v9 + ((v7 * (v6 + 2)) << 2)))
                                    v9 = load32(9568056)
                                    store32(v4 + 56, load32(9568056))
                                    store32(9568056, (v9 + ((v6 * load32(v4)) << 2)))
                                v3 = (v3 + (v11 << 16))
                                break
                            store32(v13 + 96, v8)
                            store64(v13 + 88, -4616189618054758400)
                            store32(v13 + 80, v3)
                            a_b()
                            break
                        v11 = (load32(v4 + 16) << 16)
                        v9 = load32(v4 + 20)
                        if load32(v4 + 20):
                            v7 = load8u(v12 + 124)
                            while True:  # $label27
                                v3 = load32(v4 + 28)
                                if (load32(v4 + 28) != 2147483647):
                                    v6 = load32(v4 + 4)
                                    break
                                v5 = load32(v4)
                                v10 = load32(9568052)
                                v3 = ((load32(v4) + load32(9140308)) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                store32(v4 + 28, ((load32(v4) + load32(9140308)) + ((load32(9568052) & 0xFFFFFFFF) >> 2)))
                                v6 = load32(v4 + 4)
                                store32(9568052, (v10 + ((v5 * (load32(v4 + 4) + 2)) << 2)))
                                v5 = load32(9568048)
                                store32(9568048, (load32(9568048) + 1))
                                store32(((v5 << 2) + 9563952), v4)
                                break
                            # TODO: i32.div_u
                        else:
                        v26 = 0.0
                        v3 = load16u(v12 + 110)
                        storef64(v13 + 56, i32(v11))
                        store32((v13 - -64), v8)
                        store32(v13 + 48, (v3 + 16))
                        # TODO: f64.promote_f32
                        storef64(v13 + 32, (v26 / i32(load32(59156))))
                        # TODO: f64.promote_f32
                        storef64(v13 + 40, i32((load32(9142848) * 25)))
                        a_b()
                        v27 = (i32(load16u(v12 + 112)) * 32.0)
                        v3 = load8u(9142916)
                        v28 = i32(load32(v4 + 12))
                        v29 = i32(load32(v4 + 8))
                        while True:  # $label28
                            v30 = (i32(load16u(v12 + 114)) * 32.0)
                            v4 = load32(9142440)
                            v26 = ((i32(load16u(v12 + 114)) * 32.0) + (i32(load32(9142440)) * 32.0))
                            if (((i32(load16u(v12 + 114)) * 32.0) + (i32(load32(9142440)) * 32.0)) == -55.0):
                                break
                            if not v3:
                                break
                            v26 = (((v26 * 0.5) / i32((v4 * 96))) + 0.25)
                            break
                        store32(v13 + 24, v8)
                        # TODO: f64.promote_f32
                        storef64(v13 + 16, v26)
                        # TODO: f64.promote_f32
                        storef64(v13 + 8, (v30 - (0.0 if v3 else v28)))
                        # TODO: f64.promote_f32
                        storef64(v13, (v27 - (0.0 if v3 else v29)))
                        a_b()
                        break
                    store8(v12 + 129, 0)
                    if not load32(v12 + 92):
                        break
                    v3 = load8u(9147141)
                    if load32(9140316):
                        if (load32(9140320) != load32(v12 + 28)):
                            break
                    break
                G.global0 = (v13 + 112)
                break
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break
        break
    return func28((v3 != 0), 1)

# ----------------------------------------------------------
# $func771
# ----------------------------------------------------------
def func771(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store64(v1 + 8, 1)
    while True:  # $label0
        if arg0:
            break
        arg0 = load32(9213808)
        if load8u(9147210):
            func41(28, 9173808, arg0, (v1 + 8), 2)
            break
        v3 = (arg0 << 2)
        v2 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy
        break
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $func772
# ----------------------------------------------------------
def func772(arg0, arg1, arg2):
    while True:  # $label0
        arg2 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v10 = load32(59164)
        arg1 = load32(PLAYERS)
        arg0 = 1
        while True:  # $label1
            if (v10 != load32((arg1 + (arg0 * 286704)) + 284616)):
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != arg2):
                    continue
                break
            break
        if not load8u(9216060):
            break
        if load32((((arg1 + (arg0 * 286704)) + (load32(9671152) << 2)) + 281808)):
            break
        v17 = (G.global0 - 16)
        G.global0 = (G.global0 - 16)
        arg1 = load32(PLAYERS)
        v16 = arg0
        v13 = players[arg0]
        # TODO: memory.fill
        func239(load32(v13 + 283908))
        store32(v13 + 283976, 0)
        store32(v13 + 283956, 0)
        arg0 = load32(v13 + 281788)
        if load32(v13 + 281788):
            store32(arg0 + 8, 0)
        arg0 = load32(v13 + 281792)
        if load32(v13 + 281792):
            store32(arg0 + 8, 0)
        arg2 = (arg1 + (v16 * 286704))
        arg0 = load32((arg1 + (v16 * 286704)) + 281796)
        if load32((arg1 + (v16 * 286704)) + 281796):
            store32(arg0 + 8, 0)
        v23 = load32(PLAYERS)
        while True:  # $label3
            arg0 = (arg2 + (v4 * 36))
            store32(((arg2 + (v4 * 36)) + 269408), 0)
            store64((arg0 + 269400), 0)
            store64((arg0 + 269392), 0)
            store64((arg0 + 269384), 0)
            store64((arg0 + 269376), 0)
            arg0 = (arg2 + (v4 << 2))
            store32(((arg2 + (v4 << 2)) + 282828), 0)
            store32((arg0 + 281808), 0)
            v3 = 0
            while True:  # $label2
                v6 = (arg2 + 283984)
                v7 = (v3 << 2)
                v10 = (v23 + 283984)
                store32(((arg2 + 283984) + (v3 << 2)), load32(((v23 + 283984) + v7)))
                arg0 = (v7 + 4)
                store32((v6 + (v7 + 4)), load32((arg0 + v10)))
                arg0 = (v7 + 8)
                store32((v6 + (v7 + 8)), load32((arg0 + v10)))
                arg0 = (v7 + 12)
                store32((v6 + (v7 + 12)), load32((arg0 + v10)))
                arg0 = (v7 + 16)
                store32((v6 + (v7 + 16)), load32((arg0 + v10)))
                v3 = (v3 + 5)
                if ((v3 + 5) != 155):
                    continue
                break
            v4 = (v4 + 1)
            if ((v4 + 1) != 255):
                continue
            break
        store32((arg1 + (v16 * 286704)) + 283848, load32(load32(GAME_STATE) + 4))
        store8(9682192, 1)
        while True:  # $label4
            v3 = load32(9142440)
            # TODO: i32.div_u
            # TODO: i32.div_u
            v45 = i32(120)
            v44 = ((load32(51780) * v3) - i32(120))
            if ((((load32(51780) * v3) - i32(120)) < 4294967300.0) & (v44 >= 0.0)):
                break
            break
        v5 = 0
        v18 = ((v3 & 0xFFFFFFFF) >> 1)
        v27 = load32(9684492)
        v19 = load32(9142432)
        arg2 = load32(9147316)
        arg1 = load32(9147320)
        v7 = load32(9147312)
        arg0 = load32(9147324)
        while True:  # $label22
            while True:  # $label20
                while True:  # $label5
                    if not load32(9147132):
                        break
                    if (v3 != 4096):
                        break
                    v20 = (v3 + 2)
                    v36 = (v3 - 30)
                    v37 = load32(38448)
                    v38 = load32(ENTITIES)
                    v28 = load32(9142840)
                    while True:  # $label21
                        v6 = arg1
                        arg1 = v7
                        store32(9147320, v7)
                        v10 = arg2
                        store32(9147324, arg2)
                        arg0 = ((arg0 << 11) ^ arg0)
                        arg2 = (((((v7 & 0xFFFFFFFF) >> 19) ^ ((((arg0 << 11) ^ arg0) & 0xFFFFFFFF) >> 8)) ^ v7) ^ arg0)
                        store32(9147316, (((((v7 & 0xFFFFFFFF) >> 19) ^ ((((arg0 << 11) ^ arg0) & 0xFFFFFFFF) >> 8)) ^ v7) ^ arg0))
                        arg0 = (v6 ^ (v6 << 11))
                        v7 = ((((((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg2 & 0xFFFFFFFF) >> 19)) ^ arg0) ^ arg2)
                        store32(9147312, ((((((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg2 & 0xFFFFFFFF) >> 19)) ^ arg0) ^ arg2))
                        while True:  # $label6
                            v29 = (arg2 % 4066)
                            v8 = ((arg2 % 4066) + 15)
                            arg0 = (((arg2 % 4066) + 15) - v18)
                            v30 = (v7 % v36)
                            v9 = ((v7 % v36) + 15)
                            arg0 = (((v7 % v36) + 15) - v18)
                            if (((((((arg2 % 4066) + 15) - v18) * arg0) + ((((v7 % v36) + 15) - v18) * arg0)) - 1) < 65537):
                                break
                            v24 = 1
                            while True:  # $label7
                                v5 = (30 if (u32(v15) > u32(500)) else 60)
                                v3 = (v8 - (30 if (u32(v15) > u32(500)) else 60))
                                arg0 = (v5 << 1)
                                v31 = ((v5 << 1) + v8)
                                if ((v8 - (30 if (u32(v15) > u32(500)) else 60)) >= ((v5 << 1) + v8)):
                                    break
                                v6 = (v9 - v5)
                                v39 = (arg0 + v9)
                                if ((v9 - v5) >= (arg0 + v9)):
                                    break
                                v24 = 0
                                v32 = (load32(PLAYER_COUNT) * v16)
                                v33 = load32(9142440)
                                v34 = (load32(9142440) + 2)
                                v40 = load32(38564)
                                v41 = load32(38620)
                                v42 = load32(38560)
                                v35 = load32(9143004)
                                v43 = load32(38500)
                                v12 = load32(ENTITIES)
                                v14 = load32(9142840)
                                v21 = (v5 * v5)
                                while True:  # $label11
                                    v5 = (v3 + 1)
                                    if (u32(v3) < u32(v33)):
                                        arg0 = (v3 - v8)
                                        v25 = (((v3 - v8) * arg0) - 1)
                                        arg0 = v6
                                        while True:  # $label10
                                            while True:  # $label8
                                                v4 = (arg0 - v9)
                                                if ((v25 + ((arg0 - v9) * v4)) > v21):
                                                    break
                                                if (u32(arg0) >= u32(v33)):
                                                    break
                                                if ((arg0 | v3) < 0):
                                                    break
                                                v4 = load32((v14 + ((v5 + (((arg0 + v34) + 1) * v34)) << 2)))
                                                if (u32(load32((v14 + ((v5 + (((arg0 + v34) + 1) * v34)) << 2)))) < u32(3)):
                                                    break
                                                v11 = (v12 + (v4 * 132))
                                                v22 = load8u((v12 + (v4 * 132)) + 122)
                                                if (v43 == load8u((v12 + (v4 * 132)) + 122)):
                                                    break
                                                v26 = load16u(v11 + 110)
                                                while True:  # $label9
                                                    v4 = load16u(v11 + 120)
                                                    if load16u(v11 + 120):
                                                    else:
                                                    if load8u(((v4 if load8u((v35 + (v26 + v32))) else v26) + (v26 + v32))):
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
                                                if (load32(v11 + 64) == -1):
                                                    break
                                                v4 = ((v22 * 404) + ENTITY_TYPES)
                                                if (load32(((v22 * 404) + ENTITY_TYPES) + 264) == 2):
                                                    break
                                                if (load32(v4 + 188) != 55):
                                                    break
                                                if (v22 == v42):
                                                    break
                                                if (v22 == v41):
                                                    break
                                                if (v22 != v40):
                                                    break
                                                break
                                            arg0 = (arg0 + 1)
                                            if ((arg0 + 1) != v39):
                                                continue
                                            break
                                    v24 = (v5 >= v31)
                                    v3 = v5
                                    if (v5 != v31):
                                        continue
                                    break
                                break
                            if not v24:
                                break
                            v14 = (v29 + 33)
                            v12 = 0
                            v4 = (v29 + 6)
                            arg0 = (v29 + 6)
                            v6 = (v30 + 6)
                            v21 = (v30 + 33)
                            if (u32((v30 + 6)) < u32((v30 + 33))):
                                while True:  # $label15
                                    while True:  # $label13
                                        v5 = (arg0 + 1)
                                        if (u32(arg0) <= u32(4095)):
                                            arg0 = (arg0 - v8)
                                            v25 = (((arg0 - v8) * arg0) - 1)
                                            arg0 = v6
                                            while True:  # $label14
                                                while True:  # $label12
                                                    v3 = (arg0 - v9)
                                                    if ((v25 + ((arg0 - v9) * v3)) > 81):
                                                        break
                                                    if (u32(arg0) > u32(4095)):
                                                        break
                                                    if (load32((v28 + (((((arg0 + v20) + 1) * v20) + v5) << 2))) == 1):
                                                        break
                                                    break
                                                arg0 = (arg0 + 1)
                                                if ((arg0 + 1) != v21):
                                                    continue
                                                break
                                        v12 = (u32(v5) >= u32(v14))
                                        arg0 = v5
                                        if (v5 != v14):
                                            continue
                                        break
                                    break
                                if not v12:
                                    break
                            v12 = 0
                            while True:  # $label19
                                while True:  # $label17
                                    v5 = (v4 + 1)
                                    if (u32(v4) <= u32(4095)):
                                        arg0 = (v4 - v8)
                                        v4 = (((v4 - v8) * arg0) - 1)
                                        arg0 = v6
                                        while True:  # $label18
                                            while True:  # $label16
                                                v3 = (arg0 - v9)
                                                if ((v4 + ((arg0 - v9) * v3)) > 81):
                                                    break
                                                if (u32(arg0) > u32(4095)):
                                                    break
                                                v3 = load32((v28 + (((((arg0 + v20) + 1) * v20) + v5) << 2)))
                                                if (u32(load32((v28 + (((((arg0 + v20) + 1) * v20) + v5) << 2)))) < u32(3)):
                                                    break
                                                if (v37 == load8u((v38 + (v3 * 132)) + 122)):
                                                    break
                                                break
                                            arg0 = (arg0 + 1)
                                            if ((arg0 + 1) != v21):
                                                continue
                                            break
                                    v12 = (u32(v5) >= u32(v14))
                                    v4 = v5
                                    if (v5 != v14):
                                        continue
                                    break
                                break
                            if not v12:
                                break
                            if v19:
                            else:
                            if (0 == v27):
                                break
                            break
                        arg0 = v10
                        v15 = (v15 + 1)
                        if ((v15 + 1) != 2000):
                            continue
                        break
                    break
                    break
                while True:  # $label25
                    v10 = v7
                    store32(9147320, v7)
                    store32(9147324, arg2)
                    arg0 = ((arg0 << 11) ^ arg0)
                    v6 = (((((v7 & 0xFFFFFFFF) >> 19) ^ ((((arg0 << 11) ^ arg0) & 0xFFFFFFFF) >> 8)) ^ v7) ^ arg0)
                    store32(9147316, (((((v7 & 0xFFFFFFFF) >> 19) ^ ((((arg0 << 11) ^ arg0) & 0xFFFFFFFF) >> 8)) ^ v7) ^ arg0))
                    arg0 = ((arg1 << 11) ^ arg1)
                    v7 = (((((((arg1 << 11) ^ arg1) & 0xFFFFFFFF) >> 8) ^ ((v6 & 0xFFFFFFFF) >> 19)) ^ arg0) ^ v6)
                    store32(9147312, (((((((arg1 << 11) ^ arg1) & 0xFFFFFFFF) >> 8) ^ ((v6 & 0xFFFFFFFF) >> 19)) ^ arg0) ^ v6))
                    while True:  # $label23
                        v46 = ((i32((v6 % 10000)) * 6.28318548) / 10000.0)
                        v44 = (v45 + i32((v7 % v5)))
                        # TODO: f64.promote_f32
                        v47 = ((func48(((i32((v6 % 10000)) * 6.28318548) / 10000.0)) * (v45 + i32((v7 % v5)))) + 0.5)
                        if (abs(((func48(((i32((v6 % 10000)) * 6.28318548) / 10000.0)) * (v45 + i32((v7 % v5)))) + 0.5)) < 2147483648.0):
                            break
                        break
                    v9 = (-2147483648 + v18)
                    while True:  # $label24
                        # TODO: f64.promote_f32
                        v47 = ((func49(v46) * v44) + 0.5)
                        if (abs(((func49(v46) * v44) + 0.5)) < 2147483648.0):
                            break
                        break
                    v8 = (-2147483648 + v18)
                    if v19:
                    else:
                    if (0 == v27):
                        break
                    arg0 = arg2
                    arg1 = v10
                    arg2 = v6
                    v15 = (v15 + 1)
                    if ((v15 + 1) != 2000):
                        continue
                    break
                break
                break
            while True:  # $label26
                if (load32(CURRENT_PLAYER) != v16):
                    break
                if load8u(9142917):
                    break
                store32(v17 + 4, (v9 << 5))
                store32(v17, (v8 << 5))
                v23 = load32(PLAYERS)
                break
            arg0 = (v23 + (v16 * 286704))
            store32((v23 + (v16 * 286704)) + 283900, v9)
            store32(arg0 + 283896, v8)
            store32(arg0 + 283876, v9)
            store32(arg0 + 283872, v8)
            break
        store8(9682192, 0)
        G.global0 = (v17 + 16)
        break
    return func317(v13)

# ----------------------------------------------------------
# $func774
# ----------------------------------------------------------
def func774(arg0, arg1):
    arg1 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v2 = load32(ENTITIES)
    while True:  # $label0
        if (u32(load32(9142848)) < u32((load32(load32(GAME_STATE) + 72) * 2400))):
            func29((v2 + (arg0 * 132)), 1)
            break
        while True:  # $label1
            v5 = (arg0 * 132)
            v3 = (v2 + (arg0 * 132))
            if (load8u((v2 + (arg0 * 132)) + 125) == 3):
                break
            if not load8u(v3 + 128):
                break
            v2 = (v2 + (arg0 * 132))
            store8((v2 + (arg0 * 132)) + 127, 0)
            while True:  # $label2
                v4 = load32(v2 + 40)
                if not load32(v2 + 40):
                    break
                if load8u(9142916):
                    store32(arg1 + 20, v4)
                    store32(arg1 + 16, 0)
                    a_b()
                    break
                v2 = load16u(v2 + 110)
                store32(arg1 + 4, v4)
                store32(arg1, (v2 + 16))
                a_b()
                break
            store8(v3 + 128, 0)
            v2 = load32(ENTITIES)
            break
        v2 = (v2 + v5)
        v3 = load16u(v2 + 116)
        v2 = load16u(v2 + 118)
        break
    G.global0 = (arg1 + 32)

# ----------------------------------------------------------
# $func775
# ----------------------------------------------------------
def func775(arg0, arg1):
    v8 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v2 = ((arg1 & 0xFFFFFFFF) >> 16)
    arg1 = (arg1 & 65535)
    v12 = load32(ENTITIES)
    v13 = entities[arg0]
    v4 = load16u(entities[arg0] + 110)
    v11 = load32(PLAYERS)
    while True:  # $label0
        if load8u(9142917):
            break
        v6 = load32(9299880)
        if load32(9299880):
            v6 = (v6 - 1)
            store32(9299880, (v6 - 1))
            v6 = load32((load32(9299872) + (v6 << 2)))
            break
        v6 = load32(9163776)
        v5 = (load32(9163776) + 1)
        store32(9163776, (load32(9163776) + 1))
        v9 = load32(9163784)
        if (u32(v5) < u32(load32(9163784))):
            break
        store32(v8 + 48, v9)
        a_b()
        store32(9163784, (load32(9163784) + 40000))
        break
    v14 = (arg1 << 5)
    v15 = (v2 << 5)
    while True:  # $label1
        v5 = load32(9142572)
        if not load32(9142572):
            break
        v9 = load32(v5 + 16)
        v5 = load32(v5 + 24)
        if (load32(v5 + 24) >= 100):
            v21 = loadf32((((v5 + v9) << 2) + 32700))
            if not ((loadf32((((v5 + v9) << 2) + 32700)) < 4294967300.0) & (v21 >= 0.0)):
                break
            v3 = i32(v21)
            break
        v3 = ((v9 * 1000) // v5)
        break
    while True:  # $label2
        v6 = (v14 - load32(9142952))
        v6 = (v15 - load32(9142956))
        if (((((v14 - load32(9142952)) * v6) + ((v15 - load32(9142956)) * v6)) - 1) > 9000000):
            break
        v5 = load32(39868)
        while True:  # $label3
            v9 = load32(load32(GAME_STATE) + 48)
            if not load32(load32(GAME_STATE) + 48):
                break
            if load8u(9147152):
                break
            v6 = load16u((load32(9147376) + (((load32(9142440) * v2) + arg1) << 1)))
            if (v9 == 2):
                if (u32(v6) > u32(1)):
                    break
                break
            if not v6:
                break
            break
        store32(v8 + 40, v2)
        store32(v8 + 36, arg1)
        store32(v8 + 32, v5)
        a_b()
        break
    while True:  # $label4
        v6 = (arg1 - 3)
        arg1 = players[load16u(v13 + 110)]
        v5 = load32((players[load16u(v13 + 110)] + 284180))
        v17 = (v6 + load32((players[load16u(v13 + 110)] + 284180)))
        if ((arg1 - 3) >= (v6 + load32((players[load16u(v13 + 110)] + 284180)))):
            break
        v14 = (v2 - 3)
        v18 = (v5 + v14)
        if ((v2 - 3) >= (v5 + v14)):
            break
        v19 = load32((arg1 + 284184))
        arg1 = (v11 + (v4 * 286704))
        v15 = ((v11 + (v4 * 286704)) + 281752)
        v16 = (arg1 + 281780)
        v11 = (v12 + (arg0 * 132))
        v4 = load32(9142440)
        while True:  # $label17
            v12 = (v6 + 1)
            arg0 = v14
            while True:  # $label16
                arg1 = arg0
                arg0 = (arg0 + 1)
                while True:  # $label5
                    if (u32(arg1) >= u32(v4)):
                        break
                    if ((arg1 | v6) < 0):
                        break
                    if (u32(v4) <= u32(v6)):
                        break
                    arg1 = 0
                    v3 = load32(9142840)
                    while True:  # $label15
                        while True:  # $label6
                            v2 = (v4 + 2)
                            v2 = load32((v3 + ((v12 + ((arg0 + ((v4 + 2) * arg1)) * v2)) << 2)))
                            if (u32(load32((v3 + ((v12 + ((arg0 + ((v4 + 2) * arg1)) * v2)) << 2)))) < u32(3)):
                                break
                            v2 = entities[v2]
                            v7 = load8u(entities[v2].sub_state)
                            v5 = load32(((load8u(entities[v2].sub_state) * 404) + ENTITY_TYPES) + 288)
                            if not load32(((load8u(entities[v2].sub_state) * 404) + ENTITY_TYPES) + 288):
                                break
                            if (load8u(v2 + 125) == 10):
                                break
                            v3 = load32(PLAYERS)
                            while True:  # $label7
                                v4 = load32(v2 + 64)
                                v9 = load32((((load8u(v11 + 122) * 1020) + 9299904) + (v7 << 2)))
                                # TODO: i32.div_u
                                # TODO: i32.div_u
                                v5 = 100
                                v5 = ((100 * v5) if (u32(v4) < u32(v5)) else 100)
                                if not ((((100 * v5) if (u32(v4) < u32(v5)) else 100) == v4) & (u32(v9) > u32(100))):
                                    v4 = load16u(v2 + 110)
                                    break
                                v10 = load16u(v13 + 110)
                                v4 = (v3 + (load16u(v13 + 110) * 286704))
                                while True:  # $label8
                                    if not load32(9147132):
                                        break
                                    if (load32(9671152) != v7):
                                        break
                                    v7 = load16u(v2 + 110)
                                    if (v10 == load16u(v2 + 110)):
                                        break
                                    if not v10:
                                        break
                                    v3 = (v3 + (v7 * 286704))
                                    v10 = load32((v3 + (v7 * 286704)) + 284628)
                                    v7 = load32(v3 + 284616)
                                    v20 = load32(v4 + 284616)
                                    store32(v8 + 16, (load32(v4 + 284616) if v20 else load32(v4 + 284628)))
                                    store32(v8 + 12, v4)
                                    store32(v8 + 4, v3)
                                    store32(v8, 927)
                                    store32(v8 + 8, (v7 if v7 else v10))
                                    a_b()
                                    break
                                while True:  # $label9
                                    v3 = load32((v4 + 278560))
                                    if load32((v4 + 278560)):
                                        v4 = load16u(v2 + 110)
                                        v3 = (v3 + ((load8u(v11 + 122) + (load16u(v2 + 110) * 255)) << 2))
                                        store32((v3 + ((load8u(v11 + 122) + (load16u(v2 + 110) * 255)) << 2)), (load32(v3) + 1))
                                        break
                                    v4 = load16u(v2 + 110)
                                    break
                                v3 = load32(PLAYERS)
                                v7 = load32((players[v4] + 278568))
                                if load32((players[v4] + 278568)):
                                    v7 = (v7 + ((load8u(v2 + 122) + (load16u(v13 + 110) * 255)) << 2))
                                    store32((v7 + ((load8u(v2 + 122) + (load16u(v13 + 110) * 255)) << 2)), (load32(v7) + 1))
                                store16(v2 + 116, load32(v11 + 28))
                                break
                            store32(v16, (load32(v16) + v5))
                            store32(v15, (load32(v15) + 1))
                            v7 = load16u(v13 + 110)
                            v10 = load32((v3 + (load16u(v13 + 110) * 286704)) + 278556)
                            if load32((v3 + (load16u(v13 + 110) * 286704)) + 278556):
                                v10 = (v10 + ((load8u(v11 + 122) + (v4 * 255)) << 2))
                                store32((v10 + ((load8u(v11 + 122) + (v4 * 255)) << 2)), (load32(v10) + v5))
                            v3 = load32(((v3 + (v4 * 286704)) + 278564))
                            if load32(((v3 + (v4 * 286704)) + 278564)):
                                v3 = (v3 + ((load8u(v2 + 122) + (v7 * 255)) << 2))
                                store32((v3 + ((load8u(v2 + 122) + (v7 * 255)) << 2)), (load32(v3) + v5))
                            v3 = (G.global0 - 48)
                            G.global0 = (G.global0 - 48)
                            while True:  # $label10
                                if not load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 288):
                                    break
                                v4 = load8u(v2 + 125)
                                if (load8u(v2 + 125) == 10):
                                    break
                                while True:  # $label11
                                    if (v4 == 3):
                                        break
                                    if not load8u(v2 + 128):
                                        break
                                    store8(v2 + 127, 0)
                                    while True:  # $label12
                                        v4 = load32(v2 + 40)
                                        if not load32(v2 + 40):
                                            break
                                        if load8u(9142916):
                                            store32(v3 + 36, v4)
                                            store32(v3 + 32, 0)
                                            a_b()
                                            break
                                        v7 = load16u(v2 + 110)
                                        store32(v3 + 20, v4)
                                        store32(v3 + 16, (v7 + 16))
                                        a_b()
                                        break
                                    store8(v2 + 128, 0)
                                    break
                                store8(v2 + 127, 2)
                                while True:  # $label13
                                    if not load8u(9142916):
                                        break
                                    v4 = load32(v2 + 40)
                                    if not load32(v2 + 40):
                                        break
                                    store32(v3 + 4, v4)
                                    store32(v3, -419430656)
                                    a_b()
                                    break
                                func119(func60(v2, 1.0), v2, 0, 0)
                                store8(v2 + 125, 9)
                                while True:  # $label14
                                    v4 = load32(v2 + 64)
                                    if (u32(v5) >= u32(load32(v2 + 64))):
                                        if (u32(v9) < u32(101)):
                                            break
                                        store32(v2 + 64, 0)
                                        break
                                    break
                                store32(func32(v2, v2, 0) + 64, (v4 - v5))
                                func63(v3, v2, 20, 0, load32((players[load16u(v2 + 110)] + 284200)))
                                func77(v2)
                                break
                            G.global0 = (v3 + 48)
                            func103(v2)
                            v3 = load32(9142840)
                            v4 = load32(9142440)
                            break
                        arg1 = (arg1 + 1)
                        if ((arg1 + 1) != 3):
                            continue
                        break
                    break
                if (arg0 != v18):
                    continue
                break
            v6 = v12
            if (v12 != v17):
                continue
            break
        break
    G.global0 = (v8 - -64)
    return 1061

# ----------------------------------------------------------
# $func776
# ----------------------------------------------------------
def func776(arg0, arg1):
    v4 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v3 = load32(ENTITIES)
    v2 = entities[arg0]
    while True:  # $label0
        if (u32(load32(9142848)) < u32((load32(load32(GAME_STATE) + 72) * 2400))):
            func29(v2, 1)
            break
        while True:  # $label1
            if (load8u(v2 + 125) == 3):
                break
            arg1 = (v3 + (arg0 * 132))
            if not load8u((v3 + (arg0 * 132)) + 128):
                break
            store8(arg1 + 127, 0)
            while True:  # $label2
                v5 = load32(arg1 + 40)
                if not load32(arg1 + 40):
                    break
                if load8u(9142916):
                    store32(v4 + 36, v5)
                    store32(v4 + 32, 0)
                    a_b()
                    break
                v6 = load16u(arg1 + 110)
                store32(v4 + 20, v5)
                store32(v4 + 16, (v6 + 16))
                a_b()
                break
            store8(arg1 + 128, 0)
            break
        v3 = (v3 + (arg0 * 132))
        while True:  # $label3
            arg1 = load16u(v3 + 112)
            v2 = ((load16u(v3 + 112) << 5) - load32(9142952))
            v2 = load16u(v3 + 114)
            v5 = ((load16u(v3 + 114) << 5) - load32(9142956))
            if ((((((load16u(v3 + 112) << 5) - load32(9142952)) * v2) + (((load16u(v3 + 114) << 5) - load32(9142956)) * v5)) - 1) > 9000000):
                break
            v6 = load32(39872)
            while True:  # $label4
                v7 = load32(load32(GAME_STATE) + 48)
                if not load32(load32(GAME_STATE) + 48):
                    break
                if load8u(9147152):
                    break
                v5 = load16u((load32(9147376) + (((load32(9142440) * v2) + arg1) << 1)))
                if (v7 == 2):
                    if (u32(v5) > u32(1)):
                        break
                    break
                if not v5:
                    break
                break
            store32(v4 + 8, v2)
            store32(v4 + 4, arg1)
            store32(v4, v6)
            a_b()
            v2 = load16u(v3 + 114)
            arg1 = load16u(v3 + 112)
            break
        v8 = 3.0
        v15 = i32((arg1 & 65535))
        v10 = (i32(load16u(v3 + 116)) - i32((arg1 & 65535)))
        v16 = i32((v2 & 65535))
        v9 = (i32(load16u(v3 + 118)) - i32((v2 & 65535)))
        v12 = sqrt((((i32(load16u(v3 + 116)) - i32((arg1 & 65535))) * v10) + ((i32(load16u(v3 + 118)) - i32((v2 & 65535))) * v9)))
        if not (sqrt((((i32(load16u(v3 + 116)) - i32((arg1 & 65535))) * v10) + ((i32(load16u(v3 + 118)) - i32((v2 & 65535))) * v9))) > 3.0):
            break
        v9 = (v9 / v12)
        v14 = (v10 / v12)
        v3 = load32(9142440)
        while True:  # $label19
            while True:  # $label5
                v10 = ((v14 * v8) + v15)
                # TODO: f64.promote_f32
                v17 = (((v14 * v8) + v15) + 0.5)
                if (abs((((v14 * v8) + v15) + 0.5)) < 2147483648.0):
                    break
                break
            v2 = -2147483648
            while True:  # $label7
                while True:  # $label6
                    v13 = ((v9 * v8) + v16)
                    # TODO: f64.promote_f32
                    v17 = (((v9 * v8) + v16) + 0.5)
                    if (abs((((v9 * v8) + v16) + 0.5)) < 2147483648.0):
                        break
                    break
                arg1 = -2147483648
                if (u32(-2147483648) >= u32(v3)):
                    break
                if ((arg1 | v2) < 0):
                    break
                if (u32(v2) >= u32(v3)):
                    break
                v2 = ((arg1 << 16) + v2)
                while True:  # $label8
                    if ((v8 < 4294967300.0) & (v8 >= 0.0)):
                        break
                    break
                arg1 = (0 * 50)
                while True:  # $label9
                    v11 = (v13 * 32.0)
                    if (((v13 * 32.0) < 4294967300.0) & (v11 >= 0.0)):
                        break
                    break
                v3 = 0
                while True:  # $label10
                    v11 = (v10 * 32.0)
                    if (((v10 * 32.0) < 4294967300.0) & (v11 >= 0.0)):
                        break
                    break
                v3 = load32(9142440)
                break
            while True:  # $label11
                # TODO: f64.promote_f32
                v17 = ((v9 + v10) + 0.5)
                if (abs(((v9 + v10) + 0.5)) < 2147483648.0):
                    break
                break
            v2 = -2147483648
            while True:  # $label13
                while True:  # $label12
                    # TODO: f64.promote_f32
                    v17 = ((v14 + v13) + 0.5)
                    if (abs(((v14 + v13) + 0.5)) < 2147483648.0):
                        break
                    break
                arg1 = -2147483648
                if (u32(-2147483648) >= u32(v3)):
                    break
                if ((arg1 | v2) < 0):
                    break
                if (u32(v2) >= u32(v3)):
                    break
                v2 = ((arg1 << 16) + v2)
                while True:  # $label14
                    if ((v8 < 4294967300.0) & (v8 >= 0.0)):
                        break
                    break
                v3 = load32(9142440)
                break
            while True:  # $label15
                # TODO: f64.promote_f32
                v17 = ((v10 - v9) + 0.5)
                if (abs(((v10 - v9) + 0.5)) < 2147483648.0):
                    break
                break
            v2 = -2147483648
            while True:  # $label17
                while True:  # $label16
                    # TODO: f64.promote_f32
                    v17 = ((v13 - v9) + 0.5)
                    if (abs(((v13 - v9) + 0.5)) < 2147483648.0):
                        break
                    break
                arg1 = -2147483648
                if (u32(-2147483648) >= u32(v3)):
                    break
                if ((arg1 | v2) < 0):
                    break
                if (u32(v2) >= u32(v3)):
                    break
                v2 = ((arg1 << 16) + v2)
                while True:  # $label18
                    if ((v8 < 4294967300.0) & (v8 >= 0.0)):
                        break
                    break
                v3 = load32(9142440)
                break
            v8 = (v8 + 1.0)
            if ((v8 + 1.0) < v12):
                continue
            break
        break
    G.global0 = (v4 + 48)
    return i32(v8)

# ----------------------------------------------------------
# $func777
# ----------------------------------------------------------
def func777(arg0, arg1):
    v9 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v3 = load32(ENTITIES)
    arg0 = entities[arg0]
    v7 = (players[load16u(entities[arg0] + 110)] + 281776)
    while True:  # $label0
        v10 = ((arg1 & 65535) + 1)
        v11 = (((arg1 & 0xFFFFFFFF) >> 16) + 1)
        v5 = load32((load32(9142840) + ((((arg1 & 65535) + 1) + ((((arg1 & 0xFFFFFFFF) >> 16) + 1) * (load32(9142440) + 2))) << 2)))
        if (u32(load32((load32(9142840) + ((((arg1 & 65535) + 1) + ((((arg1 & 0xFFFFFFFF) >> 16) + 1) * (load32(9142440) + 2))) << 2)))) < u32(3)):
            break
        arg1 = (v3 + (v5 * 132))
        v2 = load32(((load8u((v3 + (v5 * 132)) + 122) * 404) + ENTITY_TYPES) + 292)
        if not load32(((load8u((v3 + (v5 * 132)) + 122) * 404) + ENTITY_TYPES) + 292):
            break
        v8 = load8u(arg1 + 125)
        if (load8u(arg1 + 125) == 10):
            break
        v2 = (v2 * 96)
        # TODO: i32.div_u
        v4 = ((v2 * 96) if (u32(v2) < u32(100)) else 100)
        v12 = (v3 + (v5 * 132))
        v6 = load32((v3 + (v5 * 132)) + 64)
        v2 = (((v2 * 96) if (u32(v2) < u32(100)) else 100) if (u32(v4) < u32(v6)) else load32((v3 + (v5 * 132)) + 64))
        while True:  # $label1
            if (v8 == 3):
                break
            v8 = (v12 - -64)
            if (u32(v4) < u32(v6)):
                store32(v8, (v6 - v2))
                if not load32((v3 + (v5 * 132)) + 92):
                    break
                if load8u(9147141):
                    break
                store32(v9 + 32, v2)
                a_b()
                break
            store32(v8, 0)
            func155(arg0, arg1, 0)
            break
        func103(arg1)
        store32(v7, (load32(v7) + v2))
        v3 = load16u(v12 + 110)
        v5 = load32(PLAYERS)
        v6 = load16u(arg0 + 110)
        v4 = load32(players[load16u(arg0 + 110)] + 278556)
        if load32(players[load16u(arg0 + 110)] + 278556):
            v4 = (v4 + ((load8u(arg0 + 122) + (v3 * 255)) << 2))
            store32((v4 + ((load8u(arg0 + 122) + (v3 * 255)) << 2)), (load32(v4) + v2))
        v3 = load32(((v5 + (v3 * 286704)) + 278564))
        if not load32(((v5 + (v3 * 286704)) + 278564)):
            break
        arg1 = (v3 + ((load8u(arg1 + 122) + (v6 * 255)) << 2))
        store32((v3 + ((load8u(arg1 + 122) + (v6 * 255)) << 2)), (load32(arg1) + v2))
        break
    while True:  # $label2
        arg1 = (load32(9142440) + 2)
        v3 = load32((load32(9142840) + ((v10 + ((v11 + (load32(9142440) + 2)) * arg1)) << 2)))
        if (u32(load32((load32(9142840) + ((v10 + ((v11 + (load32(9142440) + 2)) * arg1)) << 2)))) < u32(3)):
            break
        v6 = load32(ENTITIES)
        arg1 = entities[v3]
        v2 = load32(((load8u(entities[v3].sub_state) * 404) + ENTITY_TYPES) + 292)
        if not load32(((load8u(entities[v3].sub_state) * 404) + ENTITY_TYPES) + 292):
            break
        v8 = load8u(arg1 + 125)
        if (load8u(arg1 + 125) == 10):
            break
        v2 = (v2 * 96)
        # TODO: i32.div_u
        v4 = ((v2 * 96) if (u32(v2) < u32(100)) else 100)
        v12 = (v6 + (v3 * 132))
        v5 = load32((v6 + (v3 * 132)) + 64)
        v2 = (((v2 * 96) if (u32(v2) < u32(100)) else 100) if (u32(v4) < u32(v5)) else load32((v6 + (v3 * 132)) + 64))
        while True:  # $label3
            if (v8 == 3):
                break
            v8 = (v12 - -64)
            if (u32(v4) >= u32(v5)):
                store32(v8, 0)
                func155(arg0, arg1, 0)
                break
            store32(v8, (v5 - v2))
            if not load32((v6 + (v3 * 132)) + 92):
                break
            if load8u(9147141):
                break
            store32(v9 + 16, v2)
            a_b()
            break
        func103(arg1)
        store32(v7, (load32(v7) + v2))
        v3 = load16u(v12 + 110)
        v5 = load32(PLAYERS)
        v6 = load16u(arg0 + 110)
        v4 = load32(players[load16u(arg0 + 110)] + 278556)
        if load32(players[load16u(arg0 + 110)] + 278556):
            v4 = (v4 + ((load8u(arg0 + 122) + (v3 * 255)) << 2))
            store32((v4 + ((load8u(arg0 + 122) + (v3 * 255)) << 2)), (load32(v4) + v2))
        v3 = load32(((v5 + (v3 * 286704)) + 278564))
        if not load32(((v5 + (v3 * 286704)) + 278564)):
            break
        arg1 = (v3 + ((load8u(arg1 + 122) + (v6 * 255)) << 2))
        store32((v3 + ((load8u(arg1 + 122) + (v6 * 255)) << 2)), (load32(arg1) + v2))
        break
    while True:  # $label4
        arg1 = (load32(9142440) + 2)
        v3 = load32((load32(9142840) + ((v10 + ((v11 + ((load32(9142440) + 2) << 1)) * arg1)) << 2)))
        if (u32(load32((load32(9142840) + ((v10 + ((v11 + ((load32(9142440) + 2) << 1)) * arg1)) << 2)))) < u32(3)):
            break
        v6 = load32(ENTITIES)
        arg1 = entities[v3]
        v2 = load32(((load8u(entities[v3].sub_state) * 404) + ENTITY_TYPES) + 292)
        if not load32(((load8u(entities[v3].sub_state) * 404) + ENTITY_TYPES) + 292):
            break
        v4 = load8u(arg1 + 125)
        if (load8u(arg1 + 125) == 10):
            break
        v2 = (v2 * 96)
        # TODO: i32.div_u
        v10 = ((v2 * 96) if (u32(v2) < u32(100)) else 100)
        v11 = (v6 + (v3 * 132))
        v5 = load32((v6 + (v3 * 132)) + 64)
        v2 = (((v2 * 96) if (u32(v2) < u32(100)) else 100) if (u32(v5) > u32(v10)) else load32((v6 + (v3 * 132)) + 64))
        while True:  # $label5
            if (v4 == 3):
                break
            v4 = (v11 - -64)
            if (u32(v5) <= u32(v10)):
                store32(v4, 0)
                func155(arg0, arg1, 0)
                break
            store32(v4, (v5 - v2))
            if not load32((v6 + (v3 * 132)) + 92):
                break
            if load8u(9147141):
                break
            store32(v9, v2)
            a_b()
            break
        func103(arg1)
        store32(v7, (load32(v7) + v2))
        v7 = load16u(v11 + 110)
        v3 = load32(PLAYERS)
        v5 = load16u(arg0 + 110)
        v6 = load32(players[load16u(arg0 + 110)] + 278556)
        if load32(players[load16u(arg0 + 110)] + 278556):
            arg0 = (v6 + ((load8u(arg0 + 122) + (v7 * 255)) << 2))
            store32((v6 + ((load8u(arg0 + 122) + (v7 * 255)) << 2)), (load32(arg0) + v2))
        arg0 = load32(((v3 + (v7 * 286704)) + 278564))
        if not load32(((v3 + (v7 * 286704)) + 278564)):
            break
        arg0 = (arg0 + ((load8u(arg1 + 122) + (v5 * 255)) << 2))
        store32((arg0 + ((load8u(arg1 + 122) + (v5 * 255)) << 2)), (load32(arg0) + v2))
        break
    G.global0 = (v9 + 48)
