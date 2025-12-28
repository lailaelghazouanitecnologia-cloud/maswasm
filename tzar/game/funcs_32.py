"""
Auto-generated from WAT. Contains 16 functions.
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
# $Ia
# Export: Ia
# ==========================================================
def Ia():
    """Export: Ia"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if i32_load8_u(9147212):
        break
    var1 = i32_load(41092)
    if (1 if i32_load(41092) < 2 else 0):
        break
    var0 = (var1 - 1)
    var3 = ((var1 - 1) & 3)
    var5 = i32_load(9561692)
    if (1 if (var1 - 2) < 3 else 0):
        var1 = 1
        var0 = 0
        break
    var7 = (var0 & -4)
    var0 = 0
    var1 = 1
    while True:  # loop $label2
        var2 = (var5 + (var1 * 286704))
        var0 = ((((var0 + (1 if i32_load((var5 + (var1 * 286704)) + 284616) == 0 else 0)) + (1 if i32_load((var2 + 571320)) == 0 else 0)) + (1 if i32_load((var2 + 858024)) == 0 else 0)) + (1 if i32_load((var2 + 1144728)) == 0 else 0))
        var1 = (var1 + 4)
        var6 = (var6 + 4)
        if (1 if (var6 + 4) != var7 else 0):
            continue
        break  # end loop
    if (1 if var3 == 0 else 0):
        break
    while True:  # loop $label3
        var0 = (var0 + (1 if i32_load((var5 + (var1 * 286704)) + 284616) == 0 else 0))
        var1 = (var1 + 1)
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var3 else 0):
            continue
        break  # end loop
    return var0


# ==========================================================
# $ib
# Export: ib
# ==========================================================
def ib(var0):
    """Export: ib"""
    var1 = 0
    i32_store(9681464, var0)
    var1 = 9681776
    # br_table ['$label0', '$label1', '$label2']
    _br_idx = var0
    break  # br_table
    var1 = 9681792
    i32_store(9681476, var1)
    i32_store(9681468, 0)
    break
    i32_store(9681476, 9681696)
    i32_store(9681468, 0)
    i32_store(100, i32_load(((i32_load(9681696) * 404) + 9568096) + 68))
    return 9681472


# ==========================================================
# $jb
# Export: jb
# ==========================================================
def jb(var0):
    """Export: jb"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var1 = i32_load(9681468)
    var3 = (i32_load(9681468) + var0)
    var2 = i32_load(9681464)
    var4 = ((4 if (1 if i32_load(9681464) == 1 else 0) else 3) if var2 else 18)
    var0 = (((i32_load(9681468) + var0) if var1 else (((4 if (1 if i32_load(9681464) == 1 else 0) else 3) if var2 else 18) - 1)) if (1 if var0 == -1 else 0) else var3)
    var1 = ((((i32_load(9681468) + var0) if var1 else (((4 if (1 if i32_load(9681464) == 1 else 0) else 3) if var2 else 18) - 1)) if (1 if var0 == -1 else 0) else var3) if (1 if var0 < var4 else 0) else 0)
    i32_store(9681468, ((((i32_load(9681468) + var0) if var1 else (((4 if (1 if i32_load(9681464) == 1 else 0) else 3) if var2 else 18) - 1)) if (1 if var0 == -1 else 0) else var3) if (1 if var0 < var4 else 0) else 0))
    var0 = 100
    if var2:
    else:
    i32_store(100, i32_load(((i32_load((i32_load(9681476) + (var1 << 2))) * 404) + 9568096) + 68))
    return 9681472


# ==========================================================
# $Je
# Export: Je
# ==========================================================
def Je(var0):
    """Export: Je"""
    var0 = (i32_load(9561692) + (var0 * 286704))
    return (((i32_load8_u(((i32_load(9561692) + (var0 * 286704)) + 283973)) << 8) | i32_load8_u((var0 + 283974))) | (i32_load8_u(var0 + 283972) << 16))


# ==========================================================
# $fc
# Export: fc
# ==========================================================
def fc(var0):
    """Export: fc"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var0 = 0
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var1 = 1
    var3 = (var2 - 1)
    var6 = ((var2 - 1) & 1)
    var4 = i32_load(9561692)
    if (1 if var2 != 2 else 0):
        var3 = (var3 & -2)
        var2 = 0
        while True:  # loop $label1
            var5 = (var4 + (var1 * 286704))
            if i32_load((var4 + (var1 * 286704)) + 284616):
                var0 = (var0 + (1 if i32_load8_u(var5 + 286696) == 0 else 0))
            var5 = (var4 + ((var1 + 1) * 286704))
            if i32_load((var4 + ((var1 + 1) * 286704)) + 284616):
                var0 = (var0 + (1 if i32_load8_u(var5 + 286696) == 0 else 0))
            var1 = (var1 + 2)
            var2 = (var2 + 2)
            if (1 if (var2 + 2) != var3 else 0):
                continue
            break  # end loop
    if (1 if var6 == 0 else 0):
        break
    var1 = (var4 + (var1 * 286704))
    if (1 if i32_load((var4 + (var1 * 286704)) + 284616) == 0 else 0):
        break
    var0 = (var0 + (1 if i32_load8_u(var1 + 286696) == 0 else 0))
    return var0


