"""
Auto-generated from WAT. Contains 6 functions.
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
# $func278
# ==========================================================
def func278(var0, var1):
    if (1 if var0 == 0 else 0):
        return 0
    if var0:
        if (1 if var1 <= 127 else 0):
            break
        if (1 if i32_load(i32_load(global3 + 96)) == 0 else 0):
            if (1 if (var1 & -128) == 57216 else 0):
                break
            break
        if (1 if var1 <= 2047 else 0):
            i32_store8(var0 + 1, ((var1 & 63) | 128))
            i32_store8(var0, (((var1 & 0xFFFFFFFF) >> 6) | 192))
            break
        if (1 if ((1 if (var1 & -8192) != 57344 else 0) & (1 if var1 >= 55296 else 0)) == 0 else 0):
            i32_store8(var0 + 2, ((var1 & 63) | 128))
            i32_store8(var0, (((var1 & 0xFFFFFFFF) >> 12) | 224))
            i32_store8(var0 + 1, ((((var1 & 0xFFFFFFFF) >> 6) & 63) | 128))
            break
        if (1 if (var1 - 65536) <= 1048575 else 0):
            i32_store8(var0 + 3, ((var1 & 63) | 128))
            i32_store8(var0, (((var1 & 0xFFFFFFFF) >> 18) | 240))
            i32_store8(var0 + 2, ((((var1 & 0xFFFFFFFF) >> 6) & 63) | 128))
            i32_store8(var0 + 1, ((((var1 & 0xFFFFFFFF) >> 12) & 63) | 128))
            break
        i32_store(global3 + 28, 25)
    else:
    break
    i32_store8(var0, var1)
    return 1


# ==========================================================
# $func282
# ==========================================================
def func282(var0, var1, var2, var3, var4, var5):
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
    var6 = i32_load(var2 + 220)
    var10 = i32_load(var2 + 216)
    var16 = i32_load(var2 + 372)
    if var5:
        var13 = (var1 + var6)
        var17 = (var0 + var10)
        if (1 if var10 <= 0 else 0):
            break
        if (1 if var6 <= 0 else 0):
            break
        var14 = i32_load(9142440)
        var11 = (i32_load(9142440) + 2)
        var21 = ((i32_load(9142440) + 2) * i32_load(var2 + 208))
        var12 = i32_load(9142840)
        var7 = var0
        while True:  # loop $label6
            var8 = (var7 + 1)
            var15 = (var7 - var0)
            var5 = var1
            if (1 if var7 < var14 else 0):
                while True:  # loop $label3
                    if (1 if i32_load8_u((var16 + (var15 + ((var5 - var1) * var10)))) == 0 else 0):
                        var5 = (var5 + 1)
                        break
                    if (1 if var5 >= var14 else 0):
                        break
                    if (1 if (var5 | var7) < 0 else 0):
                        break
                    var5 = (var5 + 1)
                    var18 = i32_load((var12 + ((((var21 + (var5 + 1)) * var11) + var8) << 2)))
                    if (1 if i32_load((var12 + ((((var21 + (var5 + 1)) * var11) + var8) << 2))) > 2 else 0):
                        break
                    if (1 if i32_load((var12 + (((var5 * var11) + var8) << 2))) > 2 else 0):
                        break
                    if (1 if i32_load((var12 + ((((var5 + var11) * var11) + var8) << 2))) > 2 else 0):
                        break
                    var19 = ((1 if var18 == 0 else 0) | var19)
                    var20 = (var20 + (1 if var18 == 1 else 0))
                    if (1 if var5 < var13 else 0):
                        continue
                    break  # end loop
                break
            while True:  # loop $label5
                if (1 if i32_load8_u((var16 + (var15 + ((var5 - var1) * var10)))) == 0 else 0):
                    var5 = (var5 + 1)
                    if (1 if var13 > (var5 + 1) else 0):
                        continue
                    break
                break  # end loop
            break
            var7 = var8
            if (1 if var8 < var17 else 0):
                continue
            break  # end loop
        var5 = ((var19 ^ 1) | (1 if var20 < (((var6 * var10) // 2) - 1) else 0))
        var9 = (((var19 ^ 1) | (1 if var20 < (((var6 * var10) // 2) - 1) else 0)) ^ 1)
        if (var5 & 1):
            break
        if var3:
            break
        break
    var9 = 1
    if (1 if var3 == 0 else 0):
        break
    var13 = (var1 + var6)
    var17 = (var0 + var10)
    var9 = 1
    if (1 if var10 <= 0 else 0):
        break
    if (1 if var6 <= 0 else 0):
        break
    var7 = var0
    while True:  # loop $label11
        var3 = (var7 + 1)
        var12 = (var7 - var0)
        var14 = i32_load(9140332)
        var15 = i32_load(9147288)
        var6 = i32_load(9142840)
        var5 = var1
        while True:  # loop $label10
            if (1 if i32_load8_u((var16 + (var12 + ((var5 - var1) * var10)))) == 0 else 0):
                var5 = (var5 + 1)
                break
            var11 = i32_load(9142440)
            if (1 if var4 != i32_load(var2 + 212) else 0):
                var8 = (var11 + 2)
                var5 = (var5 + 1)
                i32_store((var6 + (((((var11 + 2) + (var5 + 1)) * var8) + var3) << 2)), var4)
                i32_store((var6 + ((((i32_load(9142440) + 2) * var5) + var3) << 2)), var4)
                break
            var9 = (var11 + 2)
            var8 = (var5 + 1)
            var9 = (var6 + (((((var11 + 2) + (var5 + 1)) * var9) + var3) << 2))
            var5 = i32_load8_s((var15 + ((var5 * var11) + var7)))
            if (1 if i32_load(i32_load((var14 + (((i32_load8_s((var15 + ((var5 * var11) + var7))) ^ ((var5 & 0xFFFFFFFF) >> 7)) & 255) << 2))) + 32) != 23 else 0):
                i32_store(var9, 0)
                i32_store((var6 + ((((i32_load(9142440) + 2) * var8) + var3) << 2)), 0)
                break
            i32_store(var9, 1)
            i32_store((var6 + ((((i32_load(9142440) + 2) * var8) + var3) << 2)), 1)
            var5 = var8
            if (1 if var5 < var13 else 0):
                continue
            break  # end loop
        var7 = var3
        if (1 if var3 < var17 else 0):
            continue
        break  # end loop
    var9 = 1
    return (var9 & 1)


# ==========================================================
# $func287
# ==========================================================
def func287(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var3 = i32_load8_u(var0 + 123)
    if (1 if i32_load8_u(var0 + 123) != 1 else 0):
        var1 = i32_load(9215884)
        var2 = i32_load(var0 + 44)
        var4 = i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4)
        if ((1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) != 1 else 0) & (1 if var3 != 3 else 0)):
            break
        if (1 if var4 == 1 else 0):
            break
        break
    var2 = i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 122)
    var1 = 4
    if (1 if var2 == i32_load(38528) else 0):
        break
    var1 = 0
    if (1 if var2 == i32_load(38504) else 0):
        break
    var1 = 1
    if (1 if var2 == i32_load(38448) else 0):
        break
    var1 = 2
    if (1 if var2 == i32_load(38500) else 0):
        break
    var1 = 3
    if (1 if var2 == i32_load(38508) else 0):
        break
    var1 = 4
    if (1 if i32_load8_u(var0 + 129) == 10 else 0):
        break
    var1 = 5
    if (1 if var3 == 4 else 0):
        break
    var2 = i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4)
    if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 4 else 0):
        break
    var1 = 6
    if (1 if var3 == 6 else 0):
        break
    if (1 if var2 == 6 else 0):
        break
    var1 = 7
    if (1 if var3 == 60 else 0):
        break
    if (1 if var2 == 60 else 0):
        break
    var1 = (8 if (1 if i32_load8_u(var0 + 125) == 8 else 0) else -1)
    return var1


# ==========================================================
# $func292
# ==========================================================
def func292(var0):
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
    var1 = 1
    var4 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var1 = i32_load(9142872)
    if (1 if i32_load(9142872) == 0 else 0):
        break
    if (1 if i32_load8_u((i32_load(9143012) + (i32_load16_u(var0 + 110) + (i32_load(9142892) * var1)))) == 0 else 0):
        break
    var1 = 1
    if (1 if i32_load8_u(var0 + 125) != 3 else 0):
        break
    var2 = i32_load8_u(var0 + 122)
    var5 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var3 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 216)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 216) == 0 else 0):
        return 0
    var1 = 0
    var6 = i32_load(var5 + 220)
    if (1 if i32_load(var5 + 220) == 0 else 0):
        break
    var7 = i32_load(9142440)
    var8 = i32_load(9147376)
    var9 = i32_load16_u(var0 + 114)
    var10 = i32_load16_u(var0 + 112)
    var11 = i32_load(((var2 * 404) + 9568096) + 372)
    var0 = 0
    var2 = 1
    if (1 if var4 == 2 else 0):
        while True:  # loop $label4
            var12 = (var0 + var10)
            while True:  # loop $label3
                if (1 if i32_load8_u((var11 + ((var1 * var3) + var0))) == 0 else 0):
                    break
                var4 = i32_load16_u((var8 + (((var7 * (var1 + var9)) + var12) << 1)))
                if i32_load(var5 + 260):
                    if (1 if var4 <= 1 else 0):
                        break
                    return var2
                if (1 if var4 == 0 else 0):
                    break
                return var2
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var6 else 0):
                    continue
                break  # end loop
            var0 = (var0 + 1)
            var2 = (1 if (var0 + 1) < var3 else 0)
            var1 = 0
            if (1 if var0 != var3 else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    while True:  # loop $label7
        var5 = (var0 + var10)
        while True:  # loop $label6
            if (1 if i32_load8_u((var11 + ((var1 * var3) + var0))) == 0 else 0):
                break
            if (1 if i32_load16_u((var8 + (((var7 * (var1 + var9)) + var5) << 1))) == 0 else 0):
                break
            return var2
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var6 else 0):
                continue
            break  # end loop
        var0 = (var0 + 1)
        var2 = (1 if (var0 + 1) < var3 else 0)
        var1 = 0
        if (1 if var0 != var3 else 0):
            continue
        break  # end loop
    return (var1 & 1)


# ==========================================================
# $func293
# ==========================================================
def func293(var0):
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
    var1 = 1
    var4 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var1 = i32_load(9142872)
    if (1 if i32_load(9142872) == 0 else 0):
        break
    if (1 if i32_load8_u((i32_load(9143012) + (i32_load16_u(var0 + 110) + (i32_load(9142892) * var1)))) == 0 else 0):
        break
    var1 = 1
    if (1 if i32_load8_u(var0 + 125) != 3 else 0):
        break
    var2 = i32_load8_u(var0 + 122)
    var5 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var3 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 216)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 216) == 0 else 0):
        return 0
    var1 = 0
    var5 = i32_load(var5 + 220)
    if (1 if i32_load(var5 + 220) == 0 else 0):
        break
    var6 = i32_load(9142440)
    var7 = i32_load(9147376)
    var8 = i32_load16_u(var0 + 114)
    var9 = i32_load16_u(var0 + 112)
    var10 = i32_load(((var2 * 404) + 9568096) + 372)
    var0 = 0
    var2 = 1
    if (1 if var4 == 2 else 0):
        while True:  # loop $label4
            var4 = (var0 + var9)
            while True:  # loop $label3
                if (1 if i32_load8_u((var10 + ((var1 * var3) + var0))) == 0 else 0):
                    break
                if (1 if i32_load16_u((var7 + (((var6 * (var1 + var8)) + var4) << 1))) <= 1 else 0):
                    break
                return var2
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var5 else 0):
                    continue
                break  # end loop
            var0 = (var0 + 1)
            var2 = (1 if (var0 + 1) < var3 else 0)
            var1 = 0
            if (1 if var0 != var3 else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    while True:  # loop $label7
        var4 = (var0 + var9)
        while True:  # loop $label6
            if (1 if i32_load8_u((var10 + ((var1 * var3) + var0))) == 0 else 0):
                break
            if (1 if i32_load16_u((var7 + (((var6 * (var1 + var8)) + var4) << 1))) == 0 else 0):
                break
            return var2
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var5 else 0):
                continue
            break  # end loop
        var0 = (var0 + 1)
        var2 = (1 if (var0 + 1) < var3 else 0)
        var1 = 0
        if (1 if var0 != var3 else 0):
            continue
        break  # end loop
    return (var1 & 1)


# ==========================================================
# $func295
# ==========================================================
def func295(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var3 = i32_load8_u(var0 + 122)
    if (1 if i32_load8_u(var0 + 122) == i32_load(38500) else 0):
        break
    var2 = i32_load16_u(var0 + 110)
    var1 = (i32_load(9142892) * var1)
    var4 = i32_load(9143004)
    var5 = i32_load16_u(var0 + 120)
    if i32_load16_u(var0 + 120):
    else:
    if (1 if i32_load8_u(((var5 if i32_load8_u((var4 + (var1 + var2))) else var2) + (var2 + var1))) == 0 else 0):
        var2 = 0
        if (1 if i32_load8_u(var0 + 127) != 6 else 0):
            break
        if (1 if i32_load8_u(var0 + 128) == 0 else 0):
            break
        break
    var2 = 0
    if i32_load8_u(var0 + 128):
        break
    if (1 if i32_load8_u(var0 + 125) == 10 else 0):
        break
    if (1 if i32_load8_u(var0 + 126) == 2 else 0):
        break
    if (1 if i32_load(var0 + 64) == -1 else 0):
        break
    var0 = ((var3 * 404) + 9568096)
    if (1 if i32_load(((var3 * 404) + 9568096) + 264) == 2 else 0):
        break
    if (1 if i32_load(var0 + 188) != 55 else 0):
        break
    if (1 if i32_load(38560) == var3 else 0):
        break
    if (1 if i32_load(38620) == var3 else 0):
        break
    var2 = (1 if i32_load(38564) != var3 else 0)
    return var2

