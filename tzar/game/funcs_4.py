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
# $func141
# ==========================================================
def func141(var0, var1):
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
    var30 = 0
    var31 = 0
    var9 = (var0 // 32)
    var19 = ((var0 // 32) + 3)
    var10 = i32_load(9142440)
    var15 = (i32_load(9142440) + 2)
    var11 = (var1 // 32)
    var20 = ((var1 // 32) + 4)
    var11 = (var11 - 3)
    var8 = (var9 - 3)
    var21 = i32_load(9142848)
    var22 = i32_load(9215884)
    var23 = i32_load(38448)
    var24 = i32_load(9671128)
    var25 = i32_load(9142840)
    var26 = i32_load(9147376)
    var27 = i32_load(9142424)
    var12 = 2147483647
    var28 = (1 if i32_load8_u(9147152) == 0 else 0)
    var29 = i32_load8_u(9142408)
    while True:  # loop $label4
        var9 = (var8 + 1)
        var2 = var11
        if (1 if var8 < var10 else 0):
            while True:  # loop $label3
                if ((1 if var2 < var10 else 0) & (1 if (var2 | var8) >= 0 else 0)):
                    var13 = 0
                    var30 = ((1 if i32_load(var27 + 48) != 0 else 0) & var28)
                    var16 = (var2 + 1)
                    var31 = (var26 + (((var2 * var10) + var8) << 1))
                    while True:  # loop $label2
                        if var30:
                            if (1 if i32_load16_u(var31) == 0 else 0):
                                break
                        var17 = i32_load((var25 + ((var9 + ((var16 + (var13 * var15)) * var15)) << 2)))
                        if (1 if i32_load((var25 + ((var9 + ((var16 + (var13 * var15)) * var15)) << 2))) < 3 else 0):
                            break
                        var3 = (var24 + (var17 * 132))
                        if (1 if i32_load((var24 + (var17 * 132)) + 40) == 0 else 0):
                            break
                        if var29:
                            if (1 if var23 == i32_load8_u(var3 + 122) else 0):
                                break
                        var7 = (i32_load16_u(var3 + 112) << 5)
                        var4 = i32_load(var3 + 48)
                        if i32_load(var3 + 48):
                            var7 = (var7 - i32_load(var4 + 8))
                        else:
                        var5 = (i32_load(var4 + 12) - 0)
                        if (1 if i32_load8_u(var3 + 125) == 1 else 0):
                            var6 = (i32_load8_u(var3 + 124) << 3)
                            var2 = i32_load(((i32_load8_u(var3 + 124) << 3) + 8996))
                            var5 = (var5 - (i32_load(((i32_load8_u(var3 + 124) << 3) + 8996)) << 5))
                            var14 = i32_load((var6 + 8992))
                            var6 = (var7 - (i32_load((var6 + 8992)) << 5))
                            var2 = i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 260)
                            if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 260):
                            else:
                            var2 = (0 * var2)
                            var5 = (var2 + (((((i32_load((var22 + (i32_load(var3 + 44) << 4))) - var21) * -25) + (32000 // var2)) * (0 * var2)) // 1000))
                            var7 = (var6 + ((var2 * var14) // 1000))
                        if var4:
                            var2 = (i32_load(var4 + 4) // (i32_load(var4 + 20) * i32_load(var4 + 16)))
                            break
                        var6 = ((i32_load8_u(var3 + 122) * 404) + 9568096)
                        var2 = (i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 220) << 5)
                        var3 = (i32_load(var6 + 216) << 5)
                        var6 = (1 if var2 < 32 else 0)
                        var4 = ((var5 - 16) if (1 if var2 < 32 else 0) else var5)
                        var14 = (48 if var6 else var2)
                        var2 = (var1 - (((var5 - 16) if (1 if var2 < 32 else 0) else var5) + (((48 if var6 else var2) & 0xFFFFFFFF) >> 1)))
                        var2 = (1 if var3 < 32 else 0)
                        var5 = ((var7 - 16) if (1 if var3 < 32 else 0) else var7)
                        var6 = (48 if var2 else var3)
                        var2 = (var0 - (((var7 - 16) if (1 if var3 < 32 else 0) else var7) + (((48 if var2 else var3) & 0xFFFFFFFF) >> 1)))
                        var2 = (((var1 - (((var5 - 16) if (1 if var2 < 32 else 0) else var5) + (((48 if var6 else var2) & 0xFFFFFFFF) >> 1))) * var2) + ((var0 - (((var7 - 16) if (1 if var3 < 32 else 0) else var7) + (((48 if var2 else var3) & 0xFFFFFFFF) >> 1))) * var2))
                        var2 = (((((1 if var2 < var12 else 0) & (1 if var0 > var5 else 0)) & (1 if (var5 + var6) > var0 else 0)) & (1 if var1 > var4 else 0)) & (1 if (var4 + var14) > var1 else 0))
                        var12 = ((((var1 - (((var5 - 16) if (1 if var2 < 32 else 0) else var5) + (((48 if var6 else var2) & 0xFFFFFFFF) >> 1))) * var2) + ((var0 - (((var7 - 16) if (1 if var3 < 32 else 0) else var7) + (((48 if var2 else var3) & 0xFFFFFFFF) >> 1))) * var2)) if (((((1 if var2 < var12 else 0) & (1 if var0 > var5 else 0)) & (1 if (var5 + var6) > var0 else 0)) & (1 if var1 > var4 else 0)) & (1 if (var4 + var14) > var1 else 0)) else var12)
                        var18 = (var17 if var2 else var18)
                        var13 = (var13 + 1)
                        if (1 if (var13 + 1) != 3 else 0):
                            continue
                        break  # end loop
                else:
                var2 = (var2 + 1)
                if (1 if var16 != (var2 + 1) else 0):
                    continue
                break  # end loop
        var2 = (1 if var8 == var19 else 0)
        var8 = var9
        if (1 if var2 == 0 else 0):
            continue
        break  # end loop
    return var18


# ==========================================================
# $func157
# ==========================================================
def func157(var0):
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
    var2 = i32_load8_u(var0 + 122)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) != 1 else 0):
        break
    var3 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        break
    if (1 if i32_load(38540) == var2 else 0):
        break
    if (1 if i32_load(38812) == var2 else 0):
        break
    if (1 if i32_load(38888) == var2 else 0):
        break
    if i32_load(var3 + 8):
        var2 = (i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704))
        var18 = ((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 283908)
        var19 = (var2 + 286701)
        var9 = (var2 + 281704)
        var10 = (var2 + 281700)
        var11 = (var2 + 281696)
        var12 = (var2 + 281692)
        var13 = (var2 + 283860)
        var14 = (var2 + 283856)
        var15 = (var2 + 283852)
        var16 = (var2 + 283848)
        var5 = i32_load(9143016)
        var20 = i32_load(var3)
        var21 = (i32_load8_u(var0 + 125) - 4)
        while True:  # loop $label4
            var0 = i32_load((var20 + (var4 << 2)))
            var1 = (1 if var0 > 2147483646 else 0)
            var17 = ((i32_load((var20 + (var4 << 2))) - 2147483647) if (1 if var0 > 2147483646 else 0) else var0)
            if (1 if var4 == 0 else 0):
                if (1 if var0 < 2147483647 else 0):
                    break
                # br_table ['$label2', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label2', '$label1']
                _br_idx = var21
                break  # br_table
            if var1:
                break
            var0 = ((var17 * 404) + 9568164)
            var1 = i32_load(var16)
            if (1 if i32_load(var16) != 2147483647 else 0):
                i32_store(var16, (i32_load(var0) + var1))
            var1 = i32_load(var15)
            if (1 if i32_load(var15) != 2147483647 else 0):
                i32_store(var15, (i32_load(var0 + 4) + var1))
            var1 = i32_load(var14)
            if (1 if i32_load(var14) != 2147483647 else 0):
                i32_store(var14, (i32_load(var0 + 8) + var1))
            var1 = i32_load(var13)
            if (1 if i32_load(var13) != 2147483647 else 0):
                i32_store(var13, (i32_load(var0 + 12) + var1))
            i32_store(var12, (i32_load(var12) - i32_load(var0)))
            i32_store(var11, (i32_load(var11) - i32_load(var0 + 4)))
            i32_store(var10, (i32_load(var10) - i32_load(var0 + 8)))
            i32_store(var9, (i32_load(var9) - i32_load(var0 + 12)))
            i32_store8(var19, 1)
            var1 = i32_load(9142892)
            if (1 if i32_load(9142892) < 2 else 0):
                break
            var0 = 1
            var6 = (var1 - 1)
            var22 = ((var1 - 1) & 1)
            var7 = (i32_load(var18) * var1)
            var8 = i32_load(9561692)
            if (1 if var1 != 2 else 0):
                var6 = (var6 & -2)
                var1 = 0
                while True:  # loop $label3
                    if i32_load8_u((var5 + (var0 + var7))):
                        i32_store8((var8 + (var0 * 286704)) + 286701, 1)
                    var23 = (var0 + 1)
                    if i32_load8_u((var5 + ((var0 + 1) + var7))):
                        i32_store8((var8 + (var23 * 286704)) + 286701, 1)
                    var0 = (var0 + 2)
                    var1 = (var1 + 2)
                    if (1 if (var1 + 2) != var6 else 0):
                        continue
                    break  # end loop
            if (1 if var22 == 0 else 0):
                break
            if (1 if i32_load8_u((var5 + (var0 + var7))) == 0 else 0):
                break
            i32_store8((var8 + (var0 * 286704)) + 286701, 1)
            var0 = ((var2 + (var17 << 2)) + 282828)
            i32_store(((var2 + (var17 << 2)) + 282828), (i32_load(var0) - 1))
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < i32_load(var3 + 8) else 0):
                continue
            break  # end loop
    i32_store(var3 + 8, 0)


# ==========================================================
# $func159
# ==========================================================
def func159(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var3 = i32_load(var0 + 28)
    var5 = i32_load(9671128)
    var0 = i32_load(9215928)
    if (1 if i32_load(9215928) == 0 else 0):
        break
    var1 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) == 0 else 0):
        break
    var2 = i32_load(var0)
    var0 = 0
    while True:  # loop $label2
        if (1 if i32_load((var5 + (i32_load((var2 + (var0 << 2))) * 132)) + 28) == var3 else 0):
            break
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var1 else 0):
            continue
        break  # end loop
    var0 = i32_load(9215932)
    if (1 if i32_load(9215932) == 0 else 0):
        break
    var1 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) == 0 else 0):
        break
    var2 = i32_load(var0)
    var0 = 0
    while True:  # loop $label4
        if (1 if i32_load((var5 + (i32_load((var2 + (var0 << 2))) * 132)) + 28) == var3 else 0):
            break
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var1 else 0):
            continue
        break  # end loop
    var0 = i32_load(9215936)
    if (1 if i32_load(9215936) == 0 else 0):
        break
    var1 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) == 0 else 0):
        break
    var2 = i32_load(var0)
    var0 = 0
    while True:  # loop $label6
        if (1 if i32_load((var5 + (i32_load((var2 + (var0 << 2))) * 132)) + 28) == var3 else 0):
            break
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var1 else 0):
            continue
        break  # end loop
    var4 = 1
    var0 = i32_load(9215940)
    if (1 if i32_load(9215940) == 0 else 0):
        break
    var1 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) == 0 else 0):
        break
    var2 = i32_load(var0)
    var0 = 0
    while True:  # loop $label7
        var6 = i32_load((var5 + (i32_load((var2 + (var0 << 2))) * 132)) + 28)
        var4 = (1 if i32_load((var5 + (i32_load((var2 + (var0 << 2))) * 132)) + 28) != var3 else 0)
        if (1 if var3 == var6 else 0):
            break
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var1 else 0):
            continue
        break  # end loop
    return var4

