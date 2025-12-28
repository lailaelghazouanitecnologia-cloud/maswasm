"""
Auto-generated from WAT. Contains 3 functions.
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
# $func71
# ==========================================================
def func71(var0, var1, var2, var3, var4, var5):
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var6 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var9 = ((var2 + var4) + 6)
    var7 = func26((-1 if (1 if var9 > 1073741823 else 0) else (((var2 + var4) + 6) << 2)))
    i64_store(func26((-1 if (1 if var9 > 1073741823 else 0) else (((var2 + var4) + 6) << 2))), -4294967296)
    var8 = i32_load(9142384)
    i32_store(var7 + 20, var4)
    i32_store(var7 + 16, var2)
    i32_store(var7 + 12, var0)
    i32_store(var7 + 8, var8)
    if var2:
        # Unknown: memory.copy []
    if var4:
        # Unknown: memory.copy []
    if (1 if i32_load8_u(9147125) == 0 else 0):
        i32_store(var6 + 4, var9)
        i32_store(var6, var7)
        break
    var10 = i32_load((9142892 if i32_load8_u(9147212) else 41092))
    if (1 if i32_load((9142892 if i32_load8_u(9147212) else 41092)) >= 2 else 0):
        var8 = i32_load(9561692)
        var4 = 1
        while True:  # loop $label1
            var11 = i32_load((var8 + (var4 * 286704)) + 284616)
            if i32_load((var8 + (var4 * 286704)) + 284616):
                i32_store(var6 + 24, var11)
                i32_store(var6 + 20, var9)
                i32_store(var6 + 16, var7)
                var8 = i32_load(9561692)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var10 else 0):
                continue
            break  # end loop
    if (1 if var5 == 0 else 0):
        i32_store(59164, i32_load(9142384))
        # call_indirect via table[i32_load(((var0 << 3) + 9213824))]
        i32_store(59164, 0)
    global global0
    global0 = (var6 + 48)


# ==========================================================
# $func92
# ==========================================================
def func92(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0.0
    var6 = 0.0
    var3 = (global0 - 128)
    global global0
    global0 = (global0 - 128)
    var4 = i32_load(var0 + 40)
    if i32_load(var0 + 40):
        var5 = float(var2)
        var6 = float(var1)
        if i32_load8_u(9142916):
            i32_store(var3 + 120, var4)
            i64_store(var3 + 112, 0)
            f64_store(var3 + 104, var5)
            f64_store(var3 + 96, var6)
            a_b()
            break
        i64_store((var3 - -64), 0)
        i32_store(var3 + 80, var4)
        f64_store(var3 + 72, float(float((i32_load(9142848) * 25))))
        f64_store(var3 + 48, var6)
        f64_store(var3 + 56, var5)
        a_b()
        if i32_load8_u(9142916):
            break
        var4 = i32_load(var0 + 92)
        if (1 if i32_load(var0 + 92) == 0 else 0):
            break
        if i32_load8_u(9142906):
            break
        i64_store(var3 + 16, 0)
        i32_store(var3 + 32, var4)
        f64_store(var3 + 24, float(float((i32_load(9142848) * 25))))
        f64_store(var3, var6)
        f64_store(var3 + 8, var5)
        a_b()
        func288(var0, var1, var2)
    global global0
    global0 = (var3 + 128)


# ==========================================================
# $func107
# ==========================================================
def func107(var0, var1, var2, var3, var4):
    var5 = 0
    var5 = (global0 - 256)
    global global0
    global0 = (global0 - 256)
    if (1 if var2 <= var3 else 0):
        break
    if (var4 & 73728):
        break
    var3 = (var2 - var3)
    var1 = (1 if var3 < 256 else 0)
    func98(var5, (var1 & 255), ((var2 - var3) if (1 if var3 < 256 else 0) else 256))
    if (1 if var1 == 0 else 0):
        while True:  # loop $label1
            var3 = (var3 - 256)
            if (1 if (var3 - 256) > 255 else 0):
                continue
            break  # end loop
    global global0
    global0 = (var5 + 256)

