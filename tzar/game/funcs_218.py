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
# $func146
# ==========================================================
def func146(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var3 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var2 = i32_load(9671128)
    var4 = (var0 * 132)
    var5 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var5 + 128) == 0 else 0):
        break
    var0 = (var2 + (var0 * 132))
    i32_store8((var2 + (var0 * 132)) + 127, 0)
    var2 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var3 + 20, var2)
        i32_store(var3 + 16, 0)
        a_b()
        break
    var0 = i32_load16_u(var0 + 110)
    i32_store(var3 + 4, var2)
    i32_store(var3, (var0 + 16))
    a_b()
    i32_store8(var5 + 128, 0)
    var2 = i32_load(9671128)
    var0 = (var2 + var4)
    var2 = i32_load16_u(var0 + 116)
    var5 = i32_load16_u(var0 + 118)
    var4 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 96)
    var4 = (i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 96) - (var4 % 25))
    global global0
    global0 = (var3 + 32)


# ==========================================================
# $func202
# ==========================================================
def func202(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var3 = i32_load(var0 + 16)
    if i32_load(var0 + 16):
        var4 = i32_load(var3 + 8)
        var5 = func26((-1 if (1 if var4 > 1073741823 else 0) else (i32_load(var3 + 8) << 2)))
        if (1 if var4 == 0 else 0):
            break
        var7 = i32_load(var3)
        var3 = 0
        if (1 if var4 >= 4 else 0):
            var8 = (var4 & -4)
            while True:  # loop $label1
                var6 = (var3 << 2)
                i32_store((var5 + (var3 << 2)), i32_load((var6 + var7)))
                var9 = (var6 | 4)
                i32_store((var5 + (var6 | 4)), i32_load((var7 + var9)))
                var9 = (var6 | 8)
                i32_store((var5 + (var6 | 8)), i32_load((var7 + var9)))
                var6 = (var6 | 12)
                i32_store((var5 + (var6 | 12)), i32_load((var6 + var7)))
                var3 = (var3 + 4)
                var10 = (var10 + 4)
                if (1 if (var10 + 4) != var8 else 0):
                    continue
                break  # end loop
        var6 = (var4 & 3)
        if (var4 & 3):
            while True:  # loop $label2
                var8 = (var3 << 2)
                i32_store((var5 + (var3 << 2)), i32_load((var7 + var8)))
                var3 = (var3 + 1)
                var11 = (var11 + 1)
                if (1 if (var11 + 1) != var6 else 0):
                    continue
                break  # end loop
        if (1 if var4 == 0 else 0):
            break
        var3 = 0
        while True:  # loop $label3
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var4 else 0):
                continue
            break  # end loop
        if (1 if var1 == 0 else 0):
            break
        if i32_load8_u(9147210):
            if (1 if i32_load(59164) != i32_load(9142384) else 0):
                break
        if (1 if var4 == 0 else 0):
            break
        var1 = i32_load(9671128)
        var3 = 0
        while True:  # loop $label5
            var2 = (var1 + (i32_load((var5 + (var3 << 2))) * 132))
            if (1 if i32_load((var1 + (i32_load((var5 + (var3 << 2))) * 132)) + 36) == 0 else 0):
                func44(var2, 0)
                var1 = i32_load(9671128)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var4 else 0):
                continue
            break  # end loop
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    var1 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
            break


