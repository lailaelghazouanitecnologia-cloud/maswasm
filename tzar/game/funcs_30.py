"""
Auto-generated from WAT. Contains 20 functions.
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
# $_c
# Export: _c
# ==========================================================
def _c(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9):
    """Export: _c"""
    var10 = 0
    var10 = i32_load(9568088)
    i32_store(i32_load(9568088) + 36, var6)
    i32_store(var10 + 32, var5)
    i32_store(var10 + 16, var4)
    i32_store(var10 + 12, var3)
    i32_store(var10 + 8, var2)
    i32_store(var10 + 4, var1)
    i32_store(var10, var0)
    i32_store8(var10 + 45, var8)
    i32_store(var10 + 28, var7)
    i32_store8(var10 + 44, var9)


# ==========================================================
# $Td
# Export: Td
# ==========================================================
def Td():
    """Export: Td"""
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
    var10 = 0
    var11 = 0
    var12 = 0
    var13 = 0
    var14 = 0
    while True:  # loop $label2
        var0 = ((var3 * 404) + 9568096)
        # br_table ['$label0', '$label1', '$label1', '$label1', '$label0', '$label1']
        _br_idx = i32_load(((var3 * 404) + 9568096) + 264)
        break  # br_table
        if i32_load8_u(var0 + 354):
            break
        var6 = i32_load(var0 + 116)
        var7 = i32_load(var0 + 68)
        var8 = i32_load(var0 + 120)
        var9 = i32_load(var0 + 100)
        var4 = i32_load(var0 + 92)
        var10 = i32_load(var0 + 104)
        var11 = i32_load(var0 + 72)
        var12 = i32_load(var0 + 76)
        var5 = i32_load(var0 + 276)
        if i32_load(var0 + 276):
        else:
        var13 = 0
        var14 = i32_load(var0 + 224)
        var1 = ((var2 * 52) + 9147392)
        i32_store(((var2 * 52) + 9147392) + 48, i32_load(var0 + 260))
        i32_store(var1 + 44, var14)
        i32_store(var1 + 40, var13)
        i32_store(var1 + 36, var5)
        i32_store(var1 + 32, var6)
        i32_store(var1 + 28, var11)
        i32_store(var1 + 24, var12)
        i32_store(var1 + 20, var7)
        i32_store(var1 + 16, var8)
        i32_store(var1 + 12, var9)
        i32_store(var1 + 8, var4)
        i32_store(var1 + 4, var10)
        i32_store(var1, var3)
        var2 = (var2 + 1)
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != 255 else 0):
            continue
        break  # end loop
    return (var2 * 13)


# ==========================================================
# $Ib
# Export: Ib
# ==========================================================
def Ib(var0, var1, var2):
    """Export: Ib"""
    var3 = 0
    var0 = ((var2 * 404) + 9568096)
    if (1 if var0 != i32_load(((var2 * 404) + 9568096) + 196) else 0):
        break
    if (1 if i32_load(var0 + 264) != var1 else 0):
        break
    var0 = ((var2 * 404) + 9568096)
    if (1 if i32_load(((var2 * 404) + 9568096) + 188) == 55 else 0):
        break
    if (1 if i32_load(38528) == var2 else 0):
        break
    if (1 if i32_load(38768) != var2 else 0):
        break
    if i32_load8_u(var0 + 378):
        break
    var3 = i32_load(((var2 * 404) + 9568096) + 84)
    return var3


# ==========================================================
# $ob
# Export: ob
# ==========================================================
def ob(var0, var1):
    """Export: ob"""
    if var1:
        var0 = ((i32_load(9681816) + var0) & 3)
        i32_store(9681816, ((i32_load(9681816) + var0) & 3))
        return var0
    var0 = ((i32_load(9681820) + var0) & 3)
    i32_store(9681820, ((i32_load(9681820) + var0) & 3))
    return var0


# ==========================================================
# $func506
# ==========================================================
def func506(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var1 = 1
    var2 = i32_load(9671128)
    var3 = i32_load(var0 + 32)
    var4 = (i32_load(9671128) + (i32_load(var0 + 32) * 132))
    var5 = i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 125)
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 125) == 3 else 0):
        break
    if i32_load8_u((i32_load(9143004) + (i32_load16_u(var0 + 110) + (i32_load(9142892) * i32_load16_u(var4 + 110))))):
        break
    # br_table ['$label0', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label0', '$label1']
    _br_idx = (var5 - 4)
    break  # br_table
    var0 = i32_load8_u((var2 + (var3 * 132)) + 122)
    if (1 if i32_load8_u((var2 + (var3 * 132)) + 122) == i32_load(38552) else 0):
        break
    if (1 if i32_load(38892) == var0 else 0):
        break
    if (1 if i32_load(38816) == var0 else 0):
        break
    if (1 if i32_load(38872) == var0 else 0):
        break
    if (1 if i32_load(38584) == var0 else 0):
        break
    if (1 if i32_load(38796) != var0 else 0):
        break
    var1 = 0
    return var1


# ==========================================================
# $func518
# ==========================================================
def func518(var0, var1, var2, var3, var4):
    var2 = i32_load(9671128)
    var1 = i32_load(var1)
    var3 = ((1 if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 122) * 404) + 9568096) + 304) == 0 else 0) & var4)
    if (1 if ((1 if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 122) * 404) + 9568096) + 304) == 0 else 0) & var4) == 0 else 0):
        break
    var0 = i32_load((var2 + (var0 * 132)) + 44)
    if (1 if i32_load((var2 + (var0 * 132)) + 44) == 0 else 0):
        break
    var2 = i32_load(9215884)
    if (1 if i32_load((i32_load(9215884) + (var0 << 4)) + 4) != 46 else 0):
        break
    i32_store((var2 + ((var0 << 4) | 12)), var1)
    return var3


# ==========================================================
# $ma
# Export: ma
# ==========================================================
def ma(var0, var1, var2, var3, var4):
    """Export: ma"""
    i32_store8(9561804, (1 if var3 != 0 else 0))
    i32_store8(9561803, (1 if var2 != 0 else 0))
    i32_store8(9561802, (1 if var1 != 0 else 0))
    i32_store8(9561800, (1 if var0 != 0 else 0))
    i32_store8(9561801, (1 if var4 != 0 else 0))


# ==========================================================
# $func548
# ==========================================================
def func548(var0, var1, var2, var3, var4):
    var1 = i32_load(var1)
    var2 = (i32_load(9671128) + (i32_load(var1) * 132))
    return (((1 if i32_load8_u(((i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 122) * 404) + 9568096) + 352) == 0 else 0) | (1 if var0 == var1 else 0)) | (1 if i32_load16_u(var2 + 110) == 0 else 0))


# ==========================================================
# $db
# Export: db
# ==========================================================
def db(var0, var1, var2, var3):
    """Export: db"""
    var4 = 0
    if (1 if var0 == 54 else 0):
        break
    if i32_load8_u(((var0 * 404) + 9568096) + 378):
        break
    if var1:
        if (1 if (i32_load(((var0 * 404) + 9568096) + 264) & -5) == 0 else 0):
            break
        break
    if var2:
        if (1 if i32_load(((var0 * 404) + 9568096) + 264) != 1 else 0):
            break
    if (1 if var3 == 0 else 0):
        break
    if (1 if i32_load(((var0 * 404) + 9568096) + 264) != 2 else 0):
        break
    var4 = (i32_load(((var0 * 404) + 9568096) + 144) * -48)
    return var4


# ==========================================================
# $cb
# Export: cb
# ==========================================================
def cb(var0, var1, var2, var3):
    """Export: cb"""
    if var1:
        var0 = ((var0 * 404) + 9568096)
        if (i32_load(((var0 * 404) + 9568096) + 264) & -5):
            var1 = 0
            if (1 if var2 == 0 else 0):
                break
        var1 = -48
        break
    if var2:
        var1 = 0
        if (1 if i32_load(((var0 * 404) + 9568096) + 264) != 1 else 0):
            break
    if var3:
        var1 = 0
        var2 = ((var0 * 404) + 9568096)
        if (1 if i32_load(((var0 * 404) + 9568096) + 264) != 3 else 0):
            break
        if (1 if i32_load(var2 + 368) == 55 else 0):
            break
    var0 = i32_load(((var0 * 404) + 9568096) + 180)
    if (1 if i32_load(((var0 * 404) + 9568096) + 180) == 0 else 0):
        return 0
    var1 = 48
    var0 = (var0 + 8)
    var1 = (i32_load(var0) * var1)
    return var1


# ==========================================================
# $sa
# Export: sa
# ==========================================================
def sa(var0, var1, var2, var3, var4, var5, var6):
    """Export: sa"""
    i32_store8(59184, var1)
    i32_store(59168, var0)
    i32_store8(59185, var2)
    i32_store(9561840, var3)
    i32_store8(9142916, var4)
    i32_store8(9142917, var5)
    i32_store8(9142918, var6)


# ==========================================================
# $wc
# Export: wc
# ==========================================================
def wc(var0, var1, var2, var3, var4):
    """Export: wc"""
    var4 = (i32_load(9561692) + (var4 * 286704))
    i32_store((i32_load(9561692) + (var4 * 286704)) + 283848, (i32_load(var4 + 283848) + var0))
    var0 = (var4 + 283852)
    i32_store((var4 + 283852), (i32_load(var0) + var1))
    var0 = (var4 + 283856)
    i32_store((var4 + 283856), (i32_load(var0) + var2))
    var0 = (var4 + 283860)
    i32_store((var4 + 283860), (i32_load(var0) + var3))


# ==========================================================
# $xc
# Export: xc
# ==========================================================
def xc(var0, var1):
    """Export: xc"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var3 = i32_load(9142844)
    if (1 if i32_load(9142844) < 4 else 0):
        break
    var4 = i32_load(9671128)
    var2 = 3
    while True:  # loop $label1
        var5 = (var4 + (var2 * 132))
        if (1 if var0 == i32_load16_u((var4 + (var2 * 132)) + 110) else 0):
            if (1 if i32_load8_u(var5 + 122) == var1 else 0):
                break
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var3 else 0):
            continue
        break  # end loop
    return 0
    return var2


