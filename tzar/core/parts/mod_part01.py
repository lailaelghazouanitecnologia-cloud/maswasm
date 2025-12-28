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
# $func32
# ----------------------------------------------------------
def func32(arg0, arg1, param2):
    v13 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if (load8u(arg0 + 125) == 3):
            break
        v10 = load8u(arg0 + 122)
        v14 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        v8 = load16u(arg0 + 110)
        v9 = load32(PLAYERS)
        v4 = load32(((v10 * 72) + 9263856) + 28)
        while True:  # $label1
            if arg1:
                break
            v5 = load8u(9147152)
            if load8u(9147152):
                break
            if not load8u(9147211):
                break
            v6 = ((v10 * 404) + ENTITY_TYPES)
            v7 = load32(((v10 * 404) + ENTITY_TYPES) + 40)
            if not load32(((v10 * 404) + ENTITY_TYPES) + 40):
                break
            v2 = load16u(arg0 + 112)
            v3 = ((load16u(arg0 + 112) << 5) - load32(9142952))
            v3 = load16u(arg0 + 114)
            v11 = ((load16u(arg0 + 114) << 5) - load32(9142956))
            if ((((((load16u(arg0 + 112) << 5) - load32(9142952)) * v3) + (((load16u(arg0 + 114) << 5) - load32(9142956)) * v11)) - 1) > 9000000):
                break
            v6 = load32(v6 + 36)
            while True:  # $label2
                v11 = load32(load32(GAME_STATE) + 48)
                if not load32(load32(GAME_STATE) + 48):
                    break
                if v5:
                    break
                v5 = load16u((load32(9147376) + (((load32(9142440) * v3) + v2) << 1)))
                if (v11 == 2):
                    if (u32(v5) > u32(1)):
                        break
                    break
                if not v5:
                    break
                break
            store32(v13, load32((v6 + (((load32(9142848) + v2) % v7) << 2))))
            store32(v13 + 4, v2)
            store32(v13 + 8, v3)
            a_b()
            break
        v15 = load8u(arg0 + 124)
        while True:  # $label3
            if (load32(v14 + 264) != 1):
                break
            v2 = ((v10 * 404) + ENTITY_TYPES)
            v3 = load32(((v10 * 404) + ENTITY_TYPES) + 360)
            if load32(((v10 * 404) + ENTITY_TYPES) + 360):
                v4 = load32(v3)
                break
            while True:  # $label10
                while True:  # $label9
                    while True:  # $label8
                        while True:  # $label7
                            while True:  # $label6
                                while True:  # $label5
                                    while True:  # $label4
                                        v3 = load32(v2 + 216)
                                        v2 = load32(v2 + 220)
                                        v2 = (load32(v2 + 216) if (u32(v2) < u32(v3)) else load32(v2 + 220))
                                        # br_table ((6 if (u32(v2) >= u32(6)) else (load32(v2 + 216) if (u32(v2) < u32(v3)) else load32(v2 + 220))) - 1)
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
            v4 = (load32(9142632) if (u32(v2) > u32(5)) else v4)
            store8(arg0 + 124, 0)
            break
        if load8u(9147152):
            func77(arg0)
            store32(arg0 + 28, 0)
        while True:  # $label11
            if not load8u(9147213):
                break
            while True:  # $label12
                if not arg1:
                    if not load8u(9147152):
                        break
                v2 = load32(arg0 + 40)
                if not load32(arg0 + 40):
                    break
                func38(v2)
                break
                break
            if (load32(38448) == load8u(arg0 + 122)):
                store8(arg0 + 124, (load32(arg0 + 28) % 3))
                break
            if v4:
                store8(arg0 + 124, 0)
                func92(arg0, 0.0, 0.0)
                if not load32(v4 + 24):
                    break
                v2 = load32(arg0 + 40)
                if not load32(arg0 + 40):
                    break
                func254(v4, v2)
                break
            v2 = load32(arg0 + 40)
            if not load32(arg0 + 40):
                break
            func38(v2)
            break
        v11 = load32(arg0 + 36)
        if load32(arg0 + 36):
        v2 = load32(((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if load32(((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) * 40) + 9671200) + 32):
        if load32(9147132):
            v6 = load32(arg0 + 28)
            v7 = load32(ENTITIES)
            while True:  # $label32
                while True:  # $label14
                    while True:  # $label13
                        v3 = load32(9215904)
                        if not load32(9215904):
                            break
                        v5 = load32(v3 + 8)
                        if not load32(v3 + 8):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label15
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # $label16
                        v3 = load32(9215908)
                        if not load32(9215908):
                            break
                        v5 = load32(v3 + 8)
                        if not load32(v3 + 8):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label17
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # $label18
                        v3 = load32(9215912)
                        if not load32(9215912):
                            break
                        v5 = load32(v3 + 8)
                        if not load32(v3 + 8):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label19
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # $label20
                        v3 = load32(9215916)
                        if not load32(9215916):
                            break
                        v5 = load32(v3 + 8)
                        if not load32(v3 + 8):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label21
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # $label22
                        v3 = load32(9215920)
                        if not load32(9215920):
                            break
                        v5 = load32(v3 + 8)
                        if not load32(v3 + 8):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label23
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # $label24
                        v3 = load32(9215924)
                        if not load32(9215924):
                            break
                        v5 = load32(v3 + 8)
                        if not load32(v3 + 8):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label25
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # $label26
                        v3 = load32(9215928)
                        if not load32(9215928):
                            break
                        v5 = load32(v3 + 8)
                        if not load32(v3 + 8):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label27
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # $label28
                        v3 = load32(9215932)
                        if not load32(9215932):
                            break
                        v5 = load32(v3 + 8)
                        if not load32(v3 + 8):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label29
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # $label30
                        v3 = load32(9215936)
                        if not load32(9215936):
                            break
                        v5 = load32(v3 + 8)
                        if not load32(v3 + 8):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label31
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    v3 = load32(9215940)
                    if not load32(9215940):
                        break
                    v5 = load32(v3 + 8)
                    if not load32(v3 + 8):
                        break
                    v4 = load32(v3)
                    v2 = 0
                    while True:  # $label33
                        if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                            break
                        v2 = (v2 + 1)
                        if ((v2 + 1) != v5):
                            continue
                        break
                    break
                    break
                v5 = (v5 - 1)
                store32(v3 + 8, (v5 - 1))
                if (u32(v2) >= u32(v5)):
                    break
                while True:  # $label34
                    v2 = (v2 + 1)
                    store32((v4 + (v2 << 2)), load32((v4 + ((v2 + 1) << 2))))
                    if (u32(v2) < u32(load32(v3 + 8))):
                        continue
                    break
                break
        while True:  # $label35
            if not load8u(9147213):
                break
            if not load32(arg0 + 40):
                break
            v3 = load32(arg0 + 12)
            if not load32(arg0 + 12):
                break
            if load32(v3 + 8):
                v4 = 0
                while True:  # $label36
                    func38(load32((load32(v3) + (v4 << 2))))
                    v4 = (v4 + 2)
                    v3 = load32(arg0 + 12)
                    if (u32((v4 + 2)) < u32(load32(load32(arg0 + 12) + 8))):
                        continue
                    break
            store32(v3 + 8, 0)
            break
        while True:  # $label37
            v12 = load8u(arg0 + 125)
            if (load8u(arg0 + 125) != 4):
                break
            v2 = load8u(arg0 + 122)
            if (load8u(arg0 + 122) == load32(38600)):
                break
            if (load32(38472) == v2):
                break
            if load8u(9216060):
                break
            v2 = ((v10 * 404) + 9568164)
            v3 = (v9 + (v8 * 286704))
            v4 = load32((v9 + (v8 * 286704)) + 283848)
            if (load32((v9 + (v8 * 286704)) + 283848) != 2147483647):
                store32((v3 + 283848), (load32(v2) + v4))
            v3 = (v3 + 283852)
            v4 = load32((v3 + 283852))
            if (load32((v3 + 283852)) != 2147483647):
                store32(v3, (load32(v2 + 4) + v4))
            v3 = (v9 + (v8 * 286704))
            v4 = ((v9 + (v8 * 286704)) + 283856)
            v5 = load32(((v9 + (v8 * 286704)) + 283856))
            if (load32(((v9 + (v8 * 286704)) + 283856)) != 2147483647):
                store32(v4, (load32(v2 + 8) + v5))
            v3 = (v3 + 283860)
            v4 = load32((v3 + 283860))
            if (load32((v3 + 283860)) != 2147483647):
                store32(v3, (load32(v2 + 12) + v4))
            v3 = (v9 + (v8 * 286704))
            v4 = ((v9 + (v8 * 286704)) + 281692)
            store32(((v9 + (v8 * 286704)) + 281692), (load32(v4) - load32(v2)))
            v4 = (v3 + 281696)
            store32((v3 + 281696), (load32(v4) - load32(v2 + 4)))
            v4 = (v3 + 281700)
            store32((v3 + 281700), (load32(v4) - load32(v2 + 8)))
            v2 = load32(v2 + 12)
            v4 = 1
            store8(v3 + 286701, 1)
            v5 = (v3 + 281704)
            store32((v3 + 281704), (load32(v5) - v2))
            v2 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            v5 = (v2 - 1)
            v16 = ((v2 - 1) & 1)
            v3 = (load32(v3 + 283908) * v2)
            v6 = load32(PLAYERS)
            v7 = load32(9143016)
            if (v2 != 2):
                v2 = (v5 & -2)
                v5 = 0
                while True:  # $label38
                    if load8u((v7 + (v3 + v4))):
                        store8((v6 + (v4 * 286704)) + 286701, 1)
                    v17 = (v4 + 1)
                    if load8u((v7 + ((v4 + 1) + v3))):
                        store8((v6 + (v17 * 286704)) + 286701, 1)
                    v4 = (v4 + 2)
                    v5 = (v5 + 2)
                    if ((v5 + 2) != v2):
                        continue
                    break
            if not v16:
                break
            if not load8u((v7 + (v3 + v4))):
                break
            store8((v6 + (v4 * 286704)) + 286701, 1)
            break
        if not v11:
        func202(arg0, 0, 1)
        if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 34):
            v2 = (v9 + (v8 * 286704))
            store32((v9 + (v8 * 286704)) + 283912, (load32(v2 + 283912) - 1))
        func157(arg0)
        while True:  # $label39
            v7 = (v9 + (v8 * 286704))
            v4 = load32((v9 + (v8 * 286704)) + 281796)
            if not load32((v9 + (v8 * 286704)) + 281796):
                break
            v5 = load32(v4 + 8)
            if not load32(v4 + 8):
                break
            v6 = load32(v4)
            v2 = 0
            v12 = (v9 + (v8 * 286704))
            while True:  # $label42
                v3 = (v6 + (v2 << 2))
                if (load32((v6 + (v2 << 2))) == load32(arg0 + 28)):
                    v3 = ((v12 + (load32(v3 + 4) << 2)) + 282828)
                    store32(((v12 + (load32(v3 + 4) << 2)) + 282828), (load32(v3) - 1))
                    v5 = (load32(v4 + 8) - 1)
                    store32(v4 + 8, (load32(v4 + 8) - 1))
                    v3 = v2
                    if (u32(v5) > u32(v2)):
                        while True:  # $label40
                            v3 = (v3 + 1)
                            store32((v6 + (v3 << 2)), load32((v6 + ((v3 + 1) << 2))))
                            v5 = load32(v4 + 8)
                            if (u32(v3) < u32(load32(v4 + 8))):
                                continue
                            break
                    v5 = (v5 - 1)
                    store32(v4 + 8, (v5 - 1))
                    v3 = v2
                    if (u32(v5) > u32(v2)):
                        while True:  # $label41
                            v3 = (v3 + 1)
                            store32((v6 + (v3 << 2)), load32((v6 + ((v3 + 1) << 2))))
                            v5 = load32(v4 + 8)
                            if (u32(v3) < u32(load32(v4 + 8))):
                                continue
                            break
                    v2 = (v2 - 2)
                v2 = (v2 + 2)
                if (u32((v2 + 2)) < u32(v5)):
                    continue
                break
            break
        while True:  # $label43
            v5 = load32(v7 + 281788)
            if not load32(v7 + 281788):
                break
            v3 = load32(v5 + 8)
            if not load32(v5 + 8):
                break
            v6 = load32(v5)
            v2 = 0
            while True:  # $label45
                if (load32((v6 + (v2 << 2))) == load32(arg0 + 28)):
                    v3 = (v3 - 1)
                    store32(v5 + 8, (v3 - 1))
                    v4 = v2
                    if (u32(v2) < u32(v3)):
                        while True:  # $label44
                            v4 = (v4 + 1)
                            store32((v6 + (v4 << 2)), load32((v6 + ((v4 + 1) << 2))))
                            v3 = load32(v5 + 8)
                            if (u32(v4) < u32(load32(v5 + 8))):
                                continue
                            break
                    v2 = (v2 - 1)
                v2 = (v2 + 1)
                if (u32((v2 + 1)) < u32(v3)):
                    continue
                break
            break
        if not v11:
        v6 = ((v8 * 286704) + v9)
        v5 = (load32(38428) if load16u(arg0 + 120) else load8u(arg0 + 122))
        while True:  # $label48
            while True:  # $label46
                while True:  # $label47
                    # br_table (load8u(arg0 + 125) - 4)
                    break
                    break
                v2 = (((v9 + (v8 * 286704)) + (v5 << 2)) + 281808)
                store32((((v9 + (v8 * 286704)) + (v5 << 2)) + 281808), (load32(v2) - 1))
                store8(arg0 + 125, 3)
                if load16u(arg0 + 110):
                    func387(v6)
                v3 = load32(((v10 * 404) + ENTITY_TYPES) + 176)
                if not load32(((v10 * 404) + ENTITY_TYPES) + 176):
                    break
                v2 = (v9 + (v8 * 286704))
                store32((v9 + (v8 * 286704)) + 283980, (load32(v2 + 283980) - v3))
                v4 = load32(v2 + 283976)
                if (u32(v3) >= u32(-2147483647)):
                    store8(v2 + 286700, 1)
                v2 = (v2 + 281748)
                if (u32(load32((v2 + 281748))) >= u32(v4)):
                    break
                store32(v2, v4)
                break
                break
            v2 = (((v9 + (v8 * 286704)) + (v5 << 2)) + 282828)
            store32((((v9 + (v8 * 286704)) + (v5 << 2)) + 282828), (load32(v2) - 1))
            break
        store8(arg0 + 125, 3)
        if not load8u(9147152):
            func77(arg0)
        while True:  # $label49
            if (load32(CURRENT_PLAYER) != load16u(arg0 + 110)):
                break
            v2 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 180)
            if not load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 180):
                break
            break
        while True:  # $label50
            if (u32(load32(arg0 + 84)) < u32(12)):
                break
            if load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264):
                break
            v2 = (v9 + (v8 * 286704))
            store32((v9 + (v8 * 286704)) + 283936, (load32(v2 + 283936) - 1))
            break
        v2 = (v9 + (v8 * 286704))
        v4 = load32(((v10 * 404) + ENTITY_TYPES) + 280)
        v3 = (load32(v2 + 283976) - load32(((v10 * 404) + ENTITY_TYPES) + 280))
        store32((v9 + (v8 * 286704)) + 283976, (load32(v2 + 283976) - load32(((v10 * 404) + ENTITY_TYPES) + 280)))
        if ((v4 - 1) >= 0):
            store8(v2 + 286700, 1)
        v2 = (v2 + 281748)
        if (u32(v3) > u32(load32((v2 + 281748)))):
            store32(v2, v3)
        while True:  # $label51
            if (v5 != load32(38452)):
                break
            v2 = (v9 + (v8 * 286704))
            if load32((((v9 + (v8 * 286704)) + (v5 << 2)) + 281808)):
                break
            v4 = 0
            store32(((v2 + (load32(39144) << 2)) + 281808), 1)
            store32(v2 + 283868, load32((v2 + 284380)))
            v2 = load32(((v2 + (load32(38636) << 2)) + 284636))
            if not load32(((v2 + (load32(38636) << 2)) + 284636)):
                break
            v3 = load32(v2 + 8)
            if not load32(v2 + 8):
                break
            while True:  # $label52
                v7 = load32((load32(v2) + (v4 << 2)))
                if load32((load32(v2) + (v4 << 2))):
                v4 = (v4 + 1)
                if ((v4 + 1) != v3):
                    continue
                break
            break
        while True:  # $label53
            v2 = (v9 + (v8 * 286704))
            if load32((((v9 + (v8 * 286704)) + (v5 << 2)) + 281808)):
                break
            if (load32(v2 + 283908) != load32(CURRENT_PLAYER)):
                break
            v3 = ((v10 * 404) + ENTITY_TYPES)
            if not load32(((v10 * 404) + ENTITY_TYPES) + 244):
                break
            v2 = 0
            while True:  # $label57
                v11 = load32((load32(v3 + 240) + (v2 << 2)))
                while True:  # $label54
                    if load8u(9147141):
                        break
                    v4 = 0
                    v12 = load32(9671120)
                    if not load32(9671120):
                        break
                    while True:  # $label56
                        while True:  # $label55
                            v7 = load32(((v4 << 2) + 9263072))
                            if not load32(((v4 << 2) + 9263072)):
                                break
                            if (load32(v7 + 12) != v11):
                                break
                            if load8u(v7 + 24):
                                break
                            break
                            break
                        v4 = (v4 + 1)
                        if ((v4 + 1) != v12):
                            continue
                        break
                    break
                v2 = (v2 + 1)
                if (u32((v2 + 1)) < u32(load32(v3 + 244))):
                    continue
                break
            break
        v2 = load32(arg0 + 44)
        if load32(arg0 + 44):
            store32((load32(9215884) + (v2 << 4)), 0)
        store32(arg0 + 64, 0)
        store32(arg0 + 44, 0)
        v2 = load32(9142848)
        store8(arg0 + 122, v5)
        store16(arg0 + 116, 0)
        store32(arg0 + 68, v2)
        while True:  # $label58
            if load8u(9147152):
                break
            v3 = load32(arg0 + 28)
            while True:  # $label59
                v2 = load32((((v9 + (v8 * 286704)) + (v5 << 2)) + 284636))
                if not load32((((v9 + (v8 * 286704)) + (v5 << 2)) + 284636)):
                    break
                v5 = load32(v2 + 8)
                if not load32(v2 + 8):
                    break
                v2 = load32(v2)
                v4 = 0
                while True:  # $label60
                    v8 = (v2 + (v4 << 2))
                    if (v3 != load32((v2 + (v4 << 2)))):
                        v4 = (v4 + 1)
                        if ((v4 + 1) != v5):
                            continue
                        break
                    break
                if (v4 < 0):
                    break
                store32(v8, 0)
                v3 = load32(arg0 + 28)
                break
            func388(v6, v3)
            if (load32(38528) != load8u(arg0 + 122)):
                break
            if load8u(9147152):
                break
            break
        if not load8u(9216060):
            break
        if (load32(v14 + 264) == 2):
            break
        if arg1:
            break
        if load8u(9147152):
            break
        if not load32(((v10 * 404) + ENTITY_TYPES) + 68):
            break
        break
    G.global0 = (v13 + 16)
    return func46(0, 0)

