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
# $func435
# ==========================================================
def func435(var0, var1):
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
    var22 = 0.0
    var23 = 0.0
    var24 = 0.0
    var11 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var17 = i32_reinterpret_f32(var0)
    var3 = (i32_reinterpret_f32(var0) & 2147483647)
    if (1 if (i32_reinterpret_f32(var0) & 2147483647) <= 1305022426 else 0):
        var23 = float(var0)
        var22 = (((var23 * 0.6366197723675814) + 6755399441055744.0) + -6755399441055744.0)
        var24 = ((float(var0) + ((((var23 * 0.6366197723675814) + 6755399441055744.0) + -6755399441055744.0) * -1.5707963109016418)) + (var22 * -1.5893254773528196e-08))
        f64_store(var1, ((float(var0) + ((((var23 * 0.6366197723675814) + 6755399441055744.0) + -6755399441055744.0) * -1.5707963109016418)) + (var22 * -1.5893254773528196e-08)))
        var2 = (1 if var24 < -0.7853981852531433 else 0)
        if (1 if abs(var22) < 2147483648.0 else 0):
            break
        var3 = -2147483648
        if var2:
            var22 = (var22 + -1.0)
            f64_store(var1, ((var23 + ((var22 + -1.0) * -1.5707963109016418)) + (var22 * -1.5893254773528196e-08)))
            var3 = (var3 - 1)
            break
        if (1 if (1 if var24 > 0.7853981852531433 else 0) == 0 else 0):
            break
        var22 = (var22 + 1.0)
        f64_store(var1, ((var23 + ((var22 + 1.0) * -1.5707963109016418)) + (var22 * -1.5893254773528196e-08)))
        var3 = (var3 + 1)
        break
    if (1 if var3 >= 2139095040 else 0):
        f64_store(var1, float((var0 - var0)))
        var3 = 0
        break
    var3 = (((var3 & 0xFFFFFFFF) >> 23) - 150)
    f64_store(var11 + 8, float(f32_reinterpret_i32((var3 - ((((var3 & 0xFFFFFFFF) >> 23) - 150) << 23)))))
    var14 = (var11 + 8)
    var5 = (global0 - 560)
    global global0
    global0 = (global0 - 560)
    var2 = ((var3 - 3) // 24)
    var13 = (((var3 - 3) // 24) if (1 if var2 > 0 else 0) else 0)
    var6 = (var3 + ((((var3 - 3) // 24) if (1 if var2 > 0 else 0) else 0) * -24))
    var7 = i32_load(28928)
    if (1 if i32_load(28928) >= 0 else 0):
        var3 = (var7 + 1)
        var2 = var13
        while True:  # loop $label2
            if (1 if var2 < 0 else 0):
            else:
            f64_store(0.0, float(i32_load(((var2 << 2) + 28944))))
            var2 = (var2 + 1)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var3 else 0):
                continue
            break  # end loop
    var8 = (var6 - 24)
    var3 = 0
    var4 = (var7 if (1 if var7 > 0 else 0) else 0)
    while True:  # loop $label4
        var2 = 0
        var22 = 0.0
        while True:  # loop $label3
            var22 = ((f64_load((var14 + (var2 << 3))) * f64_load(((var5 + 320) + ((var3 - var2) << 3)))) + var22)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != 1 else 0):
                continue
            break  # end loop
        f64_store((var5 + (var3 << 3)), var22)
        var2 = (1 if var3 == var4 else 0)
        var3 = (var3 + 1)
        if (1 if var2 == 0 else 0):
            continue
        break  # end loop
    var18 = (47 - var6)
    var15 = (48 - var6)
    var19 = (var6 - 25)
    var3 = var7
    while True:  # loop $label26
        var22 = f64_load((var5 + (var3 << 3)))
        var2 = 0
        var4 = var3
        var9 = (1 if var3 <= 0 else 0)
        if (1 if (1 if var3 <= 0 else 0) == 0 else 0):
            while True:  # loop $label7
                var23 = (var22 * 5.960464477539063e-08)
                if (1 if abs((var22 * 5.960464477539063e-08)) < 2147483648.0 else 0):
                    break
                var23 = float(-2147483648)
                var22 = ((float(-2147483648) * -16777216.0) + var22)
                if (1 if abs(((float(-2147483648) * -16777216.0) + var22)) < 2147483648.0 else 0):
                    break
                i32_store(int(var22), -2147483648)
                var4 = (var4 - 1)
                var22 = (f64_load((var5 + ((var4 - 1) << 3))) + var23)
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != var3 else 0):
                    continue
                break  # end loop
        var22 = func168(var22, var8)
        var22 = (func168(var22, var8) + (math.floor((var22 * 0.125)) * -8.0))
        if (1 if abs((func168(var22, var8) + (math.floor((var22 * 0.125)) * -8.0))) < 2147483648.0 else 0):
            break
        var10 = -2147483648
        var22 = (var22 - float(var10))
        var20 = (1 if var8 <= 0 else 0)
        if (1 if (1 if var8 <= 0 else 0) == 0 else 0):
            var2 = ((var3 << 2) + var5)
            var2 = i32_load(var2 + 476)
            var2 = (var2 >> var15)
            var4 = (i32_load(var2 + 476) - ((var2 >> var15) << var15))
            i32_store(((var3 << 2) + var5) + 476, (i32_load(var2 + 476) - ((var2 >> var15) << var15)))
            var10 = (var2 + var10)
            break
        if var8:
            break
        var12 = (i32_load(((var3 << 2) + var5) + 476) >> 23)
        if (1 if (i32_load(((var3 << 2) + var5) + 476) >> 23) <= 0 else 0):
            break
        break
        var12 = 2
        if (1 if var22 >= 0.5 else 0):
            break
        var12 = 0
        break
        var2 = 0
        var4 = 0
        if (1 if var9 == 0 else 0):
            while True:  # loop $label15
                var21 = ((var5 + 480) + (var2 << 2))
                var9 = i32_load(((var5 + 480) + (var2 << 2)))
                var16 = 16777215
                if var4:
                    break
                var16 = 16777216
                if var9:
                    break
                break
                i32_store(var21, (var16 - var9))
                var4 = 1
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != var3 else 0):
                    continue
                break  # end loop
        if var20:
            break
        var2 = 8388607
        # br_table ['$label17', '$label18', '$label16']
        _br_idx = var19
        break  # br_table
        var2 = 4194303
        var9 = ((var3 << 2) + var5)
        i32_store(((var3 << 2) + var5) + 476, (i32_load(var9 + 476) & var2))
        var10 = (var10 + 1)
        if (1 if var12 != 2 else 0):
            break
        var22 = (1.0 - var22)
        var12 = 2
        if (1 if var4 == 0 else 0):
            break
        var22 = (var22 - func168(1.0, var8))
        if (1 if var22 == 0.0 else 0):
            var4 = 0
            var2 = var3
            if (1 if var7 >= var3 else 0):
                break
            while True:  # loop $label20
                var2 = (var2 - 1)
                var4 = (i32_load(((var5 + 480) + ((var2 - 1) << 2))) | var4)
                if (1 if var2 > var7 else 0):
                    continue
                break  # end loop
            if (1 if var4 == 0 else 0):
                break
            var6 = var8
            while True:  # loop $label21
                var6 = (var6 - 24)
                var3 = (var3 - 1)
                if (1 if i32_load(((var5 + 480) + ((var3 - 1) << 2))) == 0 else 0):
                    continue
                break  # end loop
            break
            var2 = 1
            while True:  # loop $label23
                var4 = var2
                var2 = (var2 + 1)
                if (1 if i32_load(((var5 + 480) + ((var7 - var4) << 2))) == 0 else 0):
                    continue
                break  # end loop
            var4 = (var3 + var4)
            while True:  # loop $label25
                var3 = (var3 + 1)
                f64_store(((var5 + 320) + ((var3 + 1) << 3)), float(i32_load((((var3 + var13) << 2) + 28944))))
                var2 = 0
                var22 = 0.0
                while True:  # loop $label24
                    var22 = ((f64_load((var14 + (var2 << 3))) * f64_load(((var5 + 320) + ((var3 - var2) << 3)))) + var22)
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != 1 else 0):
                        continue
                    break  # end loop
                f64_store((var5 + (var3 << 3)), var22)
                if (1 if var3 < var4 else 0):
                    continue
                break  # end loop
            var3 = var4
            continue
        break  # end loop
    var22 = func168(var22, (24 - var6))
    if (1 if func168(var22, (24 - var6)) >= 16777216.0 else 0):
        var23 = (var22 * 5.960464477539063e-08)
        if (1 if abs((var22 * 5.960464477539063e-08)) < 2147483648.0 else 0):
            break
        var2 = -2147483648
        var22 = ((float(-2147483648) * -16777216.0) + var22)
        if (1 if abs(((float(-2147483648) * -16777216.0) + var22)) < 2147483648.0 else 0):
            break
        i32_store(int(var22), -2147483648)
        var3 = (var3 + 1)
        break
    if (1 if abs(var22) < 2147483648.0 else 0):
        break
    var2 = -2147483648
    var6 = var8
    i32_store(((var5 + 480) + (var3 << 2)), var2)
    var22 = func168(1.0, var6)
    if (1 if var3 < 0 else 0):
        break
    var2 = var3
    while True:  # loop $label32
        var4 = var2
        f64_store((var5 + (var2 << 3)), (var22 * float(i32_load(((var5 + 480) + (var2 << 2))))))
        var2 = (var2 - 1)
        var22 = (var22 * 5.960464477539063e-08)
        if var4:
            continue
        break  # end loop
    if (1 if var3 < 0 else 0):
        break
    var4 = var3
    while True:  # loop $label34
        var22 = 0.0
        var2 = 0
        var6 = (var3 - var4)
        var8 = (var7 if (1 if var6 > var7 else 0) else (var3 - var4))
        if (1 if (var7 if (1 if var6 > var7 else 0) else (var3 - var4)) >= 0 else 0):
            while True:  # loop $label33
                var22 = ((f64_load(((var2 << 3) + 31712)) * f64_load((var5 + ((var2 + var4) << 3)))) + var22)
                var13 = (1 if var2 != var8 else 0)
                var2 = (var2 + 1)
                if var13:
                    continue
                break  # end loop
        f64_store(((var5 + 160) + (var6 << 3)), var22)
        var2 = (1 if var4 > 0 else 0)
        var4 = (var4 - 1)
        if var2:
            continue
        break  # end loop
    var22 = 0.0
    if (1 if var3 >= 0 else 0):
        while True:  # loop $label35
            var2 = var3
            var3 = (var3 - 1)
            var22 = (var22 + f64_load(((var5 + 160) + (var2 << 3))))
            if var2:
                continue
            break  # end loop
    f64_store(var11, ((-var22) if var12 else var22))
    global global0
    global0 = (var5 + 560)
    var3 = (var10 & 7)
    var22 = f64_load(var11)
    if (1 if var17 < 0 else 0):
        f64_store(var1, (-var22))
        var3 = (0 - var3)
        break
    f64_store(var1, var22)
    global global0
    global0 = (var11 + 16)
    return var3


# ==========================================================
# $func440
# ==========================================================
def func440(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var2 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var3 = i32_load(var0)
    var4 = i32_load((i32_load(var0) - 4))
    var3 = i32_load((var3 - 8))
    i64_store(var2 + 32, 0)
    i64_store(var2 + 40, 0)
    i64_store(var2 + 48, 0)
    i64_store(var2 + 55, 0)
    i64_store(var2 + 24, 0)
    i32_store(var2 + 20, 0)
    i32_store(var2 + 16, 32540)
    i32_store(var2 + 12, var0)
    i32_store(var2 + 8, var1)
    var0 = (var0 + var3)
    var3 = 0
    if func79(var4, var1, 0):
        i32_store(var2 + 56, 1)
        # call_indirect via table[i32_load(i32_load(var4) + 20)]
        var3 = (var0 if (1 if i32_load(var2 + 32) == 1 else 0) else 0)
        break
    # call_indirect via table[i32_load(i32_load(var4) + 24)]
    # br_table ['$label1', '$label2', '$label0']
    _br_idx = i32_load(var2 + 44)
    break  # br_table
    var3 = (((i32_load(var2 + 28) if (1 if i32_load(var2 + 40) == 1 else 0) else 0) if (1 if i32_load(var2 + 36) == 1 else 0) else 0) if (1 if i32_load(var2 + 48) == 1 else 0) else 0)
    break
    if (1 if i32_load(var2 + 32) != 1 else 0):
        if i32_load(var2 + 48):
            break
        if (1 if i32_load(var2 + 36) != 1 else 0):
            break
        if (1 if i32_load(var2 + 40) != 1 else 0):
            break
    var3 = i32_load(var2 + 24)
    global global0
    global0 = (var2 - -64)
    return var3


# ==========================================================
# $func444
# ==========================================================
def func444(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    if var2:
        if (1 if var3 == 0 else 0):
            break
        var4 = i32_load(var3)
        var5 = i32_load(var2)
        if (1 if var1 <= 0 else 0):
            break
        if var5:
            break
        var6 = i64_extend_u(var1)
        var5 = i32(((((i64_extend_u(var1) + (i64_extend_s(var4) * i64_extend_s(var0))) - 1) & 0xFFFFFFFFFFFFFFFF) // var6))
        if (1 if var0 <= 0 else 0):
            break
        if var4:
            break
        var6 = i64_extend_u(var0)
        var4 = i32(((((i64_extend_u(var0) + (i64_extend_s(var5) * i64_extend_s(var1))) - 1) & 0xFFFFFFFFFFFFFFFF) // var6))
        var1 = 0
        if (1 if (var5 - 1073741824) < -1073741823 else 0):
            break
        if (1 if var4 <= 0 else 0):
            break
        if (1 if var4 > 1073741823 else 0):
            break
        i32_store(var2, var5)
        i32_store(var3, var4)
        var1 = 1
        return var1
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    return 3204

