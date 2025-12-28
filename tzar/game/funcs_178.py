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
# $id
# Export: id
# ==========================================================
def id():
    """Export: id"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var0 = i32_load(9142440)
    if (i32_load(9142440) * var0):
        while True:  # loop $label0
            var0 = (i32_load(9147288) + var1)
            i32_store8((i32_load(9147288) + var1), i32_load((9147296 if i32_load8_u(var0) else 9147292)))
            var1 = (var1 + 1)
            var0 = i32_load(9142440)
            if (1 if (var1 + 1) < (i32_load(9142440) * var0) else 0):
                continue
            break  # end loop
    var1 = 0
    var3 = i32_load(9684496)
    var0 = i32_load((i32_load(9684496) - 16))
    if (1 if i32_load((i32_load(9684496) - 16)) == 0 else 0):
        break
    if (1 if var0 >= 4 else 0):
        var5 = (var0 & -4)
        while True:  # loop $label2
            var2 = ((var1 * 60) + var3)
            i32_store(((var1 * 60) + var3) + 208, 2147483647)
            i32_store(var2 + 148, 2147483647)
            i32_store(var2 + 88, 2147483647)
            i32_store(var2 + 28, 2147483647)
            var1 = (var1 + 4)
            var4 = (var4 + 4)
            if (1 if (var4 + 4) != var5 else 0):
                continue
            break  # end loop
    var2 = (var0 & 3)
    if (1 if (var0 & 3) == 0 else 0):
        break
    var0 = 0
    while True:  # loop $label3
        i32_store(((var1 * 60) + var3) + 28, 2147483647)
        var1 = (var1 + 1)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var2 else 0):
            continue
        break  # end loop
    i32_store(9140308, 0)
    hd()


# ==========================================================
# $func886
# ==========================================================
def func886(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var2 = i32_load(var0 + 8)
    var3 = i32_load(var0 + 4)
    var4 = i32_load(var0)
    if i32_load8_u(9147210):
        var0 = 0
        var5 = i32_load(9142892)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var1 = i32_load(59164)
        var6 = i32_load(9561692)
        var0 = 1
        while True:  # loop $label1
            var7 = (var6 + (var0 * 286704))
            if (1 if i32_load((var6 + (var0 * 286704)) + 284616) == var1 else 0):
                break
            if (1 if i32_load(var7 + 284628) == var1 else 0):
                break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var5 else 0):
                continue
            break  # end loop
        var0 = 0
        break
    var0 = i32_load(9142872)
    func414(var4, var3, var2, var0, 0)

