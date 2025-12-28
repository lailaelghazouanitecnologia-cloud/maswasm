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
# $func281
# ==========================================================
def func281(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var4 = i32_load(var0 + 4)
    var8 = i32_load(var0)
    var3 = ((i32_load(var0 + 4) - i32_load(var0)) >> 5)
    var5 = (((i32_load(var0 + 4) - i32_load(var0)) >> 5) + 1)
    if (1 if (((i32_load(var0 + 4) - i32_load(var0)) >> 5) + 1) < 134217728 else 0):
        var6 = (i32_load(var0 + 8) - var8)
        var7 = ((i32_load(var0 + 8) - var8) >> 4)
        var5 = (134217727 if (1 if var6 >= 2147483616 else 0) else (((i32_load(var0 + 8) - var8) >> 4) if (1 if var5 < var7 else 0) else var5))
        if (134217727 if (1 if var6 >= 2147483616 else 0) else (((i32_load(var0 + 8) - var8) >> 4) if (1 if var5 < var7 else 0) else var5)):
            if (1 if var5 >= 134217728 else 0):
                break
        else:
        var6 = 0
        var7 = i32_load(var1)
        var1 = i32_load(var2)
        var3 = (var6 + (var3 << 5))
        i64_store((var6 + (var3 << 5)) + 8, 0)
        i32_store(var3 + 4, var1)
        i32_store(var3, var7)
        i64_store(var3 + 16, 0)
        i64_store(var3 + 24, 0)
        var2 = func26(16)
        i32_store(func26(16) + 12, var1)
        i32_store(var2 + 8, var7)
        i64_store(var2, 0)
        var1 = (var2 + 16)
        i32_store(var3 + 28, (var2 + 16))
        i32_store(var3 + 24, var1)
        i32_store(var3 + 20, var2)
        var2 = (var6 + (var5 << 5))
        var1 = (var3 + 32)
        if (1 if var4 == var8 else 0):
            break
        while True:  # loop $label2
            var3 = (var3 - 32)
            var4 = (var4 - 32)
            i64_store((var3 - 32), i64_load((var4 - 32)))
            i32_store(var3 + 8, i32_load(var4 + 8))
            i32_store(var3 + 12, i32_load(var4 + 12))
            i32_store(var3 + 16, i32_load(var4 + 16))
            i32_store(var4 + 16, 0)
            i64_store(var4 + 8, 0)
            i32_store(var3 + 20, i32_load(var4 + 20))
            i32_store(var3 + 24, i32_load(var4 + 24))
            i32_store(var3 + 28, i32_load(var4 + 28))
            i32_store(var4 + 28, 0)
            i64_store(var4 + 20, 0)
            if (1 if var4 != var8 else 0):
                continue
            break  # end loop
        i32_store(var0 + 8, var2)
        var2 = i32_load(var0 + 4)
        i32_store(var0 + 4, var1)
        var4 = i32_load(var0)
        i32_store(var0, var3)
        if (1 if var2 == var4 else 0):
            break
        while True:  # loop $label4
            var0 = (var2 - 32)
            var1 = i32_load((var2 - 32) + 20)
            if i32_load((var2 - 32) + 20):
                i32_store((var2 - 8), var1)
            var1 = i32_load((var2 - 24))
            if i32_load((var2 - 24)):
                i32_store((var2 - 20), var1)
            var2 = var0
            if (1 if var0 != var4 else 0):
                continue
            break  # end loop
        break
    func42()
    raise RuntimeError('unreachable')
    func68()
    raise RuntimeError('unreachable')
    i32_store(var0 + 8, var2)
    i32_store(var0 + 4, var1)
    i32_store(var0, var3)
    if var4:
    return af(var4)


# ==========================================================
# $func284
# ==========================================================
def func284(var0):
    var1 = 0
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
    var2 = i32_load(9568064)
    if (1 if i32_load(9568064) != i32_load(9568068) else 0):
        while True:  # loop $label26
            var11 = 0
            var12 = (var2 + (var15 << 7))
            var2 = i32_load(var12)
            if (1 if i32_load((var2 + (var15 << 7)) + 4) != i32_load(var12) else 0):
                while True:  # loop $label12
                    var4 = (var2 + (var11 * 196))
                    var5 = i32_load((var2 + (var11 * 196)) + 56)
                    if (1 if i32_load((var2 + (var11 * 196)) + 56) == 0 else 0):
                        break
                    var6 = (var5 - 1)
                    var2 = i32_load(var4 + 48)
                    var9 = (i32_load(9142892) + 1)
                    if (1 if (i32_load(9142892) + 1) >= var5 else 0):
                        var10 = (var2 + (var6 << 2))
                        if (1 if var6 == 0 else 0):
                            var3 = 0
                            break
                        var7 = 0
                        var1 = 0
                        var3 = 0
                        if (1 if (var5 - 2) >= 3 else 0):
                            var13 = (var6 & -4)
                            var5 = 0
                            while True:  # loop $label2
                                var8 = (var1 << 2)
                                var3 = (i32_load((var2 + ((var1 << 2) | 12))) + (i32_load((var2 + (var8 | 8))) + (i32_load((var2 + (var8 | 4))) + (i32_load((var2 + var8)) + var3))))
                                var1 = (var1 + 4)
                                var5 = (var5 + 4)
                                if (1 if (var5 + 4) != var13 else 0):
                                    continue
                                break  # end loop
                        var5 = (var6 & 3)
                        if (1 if (var6 & 3) == 0 else 0):
                            break
                        while True:  # loop $label3
                            var3 = (i32_load((var2 + (var1 << 2))) + var3)
                            var1 = (var1 + 1)
                            var7 = (var7 + 1)
                            if (1 if (var7 + 1) != var5 else 0):
                                continue
                            break  # end loop
                        var7 = i32_load(var10)
                        var5 = (1 if var3 > ((var6 & 0xFFFFFFFF) >> 1) else 0)
                        i32_store(var10, (1 if var3 > ((var6 & 0xFFFFFFFF) >> 1) else 0))
                        var1 = i32_load(var4 + 56)
                        if (1 if var9 > i32_load(var4 + 56) else 0):
                            while True:  # loop $label4
                                if (1 if i32_load(var4 + 52) == var1 else 0):
                                    var3 = (i32_load(var4 + 60) + var1)
                                    i32_store(var4 + 52, (i32_load(var4 + 60) + var1))
                                    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
                                    if var1:
                                        # Unknown: memory.copy []
                                    var1 = i32_load(var4 + 56)
                                    i32_store(var4 + 48, var3)
                                    var2 = var3
                                i32_store(var4 + 56, (var1 + 1))
                                i32_store((var2 + (var1 << 2)), var5)
                                var1 = i32_load(var4 + 56)
                                if (1 if i32_load(var4 + 56) < var9 else 0):
                                    continue
                                break  # end loop
                        i32_store((var2 + (i32_load(9142892) << 2)), var7)
                        break
                    i32_store(var4 + 56, var6)
                    var1 = var0
                    if (1 if var6 <= var0 else 0):
                        break
                    while True:  # loop $label5
                        var1 = (var1 + 1)
                        i32_store((var2 + (var1 << 2)), i32_load((var2 + ((var1 + 1) << 2))))
                        if (1 if var1 < i32_load(var4 + 56) else 0):
                            continue
                        break  # end loop
                    var5 = i32_load(var4 + 72)
                    if (1 if i32_load(var4 + 72) == 0 else 0):
                        break
                    var6 = (var5 - 1)
                    var13 = (var4 - -64)
                    var2 = i32_load((var4 - -64))
                    var9 = (i32_load(9142892) + 1)
                    if (1 if (i32_load(9142892) + 1) >= var5 else 0):
                        var10 = (var2 + (var6 << 2))
                        if (1 if var6 == 0 else 0):
                            var3 = 0
                            break
                        var7 = 0
                        var1 = 0
                        var3 = 0
                        if (1 if (var5 - 2) >= 3 else 0):
                            var14 = (var6 & -4)
                            var5 = 0
                            while True:  # loop $label8
                                var8 = (var1 << 2)
                                var3 = (i32_load((var2 + ((var1 << 2) | 12))) + (i32_load((var2 + (var8 | 8))) + (i32_load((var2 + (var8 | 4))) + (i32_load((var2 + var8)) + var3))))
                                var1 = (var1 + 4)
                                var5 = (var5 + 4)
                                if (1 if (var5 + 4) != var14 else 0):
                                    continue
                                break  # end loop
                        var5 = (var6 & 3)
                        if (1 if (var6 & 3) == 0 else 0):
                            break
                        while True:  # loop $label9
                            var3 = (i32_load((var2 + (var1 << 2))) + var3)
                            var1 = (var1 + 1)
                            var7 = (var7 + 1)
                            if (1 if (var7 + 1) != var5 else 0):
                                continue
                            break  # end loop
                        var7 = i32_load(var10)
                        var5 = (1 if var3 > ((var6 & 0xFFFFFFFF) >> 1) else 0)
                        i32_store(var10, (1 if var3 > ((var6 & 0xFFFFFFFF) >> 1) else 0))
                        var1 = i32_load(var4 + 72)
                        if (1 if var9 > i32_load(var4 + 72) else 0):
                            while True:  # loop $label10
                                if (1 if i32_load(var4 + 68) == var1 else 0):
                                    var3 = (i32_load(var4 + 76) + var1)
                                    i32_store(var4 + 68, (i32_load(var4 + 76) + var1))
                                    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
                                    if var1:
                                        # Unknown: memory.copy []
                                    var1 = i32_load(var4 + 72)
                                    i32_store(var13, var3)
                                    var2 = var3
                                i32_store(var4 + 72, (var1 + 1))
                                i32_store((var2 + (var1 << 2)), var5)
                                var1 = i32_load(var4 + 72)
                                if (1 if i32_load(var4 + 72) < var9 else 0):
                                    continue
                                break  # end loop
                        i32_store((var2 + (i32_load(9142892) << 2)), var7)
                        break
                    i32_store(var4 + 72, var6)
                    var1 = var0
                    if (1 if var6 <= var0 else 0):
                        break
                    while True:  # loop $label11
                        var1 = (var1 + 1)
                        i32_store((var2 + (var1 << 2)), i32_load((var2 + ((var1 + 1) << 2))))
                        if (1 if var1 < i32_load(var4 + 72) else 0):
                            continue
                        break  # end loop
                    var11 = (var11 + 1)
                    var2 = i32_load(var12)
                    if (1 if (var11 + 1) < ((i32_load(var12 + 4) - i32_load(var12)) // 196) else 0):
                        continue
                    break  # end loop
            var2 = i32_load(var12 + 12)
            if (1 if i32_load(var12 + 12) != i32_load(var12 + 16) else 0):
                var11 = 0
                while True:  # loop $label25
                    var4 = (var2 + (var11 * 196))
                    var5 = i32_load((var2 + (var11 * 196)) + 56)
                    if (1 if i32_load((var2 + (var11 * 196)) + 56) == 0 else 0):
                        break
                    var6 = (var5 - 1)
                    var2 = i32_load(var4 + 48)
                    var9 = (i32_load(9142892) + 1)
                    if (1 if (i32_load(9142892) + 1) >= var5 else 0):
                        var10 = (var2 + (var6 << 2))
                        if (1 if var6 == 0 else 0):
                            var3 = 0
                            break
                        var7 = 0
                        var1 = 0
                        var3 = 0
                        if (1 if (var5 - 2) >= 3 else 0):
                            var13 = (var6 & -4)
                            var5 = 0
                            while True:  # loop $label15
                                var8 = (var1 << 2)
                                var3 = (i32_load((var2 + ((var1 << 2) | 12))) + (i32_load((var2 + (var8 | 8))) + (i32_load((var2 + (var8 | 4))) + (i32_load((var2 + var8)) + var3))))
                                var1 = (var1 + 4)
                                var5 = (var5 + 4)
                                if (1 if (var5 + 4) != var13 else 0):
                                    continue
                                break  # end loop
                        var5 = (var6 & 3)
                        if (1 if (var6 & 3) == 0 else 0):
                            break
                        while True:  # loop $label16
                            var3 = (i32_load((var2 + (var1 << 2))) + var3)
                            var1 = (var1 + 1)
                            var7 = (var7 + 1)
                            if (1 if (var7 + 1) != var5 else 0):
                                continue
                            break  # end loop
                        var7 = i32_load(var10)
                        var5 = (1 if var3 > ((var6 & 0xFFFFFFFF) >> 1) else 0)
                        i32_store(var10, (1 if var3 > ((var6 & 0xFFFFFFFF) >> 1) else 0))
                        var1 = i32_load(var4 + 56)
                        if (1 if var9 > i32_load(var4 + 56) else 0):
                            while True:  # loop $label17
                                if (1 if i32_load(var4 + 52) == var1 else 0):
                                    var3 = (i32_load(var4 + 60) + var1)
                                    i32_store(var4 + 52, (i32_load(var4 + 60) + var1))
                                    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
                                    if var1:
                                        # Unknown: memory.copy []
                                    var1 = i32_load(var4 + 56)
                                    i32_store(var4 + 48, var3)
                                    var2 = var3
                                i32_store(var4 + 56, (var1 + 1))
                                i32_store((var2 + (var1 << 2)), var5)
                                var1 = i32_load(var4 + 56)
                                if (1 if i32_load(var4 + 56) < var9 else 0):
                                    continue
                                break  # end loop
                        i32_store((var2 + (i32_load(9142892) << 2)), var7)
                        break
                    i32_store(var4 + 56, var6)
                    var1 = var0
                    if (1 if var6 <= var0 else 0):
                        break
                    while True:  # loop $label18
                        var1 = (var1 + 1)
                        i32_store((var2 + (var1 << 2)), i32_load((var2 + ((var1 + 1) << 2))))
                        if (1 if var1 < i32_load(var4 + 56) else 0):
                            continue
                        break  # end loop
                    var5 = i32_load(var4 + 72)
                    if (1 if i32_load(var4 + 72) == 0 else 0):
                        break
                    var6 = (var5 - 1)
                    var13 = (var4 - -64)
                    var2 = i32_load((var4 - -64))
                    var9 = (i32_load(9142892) + 1)
                    if (1 if (i32_load(9142892) + 1) >= var5 else 0):
                        var10 = (var2 + (var6 << 2))
                        if (1 if var6 == 0 else 0):
                            var3 = 0
                            break
                        var7 = 0
                        var1 = 0
                        var3 = 0
                        if (1 if (var5 - 2) >= 3 else 0):
                            var14 = (var6 & -4)
                            var5 = 0
                            while True:  # loop $label21
                                var8 = (var1 << 2)
                                var3 = (i32_load((var2 + ((var1 << 2) | 12))) + (i32_load((var2 + (var8 | 8))) + (i32_load((var2 + (var8 | 4))) + (i32_load((var2 + var8)) + var3))))
                                var1 = (var1 + 4)
                                var5 = (var5 + 4)
                                if (1 if (var5 + 4) != var14 else 0):
                                    continue
                                break  # end loop
                        var5 = (var6 & 3)
                        if (1 if (var6 & 3) == 0 else 0):
                            break
                        while True:  # loop $label22
                            var3 = (i32_load((var2 + (var1 << 2))) + var3)
                            var1 = (var1 + 1)
                            var7 = (var7 + 1)
                            if (1 if (var7 + 1) != var5 else 0):
                                continue
                            break  # end loop
                        var7 = i32_load(var10)
                        var5 = (1 if var3 > ((var6 & 0xFFFFFFFF) >> 1) else 0)
                        i32_store(var10, (1 if var3 > ((var6 & 0xFFFFFFFF) >> 1) else 0))
                        var1 = i32_load(var4 + 72)
                        if (1 if var9 > i32_load(var4 + 72) else 0):
                            while True:  # loop $label23
                                if (1 if i32_load(var4 + 68) == var1 else 0):
                                    var3 = (i32_load(var4 + 76) + var1)
                                    i32_store(var4 + 68, (i32_load(var4 + 76) + var1))
                                    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
                                    if var1:
                                        # Unknown: memory.copy []
                                    var1 = i32_load(var4 + 72)
                                    i32_store(var13, var3)
                                    var2 = var3
                                i32_store(var4 + 72, (var1 + 1))
                                i32_store((var2 + (var1 << 2)), var5)
                                var1 = i32_load(var4 + 72)
                                if (1 if i32_load(var4 + 72) < var9 else 0):
                                    continue
                                break  # end loop
                        i32_store((var2 + (i32_load(9142892) << 2)), var7)
                        break
                    i32_store(var4 + 72, var6)
                    var1 = var0
                    if (1 if var6 <= var0 else 0):
                        break
                    while True:  # loop $label24
                        var1 = (var1 + 1)
                        i32_store((var2 + (var1 << 2)), i32_load((var2 + ((var1 + 1) << 2))))
                        if (1 if var1 < i32_load(var4 + 72) else 0):
                            continue
                        break  # end loop
                    var11 = (var11 + 1)
                    var2 = i32_load(var12 + 12)
                    if (1 if (var11 + 1) < ((i32_load(var12 + 16) - i32_load(var12 + 12)) // 196) else 0):
                        continue
                    break  # end loop
            var15 = (var15 + 1)
            var2 = i32_load(9568064)
            if (1 if (var15 + 1) < ((i32_load(9568068) - i32_load(9568064)) >> 7) else 0):
                continue
            break  # end loop


# ==========================================================
# $func307
# ==========================================================
def func307(var0):
    var1 = 0
    i32_store(var0, 32988)
    var1 = (i32_load(var0 + 4) - 12)
    if (1 if (-1 - 1) < 0 else 0):
    return var0

