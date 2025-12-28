"""
Auto-generated from WAT. Contains 4 functions.
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
# $func319
# ==========================================================
def func319():
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var4 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    func402(i32_load(9142440))
    var1 = i32_load(9142440)
    if i32_load(9142440):
        var5 = i32_load(9147288)
        while True:  # loop $label2
            var3 = (var0 + 1)
            var2 = 0
            var6 = i32_load(9142840)
            var7 = i32_load(9140332)
            while True:  # loop $label1
                var8 = i32_load8_s((var5 + ((var1 * var2) + var0)))
                if (1 if i32_load8_s((var5 + ((var1 * var2) + var0))) < 0 else 0):
                    break
                if (1 if i32_load(i32_load((var7 + ((var8 & 255) << 2))) + 32) != 23 else 0):
                    break
                var8 = (var2 + 1)
                i32_store((var6 + ((((var2 + 1) * (var1 + 2)) + var3) << 2)), 1)
                var1 = (i32_load(9142440) + 2)
                i32_store((var6 + (((((i32_load(9142440) + 2) + var8) * var1) + var3) << 2)), 1)
                var1 = i32_load(9142440)
                var2 = (var2 + 1)
                if (1 if (var2 + 1) < var1 else 0):
                    continue
                break  # end loop
            var0 = var3
            if (1 if var3 < var1 else 0):
                continue
            break  # end loop
    var1 = 3
    if (1 if i32_load(9671136) > 3 else 0):
        var6 = 0
        while True:  # loop $label9
            var0 = (i32_load(9671128) + (var1 * 132))
            var3 = i32_load((i32_load(9671128) + (var1 * 132)) + 28)
            if (1 if i32_load((i32_load(9671128) + (var1 * 132)) + 28) == 0 else 0):
                break
            var2 = i32_load16_u(var0 + 110)
            if (1 if i32_load16_u(var0 + 110) >= i32_load(9142892) else 0):
                break
            var5 = i32_load8_u(var0 + 122)
            var7 = (1 if i32_load8_u(var0 + 122) != i32_load(38448) else 0)
            if (1 if (1 if i32_load8_u(var0 + 122) != i32_load(38448) else 0) == 0 else 0):
                i32_store(var0 + 48, i32_load(((var5 * 72) + 9263856)))
            var2 = (i32_load(9561692) + (var2 * 286704))
            if (1 if i32_load8_u(9216060) == 0 else 0):
                if (1 if i32_load(var0 + 64) == 0 else 0):
                    break
            if (1 if i32_load8_u(var0 + 125) != 3 else 0):
                break
            i32_store8(var0 + 125, 3)
            if (1 if var7 == 0 else 0):
                var3 = i32_load(var0 + 28)
            i32_store(var0 + 92, 0)
            func388(var2, var3)
            break
            if func292(var0):
                i32_store(var0 + 92, 0)
            var3 = ((var5 * 404) + 9568096)
            i32_store(var0 + 92, 0)
            if i32_load(var0 + 36):
                func138(var0)
                break
            var5 = i32_load8_u(var0 + 125)
            if (1 if i32_load(9684508) > 551 else 0):
                break
            if (1 if i32_load(var0 + 84) < 12 else 0):
                break
            if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264):
                break
            i32_store(var2 + 283936, (i32_load(var2 + 283936) + 1))
            if (1 if i32_load(var0 + 32) != -1 else 0):
                break
            if i32_load8_u(9147152):
                break
            i32_store(var0 + 32, 0)
            var6 = (var6 + 25)
            func240(var0, (((var6 + 25) % 1000) + 25), 0)
            break
            if (1 if i32_load(var3 + 264) == 4 else 0):
                i32_store8(9671157, 1)
            if (1 if i32_load(var3 + 208) == 2 else 0):
                i32_store8(9671158, 1)
            func144(var2, i32_load(var0 + 28), 0)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < i32_load(9671136) else 0):
                continue
            break  # end loop
    if i32_load8_u(9561801):
        i32_store(var4 + 16, i32_load(9142840))
        var0 = (i32_load(9142440) + 2)
        i32_store(var4 + 20, (((i32_load(9142440) + 2) * var0) * 3))
    if i32_load(9147132):
        break
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var3 = i32_load(9671136)
    if (1 if i32_load(9671136) < 4 else 0):
        break
    var0 = i32_load(9671128)
    var1 = 3
    while True:  # loop $label12
        var2 = (var0 + (var1 * 132))
        if (1 if i32_load8_u((var0 + (var1 * 132)) + 125) == 3 else 0):
            break
        if (1 if i32_load(var2 + 28) == 0 else 0):
            break
        if i32_load(var2 + 36):
            break
        var3 = i32_load(9671136)
        var0 = i32_load(9671128)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < var3 else 0):
            continue
        break  # end loop
    if (1 if i32_load8_u(9147152) == 0 else 0):
        break
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    i32_store(var4, 0)
    i32_store(var4 + 4, i32_load(9142440))
    a_b()
    global global0
    global0 = (var4 + 32)


# ==========================================================
# $func337
# ==========================================================
def func337(var0, var1, var2, var3, var4, var5):
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
    var17 = i32_load16_u(var2 + 114)
    var15 = (i32_load16_u(var2 + 114) - 1)
    var18 = i32_load16_u(var2 + 112)
    var16 = (i32_load16_u(var2 + 112) - 1)
    var19 = i32_load8_u(var2 + 122)
    var7 = ((i32_load8_u(var2 + 122) * 404) + 9568096)
    var14 = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 60)
    if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 60):
        var8 = i32_load(var7 + 56)
        var10 = i32_load(9142440)
        var6 = 2147483647
        var7 = 0
        while True:  # loop $label0
            var9 = (var7 << 2)
            var11 = (i32_load((var8 + ((var7 << 2) | 4))) + var15)
            var13 = ((i32_load((var8 + ((var7 << 2) | 4))) + var15) - var5)
            var9 = (i32_load((var8 + var9)) + var16)
            var13 = ((i32_load((var8 + var9)) + var16) - var4)
            var13 = ((((i32_load((var8 + ((var7 << 2) | 4))) + var15) - var5) * var13) + (((i32_load((var8 + var9)) + var16) - var4) * var13))
            if (1 if var6 > ((((i32_load((var8 + ((var7 << 2) | 4))) + var15) - var5) * var13) + (((i32_load((var8 + var9)) + var16) - var4) * var13)) else 0):
                var11 = (((1 if var9 < var10 else 0) & (1 if (var9 | var11) >= 0 else 0)) & (1 if var10 > var11 else 0))
                var6 = (var13 if (((1 if var9 < var10 else 0) & (1 if (var9 | var11) >= 0 else 0)) & (1 if var10 > var11 else 0)) else var6)
                var12 = (((var7 & 0xFFFFFFFF) >> 1) if var11 else var12)
            var7 = (var7 + 2)
            if (1 if (var7 + 2) < var14 else 0):
                continue
            break  # end loop
    var4 = i32_load16_u(40596)
    var5 = (i32_load16_u(40596) + 2)
    i32_store16(40596, (i32_load16_u(40596) + 2))
    if (1 if (var5 & 65535) < 65534 else 0):
        break
    i32_store16(40596, 1)
    var5 = i32_load(9142440)
    var5 = (i32_load(9142440) * var5)
    if (1 if (i32_load(9142440) * var5) == 0 else 0):
        break
    # Unknown: memory.fill []
    if var14:
        var10 = ((var14 & 0xFFFFFFFF) >> 1)
        var11 = ((var19 * 404) + 9568152)
        var7 = 0
        while True:  # loop $label6
            if (1 if var7 == 0 else 0):
                break
            if (var7 & 2):
                break
            var5 = (i32_load(var11) + (((((((var7 & 0xFFFFFFFF) >> 2) + var12) % var10) + var10) % var10) << 3))
            var8 = i32_load((i32_load(var11) + (((((((var7 & 0xFFFFFFFF) >> 2) + var12) % var10) + var10) % var10) << 3)))
            var9 = i32_load(var5 + 4)
            var5 = i32_load(9142440)
            var6 = (i32_load(9142440) + 2)
            var6 = i32_load((i32_load(9142840) + (((i32_load((i32_load(var11) + (((((((var7 & 0xFFFFFFFF) >> 2) + var12) % var10) + var10) % var10) << 3))) + var18) + (((i32_load(var5 + 4) + var17) + ((i32_load(9142440) + 2) * i32_load(var3 + 208))) * var6)) << 2)))
            if (1 if i32_load((i32_load(9142840) + (((i32_load((i32_load(var11) + (((((((var7 & 0xFFFFFFFF) >> 2) + var12) % var10) + var10) % var10) << 3))) + var18) + (((i32_load(var5 + 4) + var17) + ((i32_load(9142440) + 2) * i32_load(var3 + 208))) * var6)) << 2))) <= 2 else 0):
                if (1 if i32_load(var3 + 212) != var6 else 0):
                    break
            if (1 if var6 >= 3 else 0):
                if func205((i32_load(9671128) + (var6 * 132)), i32_load16_u(var2 + 110)):
                    break
                var5 = i32_load(9142440)
            var6 = (var9 + var15)
            var8 = (var8 + var16)
            var9 = (1 if ((var9 + var15) | (var8 + var16)) < 0 else 0)
            if (1 if ((var9 + var15) | (var8 + var16)) < 0 else 0):
                break
            if (1 if var5 <= var8 else 0):
                break
            if (1 if var5 <= var6 else 0):
                break
            if func56(var8, var6, var3, i32_load16_u(var2 + 110), 0, 0, 1, 1, 0):
                break
            var5 = i32_load(9142440)
            if var9:
                break
            if (1 if var5 <= var8 else 0):
                break
            if (1 if var5 <= var6 else 0):
                break
            if (1 if func347(var0, var1, var8, var6, var8, var6, var2, var3, var4) == 0 else 0):
                break
            return 1
            var7 = (var7 + 2)
            if (1 if (var7 + 2) < var14 else 0):
                continue
            break  # end loop
    return 0
    i32_store(var0, var8)
    i32_store(var1, var6)
    return 1


# ==========================================================
# $func338
# ==========================================================
def func338(var0, var1, var2, var3):
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
    var8 = i32_load8_u(var2 + 122)
    var10 = ((i32_load8_u(var2 + 122) * 404) + 9568096)
    var9 = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 60)
    var11 = i32_load16_u(var2 + 112)
    var12 = i32_load16_u(var2 + 114)
    var6 = i32_load(9147324)
    i32_store(9147324, i32_load(9147320))
    var7 = i32_load(9147316)
    var4 = i32_load(9147312)
    i32_store(9147316, i32_load(9147312))
    i32_store(9147320, var7)
    var6 = (var6 ^ (var6 << 11))
    var6 = ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var6 ^ (var6 << 11)) & 0xFFFFFFFF) >> 8))) ^ var6)
    i32_store(9147312, ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var6 ^ (var6 << 11)) & 0xFFFFFFFF) >> 8))) ^ var6))
    var13 = ((var6 % ((var9 & 0xFFFFFFFF) >> 1)) << 1)
    var14 = (var12 - 1)
    var15 = (var11 - 1)
    if var9:
        var6 = i32_load(9142440)
        var4 = 0
        while True:  # loop $label2
            var5 = (i32_load(var10 + 56) + (((var4 + var13) % var9) << 2))
            var7 = (i32_load((i32_load(var10 + 56) + (((var4 + var13) % var9) << 2)) + 4) + var14)
            if (1 if var6 <= (i32_load((i32_load(var10 + 56) + (((var4 + var13) % var9) << 2)) + 4) + var14) else 0):
                break
            var5 = (i32_load(var5) + var15)
            if (1 if var6 <= (i32_load(var5) + var15) else 0):
                break
            if (1 if (var5 | var7) < 0 else 0):
                break
            if func56(var5, var7, var3, i32_load16_u(var2 + 110), 0, 0, 1, 1, 0):
                break
            var6 = i32_load(9142440)
            var4 = (var4 + 2)
            if (1 if (var4 + 2) < var9 else 0):
                continue
            break  # end loop
    var6 = i32_load16_u(40596)
    var4 = (i32_load16_u(40596) + 2)
    i32_store16(40596, (i32_load16_u(40596) + 2))
    if (1 if (var4 & 65535) < 65534 else 0):
        break
    i32_store16(40596, 1)
    var4 = i32_load(9142440)
    var4 = (i32_load(9142440) * var4)
    if (1 if (i32_load(9142440) * var4) == 0 else 0):
        break
    # Unknown: memory.fill []
    if var9:
        var10 = ((var8 * 404) + 9568152)
        var4 = 0
        while True:  # loop $label5
            var7 = (i32_load(var10) + (((var4 + var13) % var9) << 2))
            var8 = i32_load((i32_load(var10) + (((var4 + var13) % var9) << 2)))
            var16 = i32_load(var7 + 4)
            var7 = i32_load(9142440)
            var5 = (i32_load(9142440) + 2)
            var5 = i32_load((i32_load(9142840) + (((i32_load((i32_load(var10) + (((var4 + var13) % var9) << 2))) + var11) + (((i32_load(var7 + 4) + var12) + ((i32_load(9142440) + 2) * i32_load(var3 + 208))) * var5)) << 2)))
            if (1 if i32_load((i32_load(9142840) + (((i32_load((i32_load(var10) + (((var4 + var13) % var9) << 2))) + var11) + (((i32_load(var7 + 4) + var12) + ((i32_load(9142440) + 2) * i32_load(var3 + 208))) * var5)) << 2))) <= 2 else 0):
                if (1 if i32_load(var3 + 212) != var5 else 0):
                    break
            if (1 if var5 >= 3 else 0):
                if func205((i32_load(9671128) + (var5 * 132)), i32_load16_u(var2 + 110)):
                    break
                var7 = i32_load(9142440)
            var5 = (var14 + var16)
            if (1 if var7 <= (var14 + var16) else 0):
                break
            var8 = (var8 + var15)
            if (1 if (var5 | (var8 + var15)) < 0 else 0):
                break
            if (1 if var7 <= var8 else 0):
                break
            if (1 if func347(var0, var1, var8, var5, var8, var5, var2, var3, var6) == 0 else 0):
                break
            return 1
            var4 = (var4 + 2)
            if (1 if (var4 + 2) < var9 else 0):
                continue
            break  # end loop
    return 0
    i32_store(var0, var5)
    i32_store(var1, var7)
    return 1


# ==========================================================
# $func347
# ==========================================================
def func347(var0, var1, var2, var3, var4, var5, var6, var7, var8):
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    var13 = 0
    var14 = 0
    i32_store(59204, var3)
    i32_store(59200, var2)
    var2 = 0
    var12 = 2
    while True:  # loop $label3
        var3 = var2
        var2 = (var2 + 2)
        var3 = (var3 << 2)
        var13 = i32_load(((var3 << 2) + 59200))
        var14 = i32_load(((var3 | 4) + 59200))
        var3 = 0
        while True:  # loop $label2
            var10 = (var3 << 2)
            var11 = (i32_load(((var3 << 2) + 9072)) + var13)
            var9 = ((i32_load(((var3 << 2) + 9072)) + var13) - var4)
            var10 = (i32_load((var10 + 9104)) + var14)
            var9 = ((i32_load((var10 + 9104)) + var14) - var5)
            if (1 if (((((i32_load(((var3 << 2) + 9072)) + var13) - var4) * var9) + (((i32_load((var10 + 9104)) + var14) - var5) * var9)) - 1) > 1600 else 0):
                break
            var9 = i32_load(9142440)
            if (1 if i32_load(9142440) <= var10 else 0):
                break
            if (1 if (var10 | var11) < 0 else 0):
                break
            if (1 if var9 <= var11 else 0):
                break
            if (1 if i32_load16_u((i32_load(9142436) + (((var9 * var10) + var11) << 1))) == var8 else 0):
                break
            var9 = (var9 + 2)
            var9 = i32_load((i32_load(9142840) + ((var11 + (((var10 + ((var9 + 2) * i32_load(var7 + 208))) + 1) * var9)) << 2)) + 4)
            if (1 if i32_load((i32_load(9142840) + ((var11 + (((var10 + ((var9 + 2) * i32_load(var7 + 208))) + 1) * var9)) << 2)) + 4) <= 2 else 0):
                if (1 if i32_load(var7 + 212) != var9 else 0):
                    break
            if (1 if var9 >= 3 else 0):
                if func205((i32_load(9671128) + (var9 * 132)), i32_load16_u(var6 + 110)):
                    break
            if func56(var11, var10, var7, i32_load16_u(var6 + 110), 0, 0, 1, 1, 0):
                break
            i32_store16((i32_load(9142436) + (((i32_load(9142440) * var10) + var11) << 1)), var8)
            var9 = ((var12 << 2) + 59200)
            i32_store(((var12 << 2) + 59200) + 4, var10)
            i32_store(var9, var11)
            var12 = (var12 + 2)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != 8 else 0):
                continue
            break  # end loop
        if (1 if var2 < var12 else 0):
            continue
        break  # end loop
    return 0
    i32_store(var0, var11)
    i32_store(var1, var10)
    return 1

