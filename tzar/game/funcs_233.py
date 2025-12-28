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
# $func505
# ==========================================================
def func505(var0, var1, param2):
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
    var17 = 0.0
    var18 = 0.0
    var6 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var4 = i32_load(9671128)
    var8 = (i32_load(9671128) + (var0 * 132))
    var3 = i32_load((i32_load(9671128) + (var0 * 132)) + 20)
    if (1 if i32_load((i32_load(9671128) + (var0 * 132)) + 20) == 0 else 0):
        break
    var2 = i32_load(var3 + 8)
    if (1 if i32_load(var3 + 8) < 3 else 0):
        break
    var7 = i32_load(var3)
    if i32_load(i32_load(var3)):
        break
    var10 = (var4 + (var0 * 132))
    var5 = i32_load16_u((var4 + (var0 * 132)) + 88)
    var9 = i32_load(var7 + 8)
    var15 = (1 if i32_load(var7 + 8) == var1 else 0)
    var11 = i32_load((var7 + (16 if (1 if i32_load(var7 + 8) == var1 else 0) else 20)))
    var12 = i32_load(9561692)
    var13 = i32_load16_u((var4 + (var1 * 132)) + 110)
    var16 = (i32_load(9561692) + (i32_load16_u((var4 + (var1 * 132)) + 110) * 286704))
    if (1 if i32_load8_u(var10 + 125) == 1 else 0):
        if (1 if var2 == 7 else 0):
            i32_store(var3 + 8, 6)
            var2 = (var5 << 2)
            if (1 if i32_load(((var5 << 2) + (var6 + 16))) == 2147483647 else 0):
                break
            var3 = (((var12 + (var13 * 286704)) + var2) + 283848)
            var2 = i32_load16_u((var4 + (var0 * 132)) + 108)
            break
        var2 = (var4 + (var0 * 132))
        var3 = i32_load16_u((var4 + (var0 * 132)) + 108)
        if (1 if i32_load16_u((var4 + (var0 * 132)) + 108) == 0 else 0):
            break
        var17 = 0.800000012
        var2 = (var12 + (i32_load16_u(var2 + 110) * 286704))
        if (1 if i32_load((((var12 + (i32_load16_u(var2 + 110) * 286704)) + (i32_load(39108) << 2)) + 281808)) != 1 else 0):
            var17 = (0.800000012 if (1 if i32_load(((var2 + (i32_load(39168) << 2)) + 281808)) == 1 else 0) else 0.75)
        if (1 if i32_load(((var6 + 16) + (var5 << 2))) == 2147483647 else 0):
            break
        var2 = (var4 + (var9 * 132))
        var9 = (var4 + (i32_load(var7 + 12) * 132))
        var14 = (i32_load16_u((var4 + (var9 * 132)) + 112) - i32_load16_u((var4 + (i32_load(var7 + 12) * 132)) + 112))
        var2 = (i32_load16_u(var2 + 114) - i32_load16_u(var9 + 114))
        var18 = (((math.sqrt(float((((i32_load16_u((var4 + (var9 * 132)) + 112) - i32_load16_u((var4 + (i32_load(var7 + 12) * 132)) + 112)) * var14) + ((i32_load16_u(var2 + 114) - i32_load16_u(var9 + 114)) * var2)))) * float((var17 * float(i32_load(var7 + 4))))) / 500.0) + 0.5)
        if ((1 if (((math.sqrt(float((((i32_load16_u((var4 + (var9 * 132)) + 112) - i32_load16_u((var4 + (i32_load(var7 + 12) * 132)) + 112)) * var14) + ((i32_load16_u(var2 + 114) - i32_load16_u(var9 + 114)) * var2)))) * float((var17 * float(i32_load(var7 + 4))))) / 500.0) + 0.5) < 4294967296.0 else 0) & (1 if var18 >= 0.0 else 0)):
            break
        var2 = 0
        var7 = ((var12 + (var13 * 286704)) + (var5 << 2))
        var5 = (((var12 + (var13 * 286704)) + (var5 << 2)) + 283848)
        i32_store((((var12 + (var13 * 286704)) + (var5 << 2)) + 283848), ((i32_load(var5) + var3) + var2))
        var3 = (var7 + 281676)
        i32_store(var3, (i32_load(var3) + var2))
        var2 = (var4 + (var0 * 132))
        i32_store16((var4 + (var0 * 132)) + 108, 0)
        i32_store(var10 + 88, ((i32_load8_u((var4 + (var1 * 132)) + 122) << 16) + var11))
        if (1 if i32_load(var2 + 92) == 0 else 0):
            break
        if i32_load(9140316):
            if (1 if i32_load(9140320) != i32_load((var4 + (var0 * 132)) + 28) else 0):
                break
        var3 = i32_load(var8 + 20)
    else:
    if (1 if var2 == 7 else 0):
        i32_store(var3 + 8, 6)
    var2 = (var4 + (var1 * 132))
    var7 = (var4 + (var1 * 132))
    var2 = i32_load(var2 + 56)
    if (1 if i32_load(var2 + 56) == 0 else 0):
        break
    var5 = i32_load(9215884)
    var9 = i32_load((i32_load(9671128) + (var2 * 132)) + 44)
    if (1 if i32_load((i32_load(9215884) + (i32_load((i32_load(9671128) + (var2 * 132)) + 44) << 4)) + 12) != var1 else 0):
        break
    if (1 if i32_load((var5 + ((var9 << 4) | 4))) == 60 else 0):
        break
    i32_store(var7 + 56, var0)
    var2 = var0
    var14 = i32_load(((var6 + 16) + (var11 << 2)))
    var5 = i32_load(((i32_load(9561692) + (i32_load16_u((var4 + (var0 * 132)) + 110) * 286704)) + 284344))
    if (1 if i32_load(((var6 + 16) + (var11 << 2))) < i32_load(((i32_load(9561692) + (i32_load16_u((var4 + (var0 * 132)) + 110) * 286704)) + 284344)) else 0):
        break
    if (1 if var0 != var2 else 0):
        break
    var2 = (var4 + (var0 * 132))
    var9 = (i32_load16_u(var2 + 108) + var5)
    i32_store16((var4 + (var0 * 132)) + 108, (i32_load16_u(var2 + 108) + var5))
    if (1 if var14 != 2147483647 else 0):
        i64_store(var6 + 8, 0)
        i64_store(var6, 0)
        var3 = (var11 << 2)
        i32_store((var6 + (var11 << 2)), var5)
        var5 = i32_load(i32_load(i32_load(var8 + 20)) + 4)
        var11 = i32_load16_u(var2 + 108)
        if (1 if i32_load(i32_load(i32_load(var8 + 20)) + 4) <= i32_load16_u(var2 + 108) else 0):
            var3 = (((var12 + (var13 * 286704)) + var3) + 283848)
            i32_store((((var12 + (var13 * 286704)) + var3) + 283848), (i32_load(var3) + (var11 - var5)))
        var9 = i32_load16_u(var2 + 108)
    else:
    var3 = i32_load(i32_load(var3) + 4)
    if (1 if i32_load(i32_load(var3) + 4) <= (var9 & 65535) else 0):
        i32_store16(var2 + 108, var3)
        if (1 if i32_load((var4 + (var0 * 132)) + 92) == 0 else 0):
            break
        if i32_load(9140316):
            if (1 if i32_load(9140320) != i32_load((var4 + (var0 * 132)) + 28) else 0):
                break
        i32_store(var7 + 56, 0)
        i32_store8(var10 + 125, 0)
        break
    if (1 if i32_load((var4 + (var0 * 132)) + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var4 + (var0 * 132)) + 28) else 0):
            break
    if (1 if i32_load8_u(var10 + 125) == 1 else 0):
        var2 = (var4 + (var0 * 132))
        var3 = i32_load(((i32_load((i32_load(9215884) + (i32_load((var4 + (var0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if i32_load(((i32_load((i32_load(9215884) + (i32_load((var4 + (var0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32):
            # call_indirect via table[var3]
            if (1 if i32_load8_u(var10 + 125) == 3 else 0):
                break
        var8 = i32_load(var2 + 44)
        if i32_load(var2 + 44):
            var10 = i32_load(9142848)
            var3 = i32_load(9215884)
            i32_store((i32_load(9215884) + (var8 << 4)) + 4, 60)
            i32_store((var3 + (i32_load(var2 + 44) << 4)) + 8, i32_load((var4 + (var0 * 132)) + 28))
            i32_store((var3 + (i32_load(var2 + 44) << 4)) + 12, var1)
            i32_store((var3 + (i32_load(var2 + 44) << 4)), (var10 + 40))
            break
        i32_store(var2 + 44, ((Ua(1000, 60, i32_load((var4 + (var0 * 132)) + 28), var1) & 0xFFFFFFFF) >> 2))
        break
    i32_store((i32_load(9215884) + (i32_load((var4 + (var0 * 132)) + 44) << 4)), (i32_load(9142848) + 40))
    global global0
    global0 = (var6 + 32)
    return call_indirect(var3)


# ==========================================================
# $Gd
# Export: Gd
# ==========================================================
def Gd(var0):
    """Export: Gd"""
    if (1 if var0 == 2147483647 else 0):
        var0 = i32_load(i32_load(9568088) + 96)
        i32_store(i32_load(i32_load(9568088) + 96), i32_load(9147392))
        i32_store(var0 + 4, i32_load(9147396))
        i32_store(var0 + 8, i32_load(9147400))
        i32_store(var0 + 12, i32_load(9147404))
        i32_store(var0 + 16, i32_load(9147408))
        i32_store(var0 + 20, i32_load(9147412))
        i32_store(var0 + 24, i32_load(9147416))
        i32_store(var0 + 28, i32_load(9147420))
        return
    func368(var0)

