"""
Auto-generated from WAT. Contains 10 functions.
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
# $Oc
# Export: Oc
# ==========================================================
def Oc(var0, var1):
    """Export: Oc"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if var1:
        var5 = i32_load(9568088)
        if (1 if var0 == 0 else 0):
            break
        var1 = 0
        if (1 if var0 >= 4 else 0):
            var7 = (var0 & -4)
            var3 = (var5 + 112)
            while True:  # loop $label1
                i32_store16((var3 + (var1 << 1)), i32_load(((var1 << 2) + 9147392)))
                var2 = (var1 | 1)
                i32_store16((var3 + ((var1 | 1) << 1)), i32_load(((var2 << 2) + 9147392)))
                var2 = (var1 | 2)
                i32_store16((var3 + ((var1 | 2) << 1)), i32_load(((var2 << 2) + 9147392)))
                var2 = (var1 | 3)
                i32_store16((var3 + ((var1 | 3) << 1)), i32_load(((var2 << 2) + 9147392)))
                var1 = (var1 + 4)
                var4 = (var4 + 4)
                if (1 if (var4 + 4) != var7 else 0):
                    continue
                break  # end loop
        var4 = (var0 & 3)
        if (1 if (var0 & 3) == 0 else 0):
            break
        while True:  # loop $label2
            i32_store16((var5 + (var1 << 1)) + 112, i32_load(((var1 << 2) + 9147392)))
            var1 = (var1 + 1)
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != var4 else 0):
                continue
            break  # end loop
        i32_store(var5 + 192, var0)
        return
    var5 = i32_load(9568076)
    if (1 if var0 == 0 else 0):
        break
    var1 = 0
    if (1 if var0 >= 4 else 0):
        var7 = (var0 & -4)
        var3 = (var5 + 24)
        while True:  # loop $label4
            i32_store16((var3 + (var1 << 1)), i32_load(((var1 << 2) + 9147392)))
            var2 = (var1 | 1)
            i32_store16((var3 + ((var1 | 1) << 1)), i32_load(((var2 << 2) + 9147392)))
            var2 = (var1 | 2)
            i32_store16((var3 + ((var1 | 2) << 1)), i32_load(((var2 << 2) + 9147392)))
            var2 = (var1 | 3)
            i32_store16((var3 + ((var1 | 3) << 1)), i32_load(((var2 << 2) + 9147392)))
            var1 = (var1 + 4)
            var4 = (var4 + 4)
            if (1 if (var4 + 4) != var7 else 0):
                continue
            break  # end loop
    var4 = (var0 & 3)
    if (1 if (var0 & 3) == 0 else 0):
        break
    while True:  # loop $label5
        i32_store16((var5 + (var1 << 1)) + 24, i32_load(((var1 << 2) + 9147392)))
        var1 = (var1 + 1)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) != var4 else 0):
            continue
        break  # end loop
    i32_store(var5 + 104, var0)


# ==========================================================
# $func854
# ==========================================================
def func854(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var2 = ((var1 * 404) + 9568096)
    var4 = i32_load(((var1 * 404) + 9568096) + 236)
    if (1 if i32_load(((var1 * 404) + 9568096) + 236) == 0 else 0):
        break
    var1 = 0
    var7 = i32_load(9561692)
    var5 = i32_load(var2 + 92)
    var2 = i32_load(var2 + 232)
    if (1 if var4 >= 4 else 0):
        var9 = (var4 & -4)
        var3 = ((var7 + (var0 * 286704)) + 269376)
        while True:  # loop $label1
            var6 = (var1 << 2)
            i32_store((var3 + (i32_load((var2 + (var1 << 2))) * 36)), var5)
            i32_store((var3 + (i32_load((var2 + (var6 | 4))) * 36)), var5)
            i32_store((var3 + (i32_load((var2 + (var6 | 8))) * 36)), var5)
            i32_store((var3 + (i32_load((var2 + (var6 | 12))) * 36)), var5)
            var1 = (var1 + 4)
            var8 = (var8 + 4)
            if (1 if (var8 + 4) != var9 else 0):
                continue
            break  # end loop
    var4 = (var4 & 3)
    if (1 if (var4 & 3) == 0 else 0):
        break
    var3 = 0
    var0 = (var7 + (var0 * 286704))
    while True:  # loop $label2
        i32_store(((var0 + (i32_load((var2 + (var1 << 2))) * 36)) + 269376), var5)
        var1 = (var1 + 1)
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != var4 else 0):
            continue
        break  # end loop


