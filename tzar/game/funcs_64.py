"""
Auto-generated from WAT. Contains 12 functions.
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
# $hc
# Export: hc
# ==========================================================
def hc(var0, var1, var2):
    """Export: hc"""
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var4 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var7 = i32_load(9561704)
    if (1 if i32_load(9561704) == 0 else 0):
        break
    var5 = i32_load(9561696)
    while True:  # loop $label2
        var6 = ((var3 << 2) + var5)
        if (1 if i32_load(((var3 << 2) + var5) + 4) >= var0 else 0):
            break
        var3 = (i32_load(var6 + 8) + var3)
        if (1 if (i32_load(var6 + 8) + var3) < var7 else 0):
            continue
        break  # end loop
    var3 = 0
    var1 = (var1 + 10)
    var0 = 0
    while True:  # loop $label3
        var6 = ((var0 << 2) + var5)
        if (1 if var1 > i32_load(((var0 << 2) + var5) + 4) else 0):
            var0 = (i32_load(var6 + 8) + var0)
            if (1 if (i32_load(var6 + 8) + var0) < var7 else 0):
                continue
            break
        break  # end loop
    if (1 if var0 <= var3 else 0):
        break
    i32_store(var4 + 8, var2)
    i32_store(var4 + 4, (var0 - var3))
    i32_store(var4, (var5 + (var3 << 2)))
    global global0
    global0 = (var4 + 16)


# ==========================================================
# $uc
# Export: uc
# ==========================================================
def uc():
    """Export: uc"""
    var0 = 0
    var0 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(var0, i32_load(9561808))
    i32_store(var0 + 4, i32_load(9561816))
    global global0
    global0 = (var0 + 16)


# ==========================================================
# $sb
# Export: sb
# ==========================================================
def sb(var0):
    """Export: sb"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var1 = ((var0 * 404) + 9568096)
    var4 = i32_load(((var0 * 404) + 9568096) + 196)
    var5 = i32_load(var1 + 264)
    if (1 if i32_load(var1 + 264) != 3 else 0):
        break
    var3 = i32_load(var1 + 180)
    if (1 if i32_load(var1 + 180) == 0 else 0):
        break
    var1 = (var3 + 8)
    break
    var1 = (var1 + 144)
    var3 = -48
    var0 = ((var0 * 404) + 9568096)
    var6 = i32_load(((var0 * 404) + 9568096) + 84)
    var0 = i32_load(var0 + 148)
    var1 = i32_load(var1)
    i32_store(var2 + 16, (1 if var5 == 3 else 0))
    i32_store(var2 + 12, var0)
    i32_store(var2 + 8, var6)
    i32_store(var2 + 4, (var1 * var3))
    i32_store(var2, var4)
    global global0
    global0 = (var2 + 32)
    return var2


