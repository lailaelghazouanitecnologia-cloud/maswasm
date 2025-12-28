"""
Auto-generated from WAT. Contains 2 functions.
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
# $func419
# ==========================================================
def func419(var0, var1):
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
    var2 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var5 = 1
    # br_table ['$label0', '$label0', '$label1', '$label2', '$label3', '$label4', '$label5']
    _br_idx = ((var1 - var0) // 28)
    break  # br_table
    var1 = (var1 - 28)
    if (1 if (i32_load((var1 - 28) + 12) * i32_load(var1 + 8)) <= (i32_load(var0 + 12) * i32_load(var0 + 8)) else 0):
        break
    i32_store(var2 + 24, i32_load(var0 + 24))
    i64_store(var2 + 16, i64_load(var0 + 16))
    i64_store(var2 + 8, i64_load(var0 + 8))
    i64_store(var2, i64_load(var0))
    i32_store(var0 + 24, i32_load(var1 + 24))
    i64_store(var0 + 16, i64_load(var1 + 16))
    i64_store(var0 + 8, i64_load(var1 + 8))
    i64_store(var0, i64_load(var1))
    i32_store(var1 + 24, i32_load(var2 + 24))
    i64_store(var1 + 16, i64_load(var2 + 16))
    i64_store(var1 + 8, i64_load(var2 + 8))
    i64_store(var1, i64_load(var2))
    break
    var3 = (var1 - 28)
    var4 = (i32_load(((var1 - 28) + 12)) * i32_load(var3 + 8))
    var1 = (var0 + 28)
    var6 = (i32_load(var0 + 40) * i32_load(var0 + 36))
    if (1 if (i32_load(var0 + 40) * i32_load(var0 + 36)) <= (i32_load(var0 + 12) * i32_load(var0 + 8)) else 0):
        if (1 if var4 <= var6 else 0):
            break
        i32_store(var2 + 24, i32_load(var1 + 24))
        i64_store(var2 + 16, i64_load(var1 + 16))
        i64_store(var2 + 8, i64_load(var1 + 8))
        i64_store(var2, i64_load(var1))
        i32_store(var1 + 24, i32_load(var3 + 24))
        i64_store(var1 + 16, i64_load(var3 + 16))
        i64_store(var1 + 8, i64_load(var3 + 8))
        i64_store(var1, i64_load(var3))
        i32_store(var3 + 24, i32_load(var2 + 24))
        i64_store(var3 + 16, i64_load(var2 + 16))
        i64_store(var3 + 8, i64_load(var2 + 8))
        i64_store(var3, i64_load(var2))
        if (1 if (i32_load(var0 + 40) * i32_load(var0 + 36)) <= (i32_load(var0 + 12) * i32_load(var0 + 8)) else 0):
            break
        i32_store(var2 + 24, i32_load(var0 + 24))
        i64_store(var2 + 16, i64_load(var0 + 16))
        i64_store(var2 + 8, i64_load(var0 + 8))
        i64_store(var2, i64_load(var0))
        i32_store(var0 + 24, i32_load(var1 + 24))
        i64_store(var0 + 16, i64_load(var1 + 16))
        i64_store(var0 + 8, i64_load(var1 + 8))
        i64_store(var0, i64_load(var1))
        i32_store(var1 + 24, i32_load(var2 + 24))
        i64_store(var1 + 16, i64_load(var2 + 16))
        i64_store(var1 + 8, i64_load(var2 + 8))
        i64_store(var1, i64_load(var2))
        break
    if (1 if var4 > var6 else 0):
        i32_store(var2 + 24, i32_load(var0 + 24))
        i64_store(var2 + 16, i64_load(var0 + 16))
        i64_store(var2 + 8, i64_load(var0 + 8))
        i64_store(var2, i64_load(var0))
        i32_store(var0 + 24, i32_load(var3 + 24))
        i64_store(var0 + 16, i64_load(var3 + 16))
        i64_store(var0 + 8, i64_load(var3 + 8))
        i64_store(var0, i64_load(var3))
        i32_store(var3 + 24, i32_load(var2 + 24))
        i64_store(var3 + 16, i64_load(var2 + 16))
        i64_store(var3 + 8, i64_load(var2 + 8))
        i64_store(var3, i64_load(var2))
        break
    i32_store(var2 + 24, i32_load(var0 + 24))
    i64_store(var2 + 16, i64_load(var0 + 16))
    i64_store(var2 + 8, i64_load(var0 + 8))
    i64_store(var2, i64_load(var0))
    i32_store(var0 + 24, i32_load(var1 + 24))
    i64_store(var0 + 16, i64_load(var1 + 16))
    i64_store(var0 + 8, i64_load(var1 + 8))
    i64_store(var0, i64_load(var1))
    i32_store(var1 + 24, i32_load(var2 + 24))
    i64_store(var1 + 16, i64_load(var2 + 16))
    i64_store(var1 + 8, i64_load(var2 + 8))
    i64_store(var1, i64_load(var2))
    if (1 if (i32_load(var3 + 12) * i32_load(var3 + 8)) <= (i32_load(var0 + 40) * i32_load(var0 + 36)) else 0):
        break
    i32_store(var2 + 24, i32_load(var1 + 24))
    i64_store(var2 + 16, i64_load(var1 + 16))
    i64_store(var2 + 8, i64_load(var1 + 8))
    i64_store(var2, i64_load(var1))
    i32_store(var1 + 24, i32_load(var3 + 24))
    i64_store(var1 + 16, i64_load(var3 + 16))
    i64_store(var1 + 8, i64_load(var3 + 8))
    i64_store(var1, i64_load(var3))
    i32_store(var3 + 24, i32_load(var2 + 24))
    i64_store(var3 + 16, i64_load(var2 + 16))
    i64_store(var3 + 8, i64_load(var2 + 8))
    i64_store(var3, i64_load(var2))
    break
    break
    break
    var6 = (i32_load(var0 + 68) * i32_load((var0 - -64)))
    var4 = (var0 + 28)
    var3 = (var0 + 56)
    var7 = (i32_load(var0 + 40) * i32_load(var0 + 36))
    var8 = (i32_load(var0 + 12) * i32_load(var0 + 8))
    if (1 if (i32_load(var0 + 40) * i32_load(var0 + 36)) <= (i32_load(var0 + 12) * i32_load(var0 + 8)) else 0):
        if (1 if var6 <= var7 else 0):
            break
        i32_store(var2 + 24, i32_load(var4 + 24))
        i64_store(var2 + 16, i64_load(var4 + 16))
        i64_store(var2 + 8, i64_load(var4 + 8))
        i64_store(var2, i64_load(var4))
        i32_store(var4 + 24, i32_load((var3 + 24)))
        i64_store(var4 + 16, i64_load((var3 + 16)))
        i64_store(var4 + 8, i64_load((var3 + 8)))
        i64_store(var4, i64_load(var3))
        i32_store(var3 + 24, i32_load(var2 + 24))
        i64_store(var3 + 16, i64_load(var2 + 16))
        i64_store(var3 + 8, i64_load(var2 + 8))
        i64_store(var3, i64_load(var2))
        if (1 if (i32_load(var0 + 40) * i32_load(var0 + 36)) <= var8 else 0):
            break
        i32_store(var2 + 24, i32_load(var0 + 24))
        i64_store(var2 + 16, i64_load(var0 + 16))
        i64_store(var2 + 8, i64_load(var0 + 8))
        i64_store(var2, i64_load(var0))
        i32_store(var0 + 24, i32_load(var4 + 24))
        i64_store(var0 + 16, i64_load(var4 + 16))
        i64_store(var0 + 8, i64_load(var4 + 8))
        i64_store(var0, i64_load(var4))
        i32_store(var4 + 24, i32_load(var2 + 24))
        i64_store(var4 + 16, i64_load(var2 + 16))
        i64_store(var4 + 8, i64_load(var2 + 8))
        i64_store(var4, i64_load(var2))
        break
    if (1 if var6 > var7 else 0):
        i32_store(var2 + 24, i32_load(var0 + 24))
        i64_store(var2 + 16, i64_load(var0 + 16))
        i64_store(var2 + 8, i64_load(var0 + 8))
        i64_store(var2, i64_load(var0))
        i32_store(var0 + 24, i32_load((var3 + 24)))
        i64_store(var0 + 16, i64_load((var3 + 16)))
        i64_store(var0 + 8, i64_load((var3 + 8)))
        i64_store(var0, i64_load(var3))
        i32_store(var3 + 24, i32_load(var2 + 24))
        i64_store(var3 + 16, i64_load(var2 + 16))
        i64_store(var3 + 8, i64_load(var2 + 8))
        i64_store(var3, i64_load(var2))
        break
    i32_store(var2 + 24, i32_load(var0 + 24))
    i64_store(var2 + 16, i64_load(var0 + 16))
    i64_store(var2 + 8, i64_load(var0 + 8))
    i64_store(var2, i64_load(var0))
    i32_store(var0 + 24, i32_load(var4 + 24))
    i64_store(var0 + 16, i64_load(var4 + 16))
    i64_store(var0 + 8, i64_load(var4 + 8))
    i64_store(var0, i64_load(var4))
    i32_store(var4 + 24, i32_load(var2 + 24))
    i64_store(var4 + 16, i64_load(var2 + 16))
    i64_store(var4 + 8, i64_load(var2 + 8))
    i64_store(var4, i64_load(var2))
    if (1 if var6 <= (i32_load(var0 + 40) * i32_load(var0 + 36)) else 0):
        break
    i32_store(var2 + 24, i32_load(var4 + 24))
    i64_store(var2 + 16, i64_load(var4 + 16))
    i64_store(var2 + 8, i64_load(var4 + 8))
    i64_store(var2, i64_load(var4))
    i32_store(var4 + 24, i32_load((var3 + 24)))
    i64_store(var4 + 16, i64_load((var3 + 16)))
    i64_store(var4 + 8, i64_load((var3 + 8)))
    i64_store(var4, i64_load(var3))
    i32_store(var3 + 24, i32_load(var2 + 24))
    i64_store(var3 + 16, i64_load(var2 + 16))
    i64_store(var3 + 8, i64_load(var2 + 8))
    i64_store(var3, i64_load(var2))
    var4 = (var0 + 84)
    if (1 if (var0 + 84) == var1 else 0):
        break
    var7 = 0
    while True:  # loop $label10
        var8 = i32_load(var4 + 12)
        var9 = i32_load(var4 + 8)
        var10 = (i32_load(var4 + 12) * i32_load(var4 + 8))
        if (1 if (i32_load(var4 + 12) * i32_load(var4 + 8)) <= (i32_load(var3 + 12) * i32_load(var3 + 8)) else 0):
            break
        var11 = i64_load(var4)
        i32_store(var2 + 8, i32_load(var4 + 24))
        i64_store(var2, i64_load(var4 + 16))
        var6 = var4
        while True:  # loop $label9
            var5 = var3
            i64_store(var6, i64_load(var3))
            i32_store(var6 + 24, i32_load(var3 + 24))
            i64_store(var6 + 16, i64_load(var3 + 16))
            i64_store(var6 + 8, i64_load(var3 + 8))
            if (1 if var0 == var3 else 0):
                var5 = var0
                break
            var6 = var5
            var3 = (var5 - 28)
            if (1 if var10 > (i32_load((var5 - 28) + 12) * i32_load(var3 + 8)) else 0):
                continue
            break  # end loop
        i32_store(var5 + 12, var8)
        i32_store(var5 + 8, var9)
        i64_store(var5, var11)
        i64_store(var5 + 16, i64_load(var2))
        i32_store(var5 + 24, i32_load(var2 + 8))
        var7 = (var7 + 1)
        if (1 if (var7 + 1) != 8 else 0):
            break
        var5 = (1 if (var4 + 28) == var1 else 0)
        break
        var3 = var4
        var5 = (var4 + 28)
        var4 = (var4 + 28)
        if (1 if var1 != var5 else 0):
            continue
        break  # end loop
    var5 = 1
    global global0
    global0 = (var2 + 32)
    return var5


# ==========================================================
# $func447
# ==========================================================
def func447(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var5 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var9 = i32_load(var1 + 4)
    var10 = i32_load(var1)
    if var0:
        var6 = i32_load(var0 + 8)
        i32_store(var1 + 72, (1 if i32_load(var0 + 8) != 0 else 0))
        var7 = var10
        var8 = var9
        if (1 if var6 == 0 else 0):
            break
        var6 = 0
        var7 = i32_load(var0 + 20)
        if (1 if i32_load(var0 + 20) <= 0 else 0):
            break
        var8 = i32_load(var0 + 24)
        if (1 if i32_load(var0 + 24) <= 0 else 0):
            break
        var3 = i32_load(var0 + 16)
        var2 = (1 if var2 > 10 else 0)
        var3 = ((i32_load(var0 + 16) & -2) if (1 if var2 > 10 else 0) else var3)
        var4 = i32_load(var0 + 12)
        var4 = ((i32_load(var0 + 12) & -2) if var2 else var4)
        if (1 if (((i32_load(var0 + 16) & -2) if (1 if var2 > 10 else 0) else var3) | ((i32_load(var0 + 12) & -2) if var2 else var4)) < 0 else 0):
            break
        if (1 if var8 > var9 else 0):
            break
        if (1 if var3 >= var9 else 0):
            break
        if (1 if var7 > var10 else 0):
            break
        if (1 if var4 >= var10 else 0):
            break
        if (1 if (var10 - var4) < var7 else 0):
            break
        if (1 if (var9 - var3) >= var8 else 0):
            break
        break
    i32_store(var1 + 72, 0)
    var7 = var10
    var8 = var9
    i32_store(var1 + 84, var3)
    i32_store(var1 + 76, var4)
    i32_store(var1 + 16, var8)
    i32_store(var1 + 12, var7)
    i32_store(var1 + 88, (var3 + var8))
    i32_store(var1 + 80, (var4 + var7))
    if (1 if var0 == 0 else 0):
        break
    var2 = i32_load(var0 + 28)
    i32_store(var1 + 92, (1 if i32_load(var0 + 28) != 0 else 0))
    var6 = 1
    var3 = 1
    if var2:
        i32_store(var5 + 12, i32_load(var0 + 32))
        i32_store(var5 + 8, i32_load(var0 + 36))
        if (1 if func444(var7, var8, (var5 + 12), (var5 + 8)) == 0 else 0):
            break
        i32_store(var1 + 96, i32_load(var5 + 12))
        i32_store(var1 + 100, i32_load(var5 + 8))
        var3 = (1 if i32_load(var1 + 92) == 0 else 0)
    var2 = (1 if i32_load(var0) != 0 else 0)
    i32_store(var1 + 68, (1 if i32_load(var0) != 0 else 0))
    i32_store(var1 + 56, (1 if i32_load(var0 + 4) == 0 else 0))
    if var3:
        break
    var0 = 0
    if (1 if i32_load(var1 + 96) < ((var10 * 3) // 4) else 0):
        var0 = (1 if i32_load(var1 + 100) < ((var9 * 3) // 4) else 0)
    i32_store(var1 + 56, 0)
    i32_store(var1 + 68, (var0 | var2))
    break
    var6 = 0
    break
    i32_store(var1 + 68, 0)
    i32_store(var1 + 92, 0)
    var6 = 1
    i32_store(var1 + 56, 1)
    global global0
    global0 = (var5 + 16)
    return var6

