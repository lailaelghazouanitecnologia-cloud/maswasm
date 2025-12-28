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
# $Yd
# Export: Yd
# ==========================================================
def Yd():
    """Export: Yd"""
    var0 = 0
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
    while True:  # loop $label1
        var1 = ((var2 * 404) + 9568096)
        if (1 if i32_load(((var2 * 404) + 9568096) + 264) != 3 else 0):
            break
        if (1 if i32_load(var1 + 180) == 0 else 0):
            break
        var0 = ((i32_load(var1 + 236) + (var0 + i32_load(var1 + 244))) + 23)
        var6 = (var6 + 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != 255 else 0):
            continue
        break  # end loop
    var1 = i32_load(9685864)
    if i32_load(9685864):
        i32_store(9685864, 0)
    var2 = (var6 * 23)
    var6 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    i32_store(9685864, func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2))))
    while True:  # loop $label12
        var1 = ((var11 * 404) + 9568096)
        if (1 if i32_load(((var11 * 404) + 9568096) + 264) != 3 else 0):
            break
        if (1 if i32_load(var1 + 180) == 0 else 0):
            break
        var19 = i64_load(var1 + 72)
        var8 = i32_load(var1 + 112)
        var7 = i32_load(var1 + 120)
        var9 = i32_load(var1 + 100)
        var10 = i32_load(var1 + 92)
        var12 = i32_load(var1 + 104)
        var14 = i32_load(var1 + 212)
        var15 = i32_load8_u(var1 + 354)
        var5 = i32_load(var1 + 236)
        var16 = i32_load(var1 + 80)
        var4 = i32_load(var1 + 244)
        var17 = i32_load(var1 + 116)
        var18 = i32_load(var1 + 68)
        var0 = (var6 + (var13 * 92))
        var3 = i32_load(var1 + 368)
        if (1 if i32_load(var1 + 368) == 60 else 0):
            break
        if (1 if var3 == 61 else 0):
            break
        if (1 if var3 == 63 else 0):
            break
        if (1 if var3 == 62 else 0):
            break
        if (1 if var3 == 55 else 0):
            break
        i32_store((var6 + (var13 * 92)) + 4, (6 if var3 else 5))
        i32_store(var0 + 8, var18)
        i32_store(var0 + 12, var17)
        i32_store(var0 + 16, var4)
        i32_store(var0 + 28, var16)
        i32_store(var0 + 32, var5)
        i32_store(var0 + 36, var15)
        i32_store(var0 + 40, var14)
        i32_store(var0 + 44, var12)
        i32_store(var0 + 48, var10)
        i32_store(var0 + 52, var9)
        i32_store(var0 + 56, var7)
        i64_store(var0 + 64, 0)
        i32_store(var0 + 60, var8)
        i64_store(var0 + 20, var19)
        i64_store(var0 + 72, 0)
        i64_store(var0 + 80, 0)
        i32_store(var0 + 88, 0)
        i32_store(var0, var11)
        if (1 if var4 == 0 else 0):
            break
        var10 = (var4 & 3)
        var3 = i32_load(var1 + 240)
        var8 = 0
        if (1 if var4 < 4 else 0):
            var0 = 0
            break
        var12 = (var4 & -4)
        var0 = 0
        var4 = 0
        while True:  # loop $label6
            var7 = (var6 + (var2 << 2))
            var9 = (var0 << 2)
            i32_store((var6 + (var2 << 2)), i32_load((var3 + (var0 << 2))))
            i32_store(var7 + 4, i32_load((var3 + (var9 | 4))))
            i32_store(var7 + 8, i32_load((var3 + (var9 | 8))))
            i32_store(var7 + 12, i32_load((var3 + (var9 | 12))))
            var0 = (var0 + 4)
            var2 = (var2 + 4)
            var4 = (var4 + 4)
            if (1 if (var4 + 4) != var12 else 0):
                continue
            break  # end loop
        if (1 if var10 == 0 else 0):
            break
        while True:  # loop $label7
            i32_store((var6 + (var2 << 2)), i32_load((var3 + (var0 << 2))))
            var0 = (var0 + 1)
            var2 = (var2 + 1)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != var10 else 0):
                continue
            break  # end loop
        if (1 if var5 == 0 else 0):
            break
        var7 = (var5 & 3)
        var1 = i32_load(var1 + 232)
        var8 = 0
        if (1 if var5 < 4 else 0):
            var0 = 0
            break
        var9 = (var5 & -4)
        var0 = 0
        var4 = 0
        while True:  # loop $label10
            var5 = (var6 + (var2 << 2))
            var3 = (var0 << 2)
            i32_store((var6 + (var2 << 2)), i32_load((var1 + (var0 << 2))))
            i32_store(var5 + 4, i32_load((var1 + (var3 | 4))))
            i32_store(var5 + 8, i32_load((var1 + (var3 | 8))))
            i32_store(var5 + 12, i32_load((var1 + (var3 | 12))))
            var0 = (var0 + 4)
            var2 = (var2 + 4)
            var4 = (var4 + 4)
            if (1 if (var4 + 4) != var9 else 0):
                continue
            break  # end loop
        if (1 if var7 == 0 else 0):
            break
        while True:  # loop $label11
            i32_store((var6 + (var2 << 2)), i32_load((var1 + (var0 << 2))))
            var0 = (var0 + 1)
            var2 = (var2 + 1)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != var7 else 0):
                continue
            break  # end loop
        var13 = (var13 + 1)
        var11 = (var11 + 1)
        if (1 if (var11 + 1) != 255 else 0):
            continue
        break  # end loop
    return (var13 * 23)


# ==========================================================
# $ne
# Export: ne
# ==========================================================
def ne(var0):
    """Export: ne"""
    var1 = 0
    var1 = i32_load(9681976)
    if i32_load(9681976):
        i32_store(9681976, 0)
    var1 = func26(524288000)
    # Unknown: memory.fill []
    i32_store(9687220, var1)
    i32_store(9681976, var1)
    i32_store(9687228, 4)
    i32_store(9687224, ((var0 * 60) + 16))
    i32_store(var1, var0)