# ==========================================================
# $ad
# Export: ad
# ==========================================================
def ad(var0, var1, var2):
    """Export: ad"""
    if (1 if var0 >= 0 else 0):
        i32_store(i32_load(9568076) + 108, var0)
    if (1 if var1 >= 0 else 0):
        i32_store(i32_load(9568076) + 112, var1)
    if (1 if var2 >= 0 else 0):
        i32_store(i32_load(9568076) + 116, var2)


# ==========================================================
# $func650
# ==========================================================
def func650(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var2 = 0
    var3 = i32_load(9561692)
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var5 = i32_load(59164)
    var1 = 1
    while True:  # loop $label1
        if (1 if var5 == i32_load((var3 + (var1 * 286704)) + 284616) else 0):
            var2 = var1
            break
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var4 else 0):
            continue
        break  # end loop
    i32_store((var3 + (var2 * 286704)) + 286692, i32_load(var0))


# ==========================================================
# $ea
# Export: ea
# ==========================================================
def ea(var0):
    """Export: ea"""
    var1 = 0
    var2 = 0
    var3 = 0
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var3 = i32_load(9561692)
    var1 = 1
    while True:  # loop $label1
        if (1 if i32_load((var3 + (var1 * 286704)) + 284616) == var0 else 0):
            break
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var2 else 0):
            continue
        break  # end loop
    var1 = 0
    return var1


