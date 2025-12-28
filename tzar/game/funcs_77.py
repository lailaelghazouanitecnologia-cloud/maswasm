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
# $func60
# ==========================================================
def func60(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0.0
    var11 = 0.0
    var12 = 0.0
    var13 = 0.0
    var14 = 0.0
    var15 = 0.0
    var4 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var3 = i32_load(var0 + 48)
    if (1 if i32_load(var0 + 48) == 0 else 0):
        break
    var2 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    var11 = (float(i32_load16_u(var0 + 112)) * 32.0)
    var13 = float(i32_load(var3 + 12))
    var14 = float(i32_load(var3 + 8))
    var12 = (float(i32_load16_u(var0 + 114)) * 32.0)
    var3 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var5 = i32_load(9142440)
    var10 = (((float(i32_load16_u(var0 + 114)) * 32.0) + ((1.0 if (1 if i32_load(var3 + 264) == 4 else 0) else float(i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 208))) * (float(i32_load(9142440)) * 32.0))) * var1)
    var1 = (((float(i32_load16_u(var0 + 114)) * 32.0) + ((1.0 if (1 if i32_load(var3 + 264) == 4 else 0) else float(i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 208))) * (float(i32_load(9142440)) * 32.0))) * var1)
    var3 = i32_load8_u(9142916)
    if (1 if i32_load8_u(9142916) == 0 else 0):
        break
    if (1 if var10 == -55.0 else 0):
        break
    var1 = (((var10 * 0.5) / float((var5 * 96))) + 0.25)
    i32_store(var4 + 56, var2)
    f64_store(var4 + 48, float(var1))
    f64_store(var4 + 40, float((var12 - (0.0 if var3 else var13))))
    f64_store(var4 + 32, float((var11 - (0.0 if var3 else var14))))
    a_b()
    if i32_load8_u(9142916):
        break
    var3 = i32_load(var0 + 92)
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    if i32_load8_u(9142906):
        break
    var2 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) == 1 else 0):
        if (1 if i32_load(var2 + 216) > 1 else 0):
            break
    var2 = i32_load(9142448)
    var5 = i32_load(i32_load(9142448) + 12)
    var2 = i32_load(var2 + 8)
    f64_store(var4 + 16, float((var10 + -1.0)))
    i32_store(var4 + 24, var3)
    f64_store(var4, float((var11 - float(var2))))
    f64_store(var4 + 8, float((var12 - float(var5))))
    a_b()
    var3 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var2 = i32_load(var0 + 24)
    if (1 if i32_load(var0 + 24) == 0 else 0):
        break
    var5 = i32_load(var2 + 4)
    if (1 if i32_load(var2 + 4) == 0 else 0):
        break
    if (1 if i32_load(var5 + 8) == 0 else 0):
        break
    var10 = (float(i32_load16_u(var0 + 112)) * 32.0)
    var1 = (float(i32_load16_u(var0 + 114)) * 32.0)
    var11 = ((float(i32_load16_u(var0 + 114)) * 32.0) + -44.0)
    var1 = (float(i32_load(9142440)) * 32.0)
    var1 = (var1 + ((float(i32_load(9142440)) * 32.0) + var1))
    var12 = ((var1 + ((float(i32_load(9142440)) * 32.0) + var1)) * 0.5)
    while True:  # loop $label6
        var6 = ((var8 | 1) << 2)
        var2 = i32_load((((var8 | 1) << 2) + i32_load(var5)))
        if (1 if i32_load((((var8 | 1) << 2) + i32_load(var5))) == 0 else 0):
            var2 = 0
            if i32_load8_u(9142917):
                break
            var2 = i32_load(9299880)
            if i32_load(9299880):
                var2 = (var2 - 1)
                i32_store(9299880, (var2 - 1))
                var2 = i32_load((i32_load(9299872) + (var2 << 2)))
                break
            var2 = i32_load(9163776)
            var7 = (i32_load(9163776) + 1)
            i32_store(9163776, (i32_load(9163776) + 1))
            var9 = i32_load(9163784)
            if (1 if var7 < i32_load(9163784) else 0):
                break
            i32_store(var3 + 32, var9)
            a_b()
            i32_store(9163784, (i32_load(9163784) + 40000))
            var7 = (i32_load16_u(var0 + 114) << 5)
            i32_store((i32_load(var5) + var6), var2)
        var6 = i32_load8_u(9142916)
        var7 = i32_load(9142584)
        var13 = float(i32_load(i32_load(9142584) + 12))
        var14 = float(i32_load(var7 + 8))
        if (1 if var1 == -55.0 else 0):
            break
        if (1 if var6 == 0 else 0):
            break
        var15 = ((var12 / float((i32_load(9142440) * 96))) + 0.25)
        i32_store(var3 + 24, var2)
        f64_store(var3 + 16, float(var15))
        f64_store(var3 + 8, float((var11 - (0.0 if var6 else var13))))
        f64_store(var3, float((var10 - (0.0 if var6 else var14))))
        a_b()
        var8 = (var8 + 2)
        if (1 if (var8 + 2) < i32_load(var5 + 8) else 0):
            continue
        break  # end loop
    global global0
    global0 = (var3 + 48)
    global global0
    global0 = (var4 - -64)
    return var3

