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
# $func740
# ==========================================================
def func740(var0, var1):
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
    var6 = i32_load(9671128)
    var7 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load(9142848) >= (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        var9 = (var6 + (var1 * 132))
        if (1 if i32_load8_u((var6 + (var1 * 132)) + 125) != 3 else 0):
            break
    func29(var7, 1)
    return
    var4 = (var6 + (var0 * 132))
    if (1 if i32_load8_u((var6 + (var0 * 132)) + 125) == 1 else 0):
        var2 = i32_load16_u(var4 + 114)
        var3 = (var6 + (var1 * 132))
        var5 = i32_load16_u((var6 + (var1 * 132)) + 114)
        var3 = i32_load16_u(var3 + 112)
        var4 = i32_load16_u(var4 + 112)
        if (1 if i32_load16_u(var3 + 112) != i32_load16_u(var4 + 112) else 0):
            break
        if (1 if var2 < var5 else 0):
            break
        if (1 if var2 > var5 else 0):
            break
        var3 = 0
        break
        var3 = (1 if (1 if var3 > var4 else 0) else (-1 if (1 if var3 < var4 else 0) else 0))
        var2 = (1 if (1 if var2 < var5 else 0) else (-1 if (1 if var2 > var5 else 0) else 0))
        var0 = (var6 + (var0 * 132))
        var2 = (((var2 * 3) + var3) + 4)
        if (1 if (((var2 * 3) + var3) + 4) <= 8 else 0):
        else:
        i32_store8(i32_load8_u((var2 + 10184)) + 124, 6)
        var0 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 276)
        func63(func37(var7, i32_load(((i32_load8_u(var0 + 122) * 72) + 9263856) + 8), 0.0, 0), var7, 23, var1, (i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 276) if var0 else 25))
        return (var6 + (var0 * 132))
    var5 = ((i32_load8_u(var4 + 122) * 404) + 9568096)
    if i32_load(((i32_load8_u(var4 + 122) * 404) + 9568096) + 216):
        var2 = (var6 + (var0 * 132))
        var10 = i32_load16_u((var6 + (var0 * 132)) + 114)
        var11 = i32_load16_u(var2 + 112)
        var12 = i32_load(9142840)
        var2 = 0
        while True:  # loop $label4
            var2 = (var2 + 1)
            var13 = ((var2 + 1) + var11)
            var3 = 0
            while True:  # loop $label3
                var3 = (var3 + 1)
                var8 = (i32_load(9142440) + 2)
                i32_store((var12 + ((var13 + ((((var3 + 1) + var10) + ((i32_load(9142440) + 2) * i32_load(var5 + 208))) * var8)) << 2)), i32_load(var5 + 212))
                var8 = i32_load(var5 + 216)
                if (1 if var3 < i32_load(var5 + 216) else 0):
                    continue
                break  # end loop
            if (1 if var2 < var8 else 0):
                continue
            break  # end loop
    var2 = (var6 + (var1 * 132))
    var10 = i32_load8_u((var6 + (var1 * 132)) + 122)
    i32_store8(var4 + 122, i32_load8_u((var6 + (var1 * 132)) + 122))
    var1 = (var6 + (var0 * 132))
    i32_store8((var6 + (var0 * 132)) + 124, i32_load8_u(var2 + 124))
    i32_store16(var1 + 120, i32_load16_u(var2 + 110))
    var5 = i32_load16_u(var2 + 112)
    i32_store16(var1 + 112, i32_load16_u(var2 + 112))
    var9 = i32_load16_u(var2 + 114)
    i32_store16(var1 + 114, i32_load16_u(var2 + 114))
    var2 = i32_load8_u(var4 + 122)
    var4 = ((i32_load8_u(var4 + 122) * 404) + 9568096)
    if i32_load(((i32_load8_u(var4 + 122) * 404) + 9568096) + 216):
        var11 = ((var2 * 404) + 9568304)
        var12 = i32_load(9142840)
        var2 = 0
        while True:  # loop $label6
            var2 = (var2 + 1)
            var13 = ((var2 + 1) + var5)
            var3 = 0
            while True:  # loop $label5
                var3 = (var3 + 1)
                var8 = (i32_load(9142440) + 2)
                i32_store((var12 + ((var13 + ((((var3 + 1) + var9) + ((i32_load(9142440) + 2) * i32_load(var11))) * var8)) << 2)), i32_load(var1 + 28))
                var8 = i32_load(var4 + 216)
                if (1 if var3 < i32_load(var4 + 216) else 0):
                    continue
                break  # end loop
            if (1 if var2 < var8 else 0):
                continue
            break  # end loop
    var3 = i32_load16_u(var1 + 114)
    var1 = i32_load16_u(var1 + 112)
    var5 = i32_load(i32_load(9142424) + 48)
    if i32_load(i32_load(9142424) + 48):
        if (1 if i32_load8_u(9147152) == 0 else 0):
            break
    var2 = i32_load(9142440)
    break
    var2 = i32_load(9142440)
    var4 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var3) + var1) << 1)))
    if (1 if var5 == 2 else 0):
        if (1 if var4 > 1 else 0):
            break
        break
    if (1 if var4 == 0 else 0):
        break
    func80(float(var1), float(var3), i32_load(9142788), 32.0, float((var2 * 96)))
    var5 = 2
    var4 = func26(16)
    var9 = ((var10 * 404) + 9568096)
    var1 = i32_load(((var10 * 404) + 9568096) + 236)
    var2 = (i32_load(((var10 * 404) + 9568096) + 236) + 2)
    i32_store(func26(16) + 4, (i32_load(((var10 * 404) + 9568096) + 236) + 2))
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    i32_store(var4, func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2))))
    i64_store(var4 + 8, 4294967296)
    if var1:
        var3 = 0
        while True:  # loop $label11
            var10 = i32_load((i32_load(var9 + 232) + (var3 << 2)))
            var5 = (i32_load((i32_load(var9 + 232) + (var3 << 2))) - 270)
            if (1 if ((1 if (i32_load((i32_load(var9 + 232) + (var3 << 2))) - 270) <= 31 else 0) if ((1 << var5) & -1073741823) else 0) == 0 else 0):
                var5 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var1 = var2
                    break
                var1 = (i32_load(var4 + 12) + var5)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var5))
                var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                if var5:
                    # Unknown: memory.copy []
                if var2:
                i32_store(var4, var1)
                var2 = var1
                i32_store(var4 + 8, (var5 + 1))
                i32_store((var1 + (var5 << 2)), var10)
                var1 = i32_load(var9 + 236)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) < var1 else 0):
                continue
            break  # end loop
        var5 = i32_load(var4 + 4)
    else:
    var1 = 0
    if (1 if 0 != var5 else 0):
        var3 = var2
        break
    var3 = (i32_load(var4 + 12) + var5)
    i32_store(var4 + 4, (i32_load(var4 + 12) + var5))
    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var5:
        # Unknown: memory.copy []
    if var2:
    i32_store(var4, var3)
    i32_store(var4 + 8, (var1 + 1))
    i32_store((var3 + (var1 << 2)), 234)
    var2 = i32_load(var4 + 8)
    if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
        var1 = var3
        break
    var1 = (i32_load(var4 + 12) + var2)
    i32_store(var4 + 4, (i32_load(var4 + 12) + var2))
    var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var2:
        # Unknown: memory.copy []
    i32_store(var4, var1)
    i32_store(var4 + 8, (var2 + 1))
    i32_store((var1 + (var2 << 2)), 235)
    var0 = (var6 + (var0 * 132))
    var3 = i32_load((var6 + (var0 * 132)) + 24)
    if (1 if i32_load((var6 + (var0 * 132)) + 24) == 0 else 0):
        var3 = func26(16)
        i64_store(func26(16), 0)
        i64_store(var3 + 8, 0)
        i32_store(var0 + 24, var3)
    i32_store(var3, var4)
    func29(var7, 1)
    return af(var3)


