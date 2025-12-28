"""
Auto-generated from WAT. Contains 13 functions.
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
# $td
# Export: td
# ==========================================================
def td():
    """Export: td"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if i32_load8_u(9147141) == 0 else 0):
        var3 = i32_load(9671120)
        if (1 if i32_load(9671120) == 0 else 0):
            break
        if (1 if var3 >= 4 else 0):
            var7 = (var3 & -4)
            while True:  # loop $label1
                var0 = (var1 << 2)
                i32_store(((var1 << 2) + 9684512), i32_load(i32_load((var0 + 9263072)) + 12))
                var5 = (var0 | 4)
                i32_store(((var0 | 4) + 9684512), i32_load(i32_load((var5 + 9263072)) + 12))
                var5 = (var0 | 8)
                i32_store(((var0 | 8) + 9684512), i32_load(i32_load((var5 + 9263072)) + 12))
                var0 = (var0 | 12)
                i32_store(((var0 | 12) + 9684512), i32_load(i32_load((var0 + 9263072)) + 12))
                var1 = (var1 + 4)
                var4 = (var4 + 4)
                if (1 if (var4 + 4) != var7 else 0):
                    continue
                break  # end loop
        var0 = (var3 & 3)
        if (1 if (var3 & 3) == 0 else 0):
            break
        while True:  # loop $label2
            var4 = (var1 << 2)
            i32_store(((var1 << 2) + 9684512), i32_load(i32_load((var4 + 9263072)) + 12))
            var1 = (var1 + 1)
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != var0 else 0):
                continue
            break  # end loop
        i32_store(var2 + 4, var3)
        i32_store(var2, 9684512)
        break
    global global0
    global0 = (var2 + 16)


# ==========================================================
# $func563
# ==========================================================
def func563(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var4 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if var2:
        var3 = i32_load(9142892)
        var6 = i32_load(9561692)
        while True:  # loop $label3
            var7 = (var5 << 2)
            var0 = 0
            if (1 if var3 < 2 else 0):
                break
            var8 = i32_load((var1 + var7))
            var0 = 1
            while True:  # loop $label1
                if (1 if i32_load((var6 + (var0 * 286704)) + 284616) == var8 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var3 else 0):
                    continue
                break  # end loop
            var0 = 0
            if (1 if var0 >= var3 else 0):
                break
            var0 = (var6 + (var0 * 286704))
            if (1 if i32_load((var6 + (var0 * 286704)) + 283908) == 0 else 0):
                break
            i32_store(var0 + 284604, i32_load((var1 + (var7 | 4))))
            var3 = i32_load(9142892)
            var5 = (var5 + 2)
            if (1 if (var5 + 2) < var2 else 0):
                continue
            break  # end loop
    if i32_load8_u(9147213):
        if (1 if i32_load(9687276) == 0 else 0):
            break
        var1 = i32_load(9142892)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var2 = i32_load(9561692)
        var0 = 1
        while True:  # loop $label6
            var3 = (var2 + (var0 * 286704))
            if (1 if i32_load8_u((var2 + (var0 * 286704)) + 286699) == 0 else 0):
                var1 = i32_load(var3 + 284604)
                if (1 if i32_load8_u(9147210) == 0 else 0):
                    break
                if (1 if i32_load(var3 + 284616) != i32_load(9561844) else 0):
                    if (1 if i32_load(9142872) != var0 else 0):
                        break
                    if (1 if i32_load8_u(9142388) == 0 else 0):
                        break
                var1 = 2147483647
                i32_store(var4 + 4, var1)
                i32_store(var4, var0)
                a_b()
                var2 = i32_load(9561692)
                var1 = i32_load(9142892)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < var1 else 0):
                continue
            break  # end loop
        break
    global global0
    global0 = (var4 + 16)


