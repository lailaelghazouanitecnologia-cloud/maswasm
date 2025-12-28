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
# $func906
# ==========================================================
def func906(var0, var1, param2):
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
    var12 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var6 = i32_load(9671128)
    var3 = (i32_load(9671128) + (var0 * 132))
    var8 = (var6 + (var1 * 132))
    var4 = i32_load8_u((var6 + (var1 * 132)) + 125)
    if (1 if i32_load8_u((var6 + (var1 * 132)) + 125) == 3 else 0):
        var0 = func336(i32_load16_u(var3 + 112), i32_load16_u(var3 + 114), i32_load16_u(var3 + 110))
        if func336(i32_load16_u(var3 + 112), i32_load16_u(var3 + 114), i32_load16_u(var3 + 110)):
            break
        func29(var3, 1)
        break
    var5 = i32_load8_u(var8 + 122)
    if (1 if i32_load8_u(var3 + 125) == 1 else 0):
        var2 = ((var5 * 404) + 9568096)
        var14 = i32_load(((var5 * 404) + 9568096) + 220)
        var4 = (var6 + (var1 * 132))
        var5 = i32_load16_u((var6 + (var1 * 132)) + 114)
        var8 = (i32_load(((var5 * 404) + 9568096) + 220) + i32_load16_u((var6 + (var1 * 132)) + 114))
        var15 = i32_load(var2 + 216)
        var10 = i32_load16_u(var4 + 112)
        var7 = (i32_load(var2 + 216) + i32_load16_u(var4 + 112))
        var9 = (var6 + (var0 * 132))
        var2 = i32_load16_u((var6 + (var0 * 132)) + 114)
        var4 = 6
        var9 = i32_load16_u(var9 + 112)
        var11 = (1 if i32_load16_u(var9 + 112) < var10 else 0)
        if (1 if i32_load16_u(var9 + 112) < var10 else 0):
            break
        if (1 if var7 <= var9 else 0):
            break
        if (1 if var2 < var5 else 0):
            break
        if (1 if var2 >= var8 else 0):
            break
        var5 = ((var14 // 2) + var5)
        var5 = (-1 if (1 if var2 > var5 else 0) else (1 if ((var14 // 2) + var5) != var2 else 0))
        var2 = ((var15 // 2) + var10)
        break
        var5 = (1 if (1 if var2 < var5 else 0) else (-1 if (1 if var2 >= var8 else 0) else 0))
        var2 = (((1 if var11 else (-1 if (1 if var7 <= var9 else 0) else 0)) + (var5 * 3)) + 4)
        if (1 if (((1 if var11 else (-1 if (1 if var7 <= var9 else 0) else 0)) + (var5 * 3)) + 4) <= 8 else 0):
            var4 = i32_load8_u((var2 + 10184))
        var2 = (var6 + (var0 * 132))
        i32_store8((var6 + (var0 * 132)) + 124, var4)
        var4 = i32_load(((i32_load((i32_load(9215884) + (i32_load(var2 + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if i32_load(((i32_load((i32_load(9215884) + (i32_load(var2 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            # call_indirect via table[var4]
        if (1 if i32_load8_u(var3 + 125) == 3 else 0):
            break
        var4 = i32_load(var2 + 44)
        if i32_load(var2 + 44):
            var5 = i32_load(9142848)
            var3 = i32_load(9215884)
            i32_store((i32_load(9215884) + (var4 << 4)) + 4, 4)
            i32_store((var3 + (i32_load(var2 + 44) << 4)) + 8, i32_load((var6 + (var0 * 132)) + 28))
            i32_store((var3 + (i32_load(var2 + 44) << 4)) + 12, var1)
            i32_store((var3 + (i32_load(var2 + 44) << 4)), (var5 + 40))
            break
        i32_store(var2 + 44, ((Ua(1000, 4, i32_load((var6 + (var0 * 132)) + 28), var1) & 0xFFFFFFFF) >> 2))
        break
    if (1 if var4 == 14 else 0):
        i32_store((i32_load(9215884) + (i32_load((var6 + (var0 * 132)) + 44) << 4)), (i32_load(9142848) + 40))
        break
    var2 = i32_load(((var5 * 404) + 9568096) + 116)
    var17 = (var6 + (var0 * 132))
    var14 = i32_load16_u((var6 + (var0 * 132)) + 110)
    var15 = i32_load(9561692)
    if (1 if var4 == 4 else 0):
        var2 = (((i32_load(i32_load(9142424) + 124) * var2) & 0xFFFFFFFF) // 100)
    var7 = (var6 + (var1 * 132))
    if var2:
    else:
    var2 = 2147483647
    var2 = (2147483647 if (1 if var4 == 4 else 0) else ((var2 & 0xFFFFFFFF) >> 2))
    var10 = (5 + (1 if (1 if i32_load(((var5 * 404) + 9568096) + 268) == 2 else 0) else ((((i32_load(((var15 + (var14 * 286704)) + 284004)) * ((i32_load((var6 + (var1 * 132)) + 68) & 0xFFFFFFFF) // var2)) & 0xFFFFFFFF) // 100) if (1 if var2 <= 1 else 0) else (2147483647 if (1 if var4 == 4 else 0) else ((var2 & 0xFFFFFFFF) >> 2)))))
    i32_store(i32_load(var7 + 64) + 64, (5 + (1 if (1 if i32_load(((var5 * 404) + 9568096) + 268) == 2 else 0) else ((((i32_load(((var15 + (var14 * 286704)) + 284004)) * ((i32_load((var6 + (var1 * 132)) + 68) & 0xFFFFFFFF) // var2)) & 0xFFFFFFFF) // 100) if (1 if var2 <= 1 else 0) else (2147483647 if (1 if var4 == 4 else 0) else ((var2 & 0xFFFFFFFF) >> 2))))))
    var11 = (var7 - -64)
    var9 = (var6 + (var0 * 132))
    var2 = i32_load16_u((var6 + (var0 * 132)) + 112)
    var13 = ((i32_load16_u((var6 + (var0 * 132)) + 112) << 5) - i32_load(9142952))
    var13 = i32_load16_u(var9 + 114)
    var16 = ((i32_load16_u(var9 + 114) << 5) - i32_load(9142956))
    if (1 if (((((i32_load16_u((var6 + (var0 * 132)) + 112) << 5) - i32_load(9142952)) * var13) + (((i32_load16_u(var9 + 114) << 5) - i32_load(9142956)) * var16)) - 1) > 9000000 else 0):
        break
    var18 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var16 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var13) + var2) << 1)))
    if (1 if var18 == 2 else 0):
        if (1 if var16 > 1 else 0):
            break
        break
    if (1 if var16 == 0 else 0):
        break
    i32_store(var12 + 40, var13)
    i32_store(var12 + 36, var2)
    i32_store(var12 + 32, i32_load(((((i32_load(9142848) + var2) % 7) << 2) + 57248)))
    a_b()
    var10 = i32_load(var11)
    var7 = i32_load(var7 + 68)
    if (1 if i32_load(var7 + 68) <= var10 else 0):
        i32_store(var11, var7)
        var2 = 0
        if (1 if i32_load(((i32_load8_u(var8 + 122) * 404) + 9568096) + 192) > 3 else 0):
            var10 = 4
            break
        var7 = (var6 + (var0 * 132))
        var10 = i32_load((var6 + (var0 * 132)) + 20)
        if (1 if i32_load((var6 + (var0 * 132)) + 20) == 0 else 0):
            break
        var11 = i32_load(var10 + 8)
        if (1 if i32_load(var10 + 8) < 3 else 0):
            break
        var13 = i32_load(var10)
        if (1 if (i32_load(i32_load(var10)) - 1) > 1 else 0):
            break
        var10 = 4
        if (1 if (i32_load(var13 + 4) + 7) != var11 else 0):
            break
        var11 = i32_load8_u(var7 + 129)
        if i32_load((i32_load(9561692) + (i32_load16_u(var17 + 110) * 286704)) + 286684):
            var7 = 0
            var10 = 4
            # br_table ['$label7', '$label8', '$label5', '$label9', '$label5']
            _br_idx = (var11 - 1)
            break  # br_table
        var7 = 0
        # br_table ['$label7', '$label8', '$label8', '$label9', '$label8']
        _br_idx = (var11 - 1)
        break  # br_table
        var7 = i32_load(38504)
        break
        var7 = i32_load(38508)
        var10 = 4
        var3 = func224(var3, i32_load(((var5 * 404) + 9568096) + 192), var7)
        if (1 if func224(var3, i32_load(((var5 * 404) + 9568096) + 192), var7) == 0 else 0):
            break
        i32_store((i32_load(9671128) + (var3 * 132)) + 88, i32_load(9142848))
        var10 = 1
        var2 = var3
        if (1 if var4 == 4 else 0):
            var3 = (var6 + (var1 * 132))
            var17 = i32_load16_u((var6 + (var1 * 132)) + 110)
            var18 = i32_load(9561692)
            i32_store8(var8 + 125, 0)
            var4 = i32_load(var3 + 40)
            if (1 if i32_load(var3 + 40) == 0 else 0):
                break
            if (1 if i32_load8_u(9142916) == 0 else 0):
                break
            var5 = i32_load((var6 + (var1 * 132)) + 92)
            i32_store(var12 + 20, var4)
            i32_store(var12 + 16, (1 if var5 != 0 else 0))
            a_b()
            if i32_load((var15 + (var14 * 286704)) + 286684):
                break
            var4 = 0
            var5 = i32_load((var6 + (var0 * 132)) + 20)
            if (1 if i32_load((var6 + (var0 * 132)) + 20) == 0 else 0):
                break
            if (1 if i32_load(var5 + 8) < 3 else 0):
                break
            var4 = (1 if (i32_load(i32_load(var5)) - 1) < 2 else 0)
            if var2:
                break
            if var4:
                break
            var19 = i32_load16_u(var3 + 110)
            var7 = 0
            var15 = i32_load16_u(var9 + 112)
            var20 = (i32_load16_u(var9 + 112) + 29)
            var11 = i32_load16_u(var9 + 114)
            var21 = (i32_load16_u(var9 + 114) + 29)
            var9 = (var11 - 30)
            var3 = (var15 - 30)
            var13 = i32_load(9142440)
            var16 = (i32_load(9142440) + 2)
            var22 = i32_load(9671128)
            var23 = i32_load(9142840)
            var14 = 2147483647
            while True:  # loop $label15
                var5 = (var3 + 1)
                if (1 if var3 < var13 else 0):
                    var2 = (var3 - var15)
                    var24 = ((var3 - var15) * var2)
                    var2 = var9
                    while True:  # loop $label14
                        var4 = var2
                        if (1 if var13 <= var2 else 0):
                            break
                        if (1 if (var3 | var4) < 0 else 0):
                            break
                        var2 = (var4 - var11)
                        var2 = (((var4 - var11) * var2) + var24)
                        if (1 if (((var4 - var11) * var2) + var24) >= var14 else 0):
                            break
                        var2 = (var22 + (i32_load((var23 + ((var5 + (((var4 + var16) + 1) * var16)) << 2))) * 132))
                        var25 = ((1 if i32_load8_u((var22 + (i32_load((var23 + ((var5 + (((var4 + var16) + 1) * var16)) << 2))) * 132)) + 125) == 4 else 0) & (1 if i32_load16_u(var2 + 110) == var19 else 0))
                        var14 = (var2 if ((1 if i32_load8_u((var22 + (i32_load((var23 + ((var5 + (((var4 + var16) + 1) * var16)) << 2))) * 132)) + 125) == 4 else 0) & (1 if i32_load16_u(var2 + 110) == var19 else 0)) else var14)
                        var7 = (i32_load(var2 + 28) if var25 else var7)
                        var2 = (var4 + 1)
                        if (1 if var4 < var21 else 0):
                            continue
                        break  # end loop
                var2 = (1 if var3 < var20 else 0)
                var3 = var5
                if var2:
                    continue
                break  # end loop
            var2 = var7
            var4 = 0
            var3 = i32_load8_u(var8 + 122)
            var5 = i32_load(((i32_load8_u(var8 + 122) * 72) + 9263856))
            if (1 if i32_load(((i32_load8_u(var8 + 122) * 72) + 9263856)) == 0 else 0):
                break
            var9 = i32_load(var5 + 20)
            if (1 if i32_load(var5 + 20) == 0 else 0):
                break
            if (1 if i32_load(38604) == var3 else 0):
                break
            var4 = (i32_load((var6 + (var1 * 132)) + 28) % var9)
            i32_store8((var6 + (var1 * 132)) + 124, var4)
            if (1 if var3 != i32_load(38600) else 0):
                if (1 if i32_load(38472) != var3 else 0):
                    break
            func286(var8)
            break
            func420(var8)
            var3 = i32_load(9671128)
            var4 = (var1 * 132)
            if (1 if i32_load(9142872) == i32_load16_u((i32_load(9671128) + (var1 * 132)) + 110) else 0):
                i32_store(var12, i32_load(39228))
                a_b()
            else:
            var3 = (var3 + var4)
            var4 = ((i32_load(9671128) + (i32_load8_u((var3 + var4) + 122) << 2)) + 282828)
            i32_store(((i32_load(9671128) + (i32_load8_u((var3 + var4) + 122) << 2)) + 282828), (i32_load(var4) - 1))
            var4 = i32_load(var3 + 20)
            if (1 if i32_load(var3 + 20) == 0 else 0):
                break
            if (1 if i32_load(var4 + 8) == 0 else 0):
                break
            func230(var3)
            break
        var5 = 0
        var3 = i32_load((var6 + (var0 * 132)) + 20)
        if (1 if i32_load((var6 + (var0 * 132)) + 20) == 0 else 0):
            break
        if (1 if i32_load(var3 + 8) < 3 else 0):
            break
        var5 = (1 if (i32_load(i32_load(var3)) - 1) < 2 else 0)
        if var2:
            break
        if var5:
            break
        var2 = func336(i32_load16_u(var9 + 112), i32_load16_u(var9 + 114), i32_load16_u((var6 + (var1 * 132)) + 110))
        var0 = (i32_load(9671128) + (var0 * 132))
        if var2:
            break
        func29(var0, 1)
        break
    if (1 if var4 != 4 else 0):
        break
    var2 = (var6 + (var1 * 132))
    i32_store((var6 + (var1 * 132)) + 88, i32_load(9142848))
    var3 = i32_load8_u(var8 + 122)
    var3 = ((((3 if (1 if i32_load(38560) == var3 else 0) else (3 if (1 if i32_load8_u(var8 + 122) == i32_load(38620) else 0) else 4)) * var10) & 0xFFFFFFFF) // var7)
    if (1 if ((((3 if (1 if i32_load(38560) == var3 else 0) else (3 if (1 if i32_load8_u(var8 + 122) == i32_load(38620) else 0) else 4)) * var10) & 0xFFFFFFFF) // var7) <= i32_load8_u(var2 + 124) else 0):
        break
    i32_store8(var2 + 124, var3)
    i32_store((i32_load(9215884) + (i32_load((var6 + (var0 * 132)) + 44) << 4)), (i32_load(9142848) + 40))
    var0 = i32_load(9671128)
    if (1 if i32_load((i32_load(9671128) + (var1 * 132)) + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var0 + (var1 * 132)) + 28) else 0):
            break
    global global0
    global0 = (var12 + 48)
    return func28(1, 1)

