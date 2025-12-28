"""
Auto-generated from WAT. Contains 3 functions.
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
# $func36
# ==========================================================
def func36(var0):
    var1 = 0
    if (1 if var0 == 0 else 0):
        break
    var1 = i32_load(var0 + 16)
    if (1 if i32_load(var0 + 16) == 0 else 0):
        break
    if (1 if i32_load(var0 + 20) > var1 else 0):
        i32_store(var0 + 16, (var1 + 1))
        i32_store(var0 + 12, (i32_load(var0 + 12) + 8))
        i64_store(var0, (i64_load8_u(var1) | (i64_load(var0) << 8)))
        return
    if (1 if i32_load(var0 + 28) == 0 else 0):
        i32_store(var0 + 28, 1)
        i64_store(var0, (i64_load(var0) << 8))
        i32_store(var0 + 12, (i32_load(var0 + 12) + 8))
        return
    i32_store(var0 + 12, 0)
    return
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func39
# ==========================================================
def func39(var0, var1):
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
    if (1 if var1 >= 0 else 0):
        if (1 if var1 > 24 else 0):
            break
        if i32_load(var0 + 24):
            break
        var5 = (var0 + 20)
        var6 = i32_load(var0 + 20)
        var2 = (i32_load(var0 + 20) + var1)
        i32_store((var0 + 20), (i32_load(var0 + 20) + var1))
        var7 = i32_load(((var1 << 2) + 17888))
        var11 = i64_load(var0)
        if (1 if var2 <= 7 else 0):
            var4 = i32_load(var0 + 12)
            var3 = i32_load(var0 + 16)
            break
        var1 = i32_load(var0 + 16)
        var4 = i32_load(var0 + 12)
        var3 = (i32_load(var0 + 16) if (1 if var1 > var4 else 0) else i32_load(var0 + 12))
        var10 = var11
        while True:  # loop $label2
            if (1 if var1 == var3 else 0):
                break
            var10 = ((var10 & 0xFFFFFFFFFFFFFFFF) >> 8)
            i64_store(var0, ((var10 & 0xFFFFFFFFFFFFFFFF) >> 8))
            var12 = i64_load8_u((i32_load(var0 + 8) + var1))
            var8 = (var2 - 8)
            i32_store(var0 + 20, (var2 - 8))
            var1 = (var1 + 1)
            i32_store(var0 + 16, (var1 + 1))
            var10 = ((var12 << 56) | var10)
            i64_store(var0, ((var12 << 56) | var10))
            var9 = (1 if var2 > 15 else 0)
            var2 = var8
            if var9:
                continue
            break  # end loop
        var3 = var1
        if (1 if var3 > var4 else 0):
            break
        var1 = (var7 & i32(((var11 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((var6 & 63)))))
        if (1 if var3 != var4 else 0):
            break
        if (1 if var2 < 65 else 0):
            break
        i32_store(var0 + 24, 1)
        break
        i32_store(var0 + 24, 1)
        var5 = (var0 + 20)
        var1 = 0
        i32_store(var5, 0)
        return var1
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    return 3953


# ==========================================================
# $func40
# ==========================================================
def func40(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15):
    var16 = 0
    var17 = 0
    var18 = 0
    var19 = 0
    var20 = 0
    var21 = 0
    var22 = 0
    var23 = 0
    var24 = 0
    var25 = 0
    var26 = 0.0
    var27 = 0.0
    var28 = 0.0
    var16 = (global0 - 320)
    global global0
    global0 = (global0 - 320)
    if i32_load8_u(9142917):
        break
    if i32_load8_u(9142916):
        var12 = 0
        var14 = 0
        if (1 if var10 <= 14 else 0):
            var10 = (var10 << 4)
            var14 = ((((i32_load(((var10 << 4) + 1748)) << 8) + i32_load((var10 + 1744))) + (i32_load((var10 + 1752)) << 16)) + (i32_load((var10 + 1756)) << 24))
        if (1 if var9 == 0 else 0):
            break
        if (1 if i32_load(var9 + 20) == 0 else 0):
            break
        var10 = i32_load(var9 + 28)
        if (1 if i32_load(var9 + 28) == 2147483647 else 0):
            var10 = i32_load(59152)
            i32_store(59152, (i32_load(59152) + 1))
            var17 = i32_load(9568052)
            i32_store(var9 + 28, var10)
            var18 = i32_load(var9)
            var12 = i32_load(var9 + 4)
            var19 = i32_load(9568048)
            i32_store(9568048, (i32_load(9568048) + 1))
            i32_store(((var19 << 2) + 9563952), var9)
            i32_store(9568052, (var17 + ((var18 * (var12 + 2)) << 2)))
            var17 = i32_load(9568056)
            i32_store(var9 + 56, i32_load(9568056))
            i32_store(9568056, (var17 + ((var12 * i32_load(var9)) << 2)))
        var12 = (var10 + (var13 << 16))
        var9 = (i32_load(9142848) * 25)
        if (1 if var2 > 0.0 else 0):
            var2 = (((var2 * 0.5) / float((i32_load(9142440) * 96))) + 0.25)
        i32_store(var16 + 316, var11)
        i64_store(var16 + 308, 65535)
        i32_store(var16 + 304, var14)
        f64_store(var16 + 296, float(var8))
        i32_store(var16 + 292, var9)
        i32_store(var16 + 288, var12)
        f64_store(var16 + 280, float(var5))
        f64_store(var16 + 272, float(var4))
        f64_store(var16 + 264, float(var3))
        f64_store(var16 + 256, float(var2))
        f64_store(var16 + 248, float(var1))
        f64_store(var16 + 240, float(var0))
        a_b()
        break
    var8 = (var8 if (1 if var8 != 0.0 else 0) else -1.0)
    if (1 if ((1 if var6 == 0.0 else 0) & (1 if var7 == 0.0 else 0)) == 0 else 0):
        var6 = (-var6)
        break
    var6 = float(i32_load(var9))
    var17 = (i32_load(var9 + 20) * i32_load(var9 + 16))
    if (1 if (i32_load(var9 + 20) * i32_load(var9 + 16)) == 0 else 0):
        break
    var26 = float(float((i32_load(var9 + 4) // var17)))
    i32_store(var16 + 224, var11)
    f64_store(var16 + 216, float(var15))
    f64_store(var16 + 208, float(var8))
    f64_store(var16 + 200, var26)
    f64_store(var16 + 192, float(var6))
    a_b()
    var17 = i32_load8_u(9142916)
    var6 = float(i32_load(var9 + 12))
    var7 = float(i32_load(var9 + 8))
    if (1 if var2 == -55.0 else 0):
        break
    if (1 if var17 == 0 else 0):
        break
    var2 = (((var2 * 0.5) / float((i32_load(9142440) * 96))) + 0.25)
    i32_store(var16 + 184, var11)
    f64_store(var16 + 176, float(var2))
    f64_store(var16 + 168, float((var1 - (0.0 if var17 else var6))))
    f64_store(var16 + 160, float((var0 - (0.0 if var17 else var7))))
    a_b()
    var26 = float(var5)
    var27 = float(var4)
    var28 = float(var3)
    if i32_load8_u(9142916):
        i32_store(var16 + 152, var11)
        f64_store(var16 + 144, var26)
        f64_store(var16 + 136, var27)
        f64_store(var16 + 128, var28)
        a_b()
        break
    f64_store(var16 + 96, var26)
    i32_store(var16 + 112, var11)
    f64_store(var16 + 104, float(float((i32_load(9142848) * 25))))
    f64_store(var16 + 80, var28)
    f64_store(var16 + 88, var27)
    a_b()
    if (1 if var14 == 0 else 0):
        var19 = i32_load(var9 + 24)
    var22 = i32_load(var9 + 16)
    var23 = i32_load(var9 + 32)
    var24 = i32_load(var9 + 20)
    if i32_load(var9 + 20):
        var18 = i32_load8_u(9142916)
        var14 = i32_load(var9 + 28)
        if (1 if i32_load(var9 + 28) == 2147483647 else 0):
            if var18:
                var14 = i32_load(59152)
                i32_store(59152, (i32_load(59152) + 1))
                var20 = i32_load(9568052)
                var21 = i32_load(var9)
                break
            var21 = i32_load(var9)
            var20 = i32_load(9568052)
            var14 = ((i32_load(var9) + i32_load(9140308)) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2))
            i32_store(var9 + 28, var14)
            var17 = i32_load(var9 + 4)
            var25 = i32_load(9568048)
            i32_store(9568048, (i32_load(9568048) + 1))
            i32_store(((var25 << 2) + 9563952), var9)
            i32_store(9568052, (((var21 * (var17 + 2)) << 2) + var20))
            if (1 if var18 == 0 else 0):
                break
            var10 = i32_load(9568056)
            i32_store(var9 + 56, i32_load(9568056))
            i32_store(9568056, (var10 + ((var17 * i32_load(var9)) << 2)))
            break
        if var18:
            break
        var17 = i32_load(var9 + 4)
        var2 = float((i32_load(9142848) * 25))
        break
    var9 = 0
    var2 = float((i32_load(9142848) * 25))
    if i32_load8_u(9142916):
        break
    var8 = 0.0
    i32_store(var16 + 16, var10)
    f64_store(var16 + 24, float(float(((((200 if (1 if var23 == 27 else 0) else (var12 * 100)) + var22) << 16) + var19))))
    i32_store(var16 + 32, var11)
    f64_store(var16 + 8, float(var2))
    f64_store(var16, float((var8 / float(i32_load(59156)))))
    a_b()
    break
    var9 = (var14 + (var13 << 16))
    var2 = float((i32_load(9142848) * 25))
    i32_store((var16 - -64), var11)
    i32_store(var16 + 48, var9)
    f64_store(var16 + 56, float(var2))
    a_b()
    global global0
    global0 = (var16 + 320)
    return (var16 + 48)

