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
# $Gb
# Export: Gb
# ==========================================================
def Gb(var0):
    """Export: Gb"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var3 = i32_load(9142440)
    if (1 if i32_load(9142440) > 0 else 0):
        while True:  # loop $label3
            var4 = (var1 + 1)
            var0 = 0
            while True:  # loop $label2
                var2 = i32_load(9142440)
                var5 = ((i32_load(9142440) * var0) + var1)
                var6 = i32_load(9147288)
                var0 = (var0 + 1)
                if (1 if i32_load((i32_load(9142840) + ((var4 + ((var0 + 1) * (var2 + 2))) << 2))) == 1 else 0):
                    break
                var2 = (var5 + var6)
                var7 = i32_load8_s((var5 + var6))
                if (1 if i32_load8_s((var5 + var6)) >= 0 else 0):
                    if (1 if i32_load(i32_load((i32_load(9140332) + ((var7 & 255) << 2))) + 32) == 23 else 0):
                        break
                i32_store8(var2, 0)
                break
                i32_store8((var5 + var6), 1)
                if (1 if var0 != var3 else 0):
                    continue
                break  # end loop
            var1 = var4
            if (1 if var4 != var3 else 0):
                continue
            break  # end loop
    var0 = 0
    var1 = i32_load(9681936)
    if i32_load(9681936):
        if i32_load(var1 + 8):
            while True:  # loop $label4
                func38(i32_load((i32_load(var1) + ((var0 << 2) | 12))))
                var0 = (var0 + 4)
                var1 = i32_load(9681936)
                if (1 if (var0 + 4) < i32_load(i32_load(9681936) + 8) else 0):
                    continue
                break  # end loop
        i32_store(var1 + 8, 0)
        i32_store(9140328, 0)
    i32_store8(9681940, 1)


# ==========================================================
# $jc
# Export: jc
# ==========================================================
def jc(var0):
    """Export: jc"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    if i32_load8_u(9142917):
        break
    if (1 if i32_load(9299864) == 0 else 0):
        break
    while True:  # loop $label3
        var1 = i32_load(9299856)
        var3 = (var5 << 2)
        var4 = (i32_load(9299856) + (var5 << 2))
        var6 = i32_load((i32_load(9299856) + (var5 << 2)))
        if (1 if i32_load((i32_load(9299856) + (var5 << 2))) == 0 else 0):
            break
        if (1 if var0 <= var6 else 0):
            break
        i32_store(var4, 0)
        var1 = i32_load((var1 + (var3 | 4)))
        if (1 if i32_load((var1 + (var3 | 4))) >= 2147483647 else 0):
            var3 = (i32_load(9671128) + ((var1 - 2147483647) * 132))
            if (1 if i32_load((i32_load(9671128) + ((var1 - 2147483647) * 132)) + 92) == 0 else 0):
                break
            var1 = i32_load(var3 + 40)
            if (1 if i32_load(var3 + 40) == 0 else 0):
                break
            if (1 if i32_load8_u(9142906) == 0 else 0):
                break
            if i32_load8_u(9142916):
                i32_store(var2 + 52, var1)
                i32_store(var2 + 48, -65281)
                a_b()
                break
            i32_store(var2 + 36, var1)
            i32_store(var2 + 32, 13)
            a_b()
            break
            var1 = i32_load8_u(var3 + 127)
            if (1 if i32_load8_u(var3 + 127) == 0 else 0):
                var1 = i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 156)
            i32_store8(var3 + 127, var1)
            var4 = i32_load(var3 + 40)
            if (1 if i32_load(var3 + 40) == 0 else 0):
                break
            var3 = (var1 if var1 else (i32_load16_u(var3 + 110) + 16))
            if i32_load8_u(9142916):
                var1 = 0
                if (1 if var3 <= 15 else 0):
                    var1 = (var3 << 4)
                    var1 = ((((i32_load(((var3 << 4) + 1748)) << 8) + i32_load((var1 + 1744))) + (i32_load((var1 + 1752)) << 16)) + (i32_load((var1 + 1756)) << 24))
                i32_store(var2 + 20, var4)
                i32_store(var2 + 16, var1)
                a_b()
                break
            i32_store(var2 + 4, var4)
            i32_store(var2, var3)
            a_b()
            break
        func38(var1)
        var5 = (var5 + 2)
        if (1 if (var5 + 2) < i32_load(9299864) else 0):
            continue
        break  # end loop
    global global0
    global0 = (var2 - -64)


