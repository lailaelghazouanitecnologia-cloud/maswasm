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
# $func178
# ==========================================================
def func178(var0):
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
    var8 = i32_load(var0 + 44)
    var11 = (i32_load(var0 + 44) - 262)
    var2 = i32_load(var0 + 116)
    while True:  # loop $label10
        var7 = i32_load(var0 + 108)
        var6 = (i32_load(var0 + 60) - (var2 + i32_load(var0 + 108)))
        if (1 if (var11 + i32_load(var0 + 44)) <= var7 else 0):
            var1 = i32_load(var0 + 56)
            i32_store(var0 + 112, (i32_load(var0 + 112) - var8))
            var7 = (i32_load(var0 + 108) - var8)
            i32_store(var0 + 108, (i32_load(var0 + 108) - var8))
            i32_store(var0 + 92, (i32_load(var0 + 92) - var8))
            if (1 if var7 < i32_load(var0 + 5812) else 0):
                i32_store(var0 + 5812, var7)
            var1 = i32_load(var0 + 76)
            var5 = (i32_load(var0 + 76) - 1)
            var4 = (i32_load(var0 + 68) + (var1 << 1))
            var3 = i32_load(var0 + 44)
            var2 = 0
            var9 = (var1 & 3)
            if (var1 & 3):
                while True:  # loop $label0
                    var4 = (var4 - 2)
                    var10 = i32_load16_u(var4)
                    var12 = (i32_load16_u(var4) - var3)
                    i32_store16((var4 - 2), ((i32_load16_u(var4) - var3) if (1 if var10 >= var12 else 0) else 0))
                    var1 = (var1 - 1)
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != var9 else 0):
                        continue
                    break  # end loop
            if (1 if var5 >= 3 else 0):
                while True:  # loop $label1
                    var2 = (var4 - 2)
                    var2 = i32_load16_u(var2)
                    var5 = (i32_load16_u(var2) - var3)
                    i32_store16((var4 - 2), ((i32_load16_u(var2) - var3) if (1 if var2 >= var5 else 0) else 0))
                    var2 = (var4 - 4)
                    var2 = i32_load16_u(var2)
                    var5 = (i32_load16_u(var2) - var3)
                    i32_store16((var4 - 4), ((i32_load16_u(var2) - var3) if (1 if var2 >= var5 else 0) else 0))
                    var2 = (var4 - 6)
                    var2 = i32_load16_u(var2)
                    var5 = (i32_load16_u(var2) - var3)
                    i32_store16((var4 - 6), ((i32_load16_u(var2) - var3) if (1 if var2 >= var5 else 0) else 0))
                    var4 = (var4 - 8)
                    var2 = i32_load16_u(var4)
                    var5 = (i32_load16_u(var4) - var3)
                    i32_store16((var4 - 8), ((i32_load16_u(var4) - var3) if (1 if var2 >= var5 else 0) else 0))
                    var1 = (var1 - 4)
                    if (var1 - 4):
                        continue
                    break  # end loop
            var4 = (i32_load(var0 + 64) + (var3 << 1))
            var2 = 0
            var1 = var3
            var5 = (var3 & 3)
            if (var3 & 3):
                while True:  # loop $label2
                    var4 = (var4 - 2)
                    var9 = i32_load16_u(var4)
                    var10 = (i32_load16_u(var4) - var3)
                    i32_store16((var4 - 2), ((i32_load16_u(var4) - var3) if (1 if var9 >= var10 else 0) else 0))
                    var1 = (var1 - 1)
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != var5 else 0):
                        continue
                    break  # end loop
            if (1 if (var3 - 1) >= 3 else 0):
                while True:  # loop $label3
                    var2 = (var4 - 2)
                    var2 = i32_load16_u(var2)
                    var5 = (i32_load16_u(var2) - var3)
                    i32_store16((var4 - 2), ((i32_load16_u(var2) - var3) if (1 if var2 >= var5 else 0) else 0))
                    var2 = (var4 - 4)
                    var2 = i32_load16_u(var2)
                    var5 = (i32_load16_u(var2) - var3)
                    i32_store16((var4 - 4), ((i32_load16_u(var2) - var3) if (1 if var2 >= var5 else 0) else 0))
                    var2 = (var4 - 6)
                    var2 = i32_load16_u(var2)
                    var5 = (i32_load16_u(var2) - var3)
                    i32_store16((var4 - 6), ((i32_load16_u(var2) - var3) if (1 if var2 >= var5 else 0) else 0))
                    var4 = (var4 - 8)
                    var2 = i32_load16_u(var4)
                    var5 = (i32_load16_u(var4) - var3)
                    i32_store16((var4 - 8), ((i32_load16_u(var4) - var3) if (1 if var2 >= var5 else 0) else 0))
                    var1 = (var1 - 4)
                    if (var1 - 4):
                        continue
                    break  # end loop
            var6 = (var6 + var8)
        var1 = i32_load(var0)
        var4 = i32_load(i32_load(var0) + 4)
        if (1 if i32_load(i32_load(var0) + 4) == 0 else 0):
            break
        var2 = i32_load(var0 + 116)
        var3 = (var4 if (1 if var4 < var6 else 0) else var6)
        if (var4 if (1 if var4 < var6 else 0) else var6):
            var6 = i32_load(var0 + 56)
            i32_store(var1 + 4, (var4 - var3))
            var4 = func35(((var6 + var7) + var2), i32_load(var1), var3)
            # br_table ['$label5', '$label6', '$label7']
            _br_idx = (i32_load(i32_load(var1 + 28) + 24) - 1)
            break  # br_table
            i32_store(var1 + 48, func89(i32_load(var1 + 48), var4, var3))
            break
            i32_store(var1 + 48, func43(i32_load(var1 + 48), var4, var3))
            i32_store(var1, (i32_load(var1) + var3))
            i32_store(var1 + 8, (i32_load(var1 + 8) + var3))
        else:
        var2 = (var2 + var3)
        i32_store(i32_load(var0 + 116) + 116, (var2 + var3))
        var4 = i32_load(var0 + 5812)
        if (1 if (i32_load(var0 + 5812) + var2) < 3 else 0):
            break
        var7 = i32_load(var0 + 56)
        var3 = (i32_load(var0 + 108) - var4)
        var1 = (i32_load(var0 + 56) + (i32_load(var0 + 108) - var4))
        var6 = i32_load8_u((i32_load(var0 + 56) + (i32_load(var0 + 108) - var4)))
        i32_store(var0 + 72, i32_load8_u((i32_load(var0 + 56) + (i32_load(var0 + 108) - var4))))
        var5 = i32_load(var0 + 84)
        var6 = i32_load(var0 + 88)
        var1 = (i32_load(var0 + 84) & (i32_load8_u(var1 + 1) ^ (var6 << i32_load(var0 + 88))))
        i32_store(var0 + 72, (i32_load(var0 + 84) & (i32_load8_u(var1 + 1) ^ (var6 << i32_load(var0 + 88)))))
        while True:  # loop $label9
            if (1 if var4 == 0 else 0):
                break
            var1 = ((i32_load8_u((var3 + var7) + 2) ^ (var1 << var6)) & var5)
            i32_store(var0 + 72, ((i32_load8_u((var3 + var7) + 2) ^ (var1 << var6)) & var5))
            var9 = (i32_load(var0 + 68) + (var1 << 1))
            i32_store16((i32_load(var0 + 64) + ((i32_load(var0 + 52) & var3) << 1)), i32_load16_u((i32_load(var0 + 68) + (var1 << 1))))
            i32_store16(var9, var3)
            var4 = (var4 - 1)
            i32_store(var0 + 5812, (var4 - 1))
            var3 = (var3 + 1)
            if (1 if (var2 + var4) > 2 else 0):
                continue
            break  # end loop
        if (1 if var2 > 261 else 0):
            break
        if i32_load(i32_load(var0) + 4):
            continue
        break  # end loop
    var4 = i32_load(var0 + 60)
    var1 = i32_load(var0 + 5824)
    if (1 if i32_load(var0 + 60) <= i32_load(var0 + 5824) else 0):
        break
    var3 = (i32_load(var0 + 116) + i32_load(var0 + 108))
    if (1 if (i32_load(var0 + 116) + i32_load(var0 + 108)) > var1 else 0):
        var1 = (var4 - var3)
        var1 = (258 if (1 if var1 >= 258 else 0) else (var4 - var3))
        func98((i32_load(var0 + 56) + var3), 0, (258 if (1 if var1 >= 258 else 0) else (var4 - var3)))
        break
    var3 = (var3 + 258)
    if (1 if (var3 + 258) <= var1 else 0):
        break
    var3 = (var3 - var1)
    var1 = (var4 - var1)
    var1 = ((var3 - var1) if (1 if var1 > var3 else 0) else (var4 - var1))
    func98((i32_load(var0 + 56) + var1), 0, ((var3 - var1) if (1 if var1 > var3 else 0) else (var4 - var1)))
    i32_store((var1 + var3) + 5824, (i32_load(var0 + 5824) + var1))
    return var0


