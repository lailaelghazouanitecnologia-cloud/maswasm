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
# $func69
# ==========================================================
def func69(var0, var1):
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
    var7 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var8 = i32_load16_u(var0 + 116)
    if (1 if i32_load16_u(var0 + 116) == 0 else 0):
        break
    var9 = i32_load16_u(var0 + 118)
    if (1 if i32_load16_u(var0 + 118) == 0 else 0):
        break
    var5 = i32_load(9671128)
    var10 = (i32_load(9671128) + (var1 * 132))
    var3 = i32_load(9142840)
    var2 = (var8 + 1)
    var4 = (i32_load(9142440) + 2)
    var6 = (var9 + 1)
    var0 = i32_load((i32_load(9142840) + (((var8 + 1) + ((i32_load(9142440) + 2) * (var9 + 1))) << 2)))
    if (1 if i32_load((i32_load(9142840) + (((var8 + 1) + ((i32_load(9142440) + 2) * (var9 + 1))) << 2))) > 2 else 0):
        break
    var0 = i32_load((var3 + ((((var4 + var6) * var4) + var2) << 2)))
    if (1 if i32_load((var3 + ((((var4 + var6) * var4) + var2) << 2))) > 2 else 0):
        break
    var6 = i32_load8_u((var5 + (var0 * 132)) + 122)
    var3 = 0
    break
    var4 = (var5 + (var0 * 132))
    var6 = i32_load8_u((var5 + (var0 * 132)) + 122)
    var2 = i32_load(((i32_load8_u((var5 + (var0 * 132)) + 122) * 404) + 9568096) + 192)
    var11 = i32_load8_u(var10 + 122)
    # br_table ['$label3', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label3', '$label5']
    _br_idx = (i32_load8_u(var10 + 122) + -64)
    break  # br_table
    if (1 if var11 != 10 else 0):
        break
    if (1 if var2 > 1 else 0):
        break
    # br_table ['$label4', '$label6', '$label6', '$label6', '$label6', '$label6', '$label6', '$label6', '$label6', '$label6', '$label4', '$label6']
    _br_idx = (i32_load8_u((var5 + (var0 * 132)) + 125) - 4)
    break  # br_table
    var3 = 0
    var4 = func224(var4, var2, 0)
    if (1 if func224(var4, var2, 0) == 0 else 0):
        break
    var2 = -1
    var3 = 1
    var0 = var4
    break
    i32_store(var7 + 12, var1)
    var3 = 0
    if (1 if i32_load(38528) == var11 else 0):
        break
    var2 = -1
    var3 = func161(var4, (var7 + 12), 1)
    # br_table ['$label2', '$label7', '$label7', '$label7', '$label7', '$label7', '$label2', '$label7']
    _br_idx = func161(var4, (var7 + 12), 1)
    break  # br_table
    var2 = -1
    if (1 if i32_load(38564) == var6 else 0):
        break
    var2 = (5 if i32_load((var5 + (var1 * 132)) + 52) else 0)
    var3 = 0
    var0 = 0
    global global0
    global0 = (var7 + 16)

