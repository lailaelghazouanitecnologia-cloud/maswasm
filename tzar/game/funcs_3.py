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
# $func93
# ==========================================================
def func93(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var6 = (var1 - 1)
    var7 = (var0 - 1)
    var3 = i32_load(var2 + 216)
    if (1 if ((1 if var0 > 0 else 0) & (1 if var1 > 0 else 0)) == 0 else 0):
        var5 = i32_load(var2 + 220)
        break
    var5 = i32_load(var2 + 220)
    if (1 if var3 <= var7 else 0):
        break
    if (1 if var5 <= var6 else 0):
        break
    if i32_load8_u(var2 + 377):
        break
    if i32_load8_u((i32_load(var2 + 372) + ((var3 * var6) + var7))):
        break
    var4 = ((1 if var1 > 0 else 0) & (1 if var0 >= 0 else 0))
    if i32_load8_u(var2 + 377):
        if (1 if var4 == 0 else 0):
            break
        if (1 if var0 >= var3 else 0):
            break
        var4 = 1
        if (1 if var5 > var6 else 0):
            break
        if (1 if var0 <= 0 else 0):
            break
        if (1 if var1 < 2 else 0):
            break
        if (1 if var3 <= var7 else 0):
            break
        var4 = 1
        if (1 if (var1 - 2) < var5 else 0):
            break
        if (1 if var0 < 2 else 0):
            break
        var4 = 1
        if (1 if var1 <= 0 else 0):
            break
        if (1 if (var0 - 2) >= var3 else 0):
            break
        if (1 if var5 > var6 else 0):
            break
        if (1 if var0 <= 0 else 0):
            break
        if (1 if var1 < 0 else 0):
            break
        if (1 if var3 <= var7 else 0):
            break
        var4 = 1
        if (1 if var1 < var5 else 0):
            break
        if (1 if var0 < 0 else 0):
            break
        if (1 if var1 < 2 else 0):
            break
        if (1 if var0 >= var3 else 0):
            break
        var4 = 1
        if (1 if (var1 - 2) < var5 else 0):
            break
        var2 = (1 if var0 < 2 else 0)
        if (1 if var0 < 2 else 0):
            break
        if (1 if var1 < 2 else 0):
            break
        if (1 if (var0 - 2) >= var3 else 0):
            break
        var4 = 1
        if (1 if (var1 - 2) < var5 else 0):
            break
        if var2:
            break
        if (1 if var1 < 0 else 0):
            break
        if (1 if (var0 - 2) >= var3 else 0):
            break
        var4 = 1
        if (1 if var1 < var5 else 0):
            break
        if (1 if (var0 | var1) < 0 else 0):
            break
        if (1 if var0 >= var3 else 0):
            break
        var4 = 1
        if (1 if var1 >= var5 else 0):
            break
        break
    var2 = i32_load(var2 + 372)
    if (1 if var4 == 0 else 0):
        break
    if (1 if var0 >= var3 else 0):
        break
    if (1 if var5 <= var6 else 0):
        break
    var4 = 1
    if i32_load8_u((var2 + ((var3 * var6) + var0))):
        break
    var8 = (var1 - 2)
    if (1 if var0 <= 0 else 0):
        break
    if (1 if var1 < 2 else 0):
        break
    if (1 if var3 <= var7 else 0):
        break
    if (1 if var5 <= var8 else 0):
        break
    var4 = 1
    if i32_load8_u((var2 + ((var3 * var8) + var7))):
        break
    var9 = (var0 - 2)
    if (1 if var0 < 2 else 0):
        break
    if (1 if var1 <= 0 else 0):
        break
    if (1 if var3 <= var9 else 0):
        break
    if (1 if var5 <= var6 else 0):
        break
    var4 = 1
    if i32_load8_u((var2 + ((var3 * var6) + var9))):
        break
    if (1 if var0 <= 0 else 0):
        break
    if (1 if var1 < 0 else 0):
        break
    if (1 if var3 <= var7 else 0):
        break
    if (1 if var1 >= var5 else 0):
        break
    var4 = 1
    if i32_load8_u((var2 + ((var1 * var3) + var7))):
        break
    if (1 if var0 < 0 else 0):
        break
    if (1 if var1 < 2 else 0):
        break
    if (1 if var0 >= var3 else 0):
        break
    if (1 if var5 <= var8 else 0):
        break
    var4 = 1
    if i32_load8_u((var2 + ((var3 * var8) + var0))):
        break
    var6 = (1 if var0 < 2 else 0)
    if (1 if var0 < 2 else 0):
        break
    if (1 if var1 < 2 else 0):
        break
    if (1 if var3 <= var9 else 0):
        break
    if (1 if var5 <= var8 else 0):
        break
    var4 = 1
    if i32_load8_u((var2 + ((var3 * var8) + var9))):
        break
    if var6:
        break
    if (1 if var1 < 0 else 0):
        break
    if (1 if var3 <= var9 else 0):
        break
    if (1 if var1 >= var5 else 0):
        break
    var4 = 1
    if i32_load8_u((var2 + ((var1 * var3) + var9))):
        break
    if (1 if (var0 | var1) < 0 else 0):
        break
    if (1 if var0 >= var3 else 0):
        break
    if (1 if var1 >= var5 else 0):
        break
    var4 = 1
    if i32_load8_u((var2 + ((var1 * var3) + var0))):
        break
    var4 = 0
    return var4


# ==========================================================
# $func98
# ==========================================================
def func98(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    if (1 if var2 >= 512 else 0):
        # Unknown: i32.extend8_s []
        # Unknown: memory.fill []
        return
    if (1 if var2 == 0 else 0):
        break
    i32_store8(var0, var1)
    var3 = (var0 + var2)
    i32_store8(((var0 + var2) - 1), var1)
    if (1 if var2 < 3 else 0):
        break
    i32_store8(var0 + 2, var1)
    i32_store8(var0 + 1, var1)
    i32_store8((var3 - 3), var1)
    i32_store8((var3 - 2), var1)
    if (1 if var2 < 7 else 0):
        break
    i32_store8(var0 + 3, var1)
    i32_store8((var3 - 4), var1)
    if (1 if var2 < 9 else 0):
        break
    var4 = ((0 - var0) & 3)
    var3 = (var0 + ((0 - var0) & 3))
    var0 = ((var1 & 255) * 16843009)
    i32_store((var0 + ((0 - var0) & 3)), ((var1 & 255) * 16843009))
    var2 = ((var2 - var4) & -4)
    var1 = (var3 + ((var2 - var4) & -4))
    i32_store(((var3 + ((var2 - var4) & -4)) - 4), var0)
    if (1 if var2 < 9 else 0):
        break
    i32_store(var3 + 8, var0)
    i32_store(var3 + 4, var0)
    i32_store((var1 - 8), var0)
    i32_store((var1 - 12), var0)
    if (1 if var2 < 25 else 0):
        break
    i32_store(var3 + 24, var0)
    i32_store(var3 + 20, var0)
    i32_store(var3 + 16, var0)
    i32_store(var3 + 12, var0)
    i32_store((var1 - 16), var0)
    i32_store((var1 - 20), var0)
    i32_store((var1 - 24), var0)
    i32_store((var1 - 28), var0)
    var2 = ((var3 & 4) | 24)
    var1 = (var2 - ((var3 & 4) | 24))
    if (1 if (var2 - ((var3 & 4) | 24)) < 32 else 0):
        break
    var5 = (i64_extend_u(var0) * 4294967297)
    var0 = (var2 + var3)
    while True:  # loop $label1
        i64_store(var0 + 24, var5)
        i64_store(var0 + 16, var5)
        i64_store(var0 + 8, var5)
        i64_store(var0, var5)
        var0 = (var0 + 32)
        var1 = (var1 - 32)
        if (1 if (var1 - 32) > 31 else 0):
            continue
        break  # end loop


# ==========================================================
# $func108
# ==========================================================
def func108(var0, var1, var2, var3):
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
    var3 = ((var3 << 1) | 1)
    var12 = (((((var3 << 1) | 1) * var3) << 1) - 2)
    if (((((var3 << 1) | 1) * var3) << 1) - 2):
        var6 = (i32_load(9142892) * var2)
        var11 = i32_load(9142440)
        var3 = (i32_load(9142440) + 2)
        var13 = ((i32_load(9142440) + 2) << 1)
        var7 = i32_load(9143004)
        var8 = i32_load(9671128)
        var9 = i32_load(9142840)
        var2 = 0
        while True:  # loop $label3
            var4 = (var2 << 2)
            var5 = (i32_load((((var2 << 2) | 4) + 8611904)) + var1)
            if (1 if var11 <= (i32_load((((var2 << 2) | 4) + 8611904)) + var1) else 0):
                break
            var4 = (i32_load((var4 + 8611904)) + var0)
            if (1 if var11 <= (i32_load((var4 + 8611904)) + var0) else 0):
                break
            if (1 if (var4 | var5) < 0 else 0):
                break
            var4 = (var4 + 1)
            var5 = (var5 + 1)
            var10 = i32_load16_u((var8 + (i32_load((var9 + (((var4 + 1) + ((var5 + 1) * var3)) << 2))) * 132)) + 110)
            if (1 if i32_load16_u((var8 + (i32_load((var9 + (((var4 + 1) + ((var5 + 1) * var3)) << 2))) * 132)) + 110) == 0 else 0):
                break
            if (1 if i32_load8_u((var7 + (var6 + var10))) == 0 else 0):
                break
            return 0
            var10 = i32_load16_u((var8 + (i32_load((var9 + ((var4 + ((var3 + var5) * var3)) << 2))) * 132)) + 110)
            if (1 if i32_load16_u((var8 + (i32_load((var9 + ((var4 + ((var3 + var5) * var3)) << 2))) * 132)) + 110) == 0 else 0):
                break
            if (1 if i32_load8_u((var7 + (var6 + var10))) == 0 else 0):
                break
            return 0
            var5 = i32_load16_u((var8 + (i32_load((var9 + ((var4 + ((var5 + var13) * var3)) << 2))) * 132)) + 110)
            if (1 if i32_load16_u((var8 + (i32_load((var9 + ((var4 + ((var5 + var13) * var3)) << 2))) * 132)) + 110) == 0 else 0):
                break
            if (1 if i32_load8_u((var7 + (var5 + var6))) == 0 else 0):
                break
            return 0
            var2 = (var2 + 2)
            if (1 if (var2 + 2) < var12 else 0):
                continue
            break  # end loop
    return 1


# ==========================================================
# $func137
# ==========================================================
def func137(var0, var1, var2, var3, var4, var5, var6):
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
    if (1 if var3 > 0 else 0):
        var19 = ((var4 << 1) | 1)
        var20 = (var1 * 3)
        var21 = (0 - var1)
        var22 = (var1 * -3)
        var23 = (0 - (var1 << 2))
        var24 = (var1 << 1)
        var25 = (0 - (var1 << 1))
        var15 = i32_load(16308)
        var9 = i32_load(17088)
        var16 = i32_load(16076)
        var7 = i32_load(17616)
        while True:  # loop $label2
            var4 = var3
            var26 = (var0 + var25)
            var10 = i32_load8_u((var0 + var25))
            var27 = (var0 + var1)
            var14 = i32_load8_u((var0 + var1))
            var8 = (i32_load8_u((var0 + var25)) - i32_load8_u((var0 + var1)))
            var17 = (var0 + var21)
            var3 = i32_load8_u((var0 + var21))
            var11 = i32_load8_u(var0)
            if (1 if (i32_load8_u((var7 + (i32_load8_u((var0 + var25)) - i32_load8_u((var0 + var1))))) + (i32_load8_u((var7 + (i32_load8_u((var0 + var21)) - i32_load8_u(var0)))) << 2)) > var19 else 0):
                break
            var28 = (var0 + var22)
            var12 = i32_load8_u((var0 + var22))
            if (1 if i32_load8_u((var7 + (i32_load8_u((var0 + var23)) - i32_load8_u((var0 + var22))))) > var5 else 0):
                break
            if (1 if i32_load8_u((var7 + (var12 - var10))) > var5 else 0):
                break
            var29 = i32_load8_u((var7 + (var10 - var3)))
            if (1 if i32_load8_u((var7 + (var10 - var3))) > var5 else 0):
                break
            var13 = (var0 + var24)
            var18 = i32_load8_u((var0 + var24))
            if (1 if i32_load8_u((var7 + (i32_load8_u((var0 + var20)) - i32_load8_u((var0 + var24))))) > var5 else 0):
                break
            if (1 if i32_load8_u((var7 + (var18 - var14))) > var5 else 0):
                break
            var30 = i32_load8_u((var7 + (var14 - var11)))
            if (1 if i32_load8_u((var7 + (var14 - var11))) > var5 else 0):
                break
            var8 = (i32_load8_s((var8 + var16)) + ((var11 - var3) * 3))
            if (1 if ((1 if var6 >= var29 else 0) & (1 if var6 >= var30 else 0)) == 0 else 0):
                var13 = i32_load8_s((var15 + ((var8 + 4) >> 3)))
                i32_store8(var17, i32_load8_u((var9 + (i32_load8_s((var15 + ((var8 + 3) >> 3))) + var3))))
                var3 = (var11 - var13)
                var13 = var0
                break
            var8 = i32_load8_s((var8 + var16))
            var12 = (((i32_load8_s((var8 + var16)) * 9) + 63) >> 7)
            i32_store8(var28, i32_load8_u((var9 + (var12 + (((i32_load8_s((var8 + var16)) * 9) + 63) >> 7)))))
            var10 = (((var8 * 18) + 63) >> 7)
            i32_store8(var26, i32_load8_u((var9 + (var10 + (((var8 * 18) + 63) >> 7)))))
            var3 = (((var8 * 27) + 63) >> 7)
            i32_store8(var17, i32_load8_u((var9 + (var3 + (((var8 * 27) + 63) >> 7)))))
            i32_store8(var0, i32_load8_u((var9 + (var11 - var3))))
            i32_store8(var27, i32_load8_u((var9 + (var14 - var10))))
            var3 = (var18 - var12)
            i32_store8(var13, i32_load8_u((var3 + var9)))
            var3 = (var4 - 1)
            var0 = (var0 + var2)
            if (1 if var4 > 1 else 0):
                continue
            break  # end loop

