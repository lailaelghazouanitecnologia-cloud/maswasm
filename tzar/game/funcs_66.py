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
# $func970
# ==========================================================
def func970(var0, var1):
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
    if (1 if i32_load(var0 + 60) < i32_load(var0 + 48) else 0):
        if (1 if i32_load(var0) == 0 else 0):
            var4 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) <= 0 else 0):
                break
            var11 = (i32_load(var0 + 52) * var4)
            break
        a_c()
        raise RuntimeError('unreachable')
        while True:  # loop $label7
            if (1 if var7 < var11 else 0):
                var12 = i32_load(var0 + 36)
                var2 = 0
                var5 = 0
                var8 = var7
                var6 = var7
                while True:  # loop $label5
                    var2 = (var2 + var12)
                    if (1 if (var2 + var12) <= 0 else 0):
                        var9 = i32_load(var0 + 40)
                        var10 = 0
                        break
                    var13 = (i32_load(var0 + 44) * var4)
                    if (1 if var6 >= (i32_load(var0 + 44) * var4) else 0):
                        break
                    var3 = (var4 + var6)
                    var10 = i32_load8_u((var1 + var6))
                    var5 = (var5 + i32_load8_u((var1 + var6)))
                    var9 = i32_load(var0 + 40)
                    var2 = (var2 - i32_load(var0 + 40))
                    if (1 if (var2 - i32_load(var0 + 40)) <= 0 else 0):
                        var6 = var3
                        break
                    while True:  # loop $label4
                        if (1 if var3 >= var13 else 0):
                            break
                        var10 = i32_load8_u((var1 + var3))
                        var5 = (var5 + i32_load8_u((var1 + var3)))
                        var6 = (var3 + var4)
                        var3 = (var3 + var4)
                        var2 = (var2 - var9)
                        if (1 if (var2 - var9) > 0 else 0):
                            continue
                        break  # end loop
                    var3 = (var2 * var10)
                    i32_store((i32_load(var0 + 80) + (var8 << 2)), ((var2 * var10) + (var5 * var9)))
                    var5 = i32(((((i64_load32_u(var0 + 12) * i64_extend_u((0 - var3))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))
                    var8 = (var4 + var8)
                    if (1 if (var4 + var8) < var11 else 0):
                        continue
                    break  # end loop
                if var2:
                    break
            var7 = (var7 + 1)
            if (1 if var4 != (var7 + 1) else 0):
                continue
            break
            break  # end loop
        a_c()
        raise RuntimeError('unreachable')
        return
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func971
# ==========================================================
def func971(var0, var1):
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
    if (1 if i32_load(var0 + 60) < i32_load(var0 + 48) else 0):
        if (1 if i32_load(var0) == 0 else 0):
            break
        var4 = i32_load(var0 + 8)
        if (1 if i32_load(var0 + 8) <= 0 else 0):
            break
        var10 = (i32_load(var0 + 52) * var4)
        var2 = i32_load(var0 + 44)
        var13 = (i32_load(var0 + 44) * var4)
        var11 = i32_load(var0 + 80)
        var7 = i32_load(var0 + 36)
        if (1 if var2 > 1 else 0):
            while True:  # loop $label6
                var5 = (var3 + var4)
                var6 = i32_load8_u((var1 + (var3 + var4)))
                var9 = i32_load8_u((var1 + var3))
                i32_store((var11 + (var3 << 2)), (var7 * i32_load8_u((var1 + var3))))
                if (1 if var5 >= var10 else 0):
                    var12 = i32_load(var0 + 40)
                    var2 = var7
                    break
                var12 = i32_load(var0 + 40)
                var2 = var7
                var8 = var5
                while True:  # loop $label4
                    var2 = (var2 - var12)
                    if (1 if (var2 - var12) < 0 else 0):
                        var8 = (var4 + var8)
                        if (1 if (var4 + var8) >= var13 else 0):
                            break
                        var9 = var6
                        var6 = i32_load8_u((var1 + var8))
                        var2 = (var2 + var7)
                    i32_store((var11 + (var5 << 2)), (((var9 - var6) * var2) + (var6 * var7)))
                    var5 = (var4 + var5)
                    if (1 if (var4 + var5) < var10 else 0):
                        continue
                    break  # end loop
                if (var12 if var2 else 0):
                    break
                var3 = (var3 + 1)
                if (1 if (var3 + 1) != var4 else 0):
                    continue
                break  # end loop
            break
        var0 = i32_load(var0 + 40)
        break
    a_c()
    raise RuntimeError('unreachable')
    while True:  # loop $label9
        var6 = i32_load8_u((var1 + var3))
        i32_store((var11 + (var3 << 2)), (var7 * i32_load8_u((var1 + var3))))
        var9 = var6
        var2 = var7
        var5 = (var3 + var4)
        var8 = (var3 + var4)
        if (1 if var5 < var10 else 0):
            while True:  # loop $label8
                var2 = (var2 - var0)
                if (1 if (var2 - var0) < 0 else 0):
                    var8 = (var4 + var8)
                    if (1 if (var4 + var8) >= var13 else 0):
                        break
                    var9 = var6
                    var6 = i32_load8_u((var1 + var8))
                    var2 = (var2 + var7)
                i32_store((var11 + (var5 << 2)), (((var9 - var6) * var2) + (var6 * var7)))
                var5 = (var4 + var5)
                if (1 if (var4 + var5) < var10 else 0):
                    continue
                break  # end loop
        if (var0 if var2 else 0):
            break
        var3 = (var3 + 1)
        if (1 if var4 != (var3 + 1) else 0):
            continue
        break  # end loop
    break
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func972
# ==========================================================
def func972(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    if (1 if i32_load((var0 - -64)) < i32_load(var0 + 56) else 0):
        var1 = i32_load(var0 + 24)
        if (1 if i32_load(var0 + 24) > 0 else 0):
            break
        if i32_load(var0 + 4):
            break
        var3 = (i32_load(var0 + 8) * i32_load(var0 + 52))
        var6 = i32_load(var0 + 76)
        var7 = i32_load(var0 + 68)
        var1 = (var1 * i32_load(var0 + 16))
        if (var1 * i32_load(var0 + 16)):
            if (1 if var3 <= 0 else 0):
                break
            var8 = i32_load(var0 + 80)
            var9 = i64_extend_u((0 - var1))
            var1 = 0
            while True:  # loop $label3
                var4 = (var1 << 2)
                var2 = (var6 + (var1 << 2))
                var4 = i32((((i64_load32_u((var4 + var8)) * var9) & 0xFFFFFFFFFFFFFFFF) >> 32))
                var5 = i32(((((i64_load32_u(var0 + 20) * i64_extend_u((i32_load((var6 + (var1 << 2))) - i32((((i64_load32_u((var4 + var8)) * var9) & 0xFFFFFFFFFFFFFFFF) >> 32))))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))
                i32_store8((var1 + var7), (-1 if (1 if var5 > 255 else 0) else i32(((((i64_load32_u(var0 + 20) * i64_extend_u((i32_load((var6 + (var1 << 2))) - i32((((i64_load32_u((var4 + var8)) * var9) & 0xFFFFFFFFFFFFFFFF) >> 32))))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))))
                i32_store(var2, var4)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var3 else 0):
                    continue
                break  # end loop
            break
        if (1 if var3 <= 0 else 0):
            break
        var1 = 0
        if (1 if var3 != 1 else 0):
            var4 = (var3 & -2)
            while True:  # loop $label4
                var2 = (var6 + (var1 << 2))
                var5 = i32(((((i64_load32_u(var0 + 20) * i64_load32_u((var6 + (var1 << 2)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))
                i32_store8((var1 + var7), (-1 if (1 if var5 > 255 else 0) else i32(((((i64_load32_u(var0 + 20) * i64_load32_u((var6 + (var1 << 2)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))))
                i32_store(var2, 0)
                var2 = (var1 | 1)
                var2 = (var6 + (var2 << 2))
                var5 = i32(((((i64_load32_u(var0 + 20) * i64_load32_u((var6 + (var2 << 2)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))
                i32_store8((var7 + (var1 | 1)), (-1 if (1 if var5 > 255 else 0) else i32(((((i64_load32_u(var0 + 20) * i64_load32_u((var6 + (var2 << 2)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))))
                i32_store(var2, 0)
                var1 = (var1 + 2)
                var8 = (var8 + 2)
                if (1 if (var8 + 2) != var4 else 0):
                    continue
                break  # end loop
        if (1 if (var3 & 1) == 0 else 0):
            break
        var0 = (var6 + (var1 << 2))
        var1 = i32(((((i64_load32_u(var0 + 20) * i64_load32_u((var6 + (var1 << 2)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))
        i32_store8((var1 + var7), (-1 if (1 if var1 > 255 else 0) else i32(((((i64_load32_u(var0 + 20) * i64_load32_u((var6 + (var1 << 2)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))))
        i32_store(var0, 0)
        return
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func973
# ==========================================================
def func973(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    if (1 if i32_load((var0 - -64)) < i32_load(var0 + 56) else 0):
        var2 = i32_load(var0 + 24)
        if (1 if i32_load(var0 + 24) > 0 else 0):
            break
        if (1 if i32_load(var0 + 4) == 0 else 0):
            break
        var3 = i32_load(var0 + 32)
        if (1 if i32_load(var0 + 32) == 0 else 0):
            break
        var4 = (i32_load(var0 + 8) * i32_load(var0 + 52))
        var6 = i32_load(var0 + 80)
        var7 = i32_load(var0 + 68)
        if (1 if var2 == 0 else 0):
            if (1 if var4 <= 0 else 0):
                break
            if (1 if var4 != 1 else 0):
                var3 = (var4 & -2)
                var2 = 0
                while True:  # loop $label4
                    var5 = i32(((((i64_load32_u(var0 + 16) * i64_load32_u((var6 + (var1 << 2)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))
                    i32_store8((var1 + var7), (-1 if (1 if var5 > 255 else 0) else i32(((((i64_load32_u(var0 + 16) * i64_load32_u((var6 + (var1 << 2)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))))
                    var5 = (var1 | 1)
                    var5 = i32(((((i64_load32_u(var0 + 16) * i64_load32_u((var6 + (var5 << 2)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))
                    i32_store8((var7 + (var1 | 1)), (-1 if (1 if var5 > 255 else 0) else i32(((((i64_load32_u(var0 + 16) * i64_load32_u((var6 + (var5 << 2)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))))
                    var1 = (var1 + 2)
                    var2 = (var2 + 2)
                    if (1 if (var2 + 2) != var3 else 0):
                        continue
                    break  # end loop
            if (1 if (var4 & 1) == 0 else 0):
                break
            var0 = i32(((((i64_load32_u(var0 + 16) * i64_load32_u((var6 + (var1 << 2)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))
            i32_store8((var1 + var7), (-1 if (1 if var0 > 255 else 0) else i32(((((i64_load32_u(var0 + 16) * i64_load32_u((var6 + (var1 << 2)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))))
            return
        var8 = (((i64_extend_u((0 - var2)) << 32) & 0xFFFFFFFFFFFFFFFF) // i64_extend_s(var3))
        if (1 if var4 <= 0 else 0):
            break
        var2 = i32_load(var0 + 76)
        var9 = (var8 & 4294967295)
        var8 = ((0 - var8) & 4294967295)
        while True:  # loop $label5
            var3 = (var1 << 2)
            var3 = i32(((((i64_load32_u(var0 + 16) * (((((var8 * i64_load32_u((var6 + (var1 << 2)))) + (var9 * i64_load32_u((var2 + var3)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32)) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))
            i32_store8((var1 + var7), (-1 if (1 if var3 > 255 else 0) else i32(((((i64_load32_u(var0 + 16) * (((((var8 * i64_load32_u((var6 + (var1 << 2)))) + (var9 * i64_load32_u((var2 + var3)))) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32)) + 2147483648) & 0xFFFFFFFFFFFFFFFF) >> 32))))
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var4 else 0):
                continue
            break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func979
# ==========================================================
def func979(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    if var0:
        if (1 if var4 == 0 else 0):
            break
        if (1 if var0 == var4 else 0):
            break
        if (1 if var1 <= 0 else 0):
            break
        if (1 if var2 <= 0 else 0):
            break
        if (1 if var1 > var3 else 0):
            break
        i32_store8(var4, i32_load8_u(var0))
        var10 = (var1 - 1)
        if (1 if (var1 - 1) == 0 else 0):
            break
        var6 = (var4 + 1)
        var7 = (var0 + 1)
        if (1 if var1 != 2 else 0):
            var11 = (var10 & -2)
            while True:  # loop $label6
                i32_store8((var5 + var6), (i32_load8_u((var5 + var7)) - i32_load8_u((var0 + var5))))
                var9 = (var5 | 1)
                i32_store8((var6 + (var5 | 1)), (i32_load8_u((var7 + var9)) - i32_load8_u((var0 + var9))))
                var5 = (var5 + 2)
                var8 = (var8 + 2)
                if (1 if (var8 + 2) != var11 else 0):
                    continue
                break  # end loop
        if (1 if (var10 & 1) == 0 else 0):
            break
        i32_store8((var5 + var6), (i32_load8_u((var5 + var7)) - i32_load8_u((var0 + var5))))
        if (1 if var2 >= 2 else 0):
            var9 = (var1 & -2)
            var11 = (var1 & 1)
            var6 = 1
            while True:  # loop $label8
                var1 = (var0 + var3)
                var4 = (var3 + var4)
                var5 = 0
                var7 = 0
                if var10:
                    while True:  # loop $label7
                        i32_store8((var4 + var5), (i32_load8_u((var1 + var5)) - i32_load8_u((var0 + var5))))
                        var8 = (var5 | 1)
                        i32_store8((var4 + (var5 | 1)), (i32_load8_u((var1 + var8)) - i32_load8_u((var0 + var8))))
                        var5 = (var5 + 2)
                        var7 = (var7 + 2)
                        if (1 if (var7 + 2) != var9 else 0):
                            continue
                        break  # end loop
                if var11:
                    i32_store8((var4 + var5), (i32_load8_u((var1 + var5)) - i32_load8_u((var0 + var5))))
                var0 = var1
                var6 = (var6 + 1)
                if (1 if (var6 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')