# ----------------------------------------------------------
# $func33
# ----------------------------------------------------------
def func33(arg0, arg1):
    if (arg1 <= 0):
        return 0
    v3 = load32(arg0 + 12)
    v4 = load32(arg0 + 8)
    while True:  # $label1
        while True:  # $label4
            while True:  # $label0
                if (v3 >= 0):
                    break
                v2 = load32(arg0 + 16)
                if not load32(arg0 + 16):
                    break
                if (u32(load32(arg0 + 24)) > u32(v2)):
                    v9 = load64(v2)
                    store32(arg0 + 16, (v2 + 7))
                    store64(arg0, ((load64(arg0) << 56) | ((((((v9 << 56) | ((v9 & 65280) << 40)) | (((v9 & 16711680) << 24) | ((v9 & 4278190080) << 8))) | ((((v9 & 0xFFFFFFFF) >> 40) & 65280) | ((((v9 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v9 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                    break
                while True:  # $label2
                    if (u32(load32(arg0 + 20)) > u32(v2)):
                        store32(arg0 + 16, (v2 + 1))
                        store64(arg0, (load8u(v2) | (load64(arg0) << 8)))
                        break
                    if load32(arg0 + 28):
                        break
                    store32(arg0 + 28, 1)
                    store64(arg0, (load64(arg0) << 8))
                    break
                break
            v2 = (v3 + 8)
            v7 = (arg1 - 1)
            while True:  # $label3
                v5 = (((v4 & 0xFFFFFFFF) >> 1) & 16777215)
                v9 = load64(arg0)
                v10 = i32(v2)
                v8 = i32(((load64(arg0) & 0xFFFFFFFF) >> i32(v2)))
                if (u32((((v4 & 0xFFFFFFFF) >> 1) & 16777215)) < u32(i32(((load64(arg0) & 0xFFFFFFFF) >> i32(v2))))):
                    store64(arg0, (v9 - (i32((v5 + 1)) << v10)))
                    break
                break
            v4 = (v5 + 1)
            v2 = (clz((v5 + 1)) ^ 24)
            v3 = ((v4 - v5) - (clz((v5 + 1)) ^ 24))
            store32(v2 + 12, ((v4 - v5) - (clz((v5 + 1)) ^ 24)))
            v4 = ((v4 << v2) - 1)
            store32(arg0 + 8, ((v4 << v2) - 1))
            v6 = (((u32(v5) < u32(v8)) << v7) | v6)
            v2 = (u32(arg1) > u32(1))
            arg1 = v7
            if v2:
                continue
            break
        return v6
        break
    a_c()
    raise Unreachable()
    return 3339

# ----------------------------------------------------------
# $func34
# ----------------------------------------------------------
def func34(arg0, arg1, arg2, arg3, arg4, arg5):
    while True:  # $label0
        if not load32(9147132):
            v7 = load32(9671136)
            break
        while True:  # $label2
            while True:  # $label1
                v18 = load32(9142848)
                if (load32(9142848) == load32(9671144)):
                    break
                store32(9671148, 3)
                store32(9671144, v18)
                break
            v6 = 3
            v7 = load32(9671136)
            if (u32(3) < u32(load32(9671136))):
                v9 = load32(ENTITIES)
                while True:  # $label3
                    v8 = (v9 + (v6 * 132))
                    if (load8u((v9 + (v6 * 132)) + 125) == 3):
                        if (u32(((v18 - load32(v8 + 68)) * 25)) > u32(70000)):
                            break
                    v6 = (v6 + 1)
                    if ((v6 + 1) != v7):
                        continue
                    break
            store32(9671148, v7)
            break
            break
        store32(9671148, (v6 + 1))
        v7 = v6
        break
    while True:  # $label4
        v19 = ((arg0 * 404) + ENTITY_TYPES)
        if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) == 3):
            break
        v20 = load32(PLAYERS)
        v16 = (arg1 if (arg1 != 2147483647) else 0)
        if not func56(arg2, arg3, v19, (arg1 if (arg1 != 2147483647) else 0), 1, v7, 1, arg5, 0):
            break
        while True:  # $label5
            v18 = (v7 != load32(9671136))
            if not (v7 != load32(9671136)):
                v8 = (v7 + 1)
                store32(9671136, (v7 + 1))
                v6 = load32(9671132)
                if (u32(v8) < u32(load32(9671132))):
                    break
                v6 = (load32(9671140) + v6)
                store32(9671132, (load32(9671140) + v6))
                store32(ENTITIES, func228(load32(ENTITIES), v6, v8))
                break
            v9 = func26(4)
            v6 = (func26(4) + 4)
            v10 = entities[v7]
            v8 = load32(entities[v7])
            if load32(entities[v7]):
                store32(v10 + 4, v8)
            store32(v10 + 8, v6)
            store32(v10 + 4, v9)
            store32(v10, v9)
            # TODO: memory.fill
            break
        v11 = load32(ENTITIES)
        v21 = entities[v7]
        store32(entities[v7].max_hp, v7)
        while True:  # $label8
            while True:  # $label6
                while True:  # $label7
                    if (load32(v19 + 264) != 2):
                        if (load32(((arg0 * 404) + ENTITY_TYPES) + 188) == 55):
                            break
                        if (load32(38500) != arg0):
                            break
                        break
                    if (load32(38500) == arg0):
                        break
                    break
                if (load32(38528) != arg0):
                    break
                break
            store16((v11 + (v7 * 132)) + 110, v16)
            break
        while True:  # $label9
            if (arg1 != 2147483647):
                break
            if (load32(((arg0 * 404) + ENTITY_TYPES) + 188) != 55):
                break
            store8((v11 + (v7 * 132)) + 126, 2)
            break
        v8 = (v11 + (v7 * 132))
        store16((v11 + (v7 * 132)) + 114, arg3)
        store16(v8 + 112, arg2)
        store8(v8 + 122, arg0)
        v6 = ((arg0 * 404) + ENTITY_TYPES)
        arg1 = load32(((arg0 * 404) + ENTITY_TYPES) + 168)
        store8(v8 + 124, (load32(((arg0 * 404) + ENTITY_TYPES) + 168) if arg1 else arg4))
        while True:  # $label10
            if arg5:
                func420(v21)
                v10 = load32(((load8u(v8 + 122) * 72) + 9263856))
                store32(v8 + 64, (load32((((v20 + (v16 * 286704)) + (arg0 * 36)) + 269388)) + load32(v6 + 104)))
                break
            while True:  # $label11
                v6 = load32(v6 + 356)
                if load32(v6 + 356):
                    break
                arg1 = ((arg0 * 404) + ENTITY_TYPES)
                arg4 = load32(((arg0 * 404) + ENTITY_TYPES) + 216)
                arg1 = load32(arg1 + 220)
                arg1 = (load32(((arg0 * 404) + ENTITY_TYPES) + 216) if (u32(arg1) < u32(arg4)) else load32(arg1 + 220))
                arg1 = ((6 if (u32(arg1) >= u32(6)) else (load32(((arg0 * 404) + ENTITY_TYPES) + 216) if (u32(arg1) < u32(arg4)) else load32(arg1 + 220))) - 1)
                if (u32(((6 if (u32(arg1) >= u32(6)) else (load32(((arg0 * 404) + ENTITY_TYPES) + 216) if (u32(arg1) < u32(arg4)) else load32(arg1 + 220))) - 1)) > u32(4)):
                    v6 = 9142636
                    break
                v6 = load32(((arg1 << 2) + 10132))
                break
            v10 = load32(v6)
            arg1 = (v11 + (v7 * 132))
            store8((v11 + (v7 * 132)) + 125, 4)
            store32(arg1 + 64, 1)
            arg1 = (((v20 + (v16 * 286704)) + (arg0 << 2)) + 282828)
            store32((((v20 + (v16 * 286704)) + (arg0 << 2)) + 282828), (load32(arg1) + 1))
            break
        v6 = (v11 + (v7 * 132))
        arg4 = ((arg0 * 404) + ENTITY_TYPES)
        arg1 = ((v20 + (v16 * 286704)) + (arg0 * 36))
        store32((v11 + (v7 * 132)) + 68, (load32(((arg0 * 404) + ENTITY_TYPES) + 108) + load32((((v20 + (v16 * 286704)) + (arg0 * 36)) + 269392))))
        store32(v6 + 52, (load32(arg4 + 92) + load32((arg1 + 269380))))
        store32(v6 + 60, (load32(arg4 + 100) + load32((arg1 + 269384))))
        store32(v6 + 84, (load32(arg4 + 112) + load32((arg1 + 269396))))
        arg1 = (load32(arg4 + 120) + load32((arg1 + 269404)))
        store32(v6 + 72, (load32(arg4 + 120) + load32((arg1 + 269404))))
        store32(v6 + 76, arg1)
        if (arg0 == load32(38528)):
            store32(v6 + 80, 300)
        if (arg0 == load32(38500)):
            v22 = load64(9147316)
            arg4 = load32(9147312)
            store32(9147316, load32(9147312))
            arg1 = load32(9147324)
            store64(9147320, v22)
            arg1 = (arg1 ^ (arg1 << 11))
            arg1 = ((arg4 ^ (((arg4 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1)
            store32(9147312, ((arg4 ^ (((arg4 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1))
            store8(v8 + 124, (arg1 % 9))
        while True:  # $label19
            if load8u(9147213):
                while True:  # $label13
                    while True:  # $label12
                        arg1 = load32(load32(GAME_STATE) + 48)
                        if not load32(load32(GAME_STATE) + 48):
                            break
                        v12 = load32(((arg0 * 404) + ENTITY_TYPES) + 216)
                        if not load32(((arg0 * 404) + ENTITY_TYPES) + 216):
                            break
                        if load8u(9147152):
                            break
                        v14 = load32(9142440)
                        v15 = load32(9147376)
                        while True:  # $label16
                            if (arg1 != 2):
                                v9 = (v12 & -2)
                                v8 = (v12 & 1)
                                v6 = 0
                                while True:  # $label15
                                    v13 = (arg2 + v17)
                                    arg1 = 0
                                    arg4 = 0
                                    if (v12 != 1):
                                        while True:  # $label14
                                            v6 = (((load16u((v15 + ((v13 + (v14 * ((arg1 | 1) + arg3))) << 1))) | load16u((v15 + ((v13 + (v14 * (arg1 + arg3))) << 1)))) != 0) | v6)
                                            arg1 = (arg1 + 2)
                                            arg4 = (arg4 + 2)
                                            if ((arg4 + 2) != v9):
                                                continue
                                            break
                                    if v8:
                                        v6 = ((load16u((v15 + ((v13 + (v14 * (arg1 + arg3))) << 1))) != 0) | v6)
                                    v17 = (v17 + 1)
                                    if ((v17 + 1) != v12):
                                        continue
                                    break
                                break
                            v9 = (v12 & -2)
                            v8 = (v12 & 1)
                            v6 = 0
                            while True:  # $label18
                                v13 = (arg2 + v17)
                                arg1 = 0
                                arg4 = 0
                                if (v12 != 1):
                                    while True:  # $label17
                                        v6 = (((u32(load16u((v15 + ((v13 + (v14 * ((arg1 | 1) + arg3))) << 1)))) > u32(1)) | (u32(load16u((v15 + ((v13 + (v14 * (arg1 + arg3))) << 1)))) > u32(1))) | v6)
                                        arg1 = (arg1 + 2)
                                        arg4 = (arg4 + 2)
                                        if ((arg4 + 2) != v9):
                                            continue
                                        break
                                if v8:
                                    v6 = ((u32(load16u((v15 + ((v13 + (v14 * (arg1 + arg3))) << 1)))) > u32(1)) | v6)
                                v17 = (v17 + 1)
                                if ((v17 + 1) != v12):
                                    continue
                                break
                            break
                        if not (v6 & 1):
                            break
                        break
                    break
                break
            if (load32(v19 + 264) != 2):
                break
            if (load32(((arg0 * 404) + ENTITY_TYPES) + 268) == 1):
                store32(v6 + 52, 1)
                break
            if (load32(38964) != arg0):
                break
            store32((v11 + (v7 * 132)) + 80, ((D(12) * 10) + 10))
            break
        while True:  # $label20
            if not load8u(9147152):
                func240(v21, 500, v18)
                break
            store32((v11 + (v7 * 132)) + 32, -1)
            break
        while True:  # $label21
            arg0 = load32(((arg0 * 404) + ENTITY_TYPES) + 280)
            if load32(((arg0 * 404) + ENTITY_TYPES) + 280):
                arg2 = (v20 + (v16 * 286704))
                arg1 = (load32(arg2 + 283976) + arg0)
                store32((v20 + (v16 * 286704)) + 283976, (load32(arg2 + 283976) + arg0))
                if (arg0 < 0):
                    store8(arg2 + 286700, 1)
                arg0 = (arg2 + 281748)
                if (u32(load32((arg2 + 281748))) >= u32(arg1)):
                    break
                store32(arg0, arg1)
                break
            if (load32(v19 + 264) != 1):
                break
            if arg5:
                break
            store32((v11 + (v7 * 132)) + 88, load32(9142848))
            break
        break
    return v7

# ----------------------------------------------------------
# $func35
# ----------------------------------------------------------
def func35(arg0, arg1, arg2):
    if (u32(arg2) >= u32(512)):
        # TODO: memory.copy
        return arg0
    v4 = (arg0 + arg2)
    while True:  # $label3
        if not ((arg0 ^ arg1) & 3):
            while True:  # $label0
                if not (arg0 & 3):
                    break
                if not arg2:
                    break
                arg2 = (arg0 ^ -1)
                v3 = (arg0 + 1)
                v3 = ((arg0 ^ -1) + (v4 if (u32(v3) < u32(v4)) else (arg0 + 1)))
                arg2 = (arg2 & 3)
                arg2 = ((((arg0 ^ -1) + (v4 if (u32(v3) < u32(v4)) else (arg0 + 1))) if (u32(arg2) > u32(v3)) else (arg2 & 3)) + 1)
                # TODO: memory.copy
                arg1 = (arg1 + arg2)
                break
            arg2 = (arg0 + arg2)
            while True:  # $label1
                v3 = (v4 & -4)
                if (u32((v4 & -4)) < u32(64)):
                    break
                v5 = (v3 + -64)
                if (u32(arg2) > u32((v3 + -64))):
                    break
                while True:  # $label2
                    store32(arg2, load32(arg1))
                    store32(arg2 + 4, load32(arg1 + 4))
                    store32(arg2 + 8, load32(arg1 + 8))
                    store32(arg2 + 12, load32(arg1 + 12))
                    store32(arg2 + 16, load32(arg1 + 16))
                    store32(arg2 + 20, load32(arg1 + 20))
                    store32(arg2 + 24, load32(arg1 + 24))
                    store32(arg2 + 28, load32(arg1 + 28))
                    store32(arg2 + 32, load32(arg1 + 32))
                    store32(arg2 + 36, load32(arg1 + 36))
                    store32(arg2 + 40, load32(arg1 + 40))
                    store32(arg2 + 44, load32(arg1 + 44))
                    store32(arg2 + 48, load32(arg1 + 48))
                    store32(arg2 + 52, load32(arg1 + 52))
                    store32(arg2 + 56, load32(arg1 + 56))
                    store32(arg2 + 60, load32(arg1 + 60))
                    arg1 = (arg1 - -64)
                    arg2 = (arg2 - -64)
                    if (u32((arg2 - -64)) <= u32(v5)):
                        continue
                    break
                break
            if (u32(arg2) >= u32(v3)):
                break
            v5 = (arg2 + 4)
            v3 = ((((arg2 ^ -1) + (v3 if (u32(v3) > u32(v5)) else (arg2 + 4))) & -4) + 4)
            # TODO: memory.copy
            arg1 = (arg1 + v3)
            arg2 = (arg2 + v3)
            break
        if (u32(v4) < u32(4)):
            arg2 = arg0
            break
        v3 = (v4 - 4)
        if (u32(arg0) > u32((v4 - 4))):
            arg2 = arg0
            break
        arg2 = arg0
        while True:  # $label4
            store8(arg2, load8u(arg1))
            store8(arg2 + 1, load8u(arg1 + 1))
            store8(arg2 + 2, load8u(arg1 + 2))
            store8(arg2 + 3, load8u(arg1 + 3))
            arg1 = (arg1 + 4)
            arg2 = (arg2 + 4)
            if (u32((arg2 + 4)) <= u32(v3)):
                continue
            break
        break
    if (u32(arg2) < u32(v4)):
        # TODO: memory.copy
    return arg0

# ----------------------------------------------------------
# $func36
# ----------------------------------------------------------
def func36(arg0):
    while True:  # $label0
        if not arg0:
            break
        v1 = load32(arg0 + 16)
        if not load32(arg0 + 16):
            break
        if (u32(load32(arg0 + 20)) > u32(v1)):
            store32(arg0 + 16, (v1 + 1))
            store32(arg0 + 12, (load32(arg0 + 12) + 8))
            store64(arg0, (load8u(v1) | (load64(arg0) << 8)))
            return
        if not load32(arg0 + 28):
            store32(arg0 + 28, 1)
            store64(arg0, (load64(arg0) << 8))
            store32(arg0 + 12, (load32(arg0 + 12) + 8))
            return
        store32(arg0 + 12, 0)
        return
        break
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func37
# ----------------------------------------------------------
def func37(arg0, arg1, arg2, arg3):
    v5 = (G.global0 - 128)
    G.global0 = (G.global0 - 128)
    while True:  # $label0
        if not arg1:
            break
        v11 = load32(arg0 + 40)
        if not load32(arg0 + 40):
            break
        v12 = load32(9142848)
        store32(arg0 + 48, arg1)
        v10 = load16u(arg0 + 110)
        v4 = load16u(arg0 + 120)
        v7 = load8u(arg0 + 122)
        while True:  # $label1
            if load32(arg0 + 92):
                v8 = 13
                if load8u(9142906):
                    break
            v8 = (((v4 if v4 else v10) & 65535) + 16)
            if not load8u(9142916):
                v4 = load8u(arg0 + 127)
                v10 = ((v7 * 404) + ENTITY_TYPES)
                if not (load8u(arg0 + 127) | load32(((v7 * 404) + ENTITY_TYPES) + 156)):
                    break
                v8 = load32(v10 + 156)
                v8 = (load32(v10 + 156) if v8 else v4)
                break
            v4 = load8u(arg0 + 127)
            v8 = (load8u(arg0 + 127) if v4 else v8)
            break
        v10 = load32(((v7 * 404) + ENTITY_TYPES) + 264)
        v14 = load32(arg1 + 32)
        v15 = load32(arg1 + 24)
        v7 = load32(arg1)
        v16 = load32(arg1 + 16)
        v4 = (load32(arg1 + 16) * load32(arg1 + 20))
        if (load32(arg1 + 16) * load32(arg1 + 20)):
            # TODO: f64.promote_f32
            v20 = i32((load32(arg1 + 4) // v4))
        if not arg3:
            while True:  # $label7
                while True:  # $label3
                    while True:  # $label2
                        if load8u(9147152):
                            v4 = load8u(arg0 + 125)
                            break
                        v4 = load32(CURRENT_PLAYER)
                        if not load32(CURRENT_PLAYER):
                            break
                        if not load8u((load32(9143012) + (load16u(arg0 + 110) + (load32(PLAYER_COUNT) * v4)))):
                            break
                        v4 = load8u(arg0 + 125)
                        if (load8u(arg0 + 125) == 3):
                            break
                        break
                    while True:  # $label6
                        while True:  # $label5
                            while True:  # $label4
                                # br_table (v4 - 4)
                                break
                                break
                            v4 = load8u(arg0 + 122)
                            v6 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
                            v9 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 216)
                            v6 = load32(v6 + 220)
                            break
                            break
                        v4 = load8u(arg0 + 122)
                        break
                    v6 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 200)
                    if not load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 200):
                        break
                    while True:  # $label8
                        v9 = load16u(arg0 + 114)
                        v4 = ((v4 * 404) + ENTITY_TYPES)
                        v9 = load32(arg0 + 48)
                        v18 = ceil(((i32(((load16u(arg0 + 114) + ((load32(((v4 * 404) + ENTITY_TYPES) + 220) & 0xFFFFFFFF) >> 1)) << 5)) - ((i32(v9) * 32.0) - i32(load32(load32(arg0 + 48) + 12)))) * 0.03125))
                        if (abs(ceil(((i32(((load16u(arg0 + 114) + ((load32(((v4 * 404) + ENTITY_TYPES) + 220) & 0xFFFFFFFF) >> 1)) << 5)) - ((i32(v9) * 32.0) - i32(load32(load32(arg0 + 48) + 12)))) * 0.03125))) < 2147483650.0):
                            break
                        break
                    v13 = (-2147483648 * 10)
                    while True:  # $label9
                        v6 = load16u(arg0 + 112)
                        v18 = ceil(((i32(((load16u(arg0 + 112) + ((load32(v4 + 216) & 0xFFFFFFFF) >> 1)) << 5)) - ((i32(v6) * 32.0) - i32(load32(v9 + 8)))) * 0.03125))
                        if (abs(ceil(((i32(((load16u(arg0 + 112) + ((load32(v4 + 216) & 0xFFFFFFFF) >> 1)) << 5)) - ((i32(v6) * 32.0) - i32(load32(v9 + 8)))) * 0.03125))) < 2147483650.0):
                            break
                        break
                    v18 = i32((i32(v18) + ((-2147483648 + v13) << 8)))
                    break
                break
            # TODO: f64.promote_f32
            v21 = v18
        if not load8u(9142916):
            store32(v5 + 112, v11)
            storef64(v5 + 104, v21)
            store64(v5 + 96, -4616189618054758400)
            storef64(v5 + 88, v20)
            # TODO: f64.promote_f32
            storef64(v5 + 80, i32(v7))
            a_b()
        arg2 = (i32((v12 * 25)) if (arg2 == 0.0) else arg2)
        while True:  # $label15
            while True:  # $label14
                while True:  # $label12
                    while True:  # $label13
                        v13 = load32(arg1 + 20)
                        if load32(arg1 + 20):
                            v12 = load8u(arg0 + 124)
                            v11 = load8u(9142916)
                            while True:  # $label11
                                v4 = load32(arg1 + 28)
                                if (load32(arg1 + 28) == 2147483647):
                                    while True:  # $label10
                                        if v11:
                                            v4 = load32(59152)
                                            store32(59152, (load32(59152) + 1))
                                            v6 = load32(9568052)
                                            v9 = load32(arg1)
                                            break
                                        v9 = load32(arg1)
                                        v6 = load32(9568052)
                                        v4 = ((load32(arg1) + load32(9140308)) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                        break
                                    store32(arg1 + 28, v4)
                                    v7 = load32(arg1 + 4)
                                    v17 = load32(9568048)
                                    store32(9568048, (load32(9568048) + 1))
                                    store32(((v17 << 2) + 9563952), arg1)
                                    store32(9568052, (((v9 * (v7 + 2)) << 2) + v6))
                                    if not v11:
                                        break
                                    arg3 = load32(9568056)
                                    store32(arg1 + 56, load32(9568056))
                                    store32(9568056, (arg3 + ((v7 * load32(arg1)) << 2)))
                                    break
                                if v11:
                                    break
                                v7 = load32(arg1 + 4)
                                break
                            arg2 = (arg2 + -0.0)
                            # TODO: i32.div_u
                            v19 = i32((v13 + v4))
                            arg1 = load32(arg0 + 40)
                            break
                        arg2 = (arg2 + -0.0)
                        v4 = 0
                        arg1 = load32(arg0 + 40)
                        if load8u(9142916):
                            break
                        break
                    store32(v5 + 16, ((15 if (v10 == 1) else v8) if arg3 else v8))
                    # TODO: f64.promote_f32
                    storef64(v5 + 24, i32(((((200 if (v14 == 27) else (0 if (v10 & -5) else 100)) + v16) << 16) + v15)))
                    store32(v5 + 32, arg1)
                    # TODO: f64.promote_f32
                    storef64(v5 + 8, arg2)
                    # TODO: f64.promote_f32
                    storef64(v5, (v19 / i32(load32(59156))))
                    a_b()
                    break
                    break
                arg2 = (arg2 + -0.0)
                v4 = (v4 + (v12 << 16))
                break
            store32(v5, load32(arg0 + 40))
            store32(v5 + 48, v4)
            # TODO: f64.promote_f32
            storef64(v5 + 56, arg2)
            a_b()
            break
        if load8u(9142916):
            break
        break
    G.global0 = (v5 + 128)
    return func60(arg0, 1.0)

# ----------------------------------------------------------
# $func38
# ----------------------------------------------------------
def func38(arg0):
    v3 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # $label1
        if (u32(arg0) >= u32(1073741823)):
            v5 = (arg0 - 1073741823)
            while True:  # $label0
                v1 = load32(9299896)
                if (load32(9299896) != load32(9299892)):
                    v2 = load32(9299888)
                    break
                v2 = (load32(9299900) + v1)
                store32(9299892, (load32(9299900) + v1))
                v4 = load32(9299888)
                v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                if v1:
                    # TODO: memory.copy
                if v4:
                    v1 = load32(9299896)
                store32(9299888, v2)
                break
            store32(9299896, (v1 + 1))
            store32((v2 + (v1 << 2)), v5)
            break
        while True:  # $label2
            v1 = load32(9299880)
            if (load32(9299880) != load32(9299876)):
                v2 = load32(9299872)
                break
            v2 = (load32(9299884) + v1)
            store32(9299876, (load32(9299884) + v1))
            v4 = load32(9299872)
            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
            if v1:
                # TODO: memory.copy
            if v4:
                v1 = load32(9299880)
            store32(9299872, v2)
            break
        store32(9299880, (v1 + 1))
        store32((v2 + (v1 << 2)), arg0)
        break
    while True:  # $label3
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
    G.global0 = (v3 + 48)

# ----------------------------------------------------------
# $func39
# ----------------------------------------------------------
def func39(arg0, arg1):
    while True:  # $label3
        if (arg1 >= 0):
            while True:  # $label4
                while True:  # $label5
                    while True:  # $label0
                        if (u32(arg1) > u32(24)):
                            break
                        if load32(arg0 + 24):
                            break
                        v5 = (arg0 + 20)
                        v6 = load32(arg0 + 20)
                        v2 = (load32(arg0 + 20) + arg1)
                        store32((arg0 + 20), (load32(arg0 + 20) + arg1))
                        v7 = load32(((arg1 << 2) + 17888))
                        v11 = load64(arg0)
                        while True:  # $label1
                            if (v2 <= 7):
                                v4 = load32(arg0 + 12)
                                v3 = load32(arg0 + 16)
                                break
                            arg1 = load32(arg0 + 16)
                            v4 = load32(arg0 + 12)
                            v3 = (load32(arg0 + 16) if (u32(arg1) > u32(v4)) else load32(arg0 + 12))
                            v10 = v11
                            while True:  # $label2
                                if (arg1 == v3):
                                    break
                                v10 = ((v10 & 0xFFFFFFFF) >> 8)
                                store64(arg0, ((v10 & 0xFFFFFFFF) >> 8))
                                v12 = load8u((load32(arg0 + 8) + arg1))
                                v8 = (v2 - 8)
                                store32(arg0 + 20, (v2 - 8))
                                arg1 = (arg1 + 1)
                                store32(arg0 + 16, (arg1 + 1))
                                v10 = ((v12 << 56) | v10)
                                store64(arg0, ((v12 << 56) | v10))
                                v9 = (v2 > 15)
                                v2 = v8
                                if v9:
                                    continue
                                break
                            v3 = arg1
                            break
                        if (u32(v3) > u32(v4)):
                            break
                        arg1 = (v7 & i32(((v11 & 0xFFFFFFFF) >> i32((v6 & 63)))))
                        if (v3 != v4):
                            break
                        if (v2 < 65):
                            break
                        store32(arg0 + 24, 1)
                        break
                        break
                    store32(arg0 + 24, 1)
                    v5 = (arg0 + 20)
                    arg1 = 0
                    break
                store32(v5, 0)
                break
            return arg1
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()
    return 3953

# ----------------------------------------------------------
# $func40
# ----------------------------------------------------------
def func40(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15):
    v16 = (G.global0 - 320)
    G.global0 = (G.global0 - 320)
    while True:  # $label0
        if load8u(9142917):
            break
        if load8u(9142916):
            arg12 = 0
            arg14 = 0
            if (u32(arg10) <= u32(14)):
                arg10 = (arg10 << 4)
                arg14 = ((((load32(((arg10 << 4) + 1748)) << 8) + load32((arg10 + 1744))) + (load32((arg10 + 1752)) << 16)) + (load32((arg10 + 1756)) << 24))
            while True:  # $label1
                if not arg9:
                    break
                if not load32(arg9 + 20):
                    break
                arg10 = load32(arg9 + 28)
                if (load32(arg9 + 28) == 2147483647):
                    arg10 = load32(59152)
                    store32(59152, (load32(59152) + 1))
                    v17 = load32(9568052)
                    store32(arg9 + 28, arg10)
                    v18 = load32(arg9)
                    arg12 = load32(arg9 + 4)
                    v19 = load32(9568048)
                    store32(9568048, (load32(9568048) + 1))
                    store32(((v19 << 2) + 9563952), arg9)
                    store32(9568052, (v17 + ((v18 * (arg12 + 2)) << 2)))
                    v17 = load32(9568056)
                    store32(arg9 + 56, load32(9568056))
                    store32(9568056, (v17 + ((arg12 * load32(arg9)) << 2)))
                arg12 = (arg10 + (arg13 << 16))
                break
            arg9 = (load32(9142848) * 25)
            if (arg2 > 0.0):
                arg2 = (((arg2 * 0.5) / i32((load32(9142440) * 96))) + 0.25)
            store32(v16 + 316, arg11)
            store64(v16 + 308, 65535)
            store32(v16 + 304, arg14)
            # TODO: f64.promote_f32
            storef64(v16 + 296, arg8)
            store32(v16 + 292, arg9)
            store32(v16 + 288, arg12)
            # TODO: f64.promote_f32
            storef64(v16 + 280, arg5)
            # TODO: f64.promote_f32
            storef64(v16 + 272, arg4)
            # TODO: f64.promote_f32
            storef64(v16 + 264, arg3)
            # TODO: f64.promote_f32
            storef64(v16 + 256, arg2)
            # TODO: f64.promote_f32
            storef64(v16 + 248, arg1)
            # TODO: f64.promote_f32
            storef64(v16 + 240, arg0)
            a_b()
            break
        arg8 = (arg8 if (arg8 != 0.0) else -1.0)
        while True:  # $label2
            if not ((arg6 == 0.0) & (arg7 == 0.0)):
                arg6 = neg(arg6)
                # TODO: f64.promote_f32
                break
            arg6 = i32(load32(arg9))
            v17 = (load32(arg9 + 20) * load32(arg9 + 16))
            if not (load32(arg9 + 20) * load32(arg9 + 16)):
                break
            # TODO: f64.promote_f32
            break
        v26 = i32((load32(arg9 + 4) // v17))
        store32(v16 + 224, arg11)
        # TODO: f64.promote_f32
        storef64(v16 + 216, arg15)
        # TODO: f64.promote_f32
        storef64(v16 + 208, arg8)
        storef64(v16 + 200, v26)
        # TODO: f64.promote_f32
        storef64(v16 + 192, arg6)
        a_b()
        v17 = load8u(9142916)
        arg6 = i32(load32(arg9 + 12))
        arg7 = i32(load32(arg9 + 8))
        while True:  # $label3
            if (arg2 == -55.0):
                break
            if not v17:
                break
            arg2 = (((arg2 * 0.5) / i32((load32(9142440) * 96))) + 0.25)
            break
        store32(v16 + 184, arg11)
        # TODO: f64.promote_f32
        storef64(v16 + 176, arg2)
        # TODO: f64.promote_f32
        storef64(v16 + 168, (arg1 - (0.0 if v17 else arg6)))
        # TODO: f64.promote_f32
        storef64(v16 + 160, (arg0 - (0.0 if v17 else arg7)))
        a_b()
        # TODO: f64.promote_f32
        v26 = arg5
        # TODO: f64.promote_f32
        v27 = arg4
        # TODO: f64.promote_f32
        v28 = arg3
        while True:  # $label4
            if load8u(9142916):
                store32(v16 + 152, arg11)
                storef64(v16 + 144, v26)
                storef64(v16 + 136, v27)
                storef64(v16 + 128, v28)
                a_b()
                break
            storef64(v16 + 96, v26)
            store32(v16 + 112, arg11)
            # TODO: f64.promote_f32
            storef64(v16 + 104, i32((load32(9142848) * 25)))
            storef64(v16 + 80, v28)
            storef64(v16 + 88, v27)
            a_b()
            break
        if not arg14:
            v19 = load32(arg9 + 24)
        v22 = load32(arg9 + 16)
        v23 = load32(arg9 + 32)
        while True:  # $label9
            while True:  # $label7
                while True:  # $label8
                    v24 = load32(arg9 + 20)
                    if load32(arg9 + 20):
                        v18 = load8u(9142916)
                        while True:  # $label6
                            arg14 = load32(arg9 + 28)
                            if (load32(arg9 + 28) == 2147483647):
                                while True:  # $label5
                                    if v18:
                                        arg14 = load32(59152)
                                        store32(59152, (load32(59152) + 1))
                                        v20 = load32(9568052)
                                        v21 = load32(arg9)
                                        break
                                    v21 = load32(arg9)
                                    v20 = load32(9568052)
                                    arg14 = ((load32(arg9) + load32(9140308)) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                    break
                                store32(arg9 + 28, arg14)
                                v17 = load32(arg9 + 4)
                                v25 = load32(9568048)
                                store32(9568048, (load32(9568048) + 1))
                                store32(((v25 << 2) + 9563952), arg9)
                                store32(9568052, (((v21 * (v17 + 2)) << 2) + v20))
                                if not v18:
                                    break
                                arg10 = load32(9568056)
                                store32(arg9 + 56, load32(9568056))
                                store32(9568056, (arg10 + ((v17 * load32(arg9)) << 2)))
                                break
                            if v18:
                                break
                            v17 = load32(arg9 + 4)
                            break
                        arg2 = i32((load32(9142848) * 25))
                        # TODO: i32.div_u
                        break
                    arg9 = 0
                    arg2 = i32((load32(9142848) * 25))
                    if load8u(9142916):
                        break
                    break
                arg8 = 0.0
                store32(v16 + 16, arg10)
                # TODO: f64.promote_f32
                storef64(v16 + 24, i32(((((200 if (v23 == 27) else (arg12 * 100)) + v22) << 16) + v19)))
                store32(v16 + 32, arg11)
                # TODO: f64.promote_f32
                storef64(v16 + 8, arg2)
                # TODO: f64.promote_f32
                storef64(v16, (arg8 / i32(load32(59156))))
                a_b()
                break
                break
            arg9 = (arg14 + (arg13 << 16))
            break
        arg2 = i32((load32(9142848) * 25))
        store32((v16 - -64), arg11)
        store32(v16 + 48, arg9)
        # TODO: f64.promote_f32
        storef64(v16 + 56, arg2)
        a_b()
        break
    G.global0 = (v16 + 320)
    return (v16 + 48)

# ----------------------------------------------------------
# $func41
# ----------------------------------------------------------
def func41(arg0, arg1, arg2, arg3, arg4):
    v8 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # $label0
        v5 = load8u(9147125)
        if not (load8u(9142388) if load8u(9147125) else 0):
            v7 = ((arg2 + arg4) + 5)
            v6 = func26((-1 if (u32(v7) > u32(1073741823)) else (((arg2 + arg4) + 5) << 2)))
            store32(func26((-1 if (u32(v7) > u32(1073741823)) else (((arg2 + arg4) + 5) << 2))) + 16, arg4)
            store32(v6 + 12, arg2)
            store32(v6 + 8, arg0)
            store64(v6, 0)
            if arg2:
                # TODO: memory.copy
            if arg4:
                # TODO: memory.copy
            if not v5:
                store32(v8 + 4, v7)
                store32(v8, v6)
                break
            arg1 = load32((PLAYER_COUNT if load8u(9147212) else 41092))
            if (u32(load32((PLAYER_COUNT if load8u(9147212) else 41092))) >= u32(2)):
                arg0 = load32(PLAYERS)
                v5 = 1
                while True:  # $label1
                    arg2 = load32((arg0 + (v5 * 286704)) + 284616)
                    if load32((arg0 + (v5 * 286704)) + 284616):
                        store32(v8 + 24, arg2)
                        store32(v8 + 20, v7)
                        store32(v8 + 16, v6)
                        arg0 = load32(PLAYERS)
                    v5 = (v5 + 1)
                    if ((v5 + 1) != arg1):
                        continue
                    break
            break
        if load8u(9140304):
            break
        v9 = load32(9142384)
        while True:  # $label2
            v5 = load32(9561704)
            if (load32(9561704) != load32(9561700)):
                v6 = load32(9561696)
                break
            v6 = (load32(9561708) + v5)
            store32(9561700, (load32(9561708) + v5))
            v7 = load32(9561696)
            v6 = func26((-1 if (u32(v6) > u32(1073741823)) else (v6 << 2)))
            if v5:
                # TODO: memory.copy
            if v7:
                v5 = load32(9561704)
            store32(9561696, v6)
            break
        store32(9561704, (v5 + 1))
        store32((v6 + (v5 << 2)), v9)
        while True:  # $label3
            v5 = load32(9561704)
            if (load32(9561704) != load32(9561700)):
                v7 = v6
                break
            v7 = (load32(9561708) + v5)
            store32(9561700, (load32(9561708) + v5))
            v7 = func26((-1 if (u32(v7) > u32(1073741823)) else (v7 << 2)))
            if v5:
                # TODO: memory.copy
            store32(9561696, v7)
            v5 = load32(9561704)
            break
        store32(9561704, (v5 + 1))
        store32((v7 + (v5 << 2)), arg0)
        while True:  # $label4
            v5 = load32(9561704)
            if (load32(9561704) != load32(9561700)):
                v6 = v7
                break
            arg0 = (load32(9561708) + v5)
            store32(9561700, (load32(9561708) + v5))
            v6 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if v5:
                # TODO: memory.copy
            store32(9561696, v6)
            v5 = load32(9561704)
            break
        store32(9561704, (v5 + 1))
        store32((v6 + (v5 << 2)), arg2)
        while True:  # $label5
            v5 = load32(9561704)
            if (load32(9561704) != load32(9561700)):
                arg0 = v6
                break
            arg0 = (load32(9561708) + v5)
            store32(9561700, (load32(9561708) + v5))
            arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if v5:
                # TODO: memory.copy
            store32(9561696, arg0)
            v5 = load32(9561704)
            break
        store32(9561704, (v5 + 1))
        store32((arg0 + (v5 << 2)), arg4)
        if arg2:
            v6 = 0
            while True:  # $label6
                v9 = load32((arg1 + (v6 << 2)))
                v5 = load32(9561704)
                if (load32(9561704) == load32(9561700)):
                    v7 = (load32(9561708) + v5)
                    store32(9561700, (load32(9561708) + v5))
                    v7 = func26((-1 if (u32(v7) > u32(1073741823)) else (v7 << 2)))
                    if v5:
                        # TODO: memory.copy
                    store32(9561696, v7)
                    v5 = load32(9561704)
                    arg0 = v7
                store32(9561704, (v5 + 1))
                store32((arg0 + (v5 << 2)), v9)
                v6 = (v6 + 1)
                if ((v6 + 1) != arg2):
                    continue
                break
        if not arg4:
            break
        v6 = 0
        while True:  # $label7
            arg2 = load32((arg3 + (v6 << 2)))
            v5 = load32(9561704)
            if (load32(9561704) == load32(9561700)):
                arg1 = (load32(9561708) + v5)
                store32(9561700, (load32(9561708) + v5))
                arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
                if v5:
                    # TODO: memory.copy
                store32(9561696, arg1)
                v5 = load32(9561704)
                arg0 = arg1
            store32(9561704, (v5 + 1))
            store32((arg0 + (v5 << 2)), arg2)
            v6 = (v6 + 1)
            if ((v6 + 1) != arg4):
                continue
            break
        break
    G.global0 = (v8 + 32)

# ----------------------------------------------------------
# $func42
# ----------------------------------------------------------
def func42():
    func313(3421)
    raise Unreachable()

# ----------------------------------------------------------
# $func43
# ----------------------------------------------------------
def func43(arg0, arg1, arg2):
    while True:  # $label0
        if not arg1:
            break
        v3 = (arg0 ^ -1)
        if (u32(arg2) >= u32(23)):
            while True:  # $label1
                if not (arg1 & 3):
                    break
                v3 = (load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                v5 = (arg1 + 1)
                while True:  # $label2
                    arg0 = (arg2 - 1)
                    if not (arg2 - 1):
                        break
                    if not (v5 & 3):
                        break
                    v3 = (load32(((((load8u(arg1 + 1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                    v5 = (arg1 + 2)
                    while True:  # $label3
                        arg0 = (arg2 - 2)
                        if not (arg2 - 2):
                            break
                        if not (v5 & 3):
                            break
                        v3 = (load32(((((load8u(arg1 + 2) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                        v5 = (arg1 + 3)
                        while True:  # $label4
                            arg0 = (arg2 - 3)
                            if not (arg2 - 3):
                                break
                            if not (v5 & 3):
                                break
                            v3 = (load32(((((load8u(arg1 + 3) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                            arg1 = (arg1 + 4)
                            arg2 = (arg2 - 4)
                            break
                            break
                        arg2 = arg0
                        arg1 = v5
                        break
                        break
                    arg2 = arg0
                    arg1 = v5
                    break
                    break
                arg2 = arg0
                arg1 = v5
                break
            # TODO: i32.div_u
            arg0 = 20
            v11 = (20 * -20)
            while True:  # $label5
                v10 = (arg0 - 1)
                if not (arg0 - 1):
                    break
                v5 = ((arg0 * 20) - 20)
                arg0 = arg1
                while True:  # $label6
                    v4 = (load32(arg0 + 16) ^ v9)
                    v9 = (load32((((((load32(arg0 + 16) ^ v9) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ load32((((v4 & 255) << 2) + 19248)))))
                    v4 = (load32(arg0 + 12) ^ v8)
                    v8 = (load32((((((load32(arg0 + 12) ^ v8) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ load32((((v4 & 255) << 2) + 19248)))))
                    v4 = (load32(arg0 + 8) ^ v6)
                    v6 = (load32((((((load32(arg0 + 8) ^ v6) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ load32((((v4 & 255) << 2) + 19248)))))
                    v4 = (load32(arg0 + 4) ^ v7)
                    v7 = (load32((((((load32(arg0 + 4) ^ v7) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ load32((((v4 & 255) << 2) + 19248)))))
                    v4 = (load32(arg0) ^ v3)
                    v3 = (load32((((((load32(arg0) ^ v3) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ load32((((v4 & 255) << 2) + 19248)))))
                    arg0 = (arg0 + 20)
                    v10 = (v10 - 1)
                    if (v10 - 1):
                        continue
                    break
                arg1 = (arg1 + v5)
                break
            arg2 = (arg2 + v11)
            arg0 = (load32(arg1) ^ v3)
            arg0 = ((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = (((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8))
            arg0 = (((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = (((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8))
            arg0 = (((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = (((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8))
            arg0 = (((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = (((((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((load32(arg1 + 16) ^ (load32(((((((((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v9)) ^ ((arg0 & 0xFFFFFFFF) >> 8))
            arg0 = (((((load32(arg1 + 16) ^ (load32(((((((((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v9)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((((((((load32(arg1 + 16) ^ (load32(((((((((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v9)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = (((((((((((load32(arg1 + 16) ^ (load32(((((((((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v9)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            v3 = ((((((((((((((load32(arg1 + 16) ^ (load32(((((((((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v9)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg1 = (arg1 + 20)
        if (u32(arg2) > u32(7)):
            while True:  # $label7
                arg0 = (load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                arg0 = ((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224)))
                arg0 = (((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 2) ^ arg0) & 255) << 2) + 18224)))
                arg0 = ((((((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 2) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 3) ^ arg0) & 255) << 2) + 18224)))
                arg0 = (((((((((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 2) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 3) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 4) ^ arg0) & 255) << 2) + 18224)))
                arg0 = ((((((((((((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 2) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 3) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 4) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 5) ^ arg0) & 255) << 2) + 18224)))
                arg0 = (((((((((((((((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 2) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 3) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 4) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 5) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 6) ^ arg0) & 255) << 2) + 18224)))
                v3 = ((((((((((((((((((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 2) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 3) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 4) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 5) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 6) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 7) ^ arg0) & 255) << 2) + 18224)))
                arg1 = (arg1 + 8)
                arg2 = (arg2 - 8)
                if (u32((arg2 - 8)) > u32(7)):
                    continue
                break
        while True:  # $label8
            if not arg2:
                break
            if (arg2 & 1):
                v3 = (load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                arg1 = (arg1 + 1)
            else:
            arg0 = arg2
            if (arg2 == 1):
                break
            while True:  # $label9
                arg2 = (load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                v3 = (load32((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) ^ load8u(arg1 + 1)) & 255) << 2) + 18224)) ^ ((arg2 & 0xFFFFFFFF) >> 8))
                arg1 = (arg1 + 2)
                arg0 = (arg0 - 2)
                if (arg0 - 2):
                    continue
                break
            break
        break
    return (v3 ^ -1)

# ----------------------------------------------------------
# $func44
# ----------------------------------------------------------
def func44(arg0, arg1):
    v3 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if load32(arg0 + 92):
            break
        v2 = load32(9213808)
        if (u32(load32(9213808)) > u32(9999)):
            break
        if (load8u(arg0 + 125) == 3):
            break
        if not arg1:
            arg1 = load32(arg0 + 28)
            store32(9213808, (v2 + 1))
            store32(((v2 << 2) + 9173808), arg1)
        arg1 = 1
        while True:  # $label1
            if (load8u(9142906) | load8u(9142916)):
                break
            arg1 = 0
            if load8u(9142917):
                break
            arg1 = load32(9299880)
            if load32(9299880):
                arg1 = (arg1 - 1)
                store32(9299880, (arg1 - 1))
                arg1 = load32((load32(9299872) + (arg1 << 2)))
                break
            arg1 = load32(9163776)
            v2 = (load32(9163776) + 1)
            store32(9163776, (load32(9163776) + 1))
            v4 = load32(9163784)
            if (u32(v2) < u32(load32(9163784))):
                break
            store32(v3, v4)
            a_b()
            store32(9163784, (load32(9163784) + 40000))
            break
        store32(arg0 + 92, arg1)
        if not load32(arg0 + 36):
        func203(arg0)
        break
    G.global0 = (v3 + 16)

# ----------------------------------------------------------
# $func45
# ----------------------------------------------------------
def func45():
    if load32(9213808):
        while True:  # $label0
            v1 = ((v0 << 2) + 9173808)
            func47(entities[load32(((v0 << 2) + 9173808))])
            store32(v1, 0)
            v0 = (v0 + 1)
            if (u32((v0 + 1)) < u32(load32(9213808))):
                continue
            break
    v0 = 0
    store32(40604, -1)
    store32(9140316, 0)
    store32(9213808, 0)
    store32(9140320, 0)
    while True:  # $label1
        if not load32(9142396):
            break
        while True:  # $label2
            func38(load32((load32(9142392) + (v0 << 2))))
            v0 = (v0 + 1)
            if (u32((v0 + 1)) < u32(load32(9142396))):
                continue
            break
        store32(9142396, 0)
        v0 = load32(9142392)
        if not load32(9142392):
            break
        break
    while True:  # $label3
        if not load32(9671176):
            break
        if load32(9671192):
            v0 = 0
            while True:  # $label4
                func38(load32((load32(9671184) + (v0 << 2))))
                v0 = (v0 + 1)
                if (u32((v0 + 1)) < u32(load32(9671192))):
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

# ----------------------------------------------------------
# $func46
# ----------------------------------------------------------
def func46(arg0, arg1):
    v4 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    a_b()
    store32(9681836, 0)
    store8(9147141, 0)
    while True:  # $label0
        v3 = load32(9671120)
        if not load32(9671120):
            break
        if not load8u(59186):
            while True:  # $label10
                v2 = load32(((v5 << 2) + 9263072))
                store8(load32(((v5 << 2) + 9263072)) + 20, 1)
                v9 = ((load32(v2 + 128) != 0) + v9)
                if not v6:
                    v7 = 0
                    while True:  # $label9
                        while True:  # $label1
                            v15 = load32(9215968)
                            if load32(9215968):
                                v16 = load32(PLAYERS)
                                v17 = load32(9215960)
                                while True:  # $label8
                                    if load8u(v2 + 22):
                                        break
                                    v8 = (v16 + (load32((v17 + (v7 << 2))) * 286704))
                                    v6 = load32(v2 + 4)
                                    v18 = load8u(v2 + 23)
                                    while True:  # $label2
                                        if load8u(v2 + 21):
                                            break
                                        while True:  # $label4
                                            while True:  # $label3
                                                if not v18:
                                                    break
                                                if (load32(((v6 * 404) + ENTITY_TYPES) + 264) != 3):
                                                    break
                                                if load32(((v8 + (v6 << 2)) + 281808)):
                                                    break
                                                break
                                            v21 = load32(v2 + 68)
                                            if not load32(v2 + 68):
                                                break
                                            v10 = 0
                                            v3 = 1
                                            v11 = 0
                                            v13 = 0
                                            while True:  # $label7
                                                v14 = load32((v2 + (v10 << 2)) + 28)
                                                v19 = load32(((load32((v2 + (v10 << 2)) + 28) * 404) + ENTITY_TYPES) + 264)
                                                v20 = (load32(((load32((v2 + (v10 << 2)) + 28) * 404) + ENTITY_TYPES) + 264) == 1)
                                                while True:  # $label6
                                                    while True:  # $label5
                                                        v14 = load32(((v8 + (v14 << 2)) + 281808))
                                                        if (load32(((v8 + (v14 << 2)) + 281808)) == 1):
                                                            break
                                                        v3 = ((v19 != 3) & v3)
                                                        if v14:
                                                            break
                                                        v3 = ((v19 != 0) & v3)
                                                        break
                                                        break
                                                    v13 = (v13 | v20)
                                                    break
                                                v11 = (v11 | v20)
                                                v10 = (v10 + 1)
                                                if ((v10 + 1) != v21):
                                                    continue
                                                break
                                            break
                                        if (((v3 & v13) if (v11 & 1) else v3) & 1):
                                            break
                                        if (u32((load32(9671124) - 95)) > u32(1)):
                                            break
                                        break
                                    if v18:
                                        if load8u(((v6 * 404) + ENTITY_TYPES) + 354):
                                            break
                                    v3 = ((v6 * 404) + ENTITY_TYPES)
                                    if (load32(((v6 * 404) + ENTITY_TYPES) + 264) == 1):
                                        if (u32(func180(v8, v6)) >= u32(load32(v3 + 204))):
                                            break
                                        v17 = load32(9215960)
                                        v16 = load32(PLAYERS)
                                        v15 = load32(9215968)
                                    v7 = (v7 + 1)
                                    if (u32((v7 + 1)) < u32(v15)):
                                        continue
                                    break
                            break
                            break
                        store8(v2 + 20, 0)
                        break
                    v6 = load8u(59186)
                    v3 = load32(9671120)
                v5 = (v5 + 1)
                if (u32((v5 + 1)) < u32(v3)):
                    continue
                break
            break
        v2 = (v3 & 1)
        if (v3 != 1):
            v6 = (v3 & -2)
            v3 = 0
            while True:  # $label11
                v7 = (v5 << 2)
                v8 = load32(((v5 << 2) + 9263072))
                store8(load32(((v5 << 2) + 9263072)) + 20, 1)
                v8 = load32(v8 + 128)
                v7 = load32(((v7 | 4) + 9263072))
                store8(load32(((v7 | 4) + 9263072)) + 20, 1)
                v9 = ((v9 + (v8 != 0)) + (load32(v7 + 128) != 0))
                v5 = (v5 + 2)
                v3 = (v3 + 2)
                if ((v3 + 2) != v6):
                    continue
                break
        if not v2:
            break
        v2 = load32(((v5 << 2) + 9263072))
        store8(load32(((v5 << 2) + 9263072)) + 20, 1)
        v9 = (v9 + (load32(v2 + 128) != 0))
        break
    while True:  # $label12
        v5 = load32(9147120)
        if not load32(9147120):
            break
        while True:  # $label14
            v2 = ((load32(9143000) * v5) + v12)
            if (u32(((load32(9143000) * v5) + v12)) >= u32(load32(9671120))):
                break
            while True:  # $label13
                v2 = load32(((v2 << 2) + 9263072))
                if not load8u(load32(((v2 << 2) + 9263072)) + 23):
                    v6 = 0
                    break
                v5 = ((load32(v2 + 4) * 404) + ENTITY_TYPES)
                v6 = (load32(((load32(v2 + 4) * 404) + ENTITY_TYPES) + 264) == 3)
                break
            v5 = load8u(v5 + 354)
            v3 = load8u(v2 + 20)
            v7 = load32(v2 + 8)
            v8 = load8u(v2 + 24)
            v10 = load32(v2 + 12)
            v11 = load32(v2 + 124)
            v2 = load32(v2 + 128)
            store32(v4 + 32, 0)
            store32(v4 + 36, v5)
            store32(v4 + 40, v2)
            store32(v4 + 44, v6)
            store32(v4 + 48, v11)
            store32(v4 + 52, v9)
            store32(v4 + 56, v10)
            store32(v4 + 60, v8)
            store32(v4 + 20, v7)
            store32(v4 + 24, v3)
            store32(v4 + 16, v12)
            store32(v4 + 28, load32(((v12 << 2) + 9147392)))
            a_b()
            v12 = (v12 + 1)
            v5 = load32(9147120)
            if (u32((v12 + 1)) < u32(load32(9147120))):
                continue
            break
        break
    if arg1:
        store32(v4, load32(9143000))
        store32(v4 + 4, (arg0 if arg0 else load32(9671120)))
        a_b()
    store8(9684768, 0)
    G.global0 = (v4 - -64)
    return v4

# ----------------------------------------------------------
# $func47
# ----------------------------------------------------------
def func47(arg0):
    v2 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # $label0
        if load8u(9142906):
            v3 = load32(arg0 + 40)
            if not load32(arg0 + 40):
                break
            v1 = load8u(arg0 + 127)
            v1 = (load8u(arg0 + 127) if v1 else 16)
            if load8u(9142916):
                if (u32(v1) <= u32(15)):
                    v1 = (v1 << 4)
                    v4 = ((((load32(((v1 << 4) + 1748)) << 8) + load32((v1 + 1744))) + (load32((v1 + 1752)) << 16)) + (load32((v1 + 1756)) << 24))
                store32(v2 + 36, v3)
                store32(v2 + 32, v4)
                a_b()
                break
            store32(v2 + 20, v3)
            store32(v2 + 16, v1)
            a_b()
            break
        if load8u(9142916):
            v1 = load32(arg0 + 40)
            if not load32(arg0 + 40):
                break
            v3 = load8u(arg0 + 125)
            store32(v2 + 4, v1)
            store32(v2, (v3 << 8))
            a_b()
            break
        while True:  # $label1
            v1 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
            if (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264) != 1):
                break
            if (u32(load32(v1 + 216)) < u32(2)):
                break
            v4 = load32(arg0 + 12)
            if not load32(arg0 + 12):
                break
            v5 = load32(v4 + 8)
            if not load32(v4 + 8):
                break
            v1 = 0
            while True:  # $label3
                v3 = (load32(v4) + (v1 << 2))
                if (load32((load32(v4) + (v1 << 2)) + 4) == 1):
                    func38(load32(v3))
                    v4 = load32(arg0 + 12)
                    v5 = (load32(v4 + 8) - 2)
                    store32(load32(arg0 + 12) + 8, (load32(v4 + 8) - 2))
                    if (u32(v1) < u32(v5)):
                        v6 = load32(v4)
                        v3 = v1
                        while True:  # $label2
                            v5 = (v6 + (v3 << 2))
                            store32((v6 + (v3 << 2)), load32(v5 + 8))
                            v3 = (v3 + 1)
                            v5 = load32(v4 + 8)
                            if (u32((v3 + 1)) < u32(load32(v4 + 8))):
                                continue
                            break
                    v1 = (v1 - 2)
                v1 = (v1 + 2)
                if (u32((v1 + 2)) < u32(v5)):
                    continue
                break
            break
            break
        func38(load32(arg0 + 92))
        break
    store32(arg0 + 92, 0)
    while True:  # $label4
        v1 = load32(arg0 + 80)
        if not load32(arg0 + 80):
            break
        if (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264) != 1):
            break
        func38(v1)
        store32(arg0 + 80, 0)
        break
    G.global0 = (v2 + 48)

# ----------------------------------------------------------
# $func48
# ----------------------------------------------------------
def func48(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        # TODO: i32.reinterpret_f32
        v3 = arg0
        v2 = (arg0 & 2147483647)
        if (u32((arg0 & 2147483647)) <= u32(1061752794)):
            if (u32(v2) < u32(964689920)):
                break
            # TODO: f64.promote_f32
            arg0 = func75(arg0)
            break
        if (u32(v2) <= u32(1081824209)):
            # TODO: f64.promote_f32
            v4 = arg0
            if (u32(v2) <= u32(1075235811)):
                if (v3 < 0):
                    arg0 = neg(func76((v4 + 1.5707963267948966)))
                    break
                arg0 = func76((v4 + -1.5707963267948966))
                break
            arg0 = func75(neg(((-3.141592653589793 if (v3 >= 0) else 3.141592653589793) + v4)))
            break
        if (u32(v2) <= u32(1088565717)):
            if (u32(v2) <= u32(1085271519)):
                # TODO: f64.promote_f32
                v4 = arg0
                if (v3 < 0):
                    arg0 = func76((v4 + 4.71238898038469))
                    break
                arg0 = neg(func76((v4 + -4.71238898038469)))
                break
            # TODO: f64.promote_f32
            arg0 = func75(((6.283185307179586 if (v3 < 0) else -6.283185307179586) + arg0))
            break
        if (u32(v2) >= u32(2139095040)):
            arg0 = (arg0 - arg0)
            break
        while True:  # $label4
            while True:  # $label3
                while True:  # $label2
                    while True:  # $label1
                        # br_table (func435(arg0, (v1 + 8)) & 3)
                        break
                        break
                    arg0 = func75(loadf64(v1 + 8))
                    break
                    break
                arg0 = func76(loadf64(v1 + 8))
                break
                break
            arg0 = func75(neg(loadf64(v1 + 8)))
            break
            break
        arg0 = neg(func76(loadf64(v1 + 8)))
        break
    G.global0 = (v1 + 16)
    return arg0

# ----------------------------------------------------------
# $func49
# ----------------------------------------------------------
def func49(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        # TODO: i32.reinterpret_f32
        v3 = arg0
        v2 = (arg0 & 2147483647)
        if (u32((arg0 & 2147483647)) <= u32(1061752794)):
            if (u32(v2) < u32(964689920)):
                break
            # TODO: f64.promote_f32
            break
        if (u32(v2) <= u32(1081824209)):
            if (u32(v2) >= u32(1075235812)):
                # TODO: f64.promote_f32
                break
            # TODO: f64.promote_f32
            v4 = arg0
            if (v3 < 0):
                break
            break
        if (u32(v2) <= u32(1088565717)):
            if (u32(v2) >= u32(1085271520)):
                # TODO: f64.promote_f32
                break
            if (v3 < 0):
                # TODO: f64.promote_f32
                break
            # TODO: f64.promote_f32
            break
        if (u32(v2) >= u32(2139095040)):
            break
        while True:  # $label4
            while True:  # $label3
                while True:  # $label2
                    while True:  # $label1
                        # br_table (func435(arg0, (v1 + 8)) & 3)
                        break
                        break
                    break
                    break
                break
                break
            break
            break
        break
    arg0 = func75(loadf64(v1 + 8))
    G.global0 = (v1 + 16)
    return arg0

# ----------------------------------------------------------
# $func50
# ----------------------------------------------------------
def func50(arg0):
    while True:  # $label1
        while True:  # $label0
            v1 = load32(arg0 + 5820)
            if (load32(arg0 + 5820) == 16):
                v1 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((v1 + load32(arg0 + 8)), load8u(arg0 + 5816))
                v1 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((v1 + load32(arg0 + 8)), load8u((arg0 + 5817)))
                store16(arg0 + 5816, 0)
                break
            if (v1 < 8):
                break
            v1 = load32(arg0 + 20)
            store32(arg0 + 20, (load32(arg0 + 20) + 1))
            store8((v1 + load32(arg0 + 8)), load8u(arg0 + 5816))
            store16(arg0 + 5816, load8u((arg0 + 5817)))
            break
        store32(0 + 5820, (load32(arg0 + 5820) - 8))
        break
    return arg0

# ----------------------------------------------------------
# $func51
# ----------------------------------------------------------
def func51(arg0, arg1):
    arg1 = func33(arg0, arg1)
    return ((0 - func33(arg0, arg1)) if func33(arg0, 1) else arg1)

# ----------------------------------------------------------
# $func52
# ----------------------------------------------------------
def func52(arg0, arg1):
    v2 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # $label0
        if not load32(40600):
            break
        if (u32(load32(9142868)) < u32(490)):
            break
        v10 = loadf32(42160)
        v3 = load8u(9143020)
        v11 = (i32(load32(9147148)) if load8u(9143020) else (loadf32(42160) * 12.0))
        v10 = (i32(load32(9147144)) if v3 else (v10 * 174.0))
        if load8u(9142916):
            v10 = loadf32(9671164)
            v12 = (v10 * loadf32(9671164))
            v11 = (v11 * v10)
            v7 = load32(9142884)
            while True:  # $label1
                v3 = load32(9142640)
                if not load32(9142640):
                    break
                if not load32(v3 + 20):
                    break
                v4 = load32(v3 + 28)
                if (load32(v3 + 28) == 2147483647):
                    v4 = load32(59152)
                    store32(59152, (load32(59152) + 1))
                    v5 = load32(9568052)
                    store32(v3 + 28, v4)
                    v8 = load32(v3)
                    v6 = load32(v3 + 4)
                    v9 = load32(9568048)
                    store32(9568048, (load32(9568048) + 1))
                    store32(((v9 << 2) + 9563952), v3)
                    store32(9568052, (v5 + ((v8 * (v6 + 2)) << 2)))
                    v5 = load32(9568056)
                    store32(v3 + 56, load32(9568056))
                    store32(9568056, (v5 + ((v6 * load32(v3)) << 2)))
                v4 = (v4 + (arg0 << 16))
                break
            store32(v2 + 76, v7)
            store32(v2 + 72, 0)
            store32(v2 + 68, (arg1 << 16))
            store32((v2 - -64), 0)
            store64(v2 + 56, 0)
            store32(v2 + 52, 0)
            store32(v2 + 48, v4)
            store64(v2 + 40, 0)
            store64(v2 + 32, 0)
            store64(v2 + 24, 0)
            store64(v2 + 16, -4590434657685733376)
            # TODO: f64.promote_f32
            storef64(v2 + 8, v12)
            # TODO: f64.promote_f32
            storef64(v2, v11)
            a_b()
            break
        v11 = loadf32(9671164)
        break
    G.global0 = (v2 + 80)

# ----------------------------------------------------------
# $func53
# ----------------------------------------------------------
def func53(arg0):
    v9 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    if load8u(9216068):
        v11 = load32(PLAYERS)
        v10 = load32(CURRENT_PLAYER)
        v12 = players[load32(CURRENT_PLAYER)]
        v2 = 1
        while True:  # $label3
            while True:  # $label0
                v7 = ((arg0 * 132) + 9216080)
                if not load8u(((arg0 * 132) + 9216080) + 23):
                    break
                v2 = 0
                while True:  # $label2
                    while True:  # $label1
                        v1 = load32(v7 + 4)
                        # br_table load32(((load32(v7 + 4) * 404) + ENTITY_TYPES) + 264)
                        break
                        break
                    v2 = 1
                    break
                    break
                if load32(((v12 + (v1 << 2)) + 281808)):
                    break
                break
            v14 = load32(v7 + 68)
            if not load32(v7 + 68):
                break
            v1 = 1
            while True:  # $label7
                if (v2 == 1):
                    v2 = 0
                    while True:  # $label6
                        v5 = load32((v7 + (v3 << 2)) + 28)
                        v8 = load32(((load32((v7 + (v3 << 2)) + 28) * 404) + ENTITY_TYPES) + 264)
                        v4 = (load32(((load32((v7 + (v3 << 2)) + 28) * 404) + ENTITY_TYPES) + 264) == 1)
                        while True:  # $label5
                            while True:  # $label4
                                v5 = load32(((v12 + (v5 << 2)) + 281808))
                                if (load32(((v12 + (v5 << 2)) + 281808)) == 1):
                                    break
                                v1 = ((v8 != 3) & v1)
                                if v5:
                                    break
                                v1 = ((v8 != 0) & v1)
                                break
                                break
                            v6 = (v4 | v6)
                            break
                        v2 = (v2 | v4)
                        v3 = (v3 + 1)
                        if ((v3 + 1) != v14):
                            continue
                        break
                    break
                v2 = 0
                while True:  # $label10
                    v5 = load32((v7 + (v3 << 2)) + 28)
                    v8 = load32(((load32((v7 + (v3 << 2)) + 28) * 404) + ENTITY_TYPES) + 264)
                    v4 = (load32(((load32((v7 + (v3 << 2)) + 28) * 404) + ENTITY_TYPES) + 264) == 1)
                    while True:  # $label9
                        while True:  # $label8
                            v5 = (v12 + (v5 << 2))
                            v5 = (load32(((v12 + (v5 << 2)) + 282828)) + load32((v5 + 281808)))
                            if ((load32(((v12 + (v5 << 2)) + 282828)) + load32((v5 + 281808))) == 1):
                                break
                            v1 = ((v8 != 3) & v1)
                            if v5:
                                break
                            v1 = ((v8 != 0) & v1)
                            break
                            break
                        v6 = (v4 | v6)
                        break
                    v2 = (v2 | v4)
                    v3 = (v3 + 1)
                    if ((v3 + 1) != v14):
                        continue
                    break
                break
            break
        v14 = (((v1 & v6) if (v2 & 1) else v1) & 1)
        while True:  # $label11
            if not load8u(v7 + 23):
                v3 = -1
                v12 = 0
                v2 = 0
                break
            while True:  # $label14
                while True:  # $label13
                    while True:  # $label12
                        v2 = load32(v7 + 4)
                        if (load32(v7 + 4) == load32(38604)):
                            break
                        if (load32(38608) == v2):
                            break
                        if (load32(38612) == v2):
                            break
                        if (load32(38616) == v2):
                            break
                        if (load32(38624) == v2):
                            break
                        if (load32(38628) == v2):
                            break
                        if (load32(38632) == v2):
                            break
                        if (load32(39056) != v2):
                            break
                        break
                    v13 = (v11 + (v10 * 286704))
                    v1 = ((v11 + (v10 * 286704)) + 282828)
                    v6 = (load32(9561044) << 2)
                    v7 = (load32(9561040) << 2)
                    v8 = (load32(9561048) << 2)
                    v4 = (load32(9561052) << 2)
                    v5 = (load32(9561056) << 2)
                    v16 = (load32(9561060) << 2)
                    v17 = (load32(9561064) << 2)
                    v15 = (load32(9561068) << 2)
                    v3 = (((((((load32((((v11 + (v10 * 286704)) + 282828) + (load32(9561044) << 2))) + load32((v1 + (load32(9561040) << 2)))) + load32((v1 + (load32(9561048) << 2)))) + load32((v1 + (load32(9561052) << 2)))) + load32((v1 + (load32(9561056) << 2)))) + load32((v1 + (load32(9561060) << 2)))) + load32((v1 + (load32(9561064) << 2)))) + load32((v1 + (load32(9561068) << 2))))
                    v1 = (v13 + 281808)
                    break
                    break
                v1 = ((v11 + (v10 * 286704)) + (v2 << 2))
                v3 = load32((((v11 + (v10 * 286704)) + (v2 << 2)) + 282828))
                break
            v16 = load32((v1 + 281808))
            v1 = ((v2 * 404) + ENTITY_TYPES)
            v17 = load8u(((v2 * 404) + ENTITY_TYPES) + 354)
            v13 = 0
            v7 = load32(v1 + 264)
            if (load32(v1 + 264) == 1):
                v14 = (v14 & (u32(func180(v12, v2)) < u32(load32(v1 + 204))))
                v7 = load32(v1 + 264)
            v12 = (v3 if (v7 == 1) else 0)
            while True:  # $label15
                v5 = ((arg0 * 132) + 9216080)
                v15 = load32(((arg0 * 132) + 9216080) + 112)
                if not load32(((arg0 * 132) + 9216080) + 112):
                    v3 = -1
                    break
                v8 = 0
                v18 = load32(ENTITIES)
                v3 = -1
                v19 = (v11 + (v10 * 286704))
                while True:  # $label20
                    while True:  # $label16
                        v1 = load32(((v19 + (load32((v5 + (v8 << 2)) + 72) << 2)) + 284636))
                        if not load32(((v19 + (load32((v5 + (v8 << 2)) + 72) << 2)) + 284636)):
                            break
                        v20 = load32(v1 + 8)
                        if not load32(v1 + 8):
                            break
                        v21 = load32(v1)
                        v6 = 0
                        while True:  # $label19
                            while True:  # $label17
                                v1 = load32((v21 + (v6 << 2)))
                                if not load32((v21 + (v6 << 2))):
                                    break
                                v1 = load32((v18 + (v1 * 132)) + 20)
                                if not load32((v18 + (v1 * 132)) + 20):
                                    break
                                v22 = load32(v1 + 8)
                                if not load32(v1 + 8):
                                    break
                                v23 = load32(v1)
                                v1 = 0
                                while True:  # $label18
                                    v4 = load32((v23 + (v1 << 2)))
                                    v24 = (u32(v4) > u32(2147483646))
                                    if (v2 == ((load32((v23 + (v1 << 2))) - 2147483647) if (u32(v4) > u32(2147483646)) else v4)):
                                        v12 = (v12 + (u32(v4) < u32(2147483647)))
                                        v13 = (v13 + v24)
                                        v3 = (v1 if (u32(v1) < u32(v3)) else v3)
                                    v1 = (v1 + 1)
                                    if ((v1 + 1) != v22):
                                        continue
                                    break
                                break
                            v6 = (v6 + 1)
                            if ((v6 + 1) != v20):
                                continue
                            break
                        break
                    v8 = (v8 + 1)
                    if ((v8 + 1) != v15):
                        continue
                    break
                break
            while True:  # $label21
                v1 = load32((v11 + (v10 * 286704)) + 281796)
                if not load32((v11 + (v10 * 286704)) + 281796):
                    break
                v10 = load32(v1 + 8)
                if not load32(v1 + 8):
                    break
                v4 = ((((v10 - 1) & 0xFFFFFFFF) >> 1) + 1)
                v8 = (((((v10 - 1) & 0xFFFFFFFF) >> 1) + 1) & 3)
                v11 = load32(v1)
                v6 = 0
                while True:  # $label22
                    if (u32(v10) < u32(7)):
                        v1 = 0
                        break
                    v5 = (v4 & -4)
                    v1 = 0
                    v4 = 0
                    while True:  # $label23
                        v10 = (v1 << 2)
                        v13 = ((((v13 + (load32((v11 + ((v1 << 2) | 4))) == v2)) + (load32((v11 + (v10 | 12))) == v2)) + (load32((v11 + (v10 | 20))) == v2)) + (load32((v11 + (v10 | 28))) == v2))
                        v1 = (v1 + 8)
                        v4 = (v4 + 4)
                        if ((v4 + 4) != v5):
                            continue
                        break
                    break
                if not v8:
                    break
                while True:  # $label24
                    v13 = (v13 + (load32((v11 + ((v1 << 2) | 4))) == v2))
                    v1 = (v1 + 2)
                    v6 = (v6 + 1)
                    if ((v6 + 1) != v8):
                        continue
                    break
                break
            v2 = (v7 == 3)
            v15 = not v7
            break
        v1 = (v7 == 1)
        store32(v9 + 36, v17)
        store32(v9 + 32, v1)
        store32(v9 + 28, v15)
        store32(v9 + 24, v2)
        store32(v9 + 20, v3)
        store32(v9 + 16, v13)
        store32(v9 + 12, v12)
        store32(v9 + 8, arg0)
        store32(v9 + 4, v16)
        store32(v9, v14)
        a_b()
    G.global0 = (v9 + 48)
    return v9

# ----------------------------------------------------------
# $func54
# ----------------------------------------------------------
def func54(arg0):
    v4 = load32(arg0 + 8)
    while True:  # $label1
        while True:  # $label0
            v2 = load32(arg0)
            if not (load32(arg0) & 15):
                v1 = (arg0 + 4)
                # TODO: i32.atomic.rmw.xchg
                arg0 = 0
                break
            v3 = G.global3
            v5 = load32(arg0 + 4)
            if (load32(G.global3 + 24) != (load32(arg0 + 4) & 1073741823)):
                break
            while True:  # $label2
                if ((v2 & 3) != 1):
                    break
                v1 = load32(arg0 + 20)
                if not load32(arg0 + 20):
                    break
                store32(arg0 + 20, (v1 - 1))
                return
                break
            v6 = (v2 & 128)
            if (v2 & 128):
                store32(v3 + 84, (arg0 + 16))
                # TODO: i32.atomic.rmw.add
            v1 = (arg0 + 4)
            v7 = load32(arg0 + 12)
            arg0 = load32(arg0 + 16)
            store32(load32(arg0 + 12), load32(arg0 + 16))
            if ((v3 + 76) != arg0):
                store32((arg0 - 4), v7)
            # TODO: i32.atomic.rmw.xchg
            arg0 = ((((v5 << 1) & (v2 << 29)) >> 31) & 2147483647)
            if not v6:
                break
            store32(v3 + 84, 0)
            while True:  # $label3
                # TODO: i32.atomic.rmw.add
                if (-1 != 1):
                    break
                if not load32(9689396):
                    break
                func111(9689392, 2147483647)
                break
            break
        if (not v4 & (arg0 >= 0)):
            break
        func97(v1)
        break

# ----------------------------------------------------------
# $func55
# ----------------------------------------------------------
def func55(arg0):
    while True:  # $label0
        if (load8u(arg0) & 15):
            break
        # TODO: i32.atomic.rmw.cmpxchg
        if 10:
            break
        return 0
        break
    while True:  # $label6
        while True:  # $label1
            v2 = load32(arg0)
            if not (load32(arg0) & 15):
                # TODO: i32.atomic.rmw.cmpxchg
                if not 10:
                    break
                v2 = load32(arg0)
            v1 = func185(arg0)
            if (func185(arg0) != 10):
                break
            v3 = (arg0 + 8)
            v4 = (arg0 + 4)
            v1 = 100
            while True:  # $label3
                while True:  # $label2
                    if not v1:
                        break
                    if not load32(v4):
                        break
                    v1 = (v1 - 1)
                    if not load32(v3):
                        continue
                    break
                break
            v1 = func185(arg0)
            if (func185(arg0) != 10):
                break
            v5 = ((v2 ^ -1) & 128)
            v6 = not (v2 & 4)
            v2 = ((v2 & 3) != 2)
            while True:  # $label7
                while True:  # $label4
                    v1 = load32(arg0 + 4)
                    v7 = (load32(arg0 + 4) & 1073741823)
                    if not ((load32(arg0 + 4) & 1073741823) | ((v1 != 0) & v6)):
                        break
                    while True:  # $label5
                        if v2:
                            break
                        if (v7 != load32(G.global3 + 24)):
                            break
                        break
                        break
                    # TODO: i32.atomic.rmw.add
                    v1 = (v1 | -2147483648)
                    # TODO: i32.atomic.rmw.cmpxchg
                    v1 = func434(v4, v1, v5)
                    # TODO: i32.atomic.rmw.sub
                    if (v1 == 27):
                        break
                    if v1:
                        break
                    break
                v1 = func185(arg0)
                if (func185(arg0) == 10):
                    continue
                break
            break
        break
    return v1

# ----------------------------------------------------------
# $func56
# ----------------------------------------------------------
def func56(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    while True:  # $label3
        while True:  # $label2
            while True:  # $label1
                while True:  # $label0
                    v11 = load32(arg2 + 248)
                    # br_table (load32(arg2 + 248) - 1)
                    break
                    break
                return func282(arg0, arg1, arg2, arg4, arg5, arg6)
                break
            return func283(arg0, arg1, arg2, arg4, arg5, arg6, arg7)
            break
        while True:  # $label10
            arg3 = arg0
            arg7 = arg2
            v12 = load32(arg2 + 216)
            v10 = load32(arg2 + 208)
            v9 = load32(arg2 + 372)
            while True:  # $label6
                while True:  # $label4
                    if not arg6:
                        break
                    if (v12 <= 0):
                        break
                    v14 = (load32(arg7 + 220) + arg1)
                    if ((load32(arg7 + 220) + arg1) <= arg1):
                        break
                    v17 = (arg3 + v12)
                    v15 = load32(9142440)
                    v18 = (load32(9142440) + 2)
                    v19 = ((load32(9142440) + 2) * v10)
                    v11 = load32(arg7 + 212)
                    arg8 = load32(9142840)
                    arg2 = arg3
                    while True:  # $label11
                        arg6 = (arg2 + 1)
                        v16 = (arg2 - arg3)
                        arg0 = arg1
                        v13 = arg1
                        while True:  # $label8
                            if (u32(arg2) < u32(v15)):
                                while True:  # $label7
                                    while True:  # $label5
                                        if not load8u((v9 + (v16 + ((arg0 - arg1) * v12)))):
                                            arg0 = (arg0 + 1)
                                            break
                                        v13 = 0
                                        if (u32(arg0) >= u32(v15)):
                                            break
                                        if ((arg0 | arg2) < 0):
                                            break
                                        arg0 = (arg0 + 1)
                                        if (load32((arg8 + ((arg6 + (((arg0 + 1) + v19) * v18)) << 2))) != v11):
                                            break
                                        break
                                    if (arg0 != v14):
                                        continue
                                    break
                                    break
                                raise Unreachable()
                            while True:  # $label9
                                if not load8u((v9 + (v16 + ((v13 - arg1) * v12)))):
                                    v13 = (v13 + 1)
                                    if (v14 != (v13 + 1)):
                                        continue
                                    break
                                break
                            break
                            break
                        arg2 = arg6
                        if (arg6 < v17):
                            continue
                        break
                    break
                v13 = 1
                if not arg4:
                    break
                if (v12 <= 0):
                    break
                v11 = (load32(arg7 + 220) + arg1)
                if ((load32(arg7 + 220) + arg1) <= arg1):
                    break
                arg8 = (arg3 + v12)
                arg0 = arg3
                while True:  # $label14
                    arg2 = (arg0 + 1)
                    arg7 = (arg0 - arg3)
                    arg6 = load32(9142840)
                    arg0 = arg1
                    while True:  # $label13
                        while True:  # $label12
                            if not load8u((v9 + (arg7 + ((arg0 - arg1) * v12)))):
                                arg0 = (arg0 + 1)
                                break
                            arg0 = (arg0 + 1)
                            arg4 = (load32(9142440) + 2)
                            store32((arg6 + ((arg2 + (((arg0 + 1) + ((load32(9142440) + 2) * v10)) * arg4)) << 2)), arg5)
                            break
                        if (arg0 != v11):
                            continue
                        break
                    arg0 = arg2
                    if (arg2 < arg8):
                        continue
                    break
                break
            break
        return v13
        break
    arg7 = load32(arg2 + 208)
    if not load32(arg2 + 208):
        while True:  # $label21
            arg3 = arg0
            arg7 = arg2
            v9 = load32(arg2 + 216)
            v14 = load32(arg2 + 372)
            while True:  # $label17
                while True:  # $label15
                    if not arg6:
                        break
                    if (v9 <= 0):
                        break
                    v16 = (load32(arg7 + 220) + arg1)
                    if ((load32(arg7 + 220) + arg1) <= arg1):
                        break
                    v11 = (arg3 + v9)
                    v17 = load32(9142440)
                    v15 = (load32(9142440) + 2)
                    arg8 = load32(ENTITIES)
                    v18 = load32(9142840)
                    arg2 = arg3
                    while True:  # $label22
                        arg6 = (arg2 + 1)
                        v19 = (arg2 - arg3)
                        arg0 = arg1
                        v10 = arg1
                        while True:  # $label19
                            if (u32(arg2) < u32(v17)):
                                while True:  # $label18
                                    while True:  # $label16
                                        if not load8u((v14 + (v19 + ((arg0 - arg1) * v9)))):
                                            arg0 = (arg0 + 1)
                                            break
                                        v10 = 0
                                        if (u32(arg0) >= u32(v17)):
                                            break
                                        if ((arg0 | arg2) < 0):
                                            break
                                        arg0 = (arg0 + 1)
                                        if load32((v18 + (((v15 * (arg0 + 1)) + arg6) << 2))):
                                            break
                                        if (load32(((load8u((arg8 + (load32((v18 + ((((arg0 + v15) * v15) + arg6) << 2))) * 132)) + 122) * 404) + ENTITY_TYPES) + 264) == 1):
                                            break
                                        break
                                    if (arg0 != v16):
                                        continue
                                    break
                                    break
                                raise Unreachable()
                            while True:  # $label20
                                if not load8u((v14 + (v19 + ((v10 - arg1) * v9)))):
                                    v10 = (v10 + 1)
                                    if (v16 != (v10 + 1)):
                                        continue
                                    break
                                break
                            break
                            break
                        arg2 = arg6
                        if (arg6 < v11):
                            continue
                        break
                    break
                v10 = 1
                if not arg4:
                    break
                if (v9 <= 0):
                    break
                arg8 = (load32(arg7 + 220) + arg1)
                if ((load32(arg7 + 220) + arg1) <= arg1):
                    break
                arg7 = (arg3 + v9)
                arg0 = arg3
                while True:  # $label25
                    arg2 = (arg0 + 1)
                    arg6 = (arg0 - arg3)
                    arg4 = load32(9142840)
                    arg0 = arg1
                    while True:  # $label24
                        while True:  # $label23
                            if not load8u((v14 + (arg6 + ((arg0 - arg1) * v9)))):
                                arg0 = (arg0 + 1)
                                break
                            arg0 = (arg0 + 1)
                            store32((arg4 + ((arg2 + ((arg0 + 1) * (load32(9142440) + 2))) << 2)), arg5)
                            break
                        if (arg0 != arg8):
                            continue
                        break
                    arg0 = arg2
                    if (arg2 < arg7):
                        continue
                    break
                break
            break
        return v10
    while True:  # $label28
        while True:  # $label27
            while True:  # $label26
                # br_table (v11 - 4)
                break
                break
            return func193(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg8)
            break
        return func194(arg0, arg1, arg2, arg3, arg4, arg5, arg6)
        break
    if (u32(arg7) <= u32(2)):
    else:
    return 0

# ----------------------------------------------------------
# $func57
# ----------------------------------------------------------
def func57(arg0):
    v10 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    if not load8u(9142917):
        store32(9143000, arg0)
        store32(9671120, 0)
        store32(9263840, 0)
        v11 = load32(ENTITIES)
        v7 = load32(PLAYERS)
        v12 = load32(CURRENT_PLAYER)
        v5 = players[load32(CURRENT_PLAYER)]
        while True:  # $label4
            while True:  # $label0
                v1 = load32(((v5 + (v3 << 2)) + 284636))
                if not load32(((v5 + (v3 << 2)) + 284636)):
                    break
                v6 = load32(v1 + 8)
                if not load32(v1 + 8):
                    break
                v8 = load32(v1)
                v1 = 0
                if (v6 != 1):
                    v13 = (v6 & -2)
                    v4 = 0
                    while True:  # $label3
                        while True:  # $label1
                            v9 = (v1 << 2)
                            v14 = load32((v8 + (v1 << 2)))
                            if not load32((v8 + (v1 << 2))):
                                break
                            v14 = load32((v11 + (v14 * 132)) + 24)
                            if not load32((v11 + (v14 * 132)) + 24):
                                break
                            v2 = ((load32(v14 + 8) != 0) | v2)
                            break
                        while True:  # $label2
                            v9 = load32((v8 + (v9 | 4)))
                            if not load32((v8 + (v9 | 4))):
                                break
                            v9 = load32((v11 + (v9 * 132)) + 24)
                            if not load32((v11 + (v9 * 132)) + 24):
                                break
                            v2 = ((load32(v9 + 8) != 0) | v2)
                            break
                        v1 = (v1 + 2)
                        v4 = (v4 + 2)
                        if ((v4 + 2) != v13):
                            continue
                        break
                if not (v6 & 1):
                    break
                v1 = load32((v8 + (v1 << 2)))
                if not load32((v8 + (v1 << 2))):
                    break
                v1 = load32((v11 + (v1 * 132)) + 24)
                if not load32((v11 + (v1 * 132)) + 24):
                    break
                v2 = ((load32(v1 + 8) != 0) | v2)
                break
            v3 = (v3 + 1)
            if ((v3 + 1) != 255):
                continue
            break
        v1 = 1
        store32(9671120, 1)
        store8(9262828, 1)
        store32(9263072, 9262808)
        v3 = (((load32((v7 + (v12 * 286704)) + 283936) != 0) | v2) & 1)
        store8(9256756, (((load32((v7 + (v12 * 286704)) + 283936) != 0) | v2) & 1))
        v6 = load8u(9143020)
        if (v3 if load8u(9143020) else 1):
            store32(9671120, 2)
            store32(9263076, 9256736)
            v1 = 2
        v3 = load32((((v7 + (v12 * 286704)) + (load32(38428) << 2)) + 281808))
        store8(9256888, (load32((((v7 + (v12 * 286704)) + (load32(38428) << 2)) + 281808)) != 0))
        while True:  # $label6
            while True:  # $label5
                if v3:
                    break
                if not v6:
                    break
                v2 = v1
                break
                break
            v2 = (v1 + 1)
            store32(9671120, (v1 + 1))
            store32(((v1 << 2) + 9263072), 9256868)
            break
        v4 = 0
        while True:  # $label15
            while True:  # $label14
                while True:  # $label13
                    while True:  # $label12
                        while True:  # $label9
                            while True:  # $label11
                                while True:  # $label7
                                    v3 = ((v4 * 404) + ENTITY_TYPES)
                                    if (load32(((v4 * 404) + ENTITY_TYPES) + 264) != 2):
                                        break
                                    if (u32(load32(v3 + 268)) > u32(2)):
                                        break
                                    v3 = load32(((v7 + (v4 << 2)) + 284636))
                                    if not load32(((v7 + (v4 << 2)) + 284636)):
                                        break
                                    v8 = load32(v3 + 8)
                                    if not load32(v3 + 8):
                                        break
                                    v3 = load32(v3)
                                    v1 = 0
                                    while True:  # $label10
                                        while True:  # $label8
                                            v5 = load32((v3 + (v1 << 2)))
                                            if not load32((v3 + (v1 << 2))):
                                                break
                                            v5 = load32((v11 + (v5 * 132)) + 36)
                                            if not load32((v11 + (v5 * 132)) + 36):
                                                break
                                            if (v12 == load16u((v11 + (v5 * 132)) + 110)):
                                                break
                                            break
                                        v1 = (v1 + 1)
                                        if ((v1 + 1) != v8):
                                            continue
                                        break
                                    break
                                v4 = (v4 + 1)
                                if ((v4 + 1) != 255):
                                    continue
                                break
                            store8(9257020, 0)
                            if v6:
                                store8(9257152, 0)
                                v1 = v2
                                break
                            store8(9257152, 0)
                            store32(((v2 << 2) + 9263072), 9257000)
                            v1 = (v2 + 1)
                            break
                            break
                        v1 = (v2 + 1)
                        store32(9671120, (v2 + 1))
                        store8(9257020, 1)
                        store8(9257152, 0)
                        store32(((v2 << 2) + 9263072), 9257000)
                        if not v6:
                            break
                        break
                    v3 = load32(9142912)
                    store8(9257284, (load32(9142912) != 0))
                    if v3:
                        break
                    v3 = v1
                    if v6:
                        break
                    break
                    break
                store32(((v1 << 2) + 9263072), 9257132)
                store8(9257284, (load32(9142912) != 0))
                v1 = (v1 + 1)
                break
            v3 = (v1 + 1)
            store32(9671120, (v1 + 1))
            store32(((v1 << 2) + 9263072), 9257264)
            break
        v2 = 0
        v8 = load32(9215884)
        while True:  # $label16
            v4 = (v7 + (v12 * 286704))
            v1 = load32(((v7 + (v12 * 286704)) + 284676))
            if not load32(((v7 + (v12 * 286704)) + 284676)):
                break
            v5 = load32(v1 + 8)
            if not load32(v1 + 8):
                break
            v13 = load32(v1)
            v1 = 0
            while True:  # $label18
                while True:  # $label17
                    v2 = load32((v13 + (v1 << 2)))
                    if not load32((v13 + (v1 << 2))):
                        break
                    v2 = (v11 + (v2 * 132))
                    if (load8u((v11 + (v2 * 132)) + 122) != 10):
                        break
                    v9 = load32(v2 + 44)
                    if not ((load32((v8 + (load32(v2 + 44) << 4)) + 4) == 22) | not v9):
                        break
                    if load8u(v2 + 125):
                        break
                    if load32(v2 + 36):
                        break
                    if (load8u(v2 + 129) == 10):
                        break
                    v2 = 1
                    break
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v5):
                    continue
                break
            v2 = 0
            break
        while True:  # $label19
            v1 = load32((v4 + 284952))
            if not load32((v4 + 284952)):
                break
            v5 = load32(v1 + 8)
            if not load32(v1 + 8):
                break
            v13 = load32(v1)
            v1 = 0
            while True:  # $label21
                while True:  # $label20
                    v4 = load32((v13 + (v1 << 2)))
                    if not load32((v13 + (v1 << 2))):
                        break
                    v4 = (v11 + (v4 * 132))
                    if (load8u((v11 + (v4 * 132)) + 122) != 79):
                        break
                    v9 = load32(v4 + 44)
                    if not ((load32((v8 + (load32(v4 + 44) << 4)) + 4) == 22) | not v9):
                        break
                    if load8u(v4 + 125):
                        break
                    if load32(v4 + 36):
                        break
                    if (load8u(v4 + 129) == 10):
                        break
                    v2 = 1
                    break
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v5):
                    continue
                break
            break
        while True:  # $label26
            while True:  # $label24
                while True:  # $label22
                    v1 = load32(((v7 + (v12 * 286704)) + 284892))
                    if not load32(((v7 + (v12 * 286704)) + 284892)):
                        break
                    v5 = load32(v1 + 8)
                    if not load32(v1 + 8):
                        break
                    v13 = load32(v1)
                    v1 = 0
                    while True:  # $label25
                        while True:  # $label23
                            v4 = load32((v13 + (v1 << 2)))
                            if not load32((v13 + (v1 << 2))):
                                break
                            v4 = (v11 + (v4 * 132))
                            if (load8u((v11 + (v4 * 132)) + 122) != 64):
                                break
                            v9 = load32(v4 + 44)
                            if not ((load32((v8 + (load32(v4 + 44) << 4)) + 4) == 22) | not v9):
                                break
                            if load8u(v4 + 125):
                                break
                            if load32(v4 + 36):
                                break
                            if (load8u(v4 + 129) == 10):
                                break
                            store8(9257416, 1)
                            break
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != v5):
                            continue
                        break
                    break
                store8(9257416, v2)
                if ((v2 | not v6) != 1):
                    break
                break
            v1 = (v3 + 1)
            store32(9671120, (v3 + 1))
            store32(((v3 << 2) + 9263072), 9257396)
            if v6:
                v3 = v1
                break
            v3 = (v3 + 2)
            store32(9671120, (v3 + 2))
            store8(9257548, 1)
            store32(((v1 << 2) + 9263072), 9257528)
            break
        v1 = 0
        v4 = load32(38764)
        v8 = load32(38456)
        v5 = (v7 + (v12 * 286704))
        while True:  # $label31
            while True:  # $label30
                while True:  # $label28
                    while True:  # $label29
                        while True:  # $label27
                            v2 = ((v1 * 404) + ENTITY_TYPES)
                            if load32(((v1 * 404) + ENTITY_TYPES) + 264):
                                break
                            if (load32(v2 + 268) == 1):
                                break
                            if not load32(v2 + 92):
                                break
                            if (v1 == v8):
                                break
                            if (v1 == v4):
                                break
                            if load32(((v5 + (v1 << 2)) + 281808)):
                                break
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != 255):
                            continue
                        break
                    store8(9261640, 0)
                    if not v6:
                        break
                    v2 = v3
                    break
                    break
                store8(9261640, 1)
                break
            v2 = (v3 + 1)
            store32(9671120, (v3 + 1))
            store32(((v3 << 2) + 9263072), 9261620)
            break
        while True:  # $label33
            while True:  # $label32
                v3 = (v7 + (v12 * 286704))
                if not load32((((v7 + (v12 * 286704)) + (v8 << 2)) + 281808)):
                    v3 = load32(((v3 + (v4 << 2)) + 281808))
                    store8(9261772, (load32(((v3 + (v4 << 2)) + 281808)) != 0))
                    if v3:
                        break
                    if not v6:
                        break
                    v1 = v2
                    break
                store8(9261772, 1)
                break
            v1 = (v2 + 1)
            store32(9671120, (v2 + 1))
            store32(((v2 << 2) + 9263072), 9261752)
            break
        while True:  # $label36
            while True:  # $label35
                while True:  # $label34
                    v3 = (v7 + (v12 * 286704))
                    if load32((((v7 + (v12 * 286704)) + (load32(38440) << 2)) + 281808)):
                        break
                    if load32(((v3 + (load32(38772) << 2)) + 281808)):
                        break
                    v3 = load32((((v7 + (v12 * 286704)) + (load32(38928) << 2)) + 281808))
                    store8(9262432, (load32((((v7 + (v12 * 286704)) + (load32(38928) << 2)) + 281808)) != 0))
                    if v3:
                        break
                    if not v6:
                        break
                    v2 = v1
                    break
                    break
                store8(9262432, 1)
                break
            v2 = (v1 + 1)
            store32(9671120, (v1 + 1))
            store32(((v1 << 2) + 9263072), 9262412)
            break
        v3 = 0
        while True:  # $label40
            while True:  # $label39
                while True:  # $label37
                    v1 = load32((((v7 + (v12 * 286704)) + (load32(38528) << 2)) + 284636))
                    if load32((((v7 + (v12 * 286704)) + (load32(38528) << 2)) + 284636)):
                        v5 = load32(v1 + 8)
                        if load32(v1 + 8):
                            v13 = load32(v1)
                            v1 = 0
                            v3 = 1
                            while True:  # $label38
                                v9 = load32((v13 + (v1 << 2)))
                                if load32((v13 + (v1 << 2))):
                                    if (u32(load32((v11 + (v9 * 132)) + 80)) > u32(449)):
                                        break
                                v1 = (v1 + 1)
                                v3 = (u32((v1 + 1)) < u32(v5))
                                if (v1 != v5):
                                    continue
                                break
                        store8(9262564, v3)
                        if not v6:
                            break
                        v3 = v2
                        break
                    store8(9262564, 0)
                    if not v6:
                        break
                    v3 = v2
                    break
                    break
                store8(9262564, (v3 & 1))
                break
            v3 = (v2 + 1)
            store32(9671120, (v2 + 1))
            store32(((v2 << 2) + 9263072), 9262544)
            break
        v1 = 0
        v11 = load32(38932)
        v5 = (v7 + (v12 * 286704))
        while True:  # $label45
            while True:  # $label44
                while True:  # $label42
                    while True:  # $label43
                        while True:  # $label41
                            if not load32(((v5 + (v1 << 2)) + 281808)):
                                break
                            v2 = ((v1 * 404) + ENTITY_TYPES)
                            if load32(((v1 * 404) + ENTITY_TYPES) + 264):
                                break
                            v13 = load32(v2 + 268)
                            if (load32(v2 + 268) == 1):
                                break
                            if not load32(v2 + 92):
                                break
                            if (v13 == 2):
                                break
                            if (v1 == v11):
                                break
                            if (v1 == v8):
                                break
                            if (v1 == v4):
                                break
                            if (load32(v2 + 224) > 1):
                                break
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != 255):
                            continue
                        break
                    store8(9262036, 0)
                    if not v6:
                        break
                    v2 = v3
                    break
                    break
                store8(9262036, 1)
                break
            v2 = (v3 + 1)
            store32(9671120, (v3 + 1))
            store32(((v3 << 2) + 9263072), 9262016)
            break
        v1 = 0
        v4 = load32(38704)
        v11 = load32(38752)
        v8 = load32(38776)
        v5 = load32(38696)
        v13 = load32(38692)
        v9 = load32(38756)
        v14 = load32(38496)
        v15 = load32(38452)
        v16 = (v7 + (v12 * 286704))
        while True:  # $label50
            while True:  # $label49
                while True:  # $label47
                    while True:  # $label48
                        while True:  # $label46
                            if not load32(((v16 + (v1 << 2)) + 281808)):
                                break
                            v3 = ((v1 * 404) + ENTITY_TYPES)
                            if load32(((v1 * 404) + ENTITY_TYPES) + 264):
                                break
                            if (load32(v3 + 268) == 1):
                                break
                            if not load32(v3 + 92):
                                break
                            if (v1 == v15):
                                break
                            if (v1 == v14):
                                break
                            if (v1 == v9):
                                break
                            if (v1 == v13):
                                break
                            if (v1 == v5):
                                break
                            if (v1 == v8):
                                break
                            if (v1 == v11):
                                break
                            if (v1 == v4):
                                break
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != 255):
                            continue
                        break
                    store8(9261904, 0)
                    if not v6:
                        break
                    v3 = v2
                    break
                    break
                store8(9261904, 1)
                break
            v3 = (v2 + 1)
            store32(9671120, (v2 + 1))
            store32(((v2 << 2) + 9263072), 9261884)
            break
        v1 = 0
        v7 = (v7 + (v12 * 286704))
        while True:  # $label56
            while True:  # $label55
                while True:  # $label54
                    while True:  # $label52
                        while True:  # $label53
                            while True:  # $label51
                                if not load32(((v7 + (v1 << 2)) + 281808)):
                                    break
                                v2 = ((v1 * 404) + ENTITY_TYPES)
                                if load32(((v1 * 404) + ENTITY_TYPES) + 264):
                                    break
                                if (load32(v2 + 268) == 1):
                                    break
                                if not load32(v2 + 92):
                                    break
                                if (load32(v2 + 224) == 1):
                                    break
                                break
                            v1 = (v1 + 1)
                            if ((v1 + 1) != 255):
                                continue
                            break
                        store8(9262168, 0)
                        if v6:
                            v2 = v3
                            break
                        v2 = v3
                        break
                        break
                    v2 = (v3 + 1)
                    store32(9671120, (v3 + 1))
                    store8(9262168, 1)
                    store32(((v3 << 2) + 9263072), 9262148)
                    if not v6:
                        break
                    break
                store8(9257548, 1)
                break
            v1 = 9257528
            v3 = (v2 + 1)
            store32(9671120, (v2 + 1))
            store32(((v2 << 2) + 9263072), v1)
            v2 = v3
            break
        v1 = 0
        while True:  # $label57
            v4 = load32(9147120)
            if not load32(9147120):
                break
            while True:  # $label58
                arg0 = load32(9143000)
                v2 = ((load32(9143000) * v4) + v1)
                if (((load32(9143000) * v4) + v1) == load32(9671120)):
                    break
                arg0 = load32(((v2 << 2) + 9263072))
                v3 = load8u(load32(((v2 << 2) + 9263072)) + 20)
                arg0 = load32(arg0 + 8)
                store64(v10 + 32, 0)
                store64(v10 + 40, 0)
                store64(v10 + 48, 0)
                store64(v10 + 56, 4294967295)
                store32(v10 + 20, arg0)
                store32(v10 + 24, v3)
                store32(v10 + 28, 0)
                store32(v10 + 16, v1)
                a_b()
                v1 = (v1 + 1)
                v4 = load32(9147120)
                if (u32((v1 + 1)) < u32(load32(9147120))):
                    continue
                break
            v2 = load32(9671120)
            arg0 = load32(9143000)
            break
        store32(v10 + 4, v2)
        store32(v10, arg0)
        a_b()
        store8(9684768, 1)
    G.global0 = (v10 - -64)
    return v10

# ----------------------------------------------------------
# $func58
# ----------------------------------------------------------
def func58(arg0, arg1):
    while True:  # $label0
        if not arg0:
            break
        # TODO: i64.div_u
        v3 = arg0
        while True:  # $label1
            v4 = i32(arg1)
            arg0 = (i32(arg1) * arg0)
            if (u32((i32(arg1) * arg0)) > u32(4294967295)):
                break
            if (u32(v3) < u32(v4)):
                break
            if not arg0:
                break
            v2 = e()
            break
        return v2
        break
    a_c()
    raise Unreachable()
    return 5173

# ----------------------------------------------------------
# $func59
# ----------------------------------------------------------
def func59(arg0, arg1, arg2, arg3):
    v23 = ((load8u(arg2 + 122) * 404) + ENTITY_TYPES)
    v24 = 1
    while True:  # $label41
        while True:  # $label38
            while True:  # $label0
                v6 = load16u(arg2 + 112)
                v21 = (load16u(arg2 + 112) - v19)
                v5 = load32(v23 + 216)
                v8 = (v19 << 1)
                v25 = (v21 + (load32(v23 + 216) + (v19 << 1)))
                if ((load16u(arg2 + 112) - v19) >= (v21 + (load32(v23 + 216) + (v19 << 1)))):
                    break
                v7 = load16u(arg2 + 114)
                v22 = (load16u(arg2 + 114) - v19)
                v4 = load32(v23 + 220)
                v8 = (v22 + (v8 + load32(v23 + 220)))
                if ((load16u(arg2 + 114) - v19) >= (v22 + (v8 + load32(v23 + 220)))):
                    break
                v27 = (v25 - 1)
                v28 = (v8 - 1)
                v29 = ((v6 + v19) + v5)
                v30 = ((v7 + v19) + v4)
                v26 = 1
                v8 = v21
                while True:  # $label40
                    v5 = v22
                    while True:  # $label39
                        while True:  # $label2
                            while True:  # $label1
                                if (v8 == v21):
                                    break
                                if (v5 == v22):
                                    break
                                if (v5 == v28):
                                    break
                                if (v8 != v27):
                                    break
                                break
                            v11 = load32(9142440)
                            if (u32(load32(9142440)) <= u32(v5)):
                                break
                            if ((v5 | v8) < 0):
                                break
                            if (u32(v8) >= u32(v11)):
                                break
                            while True:  # $label7
                                while True:  # $label6
                                    while True:  # $label3
                                        while True:  # $label4
                                            while True:  # $label5
                                                v4 = load32(arg3 + 248)
                                                # br_table (load32(arg3 + 248) - 1)
                                                break
                                                break
                                            v9 = load32(arg3 + 216)
                                            if (load32(arg3 + 216) <= 0):
                                                break
                                            v12 = (load32(arg3 + 220) + v5)
                                            if ((load32(arg3 + 220) + v5) <= v5):
                                                break
                                            v16 = (v8 + v9)
                                            v13 = load32(arg3 + 372)
                                            v17 = (v11 + 2)
                                            v18 = ((v11 + 2) * load32(arg3 + 208))
                                            v15 = load32(arg3 + 212)
                                            v20 = load32(9142840)
                                            v7 = v8
                                            while True:  # $label12
                                                v10 = (v7 + 1)
                                                v14 = (v7 - v8)
                                                v6 = v5
                                                v4 = v5
                                                while True:  # $label9
                                                    if (u32(v7) >= u32(v11)):
                                                        while True:  # $label8
                                                            if load8u((v13 + (((v6 - v5) * v9) + v14))):
                                                                break
                                                            v6 = (v6 + 1)
                                                            if ((v6 + 1) != v12):
                                                                continue
                                                            break
                                                            break
                                                        raise Unreachable()
                                                    while True:  # $label11
                                                        while True:  # $label10
                                                            if load8u((v13 + (((v4 - v5) * v9) + v14))):
                                                                if (u32(v4) >= u32(v11)):
                                                                    break
                                                                if ((v4 | v7) < 0):
                                                                    break
                                                                v4 = (v4 + 1)
                                                                if (load32((v20 + (((((v4 + 1) + v18) * v17) + v10) << 2))) == v15):
                                                                    break
                                                                break
                                                            v4 = (v4 + 1)
                                                            break
                                                        if (v4 != v12):
                                                            continue
                                                        break
                                                    break
                                                v7 = v10
                                                if (v10 < v16):
                                                    continue
                                                break
                                            break
                                            break
                                        v6 = load32(arg3 + 216)
                                        if (load32(arg3 + 216) <= 0):
                                            break
                                        v10 = (load32(arg3 + 220) + v5)
                                        if ((load32(arg3 + 220) + v5) <= v5):
                                            break
                                        v9 = (v6 + v8)
                                        v12 = (v11 + 2)
                                        v13 = ((v11 + 2) * load32(arg3 + 208))
                                        v14 = load32(9142840)
                                        v6 = v8
                                        while True:  # $label13
                                            if (u32(v6) >= u32(v11)):
                                                break
                                            v7 = (v6 + 1)
                                            v4 = v5
                                            while True:  # $label14
                                                if (v4 == v10):
                                                    v6 = v7
                                                    if (v7 < v9):
                                                        continue
                                                    break
                                                if (u32(v4) >= u32(v11)):
                                                    break
                                                if ((v4 | v6) < 0):
                                                    break
                                                v4 = (v4 + 1)
                                                if (u32(load32((v14 + (((((v4 + 1) + v13) * v12) + v7) << 2)))) <= u32(2)):
                                                    continue
                                                break
                                            break
                                        break
                                        break
                                    v9 = load32(arg3 + 216)
                                    if (load32(arg3 + 216) <= 0):
                                        break
                                    v16 = load32(arg3 + 220)
                                    if (load32(arg3 + 220) <= 0):
                                        break
                                    v17 = (v5 + v16)
                                    v31 = (v8 + v9)
                                    v18 = load32(arg3 + 372)
                                    v12 = (v11 + 2)
                                    v32 = ((v11 + 2) * load32(arg3 + 208))
                                    v13 = 0
                                    v14 = load32(9142840)
                                    v7 = 0
                                    v6 = v8
                                    while True:  # $label19
                                        v10 = (v6 + 1)
                                        v15 = (v6 - v8)
                                        v4 = v5
                                        while True:  # $label17
                                            if (u32(v6) < u32(v11)):
                                                while True:  # $label16
                                                    while True:  # $label15
                                                        if load8u((v18 + (((v4 - v5) * v9) + v15))):
                                                            if (u32(v4) >= u32(v11)):
                                                                break
                                                            if ((v4 | v6) < 0):
                                                                break
                                                            v4 = (v4 + 1)
                                                            v20 = load32((v14 + (((((v4 + 1) + v32) * v12) + v10) << 2)))
                                                            if (u32(load32((v14 + (((((v4 + 1) + v32) * v12) + v10) << 2)))) > u32(2)):
                                                                break
                                                            if (u32(load32((v14 + (((v4 * v12) + v10) << 2)))) > u32(2)):
                                                                break
                                                            if (u32(load32((v14 + ((((v4 + v12) * v12) + v10) << 2)))) > u32(2)):
                                                                break
                                                            v7 = (not v20 | v7)
                                                            v13 = (v13 + (v20 == 1))
                                                            break
                                                        v4 = (v4 + 1)
                                                        break
                                                    if (v4 < v17):
                                                        continue
                                                    break
                                                break
                                            while True:  # $label18
                                                if load8u((v18 + (((v4 - v5) * v9) + v15))):
                                                    break
                                                v4 = (v4 + 1)
                                                if ((v4 + 1) < v17):
                                                    continue
                                                break
                                            break
                                        v6 = v10
                                        if (v10 < v31):
                                            continue
                                        break
                                    if not ((u32(v13) >= u32((((v9 * v16) // 2) - 1))) & v7):
                                        break
                                    break
                                    break
                                while True:  # $label21
                                    v6 = load32(arg3 + 208)
                                    if load32(arg3 + 208):
                                        v7 = load16u(arg2 + 110)
                                        while True:  # $label22
                                            while True:  # $label20
                                                # br_table (v4 - 4)
                                                break
                                                break
                                            if not func193(v8, v5, arg3, v7, 0, 0, 1, 0):
                                                break
                                            break
                                            break
                                        if (u32(v6) > u32(2)):
                                            break
                                        v10 = load32(arg3 + 216)
                                        if (load32(arg3 + 216) <= 0):
                                            break
                                        v9 = (load32(arg3 + 220) + v5)
                                        if ((load32(arg3 + 220) + v5) <= v5):
                                            break
                                        v17 = (v8 + v10)
                                        v12 = load32(arg3 + 372)
                                        v13 = (v11 + 2)
                                        v18 = (v6 * (v11 + 2))
                                        v14 = load32(arg3 + 212)
                                        v16 = load32(9142840)
                                        v6 = v8
                                        v7 = v8
                                        if (load32(arg3 + 264) != 1):
                                            while True:  # $label27
                                                v7 = (v6 + 1)
                                                v15 = (v6 - v8)
                                                v4 = v5
                                                while True:  # $label24
                                                    if (u32(v6) >= u32(v11)):
                                                        while True:  # $label23
                                                            if load8u((v12 + (((v4 - v5) * v10) + v15))):
                                                                break
                                                            v4 = (v4 + 1)
                                                            if ((v4 + 1) != v9):
                                                                continue
                                                            break
                                                            break
                                                        raise Unreachable()
                                                    while True:  # $label26
                                                        while True:  # $label25
                                                            if load8u((v12 + (((v4 - v5) * v10) + v15))):
                                                                if (u32(v4) >= u32(v11)):
                                                                    break
                                                                if ((v4 | v6) < 0):
                                                                    break
                                                                v4 = (v4 + 1)
                                                                if (load32((v16 + (((((v4 + 1) + v18) * v13) + v7) << 2))) == v14):
                                                                    break
                                                                break
                                                            v4 = (v4 + 1)
                                                            break
                                                        if (v4 != v9):
                                                            continue
                                                        break
                                                    break
                                                v6 = v7
                                                if (v7 < v17):
                                                    continue
                                                break
                                                break
                                            raise Unreachable()
                                        while True:  # $label32
                                            v6 = (v7 + 1)
                                            v15 = (v7 - v8)
                                            v4 = v5
                                            while True:  # $label29
                                                if (u32(v7) >= u32(v11)):
                                                    while True:  # $label28
                                                        if load8u((v12 + (((v4 - v5) * v10) + v15))):
                                                            break
                                                        v4 = (v4 + 1)
                                                        if ((v4 + 1) != v9):
                                                            continue
                                                        break
                                                        break
                                                    raise Unreachable()
                                                while True:  # $label31
                                                    while True:  # $label30
                                                        if load8u((v12 + (((v4 - v5) * v10) + v15))):
                                                            if (u32(v4) >= u32(v11)):
                                                                break
                                                            if ((v4 | v7) < 0):
                                                                break
                                                            v4 = (v4 + 1)
                                                            if (load32((v16 + (((((v4 + 1) + v18) * v13) + v6) << 2))) != v14):
                                                                break
                                                            if (load32((v16 + (((v4 * v13) + v6) << 2))) == v14):
                                                                break
                                                            break
                                                        v4 = (v4 + 1)
                                                        break
                                                    if (v4 != v9):
                                                        continue
                                                    break
                                                break
                                            v7 = v6
                                            if (v6 < v17):
                                                continue
                                            break
                                        break
                                    v9 = load32(arg3 + 216)
                                    if (load32(arg3 + 216) <= 0):
                                        break
                                    v13 = (load32(arg3 + 220) + v5)
                                    if ((load32(arg3 + 220) + v5) <= v5):
                                        break
                                    v18 = (v8 + v9)
                                    v14 = load32(arg3 + 372)
                                    v12 = (v11 + 2)
                                    v15 = load32(ENTITIES)
                                    v16 = load32(9142840)
                                    v7 = v8
                                    while True:  # $label37
                                        v10 = (v7 + 1)
                                        v17 = (v7 - v8)
                                        v6 = v5
                                        v4 = v5
                                        while True:  # $label34
                                            if (u32(v7) >= u32(v11)):
                                                while True:  # $label33
                                                    if load8u((v14 + (((v6 - v5) * v9) + v17))):
                                                        break
                                                    v6 = (v6 + 1)
                                                    if ((v6 + 1) != v13):
                                                        continue
                                                    break
                                                    break
                                                raise Unreachable()
                                            while True:  # $label36
                                                while True:  # $label35
                                                    if load8u((v14 + (((v4 - v5) * v9) + v17))):
                                                        if (u32(v4) >= u32(v11)):
                                                            break
                                                        if ((v4 | v7) < 0):
                                                            break
                                                        v4 = (v4 + 1)
                                                        if load32((v16 + ((((v4 + 1) * v12) + v10) << 2))):
                                                            break
                                                        if (load32(((load8u((v15 + (load32((v16 + ((((v4 + v12) * v12) + v10) << 2))) * 132)) + 122) * 404) + ENTITY_TYPES) + 264) != 1):
                                                            break
                                                        break
                                                    v4 = (v4 + 1)
                                                    break
                                                if (v4 != v13):
                                                    continue
                                                break
                                            break
                                        v7 = v10
                                        if (v10 < v18):
                                            continue
                                        break
                                    break
                                    break
                                if not func194(v8, v5, arg3, v7, 0, 0, 1):
                                    break
                                break
                            store32(arg0, v8)
                            store32(arg1, v5)
                            if v26:
                                break
                            break
                            break
                        v5 = (v5 + 1)
                        if ((v5 + 1) != v30):
                            continue
                        break
                    v8 = (v8 + 1)
                    v26 = ((v8 + 1) < v25)
                    if (v8 != v29):
                        continue
                    break
                break
            v19 = (v19 + 1)
            v24 = (u32((v19 + 1)) < u32(20))
            if (v19 != 20):
                continue
            break
        break
    return v24

# ----------------------------------------------------------
# $func60
# ----------------------------------------------------------
def func60(arg0, arg1):
    v4 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # $label0
        v3 = load32(arg0 + 48)
        if not load32(arg0 + 48):
            break
        v2 = load32(arg0 + 40)
        if not load32(arg0 + 40):
            break
        v11 = (i32(load16u(arg0 + 112)) * 32.0)
        v13 = i32(load32(v3 + 12))
        v14 = i32(load32(v3 + 8))
        v12 = (i32(load16u(arg0 + 114)) * 32.0)
        v3 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        v5 = load32(9142440)
        v10 = (((i32(load16u(arg0 + 114)) * 32.0) + ((1.0 if (load32(v3 + 264) == 4) else i32(load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 208))) * (i32(load32(9142440)) * 32.0))) * arg1)
        arg1 = (((i32(load16u(arg0 + 114)) * 32.0) + ((1.0 if (load32(v3 + 264) == 4) else i32(load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 208))) * (i32(load32(9142440)) * 32.0))) * arg1)
        while True:  # $label1
            v3 = load8u(9142916)
            if not load8u(9142916):
                break
            if (v10 == -55.0):
                break
            arg1 = (((v10 * 0.5) / i32((v5 * 96))) + 0.25)
            break
        store32(v4 + 56, v2)
        # TODO: f64.promote_f32
        storef64(v4 + 48, arg1)
        # TODO: f64.promote_f32
        storef64(v4 + 40, (v12 - (0.0 if v3 else v13)))
        # TODO: f64.promote_f32
        storef64(v4 + 32, (v11 - (0.0 if v3 else v14)))
        a_b()
        while True:  # $label2
            if load8u(9142916):
                break
            v3 = load32(arg0 + 92)
            if not load32(arg0 + 92):
                break
            if load8u(9142906):
                break
            v2 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
            if (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264) == 1):
                if (u32(load32(v2 + 216)) > u32(1)):
                    break
            v2 = load32(9142448)
            v5 = load32(load32(9142448) + 12)
            v2 = load32(v2 + 8)
            # TODO: f64.promote_f32
            storef64(v4 + 16, (v10 + -1.0))
            store32(v4 + 24, v3)
            # TODO: f64.promote_f32
            storef64(v4, (v11 - i32(v2)))
            # TODO: f64.promote_f32
            storef64(v4 + 8, (v12 - i32(v5)))
            a_b()
            break
        v3 = (G.global0 - 48)
        G.global0 = (G.global0 - 48)
        while True:  # $label3
            v2 = load32(arg0 + 24)
            if not load32(arg0 + 24):
                break
            v5 = load32(v2 + 4)
            if not load32(v2 + 4):
                break
            if not load32(v5 + 8):
                break
            v10 = (i32(load16u(arg0 + 112)) * 32.0)
            arg1 = (i32(load16u(arg0 + 114)) * 32.0)
            v11 = ((i32(load16u(arg0 + 114)) * 32.0) + -44.0)
            arg1 = (i32(load32(9142440)) * 32.0)
            arg1 = (arg1 + ((i32(load32(9142440)) * 32.0) + arg1))
            v12 = ((arg1 + ((i32(load32(9142440)) * 32.0) + arg1)) * 0.5)
            while True:  # $label6
                v6 = ((v8 | 1) << 2)
                v2 = load32((((v8 | 1) << 2) + load32(v5)))
                if not load32((((v8 | 1) << 2) + load32(v5))):
                    v2 = 0
                    while True:  # $label4
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
                        store32(v3 + 32, v9)
                        a_b()
                        store32(9163784, (load32(9163784) + 40000))
                        break
                    v7 = (load16u(arg0 + 114) << 5)
                    store32((load32(v5) + v6), v2)
                v6 = load8u(9142916)
                v7 = load32(9142584)
                v13 = i32(load32(load32(9142584) + 12))
                v14 = i32(load32(v7 + 8))
                while True:  # $label5
                    if (arg1 == -55.0):
                        break
                    if not v6:
                        break
                    break
                v15 = ((v12 / i32((load32(9142440) * 96))) + 0.25)
                store32(v3 + 24, v2)
                # TODO: f64.promote_f32
                storef64(v3 + 16, v15)
                # TODO: f64.promote_f32
                storef64(v3 + 8, (v11 - (0.0 if v6 else v13)))
                # TODO: f64.promote_f32
                storef64(v3, (v10 - (0.0 if v6 else v14)))
                a_b()
                v8 = (v8 + 2)
                if (u32((v8 + 2)) < u32(load32(v5 + 8))):
                    continue
                break
            break
        G.global0 = (v3 + 48)
        break
    G.global0 = (v4 - -64)
    return v3

# ----------------------------------------------------------
# $func61
# ----------------------------------------------------------
def func61(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
    v23 = load32(load32(GAME_STATE) + 64)
    while True:  # $label0
        if (arg0 == 3):
            if load8u(9216060):
                break
        v10 = load32(9142440)
        v18 = ((((load32(9142440) & 0xFFFFFFFF) >> 1) - 20) if v23 else v10)
        v26 = (((((((load32(9142440) & 0xFFFFFFFF) >> 1) - 20) if v23 else v10) * (arg1 * v18)) // 65536) if (arg2 == 1) else arg1)
        if not (((((((load32(9142440) & 0xFFFFFFFF) >> 1) - 20) if v23 else v10) * (arg1 * v18)) // 65536) if (arg2 == 1) else arg1):
            break
        v38 = i32(v18)
        v27 = (arg7 != 2147483647)
        while True:  # $label18
            arg1 = load32(9147320)
            arg2 = load32(9147312)
            store32(9147320, load32(9147312))
            v11 = load32(9147316)
            store32(9147316, arg2)
            v10 = (arg1 ^ (arg1 << 11))
            arg1 = load32(9147324)
            arg1 = ((load32(9147324) << 11) ^ arg1)
            arg1 = ((arg2 ^ (((arg2 & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ arg1) & 0xFFFFFFFF) >> 8))) ^ arg1)
            v10 = ((((((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((((arg2 ^ (((arg2 & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ arg1) & 0xFFFFFFFF) >> 8))) ^ arg1) & 0xFFFFFFFF) >> 19)) ^ v10) ^ arg1)
            while True:  # $label1
                if not arg8:
                    v14 = ((arg2 << 11) ^ arg2)
                    arg2 = ((v11 << 11) ^ v11)
                    arg2 = (((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ v10)
                    v11 = (((((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8) ^ (((((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ v10) & 0xFFFFFFFF) >> 19)) ^ v14) ^ arg2)
                    v13 = ((((((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8) ^ (((((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ v10) & 0xFFFFFFFF) >> 19)) ^ v14) ^ arg2) % v18)
                    v12 = (arg2 % v18)
                    v19 = ((v10 % 7) - 3)
                    break
                store32(9147324, arg2)
                arg1 = ((arg1 << 11) ^ arg1)
                arg2 = ((arg2 << 11) ^ arg2)
                v11 = ((v11 << 11) ^ v11)
                v14 = (((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ v11) ^ v10)
                arg2 = (((((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8) ^ (((((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ v11) ^ v10) & 0xFFFFFFFF) >> 19)) ^ arg2) ^ v14)
                v11 = (((((((arg1 << 11) ^ arg1) & 0xFFFFFFFF) >> 8) ^ (((((((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8) ^ (((((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ v11) ^ v10) & 0xFFFFFFFF) >> 19)) ^ arg2) ^ v14) & 0xFFFFFFFF) >> 19)) ^ arg1) ^ arg2)
                v19 = ((((((((arg1 << 11) ^ arg1) & 0xFFFFFFFF) >> 8) ^ (((((((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8) ^ (((((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ v11) ^ v10) & 0xFFFFFFFF) >> 19)) ^ arg2) ^ v14) & 0xFFFFFFFF) >> 19)) ^ arg1) ^ arg2) & 3)
                arg1 = (v14 % v18)
                v12 = (arg1 & 1)
                v13 = (0 if (arg1 & 1) else (v14 % v18))
                v12 = ((0 - v12) & arg1)
                arg1 = v10
                v10 = v14
                break
            v20 = (arg2 & 3)
            arg1 = ((arg1 << 11) ^ arg1)
            arg1 = (((((v11 & 0xFFFFFFFF) >> 19) ^ ((((arg1 << 11) ^ arg1) & 0xFFFFFFFF) >> 8)) ^ v11) ^ arg1)
            v15 = ((((((v11 & 0xFFFFFFFF) >> 19) ^ ((((arg1 << 11) ^ arg1) & 0xFFFFFFFF) >> 8)) ^ v11) ^ arg1) % arg3)
            while True:  # $label2
                if v27:
                    v14 = v11
                    v11 = arg2
                    arg2 = v10
                    break
                v14 = arg1
                arg1 = ((v10 << 11) ^ v10)
                arg1 = (arg1 ^ ((((((v10 << 11) ^ v10) & 0xFFFFFFFF) >> 8) ^ ((v14 & 0xFFFFFFFF) >> 19)) ^ arg1))
                break
            v24 = (((arg1 ^ ((((((v10 << 11) ^ v10) & 0xFFFFFFFF) >> 8) ^ ((v14 & 0xFFFFFFFF) >> 19)) ^ arg1)) % 3) + 1)
            store32(9147320, v14)
            store32(9147324, v11)
            store32(9147316, arg1)
            arg2 = ((arg2 << 11) ^ arg2)
            arg1 = ((arg1 ^ (((arg1 & 0xFFFFFFFF) >> 19) ^ ((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8))) ^ arg2)
            store32(9147312, ((arg1 ^ (((arg1 & 0xFFFFFFFF) >> 19) ^ ((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8))) ^ arg2))
            v28 = ((arg1 % arg4) + arg6)
            if ((arg1 % arg4) + arg6):
                v14 = (arg5 + v15)
                v21 = ((arg5 + v15) << 1)
                v25 = (v14 * v14)
                v22 = 0
                while True:  # $label17
                    v13 = (v13 + v19)
                    v12 = (v12 + v20)
                    arg1 = load32(9142440)
                    while True:  # $label3
                        while True:  # $label4
                            if not arg9:
                                if (u32(arg1) <= u32(v13)):
                                    break
                                if ((v12 | v13) < 0):
                                    break
                                if (u32(arg1) <= u32(v12)):
                                    break
                                if (v22 % v24):
                                    break
                                arg1 = load32(9147324)
                                store32(9147324, load32(9147316))
                                arg2 = load32(9147320)
                                v10 = load32(9147312)
                                store32(9147320, load32(9147312))
                                arg1 = (arg1 ^ (arg1 << 11))
                                arg1 = ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1)
                                store32(9147316, ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1))
                                arg2 = (arg2 ^ (arg2 << 11))
                                arg2 = ((((((arg2 ^ (arg2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg1 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ arg1)
                                store32(9147312, ((((((arg2 ^ (arg2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg1 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ arg1))
                                v19 = ((arg2 % 7) - 3)
                                v20 = ((arg1 % 7) - 3)
                                break
                            while True:  # $label5
                                if (u32(arg1) <= u32(v12)):
                                    v12 = (v12 % arg1)
                                    break
                                if (v12 >= 0):
                                    break
                                v12 = (arg1 - (v12 % arg1))
                                break
                            while True:  # $label6
                                if (u32(arg1) <= u32(v13)):
                                    v13 = (v13 % arg1)
                                    break
                                if (v13 >= 0):
                                    break
                                v13 = (arg1 - (v13 % arg1))
                                break
                            if (v22 % v24):
                                break
                            arg1 = load32(9147324)
                            store32(9147324, load32(9147316))
                            arg2 = load32(9147320)
                            v10 = load32(9147312)
                            store32(9147320, load32(9147312))
                            arg1 = (arg1 ^ (arg1 << 11))
                            arg1 = ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1)
                            store32(9147316, ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1))
                            arg2 = (arg2 ^ (arg2 << 11))
                            arg2 = ((((((arg2 ^ (arg2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg1 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ arg1)
                            store32(9147312, ((((((arg2 ^ (arg2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg1 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ arg1))
                            arg2 = ((v19 + (arg2 % 3)) - 1)
                            arg2 = (-3 if (arg2 <= -3) else ((v19 + (arg2 % 3)) - 1))
                            v19 = (3 if (arg2 >= 3) else (-3 if (arg2 <= -3) else ((v19 + (arg2 % 3)) - 1)))
                            arg1 = ((v20 + (arg1 % 3)) - 1)
                            arg1 = (-3 if (arg1 <= -3) else ((v20 + (arg1 % 3)) - 1))
                            v20 = (3 if (arg1 >= 3) else (-3 if (arg1 <= -3) else ((v20 + (arg1 % 3)) - 1)))
                            break
                        if v23:
                            arg1 = load32(9142416)
                            arg2 = load32(9142416)
                            if not arg1:
                                arg2 = (load32(41092) if load8u(9147210) else (load32(PLAYER_COUNT) - 1))
                            v33 = func262(i32(v13), i32(v12))
                            # TODO: f32.demote_f64
                            v36 = sqrt(i32(((v13 * v13) + (v12 * v12))))
                            if (sqrt(i32(((v13 * v13) + (v12 * v12)))) >= v38):
                                break
                            # TODO: f32.demote_f64
                            v35 = v33
                            if (v33 < 0.0):
                                break
                            v37 = (6.28318548 / i32((4 if (u32(arg2) < u32(3)) else (arg2 << (arg2 & 1)))))
                            if ((6.28318548 / i32((4 if (u32(arg2) < u32(3)) else (arg2 << (arg2 & 1))))) < v35):
                                break
                            v39 = (v37 - v35)
                            v15 = 0
                            while True:  # $label13
                                arg2 = arg1
                                if not arg1:
                                    arg2 = (load32(41092) if load8u(9147210) else (load32(PLAYER_COUNT) - 1))
                                if (u32(v15) >= u32((4 if (u32(arg2) < u32(3)) else (arg2 << (arg2 & 1))))):
                                    break
                                while True:  # $label7
                                    v40 = ((v37 * i32(v15)) + (v39 if (v15 & 1) else v35))
                                    # TODO: f64.promote_f32
                                    arg2 = load32(9142440)
                                    v33 = i32(((load32(9142440) & 0xFFFFFFFF) >> 1))
                                    v34 = (((func49(((v37 * i32(v15)) + (v39 if (v15 & 1) else v35))) * v36) + 0.5) + i32(((load32(9142440) & 0xFFFFFFFF) >> 1)))
                                    if (abs((((func49(((v37 * i32(v15)) + (v39 if (v15 & 1) else v35))) * v36) + 0.5) + i32(((load32(9142440) & 0xFFFFFFFF) >> 1)))) < 2147483648.0):
                                        break
                                    break
                                v16 = -2147483648
                                while True:  # $label9
                                    while True:  # $label8
                                        # TODO: f64.promote_f32
                                        v33 = (((func48(v40) * v36) + 0.5) + v33)
                                        if (abs((((func48(v40) * v36) + 0.5) + v33)) < 2147483648.0):
                                            break
                                        break
                                    v17 = -2147483648
                                    if (u32(i32(v33)) <= u32(-2147483648)):
                                        break
                                    if (u32(arg2) <= u32(v16)):
                                        break
                                    if ((v16 | v17) < 0):
                                        break
                                    v11 = (v16 - v14)
                                    v29 = (v16 + v21)
                                    if ((v16 - v14) >= (v16 + v21)):
                                        break
                                    v10 = (v17 - v14)
                                    v30 = (v17 + v21)
                                    if ((v17 - v14) >= (v17 + v21)):
                                        break
                                    while True:  # $label12
                                        arg1 = (v11 - v16)
                                        v31 = (((v11 - v16) * arg1) - 1)
                                        arg2 = v10
                                        while True:  # $label11
                                            while True:  # $label10
                                                arg1 = (arg2 - v17)
                                                if ((v31 + ((arg2 - v17) * arg1)) > v25):
                                                    break
                                                arg1 = load32(9142440)
                                                if (u32(load32(9142440)) <= u32(arg2)):
                                                    break
                                                if ((arg2 | v11) < 0):
                                                    break
                                                if (u32(arg1) <= u32(v11)):
                                                    break
                                                store8((load32(9147288) + ((arg1 * arg2) + v11)), arg0)
                                                break
                                            arg2 = (arg2 + 1)
                                            if ((arg2 + 1) != v30):
                                                continue
                                            break
                                        v11 = (v11 + 1)
                                        if ((v11 + 1) != v29):
                                            continue
                                        break
                                    arg1 = load32(9142416)
                                    break
                                v15 = (v15 + 1)
                                continue
                                break
                            raise Unreachable()
                        v11 = (v12 - v14)
                        v15 = (v12 + v21)
                        if ((v12 - v14) >= (v12 + v21)):
                            break
                        arg1 = (v13 - v14)
                        v16 = (v13 + v21)
                        if ((v13 - v14) >= (v13 + v21)):
                            break
                        while True:  # $label16
                            arg2 = (v11 - v12)
                            v17 = (((v11 - v12) * arg2) - 1)
                            arg2 = arg1
                            while True:  # $label15
                                while True:  # $label14
                                    v10 = (arg2 - v13)
                                    if ((v17 + ((arg2 - v13) * v10)) > v25):
                                        break
                                    v10 = load32(9142440)
                                    if (u32(load32(9142440)) <= u32(arg2)):
                                        break
                                    if ((arg2 | v11) < 0):
                                        break
                                    if (u32(v10) <= u32(v11)):
                                        break
                                    store8((load32(9147288) + ((arg2 * v10) + v11)), arg0)
                                    break
                                arg2 = (arg2 + 1)
                                if ((arg2 + 1) != v16):
                                    continue
                                break
                            v11 = (v11 + 1)
                            if ((v11 + 1) != v15):
                                continue
                            break
                        break
                    v22 = (v22 + 1)
                    if (u32((v22 + 1)) < u32(v28)):
                        continue
                    break
            v32 = (v32 + 1)
            if ((v32 + 1) != v26):
                continue
            break
        break
    return arg2

# ----------------------------------------------------------
# $func62
# ----------------------------------------------------------
def func62(arg0, arg1, arg2, arg3):
    v4 = load16u(arg0 + 114)
    while True:  # $label1
        while True:  # $label0
            v5 = load16u(arg0 + 112)
            if (load16u(arg0 + 112) != arg1):
                break
            if (arg2 > v4):
                break
            if (arg2 < v4):
                break
            v4 = (arg2 != v4)
            break
            break
        v4 = (1 if (arg2 > v4) else (-1 if (arg2 < v4) else 0))
        break
    arg1 = (1 if (arg1 > v5) else (-1 if (arg1 < v5) else 0))
    arg2 = 6
    arg1 = (((v4 * 3) + arg1) + 4)
    if (u32((((v4 * 3) + arg1) + 4)) <= u32(8)):
    else:
    store8(load8u((arg1 + 10184)) + 124, 6)
    while True:  # $label3
        while True:  # $label2
            arg1 = load8u(arg0 + 122)
            arg2 = load32(((load8u(arg0 + 122) * 72) + 9263856) + 12)
            if not load32(((load8u(arg0 + 122) * 72) + 9263856) + 12):
                if (load32(38588) != arg1):
                    break
                arg2 = load32(((arg1 * 72) + 9263856) + 8)
                if not load32(((arg1 * 72) + 9263856) + 8):
                    break
            if arg3:
                break
            arg0 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 276)
            func63(func37(arg0, arg2, 0.0, 0), arg0, 10, 0, (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 276) if arg0 else 25))
            return arg0
            break
        func29(arg0, 1)
        break
    return 0

# ----------------------------------------------------------
# $func63
# ----------------------------------------------------------
def func63(arg0, arg1, arg2, arg3, param4):
    v4 = load32(((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) * 40) + 9671200) + 32)
    if load32(((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) * 40) + 9671200) + 32):
    while True:  # $label0
        if (load8u(arg0 + 125) == 3):
            break
        v5 = load32(arg0 + 44)
        if load32(arg0 + 44):
            v6 = load32(9142848)
            v4 = load32(9215884)
            store32((load32(9215884) + (v5 << 4)) + 4, arg1)
            store32((v4 + (load32(arg0 + 44) << 4)) + 8, load32(arg0 + 28))
            store32((v4 + (load32(arg0 + 44) << 4)) + 12, arg2)
            if arg3:
                # TODO: i32.div_u
                store32(v6, (arg3 + 25))
                return
            store32((v4 + (load32(arg0 + 44) << 4)), load32(9142848))
            arg0 = (load32(9215884) + (load32(arg0 + 44) << 4))
            if (load32((load32(9215884) + (load32(arg0 + 44) << 4))) != load32(9142848)):
                break
            store32(arg0, 0)
            return
        store32(arg0 + 44, ((Ua(arg3, arg1, load32(arg0 + 28), arg2) & 0xFFFFFFFF) >> 2))
        break

# ----------------------------------------------------------
# $func65
# ----------------------------------------------------------
def func65(arg0, arg1):
    while True:  # $label0
        if load8u(9147152):
            break
        v3 = load16u(arg0 + 114)
        v4 = load16u(arg0 + 112)
        while True:  # $label1
            if not load8u(59181):
                break
            if not arg1:
                break
            arg1 = load32(arg0 + 44)
            if not load32(arg0 + 44):
                break
            v2 = load32(9215884)
            if (load32((load32(9215884) + (arg1 << 4)) + 12) == 1):
                break
            if (load8u(arg0 + 125) == 7):
                break
            if load32((v2 + ((arg1 << 4) | 4))):
                break
            arg1 = (load8u(arg0 + 124) << 3)
            v3 = (v3 - load32(((load8u(arg0 + 124) << 3) + 8996)))
            v4 = (v4 - load32((arg1 + 8992)))
            break
        arg1 = load32(CURRENT_PLAYER)
        if not load32(CURRENT_PLAYER):
            break
        if not load8u((load32(9143012) + (load16u(arg0 + 110) + (load32(PLAYER_COUNT) * arg1)))):
            break
        v5 = load8u(arg0 + 125)
        if (load8u(arg0 + 125) == 3):
            break
        arg0 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        arg1 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 220)
        v2 = load32(arg0 + 216)
        while True:  # $label4
            while True:  # $label3
                while True:  # $label2
                    # br_table (v5 - 4)
                    break
                    break
                break
                break
            break
        arg0 = load32(arg0 + 200)
        if not load32(arg0 + 200):
            break
        if not load32(load32(GAME_STATE) + 48):
            break
        v5 = (load32(9142836) + (arg0 * 80))
        v6 = load32((load32(9142836) + (arg0 * 80)) + 324)
        if not load32((load32(9142836) + (arg0 * 80)) + 324):
            break
        v7 = (((arg1 & 0xFFFFFFFF) >> 1) + v3)
        v8 = (((v2 & 0xFFFFFFFF) >> 1) + v4)
        v9 = (arg0 * arg0)
        arg0 = 0
        while True:  # $label6
            while True:  # $label5
                v10 = load32(9142440)
                v3 = load32(v5 + 320)
                v2 = (arg0 << 2)
                v4 = load32((load32(v5 + 320) + ((arg0 << 2) | 4)))
                arg1 = (v7 + load32((load32(v5 + 320) + ((arg0 << 2) | 4))))
                if (u32(load32(9142440)) <= u32((v7 + load32((load32(v5 + 320) + ((arg0 << 2) | 4)))))):
                    break
                v2 = load32((v2 + v3))
                v3 = (v8 + load32((v2 + v3)))
                if (u32(v10) <= u32((v8 + load32((v2 + v3))))):
                    break
                if ((arg1 | v3) < 0):
                    break
                if (v9 >= (((v2 * v2) + (v4 * v4)) - 1)):
                    break
                func258(v3, arg1)
                break
            arg0 = (arg0 + 2)
            if (u32((arg0 + 2)) < u32(v6)):
                continue
            break
        break
    return func129(v3, arg1, 1)

# ----------------------------------------------------------
# $func66
# ----------------------------------------------------------
def func66(arg0, arg1, arg2, arg3):
    v6 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # $label0
        if not arg2:
            break
        if (load32(arg0 + 283908) != load32(CURRENT_PLAYER)):
            break
        while True:  # $label1
            arg2 = load32(arg1)
            if not load32(arg1):
                break
            if (load32(v6 + 64) >= arg2):
                break
            store32(v6 + 48, 0)
            a_b()
            break
        while True:  # $label2
            arg2 = load32(arg1 + 4)
            if not load32(arg1 + 4):
                break
            if (load32(v6 + 68) >= arg2):
                break
            store32(v6 + 32, 1)
            a_b()
            break
        while True:  # $label3
            arg2 = load32(arg1 + 8)
            if not load32(arg1 + 8):
                break
            if (load32(v6 + 72) >= arg2):
                break
            store32(v6 + 16, 2)
            a_b()
            break
        arg2 = load32(arg1 + 12)
        if not load32(arg1 + 12):
            break
        if (load32(v6 + 76) >= arg2):
            break
        store32(v6, 3)
        a_b()
        break
    arg2 = 1
    while True:  # $label4
        v4 = load32(arg1)
        if load32(arg1):
            if (load32(v6 + 64) < v4):
                break
        v5 = load32(arg1 + 4)
        if load32(arg1 + 4):
            if (load32(v6 + 68) < v5):
                break
        v5 = load32(arg1 + 8)
        if load32(arg1 + 8):
            if (load32(v6 + 72) < v5):
                break
        v5 = load32(arg1 + 12)
        if load32(arg1 + 12):
            if (load32(v6 + 76) < v5):
                break
        v10 = load32(9143016)
        while True:  # $label5
            if (load32(v6 + 64) == 2147483647):
                break
            if not v4:
                break
            if arg3:
                arg2 = (arg0 + 281692)
                store32((arg0 + 281692), (load32(arg2) + v4))
                v4 = load32(arg1)
            arg2 = load32(arg0 + 283848)
            v5 = (v4 - load32(arg0 + 283848))
            if ((v4 - load32(arg0 + 283848)) <= 0):
                store32(arg0 + 283848, (arg2 - v4))
                break
            store32(arg0 + 283848, 0)
            arg2 = (arg0 + 281708)
            store32((arg0 + 281708), (load32(arg2) + v5))
            v4 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            v7 = load32(PLAYERS)
            arg2 = 1
            while True:  # $label7
                while True:  # $label6
                    if (load8u((v10 + (load32(arg0 + 283908) + (arg2 * v4)))) & 1):
                        v8 = (v7 + (arg2 * 286704))
                        v9 = ((v7 + (arg2 * 286704)) + 283848)
                        v4 = load32(v8 + 283848)
                        if (v5 <= load32(v8 + 283848)):
                            break
                        v8 = (v8 + 281724)
                        store32((v8 + 281724), (load32(v8) + v4))
                        store32(v9, 0)
                        v5 = (v5 - v4)
                        v4 = load32(PLAYER_COUNT)
                    arg2 = (arg2 + 1)
                    if (u32((arg2 + 1)) < u32(v4)):
                        continue
                    break
                    break
                break
            store32(v9, (v4 - v5))
            arg2 = ((v7 + (arg2 * 286704)) + 281724)
            store32(((v7 + (arg2 * 286704)) + 281724), (load32(arg2) + v5))
            break
        while True:  # $label8
            if (load32(v6 + 68) == 2147483647):
                break
            arg2 = load32(arg1 + 4)
            if not load32(arg1 + 4):
                break
            if arg3:
                v4 = (arg0 + 281696)
                store32((arg0 + 281696), (load32(v4) + arg2))
                arg2 = load32(arg1 + 4)
            v4 = load32((arg0 + 283852))
            v5 = (arg2 - load32((arg0 + 283852)))
            if ((arg2 - load32((arg0 + 283852))) > 0):
                store32(arg0 + 283852, 0)
                arg2 = (arg0 + 281712)
                store32((arg0 + 281712), (load32(arg2) + v5))
                v4 = load32(PLAYER_COUNT)
                if (u32(load32(PLAYER_COUNT)) < u32(2)):
                    break
                v7 = load32(PLAYERS)
                arg2 = 1
                while True:  # $label9
                    if (load8u((v10 + (load32(arg0 + 283908) + (arg2 * v4)))) & 2):
                        v9 = (v7 + (arg2 * 286704))
                        v8 = ((v7 + (arg2 * 286704)) + 283852)
                        v4 = load32(((v7 + (arg2 * 286704)) + 283852))
                        if (load32(((v7 + (arg2 * 286704)) + 283852)) >= v5):
                            store32(v8, (v4 - v5))
                            arg2 = ((v7 + (arg2 * 286704)) + 281728)
                            store32(((v7 + (arg2 * 286704)) + 281728), (load32(arg2) + v5))
                            break
                        v9 = (v9 + 281728)
                        store32((v9 + 281728), (load32(v9) + v4))
                        store32(v8, 0)
                        v5 = (v5 - v4)
                        v4 = load32(PLAYER_COUNT)
                    arg2 = (arg2 + 1)
                    if (u32((arg2 + 1)) < u32(v4)):
                        continue
                    break
                break
            store32(arg0 + 283852, (v4 - arg2))
            break
        while True:  # $label10
            if (load32(v6 + 72) == 2147483647):
                break
            arg2 = load32(arg1 + 8)
            if not load32(arg1 + 8):
                break
            if arg3:
                v4 = (arg0 + 281700)
                store32((arg0 + 281700), (load32(v4) + arg2))
                arg2 = load32(arg1 + 8)
            v4 = load32((arg0 + 283856))
            v5 = (arg2 - load32((arg0 + 283856)))
            if ((arg2 - load32((arg0 + 283856))) > 0):
                store32(arg0 + 283856, 0)
                arg2 = (arg0 + 281716)
                store32((arg0 + 281716), (load32(arg2) + v5))
                v4 = load32(PLAYER_COUNT)
                if (u32(load32(PLAYER_COUNT)) < u32(2)):
                    break
                v7 = load32(PLAYERS)
                arg2 = 1
                while True:  # $label11
                    if (load8u((v10 + (load32(arg0 + 283908) + (arg2 * v4)))) & 4):
                        v9 = (v7 + (arg2 * 286704))
                        v8 = ((v7 + (arg2 * 286704)) + 283856)
                        v4 = load32(((v7 + (arg2 * 286704)) + 283856))
                        if (load32(((v7 + (arg2 * 286704)) + 283856)) >= v5):
                            store32(v8, (v4 - v5))
                            arg2 = ((v7 + (arg2 * 286704)) + 281732)
                            store32(((v7 + (arg2 * 286704)) + 281732), (load32(arg2) + v5))
                            break
                        v9 = (v9 + 281732)
                        store32((v9 + 281732), (load32(v9) + v4))
                        store32(v8, 0)
                        v5 = (v5 - v4)
                        v4 = load32(PLAYER_COUNT)
                    arg2 = (arg2 + 1)
                    if (u32((arg2 + 1)) < u32(v4)):
                        continue
                    break
                break
            store32(arg0 + 283856, (v4 - arg2))
            break
        arg2 = 0
        if (load32(v6 + 76) == 2147483647):
            break
        v4 = load32(arg1 + 12)
        if not load32(arg1 + 12):
            break
        if arg3:
            arg3 = (arg0 + 281704)
            store32((arg0 + 281704), (load32(arg3) + v4))
            v4 = load32(arg1 + 12)
        arg1 = load32((arg0 + 283860))
        arg3 = (v4 - load32((arg0 + 283860)))
        if ((v4 - load32((arg0 + 283860))) > 0):
            store32(arg0 + 283860, 0)
            arg1 = (arg0 + 281720)
            store32((arg0 + 281720), (load32(arg1) + arg3))
            v4 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            v5 = load32(PLAYERS)
            arg1 = 1
            while True:  # $label12
                if (load8u((v10 + (load32(arg0 + 283908) + (arg1 * v4)))) & 8):
                    v7 = (v5 + (arg1 * 286704))
                    v4 = ((v5 + (arg1 * 286704)) + 283860)
                    arg2 = load32(((v5 + (arg1 * 286704)) + 283860))
                    if (load32(((v5 + (arg1 * 286704)) + 283860)) >= arg3):
                        store32(v4, (arg2 - arg3))
                        arg0 = ((v5 + (arg1 * 286704)) + 281736)
                        store32(((v5 + (arg1 * 286704)) + 281736), (load32(arg0) + arg3))
                        arg2 = 0
                        break
                    v7 = (v7 + 281736)
                    store32((v7 + 281736), (load32(v7) + arg2))
                    store32(v4, 0)
                    v4 = load32(PLAYER_COUNT)
                    arg3 = (arg3 - arg2)
                arg2 = 0
                arg1 = (arg1 + 1)
                if (u32((arg1 + 1)) < u32(v4)):
                    continue
                break
            break
        store32(arg0 + 283860, (arg1 - v4))
        break
    G.global0 = (v6 + 80)
    return arg2

# ----------------------------------------------------------
# $func67
# ----------------------------------------------------------
def func67(arg0):
    v3 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # $label0
        if load8u(9142917):
            break
        while True:  # $label2
            while True:  # $label1
                v4 = load8u(arg0 + 125)
                # br_table (load8u(arg0 + 125) - 4)
                break
                break
            while True:  # $label3
                v2 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
                v1 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 356)
                if load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 356):
                    break
                v1 = load32(v2 + 216)
                v2 = load32(v2 + 220)
                v1 = (load32(v2 + 216) if (u32(v1) > u32(v2)) else load32(v2 + 220))
                v1 = ((6 if (u32(v1) >= u32(6)) else (load32(v2 + 216) if (u32(v1) > u32(v2)) else load32(v2 + 220))) - 1)
                if (u32(((6 if (u32(v1) >= u32(6)) else (load32(v2 + 216) if (u32(v1) > u32(v2)) else load32(v2 + 220))) - 1)) > u32(4)):
                    v1 = 9142636
                    break
                v1 = load32(((v1 << 2) + 10132))
                break
            v1 = load32(v1)
            break
        v2 = load8u(arg0 + 122)
        if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 6):
            v5 = load32(((v2 * 72) + 9263856) + 8)
            v1 = (load32(((v2 * 72) + 9263856) + 8) if v5 else v1)
        v4 = ((v4 != 4) & (v4 != 14))
        while True:  # $label4
            if not ((load32(38600) == v2) | (load32(38472) == v2)):
                break
            if v1:
                break
            v1 = load32(((v2 * 72) + 9263856))
            store8(arg0 + 124, 0)
            break
        if (load8u(arg0 + 129) == 8):
        if v1:
            break
        v1 = load8u(arg0 + 122)
        if (load8u(arg0 + 125) == 1):
            v1 = load32(((v1 * 404) + ENTITY_TYPES) + 260)
            if load32(((v1 * 404) + ENTITY_TYPES) + 260):
                v2 = (32000 // v1)
            else:
            v9 = (i32(((32000 // v1) - (i32(v2) % 25))) / 1.0)
            v2 = (load8u(arg0 + 124) << 3)
            v6 = i32(load32(((load8u(arg0 + 124) << 3) + 8996)))
            v7 = ((i32(((32000 // v1) - (i32(v2) % 25))) / 1.0) * i32(load32(((load8u(arg0 + 124) << 3) + 8996))))
            v9 = i32(load32((v2 + 8992)))
            v10 = (v9 * i32(load32((v2 + 8992))))
            v2 = (load32((load32(9215884) + (load32(arg0 + 44) << 4))) * 25)
            if v1:
                v1 = (32000 // v1)
            else:
            v11 = i32((-1 + v2))
            # TODO: f64.promote_f32
            v12 = v7
            # TODO: f64.promote_f32
            v13 = v10
            v1 = load32(arg0 + 40)
            while True:  # $label5
                if load8u(9142916):
                    store32(v3 + 72, v1)
                    store64((v3 - -64), 0)
                    storef64(v3 + 56, v12)
                    storef64(v3 + 48, v13)
                    a_b()
                    break
                store32(v3 + 32, v1)
                # TODO: f64.promote_f32
                storef64(v3 + 24, v11)
                store64(v3 + 16, 0)
                storef64(v3 + 8, v12)
                storef64(v3, v13)
                a_b()
                break
            while True:  # $label6
                v8 = (i32(load16u(arg0 + 112)) - v9)
                if (((i32(load16u(arg0 + 112)) - v9) < 4294967300.0) & (v8 >= 0.0)):
                    break
                break
            store16(i32(v8) + 112, 0)
            while True:  # $label7
                v8 = (i32(load16u(arg0 + 114)) - v6)
                if (((i32(load16u(arg0 + 114)) - v6) < 4294967300.0) & (v8 >= 0.0)):
                    break
                break
            store16(i32(v8) + 114, 0)
            if load8u(9142916):
            func288(arg0, v10, v7)
            while True:  # $label8
                v7 = (v9 + i32(load16u(arg0 + 112)))
                if (((v9 + i32(load16u(arg0 + 112))) < 4294967300.0) & (v7 >= 0.0)):
                    break
                break
            store16(i32(v7) + 112, 0)
            v6 = (v6 + i32(load16u(arg0 + 114)))
            if (((v6 + i32(load16u(arg0 + 114))) < 4294967300.0) & (v6 >= 0.0)):
                store16(arg0 + 114, i32(v6))
                break
            store16(arg0 + 114, 0)
            break
        while True:  # $label10
            while True:  # $label9
                while True:  # $label11
                    # br_table (v1 + -64)
                    break
                    break
                if (v1 != 10):
                    break
                break
            while True:  # $label12
                while True:  # $label13
                    v2 = load32(9215884)
                    v4 = load32(arg0 + 44)
                    # br_table (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) - 1)
                    break
                    break
                break
                break
            while True:  # $label14
                v2 = entities[load32((v2 + ((v4 << 4) | 12)))]
                if (load8u(entities[load32((v2 + ((v4 << 4) | 12)))].unit_class) == 10):
                    break
                while True:  # $label16
                    while True:  # $label15
                        v2 = load8u(v2 + 122)
                        # br_table (load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 188) - 1)
                        break
                        break
                    break
                    break
                if (v2 == load32(38500)):
                    break
                break
                break
            break
            break
        break
    G.global0 = (v3 + 80)
    return func86(arg0)
