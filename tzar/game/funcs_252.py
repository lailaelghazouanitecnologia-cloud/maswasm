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
# $func919
# ==========================================================
def func919(var0, var1, var2, var3, var4):
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
    var2 = i32_load(var1)
    if (1 if var0 == i32_load(var1) else 0):
        break
    var3 = i32_load(9671128)
    var6 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load((i32_load(9671128) + (var0 * 132)) + 52) == 0 else 0):
        break
    var7 = i32_load8_u(var6 + 122)
    var1 = (var3 + (var2 * 132))
    var4 = i32_load8_u((var3 + (var2 * 132)) + 122)
    if (1 if func162(var6, i32_load8_u((var3 + (var2 * 132)) + 122), i32_load8_u(var1 + 125), var2) == 0 else 0):
        break
    var1 = 0
    if i32_load(((var7 * 404) + 9568096) + 260):
        break
    if (1 if var2 == 0 else 0):
        break
    var1 = 1
    var10 = (var3 + (var0 * 132))
    # br_table ['$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label1', '$label2']
    _br_idx = (i32_load8_u((var3 + (var0 * 132)) + 125) - 4)
    break  # br_table
    var8 = i32_load(((var4 * 404) + 9568096) + 216)
    if (1 if i32_load(((var4 * 404) + 9568096) + 216) == 0 else 0):
        break
    var1 = ((var7 * 404) + 9568096)
    var11 = ((var7 * 404) + 9568096)
    var4 = (var3 + (var2 * 132))
    var12 = i32_load16_u((var3 + (var2 * 132)) + 114)
    var5 = (var3 + (var0 * 132))
    var13 = i32_load16_u((var3 + (var0 * 132)) + 114)
    var14 = i32_load16_u(var4 + 112)
    var15 = i32_load16_u(var5 + 112)
    var1 = i32_load(var1 + 224)
    var16 = (i32_load(var1 + 224) * var1)
    var4 = 0
    var5 = 1
    while True:  # loop $label6
        var1 = (var13 - (var4 + var12))
        var17 = ((var13 - (var4 + var12)) * var1)
        var1 = 0
        while True:  # loop $label5
            var9 = (var15 - (var1 + var14))
            var9 = (((var15 - (var1 + var14)) * var9) + var17)
            if (1 if var16 >= ((((var15 - (var1 + var14)) * var9) + var17) - 1) else 0):
                var18 = i32_load(var11 + 228)
                if (1 if var9 >= (i32_load(var11 + 228) * var18) else 0):
                    break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var8 else 0):
                continue
            break  # end loop
        var4 = (var4 + 1)
        var5 = (1 if (var4 + 1) < var8 else 0)
        if (1 if var4 != var8 else 0):
            continue
        break  # end loop
    if (1 if var5 == 0 else 0):
        break
    var4 = i32_load(9215884)
    var0 = (var3 + (var0 * 132))
    var1 = i32_load((var3 + (var0 * 132)) + 44)
    if (1 if i32_load((i32_load(9215884) + (i32_load((var3 + (var0 * 132)) + 44) << 4)) + 4) == 6 else 0):
        i32_store((var4 + ((var1 << 4) | 12)), var2)
        var1 = 1
        var0 = i32_load(var0 + 44)
        if (1 if i32_load(var0 + 44) == 0 else 0):
            break
        var0 = (var4 + (var0 << 4))
        var2 = i32_load((var4 + (var0 << 4)))
        if (1 if i32_load((var4 + (var0 << 4))) != i32_load(9142848) else 0):
            break
        var0 = i32_load(((var7 * 404) + 9568096) + 276)
        i32_store(var0, ((((i32_load(((var7 * 404) + 9568096) + 276) & 0xFFFFFFFF) // 25) if var0 else 1) + var2))
        break
    i32_store8(var10 + 125, 1)
    i32_store8(var10 + 125, 0)
    break
    var1 = 1
    func29(var6, 1)
    return var1
    return 1