# ==========================================================
# $func845
# ==========================================================
def func845(var0, var1):
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
    var3 = (i32_load(9671128) + (var0 * 132))
    var2 = (i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110) * 286704))
    i32_store((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110) * 286704)) + 283912, (i32_load(var2 + 283912) - 1))
    var2 = (var1 & 65535)
    if (1 if func59((var5 + 12), (var5 + 8), var3, (((var1 & 65535) * 404) + 9568096)) == 0 else 0):
        break
    var4 = func34(var2, i32_load16_u(var3 + 110), i32_load(var5 + 12), i32_load(var5 + 8), 0, 1)
    if (1 if func34(var2, i32_load16_u(var3 + 110), i32_load(var5 + 12), i32_load(var5 + 8), 0, 1) == 0 else 0):
        break
    var6 = ((var1 & 0xFFFFFFFF) >> 16)
    var8 = i32_load(9671128)
    var2 = (i32_load(9671128) + (var4 * 132))
    i32_store16((i32_load(9671128) + (var4 * 132)) + 110, 0)
    i32_store(var2 + 56, i32_load16_u(var3 + 110))
    var3 = i32_load8_u(var2 + 122)
    var7 = ((i32_load8_u(var2 + 122) * 404) + 9568096)
    # br_table ['$label1', '$label2', '$label3']
    _br_idx = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 268)
    break  # br_table
    if i32_load(var2 + 52):
        i32_store(var2 + 52, ((var1 & 0xFFFFFFFF) >> 17))
    var2 = (var8 + (var4 * 132))
    if i32_load((var8 + (var4 * 132)) + 60):
        i32_store(var2 + 60, ((var1 & 0xFFFFFFFF) >> 17))
    if i32_load(var2 + 72):
        i32_store(var2 + 72, var6)
    var7 = (var8 + (var4 * 132))
    if i32_load((var8 + (var4 * 132)) + 76):
        i32_store(var7 + 76, var6)
    var4 = 480
    if (1 if i32_load(var7 + 84) == 0 else 0):
        break
    var2 = 1
    if (1 if var1 < 327680 else 0):
        break
    var6 = ((var1 & 0xFFFFFFFF) // 327680)
    var10 = (((var1 & 0xFFFFFFFF) // 327680) & 1)
    var3 = 1
    if (1 if (var1 - 327680) >= 327680 else 0):
        var6 = (var6 & 16382)
        var1 = 0
        var3 = 0
        while True:  # loop $label6
            var1 = ((var1 + 1) % var2)
            var9 = ((var1 + 2) if ((var1 + 1) % var2) else 1)
            var2 = (var2 + (1 if var1 == 0 else 0))
            var9 = (var9 % (var2 + (1 if var1 == 0 else 0)))
            var1 = (((var1 + 2) if ((var1 + 1) % var2) else 1) if (var9 % (var2 + (1 if var1 == 0 else 0))) else 0)
            var2 = (var2 + (1 if var9 == 0 else 0))
            var3 = (var3 + 2)
            if (1 if (var3 + 2) != var6 else 0):
                continue
            break  # end loop
        var3 = (var1 + 1)
    if (1 if var10 == 0 else 0):
        break
    var2 = (var2 + (1 if (var3 % var2) == 0 else 0))
    i32_store(var7 + 84, var2)
    break
    i32_store(var2 + 52, ((var6 & 0xFFFFFFFF) // i32_load(var7 + 68)))
    var4 = 624
    break
    if i32_load(var2 + 52):
        i32_store(var2 + 52, ((var1 & 0xFFFFFFFF) >> 18))
    var2 = (var8 + (var4 * 132))
    if i32_load((var8 + (var4 * 132)) + 60):
        i32_store(var2 + 60, ((var1 & 0xFFFFFFFF) >> 18))
    var4 = 528
    if (1 if i32_load(38952) == var3 else 0):
        break
    var4 = 576
    if (1 if i32_load(38956) == var3 else 0):
        break
    var4 = (672 if (1 if i32_load(38960) == var3 else 0) else 0)
    if (1 if i32_load(9142872) != i32_load16_u((var8 + (var0 * 132)) + 110) else 0):
        break
    i32_store(var5, var4)
    a_b()
    var1 = (var0 * 132)
    func29(((var0 * 132) + i32_load(9671128)), 0)
    var1 = i32_load(9671128)
    if (1 if i32_load((var1 + i32_load(9671128)) + 92) == 0 else 0):
        break
    var2 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var1 + (var0 * 132)) + 28) else 0):
            break
    global global0
    global0 = (var5 + 16)


# ==========================================================
# $func923
# ==========================================================
def func923(var0, var1):
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
    var6 = i32_load(9671128)
    var5 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load(9142848) < (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        func29(var5, 1)
        return
    var2 = (var6 + (var1 * 132))
    var4 = ((i32_load8_u((var6 + (var1 * 132)) + 122) * 404) + 9568096)
    var10 = i32_load(((i32_load8_u((var6 + (var1 * 132)) + 122) * 404) + 9568096) + 220)
    var3 = i32_load16_u(var2 + 114)
    var7 = (i32_load(((i32_load8_u((var6 + (var1 * 132)) + 122) * 404) + 9568096) + 220) + i32_load16_u(var2 + 114))
    var11 = i32_load(var4 + 216)
    var8 = i32_load16_u(var2 + 112)
    var9 = (i32_load(var4 + 216) + i32_load16_u(var2 + 112))
    var2 = i32_load16_u(var5 + 114)
    var4 = i32_load16_u(var5 + 112)
    var12 = (1 if i32_load16_u(var5 + 112) < var8 else 0)
    if (1 if i32_load16_u(var5 + 112) < var8 else 0):
        break
    if (1 if var4 >= var9 else 0):
        break
    if (1 if var2 < var3 else 0):
        break
    if (1 if var2 >= var7 else 0):
        break
    var3 = ((var10 // 2) + var3)
    var2 = (-1 if (1 if var2 > var3 else 0) else (1 if ((var10 // 2) + var3) != var2 else 0))
    var3 = ((var11 // 2) + var8)
    break
    var2 = (1 if (1 if var2 < var3 else 0) else (-1 if (1 if var2 >= var7 else 0) else 0))
    var4 = (1 if var12 else (-1 if (1 if var4 >= var9 else 0) else 0))
    var3 = 6
    var0 = (var6 + (var0 * 132))
    var2 = (((var2 * 3) + var4) + 4)
    if (1 if (((var2 * 3) + var4) + 4) <= 8 else 0):
    else:
    i32_store8(i32_load8_u((var2 + 10184)) + 124, 6)
    var0 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 276)
    func63(func37(var5, i32_load(((i32_load8_u(var0 + 122) * 72) + 9263856) + 8), 0.0, 0), var5, 50, var1, (i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 276) if var0 else 25))
    return (var6 + (var0 * 132))

