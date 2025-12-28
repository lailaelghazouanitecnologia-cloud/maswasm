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
# $func778
# ==========================================================
def func778(var0, var1, param2):
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
    var5 = i32_load(9671128)
    var3 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 1 else 0):
        i32_store16(var3 + 108, 0)
        i32_store(var3 + 88, 0)
        var2 = i32_load(((i32_load((i32_load(9215884) + (i32_load(var3 + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if i32_load(((i32_load((i32_load(9215884) + (i32_load(var3 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            # call_indirect via table[var2]
        if (1 if i32_load8_u(var3 + 125) == 3 else 0):
            break
        var4 = i32_load(var3 + 44)
        if i32_load(var3 + 44):
            var6 = i32_load(9142848)
            var2 = i32_load(9215884)
            i32_store((i32_load(9215884) + (var4 << 4)) + 4, 55)
            i32_store((var2 + (i32_load(var3 + 44) << 4)) + 8, i32_load((var5 + (var0 * 132)) + 28))
            i32_store((var2 + (i32_load(var3 + 44) << 4)) + 12, var1)
            i32_store((var2 + (i32_load(var3 + 44) << 4)), (var6 + 80))
            return
        i32_store(var3 + 44, ((Ua(2000, 55, i32_load((var5 + (var0 * 132)) + 28), var1) & 0xFFFFFFFF) >> 2))
        return
    if (1 if i32_load8_u((var5 + (var1 * 132)) + 125) == 3 else 0):
        func29(var3, 1)
        return
    var2 = (var5 + (var0 * 132))
    var4 = (i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704))
    var6 = (i32_load16_u(var2 + 108) + i32_load16_u(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284328)))
    i32_store16((var5 + (var0 * 132)) + 108, (i32_load16_u(var2 + 108) + i32_load16_u(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284328))))
    var4 = i32_load((var4 + 284332))
    if (1 if i32_load((var4 + 284332)) <= (var6 & 65535) else 0):
        i32_store16(var2 + 108, var4)
        i32_store(var2 + 88, 2)
        func207(var3, i32_load((var5 + (var1 * 132)) + 28))
        var15 = i32_load16_u(var2 + 110)
        var9 = i32_load16_u(var2 + 112)
        var16 = (i32_load16_u(var2 + 112) + 149)
        var10 = i32_load16_u(var2 + 114)
        var17 = (i32_load16_u(var2 + 114) + 149)
        var18 = (var10 - 75)
        var2 = (var9 - 75)
        var11 = i32_load(9142440)
        var12 = (i32_load(9142440) + 2)
        var19 = i32_load(38872)
        var20 = i32_load(38796)
        var21 = i32_load(38584)
        var22 = i32_load(9671128)
        var23 = i32_load(9142840)
        var6 = 2147483647
        while True:  # loop $label5
            var13 = (var2 + 1)
            if (1 if var2 < var11 else 0):
                var1 = (var2 - var9)
                var24 = ((var2 - var9) * var1)
                var1 = var18
                while True:  # loop $label4
                    var4 = var1
                    var1 = (var1 - var10)
                    var1 = (((var1 - var10) * var1) + var24)
                    if (1 if ((((var1 - var10) * var1) + var24) - 1) > 5625 else 0):
                        break
                    if (1 if var4 >= var11 else 0):
                        break
                    if (1 if (var2 | var4) < 0 else 0):
                        break
                    if (1 if var1 >= var6 else 0):
                        break
                    var7 = (var22 + (i32_load((var23 + ((var13 + (((var4 + var12) + 1) * var12)) << 2))) * 132))
                    if (1 if i32_load16_u((var22 + (i32_load((var23 + ((var13 + (((var4 + var12) + 1) * var12)) << 2))) * 132)) + 110) != var15 else 0):
                        break
                    # br_table ['$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label1', '$label2']
                    _br_idx = (i32_load8_u(var7 + 125) - 4)
                    break  # br_table
                    var14 = i32_load8_u(var7 + 122)
                    if (1 if var21 == i32_load8_u(var7 + 122) else 0):
                        break
                    if (1 if var14 == var20 else 0):
                        break
                    if (1 if var14 != var19 else 0):
                        break
                    var8 = i32_load(var7 + 28)
                    var6 = var1
                    var1 = (var4 + 1)
                    if (1 if var4 < var17 else 0):
                        continue
                    break  # end loop
            var1 = (1 if var2 < var16 else 0)
            var2 = var13
            if var1:
                continue
            break  # end loop
        var1 = var8
        if var8:
            break
        func29(var3, 1)
        if (1 if i32_load((var5 + (var0 * 132)) + 92) == 0 else 0):
            break
        if i32_load(9140316):
            if (1 if i32_load(9140320) != i32_load((var5 + (var0 * 132)) + 28) else 0):
                break
        return
    if (1 if i32_load(var2 + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var5 + (var0 * 132)) + 28) else 0):
            break
    i32_store((i32_load(9215884) + (i32_load((var5 + (var0 * 132)) + 44) << 4)), (i32_load(9142848) + 80))


# ==========================================================
# $func797
# ==========================================================
def func797(var0, var1, var2):
    var3 = 0
    var0 = 0
    if (1 if i32_load(59164) == i32_load(9142384) else 0):
        i32_store(9143000, 0)
        var3 = i32_load(9213820)
        if i32_load(9213820):
            func47((i32_load(9671128) + (var3 * 132)))
            i32_store(9213820, 0)
        func45()
    if var2:
        while True:  # loop $label0
            func202((i32_load(9671128) + (i32_load((var1 + (var0 << 2))) * 132)), 1, 0)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var2 else 0):
                continue
            break  # end loop
    if (1 if i32_load(59164) == i32_load(9142384) else 0):


# ==========================================================
# $func826
# ==========================================================
def func826(var0, var1, var2, var3, var4):
    var3 = i32_load(9671128)
    var2 = (i32_load(9671128) + (i32_load(var1) * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 125) != 10 else 0):
        if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 188) > 3 else 0):
            break
    var2 = (var3 + (var0 * 132))
    var4 = i32_load((var3 + (var0 * 132)) + 88)
    if (1 if i32_load((var3 + (var0 * 132)) + 88) == 0 else 0):
        return 0
    if (1 if i32_load16_u(var2 + 108) == 0 else 0):
        break
    var1 = ((var4 & 0xFFFFFFFF) >> 16)
    var4 = (var4 & 65535)
    if (1 if ((var4 & 0xFFFFFFFF) >> 16) != ((var4 & 65535) if (1 if var4 != 3 else 0) else 0) else 0):
        break
    var0 = (var3 + (var0 * 132))
    var0 = func166(i32_load16_u((var3 + (var0 * 132)) + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110), var1)
    if func166(i32_load16_u((var3 + (var0 * 132)) + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110), var1):
        return 1
    func29(var2, 1)
    return 1


# ==========================================================
# $func842
# ==========================================================
def func842(var0, var1):
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
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if i32_load8_u(9147152):
        break
    var5 = i32_load(9671128)
    var2 = (i32_load(9671128) + (var0 * 132))
    var10 = i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110)
    var8 = i32_load(((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110) * 286704)) + 284324))
    if (1 if i32_load(((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110) * 286704)) + 284324)) == 0 else 0):
        break
    var4 = i32_load(var2 + 80)
    var11 = ((i32_load(var2 + 80) & 0xFFFFFFFF) // var8)
    if (1 if var4 >= var8 else 0):
        var2 = (var0 * 132)
        if (1 if func225((var1 + 12), (var1 + 8), (var5 + (var0 * 132)), ((i32_load(38984) * 404) + 9568096)) == 0 else 0):
            break
        var2 = func34(i32_load(38984), i32_load16_u((i32_load(9671128) + var2) + 110), i32_load(var1 + 12), i32_load(var1 + 8), 0, 1)
        if (1 if func34(i32_load(38984), i32_load16_u((i32_load(9671128) + var2) + 110), i32_load(var1 + 12), i32_load(var1 + 8), 0, 1) == 0 else 0):
            break
        var5 = i32_load(9671128)
        var2 = (i32_load(9671128) + (var2 * 132))
        i64_store((i32_load(9671128) + (var2 * 132)) + 64, 1073741824250)
        i32_store(var2 + 56, var10)
        i32_store(var2 + 52, var8)
        var16 = i32_load16_u((var5 + (var0 * 132)) + 110)
        var9 = i32_load(9142440)
        var14 = i32_load16_u(var2 + 114)
        var15 = i32_load16_u(var2 + 112)
        while True:  # loop $label8
            var5 = var3
            var3 = (var3 << 2)
            var7 = (i32_load((((var3 << 2) | 4) + 8611904)) + var14)
            if (1 if var9 <= (i32_load((((var3 << 2) | 4) + 8611904)) + var14) else 0):
                break
            var4 = (i32_load((var3 + 8611904)) + var15)
            if (1 if var9 <= (i32_load((var3 + 8611904)) + var15) else 0):
                break
            if (1 if (var4 | var7) < 0 else 0):
                break
            var12 = i32_load(9671128)
            var3 = (var9 + 2)
            var6 = (i32_load(9671128) + (i32_load((i32_load(9142840) + ((var4 + (((var7 + (var9 + 2)) + 1) * var3)) << 2)) + 4) * 132))
            var3 = i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9142840) + ((var4 + (((var7 + (var9 + 2)) + 1) * var3)) << 2)) + 4) * 132)) + 122)
            # br_table ['$label3', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label3', '$label4']
            _br_idx = (i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9142840) + ((var4 + (((var7 + (var9 + 2)) + 1) * var3)) << 2)) + 4) * 132)) + 122) + -64)
            break  # br_table
            if (1 if var3 != 10 else 0):
                break
            if (1 if i32_load8_u(var6 + 129) != 10 else 0):
                break
            if (1 if i32_load16_u(var6 + 110) != var16 else 0):
                break
            var4 = i32_load8_u(var6 + 125)
            var3 = i32_load(var6 + 44)
            if (1 if ((1 if i32_load((i32_load(9215884) + (i32_load(var6 + 44) << 4)) + 4) == 22 else 0) | (1 if var3 == 0 else 0)) == 0 else 0):
                break
            if var4:
                break
            if (1 if i32_load(var6 + 36) == 0 else 0):
                break
            break
            if (1 if var4 != 1 else 0):
                break
            var4 = i32_load(var6 + 32)
            var7 = (var12 + (i32_load(var6 + 32) * 132))
            var3 = i32_load8_u((var12 + (i32_load(var6 + 32) * 132)) + 122)
            if (1 if i32_load8_u((var12 + (i32_load(var6 + 32) * 132)) + 122) == i32_load(38528) else 0):
                break
            if (1 if i32_load8_u(var7 + 125) == 3 else 0):
                break
            if (1 if var4 == 0 else 0):
                break
            if (1 if i32_load(38984) != var3 else 0):
                break
            var12 = i32_load16_u(var6 + 114)
            var3 = (i32_load16_u(var7 + 114) - i32_load16_u(var6 + 114))
            var4 = i32_load16_u(var6 + 112)
            var3 = (i32_load16_u(var7 + 112) - i32_load16_u(var6 + 112))
            var3 = (var14 - var12)
            var3 = (var15 - var4)
            if (1 if (((i32_load16_u(var7 + 114) - i32_load16_u(var6 + 114)) * var3) + ((i32_load16_u(var7 + 112) - i32_load16_u(var6 + 112)) * var3)) <= (((var14 - var12) * var3) + ((var15 - var4) * var3)) else 0):
                break
            if var13:
                break
            var9 = i32_load(9142440)
            var13 = 1
            var3 = (var5 + 2)
            if (1 if var5 < 16558 else 0):
                continue
            break  # end loop
        var4 = 1
        var2 = (1 if var11 > 1 else 0)
        if (1 if var11 > 1 else 0):
            var5 = (var11 if var2 else 1)
            var3 = (var0 * 132)
            while True:  # loop $label10
                if (1 if func225((var1 + 12), (var1 + 8), (i32_load(9671128) + var3), ((i32_load(38984) * 404) + 9568096)) == 0 else 0):
                    break
                var2 = func34(i32_load(38984), i32_load16_u((i32_load(9671128) + var3) + 110), i32_load(var1 + 12), i32_load(var1 + 8), 0, 1)
                if (1 if func34(i32_load(38984), i32_load16_u((i32_load(9671128) + var3) + 110), i32_load(var1 + 12), i32_load(var1 + 8), 0, 1) == 0 else 0):
                    break
                var2 = (i32_load(9671128) + (var2 * 132))
                i64_store((i32_load(9671128) + (var2 * 132)) + 64, 1073741824250)
                i32_store(var2 + 56, var10)
                i32_store(var2 + 52, var8)
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != var5 else 0):
                    continue
                break  # end loop
        var5 = i32_load(9671128)
        var4 = i32_load((i32_load(9671128) + (var0 * 132)) + 80)
    var3 = (var8 * var11)
    if (1 if var4 <= (var8 * var11) else 0):
        break
    var2 = (var0 * 132)
    if (1 if func225((var1 + 12), (var1 + 8), (var5 + (var0 * 132)), ((i32_load(38984) * 404) + 9568096)) == 0 else 0):
        break
    var5 = func34(i32_load(38984), i32_load16_u((i32_load(9671128) + var2) + 110), i32_load(var1 + 12), i32_load(var1 + 8), 0, 1)
    if (1 if func34(i32_load(38984), i32_load16_u((i32_load(9671128) + var2) + 110), i32_load(var1 + 12), i32_load(var1 + 8), 0, 1) == 0 else 0):
        break
    var2 = i32_load(9671128)
    var0 = i32_load((i32_load(9671128) + (var0 * 132)) + 80)
    var2 = (var2 + (var5 * 132))
    i64_store((var2 + (var5 * 132)) + 64, 1073741824250)
    i32_store(var2 + 56, var10)
    i32_store(var2 + 52, (var0 - var3))
    global global0
    global0 = (var1 + 16)

