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
# $func359
# ==========================================================
def func359(var0, var1):
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
    var5 = i32_load(var0 + 124)
    var5 = i32_load(var0 + 120)
    var9 = (i32_load(var0 + 124) if (1 if i32_load(var0 + 120) < i32_load(var0 + 140) else 0) else ((var5 & 0xFFFFFFFF) >> 2))
    var3 = i32_load(var0 + 108)
    var2 = ((i32_load(var0 + 108) - i32_load(var0 + 44)) + 262)
    var12 = (((i32_load(var0 + 108) - i32_load(var0 + 44)) + 262) if (1 if var2 <= var3 else 0) else 0)
    var2 = i32_load(var0 + 144)
    var8 = i32_load(var0 + 116)
    var13 = (i32_load(var0 + 144) if (1 if var2 < var8 else 0) else i32_load(var0 + 116))
    var14 = i32_load(var0 + 56)
    var7 = (i32_load(var0 + 56) + var3)
    var15 = ((i32_load(var0 + 56) + var3) + 258)
    var3 = (var5 + var7)
    var10 = i32_load8_u((var5 + var7))
    var11 = i32_load8_u((var3 - 1))
    var16 = i32_load(var0 + 52)
    var17 = i32_load(var0 + 64)
    while True:  # loop $label10
        var4 = (var1 + var14)
        var3 = ((var1 + var14) + var5)
        if (1 if i32_load8_u(((var1 + var14) + var5)) != var10 else 0):
            break
        if (1 if i32_load8_u((var3 - 1)) != var11 else 0):
            break
        if (1 if i32_load8_u(var4) != i32_load8_u(var7) else 0):
            break
        var3 = 2
        if (1 if i32_load8_u(var4 + 1) != i32_load8_u(var7 + 1) else 0):
            break
        while True:  # loop $label8
            var2 = (var3 + var7)
            if (1 if i32_load8_u((var3 + var7) + 1) == i32_load8_u(var4 + 3) else 0):
                if (1 if i32_load8_u(var2 + 2) != i32_load8_u(var4 + 4) else 0):
                    break
                if (1 if i32_load8_u(var2 + 3) != i32_load8_u(var4 + 5) else 0):
                    break
                if (1 if i32_load8_u(var2 + 4) != i32_load8_u(var4 + 6) else 0):
                    break
                if (1 if i32_load8_u(var2 + 5) != i32_load8_u(var4 + 7) else 0):
                    break
                if (1 if i32_load8_u(var2 + 6) != i32_load8_u(var4 + 8) else 0):
                    break
                if (1 if i32_load8_u(var2 + 7) != i32_load8_u(var4 + 9) else 0):
                    break
                var2 = (var3 + 8)
                var6 = (var7 + (var3 + 8))
                if (1 if i32_load8_u((var7 + (var3 + 8))) != i32_load8_u(var4 + 10) else 0):
                    break
                var4 = (var4 + 8)
                var18 = (1 if var3 < 250 else 0)
                var3 = var2
                if var18:
                    continue
                break
            break  # end loop
        var6 = (var2 + 1)
        break
        var6 = (var2 + 2)
        break
        var6 = (var2 + 3)
        break
        var6 = (var2 + 4)
        break
        var6 = (var2 + 5)
        break
        var6 = (var2 + 6)
        break
        var6 = (var2 + 7)
        var2 = (var6 - var15)
        var3 = ((var6 - var15) + 258)
        if (1 if ((var6 - var15) + 258) <= var5 else 0):
            break
        i32_store(var0 + 112, var1)
        if (1 if var3 >= var13 else 0):
            var5 = var3
            break
        var10 = i32_load8_u((var3 + var7))
        var11 = i32_load8_u((var2 + var7) + 257)
        var5 = var3
        var1 = i32_load16_u((var17 + ((var1 & var16) << 1)))
        if (1 if var12 >= i32_load16_u((var17 + ((var1 & var16) << 1))) else 0):
            break
        var9 = (var9 - 1)
        if (var9 - 1):
            continue
        break  # end loop
    return (var5 if (1 if var5 < var8 else 0) else var8)


# ==========================================================
# $func362
# ==========================================================
def func362(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var2 = 2
    if (1 if var1 <= 2 else 0):
        var3 = i32_load(var0 + 283960)
        break
    var5 = (var1 - 2)
    var7 = ((var1 - 2) & 3)
    var3 = i32_load(var0 + 283960)
    var6 = i32_load(9561692)
    if (1 if (var1 - 3) >= 3 else 0):
        var9 = (var5 & -4)
        var1 = 0
        while True:  # loop $label1
            var5 = (var6 + (var2 * 286704))
            var4 = ((((var4 + (1 if i32_load((var6 + (var2 * 286704)) + 283960) == var3 else 0)) + (1 if i32_load((var6 + ((var2 | 1) * 286704)) + 283960) == var3 else 0)) + (1 if i32_load((var5 + 857368)) == var3 else 0)) + (1 if i32_load((var5 + 1144072)) == var3 else 0))
            var2 = (var2 + 4)
            var1 = (var1 + 4)
            if (1 if (var1 + 4) != var9 else 0):
                continue
            break  # end loop
    if var7:
        while True:  # loop $label2
            var4 = (var4 + (1 if i32_load((var6 + (var2 * 286704)) + 283960) == var3 else 0))
            var2 = (var2 + 1)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != var7 else 0):
                continue
            break  # end loop
    var2 = (var4 * 20)
    if (1 if (var4 * 20) < i32_load16_u(((var3 << 1) + 9142944)) else 0):
        var3 = i32_load(((var3 << 2) + 9142928))
        var2 = (var2 << 1)
        var1 = (i32_load(((var3 << 2) + 9142928)) + (var2 << 1))
        i32_store16(var0, i32_load16_u((i32_load(((var3 << 2) + 9142928)) + (var2 << 1))))
        i32_store16(var0 + 2, i32_load16_u((var3 + (var2 | 2))))
        i32_store16(var0 + 4, i32_load16_u((var3 + (var2 | 4))))
        i32_store16(var0 + 6, i32_load16_u((var3 + (var2 | 6))))
        i32_store16(var0 + 8, i32_load16_u(var1 + 8))
        i32_store16(var0 + 10, i32_load16_u(var1 + 10))
        i32_store16(var0 + 12, i32_load16_u(var1 + 12))
        i32_store16(var0 + 14, i32_load16_u(var1 + 14))
        i32_store16(var0 + 16, i32_load16_u(var1 + 16))
        i32_store16(var0 + 18, i32_load16_u(var1 + 18))
        i32_store16(var0 + 20, i32_load16_u(var1 + 20))
        i32_store16(var0 + 22, i32_load16_u(var1 + 22))
        i32_store16(var0 + 24, i32_load16_u(var1 + 24))
        i32_store16(var0 + 26, i32_load16_u(var1 + 26))
        i32_store16(var0 + 28, i32_load16_u(var1 + 28))
        i32_store16(var0 + 30, i32_load16_u(var1 + 30))
        i32_store16(var0 + 32, i32_load16_u(var1 + 32))
        i32_store16(var0 + 34, i32_load16_u(var1 + 34))
        i32_store16(var0 + 36, i32_load16_u(var1 + 36))
        var3 = 19
        break
    i32_store16(var0 + 8, 101)
    i64_store(var0, 32088563964837972)
    var3 = 5
    var2 = 100
    i32_store16((var0 + (var3 << 1)), var2)
    return i32_load16_u(var1 + 38)

