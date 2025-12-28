"""
Auto-generated from WAT. Contains 5 functions.
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
# $func228
# ==========================================================
def func228(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var9 = (i64_extend_u(var1) * 132)
    var5 = i32((i64_extend_u(var1) * 132))
    var3 = (i32((i64_extend_u(var1) * 132)) + 4)
    var3 = func26((-1 if i32(((var9 & 0xFFFFFFFFFFFFFFFF) >> 32)) else (-1 if (1 if var3 < var5 else 0) else (i32((i64_extend_u(var1) * 132)) + 4))))
    i32_store(func26((-1 if i32(((var9 & 0xFFFFFFFFFFFFFFFF) >> 32)) else (-1 if (1 if var3 < var5 else 0) else (i32((i64_extend_u(var1) * 132)) + 4)))), var1)
    var5 = (var3 + 4)
    if var1:
        var7 = (var5 + (var1 * 132))
        var1 = var5
        while True:  # loop $label0
            # Unknown: memory.fill []
            var4 = func26(4)
            i32_store(var1 + 4, func26(4))
            i32_store(var1, var4)
            i32_store(var1 + 8, (var4 + 4))
            var1 = (var1 + 132)
            if (1 if (var1 + 132) != var7 else 0):
                continue
            break  # end loop
    if var2:
        if (1 if var0 != var5 else 0):
            var1 = 0
            while True:  # loop $label1
                var3 = (var1 * 132)
                var4 = (var5 + (var1 * 132))
                var3 = (var0 + var3)
                # Unknown: memory.copy []
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var2 else 0):
                    continue
                break  # end loop
            break
        var4 = (var2 & 3)
        var3 = (var3 + 16)
        var7 = 0
        var1 = 0
        if (1 if var2 >= 4 else 0):
            var8 = (var2 & -4)
            var2 = 0
            while True:  # loop $label3
                var6 = (var1 * 132)
                # Unknown: memory.copy []
                var6 = ((var1 | 1) * 132)
                # Unknown: memory.copy []
                var6 = ((var1 | 2) * 132)
                # Unknown: memory.copy []
                var6 = ((var1 | 3) * 132)
                # Unknown: memory.copy []
                var1 = (var1 + 4)
                var2 = (var2 + 4)
                if (1 if (var2 + 4) != var8 else 0):
                    continue
                break  # end loop
        if (1 if var4 == 0 else 0):
            break
        while True:  # loop $label4
            var2 = (var1 * 132)
            # Unknown: memory.copy []
            var1 = (var1 + 1)
            var7 = (var7 + 1)
            if (1 if (var7 + 1) != var4 else 0):
                continue
            break  # end loop
        break
    if (1 if var0 == 0 else 0):
        break
    var4 = (var0 - 4)
    var1 = i32_load((var0 - 4))
    if i32_load((var0 - 4)):
        var1 = (var0 + (var1 * 132))
        while True:  # loop $label6
            var2 = (var1 - 132)
            var3 = i32_load((var1 - 132))
            if i32_load((var1 - 132)):
                i32_store((var1 - 128), var3)
            var1 = var2
            if (1 if var2 != var0 else 0):
                continue
            break  # end loop
    return var5


# ==========================================================
# $func246
# ==========================================================
def func246(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    a_v(i32_load(var0))
    i32_store(var0, 0)
    var1 = i32_load(var0 + 188)
    if i32_load(var0 + 188):
        var3 = i32_load(var1)
        if i32_load(var1):
            while True:  # loop $label0
                var1 = i32_load(var0 + 188)
                var2 = (var2 + 1)
                var3 = i32_load((i32_load(var0 + 188) + ((var2 + 1) << 2)))
                if i32_load((i32_load(var0 + 188) + ((var2 + 1) << 2))):
                    continue
                break  # end loop


# ==========================================================
# $func255
# ==========================================================
def func255(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    i32_store(var0, i32_load(var1))
    i32_store(var0 + 4, i32_load(var1 + 4))
    i32_store(var0 + 8, i32_load(var1 + 8))
    i32_store(var0 + 12, i32_load(var1 + 12))
    i32_store(var0 + 16, i32_load(var1 + 16))
    i32_store(var0 + 20, i32_load(var1 + 20))
    i32_store(var0 + 24, i32_load(var1 + 24))
    i32_store(var0 + 28, i32_load(var1 + 28))
    i32_store(var0 + 40, i32_load(var1 + 40))
    i32_store(var0 + 32, i32_load(var1 + 32))
    i32_store(var0 + 36, i32_load(var1 + 36))
    i32_store(var0, i32_load(var1))
    if i32_load(var1 + 56):
        while True:  # loop $label1
            var6 = i32_load((i32_load(var1 + 48) + (var4 << 2)))
            var2 = i32_load(var0 + 56)
            if (1 if i32_load(var0 + 56) != i32_load(var0 + 52) else 0):
                var3 = i32_load(var0 + 48)
                break
            var3 = (i32_load(var0 + 60) + var2)
            i32_store(var0 + 52, (i32_load(var0 + 60) + var2))
            var5 = i32_load(var0 + 48)
            var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
            if var2:
                # Unknown: memory.copy []
            if var5:
                var2 = i32_load(var0 + 56)
            i32_store(var0 + 48, var3)
            i32_store(var0 + 56, (var2 + 1))
            i32_store((var3 + (var2 << 2)), var6)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < i32_load(var1 + 56) else 0):
                continue
            break  # end loop
    if i32_load(var1 + 72):
        var4 = 0
        while True:  # loop $label3
            var6 = i32_load((i32_load(var1 + 64) + (var4 << 2)))
            var2 = i32_load(var0 + 72)
            if (1 if i32_load(var0 + 72) != i32_load(var0 + 68) else 0):
                var3 = i32_load(var0 + 64)
                break
            var3 = (i32_load(var0 + 76) + var2)
            i32_store(var0 + 68, (i32_load(var0 + 76) + var2))
            var5 = i32_load(var0 + 64)
            var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
            if var2:
                # Unknown: memory.copy []
            if var5:
                var2 = i32_load(var0 + 72)
            i32_store(var0 + 64, var3)
            i32_store(var0 + 72, (var2 + 1))
            i32_store((var3 + (var2 << 2)), var6)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < i32_load(var1 + 72) else 0):
                continue
            break  # end loop
    if i32_load(var1 + 88):
        var4 = 0
        while True:  # loop $label5
            var6 = i32_load((i32_load(var1 + 80) + (var4 << 2)))
            var2 = i32_load(var0 + 88)
            if (1 if i32_load(var0 + 88) != i32_load(var0 + 84) else 0):
                var3 = i32_load(var0 + 80)
                break
            var3 = (i32_load(var0 + 92) + var2)
            i32_store(var0 + 84, (i32_load(var0 + 92) + var2))
            var5 = i32_load(var0 + 80)
            var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
            if var2:
                # Unknown: memory.copy []
            if var5:
                var2 = i32_load(var0 + 88)
            i32_store(var0 + 80, var3)
            i32_store(var0 + 88, (var2 + 1))
            i32_store((var3 + (var2 << 2)), var6)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < i32_load(var1 + 88) else 0):
                continue
            break  # end loop
    if i32_load(var1 + 104):
        var4 = 0
        while True:  # loop $label7
            var6 = i32_load((i32_load(var1 + 96) + (var4 << 2)))
            var2 = i32_load(var0 + 104)
            if (1 if i32_load(var0 + 104) != i32_load(var0 + 100) else 0):
                var3 = i32_load(var0 + 96)
                break
            var3 = (i32_load(var0 + 108) + var2)
            i32_store(var0 + 100, (i32_load(var0 + 108) + var2))
            var5 = i32_load(var0 + 96)
            var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
            if var2:
                # Unknown: memory.copy []
            if var5:
                var2 = i32_load(var0 + 104)
            i32_store(var0 + 96, var3)
            i32_store(var0 + 104, (var2 + 1))
            i32_store((var3 + (var2 << 2)), var6)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < i32_load(var1 + 104) else 0):
                continue
            break  # end loop
    var3 = i32_load(var1 + 192)
    if (1 if i32_load(var1 + 192) == 0 else 0):
        break
    var2 = 0
    if (1 if var3 >= 4 else 0):
        var8 = (var3 & -4)
        while True:  # loop $label9
            var5 = (var0 + 112)
            var4 = (var2 << 1)
            var6 = (var1 + 112)
            i32_store16(((var0 + 112) + (var2 << 1)), i32_load16_u(((var1 + 112) + var4)))
            var7 = (var4 | 2)
            i32_store16((var5 + (var4 | 2)), i32_load16_u((var6 + var7)))
            var7 = (var4 | 4)
            i32_store16((var5 + (var4 | 4)), i32_load16_u((var6 + var7)))
            var4 = (var4 | 6)
            i32_store16((var5 + (var4 | 6)), i32_load16_u((var4 + var6)))
            var2 = (var2 + 4)
            var9 = (var9 + 4)
            if (1 if (var9 + 4) != var8 else 0):
                continue
            break  # end loop
    var4 = (var3 & 3)
    if (1 if (var3 & 3) == 0 else 0):
        break
    while True:  # loop $label10
        var5 = (var2 << 1)
        i32_store16((var0 + (var2 << 1)) + 112, i32_load16_u((var1 + var5) + 112))
        var2 = (var2 + 1)
        var10 = (var10 + 1)
        if (1 if (var10 + 1) != var4 else 0):
            continue
        break  # end loop
    i32_store(var0 + 192, var3)


# ==========================================================
# $func256
# ==========================================================
def func256(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var2 = i32_load(var0 + 24)
    if (1 if i32_load(var0 + 24) == 0 else 0):
        var2 = func26(16)
        i64_store(func26(16), 0)
        i64_store(var2 + 8, 0)
        i32_store(var0 + 24, var2)
    var0 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) == 0 else 0):
        var0 = func26(16)
        i32_store(func26(16) + 4, var1)
        var3 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        i32_store(var0 + 12, 2)
        i32_store(var0, var3)
        i32_store(var2 + 8, var0)
        i32_store(var0 + 8, 0)
        var2 = (var0 + 8)
        var3 = var1
        break
    i32_store(var0 + 8, 0)
    var2 = (var0 + 8)
    var3 = i32_load(var0 + 4)
    if (1 if i32_load(var0 + 4) > var1 else 0):
        break
    var3 = (i32_load(var0 + 12) + (var1 + var3))
    i32_store(var0 + 4, (i32_load(var0 + 12) + (var1 + var3)))
    var4 = i32_load(var0)
    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var4:
    i32_store(var0, var3)
    if (1 if var1 == 0 else 0):
        break
    var4 = (var1 & 1)
    var3 = i32_load(var0)
    var0 = 0
    if (1 if var1 != 1 else 0):
        var7 = (var1 & -2)
        var1 = 0
        while True:  # loop $label3
            var5 = (var0 << 2)
            var6 = i32_load(((var0 << 2) + 9147392))
            var8 = i32_load(var2)
            i32_store(var2, (i32_load(var2) + 1))
            i32_store((var3 + (var8 << 2)), var6)
            var5 = i32_load(((var5 | 4) + 9147392))
            var6 = i32_load(var2)
            i32_store(var2, (i32_load(var2) + 1))
            i32_store((var3 + (var6 << 2)), var5)
            var0 = (var0 + 2)
            var1 = (var1 + 2)
            if (1 if (var1 + 2) != var7 else 0):
                continue
            break  # end loop
    if (1 if var4 == 0 else 0):
        break
    var0 = i32_load(((var0 << 2) + 9147392))
    var1 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 1))
    i32_store((var3 + (var1 << 2)), var0)


# ==========================================================
# $func280
# ==========================================================
def func280(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var1 = i32_load(9568064)
    var2 = ((i32_load(9568068) - i32_load(9568064)) >> 7)
    var3 = (((i32_load(9568068) - i32_load(9568064)) >> 7) + 1)
    if (1 if (((i32_load(9568068) - i32_load(9568064)) >> 7) + 1) < 33554432 else 0):
        var1 = (i32_load(9568072) - var1)
        var4 = ((i32_load(9568072) - var1) >> 6)
        var3 = (33554431 if (1 if var1 >= 2147483520 else 0) else (((i32_load(9568072) - var1) >> 6) if (1 if var3 < var4 else 0) else var3))
        if (33554431 if (1 if var1 >= 2147483520 else 0) else (((i32_load(9568072) - var1) >> 6) if (1 if var3 < var4 else 0) else var3)):
            if (1 if var3 >= 33554432 else 0):
                break
        else:
        var1 = 0
        var4 = (var1 + (var3 << 7))
        var3 = func226((var1 + (var2 << 7)), var0)
        var5 = (func226((var1 + (var2 << 7)), var0) + 128)
        var0 = i32_load(9568068)
        var6 = i32_load(9568064)
        if (1 if i32_load(9568068) == i32_load(9568064) else 0):
            break
        while True:  # loop $label2
            var1 = (var3 - 128)
            i64_store((var3 - 128), 0)
            i32_store(var1 + 8, 0)
            var2 = (var0 - 128)
            i32_store(var1, i32_load((var0 - 128)))
            i32_store(var1 + 4, i32_load(var2 + 4))
            i32_store(var1 + 8, i32_load(var2 + 8))
            i32_store(var2 + 8, 0)
            i64_store(var2, 0)
            i32_store(var1 + 20, 0)
            i64_store(var1 + 12, 0)
            i32_store(var1 + 12, i32_load(var2 + 12))
            i32_store(var1 + 16, i32_load(var2 + 16))
            i32_store(var1 + 20, i32_load(var2 + 20))
            i32_store(var2 + 20, 0)
            i64_store(var2 + 12, 0)
            # Unknown: memory.copy []
            var3 = var1
            var0 = var2
            if (1 if var2 != var6 else 0):
                continue
            break  # end loop
        i32_store(9568072, var4)
        var3 = i32_load(9568068)
        i32_store(9568068, var5)
        var0 = i32_load(9568064)
        i32_store(9568064, var1)
        if (1 if var0 == var3 else 0):
            break
        while True:  # loop $label4
            var1 = (var3 - 128)
            var2 = i32_load((var3 - 128) + 12)
            if i32_load((var3 - 128) + 12):
                i32_store((var3 - 112), var2)
            var2 = i32_load(var1)
            if i32_load(var1):
                i32_store((var3 - 124), var2)
            var3 = var1
            if (1 if var1 != var0 else 0):
                continue
            break  # end loop
        break
    func42()
    raise RuntimeError('unreachable')
    func68()
    raise RuntimeError('unreachable')
    i32_store(9568072, var4)
    i32_store(9568068, var5)
    i32_store(9568064, var3)
    if var0:
    return af(var0)

