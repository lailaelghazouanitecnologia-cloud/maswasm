"""
Auto-generated from WAT. Contains 3 functions.
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
# $func193
# ==========================================================
def func193(var0, var1, var2, var3, var4, var5, var6, var7):
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
    var10 = i32_load(var2 + 216)
    var18 = i32_load(var2 + 208)
    var19 = i32_load(var2 + 372)
    if (1 if var6 == 0 else 0):
        break
    if (1 if var10 <= 0 else 0):
        break
    var12 = (i32_load(var2 + 220) + var1)
    if (1 if (i32_load(var2 + 220) + var1) <= var1 else 0):
        break
    var20 = (var0 + var10)
    var13 = i32_load(9142440)
    var14 = (i32_load(9142440) + 2)
    var21 = ((i32_load(9142440) + 2) * var18)
    var22 = i32_load(38472)
    var24 = i32_load(38600)
    var25 = i32_load(9671128)
    var15 = i32_load(var2 + 212)
    var16 = i32_load(9142840)
    var9 = var0
    while True:  # loop $label6
        var11 = (var9 + 1)
        var17 = (var9 - var0)
        var6 = var1
        var8 = var1
        if (1 if var9 < var13 else 0):
            while True:  # loop $label3
                if (1 if i32_load8_u((var19 + (var17 + ((var6 - var1) * var10)))) == 0 else 0):
                    var6 = (var6 + 1)
                    break
                var8 = 0
                if (1 if var6 >= var13 else 0):
                    break
                if (1 if (var6 | var9) < 0 else 0):
                    break
                var6 = (var6 + 1)
                var23 = i32_load((var16 + ((((var21 + (var6 + 1)) * var14) + var11) << 2)))
                if (1 if var15 != i32_load((var16 + ((((var21 + (var6 + 1)) * var14) + var11) << 2))) else 0):
                    var23 = (var25 + (var23 * 132))
                    var26 = i32_load8_u((var25 + (var23 * 132)) + 122)
                    if (1 if ((1 if var24 == i32_load8_u((var25 + (var23 * 132)) + 122) else 0) | (1 if var22 == var26 else 0)) == 0 else 0):
                        break
                    if (1 if i32_load16_u(var23 + 110) != var3 else 0):
                        break
                if (1 if i32_load((var16 + (((var6 * var14) + var11) << 2))) != var15 else 0):
                    break
                if (1 if var6 != var12 else 0):
                    continue
                break
                break  # end loop
            raise RuntimeError('unreachable')
        while True:  # loop $label5
            if (1 if i32_load8_u((var19 + (var17 + ((var8 - var1) * var10)))) == 0 else 0):
                var8 = (var8 + 1)
                if (1 if var12 != (var8 + 1) else 0):
                    continue
                break
            break  # end loop
        var8 = 0
        break
        var9 = var11
        if (1 if var11 < var20 else 0):
            continue
        break  # end loop
    var8 = 1
    if (1 if var4 == 0 else 0):
        break
    if (1 if var10 <= 0 else 0):
        break
    var11 = i32_load(var2 + 220)
    var13 = (i32_load(var2 + 220) + var1)
    if (1 if (i32_load(var2 + 220) + var1) <= var1 else 0):
        break
    var2 = (1 if var11 > 1 else 0)
    var14 = (3 if (1 if var11 > 1 else 0) else 4)
    var15 = (1 if var2 else 2)
    var16 = (var0 + var10)
    var2 = 0
    var17 = (1 if var7 != 8 else 0)
    var6 = var0
    while True:  # loop $label11
        var4 = (var6 + 1)
        var20 = (var6 - var0)
        var6 = var1
        var8 = var2
        while True:  # loop $label10
            if (1 if i32_load8_u((var19 + (var20 + ((var6 - var1) * var10)))) == 0 else 0):
                break
            if var17:
                break
            if (1 if var8 < var15 else 0):
                break
            if (1 if var8 <= var14 else 0):
                break
            var21 = (var6 + 1)
            var7 = (i32_load(9142440) + 2)
            var7 = ((((var6 + 1) + ((i32_load(9142440) + 2) * var18)) * var7) + var4)
            var9 = i32_load(9142840)
            if (1 if var5 == 0 else 0):
                break
            var12 = (i32_load(9671128) + (i32_load((var9 + (var7 << 2))) * 132))
            var22 = i32_load8_u((i32_load(9671128) + (i32_load((var9 + (var7 << 2))) * 132)) + 122)
            if (1 if ((1 if i32_load8_u((i32_load(9671128) + (i32_load((var9 + (var7 << 2))) * 132)) + 122) == i32_load(38600) else 0) | (1 if i32_load(38472) == var22 else 0)) == 0 else 0):
                break
            if (1 if i32_load16_u(var12 + 110) != var3 else 0):
                break
            var7 = (i32_load(9142440) + 2)
            var7 = (((((i32_load(9142440) + 2) * var18) + var21) * var7) + var4)
            var9 = i32_load(9142840)
            i32_store((var9 + (var7 << 2)), var5)
            var8 = (var8 + 1)
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != var13 else 0):
                continue
            break  # end loop
        var2 = (var2 + var11)
        var6 = var4
        if (1 if var4 < var16 else 0):
            continue
        break  # end loop
    return 1
    return var8


# ==========================================================
# $func283
# ==========================================================
def func283(var0, var1, var2, var3, var4, var5, var6):
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
    var9 = i32_load(var2 + 216)
    var14 = i32_load(var2 + 208)
    if (1 if var5 == 0 else 0):
        break
    if (1 if var9 <= 0 else 0):
        break
    var8 = (var0 + var9)
    var13 = (i32_load(var2 + 220) + var1)
    if (1 if var1 < (i32_load(var2 + 220) + var1) else 0):
        var11 = i32_load(9142440)
        var15 = (i32_load(9142440) + 2)
        var16 = ((i32_load(9142440) + 2) * var14)
        var17 = i32_load(9142840)
        var7 = var0
        while True:  # loop $label2
            if (1 if var7 >= var11 else 0):
                break
            var10 = (var7 + 1)
            var5 = var1
            while True:  # loop $label3
                if (1 if var5 == var13 else 0):
                    var7 = var10
                    if (1 if var10 < var8 else 0):
                        continue
                    break
                if (1 if var5 >= var11 else 0):
                    break
                if (1 if (var5 | var7) < 0 else 0):
                    break
                var5 = (var5 + 1)
                if (1 if i32_load((var17 + ((var10 + ((var16 + (var5 + 1)) * var15)) << 2))) <= 2 else 0):
                    continue
                break  # end loop
            break  # end loop
        break
    var5 = var0
    while True:  # loop $label4
        var5 = (var5 + 1)
        if (1 if (var5 + 1) < var8 else 0):
            continue
        break  # end loop
    var12 = 1
    if (1 if var3 == 0 else 0):
        break
    if (1 if var9 <= 0 else 0):
        break
    var11 = (i32_load(var2 + 220) + var1)
    if (1 if (i32_load(var2 + 220) + var1) <= var1 else 0):
        break
    var12 = (var0 + var9)
    var5 = var0
    while True:  # loop $label10
        var7 = (var5 + 1)
        var10 = (var5 - var0)
        var5 = var1
        while True:  # loop $label9
            if (1 if var4 != i32_load(var2 + 212) else 0):
                if var6:
                    if (1 if i32_load8_u((i32_load(var2 + 372) + (var10 + ((var5 - var1) * var9)))) == 0 else 0):
                        break
                var5 = (var5 + 1)
                var3 = (i32_load(9142440) + 2)
                i32_store((i32_load(9142840) + ((var7 + (((var5 + 1) + ((i32_load(9142440) + 2) * var14)) * var3)) << 2)), var4)
                break
                var5 = (var5 + 1)
                var3 = (i32_load(9142440) + 2)
                var3 = (i32_load(9142840) + ((var7 + (((var5 + 1) + (i32_load(9142440) + 2)) * var3)) << 2))
                if (1 if i32_load((i32_load(9142840) + ((var7 + (((var5 + 1) + (i32_load(9142440) + 2)) * var3)) << 2))) > 2 else 0):
                    break
                i32_store(var3, 0)
                break
            if (1 if var6 == 0 else 0):
                var3 = (var5 + 1)
                break
            var3 = (var5 + 1)
            var8 = (i32_load(9142440) + 2)
            var8 = i32_load((i32_load(9142840) + ((var7 + (((var5 + 1) + (i32_load(9142440) + 2)) * var8)) << 2)))
            if (1 if i32_load((i32_load(9142840) + ((var7 + (((var5 + 1) + (i32_load(9142440) + 2)) * var8)) << 2))) < 3 else 0):
                break
            if i32_load8_u((i32_load(var2 + 372) + (var10 + ((var5 - var1) * var9)))):
                break
            var13 = i32_load(9142840)
            var5 = (i32_load(9142440) + 2)
            var8 = (i32_load(9142840) + (((((i32_load(9142440) + 2) + var3) * var5) + var7) << 2))
            if (1 if i32_load((var13 + (((var3 * var5) + var7) << 2))) != 1 else 0):
                i32_store(var8, 0)
                break
            i32_store(var8, 1)
            var5 = var3
            if (1 if var5 != var11 else 0):
                continue
            break  # end loop
        var5 = var7
        if (1 if var7 < var12 else 0):
            continue
        break  # end loop
    var12 = 1
    return var12


# ==========================================================
# $func304
# ==========================================================
def func304(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    # br_table ['$label0', '$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label0', '$label2']
    _br_idx = (i32_load8_u(var0 + 125) - 4)
    break  # br_table
    return
    i32_store8(var0 + 125, 0)
    var3 = i32_load(9561692)
    var5 = i32_load16_u(var0 + 110)
    var2 = (i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704))
    var7 = i32_load(9215884)
    var1 = i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 12)
    i32_store((((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + (i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 12) << 2)) + 282828), 0)
    var1 = ((var1 * 404) + 9568164)
    var4 = i32_load(var2 + 283848)
    if (1 if i32_load(var2 + 283848) != 2147483647 else 0):
        i32_store((var2 + 283848), (i32_load(var1) + var4))
    var2 = (var2 + 283852)
    var4 = i32_load((var2 + 283852))
    if (1 if i32_load((var2 + 283852)) != 2147483647 else 0):
        i32_store(var2, (i32_load(var1 + 4) + var4))
    var2 = (var3 + (var5 * 286704))
    var4 = ((var3 + (var5 * 286704)) + 283856)
    var6 = i32_load(((var3 + (var5 * 286704)) + 283856))
    if (1 if i32_load(((var3 + (var5 * 286704)) + 283856)) != 2147483647 else 0):
        i32_store(var4, (i32_load(var1 + 8) + var6))
    var2 = (var2 + 283860)
    var4 = i32_load((var2 + 283860))
    if (1 if i32_load((var2 + 283860)) != 2147483647 else 0):
        i32_store(var2, (i32_load(var1 + 12) + var4))
    var2 = (var3 + (var5 * 286704))
    var3 = ((var3 + (var5 * 286704)) + 281692)
    i32_store(((var3 + (var5 * 286704)) + 281692), (i32_load(var3) - i32_load(var1)))
    var3 = (var2 + 281696)
    i32_store((var2 + 281696), (i32_load(var3) - i32_load(var1 + 4)))
    var3 = (var2 + 281700)
    i32_store((var2 + 281700), (i32_load(var3) - i32_load(var1 + 8)))
    var3 = i32_load(var1 + 12)
    var1 = 1
    i32_store8(var2 + 286701, 1)
    var5 = (var2 + 281704)
    i32_store((var2 + 281704), (i32_load(var5) - var3))
    var3 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var6 = (var3 - 1)
    var8 = ((var3 - 1) & 1)
    var2 = (i32_load(var2 + 283908) * var3)
    var5 = i32_load(9561692)
    var4 = i32_load(9143016)
    if (1 if var3 != 2 else 0):
        var6 = (var6 & -2)
        var3 = 0
        while True:  # loop $label4
            if i32_load8_u((var4 + (var1 + var2))):
                i32_store8((var5 + (var1 * 286704)) + 286701, 1)
            var9 = (var1 + 1)
            if i32_load8_u((var4 + ((var1 + 1) + var2))):
                i32_store8((var5 + (var9 * 286704)) + 286701, 1)
            var1 = (var1 + 2)
            var3 = (var3 + 2)
            if (1 if (var3 + 2) != var6 else 0):
                continue
            break  # end loop
    if (1 if var8 == 0 else 0):
        break
    if (1 if i32_load8_u((var4 + (var1 + var2))) == 0 else 0):
        break
    i32_store8((var5 + (var1 * 286704)) + 286701, 1)
    var1 = i32_load(var0 + 44)
    if i32_load(var0 + 44):
        i32_store((var7 + (var1 << 4)), 0)
    i32_store(var0 + 44, 0)
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    var1 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
            break
    return
    var6 = i32_load(9215884)
    var1 = i32_load(var0 + 44)
    var2 = i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4)
    # br_table ['$label6', '$label7', '$label7', '$label7', '$label7', '$label7', '$label8', '$label9']
    _br_idx = i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4)
    break  # br_table
    i32_store8(var0 + 123, 0)
    i32_store(var0 + 32, 0)
    i32_store(var0 + 116, i32_load(var0 + 112))
    var0 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        break
    if (1 if i32_load(var0 + 8) < 3 else 0):
        break
    if (1 if (i32_load(i32_load(var0)) - 1) > 1 else 0):
        break
    i32_store(var0 + 8, 0)
    return
    i32_store8(var0 + 129, 11)
    return
    if (1 if var2 != 34 else 0):
        break
    var5 = i32_load(9561692)
    var4 = i32_load16_u(var0 + 110)
    var2 = (i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704))
    var3 = i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 283848)
    if (1 if i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 283848) == 2147483647 else 0):
        break
    i32_store((var2 + 283848), (i32_load16_u((var6 + ((var1 << 4) | 12)) + 2) + var3))
    var1 = 1
    i32_store8(var2 + 286701, 1)
    var3 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var8 = (var3 - 1)
    var9 = ((var3 - 1) & 1)
    var5 = (i32_load((var5 + (var4 * 286704)) + 283908) * var3)
    var4 = i32_load(9561692)
    var7 = i32_load(9143016)
    if (1 if var3 != 2 else 0):
        var3 = (var8 & -2)
        while True:  # loop $label11
            if i32_load8_u((var7 + (var1 + var5))):
                i32_store8((var4 + (var1 * 286704)) + 286701, 1)
            var8 = (var1 + 1)
            if i32_load8_u((var7 + ((var1 + 1) + var5))):
                i32_store8((var4 + (var8 * 286704)) + 286701, 1)
            var1 = (var1 + 2)
            var10 = (var10 + 2)
            if (1 if (var10 + 2) != var3 else 0):
                continue
            break  # end loop
    if (1 if var9 == 0 else 0):
        break
    if (1 if i32_load8_u((var7 + (var1 + var5))) == 0 else 0):
        break
    i32_store8((var4 + (var1 * 286704)) + 286701, 1)
    i32_store(var2 + 283912, (i32_load(var2 + 283912) - 1))
    var1 = i32_load(var0 + 44)
    if i32_load(var0 + 44):
        i32_store((var6 + (var1 << 4)), 0)
    i32_store(var0 + 44, 0)
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    var1 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
            break

