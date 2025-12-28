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
# $func458
# ==========================================================
def func458(var0, var1):
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
    if (1 if var0 == 0 else 0):
        break
    i32_store(var0 + 8, 6932)
    i32_store(var0, 0)
    if (1 if var1 == 0 else 0):
        i32_store(var0 + 8, 8788)
        i64_store(var0, 2)
        break
    var10 = i32_load(var1 + 60)
    if (1 if i32_load(var1 + 60) <= 3 else 0):
        i32_store(var0 + 8, 8211)
        break
    var2 = i32_load(var1 + 64)
    var3 = i32_load8_u(i32_load(var1 + 64) + 1)
    var8 = i32_load8_u(var2 + 2)
    var4 = i32_load8_u(var2)
    var5 = (((i32_load8_u(var2) & 0xFFFFFFFF) >> 4) & 1)
    i32_store8(var0 + 54, (((i32_load8_u(var2) & 0xFFFFFFFF) >> 4) & 1))
    var11 = (((var4 & 0xFFFFFFFF) >> 1) & 7)
    i32_store8(var0 + 53, (((var4 & 0xFFFFFFFF) >> 1) & 7))
    var12 = (var4 & 1)
    i32_store8(var0 + 52, (1 if (var4 & 1) == 0 else 0))
    var8 = (((var4 | ((var3 << 8) | (var8 << 16))) & 0xFFFFFFFF) >> 5)
    i32_store(var0 + 56, (((var4 | ((var3 << 8) | (var8 << 16))) & 0xFFFFFFFF) >> 5))
    if (1 if var11 >= 4 else 0):
        i32_store(var0 + 8, 8180)
        break
    if (1 if var5 == 0 else 0):
        i32_store(var0 + 8, 8285)
        i64_store(var0, 4)
        break
    var4 = (var10 - 3)
    var3 = (var2 + 3)
    if (1 if var12 == 0 else 0):
        if (1 if var4 <= 6 else 0):
            i32_store(var0 + 8, 3600)
            break
        if (1 if i32_load8_u(var3) != 157 else 0):
            break
        if (1 if i32_load8_u(var2 + 4) != 1 else 0):
            break
        if (1 if i32_load8_u(var2 + 5) == 42 else 0):
            break
        i32_store(var0 + 8, 4952)
        break
        var4 = (i32_load8_u(var2 + 6) | ((i32_load8_u(var2 + 7) << 8) & 16128))
        i32_store16(var0 + 60, (i32_load8_u(var2 + 6) | ((i32_load8_u(var2 + 7) << 8) & 16128)))
        i32_store8((var0 - -64), ((i32_load8_u(var2 + 7) & 0xFFFFFFFF) >> 6))
        var3 = (i32_load8_u(var2 + 8) | ((i32_load8_u(var2 + 9) << 8) & 16128))
        i32_store16(var0 + 62, (i32_load8_u(var2 + 8) | ((i32_load8_u(var2 + 9) << 8) & 16128)))
        var8 = i32_load8_u(var2 + 9)
        i32_store(var0 + 304, (((var3 + 15) & 0xFFFFFFFF) >> 4))
        i32_store(var0 + 300, (((var4 + 15) & 0xFFFFFFFF) >> 4))
        i32_store8(var0 + 65, ((var8 & 0xFFFFFFFF) >> 6))
        i32_store(var1 + 84, 0)
        i32_store(var1 + 4, var3)
        i32_store(var1, var4)
        i32_store(var1 + 100, var3)
        i32_store(var1 + 96, var4)
        i32_store(var1 + 92, 0)
        i32_store(var1 + 88, var3)
        i32_store(var1 + 80, var4)
        i64_store(var1 + 72, 0)
        i32_store(var1 + 16, var3)
        i32_store(var1 + 12, var4)
        i32_store16(var0 + 948, 65535)
        i32_store8(var0 + 950, 255)
        i32_store(var0 + 132, 0)
        i64_store(var0 + 124, 1)
        i64_store(var0 + 116, 0)
        var3 = (var2 + 10)
        var8 = i32_load(var0 + 56)
        var4 = (var10 - 10)
    if (1 if var4 < var8 else 0):
        if i32_load(var0):
            break
        i32_store(var0 + 8, 4209)
        break
    var1 = (var0 + 16)
    func270((var0 + 16), var3, var8)
    var5 = i32_load(var0 + 56)
    if i32_load8_u(var0 + 52):
        i32_store8(var0 + 66, func33(var1, 1))
        i32_store8(var0 + 67, func33(var1, 1))
    var2 = func33(var1, 1)
    i32_store(var0 + 116, func33(var1, 1))
    if var2:
        i32_store(var0 + 120, func33(var1, 1))
        if func33(var1, 1):
            i32_store(var0 + 124, func33(var1, 1))
            if func33(var1, 1):
            else:
            i32_store8(func51(var1, 7) + 128, 0)
            if func33(var1, 1):
            else:
            i32_store8(func51(var1, 7) + 129, 0)
            if func33(var1, 1):
            else:
            i32_store8(func51(var1, 7) + 130, 0)
            if func33(var1, 1):
            else:
            i32_store8(func51(var1, 7) + 131, 0)
            if func33(var1, 1):
            else:
            i32_store8(func51(var1, 6) + 132, 0)
            if func33(var1, 1):
            else:
            i32_store8(func51(var1, 6) + 133, 0)
            if func33(var1, 1):
            else:
            i32_store8(func51(var1, 6) + 134, 0)
            if func33(var1, 1):
            else:
            i32_store8(func51(var1, 6) + 135, 0)
        if (1 if i32_load(var0 + 120) == 0 else 0):
            break
        if func33(var1, 1):
        else:
        i32_store8(func33(var1, 8) + 948, 255)
        if func33(var1, 1):
        else:
        i32_store8(func33(var1, 8) + 949, 255)
        if func33(var1, 1):
        else:
        i32_store8(func33(var1, 8) + 950, 255)
        break
    i32_store(var0 + 120, 0)
    if i32_load(var0 + 44):
        if i32_load(var0):
            break
        i32_store(var0 + 8, 3545)
        break
    i32_store(var0 + 68, func33(var1, 1))
    i32_store(var0 + 72, func33(var1, 6))
    i32_store(var0 + 76, func33(var1, 3))
    var2 = func33(var1, 1)
    i32_store(var0 + 80, func33(var1, 1))
    if (1 if var2 == 0 else 0):
        break
    if (1 if func33(var1, 1) == 0 else 0):
        break
    if func33(var1, 1):
        i32_store(var0 + 84, func51(var1, 6))
    if func33(var1, 1):
        i32_store(var0 + 88, func51(var1, 6))
    if func33(var1, 1):
        i32_store(var0 + 92, func51(var1, 6))
    if func33(var1, 1):
        i32_store(var0 + 96, func51(var1, 6))
    if func33(var1, 1):
        i32_store(var0 + 100, func51(var1, 6))
    if func33(var1, 1):
        i32_store(var0 + 104, func51(var1, 6))
    if func33(var1, 1):
        i32_store(var0 + 108, func51(var1, 6))
    if (1 if func33(var1, 1) == 0 else 0):
        break
    i32_store(var0 + 112, func51(var1, 6))
    if i32_load(var0 + 72):
    else:
    i32_store((1 if i32_load(var0 + 68) else 2) + 2352, 0)
    if i32_load(var1 + 28):
        if i32_load(var0):
            break
        i32_store(var0 + 8, 3573)
        break
    var2 = (var3 + var5)
    var10 = 0
    var11 = func33((var0 + 16), 2)
    var8 = ((-1 << func33((var0 + 16), 2)) ^ -1)
    i32_store(var0 + 324, ((-1 << func33((var0 + 16), 2)) ^ -1))
    var4 = (var4 - var5)
    var3 = (var8 * 3)
    if (1 if (var4 - var5) < (var8 * 3) else 0):
        break
    var12 = (var2 + var4)
    var4 = (var4 - var3)
    var3 = (var2 + var3)
    if var11:
        var11 = (1 if (1 if var8 <= 1 else 0) else var8)
        var9 = (var0 + 328)
        while True:  # loop $label9
            var5 = (i32_load16_u(var2) | (i32_load8_u(var2 + 2) << 16))
            var5 = ((i32_load16_u(var2) | (i32_load8_u(var2 + 2) << 16)) if (1 if var4 > var5 else 0) else var4)
            func270((var9 + (var10 << 5)), var3, ((i32_load16_u(var2) | (i32_load8_u(var2 + 2) << 16)) if (1 if var4 > var5 else 0) else var4))
            var4 = (var4 - var5)
            var3 = (var3 + var5)
            var2 = (var2 + 3)
            var10 = (var10 + 1)
            if (1 if (var10 + 1) != var11 else 0):
                continue
            break  # end loop
    func270(((var0 + (var8 << 5)) + 328), var3, var4)
    if (1 if var3 < var12 else 0):
        break
    var2 = (5 if i32_load(var0 + 48) else 7)
    if (5 if i32_load(var0 + 48) else 7):
        break
    var8 = 0
    var10 = 0
    var5 = 0
    var11 = 0
    var2 = (var0 + 16)
    var4 = func33((var0 + 16), 7)
    if func33(var2, 1):
        var10 = func51(var2, 4)
    if func33(var2, 1):
        var8 = func51(var2, 4)
    if func33(var2, 1):
        var11 = func51(var2, 4)
    if func33(var2, 1):
        var5 = func51(var2, 4)
    if func33(var2, 1):
    else:
    var12 = 0
    var2 = var4
    var9 = i32_load(var0 + 116)
    if i32_load(var0 + 116):
        var2 = (i32_load8_s(var0 + 128) + (0 if i32_load(var0 + 124) else var4))
    var3 = (var2 + var12)
    i32_store(var0 + 844, (var2 + var12))
    var6 = (var2 + var5)
    var6 = (117 if (1 if var6 >= 117 else 0) else (var2 + var5))
    i32_store(var0 + 836, i32_load8_u((((117 if (1 if var6 >= 117 else 0) else (var2 + var5)) if (1 if var6 > 0 else 0) else 0) + 10368)))
    var6 = (127 if (1 if var2 >= 127 else 0) else var2)
    i32_store(var0 + 824, i32_load16_u(((((127 if (1 if var2 >= 127 else 0) else var2) if (1 if var6 > 0 else 0) else 0) << 1) + 10496)))
    var6 = (var2 + var10)
    var6 = (127 if (1 if var6 >= 127 else 0) else (var2 + var10))
    i32_store(var0 + 820, i32_load8_u((((127 if (1 if var6 >= 127 else 0) else (var2 + var10)) if (1 if var6 > 0 else 0) else 0) + 10368)))
    var3 = (127 if (1 if var3 >= 127 else 0) else var3)
    i32_store(var0 + 840, i32_load16_u(((((127 if (1 if var3 >= 127 else 0) else var3) if (1 if var3 > 0 else 0) else 0) << 1) + 10496)))
    var3 = (var2 + var8)
    var3 = (127 if (1 if var3 >= 127 else 0) else (var2 + var8))
    i32_store(var0 + 828, (i32_load8_u((((127 if (1 if var3 >= 127 else 0) else (var2 + var8)) if (1 if var3 > 0 else 0) else 0) + 10368)) << 1))
    var2 = (var2 + var11)
    var2 = (127 if (1 if var2 >= 127 else 0) else (var2 + var11))
    var2 = (i32_load16_u(((((127 if (1 if var2 >= 127 else 0) else (var2 + var11)) if (1 if var2 > 0 else 0) else 0) << 1) + 10496)) * 101581)
    i32_store(var0 + 832, (8 if (1 if var2 < 524288 else 0) else (((i32_load16_u(((((127 if (1 if var2 >= 127 else 0) else (var2 + var11)) if (1 if var2 > 0 else 0) else 0) << 1) + 10496)) * 101581) & 0xFFFFFFFF) >> 16)))
    if (1 if var9 == 0 else 0):
        i64_store(var0 + 852, i64_load(var0 + 820))
        i64_store(var0 + 876, i64_load(var0 + 844))
        i64_store(var0 + 868, i64_load(var0 + 836))
        i64_store(var0 + 860, i64_load(var0 + 828))
        i64_store(var0 + 884, i64_load(var0 + 820))
        i64_store(var0 + 892, i64_load(var0 + 828))
        i64_store(var0 + 900, i64_load(var0 + 836))
        i64_store(var0 + 908, i64_load(var0 + 844))
        i64_store(var0 + 916, i64_load(var0 + 820))
        i64_store(var0 + 924, i64_load(var0 + 828))
        i64_store(var0 + 932, i64_load(var0 + 836))
        i64_store(var0 + 940, i64_load(var0 + 844))
        break
    var3 = (0 if i32_load(var0 + 124) else var4)
    var2 = ((0 if i32_load(var0 + 124) else var4) + i32_load8_s(var0 + 129))
    var9 = (((0 if i32_load(var0 + 124) else var4) + i32_load8_s(var0 + 129)) + var12)
    i32_store(var0 + 876, (((0 if i32_load(var0 + 124) else var4) + i32_load8_s(var0 + 129)) + var12))
    var3 = (var3 + i32_load8_s(var0 + 130))
    var6 = ((var3 + i32_load8_s(var0 + 130)) + var12)
    i32_store(var0 + 908, ((var3 + i32_load8_s(var0 + 130)) + var12))
    var7 = (var2 + var5)
    var7 = (117 if (1 if var7 >= 117 else 0) else (var2 + var5))
    i32_store(var0 + 868, i32_load8_u((((117 if (1 if var7 >= 117 else 0) else (var2 + var5)) if (1 if var7 > 0 else 0) else 0) + 10368)))
    var7 = (127 if (1 if var2 >= 127 else 0) else var2)
    i32_store(var0 + 856, i32_load16_u(((((127 if (1 if var2 >= 127 else 0) else var2) if (1 if var7 > 0 else 0) else 0) << 1) + 10496)))
    var7 = (var2 + var10)
    var7 = (127 if (1 if var7 >= 127 else 0) else (var2 + var10))
    i32_store(var0 + 852, i32_load8_u((((127 if (1 if var7 >= 127 else 0) else (var2 + var10)) if (1 if var7 > 0 else 0) else 0) + 10368)))
    var7 = (var3 + var5)
    var7 = (117 if (1 if var7 >= 117 else 0) else (var3 + var5))
    i32_store(var0 + 900, i32_load8_u((((117 if (1 if var7 >= 117 else 0) else (var3 + var5)) if (1 if var7 > 0 else 0) else 0) + 10368)))
    var7 = (127 if (1 if var3 >= 127 else 0) else var3)
    i32_store(var0 + 888, i32_load16_u(((((127 if (1 if var3 >= 127 else 0) else var3) if (1 if var7 > 0 else 0) else 0) << 1) + 10496)))
    var7 = (var3 + var10)
    var7 = (127 if (1 if var7 >= 127 else 0) else (var3 + var10))
    i32_store(var0 + 884, i32_load8_u((((127 if (1 if var7 >= 127 else 0) else (var3 + var10)) if (1 if var7 > 0 else 0) else 0) + 10368)))
    var9 = (127 if (1 if var9 >= 127 else 0) else var9)
    i32_store(var0 + 872, i32_load16_u(((((127 if (1 if var9 >= 127 else 0) else var9) if (1 if var9 > 0 else 0) else 0) << 1) + 10496)))
    var9 = (var2 + var8)
    var9 = (127 if (1 if var9 >= 127 else 0) else (var2 + var8))
    i32_store(var0 + 860, (i32_load8_u((((127 if (1 if var9 >= 127 else 0) else (var2 + var8)) if (1 if var9 > 0 else 0) else 0) + 10368)) << 1))
    var9 = (127 if (1 if var6 >= 127 else 0) else var6)
    i32_store(var0 + 904, i32_load16_u(((((127 if (1 if var6 >= 127 else 0) else var6) if (1 if var9 > 0 else 0) else 0) << 1) + 10496)))
    var9 = (var3 + var8)
    var9 = (127 if (1 if var9 >= 127 else 0) else (var3 + var8))
    i32_store(var0 + 892, (i32_load8_u((((127 if (1 if var9 >= 127 else 0) else (var3 + var8)) if (1 if var9 > 0 else 0) else 0) + 10368)) << 1))
    var2 = (var2 + var11)
    var2 = (127 if (1 if var2 >= 127 else 0) else (var2 + var11))
    var2 = (i32_load16_u(((((127 if (1 if var2 >= 127 else 0) else (var2 + var11)) if (1 if var2 > 0 else 0) else 0) << 1) + 10496)) * 101581)
    i32_store(var0 + 864, (8 if (1 if var2 < 524288 else 0) else (((i32_load16_u(((((127 if (1 if var2 >= 127 else 0) else (var2 + var11)) if (1 if var2 > 0 else 0) else 0) << 1) + 10496)) * 101581) & 0xFFFFFFFF) >> 16)))
    var2 = (var3 + var11)
    var2 = (127 if (1 if var2 >= 127 else 0) else (var3 + var11))
    var2 = (i32_load16_u(((((127 if (1 if var2 >= 127 else 0) else (var3 + var11)) if (1 if var2 > 0 else 0) else 0) << 1) + 10496)) * 101581)
    i32_store(var0 + 896, (8 if (1 if var2 < 524288 else 0) else (((i32_load16_u(((((127 if (1 if var2 >= 127 else 0) else (var3 + var11)) if (1 if var2 > 0 else 0) else 0) << 1) + 10496)) * 101581) & 0xFFFFFFFF) >> 16)))
    var2 = (i32_load8_s(var0 + 131) + (0 if i32_load(var0 + 124) else var4))
    var4 = ((i32_load8_s(var0 + 131) + (0 if i32_load(var0 + 124) else var4)) + var12)
    i32_store(var0 + 940, ((i32_load8_s(var0 + 131) + (0 if i32_load(var0 + 124) else var4)) + var12))
    var3 = (var2 + var10)
    var3 = (127 if (1 if var3 >= 127 else 0) else (var2 + var10))
    i32_store(var0 + 916, i32_load8_u((((127 if (1 if var3 >= 127 else 0) else (var2 + var10)) if (1 if var3 > 0 else 0) else 0) + 10368)))
    var3 = (127 if (1 if var2 >= 127 else 0) else var2)
    i32_store(var0 + 920, i32_load16_u(((((127 if (1 if var2 >= 127 else 0) else var2) if (1 if var3 > 0 else 0) else 0) << 1) + 10496)))
    var3 = (var2 + var5)
    var3 = (117 if (1 if var3 >= 117 else 0) else (var2 + var5))
    i32_store(var0 + 932, i32_load8_u((((117 if (1 if var3 >= 117 else 0) else (var2 + var5)) if (1 if var3 > 0 else 0) else 0) + 10368)))
    var3 = (var2 + var8)
    var3 = (127 if (1 if var3 >= 127 else 0) else (var2 + var8))
    i32_store(var0 + 924, (i32_load8_u((((127 if (1 if var3 >= 127 else 0) else (var2 + var8)) if (1 if var3 > 0 else 0) else 0) + 10368)) << 1))
    var4 = (127 if (1 if var4 >= 127 else 0) else var4)
    i32_store(var0 + 936, i32_load16_u(((((127 if (1 if var4 >= 127 else 0) else var4) if (1 if var4 > 0 else 0) else 0) << 1) + 10496)))
    var2 = (var2 + var11)
    var2 = (127 if (1 if var2 >= 127 else 0) else (var2 + var11))
    var2 = (i32_load16_u(((((127 if (1 if var2 >= 127 else 0) else (var2 + var11)) if (1 if var2 > 0 else 0) else 0) << 1) + 10496)) * 101581)
    i32_store(var0 + 928, (8 if (1 if var2 < 524288 else 0) else (((i32_load16_u(((((127 if (1 if var2 >= 127 else 0) else (var2 + var11)) if (1 if var2 > 0 else 0) else 0) << 1) + 10496)) * 101581) & 0xFFFFFFFF) >> 16)))
    if (1 if i32_load8_u(var0 + 52) == 0 else 0):
        if i32_load(var0):
            break
        i32_store(var0 + 8, 8268)
        i64_store(var0, 4)
        break
    var8 = 0
    var11 = (var0 + 948)
    while True:  # loop $label25
        var3 = 0
        while True:  # loop $label24
            var7 = (var3 * 33)
            var12 = (var8 * 264)
            var10 = (((var3 * 33) + (var0 + (var8 * 264))) + 951)
            var4 = 0
            while True:  # loop $label15
                var9 = (var7 + var12)
                var13 = ((var7 + var12) + var4)
                var14 = i32_load8_u((((var7 + var12) + var4) + 10752))
                var6 = i32_load(var1 + 8)
                var2 = i32_load(var1 + 12)
                if (1 if i32_load(var1 + 12) >= 0 else 0):
                    break
                var5 = i32_load(var1 + 16)
                if (1 if i32_load(var1 + 16) == 0 else 0):
                    break
                if (1 if i32_load(var1 + 24) > var5 else 0):
                    var15 = i64_load(var5)
                    i32_store(var1 + 16, (var5 + 7))
                    i64_store(var1, ((i64_load(var1) << 56) | ((((((var15 << 56) | ((var15 & 65280) << 40)) | (((var15 & 16711680) << 24) | ((var15 & 4278190080) << 8))) | ((((var15 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var15 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var15 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                    var2 = (var2 + 56)
                    break
                func36(var1)
                var2 = i32_load(var1 + 12)
                var5 = (((var6 * var14) & 0xFFFFFFFF) >> 8)
                var15 = i64_load(var1)
                var16 = i64_extend_u(var2)
                var2 = (1 if (((var6 * var14) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var1) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0)
                if (1 if (1 if (((var6 * var14) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var1) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0) == 0 else 0):
                    i64_store(var1, (var15 - (i64_extend_u((var5 + 1)) << var16)))
                    break
                var5 = (var5 + 1)
                var6 = (clz32((var5 + 1)) ^ 24)
                i32_store(var2 + 12, ((var6 - var5) - (clz32((var5 + 1)) ^ 24)))
                i32_store(var1 + 8, ((var5 << var6) - 1))
                if (1 if var2 == 0 else 0):
                    break
                i32_store8(func33(var1, 8), i32_load8_u((var13 + 11808)))
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != 11 else 0):
                    continue
                break  # end loop
            var4 = 0
            while True:  # loop $label19
                var7 = (var4 + var9)
                var13 = i32_load8_u(((var4 + var9) + 10763))
                var6 = i32_load(var1 + 8)
                var2 = i32_load(var1 + 12)
                if (1 if i32_load(var1 + 12) >= 0 else 0):
                    break
                var5 = i32_load(var1 + 16)
                if (1 if i32_load(var1 + 16) == 0 else 0):
                    break
                if (1 if i32_load(var1 + 24) <= var5 else 0):
                    func36(var1)
                    var2 = i32_load(var1 + 12)
                    break
                var15 = i64_load(var5)
                i32_store(var1 + 16, (var5 + 7))
                i64_store(var1, ((i64_load(var1) << 56) | ((((((var15 << 56) | ((var15 & 65280) << 40)) | (((var15 & 16711680) << 24) | ((var15 & 4278190080) << 8))) | ((((var15 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var15 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var15 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                var2 = (var2 + 56)
                var5 = (((var6 * var13) & 0xFFFFFFFF) >> 8)
                var15 = i64_load(var1)
                var16 = i64_extend_u(var2)
                var2 = (1 if (((var6 * var13) & 0xFFFFFFFF) >> 8) < i32(((i64_load(var1) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0)
                if (1 if (1 if (((var6 * var13) & 0xFFFFFFFF) >> 8) < i32(((i64_load(var1) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0) == 0 else 0):
                    break
                i64_store(var1, (var15 - (i64_extend_u((var5 + 1)) << var16)))
                var5 = (var6 - var5)
                var6 = (clz32((var6 - var5)) ^ 24)
                i32_store(var2 + 12, ((var5 + 1) - (clz32((var6 - var5)) ^ 24)))
                i32_store(var1 + 8, ((var5 << var6) - 1))
                if (1 if var2 == 0 else 0):
                    break
                i32_store8(i32_load8_u((var7 + 11819)) + 11, func33(var1, 8))
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != 11 else 0):
                    continue
                break  # end loop
            var4 = 0
            while True:  # loop $label23
                var7 = (var4 + var9)
                var13 = i32_load8_u(((var4 + var9) + 10774))
                var6 = i32_load(var1 + 8)
                var2 = i32_load(var1 + 12)
                if (1 if i32_load(var1 + 12) >= 0 else 0):
                    break
                var5 = i32_load(var1 + 16)
                if (1 if i32_load(var1 + 16) == 0 else 0):
                    break
                if (1 if i32_load(var1 + 24) <= var5 else 0):
                    func36(var1)
                    var2 = i32_load(var1 + 12)
                    break
                var15 = i64_load(var5)
                i32_store(var1 + 16, (var5 + 7))
                i64_store(var1, ((i64_load(var1) << 56) | ((((((var15 << 56) | ((var15 & 65280) << 40)) | (((var15 & 16711680) << 24) | ((var15 & 4278190080) << 8))) | ((((var15 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var15 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var15 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                var2 = (var2 + 56)
                var5 = (((var6 * var13) & 0xFFFFFFFF) >> 8)
                var15 = i64_load(var1)
                var16 = i64_extend_u(var2)
                var2 = (1 if (((var6 * var13) & 0xFFFFFFFF) >> 8) < i32(((i64_load(var1) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0)
                if (1 if (1 if (((var6 * var13) & 0xFFFFFFFF) >> 8) < i32(((i64_load(var1) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2))) else 0) == 0 else 0):
                    break
                i64_store(var1, (var15 - (i64_extend_u((var5 + 1)) << var16)))
                var5 = (var6 - var5)
                var6 = (clz32((var6 - var5)) ^ 24)
                i32_store(var2 + 12, ((var5 + 1) - (clz32((var6 - var5)) ^ 24)))
                i32_store(var1 + 8, ((var5 << var6) - 1))
                if (1 if var2 == 0 else 0):
                    break
                i32_store8(i32_load8_u((var7 + 11830)) + 22, func33(var1, 8))
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != 11 else 0):
                    continue
                break  # end loop
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != 8 else 0):
                continue
            break  # end loop
        var2 = (var11 + (var8 * 68))
        var3 = (var11 + var12)
        var10 = ((var11 + var12) + 3)
        i32_store(((var11 + (var8 * 68)) + 1124), ((var11 + var12) + 3))
        i32_store((var2 + 1120), (var3 + 234))
        var4 = (var3 + 201)
        i32_store((var2 + 1116), (var3 + 201))
        i32_store((var2 + 1112), var4)
        i32_store((var2 + 1108), var4)
        i32_store((var2 + 1104), var4)
        i32_store((var2 + 1100), var4)
        i32_store((var2 + 1096), var4)
        i32_store((var2 + 1092), var4)
        i32_store((var2 + 1088), var4)
        i32_store((var2 + 1084), (var3 + 168))
        i32_store((var2 + 1080), (var3 + 135))
        i32_store((var2 + 1076), var4)
        i32_store((var2 + 1072), (var3 + 102))
        i32_store((var2 + 1068), (var3 + 69))
        i32_store((var2 + 1064), (var3 + 36))
        i32_store((var2 + 1060), var10)
        var8 = (var8 + 1)
        if (1 if (var8 + 1) != 4 else 0):
            continue
        break  # end loop
    var2 = func33(var1, 1)
    i32_store(var0 + 2280, func33(var1, 1))
    if var2:
        i32_store8(var0 + 2284, func33(var1, 8))
    break
    a_c()
    raise RuntimeError('unreachable')
    i32_store(var0 + 4, 1)
    return 1
    i64_store(var0, 7)
    break
    i64_store(var0, 3)
    return 0