# ==========================================================
# $func413
# ==========================================================
def func413():
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    if (1 if i32_load8_u(9142388) == 0 else 0):
        break
    if (1 if i32_load8_u(9140304) == 0 else 0):
        break
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) >= 2 else 0):
        var3 = i32_load(9142872)
        var4 = i32_load(9561692)
        var0 = 1
        while True:  # loop $label2
            var1 = (var4 + (var0 * 286704))
            if (1 if i32_load((var4 + (var0 * 286704)) + 284616) == 0 else 0):
                break
            if i32_load(var1 + 284632):
                break
            if (1 if i32_load(var1 + 283908) != var3 else 0):
                break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var2 else 0):
                continue
            break  # end loop
    a_b()
    func397(i32_load(9561744), i32_load(9561736), i32_load(9561740))
    var3 = i32_load(9561748)
    var1 = i32_load(59176)
    if (1 if i32_load(9561748) < i32_load(59176) else 0):
        var1 = i32_load(9561704)
        if i32_load(9561704):
            var0 = 0
            var2 = i32_load(9561696)
            while True:  # loop $label4
                var4 = ((var0 << 2) + var2)
                if (1 if var3 <= i32_load(((var0 << 2) + var2) + 4) else 0):
                    var1 = (var1 - var0)
                    break
                var0 = (i32_load(var4 + 8) + var0)
                if (1 if var1 > (i32_load(var4 + 8) + var0) else 0):
                    continue
                break  # end loop
        var1 = 0
        func71((var2 + (var0 << 2)), 0, var1, 59176, 1, 1)
    else:
    var1 = (var1 + 10)
    i32_store(i32_load(59176), (var1 + 10))
    var0 = i32_load(9561704)
    i32_store(9561716, i32_load(9561704))
    i32_store(9561712, var1)
    if (1 if i32_load(9561700) != var0 else 0):
        var1 = i32_load(9561696)
        break
    var1 = (i32_load(9561708) + var0)
    i32_store(9561700, (i32_load(9561708) + var0))
    var2 = i32_load(9561696)
    var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var0:
        # Unknown: memory.copy []
    if var2:
        var0 = i32_load(9561704)
    i32_store(9561696, var1)
    i32_store(9561704, (var0 + 1))
    i32_store((var1 + (var0 << 2)), 0)
    var3 = i32_load(59176)
    var0 = i32_load(9561704)
    if (1 if i32_load(9561704) != i32_load(9561700) else 0):
        var2 = var1
        break
    var2 = (i32_load(9561708) + var0)
    i32_store(9561700, (i32_load(9561708) + var0))
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(9561696, var2)
    var0 = i32_load(9561704)
    i32_store(9561704, (var0 + 1))
    i32_store((var2 + (var0 << 2)), var3)
    var0 = i32_load(9561704)
    if (1 if i32_load(9561704) != i32_load(9561700) else 0):
        var1 = var2
        break
    var1 = (i32_load(9561708) + var0)
    i32_store(9561700, (i32_load(9561708) + var0))
    var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(9561696, var1)
    var0 = i32_load(9561704)
    i32_store(9561704, (var0 + 1))
    i32_store((var1 + (var0 << 2)), 3)
    i32_store8(9140304, 0)
    return af(var2)


