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
# $func381
# ==========================================================
def func381(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    var13 = 0
    i64_store(var0, 0)
    i64_store(var0 + 39, 0)
    i64_store(var0 + 32, 0)
    i64_store(var0 + 24, 0)
    i64_store(var0 + 16, 0)
    i64_store(var0 + 8, 0)
    i32_store(var0 + 52, 1)
    i32_store(var0 + 48, func26(4))
    i32_store(var0 + 68, 1)
    i64_store(var0 + 56, 4294967296)
    i32_store(var0 + 64, func26(4))
    i32_store(var0 + 84, 1)
    i64_store(var0 + 72, 4294967296)
    i32_store(var0 + 80, func26(4))
    i32_store(var0 + 100, 1)
    i64_store(var0 + 88, 4294967296)
    i32_store(var0 + 96, func26(4))
    i64_store(var0 + 104, 4294967296)
    var8 = i32_load(var2)
    var5 = (i32_load(var2) + 1)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store(var0, i32_load((var1 + (var8 << 2))))
    var7 = (var8 + 2)
    i32_store(var2, (var8 + 2))
    i32_store(var0 + 4, i32_load((var1 + (var5 << 2))))
    var5 = (var8 + 3)
    i32_store(var2, (var8 + 3))
    i32_store(var0 + 8, i32_load((var1 + (var7 << 2))))
    var7 = (var8 + 4)
    i32_store(var2, (var8 + 4))
    i32_store(var0 + 12, i32_load((var1 + (var5 << 2))))
    var5 = (var8 + 5)
    i32_store(var2, (var8 + 5))
    i32_store(var0 + 16, i32_load((var1 + (var7 << 2))))
    var7 = (var8 + 6)
    i32_store(var2, (var8 + 6))
    i32_store(var0 + 20, i32_load((var1 + (var5 << 2))))
    var5 = (var8 + 7)
    i32_store(var2, (var8 + 7))
    i32_store(var0 + 24, i32_load((var1 + (var7 << 2))))
    var7 = (var8 + 8)
    i32_store(var2, (var8 + 8))
    i32_store(var0 + 28, i32_load((var1 + (var5 << 2))))
    var5 = (var8 + 9)
    i32_store(var2, (var8 + 9))
    i32_store(var0 + 32, i32_load((var1 + (var7 << 2))))
    var7 = (var8 + 10)
    i32_store(var2, (var8 + 10))
    i32_store(var0 + 36, i32_load((var1 + (var5 << 2))))
    var5 = (var8 + 11)
    i32_store(var2, (var8 + 11))
    i32_store(var0 + 40, i32_load((var1 + (var7 << 2))))
    var7 = (var8 + 12)
    i32_store(var2, (var8 + 12))
    i32_store8(var0 + 44, (1 if i32_load((var1 + (var5 << 2))) != 0 else 0))
    var5 = (var8 + 13)
    i32_store(var2, (var8 + 13))
    i32_store8(var0 + 45, (1 if i32_load((var1 + (var7 << 2))) != 0 else 0))
    var7 = (var8 + 14)
    i32_store(var2, (var8 + 14))
    i32_store8(var0 + 46, (1 if i32_load((var1 + (var5 << 2))) != 0 else 0))
    var5 = (var8 + 15)
    i32_store(var2, (var8 + 15))
    var12 = i32_load((var1 + (var7 << 2)))
    i32_store(var0 + 192, i32_load((var1 + (var7 << 2))))
    if (1 if var12 == 0 else 0):
        break
    if (1 if var12 >= 4 else 0):
        var11 = (var12 & -4)
        var13 = (var0 + 112)
        while True:  # loop $label1
            var7 = (var5 + 1)
            i32_store(var2, (var5 + 1))
            var10 = (var6 << 1)
            i32_store16((var13 + (var6 << 1)), i32_load((var1 + (var5 << 2))))
            var8 = (var5 + 2)
            i32_store(var2, (var5 + 2))
            i32_store16((var13 + (var10 | 2)), i32_load((var1 + (var7 << 2))))
            var7 = (var5 + 3)
            i32_store(var2, (var5 + 3))
            i32_store16((var13 + (var10 | 4)), i32_load((var1 + (var8 << 2))))
            var5 = (var5 + 4)
            i32_store(var2, (var5 + 4))
            i32_store16((var13 + (var10 | 6)), i32_load((var1 + (var7 << 2))))
            var6 = (var6 + 4)
            var9 = (var9 + 4)
            if (1 if (var9 + 4) != var11 else 0):
                continue
            break  # end loop
    var7 = (var12 & 3)
    if (1 if (var12 & 3) == 0 else 0):
        break
    var8 = 0
    var9 = var5
    while True:  # loop $label2
        var5 = (var9 + 1)
        i32_store(var2, (var9 + 1))
        i32_store16((var0 + (var6 << 1)) + 112, i32_load((var1 + (var9 << 2))))
        var6 = (var6 + 1)
        var9 = var5
        var8 = (var8 + 1)
        if (1 if (var8 + 1) != var7 else 0):
            continue
        break  # end loop
    var6 = (var5 + 1)
    i32_store(var2, (var5 + 1))
    var8 = i32_load((var1 + (var5 << 2)))
    if i32_load((var1 + (var5 << 2))):
        var9 = 0
        while True:  # loop $label4
            var5 = i32_load(var2)
            i32_store(var2, (i32_load(var2) + 1))
            var7 = i32_load((var1 + (var5 << 2)))
            var5 = i32_load(var0 + 56)
            if (1 if i32_load(var0 + 56) != i32_load(var0 + 52) else 0):
                var6 = i32_load(var0 + 48)
                break
            var11 = (i32_load(var0 + 60) + var5)
            i32_store(var0 + 52, (i32_load(var0 + 60) + var5))
            var10 = i32_load(var0 + 48)
            var6 = func26((-1 if (1 if var11 > 1073741823 else 0) else (var11 << 2)))
            if var5:
                # Unknown: memory.copy []
            if var10:
                var5 = i32_load(var0 + 56)
            i32_store(var0 + 48, var6)
            i32_store(var0 + 56, (var5 + 1))
            i32_store((var6 + (var5 << 2)), var7)
            var9 = (var9 + 1)
            if (1 if (var9 + 1) != var8 else 0):
                continue
            break  # end loop
        var6 = i32_load(var2)
    var5 = (var6 + 1)
    i32_store(var2, (var6 + 1))
    var8 = i32_load((var1 + (var6 << 2)))
    if i32_load((var1 + (var6 << 2))):
        var9 = 0
        while True:  # loop $label6
            var5 = i32_load(var2)
            i32_store(var2, (i32_load(var2) + 1))
            var7 = i32_load((var1 + (var5 << 2)))
            var5 = i32_load(var0 + 72)
            if (1 if i32_load(var0 + 72) != i32_load(var0 + 68) else 0):
                var6 = i32_load(var0 + 64)
                break
            var11 = (i32_load(var0 + 76) + var5)
            i32_store(var0 + 68, (i32_load(var0 + 76) + var5))
            var10 = i32_load(var0 + 64)
            var6 = func26((-1 if (1 if var11 > 1073741823 else 0) else (var11 << 2)))
            if var5:
                # Unknown: memory.copy []
            if var10:
                var5 = i32_load(var0 + 72)
            i32_store(var0 + 64, var6)
            i32_store(var0 + 72, (var5 + 1))
            i32_store((var6 + (var5 << 2)), var7)
            var9 = (var9 + 1)
            if (1 if (var9 + 1) != var8 else 0):
                continue
            break  # end loop
        var5 = i32_load(var2)
    var6 = (var5 + 1)
    i32_store(var2, (var5 + 1))
    var8 = i32_load((var1 + (var5 << 2)))
    if i32_load((var1 + (var5 << 2))):
        var9 = 0
        while True:  # loop $label8
            var5 = i32_load(var2)
            i32_store(var2, (i32_load(var2) + 1))
            var7 = i32_load((var1 + (var5 << 2)))
            var5 = i32_load(var0 + 88)
            if (1 if i32_load(var0 + 88) != i32_load(var0 + 84) else 0):
                var6 = i32_load(var0 + 80)
                break
            var11 = (i32_load(var0 + 92) + var5)
            i32_store(var0 + 84, (i32_load(var0 + 92) + var5))
            var10 = i32_load(var0 + 80)
            var6 = func26((-1 if (1 if var11 > 1073741823 else 0) else (var11 << 2)))
            if var5:
                # Unknown: memory.copy []
            if var10:
                var5 = i32_load(var0 + 88)
            i32_store(var0 + 80, var6)
            i32_store(var0 + 88, (var5 + 1))
            i32_store((var6 + (var5 << 2)), var7)
            var9 = (var9 + 1)
            if (1 if (var9 + 1) != var8 else 0):
                continue
            break  # end loop
        var6 = i32_load(var2)
    i32_store(var2, (var6 + 1))
    var8 = i32_load((var1 + (var6 << 2)))
    if i32_load((var1 + (var6 << 2))):
        var9 = 0
        while True:  # loop $label10
            var5 = i32_load(var2)
            i32_store(var2, (i32_load(var2) + 1))
            var7 = i32_load((var1 + (var5 << 2)))
            var5 = i32_load(var0 + 104)
            if (1 if i32_load(var0 + 104) != i32_load(var0 + 100) else 0):
                var6 = i32_load(var0 + 96)
                break
            var11 = (i32_load(var0 + 108) + var5)
            i32_store(var0 + 100, (i32_load(var0 + 108) + var5))
            var10 = i32_load(var0 + 96)
            var6 = func26((-1 if (1 if var11 > 1073741823 else 0) else (var11 << 2)))
            if var5:
                # Unknown: memory.copy []
            if var10:
                var5 = i32_load(var0 + 104)
            i32_store(var0 + 96, var6)
            i32_store(var0 + 104, (var5 + 1))
            i32_store((var6 + (var5 << 2)), var7)
            var9 = (var9 + 1)
            if (1 if (var9 + 1) != var8 else 0):
                continue
            break  # end loop
    var2 = i32_load(var0 + 56)
    var7 = i32_load(9142892)
    var5 = (i32_load(9142892) + 1)
    if (1 if i32_load(var0 + 56) >= (i32_load(9142892) + 1) else 0):
        break
    while True:  # loop $label13
        if (1 if i32_load(var0 + 52) != var2 else 0):
            var1 = i32_load(var0 + 48)
            break
        var1 = (i32_load(var0 + 60) + var2)
        i32_store(var0 + 52, (i32_load(var0 + 60) + var2))
        var9 = i32_load(var0 + 48)
        var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        if var2:
            # Unknown: memory.copy []
        if var9:
            var2 = i32_load(var0 + 56)
        i32_store(var0 + 48, var1)
        i32_store(var0 + 56, (var2 + 1))
        i32_store((var1 + (var2 << 2)), 1)
        var2 = i32_load(var0 + 56)
        if (1 if i32_load(var0 + 56) < var5 else 0):
            continue
        break  # end loop
    if (1 if var3 != 1 else 0):
        break
    i32_store((i32_load(var0 + 48) + (var7 << 2)), 0)
    var2 = i32_load(var0 + 72)
    if (1 if i32_load(var0 + 72) >= var5 else 0):
        break
    while True:  # loop $label16
        if (1 if i32_load(var0 + 68) != var2 else 0):
            var1 = i32_load(var0 + 64)
            break
        var1 = (i32_load(var0 + 76) + var2)
        i32_store(var0 + 68, (i32_load(var0 + 76) + var2))
        var9 = i32_load(var0 + 64)
        var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        if var2:
            # Unknown: memory.copy []
        if var9:
            var2 = i32_load(var0 + 72)
        i32_store(var0 + 64, var1)
        i32_store(var0 + 72, (var2 + 1))
        i32_store((var1 + (var2 << 2)), 1)
        var2 = i32_load(var0 + 72)
        if (1 if i32_load(var0 + 72) < var5 else 0):
            continue
        break  # end loop
    if (1 if var3 != 1 else 0):
        break
    i32_store((i32_load(var0 + 64) + (var7 << 2)), 0)
    if (1 if var3 == 0 else 0):
        break
    if (1 if var4 > 466 else 0):
        break
    var1 = (var7 << 2)
    i32_store(((var7 << 2) + i32_load(var0 + 64)), 0)
    i32_store((i32_load(var0 + 48) + var1), 0)
    if (1 if var4 > 488 else 0):
        break
    if (1 if var3 == 0 else 0):
        break
    if (1 if i32_load(var0) != 12 else 0):
        break
    i32_store(var0 + 36, i32_load(var0 + 16))


# ==========================================================
# $func388
# ==========================================================
def func388(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var4 = (i32_load(9671128) + (var1 * 132))
    var2 = i32_load(((var0 + (i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122) << 2)) + 285656))
    if (1 if i32_load(((var0 + (i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122) << 2)) + 285656)) == 0 else 0):
        var2 = func26(16)
        i32_store(func26(16) + 4, 55)
        i32_store(var2, func26(220))
        i64_store(var2 + 8, 665719930880)
        i32_store(((var0 + (i32_load8_u(var4 + 122) << 2)) + 285656), var2)
        var5 = (var2 + 8)
        var0 = i32_load(var2)
        break
    var5 = (var2 + 8)
    var0 = i32_load(var2 + 8)
    var3 = i32_load(var2 + 4)
    if (1 if i32_load(var2 + 8) != i32_load(var2 + 4) else 0):
        var3 = var0
        var0 = i32_load(var2)
        break
    var0 = (i32_load(var2 + 12) + var3)
    i32_store(var2 + 4, (i32_load(var2 + 12) + var3))
    var4 = i32_load(var2)
    var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var3:
        # Unknown: memory.copy []
    if var4:
        var3 = i32_load(var2 + 8)
    i32_store(var2, var0)
    i32_store(var5, (var3 + 1))
    i32_store((var0 + (var3 << 2)), var1)


