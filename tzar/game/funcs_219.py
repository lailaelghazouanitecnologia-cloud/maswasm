"""
Auto-generated from WAT. Contains 3 functions.
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
# $func417
# ==========================================================
def func417(var0, var1, var2):
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
    if (1 if var0 == 0 else 0):
        break
    if (1 if var1 == 0 else 0):
        break
    var4 = i32_load(9561692)
    var5 = i32_load16_u((i32_load(9671128) + (i32_load(var1) * 132)) + 110)
    var13 = (i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (i32_load(var1) * 132)) + 110) * 286704))
    var9 = i32_load(var0 + 8)
    var6 = i32_load(var0)
    var0 = i32_load(var0 + 4)
    if (1 if i32_load(var0 + 4) == -1 else 0):
        if (1 if var2 == 0 else 0):
            break
        while True:  # loop $label1
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var2 else 0):
                continue
            break  # end loop
        break
    var17 = (1 if (1 if var0 > 100 else 0) else var0)
    if (1 if (1 if (1 if var0 > 100 else 0) else var0) == 0 else 0):
        break
    if (1 if var2 == 0 else 0):
        break
    var18 = (-2147483647 if var9 else 2147483647)
    var19 = ((var4 + (var5 * 286704)) + 281796)
    while True:  # loop $label12
        var15 = i32_load(9671128)
        var11 = 0
        var5 = 0
        var0 = var18
        while True:  # loop $label11
            var12 = (var15 + (i32_load((var1 + (var11 << 2))) * 132))
            var4 = i32_load8_u((var15 + (i32_load((var1 + (var11 << 2))) * 132)) + 125)
            # br_table ['$label2', '$label3', '$label3', '$label4', '$label3']
            _br_idx = i32_load8_u((var15 + (i32_load((var1 + (var11 << 2))) * 132)) + 125)
            break  # br_table
            if (1 if (var4 & 254) == 6 else 0):
                break
            # br_table ['$label2', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label2', '$label4']
            _br_idx = (var4 - 4)
            break  # br_table
            var3 = i32_load(var19)
            if (1 if i32_load(var19) == 0 else 0):
                break
            var8 = i32_load(var3 + 8)
            if (1 if i32_load(var3 + 8) == 0 else 0):
                break
            var4 = i32_load(var12 + 28)
            var7 = i32_load(var3)
            var3 = 0
            while True:  # loop $label7
                var10 = (var3 << 2)
                if (1 if var4 == i32_load((var7 + (var3 << 2))) else 0):
                    if (1 if i32_load((var7 + (var10 | 4))) == var6 else 0):
                        break
                var3 = (var3 + 2)
                if (1 if var8 > (var3 + 2) else 0):
                    continue
                break
                break  # end loop
            var5 = var4
            break
            var4 = 0
            var3 = i32_load(var12 + 20)
            if (1 if i32_load(var12 + 20) == 0 else 0):
                break
            var7 = i32_load(var3 + 8)
            if (1 if i32_load(var3 + 8) == 0 else 0):
                break
            var8 = i32_load(var3)
            var3 = 0
            if (1 if var7 != 1 else 0):
                var20 = (var7 & -2)
                var10 = 0
                while True:  # loop $label10
                    var21 = (var3 << 2)
                    var16 = i32_load((var8 + (var3 << 2)))
                    var4 = i32_load((var8 + (var21 | 4)))
                    var4 = ((var4 + (1 if ((i32_load((var8 + (var3 << 2))) - 2147483647) if (1 if var16 > 2147483646 else 0) else var16) == var6 else 0)) + (1 if ((i32_load((var8 + (var21 | 4))) - 2147483647) if (1 if var4 > 2147483646 else 0) else var4) == var6 else 0))
                    var3 = (var3 + 2)
                    var10 = (var10 + 2)
                    if (1 if (var10 + 2) != var20 else 0):
                        continue
                    break  # end loop
            if (1 if (var7 & 1) == 0 else 0):
                break
            var3 = i32_load((var8 + (var3 << 2)))
            var4 = (var4 + (1 if ((i32_load((var8 + (var3 << 2))) - 2147483647) if (1 if var3 > 2147483646 else 0) else var3) == var6 else 0))
            if ((1 if var0 >= var4 else 0) if var9 else (1 if var0 <= var4 else 0)):
                break
            var5 = i32_load(var12 + 28)
            var0 = var4
            var11 = (var11 + 1)
            if (1 if (var11 + 1) != var2 else 0):
                continue
            break  # end loop
        if (1 if var5 == 0 else 0):
            break
        var14 = (var14 + 1)
        if (1 if (var14 + 1) != var17 else 0):
            continue
        break  # end loop


# ==========================================================
# $func470
# ==========================================================
def func470(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var7 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var2 = i32_load(9671128)
    var1 = (i32_load(9671128) + (var0 * 132))
    var5 = i32_load16_u(var1 + 116)
    var6 = i32_load16_u(var1 + 118)
    var3 = i32_load(9142840)
    var1 = (i32_load(9142440) + 2)
    var4 = (var6 + (i32_load(9142440) + 2))
    if (1 if i32_load((i32_load(9142840) + ((var5 + (((var6 + (i32_load(9142440) + 2)) + 1) * var1)) << 2)) + 4) != 1 else 0):
        break
    if (1 if i32_load((((var5 + ((var4 + 3) * var1)) << 2) + var3) + 12) != 1 else 0):
        break
    var1 = 0
    var3 = (i32_load(9561692) + (i32_load16_u((var2 + (var0 * 132)) + 110) * 286704))
    var2 = (i32_load(((i32_load(9561692) + (i32_load16_u((var2 + (var0 * 132)) + 110) * 286704)) + 284192)) << 2)
    var3 = i32_load((var3 + 284196))
    if (1 if (i32_load(((i32_load(9561692) + (i32_load16_u((var2 + (var0 * 132)) + 110) * 286704)) + 284192)) << 2) <= i32_load((var3 + 284196)) else 0):
        var4 = ((var3 & 0xFFFFFFFF) // var2)
        var4 = (1 if (1 if var4 <= 1 else 0) else ((var3 & 0xFFFFFFFF) // var2))
        var8 = ((var6 << 16) | var5)
        while True:  # loop $label1
            var1 = (var1 + 1)
            if (1 if var1 != var4 else 0):
                continue
            break  # end loop
    var1 = 0
    if i32_load8_u(9142917):
        break
    var0 = i32_load(9299880)
    if i32_load(9299880):
        var0 = (var0 - 1)
        i32_store(9299880, (var0 - 1))
        var1 = i32_load((i32_load(9299872) + (var0 << 2)))
        break
    var1 = i32_load(9163776)
    var0 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var2 = i32_load(9163784)
    if (1 if var0 < i32_load(9163784) else 0):
        break
    i32_store(var7, var2)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    # Unknown: f64.convert_i32_u []
    global global0
    global0 = (var7 + 16)


# ==========================================================
# $func516
# ==========================================================
def func516(var0, var1):
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
    var12 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if i32_load8_u(var1 + 125) == 3 else 0):
        break
    # br_table ['$label1', '$label2', '$label3', '$label4', '$label0']
    _br_idx = i32_load(var0 + 8)
    break  # br_table
    var5 = i32_load(var0 + 20)
    var6 = i32_load(var0 + 28)
    var4 = i32_load(var0 + 24)
    var8 = i32_load(var0 + 40)
    var0 = i32_load(9147324)
    i32_store(9147324, i32_load(9147316))
    var3 = i32_load(9147320)
    var2 = i32_load(9147312)
    i32_store(9147320, i32_load(9147312))
    var0 = (var0 ^ (var0 << 11))
    var2 = ((var2 ^ (((var2 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0)
    i32_store(9147316, ((var2 ^ (((var2 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0))
    var0 = (var3 ^ (var3 << 11))
    var0 = ((((((var3 ^ (var3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var2)
    i32_store(9147312, ((((((var3 ^ (var3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var2))
    var0 = (var4 + (var0 % var8))
    break
    var2 = i32_load(var0 + 36)
    i64_store(var12 + 8, i64_load(var0 + 72))
    i64_store(var12, i64_load(var0 + 64))
    var4 = func300(var2, var12, var1)
    break
    var5 = i32_load(var0 + 104)
    if (1 if i32_load(var0 + 104) == 0 else 0):
        break
    var6 = i32_load(var0 + 96)
    var8 = i32_load16_u(var1 + 114)
    var9 = i32_load16_u(var1 + 112)
    var11 = i32_load(9671128)
    var7 = i32_load(var1 + 28)
    var2 = 2147483647
    var0 = 0
    while True:  # loop $label7
        var3 = i32_load((var6 + (var0 << 2)))
        if (1 if var7 != i32_load((var6 + (var0 << 2))) else 0):
            var3 = (var11 + (var3 * 132))
            var10 = ((i32_load16_u((var11 + (var3 * 132)) + 114) - var8) << 1)
            var10 = ((i32_load16_u(var3 + 112) - var9) << 1)
            var10 = ((((i32_load16_u((var11 + (var3 * 132)) + 114) - var8) << 1) * var10) + (((i32_load16_u(var3 + 112) - var9) << 1) * var10))
            var10 = (1 if var2 > var10 else 0)
            var2 = (((((i32_load16_u((var11 + (var3 * 132)) + 114) - var8) << 1) * var10) + (((i32_load16_u(var3 + 112) - var9) << 1) * var10)) if (1 if var2 > var10 else 0) else var2)
            var4 = (i32_load(var3 + 28) if var10 else var4)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var5 else 0):
            continue
        break  # end loop
    break
    var5 = i32_load(9140300)
    if (1 if i32_load(9140300) == 0 else 0):
        break
    var6 = i32_load16_u(var1 + 114)
    var8 = i32_load16_u(var1 + 112)
    var9 = i32_load(9671128)
    var11 = i32_load(var1 + 28)
    var2 = 2147483647
    var0 = 0
    while True:  # loop $label8
        var3 = i32_load(((var0 << 2) + 8451904))
        if (1 if var11 != i32_load(((var0 << 2) + 8451904)) else 0):
            var3 = (var9 + (var3 * 132))
            var7 = ((i32_load16_u((var9 + (var3 * 132)) + 114) - var6) << 1)
            var7 = ((i32_load16_u(var3 + 112) - var8) << 1)
            var7 = ((((i32_load16_u((var9 + (var3 * 132)) + 114) - var6) << 1) * var7) + (((i32_load16_u(var3 + 112) - var8) << 1) * var7))
            var7 = (1 if var2 > var7 else 0)
            var2 = (((((i32_load16_u((var9 + (var3 * 132)) + 114) - var6) << 1) * var7) + (((i32_load16_u(var3 + 112) - var8) << 1) * var7)) if (1 if var2 > var7 else 0) else var2)
            var4 = (i32_load(var3 + 28) if var7 else var4)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var5 else 0):
            continue
        break  # end loop
    if (1 if var4 == 0 else 0):
        break
    var2 = (i32_load(9671128) + (var4 * 132))
    var0 = i32_load16_u((i32_load(9671128) + (var4 * 132)) + 114)
    var5 = i32_load16_u(var2 + 112)
    var8 = ((i32_load8_u(var1 + 122) * 404) + 9568096)
    var9 = i32_load16_u(var1 + 110)
    if func56(i32_load16_u(var2 + 112), var0, ((i32_load8_u(var1 + 122) * 404) + 9568096), i32_load16_u(var1 + 110), 0, 0, 1, 1, 0):
        var2 = var5
        var3 = var0
        break
    var4 = i32_load(9142440)
    var2 = 0
    while True:  # loop $label11
        var6 = var2
        var2 = (var2 << 2)
        var3 = (i32_load((((var2 << 2) | 4) + 8611904)) + var0)
        if (1 if var4 <= (i32_load((((var2 << 2) | 4) + 8611904)) + var0) else 0):
            break
        var2 = (i32_load((var2 + 8611904)) + var5)
        if (1 if var4 <= (i32_load((var2 + 8611904)) + var5) else 0):
            break
        if (1 if (var2 | var3) < 0 else 0):
            break
        if func56(var2, var3, var8, var9, 0, 0, 1, 1, 0):
            break
        var4 = i32_load(9142440)
        var2 = (var6 + 2)
        if (1 if var6 < 5198 else 0):
            continue
        break  # end loop
    break
    var0 = i32_load(var1 + 20)
    if i32_load(var1 + 20):
        i32_store(var0 + 8, 0)
    i32_store(var1 + 32, 0)
    i32_store8(var1 + 129, 0)
    if i32_load(var1 + 36):
    var5 = i32_load8_u(var1 + 125)
    if (1 if i32_load8_u(var1 + 125) == 13 else 0):
        break
    if (1 if i32_load8_u(59181) == 0 else 0):
        break
    var0 = i32_load(var1 + 44)
    if (1 if i32_load(var1 + 44) == 0 else 0):
        break
    var6 = i32_load(9215884)
    if (1 if i32_load((i32_load(9215884) + (var0 << 4)) + 12) == 1 else 0):
        break
    if (1 if var5 == 7 else 0):
        break
    if i32_load((var6 + ((var0 << 4) | 4))):
        break
    var0 = (i32_load8_u(var1 + 124) << 3)
    var0 = i32_load(var1 + 44)
    if i32_load(var1 + 44):
        i32_store((i32_load(9215884) + (var0 << 4)), 0)
    i32_store(var1 + 44, 0)
    if (1 if i32_load8_u(var1 + 125) == 13 else 0):
        i32_store16(var1 + 114, var3)
        i32_store16(var1 + 112, var2)
        break
    var5 = ((i32_load8_u(var1 + 122) * 404) + 9568096)
    if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 216):
        var4 = i32_load(9142840)
        var8 = i32_load16_u(var1 + 114)
        var9 = i32_load16_u(var1 + 112)
        var6 = 0
        while True:  # loop $label14
            var6 = (var6 + 1)
            var11 = ((var6 + 1) + var9)
            var0 = 0
            while True:  # loop $label13
                var0 = (var0 + 1)
                var7 = (i32_load(9142440) + 2)
                i32_store((var4 + ((var11 + ((((var0 + 1) + var8) + ((i32_load(9142440) + 2) * i32_load(var5 + 208))) * var7)) << 2)), i32_load(var5 + 212))
                var7 = i32_load(var5 + 216)
                if (1 if var0 < i32_load(var5 + 216) else 0):
                    continue
                break  # end loop
            if (1 if var6 < var7 else 0):
                continue
            break  # end loop
    i32_store16(var1 + 114, var3)
    i32_store16(var1 + 112, var2)
    if (1 if i32_load8_u(var1 + 125) == 13 else 0):
        break
    var5 = ((i32_load8_u(var1 + 122) * 404) + 9568096)
    if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 216):
        var3 = (var3 & 65535)
        var6 = (var2 & 65535)
        var4 = i32_load(9142840)
        var2 = 0
        while True:  # loop $label16
            var2 = (var2 + 1)
            var8 = ((var2 + 1) + var6)
            var0 = 0
            while True:  # loop $label15
                var0 = (var0 + 1)
                var9 = (i32_load(9142440) + 2)
                i32_store((var4 + ((var8 + ((((var0 + 1) + var3) + ((i32_load(9142440) + 2) * i32_load(var5 + 208))) * var9)) << 2)), i32_load(var1 + 28))
                var9 = i32_load(var5 + 216)
                if (1 if var0 < i32_load(var5 + 216) else 0):
                    continue
                break  # end loop
            if (1 if var2 < var9 else 0):
                continue
            break  # end loop
    func118(var1)
    func92(var1, 0.0, 0.0)
    func29(var1, 1)
    global global0
    global0 = (var12 + 16)
    return func60(var1, 1.0)

