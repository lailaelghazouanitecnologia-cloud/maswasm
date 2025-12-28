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
# $func161
# ==========================================================
def func161(var0, var1, var2):
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
    var8 = i32_load(9671128)
    var11 = (i32_load(9671128) + (i32_load(var1) * 132))
    var9 = i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 122)
    var3 = i32_load8_u(var0 + 122)
    var13 = 1
    if (1 if var2 == 0 else 0):
        var12 = 1
        break
    var12 = 1
    while True:  # loop $label4
        var5 = (var8 + (i32_load((var1 + (var4 << 2))) * 132))
        var6 = i32_load8_u((var8 + (i32_load((var1 + (var4 << 2))) * 132)) + 122)
        # br_table ['$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label1', '$label3']
        _br_idx = (i32_load8_u((var8 + (i32_load((var1 + (var4 << 2))) * 132)) + 122) + -64)
        break  # br_table
        if (1 if var6 == 10 else 0):
            break
        var13 = 0
        if i32_load(((var6 * 404) + 9568096) + 264):
            var12 = 0
            var7 = (var7 | (1 if i32_load(var5 + 52) == 0 else 0))
        var9 = (-1 if (1 if var6 != var9 else 0) else var9)
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var2 else 0):
            continue
        break  # end loop
    var4 = i32_load16_u(var11 + 110)
    var6 = i32_load8_u(var0 + 128)
    var11 = i32_load(38768)
    if (1 if var3 == i32_load(38768) else 0):
        var2 = 55
        if (1 if var9 == i32_load(38712) else 0):
            break
    var2 = 35
    var8 = i32_load(((var3 * 404) + 9568096) + 264)
    if ((1 if i32_load(((var3 * 404) + 9568096) + 264) == 2 else 0) & var12):
        break
    var15 = i32_load8_u(9216060)
    if (1 if ((1 if i32_load8_u(9216060) == 0 else 0) & var13) == 0 else 0):
        break
    if (1 if var8 != 1 else 0):
        break
    var14 = i32_load(((var3 * 404) + 9568096) + 112)
    if (1 if i32_load(((var3 * 404) + 9568096) + 112) == 0 else 0):
        break
    var1 = i32_load16_u(var0 + 110)
    if (1 if i32_load(38500) == var3 else 0):
        break
    var5 = (i32_load(9142892) * var4)
    var10 = i32_load(9143004)
    var2 = i32_load16_u(var0 + 120)
    if i32_load16_u(var0 + 120):
    else:
    if (1 if i32_load8_u(((var2 if i32_load8_u((var10 + (var1 + var5))) else var1) + (var1 + var5))) == 0 else 0):
        if var6:
            break
        if (1 if i32_load8_u(var0 + 127) == 6 else 0):
            break
        break
    if var6:
        break
    var5 = i32_load8_u(var0 + 125)
    if (1 if i32_load8_u(var0 + 125) == 10 else 0):
        break
    if (1 if i32_load8_u(var0 + 126) == 2 else 0):
        break
    if (1 if i32_load(var0 + 64) == -1 else 0):
        break
    if (1 if i32_load(((var3 * 404) + 9568096) + 188) != 55 else 0):
        break
    if (1 if i32_load(38560) == var3 else 0):
        break
    if (1 if i32_load(38620) == var3 else 0):
        break
    if (1 if i32_load(38564) != var3 else 0):
        break
    if (1 if var1 != var4 else 0):
        break
    if (1 if var14 <= i32_load(var0 + 84) else 0):
        break
    var5 = i32_load8_u(var0 + 125)
    var2 = 54
    # br_table ['$label6', '$label5', '$label5', '$label5', '$label5', '$label5', '$label5', '$label5', '$label5', '$label5', '$label6', '$label5']
    _br_idx = (var5 - 4)
    break  # br_table
    var1 = i32_load16_u(var0 + 110)
    if (1 if i32_load(38500) == var3 else 0):
        break
    var5 = (i32_load(9142892) * var4)
    var10 = i32_load(9143004)
    var2 = var1
    var14 = i32_load16_u(var0 + 120)
    if i32_load16_u(var0 + 120):
    else:
    if (1 if i32_load8_u(((var14 if i32_load8_u((var10 + (var1 + var5))) else var1) + (var2 + var5))) == 0 else 0):
        if var6:
            break
        if (1 if i32_load8_u(var0 + 127) == 6 else 0):
            break
        break
    if var6:
        break
    if (1 if i32_load8_u(var0 + 125) == 10 else 0):
        break
    if (1 if i32_load8_u(var0 + 126) == 2 else 0):
        break
    if (1 if i32_load(var0 + 64) == -1 else 0):
        break
    if (1 if var8 == 2 else 0):
        break
    if (1 if i32_load(((var3 * 404) + 9568096) + 188) != 55 else 0):
        break
    if (1 if i32_load(38560) == var3 else 0):
        break
    if (1 if i32_load(38620) == var3 else 0):
        break
    if (1 if i32_load(38564) != var3 else 0):
        break
    if ((var7 | (1 if i32_load(38564) != var3 else 0)) & 1):
        break
    var2 = 6
    # br_table ['$label13', '$label5', '$label5', '$label5', '$label5', '$label5', '$label5', '$label5', '$label5', '$label5', '$label13', '$label5']
    _br_idx = (i32_load8_u(var0 + 125) - 4)
    break  # br_table
    var2 = 6
    if (1 if (var7 & 1) == 0 else 0):
        break
    if (1 if var13 == 0 else 0):
        break
    if (1 if i32_load(38528) != var3 else 0):
        break
    if (1 if i32_load8_u((i32_load(9143004) + ((i32_load(9142892) * var1) + var4))) == 0 else 0):
        break
    var2 = 61
    if (1 if i32_load((((i32_load(9561692) + (var4 * 286704)) + (i32_load(39188) << 2)) + 281808)) == 1 else 0):
        break
    var2 = i32_load8_u(var0 + 125)
    if (1 if var15 == 0 else 0):
        if (1 if var2 == 10 else 0):
            break
        if (1 if i32_load(((var3 * 404) + 9568096) + 188) == 55 else 0):
            break
        var2 = 1
        if (1 if var3 == var11 else 0):
            break
        break
    if (1 if var2 == 10 else 0):
        break
    if i32_load(((var3 * 404) + 9568096) + 188):
        break
    return 1
    var2 = 1
    if (1 if var3 != var11 else 0):
        break
    if (1 if i32_load(var0 + 64) >= i32_load(var0 + 68) else 0):
        break
    var2 = 4
    # br_table ['$label18', '$label5', '$label14', '$label14', '$label5', '$label14']
    _br_idx = var8
    break  # br_table
    if (1 if i32_load(((var3 * 404) + 9568096) + 268) == 2 else 0):
        break
    var2 = 0
    if i32_load8_u(9147152):
    else:
        if (1 if i32_load8_u((i32_load(9143008) + ((i32_load(9142892) * var1) + var4))) == 0 else 0):
            break
        if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 20 else 0):
            break
    if (1 if i32_load8_u(var0 + 127) == 6 else 0):
        return 0
    if (1 if var3 == var9 else 0):
        return 0
    var1 = ((var3 * 404) + 9568096)
    if (1 if i32_load(((var3 * 404) + 9568096) + 136) == 0 else 0):
        break
    if (1 if ((1 if i32_load(var1 + 140) != 0 else 0) & var12) == 0 else 0):
        break
    var0 = i32_load8_u(var0 + 125)
    var2 = ((25 if (1 if i32_load8_u(var0 + 125) != 4 else 0) else 0) if (1 if var0 != 14 else 0) else 0)
    return var2