# ==========================================================
# $func391
# ==========================================================
def func391(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    if (1 if i32_load(var0 + 44) != ((i32_load(var0 + 48) + 1) % i32_load(var0 + 40)) else 0):
        break
    var2 = i32_load(var0 + 40)
    var3 = e()
    if e():
        var5 = (var2 << 1)
        var4 = i32_load(var0 + 48)
        var2 = i32_load(var0 + 44)
        if (1 if i32_load(var0 + 48) >= i32_load(var0 + 44) else 0):
            var2 = (var4 - var2)
            break
        var2 = (i32_load(var0 + 40) - var2)
        var6 = ((i32_load(var0 + 40) - var2) * 12)
        var2 = (var2 + var4)
        i32_store(var0 + 48, var2)
        i32_store(var0 + 44, 0)
        i32_store(var0 + 40, var5)
        i32_store(var0 + 36, var3)
    else:
    if 0:
        break
    return 0
    var3 = (i32_load(var0 + 36) + (i32_load(var0 + 48) * 12))
    i64_store((i32_load(var0 + 36) + (i32_load(var0 + 48) * 12)), i64_load(var1))
    i32_store(var3 + 8, i32_load(var1 + 8))
    i32_store(var0 + 48, ((i32_load(var0 + 48) + 1) % i32_load(var0 + 40)))
    return 1

