"""
Auto-generated from WAT. Contains 7 functions.
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
# $func1089
# ==========================================================
def func1089(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var5 = i32_load(var0 + 104)
    if (1 if i32_load(var0 + 104) == 0 else 0):
        break
    var6 = i32_load(var1)
    var8 = i32_load(i32_load(var1))
    var9 = ((1 if i32_load(i32_load(var1)) == 4 else 0) | (1 if var8 == 9 else 0))
    var1 = i32_load(var0 + 16)
    var3 = i32_load(var0 + 8)
    var10 = i32_load(var0 + 12)
    if (1 if i32_load(var0 + 56) == 0 else 0):
        var4 = var3
        break
    if (1 if var3 == 0 else 0):
        break
    var4 = (var3 - 1)
    var5 = (var5 - i32_load(var0))
    var7 = var1
    var11 = i32_load(var0 + 84)
    var1 = (i32_load(var0 + 84) + (var1 + var3))
    if (1 if (i32_load(var0 + 84) + (var1 + var3)) != i32_load(var0 + 88) else 0):
        var1 = var7
        break
    var1 = (var1 - (var4 + var11))
    var0 = i32_load(var6 + 20)
    var7 = (i32_load(var6 + 16) + (i32_load(var6 + 20) * var4))
    # call_indirect via table[i32_load(9687300)]
    var0 = call_indirect(i32_load(9687300))
    if (1 if var1 != var2 else 0):
        break
    if (1 if var0 == 0 else 0):
        break
    if (1 if (var8 - 11) < -4 else 0):
        break
    # call_indirect via table[i32_load(9687292)]
    return 0
    a_c()
    raise RuntimeError('unreachable')
    return 7652


# ==========================================================
# $gd
# Export: gd
# ==========================================================
def gd():
    """Export: gd"""
    var0 = 0
    var1 = 0
    var2 = 0
    var0 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if i32_load(9140324):
        while True:  # loop $label0
            var2 = i32_load(i32_load((i32_load(9140332) + (var1 << 2))) + 32)
            i32_store(var0, var1)
            i32_store(var0 + 4, var2)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < i32_load(9140324) else 0):
                continue
            break  # end loop
    global global0
    global0 = (var0 + 16)


# ==========================================================
# $func1116
# ==========================================================
def func1116(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    if (1 if (i32_load8_u(var0 + 8) & 1) == 0 else 0):
        if (1 if i32_load(var0 + 12) <= 0 else 0):
            break
        if (1 if i32_load(var0 + 16) <= 0 else 0):
            break
        var1 = i32_load(var0 + 40)
        # call_indirect via table[i32_load(var1 + 44)]
        var2 = call_indirect(i32_load(var1 + 44))
        var3 = i32_load(var1 + 48)
        if i32_load(var1 + 48):
            # call_indirect via table[var3]
        i32_store(var1 + 16, (i32_load(var1 + 16) + var2))
        var1 = 1
        return var1
    a_c()
    raise RuntimeError('unreachable')
    return 2396


# ==========================================================
# $func48
# ==========================================================
def func48(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0.0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = i32_reinterpret_f32(var0)
    var2 = (i32_reinterpret_f32(var0) & 2147483647)
    if (1 if (i32_reinterpret_f32(var0) & 2147483647) <= 1061752794 else 0):
        if (1 if var2 < 964689920 else 0):
            break
        var0 = func75(float(var0))
        break
    if (1 if var2 <= 1081824209 else 0):
        var4 = float(var0)
        if (1 if var2 <= 1075235811 else 0):
            if (1 if var3 < 0 else 0):
                var0 = (-func76((var4 + 1.5707963267948966)))
                break
            var0 = func76((var4 + -1.5707963267948966))
            break
        var0 = func75((-((-3.141592653589793 if (1 if var3 >= 0 else 0) else 3.141592653589793) + var4)))
        break
    if (1 if var2 <= 1088565717 else 0):
        if (1 if var2 <= 1085271519 else 0):
            var4 = float(var0)
            if (1 if var3 < 0 else 0):
                var0 = func76((var4 + 4.71238898038469))
                break
            var0 = (-func76((var4 + -4.71238898038469)))
            break
        var0 = func75(((6.283185307179586 if (1 if var3 < 0 else 0) else -6.283185307179586) + float(var0)))
        break
    if (1 if var2 >= 2139095040 else 0):
        var0 = (var0 - var0)
        break
    # br_table ['$label1', '$label2', '$label3', '$label4']
    _br_idx = (func435(var0, (var1 + 8)) & 3)
    break  # br_table
    var0 = func75(f64_load(var1 + 8))
    break
    var0 = func76(f64_load(var1 + 8))
    break
    var0 = func75((-f64_load(var1 + 8)))
    break
    var0 = (-func76(f64_load(var1 + 8)))
    global global0
    global0 = (var1 + 16)
    return var0


# ==========================================================
# $func49
# ==========================================================
def func49(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0.0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = i32_reinterpret_f32(var0)
    var2 = (i32_reinterpret_f32(var0) & 2147483647)
    if (1 if (i32_reinterpret_f32(var0) & 2147483647) <= 1061752794 else 0):
        if (1 if var2 < 964689920 else 0):
            break
        break
    if (1 if var2 <= 1081824209 else 0):
        if (1 if var2 >= 1075235812 else 0):
            break
        var4 = float(var0)
        if (1 if var3 < 0 else 0):
            break
        break
    if (1 if var2 <= 1088565717 else 0):
        if (1 if var2 >= 1085271520 else 0):
            break
        if (1 if var3 < 0 else 0):
            break
        break
    if (1 if var2 >= 2139095040 else 0):
        break
    # br_table ['$label1', '$label2', '$label3', '$label4']
    _br_idx = (func435(var0, (var1 + 8)) & 3)
    break  # br_table
    break
    break
    break
    var0 = func75(f64_load(var1 + 8))
    global global0
    global0 = (var1 + 16)
    return var0


# ==========================================================
# $func52
# ==========================================================
def func52(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0.0
    var11 = 0.0
    var12 = 0.0
    var2 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    if (1 if i32_load(40600) == 0 else 0):
        break
    if (1 if i32_load(9142868) < 490 else 0):
        break
    var10 = f32_load(42160)
    var3 = i32_load8_u(9143020)
    var11 = (float(i32_load(9147148)) if i32_load8_u(9143020) else (f32_load(42160) * 12.0))
    var10 = (float(i32_load(9147144)) if var3 else (var10 * 174.0))
    if i32_load8_u(9142916):
        var10 = f32_load(9671164)
        var12 = (var10 * f32_load(9671164))
        var11 = (var11 * var10)
        var7 = i32_load(9142884)
        var3 = i32_load(9142640)
        if (1 if i32_load(9142640) == 0 else 0):
            break
        if (1 if i32_load(var3 + 20) == 0 else 0):
            break
        var4 = i32_load(var3 + 28)
        if (1 if i32_load(var3 + 28) == 2147483647 else 0):
            var4 = i32_load(59152)
            i32_store(59152, (i32_load(59152) + 1))
            var5 = i32_load(9568052)
            i32_store(var3 + 28, var4)
            var8 = i32_load(var3)
            var6 = i32_load(var3 + 4)
            var9 = i32_load(9568048)
            i32_store(9568048, (i32_load(9568048) + 1))
            i32_store(((var9 << 2) + 9563952), var3)
            i32_store(9568052, (var5 + ((var8 * (var6 + 2)) << 2)))
            var5 = i32_load(9568056)
            i32_store(var3 + 56, i32_load(9568056))
            i32_store(9568056, (var5 + ((var6 * i32_load(var3)) << 2)))
        var4 = (var4 + (var0 << 16))
        i32_store(var2 + 76, var7)
        i32_store(var2 + 72, 0)
        i32_store(var2 + 68, (var1 << 16))
        i32_store((var2 - -64), 0)
        i64_store(var2 + 56, 0)
        i32_store(var2 + 52, 0)
        i32_store(var2 + 48, var4)
        i64_store(var2 + 40, 0)
        i64_store(var2 + 32, 0)
        i64_store(var2 + 24, 0)
        i64_store(var2 + 16, -4590434657685733376)
        f64_store(var2 + 8, float(var12))
        f64_store(var2, float(var11))
        a_b()
        break
    var11 = f32_load(9671164)
    global global0
    global0 = (var2 + 80)


# ==========================================================
# $func54
# ==========================================================
def func54(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var4 = i32_load(var0 + 8)
    var2 = i32_load(var0)
    if (1 if (i32_load(var0) & 15) == 0 else 0):
        var1 = (var0 + 4)
        var0 = 0
        break
    var3 = global3
    var5 = i32_load(var0 + 4)
    if (1 if i32_load(global3 + 24) != (i32_load(var0 + 4) & 1073741823) else 0):
        break
    if (1 if (var2 & 3) != 1 else 0):
        break
    var1 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        break
    i32_store(var0 + 20, (var1 - 1))
    return
    var6 = (var2 & 128)
    if (var2 & 128):
        i32_store(var3 + 84, (var0 + 16))
    var1 = (var0 + 4)
    var7 = i32_load(var0 + 12)
    var0 = i32_load(var0 + 16)
    i32_store(i32_load(var0 + 12), i32_load(var0 + 16))
    if (1 if (var3 + 76) != var0 else 0):
        i32_store((var0 - 4), var7)
    var0 = ((((var5 << 1) & (var2 << 29)) >> 31) & 2147483647)
    if (1 if var6 == 0 else 0):
        break
    i32_store(var3 + 84, 0)
    if (1 if -1 != 1 else 0):
        break
    if (1 if i32_load(9689396) == 0 else 0):
        break
    func111(9689392, 2147483647)
    if ((1 if var4 == 0 else 0) & (1 if var0 >= 0 else 0)):
        break
    func97(var1)

