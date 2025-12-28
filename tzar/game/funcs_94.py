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
# $func1036
# ==========================================================
def func1036(var0, var1):
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
    var4 = i32_load(var0 + 8)
    if (1 if var1 <= i32_load(i32_load(var0 + 8) + 88) else 0):
        var9 = i32_load(var0 + 108)
        var3 = (var1 - i32_load(var0 + 108))
        if (1 if (var1 - i32_load(var0 + 108)) >= 17 else 0):
            break
        if (1 if var3 <= 0 else 0):
            break
        var2 = i32_load(var0 + 100)
        var7 = (i32_load(var0 + 16) + ((var9 * i32_load(var0 + 100)) << 2))
        var5 = i32_load(var4)
        var8 = i32_load(var0 + 20)
        var6 = i32_load(var0 + 192)
        if (1 if i32_load(var0 + 192) > 0 else 0):
            var2 = (var6 - 1)
            if (1 if var6 == 1 else 0):
                break
            while True:  # loop $label3
                var6 = (var2 - 1)
                var3 = (1 if var2 > 1 else 0)
                var2 = var6
                if var3:
                    continue
                break  # end loop
            break
        if (1 if var7 == var8 else 0):
            break
        # Unknown: memory.copy []
        var12 = i32_load(var0 + 108)
        if (1 if i32_load(var0 + 108) >= var1 else 0):
            break
        var3 = i32_load(var4 + 80)
        var9 = i32_load(var4 + 76)
        if (1 if i32_load(var4 + 80) <= i32_load(var4 + 76) else 0):
            break
        var2 = i32_load(var4 + 88)
        var6 = (i32_load(var4 + 88) if (1 if var1 > var2 else 0) else var1)
        var14 = i32_load(var4 + 84)
        var2 = (1 if var12 < var14 else 0)
        var7 = (i32_load(var4 + 84) if (1 if var12 < var14 else 0) else var12)
        if (1 if (i32_load(var4 + 88) if (1 if var1 > var2 else 0) else var1) <= (i32_load(var4 + 84) if (1 if var12 < var14 else 0) else var12) else 0):
            break
        var6 = (var6 - var7)
        i32_store(var4 + 16, (var6 - var7))
        var11 = (var3 - var9)
        i32_store(var4 + 12, (var3 - var9))
        i32_store(var4 + 8, (var7 - var14))
        var15 = (var5 << 2)
        var10 = ((var8 + (((var5 << 2) * (var14 - var12)) if var2 else 0)) + (var9 << 2))
        var17 = i32_load(var0 + 12)
        var12 = i32_load(i32_load(var0 + 12))
        if (1 if i32_load(i32_load(var0 + 12)) <= 10 else 0):
            var8 = i32_load(var17 + 20)
            var13 = (i32_load(var17 + 16) + (i32_load(var17 + 20) * i32_load(var0 + 116)))
            if i32_load(var4 + 92):
                if (1 if var6 <= 0 else 0):
                    var3 = 0
                    break
                var5 = 0
                var3 = 0
                while True:  # loop $label11
                    var7 = i32_load(var0 + 284)
                    var2 = i32_load(i32_load(var0 + 284) + 32)
                    var7 = (((i32_load(i32_load(var0 + 284) + 32) + i32_load(var7 + 24)) - 1) // var2)
                    var9 = (var6 - var5)
                    var2 = (var6 - var5)
                    var7 = ((((i32_load(i32_load(var0 + 284) + 32) + i32_load(var7 + 24)) - 1) // var2) if (1 if var2 > var7 else 0) else (var6 - var5))
                    if (1 if ((((i32_load(i32_load(var0 + 284) + 32) + i32_load(var7 + 24)) - 1) // var2) if (1 if var2 > var7 else 0) else (var6 - var5)) <= 0 else 0):
                        break
                    if (1 if var7 > var9 else 0):
                        break
                    var2 = (var10 + (var5 * var15))
                    func446((var10 + (var5 * var15)), var15, i32_load(i32_load(var0 + 284) + 44), var7)
                    if (1 if func82(i32_load(var0 + 284), var9, var2, var15) != var7 else 0):
                        break
                    var5 = (var5 + var7)
                    var11 = 0
                    var4 = i32_load(var0 + 284)
                    var7 = (i32_load(var0 + 284) - -64)
                    if (1 if i32_load((i32_load(var0 + 284) - -64)) >= i32_load(var4 + 56) else 0):
                        break
                    var2 = (var13 + (var3 * var8))
                    var14 = i32_load(var4 + 52)
                    var9 = i32_load(var4 + 68)
                    while True:  # loop $label10
                        if (1 if i32_load(var4 + 24) > 0 else 0):
                            break
                        func91(((var2 * var3) << 2), var4)
                        # call_indirect via table[i32_load(9687284)]
                        func454(var9, var14, var12, var2)
                        var11 = (var11 + 1)
                        var2 = (var2 + var8)
                        if (1 if i32_load(var7) < i32_load(var4 + 56) else 0):
                            continue
                        break  # end loop
                    var3 = (var3 + var11)
                    if (1 if var5 < var6 else 0):
                        continue
                    break  # end loop
                break
            if (1 if var6 > 0 else 0):
                var2 = var6
                while True:  # loop $label12
                    func454(var10, var11, var12, var13)
                    var13 = (var8 + var13)
                    var10 = (var10 + var15)
                    var3 = (1 if var2 > 1 else 0)
                    var2 = (var2 - 1)
                    if var3:
                        continue
                    break  # end loop
            var3 = var6
            var5 = (i32_load(var0 + 116) + var3)
            break
        var5 = i32_load(var0 + 116)
        if i32_load(var4 + 92):
            if (1 if var6 <= 0 else 0):
                break
            while True:  # loop $label17
                var3 = i32_load(var0 + 284)
                var2 = i32_load(var3 + 32)
                var3 = (((i32_load(var3 + 32) + i32_load(var3 + 24)) - 1) // var2)
                var2 = (var6 - var13)
                var3 = ((((i32_load(var3 + 32) + i32_load(var3 + 24)) - 1) // var2) if (1 if var2 > var3 else 0) else (var6 - var13))
                func446(var10, var15, i32_load(i32_load(var0 + 284) + 44), ((((i32_load(var3 + 32) + i32_load(var3 + 24)) - 1) // var2) if (1 if var2 > var3 else 0) else (var6 - var13)))
                if (1 if func82(i32_load(var0 + 284), var2, var10, var15) != var3 else 0):
                    break
                var13 = (var3 + var13)
                var14 = (var3 * var15)
                var11 = 0
                var4 = i32_load(var0 + 284)
                var9 = (i32_load(var0 + 284) - -64)
                if (1 if i32_load((i32_load(var0 + 284) - -64)) >= i32_load(var4 + 56) else 0):
                    break
                var8 = i32_load(var4 + 52)
                var12 = i32_load(var4 + 68)
                var7 = (i32_load(var4 + 68) + 3)
                var2 = var5
                while True:  # loop $label16
                    if (1 if i32_load(var4 + 24) > 0 else 0):
                        break
                    func91(call_indirect(i32_load(9687284)), var4)
                    # call_indirect via table[i32_load(9687284)]
                    var16 = i32_load(var0 + 12)
                    # call_indirect via table[i32_load(9688016)]
                    var3 = (var2 >> 1)
                    # call_indirect via table[i32_load(9688020)]
                    var3 = i32_load(var16 + 28)
                    if i32_load(var16 + 28):
                        # call_indirect via table[i32_load(9687308)]
                    var11 = (var11 + 1)
                    var2 = (var2 + 1)
                    if (1 if i32_load(var9) < i32_load(var4 + 56) else 0):
                        continue
                    break  # end loop
                var10 = (var10 + var14)
                var5 = (var5 + var11)
                if (1 if var6 > var13 else 0):
                    continue
                break  # end loop
            break
        if (1 if var6 <= 0 else 0):
            break
        while True:  # loop $label18
            var3 = i32_load(var0 + 12)
            # call_indirect via table[i32_load(9688016)]
            var2 = (var5 >> 1)
            # call_indirect via table[i32_load(9688020)]
            var2 = i32_load(var3 + 28)
            if i32_load(var3 + 28):
                # call_indirect via table[i32_load(9687308)]
            var5 = (var5 + 1)
            var10 = (var10 + var15)
            var2 = (1 if var6 > 1 else 0)
            var6 = (var6 - 1)
            if var2:
                continue
            break  # end loop
        i32_store(var0 + 116, var5)
        if (1 if var5 > i32_load(var17 + 8) else 0):
            break
        i32_store(var0 + 108, var1)
        if (1 if i32_load(var0 + 104) < var1 else 0):
            break
        return 0
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
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    return 2955


# ==========================================================
# $func1076
# ==========================================================
def func1076(var0, var1):
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
    if (1 if var1 <= i32_load(i32_load(var0 + 8) + 88) else 0):
        var3 = i32_load(var0 + 108)
        var12 = (var1 - i32_load(var0 + 108))
        if (1 if (var1 - i32_load(var0 + 108)) <= 0 else 0):
            var7 = var3
            break
        var2 = i32_load(var0 + 100)
        var11 = (i32_load(var0 + 16) + ((var3 * i32_load(var0 + 100)) << 2))
        while True:  # loop $label5
            var8 = (16 if (1 if var12 >= 16 else 0) else var12)
            var7 = ((16 if (1 if var12 >= 16 else 0) else var12) + var3)
            var5 = i32_load(var0 + 8)
            var6 = i32_load(i32_load(var0 + 8))
            var13 = (i32_load(i32_load(var0 + 8)) * var8)
            var9 = i32_load(var5 + 40)
            var5 = (i32_load(i32_load(var5 + 40) + 136) + (var3 * var6))
            var10 = i32_load(var0 + 20)
            var4 = i32_load(var0 + 192)
            if (1 if i32_load(var0 + 192) > 0 else 0):
                var2 = (var4 - 1)
                if (1 if var4 == 1 else 0):
                    break
                while True:  # loop $label2
                    var4 = (var2 - 1)
                    var14 = (1 if var2 > 1 else 0)
                    var2 = var4
                    if var14:
                        continue
                    break  # end loop
                break
            if (1 if var10 == var11 else 0):
                break
            # Unknown: memory.copy []
            # call_indirect via table[i32_load(9687312)]
            var2 = i32_load(var9 + 12)
            if i32_load(var9 + 12):
                if (1 if i32_load(((var2 << 2) + 9687552)) == 0 else 0):
                    break
                var2 = i32_load(var9 + 140)
                if (var8 & 1):
                    # call_indirect via table[i32_load(((i32_load(var9 + 12) << 2) + 9687552))]
                    var3 = (var3 + 1)
                    var2 = var5
                else:
                var4 = var5
                if (1 if var8 != 1 else 0):
                    while True:  # loop $label4
                        # call_indirect via table[i32_load(((i32_load(var9 + 12) << 2) + 9687552))]
                        var2 = (var4 + var6)
                        # call_indirect via table[i32_load(((i32_load(var9 + 12) << 2) + 9687552))]
                        var4 = (var2 + var6)
                        var5 = var2
                        var3 = (var3 + 2)
                        if (1 if (var3 + 2) != var7 else 0):
                            continue
                        break  # end loop
                i32_store(var9 + 140, var5)
            var2 = i32_load(var0 + 100)
            var11 = (var11 + ((i32_load(var0 + 100) * var8) << 2))
            var3 = var7
            var12 = (var12 - var8)
            if (1 if (var12 - var8) > 0 else 0):
                continue
            break  # end loop
        if (1 if var1 != var7 else 0):
            break
        i32_store(var0 + 108, var1)
        i32_store(var0 + 116, var1)
        return call_indirect(i32_load(((i32_load(var9 + 12) << 2) + 9687552)))
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    return 2967


# ==========================================================
# $func1077
# ==========================================================
def func1077(var0, var1, var2):
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
    var3 = i32_load(var0 + 36)
    if (1 if i32_load((i32_load(var0 + 36) - -64)) >= i32_load(var3 + 56) else 0):
        break
    var8 = i32_load(var3 + 52)
    if (1 if i32_load(var3 + 52) <= 0 else 0):
        while True:  # loop $label2
            if (1 if i32_load(var3 + 24) > 0 else 0):
                break
            if (1 if var2 <= var4 else 0):
                break
            if (1 if i32_load(i32_load(var0) + 8) <= (var1 + var4) else 0):
                break
            func91(0  # stack underflow, var3)
            var4 = (var4 + 1)
            var3 = i32_load(var0 + 36)
            if (1 if i32_load((i32_load(var0 + 36) - -64)) < i32_load(var3 + 56) else 0):
                continue
            break  # end loop
        break
    var9 = i32_load(var0)
    var11 = (i32_load(i32_load(var0)) - 7)
    var12 = (var8 & -2)
    var13 = (var8 & 1)
    var14 = (i32_load(var9 + 16) + (i32_load(var9 + 20) * var1))
    var6 = ((i32_load(var9 + 16) + (i32_load(var9 + 20) * var1)) + 1)
    var5 = 15
    while True:  # loop $label5
        if (1 if i32_load(var3 + 24) > 0 else 0):
            break
        if (1 if var2 <= var4 else 0):
            break
        if (1 if i32_load(i32_load(var0) + 8) <= (var1 + var4) else 0):
            break
        func91(0  # stack underflow, var3)
        var3 = 0
        var10 = 0
        if (1 if var8 != 1 else 0):
            while True:  # loop $label4
                var7 = (var6 + (var3 << 1))
                var15 = ((i32_load8_u((i32_load(i32_load(var0 + 36) + 68) + var3)) & 0xFFFFFFFF) >> 4)
                i32_store8((var6 + (var3 << 1)), (((i32_load8_u((i32_load(i32_load(var0 + 36) + 68) + var3)) & 0xFFFFFFFF) >> 4) | (i32_load8_u(var7) & 240)))
                var7 = (var3 | 1)
                var16 = (var6 + ((var3 | 1) << 1))
                var7 = ((i32_load8_u((i32_load(i32_load(var0 + 36) + 68) + var7)) & 0xFFFFFFFF) >> 4)
                i32_store8((var6 + ((var3 | 1) << 1)), (((i32_load8_u((i32_load(i32_load(var0 + 36) + 68) + var7)) & 0xFFFFFFFF) >> 4) | (i32_load8_u(var16) & 240)))
                var5 = ((var5 & var15) & var7)
                var3 = (var3 + 2)
                var10 = (var10 + 2)
                if (1 if (var10 + 2) != var12 else 0):
                    continue
                break  # end loop
        if var13:
            var10 = (var6 + (var3 << 1))
            var3 = ((i32_load8_u((i32_load(i32_load(var0 + 36) + 68) + var3)) & 0xFFFFFFFF) >> 4)
            i32_store8((var6 + (var3 << 1)), (((i32_load8_u((i32_load(i32_load(var0 + 36) + 68) + var3)) & 0xFFFFFFFF) >> 4) | (i32_load8_u(var10) & 240)))
            var5 = (var3 & var5)
        var4 = (var4 + 1)
        var6 = (var6 + i32_load(var9 + 20))
        var3 = i32_load(var0 + 36)
        if (1 if i32_load((i32_load(var0 + 36) - -64)) < i32_load(var3 + 56) else 0):
            continue
        break  # end loop
    if (1 if var11 > 3 else 0):
        break
    if (1 if var5 == 15 else 0):
        break
    # call_indirect via table[i32_load(9687296)]
    return var4
    a_c()
    raise RuntimeError('unreachable')
    return 7727

