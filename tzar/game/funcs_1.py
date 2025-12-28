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
# $func72
# ==========================================================
def func72(var0, var1):
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
    var8 = i32_load(var0 + 283848)
    i32_store(var1, i32_load(var0 + 283848))
    var9 = i32_load((var0 + 283852))
    i32_store(var1 + 4, i32_load((var0 + 283852)))
    var10 = i32_load((var0 + 283856))
    i32_store(var1 + 8, i32_load((var0 + 283856)))
    var2 = i32_load((var0 + 283860))
    i32_store(var1 + 12, i32_load((var0 + 283860)))
    var12 = i32_load(9142892)
    if (1 if i32_load(9142892) >= 2 else 0):
        var3 = i32_load(9561692)
        var11 = i32_load(9143016)
        var4 = 1
        while True:  # loop $label4
            var5 = var3
            var3 = var8
            var6 = var9
            var7 = var10
            var13 = var2
            var14 = (var4 * var12)
            var2 = ((var4 * var12) + i32_load(var0 + 283908))
            if (1 if (i32_load8_u((var11 + ((var4 * var12) + i32_load(var0 + 283908)))) & 1) == 0 else 0):
                break
            var8 = 2147483647
            if (1 if var3 == 2147483647 else 0):
                break
            var3 = i32_load((var5 + (var4 * 286704)) + 283848)
            var8 = (2147483647 if (1 if var3 == 2147483647 else 0) else (var3 + i32_load((var5 + (var4 * 286704)) + 283848)))
            i32_store(var1, (2147483647 if (1 if var3 == 2147483647 else 0) else (var3 + i32_load((var5 + (var4 * 286704)) + 283848))))
            var12 = i32_load(9142892)
            var14 = (i32_load(9142892) * var4)
            var2 = ((i32_load(9142892) * var4) + i32_load(var0 + 283908))
            var3 = i32_load(9561692)
            var2 = i32_load8_u((var2 + var11))
            if (1 if (i32_load8_u((var2 + var11)) & 2) == 0 else 0):
                break
            var9 = 2147483647
            if (1 if var6 == 2147483647 else 0):
                break
            var6 = i32_load(((var5 + (var4 * 286704)) + 283852))
            var9 = (2147483647 if (1 if var6 == 2147483647 else 0) else (var6 + i32_load(((var5 + (var4 * 286704)) + 283852))))
            i32_store(var1 + 4, (2147483647 if (1 if var6 == 2147483647 else 0) else (var6 + i32_load(((var5 + (var4 * 286704)) + 283852)))))
            var2 = i32_load8_u((var11 + (var14 + i32_load(var0 + 283908))))
            if (1 if (var2 & 4) == 0 else 0):
                break
            var10 = 2147483647
            if (1 if var7 == 2147483647 else 0):
                break
            var7 = i32_load(((var5 + (var4 * 286704)) + 283856))
            var10 = (2147483647 if (1 if var7 == 2147483647 else 0) else (var7 + i32_load(((var5 + (var4 * 286704)) + 283856))))
            i32_store(var1 + 8, (2147483647 if (1 if var7 == 2147483647 else 0) else (var7 + i32_load(((var5 + (var4 * 286704)) + 283856)))))
            var2 = i32_load8_u((var11 + (var14 + i32_load(var0 + 283908))))
            if (1 if (var2 & 8) == 0 else 0):
                var2 = var13
                break
            var2 = 2147483647
            if (1 if var13 == 2147483647 else 0):
                break
            var5 = i32_load(((var5 + (var4 * 286704)) + 283860))
            var2 = (2147483647 if (1 if var5 == 2147483647 else 0) else (i32_load(((var5 + (var4 * 286704)) + 283860)) + var13))
            i32_store(var1 + 12, (2147483647 if (1 if var5 == 2147483647 else 0) else (i32_load(((var5 + (var4 * 286704)) + 283860)) + var13)))
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < var12 else 0):
                continue
            break  # end loop
    return var5


