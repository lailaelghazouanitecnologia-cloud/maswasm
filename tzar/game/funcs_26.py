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
# $func386
# ==========================================================
def func386(var0):
    var1 = 0
    var2 = 0
    var2 = 1
    if i32_load8_u(9216060):
        break
    var1 = i32_load(i32_load(9142424) + 76)
    # br_table ['$label1', '$label2', '$label3']
    _br_idx = i32_load(i32_load(9142424) + 76)
    break  # br_table
    if i32_load(((var0 + (i32_load(9681856) << 2)) + 281808)):
        break
    if i32_load(((var0 + (i32_load(9681860) << 2)) + 281808)):
        break
    if i32_load(((var0 + (i32_load(9681864) << 2)) + 281808)):
        break
    if i32_load(((var0 + (i32_load(9681868) << 2)) + 281808)):
        break
    if i32_load(((var0 + (i32_load(9681872) << 2)) + 281808)):
        break
    if i32_load(((var0 + (i32_load(9681876) << 2)) + 281808)):
        break
    var1 = 9681880
    break
    if i32_load(((var0 + (i32_load(9681856) << 2)) + 281808)):
        break
    if i32_load(((var0 + (i32_load(9681860) << 2)) + 281808)):
        break
    if i32_load(((var0 + (i32_load(9681864) << 2)) + 281808)):
        break
    var1 = 9681868
    break
    while True:  # loop $label5
        if i32_load(((var0 + (var1 << 2)) + 281808)):
            if (1 if i32_load8_u(((var1 * 404) + 9568096) + 376) == 0 else 0):
                break
        var2 = (1 if var1 < 131 else 0)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != 132 else 0):
            continue
        break  # end loop
    return var2
    return (1 if i32_load(((var0 + (i32_load(var1) << 2)) + 281808)) != 0 else 0)


# ==========================================================
# $func392
# ==========================================================
def func392(var0, var1):
    var2 = 0
    var3 = 0
    var2 = i32_load(var1 + 44)
    var3 = (i32_load(var1 + 36) + (i32_load(var1 + 44) * 12))
    i64_store(var0, i64_load((i32_load(var1 + 36) + (i32_load(var1 + 44) * 12))))
    i32_store(var0 + 8, i32_load(var3 + 8))
    i32_store(var1 + 44, ((var2 + 1) % i32_load(var1 + 40)))


