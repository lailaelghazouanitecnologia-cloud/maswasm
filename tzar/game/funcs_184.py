"""
Auto-generated from WAT. Contains 1 functions.
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
# $func56
# ==========================================================
def func56(var0, var1, var2, var3, var4, var5, var6, var7, var8):
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
    var19 = 0
    var11 = i32_load(var2 + 248)
    # br_table ['$label0', '$label1', '$label2', '$label3']
    _br_idx = (i32_load(var2 + 248) - 1)
    break  # br_table
    return func282(var0, var1, var2, var4, var5, var6)
    return func283(var0, var1, var2, var4, var5, var6, var7)
    var3 = var0
    var7 = var2
    var12 = i32_load(var2 + 216)
    var10 = i32_load(var2 + 208)
    var9 = i32_load(var2 + 372)
    if (1 if var6 == 0 else 0):
        break
    if (1 if var12 <= 0 else 0):
        break
    var14 = (i32_load(var7 + 220) + var1)
    if (1 if (i32_load(var7 + 220) + var1) <= var1 else 0):
        break
    var17 = (var3 + var12)
    var15 = i32_load(9142440)
    var18 = (i32_load(9142440) + 2)
    var19 = ((i32_load(9142440) + 2) * var10)
    var11 = i32_load(var7 + 212)
    var8 = i32_load(9142840)
    var2 = var3
    while True:  # loop $label11
        var6 = (var2 + 1)
        var16 = (var2 - var3)
        var0 = var1
        var13 = var1
        if (1 if var2 < var15 else 0):
            while True:  # loop $label7
                if (1 if i32_load8_u((var9 + (var16 + ((var0 - var1) * var12)))) == 0 else 0):
                    var0 = (var0 + 1)
                    break
                var13 = 0
                if (1 if var0 >= var15 else 0):
                    break
                if (1 if (var0 | var2) < 0 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if i32_load((var8 + ((var6 + (((var0 + 1) + var19) * var18)) << 2))) != var11 else 0):
                    break
                if (1 if var0 != var14 else 0):
                    continue
                break
                break  # end loop
            raise RuntimeError('unreachable')
        while True:  # loop $label9
            if (1 if i32_load8_u((var9 + (var16 + ((var13 - var1) * var12)))) == 0 else 0):
                var13 = (var13 + 1)
                if (1 if var14 != (var13 + 1) else 0):
                    continue
                break
            break  # end loop
        break
        var2 = var6
        if (1 if var6 < var17 else 0):
            continue
        break  # end loop
    var13 = 1
    if (1 if var4 == 0 else 0):
        break
    if (1 if var12 <= 0 else 0):
        break
    var11 = (i32_load(var7 + 220) + var1)
    if (1 if (i32_load(var7 + 220) + var1) <= var1 else 0):
        break
    var8 = (var3 + var12)
    var0 = var3
    while True:  # loop $label14
        var2 = (var0 + 1)
        var7 = (var0 - var3)
        var6 = i32_load(9142840)
        var0 = var1
        while True:  # loop $label13
            if (1 if i32_load8_u((var9 + (var7 + ((var0 - var1) * var12)))) == 0 else 0):
                var0 = (var0 + 1)
                break
            var0 = (var0 + 1)
            var4 = (i32_load(9142440) + 2)
            i32_store((var6 + ((var2 + (((var0 + 1) + ((i32_load(9142440) + 2) * var10)) * var4)) << 2)), var5)
            if (1 if var0 != var11 else 0):
                continue
            break  # end loop
        var0 = var2
        if (1 if var2 < var8 else 0):
            continue
        break  # end loop
    return var13
    var7 = i32_load(var2 + 208)
    if (1 if i32_load(var2 + 208) == 0 else 0):
        var3 = var0
        var7 = var2
        var9 = i32_load(var2 + 216)
        var14 = i32_load(var2 + 372)
        if (1 if var6 == 0 else 0):
            break
        if (1 if var9 <= 0 else 0):
            break
        var16 = (i32_load(var7 + 220) + var1)
        if (1 if (i32_load(var7 + 220) + var1) <= var1 else 0):
            break
        var11 = (var3 + var9)
        var17 = i32_load(9142440)
        var15 = (i32_load(9142440) + 2)
        var8 = i32_load(9671128)
        var18 = i32_load(9142840)
        var2 = var3
        while True:  # loop $label22
            var6 = (var2 + 1)
            var19 = (var2 - var3)
            var0 = var1
            var10 = var1
            if (1 if var2 < var17 else 0):
                while True:  # loop $label18
                    if (1 if i32_load8_u((var14 + (var19 + ((var0 - var1) * var9)))) == 0 else 0):
                        var0 = (var0 + 1)
                        break
                    var10 = 0
                    if (1 if var0 >= var17 else 0):
                        break
                    if (1 if (var0 | var2) < 0 else 0):
                        break
                    var0 = (var0 + 1)
                    if i32_load((var18 + (((var15 * (var0 + 1)) + var6) << 2))):
                        break
                    if (1 if i32_load(((i32_load8_u((var8 + (i32_load((var18 + ((((var0 + var15) * var15) + var6) << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 1 else 0):
                        break
                    if (1 if var0 != var16 else 0):
                        continue
                    break
                    break  # end loop
                raise RuntimeError('unreachable')
            while True:  # loop $label20
                if (1 if i32_load8_u((var14 + (var19 + ((var10 - var1) * var9)))) == 0 else 0):
                    var10 = (var10 + 1)
                    if (1 if var16 != (var10 + 1) else 0):
                        continue
                    break
                break  # end loop
            break
            var2 = var6
            if (1 if var6 < var11 else 0):
                continue
            break  # end loop
        var10 = 1
        if (1 if var4 == 0 else 0):
            break
        if (1 if var9 <= 0 else 0):
            break
        var8 = (i32_load(var7 + 220) + var1)
        if (1 if (i32_load(var7 + 220) + var1) <= var1 else 0):
            break
        var7 = (var3 + var9)
        var0 = var3
        while True:  # loop $label25
            var2 = (var0 + 1)
            var6 = (var0 - var3)
            var4 = i32_load(9142840)
            var0 = var1
            while True:  # loop $label24
                if (1 if i32_load8_u((var14 + (var6 + ((var0 - var1) * var9)))) == 0 else 0):
                    var0 = (var0 + 1)
                    break
                var0 = (var0 + 1)
                i32_store((var4 + ((var2 + ((var0 + 1) * (i32_load(9142440) + 2))) << 2)), var5)
                if (1 if var0 != var8 else 0):
                    continue
                break  # end loop
            var0 = var2
            if (1 if var2 < var7 else 0):
                continue
            break  # end loop
        return var10
    # br_table ['$label26', '$label27', '$label28']
    _br_idx = (var11 - 4)
    break  # br_table
    return func193(var0, var1, var2, var3, var4, var5, var6, var8)
    return func194(var0, var1, var2, var3, var4, var5, var6)
    if (1 if var7 <= 2 else 0):
    else:
    return 0