# ==========================================================
# $Nc
# Export: Nc
# ==========================================================
def Nc():
    """Export: Nc"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var0 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var2 = i32_load(9568064)
    if (1 if i32_load(9568064) != i32_load(9568068) else 0):
        while True:  # loop $label0
            var2 = (var2 + (var1 << 7))
            var3 = i32_load((var2 + (var1 << 7)) + 104)
            i32_store(var0 + 8, var1)
            i32_store(var0 + 4, var3)
            i32_store(var0, (var2 + 24))
            a_b()
            var1 = (var1 + 1)
            var2 = i32_load(9568064)
            if (1 if (var1 + 1) < ((i32_load(9568068) - i32_load(9568064)) >> 7) else 0):
                continue
            break  # end loop
    global global0
    global0 = (var0 + 16)


# ==========================================================
# $func586
# ==========================================================
def func586(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var3 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var2 = 0
    if (i32_load8_u(9142917) | i32_load8_u(9147152)):
        break
    var4 = i32_load(59164)
    var5 = i32_load(9561692)
    var6 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var1 = 1
    while True:  # loop $label2
        var7 = (var5 + (var1 * 286704))
        if (1 if var4 == i32_load((var5 + (var1 * 286704)) + 284616) else 0):
            var2 = var1
            break
        if (1 if var4 == i32_load(var7 + 284628) else 0):
            var2 = var1
            break
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var6 else 0):
            continue
        break  # end loop
    var7 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) == 0 else 0):
        if i32_load8_u((i32_load(9143004) + (i32_load((var5 + (var2 * 286704)) + 283908) + (i32_load(9142872) * var6)))):
            break
    var2 = i32_load(var0 + 4)
    var8 = i32_load(var0)
    var0 = 0
    if (1 if var6 < 2 else 0):
        break
    var1 = 1
    while True:  # loop $label4
        var9 = (var5 + (var1 * 286704))
        if (1 if var4 == i32_load((var5 + (var1 * 286704)) + 284616) else 0):
            var0 = var1
            break
        if (1 if var4 == i32_load(var9 + 284628) else 0):
            var0 = var1
            break
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var6 else 0):
            continue
        break  # end loop
    i32_store(var3 + 16, var4)
    i32_store(var3 + 4, var2)
    i32_store(var3, var8)
    i32_store(var3 + 12, (1 if var7 == 0 else 0))
    i32_store(var3 + 8, (var5 + (var0 * 286704)))
    global global0
    global0 = (var3 + 32)


# ==========================================================
# $pb
# Export: pb
# ==========================================================
def pb(var0):
    """Export: pb"""
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var0 = (i32_load(9671128) + (var0 * 132))
    var2 = i32_load16_u((i32_load(9671128) + (var0 * 132)) + 114)
    var3 = i32_load16_u(var0 + 112)
    i32_store(var1, i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 84))
    i32_store(var1 + 4, var3)
    i32_store(var1 + 8, var2)
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $mb
# Export: mb
# ==========================================================
def mb(var0):
    """Export: mb"""
    var1 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store8(9681824, var0)
    if (1 if i32_load(9216064) == 0 else 0):
        i32_store(41088, 7)
        i64_store(var1, 7)
    i32_store(9216064, 58)
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $dd
# Export: dd
# ==========================================================
def dd(var0):
    """Export: dd"""
    var1 = 0
    var2 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var0 = ((9684460 if (1 if var0 == 1 else 0) else 9684476) if var0 else 9684444)
    var2 = i32_load(((9684460 if (1 if var0 == 1 else 0) else 9684476) if var0 else 9684444))
    i32_store(var1 + 4, i32_load(var0 + 8))
    i32_store(var1, var2)
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $func639
# ==========================================================
def func639(var0):
    var1 = 0
    var2 = 0
    var1 = (i32_load(9671128) + (i32_load(var0 + 32) * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 125) != 3 else 0):
        break
    var1 = func236(var0, var1)
    if func236(var0, var1):
        i32_store(var0 + 32, var1)
        var0 = i32_load(var0 + 20)
        if (1 if i32_load(var0 + 20) == 0 else 0):
            break
        if (1 if i32_load(var0 + 8) < 5 else 0):
            break
        i32_store(i32_load(var0) + 16, var1)
        return 0
    var2 = 1
    var0 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        break
    i32_store(var0 + 8, 0)
    return var2


# ==========================================================
# $func645
# ==========================================================
def func645(var0, var1, var2):
    var0 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if i32_load8_u(9142388):
        i32_store(var0, i32_load(59164))
    global global0
    global0 = (var0 + 16)


# ==========================================================
# $Ve
# Export: Ve
# ==========================================================
def Ve(var0):
    """Export: Ve"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var5 = i32_load(9561692)
    var3 = 1
    var1 = 1
    while True:  # loop $label1
        var6 = (var5 + (var1 * 286704))
        var7 = i32_load((var5 + (var1 * 286704)) + 284616)
        if (1 if var0 == i32_load(var6 + 284628) else 0):
            if var7:
                break
            i32_store((var6 + 284616), var0)
            var0 = (var5 + (var1 * 286704))
            i32_store8((var5 + (var1 * 286704)) + 286699, 0)
            var1 = i32_load(var0 + 283908)
            var0 = i32_load8_u(var0 + 286696)
            i32_store(var2 + 8, 0)
            i32_store(var2 + 4, var0)
            i32_store(var2, var1)
            a_b()
            break
        if (1 if var0 == var7 else 0):
            break
        var1 = (var1 + 1)
        var3 = (1 if (var1 + 1) < var4 else 0)
        if (1 if var1 != var4 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var2 + 16)
    return var3


