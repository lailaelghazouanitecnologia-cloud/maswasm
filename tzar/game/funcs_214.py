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
# $De
# Export: De
# ==========================================================
def De(var0, var1, var2):
    """Export: De"""
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
    func182()
    var6 = i32_load(9142440)
    if (1 if i32_load(9142440) > 0 else 0):
        var3 = var6
        while True:  # loop $label2
            var5 = (var4 + 1)
            var8 = i32_load(9142840)
            var0 = 0
            while True:  # loop $label1
                var7 = var0
                var0 = (var0 + 1)
                if (1 if var3 <= var7 else 0):
                    break
                if (1 if var3 <= var4 else 0):
                    break
                i32_store((var8 + ((var5 + (var0 * (var3 + 2))) << 2)), 0)
                var3 = (i32_load(9142440) + 2)
                i32_store((var8 + ((var5 + ((var0 + (i32_load(9142440) + 2)) * var3)) << 2)), 0)
                var3 = (i32_load(9142440) + 2)
                i32_store((var8 + ((var5 + ((var0 + ((i32_load(9142440) + 2) << 1)) * var3)) << 2)), 0)
                var3 = i32_load(9142440)
                if (1 if var0 != var6 else 0):
                    continue
                break  # end loop
            var4 = var5
            if (1 if var5 != var6 else 0):
                continue
            break  # end loop
        if (1 if var3 > 0 else 0):
            var4 = 0
            var5 = var3
            while True:  # loop $label5
                var6 = (var4 + 1)
                var8 = i32_load(9142840)
                var0 = 0
                while True:  # loop $label4
                    var7 = var0
                    var0 = (var0 + 1)
                    if (1 if var5 <= var7 else 0):
                        break
                    if (1 if var4 >= var5 else 0):
                        break
                    i32_store((var8 + ((var6 + (var0 * (var5 + 2))) << 2)), 0)
                    var5 = (i32_load(9142440) + 2)
                    i32_store((var8 + ((var6 + ((var0 + (i32_load(9142440) + 2)) * var5)) << 2)), 0)
                    var5 = (i32_load(9142440) + 2)
                    i32_store((var8 + ((var6 + ((var0 + ((i32_load(9142440) + 2) << 1)) * var5)) << 2)), 0)
                    var5 = i32_load(9142440)
                    if (1 if var0 != var3 else 0):
                        continue
                    break  # end loop
                var4 = var6
                if (1 if var6 != var3 else 0):
                    continue
                break  # end loop
    else:
    var7 = ((var6 & 0xFFFFFFFF) >> 1)
    var16 = var7
    var14 = var2
    var15 = var7
    var13 = var1
    var4 = i32_load(9142440)
    if (1 if i32_load(9142440) > 0 else 0):
        var0 = ((var4 & 0xFFFFFFFF) >> 1)
        var8 = (((var4 & 0xFFFFFFFF) >> 1) + 15)
        var1 = (var0 - 15)
        var9 = (var4 & -4)
        var2 = (var4 & 3)
        var10 = (var4 & -2)
        var11 = (var4 & 1)
        var12 = (1 if var4 < 4 else 0)
        var3 = 0
        while True:  # loop $label12
            if (1 if ((1 if var1 < var3 else 0) & (1 if var3 < var8 else 0)) == 0 else 0):
                var0 = 0
                var5 = 0
                if (1 if var4 != 1 else 0):
                    while True:  # loop $label8
                        if (1 if var0 <= var1 else 0):
                            break
                        if (1 if var0 >= var8 else 0):
                            break
                        i32_store8((i32_load(9147288) + ((i32_load(9142440) * var0) + var3)), 3)
                        if (1 if var0 < var1 else 0):
                            break
                        var6 = (var0 | 1)
                        if (1 if (var0 | 1) >= var8 else 0):
                            break
                        i32_store8((i32_load(9147288) + ((i32_load(9142440) * var6) + var3)), 3)
                        var0 = (var0 + 2)
                        var5 = (var5 + 2)
                        if (1 if (var5 + 2) != var10 else 0):
                            continue
                        break  # end loop
                if (1 if var11 == 0 else 0):
                    break
                if (1 if var0 <= var1 else 0):
                    break
                if (1 if var0 >= var8 else 0):
                    break
                i32_store8((i32_load(9147288) + ((i32_load(9142440) * var0) + var3)), 3)
                break
            var5 = 0
            var0 = 0
            var6 = 0
            if (1 if var12 == 0 else 0):
                while True:  # loop $label10
                    i32_store8((i32_load(9147288) + ((i32_load(9142440) * var0) + var3)), 3)
                    i32_store8((i32_load(9147288) + ((i32_load(9142440) * (var0 | 1)) + var3)), 3)
                    i32_store8((i32_load(9147288) + ((i32_load(9142440) * (var0 | 2)) + var3)), 3)
                    i32_store8((i32_load(9147288) + ((i32_load(9142440) * (var0 | 3)) + var3)), 3)
                    var0 = (var0 + 4)
                    var6 = (var6 + 4)
                    if (1 if (var6 + 4) != var9 else 0):
                        continue
                    break  # end loop
            if (1 if var2 == 0 else 0):
                break
            while True:  # loop $label11
                i32_store8((i32_load(9147288) + ((i32_load(9142440) * var0) + var3)), 3)
                var0 = (var0 + 1)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var2 else 0):
                    continue
                break  # end loop
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var4 else 0):
                continue
            break  # end loop
        var4 = i32_load(9142440)
    var0 = (((var13 * var4) & 0xFFFFFFFF) // 100)
    var3 = (var15 - (((var13 * var4) & 0xFFFFFFFF) // 100))
    var6 = ((var0 << 1) + var7)
    if (1 if (var15 - (((var13 * var4) & 0xFFFFFFFF) // 100)) < ((var0 << 1) + var7) else 0):
        var5 = (var0 * var0)
        var1 = var3
        while True:  # loop $label15
            var0 = (var1 - var7)
            var8 = (((var1 - var7) * var0) - 1)
            var0 = var3
            while True:  # loop $label14
                var4 = (var0 - var7)
                if (1 if (var8 + ((var0 - var7) * var4)) > var5 else 0):
                    break
                var4 = i32_load(9142440)
                if (1 if i32_load(9142440) <= var0 else 0):
                    break
                if (1 if (var0 | var1) < 0 else 0):
                    break
                if (1 if var1 >= var4 else 0):
                    break
                i32_store8((i32_load(9147288) + ((var0 * var4) + var1)), 3)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var6 else 0):
                    continue
                break  # end loop
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var6 else 0):
                continue
            break  # end loop
        var4 = i32_load(9142440)
    var0 = (((var14 * var4) & 0xFFFFFFFF) // 100)
    var2 = (var16 - (((var14 * var4) & 0xFFFFFFFF) // 100))
    var3 = ((var0 << 1) + var7)
    if (1 if (var16 - (((var14 * var4) & 0xFFFFFFFF) // 100)) < ((var0 << 1) + var7) else 0):
        var4 = (var0 * var0)
        var1 = var2
        while True:  # loop $label18
            var0 = (var1 - var7)
            var5 = (((var1 - var7) * var0) - 1)
            var0 = var2
            while True:  # loop $label17
                var6 = (var0 - var7)
                if (1 if (var5 + ((var0 - var7) * var6)) > var4 else 0):
                    break
                var6 = i32_load(9142440)
                if (1 if i32_load(9142440) <= var0 else 0):
                    break
                if (1 if (var0 | var1) < 0 else 0):
                    break
                if (1 if var1 >= var6 else 0):
                    break
                i32_store8((i32_load(9147288) + ((var0 * var6) + var1)), 1)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var3 else 0):
                    continue
                break  # end loop
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var3 else 0):
                continue
            break  # end loop
        var4 = i32_load(9142440)
    var3 = 0
    if var4:
        var6 = i32_load(9147288)
        var3 = var4
        var5 = 0
        while True:  # loop $label21
            var1 = (var5 + 1)
            var2 = i32_load(9142840)
            var4 = i32_load(9140332)
            var0 = 0
            while True:  # loop $label20
                var7 = i32_load8_s((var6 + ((var0 * var3) + var5)))
                if (1 if i32_load8_s((var6 + ((var0 * var3) + var5))) < 0 else 0):
                    break
                if (1 if i32_load(i32_load((var4 + ((var7 & 255) << 2))) + 32) != 23 else 0):
                    break
                var7 = (var0 + 1)
                i32_store((var2 + ((((var0 + 1) * (var3 + 2)) + var1) << 2)), 1)
                var3 = (i32_load(9142440) + 2)
                i32_store((var2 + (((((i32_load(9142440) + 2) + var7) * var3) + var1) << 2)), 1)
                var3 = i32_load(9142440)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) < var3 else 0):
                    continue
                break  # end loop
            var5 = var1
            if (1 if var1 < var3 else 0):
                continue
            break  # end loop
    func169()
    return func343()


# ==========================================================
# $func736
# ==========================================================
def func736(var0, var1):
    var2 = 0
    var2 = i32_load(9671128)
    var1 = (i32_load(9671128) + (var0 * 132))
    func238(var1, i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110), var0)
    func29(var1, 1)
    if (1 if i32_load(var1 + 92) == 0 else 0):
        break
    var1 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var2 + (var0 * 132)) + 28) else 0):
            break

