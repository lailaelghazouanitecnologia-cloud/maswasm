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
# $func415
# ==========================================================
def func415(var0, var1):
    var2 = 0
    var3 = 0
    var2 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    if i32_load8_u(9142916):
        if (1 if var0 <= 15 else 0):
            var0 = (var0 << 4)
            var3 = ((((i32_load(((var0 << 4) + 1748)) << 8) + i32_load((var0 + 1744))) + (i32_load((var0 + 1752)) << 16)) + (i32_load((var0 + 1756)) << 24))
        i32_store(var2 + 20, var1)
        i32_store(var2 + 16, var3)
        a_b()
        break
    i32_store(var2 + 4, var1)
    i32_store(var2, var0)
    a_b()
    global global0
    global0 = (var2 + 32)


# ==========================================================
# $func423
# ==========================================================
def func423(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    if (1 if ((1 if (i32_reinterpret_f32(var0) & 2147483647) < 2139095041 else 0) & (1 if (i32_reinterpret_f32(var1) & 2147483647) <= 2139095040 else 0)) == 0 else 0):
        return (var0 + var1)
    var2 = i32_reinterpret_f32(var1)
    if (1 if i32_reinterpret_f32(var1) == 1065353216 else 0):
        return func422(var0)
    var5 = (((var2 & 0xFFFFFFFF) >> 30) & 2)
    var3 = i32_reinterpret_f32(var0)
    var4 = ((((var2 & 0xFFFFFFFF) >> 30) & 2) | ((i32_reinterpret_f32(var0) & 0xFFFFFFFF) >> 31))
    var3 = (var3 & 2147483647)
    if (1 if (var3 & 2147483647) == 0 else 0):
        # br_table ['$label0', '$label1', '$label2']
        _br_idx = (var4 - 2)
        break  # br_table
        return 3.14159274
        return -3.14159274
    var2 = (var2 & 2147483647)
    if (1 if (var2 & 2147483647) != 2139095040 else 0):
        if (1 if var2 == 0 else 0):
            # Unknown: f32.copysign []
            return var0
        if (1 if ((1 if var3 != 2139095040 else 0) & (1 if (var2 + 218103808) >= var3 else 0)) == 0 else 0):
            # Unknown: f32.copysign []
            return var0
        if var5:
            if (1 if (var3 + 218103808) < var2 else 0):
                break
        var0 = func422(abs((var0 / var1)))
        # br_table ['$label2', '$label4', '$label5', '$label6']
        _br_idx = var4
        break  # br_table
        return (-var0)
        return (3.14159274 - (var0 + 8.74227766e-08))
        return ((var0 + 8.74227766e-08) + -3.14159274)
    if (1 if var3 == 2139095040 else 0):
        break
    var0 = f32_load(((var4 << 2) + 28880))
    return var0
    return f32_load(((var4 << 2) + 28864))


# ==========================================================
# $Xc
# Export: Xc
# ==========================================================
def Xc(var0):
    """Export: Xc"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0.0
    var5 = 0.0
    var6 = 0.0
    var7 = 0.0
    var8 = 0.0
    var9 = 0.0
    var1 = (global0 - 96)
    global global0
    global0 = (global0 - 96)
    var2 = i32_load(9568088)
    var3 = i32_load(i32_load(9568088) + 28)
    if (1 if i32_load(i32_load(9568088) + 28) == 0 else 0):
        break
    var5 = float((var3 << 5))
    var6 = float((i32_load(var2 + 40) << 5))
    var7 = float((i32_load(var2 + 24) << 5))
    var8 = float((i32_load(var2 + 20) << 5))
    if (1 if i32_load8_u(9142917) == 0 else 0):
        var4 = ((var6 * 0.5) + var7)
        if ((1 if ((var6 * 0.5) + var7) < 4294967300.0 else 0) & (1 if var4 >= 0.0 else 0)):
            break
        i32_store(int(var4) + 84, 0)
        var4 = ((var5 * 0.5) + var8)
        if ((1 if ((var5 * 0.5) + var8) < 4294967300.0 else 0) & (1 if var4 >= 0.0 else 0)):
            break
        i32_store(int(var4) + 80, 0)
    if (1 if var0 == 0 else 0):
        i32_store8(9684432, 1)
    var0 = i32_load(9142876)
    if i32_load8_u(9142916):
    else:
    var9 = 0.0
    i32_store(var1 + 72, var0)
    f64_store((var1 - -64), var9)
    f64_store(var1 + 56, float(var7))
    f64_store(var1 + 48, float(var8))
    a_b()
    if i32_load8_u(9142916):
        break
    i64_store(var1 + 16, 0)
    i64_store(var1 + 24, 0)
    i32_store(var1 + 32, i32_load(9142876))
    f64_store(var1 + 8, float(var6))
    f64_store(var1, float((-var5)))
    a_b()
    global global0
    global0 = (var1 + 96)
    return var1

