"""
Auto-generated from WAT. Contains 4 functions.
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
# $Ua
# Export: Ua
# ==========================================================
def Ua(var0, var1, var2, var3):
    """Export: Ua"""
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var6 = i32_load(9142848)
    var8 = (i32_load(9142848) + ((var0 & 0xFFFFFFFF) // 25))
    var4 = i32_load(9215892)
    if (1 if var0 < 25 else 0):
        break
    if (1 if var4 < 5 else 0):
        break
    var7 = i32_load(9215884)
    var0 = 4
    while True:  # loop $label2
        var5 = (var7 + (var0 << 2))
        if (1 if i32_load((var7 + (var0 << 2))) < var6 else 0):
            break
        var0 = (var0 + 4)
        if (1 if (var0 + 4) < var4 else 0):
            continue
        break  # end loop
    if (1 if i32_load(9215888) != var4 else 0):
        var5 = i32_load(9215884)
        break
    var0 = (i32_load(9215896) + var4)
    i32_store(9215888, (i32_load(9215896) + var4))
    var6 = i32_load(9215884)
    var5 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var4:
        # Unknown: memory.copy []
    if var6:
        var4 = i32_load(9215892)
    i32_store(9215884, var5)
    i32_store(9215892, (var4 + 1))
    i32_store((var5 + (var4 << 2)), var8)
    var0 = i32_load(9215892)
    if (1 if i32_load(9215892) != i32_load(9215888) else 0):
        var4 = var5
        break
    var4 = (i32_load(9215896) + var0)
    i32_store(9215888, (i32_load(9215896) + var0))
    var4 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(9215884, var4)
    var0 = i32_load(9215892)
    i32_store(9215892, (var0 + 1))
    i32_store((var4 + (var0 << 2)), var1)
    var0 = i32_load(9215892)
    if (1 if i32_load(9215892) != i32_load(9215888) else 0):
        var5 = var4
        break
    var1 = (i32_load(9215896) + var0)
    i32_store(9215888, (i32_load(9215896) + var0))
    var5 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(9215884, var5)
    var0 = i32_load(9215892)
    i32_store(9215892, (var0 + 1))
    i32_store((var5 + (var0 << 2)), var2)
    var0 = i32_load(9215892)
    if (1 if i32_load(9215892) != i32_load(9215888) else 0):
        var4 = var5
        break
    var1 = (i32_load(9215896) + var0)
    i32_store(9215888, (i32_load(9215896) + var0))
    var4 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(9215884, var4)
    var0 = i32_load(9215892)
    i32_store(9215892, (var0 + 1))
    i32_store((var4 + (var0 << 2)), var3)
    return (i32_load(9215892) - 4)
    i32_store(var5, var8)
    var5 = (var0 << 2)
    i32_store((var7 + ((var0 << 2) | 4)), var1)
    i32_store((var7 + (var5 | 8)), var2)
    i32_store((var7 + (var5 | 12)), var3)
    return var0


# ==========================================================
# $func38
# ==========================================================
def func38(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var3 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if (1 if var0 >= 1073741823 else 0):
        var5 = (var0 - 1073741823)
        var1 = i32_load(9299896)
        if (1 if i32_load(9299896) != i32_load(9299892) else 0):
            var2 = i32_load(9299888)
            break
        var2 = (i32_load(9299900) + var1)
        i32_store(9299892, (i32_load(9299900) + var1))
        var4 = i32_load(9299888)
        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        if var1:
            # Unknown: memory.copy []
        if var4:
            var1 = i32_load(9299896)
        i32_store(9299888, var2)
        i32_store(9299896, (var1 + 1))
        i32_store((var2 + (var1 << 2)), var5)
        break
    var1 = i32_load(9299880)
    if (1 if i32_load(9299880) != i32_load(9299876) else 0):
        var2 = i32_load(9299872)
        break
    var2 = (i32_load(9299884) + var1)
    i32_store(9299876, (i32_load(9299884) + var1))
    var4 = i32_load(9299872)
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var1:
        # Unknown: memory.copy []
    if var4:
        var1 = i32_load(9299880)
    i32_store(9299872, var2)
    i32_store(9299880, (var1 + 1))
    i32_store((var2 + (var1 << 2)), var0)
    if i32_load8_u(9142916):
        i32_store(var3 + 32, var0)
        a_b()
        break
    i32_store(var3 + 24, var0)
    i64_store(var3 + 16, -4602115869219225600)
    i64_store(var3 + 8, 0)
    i64_store(var3, 0)
    a_b()
    global global0
    global0 = (var3 + 48)


# ==========================================================
# $func41
# ==========================================================
def func41(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var8 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var5 = i32_load8_u(9147125)
    if (1 if (i32_load8_u(9142388) if i32_load8_u(9147125) else 0) == 0 else 0):
        var7 = ((var2 + var4) + 5)
        var6 = func26((-1 if (1 if var7 > 1073741823 else 0) else (((var2 + var4) + 5) << 2)))
        i32_store(func26((-1 if (1 if var7 > 1073741823 else 0) else (((var2 + var4) + 5) << 2))) + 16, var4)
        i32_store(var6 + 12, var2)
        i32_store(var6 + 8, var0)
        i64_store(var6, 0)
        if var2:
            # Unknown: memory.copy []
        if var4:
            # Unknown: memory.copy []
        if (1 if var5 == 0 else 0):
            i32_store(var8 + 4, var7)
            i32_store(var8, var6)
            break
        var1 = i32_load((9142892 if i32_load8_u(9147212) else 41092))
        if (1 if i32_load((9142892 if i32_load8_u(9147212) else 41092)) >= 2 else 0):
            var0 = i32_load(9561692)
            var5 = 1
            while True:  # loop $label1
                var2 = i32_load((var0 + (var5 * 286704)) + 284616)
                if i32_load((var0 + (var5 * 286704)) + 284616):
                    i32_store(var8 + 24, var2)
                    i32_store(var8 + 20, var7)
                    i32_store(var8 + 16, var6)
                    var0 = i32_load(9561692)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var1 else 0):
                    continue
                break  # end loop
        break
    if i32_load8_u(9140304):
        break
    var9 = i32_load(9142384)
    var5 = i32_load(9561704)
    if (1 if i32_load(9561704) != i32_load(9561700) else 0):
        var6 = i32_load(9561696)
        break
    var6 = (i32_load(9561708) + var5)
    i32_store(9561700, (i32_load(9561708) + var5))
    var7 = i32_load(9561696)
    var6 = func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2)))
    if var5:
        # Unknown: memory.copy []
    if var7:
        var5 = i32_load(9561704)
    i32_store(9561696, var6)
    i32_store(9561704, (var5 + 1))
    i32_store((var6 + (var5 << 2)), var9)
    var5 = i32_load(9561704)
    if (1 if i32_load(9561704) != i32_load(9561700) else 0):
        var7 = var6
        break
    var7 = (i32_load(9561708) + var5)
    i32_store(9561700, (i32_load(9561708) + var5))
    var7 = func26((-1 if (1 if var7 > 1073741823 else 0) else (var7 << 2)))
    if var5:
        # Unknown: memory.copy []
    i32_store(9561696, var7)
    var5 = i32_load(9561704)
    i32_store(9561704, (var5 + 1))
    i32_store((var7 + (var5 << 2)), var0)
    var5 = i32_load(9561704)
    if (1 if i32_load(9561704) != i32_load(9561700) else 0):
        var6 = var7
        break
    var0 = (i32_load(9561708) + var5)
    i32_store(9561700, (i32_load(9561708) + var5))
    var6 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var5:
        # Unknown: memory.copy []
    i32_store(9561696, var6)
    var5 = i32_load(9561704)
    i32_store(9561704, (var5 + 1))
    i32_store((var6 + (var5 << 2)), var2)
    var5 = i32_load(9561704)
    if (1 if i32_load(9561704) != i32_load(9561700) else 0):
        var0 = var6
        break
    var0 = (i32_load(9561708) + var5)
    i32_store(9561700, (i32_load(9561708) + var5))
    var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var5:
        # Unknown: memory.copy []
    i32_store(9561696, var0)
    var5 = i32_load(9561704)
    i32_store(9561704, (var5 + 1))
    i32_store((var0 + (var5 << 2)), var4)
    if var2:
        var6 = 0
        while True:  # loop $label6
            var9 = i32_load((var1 + (var6 << 2)))
            var5 = i32_load(9561704)
            if (1 if i32_load(9561704) == i32_load(9561700) else 0):
                var7 = (i32_load(9561708) + var5)
                i32_store(9561700, (i32_load(9561708) + var5))
                var7 = func26((-1 if (1 if var7 > 1073741823 else 0) else (var7 << 2)))
                if var5:
                    # Unknown: memory.copy []
                i32_store(9561696, var7)
                var5 = i32_load(9561704)
                var0 = var7
            i32_store(9561704, (var5 + 1))
            i32_store((var0 + (var5 << 2)), var9)
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != var2 else 0):
                continue
            break  # end loop
    if (1 if var4 == 0 else 0):
        break
    var6 = 0
    while True:  # loop $label7
        var2 = i32_load((var3 + (var6 << 2)))
        var5 = i32_load(9561704)
        if (1 if i32_load(9561704) == i32_load(9561700) else 0):
            var1 = (i32_load(9561708) + var5)
            i32_store(9561700, (i32_load(9561708) + var5))
            var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
            if var5:
                # Unknown: memory.copy []
            i32_store(9561696, var1)
            var5 = i32_load(9561704)
            var0 = var1
        i32_store(9561704, (var5 + 1))
        i32_store((var0 + (var5 << 2)), var2)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) != var4 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var8 + 32)


# ==========================================================
# $func80
# ==========================================================
def func80(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var7 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if i32_load8_u(9142917):
        break
    var5 = i32_load(9299880)
    if i32_load(9299880):
        var5 = (var5 - 1)
        i32_store(9299880, (var5 - 1))
        var5 = i32_load((i32_load(9299872) + (var5 << 2)))
        break
    var5 = i32_load(9163776)
    var6 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var9 = i32_load(9163784)
    if (1 if var6 < i32_load(9163784) else 0):
        break
    i32_store(var7, var9)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    if (1 if var2 == 0 else 0):
        break
    var6 = i32_load(var2 + 16)
    var2 = i32_load(var2 + 24)
    if (1 if i32_load(var2 + 24) >= 100 else 0):
        var0 = f32_load((((var2 + var6) << 2) + 32700))
        if (1 if ((1 if f32_load((((var2 + var6) << 2) + 32700)) < 4294967300.0 else 0) & (1 if var0 >= 0.0 else 0)) == 0 else 0):
            break
        var8 = int(var0)
        break
    var8 = ((var6 * 1000) // var2)
    global global0
    global0 = (var7 + 16)

