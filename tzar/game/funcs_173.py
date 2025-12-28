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
# $func129
# ==========================================================
def func129(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    if (1 if var1 < i32_load(40608) else 0):
        i32_store(40608, var1)
    if (1 if var1 > i32_load(40612) else 0):
        i32_store(40612, var1)
    var5 = (1 if var2 else -1)
    var3 = (i32_load(9147376) + (((i32_load(9142440) * var1) + var0) << 1))
    # br_table ['$label0', '$label1', '$label2', '$label1']
    _br_idx = (i32_load(i32_load(9142424) + 48) - 1)
    break  # br_table
    var4 = i32_load16_u(var3)
    if var2:
        if var4:
            break
        func257(var0, var1)
        break
    if (1 if var4 != 1 else 0):
        break
    func411(var0, var1)
    i32_store8(9142904, 1)
    i32_store16(var3, (i32_load16_u(var3) + var5))
    return
    if (1 if var2 == 0 else 0):
        break
    if i32_load16_u(var3):
        break
    func257(var0, var1)
    i32_store8(9142904, 1)
    i32_store16(var3, 1)
    return
    var4 = i32_load16_u(var3)
    if var2:
        if (1 if var4 <= 1 else 0):
            i32_store16(var3, 1)
            func257(var0, var1)
        else:
        i32_store16(i32_load16_u(var3), (var4 + var5))
        break
    var2 = (var4 + var5)
    i32_store16(var3, (var4 + var5))
    if (1 if (var2 & 65535) != 1 else 0):
        break
    func411(var0, var1)
    if i32_load8_u(9142904):
        break
    if (1 if ((i32_load16_u(var3) - 1) & 65535) > 1 else 0):
        break
    i32_store8(9142904, 1)
    return var3


# ==========================================================
# $func176
# ==========================================================
def func176(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var7 = i32_load(9561692)
    var3 = i32_load(9143004)
    var4 = i32_load(9142892)
    var5 = ((i32_load(9142892) * var1) + var0)
    var6 = (1 if var2 != 0 else 0)
    i32_store8((i32_load(9143004) + ((i32_load(9142892) * var1) + var0)), (1 if var2 != 0 else 0))
    i32_store8((var3 + ((var0 * var4) + var1)), var6)
    var6 = i32_load(9142872)
    var8 = (1 if i32_load(9142872) == var0 else 0)
    var9 = ((1 if i32_load(9142872) == var0 else 0) | (1 if var1 == var6 else 0))
    if var2:
        if (1 if var9 == 0 else 0):
            break
        var3 = 0
        var2 = (var1 if var8 else var0)
        if (1 if i32_load8_u((i32_load(9143012) + ((var1 if var8 else var0) + (var4 * var6)))) == 0 else 0):
            break
        var8 = (var7 + (var2 * 286704))
        while True:  # loop $label4
            var4 = i32_load(((var8 + (var3 << 2)) + 284636))
            if (1 if i32_load(((var8 + (var3 << 2)) + 284636)) == 0 else 0):
                break
            var2 = 0
            var6 = i32_load(var4 + 8)
            if (1 if i32_load(var4 + 8) == 0 else 0):
                break
            while True:  # loop $label3
                var5 = i32_load((i32_load(var4) + (var2 << 2)))
                if (1 if i32_load((i32_load(var4) + (var2 << 2))) == 0 else 0):
                    break
                var5 = (i32_load(9671128) + (var5 * 132))
                if i32_load((i32_load(9671128) + (var5 * 132)) + 36):
                    break
                func118(var5)
                var6 = i32_load(var4 + 8)
                var2 = (var2 + 1)
                if (1 if (var2 + 1) < var6 else 0):
                    continue
                break  # end loop
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != 255 else 0):
                continue
            break  # end loop
        var5 = ((i32_load(9142892) * var1) + var0)
        i32_store8((i32_load(9143016) + var5), 0)
        i32_store8((i32_load(9143016) + ((i32_load(9142892) * var0) + var1)), 0)
        var2 = i32_load(9143012)
        var3 = i32_load(9142892)
        var4 = ((i32_load(9142892) * var1) + var0)
        i32_store8((i32_load(9143012) + ((i32_load(9142892) * var1) + var0)), 0)
        var3 = ((var0 * var3) + var1)
        i32_store8((var2 + ((var0 * var3) + var1)), 0)
        var2 = i32_load(9143008)
        i32_store8((i32_load(9143008) + var4), 0)
        i32_store8((var2 + var3), 0)
    var2 = i32_load((var7 + (var0 * 286704)) + 281800)
    if i32_load((var7 + (var0 * 286704)) + 281800):
        i32_store((var2 + (var1 << 2)), 0)
    var1 = i32_load((var7 + (var1 * 286704)) + 281800)
    if i32_load((var7 + (var1 * 286704)) + 281800):
        i32_store((var1 + (var0 << 2)), 0)
    if var9:
        la()
        a_b()


# ==========================================================
# $func204
# ==========================================================
def func204(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    if (1 if i32_load8_u(var0 + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var0 + 128) == 0 else 0):
        break
    i32_store8(var0 + 127, 0)
    var3 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var2 + 52, var3)
        i32_store(var2 + 48, 0)
        a_b()
        break
    var4 = i32_load16_u(var0 + 110)
    i32_store(var2 + 36, var3)
    i32_store(var2 + 32, (var4 + 16))
    a_b()
    i32_store8(var0 + 128, 0)
    i32_store8(var0 + 127, 6)
    if (1 if i32_load8_u(9142916) == 0 else 0):
        break
    var3 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    i32_store(var2 + 20, var3)
    i32_store(var2 + 16, -13487182)
    a_b()
    func119((var2 + 16), var0, 0, 1)
    func156(1061, var0, 500)
    var1 = i32_load16_u(var0 + 112)
    var3 = ((i32_load16_u(var0 + 112) << 5) - i32_load(9142952))
    var3 = i32_load16_u(var0 + 114)
    var4 = ((i32_load16_u(var0 + 114) << 5) - i32_load(9142956))
    if (1 if (((((i32_load16_u(var0 + 112) << 5) - i32_load(9142952)) * var3) + (((i32_load16_u(var0 + 114) << 5) - i32_load(9142956)) * var4)) - 1) > 9000000 else 0):
        break
    var5 = i32_load(39880)
    var6 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var4 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var3) + var1) << 1)))
    if (1 if var6 == 2 else 0):
        if (1 if var4 > 1 else 0):
            break
        break
    if (1 if var4 == 0 else 0):
        break
    i32_store(var2 + 8, var3)
    i32_store(var2 + 4, var1)
    i32_store(var2, var5)
    a_b()
    func77(var0)
    global global0
    global0 = (var2 - -64)