# ==========================================================
# $Q
# Export: Q
# ==========================================================
def Q(var0, var1, var2):
    """Export: Q"""
    var3 = 0
    var3 = i32_load(9561692)
    if var2:
        i32_store((((var3 + (var0 * 286704)) + (var1 << 2)) + 283984), (var2 - 1))
    if (1 if var1 == 97 else 0):
        var2 = (var3 + (var0 * 286704))
        i32_store((var3 + (var0 * 286704)) + 283868, i32_load((var2 + 284372)))
    return i32_load((((var3 + (var0 * 286704)) + (var1 << 2)) + 283984))


# ==========================================================
# $R
# Export: R
# ==========================================================
def R(var0, var1, var2, var3):
    """Export: R"""
    var4 = 0
    var5 = 0
    var4 = i32_load(9561692)
    if (1 if var1 == 0 else 0):
        break
    var5 = (var4 + (var0 * 286704))
    var1 = (var1 - 1)
    i32_store(((var4 + (var0 * 286704)) + (286688 if var2 else 286684)), (100 if (1 if var1 >= 100 else 0) else (var1 - 1)))
    if (1 if var3 == 0 else 0):
        break
    if i32_load(var5 + 286688):
        break
    i32_store((var5 + 286688), 100)
    return i32_load(((var4 + (var0 * 286704)) + (286688 if var2 else 286684)))


# ==========================================================
# $func739
# ==========================================================
def func739(var0, var1):
    var2 = 0
    var3 = 0
    var2 = i32_load(9561692)
    var1 = ((var1 * 404) + 9568096)
    var3 = i32_load(((var1 * 404) + 9568096) + 212)
    if (1 if i32_load(((var1 * 404) + 9568096) + 212) == 4 else 0):
        var1 = i32_load(var1 + 92)
        var0 = (var2 + (var0 * 286704))
        i32_store8((var2 + (var0 * 286704)) + 286700, 1)
        var0 = (var0 + 284000)
        i32_store((var0 + 284000), (((var1 * i32_load(var0)) & 0xFFFFFFFF) // 100))
        return
    var0 = (((var2 + (var0 * 286704)) + (var3 << 2)) + 283984)
    i32_store((((var2 + (var0 * 286704)) + (var3 << 2)) + 283984), (i32_load(var0) + i32_load(var1 + 92)))


# ==========================================================
# $func747
# ==========================================================
def func747(var0, var1, var2, var3, var4):
    var5 = 0
    var2 = i32_load(9671128)
    var3 = i32_load(var1)
    var5 = i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 122) * 404) + 9568096) + 300)
    var1 = (1 if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 122) * 404) + 9568096) + 300) == 0 else 0)
    if (1 if var5 == 0 else 0):
        break
    if (1 if var4 == 0 else 0):
        break
    var0 = i32_load((var2 + (var0 * 132)) + 44)
    if (1 if i32_load((var2 + (var0 * 132)) + 44) == 0 else 0):
        return 0
    var1 = 0
    var2 = i32_load(9215884)
    if (1 if i32_load((i32_load(9215884) + (var0 << 4)) + 4) != 13 else 0):
        break
    i32_store((var2 + ((var0 << 4) | 12)), var3)
    var1 = 1
    return var1


