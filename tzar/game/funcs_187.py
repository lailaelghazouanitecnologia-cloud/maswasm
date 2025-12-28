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
# $func225
# ==========================================================
def func225(var0, var1, var2, var3):
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
    var18 = 0
    var19 = 0
    var6 = i32_load(9142440)
    var12 = i32_load16_u(var2 + 114)
    var13 = i32_load16_u(var2 + 112)
    while True:  # loop $label9
        var11 = var4
        var4 = (var4 << 2)
        var7 = (i32_load((((var4 << 2) | 4) + 8611904)) + var12)
        if (1 if var6 <= (i32_load((((var4 << 2) | 4) + 8611904)) + var12) else 0):
            break
        var8 = (i32_load((var4 + 8611904)) + var13)
        if (1 if var6 <= (i32_load((var4 + 8611904)) + var13) else 0):
            break
        if (1 if (var7 | var8) < 0 else 0):
            break
        var4 = (var6 + 2)
        var4 = i32_load((i32_load(9142840) + ((var8 + (((var7 + (var6 + 2)) + 1) * var4)) << 2)) + 4)
        if (1 if i32_load((i32_load(9142840) + ((var8 + (((var7 + (var6 + 2)) + 1) * var4)) << 2)) + 4) == 0 else 0):
            break
        var4 = (i32_load(9671128) + (var4 * 132))
        if (1 if i32_load8_u((i32_load(9671128) + (var4 * 132)) + 129) == 10 else 0):
            break
        if (1 if i32_load(38528) != i32_load8_u(var4 + 122) else 0):
            break
        var4 = func56(var8, var7, var3, i32_load16_u(var2 + 110), 0, 0, 1, 1, 0)
        var6 = i32_load(9142440)
        if (1 if var4 == 0 else 0):
            break
        var5 = ((i32_load8_u(var2 + 122) * 404) + 9568096)
        # br_table ['$label2', '$label3', '$label3', '$label3', '$label2', '$label3']
        _br_idx = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 264)
        break  # br_table
        var14 = i32_load(var5 + 216)
        if (1 if i32_load(var5 + 216) == 0 else 0):
            var4 = i32_load(9142432)
            break
        var4 = i32_load(9142432)
        var15 = i32_load(var5 + 220)
        if (1 if i32_load(var5 + 220) == 0 else 0):
            break
        var5 = i32_load(9215880)
        if (1 if i32_load(9215880) == 0 else 0):
            break
        if (1 if var4 == 0 else 0):
            break
        var16 = i32_load16_u(var2 + 114)
        var17 = i32_load16_u(var2 + 112)
        var18 = i32_load(var5)
        var5 = 0
        while True:  # loop $label7
            var19 = (var5 + var17)
            var9 = 0
            while True:  # loop $label6
                var10 = i32_load((var4 + ((var19 + ((var9 + var16) * var6)) << 2)))
                if (1 if i32_load((var18 + (i32_load((var4 + ((var19 + ((var9 + var16) * var6)) << 2))) << 2))) == 0 else 0):
                    break
                var9 = (var9 + 1)
                if (1 if (var9 + 1) != var15 else 0):
                    continue
                break  # end loop
            var5 = (var5 + 1)
            if (1 if var14 != (var5 + 1) else 0):
                continue
            break  # end loop
        break
        var4 = i32_load(9142432)
        if (1 if i32_load(9142432) == 0 else 0):
            break
        var10 = i32_load((var4 + ((i32_load16_u(var2 + 112) + (var6 * i32_load16_u(var2 + 114))) << 2)))
        break
        var10 = 0
        if (1 if var4 == 0 else 0):
            break
        if (1 if var10 != i32_load((var4 + (((var6 * var7) + var8) << 2))) else 0):
            break
        i32_store(var0, var8)
        i32_store(var1, var7)
        return 1
        var4 = (var11 + 2)
        if (1 if var11 < 5198 else 0):
            continue
        break  # end loop
    return 0

