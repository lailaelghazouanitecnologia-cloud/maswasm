"""
Auto-generated from WAT. Contains 4 functions.
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
# $func959
# ==========================================================
def func959(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    var8 = ((var4 << 1) & -4)
    if ((var4 << 1) & -4):
        var8 = (var3 + var8)
        while True:  # loop $label0
            var6 = (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)
            var5 = i32_load8_u(var2)
            var9 = i32_load8_u(var1)
            var10 = ((((i32_load8_u(var2) * 13320) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var1) * 6419) & 0xFFFFFFFF) >> 8))
            var7 = ((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) - ((((i32_load8_u(var2) * 13320) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var1) * 6419) & 0xFFFFFFFF) >> 8)))
            var11 = (((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) - ((((i32_load8_u(var2) * 13320) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var1) * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            var7 = ((((((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) - ((((i32_load8_u(var2) * 13320) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var1) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var11 < 16384 else 0) else (255 if (1 if var7 >= -8708 else 0) else 0))
            var5 = (((var5 * 26149) & 0xFFFFFFFF) >> 8)
            var11 = ((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var6)
            var12 = (((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var6) - 14234)
            i32_store8(var3, (((((((((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) - ((((i32_load8_u(var2) * 13320) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var1) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var11 < 16384 else 0) else (255 if (1 if var7 >= -8708 else 0) else 0)) & 0xFFFFFFFF) >> 5) | (((((((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var6) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var12 < 16384 else 0) else (248 if (1 if var11 >= 14234 else 0) else 0)) & 248)))
            var9 = (((var9 * 33050) & 0xFFFFFFFF) >> 8)
            var6 = ((((var9 * 33050) & 0xFFFFFFFF) >> 8) + var6)
            var7 = (((((var9 * 33050) & 0xFFFFFFFF) >> 8) + var6) - 17685)
            i32_store8(var3 + 1, (((var7 << 3) & 224) | ((((((((var9 * 33050) & 0xFFFFFFFF) >> 8) + var6) - 17685) & 0xFFFFFFFF) >> 9) if (1 if var7 < 16384 else 0) else (31 if (1 if var6 >= 17685 else 0) else 0))))
            var6 = (((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8)
            var5 = ((((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + var5)
            var7 = (((((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + var5) - 14234)
            var5 = (var6 - var10)
            var10 = ((var6 - var10) + 8708)
            var5 = (((((var6 - var10) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var10 < 16384 else 0) else (255 if (1 if var5 >= -8708 else 0) else 0))
            i32_store8(var3 + 2, ((((((((((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + var5) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (248 if (1 if var5 >= 14234 else 0) else 0)) & 248) | (((((((var6 - var10) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var10 < 16384 else 0) else (255 if (1 if var5 >= -8708 else 0) else 0)) & 0xFFFFFFFF) >> 5)))
            var6 = (var6 + var9)
            var5 = ((var6 + var9) - 17685)
            i32_store8(var3 + 3, (((var5 << 3) & 224) | (((((var6 + var9) - 17685) & 0xFFFFFFFF) >> 9) if (1 if var5 < 16384 else 0) else (31 if (1 if var6 >= 17685 else 0) else 0))))
            var2 = (var2 + 1)
            var1 = (var1 + 1)
            var0 = (var0 + 2)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var8 else 0):
                continue
            break  # end loop
        var3 = var8
    if (var4 & 1):
        var0 = (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)
        var2 = i32_load8_u(var2)
        var4 = ((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var2) * 26149) & 0xFFFFFFFF) >> 8))
        var8 = (((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var2) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        var1 = i32_load8_u(var1)
        var2 = (var0 - ((((i32_load8_u(var1) * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8)))
        var4 = ((var0 - ((((i32_load8_u(var1) * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        var2 = (((((var0 - ((((i32_load8_u(var1) * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var4 < 16384 else 0) else (255 if (1 if var2 >= -8708 else 0) else 0))
        i32_store8(var3, ((((((((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var2) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (248 if (1 if var4 >= 14234 else 0) else 0)) & 248) | (((((((var0 - ((((i32_load8_u(var1) * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var4 < 16384 else 0) else (255 if (1 if var2 >= -8708 else 0) else 0)) & 0xFFFFFFFF) >> 5)))
        var0 = ((((var1 * 33050) & 0xFFFFFFFF) >> 8) + var0)
        var1 = (((((var1 * 33050) & 0xFFFFFFFF) >> 8) + var0) - 17685)
        i32_store8(var3 + 1, (((var2 << 3) & 224) | ((((((((var1 * 33050) & 0xFFFFFFFF) >> 8) + var0) - 17685) & 0xFFFFFFFF) >> 9) if (1 if var1 < 16384 else 0) else (31 if (1 if var0 >= 17685 else 0) else 0))))


# ==========================================================
# $func960
# ==========================================================
def func960(var0, var1, var2, var3, var4):
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
            var5 = i32_load8_u(var1)
            var8 = i32_load8_u(var2)
            var6 = i32_load8_u(var0)
            i32_store8(var3 + 3, 255)
            var9 = (((var8 * 26149) & 0xFFFFFFFF) >> 8)
            var6 = (((var6 * 19077) & 0xFFFFFFFF) >> 8)
            var10 = ((((var8 * 26149) & 0xFFFFFFFF) >> 8) + (((var6 * 19077) & 0xFFFFFFFF) >> 8))
            var11 = (((((var8 * 26149) & 0xFFFFFFFF) >> 8) + (((var6 * 19077) & 0xFFFFFFFF) >> 8)) - 14234)
            i32_store8(var3 + 2, ((((((((var8 * 26149) & 0xFFFFFFFF) >> 8) + (((var6 * 19077) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var11 < 16384 else 0) else (255 if (1 if var10 >= 14234 else 0) else 0)))
            var10 = (((var5 * 33050) & 0xFFFFFFFF) >> 8)
            var11 = ((((var5 * 33050) & 0xFFFFFFFF) >> 8) + var6)
            var12 = (((((var5 * 33050) & 0xFFFFFFFF) >> 8) + var6) - 17685)
            i32_store8(var3, ((((((((var5 * 33050) & 0xFFFFFFFF) >> 8) + var6) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var12 < 16384 else 0) else (255 if (1 if var11 >= 17685 else 0) else 0)))
            var8 = ((((var8 * 13320) & 0xFFFFFFFF) >> 8) + (((var5 * 6419) & 0xFFFFFFFF) >> 8))
            var5 = (var6 - ((((var8 * 13320) & 0xFFFFFFFF) >> 8) + (((var5 * 6419) & 0xFFFFFFFF) >> 8)))
            var6 = ((var6 - ((((var8 * 13320) & 0xFFFFFFFF) >> 8) + (((var5 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var3 + 1, (((((var6 - ((((var8 * 13320) & 0xFFFFFFFF) >> 8) + (((var5 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var6 < 16384 else 0) else (255 if (1 if var5 >= -8708 else 0) else 0)))
            var5 = i32_load8_u(var0 + 1)
            i32_store8(var3 + 7, 255)
            var5 = (((var5 * 19077) & 0xFFFFFFFF) >> 8)
            var6 = ((((var5 * 19077) & 0xFFFFFFFF) >> 8) + var9)
            var9 = (((((var5 * 19077) & 0xFFFFFFFF) >> 8) + var9) - 14234)
            i32_store8(var3 + 6, ((((((((var5 * 19077) & 0xFFFFFFFF) >> 8) + var9) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var6 >= 14234 else 0) else 0)))
            var8 = (var5 - var8)
            var6 = ((var5 - var8) + 8708)
            i32_store8(var3 + 5, (((((var5 - var8) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var6 < 16384 else 0) else (255 if (1 if var8 >= -8708 else 0) else 0)))
            var5 = (var5 + var10)
            var8 = ((var5 + var10) - 17685)
            i32_store8(var3 + 4, (((((var5 + var10) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (255 if (1 if var5 >= 17685 else 0) else 0)))
            var2 = (var2 + 1)
            var1 = (var1 + 1)
            var0 = (var0 + 2)
            var3 = (var3 + 8)
            if (1 if (var3 + 8) != var7 else 0):
                continue
            break  # end loop
        var3 = var7
    if (var4 & 1):
        var1 = i32_load8_u(var1)
        var2 = i32_load8_u(var2)
        var0 = i32_load8_u(var0)
        i32_store8(var3 + 3, 255)
        var0 = (((var0 * 19077) & 0xFFFFFFFF) >> 8)
        var4 = ((((var0 * 19077) & 0xFFFFFFFF) >> 8) + (((var2 * 26149) & 0xFFFFFFFF) >> 8))
        var7 = (((((var0 * 19077) & 0xFFFFFFFF) >> 8) + (((var2 * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        i32_store8(var3 + 2, ((((((((var0 * 19077) & 0xFFFFFFFF) >> 8) + (((var2 * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var4 >= 14234 else 0) else 0)))
        var4 = ((((var1 * 33050) & 0xFFFFFFFF) >> 8) + var0)
        var7 = (((((var1 * 33050) & 0xFFFFFFFF) >> 8) + var0) - 17685)
        i32_store8(var3, ((((((((var1 * 33050) & 0xFFFFFFFF) >> 8) + var0) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var4 >= 17685 else 0) else 0)))
        var0 = (var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8)))
        var1 = ((var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        i32_store8(var3 + 1, (((((var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var1 < 16384 else 0) else (255 if (1 if var0 >= -8708 else 0) else 0)))


# ==========================================================
# $func961
# ==========================================================
def func961(var0, var1, var2, var3, var4):
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
            var5 = i32_load8_u(var1)
            var8 = i32_load8_u(var2)
            var9 = (((i32_load8_u(var2) * 26149) & 0xFFFFFFFF) >> 8)
            var7 = (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)
            var10 = ((((i32_load8_u(var2) * 26149) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8))
            var11 = (((((i32_load8_u(var2) * 26149) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)) - 14234)
            i32_store8(var3 + 2, ((((((((i32_load8_u(var2) * 26149) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var11 < 16384 else 0) else (255 if (1 if var10 >= 14234 else 0) else 0)))
            var10 = (((var5 * 33050) & 0xFFFFFFFF) >> 8)
            var11 = ((((var5 * 33050) & 0xFFFFFFFF) >> 8) + var7)
            var12 = (((((var5 * 33050) & 0xFFFFFFFF) >> 8) + var7) - 17685)
            i32_store8(var3, ((((((((var5 * 33050) & 0xFFFFFFFF) >> 8) + var7) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var12 < 16384 else 0) else (255 if (1 if var11 >= 17685 else 0) else 0)))
            var7 = ((((var8 * 13320) & 0xFFFFFFFF) >> 8) + (((var5 * 6419) & 0xFFFFFFFF) >> 8))
            var5 = (var7 - ((((var8 * 13320) & 0xFFFFFFFF) >> 8) + (((var5 * 6419) & 0xFFFFFFFF) >> 8)))
            var8 = ((var7 - ((((var8 * 13320) & 0xFFFFFFFF) >> 8) + (((var5 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var3 + 1, (((((var7 - ((((var8 * 13320) & 0xFFFFFFFF) >> 8) + (((var5 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (255 if (1 if var5 >= -8708 else 0) else 0)))
            var5 = (((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8)
            var8 = ((((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + var9)
            var9 = (((((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + var9) - 14234)
            i32_store8(var3 + 5, ((((((((i32_load8_u(var0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + var9) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var8 >= 14234 else 0) else 0)))
            var7 = (var5 - var7)
            var8 = ((var5 - var7) + 8708)
            i32_store8(var3 + 4, (((((var5 - var7) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (255 if (1 if var7 >= -8708 else 0) else 0)))
            var5 = (var5 + var10)
            var7 = ((var5 + var10) - 17685)
            i32_store8(var3 + 3, (((((var5 + var10) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var5 >= 17685 else 0) else 0)))
            var2 = (var2 + 1)
            var1 = (var1 + 1)
            var0 = (var0 + 2)
            var3 = (var3 + 6)
            if (1 if (var3 + 6) != var6 else 0):
                continue
            break  # end loop
        var3 = var6
    if (var4 & 1):
        var1 = i32_load8_u(var1)
        var0 = (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)
        var2 = i32_load8_u(var2)
        var4 = ((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var2) * 26149) & 0xFFFFFFFF) >> 8))
        var6 = (((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var2) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        i32_store8(var3 + 2, ((((((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u(var2) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var6 < 16384 else 0) else (255 if (1 if var4 >= 14234 else 0) else 0)))
        var4 = ((((var1 * 33050) & 0xFFFFFFFF) >> 8) + var0)
        var6 = (((((var1 * 33050) & 0xFFFFFFFF) >> 8) + var0) - 17685)
        i32_store8(var3, ((((((((var1 * 33050) & 0xFFFFFFFF) >> 8) + var0) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var6 < 16384 else 0) else (255 if (1 if var4 >= 17685 else 0) else 0)))
        var0 = (var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8)))
        var1 = ((var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        i32_store8(var3 + 1, (((((var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var1 < 16384 else 0) else (255 if (1 if var0 >= -8708 else 0) else 0)))


# ==========================================================
# $func962
# ==========================================================
def func962(var0, var1, var2, var3, var4):
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
            i32_store8(var3, 255)
            var9 = (((var8 * 33050) & 0xFFFFFFFF) >> 8)
            var6 = (((var6 * 19077) & 0xFFFFFFFF) >> 8)
            var10 = ((((var8 * 33050) & 0xFFFFFFFF) >> 8) + (((var6 * 19077) & 0xFFFFFFFF) >> 8))
            var11 = (((((var8 * 33050) & 0xFFFFFFFF) >> 8) + (((var6 * 19077) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8(var3 + 3, ((((((((var8 * 33050) & 0xFFFFFFFF) >> 8) + (((var6 * 19077) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var11 < 16384 else 0) else (255 if (1 if var10 >= 17685 else 0) else 0)))
            var10 = (((var5 * 26149) & 0xFFFFFFFF) >> 8)
            var11 = ((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var6)
            var12 = (((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var6) - 14234)
            i32_store8(var3 + 1, ((((((((var5 * 26149) & 0xFFFFFFFF) >> 8) + var6) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var12 < 16384 else 0) else (255 if (1 if var11 >= 14234 else 0) else 0)))
            var8 = ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var8 * 6419) & 0xFFFFFFFF) >> 8))
            var5 = (var6 - ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var8 * 6419) & 0xFFFFFFFF) >> 8)))
            var6 = ((var6 - ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var8 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var3 + 2, (((((var6 - ((((var5 * 13320) & 0xFFFFFFFF) >> 8) + (((var8 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var6 < 16384 else 0) else (255 if (1 if var5 >= -8708 else 0) else 0)))
            var5 = i32_load8_u(var0 + 1)
            i32_store8(var3 + 4, 255)
            var5 = (((var5 * 19077) & 0xFFFFFFFF) >> 8)
            var6 = ((((var5 * 19077) & 0xFFFFFFFF) >> 8) + var9)
            var9 = (((((var5 * 19077) & 0xFFFFFFFF) >> 8) + var9) - 17685)
            i32_store8(var3 + 7, ((((((((var5 * 19077) & 0xFFFFFFFF) >> 8) + var9) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var6 >= 17685 else 0) else 0)))
            var8 = (var5 - var8)
            var6 = ((var5 - var8) + 8708)
            i32_store8(var3 + 6, (((((var5 - var8) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var6 < 16384 else 0) else (255 if (1 if var8 >= -8708 else 0) else 0)))
            var5 = (var5 + var10)
            var8 = ((var5 + var10) - 14234)
            i32_store8(var3 + 5, (((((var5 + var10) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (255 if (1 if var5 >= 14234 else 0) else 0)))
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
        i32_store8(var3, 255)
        var0 = (((var0 * 19077) & 0xFFFFFFFF) >> 8)
        var4 = ((((var0 * 19077) & 0xFFFFFFFF) >> 8) + (((var1 * 33050) & 0xFFFFFFFF) >> 8))
        var7 = (((((var0 * 19077) & 0xFFFFFFFF) >> 8) + (((var1 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var3 + 3, ((((((((var0 * 19077) & 0xFFFFFFFF) >> 8) + (((var1 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var4 >= 17685 else 0) else 0)))
        var4 = ((((var2 * 26149) & 0xFFFFFFFF) >> 8) + var0)
        var7 = (((((var2 * 26149) & 0xFFFFFFFF) >> 8) + var0) - 14234)
        i32_store8(var3 + 1, ((((((((var2 * 26149) & 0xFFFFFFFF) >> 8) + var0) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var4 >= 14234 else 0) else 0)))
        var0 = (var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8)))
        var1 = ((var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        i32_store8(var3 + 2, (((((var0 - ((((var1 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var1 < 16384 else 0) else (255 if (1 if var0 >= -8708 else 0) else 0)))

