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
# $func402
# ==========================================================
def func402(var0):
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
    i32_store(9142440, var0)
    i32_store(9142852, 0)
    var5 = (var0 * var0)
    var9 = ((var0 * var0) << 1)
    var1 = func26(((var0 * var0) << 1))
    # Unknown: memory.fill []
    i32_store(9142436, var1)
    var1 = (var0 + 2)
    var10 = ((var0 + 2) * var1)
    var2 = func26((-1 if (1 if (var10 * 3) > 1073741823 else 0) else (((var0 + 2) * var1) * 12)))
    if var1:
        var12 = (var1 & -2)
        var13 = (var0 & 1)
        var8 = (var0 + 1)
        var7 = (var1 << 1)
        var14 = ((var1 << 1) * var1)
        while True:  # loop $label3
            if (1 if var4 == 0 else 0):
                var3 = 0
                var6 = 0
                if var8:
                    while True:  # loop $label0
                        i32_store((var2 + ((var1 * var3) << 2)), -1)
                        i32_store((var2 + (((var1 + var3) * var1) << 2)), -1)
                        i32_store((var2 + (((var3 + var7) * var1) << 2)), -1)
                        var11 = (var3 | 1)
                        i32_store((var2 + (((var3 | 1) * var1) << 2)), -1)
                        i32_store((var2 + (((var1 + var11) * var1) << 2)), -1)
                        i32_store((var2 + (((var7 + var11) * var1) << 2)), -1)
                        var3 = (var3 + 2)
                        var6 = (var6 + 2)
                        if (1 if (var6 + 2) != var12 else 0):
                            continue
                        break  # end loop
                if (1 if var13 == 0 else 0):
                    break
                i32_store((var2 + ((var1 * var3) << 2)), -1)
                i32_store((var2 + (((var1 + var3) * var1) << 2)), -1)
                i32_store((var2 + (((var3 + var7) * var1) << 2)), -1)
                break
            i32_store((var2 + (var4 << 2)), -1)
            i32_store((var2 + ((var4 + var10) << 2)), -1)
            i32_store((var2 + ((var4 + var14) << 2)), -1)
            var3 = 1
            if (1 if var1 == 1 else 0):
                break
            while True:  # loop $label2
                var6 = (0 - ((1 if var3 == var8 else 0) | (1 if var4 == var8 else 0)))
                i32_store((var2 + (((var1 * var3) + var4) << 2)), (0 - ((1 if var3 == var8 else 0) | (1 if var4 == var8 else 0))))
                i32_store((var2 + ((((var1 + var3) * var1) + var4) << 2)), var6)
                i32_store((var2 + ((((var3 + var7) * var1) + var4) << 2)), var6)
                var3 = (var3 + 1)
                if (1 if (var3 + 1) != var1 else 0):
                    continue
                break  # end loop
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var1 else 0):
                continue
            break  # end loop
    i32_store(9142840, var2)
    if (1 if i32_load8_u(9216060) == 0 else 0):
        var1 = (-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2))
        var2 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
        # Unknown: memory.fill []
        i32_store(9142432, var2)
    if i32_load8_u(9147152):
        break
    var2 = i32_load(9142424)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load(9147376):
        break
    var3 = (var9 | 4)
    var1 = func26((var9 | 4))
    # Unknown: memory.fill []
    i32_store(9147376, var1)
    if (1 if i32_load(var2 + 172) == 0 else 0):
        break
    if (1 if i32_load(var2 + 48) != 2 else 0):
        break
    if (1 if var0 == 0 else 0):
        break
    var2 = (1 if (1 if var5 <= 1 else 0) else var5)
    var3 = ((1 if (1 if var5 <= 1 else 0) else var5) & 5)
    var4 = 0
    var0 = 0
    if (1 if (var2 - 1) >= 7 else 0):
        var5 = (var2 & 2147483640)
        while True:  # loop $label5
            var2 = (var0 << 1)
            i32_store16((var1 + (var0 << 1)), 1)
            i32_store16((var1 + (var2 | 2)), 1)
            i32_store16((var1 + (var2 | 4)), 1)
            i32_store16((var1 + (var2 | 6)), 1)
            i32_store16((var1 + (var2 | 8)), 1)
            i32_store16((var1 + (var2 | 10)), 1)
            i32_store16((var1 + (var2 | 12)), 1)
            i32_store16((var1 + (var2 | 14)), 1)
            var0 = (var0 + 8)
            var15 = (var15 + 8)
            if (1 if (var15 + 8) != var5 else 0):
                continue
            break  # end loop
    if (1 if var3 == 0 else 0):
        break
    while True:  # loop $label6
        i32_store16((var1 + (var0 << 1)), 1)
        var0 = (var0 + 1)
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var3 else 0):
            continue
        break  # end loop
    i32_store(9147360, -1)
    i32_store(9147344, 1)
    var0 = i32_load(9142440)
    i32_store(9147368, i32_load(9142440))
    i32_store(9147372, (var0 + 1))
    i32_store(9147364, (var0 - 1))
    i32_store(9147356, (var0 ^ -1))
    i32_store(9147352, (0 - var0))
    i32_store(9147348, (1 - var0))

