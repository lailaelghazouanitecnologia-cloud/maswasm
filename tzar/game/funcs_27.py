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
# $func406
# ==========================================================
def func406(var0, var1, var2):
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
    if (1 if i32_load(var0 + 5792) == 0 else 0):
        var3 = i32_load(var0 + 5820)
        break
    var9 = (var0 + 5817)
    while True:  # loop $label6
        var11 = (var4 + 3)
        var4 = (i32_load(var0 + 5784) + var4)
        var5 = i32_load8_u((i32_load(var0 + 5784) + var4) + 2)
        var6 = i32_load16_u(var4)
        if (1 if i32_load16_u(var4) == 0 else 0):
            var3 = (var1 + (var5 << 2))
            var4 = i32_load16_u((var1 + (var5 << 2)) + 2)
            var5 = i32_load16_u(var3)
            var3 = i32_load(var0 + 5820)
            var6 = (i32_load16_u(var0 + 5816) | (i32_load16_u(var3) << i32_load(var0 + 5820)))
            i32_store16(var0 + 5816, (i32_load16_u(var0 + 5816) | (i32_load16_u(var3) << i32_load(var0 + 5820))))
            if (1 if (16 - var4) < var3 else 0):
                var3 = i32_load(var0 + 20)
                i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                i32_store8((var3 + i32_load(var0 + 8)), var6)
                var3 = i32_load(var0 + 20)
                i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                i32_store8((var3 + i32_load(var0 + 8)), i32_load8_u(var9))
                var3 = i32_load(var0 + 5820)
                i32_store16(var0 + 5816, ((var5 & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
                break
            break
        var10 = i32_load8_u((var5 + 23984))
        var7 = (i32_load8_u((var5 + 23984)) << 2)
        var4 = ((i32_load8_u((var5 + 23984)) << 2) + var1)
        var3 = i32_load16_u((((i32_load8_u((var5 + 23984)) << 2) + var1) + 1030))
        var12 = i32_load16_u((var4 + 1028))
        var8 = i32_load(var0 + 5820)
        var4 = (i32_load16_u(var0 + 5816) | (i32_load16_u((var4 + 1028)) << i32_load(var0 + 5820)))
        i32_store16(var0 + 5816, (i32_load16_u(var0 + 5816) | (i32_load16_u((var4 + 1028)) << i32_load(var0 + 5820))))
        if (1 if (16 - var3) < var8 else 0):
            var8 = i32_load(var0 + 20)
            i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
            i32_store8((var8 + i32_load(var0 + 8)), var4)
            var4 = i32_load(var0 + 20)
            i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
            i32_store8((var4 + i32_load(var0 + 8)), i32_load8_u(var9))
            var8 = i32_load(var0 + 5820)
            var4 = ((var12 & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820)))
            i32_store16(var0 + 5816, ((var12 & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
            break
        var3 = (var3 + var8)
        i32_store(((var3 + var8) - 16) + 5820, (var3 + var8))
        if (1 if (var10 - 28) >= -20 else 0):
            var5 = (var5 - i32_load((var7 + 25952)))
            var7 = i32_load((var7 + 25584))
            if (1 if (16 - i32_load((var7 + 25584))) < var3 else 0):
                var4 = (var4 | (var5 << var3))
                i32_store16(var0 + 5816, (var4 | (var5 << var3)))
                var3 = i32_load(var0 + 20)
                i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                i32_store8((var3 + i32_load(var0 + 8)), var4)
                var4 = i32_load(var0 + 20)
                i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                i32_store8((var4 + i32_load(var0 + 8)), i32_load8_u(var9))
                var3 = i32_load(var0 + 5820)
                var4 = (((var5 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820)))
                i32_store16(var0 + 5816, (((var5 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
                break
            var4 = (var4 | (var5 << var3))
            i32_store16(var0 + 5816, (var4 | (var5 << var3)))
            var3 = (var3 + var7)
            i32_store(((var3 + var7) - 16) + 5820, (var3 + var7))
        var7 = (var6 - 1)
        var8 = i32_load8_u((((var6 - 1) if (1 if var6 < 257 else 0) else (((var7 & 0xFFFFFFFF) >> 7) + 256)) + 23472))
        var6 = (i32_load8_u((((var6 - 1) if (1 if var6 < 257 else 0) else (((var7 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)
        var10 = (var2 + (i32_load8_u((((var6 - 1) if (1 if var6 < 257 else 0) else (((var7 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2))
        var5 = i32_load16_u((var2 + (i32_load8_u((((var6 - 1) if (1 if var6 < 257 else 0) else (((var7 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2)
        var10 = i32_load16_u(var10)
        var4 = (var4 | (i32_load16_u(var10) << var3))
        i32_store16(var0 + 5816, (var4 | (i32_load16_u(var10) << var3)))
        if (1 if (16 - var5) < var3 else 0):
            var3 = i32_load(var0 + 20)
            i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
            i32_store8((var3 + i32_load(var0 + 8)), var4)
            var4 = i32_load(var0 + 20)
            i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
            i32_store8((var4 + i32_load(var0 + 8)), i32_load8_u(var9))
            var3 = i32_load(var0 + 5820)
            var4 = ((var10 & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820)))
            i32_store16(var0 + 5816, ((var10 & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
            break
        var3 = (var3 + var5)
        i32_store(((var3 + var5) - 16) + 5820, (var3 + var5))
        if (1 if var8 < 4 else 0):
            break
        var5 = (var7 - i32_load((var6 + 26080)))
        var6 = i32_load((var6 + 25712))
        if (1 if (16 - i32_load((var6 + 25712))) < var3 else 0):
            var4 = (var4 | (var5 << var3))
            i32_store16(var0 + 5816, (var4 | (var5 << var3)))
            var3 = i32_load(var0 + 20)
            i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
            i32_store8((var3 + i32_load(var0 + 8)), var4)
            var4 = i32_load(var0 + 20)
            i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
            i32_store8((var4 + i32_load(var0 + 8)), i32_load8_u(var9))
            var4 = i32_load(var0 + 5820)
            i32_store16(var0 + 5816, (((var5 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
            break
        i32_store16(var0 + 5816, (var4 | (var5 << var3)))
        var3 = (var3 + var6)
        i32_store(((var4 + var6) - 16) + 5820, (var3 + var6))
        var4 = var11
        if (1 if var11 < i32_load(var0 + 5792) else 0):
            continue
        break  # end loop
    var2 = i32_load16_u((var1 + 1026))
    var1 = i32_load16_u(var1 + 1024)
    var4 = (i32_load16_u(var0 + 5816) | (i32_load16_u(var1 + 1024) << var3))
    i32_store16(var0 + 5816, (i32_load16_u(var0 + 5816) | (i32_load16_u(var1 + 1024) << var3)))
    if (1 if (16 - var2) < var3 else 0):
        var11 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var11 + i32_load(var0 + 8)), var4)
        var4 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var4 + i32_load(var0 + 8)), i32_load8_u((var0 + 5817)))
        var1 = i32_load(var0 + 5820)
        i32_store16(var0 + 5816, ((var1 & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
        i32_store(var0 + 5820, ((var1 + var2) - 16))
        return var0
    i32_store(var0 + 5820, (var2 + var3))
    return var0


# ==========================================================
# $func410
# ==========================================================
def func410(var0, var1):
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
    var22 = 0
    var5 = i32_load(9147288)
    var3 = i32_load(9142440)
    var9 = ((var0 & 0xFFFFFFFF) // i32_load(9142440))
    var7 = (((var0 & 0xFFFFFFFF) // i32_load(9142440)) + 1)
    var6 = ((((var0 & 0xFFFFFFFF) // i32_load(9142440)) + 1) * var3)
    var10 = (var3 * var9)
    var4 = (var0 - (var3 * var9))
    var14 = (i32_load(9147288) + (((((var0 & 0xFFFFFFFF) // i32_load(9142440)) + 1) * var3) + (var0 - (var3 * var9))))
    var8 = (var9 - 1)
    var11 = ((var9 - 1) * var3)
    var15 = (var5 + (((var9 - 1) * var3) + var4))
    var12 = (1 if var3 > var7 else 0)
    var16 = ((1 if var3 > var7 else 0) & (1 if (var4 | var7) >= 0 else 0))
    var0 = (var4 - 1)
    var17 = (var5 + (var6 + (var4 - 1)))
    var18 = (var5 + (var0 + var10))
    var19 = (var5 + (var0 + var11))
    var13 = (1 if var3 > var8 else 0)
    var20 = ((1 if var3 > var8 else 0) & (1 if (var4 | var8) >= 0 else 0))
    var4 = (var4 + 1)
    var11 = (var5 + (var11 + (var4 + 1)))
    var10 = (var5 + (var4 + var10))
    var21 = (var5 + (var4 + var6))
    var5 = (1 if var3 > var4 else 0)
    var22 = (var12 & ((1 if var3 > var4 else 0) & (1 if (var4 | var7) >= 0 else 0)))
    var6 = (1 if var0 < var3 else 0)
    var7 = (var12 & ((1 if var0 < var3 else 0) & (1 if (var0 | var7) >= 0 else 0)))
    var3 = (1 if var3 > var9 else 0)
    var12 = ((1 if var3 > var9 else 0) & (var6 & (1 if (var0 | var9) >= 0 else 0)))
    var6 = (var13 & (var6 & (1 if (var0 | var8) >= 0 else 0)))
    var8 = (var13 & (var5 & (1 if (var4 | var8) >= 0 else 0)))
    var3 = (var3 & (var5 & (1 if (var4 | var9) >= 0 else 0)))
    while True:  # loop $label9
        if (1 if var3 == 0 else 0):
            break
        var0 = i32_load(((var2 * 36) + 51812))
        if (1 if i32_load(((var2 * 36) + 51812)) == -3 else 0):
            break
        if (1 if (-1 if (1 if var0 >= -1 else 0) else var0) != (-2 if (1 if i32_load8_s(var10) == var1 else 0) else -1) else 0):
            break
        if (1 if var8 == 0 else 0):
            break
        var0 = i32_load(((var2 * 36) + 51792) + 8)
        if (1 if i32_load(((var2 * 36) + 51792) + 8) == -3 else 0):
            break
        if (1 if (-1 if (1 if var0 >= -1 else 0) else var0) != (-2 if (1 if i32_load8_s(var11) == var1 else 0) else -1) else 0):
            break
        if (1 if var20 == 0 else 0):
            break
        var0 = i32_load(((var2 * 36) + 51792) + 4)
        if (1 if i32_load(((var2 * 36) + 51792) + 4) == -3 else 0):
            break
        if (1 if (-1 if (1 if var0 >= -1 else 0) else var0) != (-2 if (1 if i32_load8_s(var15) == var1 else 0) else -1) else 0):
            break
        if (1 if var6 == 0 else 0):
            break
        var0 = i32_load(((var2 * 36) + 51792))
        if (1 if i32_load(((var2 * 36) + 51792)) == -3 else 0):
            break
        if (1 if (-1 if (1 if var0 >= -1 else 0) else var0) != (-2 if (1 if i32_load8_s(var19) == var1 else 0) else -1) else 0):
            break
        if (1 if var12 == 0 else 0):
            break
        var0 = i32_load(((var2 * 36) + 51792) + 12)
        if (1 if i32_load(((var2 * 36) + 51792) + 12) == -3 else 0):
            break
        if (1 if (-1 if (1 if var0 >= -1 else 0) else var0) != (-2 if (1 if i32_load8_s(var18) == var1 else 0) else -1) else 0):
            break
        if (1 if var7 == 0 else 0):
            break
        var0 = i32_load(((var2 * 36) + 51792) + 24)
        if (1 if i32_load(((var2 * 36) + 51792) + 24) == -3 else 0):
            break
        if (1 if (-1 if (1 if var0 >= -1 else 0) else var0) != (-2 if (1 if i32_load8_s(var17) == var1 else 0) else -1) else 0):
            break
        if (1 if var16 == 0 else 0):
            break
        var0 = i32_load(((var2 * 36) + 51820))
        if (1 if i32_load(((var2 * 36) + 51820)) == -3 else 0):
            break
        if (1 if (-1 if (1 if var0 >= -1 else 0) else var0) != (-2 if (1 if i32_load8_s(var14) == var1 else 0) else -1) else 0):
            break
        if (1 if var22 == 0 else 0):
            break
        var0 = i32_load(((var2 * 36) + 51824))
        if (1 if i32_load(((var2 * 36) + 51824)) == -3 else 0):
            break
        if (1 if (-1 if (1 if var0 >= -1 else 0) else var0) == (-2 if (1 if i32_load8_s(var21) == var1 else 0) else -1) else 0):
            break
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != 14 else 0):
            continue
        break  # end loop
    var2 = 55
    return var2

