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
# $func59
# ==========================================================
def func59(var0, var1, var2, var3):
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
    var23 = ((i32_load8_u(var2 + 122) * 404) + 9568096)
    var24 = 1
    while True:  # loop $label41
        var6 = i32_load16_u(var2 + 112)
        var21 = (i32_load16_u(var2 + 112) - var19)
        var5 = i32_load(var23 + 216)
        var8 = (var19 << 1)
        var25 = (var21 + (i32_load(var23 + 216) + (var19 << 1)))
        if (1 if (i32_load16_u(var2 + 112) - var19) >= (var21 + (i32_load(var23 + 216) + (var19 << 1))) else 0):
            break
        var7 = i32_load16_u(var2 + 114)
        var22 = (i32_load16_u(var2 + 114) - var19)
        var4 = i32_load(var23 + 220)
        var8 = (var22 + (var8 + i32_load(var23 + 220)))
        if (1 if (i32_load16_u(var2 + 114) - var19) >= (var22 + (var8 + i32_load(var23 + 220))) else 0):
            break
        var27 = (var25 - 1)
        var28 = (var8 - 1)
        var29 = ((var6 + var19) + var5)
        var30 = ((var7 + var19) + var4)
        var26 = 1
        var8 = var21
        while True:  # loop $label40
            var5 = var22
            while True:  # loop $label39
                if (1 if var8 == var21 else 0):
                    break
                if (1 if var5 == var22 else 0):
                    break
                if (1 if var5 == var28 else 0):
                    break
                if (1 if var8 != var27 else 0):
                    break
                var11 = i32_load(9142440)
                if (1 if i32_load(9142440) <= var5 else 0):
                    break
                if (1 if (var5 | var8) < 0 else 0):
                    break
                if (1 if var8 >= var11 else 0):
                    break
                var4 = i32_load(var3 + 248)
                # br_table ['$label3', '$label4', '$label5', '$label6']
                _br_idx = (i32_load(var3 + 248) - 1)
                break  # br_table
                var9 = i32_load(var3 + 216)
                if (1 if i32_load(var3 + 216) <= 0 else 0):
                    break
                var12 = (i32_load(var3 + 220) + var5)
                if (1 if (i32_load(var3 + 220) + var5) <= var5 else 0):
                    break
                var16 = (var8 + var9)
                var13 = i32_load(var3 + 372)
                var17 = (var11 + 2)
                var18 = ((var11 + 2) * i32_load(var3 + 208))
                var15 = i32_load(var3 + 212)
                var20 = i32_load(9142840)
                var7 = var8
                while True:  # loop $label12
                    var10 = (var7 + 1)
                    var14 = (var7 - var8)
                    var6 = var5
                    var4 = var5
                    if (1 if var7 >= var11 else 0):
                        while True:  # loop $label8
                            if i32_load8_u((var13 + (((var6 - var5) * var9) + var14))):
                                break
                            var6 = (var6 + 1)
                            if (1 if (var6 + 1) != var12 else 0):
                                continue
                            break
                            break  # end loop
                        raise RuntimeError('unreachable')
                    while True:  # loop $label11
                        if i32_load8_u((var13 + (((var4 - var5) * var9) + var14))):
                            if (1 if var4 >= var11 else 0):
                                break
                            if (1 if (var4 | var7) < 0 else 0):
                                break
                            var4 = (var4 + 1)
                            if (1 if i32_load((var20 + (((((var4 + 1) + var18) * var17) + var10) << 2))) == var15 else 0):
                                break
                            break
                        var4 = (var4 + 1)
                        if (1 if var4 != var12 else 0):
                            continue
                        break  # end loop
                    var7 = var10
                    if (1 if var10 < var16 else 0):
                        continue
                    break  # end loop
                break
                var6 = i32_load(var3 + 216)
                if (1 if i32_load(var3 + 216) <= 0 else 0):
                    break
                var10 = (i32_load(var3 + 220) + var5)
                if (1 if (i32_load(var3 + 220) + var5) <= var5 else 0):
                    break
                var9 = (var6 + var8)
                var12 = (var11 + 2)
                var13 = ((var11 + 2) * i32_load(var3 + 208))
                var14 = i32_load(9142840)
                var6 = var8
                while True:  # loop $label13
                    if (1 if var6 >= var11 else 0):
                        break
                    var7 = (var6 + 1)
                    var4 = var5
                    while True:  # loop $label14
                        if (1 if var4 == var10 else 0):
                            var6 = var7
                            if (1 if var7 < var9 else 0):
                                continue
                            break
                        if (1 if var4 >= var11 else 0):
                            break
                        if (1 if (var4 | var6) < 0 else 0):
                            break
                        var4 = (var4 + 1)
                        if (1 if i32_load((var14 + (((((var4 + 1) + var13) * var12) + var7) << 2))) <= 2 else 0):
                            continue
                        break  # end loop
                    break  # end loop
                break
                var9 = i32_load(var3 + 216)
                if (1 if i32_load(var3 + 216) <= 0 else 0):
                    break
                var16 = i32_load(var3 + 220)
                if (1 if i32_load(var3 + 220) <= 0 else 0):
                    break
                var17 = (var5 + var16)
                var31 = (var8 + var9)
                var18 = i32_load(var3 + 372)
                var12 = (var11 + 2)
                var32 = ((var11 + 2) * i32_load(var3 + 208))
                var13 = 0
                var14 = i32_load(9142840)
                var7 = 0
                var6 = var8
                while True:  # loop $label19
                    var10 = (var6 + 1)
                    var15 = (var6 - var8)
                    var4 = var5
                    if (1 if var6 < var11 else 0):
                        while True:  # loop $label16
                            if i32_load8_u((var18 + (((var4 - var5) * var9) + var15))):
                                if (1 if var4 >= var11 else 0):
                                    break
                                if (1 if (var4 | var6) < 0 else 0):
                                    break
                                var4 = (var4 + 1)
                                var20 = i32_load((var14 + (((((var4 + 1) + var32) * var12) + var10) << 2)))
                                if (1 if i32_load((var14 + (((((var4 + 1) + var32) * var12) + var10) << 2))) > 2 else 0):
                                    break
                                if (1 if i32_load((var14 + (((var4 * var12) + var10) << 2))) > 2 else 0):
                                    break
                                if (1 if i32_load((var14 + ((((var4 + var12) * var12) + var10) << 2))) > 2 else 0):
                                    break
                                var7 = ((1 if var20 == 0 else 0) | var7)
                                var13 = (var13 + (1 if var20 == 1 else 0))
                                break
                            var4 = (var4 + 1)
                            if (1 if var4 < var17 else 0):
                                continue
                            break  # end loop
                        break
                    while True:  # loop $label18
                        if i32_load8_u((var18 + (((var4 - var5) * var9) + var15))):
                            break
                        var4 = (var4 + 1)
                        if (1 if (var4 + 1) < var17 else 0):
                            continue
                        break  # end loop
                    var6 = var10
                    if (1 if var10 < var31 else 0):
                        continue
                    break  # end loop
                if (1 if ((1 if var13 >= (((var9 * var16) // 2) - 1) else 0) & var7) == 0 else 0):
                    break
                break
                var6 = i32_load(var3 + 208)
                if i32_load(var3 + 208):
                    var7 = i32_load16_u(var2 + 110)
                    # br_table ['$label20', '$label21', '$label22']
                    _br_idx = (var4 - 4)
                    break  # br_table
                    if (1 if func193(var8, var5, var3, var7, 0, 0, 1, 0) == 0 else 0):
                        break
                    break
                    if (1 if var6 > 2 else 0):
                        break
                    var10 = i32_load(var3 + 216)
                    if (1 if i32_load(var3 + 216) <= 0 else 0):
                        break
                    var9 = (i32_load(var3 + 220) + var5)
                    if (1 if (i32_load(var3 + 220) + var5) <= var5 else 0):
                        break
                    var17 = (var8 + var10)
                    var12 = i32_load(var3 + 372)
                    var13 = (var11 + 2)
                    var18 = (var6 * (var11 + 2))
                    var14 = i32_load(var3 + 212)
                    var16 = i32_load(9142840)
                    var6 = var8
                    var7 = var8
                    if (1 if i32_load(var3 + 264) != 1 else 0):
                        while True:  # loop $label27
                            var7 = (var6 + 1)
                            var15 = (var6 - var8)
                            var4 = var5
                            if (1 if var6 >= var11 else 0):
                                while True:  # loop $label23
                                    if i32_load8_u((var12 + (((var4 - var5) * var10) + var15))):
                                        break
                                    var4 = (var4 + 1)
                                    if (1 if (var4 + 1) != var9 else 0):
                                        continue
                                    break
                                    break  # end loop
                                raise RuntimeError('unreachable')
                            while True:  # loop $label26
                                if i32_load8_u((var12 + (((var4 - var5) * var10) + var15))):
                                    if (1 if var4 >= var11 else 0):
                                        break
                                    if (1 if (var4 | var6) < 0 else 0):
                                        break
                                    var4 = (var4 + 1)
                                    if (1 if i32_load((var16 + (((((var4 + 1) + var18) * var13) + var7) << 2))) == var14 else 0):
                                        break
                                    break
                                var4 = (var4 + 1)
                                if (1 if var4 != var9 else 0):
                                    continue
                                break  # end loop
                            var6 = var7
                            if (1 if var7 < var17 else 0):
                                continue
                            break
                            break  # end loop
                        raise RuntimeError('unreachable')
                    while True:  # loop $label32
                        var6 = (var7 + 1)
                        var15 = (var7 - var8)
                        var4 = var5
                        if (1 if var7 >= var11 else 0):
                            while True:  # loop $label28
                                if i32_load8_u((var12 + (((var4 - var5) * var10) + var15))):
                                    break
                                var4 = (var4 + 1)
                                if (1 if (var4 + 1) != var9 else 0):
                                    continue
                                break
                                break  # end loop
                            raise RuntimeError('unreachable')
                        while True:  # loop $label31
                            if i32_load8_u((var12 + (((var4 - var5) * var10) + var15))):
                                if (1 if var4 >= var11 else 0):
                                    break
                                if (1 if (var4 | var7) < 0 else 0):
                                    break
                                var4 = (var4 + 1)
                                if (1 if i32_load((var16 + (((((var4 + 1) + var18) * var13) + var6) << 2))) != var14 else 0):
                                    break
                                if (1 if i32_load((var16 + (((var4 * var13) + var6) << 2))) == var14 else 0):
                                    break
                                break
                            var4 = (var4 + 1)
                            if (1 if var4 != var9 else 0):
                                continue
                            break  # end loop
                        var7 = var6
                        if (1 if var6 < var17 else 0):
                            continue
                        break  # end loop
                    break
                var9 = i32_load(var3 + 216)
                if (1 if i32_load(var3 + 216) <= 0 else 0):
                    break
                var13 = (i32_load(var3 + 220) + var5)
                if (1 if (i32_load(var3 + 220) + var5) <= var5 else 0):
                    break
                var18 = (var8 + var9)
                var14 = i32_load(var3 + 372)
                var12 = (var11 + 2)
                var15 = i32_load(9671128)
                var16 = i32_load(9142840)
                var7 = var8
                while True:  # loop $label37
                    var10 = (var7 + 1)
                    var17 = (var7 - var8)
                    var6 = var5
                    var4 = var5
                    if (1 if var7 >= var11 else 0):
                        while True:  # loop $label33
                            if i32_load8_u((var14 + (((var6 - var5) * var9) + var17))):
                                break
                            var6 = (var6 + 1)
                            if (1 if (var6 + 1) != var13 else 0):
                                continue
                            break
                            break  # end loop
                        raise RuntimeError('unreachable')
                    while True:  # loop $label36
                        if i32_load8_u((var14 + (((var4 - var5) * var9) + var17))):
                            if (1 if var4 >= var11 else 0):
                                break
                            if (1 if (var4 | var7) < 0 else 0):
                                break
                            var4 = (var4 + 1)
                            if i32_load((var16 + ((((var4 + 1) * var12) + var10) << 2))):
                                break
                            if (1 if i32_load(((i32_load8_u((var15 + (i32_load((var16 + ((((var4 + var12) * var12) + var10) << 2))) * 132)) + 122) * 404) + 9568096) + 264) != 1 else 0):
                                break
                            break
                        var4 = (var4 + 1)
                        if (1 if var4 != var13 else 0):
                            continue
                        break  # end loop
                    var7 = var10
                    if (1 if var10 < var18 else 0):
                        continue
                    break  # end loop
                break
                if (1 if func194(var8, var5, var3, var7, 0, 0, 1) == 0 else 0):
                    break
                i32_store(var0, var8)
                i32_store(var1, var5)
                if var26:
                    break
                break
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var30 else 0):
                    continue
                break  # end loop
            var8 = (var8 + 1)
            var26 = (1 if (var8 + 1) < var25 else 0)
            if (1 if var8 != var29 else 0):
                continue
            break  # end loop
        var19 = (var19 + 1)
        var24 = (1 if (var19 + 1) < 20 else 0)
        if (1 if var19 != 20 else 0):
            continue
        break  # end loop
    return var24

