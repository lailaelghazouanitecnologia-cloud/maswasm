"""
Tzar Engine - Core module (part 5).
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
# $func1010
# ----------------------------------------------------------
def func1010(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    if arg0:
        v10 = load8u(arg5)
        v13 = load8u(arg4)
        v12 = load8u(arg3)
        v14 = load8u(arg2)
        v11 = load8u(arg0)
        store8(arg6 + 3, 255)
        v11 = (((v11 * 19077) & 0xFFFFFFFF) >> 8)
        v13 = (v13 | (v10 << 16))
        v10 = (v14 | (v12 << 16))
        v12 = (((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074)
        v14 = ((((((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
        v16 = ((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
        v9 = (((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        store8(arg6 + 2, ((((((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v16) >= u32(17685)) else 0)))
        v12 = (((v12 & 0xFFFFFFFF) >> 18) & 255)
        v16 = (v11 + ((((((v12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
        v9 = ((v11 + ((((((v12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        store8(arg6, (((((v11 + ((((((v12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v16) >= u32(14234)) else 0)))
        v11 = (v11 - ((((v14 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8)))
        v12 = ((v11 - ((((v14 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        store8(arg6 + 1, (((((v11 - ((((v14 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (v11 >= -8708) else 0)))
        if arg1:
            v11 = load8u(arg1)
            store8(arg7 + 3, 255)
            v11 = (((v11 * 19077) & 0xFFFFFFFF) >> 8)
            v12 = ((v10 + (v13 * 3)) + 131074)
            v14 = (((((v10 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
            v16 = ((((v11 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v10 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            v9 = (((((v11 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v10 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg7 + 2, ((((((((v11 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v10 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v16) >= u32(17685)) else 0)))
            v12 = (((v12 & 0xFFFFFFFF) >> 18) & 255)
            v16 = (v11 + ((((((v12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
            v9 = ((v11 + ((((((v12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg7, (((((v11 + ((((((v12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v16) >= u32(14234)) else 0)))
            v11 = (v11 - ((((v14 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8)))
            v12 = ((v11 - ((((v14 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg7 + 1, (((((v11 - ((((v14 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (v11 >= -8708) else 0)))
        v16 = (arg8 - 1)
        while True:  # $label0
            if (arg8 < 3):
                v11 = v13
                v12 = v10
                break
            v11 = (v16 >> 1)
            v25 = (1 if (v11 <= 1) else (v16 >> 1))
            v14 = 1
            while True:  # $label1
                v21 = (v14 << 1)
                v18 = ((v14 << 1) - 1)
                v11 = load8u((arg0 + ((v14 << 1) - 1)))
                v12 = load8u((arg2 + v14))
                v22 = load8u((arg3 + v14))
                v17 = load8u((arg4 + v14))
                v19 = load8u((arg5 + v14))
                v26 = (v18 << 2)
                v9 = (arg6 + (v18 << 2))
                store8((arg6 + (v18 << 2)) + 3, 255)
                v15 = (((v11 * 19077) & 0xFFFFFFFF) >> 8)
                v11 = (v17 | (v19 << 16))
                v12 = (v12 | (v22 << 16))
                v22 = ((v12 | (v22 << 16)) + v13)
                v17 = (((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296)
                v22 = ((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3)
                v19 = (((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10)
                v23 = ((((((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10) & 0xFFFFFFFF) >> 1) & 255)
                v20 = ((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                v24 = (((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                store8(v9 + 2, ((((((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v24) < u32(16384)) else (255 if (u32(v20) >= u32(17685)) else 0)))
                v19 = (((v19 & 0xFFFFFFFF) >> 17) & 255)
                v20 = (((((((v19 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8) + v15)
                v24 = ((((((((v19 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8) + v15) - 14234)
                store8(v9, (((((((((((v19 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8) + v15) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v24) < u32(16384)) else (255 if (u32(v20) >= u32(14234)) else 0)))
                v9 = (v15 - ((((v19 * 13320) & 0xFFFFFFFF) >> 8) + (((v23 * 6419) & 0xFFFFFFFF) >> 8)))
                v15 = ((v15 - ((((v19 * 13320) & 0xFFFFFFFF) >> 8) + (((v23 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                store8(v9 + 1, (((((v15 - ((((v19 * 13320) & 0xFFFFFFFF) >> 8) + (((v23 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v15) < u32(16384)) else (255 if (v9 >= -8708) else 0)))
                v15 = load8u((arg0 + v21))
                v19 = (v14 << 3)
                v9 = (arg6 + (v14 << 3))
                store8((arg6 + (v14 << 3)) + 3, 255)
                v15 = (((v15 * 19077) & 0xFFFFFFFF) >> 8)
                v17 = (((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3)
                v10 = ((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12)
                v23 = (((((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 1) & 255)
                v20 = ((((v15 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                v24 = (((((v15 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                store8(v9 + 2, ((((((((v15 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v24) < u32(16384)) else (255 if (u32(v20) >= u32(17685)) else 0)))
                v10 = (((v10 & 0xFFFFFFFF) >> 17) & 255)
                v23 = (v15 - (((((((v10 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8) + (((v23 * 6419) & 0xFFFFFFFF) >> 8)))
                v20 = ((v15 - (((((((v10 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8) + (((v23 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                store8(v9 + 1, (((((v15 - (((((((v10 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8) + (((v23 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v20) < u32(16384)) else (255 if (v23 >= -8708) else 0)))
                v10 = ((((v10 * 26149) & 0xFFFFFFFF) >> 8) + v15)
                v9 = (((((v10 * 26149) & 0xFFFFFFFF) >> 8) + v15) - 14234)
                store8(v9, ((((((((v10 * 26149) & 0xFFFFFFFF) >> 8) + v15) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v10) >= u32(14234)) else 0)))
                if arg1:
                    v9 = load8u((arg1 + v18))
                    v10 = (arg7 + v26)
                    store8((arg7 + v26) + 3, 255)
                    v9 = (((v9 * 19077) & 0xFFFFFFFF) >> 8)
                    v13 = (v13 + v17)
                    v18 = ((((v13 + v17) & 0xFFFFFFFF) >> 1) & 255)
                    v15 = ((((v9 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v13 + v17) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                    v17 = (((((v9 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v13 + v17) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8(v10 + 2, ((((((((v9 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v13 + v17) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v17) < u32(16384)) else (255 if (u32(v15) >= u32(17685)) else 0)))
                    v13 = (((v13 & 0xFFFFFFFF) >> 17) & 255)
                    v15 = (v9 + ((((((v13 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8))
                    v17 = ((v9 + ((((((v13 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    store8(v10, (((((v9 + ((((((v13 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v17) < u32(16384)) else (255 if (u32(v15) >= u32(14234)) else 0)))
                    v10 = (v9 - ((((v18 * 6419) & 0xFFFFFFFF) >> 8) + (((v13 * 13320) & 0xFFFFFFFF) >> 8)))
                    v13 = ((v9 - ((((v18 * 6419) & 0xFFFFFFFF) >> 8) + (((v13 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    store8(v10 + 1, (((((v9 - ((((v18 * 6419) & 0xFFFFFFFF) >> 8) + (((v13 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (v10 >= -8708) else 0)))
                    v13 = load8u((arg1 + v21))
                    v10 = (arg7 + v19)
                    store8((arg7 + v19) + 3, 255)
                    v13 = (((v13 * 19077) & 0xFFFFFFFF) >> 8)
                    v9 = (v11 + v22)
                    v21 = ((((v11 + v22) & 0xFFFFFFFF) >> 1) & 255)
                    v18 = ((((v13 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + v22) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                    v15 = (((((v13 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + v22) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8(v10 + 2, ((((((((v13 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + v22) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v15) < u32(16384)) else (255 if (u32(v18) >= u32(17685)) else 0)))
                    v9 = (((v9 & 0xFFFFFFFF) >> 17) & 255)
                    v21 = (v13 - ((((v21 * 6419) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8)))
                    v18 = ((v13 - ((((v21 * 6419) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    store8(v10 + 1, (((((v13 - ((((v21 * 6419) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v18) < u32(16384)) else (255 if (v21 >= -8708) else 0)))
                    v10 = (v13 + (((v9 * 26149) & 0xFFFFFFFF) >> 8))
                    v13 = ((v13 + (((v9 * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    store8(v10, (((((v13 + (((v9 * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (u32(v10) >= u32(14234)) else 0)))
                v9 = (v14 != v25)
                v14 = (v14 + 1)
                v10 = v12
                v13 = v11
                if v9:
                    continue
                break
            break
        while True:  # $label2
            if (arg8 & 1):
                break
            arg2 = load8u((arg0 + v16))
            arg3 = (v16 << 2)
            arg0 = (arg6 + (v16 << 2))
            store8((arg6 + (v16 << 2)) + 3, 255)
            arg2 = (((arg2 * 19077) & 0xFFFFFFFF) >> 8)
            arg4 = ((v11 + (v12 * 3)) + 131074)
            arg5 = (((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
            arg6 = ((((arg2 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            arg8 = (((((arg2 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg0 + 2, ((((((((arg2 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(arg8) < u32(16384)) else (255 if (u32(arg6) >= u32(17685)) else 0)))
            arg4 = (((arg4 & 0xFFFFFFFF) >> 18) & 255)
            arg6 = (arg2 + ((((((arg4 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
            arg8 = ((arg2 + ((((((arg4 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg0, (((((arg2 + ((((((arg4 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg8) < u32(16384)) else (255 if (u32(arg6) >= u32(14234)) else 0)))
            arg0 = (arg2 - ((((arg5 * 6419) & 0xFFFFFFFF) >> 8) + (((arg4 * 13320) & 0xFFFFFFFF) >> 8)))
            arg2 = ((arg2 - ((((arg5 * 6419) & 0xFFFFFFFF) >> 8) + (((arg4 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg0 + 1, (((((arg2 - ((((arg5 * 6419) & 0xFFFFFFFF) >> 8) + (((arg4 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg2) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))
            if not arg1:
                break
            arg1 = load8u((arg1 + v16))
            arg0 = (arg3 + arg7)
            store8((arg3 + arg7) + 3, 255)
            arg1 = (((arg1 * 19077) & 0xFFFFFFFF) >> 8)
            arg2 = ((v12 + (v11 * 3)) + 131074)
            arg3 = (((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
            arg4 = ((((arg1 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            arg5 = (((((arg1 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg0 + 2, ((((((((arg1 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(arg5) < u32(16384)) else (255 if (u32(arg4) >= u32(17685)) else 0)))
            arg2 = (((arg2 & 0xFFFFFFFF) >> 18) & 255)
            arg4 = (arg1 + ((((((arg2 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
            arg5 = ((arg1 + ((((((arg2 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg0, (((((arg1 + ((((((arg2 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg5) < u32(16384)) else (255 if (u32(arg4) >= u32(14234)) else 0)))
            arg0 = (arg1 - ((((arg3 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8)))
            arg1 = ((arg1 - ((((arg3 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg0 + 1, (((((arg1 - ((((arg3 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg1) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))
            break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1011
# ----------------------------------------------------------
def func1011(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    if arg0:
        v10 = (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)
        v11 = (load8u(arg4) | (load8u(arg5) << 16))
        v9 = (load8u(arg2) | (load8u(arg3) << 16))
        v12 = (((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074)
        v15 = ((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
        v16 = ((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
        v14 = (((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        store8(arg6 + 1, (((((((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v14) < u32(16384)) else (240 if (u32(v16) >= u32(17685)) else 0)) | 15))
        v12 = ((v12 & 0xFFFFFFFF) >> 18)
        v16 = (v10 + (((((v12 & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
        v14 = ((v10 + (((((v12 & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        v10 = (v10 - ((((v15 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8)))
        v12 = ((v10 - ((((v15 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        store8(arg6, (((((((v10 + (((((v12 & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v14) < u32(16384)) else (240 if (u32(v16) >= u32(14234)) else 0)) & 240) | (((((v10 - ((((v15 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (u32(v12) < u32(16384)) else (15 if (v10 >= -8708) else 0))))
        if arg1:
            v10 = (((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8)
            v12 = ((v9 + (v11 * 3)) + 131074)
            v15 = (((((v9 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
            v16 = ((((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v9 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            v14 = (((((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v9 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg7 + 1, (((((((((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v9 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v14) < u32(16384)) else (240 if (u32(v16) >= u32(17685)) else 0)) | 15))
            v12 = ((v12 & 0xFFFFFFFF) >> 18)
            v16 = (v10 + (((((v12 & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            v14 = ((v10 + (((((v12 & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            v10 = (v10 - ((((v15 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8)))
            v12 = ((v10 - ((((v15 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg7, (((((((v10 + (((((v12 & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v14) < u32(16384)) else (240 if (u32(v16) >= u32(14234)) else 0)) & 240) | (((((v10 - ((((v15 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (u32(v12) < u32(16384)) else (15 if (v10 >= -8708) else 0))))
        v16 = (arg8 - 1)
        while True:  # $label0
            if (arg8 < 3):
                v10 = v11
                v12 = v9
                break
            v10 = (v16 >> 1)
            v26 = (1 if (v10 <= 1) else (v16 >> 1))
            v15 = 1
            while True:  # $label1
                v14 = (v15 << 1)
                v21 = ((v15 << 1) - 1)
                v17 = (((v15 << 1) - 1) << 1)
                v18 = (arg6 + (((v15 << 1) - 1) << 1))
                v13 = (((load8u((arg0 + v21)) * 19077) & 0xFFFFFFFF) >> 8)
                v10 = (load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16))
                v12 = (load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16))
                v23 = ((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v11)
                v22 = (((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v11) + v9)) + 524296)
                v23 = ((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v11) + v9)) + 524296) + (v23 << 1)) & 0xFFFFFFFF) >> 3)
                v19 = (((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v11) + v9)) + 524296) + (v23 << 1)) & 0xFFFFFFFF) >> 3) + v9)
                v24 = ((((((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v11) + v9)) + 524296) + (v23 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 1) & 255)
                v20 = ((((load8u((arg0 + v21)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v11) + v9)) + 524296) + (v23 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                v25 = (((((load8u((arg0 + v21)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v11) + v9)) + 524296) + (v23 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                store8((arg6 + (((v15 << 1) - 1) << 1)) + 1, (((((((((load8u((arg0 + v21)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v11) + v9)) + 524296) + (v23 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v25) < u32(16384)) else (240 if (u32(v20) >= u32(17685)) else 0)) | 15))
                v18 = ((v19 & 0xFFFFFFFF) >> 17)
                v19 = ((((((v19 & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8) + v13)
                v20 = (((((((v19 & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8) + v13) - 14234)
                v13 = (v13 - ((((v18 * 13320) & 0xFFFFFFFF) >> 8) + (((v24 * 6419) & 0xFFFFFFFF) >> 8)))
                v18 = ((v13 - ((((v18 * 13320) & 0xFFFFFFFF) >> 8) + (((v24 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                store8(v18, ((((((((((((v19 & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8) + v13) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v20) < u32(16384)) else (240 if (u32(v19) >= u32(14234)) else 0)) & 240) | (((((v13 - ((((v18 * 13320) & 0xFFFFFFFF) >> 8) + (((v24 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (u32(v18) < u32(16384)) else (15 if (v13 >= -8708) else 0))))
                v18 = (v15 << 2)
                v19 = (arg6 + (v15 << 2))
                v13 = (((load8u((arg0 + v14)) * 19077) & 0xFFFFFFFF) >> 8)
                v22 = (((v22 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3)
                v9 = ((((v22 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v12)
                v24 = (((((((v22 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 1) & 255)
                v20 = ((((load8u((arg0 + v14)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v22 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                v25 = (((((load8u((arg0 + v14)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v22 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                store8((arg6 + (v15 << 2)) + 1, (((((((((load8u((arg0 + v14)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v22 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v25) < u32(16384)) else (240 if (u32(v20) >= u32(17685)) else 0)) | 15))
                v9 = ((v9 & 0xFFFFFFFF) >> 17)
                v19 = ((((((v9 & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8) + v13)
                v20 = (((((((v9 & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8) + v13) - 14234)
                v9 = (v13 - ((((v9 * 13320) & 0xFFFFFFFF) >> 8) + (((v24 * 6419) & 0xFFFFFFFF) >> 8)))
                v13 = ((v13 - ((((v9 * 13320) & 0xFFFFFFFF) >> 8) + (((v24 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                store8(v19, ((((((((((((v9 & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8) + v13) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v20) < u32(16384)) else (240 if (u32(v19) >= u32(14234)) else 0)) & 240) | (((((v13 - ((((v9 * 13320) & 0xFFFFFFFF) >> 8) + (((v24 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (u32(v13) < u32(16384)) else (15 if (v9 >= -8708) else 0))))
                if arg1:
                    v13 = (arg7 + v17)
                    v9 = (((load8u((arg1 + v21)) * 19077) & 0xFFFFFFFF) >> 8)
                    v11 = (v11 + v22)
                    v21 = ((((v11 + v22) & 0xFFFFFFFF) >> 1) & 255)
                    v17 = ((((load8u((arg1 + v21)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + v22) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                    v22 = (((((load8u((arg1 + v21)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + v22) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8((arg7 + v17) + 1, (((((((((load8u((arg1 + v21)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + v22) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v22) < u32(16384)) else (240 if (u32(v17) >= u32(17685)) else 0)) | 15))
                    v11 = ((v11 & 0xFFFFFFFF) >> 17)
                    v13 = (v9 + (((((v11 & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                    v17 = ((v9 + (((((v11 & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    v9 = (v9 - ((((v21 * 6419) & 0xFFFFFFFF) >> 8) + (((v11 * 13320) & 0xFFFFFFFF) >> 8)))
                    v11 = ((v9 - ((((v21 * 6419) & 0xFFFFFFFF) >> 8) + (((v11 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    store8(v13, (((((((v9 + (((((v11 & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v17) < u32(16384)) else (240 if (u32(v13) >= u32(14234)) else 0)) & 240) | (((((v9 - ((((v21 * 6419) & 0xFFFFFFFF) >> 8) + (((v11 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (u32(v11) < u32(16384)) else (15 if (v9 >= -8708) else 0))))
                    v11 = (arg7 + v18)
                    v9 = (((load8u((arg1 + v14)) * 19077) & 0xFFFFFFFF) >> 8)
                    v14 = (v10 + v23)
                    v21 = ((((v10 + v23) & 0xFFFFFFFF) >> 1) & 255)
                    v13 = ((((load8u((arg1 + v14)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v10 + v23) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                    v17 = (((((load8u((arg1 + v14)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v10 + v23) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8((arg7 + v18) + 1, (((((((((load8u((arg1 + v14)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v10 + v23) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v17) < u32(16384)) else (240 if (u32(v13) >= u32(17685)) else 0)) | 15))
                    v11 = ((v14 & 0xFFFFFFFF) >> 17)
                    v14 = (v9 + (((((v14 & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                    v13 = ((v9 + (((((v14 & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    v9 = (v9 - ((((v21 * 6419) & 0xFFFFFFFF) >> 8) + (((v11 * 13320) & 0xFFFFFFFF) >> 8)))
                    v11 = ((v9 - ((((v21 * 6419) & 0xFFFFFFFF) >> 8) + (((v11 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    store8(v11, (((((((v9 + (((((v14 & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (240 if (u32(v14) >= u32(14234)) else 0)) & 240) | (((((v9 - ((((v21 * 6419) & 0xFFFFFFFF) >> 8) + (((v11 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (u32(v11) < u32(16384)) else (15 if (v9 >= -8708) else 0))))
                v14 = (v15 != v26)
                v15 = (v15 + 1)
                v9 = v12
                v11 = v10
                if v14:
                    continue
                break
            break
        while True:  # $label2
            if (arg8 & 1):
                break
            arg2 = (v16 << 1)
            arg3 = (arg6 + (v16 << 1))
            arg0 = (((load8u((arg0 + v16)) * 19077) & 0xFFFFFFFF) >> 8)
            arg4 = ((v10 + (v12 * 3)) + 131074)
            arg5 = (((((v10 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
            arg6 = ((((load8u((arg0 + v16)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v10 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            arg8 = (((((load8u((arg0 + v16)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v10 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8((arg6 + (v16 << 1)) + 1, (((((((((load8u((arg0 + v16)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v10 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(arg8) < u32(16384)) else (240 if (u32(arg6) >= u32(17685)) else 0)) | 15))
            arg3 = ((arg4 & 0xFFFFFFFF) >> 18)
            arg4 = (arg0 + (((((arg4 & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            arg6 = ((arg0 + (((((arg4 & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            arg0 = (arg0 - ((((arg5 * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8)))
            arg3 = ((arg0 - ((((arg5 * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg3, (((((((arg0 + (((((arg4 & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg6) < u32(16384)) else (240 if (u32(arg4) >= u32(14234)) else 0)) & 240) | (((((arg0 - ((((arg5 * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (u32(arg3) < u32(16384)) else (15 if (arg0 >= -8708) else 0))))
            if not arg1:
                break
            arg2 = (arg2 + arg7)
            arg0 = (((load8u((arg1 + v16)) * 19077) & 0xFFFFFFFF) >> 8)
            arg1 = ((v12 + (v10 * 3)) + 131074)
            arg3 = (((((v12 + (v10 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
            arg4 = ((((load8u((arg1 + v16)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v12 + (v10 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            arg5 = (((((load8u((arg1 + v16)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v12 + (v10 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8((arg2 + arg7) + 1, (((((((((load8u((arg1 + v16)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v12 + (v10 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(arg5) < u32(16384)) else (240 if (u32(arg4) >= u32(17685)) else 0)) | 15))
            arg1 = ((arg1 & 0xFFFFFFFF) >> 18)
            arg2 = (arg0 + (((((arg1 & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            arg4 = ((arg0 + (((((arg1 & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            arg0 = (arg0 - ((((arg3 * 6419) & 0xFFFFFFFF) >> 8) + (((arg1 * 13320) & 0xFFFFFFFF) >> 8)))
            arg1 = ((arg0 - ((((arg3 * 6419) & 0xFFFFFFFF) >> 8) + (((arg1 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg2, (((((((arg0 + (((((arg1 & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg4) < u32(16384)) else (240 if (u32(arg2) >= u32(14234)) else 0)) & 240) | (((((arg0 - ((((arg3 * 6419) & 0xFFFFFFFF) >> 8) + (((arg1 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (u32(arg1) < u32(16384)) else (15 if (arg0 >= -8708) else 0))))
            break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1012
# ----------------------------------------------------------
def func1012(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    if arg0:
        v10 = (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)
        v12 = (load8u(arg4) | (load8u(arg5) << 16))
        v9 = (load8u(arg2) | (load8u(arg3) << 16))
        v11 = (((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074)
        v15 = (((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18)
        v17 = ((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
        v13 = (((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        store8(arg6, ((((((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (u32(v17) >= u32(14234)) else 0)))
        v11 = (((v11 & 0xFFFFFFFF) >> 2) & 255)
        v17 = (v10 + ((((((v11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
        v13 = ((v10 + ((((((v11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        store8(arg6 + 2, (((((v10 + ((((((v11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (u32(v17) >= u32(17685)) else 0)))
        v10 = (v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8)))
        v11 = ((v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        store8(arg6 + 1, (((((v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (255 if (v10 >= -8708) else 0)))
        if arg1:
            v10 = (((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8)
            v11 = ((v9 + (v12 * 3)) + 131074)
            v15 = ((((v9 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
            v17 = ((((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v9 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            v13 = (((((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v9 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg7, ((((((((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v9 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (u32(v17) >= u32(14234)) else 0)))
            v11 = (((v11 & 0xFFFFFFFF) >> 2) & 255)
            v17 = (v10 + ((((((v11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            v13 = ((v10 + ((((((v11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg7 + 2, (((((v10 + ((((((v11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (u32(v17) >= u32(17685)) else 0)))
            v10 = (v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8)))
            v11 = ((v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg7 + 1, (((((v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (255 if (v10 >= -8708) else 0)))
        v17 = (arg8 - 1)
        while True:  # $label0
            if (arg8 < 3):
                v10 = v12
                v11 = v9
                break
            v10 = (v17 >> 1)
            v26 = (1 if (v10 <= 1) else (v17 >> 1))
            v15 = 1
            while True:  # $label1
                v13 = (v15 << 1)
                v18 = ((v15 << 1) - 1)
                v20 = (((v15 << 1) - 1) * 3)
                v14 = (arg6 + (((v15 << 1) - 1) * 3))
                v16 = (((load8u((arg0 + v18)) * 19077) & 0xFFFFFFFF) >> 8)
                v10 = (load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16))
                v11 = (load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16))
                v24 = ((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12)
                v25 = (((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296)
                v24 = ((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296) + (v24 << 1)) & 0xFFFFFFFF) >> 3)
                v21 = (((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296) + (v24 << 1)) & 0xFFFFFFFF) >> 3) + v9)
                v22 = (((((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296) + (v24 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17)
                v19 = ((((load8u((arg0 + v18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296) + (v24 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                v23 = (((((load8u((arg0 + v18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296) + (v24 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                store8((arg6 + (((v15 << 1) - 1) * 3)), ((((((((load8u((arg0 + v18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296) + (v24 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v23) < u32(16384)) else (255 if (u32(v19) >= u32(14234)) else 0)))
                v21 = (((v21 & 0xFFFFFFFF) >> 1) & 255)
                v19 = (((((((v21 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8) + v16)
                v23 = ((((((((v21 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8) + v16) - 17685)
                store8(v14 + 2, (((((((((((v21 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8) + v16) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v23) < u32(16384)) else (255 if (u32(v19) >= u32(17685)) else 0)))
                v14 = (v16 - ((((v22 * 13320) & 0xFFFFFFFF) >> 8) + (((v21 * 6419) & 0xFFFFFFFF) >> 8)))
                v16 = ((v16 - ((((v22 * 13320) & 0xFFFFFFFF) >> 8) + (((v21 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                store8(v14 + 1, (((((v16 - ((((v22 * 13320) & 0xFFFFFFFF) >> 8) + (((v21 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v16) < u32(16384)) else (255 if (v14 >= -8708) else 0)))
                v21 = (v15 * 6)
                v14 = (arg6 + (v15 * 6))
                v16 = (((load8u((arg0 + v13)) * 19077) & 0xFFFFFFFF) >> 8)
                v25 = (((v25 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3)
                v9 = ((((v25 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v11)
                v22 = (((((((v25 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v11) & 0xFFFFFFFF) >> 1) & 255)
                v19 = ((((load8u((arg0 + v13)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v25 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v11) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                v23 = (((((load8u((arg0 + v13)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v25 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v11) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                store8((arg6 + (v15 * 6)) + 2, ((((((((load8u((arg0 + v13)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v25 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v11) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v23) < u32(16384)) else (255 if (u32(v19) >= u32(17685)) else 0)))
                v9 = ((v9 & 0xFFFFFFFF) >> 17)
                v22 = (v16 - ((((((v9 & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + (((v22 * 6419) & 0xFFFFFFFF) >> 8)))
                v19 = ((v16 - ((((((v9 & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + (((v22 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                store8(v14 + 1, (((((v16 - ((((((v9 & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + (((v22 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v19) < u32(16384)) else (255 if (v22 >= -8708) else 0)))
                v9 = ((((v9 * 26149) & 0xFFFFFFFF) >> 8) + v16)
                v14 = (((((v9 * 26149) & 0xFFFFFFFF) >> 8) + v16) - 14234)
                store8(v14, ((((((((v9 * 26149) & 0xFFFFFFFF) >> 8) + v16) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v14) < u32(16384)) else (255 if (u32(v9) >= u32(14234)) else 0)))
                if arg1:
                    v9 = (arg7 + v20)
                    v18 = (((load8u((arg1 + v18)) * 19077) & 0xFFFFFFFF) >> 8)
                    v12 = (v12 + v25)
                    v14 = (((v12 + v25) & 0xFFFFFFFF) >> 17)
                    v16 = ((((load8u((arg1 + v18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v12 + v25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                    v20 = (((((load8u((arg1 + v18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v12 + v25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    store8((arg7 + v20), ((((((((load8u((arg1 + v18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v12 + v25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v20) < u32(16384)) else (255 if (u32(v16) >= u32(14234)) else 0)))
                    v12 = (((v12 & 0xFFFFFFFF) >> 1) & 255)
                    v16 = (v18 + ((((((v12 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                    v20 = ((v18 + ((((((v12 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8(v9 + 2, (((((v18 + ((((((v12 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v20) < u32(16384)) else (255 if (u32(v16) >= u32(17685)) else 0)))
                    v9 = (v18 - ((((v12 * 6419) & 0xFFFFFFFF) >> 8) + (((v14 * 13320) & 0xFFFFFFFF) >> 8)))
                    v12 = ((v18 - ((((v12 * 6419) & 0xFFFFFFFF) >> 8) + (((v14 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    store8(v9 + 1, (((((v18 - ((((v12 * 6419) & 0xFFFFFFFF) >> 8) + (((v14 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (v9 >= -8708) else 0)))
                    v9 = (arg7 + v21)
                    v12 = (((load8u((arg1 + v13)) * 19077) & 0xFFFFFFFF) >> 8)
                    v13 = (v10 + v24)
                    v18 = ((((v10 + v24) & 0xFFFFFFFF) >> 1) & 255)
                    v14 = ((((load8u((arg1 + v13)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v10 + v24) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                    v16 = (((((load8u((arg1 + v13)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v10 + v24) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8((arg7 + v21) + 2, ((((((((load8u((arg1 + v13)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v10 + v24) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v16) < u32(16384)) else (255 if (u32(v14) >= u32(17685)) else 0)))
                    v13 = ((v13 & 0xFFFFFFFF) >> 17)
                    v18 = (v12 - ((((v18 * 6419) & 0xFFFFFFFF) >> 8) + (((((v13 & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8)))
                    v14 = ((v12 - ((((v18 * 6419) & 0xFFFFFFFF) >> 8) + (((((v13 & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    store8(v9 + 1, (((((v12 - ((((v18 * 6419) & 0xFFFFFFFF) >> 8) + (((((v13 & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v14) < u32(16384)) else (255 if (v18 >= -8708) else 0)))
                    v9 = (v12 + (((v13 * 26149) & 0xFFFFFFFF) >> 8))
                    v12 = ((v12 + (((v13 * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    store8(v9, (((((v12 + (((v13 * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (u32(v9) >= u32(14234)) else 0)))
                v13 = (v15 != v26)
                v15 = (v15 + 1)
                v9 = v11
                v12 = v10
                if v13:
                    continue
                break
            break
        while True:  # $label2
            if (arg8 & 1):
                break
            arg3 = (v17 * 3)
            arg2 = (arg6 + (v17 * 3))
            arg0 = (((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8)
            arg4 = ((v10 + (v11 * 3)) + 131074)
            arg5 = ((((v10 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
            arg6 = ((((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v10 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            arg8 = (((((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v10 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8((arg6 + (v17 * 3)), ((((((((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v10 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg8) < u32(16384)) else (255 if (u32(arg6) >= u32(14234)) else 0)))
            arg4 = (((arg4 & 0xFFFFFFFF) >> 2) & 255)
            arg6 = (arg0 + ((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            arg8 = ((arg0 + ((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg2 + 2, (((((arg0 + ((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(arg8) < u32(16384)) else (255 if (u32(arg6) >= u32(17685)) else 0)))
            arg0 = (arg0 - ((((arg4 * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8)))
            arg2 = ((arg0 - ((((arg4 * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg2 + 1, (((((arg0 - ((((arg4 * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg2) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))
            if not arg1:
                break
            arg0 = (arg3 + arg7)
            arg1 = (((load8u((arg1 + v17)) * 19077) & 0xFFFFFFFF) >> 8)
            arg2 = ((v11 + (v10 * 3)) + 131074)
            arg3 = ((((v11 + (v10 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
            arg4 = ((((load8u((arg1 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + (v10 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            arg5 = (((((load8u((arg1 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + (v10 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8((arg3 + arg7), ((((((((load8u((arg1 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + (v10 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg5) < u32(16384)) else (255 if (u32(arg4) >= u32(14234)) else 0)))
            arg2 = (((arg2 & 0xFFFFFFFF) >> 2) & 255)
            arg4 = (arg1 + ((((((arg2 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            arg5 = ((arg1 + ((((((arg2 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg0 + 2, (((((arg1 + ((((((arg2 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(arg5) < u32(16384)) else (255 if (u32(arg4) >= u32(17685)) else 0)))
            arg0 = (arg1 - ((((arg2 * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8)))
            arg1 = ((arg1 - ((((arg2 * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg0 + 1, (((((arg1 - ((((arg2 * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg1) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))
            break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1013
# ----------------------------------------------------------
def func1013(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    if arg0:
        v11 = (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)
        v13 = (load8u(arg4) | (load8u(arg5) << 16))
        v9 = (load8u(arg2) | (load8u(arg3) << 16))
        v12 = (((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074)
        v10 = (((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18)
        v16 = ((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
        v17 = (((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        v12 = (((v12 & 0xFFFFFFFF) >> 2) & 255)
        v10 = (v11 - (((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v10 * 13320) & 0xFFFFFFFF) >> 8)))
        v16 = ((v11 - (((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v10 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        v10 = (((((v11 - (((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v10 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v16) < u32(16384)) else (255 if (v10 >= -8708) else 0))
        store8(arg6, ((((((((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v17) < u32(16384)) else (248 if (u32(v16) >= u32(14234)) else 0)) & 248) | (((((((v11 - (((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v10 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v16) < u32(16384)) else (255 if (v10 >= -8708) else 0)) & 0xFFFFFFFF) >> 5)))
        v11 = (v11 + (((v12 * 33050) & 0xFFFFFFFF) >> 8))
        v12 = ((v11 + (((v12 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        store8(arg6 + 1, (((v10 << 3) & 224) | (((((v11 + (((v12 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 9) if (u32(v12) < u32(16384)) else (31 if (u32(v11) >= u32(17685)) else 0))))
        if arg1:
            v11 = (((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8)
            v12 = ((v9 + (v13 * 3)) + 131074)
            v10 = ((((v9 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
            v16 = ((((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v9 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            v17 = (((((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v9 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            v12 = (((v12 & 0xFFFFFFFF) >> 2) & 255)
            v10 = (v11 - (((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v10 * 13320) & 0xFFFFFFFF) >> 8)))
            v16 = ((v11 - (((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v10 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            v10 = (((((v11 - (((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v10 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v16) < u32(16384)) else (255 if (v10 >= -8708) else 0))
            store8(arg7, ((((((((((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v9 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v17) < u32(16384)) else (248 if (u32(v16) >= u32(14234)) else 0)) & 248) | (((((((v11 - (((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v10 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v16) < u32(16384)) else (255 if (v10 >= -8708) else 0)) & 0xFFFFFFFF) >> 5)))
            v11 = (v11 + (((v12 * 33050) & 0xFFFFFFFF) >> 8))
            v12 = ((v11 + (((v12 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg7 + 1, (((v10 << 3) & 224) | (((((v11 + (((v12 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 9) if (u32(v12) < u32(16384)) else (31 if (u32(v11) >= u32(17685)) else 0))))
        v16 = (arg8 - 1)
        while True:  # $label0
            if (arg8 < 3):
                v11 = v13
                v12 = v9
                break
            v11 = (v16 >> 1)
            v26 = (1 if (v11 <= 1) else (v16 >> 1))
            v10 = 1
            while True:  # $label1
                v17 = (v10 << 1)
                v15 = ((v10 << 1) - 1)
                v18 = (((v10 << 1) - 1) << 1)
                v22 = (arg6 + (((v10 << 1) - 1) << 1))
                v14 = (((load8u((arg0 + v15)) * 19077) & 0xFFFFFFFF) >> 8)
                v11 = (load8u((arg4 + v10)) | (load8u((arg5 + v10)) << 16))
                v12 = (load8u((arg2 + v10)) | (load8u((arg3 + v10)) << 16))
                v25 = ((load8u((arg2 + v10)) | (load8u((arg3 + v10)) << 16)) + v13)
                v23 = (((load8u((arg4 + v10)) | (load8u((arg5 + v10)) << 16)) + (((load8u((arg2 + v10)) | (load8u((arg3 + v10)) << 16)) + v13) + v9)) + 524296)
                v25 = ((((((load8u((arg4 + v10)) | (load8u((arg5 + v10)) << 16)) + (((load8u((arg2 + v10)) | (load8u((arg3 + v10)) << 16)) + v13) + v9)) + 524296) + (v25 << 1)) & 0xFFFFFFFF) >> 3)
                v24 = (((((((load8u((arg4 + v10)) | (load8u((arg5 + v10)) << 16)) + (((load8u((arg2 + v10)) | (load8u((arg3 + v10)) << 16)) + v13) + v9)) + 524296) + (v25 << 1)) & 0xFFFFFFFF) >> 3) + v9)
                v19 = (((((((((load8u((arg4 + v10)) | (load8u((arg5 + v10)) << 16)) + (((load8u((arg2 + v10)) | (load8u((arg3 + v10)) << 16)) + v13) + v9)) + 524296) + (v25 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17)
                v24 = (((v24 & 0xFFFFFFFF) >> 1) & 255)
                v20 = ((((load8u((arg0 + v15)) * 19077) & 0xFFFFFFFF) >> 8) - (((((((((((((load8u((arg4 + v10)) | (load8u((arg5 + v10)) << 16)) + (((load8u((arg2 + v10)) | (load8u((arg3 + v10)) << 16)) + v13) + v9)) + 524296) + (v25 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((v24 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8)))
                v21 = (((((load8u((arg0 + v15)) * 19077) & 0xFFFFFFFF) >> 8) - (((((((((((((load8u((arg4 + v10)) | (load8u((arg5 + v10)) << 16)) + (((load8u((arg2 + v10)) | (load8u((arg3 + v10)) << 16)) + v13) + v9)) + 524296) + (v25 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((v24 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                v20 = ((((((((load8u((arg0 + v15)) * 19077) & 0xFFFFFFFF) >> 8) - (((((((((((((load8u((arg4 + v10)) | (load8u((arg5 + v10)) << 16)) + (((load8u((arg2 + v10)) | (load8u((arg3 + v10)) << 16)) + v13) + v9)) + 524296) + (v25 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((v24 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v21) < u32(16384)) else (255 if (v20 >= -8708) else 0))
                v19 = ((((v19 * 26149) & 0xFFFFFFFF) >> 8) + v14)
                v21 = (((((v19 * 26149) & 0xFFFFFFFF) >> 8) + v14) - 14234)
                store8((arg6 + (((v10 << 1) - 1) << 1)), (((((((((((load8u((arg0 + v15)) * 19077) & 0xFFFFFFFF) >> 8) - (((((((((((((load8u((arg4 + v10)) | (load8u((arg5 + v10)) << 16)) + (((load8u((arg2 + v10)) | (load8u((arg3 + v10)) << 16)) + v13) + v9)) + 524296) + (v25 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((v24 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v21) < u32(16384)) else (255 if (v20 >= -8708) else 0)) & 0xFFFFFFFF) >> 5) | (((((((((v19 * 26149) & 0xFFFFFFFF) >> 8) + v14) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v21) < u32(16384)) else (248 if (u32(v19) >= u32(14234)) else 0)) & 248)))
                v14 = ((((v24 * 33050) & 0xFFFFFFFF) >> 8) + v14)
                v22 = (((((v24 * 33050) & 0xFFFFFFFF) >> 8) + v14) - 17685)
                store8(v22 + 1, (((v20 << 3) & 224) | ((((((((v24 * 33050) & 0xFFFFFFFF) >> 8) + v14) - 17685) & 0xFFFFFFFF) >> 9) if (u32(v22) < u32(16384)) else (31 if (u32(v14) >= u32(17685)) else 0))))
                v22 = (v10 << 2)
                v24 = (arg6 + (v10 << 2))
                v14 = (((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8)
                v23 = (((v23 + ((v9 + v11) << 1)) & 0xFFFFFFFF) >> 3)
                v9 = ((((v23 + ((v9 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12)
                v19 = ((((((v23 + ((v9 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 17)
                v9 = (((v9 & 0xFFFFFFFF) >> 1) & 255)
                v20 = ((((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8) - ((((((((((v23 + ((v9 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8)))
                v21 = (((((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8) - ((((((((((v23 + ((v9 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                v20 = ((((((((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8) - ((((((((((v23 + ((v9 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v21) < u32(16384)) else (255 if (v20 >= -8708) else 0))
                v19 = ((((v19 * 26149) & 0xFFFFFFFF) >> 8) + v14)
                v21 = (((((v19 * 26149) & 0xFFFFFFFF) >> 8) + v14) - 14234)
                store8((arg6 + (v10 << 2)), (((((((((((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8) - ((((((((((v23 + ((v9 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v21) < u32(16384)) else (255 if (v20 >= -8708) else 0)) & 0xFFFFFFFF) >> 5) | (((((((((v19 * 26149) & 0xFFFFFFFF) >> 8) + v14) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v21) < u32(16384)) else (248 if (u32(v19) >= u32(14234)) else 0)) & 248)))
                v9 = ((((v9 * 33050) & 0xFFFFFFFF) >> 8) + v14)
                v14 = (((((v9 * 33050) & 0xFFFFFFFF) >> 8) + v14) - 17685)
                store8(v24 + 1, (((v20 << 3) & 224) | ((((((((v9 * 33050) & 0xFFFFFFFF) >> 8) + v14) - 17685) & 0xFFFFFFFF) >> 9) if (u32(v14) < u32(16384)) else (31 if (u32(v9) >= u32(17685)) else 0))))
                if arg1:
                    v14 = (arg7 + v18)
                    v9 = (((load8u((arg1 + v15)) * 19077) & 0xFFFFFFFF) >> 8)
                    v13 = (v13 + v23)
                    v15 = (((v13 + v23) & 0xFFFFFFFF) >> 17)
                    v18 = ((((load8u((arg1 + v15)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v13 + v23) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                    v23 = (((((load8u((arg1 + v15)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v13 + v23) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    v13 = (((v13 & 0xFFFFFFFF) >> 1) & 255)
                    v15 = (v9 - (((((((v13 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8)))
                    v18 = ((v9 - (((((((v13 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    v15 = (((((v9 - (((((((v13 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v18) < u32(16384)) else (255 if (v15 >= -8708) else 0))
                    store8((arg7 + v18), ((((((((((load8u((arg1 + v15)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v13 + v23) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v23) < u32(16384)) else (248 if (u32(v18) >= u32(14234)) else 0)) & 248) | (((((((v9 - (((((((v13 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v18) < u32(16384)) else (255 if (v15 >= -8708) else 0)) & 0xFFFFFFFF) >> 5)))
                    v9 = (v9 + (((v13 * 33050) & 0xFFFFFFFF) >> 8))
                    v13 = ((v9 + (((v13 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8(v14 + 1, (((v15 << 3) & 224) | (((((v9 + (((v13 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 9) if (u32(v13) < u32(16384)) else (31 if (u32(v9) >= u32(17685)) else 0))))
                    v13 = (arg7 + v22)
                    v9 = (((load8u((arg1 + v17)) * 19077) & 0xFFFFFFFF) >> 8)
                    v17 = (v11 + v25)
                    v15 = (((v11 + v25) & 0xFFFFFFFF) >> 17)
                    v14 = ((((load8u((arg1 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v11 + v25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                    v18 = (((((load8u((arg1 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v11 + v25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    v17 = (((v17 & 0xFFFFFFFF) >> 1) & 255)
                    v15 = (v9 - (((((((v17 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8)))
                    v14 = ((v9 - (((((((v17 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    v15 = (((((v9 - (((((((v17 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v14) < u32(16384)) else (255 if (v15 >= -8708) else 0))
                    store8((arg7 + v22), ((((((((((load8u((arg1 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v11 + v25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v18) < u32(16384)) else (248 if (u32(v14) >= u32(14234)) else 0)) & 248) | (((((((v9 - (((((((v17 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v14) < u32(16384)) else (255 if (v15 >= -8708) else 0)) & 0xFFFFFFFF) >> 5)))
                    v9 = (v9 + (((v17 * 33050) & 0xFFFFFFFF) >> 8))
                    v13 = ((v9 + (((v17 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8(v13 + 1, (((v15 << 3) & 224) | (((((v9 + (((v17 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 9) if (u32(v13) < u32(16384)) else (31 if (u32(v9) >= u32(17685)) else 0))))
                v17 = (v10 != v26)
                v10 = (v10 + 1)
                v9 = v12
                v13 = v11
                if v17:
                    continue
                break
            break
        while True:  # $label2
            if (arg8 & 1):
                break
            arg2 = (v16 << 1)
            arg3 = (arg6 + (v16 << 1))
            arg0 = (((load8u((arg0 + v16)) * 19077) & 0xFFFFFFFF) >> 8)
            arg4 = ((v11 + (v12 * 3)) + 131074)
            arg5 = ((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
            arg6 = ((((load8u((arg0 + v16)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            arg8 = (((((load8u((arg0 + v16)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            arg4 = (((arg4 & 0xFFFFFFFF) >> 2) & 255)
            arg5 = (arg0 - (((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8)))
            arg6 = ((arg0 - (((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            arg5 = (((((arg0 - (((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg6) < u32(16384)) else (255 if (arg5 >= -8708) else 0))
            store8((arg6 + (v16 << 1)), ((((((((((load8u((arg0 + v16)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg8) < u32(16384)) else (248 if (u32(arg6) >= u32(14234)) else 0)) & 248) | (((((((arg0 - (((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg6) < u32(16384)) else (255 if (arg5 >= -8708) else 0)) & 0xFFFFFFFF) >> 5)))
            arg0 = (arg0 + (((arg4 * 33050) & 0xFFFFFFFF) >> 8))
            arg3 = ((arg0 + (((arg4 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg3 + 1, (((arg5 << 3) & 224) | (((((arg0 + (((arg4 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 9) if (u32(arg3) < u32(16384)) else (31 if (u32(arg0) >= u32(17685)) else 0))))
            if not arg1:
                break
            arg2 = (arg2 + arg7)
            arg0 = (((load8u((arg1 + v16)) * 19077) & 0xFFFFFFFF) >> 8)
            arg1 = ((v12 + (v11 * 3)) + 131074)
            arg3 = ((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
            arg4 = ((((load8u((arg1 + v16)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            arg5 = (((((load8u((arg1 + v16)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            arg1 = (((arg1 & 0xFFFFFFFF) >> 2) & 255)
            arg3 = (arg0 - (((((((arg1 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8)))
            arg4 = ((arg0 - (((((((arg1 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            arg3 = (((((arg0 - (((((((arg1 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg4) < u32(16384)) else (255 if (arg3 >= -8708) else 0))
            store8((arg2 + arg7), ((((((((((load8u((arg1 + v16)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg5) < u32(16384)) else (248 if (u32(arg4) >= u32(14234)) else 0)) & 248) | (((((((arg0 - (((((((arg1 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg4) < u32(16384)) else (255 if (arg3 >= -8708) else 0)) & 0xFFFFFFFF) >> 5)))
            arg0 = (arg0 + (((arg1 * 33050) & 0xFFFFFFFF) >> 8))
            arg1 = ((arg0 + (((arg1 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg2 + 1, (((arg3 << 3) & 224) | (((((arg0 + (((arg1 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 9) if (u32(arg1) < u32(16384)) else (31 if (u32(arg0) >= u32(17685)) else 0))))
            break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1014
# ----------------------------------------------------------
def func1014(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    if arg0:
        v10 = load8u(arg5)
        v13 = load8u(arg4)
        v12 = load8u(arg3)
        v14 = load8u(arg2)
        v11 = load8u(arg0)
        store8(arg6 + 3, 255)
        v11 = (((v11 * 19077) & 0xFFFFFFFF) >> 8)
        v13 = (v13 | (v10 << 16))
        v10 = (v14 | (v12 << 16))
        v12 = (((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074)
        v14 = ((((((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255)
        v16 = ((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
        v9 = (((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        store8(arg6 + 2, ((((((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v16) >= u32(14234)) else 0)))
        v12 = (((v12 & 0xFFFFFFFF) >> 2) & 255)
        v16 = (v11 + ((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
        v9 = ((v11 + ((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        store8(arg6, (((((v11 + ((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v16) >= u32(17685)) else 0)))
        v11 = (v11 - ((((v12 * 6419) & 0xFFFFFFFF) >> 8) + (((v14 * 13320) & 0xFFFFFFFF) >> 8)))
        v12 = ((v11 - ((((v12 * 6419) & 0xFFFFFFFF) >> 8) + (((v14 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        store8(arg6 + 1, (((((v11 - ((((v12 * 6419) & 0xFFFFFFFF) >> 8) + (((v14 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (v11 >= -8708) else 0)))
        if arg1:
            v11 = load8u(arg1)
            store8(arg7 + 3, 255)
            v11 = (((v11 * 19077) & 0xFFFFFFFF) >> 8)
            v12 = ((v10 + (v13 * 3)) + 131074)
            v14 = (((((v10 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255)
            v16 = ((((v11 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v10 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
            v9 = (((((v11 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v10 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg7 + 2, ((((((((v11 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v10 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v16) >= u32(14234)) else 0)))
            v12 = (((v12 & 0xFFFFFFFF) >> 2) & 255)
            v16 = (v11 + ((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            v9 = ((v11 + ((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg7, (((((v11 + ((((((v12 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v16) >= u32(17685)) else 0)))
            v11 = (v11 - ((((v12 * 6419) & 0xFFFFFFFF) >> 8) + (((v14 * 13320) & 0xFFFFFFFF) >> 8)))
            v12 = ((v11 - ((((v12 * 6419) & 0xFFFFFFFF) >> 8) + (((v14 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg7 + 1, (((((v11 - ((((v12 * 6419) & 0xFFFFFFFF) >> 8) + (((v14 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (v11 >= -8708) else 0)))
        v16 = (arg8 - 1)
        while True:  # $label0
            if (arg8 < 3):
                v11 = v13
                v12 = v10
                break
            v11 = (v16 >> 1)
            v25 = (1 if (v11 <= 1) else (v16 >> 1))
            v14 = 1
            while True:  # $label1
                v21 = (v14 << 1)
                v18 = ((v14 << 1) - 1)
                v11 = load8u((arg0 + ((v14 << 1) - 1)))
                v12 = load8u((arg2 + v14))
                v22 = load8u((arg3 + v14))
                v17 = load8u((arg4 + v14))
                v19 = load8u((arg5 + v14))
                v26 = (v18 << 2)
                v9 = (arg6 + (v18 << 2))
                store8((arg6 + (v18 << 2)) + 3, 255)
                v15 = (((v11 * 19077) & 0xFFFFFFFF) >> 8)
                v11 = (v17 | (v19 << 16))
                v12 = (v12 | (v22 << 16))
                v22 = ((v12 | (v22 << 16)) + v13)
                v17 = (((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296)
                v22 = ((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3)
                v19 = (((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10)
                v23 = ((((((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10) & 0xFFFFFFFF) >> 17) & 255)
                v20 = ((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10) & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8))
                v24 = (((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10) & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                store8(v9 + 2, ((((((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10) & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v24) < u32(16384)) else (255 if (u32(v20) >= u32(14234)) else 0)))
                v19 = (((v19 & 0xFFFFFFFF) >> 1) & 255)
                v20 = (((((((v19 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8) + v15)
                v24 = ((((((((v19 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8) + v15) - 17685)
                store8(v9, (((((((((((v19 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8) + v15) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v24) < u32(16384)) else (255 if (u32(v20) >= u32(17685)) else 0)))
                v9 = (v15 - ((((v23 * 13320) & 0xFFFFFFFF) >> 8) + (((v19 * 6419) & 0xFFFFFFFF) >> 8)))
                v15 = ((v15 - ((((v23 * 13320) & 0xFFFFFFFF) >> 8) + (((v19 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                store8(v9 + 1, (((((v15 - ((((v23 * 13320) & 0xFFFFFFFF) >> 8) + (((v19 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v15) < u32(16384)) else (255 if (v9 >= -8708) else 0)))
                v15 = load8u((arg0 + v21))
                v19 = (v14 << 3)
                v9 = (arg6 + (v14 << 3))
                store8((arg6 + (v14 << 3)) + 3, 255)
                v15 = (((v15 * 19077) & 0xFFFFFFFF) >> 8)
                v17 = (((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3)
                v10 = ((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12)
                v23 = (((((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 17) & 255)
                v20 = ((((v15 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8))
                v24 = (((((v15 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                store8(v9 + 2, ((((((((v15 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v24) < u32(16384)) else (255 if (u32(v20) >= u32(14234)) else 0)))
                v10 = (((v10 & 0xFFFFFFFF) >> 1) & 255)
                v23 = (v15 - ((((v23 * 13320) & 0xFFFFFFFF) >> 8) + ((((((v10 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8)))
                v20 = ((v15 - ((((v23 * 13320) & 0xFFFFFFFF) >> 8) + ((((((v10 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                store8(v9 + 1, (((((v15 - ((((v23 * 13320) & 0xFFFFFFFF) >> 8) + ((((((v10 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v20) < u32(16384)) else (255 if (v23 >= -8708) else 0)))
                v10 = ((((v10 * 33050) & 0xFFFFFFFF) >> 8) + v15)
                v9 = (((((v10 * 33050) & 0xFFFFFFFF) >> 8) + v15) - 17685)
                store8(v9, ((((((((v10 * 33050) & 0xFFFFFFFF) >> 8) + v15) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v10) >= u32(17685)) else 0)))
                if arg1:
                    v9 = load8u((arg1 + v18))
                    v10 = (arg7 + v26)
                    store8((arg7 + v26) + 3, 255)
                    v9 = (((v9 * 19077) & 0xFFFFFFFF) >> 8)
                    v13 = (v13 + v17)
                    v18 = ((((v13 + v17) & 0xFFFFFFFF) >> 17) & 255)
                    v15 = ((((v9 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v13 + v17) & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8))
                    v17 = (((((v9 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v13 + v17) & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    store8(v10 + 2, ((((((((v9 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v13 + v17) & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v17) < u32(16384)) else (255 if (u32(v15) >= u32(14234)) else 0)))
                    v13 = (((v13 & 0xFFFFFFFF) >> 1) & 255)
                    v15 = (v9 + ((((((v13 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                    v17 = ((v9 + ((((((v13 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8(v10, (((((v9 + ((((((v13 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v17) < u32(16384)) else (255 if (u32(v15) >= u32(17685)) else 0)))
                    v10 = (v9 - ((((v13 * 6419) & 0xFFFFFFFF) >> 8) + (((v18 * 13320) & 0xFFFFFFFF) >> 8)))
                    v13 = ((v9 - ((((v13 * 6419) & 0xFFFFFFFF) >> 8) + (((v18 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    store8(v10 + 1, (((((v9 - ((((v13 * 6419) & 0xFFFFFFFF) >> 8) + (((v18 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (v10 >= -8708) else 0)))
                    v13 = load8u((arg1 + v21))
                    v10 = (arg7 + v19)
                    store8((arg7 + v19) + 3, 255)
                    v13 = (((v13 * 19077) & 0xFFFFFFFF) >> 8)
                    v9 = (v11 + v22)
                    v21 = ((((v11 + v22) & 0xFFFFFFFF) >> 17) & 255)
                    v18 = ((((v13 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + v22) & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8))
                    v15 = (((((v13 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + v22) & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    store8(v10 + 2, ((((((((v13 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + v22) & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v15) < u32(16384)) else (255 if (u32(v18) >= u32(14234)) else 0)))
                    v9 = (((v9 & 0xFFFFFFFF) >> 1) & 255)
                    v21 = (v13 - (((((((v9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v21 * 13320) & 0xFFFFFFFF) >> 8)))
                    v18 = ((v13 - (((((((v9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v21 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    store8(v10 + 1, (((((v13 - (((((((v9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v21 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v18) < u32(16384)) else (255 if (v21 >= -8708) else 0)))
                    v10 = (v13 + (((v9 * 33050) & 0xFFFFFFFF) >> 8))
                    v13 = ((v13 + (((v9 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8(v10, (((((v13 + (((v9 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (u32(v10) >= u32(17685)) else 0)))
                v9 = (v14 != v25)
                v14 = (v14 + 1)
                v10 = v12
                v13 = v11
                if v9:
                    continue
                break
            break
        while True:  # $label2
            if (arg8 & 1):
                break
            arg2 = load8u((arg0 + v16))
            arg3 = (v16 << 2)
            arg0 = (arg6 + (v16 << 2))
            store8((arg6 + (v16 << 2)) + 3, 255)
            arg2 = (((arg2 * 19077) & 0xFFFFFFFF) >> 8)
            arg4 = ((v11 + (v12 * 3)) + 131074)
            arg5 = (((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255)
            arg6 = ((((arg2 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
            arg8 = (((((arg2 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg0 + 2, ((((((((arg2 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg8) < u32(16384)) else (255 if (u32(arg6) >= u32(14234)) else 0)))
            arg4 = (((arg4 & 0xFFFFFFFF) >> 2) & 255)
            arg6 = (arg2 + ((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            arg8 = ((arg2 + ((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg0, (((((arg2 + ((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(arg8) < u32(16384)) else (255 if (u32(arg6) >= u32(17685)) else 0)))
            arg0 = (arg2 - ((((arg4 * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8)))
            arg2 = ((arg2 - ((((arg4 * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg0 + 1, (((((arg2 - ((((arg4 * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg2) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))
            if not arg1:
                break
            arg1 = load8u((arg1 + v16))
            arg0 = (arg3 + arg7)
            store8((arg3 + arg7) + 3, 255)
            arg1 = (((arg1 * 19077) & 0xFFFFFFFF) >> 8)
            arg2 = ((v12 + (v11 * 3)) + 131074)
            arg3 = (((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255)
            arg4 = ((((arg1 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
            arg5 = (((((arg1 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg0 + 2, ((((((((arg1 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg5) < u32(16384)) else (255 if (u32(arg4) >= u32(14234)) else 0)))
            arg2 = (((arg2 & 0xFFFFFFFF) >> 2) & 255)
            arg4 = (arg1 + ((((((arg2 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            arg5 = ((arg1 + ((((((arg2 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg0, (((((arg1 + ((((((arg2 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(arg5) < u32(16384)) else (255 if (u32(arg4) >= u32(17685)) else 0)))
            arg0 = (arg1 - ((((arg2 * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8)))
            arg1 = ((arg1 - ((((arg2 * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg0 + 1, (((((arg1 - ((((arg2 * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg1) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))
            break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1015
# ----------------------------------------------------------
def func1015(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    if arg0:
        v10 = (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)
        v12 = (load8u(arg4) | (load8u(arg5) << 16))
        v9 = (load8u(arg2) | (load8u(arg3) << 16))
        v11 = (((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074)
        v15 = (((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18)
        v17 = ((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
        v13 = (((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        store8(arg6 + 2, ((((((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((load8u(arg4) | (load8u(arg5) << 16)) + ((load8u(arg2) | (load8u(arg3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (u32(v17) >= u32(14234)) else 0)))
        v11 = (((v11 & 0xFFFFFFFF) >> 2) & 255)
        v17 = (v10 + ((((((v11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
        v13 = ((v10 + ((((((v11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        store8(arg6, (((((v10 + ((((((v11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (u32(v17) >= u32(17685)) else 0)))
        v10 = (v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8)))
        v11 = ((v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        store8(arg6 + 1, (((((v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (255 if (v10 >= -8708) else 0)))
        if arg1:
            v10 = (((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8)
            v11 = ((v9 + (v12 * 3)) + 131074)
            v15 = ((((v9 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
            v17 = ((((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v9 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            v13 = (((((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v9 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg7 + 2, ((((((((load8u(arg1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v9 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (u32(v17) >= u32(14234)) else 0)))
            v11 = (((v11 & 0xFFFFFFFF) >> 2) & 255)
            v17 = (v10 + ((((((v11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            v13 = ((v10 + ((((((v11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg7, (((((v10 + ((((((v11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (u32(v17) >= u32(17685)) else 0)))
            v10 = (v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8)))
            v11 = ((v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg7 + 1, (((((v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (255 if (v10 >= -8708) else 0)))
        v17 = (arg8 - 1)
        while True:  # $label0
            if (arg8 < 3):
                v10 = v12
                v11 = v9
                break
            v10 = (v17 >> 1)
            v26 = (1 if (v10 <= 1) else (v17 >> 1))
            v15 = 1
            while True:  # $label1
                v13 = (v15 << 1)
                v18 = ((v15 << 1) - 1)
                v20 = (((v15 << 1) - 1) * 3)
                v14 = (arg6 + (((v15 << 1) - 1) * 3))
                v16 = (((load8u((arg0 + v18)) * 19077) & 0xFFFFFFFF) >> 8)
                v10 = (load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16))
                v11 = (load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16))
                v24 = ((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12)
                v25 = (((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296)
                v24 = ((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296) + (v24 << 1)) & 0xFFFFFFFF) >> 3)
                v21 = (((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296) + (v24 << 1)) & 0xFFFFFFFF) >> 3) + v9)
                v22 = (((((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296) + (v24 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17)
                v19 = ((((load8u((arg0 + v18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296) + (v24 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                v23 = (((((load8u((arg0 + v18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296) + (v24 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                store8((arg6 + (((v15 << 1) - 1) * 3)) + 2, ((((((((load8u((arg0 + v18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((((load8u((arg4 + v15)) | (load8u((arg5 + v15)) << 16)) + (((load8u((arg2 + v15)) | (load8u((arg3 + v15)) << 16)) + v12) + v9)) + 524296) + (v24 << 1)) & 0xFFFFFFFF) >> 3) + v9) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v23) < u32(16384)) else (255 if (u32(v19) >= u32(14234)) else 0)))
                v21 = (((v21 & 0xFFFFFFFF) >> 1) & 255)
                v19 = (((((((v21 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8) + v16)
                v23 = ((((((((v21 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8) + v16) - 17685)
                store8(v14, (((((((((((v21 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8) + v16) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v23) < u32(16384)) else (255 if (u32(v19) >= u32(17685)) else 0)))
                v14 = (v16 - ((((v22 * 13320) & 0xFFFFFFFF) >> 8) + (((v21 * 6419) & 0xFFFFFFFF) >> 8)))
                v16 = ((v16 - ((((v22 * 13320) & 0xFFFFFFFF) >> 8) + (((v21 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                store8(v14 + 1, (((((v16 - ((((v22 * 13320) & 0xFFFFFFFF) >> 8) + (((v21 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v16) < u32(16384)) else (255 if (v14 >= -8708) else 0)))
                v21 = (v15 * 6)
                v14 = (arg6 + (v15 * 6))
                v16 = (((load8u((arg0 + v13)) * 19077) & 0xFFFFFFFF) >> 8)
                v25 = (((v25 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3)
                v9 = ((((v25 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v11)
                v22 = ((((((v25 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v11) & 0xFFFFFFFF) >> 17)
                v19 = ((((load8u((arg0 + v13)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((((v25 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v11) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                v23 = (((((load8u((arg0 + v13)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((((v25 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v11) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                store8((arg6 + (v15 * 6)) + 2, ((((((((load8u((arg0 + v13)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((((v25 + ((v9 + v10) << 1)) & 0xFFFFFFFF) >> 3) + v11) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v23) < u32(16384)) else (255 if (u32(v19) >= u32(14234)) else 0)))
                v9 = (((v9 & 0xFFFFFFFF) >> 1) & 255)
                v22 = (v16 - ((((v22 * 13320) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8)))
                v19 = ((v16 - ((((v22 * 13320) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                store8(v14 + 1, (((((v16 - ((((v22 * 13320) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v19) < u32(16384)) else (255 if (v22 >= -8708) else 0)))
                v9 = ((((v9 * 33050) & 0xFFFFFFFF) >> 8) + v16)
                v14 = (((((v9 * 33050) & 0xFFFFFFFF) >> 8) + v16) - 17685)
                store8(v14, ((((((((v9 * 33050) & 0xFFFFFFFF) >> 8) + v16) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v14) < u32(16384)) else (255 if (u32(v9) >= u32(17685)) else 0)))
                if arg1:
                    v9 = (arg7 + v20)
                    v18 = (((load8u((arg1 + v18)) * 19077) & 0xFFFFFFFF) >> 8)
                    v12 = (v12 + v25)
                    v14 = (((v12 + v25) & 0xFFFFFFFF) >> 17)
                    v16 = ((((load8u((arg1 + v18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v12 + v25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                    v20 = (((((load8u((arg1 + v18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v12 + v25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    store8((arg7 + v20) + 2, ((((((((load8u((arg1 + v18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v12 + v25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v20) < u32(16384)) else (255 if (u32(v16) >= u32(14234)) else 0)))
                    v12 = (((v12 & 0xFFFFFFFF) >> 1) & 255)
                    v16 = (v18 + ((((((v12 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                    v20 = ((v18 + ((((((v12 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8(v9, (((((v18 + ((((((v12 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v20) < u32(16384)) else (255 if (u32(v16) >= u32(17685)) else 0)))
                    v9 = (v18 - ((((v12 * 6419) & 0xFFFFFFFF) >> 8) + (((v14 * 13320) & 0xFFFFFFFF) >> 8)))
                    v12 = ((v18 - ((((v12 * 6419) & 0xFFFFFFFF) >> 8) + (((v14 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    store8(v9 + 1, (((((v18 - ((((v12 * 6419) & 0xFFFFFFFF) >> 8) + (((v14 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (v9 >= -8708) else 0)))
                    v9 = (arg7 + v21)
                    v12 = (((load8u((arg1 + v13)) * 19077) & 0xFFFFFFFF) >> 8)
                    v13 = (v10 + v24)
                    v18 = (((v10 + v24) & 0xFFFFFFFF) >> 17)
                    v14 = ((((load8u((arg1 + v13)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v10 + v24) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                    v16 = (((((load8u((arg1 + v13)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v10 + v24) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    store8((arg7 + v21) + 2, ((((((((load8u((arg1 + v13)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((v10 + v24) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v16) < u32(16384)) else (255 if (u32(v14) >= u32(14234)) else 0)))
                    v13 = (((v13 & 0xFFFFFFFF) >> 1) & 255)
                    v18 = (v12 - (((((((v13 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v18 * 13320) & 0xFFFFFFFF) >> 8)))
                    v14 = ((v12 - (((((((v13 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v18 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    store8(v9 + 1, (((((v12 - (((((((v13 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((v18 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v14) < u32(16384)) else (255 if (v18 >= -8708) else 0)))
                    v9 = (v12 + (((v13 * 33050) & 0xFFFFFFFF) >> 8))
                    v12 = ((v12 + (((v13 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8(v9, (((((v12 + (((v13 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (u32(v9) >= u32(17685)) else 0)))
                v13 = (v15 != v26)
                v15 = (v15 + 1)
                v9 = v11
                v12 = v10
                if v13:
                    continue
                break
            break
        while True:  # $label2
            if (arg8 & 1):
                break
            arg3 = (v17 * 3)
            arg2 = (arg6 + (v17 * 3))
            arg0 = (((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8)
            arg4 = ((v10 + (v11 * 3)) + 131074)
            arg5 = ((((v10 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
            arg6 = ((((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v10 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            arg8 = (((((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v10 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8((arg6 + (v17 * 3)) + 2, ((((((((load8u((arg0 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v10 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg8) < u32(16384)) else (255 if (u32(arg6) >= u32(14234)) else 0)))
            arg4 = (((arg4 & 0xFFFFFFFF) >> 2) & 255)
            arg6 = (arg0 + ((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            arg8 = ((arg0 + ((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg2, (((((arg0 + ((((((arg4 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(arg8) < u32(16384)) else (255 if (u32(arg6) >= u32(17685)) else 0)))
            arg0 = (arg0 - ((((arg4 * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8)))
            arg2 = ((arg0 - ((((arg4 * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg2 + 1, (((((arg0 - ((((arg4 * 6419) & 0xFFFFFFFF) >> 8) + (((arg5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg2) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))
            if not arg1:
                break
            arg0 = (arg3 + arg7)
            arg1 = (((load8u((arg1 + v17)) * 19077) & 0xFFFFFFFF) >> 8)
            arg2 = ((v11 + (v10 * 3)) + 131074)
            arg3 = ((((v11 + (v10 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
            arg4 = ((((load8u((arg1 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + (v10 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            arg5 = (((((load8u((arg1 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + (v10 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8((arg3 + arg7) + 2, ((((((((load8u((arg1 + v17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + (v10 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg5) < u32(16384)) else (255 if (u32(arg4) >= u32(14234)) else 0)))
            arg2 = (((arg2 & 0xFFFFFFFF) >> 2) & 255)
            arg4 = (arg1 + ((((((arg2 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            arg5 = ((arg1 + ((((((arg2 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg0, (((((arg1 + ((((((arg2 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(arg5) < u32(16384)) else (255 if (u32(arg4) >= u32(17685)) else 0)))
            arg0 = (arg1 - ((((arg2 * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8)))
            arg1 = ((arg1 - ((((arg2 * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg0 + 1, (((((arg1 - ((((arg2 * 6419) & 0xFFFFFFFF) >> 8) + (((arg3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg1) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))
            break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1016
# ----------------------------------------------------------
def func1016(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    if arg0:
        v10 = load8u(arg5)
        v13 = load8u(arg4)
        v12 = load8u(arg3)
        v14 = load8u(arg2)
        v11 = load8u(arg0)
        store8(arg6, 255)
        v11 = (((v11 * 19077) & 0xFFFFFFFF) >> 8)
        v13 = (v13 | (v10 << 16))
        v10 = (v14 | (v12 << 16))
        v12 = (((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074)
        v14 = ((((((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
        v16 = ((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
        v9 = (((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        store8(arg6 + 3, ((((((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((v13 | (v10 << 16)) + ((v14 | (v12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v16) >= u32(17685)) else 0)))
        v12 = (((v12 & 0xFFFFFFFF) >> 18) & 255)
        v16 = (v11 + ((((((v12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
        v9 = ((v11 + ((((((v12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        store8(arg6 + 1, (((((v11 + ((((((v12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v16) >= u32(14234)) else 0)))
        v11 = (v11 - ((((v14 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8)))
        v12 = ((v11 - ((((v14 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        store8(arg6 + 2, (((((v11 - ((((v14 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (v11 >= -8708) else 0)))
        if arg1:
            v11 = load8u(arg1)
            store8(arg7, 255)
            v11 = (((v11 * 19077) & 0xFFFFFFFF) >> 8)
            v12 = ((v10 + (v13 * 3)) + 131074)
            v14 = (((((v10 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
            v16 = ((((v11 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v10 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            v9 = (((((v11 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v10 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg7 + 3, ((((((((v11 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v10 + (v13 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v16) >= u32(17685)) else 0)))
            v12 = (((v12 & 0xFFFFFFFF) >> 18) & 255)
            v16 = (v11 + ((((((v12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
            v9 = ((v11 + ((((((v12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg7 + 1, (((((v11 + ((((((v12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v16) >= u32(14234)) else 0)))
            v11 = (v11 - ((((v14 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8)))
            v12 = ((v11 - ((((v14 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg7 + 2, (((((v11 - ((((v14 * 6419) & 0xFFFFFFFF) >> 8) + (((v12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (v11 >= -8708) else 0)))
        v16 = (arg8 - 1)
        while True:  # $label0
            if (arg8 < 3):
                v11 = v13
                v12 = v10
                break
            v11 = (v16 >> 1)
            v25 = (1 if (v11 <= 1) else (v16 >> 1))
            v14 = 1
            while True:  # $label1
                v21 = (v14 << 1)
                v18 = ((v14 << 1) - 1)
                v11 = load8u((arg0 + ((v14 << 1) - 1)))
                v12 = load8u((arg2 + v14))
                v22 = load8u((arg3 + v14))
                v17 = load8u((arg4 + v14))
                v19 = load8u((arg5 + v14))
                v26 = (v18 << 2)
                v9 = (arg6 + (v18 << 2))
                store8((arg6 + (v18 << 2)), 255)
                v15 = (((v11 * 19077) & 0xFFFFFFFF) >> 8)
                v11 = (v17 | (v19 << 16))
                v12 = (v12 | (v22 << 16))
                v22 = ((v12 | (v22 << 16)) + v13)
                v17 = (((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296)
                v22 = ((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3)
                v19 = (((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10)
                v23 = ((((((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10) & 0xFFFFFFFF) >> 1) & 255)
                v20 = ((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                v24 = (((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                store8(v9 + 3, ((((((((v11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((v17 | (v19 << 16)) + (((v12 | (v22 << 16)) + v13) + v10)) + 524296) + (v22 << 1)) & 0xFFFFFFFF) >> 3) + v10) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v24) < u32(16384)) else (255 if (u32(v20) >= u32(17685)) else 0)))
                v19 = (((v19 & 0xFFFFFFFF) >> 17) & 255)
                v20 = (((((((v19 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8) + v15)
                v24 = ((((((((v19 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8) + v15) - 14234)
                store8(v9 + 1, (((((((((((v19 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8) + v15) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v24) < u32(16384)) else (255 if (u32(v20) >= u32(14234)) else 0)))
                v9 = (v15 - ((((v19 * 13320) & 0xFFFFFFFF) >> 8) + (((v23 * 6419) & 0xFFFFFFFF) >> 8)))
                v15 = ((v15 - ((((v19 * 13320) & 0xFFFFFFFF) >> 8) + (((v23 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                store8(v9 + 2, (((((v15 - ((((v19 * 13320) & 0xFFFFFFFF) >> 8) + (((v23 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v15) < u32(16384)) else (255 if (v9 >= -8708) else 0)))
                v15 = load8u((arg0 + v21))
                v19 = (v14 << 3)
                v9 = (arg6 + (v14 << 3))
                store8((arg6 + (v14 << 3)), 255)
                v15 = (((v15 * 19077) & 0xFFFFFFFF) >> 8)
                v17 = (((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3)
                v10 = ((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12)
                v23 = (((((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 1) & 255)
                v20 = ((((v15 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                v24 = (((((v15 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                store8(v9 + 3, ((((((((v15 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((v17 + ((v10 + v11) << 1)) & 0xFFFFFFFF) >> 3) + v12) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v24) < u32(16384)) else (255 if (u32(v20) >= u32(17685)) else 0)))
                v10 = (((v10 & 0xFFFFFFFF) >> 17) & 255)
                v23 = (v15 - (((((((v10 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8) + (((v23 * 6419) & 0xFFFFFFFF) >> 8)))
                v20 = ((v15 - (((((((v10 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8) + (((v23 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
                store8(v9 + 2, (((((v15 - (((((((v10 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8) + (((v23 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v20) < u32(16384)) else (255 if (v23 >= -8708) else 0)))
                v10 = ((((v10 * 26149) & 0xFFFFFFFF) >> 8) + v15)
                v9 = (((((v10 * 26149) & 0xFFFFFFFF) >> 8) + v15) - 14234)
                store8(v9 + 1, ((((((((v10 * 26149) & 0xFFFFFFFF) >> 8) + v15) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v10) >= u32(14234)) else 0)))
                if arg1:
                    v9 = load8u((arg1 + v18))
                    v10 = (arg7 + v26)
                    store8((arg7 + v26), 255)
                    v9 = (((v9 * 19077) & 0xFFFFFFFF) >> 8)
                    v13 = (v13 + v17)
                    v18 = ((((v13 + v17) & 0xFFFFFFFF) >> 1) & 255)
                    v15 = ((((v9 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v13 + v17) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                    v17 = (((((v9 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v13 + v17) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8(v10 + 3, ((((((((v9 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v13 + v17) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v17) < u32(16384)) else (255 if (u32(v15) >= u32(17685)) else 0)))
                    v13 = (((v13 & 0xFFFFFFFF) >> 17) & 255)
                    v15 = (v9 + ((((((v13 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8))
                    v17 = ((v9 + ((((((v13 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    store8(v10 + 1, (((((v9 + ((((((v13 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v17) < u32(16384)) else (255 if (u32(v15) >= u32(14234)) else 0)))
                    v10 = (v9 - ((((v18 * 6419) & 0xFFFFFFFF) >> 8) + (((v13 * 13320) & 0xFFFFFFFF) >> 8)))
                    v13 = ((v9 - ((((v18 * 6419) & 0xFFFFFFFF) >> 8) + (((v13 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    store8(v10 + 2, (((((v9 - ((((v18 * 6419) & 0xFFFFFFFF) >> 8) + (((v13 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (v10 >= -8708) else 0)))
                    v13 = load8u((arg1 + v21))
                    v10 = (arg7 + v19)
                    store8((arg7 + v19), 255)
                    v13 = (((v13 * 19077) & 0xFFFFFFFF) >> 8)
                    v9 = (v11 + v22)
                    v21 = ((((v11 + v22) & 0xFFFFFFFF) >> 1) & 255)
                    v18 = ((((v13 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + v22) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                    v15 = (((((v13 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + v22) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                    store8(v10 + 3, ((((((((v13 * 19077) & 0xFFFFFFFF) >> 8) + (((((((v11 + v22) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v15) < u32(16384)) else (255 if (u32(v18) >= u32(17685)) else 0)))
                    v9 = (((v9 & 0xFFFFFFFF) >> 17) & 255)
                    v21 = (v13 - ((((v21 * 6419) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8)))
                    v18 = ((v13 - ((((v21 * 6419) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                    store8(v10 + 2, (((((v13 - ((((v21 * 6419) & 0xFFFFFFFF) >> 8) + ((((((v9 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v18) < u32(16384)) else (255 if (v21 >= -8708) else 0)))
                    v10 = (v13 + (((v9 * 26149) & 0xFFFFFFFF) >> 8))
                    v13 = ((v13 + (((v9 * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                    store8(v10 + 1, (((((v13 + (((v9 * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v13) < u32(16384)) else (255 if (u32(v10) >= u32(14234)) else 0)))
                v9 = (v14 != v25)
                v14 = (v14 + 1)
                v10 = v12
                v13 = v11
                if v9:
                    continue
                break
            break
        while True:  # $label2
            if (arg8 & 1):
                break
            arg2 = load8u((arg0 + v16))
            arg3 = (v16 << 2)
            arg0 = (arg6 + (v16 << 2))
            store8((arg6 + (v16 << 2)), 255)
            arg2 = (((arg2 * 19077) & 0xFFFFFFFF) >> 8)
            arg4 = ((v11 + (v12 * 3)) + 131074)
            arg5 = (((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
            arg6 = ((((arg2 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            arg8 = (((((arg2 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg0 + 3, ((((((((arg2 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v11 + (v12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(arg8) < u32(16384)) else (255 if (u32(arg6) >= u32(17685)) else 0)))
            arg4 = (((arg4 & 0xFFFFFFFF) >> 18) & 255)
            arg6 = (arg2 + ((((((arg4 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
            arg8 = ((arg2 + ((((((arg4 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg0 + 1, (((((arg2 + ((((((arg4 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg8) < u32(16384)) else (255 if (u32(arg6) >= u32(14234)) else 0)))
            arg0 = (arg2 - ((((arg5 * 6419) & 0xFFFFFFFF) >> 8) + (((arg4 * 13320) & 0xFFFFFFFF) >> 8)))
            arg2 = ((arg2 - ((((arg5 * 6419) & 0xFFFFFFFF) >> 8) + (((arg4 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg0 + 2, (((((arg2 - ((((arg5 * 6419) & 0xFFFFFFFF) >> 8) + (((arg4 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg2) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))
            if not arg1:
                break
            arg1 = load8u((arg1 + v16))
            arg0 = (arg3 + arg7)
            store8((arg3 + arg7), 255)
            arg1 = (((arg1 * 19077) & 0xFFFFFFFF) >> 8)
            arg2 = ((v12 + (v11 * 3)) + 131074)
            arg3 = (((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
            arg4 = ((((arg1 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            arg5 = (((((arg1 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg0 + 3, ((((((((arg1 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((v12 + (v11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(arg5) < u32(16384)) else (255 if (u32(arg4) >= u32(17685)) else 0)))
            arg2 = (((arg2 & 0xFFFFFFFF) >> 18) & 255)
            arg4 = (arg1 + ((((((arg2 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
            arg5 = ((arg1 + ((((((arg2 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg0 + 1, (((((arg1 + ((((((arg2 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg5) < u32(16384)) else (255 if (u32(arg4) >= u32(14234)) else 0)))
            arg0 = (arg1 - ((((arg3 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8)))
            arg1 = ((arg1 - ((((arg3 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg0 + 2, (((((arg1 - ((((arg3 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg1) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))
            break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1020
# ----------------------------------------------------------
def func1020(arg0, arg1):
    v3 = load16s(arg0)
    v6 = load16s(arg0 + 24)
    v4 = (load16s(arg0) - load16s(arg0 + 24))
    v2 = load16s(arg0 + 8)
    v7 = load16s(arg0 + 16)
    v11 = (load16s(arg0 + 8) - load16s(arg0 + 16))
    v8 = (((load16s(arg0) - load16s(arg0 + 24)) - (load16s(arg0 + 8) - load16s(arg0 + 16))) + 3)
    v5 = load16s(arg0 + 6)
    v9 = load16s(arg0 + 30)
    v12 = (load16s(arg0 + 6) - load16s(arg0 + 30))
    v13 = load16s(arg0 + 14)
    v14 = load16s(arg0 + 22)
    v18 = (load16s(arg0 + 14) - load16s(arg0 + 22))
    v10 = ((load16s(arg0 + 6) - load16s(arg0 + 30)) - (load16s(arg0 + 14) - load16s(arg0 + 22)))
    v15 = ((((load16s(arg0) - load16s(arg0 + 24)) - (load16s(arg0 + 8) - load16s(arg0 + 16))) + 3) - ((load16s(arg0 + 6) - load16s(arg0 + 30)) - (load16s(arg0 + 14) - load16s(arg0 + 22))))
    v16 = load16s(arg0 + 2)
    v17 = load16s(arg0 + 26)
    v19 = (load16s(arg0 + 2) - load16s(arg0 + 26))
    v20 = load16s(arg0 + 10)
    v21 = load16s(arg0 + 18)
    v22 = (load16s(arg0 + 10) - load16s(arg0 + 18))
    v23 = ((load16s(arg0 + 2) - load16s(arg0 + 26)) - (load16s(arg0 + 10) - load16s(arg0 + 18)))
    v24 = load16s(arg0 + 4)
    v25 = load16s(arg0 + 28)
    v26 = (load16s(arg0 + 4) - load16s(arg0 + 28))
    v27 = load16s(arg0 + 12)
    arg0 = load16s(arg0 + 20)
    v28 = (load16s(arg0 + 12) - load16s(arg0 + 20))
    v29 = ((load16s(arg0 + 4) - load16s(arg0 + 28)) - (load16s(arg0 + 12) - load16s(arg0 + 20)))
    v30 = (((load16s(arg0 + 2) - load16s(arg0 + 26)) - (load16s(arg0 + 10) - load16s(arg0 + 18))) - ((load16s(arg0 + 4) - load16s(arg0 + 28)) - (load16s(arg0 + 12) - load16s(arg0 + 20))))
    store16(arg1 + 480, (((((((load16s(arg0) - load16s(arg0 + 24)) - (load16s(arg0 + 8) - load16s(arg0 + 16))) + 3) - ((load16s(arg0 + 6) - load16s(arg0 + 30)) - (load16s(arg0 + 14) - load16s(arg0 + 22)))) - (((load16s(arg0 + 2) - load16s(arg0 + 26)) - (load16s(arg0 + 10) - load16s(arg0 + 18))) - ((load16s(arg0 + 4) - load16s(arg0 + 28)) - (load16s(arg0 + 12) - load16s(arg0 + 20))))) & 0xFFFFFFFF) >> 3))
    v8 = (v8 + v10)
    v10 = (v23 + v29)
    store16(arg1 + 448, ((((v8 + v10) - (v23 + v29)) & 0xFFFFFFFF) >> 3))
    store16(arg1 + 416, (((v15 + v30) & 0xFFFFFFFF) >> 3))
    store16(arg1 + 384, (((v8 + v10) & 0xFFFFFFFF) >> 3))
    v3 = (v3 + v6)
    v6 = (v2 + v7)
    v2 = (((v3 + v6) - (v2 + v7)) + 3)
    v7 = (v5 + v9)
    v8 = (v13 + v14)
    v5 = ((v5 + v9) - (v13 + v14))
    v9 = ((((v3 + v6) - (v2 + v7)) + 3) - ((v5 + v9) - (v13 + v14)))
    v13 = (v16 + v17)
    v14 = (v20 + v21)
    v10 = ((v16 + v17) - (v20 + v21))
    v15 = (v24 + v25)
    arg0 = (arg0 + v27)
    v16 = ((v24 + v25) - (arg0 + v27))
    v17 = (((v16 + v17) - (v20 + v21)) - ((v24 + v25) - (arg0 + v27)))
    store16(arg1 + 352, (((((((v3 + v6) - (v2 + v7)) + 3) - ((v5 + v9) - (v13 + v14))) - (((v16 + v17) - (v20 + v21)) - ((v24 + v25) - (arg0 + v27)))) & 0xFFFFFFFF) >> 3))
    v2 = (v2 + v5)
    v5 = (v10 + v16)
    store16(arg1 + 320, ((((v2 + v5) - (v10 + v16)) & 0xFFFFFFFF) >> 3))
    store16(arg1 + 288, (((v9 + v17) & 0xFFFFFFFF) >> 3))
    store16(arg1 + 256, (((v2 + v5) & 0xFFFFFFFF) >> 3))
    v4 = ((v4 + v11) + 3)
    v2 = (v12 + v18)
    v11 = (((v4 + v11) + 3) - (v12 + v18))
    v5 = (v19 + v22)
    v9 = (v26 + v28)
    v12 = ((v19 + v22) - (v26 + v28))
    store16(arg1 + 224, ((((((v4 + v11) + 3) - (v12 + v18)) - ((v19 + v22) - (v26 + v28))) & 0xFFFFFFFF) >> 3))
    v4 = (v2 + v4)
    v2 = (v5 + v9)
    store16(arg1 + 192, ((((v2 + v4) - (v5 + v9)) & 0xFFFFFFFF) >> 3))
    store16(arg1 + 160, (((v11 + v12) & 0xFFFFFFFF) >> 3))
    store16(arg1 + 128, (((v2 + v4) & 0xFFFFFFFF) >> 3))
    v3 = ((v3 + v6) + 3)
    v6 = (v7 + v8)
    v4 = (((v3 + v6) + 3) - (v7 + v8))
    v2 = (v13 + v14)
    arg0 = (arg0 + v15)
    v7 = ((v13 + v14) - (arg0 + v15))
    store16(arg1 + 96, ((((((v3 + v6) + 3) - (v7 + v8)) - ((v13 + v14) - (arg0 + v15))) & 0xFFFFFFFF) >> 3))
    v3 = (v3 + v6)
    arg0 = (arg0 + v2)
    store16(arg1 + 64, ((((v3 + v6) - (arg0 + v2)) & 0xFFFFFFFF) >> 3))
    store16(arg1 + 32, (((v4 + v7) & 0xFFFFFFFF) >> 3))
    store16(arg1, (((arg0 + v3) & 0xFFFFFFFF) >> 3))

# ----------------------------------------------------------
# $func1022
# ----------------------------------------------------------
def func1022(arg0, arg1, arg2):
    func459(arg0, arg1)
    if arg2:
        func459((arg0 + 32), (arg1 + 4))

# ----------------------------------------------------------
# $func1023
# ----------------------------------------------------------
def func1023(arg0, arg1):
    arg0 = ((load16s(arg0) + 4) >> 3)
    v2 = (((load16s(arg0) + 4) >> 3) + load8u(arg1))
    v2 = ((((load16s(arg0) + 4) >> 3) + load8u(arg1)) if (v2 > 0) else 0)
    store8(arg1, (255 if (v2 >= 255) else ((((load16s(arg0) + 4) >> 3) + load8u(arg1)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 1))
    v2 = ((arg0 + load8u(arg1 + 1)) if (v2 > 0) else 0)
    store8(arg1 + 1, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 1)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 2))
    v2 = ((arg0 + load8u(arg1 + 2)) if (v2 > 0) else 0)
    store8(arg1 + 2, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 2)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 3))
    v2 = ((arg0 + load8u(arg1 + 3)) if (v2 > 0) else 0)
    store8(arg1 + 3, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 3)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 32))
    v2 = ((arg0 + load8u(arg1 + 32)) if (v2 > 0) else 0)
    store8(arg1 + 32, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 32)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 33))
    v2 = ((arg0 + load8u(arg1 + 33)) if (v2 > 0) else 0)
    store8(arg1 + 33, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 33)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 34))
    v2 = ((arg0 + load8u(arg1 + 34)) if (v2 > 0) else 0)
    store8(arg1 + 34, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 34)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 35))
    v2 = ((arg0 + load8u(arg1 + 35)) if (v2 > 0) else 0)
    store8(arg1 + 35, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 35)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 64))
    v2 = ((arg0 + load8u(arg1 + 64)) if (v2 > 0) else 0)
    store8(arg1 + 64, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 64)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 65))
    v2 = ((arg0 + load8u(arg1 + 65)) if (v2 > 0) else 0)
    store8(arg1 + 65, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 65)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 66))
    v2 = ((arg0 + load8u(arg1 + 66)) if (v2 > 0) else 0)
    store8(arg1 + 66, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 66)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 67))
    v2 = ((arg0 + load8u(arg1 + 67)) if (v2 > 0) else 0)
    store8(arg1 + 67, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 67)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 96))
    v2 = ((arg0 + load8u(arg1 + 96)) if (v2 > 0) else 0)
    store8(arg1 + 96, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 96)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 97))
    v2 = ((arg0 + load8u(arg1 + 97)) if (v2 > 0) else 0)
    store8(arg1 + 97, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 97)) if (v2 > 0) else 0)))
    v2 = (arg0 + load8u(arg1 + 98))
    v2 = ((arg0 + load8u(arg1 + 98)) if (v2 > 0) else 0)
    store8(arg1 + 98, (255 if (v2 >= 255) else ((arg0 + load8u(arg1 + 98)) if (v2 > 0) else 0)))
    arg0 = (arg0 + load8u(arg1 + 99))
    arg0 = ((arg0 + load8u(arg1 + 99)) if (arg0 > 0) else 0)
    store8(arg1 + 99, (255 if (arg0 >= 255) else ((arg0 + load8u(arg1 + 99)) if (arg0 > 0) else 0)))

# ----------------------------------------------------------
# $func1024
# ----------------------------------------------------------
def func1024(arg0, arg1):
    if load16u(arg0):
    if load16u(arg0 + 32):
    if load16u(arg0 + 64):
    if load16u(arg0 + 96):

# ----------------------------------------------------------
# $func1025
# ----------------------------------------------------------
def func1025(arg0, arg1):
    v4 = load16s(arg0 + 2)
    v5 = (((load16s(arg0 + 2) * 20091) >> 16) + v4)
    v3 = load16s(arg0 + 8)
    v7 = ((load16s(arg0 + 8) * 35468) >> 16)
    v6 = (load16s(arg0) + 4)
    v2 = (((load16s(arg0 + 8) * 35468) >> 16) + (load16s(arg0) + 4))
    arg0 = (load8u(arg1 + 32) + (((((load16s(arg0 + 2) * 20091) >> 16) + v4) + (((load16s(arg0 + 8) * 35468) >> 16) + (load16s(arg0) + 4))) >> 3))
    arg0 = ((load8u(arg1 + 32) + (((((load16s(arg0 + 2) * 20091) >> 16) + v4) + (((load16s(arg0 + 8) * 35468) >> 16) + (load16s(arg0) + 4))) >> 3)) if (arg0 > 0) else 0)
    store8(arg1 + 32, (255 if (arg0 >= 255) else ((load8u(arg1 + 32) + (((((load16s(arg0 + 2) * 20091) >> 16) + v4) + (((load16s(arg0 + 8) * 35468) >> 16) + (load16s(arg0) + 4))) >> 3)) if (arg0 > 0) else 0)))
    arg0 = ((v4 * 35468) >> 16)
    v4 = (load8u(arg1 + 33) + ((v2 + ((v4 * 35468) >> 16)) >> 3))
    v4 = ((load8u(arg1 + 33) + ((v2 + ((v4 * 35468) >> 16)) >> 3)) if (v4 > 0) else 0)
    store8(arg1 + 33, (255 if (v4 >= 255) else ((load8u(arg1 + 33) + ((v2 + ((v4 * 35468) >> 16)) >> 3)) if (v4 > 0) else 0)))
    v4 = (load8u(arg1 + 34) + ((v2 - arg0) >> 3))
    v4 = ((load8u(arg1 + 34) + ((v2 - arg0) >> 3)) if (v4 > 0) else 0)
    store8(arg1 + 34, (255 if (v4 >= 255) else ((load8u(arg1 + 34) + ((v2 - arg0) >> 3)) if (v4 > 0) else 0)))
    v2 = (load8u(arg1 + 35) + ((v2 - v5) >> 3))
    v2 = ((load8u(arg1 + 35) + ((v2 - v5) >> 3)) if (v2 > 0) else 0)
    store8(arg1 + 35, (255 if (v2 >= 255) else ((load8u(arg1 + 35) + ((v2 - v5) >> 3)) if (v2 > 0) else 0)))
    v4 = (v3 + ((v3 * 20091) >> 16))
    v2 = ((v3 + ((v3 * 20091) >> 16)) + v6)
    v3 = (load8u(arg1) + ((((v3 + ((v3 * 20091) >> 16)) + v6) + v5) >> 3))
    v3 = ((load8u(arg1) + ((((v3 + ((v3 * 20091) >> 16)) + v6) + v5) >> 3)) if (v3 > 0) else 0)
    store8(arg1, (255 if (v3 >= 255) else ((load8u(arg1) + ((((v3 + ((v3 * 20091) >> 16)) + v6) + v5) >> 3)) if (v3 > 0) else 0)))
    v3 = (load8u(arg1 + 1) + ((arg0 + v2) >> 3))
    v3 = ((load8u(arg1 + 1) + ((arg0 + v2) >> 3)) if (v3 > 0) else 0)
    store8(arg1 + 1, (255 if (v3 >= 255) else ((load8u(arg1 + 1) + ((arg0 + v2) >> 3)) if (v3 > 0) else 0)))
    v3 = (load8u(arg1 + 2) + ((v2 - arg0) >> 3))
    v3 = ((load8u(arg1 + 2) + ((v2 - arg0) >> 3)) if (v3 > 0) else 0)
    store8(arg1 + 2, (255 if (v3 >= 255) else ((load8u(arg1 + 2) + ((v2 - arg0) >> 3)) if (v3 > 0) else 0)))
    v2 = (load8u(arg1 + 3) + ((v2 - v5) >> 3))
    v2 = ((load8u(arg1 + 3) + ((v2 - v5) >> 3)) if (v2 > 0) else 0)
    store8(arg1 + 3, (255 if (v2 >= 255) else ((load8u(arg1 + 3) + ((v2 - v5) >> 3)) if (v2 > 0) else 0)))
    v2 = (v6 - v7)
    v3 = (load8u(arg1 + 64) + ((v5 + (v6 - v7)) >> 3))
    v3 = ((load8u(arg1 + 64) + ((v5 + (v6 - v7)) >> 3)) if (v3 > 0) else 0)
    store8(arg1 + 64, (255 if (v3 >= 255) else ((load8u(arg1 + 64) + ((v5 + (v6 - v7)) >> 3)) if (v3 > 0) else 0)))
    v3 = (load8u(arg1 + 65) + ((arg0 + v2) >> 3))
    v3 = ((load8u(arg1 + 65) + ((arg0 + v2) >> 3)) if (v3 > 0) else 0)
    store8(arg1 + 65, (255 if (v3 >= 255) else ((load8u(arg1 + 65) + ((arg0 + v2) >> 3)) if (v3 > 0) else 0)))
    v3 = (load8u(arg1 + 66) + ((v2 - arg0) >> 3))
    v3 = ((load8u(arg1 + 66) + ((v2 - arg0) >> 3)) if (v3 > 0) else 0)
    store8(arg1 + 66, (255 if (v3 >= 255) else ((load8u(arg1 + 66) + ((v2 - arg0) >> 3)) if (v3 > 0) else 0)))
    v2 = (load8u(arg1 + 67) + ((v2 - v5) >> 3))
    v2 = ((load8u(arg1 + 67) + ((v2 - v5) >> 3)) if (v2 > 0) else 0)
    store8(arg1 + 67, (255 if (v2 >= 255) else ((load8u(arg1 + 67) + ((v2 - v5) >> 3)) if (v2 > 0) else 0)))
    v6 = (v6 - v4)
    v2 = (load8u(arg1 + 96) + (((v6 - v4) + v5) >> 3))
    v2 = ((load8u(arg1 + 96) + (((v6 - v4) + v5) >> 3)) if (v2 > 0) else 0)
    store8(arg1 + 96, (255 if (v2 >= 255) else ((load8u(arg1 + 96) + (((v6 - v4) + v5) >> 3)) if (v2 > 0) else 0)))
    v2 = (load8u(arg1 + 97) + ((arg0 + v6) >> 3))
    v2 = ((load8u(arg1 + 97) + ((arg0 + v6) >> 3)) if (v2 > 0) else 0)
    store8(arg1 + 97, (255 if (v2 >= 255) else ((load8u(arg1 + 97) + ((arg0 + v6) >> 3)) if (v2 > 0) else 0)))
    arg0 = (load8u(arg1 + 98) + ((v6 - arg0) >> 3))
    arg0 = ((load8u(arg1 + 98) + ((v6 - arg0) >> 3)) if (arg0 > 0) else 0)
    store8(arg1 + 98, (255 if (arg0 >= 255) else ((load8u(arg1 + 98) + ((v6 - arg0) >> 3)) if (arg0 > 0) else 0)))
    arg0 = (load8u(arg1 + 99) + ((v6 - v5) >> 3))
    arg0 = ((load8u(arg1 + 99) + ((v6 - v5) >> 3)) if (arg0 > 0) else 0)
    store8(arg1 + 99, (255 if (arg0 >= 255) else ((load8u(arg1 + 99) + ((v6 - v5) >> 3)) if (arg0 > 0) else 0)))

# ----------------------------------------------------------
# $func1026
# ----------------------------------------------------------
def func1026(arg0):
    v2 = (load32(17088) - load8u((arg0 - 33)))
    v1 = ((load32(17088) - load8u((arg0 - 33))) + load8u((arg0 - 1)))
    v11 = (arg0 - 32)
    v3 = load8u((arg0 - 32))
    store8(arg0, load8u((((load32(17088) - load8u((arg0 - 33))) + load8u((arg0 - 1))) + load8u((arg0 - 32)))))
    v12 = (arg0 - 31)
    v4 = load8u((arg0 - 31))
    store8(arg0 + 1, load8u((v1 + load8u((arg0 - 31)))))
    v13 = (arg0 - 30)
    v5 = load8u((arg0 - 30))
    store8(arg0 + 2, load8u((v1 + load8u((arg0 - 30)))))
    v14 = (arg0 - 29)
    v6 = load8u((arg0 - 29))
    store8(arg0 + 3, load8u((v1 + load8u((arg0 - 29)))))
    v15 = (arg0 - 28)
    v7 = load8u((arg0 - 28))
    store8(arg0 + 4, load8u((v1 + load8u((arg0 - 28)))))
    v16 = (arg0 - 27)
    v8 = load8u((arg0 - 27))
    store8(arg0 + 5, load8u((v1 + load8u((arg0 - 27)))))
    v17 = (arg0 - 26)
    v9 = load8u((arg0 - 26))
    store8(arg0 + 6, load8u((v1 + load8u((arg0 - 26)))))
    v18 = (arg0 - 25)
    v10 = load8u((arg0 - 25))
    store8(arg0 + 7, load8u((v1 + load8u((arg0 - 25)))))
    v1 = (v2 + load8u(arg0 + 31))
    store8(arg0 + 32, load8u((v3 + (v2 + load8u(arg0 + 31)))))
    store8(arg0 + 33, load8u((v1 + v4)))
    store8(arg0 + 34, load8u((v1 + v5)))
    store8(arg0 + 35, load8u((v1 + v6)))
    store8(arg0 + 36, load8u((v1 + v7)))
    store8(arg0 + 37, load8u((v1 + v8)))
    store8(arg0 + 38, load8u((v1 + v9)))
    store8(arg0 + 39, load8u((v1 + v10)))
    v1 = (v2 + load8u(arg0 + 63))
    store8(arg0 + 64, load8u((v3 + (v2 + load8u(arg0 + 63)))))
    store8(arg0 + 65, load8u((v1 + v4)))
    store8(arg0 + 66, load8u((v1 + v5)))
    store8(arg0 + 67, load8u((v1 + v6)))
    store8(arg0 + 68, load8u((v1 + v7)))
    store8(arg0 + 69, load8u((v1 + v8)))
    store8(arg0 + 70, load8u((v1 + v9)))
    store8(arg0 + 71, load8u((v1 + v10)))
    v1 = (v2 + load8u(arg0 + 95))
    v3 = load8u(v11)
    store8(arg0 + 96, load8u(((v2 + load8u(arg0 + 95)) + load8u(v11))))
    v4 = load8u(v12)
    store8(arg0 + 97, load8u((v1 + load8u(v12))))
    v5 = load8u(v13)
    store8(arg0 + 98, load8u((v1 + load8u(v13))))
    v6 = load8u(v14)
    store8(arg0 + 99, load8u((v1 + load8u(v14))))
    v7 = load8u(v15)
    store8(arg0 + 100, load8u((v1 + load8u(v15))))
    v8 = load8u(v16)
    store8(arg0 + 101, load8u((v1 + load8u(v16))))
    v9 = load8u(v17)
    store8(arg0 + 102, load8u((v1 + load8u(v17))))
    v10 = load8u(v18)
    store8(arg0 + 103, load8u((v1 + load8u(v18))))
    v1 = (v2 + load8u(arg0 + 127))
    store8(arg0 + 128, load8u((v3 + (v2 + load8u(arg0 + 127)))))
    store8(arg0 + 129, load8u((v1 + v4)))
    store8(arg0 + 130, load8u((v1 + v5)))
    store8(arg0 + 131, load8u((v1 + v6)))
    store8(arg0 + 132, load8u((v1 + v7)))
    store8(arg0 + 133, load8u((v1 + v8)))
    store8(arg0 + 134, load8u((v1 + v9)))
    store8(arg0 + 135, load8u((v1 + v10)))
    v1 = (v2 + load8u(arg0 + 159))
    store8(arg0 + 160, load8u((v3 + (v2 + load8u(arg0 + 159)))))
    store8(arg0 + 161, load8u((v1 + v4)))
    store8(arg0 + 162, load8u((v1 + v5)))
    store8(arg0 + 163, load8u((v1 + v6)))
    store8(arg0 + 164, load8u((v1 + v7)))
    store8(arg0 + 165, load8u((v1 + v8)))
    store8(arg0 + 166, load8u((v1 + v9)))
    store8(arg0 + 167, load8u((v1 + v10)))
    v1 = (v2 + load8u(arg0 + 191))
    store8(arg0 + 192, load8u(((v2 + load8u(arg0 + 191)) + load8u(v11))))
    store8(arg0 + 193, load8u((v1 + load8u(v12))))
    store8(arg0 + 194, load8u((v1 + load8u(v13))))
    store8(arg0 + 195, load8u((v1 + load8u(v14))))
    store8(arg0 + 196, load8u((v1 + load8u(v15))))
    store8(arg0 + 197, load8u((v1 + load8u(v16))))
    store8(arg0 + 198, load8u((v1 + load8u(v17))))
    store8(arg0 + 199, load8u((v1 + load8u(v18))))
    v2 = (v2 + load8u(arg0 + 223))
    store8(arg0 + 224, load8u(((v2 + load8u(arg0 + 223)) + load8u(v11))))
    store8(arg0 + 225, load8u((v2 + load8u(v12))))
    store8(arg0 + 226, load8u((v2 + load8u(v13))))
    store8(arg0 + 227, load8u((v2 + load8u(v14))))
    store8(arg0 + 228, load8u((v2 + load8u(v15))))
    store8(arg0 + 229, load8u((v2 + load8u(v16))))
    store8(arg0 + 230, load8u((v2 + load8u(v17))))
    store8(arg0 + 231, load8u((v2 + load8u(v18))))

# ----------------------------------------------------------
# $func1027
# ----------------------------------------------------------
def func1027(arg0):
    v2 = (load32(17088) - load8u((arg0 - 33)))
    v1 = ((load32(17088) - load8u((arg0 - 33))) + load8u((arg0 - 1)))
    v3 = load8u((arg0 - 32))
    store8(arg0, load8u((((load32(17088) - load8u((arg0 - 33))) + load8u((arg0 - 1))) + load8u((arg0 - 32)))))
    v4 = load8u((arg0 - 31))
    store8(arg0 + 1, load8u((v1 + load8u((arg0 - 31)))))
    v5 = load8u((arg0 - 30))
    store8(arg0 + 2, load8u((v1 + load8u((arg0 - 30)))))
    v6 = load8u((arg0 - 29))
    store8(arg0 + 3, load8u((v1 + load8u((arg0 - 29)))))
    v1 = (v2 + load8u(arg0 + 31))
    store8(arg0 + 32, load8u((v3 + (v2 + load8u(arg0 + 31)))))
    store8(arg0 + 33, load8u((v1 + v4)))
    store8(arg0 + 34, load8u((v1 + v5)))
    store8(arg0 + 35, load8u((v1 + v6)))
    v1 = (v2 + load8u(arg0 + 63))
    store8(arg0 + 64, load8u((v3 + (v2 + load8u(arg0 + 63)))))
    store8(arg0 + 65, load8u((v1 + v4)))
    store8(arg0 + 66, load8u((v1 + v5)))
    store8(arg0 + 67, load8u((v1 + v6)))
    v2 = (v2 + load8u(arg0 + 95))
    store8(arg0 + 96, load8u((v3 + (v2 + load8u(arg0 + 95)))))
    store8(arg0 + 97, load8u((v2 + v4)))
    store8(arg0 + 98, load8u((v2 + v5)))
    store8(arg0 + 99, load8u((v2 + v6)))

# ----------------------------------------------------------
# $func1028
# ----------------------------------------------------------
def func1028(arg0):
    v3 = (arg0 - 17)
    v4 = (arg0 - 18)
    v5 = (arg0 - 19)
    v6 = (arg0 - 20)
    v7 = (arg0 - 21)
    v8 = (arg0 - 22)
    v9 = (arg0 - 23)
    v10 = (arg0 - 24)
    v11 = (arg0 - 25)
    v12 = (arg0 - 26)
    v13 = (arg0 - 27)
    v14 = (arg0 - 28)
    v15 = (arg0 - 29)
    v16 = (arg0 - 30)
    v17 = (arg0 - 31)
    v18 = (arg0 - 32)
    v19 = (load32(17088) - load8u((arg0 - 33)))
    while True:  # $label0
        v1 = (v19 + load8u((arg0 - 1)))
        store8(arg0, load8u(((v19 + load8u((arg0 - 1))) + load8u(v18))))
        store8(arg0 + 1, load8u((v1 + load8u(v17))))
        store8(arg0 + 2, load8u((v1 + load8u(v16))))
        store8(arg0 + 3, load8u((v1 + load8u(v15))))
        store8(arg0 + 4, load8u((v1 + load8u(v14))))
        store8(arg0 + 5, load8u((v1 + load8u(v13))))
        store8(arg0 + 6, load8u((v1 + load8u(v12))))
        store8(arg0 + 7, load8u((v1 + load8u(v11))))
        store8(arg0 + 8, load8u((v1 + load8u(v10))))
        store8(arg0 + 9, load8u((v1 + load8u(v9))))
        store8(arg0 + 10, load8u((v1 + load8u(v8))))
        store8(arg0 + 11, load8u((v1 + load8u(v7))))
        store8(arg0 + 12, load8u((v1 + load8u(v6))))
        store8(arg0 + 13, load8u((v1 + load8u(v5))))
        store8(arg0 + 14, load8u((v1 + load8u(v4))))
        store8(arg0 + 15, load8u((v1 + load8u(v3))))
        arg0 = (arg0 + 32)
        v2 = (v2 + 1)
        if ((v2 + 1) != 16):
            continue
        break

# ----------------------------------------------------------
# $func1029
# ----------------------------------------------------------
def func1029(arg0):
    if (u32(load32(arg0 + 4)) >= u32(2)):
        a_c()
        raise Unreachable()
    return not load32(arg0 + 20)

# ----------------------------------------------------------
# $func1030
# ----------------------------------------------------------
def func1030(arg0, arg1, arg2):
    v12 = (0 - arg1)
    v11 = (arg1 << 2)
    v6 = (arg0 + (arg1 << 2))
    v13 = (0 - (arg1 << 1))
    v14 = ((arg2 << 1) | 1)
    arg0 = load32(17088)
    arg2 = load32(16308)
    v15 = load32(16076)
    v10 = load32(17616)
    while True:  # $label0
        v3 = (v4 + v6)
        v7 = ((v4 + v6) + v12)
        v8 = load8u(((v4 + v6) + v12))
        v9 = load8u(v3)
        v5 = (load8u((v3 + v13)) - load8u((arg1 + v3)))
        if (v14 >= ((load8u((v10 + (load8u(((v4 + v6) + v12)) - load8u(v3)))) << 2) + load8u((v10 + (load8u((v3 + v13)) - load8u((arg1 + v3))))))):
            v5 = (load8s((v5 + v15)) + ((v9 - v8) * 3))
            v16 = load8s((arg2 + (((load8s((v5 + v15)) + ((v9 - v8) * 3)) + 4) >> 3)))
            store8(v7, load8u((arg0 + (load8s((arg2 + ((v5 + 3) >> 3))) + v8))))
            store8(v3, load8u((arg0 + (v9 - v16))))
        v4 = (v4 + 1)
        if ((v4 + 1) != 16):
            continue
        break
    v6 = (v6 + v11)
    v4 = 0
    while True:  # $label1
        v3 = (v4 + v6)
        v7 = ((v4 + v6) + v12)
        v8 = load8u(((v4 + v6) + v12))
        v9 = load8u(v3)
        v5 = (load8u((v3 + v13)) - load8u((arg1 + v3)))
        if (v14 >= ((load8u((v10 + (load8u(((v4 + v6) + v12)) - load8u(v3)))) << 2) + load8u((v10 + (load8u((v3 + v13)) - load8u((arg1 + v3))))))):
            v5 = (load8s((v5 + v15)) + ((v9 - v8) * 3))
            v16 = load8s((arg2 + (((load8s((v5 + v15)) + ((v9 - v8) * 3)) + 4) >> 3)))
            store8(v7, load8u((arg0 + (load8s((arg2 + ((v5 + 3) >> 3))) + v8))))
            store8(v3, load8u((arg0 + (v9 - v16))))
        v4 = (v4 + 1)
        if ((v4 + 1) != 16):
            continue
        break
    v8 = (v6 + v11)
    v4 = 0
    while True:  # $label2
        v3 = (v4 + v8)
        v9 = ((v4 + v8) + v12)
        v11 = load8u(((v4 + v8) + v12))
        v6 = load8u(v3)
        v7 = (load8u((v3 + v13)) - load8u((arg1 + v3)))
        if (v14 >= ((load8u((v10 + (load8u(((v4 + v8) + v12)) - load8u(v3)))) << 2) + load8u((v10 + (load8u((v3 + v13)) - load8u((arg1 + v3))))))):
            v7 = (load8s((v7 + v15)) + ((v6 - v11) * 3))
            v5 = load8s((arg2 + (((load8s((v7 + v15)) + ((v6 - v11) * 3)) + 4) >> 3)))
            store8(v9, load8u((arg0 + (load8s((arg2 + ((v7 + 3) >> 3))) + v11))))
            store8(v3, load8u((arg0 + (v6 - v5))))
        v4 = (v4 + 1)
        if ((v4 + 1) != 16):
            continue
        break

# ----------------------------------------------------------
# $func1031
# ----------------------------------------------------------
def func1031(arg0, arg1, arg2):
    v10 = (0 - arg1)
    v11 = (0 - (arg1 << 1))
    v12 = ((arg2 << 1) | 1)
    v5 = load32(17088)
    v6 = load32(16308)
    v13 = load32(16076)
    v7 = load32(17616)
    while True:  # $label0
        arg2 = (arg0 + v3)
        v14 = ((arg0 + v3) + v10)
        v8 = load8u(((arg0 + v3) + v10))
        v9 = load8u(arg2)
        v4 = (load8u((arg2 + v11)) - load8u((arg1 + arg2)))
        if (v12 >= ((load8u((v7 + (load8u(((arg0 + v3) + v10)) - load8u(arg2)))) << 2) + load8u((v7 + (load8u((arg2 + v11)) - load8u((arg1 + arg2))))))):
            v4 = (load8s((v4 + v13)) + ((v9 - v8) * 3))
            v15 = load8s((v6 + (((load8s((v4 + v13)) + ((v9 - v8) * 3)) + 4) >> 3)))
            store8(v14, load8u((v5 + (load8s((v6 + ((v4 + 3) >> 3))) + v8))))
            store8(arg2, load8u((v5 + (v9 - v15))))
        v3 = (v3 + 1)
        if ((v3 + 1) != 16):
            continue
        break

# ----------------------------------------------------------
# $func1032
# ----------------------------------------------------------
def func1032(arg0, arg1, arg2):
    v11 = (arg0 + 4)
    v12 = ((arg2 << 1) | 1)
    arg2 = 0
    v8 = load32(17088)
    v9 = load32(16308)
    v13 = load32(16076)
    v10 = load32(17616)
    while True:  # $label0
        v3 = (v11 + (arg1 * arg2))
        v6 = ((v11 + (arg1 * arg2)) - 1)
        v5 = load8u(((v11 + (arg1 * arg2)) - 1))
        v7 = load8u(v3)
        v4 = (load8u((v3 - 2)) - load8u(v3 + 1))
        if (v12 >= ((load8u((v10 + (load8u(((v11 + (arg1 * arg2)) - 1)) - load8u(v3)))) << 2) + load8u((v10 + (load8u((v3 - 2)) - load8u(v3 + 1)))))):
            v4 = (load8s((v4 + v13)) + ((v7 - v5) * 3))
            v14 = load8s((v9 + (((load8s((v4 + v13)) + ((v7 - v5) * 3)) + 4) >> 3)))
            store8(v6, load8u((v8 + (load8s((v9 + ((v4 + 3) >> 3))) + v5))))
            store8(v3, load8u((v8 + (v7 - v14))))
        arg2 = (arg2 + 1)
        if ((arg2 + 1) != 16):
            continue
        break
    v11 = (arg0 + 8)
    arg2 = 0
    while True:  # $label1
        v3 = (v11 + (arg1 * arg2))
        v6 = ((v11 + (arg1 * arg2)) - 1)
        v5 = load8u(((v11 + (arg1 * arg2)) - 1))
        v7 = load8u(v3)
        v4 = (load8u((v3 - 2)) - load8u(v3 + 1))
        if (v12 >= ((load8u((v10 + (load8u(((v11 + (arg1 * arg2)) - 1)) - load8u(v3)))) << 2) + load8u((v10 + (load8u((v3 - 2)) - load8u(v3 + 1)))))):
            v4 = (load8s((v4 + v13)) + ((v7 - v5) * 3))
            v14 = load8s((v9 + (((load8s((v4 + v13)) + ((v7 - v5) * 3)) + 4) >> 3)))
            store8(v6, load8u((v8 + (load8s((v9 + ((v4 + 3) >> 3))) + v5))))
            store8(v3, load8u((v8 + (v7 - v14))))
        arg2 = (arg2 + 1)
        if ((arg2 + 1) != 16):
            continue
        break
    v7 = (arg0 + 12)
    arg2 = 0
    while True:  # $label2
        arg0 = (v7 + (arg1 * arg2))
        v11 = ((v7 + (arg1 * arg2)) - 1)
        v3 = load8u(((v7 + (arg1 * arg2)) - 1))
        v5 = load8u(arg0)
        v6 = (load8u((arg0 - 2)) - load8u(arg0 + 1))
        if (v12 >= ((load8u((v10 + (load8u(((v7 + (arg1 * arg2)) - 1)) - load8u(arg0)))) << 2) + load8u((v10 + (load8u((arg0 - 2)) - load8u(arg0 + 1)))))):
            v6 = (load8s((v6 + v13)) + ((v5 - v3) * 3))
            v4 = load8s((v9 + (((load8s((v6 + v13)) + ((v5 - v3) * 3)) + 4) >> 3)))
            store8(v11, load8u((v8 + (load8s((v9 + ((v6 + 3) >> 3))) + v3))))
            store8(arg0, load8u((v8 + (v5 - v4))))
        arg2 = (arg2 + 1)
        if ((arg2 + 1) != 16):
            continue
        break

# ----------------------------------------------------------
# $func1033
# ----------------------------------------------------------
def func1033(arg0, arg1, arg2):
    v10 = ((arg2 << 1) | 1)
    v5 = load32(17088)
    v6 = load32(16308)
    v11 = load32(16076)
    v7 = load32(17616)
    while True:  # $label0
        arg2 = (arg0 + (arg1 * v3))
        v12 = ((arg0 + (arg1 * v3)) - 1)
        v8 = load8u(((arg0 + (arg1 * v3)) - 1))
        v9 = load8u(arg2)
        v4 = (load8u((arg2 - 2)) - load8u(arg2 + 1))
        if (v10 >= ((load8u((v7 + (load8u(((arg0 + (arg1 * v3)) - 1)) - load8u(arg2)))) << 2) + load8u((v7 + (load8u((arg2 - 2)) - load8u(arg2 + 1)))))):
            v4 = (load8s((v4 + v11)) + ((v9 - v8) * 3))
            v13 = load8s((v6 + (((load8s((v4 + v11)) + ((v9 - v8) * 3)) + 4) >> 3)))
            store8(v12, load8u((v5 + (load8s((v6 + ((v4 + 3) >> 3))) + v8))))
            store8(arg2, load8u((v5 + (v9 - v13))))
        v3 = (v3 + 1)
        if ((v3 + 1) != 16):
            continue
        break

# ----------------------------------------------------------
# $func1034
# ----------------------------------------------------------
def func1034(arg0):
    store32(arg0 + 20, 0)
    while True:  # $label1
        while True:  # $label0
            while True:  # $label2
                # br_table load32(arg0 + 4)
                break
                break
            a_c()
            raise Unreachable()
            break
        store32(arg0 + 4, 1)
        break
    return 1

# ----------------------------------------------------------
# $func1035
# ----------------------------------------------------------
def func1035(arg0):
    v1 = load8u(arg0 + 31)
    v3 = (load8u(arg0 + 31) + 2)
    v2 = load8u(arg0 + 63)
    store8(arg0 + 96, (((load8u(arg0 + 95) + ((load8u(arg0 + 31) + 2) + (load8u(arg0 + 63) << 1))) & 0xFFFFFFFF) >> 2))
    v4 = load8u((arg0 - 1))
    v5 = (load8u((arg0 - 1)) + 2)
    v1 = (((v2 + ((load8u((arg0 - 1)) + 2) + (v1 << 1))) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 97, (((v2 + ((load8u((arg0 - 1)) + 2) + (v1 << 1))) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 64, v1)
    v2 = load8u((arg0 - 33))
    v1 = (((load8u((arg0 - 33)) + (v3 + (v4 << 1))) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 98, (((load8u((arg0 - 33)) + (v3 + (v4 << 1))) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 65, v1)
    store8(arg0 + 32, v1)
    v3 = load8u((arg0 - 32))
    v1 = ((((v5 + load8u((arg0 - 32))) + (v2 << 1)) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 99, ((((v5 + load8u((arg0 - 32))) + (v2 << 1)) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 66, v1)
    store8(arg0 + 33, v1)
    store8(arg0, v1)
    v5 = load8u((arg0 - 29))
    v1 = load8u((arg0 - 30))
    v4 = load8u((arg0 - 31))
    v2 = (((((v2 + load8u((arg0 - 31))) + (v3 << 1)) + 2) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 67, (((((v2 + load8u((arg0 - 31))) + (v3 << 1)) + 2) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 34, v2)
    store8(arg0 + 1, v2)
    v2 = (((((v1 + v3) + (v4 << 1)) + 2) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 35, (((((v1 + v3) + (v4 << 1)) + 2) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 2, v2)
    store8(arg0 + 3, (((((v4 + v5) + (v1 << 1)) + 2) & 0xFFFFFFFF) >> 2))

# ----------------------------------------------------------
# $func1036
# ----------------------------------------------------------
def func1036(arg0, arg1):
    while True:  # $label20
        while True:  # $label19
            while True:  # $label14
                while True:  # $label8
                    while True:  # $label7
                        while True:  # $label5
                            while True:  # $label4
                                while True:  # $label0
                                    v4 = load32(arg0 + 8)
                                    if (arg1 <= load32(load32(arg0 + 8) + 88)):
                                        v9 = load32(arg0 + 108)
                                        v3 = (arg1 - load32(arg0 + 108))
                                        if ((arg1 - load32(arg0 + 108)) >= 17):
                                            break
                                        while True:  # $label1
                                            if (v3 <= 0):
                                                break
                                            v2 = load32(arg0 + 100)
                                            v7 = (load32(arg0 + 16) + ((v9 * load32(arg0 + 100)) << 2))
                                            v5 = load32(v4)
                                            v8 = load32(arg0 + 20)
                                            while True:  # $label2
                                                v6 = load32(arg0 + 192)
                                                if (load32(arg0 + 192) > 0):
                                                    v2 = (v6 - 1)
                                                    if (v6 == 1):
                                                        break
                                                    while True:  # $label3
                                                        v6 = (v2 - 1)
                                                        v3 = (u32(v2) > u32(1))
                                                        v2 = v6
                                                        if v3:
                                                            continue
                                                        break
                                                    break
                                                if (v7 == v8):
                                                    break
                                                # TODO: memory.copy
                                                break
                                            v12 = load32(arg0 + 108)
                                            if (load32(arg0 + 108) >= arg1):
                                                break
                                            v3 = load32(v4 + 80)
                                            v9 = load32(v4 + 76)
                                            if (load32(v4 + 80) <= load32(v4 + 76)):
                                                break
                                            v2 = load32(v4 + 88)
                                            v6 = (load32(v4 + 88) if (arg1 > v2) else arg1)
                                            v14 = load32(v4 + 84)
                                            v2 = (v12 < v14)
                                            v7 = (load32(v4 + 84) if (v12 < v14) else v12)
                                            if ((load32(v4 + 88) if (arg1 > v2) else arg1) <= (load32(v4 + 84) if (v12 < v14) else v12)):
                                                break
                                            v6 = (v6 - v7)
                                            store32(v4 + 16, (v6 - v7))
                                            v11 = (v3 - v9)
                                            store32(v4 + 12, (v3 - v9))
                                            store32(v4 + 8, (v7 - v14))
                                            v15 = (v5 << 2)
                                            v10 = ((v8 + (((v5 << 2) * (v14 - v12)) if v2 else 0)) + (v9 << 2))
                                            while True:  # $label13
                                                v17 = load32(arg0 + 12)
                                                v12 = load32(load32(arg0 + 12))
                                                if (u32(load32(load32(arg0 + 12))) <= u32(10)):
                                                    v8 = load32(v17 + 20)
                                                    v13 = (load32(v17 + 16) + (load32(v17 + 20) * load32(arg0 + 116)))
                                                    while True:  # $label6
                                                        if load32(v4 + 92):
                                                            if (v6 <= 0):
                                                                v3 = 0
                                                                break
                                                            v5 = 0
                                                            v3 = 0
                                                            while True:  # $label11
                                                                v7 = load32(arg0 + 284)
                                                                v2 = load32(load32(arg0 + 284) + 32)
                                                                v7 = (((load32(load32(arg0 + 284) + 32) + load32(v7 + 24)) - 1) // v2)
                                                                v9 = (v6 - v5)
                                                                v2 = (v6 - v5)
                                                                v7 = ((((load32(load32(arg0 + 284) + 32) + load32(v7 + 24)) - 1) // v2) if (v2 > v7) else (v6 - v5))
                                                                if (((((load32(load32(arg0 + 284) + 32) + load32(v7 + 24)) - 1) // v2) if (v2 > v7) else (v6 - v5)) <= 0):
                                                                    break
                                                                if (v7 > v9):
                                                                    break
                                                                v2 = (v10 + (v5 * v15))
                                                                func446((v10 + (v5 * v15)), v15, load32(load32(arg0 + 284) + 44), v7)
                                                                if (func82(load32(arg0 + 284), v9, v2, v15) != v7):
                                                                    break
                                                                v5 = (v5 + v7)
                                                                v11 = 0
                                                                while True:  # $label9
                                                                    v4 = load32(arg0 + 284)
                                                                    v7 = (load32(arg0 + 284) - -64)
                                                                    if (load32((load32(arg0 + 284) - -64)) >= load32(v4 + 56)):
                                                                        break
                                                                    v2 = (v13 + (v3 * v8))
                                                                    v14 = load32(v4 + 52)
                                                                    v9 = load32(v4 + 68)
                                                                    while True:  # $label10
                                                                        if (load32(v4 + 24) > 0):
                                                                            break
                                                                        func91(((v2 * v3) << 2), v4)
                                                                        func454(v9, v14, v12, v2)
                                                                        v11 = (v11 + 1)
                                                                        v2 = (v2 + v8)
                                                                        if (load32(v7) < load32(v4 + 56)):
                                                                            continue
                                                                        break
                                                                    break
                                                                v3 = (v3 + v11)
                                                                if (v5 < v6):
                                                                    continue
                                                                break
                                                            break
                                                        if (v6 > 0):
                                                            v2 = v6
                                                            while True:  # $label12
                                                                func454(v10, v11, v12, v13)
                                                                v13 = (v8 + v13)
                                                                v10 = (v10 + v15)
                                                                v3 = (u32(v2) > u32(1))
                                                                v2 = (v2 - 1)
                                                                if v3:
                                                                    continue
                                                                break
                                                        v3 = v6
                                                        break
                                                    v5 = (load32(arg0 + 116) + v3)
                                                    break
                                                v5 = load32(arg0 + 116)
                                                if load32(v4 + 92):
                                                    if (v6 <= 0):
                                                        break
                                                    while True:  # $label17
                                                        v3 = load32(arg0 + 284)
                                                        v2 = load32(v3 + 32)
                                                        v3 = (((load32(v3 + 32) + load32(v3 + 24)) - 1) // v2)
                                                        v2 = (v6 - v13)
                                                        v3 = ((((load32(v3 + 32) + load32(v3 + 24)) - 1) // v2) if (v2 > v3) else (v6 - v13))
                                                        func446(v10, v15, load32(load32(arg0 + 284) + 44), ((((load32(v3 + 32) + load32(v3 + 24)) - 1) // v2) if (v2 > v3) else (v6 - v13)))
                                                        if (func82(load32(arg0 + 284), v2, v10, v15) != v3):
                                                            break
                                                        v13 = (v3 + v13)
                                                        v14 = (v3 * v15)
                                                        v11 = 0
                                                        while True:  # $label15
                                                            v4 = load32(arg0 + 284)
                                                            v9 = (load32(arg0 + 284) - -64)
                                                            if (load32((load32(arg0 + 284) - -64)) >= load32(v4 + 56)):
                                                                break
                                                            v8 = load32(v4 + 52)
                                                            v12 = load32(v4 + 68)
                                                            v7 = (load32(v4 + 68) + 3)
                                                            v2 = v5
                                                            while True:  # $label16
                                                                if (load32(v4 + 24) > 0):
                                                                    break
                                                                func91(call_table(load32(9687284)), v4)
                                                                v16 = load32(arg0 + 12)
                                                                v3 = (v2 >> 1)
                                                                v3 = load32(v16 + 28)
                                                                if load32(v16 + 28):
                                                                v11 = (v11 + 1)
                                                                v2 = (v2 + 1)
                                                                if (load32(v9) < load32(v4 + 56)):
                                                                    continue
                                                                break
                                                            break
                                                        v10 = (v10 + v14)
                                                        v5 = (v5 + v11)
                                                        if (v6 > v13):
                                                            continue
                                                        break
                                                    break
                                                if (v6 <= 0):
                                                    break
                                                while True:  # $label18
                                                    v3 = load32(arg0 + 12)
                                                    v2 = (v5 >> 1)
                                                    v2 = load32(v3 + 28)
                                                    if load32(v3 + 28):
                                                    v5 = (v5 + 1)
                                                    v10 = (v10 + v15)
                                                    v2 = (u32(v6) > u32(1))
                                                    v6 = (v6 - 1)
                                                    if v2:
                                                        continue
                                                    break
                                                break
                                            store32(arg0 + 116, v5)
                                            if (v5 > load32(v17 + 8)):
                                                break
                                            break
                                        store32(arg0 + 108, arg1)
                                        if (load32(arg0 + 104) < arg1):
                                            break
                                        return 0
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
    a_c()
    raise Unreachable()
    return 2955

# ----------------------------------------------------------
# $func1037
# ----------------------------------------------------------
def func1037(arg0, arg1, arg2, arg3):
    if arg1:
        if (arg2 > 0):
            while True:  # $label0
                v5 = (v6 << 2)
                v4 = (arg1 + v5)
                v7 = load32((arg1 + v5) + 4)
                v4 = load32(v4)
                v4 = (((((load32((arg1 + v5) + 4) ^ load32(v4)) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v7))
                v5 = load32((arg0 + v5))
                store32((arg3 + (v6 << 2)), (((((((((load32((arg1 + v5) + 4) ^ load32(v4)) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v7)) & -16711936) + (load32((arg0 + v5)) & -16711936)) & -16711936) | (((v4 & 16711935) + (v5 & 16711935)) & 16711935)))
                v6 = (v6 + 1)
                if ((v6 + 1) != arg2):
                    continue
                break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1038
# ----------------------------------------------------------
def func1038(arg0, arg1, arg2, arg3):
    if arg1:
        if (arg2 > 0):
            while True:  # $label0
                v5 = (v6 << 2)
                v4 = (arg1 + v5)
                v7 = load32((arg1 + v5))
                v4 = load32((v4 - 4))
                v4 = (((((load32((arg1 + v5)) ^ load32((v4 - 4))) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v7))
                v5 = load32((arg0 + v5))
                store32((arg3 + (v6 << 2)), (((((((((load32((arg1 + v5)) ^ load32((v4 - 4))) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v7)) & -16711936) + (load32((arg0 + v5)) & -16711936)) & -16711936) | (((v4 & 16711935) + (v5 & 16711935)) & 16711935)))
                v6 = (v6 + 1)
                if ((v6 + 1) != arg2):
                    continue
                break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1039
# ----------------------------------------------------------
def func1039(arg0, arg1, arg2, arg3):
    if arg1:
        if (arg2 > 0):
            v4 = load32((arg3 - 4))
            while True:  # $label0
                v5 = (v6 << 2)
                v7 = load32((arg1 + v5))
                v4 = (((((load32((arg1 + v5)) ^ v4) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v7))
                v5 = load32((arg0 + v5))
                v4 = (((((((((load32((arg1 + v5)) ^ v4) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v7)) & -16711936) + (load32((arg0 + v5)) & -16711936)) & -16711936) | (((v4 & 16711935) + (v5 & 16711935)) & 16711935))
                store32((arg3 + (v6 << 2)), (((((((((load32((arg1 + v5)) ^ v4) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v7)) & -16711936) + (load32((arg0 + v5)) & -16711936)) & -16711936) | (((v4 & 16711935) + (v5 & 16711935)) & 16711935)))
                v6 = (v6 + 1)
                if ((v6 + 1) != arg2):
                    continue
                break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1040
# ----------------------------------------------------------
def func1040(arg0, arg1, arg2, arg3):
    if arg1:
        if (arg2 > 0):
            v6 = (arg1 - 4)
            arg1 = load32((arg3 - 4))
            while True:  # $label0
                v4 = (v5 << 2)
                v7 = load32((v4 + v6))
                arg1 = (((((load32((v4 + v6)) ^ arg1) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg1 & v7))
                v4 = load32((arg0 + v4))
                arg1 = (((((((((load32((v4 + v6)) ^ arg1) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg1 & v7)) & -16711936) + (load32((arg0 + v4)) & -16711936)) & -16711936) | (((arg1 & 16711935) + (v4 & 16711935)) & 16711935))
                store32((arg3 + (v5 << 2)), (((((((((load32((v4 + v6)) ^ arg1) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg1 & v7)) & -16711936) + (load32((arg0 + v4)) & -16711936)) & -16711936) | (((arg1 & 16711935) + (v4 & 16711935)) & 16711935)))
                v5 = (v5 + 1)
                if ((v5 + 1) != arg2):
                    continue
                break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1041
# ----------------------------------------------------------
def func1041(arg0, arg1, arg2, arg3):
    if arg1:
        if (arg2 > 0):
            v4 = load32((arg3 - 4))
            while True:  # $label0
                v5 = (v6 << 2)
                v7 = (arg1 + v5)
                v8 = load32((arg1 + v5) + 4)
                v4 = (((((load32((arg1 + v5) + 4) ^ v4) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v8))
                v7 = load32(v7)
                v4 = ((((((((((load32((arg1 + v5) + 4) ^ v4) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v8)) ^ load32(v7)) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v7))
                v5 = load32((arg0 + v5))
                v4 = ((((((((((((((load32((arg1 + v5) + 4) ^ v4) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v8)) ^ load32(v7)) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v7)) & -16711936) + (load32((arg0 + v5)) & -16711936)) & -16711936) | (((v4 & 16711935) + (v5 & 16711935)) & 16711935))
                store32((arg3 + (v6 << 2)), ((((((((((((((load32((arg1 + v5) + 4) ^ v4) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v8)) ^ load32(v7)) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v7)) & -16711936) + (load32((arg0 + v5)) & -16711936)) & -16711936) | (((v4 & 16711935) + (v5 & 16711935)) & 16711935)))
                v6 = (v6 + 1)
                if ((v6 + 1) != arg2):
                    continue
                break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1042
# ----------------------------------------------------------
def func1042(arg0, arg1, arg2, arg3):
    if arg1:
        if (arg2 > 0):
            v5 = (arg1 - 4)
            while True:  # $label0
                arg1 = (v4 << 2)
                v6 = load32((arg0 + arg1))
                arg1 = load32((arg1 + v5))
                store32((arg3 + (v4 << 2)), ((((load32((arg0 + arg1)) & -16711936) + (load32((arg1 + v5)) & -16711936)) & -16711936) | (((v6 & 16711935) + (arg1 & 16711935)) & 16711935)))
                v4 = (v4 + 1)
                if ((v4 + 1) != arg2):
                    continue
                break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1043
# ----------------------------------------------------------
def func1043(arg0, arg1, arg2, arg3):
    if arg1:
        if (arg2 > 0):
            v5 = (arg1 + 4)
            while True:  # $label0
                arg1 = (v4 << 2)
                v6 = load32((arg0 + arg1))
                arg1 = load32((arg1 + v5))
                store32((arg3 + (v4 << 2)), ((((load32((arg0 + arg1)) & -16711936) + (load32((arg1 + v5)) & -16711936)) & -16711936) | (((v6 & 16711935) + (arg1 & 16711935)) & 16711935)))
                v4 = (v4 + 1)
                if ((v4 + 1) != arg2):
                    continue
                break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1044
# ----------------------------------------------------------
def func1044(arg0, arg1, arg2, arg3):
    if arg1:
        if (arg2 > 0):
            while True:  # $label0
                v4 = (v5 << 2)
                v6 = load32((arg0 + v4))
                v4 = load32((arg1 + v4))
                store32((arg3 + (v5 << 2)), ((((load32((arg0 + v4)) & -16711936) + (load32((arg1 + v4)) & -16711936)) & -16711936) | (((v6 & 16711935) + (v4 & 16711935)) & 16711935)))
                v5 = (v5 + 1)
                if ((v5 + 1) != arg2):
                    continue
                break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1045
# ----------------------------------------------------------
def func1045(arg0, arg1, arg2, arg3):
    while True:  # $label0
        if (arg2 <= 0):
            break
        arg1 = load32((arg3 - 4))
        if (arg2 != 1):
            v7 = (arg2 & -2)
            while True:  # $label1
                v4 = (v5 << 2)
                v8 = load32((arg0 + v4))
                v9 = (((load32((arg0 + v4)) & -16711936) + (arg1 & -16711936)) & -16711936)
                arg1 = (((v8 & 16711935) + (arg1 & 16711935)) & 16711935)
                store32((arg3 + (v5 << 2)), ((((load32((arg0 + v4)) & -16711936) + (arg1 & -16711936)) & -16711936) | (((v8 & 16711935) + (arg1 & 16711935)) & 16711935)))
                v4 = (v4 | 4)
                v4 = load32((arg0 + v4))
                arg1 = ((((load32((arg0 + v4)) & -16711936) + v9) & -16711936) | (((v4 & 16711935) + arg1) & 16711935))
                store32((arg3 + (v4 | 4)), ((((load32((arg0 + v4)) & -16711936) + v9) & -16711936) | (((v4 & 16711935) + arg1) & 16711935)))
                v5 = (v5 + 2)
                v6 = (v6 + 2)
                if ((v6 + 2) != v7):
                    continue
                break
        if not (arg2 & 1):
            break
        arg2 = (v5 << 2)
        arg0 = load32((arg0 + arg2))
        store32((arg3 + (v5 << 2)), ((((load32((arg0 + arg2)) & -16711936) + (arg1 & -16711936)) & -16711936) | (((arg0 & 16711935) + (arg1 & 16711935)) & 16711935)))
        break

# ----------------------------------------------------------
# $func1046
# ----------------------------------------------------------
def func1046(arg0, arg1, arg2, arg3):
    if arg1:
        if (arg2 > 0):
            v5 = load32((arg3 - 4))
            while True:  # $label0
                v8 = (v7 << 2)
                v6 = (arg1 + v8)
                v4 = load32((arg1 + v8))
                v5 = (((((load32((arg1 + v8)) ^ v5) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v5))
                v4 = (((((((load32((arg1 + v8)) ^ v5) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v5)) & 0xFFFFFFFF) >> 24)
                v6 = load32((v6 - 4))
                v4 = ((((((((load32((arg1 + v8)) ^ v5) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v5)) & 0xFFFFFFFF) >> 24) + i32(((v4 - ((load32((v6 - 4)) & 0xFFFFFFFF) >> 24)) // 2)))
                v4 = (v5 & 255)
                v4 = ((v5 & 255) + i32(((v4 - (v6 & 255)) // 2)))
                v4 = (((v5 & 0xFFFFFFFF) >> 16) & 255)
                v4 = ((((v5 & 0xFFFFFFFF) >> 16) & 255) + i32(((v4 - (((v6 & 0xFFFFFFFF) >> 16) & 255)) // 2)))
                v5 = (((v5 & 0xFFFFFFFF) >> 8) & 255)
                v5 = ((((v5 & 0xFFFFFFFF) >> 8) & 255) + i32(((v5 - (((v6 & 0xFFFFFFFF) >> 8) & 255)) // 2)))
                v5 = (((((((((((((load32((arg1 + v8)) ^ v5) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v5)) & 0xFFFFFFFF) >> 24) + i32(((v4 - ((load32((v6 - 4)) & 0xFFFFFFFF) >> 24)) // 2))) if (u32(v4) < u32(256)) else (((v4 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | (((v5 & 255) + i32(((v4 - (v6 & 255)) // 2))) if (u32(v4) < u32(256)) else (((v4 ^ -1) & 0xFFFFFFFF) >> 24))) | ((((((v5 & 0xFFFFFFFF) >> 16) & 255) + i32(((v4 - (((v6 & 0xFFFFFFFF) >> 16) & 255)) // 2))) if (u32(v4) < u32(256)) else (((v4 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | ((((((v5 & 0xFFFFFFFF) >> 8) & 255) + i32(((v5 - (((v6 & 0xFFFFFFFF) >> 8) & 255)) // 2))) if (u32(v5) < u32(256)) else (((v5 ^ -1) & 0xFFFFFFFF) >> 24)) << 8))
                v6 = load32((arg0 + v8))
                v5 = (((((((((((((((((load32((arg1 + v8)) ^ v5) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v5)) & 0xFFFFFFFF) >> 24) + i32(((v4 - ((load32((v6 - 4)) & 0xFFFFFFFF) >> 24)) // 2))) if (u32(v4) < u32(256)) else (((v4 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | (((v5 & 255) + i32(((v4 - (v6 & 255)) // 2))) if (u32(v4) < u32(256)) else (((v4 ^ -1) & 0xFFFFFFFF) >> 24))) | ((((((v5 & 0xFFFFFFFF) >> 16) & 255) + i32(((v4 - (((v6 & 0xFFFFFFFF) >> 16) & 255)) // 2))) if (u32(v4) < u32(256)) else (((v4 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | ((((((v5 & 0xFFFFFFFF) >> 8) & 255) + i32(((v5 - (((v6 & 0xFFFFFFFF) >> 8) & 255)) // 2))) if (u32(v5) < u32(256)) else (((v5 ^ -1) & 0xFFFFFFFF) >> 24)) << 8)) & -16711936) + (load32((arg0 + v8)) & -16711936)) & -16711936) | (((v5 & 16711935) + (v6 & 16711935)) & 16711935))
                store32((arg3 + (v7 << 2)), (((((((((((((((((load32((arg1 + v8)) ^ v5) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v5)) & 0xFFFFFFFF) >> 24) + i32(((v4 - ((load32((v6 - 4)) & 0xFFFFFFFF) >> 24)) // 2))) if (u32(v4) < u32(256)) else (((v4 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | (((v5 & 255) + i32(((v4 - (v6 & 255)) // 2))) if (u32(v4) < u32(256)) else (((v4 ^ -1) & 0xFFFFFFFF) >> 24))) | ((((((v5 & 0xFFFFFFFF) >> 16) & 255) + i32(((v4 - (((v6 & 0xFFFFFFFF) >> 16) & 255)) // 2))) if (u32(v4) < u32(256)) else (((v4 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | ((((((v5 & 0xFFFFFFFF) >> 8) & 255) + i32(((v5 - (((v6 & 0xFFFFFFFF) >> 8) & 255)) // 2))) if (u32(v5) < u32(256)) else (((v5 ^ -1) & 0xFFFFFFFF) >> 24)) << 8)) & -16711936) + (load32((arg0 + v8)) & -16711936)) & -16711936) | (((v5 & 16711935) + (v6 & 16711935)) & 16711935)))
                v7 = (v7 + 1)
                if ((v7 + 1) != arg2):
                    continue
                break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1047
# ----------------------------------------------------------
def func1047(arg0, arg1, arg2, arg3):
    if arg1:
        if (arg2 > 0):
            v4 = load32((arg3 - 4))
            while True:  # $label0
                v9 = (v8 << 2)
                v6 = (arg1 + v9)
                v7 = load32((arg1 + v9))
                v6 = load32((v6 - 4))
                v5 = ((((load32((arg1 + v9)) & 0xFFFFFFFF) >> 24) + ((v4 & 0xFFFFFFFF) >> 24)) - ((load32((v6 - 4)) & 0xFFFFFFFF) >> 24))
                v5 = (((v7 & 255) + (v4 & 255)) - (v6 & 255))
                v5 = (((((v7 & 0xFFFFFFFF) >> 16) & 255) + (((v4 & 0xFFFFFFFF) >> 16) & 255)) - (((v6 & 0xFFFFFFFF) >> 16) & 255))
                v4 = (((((v7 & 0xFFFFFFFF) >> 8) & 255) + (((v4 & 0xFFFFFFFF) >> 8) & 255)) - (((v6 & 0xFFFFFFFF) >> 8) & 255))
                v4 = (((((((((load32((arg1 + v9)) & 0xFFFFFFFF) >> 24) + ((v4 & 0xFFFFFFFF) >> 24)) - ((load32((v6 - 4)) & 0xFFFFFFFF) >> 24)) if (u32(v5) < u32(256)) else (((v5 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | ((((v7 & 255) + (v4 & 255)) - (v6 & 255)) if (u32(v5) < u32(256)) else (((v5 ^ -1) & 0xFFFFFFFF) >> 24))) | (((((((v7 & 0xFFFFFFFF) >> 16) & 255) + (((v4 & 0xFFFFFFFF) >> 16) & 255)) - (((v6 & 0xFFFFFFFF) >> 16) & 255)) if (u32(v5) < u32(256)) else (((v5 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | (((((((v7 & 0xFFFFFFFF) >> 8) & 255) + (((v4 & 0xFFFFFFFF) >> 8) & 255)) - (((v6 & 0xFFFFFFFF) >> 8) & 255)) if (u32(v4) < u32(256)) else (((v4 ^ -1) & 0xFFFFFFFF) >> 24)) << 8))
                v7 = load32((arg0 + v9))
                v4 = (((((((((((((load32((arg1 + v9)) & 0xFFFFFFFF) >> 24) + ((v4 & 0xFFFFFFFF) >> 24)) - ((load32((v6 - 4)) & 0xFFFFFFFF) >> 24)) if (u32(v5) < u32(256)) else (((v5 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | ((((v7 & 255) + (v4 & 255)) - (v6 & 255)) if (u32(v5) < u32(256)) else (((v5 ^ -1) & 0xFFFFFFFF) >> 24))) | (((((((v7 & 0xFFFFFFFF) >> 16) & 255) + (((v4 & 0xFFFFFFFF) >> 16) & 255)) - (((v6 & 0xFFFFFFFF) >> 16) & 255)) if (u32(v5) < u32(256)) else (((v5 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | (((((((v7 & 0xFFFFFFFF) >> 8) & 255) + (((v4 & 0xFFFFFFFF) >> 8) & 255)) - (((v6 & 0xFFFFFFFF) >> 8) & 255)) if (u32(v4) < u32(256)) else (((v4 ^ -1) & 0xFFFFFFFF) >> 24)) << 8)) & -16711936) + (load32((arg0 + v9)) & -16711936)) & -16711936) | (((v4 & 16711935) + (v7 & 16711935)) & 16711935))
                store32((arg3 + (v8 << 2)), (((((((((((((load32((arg1 + v9)) & 0xFFFFFFFF) >> 24) + ((v4 & 0xFFFFFFFF) >> 24)) - ((load32((v6 - 4)) & 0xFFFFFFFF) >> 24)) if (u32(v5) < u32(256)) else (((v5 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | ((((v7 & 255) + (v4 & 255)) - (v6 & 255)) if (u32(v5) < u32(256)) else (((v5 ^ -1) & 0xFFFFFFFF) >> 24))) | (((((((v7 & 0xFFFFFFFF) >> 16) & 255) + (((v4 & 0xFFFFFFFF) >> 16) & 255)) - (((v6 & 0xFFFFFFFF) >> 16) & 255)) if (u32(v5) < u32(256)) else (((v5 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | (((((((v7 & 0xFFFFFFFF) >> 8) & 255) + (((v4 & 0xFFFFFFFF) >> 8) & 255)) - (((v6 & 0xFFFFFFFF) >> 8) & 255)) if (u32(v4) < u32(256)) else (((v4 ^ -1) & 0xFFFFFFFF) >> 24)) << 8)) & -16711936) + (load32((arg0 + v9)) & -16711936)) & -16711936) | (((v4 & 16711935) + (v7 & 16711935)) & 16711935)))
                v8 = (v8 + 1)
                if ((v8 + 1) != arg2):
                    continue
                break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1048
# ----------------------------------------------------------
def func1048(arg0, arg1, arg2, arg3):
    if arg1:
        if (arg2 > 0):
            v5 = load32((arg3 - 4))
            while True:  # $label0
                v12 = (v10 << 2)
                v6 = (arg1 + v12)
                v7 = load32((arg1 + v12))
                v6 = load32((v6 - 4))
                v4 = (load32((v6 - 4)) & 255)
                v8 = ((v5 & 255) - (load32((v6 - 4)) & 255))
                v8 = (v8 >> 31)
                v8 = ((v6 & 0xFFFFFFFF) >> 24)
                v9 = (((v5 & 0xFFFFFFFF) >> 24) - ((v6 & 0xFFFFFFFF) >> 24))
                v9 = (v9 >> 31)
                v9 = (((v6 & 0xFFFFFFFF) >> 8) & 255)
                v11 = ((((v5 & 0xFFFFFFFF) >> 8) & 255) - (((v6 & 0xFFFFFFFF) >> 8) & 255))
                v11 = (v11 >> 31)
                v4 = ((v7 & 255) - v4)
                v4 = (v4 >> 31)
                v4 = (((v7 & 0xFFFFFFFF) >> 24) - v8)
                v4 = (v4 >> 31)
                v4 = ((((v7 & 0xFFFFFFFF) >> 8) & 255) - v9)
                v4 = (v4 >> 31)
                v7 = (((v6 & 0xFFFFFFFF) >> 16) & 255)
                v6 = ((((v7 & 0xFFFFFFFF) >> 16) & 255) - (((v6 & 0xFFFFFFFF) >> 16) & 255))
                v6 = (v6 >> 31)
                v5 = ((((v5 & 0xFFFFFFFF) >> 16) & 255) - v7)
                v5 = (v5 >> 31)
                v5 = (load32((arg1 + v12)) if (((((((((v5 & 255) - (load32((v6 - 4)) & 255)) ^ (v8 >> 31)) - v8) + (((((v5 & 0xFFFFFFFF) >> 24) - ((v6 & 0xFFFFFFFF) >> 24)) ^ (v9 >> 31)) - v9)) + ((((((v5 & 0xFFFFFFFF) >> 8) & 255) - (((v6 & 0xFFFFFFFF) >> 8) & 255)) ^ (v11 >> 31)) - v11)) - (((((((v7 & 255) - v4) ^ (v4 >> 31)) - v4) + (((((v7 & 0xFFFFFFFF) >> 24) - v8) ^ (v4 >> 31)) - v4)) + ((((((v7 & 0xFFFFFFFF) >> 8) & 255) - v9) ^ (v4 >> 31)) - v4)) + ((((((v7 & 0xFFFFFFFF) >> 16) & 255) - (((v6 & 0xFFFFFFFF) >> 16) & 255)) ^ (v6 >> 31)) - v6))) + ((((((v5 & 0xFFFFFFFF) >> 16) & 255) - v7) ^ (v5 >> 31)) - v5)) <= 0) else v5)
                v7 = load32((arg0 + v12))
                v5 = (((((load32((arg1 + v12)) if (((((((((v5 & 255) - (load32((v6 - 4)) & 255)) ^ (v8 >> 31)) - v8) + (((((v5 & 0xFFFFFFFF) >> 24) - ((v6 & 0xFFFFFFFF) >> 24)) ^ (v9 >> 31)) - v9)) + ((((((v5 & 0xFFFFFFFF) >> 8) & 255) - (((v6 & 0xFFFFFFFF) >> 8) & 255)) ^ (v11 >> 31)) - v11)) - (((((((v7 & 255) - v4) ^ (v4 >> 31)) - v4) + (((((v7 & 0xFFFFFFFF) >> 24) - v8) ^ (v4 >> 31)) - v4)) + ((((((v7 & 0xFFFFFFFF) >> 8) & 255) - v9) ^ (v4 >> 31)) - v4)) + ((((((v7 & 0xFFFFFFFF) >> 16) & 255) - (((v6 & 0xFFFFFFFF) >> 16) & 255)) ^ (v6 >> 31)) - v6))) + ((((((v5 & 0xFFFFFFFF) >> 16) & 255) - v7) ^ (v5 >> 31)) - v5)) <= 0) else v5) & -16711936) + (load32((arg0 + v12)) & -16711936)) & -16711936) | (((v5 & 16711935) + (v7 & 16711935)) & 16711935))
                store32((arg3 + (v10 << 2)), (((((load32((arg1 + v12)) if (((((((((v5 & 255) - (load32((v6 - 4)) & 255)) ^ (v8 >> 31)) - v8) + (((((v5 & 0xFFFFFFFF) >> 24) - ((v6 & 0xFFFFFFFF) >> 24)) ^ (v9 >> 31)) - v9)) + ((((((v5 & 0xFFFFFFFF) >> 8) & 255) - (((v6 & 0xFFFFFFFF) >> 8) & 255)) ^ (v11 >> 31)) - v11)) - (((((((v7 & 255) - v4) ^ (v4 >> 31)) - v4) + (((((v7 & 0xFFFFFFFF) >> 24) - v8) ^ (v4 >> 31)) - v4)) + ((((((v7 & 0xFFFFFFFF) >> 8) & 255) - v9) ^ (v4 >> 31)) - v4)) + ((((((v7 & 0xFFFFFFFF) >> 16) & 255) - (((v6 & 0xFFFFFFFF) >> 16) & 255)) ^ (v6 >> 31)) - v6))) + ((((((v5 & 0xFFFFFFFF) >> 16) & 255) - v7) ^ (v5 >> 31)) - v5)) <= 0) else v5) & -16711936) + (load32((arg0 + v12)) & -16711936)) & -16711936) | (((v5 & 16711935) + (v7 & 16711935)) & 16711935)))
                v10 = (v10 + 1)
                if ((v10 + 1) != arg2):
                    continue
                break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1049
# ----------------------------------------------------------
def func1049(arg0, arg1, arg2, arg3):
    if arg1:
        if (arg2 > 0):
            v4 = load32((arg3 - 4))
            while True:  # $label0
                v5 = (v7 << 2)
                v6 = (arg1 + v5)
                v8 = load32((arg1 + v5) + 4)
                v9 = load32(v6)
                v8 = (((((load32((arg1 + v5) + 4) ^ load32(v6)) & 0xFFFFFFFF) >> 1) & 2139062143) + (v8 & v9))
                v6 = load32((v6 - 4))
                v4 = (((((load32((v6 - 4)) ^ v4) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v6))
                v4 = ((((((((((load32((arg1 + v5) + 4) ^ load32(v6)) & 0xFFFFFFFF) >> 1) & 2139062143) + (v8 & v9)) ^ (((((load32((v6 - 4)) ^ v4) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v6))) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v8))
                v5 = load32((arg0 + v5))
                v4 = ((((((((((((((load32((arg1 + v5) + 4) ^ load32(v6)) & 0xFFFFFFFF) >> 1) & 2139062143) + (v8 & v9)) ^ (((((load32((v6 - 4)) ^ v4) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v6))) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v8)) & -16711936) + (load32((arg0 + v5)) & -16711936)) & -16711936) | (((v4 & 16711935) + (v5 & 16711935)) & 16711935))
                store32((arg3 + (v7 << 2)), ((((((((((((((load32((arg1 + v5) + 4) ^ load32(v6)) & 0xFFFFFFFF) >> 1) & 2139062143) + (v8 & v9)) ^ (((((load32((v6 - 4)) ^ v4) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v6))) & 0xFFFFFFFF) >> 1) & 2139062143) + (v4 & v8)) & -16711936) + (load32((arg0 + v5)) & -16711936)) & -16711936) | (((v4 & 16711935) + (v5 & 16711935)) & 16711935)))
                v7 = (v7 + 1)
                if ((v7 + 1) != arg2):
                    continue
                break
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func1050
# ----------------------------------------------------------
def func1050(arg0, arg1, arg2, arg3):
    while True:  # $label0
        if (arg2 <= 0):
            break
        arg1 = 0
        if (arg2 != 1):
            v6 = (arg2 & -2)
            while True:  # $label1
                v4 = (arg1 << 2)
                store32((arg3 + (arg1 << 2)), (load32((arg0 + v4)) - 16777216))
                v4 = (v4 | 4)
                store32((arg3 + (v4 | 4)), (load32((arg0 + v4)) - 16777216))
                arg1 = (arg1 + 2)
                v5 = (v5 + 2)
                if ((v5 + 2) != v6):
                    continue
                break
        if not (arg2 & 1):
            break
        arg1 = (arg1 << 2)
        store32((arg3 + (arg1 << 2)), (load32((arg0 + arg1)) - 16777216))
        break

# ----------------------------------------------------------
# $func1051
# ----------------------------------------------------------
def func1051(arg0, arg1, arg2, arg3, arg4, arg5):
    if (arg3 > 0):
        while True:  # $label0
            store32((arg5 + (v7 << 2)), ((load8u((arg2 + v6)) | ((load8u((arg0 + v6)) << 16) | (load8u((arg1 + v6)) << 8))) | -16777216))
            v6 = (arg4 + v6)
            v7 = (v7 + 1)
            if ((v7 + 1) != arg3):
                continue
            break

# ----------------------------------------------------------
# $func1053
# ----------------------------------------------------------
def func1053(arg0, arg1, arg2, arg3, arg4, arg5):
    while True:  # $label0
        if (arg3 >= arg4):
            break
        if (arg5 <= 0):
            break
        v7 = (arg5 & -4)
        v6 = (arg5 & 3)
        v8 = (u32(arg5) < u32(4))
        while True:  # $label3
            arg5 = 0
            if not v8:
                while True:  # $label1
                    store8(arg2, ((load32((arg1 + (load8u(arg0) << 2))) & 0xFFFFFFFF) >> 8))
                    store8(arg2 + 1, ((load32((arg1 + (load8u(arg0 + 1) << 2))) & 0xFFFFFFFF) >> 8))
                    store8(arg2 + 2, ((load32((arg1 + (load8u(arg0 + 2) << 2))) & 0xFFFFFFFF) >> 8))
                    store8(arg2 + 3, ((load32((arg1 + (load8u(arg0 + 3) << 2))) & 0xFFFFFFFF) >> 8))
                    arg2 = (arg2 + 4)
                    arg0 = (arg0 + 4)
                    arg5 = (arg5 + 4)
                    if ((arg5 + 4) != v7):
                        continue
                    break
            arg5 = 0
            if v6:
                while True:  # $label2
                    store8(arg2, ((load32((arg1 + (load8u(arg0) << 2))) & 0xFFFFFFFF) >> 8))
                    arg2 = (arg2 + 1)
                    arg0 = (arg0 + 1)
                    arg5 = (arg5 + 1)
                    if ((arg5 + 1) != v6):
                        continue
                    break
            arg3 = (arg3 + 1)
            if ((arg3 + 1) != arg4):
                continue
            break
        break

# ----------------------------------------------------------
# $func1054
# ----------------------------------------------------------
def func1054(arg0, arg1, arg2, arg3, arg4, arg5):
    while True:  # $label0
        if (arg3 >= arg4):
            break
        if (arg5 <= 0):
            break
        v7 = (arg5 & -4)
        v6 = (arg5 & 3)
        v8 = (u32(arg5) < u32(4))
        while True:  # $label3
            arg5 = 0
            if not v8:
                while True:  # $label1
                    store32(arg2, load32((arg1 + (((load32(arg0) & 0xFFFFFFFF) >> 6) & 1020))))
                    store32(arg2 + 4, load32((arg1 + (((load32(arg0 + 4) & 0xFFFFFFFF) >> 6) & 1020))))
                    store32(arg2 + 8, load32((arg1 + (((load32(arg0 + 8) & 0xFFFFFFFF) >> 6) & 1020))))
                    store32(arg2 + 12, load32((arg1 + (((load32(arg0 + 12) & 0xFFFFFFFF) >> 6) & 1020))))
                    arg2 = (arg2 + 16)
                    arg0 = (arg0 + 16)
                    arg5 = (arg5 + 4)
                    if ((arg5 + 4) != v7):
                        continue
                    break
            arg5 = 0
            if v6:
                while True:  # $label2
                    store32(arg2, load32((arg1 + (((load32(arg0) & 0xFFFFFFFF) >> 6) & 1020))))
                    arg2 = (arg2 + 4)
                    arg0 = (arg0 + 4)
                    arg5 = (arg5 + 1)
                    if ((arg5 + 1) != v6):
                        continue
                    break
            arg3 = (arg3 + 1)
            if ((arg3 + 1) != arg4):
                continue
            break
        break

# ----------------------------------------------------------
# $func1055
# ----------------------------------------------------------
def func1055(arg0):
    v2 = load8u((arg0 - 29))
    v5 = (load8u((arg0 - 29)) + 2)
    v3 = load8u((arg0 - 31))
    v1 = load8u((arg0 - 30))
    v4 = (((((load8u((arg0 - 29)) + 2) + load8u((arg0 - 31))) + (load8u((arg0 - 30)) << 1)) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 32, (((((load8u((arg0 - 29)) + 2) + load8u((arg0 - 31))) + (load8u((arg0 - 30)) << 1)) & 0xFFFFFFFF) >> 2))
    v1 = (v1 + 2)
    store8(arg0, (((((v1 + 2) + load8u((arg0 - 32))) + (v3 << 1)) & 0xFFFFFFFF) >> 2))
    v3 = load8u((arg0 - 28))
    v1 = (((load8u((arg0 - 28)) + (v1 + (v2 << 1))) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 64, (((load8u((arg0 - 28)) + (v1 + (v2 << 1))) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 1, v4)
    store8(arg0 + 33, v1)
    v4 = load8u((arg0 - 27))
    v2 = (((load8u((arg0 - 27)) + (v5 + (v3 << 1))) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 96, (((load8u((arg0 - 27)) + (v5 + (v3 << 1))) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 2, v1)
    store8(arg0 + 65, v2)
    store8(arg0 + 34, v2)
    store8(arg0 + 3, v2)
    v2 = load8u((arg0 - 26))
    v3 = ((((load8u((arg0 - 26)) + (v3 + (v4 << 1))) + 2) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 97, ((((load8u((arg0 - 26)) + (v3 + (v4 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    v1 = load8u((arg0 - 25))
    v4 = ((((load8u((arg0 - 25)) + (v4 + (v2 << 1))) + 2) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 98, ((((load8u((arg0 - 25)) + (v4 + (v2 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 35, v3)
    store8(arg0 + 66, v3)
    store8(arg0 + 99, (((((v1 + v2) + (v1 << 1)) + 2) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 67, v4)

# ----------------------------------------------------------
# $func1057
# ----------------------------------------------------------
def func1057(arg0, arg1, arg2, arg3):
    if arg0:
    else:
    arg0 = 0
    while True:  # $label0
        if (arg3 <= 0):
            break
        v5 = (arg3 & 3)
        while True:  # $label1
            if (u32(arg3) < u32(4)):
                arg3 = 0
                break
            v8 = (arg3 & -4)
            arg3 = 0
            while True:  # $label2
                arg0 = (load8u((arg1 + arg3)) + arg0)
                store8((arg2 + arg3), (load8u((arg1 + arg3)) + arg0))
                v4 = (arg3 | 1)
                arg0 = (load8u((arg1 + v4)) + arg0)
                store8((arg2 + (arg3 | 1)), (load8u((arg1 + v4)) + arg0))
                v4 = (arg3 | 2)
                arg0 = (load8u((arg1 + v4)) + arg0)
                store8((arg2 + (arg3 | 2)), (load8u((arg1 + v4)) + arg0))
                v4 = (arg3 | 3)
                arg0 = (load8u((arg1 + v4)) + arg0)
                store8((arg2 + (arg3 | 3)), (load8u((arg1 + v4)) + arg0))
                arg3 = (arg3 + 4)
                v7 = (v7 + 4)
                if ((v7 + 4) != v8):
                    continue
                break
            break
        if not v5:
            break
        while True:  # $label3
            arg0 = (load8u((arg1 + arg3)) + arg0)
            store8((arg2 + arg3), (load8u((arg1 + arg3)) + arg0))
            arg3 = (arg3 + 1)
            v6 = (v6 + 1)
            if ((v6 + 1) != v5):
                continue
            break
        break
    return load8u(arg0)

# ----------------------------------------------------------
# $func1058
# ----------------------------------------------------------
def func1058(arg0, arg1, arg2, arg3, arg4):
    while True:  # $label4
        while True:  # $label3
            while True:  # $label2
                while True:  # $label1
                    while True:  # $label0
                        if arg0:
                            if not arg4:
                                break
                            if (arg0 == arg4):
                                break
                            if (arg1 <= 0):
                                break
                            if (arg2 <= 0):
                                break
                            if (arg1 > arg3):
                                break
                            store8(arg4, load8u(arg0))
                            while True:  # $label7
                                v5 = (arg1 - 1)
                                if (arg1 - 1):
                                    v7 = (arg4 + 1)
                                    v8 = (arg0 + 1)
                                    v10 = (v5 & 1)
                                    while True:  # $label5
                                        v12 = (arg1 - 2)
                                        if not (arg1 - 2):
                                            arg1 = 0
                                            break
                                        v11 = (v5 & -2)
                                        arg1 = 0
                                        while True:  # $label6
                                            store8((arg1 + v7), (load8u((arg1 + v8)) - load8u((arg0 + arg1))))
                                            v9 = (arg1 | 1)
                                            store8((v7 + (arg1 | 1)), (load8u((v8 + v9)) - load8u((arg0 + v9))))
                                            arg1 = (arg1 + 2)
                                            v6 = (v6 + 2)
                                            if ((v6 + 2) != v11):
                                                continue
                                            break
                                        break
                                    if v10:
                                        store8((arg1 + v7), (load8u((arg1 + v8)) - load8u((arg0 + arg1))))
                                    if (arg2 < 2):
                                        break
                                    v10 = (v5 & -2)
                                    v11 = (v5 & 1)
                                    v8 = 1
                                    while True:  # $label9
                                        arg4 = (arg3 + arg4)
                                        arg1 = (arg0 + arg3)
                                        store8((arg3 + arg4), (load8u((arg0 + arg3)) - load8u(arg0)))
                                        v5 = (arg4 + 1)
                                        v7 = (arg1 + 1)
                                        arg0 = 0
                                        v6 = 0
                                        if v12:
                                            while True:  # $label8
                                                store8((arg0 + v5), (load8u((arg0 + v7)) - load8u((arg0 + arg1))))
                                                v9 = (arg0 | 1)
                                                store8((v5 + (arg0 | 1)), (load8u((v7 + v9)) - load8u((arg1 + v9))))
                                                arg0 = (arg0 + 2)
                                                v6 = (v6 + 2)
                                                if ((v6 + 2) != v10):
                                                    continue
                                                break
                                        if v11:
                                            store8((arg0 + v5), (load8u((arg0 + v7)) - load8u((arg0 + arg1))))
                                        arg0 = arg1
                                        v8 = (v8 + 1)
                                        if ((v8 + 1) != arg2):
                                            continue
                                        break
                                    break
                                if (u32(arg2) < u32(2)):
                                    break
                                arg1 = (arg2 - 1)
                                v6 = ((arg2 - 1) & 3)
                                if (u32((arg2 - 2)) >= u32(3)):
                                    v5 = (arg1 & -4)
                                    arg1 = 0
                                    while True:  # $label10
                                        arg4 = (arg3 + arg4)
                                        arg2 = (arg0 + arg3)
                                        store8((arg3 + arg4), (load8u((arg0 + arg3)) - load8u(arg0)))
                                        arg4 = (arg3 + arg4)
                                        arg0 = (arg2 + arg3)
                                        store8((arg3 + arg4), (load8u((arg2 + arg3)) - load8u(arg2)))
                                        arg4 = (arg3 + arg4)
                                        arg2 = (arg0 + arg3)
                                        store8((arg3 + arg4), (load8u((arg0 + arg3)) - load8u(arg0)))
                                        arg4 = (arg3 + arg4)
                                        arg0 = (arg2 + arg3)
                                        store8((arg3 + arg4), (load8u((arg2 + arg3)) - load8u(arg2)))
                                        arg1 = (arg1 + 4)
                                        if ((arg1 + 4) != v5):
                                            continue
                                        break
                                if not v6:
                                    break
                                arg1 = 0
                                while True:  # $label11
                                    arg4 = (arg3 + arg4)
                                    arg2 = (arg0 + arg3)
                                    store8((arg3 + arg4), (load8u((arg0 + arg3)) - load8u(arg0)))
                                    arg0 = arg2
                                    arg1 = (arg1 + 1)
                                    if ((arg1 + 1) != v6):
                                        continue
                                    break
                                break
                            return
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

# ----------------------------------------------------------
# $func1059
# ----------------------------------------------------------
def func1059(arg0, arg1):
    while True:  # $label0
        if (arg1 <= 0):
            return 0
        arg1 = (arg1 - 1)
        v2 = load8u(arg0)
        arg0 = (arg0 + 1)
        if (v2 == 255):
            continue
        break
    return 1

# ----------------------------------------------------------
# $func1060
# ----------------------------------------------------------
def func1060(arg0, arg1):
    while True:  # $label0
        if (arg1 <= 0):
            break
        while True:  # $label1
            if (load8u((arg0 + v2)) == 255):
                v2 = (v2 + 4)
                v4 = (arg1 < 2)
                arg1 = (arg1 - 1)
                if not v4:
                    continue
                break
            break
        v3 = 1
        break
    return v3

# ----------------------------------------------------------
# $func1061
# ----------------------------------------------------------
def func1061(arg0):
    v1 = load8u(arg0 + 95)
    store8(arg0 + 99, load8u(arg0 + 95))
    store8(arg0 + 98, v1)
    store8(arg0 + 97, v1)
    store8(arg0 + 96, v1)
    v4 = load8u(arg0 + 31)
    v3 = (load8u(arg0 + 31) + 1)
    v2 = load8u(arg0 + 63)
    v5 = ((((load8u(arg0 + 31) + 1) + load8u(arg0 + 63)) & 0xFFFFFFFF) >> 1)
    store8(arg0 + 32, ((((load8u(arg0 + 31) + 1) + load8u(arg0 + 63)) & 0xFFFFFFFF) >> 1))
    v6 = load8u((arg0 - 1))
    store8(arg0, (((v3 + load8u((arg0 - 1))) & 0xFFFFFFFF) >> 1))
    v3 = ((((v1 + v2) + 1) & 0xFFFFFFFF) >> 1)
    store8(arg0 + 64, ((((v1 + v2) + 1) & 0xFFFFFFFF) >> 1))
    store8(arg0 + 2, v5)
    store8(arg0 + 34, v3)
    v3 = (((((v1 + v4) + (v2 << 1)) + 2) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 33, (((((v1 + v4) + (v2 << 1)) + 2) & 0xFFFFFFFF) >> 2))
    v2 = (v2 + 2)
    store8(arg0 + 1, ((((v6 + (v2 + 2)) + (v4 << 1)) & 0xFFFFFFFF) >> 2))
    v2 = ((((v1 + v2) + (v1 << 1)) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 65, ((((v1 + v2) + (v1 << 1)) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 3, v3)
    store8(arg0 + 35, v2)
    store8(arg0 + 67, v1)
    store8(arg0 + 66, v1)

# ----------------------------------------------------------
# $func1062
# ----------------------------------------------------------
def func1062(arg0, arg1, arg2, arg3, arg4, arg5):

# ----------------------------------------------------------
# $func1063
# ----------------------------------------------------------
def func1063(arg0, arg1, arg2, arg3, arg4, arg5):
    func137(arg0, 1, arg2, 8, arg3, arg4, arg5)
    func137(arg1, 1, arg2, 8, arg3, arg4, arg5)

# ----------------------------------------------------------
# $func1064
# ----------------------------------------------------------
def func1064(arg0, arg1, arg2, arg3, arg4):

# ----------------------------------------------------------
# $func1065
# ----------------------------------------------------------
def func1065(arg0, arg1, arg2, arg3, arg4):
    func137(arg0, 1, arg1, 16, arg2, arg3, arg4)

# ----------------------------------------------------------
# $func1066
# ----------------------------------------------------------
def func1066(arg0):
    store64(arg0 + 32, (load8u(arg0 + 31) * 72340172838076673))
    store64(arg0 + 64, (load8u(arg0 + 63) * 72340172838076673))
    store64(arg0 + 96, (load8u(arg0 + 95) * 72340172838076673))
    store64(arg0 + 128, (load8u(arg0 + 127) * 72340172838076673))
    store64(arg0 + 160, (load8u(arg0 + 159) * 72340172838076673))
    store64(arg0 + 192, (load8u(arg0 + 191) * 72340172838076673))
    store64(arg0 + 224, (load8u(arg0 + 223) * 72340172838076673))
    store64(arg0, (load8u((arg0 - 1)) * 72340172838076673))

# ----------------------------------------------------------
# $func1067
# ----------------------------------------------------------
def func1067(arg0):
    v2 = load8u(arg0 + 63)
    v3 = (load8u(arg0 + 63) + 2)
    v1 = load8u(arg0 + 95)
    store32(arg0 + 96, ((((((load8u(arg0 + 63) + 2) + load8u(arg0 + 95)) + (v1 << 1)) & 0xFFFFFFFF) >> 2) * 16843009))
    v4 = load8u(arg0 + 31)
    v5 = (load8u(arg0 + 31) + 2)
    store32(arg0 + 64, ((((v1 + ((load8u(arg0 + 31) + 2) + (v2 << 1))) & 0xFFFFFFFF) >> 2) * 16843009))
    v1 = load8u((arg0 - 1))
    store32(arg0 + 32, (((((v3 + load8u((arg0 - 1))) + (v4 << 1)) & 0xFFFFFFFF) >> 2) * 16843009))
    store32(arg0, (((((v5 + load8u((arg0 - 33))) + (v1 << 1)) & 0xFFFFFFFF) >> 2) * 16843009))

# ----------------------------------------------------------
# $func1068
# ----------------------------------------------------------
def func1068(arg0):
    v1 = (load8u(arg0 + 31) * 72340172838076673)
    store64(arg0 + 32, (load8u(arg0 + 31) * 72340172838076673))
    store64(arg0 + 40, v1)
    v1 = (load8u(arg0 + 63) * 72340172838076673)
    store64(arg0 + 64, (load8u(arg0 + 63) * 72340172838076673))
    store64(arg0 + 72, v1)
    v1 = (load8u(arg0 + 95) * 72340172838076673)
    store64(arg0 + 96, (load8u(arg0 + 95) * 72340172838076673))
    store64(arg0 + 104, v1)
    v1 = (load8u(arg0 + 127) * 72340172838076673)
    store64(arg0 + 128, (load8u(arg0 + 127) * 72340172838076673))
    store64(arg0 + 136, v1)
    v1 = (load8u(arg0 + 159) * 72340172838076673)
    store64(arg0 + 168, (load8u(arg0 + 159) * 72340172838076673))
    store64(arg0 + 160, v1)
    v1 = (load8u((arg0 - 1)) * 72340172838076673)
    store64(arg0, (load8u((arg0 - 1)) * 72340172838076673))
    store64(arg0 + 8, v1)
    v1 = (load8u(arg0 + 191) * 72340172838076673)
    store64(arg0 + 200, (load8u(arg0 + 191) * 72340172838076673))
    store64(arg0 + 192, v1)
    v1 = (load8u(arg0 + 223) * 72340172838076673)
    store64(arg0 + 232, (load8u(arg0 + 223) * 72340172838076673))
    store64(arg0 + 224, v1)
    v1 = (load8u(arg0 + 255) * 72340172838076673)
    store64(arg0 + 264, (load8u(arg0 + 255) * 72340172838076673))
    store64(arg0 + 256, v1)
    v1 = (load8u(arg0 + 287) * 72340172838076673)
    store64(arg0 + 296, (load8u(arg0 + 287) * 72340172838076673))
    store64(arg0 + 288, v1)
    v1 = (load8u(arg0 + 319) * 72340172838076673)
    store64(arg0 + 328, (load8u(arg0 + 319) * 72340172838076673))
    store64(arg0 + 320, v1)
    v1 = (load8u(arg0 + 351) * 72340172838076673)
    store64(arg0 + 360, (load8u(arg0 + 351) * 72340172838076673))
    store64(arg0 + 352, v1)
    v1 = (load8u(arg0 + 383) * 72340172838076673)
    store64(arg0 + 392, (load8u(arg0 + 383) * 72340172838076673))
    store64(arg0 + 384, v1)
    v1 = (load8u(arg0 + 415) * 72340172838076673)
    store64(arg0 + 424, (load8u(arg0 + 415) * 72340172838076673))
    store64(arg0 + 416, v1)
    v1 = (load8u(arg0 + 447) * 72340172838076673)
    store64(arg0 + 456, (load8u(arg0 + 447) * 72340172838076673))
    store64(arg0 + 448, v1)
    v1 = (load8u(arg0 + 479) * 72340172838076673)
    store64(arg0 + 488, (load8u(arg0 + 479) * 72340172838076673))
    store64(arg0 + 480, v1)

# ----------------------------------------------------------
# $func1069
# ----------------------------------------------------------
def func1069(arg0):
    v3 = load8u(arg0 + 31)
    v4 = load8u(arg0 + 63)
    v2 = ((((load8u(arg0 + 31) + load8u(arg0 + 63)) + 1) & 0xFFFFFFFF) >> 1)
    store8(arg0 + 98, ((((load8u(arg0 + 31) + load8u(arg0 + 63)) + 1) & 0xFFFFFFFF) >> 1))
    v7 = load8u(arg0 + 95)
    store8(arg0 + 96, ((((v4 + load8u(arg0 + 95)) + 1) & 0xFFFFFFFF) >> 1))
    store8(arg0 + 64, v2)
    v6 = load8u((arg0 - 1))
    v1 = (load8u((arg0 - 1)) + 1)
    v2 = load8u((arg0 - 33))
    v5 = ((((load8u((arg0 - 1)) + 1) + load8u((arg0 - 33))) & 0xFFFFFFFF) >> 1)
    store8(arg0 + 34, ((((load8u((arg0 - 1)) + 1) + load8u((arg0 - 33))) & 0xFFFFFFFF) >> 1))
    v1 = (((v1 + v3) & 0xFFFFFFFF) >> 1)
    store8(arg0 + 66, (((v1 + v3) & 0xFFFFFFFF) >> 1))
    store8(arg0, v5)
    store8(arg0 + 32, v1)
    v1 = load8u((arg0 - 32))
    v5 = (v6 + 2)
    v8 = (((load8u((arg0 - 32)) + ((v6 + 2) + (v2 << 1))) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 35, (((load8u((arg0 - 32)) + ((v6 + 2) + (v2 << 1))) & 0xFFFFFFFF) >> 2))
    v9 = load8u((arg0 - 31))
    store8(arg0 + 3, ((((load8u((arg0 - 30)) + (v1 + (load8u((arg0 - 31)) << 1))) + 2) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 2, ((((v9 + (v2 + (v1 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    v1 = (v3 + 2)
    v2 = (((v2 + ((v3 + 2) + (v6 << 1))) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 67, (((v2 + ((v3 + 2) + (v6 << 1))) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 1, v8)
    v3 = ((((v4 + v5) + (v3 << 1)) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 99, ((((v4 + v5) + (v3 << 1)) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 33, v2)
    store8(arg0 + 97, ((((v1 + v7) + (v4 << 1)) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 65, v3)

# ----------------------------------------------------------
# $func1070
# ----------------------------------------------------------
def func1070(arg0, arg1, arg2, arg3):
    while True:  # $label0
        if not arg0:
            if (arg3 <= 0):
                break
            arg0 = (arg3 & 3)
            if (u32(arg3) >= u32(4)):
                v8 = (arg3 & -4)
                arg3 = 0
                while True:  # $label1
                    v5 = (load8u((arg1 + v4)) + v5)
                    store8((arg2 + v4), (load8u((arg1 + v4)) + v5))
                    v7 = (v4 | 1)
                    v5 = (load8u((arg1 + v7)) + v5)
                    store8((arg2 + (v4 | 1)), (load8u((arg1 + v7)) + v5))
                    v7 = (v4 | 2)
                    v5 = (load8u((arg1 + v7)) + v5)
                    store8((arg2 + (v4 | 2)), (load8u((arg1 + v7)) + v5))
                    v7 = (v4 | 3)
                    v5 = (load8u((arg1 + v7)) + v5)
                    store8((arg2 + (v4 | 3)), (load8u((arg1 + v7)) + v5))
                    v4 = (v4 + 4)
                    arg3 = (arg3 + 4)
                    if ((arg3 + 4) != v8):
                        continue
                    break
            if not arg0:
                break
            while True:  # $label2
                v5 = (load8u((arg1 + v4)) + v5)
                store8((arg2 + v4), (load8u((arg1 + v4)) + v5))
                v4 = (v4 + 1)
                v6 = (v6 + 1)
                if ((v6 + 1) != arg0):
                    continue
                break
            break
        if (arg3 <= 0):
            break
        v5 = load8u(arg0)
        v6 = load8u(arg0)
        while True:  # $label3
            v6 = load8u((arg0 + v4))
            v5 = (((v5 & 255) - (v6 & 255)) + load8u((arg0 + v4)))
            v5 = ((((v5 & 255) - (v6 & 255)) + load8u((arg0 + v4))) if (v5 > 0) else 0)
            v5 = (load8u((arg1 + v4)) + (255 if (v5 >= 255) else ((((v5 & 255) - (v6 & 255)) + load8u((arg0 + v4))) if (v5 > 0) else 0)))
            store8((arg2 + v4), (load8u((arg1 + v4)) + (255 if (v5 >= 255) else ((((v5 & 255) - (v6 & 255)) + load8u((arg0 + v4))) if (v5 > 0) else 0))))
            v4 = (v4 + 1)
            if ((v4 + 1) != arg3):
                continue
            break
        break

# ----------------------------------------------------------
# $func1071
# ----------------------------------------------------------
def func1071(arg0, arg1, arg2, arg3, arg4):
    while True:  # $label4
        while True:  # $label3
            while True:  # $label2
                while True:  # $label1
                    while True:  # $label0
                        if arg0:
                            if not arg4:
                                break
                            if (arg0 == arg4):
                                break
                            if (arg1 <= 0):
                                break
                            if (arg2 <= 0):
                                break
                            if (arg1 > arg3):
                                break
                            store8(arg4, load8u(arg0))
                            while True:  # $label6
                                while True:  # $label7
                                    v9 = (arg1 - 1)
                                    if (arg1 - 1):
                                        v6 = (arg4 + 1)
                                        v8 = (arg0 + 1)
                                        if (arg1 != 2):
                                            v11 = (v9 & -2)
                                            while True:  # $label5
                                                store8((v5 + v6), (load8u((v5 + v8)) - load8u((arg0 + v5))))
                                                v10 = (v5 | 1)
                                                store8((v6 + (v5 | 1)), (load8u((v8 + v10)) - load8u((arg0 + v10))))
                                                v5 = (v5 + 2)
                                                v7 = (v7 + 2)
                                                if ((v7 + 2) != v11):
                                                    continue
                                                break
                                        if (v9 & 1):
                                            store8((v5 + v6), (load8u((v5 + v8)) - load8u((arg0 + v5))))
                                        v9 = 1
                                        if (arg2 <= 1):
                                            break
                                        v8 = (0 - arg3)
                                        v7 = (arg3 + arg4)
                                        v6 = (arg0 + arg3)
                                        if (arg1 <= 1):
                                            break
                                        while True:  # $label9
                                            arg0 = load8u(v6)
                                            store8(v7, (load8u(v6) - load8u((v6 + v8))))
                                            v5 = 1
                                            while True:  # $label8
                                                arg4 = (arg0 & 255)
                                                arg0 = load8u((v5 + v6))
                                                v10 = (v6 + (v5 - arg3))
                                                arg4 = ((arg4 + load8u((v6 + (v5 - arg3)))) - load8u((v10 - 1)))
                                                arg4 = (((arg4 + load8u((v6 + (v5 - arg3)))) - load8u((v10 - 1))) if (arg4 > 0) else 0)
                                                store8((v5 + v7), (load8u((v5 + v6)) - (255 if (arg4 >= 255) else (((arg4 + load8u((v6 + (v5 - arg3)))) - load8u((v10 - 1))) if (arg4 > 0) else 0))))
                                                v5 = (v5 + 1)
                                                if ((v5 + 1) != arg1):
                                                    continue
                                                break
                                            v7 = (arg3 + v7)
                                            v6 = (arg3 + v6)
                                            v9 = (v9 + 1)
                                            if ((v9 + 1) != arg2):
                                                continue
                                            break
                                        break
                                    if (u32(arg2) < u32(2)):
                                        break
                                    v8 = (0 - arg3)
                                    v7 = (arg3 + arg4)
                                    break
                                v6 = (arg0 + arg3)
                                arg0 = (arg2 - 1)
                                arg4 = ((arg2 - 1) & 1)
                                if (arg2 != 2):
                                    arg2 = (arg0 & -2)
                                    arg0 = 0
                                    while True:  # $label10
                                        store8(v7, (load8u(v6) - load8u((v6 + v8))))
                                        v5 = (arg3 + v7)
                                        arg1 = (arg3 + v6)
                                        store8((arg3 + v7), (load8u((arg3 + v6)) - load8u((arg1 + v8))))
                                        v7 = (arg3 + v5)
                                        v6 = (arg1 + arg3)
                                        arg0 = (arg0 + 2)
                                        if ((arg0 + 2) != arg2):
                                            continue
                                        break
                                if not arg4:
                                    break
                                store8(v7, (load8u(v6) - load8u((v6 + v8))))
                                break
                            return
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
    return 7251

# ----------------------------------------------------------
# $func1072
# ----------------------------------------------------------
def func1072(arg0, arg1, arg2, arg3, arg4, arg5):
    while True:  # $label1
        while True:  # $label3
            if (arg4 <= 15):
                v13 = (load32((arg1 + (arg4 << 2))) + (arg2 * 11))
                arg2 = load32(arg0 + 12)
                v8 = load32(arg0 + 8)
                while True:  # $label11
                    v10 = load8u(v13)
                    while True:  # $label0
                        if (arg2 >= 0):
                            break
                        v9 = load32(arg0 + 16)
                        if not load32(arg0 + 16):
                            break
                        if (u32(load32(arg0 + 24)) > u32(v9)):
                            v6 = load64(v9)
                            store32(arg0 + 16, (v9 + 7))
                            store64(arg0, ((load64(arg0) << 56) | ((((((v6 << 56) | ((v6 & 65280) << 40)) | (((v6 & 16711680) << 24) | ((v6 & 4278190080) << 8))) | ((((v6 & 0xFFFFFFFF) >> 40) & 65280) | ((((v6 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v6 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                            arg2 = (arg2 + 56)
                            break
                        func36(arg0)
                        arg2 = load32(arg0 + 12)
                        break
                    while True:  # $label2
                        v9 = (((v8 * v10) & 0xFFFFFFFF) >> 8)
                        v6 = load64(arg0)
                        v7 = i32(arg2)
                        v10 = (u32((((v8 * v10) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(arg0) & 0xFFFFFFFF) >> i32(arg2)))))
                        if not (u32((((v8 * v10) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(arg0) & 0xFFFFFFFF) >> i32(arg2))))):
                            v6 = (v6 - (i32((v9 + 1)) << v7))
                            store64(arg0, (v6 - (i32((v9 + 1)) << v7)))
                            break
                        break
                    v8 = (v9 + 1)
                    v9 = (clz((v9 + 1)) ^ 24)
                    arg2 = ((v8 - v9) - (clz((v9 + 1)) ^ 24))
                    store32(arg2 + 12, ((v8 - v9) - (clz((v9 + 1)) ^ 24)))
                    v11 = ((v8 << v9) - 1)
                    store32(arg0 + 8, ((v8 << v9) - 1))
                    v9 = arg4
                    v8 = arg4
                    if v10:
                        break
                    while True:  # $label6
                        v8 = load8u(v13 + 1)
                        while True:  # $label4
                            if (arg2 >= 0):
                                break
                            arg4 = load32(arg0 + 16)
                            if not load32(arg0 + 16):
                                break
                            if (u32(load32(arg0 + 24)) > u32(arg4)):
                                v7 = load64(arg4)
                                store32(arg0 + 16, (arg4 + 7))
                                v6 = ((v6 << 56) | ((((((v7 << 56) | ((v7 & 65280) << 40)) | (((v7 & 16711680) << 24) | ((v7 & 4278190080) << 8))) | ((((v7 & 0xFFFFFFFF) >> 40) & 65280) | ((((v7 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v7 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                store64(arg0, ((v6 << 56) | ((((((v7 << 56) | ((v7 & 65280) << 40)) | (((v7 & 16711680) << 24) | ((v7 & 4278190080) << 8))) | ((((v7 & 0xFFFFFFFF) >> 40) & 65280) | ((((v7 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v7 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                arg2 = (arg2 + 56)
                                break
                            func36(arg0)
                            v6 = load64(arg0)
                            arg2 = load32(arg0 + 12)
                            break
                        while True:  # $label5
                            v8 = (((v8 * v11) & 0xFFFFFFFF) >> 8)
                            v7 = i32(arg2)
                            v12 = i32(((v6 & 0xFFFFFFFF) >> i32(arg2)))
                            if (u32((((v8 * v11) & 0xFFFFFFFF) >> 8)) < u32(i32(((v6 & 0xFFFFFFFF) >> i32(arg2))))):
                                v6 = (v6 - (i32((v8 + 1)) << v7))
                                store64(arg0, (v6 - (i32((v8 + 1)) << v7)))
                                break
                            break
                        arg4 = (v8 + 1)
                        v10 = (clz((v8 + 1)) ^ 24)
                        arg2 = ((v11 - v8) - (clz((v8 + 1)) ^ 24))
                        store32(arg2 + 12, ((v11 - v8) - (clz((v8 + 1)) ^ 24)))
                        v11 = ((arg4 << v10) - 1)
                        store32(arg0 + 8, ((arg4 << v10) - 1))
                        arg4 = (v9 + 1)
                        v10 = load32((arg1 + ((v9 + 1) << 2)))
                        if (u32(v8) >= u32(v12)):
                            v8 = 16
                            v13 = v10
                            v9 = arg4
                            if (arg4 != 16):
                                continue
                            break
                        break
                    v12 = load8u(v13 + 2)
                    while True:  # $label7
                        if (arg2 >= 0):
                            break
                        v8 = load32(arg0 + 16)
                        if not load32(arg0 + 16):
                            break
                        if (u32(load32(arg0 + 24)) > u32(v8)):
                            v7 = load64(v8)
                            store32(arg0 + 16, (v8 + 7))
                            v6 = ((v6 << 56) | ((((((v7 << 56) | ((v7 & 65280) << 40)) | (((v7 & 16711680) << 24) | ((v7 & 4278190080) << 8))) | ((((v7 & 0xFFFFFFFF) >> 40) & 65280) | ((((v7 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v7 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                            store64(arg0, ((v6 << 56) | ((((((v7 << 56) | ((v7 & 65280) << 40)) | (((v7 & 16711680) << 24) | ((v7 & 4278190080) << 8))) | ((((v7 & 0xFFFFFFFF) >> 40) & 65280) | ((((v7 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v7 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                            arg2 = (arg2 + 56)
                            break
                        func36(arg0)
                        v6 = load64(arg0)
                        arg2 = load32(arg0 + 12)
                        break
                    while True:  # $label8
                        v12 = (((v11 * v12) & 0xFFFFFFFF) >> 8)
                        v7 = i32(arg2)
                        v14 = i32(((v6 & 0xFFFFFFFF) >> i32(arg2)))
                        if (u32((((v11 * v12) & 0xFFFFFFFF) >> 8)) < u32(i32(((v6 & 0xFFFFFFFF) >> i32(arg2))))):
                            store64(arg0, (v6 - (i32((v12 + 1)) << v7)))
                            break
                        break
                    v11 = (v12 + 1)
                    arg2 = (clz((v12 + 1)) ^ 24)
                    v8 = ((v11 - v12) - (clz((v12 + 1)) ^ 24))
                    store32(arg2 + 12, ((v11 - v12) - (clz((v12 + 1)) ^ 24)))
                    store32(arg0 + 8, ((v11 << arg2) - 1))
                    while True:  # $label9
                        if (u32(v12) >= u32(v14)):
                            v11 = 1
                            break
                        v11 = func463(arg0, v13)
                        v8 = load32(arg0 + 12)
                        break
                    v13 = (v10 + 22)
                    while True:  # $label10
                        if (v8 >= 0):
                            break
                        arg2 = load32(arg0 + 16)
                        if not load32(arg0 + 16):
                            break
                        if (u32(load32(arg0 + 24)) > u32(arg2)):
                            v6 = load64(arg2)
                            store32(arg0 + 16, (arg2 + 7))
                            store64(arg0, ((load64(arg0) << 56) | ((((((v6 << 56) | ((v6 & 65280) << 40)) | (((v6 & 16711680) << 24) | ((v6 & 4278190080) << 8))) | ((((v6 & 0xFFFFFFFF) >> 40) & 65280) | ((((v6 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v6 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                            v8 = (v8 + 56)
                            break
                        func36(arg0)
                        v8 = load32(arg0 + 12)
                        break
                    arg2 = (v8 - 1)
                    store32(arg0 + 12, (v8 - 1))
                    v12 = load32(arg0 + 8)
                    v14 = ((load32(arg0 + 8) & 0xFFFFFFFF) >> 1)
                    v6 = load64(arg0)
                    v7 = i32(v8)
                    v10 = ((((load32(arg0 + 8) & 0xFFFFFFFF) >> 1) - i32(((load64(arg0) & 0xFFFFFFFF) >> i32(v8)))) >> 31)
                    v8 = ((((((load32(arg0 + 8) & 0xFFFFFFFF) >> 1) - i32(((load64(arg0) & 0xFFFFFFFF) >> i32(v8)))) >> 31) + v12) | 1)
                    store32(arg0 + 8, ((((((load32(arg0 + 8) & 0xFFFFFFFF) >> 1) - i32(((load64(arg0) & 0xFFFFFFFF) >> i32(v8)))) >> 31) + v12) | 1))
                    store64(arg0, (v6 - (i32((v10 & (v14 + 1))) << v7)))
                    store16((arg5 + (load8u((v9 + 13968)) << 1)), (load32((arg3 + ((v9 > 0) << 2))) * ((v10 ^ v11) - v10)))
                    if (v9 < 15):
                        continue
                    break
            v8 = 16
            break
        return v8
        break
    a_c()
    raise Unreachable()
    return 3339

# ----------------------------------------------------------
# $func1073
# ----------------------------------------------------------
def func1073(arg0, arg1, arg2, arg3, arg4, arg5):
    while True:  # $label1
        while True:  # $label2
            if (arg4 <= 15):
                v13 = (load32((arg1 + (arg4 << 2))) + (arg2 * 11))
                v9 = load32(arg0 + 12)
                v8 = load32(arg0 + 8)
                while True:  # $label9
                    v11 = load8u(v13)
                    while True:  # $label0
                        if (v9 >= 0):
                            break
                        arg2 = load32(arg0 + 16)
                        if not load32(arg0 + 16):
                            break
                        if (u32(load32(arg0 + 24)) > u32(arg2)):
                            v6 = load64(arg2)
                            store32(arg0 + 16, (arg2 + 7))
                            v9 = (v9 + 56)
                            store32(arg0 + 12, (v9 + 56))
                            store64(arg0, ((load64(arg0) << 56) | ((((((v6 << 56) | ((v6 & 65280) << 40)) | (((v6 & 16711680) << 24) | ((v6 & 4278190080) << 8))) | ((((v6 & 0xFFFFFFFF) >> 40) & 65280) | ((((v6 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v6 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                            break
                        func36(arg0)
                        v9 = load32(arg0 + 12)
                        break
                    arg2 = (((v8 * v11) & 0xFFFFFFFF) >> 8)
                    v6 = load64(arg0)
                    v7 = i32(v9)
                    v12 = (u32((((v8 * v11) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(arg0) & 0xFFFFFFFF) >> i32(v9)))))
                    if not (u32((((v8 * v11) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(arg0) & 0xFFFFFFFF) >> i32(v9))))):
                        arg2 = (arg2 + 1)
                        v6 = (v6 - (i32((arg2 + 1)) << v7))
                        store64(arg0, (v6 - (i32((arg2 + 1)) << v7)))
                        arg2 = (v8 - arg2)
                    if (u32(arg2) <= u32(126)):
                        v9 = (v9 - load8u((arg2 + 17632)))
                        store32(arg0 + 12, (v9 - load8u((arg2 + 17632))))
                        arg2 = load8u((arg2 + 17760))
                    store32(arg0 + 8, arg2)
                    v11 = arg4
                    v8 = arg4
                    if v12:
                        break
                    while True:  # $label5
                        v8 = load8u(v13 + 1)
                        while True:  # $label3
                            if (v9 >= 0):
                                break
                            arg4 = load32(arg0 + 16)
                            if not load32(arg0 + 16):
                                break
                            if (u32(load32(arg0 + 24)) > u32(arg4)):
                                v7 = load64(arg4)
                                v9 = (v9 + 56)
                                store32(arg0 + 12, (v9 + 56))
                                store32(arg0 + 16, (arg4 + 7))
                                v6 = ((v6 << 56) | ((((((v7 << 56) | ((v7 & 65280) << 40)) | (((v7 & 16711680) << 24) | ((v7 & 4278190080) << 8))) | ((((v7 & 0xFFFFFFFF) >> 40) & 65280) | ((((v7 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v7 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                store64(arg0, ((v6 << 56) | ((((((v7 << 56) | ((v7 & 65280) << 40)) | (((v7 & 16711680) << 24) | ((v7 & 4278190080) << 8))) | ((((v7 & 0xFFFFFFFF) >> 40) & 65280) | ((((v7 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v7 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                break
                            func36(arg0)
                            v6 = load64(arg0)
                            v9 = load32(arg0 + 12)
                            break
                        while True:  # $label4
                            v8 = (((arg2 * v8) & 0xFFFFFFFF) >> 8)
                            v7 = i32(v9)
                            v10 = i32(((v6 & 0xFFFFFFFF) >> i32(v9)))
                            if (u32((((arg2 * v8) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v6 & 0xFFFFFFFF) >> i32(v9))))):
                                break
                            arg4 = (v8 + 1)
                            v6 = (v6 - (i32((v8 + 1)) << v7))
                            store64(arg0, (v6 - (i32((v8 + 1)) << v7)))
                            break
                        arg2 = (arg2 - arg4)
                        if (u32((arg2 - arg4)) <= u32(126)):
                            v9 = (v9 - load8u((arg2 + 17632)))
                            store32(arg0 + 12, (v9 - load8u((arg2 + 17632))))
                            arg2 = load8u((arg2 + 17760))
                        store32(arg0 + 8, arg2)
                        arg4 = (v11 + 1)
                        v12 = load32((arg1 + ((v11 + 1) << 2)))
                        if (u32(v8) >= u32(v10)):
                            v8 = 16
                            v13 = v12
                            v11 = arg4
                            if (arg4 != 16):
                                continue
                            break
                        break
                    v10 = load8u(v13 + 2)
                    while True:  # $label6
                        if (v9 >= 0):
                            break
                        v8 = load32(arg0 + 16)
                        if not load32(arg0 + 16):
                            break
                        if (u32(load32(arg0 + 24)) > u32(v8)):
                            v7 = load64(v8)
                            v9 = (v9 + 56)
                            store32(arg0 + 12, (v9 + 56))
                            store32(arg0 + 16, (v8 + 7))
                            v6 = ((v6 << 56) | ((((((v7 << 56) | ((v7 & 65280) << 40)) | (((v7 & 16711680) << 24) | ((v7 & 4278190080) << 8))) | ((((v7 & 0xFFFFFFFF) >> 40) & 65280) | ((((v7 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v7 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                            store64(arg0, ((v6 << 56) | ((((((v7 << 56) | ((v7 & 65280) << 40)) | (((v7 & 16711680) << 24) | ((v7 & 4278190080) << 8))) | ((((v7 & 0xFFFFFFFF) >> 40) & 65280) | ((((v7 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v7 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                            break
                        func36(arg0)
                        v6 = load64(arg0)
                        v9 = load32(arg0 + 12)
                        break
                    v10 = (((arg2 * v10) & 0xFFFFFFFF) >> 8)
                    v8 = (((arg2 * v10) & 0xFFFFFFFF) >> 8)
                    v7 = i32(v9)
                    v14 = i32(((v6 & 0xFFFFFFFF) >> i32(v9)))
                    if (u32(i32(((v6 & 0xFFFFFFFF) >> i32(v9)))) > u32(v10)):
                        v8 = (v10 + 1)
                        store64(arg0, (v6 - (i32((v10 + 1)) << v7)))
                        v8 = (arg2 - v8)
                    if (u32(v8) <= u32(126)):
                        v9 = (v9 - load8u((v8 + 17632)))
                        store32(arg0 + 12, (v9 - load8u((v8 + 17632))))
                    else:
                    store32(load8u((v8 + 17760)) + 8, v8)
                    while True:  # $label7
                        if (u32(v10) >= u32(v14)):
                            v10 = 1
                            break
                        v10 = func463(arg0, v13)
                        v9 = load32(arg0 + 12)
                        break
                    v13 = (v12 + 22)
                    while True:  # $label8
                        if (v9 >= 0):
                            break
                        arg2 = load32(arg0 + 16)
                        if not load32(arg0 + 16):
                            break
                        if (u32(load32(arg0 + 24)) > u32(arg2)):
                            v6 = load64(arg2)
                            store32(arg0 + 16, (arg2 + 7))
                            store64(arg0, ((load64(arg0) << 56) | ((((((v6 << 56) | ((v6 & 65280) << 40)) | (((v6 & 16711680) << 24) | ((v6 & 4278190080) << 8))) | ((((v6 & 0xFFFFFFFF) >> 40) & 65280) | ((((v6 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v6 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                            break
                        func36(arg0)
                        break
                    arg2 = load32(arg0 + 12)
                    v9 = (load32(arg0 + 12) - 1)
                    store32((v9 + 56) + 12, (load32(arg0 + 12) - 1))
                    v8 = load32(arg0 + 8)
                    v12 = ((load32(arg0 + 8) & 0xFFFFFFFF) >> 1)
                    v6 = load64(arg0)
                    v7 = i32(arg2)
                    arg2 = ((((load32(arg0 + 8) & 0xFFFFFFFF) >> 1) - i32(((load64(arg0) & 0xFFFFFFFF) >> i32(arg2)))) >> 31)
                    v8 = ((((((load32(arg0 + 8) & 0xFFFFFFFF) >> 1) - i32(((load64(arg0) & 0xFFFFFFFF) >> i32(arg2)))) >> 31) + v8) | 1)
                    store32(arg0 + 8, ((((((load32(arg0 + 8) & 0xFFFFFFFF) >> 1) - i32(((load64(arg0) & 0xFFFFFFFF) >> i32(arg2)))) >> 31) + v8) | 1))
                    store64(arg0, (v6 - (i32((arg2 & (v12 + 1))) << v7)))
                    store16((arg5 + (load8u((v11 + 13968)) << 1)), (load32((arg3 + ((v11 > 0) << 2))) * ((arg2 ^ v10) - arg2)))
                    if (v11 < 15):
                        continue
                    break
            v8 = 16
            break
        return v8
        break
    a_c()
    raise Unreachable()
    return 3339

# ----------------------------------------------------------
# $func1074
# ----------------------------------------------------------
def func1074(arg0, arg1, arg2):
    while True:  # $label0
        if (arg2 <= 0):
            break
        v5 = (arg2 & 3)
        if (u32(arg2) >= u32(4)):
            v7 = (arg2 & -4)
            arg2 = 0
            while True:  # $label1
                store8((arg1 + v3), ((load32((arg0 + (v3 << 2))) & 0xFFFFFFFF) >> 8))
                v4 = (v3 | 1)
                store8((arg1 + (v3 | 1)), ((load32((arg0 + (v4 << 2))) & 0xFFFFFFFF) >> 8))
                v4 = (v3 | 2)
                store8((arg1 + (v3 | 2)), ((load32((arg0 + (v4 << 2))) & 0xFFFFFFFF) >> 8))
                v4 = (v3 | 3)
                store8((arg1 + (v3 | 3)), ((load32((arg0 + (v4 << 2))) & 0xFFFFFFFF) >> 8))
                v3 = (v3 + 4)
                arg2 = (arg2 + 4)
                if ((arg2 + 4) != v7):
                    continue
                break
        if not v5:
            break
        while True:  # $label2
            store8((arg1 + v3), ((load32((arg0 + (v3 << 2))) & 0xFFFFFFFF) >> 8))
            v3 = (v3 + 1)
            v6 = (v6 + 1)
            if ((v6 + 1) != v5):
                continue
            break
        break

# ----------------------------------------------------------
# $func1075
# ----------------------------------------------------------
def func1075(arg0, arg1, arg2, arg3, arg4, arg5):
    v6 = 1
    while True:  # $label0
        if (arg3 <= 0):
            break
        if (arg2 <= 0):
            break
        v14 = (arg2 & -4)
        v12 = (arg2 & 3)
        v6 = 255
        v15 = (u32(arg2) < u32(4))
        while True:  # $label3
            arg2 = 0
            v7 = 0
            if not v15:
                while True:  # $label1
                    v8 = load8u((arg0 + (arg2 << 2)))
                    store8((arg2 + arg4), load8u((arg0 + (arg2 << 2))))
                    v9 = (arg2 | 1)
                    v9 = load8u((arg0 + (v9 << 2)))
                    store8((arg4 + (arg2 | 1)), load8u((arg0 + (v9 << 2))))
                    v10 = (arg2 | 2)
                    v10 = load8u((arg0 + (v10 << 2)))
                    store8((arg4 + (arg2 | 2)), load8u((arg0 + (v10 << 2))))
                    v11 = (arg2 | 3)
                    v11 = load8u((arg0 + (v11 << 2)))
                    store8((arg4 + (arg2 | 3)), load8u((arg0 + (v11 << 2))))
                    v6 = (v11 & (v10 & (v9 & (v6 & v8))))
                    arg2 = (arg2 + 4)
                    v7 = (v7 + 4)
                    if ((v7 + 4) != v14):
                        continue
                    break
            v7 = 0
            if v12:
                while True:  # $label2
                    v8 = load8u((arg0 + (arg2 << 2)))
                    store8((arg2 + arg4), load8u((arg0 + (arg2 << 2))))
                    arg2 = (arg2 + 1)
                    v6 = (v6 & v8)
                    v7 = (v7 + 1)
                    if ((v7 + 1) != v12):
                        continue
                    break
            arg4 = (arg4 + arg5)
            arg0 = (arg0 + arg1)
            v13 = (v13 + 1)
            if ((v13 + 1) != arg3):
                continue
            break
        v6 = ((v6 & 255) == 255)
        break
    return v6

# ----------------------------------------------------------
# $func1076
# ----------------------------------------------------------
def func1076(arg0, arg1):
    while True:  # $label6
        while True:  # $label3
            if (arg1 <= load32(load32(arg0 + 8) + 88)):
                while True:  # $label0
                    v3 = load32(arg0 + 108)
                    v12 = (arg1 - load32(arg0 + 108))
                    if ((arg1 - load32(arg0 + 108)) <= 0):
                        v7 = v3
                        break
                    v2 = load32(arg0 + 100)
                    v11 = (load32(arg0 + 16) + ((v3 * load32(arg0 + 100)) << 2))
                    while True:  # $label5
                        v8 = (16 if (v12 >= 16) else v12)
                        v7 = ((16 if (v12 >= 16) else v12) + v3)
                        v5 = load32(arg0 + 8)
                        v6 = load32(load32(arg0 + 8))
                        v13 = (load32(load32(arg0 + 8)) * v8)
                        v9 = load32(v5 + 40)
                        v5 = (load32(load32(v5 + 40) + 136) + (v3 * v6))
                        v10 = load32(arg0 + 20)
                        while True:  # $label1
                            v4 = load32(arg0 + 192)
                            if (load32(arg0 + 192) > 0):
                                v2 = (v4 - 1)
                                if (v4 == 1):
                                    break
                                while True:  # $label2
                                    v4 = (v2 - 1)
                                    v14 = (u32(v2) > u32(1))
                                    v2 = v4
                                    if v14:
                                        continue
                                    break
                                break
                            if (v10 == v11):
                                break
                            # TODO: memory.copy
                            break
                        v2 = load32(v9 + 12)
                        if load32(v9 + 12):
                            if not load32(((v2 << 2) + 9687552)):
                                break
                            v2 = load32(v9 + 140)
                            if (v8 & 1):
                                v3 = (v3 + 1)
                                v2 = v5
                            else:
                            v4 = v5
                            if (v8 != 1):
                                while True:  # $label4
                                    v2 = (v4 + v6)
                                    v4 = (v2 + v6)
                                    v5 = v2
                                    v3 = (v3 + 2)
                                    if ((v3 + 2) != v7):
                                        continue
                                    break
                            store32(v9 + 140, v5)
                        v2 = load32(arg0 + 100)
                        v11 = (v11 + ((load32(arg0 + 100) * v8) << 2))
                        v3 = v7
                        v12 = (v12 - v8)
                        if ((v12 - v8) > 0):
                            continue
                        break
                    break
                if (arg1 != v7):
                    break
                store32(arg0 + 108, arg1)
                store32(arg0 + 116, arg1)
                return call_table(load32(((load32(v9 + 12) << 2) + 9687552)))
            a_c()
            raise Unreachable()
            break
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()
    return 2967

# ----------------------------------------------------------
# $func1077
# ----------------------------------------------------------
def func1077(arg0, arg1, arg2):
    while True:  # $label1
        while True:  # $label0
            v3 = load32(arg0 + 36)
            if (load32((load32(arg0 + 36) - -64)) >= load32(v3 + 56)):
                break
            v8 = load32(v3 + 52)
            if (load32(v3 + 52) <= 0):
                while True:  # $label2
                    if (load32(v3 + 24) > 0):
                        break
                    if (arg2 <= v4):
                        break
                    if (load32(load32(arg0) + 8) <= (arg1 + v4)):
                        break
                    func91(0, v3)
                    v4 = (v4 + 1)
                    v3 = load32(arg0 + 36)
                    if (load32((load32(arg0 + 36) - -64)) < load32(v3 + 56)):
                        continue
                    break
                break
            v9 = load32(arg0)
            v11 = (load32(load32(arg0)) - 7)
            v12 = (v8 & -2)
            v13 = (v8 & 1)
            v14 = (load32(v9 + 16) + (load32(v9 + 20) * arg1))
            v6 = ((load32(v9 + 16) + (load32(v9 + 20) * arg1)) + 1)
            v5 = 15
            while True:  # $label5
                while True:  # $label3
                    if (load32(v3 + 24) > 0):
                        break
                    if (arg2 <= v4):
                        break
                    if (load32(load32(arg0) + 8) <= (arg1 + v4)):
                        break
                    func91(0, v3)
                    v3 = 0
                    v10 = 0
                    if (v8 != 1):
                        while True:  # $label4
                            v7 = (v6 + (v3 << 1))
                            v15 = ((load8u((load32(load32(arg0 + 36) + 68) + v3)) & 0xFFFFFFFF) >> 4)
                            store8((v6 + (v3 << 1)), (((load8u((load32(load32(arg0 + 36) + 68) + v3)) & 0xFFFFFFFF) >> 4) | (load8u(v7) & 240)))
                            v7 = (v3 | 1)
                            v16 = (v6 + ((v3 | 1) << 1))
                            v7 = ((load8u((load32(load32(arg0 + 36) + 68) + v7)) & 0xFFFFFFFF) >> 4)
                            store8((v6 + ((v3 | 1) << 1)), (((load8u((load32(load32(arg0 + 36) + 68) + v7)) & 0xFFFFFFFF) >> 4) | (load8u(v16) & 240)))
                            v5 = ((v5 & v15) & v7)
                            v3 = (v3 + 2)
                            v10 = (v10 + 2)
                            if ((v10 + 2) != v12):
                                continue
                            break
                    if v13:
                        v10 = (v6 + (v3 << 1))
                        v3 = ((load8u((load32(load32(arg0 + 36) + 68) + v3)) & 0xFFFFFFFF) >> 4)
                        store8((v6 + (v3 << 1)), (((load8u((load32(load32(arg0 + 36) + 68) + v3)) & 0xFFFFFFFF) >> 4) | (load8u(v10) & 240)))
                        v5 = (v3 & v5)
                    v4 = (v4 + 1)
                    v6 = (v6 + load32(v9 + 20))
                    v3 = load32(arg0 + 36)
                    if (load32((load32(arg0 + 36) - -64)) < load32(v3 + 56)):
                        continue
                    break
                break
            if (u32(v11) > u32(3)):
                break
            if (v5 == 15):
                break
            break
        return v4
        break
    a_c()
    raise Unreachable()
    return 7727

# ----------------------------------------------------------
# $func1078
# ----------------------------------------------------------
def func1078(arg0, arg1, arg2):
    while True:  # $label2
        while True:  # $label0
            v4 = load32(arg0 + 36)
            if (load32((load32(arg0 + 36) - -64)) >= load32(v4 + 56)):
                break
            v6 = load32(arg0)
            v9 = load32(load32(arg0))
            v10 = ((load32(load32(arg0)) == 4) | (v9 == 9))
            v7 = load32(v6 + 20)
            v11 = (load32(v6 + 16) + (load32(v6 + 20) * arg1))
            v12 = load32(v4 + 52)
            while True:  # $label1
                if (load32(v4 + 24) > 0):
                    break
                if (arg2 <= 0):
                    break
                v5 = (v11 + (0 if v10 else 3))
                while True:  # $label4
                    if (load32(load32(arg0) + 8) <= (arg1 + v3)):
                        break
                    func91(0, v4)
                    v8 = (call_table(load32(9687300)) | v8)
                    v3 = (v3 + 1)
                    v7 = load32(v6 + 20)
                    while True:  # $label3
                        v4 = load32(arg0 + 36)
                        if (load32((load32(arg0 + 36) - -64)) >= load32(v4 + 56)):
                            break
                        if (load32(v4 + 24) > 0):
                            break
                        v5 = (v5 + v7)
                        if (arg2 > v3):
                            continue
                        break
                    break
                break
            v5 = (v8 != 0)
            if (u32((v9 - 7)) > u32(3)):
                break
            if not v5:
                break
            break
        return v3
        break
    a_c()
    raise Unreachable()
    return 5680

# ----------------------------------------------------------
# $func1079
# ----------------------------------------------------------
def func1079(arg0):
    store32(arg0 + 4, 0)
    if load32(arg0):
        a_c()
        raise Unreachable()

# ----------------------------------------------------------
# $func1080
# ----------------------------------------------------------
def func1080(arg0, arg1):
    arg1 = load32(arg1)
    v6 = load32(load32(arg1) + 24)
    v7 = load32(arg1 + 40)
    v2 = load32(arg1 + 20)
    v3 = load32(arg1 + 36)
    v4 = load32(arg1 + 32)
    v5 = load32(arg0 + 8)
    v4 = load32(arg0 + 12)
    v8 = load32(arg0 + 16)
    func268(load32(arg0 + 20), load32(arg0 + 32), (load32(arg1 + 16) + (load32(arg1 + 32) * load32(arg0 + 8))), v4, load32(arg0 + 12), load32(arg0 + 16))
    v5 = (v5 >> 1)
    v2 = ((v4 + 1) // 2)
    v3 = ((v8 + 1) // 2)
    func268(load32(arg0 + 24), load32(arg0 + 36), (v2 + (v3 * (v5 >> 1))), load32(arg1 + 36), ((v4 + 1) // 2), ((v8 + 1) // 2))
    func268(load32(arg0 + 28), load32(arg0 + 36), (v6 + (v5 * v7)), load32(arg1 + 40), v2, v3)
    return load32(arg0 + 16)

# ----------------------------------------------------------
# $func1081
# ----------------------------------------------------------
def func1081(arg0, arg1):
    v2 = load32(arg0 + 20)
    v9 = load32(arg0 + 32)
    v5 = load32(arg0 + 24)
    v6 = load32(arg0 + 28)
    v10 = load32(arg0 + 36)
    v3 = load32(arg1)
    arg1 = load32(v3 + 20)
    v4 = (load32(load32(arg1) + 16) + (load32(v3 + 20) * load32(arg0 + 8)))
    v7 = load32(arg0 + 12)
    v3 = load32(((load32(v3) << 2) + 9687952))
    while True:  # $label0
        v8 = load32(arg0 + 16)
        if (load32(arg0 + 16) <= 0):
            break
        if (v8 != 1):
            v12 = (v8 & -2)
            while True:  # $label1
                v2 = (v2 + v9)
                v4 = (arg1 + v4)
                v5 = (v5 + v10)
                v6 = (v6 + v10)
                v4 = (arg1 + v4)
                v2 = (v2 + v9)
                v11 = (v11 + 2)
                if ((v11 + 2) != v12):
                    continue
                break
        if not (v8 & 1):
            break
        break
    return load32(arg0 + 16)

# ----------------------------------------------------------
# $func1082
# ----------------------------------------------------------
def func1082(arg0, arg1):
    v5 = load32(arg1 + 24)
    v4 = load32(arg0 + 16)
    while True:  # $label0
        v2 = load32(load32(arg1))
        if (not ((u32(load32(load32(arg1))) <= u32(12)) if ((1 << v2) & 4154) else 0) & (u32((v2 - 11)) < u32(-4))):
            break
        v2 = load32(arg0 + 104)
        if not load32(arg0 + 104):
            break
        func445(load32(arg0 + 20), load32(arg0 + 32), v2, load32(arg0), load32(arg0 + 12), v4, 0)
        break
    if (v4 <= 0):
        return 0
    v7 = ((v4 + 1) >> 1)
    v6 = load32(arg0 + 32)
    v3 = load32(arg0 + 20)
    v2 = v4
    while True:  # $label1
        v9 = func82(v5, v2, v3, v6)
        v3 = (v3 + (func82(v5, v2, v3, v6) * v6))
        v8 = (func187(v5) + v8)
        v2 = (v2 - v9)
        if ((v2 - v9) > 0):
            continue
        break
    if (v4 > 0):
        v4 = load32(arg1 + 28)
        v5 = load32(arg0 + 36)
        v3 = load32(arg0 + 24)
        v2 = v7
        while True:  # $label2
            v6 = func82(v4, v2, v3, v5)
            v3 = (v3 + (v5 * v6))
            v2 = (v2 - v6)
            if ((v2 - v6) > 0):
                continue
            break
        v3 = load32(arg0 + 28)
        arg1 = load32(arg1 + 32)
        arg0 = load32(arg0 + 36)
        while True:  # $label3
            v2 = func82(arg1, v7, v3, arg0)
            v3 = (v3 + (arg0 * v2))
            v7 = (v7 - v2)
            if ((v7 - v2) > 0):
                continue
            break
    return v8

# ----------------------------------------------------------
# $func1083
# ----------------------------------------------------------
def func1083(arg0, arg1):
    v6 = load32(arg0 + 16)
    if (load32(arg0 + 16) <= 0):
        return 0
    v11 = ((v6 + 1) >> 1)
    v2 = load32(arg1 + 24)
    while True:  # $label3
        while True:  # $label2
            while True:  # $label0
                while True:  # $label5
                    v2 = load32(arg0 + 32)
                    v12 = func82(v2, (v6 - v7), (load32(arg0 + 20) + (load32(arg0 + 32) * v7)), v2)
                    v2 = load32(arg1 + 28)
                    v3 = load32(load32(arg1 + 28) + 32)
                    v3 = (((load32(load32(arg1 + 28) + 32) + load32(v2 + 24)) - 1) // v3)
                    v2 = (v11 - v4)
                    if ((((load32(load32(arg1 + 28) + 32) + load32(v2 + 24)) - 1) // v3) if (v2 > v3) else (v11 - v4)):
                        v3 = load32(arg0 + 36)
                        v3 = func82(load32(arg1 + 28), v2, (load32(arg0 + 24) + (load32(arg0 + 36) * v4)), v3)
                        v2 = load32(arg0 + 36)
                        if (func82(load32(arg1 + 28), v2, (load32(arg0 + 24) + (load32(arg0 + 36) * v4)), v3) != func82(load32(arg1 + 32), v2, (load32(arg0 + 28) + (load32(arg0 + 36) * v4)), v2)):
                            break
                        v4 = (v3 + v4)
                    v3 = 0
                    while True:  # $label1
                        v2 = load32(arg1 + 24)
                        if (load32((load32(arg1 + 24) - -64)) >= load32(v2 + 56)):
                            break
                        v8 = load32(arg1)
                        v13 = load32(((load32(load32(arg1)) << 2) + 9687888))
                        v14 = (load32(arg1 + 16) + v9)
                        v10 = (load32(v8 + 16) + ((load32(arg1 + 16) + v9) * load32(v8 + 20)))
                        while True:  # $label4
                            if (load32(v2 + 24) > 0):
                                break
                            v5 = load32(arg1 + 28)
                            if (load32((load32(arg1 + 28) - -64)) >= load32(v5 + 56)):
                                break
                            v5 = load32(v5 + 24)
                            if (load32(v5 + 24) > 0):
                                break
                            if (load32(load32(arg1) + 8) <= (v3 + v14)):
                                break
                            if (v5 != load32(load32(arg1 + 32) + 24)):
                                break
                            func91(0, v2)
                            func91(0, load32(arg1 + 28))
                            func91(0, load32(arg1 + 32))
                            v2 = load32(arg1 + 24)
                            v3 = (v3 + 1)
                            v10 = (v10 + load32(v8 + 20))
                            v2 = load32(arg1 + 24)
                            if (load32((load32(arg1 + 24) - -64)) < load32(v2 + 56)):
                                continue
                            break
                        break
                    v9 = (v3 + v9)
                    v7 = (v7 + v12)
                    if (v6 > (v7 + v12)):
                        continue
                    break
                return v9
                break
            a_c()
            raise Unreachable()
            break
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()
    return 7626

# ----------------------------------------------------------
# $func1084
# ----------------------------------------------------------
def func1084(arg0, arg1, arg2):
    v5 = load32(arg1)
    v7 = load32(load32(arg1) + 28)
    v4 = load32(v5 + 44)
    v6 = load32(arg1 + 16)
    v3 = (load32(load32(arg1) + 28) + (load32(v5 + 44) * load32(arg1 + 16)))
    while True:  # $label3
        while True:  # $label2
            v8 = load32(arg0 + 104)
            if load32(arg0 + 104):
                while True:  # $label1
                    v4 = load32(arg0 + 16)
                    if (load32(arg0 + 16) > 0):
                        v9 = (load32(v5 + 16) + (load32(v5 + 32) * v6))
                        v6 = load32(arg1 + 36)
                        v7 = load32(arg0)
                        arg0 = 0
                        while True:  # $label0
                            v10 = func82(v6, v4, v8, v7)
                            v8 = (v8 + (func82(v6, v4, v8, v7) * v7))
                            arg0 = (func187(v6) + arg0)
                            v4 = (v4 - v10)
                            if ((v4 - v10) > 0):
                                continue
                            break
                        if (arg0 != arg2):
                            break
                        if (arg2 <= 0):
                            break
                        func445(v9, load32(v5 + 32), v3, load32(v5 + 44), load32(load32(arg1 + 36) + 52), arg2, 1)
                        return 0
                    if not arg2:
                        break
                    break
                a_c()
                raise Unreachable()
            if not v7:
                break
            if (load32(arg0 + 100) < (arg2 + v6)):
                break
            if (arg2 <= 0):
                break
            arg1 = load32(arg0 + 96)
            if (u32(arg2) >= u32(8)):
                v5 = (arg2 & -8)
                arg0 = 0
                while True:  # $label4
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    arg0 = (arg0 + 8)
                    if ((arg0 + 8) != v5):
                        continue
                    break
            arg2 = (arg2 & 7)
            if not (arg2 & 7):
                break
            arg0 = 0
            while True:  # $label5
                # TODO: memory.fill
                v3 = (v3 + v4)
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != arg2):
                    continue
                break
            break
        return 0
        break
    a_c()
    raise Unreachable()
    return 5759

# ----------------------------------------------------------
# $func1085
# ----------------------------------------------------------
def func1085(arg0, arg1, arg2):
    while True:  # $label0
        if not load32(arg0 + 104):
            break
        if (arg2 <= 0):
            break
        v4 = (load32(arg1 + 16) + arg2)
        v3 = load32(arg1 + 36)
        while True:  # $label1
            v5 = load32(arg0 + 8)
            v6 = load32(v3 + 60)
            v7 = load32(arg0)
            arg2 = (arg2 - call_table(load32(arg1 + 52)))
            if ((arg2 - call_table(load32(arg1 + 52))) > 0):
                continue
            break
        break
    return 0

# ----------------------------------------------------------
# $func1086
# ----------------------------------------------------------
def func1086(arg0, arg1):
    v2 = load32(arg0 + 16)
    v8 = load32(arg0 + 12)
    v13 = ((load32(arg0 + 12) + 1) // 2)
    v9 = load32(arg1)
    v10 = load32(v9 + 20)
    v3 = load32(arg0 + 8)
    v6 = (load32(load32(arg1) + 16) + (load32(v9 + 20) * load32(arg0 + 8)))
    v11 = load32(((load32(v9) << 2) + 9687824))
    v4 = load32(arg0 + 28)
    v5 = load32(arg0 + 24)
    v7 = load32(arg0 + 20)
    while True:  # $label0
        if not v3:
            break
        break
    v10 = (v2 + 1)
    v12 = (v2 + v3)
    if (v2 >= 3):
        v2 = (v3 + 2)
        while True:  # $label1
            v3 = load32(arg0 + 32)
            v7 = (v7 + (load32(arg0 + 32) << 1))
            v3 = load32(arg0 + 36)
            v5 = (v5 + load32(arg0 + 36))
            v4 = (v3 + v4)
            v3 = load32(v9 + 20)
            v6 = (v6 + (load32(v9 + 20) << 1))
            v2 = (v2 + 2)
            if ((v2 + 2) < v12):
                continue
            break
    v2 = (v7 + load32(arg0 + 32))
    if (load32(arg0 + 88) > (load32(arg0 + 84) + v12)):
        # TODO: memory.copy
        # TODO: memory.copy
        # TODO: memory.copy
        return (v10 - 1)
    if not (v12 & 1):
    return v10

# ----------------------------------------------------------
# $func1087
# ----------------------------------------------------------
def func1087(arg0, arg1, arg2):
    if (arg2 == load32(arg0 + 16)):
        v6 = load32(arg1)
        v7 = load32(load32(arg1) + 28)
        v4 = load32(v6 + 44)
        v3 = (load32(load32(arg1) + 28) + (load32(v6 + 44) * load32(arg0 + 8)))
        arg1 = load32(arg0 + 12)
        while True:  # $label0
            v5 = load32(arg0 + 104)
            if load32(arg0 + 104):
                if (arg2 <= 0):
                    break
                if (arg2 != 1):
                    v7 = (arg2 & -2)
                    v4 = 0
                    while True:  # $label1
                        # TODO: memory.copy
                        v3 = (v3 + load32(v6 + 44))
                        v5 = (v5 + load32(arg0))
                        # TODO: memory.copy
                        v3 = (v3 + load32(v6 + 44))
                        v5 = (v5 + load32(arg0))
                        v4 = (v4 + 2)
                        if ((v4 + 2) != v7):
                            continue
                        break
                if not (arg2 & 1):
                    break
                # TODO: memory.copy
                return 0
            if not v7:
                break
            if (arg2 <= 0):
                break
            if (u32(arg2) >= u32(8)):
                arg0 = (arg2 & -8)
                v5 = 0
                while True:  # $label2
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    # TODO: memory.fill
                    v3 = (v3 + v4)
                    v5 = (v5 + 8)
                    if ((v5 + 8) != arg0):
                        continue
                    break
            arg0 = (arg2 & 7)
            if not (arg2 & 7):
                break
            v5 = 0
            while True:  # $label3
                # TODO: memory.fill
                v3 = (v3 + v4)
                v5 = (v5 + 1)
                if ((v5 + 1) != arg0):
                    continue
                break
            break
        return 0
    a_c()
    raise Unreachable()
    return 5746

# ----------------------------------------------------------
# $func1088
# ----------------------------------------------------------
def func1088(arg0, arg1, arg2):
    while True:  # $label6
        while True:  # $label0
            v6 = load32(arg0 + 104)
            if not load32(arg0 + 104):
                break
            v4 = load32(arg0 + 16)
            v3 = load32(arg0 + 8)
            v9 = load32(arg1)
            while True:  # $label1
                if not load32(arg0 + 56):
                    arg1 = v3
                    break
                while True:  # $label2
                    if not v3:
                        v5 = (v4 - 1)
                        break
                    v6 = (v6 - load32(arg0))
                    v5 = v4
                    break
                arg1 = (v3 - 1)
                v7 = load32(arg0 + 84)
                v4 = (load32(arg0 + 84) + (v3 + v4))
                if ((load32(arg0 + 84) + (v3 + v4)) != load32(arg0 + 88)):
                    v4 = v5
                    break
                v4 = (v4 - (arg1 + v7))
                break
            v7 = load32(arg0 + 12)
            v13 = load32(v9)
            v3 = load32(v9 + 20)
            v11 = (load32(v9 + 16) + (load32(v9 + 20) * arg1))
            v5 = 15
            while True:  # $label3
                if (v4 <= 0):
                    break
                if (v7 <= 0):
                    break
                v14 = (v7 & -2)
                v15 = (v7 & 1)
                arg1 = (v11 + 1)
                while True:  # $label5
                    v3 = 0
                    v10 = 0
                    if (v7 != 1):
                        while True:  # $label4
                            v8 = (arg1 + (v3 << 1))
                            v16 = ((load8u((v3 + v6)) & 0xFFFFFFFF) >> 4)
                            store8((arg1 + (v3 << 1)), (((load8u((v3 + v6)) & 0xFFFFFFFF) >> 4) | (load8u(v8) & 240)))
                            v8 = (v3 | 1)
                            v17 = (arg1 + ((v3 | 1) << 1))
                            v8 = ((load8u((v6 + v8)) & 0xFFFFFFFF) >> 4)
                            store8((arg1 + ((v3 | 1) << 1)), (((load8u((v6 + v8)) & 0xFFFFFFFF) >> 4) | (load8u(v17) & 240)))
                            v5 = ((v5 & v16) & v8)
                            v3 = (v3 + 2)
                            v10 = (v10 + 2)
                            if ((v10 + 2) != v14):
                                continue
                            break
                    if v15:
                        v10 = (arg1 + (v3 << 1))
                        v3 = ((load8u((v3 + v6)) & 0xFFFFFFFF) >> 4)
                        store8((arg1 + (v3 << 1)), (((load8u((v3 + v6)) & 0xFFFFFFFF) >> 4) | (load8u(v10) & 240)))
                        v5 = (v3 & v5)
                    v3 = load32(v9 + 20)
                    arg1 = (arg1 + load32(v9 + 20))
                    v6 = (v6 + load32(arg0))
                    v12 = (v12 + 1)
                    if ((v12 + 1) != v4):
                        continue
                    break
                break
            if (arg2 != v4):
                break
            if (v5 == 15):
                break
            if (u32((v13 - 11)) < u32(-4)):
                break
            break
        return 0
        break
    a_c()
    raise Unreachable()
    return 7747

# ----------------------------------------------------------
# $func1089
# ----------------------------------------------------------
def func1089(arg0, arg1, arg2):
    while True:  # $label3
        while True:  # $label0
            v5 = load32(arg0 + 104)
            if not load32(arg0 + 104):
                break
            v6 = load32(arg1)
            v8 = load32(load32(arg1))
            v9 = ((load32(load32(arg1)) == 4) | (v8 == 9))
            arg1 = load32(arg0 + 16)
            v3 = load32(arg0 + 8)
            v10 = load32(arg0 + 12)
            while True:  # $label1
                if not load32(arg0 + 56):
                    v4 = v3
                    break
                while True:  # $label2
                    if not v3:
                        break
                    v4 = (v3 - 1)
                    v5 = (v5 - load32(arg0))
                    break
                v7 = arg1
                v11 = load32(arg0 + 84)
                arg1 = (load32(arg0 + 84) + (arg1 + v3))
                if ((load32(arg0 + 84) + (arg1 + v3)) != load32(arg0 + 88)):
                    arg1 = v7
                    break
                arg1 = (arg1 - (v4 + v11))
                break
            arg0 = load32(v6 + 20)
            v7 = (load32(v6 + 16) + (load32(v6 + 20) * v4))
            arg0 = call_table(load32(9687300))
            if (arg1 != arg2):
                break
            if not arg0:
                break
            if (u32((v8 - 11)) < u32(-4)):
                break
            break
        return 0
        break
    a_c()
    raise Unreachable()
    return 7652

# ----------------------------------------------------------
# $de
# Export: de
# ----------------------------------------------------------
def de(arg0, arg1):
    """Export: de"""
    while True:  # $label0
        while True:  # $label4
            while True:  # $label5
                while True:  # $label12
                    while True:  # $label1
                        while True:  # $label2
                            while True:  # $label3
                                # br_table arg1
                                break
                                break
                            v2 = load32(9671136)
                            if (u32(load32(9671136)) < u32(4)):
                                break
                            arg1 = 3
                            v3 = load32(ENTITIES)
                            if (u32(arg0) > u32(3)):
                                break
                            v6 = (arg0 - 1)
                            while True:  # $label11
                                while True:  # $label6
                                    v4 = (v3 + (arg1 * 132))
                                    if not load32(((load16u((v3 + (arg1 * 132)) + 110) << 2) + 9151488)):
                                        break
                                    if (load8u(v4 + 125) == 3):
                                        break
                                    arg0 = load8u(v4 + 122)
                                    while True:  # $label10
                                        while True:  # $label7
                                            while True:  # $label8
                                                while True:  # $label9
                                                    # br_table v6
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
                                        v5 = ((arg0 * 404) + ENTITY_TYPES)
                                        if load32(((arg0 * 404) + ENTITY_TYPES) + 264):
                                            break
                                        if (load32(v5 + 268) == 1):
                                            break
                                        if not load32(v5 + 92):
                                            break
                                        if (load32(38456) == arg0):
                                            break
                                        if (load32(38764) == arg0):
                                            break
                                        break
                                    func256(v4, load32(9151484))
                                    v2 = load32(9671136)
                                    v3 = load32(ENTITIES)
                                    break
                                arg1 = (arg1 + 1)
                                if (u32((arg1 + 1)) < u32(v2)):
                                    continue
                                break
                            break
                            break
                        v2 = load32(9671136)
                        if (u32(load32(9671136)) < u32(4)):
                            break
                        arg1 = 3
                        v3 = load32(ENTITIES)
                        if (u32(arg0) > u32(3)):
                            break
                        v6 = (arg0 - 1)
                        while True:  # $label18
                            while True:  # $label13
                                v4 = (v3 + (arg1 * 132))
                                if not load32(((load16u((v3 + (arg1 * 132)) + 110) << 2) + 9151488)):
                                    break
                                if (load8u(v4 + 125) == 3):
                                    break
                                arg0 = load8u(v4 + 122)
                                while True:  # $label17
                                    while True:  # $label14
                                        while True:  # $label15
                                            while True:  # $label16
                                                # br_table v6
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
                                    v5 = ((arg0 * 404) + ENTITY_TYPES)
                                    if load32(((arg0 * 404) + ENTITY_TYPES) + 264):
                                        break
                                    if (load32(v5 + 268) == 1):
                                        break
                                    if not load32(v5 + 92):
                                        break
                                    if (load32(38456) == arg0):
                                        break
                                    if (load32(38764) == arg0):
                                        break
                                    break
                                v2 = load32(9671136)
                                v3 = load32(ENTITIES)
                                break
                            arg1 = (arg1 + 1)
                            if (u32((arg1 + 1)) < u32(v2)):
                                continue
                            break
                        break
                        break
                    if (u32(load32(9671136)) < u32(4)):
                        break
                    v5 = (arg0 - 4)
                    v6 = (arg0 - 1)
                    arg1 = 3
                    while True:  # $label24
                        while True:  # $label19
                            v3 = entities[arg1]
                            if not load32(((load16u(entities[arg1] + 110) << 2) + 9151488)):
                                break
                            if (load8u(v3 + 125) == 3):
                                break
                            v2 = load8u(v3 + 122)
                            while True:  # $label23
                                if (u32(arg0) <= u32(3)):
                                    while True:  # $label21
                                        while True:  # $label22
                                            while True:  # $label20
                                                # br_table v6
                                                break
                                                break
                                            v4 = ((v2 * 404) + ENTITY_TYPES)
                                            if load32(((v2 * 404) + ENTITY_TYPES) + 264):
                                                break
                                            if (load32(v4 + 268) == 1):
                                                break
                                            if not load32(v4 + 92):
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
                                    if not load32(((v2 * 404) + ENTITY_TYPES) + 264):
                                        break
                                    break
                                if (v2 != v5):
                                    break
                                break
                            func368(load32(v3 + 28))
                            break
                        arg1 = (arg1 + 1)
                        if (u32((arg1 + 1)) < u32(load32(9671136))):
                            continue
                        break
                    break
                    break
                v4 = (arg0 - 4)
                while True:  # $label26
                    while True:  # $label25
                        arg0 = (v3 + (arg1 * 132))
                        if not load32(((load16u((v3 + (arg1 * 132)) + 110) << 2) + 9151488)):
                            break
                        if (load8u(arg0 + 125) == 3):
                            break
                        if (v4 != load8u(arg0 + 122)):
                            break
                        v2 = load32(9671136)
                        v3 = load32(ENTITIES)
                        break
                    arg1 = (arg1 + 1)
                    if (u32((arg1 + 1)) < u32(v2)):
                        continue
                    break
                break
                break
            v4 = (arg0 - 4)
            while True:  # $label28
                while True:  # $label27
                    arg0 = (v3 + (arg1 * 132))
                    if not load32(((load16u((v3 + (arg1 * 132)) + 110) << 2) + 9151488)):
                        break
                    if (load8u(arg0 + 125) == 3):
                        break
                    if (v4 != load8u(arg0 + 122)):
                        break
                    func256(arg0, load32(9151484))
                    v2 = load32(9671136)
                    v3 = load32(ENTITIES)
                    break
                arg1 = (arg1 + 1)
                if (u32((arg1 + 1)) < u32(v2)):
                    continue
                break
            break
        return
        break
    store32(9143000, 0)
    arg1 = load32(9213820)
    if load32(9213820):
        func47(entities[arg1])
        store32(9213820, 0)
    func45()
    if (u32(load32(9671136)) >= u32(4)):
        v5 = (arg0 - 4)
        v6 = (arg0 - 1)
        arg1 = 3
        while True:  # $label34
            while True:  # $label29
                v3 = entities[arg1]
                if not load32(((load16u(entities[arg1] + 110) << 2) + 9151488)):
                    break
                if (load8u(v3 + 125) == 3):
                    break
                v2 = load8u(v3 + 122)
                while True:  # $label33
                    if (u32(arg0) <= u32(3)):
                        while True:  # $label31
                            while True:  # $label32
                                while True:  # $label30
                                    # br_table v6
                                    break
                                    break
                                v4 = ((v2 * 404) + ENTITY_TYPES)
                                if load32(((v2 * 404) + ENTITY_TYPES) + 264):
                                    break
                                if (load32(v4 + 268) == 1):
                                    break
                                if not load32(v4 + 92):
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
                        if not load32(((v2 * 404) + ENTITY_TYPES) + 264):
                            break
                        break
                    if (v2 != v5):
                        break
                    break
                func44(v3, 0)
                break
            arg1 = (arg1 + 1)
            if (u32((arg1 + 1)) < u32(load32(9671136))):
                continue
            break

# ----------------------------------------------------------
# $gd
# Export: gd
# ----------------------------------------------------------
def gd():
    """Export: gd"""
    v0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    if load32(9140324):
        while True:  # $label0
            v2 = load32(load32((load32(9140332) + (v1 << 2))) + 32)
            store32(v0, v1)
            store32(v0 + 4, v2)
            v1 = (v1 + 1)
            if (u32((v1 + 1)) < u32(load32(9140324))):
                continue
            break
    G.global0 = (v0 + 16)

# ----------------------------------------------------------
# $xb
# Export: xb
# ----------------------------------------------------------
def xb(arg0):
    """Export: xb"""
    while True:  # $label0
        if (arg0 < 2):
            break
        if (load32(9681888) != 1):
            break
        if not load32(9671176):
            break
        v2 = load32(load32(9671168))
        store8(9681884, 1)
        store32(9681892, v2)
        store8(9681885, 0)
        if load32(9671192):
            while True:  # $label1
                func38(load32((load32(9671184) + (v1 << 2))))
                v1 = (v1 + 1)
                if (u32((v1 + 1)) < u32(load32(9671192))):
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
    store32(9681888, arg0)

# ----------------------------------------------------------
# $func1102
# ----------------------------------------------------------
def func1102(arg0, arg1, arg2):
    while True:  # $label1
        if (arg2 != 1):
            while True:  # $label0
                v3 = (load8u(arg1) + ((load8u(arg0) - 120) >> 4))
                v3 = ((load8u(arg1) + ((load8u(arg0) - 120) >> 4)) if (v3 > 0) else 0)
                store8(arg1, (255 if (v3 >= 255) else ((load8u(arg1) + ((load8u(arg0) - 120) >> 4)) if (v3 > 0) else 0)))
                v3 = (load8u(arg1 + 1) + ((load8u(arg0 + 1) - 120) >> 4))
                v3 = ((load8u(arg1 + 1) + ((load8u(arg0 + 1) - 120) >> 4)) if (v3 > 0) else 0)
                store8(arg1 + 1, (255 if (v3 >= 255) else ((load8u(arg1 + 1) + ((load8u(arg0 + 1) - 120) >> 4)) if (v3 > 0) else 0)))
                v3 = (load8u(arg1 + 2) + ((load8u(arg0 + 2) - 120) >> 4))
                v3 = ((load8u(arg1 + 2) + ((load8u(arg0 + 2) - 120) >> 4)) if (v3 > 0) else 0)
                store8(arg1 + 2, (255 if (v3 >= 255) else ((load8u(arg1 + 2) + ((load8u(arg0 + 2) - 120) >> 4)) if (v3 > 0) else 0)))
                v3 = (load8u(arg1 + 3) + ((load8u(arg0 + 3) - 120) >> 4))
                v3 = ((load8u(arg1 + 3) + ((load8u(arg0 + 3) - 120) >> 4)) if (v3 > 0) else 0)
                store8(arg1 + 3, (255 if (v3 >= 255) else ((load8u(arg1 + 3) + ((load8u(arg0 + 3) - 120) >> 4)) if (v3 > 0) else 0)))
                v3 = (load8u(arg1 + 4) + ((load8u(arg0 + 4) - 120) >> 4))
                v3 = ((load8u(arg1 + 4) + ((load8u(arg0 + 4) - 120) >> 4)) if (v3 > 0) else 0)
                store8(arg1 + 4, (255 if (v3 >= 255) else ((load8u(arg1 + 4) + ((load8u(arg0 + 4) - 120) >> 4)) if (v3 > 0) else 0)))
                v3 = (load8u(arg1 + 5) + ((load8u(arg0 + 5) - 120) >> 4))
                v3 = ((load8u(arg1 + 5) + ((load8u(arg0 + 5) - 120) >> 4)) if (v3 > 0) else 0)
                store8(arg1 + 5, (255 if (v3 >= 255) else ((load8u(arg1 + 5) + ((load8u(arg0 + 5) - 120) >> 4)) if (v3 > 0) else 0)))
                v3 = (load8u(arg1 + 6) + ((load8u(arg0 + 6) - 120) >> 4))
                v3 = ((load8u(arg1 + 6) + ((load8u(arg0 + 6) - 120) >> 4)) if (v3 > 0) else 0)
                store8(arg1 + 6, (255 if (v3 >= 255) else ((load8u(arg1 + 6) + ((load8u(arg0 + 6) - 120) >> 4)) if (v3 > 0) else 0)))
                v3 = (load8u(arg1 + 7) + ((load8u(arg0 + 7) - 120) >> 4))
                v3 = ((load8u(arg1 + 7) + ((load8u(arg0 + 7) - 120) >> 4)) if (v3 > 0) else 0)
                store8(arg1 + 7, (255 if (v3 >= 255) else ((load8u(arg1 + 7) + ((load8u(arg0 + 7) - 120) >> 4)) if (v3 > 0) else 0)))
                arg0 = (arg0 + 8)
                arg1 = (arg1 + arg2)
                v5 = (v5 + 1)
                if ((v5 + 1) != 8):
                    continue
                break
            break
        v5 = load8u(arg1 + 6)
        while True:  # $label2
            v4 = (load8u(arg1) + ((load8u(arg0) - 120) >> 4))
            v4 = ((load8u(arg1) + ((load8u(arg0) - 120) >> 4)) if (v4 > 0) else 0)
            store8(arg1, (255 if (v4 >= 255) else ((load8u(arg1) + ((load8u(arg0) - 120) >> 4)) if (v4 > 0) else 0)))
            v4 = (load8u(arg1 + 1) + ((load8u(arg0 + 1) - 120) >> 4))
            v4 = ((load8u(arg1 + 1) + ((load8u(arg0 + 1) - 120) >> 4)) if (v4 > 0) else 0)
            store8(arg1 + 1, (255 if (v4 >= 255) else ((load8u(arg1 + 1) + ((load8u(arg0 + 1) - 120) >> 4)) if (v4 > 0) else 0)))
            v4 = (load8u(arg1 + 2) + ((load8u(arg0 + 2) - 120) >> 4))
            v4 = ((load8u(arg1 + 2) + ((load8u(arg0 + 2) - 120) >> 4)) if (v4 > 0) else 0)
            store8(arg1 + 2, (255 if (v4 >= 255) else ((load8u(arg1 + 2) + ((load8u(arg0 + 2) - 120) >> 4)) if (v4 > 0) else 0)))
            v4 = (load8u(arg1 + 3) + ((load8u(arg0 + 3) - 120) >> 4))
            v4 = ((load8u(arg1 + 3) + ((load8u(arg0 + 3) - 120) >> 4)) if (v4 > 0) else 0)
            store8(arg1 + 3, (255 if (v4 >= 255) else ((load8u(arg1 + 3) + ((load8u(arg0 + 3) - 120) >> 4)) if (v4 > 0) else 0)))
            v4 = (load8u(arg1 + 4) + ((load8u(arg0 + 4) - 120) >> 4))
            v4 = ((load8u(arg1 + 4) + ((load8u(arg0 + 4) - 120) >> 4)) if (v4 > 0) else 0)
            store8(arg1 + 4, (255 if (v4 >= 255) else ((load8u(arg1 + 4) + ((load8u(arg0 + 4) - 120) >> 4)) if (v4 > 0) else 0)))
            v4 = (load8u(arg1 + 5) + ((load8u(arg0 + 5) - 120) >> 4))
            v4 = ((load8u(arg1 + 5) + ((load8u(arg0 + 5) - 120) >> 4)) if (v4 > 0) else 0)
            store8(arg1 + 5, (255 if (v4 >= 255) else ((load8u(arg1 + 5) + ((load8u(arg0 + 5) - 120) >> 4)) if (v4 > 0) else 0)))
            v5 = ((v5 & 255) + ((load8u(arg0 + 6) - 120) >> 4))
            v5 = (((v5 & 255) + ((load8u(arg0 + 6) - 120) >> 4)) if (v5 > 0) else 0)
            store8(arg1 + 6, (255 if (v5 >= 255) else (((v5 & 255) + ((load8u(arg0 + 6) - 120) >> 4)) if (v5 > 0) else 0)))
            v5 = (load8u(arg1 + 7) + ((load8u(arg0 + 7) - 120) >> 4))
            v5 = ((load8u(arg1 + 7) + ((load8u(arg0 + 7) - 120) >> 4)) if (v5 > 0) else 0)
            v5 = (255 if (v5 >= 255) else ((load8u(arg1 + 7) + ((load8u(arg0 + 7) - 120) >> 4)) if (v5 > 0) else 0))
            store8(arg1 + 7, (255 if (v5 >= 255) else ((load8u(arg1 + 7) + ((load8u(arg0 + 7) - 120) >> 4)) if (v5 > 0) else 0)))
            arg0 = (arg0 + 8)
            arg1 = (arg1 + arg2)
            v3 = (v3 + 1)
            if ((v3 + 1) != 8):
                continue
            break
        break

# ----------------------------------------------------------
# $func1103
# ----------------------------------------------------------
def func1103(arg0, arg1, arg2, arg3, arg4, arg5):
    while True:  # $label0
        if (arg3 <= 0):
            break
        if (arg2 <= 0):
            break
        v14 = (arg2 & -4)
        v12 = (arg2 & 3)
        v6 = 255
        v15 = (u32(arg2) < u32(4))
        while True:  # $label3
            arg2 = 0
            v7 = 0
            if not v15:
                while True:  # $label1
                    v8 = load8u((arg0 + arg2))
                    store8((arg4 + (arg2 << 2)), load8u((arg0 + arg2)))
                    v9 = (arg2 | 1)
                    v9 = load8u((arg0 + v9))
                    store8((arg4 + ((arg2 | 1) << 2)), load8u((arg0 + v9)))
                    v10 = (arg2 | 2)
                    v10 = load8u((arg0 + v10))
                    store8((arg4 + ((arg2 | 2) << 2)), load8u((arg0 + v10)))
                    v11 = (arg2 | 3)
                    v11 = load8u((arg0 + v11))
                    store8((arg4 + ((arg2 | 3) << 2)), load8u((arg0 + v11)))
                    v6 = (v11 & (v10 & (v9 & (v6 & v8))))
                    arg2 = (arg2 + 4)
                    v7 = (v7 + 4)
                    if ((v7 + 4) != v14):
                        continue
                    break
            v7 = 0
            if v12:
                while True:  # $label2
                    v8 = load8u((arg0 + arg2))
                    store8((arg4 + (arg2 << 2)), load8u((arg0 + arg2)))
                    arg2 = (arg2 + 1)
                    v6 = (v6 & v8)
                    v7 = (v7 + 1)
                    if ((v7 + 1) != v12):
                        continue
                    break
            arg4 = (arg4 + arg5)
            arg0 = (arg0 + arg1)
            v13 = (v13 + 1)
            if ((v13 + 1) != arg3):
                continue
            break
        v6 = (v6 != 255)
        break
    return v6

# ----------------------------------------------------------
# $func1104
# ----------------------------------------------------------
def func1104(arg0, arg1, arg2, arg3, arg4, arg5):
    while True:  # $label0
        if (arg3 <= 0):
            break
        if (arg2 <= 0):
            break
        v9 = (arg2 & -4)
        v7 = (arg2 & 3)
        v10 = (u32(arg2) < u32(4))
        v11 = (arg5 << 2)
        while True:  # $label3
            arg2 = 0
            arg5 = 0
            if not v10:
                while True:  # $label1
                    store32((arg4 + (arg2 << 2)), (load8u((arg0 + arg2)) << 8))
                    v6 = (arg2 | 1)
                    store32((arg4 + ((arg2 | 1) << 2)), (load8u((arg0 + v6)) << 8))
                    v6 = (arg2 | 2)
                    store32((arg4 + ((arg2 | 2) << 2)), (load8u((arg0 + v6)) << 8))
                    v6 = (arg2 | 3)
                    store32((arg4 + ((arg2 | 3) << 2)), (load8u((arg0 + v6)) << 8))
                    arg2 = (arg2 + 4)
                    arg5 = (arg5 + 4)
                    if ((arg5 + 4) != v9):
                        continue
                    break
            arg5 = 0
            if v7:
                while True:  # $label2
                    store32((arg4 + (arg2 << 2)), (load8u((arg0 + arg2)) << 8))
                    arg2 = (arg2 + 1)
                    arg5 = (arg5 + 1)
                    if ((arg5 + 1) != v7):
                        continue
                    break
            arg0 = (arg0 + arg1)
            arg4 = (arg4 + v11)
            v8 = (v8 + 1)
            if ((v8 + 1) != arg3):
                continue
            break
        break

# ----------------------------------------------------------
# $func1105
# ----------------------------------------------------------
def func1105(arg0):
    v1 = ((i32(((((load8u(arg0 + 223) + (load8u((arg0 - 25)) + (load8u(arg0 + 191) + (load8u((arg0 - 26)) + (load8u(arg0 + 159) + (load8u((arg0 - 27)) + (load8u(arg0 + 127) + (load8u((arg0 - 28)) + (load8u(arg0 + 95) + (load8u((arg0 - 29)) + (load8u(arg0 + 63) + (load8u((arg0 - 30)) + (load8u(arg0 + 31) + (load8u((arg0 - 31)) + (load8u((arg0 - 32)) + load8u((arg0 - 1))))))))))))))))) + 8) & 0xFFFFFFFF) >> 4)) & 255) * 72340172838076673)
    store64(arg0 + 224, ((i32(((((load8u(arg0 + 223) + (load8u((arg0 - 25)) + (load8u(arg0 + 191) + (load8u((arg0 - 26)) + (load8u(arg0 + 159) + (load8u((arg0 - 27)) + (load8u(arg0 + 127) + (load8u((arg0 - 28)) + (load8u(arg0 + 95) + (load8u((arg0 - 29)) + (load8u(arg0 + 63) + (load8u((arg0 - 30)) + (load8u(arg0 + 31) + (load8u((arg0 - 31)) + (load8u((arg0 - 32)) + load8u((arg0 - 1))))))))))))))))) + 8) & 0xFFFFFFFF) >> 4)) & 255) * 72340172838076673))
    store64(arg0 + 192, v1)
    store64(arg0 + 160, v1)
    store64(arg0 + 128, v1)
    store64(arg0 + 96, v1)
    store64(arg0 + 64, v1)
    store64(arg0 + 32, v1)
    store64(arg0, v1)

# ----------------------------------------------------------
# $func1106
# ----------------------------------------------------------
def func1106(arg0):
    v1 = ((i32(((((load8u(arg0 + 223) + (load8u(arg0 + 191) + (load8u(arg0 + 159) + (load8u(arg0 + 127) + (load8u(arg0 + 95) + (load8u(arg0 + 63) + (load8u((arg0 - 1)) + load8u(arg0 + 31)))))))) + 4) & 0xFFFFFFFF) >> 3)) & 255) * 72340172838076673)
    store64(arg0 + 224, ((i32(((((load8u(arg0 + 223) + (load8u(arg0 + 191) + (load8u(arg0 + 159) + (load8u(arg0 + 127) + (load8u(arg0 + 95) + (load8u(arg0 + 63) + (load8u((arg0 - 1)) + load8u(arg0 + 31)))))))) + 4) & 0xFFFFFFFF) >> 3)) & 255) * 72340172838076673))
    store64(arg0 + 192, v1)
    store64(arg0 + 160, v1)
    store64(arg0 + 128, v1)
    store64(arg0 + 96, v1)
    store64(arg0 + 64, v1)
    store64(arg0 + 32, v1)
    store64(arg0, v1)

# ----------------------------------------------------------
# $func1107
# ----------------------------------------------------------
def func1107(arg0):
    store64(arg0 + 224, -9187201950435737472)
    store64(arg0 + 192, -9187201950435737472)
    store64(arg0 + 160, -9187201950435737472)
    store64(arg0 + 128, -9187201950435737472)
    store64(arg0 + 96, -9187201950435737472)
    store64(arg0 + 64, -9187201950435737472)
    store64(arg0 + 32, -9187201950435737472)
    store64(arg0, -9187201950435737472)

# ----------------------------------------------------------
# $func1108
# ----------------------------------------------------------
def func1108(arg0):
    v1 = ((i32(((((load8u((arg0 - 25)) + (load8u((arg0 - 26)) + (load8u((arg0 - 27)) + (load8u((arg0 - 28)) + (load8u((arg0 - 29)) + (load8u((arg0 - 30)) + (load8u((arg0 - 32)) + load8u((arg0 - 31))))))))) + 4) & 0xFFFFFFFF) >> 3)) & 255) * 72340172838076673)
    store64(arg0 + 224, ((i32(((((load8u((arg0 - 25)) + (load8u((arg0 - 26)) + (load8u((arg0 - 27)) + (load8u((arg0 - 28)) + (load8u((arg0 - 29)) + (load8u((arg0 - 30)) + (load8u((arg0 - 32)) + load8u((arg0 - 31))))))))) + 4) & 0xFFFFFFFF) >> 3)) & 255) * 72340172838076673))
    store64(arg0 + 192, v1)
    store64(arg0 + 160, v1)
    store64(arg0 + 128, v1)
    store64(arg0 + 96, v1)
    store64(arg0 + 64, v1)
    store64(arg0 + 32, v1)
    store64(arg0, v1)

# ----------------------------------------------------------
# $func1109
# ----------------------------------------------------------
def func1109(arg0):
    v1 = ((((((load8u(arg0 + 95) + (load8u((arg0 - 29)) + (load8u(arg0 + 63) + (load8u((arg0 - 30)) + (load8u(arg0 + 31) + (load8u((arg0 - 31)) + (load8u((arg0 - 32)) + load8u((arg0 - 1))))))))) + 4) & 0xFFFFFFFF) >> 3) & 255) * 16843009)
    store32(arg0 + 96, ((((((load8u(arg0 + 95) + (load8u((arg0 - 29)) + (load8u(arg0 + 63) + (load8u((arg0 - 30)) + (load8u(arg0 + 31) + (load8u((arg0 - 31)) + (load8u((arg0 - 32)) + load8u((arg0 - 1))))))))) + 4) & 0xFFFFFFFF) >> 3) & 255) * 16843009))
    store32(arg0 + 64, v1)
    store32(arg0 + 32, v1)
    store32(arg0, v1)

# ----------------------------------------------------------
# $func1110
# ----------------------------------------------------------
def func1110(arg0):
    v1 = ((i32(((((load8u((arg0 - 17)) + (load8u(arg0 + 479) + (load8u((arg0 - 18)) + (load8u(arg0 + 447) + (load8u((arg0 - 19)) + (load8u(arg0 + 415) + (load8u((arg0 - 20)) + (load8u(arg0 + 383) + (load8u((arg0 - 21)) + (load8u(arg0 + 351) + (load8u((arg0 - 22)) + (load8u(arg0 + 319) + (load8u((arg0 - 23)) + (load8u(arg0 + 287) + (load8u((arg0 - 24)) + (load8u(arg0 + 255) + (load8u((arg0 - 25)) + (load8u(arg0 + 223) + (load8u((arg0 - 26)) + (load8u(arg0 + 191) + (load8u((arg0 - 27)) + (load8u(arg0 + 159) + (load8u((arg0 - 28)) + (load8u(arg0 + 127) + (load8u((arg0 - 29)) + (load8u(arg0 + 95) + (load8u((arg0 - 30)) + (load8u(arg0 + 63) + (load8u((arg0 - 31)) + (load8u(arg0 + 31) + (load8u((arg0 - 1)) + load8u((arg0 - 32))))))))))))))))))))))))))))))))) + 16) & 0xFFFFFFFF) >> 5)) & 255) * 72340172838076673)
    store64(arg0 + 8, ((i32(((((load8u((arg0 - 17)) + (load8u(arg0 + 479) + (load8u((arg0 - 18)) + (load8u(arg0 + 447) + (load8u((arg0 - 19)) + (load8u(arg0 + 415) + (load8u((arg0 - 20)) + (load8u(arg0 + 383) + (load8u((arg0 - 21)) + (load8u(arg0 + 351) + (load8u((arg0 - 22)) + (load8u(arg0 + 319) + (load8u((arg0 - 23)) + (load8u(arg0 + 287) + (load8u((arg0 - 24)) + (load8u(arg0 + 255) + (load8u((arg0 - 25)) + (load8u(arg0 + 223) + (load8u((arg0 - 26)) + (load8u(arg0 + 191) + (load8u((arg0 - 27)) + (load8u(arg0 + 159) + (load8u((arg0 - 28)) + (load8u(arg0 + 127) + (load8u((arg0 - 29)) + (load8u(arg0 + 95) + (load8u((arg0 - 30)) + (load8u(arg0 + 63) + (load8u((arg0 - 31)) + (load8u(arg0 + 31) + (load8u((arg0 - 1)) + load8u((arg0 - 32))))))))))))))))))))))))))))))))) + 16) & 0xFFFFFFFF) >> 5)) & 255) * 72340172838076673))
    store64(arg0, v1)
    store64(arg0 + 32, v1)
    store64(arg0 + 40, v1)
    store64(arg0 + 64, v1)
    store64(arg0 + 72, v1)
    store64(arg0 + 96, v1)
    store64(arg0 + 104, v1)
    store64(arg0 + 128, v1)
    store64(arg0 + 136, v1)
    store64(arg0 + 160, v1)
    store64(arg0 + 168, v1)
    store64(arg0 + 192, v1)
    store64(arg0 + 200, v1)
    store64(arg0 + 232, v1)
    store64(arg0 + 224, v1)
    store64(arg0 + 264, v1)
    store64(arg0 + 256, v1)
    store64(arg0 + 296, v1)
    store64(arg0 + 288, v1)
    store64(arg0 + 328, v1)
    store64(arg0 + 320, v1)
    store64(arg0 + 360, v1)
    store64(arg0 + 352, v1)
    store64(arg0 + 392, v1)
    store64(arg0 + 384, v1)
    store64(arg0 + 424, v1)
    store64(arg0 + 416, v1)
    store64(arg0 + 456, v1)
    store64(arg0 + 448, v1)
    store64(arg0 + 488, v1)
    store64(arg0 + 480, v1)

# ----------------------------------------------------------
# $func1111
# ----------------------------------------------------------
def func1111(arg0):
    v1 = ((i32(((((load8u(arg0 + 479) + (load8u(arg0 + 447) + (load8u(arg0 + 415) + (load8u(arg0 + 383) + (load8u(arg0 + 351) + (load8u(arg0 + 319) + (load8u(arg0 + 287) + (load8u(arg0 + 255) + (load8u(arg0 + 223) + (load8u(arg0 + 191) + (load8u(arg0 + 159) + (load8u(arg0 + 127) + (load8u(arg0 + 95) + (load8u(arg0 + 63) + (load8u((arg0 - 1)) + load8u(arg0 + 31)))))))))))))))) + 8) & 0xFFFFFFFF) >> 4)) & 255) * 72340172838076673)
    store64(arg0, ((i32(((((load8u(arg0 + 479) + (load8u(arg0 + 447) + (load8u(arg0 + 415) + (load8u(arg0 + 383) + (load8u(arg0 + 351) + (load8u(arg0 + 319) + (load8u(arg0 + 287) + (load8u(arg0 + 255) + (load8u(arg0 + 223) + (load8u(arg0 + 191) + (load8u(arg0 + 159) + (load8u(arg0 + 127) + (load8u(arg0 + 95) + (load8u(arg0 + 63) + (load8u((arg0 - 1)) + load8u(arg0 + 31)))))))))))))))) + 8) & 0xFFFFFFFF) >> 4)) & 255) * 72340172838076673))
    store64(arg0 + 8, v1)
    store64(arg0 + 40, v1)
    store64(arg0 + 32, v1)
    store64(arg0 + 72, v1)
    store64(arg0 + 64, v1)
    store64(arg0 + 104, v1)
    store64(arg0 + 96, v1)
    store64(arg0 + 136, v1)
    store64(arg0 + 128, v1)
    store64(arg0 + 168, v1)
    store64(arg0 + 160, v1)
    store64(arg0 + 200, v1)
    store64(arg0 + 192, v1)
    store64(arg0 + 232, v1)
    store64(arg0 + 224, v1)
    store64(arg0 + 264, v1)
    store64(arg0 + 256, v1)
    store64(arg0 + 296, v1)
    store64(arg0 + 288, v1)
    store64(arg0 + 328, v1)
    store64(arg0 + 320, v1)
    store64(arg0 + 360, v1)
    store64(arg0 + 352, v1)
    store64(arg0 + 392, v1)
    store64(arg0 + 384, v1)
    store64(arg0 + 424, v1)
    store64(arg0 + 416, v1)
    store64(arg0 + 456, v1)
    store64(arg0 + 448, v1)
    store64(arg0 + 488, v1)
    store64(arg0 + 480, v1)

# ----------------------------------------------------------
# $func1112
# ----------------------------------------------------------
def func1112(arg0):
    store64(arg0, -9187201950435737472)
    store64(arg0 + 32, -9187201950435737472)
    store64(arg0 + 64, -9187201950435737472)
    store64(arg0 + 96, -9187201950435737472)
    store64(arg0 + 128, -9187201950435737472)
    store64(arg0 + 160, -9187201950435737472)
    store64(arg0 + 192, -9187201950435737472)
    store64(arg0 + 224, -9187201950435737472)
    store64(arg0 + 256, -9187201950435737472)
    store64(arg0 + 8, -9187201950435737472)
    store64(arg0 + 40, -9187201950435737472)
    store64(arg0 + 72, -9187201950435737472)
    store64(arg0 + 104, -9187201950435737472)
    store64(arg0 + 136, -9187201950435737472)
    store64(arg0 + 168, -9187201950435737472)
    store64(arg0 + 200, -9187201950435737472)
    store64(arg0 + 232, -9187201950435737472)
    store64(arg0 + 264, -9187201950435737472)
    store64(arg0 + 296, -9187201950435737472)
    store64(arg0 + 288, -9187201950435737472)
    store64(arg0 + 328, -9187201950435737472)
    store64(arg0 + 320, -9187201950435737472)
    store64(arg0 + 360, -9187201950435737472)
    store64(arg0 + 352, -9187201950435737472)
    store64(arg0 + 392, -9187201950435737472)
    store64(arg0 + 384, -9187201950435737472)
    store64(arg0 + 424, -9187201950435737472)
    store64(arg0 + 416, -9187201950435737472)
    store64(arg0 + 456, -9187201950435737472)
    store64(arg0 + 448, -9187201950435737472)
    store64(arg0 + 488, -9187201950435737472)
    store64(arg0 + 480, -9187201950435737472)

# ----------------------------------------------------------
# $func1113
# ----------------------------------------------------------
def func1113(arg0):
    v1 = ((i32(((((load8u((arg0 - 17)) + (load8u((arg0 - 18)) + (load8u((arg0 - 19)) + (load8u((arg0 - 20)) + (load8u((arg0 - 21)) + (load8u((arg0 - 22)) + (load8u((arg0 - 23)) + (load8u((arg0 - 24)) + (load8u((arg0 - 25)) + (load8u((arg0 - 26)) + (load8u((arg0 - 27)) + (load8u((arg0 - 28)) + (load8u((arg0 - 29)) + (load8u((arg0 - 30)) + (load8u((arg0 - 32)) + load8u((arg0 - 31))))))))))))))))) + 8) & 0xFFFFFFFF) >> 4)) & 255) * 72340172838076673)
    store64(arg0, ((i32(((((load8u((arg0 - 17)) + (load8u((arg0 - 18)) + (load8u((arg0 - 19)) + (load8u((arg0 - 20)) + (load8u((arg0 - 21)) + (load8u((arg0 - 22)) + (load8u((arg0 - 23)) + (load8u((arg0 - 24)) + (load8u((arg0 - 25)) + (load8u((arg0 - 26)) + (load8u((arg0 - 27)) + (load8u((arg0 - 28)) + (load8u((arg0 - 29)) + (load8u((arg0 - 30)) + (load8u((arg0 - 32)) + load8u((arg0 - 31))))))))))))))))) + 8) & 0xFFFFFFFF) >> 4)) & 255) * 72340172838076673))
    store64(arg0 + 8, v1)
    store64(arg0 + 40, v1)
    store64(arg0 + 32, v1)
    store64(arg0 + 72, v1)
    store64(arg0 + 64, v1)
    store64(arg0 + 104, v1)
    store64(arg0 + 96, v1)
    store64(arg0 + 136, v1)
    store64(arg0 + 128, v1)
    store64(arg0 + 168, v1)
    store64(arg0 + 160, v1)
    store64(arg0 + 200, v1)
    store64(arg0 + 192, v1)
    store64(arg0 + 232, v1)
    store64(arg0 + 224, v1)
    store64(arg0 + 264, v1)
    store64(arg0 + 256, v1)
    store64(arg0 + 296, v1)
    store64(arg0 + 288, v1)
    store64(arg0 + 328, v1)
    store64(arg0 + 320, v1)
    store64(arg0 + 360, v1)
    store64(arg0 + 352, v1)
    store64(arg0 + 392, v1)
    store64(arg0 + 384, v1)
    store64(arg0 + 424, v1)
    store64(arg0 + 416, v1)
    store64(arg0 + 456, v1)
    store64(arg0 + 448, v1)
    store64(arg0 + 488, v1)
    store64(arg0 + 480, v1)
