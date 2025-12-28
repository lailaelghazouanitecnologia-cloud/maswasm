"""
Auto-generated from WAT. Contains 1 functions.
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
# $func1012
# ==========================================================
def func1012(var0, var1, var2, var3, var4, var5, var6, var7, var8):
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
        var10 = (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)
        var12 = (i32_load8_u(var4) | (i32_load8_u(var5) << 16))
        var9 = (i32_load8_u(var2) | (i32_load8_u(var3) << 16))
        var11 = (((i32_load8_u(var4) | (i32_load8_u(var5) << 16)) + ((i32_load8_u(var2) | (i32_load8_u(var3) << 16)) * 3)) + 131074)
        var15 = (((((i32_load8_u(var4) | (i32_load8_u(var5) << 16)) + ((i32_load8_u(var2) | (i32_load8_u(var3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18)
        var17 = ((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((i32_load8_u(var4) | (i32_load8_u(var5) << 16)) + ((i32_load8_u(var2) | (i32_load8_u(var3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
        var13 = (((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((i32_load8_u(var4) | (i32_load8_u(var5) << 16)) + ((i32_load8_u(var2) | (i32_load8_u(var3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        i32_store8(var6, ((((((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((i32_load8_u(var4) | (i32_load8_u(var5) << 16)) + ((i32_load8_u(var2) | (i32_load8_u(var3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var13 < 16384 else 0) else (255 if (1 if var17 >= 14234 else 0) else 0)))
        var11 = (((var11 & 0xFFFFFFFF) >> 2) & 255)
        var17 = (var10 + ((((((var11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
        var13 = ((var10 + ((((((var11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var6 + 2, (((((var10 + ((((((var11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var13 < 16384 else 0) else (255 if (1 if var17 >= 17685 else 0) else 0)))
        var10 = (var10 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8)))
        var11 = ((var10 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        i32_store8(var6 + 1, (((((var10 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var11 < 16384 else 0) else (255 if (1 if var10 >= -8708 else 0) else 0)))
        if var1:
            var10 = (((i32_load8_u(var1) * 19077) & 0xFFFFFFFF) >> 8)
            var11 = ((var9 + (var12 * 3)) + 131074)
            var15 = ((((var9 + (var12 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
            var17 = ((((i32_load8_u(var1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var9 + (var12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            var13 = (((((i32_load8_u(var1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var9 + (var12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            i32_store8(var7, ((((((((i32_load8_u(var1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var9 + (var12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var13 < 16384 else 0) else (255 if (1 if var17 >= 14234 else 0) else 0)))
            var11 = (((var11 & 0xFFFFFFFF) >> 2) & 255)
            var17 = (var10 + ((((((var11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            var13 = ((var10 + ((((((var11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8(var7 + 2, (((((var10 + ((((((var11 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var13 < 16384 else 0) else (255 if (1 if var17 >= 17685 else 0) else 0)))
            var10 = (var10 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8)))
            var11 = ((var10 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var7 + 1, (((((var10 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var11 < 16384 else 0) else (255 if (1 if var10 >= -8708 else 0) else 0)))
        var17 = (var8 - 1)
        if (1 if var8 < 3 else 0):
            var10 = var12
            var11 = var9
            break
        var10 = (var17 >> 1)
        var26 = (1 if (1 if var10 <= 1 else 0) else (var17 >> 1))
        var15 = 1
        while True:  # loop $label1
            var13 = (var15 << 1)
            var18 = ((var15 << 1) - 1)
            var20 = (((var15 << 1) - 1) * 3)
            var14 = (var6 + (((var15 << 1) - 1) * 3))
            var16 = (((i32_load8_u((var0 + var18)) * 19077) & 0xFFFFFFFF) >> 8)
            var10 = (i32_load8_u((var4 + var15)) | (i32_load8_u((var5 + var15)) << 16))
            var11 = (i32_load8_u((var2 + var15)) | (i32_load8_u((var3 + var15)) << 16))
            var24 = ((i32_load8_u((var2 + var15)) | (i32_load8_u((var3 + var15)) << 16)) + var12)
            var25 = (((i32_load8_u((var4 + var15)) | (i32_load8_u((var5 + var15)) << 16)) + (((i32_load8_u((var2 + var15)) | (i32_load8_u((var3 + var15)) << 16)) + var12) + var9)) + 524296)
            var24 = ((((((i32_load8_u((var4 + var15)) | (i32_load8_u((var5 + var15)) << 16)) + (((i32_load8_u((var2 + var15)) | (i32_load8_u((var3 + var15)) << 16)) + var12) + var9)) + 524296) + (var24 << 1)) & 0xFFFFFFFF) >> 3)
            var21 = (((((((i32_load8_u((var4 + var15)) | (i32_load8_u((var5 + var15)) << 16)) + (((i32_load8_u((var2 + var15)) | (i32_load8_u((var3 + var15)) << 16)) + var12) + var9)) + 524296) + (var24 << 1)) & 0xFFFFFFFF) >> 3) + var9)
            var22 = (((((((((i32_load8_u((var4 + var15)) | (i32_load8_u((var5 + var15)) << 16)) + (((i32_load8_u((var2 + var15)) | (i32_load8_u((var3 + var15)) << 16)) + var12) + var9)) + 524296) + (var24 << 1)) & 0xFFFFFFFF) >> 3) + var9) & 0xFFFFFFFF) >> 17)
            var19 = ((((i32_load8_u((var0 + var18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((((i32_load8_u((var4 + var15)) | (i32_load8_u((var5 + var15)) << 16)) + (((i32_load8_u((var2 + var15)) | (i32_load8_u((var3 + var15)) << 16)) + var12) + var9)) + 524296) + (var24 << 1)) & 0xFFFFFFFF) >> 3) + var9) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
            var23 = (((((i32_load8_u((var0 + var18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((((i32_load8_u((var4 + var15)) | (i32_load8_u((var5 + var15)) << 16)) + (((i32_load8_u((var2 + var15)) | (i32_load8_u((var3 + var15)) << 16)) + var12) + var9)) + 524296) + (var24 << 1)) & 0xFFFFFFFF) >> 3) + var9) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            i32_store8((var6 + (((var15 << 1) - 1) * 3)), ((((((((i32_load8_u((var0 + var18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((((i32_load8_u((var4 + var15)) | (i32_load8_u((var5 + var15)) << 16)) + (((i32_load8_u((var2 + var15)) | (i32_load8_u((var3 + var15)) << 16)) + var12) + var9)) + 524296) + (var24 << 1)) & 0xFFFFFFFF) >> 3) + var9) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var23 < 16384 else 0) else (255 if (1 if var19 >= 14234 else 0) else 0)))
            var21 = (((var21 & 0xFFFFFFFF) >> 1) & 255)
            var19 = (((((((var21 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8) + var16)
            var23 = ((((((((var21 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8) + var16) - 17685)
            i32_store8(var14 + 2, (((((((((((var21 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8) + var16) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var23 < 16384 else 0) else (255 if (1 if var19 >= 17685 else 0) else 0)))
            var14 = (var16 - ((((var22 * 13320) & 0xFFFFFFFF) >> 8) + (((var21 * 6419) & 0xFFFFFFFF) >> 8)))
            var16 = ((var16 - ((((var22 * 13320) & 0xFFFFFFFF) >> 8) + (((var21 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var14 + 1, (((((var16 - ((((var22 * 13320) & 0xFFFFFFFF) >> 8) + (((var21 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var16 < 16384 else 0) else (255 if (1 if var14 >= -8708 else 0) else 0)))
            var21 = (var15 * 6)
            var14 = (var6 + (var15 * 6))
            var16 = (((i32_load8_u((var0 + var13)) * 19077) & 0xFFFFFFFF) >> 8)
            var25 = (((var25 + ((var9 + var10) << 1)) & 0xFFFFFFFF) >> 3)
            var9 = ((((var25 + ((var9 + var10) << 1)) & 0xFFFFFFFF) >> 3) + var11)
            var22 = (((((((var25 + ((var9 + var10) << 1)) & 0xFFFFFFFF) >> 3) + var11) & 0xFFFFFFFF) >> 1) & 255)
            var19 = ((((i32_load8_u((var0 + var13)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((var25 + ((var9 + var10) << 1)) & 0xFFFFFFFF) >> 3) + var11) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
            var23 = (((((i32_load8_u((var0 + var13)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((var25 + ((var9 + var10) << 1)) & 0xFFFFFFFF) >> 3) + var11) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8((var6 + (var15 * 6)) + 2, ((((((((i32_load8_u((var0 + var13)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((((var25 + ((var9 + var10) << 1)) & 0xFFFFFFFF) >> 3) + var11) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var23 < 16384 else 0) else (255 if (1 if var19 >= 17685 else 0) else 0)))
            var9 = ((var9 & 0xFFFFFFFF) >> 17)
            var22 = (var16 - ((((((var9 & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + (((var22 * 6419) & 0xFFFFFFFF) >> 8)))
            var19 = ((var16 - ((((((var9 & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + (((var22 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var14 + 1, (((((var16 - ((((((var9 & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + (((var22 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var19 < 16384 else 0) else (255 if (1 if var22 >= -8708 else 0) else 0)))
            var9 = ((((var9 * 26149) & 0xFFFFFFFF) >> 8) + var16)
            var14 = (((((var9 * 26149) & 0xFFFFFFFF) >> 8) + var16) - 14234)
            i32_store8(var14, ((((((((var9 * 26149) & 0xFFFFFFFF) >> 8) + var16) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var14 < 16384 else 0) else (255 if (1 if var9 >= 14234 else 0) else 0)))
            if var1:
                var9 = (var7 + var20)
                var18 = (((i32_load8_u((var1 + var18)) * 19077) & 0xFFFFFFFF) >> 8)
                var12 = (var12 + var25)
                var14 = (((var12 + var25) & 0xFFFFFFFF) >> 17)
                var16 = ((((i32_load8_u((var1 + var18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((var12 + var25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                var20 = (((((i32_load8_u((var1 + var18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((var12 + var25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                i32_store8((var7 + var20), ((((((((i32_load8_u((var1 + var18)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((var12 + var25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var20 < 16384 else 0) else (255 if (1 if var16 >= 14234 else 0) else 0)))
                var12 = (((var12 & 0xFFFFFFFF) >> 1) & 255)
                var16 = (var18 + ((((((var12 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                var20 = ((var18 + ((((((var12 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                i32_store8(var9 + 2, (((((var18 + ((((((var12 & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var20 < 16384 else 0) else (255 if (1 if var16 >= 17685 else 0) else 0)))
                var9 = (var18 - ((((var12 * 6419) & 0xFFFFFFFF) >> 8) + (((var14 * 13320) & 0xFFFFFFFF) >> 8)))
                var12 = ((var18 - ((((var12 * 6419) & 0xFFFFFFFF) >> 8) + (((var14 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                i32_store8(var9 + 1, (((((var18 - ((((var12 * 6419) & 0xFFFFFFFF) >> 8) + (((var14 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var12 < 16384 else 0) else (255 if (1 if var9 >= -8708 else 0) else 0)))
                var9 = (var7 + var21)
                var12 = (((i32_load8_u((var1 + var13)) * 19077) & 0xFFFFFFFF) >> 8)
                var13 = (var10 + var24)
                var18 = ((((var10 + var24) & 0xFFFFFFFF) >> 1) & 255)
                var14 = ((((i32_load8_u((var1 + var13)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var10 + var24) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8))
                var16 = (((((i32_load8_u((var1 + var13)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var10 + var24) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                i32_store8((var7 + var21) + 2, ((((((((i32_load8_u((var1 + var13)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var10 + var24) & 0xFFFFFFFF) >> 1) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var16 < 16384 else 0) else (255 if (1 if var14 >= 17685 else 0) else 0)))
                var13 = ((var13 & 0xFFFFFFFF) >> 17)
                var18 = (var12 - ((((var18 * 6419) & 0xFFFFFFFF) >> 8) + (((((var13 & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8)))
                var14 = ((var12 - ((((var18 * 6419) & 0xFFFFFFFF) >> 8) + (((((var13 & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                i32_store8(var9 + 1, (((((var12 - ((((var18 * 6419) & 0xFFFFFFFF) >> 8) + (((((var13 & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var14 < 16384 else 0) else (255 if (1 if var18 >= -8708 else 0) else 0)))
                var9 = (var12 + (((var13 * 26149) & 0xFFFFFFFF) >> 8))
                var12 = ((var12 + (((var13 * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                i32_store8(var9, (((((var12 + (((var13 * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var12 < 16384 else 0) else (255 if (1 if var9 >= 14234 else 0) else 0)))
            var13 = (1 if var15 != var26 else 0)
            var15 = (var15 + 1)
            var9 = var11
            var12 = var10
            if var13:
                continue
            break  # end loop
        if (var8 & 1):
            break
        var3 = (var17 * 3)
        var2 = (var6 + (var17 * 3))
        var0 = (((i32_load8_u((var0 + var17)) * 19077) & 0xFFFFFFFF) >> 8)
        var4 = ((var10 + (var11 * 3)) + 131074)
        var5 = ((((var10 + (var11 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
        var6 = ((((i32_load8_u((var0 + var17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var10 + (var11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
        var8 = (((((i32_load8_u((var0 + var17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var10 + (var11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        i32_store8((var6 + (var17 * 3)), ((((((((i32_load8_u((var0 + var17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var10 + (var11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (255 if (1 if var6 >= 14234 else 0) else 0)))
        var4 = (((var4 & 0xFFFFFFFF) >> 2) & 255)
        var6 = (var0 + ((((((var4 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
        var8 = ((var0 + ((((((var4 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var2 + 2, (((((var0 + ((((((var4 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (255 if (1 if var6 >= 17685 else 0) else 0)))
        var0 = (var0 - ((((var4 * 6419) & 0xFFFFFFFF) >> 8) + (((var5 * 13320) & 0xFFFFFFFF) >> 8)))
        var2 = ((var0 - ((((var4 * 6419) & 0xFFFFFFFF) >> 8) + (((var5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        i32_store8(var2 + 1, (((((var0 - ((((var4 * 6419) & 0xFFFFFFFF) >> 8) + (((var5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var2 < 16384 else 0) else (255 if (1 if var0 >= -8708 else 0) else 0)))
        if (1 if var1 == 0 else 0):
            break
        var0 = (var3 + var7)
        var1 = (((i32_load8_u((var1 + var17)) * 19077) & 0xFFFFFFFF) >> 8)
        var2 = ((var11 + (var10 * 3)) + 131074)
        var3 = ((((var11 + (var10 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
        var4 = ((((i32_load8_u((var1 + var17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var11 + (var10 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
        var5 = (((((i32_load8_u((var1 + var17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var11 + (var10 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        i32_store8((var3 + var7), ((((((((i32_load8_u((var1 + var17)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var11 + (var10 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var5 < 16384 else 0) else (255 if (1 if var4 >= 14234 else 0) else 0)))
        var2 = (((var2 & 0xFFFFFFFF) >> 2) & 255)
        var4 = (var1 + ((((((var2 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8))
        var5 = ((var1 + ((((((var2 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var0 + 2, (((((var1 + ((((((var2 & 0xFFFFFFFF) >> 2) & 255) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var5 < 16384 else 0) else (255 if (1 if var4 >= 17685 else 0) else 0)))
        var0 = (var1 - ((((var2 * 6419) & 0xFFFFFFFF) >> 8) + (((var3 * 13320) & 0xFFFFFFFF) >> 8)))
        var1 = ((var1 - ((((var2 * 6419) & 0xFFFFFFFF) >> 8) + (((var3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        i32_store8(var0 + 1, (((((var1 - ((((var2 * 6419) & 0xFFFFFFFF) >> 8) + (((var3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var1 < 16384 else 0) else (255 if (1 if var0 >= -8708 else 0) else 0)))
        return
    a_c()
    raise RuntimeError('unreachable')

