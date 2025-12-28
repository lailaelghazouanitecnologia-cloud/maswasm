"""
Auto-generated from WAT. Contains 8 functions.
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
# $func711
# ==========================================================
def func711(var0):
    var1 = 0
    var2 = 0
    i32_store(9671124, 1)
    while True:  # loop $label0
        var2 = (var1 << 2)
        var0 = ((i32_load(((var1 << 2) + 1312)) * 132) + 9216080)
        i32_store(((i32_load(((var1 << 2) + 1312)) * 132) + 9216080) + 116, 0)
        i32_store(var0 + 16, 0)
        i32_store16(var0 + 21, 0)
        i64_store(var0 + 124, 0)
        i32_store((var2 + 9263072), var0)
        i32_store8(var0 + 24, (1 if var1 > 7 else 0))
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != 28 else 0):
            continue
        break  # end loop
    i32_store(9671120, 28)


# ==========================================================
# $sd
# Export: sd
# ==========================================================
def sd(var0):
    """Export: sd"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var5 = i32_load(9142892)
    var1 = func26(((i32_load(9142892) << 2) - -64))
    i32_store(func26(((i32_load(9142892) << 2) - -64)) + 16, 558088)
    i64_store(var1 + 8, -9151314443236311040)
    i64_store(var1, -72056494543012096)
    var2 = i32_load8_u(9142916)
    i64_store(var1 + 56, 4294901760)
    i64_store(var1 + 48, -280379750529536)
    i64_store(var1 + 40, 37300399396394132)
    i32_store(var1 + 36, -1)
    i32_store8(var1 + 35, 1)
    i32_store(var1 + 31, -130)
    i64_store(var1 + 23, -3452718337)
    var2 = (12 if var2 else 75)
    i32_store8(var1 + 22, (12 if var2 else 75))
    i32_store8(var1 + 21, var2)
    i32_store8(var1 + 20, var2)
    if (1 if var5 == 0 else 0):
        break
    var4 = i32_load(9561692)
    if (1 if var0 == 0 else 0):
        var2 = 16
        while True:  # loop $label1
            var6 = (var4 + (var3 * 286704))
            var7 = i32_load16_u((var4 + (var3 * 286704)) + 283972)
            var0 = (var1 + (var2 << 2))
            i32_store8((var1 + (var2 << 2)) + 2, i32_load8_u((var6 + 283974)))
            i32_store16(var0, var7)
            i32_store8(var0 + 3, 255)
            var2 = (var2 + 1)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var5 else 0):
                continue
            break  # end loop
        break
    if i32_load8_u(9147152):
        var2 = 16
        while True:  # loop $label2
            var6 = (var4 + (var3 * 286704))
            var7 = i32_load16_u((var4 + (var3 * 286704)) + 283972)
            var0 = (var1 + (var2 << 2))
            i32_store8((var1 + (var2 << 2)) + 2, i32_load8_u((var6 + 283974)))
            i32_store16(var0, var7)
            i32_store8(var0 + 3, 255)
            var2 = (var2 + 1)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var5 else 0):
                continue
            break  # end loop
        break
    var8 = i32_load(9143004)
    var6 = i32_load(9142872)
    var0 = i32_load8_u((var4 + 283974))
    var2 = i32_load16_u(var4 + 283972)
    i32_store8(var1 + 67, 255)
    i32_store8(var1 + 66, var0)
    i32_store16(var1 + 64, var2)
    var2 = 1
    if (1 if var5 == 1 else 0):
        break
    var0 = 17
    while True:  # loop $label4
        if (1 if var2 == var6 else 0):
            var4 = 0
            var7 = 0
            break
        var3 = i32_load8_u((var8 + (var6 + (var2 * var5))))
        var7 = (0 if i32_load8_u((var8 + (var6 + (var2 * var5)))) else -1)
        var4 = (-1 if var3 else 0)
        var9 = 0
        var3 = (var1 + (var0 << 2))
        i32_store8((var1 + (var0 << 2)), var4)
        i32_store8(var3 + 1, var7)
        i32_store8(var3 + 2, var9)
        i32_store8(var3 + 3, 255)
        var0 = (var0 + 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var5 else 0):
            continue
        break  # end loop
    return var1