# ==========================================================
# $Sd
# Export: Sd
# ==========================================================
def Sd(var0, var1, var2):
    """Export: Sd"""
    var3 = 0
    var4 = 0
    var5 = 0
    var3 = ((var0 * 404) + 9568096)
    if i32_load8_u(((var0 * 404) + 9568096) + 378):
        break
    var3 = i32_load(var3 + 264)
    if var2:
        if (1 if var3 == 0 else 0):
            break
        break
    if (1 if var3 != 1 else 0):
        break
    var2 = 0
    while True:  # loop $label3
        if i32_load8_u(((var2 * 404) + 9568096) + 378):
            break
        var3 = i32_load(((((var2 * 1020) + 9299904) + (var0 << 2)) if var1 else (((var0 * 1020) + 9299904) + (var2 << 2))))
        if (1 if i32_load(((((var2 * 1020) + 9299904) + (var0 << 2)) if var1 else (((var0 * 1020) + 9299904) + (var2 << 2)))) == 100 else 0):
            break
        var5 = ((var4 << 2) + 9147392)
        i32_store(((var4 << 2) + 9147392), var2)
        i32_store(var5 + 4, var3)
        var4 = (var4 + 2)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != 255 else 0):
            continue
        break  # end loop
    return var4


# ==========================================================
# $fb
# Export: fb
# ==========================================================
def fb(var0, var1):
    """Export: fb"""
    var2 = 0
    if (1 if var0 <= 254 else 0):
        if var1:
            var2 = 48
            break
        var2 = -48
        var0 = ((var0 * 404) + 9568240)
    else:
    return 0


# ==========================================================
# $Bb
# Export: Bb
# ==========================================================
def Bb(var0):
    """Export: Bb"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var1 = ((var0 * 404) + 9568096)
    var0 = i32_load(((var0 * 404) + 9568096) + 236)
    if (1 if i32_load(((var0 * 404) + 9568096) + 236) == 0 else 0):
        var0 = 0
        break
    var5 = (var0 & 1)
    var2 = i32_load(var1 + 232)
    if (1 if var0 == 1 else 0):
        var0 = 0
        var1 = 0
        break
    var6 = (var0 & -2)
    var0 = 0
    var1 = 0
    while True:  # loop $label2
        var3 = (var1 << 2)
        var7 = i32_load((var2 + (var1 << 2)))
        if i32_load8_u(((i32_load((var2 + (var1 << 2))) * 132) + 9216080) + 23):
            i32_store(((var0 << 2) + 9147392), var7)
            var0 = (var0 + 1)
        var3 = i32_load((var2 + (var3 | 4)))
        if i32_load8_u(((i32_load((var2 + (var3 | 4))) * 132) + 9216080) + 23):
            i32_store(((var0 << 2) + 9147392), var3)
            var0 = (var0 + 1)
        var1 = (var1 + 2)
        var4 = (var4 + 2)
        if (1 if (var4 + 2) != var6 else 0):
            continue
        break  # end loop
    if (1 if var5 == 0 else 0):
        break
    var1 = i32_load((var2 + (var1 << 2)))
    if (1 if i32_load8_u(((i32_load((var2 + (var1 << 2))) * 132) + 9216080) + 23) == 0 else 0):
        break
    i32_store(((var0 << 2) + 9147392), var1)
    var0 = (var0 + 1)
    i32_store(((var0 << 2) + 9147392), -1)


# ==========================================================
# $Zb
# Export: Zb
# ==========================================================
def Zb(var0):
    """Export: Zb"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    while True:  # loop $label2
        var1 = i32_load(((var0 + (var2 << 2)) + 284636))
        if (1 if i32_load(((var0 + (var2 << 2)) + 284636)) == 0 else 0):
            break
        var3 = i32_load(var1 + 8)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        var4 = i32_load(var1)
        var1 = 0
        while True:  # loop $label1
            var5 = i32_load((var4 + (var1 << 2)))
            if (1 if i32_load((var4 + (var1 << 2))) == 0 else 0):
                var1 = (var1 + 1)
                if (1 if var3 != (var1 + 1) else 0):
                    continue
                break
            break  # end loop
        var2 = (i32_load(9671128) + (var5 * 132))
        var1 = ((i32_load8_u((i32_load(9671128) + (var5 * 132)) + 122) * 404) + 9568096)
        i32_store(var0 + 283896, (((i32_load(((i32_load8_u((i32_load(9671128) + (var5 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + i32_load16_u(var2 + 112)))
        i32_store(var0 + 283900, (i32_load16_u(var2 + 114) + ((i32_load(var1 + 220) & 0xFFFFFFFF) >> 1)))
        return
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != 255 else 0):
            continue
        break  # end loop


# ==========================================================
# $func783
# ==========================================================
def func783(var0):
    var0 = (i32_load(9671128) + (i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 12) * 132))
    if (1 if i32_load(38528) != i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 12) * 132)) + 122) else 0):
        break
    if (1 if i32_load8_u(var0 + 125) == 3 else 0):
        break
    i32_store8(var0 + 125, 0)


# ==========================================================
# $func784
# ==========================================================
def func784(var0):
    var1 = 0
    var1 = (i32_load(9671128) + (i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 12) * 132))
    if (1 if i32_load((i32_load(9671128) + (i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 12) * 132)) + 100) == i32_load(var0 + 28) else 0):
        i32_store(var1 + 100, 0)


