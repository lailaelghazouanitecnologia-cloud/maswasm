"""
Tzar Engine - Core module (part 9).
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
# $func301
# ----------------------------------------------------------
def func301(arg0, arg1, arg2, arg3):
    v7 = (load32(PLAYER_COUNT) * arg2)
    v21 = load32(9142440)
    v13 = (load32(9142440) + 2)
    v23 = ((load32(9142440) + 2) << 1)
    v8 = load32(9215884)
    v15 = load32(38564)
    v16 = load32(38620)
    v17 = load32(38560)
    v9 = load32(9143004)
    v18 = load32(38500)
    v10 = load32(ENTITIES)
    v19 = load32(9142840)
    arg2 = 0
    while True:  # $label3
        while True:  # $label7
            while True:  # $label0
                v22 = arg2
                v4 = (arg2 << 2)
                arg2 = (load32((((arg2 << 2) | 4) + 8611904)) + arg1)
                if (u32(v21) <= u32((load32((((arg2 << 2) | 4) + 8611904)) + arg1))):
                    break
                v4 = (load32((v4 + 8611904)) + arg0)
                if (u32(v21) <= u32((load32((v4 + 8611904)) + arg0))):
                    break
                if ((arg2 | v4) < 0):
                    break
                while True:  # $label1
                    v11 = (v4 + 1)
                    v14 = (arg2 + 1)
                    arg2 = load32((v19 + (((v4 + 1) + ((arg2 + 1) * v13)) << 2)))
                    if (u32(load32((v19 + (((v4 + 1) + ((arg2 + 1) * v13)) << 2)))) < u32(3)):
                        break
                    v4 = (v10 + (arg2 * 132))
                    v6 = load8u((v10 + (arg2 * 132)) + 122)
                    v12 = ((load8u((v10 + (arg2 * 132)) + 122) * 404) + ENTITY_TYPES)
                    if not load32(((load8u((v10 + (arg2 * 132)) + 122) * 404) + ENTITY_TYPES) + 340):
                        break
                    if (v6 == v18):
                        break
                    v5 = load16u(v4 + 110)
                    while True:  # $label2
                        v20 = load16u(v4 + 120)
                        if load16u(v4 + 120):
                        else:
                        if not load8u(((v20 if load8u((v9 + (v5 + v7))) else v5) + (v5 + v7))):
                            if (load8u(v4 + 127) != 6):
                                break
                            if not load8u(v4 + 128):
                                break
                            break
                        if load8u(v4 + 128):
                            break
                        break
                    if (load8u(v4 + 125) == 10):
                        break
                    if (load8u(v4 + 126) == 2):
                        break
                    if (load32(v4 + 64) == -1):
                        break
                    if (load32(v12 + 264) == 2):
                        break
                    if (load32(v12 + 188) != 55):
                        break
                    if (v6 == v17):
                        break
                    if (v6 == v16):
                        break
                    if (v6 == v15):
                        break
                    if not ((arg3 == -1) | (arg3 == v6)):
                        break
                    v5 = load32(v4 + 104)
                    if not load32(v4 + 104):
                        break
                    v5 = load32((v10 + (v5 * 132)) + 44)
                    if (load32((v8 + (load32((v10 + (v5 * 132)) + 44) << 4)) + 4) != 40):
                        break
                    if (load32((v8 + ((v5 << 4) | 12))) != load32(v4 + 28)):
                        break
                    break
                while True:  # $label4
                    arg2 = load32((v19 + ((v11 + ((v13 + v14) * v13)) << 2)))
                    if (u32(load32((v19 + ((v11 + ((v13 + v14) * v13)) << 2)))) < u32(3)):
                        break
                    v4 = (v10 + (arg2 * 132))
                    v6 = load8u((v10 + (arg2 * 132)) + 122)
                    v12 = ((load8u((v10 + (arg2 * 132)) + 122) * 404) + ENTITY_TYPES)
                    if not load32(((load8u((v10 + (arg2 * 132)) + 122) * 404) + ENTITY_TYPES) + 340):
                        break
                    if (v6 == v18):
                        break
                    v5 = load16u(v4 + 110)
                    while True:  # $label5
                        v20 = load16u(v4 + 120)
                        if load16u(v4 + 120):
                        else:
                        if load8u(((v20 if load8u((v9 + (v5 + v7))) else v5) + (v5 + v7))):
                            if not load8u(v4 + 128):
                                break
                            break
                        if (load8u(v4 + 127) != 6):
                            break
                        if load8u(v4 + 128):
                            break
                        break
                    if (load8u(v4 + 125) == 10):
                        break
                    if (load8u(v4 + 126) == 2):
                        break
                    if (load32(v4 + 64) == -1):
                        break
                    if (load32(v12 + 264) == 2):
                        break
                    if (load32(v12 + 188) != 55):
                        break
                    if (v6 == v17):
                        break
                    if (v6 == v16):
                        break
                    if (v6 == v15):
                        break
                    if not ((arg3 == -1) | (arg3 == v6)):
                        break
                    v5 = load32(v4 + 104)
                    if not load32(v4 + 104):
                        break
                    v5 = load32((v10 + (v5 * 132)) + 44)
                    if (load32((v8 + (load32((v10 + (v5 * 132)) + 44) << 4)) + 4) != 40):
                        break
                    if (load32((v8 + ((v5 << 4) | 12))) != load32(v4 + 28)):
                        break
                    break
                arg2 = load32((v19 + ((v11 + ((v14 + v23) * v13)) << 2)))
                if (u32(load32((v19 + ((v11 + ((v14 + v23) * v13)) << 2)))) < u32(3)):
                    break
                v4 = (v10 + (arg2 * 132))
                v5 = load8u((v10 + (arg2 * 132)) + 122)
                v11 = ((load8u((v10 + (arg2 * 132)) + 122) * 404) + ENTITY_TYPES)
                if not load32(((load8u((v10 + (arg2 * 132)) + 122) * 404) + ENTITY_TYPES) + 340):
                    break
                if (v5 == v18):
                    break
                v6 = load16u(v4 + 110)
                while True:  # $label6
                    v14 = load16u(v4 + 120)
                    if load16u(v4 + 120):
                    else:
                    if load8u(((v14 if load8u((v9 + (v6 + v7))) else v6) + (v6 + v7))):
                        if not load8u(v4 + 128):
                            break
                        break
                    if (load8u(v4 + 127) != 6):
                        break
                    if load8u(v4 + 128):
                        break
                    break
                if (load8u(v4 + 125) == 10):
                    break
                if (load8u(v4 + 126) == 2):
                    break
                if (load32(v4 + 64) == -1):
                    break
                if (load32(v11 + 264) == 2):
                    break
                if (load32(v11 + 188) != 55):
                    break
                if (v5 == v17):
                    break
                if (v5 == v16):
                    break
                if (v5 == v15):
                    break
                if not ((arg3 == -1) | (arg3 == v5)):
                    break
                v5 = load32(v4 + 104)
                if not load32(v4 + 104):
                    break
                v5 = load32((v10 + (v5 * 132)) + 44)
                if (load32((v8 + (load32((v10 + (v5 * 132)) + 44) << 4)) + 4) != 40):
                    break
                if (load32((v8 + ((v5 << 4) | 12))) != load32(v4 + 28)):
                    break
                break
            arg2 = (v22 + 2)
            if (u32(v22) < u32(5198)):
                continue
            break
        arg2 = 0
        break
    return arg2

# ----------------------------------------------------------
# $cc
# Export: cc
# ----------------------------------------------------------
def cc():
    """Export: cc"""
    while True:  # $label0
        v3 = load32(9671136)
        v12 = load8u(9671158)
        v14 = (3 if load8u(9671158) else 2)
        v10 = load8u(9671157)
        v11 = not load8u(9671157)
        v2 = load32(9142440)
        if (u32(load32(9671136)) <= u32((((3 if load8u(9671158) else 2) - not load8u(9671157)) * (load32(9142440) * v2)))):
            if (u32(v3) < u32(4)):
                break
            v6 = load32(38448)
            v7 = load32(ENTITIES)
            v1 = 3
            while True:  # $label2
                while True:  # $label1
                    v4 = (v7 + (v1 * 132))
                    if (load8u((v7 + (v1 * 132)) + 125) == 3):
                        break
                    if (v6 == load8u(v4 + 122)):
                        break
                    v4 = load16u(v4 + 112)
                    v0 = (((((load16u(v4 + 114) + (v2 * load16u(v4 + 112))) * v2) + v4) * v1) + v0)
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v3):
                    continue
                break
            break
        if not v2:
            break
        v7 = load32(9142840)
        v6 = (v2 + 2)
        v8 = (0 if v10 else (v2 + 2))
        v15 = (v2 & -2)
        v13 = (v2 & 1)
        v16 = (v2 - 1)
        while True:  # $label5
            v4 = v1
            v9 = (v1 * v2)
            v1 = (v1 + 1)
            v3 = 0
            v5 = 0
            if v16:
                while True:  # $label3
                    v18 = (v3 | 1)
                    v17 = load32((v7 + ((v1 + (((v3 | 1) + v8) * v6)) << 2)))
                    if load32((v7 + ((v1 + (((v3 | 1) + v8) * v6)) << 2))):
                        v0 = ((v17 * (((v3 + v9) * v2) + v4)) + v0)
                    v3 = (v3 + 2)
                    v17 = load32((v7 + ((v1 + (((v3 + 2) + v8) * v6)) << 2)))
                    if load32((v7 + ((v1 + (((v3 + 2) + v8) * v6)) << 2))):
                        v0 = ((v17 * (((v9 + v18) * v2) + v4)) + v0)
                    v5 = (v5 + 2)
                    if ((v5 + 2) != v15):
                        continue
                    break
            while True:  # $label4
                if not v13:
                    break
                v5 = load32((v7 + ((v1 + (((v3 + v8) + 1) * v6)) << 2)))
                if not load32((v7 + ((v1 + (((v3 + v8) + 1) * v6)) << 2))):
                    break
                v0 = ((v5 * (((v3 + v9) * v2) + v4)) + v0)
                break
            if (v1 != v2):
                continue
            break
        if not (v10 | v12):
            break
        v12 = (v2 & -2)
        v15 = (v2 & 1)
        v8 = (v6 << v11)
        v1 = 0
        while True:  # $label8
            v4 = v1
            v9 = (v1 * v2)
            v1 = (v1 + 1)
            v3 = 0
            v5 = 0
            if v16:
                while True:  # $label6
                    v11 = (v3 | 1)
                    v13 = load32((v7 + ((v1 + (((v3 | 1) + v8) * v6)) << 2)))
                    if load32((v7 + ((v1 + (((v3 | 1) + v8) * v6)) << 2))):
                        v0 = ((v13 * (((v3 + v9) * v2) + v4)) + v0)
                    v3 = (v3 + 2)
                    v13 = load32((v7 + ((v1 + (((v3 + 2) + v8) * v6)) << 2)))
                    if load32((v7 + ((v1 + (((v3 + 2) + v8) * v6)) << 2))):
                        v0 = ((v13 * (((v9 + v11) * v2) + v4)) + v0)
                    v5 = (v5 + 2)
                    if ((v5 + 2) != v12):
                        continue
                    break
            while True:  # $label7
                if not v15:
                    break
                v5 = load32((v7 + ((v1 + (((v3 + v8) + 1) * v6)) << 2)))
                if not load32((v7 + ((v1 + (((v3 + v8) + 1) * v6)) << 2))):
                    break
                v0 = ((v5 * (((v3 + v9) * v2) + v4)) + v0)
                break
            if (v1 != v2):
                continue
            break
        v1 = (2 if v10 else 3)
        if ((2 if v10 else 3) == v14):
            break
        v9 = (v2 & -2)
        v12 = (v2 & 1)
        v10 = (v1 * v6)
        v1 = 0
        while True:  # $label11
            v4 = v1
            v8 = (v1 * v2)
            v1 = (v1 + 1)
            v3 = 0
            v5 = 0
            if v16:
                while True:  # $label9
                    v14 = (v3 | 1)
                    v11 = load32((v7 + ((v1 + (((v3 | 1) + v10) * v6)) << 2)))
                    if load32((v7 + ((v1 + (((v3 | 1) + v10) * v6)) << 2))):
                        v0 = ((v11 * (((v3 + v8) * v2) + v4)) + v0)
                    v3 = (v3 + 2)
                    v11 = load32((v7 + ((v1 + (((v3 + 2) + v10) * v6)) << 2)))
                    if load32((v7 + ((v1 + (((v3 + 2) + v10) * v6)) << 2))):
                        v0 = ((v11 * (((v8 + v14) * v2) + v4)) + v0)
                    v5 = (v5 + 2)
                    if ((v5 + 2) != v9):
                        continue
                    break
            while True:  # $label10
                if not v12:
                    break
                v5 = load32((v7 + ((v1 + (((v3 + v10) + 1) * v6)) << 2)))
                if not load32((v7 + ((v1 + (((v3 + v10) + 1) * v6)) << 2))):
                    break
                v0 = ((v5 * (((v3 + v8) * v2) + v4)) + v0)
                break
            if (v1 != v2):
                continue
            break
        break
    return v0

# ----------------------------------------------------------
# $func304
# ----------------------------------------------------------
def func304(arg0):
    while True:  # $label2
        while True:  # $label1
            while True:  # $label0
                # br_table (load8u(arg0 + 125) - 4)
                break
                break
            return
            break
        store8(arg0 + 125, 0)
        v3 = load32(PLAYERS)
        v5 = load16u(arg0 + 110)
        v2 = players[load16u(arg0 + 110)]
        v7 = load32(9215884)
        v1 = load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 12)
        store32(((players[load16u(arg0 + 110)] + (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 12) << 2)) + 282828), 0)
        v1 = ((v1 * 404) + 9568164)
        v4 = load32(v2 + 283848)
        if (load32(v2 + 283848) != 2147483647):
            store32((v2 + 283848), (load32(v1) + v4))
        v2 = (v2 + 283852)
        v4 = load32((v2 + 283852))
        if (load32((v2 + 283852)) != 2147483647):
            store32(v2, (load32(v1 + 4) + v4))
        v2 = (v3 + (v5 * 286704))
        v4 = ((v3 + (v5 * 286704)) + 283856)
        v6 = load32(((v3 + (v5 * 286704)) + 283856))
        if (load32(((v3 + (v5 * 286704)) + 283856)) != 2147483647):
            store32(v4, (load32(v1 + 8) + v6))
        v2 = (v2 + 283860)
        v4 = load32((v2 + 283860))
        if (load32((v2 + 283860)) != 2147483647):
            store32(v2, (load32(v1 + 12) + v4))
        v2 = (v3 + (v5 * 286704))
        v3 = ((v3 + (v5 * 286704)) + 281692)
        store32(((v3 + (v5 * 286704)) + 281692), (load32(v3) - load32(v1)))
        v3 = (v2 + 281696)
        store32((v2 + 281696), (load32(v3) - load32(v1 + 4)))
        v3 = (v2 + 281700)
        store32((v2 + 281700), (load32(v3) - load32(v1 + 8)))
        v3 = load32(v1 + 12)
        v1 = 1
        store8(v2 + 286701, 1)
        v5 = (v2 + 281704)
        store32((v2 + 281704), (load32(v5) - v3))
        while True:  # $label3
            v3 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            v6 = (v3 - 1)
            v8 = ((v3 - 1) & 1)
            v2 = (load32(v2 + 283908) * v3)
            v5 = load32(PLAYERS)
            v4 = load32(9143016)
            if (v3 != 2):
                v6 = (v6 & -2)
                v3 = 0
                while True:  # $label4
                    if load8u((v4 + (v1 + v2))):
                        store8((v5 + (v1 * 286704)) + 286701, 1)
                    v9 = (v1 + 1)
                    if load8u((v4 + ((v1 + 1) + v2))):
                        store8((v5 + (v9 * 286704)) + 286701, 1)
                    v1 = (v1 + 2)
                    v3 = (v3 + 2)
                    if ((v3 + 2) != v6):
                        continue
                    break
            if not v8:
                break
            if not load8u((v4 + (v1 + v2))):
                break
            store8((v5 + (v1 * 286704)) + 286701, 1)
            break
        v1 = load32(arg0 + 44)
        if load32(arg0 + 44):
            store32((v7 + (v1 << 4)), 0)
        store32(arg0 + 44, 0)
        while True:  # $label5
            if not load32(arg0 + 92):
                break
            v1 = load8u(9147141)
            if load32(9140316):
                if (load32(9140320) != load32(arg0 + 28)):
                    break
            break
        return
        break
    while True:  # $label7
        while True:  # $label9
            while True:  # $label8
                while True:  # $label6
                    v6 = load32(9215884)
                    v1 = load32(arg0 + 44)
                    v2 = load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4)
                    # br_table load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4)
                    break
                    break
                store8(arg0 + 123, 0)
                store32(arg0 + 32, 0)
                store32(arg0 + 116, load32(arg0 + 112))
                arg0 = load32(arg0 + 20)
                if not load32(arg0 + 20):
                    break
                if (u32(load32(arg0 + 8)) < u32(3)):
                    break
                if (u32((load32(load32(arg0)) - 1)) > u32(1)):
                    break
                store32(arg0 + 8, 0)
                return
                break
            store8(arg0 + 129, 11)
            return
            break
        if (v2 != 34):
            break
        while True:  # $label10
            v5 = load32(PLAYERS)
            v4 = load16u(arg0 + 110)
            v2 = players[load16u(arg0 + 110)]
            v3 = load32(players[load16u(arg0 + 110)] + 283848)
            if (load32(players[load16u(arg0 + 110)] + 283848) == 2147483647):
                break
            store32((v2 + 283848), (load16u((v6 + ((v1 << 4) | 12)) + 2) + v3))
            v1 = 1
            store8(v2 + 286701, 1)
            v3 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            v8 = (v3 - 1)
            v9 = ((v3 - 1) & 1)
            v5 = (load32((v5 + (v4 * 286704)) + 283908) * v3)
            v4 = load32(PLAYERS)
            v7 = load32(9143016)
            if (v3 != 2):
                v3 = (v8 & -2)
                while True:  # $label11
                    if load8u((v7 + (v1 + v5))):
                        store8((v4 + (v1 * 286704)) + 286701, 1)
                    v8 = (v1 + 1)
                    if load8u((v7 + ((v1 + 1) + v5))):
                        store8((v4 + (v8 * 286704)) + 286701, 1)
                    v1 = (v1 + 2)
                    v10 = (v10 + 2)
                    if ((v10 + 2) != v3):
                        continue
                    break
            if not v9:
                break
            if not load8u((v7 + (v1 + v5))):
                break
            store8((v4 + (v1 * 286704)) + 286701, 1)
            break
        store32(v2 + 283912, (load32(v2 + 283912) - 1))
        v1 = load32(arg0 + 44)
        if load32(arg0 + 44):
            store32((v6 + (v1 << 4)), 0)
        store32(arg0 + 44, 0)
        if not load32(arg0 + 92):
            break
        v1 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32(arg0 + 28)):
                break
        break

# ----------------------------------------------------------
# $func306
# ----------------------------------------------------------
def func306(arg0):

# ----------------------------------------------------------
# $func307
# ----------------------------------------------------------
def func307(arg0):
    store32(arg0, 32988)
    v1 = (load32(arg0 + 4) - 12)
    # TODO: i32.atomic.rmw.add
    if ((-1 - 1) < 0):
    return arg0

# ----------------------------------------------------------
# $func308
# ----------------------------------------------------------
def func308(arg0, arg1):
    v4 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # $label0
        v7 = (v4 + 32)
        v3 = (v4 + 32)
        v2 = (v4 + 21)
        v5 = ((v4 + 32) - (v4 + 21))
        if (((v4 + 32) - (v4 + 21)) <= 9):
            v6 = (((32 - clz((arg1 | 1))) * 1233) >> 12)
            if (v5 < ((((32 - clz((arg1 | 1))) * 1233) >> 12) + (u32(load32(((v6 << 2) + 32256))) <= u32(arg1)))):
                break
        while True:  # $label1
            if (u32(arg1) <= u32(999999)):
                if (u32(arg1) <= u32(9999)):
                    if (u32(arg1) <= u32(99)):
                        if (u32(arg1) <= u32(9)):
                            store8(v2, (arg1 + 48))
                            break
                        break
                    if (u32(arg1) <= u32(999)):
                        # TODO: i32.div_u
                        v3 = 100
                        store8(arg1, 148)
                        break
                    break
                if (u32(arg1) <= u32(99999)):
                    # TODO: i32.div_u
                    v3 = 10000
                    store8(arg1, 10048)
                    break
                break
            if (u32(arg1) <= u32(99999999)):
                if (u32(arg1) <= u32(9999999)):
                    # TODO: i32.div_u
                    v3 = 1000000
                    store8(arg1, 1000048)
                    break
                break
            if (u32(arg1) <= u32(999999999)):
                # TODO: i32.div_u
                v3 = 100000000
                store8(arg1, 100000048)
                break
            # TODO: i32.div_u
            v3 = 100000000
            break
        v3 = func213(func104(arg1, 100000000), (arg1 - (v3 * 100000000)))
        break
    store32(v2 + 16, 0)
    store32(v4 + 12, v3)
    v5 = load32(v4 + 12)
    v6 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label4
        v3 = (v5 - v2)
        if (u32((v5 - v2)) <= u32(2147483631)):
            while True:  # $label2
                if (u32(v3) < u32(11)):
                    store8(arg0 + 11, ((load8u(arg0 + 11) & 128) | v3))
                    store8(arg0 + 11, (load8u(arg0 + 11) & 127))
                    arg1 = arg0
                    break
                if (u32(v3) >= u32(11)):
                    arg1 = ((v3 + 16) & -16)
                    arg1 = (arg1 - 1)
                else:
                func314(arg0, (((v3 + 16) & -16) if (arg1 == 11) else (arg1 - 1)), 11)
                arg1 = load32(v4 + 8)
                store32(arg0, load32(v4 + 8))
                store32(arg0 + 8, ((load32(arg0 + 8) & -2147483648) | (load32(v4 + 12) & 2147483647)))
                store32(arg0 + 8, (load32(arg0 + 8) | -2147483648))
                store32(arg0 + 4, v3)
                break
            while True:  # $label3
                if (v2 != v5):
                    store8(arg1, load8u(v2))
                    arg1 = (arg1 + 1)
                    v2 = (v2 + 1)
                    continue
                break
            store8(v4 + 7, 0)
            store8(arg1, load8u(v4 + 7))
            G.global0 = (v4 + 16)
            break
        func212()
        raise Unreachable()
        break
    G.global0 = (v6 + 16)
    G.global0 = v7
    return (v4 + 8)

# ----------------------------------------------------------
# $func309
# ----------------------------------------------------------
def func309(arg0, arg1, arg2):
    v5 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v3 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v4 + 12, arg0)
    store32(v4 + 8, (arg0 + arg1))
    store32(v3 + 24, load32(v4 + 12))
    store32(v3 + 28, load32(v4 + 8))
    G.global0 = (v4 + 16)
    v4 = load32(v3 + 24)
    v7 = load32(v3 + 28)
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v6 = (v7 - v4)
    if (v4 != v7):
        # TODO: memory.copy
    store32(arg1 + 12, (v4 + v6))
    store32(arg1 + 8, (arg2 + v6))
    store32(v3 + 16, load32(arg1 + 12))
    store32(v3 + 20, load32(arg1 + 8))
    G.global0 = (arg1 + 16)
    store32(v3 + 12, (arg0 + (load32(v3 + 16) - arg0)))
    store32(v3 + 8, (arg2 + (load32(v3 + 20) - arg2)))
    store32(v5 + 8, load32(v3 + 12))
    store32(v5 + 12, load32(v3 + 8))
    G.global0 = (v3 + 32)
    arg0 = load32(v5 + 12)
    G.global0 = (v5 + 16)
    return arg0

# ----------------------------------------------------------
# $func310
# ----------------------------------------------------------
def func310(arg0, arg1, arg2):
    v5 = (arg2 - arg1)
    v6 = ((arg2 - arg1) >> 2)
    v3 = load32(arg0 + 8)
    v4 = load32(arg0)
    if (u32(((arg2 - arg1) >> 2)) <= u32(((load32(arg0 + 8) - load32(arg0)) >> 2))):
        v5 = (load32(arg0 + 4) - v4)
        v3 = (arg1 + (load32(arg0 + 4) - v4))
        v8 = (v5 >> 2)
        v5 = ((arg1 + (load32(arg0 + 4) - v4)) if (u32(v6) > u32((v5 >> 2))) else arg2)
        v7 = (((arg1 + (load32(arg0 + 4) - v4)) if (u32(v6) > u32((v5 >> 2))) else arg2) - arg1)
        if (arg1 != v5):
            # TODO: memory.copy
        if (u32(v6) > u32(v8)):
            arg1 = load32(arg0 + 4)
            if (arg2 != v5):
                while True:  # $label0
                    store32(arg1, load32(v3))
                    arg1 = (arg1 + 4)
                    v3 = (v3 + 4)
                    if ((v3 + 4) != arg2):
                        continue
                    break
            store32(arg0 + 4, arg1)
            return v7
        store32(arg0 + 4, (v4 + v7))
        return arg1
    if v4:
        store32(arg0 + 4, v4)
        store32(arg0 + 8, 0)
        store64(arg0, 0)
        v3 = 0
    while True:  # $label1
        if (v5 < 0):
            break
        v4 = (v3 >> 1)
        v3 = (1073741823 if (u32(v3) >= u32(2147483644)) else ((v3 >> 1) if (u32(v4) > u32(v6)) else v6))
        if (u32((1073741823 if (u32(v3) >= u32(2147483644)) else ((v3 >> 1) if (u32(v4) > u32(v6)) else v6))) >= u32(1073741824)):
            break
        v4 = (v3 << 2)
        v3 = func26((v3 << 2))
        store32(arg0 + 4, func26((v3 << 2)))
        store32(arg0, v3)
        store32(arg0 + 8, (v3 + v4))
        if (arg1 != arg2):
            arg0 = (((v5 - 4) & -4) + 4)
            # TODO: memory.copy
        else:
        store32((arg0 + v3) + 4, v3)
        return (((v5 - 4) & -4) + 4)
        break
    func42()
    raise Unreachable()
    return arg1

# ----------------------------------------------------------
# $func311
# ----------------------------------------------------------
def func311(arg0, arg1, arg2):
    v6 = (arg2 - arg1)
    v5 = ((arg2 - arg1) // 196)
    v3 = load32(arg0 + 8)
    v4 = load32(arg0)
    if (u32(((arg2 - arg1) // 196)) <= u32(((load32(arg0 + 8) - load32(arg0)) // 196))):
        v6 = ((load32(arg0 + 4) - v4) // 196)
        v3 = (arg1 + (((load32(arg0 + 4) - v4) // 196) * 196))
        v7 = ((arg1 + (((load32(arg0 + 4) - v4) // 196) * 196)) if (u32(v5) > u32(v6)) else arg2)
        v8 = (((arg1 + (((load32(arg0 + 4) - v4) // 196) * 196)) if (u32(v5) > u32(v6)) else arg2) - arg1)
        if (arg1 != v7):
            # TODO: memory.copy
        if (u32(v5) > u32(v6)):
            arg1 = load32(arg0 + 4)
            if (arg2 != v7):
                while True:  # $label0
                    # TODO: memory.copy
                    arg1 = (arg1 + 196)
                    v3 = (v3 + 196)
                    if ((v3 + 196) != arg2):
                        continue
                    break
            store32(arg0 + 4, arg1)
            return 196
        store32(arg0 + 4, (v4 + ((v8 // 196) * 196)))
        return v3
    if v4:
        store32(arg0 + 4, v4)
        store32(arg0 + 8, 0)
        store64(arg0, 0)
        v3 = 0
    while True:  # $label1
        if (u32(v5) >= u32(21913099)):
            break
        v3 = (v3 // 196)
        v4 = ((v3 // 196) << 1)
        v3 = (21913098 if (u32(v3) >= u32(10956549)) else (((v3 // 196) << 1) if (u32(v4) > u32(v5)) else v5))
        if (u32((21913098 if (u32(v3) >= u32(10956549)) else (((v3 // 196) << 1) if (u32(v4) > u32(v5)) else v5))) >= u32(21913099)):
            break
        v4 = (v3 * 196)
        v3 = func26((v3 * 196))
        store32(arg0 + 4, func26((v3 * 196)))
        store32(arg0, v3)
        store32(arg0 + 8, (v3 + v4))
        if (arg1 != arg2):
            arg0 = (v6 - 196)
            arg0 = (((v6 - 196) - (arg0 % 196)) + 196)
            # TODO: memory.copy
        else:
        store32((arg0 + v3) + 4, v3)
        return (((v6 - 196) - (arg0 % 196)) + 196)
        break
    func42()
    raise Unreachable()
    return arg1

# ----------------------------------------------------------
# $func312
# ----------------------------------------------------------
def func312(arg0, arg1):
    if ((load8u(arg0 + 11) & 0xFFFFFFFF) >> 7):
        store32(arg0 + 4, arg1)
        return
    store8(arg0 + 11, ((load8u(arg0 + 11) & 128) | arg1))
    store8(arg0 + 11, (load8u(arg0 + 11) & 127))

# ----------------------------------------------------------
# $func313
# ----------------------------------------------------------
def func313(arg0):
    v2 = func443(8)
    store32(func443(8), 32876)
    store32(v2, 32988)
    v3 = func209(arg0)
    v1 = func26((func209(arg0) + 13))
    store32(func26((func209(arg0) + 13)) + 8, 0)
    store32(v1 + 4, v3)
    store32(v1, v3)
    v1 = (v1 + 12)
    # TODO: memory.copy
    store32(v2 + 4, v1)
    store32(v2, 33036)
    a_i()
    raise Unreachable()

# ----------------------------------------------------------
# $func314
# ----------------------------------------------------------
def func314(arg0, arg1, arg2):
    arg1 = func26(arg2)
    store32(arg0 + 4, arg2)
    store32(arg0, arg1)

# ----------------------------------------------------------
# $func315
# ----------------------------------------------------------
def func315(arg0, arg1, arg2):
    v9 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        v3 = load32(PLAYER_COUNT)
        if ((arg1 != 2147483647) & (u32(load32(PLAYER_COUNT)) <= u32(arg1))):
            break
        v11 = load32(arg0 + 16)
        while True:  # $label1
            while True:  # $label4
                while True:  # $label2
                    while True:  # $label3
                        # br_table load32(arg0 + 4)
                        break
                        break
                    v8 = load32(arg0 + 88)
                    if not load32(arg0 + 88):
                        break
                    v6 = load32(arg0 + 12)
                    if not load32(arg0 + 12):
                        break
                    v5 = ((v11 * 404) + ENTITY_TYPES)
                    arg2 = 0
                    v4 = v6
                    while True:  # $label8
                        while True:  # $label5
                            if not v4:
                                v4 = 0
                                break
                            v3 = 0
                            v7 = (arg2 << 2)
                            if (load8u(entities[load32(((arg2 << 2) + load32(arg0 + 80)))].unit_class) == 3):
                                break
                            while True:  # $label7
                                v4 = entities[load32((load32(arg0 + 80) + v7))]
                                if (load8u(entities[load32((load32(arg0 + 80) + v7))].unit_class) != 3):
                                    while True:  # $label6
                                        if not func59((v9 + 12), (v9 + 8), v4, v5):
                                            break
                                        v4 = func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1)
                                        if not func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1):
                                            break
                                        if (u32(load32(arg0 + 104)) < u32(7)):
                                            break
                                        func148(v4, load32(arg0 + 96), 0)
                                        break
                                    v6 = load32(arg0 + 12)
                                v3 = (v3 + 1)
                                if (u32((v3 + 1)) < u32(v6)):
                                    continue
                                break
                            v8 = load32(arg0 + 88)
                            v4 = v6
                            break
                        arg2 = (arg2 + 1)
                        if (u32((arg2 + 1)) < u32(v8)):
                            continue
                        break
                    break
                    break
                if not v3:
                    break
                v17 = ((v11 * 404) + ENTITY_TYPES)
                arg2 = load32(arg0 + 36)
                if (u32(load32(arg0 + 36)) <= u32(3)):
                    v14 = (arg2 - 1)
                    while True:  # $label23
                        while True:  # $label9
                            arg2 = load32(arg0 + 64)
                            v4 = (v8 << 2)
                            if not load32((load32(arg0 + 64) + (v8 << 2))):
                                if not load32((arg2 + (v3 << 2))):
                                    break
                                if not load32((load32(9142420) + v4)):
                                    break
                            v5 = 0
                            v15 = load32(PLAYERS)
                            while True:  # $label22
                                while True:  # $label14
                                    while True:  # $label13
                                        while True:  # $label10
                                            while True:  # $label11
                                                while True:  # $label12
                                                    # br_table v14
                                                    break
                                                    break
                                                if (load32(((v5 * 404) + ENTITY_TYPES) + 264) == 1):
                                                    break
                                                break
                                                break
                                            if not load32(((v5 * 404) + ENTITY_TYPES) + 264):
                                                break
                                            break
                                            break
                                        arg2 = ((v5 * 404) + ENTITY_TYPES)
                                        if load32(((v5 * 404) + ENTITY_TYPES) + 264):
                                            break
                                        if (load32(arg2 + 268) == 1):
                                            break
                                        if not load32(arg2 + 92):
                                            break
                                        if (load32(38456) == v5):
                                            break
                                        if (load32(38764) == v5):
                                            break
                                        break
                                    v13 = load32((((v15 + (v8 * 286704)) + (v5 << 2)) + 284636))
                                    if not load32((((v15 + (v8 * 286704)) + (v5 << 2)) + 284636)):
                                        break
                                    v10 = 0
                                    v12 = load32(v13 + 8)
                                    if not load32(v13 + 8):
                                        break
                                    while True:  # $label21
                                        while True:  # $label15
                                            arg2 = load32((load32(v13) + (v10 << 2)))
                                            if not load32((load32(v13) + (v10 << 2))):
                                                break
                                            if not load32(arg0 + 12):
                                                break
                                            v6 = 0
                                            v18 = entities[arg2]
                                            while True:  # $label20
                                                while True:  # $label16
                                                    if not func59((v9 + 12), (v9 + 8), v18, v17):
                                                        break
                                                    arg2 = func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1)
                                                    if not func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1):
                                                        break
                                                    if (u32(load32(arg0 + 104)) < u32(7)):
                                                        break
                                                    v3 = entities[arg2]
                                                    v7 = load32(arg0 + 96)
                                                    arg2 = load32(load32(arg0 + 96))
                                                    if (u32(load32(load32(arg0 + 96))) <= u32(2147483646)):
                                                        store32(v3 + 52, arg2)
                                                    arg2 = load32(v7 + 4)
                                                    if (u32(load32(v7 + 4)) <= u32(2147483646)):
                                                        store32(v3 + 60, arg2)
                                                    while True:  # $label17
                                                        arg2 = load32(v7 + 8)
                                                        if (u32(load32(v7 + 8)) > u32(2147483646)):
                                                            break
                                                        store32(v3 + 64, arg2)
                                                        if (u32(load32(v7 + 8)) > u32(2147483646)):
                                                            break
                                                        store32(v3 + 68, load32(v7 + 12))
                                                        break
                                                    v4 = load32(v3 + 76)
                                                    arg2 = load32(v3 + 76)
                                                    while True:  # $label18
                                                        v16 = load32(v7 + 16)
                                                        if (u32(load32(v7 + 16)) > u32(2147483646)):
                                                            break
                                                        store32(v3 + 72, v16)
                                                        if (u32(load32(v7 + 16)) > u32(2147483646)):
                                                            break
                                                        arg2 = load32(v7 + 20)
                                                        store32(v3 + 76, load32(v7 + 20))
                                                        break
                                                    v7 = load32(v7 + 24)
                                                    if (u32(load32(v7 + 24)) <= u32(2147483646)):
                                                        store32(v3 + 84, v7)
                                                    v16 = ((load8u(v3 + 122) * 404) + ENTITY_TYPES)
                                                    v7 = load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 264)
                                                    while True:  # $label19
                                                        if not load32(v16 + 92):
                                                            if (v7 == 2):
                                                                break
                                                            store32(v3 + 52, 0)
                                                        if (v7 != 1):
                                                            break
                                                        arg2 = 0
                                                        store32(v3 + 72, 0)
                                                        store32(v3 + 60, 0)
                                                        store32(v3 + 76, 0)
                                                        store32(v3 + 84, 0)
                                                        break
                                                    if not load32(v3 + 64):
                                                        store32((v3 - -64), -1)
                                                    if not arg2:
                                                        break
                                                    if v4:
                                                        break
                                                    break
                                                v6 = (v6 + 1)
                                                if (u32((v6 + 1)) < u32(load32(arg0 + 12))):
                                                    continue
                                                break
                                            break
                                        v10 = (v10 + 1)
                                        if ((v10 + 1) != v12):
                                            continue
                                        break
                                    break
                                v5 = (v5 + 1)
                                if ((v5 + 1) != 255):
                                    continue
                                break
                            v3 = load32(PLAYER_COUNT)
                            break
                        v8 = (v8 + 1)
                        if (u32((v8 + 1)) < u32(v3)):
                            continue
                        break
                    break
                v13 = ((arg2 - 4) << 2)
                while True:  # $label32
                    while True:  # $label24
                        arg2 = load32(arg0 + 64)
                        v4 = (v8 << 2)
                        if not load32((load32(arg0 + 64) + (v8 << 2))):
                            if not load32((arg2 + (v3 << 2))):
                                break
                            if not load32((load32(9142420) + v4)):
                                break
                        v7 = load32(((players[v8] + v13) + 284636))
                        if not load32(((players[v8] + v13) + 284636)):
                            break
                        v10 = 0
                        v14 = load32(v7 + 8)
                        if not load32(v7 + 8):
                            break
                        while True:  # $label31
                            while True:  # $label25
                                arg2 = load32((load32(v7) + (v10 << 2)))
                                if not load32((load32(v7) + (v10 << 2))):
                                    break
                                if not load32(arg0 + 12):
                                    break
                                v6 = 0
                                v15 = entities[arg2]
                                while True:  # $label30
                                    while True:  # $label26
                                        if not func59((v9 + 12), (v9 + 8), v15, v17):
                                            break
                                        arg2 = func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1)
                                        if not func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1):
                                            break
                                        if (u32(load32(arg0 + 104)) < u32(7)):
                                            break
                                        v3 = entities[arg2]
                                        v5 = load32(arg0 + 96)
                                        arg2 = load32(load32(arg0 + 96))
                                        if (u32(load32(load32(arg0 + 96))) <= u32(2147483646)):
                                            store32(v3 + 52, arg2)
                                        arg2 = load32(v5 + 4)
                                        if (u32(load32(v5 + 4)) <= u32(2147483646)):
                                            store32(v3 + 60, arg2)
                                        while True:  # $label27
                                            arg2 = load32(v5 + 8)
                                            if (u32(load32(v5 + 8)) > u32(2147483646)):
                                                break
                                            store32(v3 + 64, arg2)
                                            if (u32(load32(v5 + 8)) > u32(2147483646)):
                                                break
                                            store32(v3 + 68, load32(v5 + 12))
                                            break
                                        v4 = load32(v3 + 76)
                                        arg2 = load32(v3 + 76)
                                        while True:  # $label28
                                            v12 = load32(v5 + 16)
                                            if (u32(load32(v5 + 16)) > u32(2147483646)):
                                                break
                                            store32(v3 + 72, v12)
                                            if (u32(load32(v5 + 16)) > u32(2147483646)):
                                                break
                                            arg2 = load32(v5 + 20)
                                            store32(v3 + 76, load32(v5 + 20))
                                            break
                                        v5 = load32(v5 + 24)
                                        if (u32(load32(v5 + 24)) <= u32(2147483646)):
                                            store32(v3 + 84, v5)
                                        v12 = ((load8u(v3 + 122) * 404) + ENTITY_TYPES)
                                        v5 = load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 264)
                                        while True:  # $label29
                                            if not load32(v12 + 92):
                                                if (v5 == 2):
                                                    break
                                                store32(v3 + 52, 0)
                                            if (v5 != 1):
                                                break
                                            arg2 = 0
                                            store32(v3 + 72, 0)
                                            store32(v3 + 60, 0)
                                            store32(v3 + 76, 0)
                                            store32(v3 + 84, 0)
                                            break
                                        if not load32(v3 + 64):
                                            store32((v3 - -64), -1)
                                        if not arg2:
                                            break
                                        if v4:
                                            break
                                        break
                                    v6 = (v6 + 1)
                                    if (u32((v6 + 1)) < u32(load32(arg0 + 12))):
                                        continue
                                    break
                                break
                            v10 = (v10 + 1)
                            if ((v10 + 1) != v14):
                                continue
                            break
                        v3 = load32(PLAYER_COUNT)
                        break
                    v8 = (v8 + 1)
                    if (u32((v8 + 1)) < u32(v3)):
                        continue
                    break
                break
                break
            v8 = load32(9140300)
            if not load32(9140300):
                break
            v5 = ((v11 * 404) + ENTITY_TYPES)
            v4 = load32(arg0 + 12)
            while True:  # $label36
                v3 = 0
                while True:  # $label33
                    v7 = entities[load32(((v6 << 2) + 8451904))]
                    v10 = load16u(entities[load32(((v6 << 2) + 8451904))] + 110)
                    if ((((load32((load32(9142420) + (load16u(entities[load32(((v6 << 2) + 8451904))] + 110) << 2))) != 0) & (arg1 == v10)) | arg2) != 1):
                        break
                    if not v4:
                        break
                    while True:  # $label35
                        while True:  # $label34
                            if not func59((v9 + 12), (v9 + 8), v7, v5):
                                break
                            v4 = func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1)
                            if not func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1):
                                break
                            if (u32(load32(arg0 + 104)) < u32(7)):
                                break
                            func148(v4, load32(arg0 + 96), 0)
                            break
                        v3 = (v3 + 1)
                        v4 = load32(arg0 + 12)
                        if (u32((v3 + 1)) < u32(load32(arg0 + 12))):
                            continue
                        break
                    v8 = load32(9140300)
                    break
                v6 = (v6 + 1)
                if (u32((v6 + 1)) < u32(v8)):
                    continue
                break
            break
            break
        if not load32(arg0 + 12):
            break
        v10 = ((v11 * 404) + ENTITY_TYPES)
        arg2 = 0
        while True:  # $label41
            v8 = load32(arg0 + 20)
            v3 = 0
            v5 = load32(arg0 + 28)
            if load32(arg0 + 28):
                v19 = load64(9147316)
                v4 = load32(9147312)
                store32(9147316, load32(9147312))
                v6 = load32(9147324)
                store64(9147320, v19)
                v6 = (v6 ^ (v6 << 11))
                v4 = ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8))) ^ v6)
                store32(9147312, ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8))) ^ v6))
            else:
            v8 = (0 + v8)
            v3 = load32(arg0 + 24)
            while True:  # $label40
                while True:  # $label37
                    v5 = load32(arg0 + 40)
                    if load32(arg0 + 40):
                        v19 = load64(9147316)
                        v4 = load32(9147312)
                        store32(9147316, load32(9147312))
                        v6 = load32(9147324)
                        store64(9147320, v19)
                        v6 = (v6 ^ (v6 << 11))
                        v4 = ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8))) ^ v6)
                        store32(9147312, ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8))) ^ v6))
                    else:
                    v5 = (0 + v3)
                    if func56((v4 % v5), (0 + v3), v10, arg1, 0, 0, 1, 1, 0):
                        v3 = v8
                        v4 = v5
                        break
                    v4 = 0
                    v6 = load32(9142440)
                    while True:  # $label39
                        while True:  # $label38
                            v7 = v4
                            v3 = (v4 << 2)
                            v4 = (load32((((v4 << 2) | 4) + 8611904)) + v5)
                            if (u32(v6) <= u32((load32((((v4 << 2) | 4) + 8611904)) + v5))):
                                break
                            v3 = (load32((v3 + 8611904)) + v8)
                            if (u32(v6) <= u32((load32((v3 + 8611904)) + v8))):
                                break
                            if ((v3 | v4) < 0):
                                break
                            if func56(v3, v4, v10, arg1, 0, 0, 1, 1, 0):
                                break
                            v6 = load32(9142440)
                            break
                        v4 = (v7 + 2)
                        if (u32(v7) < u32(5198)):
                            continue
                        break
                    break
                    break
                v4 = func34(v11, arg1, v3, v4, 0, 1)
                if not func34(v11, arg1, v3, v4, 0, 1):
                    break
                if (u32(load32(arg0 + 104)) < u32(7)):
                    break
                func148(v4, load32(arg0 + 96), 0)
                break
            arg2 = (arg2 + 1)
            if (u32((arg2 + 1)) < u32(load32(arg0 + 12))):
                continue
            break
        break
    G.global0 = (v9 + 16)
    return v8

# ----------------------------------------------------------
# $func317
# ----------------------------------------------------------
def func317(arg0):
    v1 = load32(arg0 + 283960)
    v25 = (load32(arg0 + 283960) if (u32(v1) <= u32(2)) else 0)
    while True:  # $label43
        v2 = load32(9142428)
        if (u32(load32(9142428)) >= u32(48)):
            v4 = 47
            v26 = 1
            v1 = -1
            while True:  # $label42
                v6 = (load32(GAME_STATE) + (v4 << 2))
                v29 = load32((load32(GAME_STATE) + (v4 << 2)) + 16)
                v30 = ((v4 + 7) if load32((load32(GAME_STATE) + (v4 << 2)) + 16) else v4)
                while True:  # $label0
                    if (load32(v6 + 4) != 1):
                        break
                    v17 = load32(v6 + 8)
                    if (load32(v6 + 8) < 0):
                        v17 = load32((((v25 + (v17 ^ -1)) << 2) + 9681488))
                    v12 = load32(v6)
                    v13 = load32(v6 + 12)
                    v40 = 0.0
                    while True:  # $label1
                        if not v3:
                            break
                        if (v3 != v12):
                            break
                        if (v1 != v13):
                            break
                        v40 = (3.14159274 / i32(v3))
                        break
                    if not v12:
                        v3 = 0
                        v1 = v13
                        break
                    v41 = (6.28318548 / i32(v12))
                    v9 = ((v17 * 404) + ENTITY_TYPES)
                    v35 = i32(v13)
                    v23 = 0
                    while True:  # $label41
                        v33 = ((v41 * i32(v23)) + v40)
                        v24 = load32(arg0 + 283908)
                        v1 = load32(arg0 + 283876)
                        v2 = load32(arg0 + 283872)
                        v20 = 0
                        v27 = load32(v9 + 264)
                        if not load32(v9 + 264):
                            while True:  # $label2
                                # TODO: f64.promote_f32
                                v44 = (((v33 * -8.0) / 6.2831854820251465) + 10.5)
                                if (((((v33 * -8.0) / 6.2831854820251465) + 10.5) < 4294967296.0) & (v44 >= 0.0)):
                                    break
                                break
                            v20 = (0 & 7)
                        v28 = load32(v9 + 220)
                        v42 = (i32(load32(v9 + 220)) * -0.5)
                        v34 = (((v35 * func48(v33)) + (i32(load32(v9 + 220)) * -0.5)) + 0.5)
                        v7 = load32(v9 + 216)
                        v43 = (i32(load32(v9 + 216)) * -0.5)
                        v36 = (((v35 * func49(v33)) + (i32(load32(v9 + 216)) * -0.5)) + 0.5)
                        v38 = i32(v1)
                        v39 = i32(v2)
                        while True:  # $label6
                            while True:  # $label9
                                while True:  # $label5
                                    while True:  # $label3
                                        v37 = (v33 + 0.196349546)
                                        v33 = (v33 + 6.28318548)
                                        if ((v33 + 0.196349546) >= (v33 + 6.28318548)):
                                            v8 = load32(9142440)
                                            v14 = (load32(9142440) + 2)
                                            v18 = load32(9142840)
                                            break
                                        if (v7 <= 0):
                                            while True:  # $label4
                                                v33 = (v34 + v38)
                                                if (abs((v34 + v38)) < 2147483650.0):
                                                    break
                                                break
                                            v3 = -2147483648
                                            v33 = (v36 + v39)
                                            if not (abs((v36 + v39)) < 2147483650.0):
                                                break
                                            break
                                        v18 = load32(9142840)
                                        v10 = load32(v9 + 372)
                                        v8 = load32(9142440)
                                        v14 = (load32(9142440) + 2)
                                        v19 = ((load32(9142440) + 2) * load32(v9 + 208))
                                        v15 = load32(v9 + 212)
                                        while True:  # $label21
                                            while True:  # $label7
                                                v34 = (v34 + v38)
                                                if (abs((v34 + v38)) < 2147483650.0):
                                                    break
                                                break
                                            v3 = -2147483648
                                            v11 = (v3 + v28)
                                            v1 = (-2147483648 >= (v3 + v28))
                                            while True:  # $label8
                                                v34 = (v36 + v39)
                                                if (abs((v36 + v39)) < 2147483650.0):
                                                    break
                                                break
                                            v4 = -2147483648
                                            if v1:
                                                break
                                            v21 = (v4 + v7)
                                            v2 = v4
                                            while True:  # $label10
                                                if (v27 == 1):
                                                    while True:  # $label15
                                                        v5 = (v2 + 1)
                                                        v16 = (v2 - v4)
                                                        v1 = v3
                                                        while True:  # $label12
                                                            if (u32(v2) >= u32(v8)):
                                                                while True:  # $label11
                                                                    if load8u((v10 + (((v1 - v3) * v7) + v16))):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if ((v1 + 1) != v11):
                                                                        continue
                                                                    break
                                                                    break
                                                                raise Unreachable()
                                                            while True:  # $label14
                                                                while True:  # $label13
                                                                    if not load8u((v10 + (((v1 - v3) * v7) + v16))):
                                                                        v1 = (v1 + 1)
                                                                        break
                                                                    if (u32(v1) >= u32(v8)):
                                                                        break
                                                                    if ((v1 | v2) < 0):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if (load32((v18 + (((((v1 + 1) + v19) * v14) + v5) << 2))) != v15):
                                                                        break
                                                                    if (load32((v18 + (((v1 * v14) + v5) << 2))) != v15):
                                                                        break
                                                                    break
                                                                if (v1 != v11):
                                                                    continue
                                                                break
                                                            break
                                                        v2 = v5
                                                        if (v5 < v21):
                                                            continue
                                                        break
                                                        break
                                                    raise Unreachable()
                                                while True:  # $label20
                                                    v5 = (v2 + 1)
                                                    v16 = (v2 - v4)
                                                    v1 = v3
                                                    while True:  # $label18
                                                        if (u32(v2) < u32(v8)):
                                                            while True:  # $label17
                                                                while True:  # $label16
                                                                    if not load8u((v10 + (((v1 - v3) * v7) + v16))):
                                                                        v1 = (v1 + 1)
                                                                        break
                                                                    if (u32(v1) >= u32(v8)):
                                                                        break
                                                                    if ((v1 | v2) < 0):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if (load32((v18 + (((((v1 + 1) + v19) * v14) + v5) << 2))) != v15):
                                                                        break
                                                                    break
                                                                if (v1 != v11):
                                                                    continue
                                                                break
                                                                break
                                                            raise Unreachable()
                                                        while True:  # $label19
                                                            if load8u((v10 + (((v1 - v3) * v7) + v16))):
                                                                break
                                                            v1 = (v1 + 1)
                                                            if ((v1 + 1) != v11):
                                                                continue
                                                            break
                                                        break
                                                    v2 = v5
                                                    if (v5 < v21):
                                                        continue
                                                    break
                                                break
                                                break
                                            v34 = (((v35 * func48(v37)) + v42) + 0.5)
                                            v36 = (((v35 * func49(v37)) + v43) + 0.5)
                                            v37 = (v37 + 0.196349546)
                                            if not ((v37 + 0.196349546) >= v33):
                                                continue
                                            break
                                        break
                                    while True:  # $label22
                                        v33 = (v34 + v38)
                                        if (abs((v34 + v38)) < 2147483650.0):
                                            break
                                        break
                                    v31 = -2147483648
                                    while True:  # $label23
                                        v33 = (v36 + v39)
                                        if (abs((v36 + v39)) < 2147483650.0):
                                            break
                                        break
                                    v32 = -2147483648
                                    v1 = 0
                                    while True:  # $label36
                                        while True:  # $label24
                                            v10 = v1
                                            v1 = (v1 << 2)
                                            v3 = (load32((((v1 << 2) | 4) + 8611904)) + v31)
                                            if (u32(v8) <= u32((load32((((v1 << 2) | 4) + 8611904)) + v31))):
                                                break
                                            v5 = (load32((v1 + 8611904)) + v32)
                                            if (u32(v8) <= u32((load32((v1 + 8611904)) + v32))):
                                                break
                                            if ((v3 | v5) < 0):
                                                break
                                            while True:  # $label25
                                                if (v7 <= 0):
                                                    break
                                                v11 = (v3 + v28)
                                                if ((v3 + v28) <= v3):
                                                    break
                                                v21 = (v5 + v7)
                                                v15 = load32(v9 + 372)
                                                v16 = (load32(v9 + 208) * v14)
                                                v19 = load32(v9 + 212)
                                                v4 = v5
                                                v2 = v5
                                                if (v27 == 1):
                                                    while True:  # $label30
                                                        v2 = (v4 + 1)
                                                        v22 = (v4 - v5)
                                                        v1 = v3
                                                        while True:  # $label27
                                                            if (u32(v4) >= u32(v8)):
                                                                while True:  # $label26
                                                                    if load8u((v15 + (((v1 - v3) * v7) + v22))):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if ((v1 + 1) != v11):
                                                                        continue
                                                                    break
                                                                    break
                                                                raise Unreachable()
                                                            while True:  # $label29
                                                                while True:  # $label28
                                                                    if not load8u((v15 + (((v1 - v3) * v7) + v22))):
                                                                        v1 = (v1 + 1)
                                                                        break
                                                                    if (u32(v1) >= u32(v8)):
                                                                        break
                                                                    if ((v1 | v4) < 0):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if (load32((v18 + (((((v1 + 1) + v16) * v14) + v2) << 2))) != v19):
                                                                        break
                                                                    if (load32((v18 + (((v1 * v14) + v2) << 2))) != v19):
                                                                        break
                                                                    break
                                                                if (v1 != v11):
                                                                    continue
                                                                break
                                                            break
                                                        v4 = v2
                                                        if (v2 < v21):
                                                            continue
                                                        break
                                                        break
                                                    raise Unreachable()
                                                while True:  # $label35
                                                    v4 = (v2 + 1)
                                                    v22 = (v2 - v5)
                                                    v1 = v3
                                                    while True:  # $label33
                                                        if (u32(v2) < u32(v8)):
                                                            while True:  # $label32
                                                                while True:  # $label31
                                                                    if not load8u((v15 + (((v1 - v3) * v7) + v22))):
                                                                        v1 = (v1 + 1)
                                                                        break
                                                                    if (u32(v1) >= u32(v8)):
                                                                        break
                                                                    if ((v1 | v2) < 0):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if (load32((v18 + (((((v1 + 1) + v16) * v14) + v4) << 2))) != v19):
                                                                        break
                                                                    break
                                                                if (v1 != v11):
                                                                    continue
                                                                break
                                                                break
                                                            raise Unreachable()
                                                        while True:  # $label34
                                                            if load8u((v15 + (((v1 - v3) * v7) + v22))):
                                                                break
                                                            v1 = (v1 + 1)
                                                            if ((v1 + 1) != v11):
                                                                continue
                                                            break
                                                        break
                                                    v2 = v4
                                                    if (v4 < v21):
                                                        continue
                                                    break
                                                break
                                            break
                                            break
                                        v1 = (v10 + 2)
                                        if (u32(v10) < u32(13118)):
                                            continue
                                        break
                                    break
                                    break
                                v4 = -2147483648
                                break
                            break
                        v1 = func34(v17, v24, v4, v3, v20, 1)
                        if v26:
                            store32(arg0 + 284624, v1)
                        if (load32(v9 + 268) == 1):
                            store32(entities[v1].attack, 1)
                        while True:  # $label37
                            if not v29:
                                break
                            if not v1:
                                break
                            v1 = entities[v1]
                            v2 = load32(v6 + 20)
                            if (u32(load32(v6 + 20)) <= u32(2147483646)):
                                store32(v1 + 52, v2)
                            v2 = load32(v6 + 24)
                            if (u32(load32(v6 + 24)) <= u32(2147483646)):
                                store32(v1 + 60, v2)
                            while True:  # $label38
                                v2 = load32(v6 + 28)
                                if (u32(load32(v6 + 28)) > u32(2147483646)):
                                    break
                                store32(v1 + 64, v2)
                                if (u32(load32(v6 + 28)) > u32(2147483646)):
                                    break
                                store32(v1 + 68, load32(v6 + 32))
                                break
                            v4 = load32(v1 + 76)
                            while True:  # $label39
                                v2 = load32(v6 + 36)
                                if (u32(load32(v6 + 36)) > u32(2147483646)):
                                    break
                                store32(v1 + 72, v2)
                                if (u32(load32(v6 + 36)) > u32(2147483646)):
                                    break
                                store32(v1 + 76, load32(v6 + 40))
                                break
                            v2 = load32(v6 + 44)
                            if (u32(load32(v6 + 44)) <= u32(2147483646)):
                                store32(v1 + 84, v2)
                            v3 = ((load8u(v1 + 122) * 404) + ENTITY_TYPES)
                            v2 = load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 264)
                            while True:  # $label40
                                if not load32(v3 + 92):
                                    if (v2 == 2):
                                        break
                                    store32(v1 + 52, 0)
                                if (v2 != 1):
                                    break
                                store32(v1 + 84, 0)
                                store32(v1 + 72, 0)
                                store32(v1 + 60, 0)
                                break
                            v2 = load32(v1 + 64)
                            if load32(v1 + 64):
                            else:
                                store32((v1 - -64), -1)
                            store32(v2 + 68, -1)
                            v2 = load32(v1 + 72)
                            store32(v1 + 76, load32(v1 + 72))
                            if not v2:
                                break
                            if v4:
                                break
                            break
                        v26 = 0
                        v23 = (v23 + 1)
                        if ((v23 + 1) != v12):
                            continue
                        break
                    v2 = load32(9142428)
                    v1 = v13
                    v3 = v12
                    break
                v4 = (v30 + 5)
                if (u32((v30 + 5)) < u32(v2)):
                    continue
                break
            if (v1 != -1):
                break
        while True:  # $label48
            v12 = load32(arg0 + 283908)
            v33 = 0.0
            v10 = load32(((v25 << 2) + 9681488))
            v2 = ((load32(((v25 << 2) + 9681488)) * 404) + ENTITY_TYPES)
            v6 = (0 if load32(((load32(((v25 << 2) + 9681488)) * 404) + ENTITY_TYPES) + 264) else 2)
            v34 = (i32(load32(v2 + 220)) * -0.5)
            v36 = (i32(load32(v2 + 216)) * -0.5)
            v37 = i32(load32(arg0 + 283876))
            v38 = i32(load32(arg0 + 283872))
            while True:  # $label46
                while True:  # $label47
                    v35 = (v33 + 0.196349546)
                    while True:  # $label44
                        v39 = ((((func48(v33) * 0.0) + v34) + 0.5) + v37)
                        if (abs(((((func48(v33) * 0.0) + v34) + 0.5) + v37)) < 2147483650.0):
                            break
                        break
                    v4 = -2147483648
                    arg0 = (v35 >= 6.28318548)
                    while True:  # $label45
                        v33 = ((((func49(v33) * 0.0) + v36) + 0.5) + v38)
                        if (abs(((((func49(v33) * 0.0) + v36) + 0.5) + v38)) < 2147483650.0):
                            break
                        break
                    v3 = -2147483648
                    if arg0:
                        break
                    v33 = v35
                    if not func73(v3, v4, v2, 0, 0, 1):
                        continue
                    break
                break
                break
            v13 = load32(9142440)
            arg0 = 0
            while True:  # $label50
                while True:  # $label51
                    while True:  # $label49
                        v1 = arg0
                        v5 = (arg0 << 2)
                        arg0 = (load32((((arg0 << 2) | 4) + 8611904)) + v4)
                        if (u32(v13) <= u32((load32((((arg0 << 2) | 4) + 8611904)) + v4))):
                            break
                        v5 = (load32((v5 + 8611904)) + v3)
                        if (u32(v13) <= u32((load32((v5 + 8611904)) + v3))):
                            break
                        if ((arg0 | v5) < 0):
                            break
                        if func73(v5, arg0, v2, 0, 0, 1):
                            break
                        v13 = load32(9142440)
                        break
                    arg0 = (v1 + 2)
                    if (u32(v1) < u32(13118)):
                        continue
                    break
                break
                break
            break
        store32(0 + 284624, func34(v10, v12, v5, arg0, v6, 1))
        break
    return func34(v10, v12, v3, v4, v6, 1)

# ----------------------------------------------------------
# $func318
# ----------------------------------------------------------
def func318(arg0, arg1, arg2):
    arg0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label1
        while True:  # $label0
            v3 = load8u(9147152)
            if not load8u(9147152):
                v4 = load32(arg1)
                break
            v4 = load32(9142440)
            v5 = load32(arg1)
            if (load32(9142440) == load32(arg1)):
                break
            store32(arg0, v5)
            v3 = load8u(9147152)
            break
            break
        store32(9142440, v4)
        break
    while True:  # $label2
        if not v3:
            break
        v3 = load32(arg1 + 24)
        v4 = load32(GAME_STATE)
        if (load32(arg1 + 24) == load32(load32(GAME_STATE) + 24)):
            break
        store32(v4 + 24, v3)
        Gb(arg2)
        break
    store32(GAME_STATE, 0)
    v4 = (arg2 << 2)
    v3 = func26((-1 if (u32(arg2) > u32(1073741823)) else (arg2 << 2)))
    store32(9142428, arg2)
    store32(GAME_STATE, v3)
    if arg2:
        # TODO: memory.copy
    G.global0 = (arg0 + 16)

# ----------------------------------------------------------
# $func319
# ----------------------------------------------------------
def func319():
    v4 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    func402(load32(9142440))
    v1 = load32(9142440)
    if load32(9142440):
        v5 = load32(9147288)
        while True:  # $label2
            v3 = (v0 + 1)
            v2 = 0
            v6 = load32(9142840)
            v7 = load32(9140332)
            while True:  # $label1
                while True:  # $label0
                    v8 = load8s((v5 + ((v1 * v2) + v0)))
                    if (load8s((v5 + ((v1 * v2) + v0))) < 0):
                        break
                    if (load32(load32((v7 + ((v8 & 255) << 2))) + 32) != 23):
                        break
                    v8 = (v2 + 1)
                    store32((v6 + ((((v2 + 1) * (v1 + 2)) + v3) << 2)), 1)
                    v1 = (load32(9142440) + 2)
                    store32((v6 + (((((load32(9142440) + 2) + v8) * v1) + v3) << 2)), 1)
                    v1 = load32(9142440)
                    break
                v2 = (v2 + 1)
                if (u32((v2 + 1)) < u32(v1)):
                    continue
                break
            v0 = v3
            if (u32(v3) < u32(v1)):
                continue
            break
    v1 = 3
    if (u32(load32(9671136)) > u32(3)):
        v6 = 0
        while True:  # $label9
            while True:  # $label3
                v0 = entities[v1]
                v3 = load32(entities[v1].max_hp)
                if not load32(entities[v1].max_hp):
                    break
                v2 = load16u(v0 + 110)
                if (u32(load16u(v0 + 110)) >= u32(load32(PLAYER_COUNT))):
                    break
                v5 = load8u(v0 + 122)
                v7 = (load8u(v0 + 122) != load32(38448))
                if not (load8u(v0 + 122) != load32(38448)):
                    store32(v0 + 48, load32(((v5 * 72) + 9263856)))
                v2 = players[v2]
                while True:  # $label5
                    while True:  # $label4
                        if not load8u(9216060):
                            if not load32(v0 + 64):
                                break
                        if (load8u(v0 + 125) != 3):
                            break
                        break
                    store8(v0 + 125, 3)
                    if not v7:
                        v3 = load32(v0 + 28)
                    store32(v0 + 92, 0)
                    func388(v2, v3)
                    break
                    break
                if func292(v0):
                    store32(v0 + 92, 0)
                v3 = ((v5 * 404) + ENTITY_TYPES)
                store32(v0 + 92, 0)
                while True:  # $label6
                    if load32(v0 + 36):
                        func138(v0)
                        break
                    v5 = load8u(v0 + 125)
                    break
                while True:  # $label7
                    if (u32(load32(9684508)) > u32(551)):
                        break
                    if (u32(load32(v0 + 84)) < u32(12)):
                        break
                    if load32(((load8u(v0 + 122) * 404) + ENTITY_TYPES) + 264):
                        break
                    store32(v2 + 283936, (load32(v2 + 283936) + 1))
                    break
                while True:  # $label8
                    if (load32(v0 + 32) != -1):
                        break
                    if load8u(9147152):
                        break
                    store32(v0 + 32, 0)
                    v6 = (v6 + 25)
                    func240(v0, (((v6 + 25) % 1000) + 25), 0)
                    break
                    break
                if (load32(v3 + 264) == 4):
                    store8(9671157, 1)
                if (load32(v3 + 208) == 2):
                    store8(9671158, 1)
                func144(v2, load32(v0 + 28), 0)
                break
            v1 = (v1 + 1)
            if (u32((v1 + 1)) < u32(load32(9671136))):
                continue
            break
    if load8u(9561801):
        store32(v4 + 16, load32(9142840))
        v0 = (load32(9142440) + 2)
        store32(v4 + 20, (((load32(9142440) + 2) * v0) * 3))
    while True:  # $label10
        if load32(9147132):
            break
        if not load32(load32(GAME_STATE) + 48):
            break
        if load8u(9147152):
            break
        v3 = load32(9671136)
        if (u32(load32(9671136)) < u32(4)):
            break
        v0 = load32(ENTITIES)
        v1 = 3
        while True:  # $label12
            while True:  # $label11
                v2 = (v0 + (v1 * 132))
                if (load8u((v0 + (v1 * 132)) + 125) == 3):
                    break
                if not load32(v2 + 28):
                    break
                if load32(v2 + 36):
                    break
                v3 = load32(9671136)
                v0 = load32(ENTITIES)
                break
            v1 = (v1 + 1)
            if (u32((v1 + 1)) < u32(v3)):
                continue
            break
        break
    while True:  # $label13
        if not load8u(9147152):
            break
        if not load32(load32(GAME_STATE) + 48):
            break
        store32(v4, 0)
        store32(v4 + 4, load32(9142440))
        a_b()
        break
    G.global0 = (v4 + 32)

# ----------------------------------------------------------
# $func320
# ----------------------------------------------------------
def func320(arg0):
    v3 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    if not load8u(9142917):
        if not arg0:
            while True:  # $label9
                while True:  # $label5
                    while True:  # $label4
                        while True:  # $label2
                            if not load8u(9142916):
                                while True:  # $label1
                                    while True:  # $label0
                                        arg0 = load32(9299880)
                                        if load32(9299880):
                                            arg0 = (arg0 - 1)
                                            store32(9299880, (arg0 - 1))
                                            arg0 = load32((load32(9299872) + (arg0 << 2)))
                                            break
                                        arg0 = load32(9163776)
                                        v1 = (load32(9163776) + 1)
                                        store32(9163776, (load32(9163776) + 1))
                                        v2 = load32(9163784)
                                        if (u32(v1) >= u32(load32(9163784))):
                                            break
                                        break
                                    store32(9142888, arg0)
                                    break
                                    break
                                store32(v3 + 64, v2)
                                a_b()
                                store32(9142888, arg0)
                                store32(9163784, (load32(9163784) + 40000))
                                if not load8u(9142916):
                                    break
                            while True:  # $label3
                                arg0 = load32(9299896)
                                if load32(9299896):
                                    arg0 = (arg0 - 1)
                                    store32(9299896, (arg0 - 1))
                                    arg0 = load32((load32(9299888) + (arg0 << 2)))
                                    break
                                arg0 = load32(9163780)
                                v1 = (load32(9163780) + 1)
                                store32(9163780, (load32(9163780) + 1))
                                v2 = load32(9163788)
                                if (u32(v1) < u32(load32(9163788))):
                                    break
                                store32(v3 + 48, v2)
                                a_b()
                                store32(9163788, (load32(9163788) + 40000))
                                break
                            arg0 = (arg0 + 1073741823)
                            break
                            break
                        if load8u(9142917):
                            store32(9142884, 0)
                            break
                        arg0 = load32(9299880)
                        if load32(9299880):
                            arg0 = (arg0 - 1)
                            store32(9299880, (arg0 - 1))
                            arg0 = load32((load32(9299872) + (arg0 << 2)))
                            break
                        arg0 = load32(9163776)
                        v1 = (load32(9163776) + 1)
                        store32(9163776, (load32(9163776) + 1))
                        v2 = load32(9163784)
                        if (u32(v1) < u32(load32(9163784))):
                            break
                        store32(v3 + 32, v2)
                        a_b()
                        store32(9163784, (load32(9163784) + 40000))
                        break
                    store32(9142884, arg0)
                    if load8u(9142917):
                        break
                    while True:  # $label8
                        while True:  # $label7
                            while True:  # $label6
                                arg0 = load32(9299880)
                                if load32(9299880):
                                    arg0 = (arg0 - 1)
                                    store32(9299880, (arg0 - 1))
                                    v1 = load32((load32(9299872) + (arg0 << 2)))
                                    break
                                arg0 = 0
                                v1 = load32(9163776)
                                v2 = (load32(9163776) + 1)
                                store32(9163776, (load32(9163776) + 1))
                                v4 = load32(9163784)
                                if (u32(v2) >= u32(load32(9163784))):
                                    break
                                break
                            store32(9142876, v1)
                            break
                            break
                        store32(v3 + 16, v4)
                        a_b()
                        store32(9142876, v1)
                        store32(9163784, (load32(9163784) + 40000))
                        if load8u(9142917):
                            break
                        break
                    arg0 = load32(9299880)
                    if load32(9299880):
                        arg0 = (arg0 - 1)
                        store32(9299880, (arg0 - 1))
                        arg0 = load32((load32(9299872) + (arg0 << 2)))
                        break
                    arg0 = load32(9163776)
                    v1 = (load32(9163776) + 1)
                    store32(9163776, (load32(9163776) + 1))
                    v2 = load32(9163784)
                    if (u32(v1) < u32(load32(9163784))):
                        break
                    store32(v3, v2)
                    a_b()
                    store32(9163784, (load32(9163784) + 40000))
                    break
                    break
                arg0 = 0
                store32(9142876, 0)
                break
            store32(9142880, arg0)
        while True:  # $label13
            while True:  # $label14
                while True:  # $label11
                    while True:  # $label10
                        arg0 = load32(9142640)
                        if not load32(9142640):
                            break
                        if not load32(arg0 + 20):
                            break
                        v1 = load8u(9142916)
                        if (load32(arg0 + 28) != 2147483647):
                            break
                        while True:  # $label12
                            if v1:
                                v2 = load32(59152)
                                store32(59152, (load32(59152) + 1))
                                v4 = load32(9568052)
                                v5 = load32(arg0)
                                break
                            v5 = load32(arg0)
                            v4 = load32(9568052)
                            v2 = ((load32(arg0) + load32(9140308)) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                            break
                        store32(arg0 + 28, v2)
                        v2 = load32(arg0 + 4)
                        v6 = load32(9568048)
                        store32(9568048, (load32(9568048) + 1))
                        store32(((v6 << 2) + 9563952), arg0)
                        store32(9568052, (((v5 * (v2 + 2)) << 2) + v4))
                        if not v1:
                            break
                        v1 = load32(9568056)
                        store32(arg0 + 56, load32(9568056))
                        store32(9568056, (v1 + ((v2 * load32(arg0)) << 2)))
                        break
                    if load8u(9142916):
                        break
                    break
                    break
                if v1:
                    break
                break
            break
    G.global0 = (v3 + 80)

# ----------------------------------------------------------
# $func321
# ----------------------------------------------------------
def func321(arg0, arg1, arg2):
    if (arg2 >= 0):
        v11 = load16u(arg1 + 2)
        v8 = (4 if load16u(arg1 + 2) else 3)
        v5 = (7 if v11 else 138)
        v9 = (arg0 + 5817)
        v6 = -1
        while True:  # $label12
            v10 = v11
            v14 = v13
            v13 = (v13 + 1)
            v11 = load16u((arg1 + ((v13 + 1) << 2)) + 2)
            while True:  # $label1
                while True:  # $label0
                    v3 = (v4 + 1)
                    if ((v4 + 1) >= v5):
                        break
                    if (v10 != v11):
                        break
                    v4 = v3
                    break
                    break
                while True:  # $label4
                    if (v3 < v8):
                        v4 = (arg0 + (v10 << 2))
                        v5 = ((arg0 + (v10 << 2)) + 2686)
                        v7 = (v4 + 2684)
                        v4 = load32(arg0 + 5820)
                        while True:  # $label3
                            v12 = load16u(v5)
                            v8 = load16u(v7)
                            v6 = (load16u(arg0 + 5816) | (load16u(v7) << v4))
                            store16(arg0 + 5816, (load16u(arg0 + 5816) | (load16u(v7) << v4)))
                            while True:  # $label2
                                if ((16 - v12) < v4):
                                    v4 = load32(arg0 + 20)
                                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                    store8((v4 + load32(arg0 + 8)), v6)
                                    v4 = load32(arg0 + 20)
                                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                    store8((v4 + load32(arg0 + 8)), load8u(v9))
                                    v4 = load32(arg0 + 5820)
                                    store16(arg0 + 5816, ((v8 & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                                    break
                                break
                            v4 = (v4 + v12)
                            store32(((v4 + v12) - 16) + 5820, (v4 + v12))
                            v3 = (v3 - 1)
                            if (v3 - 1):
                                continue
                            break
                        break
                    while True:  # $label8
                        if v10:
                            while True:  # $label5
                                if (v6 == v10):
                                    v5 = load32(arg0 + 5820)
                                    v4 = v3
                                    break
                                v3 = (arg0 + (v10 << 2))
                                v7 = load16u(((arg0 + (v10 << 2)) + 2686))
                                v8 = load16u((v3 + 2684))
                                v3 = load32(arg0 + 5820)
                                v6 = (load16u(arg0 + 5816) | (load16u((v3 + 2684)) << load32(arg0 + 5820)))
                                store16(arg0 + 5816, (load16u(arg0 + 5816) | (load16u((v3 + 2684)) << load32(arg0 + 5820))))
                                while True:  # $label6
                                    if ((16 - v7) < v3):
                                        v3 = load32(arg0 + 20)
                                        store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                        store8((v3 + load32(arg0 + 8)), v6)
                                        v3 = load32(arg0 + 20)
                                        store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                        store8((v3 + load32(arg0 + 8)), load8u(v9))
                                        v3 = load32(arg0 + 5820)
                                        store16(arg0 + 5816, ((v8 & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                                        break
                                    break
                                v5 = (v3 + v7)
                                store32(((v3 + v7) - 16) + 5820, (v3 + v7))
                                break
                            v8 = load16u(arg0 + 2748)
                            v3 = (load16u(arg0 + 5816) | (load16u(arg0 + 2748) << v5))
                            while True:  # $label7
                                v7 = load16u(arg0 + 2750)
                                if ((16 - load16u(arg0 + 2750)) < v5):
                                    store16(arg0 + 5816, v3)
                                    v6 = load32(arg0 + 20)
                                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                    store8((v6 + load32(arg0 + 8)), v3)
                                    v3 = load32(arg0 + 20)
                                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                    store8((v3 + load32(arg0 + 8)), load8u(v9))
                                    v3 = load32(arg0 + 5820)
                                    v5 = ((v7 + load32(arg0 + 5820)) - 16)
                                    v3 = ((v8 & 0xFFFFFFFF) >> (16 - v3))
                                    break
                                v5 = (v5 + v7)
                                break
                            store32(arg0 + 5820, v5)
                            v6 = (v4 + 65533)
                            if (v5 >= 15):
                                v3 = (v3 | (v6 << v5))
                                store16(arg0 + 5816, (v3 | (v6 << v5)))
                                v4 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v4 + load32(arg0 + 8)), v3)
                                v4 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v4 + load32(arg0 + 8)), load8u(v9))
                                v4 = load32(arg0 + 5820)
                                store16(arg0 + 5816, (((v6 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                                break
                            store16(arg0 + 5816, (v3 | (v6 << v5)))
                            break
                        v3 = load16u(arg0 + 5816)
                        v6 = load32(arg0 + 5820)
                        if (v4 <= 9):
                            v8 = load16u(arg0 + 2752)
                            v3 = (v3 | (load16u(arg0 + 2752) << v6))
                            while True:  # $label9
                                v7 = load16u(arg0 + 2754)
                                if ((16 - load16u(arg0 + 2754)) < v6):
                                    store16(arg0 + 5816, v3)
                                    v6 = load32(arg0 + 20)
                                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                    store8((v6 + load32(arg0 + 8)), v3)
                                    v3 = load32(arg0 + 20)
                                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                    store8((v3 + load32(arg0 + 8)), load8u(v9))
                                    v3 = load32(arg0 + 5820)
                                    v5 = ((v7 + load32(arg0 + 5820)) - 16)
                                    v3 = ((v8 & 0xFFFFFFFF) >> (16 - v3))
                                    break
                                v5 = (v6 + v7)
                                break
                            store32(arg0 + 5820, v5)
                            v6 = (v4 + 65534)
                            if (v5 >= 14):
                                v3 = (v3 | (v6 << v5))
                                store16(arg0 + 5816, (v3 | (v6 << v5)))
                                v4 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v4 + load32(arg0 + 8)), v3)
                                v4 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v4 + load32(arg0 + 8)), load8u(v9))
                                v4 = load32(arg0 + 5820)
                                store16(arg0 + 5816, (((v6 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                                break
                            store16(arg0 + 5816, (v3 | (v6 << v5)))
                            break
                        v8 = load16u(arg0 + 2756)
                        v3 = (v3 | (load16u(arg0 + 2756) << v6))
                        while True:  # $label10
                            v7 = load16u(arg0 + 2758)
                            if ((16 - load16u(arg0 + 2758)) < v6):
                                store16(arg0 + 5816, v3)
                                v6 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v6 + load32(arg0 + 8)), v3)
                                v3 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v3 + load32(arg0 + 8)), load8u(v9))
                                v3 = load32(arg0 + 5820)
                                v5 = ((v7 + load32(arg0 + 5820)) - 16)
                                v3 = ((v8 & 0xFFFFFFFF) >> (16 - v3))
                                break
                            v5 = (v6 + v7)
                            break
                        store32(arg0 + 5820, v5)
                        v6 = (v4 + 65526)
                        if (v5 >= 10):
                            v3 = (v3 | (v6 << v5))
                            store16(arg0 + 5816, (v3 | (v6 << v5)))
                            v4 = load32(arg0 + 20)
                            store32(arg0 + 20, (load32(arg0 + 20) + 1))
                            store8((v4 + load32(arg0 + 8)), v3)
                            v4 = load32(arg0 + 20)
                            store32(arg0 + 20, (load32(arg0 + 20) + 1))
                            store8((v4 + load32(arg0 + 8)), load8u(v9))
                            v4 = load32(arg0 + 5820)
                            store16(arg0 + 5816, (((v6 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                            break
                        store16(arg0 + 5816, (v3 | (v6 << v5)))
                        break
                    store32((v4 - 9) + 5820, (v5 + 7))
                    break
                v4 = 0
                while True:  # $label11
                    if not v11:
                        v5 = 138
                        break
                    v3 = (v10 == v11)
                    v5 = (6 if (v10 == v11) else 7)
                    break
                v8 = (3 if v3 else 4)
                v6 = v10
                break
            if (arg2 != v14):
                continue
            break
    return 3

# ----------------------------------------------------------
# $func322
# ----------------------------------------------------------
def func322(arg0, arg1, arg2):
    v6 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v7 = load32(PLAYERS)
    while True:  # $label2
        while True:  # $label1
            while True:  # $label0
                if load32(9147132):
                    if (load32(9142440) == 4096):
                        break
                v3 = load32(arg2)
                break
                break
            v3 = load32(arg2)
            if (u32((load32(arg2) + load32(((v7 + (arg1 * 286704)) + 281724)))) < u32(1000001)):
                break
            if (load32(CURRENT_PLAYER) != arg1):
                break
            store64(v6, 4294967296000930)
            a_b()
            break
            break
        if (v3 < 0):
            break
        v4 = load32(arg2 + 4)
        if (load32(arg2 + 4) < 0):
            break
        v5 = load32(arg2 + 8)
        if (load32(arg2 + 8) < 0):
            break
        v8 = load32(arg2 + 12)
        if (load32(arg2 + 12) < 0):
            break
        while True:  # $label3
            if v3:
                break
            if v4:
                break
            if v5:
                break
            if not v8:
                break
            break
        if load8u((load32(9143004) + ((load32(PLAYER_COUNT) * arg1) + arg0))):
            break
        v11 = (v7 + (arg1 * 286704))
        if func66((v7 + (arg1 * 286704)), arg2, 1, 0):
            break
        v4 = (v7 + (arg1 * 286704))
        v3 = ((v7 + (arg1 * 286704)) + 281724)
        store32(((v7 + (arg1 * 286704)) + 281724), (load32(v3) + load32(arg2)))
        v3 = (v7 + (arg0 * 286704))
        v5 = ((v7 + (arg0 * 286704)) + 281708)
        store32(((v7 + (arg0 * 286704)) + 281708), (load32(v5) + load32(arg2)))
        v5 = (v4 + 281728)
        store32((v4 + 281728), (load32(v5) + load32(arg2 + 4)))
        v5 = (v3 + 281712)
        store32((v3 + 281712), (load32(v5) + load32(arg2 + 4)))
        v5 = (v4 + 281732)
        store32((v4 + 281732), (load32(v5) + load32(arg2 + 8)))
        v5 = (v3 + 281716)
        store32((v3 + 281716), (load32(v5) + load32(arg2 + 8)))
        v4 = (v4 + 281736)
        store32((v4 + 281736), (load32(v4) + load32(arg2 + 12)))
        v4 = (v3 + 281720)
        store32((v3 + 281720), (load32(v4) + load32(arg2 + 12)))
        v4 = load32(v3 + 283848)
        if (load32(v3 + 283848) != 2147483647):
            store32((v3 + 283848), (load32(arg2) + v4))
        v3 = (v3 + 283852)
        v4 = load32((v3 + 283852))
        if (load32((v3 + 283852)) != 2147483647):
            store32(v3, (load32(arg2 + 4) + v4))
        v3 = (v7 + (arg0 * 286704))
        v4 = ((v7 + (arg0 * 286704)) + 283856)
        v5 = load32(((v7 + (arg0 * 286704)) + 283856))
        if (load32(((v7 + (arg0 * 286704)) + 283856)) != 2147483647):
            store32(v4, (load32(arg2 + 8) + v5))
        v3 = (v3 + 283860)
        v4 = load32((v3 + 283860))
        if (load32((v3 + 283860)) != 2147483647):
            store32(v3, (load32(arg2 + 12) + v4))
        v3 = 1
        v5 = (v7 + (arg0 * 286704))
        store8((v7 + (arg0 * 286704)) + 286701, 1)
        while True:  # $label4
            v4 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            v9 = (v4 - 1)
            v12 = ((v4 - 1) & 1)
            v5 = (load32(v5 + 283908) * v4)
            v8 = load32(PLAYERS)
            v10 = load32(9143016)
            if (v4 != 2):
                v9 = (v9 & -2)
                v4 = 0
                while True:  # $label5
                    if load8u((v10 + (v3 + v5))):
                        store8((v8 + (v3 * 286704)) + 286701, 1)
                    v13 = (v3 + 1)
                    if load8u((v10 + ((v3 + 1) + v5))):
                        store8((v8 + (v13 * 286704)) + 286701, 1)
                    v3 = (v3 + 2)
                    v4 = (v4 + 2)
                    if ((v4 + 2) != v9):
                        continue
                    break
            if not v12:
                break
            if not load8u((v10 + (v3 + v5))):
                break
            store8((v8 + (v3 * 286704)) + 286701, 1)
            break
        if (load32(CURRENT_PLAYER) != arg0):
            break
        v14 = load64(arg2)
        v15 = load64(arg2 + 8)
        store32(v6 + 36, load32((v7 + (arg1 * 286704)) + 284616))
        store32(v6 + 32, v11)
        store64(v6 + 24, v15)
        store64(v6 + 16, v14)
        a_b()
        break
    G.global0 = (v6 + 48)

# ----------------------------------------------------------
# $func323
# ----------------------------------------------------------
def func323(arg0, arg1):
    while True:  # $label0
        v2 = load32(arg0 + 20)
        if not load32(arg0 + 20):
            break
        if (u32(load32(v2 + 8)) < u32(2)):
            break
        v2 = load32(v2)
        if (load32(load32(v2)) != 2):
            break
        break
    v10 = load32(v2 + 4)
    v2 = load16u(arg0 + 110)
    v4 = load32(PLAYERS)
    v3 = load32(arg0 + 88)
    v11 = ((load32(arg0 + 88) & 0xFFFFFFFF) >> 16)
    v5 = load16u(arg0 + 108)
    v14 = load32(arg0 + 28)
    v7 = load32(ENTITIES)
    while True:  # $label5
        while True:  # $label3
            while True:  # $label4
                while True:  # $label2
                    while True:  # $label1
                        v6 = (v3 & 65535)
                        # br_table (v3 & 65535)
                        break
                        break
                    break
                    break
                break
                break
            break
            break
        if (load32(38528) == v11):
            break
        if (load32(((v11 * 404) + ENTITY_TYPES) + 268) == 3):
            break
        if (load32(38712) == load8u(arg0 + 122)):
            break
        break
    v3 = ((v4 + (v2 * 286704)) + 281648)
    store32(((v4 + (v2 * 286704)) + 281648), (load32(v3) + v5))
    while True:  # $label6
        v8 = (v4 + (v2 * 286704))
        v3 = (((v4 + (v2 * 286704)) + (v6 << 2)) + 283848)
        v6 = load32((((v4 + (v2 * 286704)) + (v6 << 2)) + 283848))
        if (load32((((v4 + (v2 * 286704)) + (v6 << 2)) + 283848)) == 2147483647):
            break
        store32(v3, (v5 + v6))
        v3 = 1
        store8(v8 + 286701, 1)
        v5 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v9 = (v5 - 1)
        v12 = ((v5 - 1) & 1)
        v4 = (load32((v4 + (v2 * 286704)) + 283908) * v5)
        v6 = load32(PLAYERS)
        v8 = load32(9143016)
        if (v5 != 2):
            v5 = (v9 & -2)
            v2 = 0
            while True:  # $label7
                if load8u((v8 + (v3 + v4))):
                    store8((v6 + (v3 * 286704)) + 286701, 1)
                v9 = (v3 + 1)
                if load8u((v8 + ((v3 + 1) + v4))):
                    store8((v6 + (v9 * 286704)) + 286701, 1)
                v3 = (v3 + 2)
                v2 = (v2 + 2)
                if ((v2 + 2) != v5):
                    continue
                break
        if not v12:
            break
        if not load8u((v8 + (v3 + v4))):
            break
        store8((v6 + (v3 * 286704)) + 286701, 1)
        break
    store16(arg0 + 108, 0)
    if not arg1:
        store8(arg0 + 125, 0)
        while True:  # $label8
            if not load32(arg0 + 92):
                break
            if load32(9140316):
                if (load32(9140320) != load32(arg0 + 28)):
                    break
            break
        arg1 = ((v11 * 404) + ENTITY_TYPES)
        if (load32(((v11 * 404) + ENTITY_TYPES) + 268) == 3):
            v6 = load32(9142440)
            v12 = (load32(9142440) + 2)
            v15 = ((load32(9142440) + 2) * load32(arg1 + 208))
            v8 = load16u(arg0 + 112)
            v16 = (load16u(arg0 + 112) + 29)
            v9 = load16u(arg0 + 114)
            v17 = (load16u(arg0 + 114) + 29)
            v10 = (v9 - 30)
            v2 = (v8 - 30)
            v18 = load32(ENTITIES)
            v19 = load32(9142840)
            v5 = 2147483647
            v7 = 0
            while True:  # $label11
                v4 = (v2 + 1)
                if (u32(v2) < u32(v6)):
                    arg1 = (v8 - v2)
                    v20 = ((v8 - v2) * arg1)
                    arg1 = v10
                    while True:  # $label10
                        while True:  # $label9
                            v3 = arg1
                            if (u32(v6) <= u32(arg1)):
                                break
                            if ((v2 | v3) < 0):
                                break
                            arg1 = (v9 - v3)
                            v13 = (((v9 - v3) * arg1) + v20)
                            if ((((v9 - v3) * arg1) + v20) >= v5):
                                break
                            arg1 = load32((v19 + (((((v3 + v15) + 1) * v12) + v4) << 2)))
                            if not load32((v19 + (((((v3 + v15) + 1) * v12) + v4) << 2))):
                                break
                            v13 = (v11 == load8u((v18 + (arg1 * 132)) + 122))
                            v5 = (v13 if (v11 == load8u((v18 + (arg1 * 132)) + 122)) else v5)
                            v7 = (arg1 if v13 else v7)
                            break
                        arg1 = (v3 + 1)
                        if (v3 != v17):
                            continue
                        break
                arg1 = (v2 != v16)
                v2 = v4
                if arg1:
                    continue
                break
            if v7:
                return func28(1, 1)
            func404(v14)
            return ((v4 + (v2 * 286704)) + 281664)
        while True:  # $label12
            if (v11 == load32(38528)):
                break
            v2 = (v7 + (v10 * 132))
            arg1 = load32((v7 + (v10 * 132)) + 28)
            if not load32((v7 + (v10 * 132)) + 28):
                break
            while True:  # $label13
                if (load8u(v2 + 125) == 10):
                    break
                if (u32(load32(((load8u((v7 + (v10 * 132)) + 122) * 404) + ENTITY_TYPES) + 188)) < u32(4)):
                    break
                func29(arg0, 1)
                return ((v4 + (v2 * 286704)) + 281644)
                break
            if load8u(9142916):
            else:
            return arg0
            break
        func404(v14)
    return ((v4 + (v2 * 286704)) + 281640)

# ----------------------------------------------------------
# $func324
# ----------------------------------------------------------
def func324():
    v9 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    store32(9143000, 0)
    v1 = load32(59144)
    v2 = load32(59136)
    v0 = load32(59140)
    v4 = load32(59132)
    v6 = load32(9213820)
    if load32(9213820):
        func47(entities[v6])
        store32(9213820, 0)
    if not load8u(9163792):
        func45()
    if not load8u(9147152):
        func52((207 if load8u(9143020) else 0), 0)
        a_b()
    while True:  # $label21
        while True:  # $label24
            while True:  # $label1
                while True:  # $label0
                    if (u32(((v4 - v2) if (u32(v2) < u32(v4)) else (v2 - v4))) > u32(12)):
                        break
                    if (u32(((v0 - v1) if (u32(v0) > u32(v1)) else (v1 - v0))) > u32(12)):
                        break
                    v2 = func141(v4, v0)
                    if not ((a_f() - loadf64(9681904)) < 500.0):
                        break
                    if (u32(v2) < u32(3)):
                        break
                    v1 = (load32(9681912) - v4)
                    v1 = (load32(9681916) - v0)
                    if (((((load32(9681912) - v4) * v1) + ((load32(9681916) - v0) * v1)) - 1) > 100):
                        break
                    v6 = load32(ENTITIES)
                    v1 = entities[v2]
                    if not load8u(9147152):
                        if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v1 + 110))))):
                            break
                        v5 = (v6 + (v2 * 132))
                        if (load32((load32(9215884) + (load32((v6 + (v2 * 132)) + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v5 + 127) == 6):
                            break
                        if load8u(9163793):
                        else:
                        v15 = -1
                        v2 = (v6 + (v2 * 132))
                        v1 = load8u((v6 + (v2 * 132)) + 125)
                        v10 = load8u(v2 + 122)
                        if not load8u(9163792):
                            func45()
                        while True:  # $label2
                            v20 = loadf32(40616)
                            v21 = i32(load32(9142860))
                            v22 = loadf32(9671164)
                            v23 = ((loadf32(40616) * i32(load32(9142860))) / loadf32(9671164))
                            v24 = ceil(((((loadf32(40616) * i32(load32(9142860))) / loadf32(9671164)) + 32.0) * 0.03125))
                            if (abs(ceil(((((loadf32(40616) * i32(load32(9142860))) / loadf32(9671164)) + 32.0) * 0.03125))) < 2147483650.0):
                                break
                            break
                        v0 = -2147483648
                        while True:  # $label3
                            v21 = ((((v21 - v23) * 0.5) + i32(load32(9142956))) * 0.03125)
                            if (abs(((((v21 - v23) * 0.5) + i32(load32(9142956))) * 0.03125)) < 2147483650.0):
                                break
                            break
                        v2 = -2147483648
                        while True:  # $label4
                            v20 = i32(load32(9142856))
                            v21 = ((v20 * i32(load32(9142856))) / v22)
                            v22 = ceil(((((v20 * i32(load32(9142856))) / v22) + 32.0) * 0.03125))
                            if (abs(ceil(((((v20 * i32(load32(9142856))) / v22) + 32.0) * 0.03125))) < 2147483650.0):
                                break
                            break
                        v6 = -2147483648
                        while True:  # $label5
                            v20 = ((((v20 - v21) * 0.5) + i32(load32(9142952))) * 0.03125)
                            if (abs(((((v20 - v21) * 0.5) + i32(load32(9142952))) * 0.03125)) < 2147483650.0):
                                break
                            break
                        v4 = -2147483648
                        while True:  # $label6
                            if (v6 <= 0):
                                break
                            if (v0 <= 0):
                                break
                            v13 = ((v1 == 4) | (v1 == 14))
                            v16 = (v0 + v2)
                            v17 = (v4 + v6)
                            v18 = ((v10 * 404) + 9568360)
                            v3 = load32(9142440)
                            while True:  # $label20
                                v6 = (v4 + 1)
                                v0 = v2
                                while True:  # $label19
                                    while True:  # $label9
                                        while True:  # $label8
                                            while True:  # $label7
                                                if ((v0 | v4) < 0):
                                                    break
                                                if (u32(v3) <= u32(v4)):
                                                    break
                                                if (u32(v0) < u32(v3)):
                                                    break
                                                break
                                            break
                                            break
                                        v1 = 0
                                        v14 = (v0 + 1)
                                        v19 = (v4 if (u32(v0) < u32(v4)) else v0)
                                        if (u32((v4 if (u32(v0) < u32(v4)) else v0)) >= u32(v3)):
                                            break
                                        while True:  # $label18
                                            while True:  # $label10
                                                if (u32(v3) <= u32(v19)):
                                                    break
                                                v5 = (v3 + 2)
                                                v5 = load32((load32(9142840) + ((v6 + ((v14 + ((v3 + 2) * v1)) * v5)) << 2)))
                                                if (u32(load32((load32(9142840) + ((v6 + ((v14 + ((v3 + 2) * v1)) * v5)) << 2)))) < u32(3)):
                                                    break
                                                while True:  # $label12
                                                    while True:  # $label11
                                                        v7 = load32(load32(GAME_STATE) + 48)
                                                        v8 = load8u(9147152)
                                                        if not (0 if load8u(9147152) else load32(load32(GAME_STATE) + 48)):
                                                            v5 = entities[v5]
                                                            if not v8:
                                                                break
                                                            break
                                                        v8 = load16u((load32(9147376) + (((v0 * v3) + v4) << 1)))
                                                        while True:  # $label13
                                                            if (v7 != 2):
                                                                if v8:
                                                                    break
                                                                break
                                                            if (u32(v8) < u32(2)):
                                                                break
                                                            break
                                                        break
                                                    v5 = entities[v5]
                                                    if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v5 + 110))))):
                                                        break
                                                    if (load32((load32(9215884) + (load32(v5 + 44) << 4)) + 4) == 20):
                                                        break
                                                    if (load8u(v5 + 127) == 6):
                                                        break
                                                    break
                                                while True:  # $label14
                                                    v7 = load8u(v5 + 125)
                                                    v8 = ((load8u(v5 + 125) == 4) | (v7 == 14))
                                                    if not (v13 & ((load8u(v5 + 125) == 4) | (v7 == 14))):
                                                        if (v8 | v13):
                                                            break
                                                        if (v7 != 5):
                                                            break
                                                        break
                                                    if (v7 == 5):
                                                        break
                                                    break
                                                v8 = load8u(v5 + 122)
                                                v11 = load8u(9163793)
                                                while True:  # $label16
                                                    while True:  # $label15
                                                        v12 = load8u(9163794)
                                                        if load8u(9163794):
                                                            break
                                                        if v11:
                                                            break
                                                        if (v8 == v10):
                                                            break
                                                        break
                                                    while True:  # $label17
                                                        if not v12:
                                                            break
                                                        v12 = ((v8 * 404) + ENTITY_TYPES)
                                                        if load32(((v8 * 404) + ENTITY_TYPES) + 264):
                                                            break
                                                        if (load32(v12 + 268) == 1):
                                                            break
                                                        if not load32(v12 + 92):
                                                            break
                                                        if (load32(38456) == v8):
                                                            break
                                                        if (load32(38764) == v8):
                                                            break
                                                        if (v7 != 8):
                                                            break
                                                        break
                                                    if not v11:
                                                        break
                                                    if (func287(v5) != v15):
                                                        break
                                                    if (v8 != v10):
                                                        break
                                                    if (load32(v18) == 1):
                                                        break
                                                    break
                                                func44(v5, 0)
                                                v3 = load32(9142440)
                                                break
                                            v1 = (v1 + 1)
                                            if ((v1 + 1) != 3):
                                                continue
                                            break
                                        break
                                    v0 = v14
                                    if ((v0 + 1) > v14):
                                        continue
                                    break
                                v4 = v6
                                if (v6 < v17):
                                    continue
                                break
                            break
                        break
                    v4 = load16u(v1 + 110)
                    v6 = load8u(v1 + 126)
                    v2 = (G.global0 - 16)
                    G.global0 = (G.global0 - 16)
                    while True:  # $label23
                        while True:  # $label22
                            v0 = load32(v1 + 24)
                            if not load32(v1 + 24):
                                break
                            v0 = load32(v0 + 8)
                            if not load32(v0 + 8):
                                break
                            v5 = load32(v0 + 8)
                            if not load32(v0 + 8):
                                break
                            store32(v2 + 4, load32(v0))
                            store32(v2, v5)
                            a_b()
                            break
                            break
                        a_b()
                        break
                    G.global0 = (v2 + 16)
                    v2 = load32(v1 + 52)
                    v25 = load64(v1 + 64)
                    v0 = load32(v1 + 60)
                    v26 = load64(v1 + 72)
                    v5 = load32(v1 + 84)
                    v8 = load8u(v1 + 122)
                    v3 = load32(v1 + 28)
                    store32(v9 + 36, (2147483647 if (v6 == 2) else v4))
                    store32(v9 + 32, v3)
                    store32(v9 + 28, v8)
                    store32(v9 + 24, v5)
                    store64(v9 + 16, v26)
                    store32(v9 + 4, v0)
                    store64(v9 + 8, v25)
                    store32(v9, v2)
                    func44(v1, 0)
                    break
                    break
                v2 = (v2 // 32)
                v4 = (v4 // 32)
                v6 = ((v2 // 32) if (v2 < v4) else (v4 // 32))
                v5 = (((v2 // 32) if (v2 < v4) else (v4 // 32)) if (v6 > 0) else 0)
                v2 = (v2 if (v2 > v4) else v4)
                v4 = load32(9142440)
                v6 = (load32(9142440) - 1)
                v13 = ((v2 if (v2 > v4) else v4) if (u32(v2) < u32(v4)) else (load32(9142440) - 1))
                if ((((v2 // 32) if (v2 < v4) else (v4 // 32)) if (v6 > 0) else 0) > ((v2 if (v2 > v4) else v4) if (u32(v2) < u32(v4)) else (load32(9142440) - 1))):
                    break
                v1 = (v1 // 32)
                v2 = (v0 // 32)
                v0 = ((v1 // 32) if (v1 < v2) else (v0 // 32))
                v8 = (((v1 // 32) if (v1 < v2) else (v0 // 32)) if (v0 > 0) else 0)
                v1 = (v1 if (v1 > v2) else v2)
                v1 = ((v1 if (v1 > v2) else v2) if (u32(v1) < u32(v4)) else v6)
                if ((((v1 // 32) if (v1 < v2) else (v0 // 32)) if (v0 > 0) else 0) > ((v1 if (v1 > v2) else v2) if (u32(v1) < u32(v4)) else v6)):
                    break
                v14 = (v1 + 1)
                v4 = 0
                while True:  # $label34
                    v2 = v5
                    while True:  # $label33
                        v6 = (v2 + 1)
                        v1 = v8
                        while True:  # $label32
                            while True:  # $label25
                                v3 = load32(9142440)
                                v0 = v1
                                if not ((u32(load32(9142440)) > u32(v1)) & (u32(v2) < u32(v3))):
                                    v1 = (v0 + 1)
                                    break
                                v1 = (v0 + 1)
                                v7 = (v3 + 2)
                                v7 = load32((load32(9142840) + ((v6 + (((v0 + 1) + ((v3 + 2) * v4)) * v7)) << 2)))
                                if (u32(load32((load32(9142840) + ((v6 + (((v0 + 1) + ((v3 + 2) * v4)) * v7)) << 2)))) < u32(3)):
                                    break
                                v10 = load8u(9147152)
                                while True:  # $label29
                                    while True:  # $label28
                                        while True:  # $label26
                                            v11 = load32(load32(GAME_STATE) + 48)
                                            if not load32(load32(GAME_STATE) + 48):
                                                break
                                            if v10:
                                                break
                                            v0 = load16u((load32(9147376) + (((v0 * v3) + v2) << 1)))
                                            while True:  # $label27
                                                if (v11 == 2):
                                                    if (u32(v0) > u32(1)):
                                                        break
                                                    break
                                                if not v0:
                                                    break
                                                break
                                            v3 = entities[v7]
                                            break
                                            break
                                        v3 = entities[v7]
                                        if v10:
                                            break
                                        break
                                    if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v3 + 110))))):
                                        break
                                    if (load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) == 20):
                                        break
                                    if (load8u(v3 + 127) == 6):
                                        break
                                    if (load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 264) == 1):
                                        break
                                    break
                                if load32(v3 + 92):
                                    break
                                v7 = load32(9213808)
                                if (u32(load32(9213808)) > u32(9999)):
                                    break
                                if (load8u(v3 + 125) == 3):
                                    break
                                v0 = 1
                                v10 = load32(v3 + 28)
                                store32(9213808, (v7 + 1))
                                store32(((v7 << 2) + 9173808), v10)
                                while True:  # $label30
                                    if (load8u(9142906) | load8u(9142916)):
                                        break
                                    v0 = 0
                                    if load8u(9142917):
                                        break
                                    v0 = load32(9299880)
                                    if load32(9299880):
                                        v0 = (v0 - 1)
                                        store32(9299880, (v0 - 1))
                                        v0 = load32((load32(9299872) + (v0 << 2)))
                                        break
                                    v0 = load32(9163776)
                                    v7 = (load32(9163776) + 1)
                                    store32(9163776, (load32(9163776) + 1))
                                    v10 = load32(9163784)
                                    if (u32(v7) < u32(load32(9163784))):
                                        break
                                    store32(v9 + 64, v10)
                                    a_b()
                                    store32(9163784, (load32(9163784) + 40000))
                                    break
                                store32(v3 + 92, v0)
                                if not load32(v3 + 36):
                                if (load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 264) != 1):
                                    break
                                if load32(v3 + 80):
                                    break
                                v7 = load16u(v3 + 116)
                                if not load16u(v3 + 116):
                                    break
                                v10 = load16u(v3 + 118)
                                if not load16u(v3 + 118):
                                    break
                                if not load8u(9147152):
                                    if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v3 + 110))))):
                                        break
                                    if (load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) == 20):
                                        break
                                    if (load8u(v3 + 127) == 6):
                                        break
                                v0 = 0
                                while True:  # $label31
                                    if load8u(9142917):
                                        break
                                    v0 = load32(9299880)
                                    if load32(9299880):
                                        v0 = (v0 - 1)
                                        store32(9299880, (v0 - 1))
                                        v0 = load32((load32(9299872) + (v0 << 2)))
                                        break
                                    v0 = load32(9163776)
                                    v11 = (load32(9163776) + 1)
                                    store32(9163776, (load32(9163776) + 1))
                                    v12 = load32(9163784)
                                    if (u32(v11) < u32(load32(9163784))):
                                        break
                                    store32(v9 + 48, v12)
                                    a_b()
                                    store32(9163784, (load32(9163784) + 40000))
                                    v10 = load16u(v3 + 118)
                                    v7 = load16u(v3 + 116)
                                    break
                                store32(v3 + 80, v0)
                                break
                            if (v1 != v14):
                                continue
                            break
                        v1 = (v2 != v13)
                        v2 = v6
                        if v1:
                            continue
                        break
                    v4 = (v4 + 1)
                    if ((v4 + 1) != 3):
                        continue
                    break
                break
                break
            v27 = a_f()
            store32(9681912, v4)
            storef64(9681904, v27)
            store32(9681916, v0)
            if (u32(v2) < u32(3)):
                break
            v0 = load32(ENTITIES)
            v1 = entities[v2]
            while True:  # $label35
                if not load8u(9147152):
                    if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v1 + 110))))):
                        break
                    v4 = (v0 + (v2 * 132))
                    if (load32((load32(9215884) + (load32((v0 + (v2 * 132)) + 44) << 4)) + 4) == 20):
                        break
                    if (load8u(v4 + 127) == 6):
                        break
                while True:  # $label36
                    if not load32(v1 + 92):
                        break
                    if not load8u(9163792):
                        break
                    func77(v1)
                    break
                    break
                func44(v1, 0)
                break
                break
            v2 = (v0 + (v2 * 132))
            if (load8u(9163792) | load8u((v0 + (v2 * 132)) + 128)):
                break
            store32(9213820, load32(v2 + 28))
            func44(v1, 1)
            break
        break
    G.global0 = (v9 + 80)
    return func28(0, 0)

# ----------------------------------------------------------
# $func325
# ----------------------------------------------------------
def func325(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47(entities[arg0])
        store32(9213820, 0)
    func45()
    v10 = players[load32(CURRENT_PLAYER)]
    while True:  # $label12
        while True:  # $label1
            while True:  # $label0
                if (v4 == load32(38440)):
                    break
                if (v4 == load32(38772)):
                    break
                if (v4 != load32(38928)):
                    break
                break
            v7 = load32(((v10 + (v4 << 2)) + 284636))
            if not load32(((v10 + (v4 << 2)) + 284636)):
                break
            v8 = 0
            v9 = load32(v7 + 8)
            if not load32(v7 + 8):
                break
            while True:  # $label11
                while True:  # $label2
                    arg0 = load32((load32(v7) + (v8 << 2)))
                    if not load32((load32(v7) + (v8 << 2))):
                        break
                    v5 = load32(ENTITIES)
                    v1 = entities[arg0]
                    if not load8u(9147152):
                        if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v1 + 110))))):
                            break
                        if (load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v1 + 127) == 6):
                            break
                    v6 = load32(v1 + 28)
                    while True:  # $label3
                        arg0 = load32(9215928)
                        if not load32(9215928):
                            break
                        v2 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        v3 = load32(arg0)
                        arg0 = 0
                        while True:  # $label4
                            if (load32((v5 + (load32((v3 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v2):
                                continue
                            break
                        break
                    while True:  # $label5
                        arg0 = load32(9215932)
                        if not load32(9215932):
                            break
                        v2 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        v3 = load32(arg0)
                        arg0 = 0
                        while True:  # $label6
                            if (load32((v5 + (load32((v3 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v2):
                                continue
                            break
                        break
                    while True:  # $label7
                        arg0 = load32(9215936)
                        if not load32(9215936):
                            break
                        v2 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        v3 = load32(arg0)
                        arg0 = 0
                        while True:  # $label8
                            if (load32((v5 + (load32((v3 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v2):
                                continue
                            break
                        break
                    while True:  # $label9
                        arg0 = load32(9215940)
                        if not load32(9215940):
                            break
                        v2 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        v3 = load32(arg0)
                        arg0 = 0
                        while True:  # $label10
                            if (load32((v5 + (load32((v3 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v2):
                                continue
                            break
                        break
                    if load32(v1 + 36):
                        break
                    if (load8u(v1 + 125) == 8):
                        break
                    func44(v1, 0)
                    v9 = load32(v7 + 8)
                    break
                v8 = (v8 + 1)
                if (u32((v8 + 1)) < u32(v9)):
                    continue
                break
            break
        v4 = (v4 + 1)
        if ((v4 + 1) != 255):
            continue
        break

# ----------------------------------------------------------
# $func326
# ----------------------------------------------------------
def func326(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47(entities[arg0])
        store32(9213820, 0)
    func45()
    v5 = players[load32(CURRENT_PLAYER)]
    while True:  # $label3
        while True:  # $label0
            arg0 = ((v1 * 404) + ENTITY_TYPES)
            if load32(((v1 * 404) + ENTITY_TYPES) + 264):
                break
            if (load32(arg0 + 268) == 1):
                break
            if not load32(arg0 + 92):
                break
            if (load32(arg0 + 224) > 1):
                break
            v2 = load32(((v5 + (v1 << 2)) + 284636))
            if not load32(((v5 + (v1 << 2)) + 284636)):
                break
            v3 = 0
            v4 = load32(v2 + 8)
            if not load32(v2 + 8):
                break
            while True:  # $label2
                while True:  # $label1
                    arg0 = load32((load32(v2) + (v3 << 2)))
                    if not load32((load32(v2) + (v3 << 2))):
                        break
                    arg0 = entities[arg0]
                    if not load8u(9147152):
                        if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(arg0 + 110))))):
                            break
                        if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(arg0 + 127) == 6):
                            break
                    if not func159(arg0):
                        break
                    if load32(arg0 + 36):
                        break
                    if (load8u(arg0 + 125) == 8):
                        break
                    if (load8u(arg0 + 123) == 63):
                        break
                    func44(arg0, 0)
                    v4 = load32(v2 + 8)
                    break
                v3 = (v3 + 1)
                if (u32((v3 + 1)) < u32(v4)):
                    continue
                break
            break
        v1 = (v1 + 1)
        if ((v1 + 1) != 255):
            continue
        break

# ----------------------------------------------------------
# $func327
# ----------------------------------------------------------
def func327(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47(entities[arg0])
        store32(9213820, 0)
    func45()
    v10 = players[load32(CURRENT_PLAYER)]
    while True:  # $label11
        while True:  # $label0
            if (load32(38456) != v4):
                if (v4 != load32(38764)):
                    break
            v7 = load32(((v10 + (v4 << 2)) + 284636))
            if not load32(((v10 + (v4 << 2)) + 284636)):
                break
            v8 = 0
            v9 = load32(v7 + 8)
            if not load32(v7 + 8):
                break
            while True:  # $label10
                while True:  # $label1
                    arg0 = load32((load32(v7) + (v8 << 2)))
                    if not load32((load32(v7) + (v8 << 2))):
                        break
                    v5 = load32(ENTITIES)
                    v3 = entities[arg0]
                    if not load8u(9147152):
                        if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v3 + 110))))):
                            break
                        if (load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v3 + 127) == 6):
                            break
                    v6 = load32(v3 + 28)
                    while True:  # $label2
                        arg0 = load32(9215928)
                        if not load32(9215928):
                            break
                        v1 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        v2 = load32(arg0)
                        arg0 = 0
                        while True:  # $label3
                            if (load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v1):
                                continue
                            break
                        break
                    while True:  # $label4
                        arg0 = load32(9215932)
                        if not load32(9215932):
                            break
                        v1 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        v2 = load32(arg0)
                        arg0 = 0
                        while True:  # $label5
                            if (load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v1):
                                continue
                            break
                        break
                    while True:  # $label6
                        arg0 = load32(9215936)
                        if not load32(9215936):
                            break
                        v1 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        v2 = load32(arg0)
                        arg0 = 0
                        while True:  # $label7
                            if (load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v1):
                                continue
                            break
                        break
                    while True:  # $label8
                        arg0 = load32(9215940)
                        if not load32(9215940):
                            break
                        v1 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        v2 = load32(arg0)
                        arg0 = 0
                        while True:  # $label9
                            if (load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v1):
                                continue
                            break
                        break
                    if load32(v3 + 36):
                        break
                    func44(v3, 0)
                    v9 = load32(v7 + 8)
                    break
                v8 = (v8 + 1)
                if (u32((v8 + 1)) < u32(v9)):
                    continue
                break
            break
        v4 = (v4 + 1)
        if ((v4 + 1) != 255):
            continue
        break

# ----------------------------------------------------------
# $func328
# ----------------------------------------------------------
def func328(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47(entities[arg0])
        store32(9213820, 0)
    func45()
    v5 = players[load32(CURRENT_PLAYER)]
    arg0 = 0
    while True:  # $label4
        while True:  # $label0
            v1 = ((arg0 * 404) + ENTITY_TYPES)
            if load32(((arg0 * 404) + ENTITY_TYPES) + 264):
                break
            if (load32(v1 + 268) == 1):
                break
            if not load32(v1 + 92):
                break
            while True:  # $label1
                if (load32(38452) == arg0):
                    break
                if (load32(38496) == arg0):
                    break
                if (load32(38756) == arg0):
                    break
                if (load32(38692) == arg0):
                    break
                if (load32(38696) == arg0):
                    break
                if (load32(38776) == arg0):
                    break
                if (load32(38752) == arg0):
                    break
                if (load32(38704) != arg0):
                    break
                break
            v2 = load32(((v5 + (arg0 << 2)) + 284636))
            if not load32(((v5 + (arg0 << 2)) + 284636)):
                break
            v3 = 0
            v4 = load32(v2 + 8)
            if not load32(v2 + 8):
                break
            while True:  # $label3
                while True:  # $label2
                    v1 = load32((load32(v2) + (v3 << 2)))
                    if not load32((load32(v2) + (v3 << 2))):
                        break
                    v1 = entities[v1]
                    if not load8u(9147152):
                        if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v1 + 110))))):
                            break
                        if (load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v1 + 127) == 6):
                            break
                    if not func159(v1):
                        break
                    if load32(v1 + 36):
                        break
                    if (load8u(v1 + 125) == 8):
                        break
                    if (load8u(v1 + 123) == 63):
                        break
                    func44(v1, 0)
                    v4 = load32(v2 + 8)
                    break
                v3 = (v3 + 1)
                if (u32((v3 + 1)) < u32(v4)):
                    continue
                break
            break
        arg0 = (arg0 + 1)
        if ((arg0 + 1) != 255):
            continue
        break

# ----------------------------------------------------------
# $func329
# ----------------------------------------------------------
def func329(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47(entities[arg0])
        store32(9213820, 0)
    func45()
    v10 = players[load32(CURRENT_PLAYER)]
    while True:  # $label13
        arg0 = 0
        while True:  # $label0
            v1 = ((v3 * 404) + ENTITY_TYPES)
            if load32(((v3 * 404) + ENTITY_TYPES) + 264):
                break
            if (load32(v1 + 268) == 1):
                break
            arg0 = (load32(v1 + 92) != 0)
            break
        while True:  # $label1
            if not arg0:
                break
            if (v3 == load32(38456)):
                break
            if (v3 == load32(38764)):
                break
            if (v3 == load32(38428)):
                break
            v7 = load32(((v10 + (v3 << 2)) + 284636))
            if not load32(((v10 + (v3 << 2)) + 284636)):
                break
            v8 = 0
            v9 = load32(v7 + 8)
            if not load32(v7 + 8):
                break
            while True:  # $label12
                while True:  # $label2
                    arg0 = load32((load32(v7) + (v8 << 2)))
                    if not load32((load32(v7) + (v8 << 2))):
                        break
                    v2 = load32(ENTITIES)
                    v1 = entities[arg0]
                    if not load8u(9147152):
                        if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v1 + 110))))):
                            break
                        if (load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v1 + 127) == 6):
                            break
                    v6 = load32(v1 + 28)
                    while True:  # $label3
                        arg0 = load32(9215928)
                        if not load32(9215928):
                            break
                        v4 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        v5 = load32(arg0)
                        arg0 = 0
                        while True:  # $label4
                            if (load32((v2 + (load32((v5 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v4):
                                continue
                            break
                        break
                    while True:  # $label5
                        arg0 = load32(9215932)
                        if not load32(9215932):
                            break
                        v4 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        v5 = load32(arg0)
                        arg0 = 0
                        while True:  # $label6
                            if (load32((v2 + (load32((v5 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v4):
                                continue
                            break
                        break
                    while True:  # $label7
                        arg0 = load32(9215936)
                        if not load32(9215936):
                            break
                        v4 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        v5 = load32(arg0)
                        arg0 = 0
                        while True:  # $label8
                            if (load32((v2 + (load32((v5 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v4):
                                continue
                            break
                        break
                    while True:  # $label9
                        arg0 = load32(9215940)
                        if not load32(9215940):
                            break
                        v4 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        v5 = load32(arg0)
                        arg0 = 0
                        while True:  # $label10
                            if (load32((v2 + (load32((v5 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v4):
                                continue
                            break
                        break
                    if load32(v1 + 36):
                        break
                    while True:  # $label11
                        if (load8u(v1 + 125) == 8):
                            v2 = load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4)
                            if (load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 43):
                                break
                            arg0 = load8u(v1 + 123)
                            if (load8u(v1 + 123) == 43):
                                break
                            if (v2 == 15):
                                break
                            if (arg0 == 15):
                                break
                            if (v2 == 28):
                                break
                            if (arg0 == 28):
                                break
                            if (v2 == 27):
                                break
                            if (arg0 == 27):
                                break
                            if (arg0 != 63):
                                break
                            break
                        if (load8u(v1 + 123) == 63):
                            break
                        break
                    func44(v1, 0)
                    v9 = load32(v7 + 8)
                    break
                v8 = (v8 + 1)
                if (u32((v8 + 1)) < u32(v9)):
                    continue
                break
            break
        v3 = (v3 + 1)
        if ((v3 + 1) != 255):
            continue
        break

# ----------------------------------------------------------
# $func330
# ----------------------------------------------------------
def func330(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47(entities[arg0])
        store32(9213820, 0)
    func45()
    while True:  # $label0
        v1 = load32(((players[load32(CURRENT_PLAYER)] + (load32(38528) << 2)) + 284636))
        if not load32(((players[load32(CURRENT_PLAYER)] + (load32(38528) << 2)) + 284636)):
            break
        v3 = load32(v1 + 8)
        if not load32(v1 + 8):
            break
        while True:  # $label2
            while True:  # $label1
                arg0 = load32((load32(v1) + (v2 << 2)))
                if not load32((load32(v1) + (v2 << 2))):
                    break
                arg0 = entities[arg0]
                v4 = 1
                if load8u(9147152):
                else:
                    if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(arg0 + 110))))):
                        break
                    if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                        break
                if not (load8u(arg0 + 127) != 6):
                    break
                if (u32(load32(arg0 + 80)) < u32(450)):
                    break
                if not func159(arg0):
                    break
                if load32(arg0 + 36):
                    break
                func44(arg0, 0)
                v3 = load32(v1 + 8)
                break
            v2 = (v2 + 1)
            if (u32((v2 + 1)) < u32(v3)):
                continue
            break
        break
    return func28(0, 0)

# ----------------------------------------------------------
# $func331
# ----------------------------------------------------------
def func331(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47(entities[arg0])
        store32(9213820, 0)
    func45()
    v5 = players[load32(CURRENT_PLAYER)]
    while True:  # $label3
        while True:  # $label0
            arg0 = ((v1 * 404) + ENTITY_TYPES)
            if load32(((v1 * 404) + ENTITY_TYPES) + 264):
                break
            v2 = load32(arg0 + 268)
            if (load32(arg0 + 268) == 1):
                break
            if not load32(arg0 + 92):
                break
            if (load32(arg0 + 224) < 2):
                break
            if (v1 == load32(38456)):
                break
            if (v1 == load32(38764)):
                break
            if (v1 == load32(38932)):
                break
            if (v2 == 2):
                break
            v2 = load32(((v5 + (v1 << 2)) + 284636))
            if not load32(((v5 + (v1 << 2)) + 284636)):
                break
            v3 = 0
            v4 = load32(v2 + 8)
            if not load32(v2 + 8):
                break
            while True:  # $label2
                while True:  # $label1
                    arg0 = load32((load32(v2) + (v3 << 2)))
                    if not load32((load32(v2) + (v3 << 2))):
                        break
                    arg0 = entities[arg0]
                    if not load8u(9147152):
                        if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(arg0 + 110))))):
                            break
                        if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(arg0 + 127) == 6):
                            break
                    if not func159(arg0):
                        break
                    if load32(arg0 + 36):
                        break
                    if (load8u(arg0 + 125) == 8):
                        break
                    if (load8u(arg0 + 123) == 63):
                        break
                    func44(arg0, 0)
                    v4 = load32(v2 + 8)
                    break
                v3 = (v3 + 1)
                if (u32((v3 + 1)) < u32(v4)):
                    continue
                break
            break
        v1 = (v1 + 1)
        if ((v1 + 1) != 255):
            continue
        break

# ----------------------------------------------------------
# $func332
# ----------------------------------------------------------
def func332(arg0):
    v1 = load32(CURRENT_PLAYER)
    v3 = load32(PLAYERS)
    while True:  # $label0
        if (arg0 != -1):
            if not load8u(9163792):
                break
        store32(9143000, 0)
        v2 = load32(9213820)
        if load32(9213820):
            func47(entities[v2])
            store32(9213820, 0)
        func45()
        break
    while True:  # $label1
        v4 = load32((((v3 + (v1 * 286704)) + (load32(38428) << 2)) + 284636))
        if not load32((((v3 + (v1 * 286704)) + (load32(38428) << 2)) + 284636)):
            break
        v1 = load32(v4 + 8)
        if not load32(v4 + 8):
            break
        v3 = 0
        if (arg0 == -1):
            while True:  # $label3
                while True:  # $label2
                    v2 = load32((load32(v4) + (v3 << 2)))
                    if not load32((load32(v4) + (v3 << 2))):
                        break
                    v2 = entities[v2]
                    if not load8u(9147152):
                        if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v2 + 110))))):
                            break
                        if (load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v2 + 127) == 6):
                            break
                    func44(v2, 0)
                    v1 = load32(v4 + 8)
                    break
                v3 = (v3 + 1)
                if (u32((v3 + 1)) < u32(v1)):
                    continue
                break
                break
            raise Unreachable()
        while True:  # $label6
            while True:  # $label4
                v1 = load32((load32(v4) + (v3 << 2)))
                if not load32((load32(v4) + (v3 << 2))):
                    break
                v1 = entities[v1]
                if load8u(9163792):
                    if not load8u(9147152):
                        if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v1 + 110))))):
                            break
                        if (load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v1 + 127) == 6):
                            break
                    func44(v1, 0)
                    break
                v6 = load32(v1 + 28)
                while True:  # $label5
                    v2 = load32(9681836)
                    if (load32(9681836) != load32(9681832)):
                        v1 = load32(9681828)
                        break
                    v1 = (load32(9681840) + v2)
                    store32(9681832, (load32(9681840) + v2))
                    v5 = load32(9681828)
                    v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                    if v2:
                        # TODO: memory.copy
                    if v5:
                        v2 = load32(9681836)
                    store32(9681828, v1)
                    break
                store32(9681836, (v2 + 1))
                store32((v1 + (v2 << 2)), v6)
                break
            v3 = (v3 + 1)
            if (u32((v3 + 1)) < u32(load32(v4 + 8))):
                continue
            break
        break
    while True:  # $label7
        if (arg0 != -1):
            if not load8u(9163792):
                break
        return
        break
    func172(1)

# ----------------------------------------------------------
# $func333
# ----------------------------------------------------------
def func333(arg0):
    v1 = load32(CURRENT_PLAYER)
    v2 = load32(PLAYERS)
    while True:  # $label0
        if (arg0 != -1):
            if not load8u(9163792):
                break
        store32(9143000, 0)
        v3 = load32(9213820)
        if load32(9213820):
            func47(entities[v3])
            store32(9213820, 0)
        func45()
        break
    v7 = (v2 + (v1 * 286704))
    v8 = (arg0 == -1)
    v3 = 0
    while True:  # $label7
        while True:  # $label1
            v4 = load32(((v7 + (v3 << 2)) + 284636))
            if not load32(((v7 + (v3 << 2)) + 284636)):
                break
            v5 = 0
            if not load32(v4 + 8):
                break
            while True:  # $label6
                while True:  # $label2
                    v1 = load32((load32(v4) + (v5 << 2)))
                    if not load32((load32(v4) + (v5 << 2))):
                        break
                    while True:  # $label3
                        v1 = entities[v1]
                        if (u32(load32(entities[v1].frame)) >= u32(12)):
                            if not load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 264):
                                break
                        v2 = load32(v1 + 24)
                        if not load32(v1 + 24):
                            break
                        if not load32(v2 + 8):
                            break
                        break
                    while True:  # $label4
                        if not v8:
                            if not load8u(9163792):
                                break
                        if not load8u(9147152):
                            if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v1 + 110))))):
                                break
                            if (load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 20):
                                break
                            if (load8u(v1 + 127) == 6):
                                break
                        func44(v1, 0)
                        break
                        break
                    v9 = load32(v1 + 28)
                    while True:  # $label5
                        v1 = load32(9681836)
                        if (load32(9681836) != load32(9681832)):
                            v2 = load32(9681828)
                            break
                        v2 = (load32(9681840) + v1)
                        store32(9681832, (load32(9681840) + v1))
                        v6 = load32(9681828)
                        v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                        if v1:
                            # TODO: memory.copy
                        if v6:
                            v1 = load32(9681836)
                        store32(9681828, v2)
                        break
                    store32(9681836, (v1 + 1))
                    store32((v2 + (v1 << 2)), v9)
                    break
                v5 = (v5 + 1)
                if (u32((v5 + 1)) < u32(load32(v4 + 8))):
                    continue
                break
            break
        v3 = (v3 + 1)
        if ((v3 + 1) != 255):
            continue
        break
    while True:  # $label8
        if (arg0 != -1):
            if not load8u(9163792):
                break
        return
        break
    func172(1)

# ----------------------------------------------------------
# $func334
# ----------------------------------------------------------
def func334(arg0):
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store32(9143000, 0)
    arg0 = load32(CURRENT_PLAYER)
    v2 = load32(PLAYERS)
    v3 = load32(9213820)
    if load32(9213820):
        func47(entities[v3])
        store32(9213820, 0)
    func45()
    v11 = (v2 + (arg0 * 286704))
    while True:  # $label15
        while True:  # $label12
            while True:  # $label14
                while True:  # $label0
                    v12 = load32(((v7 << 2) + 9940))
                    v8 = load32(((v11 + (load32(((v7 << 2) + 9940)) << 2)) + 284636))
                    if not load32(((v11 + (load32(((v7 << 2) + 9940)) << 2)) + 284636)):
                        break
                    v9 = 0
                    v10 = load32(v8 + 8)
                    if not load32(v8 + 8):
                        break
                    while True:  # $label13
                        while True:  # $label1
                            arg0 = load32((load32(v8) + (v9 << 2)))
                            if not load32((load32(v8) + (v9 << 2))):
                                break
                            v6 = load32(ENTITIES)
                            v2 = entities[arg0]
                            arg0 = load32(entities[arg0].target_x)
                            if not ((load32((load32(9215884) + (load32(entities[arg0].target_x) << 4)) + 4) == 22) | not arg0):
                                break
                            if load8u(v2 + 125):
                                break
                            if load32(v2 + 36):
                                break
                            v3 = load32(v2 + 28)
                            while True:  # $label4
                                while True:  # $label2
                                    arg0 = load32(9215928)
                                    if not load32(9215928):
                                        break
                                    v1 = load32(arg0 + 8)
                                    if not load32(arg0 + 8):
                                        break
                                    v4 = load32(arg0)
                                    arg0 = 0
                                    while True:  # $label3
                                        if (v3 != load32((v6 + (load32((v4 + (arg0 << 2))) * 132)) + 28)):
                                            arg0 = (arg0 + 1)
                                            if (v1 != (arg0 + 1)):
                                                continue
                                            break
                                        break
                                    v1 = 1
                                    break
                                    break
                                while True:  # $label5
                                    arg0 = load32(9215932)
                                    if not load32(9215932):
                                        break
                                    v1 = load32(arg0 + 8)
                                    if not load32(arg0 + 8):
                                        break
                                    v4 = load32(arg0)
                                    arg0 = 0
                                    while True:  # $label6
                                        if (v3 == load32((v6 + (load32((v4 + (arg0 << 2))) * 132)) + 28)):
                                            v1 = 1
                                            break
                                        arg0 = (arg0 + 1)
                                        if ((arg0 + 1) != v1):
                                            continue
                                        break
                                    break
                                while True:  # $label7
                                    arg0 = load32(9215936)
                                    if not load32(9215936):
                                        break
                                    v1 = load32(arg0 + 8)
                                    if not load32(arg0 + 8):
                                        break
                                    v4 = load32(arg0)
                                    arg0 = 0
                                    while True:  # $label8
                                        if (v3 == load32((v6 + (load32((v4 + (arg0 << 2))) * 132)) + 28)):
                                            v1 = 1
                                            break
                                        arg0 = (arg0 + 1)
                                        if ((arg0 + 1) != v1):
                                            continue
                                        break
                                    break
                                v1 = 0
                                arg0 = load32(9215940)
                                if not load32(9215940):
                                    break
                                v4 = load32(arg0 + 8)
                                if not load32(arg0 + 8):
                                    break
                                v13 = load32(arg0)
                                arg0 = 0
                                while True:  # $label9
                                    v1 = (load32((v6 + (load32((v13 + (arg0 << 2))) * 132)) + 28) == v3)
                                    if (load32((v6 + (load32((v13 + (arg0 << 2))) * 132)) + 28) == v3):
                                        break
                                    arg0 = (arg0 + 1)
                                    if ((arg0 + 1) != v4):
                                        continue
                                    break
                                break
                            if v1:
                                break
                            if (v12 != load8u(v2 + 122)):
                                break
                            if (load8u(v2 + 129) == 10):
                                break
                            while True:  # $label10
                                if load32(v2 + 92):
                                    break
                                v1 = load32(9213808)
                                if (u32(load32(9213808)) > u32(9999)):
                                    break
                                arg0 = 1
                                store32(9213808, (v1 + 1))
                                store32(((v1 << 2) + 9173808), v3)
                                while True:  # $label11
                                    if (load8u(9142906) | load8u(9142916)):
                                        break
                                    arg0 = 0
                                    if load8u(9142917):
                                        break
                                    arg0 = load32(9299880)
                                    if load32(9299880):
                                        arg0 = (arg0 - 1)
                                        store32(9299880, (arg0 - 1))
                                        arg0 = load32((load32(9299872) + (arg0 << 2)))
                                        break
                                    arg0 = load32(9163776)
                                    v3 = (load32(9163776) + 1)
                                    store32(9163776, (load32(9163776) + 1))
                                    v1 = load32(9163784)
                                    if (u32(v3) < u32(load32(9163784))):
                                        break
                                    store32(v5 + 16, v1)
                                    a_b()
                                    store32(9163784, (load32(9163784) + 40000))
                                    break
                                store32(v2 + 92, arg0)
                                if not load32(v2 + 36):
                                func203(v2)
                                break
                            if load8u(9163792):
                                break
                            v10 = load32(v8 + 8)
                            break
                        v9 = (v9 + 1)
                        if (u32((v9 + 1)) < u32(v10)):
                            continue
                        break
                    break
                v7 = (v7 + 1)
                if ((v7 + 1) != 3):
                    continue
                break
            if not load32(9213808):
                break
            break
            break
        if load8u(9142917):
            break
        arg0 = load32(v2 + 36)
        arg0 = entities[(load32(v2 + 36) if arg0 else load32(v2 + 28))]
        v2 = ((load8u(entities[(load32(v2 + 36) if arg0 else load32(v2 + 28))].sub_state) * 404) + ENTITY_TYPES)
        v3 = load32(((load8u(entities[(load32(v2 + 36) if arg0 else load32(v2 + 28))].sub_state) * 404) + ENTITY_TYPES) + 220)
        v1 = load16u(arg0 + 114)
        store32(v5, (((load32(v2 + 216) << 4) & 2147483632) + (load16u(arg0 + 112) << 5)))
        store32(v5 + 4, (((v3 << 4) & 2147483632) + (v1 << 5)))
        break
    G.global0 = (v5 + 32)

# ----------------------------------------------------------
# $func335
# ----------------------------------------------------------
def func335(arg0, arg1, arg2, arg3):
    v18 = (arg1 - 30)
    v19 = ((arg1 - 30) + 60)
    v6 = (arg0 - 30)
    v20 = ((arg0 - 30) + 60)
    v8 = load32(9142440)
    v10 = (load32(9142440) + 2)
    v21 = ((load32(9142440) + 2) * load32(((arg2 * 404) + ENTITY_TYPES) + 208))
    v22 = (v8 + 4)
    v23 = load32(ENTITIES)
    v11 = load32(9142840)
    v9 = 2147483647
    v24 = (load32(38500) != arg2)
    while True:  # $label3
        v12 = (v6 + 1)
        if (u32(v6) < u32(v8)):
            v4 = (arg0 - v6)
            v25 = ((arg0 - v6) * v4)
            v5 = v18
            while True:  # $label2
                while True:  # $label0
                    if (u32(v5) >= u32(v8)):
                        break
                    if ((v5 | v6) < 0):
                        break
                    v4 = (arg1 - v5)
                    v13 = (((arg1 - v5) * v4) + v25)
                    if ((((arg1 - v5) * v4) + v25) >= v9):
                        break
                    v7 = load32((v11 + ((v12 + (((v5 + v21) + 1) * v10)) << 2)))
                    if not load32((v11 + ((v12 + (((v5 + v21) + 1) * v10)) << 2))):
                        break
                    if (arg3 == v7):
                        break
                    v14 = (v23 + (v7 * 132))
                    v15 = (load8u((v23 + (v7 * 132)) + 122) != arg2)
                    v4 = (v9 if (load8u((v23 + (v7 * 132)) + 122) != arg2) else v13)
                    v17 = (v16 if v15 else v7)
                    while True:  # $label1
                        if v15:
                            break
                        if v24:
                            break
                        v17 = v7
                        v4 = v13
                        if load32((((load16u(v14 + 112) + ((v22 + load16u(v14 + 114)) * v10)) << 2) + v11) + 8):
                            break
                        break
                    v16 = v17
                    v9 = v4
                    break
                v5 = (v5 + 1)
                if ((v5 + 1) < v19):
                    continue
                break
        v6 = v12
        if (v12 < v20):
            continue
        break
    return v16

# ----------------------------------------------------------
# $func336
# ----------------------------------------------------------
def func336(arg0, arg1, arg2):
    v12 = (arg0 + 29)
    v13 = (arg1 + 29)
    v14 = (arg1 - 30)
    v4 = (arg0 - 30)
    v7 = load32(9142440)
    v8 = (load32(9142440) + 2)
    v15 = load32(38564)
    v16 = load32(ENTITIES)
    v17 = load32(9142840)
    v9 = 2147483647
    while True:  # $label3
        v11 = (v4 + 1)
        if (u32(v4) < u32(v7)):
            v3 = (v4 - arg0)
            v18 = ((v4 - arg0) * v3)
            v3 = v14
            while True:  # $label2
                while True:  # $label0
                    v5 = v3
                    if (u32(v7) <= u32(v3)):
                        break
                    if ((v4 | v5) < 0):
                        break
                    v3 = (v5 - arg1)
                    v3 = (((v5 - arg1) * v3) + v18)
                    if ((((v5 - arg1) * v3) + v18) >= v9):
                        break
                    v6 = (v16 + (load32((v17 + ((v11 + (((v5 + v8) + 1) * v8)) << 2))) * 132))
                    if (u32(load32((v16 + (load32((v17 + ((v11 + (((v5 + v8) + 1) * v8)) << 2))) * 132)) + 64)) >= u32(load32(v6 + 68))):
                        break
                    if (load16u(v6 + 110) != arg2):
                        break
                    v19 = load8u(v6 + 122)
                    v20 = ((load8u(v6 + 122) * 404) + ENTITY_TYPES)
                    if (load32(((load8u(v6 + 122) * 404) + ENTITY_TYPES) + 264) != 1):
                        break
                    if (load32(v20 + 188) != 55):
                        break
                    while True:  # $label1
                        if (v15 != v19):
                            break
                        # br_table (load8u(v6 + 125) - 4)
                        break
                        break
                    v10 = load32(v6 + 28)
                    v9 = v3
                    break
                v3 = (v5 + 1)
                if (v5 < v13):
                    continue
                break
        v3 = (v4 < v12)
        v4 = v11
        if v3:
            continue
        break
    return v10

# ----------------------------------------------------------
# $func337
# ----------------------------------------------------------
def func337(arg0, arg1, arg2, arg3, arg4, arg5):
    v17 = load16u(arg2 + 114)
    v15 = (load16u(arg2 + 114) - 1)
    v18 = load16u(arg2 + 112)
    v16 = (load16u(arg2 + 112) - 1)
    v19 = load8u(arg2 + 122)
    v7 = ((load8u(arg2 + 122) * 404) + ENTITY_TYPES)
    v14 = load32(((load8u(arg2 + 122) * 404) + ENTITY_TYPES) + 60)
    if load32(((load8u(arg2 + 122) * 404) + ENTITY_TYPES) + 60):
        v8 = load32(v7 + 56)
        v10 = load32(9142440)
        v6 = 2147483647
        v7 = 0
        while True:  # $label0
            v9 = (v7 << 2)
            v11 = (load32((v8 + ((v7 << 2) | 4))) + v15)
            v13 = ((load32((v8 + ((v7 << 2) | 4))) + v15) - arg5)
            v9 = (load32((v8 + v9)) + v16)
            v13 = ((load32((v8 + v9)) + v16) - arg4)
            v13 = ((((load32((v8 + ((v7 << 2) | 4))) + v15) - arg5) * v13) + (((load32((v8 + v9)) + v16) - arg4) * v13))
            if (v6 > ((((load32((v8 + ((v7 << 2) | 4))) + v15) - arg5) * v13) + (((load32((v8 + v9)) + v16) - arg4) * v13))):
                v11 = (((u32(v9) < u32(v10)) & ((v9 | v11) >= 0)) & (u32(v10) > u32(v11)))
                v6 = (v13 if (((u32(v9) < u32(v10)) & ((v9 | v11) >= 0)) & (u32(v10) > u32(v11))) else v6)
                v12 = (((v7 & 0xFFFFFFFF) >> 1) if v11 else v12)
            v7 = (v7 + 2)
            if (u32((v7 + 2)) < u32(v14)):
                continue
            break
    arg4 = load16u(40596)
    arg5 = (load16u(40596) + 2)
    store16(40596, (load16u(40596) + 2))
    while True:  # $label1
        if (u32((arg5 & 65535)) < u32(65534)):
            break
        store16(40596, 1)
        arg5 = load32(9142440)
        arg5 = (load32(9142440) * arg5)
        if not (load32(9142440) * arg5):
            break
        # TODO: memory.fill
        break
    while True:  # $label5
        if v14:
            v10 = ((v14 & 0xFFFFFFFF) >> 1)
            v11 = ((v19 * 404) + 9568152)
            v7 = 0
            while True:  # $label6
                while True:  # $label3
                    while True:  # $label2
                        if not v7:
                            break
                        if (v7 & 2):
                            break
                        break
                    arg5 = (load32(v11) + (((((((v7 & 0xFFFFFFFF) >> 2) + v12) % v10) + v10) % v10) << 3))
                    v8 = load32((load32(v11) + (((((((v7 & 0xFFFFFFFF) >> 2) + v12) % v10) + v10) % v10) << 3)))
                    v9 = load32(arg5 + 4)
                    arg5 = load32(9142440)
                    v6 = (load32(9142440) + 2)
                    v6 = load32((load32(9142840) + (((load32((load32(v11) + (((((((v7 & 0xFFFFFFFF) >> 2) + v12) % v10) + v10) % v10) << 3))) + v18) + (((load32(arg5 + 4) + v17) + ((load32(9142440) + 2) * load32(arg3 + 208))) * v6)) << 2)))
                    if (u32(load32((load32(9142840) + (((load32((load32(v11) + (((((((v7 & 0xFFFFFFFF) >> 2) + v12) % v10) + v10) % v10) << 3))) + v18) + (((load32(arg5 + 4) + v17) + ((load32(9142440) + 2) * load32(arg3 + 208))) * v6)) << 2)))) <= u32(2)):
                        if (load32(arg3 + 212) != v6):
                            break
                    if (u32(v6) >= u32(3)):
                        if func205(entities[v6], load16u(arg2 + 110)):
                            break
                        arg5 = load32(9142440)
                    while True:  # $label4
                        v6 = (v9 + v15)
                        v8 = (v8 + v16)
                        v9 = (((v9 + v15) | (v8 + v16)) < 0)
                        if (((v9 + v15) | (v8 + v16)) < 0):
                            break
                        if (u32(arg5) <= u32(v8)):
                            break
                        if (u32(arg5) <= u32(v6)):
                            break
                        if func56(v8, v6, arg3, load16u(arg2 + 110), 0, 0, 1, 1, 0):
                            break
                        arg5 = load32(9142440)
                        break
                    if v9:
                        break
                    if (u32(arg5) <= u32(v8)):
                        break
                    if (u32(arg5) <= u32(v6)):
                        break
                    if not func347(arg0, arg1, v8, v6, v8, v6, arg2, arg3, arg4):
                        break
                    return 1
                    break
                v7 = (v7 + 2)
                if (u32((v7 + 2)) < u32(v14)):
                    continue
                break
        return 0
        break
    store32(arg0, v8)
    store32(arg1, v6)
    return 1

# ----------------------------------------------------------
# $func338
# ----------------------------------------------------------
def func338(arg0, arg1, arg2, arg3):
    v8 = load8u(arg2 + 122)
    v10 = ((load8u(arg2 + 122) * 404) + ENTITY_TYPES)
    v9 = load32(((load8u(arg2 + 122) * 404) + ENTITY_TYPES) + 60)
    v11 = load16u(arg2 + 112)
    v12 = load16u(arg2 + 114)
    v6 = load32(9147324)
    store32(9147324, load32(9147320))
    v7 = load32(9147316)
    v4 = load32(9147312)
    store32(9147316, load32(9147312))
    store32(9147320, v7)
    v6 = (v6 ^ (v6 << 11))
    v6 = ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8))) ^ v6)
    store32(9147312, ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8))) ^ v6))
    v13 = ((v6 % ((v9 & 0xFFFFFFFF) >> 1)) << 1)
    v14 = (v12 - 1)
    v15 = (v11 - 1)
    while True:  # $label1
        if v9:
            v6 = load32(9142440)
            v4 = 0
            while True:  # $label2
                while True:  # $label0
                    v5 = (load32(v10 + 56) + (((v4 + v13) % v9) << 2))
                    v7 = (load32((load32(v10 + 56) + (((v4 + v13) % v9) << 2)) + 4) + v14)
                    if (u32(v6) <= u32((load32((load32(v10 + 56) + (((v4 + v13) % v9) << 2)) + 4) + v14))):
                        break
                    v5 = (load32(v5) + v15)
                    if (u32(v6) <= u32((load32(v5) + v15))):
                        break
                    if ((v5 | v7) < 0):
                        break
                    if func56(v5, v7, arg3, load16u(arg2 + 110), 0, 0, 1, 1, 0):
                        break
                    v6 = load32(9142440)
                    break
                v4 = (v4 + 2)
                if (u32((v4 + 2)) < u32(v9)):
                    continue
                break
        v6 = load16u(40596)
        v4 = (load16u(40596) + 2)
        store16(40596, (load16u(40596) + 2))
        while True:  # $label3
            if (u32((v4 & 65535)) < u32(65534)):
                break
            store16(40596, 1)
            v4 = load32(9142440)
            v4 = (load32(9142440) * v4)
            if not (load32(9142440) * v4):
                break
            # TODO: memory.fill
            break
        if v9:
            v10 = ((v8 * 404) + 9568152)
            v4 = 0
            while True:  # $label5
                while True:  # $label4
                    v7 = (load32(v10) + (((v4 + v13) % v9) << 2))
                    v8 = load32((load32(v10) + (((v4 + v13) % v9) << 2)))
                    v16 = load32(v7 + 4)
                    v7 = load32(9142440)
                    v5 = (load32(9142440) + 2)
                    v5 = load32((load32(9142840) + (((load32((load32(v10) + (((v4 + v13) % v9) << 2))) + v11) + (((load32(v7 + 4) + v12) + ((load32(9142440) + 2) * load32(arg3 + 208))) * v5)) << 2)))
                    if (u32(load32((load32(9142840) + (((load32((load32(v10) + (((v4 + v13) % v9) << 2))) + v11) + (((load32(v7 + 4) + v12) + ((load32(9142440) + 2) * load32(arg3 + 208))) * v5)) << 2)))) <= u32(2)):
                        if (load32(arg3 + 212) != v5):
                            break
                    if (u32(v5) >= u32(3)):
                        if func205(entities[v5], load16u(arg2 + 110)):
                            break
                        v7 = load32(9142440)
                    v5 = (v14 + v16)
                    if (u32(v7) <= u32((v14 + v16))):
                        break
                    v8 = (v8 + v15)
                    if ((v5 | (v8 + v15)) < 0):
                        break
                    if (u32(v7) <= u32(v8)):
                        break
                    if not func347(arg0, arg1, v8, v5, v8, v5, arg2, arg3, v6):
                        break
                    return 1
                    break
                v4 = (v4 + 2)
                if (u32((v4 + 2)) < u32(v9)):
                    continue
                break
        return 0
        break
    store32(arg0, v5)
    store32(arg1, v7)
    return 1

# ----------------------------------------------------------
# $sc
# Export: sc
# ----------------------------------------------------------
def sc(arg0):
    """Export: sc"""
    v12 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    if not arg0:
        func45()
    if load8u(9147152):
        store32(9147132, load8u(9216060))
    if load8u(9142917):
        store32(load32(GAME_STATE) + 48, load32(9142832))
    v9 = load32(PLAYER_COUNT)
    v31 = (load32(PLAYER_COUNT) * 3020)
    v34 = load32(9681936)
    v35 = (load32(load32(9681936) + 8) * 3)
    v17 = (((load32(load32(9681936) + 8) * 3) & 0xFFFFFFFF) >> 2)
    v21 = load32(9142440)
    v11 = (load32(9142440) * v21)
    v25 = ((((load32(9142440) * v21) & 0xFFFFFFFF) >> 2) + 1)
    v7 = load32(9142848)
    v26 = load32(9215892)
    v10 = (v9 * v9)
    v36 = load32(9671136)
    v22 = load32(9142912)
    v27 = load32(9684484)
    v28 = load32(9684468)
    v29 = load32(9684452)
    v30 = (load32(9684484) + (load32(9684468) + load32(9684452)))
    while True:  # $label0
        v13 = load32(9147132)
        if load32(9147132):
            break
        if not v7:
            break
        if (u32((load32(load32(GAME_STATE) + 48) - 1)) > u32(1)):
            break
        break
    v33 = (((v11 & 0xFFFFFFFF) >> 5) + 1)
    v5 = (v17 - -64)
    v23 = (load32(9142912) + ((load32(9684484) + (load32(9684468) + load32(9684452))) + ((((v11 & 0xFFFFFFFF) >> 5) + 1) + (((((v17 - -64) + v31) + v26) + (v10 << 2)) + v25))))
    v24 = load32(9142428)
    v3 = load32(9568068)
    v32 = load32(9568064)
    v14 = ((load32(9568068) - load32(9568064)) >> 7)
    v39 = (v3 == v32)
    if not (v3 == v32):
        v15 = (1 if (u32(v14) <= u32(1)) else v14)
        while True:  # $label3
            v3 = (v32 + (v8 << 7))
            v2 = ((v2 + load32((v32 + (v8 << 7)) + 104)) + 8)
            v4 = load32(v3 + 4)
            v6 = load32(v3)
            if (load32(v3 + 4) != load32(v3)):
                v4 = ((v4 - v6) // 196)
                v19 = (1 if (u32(v4) <= u32(1)) else ((v4 - v6) // 196))
                v1 = 0
                while True:  # $label1
                    v4 = (v6 + (v1 * 196))
                    v2 = ((((((v2 + load32((v6 + (v1 * 196)) + 192)) + load32(v4 + 56)) + load32(v4 + 72)) + load32(v4 + 88)) + load32(v4 + 104)) + 19)
                    v1 = (v1 + 1)
                    if ((v1 + 1) != v19):
                        continue
                    break
            v1 = load32(v3 + 16)
            v4 = load32(v3 + 12)
            if (load32(v3 + 16) != load32(v3 + 12)):
                v3 = ((v1 - v4) // 196)
                v6 = (1 if (u32(v3) <= u32(1)) else ((v1 - v4) // 196))
                v1 = 0
                while True:  # $label2
                    v3 = (v4 + (v1 * 196))
                    v2 = ((((((v2 + load32((v4 + (v1 * 196)) + 192)) + load32(v3 + 56)) + load32(v3 + 72)) + load32(v3 + 88)) + load32(v3 + 104)) + 19)
                    v1 = (v1 + 1)
                    if ((v1 + 1) != v6):
                        continue
                    break
            v8 = (v8 + 1)
            if ((v8 + 1) != v15):
                continue
            break
    v6 = (v23 + v24)
    v3 = 0
    while True:  # $label4
        if not v36:
            v8 = 0
            v23 = 0
            break
        v23 = 0
        v15 = load32(38448)
        v19 = load32(ENTITIES)
        v8 = 0
        v1 = 0
        while True:  # $label6
            while True:  # $label5
                v4 = (v19 + (v1 * 132))
                if (load8u((v19 + (v1 * 132)) + 122) == v15):
                    v8 = (v8 + 4)
                    break
                v18 = load32(v4 + 16)
                if load32(v4 + 16):
                    v6 = ((v6 + load32(v18 + 8)) + 1)
                v18 = load32(v4 + 20)
                if load32(v4 + 20):
                    v6 = ((v6 + load32(v18 + 8)) + 1)
                v23 = (v23 + 33)
                v4 = load32(v4 + 24)
                if not load32(v4 + 24):
                    break
                v18 = load32(v4)
                if load32(v4):
                    v6 = ((v6 + load32(v18 + 8)) + 1)
                v18 = load32(v4 + 12)
                if load32(v4 + 12):
                    v6 = ((v6 + load32(v18 + 8)) + 1)
                v18 = load32(v4 + 8)
                if load32(v4 + 8):
                    v6 = ((v6 + load32(v18 + 8)) + 1)
                v4 = load32(v4 + 4)
                if not load32(v4 + 4):
                    break
                v6 = ((v6 + load32(v4 + 8)) + 1)
                break
            v1 = (v1 + 1)
            if ((v1 + 1) != v36):
                continue
            break
        break
    v15 = (((802 if v13 else ((v9 * 1020) + 802)) * v9) if (v7 | v13) else 0)
    if v9:
        v19 = (v9 + 1)
        v18 = (not v7 | (v13 != 0))
        v37 = load32(PLAYERS)
        v1 = 0
        while True:  # $label8
            v4 = (v37 + (v1 * 286704))
            v20 = load32((v37 + (v1 * 286704)) + 281788)
            if load32((v37 + (v1 * 286704)) + 281788):
                v3 = ((v3 + load32(v20 + 8)) + 1)
            v20 = load32(v4 + 281792)
            if load32(v4 + 281792):
                v3 = ((v3 + load32(v20 + 8)) + 1)
            v20 = load32(v4 + 281796)
            if load32(v4 + 281796):
                v3 = ((v3 + load32(v20 + 8)) + 1)
            v20 = load32(v4 + 286680)
            if load32(v4 + 286680):
                v3 = ((v3 + load32(v20 + 8)) + 1)
            v20 = (v19 if load32(v4 + 281800) else 0)
            while True:  # $label7
                if v18:
                    break
                v4 = load32((v4 + 278572))
                if not load32((v4 + 278572)):
                    break
                v15 = ((v15 + load32(v4 + 8)) + 1)
                break
            v3 = (v3 + v20)
            v1 = (v1 + 1)
            if ((v1 + 1) != v9):
                continue
            break
    v1 = 0
    v18 = (((((v2 + v6) + v8) + v23) + v3) + v15)
    v37 = ((((((v2 + v6) + v8) + v23) + v3) + v15) << 2)
    v3 = (-1 if (u32(v18) > u32(1073741823)) else ((((((v2 + v6) + v8) + v23) + v3) + v15) << 2))
    v4 = func26((-1 if (u32(v18) > u32(1073741823)) else ((((((v2 + v6) + v8) + v23) + v3) + v15) << 2)))
    # TODO: memory.fill
    v3 = load32(CURRENT_PLAYER)
    v6 = load32(59168)
    store32(v4 + 4, v17)
    store32(v4, v6)
    v6 = load8u(9147208)
    store32(v4 + 24, v22)
    store32(v4 + 20, v27)
    store32(v4 + 16, v28)
    store32(v4 + 12, v29)
    store32(v4 + 8, v6)
    store32(v4 + 28, (0 if v13 else load32(9142952)))
    v6 = load32(9142956)
    store32(v4 + 40, v26)
    store32(v4 + 36, v9)
    store32(v4 + 32, (0 if v13 else v6))
    v9 = load32(9163776)
    store32(v4 + 68, (0 if v13 else v3))
    store32(v4 + 64, v36)
    store32(v4 + 60, v23)
    store32(v4 + 56, v8)
    store32(v4 + 52, v7)
    store32(v4 + 48, v21)
    store32(v4 + 44, (0 if v13 else v9))
    v3 = load32(9561752)
    store32(v4 + 76, v2)
    store32(v4 + 72, v3)
    v21 = load32(GAME_STATE)
    v3 = load32(load32(GAME_STATE) + 48)
    store32(v4 + 84, v24)
    store32(v4 + 80, v3)
    store32(v4 + 88, load32(9684364))
    store32(v4 + 92, load32(9684368))
    store32(v4 + 96, load32(9684372))
    storef32(v4 + 100, loadf32(9684340))
    storef32(v4 + 104, loadf32(9684344))
    storef32(v4 + 108, loadf32(9684348))
    storef32(v4 + 112, loadf32(9684352))
    storef32(v4 + 116, loadf32(9684356))
    storef32(v4 + 120, loadf32(9684360))
    store32(v4 + 124, load8u(9147209))
    store32(v4 + 128, load32(9147312))
    store32(v4 + 132, load32(9147316))
    store32(v4 + 136, load32(9147320))
    v3 = load32(9147324)
    store32(v4 + 152, v31)
    store32(v4 + 148, v13)
    store32(v4 + 144, v15)
    store32(v4 + 140, v3)
    v20 = (v5 + v30)
    v25 = (v2 + (v5 + v30))
    v2 = (v24 + (v2 + (v5 + v30)))
    v24 = (v25 + (v24 + (v2 + (v5 + v30))))
    v27 = ((v25 + (v24 + (v2 + (v5 + v30)))) + v10)
    v28 = (((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10)
    v29 = ((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10)
    v30 = (((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10)
    v19 = ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26)
    v22 = (v22 + ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26))
    v9 = ((v22 + ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26)) + v33)
    v40 = (v31 + ((v22 + ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26)) + v33))
    v31 = (v8 + (v31 + ((v22 + ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26)) + v33)))
    v3 = ((v8 + (v31 + ((v22 + ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26)) + v33))) + v23)
    store32(v12 + 28, (v15 + ((v8 + (v31 + ((v22 + ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26)) + v33))) + v23)))
    while True:  # $label9
        if not v11:
            break
        v2 = (v4 + (v2 << 2))
        v6 = load32(9147288)
        if (u32(v11) >= u32(4)):
            v8 = (v11 & -4)
            v7 = 0
            while True:  # $label10
                v16 = load8s((v1 + v6))
                store8((v1 + v2), (((load8s((v1 + v6)) & 0xFFFFFFFF) >> 7) ^ v16))
                v16 = (v1 | 1)
                v16 = load8s((v6 + v16))
                store8((v2 + (v1 | 1)), (((load8s((v6 + v16)) & 0xFFFFFFFF) >> 7) ^ v16))
                v16 = (v1 | 2)
                v16 = load8s((v6 + v16))
                store8((v2 + (v1 | 2)), (((load8s((v6 + v16)) & 0xFFFFFFFF) >> 7) ^ v16))
                v16 = (v1 | 3)
                v16 = load8s((v6 + v16))
                store8((v2 + (v1 | 3)), (((load8s((v6 + v16)) & 0xFFFFFFFF) >> 7) ^ v16))
                v1 = (v1 + 4)
                v7 = (v7 + 4)
                if ((v7 + 4) != v8):
                    continue
                break
        v8 = (v11 & 3)
        if not (v11 & 3):
            break
        v7 = 0
        while True:  # $label11
            v16 = load8s((v1 + v6))
            store8((v1 + v2), (((load8s((v1 + v6)) & 0xFFFFFFFF) >> 7) ^ v16))
            v1 = (v1 + 1)
            v7 = (v7 + 1)
            if ((v7 + 1) != v8):
                continue
            break
        break
    while True:  # $label12
        if not v33:
            break
        v1 = load32(9147376)
        if not load32(9147376):
            break
        if v13:
            break
        if not v11:
            break
        v6 = (v4 + (v22 << 2))
        v2 = 0
        if (v11 != 1):
            v13 = (v11 & -2)
            v7 = 0
            while True:  # $label13
                v8 = (v6 + (((v2 & 0xFFFFFFFF) >> 3) & 536870908))
                v22 = (load32(v8) | ((load16u((v1 + (v2 << 1))) != 0) << (v2 & 30)))
                store32((v6 + (((v2 & 0xFFFFFFFF) >> 3) & 536870908)), (load32(v8) | ((load16u((v1 + (v2 << 1))) != 0) << (v2 & 30))))
                v8 = (v2 | 1)
                store32(v8, (((load16u((v1 + ((v2 | 1) << 1))) != 0) << v8) | v22))
                v2 = (v2 + 2)
                v7 = (v7 + 2)
                if ((v7 + 2) != v13):
                    continue
                break
        if not (v11 & 1):
            break
        v6 = (v6 + (((v2 & 0xFFFFFFFF) >> 3) & 536870908))
        store32((v6 + (((v2 & 0xFFFFFFFF) >> 3) & 536870908)), (load32(v6) | ((load16u((v1 + (v2 << 1))) != 0) << v2)))
        break
    if (u32(v35) >= u32(4)):
        v7 = load32(v34)
        v2 = 0
        while True:  # $label14
            v6 = (v2 << 2)
            v1 = ((v2 << 2) + v4)
            # TODO: i32.div_u
            v6 = (v6 + (3 << 2))
            store32(v7 + 256, load32((v6 + (3 << 2))))
            store32(v1 + 260, load32(v6 + 4))
            store32(v1 + 264, load32(v6 + 8))
            v2 = (v2 + 3)
            if (u32((v2 + 3)) < u32(v17)):
                continue
            break
    while True:  # $label15
        v2 = load32(9684452)
        if not load32(9684452):
            break
        v13 = (v2 & 3)
        v8 = 0
        v1 = load32(9684444)
        while True:  # $label16
            if (u32(v2) < u32(4)):
                v2 = 0
                break
            v17 = (v2 & -4)
            v2 = 0
            v7 = 0
            while True:  # $label17
                v6 = (v4 + (v5 << 2))
                v11 = (v2 << 2)
                store32((v4 + (v5 << 2)), load32((v1 + (v2 << 2))))
                store32(v6 + 4, load32((v1 + (v11 | 4))))
                store32(v6 + 8, load32((v1 + (v11 | 8))))
                store32(v6 + 12, load32((v1 + (v11 | 12))))
                v2 = (v2 + 4)
                v5 = (v5 + 4)
                v7 = (v7 + 4)
                if ((v7 + 4) != v17):
                    continue
                break
            break
        if not v13:
            break
        while True:  # $label18
            store32((v4 + (v5 << 2)), load32((v1 + (v2 << 2))))
            v2 = (v2 + 1)
            v5 = (v5 + 1)
            v8 = (v8 + 1)
            if ((v8 + 1) != v13):
                continue
            break
        break
    while True:  # $label19
        v2 = load32(9684468)
        if not load32(9684468):
            break
        v13 = (v2 & 3)
        v8 = 0
        v1 = load32(9684460)
        while True:  # $label20
            if (u32(v2) < u32(4)):
                v2 = 0
                break
            v17 = (v2 & -4)
            v2 = 0
            v7 = 0
            while True:  # $label21
                v6 = (v4 + (v5 << 2))
                v11 = (v2 << 2)
                store32((v4 + (v5 << 2)), load32((v1 + (v2 << 2))))
                store32(v6 + 4, load32((v1 + (v11 | 4))))
                store32(v6 + 8, load32((v1 + (v11 | 8))))
                store32(v6 + 12, load32((v1 + (v11 | 12))))
                v2 = (v2 + 4)
                v5 = (v5 + 4)
                v7 = (v7 + 4)
                if ((v7 + 4) != v17):
                    continue
                break
            break
        if not v13:
            break
        while True:  # $label22
            store32((v4 + (v5 << 2)), load32((v1 + (v2 << 2))))
            v2 = (v2 + 1)
            v5 = (v5 + 1)
            v8 = (v8 + 1)
            if ((v8 + 1) != v13):
                continue
            break
        break
    while True:  # $label23
        v2 = load32(9684484)
        if not load32(9684484):
            break
        v13 = (v2 & 3)
        v8 = 0
        v1 = load32(9684476)
        while True:  # $label24
            if (u32(v2) < u32(4)):
                v2 = 0
                break
            v17 = (v2 & -4)
            v2 = 0
            v7 = 0
            while True:  # $label25
                v6 = (v4 + (v5 << 2))
                v11 = (v2 << 2)
                store32((v4 + (v5 << 2)), load32((v1 + (v2 << 2))))
                store32(v6 + 4, load32((v1 + (v11 | 4))))
                store32(v6 + 8, load32((v1 + (v11 | 8))))
                store32(v6 + 12, load32((v1 + (v11 | 12))))
                v2 = (v2 + 4)
                v5 = (v5 + 4)
                v7 = (v7 + 4)
                if ((v7 + 4) != v17):
                    continue
                break
            break
        if not v13:
            break
        while True:  # $label26
            store32((v4 + (v5 << 2)), load32((v1 + (v2 << 2))))
            v2 = (v2 + 1)
            v5 = (v5 + 1)
            v8 = (v8 + 1)
            if ((v8 + 1) != v13):
                continue
            break
        break
    store32(v12 + 24, v20)
    if not v39:
        v14 = (1 if (u32(v14) <= u32(1)) else v14)
        v13 = 0
        while True:  # $label30
            v2 = load32(v12 + 24)
            v1 = (v4 + (load32(v12 + 24) << 2))
            v8 = (v32 + (v13 << 7))
            v17 = load32((v32 + (v13 << 7)) + 4)
            v7 = load32(v8)
            store32((v4 + (load32(v12 + 24) << 2)), ((load32((v32 + (v13 << 7)) + 4) - load32(v8)) // 196))
            v11 = load32(v8 + 16)
            v5 = load32(v8 + 12)
            store32(v1 + 4, ((load32(v8 + 16) - load32(v8 + 12)) // 196))
            store32(v1 + 8, load32(v8 + 104))
            v1 = (v2 + 3)
            if load32(v8 + 104):
                v6 = 0
                while True:  # $label27
                    store32((v4 + (v1 << 2)), load16u((v8 + (v6 << 1)) + 24))
                    v1 = (v1 + 1)
                    v6 = (v6 + 1)
                    if (u32((v6 + 1)) < u32(load32(v8 + 104))):
                        continue
                    break
            v2 = (v4 + (v1 << 2))
            store32((v4 + (v1 << 2)), load32(v8 + 108))
            store32(v2 + 4, load32(v8 + 112))
            store32(v2 + 8, load32(v8 + 116))
            store32(v2 + 12, load32(v8 + 120))
            v6 = load32(v8 + 124)
            store32(v12 + 24, (v1 + 5))
            store32(v2 + 16, v6)
            v1 = 0
            v2 = 0
            if (v7 != v17):
                while True:  # $label28
                    func382((v7 + (v1 * 196)), v4, (v12 + 24))
                    v1 = (v1 + 1)
                    v7 = load32(v8)
                    if (u32((v1 + 1)) < u32(((load32(v8 + 4) - load32(v8)) // 196))):
                        continue
                    break
                v11 = load32(v8 + 16)
                v5 = load32(v8 + 12)
            if (v5 != v11):
                while True:  # $label29
                    func382((v5 + (v2 * 196)), v4, (v12 + 24))
                    v2 = (v2 + 1)
                    v5 = load32(v8 + 12)
                    if (u32((v2 + 1)) < u32(((load32(v8 + 16) - load32(v8 + 12)) // 196))):
                        continue
                    break
            v13 = (v13 + 1)
            if ((v13 + 1) != v14):
                continue
            break
    while True:  # $label31
        if not v15:
            break
        v8 = 0
        v17 = load32(PLAYER_COUNT)
        if not load32(PLAYER_COUNT):
            break
        v1 = (v17 * 255)
        v1 = (1 if (u32(v1) <= u32(1)) else (v17 * 255))
        v13 = ((1 if (u32(v1) <= u32(1)) else (v17 * 255)) & -4)
        v11 = (v1 & 3)
        v33 = load32(9147132)
        v32 = load32(PLAYERS)
        v34 = (v1 - 1)
        v35 = (u32((v1 - 1)) > u32(2))
        while True:  # $label45
            while True:  # $label32
                if v33:
                    break
                v15 = (v32 + (v8 * 286704))
                v6 = load32((v32 + (v8 * 286704)) + 278556)
                v7 = 0
                v2 = 0
                v1 = 0
                if v35:
                    while True:  # $label33
                        v14 = (v4 + (v3 << 2))
                        v5 = (v2 << 2)
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        store32(v14 + 4, load32((v6 + (v5 | 4))))
                        store32(v14 + 8, load32((v6 + (v5 | 8))))
                        store32(v14 + 12, load32((v6 + (v5 | 12))))
                        v2 = (v2 + 4)
                        v3 = (v3 + 4)
                        v1 = (v1 + 4)
                        if ((v1 + 4) != v13):
                            continue
                        break
                if v11:
                    while True:  # $label34
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        v2 = (v2 + 1)
                        v3 = (v3 + 1)
                        v7 = (v7 + 1)
                        if ((v7 + 1) != v11):
                            continue
                        break
                v6 = load32((v15 + 278560))
                v7 = 0
                v2 = 0
                v1 = 0
                v22 = (u32(v34) < u32(3))
                if not (u32(v34) < u32(3)):
                    while True:  # $label35
                        v14 = (v4 + (v3 << 2))
                        v5 = (v2 << 2)
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        store32(v14 + 4, load32((v6 + (v5 | 4))))
                        store32(v14 + 8, load32((v6 + (v5 | 8))))
                        store32(v14 + 12, load32((v6 + (v5 | 12))))
                        v2 = (v2 + 4)
                        v3 = (v3 + 4)
                        v1 = (v1 + 4)
                        if ((v1 + 4) != v13):
                            continue
                        break
                if v11:
                    while True:  # $label36
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        v2 = (v2 + 1)
                        v3 = (v3 + 1)
                        v7 = (v7 + 1)
                        if ((v7 + 1) != v11):
                            continue
                        break
                v6 = load32((v15 + 278564))
                v7 = 0
                v2 = 0
                v1 = 0
                if not v22:
                    while True:  # $label37
                        v14 = (v4 + (v3 << 2))
                        v5 = (v2 << 2)
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        store32(v14 + 4, load32((v6 + (v5 | 4))))
                        store32(v14 + 8, load32((v6 + (v5 | 8))))
                        store32(v14 + 12, load32((v6 + (v5 | 12))))
                        v2 = (v2 + 4)
                        v3 = (v3 + 4)
                        v1 = (v1 + 4)
                        if ((v1 + 4) != v13):
                            continue
                        break
                if v11:
                    while True:  # $label38
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        v2 = (v2 + 1)
                        v3 = (v3 + 1)
                        v7 = (v7 + 1)
                        if ((v7 + 1) != v11):
                            continue
                        break
                v6 = load32((v15 + 278568))
                v7 = 0
                v2 = 0
                v1 = 0
                if not v22:
                    while True:  # $label39
                        v5 = (v4 + (v3 << 2))
                        v14 = (v2 << 2)
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        store32(v5 + 4, load32((v6 + (v14 | 4))))
                        store32(v5 + 8, load32((v6 + (v14 | 8))))
                        v5 = (v3 + 3)
                        store32((v4 + ((v3 + 3) << 2)), load32((v6 + (v14 | 12))))
                        v2 = (v2 + 4)
                        v3 = (v3 + 4)
                        v1 = (v1 + 4)
                        if ((v1 + 4) != v13):
                            continue
                        break
                if v11:
                    while True:  # $label40
                        v5 = v3
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        v2 = (v2 + 1)
                        v3 = (v3 + 1)
                        v7 = (v7 + 1)
                        if ((v7 + 1) != v11):
                            continue
                        break
                v1 = load32((v15 + 278572))
                store32((v4 + (v3 << 2)), load32(load32((v15 + 278572)) + 8))
                v3 = (v5 + 2)
                if not load32(v1 + 8):
                    break
                v5 = load32(v1)
                v2 = 0
                while True:  # $label41
                    store32((v4 + (v3 << 2)), load32((v5 + (v2 << 2))))
                    v3 = (v3 + 1)
                    v2 = (v2 + 1)
                    if (u32((v2 + 1)) < u32(load32(v1 + 8))):
                        continue
                    break
                break
            v1 = 0
            v6 = 0
            while True:  # $label42
                v5 = (v4 + (v3 << 2))
                v2 = (v32 + (v8 * 286704))
                v7 = ((v32 + (v8 * 286704)) + (v6 << 2))
                store32((v4 + (v3 << 2)), load32((((v32 + (v8 * 286704)) + (v6 << 2)) + 278576)))
                store32(v5 + 4, load32((v7 + 278580)))
                store32(v5 + 8, load32((v7 + 278584)))
                v3 = (v3 + 3)
                v6 = (v6 + 3)
                if ((v6 + 3) != 255):
                    continue
                break
            while True:  # $label43
                v5 = (v4 + (v3 << 2))
                v6 = (v2 + (v1 << 2))
                store32((v4 + (v3 << 2)), load32(((v2 + (v1 << 2)) + 279596)))
                store32(v5 + 4, load32((v6 + 279600)))
                store32(v5 + 8, load32((v6 + 279604)))
                v3 = (v3 + 3)
                v1 = (v1 + 3)
                if ((v1 + 3) != 255):
                    continue
                break
            v6 = 0
            while True:  # $label44
                v5 = v3
                v1 = (v4 + (v3 << 2))
                v3 = (v2 + (v6 << 2))
                store32((v4 + (v3 << 2)), load32(((v2 + (v6 << 2)) + 280616)))
                store32(v1 + 4, load32((v3 + 280620)))
                store32(v1 + 8, load32((v3 + 280624)))
                v3 = (v5 + 3)
                v6 = (v6 + 3)
                if ((v6 + 3) != 255):
                    continue
                break
            store32((v4 + (v3 << 2)), load32((v2 + 281636)))
            store32(v1 + 16, load32((v2 + 281640)))
            store32(v1 + 20, load32((v2 + 281644)))
            store32(v1 + 24, load32((v2 + 281648)))
            store32(v1 + 28, load32((v2 + 281652)))
            store32(v1 + 32, load32((v2 + 281656)))
            store32(v1 + 36, load32((v2 + 281660)))
            store32(v1 + 40, load32((v2 + 281664)))
            store32(v1 + 44, load32((v2 + 281668)))
            store32(v1 + 48, load32((v2 + 281672)))
            store32(v1 + 52, load32((v2 + 281676)))
            store32(v1 + 56, load32((v2 + 281680)))
            store32(v1 + 60, load32((v2 + 281684)))
            store32((v1 - -64), load32((v2 + 281688)))
            store32(v1 + 68, load32((v2 + 281692)))
            store32(v1 + 72, load32((v2 + 281696)))
            store32(v1 + 76, load32((v2 + 281700)))
            store32(v1 + 80, load32((v2 + 281704)))
            store32(v1 + 84, load32((v2 + 281708)))
            store32(v1 + 88, load32((v2 + 281712)))
            store32(v1 + 92, load32((v2 + 281716)))
            store32(v1 + 96, load32((v2 + 281720)))
            store32(v1 + 100, load32((v2 + 281724)))
            store32(v1 + 104, load32((v2 + 281728)))
            store32(v1 + 108, load32((v2 + 281732)))
            store32(v1 + 112, load32((v2 + 281736)))
            store32(v1 + 116, load32((v2 + 281740)))
            store32(v1 + 120, load32((v2 + 281744)))
            store32(v1 + 124, load32((v2 + 281748)))
            store32(v1 + 128, load32((v2 + 281752)))
            store32(v1 + 132, load32((v2 + 281756)))
            store32(v1 + 136, load32((v2 + 281760)))
            store32(v1 + 140, load32((v2 + 281764)))
            store32(v1 + 144, load32((v2 + 281768)))
            store32(v1 + 148, load32((v2 + 281772)))
            store32(v1 + 152, load32((v2 + 281776)))
            store32(v1 + 156, load32((v2 + 281780)))
            v3 = (v5 + 40)
            v8 = (v8 + 1)
            if ((v8 + 1) != v17):
                continue
            break
        break
    v3 = 0
    while True:  # $label46
        v5 = load32(9142428)
        if not load32(9142428):
            break
        if (u32(v5) >= u32(4)):
            v1 = (v5 & -4)
            v2 = 0
            while True:  # $label47
                store32((v4 + ((v3 + v25) << 2)), load32((v21 + (v3 << 2))))
                v6 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v25) << 2)), load32((v21 + (v6 << 2))))
                v6 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v25) << 2)), load32((v21 + (v6 << 2))))
                v6 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v25) << 2)), load32((v21 + (v6 << 2))))
                v3 = (v3 + 4)
                v2 = (v2 + 4)
                if ((v2 + 4) != v1):
                    continue
                break
        v5 = (v5 & 3)
        if not (v5 & 3):
            break
        v2 = 0
        while True:  # $label48
            store32((v4 + ((v3 + v25) << 2)), load32((v21 + (v3 << 2))))
            v3 = (v3 + 1)
            v2 = (v2 + 1)
            if ((v2 + 1) != v5):
                continue
            break
        break
    while True:  # $label49
        if not v10:
            break
        v1 = 0
        v5 = load32(9143004)
        v3 = 0
        if (u32(v10) >= u32(4)):
            v2 = (v10 & -4)
            v6 = 0
            while True:  # $label50
                store32((v4 + ((v3 + v24) << 2)), load8u((v3 + v5)))
                v7 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v24) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v24) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v24) << 2)), load8u((v5 + v7)))
                v3 = (v3 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v2):
                    continue
                break
        v2 = (v10 & 3)
        if (v10 & 3):
            while True:  # $label51
                store32((v4 + ((v3 + v24) << 2)), load8u((v3 + v5)))
                v3 = (v3 + 1)
                v1 = (v1 + 1)
                if ((v1 + 1) != v2):
                    continue
                break
        if not v10:
            break
        v1 = 0
        v5 = load32(9143008)
        v3 = 0
        if (u32(v10) >= u32(4)):
            v2 = (v10 & -4)
            v6 = 0
            while True:  # $label52
                store32((v4 + ((v3 + v27) << 2)), load8u((v3 + v5)))
                v7 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v27) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v27) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v27) << 2)), load8u((v5 + v7)))
                v3 = (v3 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v2):
                    continue
                break
        v2 = (v10 & 3)
        if (v10 & 3):
            while True:  # $label53
                store32((v4 + ((v3 + v27) << 2)), load8u((v3 + v5)))
                v3 = (v3 + 1)
                v1 = (v1 + 1)
                if ((v1 + 1) != v2):
                    continue
                break
        if not v10:
            break
        v1 = 0
        v5 = load32(9143012)
        v3 = 0
        if (u32(v10) >= u32(4)):
            v2 = (v10 & -4)
            v6 = 0
            while True:  # $label54
                store32((v4 + ((v3 + v28) << 2)), load8u((v3 + v5)))
                v7 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v28) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v28) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v28) << 2)), load8u((v5 + v7)))
                v3 = (v3 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v2):
                    continue
                break
        v2 = (v10 & 3)
        if (v10 & 3):
            while True:  # $label55
                store32((v4 + ((v3 + v28) << 2)), load8u((v3 + v5)))
                v3 = (v3 + 1)
                v1 = (v1 + 1)
                if ((v1 + 1) != v2):
                    continue
                break
        if not v10:
            break
        v1 = 0
        v5 = load32(9143016)
        v3 = 0
        if (u32(v10) >= u32(4)):
            v2 = (v10 & -4)
            v6 = 0
            while True:  # $label56
                store32((v4 + ((v3 + v29) << 2)), load8u((v3 + v5)))
                v7 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v29) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v29) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v29) << 2)), load8u((v5 + v7)))
                v3 = (v3 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v2):
                    continue
                break
        v2 = (v10 & 3)
        if not (v10 & 3):
            break
        while True:  # $label57
            store32((v4 + ((v3 + v29) << 2)), load8u((v3 + v5)))
            v3 = (v3 + 1)
            v1 = (v1 + 1)
            if ((v1 + 1) != v2):
                continue
            break
        break
    while True:  # $label58
        if not v26:
            break
        v1 = 0
        v5 = load32(9215884)
        v3 = 0
        if (u32(v26) >= u32(4)):
            v2 = (v26 & -4)
            v6 = 0
            while True:  # $label59
                store32((v4 + ((v3 + v30) << 2)), load32((v5 + (v3 << 2))))
                v7 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v30) << 2)), load32((v5 + (v7 << 2))))
                v7 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v30) << 2)), load32((v5 + (v7 << 2))))
                v7 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v30) << 2)), load32((v5 + (v7 << 2))))
                v3 = (v3 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v2):
                    continue
                break
        v2 = (v26 & 3)
        if not (v26 & 3):
            break
        while True:  # $label60
            store32((v4 + ((v3 + v30) << 2)), load32((v5 + (v3 << 2))))
            v3 = (v3 + 1)
            v1 = (v1 + 1)
            if ((v1 + 1) != v2):
                continue
            break
        break
    v3 = 0
    while True:  # $label61
        v2 = load32(9142912)
        if not load32(9142912):
            break
        v5 = load32(9142908)
        if (u32(v2) >= u32(4)):
            v6 = (v2 & -4)
            v1 = 0
            while True:  # $label62
                store32((v4 + ((v3 + v19) << 2)), load32((v5 + (v3 << 2))))
                v7 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v19) << 2)), load32((v5 + (v7 << 2))))
                v7 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v19) << 2)), load32((v5 + (v7 << 2))))
                v7 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v19) << 2)), load32((v5 + (v7 << 2))))
                v3 = (v3 + 4)
                v1 = (v1 + 4)
                if ((v1 + 4) != v6):
                    continue
                break
        v2 = (v2 & 3)
        if not (v2 & 3):
            break
        v1 = 0
        while True:  # $label63
            store32((v4 + ((v3 + v19) << 2)), load32((v5 + (v3 << 2))))
            v3 = (v3 + 1)
            v1 = (v1 + 1)
            if ((v1 + 1) != v2):
                continue
            break
        break
    if load8u(9142917):
        store32(v21 + 48, 0)
    v6 = 0
    v7 = 0
    if load32(PLAYER_COUNT):
        v3 = v9
        while True:  # $label78
            v9 = (v4 + ((v3 + v6) << 2))
            v1 = players[v7]
            store32((v4 + ((v3 + v6) << 2)), load32(players[v7]))
            store32(v9 + 4, load32(v1 + 4))
            store32(v9 + 8, load32(v1 + 8))
            store32(v9 + 12, load32(v1 + 12))
            store32(v9 + 16, load32(v1 + 16))
            store32(v9 + 20, load32(v1 + 20))
            store32(v9 + 24, load32(v1 + 24))
            store32(v9 + 28, load32(v1 + 28))
            store32(v9 + 32, load32(v1 + 32))
            store32(v9 + 36, load32(v1 + 36))
            while True:  # $label64
                v2 = load32(v1 + 281788)
                if not load32(v1 + 281788):
                    break
                store32(v9 + 40, load32(v12 + 28))
                v5 = load32(v2 + 8)
                v8 = load32(v12 + 28)
                store32(v12 + 28, (load32(v12 + 28) + 1))
                store32((v4 + (v8 << 2)), v5)
                if not load32(v2 + 8):
                    break
                v8 = load32(v2)
                v5 = 0
                while True:  # $label65
                    v10 = load32((v8 + (v5 << 2)))
                    v11 = load32(v12 + 28)
                    store32(v12 + 28, (load32(v12 + 28) + 1))
                    store32((v4 + (v11 << 2)), v10)
                    v5 = (v5 + 1)
                    if (u32((v5 + 1)) < u32(load32(v2 + 8))):
                        continue
                    break
                break
            while True:  # $label66
                v2 = load32(v1 + 281792)
                if not load32(v1 + 281792):
                    break
                store32(v9 + 44, load32(v12 + 28))
                v5 = load32(v2 + 8)
                v8 = load32(v12 + 28)
                store32(v12 + 28, (load32(v12 + 28) + 1))
                store32((v4 + (v8 << 2)), v5)
                if not load32(v2 + 8):
                    break
                v8 = load32(v2)
                v5 = 0
                while True:  # $label67
                    v10 = load32((v8 + (v5 << 2)))
                    v11 = load32(v12 + 28)
                    store32(v12 + 28, (load32(v12 + 28) + 1))
                    store32((v4 + (v11 << 2)), v10)
                    v5 = (v5 + 1)
                    if (u32((v5 + 1)) < u32(load32(v2 + 8))):
                        continue
                    break
                break
            while True:  # $label68
                v2 = load32(v1 + 281796)
                if not load32(v1 + 281796):
                    break
                store32(v9 + 48, load32(v12 + 28))
                v5 = load32(v2 + 8)
                v8 = load32(v12 + 28)
                store32(v12 + 28, (load32(v12 + 28) + 1))
                store32((v4 + (v8 << 2)), v5)
                if not load32(v2 + 8):
                    break
                v8 = load32(v2)
                v5 = 0
                while True:  # $label69
                    v10 = load32((v8 + (v5 << 2)))
                    v11 = load32(v12 + 28)
                    store32(v12 + 28, (load32(v12 + 28) + 1))
                    store32((v4 + (v11 << 2)), v10)
                    v5 = (v5 + 1)
                    if (u32((v5 + 1)) < u32(load32(v2 + 8))):
                        continue
                    break
                break
            while True:  # $label70
                v2 = load32(v1 + 286680)
                if not load32(v1 + 286680):
                    break
                store32(v9 + 52, load32(v12 + 28))
                v5 = load32(v2 + 8)
                v9 = load32(v12 + 28)
                store32(v12 + 28, (load32(v12 + 28) + 1))
                store32((v4 + (v9 << 2)), v5)
                if not load32(v2 + 8):
                    break
                v9 = load32(v2)
                v5 = 0
                while True:  # $label71
                    v8 = load32((v9 + (v5 << 2)))
                    v10 = load32(v12 + 28)
                    store32(v12 + 28, (load32(v12 + 28) + 1))
                    store32((v4 + (v10 << 2)), v8)
                    v5 = (v5 + 1)
                    if (u32((v5 + 1)) < u32(load32(v2 + 8))):
                        continue
                    break
                break
            v5 = (v6 + 14)
            v6 = 0
            while True:  # $label72
                v9 = v5
                v5 = (v4 + ((v5 + v3) << 2))
                v2 = (v1 + (v6 * 36))
                store32((v4 + ((v5 + v3) << 2)), load32(((v1 + (v6 * 36)) + 269376)))
                store32(v5 + 4, load32((v2 + 269380)))
                store32(v5 + 8, load32((v2 + 269384)))
                store32(v5 + 12, load32((v2 + 269388)))
                store32(v5 + 16, load32((v2 + 269392)))
                store32(v5 + 20, load32((v2 + 269396)))
                store32(v5 + 24, load32((v2 + 269400)))
                store32(v5 + 28, load32((v2 + 269404)))
                store32(v5 + 32, load32((v2 + 269408)))
                v5 = (v9 + 9)
                v6 = (v6 + 1)
                if ((v6 + 1) != 255):
                    continue
                break
            v6 = (v3 + v5)
            v5 = 0
            while True:  # $label73
                v2 = (v1 + 281808)
                store32((v4 + ((v5 + v6) << 2)), load32(((v1 + 281808) + (v5 << 2))))
                v8 = (v5 + 1)
                store32((v4 + ((v6 + (v5 + 1)) << 2)), load32((v2 + (v8 << 2))))
                v8 = (v5 + 2)
                store32((v4 + ((v6 + (v5 + 2)) << 2)), load32((v2 + (v8 << 2))))
                v5 = (v5 + 3)
                if ((v5 + 3) != 255):
                    continue
                break
            v2 = (v6 + 255)
            v5 = 0
            while True:  # $label74
                v8 = (v1 + 282828)
                store32((v4 + ((v2 + v5) << 2)), load32(((v1 + 282828) + (v5 << 2))))
                v10 = (v5 + 1)
                store32((v4 + ((v2 + (v5 + 1)) << 2)), load32((v8 + (v10 << 2))))
                v10 = (v5 + 2)
                store32((v4 + ((v2 + (v5 + 2)) << 2)), load32((v8 + (v10 << 2))))
                v5 = (v5 + 3)
                if ((v5 + 3) != 255):
                    continue
                break
            v2 = ((v6 << 2) + v4)
            store32((((v6 << 2) + v4) + 2040), load32(v1 + 283848))
            store32((v2 + 2044), load32((v1 + 283852)))
            store32((v2 + 2048), load32((v1 + 283856)))
            store32((v2 + 2052), load32((v1 + 283860)))
            store32((v2 + 2056), load32(v1 + 283864))
            if load8u(9147152):
                func425(v1)
            v5 = 0
            if load32(9147132):
            else:
            store32(0, load32(v1 + 283872))
            if load32(9147132):
            else:
            store32(0, load32(v1 + 283876))
            store32((v2 + 2068), load32(v1 + 283960))
            store32((v2 + 2072), load32(v1 + 283968))
            store32((v2 + 2076), (load16u(v1 + 283972) | (load8u((v1 + 283974)) << 16)))
            v6 = (v6 + 520)
            while True:  # $label75
                v8 = (v1 + 283984)
                store32((v4 + ((v5 + v6) << 2)), load32(((v1 + 283984) + (v5 << 2))))
                v10 = (v5 | 1)
                store32((v4 + ((v6 + (v5 | 1)) << 2)), load32((v8 + (v10 << 2))))
                v10 = (v5 | 2)
                store32((v4 + ((v6 + (v5 | 2)) << 2)), load32((v8 + (v10 << 2))))
                v8 = (v5 | 3)
                if ((v5 | 3) != 155):
                    store32((v4 + ((v6 + v8) << 2)), load32(((v1 + (v8 << 2)) + 283984)))
                    v5 = (v5 + 4)
                    continue
                break
            store32((v2 + 2700), load32(v1 + 283868))
            store32((v2 + 2704), load32(v1 + 283912))
            store32((v2 + 2708), load32(v1 + 283916))
            store32((v2 + 2712), load32(v1 + 283920))
            store32((v2 + 2716), load32(v1 + 283964))
            store32((v2 + 2720), load32(v1 + 283904))
            store32((v2 + 2724), load32(v1 + 283880))
            store32((v2 + 2728), load32(v1 + 283940))
            store32((v2 + 2732), load32(v1 + 281804))
            store32((v2 + 2736), load32(v1 + 283924))
            store32((v2 + 2740), load32(v1 + 283936))
            store32((v2 + 2744), load32(v1 + 283948))
            store32((v2 + 2748), load32(v1 + 283956))
            store32((v2 + 2752), load32(v1 + 284616))
            store32((v2 + 2756), load8u(v1 + 286700))
            store32((v2 + 2760), load8u(v1 + 286701))
            store32((v2 + 2764), load8u(v1 + 286699))
            store32((v2 + 2768), load8u(v1 + 92))
            store32((v2 + 2772), load8u(v1 + 93))
            store32((v2 + 2776), load32(v1 + 283964))
            store32((v2 + 2780), load32(v1 + 283952))
            store32((v2 + 2784), load32(v1 + 80))
            store32((v2 + 2788), load32(v1 + 84))
            store32((v2 + 2792), load32(v1 + 88))
            while True:  # $label76
                v6 = load32(v1 + 281800)
                if not load32(v1 + 281800):
                    break
                store32((v2 + 2796), load32(v12 + 28))
                v5 = 0
                if not load32(PLAYER_COUNT):
                    break
                while True:  # $label77
                    v8 = load32((v6 + (v5 << 2)))
                    v10 = load32(v12 + 28)
                    store32(v12 + 28, (load32(v12 + 28) + 1))
                    store32((v4 + (v10 << 2)), v8)
                    v5 = (v5 + 1)
                    if (u32((v5 + 1)) < u32(load32(PLAYER_COUNT))):
                        continue
                    break
                break
            store32((v2 + 2800), load32(v1 + 284608))
            store32((v2 + 2804), load32(v1 + 286684))
            store32((v2 + 2808), load8u(v1 + 286696))
            store32((v2 + 2812), load32(v1 + 283976))
            store32((v2 + 2816), load32(v1 + 283980))
            store32((v2 + 2820), load32(v1 + 286688))
            if load32(9147132):
            else:
            store32(0, load32(v1 + 283896))
            if load32(9147132):
            else:
            store32(0, load32(v1 + 283900))
            v6 = (v9 + 717)
            v7 = (v7 + 1)
            if (u32((v7 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break
    if (u32(v36) >= u32(4)):
        # TODO: i32.div_u
        v9 = 33
        v26 = (33 << 5)
        v23 = (v9 * 31)
        v15 = (v9 * 30)
        v21 = (v9 * 29)
        v25 = (v9 * 28)
        v24 = (v9 * 27)
        v27 = (v9 * 26)
        v28 = (v9 * 25)
        v29 = (v9 * 24)
        v30 = (v9 * 23)
        v19 = (v9 * 22)
        v14 = (v9 * 21)
        v17 = (v9 * 20)
        v32 = (v9 * 19)
        v22 = (v9 * 18)
        v33 = (v9 * 17)
        v34 = (v9 << 4)
        v35 = (v9 * 15)
        v39 = (v9 * 14)
        v20 = (v9 * 13)
        v16 = (v9 * 12)
        v41 = (v9 * 11)
        v42 = (v9 * 10)
        v43 = (v9 * 9)
        v8 = 3
        v44 = (v9 << 3)
        v45 = (v9 * 7)
        v46 = (v9 * 6)
        v47 = (v9 * 5)
        v48 = (v9 << 2)
        v49 = (v9 * 3)
        v50 = (v9 << 1)
        v13 = load32(9147132)
        v51 = load32(38448)
        v52 = load32(ENTITIES)
        v3 = load32(v12 + 28)
        v7 = 0
        v11 = 0
        while True:  # $label92
            while True:  # $label79
                v5 = (v52 + (v8 * 132))
                v10 = load8u((v52 + (v8 * 132)) + 122)
                if (load8u((v52 + (v8 * 132)) + 122) == v51):
                    v1 = (v4 + ((v11 + v40) << 2))
                    store32((v4 + ((v11 + v40) << 2)), load32(v5 + 28))
                    store32(v1 + 4, load32(v5 + 64))
                    store32(v1 + 8, load8u(v5 + 124))
                    store32(v1 + 12, load32(v5 + 112))
                    v11 = (v11 + 4)
                    break
                while True:  # $label80
                    v2 = load32(v5 + 16)
                    if not load32(v5 + 16):
                        break
                    store32((v4 + ((v7 + v31) << 2)), v3)
                    store32((v4 + (v3 << 2)), load32(v2 + 8))
                    v3 = (v3 + 1)
                    if not load32(v2 + 8):
                        break
                    v6 = load32(v2)
                    v1 = 0
                    while True:  # $label81
                        store32((v4 + (v3 << 2)), load32((v6 + (v1 << 2))))
                        v3 = (v3 + 1)
                        v1 = (v1 + 1)
                        if (u32((v1 + 1)) < u32(load32(v2 + 8))):
                            continue
                        break
                    break
                while True:  # $label82
                    v2 = load32(v5 + 20)
                    if not load32(v5 + 20):
                        break
                    store32((v4 + (((v7 + v31) + v9) << 2)), v3)
                    store32((v4 + (v3 << 2)), load32(v2 + 8))
                    v3 = (v3 + 1)
                    if not load32(v2 + 8):
                        break
                    v6 = load32(v2)
                    v1 = 0
                    while True:  # $label83
                        store32((v4 + (v3 << 2)), load32((v6 + (v1 << 2))))
                        v3 = (v3 + 1)
                        v1 = (v1 + 1)
                        if (u32((v1 + 1)) < u32(load32(v2 + 8))):
                            continue
                        break
                    break
                while True:  # $label84
                    v2 = load32(v5 + 24)
                    if not load32(v5 + 24):
                        break
                    v6 = load32(v2)
                    if not load32(v2):
                        break
                    store32((v4 + (((v7 + v31) + v50) << 2)), v3)
                    store32((v4 + (v3 << 2)), load32(v6 + 8))
                    v3 = (v3 + 1)
                    if not load32(v6 + 8):
                        break
                    v38 = load32(v6)
                    v1 = 0
                    while True:  # $label85
                        store32((v4 + (v3 << 2)), load32((v38 + (v1 << 2))))
                        v3 = (v3 + 1)
                        v1 = (v1 + 1)
                        if (u32((v1 + 1)) < u32(load32(v6 + 8))):
                            continue
                        break
                    break
                v1 = (v7 + v31)
                store32((v4 + (((v7 + v31) + v49) << 2)), load32(v5 + 28))
                store32((v4 + ((v1 + v48) << 2)), load32(v5 + 32))
                store32((v4 + ((v1 + v47) << 2)), load32(v5 + 36))
                store32((v4 + ((v1 + v46) << 2)), (0 if v13 else load32(v5 + 40)))
                store32((v4 + ((v1 + v45) << 2)), load32(v5 + 44))
                v6 = load32(v5 + 48)
                if load32(v5 + 48):
                    if v13:
                    else:
                    store32(0, load32(v6 + 32))
                store32((v4 + ((v1 + v43) << 2)), load32(v5 + 52))
                store32((v4 + ((v1 + v42) << 2)), load32(v5 + 60))
                store32((v4 + ((v1 + v41) << 2)), load32(v5 + 64))
                store32((v4 + ((v1 + v16) << 2)), load32(v5 + 68))
                store32((v4 + ((v1 + v20) << 2)), load32(v5 + 72))
                store32((v4 + ((v1 + v39) << 2)), load32(v5 + 76))
                store32((v4 + ((v1 + v35) << 2)), load32(v5 + 80))
                store32((v4 + ((v1 + v34) << 2)), load32(v5 + 84))
                store32((v4 + ((v1 + v33) << 2)), load32(v5 + 88))
                store32((v4 + ((v1 + v22) << 2)), (0 if v13 else load32(v5 + 92)))
                store32((v4 + ((v1 + v32) << 2)), load32(v5 + 108))
                store32((v4 + ((v1 + v17) << 2)), load32(v5 + 112))
                store32((v4 + ((v1 + v14) << 2)), load32(v5 + 116))
                store32((v4 + ((v1 + v19) << 2)), load16u(v5 + 120))
                store32((v4 + ((v1 + v30) << 2)), ((((load8u(v5 + 123) << 8) | (load8u(v5 + 124) << 16)) | (load8u(v5 + 125) << 24)) | v10))
                store32((v4 + ((v1 + v29) << 2)), load32(v5 + 126))
                store32((v4 + ((v1 + v28) << 2)), load32(v5 + 96))
                store32((v4 + ((v1 + v27) << 2)), load32(v5 + 56))
                while True:  # $label86
                    if not v2:
                        break
                    while True:  # $label87
                        v10 = load32(v2 + 12)
                        if not load32(v2 + 12):
                            break
                        store32((v4 + ((v1 + v24) << 2)), v3)
                        store32((v4 + (v3 << 2)), load32(v10 + 8))
                        v3 = (v3 + 1)
                        if not load32(v10 + 8):
                            break
                        v38 = load32(v10)
                        v6 = 0
                        while True:  # $label88
                            store32((v4 + (v3 << 2)), load32((v38 + (v6 << 2))))
                            v3 = (v3 + 1)
                            v6 = (v6 + 1)
                            if (u32((v6 + 1)) < u32(load32(v10 + 8))):
                                continue
                            break
                        break
                    while True:  # $label89
                        v10 = load32(v2 + 8)
                        if not load32(v2 + 8):
                            break
                        store32((v4 + ((v1 + v25) << 2)), v3)
                        store32((v4 + (v3 << 2)), load32(v10 + 8))
                        v3 = (v3 + 1)
                        if not load32(v10 + 8):
                            break
                        v38 = load32(v10)
                        v6 = 0
                        while True:  # $label90
                            store32((v4 + (v3 << 2)), load32((v38 + (v6 << 2))))
                            v3 = (v3 + 1)
                            v6 = (v6 + 1)
                            if (u32((v6 + 1)) < u32(load32(v10 + 8))):
                                continue
                            break
                        break
                    v2 = load32(v2 + 4)
                    if not load32(v2 + 4):
                        break
                    store32((v4 + ((v1 + v21) << 2)), v3)
                    store32((v4 + (v3 << 2)), load32(v2 + 8))
                    v3 = (v3 + 1)
                    if not load32(v2 + 8):
                        break
                    v10 = load32(v2)
                    v6 = 0
                    while True:  # $label91
                        store32((v4 + (v3 << 2)), load32((v10 + (v6 << 2))))
                        v3 = (v3 + 1)
                        v6 = (v6 + 1)
                        if (u32((v6 + 1)) < u32(load32(v2 + 8))):
                            continue
                        break
                    break
                store32((v4 + ((v1 + v15) << 2)), load32(v5 + 100))
                store32((v4 + ((v1 + v23) << 2)), load32(v5 + 104))
                store32((v4 + ((v1 + v26) << 2)), load8u(v5 + 130))
                v7 = (v7 + 1)
                break
            v8 = (v8 + 1)
            if ((v8 + 1) != v36):
                continue
            break
    v5 = load32(9687204)
    if load32(9687204):
        store32(9687204, 0)
    v5 = func26(v37)
    store32(9687204, func26(v37))
    store32(v5, v18)
    store32(v12 + 24, v37)
    store32(9147396, v18)
    v5 = (load32(v12 + 24) + 4)
    store32(9147392, (load32(v12 + 24) + 4))
    store32(v12 + 24, v5)
    v9 = load32(9687204)
    while True:  # $label93
        if not arg0:
            v5 = v9
            break
        v5 = 0
        v3 = 0
        arg0 = load32(v12 + 24)
        if load32(v12 + 24):
            v1 = -1
            while True:  # $label94
                v4 = (v1 ^ load8u((v3 + v9)))
                v1 = (((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1)
                v4 = (((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v4 = (((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v4 = (((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v4 = (((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v4 = (((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v4 = (((((((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v4 = (((((((((((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((((((((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v1 = (((((((((((((((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v3 = (v3 + 1)
                if ((v3 + 1) != arg0):
                    continue
                break
            v3 = (v1 ^ -1)
        store32(v12, v9)
        store32(v12 + 4, arg0)
        store32(v12 + 8, v3)
        # TODO: i32.div_u
        store32(load32(9142848) + 12, 10)
        break
    G.global0 = (v12 + 32)
    return v5