# ==========================================================
# $func184
# ==========================================================
def func184(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var4 = i32_load(var0 + 5820)
    if (1 if i32_load(var0 + 5820) >= 14 else 0):
        var4 = (i32_load16_u(var0 + 5816) | (var3 << var4))
        i32_store16(var0 + 5816, (i32_load16_u(var0 + 5816) | (var3 << var4)))
        var5 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var5 + i32_load(var0 + 8)), var4)
        var4 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var4 + i32_load(var0 + 8)), i32_load8_u((var0 + 5817)))
        var3 = i32_load(var0 + 5820)
        var5 = (((var3 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820)))
        i32_store16(var0 + 5816, (((var3 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
        break
    var5 = (i32_load16_u(var0 + 5816) | (var3 << var4))
    i32_store16(var0 + 5816, (i32_load16_u(var0 + 5816) | (var3 << var4)))
    var3 = (var4 + 3)
    if (1 if (var4 + 3) >= 9 else 0):
        var3 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var3 + i32_load(var0 + 8)), var5)
        var3 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var3 + i32_load(var0 + 8)), i32_load8_u((var0 + 5817)))
        break
    if (1 if var3 <= 0 else 0):
        break
    var3 = i32_load(var0 + 20)
    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
    i32_store8((var3 + i32_load(var0 + 8)), var5)
    i32_store(var0 + 5820, 0)
    i32_store16(var0 + 5816, 0)
    var3 = i32_load(var0 + 20)
    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
    i32_store8((var3 + i32_load(var0 + 8)), var2)
    var3 = i32_load(var0 + 20)
    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
    i32_store8((var3 + i32_load(var0 + 8)), ((var2 & 0xFFFFFFFF) >> 8))
    var3 = i32_load(var0 + 20)
    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
    var3 = (var2 ^ -1)
    i32_store8((var3 + i32_load(var0 + 8)), (var2 ^ -1))
    var4 = i32_load(var0 + 20)
    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
    i32_store8((var4 + i32_load(var0 + 8)), ((var3 & 0xFFFFFFFF) >> 8))
    if var2:
    i32_store(var0 + 20, (i32_load(var0 + 20) + var2))
    return (var3 - 13)

