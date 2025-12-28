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
# $func183
# ==========================================================
def func183(var0, var1, var2, var3, var4, var5, var6, var7, var8):
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
    var20 = 0
    var21 = 0
    var22 = 0
    var13 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var9 = 1
    var20 = i32_load8_u(var0 + 125)
    if (1 if i32_load8_u(var0 + 125) == 3 else 0):
        break
    var9 = i32_load(((var1 + (var2 * 36)) + 269376))
    var9 = (i32_load(((var1 + (var2 * 36)) + 269376)) if var9 else 100)
    var12 = ((var2 * 404) + 9568096)
    i32_store(var13, (((i32_load(((var1 + (var2 * 36)) + 269376)) if var9 else 100) * i32_load(((var2 * 404) + 9568096) + 68)) // 100))
    i32_store(var13 + 4, ((i32_load(var12 + 72) * var9) // 100))
    i32_store(var13 + 8, ((i32_load(var12 + 76) * var9) // 100))
    i32_store(var13 + 12, ((i32_load(var12 + 80) * var9) // 100))
    if (1 if var3 == 0 else 0):
        if (1 if i32_load(var12 + 264) != 3 else 0):
            break
        if var5:
            break
        var9 = 0
        var3 = (var1 + (var2 << 2))
        if i32_load(((var1 + (var2 << 2)) + 282828)):
            break
        if i32_load((var3 + 281808)):
            break
        var7 = i32_load(var0 + 20)
        if (1 if i32_load(var0 + 20) == 0 else 0):
            var7 = func26(16)
            i32_store(func26(16) + 4, 16)
            i32_store(var7, func26(64))
            i64_store(var7 + 8, 68719476736)
            i32_store(var0 + 20, var7)
            break
        if (1 if var4 == 0 else 0):
            break
        if (1 if var6 == 0 else 0):
            break
        var3 = i32_load(var7 + 8)
        if (1 if i32_load(var7 + 8) == 0 else 0):
            break
        var11 = (var2 + 2147483647)
        var10 = i32_load(var7)
        var9 = 0
        var6 = 0
        while True:  # loop $label3
            if (1 if i32_load((var10 + (var6 << 2))) == var11 else 0):
                break
            var6 = (var6 + 1)
            if (1 if var3 != (var6 + 1) else 0):
                continue
            break  # end loop
        break
    var5 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        var9 = 0
        break
    var4 = i32_load(var5 + 8)
    if (1 if i32_load(var5 + 8) == 0 else 0):
        var8 = 0
        var11 = -1
        break
    var14 = (var4 & 1)
    var6 = i32_load(var5)
    if (1 if var4 == 1 else 0):
        var11 = -1
        var9 = 0
        var8 = 0
        break
    var16 = (var4 & -2)
    var11 = -1
    var9 = 0
    var8 = 0
    var4 = 0
    while True:  # loop $label6
        var15 = (var9 | 1)
        var10 = i32_load((var6 + ((var9 | 1) << 2)))
        var17 = (1 if i32_load((var6 + ((var9 | 1) << 2))) > 2147483646 else 0)
        var12 = i32_load((var6 + (var9 << 2)))
        var20 = (1 if i32_load((var6 + (var9 << 2))) > 2147483646 else 0)
        var12 = (1 if ((var12 - 2147483647) if var20 else var12) == var2 else 0)
        var10 = (1 if ((var10 - 2147483647) if var17 else var10) == var2 else 0)
        var8 = ((1 if i32_load((var6 + ((var9 | 1) << 2))) > 2147483646 else 0) if (1 if ((var10 - 2147483647) if var17 else var10) == var2 else 0) else ((1 if i32_load((var6 + (var9 << 2))) > 2147483646 else 0) if (1 if ((var12 - 2147483647) if var20 else var12) == var2 else 0) else var8))
        var11 = (var15 if var10 else (var9 if var12 else var11))
        var9 = (var9 + 2)
        var4 = (var4 + 2)
        if (1 if (var4 + 2) != var16 else 0):
            continue
        break  # end loop
    if (1 if var14 == 0 else 0):
        break
    var4 = i32_load((var6 + (var9 << 2)))
    var6 = (1 if i32_load((var6 + (var9 << 2))) > 2147483646 else 0)
    var4 = (1 if ((var4 - 2147483647) if var6 else var4) == var2 else 0)
    var8 = ((1 if i32_load((var6 + (var9 << 2))) > 2147483646 else 0) if (1 if ((var4 - 2147483647) if var6 else var4) == var2 else 0) else var8)
    var11 = (var9 if var4 else var11)
    var4 = i32_load(var1 + 281796)
    if (1 if i32_load(var1 + 281796) == 0 else 0):
        break
    var6 = i32_load(var4 + 8)
    if (1 if i32_load(var4 + 8) == 0 else 0):
        break
    var10 = i32_load(var0 + 28)
    var12 = i32_load(var4)
    var9 = 0
    while True:  # loop $label11
        var14 = (var9 << 2)
        if (1 if i32_load((var12 + (var9 << 2))) != var10 else 0):
            break
        if (1 if i32_load((var12 + (var14 | 4))) != var2 else 0):
            break
        var10 = (var6 - 1)
        i32_store(var4 + 8, (var6 - 1))
        if (1 if var9 < var10 else 0):
            var6 = var9
            while True:  # loop $label9
                var6 = (var6 + 1)
                i32_store((var12 + (var6 << 2)), i32_load((var12 + ((var6 + 1) << 2))))
                var10 = i32_load(var4 + 8)
                if (1 if var6 < i32_load(var4 + 8) else 0):
                    continue
                break  # end loop
        var6 = (var10 - 1)
        i32_store(var4 + 8, (var10 - 1))
        if (1 if var6 > var9 else 0):
            while True:  # loop $label10
                var9 = (var9 + 1)
                i32_store((var12 + (var9 << 2)), i32_load((var12 + ((var9 + 1) << 2))))
                if (1 if var9 < i32_load(var4 + 8) else 0):
                    continue
                break  # end loop
        var6 = ((var1 + (var2 << 2)) + 282828)
        i32_store(((var1 + (var2 << 2)) + 282828), (i32_load(var6) - 1))
        break
        var9 = (var9 + 2)
        if (1 if (var9 + 2) < var6 else 0):
            continue
        break  # end loop
    var14 = ((var2 * 404) + 9568096)
    if (1 if i32_load(((var2 * 404) + 9568096) + 264) != 3 else 0):
        break
    var6 = i32_load(var14 + 244)
    if (1 if i32_load(var14 + 244) == 0 else 0):
        break
    var17 = i32_load(((var2 * 404) + 9568096) + 240)
    var16 = 0
    while True:  # loop $label18
        if (1 if var4 == 0 else 0):
            break
        var10 = i32_load(var4 + 8)
        if (1 if i32_load(var4 + 8) == 0 else 0):
            break
        var15 = i32_load(((i32_load((var17 + (var16 << 2))) * 132) + 9216080) + 4)
        var20 = i32_load(var0 + 28)
        var12 = i32_load(var4)
        var9 = 0
        while True:  # loop $label17
            var18 = (var9 << 2)
            if (1 if i32_load((var12 + (var9 << 2))) != var20 else 0):
                break
            if (1 if i32_load((var12 + (var18 | 4))) != var15 else 0):
                break
            var10 = (var10 - 1)
            i32_store(var4 + 8, (var10 - 1))
            var6 = var9
            if (1 if var9 < var10 else 0):
                while True:  # loop $label15
                    var6 = (var6 + 1)
                    i32_store((var12 + (var6 << 2)), i32_load((var12 + ((var6 + 1) << 2))))
                    var10 = i32_load(var4 + 8)
                    if (1 if var6 < i32_load(var4 + 8) else 0):
                        continue
                    break  # end loop
            var6 = (var10 - 1)
            i32_store(var4 + 8, (var10 - 1))
            if (1 if var6 > var9 else 0):
                while True:  # loop $label16
                    var9 = (var9 + 1)
                    i32_store((var12 + (var9 << 2)), i32_load((var12 + ((var9 + 1) << 2))))
                    if (1 if var9 < i32_load(var4 + 8) else 0):
                        continue
                    break  # end loop
            var6 = ((var1 + (var15 << 2)) + 282828)
            i32_store(((var1 + (var15 << 2)) + 282828), (i32_load(var6) - 1))
            var6 = i32_load(var14 + 244)
            break
            var9 = (var9 + 2)
            if (1 if (var9 + 2) < var10 else 0):
                continue
            break  # end loop
        var16 = (var16 + 1)
        if (1 if (var16 + 1) < var6 else 0):
            continue
        break  # end loop
    if (1 if var11 == -1 else 0):
        break
    var4 = ((var1 + (var2 << 2)) + 282828)
    i32_store(((var1 + (var2 << 2)) + 282828), (i32_load(var4) - 1))
    var9 = i32_load(var5 + 8)
    if (1 if i32_load(var14 + 264) != 3 else 0):
        break
    var10 = 0
    if (1 if var9 == 0 else 0):
        var9 = 0
        break
    while True:  # loop $label24
        var4 = i32_load((i32_load(var5) + (var10 << 2)))
        var4 = ((i32_load((i32_load(var5) + (var10 << 2))) - 2147483647) if (1 if var4 > 2147483646 else 0) else var4)
        var6 = ((((i32_load((i32_load(var5) + (var10 << 2))) - 2147483647) if (1 if var4 > 2147483646 else 0) else var4) * 404) + 9568096)
        # br_table ['$label21', '$label22', '$label22', '$label21', '$label22']
        _br_idx = i32_load(((((i32_load((i32_load(var5) + (var10 << 2))) - 2147483647) if (1 if var4 > 2147483646 else 0) else var4) * 404) + 9568096) + 264)
        break  # br_table
        var9 = 0
        var6 = i32_load(var6 + 180)
        var12 = i32_load(i32_load(var6 + 180) + 68)
        if (1 if i32_load(i32_load(var6 + 180) + 68) == 0 else 0):
            break
        while True:  # loop $label23
            if (1 if var2 != i32_load((var6 + (var9 << 2)) + 28) else 0):
                var9 = (var9 + 1)
                if (1 if var12 != (var9 + 1) else 0):
                    continue
                break
            break  # end loop
        var10 = (var10 - 1)
        var5 = i32_load(var0 + 20)
        var10 = (var10 + 1)
        var9 = i32_load(var5 + 8)
        if (1 if (var10 + 1) < i32_load(var5 + 8) else 0):
            continue
        break  # end loop
    var6 = (var9 - 1)
    i32_store(var5 + 8, (var9 - 1))
    if (1 if var6 > var11 else 0):
        var3 = i32_load(var5)
        var9 = var11
        while True:  # loop $label25
            var9 = (var9 + 1)
            i32_store((var3 + (var9 << 2)), i32_load((var3 + ((var9 + 1) << 2))))
            var6 = i32_load(var5 + 8)
            if (1 if var9 < i32_load(var5 + 8) else 0):
                continue
            break  # end loop
    if (1 if var7 == 0 else 0):
        break
    # br_table ['$label26', '$label27', '$label27', '$label27', '$label27', '$label27', '$label27', '$label27', '$label27', '$label27', '$label26', '$label27']
    _br_idx = (i32_load8_u(var0 + 125) - 4)
    break  # br_table
    if var6:
        if var11:
            break
        func230(var0)
        break
    var3 = i32_load(var0 + 44)
    if i32_load(var0 + 44):
        i32_store((i32_load(9215884) + (var3 << 4)), 0)
    i32_store(var0 + 44, 0)
    func29(var0, 1)
    if var11:
        break
    if (1 if (var8 & 1) == 0 else 0):
        break
    # br_table ['$label19', '$label30', '$label30', '$label30', '$label30', '$label30', '$label30', '$label30', '$label30', '$label30', '$label19', '$label30']
    _br_idx = (i32_load8_u(var0 + 125) - 4)
    break  # br_table
    if (var8 & 1):
        break
    var3 = i32_load(var1 + 283848)
    if (1 if i32_load(var1 + 283848) != 2147483647 else 0):
        i32_store(var1 + 283848, (i32_load(var13) + var3))
    var3 = i32_load((var1 + 283852))
    if (1 if i32_load((var1 + 283852)) != 2147483647 else 0):
        i32_store(var1 + 283852, (i32_load(var13 + 4) + var3))
    var3 = i32_load((var1 + 283856))
    if (1 if i32_load((var1 + 283856)) != 2147483647 else 0):
        i32_store(var1 + 283856, (i32_load(var13 + 8) + var3))
    var3 = i32_load(var13 + 12)
    var4 = i32_load((var1 + 283860))
    if (1 if i32_load((var1 + 283860)) != 2147483647 else 0):
        i32_store(var1 + 283860, (var3 + var4))
    var4 = (var1 + 281692)
    i32_store((var1 + 281692), (i32_load(var4) - i32_load(var13)))
    var4 = (var1 + 281696)
    i32_store((var1 + 281696), (i32_load(var4) - i32_load(var13 + 4)))
    var4 = i32_load(var13 + 8)
    var5 = (var1 + 281704)
    i32_store((var1 + 281704), (i32_load(var5) - var3))
    var9 = 1
    i32_store8(var1 + 286701, 1)
    var3 = (var1 + 281700)
    i32_store((var1 + 281700), (i32_load(var3) - var4))
    var3 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var6 = (var3 - 1)
    var7 = ((var3 - 1) & 1)
    var1 = (i32_load(var1 + 283908) * var3)
    var4 = i32_load(9561692)
    var5 = i32_load(9143016)
    if (1 if var3 != 2 else 0):
        var3 = (var6 & -2)
        var10 = 0
        while True:  # loop $label31
            if i32_load8_u((var5 + (var1 + var9))):
                i32_store8((var4 + (var9 * 286704)) + 286701, 1)
            var6 = (var9 + 1)
            if i32_load8_u((var5 + ((var9 + 1) + var1))):
                i32_store8((var4 + (var6 * 286704)) + 286701, 1)
            var9 = (var9 + 2)
            var10 = (var10 + 2)
            if (1 if (var10 + 2) != var3 else 0):
                continue
            break  # end loop
    if (1 if var7 == 0 else 0):
        break
    if (1 if i32_load8_u((var5 + (var1 + var9))) == 0 else 0):
        break
    i32_store8((var4 + (var9 * 286704)) + 286701, 1)
    var1 = ((var2 * 404) + 9568096)
    if (1 if i32_load(var1 + 244) == 0 else 0):
        break
    var9 = 0
    while True:  # loop $label33
        var9 = (var9 + 1)
        if (1 if (var9 + 1) < i32_load(var1 + 244) else 0):
            continue
        break  # end loop
    break
    if var4:
        break
    var3 = i32_load(var7 + 8)
    if (1 if i32_load(var7 + 8) == 0 else 0):
        break
    var11 = (var2 + 2147483647)
    var10 = i32_load(var7)
    var9 = 0
    var6 = 0
    while True:  # loop $label35
        if (1 if i32_load((var10 + (var6 << 2))) == var11 else 0):
            break
        var6 = (var6 + 1)
        if (1 if (var6 + 1) != var3 else 0):
            continue
        break  # end loop
    var3 = i32_load(var1 + 281796)
    if (1 if i32_load(var1 + 281796) == 0 else 0):
        break
    if var5:
        break
    var6 = i32_load(var3 + 8)
    if (1 if i32_load(var3 + 8) == 0 else 0):
        break
    var11 = i32_load(var0 + 28)
    var3 = i32_load(var3)
    var9 = 0
    while True:  # loop $label38
        var10 = (var9 << 2)
        if (1 if i32_load((var3 + (var9 << 2))) != var11 else 0):
            break
        if (1 if i32_load((var3 + (var10 | 4))) != var2 else 0):
            break
        var9 = 0
        break
        var9 = (var9 + 2)
        if (1 if (var9 + 2) < var6 else 0):
            continue
        break  # end loop
    if (1 if var4 == 0 else 0):
        break
    if (1 if i32_load(var7 + 8) == 0 else 0):
        var10 = 0
        break
    var6 = (var7 + 8)
    var14 = ((var2 * 404) + 9568096)
    var18 = ((var1 + (var2 << 2)) + 282828)
    var3 = 0
    var11 = 0
    while True:  # loop $label47
        var7 = i32_load(var7)
        var9 = i32_load((i32_load(var7) + (var3 << 2)))
        if (1 if ((i32_load((i32_load(var7) + (var3 << 2))) - 2147483647) if (1 if var9 > 2147483646 else 0) else var9) != var2 else 0):
            break
        if (1 if var3 == 0 else 0):
            i32_store(var7, (i32_load(var7) + 2147483647))
            if (1 if i32_load(var0 + 92) == 0 else 0):
                break
            var3 = i32_load8_u(9147141)
            if i32_load(9140316):
                if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
                    break
            var3 = 0
            var9 = 0
            if (1 if i32_load(var14 + 244) == 0 else 0):
                var11 = 1
                break
            while True:  # loop $label43
                var11 = 1
                var9 = (var9 + 1)
                if (1 if (var9 + 1) < i32_load(var14 + 244) else 0):
                    continue
                break  # end loop
            break
        var9 = i32_load(var1 + 283848)
        if (1 if i32_load(var1 + 283848) != 2147483647 else 0):
            i32_store(var1 + 283848, (i32_load(var13) + var9))
        var9 = i32_load(var1 + 283852)
        if (1 if i32_load(var1 + 283852) != 2147483647 else 0):
            i32_store(var1 + 283852, (i32_load(var13 + 4) + var9))
        var9 = i32_load(var1 + 283856)
        if (1 if i32_load(var1 + 283856) != 2147483647 else 0):
            i32_store(var1 + 283856, (i32_load(var13 + 8) + var9))
        var9 = i32_load(var13 + 12)
        var10 = i32_load(var1 + 283860)
        if (1 if i32_load(var1 + 283860) != 2147483647 else 0):
            i32_store(var1 + 283860, (var9 + var10))
        i32_store(var1 + 281692, (i32_load(var1 + 281692) - i32_load(var13)))
        i32_store(var1 + 281696, (i32_load(var1 + 281696) - i32_load(var13 + 4)))
        var10 = i32_load(var13 + 8)
        i32_store(var1 + 281704, (i32_load(var1 + 281704) - var9))
        i32_store8(var1 + 286701, 1)
        i32_store(var1 + 281700, (i32_load(var1 + 281700) - var10))
        var10 = i32_load(9142892)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var9 = 1
        var19 = (var10 - 1)
        var21 = ((var10 - 1) & 1)
        var16 = (i32_load(var1 + 283908) * var10)
        var15 = i32_load(9561692)
        var17 = i32_load(9143016)
        if (1 if var10 != 2 else 0):
            var19 = (var19 & -2)
            var10 = 0
            while True:  # loop $label45
                if i32_load8_u((var17 + (var9 + var16))):
                    i32_store8((var15 + (var9 * 286704)) + 286701, 1)
                var22 = (var9 + 1)
                if i32_load8_u((var17 + ((var9 + 1) + var16))):
                    i32_store8((var15 + (var22 * 286704)) + 286701, 1)
                var9 = (var9 + 2)
                var10 = (var10 + 2)
                if (1 if (var10 + 2) != var19 else 0):
                    continue
                break  # end loop
        if (1 if var21 == 0 else 0):
            break
        if (1 if i32_load8_u((var17 + (var9 + var16))) == 0 else 0):
            break
        i32_store8((var15 + (var9 * 286704)) + 286701, 1)
        var10 = (i32_load(var6) - 1)
        i32_store(var6, (i32_load(var6) - 1))
        var9 = var3
        if (1 if var10 > var3 else 0):
            while True:  # loop $label46
                var9 = (var9 + 1)
                i32_store((var7 + (var9 << 2)), i32_load((var7 + ((var9 + 1) << 2))))
                if (1 if var9 < i32_load(var6) else 0):
                    continue
                break  # end loop
        i32_store(var18, (i32_load(var18) - 1))
        var3 = (var3 - 1)
        var7 = i32_load(var0 + 20)
        var6 = (i32_load(var0 + 20) + 8)
        var3 = (var3 + 1)
        var10 = i32_load(var7 + 8)
        if (1 if (var3 + 1) < i32_load(var7 + 8) else 0):
            continue
        break  # end loop
    var9 = 1
    if (var11 & 1):
        break
    if var10:
        break
    # br_table ['$label48', '$label39', '$label39', '$label39', '$label39', '$label39', '$label39', '$label39', '$label39', '$label39', '$label48', '$label39']
    _br_idx = (var20 - 4)
    break  # br_table
    var3 = (var4 ^ 1)
    if (1 if func66(var1, var13, (var4 ^ 1), 1) == 0 else 0):
        break
    if (1 if (var3 | var5) == 0 else 0):
        func181(var1, i32_load(var0 + 28), var2)
        var1 = ((var1 + (var2 << 2)) + 282828)
        i32_store(((var1 + (var2 << 2)) + 282828), (i32_load(var1) + 1))
    var9 = 0
    func294(var0)
    var0 = ((var2 * 404) + 9568096)
    if (1 if i32_load(var0 + 244) == 0 else 0):
        break
    var7 = 0
    while True:  # loop $label49
        var7 = (var7 + 1)
        if (1 if (var7 + 1) < i32_load(var0 + 244) else 0):
            continue
        break  # end loop
    break
    if (1 if var8 == 0 else 0):
        break
    var9 = 0
    var6 = 0
    var10 = 0
    var14 = 0
    var16 = i32_load16_u(var0 + 110)
    var15 = i32_load(9561692)
    var8 = i32_load(((var2 * 404) + 9568096) + 180)
    if (1 if i32_load8_u(i32_load(((var2 * 404) + 9568096) + 180) + 23) == 0 else 0):
        break
    var3 = i32_load(var8 + 4)
    if (1 if i32_load(((i32_load(var8 + 4) * 404) + 9568096) + 264) != 3 else 0):
        break
    if (1 if i32_load((((var15 + (var16 * 286704)) + (var3 << 2)) + 281808)) == 0 else 0):
        break
    var11 = i32_load(var8 + 68)
    break
    var7 = 1
    var11 = i32_load(var8 + 68)
    if (1 if i32_load(var8 + 68) == 0 else 0):
        break
    var18 = (var15 + (var16 * 286704))
    var3 = 1
    while True:  # loop $label56
        var19 = i32_load((var8 + (var6 << 2)) + 28)
        var7 = i32_load(((i32_load((var8 + (var6 << 2)) + 28) * 404) + 9568096) + 264)
        var17 = (1 if i32_load(((i32_load((var8 + (var6 << 2)) + 28) * 404) + 9568096) + 264) == 1 else 0)
        var19 = i32_load(((var18 + (var19 << 2)) + 281808))
        if (1 if i32_load(((var18 + (var19 << 2)) + 281808)) == 1 else 0):
            break
        var3 = ((1 if var7 != 3 else 0) & var3)
        if var19:
            break
        var3 = ((1 if var7 != 0 else 0) & var3)
        break
        var10 = (var10 | var17)
        var14 = (var14 | var17)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) != var11 else 0):
            continue
        break  # end loop
    var7 = 1
    if (((var3 & var10) if (var14 & 1) else var3) & 1):
        break
    if (1 if var11 == 0 else 0):
        break
    var10 = (var15 + (var16 * 286704))
    var14 = ((var15 + (var16 * 286704)) + 281796)
    var16 = i32_load(var0 + 28)
    var3 = 0
    var15 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        while True:  # loop $label60
            var15 = i32_load((var8 + (var3 << 2)) + 28)
            if i32_load(((var10 + (i32_load((var8 + (var3 << 2)) + 28) << 2)) + 281808)):
                break
            var7 = 0
            var6 = i32_load(var14)
            if (1 if i32_load(var14) == 0 else 0):
                break
            var17 = i32_load(var6 + 8)
            if (1 if i32_load(var6 + 8) == 0 else 0):
                break
            var7 = i32_load(var6)
            var6 = 0
            while True:  # loop $label59
                var18 = (var6 << 2)
                if (1 if var16 == i32_load((var7 + (var6 << 2))) else 0):
                    if (1 if i32_load((var7 + (var18 | 4))) == var15 else 0):
                        break
                var6 = (var6 + 2)
                if (1 if (var6 + 2) < var17 else 0):
                    continue
                break  # end loop
            break
            var7 = 2
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var11 else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    while True:  # loop $label65
        var17 = i32_load((var8 + (var3 << 2)) + 28)
        if i32_load(((var10 + (i32_load((var8 + (var3 << 2)) + 28) << 2)) + 281808)):
            break
        var18 = i32_load(var15 + 8)
        if (1 if i32_load(var15 + 8) == 0 else 0):
            break
        var19 = i32_load(var15)
        var7 = 0
        while True:  # loop $label63
            var6 = i32_load((var19 + (var7 << 2)))
            if (1 if var17 != ((i32_load((var19 + (var7 << 2))) - 2147483647) if (1 if var6 > 2147483646 else 0) else var6) else 0):
                var7 = (var7 + 1)
                if (1 if var18 != (var7 + 1) else 0):
                    continue
                break
            break  # end loop
        break
        var7 = 0
        var6 = i32_load(var14)
        if (1 if i32_load(var14) == 0 else 0):
            break
        var18 = i32_load(var6 + 8)
        if (1 if i32_load(var6 + 8) == 0 else 0):
            break
        var7 = i32_load(var6)
        var6 = 0
        while True:  # loop $label64
            var19 = (var6 << 2)
            if (1 if var16 == i32_load((var7 + (var6 << 2))) else 0):
                if (1 if i32_load((var7 + (var19 | 4))) == var17 else 0):
                    break
            var6 = (var6 + 2)
            if (1 if (var6 + 2) < var18 else 0):
                continue
            break  # end loop
        break
        var7 = 2
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != var11 else 0):
            continue
        break  # end loop
    # br_table ['$label0', '$label50', '$label66', '$label50']
    _br_idx = var7
    break  # br_table
    func181(var1, i32_load(var0 + 28), var2)
    var1 = ((var1 + (var2 << 2)) + 282828)
    i32_store(((var1 + (var2 << 2)) + 282828), (i32_load(var1) + 1))
    func294(var0)
    var0 = ((var2 * 404) + 9568096)
    if (1 if i32_load(var0 + 244) == 0 else 0):
        break
    var7 = 0
    while True:  # loop $label67
        var7 = (var7 + 1)
        if (1 if (var7 + 1) < i32_load(var0 + 244) else 0):
            continue
        break  # end loop
    break
    var8 = ((2147483647 if var4 else 0) + var2)
    var3 = i32_load(var0 + 20)
    var7 = i32_load(i32_load(var0 + 20) + 8)
    if (1 if i32_load(i32_load(var0 + 20) + 8) != i32_load(var3 + 4) else 0):
        var6 = i32_load(var3)
        break
    var6 = (i32_load(var3 + 12) + var7)
    i32_store(var3 + 4, (i32_load(var3 + 12) + var7))
    var4 = i32_load(var3)
    var6 = func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2)))
    if var7:
        # Unknown: memory.copy []
    if var4:
        var7 = i32_load(var3 + 8)
    i32_store(var3, var6)
    i32_store(var3 + 8, (var7 + 1))
    i32_store((var6 + (var7 << 2)), var8)
    if (1 if var5 == 0 else 0):
        var1 = ((var1 + (var2 << 2)) + 282828)
        i32_store(((var1 + (var2 << 2)) + 282828), (i32_load(var1) + 1))
    if (1 if i32_load(i32_load(var0 + 20) + 8) != 1 else 0):
        break
    # br_table ['$label69', '$label70', '$label70', '$label70', '$label70', '$label70', '$label70', '$label70', '$label70', '$label70', '$label69', '$label70']
    _br_idx = (var20 - 4)
    break  # br_table
    i32_store8(var0 + 125, 6)
    func63(af(var4), var0, 2, 0, ((((i32_load(((var2 * 404) + 9568096) + 116) * i32_load((i32_load(9142424) + (132 if i32_load(var12 + 264) else 128)))) * 1000) & 0xFFFFFFFF) // 100))
    var1 = ((var2 * 404) + 9568096)
    if (1 if i32_load(var1 + 244) == 0 else 0):
        break
    var9 = 0
    while True:  # loop $label71
        var9 = (var9 + 1)
        if (1 if (var9 + 1) < i32_load(var1 + 244) else 0):
            continue
        break  # end loop
    var9 = 1
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    var1 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
            break
    global global0
    global0 = (var13 + 16)
    return var9