# ==========================================================
# $M
# Export: M
# ==========================================================
def M(var0):
    """Export: M"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = func26(var0)
    if (1 if var0 == 0 else 0):
        break
    var4 = (var0 & 3)
    if (1 if var0 >= 4 else 0):
        var5 = (var0 & 65532)
        var0 = 0
        while True:  # loop $label1
            i32_store8((var1 + var2), (1 if i32_load(((var1 << 2) + 9147392)) != 0 else 0))
            var3 = (var1 | 1)
            i32_store8((var2 + (var1 | 1)), (1 if i32_load(((var3 << 2) + 9147392)) != 0 else 0))
            var3 = (var1 | 2)
            i32_store8((var2 + (var1 | 2)), (1 if i32_load(((var3 << 2) + 9147392)) != 0 else 0))
            var3 = (var1 | 3)
            i32_store8((var2 + (var1 | 3)), (1 if i32_load(((var3 << 2) + 9147392)) != 0 else 0))
            var1 = (var1 + 4)
            var0 = (var0 + 4)
            if (1 if (var0 + 4) != var5 else 0):
                continue
            break  # end loop
    if (1 if var4 == 0 else 0):
        break
    while True:  # loop $label2
        i32_store8((var1 + var2), (1 if i32_load(((var1 << 2) + 9147392)) != 0 else 0))
        var1 = (var1 + 1)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) != var4 else 0):
            continue
        break  # end loop
    return var2


# ==========================================================
# $Yc
# Export: Yc
# ==========================================================
def Yc(var0):
    """Export: Yc"""
    var1 = 0
    var1 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    i32_store8(59183, var0)
    if (1 if var0 == 0 else 0):
        var0 = i32_load(9142876)
        if i32_load8_u(9142916):
            i32_store(var1 + 32, var0)
            a_b()
            break
        i32_store(var1 + 24, var0)
        i64_store(var1 + 16, -4602115869219225600)
        i64_store(var1 + 8, 0)
        i64_store(var1, 0)
        a_b()
        i32_store8(9684432, 0)
        break
    var0 = i32_load(i32_load(9568088) + 28)
    global global0
    global0 = (var1 + 48)
    return var0


# ==========================================================
# $func952
# ==========================================================
def func952(var0, var1, var2):
    var3 = 0
    var3 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    if func79(var0, var1, 0):
        break
    if (1 if var1 == 0 else 0):
        break
    var1 = func440(var1, 32588)
    if (1 if func440(var1, 32588) == 0 else 0):
        break
    # Unknown: memory.fill []
    i32_store(var3 + 56, 1)
    i32_store(var3 + 20, -1)
    i32_store(var3 + 16, var0)
    i32_store(var3 + 8, var1)
    # call_indirect via table[i32_load(i32_load(var1) + 28)]
    var0 = i32_load(var3 + 32)
    if (1 if i32_load(var3 + 32) == 1 else 0):
        i32_store(var2, i32_load(var3 + 24))
    var0 = (1 if var0 == 1 else 0)
    global global0
    global0 = (var3 - -64)
    return var0


# ==========================================================
# $L
# Export: L
# ==========================================================
def L(var0):
    """Export: L"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = func26(var0)
    if (1 if var0 == 0 else 0):
        break
    var4 = (var0 & 3)
    if (1 if var0 >= 4 else 0):
        var5 = (var0 & -4)
        var0 = 0
        while True:  # loop $label1
            i32_store8((var1 + var2), i32_load(((var1 << 2) + 9147392)))
            var3 = (var1 | 1)
            i32_store8((var2 + (var1 | 1)), i32_load(((var3 << 2) + 9147392)))
            var3 = (var1 | 2)
            i32_store8((var2 + (var1 | 2)), i32_load(((var3 << 2) + 9147392)))
            var3 = (var1 | 3)
            i32_store8((var2 + (var1 | 3)), i32_load(((var3 << 2) + 9147392)))
            var1 = (var1 + 4)
            var0 = (var0 + 4)
            if (1 if (var0 + 4) != var5 else 0):
                continue
            break  # end loop
    if (1 if var4 == 0 else 0):
        break
    while True:  # loop $label2
        i32_store8((var1 + var2), i32_load(((var1 << 2) + 9147392)))
        var1 = (var1 + 1)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) != var4 else 0):
            continue
        break  # end loop
    return var2


# ==========================================================
# $J
# Export: J
# ==========================================================
def J(var0):
    """Export: J"""
    var1 = 0
    var2 = 0
    var3 = 0
    var2 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var0:
        while True:  # loop $label0
            var1 = (var1 << 2)
            i32_store((var2 + (var1 << 2)), i32_load((var1 + 9147392)))
            var3 = (var3 + 1)
            var1 = ((var3 + 1) & 65535)
            if (1 if ((var3 + 1) & 65535) < var0 else 0):
                continue
            break  # end loop
    return var2


# ==========================================================
# $K
# Export: K
# ==========================================================
def K(var0):
    """Export: K"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = func26((-1 if (1 if var0 < 0 else 0) else (var0 << 1)))
    if (1 if var0 == 0 else 0):
        break
    var4 = (var0 & 3)
    if (1 if var0 >= 4 else 0):
        var5 = (var0 & -4)
        var0 = 0
        while True:  # loop $label1
            i32_store16((var2 + (var1 << 1)), i32_load(((var1 << 2) + 9147392)))
            var3 = (var1 | 1)
            i32_store16((var2 + ((var1 | 1) << 1)), i32_load(((var3 << 2) + 9147392)))
            var3 = (var1 | 2)
            i32_store16((var2 + ((var1 | 2) << 1)), i32_load(((var3 << 2) + 9147392)))
            var3 = (var1 | 3)
            i32_store16((var2 + ((var1 | 3) << 1)), i32_load(((var3 << 2) + 9147392)))
            var1 = (var1 + 4)
            var0 = (var0 + 4)
            if (1 if (var0 + 4) != var5 else 0):
                continue
            break  # end loop
    if (1 if var4 == 0 else 0):
        break
    while True:  # loop $label2
        i32_store16((var2 + (var1 << 1)), i32_load(((var1 << 2) + 9147392)))
        var1 = (var1 + 1)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) != var4 else 0):
            continue
        break  # end loop
    return var2