# ==========================================================
# $func162
# ==========================================================
def func162(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if (1 if i32_load(9142848) >= (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        break
    if (1 if i32_load(var0 + 56) == 1 else 0):
    else:
    if 0:
        break
    if (1 if i32_load(38564) == var1 else 0):
        break
    # br_table ['$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label0', '$label2']
    _br_idx = (var2 - 4)
    break  # br_table
    if (1 if var3 == 0 else 0):
        break
    var2 = i32_load(9561692)
    var5 = i32_load(9671128)
    var4 = (i32_load(9671128) + (var3 * 132))
    var6 = i32_load16_u((i32_load(9671128) + (var3 * 132)) + 110)
    var7 = i32_load((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (var3 * 132)) + 110) * 286704)) + 283872)
    if (1 if i32_load((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (var3 * 132)) + 110) * 286704)) + 283872) == 0 else 0):
        break
    var4 = (i32_load16_u(var4 + 112) - var7)
    var4 = (var4 >> 31)
    if (1 if (((i32_load16_u(var4 + 112) - var7) ^ (var4 >> 31)) - var4) > 30 else 0):
        break
    var4 = 0
    var2 = (i32_load16_u((var5 + (var3 * 132)) + 114) - i32_load((var2 + (var6 * 286704)) + 283876))
    var2 = (var2 >> 31)
    if (1 if (((i32_load16_u((var5 + (var3 * 132)) + 114) - i32_load((var2 + (var6 * 286704)) + 283876)) ^ (var2 >> 31)) - var2) < 31 else 0):
        break
    var3 = ((var1 * 404) + 9568096)
    var2 = i32_load(((var1 * 404) + 9568096) + 264)
    var0 = i32_load8_u(var0 + 122)
    if (1 if i32_load(var3 + 188) == 55 else 0):
        break
    if (1 if var2 != 1 else 0):
        break
    if (1 if i32_load(38500) == var1 else 0):
        break
    return 0
    if (1 if var2 == 4 else 0):
        var4 = 0
        if (1 if i32_load(((var0 * 404) + 9568096) + 224) == 1 else 0):
            break
    var4 = 0
    if (1 if i32_load(((var0 * 404) + 9568096) + 272) == 0 else 0):
        if (1 if i32_load(38648) != var0 else 0):
            break
    if (1 if i32_load(((var1 * 404) + 9568096) + 208) == 2 else 0):
        break
    if (1 if i32_load(38564) != var1 else 0):
        break
    var3 = ((var0 * 404) + 9568096)
    if i32_load8_u(((var0 * 404) + 9568096) + 334):
        break
    if (1 if i32_load(var3 + 268) != 2 else 0):
        break
    if (1 if var0 != i32_load(38728) else 0):
        if (1 if i32_load(38996) != var0 else 0):
            break
    if var2:
        break
    if (1 if i32_load(((var1 * 404) + 9568096) + 268) == 2 else 0):
        break
    var2 = ((var0 * 404) + 9568096)
    if i32_load8_u(((var0 * 404) + 9568096) + 379):
        break
    var2 = i32_load(var2 + 24)
    if (1 if i32_load(var2 + 24) == 0 else 0):
        return 1
    var3 = i32_load(((var0 * 404) + 9568096) + 364)
    if (1 if i32_load(((var0 * 404) + 9568096) + 364) == 0 else 0):
        break
    var0 = 0
    while True:  # loop $label7
        var4 = (1 if i32_load((var2 + (var0 << 2))) == var1 else 0)
        if (1 if i32_load((var2 + (var0 << 2))) == var1 else 0):
            break
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var3 else 0):
            continue
        break  # end loop
    return var4