# ==========================================================
# $func396
# ==========================================================
def func396(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var5 = (var0 + var1)
    var2 = i32_load(var0 + 4)
    if (i32_load(var0 + 4) & 1):
        break
    if (1 if (var2 & 3) == 0 else 0):
        break
    var2 = i32_load(var0)
    var1 = (i32_load(var0) + var1)
    var0 = (var0 - var2)
    if (1 if (var0 - var2) != i32_load(9690484) else 0):
        if (1 if var2 <= 255 else 0):
            var2 = ((var2 & 0xFFFFFFFF) >> 3)
            var4 = i32_load(var0 + 8)
            var3 = i32_load(var0 + 12)
            if (1 if i32_load(var0 + 8) != i32_load(var0 + 12) else 0):
                break
            i32_store(9690464, (i32_load(9690464) & rotl32(-2, var2)))
            break
        var6 = i32_load(var0 + 24)
        var2 = i32_load(var0 + 12)
        if (1 if var0 != i32_load(var0 + 12) else 0):
            var3 = i32_load(var0 + 8)
            i32_store(i32_load(var0 + 8) + 12, var2)
            i32_store(var2 + 8, var3)
            break
        var4 = (var0 + 20)
        var3 = i32_load((var0 + 20))
        if i32_load((var0 + 20)):
            break
        var4 = (var0 + 16)
        var3 = i32_load((var0 + 16))
        if i32_load((var0 + 16)):
            break
        var2 = 0
        break
        while True:  # loop $label5
            var7 = var4
            var2 = var3
            var4 = (var3 + 20)
            var3 = i32_load((var3 + 20))
            if i32_load((var3 + 20)):
                continue
            var4 = (var2 + 16)
            var3 = i32_load(var2 + 16)
            if i32_load(var2 + 16):
                continue
            break  # end loop
        i32_store(var7, 0)
        if (1 if var6 == 0 else 0):
            break
        var4 = i32_load(var0 + 28)
        var3 = ((i32_load(var0 + 28) << 2) + 9690768)
        if (1 if i32_load(((i32_load(var0 + 28) << 2) + 9690768)) == var0 else 0):
            i32_store(var3, var2)
            if var2:
                break
            i32_store(9690468, (i32_load(9690468) & rotl32(-2, var4)))
            break
        i32_store((var6 + (16 if (1 if i32_load(var6 + 16) == var0 else 0) else 20)), var2)
        if (1 if var2 == 0 else 0):
            break
        i32_store(var2 + 24, var6)
        var3 = i32_load(var0 + 16)
        if i32_load(var0 + 16):
            i32_store(var2 + 16, var3)
            i32_store(var3 + 24, var2)
        var3 = i32_load(var0 + 20)
        if (1 if i32_load(var0 + 20) == 0 else 0):
            break
        i32_store(var2 + 20, var3)
        i32_store(var3 + 24, var2)
        break
    var2 = i32_load(var5 + 4)
    if (1 if (i32_load(var5 + 4) & 3) != 3 else 0):
        break
    i32_store(9690472, var1)
    i32_store(var5 + 4, (var2 & -2))
    i32_store(var0 + 4, (var1 | 1))
    i32_store(var5, var1)
    return
    i32_store(var4 + 12, var3)
    i32_store(var3 + 8, var4)
    var2 = i32_load(var5 + 4)
    if (1 if (i32_load(var5 + 4) & 2) == 0 else 0):
        if (1 if i32_load(9690488) == var5 else 0):
            i32_store(9690488, var0)
            var1 = (i32_load(9690476) + var1)
            i32_store(9690476, (i32_load(9690476) + var1))
            i32_store(var0 + 4, (var1 | 1))
            if (1 if var0 != i32_load(9690484) else 0):
                break
            i32_store(9690472, 0)
            i32_store(9690484, 0)
            return
        if (1 if i32_load(9690484) == var5 else 0):
            i32_store(9690484, var0)
            var1 = (i32_load(9690472) + var1)
            i32_store(9690472, (i32_load(9690472) + var1))
            i32_store(var0 + 4, (var1 | 1))
            i32_store((var0 + var1), var1)
            return
        var1 = ((var2 & -8) + var1)
        if (1 if var2 <= 255 else 0):
            var2 = ((var2 & 0xFFFFFFFF) >> 3)
            var3 = i32_load(var5 + 12)
            var4 = i32_load(var5 + 8)
            if (1 if i32_load(var5 + 12) == i32_load(var5 + 8) else 0):
                i32_store(9690464, (i32_load(9690464) & rotl32(-2, var2)))
                break
            i32_store(var4 + 12, var3)
            i32_store(var3 + 8, var4)
            break
        var6 = i32_load(var5 + 24)
        var2 = i32_load(var5 + 12)
        if (1 if var5 != i32_load(var5 + 12) else 0):
            var3 = i32_load(var5 + 8)
            i32_store(i32_load(var5 + 8) + 12, var2)
            i32_store(var2 + 8, var3)
            break
        var3 = (var5 + 20)
        var4 = i32_load((var5 + 20))
        if i32_load((var5 + 20)):
            break
        var3 = (var5 + 16)
        var4 = i32_load((var5 + 16))
        if i32_load((var5 + 16)):
            break
        var2 = 0
        break
        while True:  # loop $label10
            var7 = var3
            var2 = var4
            var3 = (var4 + 20)
            var4 = i32_load((var4 + 20))
            if i32_load((var4 + 20)):
                continue
            var3 = (var2 + 16)
            var4 = i32_load(var2 + 16)
            if i32_load(var2 + 16):
                continue
            break  # end loop
        i32_store(var7, 0)
        if (1 if var6 == 0 else 0):
            break
        var4 = i32_load(var5 + 28)
        var3 = ((i32_load(var5 + 28) << 2) + 9690768)
        if (1 if i32_load(((i32_load(var5 + 28) << 2) + 9690768)) == var5 else 0):
            i32_store(var3, var2)
            if var2:
                break
            i32_store(9690468, (i32_load(9690468) & rotl32(-2, var4)))
            break
        i32_store((var6 + (16 if (1 if i32_load(var6 + 16) == var5 else 0) else 20)), var2)
        if (1 if var2 == 0 else 0):
            break
        i32_store(var2 + 24, var6)
        var3 = i32_load(var5 + 16)
        if i32_load(var5 + 16):
            i32_store(var2 + 16, var3)
            i32_store(var3 + 24, var2)
        var3 = i32_load(var5 + 20)
        if (1 if i32_load(var5 + 20) == 0 else 0):
            break
        i32_store(var2 + 20, var3)
        i32_store(var3 + 24, var2)
        i32_store(var0 + 4, (var1 | 1))
        i32_store((var0 + var1), var1)
        if (1 if var0 != i32_load(9690484) else 0):
            break
        i32_store(9690472, var1)
        return
    i32_store(var5 + 4, (var2 & -2))
    i32_store(var0 + 4, (var1 | 1))
    i32_store((var0 + var1), var1)
    if (1 if var1 <= 255 else 0):
        var2 = ((var1 & -8) + 9690504)
        var3 = i32_load(9690464)
        var1 = (1 << ((var1 & 0xFFFFFFFF) >> 3))
        if (1 if (i32_load(9690464) & (1 << ((var1 & 0xFFFFFFFF) >> 3))) == 0 else 0):
            i32_store(9690464, (var1 | var3))
            break
        var1 = i32_load(var2 + 8)
        i32_store(var2 + 8, var0)
        i32_store(var1 + 12, var0)
        i32_store(var0 + 12, var2)
        i32_store(var0 + 8, var1)
        return var2
    var4 = 31
    if (1 if var1 <= 16777215 else 0):
        var2 = clz32(((var1 & 0xFFFFFFFF) >> 8))
        var4 = (((((var1 & 0xFFFFFFFF) >> (38 - clz32(((var1 & 0xFFFFFFFF) >> 8)))) & 1) - (var2 << 1)) + 62)
    i32_store(var0 + 28, var4)
    i64_store(var0 + 16, 0)
    var7 = ((var4 << 2) + 9690768)
    var3 = i32_load(9690468)
    var2 = (1 << var4)
    if (1 if (i32_load(9690468) & (1 << var4)) == 0 else 0):
        i32_store(9690468, (var2 | var3))
        i32_store(var7, var0)
        i32_store(var0 + 24, var7)
        break
    var4 = (var1 << ((25 - ((var4 & 0xFFFFFFFF) >> 1)) if (1 if var4 != 31 else 0) else 0))
    var2 = i32_load(var7)
    while True:  # loop $label16
        var3 = var2
        if (1 if (i32_load(var2 + 4) & -8) == var1 else 0):
            break
        var2 = ((var4 & 0xFFFFFFFF) >> 29)
        var4 = (var4 << 1)
        var7 = (var3 + (var2 & 4))
        var2 = i32_load(((var3 + (var2 & 4)) + 16))
        if i32_load(((var3 + (var2 & 4)) + 16)):
            continue
        break  # end loop
    i32_store(var7 + 16, var0)
    i32_store(var0 + 24, var3)
    i32_store(var0 + 12, var0)
    i32_store(var0 + 8, var0)
    return
    var1 = i32_load(var3 + 8)
    i32_store(i32_load(var3 + 8) + 12, var0)
    i32_store(var3 + 8, var0)
    i32_store(var0 + 24, 0)
    i32_store(var0 + 12, var3)
    i32_store(var0 + 8, var1)
    return 0  # Stack underflow


# ==========================================================
# $func400
# ==========================================================
def func400(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    if (1 if var0 == 0 else 0):
        break
    if (1 if i32_load(var0 + 32) == 0 else 0):
        break
    var2 = i32_load(var0 + 36)
    if (1 if i32_load(var0 + 36) == 0 else 0):
        break
    var1 = i32_load(var0 + 28)
    if (1 if i32_load(var0 + 28) == 0 else 0):
        break
    if (1 if i32_load(var1) != var0 else 0):
        break
    var3 = i32_load(var1 + 4)
    # br_table ['$label1', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label1', '$label0', '$label0', '$label0', '$label1', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label1', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label1', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label1', '$label2']
    _br_idx = (i32_load(var1 + 4) - 57)
    break  # br_table
    if (1 if var3 == 666 else 0):
        break
    if (1 if var3 != 42 else 0):
        break
    var3 = i32_load(var1 + 8)
    if i32_load(var1 + 8):
        # call_indirect via table[var2]
        var1 = i32_load(var0 + 28)
    var2 = i32_load(var1 + 68)
    if i32_load(var1 + 68):
        # call_indirect via table[i32_load(var0 + 36)]
        var1 = i32_load(var0 + 28)
    var2 = i32_load(var1 + 64)
    if i32_load(var1 + 64):
        # call_indirect via table[i32_load(var0 + 36)]
        var1 = i32_load(var0 + 28)
    var2 = i32_load(var1 + 56)
    if i32_load(var1 + 56):
        # call_indirect via table[i32_load(var0 + 36)]
        var1 = i32_load(var0 + 28)
    # call_indirect via table[i32_load(var0 + 36)]
    i32_store(var0 + 28, 0)

