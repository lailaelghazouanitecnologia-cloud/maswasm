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
# $func44
# ==========================================================
def func44(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var3 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if i32_load(var0 + 92):
        break
    var2 = i32_load(9213808)
    if (1 if i32_load(9213808) > 9999 else 0):
        break
    if (1 if i32_load8_u(var0 + 125) == 3 else 0):
        break
    if (1 if var1 == 0 else 0):
        var1 = i32_load(var0 + 28)
        i32_store(9213808, (var2 + 1))
        i32_store(((var2 << 2) + 9173808), var1)
    var1 = 1
    if (i32_load8_u(9142906) | i32_load8_u(9142916)):
        break
    var1 = 0
    if i32_load8_u(9142917):
        break
    var1 = i32_load(9299880)
    if i32_load(9299880):
        var1 = (var1 - 1)
        i32_store(9299880, (var1 - 1))
        var1 = i32_load((i32_load(9299872) + (var1 << 2)))
        break
    var1 = i32_load(9163776)
    var2 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var4 = i32_load(9163784)
    if (1 if var2 < i32_load(9163784) else 0):
        break
    i32_store(var3, var4)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    i32_store(var0 + 92, var1)
    if (1 if i32_load(var0 + 36) == 0 else 0):
    func203(var0)
    global global0
    global0 = (var3 + 16)


# ==========================================================
# $af
# Export: af
# ==========================================================
def af(var0):
    """Export: af"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if (1 if var0 == 0 else 0):
        break
    if (i32_load8_u(9690908) & 2):
        if func55(9690912):
            break
    var2 = (var0 - 8)
    var1 = i32_load((var0 - 4))
    var0 = (i32_load((var0 - 4)) & -8)
    var5 = ((var0 - 8) + (i32_load((var0 - 4)) & -8))
    if (var1 & 1):
        break
    if (1 if (var1 & 3) == 0 else 0):
        break
    var1 = i32_load(var2)
    var2 = (var2 - i32_load(var2))
    if (1 if (var2 - i32_load(var2)) < i32_load(9690480) else 0):
        break
    var0 = (var0 + var1)
    if (1 if i32_load(9690484) != var2 else 0):
        if (1 if var1 <= 255 else 0):
            var4 = ((var1 & 0xFFFFFFFF) >> 3)
            var1 = i32_load(var2 + 12)
            var3 = i32_load(var2 + 8)
            if (1 if i32_load(var2 + 12) == i32_load(var2 + 8) else 0):
                i32_store(9690464, (i32_load(9690464) & rotl32(-2, var4)))
                break
            i32_store(var3 + 12, var1)
            i32_store(var1 + 8, var3)
            break
        var6 = i32_load(var2 + 24)
        var1 = i32_load(var2 + 12)
        if (1 if var2 != i32_load(var2 + 12) else 0):
            var3 = i32_load(var2 + 8)
            i32_store(i32_load(var2 + 8) + 12, var1)
            i32_store(var1 + 8, var3)
            break
        var3 = (var2 + 20)
        var4 = i32_load((var2 + 20))
        if i32_load((var2 + 20)):
            break
        var3 = (var2 + 16)
        var4 = i32_load((var2 + 16))
        if i32_load((var2 + 16)):
            break
        var1 = 0
        break
        while True:  # loop $label5
            var7 = var3
            var1 = var4
            var3 = (var4 + 20)
            var4 = i32_load((var4 + 20))
            if i32_load((var4 + 20)):
                continue
            var3 = (var1 + 16)
            var4 = i32_load(var1 + 16)
            if i32_load(var1 + 16):
                continue
            break  # end loop
        i32_store(var7, 0)
        if (1 if var6 == 0 else 0):
            break
        var3 = i32_load(var2 + 28)
        var4 = ((i32_load(var2 + 28) << 2) + 9690768)
        if (1 if i32_load(((i32_load(var2 + 28) << 2) + 9690768)) == var2 else 0):
            i32_store(var4, var1)
            if var1:
                break
            i32_store(9690468, (i32_load(9690468) & rotl32(-2, var3)))
            break
        i32_store((var6 + (16 if (1 if i32_load(var6 + 16) == var2 else 0) else 20)), var1)
        if (1 if var1 == 0 else 0):
            break
        i32_store(var1 + 24, var6)
        var3 = i32_load(var2 + 16)
        if i32_load(var2 + 16):
            i32_store(var1 + 16, var3)
            i32_store(var3 + 24, var1)
        var3 = i32_load(var2 + 20)
        if (1 if i32_load(var2 + 20) == 0 else 0):
            break
        i32_store(var1 + 20, var3)
        i32_store(var3 + 24, var1)
        break
    var1 = i32_load(var5 + 4)
    if (1 if (i32_load(var5 + 4) & 3) != 3 else 0):
        break
    i32_store(9690472, var0)
    i32_store(var5 + 4, (var1 & -2))
    i32_store(var2 + 4, (var0 | 1))
    i32_store((var0 + var2), var0)
    break
    if (1 if var2 >= var5 else 0):
        break
    var1 = i32_load(var5 + 4)
    if (1 if (i32_load(var5 + 4) & 1) == 0 else 0):
        break
    if (1 if (var1 & 2) == 0 else 0):
        if (1 if i32_load(9690488) == var5 else 0):
            i32_store(9690488, var2)
            var0 = (i32_load(9690476) + var0)
            i32_store(9690476, (i32_load(9690476) + var0))
            i32_store(var2 + 4, (var0 | 1))
            if (1 if var2 != i32_load(9690484) else 0):
                break
            i32_store(9690472, 0)
            i32_store(9690484, 0)
            break
        if (1 if i32_load(9690484) == var5 else 0):
            i32_store(9690484, var2)
            var0 = (i32_load(9690472) + var0)
            i32_store(9690472, (i32_load(9690472) + var0))
            i32_store(var2 + 4, (var0 | 1))
            i32_store((var0 + var2), var0)
            break
        var0 = ((var1 & -8) + var0)
        if (1 if var1 <= 255 else 0):
            var4 = ((var1 & 0xFFFFFFFF) >> 3)
            var1 = i32_load(var5 + 12)
            var3 = i32_load(var5 + 8)
            if (1 if i32_load(var5 + 12) == i32_load(var5 + 8) else 0):
                i32_store(9690464, (i32_load(9690464) & rotl32(-2, var4)))
                break
            i32_store(var3 + 12, var1)
            i32_store(var1 + 8, var3)
            break
        var6 = i32_load(var5 + 24)
        var1 = i32_load(var5 + 12)
        if (1 if var5 != i32_load(var5 + 12) else 0):
            var3 = i32_load(var5 + 8)
            i32_store(i32_load(var5 + 8) + 12, var1)
            i32_store(var1 + 8, var3)
            break
        var4 = (var5 + 20)
        var3 = i32_load((var5 + 20))
        if i32_load((var5 + 20)):
            break
        var4 = (var5 + 16)
        var3 = i32_load((var5 + 16))
        if i32_load((var5 + 16)):
            break
        var1 = 0
        break
        while True:  # loop $label10
            var7 = var4
            var1 = var3
            var4 = (var3 + 20)
            var3 = i32_load((var3 + 20))
            if i32_load((var3 + 20)):
                continue
            var4 = (var1 + 16)
            var3 = i32_load(var1 + 16)
            if i32_load(var1 + 16):
                continue
            break  # end loop
        i32_store(var7, 0)
        if (1 if var6 == 0 else 0):
            break
        var3 = i32_load(var5 + 28)
        var4 = ((i32_load(var5 + 28) << 2) + 9690768)
        if (1 if i32_load(((i32_load(var5 + 28) << 2) + 9690768)) == var5 else 0):
            i32_store(var4, var1)
            if var1:
                break
            i32_store(9690468, (i32_load(9690468) & rotl32(-2, var3)))
            break
        i32_store((var6 + (16 if (1 if i32_load(var6 + 16) == var5 else 0) else 20)), var1)
        if (1 if var1 == 0 else 0):
            break
        i32_store(var1 + 24, var6)
        var3 = i32_load(var5 + 16)
        if i32_load(var5 + 16):
            i32_store(var1 + 16, var3)
            i32_store(var3 + 24, var1)
        var3 = i32_load(var5 + 20)
        if (1 if i32_load(var5 + 20) == 0 else 0):
            break
        i32_store(var1 + 20, var3)
        i32_store(var3 + 24, var1)
        i32_store(var2 + 4, (var0 | 1))
        i32_store((var0 + var2), var0)
        if (1 if var2 != i32_load(9690484) else 0):
            break
        i32_store(9690472, var0)
        break
    i32_store(var5 + 4, (var1 & -2))
    i32_store(var2 + 4, (var0 | 1))
    i32_store((var0 + var2), var0)
    if (1 if var0 <= 255 else 0):
        var1 = ((var0 & -8) + 9690504)
        var3 = i32_load(9690464)
        var0 = (1 << ((var0 & 0xFFFFFFFF) >> 3))
        if (1 if (i32_load(9690464) & (1 << ((var0 & 0xFFFFFFFF) >> 3))) == 0 else 0):
            i32_store(9690464, (var0 | var3))
            break
        var0 = i32_load(var1 + 8)
        i32_store(var1 + 8, var2)
        i32_store(var0 + 12, var2)
        i32_store(var2 + 12, var1)
        i32_store(var2 + 8, var0)
        break
    var3 = 31
    if (1 if var0 <= 16777215 else 0):
        var1 = clz32(((var0 & 0xFFFFFFFF) >> 8))
        var3 = (((((var0 & 0xFFFFFFFF) >> (38 - clz32(((var0 & 0xFFFFFFFF) >> 8)))) & 1) - (var1 << 1)) + 62)
    i32_store(var2 + 28, var3)
    i64_store(var2 + 16, 0)
    var1 = ((var3 << 2) + 9690768)
    var4 = i32_load(9690468)
    var7 = (1 << var3)
    if (1 if (i32_load(9690468) & (1 << var3)) == 0 else 0):
        i32_store(9690468, (var4 | var7))
        i32_store(var1, var2)
        i32_store(var2 + 24, var1)
        break
    var3 = (var0 << ((25 - ((var3 & 0xFFFFFFFF) >> 1)) if (1 if var3 != 31 else 0) else 0))
    var1 = i32_load(var1)
    while True:  # loop $label16
        var4 = var1
        if (1 if (i32_load(var1 + 4) & -8) == var0 else 0):
            break
        var1 = ((var3 & 0xFFFFFFFF) >> 29)
        var3 = (var3 << 1)
        var7 = (var4 + (var1 & 4))
        var1 = i32_load(((var4 + (var1 & 4)) + 16))
        if i32_load(((var4 + (var1 & 4)) + 16)):
            continue
        break  # end loop
    i32_store(var7 + 16, var2)
    i32_store(var2 + 24, var4)
    i32_store(var2 + 12, var2)
    i32_store(var2 + 8, var2)
    break
    var0 = i32_load(var4 + 8)
    i32_store(i32_load(var4 + 8) + 12, var2)
    i32_store(var4 + 8, var2)
    i32_store(var2 + 24, 0)
    i32_store(var2 + 12, var4)
    i32_store(var2 + 8, var0)
    var0 = (i32_load(9690496) - 1)
    i32_store(9690496, ((i32_load(9690496) - 1) if var0 else -1))
    if (1 if (i32_load8_u(9690908) & 2) == 0 else 0):
        break
    func54(9690912)
    return var1

