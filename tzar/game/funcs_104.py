"""
Auto-generated from WAT. Contains 5 functions.
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
# $func823
# ==========================================================
def func823(var0, var1):
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
    while True:  # loop $label6
        if (1 if i32_load(var0 + 116) <= 261 else 0):
            var2 = i32_load(var0 + 116)
            if var1:
                break
            if (1 if var2 >= 262 else 0):
                break
            return 0
            if (1 if var2 == 0 else 0):
                break
            if (1 if var2 < 3 else 0):
                break
        var4 = i32_load(var0 + 108)
        var2 = (i32_load(var0 + 84) & (i32_load8_u((i32_load(var0 + 108) + i32_load(var0 + 56)) + 2) ^ (i32_load(var0 + 72) << i32_load(var0 + 88))))
        i32_store(var0 + 72, (i32_load(var0 + 84) & (i32_load8_u((i32_load(var0 + 108) + i32_load(var0 + 56)) + 2) ^ (i32_load(var0 + 72) << i32_load(var0 + 88)))))
        var2 = (i32_load(var0 + 68) + (var2 << 1))
        var3 = i32_load16_u((i32_load(var0 + 68) + (var2 << 1)))
        i32_store16((i32_load(var0 + 64) + ((var4 & i32_load(var0 + 52)) << 1)), i32_load16_u((i32_load(var0 + 68) + (var2 << 1))))
        i32_store16(var2, var4)
        if (1 if var3 == 0 else 0):
            break
        if (1 if (i32_load(var0 + 44) - 262) < (var4 - var3) else 0):
            break
        var3 = func359(var0, var3)
        i32_store(var0 + 96, func359(var0, var3))
        break
        var3 = i32_load(var0 + 96)
        if (1 if var3 >= 3 else 0):
            var2 = i32_load(var0 + 5792)
            i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
            var4 = (i32_load(var0 + 108) - i32_load(var0 + 112))
            i32_store8((var2 + i32_load(var0 + 5784)), (i32_load(var0 + 108) - i32_load(var0 + 112)))
            var2 = i32_load(var0 + 5792)
            i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
            i32_store8((var2 + i32_load(var0 + 5784)), ((var4 & 0xFFFFFFFF) >> 8))
            var2 = i32_load(var0 + 5792)
            i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
            var2 = (var3 - 3)
            i32_store8((var2 + i32_load(var0 + 5784)), (var3 - 3))
            var2 = (((i32_load8_u(((var2 & 255) + 23984)) << 2) + var0) + 1176)
            i32_store16((((i32_load8_u(((var2 & 255) + 23984)) << 2) + var0) + 1176), (i32_load16_u(var2) + 1))
            var2 = ((var4 - 1) & 65535)
            var2 = ((var0 + (i32_load8_u(((((var4 - 1) & 65535) if (1 if var2 < 256 else 0) else (((var2 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2440)
            i32_store16(((var0 + (i32_load8_u(((((var4 - 1) & 65535) if (1 if var2 < 256 else 0) else (((var2 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2440), (i32_load16_u(var2) + 1))
            var3 = i32_load(var0 + 96)
            var2 = (i32_load(var0 + 116) - i32_load(var0 + 96))
            i32_store(var0 + 116, (i32_load(var0 + 116) - i32_load(var0 + 96)))
            var8 = i32_load(var0 + 5796)
            var9 = i32_load(var0 + 5792)
            if (1 if var3 > i32_load(var0 + 128) else 0):
                break
            if (1 if var2 < 3 else 0):
                break
            var6 = (var3 - 1)
            i32_store(var0 + 96, (var3 - 1))
            var7 = i32_load(var0 + 72)
            var3 = i32_load(var0 + 108)
            var10 = i32_load(var0 + 52)
            var11 = i32_load(var0 + 64)
            var12 = i32_load(var0 + 68)
            var13 = i32_load(var0 + 84)
            var14 = i32_load(var0 + 56)
            var5 = i32_load(var0 + 88)
            while True:  # loop $label5
                var2 = var3
                var3 = (var3 + 1)
                i32_store(var0 + 108, (var3 + 1))
                var7 = ((i32_load8_u((var2 + var14) + 3) ^ (var7 << var5)) & var13)
                i32_store(var0 + 72, ((i32_load8_u((var2 + var14) + 3) ^ (var7 << var5)) & var13))
                var4 = (var12 + (var7 << 1))
                i32_store16((var11 + ((var3 & var10) << 1)), i32_load16_u((var12 + (var7 << 1))))
                i32_store16(var4, var3)
                var6 = (var6 - 1)
                i32_store(var0 + 96, (var6 - 1))
                if var6:
                    continue
                break  # end loop
            var3 = (var2 + 2)
            i32_store(var0 + 108, (var2 + 2))
            if (1 if var8 != var9 else 0):
                continue
            break
            i32_store(var0 + 96, 0)
            var3 = (i32_load(var0 + 108) + var3)
            i32_store(var0 + 108, (i32_load(var0 + 108) + var3))
            var4 = (i32_load(var0 + 56) + var3)
            var2 = i32_load8_u((i32_load(var0 + 56) + var3))
            i32_store(var0 + 72, i32_load8_u((i32_load(var0 + 56) + var3)))
            i32_store(var0 + 72, (i32_load(var0 + 84) & (i32_load8_u(var4 + 1) ^ (var2 << i32_load(var0 + 88)))))
            if (1 if var8 != var9 else 0):
                continue
            break
        var3 = i32_load8_u((i32_load(var0 + 56) + i32_load(var0 + 108)))
        var2 = i32_load(var0 + 5792)
        i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
        i32_store8((var2 + i32_load(var0 + 5784)), 0)
        var2 = i32_load(var0 + 5792)
        i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
        i32_store8((var2 + i32_load(var0 + 5784)), 0)
        var2 = i32_load(var0 + 5792)
        i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
        i32_store8((var2 + i32_load(var0 + 5784)), var3)
        var2 = (var0 + (var3 << 2))
        i32_store16(((var0 + (var3 << 2)) + 148), (i32_load16_u(var2 + 148) + 1))
        i32_store(var0 + 116, (i32_load(var0 + 116) - 1))
        var3 = (i32_load(var0 + 108) + 1)
        i32_store(var0 + 108, (i32_load(var0 + 108) + 1))
        if (1 if i32_load(var0 + 5792) != i32_load(var0 + 5796) else 0):
            continue
        var6 = 0
        var2 = i32_load(var0 + 92)
        if (1 if i32_load(var0 + 92) >= 0 else 0):
        else:
        i32_store(var0 + 92, i32_load(var0 + 108))
        var5 = i32_load(var0)
        var4 = i32_load(i32_load(var0) + 28)
        var3 = i32_load(var4 + 20)
        var2 = i32_load(var5 + 16)
        var3 = (i32_load(var4 + 20) if (1 if var2 > var3 else 0) else i32_load(var5 + 16))
        if (1 if (i32_load(var4 + 20) if (1 if var2 > var3 else 0) else i32_load(var5 + 16)) == 0 else 0):
            break
        i32_store(var5 + 12, (i32_load(var5 + 12) + var3))
        i32_store(var4 + 16, (i32_load(var4 + 16) + var3))
        i32_store(var5 + 20, (i32_load(var5 + 20) + var3))
        i32_store(var5 + 16, (i32_load(var5 + 16) - var3))
        var2 = i32_load(var4 + 20)
        i32_store(var4 + 20, (i32_load(var4 + 20) - var3))
        if (1 if var2 != var3 else 0):
            break
        i32_store(var4 + 16, i32_load(var4 + 8))
        if i32_load(i32_load(var0) + 16):
            continue
        break  # end loop
    return 0
    var2 = i32_load(var0 + 108)
    i32_store(var0 + 5812, (2 if (1 if var2 >= 2 else 0) else i32_load(var0 + 108)))
    if (1 if var1 == 4 else 0):
        var6 = 0
        var1 = i32_load(var0 + 92)
        if (1 if i32_load(var0 + 92) >= 0 else 0):
        else:
        i32_store(var0 + 92, i32_load(var0 + 108))
        var4 = i32_load(var0)
        var3 = i32_load(i32_load(var0) + 28)
        var2 = i32_load(var3 + 20)
        var1 = i32_load(var4 + 16)
        var2 = (i32_load(var3 + 20) if (1 if var1 > var2 else 0) else i32_load(var4 + 16))
        if (1 if (i32_load(var3 + 20) if (1 if var1 > var2 else 0) else i32_load(var4 + 16)) == 0 else 0):
            break
        i32_store(var4 + 12, (i32_load(var4 + 12) + var2))
        i32_store(var3 + 16, (i32_load(var3 + 16) + var2))
        i32_store(var4 + 20, (i32_load(var4 + 20) + var2))
        i32_store(var4 + 16, (i32_load(var4 + 16) - var2))
        var1 = i32_load(var3 + 20)
        i32_store(var3 + 20, (i32_load(var3 + 20) - var2))
        if (1 if var1 != var2 else 0):
            break
        i32_store(var3 + 16, i32_load(var3 + 8))
        return (3 if i32_load(i32_load(var0) + 16) else 2)
    if (1 if i32_load(var0 + 5792) == 0 else 0):
        break
    var6 = 0
    var1 = i32_load(var0 + 92)
    if (1 if i32_load(var0 + 92) >= 0 else 0):
    else:
    i32_store(var0 + 92, i32_load(var0 + 108))
    var4 = i32_load(var0)
    var3 = i32_load(i32_load(var0) + 28)
    var2 = i32_load(var3 + 20)
    var1 = i32_load(var4 + 16)
    var2 = (i32_load(var3 + 20) if (1 if var1 > var2 else 0) else i32_load(var4 + 16))
    if (1 if (i32_load(var3 + 20) if (1 if var1 > var2 else 0) else i32_load(var4 + 16)) == 0 else 0):
        break
    i32_store(var4 + 12, (i32_load(var4 + 12) + var2))
    i32_store(var3 + 16, (i32_load(var3 + 16) + var2))
    i32_store(var4 + 20, (i32_load(var4 + 20) + var2))
    i32_store(var4 + 16, (i32_load(var4 + 16) - var2))
    var1 = i32_load(var3 + 20)
    i32_store(var3 + 20, (i32_load(var3 + 20) - var2))
    if (1 if var1 != var2 else 0):
        break
    i32_store(var3 + 16, i32_load(var3 + 8))
    if i32_load(i32_load(var0) + 16):
        break
    return 0
    return 1


# ==========================================================
# $func832
# ==========================================================
def func832(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var6 = i32_load(var0)
    if (1 if i32_load(var0) < i32_load(59176) else 0):
        var4 = i32_load(9561704)
        if i32_load(9561704):
            var0 = 0
            var5 = i32_load(9561696)
            while True:  # loop $label1
                var3 = ((var0 << 2) + var5)
                if (1 if var6 <= i32_load(((var0 << 2) + var5) + 4) else 0):
                    var3 = (var4 - var0)
                    break
                var0 = (i32_load(var3 + 8) + var0)
                if (1 if var4 > (i32_load(var3 + 8) + var0) else 0):
                    continue
                break  # end loop
            var3 = 0
        func71((var5 + (var0 << 2)), 0, var3, 59176, 1, 1)
        break
    func71(35, 0, 0, 59176, 1, 1)
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) >= 2 else 0):
        var5 = i32_load(9561692)
        var0 = 1
        while True:  # loop $label4
            if (1 if i32_load((var1 + (var0 << 2))) == 0 else 0):
                break
            var3 = (var5 + (var0 * 286704))
            if i32_load((var5 + (var0 * 286704)) + 284616):
                break
            i32_store((var3 + 284616), i32_load(var3 + 284628))
            i32_store8(var3 + 286699, 0)
            var4 = i32_load(var3 + 283908)
            var3 = i32_load8_u(var3 + 286696)
            i32_store(var2 + 8, 0)
            i32_store(var2 + 4, var3)
            i32_store(var2, var4)
            a_b()
            var4 = i32_load(9142892)
            var5 = i32_load(9561692)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < var4 else 0):
                continue
            break  # end loop
    global global0
    global0 = (var2 + 16)
    return var2


# ==========================================================
# $Z
# Export: Z
# ==========================================================
def Z(var0, var1):
    """Export: Z"""
    var2 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var0 = (i32_load(9561692) + (var0 * 286704))
    var1 = ((i32_load(var0 + 283960) + var1) & 3)
    i32_store((i32_load(9561692) + (var0 * 286704)) + 283960, ((i32_load(var0 + 283960) + var1) & 3))
    if i32_load8_u(9147210):
        i32_store(var2, i32_load(var0 + 283908))
        i32_store(var2 + 4, ((i32_load8_u((var0 + 283974)) | (i32_load8_u((var0 + 283973)) << 8)) | (i32_load8_u(var0 + 283972) << 16)))
        i32_store(var2 + 8, i32_load(var0 + 284608))
        var0 = (var0 + 283960)
        i32_store(var2 + 12, i32_load((var0 + 283960)))
        func71(16, 0, 0, var2, 4, 1)
        var1 = i32_load(var0)
    global global0
    global0 = (var2 + 16)
    return var1


# ==========================================================
# $_
# Export: _
# ==========================================================
def _(var0, var1):
    """Export: _"""
    var2 = 0
    var3 = 0
    var4 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var0 = (i32_load(9561692) + (var0 * 286704))
    i32_store8((i32_load(9561692) + (var0 * 286704)) + 283972, ((var1 & 0xFFFFFFFF) >> 16))
    var3 = (var0 + 283974)
    i32_store8((var0 + 283974), var1)
    var4 = (var0 + 283973)
    i32_store8((var0 + 283973), ((var1 & 0xFFFFFFFF) >> 8))
    if i32_load8_u(9147210):
        i32_store(var2, i32_load(var0 + 283908))
        i32_store(var2 + 4, ((i32_load8_u(var3) | (i32_load8_u(var4) << 8)) | (i32_load8_u((var0 + 283972)) << 16)))
        i32_store(var2 + 8, i32_load(var0 + 284608))
        i32_store(var2 + 12, i32_load(var0 + 283960))
        func71(16, 0, 0, var2, 4, 1)
    global global0
    global0 = (var2 + 16)


# ==========================================================
# $Y
# Export: Y
# ==========================================================
def Y(var0, var1):
    """Export: Y"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var5 = i32_load(9561692)
    var3 = (i32_load(9561692) + (var0 * 286704))
    var6 = i32_load((i32_load(9561692) + (var0 * 286704)) + 284608)
    if ((1 if i32_load((i32_load(9561692) + (var0 * 286704)) + 284608) == 0 else 0) & (1 if var1 < 0 else 0)):
        break
    var3 = (var3 + 284608)
    var4 = ((var1 + var6) % 17)
    i32_store((var3 + 284608), ((var1 + var6) % 17))
    if (1 if i32_load8_u(9147210) == 0 else 0):
        break
    var0 = (var5 + (var0 * 286704))
    i32_store(var2, i32_load((var5 + (var0 * 286704)) + 283908))
    i32_store(var2 + 4, ((i32_load8_u((var0 + 283974)) | (i32_load8_u((var0 + 283973)) << 8)) | (i32_load8_u(var0 + 283972) << 16)))
    i32_store(var2 + 8, i32_load(var3))
    i32_store(var2 + 12, i32_load(var0 + 283960))
    func71(16, 0, 0, var2, 4, 1)
    var4 = i32_load(var3)
    global global0
    global0 = (var2 + 16)
    return var4

