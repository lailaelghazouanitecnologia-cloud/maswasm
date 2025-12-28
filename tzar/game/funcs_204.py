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
# $ld
# Export: ld
# ==========================================================
def ld(var0):
    """Export: ld"""
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
    var13 = i32_load(9142440)
    var3 = (var0 + 2)
    var12 = ((var0 + 2) * var3)
    var6 = func26((-1 if (1 if (var12 * 3) > 1073741823 else 0) else (((var0 + 2) * var3) * 12)))
    if var3:
        var10 = (var3 & -2)
        var15 = (var0 & 1)
        var5 = (var0 + 1)
        var16 = (var13 + 2)
        var7 = ((var13 + 2) << 1)
        var17 = (var3 << 1)
        var9 = ((var3 << 1) * var3)
        var8 = i32_load(9142840)
        var4 = (1 if var0 == -1 else 0)
        while True:  # loop $label6
            if (1 if var1 == 0 else 0):
                var2 = 0
                var14 = 0
                if (1 if var4 == 0 else 0):
                    while True:  # loop $label0
                        i32_store((var6 + ((var2 * var3) << 2)), -1)
                        i32_store((var6 + (((var2 + var3) * var3) << 2)), -1)
                        i32_store((var6 + (((var2 + var17) * var3) << 2)), -1)
                        var11 = (var2 | 1)
                        i32_store((var6 + (((var2 | 1) * var3) << 2)), -1)
                        i32_store((var6 + (((var3 + var11) * var3) << 2)), -1)
                        i32_store((var6 + (((var11 + var17) * var3) << 2)), -1)
                        var2 = (var2 + 2)
                        var14 = (var14 + 2)
                        if (1 if (var14 + 2) != var10 else 0):
                            continue
                        break  # end loop
                if (1 if var15 == 0 else 0):
                    break
                i32_store((var6 + ((var2 * var3) << 2)), -1)
                i32_store((var6 + (((var2 + var3) * var3) << 2)), -1)
                i32_store((var6 + (((var2 + var17) * var3) << 2)), -1)
                break
            i32_store((var6 + (var1 << 2)), -1)
            i32_store((var6 + ((var1 + var12) << 2)), -1)
            i32_store((var6 + ((var1 + var9) << 2)), -1)
            var2 = 1
            if (1 if var3 == 1 else 0):
                break
            while True:  # loop $label5
                if (1 if ((1 if var2 != var5 else 0) & (1 if var1 != var5 else 0)) == 0 else 0):
                    i32_store((var6 + (((var2 * var3) + var1) << 2)), -1)
                    i32_store((var6 + ((((var2 + var3) * var3) + var1) << 2)), -1)
                    break
                if (1 if var2 >= var13 else 0):
                    break
                if (1 if var1 >= var13 else 0):
                    break
                if (1 if (var1 | var2) >= 0 else 0):
                    break
                i32_store((var6 + (((var2 * var3) + var1) << 2)), 0)
                i32_store((var6 + ((((var2 + var3) * var3) + var1) << 2)), 0)
                break
                i32_store((var6 + (((var2 * var3) + var1) << 2)), i32_load((var8 + (((var2 * var16) + var1) << 2))))
                i32_store((var6 + ((((var2 + var3) * var3) + var1) << 2)), i32_load((var8 + ((((var2 + var16) * var16) + var1) << 2))))
                i32_store(0, i32_load((var8 + ((((var2 + var7) * var16) + var1) << 2))))
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != var3 else 0):
                    continue
                break  # end loop
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var3 else 0):
                continue
            break  # end loop
    var12 = (var0 * var0)
    var11 = func26((var0 * var0))
    var4 = (-1 if (var12 & 805306368) else (var12 << 4))
    var15 = func26((-1 if (var12 & 805306368) else (var12 << 4)))
    # Unknown: memory.fill []
    var1 = var13
    if (var13 * var1):
        var2 = i32_load(9147288)
        var8 = 0
        while True:  # loop $label7
            var9 = (var2 + var8)
            var4 = i32_load8_s((var2 + var8))
            if (1 if i32_load8_s((var2 + var8)) < 0 else 0):
                i32_store8(var9, (var4 ^ -1))
                var2 = i32_load(9147288)
                var1 = i32_load(9142440)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) < (var1 * var1) else 0):
                continue
            break  # end loop
    if var0:
        # Unknown: memory.fill []
    if var1:
        var4 = 0
        while True:  # loop $label10
            var9 = (var4 + 1)
            var8 = 0
            while True:  # loop $label9
                if (1 if ((1 if var0 > var4 else 0) & (1 if var0 > var8 else 0)) == 0 else 0):
                    var14 = i32_load(9142840)
                    var8 = (var8 + 1)
                    var2 = (var1 + 2)
                    var7 = i32_load((i32_load(9142840) + ((var9 + ((var8 + 1) * (var1 + 2))) << 2)))
                    if (1 if (i32_load((i32_load(9142840) + ((var9 + ((var8 + 1) * (var1 + 2))) << 2))) - 3) < -4 else 0):
                        var5 = (i32_load(9671128) + (var7 * 132))
                        var10 = func26(4)
                        var1 = (func26(4) + 4)
                        var7 = i32_load(var5)
                        if i32_load(var5):
                            i32_store(var5 + 4, var7)
                        i32_store(var5 + 8, var1)
                        i32_store(var5 + 4, var10)
                        i32_store(var5, var10)
                        # Unknown: memory.fill []
                        var1 = i32_load(9142440)
                        var2 = (i32_load(9142440) + 2)
                        var14 = i32_load(9142840)
                    var7 = i32_load((var14 + ((var9 + ((var2 + var8) * var2)) << 2)))
                    if (1 if (i32_load((var14 + ((var9 + ((var2 + var8) * var2)) << 2))) - 3) <= -5 else 0):
                        var5 = (i32_load(9671128) + (var7 * 132))
                        var10 = func26(4)
                        var1 = (func26(4) + 4)
                        var7 = i32_load(var5)
                        if i32_load(var5):
                            i32_store(var5 + 4, var7)
                        i32_store(var5 + 8, var1)
                        i32_store(var5 + 4, var10)
                        i32_store(var5, var10)
                        # Unknown: memory.fill []
                        var1 = i32_load(9142440)
                        var2 = (i32_load(9142440) + 2)
                        var14 = i32_load(9142840)
                    var7 = i32_load((var14 + ((var9 + ((var8 + (var2 << 1)) * var2)) << 2)))
                    if (1 if (i32_load((var14 + ((var9 + ((var8 + (var2 << 1)) * var2)) << 2))) - 3) > -5 else 0):
                        break
                    var5 = (i32_load(9671128) + (var7 * 132))
                    var10 = func26(4)
                    var1 = (func26(4) + 4)
                    var7 = i32_load(var5)
                    if i32_load(var5):
                        i32_store(var5 + 4, var7)
                    i32_store(var5 + 8, var1)
                    i32_store(var5 + 4, var10)
                    i32_store(var5, var10)
                    # Unknown: memory.fill []
                    var1 = i32_load(9142440)
                    break
                i32_store8((var11 + ((var0 * var8) + var4)), i32_load8_u((i32_load(9147288) + ((var1 * var8) + var4))))
                var8 = (var8 + 1)
                if (1 if var1 > var8 else 0):
                    continue
                break  # end loop
            var4 = var9
            if (1 if var9 < var1 else 0):
                continue
            break  # end loop
    var4 = i32_load(9142840)
    if i32_load(9142840):
        i32_store(9142840, 0)
    var4 = i32_load(9147288)
    if i32_load(9147288):
        i32_store(9147288, 0)
    var4 = i32_load(9142400)
    if i32_load(9142400):
        i32_store(9142400, 0)
    var4 = i32_load(9142432)
    if i32_load(9142432):
        i32_store(9142432, 0)
    var4 = i32_load(9142436)
    if i32_load(9142436):
        i32_store(9142436, 0)
    i32_store(9147288, var11)
    i32_store(9142840, var6)
    i32_store(9142400, var15)
    var1 = (var12 << 1)
    var4 = func26((var12 << 1))
    # Unknown: memory.fill []
    i32_store(9142440, var0)
    i32_store(9142436, var4)
    var1 = (-1 if (1 if var12 > 1073741823 else 0) else (var12 << 2))
    var4 = func26((-1 if (1 if var12 > 1073741823 else 0) else (var12 << 2)))
    # Unknown: memory.fill []
    i32_store(9147372, (var0 + 1))
    i32_store(9147368, var0)
    i32_store(9147364, (var0 - 1))
    i32_store(9147360, -1)
    i32_store(9147356, (var0 ^ -1))
    i32_store(9147352, (0 - var0))
    i32_store(9147348, (1 - var0))
    i32_store(9147344, 1)
    i32_store(9142432, var4)
    if (1 if var0 < var13 else 0):
        var9 = 0
        var11 = i32_load(9681936)
        var2 = i32_load(i32_load(9681936) + 8)
        if i32_load(i32_load(9681936) + 8):
            var4 = i32_load(9684500)
            var10 = i32_load(9684496)
            while True:  # loop $label16
                var15 = (i32_load(var11) + (var9 << 2))
                var7 = i32_load((i32_load(var11) + (var9 << 2)))
                var0 = 0
                var13 = i32_load((var10 - 16))
                if i32_load((var10 - 16)):
                    while True:  # loop $label12
                        var1 = (var10 + (var0 * 60))
                        if (1 if i32_load((var10 + (var0 * 60)) + 52) == var7 else 0):
                            break
                        var0 = (var0 + 1)
                        if (1 if (var0 + 1) != var13 else 0):
                            continue
                        break  # end loop
                var0 = 0
                var1 = var4
                if (1 if i32_load(var4 + 52) == var7 else 0):
                    break
                while True:  # loop $label13
                    var0 = (var0 + 1)
                    var1 = (var4 + ((var0 + 1) * 60))
                    if (1 if i32_load((var4 + ((var0 + 1) * 60)) + 52) != var7 else 0):
                        continue
                    break  # end loop
                var0 = (i32_load(9142440) << 5)
                if (1 if (i32_load(9142440) << 5) >= (i32_load(var1) + (i32_load(var15 + 4) - i32_load(var1 + 8))) else 0):
                    if (1 if (i32_load(var15 + 8) + ((i32_load(var1 + 4) // (i32_load(var1 + 16) * i32_load(var1 + 20))) - i32_load(var1 + 12))) <= var0 else 0):
                        break
                func38(i32_load(var15 + 12))
                var11 = i32_load(9681936)
                var2 = (i32_load(var11 + 8) - 4)
                i32_store(i32_load(9681936) + 8, (i32_load(var11 + 8) - 4))
                var4 = i32_load(9684500)
                var10 = i32_load(9684496)
                if (1 if var2 > var9 else 0):
                    var13 = i32_load(var11)
                    var0 = var9
                    while True:  # loop $label15
                        var1 = (var13 + (var0 << 2))
                        i32_store((var13 + (var0 << 2)), i32_load(var1 + 16))
                        var0 = (var0 + 1)
                        var2 = i32_load(var11 + 8)
                        if (1 if (var0 + 1) < i32_load(var11 + 8) else 0):
                            continue
                        break  # end loop
                var9 = (var9 - 4)
                var9 = (var9 + 4)
                if (1 if (var9 + 4) < var2 else 0):
                    continue
                break  # end loop
    return func115(0, 0, var0, 0, 0)


# ==========================================================
# $func62
# ==========================================================
def func62(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var4 = i32_load16_u(var0 + 114)
    var5 = i32_load16_u(var0 + 112)
    if (1 if i32_load16_u(var0 + 112) != var1 else 0):
        break
    if (1 if var2 > var4 else 0):
        break
    if (1 if var2 < var4 else 0):
        break
    var4 = (1 if var2 != var4 else 0)
    break
    var4 = (1 if (1 if var2 > var4 else 0) else (-1 if (1 if var2 < var4 else 0) else 0))
    var1 = (1 if (1 if var1 > var5 else 0) else (-1 if (1 if var1 < var5 else 0) else 0))
    var2 = 6
    var1 = (((var4 * 3) + var1) + 4)
    if (1 if (((var4 * 3) + var1) + 4) <= 8 else 0):
    else:
    i32_store8(i32_load8_u((var1 + 10184)) + 124, 6)
    var1 = i32_load8_u(var0 + 122)
    var2 = i32_load(((i32_load8_u(var0 + 122) * 72) + 9263856) + 12)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 72) + 9263856) + 12) == 0 else 0):
        if (1 if i32_load(38588) != var1 else 0):
            break
        var2 = i32_load(((var1 * 72) + 9263856) + 8)
        if (1 if i32_load(((var1 * 72) + 9263856) + 8) == 0 else 0):
            break
    if var3:
        break
    var0 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 276)
    func63(func37(var0, var2, 0.0, 0), var0, 10, 0, (i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 276) if var0 else 25))
    return var0
    func29(var0, 1)
    return 0

