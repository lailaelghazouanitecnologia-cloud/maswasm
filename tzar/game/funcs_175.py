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
# $func160
# ==========================================================
def func160(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var3 = i32_load8_u(59181)
    var8 = i32_load16_u(var0 + 114)
    var9 = i32_load16_u(var0 + 112)
    if i32_load8_u(9147152):
        var4 = i32_load8_u(var0 + 125)
        break
    var4 = i32_load(9142872)
    if (1 if i32_load(9142872) == 0 else 0):
        break
    if (1 if i32_load8_u((i32_load(9143012) + (i32_load16_u(var0 + 110) + (i32_load(9142892) * var4)))) == 0 else 0):
        break
    var4 = i32_load8_u(var0 + 125)
    if (1 if i32_load8_u(var0 + 125) == 3 else 0):
        break
    var7 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var5 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 220)
    var0 = ((var8 - (var2 if var3 else 0)) + ((i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1))
    var3 = i32_load(var7 + 216)
    var8 = ((var9 - (var1 if var3 else 0)) + ((i32_load(var7 + 216) & 0xFFFFFFFF) >> 1))
    # br_table ['$label2', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label2', '$label3']
    _br_idx = (var4 - 4)
    break  # br_table
    break
    var7 = i32_load(var7 + 200)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    var10 = (((var1 + (var2 * 3)) + 4) << 2)
    var3 = i32_load(9142836)
    var4 = ((((var1 + (var2 * 3)) + 4) << 2) + (i32_load(9142836) + (var7 * 80)))
    var11 = i32_load(((((var1 + (var2 * 3)) + 4) << 2) + (i32_load(9142836) + (var7 * 80))) + 44)
    if i32_load(((((var1 + (var2 * 3)) + 4) << 2) + (i32_load(9142836) + (var7 * 80))) + 44):
        var5 = i32_load(var4 + 8)
        var4 = i32_load(9142440)
        var3 = 0
        while True:  # loop $label7
            var6 = (var3 << 2)
            var9 = (i32_load((var5 + ((var3 << 2) | 4))) + var0)
            if (1 if var4 <= (i32_load((var5 + ((var3 << 2) | 4))) + var0) else 0):
                break
            var6 = (i32_load((var5 + var6)) + var8)
            if (1 if var4 <= (i32_load((var5 + var6)) + var8) else 0):
                break
            if (1 if (var6 | var9) < 0 else 0):
                break
            var4 = i32_load(9142440)
            var3 = (var3 + 2)
            if (1 if (var3 + 2) < var11 else 0):
                continue
            break  # end loop
        var3 = i32_load(9142836)
    var3 = ((var3 + ((var7 + 4) * 80)) + var10)
    var10 = i32_load(((var3 + ((var7 + 4) * 80)) + var10) + 44)
    if i32_load(((var3 + ((var7 + 4) * 80)) + var10) + 44):
        var5 = i32_load(var3 + 8)
        var4 = i32_load(9142440)
        var3 = 0
        while True:  # loop $label9
            var6 = (var3 << 2)
            var9 = (i32_load((var5 + ((var3 << 2) | 4))) + var0)
            if (1 if var4 <= (i32_load((var5 + ((var3 << 2) | 4))) + var0) else 0):
                break
            var6 = (i32_load((var5 + var6)) + var8)
            if (1 if var4 <= (i32_load((var5 + var6)) + var8) else 0):
                break
            if (1 if (var6 | var9) < 0 else 0):
                break
            func258(var6, var9)
            var4 = i32_load(9142440)
            var3 = (var3 + 2)
            if (1 if (var3 + 2) < var10 else 0):
                continue
            break  # end loop
    if (1 if i32_load(i32_load(9142424) + 48) == 1 else 0):
        break
    var3 = ((i32_load(9142836) + (var7 * 80)) + ((((1 - var2) * 3) - var1) << 2))
    var7 = i32_load(((i32_load(9142836) + (var7 * 80)) + ((((1 - var2) * 3) - var1) << 2)) + 48)
    if (1 if i32_load(((i32_load(9142836) + (var7 * 80)) + ((((1 - var2) * 3) - var1) << 2)) + 48) == 0 else 0):
        break
    var5 = (var0 + var2)
    var8 = (var1 + var8)
    var0 = i32_load(var3 + 12)
    var4 = i32_load(9142440)
    var3 = 0
    while True:  # loop $label11
        var2 = (var3 << 2)
        var1 = (var5 + i32_load((var0 + ((var3 << 2) | 4))))
        if (1 if var4 <= (var5 + i32_load((var0 + ((var3 << 2) | 4)))) else 0):
            break
        var2 = (var8 + i32_load((var0 + var2)))
        if (1 if var4 <= (var8 + i32_load((var0 + var2))) else 0):
            break
        if (1 if (var1 | var2) < 0 else 0):
            break
        var4 = i32_load(9142440)
        var3 = (var3 + 2)
        if (1 if (var3 + 2) < var7 else 0):
            continue
        break  # end loop
    return func129(var2, var1, 0)


# ==========================================================
# $func414
# ==========================================================
def func414(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var5 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    if (1 if var2 == 0 else 0):
        break
    if (1 if var2 == var3 else 0):
        break
    var6 = i32_load(9142892)
    if (1 if i32_load(9142892) <= var2 else 0):
        break
    var10 = (var4 ^ 1)
    var11 = ((var4 ^ 1) & (1 if var1 != 0 else 0))
    if ((var4 ^ 1) & (1 if var1 != 0 else 0)):
        if i32_load8_u((i32_load(9143004) + ((var2 * var6) + var3))):
            break
    var7 = i32_load8_u(9147210)
    var9 = (var10 & (1 if i32_load8_u(9147210) == 0 else 0))
    if (var10 & (1 if i32_load8_u(9147210) == 0 else 0)):
        var8 = (1 if i32_load(9142872) == var3 else 0)
    # br_table ['$label1', '$label2', '$label3', '$label0']
    _br_idx = (var0 - 1)
    break  # br_table
    if i32_load(9147132):
        break
    if (1 if var7 == 0 else 0):
        break
    if (1 if var4 == 0 else 0):
        break
    var0 = ((var2 * var6) + var3)
    var6 = (((var2 * var6) + var3) + i32_load(9143012))
    if (1 if i32_load8_u((((var2 * var6) + var3) + i32_load(9143012))) == var1 else 0):
        break
    if var1:
        i32_store8(var6, 1)
    if (1 if var2 == i32_load(9142872) else 0):
        func374(var3, var1)
    if (1 if var1 == 0 else 0):
        i32_store8((i32_load(9143012) + var0), 0)
    if (1 if i32_load(9142872) != var2 else 0):
        break
    a_b()
    var6 = (918 if var1 else 919)
    if (1 if var2 == i32_load(9142872) else 0):
        var0 = (i32_load(9561692) + (var3 * 286704))
        var9 = i32_load((i32_load(9561692) + (var3 * 286704)) + 284628)
        var7 = i32_load(var0 + 284616)
        i32_store(var5 + 48, var6)
        i32_store(var5 + 52, var0)
        i32_store(var5 + 56, (var7 if var7 else var9))
        a_b()
    if (1 if var8 == 0 else 0):
        break
    while True:  # loop $label8
        var0 = var3
        if (1 if var3 == 0 else 0):
            break
        if (1 if var0 == var2 else 0):
            break
        var3 = i32_load(9142892)
        if (1 if i32_load(9142892) <= var0 else 0):
            break
        if var11:
            if i32_load8_u((i32_load(9143004) + ((var0 * var3) + var2))):
                break
        var7 = i32_load8_u(9147210)
        if ((1 if i32_load8_u(9147210) == 0 else 0) & var10):
            var8 = (1 if i32_load(9142872) == var2 else 0)
            break
        var8 = 0
        if i32_load(9147132):
            break
        if (1 if var7 == 0 else 0):
            break
        if (1 if var4 == 0 else 0):
            break
        var3 = ((var0 * var3) + var2)
        var7 = (((var0 * var3) + var2) + i32_load(9143012))
        if (1 if i32_load8_u((((var0 * var3) + var2) + i32_load(9143012))) == var1 else 0):
            break
        if var1:
            i32_store8(var7, 1)
        if (1 if var0 == i32_load(9142872) else 0):
            func374(var2, var1)
        if (1 if var1 == 0 else 0):
            i32_store8((i32_load(9143012) + var3), 0)
        if (1 if i32_load(9142872) != var0 else 0):
            break
        a_b()
        if (1 if var0 == i32_load(9142872) else 0):
            var3 = (i32_load(9561692) + (var2 * 286704))
            var9 = i32_load((i32_load(9561692) + (var2 * 286704)) + 284628)
            var7 = i32_load(var3 + 284616)
            i32_store(var5 + 32, var6)
            i32_store(var5 + 36, var3)
            i32_store(var5 + 40, (var7 if var7 else var9))
            a_b()
        var3 = var2
        var2 = var0
        if var8:
            continue
        break  # end loop
    break
    var0 = i32_load(9143008)
    var4 = (i32_load(9143008) + ((var3 * var6) + var2))
    if (1 if i32_load8_u((i32_load(9143008) + ((var3 * var6) + var2))) == var1 else 0):
        break
    if i32_load(9147132):
        if (1 if i32_load(9142440) == 4096 else 0):
            break
    var4 = (1 if var1 != 0 else 0)
    i32_store8(var4, (1 if var1 != 0 else 0))
    if var8:
        i32_store8((var0 + ((var2 * var6) + var3)), var4)
    if (1 if i32_load(9142872) != var2 else 0):
        break
    var0 = (i32_load(9561692) + (var3 * 286704))
    var3 = i32_load((i32_load(9561692) + (var3 * 286704)) + 284628)
    var2 = i32_load(var0 + 284616)
    i32_store(var5 + 16, (450 if var1 else 532))
    i32_store(var5 + 20, var0)
    i32_store(var5 + 24, (var2 if var2 else var3))
    a_b()
    break
    var0 = (i32_load(9143016) + ((var3 * var6) + var2))
    if (1 if i32_load8_u((i32_load(9143016) + ((var3 * var6) + var2))) == var1 else 0):
        break
    var4 = i32_load(9142424)
    if i32_load(i32_load(9142424) + 180):
        if (1 if i32_load(9142848) < (i32_load(var4 + 72) * 2400) else 0):
            break
    if i32_load(9147132):
        if (1 if i32_load(9142440) == 4096 else 0):
            break
    i32_store8(var0, var1)
    if (var9 & (1 if var1 != 0 else 0)):
        var0 = (i32_load(9143016) + ((var2 * var6) + var3))
        i32_store8((i32_load(9143016) + ((var2 * var6) + var3)), (i32_load8_u(var0) | var1))
    var0 = i32_load(9561692)
    i32_store8((i32_load(9561692) + (var2 * 286704)) + 286701, 1)
    if (1 if i32_load(9142872) != var2 else 0):
        break
    var0 = (var0 + (var3 * 286704))
    var3 = i32_load((var0 + (var3 * 286704)) + 284628)
    var2 = i32_load(var0 + 284616)
    i32_store(var5 + 4, var0)
    i32_store(var5, var1)
    i32_store(var5 + 8, (var2 if var2 else var3))
    a_b()
    global global0
    global0 = (var5 - -64)

