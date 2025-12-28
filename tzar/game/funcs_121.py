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
# $func216
# ==========================================================
def func216(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var5 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) != i32_load(var0 + 4) else 0):
        var6 = i32_load(var0)
        break
    var6 = (i32_load(var0 + 12) + var5)
    i32_store(var0 + 4, (i32_load(var0 + 12) + var5))
    var7 = i32_load(var0)
    var6 = func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2)))
    if var5:
        # Unknown: memory.copy []
    if var7:
        var5 = i32_load(var0 + 8)
    i32_store(var0, var6)
    i32_store(var0 + 8, (var5 + 1))
    i32_store((var6 + (var5 << 2)), var1)
    var5 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) != i32_load(var0 + 4) else 0):
        var1 = var6
        break
    var1 = (i32_load(var0 + 12) + var5)
    i32_store(var0 + 4, (i32_load(var0 + 12) + var5))
    var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var5:
        # Unknown: memory.copy []
    i32_store(var0, var1)
    var5 = i32_load(var0 + 8)
    i32_store(var0 + 8, (var5 + 1))
    i32_store((var1 + (var5 << 2)), var2)
    var5 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) != i32_load(var0 + 4) else 0):
        var6 = var1
        break
    var2 = (i32_load(var0 + 12) + var5)
    i32_store(var0 + 4, (i32_load(var0 + 12) + var5))
    var6 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var5:
        # Unknown: memory.copy []
    i32_store(var0, var6)
    var5 = i32_load(var0 + 8)
    i32_store(var0 + 8, (var5 + 1))
    i32_store((var6 + (var5 << 2)), var3)
    var5 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) != i32_load(var0 + 4) else 0):
        var1 = var6
        break
    var1 = (i32_load(var0 + 12) + var5)
    i32_store(var0 + 4, (i32_load(var0 + 12) + var5))
    var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var5:
        # Unknown: memory.copy []
    i32_store(var0, var1)
    var5 = i32_load(var0 + 8)
    i32_store(var0 + 8, (var5 + 1))
    i32_store((var1 + (var5 << 2)), var4)