# ==========================================================
# $yd
# Export: yd
# ==========================================================
def yd(var0):
    """Export: yd"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var1 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var2 = ((var0 * 404) + 9568096)
    var3 = i32_load(((var0 * 404) + 9568096) + 92)
    var5 = i64_load(var2 + 104)
    var4 = i32_load(var2 + 100)
    var2 = i32_load(var2 + 120)
    i32_store(var1 + 28, var0)
    i32_store(var1 + 24, 0)
    i32_store(var1 + 20, var2)
    i32_store(var1 + 16, var2)
    i32_store(var1 + 4, var4)
    i64_store(var1 + 8, var5)
    i32_store(var1, var3)
    global global0
    global0 = (var1 + 32)


# ==========================================================
# $func786
# ==========================================================
def func786(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var4 = i32_load(9142832)
    if (1 if i32_load(9142832) == 0 else 0):
        if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
            break
    var7 = i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122)
    var8 = i32_load(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 212)
    # br_table ['$label1', '$label2', '$label3']
    _br_idx = i32_load(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 212)
    break  # br_table
    var0 = i32_load(var2)
    var6 = i32_load(var3)
    var5 = (i32_load(9142440) + 2)
    if (1 if i32_load((i32_load(9142840) + ((i32_load(var2) + (((i32_load(var3) + (i32_load(9142440) + 2)) + 1) * var5)) << 2)) + 4) != 1 else 0):
        break
    break
    var0 = i32_load(var2)
    var6 = i32_load(var3)
    var5 = (i32_load(9142440) + 2)
    if (1 if (i32_load((i32_load(9142840) + ((i32_load(var2) + (((i32_load(var3) + (i32_load(9142440) + 2)) + 1) * var5)) << 2)) + 4) - 3) >= -2 else 0):
        break
    i32_store(var1 + 12, var0)
    i32_store(var1 + 8, var6)
    if (1 if func167((var1 + 12), (var1 + 8), 1, var8, i32_load(((var7 * 404) + 9568096) + 216)) == 0 else 0):
        break
    i32_store(var2, i32_load(var1 + 12))
    i32_store(var3, i32_load(var1 + 8))
    var4 = i32_load(9142832)
    if var4:
        break
    var0 = (1 if i32_load(i32_load(9142424) + 48) == 0 else 0)
    global global0
    global0 = (var1 + 16)
    return var0


# ==========================================================
# $Hd
# Export: Hd
# ==========================================================
def Hd(var0):
    """Export: Hd"""
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    i32_store(9684792, i32_load(((var0 << 2) + 9140336)))
    i32_store8(9681884, 0)
    var0 = i32_load(9142880)
    if i32_load8_u(9142916):
        i32_store(var1 + 48, var0)
        a_b()
        break
    i32_store(var1 + 40, var0)
    i64_store(var1 + 32, -4602115869219225600)
    i64_store(var1 + 24, 0)
    i64_store(var1 + 16, 0)
    a_b()
    var0 = 0
    if (1 if i32_load(9684796) == 0 else 0):
        if i32_load8_u(9142917):
            break
        var0 = i32_load(9299880)
        if i32_load(9299880):
            var0 = (var0 - 1)
            i32_store(9299880, (var0 - 1))
            var0 = i32_load((i32_load(9299872) + (var0 << 2)))
            break
        var0 = i32_load(9163776)
        var2 = (i32_load(9163776) + 1)
        i32_store(9163776, (i32_load(9163776) + 1))
        var3 = i32_load(9163784)
        if (1 if var2 < i32_load(9163784) else 0):
            break
        i32_store(var1, var3)
        a_b()
        i32_store(9163784, (i32_load(9163784) + 40000))
        i32_store(9684796, var0)
    global global0
    global0 = (var1 - -64)


# ==========================================================
# $func808
# ==========================================================
def func808(var0):
    var1 = 0
    var2 = 0.0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = i64_load(var0 + 32)
    if (1 if i64_load(var0 + 32) != 0 else 0):
        # Unknown: f64.convert_i64_u []
        # Unknown: f64.convert_i64_u []
        var2 = ((i64_load(var0 + 24) * 100.0) / var3)
        if ((1 if ((i64_load(var0 + 24) * 100.0) / var3) < 4294967296.0 else 0) & (1 if var2 >= 0.0 else 0)):
            break
        i32_store(int(var2), 0)
    global global0
    global0 = (var1 + 16)
    return var1


# ==========================================================
# $Qc
# Export: Qc
# ==========================================================
def Qc(var0):
    """Export: Qc"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var3 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var2 = i32_load(9684424)
    if var0:
        var5 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        var4 = i32_load(var2)
        while True:  # loop $label1
            if (1 if var0 != i32_load((var4 + (var1 << 2))) else 0):
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var5 else 0):
                    continue
                break
            break  # end loop
        if (1 if var1 < 0 else 0):
            break
        var0 = (var5 - 1)
        i32_store(var2 + 8, (var5 - 1))
        if (1 if var0 <= var1 else 0):
            break
        while True:  # loop $label2
            var1 = (var1 + 1)
            i32_store((var4 + (var1 << 2)), i32_load((var4 + ((var1 + 1) << 2))))
            if (1 if var1 < i32_load(var2 + 8) else 0):
                continue
            break  # end loop
        break
    i32_store(var2 + 8, 0)
    var0 = i32_load(9568088)
    var1 = i32_load(i32_load(9568088) + 104)
    var2 = i32_load(var0 + 88)
    var4 = i32_load(var0 + 96)
    i32_store(var3, i32_load(var0 + 80))
    i32_store(var3 + 4, var2)
    i32_store(var3 + 8, var4)
    i32_store(var3 + 12, var1)
    global global0
    global0 = (var3 + 16)