# ==========================================================
# $S
# Export: S
# ==========================================================
def S(var0, var1):
    """Export: S"""
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
    var6 = i32_load(9561692)
    if (1 if var1 == 0 else 0):
        var1 = ((var6 + (var0 * 286704)) + 283984)
        while True:  # loop $label0
            var2 = (var4 << 2)
            i32_store(((var4 << 2) + 9561072), i32_load((var1 + var2)))
            var3 = (var2 + 4)
            i32_store(((var2 + 4) + 9561072), i32_load((var1 + var3)))
            var3 = (var2 + 8)
            i32_store(((var2 + 8) + 9561072), i32_load((var1 + var3)))
            var3 = (var2 + 12)
            i32_store(((var2 + 12) + 9561072), i32_load((var1 + var3)))
            var2 = (var2 + 16)
            i32_store(((var2 + 16) + 9561072), i32_load((var1 + var2)))
            var4 = (var4 + 5)
            if (1 if (var4 + 5) != 155 else 0):
                continue
            break  # end loop
        var1 = i32_load(9142892)
        if i32_load(9142892):
            var9 = (var6 + (var0 * 286704))
            var10 = ((var6 + (var0 * 286704)) + 286688)
            var11 = (var9 + 286684)
            var4 = 0
            while True:  # loop $label3
                var2 = (var6 + (var4 * 286704))
                if (1 if var0 != i32_load((var6 + (var4 * 286704)) + 283908) else 0):
                    var1 = i32_load(var11)
                    if (1 if i32_load(var11) == 0 else 0):
                        break
                    if (1 if var4 == 0 else 0):
                        break
                    i32_store(var2 + 286684, var1)
                    i32_store(var2 + 286688, i32_load(var10))
                    var8 = 0
                    while True:  # loop $label2
                        var3 = (var2 + 283984)
                        var1 = (var8 << 2)
                        var7 = (var9 + 283984)
                        i32_store(((var2 + 283984) + (var8 << 2)), i32_load(((var9 + 283984) + var1)))
                        var5 = (var1 + 4)
                        i32_store((var3 + (var1 + 4)), i32_load((var5 + var7)))
                        var5 = (var1 + 8)
                        i32_store((var3 + (var1 + 8)), i32_load((var5 + var7)))
                        var5 = (var1 + 12)
                        i32_store((var3 + (var1 + 12)), i32_load((var5 + var7)))
                        var1 = (var1 + 16)
                        i32_store((var3 + (var1 + 16)), i32_load((var1 + var7)))
                        var8 = (var8 + 5)
                        if (1 if (var8 + 5) != 155 else 0):
                            continue
                        break  # end loop
                    i32_store(var2 + 283868, i32_load((var2 + 284372)))
                    var1 = i32_load(9142892)
                var4 = (var4 + 1)
                if (1 if (var4 + 1) < var1 else 0):
                    continue
                break  # end loop
        return
    var0 = (var6 + (var0 * 286704))
    i32_store((var6 + (var0 * 286704)) + 283868, i32_load(9561460))
    # Unknown: memory.copy []
    var1 = i32_load(9142424)
    i32_store((var0 + 284000), i32_load(i32_load(9142424) + 40))
    i32_store((var0 + 284136), i32_load(var1 + 36))

