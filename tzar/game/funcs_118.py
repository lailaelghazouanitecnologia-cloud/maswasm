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
# $func112
# ==========================================================
def func112(var0, var1):
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
    var5 = i32_load(9142892)
    var9 = (i32_load(9142892) * var5)
    var7 = func26((i32_load(9142892) * var5))
    # Unknown: memory.fill []
    var8 = func26(var9)
    # Unknown: memory.fill []
    var11 = (var5 if (1 if var0 > var5 else 0) else var0)
    if (1 if var0 == 0 else 0):
        break
    if (1 if i32_load8_u(9147208) == 0 else 0):
        break
    if (1 if var5 >= 2 else 0):
        var2 = (var5 - 1)
        var12 = ((var5 - 1) & -4)
        var10 = (var2 & 3)
        var13 = (1 if (var5 - 2) < 3 else 0)
        var3 = 1
        while True:  # loop $label3
            var6 = (var3 * var5)
            var4 = 0
            var2 = 1
            if (1 if var13 == 0 else 0):
                while True:  # loop $label1
                    i32_store8((var7 + (var2 + var6)), (1 if var2 != var3 else 0))
                    var14 = (var2 + 1)
                    i32_store8((var7 + ((var2 + 1) + var6)), (1 if var3 != var14 else 0))
                    var14 = (var2 + 2)
                    i32_store8((var7 + ((var2 + 2) + var6)), (1 if var3 != var14 else 0))
                    var14 = (var2 + 3)
                    i32_store8((var7 + ((var2 + 3) + var6)), (1 if var3 != var14 else 0))
                    var2 = (var2 + 4)
                    var4 = (var4 + 4)
                    if (1 if (var4 + 4) != var12 else 0):
                        continue
                    break  # end loop
            var4 = 0
            if var10:
                while True:  # loop $label2
                    i32_store8((var7 + (var2 + var6)), (1 if var2 != var3 else 0))
                    var2 = (var2 + 1)
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != var10 else 0):
                        continue
                    break  # end loop
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var5 else 0):
                continue
            break  # end loop
    if (1 if var11 < 2 else 0):
        break
    var2 = (var11 - 1)
    var14 = ((var11 - 1) & -4)
    var13 = (var2 & 3)
    var6 = i32_load(9143004)
    var15 = (1 if (var11 - 2) < 3 else 0)
    var3 = 1
    while True:  # loop $label6
        var10 = (var3 * var5)
        var12 = (var0 * var3)
        var2 = 1
        var4 = 0
        if (1 if var15 == 0 else 0):
            while True:  # loop $label4
                i32_store8((var7 + (var2 + var10)), i32_load8_u((var6 + (var2 + var12))))
                var16 = (var2 + 1)
                i32_store8((var7 + ((var2 + 1) + var10)), i32_load8_u((var6 + (var12 + var16))))
                var16 = (var2 + 2)
                i32_store8((var7 + ((var2 + 2) + var10)), i32_load8_u((var6 + (var12 + var16))))
                var16 = (var2 + 3)
                i32_store8((var7 + ((var2 + 3) + var10)), i32_load8_u((var6 + (var12 + var16))))
                var2 = (var2 + 4)
                var4 = (var4 + 4)
                if (1 if (var4 + 4) != var14 else 0):
                    continue
                break  # end loop
        var4 = 0
        if var13:
            while True:  # loop $label5
                i32_store8((var7 + (var2 + var10)), i32_load8_u((var6 + (var2 + var12))))
                var2 = (var2 + 1)
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != var13 else 0):
                    continue
                break  # end loop
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != var11 else 0):
            continue
        break  # end loop
    if ((1 if var0 == 0 else 0) & (var1 ^ 1)):
        break
    if (1 if i32_load8_u(9147209) == 0 else 0):
        break
    if (1 if var5 >= 2 else 0):
        var1 = (var5 - 1)
        var10 = ((var5 - 1) & -4)
        var6 = (var1 & 3)
        var12 = (1 if (var5 - 2) < 3 else 0)
        var3 = 1
        while True:  # loop $label10
            var1 = (var3 * var5)
            var4 = 0
            var2 = 1
            if (1 if var12 == 0 else 0):
                while True:  # loop $label8
                    i32_store8((var8 + (var1 + var2)), (1 if var2 == var3 else 0))
                    var13 = (var2 + 1)
                    i32_store8((var8 + ((var2 + 1) + var1)), (1 if var3 == var13 else 0))
                    var13 = (var2 + 2)
                    i32_store8((var8 + ((var2 + 2) + var1)), (1 if var3 == var13 else 0))
                    var13 = (var2 + 3)
                    i32_store8((var8 + ((var2 + 3) + var1)), (1 if var3 == var13 else 0))
                    var2 = (var2 + 4)
                    var4 = (var4 + 4)
                    if (1 if (var4 + 4) != var10 else 0):
                        continue
                    break  # end loop
            var4 = 0
            if var6:
                while True:  # loop $label9
                    i32_store8((var8 + (var1 + var2)), (1 if var2 == var3 else 0))
                    var2 = (var2 + 1)
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != var6 else 0):
                        continue
                    break  # end loop
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var5 else 0):
                continue
            break  # end loop
    if (1 if var11 < 2 else 0):
        break
    var1 = (var11 - 1)
    var13 = ((var11 - 1) & -4)
    var12 = (var1 & 3)
    var1 = i32_load(9143012)
    var14 = (1 if (var11 - 2) < 3 else 0)
    var3 = 1
    while True:  # loop $label13
        var6 = (var3 * var5)
        var10 = (var0 * var3)
        var2 = 1
        var4 = 0
        if (1 if var14 == 0 else 0):
            while True:  # loop $label11
                i32_store8((var8 + (var2 + var6)), i32_load8_u((var1 + (var2 + var10))))
                var15 = (var2 + 1)
                i32_store8((var8 + ((var2 + 1) + var6)), i32_load8_u((var1 + (var10 + var15))))
                var15 = (var2 + 2)
                i32_store8((var8 + ((var2 + 2) + var6)), i32_load8_u((var1 + (var10 + var15))))
                var15 = (var2 + 3)
                i32_store8((var8 + ((var2 + 3) + var6)), i32_load8_u((var1 + (var10 + var15))))
                var2 = (var2 + 4)
                var4 = (var4 + 4)
                if (1 if (var4 + 4) != var13 else 0):
                    continue
                break  # end loop
        var4 = 0
        if var12:
            while True:  # loop $label12
                i32_store8((var8 + (var2 + var6)), i32_load8_u((var1 + (var2 + var10))))
                var2 = (var2 + 1)
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != var12 else 0):
                    continue
                break  # end loop
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != var11 else 0):
            continue
        break  # end loop
    var0 = i32_load(9143004)
    if (1 if i32_load(9143004) == 0 else 0):
        break
    i32_store(9143004, 0)
    var0 = i32_load(9143008)
    if i32_load(9143008):
        i32_store(9143008, 0)
    var0 = i32_load(9143016)
    if i32_load(9143016):
        i32_store(9143016, 0)
    if i32_load8_u(9147209):
        break
    var0 = i32_load(9143012)
    if (1 if i32_load(9143012) == 0 else 0):
        break
    i32_store(9143012, var8)
    i32_store(9143004, var7)
    var1 = func26(var9)
    # Unknown: memory.fill []
    i32_store(9143008, var1)
    var0 = func26(var9)
    # Unknown: memory.fill []
    i32_store(9143016, var0)
    var0 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var4 = (var0 - 1)
    var5 = ((var0 - 1) & 3)
    var2 = 1
    var11 = (var0 - 2)
    if (1 if (var0 - 2) >= 3 else 0):
        var8 = (var4 & -4)
        var3 = 0
        while True:  # loop $label16
            i32_store8((var7 + (var0 * var2)), 1)
            i32_store8((var2 + var7), 1)
            var9 = (var2 + 1)
            i32_store8((var7 + (var0 * (var2 + 1))), 1)
            i32_store8((var7 + var9), 1)
            var9 = (var2 + 2)
            i32_store8((var7 + (var0 * (var2 + 2))), 1)
            i32_store8((var7 + var9), 1)
            var9 = (var2 + 3)
            i32_store8((var7 + (var0 * (var2 + 3))), 1)
            i32_store8((var7 + var9), 1)
            var2 = (var2 + 4)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var8 else 0):
                continue
            break  # end loop
    if var5:
        var3 = 0
        while True:  # loop $label17
            i32_store8((var7 + (var0 * var2)), 1)
            i32_store8((var2 + var7), 1)
            var2 = (var2 + 1)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var5 else 0):
                continue
            break  # end loop
    if (1 if var0 < 2 else 0):
        break
    if (1 if i32_load8_u(9147208) == 0 else 0):
        var3 = i32_load(9561692)
        var4 = 1
        while True:  # loop $label20
            var5 = (var0 * var4)
            var8 = ((var3 + (var4 * 286704)) + 284608)
            var2 = 1
            while True:  # loop $label19
                var11 = (var2 + var5)
                var9 = (1 if var2 == var4 else 0)
                if (1 if var2 == var4 else 0):
                    break
                var6 = i32_load(var8)
                if (1 if i32_load(var8) == 0 else 0):
                    break
                i32_store8((var7 + (var2 + var5)), ((1 if var6 == i32_load((var3 + (var2 * 286704)) + 284608) else 0) ^ 1))
                i32_store8((var1 + var11), var9)
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != var0 else 0):
                    continue
                break  # end loop
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var0 else 0):
                continue
            break  # end loop
        break
    var9 = (var4 & -4)
    var8 = (var4 & 3)
    var3 = 1
    while True:  # loop $label23
        var5 = (var0 * var3)
        var4 = 0
        var2 = 1
        if (1 if var11 >= 3 else 0):
            while True:  # loop $label21
                i32_store8((var1 + (var2 + var5)), (1 if var2 == var3 else 0))
                var6 = (var2 + 1)
                i32_store8((var1 + ((var2 + 1) + var5)), (1 if var3 == var6 else 0))
                var6 = (var2 + 2)
                i32_store8((var1 + ((var2 + 2) + var5)), (1 if var3 == var6 else 0))
                var6 = (var2 + 3)
                i32_store8((var1 + ((var2 + 3) + var5)), (1 if var3 == var6 else 0))
                var2 = (var2 + 4)
                var4 = (var4 + 4)
                if (1 if (var4 + 4) != var9 else 0):
                    continue
                break  # end loop
        var4 = 0
        if var8:
            while True:  # loop $label22
                i32_store8((var1 + (var2 + var5)), (1 if var2 == var3 else 0))
                var2 = (var2 + 1)
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != var8 else 0):
                    continue
                break  # end loop
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != var0 else 0):
            continue
        break  # end loop
    if i32_load8_u(9147209):
        break
    var2 = 0
    var1 = (var0 * var0)
    var0 = func26((var0 * var0))
    # Unknown: memory.fill []
    i32_store(9143012, var0)
    if (1 if var1 == 0 else 0):
        break
    if (1 if var1 >= 4 else 0):
        var4 = (var1 & -4)
        var3 = 0
        while True:  # loop $label25
            i32_store8((var0 + var2), (i32_load8_u((var2 + var7)) ^ 1))
            var5 = (var2 | 1)
            i32_store8((var0 + (var2 | 1)), (i32_load8_u((var5 + var7)) ^ 1))
            var5 = (var2 | 2)
            i32_store8((var0 + (var2 | 2)), (i32_load8_u((var5 + var7)) ^ 1))
            var5 = (var2 | 3)
            i32_store8((var0 + (var2 | 3)), (i32_load8_u((var5 + var7)) ^ 1))
            var2 = (var2 + 4)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var4 else 0):
                continue
            break  # end loop
    var1 = (var1 & 3)
    if (1 if (var1 & 3) == 0 else 0):
        break
    var3 = 0
    while True:  # loop $label26
        i32_store8((var0 + var2), (i32_load8_u((var2 + var7)) ^ 1))
        var2 = (var2 + 1)
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != var1 else 0):
            continue
        break  # end loop
    return var1


