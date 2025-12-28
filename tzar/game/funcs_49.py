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
# $func128
# ==========================================================
def func128(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    if (1 if (i32_load8_u(var0) & 32) == 0 else 0):
        var3 = var1
        var1 = var0
        var0 = i32_load(var0 + 16)
        if i32_load(var0 + 16):
        else:
            if func433(var1):
                break
        var5 = i32_load(var1 + 20)
        if (1 if var0 > (i32_load(var1 + 16) - i32_load(var1 + 20)) else 0):
            # call_indirect via table[i32_load(var1 + 36)]
            break
        if (1 if i32_load(var1 + 80) < 0 else 0):
            break
        var0 = var2
        while True:  # loop $label3
            var4 = var0
            if (1 if var0 == 0 else 0):
                break
            var0 = (var4 - 1)
            if (1 if i32_load8_u((var3 + (var4 - 1))) != 10 else 0):
                continue
            break  # end loop
        # call_indirect via table[i32_load(var1 + 36)]
        if (1 if call_indirect(i32_load(var1 + 36)) < var4 else 0):
            break
        var3 = (var3 + var4)
        var2 = (var2 - var4)
        var5 = i32_load(var1 + 20)
        i32_store(var1 + 20, (i32_load(var1 + 20) + var2))
    return var4


# ==========================================================
# $func130
# ==========================================================
def func130(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var2 = i32_load(var0 + 28)
    var1 = i32_load(var2 + 20)
    var3 = i32_load(var0 + 16)
    var1 = (i32_load(var2 + 20) if (1 if var1 < var3 else 0) else i32_load(var0 + 16))
    if (1 if (i32_load(var2 + 20) if (1 if var1 < var3 else 0) else i32_load(var0 + 16)) == 0 else 0):
        break
    i32_store(var0 + 12, (i32_load(var0 + 12) + var1))
    i32_store(var2 + 16, (i32_load(var2 + 16) + var1))
    i32_store(var0 + 20, (i32_load(var0 + 20) + var1))
    i32_store(var0 + 16, (i32_load(var0 + 16) - var1))
    var0 = i32_load(var2 + 20)
    i32_store(var2 + 20, (i32_load(var2 + 20) - var1))
    if (1 if var0 != var1 else 0):
        break
    i32_store(var2 + 16, i32_load(var2 + 8))


# ==========================================================
# $func135
# ==========================================================
def func135(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var2 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) > 31 else 0):
        var3 = i32_load(var0 + 12)
        var1 = i32_load(var0 + 16)
        if (1 if i32_load(var0 + 12) > (i32_load(var0 + 16) + 8) else 0):
            i32_store(var0 + 20, (var2 - 32))
            var7 = ((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> 32)
            i64_store(var0, ((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> 32))
            var8 = i64_load32_u((i32_load(var0 + 8) + var1))
            i32_store(var0 + 16, (var1 + 4))
            i64_store(var0, ((var8 << 32) | var7))
            return
        var5 = (var1 if (1 if var1 > var3 else 0) else var3)
        while True:  # loop $label1
            if (1 if var1 == var5 else 0):
                var1 = var5
                var4 = var2
                break
            var7 = ((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> 8)
            i64_store(var0, ((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> 8))
            var8 = i64_load8_u((i32_load(var0 + 8) + var1))
            var4 = (var2 - 8)
            i32_store(var0 + 20, (var2 - 8))
            var1 = (var1 + 1)
            i32_store(var0 + 16, (var1 + 1))
            i64_store(var0, ((var8 << 56) | var7))
            var6 = (1 if var2 > 15 else 0)
            var2 = var4
            if var6:
                continue
            break  # end loop
        if (1 if var1 > var3 else 0):
            break
        if (1 if i32_load(var0 + 24) == 0 else 0):
            if (1 if var1 != var3 else 0):
                break
            if (1 if var4 < 65 else 0):
                break
        i64_store(var0 + 20, 4294967296)
        return
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func145
# ==========================================================
def func145(var0, var1):
    var2 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    # br_table ['$label0', '$label1', '$label2', '$label2', '$label3', '$label2', '$label4', '$label2', '$label2', '$label5', '$label2', '$label2', '$label2', '$label5', '$label6', '$label5', '$label5', '$label6', '$label5', '$label2', '$label2', '$label2', '$label2', '$label4', '$label2', '$label0', '$label7', '$label5', '$label5', '$label5', '$label5', '$label2', '$label2', '$label2', '$label2', '$label8', '$label2', '$label5', '$label0', '$label6', '$label6', '$label6', '$label6', '$label5', '$label2', '$label2', '$label5', '$label4', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label6', '$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label8', '$label6', '$label0', '$label2', '$label9', '$label2', '$label2', '$label2', '$label10', '$label2']
    _br_idx = var0
    break  # br_table
    if i32_load(9216064):
        break
    break
    if i32_load(9216064):
        break
    break
    if i32_load(9216064):
        break
    break
    if (1 if i32_load(9216064) == 0 else 0):
        break
    break
    if i32_load(9216064):
        break
    break
    if i32_load(9216064):
        break
    break
    if i32_load(9216064):
        break
    break
    if i32_load(9216064):
        break
    break
    if i32_load(9216064):
        break
    break
    if i32_load(9216064):
        break
    break
    if i32_load(9216064):
        break
    var0 = 2
    i32_store(4, 2)
    i32_store(var2, var0)
    i32_store(var2 + 4, var1)
    global global0
    global0 = (var2 + 16)
    return var2


# ==========================================================
# $func155
# ==========================================================
def func155(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var3 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var4 = i32_load(9561692)
    var6 = i32_load16_u(var0 + 110)
    if (1 if i32_load(9147132) == 0 else 0):
        break
    if (1 if i32_load(9671152) != i32_load8_u(var1 + 122) else 0):
        break
    var5 = i32_load16_u(var1 + 110)
    if (1 if var6 == i32_load16_u(var1 + 110) else 0):
        break
    if (1 if var6 == 0 else 0):
        break
    var8 = (var4 + (var5 * 286704))
    var5 = (var4 + (var5 * 286704))
    var9 = i32_load((var4 + (var5 * 286704)) + 284628)
    var5 = i32_load(var5 + 284616)
    var7 = (var4 + (var6 * 286704))
    var10 = i32_load((var4 + (var6 * 286704)) + 284616)
    i32_store(var3 + 16, (i32_load((var4 + (var6 * 286704)) + 284616) if var10 else i32_load(var7 + 284628)))
    i32_store(var3 + 12, var7)
    i32_store(var3 + 4, var8)
    i32_store(var3, 927)
    i32_store(var3 + 8, (var5 if var5 else var9))
    a_b()
    if var2:
        break
    var4 = i32_load(((var4 + (var6 * 286704)) + 278560))
    if (1 if i32_load(((var4 + (var6 * 286704)) + 278560)) == 0 else 0):
        var2 = i32_load16_u(var1 + 110)
        break
    var2 = i32_load16_u(var1 + 110)
    var4 = (var4 + ((i32_load8_u(var0 + 122) + (i32_load16_u(var1 + 110) * 255)) << 2))
    i32_store((var4 + ((i32_load8_u(var0 + 122) + (i32_load16_u(var1 + 110) * 255)) << 2)), (i32_load(var4) + 1))
    var2 = i32_load(((i32_load(9561692) + (var2 * 286704)) + 278568))
    if (1 if i32_load(((i32_load(9561692) + (var2 * 286704)) + 278568)) == 0 else 0):
        break
    var2 = (var2 + ((i32_load8_u(var1 + 122) + (i32_load16_u(var0 + 110) * 255)) << 2))
    i32_store((var2 + ((i32_load8_u(var1 + 122) + (i32_load16_u(var0 + 110) * 255)) << 2)), (i32_load(var2) + 1))
    i32_store16(var1 + 116, i32_load(var0 + 28))
    global global0
    global0 = (var3 + 32)


# ==========================================================
# $func172
# ==========================================================
def func172(var0):
    var1 = 0
    var2 = 0
    var1 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    if var0:
        i32_store(9143000, 0)
    var0 = 0
    a_b()
    i32_store(9671120, 0)
    var2 = i32_load(9147120)
    if (1 if i32_load(9147120) == 0 else 0):
        break
    while True:  # loop $label1
        var2 = ((i32_load(9143000) * var2) + var0)
        if (1 if ((i32_load(9143000) * var2) + var0) >= i32_load(9681836) else 0):
            break
        i32_store(9671120, (i32_load(9671120) + 1))
        var2 = i32_load(((i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9681828) + (var2 << 2))) * 132)) + 122) * 404) + 9568096) + 144)
        i64_store(var1 + 32, 1)
        i64_store(var1 + 40, 0)
        i64_store(var1 + 48, 0)
        i64_store(var1 + 56, 4294967295)
        i64_store(var1 + 24, 1)
        i32_store(var1 + 20, (0 - var2))
        i32_store(var1 + 16, var0)
        a_b()
        var0 = (var0 + 1)
        var2 = i32_load(9147120)
        if (1 if (var0 + 1) < i32_load(9147120) else 0):
            continue
        break  # end loop
    i32_store(var1, i32_load(9143000))
    i32_store(var1 + 4, i32_load(9681836))
    a_b()
    global global0
    global0 = (var1 - -64)

