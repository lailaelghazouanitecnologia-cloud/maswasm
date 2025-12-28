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
# $Pd
# Export: Pd
# ==========================================================
def Pd(var0, var1, var2, var3, var4, var5, var6):
    """Export: Pd"""
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
    var20 = 0
    var21 = 0
    var22 = 0
    var23 = 0
    var24 = 0
    var7 = (global0 - 176)
    global global0
    global0 = (global0 - 176)
    var8 = i32_load(9561692)
    var10 = ((var0 * 132) + 9216080)
    var15 = (0 if var6 else i32_load(9671124))
    if (1 if ((0 if var6 else i32_load(9671124)) - 97) > -3 else 0):
        break
    var13 = i32_load(var10 + 68)
    if (1 if i32_load(var10 + 68) == 0 else 0):
        break
    var14 = i32_load(9147132)
    var16 = ((var0 * 132) + 9216080)
    var17 = (var8 + (var3 * 286704))
    var6 = 0
    while True:  # loop $label3
        var18 = i32_load((var16 + (var6 << 2)) + 28)
        var9 = ((i32_load((var16 + (var6 << 2)) + 28) * 404) + 9568096)
        if (1 if i32_load(((i32_load((var16 + (var6 << 2)) + 28) * 404) + 9568096) + 196) == var2 else 0):
            break
        if var14:
            break
        # br_table ['$label1', '$label2', '$label2', '$label1', '$label2']
        _br_idx = i32_load(var9 + 264)
        break  # br_table
        if i32_load8_u(var9 + 354):
            break
        var12 = ((var11 << 2) + 9147392)
        i32_store(((var11 << 2) + 9147392), i32_load(var9 + 84))
        var9 = i32_load(var9 + 180)
        i32_store(var12 + 4, i32_load(i32_load(var9 + 180) + 8))
        i32_store(var12 + 8, i32_load(var9 + 12))
        i32_store(var12 + 12, i32_load(((var17 + (var18 << 2)) + 281808)))
        var11 = (var11 + 4)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) != var13 else 0):
            continue
        break  # end loop
    var9 = i32_load(var10 + 12)
    i64_store(var7 + 168, 0)
    i64_store(var7 + 160, 0)
    if i32_load8_u(var10 + 23):
        var1 = i32_load(((var0 * 132) + 9216080) + 4)
        if (1 if var4 == 0 else 0):
            var4 = i32_load((((var8 + (var3 * 286704)) + (var1 * 36)) + 269376))
            var4 = (i32_load((((var8 + (var3 * 286704)) + (var1 * 36)) + 269376)) if var4 else 100)
            var5 = ((var1 * 404) + 9568096)
            var12 = ((((i32_load((((var8 + (var3 * 286704)) + (var1 * 36)) + 269376)) if var4 else 100) * i32_load(((var1 * 404) + 9568096) + 80)) & 0xFFFFFFFF) // 100)
            var13 = (((i32_load(var5 + 72) * var4) & 0xFFFFFFFF) // 100)
            var14 = (((i32_load(var5 + 68) * var4) & 0xFFFFFFFF) // 100)
            break
        if (1 if var15 != 95 else 0):
            var4 = ((var1 * 404) + 9568096)
            var14 = (((i32_load(((var1 * 404) + 9568096) + 68) * 36) // 10) + 620)
            var12 = ((i32_load(var4 + 80) * 36) // 10)
            var13 = ((i32_load(var4 + 72) * 36) // 10)
            break
        var4 = ((var1 * 404) + 9568096)
        var14 = (((i32_load(((var1 * 404) + 9568096) + 68) * 144) // 10) + (120 if (1 if i32_load((((var8 + (var3 * 286704)) + (i32_load(39136) << 2)) + 281808)) == 1 else 0) else 0))
        var12 = ((i32_load(var4 + 80) * 144) // 10)
        var13 = ((i32_load(var4 + 72) * 144) // 10)
        var15 = ((i32_load(var4 + 76) * 144) // 10)
        var5 = ((var1 * 404) + 9568096)
        var17 = i32_load(((var1 * 404) + 9568096) + 264)
        if (1 if i32_load(((var1 * 404) + 9568096) + 264) != 3 else 0):
            break
        var4 = i32_load(var5 + 368)
        if (1 if i32_load(var5 + 368) == 60 else 0):
            break
        if (1 if var4 == 61 else 0):
            break
        if (1 if var4 == 63 else 0):
            break
        if (1 if var4 == 62 else 0):
            break
        if (1 if var4 == 55 else 0):
            break
        var4 = (6 if var4 else 5)
        var16 = 0
        var6 = i32_load(var10)
        if (1 if i32_load(var10) == 5 else 0):
            break
        if (1 if var6 == 12 else 0):
            break
        if (1 if var6 == 7 else 0):
            break
        var9 = (3 if (1 if var6 == 15 else 0) else (3 if (1 if var6 == 1 else 0) else (3 if (1 if var6 == 16 else 0) else -1)))
        var18 = i32_load(var5 + 116)
        var19 = i32_load(var5 + 236)
        var20 = i32_load(var5 + 232)
        var21 = i32_load(var5 + 244)
        var22 = i32_load(var5 + 240)
        var6 = ((var1 * 404) + 9568096)
        var23 = i32_load(((var1 * 404) + 9568096) + 144)
        if (1 if var17 == 1 else 0):
            var3 = func180((var8 + (var3 * 286704)), var1)
            var8 = i32_load(var6 + 204)
        else:
        i32_store((i32_load(var6 + 204) if (1 if var3 >= var8 else 0) else 0) + 144, 0)
        i32_store(var7 + 140, var2)
        i32_store(var7 + 136, var23)
        i32_store(var7 + 132, var9)
        i32_store(var7 + 128, var18)
        i32_store(var7 + 124, var19)
        i32_store(var7 + 120, var20)
        i32_store(var7 + 116, var21)
        i32_store(var7 + 112, var22)
        var3 = i32_load(var6 + 88)
        var6 = i32_load(var6 + 84)
        var8 = i32_load(var10 + 12)
        var2 = 0
        if (1 if i32_load(var5 + 264) == 3 else 0):
            var2 = i32_load(((var1 * 404) + 9568096) + 120)
        var24 = i64_load(((var0 * 132) + 9216080) + 124)
        var0 = ((var1 * 404) + 9568096)
        var1 = i32_load(((var1 * 404) + 9568096) + 92)
        var5 = i32_load(var0 + 100)
        var10 = i32_load(var0 + 104)
        var0 = i32_load(var0 + 212)
        i32_store((var7 - -64), var8)
        i32_store(var7 + 68, var6)
        i32_store(var7 + 72, var3)
        i32_store(var7 + 76, var11)
        i32_store(var7 + 80, var2)
        i32_store(var7 + 108, var0)
        i32_store(var7 + 104, var10)
        i32_store(var7 + 100, var5)
        i32_store(var7 + 96, var1)
        i32_store(var7 + 92, var4)
        i64_store(var7 + 84, var24)
        i32_store(var7 + 52, var13)
        i32_store(var7 + 56, var15)
        i32_store(var7 + 60, var12)
        i32_store(var7 + 48, var14)
        break
    var6 = 0
    var2 = i32_load(var10)
    if ((1 if i32_load(var10) != 1 else 0) & (1 if var2 != 13 else 0)):
        break
    var2 = i32_load(((var0 * 132) + 9216080) + 4)
    if (1 if i32_load(((var0 * 132) + 9216080) + 4) == 0 else 0):
        break
    var4 = ((var2 * 40) + 9671200)
    var2 = i32_load(((var2 * 40) + 9671200) + 12)
    if i32_load(((var2 * 40) + 9671200) + 12):
        i64_store(var7 + 160, i64_load(var2))
        i64_store(var7 + 168, i64_load(var2 + 8))
    var2 = i32_load(var4 + 8)
    if (1 if i32_load(var4 + 8) == 0 else 0):
        break
    var6 = i32_load((((var8 + (i32_load16_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 110) * 286704)) + (var2 << 2)) + 283984))
    if (1 if var15 != 240 else 0):
        break
    if (1 if i32_load(38892) != var5 else 0):
        break
    var2 = i32_load((var8 + (var3 * 286704)) + 281792)
    if (1 if i32_load((var8 + (var3 * 286704)) + 281792) == 0 else 0):
        break
    if (1 if i32_load(var2 + 8) <= var1 else 0):
        break
    var1 = i32_load((i32_load(var2) + (var1 << 2)))
    var2 = ((i32_load((i32_load(var2) + (var1 << 2))) & 0xFFFFFFFF) >> 16)
    var4 = (var1 & 65535)
    var1 = (((var1 & 65535) * 404) + 9568096)
    # br_table ['$label10', '$label11', '$label12', '$label9']
    _br_idx = i32_load((((var1 & 65535) * 404) + 9568096) + 268)
    break  # br_table
    var2 = (var2 * 150)
    i32_store(var7 + 160, ((((var2 * 150) * i32_load(var1 + 68)) & 0xFFFFFFFF) // 100))
    i32_store(var7 + 164, (((i32_load(var1 + 72) * var2) & 0xFFFFFFFF) // 100))
    i32_store(var7 + 168, (((i32_load(var1 + 76) * var2) & 0xFFFFFFFF) // 100))
    i32_store(var7 + 172, (((i32_load(var1 + 80) * var2) & 0xFFFFFFFF) // 100))
    break
    if (1 if i32_load(38972) == var4 else 0):
        break
    if (1 if i32_load(38976) == var4 else 0):
        break
    break
    i32_store((20 if (1 if i32_load(38968) == var4 else 0) else 4) + 160, (8 * var2))
    break
    i32_store(var7 + 160, (var2 << 4))
    if (1 if var9 == 323 else 0):
        var1 = (var8 + (var3 * 286704))
        i32_store(((var7 + 160) + (i32_load((var8 + (var3 * 286704)) + 283920) << 2)), i32_load(var1 + 283916))
    var0 = i32_load(((var0 * 132) + 9216080) + 120)
    i32_store(var7 + 16, i32_load(var10 + 12))
    i32_store(var7 + 20, var0)
    i32_store(var7 + 24, 0)
    i32_store(var7 + 28, var11)
    i32_store(var7 + 32, var6)
    i64_store(var7, i64_load(var7 + 160))
    i64_store(var7 + 8, i64_load(var7 + 168))
    if var11:
        # Unknown: memory.fill []
    global global0
    global0 = (var7 + 176)
    return (var11 << 2)


# ==========================================================
# $func346
# ==========================================================
def func346():
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
    var1 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if (1 if i32_load8_u(9216060) == 0 else 0):
        break
    if (1 if i32_load(9142872) == 0 else 0):
        break
    if i32_load8_u(9142917):
        break
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var4 = i32_load(9561692)
    var2 = 1
    while True:  # loop $label4
        var5 = (var4 + (var2 * 286704))
        i32_store((var4 + (var2 * 286704)) + 283944, 1)
        var3 = i32_load(9142892)
        if (1 if i32_load(9142892) > 1 else 0):
            var8 = (var5 + 283944)
            var7 = 1
            var0 = 1
            while True:  # loop $label3
                if (1 if var0 == var2 else 0):
                    break
                var6 = (var4 + (var0 * 286704))
                if (1 if i32_load((var4 + (var0 * 286704)) + 284616) == 0 else 0):
                    break
                var6 = func88(var6)
                var9 = func88(var5)
                if (1 if func88(var6) <= func88(var5) else 0):
                    if (1 if var6 != var9 else 0):
                        break
                    if (1 if var0 <= var2 else 0):
                        break
                var7 = (var7 + 1)
                i32_store(var8, (var7 + 1))
                var3 = i32_load(9142892)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) < var3 else 0):
                    continue
                break  # end loop
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var3 else 0):
            continue
        break  # end loop
    if (1 if var3 < 2 else 0):
        break
    var4 = i32_load(9561692)
    var2 = 1
    while True:  # loop $label5
        var0 = (var4 + (var2 * 286704))
        var5 = i32_load((var4 + (var2 * 286704)) + 284616)
        if i32_load((var4 + (var2 * 286704)) + 284616):
            var4 = func88(var0)
            var7 = i32_load8_u(var0 + 283972)
            var8 = i32_load(var0 + 283944)
            var3 = i32_load(var0 + 283908)
            var6 = i32_load8_u((var0 + 283974))
            i32_store(var1 + 16, i32_load8_u((var0 + 283973)))
            i32_store(var1 + 20, var6)
            i32_store(var1 + 24, var5)
            i32_store(var1 + 28, var3)
            var5 = i32_load(9142872)
            i32_store(var1 + 32, ((1 if i32_load(9142872) != 0 else 0) & (1 if var3 == var5 else 0)))
            i32_store(var1, var4)
            i32_store(var1 + 4, var8)
            i32_store(var1 + 8, var0)
            i32_store(var1 + 12, var7)
            a_b()
            var4 = i32_load(9561692)
            var3 = i32_load(9142892)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var3 else 0):
            continue
        break  # end loop
    a_b()
    global global0
    global0 = (var1 + 48)


# ==========================================================
# $func361
# ==========================================================
def func361():
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var5 = i32_load(9561692)
    var3 = 1
    var1 = 1
    if i32_load8_u(9147127):
        while True:  # loop $label4
            var2 = (var5 + (var3 * 286704))
            i32_store((var5 + (var3 * 286704)) + 283892, func88(var2))
            var0 = 0
            var1 = i32_load((var2 + 278572))
            var4 = i32_load(i32_load((var2 + 278572)) + 8)
            if i32_load(i32_load((var2 + 278572)) + 8):
                var6 = i32_load(var1)
                var1 = 0
                while True:  # loop $label1
                    var1 = (i32_load((var6 + (var0 << 2))) + var1)
                    var0 = (var0 + 15)
                    if (1 if (var0 + 15) < var4 else 0):
                        continue
                    break  # end loop
                var0 = ((var1 & 0xFFFFFFFF) // 6)
            i32_store(var2 + 283888, var0)
            if (1 if i32_load(9147128) == 9 else 0):
                var0 = (((i32_load(var2 + 283956) * 100) & 0xFFFFFFFF) // i32_load(9561724))
            i32_store(var2 + 283884, var0)
            var4 = (var2 + 283884)
            var2 = i32_load(var2 + 284608)
            var1 = i32_load(9561720)
            if (1 if i32_load(var2 + 284608) != i32_load(9561720) else 0):
                break
            if (1 if var1 == 0 else 0):
                break
            i32_store(var4, (((var0 * 155) & 0xFFFFFFFF) // 100))
            var1 = i32_load(9561720)
            var0 = i32_load(9142892)
            if (1 if var1 == var2 else 0):
                break
            if (1 if var1 == 0 else 0):
                break
            if (1 if var0 != 3 else 0):
                break
            if (1 if i32_load(9147128) != 1 else 0):
                break
            i32_store(var4, 0)
            var0 = i32_load(9142892)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) < var0 else 0):
                continue
            break  # end loop
        break
    while True:  # loop $label6
        var0 = (var5 + (var1 * 286704))
        var2 = func88(var0)
        i32_store((var5 + (var1 * 286704)) + 283884, func88(var0))
        i32_store(var0 + 283892, var2)
        var1 = (var1 + 1)
        var0 = i32_load(9142892)
        if (1 if (var1 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    if (1 if var0 < 2 else 0):
        break
    var3 = i32_load(9561692)
    var2 = 1
    while True:  # loop $label9
        var0 = (var3 + (var2 * 286704))
        i32_store((var3 + (var2 * 286704)) + 283944, 1)
        var1 = i32_load(9142892)
        if (1 if i32_load(9142892) >= 2 else 0):
            var4 = (var0 + 283944)
            var6 = (var0 + 283884)
            var5 = 1
            var0 = 1
            while True:  # loop $label8
                if (1 if var0 == var2 else 0):
                    break
                var7 = i32_load((var3 + (var0 * 286704)) + 283884)
                var8 = i32_load(var6)
                if (1 if i32_load((var3 + (var0 * 286704)) + 283884) <= i32_load(var6) else 0):
                    if (1 if var7 != var8 else 0):
                        break
                    if (1 if var0 <= var2 else 0):
                        break
                var5 = (var5 + 1)
                i32_store(var4, (var5 + 1))
                var1 = i32_load(9142892)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) < var1 else 0):
                    continue
                break  # end loop
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var1 else 0):
            continue
        break  # end loop