# ==========================================================
# $ja
# Export: ja
# ==========================================================
def ja(var0, var1, var2, var3):
    """Export: ja"""
    var4 = 0
    var5 = 0
    var6 = 0
    var6 = i32_load(9142892)
    if (1 if i32_load(9142892) >= 2 else 0):
        var5 = i32_load(9561692)
        var4 = 1
        while True:  # loop $label1
            if (1 if i32_load((var5 + (var4 * 286704)) + 284616) == var0 else 0):
                break
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var6 else 0):
                continue
            break  # end loop
        return 0
        var0 = (var5 + (var4 * 286704))
        i32_store8((var5 + (var4 * 286704)) + 283972, var1)
        i32_store8((var0 + 283974), var3)
        i32_store8((var0 + 283973), var2)
    return var4


# ==========================================================
# $ia
# Export: ia
# ==========================================================
def ia(var0, var1):
    """Export: ia"""
    var2 = 0
    var3 = 0
    var4 = 0
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) >= 2 else 0):
        var3 = i32_load(9561692)
        var2 = 1
        while True:  # loop $label1
            if (1 if i32_load((var3 + (var2 * 286704)) + 284616) == var0 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var4 else 0):
                continue
            break  # end loop
        return 0
        i32_store((var3 + (var2 * 286704)) + 283960, var1)
    return var2


