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
# $func267
# ==========================================================
def func267(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    while True:  # loop $label3
        var2 = 6
        var3 = 10
        var1 = i32_load(var0)
        # br_table ['$label0', '$label1', '$label2']
        _br_idx = ((i32_load(var0) & 2147483647) - 2147483646)
        break  # br_table
        if (1 if var1 != (var1 + 1) else 0):
            continue
        break  # end loop
    var3 = 0
    var2 = var3
    return var2

