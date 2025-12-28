"""
Auto-generated from WAT. Contains 7 functions.
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
# $func66
# ==========================================================
def func66(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var6 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    if (1 if var2 == 0 else 0):
        break
    if (1 if i32_load(var0 + 283908) != i32_load(9142872) else 0):
        break
    var2 = i32_load(var1)
    if (1 if i32_load(var1) == 0 else 0):
        break
    if (1 if i32_load(var6 + 64) >= var2 else 0):
        break
    i32_store(var6 + 48, 0)
    a_b()
    var2 = i32_load(var1 + 4)
    if (1 if i32_load(var1 + 4) == 0 else 0):
        break
    if (1 if i32_load(var6 + 68) >= var2 else 0):
        break
    i32_store(var6 + 32, 1)
    a_b()
    var2 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    if (1 if i32_load(var6 + 72) >= var2 else 0):
        break
    i32_store(var6 + 16, 2)
    a_b()
    var2 = i32_load(var1 + 12)
    if (1 if i32_load(var1 + 12) == 0 else 0):
        break
    if (1 if i32_load(var6 + 76) >= var2 else 0):
        break
    i32_store(var6, 3)
    a_b()
    var2 = 1
    var4 = i32_load(var1)
    if i32_load(var1):
        if (1 if i32_load(var6 + 64) < var4 else 0):
            break
    var5 = i32_load(var1 + 4)
    if i32_load(var1 + 4):
        if (1 if i32_load(var6 + 68) < var5 else 0):
            break
    var5 = i32_load(var1 + 8)
    if i32_load(var1 + 8):
        if (1 if i32_load(var6 + 72) < var5 else 0):
            break
    var5 = i32_load(var1 + 12)
    if i32_load(var1 + 12):
        if (1 if i32_load(var6 + 76) < var5 else 0):
            break
    var10 = i32_load(9143016)
    if (1 if i32_load(var6 + 64) == 2147483647 else 0):
        break
    if (1 if var4 == 0 else 0):
        break
    if var3:
        var2 = (var0 + 281692)
        i32_store((var0 + 281692), (i32_load(var2) + var4))
        var4 = i32_load(var1)
    var2 = i32_load(var0 + 283848)
    var5 = (var4 - i32_load(var0 + 283848))
    if (1 if (var4 - i32_load(var0 + 283848)) <= 0 else 0):
        i32_store(var0 + 283848, (var2 - var4))
        break
    i32_store(var0 + 283848, 0)
    var2 = (var0 + 281708)
    i32_store((var0 + 281708), (i32_load(var2) + var5))
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var7 = i32_load(9561692)
    var2 = 1
    while True:  # loop $label7
        if (i32_load8_u((var10 + (i32_load(var0 + 283908) + (var2 * var4)))) & 1):
            var8 = (var7 + (var2 * 286704))
            var9 = ((var7 + (var2 * 286704)) + 283848)
            var4 = i32_load(var8 + 283848)
            if (1 if var5 <= i32_load(var8 + 283848) else 0):
                break
            var8 = (var8 + 281724)
            i32_store((var8 + 281724), (i32_load(var8) + var4))
            i32_store(var9, 0)
            var5 = (var5 - var4)
            var4 = i32_load(9142892)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var4 else 0):
            continue
        break
        break  # end loop
    i32_store(var9, (var4 - var5))
    var2 = ((var7 + (var2 * 286704)) + 281724)
    i32_store(((var7 + (var2 * 286704)) + 281724), (i32_load(var2) + var5))
    if (1 if i32_load(var6 + 68) == 2147483647 else 0):
        break
    var2 = i32_load(var1 + 4)
    if (1 if i32_load(var1 + 4) == 0 else 0):
        break
    if var3:
        var4 = (var0 + 281696)
        i32_store((var0 + 281696), (i32_load(var4) + var2))
        var2 = i32_load(var1 + 4)
    var4 = i32_load((var0 + 283852))
    var5 = (var2 - i32_load((var0 + 283852)))
    if (1 if (var2 - i32_load((var0 + 283852))) > 0 else 0):
        i32_store(var0 + 283852, 0)
        var2 = (var0 + 281712)
        i32_store((var0 + 281712), (i32_load(var2) + var5))
        var4 = i32_load(9142892)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var7 = i32_load(9561692)
        var2 = 1
        while True:  # loop $label9
            if (i32_load8_u((var10 + (i32_load(var0 + 283908) + (var2 * var4)))) & 2):
                var9 = (var7 + (var2 * 286704))
                var8 = ((var7 + (var2 * 286704)) + 283852)
                var4 = i32_load(((var7 + (var2 * 286704)) + 283852))
                if (1 if i32_load(((var7 + (var2 * 286704)) + 283852)) >= var5 else 0):
                    i32_store(var8, (var4 - var5))
                    var2 = ((var7 + (var2 * 286704)) + 281728)
                    i32_store(((var7 + (var2 * 286704)) + 281728), (i32_load(var2) + var5))
                    break
                var9 = (var9 + 281728)
                i32_store((var9 + 281728), (i32_load(var9) + var4))
                i32_store(var8, 0)
                var5 = (var5 - var4)
                var4 = i32_load(9142892)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < var4 else 0):
                continue
            break  # end loop
        break
    i32_store(var0 + 283852, (var4 - var2))
    if (1 if i32_load(var6 + 72) == 2147483647 else 0):
        break
    var2 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    if var3:
        var4 = (var0 + 281700)
        i32_store((var0 + 281700), (i32_load(var4) + var2))
        var2 = i32_load(var1 + 8)
    var4 = i32_load((var0 + 283856))
    var5 = (var2 - i32_load((var0 + 283856)))
    if (1 if (var2 - i32_load((var0 + 283856))) > 0 else 0):
        i32_store(var0 + 283856, 0)
        var2 = (var0 + 281716)
        i32_store((var0 + 281716), (i32_load(var2) + var5))
        var4 = i32_load(9142892)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var7 = i32_load(9561692)
        var2 = 1
        while True:  # loop $label11
            if (i32_load8_u((var10 + (i32_load(var0 + 283908) + (var2 * var4)))) & 4):
                var9 = (var7 + (var2 * 286704))
                var8 = ((var7 + (var2 * 286704)) + 283856)
                var4 = i32_load(((var7 + (var2 * 286704)) + 283856))
                if (1 if i32_load(((var7 + (var2 * 286704)) + 283856)) >= var5 else 0):
                    i32_store(var8, (var4 - var5))
                    var2 = ((var7 + (var2 * 286704)) + 281732)
                    i32_store(((var7 + (var2 * 286704)) + 281732), (i32_load(var2) + var5))
                    break
                var9 = (var9 + 281732)
                i32_store((var9 + 281732), (i32_load(var9) + var4))
                i32_store(var8, 0)
                var5 = (var5 - var4)
                var4 = i32_load(9142892)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < var4 else 0):
                continue
            break  # end loop
        break
    i32_store(var0 + 283856, (var4 - var2))
    var2 = 0
    if (1 if i32_load(var6 + 76) == 2147483647 else 0):
        break
    var4 = i32_load(var1 + 12)
    if (1 if i32_load(var1 + 12) == 0 else 0):
        break
    if var3:
        var3 = (var0 + 281704)
        i32_store((var0 + 281704), (i32_load(var3) + var4))
        var4 = i32_load(var1 + 12)
    var1 = i32_load((var0 + 283860))
    var3 = (var4 - i32_load((var0 + 283860)))
    if (1 if (var4 - i32_load((var0 + 283860))) > 0 else 0):
        i32_store(var0 + 283860, 0)
        var1 = (var0 + 281720)
        i32_store((var0 + 281720), (i32_load(var1) + var3))
        var4 = i32_load(9142892)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var5 = i32_load(9561692)
        var1 = 1
        while True:  # loop $label12
            if (i32_load8_u((var10 + (i32_load(var0 + 283908) + (var1 * var4)))) & 8):
                var7 = (var5 + (var1 * 286704))
                var4 = ((var5 + (var1 * 286704)) + 283860)
                var2 = i32_load(((var5 + (var1 * 286704)) + 283860))
                if (1 if i32_load(((var5 + (var1 * 286704)) + 283860)) >= var3 else 0):
                    i32_store(var4, (var2 - var3))
                    var0 = ((var5 + (var1 * 286704)) + 281736)
                    i32_store(((var5 + (var1 * 286704)) + 281736), (i32_load(var0) + var3))
                    var2 = 0
                    break
                var7 = (var7 + 281736)
                i32_store((var7 + 281736), (i32_load(var7) + var2))
                i32_store(var4, 0)
                var4 = i32_load(9142892)
                var3 = (var3 - var2)
            var2 = 0
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < var4 else 0):
                continue
            break  # end loop
        break
    i32_store(var0 + 283860, (var1 - var4))
    global global0
    global0 = (var6 + 80)
    return var2


# ==========================================================
# $func82
# ==========================================================
def func82(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    if (1 if var1 <= 0 else 0):
        break
    var6 = (var0 - -64)
    while True:  # loop $label3
        if (1 if i32_load(var6) < i32_load(var0 + 56) else 0):
            if (1 if i32_load(var0 + 24) <= 0 else 0):
                break
        if i32_load(var0 + 4):
            i64_store(var0 + 76, rotl64(i64_load(var0 + 76), 32))
        if (1 if i32_load(var0 + 60) >= i32_load(var0 + 48) else 0):
            a_c()
            raise RuntimeError('unreachable')
        # call_indirect via table[i32_load((9687804 if i32_load(var0) else 9687800))]
        if i32_load(var0 + 4):
            break
        if (1 if (i32_load(var0 + 52) * i32_load(var0 + 8)) <= 0 else 0):
            break
        var7 = i32_load(var0 + 76)
        var8 = i32_load(var0 + 80)
        var4 = 0
        while True:  # loop $label2
            var9 = (var4 << 2)
            var10 = (var7 + (var4 << 2))
            i32_store((var7 + (var4 << 2)), (i32_load(var10) + i32_load((var8 + var9))))
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < (i32_load(var0 + 52) * i32_load(var0 + 8)) else 0):
                continue
            break  # end loop
        i32_store(var0 + 60, (i32_load(var0 + 60) + 1))
        i32_store(var0 + 24, (i32_load(var0 + 24) - i32_load(var0 + 32)))
        var2 = (var2 + var3)
        var5 = (var5 + 1)
        if (1 if (var5 + 1) != var1 else 0):
            continue
        break  # end loop
    var5 = var1
    return var5


# ==========================================================
# $func91
# ==========================================================
def func91(var0, param1):
    var1 = 0
    var2 = 0
    var3 = 0
    if (1 if i32_load(var0 + 24) <= 0 else 0):
        var2 = i32_load(var0 + 56)
        if (1 if i32_load(var0 + 56) <= i32_load((var0 - -64)) else 0):
            break
        var1 = 9687808
        if i32_load(var0 + 4):
            break
        var1 = 9687812
        if i32_load(var0 + 20):
            break
        if (1 if i32_load(var0 + 48) != var2 else 0):
            break
        if (1 if i32_load(var0 + 36) != 1 else 0):
            break
        if (1 if i32_load(var0 + 44) != 1 else 0):
            break
        var1 = i32_load(var0 + 52)
        if (1 if i32_load(var0 + 52) > 2 else 0):
            break
        if (1 if (var1 * i32_load(var0 + 8)) <= 0 else 0):
            break
        var2 = i32_load(var0 + 76)
        var1 = 0
        while True:  # loop $label5
            var3 = (var1 << 2)
            i32_store8((i32_load(var0 + 68) + var1), i32_load((var2 + (var1 << 2))))
            var2 = i32_load(var0 + 76)
            i32_store((i32_load(var0 + 76) + var3), 0)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < (i32_load(var0 + 52) * i32_load(var0 + 8)) else 0):
                continue
            break  # end loop
        break
        # call_indirect via table[i32_load(var1)]
        i32_store(var0 + 24, (i32_load(var0 + 24) + i32_load(var0 + 28)))
        i32_store(var0 + 68, (i32_load(var0 + 68) + i32_load(var0 + 72)))
        var0 = (var0 - -64)
        i32_store((var0 - -64), (i32_load(var0) + 1))
    return
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func99
# ==========================================================
def func99(var0, var1, var2):
    if (1 if var1 == 5 else 0):
        if (1 if i32_load(var0 + 48) == 0 else 0):
            break
    if (1 if i32_load(var0) == 0 else 0):
        i32_store(var0 + 8, var2)
        i32_store(var0, var1)
        i32_store(var0 + 4, 0)
    return 0
    a_c()
    raise RuntimeError('unreachable')
    return 3476


# ==========================================================
# $func123
# ==========================================================
def func123(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    # br_table ['$label0', '$label1', '$label2']
    _br_idx = i32_load(var0 + 4)
    break  # br_table
    func299(var0, var1)
    return
    var3 = i32_load(var0 + 88)
    if (1 if i32_load(var0 + 88) == 0 else 0):
        break
    var4 = i32_load(9671128)
    while True:  # loop $label4
        var5 = (var4 + (i32_load((i32_load(var0 + 80) + (var2 << 2))) * 132))
        if (1 if i32_load8_u((var4 + (i32_load((i32_load(var0 + 80) + (var2 << 2))) * 132)) + 125) != 3 else 0):
            # call_indirect via table[var1]
            var4 = i32_load(9671128)
            var3 = i32_load(var0 + 88)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var3 else 0):
            continue
        break  # end loop
    break
    var3 = i32_load(9140300)
    if (1 if i32_load(9140300) == 0 else 0):
        break
    var4 = i32_load(9142420)
    var5 = i32_load(9671128)
    while True:  # loop $label5
        var6 = (var5 + (i32_load(((var2 << 2) + 8451904)) * 132))
        if i32_load((var4 + (i32_load16_u((var5 + (i32_load(((var2 << 2) + 8451904)) * 132)) + 110) << 2))):
            # call_indirect via table[var1]
            var4 = i32_load(9142420)
            var5 = i32_load(9671128)
            var3 = i32_load(9140300)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var3 else 0):
            continue
        break  # end loop


# ==========================================================
# $func125
# ==========================================================
def func125(var0):
    var1 = 0
    var2 = 0
    var2 = ((var0 + 7) & -8)
    while True:  # loop $label1
        var0 = i32_atomic_load(52740)
        var1 = (i32_atomic_load(52740) + var2)
        if (var2 if (1 if (i32_atomic_load(52740) + var2) <= var0 else 0) else 0):
            break
        if (1 if var1 > (memory_size() << 16) else 0):
            if (1 if a_n(var1) == 0 else 0):
                break
        if (1 if var1 != var0 else 0):
            continue
        break  # end loop
    return var0
    i32_store((global3 + 28), 48)
    return -1


# ==========================================================
# $la
# Export: la
# ==========================================================
def la():
    """Export: la"""
    var0 = 0
    var1 = 0
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
    var0 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if (i32_load8_u(9216060) | i32_load8_u(9142917)):
        break
    a_b()
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var3 = 1
    while True:  # loop $label1
        var1 = (i32_load(9561692) + (var3 * 286704))
        var5 = i32_load8_u(((i32_load(9561692) + (var3 * 286704)) + 283973))
        var6 = i32_load8_u(var1 + 283972)
        var7 = i32_load(var1 + 284608)
        var8 = i32_load8_u(var1 + 286699)
        var9 = i32_load(var1 + 284628)
        var4 = i32_load(var1 + 284616)
        var2 = i32_load8_u((i32_load(9143004) + (i32_load(9142872) + (i32_load(var1 + 283908) * var2))))
        var10 = i32_load(var1 + 284604)
        var11 = i32_load8_u(var1 + 286696)
        i32_store(var0 + 16, i32_load8_u((var1 + 283974)))
        i32_store(var0 + 20, var11)
        i32_store(var0 + 24, var10)
        i32_store(var0 + 28, var2)
        i32_store(var0 + 32, (var4 if var4 else var9))
        i32_store(var0 + 36, var8)
        i32_store(var0 + 40, var7)
        i32_store(var0, var3)
        i32_store(var0 + 4, var1)
        i32_store(var0 + 8, var6)
        i32_store(var0 + 12, var5)
        a_b()
        var3 = (var3 + 1)
        var2 = i32_load(9142892)
        if (1 if (var3 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    global global0
    global0 = (var0 + 48)