# ==========================================================
# $func655
# ==========================================================
def func655(var0, var1, var2, var3, var4):
    var5 = 0
    var3 = 1
    var2 = i32_load(9671128)
    var4 = i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122)
    if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 136) == 0 else 0):
        break
    var1 = i32_load(var1)
    var5 = i32_load8_u((var2 + (i32_load(var1) * 132)) + 122)
    if (1 if i32_load(((i32_load8_u((var2 + (i32_load(var1) * 132)) + 122) * 404) + 9568096) + 208) == 0 else 0):
        if (1 if i32_load(((var4 * 404) + 9568096) + 208) == 2 else 0):
            break
    if (1 if i32_load(9142848) >= (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        break
    var1 = i32_load((var2 + (var1 * 132)) + 56)
    if (1 if i32_load((var2 + (var1 * 132)) + 56) == 0 else 0):
        break
    if (1 if var1 == i32_load16_u((var2 + (var0 * 132)) + 110) else 0):
        break
    if (1 if i32_load(38984) != var5 else 0):
        break
    var3 = 0
    return var3


# ==========================================================
# $func656
# ==========================================================
def func656(var0):
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
    var17 = 0
    var18 = 0
    var19 = 0
    var20 = 0
    var8 = i32_load(9671128)
    var13 = i32_load(var0 + 32)
    var1 = (i32_load(9671128) + (i32_load(var0 + 32) * 132))
    if (1 if i32_load((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 36) == 0 else 0):
        if (1 if i32_load8_u(var1 + 125) != 3 else 0):
            break
    var5 = i32_load8_u(var1 + 122)
    if (1 if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 268) != 3 else 0):
        break
    var1 = i32_load8_u(var0 + 122)
    # br_table ['$label2', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label2', '$label4']
    _br_idx = (i32_load8_u(var0 + 122) + -64)
    break  # br_table
    if (1 if var1 == 10 else 0):
        break
    if (1 if i32_load8_u(9216060) == 0 else 0):
        break
    var9 = i32_load(9142440)
    var14 = (i32_load(9142440) + 2)
    var15 = ((i32_load(9142440) + 2) * i32_load(((var5 * 404) + 9568096) + 208))
    var10 = i32_load16_u(var0 + 112)
    var16 = (i32_load16_u(var0 + 112) + 9)
    var11 = i32_load16_u(var0 + 114)
    var17 = (i32_load16_u(var0 + 114) + 9)
    var18 = (var11 - 10)
    var2 = (var10 - 10)
    var19 = i32_load(9142840)
    var6 = 2147483647
    while True:  # loop $label7
        var12 = (var2 + 1)
        if (1 if var2 < var9 else 0):
            var1 = (var10 - var2)
            var20 = ((var10 - var2) * var1)
            var1 = var18
            while True:  # loop $label6
                var3 = var1
                if (1 if var9 <= var1 else 0):
                    break
                if (1 if (var2 | var3) < 0 else 0):
                    break
                var1 = (var11 - var3)
                var7 = (((var11 - var3) * var1) + var20)
                if (1 if (((var11 - var3) * var1) + var20) >= var6 else 0):
                    break
                var1 = i32_load((var19 + (((((var3 + var15) + 1) * var14) + var12) << 2)))
                if (1 if i32_load((var19 + (((((var3 + var15) + 1) * var14) + var12) << 2))) == 0 else 0):
                    break
                var7 = (1 if i32_load8_u((var8 + (var1 * 132)) + 122) == var5 else 0)
                var6 = (var7 if (1 if i32_load8_u((var8 + (var1 * 132)) + 122) == var5 else 0) else var6)
                var4 = (var1 if var7 else var4)
                var1 = (var3 + 1)
                if (1 if var3 != var17 else 0):
                    continue
                break  # end loop
        var1 = (1 if var2 != var16 else 0)
        var2 = var12
        if var1:
            continue
        break  # end loop
    if var4:
        i32_store(var0 + 32, var4)
        return 0
    if (1 if i32_load(38984) != var5 else 0):
        break
    i32_store8(var0 + 129, 10)
    return 1
    i32_store8(var0 + 123, 0)
    i32_store(var0 + 32, 0)
    var1 = (var8 + (var13 * 132))
    i32_store16(var0 + 116, i32_load16_u((var8 + (var13 * 132)) + 112))
    i32_store16(var0 + 118, i32_load16_u(var1 + 114))
    return 0

