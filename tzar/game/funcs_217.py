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
# $func30
# ==========================================================
def func30(var0, var1, var2, var3, var4, var5, var6, var7, var8, param9):
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
    var22 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    i32_store(var22 + 24, var3)
    i32_store(var22 + 28, var1)
    i32_store(var22 + 20, var4)
    var3 = 0
    if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 20 else 0):
        break
    var1 = i32_load8_u(var0 + 125)
    if (1 if (i32_load8_u(var0 + 125) & -2) == 12 else 0):
        break
    if (1 if var1 == 3 else 0):
        break
    var1 = i32_load(((var2 * 40) + 9671200) + 24)
    if i32_load(((var2 * 40) + 9671200) + 24):
        # call_indirect via table[var1]
        if call_indirect(var1):
            break
    if i32_load(var0 + 36):
        if i32_load(var0 + 36):
            break
    var14 = var0
    var0 = i32_load(var22 + 28)
    var1 = 0
    var12 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    if (1 if var0 == 0 else 0):
        break
    var30 = i32_load(9561692)
    var27 = i32_load16_u(var14 + 110)
    var11 = (i32_load(9561692) + (i32_load16_u(var14 + 110) * 286704))
    if (1 if i32_load((i32_load(9561692) + (i32_load16_u(var14 + 110) * 286704)) + 286684) == 0 else 0):
        break
    var4 = i32_load(9671128)
    var28 = (i32_load(9671128) + (var0 * 132))
    var9 = i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122)
    var13 = i32_load(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 264)
    if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 264) == 4 else 0):
        break
    var20 = i32_load8_u(var14 + 122)
    var10 = i32_load(((i32_load8_u(var14 + 122) * 404) + 9568096) + 264)
    if (1 if i32_load(((i32_load8_u(var14 + 122) * 404) + 9568096) + 264) == 4 else 0):
        break
    var18 = i32_load16_u(var14 + 112)
    i32_store(var12 + 12, i32_load16_u(var14 + 112))
    var21 = i32_load16_u(var14 + 114)
    i32_store(var12 + 8, i32_load16_u(var14 + 114))
    if var10:
        var1 = ((var20 * 404) + 9568096)
        var15 = i32_load(((var20 * 404) + 9568096) + 216)
        if (1 if i32_load(((var20 * 404) + 9568096) + 216) == 0 else 0):
            var10 = 0
            break
        var10 = 0
        var16 = i32_load(var1 + 220)
        if (1 if i32_load(var1 + 220) == 0 else 0):
            break
        var1 = i32_load(9215880)
        if (1 if i32_load(9215880) == 0 else 0):
            break
        var19 = i32_load(9142432)
        if (1 if i32_load(9142432) == 0 else 0):
            break
        var24 = i32_load(9142440)
        var17 = i32_load(var1)
        var20 = 0
        while True:  # loop $label4
            var23 = (var18 + var20)
            var1 = 0
            while True:  # loop $label3
                var10 = i32_load((var19 + ((var23 + ((var1 + var21) * var24)) << 2)))
                if (1 if i32_load((var17 + (i32_load((var19 + ((var23 + ((var1 + var21) * var24)) << 2))) << 2))) == 0 else 0):
                    break
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var16 else 0):
                    continue
                break  # end loop
            var10 = 0
            var20 = (var20 + 1)
            if (1 if (var20 + 1) != var15 else 0):
                continue
            break  # end loop
        break
    var10 = 0
    var1 = i32_load(9142432)
    if (1 if i32_load(9142432) == 0 else 0):
        break
    var10 = i32_load((var1 + (((i32_load(9142440) * var21) + var18) << 2)))
    # br_table ['$label5', '$label6', '$label6', '$label6', '$label5', '$label6']
    _br_idx = var13
    break  # br_table
    var1 = ((var9 * 404) + 9568096)
    var13 = i32_load(((var9 * 404) + 9568096) + 216)
    if (1 if i32_load(((var9 * 404) + 9568096) + 216) == 0 else 0):
        var20 = 0
        break
    var20 = 0
    var15 = i32_load(var1 + 220)
    if (1 if i32_load(var1 + 220) == 0 else 0):
        break
    var1 = i32_load(9215880)
    if (1 if i32_load(9215880) == 0 else 0):
        break
    var16 = i32_load(9142432)
    if (1 if i32_load(9142432) == 0 else 0):
        break
    var0 = (var4 + (var0 * 132))
    var4 = i32_load16_u((var4 + (var0 * 132)) + 114)
    var0 = i32_load16_u(var0 + 112)
    var19 = i32_load(9142440)
    var24 = i32_load(var1)
    var9 = 0
    while True:  # loop $label9
        var17 = (var0 + var9)
        var1 = 0
        while True:  # loop $label8
            var20 = i32_load((var16 + ((var17 + ((var1 + var4) * var19)) << 2)))
            if (1 if i32_load((var24 + (i32_load((var16 + ((var17 + ((var1 + var4) * var19)) << 2))) << 2))) == 0 else 0):
                break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var15 else 0):
                continue
            break  # end loop
        var20 = 0
        var9 = (var9 + 1)
        if (1 if (var9 + 1) != var13 else 0):
            continue
        break  # end loop
    break
    var20 = 0
    var1 = i32_load(9142432)
    if (1 if i32_load(9142432) == 0 else 0):
        break
    var0 = (var4 + (var0 * 132))
    var20 = i32_load((var1 + (((i32_load(9142440) * i32_load16_u((var4 + (var0 * 132)) + 114)) + i32_load16_u(var0 + 112)) << 2)))
    var1 = 0
    if (1 if var10 == var20 else 0):
        break
    var4 = 0
    i32_store8(var14 + 129, 0)
    var1 = 1
    var0 = i32_load(9684440)
    if (1 if i32_load(9684440) == 0 else 0):
        break
    var32 = i32_load(((i32_load((var30 + (var27 * 286704)) + 283960) << 2) + 58928))
    var9 = i32_load(9684436)
    while True:  # loop $label12
        var1 = (var0 * var4)
        if (1 if var4 != var10 else 0):
            if (1 if i32_load8_u((var9 + (var1 + var10))) == 0 else 0):
                break
        if (1 if var4 == var20 else 0):
            break
        if i32_load8_u((var9 + (var1 + var20))):
            break
        var1 = 1
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var0 else 0):
            continue
        break
        break  # end loop
    var1 = 1
    if (1 if var4 == 0 else 0):
        break
    var0 = (var30 + (var27 * 286704))
    i32_store((var30 + (var27 * 286704)) + 283940, (i32_load(var0 + 283940) + 1))
    var24 = ((var32 * 404) + 9568096)
    var0 = i32_load(((var32 * 404) + 9568096) + 68)
    if i32_load(((var32 * 404) + 9568096) + 68):
        if (1 if i32_load(var12 + 16) < var0 else 0):
            break
    var0 = i32_load(var24 + 72)
    if i32_load(var24 + 72):
        if (1 if i32_load(var12 + 20) < var0 else 0):
            break
    var0 = i32_load(var24 + 76)
    if i32_load(var24 + 76):
        if (1 if i32_load(var12 + 24) < var0 else 0):
            break
    var0 = i32_load(var24 + 80)
    if i32_load(var24 + 80):
        if (1 if i32_load(var12 + 28) < var0 else 0):
            break
    var9 = 0
    var13 = 0
    var19 = i32_load(9671128)
    var23 = i32_load(9142432)
    if i32_load(9142432):
        var25 = i32_load(9142440)
        var13 = 1
        while True:  # loop $label20
            var1 = i32_load(((var9 << 2) + 58928))
            var0 = i32_load(((var11 + (i32_load(((var9 << 2) + 58928)) << 2)) + 284636))
            if (1 if i32_load(((var11 + (i32_load(((var9 << 2) + 58928)) << 2)) + 284636)) == 0 else 0):
                break
            var26 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var17 = ((var1 * 404) + 9568096)
            var29 = i32_load(var0)
            var16 = 0
            while True:  # loop $label19
                var0 = i32_load((var29 + (var16 << 2)))
                if (1 if i32_load((var29 + (var16 << 2))) == 0 else 0):
                    break
                var0 = (var19 + (var0 * 132))
                var15 = i32_load16_u((var19 + (var0 * 132)) + 112)
                var31 = (i32_load16_u((var19 + (var0 * 132)) + 112) + i32_load(var17 + 216))
                if (1 if (i32_load16_u((var19 + (var0 * 132)) + 112) + i32_load(var17 + 216)) <= var15 else 0):
                    break
                var1 = i32_load16_u(var0 + 114)
                var33 = (i32_load16_u(var0 + 114) + i32_load(var17 + 220))
                if (1 if (i32_load16_u(var0 + 114) + i32_load(var17 + 220)) <= var1 else 0):
                    break
                while True:  # loop $label18
                    var0 = var1
                    while True:  # loop $label17
                        if (1 if i32_load((var23 + (((var0 * var25) + var15) << 2))) == var4 else 0):
                            break
                        var0 = (var0 + 1)
                        if (1 if (var0 + 1) != var33 else 0):
                            continue
                        break  # end loop
                    var15 = (var15 + 1)
                    if (1 if (var15 + 1) != var31 else 0):
                        continue
                    break  # end loop
                var16 = (var16 + 1)
                if (1 if (var16 + 1) != var26 else 0):
                    continue
                break  # end loop
            var9 = (var9 + 1)
            var13 = (1 if (var9 + 1) < 3 else 0)
            if (1 if var9 != 3 else 0):
                continue
            break  # end loop
        break
    if var4:
        break
    var13 = 1
    while True:  # loop $label24
        var1 = i32_load(((var9 << 2) + 58928))
        var0 = i32_load(((var11 + (i32_load(((var9 << 2) + 58928)) << 2)) + 284636))
        if (1 if i32_load(((var11 + (i32_load(((var9 << 2) + 58928)) << 2)) + 284636)) == 0 else 0):
            break
        var15 = i32_load(var0 + 8)
        if (1 if i32_load(var0 + 8) == 0 else 0):
            break
        var1 = ((var1 * 404) + 9568096)
        var16 = i32_load(var0)
        var0 = 0
        while True:  # loop $label23
            var17 = i32_load((var16 + (var0 << 2)))
            if (1 if i32_load((var16 + (var0 << 2))) == 0 else 0):
                break
            var17 = (var19 + (var17 * 132))
            var23 = i32_load16_u((var19 + (var17 * 132)) + 112)
            if (1 if (i32_load16_u((var19 + (var17 * 132)) + 112) + i32_load(var1 + 216)) <= var23 else 0):
                break
            var17 = i32_load16_u(var17 + 114)
            if (1 if (i32_load16_u(var17 + 114) + i32_load(var1 + 220)) > var17 else 0):
                break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var15 else 0):
                continue
            break  # end loop
        var9 = (var9 + 1)
        var13 = (1 if (var9 + 1) < 3 else 0)
        if (1 if var9 != 3 else 0):
            continue
        break  # end loop
    if var13:
        break
    i32_store(var12 + 16, var18)
    i32_store(var12 + 4, var21)
    var18 = i32_load(9142440)
    if (1 if i32_load(9142440) < 2 else 0):
        break
    var17 = i32_load(var12 + 16)
    var13 = (i32_load(var12 + 16) - 1)
    var15 = i32_load(var12 + 4)
    var1 = (i32_load(var12 + 4) - 1)
    var21 = (var17 + 2)
    var16 = (var15 + 2)
    var19 = 1
    while True:  # loop $label39
        if (1 if var13 >= var21 else 0):
            break
        if (1 if var1 >= var16 else 0):
            break
        var25 = (var21 - 1)
        var26 = (var16 - 1)
        var23 = 1
        var9 = var13
        var29 = i32_load(9142432)
        if (1 if i32_load(9142432) == 0 else 0):
            while True:  # loop $label34
                if (1 if var9 >= var18 else 0):
                    break
                if (1 if var9 == var25 else 0):
                    break
                var0 = var1
                if (1 if var9 == var13 else 0):
                    break
                while True:  # loop $label31
                    if ((1 if var0 != var1 else 0) & (1 if var0 != var26 else 0)):
                        break
                    if (1 if var0 >= var18 else 0):
                        break
                    if (1 if (var0 | var9) < 0 else 0):
                        break
                    if var4:
                        break
                    break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var16 else 0):
                        continue
                    break  # end loop
                break
                var0 = var1
                if var4:
                    break
                while True:  # loop $label33
                    if (1 if var0 >= var18 else 0):
                        break
                    if (1 if (var0 | var9) < 0 else 0):
                        break
                    break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var16 else 0):
                        continue
                    break  # end loop
                var9 = (var9 + 1)
                var23 = (1 if (var9 + 1) < var21 else 0)
                if (1 if var9 != var21 else 0):
                    continue
                break
                break  # end loop
            raise RuntimeError('unreachable')
        while True:  # loop $label38
            var0 = var1
            if (1 if var9 < var18 else 0):
                while True:  # loop $label37
                    if (1 if var9 == var13 else 0):
                        break
                    if (1 if var0 == var1 else 0):
                        break
                    if (1 if var0 == var26 else 0):
                        break
                    if (1 if var9 != var25 else 0):
                        break
                    if (1 if var0 >= var18 else 0):
                        break
                    if (1 if (var0 | var9) < 0 else 0):
                        break
                    if (1 if i32_load((var29 + (((var0 * var18) + var9) << 2))) != var4 else 0):
                        break
                    break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var16 else 0):
                        continue
                    break  # end loop
            var9 = (var9 + 1)
            var23 = (1 if (var9 + 1) < var21 else 0)
            if (1 if var9 != var21 else 0):
                continue
            break  # end loop
        break
        i32_store(var12 + 16, var9)
        var15 = var0
        i32_store(var12 + 4, var0)
        if var23:
            break
        var18 = i32_load(9142440)
        var17 = i32_load(var12 + 16)
        var19 = (var19 + 1)
        var1 = (var15 - (var19 + 1))
        var0 = ((var19 << 1) | 1)
        var16 = ((var15 - (var19 + 1)) + ((var19 << 1) | 1))
        var13 = (var17 - var19)
        var21 = ((var17 - var19) + var0)
        if (1 if var18 > var19 else 0):
            continue
        break  # end loop
    var18 = i32_load(var12 + 16)
    var21 = i32_load(var12 + 4)
    var13 = 0
    var15 = 0
    var16 = i32_load(9671128)
    var17 = i32_load(9142432)
    if i32_load(9142432):
        var23 = i32_load(9142440)
        var0 = 2147483647
        while True:  # loop $label43
            var1 = i32_load(((var11 + (i32_load(((var13 << 2) + 58896)) << 2)) + 284636))
            if (1 if i32_load(((var11 + (i32_load(((var13 << 2) + 58896)) << 2)) + 284636)) == 0 else 0):
                break
            var25 = i32_load(var1 + 8)
            if (1 if i32_load(var1 + 8) == 0 else 0):
                break
            var26 = i32_load(var1)
            var9 = 0
            while True:  # loop $label42
                var1 = i32_load((var26 + (var9 << 2)))
                if (1 if i32_load((var26 + (var9 << 2))) == 0 else 0):
                    break
                var19 = (var16 + (var1 * 132))
                var29 = i32_load16_u((var16 + (var1 * 132)) + 114)
                var1 = (var21 - i32_load16_u((var16 + (var1 * 132)) + 114))
                var31 = i32_load16_u(var19 + 112)
                var1 = (var18 - i32_load16_u(var19 + 112))
                var1 = (((var21 - i32_load16_u((var16 + (var1 * 132)) + 114)) * var1) + ((var18 - i32_load16_u(var19 + 112)) * var1))
                if (1 if (((var21 - i32_load16_u((var16 + (var1 * 132)) + 114)) * var1) + ((var18 - i32_load16_u(var19 + 112)) * var1)) >= var0 else 0):
                    break
                if (1 if i32_load((var17 + (((var23 * var29) + var31) << 2))) != var10 else 0):
                    break
                var15 = i32_load(var19 + 28)
                var0 = var1
                var9 = (var9 + 1)
                if (1 if (var9 + 1) != var25 else 0):
                    continue
                break  # end loop
            var13 = (var13 + 1)
            if (1 if (var13 + 1) != 3 else 0):
                continue
            break  # end loop
        break
    if var10:
        break
    var0 = 2147483647
    while True:  # loop $label48
        var1 = i32_load(((var11 + (i32_load(((var13 << 2) + 58896)) << 2)) + 284636))
        if (1 if i32_load(((var11 + (i32_load(((var13 << 2) + 58896)) << 2)) + 284636)) == 0 else 0):
            break
        var19 = i32_load(var1 + 8)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        var17 = i32_load(var1)
        var9 = 0
        while True:  # loop $label47
            var1 = i32_load((var17 + (var9 << 2)))
            if (1 if i32_load((var17 + (var9 << 2))) == 0 else 0):
                break
            var10 = (var16 + (var1 * 132))
            var1 = (var21 - i32_load16_u((var16 + (var1 * 132)) + 114))
            var1 = (var18 - i32_load16_u(var10 + 112))
            var1 = (((var21 - i32_load16_u((var16 + (var1 * 132)) + 114)) * var1) + ((var18 - i32_load16_u(var10 + 112)) * var1))
            if (1 if (((var21 - i32_load16_u((var16 + (var1 * 132)) + 114)) * var1) + ((var18 - i32_load16_u(var10 + 112)) * var1)) >= var0 else 0):
                break
            var15 = i32_load(var10 + 28)
            var0 = var1
            var9 = (var9 + 1)
            if (1 if (var9 + 1) != var19 else 0):
                continue
            break  # end loop
        var13 = (var13 + 1)
        if (1 if (var13 + 1) != 3 else 0):
            continue
        break  # end loop
    var9 = var15
    if (1 if var15 == 0 else 0):
        break
    var10 = i32_load(9142440)
    var0 = 0
    while True:  # loop $label51
        var1 = var0
        var11 = (var0 << 2)
        var0 = (i32_load((((var0 << 2) | 4) + 8611904)) + var21)
        if (1 if var10 <= (i32_load((((var0 << 2) | 4) + 8611904)) + var21) else 0):
            break
        var11 = (i32_load((var11 + 8611904)) + var18)
        if (1 if var10 <= (i32_load((var11 + 8611904)) + var18) else 0):
            break
        if (1 if (var0 | var11) < 0 else 0):
            break
        if func56(var11, var0, var24, i32_load16_u(var14 + 110), 0, 0, 1, 1, 0):
            break
        var10 = i32_load(9142440)
        var0 = (var1 + 2)
        if (1 if var1 < 718 else 0):
            continue
        break  # end loop
    var30 = (var30 + (var27 * 286704))
    var18 = 0
    while True:  # loop $label76
        var0 = i32_load(((var30 + (i32_load(((var18 << 2) + 58940)) << 2)) + 284636))
        if (1 if i32_load(((var30 + (i32_load(((var18 << 2) + 58940)) << 2)) + 284636)) == 0 else 0):
            break
        var16 = i32_load(var0 + 8)
        if (1 if i32_load(var0 + 8) == 0 else 0):
            break
        var1 = 0
        var27 = i32_load(39216)
        var17 = i32_load(9561692)
        var19 = i32_load(9215880)
        var21 = i32_load(9142440)
        var11 = i32_load(9142432)
        var23 = i32_load(9671128)
        var32 = i32_load(var0)
        var24 = 1
        while True:  # loop $label62
            var0 = i32_load((var32 + (var1 << 2)))
            if (1 if i32_load((var32 + (var1 << 2))) == 0 else 0):
                break
            var13 = (var23 + (var0 * 132))
            var10 = ((i32_load8_u((var23 + (var0 * 132)) + 122) * 404) + 9568096)
            # br_table ['$label54', '$label55', '$label55', '$label55', '$label54', '$label55']
            _br_idx = i32_load(((i32_load8_u((var23 + (var0 * 132)) + 122) * 404) + 9568096) + 264)
            break  # br_table
            var0 = 0
            var25 = i32_load(var10 + 216)
            if (1 if i32_load(var10 + 216) == 0 else 0):
                break
            var26 = i32_load(var10 + 220)
            if (1 if i32_load(var10 + 220) == 0 else 0):
                break
            if (1 if var19 == 0 else 0):
                break
            if (1 if var11 == 0 else 0):
                break
            var29 = i32_load16_u(var13 + 114)
            var31 = i32_load16_u(var13 + 112)
            var33 = i32_load(var19)
            var15 = 0
            while True:  # loop $label58
                var34 = (var15 + var31)
                var9 = 0
                while True:  # loop $label57
                    var0 = i32_load((var11 + ((var34 + ((var9 + var29) * var21)) << 2)))
                    if (1 if i32_load((var33 + (i32_load((var11 + ((var34 + ((var9 + var29) * var21)) << 2))) << 2))) == 0 else 0):
                        break
                    var9 = (var9 + 1)
                    if (1 if (var9 + 1) != var26 else 0):
                        continue
                    break  # end loop
                var0 = 0
                var15 = (var15 + 1)
                if (1 if (var15 + 1) != var25 else 0):
                    continue
                break  # end loop
            break
            if (1 if var11 == 0 else 0):
                var0 = 0
                break
            var0 = i32_load((var11 + ((i32_load16_u(var13 + 112) + (var21 * i32_load16_u(var13 + 114))) << 2)))
            if (1 if var0 != var4 else 0):
                break
            if (1 if i32_load8_u(var13 + 123) == 38 else 0):
                break
            var25 = i32_load(var13 + 80)
            var0 = i32_load(var10 + 136)
            if (1 if i32_load(var13 + 80) >= ((((i32_load(var10 + 136) * 150) & 0xFFFFFFFF) // 100) if (1 if i32_load((((var17 + (i32_load16_u(var13 + 110) * 286704)) + (var27 << 2)) + 281808)) == 1 else 0) else var0) else 0):
                break
            # br_table ['$label59', '$label53', '$label53', '$label53', '$label53', '$label53', '$label53', '$label59', '$label53']
            _br_idx = i32_load8_u(var13 + 129)
            break  # br_table
            var0 = i32_load(var13 + 88)
            if (1 if i32_load(var13 + 88) == 0 else 0):
                break
            if var11:
            else:
            if (1 if 0 == var20 else 0):
                break
            var1 = (var1 + 1)
            var24 = (1 if (var1 + 1) < var16 else 0)
            if (1 if var1 != var16 else 0):
                continue
            break
            break  # end loop
        var0 = 0
        var1 = 0
        var15 = 0
        var11 = i32_load8_u(var28 + 122)
        var9 = ((i32_load8_u(var28 + 122) * 404) + 9568096)
        # br_table ['$label63', '$label64', '$label64', '$label64', '$label63', '$label64']
        _br_idx = i32_load(((i32_load8_u(var28 + 122) * 404) + 9568096) + 264)
        break  # br_table
        var19 = i32_load(var9 + 216)
        if (1 if i32_load(var9 + 216) == 0 else 0):
            break
        var16 = i32_load(9142432)
        var27 = i32_load(((var11 * 404) + 9568096) + 220)
        if (1 if i32_load(((var11 * 404) + 9568096) + 220) == 0 else 0):
            break
        var0 = i32_load16_u(var28 + 114)
        var1 = i32_load16_u(var28 + 112)
        if (1 if var16 == 0 else 0):
            break
        var17 = i32_load(9142440)
        var23 = i32_load(i32_load(9215880))
        while True:  # loop $label69
            var11 = (var1 + var15)
            var10 = 0
            while True:  # loop $label67
                var9 = (var0 + var10)
                if i32_load((var23 + (i32_load((var16 + ((((var0 + var10) * var17) + var11) << 2))) << 2))):
                    var10 = (var10 + 1)
                    if (1 if var27 != (var10 + 1) else 0):
                        continue
                    break
                break  # end loop
            var1 = var11
            var0 = var9
            break
            var15 = (var15 + 1)
            if (1 if (var15 + 1) != var19 else 0):
                continue
            break  # end loop
        break
        var0 = i32_load16_u(var28 + 114)
        var1 = i32_load16_u(var28 + 112)
        var16 = i32_load(9142432)
        if i32_load(9142432):
            var9 = i32_load(var12 + 8)
            var15 = i32_load(var12 + 12)
            while True:  # loop $label71
                var10 = (var0 - var9)
                var11 = (var1 - var15)
                if (1 if (var1 - var15) == 0 else 0):
                    break
                if (1 if var0 == var9 else 0):
                    break
                var11 = (var10 // var11)
                var11 = (var11 >> 31)
                var11 = (var11 if (1 if (((var10 // var11) ^ (var11 >> 31)) - var11) <= 1 else 0) else 0)
                var9 = ((var11 if (1 if (((var10 // var11) ^ (var11 >> 31)) - var11) <= 1 else 0) else 0) // var10)
                var9 = (var9 >> 31)
                var10 = (var10 if (1 if ((((var11 if (1 if (((var10 // var11) ^ (var11 >> 31)) - var11) <= 1 else 0) else 0) // var10) ^ (var9 >> 31)) - var9) <= 1 else 0) else 0)
                i32_store(var12 + 12, ((-1 if (1 if var11 < 0 else 0) else (1 if var11 != 0 else 0)) + var15))
                var9 = (i32_load(var12 + 8) + (-1 if (1 if var10 < 0 else 0) else (1 if var10 != 0 else 0)))
                i32_store(var12 + 8, (i32_load(var12 + 8) + (-1 if (1 if var10 < 0 else 0) else (1 if var10 != 0 else 0))))
                var15 = i32_load(var12 + 12)
                if (1 if i32_load((var16 + ((i32_load(var12 + 12) + (i32_load(9142440) * var9)) << 2))) != var20 else 0):
                    continue
                break  # end loop
            break
        if var20:
            var9 = i32_load(var12 + 8)
            while True:  # loop $label74
                var10 = (var0 - var9)
                var2 = i32_load(var12 + 12)
                var11 = (var1 - i32_load(var12 + 12))
                if (1 if (var1 - i32_load(var12 + 12)) == 0 else 0):
                    break
                if (1 if var0 == var9 else 0):
                    break
                var3 = (var10 // var11)
                var3 = (var3 >> 31)
                var11 = (var11 if (1 if (((var10 // var11) ^ (var3 >> 31)) - var3) <= 1 else 0) else 0)
                var3 = ((var11 if (1 if (((var10 // var11) ^ (var3 >> 31)) - var3) <= 1 else 0) else 0) // var10)
                var3 = (var3 >> 31)
                var10 = (var10 if (1 if ((((var11 if (1 if (((var10 // var11) ^ (var3 >> 31)) - var3) <= 1 else 0) else 0) // var10) ^ (var3 >> 31)) - var3) <= 1 else 0) else 0)
                i32_store(var12 + 12, ((-1 if (1 if var11 < 0 else 0) else (1 if var11 != 0 else 0)) + var2))
                var9 = (i32_load(var12 + 8) + (-1 if (1 if var10 < 0 else 0) else (1 if var10 != 0 else 0)))
                i32_store(var12 + 8, (i32_load(var12 + 8) + (-1 if (1 if var10 < 0 else 0) else (1 if var10 != 0 else 0))))
                continue
                break  # end loop
            raise RuntimeError('unreachable')
        var9 = i32_load(var12 + 8)
        var10 = (var0 - i32_load(var12 + 8))
        var1 = i32_load(var12 + 12)
        var11 = (var1 - i32_load(var12 + 12))
        if (1 if (var1 - i32_load(var12 + 12)) == 0 else 0):
            break
        if (1 if var0 == var9 else 0):
            break
        var0 = (var10 // var11)
        var0 = (var0 >> 31)
        var11 = (var11 if (1 if (((var10 // var11) ^ (var0 >> 31)) - var0) <= 1 else 0) else 0)
        var0 = ((var11 if (1 if (((var10 // var11) ^ (var0 >> 31)) - var0) <= 1 else 0) else 0) // var10)
        var0 = (var0 >> 31)
        var10 = (var10 if (1 if ((((var11 if (1 if (((var10 // var11) ^ (var0 >> 31)) - var0) <= 1 else 0) else 0) // var10) ^ (var0 >> 31)) - var0) <= 1 else 0) else 0)
        i32_store(var12 + 12, ((-1 if (1 if var11 < 0 else 0) else (1 if var11 != 0 else 0)) + var1))
        i32_store(var12 + 8, (i32_load(var12 + 8) + (-1 if (1 if var10 < 0 else 0) else (1 if var10 != 0 else 0))))
        i32_store(var13 + 88, (i32_load(var12 + 12) + (var21 * i32_load(var12 + 8))))
        i32_store(var13 + 80, (var25 + 1))
        if (1 if var24 == 0 else 0):
            break
        var1 = 2
        break
        var1 = 1
        var18 = (var18 + 1)
        if (1 if (var18 + 1) != 3 else 0):
            continue
        break  # end loop
    break
    var0 = (var9 * 132)
    func261(var32, var11, var0, ((var9 * 132) + i32_load(9671128)))
    if i32_load(i32_load(9142424) + 156):
        func29((i32_load(9671128) + var0), 1)
    var1 = 1
    global global0
    global0 = (var12 + 32)
    # br_table ['$label77', '$label78', '$label0', '$label78']
    _br_idx = var1
    break  # br_table
    if (1 if i32_load(var14 + 44) == 0 else 0):
        break
    var0 = i32_load(var14 + 20)
    if i32_load(var14 + 20):
        i32_store(var0 + 8, 0)
    func92(var14, 0.0, 0.0)
    func29(var14, 1)
    break
    var0 = i32_load(((i32_load((i32_load(9215884) + (i32_load(var14 + 44) << 4)) + 4) * 40) + 9671200) + 32)
    if i32_load(((i32_load((i32_load(9215884) + (i32_load(var14 + 44) << 4)) + 4) * 40) + 9671200) + 32):
        # call_indirect via table[var0]
    if (1 if var2 != 6 else 0):
        break
    if (1 if var8 == 0 else 0):
        break
    var11 = i32_load(9215884)
    var9 = i32_load(var14 + 44)
    if (1 if i32_load((i32_load(9215884) + (i32_load(var14 + 44) << 4)) + 4) != 6 else 0):
        break
    var4 = i32_load(var14 + 28)
    var1 = 0
    var20 = i32_load(9671128)
    var10 = i32_load(var22 + 28)
    var0 = (i32_load(9671128) + (i32_load(var22 + 28) * 132))
    var3 = i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(var22 + 28) * 132)) + 122) * 404) + 9568096) + 216)
    if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(var22 + 28) * 132)) + 122) * 404) + 9568096) + 216) == 0 else 0):
        break
    var13 = i32_load16_u(var0 + 114)
    var1 = (var20 + (var4 * 132))
    var20 = i32_load16_u((var20 + (var4 * 132)) + 114)
    var15 = i32_load16_u(var0 + 112)
    var28 = i32_load16_u(var1 + 112)
    var0 = i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 224)
    var12 = (i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 224) * var0)
    var0 = 0
    var1 = 1
    while True:  # loop $label82
        var4 = (var20 - (var0 + var13))
        var18 = (((var20 - (var0 + var13)) * var4) - 1)
        var4 = 0
        while True:  # loop $label81
            var21 = (var28 - (var4 + var15))
            if (1 if (var18 + ((var28 - (var4 + var15)) * var21)) <= var12 else 0):
                break
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var3 else 0):
                continue
            break  # end loop
        var0 = (var0 + 1)
        var1 = (1 if (var0 + 1) < var3 else 0)
        if (1 if var0 != var3 else 0):
            continue
        break  # end loop
    if (1 if var1 == 0 else 0):
        break
    if (1 if var6 != -1 else 0):
        i32_store8(var14 + 129, var6)
    i32_store((var11 + ((var9 << 4) | 12)), var10)
    var3 = 0
    break
    if (1 if i32_load8_u(var14 + 127) != 1 else 0):
        break
    i32_store8(var14 + 127, 0)
    var0 = i32_load(var14 + 40)
    if (1 if i32_load(var14 + 40) == 0 else 0):
        break
    if (1 if i32_load8_u(9142916) == 0 else 0):
        break
    i32_store(var22 + 4, var0)
    i32_store(var22, 0)
    a_b()
    if (1 if var6 == -1 else 0):
        break
    if (1 if i32_load8_u(var14 + 129) == var6 else 0):
        break
    i32_store8(var14 + 129, var6)
    var1 = 1
    i32_store8(var14 + 123, var2)
    i32_store(var14 + 56, 0)
    i32_store(var14 + 96, var5)
    var0 = i32_load(var22 + 28)
    if (1 if i32_load(var22 + 28) >= 3 else 0):
        var2 = i32_load(var14 + 32)
        i32_store(var14 + 32, var0)
        var1 = (var1 | ((1 if var6 == 9 else 0) & (1 if var0 != var2 else 0)))
        break
    i32_store16(var14 + 116, i32_load(var22 + 24))
    var0 = i32_load(var22 + 20)
    i32_store(var14 + 32, 0)
    i32_store16(var14 + 118, var0)
    var3 = 1
    if (1 if i32_load8_u(var14 + 125) == 1 else 0):
        break
    if (1 if var8 == 0 else 0):
        break
    if (1 if i32_load((i32_load(9215884) + (i32_load(var14 + 44) << 4)) + 4) != 6 else 0):
        break
    var0 = i32_load8_u(var14 + 129)
    if (1 if i32_load8_u(var14 + 129) == 5 else 0):
        break
    if (1 if (var1 | (1 if var0 != 9 else 0)) == 0 else 0):
        break
    i32_store8(var14 + 125, 1)
    func63(var22, var14, 0, 1, var7)
    global global0
    global0 = (var22 + 32)
    return var3