# ==========================================================
# $Rd
# Export: Rd
# ==========================================================
def Rd(var0, var1):
    """Export: Rd"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var3 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    if (1 if i32_load8_u(9216068) == 0 else 0):
        var1 = i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) * 404) + 9568096) + 196)
    var2 = ((var0 * 132) + 9216080)
    if (1 if i32_load8_u(((var0 * 132) + 9216080) + 23) == 0 else 0):
        var5 = 1
        var7 = 2147483647
        break
    var5 = 1
    var7 = i32_load(var2 + 4)
    var4 = ((i32_load(var2 + 4) * 404) + 9568096)
    if (1 if i32_load(((i32_load(var2 + 4) * 404) + 9568096) + 264) == 3 else 0):
        break
    var0 = i32_load(var4 + 196)
    if (1 if i32_load(var4 + 196) == var1 else 0):
        break
    if (1 if var0 > 2 else 0):
        break
    var5 = (1 if i32_load(9147132) != 0 else 0)
    var6 = i32_load(var4 + 144)
    var8 = i32_load(var4 + 88)
    var5 = ((1 if i32_load8_u(var4 + 354) == 0 else 0) & var5)
    var1 = i32_load(var4 + 84)
    var0 = i32_load(var2 + 8)
    var2 = i32_load(var2)
    if (1 if i32_load(var2) == 5 else 0):
        break
    if (1 if var2 == 12 else 0):
        break
    if (1 if var2 == 7 else 0):
        break
    var4 = (3 if (1 if var2 == 15 else 0) else (3 if (1 if var2 == 1 else 0) else (3 if (1 if var2 == 16 else 0) else -1)))
    i32_store(var3 + 28, var5)
    i32_store(var3 + 24, var7)
    i32_store(var3 + 20, var4)
    i32_store(var3 + 16, (0 - var6))
    i32_store(var3 + 8, var8)
    i32_store(var3 + 4, var1)
    i32_store(var3, var0)
    i32_store(var3 + 12, (1 if var2 == 2 else 0))
    global global0
    global0 = (var3 + 32)
    return var3


# ==========================================================
# $Ee
# Export: Ee
# ==========================================================
def Ee(var0):
    """Export: Ee"""
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
    var5 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var1 = 9143012
    if (1 if var0 <= 2 else 0):
        var1 = i32_load(((var0 << 2) + 10284))
    var3 = 1
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) > 1 else 0):
        var6 = i32_load(var1)
        while True:  # loop $label3
            var8 = (i32_load(9561692) + (var3 * 286704))
            if (1 if var2 < 2 else 0):
                break
            var4 = (var2 - 1)
            var9 = ((var2 - 1) & 3)
            var1 = 1
            if (1 if (var2 - 2) >= 3 else 0):
                var10 = (var4 & -4)
                var4 = 0
                while True:  # loop $label1
                    i32_store(((var1 << 2) + 9147392), i32_load8_u((var6 + ((var1 * var2) + var3))))
                    var7 = (var1 + 1)
                    i32_store((((var1 + 1) << 2) + 9147392), i32_load8_u((var6 + ((var2 * var7) + var3))))
                    var7 = (var1 + 2)
                    i32_store((((var1 + 2) << 2) + 9147392), i32_load8_u((var6 + ((var2 * var7) + var3))))
                    var7 = (var1 + 3)
                    i32_store((((var1 + 3) << 2) + 9147392), i32_load8_u((var6 + ((var2 * var7) + var3))))
                    var1 = (var1 + 4)
                    var4 = (var4 + 4)
                    if (1 if (var4 + 4) != var10 else 0):
                        continue
                    break  # end loop
            var4 = 0
            if (1 if var9 == 0 else 0):
                break
            while True:  # loop $label2
                i32_store(((var1 << 2) + 9147392), i32_load8_u((var6 + ((var1 * var2) + var3))))
                var1 = (var1 + 1)
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != var9 else 0):
                    continue
                break  # end loop
            var1 = i32_load8_u(var8 + 283972)
            var2 = i32_load8_u((var8 + 283974))
            var4 = i32_load8_u((var8 + 283973))
            i32_store(var5 + 12, var0)
            i32_store(var5 + 4, var8)
            i32_store(var5, var3)
            i32_store(var5 + 8, ((var2 | (var4 << 8)) | (var1 << 16)))
            var3 = (var3 + 1)
            var2 = i32_load(9142892)
            if (1 if (var3 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    global global0
    global0 = (var5 + 16)


# ==========================================================
# $func748
# ==========================================================
def func748(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var2 = i32_load(9671128)
    var3 = i32_load(var0 + 32)
    var1 = (i32_load(9671128) + (i32_load(var0 + 32) * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 125) != 3 else 0):
        if (1 if i32_load(var1 + 64) < i32_load(var1 + 68) else 0):
            break
        if (1 if i32_load(var0 + 96) == 0 else 0):
            break
        break
    if i32_load(var0 + 96):
        break
    var1 = (var2 + (var3 * 132))
    var1 = func243(i32_load16_u((var2 + (var3 * 132)) + 112), i32_load16_u(var1 + 114), i32_load16_u(var0 + 110))
    if (1 if func243(i32_load16_u((var2 + (var3 * 132)) + 112), i32_load16_u(var1 + 114), i32_load16_u(var0 + 110)) == 0 else 0):
        return 1
    i32_store(var0 + 32, var1)
    return 0

