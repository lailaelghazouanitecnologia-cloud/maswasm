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
# $func78
# ==========================================================
def func78(var0, var1, var2, var3):
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
    var15 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var11 = i32_load16_u(var0 + 110)
    if (1 if i32_load16_u(var0 + 110) == var1 else 0):
        break
    var12 = i32_load8_u(var0 + 122)
    var5 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) == 2 else 0):
        break
    if (1 if i32_load(var5 + 188) != 55 else 0):
        if (1 if i32_load(38528) != var12 else 0):
            break
    var10 = i32_load8_u(var0 + 125)
    if (1 if i32_load8_u(var0 + 125) == 3 else 0):
        break
    var4 = ((var12 * 404) + 9568096)
    var16 = i32_load(((var12 * 404) + 9568096) + 176)
    var13 = i32_load(9561692)
    var14 = (i32_load(9561692) + (var11 * 286704))
    var9 = i32_load(var4 + 280)
    var6 = (i32_load(var14 + 283976) - i32_load(var4 + 280))
    i32_store((i32_load(9561692) + (var11 * 286704)) + 283976, (i32_load(var14 + 283976) - i32_load(var4 + 280)))
    i32_store(var14 + 283980, (i32_load(var14 + 283980) - var16))
    if (1 if ((1 if (var9 - 1) < 0 else 0) & (1 if var16 < -2147483647 else 0)) == 0 else 0):
        i32_store8(var14 + 286700, 1)
    var4 = ((var13 + (var11 * 286704)) + 281748)
    if (1 if var6 > i32_load(((var13 + (var11 * 286704)) + 281748)) else 0):
        i32_store(var4, var6)
    # br_table ['$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label1', '$label2']
    _br_idx = (var10 - 4)
    break  # br_table
    var5 = (((var13 + (var11 * 286704)) + (var12 << 2)) + 282828)
    i32_store((((var13 + (var11 * 286704)) + (var12 << 2)) + 282828), (i32_load(var5) - 1))
    break
    var4 = (((var13 + (var11 * 286704)) + (var12 << 2)) + 281808)
    var4 = (i32_load(var4) - 1)
    i32_store((((var13 + (var11 * 286704)) + (var12 << 2)) + 281808), (i32_load(var4) - 1))
    if var4:
        break
    if (1 if i32_load(var14 + 283908) != i32_load(9142872) else 0):
        break
    if (1 if i32_load(var5 + 244) == 0 else 0):
        break
    while True:  # loop $label8
        var10 = i32_load((i32_load(var5 + 240) + (var7 << 2)))
        if i32_load8_u(9147141):
            break
        var8 = 0
        var4 = i32_load(9671120)
        if (1 if i32_load(9671120) == 0 else 0):
            break
        while True:  # loop $label7
            var6 = i32_load(((var8 << 2) + 9263072))
            if (1 if i32_load(((var8 << 2) + 9263072)) == 0 else 0):
                break
            if (1 if i32_load(var6 + 12) != var10 else 0):
                break
            if i32_load8_u(var6 + 24):
                break
            break
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != var4 else 0):
                continue
            break  # end loop
        var7 = (var7 + 1)
        if (1 if (var7 + 1) < i32_load(var5 + 244) else 0):
            continue
        break  # end loop
    var5 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        break
    if (1 if i32_load(var5 + 8) == 0 else 0):
        break
    func157(var0)
    var5 = i32_load(9215884)
    var4 = i32_load(var0 + 44)
    # br_table ['$label10', '$label9', '$label9', '$label10', '$label9']
    _br_idx = (i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) - 2)
    break  # br_table
    if var4:
        i32_store((var5 + (var4 << 4)), 0)
    i32_store(var0 + 44, 0)
    var8 = i32_load((var13 + (var11 * 286704)) + 281796)
    if (1 if i32_load((var13 + (var11 * 286704)) + 281796) == 0 else 0):
        break
    var7 = i32_load(var8 + 8)
    if (1 if i32_load(var8 + 8) == 0 else 0):
        break
    var6 = i32_load(var8)
    var5 = 0
    var10 = (var13 + (var11 * 286704))
    while True:  # loop $label14
        var4 = (var6 + (var5 << 2))
        if (1 if i32_load((var6 + (var5 << 2))) == i32_load(var0 + 28) else 0):
            var4 = ((var10 + (i32_load(var4 + 4) << 2)) + 282828)
            i32_store(((var10 + (i32_load(var4 + 4) << 2)) + 282828), (i32_load(var4) - 1))
            var7 = (i32_load(var8 + 8) - 1)
            i32_store(var8 + 8, (i32_load(var8 + 8) - 1))
            var4 = var5
            if (1 if var5 < var7 else 0):
                while True:  # loop $label12
                    var4 = (var4 + 1)
                    i32_store((var6 + (var4 << 2)), i32_load((var6 + ((var4 + 1) << 2))))
                    var7 = i32_load(var8 + 8)
                    if (1 if var4 < i32_load(var8 + 8) else 0):
                        continue
                    break  # end loop
            var7 = (var7 - 1)
            i32_store(var8 + 8, (var7 - 1))
            var4 = var5
            if (1 if var5 < var7 else 0):
                while True:  # loop $label13
                    var4 = (var4 + 1)
                    i32_store((var6 + (var4 << 2)), i32_load((var6 + ((var4 + 1) << 2))))
                    var7 = i32_load(var8 + 8)
                    if (1 if var4 < i32_load(var8 + 8) else 0):
                        continue
                    break  # end loop
            var5 = (var5 - 2)
        var5 = (var5 + 2)
        if (1 if (var5 + 2) < var7 else 0):
            continue
        break  # end loop
    i32_store16(var0 + 110, var1)
    var7 = i32_load(9561692)
    var8 = i32_load16_u(var0 + 110)
    var6 = (i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704))
    var5 = (i32_load(var6 + 283976) + var9)
    i32_store((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 283976, (i32_load(var6 + 283976) + var9))
    i32_store(var6 + 283980, (i32_load(var6 + 283980) + var16))
    if (1 if ((1 if var16 <= 0 else 0) & (1 if var9 >= 0 else 0)) == 0 else 0):
        i32_store8((var7 + (var8 * 286704)) + 286700, 1)
    var1 = ((var7 + (var8 * 286704)) + 281748)
    if (1 if var5 > i32_load(((var7 + (var8 * 286704)) + 281748)) else 0):
        i32_store(var1, var5)
    var4 = i32_load(var0 + 28)
    var1 = i32_load((((var13 + (var11 * 286704)) + (i32_load8_u(var0 + 122) << 2)) + 284636))
    if (1 if i32_load((((var13 + (var11 * 286704)) + (i32_load8_u(var0 + 122) << 2)) + 284636)) == 0 else 0):
        break
    var10 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    var5 = i32_load(var1)
    var9 = 0
    while True:  # loop $label16
        var1 = (var5 + (var9 << 2))
        if (1 if var4 != i32_load((var5 + (var9 << 2))) else 0):
            var9 = (var9 + 1)
            if (1 if (var9 + 1) != var10 else 0):
                continue
            break
        break  # end loop
    if (1 if var9 < 0 else 0):
        break
    i32_store(var1, 0)
    var4 = i32_load(var0 + 28)
    func144(var6, var4, 1)
    if i32_load(9147132):
        var1 = (var13 + (var11 * 286704))
        if i32_load((var13 + (var11 * 286704)) + 283908):
            i32_store(var1 + 283956, (i32_load(var1 + 283956) + i32_load(((var12 * 404) + 9568096) + 68)))
        var1 = (var7 + (var8 * 286704))
        i32_store((var7 + (var8 * 286704)) + 283956, (i32_load(var1 + 283956) - i32_load(((var12 * 404) + 9568096) + 68)))
    if (1 if i32_load8_u(9142916) == 0 else 0):
        break
    var4 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    var5 = i32_load8_u(var0 + 122)
    var1 = i32_load16_u(var0 + 110)
    i32_store(var15 + 4, var4)
    i32_store(var15, (var5 | (var1 << 16)))
    a_b()
    # br_table ['$label18', '$label19', '$label19', '$label19', '$label19', '$label19', '$label19', '$label19', '$label19', '$label19', '$label18', '$label19']
    _br_idx = (i32_load8_u(var0 + 125) - 4)
    break  # br_table
    var1 = (((var7 + (var8 * 286704)) + (i32_load8_u(var0 + 122) << 2)) + 282828)
    i32_store((((var7 + (var8 * 286704)) + (i32_load8_u(var0 + 122) << 2)) + 282828), (i32_load(var1) + 1))
    break
    var5 = (var7 + (var8 * 286704))
    var1 = (((var7 + (var8 * 286704)) + (i32_load8_u(var0 + 122) << 2)) + 281808)
    var1 = i32_load(var1)
    i32_store((((var7 + (var8 * 286704)) + (i32_load8_u(var0 + 122) << 2)) + 281808), (i32_load(var1) + 1))
    if var1:
        break
    if (1 if i32_load(var5 + 283908) != i32_load(9142872) else 0):
        break
    var6 = ((var12 * 404) + 9568096)
    if (1 if i32_load(((var12 * 404) + 9568096) + 244) == 0 else 0):
        break
    var5 = 0
    while True:  # loop $label24
        var4 = i32_load((i32_load(var6 + 240) + (var5 << 2)))
        if i32_load8_u(9147141):
            break
        var9 = 0
        var1 = i32_load(9671120)
        if (1 if i32_load(9671120) == 0 else 0):
            break
        while True:  # loop $label23
            var10 = i32_load(((var9 << 2) + 9263072))
            if (1 if i32_load(((var9 << 2) + 9263072)) == 0 else 0):
                break
            if (1 if i32_load(var10 + 12) != var4 else 0):
                break
            if i32_load8_u(var10 + 24):
                break
            break
            var9 = (var9 + 1)
            if (1 if (var9 + 1) != var1 else 0):
                continue
            break  # end loop
        var5 = (var5 + 1)
        if (1 if (var5 + 1) < i32_load(var6 + 244) else 0):
            continue
        break  # end loop
    if var3:
    func77(var0)
    if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 20):
    func387(var14)
    if (1 if var2 == 0 else 0):
        break
    var1 = i32_load(var0 + 44)
    if (1 if i32_load(var0 + 44) == 0 else 0):
        break
    if i32_load((i32_load(9215884) + (var1 << 4)) + 4):
        break
    i32_store8(var0 + 123, 0)
    i32_store(var0 + 32, 0)
    i32_store(var0 + 116, i32_load(var0 + 112))
    break
    func29(var0, 1)
    global global0
    global0 = (var15 + 16)


