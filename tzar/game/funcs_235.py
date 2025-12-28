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
# $func627
# ==========================================================
def func627(var0):
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
    var2 = i32_load(9671128)
    var3 = i32_load(var0 + 32)
    var1 = (i32_load(9671128) + (i32_load(var0 + 32) * 132))
    var5 = i32_load(9561692)
    if (1 if i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 286684) == 0 else 0):
        var6 = i32_load(var1 + 16)
        if (1 if i32_load(var1 + 16) == 0 else 0):
            break
        var2 = (var2 + (var3 * 132))
        var3 = i32_load(((i32_load8_u((var2 + (var3 * 132)) + 122) * 404) + 9568096) + 136)
        if (1 if i32_load(var6 + 8) < ((((i32_load(((i32_load8_u((var2 + (var3 * 132)) + 122) * 404) + 9568096) + 136) * 150) & 0xFFFFFFFF) // 100) if (1 if i32_load((((var5 + (i32_load16_u(var2 + 110) * 286704)) + (i32_load(39216) << 2)) + 281808)) == 1 else 0) else var3) else 0):
            break
        var9 = i32_load16_u(var1 + 110)
        var10 = (((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + (i32_load(39216) << 2)) + 281808)
        var3 = i32_load(9142440)
        var5 = (i32_load(9142440) + 2)
        var11 = i32_load8_u(var1 + 122)
        var6 = ((i32_load8_u(var1 + 122) * 404) + 9568096)
        var7 = i32_load(9671128)
        var12 = i32_load(9142840)
        var13 = i32_load16_u(var1 + 114)
        var14 = i32_load16_u(var1 + 112)
        var1 = 0
        while True:  # loop $label4
            var2 = var1
            var4 = (var1 << 2)
            var1 = (i32_load((((var1 << 2) | 4) + 8611904)) + var13)
            if (1 if var3 <= (i32_load((((var1 << 2) | 4) + 8611904)) + var13) else 0):
                break
            var4 = (i32_load((var4 + 8611904)) + var14)
            if (1 if var3 <= (i32_load((var4 + 8611904)) + var14) else 0):
                break
            if (1 if (var1 | var4) < 0 else 0):
                break
            var4 = i32_load((((var4 + (((var1 + (i32_load(var6 + 208) * var5)) + 1) * var5)) << 2) + var12) + 4)
            var1 = (var7 + (i32_load((((var4 + (((var1 + (i32_load(var6 + 208) * var5)) + 1) * var5)) << 2) + var12) + 4) * 132))
            if (1 if i32_load8_u((var7 + (i32_load((((var4 + (((var1 + (i32_load(var6 + 208) * var5)) + 1) * var5)) << 2) + var12) + 4) * 132)) + 122) != var11 else 0):
                break
            if (1 if i32_load16_u(var1 + 110) != var9 else 0):
                break
            # br_table ['$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label1', '$label2']
            _br_idx = (i32_load8_u(var1 + 125) - 4)
            break  # br_table
            var1 = i32_load(var1 + 16)
            if i32_load(var1 + 16):
                var15 = i32_load(var6 + 136)
                if (1 if i32_load(var1 + 8) >= ((((i32_load(var6 + 136) * 150) & 0xFFFFFFFF) // 100) if (1 if i32_load(var10) == 1 else 0) else var15) else 0):
                    break
            break
            var1 = (var2 + 2)
            if (1 if var2 < 1918 else 0):
                continue
            break  # end loop
        var1 = 0
        if (1 if 0 == 0 else 0):
            break
        i32_store(var0 + 32, var1)
        return 0
    if (1 if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 264) != 4 else 0):
        return 0
    var8 = 1
    var2 = (var2 + (var3 * 132))
    if (1 if i32_load8_u((var2 + (var3 * 132)) + 123) == 38 else 0):
        break
    if i32_load8_u(var2 + 125):
        return 0
    var8 = 0
    if (1 if i32_load8_u(var2 + 129) == 7 else 0):
        break
    return var8


# ==========================================================
# $func632
# ==========================================================
def func632(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var1 = i32_load(9671128)
    var2 = (i32_load(9671128) + (var0 * 132))
    var3 = i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125)
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 3 else 0):
        break
    if i32_load16_u(var2 + 110):
        break
    var4 = (var1 + (var0 * 132))
    if (1 if var3 > 1 else 0):
        break
    if i32_load8_u(var4 + 123):
        break
    var0 = (var1 + (var0 * 132))
    var5 = i32_load16_u((var1 + (var0 * 132)) + 112)
    var6 = i32_load16_u(var0 + 114)
    var0 = i32_load(9147324)
    i32_store(9147324, i32_load(9147316))
    var1 = i32_load(9147320)
    var3 = i32_load(9147312)
    i32_store(9147320, i32_load(9147312))
    var0 = (var0 ^ (var0 << 11))
    var0 = ((var3 ^ (((var3 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0)
    i32_store(9147316, ((var3 ^ (((var3 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0))
    var1 = (var1 ^ (var1 << 11))
    var1 = ((((((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var0 & 0xFFFFFFFF) >> 19)) ^ var1) ^ var0)
    i32_store(9147312, ((((((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var0 & 0xFFFFFFFF) >> 19)) ^ var1) ^ var0))
    var2 = ((var5 + (var0 % 21)) - 10)
    var0 = i32_load(9142440)
    var3 = (i32_load(9142440) - 1)
    var2 = (((var5 + (var0 % 21)) - 10) if (1 if var0 > var2 else 0) else (i32_load(9142440) - 1))
    var1 = ((var6 + (var1 % 21)) - 10)
    var0 = (((var6 + (var1 % 21)) - 10) if (1 if var0 > var1 else 0) else var3)
    var7 = i64_load(9147316)
    var0 = i32_load(9147312)
    i32_store(9147316, i32_load(9147312))
    var1 = i32_load(9147324)
    i64_store(9147320, var7)
    var1 = (var1 ^ (var1 << 11))
    var0 = ((var0 ^ (((var0 & 0xFFFFFFFF) >> 19) ^ (((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8))) ^ var1)
    i32_store(9147312, ((var0 ^ (((var0 & 0xFFFFFFFF) >> 19) ^ (((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8))) ^ var1))


# ==========================================================
# $func635
# ==========================================================
def func635(var0, var1):
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
    var5 = i32_load(9671128)
    var7 = (i32_load(9671128) + (var0 * 132))
    if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 128):
        break
    var1 = i32_load8_u(var7 + 125)
    if ((1 if i32_load8_u(var7 + 125) <= 14 else 0) if ((1 << var1) & 16408) else 0):
        break
    var1 = -1
    var10 = func106(var7, -1, -1, -1)
    if (1 if func106(var7, -1, -1, -1) == 0 else 0):
        break
    var14 = (var5 + (var0 * 132))
    if (1 if i32_load8_u((var5 + (var0 * 132)) + 129) == 6 else 0):
        break
    var1 = 5
    if (1 if i32_load(((i32_load8_u(var14 + 122) * 404) + 9568096) + 264) == 1 else 0):
        break
    var2 = (i32_load(9671128) + (var10 * 132))
    var19 = ((i32_load(9671128) + (var10 * 132)) - -64)
    var11 = (var5 + (var0 * 132))
    var5 = i32_load16_u((var5 + (var0 * 132)) + 114)
    var20 = (i32_load16_u((var5 + (var0 * 132)) + 114) + 9)
    var1 = i32_load16_u(var11 + 112)
    var21 = (i32_load16_u(var11 + 112) + 9)
    var5 = (var5 - 5)
    var6 = (var1 - 5)
    while True:  # loop $label7
        var15 = (var6 + 1)
        var1 = var5
        while True:  # loop $label6
            var4 = (var6 - i32_load16_u(var11 + 112))
            var4 = var1
            var1 = (var1 - i32_load16_u(var11 + 114))
            if (1 if ((((var6 - i32_load16_u(var11 + 112)) * var4) + ((var1 - i32_load16_u(var11 + 114)) * var1)) - 1) > 25 else 0):
                break
            var12 = i32_load(9142440)
            if (1 if i32_load(9142440) <= var4 else 0):
                break
            if (1 if (var4 | var6) < 0 else 0):
                break
            if (1 if var6 >= var12 else 0):
                break
            var22 = (var4 + 1)
            var1 = 0
            var16 = i32_load(9142840)
            while True:  # loop $label5
                var3 = (var12 + 2)
                var3 = i32_load((var16 + ((var15 + ((var22 + ((var12 + 2) * var1)) * var3)) << 2)))
                if (1 if i32_load((var16 + ((var15 + ((var22 + ((var12 + 2) * var1)) * var3)) << 2))) < 3 else 0):
                    break
                if (1 if var0 == var3 else 0):
                    break
                var8 = i32_load8_u(var2 + 122)
                if (1 if i32_load8_u(var2 + 122) == i32_load(38500) else 0):
                    break
                var13 = i32_load16_u(var2 + 110)
                var9 = (i32_load(9671128) + (var3 * 132))
                var17 = (i32_load(9142892) * i32_load16_u((i32_load(9671128) + (var3 * 132)) + 110))
                var18 = i32_load(9143004)
                var3 = i32_load16_u(var2 + 120)
                if i32_load16_u(var2 + 120):
                else:
                if (1 if i32_load8_u(((var3 if i32_load8_u((var18 + (var13 + var17))) else var13) + (var13 + var17))) == 0 else 0):
                    if (1 if i32_load8_u(var2 + 127) != 6 else 0):
                        break
                    if (1 if i32_load8_u(var2 + 128) == 0 else 0):
                        break
                    break
                if i32_load8_u(var2 + 128):
                    break
                if (1 if i32_load8_u(var2 + 125) == 10 else 0):
                    break
                if (1 if i32_load8_u(var2 + 126) == 2 else 0):
                    break
                if (1 if i32_load(var19) == -1 else 0):
                    break
                var3 = ((var8 * 404) + 9568096)
                if (1 if i32_load(((var8 * 404) + 9568096) + 264) == 2 else 0):
                    break
                if (1 if i32_load(var3 + 188) != 55 else 0):
                    break
                if (1 if i32_load(38560) == var8 else 0):
                    break
                if (1 if i32_load(38620) == var8 else 0):
                    break
                if (1 if i32_load(38564) == var8 else 0):
                    break
                if (1 if i32_load((i32_load(9215884) + (i32_load(var9 + 44) << 4)) + 4) != 22 else 0):
                    break
                if (1 if i32_load8_u(var9 + 129) == 6 else 0):
                    break
                if i32_load8_u(var9 + 128):
                    break
                var16 = i32_load(9142840)
                var12 = i32_load(9142440)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != 3 else 0):
                    continue
                break  # end loop
            var1 = (var4 + 1)
            if (1 if var4 != var20 else 0):
                continue
            break  # end loop
        var1 = (1 if var6 == var21 else 0)
        var6 = var15
        if (1 if var1 == 0 else 0):
            continue
        break  # end loop
    var1 = (-1 if (1 if i32_load8_u(var14 + 129) == 6 else 0) else 5)
    return
    i32_store((i32_load(9215884) + (i32_load(var7 + 44) << 4)), (i32_load(9142848) + (80 if i32_load8_u(9216060) else 40)))
    return 0  # Stack underflow


# ==========================================================
# $func638
# ==========================================================
def func638(var0, var1, param2):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var4 = i32_load(9671128)
    var1 = (i32_load(9671128) + (var0 * 132))
    var3 = i32_load((i32_load(9671128) + (var0 * 132)) + 20)
    if (1 if i32_load((i32_load(9671128) + (var0 * 132)) + 20) == 0 else 0):
        break
    if (1 if i32_load(var3 + 8) < 5 else 0):
        break
    var2 = i32_load(i32_load(var3) + 16)
    if (1 if i32_load8_u(var1 + 125) == 1 else 0):
        var2 = (var4 + (var0 * 132))
        var3 = i32_load(((i32_load((i32_load(9215884) + (i32_load((var4 + (var0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if i32_load(((i32_load((i32_load(9215884) + (i32_load((var4 + (var0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32):
            # call_indirect via table[var3]
        if (1 if i32_load8_u(var1 + 125) == 3 else 0):
            break
        var3 = i32_load(var2 + 44)
        if i32_load(var2 + 44):
            var5 = i32_load(9142848)
            var1 = i32_load(9215884)
            i32_store((i32_load(9215884) + (var3 << 4)) + 4, 69)
            i32_store((var1 + (i32_load(var2 + 44) << 4)) + 8, i32_load((var4 + (var0 * 132)) + 28))
            i32_store((var1 + (i32_load(var2 + 44) << 4)) + 12, var0)
            i32_store((var1 + (i32_load(var2 + 44) << 4)), (var5 + 40))
            return
        i32_store(var2 + 44, ((Ua(1000, 69, i32_load((var4 + (var0 * 132)) + 28), var0) & 0xFFFFFFFF) >> 2))
        return
    var3 = (var4 + (var2 * 132))
    var5 = func106(var1, -1, i32_load16_u((var4 + (var2 * 132)) + 112), i32_load16_u(var3 + 114))
    if func106(var1, -1, i32_load16_u((var4 + (var2 * 132)) + 112), i32_load16_u(var3 + 114)):
    var5 = (var4 + (var0 * 132))
    var6 = (i32_load16_u((var4 + (var0 * 132)) + 112) - i32_load16_u(var3 + 112))
    var3 = (i32_load16_u(var5 + 114) - i32_load16_u(var3 + 114))
    if (1 if ((((i32_load16_u((var4 + (var0 * 132)) + 112) - i32_load16_u(var3 + 112)) * var6) + ((i32_load16_u(var5 + 114) - i32_load16_u(var3 + 114)) * var3)) - 1) >= 26 else 0):
        return
    if (1 if i32_load8_u((var4 + (var2 * 132)) + 125) == 3 else 0):
        var0 = i32_load(var1 + 20)
        var4 = func236(var1, (var4 + (var2 * 132)))
        if func236(var1, (var4 + (var2 * 132))):
            if (1 if var0 == 0 else 0):
                break
            if (1 if i32_load(var0 + 8) < 5 else 0):
                break
            i32_store(i32_load(var0) + 16, var4)
            return
        i32_store(var0 + 8, 0)
        func29(var1, 1)
        return
    i32_store((i32_load(9215884) + (i32_load((var4 + (var0 * 132)) + 44) << 4)), (i32_load(9142848) + 40))