# ==========================================================
# $func825
# ==========================================================
def func825(var0):
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
    var1 = 3
    var7 = i32_load(9671128)
    var5 = i32_load(var0 + 32)
    var2 = (i32_load(9671128) + (i32_load(var0 + 32) * 132))
    var6 = i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 125)
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 125) != 10 else 0):
        var3 = 1
        var4 = i32_load8_u(var2 + 122)
        var1 = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 188)
        if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 188) > 3 else 0):
            break
        if var6:
            break
    var4 = i32_load8_u(var2 + 122)
    if (1 if i32_load8_u(var0 + 125) != 7 else 0):
        break
    if (1 if i32_load(38504) == var4 else 0):
        break
    if (1 if i32_load(38508) != var4 else 0):
        break
    var3 = 0
    if (1 if i32_load(38500) != var4 else 0):
        break
    var2 = (var7 + (var5 * 132))
    var6 = (i32_load(9142440) + 2)
    var2 = i32_load((i32_load(9142840) + ((i32_load16_u((var7 + (var5 * 132)) + 112) + ((((i32_load(9142440) + 2) + i32_load16_u(var2 + 114)) + 2) * var6)) << 2)) + 8)
    if (1 if i32_load((i32_load(9142840) + ((i32_load16_u((var7 + (var5 * 132)) + 112) + ((((i32_load(9142440) + 2) + i32_load16_u(var2 + 114)) + 2) * var6)) << 2)) + 8) == 0 else 0):
        break
    if (1 if var2 == i32_load(var0 + 28) else 0):
        break
    var3 = 0
    if (1 if var4 != i32_load(38528) else 0):
        if (1 if i32_load(38504) == var4 else 0):
            break
        if (1 if i32_load(38508) == var4 else 0):
            break
        var1 = func335(i32_load16_u(var0 + 112), i32_load16_u(var0 + 114), i32_load(((var1 << 2) + 9680)), var5)
        if (1 if func335(i32_load16_u(var0 + 112), i32_load16_u(var0 + 114), i32_load(((var1 << 2) + 9680)), var5) == 0 else 0):
            break
        break
    var5 = i32_load(9142440)
    var6 = (i32_load(9142440) + 3)
    var8 = (var5 + 2)
    var9 = i32_load(9142840)
    var10 = i32_load16_u(var0 + 114)
    var11 = i32_load16_u(var0 + 112)
    var12 = i32_load16_u(var0 + 110)
    var1 = 0
    while True:  # loop $label6
        var3 = var1
        var2 = (var1 << 2)
        var1 = (i32_load((((var1 << 2) | 4) + 8611904)) + var10)
        if (1 if var5 <= (i32_load((((var1 << 2) | 4) + 8611904)) + var10) else 0):
            break
        var2 = (i32_load((var2 + 8611904)) + var11)
        if (1 if var5 <= (i32_load((var2 + 8611904)) + var11) else 0):
            break
        if (1 if (var1 | var2) < 0 else 0):
            break
        var2 = i32_load((((var2 + ((var1 + var6) * var8)) << 2) + var9) + 4)
        var1 = (var7 + (i32_load((((var2 + ((var1 + var6) * var8)) << 2) + var9) + 4) * 132))
        if (1 if var4 != i32_load8_u((var7 + (i32_load((((var2 + ((var1 + var6) * var8)) << 2) + var9) + 4) * 132)) + 122) else 0):
            break
        if (1 if i32_load(var1 + 72) < 50 else 0):
            break
        if (1 if i32_load8_u(var1 + 125) == 12 else 0):
            break
        if (1 if i32_load16_u(var1 + 110) != var12 else 0):
            break
        if (1 if i32_load(var1 + 96) == 0 else 0):
            break
        var1 = (var3 + 2)
        if (1 if var3 <= 16557 else 0):
            continue
        break
        break  # end loop
    var1 = i32_load((var7 + (var2 * 132)) + 28)
    if i32_load((var7 + (var2 * 132)) + 28):
        break
    i32_store8(var0 + 129, 10)
    i32_store(var0 + 32, 0)
    var3 = 1
    return var3
    i32_store(var0 + 32, var1)
    return 0


