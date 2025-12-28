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
# $func367
# ==========================================================
def func367(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var2 = (var0 + 148)
    while True:  # loop $label0
        var3 = (var1 << 2)
        i32_store16((var2 + (var1 << 2)), 0)
        i32_store16((var2 + (var3 | 4)), 0)
        var1 = (var1 + 2)
        if (1 if (var1 + 2) != 286 else 0):
            continue
        break  # end loop
    i32_store16(var0 + 2684, 0)
    i32_store16(var0 + 2440, 0)
    i32_store16((var0 + 2756), 0)
    i32_store16((var0 + 2752), 0)
    i32_store16((var0 + 2748), 0)
    i32_store16((var0 + 2744), 0)
    i32_store16((var0 + 2740), 0)
    i32_store16((var0 + 2736), 0)
    i32_store16((var0 + 2732), 0)
    i32_store16((var0 + 2728), 0)
    i32_store16((var0 + 2724), 0)
    i32_store16((var0 + 2720), 0)
    i32_store16((var0 + 2716), 0)
    i32_store16((var0 + 2712), 0)
    i32_store16((var0 + 2708), 0)
    i32_store16((var0 + 2704), 0)
    i32_store16((var0 + 2700), 0)
    i32_store16((var0 + 2696), 0)
    i32_store16((var0 + 2692), 0)
    i32_store16((var0 + 2688), 0)
    i32_store16((var0 + 2556), 0)
    i32_store16((var0 + 2552), 0)
    i32_store16((var0 + 2548), 0)
    i32_store16((var0 + 2544), 0)
    i32_store16((var0 + 2540), 0)
    i32_store16((var0 + 2536), 0)
    i32_store16((var0 + 2532), 0)
    i32_store16((var0 + 2528), 0)
    i32_store16((var0 + 2524), 0)
    i32_store16((var0 + 2520), 0)
    i32_store16((var0 + 2516), 0)
    i32_store16((var0 + 2512), 0)
    i32_store16((var0 + 2508), 0)
    i32_store16((var0 + 2504), 0)
    i32_store16((var0 + 2500), 0)
    i32_store16((var0 + 2496), 0)
    i32_store16((var0 + 2492), 0)
    i32_store16((var0 + 2488), 0)
    i32_store16((var0 + 2484), 0)
    i32_store16((var0 + 2480), 0)
    i32_store16((var0 + 2476), 0)
    i32_store16((var0 + 2472), 0)
    i32_store16((var0 + 2468), 0)
    i32_store16((var0 + 2464), 0)
    i32_store16((var0 + 2460), 0)
    i32_store16((var0 + 2456), 0)
    i32_store16((var0 + 2452), 0)
    i32_store16((var0 + 2448), 0)
    i32_store16((var0 + 2444), 0)
    i64_store(var0 + 5804, 0)
    i32_store16((var0 + 1172), 1)
    i32_store(var0 + 5800, 0)
    i32_store(var0 + 5792, 0)


# ==========================================================
# $func371
# ==========================================================
def func371(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    if (1 if (i32_load8_s(i32_load(var0)) - 48) >= 10 else 0):
        return 0
    while True:  # loop $label0
        var3 = i32_load(var0)
        var1 = -1
        if (1 if var2 <= 214748364 else 0):
            var1 = (i32_load8_s(var3) - 48)
            var2 = (var2 * 10)
            var1 = (-1 if (1 if var1 > (var2 ^ 2147483647) else 0) else ((i32_load8_s(var3) - 48) + (var2 * 10)))
        i32_store(var0, (var3 + 1))
        var2 = var1
        if (1 if (i32_load8_s(var3 + 1) - 48) < 10 else 0):
            continue
        break  # end loop
    return var2


# ==========================================================
# $func372
# ==========================================================
def func372(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var2 = i32_load(var0 + 28)
    if (1 if i32_load(var0 + 28) <= 0 else 0):
        break
    var3 = i32_load(var0 + 24)
    var0 = 0
    while True:  # loop $label1
        var4 = i32_load((var3 + (var0 << 2)))
        if (1 if var1 != i32_load(i32_load((var3 + (var0 << 2))) + 28) else 0):
            var0 = (var0 + 1)
            if (1 if var2 != (var0 + 1) else 0):
                continue
            break
        break  # end loop
    return var4
    return 0


# ==========================================================
# $func373
# ==========================================================
def func373(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var6 = (var0 + 1)
    var8 = i32_load(9147288)
    var3 = i32_load(9142440)
    var10 = (1 if i32_load(9142440) <= var1 else 0)
    if (1 if i32_load(9142440) <= var1 else 0):
        break
    if (1 if var3 <= var6 else 0):
        break
    if (1 if (var1 | var6) < 0 else 0):
        break
    var4 = i32_load8_s((var8 + ((var1 * var3) + var6)))
    if (1 if i32_load8_s((var8 + ((var1 * var3) + var6))) < 0 else 0):
        break
    if (1 if var2 != var4 else 0):
        break
    var5 = (var1 - 1)
    var9 = (1 if var3 <= (var1 - 1) else 0)
    if (1 if var3 <= (var1 - 1) else 0):
        break
    if (1 if var3 <= var6 else 0):
        break
    if (1 if (var5 | var6) < 0 else 0):
        break
    var4 = i32_load8_s((var8 + ((var3 * var5) + var6)))
    if (1 if i32_load8_s((var8 + ((var3 * var5) + var6))) < 0 else 0):
        break
    if (1 if var2 != var4 else 0):
        break
    if var9:
        break
    if (1 if var0 >= var3 else 0):
        break
    if (1 if (var0 | var5) < 0 else 0):
        break
    var4 = i32_load8_s((var8 + ((var3 * var5) + var0)))
    if (1 if i32_load8_s((var8 + ((var3 * var5) + var0))) < 0 else 0):
        break
    if (1 if var2 != var4 else 0):
        break
    var7 = (var0 - 1)
    if var9:
        break
    if (1 if var3 <= var7 else 0):
        break
    if (1 if (var5 | var7) < 0 else 0):
        break
    var4 = i32_load8_s((var8 + ((var3 * var5) + var7)))
    if (1 if i32_load8_s((var8 + ((var3 * var5) + var7))) < 0 else 0):
        break
    if (1 if var2 != var4 else 0):
        break
    if var10:
        break
    if (1 if var3 <= var7 else 0):
        break
    if (1 if (var1 | var7) < 0 else 0):
        break
    var4 = i32_load8_s((var8 + ((var1 * var3) + var7)))
    if (1 if i32_load8_s((var8 + ((var1 * var3) + var7))) < 0 else 0):
        break
    if (1 if var2 != var4 else 0):
        break
    var5 = (var1 + 1)
    var9 = (1 if var3 <= (var1 + 1) else 0)
    if (1 if var3 <= (var1 + 1) else 0):
        break
    if (1 if var3 <= var7 else 0):
        break
    if (1 if (var5 | var7) < 0 else 0):
        break
    var4 = i32_load8_s((var8 + ((var3 * var5) + var7)))
    if (1 if i32_load8_s((var8 + ((var3 * var5) + var7))) < 0 else 0):
        break
    if (1 if var2 != var4 else 0):
        break
    if var9:
        break
    if (1 if var0 >= var3 else 0):
        break
    if (1 if (var0 | var5) < 0 else 0):
        break
    var4 = i32_load8_s((var8 + ((var3 * var5) + var0)))
    if (1 if i32_load8_s((var8 + ((var3 * var5) + var0))) < 0 else 0):
        break
    if (1 if var2 != var4 else 0):
        break
    var1 = -1
    if var9:
        break
    if (1 if var3 <= var6 else 0):
        break
    if (1 if (var5 | var6) < 0 else 0):
        break
    var4 = i32_load8_s((var8 + ((var3 * var5) + var6)))
    if (1 if i32_load8_s((var8 + ((var3 * var5) + var6))) < 0 else 0):
        break
    if (1 if var2 == var4 else 0):
        break
    var1 = var4
    return var1


# ==========================================================
# $func382
# ==========================================================
def func382(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var3 = i32_load(var0)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load(var0 + 4)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load(var0 + 8)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load(var0 + 12)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load(var0 + 16)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load(var0 + 20)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load(var0 + 24)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load(var0 + 28)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load(var0 + 32)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load(var0 + 36)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load(var0 + 40)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load8_u(var0 + 44)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load8_u(var0 + 45)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load8_u(var0 + 46)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load(var0 + 192)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    if i32_load(var0 + 192):
        var3 = 0
        while True:  # loop $label0
            var4 = i32_load16_u((var0 + (var3 << 1)) + 112)
            var5 = i32_load(var2)
            i32_store(var2, (i32_load(var2) + 1))
            i32_store((var1 + (var5 << 2)), var4)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) < i32_load(var0 + 192) else 0):
                continue
            break  # end loop
    var3 = i32_load(var0 + 56)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    if i32_load(var0 + 56):
        var4 = i32_load(var0 + 48)
        var3 = 0
        while True:  # loop $label1
            var5 = i32_load((var4 + (var3 << 2)))
            var6 = i32_load(var2)
            i32_store(var2, (i32_load(var2) + 1))
            i32_store((var1 + (var6 << 2)), var5)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) < i32_load(var0 + 56) else 0):
                continue
            break  # end loop
    var3 = i32_load(var0 + 72)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    if i32_load(var0 + 72):
        var4 = i32_load(var0 + 64)
        var3 = 0
        while True:  # loop $label2
            var5 = i32_load((var4 + (var3 << 2)))
            var6 = i32_load(var2)
            i32_store(var2, (i32_load(var2) + 1))
            i32_store((var1 + (var6 << 2)), var5)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) < i32_load(var0 + 72) else 0):
                continue
            break  # end loop
    var3 = i32_load(var0 + 88)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    if i32_load(var0 + 88):
        var4 = i32_load(var0 + 80)
        var3 = 0
        while True:  # loop $label3
            var5 = i32_load((var4 + (var3 << 2)))
            var6 = i32_load(var2)
            i32_store(var2, (i32_load(var2) + 1))
            i32_store((var1 + (var6 << 2)), var5)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) < i32_load(var0 + 88) else 0):
                continue
            break  # end loop
    var3 = i32_load(var0 + 104)
    var4 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    if i32_load(var0 + 104):
        var4 = i32_load(var0 + 96)
        var3 = 0
        while True:  # loop $label4
            var5 = i32_load((var4 + (var3 << 2)))
            var6 = i32_load(var2)
            i32_store(var2, (i32_load(var2) + 1))
            i32_store((var1 + (var6 << 2)), var5)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) < i32_load(var0 + 104) else 0):
                continue
            break  # end loop


# ==========================================================
# $func385
# ==========================================================
def func385(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var3 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var2 = 1
    var4 = (var3 - 1)
    var7 = ((var3 - 1) & 1)
    var0 = i32_load(var0 + 283908)
    var5 = (i32_load(var0 + 283908) * var3)
    var6 = i32_load(9143004)
    if (1 if var3 != 2 else 0):
        var4 = (var4 & -2)
        var3 = 0
        while True:  # loop $label1
            var1 = (var2 + 1)
            var1 = ((var1 + ((1 if i32_load8_u((var6 + (var2 + var5))) == 0 else 0) & (1 if var0 != var2 else 0))) + ((1 if i32_load8_u((var6 + (var5 + (var2 + 1)))) == 0 else 0) & (1 if var0 != var1 else 0)))
            var2 = (var2 + 2)
            var3 = (var3 + 2)
            if (1 if (var3 + 2) != var4 else 0):
                continue
            break  # end loop
    if (1 if var7 == 0 else 0):
        break
    var1 = (var1 + ((1 if i32_load8_u((var6 + (var2 + var5))) == 0 else 0) & (1 if var0 != var2 else 0)))
    return var1

