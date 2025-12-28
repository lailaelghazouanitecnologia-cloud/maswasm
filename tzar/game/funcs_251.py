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
# $func142
# ==========================================================
def func142(var0, var1):
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
    var32 = 0
    var33 = 0
    var34 = 0
    var35 = 0
    var12 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var14 = i32_load(9561692)
    var16 = i32_load16_u(var0 + 110)
    var18 = (i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704))
    var2 = i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 281804)
    if (1 if i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 281804) == 0 else 0):
        break
    if (1 if ((i32_load(9142848) - var2) * 25) > 29999 else 0):
        break
    if (1 if var1 == 0 else 0):
        break
    func29(var0, 1)
    break
    var23 = i32_load(var18 + 283876)
    var24 = i32_load(var18 + 283872)
    i32_store8(var0 + 129, 2)
    var19 = i32_load(((i32_load(var18 + 283960) << 2) + 9687152))
    var30 = ((var18 + (i32_load(((i32_load(var18 + 283960) << 2) + 9687152)) << 2)) + 284636)
    var2 = i32_load(((var18 + (i32_load(((i32_load(var18 + 283960) << 2) + 9687152)) << 2)) + 284636))
    if (1 if i32_load(((var18 + (i32_load(((i32_load(var18 + 283960) << 2) + 9687152)) << 2)) + 284636)) == 0 else 0):
        break
    var20 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) == 0 else 0):
        break
    var6 = i32_load(9142440)
    var9 = (i32_load(9142440) + 2)
    var21 = i32_load(38448)
    var27 = i32_load(9142840)
    var10 = i32_load(9671128)
    var17 = i32_load(var2)
    var28 = 1
    while True:  # loop $label14
        var2 = i32_load((var17 + (var7 << 2)))
        if (1 if i32_load((var17 + (var7 << 2))) == 0 else 0):
            break
        var3 = (var10 + (var2 * 132))
        # br_table ['$label4', '$label3', '$label3', '$label3', '$label5', '$label3']
        _br_idx = i32_load8_u((var10 + (var2 * 132)) + 125)
        break  # br_table
        break
        var15 = i32_load16_u(var3 + 114)
        var25 = (i32_load16_u(var3 + 114) + 11)
        var13 = i32_load16_u(var3 + 112)
        var26 = (i32_load16_u(var3 + 112) + 11)
        var3 = (var13 - 6)
        var8 = (var15 - 6)
        var11 = 0
        while True:  # loop $label8
            var5 = (var3 + 1)
            if (1 if var3 < var6 else 0):
                var2 = (var3 - var13)
                var22 = (((var3 - var13) * var2) - 1)
                var2 = var8
                while True:  # loop $label7
                    var4 = var2
                    var2 = (var2 - var15)
                    if (1 if (var22 + ((var2 - var15) * var2)) > 36 else 0):
                        break
                    if (1 if var4 >= var6 else 0):
                        break
                    if (1 if (var3 | var4) < 0 else 0):
                        break
                    var2 = i32_load((var27 + (((((var4 + var9) + 1) * var9) + var5) << 2)))
                    if (1 if i32_load((var27 + (((((var4 + var9) + 1) * var9) + var5) << 2))) < 3 else 0):
                        break
                    var11 = (var11 + (1 if var21 == i32_load8_u((var10 + (var2 * 132)) + 122) else 0))
                    var2 = (var4 + 1)
                    if (1 if var4 != var25 else 0):
                        continue
                    break  # end loop
            var2 = (1 if var3 != var26 else 0)
            var3 = var5
            if var2:
                continue
            break  # end loop
        if (1 if var11 < 4 else 0):
            break
        var20 = (var13 + 9)
        var17 = (var15 + 9)
        var11 = (var15 - 10)
        var4 = (var13 - 10)
        var25 = (var9 * i32_load(((var21 * 404) + 9568096) + 208))
        var3 = 2147483647
        var8 = 0
        while True:  # loop $label11
            var7 = (var4 + 1)
            if (1 if var4 < var6 else 0):
                var2 = (var13 - var4)
                var26 = ((var13 - var4) * var2)
                var2 = var11
                while True:  # loop $label10
                    var5 = var2
                    if (1 if var6 <= var2 else 0):
                        break
                    if (1 if (var4 | var5) < 0 else 0):
                        break
                    var2 = (var15 - var5)
                    var22 = (((var15 - var5) * var2) + var26)
                    if (1 if (((var15 - var5) * var2) + var26) >= var3 else 0):
                        break
                    var2 = i32_load((var27 + (((((var5 + var25) + 1) * var9) + var7) << 2)))
                    if (1 if i32_load((var27 + (((((var5 + var25) + 1) * var9) + var7) << 2))) == 0 else 0):
                        break
                    var22 = (1 if var21 == i32_load8_u((var10 + (var2 * 132)) + 122) else 0)
                    var3 = (var22 if (1 if var21 == i32_load8_u((var10 + (var2 * 132)) + 122) else 0) else var3)
                    var8 = (var2 if var22 else var8)
                    var2 = (var5 + 1)
                    if (1 if var5 != var17 else 0):
                        continue
                    break  # end loop
            var2 = (1 if var4 != var20 else 0)
            var4 = var7
            if var2:
                continue
            break  # end loop
        if var8:
            break
        var2 = i32_load(var0 + 44)
        if (1 if i32_load(var0 + 44) == 0 else 0):
            break
        var3 = i32_load(9215884)
        if (1 if i32_load((i32_load(9215884) + (var2 << 4)) + 12) == 1 else 0):
            break
        if (1 if i32_load8_u(var0 + 125) == 7 else 0):
            break
        if (1 if i32_load((var3 + ((var2 << 4) | 4))) == 0 else 0):
            break
        func29(var0, 1)
        if (1 if var28 == 0 else 0):
            break
        break
        var7 = (var7 + 1)
        var28 = (1 if (var7 + 1) < var20 else 0)
        if (1 if var7 != var20 else 0):
            continue
        break  # end loop
    var21 = ((var19 * 404) + 9568096)
    var2 = (var14 + (var16 * 286704))
    if (1 if i32_load(((var19 * 404) + 9568096) + 68) > i32_load((var14 + (var16 * 286704)) + 283848) else 0):
        break
    if (1 if i32_load(var21 + 72) > i32_load((var2 + 283852)) else 0):
        break
    var2 = ((var19 * 404) + 9568096)
    var3 = (var14 + (var16 * 286704))
    if (1 if i32_load(((var19 * 404) + 9568096) + 76) > i32_load(((var14 + (var16 * 286704)) + 283856)) else 0):
        break
    if (1 if i32_load(var2 + 80) <= i32_load((var3 + 283860)) else 0):
        break
    var7 = i32_load(9142440)
    var11 = (i32_load(9142440) + 2)
    var15 = i32_load(38448)
    var13 = ((i32_load(9142440) + 2) * i32_load(((i32_load(38448) * 404) + 9568096) + 208))
    var9 = (var23 + 24)
    var10 = (var24 + 24)
    var8 = (var23 - 25)
    var1 = (var24 - 25)
    var18 = i32_load(9671128)
    var14 = i32_load(9142840)
    var3 = 2147483647
    var6 = 0
    while True:  # loop $label19
        var5 = (var1 + 1)
        if (1 if var1 < var7 else 0):
            var2 = (var24 - var1)
            var16 = ((var24 - var1) * var2)
            var2 = var8
            while True:  # loop $label18
                var4 = var2
                if (1 if var7 <= var2 else 0):
                    break
                if (1 if (var1 | var4) < 0 else 0):
                    break
                var2 = (var23 - var4)
                var19 = (((var23 - var4) * var2) + var16)
                if (1 if (((var23 - var4) * var2) + var16) >= var3 else 0):
                    break
                var2 = i32_load((var14 + (((((var4 + var13) + 1) * var11) + var5) << 2)))
                if (1 if i32_load((var14 + (((((var4 + var13) + 1) * var11) + var5) << 2))) == 0 else 0):
                    break
                var19 = (1 if var15 == i32_load8_u((var18 + (var2 * 132)) + 122) else 0)
                var3 = (var19 if (1 if var15 == i32_load8_u((var18 + (var2 * 132)) + 122) else 0) else var3)
                var6 = (var2 if var19 else var6)
                var2 = (var4 + 1)
                if (1 if var4 < var9 else 0):
                    continue
                break  # end loop
        var2 = (1 if var1 < var10 else 0)
        var1 = var5
        if var2:
            continue
        break  # end loop
    if var6:
        break
    var1 = i32_load(var0 + 44)
    if (1 if i32_load(var0 + 44) == 0 else 0):
        break
    var2 = i32_load(9215884)
    if (1 if i32_load((i32_load(9215884) + (var1 << 4)) + 12) == 1 else 0):
        break
    if (1 if i32_load8_u(var0 + 125) == 7 else 0):
        break
    if i32_load((var2 + ((var1 << 4) | 4))):
        break
    break
    func29(var0, 1)
    break
    if (1 if i32_load(9142440) >= 2 else 0):
        var7 = (var24 - 1)
        var8 = (var23 - 1)
        var10 = (var24 + 2)
        var9 = (var23 + 2)
        var22 = ((var14 + (var16 * 286704)) + 283908)
        var14 = 1
        while True:  # loop $label37
            if (1 if var7 >= var10 else 0):
                break
            if (1 if var8 >= var9 else 0):
                break
            var16 = (var10 - 1)
            var20 = (var9 - 1)
            var27 = 1
            var5 = var7
            while True:  # loop $label36
                var28 = 1
                var2 = var8
                var4 = var8
                var15 = (var5 - 6)
                var31 = (var5 + 12)
                if (1 if (var5 - 6) >= (var5 + 12) else 0):
                    while True:  # loop $label24
                        if (1 if var5 == var7 else 0):
                            break
                        if (1 if var2 == var8 else 0):
                            break
                        if (1 if var2 == var20 else 0):
                            break
                        if (1 if var5 != var16 else 0):
                            break
                        var3 = i32_load(9142440)
                        if (1 if i32_load(9142440) <= var2 else 0):
                            break
                        if (1 if (var2 | var5) < 0 else 0):
                            break
                        if (1 if var3 <= var5 else 0):
                            break
                        var2 = (var2 + 1)
                        if (1 if (var2 + 1) != var9 else 0):
                            continue
                        break
                        break  # end loop
                    raise RuntimeError('unreachable')
                while True:  # loop $label34
                    if (1 if var5 == var7 else 0):
                        break
                    if (1 if var4 == var8 else 0):
                        break
                    if (1 if var4 == var20 else 0):
                        break
                    if (1 if var5 != var16 else 0):
                        break
                    var2 = i32_load(9142440)
                    if (1 if i32_load(9142440) <= var4 else 0):
                        break
                    if (1 if (var4 | var5) < 0 else 0):
                        break
                    if (1 if var2 <= var5 else 0):
                        break
                    if (1 if func73(var5, var4, var21, 0, 0, 1) == 0 else 0):
                        break
                    var13 = (var4 - 6)
                    var32 = (var4 + 12)
                    if (1 if (var4 - 6) >= (var4 + 12) else 0):
                        break
                    var6 = 0
                    var17 = i32_load(9142440)
                    var25 = (i32_load(9142440) + 2)
                    var33 = i32_load(38448)
                    var26 = i32_load(9671128)
                    var34 = i32_load(9142840)
                    var3 = var15
                    while True:  # loop $label30
                        var11 = (var3 + 1)
                        if (1 if var3 < var17 else 0):
                            var2 = (var3 - var5)
                            var35 = (((var3 - var5) * var2) - 1)
                            var2 = var13
                            while True:  # loop $label29
                                var29 = (var2 - var4)
                                if (1 if (var35 + ((var2 - var4) * var29)) > 36 else 0):
                                    break
                                if (1 if var2 >= var17 else 0):
                                    break
                                if (1 if (var2 | var3) < 0 else 0):
                                    break
                                var29 = i32_load((var34 + (((((var2 + var25) + 1) * var25) + var11) << 2)))
                                if (1 if i32_load((var34 + (((((var2 + var25) + 1) * var25) + var11) << 2))) < 3 else 0):
                                    break
                                var6 = (var6 + (1 if var33 == i32_load8_u((var26 + (var29 * 132)) + 122) else 0))
                                var2 = (var2 + 1)
                                if (1 if (var2 + 1) != var32 else 0):
                                    continue
                                break  # end loop
                        var3 = var11
                        if (1 if var11 != var31 else 0):
                            continue
                        break  # end loop
                    if (1 if var6 < 11 else 0):
                        break
                    if (1 if func108(var5, var4, i32_load(var22), 7) == 0 else 0):
                        break
                    var2 = i32_load(var30)
                    if (1 if i32_load(var30) == 0 else 0):
                        break
                    var3 = i32_load(var2 + 8)
                    if (1 if i32_load(var2 + 8) == 0 else 0):
                        break
                    var13 = i32_load(var2)
                    var2 = 0
                    var11 = 1
                    while True:  # loop $label33
                        var6 = i32_load((var13 + (var2 << 2)))
                        if i32_load((var13 + (var2 << 2))):
                            var6 = (var26 + (var6 * 132))
                            var17 = (var5 - i32_load16_u((var26 + (var6 * 132)) + 112))
                            var6 = (var4 - i32_load16_u(var6 + 114))
                            if (1 if ((((var5 - i32_load16_u((var26 + (var6 * 132)) + 112)) * var17) + ((var4 - i32_load16_u(var6 + 114)) * var6)) - 1) <= 81 else 0):
                                break
                        var2 = (var2 + 1)
                        var11 = (1 if (var2 + 1) < var3 else 0)
                        if (1 if var2 != var3 else 0):
                            continue
                        break
                        break  # end loop
                    if (1 if var11 == 0 else 0):
                        break
                    var4 = (var4 + 1)
                    var28 = (1 if (var4 + 1) < var9 else 0)
                    if (1 if var4 != var9 else 0):
                        continue
                    break
                    break  # end loop
                var2 = i32_load(var0 + 28)
                i32_store(var12 + 24, var4)
                i32_store(var12 + 20, var5)
                i32_store(var12 + 16, var19)
                var3 = i32_load16_u(var0 + 110)
                i64_store(var12 + 48, 4294967297)
                i64_store(var12 + 40, 4294967297)
                i64_store(var12 + 32, 4294967297)
                i32_store(var12 + 28, var3)
                i32_store(var12 + 56, 0)
                i32_store(var12 + 12, var2)
                if i32_load(i32_load(9142424) + 156):
                    func29((i32_load(9671128) + (var2 * 132)), 1)
                if var28:
                    break
                var5 = (var5 + 1)
                var27 = (1 if (var5 + 1) < var10 else 0)
                if (1 if var5 != var10 else 0):
                    continue
                break
                break  # end loop
            if var27:
                break
            var9 = (var9 + 1)
            var10 = (var10 + 1)
            var14 = (var14 + 1)
            var8 = (var23 - (var14 + 1))
            var7 = (var24 - var14)
            if (1 if var14 < i32_load(9142440) else 0):
                continue
            break  # end loop
    i32_store((var18 + 281804), i32_load(9142848))
    if (1 if var1 == 0 else 0):
        break
    func29(var0, 1)
    var2 = 0
    global global0
    global0 = (var12 - -64)
    return var2


# ==========================================================
# $func261
# ==========================================================
def func261(var0, var1, var2, var3):
    var4 = 0
    var4 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    i32_store(var4 + 24, var2)
    i32_store(var4 + 20, var1)
    i32_store(var4 + 16, var0)
    var0 = i32_load16_u(var3 + 110)
    i32_store(var4 + 56, 0)
    i64_store(var4 + 48, 4294967297)
    i64_store(var4 + 40, 4294967297)
    i64_store(var4 + 32, 4294967297)
    i32_store(var4 + 28, var0)
    i32_store(var4 + 12, i32_load(var3 + 28))
    global global0
    global0 = (var4 - -64)

