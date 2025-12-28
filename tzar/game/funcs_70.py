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
# $func1013
# ==========================================================
def func1013(var0, var1, var2, var3, var4, var5, var6, var7, var8):
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
        var11 = (((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8)
        var13 = (i32_load8_u(var4) | (i32_load8_u(var5) << 16))
        var9 = (i32_load8_u(var2) | (i32_load8_u(var3) << 16))
        var12 = (((i32_load8_u(var4) | (i32_load8_u(var5) << 16)) + ((i32_load8_u(var2) | (i32_load8_u(var3) << 16)) * 3)) + 131074)
        var10 = (((((i32_load8_u(var4) | (i32_load8_u(var5) << 16)) + ((i32_load8_u(var2) | (i32_load8_u(var3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18)
        var16 = ((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((i32_load8_u(var4) | (i32_load8_u(var5) << 16)) + ((i32_load8_u(var2) | (i32_load8_u(var3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
        var17 = (((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((i32_load8_u(var4) | (i32_load8_u(var5) << 16)) + ((i32_load8_u(var2) | (i32_load8_u(var3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        var12 = (((var12 & 0xFFFFFFFF) >> 2) & 255)
        var10 = (var11 - (((((((var12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var10 * 13320) & 0xFFFFFFFF) >> 8)))
        var16 = ((var11 - (((((((var12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var10 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        var10 = (((((var11 - (((((((var12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var10 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var16 < 16384 else 0) else (255 if (1 if var10 >= -8708 else 0) else 0))
        i32_store8(var6, ((((((((((i32_load8_u(var0) * 19077) & 0xFFFFFFFF) >> 8) + ((((((((i32_load8_u(var4) | (i32_load8_u(var5) << 16)) + ((i32_load8_u(var2) | (i32_load8_u(var3) << 16)) * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var17 < 16384 else 0) else (248 if (1 if var16 >= 14234 else 0) else 0)) & 248) | (((((((var11 - (((((((var12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var10 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var16 < 16384 else 0) else (255 if (1 if var10 >= -8708 else 0) else 0)) & 0xFFFFFFFF) >> 5)))
        var11 = (var11 + (((var12 * 33050) & 0xFFFFFFFF) >> 8))
        var12 = ((var11 + (((var12 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var6 + 1, (((var10 << 3) & 224) | (((((var11 + (((var12 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 9) if (1 if var12 < 16384 else 0) else (31 if (1 if var11 >= 17685 else 0) else 0))))
        if var1:
            var11 = (((i32_load8_u(var1) * 19077) & 0xFFFFFFFF) >> 8)
            var12 = ((var9 + (var13 * 3)) + 131074)
            var10 = ((((var9 + (var13 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
            var16 = ((((i32_load8_u(var1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var9 + (var13 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
            var17 = (((((i32_load8_u(var1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var9 + (var13 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            var12 = (((var12 & 0xFFFFFFFF) >> 2) & 255)
            var10 = (var11 - (((((((var12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var10 * 13320) & 0xFFFFFFFF) >> 8)))
            var16 = ((var11 - (((((((var12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var10 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            var10 = (((((var11 - (((((((var12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var10 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var16 < 16384 else 0) else (255 if (1 if var10 >= -8708 else 0) else 0))
            i32_store8(var7, ((((((((((i32_load8_u(var1) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var9 + (var13 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var17 < 16384 else 0) else (248 if (1 if var16 >= 14234 else 0) else 0)) & 248) | (((((((var11 - (((((((var12 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var10 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var16 < 16384 else 0) else (255 if (1 if var10 >= -8708 else 0) else 0)) & 0xFFFFFFFF) >> 5)))
            var11 = (var11 + (((var12 * 33050) & 0xFFFFFFFF) >> 8))
            var12 = ((var11 + (((var12 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8(var7 + 1, (((var10 << 3) & 224) | (((((var11 + (((var12 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 9) if (1 if var12 < 16384 else 0) else (31 if (1 if var11 >= 17685 else 0) else 0))))
        var16 = (var8 - 1)
        if (1 if var8 < 3 else 0):
            var11 = var13
            var12 = var9
            break
        var11 = (var16 >> 1)
        var26 = (1 if (1 if var11 <= 1 else 0) else (var16 >> 1))
        var10 = 1
        while True:  # loop $label1
            var17 = (var10 << 1)
            var15 = ((var10 << 1) - 1)
            var18 = (((var10 << 1) - 1) << 1)
            var22 = (var6 + (((var10 << 1) - 1) << 1))
            var14 = (((i32_load8_u((var0 + var15)) * 19077) & 0xFFFFFFFF) >> 8)
            var11 = (i32_load8_u((var4 + var10)) | (i32_load8_u((var5 + var10)) << 16))
            var12 = (i32_load8_u((var2 + var10)) | (i32_load8_u((var3 + var10)) << 16))
            var25 = ((i32_load8_u((var2 + var10)) | (i32_load8_u((var3 + var10)) << 16)) + var13)
            var23 = (((i32_load8_u((var4 + var10)) | (i32_load8_u((var5 + var10)) << 16)) + (((i32_load8_u((var2 + var10)) | (i32_load8_u((var3 + var10)) << 16)) + var13) + var9)) + 524296)
            var25 = ((((((i32_load8_u((var4 + var10)) | (i32_load8_u((var5 + var10)) << 16)) + (((i32_load8_u((var2 + var10)) | (i32_load8_u((var3 + var10)) << 16)) + var13) + var9)) + 524296) + (var25 << 1)) & 0xFFFFFFFF) >> 3)
            var24 = (((((((i32_load8_u((var4 + var10)) | (i32_load8_u((var5 + var10)) << 16)) + (((i32_load8_u((var2 + var10)) | (i32_load8_u((var3 + var10)) << 16)) + var13) + var9)) + 524296) + (var25 << 1)) & 0xFFFFFFFF) >> 3) + var9)
            var19 = (((((((((i32_load8_u((var4 + var10)) | (i32_load8_u((var5 + var10)) << 16)) + (((i32_load8_u((var2 + var10)) | (i32_load8_u((var3 + var10)) << 16)) + var13) + var9)) + 524296) + (var25 << 1)) & 0xFFFFFFFF) >> 3) + var9) & 0xFFFFFFFF) >> 17)
            var24 = (((var24 & 0xFFFFFFFF) >> 1) & 255)
            var20 = ((((i32_load8_u((var0 + var15)) * 19077) & 0xFFFFFFFF) >> 8) - (((((((((((((i32_load8_u((var4 + var10)) | (i32_load8_u((var5 + var10)) << 16)) + (((i32_load8_u((var2 + var10)) | (i32_load8_u((var3 + var10)) << 16)) + var13) + var9)) + 524296) + (var25 << 1)) & 0xFFFFFFFF) >> 3) + var9) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((var24 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8)))
            var21 = (((((i32_load8_u((var0 + var15)) * 19077) & 0xFFFFFFFF) >> 8) - (((((((((((((i32_load8_u((var4 + var10)) | (i32_load8_u((var5 + var10)) << 16)) + (((i32_load8_u((var2 + var10)) | (i32_load8_u((var3 + var10)) << 16)) + var13) + var9)) + 524296) + (var25 << 1)) & 0xFFFFFFFF) >> 3) + var9) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((var24 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            var20 = ((((((((i32_load8_u((var0 + var15)) * 19077) & 0xFFFFFFFF) >> 8) - (((((((((((((i32_load8_u((var4 + var10)) | (i32_load8_u((var5 + var10)) << 16)) + (((i32_load8_u((var2 + var10)) | (i32_load8_u((var3 + var10)) << 16)) + var13) + var9)) + 524296) + (var25 << 1)) & 0xFFFFFFFF) >> 3) + var9) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((var24 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var21 < 16384 else 0) else (255 if (1 if var20 >= -8708 else 0) else 0))
            var19 = ((((var19 * 26149) & 0xFFFFFFFF) >> 8) + var14)
            var21 = (((((var19 * 26149) & 0xFFFFFFFF) >> 8) + var14) - 14234)
            i32_store8((var6 + (((var10 << 1) - 1) << 1)), (((((((((((i32_load8_u((var0 + var15)) * 19077) & 0xFFFFFFFF) >> 8) - (((((((((((((i32_load8_u((var4 + var10)) | (i32_load8_u((var5 + var10)) << 16)) + (((i32_load8_u((var2 + var10)) | (i32_load8_u((var3 + var10)) << 16)) + var13) + var9)) + 524296) + (var25 << 1)) & 0xFFFFFFFF) >> 3) + var9) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((var24 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var21 < 16384 else 0) else (255 if (1 if var20 >= -8708 else 0) else 0)) & 0xFFFFFFFF) >> 5) | (((((((((var19 * 26149) & 0xFFFFFFFF) >> 8) + var14) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var21 < 16384 else 0) else (248 if (1 if var19 >= 14234 else 0) else 0)) & 248)))
            var14 = ((((var24 * 33050) & 0xFFFFFFFF) >> 8) + var14)
            var22 = (((((var24 * 33050) & 0xFFFFFFFF) >> 8) + var14) - 17685)
            i32_store8(var22 + 1, (((var20 << 3) & 224) | ((((((((var24 * 33050) & 0xFFFFFFFF) >> 8) + var14) - 17685) & 0xFFFFFFFF) >> 9) if (1 if var22 < 16384 else 0) else (31 if (1 if var14 >= 17685 else 0) else 0))))
            var22 = (var10 << 2)
            var24 = (var6 + (var10 << 2))
            var14 = (((i32_load8_u((var0 + var17)) * 19077) & 0xFFFFFFFF) >> 8)
            var23 = (((var23 + ((var9 + var11) << 1)) & 0xFFFFFFFF) >> 3)
            var9 = ((((var23 + ((var9 + var11) << 1)) & 0xFFFFFFFF) >> 3) + var12)
            var19 = ((((((var23 + ((var9 + var11) << 1)) & 0xFFFFFFFF) >> 3) + var12) & 0xFFFFFFFF) >> 17)
            var9 = (((var9 & 0xFFFFFFFF) >> 1) & 255)
            var20 = ((((i32_load8_u((var0 + var17)) * 19077) & 0xFFFFFFFF) >> 8) - ((((((((((var23 + ((var9 + var11) << 1)) & 0xFFFFFFFF) >> 3) + var12) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((var9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8)))
            var21 = (((((i32_load8_u((var0 + var17)) * 19077) & 0xFFFFFFFF) >> 8) - ((((((((((var23 + ((var9 + var11) << 1)) & 0xFFFFFFFF) >> 3) + var12) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((var9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            var20 = ((((((((i32_load8_u((var0 + var17)) * 19077) & 0xFFFFFFFF) >> 8) - ((((((((((var23 + ((var9 + var11) << 1)) & 0xFFFFFFFF) >> 3) + var12) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((var9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var21 < 16384 else 0) else (255 if (1 if var20 >= -8708 else 0) else 0))
            var19 = ((((var19 * 26149) & 0xFFFFFFFF) >> 8) + var14)
            var21 = (((((var19 * 26149) & 0xFFFFFFFF) >> 8) + var14) - 14234)
            i32_store8((var6 + (var10 << 2)), (((((((((((i32_load8_u((var0 + var17)) * 19077) & 0xFFFFFFFF) >> 8) - ((((((((((var23 + ((var9 + var11) << 1)) & 0xFFFFFFFF) >> 3) + var12) & 0xFFFFFFFF) >> 17) * 13320) & 0xFFFFFFFF) >> 8) + ((((((var9 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var21 < 16384 else 0) else (255 if (1 if var20 >= -8708 else 0) else 0)) & 0xFFFFFFFF) >> 5) | (((((((((var19 * 26149) & 0xFFFFFFFF) >> 8) + var14) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var21 < 16384 else 0) else (248 if (1 if var19 >= 14234 else 0) else 0)) & 248)))
            var9 = ((((var9 * 33050) & 0xFFFFFFFF) >> 8) + var14)
            var14 = (((((var9 * 33050) & 0xFFFFFFFF) >> 8) + var14) - 17685)
            i32_store8(var24 + 1, (((var20 << 3) & 224) | ((((((((var9 * 33050) & 0xFFFFFFFF) >> 8) + var14) - 17685) & 0xFFFFFFFF) >> 9) if (1 if var14 < 16384 else 0) else (31 if (1 if var9 >= 17685 else 0) else 0))))
            if var1:
                var14 = (var7 + var18)
                var9 = (((i32_load8_u((var1 + var15)) * 19077) & 0xFFFFFFFF) >> 8)
                var13 = (var13 + var23)
                var15 = (((var13 + var23) & 0xFFFFFFFF) >> 17)
                var18 = ((((i32_load8_u((var1 + var15)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((var13 + var23) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                var23 = (((((i32_load8_u((var1 + var15)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((var13 + var23) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                var13 = (((var13 & 0xFFFFFFFF) >> 1) & 255)
                var15 = (var9 - (((((((var13 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8)))
                var18 = ((var9 - (((((((var13 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                var15 = (((((var9 - (((((((var13 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var18 < 16384 else 0) else (255 if (1 if var15 >= -8708 else 0) else 0))
                i32_store8((var7 + var18), ((((((((((i32_load8_u((var1 + var15)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((var13 + var23) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var23 < 16384 else 0) else (248 if (1 if var18 >= 14234 else 0) else 0)) & 248) | (((((((var9 - (((((((var13 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var18 < 16384 else 0) else (255 if (1 if var15 >= -8708 else 0) else 0)) & 0xFFFFFFFF) >> 5)))
                var9 = (var9 + (((var13 * 33050) & 0xFFFFFFFF) >> 8))
                var13 = ((var9 + (((var13 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                i32_store8(var14 + 1, (((var15 << 3) & 224) | (((((var9 + (((var13 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 9) if (1 if var13 < 16384 else 0) else (31 if (1 if var9 >= 17685 else 0) else 0))))
                var13 = (var7 + var22)
                var9 = (((i32_load8_u((var1 + var17)) * 19077) & 0xFFFFFFFF) >> 8)
                var17 = (var11 + var25)
                var15 = (((var11 + var25) & 0xFFFFFFFF) >> 17)
                var14 = ((((i32_load8_u((var1 + var17)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((var11 + var25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8))
                var18 = (((((i32_load8_u((var1 + var17)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((var11 + var25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
                var17 = (((var17 & 0xFFFFFFFF) >> 1) & 255)
                var15 = (var9 - (((((((var17 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8)))
                var14 = ((var9 - (((((((var17 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
                var15 = (((((var9 - (((((((var17 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var14 < 16384 else 0) else (255 if (1 if var15 >= -8708 else 0) else 0))
                i32_store8((var7 + var22), ((((((((((i32_load8_u((var1 + var17)) * 19077) & 0xFFFFFFFF) >> 8) + ((((((var11 + var25) & 0xFFFFFFFF) >> 17) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var18 < 16384 else 0) else (248 if (1 if var14 >= 14234 else 0) else 0)) & 248) | (((((((var9 - (((((((var17 & 0xFFFFFFFF) >> 1) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var15 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var14 < 16384 else 0) else (255 if (1 if var15 >= -8708 else 0) else 0)) & 0xFFFFFFFF) >> 5)))
                var9 = (var9 + (((var17 * 33050) & 0xFFFFFFFF) >> 8))
                var13 = ((var9 + (((var17 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
                i32_store8(var13 + 1, (((var15 << 3) & 224) | (((((var9 + (((var17 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 9) if (1 if var13 < 16384 else 0) else (31 if (1 if var9 >= 17685 else 0) else 0))))
            var17 = (1 if var10 != var26 else 0)
            var10 = (var10 + 1)
            var9 = var12
            var13 = var11
            if var17:
                continue
            break  # end loop
        if (var8 & 1):
            break
        var2 = (var16 << 1)
        var3 = (var6 + (var16 << 1))
        var0 = (((i32_load8_u((var0 + var16)) * 19077) & 0xFFFFFFFF) >> 8)
        var4 = ((var11 + (var12 * 3)) + 131074)
        var5 = ((((var11 + (var12 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
        var6 = ((((i32_load8_u((var0 + var16)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var11 + (var12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
        var8 = (((((i32_load8_u((var0 + var16)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var11 + (var12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        var4 = (((var4 & 0xFFFFFFFF) >> 2) & 255)
        var5 = (var0 - (((((((var4 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var5 * 13320) & 0xFFFFFFFF) >> 8)))
        var6 = ((var0 - (((((((var4 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        var5 = (((((var0 - (((((((var4 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var6 < 16384 else 0) else (255 if (1 if var5 >= -8708 else 0) else 0))
        i32_store8((var6 + (var16 << 1)), ((((((((((i32_load8_u((var0 + var16)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var11 + (var12 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var8 < 16384 else 0) else (248 if (1 if var6 >= 14234 else 0) else 0)) & 248) | (((((((var0 - (((((((var4 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var5 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var6 < 16384 else 0) else (255 if (1 if var5 >= -8708 else 0) else 0)) & 0xFFFFFFFF) >> 5)))
        var0 = (var0 + (((var4 * 33050) & 0xFFFFFFFF) >> 8))
        var3 = ((var0 + (((var4 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var3 + 1, (((var5 << 3) & 224) | (((((var0 + (((var4 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 9) if (1 if var3 < 16384 else 0) else (31 if (1 if var0 >= 17685 else 0) else 0))))
        if (1 if var1 == 0 else 0):
            break
        var2 = (var2 + var7)
        var0 = (((i32_load8_u((var1 + var16)) * 19077) & 0xFFFFFFFF) >> 8)
        var1 = ((var12 + (var11 * 3)) + 131074)
        var3 = ((((var12 + (var11 * 3)) + 131074) & 0xFFFFFFFF) >> 18)
        var4 = ((((i32_load8_u((var1 + var16)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var12 + (var11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8))
        var5 = (((((i32_load8_u((var1 + var16)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var12 + (var11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        var1 = (((var1 & 0xFFFFFFFF) >> 2) & 255)
        var3 = (var0 - (((((((var1 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var3 * 13320) & 0xFFFFFFFF) >> 8)))
        var4 = ((var0 - (((((((var1 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        var3 = (((((var0 - (((((((var1 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var4 < 16384 else 0) else (255 if (1 if var3 >= -8708 else 0) else 0))
        i32_store8((var2 + var7), ((((((((((i32_load8_u((var1 + var16)) * 19077) & 0xFFFFFFFF) >> 8) + (((((((var12 + (var11 * 3)) + 131074) & 0xFFFFFFFF) >> 18) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var5 < 16384 else 0) else (248 if (1 if var4 >= 14234 else 0) else 0)) & 248) | (((((((var0 - (((((((var1 & 0xFFFFFFFF) >> 2) & 255) * 6419) & 0xFFFFFFFF) >> 8) + (((var3 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var4 < 16384 else 0) else (255 if (1 if var3 >= -8708 else 0) else 0)) & 0xFFFFFFFF) >> 5)))
        var0 = (var0 + (((var1 * 33050) & 0xFFFFFFFF) >> 8))
        var1 = ((var0 + (((var1 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        i32_store8(var2 + 1, (((var3 << 3) & 224) | (((((var0 + (((var1 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 9) if (1 if var1 < 16384 else 0) else (31 if (1 if var0 >= 17685 else 0) else 0))))
        return
    a_c()
    raise RuntimeError('unreachable')

