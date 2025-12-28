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
# $func517
# ==========================================================
def func517(var0, var1, param2):
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
    var13 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var4 = i32_load(9671128)
    var14 = (i32_load(9671128) + (var1 * 132))
    var5 = (var4 + (var0 * 132))
    var3 = i32_load8_u((var4 + (var0 * 132)) + 125)
    if (1 if i32_load8_u((var4 + (var0 * 132)) + 125) == 1 else 0):
        var2 = ((i32_load8_u(var14 + 122) * 404) + 9568096)
        var8 = i32_load(((i32_load8_u(var14 + 122) * 404) + 9568096) + 220)
        var10 = i32_load16_u(var14 + 114)
        var15 = (i32_load(((i32_load8_u(var14 + 122) * 404) + 9568096) + 220) + i32_load16_u(var14 + 114))
        var3 = i32_load(var2 + 216)
        var12 = i32_load16_u(var14 + 112)
        var6 = (i32_load(var2 + 216) + i32_load16_u(var14 + 112))
        var9 = i32_load16_u(var5 + 114)
        var7 = i32_load16_u(var5 + 112)
        var2 = (1 if i32_load16_u(var5 + 112) < var12 else 0)
        if (1 if i32_load16_u(var5 + 112) < var12 else 0):
            break
        if (1 if var6 <= var7 else 0):
            break
        if (1 if var9 < var10 else 0):
            break
        if (1 if var9 >= var15 else 0):
            break
        var2 = ((var8 // 2) + var10)
        var8 = (-1 if (1 if var2 < var9 else 0) else (1 if ((var8 // 2) + var10) != var9 else 0))
        var2 = ((var3 // 2) + var12)
        break
        var8 = (1 if (1 if var9 < var10 else 0) else (-1 if (1 if var9 >= var15 else 0) else 0))
        var7 = (1 if var2 else (-1 if (1 if var6 <= var7 else 0) else 0))
        var3 = 6
        var2 = (((var8 * 3) + var7) + 4)
        if (1 if (((var8 * 3) + var7) + 4) <= 8 else 0):
            var3 = i32_load8_u((var2 + 10184))
        var2 = (var4 + (var0 * 132))
        i32_store8((var4 + (var0 * 132)) + 124, var3)
        var2 = ((i32_load8_u(var2 + 122) * 72) + 9263856)
        if i32_load(((i32_load8_u(var2 + 122) * 72) + 9263856) + 12):
            break
        var6 = (var4 + (var0 * 132))
        var2 = i32_load(((i32_load((i32_load(9215884) + (i32_load((var4 + (var0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if i32_load(((i32_load((i32_load(9215884) + (i32_load((var4 + (var0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32):
            # call_indirect via table[var2]
        if (1 if i32_load8_u(var5 + 125) == 3 else 0):
            break
        var3 = i32_load(var6 + 44)
        if i32_load(var6 + 44):
            var2 = i32_load(9142848)
            var8 = i32_load(9215884)
            i32_store((i32_load(9215884) + (var3 << 4)) + 4, 46)
            i32_store((var8 + (i32_load(var6 + 44) << 4)) + 8, i32_load((var4 + (var0 * 132)) + 28))
            i32_store((var8 + (i32_load(var6 + 44) << 4)) + 12, var1)
            i32_store((var8 + (i32_load(var6 + 44) << 4)), (var2 + 1))
            break
        i32_store(var6 + 44, ((Ua(25, 46, i32_load((var4 + (var0 * 132)) + 28), var1) & 0xFFFFFFFF) >> 2))
        break
    if (1 if i32_load8_u(var14 + 125) != 3 else 0):
        var15 = (var4 + (var1 * 132))
        var11 = (var4 + (var0 * 132))
        if (1 if i32_load((var4 + (var1 * 132)) + 84) < i32_load((var4 + (var0 * 132)) + 84) else 0):
            break
    var2 = (var4 + (var0 * 132))
    if i32_load((var4 + (var0 * 132)) + 96):
        break
    var0 = (var4 + (var1 * 132))
    var0 = func208(i32_load16_u((var4 + (var1 * 132)) + 112), i32_load16_u(var0 + 114), i32_load16_u(var2 + 110), i32_load(var2 + 84))
    if func208(i32_load16_u((var4 + (var1 * 132)) + 112), i32_load16_u(var0 + 114), i32_load16_u(var2 + 110), i32_load(var2 + 84)):
        break
    func29(var5, 1)
    break
    var6 = i32_load(var11 + 96)
    if (1 if i32_load(var11 + 96) == 0 else 0):
        var10 = i32_load(9561692)
        var7 = i32_load16_u(var11 + 110)
        var12 = i32_load(((i32_load(9561692) + (i32_load16_u(var11 + 110) * 286704)) + 284304))
        if (1 if var3 == 8 else 0):
            i32_store8(var5 + 125, 1)
            var3 = 1
        var9 = (var4 + (var0 * 132))
        var8 = i32_load((var4 + (var0 * 132)) + 72)
        if (1 if var12 > i32_load((var4 + (var0 * 132)) + 72) else 0):
            var2 = i32_load(((i32_load8_u(var9 + 122) * 72) + 9263856))
            if (1 if i32_load(((i32_load8_u(var9 + 122) * 72) + 9263856)) != i32_load(var9 + 48) else 0):
                var7 = i32_load16_u(var11 + 110)
                var10 = i32_load(9561692)
                var3 = i32_load8_u(var5 + 125)
            var2 = i32_load(((var10 + (var7 * 286704)) + 284156))
            if (1 if var3 == 1 else 0):
                func63(func37(var5, var2, 0.0, 0), var5, 46, var1, var2)
                break
            i32_store((i32_load(9215884) + (i32_load((var4 + (var0 * 132)) + 44) << 4)), (i32_load(9142848) + ((var2 & 0xFFFFFFFF) // 25)))
            break
        var3 = (var4 + (var1 * 132))
        var2 = (i32_load16_u(var9 + 112) - i32_load16_u((var4 + (var1 * 132)) + 112))
        var2 = (i32_load16_u(var9 + 114) - i32_load16_u(var3 + 114))
        var3 = (var10 + (var7 * 286704))
        var2 = i32_load(((var10 + (var7 * 286704)) + 284096))
        if (1 if ((((i32_load16_u(var9 + 112) - i32_load16_u((var4 + (var1 * 132)) + 112)) * var2) + ((i32_load16_u(var9 + 114) - i32_load16_u(var3 + 114)) * var2)) - 1) > (i32_load(((var10 + (var7 * 286704)) + 284096)) * var2) else 0):
            func117(var5, var1, 46)
            break
        i32_store(var9 + 72, (var8 - var12))
        var2 = (var3 + 281668)
        i32_store((var3 + 281668), (i32_load(var2) + var12))
    var0 = ((i32_load8_u((var4 + (var0 * 132)) + 122) * 72) + 9263856)
    if i32_load(((i32_load8_u((var4 + (var0 * 132)) + 122) * 72) + 9263856) + 12):
        var0 = (var4 + (var1 * 132))
        break
    var2 = i32_load(var11 + 84)
    if (1 if i32_load(var11 + 84) > i32_load(var15 + 84) else 0):
        var8 = (var4 + (var1 * 132))
        var7 = i32_load16_u((var4 + (var1 * 132)) + 114)
        var6 = i32_load16_u(var8 + 112)
        var0 = i32_load(i32_load(9142424) + 48)
        if i32_load(i32_load(9142424) + 48):
            if (1 if i32_load8_u(9147152) == 0 else 0):
                break
        var3 = i32_load(9142440)
        break
        var3 = i32_load(9142440)
        var2 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var7) + var6) << 1)))
        if (1 if var0 == 2 else 0):
            if (1 if var2 > 1 else 0):
                break
            break
        if (1 if var2 == 0 else 0):
            break
        func80(float(var6), float((var7 - 1)), i32_load(9142584), 32.0, float((var3 * 96)))
        var7 = i32_load16_u(var8 + 114)
        var6 = i32_load16_u(var8 + 112)
        var0 = ((var6 << 5) - i32_load(9142952))
        var0 = ((var7 << 5) - i32_load(9142956))
        if (1 if (((((var6 << 5) - i32_load(9142952)) * var0) + (((var7 << 5) - i32_load(9142956)) * var0)) - 1) > 9000000 else 0):
            break
        var2 = i32_load(39892)
        var0 = i32_load(i32_load(9142424) + 48)
        if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
            break
        if i32_load8_u(9147152):
            break
        var3 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var7) + var6) << 1)))
        if (1 if var0 == 2 else 0):
            if (1 if var3 > 1 else 0):
                break
            break
        if (1 if var3 == 0 else 0):
            break
        i32_store(var13 + 8, var7)
        i32_store(var13 + 4, var6)
        i32_store(var13, var2)
        a_b()
        var2 = (var4 + (var1 * 132))
        var0 = (i32_load(var2 + 80) + 100)
        i32_store((var4 + (var1 * 132)) + 80, (i32_load(var2 + 80) + 100))
        var0 = i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284008))
        if (1 if var0 >= (((i32_load(var15 + 84) * 100) & 0xFFFFFFFF) // (1 if (1 if var0 <= 1 else 0) else i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284008)))) else 0):
            func198(var14)
        if i32_load(var11 + 96):
            break
        func291(var5, 46, var1, 1400)
        break
    if var6:
        i32_store8(var5 + 125, 0)
    if i32_load(var11 + 96):
        break
    var0 = (var4 + (var1 * 132))
    func117(var5, func208(i32_load16_u((var4 + (var1 * 132)) + 112), i32_load16_u(var0 + 114), i32_load16_u(var11 + 110), var2), 46)
    if (1 if i32_load(var11 + 96) == 0 else 0):
        break
    func29(var5, 1)
    if (1 if i32_load((var4 + (var1 * 132)) + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var4 + (var1 * 132)) + 28) else 0):
            break
    global global0
    global0 = (var13 + 16)
    return func28(1, 1)


# ==========================================================
# $func723
# ==========================================================
def func723(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var2 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var6 = i32_load(9671128)
    var7 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load(9142848) < (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        func29(var7, 1)
        break
    if (1 if i32_load8_u(var7 + 125) == 3 else 0):
        break
    var3 = (var6 + (var0 * 132))
    if (1 if i32_load8_u((var6 + (var0 * 132)) + 128) == 0 else 0):
        break
    i32_store8(var3 + 127, 0)
    var8 = i32_load(var3 + 40)
    if (1 if i32_load(var3 + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var2 + 36, var8)
        i32_store(var2 + 32, 0)
        a_b()
        break
    var4 = i32_load16_u(var3 + 110)
    i32_store(var2 + 20, var8)
    i32_store(var2 + 16, (var4 + 16))
    a_b()
    i32_store8(var3 + 128, 0)
    var8 = i32_load(9671128)
    var3 = (i32_load(9671128) + (var1 * 132))
    var4 = i32_load16_u(var3 + 114)
    var5 = i32_load16_u(var3 + 112)
    var10 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var9 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var4) + var5) << 1)))
    if (1 if var10 == 2 else 0):
        if (1 if var9 > 1 else 0):
            break
        break
    if (1 if var9 == 0 else 0):
        break
    var5 = ((i32_load8_u(var3 + 122) * 404) + 9568096)
    func375(((var5 + ((i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1)) << 5), ((((i32_load(var5 + 220) & 0xFFFFFFFF) >> 1) + var4) << 5))
    var6 = (var6 + (var0 * 132))
    var0 = i32_load16_u((var6 + (var0 * 132)) + 112)
    var4 = ((i32_load16_u((var6 + (var0 * 132)) + 112) << 5) - i32_load(9142952))
    var4 = i32_load16_u(var6 + 114)
    var5 = ((i32_load16_u(var6 + 114) << 5) - i32_load(9142956))
    if (1 if (((((i32_load16_u((var6 + (var0 * 132)) + 112) << 5) - i32_load(9142952)) * var4) + (((i32_load16_u(var6 + 114) << 5) - i32_load(9142956)) * var5)) - 1) > 9000000 else 0):
        break
    var9 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var5 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var4) + var0) << 1)))
    if (1 if var9 == 2 else 0):
        if (1 if var5 > 1 else 0):
            break
        break
    if (1 if var5 == 0 else 0):
        break
    i32_store(var2 + 8, var4)
    i32_store(var2 + 4, var0)
    i32_store(var2, i32_load(((((i32_load(9142848) + var0) & 1) << 2) + 57612)))
    a_b()
    var0 = (i32_load(((i32_load8_u((var8 + (var1 * 132)) + 122) * 404) + 9568096) + 308) * i32_load(((i32_load(9561692) + (i32_load16_u(var6 + 110) * 286704)) + 284224)))
    global global0
    global0 = (var2 + 48)
    return func81(var3, var7, (1 if (1 if var0 < 100 else 0) else (((i32_load(((i32_load8_u((var8 + (var1 * 132)) + 122) * 404) + 9568096) + 308) * i32_load(((i32_load(9561692) + (i32_load16_u(var6 + 110) * 286704)) + 284224))) & 0xFFFFFFFF) // 100)), 1)