# ==========================================================
# $func420
# ==========================================================
def func420(var0):
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
    var12 = 0
    var13 = 0
    var14 = 0
    var15 = 0
    var16 = 0
    var7 = i32_load(9561692)
    i32_store(var0 + 88, 0)
    var6 = i32_load16_u(var0 + 110)
    var2 = i32_load8_u(var0 + 122)
    var3 = ((var7 + (i32_load16_u(var0 + 110) * 286704)) + (i32_load8_u(var0 + 122) << 2))
    var1 = (((var7 + (i32_load16_u(var0 + 110) * 286704)) + (i32_load8_u(var0 + 122) << 2)) + 281808)
    var5 = i32_load(var1)
    var4 = (i32_load(var1) + 1)
    i32_store((((var7 + (i32_load16_u(var0 + 110) * 286704)) + (i32_load8_u(var0 + 122) << 2)) + 281808), (i32_load(var1) + 1))
    if i32_load8_u(9142905):
        break
    var1 = (var3 + 278576)
    i32_store((var3 + 278576), (i32_load(var1) + 1))
    var1 = (var3 + 279596)
    var3 = i32_load((var3 + 279596))
    if (1 if var4 <= i32_load((var3 + 279596)) else 0):
        break
    i32_store(var1, (var3 + 1))
    if var3:
        break
    if (1 if i32_load(38468) == var2 else 0):
        break
    if (1 if i32_load(38668) == var2 else 0):
        break
    if (1 if i32_load(38664) == var2 else 0):
        break
    if (1 if i32_load(38488) == var2 else 0):
        break
    if (1 if i32_load(38848) == var2 else 0):
        break
    if (1 if i32_load(38916) == var2 else 0):
        break
    if (1 if i32_load(38516) == var2 else 0):
        break
    if (1 if i32_load(38844) == var2 else 0):
        break
    if (1 if i32_load(38912) == var2 else 0):
        break
    if (1 if i32_load(38464) == var2 else 0):
        break
    if (1 if i32_load(38836) == var2 else 0):
        break
    if (1 if i32_load(38904) == var2 else 0):
        break
    if (1 if i32_load(38484) == var2 else 0):
        break
    if (1 if i32_load(38840) == var2 else 0):
        break
    if (1 if i32_load(38908) == var2 else 0):
        break
    if (1 if i32_load(38476) == var2 else 0):
        break
    if (1 if i32_load(38820) == var2 else 0):
        break
    if (1 if i32_load(38700) == var2 else 0):
        break
    if (1 if i32_load(38520) == var2 else 0):
        break
    if (1 if i32_load(38808) == var2 else 0):
        break
    if (1 if i32_load(38884) == var2 else 0):
        break
    if (1 if i32_load(38564) == var2 else 0):
        break
    if (1 if i32_load(38852) != var2 else 0):
        break
    i32_store((((var7 + (var6 * 286704)) + (var2 << 2)) + 280616), (i32_load(9142848) * 25))
    if var5:
        break
    if (1 if i32_load((var7 + (var6 * 286704)) + 283908) != i32_load(9142872) else 0):
        break
    var9 = ((var2 * 404) + 9568096)
    if (1 if i32_load(((var2 * 404) + 9568096) + 244) == 0 else 0):
        break
    while True:  # loop $label6
        var5 = i32_load((i32_load(var9 + 240) + (var8 << 2)))
        if i32_load8_u(9147141):
            break
        var1 = 0
        var4 = i32_load(9671120)
        if (1 if i32_load(9671120) == 0 else 0):
            break
        while True:  # loop $label5
            var3 = i32_load(((var1 << 2) + 9263072))
            if (1 if i32_load(((var1 << 2) + 9263072)) == 0 else 0):
                break
            if (1 if i32_load(var3 + 12) != var5 else 0):
                break
            if i32_load8_u(var3 + 24):
                break
            break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var4 else 0):
                continue
            break  # end loop
        var8 = (var8 + 1)
        if (1 if (var8 + 1) < i32_load(var9 + 244) else 0):
            continue
        break  # end loop
    var1 = i32_load(((var2 * 404) + 9568096) + 176)
    if (1 if i32_load(((var2 * 404) + 9568096) + 176) == 0 else 0):
        break
    var5 = (var7 + (var6 * 286704))
    i32_store((var7 + (var6 * 286704)) + 283980, (i32_load(var5 + 283980) + var1))
    var4 = i32_load(var5 + 283976)
    if (1 if var1 > 0 else 0):
        i32_store8(var5 + 286700, 1)
    var1 = (var5 + 281748)
    if (1 if i32_load((var5 + 281748)) >= var4 else 0):
        break
    i32_store(var1, var4)
    if i32_load8_u(9147152):
        break
    var1 = i32_load8_u(var0 + 122)
    if (1 if i32_load8_u(var0 + 122) == i32_load(38540) else 0):
        break
    if (1 if i32_load(38812) == var1 else 0):
        break
    if (1 if i32_load(38888) != var1 else 0):
        break
    var10 = i32_load8_u(var0 + 122)
    if (1 if i32_load((var7 + (var6 * 286704)) + 286684) == 0 else 0):
        break
    if (1 if var10 != i32_load(38512) else 0):
        if (1 if i32_load(38792) != var10 else 0):
            break
    var1 = ((var2 * 404) + 9568096)
    var5 = (i32_load(((var2 * 404) + 9568096) + 216) + 2)
    if (1 if (i32_load(((var2 * 404) + 9568096) + 216) + 2) <= 0 else 0):
        break
    var4 = (i32_load(var1 + 220) + 2)
    if (1 if (i32_load(var1 + 220) + 2) <= 0 else 0):
        break
    var14 = i32_load(9142440)
    var15 = (i32_load(9142440) + 2)
    var1 = (var7 + (var6 * 286704))
    var16 = ((var7 + (var6 * 286704)) + 283876)
    var11 = (var1 + 283872)
    var12 = i32_load(var0 + 28)
    var13 = i32_load(9142840)
    var3 = i32_load16_u(var0 + 112)
    var6 = (i32_load16_u(var0 + 112) - 1)
    var1 = (var5 + (i32_load16_u(var0 + 112) - 1))
    var2 = ((var5 + (i32_load16_u(var0 + 112) - 1)) if (1 if var1 > var3 else 0) else var3)
    var3 = i32_load16_u(var0 + 114)
    var5 = (i32_load16_u(var0 + 114) - 1)
    var1 = (var4 + (i32_load16_u(var0 + 114) - 1))
    var7 = ((var4 + (i32_load16_u(var0 + 114) - 1)) if (1 if var1 > var3 else 0) else var3)
    var9 = 2147483647
    while True:  # loop $label13
        var3 = (var6 + 1)
        var1 = var5
        if (1 if var6 < var14 else 0):
            while True:  # loop $label12
                var8 = var1
                var1 = (var1 + 1)
                if (1 if var8 >= var14 else 0):
                    break
                if (1 if (var6 | var8) < 0 else 0):
                    break
                if (1 if i32_load((var13 + ((var3 + ((var1 + var15) * var15)) << 2))) == var12 else 0):
                    break
                var4 = (var8 - i32_load(var16))
                var4 = (var6 - i32_load(var11))
                var4 = (((var8 - i32_load(var16)) * var4) + ((var6 - i32_load(var11)) * var4))
                if (1 if (((var8 - i32_load(var16)) * var4) + ((var6 - i32_load(var11)) * var4)) >= var9 else 0):
                    break
                i32_store16(var0 + 118, var8)
                i32_store16(var0 + 116, var6)
                var9 = var4
                if (1 if var1 != var7 else 0):
                    continue
                break  # end loop
        var6 = var3
        if (1 if var3 != var2 else 0):
            continue
        break  # end loop
    var1 = ((var10 * 404) + 9568096)
    if (1 if i32_load8_u(((var10 * 404) + 9568096) + 377) == 0 else 0):
        break
    var11 = i32_load(var1 + 216)
    if (1 if i32_load(var1 + 216) <= 0 else 0):
        break
    var3 = i32_load16_u(var0 + 114)
    var12 = (i32_load16_u(var0 + 114) + i32_load(var1 + 220))
    if (1 if (i32_load16_u(var0 + 114) + i32_load(var1 + 220)) <= var3 else 0):
        break
    var5 = i32_load16_u(var0 + 112)
    var13 = (var11 + i32_load16_u(var0 + 112))
    var2 = i32_load(var1 + 372)
    var7 = ((var10 * 404) + 9568308)
    var1 = var5
    while True:  # loop $label17
        var4 = (var1 + 1)
        var6 = (var1 - var5)
        var8 = i32_load(9142840)
        var1 = var3
        while True:  # loop $label16
            if i32_load8_u((var2 + (var6 + ((var1 - var3) * var11)))):
                var1 = (var1 + 1)
                break
            var9 = (i32_load(9142440) + 2)
            var1 = (var1 + 1)
            i32_store((var8 + (((((i32_load(9142440) + 2) + (var1 + 1)) * var9) + var4) << 2)), i32_load(var7))
            if (1 if var1 != var12 else 0):
                continue
            break  # end loop
        var1 = var4
        if (1 if var4 < var13 else 0):
            continue
        break  # end loop
    if (1 if i32_load(9142872) != i32_load16_u(var0 + 110) else 0):
        break
    var0 = i32_load(((var10 * 404) + 9568096) + 180)
    if (1 if i32_load(((var10 * 404) + 9568096) + 180) == 0 else 0):
        break

