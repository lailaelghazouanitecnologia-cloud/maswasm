"""
Auto-generated from WAT. Contains 5 functions.
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
# $func167
# ==========================================================
def func167(var0, var1, var2, var3, var4):
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
    var8 = i32_load(9142440)
    var20 = i32_load(var1)
    var21 = i32_load(var0)
    if (1 if var4 == 0 else 0):
        var11 = 1
        while True:  # loop $label7
            var4 = ((var7 << 1) | 1)
            var3 = (var21 - var7)
            var12 = (((var7 << 1) | 1) + (var21 - var7))
            var13 = ((((var7 << 1) | 1) + (var21 - var7)) - 1)
            var2 = (var20 - var7)
            var4 = (var4 + (var20 - var7))
            var14 = ((var4 + (var20 - var7)) - 1)
            var6 = var3
            while True:  # loop $label6
                if (1 if var6 >= var8 else 0):
                    break
                var5 = var2
                if (1 if var6 != var13 else 0):
                    if (1 if var3 != var6 else 0):
                        break
                while True:  # loop $label3
                    if ((1 if var5 < var8 else 0) & (1 if (var5 | var6) >= 0 else 0)):
                        break
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) < var4 else 0):
                        continue
                    break  # end loop
                break
                while True:  # loop $label5
                    if ((1 if var2 != var5 else 0) & (1 if var5 != var14 else 0)):
                        break
                    if (1 if var5 >= var8 else 0):
                        break
                    if (1 if (var5 | var6) >= 0 else 0):
                        break
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) < var4 else 0):
                        continue
                    break  # end loop
                var6 = (var6 + 1)
                if (1 if (var6 + 1) < var12 else 0):
                    continue
                break  # end loop
            var11 = (1 if var7 < 39 else 0)
            var7 = (var7 + 1)
            if (1 if (var7 + 1) != 40 else 0):
                continue
            break  # end loop
        break
    var22 = (var4 & -2)
    var23 = (var4 & 1)
    var15 = (var8 + 2)
    var24 = ((var8 + 2) * var2)
    var16 = i32_load(9142840)
    var11 = 1
    while True:  # loop $label14
        var2 = ((var9 << 1) | 1)
        var12 = (var21 - var9)
        var25 = (((var9 << 1) | 1) + (var21 - var9))
        var26 = ((((var9 << 1) | 1) + (var21 - var9)) - 1)
        var13 = (var20 - var9)
        var27 = (var2 + (var20 - var9))
        var28 = ((var2 + (var20 - var9)) - 1)
        var6 = var12
        while True:  # loop $label13
            var14 = (var6 + 1)
            if (1 if var6 < var8 else 0):
                var29 = (1 if var6 == var26 else 0)
                var30 = (1 if var6 == var12 else 0)
                var5 = var13
                while True:  # loop $label12
                    if (1 if (var29 | ((var30 | (1 if var5 == var13 else 0)) | (1 if var5 == var28 else 0))) == 0 else 0):
                        break
                    if (1 if var5 >= var8 else 0):
                        break
                    if (1 if (var5 | var6) < 0 else 0):
                        break
                    var10 = 1
                    var17 = ((var5 + var24) + 1)
                    var18 = 0
                    while True:  # loop $label11
                        var19 = (var14 + var18)
                        var2 = 0
                        var7 = 0
                        if (1 if var4 != 1 else 0):
                            while True:  # loop $label10
                                var10 = (((1 if i32_load((var16 + ((var19 + ((var17 + (var2 | 1)) * var15)) << 2))) == var3 else 0) & (1 if i32_load((var16 + ((var19 + ((var2 + var17) * var15)) << 2))) == var3 else 0)) & var10)
                                var2 = (var2 + 2)
                                var7 = (var7 + 2)
                                if (1 if (var7 + 2) != var22 else 0):
                                    continue
                                break  # end loop
                        if var23:
                            var10 = ((1 if i32_load((var16 + ((var19 + ((var2 + var17) * var15)) << 2))) == var3 else 0) & var10)
                        var18 = (var18 + 1)
                        if (1 if (var18 + 1) != var4 else 0):
                            continue
                        break  # end loop
                    if var10:
                        break
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) < var27 else 0):
                        continue
                    break  # end loop
            var6 = var14
            if (1 if var14 < var25 else 0):
                continue
            break  # end loop
        var11 = (1 if var9 < 39 else 0)
        var9 = (var9 + 1)
        if (1 if (var9 + 1) != 40 else 0):
            continue
        break  # end loop
    break
    i32_store(var0, var6)
    i32_store(var1, var5)
    return var11


# ==========================================================
# $func168
# ==========================================================
def func168(var0, var1):
    if (1 if var1 >= 1024 else 0):
        var0 = (var0 * 8.98846567431158e+307)
        if (1 if var1 < 2047 else 0):
            var1 = (var1 - 1023)
            break
        var0 = (var0 * 8.98846567431158e+307)
        var1 = ((3069 if (1 if var1 >= 3069 else 0) else var1) - 2046)
        break
    if (1 if var1 > -1023 else 0):
        break
    var0 = (var0 * 2.004168360008973e-292)
    if (1 if var1 > -1992 else 0):
        var1 = (var1 + 969)
        break
    var0 = (var0 * 2.004168360008973e-292)
    var1 = ((-2960 if (1 if var1 <= -2960 else 0) else var1) + 1938)
    return (var0 * f64_reinterpret_i64((i64_extend_u((var1 + 1023)) << 52)))


# ==========================================================
# $func180
# ==========================================================
def func180(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    if (1 if i32_load(38604) == var1 else 0):
        break
    if (1 if i32_load(38608) == var1 else 0):
        break
    if (1 if i32_load(38612) == var1 else 0):
        break
    if (1 if i32_load(38616) == var1 else 0):
        break
    if (1 if i32_load(38624) == var1 else 0):
        break
    if (1 if i32_load(38628) == var1 else 0):
        break
    if (1 if i32_load(38632) == var1 else 0):
        break
    if (1 if i32_load(39056) != var1 else 0):
        break
    var1 = (var0 + 281808)
    var2 = (i32_load(9561068) << 2)
    var3 = (i32_load(9561064) << 2)
    var4 = (i32_load(9561060) << 2)
    var5 = (i32_load(9561056) << 2)
    var6 = (i32_load(9561052) << 2)
    var7 = (i32_load(9561048) << 2)
    var8 = (i32_load(9561044) << 2)
    var9 = (i32_load(9561040) << 2)
    var0 = (var0 + 282828)
    return ((i32_load(((var0 + 281808) + (i32_load(9561068) << 2))) + ((i32_load((var1 + (i32_load(9561064) << 2))) + ((i32_load((var1 + (i32_load(9561060) << 2))) + ((i32_load((var1 + (i32_load(9561056) << 2))) + ((i32_load((var1 + (i32_load(9561052) << 2))) + ((i32_load((var1 + (i32_load(9561048) << 2))) + ((i32_load((var1 + (i32_load(9561044) << 2))) + (i32_load((var1 + (i32_load(9561040) << 2))) + i32_load(((var0 + 282828) + var9)))) + i32_load((var0 + var8)))) + i32_load((var0 + var7)))) + i32_load((var0 + var6)))) + i32_load((var0 + var5)))) + i32_load((var0 + var4)))) + i32_load((var0 + var3)))) + i32_load((var0 + var2)))
    var0 = (var0 + (var1 << 2))
    return (i32_load(((var0 + (var1 << 2)) + 282828)) + i32_load((var0 + 281808)))


# ==========================================================
# $func185
# ==========================================================
def func185(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    if (1 if (i32_load8_u(var0) & 15) == 0 else 0):
        return (10 & 10)
    var2 = i32_load(var0)
    var1 = global3
    var4 = i32_load(global3 + 24)
    var3 = i32_load(var0 + 4)
    var6 = (i32_load(var0 + 4) & 1073741823)
    if (1 if i32_load(global3 + 24) != (i32_load(var0 + 4) & 1073741823) else 0):
        break
    if (1 if (var2 & 8) == 0 else 0):
        break
    if (1 if i32_load(var0 + 20) >= 0 else 0):
        break
    i32_store(var0 + 20, 0)
    var3 = (var3 & 1073741824)
    break
    if (1 if (var2 & 3) != 1 else 0):
        break
    var5 = 6
    var1 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) > 2147483646 else 0):
        break
    i32_store(var0 + 20, (var1 + 1))
    break
    var5 = 56
    if (1 if var6 == 1073741823 else 0):
        break
    if var6:
        break
    if (0 if (var2 & 4) else var3):
        break
    if (var2 & 128):
        if (1 if i32_load(var1 + 80) == 0 else 0):
            i32_store(var1 + 80, -12)
        var6 = i32_load(var0 + 8)
        i32_store(var1 + 84, (var0 + 16))
    else:
    if (1 if ((var4 | -2147483648) if var6 else var4) == (var4 | (var3 & 1073741824)) else 0):
        break
    i32_store(var1 + 84, 0)
    if (1 if (var2 & 12) != 12 else 0):
        break
    if i32_load(var0 + 8):
        break
    break
    var2 = i32_load(var1 + 76)
    var5 = (var1 + 76)
    i32_store(var0 + 12, (var1 + 76))
    i32_store(var0 + 16, var2)
    var4 = (var0 + 16)
    if (1 if var2 != var5 else 0):
        i32_store((var2 - 4), var4)
    i32_store(var1 + 76, var4)
    var5 = 0
    i32_store(var1 + 84, 0)
    if (1 if var3 == 0 else 0):
        break
    i32_store(var0 + 20, 0)
    break
    return var5


# ==========================================================
# $func188
# ==========================================================
def func188():
    var0 = 0
    var0 = i32_load(52304)
    if (1 if i32_load(52304) != i32_load(52300) else 0):
        i32_store(9687288, 281)
        i32_store(9687284, 282)
        i32_store(9687296, 283)
        i32_store(9687316, 284)
        i32_store(9687292, 285)
        i32_store(9687300, 286)
        i32_store(9687304, 287)
        i32_store(9687308, 288)
        i32_store(9687312, 289)
        i32_store(9687320, 290)
        i32_store(9687324, 291)
        i32_store(9687328, 292)
        i32_store(52300, var0)

