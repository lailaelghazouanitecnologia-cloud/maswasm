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
# $func1072
# ==========================================================
def func1072(var0, var1, var2, var3, var4, var5):
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    var13 = 0
    var14 = 0
    if (1 if var4 <= 15 else 0):
        var13 = (i32_load((var1 + (var4 << 2))) + (var2 * 11))
        var2 = i32_load(var0 + 12)
        var8 = i32_load(var0 + 8)
        while True:  # loop $label11
            var10 = i32_load8_u(var13)
            if (1 if var2 >= 0 else 0):
                break
            var9 = i32_load(var0 + 16)
            if (1 if i32_load(var0 + 16) == 0 else 0):
                break
            if (1 if i32_load(var0 + 24) > var9 else 0):
                var6 = i64_load(var9)
                i32_store(var0 + 16, (var9 + 7))
                i64_store(var0, ((i64_load(var0) << 56) | ((((((var6 << 56) | ((var6 & 65280) << 40)) | (((var6 & 16711680) << 24) | ((var6 & 4278190080) << 8))) | ((((var6 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var6 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var6 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                var2 = (var2 + 56)
                break
            func36(var0)
            var2 = i32_load(var0 + 12)
            var9 = (((var8 * var10) & 0xFFFFFFFF) >> 8)
            var6 = i64_load(var0)
            var7 = i64_extend_u(var2)
            var10 = (1 if (((var8 * var10) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0)
            if (1 if (1 if (((var8 * var10) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0) == 0 else 0):
                var6 = (var6 - (i64_extend_u((var9 + 1)) << var7))
                i64_store(var0, (var6 - (i64_extend_u((var9 + 1)) << var7)))
                break
            var8 = (var9 + 1)
            var9 = (clz32((var9 + 1)) ^ 24)
            var2 = ((var8 - var9) - (clz32((var9 + 1)) ^ 24))
            i32_store(var2 + 12, ((var8 - var9) - (clz32((var9 + 1)) ^ 24)))
            var11 = ((var8 << var9) - 1)
            i32_store(var0 + 8, ((var8 << var9) - 1))
            var9 = var4
            var8 = var4
            if var10:
                break
            while True:  # loop $label6
                var8 = i32_load8_u(var13 + 1)
                if (1 if var2 >= 0 else 0):
                    break
                var4 = i32_load(var0 + 16)
                if (1 if i32_load(var0 + 16) == 0 else 0):
                    break
                if (1 if i32_load(var0 + 24) > var4 else 0):
                    var7 = i64_load(var4)
                    i32_store(var0 + 16, (var4 + 7))
                    var6 = ((var6 << 56) | ((((((var7 << 56) | ((var7 & 65280) << 40)) | (((var7 & 16711680) << 24) | ((var7 & 4278190080) << 8))) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var7 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                    i64_store(var0, ((var6 << 56) | ((((((var7 << 56) | ((var7 & 65280) << 40)) | (((var7 & 16711680) << 24) | ((var7 & 4278190080) << 8))) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var7 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                    var2 = (var2 + 56)
                    break
                func36(var0)
                var6 = i64_load(var0)
                var2 = i32_load(var0 + 12)
                var8 = (((var8 * var11) & 0xFFFFFFFF) >> 8)
                var7 = i64_extend_u(var2)
                var12 = i32(((var6 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2)))
                if (1 if (((var8 * var11) & 0xFFFFFFFF) >> 8) < i32(((var6 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0):
                    var6 = (var6 - (i64_extend_u((var8 + 1)) << var7))
                    i64_store(var0, (var6 - (i64_extend_u((var8 + 1)) << var7)))
                    break
                var4 = (var8 + 1)
                var10 = (clz32((var8 + 1)) ^ 24)
                var2 = ((var11 - var8) - (clz32((var8 + 1)) ^ 24))
                i32_store(var2 + 12, ((var11 - var8) - (clz32((var8 + 1)) ^ 24)))
                var11 = ((var4 << var10) - 1)
                i32_store(var0 + 8, ((var4 << var10) - 1))
                var4 = (var9 + 1)
                var10 = i32_load((var1 + ((var9 + 1) << 2)))
                if (1 if var8 >= var12 else 0):
                    var8 = 16
                    var13 = var10
                    var9 = var4
                    if (1 if var4 != 16 else 0):
                        continue
                    break
                break  # end loop
            var12 = i32_load8_u(var13 + 2)
            if (1 if var2 >= 0 else 0):
                break
            var8 = i32_load(var0 + 16)
            if (1 if i32_load(var0 + 16) == 0 else 0):
                break
            if (1 if i32_load(var0 + 24) > var8 else 0):
                var7 = i64_load(var8)
                i32_store(var0 + 16, (var8 + 7))
                var6 = ((var6 << 56) | ((((((var7 << 56) | ((var7 & 65280) << 40)) | (((var7 & 16711680) << 24) | ((var7 & 4278190080) << 8))) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var7 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                i64_store(var0, ((var6 << 56) | ((((((var7 << 56) | ((var7 & 65280) << 40)) | (((var7 & 16711680) << 24) | ((var7 & 4278190080) << 8))) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var7 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                var2 = (var2 + 56)
                break
            func36(var0)
            var6 = i64_load(var0)
            var2 = i32_load(var0 + 12)
            var12 = (((var11 * var12) & 0xFFFFFFFF) >> 8)
            var7 = i64_extend_u(var2)
            var14 = i32(((var6 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2)))
            if (1 if (((var11 * var12) & 0xFFFFFFFF) >> 8) < i32(((var6 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0):
                i64_store(var0, (var6 - (i64_extend_u((var12 + 1)) << var7)))
                break
            var11 = (var12 + 1)
            var2 = (clz32((var12 + 1)) ^ 24)
            var8 = ((var11 - var12) - (clz32((var12 + 1)) ^ 24))
            i32_store(var2 + 12, ((var11 - var12) - (clz32((var12 + 1)) ^ 24)))
            i32_store(var0 + 8, ((var11 << var2) - 1))
            if (1 if var12 >= var14 else 0):
                var11 = 1
                break
            var11 = func463(var0, var13)
            var8 = i32_load(var0 + 12)
            var13 = (var10 + 22)
            if (1 if var8 >= 0 else 0):
                break
            var2 = i32_load(var0 + 16)
            if (1 if i32_load(var0 + 16) == 0 else 0):
                break
            if (1 if i32_load(var0 + 24) > var2 else 0):
                var6 = i64_load(var2)
                i32_store(var0 + 16, (var2 + 7))
                i64_store(var0, ((i64_load(var0) << 56) | ((((((var6 << 56) | ((var6 & 65280) << 40)) | (((var6 & 16711680) << 24) | ((var6 & 4278190080) << 8))) | ((((var6 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var6 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var6 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                var8 = (var8 + 56)
                break
            func36(var0)
            var8 = i32_load(var0 + 12)
            var2 = (var8 - 1)
            i32_store(var0 + 12, (var8 - 1))
            var12 = i32_load(var0 + 8)
            var14 = ((i32_load(var0 + 8) & 0xFFFFFFFF) >> 1)
            var6 = i64_load(var0)
            var7 = i64_extend_u(var8)
            var10 = ((((i32_load(var0 + 8) & 0xFFFFFFFF) >> 1) - i32(((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var8)))) >> 31)
            var8 = ((((((i32_load(var0 + 8) & 0xFFFFFFFF) >> 1) - i32(((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var8)))) >> 31) + var12) | 1)
            i32_store(var0 + 8, ((((((i32_load(var0 + 8) & 0xFFFFFFFF) >> 1) - i32(((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var8)))) >> 31) + var12) | 1))
            i64_store(var0, (var6 - (i64_extend_u((var10 & (var14 + 1))) << var7)))
            i32_store16((var5 + (i32_load8_u((var9 + 13968)) << 1)), (i32_load((var3 + ((1 if var9 > 0 else 0) << 2))) * ((var10 ^ var11) - var10)))
            if (1 if var9 < 15 else 0):
                continue
            break  # end loop
    var8 = 16
    return var8
    a_c()
    raise RuntimeError('unreachable')
    return 3339

