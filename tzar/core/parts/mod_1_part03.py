"""
Tzar Engine - Core module (part 3).
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
# $func778
# ----------------------------------------------------------
def func778(arg0, arg1, param2):
    while True:  # $label0
        v5 = load32(ENTITIES)
        v3 = entities[arg0]
        if (load8u(entities[arg0].unit_class) == 1):
            store16(v3 + 108, 0)
            store32(v3 + 88, 0)
            v2 = load32(((load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            if (load8u(v3 + 125) == 3):
                break
            v4 = load32(v3 + 44)
            if load32(v3 + 44):
                v6 = load32(9142848)
                v2 = load32(9215884)
                store32((load32(9215884) + (v4 << 4)) + 4, 55)
                store32((v2 + (load32(v3 + 44) << 4)) + 8, load32((v5 + (arg0 * 132)) + 28))
                store32((v2 + (load32(v3 + 44) << 4)) + 12, arg1)
                store32((v2 + (load32(v3 + 44) << 4)), (v6 + 80))
                return
            store32(v3 + 44, ((Ua(2000, 55, load32((v5 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
            return
        if (load8u((v5 + (arg1 * 132)) + 125) == 3):
            func29(v3, 1)
            return
        v2 = (v5 + (arg0 * 132))
        v4 = players[load16u(v2 + 110)]
        v6 = (load16u(v2 + 108) + load16u((players[load16u(v2 + 110)] + 284328)))
        store16((v5 + (arg0 * 132)) + 108, (load16u(v2 + 108) + load16u((players[load16u(v2 + 110)] + 284328))))
        v4 = load32((v4 + 284332))
        if (u32(load32((v4 + 284332))) <= u32((v6 & 65535))):
            store16(v2 + 108, v4)
            store32(v2 + 88, 2)
            func207(v3, load32((v5 + (arg1 * 132)) + 28))
            v15 = load16u(v2 + 110)
            v9 = load16u(v2 + 112)
            v16 = (load16u(v2 + 112) + 149)
            v10 = load16u(v2 + 114)
            v17 = (load16u(v2 + 114) + 149)
            v18 = (v10 - 75)
            v2 = (v9 - 75)
            v11 = load32(9142440)
            v12 = (load32(9142440) + 2)
            v19 = load32(38872)
            v20 = load32(38796)
            v21 = load32(38584)
            v22 = load32(ENTITIES)
            v23 = load32(9142840)
            v6 = 2147483647
            while True:  # $label5
                v13 = (v2 + 1)
                if (u32(v2) < u32(v11)):
                    arg1 = (v2 - v9)
                    v24 = ((v2 - v9) * arg1)
                    arg1 = v18
                    while True:  # $label4
                        while True:  # $label1
                            v4 = arg1
                            arg1 = (arg1 - v10)
                            arg1 = (((arg1 - v10) * arg1) + v24)
                            if (((((arg1 - v10) * arg1) + v24) - 1) > 5625):
                                break
                            if (u32(v4) >= u32(v11)):
                                break
                            if ((v2 | v4) < 0):
                                break
                            if (arg1 >= v6):
                                break
                            v7 = (v22 + (load32((v23 + ((v13 + (((v4 + v12) + 1) * v12)) << 2))) * 132))
                            if (load16u((v22 + (load32((v23 + ((v13 + (((v4 + v12) + 1) * v12)) << 2))) * 132)) + 110) != v15):
                                break
                            while True:  # $label2
                                # br_table (load8u(v7 + 125) - 4)
                                break
                                break
                            while True:  # $label3
                                v14 = load8u(v7 + 122)
                                if (v21 == load8u(v7 + 122)):
                                    break
                                if (v14 == v20):
                                    break
                                if (v14 != v19):
                                    break
                                break
                            v8 = load32(v7 + 28)
                            v6 = arg1
                            break
                        arg1 = (v4 + 1)
                        if (v4 < v17):
                            continue
                        break
                arg1 = (v2 < v16)
                v2 = v13
                if arg1:
                    continue
                break
            while True:  # $label6
                arg1 = v8
                if v8:
                    break
                func29(v3, 1)
                break
            if not load32((v5 + (arg0 * 132)) + 92):
                break
            if load32(9140316):
                if (load32(9140320) != load32((v5 + (arg0 * 132)) + 28)):
                    break
            return
        while True:  # $label7
            if not load32(v2 + 92):
                break
            if load32(9140316):
                if (load32(9140320) != load32((v5 + (arg0 * 132)) + 28)):
                    break
            break
        store32((load32(9215884) + (load32((v5 + (arg0 * 132)) + 44) << 4)), (load32(9142848) + 80))
        break

# ----------------------------------------------------------
# $func780
# ----------------------------------------------------------
def func780(arg0, arg1):
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
        v4 = load16u(v2 + 118)
        v3 = players[load16u(v2 + 110)]
        v6 = load32((players[load16u(v2 + 110)] + 284364))
        v11 = (v3 - load32((players[load16u(v2 + 110)] + 284364)))
        v2 = (v6 << 1)
        v13 = (v6 << 1)
        v14 = load32((v3 + 284368))
        v12 = load32((v3 + 284360))
        if load32((v3 + 284360)):
            v15 = v2
            v16 = arg0
            v17 = (v4 - v6)
            v18 = (v6 + (v4 - v6))
            v19 = (v6 + v11)
            v8 = load32(9142440)
            v5 = load32(9147316)
            v3 = load32(9147320)
            arg0 = load32(9147312)
            v4 = load32(9147324)
            v20 = (v6 * v6)
            while True:  # $label5
                store32(9147320, arg0)
                v2 = v5
                store32(9147324, v5)
                v4 = ((v4 << 11) ^ v4)
                v5 = (((((arg0 & 0xFFFFFFFF) >> 19) ^ ((((v4 << 11) ^ v4) & 0xFFFFFFFF) >> 8)) ^ arg0) ^ v4)
                store32(9147316, (((((arg0 & 0xFFFFFFFF) >> 19) ^ ((((v4 << 11) ^ v4) & 0xFFFFFFFF) >> 8)) ^ arg0) ^ v4))
                v3 = ((v3 << 11) ^ v3)
                v4 = (((((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8) ^ ((v5 & 0xFFFFFFFF) >> 19)) ^ v3) ^ v5)
                store32(9147312, (((((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8) ^ ((v5 & 0xFFFFFFFF) >> 19)) ^ v3) ^ v5))
                v3 = (v5 % v13)
                while True:  # $label4
                    while True:  # $label3
                        v9 = ((v4 % v15) + v17)
                        if (u32(v8) <= u32(((v4 % v15) + v17))):
                            break
                        v10 = (v3 + v11)
                        if (u32(v8) <= u32((v3 + v11))):
                            break
                        if ((v9 | v10) < 0):
                            break
                        if v6:
                            v3 = arg0
                            arg0 = v4
                            v4 = v2
                            v2 = (v10 - v19)
                            v2 = (v9 - v18)
                            if (((((v10 - v19) * v2) + ((v9 - v18) * v2)) - 1) > v20):
                                break
                        # TODO: i32.div_u
                        v8 = load32(9142440)
                        v5 = load32(9147316)
                        v3 = load32(9147320)
                        arg0 = load32(9147312)
                        v4 = load32(9147324)
                        break
                        break
                    v3 = arg0
                    arg0 = v4
                    v4 = v2
                    break
                v7 = (v7 + 1)
                if ((v7 + 1) != v12):
                    continue
                break
        break
    G.global0 = (arg1 + 32)

# ----------------------------------------------------------
# $func781
# ----------------------------------------------------------
def func781(arg0, arg1):
    v2 = load32(ENTITIES)
    arg0 = entities[arg0]
    func29(entities[arg0], 1)
    arg1 = (v2 + (arg1 * 132))
    if (load8u((v2 + (arg1 * 132)) + 125) != 10):
        # TODO: i32.div_u

# ----------------------------------------------------------
# $func783
# ----------------------------------------------------------
def func783(arg0):
    while True:  # $label0
        arg0 = entities[load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 12)]
        if (load32(38528) != load8u(entities[load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 12)].sub_state)):
            break
        if (load8u(arg0 + 125) == 3):
            break
        store8(arg0 + 125, 0)
        break

# ----------------------------------------------------------
# $func784
# ----------------------------------------------------------
def func784(arg0):
    v1 = entities[load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 12)]
    if (load32(entities[load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 12)].cargo) == load32(arg0 + 28)):
        store32(v1 + 100, 0)

# ----------------------------------------------------------
# $func785
# ----------------------------------------------------------
def func785(arg0, arg1, arg2):
    if arg2:
        arg0 = 0
        while True:  # $label0
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break

# ----------------------------------------------------------
# $func786
# ----------------------------------------------------------
def func786(arg0, arg1, arg2, arg3, arg4):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label5
        while True:  # $label0
            arg4 = load32(9142832)
            if not load32(9142832):
                if not load32(load32(GAME_STATE) + 48):
                    break
            while True:  # $label3
                while True:  # $label4
                    while True:  # $label2
                        while True:  # $label1
                            v7 = load8u(entities[arg0].sub_state)
                            v8 = load32(((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES) + 212)
                            # br_table load32(((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES) + 212)
                            break
                            break
                        arg0 = load32(arg2)
                        v6 = load32(arg3)
                        v5 = (load32(9142440) + 2)
                        if (load32((load32(9142840) + ((load32(arg2) + (((load32(arg3) + (load32(9142440) + 2)) + 1) * v5)) << 2)) + 4) != 1):
                            break
                        break
                        break
                    arg0 = load32(arg2)
                    v6 = load32(arg3)
                    v5 = (load32(9142440) + 2)
                    if (u32((load32((load32(9142840) + ((load32(arg2) + (((load32(arg3) + (load32(9142440) + 2)) + 1) * v5)) << 2)) + 4) - 3)) >= u32(-2)):
                        break
                    break
                store32(arg1 + 12, arg0)
                store32(arg1 + 8, v6)
                if not func167((arg1 + 12), (arg1 + 8), 1, v8, load32(((v7 * 404) + ENTITY_TYPES) + 216)):
                    break
                store32(arg2, load32(arg1 + 12))
                store32(arg3, load32(arg1 + 8))
                arg4 = load32(9142832)
                break
            if arg4:
                break
            break
        break
    arg0 = not load32(load32(GAME_STATE) + 48)
    G.global0 = (arg1 + 16)
    return arg0

# ----------------------------------------------------------
# $func787
# ----------------------------------------------------------
def func787(arg0):
    v12 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # $label0
        if (load32(CURRENT_PLAYER) != load16u(arg0 + 110)):
            break
        v22 = load16u(arg0 + 114)
        v33 = load16u(arg0 + 118)
        v1 = (load16u(arg0 + 114) - load16u(arg0 + 118))
        v23 = load16u(arg0 + 112)
        v34 = load16u(arg0 + 116)
        v1 = (load16u(arg0 + 112) - load16u(arg0 + 116))
        if (u32((((load16u(arg0 + 114) - load16u(arg0 + 118)) * v1) + ((load16u(arg0 + 112) - load16u(arg0 + 116)) * v1))) > u32(4)):
            break
        v26 = ((load8u(arg0 + 124) & 0xFFFFFFFF) >> 1)
        v13 = load32(9142440)
        v24 = (load32(9142440) + 2)
        v25 = load8u(arg0 + 122)
        v1 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        v18 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        v10 = load32(v1 + 200)
        v15 = (load32(v1 + 200) << 1)
        v17 = load32(v1 + 216)
        v30 = load32(v1 + 212)
        v27 = (v10 * v10)
        v31 = load32(9147376)
        v32 = load32(9142840)
        v8 = v22
        v9 = v23
        while True:  # $label25
            while True:  # $label26
                v14 = 0
                v5 = 0
                v6 = 0
                while True:  # $label10
                    v1 = (v6 << 3)
                    v7 = (load32(((v6 << 3) + 8992)) + v9)
                    while True:  # $label4
                        v11 = (load32((v1 + 8996)) + v8)
                        v4 = (v17 + (load32((v1 + 8996)) + v8))
                        if ((v17 + (load32((v1 + 8996)) + v8)) > v11):
                            v1 = (v7 + v17)
                            v19 = (v7 if (v1 < v7) else (v7 + v17))
                            v20 = (v24 * load32(v18 + 208))
                            v3 = 0
                            v1 = v11
                            while True:  # $label3
                                v1 = (v1 + 1)
                                v21 = (((v1 + 1) + v20) * v24)
                                v2 = v7
                                while True:  # $label2
                                    while True:  # $label1
                                        if (v2 != v19):
                                            v2 = (v2 + 1)
                                            if (load32((v32 + (((v2 + 1) + v21) << 2))) == v30):
                                                continue
                                            break
                                        break
                                    v3 = (v1 >= v4)
                                    if (v1 != v4):
                                        continue
                                    break
                                break
                            if not (v3 & 1):
                                break
                        v3 = 0
                        while True:  # $label9
                            while True:  # $label5
                                v4 = (v7 - v10)
                                v19 = (v7 + v15)
                                if ((v7 - v10) >= (v7 + v15)):
                                    break
                                v1 = (v11 - v10)
                                v20 = (v11 + v15)
                                if ((v11 - v10) >= (v11 + v15)):
                                    break
                                while True:  # $label8
                                    if (u32(v4) < u32(v13)):
                                        v2 = (v4 - v7)
                                        v21 = (((v4 - v7) * v2) - 1)
                                        v2 = v1
                                        while True:  # $label7
                                            while True:  # $label6
                                                v28 = (v2 - v11)
                                                if ((v21 + ((v2 - v11) * v28)) > v27):
                                                    break
                                                if (u32(v2) >= u32(v13)):
                                                    break
                                                if ((v2 | v4) < 0):
                                                    break
                                                v3 = (v3 + not load16u((v31 + (((v2 * v13) + v4) << 1))))
                                                break
                                            v2 = (v2 + 1)
                                            if ((v2 + 1) != v20):
                                                continue
                                            break
                                    v4 = (v4 + 1)
                                    if ((v4 + 1) != v19):
                                        continue
                                    break
                                if (u32(v3) > u32(v5)):
                                    break
                                break
                            if (v3 != v5):
                                break
                            if (((v14 & 0xFFFFFFFF) >> 1) != v26):
                                break
                            break
                        v5 = v3
                        v14 = v6
                        break
                    v6 = (v6 + 1)
                    if ((v6 + 1) != 8):
                        continue
                    break
                while True:  # $label18
                    if not v5:
                        v4 = (v8 + 2)
                        v14 = (v9 + 2)
                        v7 = (v8 - 1)
                        v11 = (v9 - 1)
                        v26 = load32(v18 + 208)
                        v27 = (v24 * load32(v18 + 208))
                        v25 = ((v25 * 404) + ENTITY_TYPES)
                        v10 = load32(9142432)
                        v19 = (load32(9142432) + (((v13 * v22) + v23) << 2))
                        v18 = load32(9215880)
                        v16 = 1
                        while True:  # $label24
                            while True:  # $label11
                                if (v11 >= v14):
                                    break
                                if (v4 <= v7):
                                    break
                                v20 = (v14 - 1)
                                v21 = (v4 - 1)
                                v1 = v11
                                while True:  # $label23
                                    if (u32(v1) < u32(v13)):
                                        v28 = (v1 == v20)
                                        v35 = (v1 == v11)
                                        v2 = (v1 + v17)
                                        v36 = (v1 if (v1 > v2) else (v1 + v17))
                                        v3 = v7
                                        while True:  # $label22
                                            while True:  # $label12
                                                if not (v28 | ((v35 | (v3 == v7)) | (v3 == v21))):
                                                    break
                                                if (u32(v3) >= u32(v13)):
                                                    break
                                                if ((v1 | v3) < 0):
                                                    break
                                                v2 = 1
                                                if (u32(v26) <= u32(1)):
                                                    if v10:
                                                    else:
                                                    v15 = 0
                                                    while True:  # $label15
                                                        while True:  # $label14
                                                            while True:  # $label13
                                                                # br_table load32(v25 + 264)
                                                                break
                                                                break
                                                            if not v10:
                                                                v5 = 0
                                                                break
                                                            v5 = load32(v19)
                                                            break
                                                            break
                                                        v5 = 0
                                                        if not v17:
                                                            break
                                                        if not v10:
                                                            break
                                                        v29 = load32(v25 + 220)
                                                        if not load32(v25 + 220):
                                                            break
                                                        if not v18:
                                                            break
                                                        v37 = load32(v18)
                                                        v6 = 0
                                                        while True:  # $label17
                                                            v38 = (v6 + v23)
                                                            v2 = 0
                                                            while True:  # $label16
                                                                v5 = load32((v10 + ((v38 + ((v2 + v22) * v13)) << 2)))
                                                                if not load32((v37 + (load32((v10 + ((v38 + ((v2 + v22) * v13)) << 2))) << 2))):
                                                                    break
                                                                v2 = (v2 + 1)
                                                                if ((v2 + 1) != v29):
                                                                    continue
                                                                break
                                                            v5 = 0
                                                            v6 = (v6 + 1)
                                                            if ((v6 + 1) != v17):
                                                                continue
                                                            break
                                                        break
                                                else:
                                                if not 1:
                                                    break
                                                if load16u((v31 + (((v3 * v13) + v1) << 1))):
                                                    break
                                                v5 = 0
                                                v6 = v3
                                                v15 = (v3 + v17)
                                                if ((v3 + v17) <= v3):
                                                    break
                                                while True:  # $label21
                                                    v6 = (v6 + 1)
                                                    v29 = (((v6 + 1) + v27) * v24)
                                                    v2 = v1
                                                    while True:  # $label20
                                                        while True:  # $label19
                                                            if (v2 != v36):
                                                                v2 = (v2 + 1)
                                                                if (load32((v32 + (((v2 + 1) + v29) << 2))) == v30):
                                                                    continue
                                                                break
                                                            break
                                                        v5 = (v6 >= v15)
                                                        if (v6 != v15):
                                                            continue
                                                        break
                                                    break
                                                if (v5 & 1):
                                                    break
                                                break
                                            v3 = (v3 + 1)
                                            if ((v3 + 1) != v4):
                                                continue
                                            break
                                    v1 = (v1 + 1)
                                    if ((v1 + 1) != v14):
                                        continue
                                    break
                                break
                            v4 = (v4 + 1)
                            v14 = (v14 + 1)
                            v16 = (v16 + 1)
                            v7 = (v8 - (v16 + 1))
                            v11 = (v9 - v16)
                            if (v16 != 250):
                                continue
                            break
                        break
                    v1 = (v14 << 3)
                    v8 = (load32(((v14 << 3) + 8996)) + v8)
                    v9 = (load32((v1 + 8992)) + v9)
                    v16 = (v16 + 1)
                    if ((v16 + 1) != 8):
                        continue
                    break
                    break
                break
            v9 = v1
            v8 = v3
            break
        if ((v9 == v34) & (v8 == v33)):
            break
        if ((v9 == v23) & (v8 == v22)):
            break
        if load8u(9147210):
            store32(v12 + 40, 0)
            store64(v12 + 32, 0)
            store64(v12 + 24, 270582939648)
            store32(v12 + 20, v8)
            store32(v12 + 16, v9)
            store32(v12 + 12, load32(arg0 + 28))
            func41(5, (v12 + 12), 1, (v12 + 16), 7)
            break
        store16(arg0 + 118, v8)
        store16(arg0 + 116, v9)
        break
    G.global0 = (v12 + 48)
    return 0

# ----------------------------------------------------------
# $func788
# ----------------------------------------------------------
def func788(arg0, arg1):
    while True:  # $label0
        if (load8u(arg1 + 125) == 3):
            break
        while True:  # $label18
            if not load32(arg0 + 8):
                if (u32(load32(arg0 + 104)) < u32(7)):
                    break
                v2 = load32(arg0 + 96)
                v4 = load32(arg1 + 76)
                v3 = load32(arg1 + 76)
                while True:  # $label6
                    while True:  # $label5
                        while True:  # $label4
                            while True:  # $label3
                                while True:  # $label2
                                    while True:  # $label1
                                        v5 = load32(arg0 + 16)
                                        # br_table load32(arg0 + 16)
                                        break
                                        break
                                    arg0 = load32(v2)
                                    if (load32(v2) != 2147483647):
                                        store32(arg1 + 52, arg0)
                                    arg0 = load32(v2 + 4)
                                    if (load32(v2 + 4) != 2147483647):
                                        store32(arg1 + 60, arg0)
                                    while True:  # $label7
                                        arg0 = load32(v2 + 8)
                                        if (load32(v2 + 8) == 2147483647):
                                            break
                                        store32(arg1 + 64, arg0)
                                        if (load32(v2 + 8) == 2147483647):
                                            break
                                        store32(arg1 + 68, load32(v2 + 12))
                                        break
                                    while True:  # $label8
                                        arg0 = load32(v2 + 16)
                                        if (load32(v2 + 16) == 2147483647):
                                            break
                                        store32(arg1 + 72, arg0)
                                        if (load32(v2 + 16) == 2147483647):
                                            break
                                        v3 = load32(v2 + 20)
                                        store32(arg1 + 76, load32(v2 + 20))
                                        break
                                    arg0 = load32(v2 + 24)
                                    if (load32(v2 + 24) == 2147483647):
                                        break
                                    store32(arg1 + 84, arg0)
                                    break
                                    break
                                arg0 = load32(v2)
                                if (load32(v2) != 2147483647):
                                    store32(arg1 + 52, (load32(arg1 + 52) + arg0))
                                arg0 = load32(v2 + 4)
                                if (load32(v2 + 4) != 2147483647):
                                    store32(arg1 + 60, (load32(arg1 + 60) + arg0))
                                while True:  # $label9
                                    arg0 = load32(v2 + 8)
                                    if (load32(v2 + 8) == 2147483647):
                                        break
                                    store32(arg1 + 64, (load32(arg1 + 64) + arg0))
                                    if (load32(v2 + 8) == 2147483647):
                                        break
                                    store32(arg1 + 68, (load32(arg1 + 68) + load32(v2 + 12)))
                                    break
                                while True:  # $label10
                                    arg0 = load32(v2 + 16)
                                    if (load32(v2 + 16) == 2147483647):
                                        break
                                    store32(arg1 + 72, (load32(arg1 + 72) + arg0))
                                    if (load32(v2 + 16) == 2147483647):
                                        break
                                    v3 = (load32(v2 + 20) + v4)
                                    store32(arg1 + 76, (load32(v2 + 20) + v4))
                                    break
                                arg0 = load32(v2 + 24)
                                if (load32(v2 + 24) == 2147483647):
                                    break
                                store32(arg1 + 84, (load32(arg1 + 84) + arg0))
                                break
                                break
                            arg0 = load32(v2)
                            if (load32(v2) != 2147483647):
                                store32(arg1 + 52, (load32(arg1 + 52) - arg0))
                            arg0 = load32(v2 + 4)
                            if (load32(v2 + 4) != 2147483647):
                                store32(arg1 + 60, (load32(arg1 + 60) - arg0))
                            while True:  # $label11
                                arg0 = load32(v2 + 8)
                                if (load32(v2 + 8) == 2147483647):
                                    break
                                store32(arg1 + 64, (load32(arg1 + 64) - arg0))
                                if (load32(v2 + 8) == 2147483647):
                                    break
                                store32(arg1 + 68, (load32(arg1 + 68) - load32(v2 + 12)))
                                break
                            while True:  # $label12
                                arg0 = load32(v2 + 16)
                                if (load32(v2 + 16) == 2147483647):
                                    break
                                store32(arg1 + 72, (load32(arg1 + 72) - arg0))
                                if (load32(v2 + 16) == 2147483647):
                                    break
                                v3 = (v4 - load32(v2 + 20))
                                store32(arg1 + 76, (v4 - load32(v2 + 20)))
                                break
                            arg0 = load32(v2 + 24)
                            if (load32(v2 + 24) == 2147483647):
                                break
                            store32(arg1 + 84, (load32(arg1 + 84) - arg0))
                            break
                            break
                        arg0 = load32(v2)
                        if (load32(v2) != 2147483647):
                            store32(arg1 + 52, (load32(arg1 + 52) * arg0))
                        arg0 = load32(v2 + 4)
                        if (load32(v2 + 4) != 2147483647):
                            store32(arg1 + 60, (load32(arg1 + 60) * arg0))
                        while True:  # $label13
                            arg0 = load32(v2 + 8)
                            if (load32(v2 + 8) == 2147483647):
                                break
                            store32(arg1 + 64, (load32(arg1 + 64) * arg0))
                            if (load32(v2 + 8) == 2147483647):
                                break
                            store32(arg1 + 68, (load32(arg1 + 68) * load32(v2 + 12)))
                            break
                        while True:  # $label14
                            arg0 = load32(v2 + 16)
                            if (load32(v2 + 16) == 2147483647):
                                break
                            store32(arg1 + 72, (load32(arg1 + 72) * arg0))
                            if (load32(v2 + 16) == 2147483647):
                                break
                            v3 = (load32(v2 + 20) * v4)
                            store32(arg1 + 76, (load32(v2 + 20) * v4))
                            break
                        arg0 = load32(v2 + 24)
                        if (load32(v2 + 24) == 2147483647):
                            break
                        store32(arg1 + 84, (load32(arg1 + 84) * arg0))
                        break
                        break
                    arg0 = load32(v2)
                    if (load32(v2) != 2147483647):
                        # TODO: i32.div_u
                        store32(load32(arg1 + 52) + 52, arg0)
                    arg0 = load32(v2 + 4)
                    if (load32(v2 + 4) != 2147483647):
                        # TODO: i32.div_u
                        store32(load32(arg1 + 60) + 60, arg0)
                    while True:  # $label15
                        arg0 = load32(v2 + 8)
                        if (load32(v2 + 8) == 2147483647):
                            break
                        # TODO: i32.div_u
                        store32(load32(arg1 + 64) + 64, arg0)
                        if (load32(v2 + 8) == 2147483647):
                            break
                        # TODO: i32.div_u
                        store32(load32(arg1 + 68) + 68, load32(v2 + 12))
                        break
                    while True:  # $label16
                        arg0 = load32(v2 + 16)
                        if (load32(v2 + 16) == 2147483647):
                            break
                        # TODO: i32.div_u
                        store32(load32(arg1 + 72) + 72, arg0)
                        if (load32(v2 + 16) == 2147483647):
                            break
                        # TODO: i32.div_u
                        v3 = load32(v2 + 20)
                        store32(v4 + 76, load32(v2 + 20))
                        break
                    arg0 = load32(v2 + 24)
                    if (load32(v2 + 24) == 2147483647):
                        break
                    # TODO: i32.div_u
                    store32(load32(arg1 + 84) + 84, arg0)
                    break
                v2 = ((load8u(arg1 + 122) * 404) + ENTITY_TYPES)
                arg0 = load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 264)
                while True:  # $label17
                    if not load32(v2 + 92):
                        if (arg0 == 2):
                            break
                        store32(arg1 + 52, 0)
                    if (arg0 != 1):
                        break
                    store64(arg1 + 72, 0)
                    v3 = 0
                    store32(arg1 + 60, 0)
                    break
                v2 = load32(arg1 + 64)
                if load32(arg1 + 64):
                    arg0 = (2147483646 if (v5 != 2) else 0)
                    if (u32(load32(arg1 + 52)) >= u32(2147483647)):
                        store32(arg1 + 52, arg0)
                    if (u32(load32(arg1 + 60)) >= u32(2147483647)):
                        store32(arg1 + 60, arg0)
                    if (u32(v2) >= u32(2147483647)):
                        store32(arg1 + 64, arg0)
                        v2 = arg0
                    v5 = load32(arg1 + 68)
                    if (u32(load32(arg1 + 68)) >= u32(2147483647)):
                        store32(arg1 + 68, arg0)
                        v5 = arg0
                    if (u32(load32(arg1 + 72)) >= u32(2147483647)):
                        store32(arg1 + 72, arg0)
                    if (u32(v3) >= u32(2147483647)):
                        store32(arg1 + 76, arg0)
                        v3 = arg0
                    if (u32(load32(arg1 + 84)) >= u32(2147483647)):
                        store32(arg1 + 84, arg0)
                    if (u32(v2) > u32(v5)):
                        store32(arg1 + 64, v5)
                    if not v3:
                        break
                    if v4:
                        break
                    break
                return
            if not load32(arg0 + 36):
                store32(arg1 + 64, load32(arg1 + 68))
                break
            store32(arg1 + 72, load32(arg1 + 76))
            break
        if not load32(arg1 + 92):
            break
        if load32(9140316):
            if (load32(9140320) != load32(arg1 + 28)):
                break
        break

# ----------------------------------------------------------
# $func790
# ----------------------------------------------------------
def func790(arg0, arg1):
    while True:  # $label0
        while True:  # $label1
            # br_table (load8u(arg1 + 125) - 3)
            break
            break
        func119(0, arg1, 13, 1)
        arg0 = ((load8u(arg1 + 122) * 404) + ENTITY_TYPES)
        arg0 = load8u(arg1 + 125)
        arg0 = ((load8u(arg1 + 122) * 404) + ENTITY_TYPES)
        if load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 216):
            v5 = load32(9142840)
            v6 = load16u(arg1 + 114)
            v7 = load16u(arg1 + 112)
            while True:  # $label3
                v2 = (v2 + 1)
                v8 = ((v2 + 1) + v7)
                v3 = 0
                while True:  # $label2
                    v3 = (v3 + 1)
                    v4 = (load32(9142440) + 2)
                    store32((v5 + ((v8 + ((((v3 + 1) + v6) + ((load32(9142440) + 2) * load32(arg0 + 208))) * v4)) << 2)), load32(arg0 + 212))
                    v4 = load32(arg0 + 216)
                    if (u32(v3) < u32(load32(arg0 + 216))):
                        continue
                    break
                if (u32(v2) < u32(v4)):
                    continue
                break
        func138(arg1)
        break

# ----------------------------------------------------------
# $func792
# ----------------------------------------------------------
def func792(arg0, arg1):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if not arg0:
            break
        if not load8u(9163793):
            break
        if (u32(load32(9684392)) > u32(2)):
            break
        v5 = load32(9142856)
        v6 = load32(9142952)
        v7 = load32(9142864)
        v4 = loadf32(9671164)
        arg0 = load32(9142860)
        v8 = load32(9142956)
        v2 = loadf32(40616)
        v9 = load32(9142868)
        store32(arg1 + 12, load8u(9163792))
        while True:  # $label1
            v3 = i32(arg0)
            v3 = (((i32(arg0) - ((v2 * v3) / v4)) * 0.5) + ((v2 * i32(((v9 & 0xFFFFFFFF) >> 1))) + i32(v8)))
            if (abs((((i32(arg0) - ((v2 * v3) / v4)) * 0.5) + ((v2 * i32(((v9 & 0xFFFFFFFF) >> 1))) + i32(v8)))) < 2147483650.0):
                break
            break
        store32(i32(v3) + 8, (-2147483648 // 32))
        while True:  # $label2
            v3 = i32(v5)
            v2 = (((v2 * i32(((v7 & 0xFFFFFFFF) >> 1))) + i32(v6)) + ((i32(v5) - ((v2 * v3) / v4)) * 0.5))
            if (abs((((v2 * i32(((v7 & 0xFFFFFFFF) >> 1))) + i32(v6)) + ((i32(v5) - ((v2 * v3) / v4)) * 0.5))) < 2147483650.0):
                break
            break
        store32(i32(v2) + 4, (-2147483648 // 32))
        func71(37, 0, 0, (arg1 + 4), 3, 0)
        store32(9684392, (load32(9684392) + 1))
        break
    G.global0 = (arg1 + 16)
    return arg1

# ----------------------------------------------------------
# $func794
# ----------------------------------------------------------
def func794():
    v0 = G.global1
    if not load32(G.global1):
        store32(v0, 1)
        v0 = func372(9688236, G.global3)
        func54(9688236)
        while True:  # $label0
            if not v0:
                break
            if load32(v0 + 32):
                break
            func248(0, v0)
            break
        store32(G.global1, 0)

# ----------------------------------------------------------
# $func797
# ----------------------------------------------------------
def func797(arg0, arg1, arg2):
    arg0 = 0
    if (load32(59164) == load32(9142384)):
        store32(9143000, 0)
        v3 = load32(9213820)
        if load32(9213820):
            func47(entities[v3])
            store32(9213820, 0)
        func45()
    if arg2:
        while True:  # $label0
            func202(entities[load32((arg1 + (arg0 << 2)))], 1, 0)
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break
    if (load32(59164) == load32(9142384)):

# ----------------------------------------------------------
# $func798
# ----------------------------------------------------------
def func798(arg0):
    v2 = (G.global0 - 40032)
    G.global0 = (G.global0 - 40032)
    while True:  # $label6
        if load8u(9163792):
            v4 = load32(9213808)
            if load32(9213808):
                # TODO: memory.copy
            store32(9143000, 0)
            arg0 = load32(9213820)
            if load32(9213820):
                func47(entities[arg0])
                store32(9213820, 0)
            func45()
            if v4:
                while True:  # $label5
                    while True:  # $label0
                        v8 = entities[load32(((v2 + 32) + (v7 << 2)))]
                        arg0 = load32(entities[load32(((v2 + 32) + (v7 << 2)))].y)
                        if not load32(entities[load32(((v2 + 32) + (v7 << 2)))].y):
                            break
                        if not load32(arg0 + 8):
                            break
                        v6 = 0
                        while True:  # $label4
                            while True:  # $label1
                                arg0 = entities[load32((load32(arg0) + (v6 << 2)))]
                                if load32(entities[load32((load32(arg0) + (v6 << 2)))].flags):
                                    break
                                v3 = load32(9213808)
                                if (u32(load32(9213808)) > u32(9999)):
                                    break
                                if (load8u(arg0 + 125) == 3):
                                    break
                                store32(((v3 << 2) + 9173808), load32(arg0 + 28))
                                v1 = 1
                                store32(9213808, (v3 + 1))
                                while True:  # $label2
                                    if (load8u(9142906) | load8u(9142916)):
                                        break
                                    v1 = 0
                                    if load8u(9142917):
                                        break
                                    v1 = load32(9299880)
                                    if load32(9299880):
                                        v1 = (v1 - 1)
                                        store32(9299880, (v1 - 1))
                                        v1 = load32((load32(9299872) + (v1 << 2)))
                                        break
                                    v1 = load32(9163776)
                                    v3 = (load32(9163776) + 1)
                                    store32(9163776, (load32(9163776) + 1))
                                    v5 = load32(9163784)
                                    if (u32(v3) < u32(load32(9163784))):
                                        break
                                    store32(v2 + 16, v5)
                                    a_b()
                                    store32(9163784, (load32(9163784) + 40000))
                                    break
                                store32(arg0 + 92, v1)
                                if not load32(arg0 + 36):
                                if (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264) != 1):
                                    break
                                if load32(arg0 + 80):
                                    break
                                v3 = load16u(arg0 + 116)
                                if not load16u(arg0 + 116):
                                    break
                                v5 = load16u(arg0 + 118)
                                if not load16u(arg0 + 118):
                                    break
                                if not load8u(9147152):
                                    if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(arg0 + 110))))):
                                        break
                                    if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                                        break
                                    if (load8u(arg0 + 127) == 6):
                                        break
                                v1 = 0
                                while True:  # $label3
                                    if load8u(9142917):
                                        break
                                    v1 = load32(9299880)
                                    if load32(9299880):
                                        v1 = (v1 - 1)
                                        store32(9299880, (v1 - 1))
                                        v1 = load32((load32(9299872) + (v1 << 2)))
                                        break
                                    v1 = load32(9163776)
                                    v9 = (load32(9163776) + 1)
                                    store32(9163776, (load32(9163776) + 1))
                                    v10 = load32(9163784)
                                    if (u32(v9) < u32(load32(9163784))):
                                        break
                                    store32(v2, v10)
                                    a_b()
                                    store32(9163784, (load32(9163784) + 40000))
                                    v5 = load16u(arg0 + 118)
                                    v3 = load16u(arg0 + 116)
                                    break
                                store32(arg0 + 80, v1)
                                break
                            v6 = (v6 + 1)
                            arg0 = load32(v8 + 16)
                            if (u32((v6 + 1)) < u32(load32(load32(v8 + 16) + 8))):
                                continue
                            break
                        break
                    v7 = (v7 + 1)
                    if ((v7 + 1) != v4):
                        continue
                    break
            break
        store32(v2 + 32, 0)
        arg0 = load32(9213808)
        if load8u(9147210):
            func41(6, 9173808, arg0, (v2 + 32), 1)
            break
        v4 = (arg0 << 2)
        v1 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy
        break
    G.global0 = (v2 + 40032)

# ----------------------------------------------------------
# $func799
# ----------------------------------------------------------
def func799():
    v0 = e()
    if e():
        atomic_store(v0 + 8, 0)
        store32(v0 + 184, 0)
        store32(v0 + 4, 0)
    return v0

# ----------------------------------------------------------
# $xd
# Export: xd
# ----------------------------------------------------------
def xd(arg0):
    """Export: xd"""
    if load32(9213808):
        func256(entities[load32(9173808)], arg0)

# ----------------------------------------------------------
# $func805
# ----------------------------------------------------------
def func805(arg0):
    v8 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v3 = load32(arg0 + 12)
    v5 = (load32(arg0 + 12) + 16)
    v9 = func234((load32(arg0 + 12) + 16), 0)
    while True:  # $label0
        v1 = load32(v3)
        if not load32(v3):
            break
        if not load8u(9142916):
            while True:  # $label1
                v2 = (v5 + (v4 * 60))
                if (load32((v5 + (v4 * 60)) + 32) == 3):
                    store32(v2 + 28, (load32(9140308) + ((load32(9568052) & 0xFFFFFFFF) >> 2)))
                    store32(9568052, (load32(9568052) + ((load32(v2) * (load32(v2 + 4) + 2)) << 2)))
                    v1 = load32(9568048)
                    store32(9568048, (load32(9568048) + 1))
                    store32(((v1 << 2) + 9563952), v2)
                    v1 = load32(v3)
                v4 = (v4 + 1)
                if (u32((v4 + 1)) < u32(v1)):
                    continue
                break
                break
            raise Unreachable()
        while True:  # $label2
            v2 = (v5 + (v4 * 60))
            if (load32((v5 + (v4 * 60)) + 32) == 3):
                v1 = load32(59152)
                store32(59152, (load32(59152) + 1))
                store32(v2 + 28, v1)
                v1 = load32(v2)
                v7 = load32(v2 + 4)
                v6 = load32(9568048)
                store32(9568048, (load32(9568048) + 1))
                store32(((v6 << 2) + 9563952), v2)
                store32(9568052, (load32(9568052) + ((v1 * (v7 + 2)) << 2)))
                v1 = load32(v3)
            v4 = (v4 + 1)
            if (u32((v4 + 1)) < u32(v1)):
                continue
            break
        break
    v2 = load32(9140308)
    v4 = load32(9568052)
    v1 = (load32(59156) << 2)
    v3 = (load32(9568052) % (load32(59156) << 2))
    if (load32(9568052) % (load32(59156) << 2)):
        v4 = ((v4 - v3) + v1)
        store32(9568052, ((v4 - v3) + v1))
    store32(9140308, (((v4 & 0xFFFFFFFF) >> 2) + v2))
    v1 = func26(20)
    v3 = load32(9568048)
    store32(v1 + 8, v4)
    store32(v1 + 4, v2)
    store32(v1, v3)
    v4 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
    store32(v1 + 16, arg0)
    store32(v1 + 12, v4)
    while True:  # $label3
        if not v3:
            break
        arg0 = 0
        v4 = 0
        if (u32(v3) >= u32(4)):
            v7 = (v3 & -4)
            v2 = 0
            while True:  # $label4
                v5 = (v4 << 2)
                store32(((v4 << 2) + load32(v1 + 12)), load32((v5 + 9563952)))
                v6 = (v5 | 4)
                store32(((v5 | 4) + load32(v1 + 12)), load32((v6 + 9563952)))
                v6 = (v5 | 8)
                store32(((v5 | 8) + load32(v1 + 12)), load32((v6 + 9563952)))
                v5 = (v5 | 12)
                store32(((v5 | 12) + load32(v1 + 12)), load32((v5 + 9563952)))
                v4 = (v4 + 4)
                v2 = (v2 + 4)
                if ((v2 + 4) != v7):
                    continue
                break
        v2 = (v3 & 3)
        if not (v3 & 3):
            break
        while True:  # $label5
            v3 = (v4 << 2)
            store32(((v4 << 2) + load32(v1 + 12)), load32((v3 + 9563952)))
            v4 = (v4 + 1)
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != v2):
                continue
            break
        break
    func186((v8 + 12), 0, 59, v1)
    store32(9568052, 0)
    store32(9568048, 0)
    arg0 = load32(9671136)
    if (u32(load32(9671136)) >= u32(4)):
        v2 = load32(ENTITIES)
        v4 = 3
        while True:  # $label11
            while True:  # $label6
                v3 = (v2 + (v4 * 132))
                v1 = load8u((v2 + (v4 * 132)) + 125)
                if (load8u((v2 + (v4 * 132)) + 125) == 3):
                    break
                if (v9 != load8u(v3 + 122)):
                    break
                v5 = load32(v3 + 40)
                while True:  # $label7
                    arg0 = load32(9299880)
                    if (load32(9299880) != load32(9299876)):
                        v2 = load32(9299872)
                        break
                    v2 = (load32(9299884) + arg0)
                    store32(9299876, (load32(9299884) + arg0))
                    v1 = load32(9299872)
                    v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                    if arg0:
                        # TODO: memory.copy
                    if v1:
                        arg0 = load32(9299880)
                    store32(9299872, v2)
                    v1 = load8u(v3 + 125)
                    break
                store32(9299880, (arg0 + 1))
                store32((v2 + (arg0 << 2)), v5)
                store32(v3 + 40, 0)
                arg0 = (v1 & 255)
                v2 = (((v1 & 255) != 4) & (arg0 != 14))
                while True:  # $label10
                    while True:  # $label9
                        while True:  # $label8
                            # br_table (arg0 - 4)
                            break
                            break
                        arg0 = ((load8u(v3 + 122) * 404) + ENTITY_TYPES)
                        v1 = load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 356)
                        if load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 356):
                            break
                        v1 = 9142636
                        v5 = load32(arg0 + 216)
                        arg0 = load32(arg0 + 220)
                        arg0 = (load32(arg0 + 216) if (u32(arg0) < u32(v5)) else load32(arg0 + 220))
                        arg0 = ((6 if (u32(arg0) >= u32(6)) else (load32(arg0 + 216) if (u32(arg0) < u32(v5)) else load32(arg0 + 220))) - 1)
                        if (u32(((6 if (u32(arg0) >= u32(6)) else (load32(arg0 + 216) if (u32(arg0) < u32(v5)) else load32(arg0 + 220))) - 1)) >= u32(5)):
                            break
                        v1 = load32(((arg0 << 2) + 10132))
                        break
                        break
                    v1 = ((load8u(v3 + 122) * 72) + 9263856)
                    break
                arg0 = load32(9671136)
                v2 = load32(ENTITIES)
                break
            v4 = (v4 + 1)
            if (u32((v4 + 1)) < u32(arg0)):
                continue
            break
    while True:  # $label12
        if not load32(9671176):
            break
        if (load32(load32(9671168)) != v9):
            break
        break
    G.global0 = (v8 + 16)

# ----------------------------------------------------------
# $func808
# ----------------------------------------------------------
def func808(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v3 = load64(arg0 + 32)
    if (load64(arg0 + 32) != 0):
        while True:  # $label0
            v2 = ((i64(load64(arg0 + 24)) * 100.0) / i64(v3))
            if ((((i64(load64(arg0 + 24)) * 100.0) / i64(v3)) < 4294967296.0) & (v2 >= 0.0)):
                break
            break
        store32(i32(v2), 0)
    G.global0 = (v1 + 16)
    return v1

# ----------------------------------------------------------
# $we
# Export: we
# ----------------------------------------------------------
def we(arg0, arg1, arg2):
    """Export: we"""
    v3 = (G.global0 - 240)
    G.global0 = (G.global0 - 240)
    store8(40588, arg0)
    store16(v3 + 52, load16u(3837))
    store16(v3 + 60, load16u(2478))
    store8(v3 + 43, 5)
    store32(v3 + 32, load32(3119))
    store8(v3 + 36, load8u(3123))
    store8(v3 + 37, 0)
    store64(v3 + 44, load64(3829))
    store8(v3 + 67, 6)
    store16(v3 + 54, 2560)
    store32(v3 + 56, load32(2474))
    store8(v3 + 79, 4)
    store8(v3 + 62, 0)
    store8(v3 + 72, 0)
    store8(v3 + 100, 0)
    store16(v3 + 84, load16u(3518))
    store16(v3 + 108, load16u(4775))
    store8(v3 + 91, 6)
    store32(v3 + 68, 2003791475)
    store8(v3 + 103, 8)
    store8(v3 + 86, 0)
    store64(v3 + 92, 7236828769417322866)
    store8(v3 + 115, 6)
    store8(v3 + 127, 5)
    store8(v3 + 110, 0)
    store32(v3 + 80, load32(3514))
    store32(v3 + 104, load32(4771))
    store8(v3 + 136, 0)
    store8(v3 + 120, load8u(7806))
    store8(v3 + 139, 8)
    store8(v3 + 121, 0)
    store64(v3 + 128, 8606218855064367719)
    store32(v3 + 116, load32(7802))
    store32(59156, arg2)
    store32(9687252, 0)
    store32(9568092, arg1)
    while True:  # $label0
        arg0 = load8u(9147213)
        if (load8u(9147213) | load8u(9147212)):
        else:
            arg0 = load32(9142440)
            store32(9147288, func26((load32(9142440) * arg0)))
            func402(arg0)
        if (load8u(9147213) & 255):
            break
        if (u32(arg1) >= u32(2)):
            arg2 = load8u(59184)
            arg0 = (22 if load8u(59184) else 6)
            v4 = (2117 if arg2 else 2133)
            while True:  # $label1
                if arg2:
                    v5 = (arg0 | 15)
                    arg2 = func26(((arg0 | 15) + 1))
                    store32(v3 + 28, (v5 - 2147483647))
                    store32(v3 + 20, arg2)
                    store32(v3 + 24, arg0)
                    break
                store8(v3 + 31, arg0)
                arg2 = (v3 + 20)
                break
            # TODO: memory.copy
            store8((arg0 + arg2), 0)
            arg0 = (v3 + 8)
            arg0 = func211(arg0, 8178)
            store32(v3 + 152, load32(func211(arg0, 8178) + 8))
            store64(v3 + 144, load64(arg0))
            store64(arg0, 0)
            store32(arg0 + 8, 0)
            arg0 = load8u(v3 + 155)
            arg1 = (i32(load8u(v3 + 155)) < 0)
            if (load8s(v3 + 155) < 0):
            if (load8s(v3 + 19) < 0):
            arg0 = load8s(v3 + 31)
            while True:  # $label2
                if (load8s(9681935) >= 0):
                    if (arg0 >= 0):
                        store64(9681924, load64(v3 + 20))
                        store32(9681932, load32(v3 + 28))
                        break
                    arg2 = load32(v3 + 20)
                    arg0 = load32(v3 + 24)
                    arg1 = (G.global0 - 16)
                    G.global0 = (G.global0 - 16)
                    while True:  # $label3
                        if (u32(arg0) <= u32(10)):
                            store8(9681935, ((load8u(9681935) & 128) | arg0))
                            store8(9681935, (load8u(9681935) & 127))
                            func122(9681924, arg2, arg0)
                            store8(arg1 + 15, 0)
                            store8((arg0 + 9681924), load8u(arg1 + 15))
                            break
                        v4 = (load8u(9681935) & 127)
                        break
                    G.global0 = (arg1 + 16)
                    break
                arg1 = (arg0 < 0)
                arg2 = (load32(v3 + 20) if (arg0 < 0) else (v3 + 20))
                arg0 = (load32(v3 + 24) if arg1 else (arg0 & 255))
                arg1 = (G.global0 - 16)
                G.global0 = (G.global0 - 16)
                while True:  # $label4
                    v4 = (load32(9681932) & 2147483647)
                    if (u32(arg0) < u32((load32(9681932) & 2147483647))):
                        v4 = load32(9681924)
                        store32(9681928, arg0)
                        func122(v4, arg2, arg0)
                        store8(arg1 + 15, 0)
                        store8((arg0 + v4), load8u(arg1 + 15))
                        break
                    v4 = load32(9681928)
                    break
                G.global0 = (arg1 + 16)
                break
            arg0 = (v3 + 20)
            arg1 = load32(v3 + 20)
            arg2 = load8s(v3 + 31)
            v4 = (v3 + 144)
            # TODO: memory.fill
            store32(v3 + 144, 5522759)
            store32(v3 + 188, 102)
            store32(v3 + 180, 103)
            store32(v3 + 184, 56)
            store32(v3 + 196, (1 if load8u(59184) else (5 if load8u(59185) else 1)))
            func179(v4, (arg1 if (arg2 < 0) else arg0))
            if (load8s(v3 + 31) >= 0):
                break
            break
        arg0 = (v3 + 144)
        # TODO: memory.fill
        store32(v3 + 144, 5522759)
        store32(v3 + 188, 102)
        store32(v3 + 180, 103)
        store32(v3 + 184, 56)
        store32(v3 + 196, (1 if load8u(59184) else (5 if load8u(59185) else 1)))
        func179(arg0, 7765)
        break
    store32(v3 + 28, 0)
    store8(v3 + 27, 0)
    store8(v3 + 31, 7)
    store32(v3 + 20, load32(8172))
    store32(v3 + 23, load32(8175))
    arg2 = ((v3 + 32) + (load32(load32(GAME_STATE) + 24) * 12))
    arg0 = load8u(arg2 + 11)
    v5 = i32(arg0)
    v4 = (load32(((v3 + 32) + (load32(load32(GAME_STATE) + 24) * 12)) + 4) if (i32(arg0) < 0) else load8u(arg2 + 11))
    arg0 = ((load32(((v3 + 32) + (load32(load32(GAME_STATE) + 24) * 12)) + 4) if (i32(arg0) < 0) else load8u(arg2 + 11)) + 5)
    if (u32(((load32(((v3 + 32) + (load32(load32(GAME_STATE) + 24) * 12)) + 4) if (i32(arg0) < 0) else load8u(arg2 + 11)) + 5)) < u32(2147483632)):
        while True:  # $label5
            if (u32(arg0) <= u32(10)):
                store32(v3 + 152, 0)
                store64(v3 + 144, 0)
                store8(v3 + 155, arg0)
                arg1 = (v3 + 144)
                break
            v6 = ((arg0 | 15) + 1)
            arg1 = func26(((arg0 | 15) + 1))
            store32(v3 + 148, arg0)
            store32(v3 + 144, arg1)
            store32(v3 + 152, (v6 | -2147483648))
            break
        if v4:
            # TODO: memory.copy
        arg0 = (arg1 + v4)
        store8((arg1 + v4) + 5, 0)
        store8(arg0 + 4, load8u(7782))
        store32(arg0, load32(7778))
        arg0 = load8s(v3 + 155)
        arg1 = (load8s(v3 + 155) < 0)
        if (load8s(v3 + 155) < 0):
        arg0 = load32(v3 + 20)
        arg1 = load8s(v3 + 31)
        arg2 = (v3 + 144)
        # TODO: memory.fill
        store32(v3 + 144, 5522759)
        store32(v3 + 188, 104)
        store32(v3 + 180, 103)
        store32(v3 + 184, 56)
        store32(v3 + 196, (1 if load8u(59184) else (5 if load8u(59185) else 1)))
        func179(arg2, (arg0 if (arg1 < 0) else (v3 + 20)))
        if (load8s(v3 + 31) < 0):
        if (load8s(v3 + 139) < 0):
        if (load8s(v3 + 127) < 0):
        if (load8s(v3 + 115) < 0):
        if (load8s(v3 + 103) < 0):
        if (load8s(v3 + 91) < 0):
        if (load8s(v3 + 79) < 0):
        if (load8s(v3 + 67) < 0):
        if (load8s(v3 + 55) < 0):
        if (load8s(v3 + 43) < 0):
        G.global0 = (v3 + 240)
        return af(load32(v3 + 32))
    func212()
    raise Unreachable()
    return af(load32(v3 + 44))

# ----------------------------------------------------------
# $func810
# ----------------------------------------------------------
def func810(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v2 = load32(arg0 + 8)
    store32(v1 + 4, load16u(arg0 + 42))
    store32(v1, v2)
    func383(func363(8863, v1), arg0)
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $func811
# ----------------------------------------------------------
def func811(arg0, arg1):
    while True:  # $label3
        while True:  # $label2
            while True:  # $label1
                while True:  # $label0
                    # br_table (arg0 - 1)
                    break
                    break
                break
                break
            arg0 = G.global3
            break
        break
    v15 = arg0
    if (arg0 == G.global3):
    else:
    if 0:
    else:
        v6 = (G.global0 - 32)
        G.global0 = (G.global0 - 32)
        store32(v6 + 28, arg1)
        store32(v6 + 16, arg1)
        store32(v6 + 24, 0)
        store32(v6 + 20, 422)
        store64(v6 + 8, load64(v6 + 20))
        v9 = (G.global0 - 16)
        G.global0 = (G.global0 - 16)
        while True:  # $label16
            while True:  # $label15
                arg0 = func372(9688236, v15)
                if not func372(9688236, v15):
                    arg0 = load32(9688264)
                    if (load32(9688264) == load32(9688268)):
                        while True:  # $label4
                            v16 = ((arg0 << 1) if arg0 else 1)
                            v7 = (((arg0 << 1) if arg0 else 1) << 2)
                            arg0 = 0
                            v10 = load32(9688260)
                            if not load32(9688260):
                                break
                            if (u32(v7) >= u32(-64)):
                                store32(G.global3 + 28, 48)
                                break
                            while True:  # $label5
                                if (load8u(MEM_FLAGS) & 2):
                                    if func55(MEM_MUTEX):
                                        break
                                while True:  # $label6
                                    v4 = (16 if (u32(v7) < u32(11)) else ((v7 + 11) & -8))
                                    arg1 = (v10 - 8)
                                    v8 = load32((v10 - 8) + 4)
                                    v2 = (load32((v10 - 8) + 4) & -8)
                                    while True:  # $label7
                                        if not (v8 & 3):
                                            if (u32(v4) < u32(256)):
                                                break
                                            if (u32((v4 + 4)) <= u32(v2)):
                                                arg0 = arg1
                                                if (u32((v2 - v4)) <= u32((load32(9690448) << 1))):
                                                    break
                                            break
                                        v5 = (arg1 + v2)
                                        while True:  # $label8
                                            if (u32(v2) >= u32(v4)):
                                                arg0 = (v2 - v4)
                                                if (u32((v2 - v4)) < u32(16)):
                                                    break
                                                store32(arg1 + 4, (((v8 & 1) | v4) | 2))
                                                v2 = (arg1 + v4)
                                                store32((arg1 + v4) + 4, (arg0 | 3))
                                                store32(v5 + 4, (load32(v5 + 4) | 1))
                                                break
                                            if (load32(HEAP_END) == v5):
                                                v2 = (load32(HEAP_TOTAL) + v2)
                                                if (u32((load32(HEAP_TOTAL) + v2)) <= u32(v4)):
                                                    break
                                                store32(arg1 + 4, (((v8 & 1) | v4) | 2))
                                                arg0 = (arg1 + v4)
                                                v2 = (v2 - v4)
                                                store32((arg1 + v4) + 4, ((v2 - v4) | 1))
                                                store32(HEAP_TOTAL, v2)
                                                store32(HEAP_END, arg0)
                                                break
                                            if (load32(HEAP_TOP) == v5):
                                                v2 = (load32(FREE_SIZE) + v2)
                                                if (u32((load32(FREE_SIZE) + v2)) < u32(v4)):
                                                    break
                                                while True:  # $label9
                                                    arg0 = (v2 - v4)
                                                    if (u32((v2 - v4)) >= u32(16)):
                                                        store32(arg1 + 4, (((v8 & 1) | v4) | 2))
                                                        v3 = (arg1 + v4)
                                                        store32((arg1 + v4) + 4, (arg0 | 1))
                                                        v2 = (arg1 + v2)
                                                        store32((arg1 + v2), arg0)
                                                        store32(v2 + 4, (load32(v2 + 4) & -2))
                                                        break
                                                    store32(arg1 + 4, (((v8 & 1) | v2) | 2))
                                                    arg0 = (arg1 + v2)
                                                    store32((arg1 + v2) + 4, (load32(arg0 + 4) | 1))
                                                    arg0 = 0
                                                    break
                                                store32(HEAP_TOP, v3)
                                                store32(FREE_SIZE, arg0)
                                                break
                                            v3 = load32(v5 + 4)
                                            if (load32(v5 + 4) & 2):
                                                break
                                            v11 = ((v3 & -8) + v2)
                                            if (u32(((v3 & -8) + v2)) < u32(v4)):
                                                break
                                            v13 = (v11 - v4)
                                            while True:  # $label10
                                                if (u32(v3) <= u32(255)):
                                                    arg0 = load32(v5 + 12)
                                                    v2 = load32(v5 + 8)
                                                    if (load32(v5 + 12) == load32(v5 + 8)):
                                                        store32(HEAP_FREELIST, (load32(HEAP_FREELIST) & rotl(-2, ((v3 & 0xFFFFFFFF) >> 3))))
                                                        break
                                                    store32(v2 + 12, arg0)
                                                    store32(arg0 + 8, v2)
                                                    break
                                                v12 = load32(v5 + 24)
                                                while True:  # $label11
                                                    v2 = load32(v5 + 12)
                                                    if (v5 != load32(v5 + 12)):
                                                        arg0 = load32(v5 + 8)
                                                        store32(load32(v5 + 8) + 12, v2)
                                                        store32(v2 + 8, arg0)
                                                        break
                                                    while True:  # $label12
                                                        v3 = (v5 + 20)
                                                        arg0 = load32((v5 + 20))
                                                        if load32((v5 + 20)):
                                                            break
                                                        v3 = (v5 + 16)
                                                        arg0 = load32((v5 + 16))
                                                        if load32((v5 + 16)):
                                                            break
                                                        v2 = 0
                                                        break
                                                        break
                                                    while True:  # $label13
                                                        v14 = v3
                                                        v2 = arg0
                                                        v3 = (arg0 + 20)
                                                        arg0 = load32((arg0 + 20))
                                                        if load32((arg0 + 20)):
                                                            continue
                                                        v3 = (v2 + 16)
                                                        arg0 = load32(v2 + 16)
                                                        if load32(v2 + 16):
                                                            continue
                                                        break
                                                    store32(v14, 0)
                                                    break
                                                if not v12:
                                                    break
                                                while True:  # $label14
                                                    arg0 = load32(v5 + 28)
                                                    v3 = ((load32(v5 + 28) << 2) + 9690768)
                                                    if (load32(((load32(v5 + 28) << 2) + 9690768)) == v5):
                                                        store32(v3, v2)
                                                        if v2:
                                                            break
                                                        store32(HEAP_TREE, (load32(HEAP_TREE) & rotl(-2, arg0)))
                                                        break
                                                    store32((v12 + (16 if (load32(v12 + 16) == v5) else 20)), v2)
                                                    if not v2:
                                                        break
                                                    break
                                                store32(v2 + 24, v12)
                                                arg0 = load32(v5 + 16)
                                                if load32(v5 + 16):
                                                    store32(v2 + 16, arg0)
                                                    store32(arg0 + 24, v2)
                                                arg0 = load32(v5 + 20)
                                                if not load32(v5 + 20):
                                                    break
                                                store32(v2 + 20, arg0)
                                                store32(arg0 + 24, v2)
                                                break
                                            if (u32(v13) <= u32(15)):
                                                store32(arg1 + 4, (((v8 & 1) | v11) | 2))
                                                arg0 = (arg1 + v11)
                                                store32((arg1 + v11) + 4, (load32(arg0 + 4) | 1))
                                                break
                                            store32(arg1 + 4, (((v8 & 1) | v4) | 2))
                                            arg0 = (arg1 + v4)
                                            store32((arg1 + v4) + 4, (v13 | 3))
                                            v2 = (arg1 + v11)
                                            store32((arg1 + v11) + 4, (load32(v2 + 4) | 1))
                                            break
                                        arg0 = arg1
                                        break
                                    break
                                arg0 = arg0
                                if (load8u(MEM_FLAGS) & 2):
                                    func54(MEM_MUTEX)
                                if arg0:
                                    break
                                arg0 = e()
                                if not e():
                                    break
                                arg1 = load32((v10 - 4))
                                arg1 = ((-4 if (load32((v10 - 4)) & 3) else -8) + (arg1 & -8))
                                break
                            break
                        arg0 = arg0
                        if not arg0:
                            break
                        store32(9688268, v16)
                        store32(9688260, arg0)
                    arg0 = func393(v15)
                    if not func393(v15):
                        break
                    arg1 = load32(9688264)
                    store32(9688264, (load32(9688264) + 1))
                    store32((load32(9688260) + (arg1 << 2)), arg0)
                break
                break
            break
        arg1 = 0
        func54(9688236)
        if arg1:
            store32(v9 + 8, load32(v6 + 16))
            store64(v9, load64(v6 + 8))
            arg0 = (G.global0 - 48)
            G.global0 = (G.global0 - 48)
            while True:  # $label17
                v3 = load32(arg1 + 28)
                v2 = atomic_load(load32(arg1 + 28) + 124)
                while True:  # $label18
                    if not v2:
                        break
                    # TODO: i32.atomic.rmw.cmpxchg
                    v2 = (v2 + 1)
                    if (v2 != (v2 + 1)):
                        continue
                    break
                break
            if 1:
                v2 = (arg1 + 4)
                store32(arg0 + 32, load32(v9 + 8))
                store64(arg0 + 24, load64(v9))
                v3 = func391(arg1, (arg0 + 24))
                func54(v2)
                while True:  # $label19
                    if v3:
                        # TODO: i32.atomic.rmw.xchg
                        v3 = 2
                        v2 = load32(arg1 + 28)
                        if (v3 == 2):
                            break
                        store32(arg0 + 44, arg1)
                        store32(arg0 + 16, arg1)
                        store32(arg0 + 40, 423)
                        store32(arg0 + 36, 424)
                        store64(arg0 + 8, load64(arg0 + 36))
                        v3 = (G.global0 - 16)
                        G.global0 = (G.global0 - 16)
                        v14 = load32(v2 + 120)
                        store32(v3 + 8, load32(arg0 + 16))
                        store64(v3, load64(arg0 + 8))
                        func54((load32(v2 + 120) + 4))
                        while True:  # $label20
                            # TODO: i32.atomic.rmw.xchg
                            if (2 == 2):
                                break
                            if atomic_load(v2 + 128):
                                # TODO: memory.atomic.notify
                                break
                            a_u()
                            break
                        G.global0 = (v3 + 16)
                    break
                arg1 = load32(arg1 + 28)
                # TODO: i32.atomic.rmw.sub
                if (1 == 1):
                    func111((arg1 + 124), 2147483647)
            G.global0 = (arg0 + 48)
        G.global0 = (v9 + 16)
        G.global0 = (v6 + 32)
    return 0

# ----------------------------------------------------------
# $func814
# ----------------------------------------------------------
def func814(arg0, arg1, arg2):
    v4 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v3 = load32(PLAYER_COUNT)
    while True:  # $label0
        while True:  # $label1
            if load8u(9147210):
                if (u32(v3) < u32(2)):
                    break
                arg2 = load32(59164)
                v6 = load32(PLAYERS)
                arg1 = 1
                while True:  # $label2
                    v5 = (v6 + (arg1 * 286704))
                    if (load32((v6 + (arg1 * 286704)) + 284616) == arg2):
                        break
                    if (load32(v5 + 284628) == arg2):
                        break
                    arg1 = (arg1 + 1)
                    if ((arg1 + 1) != v3):
                        continue
                    break
                arg1 = 0
                break
            arg1 = load32(CURRENT_PLAYER)
            break
        if (u32(v3) < u32(2)):
            break
        v5 = load32(arg0)
        v6 = load32(PLAYERS)
        arg2 = 1
        while True:  # $label4
            while True:  # $label3
                v7 = (v6 + (arg2 * 286704))
                if (load32((v6 + (arg2 * 286704)) + 284616) == v5):
                    break
                if (load32(v7 + 284628) == v5):
                    break
                arg2 = (arg2 + 1)
                if ((arg2 + 1) != v3):
                    continue
                break
                break
            break
        if (u32(arg2) >= u32(v3)):
            break
        if (arg1 == arg2):
            break
        if not load32(9147136):
            break
        v11 = load32(arg0 + 4)
        v9 = (v6 + (arg2 * 286704))
        v8 = ((v6 + (arg2 * 286704)) + 281800)
        arg0 = load32(v9 + 281800)
        if not load32(v9 + 281800):
            v5 = (-1 if (u32(v3) > u32(1073741823)) else (v3 << 2))
            arg0 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
            # TODO: memory.fill
            store32(v8, arg0)
        v5 = (v6 + (arg1 * 286704))
        v10 = ((v6 + (arg1 * 286704)) + 281800)
        v7 = load32(v5 + 281800)
        if load32(v5 + 281800):
        else:
            arg0 = (-1 if (u32(v3) > u32(1073741823)) else (v3 << 2))
            v7 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
            # TODO: memory.fill
            store32(v10, v7)
        arg0 = load32((load32(v8) + (arg1 << 2)))
        if load32((load32(v8) + (arg1 << 2))):
            if (u32(((load32(9142848) - arg0) * 25)) < u32(60000)):
                break
        arg0 = load8u((load32(9143004) + (arg2 + (arg1 * v3))))
        if not v11:
            while True:  # $label5
                if arg0:
                    break
                if (load32(CURRENT_PLAYER) != arg2):
                    break
                arg0 = (v6 + (arg1 * 286704))
                v3 = load32((v6 + (arg1 * 286704)) + 284628)
                arg0 = load32(arg0 + 284616)
                store32(v4 + 4, v5)
                store32(v4, 914)
                store32(v4 + 8, (arg0 if arg0 else v3))
                a_b()
                break
            func176(arg2, arg1, 1)
            break
        if not arg0:
            break
        while True:  # $label6
            if not load32(9147132):
                break
            if (load32(9142440) != 4096):
                break
            if (u32(func385(v5)) > u32(2)):
                break
            v7 = load32(v10)
            break
        if load32((v7 + (arg2 << 2))):
            while True:  # $label7
                if not load32(9147132):
                    break
                if (load32(9142440) != 4096):
                    break
                if (u32(func385(v9)) < u32(3)):
                    break
                a_b()
                break
                break
            func176(arg2, arg1, 0)
            if (load32(CURRENT_PLAYER) != arg2):
                break
            arg0 = (v6 + (arg1 * 286704))
            arg1 = load32((v6 + (arg1 * 286704)) + 284628)
            arg0 = load32(arg0 + 284616)
            store32(v4 + 36, v5)
            store32(v4 + 32, 916)
            store32(v4 + 40, (arg0 if arg0 else arg1))
            a_b()
            break
        store32((load32(v8) + (arg1 << 2)), load32(9142848))
        if (load32(CURRENT_PLAYER) != arg2):
            break
        store32(v4 + 16, load32((v6 + (arg1 * 286704)) + 284616))
        a_b()
        break
    G.global0 = (v4 + 48)
    return (v4 + 16)

# ----------------------------------------------------------
# $me
# Export: me
# ----------------------------------------------------------
def me():
    """Export: me"""
    v0 = load32(9681976)
    if load32(9681976):
        store32(9681976, 0)

# ----------------------------------------------------------
# $func819
# ----------------------------------------------------------
def func819(arg0, arg1):
    while True:  # $label0
        if (arg1 == -1):
            break
        if arg1:
            func38(arg1)
        if (u32(load32(load32(GAME_STATE) + 48)) < u32(2)):
            break
        v6 = load32(9142836)
        v7 = load32(load32(9142836) + 964)
        if not load32(load32(9142836) + 964):
            break
        v8 = ((arg0 & 0xFFFFFFFF) >> 16)
        v9 = (arg0 & 65535)
        arg0 = load32(9142440)
        arg1 = 0
        while True:  # $label2
            while True:  # $label1
                v2 = load32(v6 + 960)
                v3 = (arg1 << 2)
                v4 = load32((load32(v6 + 960) + ((arg1 << 2) | 4)))
                v5 = (load32((load32(v6 + 960) + ((arg1 << 2) | 4))) + v8)
                if (u32(arg0) <= u32((load32((load32(v6 + 960) + ((arg1 << 2) | 4))) + v8))):
                    break
                v2 = load32((v2 + v3))
                v3 = (load32((v2 + v3)) + v9)
                if (u32(arg0) <= u32((load32((v2 + v3)) + v9))):
                    break
                if ((v3 | v5) < 0):
                    break
                if ((((v2 * v2) + (v4 * v4)) - 1) > 64):
                    break
                arg0 = load32(9142440)
                break
            arg1 = (arg1 + 2)
            if (u32((arg1 + 2)) < u32(v7)):
                continue
            break
        break

# ----------------------------------------------------------
# $gc
# Export: gc
# ----------------------------------------------------------
def gc(arg0):
    """Export: gc"""
    arg0 = ((arg0 << 2) + 9682208)
    v1 = load32(((arg0 << 2) + 9682208))
    if load32(((arg0 << 2) + 9682208)):
        store32(arg0, 0)

# ----------------------------------------------------------
# $func822
# ----------------------------------------------------------
def func822(arg0, arg1):
    while True:  # $label7
        while True:  # $label2
            while True:  # $label3
                while True:  # $label0
                    if (u32(load32(arg0 + 116)) > u32(261)):
                        break
                    v2 = load32(arg0 + 116)
                    while True:  # $label1
                        if arg1:
                            break
                        if (u32(v2) >= u32(262)):
                            break
                        return 0
                        break
                    if not v2:
                        break
                    if (u32(v2) > u32(2)):
                        break
                    v2 = load32(arg0 + 96)
                    store32(arg0 + 120, load32(arg0 + 96))
                    store32(arg0 + 100, load32(arg0 + 112))
                    v4 = 2
                    store32(arg0 + 96, 2)
                    break
                    break
                v4 = 2
                v3 = load32(arg0 + 108)
                v2 = (load32(arg0 + 84) & (load8u((load32(arg0 + 108) + load32(arg0 + 56)) + 2) ^ (load32(arg0 + 72) << load32(arg0 + 88))))
                store32(arg0 + 72, (load32(arg0 + 84) & (load8u((load32(arg0 + 108) + load32(arg0 + 56)) + 2) ^ (load32(arg0 + 72) << load32(arg0 + 88)))))
                v2 = (load32(arg0 + 68) + (v2 << 1))
                v5 = load16u((load32(arg0 + 68) + (v2 << 1)))
                store16((load32(arg0 + 64) + ((v3 & load32(arg0 + 52)) << 1)), load16u((load32(arg0 + 68) + (v2 << 1))))
                store16(v2, v3)
                v2 = load32(arg0 + 96)
                store32(arg0 + 120, load32(arg0 + 96))
                store32(arg0 + 100, load32(arg0 + 112))
                store32(arg0 + 96, 2)
                if not v5:
                    break
                while True:  # $label4
                    if (u32(v2) >= u32(load32(arg0 + 128))):
                        break
                    if (u32((load32(arg0 + 44) - 262)) < u32((v3 - v5))):
                        break
                    v4 = func359(arg0, v5)
                    store32(arg0 + 96, func359(arg0, v5))
                    if (u32(v4) > u32(5)):
                        break
                    if (load32(arg0 + 136) != 1):
                        if (v4 != 3):
                            break
                        v4 = 3
                        if (u32((load32(arg0 + 108) - load32(arg0 + 112))) < u32(4097)):
                            break
                    v4 = 2
                    store32(arg0 + 96, 2)
                    break
                v2 = load32(arg0 + 120)
                break
            while True:  # $label5
                if (u32(v2) < u32(3)):
                    break
                if (u32(v2) < u32(v4)):
                    break
                v3 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                v5 = load32(arg0 + 116)
                v6 = load32(arg0 + 108)
                v3 = (load32(arg0 + 108) + (load32(arg0 + 100) ^ -1))
                store8((v3 + load32(arg0 + 5784)), (load32(arg0 + 108) + (load32(arg0 + 100) ^ -1)))
                v4 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v4 + load32(arg0 + 5784)), ((v3 & 0xFFFFFFFF) >> 8))
                v4 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                v2 = (v2 - 3)
                store8((v4 + load32(arg0 + 5784)), (v2 - 3))
                v2 = (((load8u(((v2 & 255) + 23984)) << 2) + arg0) + 1176)
                store16((((load8u(((v2 & 255) + 23984)) << 2) + arg0) + 1176), (load16u(v2) + 1))
                v2 = ((v3 - 1) & 65535)
                v2 = ((arg0 + (load8u(((((v3 - 1) & 65535) if (u32(v2) < u32(256)) else (((v2 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2440)
                store16(((arg0 + (load8u(((((v3 - 1) & 65535) if (u32(v2) < u32(256)) else (((v2 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2440), (load16u(v2) + 1))
                v2 = load32(arg0 + 120)
                v4 = (load32(arg0 + 120) - 2)
                store32(arg0 + 120, (load32(arg0 + 120) - 2))
                store32(arg0 + 116, ((load32(arg0 + 116) - v2) + 1))
                v5 = ((v5 + v6) - 3)
                v2 = load32(arg0 + 108)
                v6 = load32(arg0 + 5796)
                v8 = load32(arg0 + 5792)
                while True:  # $label6
                    v3 = v2
                    v2 = (v2 + 1)
                    store32(arg0 + 108, (v2 + 1))
                    if (u32(v2) <= u32(v5)):
                        v7 = (load32(arg0 + 84) & (load8u((v3 + load32(arg0 + 56)) + 3) ^ (load32(arg0 + 72) << load32(arg0 + 88))))
                        store32(arg0 + 72, (load32(arg0 + 84) & (load8u((v3 + load32(arg0 + 56)) + 3) ^ (load32(arg0 + 72) << load32(arg0 + 88)))))
                        v7 = (load32(arg0 + 68) + (v7 << 1))
                        store16((load32(arg0 + 64) + ((load32(arg0 + 52) & v2) << 1)), load16u((load32(arg0 + 68) + (v7 << 1))))
                        store16(v7, v2)
                    v4 = (v4 - 1)
                    store32(arg0 + 120, (v4 - 1))
                    if v4:
                        continue
                    break
                store32(arg0 + 96, 2)
                store32(arg0 + 104, 0)
                v3 = (v3 + 2)
                store32(arg0 + 108, (v3 + 2))
                if (v6 != v8):
                    continue
                v4 = 0
                v2 = load32(arg0 + 92)
                if (load32(arg0 + 92) >= 0):
                else:
                store32(arg0 + 92, load32(arg0 + 108))
                v2 = load32(arg0)
                v3 = load32(load32(arg0) + 28)
                while True:  # $label8
                    v4 = load32(v3 + 20)
                    v5 = load32(v2 + 16)
                    v4 = (load32(v3 + 20) if (u32(v4) < u32(v5)) else load32(v2 + 16))
                    if not (load32(v3 + 20) if (u32(v4) < u32(v5)) else load32(v2 + 16)):
                        break
                    store32(v2 + 12, (load32(v2 + 12) + v4))
                    store32(v3 + 16, (load32(v3 + 16) + v4))
                    store32(v2 + 20, (load32(v2 + 20) + v4))
                    store32(v2 + 16, (load32(v2 + 16) - v4))
                    v2 = load32(v3 + 20)
                    store32(v3 + 20, (load32(v3 + 20) - v4))
                    if (v2 != v4):
                        break
                    store32(v3 + 16, load32(v3 + 8))
                    break
                if load32(load32(arg0) + 16):
                    continue
                return 0
                break
            if load32(arg0 + 104):
                v2 = load8u(((load32(arg0 + 108) + load32(arg0 + 56)) - 1))
                v3 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v3 + load32(arg0 + 5784)), 0)
                v3 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v3 + load32(arg0 + 5784)), 0)
                v3 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v3 + load32(arg0 + 5784)), v2)
                v2 = (arg0 + (v2 << 2))
                store16(((arg0 + (v2 << 2)) + 148), (load16u(v2 + 148) + 1))
                while True:  # $label9
                    if (load32(arg0 + 5792) != load32(arg0 + 5796)):
                        break
                    v4 = 0
                    v2 = load32(arg0 + 92)
                    if (load32(arg0 + 92) >= 0):
                    else:
                    store32(arg0 + 92, load32(arg0 + 108))
                    v2 = load32(arg0)
                    v3 = load32(load32(arg0) + 28)
                    v4 = load32(v3 + 20)
                    v5 = load32(v2 + 16)
                    v4 = (load32(v3 + 20) if (u32(v4) < u32(v5)) else load32(v2 + 16))
                    if not (load32(v3 + 20) if (u32(v4) < u32(v5)) else load32(v2 + 16)):
                        break
                    store32(v2 + 12, (load32(v2 + 12) + v4))
                    store32(v3 + 16, (load32(v3 + 16) + v4))
                    store32(v2 + 20, (load32(v2 + 20) + v4))
                    store32(v2 + 16, (load32(v2 + 16) - v4))
                    v2 = load32(v3 + 20)
                    store32(v3 + 20, (load32(v3 + 20) - v4))
                    if (v2 != v4):
                        break
                    store32(v3 + 16, load32(v3 + 8))
                    break
                store32(arg0 + 108, (load32(arg0 + 108) + 1))
                store32(arg0 + 116, (load32(arg0 + 116) - 1))
                if load32(load32(arg0) + 16):
                    continue
                return 0
            else:
                store32(arg0 + 104, 1)
                store32(arg0 + 108, (load32(arg0 + 108) + 1))
                store32(arg0 + 116, (load32(arg0 + 116) - 1))
                continue
            raise Unreachable()
            break
        break
    if load32(arg0 + 104):
        v2 = load8u(((load32(arg0 + 108) + load32(arg0 + 56)) - 1))
        v3 = load32(arg0 + 5792)
        store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
        store8((v3 + load32(arg0 + 5784)), 0)
        v3 = load32(arg0 + 5792)
        store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
        store8((v3 + load32(arg0 + 5784)), 0)
        v3 = load32(arg0 + 5792)
        store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
        store8((v3 + load32(arg0 + 5784)), v2)
        v2 = (arg0 + (v2 << 2))
        store16(((arg0 + (v2 << 2)) + 148), (load16u(v2 + 148) + 1))
        store32(arg0 + 104, 0)
    v2 = load32(arg0 + 108)
    store32(arg0 + 5812, (2 if (u32(v2) >= u32(2)) else load32(arg0 + 108)))
    if (arg1 == 4):
        v4 = 0
        arg1 = load32(arg0 + 92)
        if (load32(arg0 + 92) >= 0):
        else:
        store32(arg0 + 92, load32(arg0 + 108))
        arg1 = load32(arg0)
        v2 = load32(load32(arg0) + 28)
        while True:  # $label10
            v3 = load32(v2 + 20)
            v4 = load32(arg1 + 16)
            v3 = (load32(v2 + 20) if (u32(v3) < u32(v4)) else load32(arg1 + 16))
            if not (load32(v2 + 20) if (u32(v3) < u32(v4)) else load32(arg1 + 16)):
                break
            store32(arg1 + 12, (load32(arg1 + 12) + v3))
            store32(v2 + 16, (load32(v2 + 16) + v3))
            store32(arg1 + 20, (load32(arg1 + 20) + v3))
            store32(arg1 + 16, (load32(arg1 + 16) - v3))
            arg1 = load32(v2 + 20)
            store32(v2 + 20, (load32(v2 + 20) - v3))
            if (arg1 != v3):
                break
            store32(v2 + 16, load32(v2 + 8))
            break
        return (3 if load32(load32(arg0) + 16) else 2)
    while True:  # $label11
        if not load32(arg0 + 5792):
            break
        v4 = 0
        arg1 = load32(arg0 + 92)
        if (load32(arg0 + 92) >= 0):
        else:
        store32(arg0 + 92, load32(arg0 + 108))
        arg1 = load32(arg0)
        v2 = load32(load32(arg0) + 28)
        while True:  # $label12
            v3 = load32(v2 + 20)
            v4 = load32(arg1 + 16)
            v3 = (load32(v2 + 20) if (u32(v3) < u32(v4)) else load32(arg1 + 16))
            if not (load32(v2 + 20) if (u32(v3) < u32(v4)) else load32(arg1 + 16)):
                break
            store32(arg1 + 12, (load32(arg1 + 12) + v3))
            store32(v2 + 16, (load32(v2 + 16) + v3))
            store32(arg1 + 20, (load32(arg1 + 20) + v3))
            store32(arg1 + 16, (load32(arg1 + 16) - v3))
            arg1 = load32(v2 + 20)
            store32(v2 + 20, (load32(v2 + 20) - v3))
            if (arg1 != v3):
                break
            store32(v2 + 16, load32(v2 + 8))
            break
        if load32(load32(arg0) + 16):
            break
        return 0
        break
    return 1

# ----------------------------------------------------------
# $func823
# ----------------------------------------------------------
def func823(arg0, arg1):
    while True:  # $label1
        while True:  # $label6
            while True:  # $label3
                while True:  # $label2
                    if (u32(load32(arg0 + 116)) <= u32(261)):
                        v2 = load32(arg0 + 116)
                        while True:  # $label0
                            if arg1:
                                break
                            if (u32(v2) >= u32(262)):
                                break
                            return 0
                            break
                        if not v2:
                            break
                        if (u32(v2) < u32(3)):
                            break
                    v4 = load32(arg0 + 108)
                    v2 = (load32(arg0 + 84) & (load8u((load32(arg0 + 108) + load32(arg0 + 56)) + 2) ^ (load32(arg0 + 72) << load32(arg0 + 88))))
                    store32(arg0 + 72, (load32(arg0 + 84) & (load8u((load32(arg0 + 108) + load32(arg0 + 56)) + 2) ^ (load32(arg0 + 72) << load32(arg0 + 88)))))
                    v2 = (load32(arg0 + 68) + (v2 << 1))
                    v3 = load16u((load32(arg0 + 68) + (v2 << 1)))
                    store16((load32(arg0 + 64) + ((v4 & load32(arg0 + 52)) << 1)), load16u((load32(arg0 + 68) + (v2 << 1))))
                    store16(v2, v4)
                    if not v3:
                        break
                    if (u32((load32(arg0 + 44) - 262)) < u32((v4 - v3))):
                        break
                    v3 = func359(arg0, v3)
                    store32(arg0 + 96, func359(arg0, v3))
                    break
                    break
                v3 = load32(arg0 + 96)
                break
            while True:  # $label7
                if (u32(v3) >= u32(3)):
                    v2 = load32(arg0 + 5792)
                    store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                    v4 = (load32(arg0 + 108) - load32(arg0 + 112))
                    store8((v2 + load32(arg0 + 5784)), (load32(arg0 + 108) - load32(arg0 + 112)))
                    v2 = load32(arg0 + 5792)
                    store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                    store8((v2 + load32(arg0 + 5784)), ((v4 & 0xFFFFFFFF) >> 8))
                    v2 = load32(arg0 + 5792)
                    store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                    v2 = (v3 - 3)
                    store8((v2 + load32(arg0 + 5784)), (v3 - 3))
                    v2 = (((load8u(((v2 & 255) + 23984)) << 2) + arg0) + 1176)
                    store16((((load8u(((v2 & 255) + 23984)) << 2) + arg0) + 1176), (load16u(v2) + 1))
                    v2 = ((v4 - 1) & 65535)
                    v2 = ((arg0 + (load8u(((((v4 - 1) & 65535) if (u32(v2) < u32(256)) else (((v2 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2440)
                    store16(((arg0 + (load8u(((((v4 - 1) & 65535) if (u32(v2) < u32(256)) else (((v2 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2440), (load16u(v2) + 1))
                    v3 = load32(arg0 + 96)
                    v2 = (load32(arg0 + 116) - load32(arg0 + 96))
                    store32(arg0 + 116, (load32(arg0 + 116) - load32(arg0 + 96)))
                    v8 = load32(arg0 + 5796)
                    v9 = load32(arg0 + 5792)
                    while True:  # $label4
                        if (u32(v3) > u32(load32(arg0 + 128))):
                            break
                        if (u32(v2) < u32(3)):
                            break
                        v6 = (v3 - 1)
                        store32(arg0 + 96, (v3 - 1))
                        v7 = load32(arg0 + 72)
                        v3 = load32(arg0 + 108)
                        v10 = load32(arg0 + 52)
                        v11 = load32(arg0 + 64)
                        v12 = load32(arg0 + 68)
                        v13 = load32(arg0 + 84)
                        v14 = load32(arg0 + 56)
                        v5 = load32(arg0 + 88)
                        while True:  # $label5
                            v2 = v3
                            v3 = (v3 + 1)
                            store32(arg0 + 108, (v3 + 1))
                            v7 = ((load8u((v2 + v14) + 3) ^ (v7 << v5)) & v13)
                            store32(arg0 + 72, ((load8u((v2 + v14) + 3) ^ (v7 << v5)) & v13))
                            v4 = (v12 + (v7 << 1))
                            store16((v11 + ((v3 & v10) << 1)), load16u((v12 + (v7 << 1))))
                            store16(v4, v3)
                            v6 = (v6 - 1)
                            store32(arg0 + 96, (v6 - 1))
                            if v6:
                                continue
                            break
                        v3 = (v2 + 2)
                        store32(arg0 + 108, (v2 + 2))
                        if (v8 != v9):
                            continue
                        break
                        break
                    store32(arg0 + 96, 0)
                    v3 = (load32(arg0 + 108) + v3)
                    store32(arg0 + 108, (load32(arg0 + 108) + v3))
                    v4 = (load32(arg0 + 56) + v3)
                    v2 = load8u((load32(arg0 + 56) + v3))
                    store32(arg0 + 72, load8u((load32(arg0 + 56) + v3)))
                    store32(arg0 + 72, (load32(arg0 + 84) & (load8u(v4 + 1) ^ (v2 << load32(arg0 + 88)))))
                    if (v8 != v9):
                        continue
                    break
                v3 = load8u((load32(arg0 + 56) + load32(arg0 + 108)))
                v2 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v2 + load32(arg0 + 5784)), 0)
                v2 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v2 + load32(arg0 + 5784)), 0)
                v2 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v2 + load32(arg0 + 5784)), v3)
                v2 = (arg0 + (v3 << 2))
                store16(((arg0 + (v3 << 2)) + 148), (load16u(v2 + 148) + 1))
                store32(arg0 + 116, (load32(arg0 + 116) - 1))
                v3 = (load32(arg0 + 108) + 1)
                store32(arg0 + 108, (load32(arg0 + 108) + 1))
                if (load32(arg0 + 5792) != load32(arg0 + 5796)):
                    continue
                break
            v6 = 0
            v2 = load32(arg0 + 92)
            if (load32(arg0 + 92) >= 0):
            else:
            store32(arg0 + 92, load32(arg0 + 108))
            v5 = load32(arg0)
            v4 = load32(load32(arg0) + 28)
            while True:  # $label8
                v3 = load32(v4 + 20)
                v2 = load32(v5 + 16)
                v3 = (load32(v4 + 20) if (u32(v2) > u32(v3)) else load32(v5 + 16))
                if not (load32(v4 + 20) if (u32(v2) > u32(v3)) else load32(v5 + 16)):
                    break
                store32(v5 + 12, (load32(v5 + 12) + v3))
                store32(v4 + 16, (load32(v4 + 16) + v3))
                store32(v5 + 20, (load32(v5 + 20) + v3))
                store32(v5 + 16, (load32(v5 + 16) - v3))
                v2 = load32(v4 + 20)
                store32(v4 + 20, (load32(v4 + 20) - v3))
                if (v2 != v3):
                    break
                store32(v4 + 16, load32(v4 + 8))
                break
            if load32(load32(arg0) + 16):
                continue
            break
        return 0
        break
    v2 = load32(arg0 + 108)
    store32(arg0 + 5812, (2 if (u32(v2) >= u32(2)) else load32(arg0 + 108)))
    if (arg1 == 4):
        v6 = 0
        arg1 = load32(arg0 + 92)
        if (load32(arg0 + 92) >= 0):
        else:
        store32(arg0 + 92, load32(arg0 + 108))
        v4 = load32(arg0)
        v3 = load32(load32(arg0) + 28)
        while True:  # $label9
            v2 = load32(v3 + 20)
            arg1 = load32(v4 + 16)
            v2 = (load32(v3 + 20) if (u32(arg1) > u32(v2)) else load32(v4 + 16))
            if not (load32(v3 + 20) if (u32(arg1) > u32(v2)) else load32(v4 + 16)):
                break
            store32(v4 + 12, (load32(v4 + 12) + v2))
            store32(v3 + 16, (load32(v3 + 16) + v2))
            store32(v4 + 20, (load32(v4 + 20) + v2))
            store32(v4 + 16, (load32(v4 + 16) - v2))
            arg1 = load32(v3 + 20)
            store32(v3 + 20, (load32(v3 + 20) - v2))
            if (arg1 != v2):
                break
            store32(v3 + 16, load32(v3 + 8))
            break
        return (3 if load32(load32(arg0) + 16) else 2)
    while True:  # $label10
        if not load32(arg0 + 5792):
            break
        v6 = 0
        arg1 = load32(arg0 + 92)
        if (load32(arg0 + 92) >= 0):
        else:
        store32(arg0 + 92, load32(arg0 + 108))
        v4 = load32(arg0)
        v3 = load32(load32(arg0) + 28)
        while True:  # $label11
            v2 = load32(v3 + 20)
            arg1 = load32(v4 + 16)
            v2 = (load32(v3 + 20) if (u32(arg1) > u32(v2)) else load32(v4 + 16))
            if not (load32(v3 + 20) if (u32(arg1) > u32(v2)) else load32(v4 + 16)):
                break
            store32(v4 + 12, (load32(v4 + 12) + v2))
            store32(v3 + 16, (load32(v3 + 16) + v2))
            store32(v4 + 20, (load32(v4 + 20) + v2))
            store32(v4 + 16, (load32(v4 + 16) - v2))
            arg1 = load32(v3 + 20)
            store32(v3 + 20, (load32(v3 + 20) - v2))
            if (arg1 != v2):
                break
            store32(v3 + 16, load32(v3 + 8))
            break
        if load32(load32(arg0) + 16):
            break
        return 0
        break
    return 1

# ----------------------------------------------------------
# $func824
# ----------------------------------------------------------
def func824(arg0, arg1, param2):
    v19 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # $label1
        while True:  # $label0
            while True:  # $label2
                v5 = load32(ENTITIES)
                v6 = entities[arg0]
                v2 = load8u(entities[arg0].sub_state)
                # br_table (load8u(entities[arg0].sub_state) + -64)
                break
                break
            if (v2 != 10):
                break
            break
        while True:  # $label3
            v2 = load32(v6 + 20)
            if not load32(v6 + 20):
                break
            if (u32(load32(v2 + 8)) < u32(3)):
                break
            if (u32((load32(load32(v2)) - 1)) > u32(1)):
                break
            store32(v2 + 8, 0)
            break
        v11 = (v5 + (arg1 * 132))
        v14 = load8u((v5 + (arg1 * 132)) + 122)
        while True:  # $label5
            while True:  # $label4
                if (load8u(v11 + 125) == 10):
                    v7 = 3
                    v8 = 1
                    break
                v7 = load32(((v14 * 404) + ENTITY_TYPES) + 188)
                if (u32(load32(((v14 * 404) + ENTITY_TYPES) + 188)) >= u32(4)):
                    func29(v6, 1)
                    break
                v8 = (v7 == 3)
                # br_table v7
                break
                break
            v4 = (v5 + (arg0 * 132))
            v9 = load16u((v5 + (arg0 * 132)) + 112)
            v2 = ((load16u((v5 + (arg0 * 132)) + 112) << 5) - load32(9142952))
            v3 = load16u(v4 + 114)
            v2 = ((load16u(v4 + 114) << 5) - load32(9142956))
            if ((((((load16u((v5 + (arg0 * 132)) + 112) << 5) - load32(9142952)) * v2) + (((load16u(v4 + 114) << 5) - load32(9142956)) * v2)) - 1) > 9000000):
                break
            while True:  # $label6
                v2 = load32(load32(GAME_STATE) + 48)
                if not load32(load32(GAME_STATE) + 48):
                    break
                if load8u(9147152):
                    break
                v4 = load16u((load32(9147376) + (((load32(9142440) * v3) + v9) << 1)))
                if (v2 == 2):
                    if (u32(v4) > u32(1)):
                        break
                    break
                if not v4:
                    break
                break
            store32(v19 + 40, v3)
            store32(v19 + 36, v9)
            store32(v19 + 32, load32(((((load32(9142848) + v9) % 3) << 2) + 57224)))
            a_b()
            break
        while True:  # $label7
            if (v7 == 1):
                v4 = (v5 + (arg0 * 132))
                v9 = load16u((v5 + (arg0 * 132)) + 112)
                v2 = ((load16u((v5 + (arg0 * 132)) + 112) << 5) - load32(9142952))
                v3 = load16u(v4 + 114)
                v2 = ((load16u(v4 + 114) << 5) - load32(9142956))
                if ((((((load16u((v5 + (arg0 * 132)) + 112) << 5) - load32(9142952)) * v2) + (((load16u(v4 + 114) << 5) - load32(9142956)) * v2)) - 1) > 9000000):
                    break
                while True:  # $label8
                    v2 = load32(load32(GAME_STATE) + 48)
                    if not load32(load32(GAME_STATE) + 48):
                        break
                    if load8u(9147152):
                        break
                    v4 = load16u((load32(9147376) + (((load32(9142440) * v3) + v9) << 1)))
                    if (v2 == 2):
                        if (u32(v4) > u32(1)):
                            break
                        break
                    if not v4:
                        break
                    break
                store32(v19 + 8, v3)
                store32(v19 + 4, v9)
                store32(v19, load32(((((load32(9142848) + v9) % 11) << 2) + 57168)))
                a_b()
                break
            if (v7 != 2):
                break
            v20 = 1
            if (load32(38500) != load8u(v11 + 122)):
                break
            v4 = (v5 + (arg0 * 132))
            v9 = load16u((v5 + (arg0 * 132)) + 112)
            v2 = ((load16u((v5 + (arg0 * 132)) + 112) << 5) - load32(9142952))
            v3 = load16u(v4 + 114)
            v2 = ((load16u(v4 + 114) << 5) - load32(9142956))
            if ((((((load16u((v5 + (arg0 * 132)) + 112) << 5) - load32(9142952)) * v2) + (((load16u(v4 + 114) << 5) - load32(9142956)) * v2)) - 1) > 9000000):
                break
            while True:  # $label9
                v2 = load32(load32(GAME_STATE) + 48)
                if not load32(load32(GAME_STATE) + 48):
                    break
                if load8u(9147152):
                    break
                v4 = load16u((load32(9147376) + (((load32(9142440) * v3) + v9) << 1)))
                if (v2 == 2):
                    if (u32(v4) > u32(1)):
                        break
                    break
                if not v4:
                    break
                break
            store32(v19 + 24, v3)
            store32(v19 + 20, v9)
            store32(v19 + 16, load32(((((load32(9142848) + v9) % 3) << 2) + 57212)))
            a_b()
            break
        v17 = load32(38528)
        v12 = load8u(v11 + 122)
        v9 = (v5 + (arg0 * 132))
        if (load8u((v5 + (arg0 * 132)) + 125) == 1):
            v8 = (v12 != v17)
            if not (v20 & (v12 != v17)):
                v4 = ((v14 * 404) + ENTITY_TYPES)
                v3 = load32(((v14 * 404) + ENTITY_TYPES) + 220)
                v2 = (v5 + (arg1 * 132))
                v18 = load16u((v5 + (arg1 * 132)) + 114)
                v21 = (load32(((v14 * 404) + ENTITY_TYPES) + 220) + load16u((v5 + (arg1 * 132)) + 114))
                v4 = load32(v4 + 216)
                v17 = load16u(v2 + 112)
                v14 = (load32(v4 + 216) + load16u(v2 + 112))
                v2 = (v5 + (arg0 * 132))
                v13 = load16u((v5 + (arg0 * 132)) + 114)
                while True:  # $label11
                    while True:  # $label10
                        v15 = load16u(v2 + 112)
                        v2 = (u32(load16u(v2 + 112)) < u32(v17))
                        if (u32(load16u(v2 + 112)) < u32(v17)):
                            break
                        if (v14 <= v15):
                            break
                        if (u32(v13) < u32(v18)):
                            break
                        if (v13 >= v21):
                            break
                        v2 = ((v3 // 2) + v18)
                        v10 = (-1 if (v2 < v13) else (((v3 // 2) + v18) != v13))
                        v2 = ((v4 // 2) + v17)
                        break
                        break
                    v10 = (1 if (u32(v13) < u32(v18)) else (-1 if (v13 >= v21) else 0))
                    break
                v2 = (((1 if v2 else (-1 if (v14 <= v15) else 0)) + (v10 * 3)) + 4)
                if (u32((((1 if v2 else (-1 if (v14 <= v15) else 0)) + (v10 * 3)) + 4)) <= u32(8)):
                else:
                store8(load8u((v2 + 10184)) + 124, 6)
            v2 = load8u(v6 + 122)
            while True:  # $label12
                if (v7 == 1):
                    break
                if v20:
                    if not v8:
                        func119(func37(v6, load32(((v2 * 72) + 9263856) + 56), 0.0, 0), v11, 12, 1)
                        store32((v5 + (arg1 * 132)) + 96, 0)
                        break
                    break
                break
            v8 = (v5 + (arg0 * 132))
            store16((v5 + (arg0 * 132)) + 108, 0)
            store32(v8 + 88, 0)
            v2 = load32(((load32((load32(9215884) + (load32(v8 + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32(v8 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            if (load8u(v9 + 125) == 3):
                break
            v4 = load32(v8 + 44)
            if load32(v8 + 44):
                v2 = load32(9142848)
                v3 = load32(9215884)
                store32((load32(9215884) + (v4 << 4)) + 4, 1)
                store32((v3 + (load32(v8 + 44) << 4)) + 8, load32((v5 + (arg0 * 132)) + 28))
                store32((v3 + (load32(v8 + 44) << 4)) + 12, arg1)
                store32((v3 + (load32(v8 + 44) << 4)), (v2 + 40))
                break
            store32(v8 + 44, ((Ua(1000, 1, load32((v5 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
            break
        while True:  # $label21
            while True:  # $label18
                while True:  # $label20
                    while True:  # $label19
                        while True:  # $label17
                            if (load8u(v11 + 125) == 3):
                                if (v7 == 1):
                                    v7 = load32(ENTITIES)
                                    arg0 = (v5 + (arg0 * 132))
                                    v15 = load16u(arg0 + 110)
                                    arg0 = entities[func166(load16u((v5 + (arg0]
                                    v16 = load16u(entities[func166(load16u((v5 + (arg0].rally_y)
                                    v18 = (load16u(entities[func166(load16u((v5 + (arg0].rally_y) + 29)
                                    v5 = load16u(arg0 + 114)
                                    v21 = (load16u(arg0 + 114) + 29)
                                    v2 = (v5 - 30)
                                    arg1 = (v16 - 30)
                                    v11 = load32(9142440)
                                    v17 = (load32(9142440) + 2)
                                    v14 = ((load32(9142440) + 2) * load32(((v12 * 404) + ENTITY_TYPES) + 208))
                                    v9 = load32(9142840)
                                    v20 = 2147483647
                                    while True:  # $label15
                                        v4 = (arg1 + 1)
                                        if (u32(arg1) < u32(v11)):
                                            arg0 = (v16 - arg1)
                                            v8 = ((v16 - arg1) * arg0)
                                            arg0 = v2
                                            while True:  # $label14
                                                while True:  # $label13
                                                    v3 = arg0
                                                    if (u32(v11) <= u32(arg0)):
                                                        break
                                                    if ((arg1 | v3) < 0):
                                                        break
                                                    arg0 = (v5 - v3)
                                                    arg0 = (((v5 - v3) * arg0) + v8)
                                                    if ((((v5 - v3) * arg0) + v8) >= v20):
                                                        break
                                                    v13 = load32((v9 + (((((v3 + v14) + 1) * v17) + v4) << 2)))
                                                    if not load32((v9 + (((((v3 + v14) + 1) * v17) + v4) << 2))):
                                                        break
                                                    arg0 = (load8u((v7 + (v13 * 132)) + 122) == v12)
                                                    v20 = (arg0 if (load8u((v7 + (v13 * 132)) + 122) == v12) else v20)
                                                    v10 = (v13 if arg0 else v10)
                                                    break
                                                arg0 = (v3 + 1)
                                                if (v3 != v21):
                                                    continue
                                                break
                                        arg0 = (arg1 != v18)
                                        arg1 = v4
                                        if arg0:
                                            continue
                                        break
                                    if v10:
                                        while True:  # $label16
                                            if not load32(players[v15] + 286684):
                                                break
                                            arg1 = (v7 + (v10 * 132))
                                            arg0 = (v16 - load16u((v7 + (v10 * 132)) + 112))
                                            arg0 = (v5 - load16u(arg1 + 114))
                                            if (((((v16 - load16u((v7 + (v10 * 132)) + 112)) * arg0) + ((v5 - load16u(arg1 + 114)) * arg0)) - 1) < 50):
                                                break
                                            break
                                            break
                                        break
                                    func29(v6, 1)
                                    break
                                if (v12 == v17):
                                    v2 = load32((v5 + (arg0 * 132)) + 88)
                                    store32((v5 + (arg1 * 132)) + 72, 0)
                                    # TODO: i32.div_u
                                    break
                                func29(v6, 1)
                                break
                            if (v12 != v17):
                                break
                            v3 = (v5 + (arg1 * 132))
                            v4 = load32((v5 + (arg1 * 132)) + 72)
                            if (u32(load32((v5 + (arg1 * 132)) + 72)) > u32(3)):
                                break
                            v2 = load32((v5 + (arg0 * 132)) + 88)
                            store32(v3 + 72, 0)
                            store8(v11 + 125, 0)
                            # TODO: i32.div_u
                            break
                        v3 = (1000 + v4)
                        if load32(load32(GAME_STATE) + 176):
                            break
                        v2 = (v5 + (arg1 * 132))
                        if (u32(load32((v5 + (arg1 * 132)) + 80)) < u32(load32((players[load16u(v2 + 110)] + 284320)))):
                            break
                        break
                        break
                    store32(v3 + 72, (v4 - 3))
                    v3 = 0
                    break
                v4 = load32(ENTITIES)
                if not load32(entities[arg1].flags):
                    break
                v2 = load8u(9147141)
                if load32(9140316):
                    if (load32(9140320) != load32((v4 + (arg1 * 132)) + 28)):
                        break
                break
                break
            v3 = 0
            store32((v5 + (arg1 * 132)) + 88, load32(9142848))
            break
        v5 = load32(ENTITIES)
        v11 = entities[arg0]
        v2 = (load32(entities[arg0].direction) + 1000)
        if ((((load32(entities[arg0].direction) + 1000) == load32(((v7 << 2) + 51760))) & (v12 != v17)) | v3):
            v4 = (v5 + (arg0 * 132))
            if (v12 != v17):
            else:
            store16(load32((((load32(PLAYERS) + (load16u((v5 + (arg0 * 132)) + 110) * 286704)) + (v7 << 2)) + 283984)) + 108, v3)
            v2 = (v5 + (arg1 * 132))
            store32(v11 + 88, ((load8u((v5 + (arg1 * 132)) + 122) << 16) + v7))
            func207(v11, load32(v2 + 28))
            while True:  # $label22
                if v20:
                    break
                v20 = load16u(v4 + 108)
                while True:  # $label24
                    while True:  # $label23
                        # br_table v7
                        break
                        break
                    # TODO: i32.div_u
                    v20 = load32(((load32(PLAYERS) + (load16u((v5 + (arg0 * 132)) + 110) * 286704)) + 284100))
                    break
                if (load8u((v5 + (arg1 * 132)) + 125) == 10):
                    break
                v9 = (10 if (v7 == 1) else v20)
                v3 = (G.global0 - 16)
                G.global0 = (G.global0 - 16)
                while True:  # $label25
                    v14 = (v5 + (arg1 * 132))
                    if (load8u((v5 + (arg1 * 132)) + 125) == 3):
                        break
                    arg1 = load32(v14 + 64)
                    if (u32(v9) >= u32(load32(v14 + 64))):
                        store32(v14 + 64, 0)
                        break
                    store32(v14 + 64, (arg1 - v9))
                    if not load32(v14 + 92):
                        break
                    if load8u(9147141):
                        break
                    store32(v3, v9)
                    a_b()
                    break
                G.global0 = (v3 + 16)
                break
            while True:  # $label26
                if not load32(v4 + 92):
                    break
                if load32(9140316):
                    if (load32(9140320) != load32((v5 + (arg0 * 132)) + 28)):
                        break
                break
            arg1 = (0 if v8 else v7)
            while True:  # $label27
                v9 = load8u(v2 + 122)
                if (load8u(v2 + 122) != load32(38508)):
                    if (load32(38504) != v9):
                        break
                v17 = (v5 + (arg0 * 132))
                v10 = load16u((v5 + (arg0 * 132)) + 112)
                v3 = load16u(v17 + 110)
                v13 = (v10 + 1)
                v12 = load32(9142440)
                v6 = (load32(9142440) + 2)
                v15 = load32(ENTITIES)
                v18 = load32(9142840)
                while True:  # $label30
                    while True:  # $label28
                        v16 = load16u(v17 + 114)
                        v4 = (u32(v12) <= u32(load16u(v17 + 114)))
                        if (u32(v12) <= u32(load16u(v17 + 114))):
                            break
                        if (u32(v12) <= u32(v13)):
                            break
                        if ((v13 | v16) < 0):
                            break
                        v2 = load32((((v10 + (((v6 + v16) + 1) * v6)) << 2) + v18) + 8)
                        if (u32(load32((((v10 + (((v6 + v16) + 1) * v6)) << 2) + v18) + 8)) < u32(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # $label29
                            # br_table (load8u(v2 + 125) - 4)
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    while True:  # $label31
                        v14 = (v16 - 1)
                        v8 = (u32(v12) <= u32((v16 - 1)))
                        if (u32(v12) <= u32((v16 - 1))):
                            break
                        if (u32(v12) <= u32(v13)):
                            break
                        if ((v13 | v14) < 0):
                            break
                        v2 = load32((((v10 + ((v6 + v16) * v6)) << 2) + v18) + 8)
                        if (u32(load32((((v10 + ((v6 + v16) * v6)) << 2) + v18) + 8)) < u32(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # $label32
                            # br_table (load8u(v2 + 125) - 4)
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    while True:  # $label33
                        if v8:
                            break
                        if (u32(v10) >= u32(v12)):
                            break
                        if ((v10 | v14) < 0):
                            break
                        v2 = load32((v18 + ((v13 + ((v6 + v16) * v6)) << 2)))
                        if (u32(load32((v18 + ((v13 + ((v6 + v16) * v6)) << 2)))) < u32(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # $label34
                            # br_table (load8u(v2 + 125) - 4)
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    v21 = (v10 - 1)
                    while True:  # $label35
                        if v8:
                            break
                        if (u32(v12) <= u32(v21)):
                            break
                        if ((v14 | v21) < 0):
                            break
                        v2 = load32((v18 + ((((v6 + v16) * v6) + v10) << 2)))
                        if (u32(load32((v18 + ((((v6 + v16) * v6) + v10) << 2)))) < u32(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # $label36
                            # br_table (load8u(v2 + 125) - 4)
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    v8 = (v16 + 1)
                    while True:  # $label37
                        if v4:
                            break
                        if (u32(v12) <= u32(v21)):
                            break
                        if ((v16 | v21) < 0):
                            break
                        v2 = load32((v18 + ((((v6 + v8) * v6) + v10) << 2)))
                        if (u32(load32((v18 + ((((v6 + v8) * v6) + v10) << 2)))) < u32(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # $label38
                            # br_table (load8u(v2 + 125) - 4)
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    while True:  # $label39
                        v4 = (u32(v8) >= u32(v12))
                        if (u32(v8) >= u32(v12)):
                            break
                        if (u32(v12) <= u32(v21)):
                            break
                        if ((v8 | v21) < 0):
                            break
                        v2 = load32((v18 + (((((v6 + v16) + 2) * v6) + v10) << 2)))
                        if (u32(load32((v18 + (((((v6 + v16) + 2) * v6) + v10) << 2)))) < u32(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # $label40
                            # br_table (load8u(v2 + 125) - 4)
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    while True:  # $label41
                        if v4:
                            break
                        if (u32(v10) >= u32(v12)):
                            break
                        if ((v8 | v10) < 0):
                            break
                        v2 = load32((v18 + ((v13 + (((v6 + v16) + 2) * v6)) << 2)))
                        if (u32(load32((v18 + ((v13 + (((v6 + v16) + 2) * v6)) << 2)))) < u32(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # $label42
                            # br_table (load8u(v2 + 125) - 4)
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    while True:  # $label43
                        if v4:
                            break
                        if (u32(v12) <= u32(v13)):
                            break
                        if ((v8 | v13) < 0):
                            break
                        v2 = load32((((v10 + (((v6 + v16) + 2) * v6)) << 2) + v18) + 8)
                        if (u32(load32((((v10 + (((v6 + v16) + 2) * v6)) << 2) + v18) + 8)) < u32(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # $label44
                            # br_table (load8u(v2 + 125) - 4)
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    v7 = 0
                    break
                if v7:
                    store32(v11 + 88, 0)
                    store32((load32(9215884) + (load32(v17 + 44) << 4)), (load32(9142848) + 40))
                    break
                if not load32(players[v3] + 286684):
                    break
                if func87(v11, v9):
                    break
                break
            arg0 = (v5 + (arg0 * 132))
            arg0 = func166(load16u((v5 + (arg0 * 132)) + 112), load16u(arg0 + 114), load16u(arg0 + 110), arg1)
            if func166(load16u((v5 + (arg0 * 132)) + 112), load16u(arg0 + 114), load16u(arg0 + 110), arg1):
                break
            func29(v11, 1)
            break
        store32(v11 + 88, v2)
        store32((load32(9215884) + (load32((v5 + (arg0 * 132)) + 44) << 4)), (load32(9142848) + 40))
        break
    G.global0 = (v19 + 48)
    return func28(1, 1)

# ----------------------------------------------------------
# $func825
# ----------------------------------------------------------
def func825(arg0):
    v1 = 3
    while True:  # $label3
        while True:  # $label0
            while True:  # $label1
                v7 = load32(ENTITIES)
                v5 = load32(arg0 + 32)
                v2 = entities[load32(arg0 + 32)]
                v6 = load8u(entities[load32(arg0 + 32)].unit_class)
                if (load8u(entities[load32(arg0 + 32)].unit_class) != 10):
                    v3 = 1
                    v4 = load8u(v2 + 122)
                    v1 = load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 188)
                    if (u32(load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 188)) > u32(3)):
                        break
                    if v6:
                        break
                v4 = load8u(v2 + 122)
                while True:  # $label2
                    if (load8u(arg0 + 125) != 7):
                        break
                    if (load32(38504) == v4):
                        break
                    if (load32(38508) != v4):
                        break
                    break
                v3 = 0
                if (load32(38500) != v4):
                    break
                v2 = (v7 + (v5 * 132))
                v6 = (load32(9142440) + 2)
                v2 = load32((load32(9142840) + ((load16u((v7 + (v5 * 132)) + 112) + ((((load32(9142440) + 2) + load16u(v2 + 114)) + 2) * v6)) << 2)) + 8)
                if not load32((load32(9142840) + ((load16u((v7 + (v5 * 132)) + 112) + ((((load32(9142440) + 2) + load16u(v2 + 114)) + 2) * v6)) << 2)) + 8):
                    break
                if (v2 == load32(arg0 + 28)):
                    break
                break
            v3 = 0
            if (v4 != load32(38528)):
                if (load32(38504) == v4):
                    break
                if (load32(38508) == v4):
                    break
                v1 = func335(load16u(arg0 + 112), load16u(arg0 + 114), load32(((v1 << 2) + 9680)), v5)
                if not func335(load16u(arg0 + 112), load16u(arg0 + 114), load32(((v1 << 2) + 9680)), v5):
                    break
                break
            v5 = load32(9142440)
            v6 = (load32(9142440) + 3)
            v8 = (v5 + 2)
            v9 = load32(9142840)
            v10 = load16u(arg0 + 114)
            v11 = load16u(arg0 + 112)
            v12 = load16u(arg0 + 110)
            v1 = 0
            while True:  # $label7
                while True:  # $label6
                    while True:  # $label5
                        while True:  # $label4
                            v3 = v1
                            v2 = (v1 << 2)
                            v1 = (load32((((v1 << 2) | 4) + 8611904)) + v10)
                            if (u32(v5) <= u32((load32((((v1 << 2) | 4) + 8611904)) + v10))):
                                break
                            v2 = (load32((v2 + 8611904)) + v11)
                            if (u32(v5) <= u32((load32((v2 + 8611904)) + v11))):
                                break
                            if ((v1 | v2) < 0):
                                break
                            v2 = load32((((v2 + ((v1 + v6) * v8)) << 2) + v9) + 4)
                            v1 = (v7 + (load32((((v2 + ((v1 + v6) * v8)) << 2) + v9) + 4) * 132))
                            if (v4 != load8u((v7 + (load32((((v2 + ((v1 + v6) * v8)) << 2) + v9) + 4) * 132)) + 122)):
                                break
                            if (u32(load32(v1 + 72)) < u32(50)):
                                break
                            if (load8u(v1 + 125) == 12):
                                break
                            if (load16u(v1 + 110) != v12):
                                break
                            if not load32(v1 + 96):
                                break
                            break
                        v1 = (v3 + 2)
                        if (u32(v3) <= u32(16557)):
                            continue
                        break
                        break
                    break
                v1 = load32((v7 + (v2 * 132)) + 28)
                if load32((v7 + (v2 * 132)) + 28):
                    break
                break
            store8(arg0 + 129, 10)
            store32(arg0 + 32, 0)
            v3 = 1
            break
        return v3
        break
    store32(arg0 + 32, v1)
    return 0

# ----------------------------------------------------------
# $func826
# ----------------------------------------------------------
def func826(arg0, arg1, arg2, arg3, arg4):
    while True:  # $label0
        arg3 = load32(ENTITIES)
        arg2 = entities[load32(arg1)]
        if (load8u(entities[load32(arg1)].unit_class) != 10):
            if (u32(load32(((load8u(arg2 + 122) * 404) + ENTITY_TYPES) + 188)) > u32(3)):
                break
        arg2 = (arg3 + (arg0 * 132))
        arg4 = load32((arg3 + (arg0 * 132)) + 88)
        if not load32((arg3 + (arg0 * 132)) + 88):
            return 0
        if not load16u(arg2 + 108):
            break
        arg1 = ((arg4 & 0xFFFFFFFF) >> 16)
        arg4 = (arg4 & 65535)
        if (((arg4 & 0xFFFFFFFF) >> 16) != ((arg4 & 65535) if (arg4 != 3) else 0)):
            break
        arg0 = (arg3 + (arg0 * 132))
        arg0 = func166(load16u((arg3 + (arg0 * 132)) + 112), load16u(arg0 + 114), load16u(arg0 + 110), arg1)
        if func166(load16u((arg3 + (arg0 * 132)) + 112), load16u(arg0 + 114), load16u(arg0 + 110), arg1):
            return 1
        func29(arg2, 1)
        break
    return 1

# ----------------------------------------------------------
# $func827
# ----------------------------------------------------------
def func827(arg0):
    while True:  # $label0
        v1 = load32(ENTITIES)
        arg0 = (v1 + (arg0 * 132))
        v1 = load32((v1 + (arg0 * 132)) + 32)
        v3 = load8u(entities[load32((v1 + (arg0].sub_state)
        if (load8u(entities[load32((v1 + (arg0].sub_state) != load32(38448)):
            break
        v1 = func335(load16u(arg0 + 112), load16u(arg0 + 114), v3, v1)
        if not func335(load16u(arg0 + 112), load16u(arg0 + 114), v3, v1):
            break
        store32(arg0 + 32, v1)
        func140(arg0)
        v2 = 1
        break
    return v2

# ----------------------------------------------------------
# $func830
# ----------------------------------------------------------
def func830(arg0, arg1, arg2):
    func397(load32(arg0), arg1, arg2)

# ----------------------------------------------------------
# $func831
# ----------------------------------------------------------
def func831(arg0, arg1, arg2):
    if load8u(9142388):
        v5 = load32(PLAYERS)
        v3 = load32(arg0)
        while True:  # $label0
            v7 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            v6 = load32(59164)
            arg0 = 1
            while True:  # $label1
                v8 = (v5 + (arg0 * 286704))
                if (v6 == load32((v5 + (arg0 * 286704)) + 284616)):
                    v4 = arg0
                    break
                if (v6 == load32(v8 + 284628)):
                    v4 = arg0
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v7):
                    continue
                break
            break
        store32((v5 + (v4 * 286704)) + 284632, v3)
        while True:  # $label2
            if (u32(load32(9561744)) >= u32(v3)):
                break
            store32(9561744, v3)
            if not arg2:
                break
            arg0 = load32(9561736)
            if load32(9561736):
                store32(9561736, 0)
            v4 = (arg2 << 2)
            arg0 = func26((-1 if (u32(arg2) > u32(1073741823)) else (arg2 << 2)))
            store32(9561740, arg2)
            store32(9561736, arg0)
            # TODO: memory.copy
            break
        if (u32(v3) < u32(load32(9561748))):
            store32(9561748, v3)

# ----------------------------------------------------------
# $func832
# ----------------------------------------------------------
def func832(arg0, arg1, arg2):
    arg2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label2
        v6 = load32(arg0)
        if (u32(load32(arg0)) < u32(load32(59176))):
            while True:  # $label0
                v4 = load32(9561704)
                if load32(9561704):
                    arg0 = 0
                    v5 = load32(9561696)
                    while True:  # $label1
                        v3 = ((arg0 << 2) + v5)
                        if (u32(v6) <= u32(load32(((arg0 << 2) + v5) + 4))):
                            v3 = (v4 - arg0)
                            break
                        arg0 = (load32(v3 + 8) + arg0)
                        if (u32(v4) > u32((load32(v3 + 8) + arg0))):
                            continue
                        break
                    v3 = 0
                break
            func71((v5 + (arg0 << 2)), 0, v3, 59176, 1, 1)
            break
        func71(35, 0, 0, 59176, 1, 1)
        break
    v4 = load32(PLAYER_COUNT)
    if (u32(load32(PLAYER_COUNT)) >= u32(2)):
        v5 = load32(PLAYERS)
        arg0 = 1
        while True:  # $label4
            while True:  # $label3
                if not load32((arg1 + (arg0 << 2))):
                    break
                v3 = (v5 + (arg0 * 286704))
                if load32((v5 + (arg0 * 286704)) + 284616):
                    break
                store32((v3 + 284616), load32(v3 + 284628))
                store8(v3 + 286699, 0)
                v4 = load32(v3 + 283908)
                v3 = load8u(v3 + 286696)
                store32(arg2 + 8, 0)
                store32(arg2 + 4, v3)
                store32(arg2, v4)
                a_b()
                v4 = load32(PLAYER_COUNT)
                v5 = load32(PLAYERS)
                break
            arg0 = (arg0 + 1)
            if (u32((arg0 + 1)) < u32(v4)):
                continue
            break
    G.global0 = (arg2 + 16)
    return arg2

# ----------------------------------------------------------
# $func834
# ----------------------------------------------------------
def func834(arg0, arg1):
    store8(9163793, arg0)
    while True:  # $label0
        if not arg0:
            break
        if not load32(9671176):
            break
        arg1 = load32(38620)
        v2 = load32(38560)
        arg0 = load32(load32(9671168))
        v2 = (load32(38620) if (arg0 == v2) else (load32(38560) if (arg0 == arg1) else load32(load32(9671168))))
        arg1 = ((load32(38620) if (arg0 == v2) else (load32(38560) if (arg0 == arg1) else load32(load32(9671168)))) + 1)
        arg1 = load32(38604)
        arg1 = (((load32(38620) if (arg0 == v2) else (load32(38560) if (arg0 == arg1) else load32(load32(9671168)))) + 1) if (arg0 == arg1) else (arg1 if (arg0 == load32(38608)) else (arg1 if (arg0 == load32(38612)) else (load32(38604) if (arg0 == load32(38616)) else v2))))
        while True:  # $label2
            while True:  # $label1
                v2 = load32(38624)
                if (load32(38624) != arg0):
                    if (arg0 != load32(38628)):
                        break
                break
                break
            v3 = load32(39056)
            if (arg0 == load32(38632)):
                break
            break
        v3 = (v2 if (arg0 == v3) else arg1)
        if ((arg1 + 1) == (v2 if (arg0 == v3) else arg1)):
            break
        if load32(9671192):
            arg0 = 0
            while True:  # $label3
                func38(load32((load32(9671184) + (arg0 << 2))))
                arg0 = (arg0 + 1)
                if (u32((arg0 + 1)) < u32(load32(9671192))):
                    continue
                break
        arg0 = 0
        store32(9671192, 0)
        store32(9671176, 0)
        store8(9142412, 0)
        if load8u(9684396):
            store8(9684396, 0)
            a_b()
            arg0 = load32(9671176)
        while True:  # $label4
            arg1 = load32(9671172)
            if (u32(load32(9671172)) > u32((arg0 + 3))):
                arg1 = load32(9671168)
                break
            arg1 = ((arg1 + load32(9671180)) + 3)
            store32(9671172, ((arg1 + load32(9671180)) + 3))
            v2 = load32(9671168)
            arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
            if arg0:
                # TODO: memory.copy
            if v2:
                arg0 = load32(9671176)
            store32(9671168, arg1)
            break
        store32(9671176, (arg0 + 1))
        store32((arg1 + (arg0 << 2)), v3)
        arg0 = load32(9671176)
        store32(9671176, (load32(9671176) + 1))
        store32((arg1 + (arg0 << 2)), 0)
        arg0 = load32(9671176)
        store32(9671176, (load32(9671176) + 1))
        store32((arg1 + (arg0 << 2)), 0)
        if not load8u(9147152):
            break
        store8(9142412, 1)
        break
    return func132(2147483647, 2147483647)

# ----------------------------------------------------------
# $func837
# ----------------------------------------------------------
def func837(arg0, arg1):
    func146(arg0, load32(38940))

# ----------------------------------------------------------
# $func838
# ----------------------------------------------------------
def func838(arg0, arg1):
    func146(arg0, load32(38932))

# ----------------------------------------------------------
# $func839
# ----------------------------------------------------------
def func839(arg0, arg1):
    func146(arg0, load32(38936))

# ----------------------------------------------------------
# $func840
# ----------------------------------------------------------
def func840(arg0, arg1):
    v2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store32(v2 + 28, (arg0 & 65535))
    store32(v2 + 24, ((arg0 & 0xFFFFFFFF) >> 16))
    v3 = (arg1 & 65535)
    arg0 = (((arg1 & 65535) * 404) + ENTITY_TYPES)
    arg0 = load32(v2 + 28)
    arg1 = load32(v2 + 24)
    while True:  # $label2
        while True:  # $label1
            while True:  # $label0
                v5 = load32(load32(GAME_STATE) + 48)
                if load32(load32(GAME_STATE) + 48):
                    if not load8u(9147152):
                        break
                v3 = load32(9142440)
                break
                break
            v3 = load32(9142440)
            v4 = load16u((load32(9147376) + (((load32(9142440) * arg1) + arg0) << 1)))
            if (v5 == 2):
                if (u32(v4) > u32(1)):
                    break
                break
            if not v4:
                break
            break
        func80(i32(arg0), i32(arg1), load32(9142536), 32.0, i32((v3 * 96)))
        break
    while True:  # $label3
        v3 = ((arg0 << 5) - load32(9142952))
        v3 = ((arg1 << 5) - load32(9142956))
        if ((((((arg0 << 5) - load32(9142952)) * v3) + (((arg1 << 5) - load32(9142956)) * v3)) - 1) > 9000000):
            break
        while True:  # $label4
            v4 = load32(load32(GAME_STATE) + 48)
            if not load32(load32(GAME_STATE) + 48):
                break
            if load8u(9147152):
                break
            v3 = load16u((load32(9147376) + (((load32(9142440) * arg1) + arg0) << 1)))
            if (v4 == 2):
                if (u32(v3) > u32(1)):
                    break
                break
            if not v3:
                break
            break
        store32(v2 + 8, arg1)
        store32(v2 + 4, arg0)
        store32(v2, load32(((((load32(9142848) + arg0) % 10) << 2) + 57744)))
        a_b()
        break
    G.global0 = (v2 + 32)

# ----------------------------------------------------------
# $func841
# ----------------------------------------------------------
def func841(arg0, arg1, arg2):
    arg2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # $label0
        v7 = load32(ENTITIES)
        v4 = load32(arg1)
        v5 = entities[load32(arg1)]
        if (load8u(entities[load32(arg1)].unit_class) == 3):
            break
        arg1 = load32(v5 + 20)
        if not load32(v5 + 20):
            break
        arg1 = load32(arg0)
        arg0 = load32((load32(arg1) + (load32(arg0) << 2)))
        if not load32((load32(arg1) + (load32(arg0) << 2))):
            break
        v6 = (arg0 - 1)
        v3 = (((arg0 - 1) * 404) + ENTITY_TYPES)
        v8 = load32(PLAYERS)
        v7 = load16u((v7 + (v4 * 132)) + 110)
        arg0 = (load32(PLAYERS) + (load16u((v7 + (v4 * 132)) + 110) * 286704))
        v9 = load32((((load32(PLAYERS) + (load16u((v7 + (v4 * 132)) + 110) * 286704)) + (load32(39136) << 2)) + 281808))
        store32(arg2, (((load32((((arg0 - 1) * 404) + ENTITY_TYPES) + 68) * 144) // 10) + (120 if (load32((((load32(PLAYERS) + (load16u((v7 + (v4 * 132)) + 110) * 286704)) + (load32(39136) << 2)) + 281808)) == 1) else 0)))
        store32(arg2 + 4, ((load32(v3 + 72) * 144) // 10))
        store32(arg2 + 8, ((load32(v3 + 76) * 144) // 10))
        store32(arg2 + 12, ((load32(v3 + 80) * 144) // 10))
        while True:  # $label2
            while True:  # $label1
                v3 = (load32(arg0 + 283976) + 1)
                if (u32((load32(arg0 + 283976) + 1)) > u32((load32((arg0 + 284136)) + load32(arg0 + 283980)))):
                    arg1 = 57101
                    if (load32(arg0 + 283908) == load32(CURRENT_PLAYER)):
                        break
                    break
                if (u32(v3) <= u32(load32((arg0 + 284000)))):
                    break
                arg1 = 57113
                if (load32((v8 + (v7 * 286704)) + 283908) != load32(CURRENT_PLAYER)):
                    break
                break
            a_b()
            break
            break
        if func66(arg0, arg2, 1, 1):
            break
        arg0 = load32(load32(v5 + 20))
        while True:  # $label3
            if (u32(arg1) >= u32(7)):
                break
            v3 = (arg1 + 1)
            v5 = (arg0 + ((arg1 + 1) << 2))
            store32((arg0 + (arg1 << 2)), load32((arg0 + ((arg1 + 1) << 2))))
            if (v3 == 7):
                break
            v3 = (arg1 + 2)
            store32(v5, load32((arg0 + ((arg1 + 2) << 2))))
            if (v3 == 7):
                break
            v3 = (arg1 + 3)
            v5 = (arg0 + ((arg1 + 3) << 2))
            store32((arg0 + (v3 << 2)), load32((arg0 + ((arg1 + 3) << 2))))
            if (v3 == 7):
                break
            v3 = (arg1 + 4)
            store32(v5, load32((arg0 + ((arg1 + 4) << 2))))
            if (v3 == 7):
                break
            v3 = (arg1 + 5)
            v5 = (arg0 + ((arg1 + 5) << 2))
            store32((arg0 + (v3 << 2)), load32((arg0 + ((arg1 + 5) << 2))))
            if (v3 == 7):
                break
            v3 = (arg1 + 6)
            store32(v5, load32((arg0 + ((arg1 + 6) << 2))))
            if (v3 == 7):
                break
            store32((arg0 + (v3 << 2)), load32(((arg1 << 2) + arg0) + 28))
            break
        arg1 = 0
        store32(arg0 + 28, 0)
        arg0 = ((v8 + (v7 * 286704)) + 281744)
        store32(((v8 + (v7 * 286704)) + 281744), (load32(arg0) + 9))
        arg0 = ((v6 * 404) + ENTITY_TYPES)
        while True:  # $label6
            if (v9 == 1):
                v5 = (v4 * 132)
                while True:  # $label5
                    while True:  # $label4
                        v3 = (load32(ENTITIES) + v5)
                        if not func59((arg2 + 28), (arg2 + 24), (load32(ENTITIES) + v5), arg0):
                            break
                        v8 = func34(v6, load16u(v3 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                        if not func34(v6, load16u(v3 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1):
                            break
                        v7 = load32(ENTITIES)
                        v3 = entities[v8]
                        if load32(entities[v8].max_hp):
                            store32(v3 + 84, 4)
                            store32(v3 + 52, (load32(v3 + 52) + 4))
                            store32(v3 + 60, (load32(v3 + 60) + 2))
                        func69((v5 + v7), v8)
                        break
                    arg1 = (arg1 + 1)
                    if ((arg1 + 1) != 9):
                        continue
                    break
                break
            while True:  # $label7
                arg1 = entities[v4]
                if not func59((arg2 + 28), (arg2 + 24), entities[v4], arg0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if not func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1):
                    break
                func69(entities[v4], arg1)
                break
            while True:  # $label8
                arg1 = entities[v4]
                if not func59((arg2 + 28), (arg2 + 24), entities[v4], arg0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if not func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1):
                    break
                func69(entities[v4], arg1)
                break
            while True:  # $label9
                arg1 = entities[v4]
                if not func59((arg2 + 28), (arg2 + 24), entities[v4], arg0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if not func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1):
                    break
                func69(entities[v4], arg1)
                break
            while True:  # $label10
                arg1 = entities[v4]
                if not func59((arg2 + 28), (arg2 + 24), entities[v4], arg0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if not func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1):
                    break
                func69(entities[v4], arg1)
                break
            while True:  # $label11
                arg1 = entities[v4]
                if not func59((arg2 + 28), (arg2 + 24), entities[v4], arg0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if not func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1):
                    break
                func69(entities[v4], arg1)
                break
            while True:  # $label12
                arg1 = entities[v4]
                if not func59((arg2 + 28), (arg2 + 24), entities[v4], arg0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if not func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1):
                    break
                func69(entities[v4], arg1)
                break
            while True:  # $label13
                arg1 = entities[v4]
                if not func59((arg2 + 28), (arg2 + 24), entities[v4], arg0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if not func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1):
                    break
                func69(entities[v4], arg1)
                break
            while True:  # $label14
                arg1 = entities[v4]
                if not func59((arg2 + 28), (arg2 + 24), entities[v4], arg0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if not func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1):
                    break
                func69(entities[v4], arg1)
                break
            arg1 = entities[v4]
            if not func59((arg2 + 28), (arg2 + 24), entities[v4], arg0):
                break
            arg0 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
            if not func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1):
                break
            func69(entities[v4], arg0)
            break
        if (load32(9671124) != 95):
            break
        if (load32(9173808) != v4):
            break
        break
    G.global0 = (arg2 + 32)

# ----------------------------------------------------------
# $func842
# ----------------------------------------------------------
def func842(arg0, arg1):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if load8u(9147152):
            break
        v5 = load32(ENTITIES)
        v2 = entities[arg0]
        v10 = load16u(entities[arg0] + 110)
        v8 = load32((players[load16u(entities[arg0] + 110)] + 284324))
        if not load32((players[load16u(entities[arg0] + 110)] + 284324)):
            break
        v4 = load32(v2 + 80)
        # TODO: i32.div_u
        v11 = v8
        if (u32(v4) >= u32(v8)):
            while True:  # $label1
                v2 = (arg0 * 132)
                if not func225((arg1 + 12), (arg1 + 8), (v5 + (arg0 * 132)), ((load32(38984) * 404) + ENTITY_TYPES)):
                    break
                v2 = func34(load32(38984), load16u((load32(ENTITIES) + v2) + 110), load32(arg1 + 12), load32(arg1 + 8), 0, 1)
                if not func34(load32(38984), load16u((load32(ENTITIES) + v2) + 110), load32(arg1 + 12), load32(arg1 + 8), 0, 1):
                    break
                v5 = load32(ENTITIES)
                v2 = entities[v2]
                store64(entities[v2].range, 1073741824250)
                store32(v2 + 56, v10)
                store32(v2 + 52, v8)
                v16 = load16u((v5 + (arg0 * 132)) + 110)
                v9 = load32(9142440)
                v14 = load16u(v2 + 114)
                v15 = load16u(v2 + 112)
                while True:  # $label8
                    while True:  # $label7
                        while True:  # $label2
                            v5 = v3
                            v3 = (v3 << 2)
                            v7 = (load32((((v3 << 2) | 4) + 8611904)) + v14)
                            if (u32(v9) <= u32((load32((((v3 << 2) | 4) + 8611904)) + v14))):
                                break
                            v4 = (load32((v3 + 8611904)) + v15)
                            if (u32(v9) <= u32((load32((v3 + 8611904)) + v15))):
                                break
                            if ((v4 | v7) < 0):
                                break
                            while True:  # $label3
                                while True:  # $label4
                                    v12 = load32(ENTITIES)
                                    v3 = (v9 + 2)
                                    v6 = entities[load32((load32(9142840) + ((v4 + (((v7 + (v9 + 2)) + 1) * v3)) << 2)) + 4)]
                                    v3 = load8u(entities[load32((load32(9142840) + ((v4 + (((v7 + (v9 + 2)) + 1) * v3)) << 2)) + 4)].sub_state)
                                    # br_table (load8u(entities[load32((load32(9142840) + ((v4 + (((v7 + (v9 + 2)) + 1) * v3)) << 2)) + 4)].sub_state) + -64)
                                    break
                                    break
                                if (v3 != 10):
                                    break
                                break
                            if (load8u(v6 + 129) != 10):
                                break
                            if (load16u(v6 + 110) != v16):
                                break
                            v4 = load8u(v6 + 125)
                            while True:  # $label6
                                while True:  # $label5
                                    v3 = load32(v6 + 44)
                                    if not ((load32((load32(9215884) + (load32(v6 + 44) << 4)) + 4) == 22) | not v3):
                                        break
                                    if v4:
                                        break
                                    if not load32(v6 + 36):
                                        break
                                    break
                                    break
                                if (v4 != 1):
                                    break
                                v4 = load32(v6 + 32)
                                v7 = (v12 + (load32(v6 + 32) * 132))
                                v3 = load8u((v12 + (load32(v6 + 32) * 132)) + 122)
                                if (load8u((v12 + (load32(v6 + 32) * 132)) + 122) == load32(38528)):
                                    break
                                if (load8u(v7 + 125) == 3):
                                    break
                                if not v4:
                                    break
                                if (load32(38984) != v3):
                                    break
                                v12 = load16u(v6 + 114)
                                v3 = (load16u(v7 + 114) - load16u(v6 + 114))
                                v4 = load16u(v6 + 112)
                                v3 = (load16u(v7 + 112) - load16u(v6 + 112))
                                v3 = (v14 - v12)
                                v3 = (v15 - v4)
                                if (u32((((load16u(v7 + 114) - load16u(v6 + 114)) * v3) + ((load16u(v7 + 112) - load16u(v6 + 112)) * v3))) <= u32((((v14 - v12) * v3) + ((v15 - v4) * v3)))):
                                    break
                                break
                            if v13:
                                break
                            v9 = load32(9142440)
                            v13 = 1
                            break
                        v3 = (v5 + 2)
                        if (u32(v5) < u32(16558)):
                            continue
                        break
                    break
                break
            v4 = 1
            v2 = (u32(v11) > u32(1))
            if (u32(v11) > u32(1)):
                v5 = (v11 if v2 else 1)
                v3 = (arg0 * 132)
                while True:  # $label10
                    while True:  # $label9
                        if not func225((arg1 + 12), (arg1 + 8), (load32(ENTITIES) + v3), ((load32(38984) * 404) + ENTITY_TYPES)):
                            break
                        v2 = func34(load32(38984), load16u((load32(ENTITIES) + v3) + 110), load32(arg1 + 12), load32(arg1 + 8), 0, 1)
                        if not func34(load32(38984), load16u((load32(ENTITIES) + v3) + 110), load32(arg1 + 12), load32(arg1 + 8), 0, 1):
                            break
                        v2 = entities[v2]
                        store64(entities[v2].range, 1073741824250)
                        store32(v2 + 56, v10)
                        store32(v2 + 52, v8)
                        break
                    v4 = (v4 + 1)
                    if ((v4 + 1) != v5):
                        continue
                    break
            v5 = load32(ENTITIES)
            v4 = load32(entities[arg0].animation)
        v3 = (v8 * v11)
        if (u32(v4) <= u32((v8 * v11))):
            break
        v2 = (arg0 * 132)
        if not func225((arg1 + 12), (arg1 + 8), (v5 + (arg0 * 132)), ((load32(38984) * 404) + ENTITY_TYPES)):
            break
        v5 = func34(load32(38984), load16u((load32(ENTITIES) + v2) + 110), load32(arg1 + 12), load32(arg1 + 8), 0, 1)
        if not func34(load32(38984), load16u((load32(ENTITIES) + v2) + 110), load32(arg1 + 12), load32(arg1 + 8), 0, 1):
            break
        v2 = load32(ENTITIES)
        arg0 = load32(entities[arg0].animation)
        v2 = (v2 + (v5 * 132))
        store64((v2 + (v5 * 132)) + 64, 1073741824250)
        store32(v2 + 56, v10)
        store32(v2 + 52, (arg0 - v3))
        break
    G.global0 = (arg1 + 16)

# ----------------------------------------------------------
# $kb
# Export: kb
# ----------------------------------------------------------
def kb():
    """Export: kb"""
    v0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v1 = load32(9173808)
    store32(v0 + 12, load32(9173808))
    store32(v0 + 4, load32((load32(9681476) + (load32(9681468) << 2))))
    store32(v0 + 8, load32(9681472))
    while True:  # $label0
        if load8u(9147210):
            func41(12, (v0 + 12), 1, (v0 + 4), 2)
            break
        v2 = func26(4)
        store32(func26(4), v1)
        break
    G.global0 = (v0 + 16)

# ----------------------------------------------------------
# $func844
# ----------------------------------------------------------
def func844(arg0, arg1, arg2):
    arg2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        v5 = load32(ENTITIES)
        v6 = load32(arg1)
        arg1 = entities[load32(arg1)]
        v3 = load8u(entities[load32(arg1)].unit_class)
        if (load8u(entities[load32(arg1)].unit_class) == 3):
            break
        v4 = load32(PLAYERS)
        v8 = load16u(arg1 + 110)
        if load32(players[load16u(arg1 + 110)] + 283912):
            break
        v7 = load32(arg0)
        arg0 = load32(arg0 + 4)
        store32(arg2 + 12, 0)
        store64(arg2 + 4, 0)
        store32(arg2, arg0)
        if v3:
            break
        if func66((v4 + (v8 * 286704)), arg2, 1, 1):
            break
        v3 = load32(((v7 * 404) + ENTITY_TYPES) + 268)
        v4 = players[load16u(arg1 + 110)]
        store32(players[load16u(arg1 + 110)] + 283912, (load32(v4 + 283912) + 1))
        # TODO: i32.div_u
        func63(arg1, 34, ((arg0 << 16) + v7), (load32(load32(GAME_STATE) + 132) * ((500 if (v3 == 1) else 250) * arg0)), 100)
        if not load32((v5 + (v6 * 132)) + 92):
            break
        arg0 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32((v5 + (v6 * 132)) + 28)):
                break
        break
    G.global0 = (arg2 + 16)

# ----------------------------------------------------------
# $func845
# ----------------------------------------------------------
def func845(arg0, arg1):
    v5 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v3 = entities[arg0]
    v2 = players[load16u(entities[arg0] + 110)]
    store32(players[load16u(entities[arg0] + 110)] + 283912, (load32(v2 + 283912) - 1))
    while True:  # $label0
        v2 = (arg1 & 65535)
        if not func59((v5 + 12), (v5 + 8), v3, (((arg1 & 65535) * 404) + ENTITY_TYPES)):
            break
        v4 = func34(v2, load16u(v3 + 110), load32(v5 + 12), load32(v5 + 8), 0, 1)
        if not func34(v2, load16u(v3 + 110), load32(v5 + 12), load32(v5 + 8), 0, 1):
            break
        v6 = ((arg1 & 0xFFFFFFFF) >> 16)
        v8 = load32(ENTITIES)
        v2 = entities[v4]
        store16(entities[v4] + 110, 0)
        store32(v2 + 56, load16u(v3 + 110))
        while True:  # $label4
            while True:  # $label3
                while True:  # $label2
                    while True:  # $label1
                        v3 = load8u(v2 + 122)
                        v7 = ((load8u(v2 + 122) * 404) + ENTITY_TYPES)
                        # br_table load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 268)
                        break
                        break
                    if load32(v2 + 52):
                        store32(v2 + 52, ((arg1 & 0xFFFFFFFF) >> 17))
                    v2 = (v8 + (v4 * 132))
                    if load32((v8 + (v4 * 132)) + 60):
                        store32(v2 + 60, ((arg1 & 0xFFFFFFFF) >> 17))
                    if load32(v2 + 72):
                        store32(v2 + 72, v6)
                    v7 = (v8 + (v4 * 132))
                    if load32((v8 + (v4 * 132)) + 76):
                        store32(v7 + 76, v6)
                    v4 = 480
                    if not load32(v7 + 84):
                        break
                    v2 = 1
                    while True:  # $label5
                        if (u32(arg1) < u32(327680)):
                            break
                        # TODO: i32.div_u
                        v6 = 327680
                        v10 = (327680 & 1)
                        v3 = 1
                        if (u32((arg1 - 327680)) >= u32(327680)):
                            v6 = (v6 & 16382)
                            arg1 = 0
                            v3 = 0
                            while True:  # $label6
                                arg1 = ((arg1 + 1) % v2)
                                v9 = ((arg1 + 2) if ((arg1 + 1) % v2) else 1)
                                v2 = (v2 + not arg1)
                                v9 = (v9 % (v2 + not arg1))
                                arg1 = (((arg1 + 2) if ((arg1 + 1) % v2) else 1) if (v9 % (v2 + not arg1)) else 0)
                                v2 = (v2 + not v9)
                                v3 = (v3 + 2)
                                if ((v3 + 2) != v6):
                                    continue
                                break
                            v3 = (arg1 + 1)
                        if not v10:
                            break
                        v2 = (v2 + not (v3 % v2))
                        break
                    store32(v7 + 84, v2)
                    break
                    break
                # TODO: i32.div_u
                store32(v6 + 52, load32(v7 + 68))
                v4 = 624
                break
                break
            if load32(v2 + 52):
                store32(v2 + 52, ((arg1 & 0xFFFFFFFF) >> 18))
            v2 = (v8 + (v4 * 132))
            if load32((v8 + (v4 * 132)) + 60):
                store32(v2 + 60, ((arg1 & 0xFFFFFFFF) >> 18))
            v4 = 528
            if (load32(38952) == v3):
                break
            v4 = 576
            if (load32(38956) == v3):
                break
            v4 = (672 if (load32(38960) == v3) else 0)
            break
        if (load32(CURRENT_PLAYER) != load16u((v8 + (arg0 * 132)) + 110)):
            break
        store32(v5, v4)
        a_b()
        break
    arg1 = (arg0 * 132)
    func29(((arg0 * 132) + load32(ENTITIES)), 0)
    while True:  # $label7
        arg1 = load32(ENTITIES)
        if not load32((arg1 + load32(ENTITIES)) + 92):
            break
        v2 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32((arg1 + (arg0 * 132)) + 28)):
                break
        break
    G.global0 = (v5 + 16)

# ----------------------------------------------------------
# $func846
# ----------------------------------------------------------
def func846(arg0, arg1, arg2):
    arg2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # $label0
        v4 = load32(ENTITIES)
        v6 = load32(arg1)
        v7 = entities[load32(arg1)]
        if (load8u(entities[load32(arg1)].unit_class) == 3):
            break
        arg1 = load32(v7 + 20)
        if not load32(v7 + 20):
            break
        v3 = load32(arg0)
        arg1 = (load32(arg0) + 8)
        arg0 = load32((load32(arg1) + ((load32(arg0) + 8) << 2)))
        if not load32((load32(arg1) + ((load32(arg0) + 8) << 2))):
            break
        v9 = (arg0 - 1)
        arg0 = (((arg0 - 1) * 404) + ENTITY_TYPES)
        store32(arg2, (((load32((((arg0 - 1) * 404) + ENTITY_TYPES) + 68) * 36) // 10) + 620))
        store32(arg2 + 4, ((load32(arg0 + 72) * 36) // 10))
        store32(arg2 + 8, ((load32(arg0 + 76) * 36) // 10))
        store32(arg2 + 12, ((load32(arg0 + 80) * 36) // 10))
        while True:  # $label2
            while True:  # $label1
                v8 = load32(PLAYERS)
                v10 = (v4 + (v6 * 132))
                v4 = load16u((v4 + (v6 * 132)) + 110)
                arg0 = (load32(PLAYERS) + (load16u((v4 + (v6 * 132)) + 110) * 286704))
                v5 = (load32((load32(PLAYERS) + (load16u((v4 + (v6 * 132)) + 110) * 286704)) + 283976) + 1)
                if (u32((load32((load32(PLAYERS) + (load16u((v4 + (v6 * 132)) + 110) * 286704)) + 283976) + 1)) > u32((load32((arg0 + 284136)) + load32(arg0 + 283980)))):
                    arg1 = 57101
                    if (load32(arg0 + 283908) == load32(CURRENT_PLAYER)):
                        break
                    break
                if (u32(v5) <= u32(load32((arg0 + 284000)))):
                    break
                arg1 = 57113
                if (load32((v8 + (v4 * 286704)) + 283908) != load32(CURRENT_PLAYER)):
                    break
                break
            a_b()
            break
            break
        if func66((v8 + (v4 * 286704)), arg2, 1, 1):
            break
        arg0 = load32(load32(v7 + 20))
        while True:  # $label3
            if (u32(arg1) > u32(14)):
                break
            v11 = ((3 - v3) & 3)
            if ((3 - v3) & 3):
                v5 = 0
                while True:  # $label4
                    arg1 = (arg1 + 1)
                    store32((arg0 + (arg1 << 2)), load32((arg0 + ((arg1 + 1) << 2))))
                    v5 = (v5 + 1)
                    if ((v5 + 1) != v11):
                        continue
                    break
            if (u32((v3 - 4)) <= u32(2)):
                break
            while True:  # $label5
                v3 = (arg0 + (arg1 << 2))
                v12 = load64((arg0 + (arg1 << 2)) + 4)
                store32(v3 + 8, load32(v3 + 12))
                store64(v3, v12)
                arg1 = (arg1 + 4)
                store32(v3 + 12, load32((arg0 + ((arg1 + 4) << 2))))
                if (arg1 != 15):
                    continue
                break
            break
        store32(arg0 + 60, 0)
        arg1 = 0
        if func59((arg2 + 28), (arg2 + 24), v7, ((v9 * 404) + ENTITY_TYPES)):
            arg1 = func34(v9, load16u(v10 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
        arg0 = entities[arg1]
        if load32(entities[arg1].max_hp):
            arg1 = load32((players[load16u(v10 + 110)] + 284248))
            store32(arg0 + 84, load32((players[load16u(v10 + 110)] + 284248)))
            func201(arg0)
            v3 = (v8 + (v4 * 286704))
            store32((v8 + (v4 * 286704)) + 283936, (load32(v3 + 283936) + 1))
            v3 = (v3 + 281636)
            store32((v3 + 281636), (load32(v3) + 1))
            store32(arg0 + 52, (arg1 + load32(arg0 + 52)))
            store32(arg0 + 60, (load32(arg0 + 60) + ((arg1 & 0xFFFFFFFF) >> 1)))
            func69(entities[v6], load32(arg0 + 28))
        if (load32(9671124) != 96):
            break
        if (load32(9173808) != v6):
            break
        break
    G.global0 = (arg2 + 32)

# ----------------------------------------------------------
# $func847
# ----------------------------------------------------------
def func847(arg0, arg1):
    while True:  # $label0
        if not arg0:
            break
        v3 = ((arg1 << 2) + 9215712)
        arg0 = load32(((arg1 << 2) + 9215712))
        if load8u(9163793):
            if not arg0:
                arg0 = func26(16)
                store32(func26(16) + 4, 10000)
                store32(arg0, func26(40000))
                store64(arg0 + 8, 4294967296)
                store32(v3, arg0)
            arg1 = load32(9213808)
            store32(arg0 + 8, load32(9213808))
            if not arg1:
                break
            arg1 = load32(arg0)
            arg0 = 0
            while True:  # $label1
                v2 = (arg0 << 2)
                store32((arg1 + (arg0 << 2)), load32((v2 + 9173808)))
                arg0 = (arg0 + 1)
                if (u32((arg0 + 1)) < u32(load32(9213808))):
                    continue
                break
            break
        if not arg0:
            break
        store32(9143000, 0)
        arg0 = load32(9213820)
        if load32(9213820):
            func47(entities[arg0])
            store32(9213820, 0)
        func45()
        arg1 = load32(v3)
        if load32(load32(v3) + 8):
            v4 = load32(ENTITIES)
            arg0 = 0
            while True:  # $label3
                while True:  # $label2
                    v2 = (v4 + (load32((load32(arg1) + (arg0 << 2))) * 132))
                    if (load8u((v4 + (load32((load32(arg1) + (arg0 << 2))) * 132)) + 125) == 3):
                        break
                    if not load8u(9147152):
                        if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v2 + 110))))):
                            break
                        if (load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v2 + 127) == 6):
                            break
                    if load8u(9163792):
                        if load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 264):
                            break
                    func44(v2, 0)
                    arg1 = load32(v3)
                    v4 = load32(ENTITIES)
                    break
                arg0 = (arg0 + 1)
                if (u32((arg0 + 1)) < u32(load32(arg1 + 8))):
                    continue
                break
        break

# ----------------------------------------------------------
# $func848
# ----------------------------------------------------------
def func848(arg0, arg1):
    func146(arg0, load32(38724))

# ----------------------------------------------------------
# $func849
# ----------------------------------------------------------
def func849(arg0, arg1):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if load8u(9147152):
            break
        v17 = load32(PLAYERS)
        v2 = load32(ENTITIES)
        v4 = (arg0 * 132)
        arg0 = entities[arg0]
        v10 = load16u(entities[arg0] + 110)
        v11 = players[load16u(entities[arg0] + 110)]
        v18 = load8u(arg0 + 122)
        v19 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 68)
        arg0 = ((load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 68) & 0xFFFFFFFF) >> 1)
        while True:  # $label1
            if (load32(9671152) != v18):
                break
            arg0 = ((load32(v11 + 283848) // 2) + arg0)
            v7 = load32(9671136)
            # TODO: i32.div_u
            v8 = 200
            v3 = load32(9671132)
            if (u32((func88(v11) + 200)) < u32(load32(9671132))):
                break
            v8 = (load32(9671140) + (v3 + v8))
            store32(9671132, (load32(9671140) + (v3 + v8)))
            v2 = func228(v2, v8, v7)
            store32(ENTITIES, func228(v2, v8, v7))
            break
        v2 = (v2 + v4)
        v20 = load16u((v2 + v4) + 112)
        v8 = load16u(v2 + 114)
        # TODO: i32.div_u
        v9 = 100
        v2 = (100 * -100)
        v4 = load32(9671132)
        v7 = load32(9671136)
        if (u32(load32(9671132)) <= u32((load32(9671136) + v9))):
            v4 = (load32(9671140) + (v4 + v9))
            store32(9671132, (load32(9671140) + (v4 + v9)))
            store32(ENTITIES, func228(load32(ENTITIES), v4, v7))
        v13 = (100 if (u32(arg0) >= u32(100)) else 0)
        arg0 = (arg0 + v2)
        v7 = v8
        while True:  # $label9
            v6 = (v8 - v12)
            v2 = ((v12 << 1) | 1)
            v14 = (((v8 - v12) + ((v12 << 1) | 1)) - 1)
            v4 = (v20 - v12)
            v21 = (v2 + (v20 - v12))
            v15 = ((v2 + (v20 - v12)) - 1)
            v2 = v4
            while True:  # $label3
                while True:  # $label5
                    while True:  # $label2
                        v3 = load32(9142440)
                        if (u32(v6) >= u32(load32(9142440))):
                            break
                        if ((v2 | v6) < 0):
                            break
                        if (u32(v2) >= u32(v3)):
                            break
                        v3 = func34(load32(39064), 0, v2, v6, 0, 1)
                        if func34(load32(39064), 0, v2, v6, 0, 1):
                            v16 = entities[v3]
                            store64(entities[v3].range, 2147483648500)
                            store32(v16 + 52, (arg0 + v13))
                            arg0 = 0
                        v5 = (v5 + (v3 != 0))
                        if (u32((v5 + (v3 != 0))) >= u32(v9)):
                            break
                        v3 = load32(9142440)
                        break
                    while True:  # $label4
                        if (u32(v3) <= u32(v14)):
                            break
                        if ((v2 | v14) < 0):
                            break
                        if (u32(v2) >= u32(v3)):
                            break
                        v3 = func34(load32(39064), 0, v2, v14, 0, 1)
                        if func34(load32(39064), 0, v2, v14, 0, 1):
                            v16 = entities[v3]
                            store64(entities[v3].range, 2147483648500)
                            store32(v16 + 52, (arg0 + v13))
                            arg0 = 0
                        v5 = (v5 + (v3 != 0))
                        if (u32((v5 + (v3 != 0))) >= u32(v9)):
                            break
                        break
                    v2 = (v2 + 1)
                    if ((v2 + 1) < v21):
                        continue
                    break
                v2 = (v6 + 1)
                if (v14 > (v6 + 1)):
                    while True:  # $label8
                        while True:  # $label6
                            v3 = load32(9142440)
                            if (u32(v2) >= u32(load32(9142440))):
                                break
                            if ((v2 | v4) < 0):
                                break
                            if (u32(v3) <= u32(v4)):
                                break
                            v3 = func34(load32(39064), 0, v4, v2, 0, 1)
                            if func34(load32(39064), 0, v4, v2, 0, 1):
                                v6 = entities[v3]
                                store64(entities[v3].range, 2147483648500)
                                store32(v6 + 52, (arg0 + v13))
                                arg0 = 0
                            v5 = (v5 + (v3 != 0))
                            if (u32((v5 + (v3 != 0))) >= u32(v9)):
                                break
                            v3 = load32(9142440)
                            break
                        while True:  # $label7
                            if (u32(v2) >= u32(v3)):
                                break
                            if ((v2 | v15) < 0):
                                break
                            if (u32(v3) <= u32(v15)):
                                break
                            v3 = func34(load32(39064), 0, v15, v2, 0, 1)
                            if func34(load32(39064), 0, v15, v2, 0, 1):
                                v6 = entities[v3]
                                store64(entities[v3].range, 2147483648500)
                                store32(v6 + 52, (arg0 + v13))
                                arg0 = 0
                            v5 = (v5 + (v3 != 0))
                            if (u32((v5 + (v3 != 0))) >= u32(v9)):
                                break
                            break
                        v2 = (v2 + 1)
                        if ((v2 + 1) != v7):
                            continue
                        break
                v7 = (v7 + 1)
                v12 = (v12 + 1)
                if ((v12 + 1) != 512):
                    continue
                break
            break
        store32(v11 + 283956, (load32(v11 + 283956) + v19))
        if not v10:
            break
        if (load32(9671152) != v18):
            break
        if (u32(load32(9671136)) >= u32(4)):
            arg0 = 3
            while True:  # $label11
                while True:  # $label10
                    v2 = entities[arg0]
                    if (load16u(entities[arg0] + 110) != v10):
                        break
                    if load8u(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 332):
                        func78(v2, 0, 0, 1)
                        break
                    break
                arg0 = (arg0 + 1)
                if (u32((arg0 + 1)) < u32(load32(9671136))):
                    continue
                break
        arg0 = (v17 + (v10 * 286704))
        store32((v17 + (v10 * 286704)) + 283976, 0)
        store32(arg0 + 283848, 0)
        v2 = load32(arg0 + 281788)
        if load32(arg0 + 281788):
            store32(v2 + 8, 0)
        arg0 = load32(arg0 + 281792)
        if load32(arg0 + 281792):
            store32(arg0 + 8, 0)
        arg0 = (v17 + (v10 * 286704))
        v2 = load32((v17 + (v10 * 286704)) + 281796)
        if load32((v17 + (v10 * 286704)) + 281796):
            store32(v2 + 8, 0)
        v2 = load32(arg0 + 284628)
        arg0 = load32(arg0 + 284616)
        store32(arg1 + 4, v11)
        store32(arg1, 118)
        store32(arg1 + 8, (arg0 if arg0 else v2))
        a_b()
        if (load32(CURRENT_PLAYER) != v10):
            break
        a_b()
        break
    G.global0 = (arg1 + 16)

# ----------------------------------------------------------
# $func850
# ----------------------------------------------------------
def func850(arg0, arg1):
    func146(arg0, load32(38728))

# ----------------------------------------------------------
# $func851
# ----------------------------------------------------------
def func851(arg0, arg1):
    v5 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v10 = ((arg0 & 0xFFFFFFFF) >> 16)
    v15 = (((arg0 & 0xFFFFFFFF) >> 16) + 3)
    v11 = (arg0 & 65535)
    v16 = ((arg0 & 65535) + 3)
    v17 = (v10 - 2)
    v7 = (v11 - 2)
    v8 = entities[arg1]
    v18 = load32((players[load16u(entities[arg1] + 110)] + 284356))
    while True:  # $label6
        v14 = (v7 + 1)
        arg0 = (v7 - v11)
        v19 = (((v7 - v11) * arg0) - 1)
        arg0 = v17
        while True:  # $label5
            while True:  # $label0
                arg1 = arg0
                arg0 = (arg0 - v10)
                if ((v19 + ((arg0 - v10) * arg0)) > 4):
                    break
                arg0 = load32(9142440)
                if (u32(load32(9142440)) <= u32(arg1)):
                    break
                if ((arg1 | v7) < 0):
                    break
                if (u32(arg0) <= u32(v7)):
                    break
                v20 = ((v18 & 0xFFFFFFFF) >> ((v7 != v11) | (arg1 != v10)))
                v21 = (arg1 + 1)
                arg0 = 0
                while True:  # $label4
                    while True:  # $label1
                        v4 = (load32(9142440) + 2)
                        v4 = load32((load32(9142840) + ((v14 + ((v21 + ((load32(9142440) + 2) * arg0)) * v4)) << 2)))
                        if (u32(load32((load32(9142840) + ((v14 + ((v21 + ((load32(9142440) + 2) * arg0)) * v4)) << 2)))) < u32(3)):
                            break
                        v4 = entities[v4]
                        v6 = load8u(entities[v4].sub_state)
                        v2 = load32(((load8u(entities[v4].sub_state) * 404) + ENTITY_TYPES) + 284)
                        if not load32(((load8u(entities[v4].sub_state) * 404) + ENTITY_TYPES) + 284):
                            break
                        v9 = load8u(v4 + 125)
                        if (load8u(v4 + 125) == 10):
                            break
                        v2 = (v2 * v20)
                        # TODO: i32.div_u
                        v2 = ((v2 * v20) if (u32(v2) < u32(100)) else 100)
                        v3 = load32(v4 + 64)
                        v2 = (((v2 * v20) if (u32(v2) < u32(100)) else 100) if (u32(v2) < u32(v3)) else load32(v4 + 64))
                        v3 = load16u(v4 + 110)
                        v12 = load32(PLAYERS)
                        v22 = load16u(v8 + 110)
                        v13 = load32(players[load16u(v8 + 110)] + 278556)
                        if load32(players[load16u(v8 + 110)] + 278556):
                            v13 = (v13 + ((load8u(v8 + 122) + (v3 * 255)) << 2))
                            store32((v13 + ((load8u(v8 + 122) + (v3 * 255)) << 2)), (load32(v13) + v2))
                        v3 = load32(((v12 + (v3 * 286704)) + 278564))
                        if load32(((v12 + (v3 * 286704)) + 278564)):
                            v3 = (v3 + (((v22 * 255) + v6) << 2))
                            store32((v3 + (((v22 * 255) + v6) << 2)), (load32(v3) + v2))
                        if (v9 == 3):
                            break
                        v3 = (v4 - -64)
                        v6 = load32((v4 - -64))
                        if (u32(v2) < u32(load32((v4 - -64)))):
                            store32(v3, (v6 - v2))
                            if not load32(v4 + 92):
                                break
                            if load8u(9147141):
                                break
                            store32(v5, v2)
                            a_b()
                            break
                        store32(v3, 0)
                        v6 = load32(PLAYERS)
                        v3 = load16u(v8 + 110)
                        v2 = players[load16u(v8 + 110)]
                        while True:  # $label2
                            if not load32(9147132):
                                break
                            if (load32(9671152) != load8u(v4 + 122)):
                                break
                            v9 = load16u(v4 + 110)
                            if (v3 == load16u(v4 + 110)):
                                break
                            if not v3:
                                break
                            v3 = (v6 + (v9 * 286704))
                            v9 = load32((v6 + (v9 * 286704)) + 284628)
                            v6 = load32(v3 + 284616)
                            v12 = load32(v2 + 284616)
                            store32(v5 + 32, (load32(v2 + 284616) if v12 else load32(v2 + 284628)))
                            store32(v5 + 28, v2)
                            store32(v5 + 20, v3)
                            store32(v5 + 16, 927)
                            store32(v5 + 24, (v6 if v6 else v9))
                            a_b()
                            break
                        while True:  # $label3
                            v3 = load32((v2 + 278560))
                            if not load32((v2 + 278560)):
                                v2 = load16u(v4 + 110)
                                break
                            v2 = load16u(v4 + 110)
                            v3 = (v3 + ((load8u(v8 + 122) + (load16u(v4 + 110) * 255)) << 2))
                            store32((v3 + ((load8u(v8 + 122) + (load16u(v4 + 110) * 255)) << 2)), (load32(v3) + 1))
                            break
                        v2 = load32((players[v2] + 278568))
                        if load32((players[v2] + 278568)):
                            v2 = (v2 + ((load8u(v4 + 122) + (load16u(v8 + 110) * 255)) << 2))
                            store32((v2 + ((load8u(v4 + 122) + (load16u(v8 + 110) * 255)) << 2)), (load32(v2) + 1))
                        store16(v4 + 116, load32(v8 + 28))
                        break
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != 3):
                        continue
                    break
                break
            arg0 = (arg1 + 1)
            if (arg1 != v15):
                continue
            break
        arg0 = (v7 == v16)
        v7 = v14
        if not arg0:
            continue
        break
    G.global0 = (v5 + 48)

# ----------------------------------------------------------
# $func852
# ----------------------------------------------------------
def func852(arg0, arg1):
    v7 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v2 = ((arg0 & -32) - load32(9142952))
    v2 = ((arg1 & -32) - load32(9142956))
    v2 = (((((arg0 & -32) - load32(9142952)) * v2) + (((arg1 & -32) - load32(9142956)) * v2)) - 1)
    while True:  # $label0
        while True:  # $label1
            v4 = ((arg0 & 0xFFFFFFFF) >> 5)
            v5 = ((arg1 & 0xFFFFFFFF) >> 5)
            v3 = load32(9142440)
            v6 = (load32(9142440) + 2)
            if (load32((load32(9142840) + ((((arg0 & 0xFFFFFFFF) >> 5) + (((((arg1 & 0xFFFFFFFF) >> 5) + (load32(9142440) + 2)) + 1) * v6)) << 2)) + 4) == 1):
                if (v2 > 9000000):
                    v2 = 9142540
                    break
                v6 = load32(39836)
                v2 = 9142540
                v8 = load32(load32(GAME_STATE) + 48)
                if not load32(load32(GAME_STATE) + 48):
                    break
                if load8u(9147152):
                    break
                v3 = load16u((load32(9147376) + (((v3 * v5) + v4) << 1)))
                if (v8 == 2):
                    if (u32(v3) > u32(1)):
                        break
                    break
                if v3:
                    break
                break
            if (v2 > 9000000):
                v2 = 9142544
                break
            v6 = load32(39832)
            v2 = 9142544
            v8 = load32(load32(GAME_STATE) + 48)
            if not load32(load32(GAME_STATE) + 48):
                break
            if load8u(9147152):
                break
            v3 = load16u((load32(9147376) + (((v3 * v5) + v4) << 1)))
            if (v8 == 2):
                if (u32(v3) > u32(1)):
                    break
                break
            if not v3:
                break
            break
        store32(v7 + 8, v5)
        store32(v7 + 4, v4)
        store32(v7, v6)
        a_b()
        break
    v3 = load32(v2)
    while True:  # $label3
        while True:  # $label2
            v6 = load32(load32(GAME_STATE) + 48)
            if not load32(load32(GAME_STATE) + 48):
                break
            if load8u(9147152):
                break
            v2 = load16u((load32(9147376) + (((load32(9142440) * v5) + v4) << 1)))
            if (v6 == 2):
                if (u32(v2) > u32(1)):
                    break
                break
            if not v2:
                break
            break
        v2 = (v4 * v5)
        # TODO: f32.demote_f64
        func80(i32(((arg0 + (((v4 * v5) * v4) & 31)) - 16)), i32(((arg1 + ((v2 * v5) & 31)) - 16)), v3, 1.0, (i32(arg1) * 0.7))
        break
    G.global0 = (v7 + 16)

# ----------------------------------------------------------
# $func853
# ----------------------------------------------------------
def func853(arg0, arg1):
    while True:  # $label0
        if not arg1:
            break
        v3 = load32(ENTITIES)
        v6 = entities[arg0]
        v7 = load8u(entities[arg0].unit_class)
        arg1 = load8u(entities[arg0].unit_class)
        if (load8u(entities[arg0].unit_class) == 3):
            break
        while True:  # $label1
            if (arg1 == 12):
                break
            arg1 = (v3 + (arg0 * 132))
            v2 = load32((v3 + (arg0 * 132)) + 72)
            v5 = load32(arg1 + 76)
            if (u32(load32((v3 + (arg0 * 132)) + 72)) < u32(load32(arg1 + 76))):
                v2 = (load32((players[load16u(arg1 + 110)] + 284072)) + v2)
                v2 = ((load32((players[load16u(arg1 + 110)] + 284072)) + v2) if (u32(v2) < u32(v5)) else v5)
                store32(arg1 + 72, ((load32((players[load16u(arg1 + 110)] + 284072)) + v2) if (u32(v2) < u32(v5)) else v5))
            while True:  # $label2
                v4 = load32(arg1 + 96)
                if load32(arg1 + 96):
                    v4 = entities[v4]
                    if ((load8u(entities[v4].unit_class) & 251) != 3):
                        if (load32(v4 + 32) == arg0):
                            break
                    store32(arg1 + 96, 0)
                break
            v4 = 0
            if (v2 != v5):
                break
            if v4:
                break
            if load32((v3 + (arg0 * 132)) + 36):
                break
            if (v7 == 1):
                break
            func403(v6)
            break
        arg0 = (v3 + (arg0 * 132))
        v3 = load32((v3 + (arg0 * 132)) + 80)
        v2 = players[load16u(arg0 + 110)]
        arg1 = load32((players[load16u(arg0 + 110)] + 284320))
        if (u32(load32((v3 + (arg0 * 132)) + 80)) >= u32(load32((players[load16u(arg0 + 110)] + 284320)))):
            break
        arg0 = (load32((v2 + 284076)) + v3)
        store32(arg0 + 80, ((load32((v2 + 284076)) + v3) if (u32(arg0) < u32(arg1)) else arg1))
        break

# ----------------------------------------------------------
# $func854
# ----------------------------------------------------------
def func854(arg0, arg1):
    while True:  # $label0
        v2 = ((arg1 * 404) + ENTITY_TYPES)
        v4 = load32(((arg1 * 404) + ENTITY_TYPES) + 236)
        if not load32(((arg1 * 404) + ENTITY_TYPES) + 236):
            break
        arg1 = 0
        v7 = load32(PLAYERS)
        v5 = load32(v2 + 92)
        v2 = load32(v2 + 232)
        if (u32(v4) >= u32(4)):
            v9 = (v4 & -4)
            v3 = ((v7 + (arg0 * 286704)) + 269376)
            while True:  # $label1
                v6 = (arg1 << 2)
                store32((v3 + (load32((v2 + (arg1 << 2))) * 36)), v5)
                store32((v3 + (load32((v2 + (v6 | 4))) * 36)), v5)
                store32((v3 + (load32((v2 + (v6 | 8))) * 36)), v5)
                store32((v3 + (load32((v2 + (v6 | 12))) * 36)), v5)
                arg1 = (arg1 + 4)
                v8 = (v8 + 4)
                if ((v8 + 4) != v9):
                    continue
                break
        v4 = (v4 & 3)
        if not (v4 & 3):
            break
        v3 = 0
        arg0 = (v7 + (arg0 * 286704))
        while True:  # $label2
            store32(((arg0 + (load32((v2 + (arg1 << 2))) * 36)) + 269376), v5)
            arg1 = (arg1 + 1)
            v3 = (v3 + 1)
            if ((v3 + 1) != v4):
                continue
            break
        break

# ----------------------------------------------------------
# $func855
# ----------------------------------------------------------
def func855(arg0, arg1, arg2):
    if arg2:
        v4 = load32(arg0)
        v3 = load32(ENTITIES)
        arg0 = 0
        while True:  # $label0
            v5 = (v3 + (load32((arg1 + (arg0 << 2))) * 132))
            if (load8u((v3 + (load32((arg1 + (arg0 << 2))) * 132)) + 125) != 3):
                v3 = load32(ENTITIES)
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break

# ----------------------------------------------------------
# $func856
# ----------------------------------------------------------
def func856(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v1 + 12, arg0)
    arg0 = load32(9213808)
    while True:  # $label0
        if load8u(9147210):
            func41(11, 9173808, arg0, (v1 + 12), 1)
            break
        v3 = (arg0 << 2)
        v2 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy
        break
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $func857
# ----------------------------------------------------------
def func857(arg0, arg1):

# ----------------------------------------------------------
# $func858
# ----------------------------------------------------------
def func858(arg0, arg1):
    v4 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    arg1 = load32(ENTITIES)
    while True:  # $label0
        if (u32(load32(9142848)) < u32((load32(load32(GAME_STATE) + 72) * 2400))):
            func29((arg1 + (arg0 * 132)), 1)
            break
        while True:  # $label1
            v2 = (arg0 * 132)
            v3 = (arg1 + (arg0 * 132))
            if (load8u((arg1 + (arg0 * 132)) + 125) == 3):
                break
            if not load8u(v3 + 128):
                break
            arg1 = (arg1 + (arg0 * 132))
            store8((arg1 + (arg0 * 132)) + 127, 0)
            while True:  # $label2
                v5 = load32(arg1 + 40)
                if not load32(arg1 + 40):
                    break
                if load8u(9142916):
                    store32(v4 + 20, v5)
                    store32(v4 + 16, 0)
                    a_b()
                    break
                arg1 = load16u(arg1 + 110)
                store32(v4 + 4, v5)
                store32(v4, (arg1 + 16))
                a_b()
                break
            store8(v3 + 128, 0)
            arg1 = load32(ENTITIES)
            break
        v2 = (arg1 + v2)
        v9 = load16u((arg1 + v2) + 110)
        v3 = load32(PLAYERS)
        arg1 = load16u(v2 + 116)
        v5 = load16u(v2 + 118)
        v10 = (arg1 - 2)
        v2 = players[load16u(v2 + 110)]
        arg1 = load32((players[load16u(v2 + 110)] + 284272))
        v14 = (v10 + load32((players[load16u(v2 + 110)] + 284272)))
        if ((arg1 - 2) >= (v10 + load32((players[load16u(v2 + 110)] + 284272)))):
            break
        v5 = (v5 - 2)
        v15 = (arg1 + v5)
        if ((v5 - 2) >= (arg1 + v5)):
            break
        v12 = load32((v2 + 284276))
        arg1 = (v3 + (v9 * 286704))
        v7 = ((v3 + (v9 * 286704)) + 281768)
        v13 = (arg1 + 283908)
        v8 = (arg1 + 281764)
        v6 = load32(9142440)
        while True:  # $label7
            v3 = (v10 + 1)
            arg1 = v5
            while True:  # $label6
                v2 = arg1
                arg1 = (arg1 + 1)
                while True:  # $label3
                    if (u32(v2) >= u32(v6)):
                        break
                    if ((v2 | v10) < 0):
                        break
                    if (u32(v6) <= u32(v10)):
                        break
                    while True:  # $label4
                        v11 = load32(9142840)
                        v9 = (v6 + 2)
                        v2 = load32((load32(9142840) + ((v3 + (arg1 * (v6 + 2))) << 2)))
                        if (u32(load32((load32(9142840) + ((v3 + (arg1 * (v6 + 2))) << 2)))) <= u32(2)):
                            break
                        if (arg0 == v2):
                            break
                        v2 = entities[v2]
                        if not load32(((load8u(entities[v2].sub_state) * 404) + ENTITY_TYPES) + 344):
                            break
                        if (u32(((load8u(v2 + 125) - 9) & 255)) < u32(2)):
                            break
                        store32(v8, (load32(v8) + 1))
                        if load8u((load32(9143004) + (load32(v13) + (load32(PLAYER_COUNT) * load16u(v2 + 110))))):
                            store32(v7, (load32(v7) + load32(v2 + 64)))
                        func204(v2, v12)
                        v6 = load32(9142440)
                        v9 = (load32(9142440) + 2)
                        v11 = load32(9142840)
                        break
                    while True:  # $label5
                        v2 = load32((v11 + ((v3 + ((arg1 + v9) * v9)) << 2)))
                        if (u32(load32((v11 + ((v3 + ((arg1 + v9) * v9)) << 2)))) < u32(3)):
                            break
                        if (arg0 == v2):
                            break
                        v2 = entities[v2]
                        if not load32(((load8u(entities[v2].sub_state) * 404) + ENTITY_TYPES) + 344):
                            break
                        if (u32(((load8u(v2 + 125) - 9) & 255)) < u32(2)):
                            break
                        store32(v8, (load32(v8) + 1))
                        if load8u((load32(9143004) + (load32(v13) + (load32(PLAYER_COUNT) * load16u(v2 + 110))))):
                            store32(v7, (load32(v7) + load32(v2 + 64)))
                        func204(v2, v12)
                        v11 = load32(9142840)
                        v6 = load32(9142440)
                        break
                    v2 = (v6 + 2)
                    v2 = load32((v11 + ((v3 + ((arg1 + ((v6 + 2) << 1)) * v2)) << 2)))
                    if (u32(load32((v11 + ((v3 + ((arg1 + ((v6 + 2) << 1)) * v2)) << 2)))) < u32(3)):
                        break
                    if (arg0 == v2):
                        break
                    v2 = entities[v2]
                    if not load32(((load8u(entities[v2].sub_state) * 404) + ENTITY_TYPES) + 344):
                        break
                    if (u32(((load8u(v2 + 125) - 9) & 255)) < u32(2)):
                        break
                    store32(v8, (load32(v8) + 1))
                    if load8u((load32(9143004) + (load32(v13) + (load32(PLAYER_COUNT) * load16u(v2 + 110))))):
                        store32(v7, (load32(v7) + load32(v2 + 64)))
                    func204(v2, v12)
                    v6 = load32(9142440)
                    break
                if (arg1 != v15):
                    continue
                break
            v10 = v3
            if (v3 != v14):
                continue
            break
        break
    G.global0 = (v4 + 32)

# ----------------------------------------------------------
# $kd
# Export: kd
# ----------------------------------------------------------
def kd(arg0):
    """Export: kd"""
    v1 = load8u(9681940)
    while True:  # $label1
        while True:  # $label0
            v2 = load32(9142400)
            if not load32(9142400):
                break
            if v1:
                break
            if not load8u(59182):
                break
            break
        while True:  # $label2
            if not load8u(9142917):
                if v1:
                    store8(9681940, 0)
                    v1 = load32(9142440)
                    v1 = (load32(9142440) * v1)
                    if not ((load32(9142440) * v1) << 2):
                        break
                    # TODO: memory.fill
                    break
                v1 = load32(9142440)
                v1 = (load32(9142440) * v1)
                v1 = (-1 if (v1 & 805306368) else ((load32(9142440) * v1) << 4))
                v2 = func26((-1 if (v1 & 805306368) else ((load32(9142440) * v1) << 4)))
                # TODO: memory.fill
                store32(9142400, v2)
                break
            store8(9681940, 0)
            break
        while True:  # $label3
            if not arg0:
                break
            if load8u(9147152):
                break
            if not load8u(9147212):
                break
            break
        break
    if load8u(9142917):
        a_b()
    func152()
    if not load8u(9147152):
    return (0 if load8u(9142917) else load32(9142400))

# ----------------------------------------------------------
# $jd
# Export: jd
# ----------------------------------------------------------
def jd(arg0):
    """Export: jd"""
    v1 = load8u(9681940)
    while True:  # $label1
        while True:  # $label0
            v3 = load32(9142404)
            if not load32(9142404):
                break
            if v1:
                break
            if not load8u(59182):
                break
            break
        while True:  # $label2
            if v1:
                store8(9681940, 0)
                v1 = load32(9142440)
                if not ((load32(9142440) * v1) * 3):
                    break
                while True:  # $label3
                    store32((v3 + (v2 << 2)), 0)
                    v2 = (v2 + 1)
                    v1 = load32(9142440)
                    if (u32((v2 + 1)) < u32(((load32(9142440) * v1) * 3))):
                        continue
                    break
                break
            v1 = load32(9142440)
            v2 = (load32(9142440) * v1)
            v2 = (-1 if (u32((v2 * 3)) > u32(1073741823)) else ((load32(9142440) * v1) * 12))
            v3 = func26((-1 if (u32((v2 * 3)) > u32(1073741823)) else ((load32(9142440) * v1) * 12)))
            # TODO: memory.fill
            store32(9142404, v3)
            break
        while True:  # $label4
            if not arg0:
                break
            if load8u(9147152):
                break
            if not load8u(9147212):
                break
            break
        break
    func152()
    if not load8u(9147152):
    return (0 if load8u(9142917) else load32(9142404))

# ----------------------------------------------------------
# $ha
# Export: ha
# ----------------------------------------------------------
def ha(arg0):
    """Export: ha"""
    store32(9561756, arg0)
    v2 = (load32(9561764) + 1)
    store32(9561764, (load32(9561764) + 1))
    v1 = 2
    if (u32(v2) <= u32(7)):
        v1 = load32(9561760)
        if load32(9561760):
            return (arg0 == v1)
    else:
    return 2

# ----------------------------------------------------------
# $wd
# Export: wd
# ----------------------------------------------------------
def wd(arg0, arg1):
    """Export: wd"""
    store32(9147120, arg0)
    if not arg1:
        func45()

# ----------------------------------------------------------
# $ld
# Export: ld
# ----------------------------------------------------------
def ld(arg0):
    """Export: ld"""
    v13 = load32(9142440)
    v3 = (arg0 + 2)
    v12 = ((arg0 + 2) * v3)
    v6 = func26((-1 if (u32((v12 * 3)) > u32(1073741823)) else (((arg0 + 2) * v3) * 12)))
    if v3:
        v10 = (v3 & -2)
        v15 = (arg0 & 1)
        v5 = (arg0 + 1)
        v16 = (v13 + 2)
        v7 = ((v13 + 2) << 1)
        v17 = (v3 << 1)
        v9 = ((v3 << 1) * v3)
        v8 = load32(9142840)
        v4 = (arg0 == -1)
        while True:  # $label6
            while True:  # $label1
                if not v1:
                    v2 = 0
                    v14 = 0
                    if not v4:
                        while True:  # $label0
                            store32((v6 + ((v2 * v3) << 2)), -1)
                            store32((v6 + (((v2 + v3) * v3) << 2)), -1)
                            store32((v6 + (((v2 + v17) * v3) << 2)), -1)
                            v11 = (v2 | 1)
                            store32((v6 + (((v2 | 1) * v3) << 2)), -1)
                            store32((v6 + (((v3 + v11) * v3) << 2)), -1)
                            store32((v6 + (((v11 + v17) * v3) << 2)), -1)
                            v2 = (v2 + 2)
                            v14 = (v14 + 2)
                            if ((v14 + 2) != v10):
                                continue
                            break
                    if not v15:
                        break
                    store32((v6 + ((v2 * v3) << 2)), -1)
                    store32((v6 + (((v2 + v3) * v3) << 2)), -1)
                    store32((v6 + (((v2 + v17) * v3) << 2)), -1)
                    break
                store32((v6 + (v1 << 2)), -1)
                store32((v6 + ((v1 + v12) << 2)), -1)
                store32((v6 + ((v1 + v9) << 2)), -1)
                v2 = 1
                if (v3 == 1):
                    break
                while True:  # $label5
                    while True:  # $label2
                        if not ((v2 != v5) & (v1 != v5)):
                            store32((v6 + (((v2 * v3) + v1) << 2)), -1)
                            store32((v6 + ((((v2 + v3) * v3) + v1) << 2)), -1)
                            break
                        while True:  # $label4
                            while True:  # $label3
                                if (u32(v2) >= u32(v13)):
                                    break
                                if (u32(v1) >= u32(v13)):
                                    break
                                if ((v1 | v2) >= 0):
                                    break
                                break
                            store32((v6 + (((v2 * v3) + v1) << 2)), 0)
                            store32((v6 + ((((v2 + v3) * v3) + v1) << 2)), 0)
                            break
                            break
                        store32((v6 + (((v2 * v3) + v1) << 2)), load32((v8 + (((v2 * v16) + v1) << 2))))
                        store32((v6 + ((((v2 + v3) * v3) + v1) << 2)), load32((v8 + ((((v2 + v16) * v16) + v1) << 2))))
                        break
                    store32(0, load32((v8 + ((((v2 + v7) * v16) + v1) << 2))))
                    v2 = (v2 + 1)
                    if ((v2 + 1) != v3):
                        continue
                    break
                break
            v1 = (v1 + 1)
            if ((v1 + 1) != v3):
                continue
            break
    v12 = (arg0 * arg0)
    v11 = func26((arg0 * arg0))
    v4 = (-1 if (v12 & 805306368) else (v12 << 4))
    v15 = func26((-1 if (v12 & 805306368) else (v12 << 4)))
    # TODO: memory.fill
    v1 = v13
    if (v13 * v1):
        v2 = load32(9147288)
        v8 = 0
        while True:  # $label7
            v9 = (v2 + v8)
            v4 = load8s((v2 + v8))
            if (load8s((v2 + v8)) < 0):
                store8(v9, (v4 ^ -1))
                v2 = load32(9147288)
                v1 = load32(9142440)
            v8 = (v8 + 1)
            if (u32((v8 + 1)) < u32((v1 * v1))):
                continue
            break
    if arg0:
        # TODO: memory.fill
    if v1:
        v4 = 0
        while True:  # $label10
            v9 = (v4 + 1)
            v8 = 0
            while True:  # $label9
                while True:  # $label8
                    if not ((u32(arg0) > u32(v4)) & (u32(arg0) > u32(v8))):
                        v14 = load32(9142840)
                        v8 = (v8 + 1)
                        v2 = (v1 + 2)
                        v7 = load32((load32(9142840) + ((v9 + ((v8 + 1) * (v1 + 2))) << 2)))
                        if (u32((load32((load32(9142840) + ((v9 + ((v8 + 1) * (v1 + 2))) << 2))) - 3)) < u32(-4)):
                            v5 = entities[v7]
                            v10 = func26(4)
                            v1 = (func26(4) + 4)
                            v7 = load32(v5)
                            if load32(v5):
                                store32(v5 + 4, v7)
                            store32(v5 + 8, v1)
                            store32(v5 + 4, v10)
                            store32(v5, v10)
                            # TODO: memory.fill
                            v1 = load32(9142440)
                            v2 = (load32(9142440) + 2)
                            v14 = load32(9142840)
                        v7 = load32((v14 + ((v9 + ((v2 + v8) * v2)) << 2)))
                        if (u32((load32((v14 + ((v9 + ((v2 + v8) * v2)) << 2))) - 3)) <= u32(-5)):
                            v5 = entities[v7]
                            v10 = func26(4)
                            v1 = (func26(4) + 4)
                            v7 = load32(v5)
                            if load32(v5):
                                store32(v5 + 4, v7)
                            store32(v5 + 8, v1)
                            store32(v5 + 4, v10)
                            store32(v5, v10)
                            # TODO: memory.fill
                            v1 = load32(9142440)
                            v2 = (load32(9142440) + 2)
                            v14 = load32(9142840)
                        v7 = load32((v14 + ((v9 + ((v8 + (v2 << 1)) * v2)) << 2)))
                        if (u32((load32((v14 + ((v9 + ((v8 + (v2 << 1)) * v2)) << 2))) - 3)) > u32(-5)):
                            break
                        v5 = entities[v7]
                        v10 = func26(4)
                        v1 = (func26(4) + 4)
                        v7 = load32(v5)
                        if load32(v5):
                            store32(v5 + 4, v7)
                        store32(v5 + 8, v1)
                        store32(v5 + 4, v10)
                        store32(v5, v10)
                        # TODO: memory.fill
                        v1 = load32(9142440)
                        break
                    store8((v11 + ((arg0 * v8) + v4)), load8u((load32(9147288) + ((v1 * v8) + v4))))
                    v8 = (v8 + 1)
                    break
                if (u32(v1) > u32(v8)):
                    continue
                break
            v4 = v9
            if (u32(v9) < u32(v1)):
                continue
            break
    v4 = load32(9142840)
    if load32(9142840):
        store32(9142840, 0)
    v4 = load32(9147288)
    if load32(9147288):
        store32(9147288, 0)
    v4 = load32(9142400)
    if load32(9142400):
        store32(9142400, 0)
    v4 = load32(9142432)
    if load32(9142432):
        store32(9142432, 0)
    v4 = load32(9142436)
    if load32(9142436):
        store32(9142436, 0)
    store32(9147288, v11)
    store32(9142840, v6)
    store32(9142400, v15)
    v1 = (v12 << 1)
    v4 = func26((v12 << 1))
    # TODO: memory.fill
    store32(9142440, arg0)
    store32(9142436, v4)
    v1 = (-1 if (u32(v12) > u32(1073741823)) else (v12 << 2))
    v4 = func26((-1 if (u32(v12) > u32(1073741823)) else (v12 << 2)))
    # TODO: memory.fill
    store32(9147372, (arg0 + 1))
    store32(9147368, arg0)
    store32(9147364, (arg0 - 1))
    store32(9147360, -1)
    store32(9147356, (arg0 ^ -1))
    store32(9147352, (0 - arg0))
    store32(9147348, (1 - arg0))
    store32(9147344, 1)
    store32(9142432, v4)
    if (u32(arg0) < u32(v13)):
        v9 = 0
        v11 = load32(9681936)
        v2 = load32(load32(9681936) + 8)
        if load32(load32(9681936) + 8):
            v4 = load32(9684500)
            v10 = load32(9684496)
            while True:  # $label16
                v15 = (load32(v11) + (v9 << 2))
                v7 = load32((load32(v11) + (v9 << 2)))
                arg0 = 0
                while True:  # $label11
                    v13 = load32((v10 - 16))
                    if load32((v10 - 16)):
                        while True:  # $label12
                            v1 = (v10 + (arg0 * 60))
                            if (load32((v10 + (arg0 * 60)) + 52) == v7):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v13):
                                continue
                            break
                    arg0 = 0
                    v1 = v4
                    if (load32(v4 + 52) == v7):
                        break
                    while True:  # $label13
                        arg0 = (arg0 + 1)
                        v1 = (v4 + ((arg0 + 1) * 60))
                        if (load32((v4 + ((arg0 + 1) * 60)) + 52) != v7):
                            continue
                        break
                    break
                while True:  # $label14
                    arg0 = (load32(9142440) << 5)
                    if (u32((load32(9142440) << 5)) >= u32((load32(v1) + (load32(v15 + 4) - load32(v1 + 8))))):
                        if (u32((load32(v15 + 8) + ((load32(v1 + 4) // (load32(v1 + 16) * load32(v1 + 20))) - load32(v1 + 12)))) <= u32(arg0)):
                            break
                    func38(load32(v15 + 12))
                    v11 = load32(9681936)
                    v2 = (load32(v11 + 8) - 4)
                    store32(load32(9681936) + 8, (load32(v11 + 8) - 4))
                    v4 = load32(9684500)
                    v10 = load32(9684496)
                    if (u32(v2) > u32(v9)):
                        v13 = load32(v11)
                        arg0 = v9
                        while True:  # $label15
                            v1 = (v13 + (arg0 << 2))
                            store32((v13 + (arg0 << 2)), load32(v1 + 16))
                            arg0 = (arg0 + 1)
                            v2 = load32(v11 + 8)
                            if (u32((arg0 + 1)) < u32(load32(v11 + 8))):
                                continue
                            break
                    v9 = (v9 - 4)
                    break
                v9 = (v9 + 4)
                if (u32((v9 + 4)) < u32(v2)):
                    continue
                break
    return func115(0, 0, arg0, 0, 0)