# ==========================================================
# $func113
# ==========================================================
def func113(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    if (1 if i32_load8_u(9142917) == 0 else 0):
        var5 = ((i32_load(9142848) * 25) + var0)
        var2 = i32_load(9299864)
        if i32_load(9299864):
            var0 = 0
            var4 = i32_load(9299856)
            while True:  # loop $label1
                var3 = (var4 + (var0 << 2))
                if (1 if i32_load((var4 + (var0 << 2))) == 0 else 0):
                    break
                var0 = (var0 + 2)
                if (1 if (var0 + 2) < var2 else 0):
                    continue
                break  # end loop
        if (1 if i32_load(9299860) != var2 else 0):
            var3 = i32_load(9299856)
            break
        var0 = (i32_load(9299868) + var2)
        i32_store(9299860, (i32_load(9299868) + var2))
        var4 = i32_load(9299856)
        var3 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var2:
            # Unknown: memory.copy []
        if var4:
            var2 = i32_load(9299864)
        i32_store(9299856, var3)
        i32_store(9299864, (var2 + 1))
        i32_store((var3 + (var2 << 2)), var5)
        var0 = i32_load(9299864)
        if (1 if i32_load(9299864) != i32_load(9299860) else 0):
            var2 = var3
            break
        var2 = (i32_load(9299868) + var0)
        i32_store(9299860, (i32_load(9299868) + var0))
        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        if var0:
            # Unknown: memory.copy []
        i32_store(9299856, var2)
        var0 = i32_load(9299864)
        i32_store(9299864, (var0 + 1))
        break
        i32_store(var3, var5)
        i32_store((var4 + ((var0 << 2) | 4)), var1)
    return (var2 + (var0 << 2))

