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
# $Ea
# Export: Ea
# ==========================================================
def Ea(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12):
    """Export: Ea"""
    var13 = 0
    var14 = 0
    var15 = 0
    if var6:
        var6 = i32_load(9561792)
        if (1 if i32_load(9561792) != i32_load(9561788) else 0):
            var4 = i32_load(9561784)
            break
        var1 = (i32_load(9561796) + var6)
        i32_store(9561788, (i32_load(9561796) + var6))
        var0 = i32_load(9561784)
        var4 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        if var6:
            # Unknown: memory.copy []
        if var0:
            var6 = i32_load(9561792)
        i32_store(9561784, var4)
        i32_store(9561792, (var6 + 1))
        i32_store((var4 + (var6 << 2)), var3)
        var1 = (i32_load(59176) + 10)
        var6 = i32_load(9561792)
        if (1 if i32_load(9561792) != i32_load(9561788) else 0):
            var3 = var4
            break
        var0 = (i32_load(9561796) + var6)
        i32_store(9561788, (i32_load(9561796) + var6))
        var3 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var6:
            # Unknown: memory.copy []
        i32_store(9561784, var3)
        var6 = i32_load(9561792)
        i32_store(9561792, (var6 + 1))
        i32_store((var3 + (var6 << 2)), var1)
        var6 = i32_load(9561792)
        if (1 if i32_load(9561792) != i32_load(9561788) else 0):
            var4 = var3
            break
        var0 = (i32_load(9561796) + var6)
        i32_store(9561788, (i32_load(9561796) + var6))
        var4 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var6:
            # Unknown: memory.copy []
        i32_store(9561784, var4)
        var6 = i32_load(9561792)
        i32_store(9561792, (var6 + 1))
        i32_store((var4 + (var6 << 2)), var5)
        var6 = i32_load(9561792)
        if (1 if i32_load(9561792) != i32_load(9561788) else 0):
            var3 = var4
            break
        var0 = (i32_load(9561796) + var6)
        i32_store(9561788, (i32_load(9561796) + var6))
        var3 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var6:
            # Unknown: memory.copy []
        i32_store(9561784, var3)
        var6 = i32_load(9561792)
        i32_store(9561792, (var6 + 1))
        i32_store((var3 + (var6 << 2)), var2)
        var6 = i32_load(9561792)
        if (1 if i32_load(9561792) != i32_load(9561788) else 0):
            var4 = var3
            break
        var0 = (i32_load(9561796) + var6)
        i32_store(9561788, (i32_load(9561796) + var6))
        var4 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var6:
            # Unknown: memory.copy []
        i32_store(9561784, var4)
        var6 = i32_load(9561792)
        i32_store(9561792, (var6 + 1))
        i32_store((var4 + (var6 << 2)), var8)
        var6 = i32_load(9561792)
        if (1 if i32_load(9561792) != i32_load(9561788) else 0):
            var3 = var4
            break
        var0 = (i32_load(9561796) + var6)
        i32_store(9561788, (i32_load(9561796) + var6))
        var3 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var6:
            # Unknown: memory.copy []
        i32_store(9561784, var3)
        var6 = i32_load(9561792)
        i32_store(9561792, (var6 + 1))
        i32_store((var3 + (var6 << 2)), var7)
        var6 = i32_load(9561792)
        if (1 if i32_load(9561792) != i32_load(9561788) else 0):
            var4 = var3
            break
        var0 = (i32_load(9561796) + var6)
        i32_store(9561788, (i32_load(9561796) + var6))
        var4 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var6:
            # Unknown: memory.copy []
        i32_store(9561784, var4)
        var6 = i32_load(9561792)
        i32_store(9561792, (var6 + 1))
        i32_store((var4 + (var6 << 2)), var9)
        var6 = i32_load(9561792)
        if (1 if i32_load(9561792) != i32_load(9561788) else 0):
            var3 = var4
            break
        var0 = (i32_load(9561796) + var6)
        i32_store(9561788, (i32_load(9561796) + var6))
        var3 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var6:
            # Unknown: memory.copy []
        i32_store(9561784, var3)
        var6 = i32_load(9561792)
        i32_store(9561792, (var6 + 1))
        i32_store((var3 + (var6 << 2)), var10)
        return 0
    var6 = 0
    if (1 if i32_load8_u(9561832) == 0 else 0):
        var13 = i32_load(9561692)
        var14 = (var11 + 1)
        var11 = ((var11 + 1) * 286704)
        var6 = (i32_load(9561692) + ((var11 + 1) * 286704))
        i32_store((i32_load(9561692) + ((var11 + 1) * 286704)) + 283908, var14)
        var15 = i32_load8_u(9147212)
        i32_store(var6 + 286684, ((1 if i32_load8_u(9147212) == 0 else 0) & var4))
        if (1 if var4 == 0 else 0):
            i32_store((var11 + var13) + 284616, var3)
        var11 = (var11 + var13)
        i32_store((var11 + var13) + 283952, var8)
        i32_store(var11 + 283948, var5)
        i32_store(var11 + 284620, (var12 + 1))
        i32_store(var11 + 283964, var9)
        i32_store8(var11 + 93, var10)
        i32_store8(var11 + 92, var7)
        if (1 if var3 != i32_load(9142384) else 0):
            if i32_load8_u(9147210):
                break
            if var4:
                break
        i32_store(9142872, var14)
        if (1 if var15 == 0 else 0):
            var3 = (var13 + (var14 * 286704))
            i32_store((var13 + (var14 * 286704)) + 284608, var0)
            i32_store(var3 + 283960, (var1 if (1 if var1 <= 4 else 0) else 0))
            i32_store8(var3 + 283972, ((var2 & 0xFFFFFFFF) >> 16))
            i32_store8((var3 + 283974), var2)
            i32_store8((var3 + 283973), ((var2 & 0xFFFFFFFF) >> 8))
        i32_store(41092, (i32_load(41092) + 1))
    return var6


# ==========================================================
# $ke
# Export: ke
# ==========================================================
def ke():
    """Export: ke"""
    var0 = 0
    var1 = 0
    var0 = i32_load(9687204)
    if i32_load(9687204):
        i32_store(9687204, 0)
    var0 = i32_load(9687216)
    var1 = func26(i32_load(9687216))
    i32_store(9687204, func26(i32_load(9687216)))
    i32_store(9147392, i32_load(9687216))
    return i32_load(9687204)

