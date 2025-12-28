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
# $func895
# ==========================================================
def func895(var0, var1, param2):
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
    var6 = i32_load(9671128)
    var10 = (i32_load(9671128) + (var1 * 132))
    var2 = i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122)
    var7 = (var6 + (var0 * 132))
    if (1 if i32_load8_u((var6 + (var0 * 132)) + 125) == 1 else 0):
        var2 = ((var2 * 404) + 9568096)
        var12 = i32_load(((var2 * 404) + 9568096) + 220)
        var4 = i32_load16_u(var10 + 114)
        var5 = (i32_load(((var2 * 404) + 9568096) + 220) + i32_load16_u(var10 + 114))
        var14 = i32_load(var2 + 216)
        var10 = i32_load16_u(var10 + 112)
        var13 = (i32_load(var2 + 216) + i32_load16_u(var10 + 112))
        var2 = i32_load16_u(var7 + 114)
        var3 = i32_load16_u(var7 + 112)
        var15 = (1 if i32_load16_u(var7 + 112) < var10 else 0)
        if (1 if i32_load16_u(var7 + 112) < var10 else 0):
            break
        if (1 if var3 >= var13 else 0):
            break
        if (1 if var2 < var4 else 0):
            break
        if (1 if var2 >= var5 else 0):
            break
        var4 = ((var12 // 2) + var4)
        var2 = (-1 if (1 if var2 > var4 else 0) else (1 if ((var12 // 2) + var4) != var2 else 0))
        var4 = ((var14 // 2) + var10)
        break
        var2 = (1 if (1 if var2 < var4 else 0) else (-1 if (1 if var2 >= var5 else 0) else 0))
        var3 = (1 if var15 else (-1 if (1 if var3 >= var13 else 0) else 0))
        var4 = 6
        var2 = (((var2 * 3) + var3) + 4)
        if (1 if (((var2 * 3) + var3) + 4) <= 8 else 0):
            var4 = i32_load8_u((var2 + 10184))
        var2 = (var6 + (var0 * 132))
        i32_store8((var6 + (var0 * 132)) + 124, var4)
        var3 = i32_load(((i32_load((i32_load(9215884) + (i32_load(var2 + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if i32_load(((i32_load((i32_load(9215884) + (i32_load(var2 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            # call_indirect via table[var3]
        if (1 if i32_load8_u(var7 + 125) == 3 else 0):
            break
        var4 = i32_load(var2 + 44)
        if i32_load(var2 + 44):
            var7 = i32_load(9142848)
            var3 = i32_load(9215884)
            i32_store((i32_load(9215884) + (var4 << 4)) + 4, 54)
            i32_store((var3 + (i32_load(var2 + 44) << 4)) + 8, i32_load((var6 + (var0 * 132)) + 28))
            i32_store((var3 + (i32_load(var2 + 44) << 4)) + 12, var1)
            i32_store((var3 + (i32_load(var2 + 44) << 4)), (var7 + 40))
            return call_indirect(var3)
        i32_store(var2 + 44, ((Ua(1000, 54, i32_load((var6 + (var0 * 132)) + 28), var1) & 0xFFFFFFFF) >> 2))
        return (i32_load(9671128) + (i32_load(var2 + 28) * 132))
    if (1 if i32_load8_u(var10 + 125) != 3 else 0):
        var3 = i32_load16_u((var6 + (var0 * 132)) + 110)
        var4 = i32_load16_u((var6 + (var1 * 132)) + 110)
        if i32_load8_u((i32_load(9143004) + (i32_load16_u((var6 + (var0 * 132)) + 110) + (i32_load16_u((var6 + (var1 * 132)) + 110) * i32_load(9142892))))):
            break
    func29(var7, 1)
    return func37(var7, i32_load(((i32_load8_u(var2 + 122) * 72) + 9263856) + 16), 0.0, 0)
    if (1 if var3 == var4 else 0):
        var4 = i32_load((var6 + (var1 * 132)) + 84)
        break
    func103(var10)
    var3 = (var6 + (var1 * 132))
    var4 = i32_load((var6 + (var1 * 132)) + 84)
    if (1 if i32_load((var6 + (var1 * 132)) + 84) < 6 else 0):
        break
    var2 = i32_load8_u(var10 + 122)
    var3 = -5
    var5 = (var6 + (var1 * 132))
    var3 = (var3 + var4)
    i32_store((var6 + (var1 * 132)) + 84, (var3 + var4))
    var2 = i32_load(((var2 * 404) + 9568096) + 112)
    if (1 if var3 <= i32_load(((var2 * 404) + 9568096) + 112) else 0):
        break
    i32_store(var5 + 84, var2)
    if (1 if i32_load(var5 + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var6 + (var1 * 132)) + 28) else 0):
            break
    func29(var7, 1)
    return func28(1, 1)
    i32_store(var3 + 84, 1)
    var13 = i32_load(9142892)
    if i32_load(9142892):
        # Unknown: memory.fill []
    var3 = ((var2 * 404) + 9568096)
    var20 = i32_load(((var2 * 404) + 9568096) + 216)
    var7 = (var6 + (var0 * 132))
    var4 = i32_load16_u((var6 + (var0 * 132)) + 112)
    var21 = (i32_load(((var2 * 404) + 9568096) + 216) + i32_load16_u((var6 + (var0 * 132)) + 112))
    if (1 if (i32_load(((var2 * 404) + 9568096) + 216) + i32_load16_u((var6 + (var0 * 132)) + 112)) <= var4 else 0):
        break
    var7 = i32_load16_u(var7 + 114)
    var22 = (i32_load16_u(var7 + 114) + i32_load(var3 + 220))
    if (1 if (i32_load16_u(var7 + 114) + i32_load(var3 + 220)) <= var7 else 0):
        break
    var14 = (var6 + (var1 * 132))
    var15 = i32_load(9215884)
    var16 = i32_load(9671128)
    var17 = i32_load(9142840)
    var19 = i32_load(9142440)
    var12 = (i32_load(9142440) + 2)
    var23 = ((i32_load(9142440) + 2) << 1)
    var24 = i32_load(((var2 * 404) + 9568096) + 372)
    var2 = var4
    while True:  # loop $label14
        var25 = (var2 - var4)
        var3 = var7
        while True:  # loop $label13
            var5 = 0
            if i32_load8_u((var24 + (var25 + ((var3 - var7) * var20)))):
                while True:  # loop $label12
                    var11 = (var5 << 3)
                    var9 = (i32_load(((var5 << 3) + 8932)) + var3)
                    if (1 if var19 <= (i32_load(((var5 << 3) + 8932)) + var3) else 0):
                        break
                    var11 = (i32_load((var11 + 8928)) + var2)
                    if (1 if var19 <= (i32_load((var11 + 8928)) + var2) else 0):
                        break
                    if (1 if (var9 | var11) < 0 else 0):
                        break
                    var11 = (var11 + 1)
                    var9 = (var9 + 1)
                    var8 = i32_load((var17 + (((var11 + 1) + ((var9 + 1) * var12)) << 2)))
                    if (1 if i32_load((var17 + (((var11 + 1) + ((var9 + 1) * var12)) << 2))) < 3 else 0):
                        break
                    if (1 if var1 == var8 else 0):
                        break
                    var8 = (var16 + (var8 * 132))
                    var18 = i32_load16_u((var16 + (var8 * 132)) + 110)
                    if (1 if i32_load16_u((var16 + (var8 * 132)) + 110) == 0 else 0):
                        break
                    if (1 if i32_load8_u(var8 + 123) != 54 else 0):
                        break
                    if (1 if i32_load((var15 + (i32_load(var8 + 44) << 4)) + 12) != i32_load(var14 + 28) else 0):
                        break
                    var8 = ((var18 << 2) + 59200)
                    i32_store(((var18 << 2) + 59200), (i32_load(var8) + 1))
                    var8 = i32_load((var17 + ((var11 + ((var9 + var12) * var12)) << 2)))
                    if (1 if i32_load((var17 + ((var11 + ((var9 + var12) * var12)) << 2))) < 3 else 0):
                        break
                    if (1 if var1 == var8 else 0):
                        break
                    var8 = (var16 + (var8 * 132))
                    var18 = i32_load16_u((var16 + (var8 * 132)) + 110)
                    if (1 if i32_load16_u((var16 + (var8 * 132)) + 110) == 0 else 0):
                        break
                    if (1 if i32_load8_u(var8 + 123) != 54 else 0):
                        break
                    if (1 if i32_load((var15 + (i32_load(var8 + 44) << 4)) + 12) != i32_load(var14 + 28) else 0):
                        break
                    var8 = ((var18 << 2) + 59200)
                    i32_store(((var18 << 2) + 59200), (i32_load(var8) + 1))
                    var9 = i32_load((var17 + ((var11 + ((var9 + var23) * var12)) << 2)))
                    if (1 if i32_load((var17 + ((var11 + ((var9 + var23) * var12)) << 2))) < 3 else 0):
                        break
                    if (1 if var1 == var9 else 0):
                        break
                    var9 = (var16 + (var9 * 132))
                    var11 = i32_load16_u((var16 + (var9 * 132)) + 110)
                    if (1 if i32_load16_u((var16 + (var9 * 132)) + 110) == 0 else 0):
                        break
                    if (1 if i32_load8_u(var9 + 123) != 54 else 0):
                        break
                    if (1 if i32_load((var15 + (i32_load(var9 + 44) << 4)) + 12) != i32_load(var14 + 28) else 0):
                        break
                    var9 = ((var11 << 2) + 59200)
                    i32_store(((var11 << 2) + 59200), (i32_load(var9) + 1))
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != 8 else 0):
                        continue
                    break  # end loop
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var22 else 0):
                continue
            break  # end loop
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var21 else 0):
            continue
        break  # end loop
    if (1 if var13 == 0 else 0):
        break
    var4 = 0
    var5 = 0
    var2 = 0
    if (1 if var13 >= 4 else 0):
        var7 = (var13 & -4)
        var3 = 0
        while True:  # loop $label15
            var12 = (var5 | 3)
            var14 = (var5 | 2)
            var15 = (var5 | 1)
            var2 = (var5 if (1 if i32_load(((var5 << 2) + 59200)) > i32_load(((var2 << 2) + 59200)) else 0) else var2)
            var2 = ((var5 | 1) if (1 if i32_load(((var15 << 2) + 59200)) > i32_load(((var2 << 2) + 59200)) else 0) else (var5 if (1 if i32_load(((var5 << 2) + 59200)) > i32_load(((var2 << 2) + 59200)) else 0) else var2))
            var2 = ((var5 | 2) if (1 if i32_load(((var14 << 2) + 59200)) > i32_load(((var2 << 2) + 59200)) else 0) else ((var5 | 1) if (1 if i32_load(((var15 << 2) + 59200)) > i32_load(((var2 << 2) + 59200)) else 0) else (var5 if (1 if i32_load(((var5 << 2) + 59200)) > i32_load(((var2 << 2) + 59200)) else 0) else var2)))
            var2 = ((var5 | 3) if (1 if i32_load(((var12 << 2) + 59200)) > i32_load(((var2 << 2) + 59200)) else 0) else ((var5 | 2) if (1 if i32_load(((var14 << 2) + 59200)) > i32_load(((var2 << 2) + 59200)) else 0) else ((var5 | 1) if (1 if i32_load(((var15 << 2) + 59200)) > i32_load(((var2 << 2) + 59200)) else 0) else (var5 if (1 if i32_load(((var5 << 2) + 59200)) > i32_load(((var2 << 2) + 59200)) else 0) else var2))))
            var5 = (var5 + 4)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var7 else 0):
                continue
            break  # end loop
    var3 = (var13 & 3)
    if (var13 & 3):
        while True:  # loop $label16
            var2 = (var5 if (1 if i32_load(((var5 << 2) + 59200)) > i32_load(((var2 << 2) + 59200)) else 0) else var2)
            var5 = (var5 + 1)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var3 else 0):
                continue
            break  # end loop
    if (1 if var2 == 0 else 0):
        break
    func78(var10, var2, 1, 1)
    if (1 if i32_load((var6 + (var1 * 132)) + 92) == 0 else 0):
        break
    var2 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var6 + (var1 * 132)) + 28) else 0):
            break
    if (1 if i32_load((var6 + (var1 * 132)) + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var6 + (var1 * 132)) + 28) else 0):
            break
    i32_store((i32_load(9215884) + (i32_load((var6 + (var0 * 132)) + 44) << 4)), (i32_load(9142848) + 40))
    return func28(1, 1)


# ==========================================================
# $func916
# ==========================================================
def func916(var0, var1):
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
    var4 = (i32_load(9671128) + (var0 * 132))
    var7 = i32_load16_u(var4 + 116)
    var8 = i32_load16_u(var4 + 118)
    var0 = i32_load(((i32_load(9561692) + (i32_load16_u(var4 + 110) * 286704)) + 284140))
    var1 = (var7 - i32_load(((i32_load(9561692) + (i32_load16_u(var4 + 110) * 286704)) + 284140)))
    var5 = (var0 << 1)
    var10 = (var7 + (var0 << 1))
    if (1 if (var7 - i32_load(((i32_load(9561692) + (i32_load16_u(var4 + 110) * 286704)) + 284140))) >= (var7 + (var0 << 1)) else 0):
        break
    var11 = (var8 - var0)
    var12 = (var5 + var8)
    if (1 if (var8 - var0) >= (var5 + var8) else 0):
        break
    var13 = (var0 * var0)
    while True:  # loop $label5
        var5 = (var1 + 1)
        var0 = (var1 - var7)
        var14 = (((var1 - var7) * var0) - 1)
        var0 = var11
        while True:  # loop $label4
            var2 = (var0 - var8)
            if (1 if (var14 + ((var0 - var8) * var2)) > var13 else 0):
                break
            var2 = i32_load(9142440)
            if (1 if i32_load(9142440) <= var0 else 0):
                break
            if (1 if (var0 | var1) < 0 else 0):
                break
            if (1 if var1 >= var2 else 0):
                break
            var6 = i32_load(9142840)
            var9 = (var0 + 1)
            var2 = (var2 + 2)
            var3 = i32_load((i32_load(9142840) + ((var5 + ((var0 + 1) * (var2 + 2))) << 2)))
            if (1 if i32_load((i32_load(9142840) + ((var5 + ((var0 + 1) * (var2 + 2))) << 2))) <= 2 else 0):
                break
            var3 = (i32_load(9671128) + (var3 * 132))
            if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var3 * 132)) + 122) * 404) + 9568096) + 296) == 0 else 0):
                break
            if i32_load8_u((i32_load(9143004) + (i32_load16_u(var4 + 110) + (i32_load(9142892) * i32_load16_u(var3 + 110))))):
                break
            func206(var3)
            var2 = (i32_load(9142440) + 2)
            var6 = i32_load(9142840)
            var3 = i32_load((var6 + ((var5 + ((var2 + var9) * var2)) << 2)))
            if (1 if i32_load((var6 + ((var5 + ((var2 + var9) * var2)) << 2))) < 3 else 0):
                break
            var3 = (i32_load(9671128) + (var3 * 132))
            if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var3 * 132)) + 122) * 404) + 9568096) + 296) == 0 else 0):
                break
            if i32_load8_u((i32_load(9143004) + (i32_load16_u(var4 + 110) + (i32_load(9142892) * i32_load16_u(var3 + 110))))):
                break
            func206(var3)
            var2 = (i32_load(9142440) + 2)
            var6 = i32_load(9142840)
            var2 = i32_load((var6 + ((var5 + ((var9 + (var2 << 1)) * var2)) << 2)))
            if (1 if i32_load((var6 + ((var5 + ((var9 + (var2 << 1)) * var2)) << 2))) < 3 else 0):
                break
            var2 = (i32_load(9671128) + (var2 * 132))
            if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122) * 404) + 9568096) + 296) == 0 else 0):
                break
            if i32_load8_u((i32_load(9143004) + (i32_load16_u(var4 + 110) + (i32_load(9142892) * i32_load16_u(var2 + 110))))):
                break
            func206(var2)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var12 else 0):
                continue
            break  # end loop
        var1 = var5
        if (1 if var5 != var10 else 0):
            continue
        break  # end loop

