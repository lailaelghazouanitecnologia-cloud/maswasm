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
# $func824
# ==========================================================
def func824(var0, var1, param2):
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
    var19 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var5 = i32_load(9671128)
    var6 = (i32_load(9671128) + (var0 * 132))
    var2 = i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122)
    # br_table ['$label0', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label0', '$label2']
    _br_idx = (i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) + -64)
    break  # br_table
    if (1 if var2 != 10 else 0):
        break
    var2 = i32_load(var6 + 20)
    if (1 if i32_load(var6 + 20) == 0 else 0):
        break
    if (1 if i32_load(var2 + 8) < 3 else 0):
        break
    if (1 if (i32_load(i32_load(var2)) - 1) > 1 else 0):
        break
    i32_store(var2 + 8, 0)
    var11 = (var5 + (var1 * 132))
    var14 = i32_load8_u((var5 + (var1 * 132)) + 122)
    if (1 if i32_load8_u(var11 + 125) == 10 else 0):
        var7 = 3
        var8 = 1
        break
    var7 = i32_load(((var14 * 404) + 9568096) + 188)
    if (1 if i32_load(((var14 * 404) + 9568096) + 188) >= 4 else 0):
        func29(var6, 1)
        break
    var8 = (1 if var7 == 3 else 0)
    # br_table ['$label4', '$label5', '$label5', '$label4', '$label5']
    _br_idx = var7
    break  # br_table
    var4 = (var5 + (var0 * 132))
    var9 = i32_load16_u((var5 + (var0 * 132)) + 112)
    var2 = ((i32_load16_u((var5 + (var0 * 132)) + 112) << 5) - i32_load(9142952))
    var3 = i32_load16_u(var4 + 114)
    var2 = ((i32_load16_u(var4 + 114) << 5) - i32_load(9142956))
    if (1 if (((((i32_load16_u((var5 + (var0 * 132)) + 112) << 5) - i32_load(9142952)) * var2) + (((i32_load16_u(var4 + 114) << 5) - i32_load(9142956)) * var2)) - 1) > 9000000 else 0):
        break
    var2 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var4 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var3) + var9) << 1)))
    if (1 if var2 == 2 else 0):
        if (1 if var4 > 1 else 0):
            break
        break
    if (1 if var4 == 0 else 0):
        break
    i32_store(var19 + 40, var3)
    i32_store(var19 + 36, var9)
    i32_store(var19 + 32, i32_load(((((i32_load(9142848) + var9) % 3) << 2) + 57224)))
    a_b()
    if (1 if var7 == 1 else 0):
        var4 = (var5 + (var0 * 132))
        var9 = i32_load16_u((var5 + (var0 * 132)) + 112)
        var2 = ((i32_load16_u((var5 + (var0 * 132)) + 112) << 5) - i32_load(9142952))
        var3 = i32_load16_u(var4 + 114)
        var2 = ((i32_load16_u(var4 + 114) << 5) - i32_load(9142956))
        if (1 if (((((i32_load16_u((var5 + (var0 * 132)) + 112) << 5) - i32_load(9142952)) * var2) + (((i32_load16_u(var4 + 114) << 5) - i32_load(9142956)) * var2)) - 1) > 9000000 else 0):
            break
        var2 = i32_load(i32_load(9142424) + 48)
        if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
            break
        if i32_load8_u(9147152):
            break
        var4 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var3) + var9) << 1)))
        if (1 if var2 == 2 else 0):
            if (1 if var4 > 1 else 0):
                break
            break
        if (1 if var4 == 0 else 0):
            break
        i32_store(var19 + 8, var3)
        i32_store(var19 + 4, var9)
        i32_store(var19, i32_load(((((i32_load(9142848) + var9) % 11) << 2) + 57168)))
        a_b()
        break
    if (1 if var7 != 2 else 0):
        break
    var20 = 1
    if (1 if i32_load(38500) != i32_load8_u(var11 + 122) else 0):
        break
    var4 = (var5 + (var0 * 132))
    var9 = i32_load16_u((var5 + (var0 * 132)) + 112)
    var2 = ((i32_load16_u((var5 + (var0 * 132)) + 112) << 5) - i32_load(9142952))
    var3 = i32_load16_u(var4 + 114)
    var2 = ((i32_load16_u(var4 + 114) << 5) - i32_load(9142956))
    if (1 if (((((i32_load16_u((var5 + (var0 * 132)) + 112) << 5) - i32_load(9142952)) * var2) + (((i32_load16_u(var4 + 114) << 5) - i32_load(9142956)) * var2)) - 1) > 9000000 else 0):
        break
    var2 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var4 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var3) + var9) << 1)))
    if (1 if var2 == 2 else 0):
        if (1 if var4 > 1 else 0):
            break
        break
    if (1 if var4 == 0 else 0):
        break
    i32_store(var19 + 24, var3)
    i32_store(var19 + 20, var9)
    i32_store(var19 + 16, i32_load(((((i32_load(9142848) + var9) % 3) << 2) + 57212)))
    a_b()
    var17 = i32_load(38528)
    var12 = i32_load8_u(var11 + 122)
    var9 = (var5 + (var0 * 132))
    if (1 if i32_load8_u((var5 + (var0 * 132)) + 125) == 1 else 0):
        var8 = (1 if var12 != var17 else 0)
        if (1 if (var20 & (1 if var12 != var17 else 0)) == 0 else 0):
            var4 = ((var14 * 404) + 9568096)
            var3 = i32_load(((var14 * 404) + 9568096) + 220)
            var2 = (var5 + (var1 * 132))
            var18 = i32_load16_u((var5 + (var1 * 132)) + 114)
            var21 = (i32_load(((var14 * 404) + 9568096) + 220) + i32_load16_u((var5 + (var1 * 132)) + 114))
            var4 = i32_load(var4 + 216)
            var17 = i32_load16_u(var2 + 112)
            var14 = (i32_load(var4 + 216) + i32_load16_u(var2 + 112))
            var2 = (var5 + (var0 * 132))
            var13 = i32_load16_u((var5 + (var0 * 132)) + 114)
            var15 = i32_load16_u(var2 + 112)
            var2 = (1 if i32_load16_u(var2 + 112) < var17 else 0)
            if (1 if i32_load16_u(var2 + 112) < var17 else 0):
                break
            if (1 if var14 <= var15 else 0):
                break
            if (1 if var13 < var18 else 0):
                break
            if (1 if var13 >= var21 else 0):
                break
            var2 = ((var3 // 2) + var18)
            var10 = (-1 if (1 if var2 < var13 else 0) else (1 if ((var3 // 2) + var18) != var13 else 0))
            var2 = ((var4 // 2) + var17)
            break
            var10 = (1 if (1 if var13 < var18 else 0) else (-1 if (1 if var13 >= var21 else 0) else 0))
            var2 = (((1 if var2 else (-1 if (1 if var14 <= var15 else 0) else 0)) + (var10 * 3)) + 4)
            if (1 if (((1 if var2 else (-1 if (1 if var14 <= var15 else 0) else 0)) + (var10 * 3)) + 4) <= 8 else 0):
            else:
            i32_store8(i32_load8_u((var2 + 10184)) + 124, 6)
        var2 = i32_load8_u(var6 + 122)
        if (1 if var7 == 1 else 0):
            break
        if var20:
            if (1 if var8 == 0 else 0):
                func119(func37(var6, i32_load(((var2 * 72) + 9263856) + 56), 0.0, 0), var11, 12, 1)
                i32_store((var5 + (var1 * 132)) + 96, 0)
                break
            break
        var8 = (var5 + (var0 * 132))
        i32_store16((var5 + (var0 * 132)) + 108, 0)
        i32_store(var8 + 88, 0)
        var2 = i32_load(((i32_load((i32_load(9215884) + (i32_load(var8 + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if i32_load(((i32_load((i32_load(9215884) + (i32_load(var8 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            # call_indirect via table[var2]
        if (1 if i32_load8_u(var9 + 125) == 3 else 0):
            break
        var4 = i32_load(var8 + 44)
        if i32_load(var8 + 44):
            var2 = i32_load(9142848)
            var3 = i32_load(9215884)
            i32_store((i32_load(9215884) + (var4 << 4)) + 4, 1)
            i32_store((var3 + (i32_load(var8 + 44) << 4)) + 8, i32_load((var5 + (var0 * 132)) + 28))
            i32_store((var3 + (i32_load(var8 + 44) << 4)) + 12, var1)
            i32_store((var3 + (i32_load(var8 + 44) << 4)), (var2 + 40))
            break
        i32_store(var8 + 44, ((Ua(1000, 1, i32_load((var5 + (var0 * 132)) + 28), var1) & 0xFFFFFFFF) >> 2))
        break
    if (1 if i32_load8_u(var11 + 125) == 3 else 0):
        if (1 if var7 == 1 else 0):
            var7 = i32_load(9671128)
            var0 = (var5 + (var0 * 132))
            var15 = i32_load16_u(var0 + 110)
            var0 = (i32_load(9671128) + (func166(i32_load16_u((var5 + (var0 * 132)) + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110), 1) * 132))
            var16 = i32_load16_u((i32_load(9671128) + (func166(i32_load16_u((var5 + (var0 * 132)) + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110), 1) * 132)) + 112)
            var18 = (i32_load16_u((i32_load(9671128) + (func166(i32_load16_u((var5 + (var0 * 132)) + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110), 1) * 132)) + 112) + 29)
            var5 = i32_load16_u(var0 + 114)
            var21 = (i32_load16_u(var0 + 114) + 29)
            var2 = (var5 - 30)
            var1 = (var16 - 30)
            var11 = i32_load(9142440)
            var17 = (i32_load(9142440) + 2)
            var14 = ((i32_load(9142440) + 2) * i32_load(((var12 * 404) + 9568096) + 208))
            var9 = i32_load(9142840)
            var20 = 2147483647
            while True:  # loop $label15
                var4 = (var1 + 1)
                if (1 if var1 < var11 else 0):
                    var0 = (var16 - var1)
                    var8 = ((var16 - var1) * var0)
                    var0 = var2
                    while True:  # loop $label14
                        var3 = var0
                        if (1 if var11 <= var0 else 0):
                            break
                        if (1 if (var1 | var3) < 0 else 0):
                            break
                        var0 = (var5 - var3)
                        var0 = (((var5 - var3) * var0) + var8)
                        if (1 if (((var5 - var3) * var0) + var8) >= var20 else 0):
                            break
                        var13 = i32_load((var9 + (((((var3 + var14) + 1) * var17) + var4) << 2)))
                        if (1 if i32_load((var9 + (((((var3 + var14) + 1) * var17) + var4) << 2))) == 0 else 0):
                            break
                        var0 = (1 if i32_load8_u((var7 + (var13 * 132)) + 122) == var12 else 0)
                        var20 = (var0 if (1 if i32_load8_u((var7 + (var13 * 132)) + 122) == var12 else 0) else var20)
                        var10 = (var13 if var0 else var10)
                        var0 = (var3 + 1)
                        if (1 if var3 != var21 else 0):
                            continue
                        break  # end loop
                var0 = (1 if var1 != var18 else 0)
                var1 = var4
                if var0:
                    continue
                break  # end loop
            if var10:
                if (1 if i32_load((i32_load(9561692) + (var15 * 286704)) + 286684) == 0 else 0):
                    break
                var1 = (var7 + (var10 * 132))
                var0 = (var16 - i32_load16_u((var7 + (var10 * 132)) + 112))
                var0 = (var5 - i32_load16_u(var1 + 114))
                if (1 if ((((var16 - i32_load16_u((var7 + (var10 * 132)) + 112)) * var0) + ((var5 - i32_load16_u(var1 + 114)) * var0)) - 1) < 50 else 0):
                    break
                break
                break
            func29(var6, 1)
            break
        if (1 if var12 == var17 else 0):
            var2 = i32_load((var5 + (var0 * 132)) + 88)
            i32_store((var5 + (var1 * 132)) + 72, 0)
            break
        func29(var6, 1)
        break
    if (1 if var12 != var17 else 0):
        break
    var3 = (var5 + (var1 * 132))
    var4 = i32_load((var5 + (var1 * 132)) + 72)
    if (1 if i32_load((var5 + (var1 * 132)) + 72) > 3 else 0):
        break
    var2 = i32_load((var5 + (var0 * 132)) + 88)
    i32_store(var3 + 72, 0)
    i32_store8(var11 + 125, 0)
    var3 = ((((var2 * 3) & 0xFFFFFFFF) // 1000) + var4)
    if i32_load(i32_load(9142424) + 176):
        break
    var2 = (var5 + (var1 * 132))
    if (1 if i32_load((var5 + (var1 * 132)) + 80) < i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284320)) else 0):
        break
    break
    i32_store(var3 + 72, (var4 - 3))
    var3 = 0
    var4 = i32_load(9671128)
    if (1 if i32_load((i32_load(9671128) + (var1 * 132)) + 92) == 0 else 0):
        break
    var2 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var4 + (var1 * 132)) + 28) else 0):
            break
    break
    var3 = 0
    i32_store((var5 + (var1 * 132)) + 88, i32_load(9142848))
    var5 = i32_load(9671128)
    var11 = (i32_load(9671128) + (var0 * 132))
    var2 = (i32_load((i32_load(9671128) + (var0 * 132)) + 88) + 1000)
    if (((1 if (i32_load((i32_load(9671128) + (var0 * 132)) + 88) + 1000) == i32_load(((var7 << 2) + 51760)) else 0) & (1 if var12 != var17 else 0)) | var3):
        var4 = (var5 + (var0 * 132))
        if (1 if var12 != var17 else 0):
        else:
        i32_store16(i32_load((((i32_load(9561692) + (i32_load16_u((var5 + (var0 * 132)) + 110) * 286704)) + (var7 << 2)) + 283984)) + 108, var3)
        var2 = (var5 + (var1 * 132))
        i32_store(var11 + 88, ((i32_load8_u((var5 + (var1 * 132)) + 122) << 16) + var7))
        func207(var11, i32_load(var2 + 28))
        if var20:
            break
        var20 = i32_load16_u(var4 + 108)
        # br_table ['$label23', '$label24', '$label24', '$label23', '$label24']
        _br_idx = var7
        break  # br_table
        var20 = ((var20 & 0xFFFFFFFF) // i32_load(((i32_load(9561692) + (i32_load16_u((var5 + (var0 * 132)) + 110) * 286704)) + 284100)))
        if (1 if i32_load8_u((var5 + (var1 * 132)) + 125) == 10 else 0):
            break
        var9 = (10 if (1 if var7 == 1 else 0) else var20)
        var3 = (global0 - 16)
        global global0
        global0 = (global0 - 16)
        var14 = (var5 + (var1 * 132))
        if (1 if i32_load8_u((var5 + (var1 * 132)) + 125) == 3 else 0):
            break
        var1 = i32_load(var14 + 64)
        if (1 if var9 >= i32_load(var14 + 64) else 0):
            i32_store(var14 + 64, 0)
            break
        i32_store(var14 + 64, (var1 - var9))
        if (1 if i32_load(var14 + 92) == 0 else 0):
            break
        if i32_load8_u(9147141):
            break
        i32_store(var3, var9)
        a_b()
        global global0
        global0 = (var3 + 16)
        if (1 if i32_load(var4 + 92) == 0 else 0):
            break
        if i32_load(9140316):
            if (1 if i32_load(9140320) != i32_load((var5 + (var0 * 132)) + 28) else 0):
                break
        var1 = (0 if var8 else var7)
        var9 = i32_load8_u(var2 + 122)
        if (1 if i32_load8_u(var2 + 122) != i32_load(38508) else 0):
            if (1 if i32_load(38504) != var9 else 0):
                break
        var17 = (var5 + (var0 * 132))
        var10 = i32_load16_u((var5 + (var0 * 132)) + 112)
        var3 = i32_load16_u(var17 + 110)
        var13 = (var10 + 1)
        var12 = i32_load(9142440)
        var6 = (i32_load(9142440) + 2)
        var15 = i32_load(9671128)
        var18 = i32_load(9142840)
        var16 = i32_load16_u(var17 + 114)
        var4 = (1 if var12 <= i32_load16_u(var17 + 114) else 0)
        if (1 if var12 <= i32_load16_u(var17 + 114) else 0):
            break
        if (1 if var12 <= var13 else 0):
            break
        if (1 if (var13 | var16) < 0 else 0):
            break
        var2 = i32_load((((var10 + (((var6 + var16) + 1) * var6)) << 2) + var18) + 8)
        if (1 if i32_load((((var10 + (((var6 + var16) + 1) * var6)) << 2) + var18) + 8) < 3 else 0):
            break
        var2 = (var15 + (var2 * 132))
        if (1 if i32_load16_u((var15 + (var2 * 132)) + 110) != var3 else 0):
            break
        # br_table ['$label28', '$label29', '$label29', '$label29', '$label29', '$label29', '$label29', '$label29', '$label29', '$label29', '$label28', '$label29']
        _br_idx = (i32_load8_u(var2 + 125) - 4)
        break  # br_table
        var7 = 1
        var2 = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192)
        if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192) == var1 else 0):
            break
        if (1 if var2 == 4 else 0):
            break
        var14 = (var16 - 1)
        var8 = (1 if var12 <= (var16 - 1) else 0)
        if (1 if var12 <= (var16 - 1) else 0):
            break
        if (1 if var12 <= var13 else 0):
            break
        if (1 if (var13 | var14) < 0 else 0):
            break
        var2 = i32_load((((var10 + ((var6 + var16) * var6)) << 2) + var18) + 8)
        if (1 if i32_load((((var10 + ((var6 + var16) * var6)) << 2) + var18) + 8) < 3 else 0):
            break
        var2 = (var15 + (var2 * 132))
        if (1 if i32_load16_u((var15 + (var2 * 132)) + 110) != var3 else 0):
            break
        # br_table ['$label31', '$label32', '$label32', '$label32', '$label32', '$label32', '$label32', '$label32', '$label32', '$label32', '$label31', '$label32']
        _br_idx = (i32_load8_u(var2 + 125) - 4)
        break  # br_table
        var7 = 1
        var2 = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192)
        if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192) == var1 else 0):
            break
        if (1 if var2 == 4 else 0):
            break
        if var8:
            break
        if (1 if var10 >= var12 else 0):
            break
        if (1 if (var10 | var14) < 0 else 0):
            break
        var2 = i32_load((var18 + ((var13 + ((var6 + var16) * var6)) << 2)))
        if (1 if i32_load((var18 + ((var13 + ((var6 + var16) * var6)) << 2))) < 3 else 0):
            break
        var2 = (var15 + (var2 * 132))
        if (1 if i32_load16_u((var15 + (var2 * 132)) + 110) != var3 else 0):
            break
        # br_table ['$label33', '$label34', '$label34', '$label34', '$label34', '$label34', '$label34', '$label34', '$label34', '$label34', '$label33', '$label34']
        _br_idx = (i32_load8_u(var2 + 125) - 4)
        break  # br_table
        var7 = 1
        var2 = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192)
        if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192) == var1 else 0):
            break
        if (1 if var2 == 4 else 0):
            break
        var21 = (var10 - 1)
        if var8:
            break
        if (1 if var12 <= var21 else 0):
            break
        if (1 if (var14 | var21) < 0 else 0):
            break
        var2 = i32_load((var18 + ((((var6 + var16) * var6) + var10) << 2)))
        if (1 if i32_load((var18 + ((((var6 + var16) * var6) + var10) << 2))) < 3 else 0):
            break
        var2 = (var15 + (var2 * 132))
        if (1 if i32_load16_u((var15 + (var2 * 132)) + 110) != var3 else 0):
            break
        # br_table ['$label35', '$label36', '$label36', '$label36', '$label36', '$label36', '$label36', '$label36', '$label36', '$label36', '$label35', '$label36']
        _br_idx = (i32_load8_u(var2 + 125) - 4)
        break  # br_table
        var7 = 1
        var2 = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192)
        if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192) == var1 else 0):
            break
        if (1 if var2 == 4 else 0):
            break
        var8 = (var16 + 1)
        if var4:
            break
        if (1 if var12 <= var21 else 0):
            break
        if (1 if (var16 | var21) < 0 else 0):
            break
        var2 = i32_load((var18 + ((((var6 + var8) * var6) + var10) << 2)))
        if (1 if i32_load((var18 + ((((var6 + var8) * var6) + var10) << 2))) < 3 else 0):
            break
        var2 = (var15 + (var2 * 132))
        if (1 if i32_load16_u((var15 + (var2 * 132)) + 110) != var3 else 0):
            break
        # br_table ['$label37', '$label38', '$label38', '$label38', '$label38', '$label38', '$label38', '$label38', '$label38', '$label38', '$label37', '$label38']
        _br_idx = (i32_load8_u(var2 + 125) - 4)
        break  # br_table
        var7 = 1
        var2 = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192)
        if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192) == var1 else 0):
            break
        if (1 if var2 == 4 else 0):
            break
        var4 = (1 if var8 >= var12 else 0)
        if (1 if var8 >= var12 else 0):
            break
        if (1 if var12 <= var21 else 0):
            break
        if (1 if (var8 | var21) < 0 else 0):
            break
        var2 = i32_load((var18 + (((((var6 + var16) + 2) * var6) + var10) << 2)))
        if (1 if i32_load((var18 + (((((var6 + var16) + 2) * var6) + var10) << 2))) < 3 else 0):
            break
        var2 = (var15 + (var2 * 132))
        if (1 if i32_load16_u((var15 + (var2 * 132)) + 110) != var3 else 0):
            break
        # br_table ['$label39', '$label40', '$label40', '$label40', '$label40', '$label40', '$label40', '$label40', '$label40', '$label40', '$label39', '$label40']
        _br_idx = (i32_load8_u(var2 + 125) - 4)
        break  # br_table
        var7 = 1
        var2 = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192)
        if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192) == var1 else 0):
            break
        if (1 if var2 == 4 else 0):
            break
        if var4:
            break
        if (1 if var10 >= var12 else 0):
            break
        if (1 if (var8 | var10) < 0 else 0):
            break
        var2 = i32_load((var18 + ((var13 + (((var6 + var16) + 2) * var6)) << 2)))
        if (1 if i32_load((var18 + ((var13 + (((var6 + var16) + 2) * var6)) << 2))) < 3 else 0):
            break
        var2 = (var15 + (var2 * 132))
        if (1 if i32_load16_u((var15 + (var2 * 132)) + 110) != var3 else 0):
            break
        # br_table ['$label41', '$label42', '$label42', '$label42', '$label42', '$label42', '$label42', '$label42', '$label42', '$label42', '$label41', '$label42']
        _br_idx = (i32_load8_u(var2 + 125) - 4)
        break  # br_table
        var7 = 1
        var2 = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192)
        if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192) == var1 else 0):
            break
        if (1 if var2 == 4 else 0):
            break
        if var4:
            break
        if (1 if var12 <= var13 else 0):
            break
        if (1 if (var8 | var13) < 0 else 0):
            break
        var2 = i32_load((((var10 + (((var6 + var16) + 2) * var6)) << 2) + var18) + 8)
        if (1 if i32_load((((var10 + (((var6 + var16) + 2) * var6)) << 2) + var18) + 8) < 3 else 0):
            break
        var2 = (var15 + (var2 * 132))
        if (1 if i32_load16_u((var15 + (var2 * 132)) + 110) != var3 else 0):
            break
        # br_table ['$label43', '$label44', '$label44', '$label44', '$label44', '$label44', '$label44', '$label44', '$label44', '$label44', '$label43', '$label44']
        _br_idx = (i32_load8_u(var2 + 125) - 4)
        break  # br_table
        var7 = 1
        var2 = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192)
        if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 192) == var1 else 0):
            break
        if (1 if var2 == 4 else 0):
            break
        var7 = 0
        if var7:
            i32_store(var11 + 88, 0)
            i32_store((i32_load(9215884) + (i32_load(var17 + 44) << 4)), (i32_load(9142848) + 40))
            break
        if (1 if i32_load((i32_load(9561692) + (var3 * 286704)) + 286684) == 0 else 0):
            break
        if func87(var11, var9):
            break
        var0 = (var5 + (var0 * 132))
        var0 = func166(i32_load16_u((var5 + (var0 * 132)) + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110), var1)
        if func166(i32_load16_u((var5 + (var0 * 132)) + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110), var1):
            break
        func29(var11, 1)
        break
    i32_store(var11 + 88, var2)
    i32_store((i32_load(9215884) + (i32_load((var5 + (var0 * 132)) + 44) << 4)), (i32_load(9142848) + 40))
    global global0
    global0 = (var19 + 48)
    return func28(1, 1)