# ==========================================================
# $func73
# ==========================================================
def func73(var0, var1, var2, var3, var4, var5):
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
    var7 = i32_load(var2 + 216)
    var16 = i32_load(var2 + 208)
    var11 = i32_load(var2 + 372)
    if (1 if var5 == 0 else 0):
        break
    if (1 if var7 <= 0 else 0):
        break
    var9 = (i32_load(var2 + 220) + var1)
    if (1 if (i32_load(var2 + 220) + var1) <= var1 else 0):
        break
    var17 = (var0 + var7)
    var10 = i32_load(9142440)
    var13 = (i32_load(9142440) + 2)
    var18 = ((i32_load(9142440) + 2) * var16)
    var14 = i32_load(var2 + 212)
    var15 = i32_load(9142840)
    if (1 if i32_load(var2 + 264) == 1 else 0):
        var6 = var0
        while True:  # loop $label6
            var8 = (var6 + 1)
            var12 = (var6 - var0)
            var5 = var1
            if (1 if var6 >= var10 else 0):
                while True:  # loop $label1
                    if i32_load8_u((var11 + (var12 + ((var5 - var1) * var7)))):
                        return 0
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var9 else 0):
                        continue
                    break
                    break  # end loop
                raise RuntimeError('unreachable')
            while True:  # loop $label5
                if (1 if i32_load8_u((var11 + (var12 + ((var5 - var1) * var7)))) == 0 else 0):
                    var5 = (var5 + 1)
                    break
                if (1 if var5 >= var10 else 0):
                    break
                if (1 if (var5 | var6) < 0 else 0):
                    break
                var5 = (var5 + 1)
                if (1 if i32_load((var15 + ((((var18 + (var5 + 1)) * var13) + var8) << 2))) != var14 else 0):
                    break
                if (1 if i32_load((var15 + (((var5 * var13) + var8) << 2))) != var14 else 0):
                    break
                if (1 if var5 != var9 else 0):
                    continue
                break  # end loop
            var6 = var8
            if (1 if var8 < var17 else 0):
                continue
            break  # end loop
        break
    var6 = var0
    while True:  # loop $label11
        var8 = (var6 + 1)
        var12 = (var6 - var0)
        var5 = var1
        if (1 if var6 < var10 else 0):
            while True:  # loop $label8
                if (1 if i32_load8_u((var11 + (var12 + ((var5 - var1) * var7)))) == 0 else 0):
                    var5 = (var5 + 1)
                    break
                if (1 if var5 >= var10 else 0):
                    break
                if (1 if (var5 | var6) < 0 else 0):
                    break
                var5 = (var5 + 1)
                if (1 if i32_load((var15 + ((((var18 + (var5 + 1)) * var13) + var8) << 2))) != var14 else 0):
                    break
                if (1 if var5 != var9 else 0):
                    continue
                break
                break  # end loop
            raise RuntimeError('unreachable')
        while True:  # loop $label10
            if (1 if i32_load8_u((var11 + (var12 + ((var5 - var1) * var7)))) == 0 else 0):
                var5 = (var5 + 1)
                if (1 if var9 != (var5 + 1) else 0):
                    continue
                break
            break  # end loop
        return 0
        var6 = var8
        if (1 if var8 < var17 else 0):
            continue
        break  # end loop
    var19 = 1
    if (1 if var3 == 0 else 0):
        break
    if (1 if var7 <= 0 else 0):
        break
    var3 = (i32_load(var2 + 220) + var1)
    if (1 if (i32_load(var2 + 220) + var1) <= var1 else 0):
        break
    var6 = (var0 + var7)
    var5 = var0
    while True:  # loop $label14
        var2 = (var5 + 1)
        var8 = (var5 - var0)
        var9 = i32_load(9142840)
        var5 = var1
        while True:  # loop $label13
            if (1 if i32_load8_u((var11 + (var8 + ((var5 - var1) * var7)))) == 0 else 0):
                var5 = (var5 + 1)
                break
            var5 = (var5 + 1)
            var10 = (i32_load(9142440) + 2)
            i32_store((var9 + ((var2 + (((var5 + 1) + ((i32_load(9142440) + 2) * var16)) * var10)) << 2)), var4)
            if (1 if var3 != var5 else 0):
                continue
            break  # end loop
        var5 = var2
        if (1 if var2 < var6 else 0):
            continue
        break  # end loop
    return var19


