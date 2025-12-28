"""
Auto-generated from WAT. Contains 7 functions.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from runtime import (
    memory, i32_load, i64_load, f32_load, f64_load,
    i32_store, i64_store, f32_store, f64_store,
    i32_load8_s, i32_load8_u, i32_load16_s, i32_load16_u,
    i64_load8_s, i64_load8_u, i64_load16_s, i64_load16_u,
    i64_load32_s, i64_load32_u,
    i32_store8, i32_store16, i64_store8, i64_store16, i64_store32,
    i32_atomic_load, i64_atomic_load,
    i32_atomic_store, i64_atomic_store,
    global0, global1, global2, global3, global4,
    global5, global6, global7, global8,
    i32, i64, i64_extend_s, i64_extend_u,
    rotl32, rotr32, rotl64, rotr64,
    clz32, ctz32, popcnt32, clz64, ctz64, popcnt64,
    call_indirect,
)

# ==========================================================
# $func905
# ==========================================================
def func905(var0, var1, var2, var3, var4):
    var2 = i32_load(9671128)
    var3 = (i32_load(9671128) + (i32_load(var1) * 132))
    if (1 if i32_load(38564) != i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 122) else 0):
        break
    var1 = 1
    # br_table ['$label0', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label0', '$label1']
    _br_idx = (i32_load8_u(var3 + 125) - 4)
    break  # br_table
    var1 = 1
    var0 = i32_load8_u((var2 + (var0 * 132)) + 122)
    # br_table ['$label2', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label2', '$label3']
    _br_idx = (i32_load8_u((var2 + (var0 * 132)) + 122) + -64)
    break  # br_table
    if (1 if var0 != 10 else 0):
        break
    var1 = 0
    return var1


# ==========================================================
# $func922
# ==========================================================
def func922(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = 0
    var3 = i32_load(9561692)
    var5 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var4 = i32_load(59164)
    var1 = 1
    while True:  # loop $label1
        var6 = (var3 + (var1 * 286704))
        if (1 if var4 == i32_load((var3 + (var1 * 286704)) + 284616) else 0):
            var2 = var1
            break
        if (1 if var4 == i32_load(var6 + 284628) else 0):
            var2 = var1
            break
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var5 else 0):
            continue
        break  # end loop
    var1 = (var3 + (var2 * 286704))
    i32_store((var3 + (var2 * 286704)) + 283928, i32_load(var0))
    i32_store(var1 + 283932, i32_load(var0 + 4))


# ==========================================================
# $func926
# ==========================================================
def func926(var0, var1, var2, var3, var4):
    var0 = i32_load(var1)
    if i32_load(var1):
        if i32_load8_u(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 335):
            break
    return 1


# ==========================================================
# $func939
# ==========================================================
def func939():
    # br_table ['$label0', '$label1', '$label2']
    _br_idx = 1
    break  # br_table
    global global1
    global1 = 1024
    # Unknown: memory.fill []
    # Unknown: memory.init [0]
    # Unknown: memory.fill []
    # Unknown: memory.init [1]
    # Unknown: memory.fill []
    # Unknown: memory.init [2]
    # Unknown: memory.fill []
    # Unknown: memory.init [3]
    # Unknown: memory.fill []
    # Unknown: memory.init [4]
    # Unknown: memory.fill []
    # Unknown: memory.init [5]
    # Unknown: memory.fill []
    # Unknown: memory.init [6]
    # Unknown: memory.fill []
    # Unknown: memory.init [7]
    # Unknown: memory.fill []
    # Unknown: memory.init [8]
    # Unknown: memory.fill []
    # Unknown: memory.init [9]
    # Unknown: memory.fill []
    # Unknown: memory.init [10]
    # Unknown: memory.init [11]
    # Unknown: memory.fill []
    # Unknown: memory.init [12]
    # Unknown: memory.fill []
    # Unknown: memory.init [13]
    # Unknown: memory.fill []
    # Unknown: memory.init [14]
    # Unknown: memory.fill []
    # Unknown: memory.init [15]
    # Unknown: memory.fill []
    # Unknown: memory.init [16]
    # Unknown: memory.fill []
    i32_atomic_store(9690988, 2)
    break
    # Unknown: data.drop [0]
    # Unknown: data.drop [1]
    # Unknown: data.drop [2]
    # Unknown: data.drop [3]
    # Unknown: data.drop [4]
    # Unknown: data.drop [5]
    # Unknown: data.drop [6]
    # Unknown: data.drop [7]
    # Unknown: data.drop [8]
    # Unknown: data.drop [9]
    # Unknown: data.drop [10]
    # Unknown: data.drop [11]
    # Unknown: data.drop [12]
    # Unknown: data.drop [13]
    # Unknown: data.drop [14]
    # Unknown: data.drop [15]
    # Unknown: data.drop [16]


# ==========================================================
# $func956
# ==========================================================
def func956(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    var7 = ((var4 << 2) & -8)
    if ((var4 << 2) & -8):
        var7 = (var3 + var7)
        while True:  # loop $label0
            var5 = i32_load8_u(var2)
            var8 = i32_load8_u(var1)
            var6 = i32_load8_u(var0)
            i32_store8(var3 + 3, 255)
            var9 = (((var8 * 33050) & 0xFFFFFFFF) >> 8)
            var6 = (((var6 * 19077) & 0xFFFFFFFF) >> 8)
            var10 = ((((var8 * 33050) & 0xFFFFFFFF) >> 8) + (((var6 * 19077) & 0xFFFFFFFF) >> 8))
            var11 = (((((var8 * 33050) & 0xFFFFFFFF) >> 8) + (((var6 * 19077) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8(var3 + 2, ((((((((var8 * 33050) & 0xFFFFFFFF) >> 8) + (((var6 * 19077) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var11 < 16384 else 0) else (255 if (1 if var10 >= 17685 else 0) else 0)))
            var10 = (((var5 * 26149) & 0xFFFFFFFF) >> 8)
            var11 = ((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var6)
            var12 = (((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var6) - 14234)
            i32_store8(var3, ((((((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var6) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var12 < 16384 else 0) else (255 if (1 if var11 >= 14234 else 0) else 0)))
            var8 = ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var8 * 6419) & 0xFFFFFFFF) >> 8))
            var5 = (var6 - ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var8 * 6419) & 0xFFFFFFFF) >> 8)))
            var6 = ((var6 - ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var8 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var3 + 1, (((((var6 - ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var8 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var6 < 16384 else 0) else (255 if (1 if var5 >= -8708 else 0) else 0)))
            var5 = i32_load8_u(var0 + 1)
            i32_store8(var3 + 7, 255)
            var5 = (((var5 * 19077) & 0xFFFFFFFF) >> 8)
            var6 = ((((var5 * 19077) & 0xFFFFFFFF) >> 8) + var9)
            var9 = (((((var5 * 19077) & 0xFFFFFFFF) >> 8) + var9) - 17685)
            i32_store8(var3 + 6, ((((((((var5 * 19077) & 0xFFFFFFFF) >> 8) + var9) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var6 >= 17685 else 0) else 0)))
            var8 = (var5 - var8)
            var6 = ((var5 - var8) + 8708)
            i32_store8(var3 + 5, (((((var5 - var8) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var6 < 16384 else 0) else (255 if (1 if var8 >= -8708 else 0) else 0)))
            var5 = (var5 + var10)
            var8 = ((var5 + var10) - 14234)
            i32_store8(var3 + 4, (((((var5 + var10) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (255 if (1 if var5 >= 14234 else 0) else 0)))
            var2 = (var2 + 1)
            var1 = (var1 + 1)
            var0 = (var0 + 2)
            var3 = (var3 + 8)
            if (1 if (var3 + 8) != var7 else 0):
                continue
            break  # end loop
        var3 = var7
    if (var4 & 1):
        var2 = i32_load8_u(var2)
        var1 = i32_load8_u(var1)
        var0 = i32_load8_u(var0)
        i32_store8(var3 + 3, 255)
        var0 = (((var0 * 19077) & 0xFFFFFFFF) >> 8)
        var4 = ((((var0 * 19077) & 0xFFFFFFFF) >> 8) + (((var1 * 33050) & 0xFFFFFFFF) >> 8))
        var7 = (((((var0 * 19077) & 0xFFFFFFFF) >> 8) + (((var1 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var3 + 2, ((((((((var0 * 19077) & 0xFFFFFFFF) >> 8) + (((var1 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var4 >= 17685 else 0) else 0)))
        var4 = ((((var2 * 26149) & 0xFFFFFFFF) >> 8) + var0)
        var7 = (((((var2 * 26149) & 0xFFFFFFFF) >> 8) + var0) - 14234)
        i32_store8(var3, ((((((((var2 * 26149) & 0xFFFFFFFF) >> 8) + var0) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var4 >= 14234 else 0) else 0)))
        var0 = (var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8)))
        var1 = ((var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        i32_store8(var3 + 1, (((((var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var1 < 16384 else 0) else (255 if (1 if var0 >= -8708 else 0) else 0)))


# ==========================================================
# $func957
# ==========================================================
def func957(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    var7 = ((var4 << 1) & -4)
    if ((var4 << 1) & -4):
        var7 = (var3 + var7)
        while True:  # loop $label0
            var5 = i32_load8_u(var2)
            var6 = i32_load8_u(var1)
            var9 = (((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8)
            var8 = (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)
            var10 = ((((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8))
            var11 = (((((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8(var3 + 1, (((((((((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var11 < 16384 else 0) else (240 if (1 if var10 >= 17685 else 0) else 0)) | 15))
            var10 = (((var5 * 26149) & 0xFFFFFFFF) >> 8)
            var11 = ((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var8)
            var12 = (((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var8) - 14234)
            var8 = ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var6 * 6419) & 0xFFFFFFFF) >> 8))
            var5 = (var8 - ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var6 * 6419) & 0xFFFFFFFF) >> 8)))
            var6 = ((var8 - ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var6 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var3, ((((((((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var8) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var12 < 16384 else 0) else (240 if (1 if var11 >= 14234 else 0) else 0)) & 240) | (((((var8 - ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var6 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (1 if var6 < 16384 else 0) else (15 if (1 if var5 >= -8708 else 0) else 0))))
            var5 = (((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8)
            var6 = ((((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + var9)
            var9 = (((((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + var9) - 17685)
            i32_store8(var3 + 3, (((((((((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + var9) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (240 if (1 if var6 >= 17685 else 0) else 0)) | 15))
            var6 = (var5 + var10)
            var9 = ((var5 + var10) - 14234)
            var5 = (var5 - var8)
            var8 = ((var5 - var8) + 8708)
            i32_store8(var3 + 2, (((((((var5 + var10) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (240 if (1 if var6 >= 14234 else 0) else 0)) & 240) | (((((var5 - var8) + 8708) & 0xFFFFFFFF) >> 10) if (1 if var8 < 16384 else 0) else (15 if (1 if var5 >= -8708 else 0) else 0))))
            var2 = (var2 + 1)
            var1 = (var1 + 1)
            var0 = (var0 + 2)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var7 else 0):
                continue
            break  # end loop
        var3 = var7
    if (var4 & 1):
        var2 = i32_load8_u(var2)
        var0 = (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)
        var1 = i32_load8_u(var1)
        var4 = ((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8))
        var7 = (((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var3 + 1, (((((((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (240 if (1 if var4 >= 17685 else 0) else 0)) | 15))
        var3 = ((((var2 * 26149) & 0xFFFFFFFF) >> 8) + var0)
        var4 = (((((var2 * 26149) & 0xFFFFFFFF) >> 8) + var0) - 14234)
        var0 = (var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8)))
        var1 = ((var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        i32_store8(var3, ((((((((((var2 * 26149) & 0xFFFFFFFF) >> 8) + var0) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var4 < 16384 else 0) else (240 if (1 if var3 >= 14234 else 0) else 0)) & 240) | (((((var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (1 if var1 < 16384 else 0) else (15 if (1 if var0 >= -8708 else 0) else 0))))


# ==========================================================
# $func958
# ==========================================================
def func958(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    var6 = (var4 & -2)
    if (var4 & -2):
        var6 = (var3 + (var6 * 3))
        while True:  # loop $label0
            var5 = i32_load8_u(var2)
            var8 = i32_load8_u(var1)
            var9 = (((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8)
            var7 = (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)
            var10 = ((((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8))
            var11 = (((((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8(var3 + 2, ((((((((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var11 < 16384 else 0) else (255 if (1 if var10 >= 17685 else 0) else 0)))
            var10 = (((var5 * 26149) & 0xFFFFFFFF) >> 8)
            var11 = ((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var7)
            var12 = (((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var7) - 14234)
            i32_store8(var3, ((((((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var7) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var12 < 16384 else 0) else (255 if (1 if var11 >= 14234 else 0) else 0)))
            var7 = ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var8 * 6419) & 0xFFFFFFFF) >> 8))
            var5 = (var7 - ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var8 * 6419) & 0xFFFFFFFF) >> 8)))
            var8 = ((var7 - ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var8 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var3 + 1, (((((var7 - ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var8 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (255 if (1 if var5 >= -8708 else 0) else 0)))
            var5 = (((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8)
            var8 = ((((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + var9)
            var9 = (((((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + var9) - 17685)
            i32_store8(var3 + 5, ((((((((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + var9) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var8 >= 17685 else 0) else 0)))
            var7 = (var5 - var7)
            var8 = ((var5 - var7) + 8708)
            i32_store8(var3 + 4, (((((var5 - var7) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (255 if (1 if var7 >= -8708 else 0) else 0)))
            var5 = (var5 + var10)
            var7 = ((var5 + var10) - 14234)
            i32_store8(var3 + 3, (((((var5 + var10) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var5 >= 14234 else 0) else 0)))
            var2 = (var2 + 1)
            var1 = (var1 + 1)
            var0 = (var0 + 2)
            var3 = (var3 + 6)
            if (1 if (var3 + 6) != var6 else 0):
                continue
            break  # end loop
        var3 = var6
    if (var4 & 1):
        var2 = i32_load8_u(var2)
        var0 = (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)
        var1 = i32_load8_u(var1)
        var4 = ((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8))
        var6 = (((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var3 + 2, ((((((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var1) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var6 < 16384 else 0) else (255 if (1 if var4 >= 17685 else 0) else 0)))
        var4 = ((((var2 * 26149) & 0xFFFFFFFF) >> 8) + var0)
        var6 = (((((var2 * 26149) & 0xFFFFFFFF) >> 8) + var0) - 14234)
        i32_store8(var3, ((((((((var2 * 26149) & 0xFFFFFFFF) >> 8) + var0) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var6 < 16384 else 0) else (255 if (1 if var4 >= 14234 else 0) else 0)))
        var0 = (var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8)))
        var1 = ((var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        i32_store8(var3 + 1, (((((var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var1 < 16384 else 0) else (255 if (1 if var0 >= -8708 else 0) else 0)))

