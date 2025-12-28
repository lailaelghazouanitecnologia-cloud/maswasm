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
# $func275
# ==========================================================
def func275(var0, var1, var2, var3, var4, var5):
    var6 = 0
    var7 = 0
    var8 = 0
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
    var27 = 0
    var28 = 0
    var29 = 0
    var30 = 0
    var31 = 0
    var32 = 0
    var19 = i32_load(var0 + 120)
    var8 = i32_load(var0 + 56)
    var6 = i32_load(var0 + 112)
    var13 = (var6 // var2)
    var15 = (i32_load(var0 + 112) - ((var6 // var2) * var2))
    var28 = i32_load(var0 + 148)
    var10 = (var2 * var4)
    var9 = (1 if var6 >= (var2 * var4) else 0)
    if (1 if (1 if var6 >= (var2 * var4) else 0) == 0 else 0):
        var7 = i32_load(var0 + 152)
        if i32_load(var0 + 152):
        else:
        var7 = 0
        if (1 if 0 >= i32_load(var0 + 164) else 0):
            break
        var14 = (i32_load(var0 + 168) + (var7 * 548))
    if (1 if var4 > i32_load(var0 + 108) else 0):
        var7 = (var2 * var3)
        if (1 if (var2 * var3) >= var10 else 0):
            var25 = (var0 + 124)
            var16 = (var0 + 24)
            var26 = (var1 + (var10 << 2))
            var3 = (var1 + (var6 << 2))
            if var9:
                break
            var17 = (var25 if (1 if var19 > 0 else 0) else 0)
            var27 = (var13 if var8 else 16777216)
            var20 = (var0 + 120)
            var30 = (var19 + 280)
            var29 = (var1 + (var7 << 2))
            var31 = (var0 + 136)
            var22 = (var0 - -64)
            var10 = var3
            while True:  # loop $label34
                if (1 if var13 >= var27 else 0):
                    if (1 if i32_load(var0 + 56) == 0 else 0):
                        break
                    i64_store(var22, i64_load(var16))
                    i64_store(var22 + 24, i64_load(var16 + 24))
                    i64_store(var22 + 16, i64_load(var16 + 16))
                    i64_store(var22 + 8, i64_load(var16 + 8))
                    i32_store(var0 + 96, ((var3 - var1) >> 2))
                    if (1 if i32_load(var0 + 120) > 0 else 0):
                        func456(var25, var31)
                    var27 = (var13 + 8)
                if (1 if (var15 & var28) == 0 else 0):
                    var6 = i32_load(var0 + 152)
                    if i32_load(var0 + 152):
                    else:
                    var6 = 0
                    if (1 if 0 >= i32_load(var0 + 164) else 0):
                        break
                    var14 = (i32_load(var0 + 168) + (var6 * 548))
                if (1 if var14 == 0 else 0):
                    break
                if i32_load(var14 + 28):
                    var6 = i32_load(var14 + 24)
                    break
                if (1 if i32_load(var0 + 44) >= 32 else 0):
                    func135(var16)
                if i32_load(var14 + 32):
                    var32 = i64_load(var0 + 24)
                    var6 = i32_load(var0 + 44)
                    var8 = (var14 + ((i32(((i64_load(var0 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((i32_load(var0 + 44) & 63)))) & 63) << 3))
                    var9 = i32_load((var14 + ((i32(((i64_load(var0 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((i32_load(var0 + 44) & 63)))) & 63) << 3)) + 36)
                    var7 = (i32_load((var14 + ((i32(((i64_load(var0 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((i32_load(var0 + 44) & 63)))) & 63) << 3)) + 36) + var6)
                    var6 = i32_load(var8 + 40)
                    if (1 if var9 <= 255 else 0):
                        i32_store(var0 + 44, var7)
                        i32_store(var3, var6)
                        var6 = 0
                        break
                    i32_store(var0 + 44, (var7 - 256))
                    if (1 if var6 <= 255 else 0):
                        break
                    var7 = i32_load(var0 + 40)
                    var8 = i32_load(var0 + 36)
                    if (1 if i32_load(var0 + 40) > i32_load(var0 + 36) else 0):
                        break
                    if i32_load(var0 + 48):
                        break
                    if (1 if var7 == var8 else 0):
                        if (1 if i32_load(var0 + 44) > 64 else 0):
                            break
                    if var6:
                        break
                    break
                var32 = i64_load(var0 + 24)
                var7 = i32_load(var0 + 44)
                var6 = (i32_load(var14) + ((i32(((i64_load(var0 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((i32_load(var0 + 44) & 63)))) & 255) << 2))
                var8 = i32_load8_u((i32_load(var14) + ((i32(((i64_load(var0 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((i32_load(var0 + 44) & 63)))) & 255) << 2)))
                if (1 if i32_load8_u((i32_load(var14) + ((i32(((i64_load(var0 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((i32_load(var0 + 44) & 63)))) & 255) << 2))) >= 9 else 0):
                    var7 = (var7 + 8)
                    var6 = ((var6 + (i32_load16_u(var6 + 2) << 2)) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var7 + 8) & 63)))) & ((-1 << (var8 - 8)) ^ -1)) << 2))
                else:
                i32_store(i32_load8_u(((var6 + (i32_load16_u(var6 + 2) << 2)) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var7 + 8) & 63)))) & ((-1 << (var8 - 8)) ^ -1)) << 2))) + 44, ((var8 & 255) + var7))
                var8 = i32_load(var0 + 36)
                var7 = i32_load(var0 + 40)
                var6 = i32_load16_u(var6 + 2)
                if (1 if var7 > var8 else 0):
                    break
                if i32_load(var0 + 48):
                    break
                if (1 if var7 == var8 else 0):
                    if (1 if i32_load(var0 + 44) > 64 else 0):
                        break
                if (1 if var6 <= 255 else 0):
                    if i32_load(var14 + 20):
                        var6 = (i32_load(var14 + 24) | (var6 << 8))
                        break
                    var7 = i32_load(var0 + 44)
                    var8 = (i32_load(var14 + 4) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((i32_load(var0 + 44) & 63)))) & 255) << 2))
                    var9 = i32_load8_u((i32_load(var14 + 4) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((i32_load(var0 + 44) & 63)))) & 255) << 2)))
                    if (1 if i32_load8_u((i32_load(var14 + 4) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((i32_load(var0 + 44) & 63)))) & 255) << 2))) >= 9 else 0):
                        var7 = (var7 + 8)
                        var8 = ((var8 + (i32_load16_u(var8 + 2) << 2)) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var7 + 8) & 63)))) & ((-1 << (var9 - 8)) ^ -1)) << 2))
                    else:
                    var7 = ((var9 & 255) + var7)
                    i32_store(i32_load8_u(((var8 + (i32_load16_u(var8 + 2) << 2)) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var7 + 8) & 63)))) & ((-1 << (var9 - 8)) ^ -1)) << 2))) + 44, ((var9 & 255) + var7))
                    var11 = i32_load16_u(var8 + 2)
                    if (1 if var7 >= 32 else 0):
                        func135(var16)
                        var32 = i64_load(var0 + 24)
                        var7 = i32_load(var0 + 44)
                    var8 = (i32_load(var14 + 8) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((var7 & 63)))) & 255) << 2))
                    var12 = i32_load8_u((i32_load(var14 + 8) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((var7 & 63)))) & 255) << 2)))
                    if (1 if i32_load8_u((i32_load(var14 + 8) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((var7 & 63)))) & 255) << 2))) >= 9 else 0):
                        var7 = (var7 + 8)
                        var8 = ((var8 + (i32_load16_u(var8 + 2) << 2)) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var7 + 8) & 63)))) & ((-1 << (var12 - 8)) ^ -1)) << 2))
                        var12 = i32_load8_u(((var8 + (i32_load16_u(var8 + 2) << 2)) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var7 + 8) & 63)))) & ((-1 << (var12 - 8)) ^ -1)) << 2)))
                    var18 = i32_load16_u(var8 + 2)
                    var8 = (var7 + (var12 & 255))
                    var7 = (i32_load(var14 + 12) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var7 + (var12 & 255)) & 63)))) & 255) << 2))
                    var9 = i32_load8_u((i32_load(var14 + 12) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var7 + (var12 & 255)) & 63)))) & 255) << 2)))
                    if (1 if i32_load8_u((i32_load(var14 + 12) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var7 + (var12 & 255)) & 63)))) & 255) << 2))) >= 9 else 0):
                        var8 = (var8 + 8)
                        var7 = ((var7 + (i32_load16_u(var7 + 2) << 2)) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var8 + 8) & 63)))) & ((-1 << (var9 - 8)) ^ -1)) << 2))
                    else:
                    var8 = ((var9 & 255) + var8)
                    i32_store(i32_load8_u(((var7 + (i32_load16_u(var7 + 2) << 2)) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var8 + 8) & 63)))) & ((-1 << (var9 - 8)) ^ -1)) << 2))) + 44, ((var9 & 255) + var8))
                    var9 = i32_load(var0 + 40)
                    var12 = i32_load(var0 + 36)
                    if (1 if i32_load(var0 + 40) > i32_load(var0 + 36) else 0):
                        break
                    if i32_load(var0 + 48):
                        break
                    var7 = i32_load16_u(var7 + 2)
                    if ((1 if var9 == var12 else 0) & (1 if var8 > 64 else 0)):
                        break
                    var6 = ((((var11 << 16) | (var6 << 8)) | var18) | (var7 << 24))
                    break
                if (1 if var6 <= 279 else 0):
                    var12 = (var6 - 256)
                    if (1 if (var6 - 256) >= 4 else 0):
                        var7 = (((var6 - 258) & 0xFFFFFFFF) >> 1)
                        var12 = (func39(var16, (((var6 - 258) & 0xFFFFFFFF) >> 1)) + (((var6 & 1) | 2) << var7))
                        var32 = i64_load(var0 + 24)
                    var7 = i32_load(var0 + 44)
                    var6 = (i32_load(var14 + 16) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((i32_load(var0 + 44) & 63)))) & 255) << 2))
                    var8 = i32_load8_u((i32_load(var14 + 16) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((i32_load(var0 + 44) & 63)))) & 255) << 2)))
                    if (1 if i32_load8_u((i32_load(var14 + 16) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((i32_load(var0 + 44) & 63)))) & 255) << 2))) >= 9 else 0):
                        var7 = (var7 + 8)
                        var6 = ((var6 + (i32_load16_u(var6 + 2) << 2)) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var7 + 8) & 63)))) & ((-1 << (var8 - 8)) ^ -1)) << 2))
                    else:
                    var7 = ((var8 & 255) + var7)
                    i32_store(i32_load8_u(((var6 + (i32_load16_u(var6 + 2) << 2)) + ((i32(((var32 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var7 + 8) & 63)))) & ((-1 << (var8 - 8)) ^ -1)) << 2))) + 44, ((var8 & 255) + var7))
                    var6 = i32_load16_u(var6 + 2)
                    if (1 if var7 >= 32 else 0):
                        func135(var16)
                    if (1 if var6 >= 4 else 0):
                        var7 = (((var6 - 2) & 0xFFFFFFFF) >> 1)
                        var6 = (func39(var16, (((var6 - 2) & 0xFFFFFFFF) >> 1)) + (((var6 & 1) | 2) << var7))
                    if (1 if (var6 + 1) >= 121 else 0):
                        break
                    var6 = i32_load8_u((var6 + 13840))
                    var6 = (((((i32_load8_u((var6 + 13840)) & 0xFFFFFFFF) >> 4) * var2) - (var6 & 15)) + 8)
                    var9 = (1 if (1 if var6 <= 1 else 0) else (((((i32_load8_u((var6 + 13840)) & 0xFFFFFFFF) >> 4) * var2) - (var6 & 15)) + 8))
                    var6 = i32_load(var0 + 40)
                    var7 = i32_load(var0 + 36)
                    if (1 if i32_load(var0 + 40) > i32_load(var0 + 36) else 0):
                        break
                    if i32_load(var0 + 48):
                        break
                    if (1 if var6 == var7 else 0):
                        if (1 if i32_load(var0 + 44) > 64 else 0):
                            break
                    if (1 if ((var3 - var1) >> 2) < var9 else 0):
                        break
                    var8 = (var12 + 1)
                    if (1 if (var12 + 1) > ((var29 - var3) >> 2) else 0):
                        break
                    var7 = var8
                    var18 = 0
                    var23 = 0
                    var6 = var3
                    var12 = (var3 - (var9 << 2))
                    if (var6 & 3):
                        break
                    if (1 if var9 > 2 else 0):
                        break
                    if (1 if var7 < 4 else 0):
                        break
                    if (1 if var9 == 1 else 0):
                        var9 = i32_load(var12)
                        var32 = i64_extend_u(i32_load(var12))
                        var32 = ((i64_extend_u(i32_load(var12)) << 32) | var32)
                        break
                    var32 = i64_load(var12)
                    var9 = i32(i64_load(var12))
                    if (var6 & 4):
                        i32_store(var6, var9)
                        var7 = (var7 - 1)
                        var32 = rotl64(var32, 32)
                        var12 = (var12 + 4)
                        var6 = (var6 + 4)
                    if (var6 & 7):
                        break
                    var11 = ((var7 & 0xFFFFFFFF) >> 1)
                    var24 = (((var7 & 0xFFFFFFFF) >> 1) & 7)
                    var9 = 0
                    if (1 if (var11 - 1) >= 7 else 0):
                        var21 = (var11 & 2147483640)
                        while True:  # loop $label15
                            var11 = (var9 << 3)
                            i64_store((var6 + (var9 << 3)), var32)
                            i64_store((var6 + (var11 | 8)), var32)
                            i64_store((var6 + (var11 | 16)), var32)
                            i64_store((var6 + (var11 | 24)), var32)
                            i64_store((var6 + (var11 | 32)), var32)
                            i64_store((var6 + (var11 | 40)), var32)
                            i64_store((var6 + (var11 | 48)), var32)
                            i64_store((var6 + (var11 | 56)), var32)
                            var9 = (var9 + 8)
                            var23 = (var23 + 8)
                            if (1 if (var23 + 8) != var21 else 0):
                                continue
                            break  # end loop
                    if var24:
                        while True:  # loop $label16
                            i64_store((var6 + (var9 << 3)), var32)
                            var9 = (var9 + 1)
                            var18 = (var18 + 1)
                            if (1 if (var18 + 1) != var24 else 0):
                                continue
                            break  # end loop
                    if (1 if (var7 & 1) == 0 else 0):
                        break
                    var7 = ((var7 << 2) & -8)
                    i32_store((var6 + ((var7 << 2) & -8)), i32_load((var7 + var12)))
                    break
                    if (1 if var7 <= var9 else 0):
                        break
                    if (1 if var7 <= 0 else 0):
                        break
                    var9 = 0
                    if (1 if var7 >= 4 else 0):
                        var24 = (var7 & -4)
                        while True:  # loop $label19
                            var11 = (var9 << 2)
                            i32_store((var6 + (var9 << 2)), i32_load((var11 + var12)))
                            var21 = (var11 | 4)
                            i32_store((var6 + (var11 | 4)), i32_load((var12 + var21)))
                            var21 = (var11 | 8)
                            i32_store((var6 + (var11 | 8)), i32_load((var12 + var21)))
                            var11 = (var11 | 12)
                            i32_store((var6 + (var11 | 12)), i32_load((var11 + var12)))
                            var9 = (var9 + 4)
                            var23 = (var23 + 4)
                            if (1 if (var23 + 4) != var24 else 0):
                                continue
                            break  # end loop
                    var7 = (var7 & 3)
                    if (1 if (var7 & 3) == 0 else 0):
                        break
                    while True:  # loop $label20
                        var11 = (var9 << 2)
                        i32_store((var6 + (var9 << 2)), i32_load((var11 + var12)))
                        var9 = (var9 + 1)
                        var18 = (var18 + 1)
                        if (1 if (var18 + 1) != var7 else 0):
                            continue
                        break  # end loop
                    break
                    a_c()
                    raise RuntimeError('unreachable')
                    # Unknown: memory.copy []
                    var3 = (var3 + (var8 << 2))
                    var15 = (var8 + var15)
                    if (1 if (var8 + var15) < var2 else 0):
                        break
                    if (1 if var5 == 0 else 0):
                        while True:  # loop $label22
                            var13 = (var13 + 1)
                            var15 = (var15 - var2)
                            if (1 if (var15 - var2) >= var2 else 0):
                                continue
                            break
                            break  # end loop
                        raise RuntimeError('unreachable')
                    while True:  # loop $label24
                        var15 = (var15 - var2)
                        var6 = var13
                        var13 = (var13 + 1)
                        if (1 if var4 <= var6 else 0):
                            break
                        if (var13 & 15):
                            break
                        # call_indirect via table[var5]
                        if (1 if var2 <= var15 else 0):
                            continue
                        break  # end loop
                    if (1 if var3 > var29 else 0):
                        break
                    if (var15 & var28):
                        var6 = i32_load(var20 + 32)
                        if i32_load(var20 + 32):
                        else:
                        var6 = 0
                        if (1 if 0 >= i32_load(var20 + 44) else 0):
                            break
                        var14 = (i32_load(var20 + 48) + (var6 * 548))
                    if (1 if var19 <= 0 else 0):
                        break
                    if (1 if var3 <= var10 else 0):
                        break
                    var6 = i32_load(var17)
                    while True:  # loop $label27
                        var7 = i32_load(var10)
                        i32_store((var6 + ((((i32_load(var10) * 506832829) & 0xFFFFFFFF) >> i32_load(var17 + 4)) << 2)), var7)
                        var10 = (var10 + 4)
                        if (1 if (var10 + 4) < var3 else 0):
                            continue
                        break  # end loop
                    break
                if (1 if var6 >= var30 else 0):
                    break
                if (1 if var19 <= 0 else 0):
                    break
                if (1 if var3 > var10 else 0):
                    var7 = i32_load(var17)
                    while True:  # loop $label29
                        var8 = i32_load(var10)
                        i32_store((var7 + ((((i32_load(var10) * 506832829) & 0xFFFFFFFF) >> i32_load(var17 + 4)) << 2)), var8)
                        var10 = (var10 + 4)
                        if (1 if (var10 + 4) < var3 else 0):
                            continue
                        break  # end loop
                var6 = (var6 - 280)
                if (((var6 - 280) & 0xFFFFFFFF) >> i32_load(var17 + 8)):
                    break
                var6 = i32_load((i32_load(var17) + (var6 << 2)))
                break
                a_c()
                raise RuntimeError('unreachable')
                a_c()
                raise RuntimeError('unreachable')
                a_c()
                raise RuntimeError('unreachable')
                a_c()
                raise RuntimeError('unreachable')
                a_c()
                raise RuntimeError('unreachable')
                a_c()
                raise RuntimeError('unreachable')
                i32_store(var3, var6)
                var6 = (var3 + 4)
                var15 = (var15 + 1)
                if (1 if var2 > (var15 + 1) else 0):
                    var3 = var6
                    break
                var7 = (var13 + 1)
                if (1 if var5 == 0 else 0):
                    break
                if (1 if var4 <= var13 else 0):
                    break
                if (var7 & 15):
                    break
                # call_indirect via table[var5]
                var15 = 0
                if (1 if var19 <= 0 else 0):
                    break
                if (1 if var6 <= var10 else 0):
                    break
                var13 = i32_load(var17)
                while True:  # loop $label33
                    var8 = i32_load(var10)
                    i32_store((var13 + ((((i32_load(var10) * 506832829) & 0xFFFFFFFF) >> i32_load(var17 + 4)) << 2)), var8)
                    var8 = (1 if var3 > var10 else 0)
                    var10 = (var10 + 4)
                    if var8:
                        continue
                    break  # end loop
                var3 = var6
                var13 = var7
                if (1 if var3 < var26 else 0):
                    continue
                break  # end loop
            var2 = i32_load(var0 + 40)
            var6 = i32_load(var0 + 36)
            if (1 if i32_load(var0 + 40) > i32_load(var0 + 36) else 0):
                break
            if (1 if i32_load(var0 + 48) == 0 else 0):
                var10 = 0
                if (1 if var2 == var6 else 0):
                    var10 = (1 if i32_load(var0 + 44) > 64 else 0)
                i32_store(var0 + 48, var10)
                if i32_load(var0 + 56):
                    break
                break
            var10 = 1
            i32_store(var0 + 48, 1)
            if (1 if i32_load(var0 + 56) == 0 else 0):
                break
            var2 = (1 if var3 < var26 else 0)
            var6 = ((1 if var3 < var26 else 0) & (1 if var10 != 0 else 0))
            if (1 if (((1 if var3 < var26 else 0) & (1 if var10 != 0 else 0)) if var2 else 1) == 0 else 0):
                break
            if var6:
                i32_store(var0, 5)
                i64_store(var16, i64_load(var0 + 64))
                i64_store(var16 + 24, i64_load(var0 + 88))
                i64_store(var16 + 16, i64_load(var0 + 80))
                i64_store(var16 + 8, i64_load(var0 + 72))
                i32_store(var0 + 112, i32_load(var0 + 96))
                var10 = 1
                if (1 if i32_load(var0 + 120) <= 0 else 0):
                    break
                func456((var0 + 136), var25)
                return 1
            if (1 if var3 >= var26 else 0):
                break
            if var10:
                break
            if var5:
                # call_indirect via table[var5]
            i32_store(var0, 0)
            i32_store(var0 + 112, ((var3 - var1) >> 2))
            return 1
            var10 = 0
            # br_table ['$label40', '$label38', '$label38', '$label38', '$label38', '$label40', '$label38']
            _br_idx = i32_load(var0)
            break  # br_table
            i32_store(var0, 3)
            return var10
            a_c()
            raise RuntimeError('unreachable')
        a_c()
        raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    return 3160