# ==========================================================
# $func351
# ==========================================================
def func351(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10):
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
    var21 = 0
    var22 = 0
    var23 = 0
    var24 = 0
    var25 = 0
    var26 = 0
    var27 = 0
    var28 = 0
    var29 = 0
    var14 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var19 = i32_load8_u(var0 + 122)
    var11 = i32_load(9671128)
    var18 = (i32_load(9671128) + (var3 * 132))
    var12 = i32_load8_u((i32_load(9671128) + (var3 * 132)) + 122)
    if ((1 if var4 != -1 else 0) & (1 if i32_load8_u((i32_load(9671128) + (var3 * 132)) + 122) != var4 else 0)):
        break
    var16 = i32_load16_u(var18 + 110)
    if (1 if i32_load(38500) == var12 else 0):
        break
    var13 = (i32_load(9142892) * var6)
    var15 = i32_load(9143004)
    var17 = i32_load16_u((var11 + (var3 * 132)) + 120)
    if i32_load16_u((var11 + (var3 * 132)) + 120):
    else:
    if (1 if i32_load8_u(((var17 if i32_load8_u((var15 + (var13 + var16))) else var16) + (var16 + var13))) == 0 else 0):
        var5 = (var11 + (var3 * 132))
        if ((1 if var5 == 0 else 0) & (1 if i32_load8_u((var11 + (var3 * 132)) + 127) != 6 else 0)):
            break
        if (1 if i32_load8_u(var5 + 128) == 0 else 0):
            break
        break
    if i32_load8_u((var11 + (var3 * 132)) + 128):
        break
    var5 = (var11 + (var3 * 132))
    var13 = i32_load8_u((var11 + (var3 * 132)) + 125)
    if (1 if i32_load8_u((var11 + (var3 * 132)) + 125) == 10 else 0):
        break
    if (1 if i32_load8_u(var5 + 126) == 2 else 0):
        break
    var15 = i32_load(var5 + 64)
    if (1 if i32_load(var5 + 64) == -1 else 0):
        break
    var5 = ((var12 * 404) + 9568096)
    var17 = i32_load(((var12 * 404) + 9568096) + 264)
    if (1 if i32_load(((var12 * 404) + 9568096) + 264) == 2 else 0):
        break
    if (1 if i32_load(var5 + 188) != 55 else 0):
        break
    if (1 if i32_load(38560) == var12 else 0):
        break
    if (1 if i32_load(38620) == var12 else 0):
        break
    if (1 if i32_load(38564) == var12 else 0):
        break
    var20 = i32_load((var11 + (var3 * 132)) + 28)
    if (1 if func162(var0, var12, var13, i32_load((var11 + (var3 * 132)) + 28)) == 0 else 0):
        break
    var21 = i32_load(var8 + 286684)
    if i32_load(var8 + 286684):
        # br_table ['$label3', '$label4', '$label4', '$label4', '$label3', '$label4']
        _br_idx = var17
        break  # br_table
        var8 = ((var12 * 404) + 9568096)
        var22 = i32_load(((var12 * 404) + 9568096) + 216)
        if (1 if i32_load(((var12 * 404) + 9568096) + 216) == 0 else 0):
            var5 = 0
            break
        var5 = 0
        var23 = i32_load(var8 + 220)
        if (1 if i32_load(var8 + 220) == 0 else 0):
            break
        var8 = i32_load(9215880)
        if (1 if i32_load(9215880) == 0 else 0):
            break
        var24 = i32_load(9142432)
        if (1 if i32_load(9142432) == 0 else 0):
            break
        var5 = (var11 + (var3 * 132))
        var25 = i32_load16_u((var11 + (var3 * 132)) + 114)
        var26 = i32_load16_u(var5 + 112)
        var27 = i32_load(9142440)
        var28 = i32_load(var8)
        var13 = 0
        while True:  # loop $label7
            var29 = (var13 + var26)
            var8 = 0
            while True:  # loop $label6
                var5 = i32_load((var24 + ((var29 + ((var8 + var25) * var27)) << 2)))
                if (1 if i32_load((var28 + (i32_load((var24 + ((var29 + ((var8 + var25) * var27)) << 2))) << 2))) == 0 else 0):
                    break
                var8 = (var8 + 1)
                if (1 if (var8 + 1) != var23 else 0):
                    continue
                break  # end loop
            var5 = 0
            var13 = (var13 + 1)
            if (1 if (var13 + 1) != var22 else 0):
                continue
            break  # end loop
        break
        var5 = 0
        var8 = i32_load(9142432)
        if (1 if i32_load(9142432) == 0 else 0):
            break
        var5 = (var11 + (var3 * 132))
        var5 = i32_load((var8 + (((i32_load(9142440) * i32_load16_u((var11 + (var3 * 132)) + 114)) + i32_load16_u(var5 + 112)) << 2)))
        if (1 if var5 != var7 else 0):
            break
    if (1 if var4 != -1 else 0):
        break
    if var21:
        break
    if (1 if i32_load8_u(((var12 * 404) + 9568096) + 380) == 0 else 0):
        break
    if (1 if var15 > 1 else 0):
        break
    var4 = i32_load(((var19 * 404) + 9568096) + 228)
    if i32_load(((var19 * 404) + 9568096) + 228):
        var5 = (i32_load16_u(var0 + 114) - var10)
        var5 = (i32_load16_u(var0 + 112) - var9)
        if (1 if (((i32_load16_u(var0 + 114) - var10) * var5) + ((i32_load16_u(var0 + 112) - var9) * var5)) < (var4 * var4) else 0):
            break
    var4 = i32_load((var11 + (var3 * 132)) + 100)
    if i32_load((var11 + (var3 * 132)) + 100):
        var4 = (var11 + (var4 * 132))
        if (1 if (var15 + 5) < (((i32_load((((i32_load8_u((var11 + (var4 * 132)) + 122) * 1020) + 9299904) + (var12 << 2))) * i32_load(var4 + 52)) & 0xFFFFFFFF) // 100) else 0):
            break
    if (1 if var17 == 1 else 0):
        if (1 if i32_load((var11 + (var3 * 132)) + 84) < i32_load(((var12 * 404) + 9568096) + 112) else 0):
            break
    var5 = (i32_load(9671128) + (var20 * 132))
    var4 = (i32_load16_u(var0 + 114) - i32_load16_u((i32_load(9671128) + (var20 * 132)) + 114))
    var4 = (i32_load16_u(var0 + 112) - i32_load16_u(var5 + 112))
    var4 = (((i32_load16_u(var0 + 114) - i32_load16_u((i32_load(9671128) + (var20 * 132)) + 114)) * var4) + ((i32_load16_u(var0 + 112) - i32_load16_u(var5 + 112)) * var4))
    var5 = ((i32_load8_u(var5 + 122) * 404) + 9568096)
    if (1 if i32_load(((i32_load8_u(var5 + 122) * 404) + 9568096) + 264) == 1 else 0):
        var4 = (var4 if (1 if i32_load(var5 + 268) == 1 else 0) else (var4 + 100))
    if (1 if i32_load(var1) <= var4 else 0):
        break
    if (1 if i32_load(var0 + 28) == var3 else 0):
        break
    i32_store(var2, var3)
    i32_store(var1, var4)
    if (1 if i32_load8_u(((var19 * 404) + 9568096) + 336) == 0 else 0):
        break
    if (1 if i32_load8_u((i32_load(9143004) + ((i32_load(9142892) * var16) + var6))) == 0 else 0):
        break
    var0 = (var11 + (var3 * 132))
    if (1 if i32_load8_u((var11 + (var3 * 132)) + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var0 + 128) == 0 else 0):
        break
    var1 = (var11 + (var3 * 132))
    i32_store8((var11 + (var3 * 132)) + 127, 0)
    var1 = i32_load(var1 + 40)
    if (1 if i32_load(var1 + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var14 + 20, var1)
        i32_store(var14 + 16, 0)
        a_b()
        break
    var2 = i32_load16_u(var18 + 110)
    i32_store(var14 + 4, var1)
    i32_store(var14, (var2 + 16))
    a_b()
    i32_store8(var0 + 128, 0)
    func290(var18)
    global global0
    global0 = (var14 + 32)
    return var14


# ==========================================================
# $func368
# ==========================================================
def func368(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var1 = i32_load(9671128)
    func148(var0, 9147392, 0)
    var3 = (var1 + (var0 * 132))
    var5 = i32_load(9147420)
    # br_table ['$label0', '$label1', '$label2']
    _br_idx = (i32_load(9147420) - 2147483646)
    break  # br_table
    var2 = 2
    i32_store8(var3 + 126, 2)
    var5 = 0
    break
    var2 = i32_load8_u(var3 + 126)
    if (1 if i32_load8_u(var3 + 126) != 2 else 0):
        break
    var2 = 0
    i32_store8(var3 + 126, 0)
    var6 = i32_load(9215884)
    var7 = (var1 + (var0 * 132))
    var4 = i32_load((var1 + (var0 * 132)) + 44)
    if (1 if i32_load((i32_load(9215884) + (i32_load((var1 + (var0 * 132)) + 44) << 4)) + 4) != 51 else 0):
        break
    if var4:
        i32_store((var6 + (var4 << 4)), 0)
    i32_store(var7 + 44, 0)
    var4 = (var1 + (var0 * 132))
    if (1 if var5 == i32_load16_u((var1 + (var0 * 132)) + 110) else 0):
        break
    if (1 if i32_load(((i32_load8_u(var4 + 122) * 404) + 9568096) + 188) != 55 else 0):
        break
    func78(var3, var5, 1, 1)
    var2 = i32_load8_u((var1 + (var0 * 132)) + 126)
    if (1 if var2 != 2 else 0):
        break
    var0 = (var1 + (var0 * 132))
    if (1 if i32_load(((i32_load8_u((var1 + (var0 * 132)) + 122) * 404) + 9568096) + 264) == 2 else 0):
        break


# ==========================================================
# $func387
# ==========================================================
def func387(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = i32_load(var0 + 283908)
    if (1 if i32_load(var0 + 283908) == 0 else 0):
        break
    if i32_load8_u(var0 + 286696):
        break
    if i32_load8_u(9147152):
        break
    if func386(var0):
        break
    if (1 if i32_load(i32_load(9142424) + 80) == 0 else 0):
        break
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var5 = i32_load(var0 + 284608)
    if (1 if i32_load(var0 + 284608) == 0 else 0):
        break
    var6 = i32_load(9561692)
    var1 = 1
    while True:  # loop $label3
        if (1 if var1 == var2 else 0):
            break
        var3 = (var6 + (var1 * 286704))
        if i32_load8_u((var6 + (var1 * 286704)) + 286696):
            break
        if (1 if i32_load(var3 + 284608) != var5 else 0):
            break
        if func386(var3):
            break
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var4 else 0):
            continue
        break  # end loop
    if (1 if i32_load(9671136) >= 4 else 0):
        var2 = i32_load(var0 + 283908)
        var1 = 3
        while True:  # loop $label5
            var3 = (i32_load(9671128) + (var1 * 132))
            if (1 if var2 != i32_load16_u((i32_load(9671128) + (var1 * 132)) + 110) else 0):
                break
            if i32_load8_u(((i32_load8_u(var3 + 122) * 404) + 9568096) + 332):
                func78(var3, 0, 0, 1)
                break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < i32_load(9671136) else 0):
                continue
            break  # end loop
    if (1 if i32_load(i32_load(9142424) + 80) == 0 else 0):
        break
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var1 = i32_load(var0 + 284608)
    if (1 if i32_load(var0 + 284608) == 0 else 0):
        break
    var4 = i32_load(9561692)
    var3 = 1
    while True:  # loop $label9
        if (1 if var1 == 0 else 0):
            break
        var1 = (var4 + (var3 * 286704))
        if (1 if var1 != i32_load((var4 + (var3 * 286704)) + 284608) else 0):
            break
        if (1 if i32_load(9671136) >= 4 else 0):
            var4 = i32_load(var1 + 283908)
            var1 = 3
            while True:  # loop $label8
                var2 = (i32_load(9671128) + (var1 * 132))
                if (1 if var4 != i32_load16_u((i32_load(9671128) + (var1 * 132)) + 110) else 0):
                    break
                if i32_load8_u(((i32_load8_u(var2 + 122) * 404) + 9568096) + 332):
                    func78(var2, 0, 0, 1)
                    break
                var1 = (var1 + 1)
                if (1 if (var1 + 1) < i32_load(9671136) else 0):
                    continue
                break  # end loop
        var2 = i32_load(9142892)
        var4 = i32_load(9561692)
        var3 = (var3 + 1)
        if (1 if (var3 + 1) >= var2 else 0):
            break
        var1 = i32_load(var0 + 284608)
        continue
        break  # end loop
    raise RuntimeError('unreachable')

