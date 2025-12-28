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
# $func449
# ==========================================================
def func449(var0, var1, var2, var3, var4, param5, param6, param7, param8, param9, param10, param11, param12, param13, param14, param15):
    var5 = 0
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
    var33 = 0
    var34 = 0
    var35 = 0
    var36 = 0
    var37 = 0
    var38 = 0
    var39 = 0
    var40 = 0
    var41 = 0
    var23 = (global0 - 144)
    global global0
    global0 = (global0 - 144)
    if (1 if var2 == 0 else 0):
        break
    var7 = (var23 + 4)
    if (var23 + 4):
        # Unknown: memory.fill []
    else:
    if (1 if 0 == 0 else 0):
        break
    i32_store(var23 + 140, 0)
    i64_store(var23 + 132, 0)
    i64_store(var23 + 124, 0)
    i64_store(var23 + 116, 0)
    i64_store(var23 + 108, 0)
    i64_store(var23 + 100, 0)
    i32_store(var23 + 28, var3)
    i32_store(var23 + 24, var4)
    i64_store(var23 + 92, 0)
    i32_store(var23 + 4, 1)
    i32_store(var23 + 16, 1)
    i32_store(var23 + 88, (var23 + 4))
    i32_store(var23 + 20, var2)
    var26 = (var23 + 88)
    var14 = (global0 - 160)
    global global0
    global0 = (global0 - 160)
    i32_store(var14 + 20, 1)
    i32_store(var14 + 16, var1)
    i32_store(var14 + 12, var0)
    i32_store(var14 + 156, 0)
    var7 = (var14 + 156)
    var9 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    i32_store(var9 + 56, var1)
    var2 = var0
    i32_store(var9 + 60, var0)
    var17 = (var14 + 12)
    if (var14 + 12):
    else:
    var4 = 0
    if (1 if var2 == 0 else 0):
        var3 = 7
        break
    if (1 if var1 < 12 else 0):
        var3 = 7
        break
    i32_store(var9 + 44, 0)
    i64_store(var9 + 36, 0)
    i64_store(var9 + 28, 0)
    i64_store(var9 + 20, 0)
    i32_store(var9 + 16, var1)
    i32_store(var9 + 12, var2)
    var13 = func358(var2, 6935)
    if func358(var2, 6935):
        break
    var3 = 3
    if (1 if i32_load(var2 + 8) != 1346520407 else 0):
        break
    var12 = i32_load(var2 + 4)
    if (1 if (i32_load(var2 + 4) + 9) < 21 else 0):
        break
    if (1 if var4 == 0 else 0):
        break
    if (1 if var12 <= (var1 - 8) else 0):
        break
    var3 = 7
    break
    i32_store(var9 + 40, var12)
    var2 = (var2 + 12)
    i32_store(var9 + 60, (var2 + 12))
    var1 = (var1 - 12)
    i32_store(var9 + 56, (var1 - 12))
    if (1 if var1 >= 8 else 0):
        break
    var3 = 7
    break
    var8 = func358(var2, 5741)
    if (1 if func358(var2, 5741) == 0 else 0):
        if (1 if i32_load(var2 + 4) != 10 else 0):
            var3 = 3
            break
        var3 = 7
        if (1 if var1 < 18 else 0):
            break
        var16 = ((i32_load16_u(var2 + 12) | (i32_load8_u(var2 + 14) << 16)) + 1)
        var15 = ((i32_load16_u(var2 + 15) | (i32_load8_u(var2 + 17) << 16)) + 1)
        if (1 if (((i64_extend_u(((i32_load16_u(var2 + 12) | (i32_load8_u(var2 + 14) << 16)) + 1)) * i64_extend_u(((i32_load16_u(var2 + 15) | (i32_load8_u(var2 + 17) << 16)) + 1))) & 0xFFFFFFFFFFFFFFFF) >> 32) != 0 else 0):
            var3 = 3
            break
        var0 = i32_load(var2 + 8)
        var1 = (var1 - 18)
        i32_store(var9 + 56, (var1 - 18))
        var2 = (var2 + 18)
        i32_store(var9 + 60, (var2 + 18))
        var3 = 3
        if var13:
            break
        var18 = (((var0 & 2) & 0xFFFFFFFF) >> 1)
    if var7:
        i32_store(var7, var18)
    i32_store(var9 + 48, var15)
    i32_store(var9 + 52, var16)
    if ((1 if var17 == 0 else 0) & var18):
        break
    var0 = 7
    if (1 if var1 < 4 else 0):
        break
    var21 = (var9 + 56)
    if (var8 | var13):
        if (1 if var13 == 0 else 0):
            break
        if (1 if var8 == 0 else 0):
            break
        if (1 if i32_load(var2) != 1213221953 else 0):
            break
    var11 = (var9 + 56)
    var13 = (var9 + 28)
    var7 = (var9 + 32)
    if (var9 + 60):
        if (1 if var11 == 0 else 0):
            break
        if (1 if var13 == 0 else 0):
            break
        if (1 if var7 == 0 else 0):
            break
        var1 = i32_load(var11)
        var2 = i32_load(var9 + 60)
        i32_store(var13, 0)
        i32_store(var7, 0)
        i32_store(var9 + 60, var2)
        i32_store(var11, var1)
        if (1 if var1 < 8 else 0):
            break
        if (1 if var12 == 0 else 0):
            while True:  # loop $label12
                var3 = i32_load(var2 + 4)
                if (1 if i32_load(var2 + 4) > -10 else 0):
                    break
                var18 = 0
                if (1 if i32_load(var2) == 540561494 else 0):
                    break
                if (1 if i32_load(var2) == 1278758998 else 0):
                    break
                var0 = ((var3 + 9) & -2)
                if (1 if ((var3 + 9) & -2) > var1 else 0):
                    break
                if (1 if i32_load(var2) == 1213221953 else 0):
                    i32_store(var13, (var2 + 8))
                    i32_store(var7, var3)
                var2 = (var0 + var2)
                i32_store(var9 + 60, (var0 + var2))
                var1 = (var1 - var0)
                i32_store(var11, (var1 - var0))
                if (1 if var1 >= 8 else 0):
                    continue
                break  # end loop
            break
        var29 = 22
        while True:  # loop $label13
            var18 = 3
            var0 = i32_load(var2 + 4)
            if (1 if i32_load(var2 + 4) > -10 else 0):
                break
            var3 = ((var0 + 9) & -2)
            var29 = (((var0 + 9) & -2) + var29)
            if (1 if (((var0 + 9) & -2) + var29) > var12 else 0):
                break
            var18 = 0
            if (1 if i32_load(var2) == 540561494 else 0):
                break
            if (1 if i32_load(var2) == 1278758998 else 0):
                break
            if (1 if var1 < var3 else 0):
                break
            if (1 if i32_load(var2) == 1213221953 else 0):
                i32_store(var13, (var2 + 8))
                i32_store(var7, var0)
            var2 = (var2 + var3)
            i32_store(var9 + 60, (var2 + var3))
            var1 = (var1 - var3)
            i32_store(var11, (var1 - var3))
            var18 = 7
            if (1 if var1 > 7 else 0):
                continue
            break  # end loop
        break
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    var0 = 3290
    if 3290:
        break
    var2 = i32_load(var9 + 40)
    var13 = (var9 + 36)
    var7 = (var9 + 44)
    var11 = i32_load(var9 + 60)
    if i32_load(var9 + 60):
        if (1 if var21 == 0 else 0):
            break
        if (1 if var13 == 0 else 0):
            break
        if (1 if var7 == 0 else 0):
            break
        var1 = i32_load(var21)
        if (1 if i32_load(var21) < 8 else 0):
            break
        var0 = i32_load(var11)
        if (1 if ((1 if i32_load(var11) != 540561494 else 0) & (1 if var0 != 1278758998 else 0)) == 0 else 0):
            var3 = i32_load(var11 + 4)
            if (1 if var2 >= 12 else 0):
                if (1 if var3 > (var2 - 12) else 0):
                    break
            if var4:
                if (1 if var3 > (var1 - 8) else 0):
                    break
            i32_store(var13, var3)
            i32_store(var9 + 60, (var11 + 8))
            i32_store(var21, (i32_load(var21) - 8))
            i32_store(var7, (1 if var0 == 1278758998 else 0))
            break
        var0 = 0
        if (1 if var1 < 5 else 0):
            break
        if (1 if i32_load8_u(var11) != 47 else 0):
            break
        var0 = (1 if i32_load8_u(var11 + 4) < 32 else 0)
        i32_store(var7, var0)
        i32_store(var13, i32_load(var21))
        break
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    var0 = 3702
    if 3702:
        break
    var3 = 3
    var2 = i32_load(var9 + 36)
    if (1 if i32_load(var9 + 36) > -10 else 0):
        break
    var13 = i32_load(var9 + 56)
    if (1 if i32_load(var9 + 44) == 0 else 0):
        var0 = 7
        if (1 if var13 < 10 else 0):
            break
        var7 = (var9 + 52)
        var4 = (var9 + 48)
        var0 = 0
        var11 = i32_load(var9 + 60)
        if (1 if i32_load(var9 + 60) == 0 else 0):
            break
        if (1 if var13 < 10 else 0):
            break
        if (1 if i32_load8_u(var11 + 3) != 157 else 0):
            break
        if (1 if i32_load8_u(var11 + 4) != 1 else 0):
            break
        if (1 if i32_load8_u(var11 + 5) != 42 else 0):
            break
        var1 = i32_load8_u(var11)
        if (1 if (i32_load8_u(var11) & 25) != 16 else 0):
            break
        if (1 if (((((i32_load8_u(var11 + 1) << 8) | (i32_load8_u(var11 + 2) << 16)) | var1) & 0xFFFFFFFF) >> 5) >= var2 else 0):
            break
        var2 = (i32_load8_u(var11 + 6) | ((i32_load8_u(var11 + 7) << 8) & 16128))
        if (1 if (i32_load8_u(var11 + 6) | ((i32_load8_u(var11 + 7) << 8) & 16128)) == 0 else 0):
            break
        var1 = (i32_load8_u(var11 + 8) | ((i32_load8_u(var11 + 9) << 8) & 16128))
        if (1 if (i32_load8_u(var11 + 8) | ((i32_load8_u(var11 + 9) << 8) & 16128)) == 0 else 0):
            break
        if var7:
            i32_store(var7, var2)
        var0 = 1
        if (1 if var4 == 0 else 0):
            break
        i32_store(var4, var1)
        if var0:
            break
        break
    var0 = 7
    if (1 if var13 < 5 else 0):
        break
    var1 = i32_load(var9 + 60)
    var7 = (var9 + 52)
    var4 = (var9 + 48)
    var0 = 0
    var11 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    if (1 if var1 == 0 else 0):
        break
    if (1 if var13 < 5 else 0):
        break
    if (1 if i32_load8_u(var1) != 47 else 0):
        break
    if (1 if i32_load8_u(var1 + 4) > 31 else 0):
        break
    if (1 if func39(var11, 8) != 47 else 0):
        break
    var2 = func39(var11, 14)
    var1 = func39(var11, 14)
    if (func39(var11, 3) | i32_load(var11 + 24)):
        break
    if var7:
        i32_store(var7, (var2 + 1))
    if var4:
        i32_store(var4, (var1 + 1))
    var0 = 1
    global global0
    global0 = (var11 + 32)
    if (1 if var0 == 0 else 0):
        break
    if (1 if var8 == 0 else 0):
        if (1 if var16 != i32_load(var9 + 52) else 0):
            break
        if (1 if var15 != i32_load(var9 + 48) else 0):
            break
    if (1 if var17 == 0 else 0):
        break
    var40 = i64_load(var9 + 12)
    i64_store(var17, i64_load(var9 + 12))
    i32_store(var17 + 32, i32_load(var9 + 44))
    i64_store(var17 + 24, i64_load(var9 + 36))
    i64_store(var17 + 16, i64_load(var9 + 28))
    i64_store(var17 + 8, i64_load(var9 + 20))
    var0 = (i32_load(var9 + 60) - i32(var40))
    i32_store(var17 + 12, (i32_load(var9 + 60) - i32(var40)))
    if (1 if var0 < 0 else 0):
        break
    if (1 if var0 == (i32_load(var17 + 4) - i32_load(var9 + 56)) else 0):
        break
    a_c()
    raise RuntimeError('unreachable')
    if var17:
        var3 = var0
        break
    if var8:
        var3 = var0
        break
    var3 = var0
    if (1 if var0 != 7 else 0):
        break
    var3 = 0
    global global0
    global0 = (var9 - -64)
    break
    a_c()
    raise RuntimeError('unreachable')
    i32_store(399 + 48, 4033)
    if i32_load(var14 + 48):
        if (1 if i32_load(var14 + 48) != 7 else 0):
            break
        if i32_load(var14 + 156):
            break
        break
    if (1 if i32_load(var14 + 156) == 0 else 0):
        break
    i32_store(var14 + 48, 4)
    if i32_load(var14 + 48):
        break
    if (1 if var26 == 0 else 0):
        break
    var0 = (var14 + 48)
    if (var14 + 48):
        # Unknown: memory.fill []
    var0 = i32_load(var14 + 24)
    i32_store(var14 + 112, (i32_load(var14 + 24) + i32_load(var14 + 12)))
    i32_store(var14 + 108, (i32_load(var14 + 16) - var0))
    i32_store(var14 + 100, 262)
    i32_store(var14 + 96, 263)
    i32_store(var14 + 92, 264)
    i32_store(var14 + 88, var26)
    if (1 if i32_load(var14 + 44) == 0 else 0):
        var5 = func134(1, 2424)
        if (1 if func134(1, 2424) == 0 else 0):
            break
        i32_store(var5 + 8, 6932)
        i32_store(var5, 0)
        # call_indirect via table[i32_load(52340)]
        i32_store(var5 + 324, 0)
        i32_store(var5 + 4, 0)
        var0 = i32_load(52304)
        if (1 if i32_load(52304) == i32_load(52296) else 0):
            break
        if var0:
            # call_indirect via table[var0]
            if call_indirect(var0):
                break
        i32_store(279, 280)
        i32_store(52296, i32_load(52304))
        if (1 if var5 == 0 else 0):
            break
        i32_store(var5 + 2392, i32_load(var14 + 28))
        i32_store(var5 + 2396, i32_load(var14 + 32))
        if func458(var5, (var14 + 48)):
            var3 = func451(i32_load(var14 + 48), i32_load(var14 + 52), i32_load(var26 + 20), i32_load(var26))
            if func451(i32_load(var14 + 48), i32_load(var14 + 52), i32_load(var26 + 20), i32_load(var26)):
                break
            var1 = (var14 + 12)
            var0 = i32_load(var26 + 20)
            if (1 if i32_load(var26 + 20) == 0 else 0):
                break
            if (1 if var1 == 0 else 0):
                break
            if (1 if i32_load(var0 + 40) == 0 else 0):
                break
            if (1 if i32_load(var1 + 32) == 0 else 0):
                break
            a_c()
            raise RuntimeError('unreachable')
            i32_store(var5 + 160, 0)
            var2 = i32_load(var26 + 20)
            if var5:
                if (1 if var2 == 0 else 0):
                    break
                var0 = i32_load(var2 + 44)
                if (1 if i32_load(var2 + 44) < 0 else 0):
                    break
                var3 = 255
                if (1 if var0 <= 100 else 0):
                    var3 = ((((var0 * 255) & 65535) & 0xFFFFFFFF) // 100)
                    if (1 if (var0 & 65535) == 0 else 0):
                        break
                var0 = i32_load(var5 + 844)
                if (1 if i32_load(var5 + 844) >= 12 else 0):
                    var1 = i32_load(var5 + 848)
                    break
                var1 = (((var3 * i32_load8_u(((var0 if (1 if var0 > 0 else 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3)
                i32_store(var5 + 848, (((var3 * i32_load8_u(((var0 if (1 if var0 > 0 else 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3))
                var0 = i32_load(var5 + 876)
                if (1 if i32_load(var5 + 876) >= 12 else 0):
                    var10 = i32_load(var5 + 880)
                    break
                var10 = (((var3 * i32_load8_u(((var0 if (1 if var0 > 0 else 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3)
                i32_store(var5 + 880, (((var3 * i32_load8_u(((var0 if (1 if var0 > 0 else 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3))
                var0 = (var1 | var10)
                var1 = i32_load(var5 + 908)
                if (1 if i32_load(var5 + 908) >= 12 else 0):
                    var10 = i32_load(var5 + 912)
                    break
                var10 = (((var3 * i32_load8_u(((var1 if (1 if var1 > 0 else 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3)
                i32_store(var5 + 912, (((var3 * i32_load8_u(((var1 if (1 if var1 > 0 else 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3))
                var0 = (var0 | var10)
                var1 = i32_load(var5 + 940)
                if (1 if i32_load(var5 + 940) >= 12 else 0):
                    var3 = i32_load(var5 + 944)
                    break
                var3 = (((var3 * i32_load8_u(((var1 if (1 if var1 > 0 else 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3)
                i32_store(var5 + 944, (((var3 * i32_load8_u(((var1 if (1 if var1 > 0 else 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3))
                if (1 if (var0 | var3) == 0 else 0):
                    break
                # Unknown: memory.copy []
                i64_store(var5 + 588, 133143986176)
                i32_store(var5 + 816, 256)
                i32_store(var5 + 584, 1)
                var0 = i32_load(var2 + 52)
                i32_store(var5 + 2416, i32_load(var2 + 52))
                if (1 if var0 <= 100 else 0):
                    if (1 if var0 >= 0 else 0):
                        break
                else:
                i32_store(0 + 2416, 100)
                break
            a_c()
            raise RuntimeError('unreachable')
            var3 = 0
            var22 = (var14 + 48)
            var12 = 0
            var18 = 0
            if (1 if var5 == 0 else 0):
                break
            if (1 if var22 == 0 else 0):
                if i32_load(var5):
                    break
                i32_store(var5 + 8, 8496)
                i32_store(var5, 2)
                var39 = (var5 + 4)
                break
            var39 = (var5 + 4)
            if (1 if i32_load(var5 + 4) == 0 else 0):
                if (1 if func458(var5, var22) == 0 else 0):
                    break
                if (1 if i32_load(var5 + 4) == 0 else 0):
                    break
            var0 = i32_load(var22 + 48)
            if (1 if i32_load(var22 + 48) == 0 else 0):
                break
            # call_indirect via table[var0]
            if call_indirect(var0):
                break
            break
            if i32_load(var22 + 68):
                i32_store(var5 + 2352, 0)
                break
            var0 = 2
            var1 = i32_load(var5 + 2352)
            var12 = i32_load8_u((i32_load(var5 + 2352) + 10321))
            if (1 if var1 == 2 else 0):
                break
            var0 = var1
            var2 = (i32_load(var22 + 76) - var12)
            i32_store(var5 + 308, ((i32_load(var22 + 76) - var12) >> 4))
            var1 = (i32_load(var22 + 84) - var12)
            i32_store(var5 + 312, ((i32_load(var22 + 84) - var12) >> 4))
            if (1 if var2 < 0 else 0):
                i32_store(var5 + 308, 0)
            if (1 if var1 >= 0 else 0):
                break
            break
            i32_store(var5 + 308, 0)
            i32_store((var5 + 312), 0)
            var1 = (var12 + 15)
            var4 = (((var12 + 15) + i32_load(var22 + 88)) >> 4)
            i32_store(var5 + 320, (((var12 + 15) + i32_load(var22 + 88)) >> 4))
            var2 = ((var1 + i32_load(var22 + 80)) >> 4)
            var1 = i32_load(var5 + 300)
            i32_store(var5 + 316, (((var1 + i32_load(var22 + 80)) >> 4) if (1 if var1 > var2 else 0) else i32_load(var5 + 300)))
            var1 = i32_load(var5 + 304)
            if (1 if i32_load(var5 + 304) < var4 else 0):
                i32_store(var5 + 320, var1)
            if (1 if var0 > 0 else 0):
                var13 = i32_load(var5 + 116)
                if (1 if i32_load(var5 + 80) == 0 else 0):
                    if var13:
                        var0 = i32_load8_s(var5 + 132)
                        if i32_load(var5 + 124):
                            break
                        break
                    var0 = i32_load(var5 + 72)
                    var7 = ((i32_load(var5 + 72) + var0) if (1 if var0 >= 63 else 0) else i32_load(var5 + 72))
                    var0 = (1 if ((i32_load(var5 + 72) + var0) if (1 if var0 >= 63 else 0) else i32_load(var5 + 72)) > 0 else 0)
                    if (1 if (1 if ((i32_load(var5 + 72) + var0) if (1 if var0 >= 63 else 0) else i32_load(var5 + 72)) > 0 else 0) == 0 else 0):
                        i32_store8(var5 + 2356, 0)
                        i32_store8((var5 + 2360), 0)
                        i32_store8((var5 + 2358), 0)
                        break
                    var1 = (var7 if var0 else 0)
                    var4 = (2 if (1 if var1 > 39 else 0) else (1 if (var7 if var0 else 0) > 14 else 0))
                    var2 = (var1 << 1)
                    var0 = i32_load(var5 + 76)
                    if (1 if i32_load(var5 + 76) <= 0 else 0):
                        i32_store8((var5 + 2359), var4)
                        var0 = (var2 + var7)
                        i32_store8(var5 + 2356, (var2 + var7))
                        i32_store8((var5 + 2357), var7)
                        i32_store8((var5 + 2361), var7)
                        i32_store8((var5 + 2358), 0)
                        i32_store8((var5 + 2363), var4)
                        i32_store8((var5 + 2360), var0)
                        break
                    i32_store8((var5 + 2359), var4)
                    i32_store8((var5 + 2358), 0)
                    i32_store8((var5 + 2363), var4)
                    var1 = ((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1))
                    var0 = (9 - var0)
                    var0 = (((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var0))
                    var0 = (1 if (1 if var0 <= 1 else 0) else (((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var0)))
                    i32_store8((var5 + 2357), (1 if (1 if var0 <= 1 else 0) else (((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var0))))
                    i32_store8((var5 + 2361), var0)
                    var0 = (var0 + var2)
                    i32_store8(var5 + 2356, (var0 + var2))
                    i32_store8((var5 + 2360), var0)
                    break
                var16 = i32_load(var5 + 84)
                if (1 if var13 == 0 else 0):
                    var7 = (i32_load(var5 + 72) + var16)
                    var15 = (63 if (1 if var7 >= 63 else 0) else (i32_load(var5 + 72) + var16))
                    var0 = (1 if var15 > 0 else 0)
                    var2 = ((63 if (1 if var7 >= 63 else 0) else (i32_load(var5 + 72) + var16)) if (1 if var15 > 0 else 0) else 0)
                    if var0:
                        var0 = var2
                        var4 = i32_load(var5 + 76)
                        if (1 if i32_load(var5 + 76) > 0 else 0):
                            var1 = ((var2 & 0xFFFFFFFF) >> (2 if (1 if var4 > 4 else 0) else 1))
                            var0 = (9 - var4)
                            var0 = (((var2 & 0xFFFFFFFF) >> (2 if (1 if var4 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var4))
                        i32_store8((var5 + 2359), (2 if (1 if var2 > 39 else 0) else (1 if var2 > 14 else 0)))
                        var0 = (1 if (1 if var0 <= 1 else 0) else var0)
                        i32_store8((var5 + 2357), (1 if (1 if var0 <= 1 else 0) else var0))
                        i32_store8(var5 + 2356, (var0 + (var2 << 1)))
                        break
                    i32_store8(var5 + 2356, 0)
                    i32_store8((var5 + 2358), 0)
                    var0 = (i32_load(var5 + 100) + var7)
                    var13 = (63 if (1 if var0 >= 63 else 0) else (i32_load(var5 + 100) + var7))
                    var0 = (1 if var13 > 0 else 0)
                    var1 = ((63 if (1 if var0 >= 63 else 0) else (i32_load(var5 + 100) + var7)) if (1 if var13 > 0 else 0) else 0)
                    if var0:
                        var0 = var1
                        var7 = i32_load(var5 + 76)
                        if (1 if i32_load(var5 + 76) > 0 else 0):
                            var4 = ((var1 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1))
                            var0 = (9 - var7)
                            var0 = (((var1 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1)) if (1 if var0 > var4 else 0) else (9 - var7))
                        i32_store8((var5 + 2363), (2 if (1 if var1 > 39 else 0) else (1 if var1 > 14 else 0)))
                        var0 = (1 if (1 if var0 <= 1 else 0) else var0)
                        i32_store8((var5 + 2361), (1 if (1 if var0 <= 1 else 0) else var0))
                        i32_store8(var5 + 2360, (var0 + (var1 << 1)))
                        break
                    i32_store8(var5 + 2360, 0)
                    i32_store8((var5 + 2362), 1)
                    if (1 if var15 > 0 else 0):
                        var0 = var2
                        var7 = i32_load(var5 + 76)
                        if (1 if i32_load(var5 + 76) > 0 else 0):
                            var4 = ((var2 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1))
                            var0 = (9 - var7)
                            var0 = (((var2 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1)) if (1 if var0 > var4 else 0) else (9 - var7))
                        i32_store8((var5 + 2367), (2 if (1 if var2 > 39 else 0) else (1 if var2 > 14 else 0)))
                        var0 = (1 if (1 if var0 <= 1 else 0) else var0)
                        i32_store8((var5 + 2365), (1 if (1 if var0 <= 1 else 0) else var0))
                        i32_store8(var5 + 2364, (var0 + (var2 << 1)))
                        break
                    i32_store8(var5 + 2364, 0)
                    i32_store8((var5 + 2366), 0)
                    if (1 if var13 > 0 else 0):
                        var0 = var1
                        var7 = i32_load(var5 + 76)
                        if (1 if i32_load(var5 + 76) > 0 else 0):
                            var4 = ((var1 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1))
                            var0 = (9 - var7)
                            var0 = (((var1 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1)) if (1 if var0 > var4 else 0) else (9 - var7))
                        i32_store8((var5 + 2371), (2 if (1 if var1 > 39 else 0) else (1 if var1 > 14 else 0)))
                        var0 = (1 if (1 if var0 <= 1 else 0) else var0)
                        i32_store8((var5 + 2369), (1 if (1 if var0 <= 1 else 0) else var0))
                        i32_store8(var5 + 2368, (var0 + (var1 << 1)))
                        break
                    i32_store8(var5 + 2368, 0)
                    i32_store8((var5 + 2370), 1)
                    if (1 if var15 > 0 else 0):
                        var0 = var2
                        var7 = i32_load(var5 + 76)
                        if (1 if i32_load(var5 + 76) > 0 else 0):
                            var4 = ((var2 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1))
                            var0 = (9 - var7)
                            var0 = (((var2 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1)) if (1 if var0 > var4 else 0) else (9 - var7))
                        i32_store8((var5 + 2375), (2 if (1 if var2 > 39 else 0) else (1 if var2 > 14 else 0)))
                        var0 = (1 if (1 if var0 <= 1 else 0) else var0)
                        i32_store8((var5 + 2373), (1 if (1 if var0 <= 1 else 0) else var0))
                        i32_store8(var5 + 2372, (var0 + (var2 << 1)))
                        break
                    i32_store8(var5 + 2372, 0)
                    i32_store8((var5 + 2374), 0)
                    if (1 if var13 > 0 else 0):
                        var0 = var1
                        var7 = i32_load(var5 + 76)
                        if (1 if i32_load(var5 + 76) > 0 else 0):
                            var4 = ((var1 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1))
                            var0 = (9 - var7)
                            var0 = (((var1 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1)) if (1 if var0 > var4 else 0) else (9 - var7))
                        i32_store8((var5 + 2379), (2 if (1 if var1 > 39 else 0) else (1 if var1 > 14 else 0)))
                        var0 = (1 if (1 if var0 <= 1 else 0) else var0)
                        i32_store8((var5 + 2377), (1 if (1 if var0 <= 1 else 0) else var0))
                        i32_store8(var5 + 2376, (var0 + (var1 << 1)))
                        break
                    i32_store8(var5 + 2376, 0)
                    i32_store8((var5 + 2378), 1)
                    if (1 if var15 > 0 else 0):
                        var0 = var2
                        var7 = i32_load(var5 + 76)
                        if (1 if i32_load(var5 + 76) > 0 else 0):
                            var4 = ((var2 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1))
                            var0 = (9 - var7)
                            var0 = (((var2 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1)) if (1 if var0 > var4 else 0) else (9 - var7))
                        i32_store8((var5 + 2383), (2 if (1 if var2 > 39 else 0) else (1 if var2 > 14 else 0)))
                        var0 = (1 if (1 if var0 <= 1 else 0) else var0)
                        i32_store8((var5 + 2381), (1 if (1 if var0 <= 1 else 0) else var0))
                        i32_store8(var5 + 2380, (var0 + (var2 << 1)))
                        break
                    i32_store8(var5 + 2380, 0)
                    i32_store8((var5 + 2382), 0)
                    if (1 if var13 > 0 else 0):
                        var0 = var1
                        var4 = i32_load(var5 + 76)
                        if (1 if i32_load(var5 + 76) > 0 else 0):
                            var2 = ((var1 & 0xFFFFFFFF) >> (2 if (1 if var4 > 4 else 0) else 1))
                            var0 = (9 - var4)
                            var0 = (((var1 & 0xFFFFFFFF) >> (2 if (1 if var4 > 4 else 0) else 1)) if (1 if var0 > var2 else 0) else (9 - var4))
                        i32_store8((var5 + 2387), (2 if (1 if var1 > 39 else 0) else (1 if var1 > 14 else 0)))
                        var0 = (1 if (1 if var0 <= 1 else 0) else var0)
                        i32_store8((var5 + 2385), (1 if (1 if var0 <= 1 else 0) else var0))
                        i32_store8(var5 + 2384, (var0 + (var1 << 1)))
                        break
                    i32_store8(var5 + 2384, 0)
                    i32_store8((var5 + 2386), 1)
                    break
                var4 = i32_load(var5 + 100)
                var2 = i32_load(var5 + 124)
                var12 = 0
                while True:  # loop $label61
                    var0 = i32_load8_s((var5 + var12) + 132)
                    var11 = (var5 + (var12 << 3))
                    var13 = ((var5 + (var12 << 3)) + 2356)
                    if var2:
                    else:
                    var15 = ((i32_load(var5 + 72) + var0) + var16)
                    var0 = (var0 if (1 if var15 >= 63 else 0) else ((i32_load(var5 + 72) + var0) + var16))
                    if (1 if (var0 if (1 if var15 >= 63 else 0) else ((i32_load(var5 + 72) + var0) + var16)) > 0 else 0):
                        var8 = (var0 if (1 if var0 > 0 else 0) else 0)
                        var0 = (var0 if (1 if var0 > 0 else 0) else 0)
                        var7 = i32_load(var5 + 76)
                        if (1 if i32_load(var5 + 76) > 0 else 0):
                            var1 = ((var8 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1))
                            var0 = (9 - var7)
                            var0 = (((var8 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var7))
                        var0 = (1 if (1 if var0 <= 1 else 0) else var0)
                        i32_store8((var11 + 2357), (1 if (1 if var0 <= 1 else 0) else var0))
                        i32_store8(var13, (var0 + (var8 << 1)))
                        i32_store8((var11 + 2359), (2 if (1 if var8 > 39 else 0) else (1 if var8 > 14 else 0)))
                        break
                    i32_store8(var13, 0)
                    i32_store8((var11 + 2358), 0)
                    var13 = (var11 + 2360)
                    var0 = (var4 + var15)
                    var0 = (63 if (1 if var0 >= 63 else 0) else (var4 + var15))
                    if (1 if (63 if (1 if var0 >= 63 else 0) else (var4 + var15)) > 0 else 0):
                        var15 = (var0 if (1 if var0 > 0 else 0) else 0)
                        var0 = (var0 if (1 if var0 > 0 else 0) else 0)
                        var7 = i32_load(var5 + 76)
                        if (1 if i32_load(var5 + 76) > 0 else 0):
                            var1 = ((var15 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1))
                            var0 = (9 - var7)
                            var0 = (((var15 & 0xFFFFFFFF) >> (2 if (1 if var7 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var7))
                        var0 = (1 if (1 if var0 <= 1 else 0) else var0)
                        i32_store8((var11 + 2361), (1 if (1 if var0 <= 1 else 0) else var0))
                        i32_store8(var13, (var0 + (var15 << 1)))
                        i32_store8((var11 + 2363), (2 if (1 if var15 > 39 else 0) else (1 if var15 > 14 else 0)))
                        break
                    i32_store8(var13, 0)
                    i32_store8((var11 + 2362), 1)
                    var12 = (var12 + 1)
                    if (1 if (var12 + 1) != 4 else 0):
                        continue
                    break  # end loop
            break
            i32_store8((var5 + 2362), 1)
            if var13:
                var0 = i32_load8_s(var5 + 133)
                if i32_load(var5 + 124):
                    break
                break
            var0 = i32_load(var5 + 72)
            var7 = ((i32_load(var5 + 72) + var0) if (1 if var0 >= 63 else 0) else i32_load(var5 + 72))
            if (1 if ((i32_load(var5 + 72) + var0) if (1 if var0 >= 63 else 0) else i32_load(var5 + 72)) > 0 else 0):
                var1 = (var7 if (1 if var7 > 0 else 0) else 0)
                var4 = (2 if (1 if var1 > 39 else 0) else (1 if (var7 if (1 if var7 > 0 else 0) else 0) > 14 else 0))
                var2 = (var1 << 1)
                var0 = i32_load(var5 + 76)
                if (1 if i32_load(var5 + 76) <= 0 else 0):
                    i32_store8((var5 + 2367), var4)
                    var0 = (var2 + var7)
                    i32_store8((var5 + 2364), (var2 + var7))
                    i32_store8((var5 + 2365), var7)
                    i32_store8((var5 + 2369), var7)
                    i32_store8((var5 + 2366), 0)
                    i32_store8((var5 + 2371), var4)
                    i32_store8((var5 + 2368), var0)
                    break
                i32_store8((var5 + 2367), var4)
                i32_store8((var5 + 2366), 0)
                i32_store8((var5 + 2371), var4)
                var1 = ((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1))
                var0 = (9 - var0)
                var0 = (((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var0))
                var0 = (1 if (1 if var0 <= 1 else 0) else (((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var0)))
                i32_store8((var5 + 2365), (1 if (1 if var0 <= 1 else 0) else (((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var0))))
                i32_store8((var5 + 2369), var0)
                var0 = (var0 + var2)
                i32_store8((var5 + 2364), (var0 + var2))
                i32_store8((var5 + 2368), var0)
                break
            i32_store8((var5 + 2368), 0)
            i32_store8((var5 + 2366), 0)
            i32_store8((var5 + 2364), 0)
            i32_store8((var5 + 2370), 1)
            if var13:
                var0 = i32_load8_s(var5 + 134)
                if i32_load(var5 + 124):
                    break
                break
            var0 = i32_load(var5 + 72)
            var7 = ((i32_load(var5 + 72) + var0) if (1 if var0 >= 63 else 0) else i32_load(var5 + 72))
            if (1 if ((i32_load(var5 + 72) + var0) if (1 if var0 >= 63 else 0) else i32_load(var5 + 72)) > 0 else 0):
                var1 = (var7 if (1 if var7 > 0 else 0) else 0)
                var4 = (2 if (1 if var1 > 39 else 0) else (1 if (var7 if (1 if var7 > 0 else 0) else 0) > 14 else 0))
                var2 = (var1 << 1)
                var0 = i32_load(var5 + 76)
                if (1 if i32_load(var5 + 76) <= 0 else 0):
                    i32_store8((var5 + 2375), var4)
                    var0 = (var2 + var7)
                    i32_store8((var5 + 2372), (var2 + var7))
                    i32_store8((var5 + 2373), var7)
                    i32_store8((var5 + 2377), var7)
                    i32_store8((var5 + 2374), 0)
                    i32_store8((var5 + 2379), var4)
                    i32_store8((var5 + 2376), var0)
                    break
                i32_store8((var5 + 2375), var4)
                i32_store8((var5 + 2374), 0)
                i32_store8((var5 + 2379), var4)
                var1 = ((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1))
                var0 = (9 - var0)
                var0 = (((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var0))
                var0 = (1 if (1 if var0 <= 1 else 0) else (((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var0)))
                i32_store8((var5 + 2373), (1 if (1 if var0 <= 1 else 0) else (((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var0))))
                i32_store8((var5 + 2377), var0)
                var0 = (var0 + var2)
                i32_store8((var5 + 2372), (var0 + var2))
                i32_store8((var5 + 2376), var0)
                break
            i32_store8((var5 + 2376), 0)
            i32_store8((var5 + 2374), 0)
            i32_store8((var5 + 2372), 0)
            i32_store8((var5 + 2378), 1)
            if var13:
                var0 = i32_load8_s(var5 + 135)
                if i32_load(var5 + 124):
                    break
                break
            var0 = i32_load(var5 + 72)
            var7 = ((i32_load(var5 + 72) + var0) if (1 if var0 >= 63 else 0) else i32_load(var5 + 72))
            if (1 if ((i32_load(var5 + 72) + var0) if (1 if var0 >= 63 else 0) else i32_load(var5 + 72)) > 0 else 0):
                var1 = (var7 if (1 if var7 > 0 else 0) else 0)
                var4 = (2 if (1 if var1 > 39 else 0) else (1 if (var7 if (1 if var7 > 0 else 0) else 0) > 14 else 0))
                var2 = (var1 << 1)
                var0 = i32_load(var5 + 76)
                if (1 if i32_load(var5 + 76) <= 0 else 0):
                    i32_store8((var5 + 2383), var4)
                    var0 = (var2 + var7)
                    i32_store8((var5 + 2380), (var2 + var7))
                    i32_store8((var5 + 2381), var7)
                    i32_store8((var5 + 2385), var7)
                    i32_store8((var5 + 2382), 0)
                    i32_store8((var5 + 2387), var4)
                    i32_store8((var5 + 2384), var0)
                    break
                i32_store8((var5 + 2383), var4)
                i32_store8((var5 + 2382), 0)
                i32_store8((var5 + 2387), var4)
                var1 = ((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1))
                var0 = (9 - var0)
                var0 = (((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var0))
                var0 = (1 if (1 if var0 <= 1 else 0) else (((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var0)))
                i32_store8((var5 + 2381), (1 if (1 if var0 <= 1 else 0) else (((var1 & 0xFFFFFFFF) >> (2 if (1 if var0 > 4 else 0) else 1)) if (1 if var0 > var1 else 0) else (9 - var0))))
                i32_store8((var5 + 2385), var0)
                var0 = (var0 + var2)
                i32_store8((var5 + 2380), (var0 + var2))
                i32_store8((var5 + 2384), var0)
                break
            i32_store8((var5 + 2384), 0)
            i32_store8((var5 + 2382), 0)
            i32_store8((var5 + 2380), 0)
            i32_store8((var5 + 2386), 1)
            if 0:
                break
            var1 = 0
            i32_store(var5 + 164, 0)
            var12 = 1
            if (1 if i32_load(var5 + 160) > 0 else 0):
                # call_indirect via table[i32_load(52344)]
                if (1 if call_indirect(i32_load(52344)) == 0 else 0):
                    break
                i32_store(var5 + 152, (var5 + 192))
                i32_store(var5 + 148, var5)
                i32_store(var5 + 144, 261)
                var12 = (3 if (1 if i32_load(var5 + 2352) > 0 else 0) else 2)
            i32_store(var5 + 168, var12)
            break
            if (1 if func99(var5, 1, 8437) == 0 else 0):
                break
            var12 = i32_load(var5 + 168)
            var9 = i32_load(var5 + 300)
            var2 = i32_load(var5 + 160)
            var19 = i32_load(var5 + 2352)
            var15 = (((i32_load(var5 + 300) << (1 if i32_load(var5 + 160) > 0 else 0)) << 2) if (1 if i32_load(var5 + 2352) > 0 else 0) else 0)
            var4 = (var9 << 5)
            var13 = (var12 << 4)
            var11 = ((var9 << 5) * ((((var12 << 4) + i32_load8_u((var19 + 10321))) * 3) // 2))
            var17 = (var9 << 2)
            var21 = ((var9 << 1) + 2)
            var8 = ((var9 << (1 if var2 == 2 else 0)) * 800)
            if i32_load(var5 + 2392):
            else:
            var41 = 0
            var40 = (0 + (i64_extend_u(var11) + (i64_extend_u(var15) + (i64_extend_u(var8) + (i64_extend_u(var21) + (i64_extend_u(var4) + i64_extend_u(var17)))))))
            if (1 if (0 + (i64_extend_u(var11) + (i64_extend_u(var15) + (i64_extend_u(var8) + (i64_extend_u(var21) + (i64_extend_u(var4) + i64_extend_u(var17))))))) > 4294966432 else 0):
                break
            var10 = i32_load(var5 + 2332)
            var40 = (var40 + 863)
            var1 = i32_load(var5 + 2336)
            if (1 if (var40 + 863) > i64_extend_u(i32_load(var5 + 2336)) else 0):
                var1 = 0
                i32_store(var5 + 2336, 0)
                var10 = func58(var40, 1)
                i32_store(var5 + 2332, func58(var40, 1))
                if (1 if var10 == 0 else 0):
                    break
                var1 = i32(var40)
                i32_store(var5 + 2336, i32(var40))
                var19 = i32_load(var5 + 2352)
                var2 = i32_load(var5 + 160)
            i32_store(var5 + 2288, var10)
            i32_store(var5 + 172, 0)
            var0 = (var10 + var17)
            i32_store(var5 + 2296, (var10 + var17))
            var0 = (var0 + var4)
            var7 = ((var0 + var4) + 2)
            i32_store(var5 + 2300, ((var0 + var4) + 2))
            var0 = (var0 + var21)
            var4 = ((var0 + var21) if var15 else 0)
            i32_store(var5 + 2304, ((var0 + var21) if var15 else 0))
            i32_store(var5 + 184, var4)
            var0 = (var0 + var15)
            if (1 if var19 > 0 else 0):
                if (1 if var2 <= 0 else 0):
                    var25 = ((var0 + 31) & -32)
                    i32_store(var5 + 2308, ((var0 + 31) & -32))
                    var2 = (var25 + 832)
                    i32_store(var5 + 2348, (var25 + 832))
                    break
                i32_store(var5 + 184, (var4 + (var9 << 2)))
            var25 = ((var0 + 31) & -32)
            i32_store(var5 + 2308, ((var0 + 31) & -32))
            var0 = (var25 + 832)
            i32_store(var5 + 2348, (var25 + 832))
            var2 = (var0 + ((var9 if (1 if var2 == 2 else 0) else 0) * 800))
            i32_store(var5 + 164, 0)
            var16 = (var9 << 3)
            i32_store(var5 + 2328, (var9 << 3))
            var15 = (var9 << 4)
            i32_store(var5 + 2324, (var9 << 4))
            i32_store(var5 + 188, var2)
            var4 = ((var8 + var25) + 832)
            var2 = i32_load8_u((var19 + 10321))
            var0 = (((var8 + var25) + 832) + (var15 * i32_load8_u((var19 + 10321))))
            i32_store(var5 + 2312, (((var8 + var25) + 832) + (var15 * i32_load8_u((var19 + 10321)))))
            var4 = (var4 + var11)
            i32_store(var5 + 2408, (0 if (1 if var41 == 0 else 0) else (var4 + var11)))
            var2 = (((var2 & 0xFFFFFFFF) >> 1) * var16)
            var0 = ((((var2 & 0xFFFFFFFF) >> 1) * var16) + (var0 + (var13 * var15)))
            i32_store(var5 + 2316, ((((var2 & 0xFFFFFFFF) >> 1) * var16) + (var0 + (var13 * var15))))
            i32_store(var5 + 2320, ((var0 + ((var12 * var16) << 3)) + var2))
            if (1 if (var4 + i32(var41)) > (var1 + var10) else 0):
                break
            # Unknown: memory.fill []
            i32_store16((i32_load(var5 + 2300) - 2), 0)
            i32_store(var5 + 2340, 0)
            i32_store(var5 + 2292, 0)
            # Unknown: memory.fill []
            break
            if (1 if func99(var5, 1, 8229) == 0 else 0):
                break
            i32_store(var22 + 8, 0)
            i32_store(var22 + 20, i32_load(var5 + 2312))
            i32_store(var22 + 24, i32_load(var5 + 2316))
            i32_store(var22 + 28, i32_load(var5 + 2320))
            i32_store(var22 + 32, i32_load(var5 + 2324))
            var0 = i32_load(var5 + 2328)
            i32_store(var22 + 104, 0)
            i32_store(var22 + 36, var0)
            if (1 if i32_load(52304) != i32_load(52308) else 0):
                i32_store(9687452, 294)
                i32_store(9687332, 295)
                i32_store(9687464, 296)
                i32_store(9687456, 297)
                i32_store(9687460, 298)
                i32_store(9687468, 299)
                i32_store(9687472, 300)
                i32_store(9687488, 301)
                i32_store(9687476, 302)
                i32_store(9687480, 303)
                i32_store(9687496, 304)
                i32_store(9687504, 305)
                i32_store(9687508, 306)
                i32_store(9687512, 307)
                i32_store(9687516, 308)
                i32_store(9687492, 309)
                i32_store(9687484, 310)
                i32_store(9687500, 311)
                i32_store(9687400, 312)
                i32_store(9687392, 313)
                i32_store(9687384, 314)
                i32_store(9687380, 315)
                i32_store(9687376, 316)
                i32_store(9687412, 317)
                i32_store(9687408, 318)
                i32_store(9687404, 319)
                i32_store(9687396, 320)
                i32_store(9687388, 321)
                i32_store(9687368, 322)
                i32_store(9687364, 323)
                i32_store(9687360, 324)
                i32_store(9687356, 325)
                i32_store(9687352, 326)
                i32_store(9687348, 327)
                i32_store(9687344, 328)
                i32_store(9687448, 329)
                i32_store(9687444, 330)
                i32_store(9687440, 331)
                i32_store(9687436, 332)
                i32_store(9687432, 333)
                i32_store(9687428, 334)
                i32_store(9687424, 335)
                i32_store(9687520, 336)
                i32_store(52308, i32_load(52304))
            var1 = 1
            break
            a_c()
            raise RuntimeError('unreachable')
            if (1 if 2020 == 0 else 0):
                break
            i32_store(var5 + 2344, 0)
            if (1 if i32_load(var5 + 320) > 0 else 0):
                var6 = (var5 + 16)
                while True:  # loop $label139
                    var15 = i32_load(var5 + 324)
                    var17 = 0
                    if (1 if i32_load(var5 + 300) > 0 else 0):
                        var16 = (var5 + 2292)
                        while True:  # loop $label128
                            var13 = i32_load(var5 + 2288)
                            var7 = i32_load(var5 + 2348)
                            if (1 if i32_load(var5 + 120) == 0 else 0):
                                break
                            var1 = i32_load(var6 + 8)
                            var0 = i32_load8_u(var5 + 948)
                            var2 = i32_load(var6 + 12)
                            if (1 if i32_load(var6 + 12) >= 0 else 0):
                                break
                            var4 = i32_load(var6 + 16)
                            if (1 if i32_load(var6 + 16) == 0 else 0):
                                break
                            if (1 if i32_load(var6 + 24) > var4 else 0):
                                var40 = i64_load(var4)
                                i32_store(var6 + 16, (var4 + 7))
                                i64_store(var6, ((i64_load(var6) << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                var2 = (var2 + 56)
                                break
                            func36(var6)
                            var2 = i32_load(var6 + 12)
                            var11 = (((var0 * var1) & 0xFFFFFFFF) >> 8)
                            var41 = i64_load(var6)
                            var40 = i64_extend_u(var2)
                            var4 = i32(((i64_load(var6) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2)))
                            if (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) < i32(((i64_load(var6) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0):
                                var41 = (var41 - (i64_extend_u((var11 + 1)) << var40))
                                i64_store(var6, (var41 - (i64_extend_u((var11 + 1)) << var40)))
                                break
                            var1 = (var11 + 1)
                            var0 = (clz32((var11 + 1)) ^ 24)
                            var2 = ((var1 - var11) - (clz32((var11 + 1)) ^ 24))
                            i32_store(var2 + 12, ((var1 - var11) - (clz32((var11 + 1)) ^ 24)))
                            var8 = ((var1 << var0) - 1)
                            i32_store(var6 + 8, ((var1 << var0) - 1))
                            if (1 if var4 <= var11 else 0):
                                var0 = i32_load8_u(var5 + 949)
                                if (1 if var2 >= 0 else 0):
                                    break
                                var1 = i32_load(var6 + 16)
                                if (1 if i32_load(var6 + 16) == 0 else 0):
                                    break
                                if (1 if i32_load(var6 + 24) > var1 else 0):
                                    var40 = i64_load(var1)
                                    i32_store(var6 + 16, (var1 + 7))
                                    var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                    i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                    var2 = (var2 + 56)
                                    break
                                func36(var6)
                                var41 = i64_load(var6)
                                var2 = i32_load(var6 + 12)
                                var4 = (((var0 * var8) & 0xFFFFFFFF) >> 8)
                                var40 = i64_extend_u(var2)
                                var2 = i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2)))
                                if (1 if (((var0 * var8) & 0xFFFFFFFF) >> 8) < i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0):
                                    i64_store(var6, (var41 - (i64_extend_u((var4 + 1)) << var40)))
                                    break
                                var1 = (var4 + 1)
                                var0 = (clz32((var4 + 1)) ^ 24)
                                i32_store(var2 + 12, ((var8 - var4) - (clz32((var4 + 1)) ^ 24)))
                                i32_store(var6 + 8, ((var1 << var0) - 1))
                                break
                            var0 = i32_load8_u(var5 + 950)
                            if (1 if var2 >= 0 else 0):
                                break
                            var1 = i32_load(var6 + 16)
                            if (1 if i32_load(var6 + 16) == 0 else 0):
                                break
                            if (1 if i32_load(var6 + 24) > var1 else 0):
                                var40 = i64_load(var1)
                                i32_store(var6 + 16, (var1 + 7))
                                var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                var2 = (var2 + 56)
                                break
                            func36(var6)
                            var41 = i64_load(var6)
                            var2 = i32_load(var6 + 12)
                            var4 = (((var0 * var8) & 0xFFFFFFFF) >> 8)
                            var40 = i64_extend_u(var2)
                            var2 = i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2)))
                            if (1 if (((var0 * var8) & 0xFFFFFFFF) >> 8) < i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0):
                                i64_store(var6, (var41 - (i64_extend_u((var4 + 1)) << var40)))
                                break
                            var1 = (var4 + 1)
                            var0 = (clz32((var4 + 1)) ^ 24)
                            i32_store(var2 + 12, ((var8 - var4) - (clz32((var4 + 1)) ^ 24)))
                            i32_store(var6 + 8, ((var1 << var0) - 1))
                            var0 = ((1 if var2 > var4 else 0) | 2)
                            var9 = (var7 + (var17 * 800))
                            i32_store8((var7 + (var17 * 800)) + 798, var0)
                            if (1 if i32_load(var5 + 2280) == 0 else 0):
                                var2 = i32_load(var6 + 12)
                                var10 = i32_load(var6 + 8)
                                break
                            var1 = i32_load(var6 + 8)
                            var0 = i32_load8_u(var5 + 2284)
                            var2 = i32_load(var6 + 12)
                            if (1 if i32_load(var6 + 12) >= 0 else 0):
                                break
                            var4 = i32_load(var6 + 16)
                            if (1 if i32_load(var6 + 16) == 0 else 0):
                                break
                            if (1 if i32_load(var6 + 24) > var4 else 0):
                                var40 = i64_load(var4)
                                i32_store(var6 + 16, (var4 + 7))
                                i64_store(var6, ((i64_load(var6) << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                var2 = (var2 + 56)
                                break
                            func36(var6)
                            var2 = i32_load(var6 + 12)
                            var7 = (((var0 * var1) & 0xFFFFFFFF) >> 8)
                            var41 = i64_load(var6)
                            var40 = i64_extend_u(var2)
                            var4 = i32(((i64_load(var6) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2)))
                            if (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) < i32(((i64_load(var6) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0):
                                i64_store(var6, (var41 - (i64_extend_u((var7 + 1)) << var40)))
                                break
                            var1 = (var7 + 1)
                            var0 = (clz32((var7 + 1)) ^ 24)
                            var2 = ((var1 - var7) - (clz32((var7 + 1)) ^ 24))
                            i32_store(var2 + 12, ((var1 - var7) - (clz32((var7 + 1)) ^ 24)))
                            var10 = ((var1 << var0) - 1)
                            i32_store(var6 + 8, ((var1 << var0) - 1))
                            i32_store8(var9 + 797, (1 if var4 > var7 else 0))
                            if (1 if var2 >= 0 else 0):
                                break
                            var0 = i32_load(var6 + 16)
                            if (1 if i32_load(var6 + 16) == 0 else 0):
                                break
                            if (1 if i32_load(var6 + 24) > var0 else 0):
                                var40 = i64_load(var0)
                                i32_store(var6 + 16, (var0 + 7))
                                i64_store(var6, ((i64_load(var6) << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                var2 = (var2 + 56)
                                break
                            func36(var6)
                            var2 = i32_load(var6 + 12)
                            var8 = ((var17 << 2) + var13)
                            var0 = (((var10 * 145) & 0xFFFFFFFF) >> 8)
                            var41 = i64_load(var6)
                            var40 = i64_extend_u(var2)
                            var4 = (1 if (((var10 * 145) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var6) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0)
                            if (1 if (1 if (((var10 * 145) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var6) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0) == 0 else 0):
                                i64_store(var6, (var41 - (i64_extend_u((var0 + 1)) << var40)))
                                break
                            var1 = (var0 + 1)
                            var0 = (clz32((var0 + 1)) ^ 24)
                            var2 = ((var10 - var0) - (clz32((var0 + 1)) ^ 24))
                            i32_store(var2 + 12, ((var10 - var0) - (clz32((var0 + 1)) ^ 24)))
                            var0 = ((var1 << var0) - 1)
                            i32_store(var6 + 8, ((var1 << var0) - 1))
                            i32_store8(var9 + 768, var4)
                            if (1 if var4 == 0 else 0):
                                if (1 if var2 >= 0 else 0):
                                    break
                                var1 = i32_load(var6 + 16)
                                if (1 if i32_load(var6 + 16) == 0 else 0):
                                    break
                                if (1 if i32_load(var6 + 24) > var1 else 0):
                                    var40 = i64_load(var1)
                                    i32_store(var6 + 16, (var1 + 7))
                                    i64_store(var6, ((i64_load(var6) << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                    var2 = (var2 + 56)
                                    break
                                func36(var6)
                                var2 = i32_load(var6 + 12)
                                var1 = (((var0 * 156) & 0xFFFFFFFF) >> 8)
                                var41 = i64_load(var6)
                                var40 = i64_extend_u(var2)
                                var4 = (1 if (((var0 * 156) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var6) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0)
                                if (1 if (1 if (((var0 * 156) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var6) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0) == 0 else 0):
                                    var41 = (var41 - (i64_extend_u((var1 + 1)) << var40))
                                    i64_store(var6, (var41 - (i64_extend_u((var1 + 1)) << var40)))
                                    break
                                var1 = (var1 + 1)
                                var0 = (clz32((var1 + 1)) ^ 24)
                                var2 = ((var0 - var1) - (clz32((var1 + 1)) ^ 24))
                                i32_store(var2 + 12, ((var0 - var1) - (clz32((var1 + 1)) ^ 24)))
                                var1 = ((var1 << var0) - 1)
                                i32_store(var6 + 8, ((var1 << var0) - 1))
                                if (1 if var4 == 0 else 0):
                                    if (1 if var2 >= 0 else 0):
                                        break
                                    var0 = i32_load(var6 + 16)
                                    if (1 if i32_load(var6 + 16) == 0 else 0):
                                        break
                                    if (1 if i32_load(var6 + 24) > var0 else 0):
                                        var40 = i64_load(var0)
                                        i32_store(var6 + 16, (var0 + 7))
                                        var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                        i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                        var2 = (var2 + 56)
                                        break
                                    func36(var6)
                                    var41 = i64_load(var6)
                                    var2 = i32_load(var6 + 12)
                                    var0 = (((var1 & 0xFFFFFFFF) >> 1) & 16777215)
                                    var40 = i64_extend_u(var2)
                                    if (1 if (((var1 & 0xFFFFFFFF) >> 1) & 16777215) < i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0):
                                        var19 = 1
                                        i64_store(var6, (var41 - (i64_extend_u((var0 + 1)) << var40)))
                                        break
                                    var19 = 3
                                    var1 = (var0 + 1)
                                    var0 = (clz32((var0 + 1)) ^ 24)
                                    var2 = ((var1 - var0) - (clz32((var0 + 1)) ^ 24))
                                    break
                                if (1 if var2 >= 0 else 0):
                                    break
                                var0 = i32_load(var6 + 16)
                                if (1 if i32_load(var6 + 16) == 0 else 0):
                                    break
                                if (1 if i32_load(var6 + 24) > var0 else 0):
                                    var40 = i64_load(var0)
                                    i32_store(var6 + 16, (var0 + 7))
                                    var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                    i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                    var2 = (var2 + 56)
                                    break
                                func36(var6)
                                var41 = i64_load(var6)
                                var2 = i32_load(var6 + 12)
                                var0 = (((var1 * 163) & 0xFFFFFFFF) >> 8)
                                var40 = i64_extend_u(var2)
                                if (1 if (((var1 * 163) & 0xFFFFFFFF) >> 8) < i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0):
                                    i64_store(var6, (var41 - (i64_extend_u((var0 + 1)) << var40)))
                                    var19 = 2
                                    break
                                var19 = 0
                                var1 = (var0 + 1)
                                var0 = (clz32((var0 + 1)) ^ 24)
                                var2 = ((var1 - var0) - (clz32((var0 + 1)) ^ 24))
                                var0 = (var1 << var0)
                                i32_store(var6 + 12, var2)
                                i32_store(var6 + 8, (var0 - 1))
                                i32_store8(var9 + 769, var19)
                                var0 = (var19 * 16843009)
                                i32_store(var8, (var19 * 16843009))
                                i32_store(var16, var0)
                                break
                            var20 = (var9 + 769)
                            var25 = 0
                            while True:  # loop $label120
                                var13 = (var16 + var25)
                                var2 = i32_load8_u((var16 + var25))
                                var19 = 0
                                while True:  # loop $label119
                                    var7 = (var8 + var19)
                                    var27 = (((i32_load8_u((var8 + var19)) * 90) + (var2 * 9)) + 12864)
                                    var0 = i32_load8_u((((i32_load8_u((var8 + var19)) * 90) + (var2 * 9)) + 12864))
                                    var1 = i32_load(var6 + 8)
                                    var2 = i32_load(var6 + 12)
                                    if (1 if i32_load(var6 + 12) >= 0 else 0):
                                        break
                                    var4 = i32_load(var6 + 16)
                                    if (1 if i32_load(var6 + 16) == 0 else 0):
                                        break
                                    if (1 if i32_load(var6 + 24) > var4 else 0):
                                        var40 = i64_load(var4)
                                        i32_store(var6 + 16, (var4 + 7))
                                        i64_store(var6, ((i64_load(var6) << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                        var2 = (var2 + 56)
                                        break
                                    func36(var6)
                                    var2 = i32_load(var6 + 12)
                                    var0 = (((var0 * var1) & 0xFFFFFFFF) >> 8)
                                    var41 = i64_load(var6)
                                    var40 = i64_extend_u(var2)
                                    var4 = (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var6) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0)
                                    if (1 if (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var6) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0) == 0 else 0):
                                        var41 = (var41 - (i64_extend_u((var0 + 1)) << var40))
                                        i64_store(var6, (var41 - (i64_extend_u((var0 + 1)) << var40)))
                                        break
                                    var1 = (var0 + 1)
                                    var0 = (clz32((var0 + 1)) ^ 24)
                                    var12 = ((var1 - var0) - (clz32((var0 + 1)) ^ 24))
                                    i32_store(var2 + 12, ((var1 - var0) - (clz32((var0 + 1)) ^ 24)))
                                    var1 = ((var1 << var0) - 1)
                                    i32_store(var6 + 8, ((var1 << var0) - 1))
                                    var2 = 0
                                    if var4:
                                        break
                                    var0 = i32_load8_u(var27 + 1)
                                    if (1 if var12 >= 0 else 0):
                                        break
                                    var2 = i32_load(var6 + 16)
                                    if (1 if i32_load(var6 + 16) == 0 else 0):
                                        break
                                    if (1 if i32_load(var6 + 24) > var2 else 0):
                                        var40 = i64_load(var2)
                                        i32_store(var6 + 16, (var2 + 7))
                                        var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                        i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                        var12 = (var12 + 56)
                                        break
                                    func36(var6)
                                    var41 = i64_load(var6)
                                    var12 = i32_load(var6 + 12)
                                    var0 = (((var0 * var1) & 0xFFFFFFFF) >> 8)
                                    var40 = i64_extend_u(var12)
                                    var4 = (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) >= i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var12))) else 0)
                                    if (1 if (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) >= i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var12))) else 0) == 0 else 0):
                                        var41 = (var41 - (i64_extend_u((var0 + 1)) << var40))
                                        i64_store(var6, (var41 - (i64_extend_u((var0 + 1)) << var40)))
                                        break
                                    var1 = (var0 + 1)
                                    var0 = (clz32((var0 + 1)) ^ 24)
                                    var10 = ((var1 - var0) - (clz32((var0 + 1)) ^ 24))
                                    i32_store(var12 + 12, ((var1 - var0) - (clz32((var0 + 1)) ^ 24)))
                                    var1 = ((var1 << var0) - 1)
                                    i32_store(var6 + 8, ((var1 << var0) - 1))
                                    var2 = 1
                                    if var4:
                                        break
                                    var0 = i32_load8_u(var27 + 2)
                                    if (1 if var10 >= 0 else 0):
                                        break
                                    var2 = i32_load(var6 + 16)
                                    if (1 if i32_load(var6 + 16) == 0 else 0):
                                        break
                                    if (1 if i32_load(var6 + 24) > var2 else 0):
                                        var40 = i64_load(var2)
                                        i32_store(var6 + 16, (var2 + 7))
                                        var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                        i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                        var10 = (var10 + 56)
                                        break
                                    func36(var6)
                                    var41 = i64_load(var6)
                                    var10 = i32_load(var6 + 12)
                                    var0 = (((var0 * var1) & 0xFFFFFFFF) >> 8)
                                    var40 = i64_extend_u(var10)
                                    var4 = (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) >= i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var10))) else 0)
                                    if (1 if (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) >= i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var10))) else 0) == 0 else 0):
                                        var41 = (var41 - (i64_extend_u((var0 + 1)) << var40))
                                        i64_store(var6, (var41 - (i64_extend_u((var0 + 1)) << var40)))
                                        break
                                    var1 = (var0 + 1)
                                    var0 = (clz32((var0 + 1)) ^ 24)
                                    var10 = ((var1 - var0) - (clz32((var0 + 1)) ^ 24))
                                    i32_store(var10 + 12, ((var1 - var0) - (clz32((var0 + 1)) ^ 24)))
                                    var1 = ((var1 << var0) - 1)
                                    i32_store(var6 + 8, ((var1 << var0) - 1))
                                    var2 = 2
                                    if var4:
                                        break
                                    var0 = i32_load8_u(var27 + 3)
                                    if (1 if var10 >= 0 else 0):
                                        break
                                    var2 = i32_load(var6 + 16)
                                    if (1 if i32_load(var6 + 16) == 0 else 0):
                                        break
                                    if (1 if i32_load(var6 + 24) > var2 else 0):
                                        var40 = i64_load(var2)
                                        i32_store(var6 + 16, (var2 + 7))
                                        var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                        i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                        var10 = (var10 + 56)
                                        break
                                    func36(var6)
                                    var41 = i64_load(var6)
                                    var10 = i32_load(var6 + 12)
                                    var21 = (((var0 * var1) & 0xFFFFFFFF) >> 8)
                                    var40 = i64_extend_u(var10)
                                    var4 = i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var10)))
                                    if (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) < i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var10))) else 0):
                                        var41 = (var41 - (i64_extend_u((var21 + 1)) << var40))
                                        i64_store(var6, (var41 - (i64_extend_u((var21 + 1)) << var40)))
                                        break
                                    var1 = (var21 + 1)
                                    var0 = (clz32((var21 + 1)) ^ 24)
                                    var2 = ((var1 - var21) - (clz32((var21 + 1)) ^ 24))
                                    i32_store(var10 + 12, ((var1 - var21) - (clz32((var21 + 1)) ^ 24)))
                                    var11 = ((var1 << var0) - 1)
                                    i32_store(var6 + 8, ((var1 << var0) - 1))
                                    if (1 if var4 <= var21 else 0):
                                        var0 = i32_load8_u(var27 + 4)
                                        if (1 if var2 >= 0 else 0):
                                            break
                                        var1 = i32_load(var6 + 16)
                                        if (1 if i32_load(var6 + 16) == 0 else 0):
                                            break
                                        if (1 if i32_load(var6 + 24) > var1 else 0):
                                            var40 = i64_load(var1)
                                            i32_store(var6 + 16, (var1 + 7))
                                            var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                            i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                            var2 = (var2 + 56)
                                            break
                                        func36(var6)
                                        var41 = i64_load(var6)
                                        var2 = i32_load(var6 + 12)
                                        var0 = (((var0 * var11) & 0xFFFFFFFF) >> 8)
                                        var40 = i64_extend_u(var2)
                                        var4 = (1 if (((var0 * var11) & 0xFFFFFFFF) >> 8) >= i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0)
                                        if (1 if (1 if (((var0 * var11) & 0xFFFFFFFF) >> 8) >= i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0) == 0 else 0):
                                            var41 = (var41 - (i64_extend_u((var0 + 1)) << var40))
                                            i64_store(var6, (var41 - (i64_extend_u((var0 + 1)) << var40)))
                                            break
                                        var1 = (var0 + 1)
                                        var0 = (clz32((var0 + 1)) ^ 24)
                                        var12 = ((var11 - var0) - (clz32((var0 + 1)) ^ 24))
                                        i32_store(var2 + 12, ((var11 - var0) - (clz32((var0 + 1)) ^ 24)))
                                        var1 = ((var1 << var0) - 1)
                                        i32_store(var6 + 8, ((var1 << var0) - 1))
                                        var2 = 3
                                        if var4:
                                            break
                                        var0 = i32_load8_u(var27 + 5)
                                        if (1 if var12 >= 0 else 0):
                                            break
                                        var2 = i32_load(var6 + 16)
                                        if (1 if i32_load(var6 + 16) == 0 else 0):
                                            break
                                        if (1 if i32_load(var6 + 24) > var2 else 0):
                                            var40 = i64_load(var2)
                                            i32_store(var6 + 16, (var2 + 7))
                                            var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                            i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                            var12 = (var12 + 56)
                                            break
                                        func36(var6)
                                        var41 = i64_load(var6)
                                        var12 = i32_load(var6 + 12)
                                        var0 = (((var0 * var1) & 0xFFFFFFFF) >> 8)
                                        var40 = i64_extend_u(var12)
                                        if (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) < i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var12))) else 0):
                                            i64_store(var6, (var41 - (i64_extend_u((var0 + 1)) << var40)))
                                            var10 = (var1 - var0)
                                            break
                                        var10 = (var0 + 1)
                                        var2 = 4
                                        var0 = (clz32(var10) ^ 24)
                                        var12 = (var12 - (clz32(var10) ^ 24))
                                        break
                                    var0 = i32_load8_u(var27 + 6)
                                    if (1 if var2 >= 0 else 0):
                                        break
                                    var1 = i32_load(var6 + 16)
                                    if (1 if i32_load(var6 + 16) == 0 else 0):
                                        break
                                    if (1 if i32_load(var6 + 24) > var1 else 0):
                                        var40 = i64_load(var1)
                                        i32_store(var6 + 16, (var1 + 7))
                                        var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                        i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                        var2 = (var2 + 56)
                                        break
                                    func36(var6)
                                    var41 = i64_load(var6)
                                    var2 = i32_load(var6 + 12)
                                    var0 = (((var0 * var11) & 0xFFFFFFFF) >> 8)
                                    var40 = i64_extend_u(var2)
                                    var4 = (1 if (((var0 * var11) & 0xFFFFFFFF) >> 8) >= i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0)
                                    if (1 if (1 if (((var0 * var11) & 0xFFFFFFFF) >> 8) >= i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0) == 0 else 0):
                                        var41 = (var41 - (i64_extend_u((var0 + 1)) << var40))
                                        i64_store(var6, (var41 - (i64_extend_u((var0 + 1)) << var40)))
                                        break
                                    var1 = (var0 + 1)
                                    var0 = (clz32((var0 + 1)) ^ 24)
                                    var12 = ((var11 - var0) - (clz32((var0 + 1)) ^ 24))
                                    i32_store(var2 + 12, ((var11 - var0) - (clz32((var0 + 1)) ^ 24)))
                                    var1 = ((var1 << var0) - 1)
                                    i32_store(var6 + 8, ((var1 << var0) - 1))
                                    var2 = 6
                                    if var4:
                                        break
                                    var0 = i32_load8_u(var27 + 7)
                                    if (1 if var12 >= 0 else 0):
                                        break
                                    var2 = i32_load(var6 + 16)
                                    if (1 if i32_load(var6 + 16) == 0 else 0):
                                        break
                                    if (1 if i32_load(var6 + 24) > var2 else 0):
                                        var40 = i64_load(var2)
                                        i32_store(var6 + 16, (var2 + 7))
                                        var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                        i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                        var12 = (var12 + 56)
                                        break
                                    func36(var6)
                                    var41 = i64_load(var6)
                                    var12 = i32_load(var6 + 12)
                                    var0 = (((var0 * var1) & 0xFFFFFFFF) >> 8)
                                    var40 = i64_extend_u(var12)
                                    var4 = (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) >= i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var12))) else 0)
                                    if (1 if (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) >= i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var12))) else 0) == 0 else 0):
                                        var41 = (var41 - (i64_extend_u((var0 + 1)) << var40))
                                        i64_store(var6, (var41 - (i64_extend_u((var0 + 1)) << var40)))
                                        break
                                    var1 = (var0 + 1)
                                    var0 = (clz32((var0 + 1)) ^ 24)
                                    var10 = ((var1 - var0) - (clz32((var0 + 1)) ^ 24))
                                    i32_store(var12 + 12, ((var1 - var0) - (clz32((var0 + 1)) ^ 24)))
                                    var1 = ((var1 << var0) - 1)
                                    i32_store(var6 + 8, ((var1 << var0) - 1))
                                    var2 = 7
                                    if var4:
                                        break
                                    var0 = i32_load8_u(var27 + 8)
                                    if (1 if var10 >= 0 else 0):
                                        break
                                    var2 = i32_load(var6 + 16)
                                    if (1 if i32_load(var6 + 16) == 0 else 0):
                                        break
                                    if (1 if i32_load(var6 + 24) > var2 else 0):
                                        var40 = i64_load(var2)
                                        i32_store(var6 + 16, (var2 + 7))
                                        var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                        i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                        var10 = (var10 + 56)
                                        break
                                    func36(var6)
                                    var41 = i64_load(var6)
                                    var10 = i32_load(var6 + 12)
                                    var0 = (((var0 * var1) & 0xFFFFFFFF) >> 8)
                                    var40 = i64_extend_u(var10)
                                    if (1 if (((var0 * var1) & 0xFFFFFFFF) >> 8) < i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var10))) else 0):
                                        i64_store(var6, (var41 - (i64_extend_u((var0 + 1)) << var40)))
                                        var0 = (var1 - var0)
                                        break
                                    var0 = (var0 + 1)
                                    var2 = 8
                                    var1 = (clz32(var0) ^ 24)
                                    var12 = (var10 - (clz32(var0) ^ 24))
                                    var0 = (var0 << var1)
                                    i32_store(var6 + 12, var12)
                                    i32_store(var6 + 8, (var0 - 1))
                                    i32_store8(var7, var2)
                                    var19 = (var19 + 1)
                                    if (1 if (var19 + 1) != 4 else 0):
                                        continue
                                    break  # end loop
                                i32_store(var20, i32_load(var8))
                                i32_store8(var13, var2)
                                var20 = (var20 + 4)
                                var25 = (var25 + 1)
                                if (1 if (var25 + 1) != 4 else 0):
                                    continue
                                break  # end loop
                            var0 = i32_load(var6 + 8)
                            var2 = i32_load(var6 + 12)
                            if (1 if i32_load(var6 + 12) >= 0 else 0):
                                break
                            var1 = i32_load(var6 + 16)
                            if (1 if i32_load(var6 + 16) == 0 else 0):
                                break
                            if (1 if i32_load(var6 + 24) > var1 else 0):
                                var40 = i64_load(var1)
                                i32_store(var6 + 16, (var1 + 7))
                                i64_store(var6, ((i64_load(var6) << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                var2 = (var2 + 56)
                                break
                            func36(var6)
                            var2 = i32_load(var6 + 12)
                            var1 = (((var0 * 142) & 0xFFFFFFFF) >> 8)
                            var41 = i64_load(var6)
                            var40 = i64_extend_u(var2)
                            var4 = (1 if (((var0 * 142) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var6) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0)
                            if (1 if (1 if (((var0 * 142) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var6) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0) == 0 else 0):
                                var41 = (var41 - (i64_extend_u((var1 + 1)) << var40))
                                i64_store(var6, (var41 - (i64_extend_u((var1 + 1)) << var40)))
                                break
                            var1 = (var1 + 1)
                            var0 = (clz32((var1 + 1)) ^ 24)
                            var2 = ((var0 - var1) - (clz32((var1 + 1)) ^ 24))
                            i32_store(var2 + 12, ((var0 - var1) - (clz32((var1 + 1)) ^ 24)))
                            var0 = ((var1 << var0) - 1)
                            i32_store(var6 + 8, ((var1 << var0) - 1))
                            var19 = 0
                            if var4:
                                break
                            if (1 if var2 >= 0 else 0):
                                break
                            var1 = i32_load(var6 + 16)
                            if (1 if i32_load(var6 + 16) == 0 else 0):
                                break
                            if (1 if i32_load(var6 + 24) > var1 else 0):
                                var40 = i64_load(var1)
                                i32_store(var6 + 16, (var1 + 7))
                                var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                var2 = (var2 + 56)
                                break
                            func36(var6)
                            var41 = i64_load(var6)
                            var2 = i32_load(var6 + 12)
                            var1 = (((var0 * 114) & 0xFFFFFFFF) >> 8)
                            var40 = i64_extend_u(var2)
                            var4 = (1 if (((var0 * 114) & 0xFFFFFFFF) >> 8) >= i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0)
                            if (1 if (1 if (((var0 * 114) & 0xFFFFFFFF) >> 8) >= i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0) == 0 else 0):
                                var41 = (var41 - (i64_extend_u((var1 + 1)) << var40))
                                i64_store(var6, (var41 - (i64_extend_u((var1 + 1)) << var40)))
                                break
                            var1 = (var1 + 1)
                            var0 = (clz32((var1 + 1)) ^ 24)
                            var2 = ((var0 - var1) - (clz32((var1 + 1)) ^ 24))
                            i32_store(var2 + 12, ((var0 - var1) - (clz32((var1 + 1)) ^ 24)))
                            var0 = ((var1 << var0) - 1)
                            i32_store(var6 + 8, ((var1 << var0) - 1))
                            var19 = 2
                            if var4:
                                break
                            if (1 if var2 >= 0 else 0):
                                break
                            var1 = i32_load(var6 + 16)
                            if (1 if i32_load(var6 + 16) == 0 else 0):
                                break
                            if (1 if i32_load(var6 + 24) > var1 else 0):
                                var40 = i64_load(var1)
                                i32_store(var6 + 16, (var1 + 7))
                                var41 = ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                i64_store(var6, ((var41 << 56) | ((((((var40 << 56) | ((var40 & 65280) << 40)) | (((var40 & 16711680) << 24) | ((var40 & 4278190080) << 8))) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                var2 = (var2 + 56)
                                break
                            func36(var6)
                            var41 = i64_load(var6)
                            var2 = i32_load(var6 + 12)
                            var1 = (((var0 * 183) & 0xFFFFFFFF) >> 8)
                            var40 = i64_extend_u(var2)
                            if (1 if (((var0 * 183) & 0xFFFFFFFF) >> 8) < i32(((var41 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0):
                                var19 = 1
                                i64_store(var6, (var41 - (i64_extend_u((var1 + 1)) << var40)))
                                break
                            var19 = 3
                            var1 = (var1 + 1)
                            var0 = (clz32((var1 + 1)) ^ 24)
                            i32_store(var2 + 12, ((var0 - var1) - (clz32((var1 + 1)) ^ 24)))
                            i32_store(var6 + 8, ((var1 << var0) - 1))
                            i32_store8(var9 + 785, var19)
                            var17 = (var17 + 1)
                            if (1 if (var17 + 1) < i32_load(var5 + 300) else 0):
                                continue
                            break  # end loop
                    break
                    a_c()
                    raise RuntimeError('unreachable')
                    if (1 if 3339 == 0 else 0):
                        break
                    if (1 if i32_load(var5 + 2340) < i32_load(var5 + 300) else 0):
                        var24 = ((var5 + ((var15 & var18) << 5)) + 328)
                        while True:  # loop $label135
                            var10 = 0
                            var25 = 0
                            var8 = 0
                            var28 = (global0 - 32)
                            global global0
                            global0 = (global0 - 32)
                            var2 = i32_load(var5 + 2300)
                            var32 = (i32_load(var5 + 2300) - 2)
                            var30 = i32_load(var5 + 2340)
                            var33 = (var2 + (i32_load(var5 + 2340) << 1))
                            var34 = i32_load(var5 + 2348)
                            if i32_load(var5 + 2280):
                                var0 = (var34 + (var30 * 800))
                                if i32_load8_u((var34 + (var30 * 800)) + 797):
                                    break
                            var0 = (var34 + (var30 * 800))
                            var16 = i32_load8_u((var34 + (var30 * 800)) + 798)
                            # Unknown: memory.fill []
                            var7 = (var5 + (var16 << 5))
                            if (1 if i32_load8_u(var0 + 768) == 0 else 0):
                                var18 = (var5 + 2008)
                                i64_store(var28 + 24, 0)
                                i64_store(var28 + 16, 0)
                                i64_store(var28 + 8, 0)
                                i64_store(var28, 0)
                                var10 = 1
                                var1 = (var2 - 1)
                                var4 = (var2 + (var30 << 1))
                                # call_indirect via table[i32_load(9687280)]
                                var2 = call_indirect(i32_load(9687280))
                                var1 = (1 if call_indirect(i32_load(9687280)) > 0 else 0)
                                i32_store8(var28, (1 if call_indirect(i32_load(9687280)) > 0 else 0))
                                i32_store8(var4 + 1, var1)
                                if (1 if var2 >= 2 else 0):
                                    # call_indirect via table[i32_load(9687332)]
                                    break
                                var1 = (((i32_load16_s(var28) + 3) & 0xFFFFFFFF) >> 3)
                                i32_store16(var0 + 480, (((i32_load16_s(var28) + 3) & 0xFFFFFFFF) >> 3))
                                i32_store16(var0 + 448, var1)
                                i32_store16(var0 + 416, var1)
                                i32_store16(var0 + 384, var1)
                                i32_store16(var0 + 352, var1)
                                i32_store16(var0 + 320, var1)
                                i32_store16(var0 + 288, var1)
                                i32_store16(var0 + 256, var1)
                                i32_store16(var0 + 224, var1)
                                i32_store16(var0 + 192, var1)
                                i32_store16(var0 + 160, var1)
                                i32_store16(var0 + 128, var1)
                                i32_store16(var0 + 96, var1)
                                i32_store16(var0 + 64, var1)
                                i32_store16(var0 + 32, var1)
                                i32_store16(var0, var1)
                                break
                            var18 = (var5 + 2212)
                            var9 = (var7 + 820)
                            var29 = (i32_load8_u(var32) & 15)
                            var35 = (i32_load8_u(var33) & 15)
                            while True:  # loop $label133
                                var1 = var0
                                # call_indirect via table[i32_load(9687280)]
                                var17 = call_indirect(i32_load(9687280))
                                var15 = i32_load16_u(var0)
                                var2 = (1 if var10 < var17 else 0)
                                var0 = ((var35 & 0xFFFFFFFF) >> 1)
                                # call_indirect via table[i32_load(9687280)]
                                var21 = call_indirect(i32_load(9687280))
                                var13 = i32_load16_u(var1 + 32)
                                var7 = (1 if var10 < var21 else 0)
                                var2 = ((((var0 & 126) | (var2 << 7)) & 0xFFFFFFFF) >> 1)
                                # call_indirect via table[i32_load(9687280)]
                                var11 = call_indirect(i32_load(9687280))
                                var0 = i32_load16_u(var1 + 64)
                                var4 = (1 if var10 < var11 else 0)
                                var2 = ((((var7 << 7) | var2) & 0xFFFFFFFF) >> 1)
                                # call_indirect via table[i32_load(9687280)]
                                var7 = call_indirect(i32_load(9687280))
                                var25 = ((((((3 if (1 if var21 > 3 else 0) else (2 if (1 if var21 >= 2 else 0) else (1 if var13 != 0 else 0))) | (12 if (1 if var17 > 3 else 0) else (8 if (1 if var17 >= 2 else 0) else ((1 if var15 != 0 else 0) << 2)))) << 4) | (12 if (1 if var11 > 3 else 0) else (8 if (1 if var11 >= 2 else 0) else ((1 if var0 != 0 else 0) << 2)))) | (3 if (1 if var7 > 3 else 0) else (2 if (1 if var7 >= 2 else 0) else (1 if i32_load16_u(var1 + 96) != 0 else 0)))) | (var25 << 8))
                                var0 = (1 if var7 > var10 else 0)
                                var35 = (((1 if var7 > var10 else 0) << 3) | ((((var4 << 7) | var2) & 0xFFFFFFFF) >> 5))
                                var29 = ((var0 << 7) | (((var29 & 254) & 0xFFFFFFFF) >> 1))
                                var0 = (var1 + 128)
                                var8 = (var8 + 1)
                                if (1 if (var8 + 1) != 4 else 0):
                                    continue
                                break  # end loop
                            var31 = (var5 + 2144)
                            var4 = i32_load8_u(var32)
                            var2 = i32_load8_u(var33)
                            var27 = (var5 + (var16 << 5))
                            var20 = ((var5 + (var16 << 5)) + 836)
                            # call_indirect via table[i32_load(9687280)]
                            var36 = call_indirect(i32_load(9687280))
                            var9 = i32_load16_u(var1 + 128)
                            var0 = (1 if var36 > 0 else 0)
                            # call_indirect via table[i32_load(9687280)]
                            var37 = call_indirect(i32_load(9687280))
                            var17 = i32_load16_u(var1 + 160)
                            # call_indirect via table[i32_load(9687280)]
                            var38 = call_indirect(i32_load(9687280))
                            var21 = i32_load16_u(var1 + 192)
                            var11 = (1 if var38 > 0 else 0)
                            var8 = (1 if var37 > 0 else 0)
                            # call_indirect via table[i32_load(9687280)]
                            var10 = call_indirect(i32_load(9687280))
                            var16 = i32_load16_u(var1 + 224)
                            var4 = i32_load8_u(var32)
                            var2 = i32_load8_u(var33)
                            # call_indirect via table[i32_load(9687280)]
                            var12 = call_indirect(i32_load(9687280))
                            var15 = i32_load16_u(var1 + 256)
                            var0 = (1 if var12 > 0 else 0)
                            # call_indirect via table[i32_load(9687280)]
                            var18 = call_indirect(i32_load(9687280))
                            var13 = i32_load16_u(var1 + 288)
                            # call_indirect via table[i32_load(9687280)]
                            var19 = call_indirect(i32_load(9687280))
                            var7 = i32_load16_u(var1 + 320)
                            var0 = (1 if var19 > 0 else 0)
                            var4 = (1 if var18 > 0 else 0)
                            # call_indirect via table[i32_load(9687280)]
                            var20 = call_indirect(i32_load(9687280))
                            var2 = i32_load16_u(var1 + 352)
                            var1 = ((1 if var20 > 0 else 0) << 7)
                            var0 = ((1 if var10 > 0 else 0) << 5)
                            i32_store8(var33, (((((1 if var20 > 0 else 0) << 7) | (var0 << 6)) | (((1 if var10 > 0 else 0) << 5) | (var11 << 4))) | var35))
                            i32_store8(var32, (((((var8 << 4) | ((var29 & 0xFFFFFFFF) >> 4)) | var0) | (var4 << 6)) | var1))
                            var1 = (var34 + (var30 * 800))
                            var0 = ((((((3 if (1 if var37 > 3 else 0) else (2 if (1 if var37 >= 2 else 0) else (1 if var17 != 0 else 0))) | (12 if (1 if var36 > 3 else 0) else (8 if (1 if var36 >= 2 else 0) else ((1 if var9 != 0 else 0) << 2)))) << 4) | (12 if (1 if var38 > 3 else 0) else (8 if (1 if var38 >= 2 else 0) else ((1 if var21 != 0 else 0) << 2)))) | (3 if (1 if var10 > 3 else 0) else (2 if (1 if var10 >= 2 else 0) else (1 if var16 != 0 else 0)))) | ((((((3 if (1 if var18 > 3 else 0) else (2 if (1 if var18 >= 2 else 0) else (1 if var13 != 0 else 0))) | (12 if (1 if var12 > 3 else 0) else (8 if (1 if var12 >= 2 else 0) else ((1 if var15 != 0 else 0) << 2)))) << 4) | (12 if (1 if var19 > 3 else 0) else (8 if (1 if var19 >= 2 else 0) else ((1 if var7 != 0 else 0) << 2)))) | (3 if (1 if var20 > 3 else 0) else (2 if (1 if var20 >= 2 else 0) else (1 if var2 != 0 else 0)))) << 8))
                            i32_store((var34 + (var30 * 800)) + 792, ((((((3 if (1 if var37 > 3 else 0) else (2 if (1 if var37 >= 2 else 0) else (1 if var17 != 0 else 0))) | (12 if (1 if var36 > 3 else 0) else (8 if (1 if var36 >= 2 else 0) else ((1 if var9 != 0 else 0) << 2)))) << 4) | (12 if (1 if var38 > 3 else 0) else (8 if (1 if var38 >= 2 else 0) else ((1 if var21 != 0 else 0) << 2)))) | (3 if (1 if var10 > 3 else 0) else (2 if (1 if var10 >= 2 else 0) else (1 if var16 != 0 else 0)))) | ((((((3 if (1 if var18 > 3 else 0) else (2 if (1 if var18 >= 2 else 0) else (1 if var13 != 0 else 0))) | (12 if (1 if var12 > 3 else 0) else (8 if (1 if var12 >= 2 else 0) else ((1 if var15 != 0 else 0) << 2)))) << 4) | (12 if (1 if var19 > 3 else 0) else (8 if (1 if var19 >= 2 else 0) else ((1 if var7 != 0 else 0) << 2)))) | (3 if (1 if var20 > 3 else 0) else (2 if (1 if var20 >= 2 else 0) else (1 if var2 != 0 else 0)))) << 8)))
                            i32_store(var1 + 788, var25)
                            if (var0 & 43690):
                            else:
                            i32_store8(0 + 796, i32_load(var27 + 848))
                            var10 = (1 if (var0 | var25) != 0 else 0)
                            break
                            i32_store8(var33, 0)
                            i32_store8(var32, 0)
                            if (1 if i32_load8_u(var0 + 768) == 0 else 0):
                                i32_store8((var2 + (var30 << 1)) + 1, 0)
                                i32_store8((var2 - 1), 0)
                            var0 = (var34 + (var30 * 800))
                            i64_store((var34 + (var30 * 800)) + 788, 0)
                            i32_store8(var0 + 796, 0)
                            if (1 if i32_load(var5 + 2352) > 0 else 0):
                                var1 = (i32_load(var5 + 2304) + (i32_load(var5 + 2340) << 2))
                                var0 = (var34 + (var30 * 800))
                                i32_store((i32_load(var5 + 2304) + (i32_load(var5 + 2340) << 2)), i32_load((((var5 + (i32_load8_u((var34 + (var30 * 800)) + 798) << 3)) + (i32_load8_u(var0 + 768) << 2)) + 2356)))
                                i32_store8(var1 + 2, (i32_load8_u(var1 + 2) | var10))
                            var0 = i32_load(var24 + 28)
                            global global0
                            global0 = (var28 + 32)
                            if var0:
                                var20 = 0
                                if i32_load(var5):
                                    break
                                i32_store(var5 + 8, 8324)
                                i64_store(var5, 7)
                                break
                            var0 = (i32_load(var5 + 2340) + 1)
                            i32_store(var5 + 2340, (i32_load(var5 + 2340) + 1))
                            if (1 if var0 < i32_load(var5 + 300) else 0):
                                continue
                            break  # end loop
                    i32_store16((i32_load(var5 + 2300) - 2), 0)
                    i32_store(var5 + 2340, 0)
                    i32_store(var5 + 2292, 0)
                    var0 = 0
                    if (1 if i32_load(var5 + 2352) <= 0 else 0):
                        break
                    var1 = i32_load(var5 + 2344)
                    if (1 if i32_load(var5 + 2344) < i32_load(var5 + 312) else 0):
                        break
                    var0 = (1 if var1 <= i32_load(var5 + 320) else 0)
                    var4 = (var5 + 172)
                    if (1 if i32_load(var5 + 160) == 0 else 0):
                        i32_store(var5 + 180, var0)
                        i32_store(var5 + 176, i32_load(var5 + 2344))
                        func273(var20, 0, (var1 + 352), var1, var5, var4)
                        break
                    var2 = (var5 + 136)
                    # call_indirect via table[i32_load(52348)]
                    var1 = call_indirect(i32_load(52348))
                    if (1 if i32_load(var5 + 140) == 1 else 0):
                        if (var1 & 1):
                            # Unknown: memory.copy []
                            i32_store(var5 + 180, var0)
                            i32_store(var5 + 172, i32_load(var5 + 164))
                            i32_store(var5 + 176, i32_load(var5 + 2344))
                            if (1 if i32_load(var5 + 160) == 2 else 0):
                                var1 = i32_load(var5 + 2348)
                                i32_store(var5 + 2348, i32_load(var5 + 188))
                                i32_store(var5 + 188, var1)
                                break
                            func273((var5 + 136), (var5 + 192), var22, 108, var5, var4)
                            if var0:
                                var0 = i32_load(var5 + 2304)
                                i32_store(var5 + 2304, i32_load(var5 + 184))
                                i32_store(var5 + 184, var0)
                            # call_indirect via table[i32_load(52352)]
                            var0 = (i32_load(var5 + 164) + 1)
                            i32_store(var5 + 164, ((i32_load(var5 + 164) + 1) if (1 if var0 != i32_load(var5 + 168) else 0) else 0))
                        else:
                        break
                    a_c()
                    raise RuntimeError('unreachable')
                    if (1 if 2263 == 0 else 0):
                        var20 = 0
                        if i32_load(var5):
                            break
                        i32_store(var5 + 8, 8308)
                        i64_store(var5, 6)
                        break
                    var18 = (i32_load(var5 + 2344) + 1)
                    i32_store(var5 + 2344, (i32_load(var5 + 2344) + 1))
                    if (1 if var18 < i32_load(var5 + 320) else 0):
                        continue
                    break  # end loop
            if (1 if i32_load(var5 + 160) <= 0 else 0):
                break
            # call_indirect via table[i32_load(52348)]
            if call_indirect(i32_load(52348)):
                break
            var20 = 0
            break
            var20 = 1
            break
            a_c()
            raise RuntimeError('unreachable')
            var20 = 0
            if i32_load(var5):
                break
            i32_store(var5 + 8, 8359)
            i64_store(var5, 7)
            var0 = 1
            if (1 if i32_load(var5 + 160) > 0 else 0):
                # call_indirect via table[i32_load(52348)]
                var0 = call_indirect(i32_load(52348))
            var1 = i32_load(var22 + 52)
            if i32_load(var22 + 52):
                # call_indirect via table[var1]
            if (var0 & var20):
                break
            # call_indirect via table[i32_load(52360)]
            func450(var5)
            i64_store(var5 + 16, 0)
            i64_store(var5 + 2332, 0)
            i64_store(var5 + 24, 0)
            i64_store(var5 + 32, 0)
            i64_store(var5 + 40, 0)
            var18 = 0
            i32_store(var39, 0)
            if var18:
                break
        var3 = i32_load(var5)
        if var5:
            # call_indirect via table[i32_load(52360)]
            func450(var5)
            i64_store(var5 + 16, 0)
            i64_store(var5 + 2332, 0)
            i64_store(var5 + 24, 0)
            i64_store(var5 + 32, 0)
            i64_store(var5 + 40, 0)
            i32_store(var5 + 4, 0)
        break
    var8 = func134(1, 288)
    if func134(1, 288):
        i64_store(var8, 8589934592)
        func453()
    if (1 if var8 == 0 else 0):
        break
    var3 = (var14 + 48)
    if (1 if var8 == 0 else 0):
        break
    if (1 if var3 == 0 else 0):
        # br_table ['$label144', '$label143', '$label143', '$label143', '$label143', '$label144', '$label143']
        _br_idx = i32_load(var8)
        break  # br_table
    i32_store(var8, 0)
    i32_store(var8 + 8, var3)
    var1 = (var8 + 24)
    if (1 if func39(var1, 8) != 47 else 0):
        break
    var2 = func39(var1, 14)
    var0 = func39(var1, 14)
    if func39(var1, 3):
        break
    if (1 if i32_load(var8 + 48) == 0 else 0):
        break
    # br_table ['$label147', '$label148', '$label148', '$label148', '$label148', '$label147', '$label148']
    _br_idx = i32_load(var8)
    break  # br_table
    i32_store(var8, 3)
    break
    i32_store(var8 + 4, 2)
    var1 = (var0 + 1)
    i32_store(var3 + 4, (var0 + 1))
    var0 = (var2 + 1)
    i32_store(var3, (var2 + 1))
    var10 = 1
    if func153(var0, var1, 1, var8, 0):
        break
    func191(var8)
    var10 = 0
    if i32_load(var8):
        break
    a_c()
    raise RuntimeError('unreachable')
    i32_store(var8, 2)
    if var10:
        var3 = func451(i32_load(var14 + 48), i32_load(var14 + 52), i32_load(var26 + 20), i32_load(var26))
        if func451(i32_load(var14 + 48), i32_load(var14 + 52), i32_load(var26 + 20), i32_load(var26)):
            break
        var3 = 0
        if (1 if var8 == 0 else 0):
            break
        if i32_load(var8 + 172):
            if (1 if i32_load(var8 + 168) == 0 else 0):
                break
            if (1 if i32_load(var8 + 164) <= 0 else 0):
                break
            var16 = i32_load(var8 + 8)
            if (1 if i32_load(var8 + 8) == 0 else 0):
                break
            var13 = i32_load(var16 + 40)
            if (1 if i32_load(var16 + 40) == 0 else 0):
                break
            if i32_load(var8 + 4):
                var0 = i32_load(var13)
                i32_store(var8 + 12, i32_load(var13))
                if (1 if var0 == 0 else 0):
                    break
                if (1 if func447(i32_load(var13 + 20), var16, 3) == 0 else 0):
                    var1 = 2
                    # br_table ['$label156', '$label157', '$label157', '$label157', '$label157', '$label156', '$label157']
                    _br_idx = i32_load(var8)
                    break  # br_table
                var0 = i32_load(var8 + 100)
                var1 = i32_load(var16)
                if (1 if i32_load(var8 + 100) > i32_load(var16) else 0):
                    break
                var40 = (i64_load32_s(var8 + 104) * i64_extend_s(var0))
                var0 = (var1 & 65535)
                var1 = func58(((i64_load32_s(var8 + 104) * i64_extend_s(var0)) + (i64_extend_u((var1 & 65535)) + (i64_extend_s(var1) << 4))), 4)
                i32_store(var8 + 16, func58(((i64_load32_s(var8 + 104) * i64_extend_s(var0)) + (i64_extend_u((var1 & 65535)) + (i64_extend_s(var1) << 4))), 4))
                if (1 if var1 == 0 else 0):
                    i32_store(var8 + 20, 0)
                    var1 = 1
                    # br_table ['$label156', '$label157', '$label157', '$label157', '$label157', '$label156', '$label157']
                    _br_idx = i32_load(var8)
                    break  # br_table
                i32_store(var8 + 20, ((var1 + (i32(var40) << 2)) + (var0 << 2)))
                if i32_load(var16 + 92):
                    var7 = i32_load(var16 + 100)
                    var4 = i32_load(var16 + 16)
                    var0 = i32_load(var16 + 12)
                    var1 = 1
                    var2 = i32_load(var16 + 96)
                    var41 = i64_extend_s(i32_load(var16 + 96))
                    var40 = (i64_extend_s(i32_load(var16 + 96)) << 5)
                    var15 = func58((((i64_extend_s(i32_load(var16 + 96)) << 5) + (var41 << 2)) + 84), 1)
                    if (1 if func58((((i64_extend_s(i32_load(var16 + 96)) << 5) + (var41 << 2)) + 84), 1) == 0 else 0):
                        # br_table ['$label156', '$label157', '$label157', '$label157', '$label157', '$label156', '$label157']
                        _br_idx = i32_load(var8)
                        break  # br_table
                    if i32_load(var8 + 280):
                        break
                    i32_store(var8 + 284, var15)
                    i32_store(var8 + 280, var15)
                    var0 = (var15 + 84)
                    if (1 if func90(var15, var0, var4, ((var15 + 84) + i32(var40)), var2, var7, 0, 4, var0) == 0 else 0):
                        break
                    if i32_load(var16 + 92):
                        break
                var1 = i32_load(i32_load(var8 + 12))
                if (1 if (i32_load(i32_load(var8 + 12)) - 11) < -4 else 0):
                    break
                func188()
                var1 = i32_load(i32_load(var8 + 12))
                if (1 if var1 < 11 else 0):
                    break
                var0 = i32_load(52304)
                if (1 if i32_load(52304) != i32_load(52336) else 0):
                    i32_store(9688020, 406)
                    i32_store(9688016, 407)
                    i32_store(9688004, 408)
                    i32_store(9688008, 409)
                    i32_store(9688012, 410)
                    i32_store(52336, var0)
                if (1 if i32_load(i32_load(var8 + 12) + 28) == 0 else 0):
                    break
                func188()
                if (1 if i32_load(var8 + 56) == 0 else 0):
                    break
                if (1 if i32_load(var8 + 120) <= 0 else 0):
                    break
                var0 = (var8 + 136)
                if i32_load((var8 + 136)):
                    break
                if func455(var0, i32_load(var8 + 132)):
                    break
                var1 = 1
                # br_table ['$label156', '$label157', '$label157', '$label157', '$label157', '$label156', '$label157']
                _br_idx = i32_load(var8)
                break  # br_table
                i32_store(var8 + 4, 0)
            if (1 if func275(var8, i32_load(var8 + 16), i32_load(var8 + 100), i32_load(var8 + 104), i32_load(var16 + 88), 278) == 0 else 0):
                break
            i32_store(var13 + 16, i32_load(var8 + 116))
            break
            i32_store(var8, var1)
            func191(var8)
            if (1 if i32_load(var8) == 0 else 0):
                break
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
        a_c()
        raise RuntimeError('unreachable')
        a_c()
        raise RuntimeError('unreachable')
        a_c()
        raise RuntimeError('unreachable')
        if 4800:
            break
    var3 = i32_load(var8)
    func190(var8)
    if var3:
        var0 = i32_load(var26)
        if i32_load(var26):
            if (1 if i32_load(var0 + 12) <= 0 else 0):
            i32_store(var0 + 80, 0)
        break
    var0 = i32_load(var26 + 20)
    if (1 if i32_load(var26 + 20) == 0 else 0):
        break
    if (1 if i32_load(var0 + 48) == 0 else 0):
        break
    var7 = i32_load(var26)
    if i32_load(var26):
        var4 = i32_load(var7 + 16)
        var2 = i32_load(var7 + 8)
        if (1 if i32_load(var7) <= 10 else 0):
            var0 = (var7 + 20)
            var10 = i32_load((var7 + 20))
            i32_store(var7 + 16, (var4 + (i32_load((var7 + 20)) * (var2 - 1))))
            break
        var0 = i32_load(var7 + 32)
        i32_store(var7 + 32, (0 - i32_load(var7 + 32)))
        var3 = i32_load(var7 + 36)
        i32_store(var7 + 36, (0 - i32_load(var7 + 36)))
        var1 = i32_load(var7 + 40)
        i32_store(var7 + 40, (0 - i32_load(var7 + 40)))
        var40 = (i64_extend_s(var2) - 1)
        var2 = i32((i64_extend_s(var2) - 1))
        i32_store(var7 + 16, (var4 + (var0 * i32((i64_extend_s(var2) - 1)))))
        var0 = i32(((var40 & 0xFFFFFFFFFFFFFFFF) >> 1))
        i32_store(var7 + 20, (i32_load(var7 + 20) + (var3 * i32(((var40 & 0xFFFFFFFFFFFFFFFF) >> 1)))))
        i32_store(var7 + 24, (i32_load(var7 + 24) + (var0 * var1)))
        var1 = i32_load(var7 + 28)
        if (1 if i32_load(var7 + 28) == 0 else 0):
            break
        var0 = (var7 + 44)
        var10 = i32_load((var7 + 44))
        i32_store(var7 + 28, (var1 + (i32_load((var7 + 44)) * var2)))
        i32_store(var0, (0 - var10))
    global global0
    global0 = (var14 + 160)
    break
    a_c()
    raise RuntimeError('unreachable')
    global global0
    global0 = (var23 + 144)
    return 3738

