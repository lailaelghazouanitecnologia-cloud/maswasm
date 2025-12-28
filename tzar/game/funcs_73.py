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
# $func1016
# ==========================================================
def func1016(var0, var1, var2, var3, var4, var5, var6, var7, var8):
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    var13 = 0
    var14 = 0
    var15 = 0
    var16 = 0
    var17 = 0
    var18 = 0
    var19 = 0
    var20 = 0
    var21 = 0
    var22 = 0
    var23 = 0
    var24 = 0
    var25 = 0
    var26 = 0
    if var0:
        var10 = i32_load8_u(var5)
        var13 = i32_load8_u(var4)
        var12 = i32_load8_u(var3)
        var14 = i32_load8_u(var2)
        var11 = i32_load8_u(var0)
        i32_store8(var6, 255)
        var11 = (((var11 * 19077) & 0xFFFFFFFF) >> 8)
        var13 = (var13 | (var10 << 16))
        var10 = (var14 | (var12 << 16))
        var12 = (((var13 | (var10 << 16)) + ((var14 | (var12 << 16)) * 3)) + 131074)
        var14 = ((((((var13 | (var10 << 16)) + ((var14 | (var12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
        var16 = ((((var11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((var13 | (var10 << 16)) + ((var14 | (var12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
        var9 = (((((var11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((var13 | (var10 << 16)) + ((var14 | (var12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var6 + 3, ((((((((var11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((var13 | (var10 << 16)) + ((var14 | (var12 << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var16 >= 17685 else 0) else 0)))
        var12 = (((var12 & 0xFFFFFFFF) >> 18) & 255)
        var16 = (var11 + ((((((var12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
        var9 = ((var11 + ((((((var12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        i32_store8(var6 + 1, (((((var11 + ((((((var12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var16 >= 14234 else 0) else 0)))
        var11 = (var11 - ((((var14 * 6419) & 0xFFFFFFFF) >> 8) + (((var12 * 13320) & 0xFFFFFFFF) >> 8)))
        var12 = ((var11 - ((((var14 * 6419) & 0xFFFFFFFF) >> 8) + (((var12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        i32_store8(var6 + 2, (((((var11 - ((((var14 * 6419) & 0xFFFFFFFF) >> 8) + (((var12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var12 < 16384 else 0) else (255 if (1 if var11 >= -8708 else 0) else 0)))
        if var1:
            var11 = i32_load8_u(var1)
            i32_store8(var7, 255)
            var11 = (((var11 * 19077) & 0xFFFFFFFF) >> 8)
            var12 = ((var10 + (var13 * 3)) + 131074)
            var14 = (((((var10 + (var13 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
            var16 = ((((var11 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((var10 + (var13 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            var9 = (((((var11 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((var10 + (var13 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8(var7 + 3, ((((((((var11 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((var10 + (var13 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var16 >= 17685 else 0) else 0)))
            var12 = (((var12 & 0xFFFFFFFF) >> 18) & 255)
            var16 = (var11 + ((((((var12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
            var9 = ((var11 + ((((((var12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            i32_store8(var7 + 1, (((((var11 + ((((((var12 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var16 >= 14234 else 0) else 0)))
            var11 = (var11 - ((((var14 * 6419) & 0xFFFFFFFF) >> 8) + (((var12 * 13320) & 0xFFFFFFFF) >> 8)))
            var12 = ((var11 - ((((var14 * 6419) & 0xFFFFFFFF) >> 8) + (((var12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var7 + 2, (((((var11 - ((((var14 * 6419) & 0xFFFFFFFF) >> 8) + (((var12 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var12 < 16384 else 0) else (255 if (1 if var11 >= -8708 else 0) else 0)))
        var16 = (var8 - 1)
        if (1 if var8 < 3 else 0):
            var11 = var13
            var12 = var10
            break
        var11 = (var16 >> 1)
        var25 = (1 if (1 if var11 <= 1 else 0) else (var16 >> 1))
        var14 = 1
        while True:  # loop $label1
            var21 = (var14 << 1)
            var18 = ((var14 << 1) - 1)
            var11 = i32_load8_u((var0 + ((var14 << 1) - 1)))
            var12 = i32_load8_u((var2 + var14))
            var22 = i32_load8_u((var3 + var14))
            var17 = i32_load8_u((var4 + var14))
            var19 = i32_load8_u((var5 + var14))
            var26 = (var18 << 2)
            var9 = (var6 + (var18 << 2))
            i32_store8((var6 + (var18 << 2)), 255)
            var15 = (((var11 * 19077) & 0xFFFFFFFF) >> 8)
            var11 = (var17 | (var19 << 16))
            var12 = (var12 | (var22 << 16))
            var22 = ((var12 | (var22 << 16)) + var13)
            var17 = (((var17 | (var19 << 16)) + (((var12 | (var22 << 16)) + var13) + var10)) + 524296)
            var22 = ((((((var17 | (var19 << 16)) + (((var12 | (var22 << 16)) + var13) + var10)) + 524296) + (var22 << 1)) & 0xFFFFFFFF) >> 3)
            var19 = (((((((var17 | (var19 << 16)) + (((var12 | (var22 << 16)) + var13) + var10)) + 524296) + (var22 << 1)) & 0xFFFFFFFF) >> 3) + var10)
            var23 = ((((((((((var17 | (var19 << 16)) + (((var12 | (var22 << 16)) + var13) + var10)) + 524296) + (var22 << 1)) & 0xFFFFFFFF) >> 3) + var10) & 0xFFFFFFFF) >> 1) & 255)
            var20 = ((((var11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((var17 | (var19 << 16)) + (((var12 | (var22 << 16)) + var13) + var10)) + 524296) + (var22 << 1)) & 0xFFFFFFFF) >> 3) + var10) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            var24 = (((((var11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((var17 | (var19 << 16)) + (((var12 | (var22 << 16)) + var13) + var10)) + 524296) + (var22 << 1)) & 0xFFFFFFFF) >> 3) + var10) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8(var9 + 3, ((((((((var11 * 19077) & 0xFFFFFFFF) >> 8) + (((((((((((((var17 | (var19 << 16)) + (((var12 | (var22 << 16)) + var13) + var10)) + 524296) + (var22 << 1)) & 0xFFFFFFFF) >> 3) + var10) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var24 < 16384 else 0) else (255 if (1 if var20 >= 17685 else 0) else 0)))
            var19 = (((var19 & 0xFFFFFFFF) >> 17) & 255)
            var20 = (((((((var19 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8) + var15)
            var24 = ((((((((var19 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8) + var15) - 14234)
            i32_store8(var9 + 1, (((((((((((var19 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8) + var15) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var24 < 16384 else 0) else (255 if (1 if var20 >= 14234 else 0) else 0)))
            var9 = (var15 - ((((var19 * 13320) & 0xFFFFFFFF) >> 8) + (((var23 * 6419) & 0xFFFFFFFF) >> 8)))
            var15 = ((var15 - ((((var19 * 13320) & 0xFFFFFFFF) >> 8) + (((var23 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var9 + 2, (((((var15 - ((((var19 * 13320) & 0xFFFFFFFF) >> 8) + (((var23 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var15 < 16384 else 0) else (255 if (1 if var9 >= -8708 else 0) else 0)))
            var15 = i32_load8_u((var0 + var21))
            var19 = (var14 << 3)
            var9 = (var6 + (var14 << 3))
            i32_store8((var6 + (var14 << 3)), 255)
            var15 = (((var15 * 19077) & 0xFFFFFFFF) >> 8)
            var17 = (((var17 + ((var10 + var11) << 1)) & 0xFFFFFFFF) >> 3)
            var10 = ((((var17 + ((var10 + var11) << 1)) & 0xFFFFFFFF) >> 3) + var12)
            var23 = (((((((var17 + ((var10 + var11) << 1)) & 0xFFFFFFFF) >> 3) + var12) & 0xFFFFFFFF) >> 1) & 255)
            var20 = ((((var15 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((var17 + ((var10 + var11) << 1)) & 0xFFFFFFFF) >> 3) + var12) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            var24 = (((((var15 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((var17 + ((var10 + var11) << 1)) & 0xFFFFFFFF) >> 3) + var12) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8(var9 + 3, ((((((((var15 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((var17 + ((var10 + var11) << 1)) & 0xFFFFFFFF) >> 3) + var12) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var24 < 16384 else 0) else (255 if (1 if var20 >= 17685 else 0) else 0)))
            var10 = (((var10 & 0xFFFFFFFF) >> 17) & 255)
            var23 = (var15 - (((((((var10 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8) + (((var23 * 6419) & 0xFFFFFFFF) >> 8)))
            var20 = ((var15 - (((((((var10 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8) + (((var23 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var9 + 2, (((((var15 - (((((((var10 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8) + (((var23 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var20 < 16384 else 0) else (255 if (1 if var23 >= -8708 else 0) else 0)))
            var10 = ((((var10 * 26149) & 0xFFFFFFFF) >> 8) + var15)
            var9 = (((((var10 * 26149) & 0xFFFFFFFF) >> 8) + var15) - 14234)
            i32_store8(var9 + 1, ((((((((var10 * 26149) & 0xFFFFFFFF) >> 8) + var15) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var10 >= 14234 else 0) else 0)))
            if var1:
                var9 = i32_load8_u((var1 + var18))
                var10 = (var7 + var26)
                i32_store8((var7 + var26), 255)
                var9 = (((var9 * 19077) & 0xFFFFFFFF) >> 8)
                var13 = (var13 + var17)
                var18 = ((((var13 + var17) & 0xFFFFFFFF) >> 1) & 255)
                var15 = ((((var9 * 19077) & 0xFFFFFFFF) >> 8) + (((((((var13 + var17) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                var17 = (((((var9 * 19077) & 0xFFFFFFFF) >> 8) + (((((((var13 + var17) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                i32_store8(var10 + 3, ((((((((var9 * 19077) & 0xFFFFFFFF) >> 8) + (((((((var13 + var17) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var17 < 16384 else 0) else (255 if (1 if var15 >= 17685 else 0) else 0)))
                var13 = (((var13 & 0xFFFFFFFF) >> 17) & 255)
                var15 = (var9 + ((((((var13 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8))
                var17 = ((var9 + ((((((var13 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                i32_store8(var10 + 1, (((((var9 + ((((((var13 & 0xFFFFFFFF) >> 17) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var17 < 16384 else 0) else (255 if (1 if var15 >= 14234 else 0) else 0)))
                var10 = (var9 - ((((var18 * 6419) & 0xFFFFFFFF) >> 8) + (((var13 * 13320) & 0xFFFFFFFF) >> 8)))
                var13 = ((var9 - ((((var18 * 6419) & 0xFFFFFFFF) >> 8) + (((var13 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                i32_store8(var10 + 2, (((((var9 - ((((var18 * 6419) & 0xFFFFFFFF) >> 8) + (((var13 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var13 < 16384 else 0) else (255 if (1 if var10 >= -8708 else 0) else 0)))
                var13 = i32_load8_u((var1 + var21))
                var10 = (var7 + var19)
                i32_store8((var7 + var19), 255)
                var13 = (((var13 * 19077) & 0xFFFFFFFF) >> 8)
                var9 = (var11 + var22)
                var21 = ((((var11 + var22) & 0xFFFFFFFF) >> 1) & 255)
                var18 = ((((var13 * 19077) & 0xFFFFFFFF) >> 8) + (((((((var11 + var22) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                var15 = (((((var13 * 19077) & 0xFFFFFFFF) >> 8) + (((((((var11 + var22) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                i32_store8(var10 + 3, ((((((((var13 * 19077) & 0xFFFFFFFF) >> 8) + (((((((var11 + var22) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var15 < 16384 else 0) else (255 if (1 if var18 >= 17685 else 0) else 0)))
                var9 = (((var9 & 0xFFFFFFFF) >> 17) & 255)
                var21 = (var13 - ((((var21 * 6419) & 0xFFFFFFFF) >> 8) + ((((((var9 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8)))
                var18 = ((var13 - ((((var21 * 6419) & 0xFFFFFFFF) >> 8) + ((((((var9 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                i32_store8(var10 + 2, (((((var13 - ((((var21 * 6419) & 0xFFFFFFFF) >> 8) + ((((((var9 & 0xFFFFFFFF) >> 17) & 255) * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var18 < 16384 else 0) else (255 if (1 if var21 >= -8708 else 0) else 0)))
                var10 = (var13 + (((var9 * 26149) & 0xFFFFFFFF) >> 8))
                var13 = ((var13 + (((var9 * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                i32_store8(var10 + 1, (((((var13 + (((var9 * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var13 < 16384 else 0) else (255 if (1 if var10 >= 14234 else 0) else 0)))
            var9 = (1 if var14 != var25 else 0)
            var14 = (var14 + 1)
            var10 = var12
            var13 = var11
            if var9:
                continue
            break  # end loop
        if (var8 & 1):
            break
        var2 = i32_load8_u((var0 + var16))
        var3 = (var16 << 2)
        var0 = (var6 + (var16 << 2))
        i32_store8((var6 + (var16 << 2)), 255)
        var2 = (((var2 * 19077) & 0xFFFFFFFF) >> 8)
        var4 = ((var11 + (var12 * 3)) + 131074)
        var5 = (((((var11 + (var12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
        var6 = ((((var2 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((var11 + (var12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
        var8 = (((((var2 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((var11 + (var12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var0 + 3, ((((((((var2 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((var11 + (var12 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (255 if (1 if var6 >= 17685 else 0) else 0)))
        var4 = (((var4 & 0xFFFFFFFF) >> 18) & 255)
        var6 = (var2 + ((((((var4 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
        var8 = ((var2 + ((((((var4 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        i32_store8(var0 + 1, (((((var2 + ((((((var4 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (255 if (1 if var6 >= 14234 else 0) else 0)))
        var0 = (var2 - ((((var5 * 6419) & 0xFFFFFFFF) >> 8) + (((var4 * 13320) & 0xFFFFFFFF) >> 8)))
        var2 = ((var2 - ((((var5 * 6419) & 0xFFFFFFFF) >> 8) + (((var4 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        i32_store8(var0 + 2, (((((var2 - ((((var5 * 6419) & 0xFFFFFFFF) >> 8) + (((var4 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var2 < 16384 else 0) else (255 if (1 if var0 >= -8708 else 0) else 0)))
        if (1 if var1 == 0 else 0):
            break
        var1 = i32_load8_u((var1 + var16))
        var0 = (var3 + var7)
        i32_store8((var3 + var7), 255)
        var1 = (((var1 * 19077) & 0xFFFFFFFF) >> 8)
        var2 = ((var12 + (var11 * 3)) + 131074)
        var3 = (((((var12 + (var11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255)
        var4 = ((((var1 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((var12 + (var11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
        var5 = (((((var1 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((var12 + (var11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var0 + 3, ((((((((var1 * 19077) & 0xFFFFFFFF) >> 8) + ((((((((var12 + (var11 * 3)) + 131074) & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var5 < 16384 else 0) else (255 if (1 if var4 >= 17685 else 0) else 0)))
        var2 = (((var2 & 0xFFFFFFFF) >> 18) & 255)
        var4 = (var1 + ((((((var2 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8))
        var5 = ((var1 + ((((((var2 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        i32_store8(var0 + 1, (((((var1 + ((((((var2 & 0xFFFFFFFF) >> 18) & 255) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var5 < 16384 else 0) else (255 if (1 if var4 >= 14234 else 0) else 0)))
        var0 = (var1 - ((((var3 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8)))
        var1 = ((var1 - ((((var3 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        i32_store8(var0 + 2, (((((var1 - ((((var3 * 6419) & 0xFFFFFFFF) >> 8) + (((var2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var1 < 16384 else 0) else (255 if (1 if var0 >= -8708 else 0) else 0)))
        return
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func1037
# ==========================================================
def func1037(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if var1:
        if (1 if var2 > 0 else 0):
            while True:  # loop $label0
                var5 = (var6 << 2)
                var4 = (var1 + var5)
                var7 = i32_load((var1 + var5) + 4)
                var4 = i32_load(var4)
                var4 = (((((i32_load((var1 + var5) + 4) ^ i32_load(var4)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var7))
                var5 = i32_load((var0 + var5))
                i32_store((var3 + (var6 << 2)), (((((((((i32_load((var1 + var5) + 4) ^ i32_load(var4)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var7)) & -16711936) + (i32_load((var0 + var5)) & -16711936)) & -16711936) | (((var4 & 16711935) + (var5 & 16711935)) & 16711935)))
                var6 = (var6 + 1)
                if (1 if (var6 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func1038
# ==========================================================
def func1038(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if var1:
        if (1 if var2 > 0 else 0):
            while True:  # loop $label0
                var5 = (var6 << 2)
                var4 = (var1 + var5)
                var7 = i32_load((var1 + var5))
                var4 = i32_load((var4 - 4))
                var4 = (((((i32_load((var1 + var5)) ^ i32_load((var4 - 4))) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var7))
                var5 = i32_load((var0 + var5))
                i32_store((var3 + (var6 << 2)), (((((((((i32_load((var1 + var5)) ^ i32_load((var4 - 4))) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var7)) & -16711936) + (i32_load((var0 + var5)) & -16711936)) & -16711936) | (((var4 & 16711935) + (var5 & 16711935)) & 16711935)))
                var6 = (var6 + 1)
                if (1 if (var6 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func1039
# ==========================================================
def func1039(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if var1:
        if (1 if var2 > 0 else 0):
            var4 = i32_load((var3 - 4))
            while True:  # loop $label0
                var5 = (var6 << 2)
                var7 = i32_load((var1 + var5))
                var4 = (((((i32_load((var1 + var5)) ^ var4) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var7))
                var5 = i32_load((var0 + var5))
                var4 = (((((((((i32_load((var1 + var5)) ^ var4) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var7)) & -16711936) + (i32_load((var0 + var5)) & -16711936)) & -16711936) | (((var4 & 16711935) + (var5 & 16711935)) & 16711935))
                i32_store((var3 + (var6 << 2)), (((((((((i32_load((var1 + var5)) ^ var4) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var7)) & -16711936) + (i32_load((var0 + var5)) & -16711936)) & -16711936) | (((var4 & 16711935) + (var5 & 16711935)) & 16711935)))
                var6 = (var6 + 1)
                if (1 if (var6 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')