# ==========================================================
# $hd
# Export: hd
# ==========================================================
def hd():
    """Export: hd"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var2 = 3
    if (1 if i32_load(9671136) > 3 else 0):
        while True:  # loop $label1
            var0 = (i32_load(9671128) + (var2 * 132))
            if (1 if i32_load((i32_load(9671128) + (var2 * 132)) + 28) == 0 else 0):
                break
            if (1 if i32_load(var0 + 40) == 0 else 0):
                break
            if (1 if i32_load(var0 + 64) == 0 else 0):
                if (1 if i32_load(38448) != i32_load8_u(var0 + 122) else 0):
                    break
                break
            var3 = i32_load(var0 + 48)
            var1 = i32_load(i32_load(var0 + 48) + 20)
            var4 = i32_load8_u(var0 + 124)
            if (1 if i32_load(i32_load(var0 + 48) + 20) <= i32_load8_u(var0 + 124) else 0):
                var1 = (var4 % var1)
                i32_store8(var0 + 124, ((3 if (1 if var1 < 3 else 0) else (var4 % var1)) if (1 if i32_load(38448) == i32_load8_u(var0 + 122) else 0) else var1))
            var0 = i32_load8_u(var0 + 125)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < i32_load(9671136) else 0):
                continue
            break  # end loop
    func320(1)


# ==========================================================
# $func374
# ==========================================================
def func374(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var2 = i32_load(9561692)
    if (1 if var1 == 0 else 0):
        var5 = (var2 + (var0 * 286704))
        while True:  # loop $label3
            var2 = i32_load(((var5 + (var4 << 2)) + 284636))
            if (1 if i32_load(((var5 + (var4 << 2)) + 284636)) == 0 else 0):
                break
            var0 = 0
            var1 = i32_load(var2 + 8)
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            while True:  # loop $label2
                var3 = i32_load((i32_load(var2) + (var0 << 2)))
                if (1 if i32_load((i32_load(var2) + (var0 << 2))) == 0 else 0):
                    break
                var3 = (i32_load(9671128) + (var3 * 132))
                if i32_load((i32_load(9671128) + (var3 * 132)) + 36):
                    break
                func118(var3)
                var1 = i32_load(var2 + 8)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) < var1 else 0):
                    continue
                break  # end loop
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != 255 else 0):
                continue
            break  # end loop
        break
    var5 = (var2 + (var0 * 286704))
    while True:  # loop $label8
        var2 = i32_load(((var5 + (var4 << 2)) + 284636))
        if (1 if i32_load(((var5 + (var4 << 2)) + 284636)) == 0 else 0):
            break
        var0 = 0
        var1 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        while True:  # loop $label7
            var3 = i32_load((i32_load(var2) + (var0 << 2)))
            if (1 if i32_load((i32_load(var2) + (var0 << 2))) == 0 else 0):
                break
            var3 = (i32_load(9671128) + (var3 * 132))
            if i32_load((i32_load(9671128) + (var3 * 132)) + 36):
                break
            func118(var3)
            var1 = i32_load(var2 + 8)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < var1 else 0):
                continue
            break  # end loop
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != 255 else 0):
            continue
        break  # end loop


# ==========================================================
# $func393
# ==========================================================
def func393(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var1 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    if (1 if func185(52372) == 0 else 0):
        var2 = i32_load(52424)
        if (1 if i32_load(52424) != 52368 else 0):
            while True:  # loop $label0
                var3 = i32_load(var2 + 56)
                if (1 if i32_atomic_load(var2) == 0 else 0):
                    var4 = i32_load(var2 + 52)
                    i32_store(i32_load(var2 + 52) + 56, i32_load(var2 + 56))
                    i32_store(i32_load(var2 + 56) + 52, var4)
                    func390(var2)
                var2 = var3
                if (1 if var3 != 52368 else 0):
                    continue
                break  # end loop
        func54(52372)
    var2 = e()
    if (1 if e() == 0 else 0):
        break
    var3 = e()
    if (1 if e() == 0 else 0):
        break
    i64_store(var1 + 40, 0)
    i64_store(var1 + 48, 0)
    i32_store(var1 + 60, 0)
    i64_store(var1 + 32, 0)
    i32_store(var1 + 28, var0)
    i32_store(var1 + 24, 0)
    i32_store(var1 + 20, var3)
    i32_store(var1 + 16, 128)
    i32_store(var1 + 12, 0)
    i32_store(var1 + 8, 0)
    i32_store(var1 + 4, 0)
    i32_store(var1, 0)
    i32_store(var2, i32_load(var1 + 60))
    i64_store(var2 + 20, i64_load(var1 + 48))
    i64_store(var2 + 12, i64_load(var1 + 40))
    i64_store(var2 + 4, i64_load(var1 + 32))
    i32_store(var2 + 28, i32_load(var1 + 28))
    i32_store(var2 + 32, i32_load(var1 + 24))
    i32_store(var2 + 36, i32_load(var1 + 20))
    i32_store(var2 + 40, i32_load(var1 + 16))
    i32_store(var2 + 44, i32_load(var1 + 12))
    i32_store(var2 + 48, i32_load(var1 + 8))
    i32_store(var2 + 52, i32_load(var1 + 4))
    i32_store(var2 + 56, i32_load(var1))
    var5 = var2
    global global0
    global0 = (var1 - -64)
    return var5


# ==========================================================
# $func411
# ==========================================================
def func411(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var3 = i32_load(9142840)
    var0 = (var0 + 1)
    var4 = (var1 + 1)
    var1 = (i32_load(9142440) + 2)
    var2 = i32_load((i32_load(9142840) + (((var0 + 1) + ((var1 + 1) * (i32_load(9142440) + 2))) << 2)))
    if (1 if i32_load((i32_load(9142840) + (((var0 + 1) + ((var1 + 1) * (i32_load(9142440) + 2))) << 2))) < 3 else 0):
        break
    var2 = (i32_load(9671128) + (var2 * 132))
    if i32_load(((i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122) * 404) + 9568096) + 264):
        if (1 if i32_load(i32_load(9142424) + 48) != 3 else 0):
            break
    func158(var2)
    var1 = (i32_load(9142440) + 2)
    var3 = i32_load(9142840)
    var2 = i32_load((var3 + ((var0 + ((var1 + var4) * var1)) << 2)))
    if (1 if i32_load((var3 + ((var0 + ((var1 + var4) * var1)) << 2))) < 3 else 0):
        break
    var2 = (i32_load(9671128) + (var2 * 132))
    if i32_load(((i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122) * 404) + 9568096) + 264):
        if (1 if i32_load(i32_load(9142424) + 48) != 3 else 0):
            break
    func158(var2)
    var1 = (i32_load(9142440) + 2)
    var3 = i32_load(9142840)
    var0 = i32_load((var3 + ((var0 + ((var4 + (var1 << 1)) * var1)) << 2)))
    if (1 if i32_load((var3 + ((var0 + ((var4 + (var1 << 1)) * var1)) << 2))) < 3 else 0):
        break
    var0 = (i32_load(9671128) + (var0 * 132))
    if i32_load(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 264):
        if (1 if i32_load(i32_load(9142424) + 48) != 3 else 0):
            break
    func158(var0)