# ==========================================================
# $Kc
# Export: Kc
# ==========================================================
def Kc():
    """Export: Kc"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var0 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var2 = 1
    if (1 if i32_load(9142892) > 1 else 0):
        while True:  # loop $label0
            var1 = (i32_load(9561692) + (var2 * 286704))
            var3 = i32_load((i32_load(9561692) + (var2 * 286704)) + 283908)
            var4 = i32_load(var1 + 284608)
            var5 = i32_load8_u((var1 + 283974))
            var6 = i32_load8_u((var1 + 283973))
            i32_store(var0 + 16, i32_load8_u(var1 + 283972))
            i32_store(var0 + 20, var6)
            i32_store(var0 + 24, var5)
            i32_store(var0, var2)
            i32_store(var0 + 4, var1)
            i32_store(var0 + 8, var4)
            i32_store(var0 + 12, (1 if var3 == i32_load(9142872) else 0))
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    global global0
    global0 = (var0 + 32)


# ==========================================================
# $Sc
# Export: Sc
# ==========================================================
def Sc(var0):
    """Export: Sc"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var3 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var4 = i32_load(9568088)
    var6 = ((i32_load(9568088) + 96) if var0 else (var4 + 80))
    i32_store(9684424, ((i32_load(9568088) + 96) if var0 else (var4 + 80)))
    var5 = i32_load(var6 + 8)
    if i32_load(var6 + 8):
        var7 = i32_load((var4 + (96 if var0 else 80)))
        var8 = i32_load(9671128)
        var2 = var5
        while True:  # loop $label1
            if (1 if i32_load8_u((var8 + (i32_load((var7 + (var1 << 2))) * 132)) + 125) == 3 else 0):
                var2 = (var2 - 1)
                i32_store(var6 + 8, (var2 - 1))
                var0 = var1
                if (1 if var1 < var2 else 0):
                    while True:  # loop $label0
                        var0 = (var0 + 1)
                        i32_store((var7 + (var0 << 2)), i32_load((var7 + ((var0 + 1) << 2))))
                        var2 = i32_load(var6 + 8)
                        if (1 if var0 < i32_load(var6 + 8) else 0):
                            continue
                        break  # end loop
                var1 = (var1 - 1)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < var2 else 0):
                continue
            break  # end loop
    if (1 if var2 != var5 else 0):
        var1 = i32_load(var4 + 88)
        var5 = i32_load(var4 + 80)
        var0 = i32_load(var4 + 96)
        i32_store(var3 + 12, i32_load(var4 + 104))
        i32_store(var3 + 8, var0)
        i32_store(var3 + 4, var1)
        i32_store(var3, var5)
    global global0
    global0 = (var3 + 16)


# ==========================================================
# $Tc
# Export: Tc
# ==========================================================
def Tc(var0):
    """Export: Tc"""
    var1 = 0
    var2 = 0
    var0 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var1 = i32_load(9684424)
    if i32_load(i32_load(9684424) + 8):
        while True:  # loop $label1
            var1 = i32_load((i32_load(9671128) + (i32_load((i32_load(var1) + (var2 << 2))) * 132)) + 40)
            if (1 if i32_load((i32_load(9671128) + (i32_load((i32_load(var1) + (var2 << 2))) * 132)) + 40) == 0 else 0):
                break
            if i32_load8_u(9142916):
                i32_store(var0 + 20, var1)
                i32_store(var0 + 16, -16711936)
                a_b()
                break
            i32_store(var0 + 4, var1)
            i32_store(var0, 0)
            a_b()
            var2 = (var2 + 1)
            var1 = i32_load(9684424)
            if (1 if (var2 + 1) < i32_load(i32_load(9684424) + 8) else 0):
                continue
            break  # end loop
    global global0
    global0 = (var0 + 32)

