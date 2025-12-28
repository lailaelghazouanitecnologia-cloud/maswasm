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
# $func399
# ==========================================================
def func399(var0, var1):
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
    var3 = (i32_load(var0 + 12) - 5)
    var2 = i32_load(var0 + 44)
    var9 = ((i32_load(var0 + 12) - 5) if (1 if var2 > var3 else 0) else i32_load(var0 + 44))
    var6 = i32_load(i32_load(var0) + 4)
    var10 = (1 if var1 != 4 else 0)
    while True:  # loop $label5
        var5 = 1
        var2 = i32_load(var0)
        var3 = i32_load(i32_load(var0) + 16)
        var8 = ((i32_load(var0 + 5820) + 42) >> 3)
        if (1 if i32_load(i32_load(var0) + 16) < ((i32_load(var0 + 5820) + 42) >> 3) else 0):
            break
        var11 = i32_load(var0 + 108)
        var12 = i32_load(var0 + 92)
        var7 = (i32_load(var0 + 108) - i32_load(var0 + 92))
        var4 = ((i32_load(var0 + 108) - i32_load(var0 + 92)) + i32_load(var2 + 4))
        var3 = (var3 - var8)
        var3 = (((i32_load(var0 + 108) - i32_load(var0 + 92)) + i32_load(var2 + 4)) if (1 if var3 > var4 else 0) else (var3 - var8))
        var3 = (65535 if (1 if var3 >= 65535 else 0) else (((i32_load(var0 + 108) - i32_load(var0 + 92)) + i32_load(var2 + 4)) if (1 if var3 > var4 else 0) else (var3 - var8)))
        if (1 if var9 > (65535 if (1 if var3 >= 65535 else 0) else (((i32_load(var0 + 108) - i32_load(var0 + 92)) + i32_load(var2 + 4)) if (1 if var3 > var4 else 0) else (var3 - var8))) else 0):
            if (1 if var1 == 0 else 0):
                break
            if (var10 & (1 if var3 == 0 else 0)):
                break
            if (1 if var3 != var4 else 0):
                break
        var8 = ((1 if var1 == 4 else 0) & (1 if var3 == var4 else 0))
        i32_store8(((i32_load(var0 + 20) + i32_load(var0 + 8)) - 4), var3)
        i32_store8(((i32_load(var0 + 20) + i32_load(var0 + 8)) - 3), ((var3 & 0xFFFFFFFF) >> 8))
        var2 = (var3 ^ -1)
        i32_store8(((i32_load(var0 + 20) + i32_load(var0 + 8)) - 2), (var3 ^ -1))
        i32_store8(((i32_load(var0 + 20) + i32_load(var0 + 8)) - 1), ((var2 & 0xFFFFFFFF) >> 8))
        var2 = i32_load(var0)
        var4 = i32_load(i32_load(var0) + 28)
        var5 = i32_load(var4 + 20)
        var13 = i32_load(var2 + 16)
        var5 = (i32_load(var4 + 20) if (1 if var5 < var13 else 0) else i32_load(var2 + 16))
        if (1 if (i32_load(var4 + 20) if (1 if var5 < var13 else 0) else i32_load(var2 + 16)) == 0 else 0):
            break
        i32_store(var2 + 12, (i32_load(var2 + 12) + var5))
        i32_store(var4 + 16, (i32_load(var4 + 16) + var5))
        i32_store(var2 + 20, (i32_load(var2 + 20) + var5))
        i32_store(var2 + 16, (i32_load(var2 + 16) - var5))
        var2 = i32_load(var4 + 20)
        i32_store(var4 + 20, (i32_load(var4 + 20) - var5))
        if (1 if var2 != var5 else 0):
            break
        i32_store(var4 + 16, i32_load(var4 + 8))
        if (1 if var11 != var12 else 0):
            var2 = (var7 if (1 if var3 > var7 else 0) else var3)
            var4 = i32_load(var0)
            i32_store(i32_load(var0) + 12, (i32_load(var4 + 12) + var2))
            i32_store(var4 + 16, (i32_load(var4 + 16) - var2))
            i32_store(var4 + 20, (i32_load(var4 + 20) + var2))
            i32_store(var0 + 92, (i32_load(var0 + 92) + var2))
            var3 = (var3 - var2)
        if var3:
            var2 = i32_load(var0)
            var5 = i32_load(i32_load(var0) + 12)
            var7 = i32_load(var2 + 4)
            var4 = (i32_load(var2 + 4) if (1 if var3 > var7 else 0) else var3)
            if (i32_load(var2 + 4) if (1 if var3 > var7 else 0) else var3):
                i32_store(var2 + 4, (var7 - var4))
                var5 = func35(var5, i32_load(var2), var4)
                # br_table ['$label2', '$label3', '$label4']
                _br_idx = (i32_load(i32_load(var2 + 28) + 24) - 1)
                break  # br_table
                i32_store(var2 + 48, func89(i32_load(var2 + 48), var5, var4))
                break
                i32_store(var2 + 48, func43(i32_load(var2 + 48), var5, var4))
                i32_store(var2, (i32_load(var2) + var4))
                i32_store(var2 + 8, (i32_load(var2 + 8) + var4))
                var2 = i32_load(var0)
                var5 = i32_load(i32_load(var0) + 12)
            i32_store(var2 + 12, (var3 + var5))
            i32_store(var2 + 16, (i32_load(var2 + 16) - var3))
            i32_store(var2 + 20, (i32_load(var2 + 20) + var3))
        if (1 if var8 == 0 else 0):
            continue
        break  # end loop
    var2 = i32_load(var0)
    var5 = 0
    var3 = i32_load(var2 + 4)
    if (1 if i32_load(var2 + 4) == var6 else 0):
        var3 = i32_load(var0 + 108)
        break
    var4 = (var6 - var3)
    var3 = i32_load(var0 + 44)
    if (1 if (var6 - var3) >= i32_load(var0 + 44) else 0):
        i32_store(var0 + 5808, 2)
        var3 = i32_load(var0 + 44)
        i32_store(var0 + 5812, i32_load(var0 + 44))
        i32_store(var0 + 108, var3)
        break
    var2 = i32_load(var0 + 108)
    if (1 if (i32_load(var0 + 60) - i32_load(var0 + 108)) > var4 else 0):
        break
    var2 = (var2 - var3)
    i32_store(var0 + 108, (var2 - var3))
    var6 = i32_load(var0 + 56)
    var3 = i32_load(var0 + 5808)
    if (1 if i32_load(var0 + 5808) <= 1 else 0):
        i32_store(var0 + 5808, (var3 + 1))
    var2 = i32_load(var0 + 108)
    if (1 if i32_load(var0 + 108) >= i32_load(var0 + 5812) else 0):
        break
    i32_store(var0 + 5812, var2)
    var3 = (i32_load(var0 + 108) + var4)
    i32_store(var0 + 108, (i32_load(var0 + 108) + var4))
    var2 = i32_load(var0 + 5812)
    var6 = (i32_load(var0 + 44) - i32_load(var0 + 5812))
    i32_store(var0 + 5812, ((var4 if (1 if var4 < var6 else 0) else (i32_load(var0 + 44) - i32_load(var0 + 5812))) + var2))
    i32_store(var0 + 92, var3)
    if (1 if var3 > i32_load(var0 + 5824) else 0):
        i32_store(var0 + 5824, var3)
    var2 = 3
    if (1 if var5 == 0 else 0):
        break
    # br_table ['$label10', '$label11', '$label11', '$label11', '$label10', '$label11']
    _br_idx = var1
    break  # br_table
    if i32_load(i32_load(var0) + 4):
        break
    var2 = 1
    if (1 if var3 == i32_load(var0 + 92) else 0):
        break
    var2 = (i32_load(var0 + 60) - var3)
    if (1 if (i32_load(var0 + 60) - var3) >= i32_load(i32_load(var0) + 4) else 0):
        break
    var5 = i32_load(var0 + 92)
    var4 = i32_load(var0 + 44)
    if (1 if i32_load(var0 + 92) < i32_load(var0 + 44) else 0):
        break
    var3 = (var3 - var4)
    i32_store(var0 + 108, (var3 - var4))
    i32_store(var0 + 92, (var5 - var4))
    var5 = i32_load(var0 + 56)
    var3 = i32_load(var0 + 5808)
    if (1 if i32_load(var0 + 5808) <= 1 else 0):
        i32_store(var0 + 5808, (var3 + 1))
    var2 = (i32_load(var0 + 44) + var2)
    var3 = i32_load(var0 + 108)
    if (1 if i32_load(var0 + 108) >= i32_load(var0 + 5812) else 0):
        break
    i32_store(var0 + 5812, var3)
    var4 = i32_load(var0)
    var5 = i32_load(i32_load(var0) + 4)
    var2 = (var2 if (1 if var2 < var5 else 0) else i32_load(i32_load(var0) + 4))
    if (var2 if (1 if var2 < var5 else 0) else i32_load(i32_load(var0) + 4)):
        var6 = i32_load(var0 + 56)
        i32_store(var4 + 4, (var5 - var2))
        var3 = func35((var3 + var6), i32_load(var4), var2)
        # br_table ['$label13', '$label14', '$label15']
        _br_idx = (i32_load(i32_load(var4 + 28) + 24) - 1)
        break  # br_table
        i32_store(var4 + 48, func89(i32_load(var4 + 48), var3, var2))
        break
        i32_store(var4 + 48, func43(i32_load(var4 + 48), var3, var2))
        i32_store(var4, (i32_load(var4) + var2))
        i32_store(var4 + 8, (i32_load(var4 + 8) + var2))
        var3 = (i32_load(var0 + 108) + var2)
        i32_store(var0 + 108, (i32_load(var0 + 108) + var2))
        var4 = i32_load(var0 + 5812)
        var5 = (i32_load(var0 + 44) - i32_load(var0 + 5812))
        i32_store(var0 + 5812, ((var2 if (1 if var2 < var5 else 0) else (i32_load(var0 + 44) - i32_load(var0 + 5812))) + var4))
    if (1 if var3 > i32_load(var0 + 5824) else 0):
        i32_store(var0 + 5824, var3)
    var6 = i32_load(var0 + 92)
    var5 = (var3 - i32_load(var0 + 92))
    var2 = (i32_load(var0 + 12) - ((i32_load(var0 + 5820) + 42) >> 3))
    var4 = (65535 if (1 if var2 >= 65535 else 0) else (i32_load(var0 + 12) - ((i32_load(var0 + 5820) + 42) >> 3)))
    var2 = i32_load(var0 + 44)
    if (1 if (var3 - i32_load(var0 + 92)) < ((65535 if (1 if var2 >= 65535 else 0) else (i32_load(var0 + 12) - ((i32_load(var0 + 5820) + 42) >> 3))) if (1 if var2 > var4 else 0) else i32_load(var0 + 44)) else 0):
        var2 = 0
        if (1 if var1 == 0 else 0):
            break
        if (1 if ((1 if var1 == 4 else 0) | (1 if var3 != var6 else 0)) == 0 else 0):
            break
        if i32_load(i32_load(var0) + 4):
            break
        if (1 if var4 < var5 else 0):
            break
    var2 = 0
    if (1 if var1 == 4 else 0):
        var2 = ((1 if i32_load(i32_load(var0) + 4) == 0 else 0) & (1 if var4 >= var5 else 0))
    var1 = (var5 if (1 if var4 > var5 else 0) else var4)
    i32_store(var0 + 92, (i32_load(var0 + 92) + var1))
    var0 = i32_load(var0)
    var1 = i32_load(i32_load(var0) + 28)
    var3 = i32_load(var1 + 20)
    var4 = i32_load(var0 + 16)
    var3 = (i32_load(var1 + 20) if (1 if var3 < var4 else 0) else i32_load(var0 + 16))
    if (1 if (i32_load(var1 + 20) if (1 if var3 < var4 else 0) else i32_load(var0 + 16)) == 0 else 0):
        break
    i32_store(var0 + 12, (i32_load(var0 + 12) + var3))
    i32_store(var1 + 16, (i32_load(var1 + 16) + var3))
    i32_store(var0 + 20, (i32_load(var0 + 20) + var3))
    i32_store(var0 + 16, (i32_load(var0 + 16) - var3))
    var0 = i32_load(var1 + 20)
    i32_store(var1 + 20, (i32_load(var1 + 20) - var3))
    if (1 if var0 != var3 else 0):
        break
    i32_store(var1 + 16, i32_load(var1 + 8))
    var2 = (2 if var2 else 0)
    return var2