# ==========================================================
# $func164
# ==========================================================
def func164():
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
    while True:  # loop $label0
        var2 = ((var0 * 132) + 9216080)
        if i32_load8_u(((var0 * 132) + 9216080) + 23):
            i32_store(((i32_load(var2 + 4) * 404) + 9568096) + 180, var2)
        i32_store(var2 + 68, 0)
        i32_store(var2 + 112, 0)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != 356 else 0):
            continue
        break  # end loop
    var8 = i32_load8_u(9216060)
    while True:  # loop $label7
        var2 = ((var4 * 404) + 9568096)
        if (1 if i32_load(((var4 * 404) + 9568096) + 148) == 0 else 0):
            i32_store(var2 + 148, 9)
        var0 = i32_load(var2 + 244)
        if (1 if i32_load(var2 + 244) == 0 else 0):
            break
        var3 = i32_load(var2 + 240)
        var1 = 0
        if (1 if var0 != 1 else 0):
            var9 = (var0 & -2)
            var6 = 0
            while True:  # loop $label2
                var7 = (var1 << 2)
                var5 = ((i32_load((var3 + (var1 << 2))) * 132) + 9216080)
                var10 = i32_load(var5 + 68)
                i32_store(((i32_load((var3 + (var1 << 2))) * 132) + 9216080) + 68, (i32_load(var5 + 68) + 1))
                i32_store((var5 + (var10 << 2)) + 28, var4)
                var5 = ((i32_load((var3 + (var7 | 4))) * 132) + 9216080)
                var7 = i32_load(var5 + 68)
                i32_store(((i32_load((var3 + (var7 | 4))) * 132) + 9216080) + 68, (i32_load(var5 + 68) + 1))
                i32_store((var5 + (var7 << 2)) + 28, var4)
                var1 = (var1 + 2)
                var6 = (var6 + 2)
                if (1 if (var6 + 2) != var9 else 0):
                    continue
                break  # end loop
        if (1 if (var0 & 1) == 0 else 0):
            break
        var1 = ((i32_load((var3 + (var1 << 2))) * 132) + 9216080)
        var0 = i32_load(var1 + 68)
        i32_store(((i32_load((var3 + (var1 << 2))) * 132) + 9216080) + 68, (i32_load(var1 + 68) + 1))
        i32_store((var1 + (var0 << 2)) + 28, var4)
        var1 = i32_load(var2 + 180)
        if (1 if i32_load(var2 + 180) == 0 else 0):
            break
        var0 = i32_load(var2 + 264)
        if (1 if i32_load(var2 + 264) == 1 else 0):
            var0 = i32_load(var2 + 196)
            if (1 if ((1 if var8 == 0 else 0) & (1 if i32_load(var2 + 196) != 3 else 0)) == 0 else 0):
                var0 = i32_load(var1 + 112)
                i32_store(var1 + 112, (i32_load(var1 + 112) + 1))
                var3 = (var1 + 72)
                i32_store(((var1 + 72) + (var0 << 2)), 10)
                var0 = i32_load(var1 + 112)
                i32_store(var1 + 112, (i32_load(var1 + 112) + 1))
                i32_store((var3 + (var0 << 2)), 79)
                break
            var0 = i32_load(((var0 << 2) + 9940))
            var3 = i32_load(var1 + 112)
            i32_store(var1 + 112, (i32_load(var1 + 112) + 1))
            i32_store((var1 + (var3 << 2)) + 72, var0)
        else:
        if (1 if var0 == 3 else 0):
            break
        var0 = i32_load(var2 + 236)
        if (1 if i32_load(var2 + 236) == 0 else 0):
            break
        var6 = i32_load(var2 + 232)
        var1 = 0
        while True:  # loop $label6
            var3 = ((i32_load((var6 + (var1 << 2))) * 132) + 9216080)
            if (1 if i32_load8_u(((i32_load((var6 + (var1 << 2))) * 132) + 9216080) + 23) == 0 else 0):
                break
            var3 = i32_load(((i32_load(var3 + 4) * 404) + 9568096) + 180)
            if (1 if i32_load(((i32_load(var3 + 4) * 404) + 9568096) + 180) == 0 else 0):
                break
            var0 = i32_load(var3 + 112)
            i32_store(var3 + 112, (i32_load(var3 + 112) + 1))
            i32_store((var3 + (var0 << 2)) + 72, var4)
            var0 = i32_load(var2 + 236)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < var0 else 0):
                continue
            break  # end loop
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != 255 else 0):
            continue
        break  # end loop
    return i32_load(var2 + 264)

