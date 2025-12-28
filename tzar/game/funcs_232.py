"""
Auto-generated from WAT. Contains 5 functions.
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
# $func403
# ==========================================================
def func403(var0):
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
    var4 = i32_load(9142440)
    var5 = (i32_load(9142440) + 2)
    var9 = i32_load(9215884)
    var6 = i32_load(var0 + 28)
    var7 = i32_load(9671128)
    var10 = i32_load(9142840)
    var11 = i32_load16_u(var0 + 114)
    var12 = i32_load16_u(var0 + 112)
    var13 = i32_load16_u(var0 + 110)
    while True:  # loop $label4
        var8 = var1
        var2 = (var1 << 2)
        var1 = (i32_load((((var1 << 2) | 4) + 8611904)) + var11)
        if (1 if var4 <= (i32_load((((var1 << 2) | 4) + 8611904)) + var11) else 0):
            break
        var2 = (i32_load((var2 + 8611904)) + var12)
        if (1 if var4 <= (i32_load((var2 + 8611904)) + var12) else 0):
            break
        if (1 if (var1 | var2) < 0 else 0):
            break
        var2 = i32_load((((var2 + (((var1 + var5) + 1) * var5)) << 2) + var10) + 4)
        var1 = (var7 + (i32_load((((var2 + (((var1 + var5) + 1) * var5)) << 2) + var10) + 4) * 132))
        var3 = i32_load8_u((var7 + (i32_load((((var2 + (((var1 + var5) + 1) * var5)) << 2) + var10) + 4) * 132)) + 122)
        # br_table ['$label1', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label1', '$label2']
        _br_idx = (i32_load8_u((var7 + (i32_load((((var2 + (((var1 + var5) + 1) * var5)) << 2) + var10) + 4) * 132)) + 122) + -64)
        break  # br_table
        if (1 if var3 != 10 else 0):
            break
        if (1 if i32_load16_u(var1 + 110) != var13 else 0):
            break
        if (1 if i32_load(var1 + 32) == var6 else 0):
            break
        if (1 if i32_load8_u(var1 + 129) != 10 else 0):
            break
        var3 = i32_load(var1 + 44)
        if (1 if ((1 if i32_load((var9 + (i32_load(var1 + 44) << 4)) + 4) == 22 else 0) | (1 if var3 == 0 else 0)) == 0 else 0):
            break
        if i32_load8_u(var1 + 125):
            break
        if i32_load(var1 + 36):
            break
        var1 = (var7 + (var2 * 132))
        i32_store(var0 + 96, i32_load(var1 + 28))
        return
        var1 = (var8 + 2)
        if (1 if var8 < 2734 else 0):
            continue
        break  # end loop


# ==========================================================
# $func404
# ==========================================================
def func404(var0):
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
    var20 = 0
    var13 = i32_load(9671128)
    var1 = (i32_load(9671128) + (var0 * 132))
    i32_store8((i32_load(9671128) + (var0 * 132)) + 129, 10)
    var5 = i32_load(9142440)
    var14 = (i32_load(9142440) + 2)
    var16 = i32_load(38984)
    var17 = ((i32_load(9142440) + 2) * i32_load(((i32_load(38984) * 404) + 9568096) + 208))
    var9 = i32_load16_u(var1 + 112)
    var18 = (i32_load16_u(var1 + 112) + 29)
    var10 = i32_load16_u(var1 + 114)
    var19 = (i32_load16_u(var1 + 114) + 29)
    var11 = (var10 - 30)
    var2 = (var9 - 30)
    var8 = i32_load(9671128)
    var15 = i32_load(9142840)
    var6 = 2147483647
    while True:  # loop $label2
        var3 = (var2 + 1)
        if (1 if var2 < var5 else 0):
            var1 = (var9 - var2)
            var20 = ((var9 - var2) * var1)
            var1 = var11
            while True:  # loop $label1
                var4 = var1
                if (1 if var5 <= var1 else 0):
                    break
                if (1 if (var2 | var4) < 0 else 0):
                    break
                var1 = (var10 - var4)
                var12 = (((var10 - var4) * var1) + var20)
                if (1 if (((var10 - var4) * var1) + var20) >= var6 else 0):
                    break
                var1 = i32_load((var15 + (((((var4 + var17) + 1) * var14) + var3) << 2)))
                if (1 if i32_load((var15 + (((((var4 + var17) + 1) * var14) + var3) << 2))) == 0 else 0):
                    break
                var12 = (1 if var16 == i32_load8_u((var8 + (var1 * 132)) + 122) else 0)
                var6 = (var12 if (1 if var16 == i32_load8_u((var8 + (var1 * 132)) + 122) else 0) else var6)
                var7 = (var1 if var12 else var7)
                var1 = (var4 + 1)
                if (1 if var4 != var19 else 0):
                    continue
                break  # end loop
        var1 = (1 if var2 != var18 else 0)
        var2 = var3
        if var1:
            continue
        break  # end loop
    var4 = (var13 + (var0 * 132))
    if var7:
        return
    var11 = (var5 + 3)
    var6 = i32_load(38528)
    var7 = i32_load16_u((var13 + (var0 * 132)) + 110)
    var1 = 0
    while True:  # loop $label5
        var2 = var1
        var3 = (var1 << 2)
        var1 = (i32_load((((var1 << 2) | 4) + 8611904)) + var10)
        if (1 if var5 <= (i32_load((((var1 << 2) | 4) + 8611904)) + var10) else 0):
            break
        var3 = (i32_load((var3 + 8611904)) + var9)
        if (1 if var5 <= (i32_load((var3 + 8611904)) + var9) else 0):
            break
        if (1 if (var1 | var3) < 0 else 0):
            break
        var3 = i32_load((((var3 + ((var1 + var11) * var14)) << 2) + var15) + 4)
        var1 = (var8 + (i32_load((((var3 + ((var1 + var11) * var14)) << 2) + var15) + 4) * 132))
        if (1 if var6 != i32_load8_u((var8 + (i32_load((((var3 + ((var1 + var11) * var14)) << 2) + var15) + 4) * 132)) + 122) else 0):
            break
        if (1 if i32_load(var1 + 72) < 50 else 0):
            break
        if (1 if i32_load8_u(var1 + 125) == 12 else 0):
            break
        if (1 if i32_load16_u(var1 + 110) != var7 else 0):
            break
        if (1 if i32_load(var1 + 96) == 0 else 0):
            break
        var1 = (var2 + 2)
        if (1 if var2 <= 16557 else 0):
            continue
        break
        break  # end loop
    var1 = i32_load((var8 + (var3 * 132)) + 28)
    if (1 if i32_load((var8 + (var3 * 132)) + 28) == 0 else 0):
        break
    i32_store((var8 + (var1 * 132)) + 96, var0)
    return
    func29(var4, 1)


# ==========================================================
# $func476
# ==========================================================
def func476(var0, var1):
    var2 = 0
    var3 = 0
    var2 = i32_load(9671128)
    var1 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var1 + 129) != 7 else 0):
        break
    var0 = (var2 + (var0 * 132))
    var2 = i32_load((var2 + (var0 * 132)) + 88)
    if (1 if i32_load((var2 + (var0 * 132)) + 88) == 0 else 0):
        break
    var3 = i32_load(9142440)
    i32_store(var0 + 80, 0)
    i32_store(var0 + 88, 0)
    i32_store8(var1 + 129, 0)
    var0 = ((var2 & 0xFFFFFFFF) // var3)


# ==========================================================
# $func488
# ==========================================================
def func488(var0, var1):
    var0 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 129) == 7 else 0):
        i32_store8(var0 + 129, 0)
    func202(var0, 0, 0)
    func29(var0, 1)


# ==========================================================
# $func495
# ==========================================================
def func495(var0, var1, param2):
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
    var9 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var4 = i32_load(9671128)
    if (1 if i32_load(9142848) < (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        func29((var4 + (var0 * 132)), 1)
        break
    var3 = (var0 * 132)
    var2 = (var4 + (var0 * 132))
    if (1 if i32_load8_u((var4 + (var0 * 132)) + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var2 + 128) == 0 else 0):
        break
    var4 = (var4 + (var0 * 132))
    i32_store8((var4 + (var0 * 132)) + 127, 0)
    var5 = i32_load(var4 + 40)
    if (1 if i32_load(var4 + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var9 + 20, var5)
        i32_store(var9 + 16, 0)
        a_b()
        break
    var4 = i32_load16_u(var4 + 110)
    i32_store(var9 + 4, var5)
    i32_store(var9, (var4 + 16))
    a_b()
    i32_store8(var2 + 128, 0)
    var4 = i32_load(9671128)
    var10 = (var3 + var4)
    var2 = (var4 + (var1 * 132))
    if (1 if i32_load8_u((var4 + (var1 * 132)) + 125) == 3 else 0):
        func29(var10, 1)
        break
    var8 = (var4 + (var1 * 132))
    var5 = i32_load16_u((var4 + (var1 * 132)) + 112)
    var6 = (var4 + (var0 * 132))
    if (1 if i32_load8_u((var4 + (var0 * 132)) + 125) == 1 else 0):
        var3 = i32_load16_u(var6 + 114)
        var2 = i32_load16_u(var8 + 114)
        var8 = i32_load16_u(var6 + 112)
        if (1 if var5 != i32_load16_u(var6 + 112) else 0):
            break
        if (1 if var2 > var3 else 0):
            break
        if (1 if var2 < var3 else 0):
            break
        var8 = 0
        break
        var8 = (1 if (1 if var5 > var8 else 0) else (-1 if (1 if var5 < var8 else 0) else 0))
        var3 = (1 if (1 if var2 > var3 else 0) else (-1 if (1 if var2 < var3 else 0) else 0))
        var7 = 6
        var3 = (((var3 * 3) + var8) + 4)
        if (1 if (((var3 * 3) + var8) + 4) <= 8 else 0):
            var7 = i32_load8_u((var3 + 10184))
        var3 = (var4 + (var0 * 132))
        i32_store8((var4 + (var0 * 132)) + 124, var7)
        if (1 if var0 != var1 else 0):
        var2 = i32_load(((i32_load((i32_load(9215884) + (i32_load(var3 + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if i32_load(((i32_load((i32_load(9215884) + (i32_load(var3 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            # call_indirect via table[var2]
        if (1 if i32_load8_u(var6 + 125) == 3 else 0):
            break
        var5 = i32_load(var3 + 44)
        if i32_load(var3 + 44):
            var10 = i32_load(9142848)
            var2 = i32_load(9215884)
            i32_store((i32_load(9215884) + (var5 << 4)) + 4, 40)
            i32_store((var2 + (i32_load(var3 + 44) << 4)) + 8, i32_load((var4 + (var0 * 132)) + 28))
            i32_store((var2 + (i32_load(var3 + 44) << 4)) + 12, var1)
            i32_store((var2 + (i32_load(var3 + 44) << 4)), (var10 + 28))
            break
        i32_store(var3 + 44, ((Ua(700, 40, i32_load((var4 + (var0 * 132)) + 28), var1) & 0xFFFFFFFF) >> 2))
        i32_store((var4 + (var1 * 132)) + 104, var0)
        break
    var3 = i32_load16_u(var8 + 114)
    var11 = i32_load(i32_load(9142424) + 48)
    if i32_load(i32_load(9142424) + 48):
        if (1 if i32_load8_u(9147152) == 0 else 0):
            break
    var6 = i32_load(9142440)
    break
    var6 = i32_load(9142440)
    var7 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var3) + var5) << 1)))
    if (1 if var11 == 2 else 0):
        if (1 if var7 > 1 else 0):
            break
        break
    if (1 if var7 == 0 else 0):
        break
    func80(float(var5), float(var3), i32_load(9142580), 32.0, float((var6 * 96)))
    var5 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    i32_store8(var2 + 127, 5)
    if (1 if i32_load8_u(9142916) == 0 else 0):
        break
    var3 = i32_load(var2 + 40)
    if (1 if i32_load(var2 + 40) == 0 else 0):
        break
    i32_store(var5 + 20, var3)
    i32_store(var5 + 16, -11842741)
    a_b()
    var3 = i32_load16_u(var2 + 112)
    var6 = ((i32_load16_u(var2 + 112) << 5) - i32_load(9142952))
    var6 = i32_load16_u(var2 + 114)
    var7 = ((i32_load16_u(var2 + 114) << 5) - i32_load(9142956))
    if (1 if (((((i32_load16_u(var2 + 112) << 5) - i32_load(9142952)) * var6) + (((i32_load16_u(var2 + 114) << 5) - i32_load(9142956)) * var7)) - 1) > 9000000 else 0):
        break
    var11 = i32_load(39888)
    var12 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var7 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var6) + var3) << 1)))
    if (1 if var12 == 2 else 0):
        if (1 if var7 > 1 else 0):
            break
        break
    if (1 if var7 == 0 else 0):
        break
    i32_store(var5 + 8, var6)
    i32_store(var5 + 4, var3)
    i32_store(var5, var11)
    a_b()
    func119(var5, var2, 0, 1)
    i32_store8(var2 + 125, 10)
    func63(1738, var2, 20, 0, i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284220)))
    func77(var2)
    global global0
    global0 = (var5 + 32)
    i32_store((var4 + (var1 * 132)) + 104, 0)
    if (1 if var0 == var1 else 0):
        break
    var2 = i32_load8_u((var4 + (var0 * 132)) + 129)
    if (1 if (i32_load8_u((var4 + (var0 * 132)) + 129) & 254) == 14 else 0):
        var0 = func301(i32_load16_u(var8 + 112), i32_load16_u(var8 + 114), i32_load16_u((var4 + (var0 * 132)) + 110), (-1 if (1 if var2 != 15 else 0) else i32_load8_u((var4 + (var1 * 132)) + 122)))
        if func301(i32_load16_u(var8 + 112), i32_load16_u(var8 + 114), i32_load16_u((var4 + (var0 * 132)) + 110), (-1 if (1 if var2 != 15 else 0) else i32_load8_u((var4 + (var1 * 132)) + 122))):
            break
        func29(var10, 1)
        break
    func29(var10, 1)
    global global0
    global0 = (var9 + 32)
    return (var5 + 16)

