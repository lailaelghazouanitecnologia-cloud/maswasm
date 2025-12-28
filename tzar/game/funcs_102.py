"""
Auto-generated from WAT. Contains 6 functions.
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
# $Ca
# Export: Ca
# ==========================================================
def Ca(var0):
    """Export: Ca"""
    var1 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(var1 + 12, var0)
    func71(21, 0, 0, (var1 + 12), 1, 0)
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $func587
# ==========================================================
def func587(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var1 = 0
    var3 = i32_load(9142892)
    var4 = i32_load(var0)
    if i32_load8_u(9147210):
        if (1 if var3 < 2 else 0):
            break
        var5 = i32_load(59164)
        var6 = i32_load(9561692)
        var1 = 1
        while True:  # loop $label1
            var7 = (var6 + (var1 * 286704))
            if (1 if i32_load((var6 + (var1 * 286704)) + 284616) == var5 else 0):
                break
            if (1 if i32_load(var7 + 284628) == var5 else 0):
                break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var3 else 0):
                continue
            break  # end loop
        var1 = 0
        break
    var1 = i32_load(9142872)
    if (1 if var4 == 0 else 0):
        break
    if (1 if var1 == var4 else 0):
        break
    if (1 if var3 <= var4 else 0):
        break
    var3 = i32_load(9142424)
    if i32_load(i32_load(9142424) + 180):
        if (1 if i32_load(9142848) < (i32_load(var3 + 72) * 2400) else 0):
            break
    i32_store(var2, i32_load(var0 + 4))
    i32_store(var2 + 4, i32_load(var0 + 8))
    i32_store(var2 + 8, i32_load(var0 + 12))
    i32_store(var2 + 12, i32_load(var0 + 16))
    func322(var4, var1, var2)
    global global0
    global0 = (var2 + 16)


# ==========================================================
# $We
# Export: We
# ==========================================================
def We():
    """Export: We"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var3 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(var3 + 12, 0)
    func71(30, (var3 + 12), 1, 0, 0, 1)
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var5 = i32_load(9561692)
    var1 = 1
    while True:  # loop $label2
        var2 = (var5 + (var1 * 286704))
        var6 = i32_load((var5 + (var1 * 286704)) + 284616)
        if (1 if i32_load((var5 + (var1 * 286704)) + 284616) == 0 else 0):
            break
        if (1 if i32_load(var2 + 284604) == 0 else 0):
            break
        var7 = ((var0 << 2) + 8447808)
        i32_store(((var0 << 2) + 8447808), var6)
        i32_store(var7 + 4, i32_load((var2 + 284604)))
        var0 = (var0 + 2)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var4 else 0):
            continue
        break  # end loop
    if (1 if var0 == 0 else 0):
        break
    func71(32, 8447808, var0, 0, 0, 1)
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var0 = i32_load(9561692)
    var1 = 1
    while True:  # loop $label4
        var4 = (var0 + (var1 * 286704))
        if (1 if i32_load8_u((var0 + (var1 * 286704)) + 286699) == 0 else 0):
            var2 = i32_load(var4 + 284604)
            if (1 if i32_load8_u(9147210) == 0 else 0):
                break
            if (1 if i32_load(var4 + 284616) != i32_load(9561844) else 0):
                if (1 if i32_load(9142872) != var1 else 0):
                    break
                if (1 if i32_load8_u(9142388) == 0 else 0):
                    break
            var2 = 2147483647
            i32_store(var3 + 4, var2)
            i32_store(var3, var1)
            a_b()
            var2 = i32_load(9142892)
            var0 = i32_load(9561692)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < var2 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var3 + 16)


# ==========================================================
# $func649
# ==========================================================
def func649(var0, var1, var2):
    var0 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(var0 + 12, 0)
    func71(31, (var0 + 12), 1, 0, 0, 1)
    global global0
    global0 = (var0 + 16)


# ==========================================================
# $le
# Export: le
# ==========================================================
def le(var0):
    """Export: le"""
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(9142912, var0)
    var2 = (var0 << 2)
    var3 = (-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2))
    var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    # Unknown: memory.fill []
    i32_store(9142908, var0)
    i32_store(var1 + 12, var2)
    var0 = i32_load(9142908)
    global global0
    global0 = (var1 + 16)
    return var0


# ==========================================================
# $func792
# ==========================================================
def func792(var0, var1):
    var2 = 0.0
    var3 = 0.0
    var4 = 0.0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if var0 == 0 else 0):
        break
    if (1 if i32_load8_u(9163793) == 0 else 0):
        break
    if (1 if i32_load(9684392) > 2 else 0):
        break
    var5 = i32_load(9142856)
    var6 = i32_load(9142952)
    var7 = i32_load(9142864)
    var4 = f32_load(9671164)
    var0 = i32_load(9142860)
    var8 = i32_load(9142956)
    var2 = f32_load(40616)
    var9 = i32_load(9142868)
    i32_store(var1 + 12, i32_load8_u(9163792))
    var3 = float(var0)
    var3 = (((float(var0) - ((var2 * var3) / var4)) * 0.5) + ((var2 * float(((var9 & 0xFFFFFFFF) >> 1))) + float(var8)))
    if (1 if abs((((float(var0) - ((var2 * var3) / var4)) * 0.5) + ((var2 * float(((var9 & 0xFFFFFFFF) >> 1))) + float(var8)))) < 2147483650.0 else 0):
        break
    i32_store(int(var3) + 8, (-2147483648 // 32))
    var3 = float(var5)
    var2 = (((var2 * float(((var7 & 0xFFFFFFFF) >> 1))) + float(var6)) + ((float(var5) - ((var2 * var3) / var4)) * 0.5))
    if (1 if abs((((var2 * float(((var7 & 0xFFFFFFFF) >> 1))) + float(var6)) + ((float(var5) - ((var2 * var3) / var4)) * 0.5))) < 2147483650.0 else 0):
        break
    i32_store(int(var2) + 4, (-2147483648 // 32))
    func71(37, 0, 0, (var1 + 4), 3, 0)
    i32_store(9684392, (i32_load(9684392) + 1))
    global global0
    global0 = (var1 + 16)
    return var1