# ==========================================================
# $ha
# Export: ha
# ==========================================================
def ha(var0):
    """Export: ha"""
    var1 = 0
    var2 = 0
    i32_store(9561756, var0)
    var2 = (i32_load(9561764) + 1)
    i32_store(9561764, (i32_load(9561764) + 1))
    var1 = 2
    if (1 if var2 <= 7 else 0):
        var1 = i32_load(9561760)
        if i32_load(9561760):
            return (1 if var0 == var1 else 0)
    else:
    return 2


# ==========================================================
# $Qa
# Export: Qa
# ==========================================================
def Qa(var0):
    """Export: Qa"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var2 = 1
    var3 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var4 = i32_load(9561692)
    var1 = 1
    while True:  # loop $label1
        if (1 if var0 != i32_load((var4 + (var1 * 286704)) + 284616) else 0):
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var3 else 0):
                continue
            break
        break  # end loop
    var2 = (1 if i32_load8_u((i32_load(9143004) + (i32_load((var4 + (var1 * 286704)) + 283908) + (i32_load(9142872) * var3)))) != 0 else 0)
    return var2


# ==========================================================
# $func880
# ==========================================================
def func880(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var7 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var3 = i32_load(59164)
    var4 = i32_load(9561692)
    var0 = 1
    while True:  # loop $label2
        var5 = (var4 + (var0 * 286704))
        if (1 if i32_load((var4 + (var0 * 286704)) + 284616) == var3 else 0):
            break
        if (1 if i32_load(var5 + 284628) == var3 else 0):
            break
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var7 else 0):
            continue
        break  # end loop
    var3 = 0
    break
    if (1 if var2 == 0 else 0):
        var3 = 1
        break
    var4 = i32_load(var1)
    var8 = i32_load(9671136)
    var6 = ((1 if i32_load(var1) < 3 else 0) | (1 if var4 >= i32_load(9671136) else 0))
    var3 = 0
    if (1 if i32_load8_u(9147152) == 0 else 0):
        var5 = 0
        if var6:
            break
        var6 = i32_load(9215884)
        var9 = i32_load(9143008)
        var10 = i32_load(9671128)
        while True:  # loop $label3
            var4 = (var10 + (var4 * 132))
            if (1 if i32_load8_u((var9 + ((var7 * i32_load16_u((var10 + (var4 * 132)) + 110)) + var0))) == 0 else 0):
                break
            if (1 if i32_load((var6 + (i32_load(var4 + 44) << 4)) + 4) == 20 else 0):
                break
            if (1 if i32_load8_u(var4 + 127) == 6 else 0):
                break
            var5 = (var5 + 1)
            var3 = (1 if (var5 + 1) >= var2 else 0)
            if (1 if var2 == var5 else 0):
                break
            var4 = i32_load((var1 + (var5 << 2)))
            if (1 if i32_load((var1 + (var5 << 2))) < 3 else 0):
                break
            if (1 if var4 < var8 else 0):
                continue
            break  # end loop
        break
    if var6:
        break
    var4 = (var2 - 1)
    var0 = 0
    while True:  # loop $label5
        var3 = (var0 + 1)
        if (1 if var0 == var4 else 0):
            break
        var5 = i32_load((var1 + (var3 << 2)))
        if (1 if i32_load((var1 + (var3 << 2))) < 3 else 0):
            break
        var0 = var3
        if (1 if var5 < var8 else 0):
            continue
        break  # end loop
    var3 = (1 if var2 <= var3 else 0)
    return var3


# ==========================================================
# $func881
# ==========================================================
def func881(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var7 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var3 = i32_load(59164)
    var4 = i32_load(9561692)
    var0 = 1
    while True:  # loop $label2
        var5 = (var4 + (var0 * 286704))
        if (1 if i32_load((var4 + (var0 * 286704)) + 284616) == var3 else 0):
            break
        if (1 if i32_load(var5 + 284628) == var3 else 0):
            break
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var7 else 0):
            continue
        break  # end loop
    var3 = 0
    break
    if (1 if var2 == 0 else 0):
        var3 = 1
        break
    var4 = i32_load(var1)
    var8 = i32_load(9671136)
    var6 = ((1 if i32_load(var1) < 3 else 0) | (1 if var4 >= i32_load(9671136) else 0))
    var3 = 0
    if (1 if i32_load8_u(9147152) == 0 else 0):
        var5 = 0
        if var6:
            break
        var9 = i32_load(9215884)
        var10 = i32_load(9143008)
        var6 = i32_load(9671128)
        while True:  # loop $label3
            var4 = (var6 + (i32_load((var6 + (var4 * 132)) + 36) * 132))
            if (1 if i32_load8_u((var10 + ((var7 * i32_load16_u((var6 + (i32_load((var6 + (var4 * 132)) + 36) * 132)) + 110)) + var0))) == 0 else 0):
                break
            if (1 if i32_load((var9 + (i32_load(var4 + 44) << 4)) + 4) == 20 else 0):
                break
            if (1 if i32_load8_u(var4 + 127) == 6 else 0):
                break
            var5 = (var5 + 1)
            var3 = (1 if (var5 + 1) >= var2 else 0)
            if (1 if var2 == var5 else 0):
                break
            var4 = i32_load((var1 + (var5 << 2)))
            if (1 if i32_load((var1 + (var5 << 2))) < 3 else 0):
                break
            if (1 if var4 < var8 else 0):
                continue
            break  # end loop
        break
    if var6:
        break
    var4 = (var2 - 1)
    var0 = 0
    while True:  # loop $label5
        var3 = (var0 + 1)
        if (1 if var0 == var4 else 0):
            break
        var5 = i32_load((var1 + (var3 << 2)))
        if (1 if i32_load((var1 + (var3 << 2))) < 3 else 0):
            break
        var0 = var3
        if (1 if var5 < var8 else 0):
            continue
        break  # end loop
    var3 = (1 if var2 <= var3 else 0)
    return var3


# ==========================================================
# $func883
# ==========================================================
def func883(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var3 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var0 = i32_load(59164)
    var4 = i32_load(9561692)
    var2 = 1
    while True:  # loop $label2
        var5 = (var4 + (var2 * 286704))
        if (1 if i32_load((var4 + (var2 * 286704)) + 284616) == var0 else 0):
            break
        if (1 if i32_load(var5 + 284628) == var0 else 0):
            break
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var3 else 0):
            continue
        break  # end loop
    return 0
    if i32_load8_u(9147152):
        break
    var2 = i32_load(9671128)
    var1 = i32_load((var2 + (i32_load(var1) * 132)) + 36)
    if (1 if i32_load8_u((i32_load(9143008) + (var2 + (var3 * i32_load16_u((i32_load(9671128) + (i32_load((var2 + (i32_load(var1) * 132)) + 36) * 132)) + 110))))) == 0 else 0):
        break
    var1 = (var2 + (var1 * 132))
    if (1 if i32_load((i32_load(9215884) + (i32_load((var2 + (var1 * 132)) + 44) << 4)) + 4) == 20 else 0):
        break
    return (1 if i32_load8_u(var1 + 127) != 6 else 0)


# ==========================================================
# $Ie
# Export: Ie
# ==========================================================
def Ie(var0, var1, var2, var3):
    """Export: Ie"""
    var4 = 0
    # br_table ['$label0', '$label1', '$label1', '$label2', '$label1']
    _br_idx = var3
    break  # br_table
    var3 = i32_load(9143004)
    var4 = i32_load(9142892)
    var0 = (1 if var0 != 0 else 0)
    i32_store8((i32_load(9143004) + ((i32_load(9142892) * var1) + var2)), (1 if var0 != 0 else 0))
    i32_store8((var3 + ((var2 * var4) + var1)), var0)
    return
    i32_store8((i32_load(9143012) + ((i32_load(9142892) * var1) + var2)), (1 if var0 != 0 else 0))


# ==========================================================
# $func896
# ==========================================================
def func896(var0, var1, var2, var3, var4):
    var2 = 1
    var3 = i32_load(9671128)
    var1 = i32_load(var1)
    var4 = (i32_load(9671128) + (i32_load(var1) * 132))
    # br_table ['$label0', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label0', '$label1']
    _br_idx = (i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 125) - 4)
    break  # br_table
    var4 = ((i32_load8_u(var4 + 122) * 404) + 9568096)
    if (1 if i32_load(((i32_load8_u(var4 + 122) * 404) + 9568096) + 264) != 1 else 0):
        break
    if (1 if i32_load(var4 + 112) == 0 else 0):
        break
    if (1 if i32_load(9142848) <= (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        break
    var0 = i32_load16_u((var3 + (var0 * 132)) + 110)
    var1 = i32_load16_u((var3 + (var1 * 132)) + 110)
    var2 = ((1 if i32_load8_u((i32_load(9143004) + (i32_load16_u((var3 + (var0 * 132)) + 110) + (i32_load16_u((var3 + (var1 * 132)) + 110) * i32_load(9142892))))) == 0 else 0) & (1 if var0 != var1 else 0))
    return var2


# ==========================================================
# $Md
# Export: Md
# ==========================================================
def Md(var0, var1):
    """Export: Md"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if var0:
        break
    if i32_load8_u(9147210):
        break
    var1 = i32_load(9561692)
    var3 = i32_load(9142872)
    var0 = (i32_load(9561692) + (i32_load(9142872) * 286704))
    var2 = i32_load((i32_load(9561692) + (i32_load(9142872) * 286704)) + 283848)
    if (1 if i32_load((i32_load(9561692) + (i32_load(9142872) * 286704)) + 283848) != 2147483647 else 0):
        i32_store((var0 + 283848), (var2 + 50000))
    var0 = (var0 + 283852)
    var2 = i32_load((var0 + 283852))
    if (1 if i32_load((var0 + 283852)) != 2147483647 else 0):
        i32_store(var0, (var2 + 50000))
    var0 = (var1 + (var3 * 286704))
    var2 = ((var1 + (var3 * 286704)) + 283856)
    var4 = i32_load(((var1 + (var3 * 286704)) + 283856))
    if (1 if i32_load(((var1 + (var3 * 286704)) + 283856)) != 2147483647 else 0):
        i32_store(var2, (var4 + 50000))
    var0 = (var0 + 283860)
    var2 = i32_load((var0 + 283860))
    if (1 if i32_load((var0 + 283860)) != 2147483647 else 0):
        i32_store(var0, (var2 + 50000))
    var0 = 1
    var3 = (var1 + (var3 * 286704))
    i32_store8((var1 + (var3 * 286704)) + 286701, 1)
    var1 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var5 = (var1 - 1)
    var6 = ((var1 - 1) & 1)
    var3 = (i32_load(var3 + 283908) * var1)
    var2 = i32_load(9561692)
    var4 = i32_load(9143016)
    if (1 if var1 != 2 else 0):
        var5 = (var5 & -2)
        var1 = 0
        while True:  # loop $label1
            if i32_load8_u((var4 + (var0 + var3))):
                i32_store8((var2 + (var0 * 286704)) + 286701, 1)
            var7 = (var0 + 1)
            if i32_load8_u((var4 + ((var0 + 1) + var3))):
                i32_store8((var2 + (var7 * 286704)) + 286701, 1)
            var0 = (var0 + 2)
            var1 = (var1 + 2)
            if (1 if (var1 + 2) != var5 else 0):
                continue
            break  # end loop
    if (1 if var6 == 0 else 0):
        break
    if (1 if i32_load8_u((var4 + (var0 + var3))) == 0 else 0):
        break
    i32_store8((var2 + (var0 * 286704)) + 286701, 1)