# ==========================================================
# $func79
# ==========================================================
def func79(var0, var1, var2):
    var3 = 0
    if (1 if var2 == 0 else 0):
        return (1 if i32_load(var0 + 4) == i32_load(var1 + 4) else 0)
    if (1 if var0 == var1 else 0):
        return 1
    var2 = i32_load(var1 + 4)
    var1 = i32_load8_u(i32_load(var1 + 4))
    var3 = i32_load(var0 + 4)
    var0 = i32_load8_u(i32_load(var0 + 4))
    if (1 if i32_load8_u(i32_load(var0 + 4)) == 0 else 0):
        break
    if (1 if var0 != var1 else 0):
        break
    while True:  # loop $label1
        var1 = i32_load8_u(var2 + 1)
        var0 = i32_load8_u(var3 + 1)
        if (1 if i32_load8_u(var3 + 1) == 0 else 0):
            break
        var2 = (var2 + 1)
        var3 = (var3 + 1)
        if (1 if var0 == var1 else 0):
            continue
        break  # end loop
    return (1 if var0 == var1 else 0)


# ==========================================================
# $func84
# ==========================================================
def func84(var0, var1, var2, var3, var4, var5, var6):
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
    if (1 if var3 > 0 else 0):
        var17 = ((var4 << 1) | 1)
        var18 = (var1 * 3)
        var19 = (0 - var1)
        var20 = (var1 * -3)
        var21 = (0 - (var1 << 2))
        var22 = (var1 << 1)
        var23 = (0 - (var1 << 1))
        var24 = i32_load(16076)
        var10 = i32_load(17088)
        var11 = i32_load(16308)
        var8 = i32_load(17616)
        while True:  # loop $label2
            var4 = var3
            var25 = (var0 + var23)
            var9 = i32_load8_u((var0 + var23))
            var12 = (var0 + var1)
            var14 = i32_load8_u((var0 + var1))
            var15 = (i32_load8_u((var0 + var23)) - i32_load8_u((var0 + var1)))
            var16 = (var0 + var19)
            var3 = i32_load8_u((var0 + var19))
            var13 = i32_load8_u(var0)
            if (1 if (i32_load8_u((var8 + (i32_load8_u((var0 + var23)) - i32_load8_u((var0 + var1))))) + (i32_load8_u((var8 + (i32_load8_u((var0 + var19)) - i32_load8_u(var0)))) << 2)) > var17 else 0):
                break
            var7 = i32_load8_u((var0 + var20))
            if (1 if i32_load8_u((var8 + (i32_load8_u((var0 + var21)) - i32_load8_u((var0 + var20))))) > var5 else 0):
                break
            if (1 if i32_load8_u((var8 + (var7 - var9))) > var5 else 0):
                break
            var26 = i32_load8_u((var8 + (var9 - var3)))
            if (1 if i32_load8_u((var8 + (var9 - var3))) > var5 else 0):
                break
            var7 = i32_load8_u((var0 + var22))
            if (1 if i32_load8_u((var8 + (i32_load8_u((var0 + var18)) - i32_load8_u((var0 + var22))))) > var5 else 0):
                break
            if (1 if i32_load8_u((var8 + (var7 - var14))) > var5 else 0):
                break
            var27 = i32_load8_u((var8 + (var14 - var13)))
            if (1 if i32_load8_u((var8 + (var14 - var13))) > var5 else 0):
                break
            var7 = ((var13 - var3) * 3)
            if (1 if ((1 if var6 >= var26 else 0) & (1 if var6 >= var27 else 0)) == 0 else 0):
                var12 = (var7 + i32_load8_s((var15 + var24)))
                var9 = i32_load8_s((var11 + (((var7 + i32_load8_s((var15 + var24))) + 4) >> 3)))
                i32_store8(var16, i32_load8_u((var10 + (i32_load8_s((var11 + ((var12 + 3) >> 3))) + var3))))
                var12 = var0
                break
            var15 = i32_load8_s((var11 + ((var7 + 3) >> 3)))
            var9 = i32_load8_s((var11 + ((var7 + 4) >> 3)))
            var7 = ((i32_load8_s((var11 + ((var7 + 4) >> 3))) + 1) >> 1)
            i32_store8(var25, i32_load8_u((var10 + (var9 + ((i32_load8_s((var11 + ((var7 + 4) >> 3))) + 1) >> 1)))))
            i32_store8(var16, i32_load8_u((var10 + (var3 + var15))))
            i32_store8(var0, i32_load8_u((var10 + (var13 - var9))))
            var3 = (var14 - var7)
            i32_store8(var12, i32_load8_u((var3 + var10)))
            var3 = (var4 - 1)
            var0 = (var0 + var2)
            if (1 if var4 > 1 else 0):
                continue
            break  # end loop
    return (var13 - var9)

