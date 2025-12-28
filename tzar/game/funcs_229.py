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
# $func87
# ==========================================================
def func87(var0, var1):
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
    var24 = 0.0
    var25 = 0.0
    var4 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var19 = i32_load(9561692)
    var17 = (1 if (1 if i32_load(38504) == var1 else 0) else 4)
    i32_store8(var0 + 129, (1 if (1 if i32_load(38504) == var1 else 0) else 4))
    var1 = i32_load(((var19 + (var1 << 2)) + 284636))
    if (1 if i32_load(((var19 + (var1 << 2)) + 284636)) == 0 else 0):
        break
    var20 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    var21 = i32_load16_u(var0 + 110)
    var22 = (var19 + (i32_load16_u(var0 + 110) * 286704))
    var9 = ((var19 + (i32_load16_u(var0 + 110) * 286704)) + 283872)
    var10 = (var22 + 283876)
    var11 = i32_load(var22 + 283960)
    var14 = (((var19 + (var21 * 286704)) + (i32_load(((i32_load(var22 + 283960) << 2) + 9940)) << 2)) + 284636)
    var13 = i32_load(9215884)
    var15 = i32_load(9671128)
    var8 = i32_load(var1)
    var24 = -1.0
    while True:  # loop $label5
        var1 = i32_load((var8 + (var16 << 2)))
        if (1 if i32_load((var8 + (var16 << 2))) == 0 else 0):
            break
        var18 = (var15 + (var1 * 132))
        if (1 if i32_load8_u((var15 + (var1 * 132)) + 125) == 3 else 0):
            break
        var1 = (i32_load(var10) - i32_load16_u(var18 + 114))
        var1 = (i32_load(var9) - i32_load16_u(var18 + 112))
        var25 = f32((math.sqrt(float((((i32_load(var10) - i32_load16_u(var18 + 114)) * var1) + ((i32_load(var9) - i32_load16_u(var18 + 112)) * var1)))) + float(float((((i32_load(var18 + 68) - i32_load(var18 + 64)) & 0xFFFFFFFF) // 100)))))
        if (1 if ((1 if var24 < 0.0 else 0) | (1 if f32((math.sqrt(float((((i32_load(var10) - i32_load16_u(var18 + 114)) * var1) + ((i32_load(var9) - i32_load16_u(var18 + 112)) * var1)))) + float(float((((i32_load(var18 + 68) - i32_load(var18 + 64)) & 0xFFFFFFFF) // 100))))) < var24 else 0)) == 0 else 0):
            break
        var7 = 0
        var1 = i32_load(var14)
        if (1 if i32_load(var14) == 0 else 0):
            break
        var2 = i32_load(var1 + 8)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        var6 = i32_load(var1)
        var1 = 0
        while True:  # loop $label4
            var5 = i32_load((var6 + (var1 << 2)))
            if (1 if i32_load((var6 + (var1 << 2))) == 0 else 0):
                break
            var5 = (var15 + (var5 * 132))
            if (1 if i32_load8_u((var15 + (var5 * 132)) + 129) != var17 else 0):
                break
            var3 = i32_load(var18 + 28)
            if (1 if i32_load(var18 + 28) != i32_load(var5 + 32) else 0):
                var5 = i32_load(var5 + 44)
                if (1 if i32_load((var13 + (i32_load(var5 + 44) << 4)) + 4) != 1 else 0):
                    break
                if (1 if i32_load((var13 + ((var5 << 4) | 12))) != var3 else 0):
                    break
            var7 = (var7 + 1)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var2 else 0):
                continue
            break  # end loop
        var1 = (1 if var7 < 20 else 0)
        var12 = (i32_load(var18 + 28) if (1 if var7 < 20 else 0) else var12)
        var24 = (var25 if var1 else var24)
        var23 = (var7 if var1 else var23)
        var16 = (var16 + 1)
        if (1 if (var16 + 1) != var20 else 0):
            continue
        break  # end loop
    if (1 if var12 == 0 else 0):
        var2 = 0
        break
    var7 = 0
    var17 = i32_load(9671128)
    var2 = i32_load8_u((i32_load(9671128) + (var12 * 132)) + 122)
    var20 = i32_load(((var11 << 2) + 9687164))
    var9 = i32_load((((var19 + (var21 * 286704)) + (i32_load(((var11 << 2) + 9687164)) << 2)) + 284636))
    if (1 if i32_load((((var19 + (var21 * 286704)) + (i32_load(((var11 << 2) + 9687164)) << 2)) + 284636)) == 0 else 0):
        break
    var10 = i32_load(var9 + 8)
    if (1 if i32_load(var9 + 8) == 0 else 0):
        break
    var6 = (var17 + (var12 * 132))
    var1 = 0
    while True:  # loop $label9
        var11 = i32_load((i32_load(var9) + (var1 << 2)))
        if (1 if i32_load((i32_load(var9) + (var1 << 2))) == 0 else 0):
            break
        var14 = i32_load(9671128)
        var8 = (i32_load(9671128) + (var11 * 132))
        var3 = i32_load8_u((i32_load(9671128) + (var11 * 132)) + 125)
        if (1 if i32_load8_u((i32_load(9671128) + (var11 * 132)) + 125) == 3 else 0):
            break
        var5 = i32_load(var8 + 96)
        if (1 if i32_load(var8 + 96) == i32_load(var6 + 28) else 0):
            if var3:
                break
            var7 = (var7 + 1)
            break
        if (1 if i32_load8_u((var14 + (var5 * 132)) + 125) != 3 else 0):
            break
        var10 = i32_load(var9 + 8)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < var10 else 0):
            continue
        break  # end loop
    if (1 if ((1 if var7 < 4 else 0) & (1 if var7 <= ((var23 & 0xFFFFFFFF) // 6) else 0)) == 0 else 0):
        var2 = 1
        break
    var2 = i32_load(((var2 * 404) + 9568096) + 216)
    var13 = ((var20 * 404) + 9568096)
    var1 = i32_load(((var20 * 404) + 9568096) + 216)
    var15 = ((var19 + (var21 * 286704)) + 283908)
    var8 = (var17 + (var12 * 132))
    var6 = i32_load16_u((var17 + (var12 * 132)) + 112)
    var3 = i32_load16_u(var8 + 114)
    var5 = (i32_load16_u(var8 + 114) + (i32_load(var13 + 220) ^ -1))
    if (1 if func73(i32_load16_u((var17 + (var12 * 132)) + 112), (i32_load16_u(var8 + 114) + (i32_load(var13 + 220) ^ -1)), var13, 0, 0, 1) == 0 else 0):
        break
    if (1 if func108(var6, var5, i32_load(var15), 7) == 0 else 0):
        break
    var1 = var6
    break
    var2 = (var2 + 1)
    var5 = ((var2 + 1) + var3)
    if (1 if func73(var6, ((var2 + 1) + var3), var13, 0, 0, 1) == 0 else 0):
        break
    if (1 if func108(var6, var5, i32_load(var15), 7) == 0 else 0):
        break
    var1 = var6
    break
    var1 = ((var1 ^ -1) + var6)
    if (1 if func73(((var1 ^ -1) + var6), var3, var13, 0, 0, 1) == 0 else 0):
        break
    if (1 if func108(var1, var3, i32_load(var15), 7) == 0 else 0):
        break
    var5 = var3
    break
    var1 = (var2 + var6)
    if (1 if func73((var2 + var6), var3, var13, 0, 0, 1) == 0 else 0):
        break
    if (1 if func108(var1, var3, i32_load(var15), 7) == 0 else 0):
        break
    var5 = var3
    break
    if var7:
        break
    var16 = i32_load(9142440)
    var14 = 2147483647
    var2 = 0
    while True:  # loop $label17
        var8 = var2
        var2 = (var2 << 2)
        var9 = i32_load((((var2 << 2) | 4) + 8611904))
        var10 = (i32_load((((var2 << 2) | 4) + 8611904)) + var3)
        if (1 if var16 <= (i32_load((((var2 << 2) | 4) + 8611904)) + var3) else 0):
            break
        var2 = i32_load((var2 + 8611904))
        var11 = (i32_load((var2 + 8611904)) + var6)
        if (1 if var16 <= (i32_load((var2 + 8611904)) + var6) else 0):
            break
        if (1 if (var10 | var11) < 0 else 0):
            break
        var2 = ((var9 * var9) + (var2 * var2))
        if (1 if ((var9 * var9) + (var2 * var2)) >= var14 else 0):
            break
        var9 = func73(var11, var10, var13, 0, 0, 1)
        var16 = i32_load(9142440)
        if (1 if var9 == 0 else 0):
            break
        if (1 if func108(var11, var10, i32_load(var15), 7) == 0 else 0):
            break
        var1 = var11
        var5 = var10
        var14 = var2
        var2 = (var8 + 2)
        if (1 if var8 < 1918 else 0):
            continue
        break  # end loop
    var2 = 0
    if (1 if var14 == 2147483647 else 0):
        break
    var6 = ((var20 * 404) + 9568096)
    var3 = i32_load(((var20 * 404) + 9568096) + 68)
    if i32_load(((var20 * 404) + 9568096) + 68):
        if (1 if i32_load(var4 + 16) < var3 else 0):
            break
    var3 = i32_load(var6 + 72)
    if i32_load(var6 + 72):
        if (1 if i32_load(var4 + 20) < var3 else 0):
            break
    var3 = i32_load(var6 + 76)
    if i32_load(var6 + 76):
        if (1 if i32_load(var4 + 24) < var3 else 0):
            break
    var3 = i32_load(var6 + 80)
    if (1 if i32_load(var6 + 80) == 0 else 0):
        break
    if (1 if i32_load(var4 + 28) >= var3 else 0):
        break
    var2 = 0
    break
    var3 = i32_load(var0 + 28)
    i32_store(var4 + 24, var5)
    i32_store(var4 + 20, var1)
    i32_store(var4 + 16, var20)
    var0 = i32_load16_u(var0 + 110)
    i64_store(var4 + 48, 4294967297)
    i64_store(var4 + 40, 4294967297)
    i64_store(var4 + 32, 4294967297)
    i32_store(var4 + 28, var0)
    i32_store(var4 + 56, 0)
    i32_store(var4 + 12, var3)
    var2 = 1
    if i32_load(i32_load(9142424) + 156):
        func29((i32_load(9671128) + (var3 * 132)), 1)
    var0 = (i32_load(9142440) + 2)
    var0 = i32_load((i32_load(9142840) + ((var1 + (((var5 + (i32_load(9142440) + 2)) + 1) * var0)) << 2)) + 4)
    if (1 if i32_load((i32_load(9142840) + ((var1 + (((var5 + (i32_load(9142440) + 2)) + 1) * var0)) << 2)) + 4) < 3 else 0):
        break
    i32_store((i32_load(9671128) + (var0 * 132)) + 96, var12)
    break
    var2 = 1
    break
    var2 = 1
    global global0
    global0 = (var4 - -64)
    return var2


# ==========================================================
# $func143
# ==========================================================
def func143(var0, var1):
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
    var2 = i32_load16_u(var0 + 110)
    var3 = i32_load(9561692)
    if var1:
        var2 = (var3 + (var2 * 286704))
        var1 = i32_load((((var3 + (var2 * 286704)) + (i32_load(38528) << 2)) + 284636))
        if (1 if i32_load((((var3 + (var2 * 286704)) + (i32_load(38528) << 2)) + 284636)) == 0 else 0):
            break
        var3 = i32_load(var1 + 8)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        var4 = i32_load(var1)
        var1 = 0
        while True:  # loop $label1
            var5 = i32_load((var4 + (var1 << 2)))
            if (1 if i32_load((var4 + (var1 << 2))) == 0 else 0):
                var1 = (var1 + 1)
                if (1 if var3 != (var1 + 1) else 0):
                    continue
                break
            break  # end loop
        var1 = i32_load(9671128)
        i32_store8(var0 + 129, 10)
        return 1
        var1 = i32_load(((var2 + (i32_load(((i32_load(var2 + 283960) << 2) + 9687176)) << 2)) + 284636))
        if (1 if i32_load(((var2 + (i32_load(((i32_load(var2 + 283960) << 2) + 9687176)) << 2)) + 284636)) == 0 else 0):
            break
        var2 = i32_load(var1 + 8)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        var3 = i32_load(var1)
        var1 = 0
        while True:  # loop $label4
            var4 = i32_load((var3 + (var1 << 2)))
            if i32_load((var3 + (var1 << 2))):
                break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var2 else 0):
                continue
            break  # end loop
        return 0
        var1 = i32_load(9671128)
        i32_store8(var0 + 129, 10)
        return 1
    var7 = i32_load(38500)
    var4 = ((i32_load(38500) * 404) + 9568096)
    var1 = (var3 + (var2 * 286704))
    if (1 if i32_load(((i32_load(38500) * 404) + 9568096) + 68) > i32_load((var3 + (var2 * 286704)) + 283848) else 0):
        break
    if (1 if i32_load(var4 + 72) > i32_load((var1 + 283852)) else 0):
        break
    var4 = ((var7 * 404) + 9568096)
    var2 = (var3 + (var2 * 286704))
    if (1 if i32_load(((var7 * 404) + 9568096) + 76) > i32_load(((var3 + (var2 * 286704)) + 283856)) else 0):
        break
    if (1 if i32_load(var4 + 80) > i32_load((var2 + 283860)) else 0):
        break
    var16 = i32_load(var1 + 283876)
    var17 = i32_load(var1 + 283872)
    i32_store8(var0 + 129, 3)
    var6 = i32_load(9142440)
    var8 = (i32_load(9142440) + 2)
    var9 = ((var7 * 404) + 9568096)
    var18 = i32_load(9671128)
    var11 = i32_load(9142840)
    var1 = 0
    while True:  # loop $label12
        var12 = var1
        var1 = (var1 << 2)
        var3 = (i32_load((((var1 << 2) | 4) + 8611904)) + var16)
        if (1 if var6 <= (i32_load((((var1 << 2) | 4) + 8611904)) + var16) else 0):
            break
        var4 = (i32_load((var1 + 8611904)) + var17)
        if (1 if var6 <= (i32_load((var1 + 8611904)) + var17) else 0):
            break
        if (1 if (var3 | var4) < 0 else 0):
            break
        var10 = i32_load(var9 + 216)
        if (1 if i32_load(var9 + 216) <= 0 else 0):
            break
        var13 = (i32_load(var9 + 220) + var3)
        if (1 if (i32_load(var9 + 220) + var3) <= var3 else 0):
            break
        var19 = (var4 + var10)
        var14 = i32_load(var9 + 372)
        var2 = var4
        while True:  # loop $label11
            var5 = (var2 + 1)
            var15 = (var2 - var4)
            var1 = var3
            if (1 if var2 < var6 else 0):
                while True:  # loop $label8
                    if (1 if i32_load8_u((var14 + (((var1 - var3) * var10) + var15))) == 0 else 0):
                        var1 = (var1 + 1)
                        break
                    if (1 if var1 >= var6 else 0):
                        break
                    if (1 if (var1 | var2) < 0 else 0):
                        break
                    var1 = (var1 + 1)
                    if i32_load((var11 + ((((var1 + 1) * var8) + var5) << 2))):
                        break
                    if (1 if i32_load(((i32_load8_u((var18 + (i32_load((var11 + ((((var1 + var8) * var8) + var5) << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 1 else 0):
                        break
                    if (1 if var1 != var13 else 0):
                        continue
                    break
                    break  # end loop
                raise RuntimeError('unreachable')
            while True:  # loop $label10
                if i32_load8_u((var14 + (((var1 - var3) * var10) + var15))):
                    break
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var13 else 0):
                    continue
                break  # end loop
            var2 = var5
            if (1 if var5 < var19 else 0):
                continue
            break  # end loop
        func261(var7, var4, var3, var0)
        return 1
        var1 = (var12 + 2)
        if (1 if var12 < 3358 else 0):
            continue
        break  # end loop
    return 0