# ==========================================================
# $func219
# ==========================================================
def func219():
    var0 = 0
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
    var5 = i32_load(9142432)
    if (1 if i32_load(9142432) == 0 else 0):
        break
    var3 = i32_load(9215876)
    if i32_load(9215876):
        var0 = i32_load(9215880)
        break
    var3 = func26(16)
    i32_store(func26(16) + 4, 1024)
    i32_store(var3, func26(4096))
    i64_store(var3 + 8, 4398046511104)
    i32_store(9215876, var3)
    var0 = func26(16)
    i32_store(func26(16) + 4, 256)
    i32_store(var0, func26(1024))
    i64_store(var0 + 8, 4398046511104)
    i32_store(9215880, var0)
    var7 = 1
    i32_store(var0 + 8, 1)
    i32_store(var3 + 8, 0)
    var4 = i32_load(9142440)
    if (1 if i32_load(9142440) <= 0 else 0):
        var0 = var4
        break
    var0 = var4
    while True:  # loop $label12
        var3 = 0
        while True:  # loop $label11
            var1 = ((var0 * var3) + var8)
            if (1 if i32_load((var5 + (((var0 * var3) + var8) << 2))) == 0 else 0):
                var5 = 0
                var0 = i32_load8_s((i32_load(9147288) + var1))
                if (1 if i32_load8_s((i32_load(9147288) + var1)) >= 0 else 0):
                    var5 = (1 if i32_load(i32_load((i32_load(9140332) + ((var0 & 255) << 2))) + 32) == 23 else 0)
                var2 = i32_load(9215880)
                var0 = i32_load(i32_load(9215880) + 8)
                if (1 if i32_load(i32_load(9215880) + 8) != i32_load(var2 + 4) else 0):
                    var1 = i32_load(var2)
                    break
                var1 = (i32_load(var2 + 12) + var0)
                i32_store(var2 + 4, (i32_load(var2 + 12) + var0))
                var6 = i32_load(var2)
                var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                if var0:
                    # Unknown: memory.copy []
                if var6:
                    var0 = i32_load(var2 + 8)
                i32_store(var2, var1)
                i32_store(var2 + 8, (var0 + 1))
                i32_store((var1 + (var0 << 2)), var5)
                var11 = 0
                var16 = i32_load(9142440)
                var0 = ((i32_load(9142440) * var3) + var8)
                i32_store(59200, ((i32_load(9142440) * var3) + var8))
                i32_store((i32_load(9142432) + (var0 << 2)), var7)
                var9 = 1
                while True:  # loop $label10
                    var0 = i32_load((((var11 & 2097151) << 2) + 59200))
                    var0 = i32_load(9142440)
                    var17 = ((var0 & 0xFFFFFFFF) // i32_load(9142440))
                    var18 = (i32_load((((var11 & 2097151) << 2) + 59200)) - (((var0 & 0xFFFFFFFF) // i32_load(9142440)) * var0))
                    var12 = 0
                    while True:  # loop $label9
                        var2 = i32_load(9142440)
                        var1 = (var12 << 3)
                        var0 = (i32_load(((var12 << 3) + 8932)) + var17)
                        if (1 if i32_load(9142440) <= (i32_load(((var12 << 3) + 8932)) + var17) else 0):
                            break
                        var1 = (i32_load((var1 + 8928)) + var18)
                        if (1 if var2 <= (i32_load((var1 + 8928)) + var18) else 0):
                            break
                        if (1 if (var0 | var1) < 0 else 0):
                            break
                        var10 = i32_load(9142432)
                        var0 = ((var0 * var16) + var1)
                        var19 = (((var0 * var16) + var1) << 2)
                        var6 = (i32_load(9142432) + (((var0 * var16) + var1) << 2))
                        var2 = i32_load((i32_load(9142432) + (((var0 * var16) + var1) << 2)))
                        if i32_load((i32_load(9142432) + (((var0 * var16) + var1) << 2))):
                            if (1 if var2 == var7 else 0):
                                break
                            var1 = i32_load(9215876)
                            var6 = i32_load(i32_load(9215876) + 8)
                            if i32_load(i32_load(9215876) + 8):
                                var14 = i32_load(var1)
                                var0 = 0
                                while True:  # loop $label5
                                    var13 = (var0 << 2)
                                    var15 = i32_load((var14 + ((var0 << 2) | 4)))
                                    var13 = i32_load((var13 + var14))
                                    if ((1 if var7 == i32_load((var13 + var14)) else 0) & (1 if var2 == var15 else 0)):
                                        break
                                    if ((1 if var2 == var13 else 0) & (1 if var7 == var15 else 0)):
                                        break
                                    var0 = (var0 + 2)
                                    if (1 if (var0 + 2) < var6 else 0):
                                        continue
                                    break  # end loop
                            if (1 if i32_load(var1 + 4) != var6 else 0):
                                var0 = i32_load(var1)
                                break
                            var0 = (i32_load(var1 + 12) + var6)
                            i32_store(var1 + 4, (i32_load(var1 + 12) + var6))
                            var2 = i32_load(var1)
                            var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
                            if var6:
                                # Unknown: memory.copy []
                            if var2:
                                var6 = i32_load(var1 + 8)
                            i32_store(var1, var0)
                            var10 = i32_load(9142432)
                            var2 = i32_load(9215876)
                            i32_store(var1 + 8, (var6 + 1))
                            i32_store((var0 + (var6 << 2)), var7)
                            var10 = i32_load((var10 + var19))
                            var0 = i32_load(var2 + 8)
                            if (1 if i32_load(var2 + 8) != i32_load(var2 + 4) else 0):
                                var1 = i32_load(var2)
                                break
                            var1 = (i32_load(var2 + 12) + var0)
                            i32_store(var2 + 4, (i32_load(var2 + 12) + var0))
                            var6 = i32_load(var2)
                            var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                            if var0:
                                # Unknown: memory.copy []
                            if var6:
                                var0 = i32_load(var2 + 8)
                            i32_store(var2, var1)
                            i32_store(var2 + 8, (var0 + 1))
                            i32_store((var1 + (var0 << 2)), var10)
                            break
                        var1 = i32_load8_u((i32_load(9147288) + var0))
                        # Unknown: i32.extend8_s []
                        var2 = i32_load8_u((i32_load(9147288) + var0))
                        if var5:
                            if (1 if var2 < 0 else 0):
                                break
                            if (1 if i32_load(i32_load((i32_load(9140332) + (var1 << 2))) + 32) == 23 else 0):
                                break
                            break
                        if (1 if var2 < 0 else 0):
                            break
                        if (1 if i32_load(i32_load((i32_load(9140332) + (var1 << 2))) + 32) == 23 else 0):
                            break
                        i32_store((((var9 & 2097151) << 2) + 59200), var0)
                        i32_store(var6, var7)
                        var9 = (var9 + 1)
                        var12 = (var12 + 1)
                        if (1 if (var12 + 1) != 8 else 0):
                            continue
                        break  # end loop
                    var11 = (var11 + 1)
                    if (1 if (var11 + 1) < var9 else 0):
                        continue
                    break  # end loop
                var7 = (var7 + 1)
                var0 = i32_load(9142440)
                var5 = i32_load(9142432)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var4 else 0):
                continue
            break  # end loop
        var8 = (var8 + 1)
        if (1 if (var8 + 1) != var4 else 0):
            continue
        break  # end loop
    if var7:
        break
    var7 = 0
    break
    i32_store(((var7 << 2) + 59200), 0)
    var2 = 0
    var0 = (var0 * var0)
    if (1 if (var0 * var0) == 0 else 0):
        break
    var8 = 0
    var3 = 0
    if (1 if var0 >= 4 else 0):
        var6 = (var0 & -4)
        var1 = 0
        while True:  # loop $label15
            var4 = (var3 << 2)
            var9 = ((i32_load((var5 + (var3 << 2))) << 2) + 59200)
            i32_store(((i32_load((var5 + (var3 << 2))) << 2) + 59200), (i32_load(var9) + 1))
            var9 = ((i32_load((var5 + (var4 | 4))) << 2) + 59200)
            i32_store(((i32_load((var5 + (var4 | 4))) << 2) + 59200), (i32_load(var9) + 1))
            var9 = ((i32_load((var5 + (var4 | 8))) << 2) + 59200)
            i32_store(((i32_load((var5 + (var4 | 8))) << 2) + 59200), (i32_load(var9) + 1))
            var4 = ((i32_load((var5 + (var4 | 12))) << 2) + 59200)
            i32_store(((i32_load((var5 + (var4 | 12))) << 2) + 59200), (i32_load(var4) + 1))
            var3 = (var3 + 4)
            var1 = (var1 + 4)
            if (1 if (var1 + 4) != var6 else 0):
                continue
            break  # end loop
    var0 = (var0 & 3)
    if (1 if (var0 & 3) == 0 else 0):
        break
    while True:  # loop $label16
        var4 = ((i32_load((var5 + (var3 << 2))) << 2) + 59200)
        i32_store(((i32_load((var5 + (var3 << 2))) << 2) + 59200), (i32_load(var4) + 1))
        var3 = (var3 + 1)
        var8 = (var8 + 1)
        if (1 if (var8 + 1) != var0 else 0):
            continue
        break  # end loop
    if var2:
        break
    var3 = 0
    var5 = i32_load(9684492)
    var8 = i32_load(i32_load(9215880))
    if (1 if var7 != 1 else 0):
        var1 = (var7 & -2)
        var0 = 0
        while True:  # loop $label20
            var4 = (var3 << 2)
            if i32_load((var8 + (var3 << 2))):
                break
            if (1 if i32_load((var4 + 59200)) <= i32_load(((var5 << 2) + 59200)) else 0):
                break
            i32_store(9684492, var3)
            var5 = var3
            var4 = (var3 | 1)
            var2 = ((var3 | 1) << 2)
            if i32_load((var8 + ((var3 | 1) << 2))):
                break
            if (1 if i32_load((var2 + 59200)) <= i32_load(((var5 << 2) + 59200)) else 0):
                break
            i32_store(9684492, var4)
            var5 = var4
            var3 = (var3 + 2)
            var0 = (var0 + 2)
            if (1 if (var0 + 2) != var1 else 0):
                continue
            break  # end loop
    if (1 if (var7 & 1) == 0 else 0):
        break
    var0 = (var3 << 2)
    if i32_load((var8 + (var3 << 2))):
        break
    if (1 if i32_load((var0 + 59200)) <= i32_load(((var5 << 2) + 59200)) else 0):
        break
    i32_store(9684492, var3)
    var8 = 0
    var0 = (var7 * var7)
    var5 = func26((var7 * var7))
    # Unknown: memory.fill []
    i32_store(9684440, var7)
    i32_store(9684436, var5)
    var0 = i32_load(9215876)
    var4 = i32_load(i32_load(9215876) + 8)
    if (1 if i32_load(i32_load(9215876) + 8) == 0 else 0):
        break
    var3 = ((((var4 - 1) & 0xFFFFFFFF) >> 1) + 1)
    var2 = (((((var4 - 1) & 0xFFFFFFFF) >> 1) + 1) & 1)
    var0 = i32_load(var0)
    if (1 if var4 >= 3 else 0):
        var3 = (var3 & -2)
        var1 = 0
        while True:  # loop $label21
            var4 = (var8 << 2)
            var6 = i32_load((var0 + ((var8 << 2) | 4)))
            var9 = i32_load((var0 + var4))
            i32_store8((var5 + ((i32_load((var0 + ((var8 << 2) | 4))) * var7) + i32_load((var0 + var4)))), 1)
            i32_store8((var5 + (var6 + (var7 * var9))), 1)
            var6 = i32_load((var0 + (var4 | 8)))
            var4 = i32_load((var0 + (var4 | 12)))
            i32_store8((var5 + (i32_load((var0 + (var4 | 8))) + (i32_load((var0 + (var4 | 12))) * var7))), 1)
            i32_store8((var5 + (var4 + (var6 * var7))), 1)
            var8 = (var8 + 4)
            var1 = (var1 + 2)
            if (1 if (var1 + 2) != var3 else 0):
                continue
            break  # end loop
    if (1 if var2 == 0 else 0):
        break
    var4 = (var8 << 2)
    var3 = i32_load((var0 + ((var8 << 2) | 4)))
    var0 = i32_load((var0 + var4))
    i32_store8((var5 + ((i32_load((var0 + ((var8 << 2) | 4))) * var7) + i32_load((var0 + var4)))), 1)
    i32_store8((var5 + (var3 + (var0 * var7))), 1)
    return var0

