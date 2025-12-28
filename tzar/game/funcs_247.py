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
# $func746
# ==========================================================
def func746(var0, var1, param2):
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
    var16 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = i32_load(9671128)
    var4 = (i32_load(9671128) + (var0 * 132))
    var6 = (var3 + (var1 * 132))
    var12 = i32_load8_u((var3 + (var1 * 132)) + 122)
    var11 = i32_load8_u(var4 + 125)
    if (1 if i32_load8_u(var4 + 125) == 1 else 0):
        var2 = ((var12 * 404) + 9568096)
        var7 = i32_load(((var12 * 404) + 9568096) + 220)
        var8 = i32_load16_u(var6 + 114)
        var14 = (i32_load(((var12 * 404) + 9568096) + 220) + i32_load16_u(var6 + 114))
        var5 = i32_load(var2 + 216)
        var12 = i32_load16_u(var6 + 112)
        var6 = (i32_load(var2 + 216) + i32_load16_u(var6 + 112))
        var9 = i32_load16_u(var4 + 114)
        var10 = i32_load16_u(var4 + 112)
        var2 = (1 if i32_load16_u(var4 + 112) < var12 else 0)
        if (1 if i32_load16_u(var4 + 112) < var12 else 0):
            break
        if (1 if var6 <= var10 else 0):
            break
        if (1 if var8 > var9 else 0):
            break
        if (1 if var9 >= var14 else 0):
            break
        var2 = ((var7 // 2) + var8)
        var13 = (-1 if (1 if var2 < var9 else 0) else (1 if ((var7 // 2) + var8) != var9 else 0))
        var2 = ((var5 // 2) + var12)
        break
        var13 = (1 if (1 if var8 > var9 else 0) else (-1 if (1 if var9 >= var14 else 0) else 0))
        var11 = (1 if var2 else (-1 if (1 if var6 <= var10 else 0) else 0))
        var5 = 6
        var2 = (((var13 * 3) + var11) + 4)
        if (1 if (((var13 * 3) + var11) + 4) <= 8 else 0):
            var5 = i32_load8_u((var2 + 10184))
        var2 = (var3 + (var0 * 132))
        i32_store8((var3 + (var0 * 132)) + 124, var5)
        var2 = ((i32_load8_u(var2 + 122) * 72) + 9263856)
        if i32_load(((i32_load8_u(var2 + 122) * 72) + 9263856) + 12):
            break
        var6 = (var3 + (var0 * 132))
        var2 = i32_load(((i32_load((i32_load(9215884) + (i32_load((var3 + (var0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if i32_load(((i32_load((i32_load(9215884) + (i32_load((var3 + (var0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32):
            # call_indirect via table[var2]
        if (1 if i32_load8_u(var4 + 125) == 3 else 0):
            break
        var5 = i32_load(var6 + 44)
        if i32_load(var6 + 44):
            var2 = i32_load(9142848)
            var7 = i32_load(9215884)
            i32_store((i32_load(9215884) + (var5 << 4)) + 4, 13)
            i32_store((var7 + (i32_load(var6 + 44) << 4)) + 8, i32_load((var3 + (var0 * 132)) + 28))
            i32_store((var7 + (i32_load(var6 + 44) << 4)) + 12, var1)
            i32_store((var7 + (i32_load(var6 + 44) << 4)), (var2 + 1))
            break
        i32_store(var6 + 44, ((Ua(25, 13, i32_load((var3 + (var0 * 132)) + 28), var1) & 0xFFFFFFFF) >> 2))
        break
    if (1 if i32_load8_u(var6 + 125) == 3 else 0):
        break
    var17 = (var3 + (var1 * 132))
    var14 = i32_load((var3 + (var1 * 132)) + 64)
    if (1 if i32_load((var3 + (var1 * 132)) + 64) >= i32_load(var17 + 68) else 0):
        break
    if (1 if i32_load(var17 + 36) == 0 else 0):
        break
    var2 = (var3 + (var0 * 132))
    if i32_load((var3 + (var0 * 132)) + 96):
        break
    var0 = (var3 + (var1 * 132))
    var0 = func243(i32_load16_u((var3 + (var1 * 132)) + 112), i32_load16_u(var0 + 114), i32_load16_u(var2 + 110))
    if func243(i32_load16_u((var3 + (var1 * 132)) + 112), i32_load16_u(var0 + 114), i32_load16_u(var2 + 110)):
        break
    func29(var4, 1)
    break
    var9 = (var3 + (var0 * 132))
    var13 = i32_load16_u((var3 + (var0 * 132)) + 110)
    var15 = i32_load(9561692)
    var6 = i32_load(var9 + 96)
    if i32_load(var9 + 96):
        var2 = (var3 + (var1 * 132))
        var11 = i32_load16_u((var3 + (var1 * 132)) + 114)
        var18 = i32_load16_u(var2 + 112)
        break
    var10 = i32_load(((var15 + (var13 * 286704)) + 284164))
    if (1 if var11 == 8 else 0):
        i32_store8(var4 + 125, 1)
        var11 = 1
    var8 = (var3 + (var0 * 132))
    var7 = i32_load((var3 + (var0 * 132)) + 72)
    if (1 if var10 > i32_load((var3 + (var0 * 132)) + 72) else 0):
        var2 = i32_load(((i32_load8_u(var8 + 122) * 72) + 9263856))
        if (1 if i32_load(((i32_load8_u(var8 + 122) * 72) + 9263856)) != i32_load(var8 + 48) else 0):
            var13 = i32_load16_u(var9 + 110)
            var11 = i32_load8_u(var4 + 125)
            var15 = i32_load(9561692)
        var2 = i32_load(((var15 + (var13 * 286704)) + 284156))
        if (1 if (var11 & 255) == 1 else 0):
            func63(func37(var4, var2, 0.0, 0), var4, 13, var1, var2)
            break
        i32_store((i32_load(9215884) + (i32_load((var3 + (var0 * 132)) + 44) << 4)), (i32_load(9142848) + ((var2 & 0xFFFFFFFF) // 25)))
        break
    var5 = (var3 + (var1 * 132))
    var18 = i32_load16_u((var3 + (var1 * 132)) + 112)
    var2 = (i32_load16_u(var8 + 112) - i32_load16_u((var3 + (var1 * 132)) + 112))
    var11 = i32_load16_u(var5 + 114)
    var2 = (i32_load16_u(var8 + 114) - i32_load16_u(var5 + 114))
    var5 = (var15 + (var13 * 286704))
    var2 = i32_load(((var15 + (var13 * 286704)) + 284024))
    if (1 if ((((i32_load16_u(var8 + 112) - i32_load16_u((var3 + (var1 * 132)) + 112)) * var2) + ((i32_load16_u(var8 + 114) - i32_load16_u(var5 + 114)) * var2)) - 1) > (i32_load(((var15 + (var13 * 286704)) + 284024)) * var2) else 0):
        func117(var4, var1, 13)
        break
    i32_store(var8 + 72, (var7 - var10))
    var2 = (var5 + 281668)
    i32_store((var5 + 281668), (i32_load(var2) + var10))
    var8 = (var17 - -64)
    var2 = (i32_load(((var12 * 404) + 9568096) + 300) * i32_load(((var15 + (var13 * 286704)) + 284160)))
    i32_store((var17 - -64), ((1 if (1 if var2 < 100 else 0) else (((i32_load(((var12 * 404) + 9568096) + 300) * i32_load(((var15 + (var13 * 286704)) + 284160))) & 0xFFFFFFFF) // 100)) + var14))
    var10 = (var3 + (var1 * 132))
    var2 = i32_load(i32_load(9142424) + 48)
    if i32_load(i32_load(9142424) + 48):
        if (1 if i32_load8_u(9147152) == 0 else 0):
            break
    var7 = i32_load(9142440)
    break
    var7 = i32_load(9142440)
    var5 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * (var11 & 65535)) + var18) << 1)))
    if (1 if var2 == 2 else 0):
        if (1 if var5 > 1 else 0):
            break
        break
    if (1 if var5 == 0 else 0):
        break
    func80(float(var18), float((var11 & 65535)), i32_load(9142552), 32.0, float((var7 * 96)))
    var12 = i32_load16_u(var10 + 112)
    var2 = ((i32_load16_u(var10 + 112) << 5) - i32_load(9142952))
    var14 = i32_load16_u(var10 + 114)
    var2 = ((i32_load16_u(var10 + 114) << 5) - i32_load(9142956))
    if (1 if (((((i32_load16_u(var10 + 112) << 5) - i32_load(9142952)) * var2) + (((i32_load16_u(var10 + 114) << 5) - i32_load(9142956)) * var2)) - 1) > 9000000 else 0):
        break
    var5 = i32_load(39864)
    var2 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var7 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var14) + var12) << 1)))
    if (1 if var2 == 2 else 0):
        if (1 if var7 > 1 else 0):
            break
        break
    if (1 if var7 == 0 else 0):
        break
    i32_store(var16 + 8, var14)
    i32_store(var16 + 4, var12)
    i32_store(var16, var5)
    a_b()
    var2 = i32_load(var17 + 68)
    if (1 if i32_load(var17 + 68) <= i32_load(var8) else 0):
        i32_store(var8, var2)
        if var6:
            i32_store8(var4 + 125, 0)
        if i32_load(var9 + 96):
            break
        func117(var4, func243(i32_load16_u(var10 + 112), i32_load16_u(var10 + 114), i32_load16_u(var9 + 110)), 13)
        break
    if i32_load(var9 + 96):
        break
    var0 = i32_load(((i32_load8_u((var3 + (var0 * 132)) + 122) * 404) + 9568096) + 276)
    func291(var4, 13, var1, (i32_load(((i32_load8_u((var3 + (var0 * 132)) + 122) * 404) + 9568096) + 276) if var0 else 25))
    if (1 if i32_load(var9 + 96) == 0 else 0):
        break
    func29(var4, 1)
    if (1 if i32_load((var3 + (var1 * 132)) + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var3 + (var1 * 132)) + 28) else 0):
            break
    global global0
    global0 = (var16 + 16)
    return func28(1, 1)


# ==========================================================
# $func781
# ==========================================================
def func781(var0, var1):
    var2 = 0
    var2 = i32_load(9671128)
    var0 = (i32_load(9671128) + (var0 * 132))
    func29((i32_load(9671128) + (var0 * 132)), 1)
    var1 = (var2 + (var1 * 132))
    if (1 if i32_load8_u((var2 + (var1 * 132)) + 125) != 10 else 0):

