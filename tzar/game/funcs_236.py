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
# $func654
# ==========================================================
def func654(var0, var1):
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
    var12 = 0
    var13 = 0
    var14 = 0
    var15 = 0
    var16 = 0
    var17 = 0
    var18 = 0
    var19 = 0
    var5 = i32_load(9671128)
    var8 = (i32_load(9671128) + (var0 * 132))
    var9 = (var5 + (var1 * 132))
    var2 = i32_load8_u((var5 + (var1 * 132)) + 122)
    if (1 if i32_load8_u(9216060) == 0 else 0):
        break
    if (1 if i32_load(39064) != var2 else 0):
        break
    var12 = (var5 + (var1 * 132))
    var2 = i32_load(9561692)
    var13 = (var5 + (var0 * 132))
    var6 = i32_load16_u((var5 + (var0 * 132)) + 110)
    var1 = (i32_load(9561692) + (i32_load16_u((var5 + (var0 * 132)) + 110) * 286704))
    var3 = i32_load((i32_load(9561692) + (i32_load16_u((var5 + (var0 * 132)) + 110) * 286704)) + 283848)
    if (1 if i32_load((i32_load(9561692) + (i32_load16_u((var5 + (var0 * 132)) + 110) * 286704)) + 283848) == 2147483647 else 0):
        break
    i32_store((var1 + 283848), (i32_load(var12 + 52) + var3))
    var3 = 1
    i32_store8(var1 + 286701, 1)
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var10 = (var4 - 1)
    var14 = ((var4 - 1) & 1)
    var6 = (i32_load((var2 + (var6 * 286704)) + 283908) * var4)
    var2 = 0
    var7 = i32_load(9561692)
    var11 = i32_load(9143016)
    if (1 if var4 != 2 else 0):
        var4 = (var10 & -2)
        while True:  # loop $label2
            if i32_load8_u((var11 + (var3 + var6))):
                i32_store8((var7 + (var3 * 286704)) + 286701, 1)
            var10 = (var3 + 1)
            if i32_load8_u((var11 + ((var3 + 1) + var6))):
                i32_store8((var7 + (var10 * 286704)) + 286701, 1)
            var3 = (var3 + 2)
            var2 = (var2 + 2)
            if (1 if (var2 + 2) != var4 else 0):
                continue
            break  # end loop
    if (1 if var14 == 0 else 0):
        break
    if (1 if i32_load8_u((var11 + (var3 + var6))) == 0 else 0):
        break
    i32_store8((var7 + (var3 * 286704)) + 286701, 1)
    var1 = (var1 + 281640)
    i32_store((var1 + 281640), (i32_load(var1) + i32_load(var12 + 52)))
    if i32_load8_u(9142917):
        break
    if (1 if i32_load(9142872) != i32_load16_u(var13 + 110) else 0):
        break
    a_b()
    var0 = (var5 + (var0 * 132))
    i32_store8((var5 + (var0 * 132)) + 125, 0)
    var6 = i32_load(9142440)
    var12 = (i32_load(9142440) + 2)
    var13 = i32_load8_u(var9 + 122)
    var10 = ((i32_load(9142440) + 2) * i32_load(((i32_load8_u(var9 + 122) * 404) + 9568096) + 208))
    var7 = i32_load16_u(var0 + 112)
    var14 = (i32_load16_u(var0 + 112) + 12)
    var11 = i32_load16_u(var0 + 114)
    var16 = (i32_load16_u(var0 + 114) + 12)
    var9 = (var11 - 12)
    var2 = (var7 - 12)
    var17 = i32_load(9671128)
    var18 = i32_load(9142840)
    var4 = 2147483647
    var0 = 0
    while True:  # loop $label6
        var5 = (var2 + 1)
        if (1 if var2 < var6 else 0):
            var1 = (var7 - var2)
            var19 = ((var7 - var2) * var1)
            var1 = var9
            while True:  # loop $label5
                var3 = var1
                if (1 if var6 <= var1 else 0):
                    break
                if (1 if (var2 | var3) < 0 else 0):
                    break
                var1 = (var11 - var3)
                var15 = (((var11 - var3) * var1) + var19)
                if (1 if (((var11 - var3) * var1) + var19) >= var4 else 0):
                    break
                var1 = i32_load((var18 + (((((var3 + var10) + 1) * var12) + var5) << 2)))
                if (1 if i32_load((var18 + (((((var3 + var10) + 1) * var12) + var5) << 2))) == 0 else 0):
                    break
                var15 = (1 if i32_load8_u((var17 + (var1 * 132)) + 122) == var13 else 0)
                var4 = (var15 if (1 if i32_load8_u((var17 + (var1 * 132)) + 122) == var13 else 0) else var4)
                var0 = (var1 if var15 else var0)
                var1 = (var3 + 1)
                if (1 if var3 != var16 else 0):
                    continue
                break  # end loop
        var1 = (1 if var2 != var14 else 0)
        var2 = var5
        if var1:
            continue
        break  # end loop
    if var0:
        return 1064
    func29(var8, 1)
    return 54546
    var6 = ((var2 * 404) + 9568096)
    if (1 if i32_load(((var2 * 404) + 9568096) + 268) != 3 else 0):
        break
    var3 = (var5 + (var0 * 132))
    var4 = i32_load8_u((var5 + (var0 * 132)) + 122)
    # br_table ['$label8', '$label7', '$label7', '$label7', '$label7', '$label7', '$label7', '$label7', '$label7', '$label7', '$label7', '$label7', '$label7', '$label7', '$label7', '$label8', '$label9']
    _br_idx = (i32_load8_u((var5 + (var0 * 132)) + 122) + -64)
    break  # br_table
    if (1 if var4 != 10 else 0):
        break
    var6 = (var5 + (var1 * 132))
    i32_store16(var3 + 108, i32_load((var5 + (var1 * 132)) + 52))
    var4 = (var5 + (var0 * 132))
    if (1 if i32_load8_u(var6 + 125) != 10 else 0):
    else:
    i32_store(i32_load(((var2 * 404) + 9568096) + 188) + 88, (3 + (var2 << 16)))
    var1 = (var5 + (var1 * 132))
    func207(var8, i32_load((var5 + (var1 * 132)) + 28))
    i32_store8(var4 + 125, 0)
    var5 = ((i32_load8_u(var9 + 122) * 404) + 9568096)
    if i32_load(((i32_load8_u(var9 + 122) * 404) + 9568096) + 216):
        var7 = i32_load16_u(var1 + 114)
        var11 = i32_load16_u(var1 + 112)
        var12 = i32_load(9142840)
        var2 = 0
        while True:  # loop $label11
            var2 = (var2 + 1)
            var13 = ((var2 + 1) + var11)
            var3 = 0
            while True:  # loop $label10
                var3 = (var3 + 1)
                var10 = (i32_load(9142440) + 2)
                i32_store((var12 + ((var13 + ((((var3 + 1) + var7) + ((i32_load(9142440) + 2) * i32_load(var5 + 208))) * var10)) << 2)), i32_load(var5 + 212))
                var10 = i32_load(var5 + 216)
                if (1 if var3 < i32_load(var5 + 216) else 0):
                    continue
                break  # end loop
            if (1 if var2 < var10 else 0):
                continue
            break  # end loop
    func138(var9)
    i32_store(var1 + 36, var0)
    if (1 if i32_load8_u(var6 + 125) != 10 else 0):
    else:
    var0 = func166(i32_load16_u(var4 + 114), i32_load16_u(var4 + 110), i32_load(((i32_load8_u(var9 + 122) * 404) + 9568096) + 188), 3)
    if func166(i32_load16_u(var4 + 114), i32_load16_u(var4 + 110), i32_load(((i32_load8_u(var9 + 122) * 404) + 9568096) + 188), 3):
        return (var5 + (var0 * 132))
    func29(var8, 1)
    return func32(0  # stack underflow, var9, 1)
    if (1 if func297(var8, var1) == 0 else 0):
        break
    var4 = ((i32_load8_u(var9 + 122) * 404) + 9568096)
    if i32_load(((i32_load8_u(var9 + 122) * 404) + 9568096) + 216):
        var2 = (var5 + (var1 * 132))
        var7 = i32_load16_u((var5 + (var1 * 132)) + 114)
        var11 = i32_load16_u(var2 + 112)
        var12 = i32_load(9142840)
        var2 = 0
        while True:  # loop $label14
            var2 = (var2 + 1)
            var13 = ((var2 + 1) + var11)
            var3 = 0
            while True:  # loop $label13
                var3 = (var3 + 1)
                var10 = (i32_load(9142440) + 2)
                i32_store((var12 + ((var13 + ((((var3 + 1) + var7) + ((i32_load(9142440) + 2) * i32_load(var4 + 208))) * var10)) << 2)), i32_load(var4 + 212))
                var10 = i32_load(var4 + 216)
                if (1 if var3 < i32_load(var4 + 216) else 0):
                    continue
                break  # end loop
            if (1 if var2 < var10 else 0):
                continue
            break  # end loop
    func138(var9)
    var2 = (var5 + (var1 * 132))
    i32_store((var5 + (var1 * 132)) + 36, var0)
    if (1 if i32_load(var6 + 268) == 2 else 0):
        var1 = (var5 + (var0 * 132))
        i32_store((var5 + (var0 * 132)) + 52, (i32_load(var1 + 52) + i32_load(var2 + 52)))
        i32_store(var1 + 60, (i32_load(var1 + 60) + i32_load(var2 + 60)))
    var2 = 0
    var9 = 0
    var6 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = i32_load(var8 + 24)
    if (1 if i32_load(var8 + 24) == 0 else 0):
        var3 = func26(16)
        i64_store(func26(16), 0)
        i64_store(var3 + 8, 0)
        i32_store(var8 + 24, var3)
    var1 = i32_load(var3 + 4)
    if (1 if i32_load(var3 + 4) == 0 else 0):
        var1 = func26(16)
        i32_store(func26(16) + 4, 2)
        i32_store(var1, func26(8))
        i64_store(var1 + 8, 8589934592)
        i32_store(var3 + 4, var1)
        break
    var4 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    var7 = i32_load(var1)
    while True:  # loop $label17
        if (1 if i32_load((var7 + (var2 << 2))) == 0 else 0):
            break
        var2 = (var2 + 2)
        if (1 if (var2 + 2) < var4 else 0):
            continue
        break  # end loop
    if (1 if i32_load(var8 + 40) == 0 else 0):
        break
    if i32_load8_u(9142917):
        break
    var2 = i32_load(9299880)
    if i32_load(9299880):
        var2 = (var2 - 1)
        i32_store(9299880, (var2 - 1))
        var9 = i32_load((i32_load(9299872) + (var2 << 2)))
        break
    var9 = i32_load(9163776)
    var2 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var4 = i32_load(9163784)
    if (1 if var2 < i32_load(9163784) else 0):
        break
    i32_store(var6, var4)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    var3 = i32_load(var8 + 24)
    var1 = i32_load(i32_load(var8 + 24) + 4)
    var2 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) != i32_load(var1 + 4) else 0):
        var4 = i32_load(var1)
        break
    var4 = (i32_load(var1 + 12) + var2)
    i32_store(var1 + 4, (i32_load(var1 + 12) + var2))
    var7 = i32_load(var1)
    var4 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
    if var2:
        # Unknown: memory.copy []
    if var7:
        var3 = i32_load(var8 + 24)
        var2 = i32_load(var1 + 8)
    i32_store(var1, var4)
    var3 = i32_load(var3 + 4)
    i32_store(var1 + 8, (var2 + 1))
    i32_store((var4 + (var2 << 2)), 0)
    var1 = i32_load(var3 + 8)
    if (1 if i32_load(var3 + 8) != i32_load(var3 + 4) else 0):
        var2 = i32_load(var3)
        break
    var2 = (i32_load(var3 + 12) + var1)
    i32_store(var3 + 4, (i32_load(var3 + 12) + var1))
    var4 = i32_load(var3)
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var1:
        # Unknown: memory.copy []
    if var4:
        var1 = i32_load(var3 + 8)
    i32_store(var3, var2)
    i32_store(var3 + 8, (var1 + 1))
    i32_store((var2 + (var1 << 2)), var9)
    if (1 if i32_load(var8 + 40) == 0 else 0):
        break
    var1 = (i32_load16_u(var8 + 114) << 5)
    global global0
    global0 = (var6 + 16)
    if (1 if i32_load((var5 + (var0 * 132)) + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var5 + (var0 * 132)) + 28) else 0):
            break
    if (1 if i32_load8_u(9147141) == 0 else 0):
        break
    if (1 if i32_load(9173808) != i32_load((var5 + (var0 * 132)) + 28) else 0):
        break
    Ya(1)
    func29(var8, 1)
    return func28(1, 1)