# ==========================================================
# $func85
# ==========================================================
def func85(var0, var1, param2):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    i32_store8(var0 + 125, 1)
    var4 = i32_load(9142840)
    var6 = i32_load16_u(var0 + 112)
    var8 = i32_load16_u(var0 + 114)
    var2 = (i32_load(9142440) + 2)
    var3 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    if (1 if i32_load((i32_load(9142840) + ((i32_load16_u(var0 + 112) + (((i32_load16_u(var0 + 114) + ((i32_load(9142440) + 2) * i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 208))) + 1) * var2)) << 2)) + 4) != i32_load(var3 + 212) else 0):
        break
    if (1 if i32_load(var3 + 216) == 0 else 0):
        break
    while True:  # loop $label2
        var5 = (var5 + 1)
        var9 = ((var5 + 1) + var6)
        var2 = 0
        while True:  # loop $label1
            var2 = (var2 + 1)
            var7 = (i32_load(9142440) + 2)
            i32_store((var4 + ((var9 + ((((var2 + 1) + var8) + ((i32_load(9142440) + 2) * i32_load(var3 + 208))) * var7)) << 2)), i32_load(var0 + 28))
            var7 = i32_load(var3 + 216)
            if (1 if var2 < i32_load(var3 + 216) else 0):
                continue
            break  # end loop
        if (1 if var5 < var7 else 0):
            continue
        break  # end loop
    func92(var0, 0.0, 0.0)
    if i32_load8_u(9142916):
    var2 = i32_load8_u(var0 + 123)
    if (1 if i32_load8_u(var0 + 123) == 0 else 0):
        break
    if (1 if var1 == 0 else 0):
        break
    var1 = i32_load(var0 + 96)
    if i32_load(var0 + 96):
        var3 = i32_load(9671128)
        var2 = (i32_load(9671128) + (var1 * 132))
        if (1 if i32_load((i32_load(9671128) + (var1 * 132)) + 36) != i32_load(var0 + 28) else 0):
            break
        if (1 if i32_load8_u(var2 + 125) == 3 else 0):
            break
        var1 = (var3 + (var1 * 132))
        if i32_load(((i32_load8_u((var3 + (var1 * 132)) + 122) * 404) + 9568096) + 268):
            var1 = i32_load(var1 + 52)
            i32_store(var1 + 52, (i32_load(var1 + 52) - 1))
            if (1 if var1 >= 2 else 0):
                break
        break
        func29(var0, 0)
        return func32(func60(var0, 1.0), var2, 0)
    var3 = i32_load(9561692)
    var5 = i32_load16_u(var0 + 110)
    var1 = (i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704))
    var4 = ((var2 * 40) + 9671200)
    if (1 if i32_load8_u(((var2 * 40) + 9671200) + 18) == 0 else 0):
        break
    var6 = (i32_load(var1 + 283976) + 1)
    if (1 if (i32_load(var1 + 283976) + 1) > (i32_load((var1 + 284136)) + i32_load(var1 + 283980)) else 0):
        var2 = 57101
        if (1 if i32_load((var3 + (var5 * 286704)) + 283908) == i32_load(9142872) else 0):
            break
        break
    var3 = (var3 + (var5 * 286704))
    if (1 if var6 <= i32_load(((var3 + (var5 * 286704)) + 284000)) else 0):
        break
    var2 = 57113
    if (1 if i32_load(var3 + 283908) != i32_load(9142872) else 0):
        break
    a_b()
    break
    var3 = i32_load(var4 + 12)
    if i32_load(var4 + 12):
        if func66(var1, var3, 1, 1):
            break
    else:
    var2 = i32_load(((var2 * 40) + 9671200) + 8)
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = 1
    if (1 if var2 == 0 else 0):
        break
    var5 = i32_load(var0 + 72)
    var4 = (i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704))
    var2 = i32_load((((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + (var2 << 2)) + 283984))
    if (1 if i32_load(var0 + 72) < i32_load((((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + (var2 << 2)) + 283984)) else 0):
        if (1 if var2 <= i32_load(var0 + 76) else 0):
            break
        i32_store8(var0 + 127, 1)
        var2 = i32_load(var0 + 40)
        if (1 if i32_load(var0 + 40) == 0 else 0):
            break
        if (1 if i32_load8_u(9142916) == 0 else 0):
            break
        i32_store(var1 + 4, var2)
        i32_store(var1, -16776961)
        a_b()
        var2 = i32_load(var0 + 44)
        if i32_load(var0 + 44):
            i32_store((i32_load(9215884) + (var2 << 4)), 0)
        i32_store8(var0 + 125, 8)
        var3 = 0
        i32_store(var0 + 44, 0)
        break
    var4 = (var4 + 281668)
    i32_store((var4 + 281668), (i32_load(var4) + var2))
    i32_store(var0 + 72, (var5 - var2))
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
            break
    global global0
    global0 = (var1 + 16)
    if (1 if var3 == 0 else 0):
        break
    # call_indirect via table[i32_load(((i32_load8_u(var0 + 123) * 40) + 9671200) + 20)]
    if (1 if i32_load8_u(var0 + 125) == 10 else 0):
        break
    if (1 if i32_load8_u(var0 + 123) == 63 else 0):
        break
    i32_store8(var0 + 125, 0)
    return call_indirect(i32_load(((i32_load8_u(var0 + 123) * 40) + 9671200) + 20))
    var1 = i32_load(((var2 * 40) + 9671200) + 36)
    if i32_load(((var2 * 40) + 9671200) + 36):
        # call_indirect via table[var1]
        if call_indirect(var1):
            break
    func29(var0, 1)
    return i32_load(var0 + 28)
    func29(var0, 1)
    return i32_load(var0 + 32)

