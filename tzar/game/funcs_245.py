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
# $func421
# ==========================================================
def func421(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
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
    var30 = 0.0
    var31 = 0.0
    var32 = 0.0
    var33 = 0.0
    var34 = 0.0
    var35 = 0.0
    var36 = 0.0
    var37 = 0.0
    var15 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var4 = i32_load(9671128)
    var16 = (1 if var0 >= 0 else 0)
    var9 = (var0 if (1 if var0 >= 0 else 0) else (var0 - 2147483647))
    var6 = (i32_load(9671128) + ((var0 if (1 if var0 >= 0 else 0) else (var0 - 2147483647)) * 132))
    var5 = i32_load((i32_load(9671128) + ((var0 if (1 if var0 >= 0 else 0) else (var0 - 2147483647)) * 132)) + 44)
    var10 = i32_load(9215884)
    if (1 if var16 == 0 else 0):
        i32_store((var10 + ((var5 << 4) | 8)), var9)
    var11 = i32_load8_u(var6 + 129)
    if (1 if ((i32_load8_u(var6 + 129) - 11) & 255) <= 1 else 0):
        i32_store((var4 + (var1 * 132)) + 100, 0)
        func29(var6, 1)
        i32_store8(var6 + 129, (6 if (1 if var11 == 12 else 0) else 0))
        break
    var21 = (var4 + (var9 * 132))
    var16 = i32_load8_u((var4 + (var9 * 132)) + 122)
    var7 = ((i32_load8_u((var4 + (var9 * 132)) + 122) * 72) + 9263856)
    var25 = i32_load(((i32_load8_u((var4 + (var9 * 132)) + 122) * 72) + 9263856) + 8)
    if (1 if i32_load(((i32_load8_u((var4 + (var9 * 132)) + 122) * 72) + 9263856) + 8) == 0 else 0):
        var25 = i32_load(var7)
    var28 = (var4 + (var1 * 132))
    var7 = i32_load8_u((var4 + (var1 * 132)) + 122)
    var29 = i32_load((var10 + (var5 << 4)) + 12)
    var5 = i32_load8_u(var28 + 125)
    var10 = i32_load(38564)
    if (1 if i32_load(9142848) >= (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        break
    if (1 if var7 == var10 else 0):
        break
    # br_table ['$label2', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label2', '$label3']
    _br_idx = (var5 - 4)
    break  # br_table
    if (1 if i32_load((var4 + (var9 * 132)) + 56) == 1 else 0):
        if (1 if i32_load(((var16 * 404) + 9568096) + 268) == 1 else 0):
            break
    func29(var6, 1)
    break
    var2 = (1 if var5 == 3 else 0)
    if (1 if var5 != 3 else 0):
        break
    if (1 if var7 != var10 else 0):
        break
    var0 = (var4 + (var1 * 132))
    var0 = func250(i32_load16_u((var4 + (var1 * 132)) + 112), i32_load16_u(var0 + 114), i32_load((var4 + (var9 * 132)) + 28))
    if func250(i32_load16_u((var4 + (var1 * 132)) + 112), i32_load16_u(var0 + 114), i32_load((var4 + (var9 * 132)) + 28)):
        break
    func29(var6, 1)
    break
    if var2:
        break
    var2 = (var4 + (var1 * 132))
    if i32_load((var4 + (var1 * 132)) + 36):
        break
    if i32_load8_u(var2 + 128):
        break
    if (1 if var5 == 10 else 0):
        break
    if (1 if i32_load(((var16 * 404) + 9568096) + 184) == 0 else 0):
        break
    var5 = i32_load((var4 + (var1 * 132)) + 100)
    if (1 if i32_load((var4 + (var1 * 132)) + 100) == 0 else 0):
        break
    if ((1 if var5 == var9 else 0) & (1 if var0 >= 0 else 0)):
        break
    var0 = (var4 + (var5 * 132))
    if (1 if (i32_load((var4 + (var1 * 132)) + 64) + 5) >= (((i32_load((((i32_load8_u((var4 + (var5 * 132)) + 122) * 1020) + 9299904) + (var7 << 2))) * i32_load(var0 + 52)) & 0xFFFFFFFF) // 100) else 0):
        break
    if (1 if var7 == var10 else 0):
        break
    if i32_load8_u(((var7 * 404) + 9568096) + 380):
        i32_store8(var6 + 129, 9)
        break
    if (1 if var11 != 9 else 0):
        break
    var5 = func106(var6, var7, -1, -1)
    if (1 if func106(var6, var7, -1, -1) == 0 else 0):
        func29(var6, 1)
        var0 = (var4 + (var1 * 132))
        if (1 if i32_load((var4 + (var1 * 132)) + 100) != var9 else 0):
            break
        i32_store(var0 + 100, 0)
        break
    var10 = i32_load(9671128)
    var11 = i32_load8_u((i32_load(9671128) + (var5 * 132)) + 122)
    var0 = ((i32_load8_u((i32_load(9671128) + (var5 * 132)) + 122) * 404) + 9568096)
    if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var5 * 132)) + 122) * 404) + 9568096) + 264) == 1 else 0):
        break
    var3 = i32_load(var0 + 216)
    if (1 if i32_load(var0 + 216) == 0 else 0):
        break
    var2 = i32_load8_u(var21 + 122)
    var0 = ((i32_load8_u(var21 + 122) * 404) + 9568096)
    var17 = ((i32_load8_u(var21 + 122) * 404) + 9568096)
    var8 = (var10 + (var5 * 132))
    var12 = i32_load16_u((var10 + (var5 * 132)) + 114)
    var13 = (var4 + (var9 * 132))
    var14 = i32_load16_u((var4 + (var9 * 132)) + 114)
    var18 = i32_load16_u(var8 + 112)
    var20 = i32_load16_u(var13 + 112)
    var0 = i32_load(var0 + 224)
    var24 = (i32_load(var0 + 224) * var0)
    var8 = 0
    var13 = 1
    while True:  # loop $label11
        var0 = (var14 - (var8 + var12))
        var26 = ((var14 - (var8 + var12)) * var0)
        var0 = 0
        while True:  # loop $label10
            var22 = (var20 - (var0 + var18))
            var22 = (((var20 - (var0 + var18)) * var22) + var26)
            if (1 if var24 >= ((((var20 - (var0 + var18)) * var22) + var26) - 1) else 0):
                var23 = i32_load(var17 + 228)
                if (1 if var22 >= (i32_load(var17 + 228) * var23) else 0):
                    break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var3 else 0):
                continue
            break  # end loop
        var8 = (var8 + 1)
        var13 = (1 if (var8 + 1) < var3 else 0)
        if (1 if var3 != var8 else 0):
            continue
        break  # end loop
    if (1 if (var13 & 1) == 0 else 0):
        break
    var0 = (var4 + (var1 * 132))
    if (1 if var9 == i32_load((var4 + (var1 * 132)) + 100) else 0):
        i32_store(var0 + 100, 0)
    i32_store((i32_load(9215884) + (i32_load(var6 + 44) << 4)) + 12, var5)
    break
    var0 = (var4 + (var9 * 132))
    if (1 if i32_load8_u((var4 + (var9 * 132)) + 125) == 1 else 0):
        i32_store8(var0 + 125, 0)
    break
    var2 = var16
    var11 = var7
    var10 = var4
    var5 = var1
    var17 = (var10 + (var5 * 132))
    var26 = ((var16 * 404) + 9568096)
    if (1 if i32_load(((var16 * 404) + 9568096) + 264) != 1 else 0):
        var0 = ((var7 * 404) + 9568096)
        var14 = i32_load(((var7 * 404) + 9568096) + 220)
        var1 = i32_load16_u(var17 + 114)
        var3 = (i32_load(((var7 * 404) + 9568096) + 220) + i32_load16_u(var17 + 114))
        var18 = i32_load(var0 + 216)
        var13 = i32_load16_u(var17 + 112)
        var12 = (i32_load(var0 + 216) + i32_load16_u(var17 + 112))
        var8 = (var4 + (var9 * 132))
        var0 = i32_load16_u((var4 + (var9 * 132)) + 114)
        var8 = i32_load16_u(var8 + 112)
        var20 = (1 if i32_load16_u(var8 + 112) < var13 else 0)
        if (1 if i32_load16_u(var8 + 112) < var13 else 0):
            break
        if (1 if var8 >= var12 else 0):
            break
        if (1 if var0 < var1 else 0):
            break
        if (1 if var0 >= var3 else 0):
            break
        var1 = ((var14 // 2) + var1)
        var1 = (-1 if (1 if var0 > var1 else 0) else (1 if ((var14 // 2) + var1) != var0 else 0))
        var0 = ((var18 // 2) + var13)
        break
        var1 = (1 if (1 if var0 < var1 else 0) else (-1 if (1 if var0 >= var3 else 0) else 0))
        var0 = (((1 if var20 else (-1 if (1 if var8 >= var12 else 0) else 0)) + (var1 * 3)) + 4)
        if (1 if (((1 if var20 else (-1 if (1 if var8 >= var12 else 0) else 0)) + (var1 * 3)) + 4) <= 8 else 0):
        else:
        i32_store8(i32_load8_u((var0 + 10184)) + 124, 6)
    if i32_load(((var7 * 404) + 9568096) + 260):
        var12 = (var10 + (var5 * 132))
        var13 = i32_load16_u((var10 + (var5 * 132)) + 114)
        var3 = i32_load16_u(var12 + 112)
        var8 = i32_load(((var11 * 404) + 9568096) + 216)
        if i32_load(((var11 * 404) + 9568096) + 216):
            var0 = ((var2 * 404) + 9568096)
            var2 = ((var2 * 404) + 9568096)
            var1 = (var4 + (var9 * 132))
            var14 = i32_load16_u((var4 + (var9 * 132)) + 114)
            var18 = i32_load16_u(var1 + 112)
            var0 = i32_load(var0 + 224)
            var20 = (i32_load(var0 + 224) * var0)
            var1 = 0
            var11 = 1
            while True:  # loop $label17
                var0 = (var14 - (var1 + var13))
                var24 = ((var14 - (var1 + var13)) * var0)
                var0 = 0
                while True:  # loop $label16
                    var22 = (var18 - (var0 + var3))
                    var22 = (((var18 - (var0 + var3)) * var22) + var24)
                    if (1 if var20 >= ((((var18 - (var0 + var3)) * var22) + var24) - 1) else 0):
                        var23 = i32_load(var2 + 228)
                        if (1 if var22 >= (i32_load(var2 + 228) * var23) else 0):
                            break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var8 else 0):
                        continue
                    break  # end loop
                var1 = (var1 + 1)
                var11 = (1 if (var1 + 1) < var8 else 0)
                if (1 if var1 != var8 else 0):
                    continue
                break  # end loop
            var0 = 0
            if (var11 & 1):
                break
        if (1 if i32_load8_u(var12 + 125) == 1 else 0):
            var0 = (i32_load8_u((var10 + (var5 * 132)) + 124) << 3)
            var13 = (var13 - i32_load(((i32_load8_u((var10 + (var5 * 132)) + 124) << 3) + 8996)))
            var3 = (var3 - i32_load((var0 + 8992)))
        var11 = i32_load(((var7 * 404) + 9568096) + 216)
        if (1 if i32_load(((var7 * 404) + 9568096) + 216) == 0 else 0):
            var1 = 0
            break
        var22 = (var11 & -2)
        var23 = (var11 & 1)
        var24 = (var11 - 1)
        var0 = ((var16 * 404) + 9568096)
        var12 = ((var16 * 404) + 9568096)
        var1 = (var4 + (var9 * 132))
        var27 = i32_load16_u((var4 + (var9 * 132)) + 114)
        var14 = i32_load16_u(var1 + 112)
        var0 = i32_load(var0 + 224)
        var18 = (i32_load(var0 + 224) * var0)
        var1 = 1
        var8 = 0
        while True:  # loop $label22
            var0 = (var27 - (var8 + var13))
            var20 = ((var27 - (var8 + var13)) * var0)
            var0 = 0
            var2 = 0
            if var24:
                while True:  # loop $label20
                    var19 = (var14 - (var0 + var3))
                    var19 = (var20 + ((var14 - (var0 + var3)) * var19))
                    if (1 if var18 >= ((var20 + ((var14 - (var0 + var3)) * var19)) - 1) else 0):
                        var1 = i32_load(var12 + 228)
                        var1 = (var1 if (1 if var19 < (i32_load(var12 + 228) * var1) else 0) else 0)
                    var19 = (var14 - ((var0 | 1) + var3))
                    var19 = (var20 + ((var14 - ((var0 | 1) + var3)) * var19))
                    if (1 if var18 >= ((var20 + ((var14 - ((var0 | 1) + var3)) * var19)) - 1) else 0):
                        var1 = i32_load(var12 + 228)
                        var1 = (var1 if (1 if var19 < (i32_load(var12 + 228) * var1) else 0) else 0)
                    var0 = (var0 + 2)
                    var2 = (var2 + 2)
                    if (1 if (var2 + 2) != var22 else 0):
                        continue
                    break  # end loop
            if (1 if var23 == 0 else 0):
                break
            var0 = (var14 - (var0 + var3))
            var0 = (var20 + ((var14 - (var0 + var3)) * var0))
            if (1 if ((var20 + ((var14 - (var0 + var3)) * var0)) - 1) > var18 else 0):
                break
            var1 = i32_load(var12 + 228)
            var1 = (var1 if (1 if var0 < (i32_load(var12 + 228) * var1) else 0) else 0)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != var11 else 0):
                continue
            break  # end loop
        var0 = 0
        if (1 if (var1 & 1) == 0 else 0):
            break
        if (1 if var11 == 0 else 0):
            var1 = 0
            break
        var22 = (var11 & -2)
        var23 = (var11 & 1)
        var0 = ((var16 * 404) + 9568096)
        var12 = ((var16 * 404) + 9568096)
        var1 = (var4 + (var9 * 132))
        var27 = i32_load16_u((var4 + (var9 * 132)) + 114)
        var14 = i32_load16_u(var1 + 112)
        var0 = (i32_load(var0 + 224) + 1)
        var18 = ((i32_load(var0 + 224) + 1) * var0)
        var1 = 0
        var8 = 0
        while True:  # loop $label25
            var0 = (var27 - (var8 + var13))
            var20 = ((var27 - (var8 + var13)) * var0)
            var0 = 0
            var2 = 0
            if var24:
                while True:  # loop $label23
                    var19 = (var14 - (var0 + var3))
                    var19 = (var20 + ((var14 - (var0 + var3)) * var19))
                    if (1 if var18 >= ((var20 + ((var14 - (var0 + var3)) * var19)) - 1) else 0):
                        var1 = i32_load(var12 + 228)
                        var1 = (1 if (1 if var19 >= (i32_load(var12 + 228) * var1) else 0) else var1)
                    var19 = (var14 - ((var0 | 1) + var3))
                    var19 = (var20 + ((var14 - ((var0 | 1) + var3)) * var19))
                    if (1 if var18 >= ((var20 + ((var14 - ((var0 | 1) + var3)) * var19)) - 1) else 0):
                        var1 = i32_load(var12 + 228)
                        var1 = (1 if (1 if var19 >= (i32_load(var12 + 228) * var1) else 0) else var1)
                    var0 = (var0 + 2)
                    var2 = (var2 + 2)
                    if (1 if (var2 + 2) != var22 else 0):
                        continue
                    break  # end loop
            if (1 if var23 == 0 else 0):
                break
            var0 = (var14 - (var0 + var3))
            var0 = (var20 + ((var14 - (var0 + var3)) * var0))
            if (1 if ((var20 + ((var14 - (var0 + var3)) * var0)) - 1) > var18 else 0):
                break
            var1 = i32_load(var12 + 228)
            var1 = (1 if (1 if var0 >= (i32_load(var12 + 228) * var1) else 0) else var1)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != var11 else 0):
                continue
            break  # end loop
        var0 = (var1 & 1)
        if (1 if (var1 & 1) == 0 else 0):
            break
    else:
    var8 = 0
    var11 = (var4 + (var9 * 132))
    if (1 if i32_load8_u((var4 + (var9 * 132)) + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var11 + 128) == 0 else 0):
        break
    var0 = (var4 + (var9 * 132))
    i32_store8((var4 + (var9 * 132)) + 127, 0)
    var1 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    if (1 if i32_load8_u(9142916) == 0 else 0):
        break
    i32_store(var15 + 36, var1)
    i32_store(var15 + 32, 0)
    a_b()
    break
    if i32_load(((var16 * 404) + 9568096) + 260):
        break
    func29(var6, 1)
    break
    var0 = i32_load16_u(var0 + 110)
    i32_store(var15 + 20, var1)
    i32_store(var15 + 16, (var0 + 16))
    a_b()
    i32_store8(var11 + 128, 0)
    if (1 if i32_load((var10 + (var5 * 132)) + 64) == -1 else 0):
        func29(var6, 1)
        break
    var2 = i32_load8_u(var21 + 122)
    var0 = i32_load(((i32_load8_u(var21 + 122) * 404) + 9568096) + 96)
    var0 = (i32_load(((i32_load8_u(var21 + 122) * 404) + 9568096) + 96) - (var0 % 25))
    var1 = (25 if (1 if var0 <= 25 else 0) else (i32_load(((i32_load8_u(var21 + 122) * 404) + 9568096) + 96) - (var0 % 25)))
    var0 = ((var8 ^ 1) & (1 if i32_load8_u(var11 + 125) == 1 else 0))
    if (1 if var29 < 2 else 0):
        break
    if (1 if var0 == 0 else 0):
        break
    var2 = ((var2 * 404) + 9568096)
    if (1 if i32_load(((var2 * 404) + 9568096) + 268) != 2 else 0):
        break
    var2 = i32_load(var2 + 276)
    var2 = (i32_load(var2 + 276) if var2 else 25)
    var3 = (32000 // i32_load(((var16 * 404) + 9568096) + 260))
    var1 = (((i32_load(var2 + 276) if var2 else 25) - (32000 // i32_load(((var16 * 404) + 9568096) + 260))) if (1 if var2 > (var1 + var3) else 0) else var1)
    if var8:
        break
    # br_table ['$label32', '$label31', '$label31', '$label31', '$label32', '$label31']
    _br_idx = i32_load(var26 + 264)
    break  # br_table
    if var0:
        var0 = (var10 + (var5 * 132))
        func63(func37(var6, var25, (0.0 if var0 else float(((i32_load(9142848) * 25) - var1))), 0), var6, 6, i32_load((var10 + (var5 * 132)) + 28), var1)
        if i32_load(var0 + 100):
            break
        i32_store(var0 + 100, i32_load((var4 + (var9 * 132)) + 28))
        break
    var0 = (var10 + (var5 * 132))
    if (1 if i32_load((var10 + (var5 * 132)) + 100) == 0 else 0):
        i32_store(var0 + 100, i32_load((var4 + (var9 * 132)) + 28))
    if (1 if i32_load8_u(((i32_load8_u(var21 + 122) * 404) + 9568096) + 333) == 0 else 0):
        break
    var0 = (var10 + (var5 * 132))
    if (1 if i32_load(38564) != i32_load8_u((var10 + (var5 * 132)) + 122) else 0):
        break
    # br_table ['$label33', '$label34', '$label34', '$label34', '$label34', '$label34', '$label34', '$label34', '$label34', '$label34', '$label33', '$label34']
    _br_idx = (i32_load8_u(var0 + 125) - 4)
    break  # br_table
    var0 = func106(var6, -1, -1, -1)
    if (1 if func106(var6, -1, -1, -1) == 0 else 0):
        break
    if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 264) == 1 else 0):
        break
    break
    var0 = 0
    var12 = i32_load(var6 + 84)
    var1 = i32_load(9561692)
    var2 = i32_load16_u(var6 + 110)
    var3 = (i32_load(9561692) + (i32_load16_u(var6 + 110) * 286704))
    if (1 if i32_load(var6 + 84) >= i32_load(((i32_load(9561692) + (i32_load16_u(var6 + 110) * 286704)) + 284316)) else 0):
        break
    var14 = i32_load((var3 + 284012))
    var13 = 10
    if i32_load(((var3 + (i32_load(38488) << 2)) + 281808)):
        break
    var3 = (var1 + (var2 * 286704))
    if i32_load((((var1 + (var2 * 286704)) + (i32_load(38848) << 2)) + 281808)):
        break
    var13 = (10 if i32_load(((var3 + (i32_load(38916) << 2)) + 281808)) else 0)
    if (1 if var12 >= (var13 + var14) else 0):
        break
    var0 = (1 if i32_load(((var1 + (var2 * 286704)) + 284008)) != 0 else 0)
    if (1 if var0 == 0 else 0):
        break
    var0 = (var4 + (var9 * 132))
    var1 = (i32_load(var0 + 80) + (i32_load(var0 + 52) << 1))
    i32_store((var4 + (var9 * 132)) + 80, (i32_load(var0 + 80) + (i32_load(var0 + 52) << 1)))
    var0 = i32_load(var0 + 84)
    if (1 if var1 < ((1 if (1 if var0 <= 1 else 0) else i32_load(var0 + 84)) * 100) else 0):
        break
    func198(var6)
    var0 = (var4 + (var9 * 132))
    var3 = ((var16 * 404) + 9568096)
    var13 = i32_load(((var16 * 404) + 9568096) + 32)
    if (1 if i32_load(((var16 * 404) + 9568096) + 32) == 0 else 0):
        break
    var1 = i32_load16_u(var0 + 112)
    var2 = ((i32_load16_u(var0 + 112) << 5) - i32_load(9142952))
    var2 = i32_load16_u(var0 + 114)
    var12 = ((i32_load16_u(var0 + 114) << 5) - i32_load(9142956))
    if (1 if (((((i32_load16_u(var0 + 112) << 5) - i32_load(9142952)) * var2) + (((i32_load16_u(var0 + 114) << 5) - i32_load(9142956)) * var12)) - 1) > 9000000 else 0):
        break
    var12 = i32_load(var3 + 28)
    var14 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var3 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var2) + var1) << 1)))
    if (1 if var14 != 2 else 0):
        break
    if (1 if var3 > 1 else 0):
        break
    break
    var0 = (var4 + (var9 * 132))
    i32_store(var15 + 44, i32_load16_u((var4 + (var9 * 132)) + 112))
    i32_store(var15 + 40, i32_load16_u(var0 + 114))
    var16 = i32_load(var0 + 28)
    var0 = 0
    var11 = i32_load(9142440)
    var5 = (i32_load(9142440) + 2)
    var7 = i32_load(9142840)
    var9 = i32_load(var15 + 40)
    var8 = i32_load(var15 + 44)
    while True:  # loop $label45
        var4 = var0
        var0 = (var0 << 2)
        var2 = (i32_load((((var0 << 2) | 4) + 8611904)) + var9)
        if (1 if var11 <= (i32_load((((var0 << 2) | 4) + 8611904)) + var9) else 0):
            break
        var10 = (i32_load((var0 + 8611904)) + var8)
        if (1 if var11 <= (i32_load((var0 + 8611904)) + var8) else 0):
            break
        if (1 if (var2 | var10) < 0 else 0):
            break
        var0 = (var10 - 1)
        var1 = (var2 + var5)
        var21 = ((var2 + var5) * var5)
        var3 = ((var1 + 2) * var5)
        var13 = ((var1 + 1) * var5)
        while True:  # loop $label43
            var1 = (var0 + 1)
            var17 = i32_load((var7 + ((var21 + (var0 + 1)) << 2)))
            if (i32_load((var7 + ((var21 + (var0 + 1)) << 2))) if (1 if var16 != var17 else 0) else 0):
                break
            var17 = i32_load((var7 + ((var1 + var13) << 2)))
            if (i32_load((var7 + ((var1 + var13) << 2))) if (1 if var16 != var17 else 0) else 0):
                break
            var17 = i32_load((var7 + ((var1 + var3) << 2)))
            if (i32_load((var7 + ((var1 + var3) << 2))) if (1 if var16 != var17 else 0) else 0):
                break
            var17 = (1 if var0 <= var10 else 0)
            var0 = var1
            if var17:
                continue
            break  # end loop
        i32_store(var15 + 44, var10)
        i32_store(var15 + 40, var2)
        break
        var0 = (var4 + 2)
        if (1 if var4 < 878 else 0):
            continue
        break  # end loop
    if 0:
        break
    func29(var6, 1)
    break
    if (1 if var3 == 0 else 0):
        break
    i32_store(var15, i32_load((var12 + (((i32_load(9142848) + var1) % var13) << 2))))
    i32_store(var15 + 4, var1)
    i32_store(var15 + 8, var2)
    a_b()
    var2 = ((var16 * 404) + 9568096)
    if i32_load(((var16 * 404) + 9568096) + 184):
        var1 = ((var7 * 404) + 9568096)
        var7 = i32_load(((var7 * 404) + 9568096) + 216)
        var11 = (var10 + (var5 * 132))
        var3 = i32_load16_u((var10 + (var5 * 132)) + 112)
        var36 = ((float(i32_load(var2 + 216)) * 0.5) + float(i32_load16_u(var0 + 112)))
        var33 = ((((float(i32_load(((var7 * 404) + 9568096) + 216)) * 0.5) + float(i32_load16_u((var10 + (var5 * 132)) + 112))) - ((float(i32_load(var2 + 216)) * 0.5) + float(i32_load16_u(var0 + 112)))) * 32.0)
        var1 = i32_load(var1 + 220)
        var11 = i32_load16_u(var11 + 114)
        var37 = ((float(i32_load(var2 + 220)) * 0.5) + float(i32_load16_u(var0 + 114)))
        var32 = ((((float(i32_load(var1 + 220)) * 0.5) + float(i32_load16_u(var11 + 114))) - ((float(i32_load(var2 + 220)) * 0.5) + float(i32_load16_u(var0 + 114)))) * 32.0)
        var30 = math.sqrt(((((((float(i32_load(((var7 * 404) + 9568096) + 216)) * 0.5) + float(i32_load16_u((var10 + (var5 * 132)) + 112))) - ((float(i32_load(var2 + 216)) * 0.5) + float(i32_load16_u(var0 + 112)))) * 32.0) * var33) + (((((float(i32_load(var1 + 220)) * 0.5) + float(i32_load16_u(var11 + 114))) - ((float(i32_load(var2 + 220)) * 0.5) + float(i32_load16_u(var0 + 114)))) * 32.0) * var32)))
        var0 = (((var1 & 0xFFFFFFFF) >> 1) + var11)
        var7 = (((var7 & 0xFFFFFFFF) >> 1) + var3)
        var1 = i32_load(var2 + 272)
        if (1 if i32_load(var2 + 272) == 0 else 0):
            var30 = (var30 / 451.0)
            var31 = ((var30 / 451.0) * 1000.0)
            var31 = (((((var30 / 451.0) * 1000.0) + -25.0) if (1 if var31 > 25.0 else 0) else var31) + 25.0)
            if ((1 if (((((var30 / 451.0) * 1000.0) + -25.0) if (1 if var31 > 25.0 else 0) else var31) + 25.0) < 4294967300.0 else 0) & (1 if var31 >= 0.0 else 0)):
                break
            var1 = 0
            var31 = (var32 / var30)
            var34 = (var33 / var30)
            if (1 if i32_load(38648) == i32_load8_u(var21 + 122) else 0):
                var30 = 0.0
                break
            var30 = 0.0
            break
        var31 = ((float(var1) * 3.14159274) / 180.0)
        var34 = func48(((float(var1) * 3.14159274) / 180.0))
        var31 = func49(var31)
        var30 = (var34 * var31)
        var34 = (func49(var31) * math.sqrt(((var30 * 580.0) / ((var34 * var31) + var30))))
        var31 = (var30 / (func49(var31) * math.sqrt(((var30 * 580.0) / ((var34 * var31) + var30)))))
        var30 = (((var30 / (func49(var31) * math.sqrt(((var30 * 580.0) / ((var34 * var31) + var30))))) * 1000.0) + 25.0)
        if ((1 if (((var30 / (func49(var31) * math.sqrt(((var30 * 580.0) / ((var34 * var31) + var30))))) * 1000.0) + 25.0) < 4294967300.0 else 0) & (1 if var30 >= 0.0 else 0)):
            break
        var1 = 0
        var30 = func423((-var33), (-var32))
        var35 = func48(var30)
        var30 = ((func48(var30) * -0.49999997) * 580.0)
        var30 = ((-((func48(var30) * -0.49999997) * 580.0)) if (1 if var30 < 0.0 else 0) else var30)
        var31 = f32(((float(var32) + (float((var31 * (var31 * ((-((func48(var30) * -0.49999997) * 580.0)) if (1 if var30 < 0.0 else 0) else var30)))) * -0.5)) / float(var31)))
        var34 = (var34 * (-var35))
        var35 = 0.0
        var0 = i32_load8_u(var21 + 122)
        if (1 if i32_load8_u(var21 + 122) == i32_load(38644) else 0):
            break
        if (1 if i32_load(38568) == var0 else 0):
            break
        if (1 if i32_load(38576) == var0 else 0):
            break
        var35 = ((func423(var32, var33) + (0.0 if i32_load8_u(9142916) else 10.0)) + 1.57079637)
        if i32_load8_u(9142917):
            break
        if (1 if func293(var17) == 0 else 0):
            if (1 if func293(var6) == 0 else 0):
                break
        var0 = func244(i32_load(i32_load(var2 + 184)))
        var0 = i32_load(((i32_load8_u(var21 + 122) * 404) + 9568096) + 276)
        if (1 if var1 <= (i32_load(((i32_load8_u(var21 + 122) * 404) + 9568096) + 276) if var0 else 25) else 0):
            break
        i32_store((i32_load(9215884) + (i32_load(var6 + 44) << 4)) + 8, (i32_load((var4 + (var9 * 132)) + 28) + 2147483647))
        break
    if (1 if i32_load(38932) != i32_load8_u(var21 + 122) else 0):
        break
    var1 = (var4 + (var9 * 132))
    if (1 if i32_load((var4 + (var9 * 132)) + 48) == 0 else 0):
        break
    if (1 if i32_load(var1 + 40) == 0 else 0):
        break
    var2 = func245()
    var7 = i32_load(9142772)
    var13 = (i32_load(i32_load(9142772)) // 2)
    var1 = i32_load(var1 + 48)
    var12 = (i32_load(i32_load(var1 + 48)) // 2)
    var3 = (i32_load(var1 + 20) * i32_load(var1 + 16))
    if (i32_load(var1 + 20) * i32_load(var1 + 16)):
        var32 = float(((i32_load(var1 + 4) // var3) // 2))
    var3 = (i32_load(var7 + 20) * i32_load(var7 + 16))
    if (i32_load(var7 + 20) * i32_load(var7 + 16)):
        var33 = float(((i32_load(var7 + 4) // var3) // 2))
    var3 = i32_load8_u((var4 + (var9 * 132)) + 124)
    var14 = (i32_load8_u((var4 + (var9 * 132)) + 124) << 3)
    var18 = i32_load(((i32_load8_u((var4 + (var9 * 132)) + 124) << 3) + 8996))
    var30 = (float(i32_load16_u(var0 + 114)) * 32.0)
    var31 = (((float(i32_load16_u(var0 + 114)) * 32.0) + (float(i32_load(9142440)) * 32.0)) + 128.0)
    var32 = (0.707106769 if (var3 & 1) else 1.0)
    var30 = (var32 * (0.707106769 if (var3 & 1) else 1.0))
    if (1 if abs((var32 * (0.707106769 if (var3 & 1) else 1.0))) < 2147483650.0 else 0):
        break
    var33 = ((var30 + ((int(var30) + float((-2147483648 * var18))) - float(i32_load(var1 + 12)))) - var33)
    var14 = i32_load((var14 + 8992))
    var32 = float(var12)
    var30 = (var32 * float(var12))
    if (1 if abs((var32 * float(var12))) < 2147483650.0 else 0):
        break
    func254(i32_load(9142772), var2)
    var1 = i32_load((var4 + (var9 * 132)) + 52)
    var0 = (var10 + (var5 * 132))
    var13 = i32_load(((i32_load8_u((var10 + (var5 * 132)) + 122) * 404) + 9568096) + 324)
    if (1 if i32_load(((i32_load8_u((var10 + (var5 * 132)) + 122) * 404) + 9568096) + 324) == 0 else 0):
        break
    if (1 if i32_load(38676) != i32_load8_u(var21 + 122) else 0):
        break
    var7 = (var4 + (var9 * 132))
    var12 = i32_load((var4 + (var9 * 132)) + 72)
    var2 = (i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704))
    var3 = i32_load(((i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704)) + 284300))
    if (1 if i32_load((var4 + (var9 * 132)) + 72) < i32_load(((i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704)) + 284300)) else 0):
        break
    var1 = (var2 + 281668)
    i32_store((var2 + 281668), (i32_load(var1) + var3))
    var1 = i32_load((var2 + 284308))
    i32_store(var7 + 72, (var12 - var3))
    var1 = (((var1 * var13) & 0xFFFFFFFF) // 100)
    var1 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 400)
    if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 400):
        var7 = i32_load((var10 + (var5 * 132)) + 52)
        if (1 if i32_load8_u(var11 + 125) == 3 else 0):
            break
    if (1 if i32_load8_u((var10 + (var5 * 132)) + 125) != 3 else 0):
        break
    if i32_load8_u(((i32_load8_u(var28 + 122) * 404) + 9568096) + 380):
        i32_store8(var6 + 129, 9)
    var0 = i32_load8_u(var0 + 122)
    if (1 if i32_load8_u(var0 + 122) == i32_load(38564) else 0):
        var0 = (var10 + (var5 * 132))
        func117(var6, func250(i32_load16_u((var10 + (var5 * 132)) + 112), i32_load16_u(var0 + 114), i32_load((var4 + (var9 * 132)) + 28)), 6)
        break
    func117(var6, func106(var6, (-1 if (1 if i32_load8_u(var6 + 129) != 9 else 0) else var0), -1, -1), 6)
    break
    if var8:
        if i32_load(((var16 * 404) + 9568096) + 260):
            break
        func29(var6, 1)
        break
    var0 = i32_load(((i32_load8_u(var21 + 122) * 404) + 9568096) + 276)
    i32_store((i32_load(9215884) + (i32_load(var6 + 44) << 4)), (i32_load(9142848) + (((i32_load(((i32_load8_u(var21 + 122) * 404) + 9568096) + 276) & 0xFFFFFFFF) // 25) if var0 else 1)))
    global global0
    global0 = (var15 + 48)
    return func81(var17, var6, var1, 1)

