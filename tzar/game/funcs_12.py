"""
Auto-generated from WAT. Contains 2 functions.
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
# $func236
# ==========================================================
def func236(var0, var1):
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
    var3 = i32_load(9142440)
    var4 = (i32_load(9142440) + 2)
    var5 = i32_load(var0 + 28)
    var6 = i32_load(9671128)
    var7 = i32_load(9142840)
    var8 = i32_load16_u(var1 + 114)
    var9 = i32_load16_u(var1 + 112)
    var10 = i32_load16_u(var1 + 110)
    var11 = i32_load8_u(var1 + 122)
    var0 = 0
    while True:  # loop $label2
        var1 = var0
        var2 = (var0 << 2)
        var0 = (i32_load((((var0 << 2) | 4) + 8611904)) + var8)
        if (1 if var3 <= (i32_load((((var0 << 2) | 4) + 8611904)) + var8) else 0):
            break
        var2 = (i32_load((var2 + 8611904)) + var9)
        if (1 if var3 <= (i32_load((var2 + 8611904)) + var9) else 0):
            break
        if (1 if (var0 | var2) < 0 else 0):
            break
        var0 = i32_load((((var2 + (((var0 + var4) + 1) * var4)) << 2) + var7) + 4)
        if (1 if i32_load((((var2 + (((var0 + var4) + 1) * var4)) << 2) + var7) + 4) == 0 else 0):
            break
        if (1 if var0 == var5 else 0):
            break
        var2 = (var6 + (var0 * 132))
        if (1 if i32_load16_u((var6 + (var0 * 132)) + 110) != var10 else 0):
            break
        if (1 if i32_load8_u(var2 + 122) == var11 else 0):
            break
        var0 = (var1 + 2)
        if (1 if var1 < 878 else 0):
            continue
        break  # end loop
    var0 = 0
    while True:  # loop $label4
        var1 = var0
        var2 = (var0 << 2)
        var0 = (i32_load((((var0 << 2) | 4) + 8611904)) + var8)
        if (1 if var3 <= (i32_load((((var0 << 2) | 4) + 8611904)) + var8) else 0):
            break
        var2 = (i32_load((var2 + 8611904)) + var9)
        if (1 if var3 <= (i32_load((var2 + 8611904)) + var9) else 0):
            break
        if (1 if (var0 | var2) < 0 else 0):
            break
        var0 = i32_load((((var2 + (((var0 + var4) + 1) * var4)) << 2) + var7) + 4)
        if (1 if i32_load((((var2 + (((var0 + var4) + 1) * var4)) << 2) + var7) + 4) == 0 else 0):
            break
        if (1 if var0 == var5 else 0):
            break
        var2 = (var6 + (var0 * 132))
        if (1 if i32_load16_u((var6 + (var0 * 132)) + 110) != var10 else 0):
            break
        if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 264) == 0 else 0):
            break
        var0 = (var1 + 2)
        if (1 if var1 < 878 else 0):
            continue
        break  # end loop
    var0 = 0
    return var0


# ==========================================================
# $func241
# ==========================================================
def func241(var0, var1, var2, var3, var4, var5):
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
    var6 = (global0 + -64)
    i64_store((global0 + -64) + 48, 0)
    i64_store(var6 + 56, 0)
    i64_store(var6 + 32, 0)
    i64_store(var6 + 40, 0)
    if var2:
        if (1 if var2 >= 4 else 0):
            var11 = (var2 & -4)
            while True:  # loop $label0
                var13 = (var6 + 32)
                var14 = (var9 << 1)
                var10 = ((var6 + 32) + (i32_load16_u((var1 + (var9 << 1))) << 1))
                i32_store16(((var6 + 32) + (i32_load16_u((var1 + (var9 << 1))) << 1)), (i32_load16_u(var10) + 1))
                var10 = ((i32_load16_u((var1 + (var14 | 2))) << 1) + var13)
                i32_store16(((i32_load16_u((var1 + (var14 | 2))) << 1) + var13), (i32_load16_u(var10) + 1))
                var10 = ((i32_load16_u((var1 + (var14 | 4))) << 1) + var13)
                i32_store16(((i32_load16_u((var1 + (var14 | 4))) << 1) + var13), (i32_load16_u(var10) + 1))
                var14 = ((i32_load16_u((var1 + (var14 | 6))) << 1) + var13)
                i32_store16(((i32_load16_u((var1 + (var14 | 6))) << 1) + var13), (i32_load16_u(var14) + 1))
                var9 = (var9 + 4)
                var7 = (var7 + 4)
                if (1 if (var7 + 4) != var11 else 0):
                    continue
                break  # end loop
        var7 = (var2 & 3)
        if (var2 & 3):
            while True:  # loop $label1
                var14 = ((var6 + 32) + (i32_load16_u((var1 + (var9 << 1))) << 1))
                i32_store16(((var6 + 32) + (i32_load16_u((var1 + (var9 << 1))) << 1)), (i32_load16_u(var14) + 1))
                var9 = (var9 + 1)
                var8 = (var8 + 1)
                if (1 if (var8 + 1) != var7 else 0):
                    continue
                break  # end loop
        var9 = i32_load(var4)
        var11 = 15
        var7 = i32_load16_u(var6 + 62)
        if i32_load16_u(var6 + 62):
            break
        break
    var9 = i32_load(var4)
    var11 = 14
    var7 = 0
    if i32_load16_u(var6 + 60):
        break
    var11 = 13
    if i32_load16_u(var6 + 58):
        break
    var11 = 12
    if i32_load16_u(var6 + 56):
        break
    var11 = 11
    if i32_load16_u(var6 + 54):
        break
    var11 = 10
    if i32_load16_u(var6 + 52):
        break
    var11 = 9
    if i32_load16_u(var6 + 50):
        break
    var11 = 8
    if i32_load16_u(var6 + 48):
        break
    var11 = 7
    if i32_load16_u(var6 + 46):
        break
    var11 = 6
    if i32_load16_u(var6 + 44):
        break
    var11 = 5
    if i32_load16_u(var6 + 42):
        break
    var11 = 4
    if i32_load16_u(var6 + 40):
        break
    var11 = 3
    if i32_load16_u(var6 + 38):
        break
    var11 = 2
    if i32_load16_u(var6 + 36):
        break
    if (1 if i32_load16_u(var6 + 34) == 0 else 0):
        var0 = i32_load(var3)
        i32_store(var3, (i32_load(var3) + 4))
        i32_store(var0, 320)
        var0 = i32_load(var3)
        i32_store(var3, (i32_load(var3) + 4))
        i32_store(var0, 320)
        var10 = 1
        break
    var13 = (1 if var9 != 0 else 0)
    var11 = 1
    var9 = 1
    break
    var13 = (var9 if (1 if var9 < var11 else 0) else var11)
    var15 = 1
    var9 = 1
    while True:  # loop $label6
        if i32_load16_u(((var6 + 32) + (var9 << 1))):
            break
        var9 = (var9 + 1)
        if (1 if (var9 + 1) != var11 else 0):
            continue
        break  # end loop
    var9 = var11
    var8 = -1
    var14 = i32_load16_u(var6 + 34)
    if (1 if i32_load16_u(var6 + 34) > 2 else 0):
        break
    var10 = i32_load16_u(var6 + 36)
    var12 = (i32_load16_u(var6 + 36) + (var14 << 1))
    if (1 if (i32_load16_u(var6 + 36) + (var14 << 1)) > 4 else 0):
        break
    var27 = i32_load16_u(var6 + 38)
    var12 = (i32_load16_u(var6 + 38) + (var12 << 1))
    if (1 if (i32_load16_u(var6 + 38) + (var12 << 1)) > 8 else 0):
        break
    var16 = i32_load16_u(var6 + 40)
    var12 = (i32_load16_u(var6 + 40) + (var12 << 1))
    if (1 if (i32_load16_u(var6 + 40) + (var12 << 1)) > 16 else 0):
        break
    var21 = i32_load16_u(var6 + 42)
    var12 = (32 - (i32_load16_u(var6 + 42) + (var12 << 1)))
    if (1 if (32 - (i32_load16_u(var6 + 42) + (var12 << 1))) < 0 else 0):
        break
    var12 = i32_load16_u(var6 + 44)
    var17 = ((var12 << 1) - i32_load16_u(var6 + 44))
    if (1 if ((var12 << 1) - i32_load16_u(var6 + 44)) < 0 else 0):
        break
    var17 = i32_load16_u(var6 + 46)
    var18 = ((var17 << 1) - i32_load16_u(var6 + 46))
    if (1 if ((var17 << 1) - i32_load16_u(var6 + 46)) < 0 else 0):
        break
    var18 = i32_load16_u(var6 + 48)
    var19 = ((var18 << 1) - i32_load16_u(var6 + 48))
    if (1 if ((var18 << 1) - i32_load16_u(var6 + 48)) < 0 else 0):
        break
    var19 = i32_load16_u(var6 + 50)
    var20 = ((var19 << 1) - i32_load16_u(var6 + 50))
    if (1 if ((var19 << 1) - i32_load16_u(var6 + 50)) < 0 else 0):
        break
    var20 = i32_load16_u(var6 + 52)
    var22 = ((var20 << 1) - i32_load16_u(var6 + 52))
    if (1 if ((var20 << 1) - i32_load16_u(var6 + 52)) < 0 else 0):
        break
    var22 = i32_load16_u(var6 + 54)
    var23 = ((var22 << 1) - i32_load16_u(var6 + 54))
    if (1 if ((var22 << 1) - i32_load16_u(var6 + 54)) < 0 else 0):
        break
    var23 = i32_load16_u(var6 + 56)
    var24 = ((var23 << 1) - i32_load16_u(var6 + 56))
    if (1 if ((var23 << 1) - i32_load16_u(var6 + 56)) < 0 else 0):
        break
    var24 = i32_load16_u(var6 + 58)
    var25 = ((var24 << 1) - i32_load16_u(var6 + 58))
    if (1 if ((var24 << 1) - i32_load16_u(var6 + 58)) < 0 else 0):
        break
    var25 = i32_load16_u(var6 + 60)
    var26 = ((var25 << 1) - i32_load16_u(var6 + 60))
    if (1 if ((var25 << 1) - i32_load16_u(var6 + 60)) < 0 else 0):
        break
    var26 = (var26 << 1)
    if (1 if (var26 << 1) < var7 else 0):
        break
    if ((1 if var7 != var26 else 0) if ((1 if var0 == 0 else 0) | var15) else 0):
        break
    var15 = (1 if var9 < var13 else 0)
    var8 = 0
    i32_store16(var6 + 2, 0)
    i32_store16(var6 + 4, var14)
    var7 = (var10 + var14)
    i32_store16(var6 + 6, (var10 + var14))
    var7 = (var7 + var27)
    i32_store16(var6 + 8, (var7 + var27))
    var7 = (var7 + var16)
    i32_store16(var6 + 10, (var7 + var16))
    var7 = (var7 + var21)
    i32_store16(var6 + 12, (var7 + var21))
    var7 = (var7 + var12)
    i32_store16(var6 + 14, (var7 + var12))
    var7 = (var7 + var17)
    i32_store16(var6 + 16, (var7 + var17))
    var7 = (var7 + var18)
    i32_store16(var6 + 18, (var7 + var18))
    var7 = (var7 + var19)
    i32_store16(var6 + 20, (var7 + var19))
    var7 = (var7 + var20)
    i32_store16(var6 + 22, (var7 + var20))
    var7 = (var7 + var22)
    i32_store16(var6 + 24, (var7 + var22))
    var7 = (var7 + var23)
    i32_store16(var6 + 26, (var7 + var23))
    var7 = (var7 + var24)
    i32_store16(var6 + 28, (var7 + var24))
    i32_store16(var6 + 30, (var7 + var25))
    if (1 if var2 == 0 else 0):
        break
    if (1 if var2 != 1 else 0):
        var14 = (var2 & -2)
        var7 = 0
        while True:  # loop $label9
            var10 = i32_load16_u((var1 + (var8 << 1)))
            if i32_load16_u((var1 + (var8 << 1))):
                var10 = (var6 + (var10 << 1))
                var10 = i32_load16_u(var10)
                i32_store16((var6 + (var10 << 1)), (i32_load16_u(var10) + 1))
                i32_store16((var5 + (var10 << 1)), var8)
            var10 = (var8 | 1)
            var12 = i32_load16_u((var1 + ((var8 | 1) << 1)))
            if i32_load16_u((var1 + ((var8 | 1) << 1))):
                var12 = (var6 + (var12 << 1))
                var12 = i32_load16_u(var12)
                i32_store16((var6 + (var12 << 1)), (i32_load16_u(var12) + 1))
                i32_store16((var5 + (var12 << 1)), var10)
            var8 = (var8 + 2)
            var7 = (var7 + 2)
            if (1 if (var7 + 2) != var14 else 0):
                continue
            break  # end loop
    if (1 if (var2 & 1) == 0 else 0):
        break
    var2 = i32_load16_u((var1 + (var8 << 1)))
    if (1 if i32_load16_u((var1 + (var8 << 1))) == 0 else 0):
        break
    var2 = (var6 + (var2 << 1))
    var2 = i32_load16_u(var2)
    i32_store16((var6 + (var2 << 1)), (i32_load16_u(var2) + 1))
    i32_store16((var5 + (var2 << 1)), var8)
    var10 = (var13 if var15 else var9)
    var21 = 20
    var22 = 0
    var14 = var5
    var12 = var5
    var17 = 0
    # br_table ['$label10', '$label11', '$label12']
    _br_idx = var0
    break  # br_table
    var8 = 1
    if (1 if var10 > 9 else 0):
        break
    var21 = 257
    var12 = 26272
    var14 = 26208
    var17 = 1
    break
    var22 = (1 if var0 == 2 else 0)
    var21 = 0
    var12 = 26400
    var14 = 26336
    if (1 if var0 != 2 else 0):
        break
    var8 = 1
    if (1 if var10 > 9 else 0):
        break
    var18 = (1 << var10)
    var24 = ((1 << var10) - 1)
    var19 = i32_load(var3)
    var20 = 0
    var7 = var10
    var16 = 0
    var15 = 0
    var0 = -1
    while True:  # loop $label20
        var27 = (1 << var7)
        while True:  # loop $label17
            var13 = (var9 - var16)
            var7 = i32_load16_u((var5 + (var20 << 1)))
            if (1 if (i32_load16_u((var5 + (var20 << 1))) + 1) < var21 else 0):
                break
            if (1 if var7 < var21 else 0):
                var7 = 0
                break
            var2 = ((var7 - var21) << 1)
            var7 = i32_load16_u((var14 + ((var7 - var21) << 1)))
            var2 = i32_load8_u((var2 + var12))
            var25 = ((var15 & 0xFFFFFFFF) >> var16)
            var26 = (-1 << var13)
            var8 = var27
            while True:  # loop $label14
                var8 = (var8 + var26)
                var23 = (var19 + (((var8 + var26) + var25) << 2))
                i32_store16((var19 + (((var8 + var26) + var25) << 2)) + 2, var7)
                i32_store8(var23 + 1, var13)
                i32_store8(var23, var2)
                if var8:
                    continue
                break  # end loop
            var7 = (1 << (var9 - 1))
            while True:  # loop $label15
                var2 = var7
                var7 = ((var7 & 0xFFFFFFFF) >> 1)
                if (var2 & var15):
                    continue
                break  # end loop
            var8 = ((var6 + 32) + (var9 << 1))
            var8 = (i32_load16_u(var8) - 1)
            i32_store16(((var6 + 32) + (var9 << 1)), (i32_load16_u(var8) - 1))
            var15 = ((((var2 - 1) & var15) + var2) if var2 else 0)
            var20 = (var20 + 1)
            if (1 if (var8 & 65535) == 0 else 0):
                if (1 if var9 == var11 else 0):
                    break
                var9 = i32_load16_u((var1 + (i32_load16_u((var5 + (var20 << 1))) << 1)))
            if (1 if var9 <= var10 else 0):
                continue
            var2 = (var15 & var24)
            if (1 if (var15 & var24) == var0 else 0):
                continue
            break  # end loop
        var16 = (var16 if var16 else var10)
        var7 = (var9 - (var16 if var16 else var10))
        var13 = (1 << (var9 - (var16 if var16 else var10)))
        if (1 if var9 < var11 else 0):
            var0 = (var11 - var16)
            var8 = var9
            while True:  # loop $label19
                var8 = (var13 - i32_load16_u(((var6 + 32) + (var8 << 1))))
                if (1 if (var13 - i32_load16_u(((var6 + 32) + (var8 << 1)))) <= 0 else 0):
                    break
                var13 = (var8 << 1)
                var7 = (var7 + 1)
                var8 = ((var7 + 1) + var16)
                if (1 if ((var7 + 1) + var16) < var11 else 0):
                    continue
                break  # end loop
            var7 = var0
            var13 = (1 << var7)
        var8 = 1
        var18 = (var13 + var18)
        if (var17 & (1 if (var13 + var18) > 852 else 0)):
            break
        if (var22 & (1 if var18 > 592 else 0)):
            break
        var8 = i32_load(var3)
        var0 = (i32_load(var3) + (var2 << 2))
        i32_store8((i32_load(var3) + (var2 << 2)) + 1, var10)
        i32_store8(var0, var7)
        var19 = (var19 + (var27 << 2))
        i32_store16(var0 + 2, ((((var19 + (var27 << 2)) - var8) & 0xFFFFFFFF) >> 2))
        var0 = var2
        continue
        break  # end loop
    if var15:
        var0 = (var19 + (var15 << 2))
        i32_store16((var19 + (var15 << 2)) + 2, 0)
        i32_store8(var0 + 1, var13)
        i32_store8(var0, 64)
    i32_store(var3, (i32_load(var3) + (var18 << 2)))
    i32_store(var4, var10)
    var8 = 0
    return var8

