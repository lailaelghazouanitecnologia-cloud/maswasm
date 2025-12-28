"""
Auto-generated from WAT. Contains 4 functions.
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
# $func1058
# ==========================================================
def func1058(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
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
        var5 = (var1 - 1)
        if (var1 - 1):
            var7 = (var4 + 1)
            var8 = (var0 + 1)
            var10 = (var5 & 1)
            var12 = (var1 - 2)
            if (1 if (var1 - 2) == 0 else 0):
                var1 = 0
                break
            var11 = (var5 & -2)
            var1 = 0
            while True:  # loop $label6
                i32_store8((var1 + var7), (i32_load8_u((var1 + var8)) - i32_load8_u((var0 + var1))))
                var9 = (var1 | 1)
                i32_store8((var7 + (var1 | 1)), (i32_load8_u((var8 + var9)) - i32_load8_u((var0 + var9))))
                var1 = (var1 + 2)
                var6 = (var6 + 2)
                if (1 if (var6 + 2) != var11 else 0):
                    continue
                break  # end loop
            if var10:
                i32_store8((var1 + var7), (i32_load8_u((var1 + var8)) - i32_load8_u((var0 + var1))))
            if (1 if var2 < 2 else 0):
                break
            var10 = (var5 & -2)
            var11 = (var5 & 1)
            var8 = 1
            while True:  # loop $label9
                var4 = (var3 + var4)
                var1 = (var0 + var3)
                i32_store8((var3 + var4), (i32_load8_u((var0 + var3)) - i32_load8_u(var0)))
                var5 = (var4 + 1)
                var7 = (var1 + 1)
                var0 = 0
                var6 = 0
                if var12:
                    while True:  # loop $label8
                        i32_store8((var0 + var5), (i32_load8_u((var0 + var7)) - i32_load8_u((var0 + var1))))
                        var9 = (var0 | 1)
                        i32_store8((var5 + (var0 | 1)), (i32_load8_u((var7 + var9)) - i32_load8_u((var1 + var9))))
                        var0 = (var0 + 2)
                        var6 = (var6 + 2)
                        if (1 if (var6 + 2) != var10 else 0):
                            continue
                        break  # end loop
                if var11:
                    i32_store8((var0 + var5), (i32_load8_u((var0 + var7)) - i32_load8_u((var0 + var1))))
                var0 = var1
                var8 = (var8 + 1)
                if (1 if (var8 + 1) != var2 else 0):
                    continue
                break  # end loop
            break
        if (1 if var2 < 2 else 0):
            break
        var1 = (var2 - 1)
        var6 = ((var2 - 1) & 3)
        if (1 if (var2 - 2) >= 3 else 0):
            var5 = (var1 & -4)
            var1 = 0
            while True:  # loop $label10
                var4 = (var3 + var4)
                var2 = (var0 + var3)
                i32_store8((var3 + var4), (i32_load8_u((var0 + var3)) - i32_load8_u(var0)))
                var4 = (var3 + var4)
                var0 = (var2 + var3)
                i32_store8((var3 + var4), (i32_load8_u((var2 + var3)) - i32_load8_u(var2)))
                var4 = (var3 + var4)
                var2 = (var0 + var3)
                i32_store8((var3 + var4), (i32_load8_u((var0 + var3)) - i32_load8_u(var0)))
                var4 = (var3 + var4)
                var0 = (var2 + var3)
                i32_store8((var3 + var4), (i32_load8_u((var2 + var3)) - i32_load8_u(var2)))
                var1 = (var1 + 4)
                if (1 if (var1 + 4) != var5 else 0):
                    continue
                break  # end loop
        if (1 if var6 == 0 else 0):
            break
        var1 = 0
        while True:  # loop $label11
            var4 = (var3 + var4)
            var2 = (var0 + var3)
            i32_store8((var3 + var4), (i32_load8_u((var0 + var3)) - i32_load8_u(var0)))
            var0 = var2
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var6 else 0):
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


# ==========================================================
# $func1071
# ==========================================================
def func1071(var0, var1, var2, var3, var4):
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
        var9 = (var1 - 1)
        if (var1 - 1):
            var6 = (var4 + 1)
            var8 = (var0 + 1)
            if (1 if var1 != 2 else 0):
                var11 = (var9 & -2)
                while True:  # loop $label5
                    i32_store8((var5 + var6), (i32_load8_u((var5 + var8)) - i32_load8_u((var0 + var5))))
                    var10 = (var5 | 1)
                    i32_store8((var6 + (var5 | 1)), (i32_load8_u((var8 + var10)) - i32_load8_u((var0 + var10))))
                    var5 = (var5 + 2)
                    var7 = (var7 + 2)
                    if (1 if (var7 + 2) != var11 else 0):
                        continue
                    break  # end loop
            if (var9 & 1):
                i32_store8((var5 + var6), (i32_load8_u((var5 + var8)) - i32_load8_u((var0 + var5))))
            var9 = 1
            if (1 if var2 <= 1 else 0):
                break
            var8 = (0 - var3)
            var7 = (var3 + var4)
            var6 = (var0 + var3)
            if (1 if var1 <= 1 else 0):
                break
            while True:  # loop $label9
                var0 = i32_load8_u(var6)
                i32_store8(var7, (i32_load8_u(var6) - i32_load8_u((var6 + var8))))
                var5 = 1
                while True:  # loop $label8
                    var4 = (var0 & 255)
                    var0 = i32_load8_u((var5 + var6))
                    var10 = (var6 + (var5 - var3))
                    var4 = ((var4 + i32_load8_u((var6 + (var5 - var3)))) - i32_load8_u((var10 - 1)))
                    var4 = (((var4 + i32_load8_u((var6 + (var5 - var3)))) - i32_load8_u((var10 - 1))) if (1 if var4 > 0 else 0) else 0)
                    i32_store8((var5 + var7), (i32_load8_u((var5 + var6)) - (255 if (1 if var4 >= 255 else 0) else (((var4 + i32_load8_u((var6 + (var5 - var3)))) - i32_load8_u((var10 - 1))) if (1 if var4 > 0 else 0) else 0))))
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var1 else 0):
                        continue
                    break  # end loop
                var7 = (var3 + var7)
                var6 = (var3 + var6)
                var9 = (var9 + 1)
                if (1 if (var9 + 1) != var2 else 0):
                    continue
                break  # end loop
            break
        if (1 if var2 < 2 else 0):
            break
        var8 = (0 - var3)
        var7 = (var3 + var4)
        var6 = (var0 + var3)
        var0 = (var2 - 1)
        var4 = ((var2 - 1) & 1)
        if (1 if var2 != 2 else 0):
            var2 = (var0 & -2)
            var0 = 0
            while True:  # loop $label10
                i32_store8(var7, (i32_load8_u(var6) - i32_load8_u((var6 + var8))))
                var5 = (var3 + var7)
                var1 = (var3 + var6)
                i32_store8((var3 + var7), (i32_load8_u((var3 + var6)) - i32_load8_u((var1 + var8))))
                var7 = (var3 + var5)
                var6 = (var1 + var3)
                var0 = (var0 + 2)
                if (1 if (var0 + 2) != var2 else 0):
                    continue
                break  # end loop
        if (1 if var4 == 0 else 0):
            break
        i32_store8(var7, (i32_load8_u(var6) - i32_load8_u((var6 + var8))))
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
    return 7251


# ==========================================================
# $func1087
# ==========================================================
def func1087(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if (1 if var2 == i32_load(var0 + 16) else 0):
        var6 = i32_load(var1)
        var7 = i32_load(i32_load(var1) + 28)
        var4 = i32_load(var6 + 44)
        var3 = (i32_load(i32_load(var1) + 28) + (i32_load(var6 + 44) * i32_load(var0 + 8)))
        var1 = i32_load(var0 + 12)
        var5 = i32_load(var0 + 104)
        if i32_load(var0 + 104):
            if (1 if var2 <= 0 else 0):
                break
            if (1 if var2 != 1 else 0):
                var7 = (var2 & -2)
                var4 = 0
                while True:  # loop $label1
                    # Unknown: memory.copy []
                    var3 = (var3 + i32_load(var6 + 44))
                    var5 = (var5 + i32_load(var0))
                    # Unknown: memory.copy []
                    var3 = (var3 + i32_load(var6 + 44))
                    var5 = (var5 + i32_load(var0))
                    var4 = (var4 + 2)
                    if (1 if (var4 + 2) != var7 else 0):
                        continue
                    break  # end loop
            if (1 if (var2 & 1) == 0 else 0):
                break
            # Unknown: memory.copy []
            return 0
        if (1 if var7 == 0 else 0):
            break
        if (1 if var2 <= 0 else 0):
            break
        if (1 if var2 >= 8 else 0):
            var0 = (var2 & -8)
            var5 = 0
            while True:  # loop $label2
                # Unknown: memory.fill []
                var3 = (var3 + var4)
                # Unknown: memory.fill []
                var3 = (var3 + var4)
                # Unknown: memory.fill []
                var3 = (var3 + var4)
                # Unknown: memory.fill []
                var3 = (var3 + var4)
                # Unknown: memory.fill []
                var3 = (var3 + var4)
                # Unknown: memory.fill []
                var3 = (var3 + var4)
                # Unknown: memory.fill []
                var3 = (var3 + var4)
                # Unknown: memory.fill []
                var3 = (var3 + var4)
                var5 = (var5 + 8)
                if (1 if (var5 + 8) != var0 else 0):
                    continue
                break  # end loop
        var0 = (var2 & 7)
        if (1 if (var2 & 7) == 0 else 0):
            break
        var5 = 0
        while True:  # loop $label3
            # Unknown: memory.fill []
            var3 = (var3 + var4)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var0 else 0):
                continue
            break  # end loop
        return 0
    a_c()
    raise RuntimeError('unreachable')
    return 5746


# ==========================================================
# $func1088
# ==========================================================
def func1088(var0, var1, var2):
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
    var6 = i32_load(var0 + 104)
    if (1 if i32_load(var0 + 104) == 0 else 0):
        break
    var4 = i32_load(var0 + 16)
    var3 = i32_load(var0 + 8)
    var9 = i32_load(var1)
    if (1 if i32_load(var0 + 56) == 0 else 0):
        var1 = var3
        break
    if (1 if var3 == 0 else 0):
        var5 = (var4 - 1)
        break
    var6 = (var6 - i32_load(var0))
    var5 = var4
    var1 = (var3 - 1)
    var7 = i32_load(var0 + 84)
    var4 = (i32_load(var0 + 84) + (var3 + var4))
    if (1 if (i32_load(var0 + 84) + (var3 + var4)) != i32_load(var0 + 88) else 0):
        var4 = var5
        break
    var4 = (var4 - (var1 + var7))
    var7 = i32_load(var0 + 12)
    var13 = i32_load(var9)
    var3 = i32_load(var9 + 20)
    var11 = (i32_load(var9 + 16) + (i32_load(var9 + 20) * var1))
    var5 = 15
    if (1 if var4 <= 0 else 0):
        break
    if (1 if var7 <= 0 else 0):
        break
    var14 = (var7 & -2)
    var15 = (var7 & 1)
    var1 = (var11 + 1)
    while True:  # loop $label5
        var3 = 0
        var10 = 0
        if (1 if var7 != 1 else 0):
            while True:  # loop $label4
                var8 = (var1 + (var3 << 1))
                var16 = ((i32_load8_u((var3 + var6)) & 0xFFFFFFFF) >> 4)
                i32_store8((var1 + (var3 << 1)), (((i32_load8_u((var3 + var6)) & 0xFFFFFFFF) >> 4) | (i32_load8_u(var8) & 240)))
                var8 = (var3 | 1)
                var17 = (var1 + ((var3 | 1) << 1))
                var8 = ((i32_load8_u((var6 + var8)) & 0xFFFFFFFF) >> 4)
                i32_store8((var1 + ((var3 | 1) << 1)), (((i32_load8_u((var6 + var8)) & 0xFFFFFFFF) >> 4) | (i32_load8_u(var17) & 240)))
                var5 = ((var5 & var16) & var8)
                var3 = (var3 + 2)
                var10 = (var10 + 2)
                if (1 if (var10 + 2) != var14 else 0):
                    continue
                break  # end loop
        if var15:
            var10 = (var1 + (var3 << 1))
            var3 = ((i32_load8_u((var3 + var6)) & 0xFFFFFFFF) >> 4)
            i32_store8((var1 + (var3 << 1)), (((i32_load8_u((var3 + var6)) & 0xFFFFFFFF) >> 4) | (i32_load8_u(var10) & 240)))
            var5 = (var3 & var5)
        var3 = i32_load(var9 + 20)
        var1 = (var1 + i32_load(var9 + 20))
        var6 = (var6 + i32_load(var0))
        var12 = (var12 + 1)
        if (1 if (var12 + 1) != var4 else 0):
            continue
        break  # end loop
    if (1 if var2 != var4 else 0):
        break
    if (1 if var5 == 15 else 0):
        break
    if (1 if (var13 - 11) < -4 else 0):
        break
    # call_indirect via table[i32_load(9687296)]
    return 0
    a_c()
    raise RuntimeError('unreachable')
    return 7747

