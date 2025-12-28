"""
Tzar Engine - Core module (part 11).
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
# $pc
# Export: pc
# ----------------------------------------------------------
def pc(arg0, arg1, arg2):
    """Export: pc"""
    v5 = (G.global0 - 96)
    G.global0 = (G.global0 - 96)
    while True:  # $label0
        if load8u(9684432):
            break
        if not load32(51776):
            store8(9215872, 1)
            while True:  # $label1
                v3 = load32(9216000)
                if (load32(9216000) != load32(9215996)):
                    v4 = load32(9215992)
                    break
                v4 = (load32(9216004) + v3)
                store32(9215996, (load32(9216004) + v3))
                v6 = load32(9215992)
                v4 = func26((-1 if (u32(v4) > u32(1073741823)) else (v4 << 2)))
                if v3:
                    # TODO: memory.copy
                if v6:
                    v3 = load32(9216000)
                store32(9215992, v4)
                break
            store32(9216000, (v3 + 1))
            store32((v4 + (v3 << 2)), arg0)
            while True:  # $label2
                arg0 = load32(9216000)
                if (load32(9216000) != load32(9215996)):
                    v3 = v4
                    break
                v3 = (load32(9216004) + arg0)
                store32(9215996, (load32(9216004) + arg0))
                v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                if arg0:
                    # TODO: memory.copy
                store32(9215992, v3)
                arg0 = load32(9216000)
                break
            store32(9216000, (arg0 + 1))
            store32((v3 + (arg0 << 2)), arg1)
            while True:  # $label3
                arg1 = load32(9216000)
                if (load32(9216000) != load32(9215996)):
                    arg0 = v3
                    break
                arg0 = (load32(9216004) + arg1)
                store32(9215996, (load32(9216004) + arg1))
                arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                if arg1:
                    # TODO: memory.copy
                store32(9215992, arg0)
                arg1 = load32(9216000)
                break
            store32(9216000, (arg1 + 1))
            store32((arg0 + (arg1 << 2)), arg2)
            break
        while True:  # $label4
            if arg2:
                store32(9681444, arg1)
                store32(9681440, arg0)
                break
            arg1 = load32(9681444)
            arg0 = load32(9681440)
            break
        while True:  # $label5
            v15 = i32(load32(9142860))
            v15 = loadf32(40616)
            v16 = loadf32(9671164)
            v17 = (((i32(load32(9142860)) - ((v15 * loadf32(40616)) / loadf32(9671164))) * 0.5) + ((v15 * i32(arg1)) + i32(load32(9142956))))
            if (abs((((i32(load32(9142860)) - ((v15 * loadf32(40616)) / loadf32(9671164))) * 0.5) + ((v15 * i32(arg1)) + i32(load32(9142956))))) < 2147483650.0):
                break
            break
        arg1 = -2147483648
        while True:  # $label6
            v17 = i32(load32(9142856))
            v15 = (((v15 * i32(arg0)) + i32(load32(9142952))) + ((i32(load32(9142856)) - ((v15 * v17) / v16)) * 0.5))
            if (abs((((v15 * i32(arg0)) + i32(load32(9142952))) + ((i32(load32(9142856)) - ((v15 * v17) / v16)) * 0.5))) < 2147483650.0):
                break
            break
        arg0 = -2147483648
        if load8u(9681884):
            break
        arg2 = load8u(9142409)
        if load8u(9142409):
            if load32(9142900):
                break
        if load32(9684792):
            arg2 = load32(9684792)
            v6 = load32(load32(9684792))
            v7 = (arg0 - load32(load32(9684792)))
            v10 = load32(arg2 + 8)
            arg1 = (load32(arg2 + 20) * load32(arg2 + 16))
            if (load32(arg2 + 20) * load32(arg2 + 16)):
            else:
            v11 = ((load32(arg2 + 4) // arg1) - 0)
            arg0 = (((load32(arg2 + 4) // arg1) - 0) // 32)
            v12 = load32(arg2 + 12)
            while True:  # $label7
                v3 = (v7 // 32)
                v6 = ((v3 + (v6 // 32)) + ((v6 & 31) != 0))
                if ((v7 // 32) >= ((v3 + (v6 // 32)) + ((v6 & 31) != 0))):
                    v8 = load32(9142440)
                    v4 = 1
                    break
                arg1 = (load32(arg2 + 4) // arg1)
                arg1 = ((((load32(arg2 + 4) // arg1) // 32) + arg0) + ((arg1 & 31) != 0))
                v13 = (arg0 if (arg0 > arg1) else ((((load32(arg2 + 4) // arg1) // 32) + arg0) + ((arg1 & 31) != 0)))
                v8 = load32(9142440)
                v9 = (load32(9142440) + 2)
                v14 = load32(9142840)
                while True:  # $label9
                    v3 = (v3 + 1)
                    arg1 = arg0
                    while True:  # $label8
                        if (arg1 != v13):
                            arg1 = (arg1 + 1)
                            if (load32((v14 + (((((arg1 + 1) + v9) * v9) + v3) << 2))) != 1):
                                continue
                            break
                        break
                    v4 = (v3 >= v6)
                    if (v3 != v6):
                        continue
                    break
                break
            break
        while True:  # $label10
            if load32(9671176):
                break
            if not arg2:
                break
            v15 = i32(arg1)
            v16 = i32(load32(59140))
            arg2 = (v15 < v16)
            v17 = (i32(arg1) if (v15 < v16) else i32(load32(59140)))
            v18 = i32(arg0)
            v19 = i32(load32(59132))
            v3 = (v18 < v19)
            v20 = (i32(arg0) if (v18 < v19) else i32(load32(59132)))
            while True:  # $label11
                if not load8u(59183):
                    v15 = abs((v15 - v16))
                    break
                while True:  # $label12
                    v15 = (v17 * 0.03125)
                    if (abs((v17 * 0.03125)) < 2147483650.0):
                        break
                    break
                v17 = i32((-2147483648 << 5))
                v15 = (ceil((abs((i32(v15) - i32((-2147483648 << 5)))) * 0.03125)) * 32.0)
                while True:  # $label13
                    v16 = (v20 * 0.03125)
                    if (abs((v20 * 0.03125)) < 2147483650.0):
                        break
                    break
                v20 = i32((-2147483648 << 5))
                break
            v18 = (ceil((abs((i32(v16) - i32((-2147483648 << 5)))) * 0.03125)) * 32.0)
            if not load8u(9142410):
                store8(9142410, 1)
            if load8u(9142916):
                break
            v3 = load32(9142876)
            v16 = 0.0
            arg2 = (G.global0 - 32)
            G.global0 = (G.global0 - 32)
            if load8u(9142916):
                v16 = ((0.0 / i32((load32(9142440) * 96))) + 0.25)
            store32(arg2 + 24, v3)
            # TODO: f64.promote_f32
            storef64(arg2 + 16, v16)
            # TODO: f64.promote_f32
            storef64(arg2 + 8, (v17 + -0.0))
            # TODO: f64.promote_f32
            storef64(arg2, (v20 + -0.0))
            a_b()
            G.global0 = (arg2 + 32)
            if load8u(9142916):
                break
            store64((v5 - -64), 0)
            store64(v5 + 72, 0)
            store32(v5 + 80, load32(9142876))
            # TODO: f64.promote_f32
            storef64(v5 + 56, v15)
            # TODO: f64.promote_f32
            storef64(v5 + 48, neg(v18))
            a_b()
            break
        arg2 = (arg0 // 32)
        while True:  # $label17
            while True:  # $label15
                while True:  # $label16
                    while True:  # $label14
                        v4 = load32(9142440)
                        v6 = (arg1 // 32)
                        if (u32(load32(9142440)) <= u32((arg1 // 32))):
                            break
                        if ((arg2 | v6) < 0):
                            break
                        if (u32(arg2) >= u32(v4)):
                            break
                        v7 = load8u(9147152)
                        if not (0 if load8u(9147152) else load32(load32(GAME_STATE) + 48)):
                            v3 = load32(40604)
                            break
                        v3 = load32(40604)
                        if load16u((load32(9147376) + (((v4 * v6) + arg2) << 1))):
                            break
                        if (v3 != -1):
                            break
                        break
                        break
                    v3 = load32(40604)
                    if (load32(40604) != -1):
                        break
                    break
                if load32(9216064):
                    break
                store32(41088, 2)
                store64(v5 + 32, 2)
                break
                break
            if (v3 != -1):
                break
            if v7:
                break
            if load32(9216064):
                break
            while True:  # $label18
                arg0 = func141(arg0, arg1)
                if func141(arg0, arg1):
                    arg1 = load32(9213808)
                    if load32(9213808):
                        break
                store32(41088, 2)
                store64(v5 + 16, 2)
                break
                break
            arg0 = func161(entities[arg0], 9173808, arg1)
            if func161(entities[arg0], 9173808, arg1):
                break
            store32(41088, 2)
            store64(v5, 2)
            break
            break
        if not load8u(((v3 * 40) + 9671200) + 17):
            break
        break
    G.global0 = (v5 + 96)
    return func145(v3, not func141(arg0, arg1))

# ----------------------------------------------------------
# $func358
# ----------------------------------------------------------
def func358(arg0, arg1):
    v2 = 4
    while True:  # $label2
        while True:  # $label0
            if ((arg0 | arg1) & 3):
                break
            while True:  # $label1
                if (load32(arg0) != load32(arg1)):
                    break
                arg1 = (arg1 + 4)
                arg0 = (arg0 + 4)
                v2 = (v2 - 4)
                if (u32((v2 - 4)) > u32(3)):
                    continue
                break
            if not v2:
                break
            break
        while True:  # $label3
            v3 = load8u(arg0)
            v4 = load8u(arg1)
            if (load8u(arg0) == load8u(arg1)):
                arg1 = (arg1 + 1)
                arg0 = (arg0 + 1)
                v2 = (v2 - 1)
                if (v2 - 1):
                    continue
                break
            break
        return (v3 - v4)
        break
    return 0

# ----------------------------------------------------------
# $func359
# ----------------------------------------------------------
def func359(arg0, arg1):
    v5 = load32(arg0 + 124)
    v5 = load32(arg0 + 120)
    v9 = (load32(arg0 + 124) if (u32(load32(arg0 + 120)) < u32(load32(arg0 + 140))) else ((v5 & 0xFFFFFFFF) >> 2))
    v3 = load32(arg0 + 108)
    v2 = ((load32(arg0 + 108) - load32(arg0 + 44)) + 262)
    v12 = (((load32(arg0 + 108) - load32(arg0 + 44)) + 262) if (u32(v2) <= u32(v3)) else 0)
    v2 = load32(arg0 + 144)
    v8 = load32(arg0 + 116)
    v13 = (load32(arg0 + 144) if (u32(v2) < u32(v8)) else load32(arg0 + 116))
    v14 = load32(arg0 + 56)
    v7 = (load32(arg0 + 56) + v3)
    v15 = ((load32(arg0 + 56) + v3) + 258)
    v3 = (v5 + v7)
    v10 = load8u((v5 + v7))
    v11 = load8u((v3 - 1))
    v16 = load32(arg0 + 52)
    v17 = load32(arg0 + 64)
    while True:  # $label10
        while True:  # $label9
            while True:  # $label0
                v4 = (arg1 + v14)
                v3 = ((arg1 + v14) + v5)
                if (load8u(((arg1 + v14) + v5)) != v10):
                    break
                if (load8u((v3 - 1)) != v11):
                    break
                if (load8u(v4) != load8u(v7)):
                    break
                v3 = 2
                if (load8u(v4 + 1) != load8u(v7 + 1)):
                    break
                while True:  # $label7
                    while True:  # $label6
                        while True:  # $label5
                            while True:  # $label4
                                while True:  # $label3
                                    while True:  # $label2
                                        while True:  # $label1
                                            while True:  # $label8
                                                v2 = (v3 + v7)
                                                if (load8u((v3 + v7) + 1) == load8u(v4 + 3)):
                                                    if (load8u(v2 + 2) != load8u(v4 + 4)):
                                                        break
                                                    if (load8u(v2 + 3) != load8u(v4 + 5)):
                                                        break
                                                    if (load8u(v2 + 4) != load8u(v4 + 6)):
                                                        break
                                                    if (load8u(v2 + 5) != load8u(v4 + 7)):
                                                        break
                                                    if (load8u(v2 + 6) != load8u(v4 + 8)):
                                                        break
                                                    if (load8u(v2 + 7) != load8u(v4 + 9)):
                                                        break
                                                    v2 = (v3 + 8)
                                                    v6 = (v7 + (v3 + 8))
                                                    if (load8u((v7 + (v3 + 8))) != load8u(v4 + 10)):
                                                        break
                                                    v4 = (v4 + 8)
                                                    v18 = (u32(v3) < u32(250))
                                                    v3 = v2
                                                    if v18:
                                                        continue
                                                    break
                                                break
                                            v6 = (v2 + 1)
                                            break
                                            break
                                        v6 = (v2 + 2)
                                        break
                                        break
                                    v6 = (v2 + 3)
                                    break
                                    break
                                v6 = (v2 + 4)
                                break
                                break
                            v6 = (v2 + 5)
                            break
                            break
                        v6 = (v2 + 6)
                        break
                        break
                    v6 = (v2 + 7)
                    break
                v2 = (v6 - v15)
                v3 = ((v6 - v15) + 258)
                if (((v6 - v15) + 258) <= v5):
                    break
                store32(arg0 + 112, arg1)
                if (v3 >= v13):
                    v5 = v3
                    break
                v10 = load8u((v3 + v7))
                v11 = load8u((v2 + v7) + 257)
                v5 = v3
                break
            arg1 = load16u((v17 + ((arg1 & v16) << 1)))
            if (u32(v12) >= u32(load16u((v17 + ((arg1 & v16) << 1))))):
                break
            v9 = (v9 - 1)
            if (v9 - 1):
                continue
            break
        break
    return (v5 if (u32(v5) < u32(v8)) else v8)

# ----------------------------------------------------------
# $func360
# ----------------------------------------------------------
def func360(arg0, arg1):
    if load8u(9147210):
        func41(5, 9173808, arg1, arg0, (7 if arg0 else 0))
        return
    v3 = (arg1 << 2)
    v2 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
    if arg1:
        # TODO: memory.copy

# ----------------------------------------------------------
# $func361
# ----------------------------------------------------------
def func361():
    while True:  # $label0
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v5 = load32(PLAYERS)
        v3 = 1
        v1 = 1
        while True:  # $label5
            if load8u(9147127):
                while True:  # $label4
                    v2 = (v5 + (v3 * 286704))
                    store32((v5 + (v3 * 286704)) + 283892, func88(v2))
                    v0 = 0
                    v1 = load32((v2 + 278572))
                    v4 = load32(load32((v2 + 278572)) + 8)
                    if load32(load32((v2 + 278572)) + 8):
                        v6 = load32(v1)
                        v1 = 0
                        while True:  # $label1
                            v1 = (load32((v6 + (v0 << 2))) + v1)
                            v0 = (v0 + 15)
                            if (u32((v0 + 15)) < u32(v4)):
                                continue
                            break
                        # TODO: i32.div_u
                        v0 = 6
                    store32(v2 + 283888, v0)
                    if (load32(9147128) == 9):
                        # TODO: i32.div_u
                        v0 = load32(9561724)
                    store32(v2 + 283884, v0)
                    v4 = (v2 + 283884)
                    while True:  # $label2
                        v2 = load32(v2 + 284608)
                        v1 = load32(9561720)
                        if (load32(v2 + 284608) != load32(9561720)):
                            break
                        if not v1:
                            break
                        # TODO: i32.div_u
                        store32((v0 * 155), 100)
                        v1 = load32(9561720)
                        break
                    v0 = load32(PLAYER_COUNT)
                    while True:  # $label3
                        if (v1 == v2):
                            break
                        if not v1:
                            break
                        if (v0 != 3):
                            break
                        if (load32(9147128) != 1):
                            break
                        store32(v4, 0)
                        v0 = load32(PLAYER_COUNT)
                        break
                    v3 = (v3 + 1)
                    if (u32((v3 + 1)) < u32(v0)):
                        continue
                    break
                break
            while True:  # $label6
                v0 = (v5 + (v1 * 286704))
                v2 = func88(v0)
                store32((v5 + (v1 * 286704)) + 283884, func88(v0))
                store32(v0 + 283892, v2)
                v1 = (v1 + 1)
                v0 = load32(PLAYER_COUNT)
                if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                    continue
                break
            break
        if (u32(v0) < u32(2)):
            break
        v3 = load32(PLAYERS)
        v2 = 1
        while True:  # $label9
            v0 = (v3 + (v2 * 286704))
            store32((v3 + (v2 * 286704)) + 283944, 1)
            v1 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) >= u32(2)):
                v4 = (v0 + 283944)
                v6 = (v0 + 283884)
                v5 = 1
                v0 = 1
                while True:  # $label8
                    while True:  # $label7
                        if (v0 == v2):
                            break
                        v7 = load32((v3 + (v0 * 286704)) + 283884)
                        v8 = load32(v6)
                        if (u32(load32((v3 + (v0 * 286704)) + 283884)) <= u32(load32(v6))):
                            if (v7 != v8):
                                break
                            if (u32(v0) <= u32(v2)):
                                break
                        v5 = (v5 + 1)
                        store32(v4, (v5 + 1))
                        v1 = load32(PLAYER_COUNT)
                        break
                    v0 = (v0 + 1)
                    if (u32((v0 + 1)) < u32(v1)):
                        continue
                    break
            v2 = (v2 + 1)
            if (u32((v2 + 1)) < u32(v1)):
                continue
            break
        break

# ----------------------------------------------------------
# $func362
# ----------------------------------------------------------
def func362(arg0, arg1):
    v2 = 2
    while True:  # $label3
        while True:  # $label0
            if (u32(arg1) <= u32(2)):
                v3 = load32(arg0 + 283960)
                break
            v5 = (arg1 - 2)
            v7 = ((arg1 - 2) & 3)
            v3 = load32(arg0 + 283960)
            v6 = load32(PLAYERS)
            if (u32((arg1 - 3)) >= u32(3)):
                v9 = (v5 & -4)
                arg1 = 0
                while True:  # $label1
                    v5 = (v6 + (v2 * 286704))
                    v4 = ((((v4 + (load32((v6 + (v2 * 286704)) + 283960) == v3)) + (load32((v6 + ((v2 | 1) * 286704)) + 283960) == v3)) + (load32((v5 + 857368)) == v3)) + (load32((v5 + 1144072)) == v3))
                    v2 = (v2 + 4)
                    arg1 = (arg1 + 4)
                    if ((arg1 + 4) != v9):
                        continue
                    break
            if v7:
                while True:  # $label2
                    v4 = (v4 + (load32((v6 + (v2 * 286704)) + 283960) == v3))
                    v2 = (v2 + 1)
                    v8 = (v8 + 1)
                    if ((v8 + 1) != v7):
                        continue
                    break
            break
        v2 = (v4 * 20)
        if (u32((v4 * 20)) < u32(load16u(((v3 << 1) + 9142944)))):
            v3 = load32(((v3 << 2) + 9142928))
            v2 = (v2 << 1)
            arg1 = (load32(((v3 << 2) + 9142928)) + (v2 << 1))
            store16(arg0, load16u((load32(((v3 << 2) + 9142928)) + (v2 << 1))))
            store16(arg0 + 2, load16u((v3 + (v2 | 2))))
            store16(arg0 + 4, load16u((v3 + (v2 | 4))))
            store16(arg0 + 6, load16u((v3 + (v2 | 6))))
            store16(arg0 + 8, load16u(arg1 + 8))
            store16(arg0 + 10, load16u(arg1 + 10))
            store16(arg0 + 12, load16u(arg1 + 12))
            store16(arg0 + 14, load16u(arg1 + 14))
            store16(arg0 + 16, load16u(arg1 + 16))
            store16(arg0 + 18, load16u(arg1 + 18))
            store16(arg0 + 20, load16u(arg1 + 20))
            store16(arg0 + 22, load16u(arg1 + 22))
            store16(arg0 + 24, load16u(arg1 + 24))
            store16(arg0 + 26, load16u(arg1 + 26))
            store16(arg0 + 28, load16u(arg1 + 28))
            store16(arg0 + 30, load16u(arg1 + 30))
            store16(arg0 + 32, load16u(arg1 + 32))
            store16(arg0 + 34, load16u(arg1 + 34))
            store16(arg0 + 36, load16u(arg1 + 36))
            v3 = 19
            break
        store16(arg0 + 8, 101)
        store64(arg0, 32088563964837972)
        v3 = 5
        break
    v2 = 100
    store16((arg0 + (v3 << 1)), v2)
    return load16u(arg1 + 38)

# ----------------------------------------------------------
# $func363
# ----------------------------------------------------------
def func363(arg0, arg1):
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v4 + 12, arg1)
    v2 = (G.global0 - 208)
    G.global0 = (G.global0 - 208)
    store32(v2 + 204, arg1)
    arg1 = (v2 + 160)
    # TODO: memory.fill
    store32(v2 + 200, load32(v2 + 204))
    while True:  # $label0
        if (func352(0, arg0, (v2 + 200), (v2 + 80), arg1) < 0):
            break
        if (load32(52668) >= 0):
            while True:  # $label1
                arg1 = load32(G.global3 + 24)
                if (load32(G.global3 + 24) == (load32(52668) & -1073741825)):
                    break
                v3 = 1
                # TODO: i32.atomic.rmw.cmpxchg
                if not arg1:
                    break
                v7 = (arg1 | 1073741824)
                # TODO: i32.atomic.rmw.cmpxchg
                arg1 = (arg1 | 1073741824)
                if not (arg1 | 1073741824):
                    break
                while True:  # $label3
                    v5 = (arg1 | 1073741824)
                    while True:  # $label2
                        if not (arg1 & 1073741824):
                            # TODO: i32.atomic.rmw.cmpxchg
                            if (arg1 != v5):
                                break
                        func439(52668, v5)
                        break
                    # TODO: i32.atomic.rmw.cmpxchg
                    arg1 = v7
                    if v7:
                        continue
                    break
                break
        arg1 = load32(52592)
        if (load32(52664) <= 0):
            store32(52592, (arg1 & -33))
        while True:  # $label6
            while True:  # $label5
                while True:  # $label4
                    if not load32(52640):
                        store32(52640, 80)
                        store32(52620, 0)
                        store64(52608, 0)
                        v6 = load32(52636)
                        store32(52636, v2)
                        break
                    if load32(52608):
                        break
                    break
                if func433(52592):
                    break
                break
            break
        arg0 = func352(52592, arg0, (v2 + 200), (v2 + 80), (v2 + 160))
        if v6:
            store32(52640, 0)
            store32(52636, v6)
            store32(52620, 0)
            store64(52608, 0)
        else:
        store32(52592, (load32(52592) | (arg1 & 32)))
        if not v3:
            break
        # TODO: i32.atomic.rmw.xchg
        if (0 & 1073741824):
            func97(52668)
        break
    G.global0 = (v2 + 208)
    G.global0 = (v4 + 16)
    return 52668

# ----------------------------------------------------------
# $func364
# ----------------------------------------------------------
def func364(arg0, arg1, arg2):
    while True:  # $label0
        v5 = load32(arg0)
        v3 = ((load32(arg0) * 404) + ENTITY_TYPES)
        v6 = (1 if (load32(((load32(arg0) * 404) + ENTITY_TYPES) + 368) != 55) else arg2)
        if not (1 if (load32(((load32(arg0) * 404) + ENTITY_TYPES) + 368) != 55) else arg2):
            break
        v7 = (v3 + 68)
        arg2 = 0
        while True:  # $label2
            arg0 = entities[load32((arg1 + (arg2 << 2)))]
            v4 = players[load16u(entities[load32((arg1 + (arg2 << 2)))] + 110)]
            v8 = (players[load16u(entities[load32((arg1 + (arg2 << 2)))] + 110)] + (v5 << 2))
            if load32(((players[load16u(entities[load32((arg1 + (arg2 << 2)))] + 110)] + (v5 << 2)) + 281808)):
                break
            if load8u(arg0 + 125):
                break
            if func66(v4, v7, 1, 1):
                break
            if (load32(v3 + 368) != 55):
                store32((v8 + 282828), 1)
            store8(arg0 + 125, 5)
            # TODO: i32.div_u
            func63(arg0, 5, v5, ((load32(v3 + 116) * load32(load32(GAME_STATE) + 132)) * 1000), 100)
            while True:  # $label1
                if not load32(arg0 + 92):
                    break
                v4 = load8u(9147141)
                if load32(9140316):
                    if (load32(9140320) != load32(arg0 + 28)):
                        break
                break
            arg2 = (arg2 + 1)
            if ((arg2 + 1) != v6):
                continue
            break
        break

# ----------------------------------------------------------
# $func365
# ----------------------------------------------------------
def func365(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    v9 = (arg8 << 2)
    v10 = load32(((arg8 << 2) + 9344))
    v14 = load32((v9 + 9264))
    v11 = load32(9142440)
    while True:  # $label3
        while True:  # $label2
            while True:  # $label1
                if (((28728 & 0xFFFFFFFF) >> arg8) & 1):
                    while True:  # $label0
                        arg8 = ((v14 * 5) + arg2)
                        if ((((v14 * 5) + arg2) if (arg2 > arg8) else arg2) > arg0):
                            break
                        if ((arg2 if (arg2 > arg8) else arg8) < arg0):
                            break
                        arg8 = (arg1 - arg3)
                        break
                        break
                    v9 = (arg1 - arg3)
                    v9 = ((arg1 - arg3) * v9)
                    arg8 = (arg0 - arg8)
                    arg8 = (((arg1 - arg3) * v9) + ((arg0 - arg8) * arg8))
                    v12 = (arg0 - arg2)
                    v9 = (v9 + ((arg0 - arg2) * v12))
                    break
                if not (((74898 & 0xFFFFFFFF) >> arg8) & 1):
                    break
                arg8 = (arg0 - arg2)
                arg8 = ((arg0 - arg2) * arg8)
                v9 = ((v10 * 5) + arg3)
                v12 = (arg3 > v9)
                if ((arg1 >= (((v10 * 5) + arg3) if (arg3 > v9) else arg3)) & ((arg3 if v12 else v9) >= arg1)):
                    break
                v9 = (arg1 - v9)
                v9 = (((arg1 - v9) * v9) + arg8)
                arg8 = (arg1 - arg3)
                arg8 = (arg8 + ((arg1 - arg3) * arg8))
                break
            if not ((((arg1 - v9) * v9) + arg8) if (u32(arg8) > u32(v9)) else (arg8 + ((arg1 - arg3) * arg8))):
                break
            v12 = (v11 + 2)
            v15 = (((v11 + 2) * arg5) + 1)
            v13 = load32(9142840)
            while True:  # $label5
                while True:  # $label4
                    if (u32(arg3) >= u32(v11)):
                        break
                    if (u32(arg2) >= u32(v11)):
                        break
                    if ((arg2 | arg3) < 0):
                        break
                    arg8 = arg2
                    v9 = arg3
                    if (load32((((arg2 + ((v15 + arg3) * v12)) << 2) + v13) + 4) == arg4):
                        break
                    break
                arg8 = (arg2 + v14)
                while True:  # $label6
                    v9 = (arg3 + v10)
                    if (u32(v11) <= u32((arg3 + v10))):
                        break
                    if (u32(arg8) >= u32(v11)):
                        break
                    if ((arg8 | v9) < 0):
                        break
                    if (load32((((arg8 + ((v9 + v15) * v12)) << 2) + v13) + 4) == arg4):
                        break
                    break
                arg8 = (arg8 + v14)
                while True:  # $label7
                    v9 = (v9 + v10)
                    if (u32(v11) <= u32((v9 + v10))):
                        break
                    if (u32(arg8) >= u32(v11)):
                        break
                    if ((arg8 | v9) < 0):
                        break
                    if (load32((((arg8 + ((v9 + v15) * v12)) << 2) + v13) + 4) == arg4):
                        break
                    break
                arg8 = (arg8 + v14)
                while True:  # $label8
                    v9 = (v9 + v10)
                    if (u32(v11) <= u32((v9 + v10))):
                        break
                    if (u32(arg8) >= u32(v11)):
                        break
                    if ((arg8 | v9) < 0):
                        break
                    if (load32((((arg8 + ((v9 + v15) * v12)) << 2) + v13) + 4) == arg4):
                        break
                    break
                arg8 = (arg8 + v14)
                while True:  # $label9
                    v9 = (v9 + v10)
                    if (u32(v11) <= u32((v9 + v10))):
                        break
                    if (u32(arg8) >= u32(v11)):
                        break
                    if ((arg8 | v9) < 0):
                        break
                    if (load32((((arg8 + ((v9 + v15) * v12)) << 2) + v13) + 4) == arg4):
                        break
                    break
                v9 = (v9 + v10)
                if (u32(v11) <= u32((v9 + v10))):
                    break
                arg8 = (arg8 + v14)
                if (u32(v11) <= u32((arg8 + v14))):
                    break
                if ((arg8 | v9) < 0):
                    break
                if (load32((((arg8 + ((v9 + v15) * v12)) << 2) + v13) + 4) != arg4):
                    break
                break
            arg2 = (arg2 - arg0)
            arg2 = (arg2 >> 31)
            arg2 = (((arg2 - arg0) ^ (arg2 >> 31)) - arg2)
            arg3 = (arg3 - arg1)
            arg3 = (arg3 >> 31)
            arg3 = (((arg3 - arg1) ^ (arg3 >> 31)) - arg3)
            v15 = (((((arg2 - arg0) ^ (arg2 >> 31)) - arg2) if (u32(arg2) > u32(arg3)) else (((arg3 - arg1) ^ (arg3 >> 31)) - arg3)) << 5)
            store32(59200, (arg8 + (v9 << 16)))
            v24 = load32(9142436)
            v13 = 1
            v10 = 1
            while True:  # $label23
                arg2 = load32(((v25 << 2) + 59200))
                arg8 = ((load32(((v25 << 2) + 59200)) & 0xFFFFFFFF) >> 16)
                v9 = (arg2 & 65535)
                arg2 = ((((load32(((v25 << 2) + 59200)) & 0xFFFFFFFF) >> 16) * v11) + (arg2 & 65535))
                while True:  # $label10
                    if not v13:
                        if (load16u((v24 + (arg2 << 1))) == (v14 & 65535)):
                            break
                    v20 = load32(9142436)
                    v21 = (load32(9142436) + (arg2 << 1))
                    v17 = load32(9142440)
                    v19 = (load32(9142440) + 2)
                    v22 = ((load32(9142440) + 2) * arg5)
                    v18 = (((load32(9142440) + 2) * arg5) + 1)
                    v23 = load32(ENTITIES)
                    v12 = load32(9142840)
                    while True:  # $label22
                        arg2 = (arg1 - arg8)
                        while True:  # $label11
                            arg3 = (arg0 - v9)
                            if not (arg0 - v9):
                                break
                            if (arg1 == arg8):
                                break
                            arg3 = (arg2 // arg3)
                            arg3 = (arg3 >> 31)
                            arg3 = (arg3 if (u32((((arg2 // arg3) ^ (arg3 >> 31)) - arg3)) <= u32(1)) else 0)
                            arg2 = ((arg3 if (u32((((arg2 // arg3) ^ (arg3 >> 31)) - arg3)) <= u32(1)) else 0) // arg2)
                            arg2 = (arg2 >> 31)
                            arg2 = (arg2 if (u32(((((arg3 if (u32((((arg2 // arg3) ^ (arg3 >> 31)) - arg3)) <= u32(1)) else 0) // arg2) ^ (arg2 >> 31)) - arg2)) <= u32(1)) else 0)
                            break
                        v16 = (-1 if (arg2 < 0) else (arg2 != 0))
                        arg2 = ((-1 if (arg2 < 0) else (arg2 != 0)) + arg8)
                        while True:  # $label12
                            v26 = (-1 if (arg3 < 0) else (arg3 != 0))
                            arg3 = ((-1 if (arg3 < 0) else (arg3 != 0)) + v9)
                            if (((-1 if (arg3 < 0) else (arg3 != 0)) + v9) != arg0):
                                break
                            if (arg1 != arg2):
                                break
                            store32(arg6, (0 - v26))
                            store32(arg7, (0 - v16))
                            return 1
                            break
                        if not v13:
                            store16((v20 + (((arg2 * v11) + arg3) << 1)), v14)
                        while True:  # $label13
                            v16 = load32((((arg3 + (v19 * (arg2 + v18))) << 2) + v12) + 4)
                            if (load32((((arg3 + (v19 * (arg2 + v18))) << 2) + v12) + 4) == arg4):
                                break
                            if (v16 != -1):
                                if (load8u((v23 + (v16 * 132)) + 125) == 1):
                                    break
                            while True:  # $label14
                                if not v13:
                                    arg2 = (v9 + 1)
                                    arg3 = load32(9142436)
                                    v13 = load32(ENTITIES)
                                    v20 = (v9 + 2)
                                    v23 = ((arg8 + v18) * v19)
                                    v17 = load32((v12 + (((v9 + 2) + ((arg8 + v18) * v19)) << 2)))
                                    if (arg4 != load32((v12 + (((v9 + 2) + ((arg8 + v18) * v19)) << 2)))):
                                        if (v17 == -1):
                                            break
                                        if (load8u((v13 + (v17 * 132)) + 125) != 1):
                                            break
                                    if (load16u((arg3 + (((arg8 * v11) + arg2) << 1))) == (v14 & 65535)):
                                        break
                                    store32(((v10 << 2) + 59200), ((arg8 << 16) + arg2))
                                    v10 = (v10 + 1)
                                    if (u32((v10 + 1)) <= u32(v15)):
                                        break
                                    break
                                arg2 = load16u(40596)
                                arg3 = (load16u(40596) + 2)
                                store16(40596, (load16u(40596) + 2))
                                while True:  # $label15
                                    if (u32((arg3 & 65535)) < u32(65534)):
                                        break
                                    store16(40596, 1)
                                    arg3 = (v17 * v17)
                                    if not (v17 * v17):
                                        break
                                    # TODO: memory.fill
                                    break
                                v14 = (arg2 + 1)
                                store32(((v10 << 2) + 59200), ((arg8 << 16) + v9))
                                v10 = (v10 + 1)
                                break
                                break
                            v17 = (arg8 - 1)
                            while True:  # $label16
                                v21 = ((arg8 + v22) * v19)
                                v16 = load32((v12 + ((arg2 + ((arg8 + v22) * v19)) << 2)))
                                if (arg4 != load32((v12 + ((arg2 + ((arg8 + v22) * v19)) << 2)))):
                                    if (v16 == -1):
                                        break
                                    if (load8u((v13 + (v16 * 132)) + 125) != 1):
                                        break
                                if (load16u((arg3 + (((v11 * v17) + v9) << 1))) == (v14 & 65535)):
                                    break
                                store32(((v10 << 2) + 59200), ((v17 << 16) + v9))
                                v10 = (v10 + 1)
                                if (u32((v10 + 1)) <= u32(v15)):
                                    break
                                break
                                break
                            v16 = (v9 - 1)
                            while True:  # $label17
                                v22 = load32((v12 + ((v9 + v23) << 2)))
                                if (arg4 != load32((v12 + ((v9 + v23) << 2)))):
                                    if (v22 == -1):
                                        break
                                    if (load8u((v13 + (v22 * 132)) + 125) != 1):
                                        break
                                if (load16u((arg3 + (((arg8 * v11) + v16) << 1))) == (v14 & 65535)):
                                    break
                                store32(((v10 << 2) + 59200), ((arg8 << 16) + v16))
                                v10 = (v10 + 1)
                                if (u32((v10 + 1)) <= u32(v15)):
                                    break
                                break
                                break
                            while True:  # $label18
                                arg8 = (arg8 + 1)
                                v19 = ((v18 + (arg8 + 1)) * v19)
                                v18 = load32((v12 + ((arg2 + ((v18 + (arg8 + 1)) * v19)) << 2)))
                                if (arg4 != load32((v12 + ((arg2 + ((v18 + (arg8 + 1)) * v19)) << 2)))):
                                    if (v18 == -1):
                                        break
                                    if (load8u((v13 + (v18 * 132)) + 125) != 1):
                                        break
                                if (load16u((arg3 + (((arg8 * v11) + v9) << 1))) == (v14 & 65535)):
                                    break
                                store32(((v10 << 2) + 59200), ((arg8 << 16) + v9))
                                v10 = (v10 + 1)
                                if (u32((v10 + 1)) <= u32(v15)):
                                    break
                                break
                                break
                            while True:  # $label19
                                v18 = load32((v12 + ((v20 + v21) << 2)))
                                if (arg4 != load32((v12 + ((v20 + v21) << 2)))):
                                    if (v18 == -1):
                                        break
                                    if (load8u((v13 + (v18 * 132)) + 125) != 1):
                                        break
                                if (load16u((arg3 + (((v11 * v17) + arg2) << 1))) == (v14 & 65535)):
                                    break
                                store32(((v10 << 2) + 59200), ((v17 << 16) + arg2))
                                v10 = (v10 + 1)
                                if (u32((v10 + 1)) <= u32(v15)):
                                    break
                                break
                                break
                            while True:  # $label20
                                v18 = load32((v12 + ((v9 + v21) << 2)))
                                if (arg4 != load32((v12 + ((v9 + v21) << 2)))):
                                    if (v18 == -1):
                                        break
                                    if (load8u((v13 + (v18 * 132)) + 125) != 1):
                                        break
                                if (load16u((arg3 + (((v11 * v17) + v16) << 1))) == (v14 & 65535)):
                                    break
                                store32(((v10 << 2) + 59200), ((v17 << 16) + v16))
                                v10 = (v10 + 1)
                                if (u32((v10 + 1)) <= u32(v15)):
                                    break
                                break
                                break
                            while True:  # $label21
                                v9 = load32((v12 + ((v9 + v19) << 2)))
                                if (arg4 != load32((v12 + ((v9 + v19) << 2)))):
                                    if (v9 == -1):
                                        break
                                    if (load8u((v13 + (v9 * 132)) + 125) != 1):
                                        break
                                if (load16u((arg3 + (((arg8 * v11) + v16) << 1))) == (v14 & 65535)):
                                    break
                                store32(((v10 << 2) + 59200), ((arg8 << 16) + v16))
                                v10 = (v10 + 1)
                                if (u32((v10 + 1)) <= u32(v15)):
                                    break
                                break
                                break
                            v9 = load32((v12 + ((v19 + v20) << 2)))
                            if (arg4 != load32((v12 + ((v19 + v20) << 2)))):
                                if (v9 == -1):
                                    break
                                if (load8u((v13 + (v9 * 132)) + 125) != 1):
                                    break
                            if (load16u((arg3 + (((arg8 * v11) + arg2) << 1))) == (v14 & 65535)):
                                break
                            store32(((v10 << 2) + 59200), ((arg8 << 16) + arg2))
                            v10 = (v10 + 1)
                            if (u32((v10 + 1)) <= u32(v15)):
                                break
                            break
                            break
                        store16(v21, v14)
                        v9 = arg3
                        arg8 = arg2
                        continue
                        break
                    raise Unreachable()
                    break
                v13 = 0
                v25 = (v25 + 1)
                if (u32((v25 + 1)) < u32(v10)):
                    continue
                break
            break
        return 0
        break
    return 0

# ----------------------------------------------------------
# $func366
# ----------------------------------------------------------
def func366():
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    if not load32(9690440):
        store32(9690460, 2)
        store64(9690452, -1)
        store64(9690444, 17592186048512)
        store32(MEM_FLAGS, 2)
        store32(v1 + 12, 0)
        v0 = (G.global0 - 32)
        store64((G.global0 - 32) + 24, 0)
        store64(v0 + 16, 0)
        store64(v0 + 8, 0)
        store64(MEM_MUTEX, load64(v0 + 8))
        store64(9690928, load64(v0 + 24))
        store64(9690920, load64(v0 + 16))
        v0 = (v1 + 12)
        if (v1 + 12):
            store32(MEM_MUTEX, load32(v0))
        store32(9690440, (((v1 + 8) & -16) ^ 1431655768))
    func54(9690960)
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $func367
# ----------------------------------------------------------
def func367(arg0):
    v2 = (arg0 + 148)
    while True:  # $label0
        v3 = (v1 << 2)
        store16((v2 + (v1 << 2)), 0)
        store16((v2 + (v3 | 4)), 0)
        v1 = (v1 + 2)
        if ((v1 + 2) != 286):
            continue
        break
    store16(arg0 + 2684, 0)
    store16(arg0 + 2440, 0)
    store16((arg0 + 2756), 0)
    store16((arg0 + 2752), 0)
    store16((arg0 + 2748), 0)
    store16((arg0 + 2744), 0)
    store16((arg0 + 2740), 0)
    store16((arg0 + 2736), 0)
    store16((arg0 + 2732), 0)
    store16((arg0 + 2728), 0)
    store16((arg0 + 2724), 0)
    store16((arg0 + 2720), 0)
    store16((arg0 + 2716), 0)
    store16((arg0 + 2712), 0)
    store16((arg0 + 2708), 0)
    store16((arg0 + 2704), 0)
    store16((arg0 + 2700), 0)
    store16((arg0 + 2696), 0)
    store16((arg0 + 2692), 0)
    store16((arg0 + 2688), 0)
    store16((arg0 + 2556), 0)
    store16((arg0 + 2552), 0)
    store16((arg0 + 2548), 0)
    store16((arg0 + 2544), 0)
    store16((arg0 + 2540), 0)
    store16((arg0 + 2536), 0)
    store16((arg0 + 2532), 0)
    store16((arg0 + 2528), 0)
    store16((arg0 + 2524), 0)
    store16((arg0 + 2520), 0)
    store16((arg0 + 2516), 0)
    store16((arg0 + 2512), 0)
    store16((arg0 + 2508), 0)
    store16((arg0 + 2504), 0)
    store16((arg0 + 2500), 0)
    store16((arg0 + 2496), 0)
    store16((arg0 + 2492), 0)
    store16((arg0 + 2488), 0)
    store16((arg0 + 2484), 0)
    store16((arg0 + 2480), 0)
    store16((arg0 + 2476), 0)
    store16((arg0 + 2472), 0)
    store16((arg0 + 2468), 0)
    store16((arg0 + 2464), 0)
    store16((arg0 + 2460), 0)
    store16((arg0 + 2456), 0)
    store16((arg0 + 2452), 0)
    store16((arg0 + 2448), 0)
    store16((arg0 + 2444), 0)
    store64(arg0 + 5804, 0)
    store16((arg0 + 1172), 1)
    store32(arg0 + 5800, 0)
    store32(arg0 + 5792, 0)

# ----------------------------------------------------------
# $func368
# ----------------------------------------------------------
def func368(arg0):
    v1 = load32(ENTITIES)
    func148(arg0, 9147392, 0)
    v3 = (v1 + (arg0 * 132))
    while True:  # $label0
        while True:  # $label3
            while True:  # $label2
                while True:  # $label1
                    v5 = load32(9147420)
                    # br_table (load32(9147420) - 2147483646)
                    break
                    break
                v2 = 2
                store8(v3 + 126, 2)
                v5 = 0
                break
                break
            v2 = load8u(v3 + 126)
            if (load8u(v3 + 126) != 2):
                break
            v2 = 0
            store8(v3 + 126, 0)
            v6 = load32(9215884)
            v7 = (v1 + (arg0 * 132))
            v4 = load32((v1 + (arg0 * 132)) + 44)
            if (load32((load32(9215884) + (load32((v1 + (arg0 * 132)) + 44) << 4)) + 4) != 51):
                break
            if v4:
                store32((v6 + (v4 << 4)), 0)
            store32(v7 + 44, 0)
            break
        while True:  # $label4
            v4 = (v1 + (arg0 * 132))
            if (v5 == load16u((v1 + (arg0 * 132)) + 110)):
                break
            if (load32(((load8u(v4 + 122) * 404) + ENTITY_TYPES) + 188) != 55):
                break
            func78(v3, v5, 1, 1)
            v2 = load8u((v1 + (arg0 * 132)) + 126)
            break
        if (v2 != 2):
            break
        arg0 = (v1 + (arg0 * 132))
        if (load32(((load8u((v1 + (arg0 * 132)) + 122) * 404) + ENTITY_TYPES) + 264) == 2):
            break
        break

# ----------------------------------------------------------
# $func369
# ----------------------------------------------------------
def func369(arg0):
    while True:  # $label0
        if not load32(9671176):
            break
        if load32(9671192):
            while True:  # $label1
                func38(load32((load32(9671184) + (v2 << 2))))
                v2 = (v2 + 1)
                if (u32((v2 + 1)) < u32(load32(9671192))):
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
    v2 = load32(9671176)
    while True:  # $label2
        v1 = load32(9671172)
        if (u32(load32(9671172)) > u32((v2 + 3))):
            v1 = load32(9671168)
            break
        v1 = ((v1 + load32(9671180)) + 3)
        store32(9671172, ((v1 + load32(9671180)) + 3))
        v3 = load32(9671168)
        v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
        if v2:
            # TODO: memory.copy
        if v3:
            v2 = load32(9671176)
        store32(9671168, v1)
        break
    store32(9671176, (v2 + 1))
    store32((v1 + (v2 << 2)), arg0)
    arg0 = load32(9671176)
    store32(9671176, (load32(9671176) + 1))
    store32((v1 + (arg0 << 2)), 0)
    arg0 = load32(9671176)
    store32(9671176, (load32(9671176) + 1))
    store32((v1 + (arg0 << 2)), 0)
    if not load8u(9147336):
        while True:  # $label3
            v4 = i32(load32(9142860))
            v4 = loadf32(40616)
            v6 = loadf32(9671164)
            v5 = (((i32(load32(9142860)) - ((v4 * loadf32(40616)) / loadf32(9671164))) * 0.5) + ((v4 * i32(load32(9681444))) + i32(load32(9142956))))
            if (abs((((i32(load32(9142860)) - ((v4 * loadf32(40616)) / loadf32(9671164))) * 0.5) + ((v4 * i32(load32(9681444))) + i32(load32(9142956))))) < 2147483650.0):
                break
            break
        arg0 = -2147483648
        while True:  # $label4
            v5 = i32(load32(9142856))
            v4 = (((v4 * i32(load32(9681440))) + i32(load32(9142952))) + ((i32(load32(9142856)) - ((v4 * v5) / v6)) * 0.5))
            if (abs((((v4 * i32(load32(9681440))) + i32(load32(9142952))) + ((i32(load32(9142856)) - ((v4 * v5) / v6)) * 0.5))) < 2147483650.0):
                break
            break
    return func132(-2147483648, arg0)

# ----------------------------------------------------------
# $func370
# ----------------------------------------------------------
def func370(arg0, arg1, arg2):
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if not (load8u(9568060) | load8u(9147152)):
            break
        if load8u(9142917):
            break
        while True:  # $label1
            v3 = load32(9299880)
            if load32(9299880):
                v3 = (v3 - 1)
                store32(9299880, (v3 - 1))
                v3 = load32((load32(9299872) + (v3 << 2)))
                break
            v3 = load32(9163776)
            v5 = (load32(9163776) + 1)
            store32(9163776, (load32(9163776) + 1))
            v6 = load32(9163784)
            if (u32(v5) < u32(load32(9163784))):
                break
            store32(v4, v6)
            a_b()
            store32(9163784, (load32(9163784) + 40000))
            break
        break
    G.global0 = (v4 + 16)
    return v3

# ----------------------------------------------------------
# $func371
# ----------------------------------------------------------
def func371(arg0):
    if (u32((load8s(load32(arg0)) - 48)) >= u32(10)):
        return 0
    while True:  # $label0
        v3 = load32(arg0)
        v1 = -1
        if (u32(v2) <= u32(214748364)):
            v1 = (load8s(v3) - 48)
            v2 = (v2 * 10)
            v1 = (-1 if (v1 > (v2 ^ 2147483647)) else ((load8s(v3) - 48) + (v2 * 10)))
        store32(arg0, (v3 + 1))
        v2 = v1
        if (u32((load8s(v3 + 1) - 48)) < u32(10)):
            continue
        break
    return v2

# ----------------------------------------------------------
# $func372
# ----------------------------------------------------------
def func372(arg0, arg1):
    while True:  # $label0
        v2 = load32(arg0 + 28)
        if (load32(arg0 + 28) <= 0):
            break
        v3 = load32(arg0 + 24)
        arg0 = 0
        while True:  # $label1
            v4 = load32((v3 + (arg0 << 2)))
            if (arg1 != load32(load32((v3 + (arg0 << 2))) + 28)):
                arg0 = (arg0 + 1)
                if (v2 != (arg0 + 1)):
                    continue
                break
            break
        return v4
        break
    return 0

# ----------------------------------------------------------
# $func373
# ----------------------------------------------------------
def func373(arg0, arg1, arg2):
    v6 = (arg0 + 1)
    v8 = load32(9147288)
    while True:  # $label8
        while True:  # $label1
            while True:  # $label0
                v3 = load32(9142440)
                v10 = (u32(load32(9142440)) <= u32(arg1))
                if (u32(load32(9142440)) <= u32(arg1)):
                    break
                if (u32(v3) <= u32(v6)):
                    break
                if ((arg1 | v6) < 0):
                    break
                v4 = load8s((v8 + ((arg1 * v3) + v6)))
                if (load8s((v8 + ((arg1 * v3) + v6))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            while True:  # $label2
                v5 = (arg1 - 1)
                v9 = (u32(v3) <= u32((arg1 - 1)))
                if (u32(v3) <= u32((arg1 - 1))):
                    break
                if (u32(v3) <= u32(v6)):
                    break
                if ((v5 | v6) < 0):
                    break
                v4 = load8s((v8 + ((v3 * v5) + v6)))
                if (load8s((v8 + ((v3 * v5) + v6))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            while True:  # $label3
                if v9:
                    break
                if (u32(arg0) >= u32(v3)):
                    break
                if ((arg0 | v5) < 0):
                    break
                v4 = load8s((v8 + ((v3 * v5) + arg0)))
                if (load8s((v8 + ((v3 * v5) + arg0))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            v7 = (arg0 - 1)
            while True:  # $label4
                if v9:
                    break
                if (u32(v3) <= u32(v7)):
                    break
                if ((v5 | v7) < 0):
                    break
                v4 = load8s((v8 + ((v3 * v5) + v7)))
                if (load8s((v8 + ((v3 * v5) + v7))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            while True:  # $label5
                if v10:
                    break
                if (u32(v3) <= u32(v7)):
                    break
                if ((arg1 | v7) < 0):
                    break
                v4 = load8s((v8 + ((arg1 * v3) + v7)))
                if (load8s((v8 + ((arg1 * v3) + v7))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            while True:  # $label6
                v5 = (arg1 + 1)
                v9 = (u32(v3) <= u32((arg1 + 1)))
                if (u32(v3) <= u32((arg1 + 1))):
                    break
                if (u32(v3) <= u32(v7)):
                    break
                if ((v5 | v7) < 0):
                    break
                v4 = load8s((v8 + ((v3 * v5) + v7)))
                if (load8s((v8 + ((v3 * v5) + v7))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            while True:  # $label7
                if v9:
                    break
                if (u32(arg0) >= u32(v3)):
                    break
                if ((arg0 | v5) < 0):
                    break
                v4 = load8s((v8 + ((v3 * v5) + arg0)))
                if (load8s((v8 + ((v3 * v5) + arg0))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            arg1 = -1
            if v9:
                break
            if (u32(v3) <= u32(v6)):
                break
            if ((v5 | v6) < 0):
                break
            v4 = load8s((v8 + ((v3 * v5) + v6)))
            if (load8s((v8 + ((v3 * v5) + v6))) < 0):
                break
            if (arg2 == v4):
                break
            break
        arg1 = v4
        break
    return arg1

# ----------------------------------------------------------
# $func374
# ----------------------------------------------------------
def func374(arg0, arg1):
    v2 = load32(PLAYERS)
    while True:  # $label4
        if not arg1:
            v5 = (v2 + (arg0 * 286704))
            while True:  # $label3
                while True:  # $label0
                    v2 = load32(((v5 + (v4 << 2)) + 284636))
                    if not load32(((v5 + (v4 << 2)) + 284636)):
                        break
                    arg0 = 0
                    arg1 = load32(v2 + 8)
                    if not load32(v2 + 8):
                        break
                    while True:  # $label2
                        while True:  # $label1
                            v3 = load32((load32(v2) + (arg0 << 2)))
                            if not load32((load32(v2) + (arg0 << 2))):
                                break
                            v3 = entities[v3]
                            if load32(entities[v3].action):
                                break
                            func118(v3)
                            arg1 = load32(v2 + 8)
                            break
                        arg0 = (arg0 + 1)
                        if (u32((arg0 + 1)) < u32(arg1)):
                            continue
                        break
                    break
                v4 = (v4 + 1)
                if ((v4 + 1) != 255):
                    continue
                break
            break
        v5 = (v2 + (arg0 * 286704))
        while True:  # $label8
            while True:  # $label5
                v2 = load32(((v5 + (v4 << 2)) + 284636))
                if not load32(((v5 + (v4 << 2)) + 284636)):
                    break
                arg0 = 0
                arg1 = load32(v2 + 8)
                if not load32(v2 + 8):
                    break
                while True:  # $label7
                    while True:  # $label6
                        v3 = load32((load32(v2) + (arg0 << 2)))
                        if not load32((load32(v2) + (arg0 << 2))):
                            break
                        v3 = entities[v3]
                        if load32(entities[v3].action):
                            break
                        func118(v3)
                        arg1 = load32(v2 + 8)
                        break
                    arg0 = (arg0 + 1)
                    if (u32((arg0 + 1)) < u32(arg1)):
                        continue
                    break
                break
            v4 = (v4 + 1)
            if ((v4 + 1) != 255):
                continue
            break
        break

# ----------------------------------------------------------
# $func375
# ----------------------------------------------------------
def func375(arg0, arg1):
    v3 = func244(load32(9142588))
    while True:  # $label0
        arg0 = load32(9142588)
        if not load32(9142588):
            break
        arg1 = load32(arg0 + 16)
        arg0 = load32(arg0 + 24)
        if (load32(arg0 + 24) >= 100):
            v4 = loadf32((((arg0 + arg1) << 2) + 32700))
            if not ((loadf32((((arg0 + arg1) << 2) + 32700)) < 4294967300.0) & (v4 >= 0.0)):
                break
            v2 = i32(v4)
            break
        v2 = ((arg1 * 1000) // arg0)
        break

# ----------------------------------------------------------
# $func376
# ----------------------------------------------------------
def func376(arg0, arg1):
    v3 = (load32(arg1 + 52) + load32(arg0 + 52))
    store32(arg1 + 52, (load32(arg1 + 52) + load32(arg0 + 52)))
    v4 = (load32(arg1 + 60) + load32(arg0 + 60))
    store32(arg1 + 60, (load32(arg1 + 60) + load32(arg0 + 60)))
    if load32(arg0 + 84):
        v2 = load32(arg1 + 84)
        v7 = load32(PLAYERS)
        while True:  # $label0
            store32(arg1 + 80, 0)
            v5 = (v2 + 1)
            store32(arg1 + 84, (v2 + 1))
            v2 = (v7 + (load16u(arg1 + 110) * 286704))
            v6 = ((v7 + (load16u(arg1 + 110) * 286704)) + 281672)
            store32(((v7 + (load16u(arg1 + 110) * 286704)) + 281672), (load32(v6) + 1))
            if (load32((v2 + 284388)) == v5):
                func201(arg1)
                store32(v2 + 283936, (load32(v2 + 283936) + 1))
                v3 = (v2 + 281636)
                store32((v2 + 281636), (load32(v3) + 1))
                v4 = load32(arg1 + 60)
                v7 = load32(PLAYERS)
                v3 = load32(arg1 + 52)
            v2 = (v2 + 284020)
            store32(arg1 + 64, (load32(arg1 + 64) + load32((v2 + 284020))))
            store32(arg1 + 68, (load32(arg1 + 68) + load32(v2)))
            v2 = load32(arg1 + 84)
            v5 = (v2 & 1)
            v6 = (load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 224) > 1)
            v4 = ((((load32(arg1 + 84) & 3) == 1) if (load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 224) > 1) else (v2 & 1)) + v4)
            store32(arg1 + 60, ((((load32(arg1 + 84) & 3) == 1) if (load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 224) > 1) else (v2 & 1)) + v4))
            v3 = ((v5 if v6 else 1) + v3)
            store32(arg1 + 52, ((v5 if v6 else 1) + v3))
            v8 = (v8 + 1)
            if (u32((v8 + 1)) < u32(load32(arg0 + 84))):
                continue
            break
    v2 = load32(arg1 + 72)
    while True:  # $label1
        v3 = load32(arg0 + 72)
        if not load32(arg0 + 72):
            break
        if v2:
            break
        v2 = load32(arg1 + 72)
        v3 = load32(arg0 + 72)
        break
    store32(arg1 + 72, (v2 + v3))
    store32(arg1 + 76, (load32(arg1 + 76) + load32(arg0 + 76)))
    arg0 = load32(arg0 + 80)
    store32(arg1 + 64, (load32(arg0 + 80) + load32(arg1 + 64)))
    store32(arg1 + 68, (arg0 + load32(arg1 + 68)))
    while True:  # $label2
        if not load32(arg1 + 92):
            break
        if load32(9140316):
            if (load32(9140320) != load32(arg1 + 28)):
                break
        break

# ----------------------------------------------------------
# $func377
# ----------------------------------------------------------
def func377(arg0, param1):
    arg0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v1 = load32(ENTITIES)
    v1 = entities[load32((load32(load32((v1 + (load32(9173808)]
    v2 = load32(entities[load32((load32(load32((v1 + (load32(9173808)].max_hp)
    store32(arg0 + 12, load32(entities[load32((load32(load32((v1 + (load32(9173808)].max_hp))
    while True:  # $label1
        while True:  # $label0
            v3 = load8u(v1 + 122)
            v4 = load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 172)
            if not load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 172):
                break
            if load32(9213812):
                break
            if load8u(9163793):
                if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 268)) > u32(1)):
                    break
                if load8u(9147210):
                    func41(39, (arg0 + 12), 1, 0, 0)
                    break
                v1 = func26(4)
                store32(func26(4), v2)
                break
            v2 = ((v4 * 132) + 9216080)
            store32(9142896, load32(v1 + 28))
            break
            break
        if load8u(9147210):
            func41(1, (arg0 + 12), 1, 0, 0)
            break
        v1 = func26(4)
        store32(func26(4), v2)
        break
    G.global0 = (arg0 + 16)

# ----------------------------------------------------------
# $func378
# ----------------------------------------------------------
def func378(arg0, arg1):
    func29(entities[arg0], 1)

# ----------------------------------------------------------
# $rc
# Export: rc
# ----------------------------------------------------------
def rc(arg0, arg1, arg2, arg3, param4, param5):
    """Export: rc"""
    v8 = (G.global0 - 40000)
    G.global0 = (G.global0 - 40000)
    while True:  # $label0
        if not load32(51776):
            store8(9215872, 1)
            func216(9216024, arg0, arg1, arg2, arg3)
            break
        arg1 = (arg1 == 2147483647)
        store32(9213812, (0 if (arg1 == 2147483647) else arg1))
        if arg2:
            v11 = ((arg2 * 132) + 9216080)
            if not load8u(((arg2 * 132) + 9216080) + 23):
                break
            v4 = load32(CURRENT_PLAYER)
            v6 = load32(PLAYERS)
            v5 = load32(9213808)
            if load32(9213808):
                # TODO: memory.copy
            store32(9213808, 0)
            while True:  # $label1
                v7 = load32((((v6 + (v4 * 286704)) + (arg3 << 2)) + 284636))
                if not load32((((v6 + (v4 * 286704)) + (arg3 << 2)) + 284636)):
                    break
                arg0 = load32(v7 + 8)
                if not load32(v7 + 8):
                    break
                arg1 = 0
                v9 = load32(ENTITIES)
                v10 = load32(v7)
                while True:  # $label4
                    if not load8u(9147152):
                        v6 = ((v6 + (v4 * 286704)) + 283908)
                        v12 = load32(9215884)
                        v13 = load32(PLAYER_COUNT)
                        v14 = load32(9143008)
                        arg3 = 0
                        while True:  # $label3
                            while True:  # $label2
                                v4 = load32((v10 + (arg1 << 2)))
                                if not load32((v10 + (arg1 << 2))):
                                    break
                                v4 = (v9 + (v4 * 132))
                                if not load8u((v14 + (load32(v6) + (v13 * load16u((v9 + (v4 * 132)) + 110))))):
                                    break
                                if (load32((v12 + (load32(v4 + 44) << 4)) + 4) == 20):
                                    break
                                if (load8u(v4 + 127) == 6):
                                    break
                                store32(((arg3 << 2) + 9173808), load32(v4 + 28))
                                arg3 = (arg3 + 1)
                                store32(9213808, (arg3 + 1))
                                arg0 = load32(v7 + 8)
                                break
                            arg1 = (arg1 + 1)
                            if (u32((arg1 + 1)) < u32(arg0)):
                                continue
                            break
                        break
                    arg3 = 0
                    while True:  # $label5
                        v4 = load32((v10 + (arg1 << 2)))
                        if load32((v10 + (arg1 << 2))):
                            store32(((arg3 << 2) + 9173808), load32((v9 + (v4 * 132)) + 28))
                            arg3 = (arg3 + 1)
                            store32(9213808, (arg3 + 1))
                            arg0 = load32(v7 + 8)
                        arg1 = (arg1 + 1)
                        if (u32((arg1 + 1)) < u32(arg0)):
                            continue
                        break
                    break
                if not arg3:
                    break
                arg0 = load32(v11)
                if (load32(v11) == 12):
                    store32(9213808, 0)
                break
            if v5:
                # TODO: memory.copy
            store32(9213808, v5)
            break
        while True:  # $label6
            arg2 = ((0 if arg1 else (load32(9143000) * load32(9147120))) + arg0)
            arg3 = load32(9671120)
            if (u32(((0 if arg1 else (load32(9143000) * load32(9147120))) + arg0)) >= u32(load32(9671120))):
                arg1 = load32(9681836)
                if not (load32(9681836) | load8u(9147141)):
                    break
                if (u32(arg0) < u32(arg3)):
                    break
                break
            arg1 = load32(9681836)
            break
        store32(9213816, arg0)
        if arg1:
            arg0 = (G.global0 - 16)
            G.global0 = (G.global0 - 16)
            func45()
            arg1 = load32(9143000)
            store32(9143000, 0)
            arg2 = (load32(9213816) + (arg1 * load32(9147120)))
            if (u32((load32(9213816) + (arg1 * load32(9147120)))) <= u32(load32(9681836))):
                while True:  # $label8
                    while True:  # $label9
                        while True:  # $label7
                            arg1 = load32(ENTITIES)
                            arg3 = load32((load32(9681828) + (arg2 << 2)))
                            arg2 = entities[load32((load32(9681828) + (arg2 << 2)))]
                            if (load32(((load8u(entities[load32((load32(9681828) + (arg2 << 2)))].sub_state) * 404) + ENTITY_TYPES) + 264) != 2):
                                break
                            v5 = load32(arg2 + 36)
                            if not load32(arg2 + 36):
                                break
                            arg1 = (arg1 + (v5 * 132))
                            func44((arg1 + (v5 * 132)), 0)
                            if load8u(9142917):
                                break
                            arg2 = load32(arg1 + 36)
                            arg1 = entities[(load32(arg1 + 36) if arg2 else load32(arg1 + 28))]
                            arg2 = load8u(entities[(load32(arg1 + 36) if arg2 else load32(arg1 + 28))].sub_state)
                            arg3 = (((load32(((load8u(entities[(load32(arg1 + 36) if arg2 else load32(arg1 + 28))].sub_state) * 404) + ENTITY_TYPES) + 220) << 4) & 2147483632) + (load16u(arg1 + 114) << 5))
                            break
                            break
                        func44(arg2, 0)
                        if load8u(9142917):
                            break
                        arg1 = (arg1 + (arg3 * 132))
                        arg2 = load32((arg1 + (arg3 * 132)) + 36)
                        arg1 = entities[(load32((arg1 + (arg3]
                        arg2 = load8u(entities[(load32((arg1 + (arg3].sub_state)
                        arg3 = (((load32(((load8u(entities[(load32((arg1 + (arg3].sub_state) * 404) + ENTITY_TYPES) + 220) << 4) & 2147483632) + (load16u(arg1 + 114) << 5))
                        break
                    arg1 = (arg1 + 112)
                    arg2 = load32(((arg2 * 404) + ENTITY_TYPES) + 216)
                    arg1 = load16u(arg1)
                    store32(arg0 + 4, arg3)
                    store32(arg0, (((arg2 << 4) & 2147483632) + (arg1 << 5)))
                    break
            G.global0 = (arg0 + 16)
            break
        if load8u(9147141):
            func377(func28(0, 0), arg1)
            break
        arg0 = load32(((arg2 << 2) + 9263072))
        if not load32(((arg2 << 2) + 9263072)):
            break
        arg1 = load32(arg0)
        while True:  # $label10
            if load8u(arg0 + 20):
                break
            while True:  # $label11
                if (arg1 != 5):
                    break
                if (load32(9213812) != 2):
                    break
                func242(load32(arg0 + 4))
                break
            break
        break
    G.global0 = (v8 + 40000)
    return call_table(arg1)

# ----------------------------------------------------------
# $func380
# ----------------------------------------------------------
def func380(arg0):
    while True:  # $label16
        while True:  # $label18
            while True:  # $label19
                while True:  # $label4
                    while True:  # $label5
                        while True:  # $label6
                            while True:  # $label7
                                while True:  # $label8
                                    while True:  # $label9
                                        while True:  # $label10
                                            while True:  # $label11
                                                while True:  # $label12
                                                    while True:  # $label13
                                                        while True:  # $label14
                                                            while True:  # $label15
                                                                while True:  # $label3
                                                                    while True:  # $label2
                                                                        while True:  # $label1
                                                                            while True:  # $label0
                                                                                # br_table load32(arg0)
                                                                                break
                                                                                break
                                                                            v10 = func165(arg0, 67)
                                                                            break
                                                                            break
                                                                        v10 = func165(arg0, 68)
                                                                        break
                                                                        break
                                                                    v10 = func165(arg0, 69)
                                                                    break
                                                                    break
                                                                while True:  # $label17
                                                                    # br_table load32(arg0 + 4)
                                                                    break
                                                                    break
                                                                v1 = load32(arg0 + 88)
                                                                if not load32(arg0 + 88):
                                                                    break
                                                                v7 = load32(9142420)
                                                                v9 = load32(ENTITIES)
                                                                v8 = load32(arg0 + 80)
                                                                v4 = load32(arg0 + 32)
                                                                v11 = not load32(arg0 + 32)
                                                                v12 = (load8u(arg0 + 45) != 0)
                                                                while True:  # $label24
                                                                    while True:  # $label23
                                                                        v5 = load32((v8 + (v2 << 2)))
                                                                        v16 = (v9 + (load32((v8 + (v2 << 2))) * 132))
                                                                        if ((load8u((v9 + (load32((v8 + (v2 << 2))) * 132)) + 125) == 3) != v12):
                                                                            v3 = load32(9140300)
                                                                            while True:  # $label21
                                                                                while True:  # $label20
                                                                                    if (u32(load32(9684388)) >= u32(2)):
                                                                                        v1 = 0
                                                                                        if not v3:
                                                                                            break
                                                                                        while True:  # $label22
                                                                                            if (load32(((v1 << 2) + 8451904)) == v5):
                                                                                                break
                                                                                            v1 = (v1 + 1)
                                                                                            if ((v1 + 1) != v3):
                                                                                                continue
                                                                                            break
                                                                                    v1 = v3
                                                                                    if (u32(v3) > u32(39999)):
                                                                                        break
                                                                                    break
                                                                                store32(9140300, (v1 + 1))
                                                                                store32(((v1 << 2) + 8451904), v5)
                                                                                break
                                                                            store32((v7 + (load16u(v16 + 110) << 2)), 1)
                                                                            v6 = (v6 | v11)
                                                                            v1 = load32(arg0 + 88)
                                                                            break
                                                                        if not v4:
                                                                            break
                                                                        break
                                                                        break
                                                                    v2 = (v2 + 1)
                                                                    if (u32((v2 + 1)) < u32(v1)):
                                                                        continue
                                                                    break
                                                                v10 = ((v4 != 0) | v6)
                                                                break
                                                                break
                                                            v4 = load32(PLAYER_COUNT)
                                                            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                                break
                                                            v7 = load32(PLAYERS)
                                                            v2 = load32(9142420)
                                                            v6 = load32(arg0 + 48)
                                                            v5 = load8u(arg0 + 45)
                                                            v1 = 1
                                                            while True:  # $label29
                                                                v3 = load32((v6 + (v4 << 2)))
                                                                while True:  # $label25
                                                                    while True:  # $label27
                                                                        while True:  # $label26
                                                                            arg0 = (v1 << 2)
                                                                            if not load32((v6 + (v1 << 2))):
                                                                                if not v3:
                                                                                    break
                                                                                if load32((arg0 + v2)):
                                                                                    break
                                                                                break
                                                                            if not v3:
                                                                                break
                                                                            break
                                                                        store32((arg0 + v2), 0)
                                                                        break
                                                                    while True:  # $label28
                                                                        v3 = (v7 + (v1 * 286704))
                                                                        v4 = (load32((v7 + (v1 * 286704)) + 283976) + 1)
                                                                        if (u32((load32((v7 + (v1 * 286704)) + 283976) + 1)) > u32((load32((v3 + 284136)) + load32(v3 + 283980)))):
                                                                            if not v5:
                                                                                break
                                                                            break
                                                                        if ((v5 != 0) == (u32(v4) > u32(load32((v3 + 284000))))):
                                                                            break
                                                                        break
                                                                    v10 = 1
                                                                    store32((arg0 + v2), 1)
                                                                    break
                                                                v1 = (v1 + 1)
                                                                v4 = load32(PLAYER_COUNT)
                                                                if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                                                                    continue
                                                                break
                                                            break
                                                            break
                                                        v4 = load32(PLAYER_COUNT)
                                                        if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                            break
                                                        v2 = load32(PLAYERS)
                                                        v3 = load32(9142420)
                                                        v7 = load32(arg0 + 48)
                                                        v9 = load8u(arg0 + 45)
                                                        v1 = 1
                                                        while True:  # $label39
                                                            v4 = load32((v7 + (v4 << 2)))
                                                            while True:  # $label30
                                                                while True:  # $label32
                                                                    while True:  # $label31
                                                                        v6 = (v1 << 2)
                                                                        if not load32((v7 + (v1 << 2))):
                                                                            if not v4:
                                                                                break
                                                                            if load32((v3 + v6)):
                                                                                break
                                                                            break
                                                                        if not v4:
                                                                            break
                                                                        break
                                                                    store32((v3 + v6), 0)
                                                                    break
                                                                v4 = load32(arg0 + 32)
                                                                v5 = load32(arg0 + 28)
                                                                while True:  # $label37
                                                                    while True:  # $label38
                                                                        while True:  # $label35
                                                                            while True:  # $label34
                                                                                while True:  # $label33
                                                                                    while True:  # $label36
                                                                                        # br_table load32(arg0 + 16)
                                                                                        break
                                                                                        break
                                                                                    if not v9:
                                                                                        break
                                                                                    break
                                                                                    break
                                                                                break
                                                                                break
                                                                            break
                                                                            break
                                                                        break
                                                                    if ((load32((((v2 + (v1 * 286704)) + (v5 << 2)) + 283984)) == v4) == (v9 != 0)):
                                                                        break
                                                                    break
                                                                v10 = 1
                                                                store32((v3 + v6), 1)
                                                                break
                                                            v1 = (v1 + 1)
                                                            v4 = load32(PLAYER_COUNT)
                                                            if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                                                                continue
                                                            break
                                                        break
                                                        break
                                                    while True:  # $label40
                                                        v2 = load32(PLAYER_COUNT)
                                                        if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                            break
                                                        v7 = load32(arg0 + 80)
                                                        v10 = load32(PLAYERS)
                                                        v3 = load32(9142420)
                                                        v4 = load32(arg0 + 48)
                                                        v1 = 1
                                                        if not load32(arg0 + 32):
                                                            while True:  # $label46
                                                                v2 = load32((v4 + (v2 << 2)))
                                                                while True:  # $label41
                                                                    while True:  # $label43
                                                                        while True:  # $label42
                                                                            v5 = (v1 << 2)
                                                                            if not load32((v4 + (v1 << 2))):
                                                                                if not v2:
                                                                                    break
                                                                                if load32((v3 + v5)):
                                                                                    break
                                                                                break
                                                                            if not v2:
                                                                                break
                                                                            break
                                                                        store32((v3 + v5), 0)
                                                                        break
                                                                    v9 = load32(arg0 + 88)
                                                                    if not load32(arg0 + 88):
                                                                        break
                                                                    v2 = 0
                                                                    v5 = (load32(9142420) + v5)
                                                                    v8 = load8u(arg0 + 45)
                                                                    while True:  # $label45
                                                                        while True:  # $label44
                                                                            v11 = (v2 << 2)
                                                                            if not load32((v7 + (v2 << 2))):
                                                                                break
                                                                            if ((load32((((v10 + (v1 * 286704)) + v11) + 281808)) != 0) == (v8 != 0)):
                                                                                break
                                                                            v6 = 1
                                                                            store32(v5, 1)
                                                                            break
                                                                            break
                                                                        v2 = (v2 + 1)
                                                                        if (u32((v2 + 1)) < u32(v9)):
                                                                            continue
                                                                        break
                                                                    break
                                                                v1 = (v1 + 1)
                                                                v2 = load32(PLAYER_COUNT)
                                                                if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                                                                    continue
                                                                break
                                                                break
                                                            raise Unreachable()
                                                        while True:  # $label52
                                                            v2 = load32((v4 + (v2 << 2)))
                                                            while True:  # $label47
                                                                while True:  # $label49
                                                                    while True:  # $label48
                                                                        v5 = (v1 << 2)
                                                                        if not load32((v4 + (v1 << 2))):
                                                                            if not v2:
                                                                                break
                                                                            if load32((v3 + v5)):
                                                                                break
                                                                            break
                                                                        if not v2:
                                                                            break
                                                                        break
                                                                    store32((v3 + v5), 0)
                                                                    break
                                                                v9 = load32(arg0 + 88)
                                                                if not load32(arg0 + 88):
                                                                    break
                                                                v2 = 0
                                                                v8 = (load32(9142420) + v5)
                                                                v11 = load8u(arg0 + 45)
                                                                while True:  # $label51
                                                                    while True:  # $label50
                                                                        v12 = (v2 << 2)
                                                                        if load32((v7 + (v2 << 2))):
                                                                            if ((load32((((v10 + (v1 * 286704)) + v12) + 281808)) != 0) == (v11 != 0)):
                                                                                break
                                                                            store32(v8, 1)
                                                                            v9 = load32(arg0 + 88)
                                                                            v6 = 1
                                                                        v2 = (v2 + 1)
                                                                        if (u32((v2 + 1)) < u32(v9)):
                                                                            continue
                                                                        break
                                                                        break
                                                                    break
                                                                v6 = 0
                                                                store32((v3 + v5), 0)
                                                                break
                                                            v1 = (v1 + 1)
                                                            v2 = load32(PLAYER_COUNT)
                                                            if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                                                                continue
                                                            break
                                                        break
                                                    v10 = v6
                                                    break
                                                    break
                                                v10 = func165(arg0, 70)
                                                break
                                                break
                                            while True:  # $label54
                                                while True:  # $label55
                                                    v2 = load32(arg0 + 4)
                                                    if (u32(load32(arg0 + 4)) <= u32(2)):
                                                        while True:  # $label53
                                                            # br_table v2
                                                            break
                                                            break
                                                        v1 = load32(arg0 + 88)
                                                        if not load32(arg0 + 88):
                                                            break
                                                        v12 = load32(9142420)
                                                        v16 = load32(ENTITIES)
                                                        v14 = load32(arg0 + 80)
                                                        v5 = load32(arg0 + 32)
                                                        v13 = not load32(arg0 + 32)
                                                        v9 = load8u(arg0 + 45)
                                                        v2 = 0
                                                        while True:  # $label67
                                                            while True:  # $label66
                                                                while True:  # $label57
                                                                    while True:  # $label56
                                                                        v8 = load32((v14 + (v2 << 2)))
                                                                        v11 = (v16 + (load32((v14 + (v2 << 2))) * 132))
                                                                        if (load8u((v16 + (load32((v14 + (v2 << 2))) * 132)) + 125) == 3):
                                                                            if v9:
                                                                                break
                                                                            break
                                                                        while True:  # $label58
                                                                            v3 = load32(v11 + 24)
                                                                            if load32(v11 + 24):
                                                                                v3 = load32(v3 + 12)
                                                                                if not load32(v3 + 12):
                                                                                    v7 = 0
                                                                                    v3 = load32(arg0 + 8)
                                                                                    v4 = (load32(arg0 + 8) if (u32(v3) < u32(16777216)) else 0)
                                                                                    break
                                                                                v3 = load32(v3)
                                                                                v7 = load32((load32(v3) + (load32(arg0 + 36) << 2)))
                                                                                v4 = load32(arg0 + 8)
                                                                                if (u32(load32(arg0 + 8)) < u32(16777216)):
                                                                                    break
                                                                                v4 = load32((((v4 << 2) + v3) - 67108864))
                                                                                break
                                                                            v7 = 0
                                                                            v3 = load32(arg0 + 8)
                                                                            v4 = (load32(arg0 + 8) if (u32(v3) <= u32(16777215)) else 0)
                                                                            break
                                                                        while True:  # $label62
                                                                            while True:  # $label61
                                                                                while True:  # $label60
                                                                                    while True:  # $label59
                                                                                        # br_table load32(arg0 + 28)
                                                                                        break
                                                                                        break
                                                                                    break
                                                                                    break
                                                                                break
                                                                                break
                                                                            break
                                                                        if ((v4 == v7) == (v9 != 0)):
                                                                            break
                                                                        break
                                                                    v3 = load32(9140300)
                                                                    while True:  # $label64
                                                                        while True:  # $label63
                                                                            if (u32(load32(9684388)) >= u32(2)):
                                                                                v1 = 0
                                                                                if not v3:
                                                                                    break
                                                                                while True:  # $label65
                                                                                    if (load32(((v1 << 2) + 8451904)) == v8):
                                                                                        break
                                                                                    v1 = (v1 + 1)
                                                                                    if ((v1 + 1) != v3):
                                                                                        continue
                                                                                    break
                                                                            v1 = v3
                                                                            if (u32(v3) > u32(39999)):
                                                                                break
                                                                            break
                                                                        store32(9140300, (v1 + 1))
                                                                        store32(((v1 << 2) + 8451904), v8)
                                                                        break
                                                                    store32((v12 + (load16u(v11 + 110) << 2)), 1)
                                                                    v6 = (v6 | v13)
                                                                    v1 = load32(arg0 + 88)
                                                                    break
                                                                    break
                                                                if not v5:
                                                                    break
                                                                break
                                                                break
                                                            v2 = (v2 + 1)
                                                            if (u32((v2 + 1)) < u32(v1)):
                                                                continue
                                                            break
                                                        v10 = ((v5 != 0) | v6)
                                                        break
                                                    v2 = load32(PLAYER_COUNT)
                                                    if (u32(load32(PLAYER_COUNT)) >= u32(2)):
                                                        v10 = load32(PLAYERS)
                                                        v6 = load32(9142420)
                                                        v7 = load32(arg0 + 48)
                                                        v9 = (load8u(arg0 + 45) != 0)
                                                        v1 = 1
                                                        while True:  # $label76
                                                            v2 = load32((v7 + (v2 << 2)))
                                                            while True:  # $label68
                                                                while True:  # $label70
                                                                    while True:  # $label69
                                                                        v4 = (v1 << 2)
                                                                        if not load32((v7 + (v1 << 2))):
                                                                            if not v2:
                                                                                break
                                                                            if load32((v4 + v6)):
                                                                                break
                                                                            break
                                                                        if not v2:
                                                                            break
                                                                        break
                                                                    store32((v4 + v6), 0)
                                                                    break
                                                                while True:  # $label71
                                                                    v2 = load32((v10 + (v1 * 286704)) + 286680)
                                                                    if not load32((v10 + (v1 * 286704)) + 286680):
                                                                        v3 = 0
                                                                        v2 = load32(arg0 + 8)
                                                                        v2 = (load32(arg0 + 8) if (u32(v2) <= u32(16777215)) else 0)
                                                                        break
                                                                    v8 = load32(v2)
                                                                    v3 = load32((load32(v2) + (load32(arg0 + 36) << 2)))
                                                                    v2 = load32(arg0 + 8)
                                                                    if (u32(load32(arg0 + 8)) < u32(16777216)):
                                                                        break
                                                                    v2 = load32((((v2 << 2) + v8) - 67108864))
                                                                    break
                                                                while True:  # $label75
                                                                    while True:  # $label74
                                                                        while True:  # $label73
                                                                            while True:  # $label72
                                                                                # br_table load32(arg0 + 28)
                                                                                break
                                                                                break
                                                                            break
                                                                            break
                                                                        break
                                                                        break
                                                                    break
                                                                if ((v2 == v3) == v9):
                                                                    break
                                                                v5 = 1
                                                                store32((v4 + v6), 1)
                                                                break
                                                            v1 = (v1 + 1)
                                                            v2 = load32(PLAYER_COUNT)
                                                            if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                                                                continue
                                                            break
                                                    v10 = v5
                                                    break
                                                    break
                                                v7 = load32(9140300)
                                                v5 = load32(arg0 + 32)
                                                store32(9140300, 0)
                                                if load32(PLAYER_COUNT):
                                                    v2 = load32(9142420)
                                                    while True:  # $label77
                                                        store32((v2 + (v1 << 2)), 0)
                                                        v1 = (v1 + 1)
                                                        if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                                                            continue
                                                        break
                                                if v7:
                                                    v8 = not v5
                                                    v11 = load32(9142420)
                                                    v12 = load32(ENTITIES)
                                                    v16 = (load8u(arg0 + 45) != 0)
                                                    v2 = 0
                                                    while True:  # $label87
                                                        while True:  # $label78
                                                            v9 = load32(((v2 << 2) + 8451904))
                                                            v14 = (v12 + (load32(((v2 << 2) + 8451904)) * 132))
                                                            v1 = load32((v12 + (load32(((v2 << 2) + 8451904)) * 132)) + 24)
                                                            if load32((v12 + (load32(((v2 << 2) + 8451904)) * 132)) + 24):
                                                                v1 = load32(v1 + 12)
                                                                if not load32(v1 + 12):
                                                                    v4 = 0
                                                                    v1 = load32(arg0 + 8)
                                                                    v1 = (load32(arg0 + 8) if (u32(v1) < u32(16777216)) else 0)
                                                                    break
                                                                v3 = load32(v1)
                                                                v4 = load32((load32(v1) + (load32(arg0 + 36) << 2)))
                                                                v1 = load32(arg0 + 8)
                                                                if (u32(load32(arg0 + 8)) < u32(16777216)):
                                                                    break
                                                                v1 = load32((((v1 << 2) + v3) - 67108864))
                                                                break
                                                            v4 = 0
                                                            v1 = load32(arg0 + 8)
                                                            v1 = (load32(arg0 + 8) if (u32(v1) <= u32(16777215)) else 0)
                                                            break
                                                        while True:  # $label86
                                                            while True:  # $label82
                                                                while True:  # $label81
                                                                    while True:  # $label80
                                                                        while True:  # $label79
                                                                            # br_table load32(arg0 + 28)
                                                                            break
                                                                            break
                                                                        break
                                                                        break
                                                                    break
                                                                    break
                                                                break
                                                            if ((v1 == v4) != v16):
                                                                v3 = load32(9140300)
                                                                while True:  # $label84
                                                                    while True:  # $label83
                                                                        if (u32(load32(9684388)) >= u32(2)):
                                                                            v1 = 0
                                                                            if not v3:
                                                                                break
                                                                            while True:  # $label85
                                                                                if (load32(((v1 << 2) + 8451904)) == v9):
                                                                                    break
                                                                                v1 = (v1 + 1)
                                                                                if ((v1 + 1) != v3):
                                                                                    continue
                                                                                break
                                                                        v1 = v3
                                                                        if (u32(v3) > u32(39999)):
                                                                            break
                                                                        break
                                                                    store32(9140300, (v1 + 1))
                                                                    store32(((v1 << 2) + 8451904), v9)
                                                                    break
                                                                store32((v11 + (load16u(v14 + 110) << 2)), 1)
                                                                v6 = (v6 | v8)
                                                                break
                                                            if not v5:
                                                                break
                                                            break
                                                            break
                                                        v2 = (v2 + 1)
                                                        if ((v2 + 1) != v7):
                                                            continue
                                                        break
                                                v10 = ((v5 != 0) | v6)
                                                break
                                                break
                                            v1 = load32(PLAYER_COUNT)
                                            if not load32(PLAYER_COUNT):
                                                break
                                            v12 = load32(PLAYERS)
                                            v8 = load32(9142420)
                                            v16 = load32(arg0 + 48)
                                            v2 = load32(arg0 + 32)
                                            v17 = (u32(load32(arg0 + 32)) > u32(3))
                                            v18 = (v2 - 1)
                                            v22 = ((v2 - 4) << 2)
                                            while True:  # $label122
                                                v2 = load32((v16 + (v1 << 2)))
                                                while True:  # $label88
                                                    while True:  # $label90
                                                        while True:  # $label89
                                                            v11 = (v9 << 2)
                                                            if not load32((v16 + (v9 << 2))):
                                                                if not v2:
                                                                    break
                                                                if load32((v8 + v11)):
                                                                    break
                                                                break
                                                            if not v2:
                                                                break
                                                            break
                                                        store32((v8 + v11), 0)
                                                        break
                                                    v6 = load32(9140300)
                                                    while True:  # $label121
                                                        while True:  # $label120
                                                            while True:  # $label119
                                                                while True:  # $label108
                                                                    while True:  # $label107
                                                                        if not v17:
                                                                            v5 = 0
                                                                            v19 = load32(9684388)
                                                                            v14 = load32(ENTITIES)
                                                                            v20 = load32(38764)
                                                                            v21 = load32(38456)
                                                                            v3 = 0
                                                                            v2 = v6
                                                                            while True:  # $label106
                                                                                while True:  # $label95
                                                                                    while True:  # $label94
                                                                                        while True:  # $label92
                                                                                            while True:  # $label93
                                                                                                while True:  # $label91
                                                                                                    # br_table v18
                                                                                                    break
                                                                                                    break
                                                                                                v1 = ((v3 * 404) + ENTITY_TYPES)
                                                                                                if load32(((v3 * 404) + ENTITY_TYPES) + 264):
                                                                                                    break
                                                                                                if (load32(v1 + 268) == 1):
                                                                                                    break
                                                                                                if not load32(v1 + 92):
                                                                                                    break
                                                                                                if (v3 == v21):
                                                                                                    break
                                                                                                if (v3 != v20):
                                                                                                    break
                                                                                                break
                                                                                                break
                                                                                            if (load32(((v3 * 404) + ENTITY_TYPES) + 264) == 1):
                                                                                                break
                                                                                            break
                                                                                            break
                                                                                        if load32(((v3 * 404) + ENTITY_TYPES) + 264):
                                                                                            break
                                                                                        break
                                                                                    v1 = load32((((v12 + (v9 * 286704)) + (v3 << 2)) + 284636))
                                                                                    if not load32((((v12 + (v9 * 286704)) + (v3 << 2)) + 284636)):
                                                                                        break
                                                                                    v23 = load32(v1 + 8)
                                                                                    if not load32(v1 + 8):
                                                                                        break
                                                                                    v13 = load8u(arg0 + 45)
                                                                                    v24 = load32(v1)
                                                                                    v4 = 0
                                                                                    while True:  # $label105
                                                                                        while True:  # $label96
                                                                                            v1 = load32((v24 + (v4 << 2)))
                                                                                            if not load32((v24 + (v4 << 2))):
                                                                                                break
                                                                                            while True:  # $label97
                                                                                                v15 = load32((v14 + (v1 * 132)) + 28)
                                                                                                v1 = (v14 + (load32((v14 + (v1 * 132)) + 28) * 132))
                                                                                                if (load8u((v14 + (load32((v14 + (v1 * 132)) + 28) * 132)) + 125) == 3):
                                                                                                    if v13:
                                                                                                        break
                                                                                                    break
                                                                                                while True:  # $label98
                                                                                                    v1 = load32(v1 + 24)
                                                                                                    if load32(v1 + 24):
                                                                                                        v1 = load32(v1 + 12)
                                                                                                        if not load32(v1 + 12):
                                                                                                            v7 = 0
                                                                                                            v1 = load32(arg0 + 8)
                                                                                                            v1 = (load32(arg0 + 8) if (u32(v1) < u32(16777216)) else 0)
                                                                                                            break
                                                                                                        v25 = load32(v1)
                                                                                                        v7 = load32((load32(v1) + (load32(arg0 + 36) << 2)))
                                                                                                        v1 = load32(arg0 + 8)
                                                                                                        if (u32(load32(arg0 + 8)) < u32(16777216)):
                                                                                                            break
                                                                                                        v1 = load32((((v1 << 2) + v25) - 67108864))
                                                                                                        break
                                                                                                    v7 = 0
                                                                                                    v1 = load32(arg0 + 8)
                                                                                                    v1 = (load32(arg0 + 8) if (u32(v1) <= u32(16777215)) else 0)
                                                                                                    break
                                                                                                while True:  # $label102
                                                                                                    while True:  # $label101
                                                                                                        while True:  # $label100
                                                                                                            while True:  # $label99
                                                                                                                # br_table load32(arg0 + 28)
                                                                                                                break
                                                                                                                break
                                                                                                            break
                                                                                                            break
                                                                                                        break
                                                                                                        break
                                                                                                    break
                                                                                                if ((v1 == v7) == (v13 != 0)):
                                                                                                    break
                                                                                                break
                                                                                            v5 = (v5 + 1)
                                                                                            while True:  # $label103
                                                                                                if (u32(v19) >= u32(2)):
                                                                                                    v1 = 0
                                                                                                    if not v2:
                                                                                                        break
                                                                                                    while True:  # $label104
                                                                                                        if (load32(((v1 << 2) + 8451904)) == v15):
                                                                                                            break
                                                                                                        v1 = (v1 + 1)
                                                                                                        if ((v1 + 1) != v2):
                                                                                                            continue
                                                                                                        break
                                                                                                v1 = v2
                                                                                                if (u32(v2) > u32(39999)):
                                                                                                    break
                                                                                                break
                                                                                            v2 = (v1 + 1)
                                                                                            store32(9140300, (v1 + 1))
                                                                                            store32(((v1 << 2) + 8451904), v15)
                                                                                            break
                                                                                        v4 = (v4 + 1)
                                                                                        if ((v4 + 1) != v23):
                                                                                            continue
                                                                                        break
                                                                                    break
                                                                                v3 = (v3 + 1)
                                                                                if ((v3 + 1) != 255):
                                                                                    continue
                                                                                break
                                                                            break
                                                                        v2 = load32((((v12 + (v9 * 286704)) + v22) + 284636))
                                                                        if not load32((((v12 + (v9 * 286704)) + v22) + 284636)):
                                                                            break
                                                                        v15 = load32(v2 + 8)
                                                                        if not load32(v2 + 8):
                                                                            break
                                                                        v4 = 0
                                                                        v19 = load32(9684388)
                                                                        v3 = load8u(arg0 + 45)
                                                                        v14 = load32(ENTITIES)
                                                                        v20 = load32(v2)
                                                                        v5 = 0
                                                                        v2 = v6
                                                                        while True:  # $label118
                                                                            while True:  # $label109
                                                                                v1 = load32((v20 + (v4 << 2)))
                                                                                if not load32((v20 + (v4 << 2))):
                                                                                    break
                                                                                while True:  # $label110
                                                                                    v13 = load32((v14 + (v1 * 132)) + 28)
                                                                                    v1 = (v14 + (load32((v14 + (v1 * 132)) + 28) * 132))
                                                                                    if (load8u((v14 + (load32((v14 + (v1 * 132)) + 28) * 132)) + 125) == 3):
                                                                                        if v3:
                                                                                            break
                                                                                        break
                                                                                    while True:  # $label111
                                                                                        v1 = load32(v1 + 24)
                                                                                        if load32(v1 + 24):
                                                                                            v1 = load32(v1 + 12)
                                                                                            if not load32(v1 + 12):
                                                                                                v7 = 0
                                                                                                v1 = load32(arg0 + 8)
                                                                                                v1 = (load32(arg0 + 8) if (u32(v1) < u32(16777216)) else 0)
                                                                                                break
                                                                                            v21 = load32(v1)
                                                                                            v7 = load32((load32(v1) + (load32(arg0 + 36) << 2)))
                                                                                            v1 = load32(arg0 + 8)
                                                                                            if (u32(load32(arg0 + 8)) < u32(16777216)):
                                                                                                break
                                                                                            v1 = load32((((v1 << 2) + v21) - 67108864))
                                                                                            break
                                                                                        v7 = 0
                                                                                        v1 = load32(arg0 + 8)
                                                                                        v1 = (load32(arg0 + 8) if (u32(v1) <= u32(16777215)) else 0)
                                                                                        break
                                                                                    while True:  # $label115
                                                                                        while True:  # $label114
                                                                                            while True:  # $label113
                                                                                                while True:  # $label112
                                                                                                    # br_table load32(arg0 + 28)
                                                                                                    break
                                                                                                    break
                                                                                                break
                                                                                                break
                                                                                            break
                                                                                            break
                                                                                        break
                                                                                    if ((v1 == v7) == (v3 != 0)):
                                                                                        break
                                                                                    break
                                                                                v5 = (v5 + 1)
                                                                                while True:  # $label116
                                                                                    if (u32(v19) >= u32(2)):
                                                                                        v1 = 0
                                                                                        if not v2:
                                                                                            break
                                                                                        while True:  # $label117
                                                                                            if (load32(((v1 << 2) + 8451904)) == v13):
                                                                                                break
                                                                                            v1 = (v1 + 1)
                                                                                            if ((v1 + 1) != v2):
                                                                                                continue
                                                                                            break
                                                                                    v1 = v2
                                                                                    if (u32(v2) > u32(39999)):
                                                                                        break
                                                                                    break
                                                                                v2 = (v1 + 1)
                                                                                store32(9140300, (v1 + 1))
                                                                                store32(((v1 << 2) + 8451904), v13)
                                                                                break
                                                                            v4 = (v4 + 1)
                                                                            if ((v4 + 1) != v15):
                                                                                continue
                                                                            break
                                                                        break
                                                                    v1 = load32(arg0 + 12)
                                                                    v4 = load32(arg0 + 16)
                                                                    if load32(arg0 + 16):
                                                                        break
                                                                    if (u32(v1) < u32(v5)):
                                                                        break
                                                                    break
                                                                    break
                                                                v1 = load32(arg0 + 12)
                                                                v4 = load32(arg0 + 16)
                                                                v5 = 0
                                                                break
                                                            if not v4:
                                                                break
                                                            if (u32(v1) <= u32(v5)):
                                                                break
                                                            break
                                                        v10 = 1
                                                        store32((v8 + v11), 1)
                                                        v1 = load32(arg0 + 12)
                                                        v4 = load32(arg0 + 16)
                                                        break
                                                    if not v4:
                                                        break
                                                    if (u32(v1) > u32(v5)):
                                                        break
                                                    store32(9140300, v6)
                                                    break
                                                v9 = (v9 + 1)
                                                v1 = load32(PLAYER_COUNT)
                                                if (u32((v9 + 1)) < u32(load32(PLAYER_COUNT))):
                                                    continue
                                                break
                                            break
                                            break
                                        while True:  # $label127
                                            while True:  # $label129
                                                while True:  # $label128
                                                    while True:  # $label125
                                                        while True:  # $label124
                                                            while True:  # $label123
                                                                # br_table load32(arg0 + 4)
                                                                break
                                                                break
                                                            v2 = 3
                                                            if (u32(load32(9671136)) > u32(3)):
                                                                while True:  # $label126
                                                                    if func233(v2, arg0):
                                                                        store32(9684384, (load32(9684384) + 1))
                                                                        v1 = 1
                                                                    v2 = (v2 + 1)
                                                                    if (u32((v2 + 1)) < u32(load32(9671136))):
                                                                        continue
                                                                    break
                                                            break
                                                            break
                                                        if load32(arg0 + 88):
                                                            break
                                                        break
                                                        break
                                                    if load32(9140300):
                                                        break
                                                    break
                                                    break
                                                while True:  # $label130
                                                    if func233(load32((load32(arg0 + 80) + (v2 << 2))), arg0):
                                                        store32(9684384, (load32(9684384) + 1))
                                                        v1 = 1
                                                    v2 = (v2 + 1)
                                                    if (u32((v2 + 1)) < u32(load32(arg0 + 88))):
                                                        continue
                                                    break
                                                break
                                                break
                                            while True:  # $label131
                                                if func233(load32(((v2 << 2) + 8451904)), arg0):
                                                    store32(9684384, (load32(9684384) + 1))
                                                    v1 = 1
                                                v2 = (v2 + 1)
                                                if (u32((v2 + 1)) < u32(load32(9140300))):
                                                    continue
                                                break
                                            break
                                        if load32(PLAYER_COUNT):
                                            v2 = load32(9142420)
                                            arg0 = 0
                                            while True:  # $label132
                                                v3 = (v2 + (arg0 << 2))
                                                store32((v2 + (arg0 << 2)), (load32(v3) == 2))
                                                arg0 = (arg0 + 1)
                                                if (u32((arg0 + 1)) < u32(load32(PLAYER_COUNT))):
                                                    continue
                                                break
                                        v10 = v1
                                        break
                                        break
                                    if not load8u(9147210):
                                        break
                                    v4 = load32(PLAYER_COUNT)
                                    if (u32(load32(PLAYER_COUNT)) >= u32(2)):
                                        v7 = load32(PLAYERS)
                                        v2 = load32(9142420)
                                        v3 = load32(arg0 + 48)
                                        v10 = not load8u(arg0 + 45)
                                        v1 = 1
                                        while True:  # $label136
                                            v6 = load32((v3 + (v4 << 2)))
                                            while True:  # $label133
                                                while True:  # $label135
                                                    while True:  # $label134
                                                        arg0 = (v1 << 2)
                                                        if not load32((v3 + (v1 << 2))):
                                                            if not v6:
                                                                break
                                                            if load32((arg0 + v2)):
                                                                break
                                                            break
                                                        if not v6:
                                                            break
                                                        break
                                                    store32((arg0 + v2), 0)
                                                    break
                                                v6 = (v7 + (v1 * 286704))
                                                if (v10 == ((load32((v7 + (v1 * 286704)) + 284616) | load32(v6 + 284628)) != 0)):
                                                    break
                                                v5 = 1
                                                store32((arg0 + v2), 1)
                                                break
                                            v1 = (v1 + 1)
                                            v4 = load32(PLAYER_COUNT)
                                            if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                                                continue
                                            break
                                    v10 = (v5 & 1)
                                    break
                                    break
                                v2 = (load32(9142848) * 25)
                                v1 = load32(arg0 + 12)
                                v10 = ((load8u(arg0 + 45) != 0) ^ ((u32((load32(9142848) * 25)) < u32(load32(arg0 + 12))) if load32(arg0 + 16) else (u32(v1) < u32(v2))))
                                break
                                break
                            v4 = load32(PLAYER_COUNT)
                            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                break
                            v5 = load32(PLAYERS)
                            v2 = load32(9142420)
                            v3 = load32(arg0 + 48)
                            v7 = load8u(arg0 + 45)
                            v1 = 1
                            while True:  # $label140
                                v6 = load32((v3 + (v4 << 2)))
                                while True:  # $label137
                                    while True:  # $label139
                                        while True:  # $label138
                                            arg0 = (v1 << 2)
                                            if not load32((v3 + (v1 << 2))):
                                                if not v6:
                                                    break
                                                if load32((arg0 + v2)):
                                                    break
                                                break
                                            if not v6:
                                                break
                                            break
                                        store32((arg0 + v2), 0)
                                        break
                                    v6 = load8u((v5 + (v1 * 286704)) + 286696)
                                    if ((not load8u((v5 + (v1 * 286704)) + 286696) if v7 else (v6 != 0)) != 1):
                                        break
                                    v10 = 1
                                    store32((arg0 + v2), 1)
                                    break
                                v1 = (v1 + 1)
                                v4 = load32(PLAYER_COUNT)
                                if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                                    continue
                                break
                            break
                            break
                        v4 = load32(PLAYER_COUNT)
                        if (u32(load32(PLAYER_COUNT)) < u32(2)):
                            break
                        v5 = load32(PLAYERS)
                        v2 = load32(9142420)
                        v3 = load32(arg0 + 48)
                        v7 = load8u(arg0 + 45)
                        v1 = 1
                        while True:  # $label144
                            v6 = load32((v3 + (v4 << 2)))
                            while True:  # $label141
                                while True:  # $label143
                                    while True:  # $label142
                                        arg0 = (v1 << 2)
                                        if not load32((v3 + (v1 << 2))):
                                            if not v6:
                                                break
                                            if load32((arg0 + v2)):
                                                break
                                            break
                                        if not v6:
                                            break
                                        break
                                    store32((arg0 + v2), 0)
                                    break
                                v6 = load8u((v5 + (v1 * 286704)) + 286697)
                                if ((not load8u((v5 + (v1 * 286704)) + 286697) if v7 else (v6 != 0)) != 1):
                                    break
                                v10 = 1
                                store32((arg0 + v2), 1)
                                break
                            v1 = (v1 + 1)
                            v4 = load32(PLAYER_COUNT)
                            if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                                continue
                            break
                        break
                        break
                    v2 = load32(PLAYER_COUNT)
                    if (u32(load32(PLAYER_COUNT)) >= u32(2)):
                        v3 = load32(arg0 + 80)
                        v6 = load32(PLAYERS)
                        v4 = load32(9142420)
                        v10 = load32(arg0 + 48)
                        v9 = load8u(arg0 + 45)
                        v1 = 1
                        while True:  # $label154
                            v2 = load32((v10 + (v2 << 2)))
                            while True:  # $label145
                                while True:  # $label147
                                    while True:  # $label146
                                        v5 = (v1 << 2)
                                        if not load32((v10 + (v1 << 2))):
                                            if not v2:
                                                break
                                            if load32((v4 + v5)):
                                                break
                                            break
                                        if not v2:
                                            break
                                        break
                                    store32((v4 + v5), 0)
                                    break
                                while True:  # $label152
                                    while True:  # $label153
                                        while True:  # $label150
                                            while True:  # $label149
                                                while True:  # $label148
                                                    while True:  # $label151
                                                        # br_table load32(arg0 + 16)
                                                        break
                                                        break
                                                    if not v9:
                                                        break
                                                    break
                                                    break
                                                v2 = 1
                                                v8 = load32(v3)
                                                if (load32(v3) != -2147483647):
                                                    v2 = (load32((v6 + (v1 * 286704)) + 283848) >= v8)
                                                v8 = load32(v3 + 4)
                                                if (load32(v3 + 4) != -2147483647):
                                                    v2 = ((load32(((v6 + (v1 * 286704)) + 283852)) >= v8) & v2)
                                                v8 = load32(v3 + 8)
                                                if (load32(v3 + 8) != -2147483647):
                                                    v2 = ((load32(((v6 + (v1 * 286704)) + 283856)) >= v8) & v2)
                                                v8 = load32(v3 + 12)
                                                if (load32(v3 + 12) == -2147483647):
                                                    break
                                                v2 = ((load32(((v6 + (v1 * 286704)) + 283860)) >= v8) & v2)
                                                break
                                                break
                                            v2 = 1
                                            v8 = load32(v3)
                                            if (load32(v3) != -2147483647):
                                                v2 = (load32((v6 + (v1 * 286704)) + 283848) <= v8)
                                            v8 = load32(v3 + 4)
                                            if (load32(v3 + 4) != -2147483647):
                                                v2 = ((load32(((v6 + (v1 * 286704)) + 283852)) <= v8) & v2)
                                            v8 = load32(v3 + 8)
                                            if (load32(v3 + 8) != -2147483647):
                                                v2 = ((load32(((v6 + (v1 * 286704)) + 283856)) <= v8) & v2)
                                            v8 = load32(v3 + 12)
                                            if (load32(v3 + 12) == -2147483647):
                                                break
                                            v2 = ((load32(((v6 + (v1 * 286704)) + 283860)) <= v8) & v2)
                                            break
                                            break
                                        v2 = 1
                                        v8 = load32(v3)
                                        if (load32(v3) != -2147483647):
                                            v2 = (load32((v6 + (v1 * 286704)) + 283848) == v8)
                                        v8 = load32(v3 + 4)
                                        if (load32(v3 + 4) != -2147483647):
                                            v2 = ((load32(((v6 + (v1 * 286704)) + 283852)) == v8) & v2)
                                        v8 = load32(v3 + 8)
                                        if (load32(v3 + 8) != -2147483647):
                                            v2 = ((load32(((v6 + (v1 * 286704)) + 283856)) == v8) & v2)
                                        v8 = load32(v3 + 12)
                                        if (load32(v3 + 12) == -2147483647):
                                            break
                                        v2 = ((load32(((v6 + (v1 * 286704)) + 283860)) == v8) & v2)
                                        break
                                    if (v2 == (v9 != 0)):
                                        break
                                    break
                                v7 = 1
                                store32((v4 + v5), 1)
                                break
                            v1 = (v1 + 1)
                            v2 = load32(PLAYER_COUNT)
                            if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                                continue
                            break
                    v10 = v7
                    break
                    break
                while True:  # $label156
                    while True:  # $label157
                        while True:  # $label155
                            # br_table load32(arg0 + 4)
                            break
                            break
                        v4 = load32(arg0 + 88)
                        if not load32(arg0 + 88):
                            break
                        v9 = load32(9142420)
                        v8 = load32(ENTITIES)
                        v11 = load32(arg0 + 80)
                        v5 = load32(arg0 + 32)
                        v12 = not load32(arg0 + 32)
                        v16 = (load8u(arg0 + 45) != 0)
                        while True:  # $label162
                            while True:  # $label161
                                v7 = load32((v11 + (v2 << 2)))
                                v14 = (v8 + (load32((v11 + (v2 << 2))) * 132))
                                v1 = load8u((v8 + (load32((v11 + (v2 << 2))) * 132)) + 125)
                                if (((load8u((v8 + (load32((v11 + (v2 << 2))) * 132)) + 125) != 3) & (v1 != 14)) != v16):
                                    v3 = load32(9140300)
                                    while True:  # $label159
                                        while True:  # $label158
                                            if (u32(load32(9684388)) >= u32(2)):
                                                v1 = 0
                                                if not v3:
                                                    break
                                                while True:  # $label160
                                                    if (load32(((v1 << 2) + 8451904)) == v7):
                                                        break
                                                    v1 = (v1 + 1)
                                                    if ((v1 + 1) != v3):
                                                        continue
                                                    break
                                            v1 = v3
                                            if (u32(v3) > u32(39999)):
                                                break
                                            break
                                        store32(9140300, (v1 + 1))
                                        store32(((v1 << 2) + 8451904), v7)
                                        break
                                    store32((v9 + (load16u(v14 + 110) << 2)), 1)
                                    v6 = (v6 | v12)
                                    v4 = load32(arg0 + 88)
                                    break
                                if not v5:
                                    break
                                break
                                break
                            v2 = (v2 + 1)
                            if (u32((v2 + 1)) < u32(v4)):
                                continue
                            break
                        v10 = ((v5 != 0) | v6)
                        break
                        break
                    v4 = load32(9140300)
                    v3 = load32(arg0 + 32)
                    store32(9140300, 0)
                    if load32(PLAYER_COUNT):
                        v2 = load32(9142420)
                        while True:  # $label163
                            store32((v2 + (v1 << 2)), 0)
                            v1 = (v1 + 1)
                            if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                                continue
                            break
                    if v4:
                        v7 = not v3
                        v9 = load32(9142420)
                        v8 = load32(ENTITIES)
                        v11 = (load8u(arg0 + 45) != 0)
                        v2 = 0
                        while True:  # $label168
                            while True:  # $label167
                                v5 = load32(((v2 << 2) + 8451904))
                                v12 = (v8 + (load32(((v2 << 2) + 8451904)) * 132))
                                arg0 = load8u((v8 + (load32(((v2 << 2) + 8451904)) * 132)) + 125)
                                if (((load8u((v8 + (load32(((v2 << 2) + 8451904)) * 132)) + 125) != 3) & (arg0 != 14)) != v11):
                                    arg0 = load32(9140300)
                                    while True:  # $label165
                                        while True:  # $label164
                                            if (u32(load32(9684388)) >= u32(2)):
                                                v1 = 0
                                                if not arg0:
                                                    break
                                                while True:  # $label166
                                                    if (load32(((v1 << 2) + 8451904)) == v5):
                                                        break
                                                    v1 = (v1 + 1)
                                                    if ((v1 + 1) != arg0):
                                                        continue
                                                    break
                                            v1 = arg0
                                            if (u32(arg0) > u32(39999)):
                                                break
                                            break
                                        store32(9140300, (v1 + 1))
                                        store32(((v1 << 2) + 8451904), v5)
                                        break
                                    store32((v9 + (load16u(v12 + 110) << 2)), 1)
                                    v6 = (v6 | v7)
                                    break
                                if not v3:
                                    break
                                break
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v4):
                                continue
                            break
                    v10 = ((v3 != 0) | v6)
                    break
                    break
                v1 = load32(PLAYER_COUNT)
                if not load32(PLAYER_COUNT):
                    break
                v16 = load32(PLAYERS)
                v11 = load32(9142420)
                v14 = load32(arg0 + 48)
                v2 = load32(arg0 + 32)
                v22 = (u32(load32(arg0 + 32)) > u32(3))
                v19 = (v2 - 1)
                v20 = ((v2 - 4) << 2)
                while True:  # $label192
                    v2 = load32((v14 + (v1 << 2)))
                    while True:  # $label169
                        while True:  # $label171
                            while True:  # $label170
                                v12 = (v9 << 2)
                                if not load32((v14 + (v9 << 2))):
                                    if not v2:
                                        break
                                    if load32((v11 + v12)):
                                        break
                                    break
                                if not v2:
                                    break
                                break
                            store32((v11 + v12), 0)
                            break
                        v6 = load32(9140300)
                        while True:  # $label191
                            while True:  # $label190
                                while True:  # $label189
                                    while True:  # $label184
                                        while True:  # $label183
                                            if not v22:
                                                v5 = 0
                                                v8 = load32(ENTITIES)
                                                v21 = load32(38764)
                                                v23 = load32(38456)
                                                v24 = load32(9684388)
                                                v7 = 0
                                                v3 = v6
                                                while True:  # $label182
                                                    while True:  # $label176
                                                        while True:  # $label175
                                                            while True:  # $label173
                                                                while True:  # $label174
                                                                    while True:  # $label172
                                                                        # br_table v19
                                                                        break
                                                                        break
                                                                    v2 = ((v7 * 404) + ENTITY_TYPES)
                                                                    if load32(((v7 * 404) + ENTITY_TYPES) + 264):
                                                                        break
                                                                    if (load32(v2 + 268) == 1):
                                                                        break
                                                                    if not load32(v2 + 92):
                                                                        break
                                                                    if (v7 == v23):
                                                                        break
                                                                    if (v7 != v21):
                                                                        break
                                                                    break
                                                                    break
                                                                if (load32(((v7 * 404) + ENTITY_TYPES) + 264) == 1):
                                                                    break
                                                                break
                                                                break
                                                            if load32(((v7 * 404) + ENTITY_TYPES) + 264):
                                                                break
                                                            break
                                                        v2 = load32((((v16 + (v9 * 286704)) + (v7 << 2)) + 284636))
                                                        if not load32((((v16 + (v9 * 286704)) + (v7 << 2)) + 284636)):
                                                            break
                                                        v13 = load32(v2 + 8)
                                                        if not load32(v2 + 8):
                                                            break
                                                        v15 = load8u(arg0 + 45)
                                                        v17 = load32(v2)
                                                        v4 = 0
                                                        v2 = v3
                                                        if (u32(v24) >= u32(2)):
                                                            while True:  # $label179
                                                                while True:  # $label177
                                                                    v1 = load32((v17 + (v4 << 2)))
                                                                    if not load32((v17 + (v4 << 2))):
                                                                        break
                                                                    v18 = load32((v8 + (v1 * 132)) + 28)
                                                                    v1 = load8u((v8 + (load32((v8 + (v1 * 132)) + 28) * 132)) + 125)
                                                                    if (((load8u((v8 + (load32((v8 + (v1 * 132)) + 28) * 132)) + 125) != 3) & (v1 != 14)) == (v15 != 0)):
                                                                        break
                                                                    v5 = (v5 + 1)
                                                                    v1 = 0
                                                                    if v2:
                                                                        while True:  # $label178
                                                                            if (load32(((v1 << 2) + 8451904)) == v18):
                                                                                break
                                                                            v1 = (v1 + 1)
                                                                            if ((v1 + 1) != v2):
                                                                                continue
                                                                            break
                                                                        if (u32(v2) >= u32(40000)):
                                                                            break
                                                                    v3 = (v2 + 1)
                                                                    store32(9140300, (v2 + 1))
                                                                    store32(((v2 << 2) + 8451904), v18)
                                                                    v2 = v3
                                                                    break
                                                                v4 = (v4 + 1)
                                                                if ((v4 + 1) != v13):
                                                                    continue
                                                                break
                                                                break
                                                            raise Unreachable()
                                                        while True:  # $label181
                                                            while True:  # $label180
                                                                v1 = load32((v17 + (v4 << 2)))
                                                                if not load32((v17 + (v4 << 2))):
                                                                    break
                                                                v1 = load32((v8 + (v1 * 132)) + 28)
                                                                v18 = load8u((v8 + (load32((v8 + (v1 * 132)) + 28) * 132)) + 125)
                                                                if (((load8u((v8 + (load32((v8 + (v1 * 132)) + 28) * 132)) + 125) != 3) & (v18 != 14)) == (v15 != 0)):
                                                                    break
                                                                v5 = (v5 + 1)
                                                                if (u32(v2) > u32(39999)):
                                                                    break
                                                                v3 = (v2 + 1)
                                                                store32(9140300, (v2 + 1))
                                                                store32(((v2 << 2) + 8451904), v1)
                                                                v2 = v3
                                                                break
                                                            v4 = (v4 + 1)
                                                            if ((v4 + 1) != v13):
                                                                continue
                                                            break
                                                        break
                                                    v7 = (v7 + 1)
                                                    if ((v7 + 1) != 255):
                                                        continue
                                                    break
                                                break
                                            v2 = load32((((v16 + (v9 * 286704)) + v20) + 284636))
                                            if not load32((((v16 + (v9 * 286704)) + v20) + 284636)):
                                                break
                                            v8 = load32(v2 + 8)
                                            if not load32(v2 + 8):
                                                break
                                            v4 = 0
                                            v13 = load32(9684388)
                                            v15 = load8u(arg0 + 45)
                                            v3 = load32(ENTITIES)
                                            v17 = load32(v2)
                                            v5 = 0
                                            v2 = v6
                                            while True:  # $label188
                                                while True:  # $label185
                                                    v1 = load32((v17 + (v4 << 2)))
                                                    if not load32((v17 + (v4 << 2))):
                                                        break
                                                    v7 = load32((v3 + (v1 * 132)) + 28)
                                                    v1 = load8u((v3 + (load32((v3 + (v1 * 132)) + 28) * 132)) + 125)
                                                    if (((load8u((v3 + (load32((v3 + (v1 * 132)) + 28) * 132)) + 125) != 3) & (v1 != 14)) == (v15 != 0)):
                                                        break
                                                    v5 = (v5 + 1)
                                                    while True:  # $label186
                                                        if (u32(v13) >= u32(2)):
                                                            v1 = 0
                                                            if not v2:
                                                                break
                                                            while True:  # $label187
                                                                if (load32(((v1 << 2) + 8451904)) == v7):
                                                                    break
                                                                v1 = (v1 + 1)
                                                                if ((v1 + 1) != v2):
                                                                    continue
                                                                break
                                                        v1 = v2
                                                        if (u32(v2) > u32(39999)):
                                                            break
                                                        break
                                                    v2 = (v1 + 1)
                                                    store32(9140300, (v1 + 1))
                                                    store32(((v1 << 2) + 8451904), v7)
                                                    break
                                                v4 = (v4 + 1)
                                                if ((v4 + 1) != v8):
                                                    continue
                                                break
                                            break
                                        v1 = load32(arg0 + 12)
                                        v4 = load32(arg0 + 16)
                                        if load32(arg0 + 16):
                                            break
                                        if (u32(v1) < u32(v5)):
                                            break
                                        break
                                        break
                                    v1 = load32(arg0 + 12)
                                    v4 = load32(arg0 + 16)
                                    v5 = 0
                                    break
                                if not v4:
                                    break
                                if (u32(v1) <= u32(v5)):
                                    break
                                break
                            v10 = 1
                            store32((v11 + v12), 1)
                            v1 = load32(arg0 + 12)
                            v4 = load32(arg0 + 16)
                            break
                        if not v4:
                            break
                        if (u32(v1) > u32(v5)):
                            break
                        store32(9140300, v6)
                        break
                    v9 = (v9 + 1)
                    v1 = load32(PLAYER_COUNT)
                    if (u32((v9 + 1)) < u32(load32(PLAYER_COUNT))):
                        continue
                    break
                break
                break
            v4 = load32(9140300)
            v3 = load32(arg0 + 32)
            store32(9140300, 0)
            if load32(PLAYER_COUNT):
                v2 = load32(9142420)
                while True:  # $label193
                    store32((v2 + (v1 << 2)), 0)
                    v1 = (v1 + 1)
                    if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                        continue
                    break
            if v4:
                v7 = not v3
                v9 = load32(9142420)
                v8 = load32(ENTITIES)
                v11 = (load8u(arg0 + 45) != 0)
                v2 = 0
                while True:  # $label198
                    while True:  # $label197
                        v5 = load32(((v2 << 2) + 8451904))
                        v12 = (v8 + (load32(((v2 << 2) + 8451904)) * 132))
                        if ((load8u((v8 + (load32(((v2 << 2) + 8451904)) * 132)) + 125) == 3) != v11):
                            arg0 = load32(9140300)
                            while True:  # $label195
                                while True:  # $label194
                                    if (u32(load32(9684388)) >= u32(2)):
                                        v1 = 0
                                        if not arg0:
                                            break
                                        while True:  # $label196
                                            if (load32(((v1 << 2) + 8451904)) == v5):
                                                break
                                            v1 = (v1 + 1)
                                            if ((v1 + 1) != arg0):
                                                continue
                                            break
                                    v1 = arg0
                                    if (u32(arg0) > u32(39999)):
                                        break
                                    break
                                store32(9140300, (v1 + 1))
                                store32(((v1 << 2) + 8451904), v5)
                                break
                            store32((v9 + (load16u(v12 + 110) << 2)), 1)
                            v6 = (v6 | v7)
                            break
                        if not v3:
                            break
                        break
                        break
                    v2 = (v2 + 1)
                    if ((v2 + 1) != v4):
                        continue
                    break
            v10 = ((v3 != 0) | v6)
            break
            break
        v1 = load32(PLAYER_COUNT)
        if not load32(PLAYER_COUNT):
            break
        v16 = load32(PLAYERS)
        v11 = load32(9142420)
        v14 = load32(arg0 + 48)
        v2 = load32(arg0 + 32)
        v22 = (u32(load32(arg0 + 32)) > u32(3))
        v19 = (v2 - 1)
        v20 = ((v2 - 4) << 2)
        while True:  # $label223
            v2 = load32((v14 + (v1 << 2)))
            while True:  # $label199
                while True:  # $label201
                    while True:  # $label200
                        v12 = (v9 << 2)
                        if not load32((v14 + (v9 << 2))):
                            if not v2:
                                break
                            if load32((v11 + v12)):
                                break
                            break
                        if not v2:
                            break
                        break
                    store32((v11 + v12), 0)
                    break
                v6 = load32(9140300)
                while True:  # $label222
                    while True:  # $label221
                        while True:  # $label220
                            while True:  # $label214
                                while True:  # $label213
                                    if not v22:
                                        v5 = 0
                                        v8 = load32(ENTITIES)
                                        v21 = load32(38764)
                                        v23 = load32(38456)
                                        v24 = load32(9684388)
                                        v7 = 0
                                        v3 = v6
                                        while True:  # $label212
                                            while True:  # $label206
                                                while True:  # $label205
                                                    while True:  # $label203
                                                        while True:  # $label204
                                                            while True:  # $label202
                                                                # br_table v19
                                                                break
                                                                break
                                                            v2 = ((v7 * 404) + ENTITY_TYPES)
                                                            if load32(((v7 * 404) + ENTITY_TYPES) + 264):
                                                                break
                                                            if (load32(v2 + 268) == 1):
                                                                break
                                                            if not load32(v2 + 92):
                                                                break
                                                            if (v7 == v23):
                                                                break
                                                            if (v7 != v21):
                                                                break
                                                            break
                                                            break
                                                        if (load32(((v7 * 404) + ENTITY_TYPES) + 264) == 1):
                                                            break
                                                        break
                                                        break
                                                    if load32(((v7 * 404) + ENTITY_TYPES) + 264):
                                                        break
                                                    break
                                                v2 = load32((((v16 + (v9 * 286704)) + (v7 << 2)) + 285656))
                                                if not load32((((v16 + (v9 * 286704)) + (v7 << 2)) + 285656)):
                                                    break
                                                v13 = load32(v2 + 8)
                                                if not load32(v2 + 8):
                                                    break
                                                v15 = load8u(arg0 + 45)
                                                v17 = load32(v2)
                                                v4 = 0
                                                v2 = v3
                                                if (u32(v24) >= u32(2)):
                                                    while True:  # $label209
                                                        while True:  # $label207
                                                            v1 = load32((v17 + (v4 << 2)))
                                                            if not load32((v17 + (v4 << 2))):
                                                                break
                                                            v18 = load32((v8 + (v1 * 132)) + 28)
                                                            if ((load8u((v8 + (load32((v8 + (v1 * 132)) + 28) * 132)) + 125) == 3) == (v15 != 0)):
                                                                break
                                                            v5 = (v5 + 1)
                                                            v1 = 0
                                                            if v2:
                                                                while True:  # $label208
                                                                    if (load32(((v1 << 2) + 8451904)) == v18):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if ((v1 + 1) != v2):
                                                                        continue
                                                                    break
                                                                if (u32(v2) >= u32(40000)):
                                                                    break
                                                            v3 = (v2 + 1)
                                                            store32(9140300, (v2 + 1))
                                                            store32(((v2 << 2) + 8451904), v18)
                                                            v2 = v3
                                                            break
                                                        v4 = (v4 + 1)
                                                        if ((v4 + 1) != v13):
                                                            continue
                                                        break
                                                        break
                                                    raise Unreachable()
                                                while True:  # $label211
                                                    while True:  # $label210
                                                        v1 = load32((v17 + (v4 << 2)))
                                                        if not load32((v17 + (v4 << 2))):
                                                            break
                                                        v1 = load32((v8 + (v1 * 132)) + 28)
                                                        if ((load8u((v8 + (load32((v8 + (v1 * 132)) + 28) * 132)) + 125) == 3) == (v15 != 0)):
                                                            break
                                                        v5 = (v5 + 1)
                                                        if (u32(v2) > u32(39999)):
                                                            break
                                                        v3 = (v2 + 1)
                                                        store32(9140300, (v2 + 1))
                                                        store32(((v2 << 2) + 8451904), v1)
                                                        v2 = v3
                                                        break
                                                    v4 = (v4 + 1)
                                                    if ((v4 + 1) != v13):
                                                        continue
                                                    break
                                                break
                                            v7 = (v7 + 1)
                                            if ((v7 + 1) != 255):
                                                continue
                                            break
                                        break
                                    v2 = load32((((v16 + (v9 * 286704)) + v20) + 285656))
                                    if not load32((((v16 + (v9 * 286704)) + v20) + 285656)):
                                        break
                                    v7 = load32(v2 + 8)
                                    if not load32(v2 + 8):
                                        break
                                    v4 = 0
                                    v8 = load8u(arg0 + 45)
                                    v3 = load32(ENTITIES)
                                    v13 = load32(v2)
                                    v5 = 0
                                    v2 = v6
                                    if (u32(load32(9684388)) >= u32(2)):
                                        while True:  # $label217
                                            while True:  # $label215
                                                v1 = load32((v13 + (v4 << 2)))
                                                if not load32((v13 + (v4 << 2))):
                                                    break
                                                v15 = load32((v3 + (v1 * 132)) + 28)
                                                if ((load8u((v3 + (load32((v3 + (v1 * 132)) + 28) * 132)) + 125) == 3) == (v8 != 0)):
                                                    break
                                                v5 = (v5 + 1)
                                                v1 = 0
                                                if v2:
                                                    while True:  # $label216
                                                        if (load32(((v1 << 2) + 8451904)) == v15):
                                                            break
                                                        v1 = (v1 + 1)
                                                        if ((v1 + 1) != v2):
                                                            continue
                                                        break
                                                    if (u32(v2) >= u32(40000)):
                                                        break
                                                v1 = (v2 + 1)
                                                store32(9140300, (v2 + 1))
                                                store32(((v2 << 2) + 8451904), v15)
                                                v2 = v1
                                                break
                                            v4 = (v4 + 1)
                                            if ((v4 + 1) != v7):
                                                continue
                                            break
                                            break
                                        raise Unreachable()
                                    while True:  # $label219
                                        while True:  # $label218
                                            v1 = load32((v13 + (v4 << 2)))
                                            if not load32((v13 + (v4 << 2))):
                                                break
                                            v15 = load32((v3 + (v1 * 132)) + 28)
                                            if ((load8u((v3 + (load32((v3 + (v1 * 132)) + 28) * 132)) + 125) == 3) == (v8 != 0)):
                                                break
                                            v5 = (v5 + 1)
                                            if (u32(v2) > u32(39999)):
                                                break
                                            v1 = (v2 + 1)
                                            store32(9140300, (v2 + 1))
                                            store32(((v2 << 2) + 8451904), v15)
                                            v2 = v1
                                            break
                                        v4 = (v4 + 1)
                                        if ((v4 + 1) != v7):
                                            continue
                                        break
                                    break
                                v1 = load32(arg0 + 12)
                                v4 = load32(arg0 + 16)
                                if load32(arg0 + 16):
                                    break
                                if (u32(v1) < u32(v5)):
                                    break
                                break
                                break
                            v1 = load32(arg0 + 12)
                            v4 = load32(arg0 + 16)
                            v5 = 0
                            break
                        if not v4:
                            break
                        if (u32(v1) <= u32(v5)):
                            break
                        break
                    v10 = 1
                    store32((v11 + v12), 1)
                    v1 = load32(arg0 + 12)
                    v4 = load32(arg0 + 16)
                    break
                if not v4:
                    break
                if (u32(v1) > u32(v5)):
                    break
                store32(9140300, v6)
                break
            v9 = (v9 + 1)
            v1 = load32(PLAYER_COUNT)
            if (u32((v9 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break
        break
    return (v10 & 1)

# ----------------------------------------------------------
# $func381
# ----------------------------------------------------------
def func381(arg0, arg1, arg2, arg3, arg4):
    store64(arg0, 0)
    store64(arg0 + 39, 0)
    store64(arg0 + 32, 0)
    store64(arg0 + 24, 0)
    store64(arg0 + 16, 0)
    store64(arg0 + 8, 0)
    store32(arg0 + 52, 1)
    store32(arg0 + 48, func26(4))
    store32(arg0 + 68, 1)
    store64(arg0 + 56, 4294967296)
    store32(arg0 + 64, func26(4))
    store32(arg0 + 84, 1)
    store64(arg0 + 72, 4294967296)
    store32(arg0 + 80, func26(4))
    store32(arg0 + 100, 1)
    store64(arg0 + 88, 4294967296)
    store32(arg0 + 96, func26(4))
    store64(arg0 + 104, 4294967296)
    v8 = load32(arg2)
    v5 = (load32(arg2) + 1)
    store32(arg2, (load32(arg2) + 1))
    store32(arg0, load32((arg1 + (v8 << 2))))
    v7 = (v8 + 2)
    store32(arg2, (v8 + 2))
    store32(arg0 + 4, load32((arg1 + (v5 << 2))))
    v5 = (v8 + 3)
    store32(arg2, (v8 + 3))
    store32(arg0 + 8, load32((arg1 + (v7 << 2))))
    v7 = (v8 + 4)
    store32(arg2, (v8 + 4))
    store32(arg0 + 12, load32((arg1 + (v5 << 2))))
    v5 = (v8 + 5)
    store32(arg2, (v8 + 5))
    store32(arg0 + 16, load32((arg1 + (v7 << 2))))
    v7 = (v8 + 6)
    store32(arg2, (v8 + 6))
    store32(arg0 + 20, load32((arg1 + (v5 << 2))))
    v5 = (v8 + 7)
    store32(arg2, (v8 + 7))
    store32(arg0 + 24, load32((arg1 + (v7 << 2))))
    v7 = (v8 + 8)
    store32(arg2, (v8 + 8))
    store32(arg0 + 28, load32((arg1 + (v5 << 2))))
    v5 = (v8 + 9)
    store32(arg2, (v8 + 9))
    store32(arg0 + 32, load32((arg1 + (v7 << 2))))
    v7 = (v8 + 10)
    store32(arg2, (v8 + 10))
    store32(arg0 + 36, load32((arg1 + (v5 << 2))))
    v5 = (v8 + 11)
    store32(arg2, (v8 + 11))
    store32(arg0 + 40, load32((arg1 + (v7 << 2))))
    v7 = (v8 + 12)
    store32(arg2, (v8 + 12))
    store8(arg0 + 44, (load32((arg1 + (v5 << 2))) != 0))
    v5 = (v8 + 13)
    store32(arg2, (v8 + 13))
    store8(arg0 + 45, (load32((arg1 + (v7 << 2))) != 0))
    v7 = (v8 + 14)
    store32(arg2, (v8 + 14))
    store8(arg0 + 46, (load32((arg1 + (v5 << 2))) != 0))
    v5 = (v8 + 15)
    store32(arg2, (v8 + 15))
    v12 = load32((arg1 + (v7 << 2)))
    store32(arg0 + 192, load32((arg1 + (v7 << 2))))
    while True:  # $label0
        if not v12:
            break
        if (u32(v12) >= u32(4)):
            v11 = (v12 & -4)
            v13 = (arg0 + 112)
            while True:  # $label1
                v7 = (v5 + 1)
                store32(arg2, (v5 + 1))
                v10 = (v6 << 1)
                store16((v13 + (v6 << 1)), load32((arg1 + (v5 << 2))))
                v8 = (v5 + 2)
                store32(arg2, (v5 + 2))
                store16((v13 + (v10 | 2)), load32((arg1 + (v7 << 2))))
                v7 = (v5 + 3)
                store32(arg2, (v5 + 3))
                store16((v13 + (v10 | 4)), load32((arg1 + (v8 << 2))))
                v5 = (v5 + 4)
                store32(arg2, (v5 + 4))
                store16((v13 + (v10 | 6)), load32((arg1 + (v7 << 2))))
                v6 = (v6 + 4)
                v9 = (v9 + 4)
                if ((v9 + 4) != v11):
                    continue
                break
        v7 = (v12 & 3)
        if not (v12 & 3):
            break
        v8 = 0
        v9 = v5
        while True:  # $label2
            v5 = (v9 + 1)
            store32(arg2, (v9 + 1))
            store16((arg0 + (v6 << 1)) + 112, load32((arg1 + (v9 << 2))))
            v6 = (v6 + 1)
            v9 = v5
            v8 = (v8 + 1)
            if ((v8 + 1) != v7):
                continue
            break
        break
    v6 = (v5 + 1)
    store32(arg2, (v5 + 1))
    v8 = load32((arg1 + (v5 << 2)))
    if load32((arg1 + (v5 << 2))):
        v9 = 0
        while True:  # $label4
            v5 = load32(arg2)
            store32(arg2, (load32(arg2) + 1))
            v7 = load32((arg1 + (v5 << 2)))
            while True:  # $label3
                v5 = load32(arg0 + 56)
                if (load32(arg0 + 56) != load32(arg0 + 52)):
                    v6 = load32(arg0 + 48)
                    break
                v11 = (load32(arg0 + 60) + v5)
                store32(arg0 + 52, (load32(arg0 + 60) + v5))
                v10 = load32(arg0 + 48)
                v6 = func26((-1 if (u32(v11) > u32(1073741823)) else (v11 << 2)))
                if v5:
                    # TODO: memory.copy
                if v10:
                    v5 = load32(arg0 + 56)
                store32(arg0 + 48, v6)
                break
            store32(arg0 + 56, (v5 + 1))
            store32((v6 + (v5 << 2)), v7)
            v9 = (v9 + 1)
            if ((v9 + 1) != v8):
                continue
            break
        v6 = load32(arg2)
    v5 = (v6 + 1)
    store32(arg2, (v6 + 1))
    v8 = load32((arg1 + (v6 << 2)))
    if load32((arg1 + (v6 << 2))):
        v9 = 0
        while True:  # $label6
            v5 = load32(arg2)
            store32(arg2, (load32(arg2) + 1))
            v7 = load32((arg1 + (v5 << 2)))
            while True:  # $label5
                v5 = load32(arg0 + 72)
                if (load32(arg0 + 72) != load32(arg0 + 68)):
                    v6 = load32(arg0 + 64)
                    break
                v11 = (load32(arg0 + 76) + v5)
                store32(arg0 + 68, (load32(arg0 + 76) + v5))
                v10 = load32(arg0 + 64)
                v6 = func26((-1 if (u32(v11) > u32(1073741823)) else (v11 << 2)))
                if v5:
                    # TODO: memory.copy
                if v10:
                    v5 = load32(arg0 + 72)
                store32(arg0 + 64, v6)
                break
            store32(arg0 + 72, (v5 + 1))
            store32((v6 + (v5 << 2)), v7)
            v9 = (v9 + 1)
            if ((v9 + 1) != v8):
                continue
            break
        v5 = load32(arg2)
    v6 = (v5 + 1)
    store32(arg2, (v5 + 1))
    v8 = load32((arg1 + (v5 << 2)))
    if load32((arg1 + (v5 << 2))):
        v9 = 0
        while True:  # $label8
            v5 = load32(arg2)
            store32(arg2, (load32(arg2) + 1))
            v7 = load32((arg1 + (v5 << 2)))
            while True:  # $label7
                v5 = load32(arg0 + 88)
                if (load32(arg0 + 88) != load32(arg0 + 84)):
                    v6 = load32(arg0 + 80)
                    break
                v11 = (load32(arg0 + 92) + v5)
                store32(arg0 + 84, (load32(arg0 + 92) + v5))
                v10 = load32(arg0 + 80)
                v6 = func26((-1 if (u32(v11) > u32(1073741823)) else (v11 << 2)))
                if v5:
                    # TODO: memory.copy
                if v10:
                    v5 = load32(arg0 + 88)
                store32(arg0 + 80, v6)
                break
            store32(arg0 + 88, (v5 + 1))
            store32((v6 + (v5 << 2)), v7)
            v9 = (v9 + 1)
            if ((v9 + 1) != v8):
                continue
            break
        v6 = load32(arg2)
    store32(arg2, (v6 + 1))
    v8 = load32((arg1 + (v6 << 2)))
    if load32((arg1 + (v6 << 2))):
        v9 = 0
        while True:  # $label10
            v5 = load32(arg2)
            store32(arg2, (load32(arg2) + 1))
            v7 = load32((arg1 + (v5 << 2)))
            while True:  # $label9
                v5 = load32(arg0 + 104)
                if (load32(arg0 + 104) != load32(arg0 + 100)):
                    v6 = load32(arg0 + 96)
                    break
                v11 = (load32(arg0 + 108) + v5)
                store32(arg0 + 100, (load32(arg0 + 108) + v5))
                v10 = load32(arg0 + 96)
                v6 = func26((-1 if (u32(v11) > u32(1073741823)) else (v11 << 2)))
                if v5:
                    # TODO: memory.copy
                if v10:
                    v5 = load32(arg0 + 104)
                store32(arg0 + 96, v6)
                break
            store32(arg0 + 104, (v5 + 1))
            store32((v6 + (v5 << 2)), v7)
            v9 = (v9 + 1)
            if ((v9 + 1) != v8):
                continue
            break
    while True:  # $label11
        arg2 = load32(arg0 + 56)
        v7 = load32(PLAYER_COUNT)
        v5 = (load32(PLAYER_COUNT) + 1)
        if (u32(load32(arg0 + 56)) >= u32((load32(PLAYER_COUNT) + 1))):
            break
        while True:  # $label13
            while True:  # $label12
                if (load32(arg0 + 52) != arg2):
                    arg1 = load32(arg0 + 48)
                    break
                arg1 = (load32(arg0 + 60) + arg2)
                store32(arg0 + 52, (load32(arg0 + 60) + arg2))
                v9 = load32(arg0 + 48)
                arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
                if arg2:
                    # TODO: memory.copy
                if v9:
                    arg2 = load32(arg0 + 56)
                store32(arg0 + 48, arg1)
                break
            store32(arg0 + 56, (arg2 + 1))
            store32((arg1 + (arg2 << 2)), 1)
            arg2 = load32(arg0 + 56)
            if (u32(load32(arg0 + 56)) < u32(v5)):
                continue
            break
        if (arg3 != 1):
            break
        store32((load32(arg0 + 48) + (v7 << 2)), 0)
        break
    while True:  # $label14
        arg2 = load32(arg0 + 72)
        if (u32(load32(arg0 + 72)) >= u32(v5)):
            break
        while True:  # $label16
            while True:  # $label15
                if (load32(arg0 + 68) != arg2):
                    arg1 = load32(arg0 + 64)
                    break
                arg1 = (load32(arg0 + 76) + arg2)
                store32(arg0 + 68, (load32(arg0 + 76) + arg2))
                v9 = load32(arg0 + 64)
                arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
                if arg2:
                    # TODO: memory.copy
                if v9:
                    arg2 = load32(arg0 + 72)
                store32(arg0 + 64, arg1)
                break
            store32(arg0 + 72, (arg2 + 1))
            store32((arg1 + (arg2 << 2)), 1)
            arg2 = load32(arg0 + 72)
            if (u32(load32(arg0 + 72)) < u32(v5)):
                continue
            break
        if (arg3 != 1):
            break
        store32((load32(arg0 + 64) + (v7 << 2)), 0)
        break
    while True:  # $label17
        if not arg3:
            break
        if (u32(arg4) > u32(466)):
            break
        arg1 = (v7 << 2)
        store32(((v7 << 2) + load32(arg0 + 64)), 0)
        store32((load32(arg0 + 48) + arg1), 0)
        break
    while True:  # $label18
        if (u32(arg4) > u32(488)):
            break
        if not arg3:
            break
        if (load32(arg0) != 12):
            break
        store32(arg0 + 36, load32(arg0 + 16))
        break

# ----------------------------------------------------------
# $func382
# ----------------------------------------------------------
def func382(arg0, arg1, arg2):
    v3 = load32(arg0)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load32(arg0 + 4)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load32(arg0 + 8)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load32(arg0 + 12)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load32(arg0 + 16)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load32(arg0 + 20)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load32(arg0 + 24)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load32(arg0 + 28)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load32(arg0 + 32)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load32(arg0 + 36)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load32(arg0 + 40)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load8u(arg0 + 44)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load8u(arg0 + 45)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load8u(arg0 + 46)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    v3 = load32(arg0 + 192)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    if load32(arg0 + 192):
        v3 = 0
        while True:  # $label0
            v4 = load16u((arg0 + (v3 << 1)) + 112)
            v5 = load32(arg2)
            store32(arg2, (load32(arg2) + 1))
            store32((arg1 + (v5 << 2)), v4)
            v3 = (v3 + 1)
            if (u32((v3 + 1)) < u32(load32(arg0 + 192))):
                continue
            break
    v3 = load32(arg0 + 56)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    if load32(arg0 + 56):
        v4 = load32(arg0 + 48)
        v3 = 0
        while True:  # $label1
            v5 = load32((v4 + (v3 << 2)))
            v6 = load32(arg2)
            store32(arg2, (load32(arg2) + 1))
            store32((arg1 + (v6 << 2)), v5)
            v3 = (v3 + 1)
            if (u32((v3 + 1)) < u32(load32(arg0 + 56))):
                continue
            break
    v3 = load32(arg0 + 72)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    if load32(arg0 + 72):
        v4 = load32(arg0 + 64)
        v3 = 0
        while True:  # $label2
            v5 = load32((v4 + (v3 << 2)))
            v6 = load32(arg2)
            store32(arg2, (load32(arg2) + 1))
            store32((arg1 + (v6 << 2)), v5)
            v3 = (v3 + 1)
            if (u32((v3 + 1)) < u32(load32(arg0 + 72))):
                continue
            break
    v3 = load32(arg0 + 88)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    if load32(arg0 + 88):
        v4 = load32(arg0 + 80)
        v3 = 0
        while True:  # $label3
            v5 = load32((v4 + (v3 << 2)))
            v6 = load32(arg2)
            store32(arg2, (load32(arg2) + 1))
            store32((arg1 + (v6 << 2)), v5)
            v3 = (v3 + 1)
            if (u32((v3 + 1)) < u32(load32(arg0 + 88))):
                continue
            break
    v3 = load32(arg0 + 104)
    v4 = load32(arg2)
    store32(arg2, (load32(arg2) + 1))
    store32((arg1 + (v4 << 2)), v3)
    if load32(arg0 + 104):
        v4 = load32(arg0 + 96)
        v3 = 0
        while True:  # $label4
            v5 = load32((v4 + (v3 << 2)))
            v6 = load32(arg2)
            store32(arg2, (load32(arg2) + 1))
            store32((arg1 + (v6 << 2)), v5)
            v3 = (v3 + 1)
            if (u32((v3 + 1)) < u32(load32(arg0 + 104))):
                continue
            break

# ----------------------------------------------------------
# $func383
# ----------------------------------------------------------
def func383(arg0, param1):
    if arg0:
        while True:  # $label0
            atomic_store(arg0 + 108, 0)
            if not load32(arg0):
                break
            v1 = load16u(arg0 + 40)
            if (u32(load16u(arg0 + 40)) > u32(4)):
                break
            while True:  # $label1
                if (v1 == 4):
                    break
                v1 = load32(arg0 + 152)
                if not load32(arg0 + 152):
                    break
                store16(arg0 + 42, 65535)
                store64(arg0 + 44, load64(8825))
                store64(arg0 + 52, load64(8833))
                store64(arg0 + 60, load64(8841))
                store64(arg0 + 68, load64(8849))
                store64(arg0 + 74, load64(8855))
                break
            func246(arg0)
            break

# ----------------------------------------------------------
# $func384
# ----------------------------------------------------------
def func384(arg0):

# ----------------------------------------------------------
# $func385
# ----------------------------------------------------------
def func385(arg0):
    while True:  # $label0
        v3 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v2 = 1
        v4 = (v3 - 1)
        v7 = ((v3 - 1) & 1)
        arg0 = load32(arg0 + 283908)
        v5 = (load32(arg0 + 283908) * v3)
        v6 = load32(9143004)
        if (v3 != 2):
            v4 = (v4 & -2)
            v3 = 0
            while True:  # $label1
                v1 = (v2 + 1)
                v1 = ((v1 + (not load8u((v6 + (v2 + v5))) & (arg0 != v2))) + (not load8u((v6 + (v5 + (v2 + 1)))) & (arg0 != v1)))
                v2 = (v2 + 2)
                v3 = (v3 + 2)
                if ((v3 + 2) != v4):
                    continue
                break
        if not v7:
            break
        v1 = (v1 + (not load8u((v6 + (v2 + v5))) & (arg0 != v2)))
        break
    return v1

# ----------------------------------------------------------
# $func386
# ----------------------------------------------------------
def func386(arg0):
    v2 = 1
    while True:  # $label4
        while True:  # $label0
            if load8u(9216060):
                break
            while True:  # $label1
                while True:  # $label3
                    while True:  # $label2
                        v1 = load32(load32(GAME_STATE) + 76)
                        # br_table load32(load32(GAME_STATE) + 76)
                        break
                        break
                    if load32(((arg0 + (load32(9681856) << 2)) + 281808)):
                        break
                    if load32(((arg0 + (load32(9681860) << 2)) + 281808)):
                        break
                    if load32(((arg0 + (load32(9681864) << 2)) + 281808)):
                        break
                    if load32(((arg0 + (load32(9681868) << 2)) + 281808)):
                        break
                    if load32(((arg0 + (load32(9681872) << 2)) + 281808)):
                        break
                    if load32(((arg0 + (load32(9681876) << 2)) + 281808)):
                        break
                    v1 = 9681880
                    break
                    break
                if load32(((arg0 + (load32(9681856) << 2)) + 281808)):
                    break
                if load32(((arg0 + (load32(9681860) << 2)) + 281808)):
                    break
                if load32(((arg0 + (load32(9681864) << 2)) + 281808)):
                    break
                v1 = 9681868
                break
                break
            while True:  # $label5
                if load32(((arg0 + (v1 << 2)) + 281808)):
                    if not load8u(((v1 * 404) + ENTITY_TYPES) + 376):
                        break
                v2 = (u32(v1) < u32(131))
                v1 = (v1 + 1)
                if ((v1 + 1) != 132):
                    continue
                break
            break
        return v2
        break
    return (load32(((arg0 + (load32(v1) << 2)) + 281808)) != 0)

# ----------------------------------------------------------
# $func387
# ----------------------------------------------------------
def func387(arg0):
    while True:  # $label0
        v2 = load32(arg0 + 283908)
        if not load32(arg0 + 283908):
            break
        if load8u(arg0 + 286696):
            break
        if load8u(9147152):
            break
        if func386(arg0):
            break
        while True:  # $label1
            if not load32(load32(GAME_STATE) + 80):
                break
            v4 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            v5 = load32(arg0 + 284608)
            if not load32(arg0 + 284608):
                break
            v6 = load32(PLAYERS)
            v1 = 1
            while True:  # $label3
                while True:  # $label2
                    if (v1 == v2):
                        break
                    v3 = (v6 + (v1 * 286704))
                    if load8u((v6 + (v1 * 286704)) + 286696):
                        break
                    if (load32(v3 + 284608) != v5):
                        break
                    if func386(v3):
                        break
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v4):
                    continue
                break
            break
        if (u32(load32(9671136)) >= u32(4)):
            v2 = load32(arg0 + 283908)
            v1 = 3
            while True:  # $label5
                while True:  # $label4
                    v3 = entities[v1]
                    if (v2 != load16u(entities[v1] + 110)):
                        break
                    if load8u(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 332):
                        func78(v3, 0, 0, 1)
                        break
                    break
                v1 = (v1 + 1)
                if (u32((v1 + 1)) < u32(load32(9671136))):
                    continue
                break
        if not load32(load32(GAME_STATE) + 80):
            break
        v2 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v1 = load32(arg0 + 284608)
        if not load32(arg0 + 284608):
            break
        v4 = load32(PLAYERS)
        v3 = 1
        while True:  # $label9
            while True:  # $label6
                if not v1:
                    break
                v1 = (v4 + (v3 * 286704))
                if (v1 != load32((v4 + (v3 * 286704)) + 284608)):
                    break
                if (u32(load32(9671136)) >= u32(4)):
                    v4 = load32(v1 + 283908)
                    v1 = 3
                    while True:  # $label8
                        while True:  # $label7
                            v2 = entities[v1]
                            if (v4 != load16u(entities[v1] + 110)):
                                break
                            if load8u(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 332):
                                func78(v2, 0, 0, 1)
                                break
                            break
                        v1 = (v1 + 1)
                        if (u32((v1 + 1)) < u32(load32(9671136))):
                            continue
                        break
                v2 = load32(PLAYER_COUNT)
                v4 = load32(PLAYERS)
                break
            v3 = (v3 + 1)
            if (u32((v3 + 1)) >= u32(v2)):
                break
            v1 = load32(arg0 + 284608)
            continue
            break
        raise Unreachable()
        break

# ----------------------------------------------------------
# $func388
# ----------------------------------------------------------
def func388(arg0, arg1):
    while True:  # $label0
        v4 = entities[arg1]
        v2 = load32(((arg0 + (load8u(entities[arg1].sub_state) << 2)) + 285656))
        if not load32(((arg0 + (load8u(entities[arg1].sub_state) << 2)) + 285656)):
            v2 = func26(16)
            store32(func26(16) + 4, 55)
            store32(v2, func26(220))
            store64(v2 + 8, 665719930880)
            store32(((arg0 + (load8u(v4 + 122) << 2)) + 285656), v2)
            v5 = (v2 + 8)
            arg0 = load32(v2)
            break
        v5 = (v2 + 8)
        arg0 = load32(v2 + 8)
        v3 = load32(v2 + 4)
        if (load32(v2 + 8) != load32(v2 + 4)):
            v3 = arg0
            arg0 = load32(v2)
            break
        arg0 = (load32(v2 + 12) + v3)
        store32(v2 + 4, (load32(v2 + 12) + v3))
        v4 = load32(v2)
        arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if v3:
            # TODO: memory.copy
        if v4:
            v3 = load32(v2 + 8)
        store32(v2, arg0)
        break
    store32(v5, (v3 + 1))
    store32((arg0 + (v3 << 2)), arg1)

# ----------------------------------------------------------
# $func390
# ----------------------------------------------------------
def func390(arg0):
    if (load32(arg0 + 4) >= 129):
        v1 = load32(9689392)
        if load32(9689392):
            while True:  # $label0
                v1 = load32(9689392)
                if load32(9689392):
                    continue
                break

# ----------------------------------------------------------
# $func391
# ----------------------------------------------------------
def func391(arg0, arg1):
    while True:  # $label0
        if (load32(arg0 + 44) != ((load32(arg0 + 48) + 1) % load32(arg0 + 40))):
            break
        v2 = load32(arg0 + 40)
        v3 = e()
        if e():
            v5 = (v2 << 1)
            while True:  # $label1
                v4 = load32(arg0 + 48)
                v2 = load32(arg0 + 44)
                if (load32(arg0 + 48) >= load32(arg0 + 44)):
                    v2 = (v4 - v2)
                    break
                v2 = (load32(arg0 + 40) - v2)
                v6 = ((load32(arg0 + 40) - v2) * 12)
                v2 = (v2 + v4)
                break
            store32(arg0 + 48, v2)
            store32(arg0 + 44, 0)
            store32(arg0 + 40, v5)
            store32(arg0 + 36, v3)
        else:
        if 0:
            break
        return 0
        break
    v3 = (load32(arg0 + 36) + (load32(arg0 + 48) * 12))
    store64((load32(arg0 + 36) + (load32(arg0 + 48) * 12)), load64(arg1))
    store32(v3 + 8, load32(arg1 + 8))
    store32(arg0 + 48, ((load32(arg0 + 48) + 1) % load32(arg0 + 40)))
    return 1

# ----------------------------------------------------------
# $func392
# ----------------------------------------------------------
def func392(arg0, arg1):
    v2 = load32(arg1 + 44)
    v3 = (load32(arg1 + 36) + (load32(arg1 + 44) * 12))
    store64(arg0, load64((load32(arg1 + 36) + (load32(arg1 + 44) * 12))))
    store32(arg0 + 8, load32(v3 + 8))
    store32(arg1 + 44, ((v2 + 1) % load32(arg1 + 40)))

# ----------------------------------------------------------
# $func393
# ----------------------------------------------------------
def func393(arg0):
    v1 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    if not func185(52372):
        v2 = load32(52424)
        if (load32(52424) != 52368):
            while True:  # $label0
                v3 = load32(v2 + 56)
                if not atomic_load(v2):
                    v4 = load32(v2 + 52)
                    store32(load32(v2 + 52) + 56, load32(v2 + 56))
                    store32(load32(v2 + 56) + 52, v4)
                    func390(v2)
                v2 = v3
                if (v3 != 52368):
                    continue
                break
        func54(52372)
    while True:  # $label1
        v2 = e()
        if not e():
            break
        v3 = e()
        if not e():
            break
        store64(v1 + 40, 0)
        store64(v1 + 48, 0)
        store32(v1 + 60, 0)
        store64(v1 + 32, 0)
        store32(v1 + 28, arg0)
        store32(v1 + 24, 0)
        store32(v1 + 20, v3)
        store32(v1 + 16, 128)
        store32(v1 + 12, 0)
        store32(v1 + 8, 0)
        store32(v1 + 4, 0)
        store32(v1, 0)
        store32(v2, load32(v1 + 60))
        store64(v2 + 20, load64(v1 + 48))
        store64(v2 + 12, load64(v1 + 40))
        store64(v2 + 4, load64(v1 + 32))
        store32(v2 + 28, load32(v1 + 28))
        store32(v2 + 32, load32(v1 + 24))
        store32(v2 + 36, load32(v1 + 20))
        store32(v2 + 40, load32(v1 + 16))
        store32(v2 + 44, load32(v1 + 12))
        store32(v2 + 48, load32(v1 + 8))
        store32(v2 + 52, load32(v1 + 4))
        store32(v2 + 56, load32(v1))
        v5 = v2
        break
    G.global0 = (v1 - -64)
    return v5

# ----------------------------------------------------------
# $func394
# ----------------------------------------------------------
def func394(arg0, param1):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v2 = (arg0 + 4)
    if (load32(arg0 + 44) != load32(arg0 + 48)):
        while True:  # $label0
            func392((v1 + 4), arg0)
            v3 = load32(v1 + 8)
            if load32(v1 + 8):
            if (load32(arg0 + 44) != load32(arg0 + 48)):
                continue
            break
    func54(v2)
    atomic_store(arg0, 0)
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $func396
# ----------------------------------------------------------
def func396(arg0, arg1):
    v5 = (arg0 + arg1)
    while True:  # $label1
        while True:  # $label0
            v2 = load32(arg0 + 4)
            if (load32(arg0 + 4) & 1):
                break
            if not (v2 & 3):
                break
            v2 = load32(arg0)
            arg1 = (load32(arg0) + arg1)
            while True:  # $label2
                arg0 = (arg0 - v2)
                if ((arg0 - v2) != load32(HEAP_TOP)):
                    if (u32(v2) <= u32(255)):
                        v2 = ((v2 & 0xFFFFFFFF) >> 3)
                        v4 = load32(arg0 + 8)
                        v3 = load32(arg0 + 12)
                        if (load32(arg0 + 8) != load32(arg0 + 12)):
                            break
                        store32(HEAP_FREELIST, (load32(HEAP_FREELIST) & rotl(-2, v2)))
                        break
                    v6 = load32(arg0 + 24)
                    while True:  # $label3
                        v2 = load32(arg0 + 12)
                        if (arg0 != load32(arg0 + 12)):
                            v3 = load32(arg0 + 8)
                            store32(load32(arg0 + 8) + 12, v2)
                            store32(v2 + 8, v3)
                            break
                        while True:  # $label4
                            v4 = (arg0 + 20)
                            v3 = load32((arg0 + 20))
                            if load32((arg0 + 20)):
                                break
                            v4 = (arg0 + 16)
                            v3 = load32((arg0 + 16))
                            if load32((arg0 + 16)):
                                break
                            v2 = 0
                            break
                            break
                        while True:  # $label5
                            v7 = v4
                            v2 = v3
                            v4 = (v3 + 20)
                            v3 = load32((v3 + 20))
                            if load32((v3 + 20)):
                                continue
                            v4 = (v2 + 16)
                            v3 = load32(v2 + 16)
                            if load32(v2 + 16):
                                continue
                            break
                        store32(v7, 0)
                        break
                    if not v6:
                        break
                    while True:  # $label6
                        v4 = load32(arg0 + 28)
                        v3 = ((load32(arg0 + 28) << 2) + 9690768)
                        if (load32(((load32(arg0 + 28) << 2) + 9690768)) == arg0):
                            store32(v3, v2)
                            if v2:
                                break
                            store32(HEAP_TREE, (load32(HEAP_TREE) & rotl(-2, v4)))
                            break
                        store32((v6 + (16 if (load32(v6 + 16) == arg0) else 20)), v2)
                        if not v2:
                            break
                        break
                    store32(v2 + 24, v6)
                    v3 = load32(arg0 + 16)
                    if load32(arg0 + 16):
                        store32(v2 + 16, v3)
                        store32(v3 + 24, v2)
                    v3 = load32(arg0 + 20)
                    if not load32(arg0 + 20):
                        break
                    store32(v2 + 20, v3)
                    store32(v3 + 24, v2)
                    break
                v2 = load32(v5 + 4)
                if ((load32(v5 + 4) & 3) != 3):
                    break
                store32(FREE_SIZE, arg1)
                store32(v5 + 4, (v2 & -2))
                store32(arg0 + 4, (arg1 | 1))
                store32(v5, arg1)
                return
                break
            store32(v4 + 12, v3)
            store32(v3 + 8, v4)
            break
        while True:  # $label12
            v2 = load32(v5 + 4)
            if not (load32(v5 + 4) & 2):
                if (load32(HEAP_END) == v5):
                    store32(HEAP_END, arg0)
                    arg1 = (load32(HEAP_TOTAL) + arg1)
                    store32(HEAP_TOTAL, (load32(HEAP_TOTAL) + arg1))
                    store32(arg0 + 4, (arg1 | 1))
                    if (arg0 != load32(HEAP_TOP)):
                        break
                    store32(FREE_SIZE, 0)
                    store32(HEAP_TOP, 0)
                    return
                if (load32(HEAP_TOP) == v5):
                    store32(HEAP_TOP, arg0)
                    arg1 = (load32(FREE_SIZE) + arg1)
                    store32(FREE_SIZE, (load32(FREE_SIZE) + arg1))
                    store32(arg0 + 4, (arg1 | 1))
                    store32((arg0 + arg1), arg1)
                    return
                arg1 = ((v2 & -8) + arg1)
                while True:  # $label7
                    if (u32(v2) <= u32(255)):
                        v2 = ((v2 & 0xFFFFFFFF) >> 3)
                        v3 = load32(v5 + 12)
                        v4 = load32(v5 + 8)
                        if (load32(v5 + 12) == load32(v5 + 8)):
                            store32(HEAP_FREELIST, (load32(HEAP_FREELIST) & rotl(-2, v2)))
                            break
                        store32(v4 + 12, v3)
                        store32(v3 + 8, v4)
                        break
                    v6 = load32(v5 + 24)
                    while True:  # $label8
                        v2 = load32(v5 + 12)
                        if (v5 != load32(v5 + 12)):
                            v3 = load32(v5 + 8)
                            store32(load32(v5 + 8) + 12, v2)
                            store32(v2 + 8, v3)
                            break
                        while True:  # $label9
                            v3 = (v5 + 20)
                            v4 = load32((v5 + 20))
                            if load32((v5 + 20)):
                                break
                            v3 = (v5 + 16)
                            v4 = load32((v5 + 16))
                            if load32((v5 + 16)):
                                break
                            v2 = 0
                            break
                            break
                        while True:  # $label10
                            v7 = v3
                            v2 = v4
                            v3 = (v4 + 20)
                            v4 = load32((v4 + 20))
                            if load32((v4 + 20)):
                                continue
                            v3 = (v2 + 16)
                            v4 = load32(v2 + 16)
                            if load32(v2 + 16):
                                continue
                            break
                        store32(v7, 0)
                        break
                    if not v6:
                        break
                    while True:  # $label11
                        v4 = load32(v5 + 28)
                        v3 = ((load32(v5 + 28) << 2) + 9690768)
                        if (load32(((load32(v5 + 28) << 2) + 9690768)) == v5):
                            store32(v3, v2)
                            if v2:
                                break
                            store32(HEAP_TREE, (load32(HEAP_TREE) & rotl(-2, v4)))
                            break
                        store32((v6 + (16 if (load32(v6 + 16) == v5) else 20)), v2)
                        if not v2:
                            break
                        break
                    store32(v2 + 24, v6)
                    v3 = load32(v5 + 16)
                    if load32(v5 + 16):
                        store32(v2 + 16, v3)
                        store32(v3 + 24, v2)
                    v3 = load32(v5 + 20)
                    if not load32(v5 + 20):
                        break
                    store32(v2 + 20, v3)
                    store32(v3 + 24, v2)
                    break
                store32(arg0 + 4, (arg1 | 1))
                store32((arg0 + arg1), arg1)
                if (arg0 != load32(HEAP_TOP)):
                    break
                store32(FREE_SIZE, arg1)
                return
            store32(v5 + 4, (v2 & -2))
            store32(arg0 + 4, (arg1 | 1))
            store32((arg0 + arg1), arg1)
            break
        if (u32(arg1) <= u32(255)):
            v2 = ((arg1 & -8) + 9690504)
            while True:  # $label13
                v3 = load32(HEAP_FREELIST)
                arg1 = (1 << ((arg1 & 0xFFFFFFFF) >> 3))
                if not (load32(HEAP_FREELIST) & (1 << ((arg1 & 0xFFFFFFFF) >> 3))):
                    store32(HEAP_FREELIST, (arg1 | v3))
                    break
                break
            arg1 = load32(v2 + 8)
            store32(v2 + 8, arg0)
            store32(arg1 + 12, arg0)
            store32(arg0 + 12, v2)
            store32(arg0 + 8, arg1)
            return v2
        v4 = 31
        if (u32(arg1) <= u32(16777215)):
            v2 = clz(((arg1 & 0xFFFFFFFF) >> 8))
            v4 = (((((arg1 & 0xFFFFFFFF) >> (38 - clz(((arg1 & 0xFFFFFFFF) >> 8)))) & 1) - (v2 << 1)) + 62)
        store32(arg0 + 28, v4)
        store64(arg0 + 16, 0)
        v7 = ((v4 << 2) + 9690768)
        while True:  # $label15
            while True:  # $label14
                v3 = load32(HEAP_TREE)
                v2 = (1 << v4)
                if not (load32(HEAP_TREE) & (1 << v4)):
                    store32(HEAP_TREE, (v2 | v3))
                    store32(v7, arg0)
                    store32(arg0 + 24, v7)
                    break
                v4 = (arg1 << ((25 - ((v4 & 0xFFFFFFFF) >> 1)) if (v4 != 31) else 0))
                v2 = load32(v7)
                while True:  # $label16
                    v3 = v2
                    if ((load32(v2 + 4) & -8) == arg1):
                        break
                    v2 = ((v4 & 0xFFFFFFFF) >> 29)
                    v4 = (v4 << 1)
                    v7 = (v3 + (v2 & 4))
                    v2 = load32(((v3 + (v2 & 4)) + 16))
                    if load32(((v3 + (v2 & 4)) + 16)):
                        continue
                    break
                store32(v7 + 16, arg0)
                store32(arg0 + 24, v3)
                break
            store32(arg0 + 12, arg0)
            store32(arg0 + 8, arg0)
            return
            break
        arg1 = load32(v3 + 8)
        store32(load32(v3 + 8) + 12, arg0)
        store32(v3 + 8, arg0)
        store32(arg0 + 24, 0)
        store32(arg0 + 12, v3)
        store32(arg0 + 8, arg1)
        break

# ----------------------------------------------------------
# $func397
# ----------------------------------------------------------
def func397(arg0, arg1, arg2):
    while True:  # $label0
        if not arg2:
            break
        v3 = load32(59176)
        while True:  # $label1
            v4 = ((v5 << 2) + arg1)
            if (u32(load32(((v5 << 2) + arg1) + 4)) > u32(v3)):
                break
            v5 = (load32(v4 + 8) + v5)
            if (u32((load32(v4 + 8) + v5)) < u32(arg2)):
                continue
            break
        break
    if (u32(arg2) > u32(v5)):
        while True:  # $label3
            v7 = load32((arg1 + (v5 << 2)))
            while True:  # $label2
                v3 = load32(9561704)
                if (load32(9561704) != load32(9561700)):
                    v4 = load32(9561696)
                    break
                v4 = (load32(9561708) + v3)
                store32(9561700, (load32(9561708) + v3))
                v6 = load32(9561696)
                v4 = func26((-1 if (u32(v4) > u32(1073741823)) else (v4 << 2)))
                if v3:
                    # TODO: memory.copy
                if v6:
                    v3 = load32(9561704)
                store32(9561696, v4)
                break
            store32(9561704, (v3 + 1))
            store32((v4 + (v3 << 2)), v7)
            v5 = (v5 + 1)
            if ((v5 + 1) != arg2):
                continue
            break
    if (u32(arg0) > u32(load32(59160))):
        store32(59160, arg0)
    if (u32(arg0) > u32(load32(59176))):
        store32(59176, arg0)

# ----------------------------------------------------------
# $func398
# ----------------------------------------------------------
def func398(arg0):
    if not load8u(9142917):
        v5 = (arg0 + 2147483647)
        v4 = ((load32(9142848) * 25) + 150)
        while True:  # $label4
            while True:  # $label0
                v1 = load32(9299864)
                if load32(9299864):
                    arg0 = 0
                    v3 = load32(9299856)
                    while True:  # $label1
                        v2 = (v3 + (arg0 << 2))
                        if not load32((v3 + (arg0 << 2))):
                            break
                        arg0 = (arg0 + 2)
                        if (u32((arg0 + 2)) < u32(v1)):
                            continue
                        break
                while True:  # $label2
                    if (load32(9299860) != v1):
                        v2 = load32(9299856)
                        break
                    arg0 = (load32(9299868) + v1)
                    store32(9299860, (load32(9299868) + v1))
                    v3 = load32(9299856)
                    v2 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                    if v1:
                        # TODO: memory.copy
                    if v3:
                        v1 = load32(9299864)
                    store32(9299856, v2)
                    break
                store32(9299864, (v1 + 1))
                store32((v2 + (v1 << 2)), v4)
                while True:  # $label3
                    arg0 = load32(9299864)
                    if (load32(9299864) != load32(9299860)):
                        v1 = v2
                        break
                    v1 = (load32(9299868) + arg0)
                    store32(9299860, (load32(9299868) + arg0))
                    v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                    if arg0:
                        # TODO: memory.copy
                    store32(9299856, v1)
                    arg0 = load32(9299864)
                    break
                store32(9299864, (arg0 + 1))
                break
                break
            store32(v2, v4)
            break
        store32((v3 + ((arg0 << 2) | 4)), v5)
    return (v1 + (arg0 << 2))

# ----------------------------------------------------------
# $func399
# ----------------------------------------------------------
def func399(arg0, arg1):
    v3 = (load32(arg0 + 12) - 5)
    v2 = load32(arg0 + 44)
    v9 = ((load32(arg0 + 12) - 5) if (u32(v2) > u32(v3)) else load32(arg0 + 44))
    v6 = load32(load32(arg0) + 4)
    v10 = (arg1 != 4)
    while True:  # $label0
        while True:  # $label5
            v5 = 1
            v2 = load32(arg0)
            v3 = load32(load32(arg0) + 16)
            v8 = ((load32(arg0 + 5820) + 42) >> 3)
            if (u32(load32(load32(arg0) + 16)) < u32(((load32(arg0 + 5820) + 42) >> 3))):
                break
            v11 = load32(arg0 + 108)
            v12 = load32(arg0 + 92)
            v7 = (load32(arg0 + 108) - load32(arg0 + 92))
            v4 = ((load32(arg0 + 108) - load32(arg0 + 92)) + load32(v2 + 4))
            v3 = (v3 - v8)
            v3 = (((load32(arg0 + 108) - load32(arg0 + 92)) + load32(v2 + 4)) if (u32(v3) > u32(v4)) else (v3 - v8))
            v3 = (65535 if (u32(v3) >= u32(65535)) else (((load32(arg0 + 108) - load32(arg0 + 92)) + load32(v2 + 4)) if (u32(v3) > u32(v4)) else (v3 - v8)))
            if (u32(v9) > u32((65535 if (u32(v3) >= u32(65535)) else (((load32(arg0 + 108) - load32(arg0 + 92)) + load32(v2 + 4)) if (u32(v3) > u32(v4)) else (v3 - v8))))):
                if not arg1:
                    break
                if (v10 & not v3):
                    break
                if (v3 != v4):
                    break
            v8 = ((arg1 == 4) & (v3 == v4))
            store8(((load32(arg0 + 20) + load32(arg0 + 8)) - 4), v3)
            store8(((load32(arg0 + 20) + load32(arg0 + 8)) - 3), ((v3 & 0xFFFFFFFF) >> 8))
            v2 = (v3 ^ -1)
            store8(((load32(arg0 + 20) + load32(arg0 + 8)) - 2), (v3 ^ -1))
            store8(((load32(arg0 + 20) + load32(arg0 + 8)) - 1), ((v2 & 0xFFFFFFFF) >> 8))
            v2 = load32(arg0)
            v4 = load32(load32(arg0) + 28)
            while True:  # $label1
                v5 = load32(v4 + 20)
                v13 = load32(v2 + 16)
                v5 = (load32(v4 + 20) if (u32(v5) < u32(v13)) else load32(v2 + 16))
                if not (load32(v4 + 20) if (u32(v5) < u32(v13)) else load32(v2 + 16)):
                    break
                store32(v2 + 12, (load32(v2 + 12) + v5))
                store32(v4 + 16, (load32(v4 + 16) + v5))
                store32(v2 + 20, (load32(v2 + 20) + v5))
                store32(v2 + 16, (load32(v2 + 16) - v5))
                v2 = load32(v4 + 20)
                store32(v4 + 20, (load32(v4 + 20) - v5))
                if (v2 != v5):
                    break
                store32(v4 + 16, load32(v4 + 8))
                break
            if (v11 != v12):
                v2 = (v7 if (u32(v3) > u32(v7)) else v3)
                v4 = load32(arg0)
                store32(load32(arg0) + 12, (load32(v4 + 12) + v2))
                store32(v4 + 16, (load32(v4 + 16) - v2))
                store32(v4 + 20, (load32(v4 + 20) + v2))
                store32(arg0 + 92, (load32(arg0 + 92) + v2))
                v3 = (v3 - v2)
            if v3:
                v2 = load32(arg0)
                v5 = load32(load32(arg0) + 12)
                v7 = load32(v2 + 4)
                v4 = (load32(v2 + 4) if (u32(v3) > u32(v7)) else v3)
                if (load32(v2 + 4) if (u32(v3) > u32(v7)) else v3):
                    store32(v2 + 4, (v7 - v4))
                    v5 = func35(v5, load32(v2), v4)
                    while True:  # $label4
                        while True:  # $label3
                            while True:  # $label2
                                # br_table (load32(load32(v2 + 28) + 24) - 1)
                                break
                                break
                            store32(v2 + 48, func89(load32(v2 + 48), v5, v4))
                            break
                            break
                        store32(v2 + 48, func43(load32(v2 + 48), v5, v4))
                        break
                    store32(v2, (load32(v2) + v4))
                    store32(v2 + 8, (load32(v2 + 8) + v4))
                    v2 = load32(arg0)
                    v5 = load32(load32(arg0) + 12)
                store32(v2 + 12, (v3 + v5))
                store32(v2 + 16, (load32(v2 + 16) - v3))
                store32(v2 + 20, (load32(v2 + 20) + v3))
            if not v8:
                continue
            break
        v2 = load32(arg0)
        v5 = 0
        break
    while True:  # $label6
        v3 = load32(v2 + 4)
        if (load32(v2 + 4) == v6):
            v3 = load32(arg0 + 108)
            break
        while True:  # $label7
            v4 = (v6 - v3)
            v3 = load32(arg0 + 44)
            if (u32((v6 - v3)) >= u32(load32(arg0 + 44))):
                store32(arg0 + 5808, 2)
                v3 = load32(arg0 + 44)
                store32(arg0 + 5812, load32(arg0 + 44))
                store32(arg0 + 108, v3)
                break
            while True:  # $label8
                v2 = load32(arg0 + 108)
                if (u32((load32(arg0 + 60) - load32(arg0 + 108))) > u32(v4)):
                    break
                v2 = (v2 - v3)
                store32(arg0 + 108, (v2 - v3))
                v6 = load32(arg0 + 56)
                v3 = load32(arg0 + 5808)
                if (u32(load32(arg0 + 5808)) <= u32(1)):
                    store32(arg0 + 5808, (v3 + 1))
                v2 = load32(arg0 + 108)
                if (u32(load32(arg0 + 108)) >= u32(load32(arg0 + 5812))):
                    break
                store32(arg0 + 5812, v2)
                break
            v3 = (load32(arg0 + 108) + v4)
            store32(arg0 + 108, (load32(arg0 + 108) + v4))
            v2 = load32(arg0 + 5812)
            v6 = (load32(arg0 + 44) - load32(arg0 + 5812))
            store32(arg0 + 5812, ((v4 if (u32(v4) < u32(v6)) else (load32(arg0 + 44) - load32(arg0 + 5812))) + v2))
            break
        store32(arg0 + 92, v3)
        break
    if (u32(v3) > u32(load32(arg0 + 5824))):
        store32(arg0 + 5824, v3)
    v2 = 3
    while True:  # $label9
        if not v5:
            break
        while True:  # $label10
            while True:  # $label11
                # br_table arg1
                break
                break
            if load32(load32(arg0) + 4):
                break
            v2 = 1
            if (v3 == load32(arg0 + 92)):
                break
            break
        while True:  # $label12
            v2 = (load32(arg0 + 60) - v3)
            if (u32((load32(arg0 + 60) - v3)) >= u32(load32(load32(arg0) + 4))):
                break
            v5 = load32(arg0 + 92)
            v4 = load32(arg0 + 44)
            if (load32(arg0 + 92) < load32(arg0 + 44)):
                break
            v3 = (v3 - v4)
            store32(arg0 + 108, (v3 - v4))
            store32(arg0 + 92, (v5 - v4))
            v5 = load32(arg0 + 56)
            v3 = load32(arg0 + 5808)
            if (u32(load32(arg0 + 5808)) <= u32(1)):
                store32(arg0 + 5808, (v3 + 1))
            v2 = (load32(arg0 + 44) + v2)
            v3 = load32(arg0 + 108)
            if (u32(load32(arg0 + 108)) >= u32(load32(arg0 + 5812))):
                break
            store32(arg0 + 5812, v3)
            break
        v4 = load32(arg0)
        v5 = load32(load32(arg0) + 4)
        v2 = (v2 if (u32(v2) < u32(v5)) else load32(load32(arg0) + 4))
        if (v2 if (u32(v2) < u32(v5)) else load32(load32(arg0) + 4)):
            v6 = load32(arg0 + 56)
            store32(v4 + 4, (v5 - v2))
            v3 = func35((v3 + v6), load32(v4), v2)
            while True:  # $label15
                while True:  # $label14
                    while True:  # $label13
                        # br_table (load32(load32(v4 + 28) + 24) - 1)
                        break
                        break
                    store32(v4 + 48, func89(load32(v4 + 48), v3, v2))
                    break
                    break
                store32(v4 + 48, func43(load32(v4 + 48), v3, v2))
                break
            store32(v4, (load32(v4) + v2))
            store32(v4 + 8, (load32(v4 + 8) + v2))
            v3 = (load32(arg0 + 108) + v2)
            store32(arg0 + 108, (load32(arg0 + 108) + v2))
            v4 = load32(arg0 + 5812)
            v5 = (load32(arg0 + 44) - load32(arg0 + 5812))
            store32(arg0 + 5812, ((v2 if (u32(v2) < u32(v5)) else (load32(arg0 + 44) - load32(arg0 + 5812))) + v4))
        if (u32(v3) > u32(load32(arg0 + 5824))):
            store32(arg0 + 5824, v3)
        v6 = load32(arg0 + 92)
        v5 = (v3 - load32(arg0 + 92))
        v2 = (load32(arg0 + 12) - ((load32(arg0 + 5820) + 42) >> 3))
        v4 = (65535 if (u32(v2) >= u32(65535)) else (load32(arg0 + 12) - ((load32(arg0 + 5820) + 42) >> 3)))
        v2 = load32(arg0 + 44)
        if (u32((v3 - load32(arg0 + 92))) < u32(((65535 if (u32(v2) >= u32(65535)) else (load32(arg0 + 12) - ((load32(arg0 + 5820) + 42) >> 3))) if (u32(v2) > u32(v4)) else load32(arg0 + 44)))):
            v2 = 0
            if not arg1:
                break
            if not ((arg1 == 4) | (v3 != v6)):
                break
            if load32(load32(arg0) + 4):
                break
            if (u32(v4) < u32(v5)):
                break
        v2 = 0
        if (arg1 == 4):
            v2 = (not load32(load32(arg0) + 4) & (u32(v4) >= u32(v5)))
        arg1 = (v5 if (u32(v4) > u32(v5)) else v4)
        store32(arg0 + 92, (load32(arg0 + 92) + arg1))
        arg0 = load32(arg0)
        arg1 = load32(load32(arg0) + 28)
        while True:  # $label16
            v3 = load32(arg1 + 20)
            v4 = load32(arg0 + 16)
            v3 = (load32(arg1 + 20) if (u32(v3) < u32(v4)) else load32(arg0 + 16))
            if not (load32(arg1 + 20) if (u32(v3) < u32(v4)) else load32(arg0 + 16)):
                break
            store32(arg0 + 12, (load32(arg0 + 12) + v3))
            store32(arg1 + 16, (load32(arg1 + 16) + v3))
            store32(arg0 + 20, (load32(arg0 + 20) + v3))
            store32(arg0 + 16, (load32(arg0 + 16) - v3))
            arg0 = load32(arg1 + 20)
            store32(arg1 + 20, (load32(arg1 + 20) - v3))
            if (arg0 != v3):
                break
            store32(arg1 + 16, load32(arg1 + 8))
            break
        v2 = (2 if v2 else 0)
        break
    return v2
