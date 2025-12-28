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
# $func360
# ==========================================================
def func360(var0, var1):
    var2 = 0
    var3 = 0
    if i32_load8_u(9147210):
        func41(5, 9173808, var1, var0, (7 if var0 else 0))
        return
    var3 = (var1 << 2)
    var2 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var1:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9213864)]


# ==========================================================
# $func363
# ==========================================================
def func363(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var4 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(var4 + 12, var1)
    var2 = (global0 - 208)
    global global0
    global0 = (global0 - 208)
    i32_store(var2 + 204, var1)
    var1 = (var2 + 160)
    # Unknown: memory.fill []
    i32_store(var2 + 200, i32_load(var2 + 204))
    if (1 if func352(0, var0, (var2 + 200), (var2 + 80), var1) < 0 else 0):
        break
    if (1 if i32_load(52668) >= 0 else 0):
        var1 = i32_load(global3 + 24)
        if (1 if i32_load(global3 + 24) == (i32_load(52668) & -1073741825) else 0):
            break
        var3 = 1
        if (1 if var1 == 0 else 0):
            break
        var7 = (var1 | 1073741824)
        var1 = (var1 | 1073741824)
        if (1 if (var1 | 1073741824) == 0 else 0):
            break
        while True:  # loop $label3
            var5 = (var1 | 1073741824)
            if (1 if (var1 & 1073741824) == 0 else 0):
                if (1 if var1 != var5 else 0):
                    break
            func439(52668, var5)
            var1 = var7
            if var7:
                continue
            break  # end loop
    var1 = i32_load(52592)
    if (1 if i32_load(52664) <= 0 else 0):
        i32_store(52592, (var1 & -33))
    if (1 if i32_load(52640) == 0 else 0):
        i32_store(52640, 80)
        i32_store(52620, 0)
        i64_store(52608, 0)
        var6 = i32_load(52636)
        i32_store(52636, var2)
        break
    if i32_load(52608):
        break
    if func433(52592):
        break
    var0 = func352(52592, var0, (var2 + 200), (var2 + 80), (var2 + 160))
    if var6:
        # call_indirect via table[i32_load(52628)]
        i32_store(52640, 0)
        i32_store(52636, var6)
        i32_store(52620, 0)
        i64_store(52608, 0)
    else:
    i32_store(52592, (i32_load(52592) | (var1 & 32)))
    if (1 if var3 == 0 else 0):
        break
    if (0 & 1073741824):
        func97(52668)
    global global0
    global0 = (var2 + 208)
    global global0
    global0 = (var4 + 16)
    return 52668


# ==========================================================
# $func375
# ==========================================================
def func375(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0.0
    var3 = func244(i32_load(9142588))
    var0 = i32_load(9142588)
    if (1 if i32_load(9142588) == 0 else 0):
        break
    var1 = i32_load(var0 + 16)
    var0 = i32_load(var0 + 24)
    if (1 if i32_load(var0 + 24) >= 100 else 0):
        var4 = f32_load((((var0 + var1) << 2) + 32700))
        if (1 if ((1 if f32_load((((var0 + var1) << 2) + 32700)) < 4294967300.0 else 0) & (1 if var4 >= 0.0 else 0)) == 0 else 0):
            break
        var2 = int(var4)
        break
    var2 = ((var1 * 1000) // var0)


# ==========================================================
# $func376
# ==========================================================
def func376(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var3 = (i32_load(var1 + 52) + i32_load(var0 + 52))
    i32_store(var1 + 52, (i32_load(var1 + 52) + i32_load(var0 + 52)))
    var4 = (i32_load(var1 + 60) + i32_load(var0 + 60))
    i32_store(var1 + 60, (i32_load(var1 + 60) + i32_load(var0 + 60)))
    if i32_load(var0 + 84):
        var2 = i32_load(var1 + 84)
        var7 = i32_load(9561692)
        while True:  # loop $label0
            i32_store(var1 + 80, 0)
            var5 = (var2 + 1)
            i32_store(var1 + 84, (var2 + 1))
            var2 = (var7 + (i32_load16_u(var1 + 110) * 286704))
            var6 = ((var7 + (i32_load16_u(var1 + 110) * 286704)) + 281672)
            i32_store(((var7 + (i32_load16_u(var1 + 110) * 286704)) + 281672), (i32_load(var6) + 1))
            if (1 if i32_load((var2 + 284388)) == var5 else 0):
                func201(var1)
                i32_store(var2 + 283936, (i32_load(var2 + 283936) + 1))
                var3 = (var2 + 281636)
                i32_store((var2 + 281636), (i32_load(var3) + 1))
                var4 = i32_load(var1 + 60)
                var7 = i32_load(9561692)
                var3 = i32_load(var1 + 52)
            var2 = (var2 + 284020)
            i32_store(var1 + 64, (i32_load(var1 + 64) + i32_load((var2 + 284020))))
            i32_store(var1 + 68, (i32_load(var1 + 68) + i32_load(var2)))
            var2 = i32_load(var1 + 84)
            var5 = (var2 & 1)
            var6 = (1 if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 224) > 1 else 0)
            var4 = (((1 if (i32_load(var1 + 84) & 3) == 1 else 0) if (1 if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 224) > 1 else 0) else (var2 & 1)) + var4)
            i32_store(var1 + 60, (((1 if (i32_load(var1 + 84) & 3) == 1 else 0) if (1 if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 224) > 1 else 0) else (var2 & 1)) + var4))
            var3 = ((var5 if var6 else 1) + var3)
            i32_store(var1 + 52, ((var5 if var6 else 1) + var3))
            var8 = (var8 + 1)
            if (1 if (var8 + 1) < i32_load(var0 + 84) else 0):
                continue
            break  # end loop
    var2 = i32_load(var1 + 72)
    var3 = i32_load(var0 + 72)
    if (1 if i32_load(var0 + 72) == 0 else 0):
        break
    if var2:
        break
    var2 = i32_load(var1 + 72)
    var3 = i32_load(var0 + 72)
    i32_store(var1 + 72, (var2 + var3))
    i32_store(var1 + 76, (i32_load(var1 + 76) + i32_load(var0 + 76)))
    var0 = i32_load(var0 + 80)
    i32_store(var1 + 64, (i32_load(var0 + 80) + i32_load(var1 + 64)))
    i32_store(var1 + 68, (var0 + i32_load(var1 + 68)))
    if (1 if i32_load(var1 + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load(var1 + 28) else 0):
            break


# ==========================================================
# $func377
# ==========================================================
def func377(var0, param1):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var0 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var1 = i32_load(9671128)
    var1 = (i32_load(9671128) + (i32_load((i32_load(i32_load((var1 + (i32_load(9173808) * 132)) + 16)) + ((i32_load(9213816) + (i32_load(9147120) * i32_load(9143000))) << 2))) * 132))
    var2 = i32_load((i32_load(9671128) + (i32_load((i32_load(i32_load((var1 + (i32_load(9173808) * 132)) + 16)) + ((i32_load(9213816) + (i32_load(9147120) * i32_load(9143000))) << 2))) * 132)) + 28)
    i32_store(var0 + 12, i32_load((i32_load(9671128) + (i32_load((i32_load(i32_load((var1 + (i32_load(9173808) * 132)) + 16)) + ((i32_load(9213816) + (i32_load(9147120) * i32_load(9143000))) << 2))) * 132)) + 28))
    var3 = i32_load8_u(var1 + 122)
    var4 = i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 172)
    if (1 if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 172) == 0 else 0):
        break
    if i32_load(9213812):
        break
    if i32_load8_u(9163793):
        if (1 if i32_load(((var3 * 404) + 9568096) + 268) > 1 else 0):
            break
        if i32_load8_u(9147210):
            func41(39, (var0 + 12), 1, 0, 0)
            break
        var1 = func26(4)
        i32_store(func26(4), var2)
        # call_indirect via table[i32_load(9214136)]
        break
    var2 = ((var4 * 132) + 9216080)
    # call_indirect via table[i32_load(var2)]
    i32_store(9142896, i32_load(var1 + 28))
    break
    if i32_load8_u(9147210):
        func41(1, (var0 + 12), 1, 0, 0)
        break
    var1 = func26(4)
    i32_store(func26(4), var2)
    # call_indirect via table[i32_load(9213832)]
    global global0
    global0 = (var0 + 16)


# ==========================================================
# $func383
# ==========================================================
def func383(var0, param1):
    var1 = 0
    if var0:
        i32_atomic_store(var0 + 108, 0)
        if (1 if i32_load(var0) == 0 else 0):
            break
        var1 = i32_load16_u(var0 + 40)
        if (1 if i32_load16_u(var0 + 40) > 4 else 0):
            break
        if (1 if var1 == 4 else 0):
            break
        var1 = i32_load(var0 + 152)
        if (1 if i32_load(var0 + 152) == 0 else 0):
            break
        i32_store16(var0 + 42, 65535)
        i64_store(var0 + 44, i64_load(8825))
        i64_store(var0 + 52, i64_load(8833))
        i64_store(var0 + 60, i64_load(8841))
        i64_store(var0 + 68, i64_load(8849))
        i64_store(var0 + 74, i64_load(8855))
        # call_indirect via table[var1]
        func246(var0)


# ==========================================================
# $func401
# ==========================================================
def func401(var0, var1, var2):
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
    var5 = i32_load(9681936)
    if i32_load(i32_load(9681936) + 8):
        var9 = (var1 + var2)
        var13 = (var0 + var2)
        var10 = i32_load(9684500)
        var11 = i32_load(9684496)
        while True:  # loop $label9
            var12 = (i32_load(var5) + (var4 << 2))
            var6 = i32_load((i32_load(var5) + (var4 << 2)))
            var2 = 0
            var8 = i32_load((var11 - 16))
            if i32_load((var11 - 16)):
                while True:  # loop $label1
                    var3 = (var11 + (var2 * 60))
                    if (1 if i32_load((var11 + (var2 * 60)) + 52) == var6 else 0):
                        break
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != var8 else 0):
                        continue
                    break  # end loop
            var2 = 0
            var3 = var10
            if (1 if i32_load(var10 + 52) == var6 else 0):
                break
            while True:  # loop $label2
                var2 = (var2 + 1)
                var3 = (var10 + ((var2 + 1) * 60))
                if (1 if i32_load((var10 + ((var2 + 1) * 60)) + 52) != var6 else 0):
                    continue
                break  # end loop
            var6 = (i32_load(var3 + 4) // (i32_load(var3 + 20) * i32_load(var3 + 16)))
            var7 = (i32_load(var12 + 8) - i32_load(var3 + 12))
            var2 = (i32_load(var12 + 4) - i32_load(var3 + 8))
            var8 = ((1 if (i32_load(var12 + 4) - i32_load(var3 + 8)) > var0 else 0) & (1 if var2 < var13 else 0))
            if (1 if ((1 if (i32_load(var12 + 4) - i32_load(var3 + 8)) > var0 else 0) & (1 if var2 < var13 else 0)) == 0 else 0):
                break
            if (1 if var1 >= var7 else 0):
                break
            if (1 if var7 < var9 else 0):
                break
            var2 = (i32_load(var3) + var2)
            var2 = ((1 if (i32_load(var3) + var2) > var0 else 0) & (1 if var2 < var13 else 0))
            if (1 if var1 >= var7 else 0):
                break
            if (1 if var2 == 0 else 0):
                break
            if (1 if var7 < var9 else 0):
                break
            if (1 if var2 == 0 else 0):
                break
            var2 = (var6 + var7)
            if (1 if (var6 + var7) <= var1 else 0):
                break
            if (1 if var2 < var9 else 0):
                break
            if (1 if var8 == 0 else 0):
                break
            var2 = (var6 + var7)
            if (1 if (var6 + var7) <= var1 else 0):
                break
            if (1 if var2 >= var9 else 0):
                break
            func38(i32_load(var12 + 12))
            var5 = i32_load(9681936)
            var2 = (i32_load(var5 + 8) - 4)
            i32_store(i32_load(9681936) + 8, (i32_load(var5 + 8) - 4))
            var10 = i32_load(9684500)
            var11 = i32_load(9684496)
            if (1 if var2 > var4 else 0):
                var8 = i32_load(var5)
                var2 = var4
                while True:  # loop $label8
                    var3 = (var8 + (var2 << 2))
                    i32_store((var8 + (var2 << 2)), i32_load(var3 + 16))
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) < i32_load(var5 + 8) else 0):
                        continue
                    break  # end loop
            var4 = (var4 - 4)
            var4 = (var4 + 4)
            if (1 if (var4 + 4) < i32_load(var5 + 8) else 0):
                continue
            break  # end loop


# ==========================================================
# $Nb
# Export: Nb
# ==========================================================
def Nb():
    """Export: Nb"""
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
    var1 = i32_load8_u(9147210)
    if (1 if i32_load8_u(9147210) == 0 else 0):
        i32_store(9142872, 1)
        break
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var4 = i32_load(9142384)
    var5 = i32_load(9561692)
    var0 = 1
    while True:  # loop $label2
        if (1 if i32_load((var5 + (var0 * 286704)) + 284616) == var4 else 0):
            break
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var2 else 0):
            continue
        break  # end loop
    var0 = 0
    i32_store(9142872, var0)
    i32_store(9142892, i32_load(41092))
    var10 = i32_load(9561692)
    i32_store16(i32_load(9561692) + 283972, 65535)
    i32_store8((var10 + 283974), 255)
    var3 = i32_load(9142424)
    var4 = i32_load(i32_load(9142424) + 16)
    var0 = (1 if i32_load(i32_load(9142424) + 16) == 991915600 else 0)
    i32_store8(9216060, (1 if i32_load(i32_load(9142424) + 16) == 991915600 else 0))
    var6 = i32_load(var3 + 4)
    var11 = i32_load(var3 + 4)
    var7 = i32_load(var3 + 8)
    var12 = i32_load(var3 + 8)
    var8 = i32_load(var3 + 12)
    var9 = i32_load(var3 + 12)
    var5 = var4
    var2 = i32_load(var3 + 44)
    if (1 if i32_load(var3 + 44) >= 101 else 0):
        var2 = ((var2 * 15) - 1500)
        var5 = ((((((var2 * 15) - 1500) * var4) & 0xFFFFFFFF) // 100) + var4)
        var12 = ((((var2 * var7) & 0xFFFFFFFF) // 100) + var7)
        var11 = ((((var2 * var6) & 0xFFFFFFFF) // 100) + var6)
        var9 = ((((var2 * var8) & 0xFFFFFFFF) // 100) + var8)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var4 = (0 if var0 else var4)
    var2 = 1
    if (1 if var1 == 0 else 0):
        while True:  # loop $label6
            var0 = (var10 + (var2 * 286704))
            if (1 if i32_load((var10 + (var2 * 286704)) + 283960) <= 2 else 0):
                var1 = i32_load(var0 + 284616)
                break
            var1 = i32_load(var0 + 284616)
            i32_store((var0 + 283960), ((i32_load(var0 + 284616) + i32_load(var3 + 184)) % 3))
            if (1 if ((1 if var1 == 0 else 0) & (1 if var2 > 1 else 0)) == 0 else 0):
                var1 = i32_load(var0 + 286684)
                break
            var1 = i32_load(var3 + 44)
            i32_store(var0 + 286684, i32_load(var3 + 44))
            i32_store(var0 + 286688, i32_load(var3 + 52))
            i32_store(var0 + 283848, (var11 if var1 else var6))
            i32_store((var0 + 283860), (var5 if var1 else var4))
            i32_store((var0 + 283856), (var9 if var1 else var8))
            i32_store((var0 + 283852), (var12 if var1 else var7))
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < i32_load(9142892) else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    while True:  # loop $label9
        var0 = (var10 + (var2 * 286704))
        if (1 if i32_load((var10 + (var2 * 286704)) + 283960) <= 2 else 0):
            var1 = i32_load(var0 + 284616)
            break
        var1 = i32_load(var0 + 284616)
        i32_store((var0 + 283960), ((i32_load(var0 + 284616) + i32_load(var3 + 184)) % 3))
        if var1:
            var1 = i32_load(var0 + 286684)
            break
        var1 = i32_load(var3 + 44)
        i32_store(var0 + 286684, i32_load(var3 + 44))
        i32_store(var0 + 286688, i32_load(var3 + 52))
        i32_store(var0 + 283848, (var11 if var1 else var6))
        i32_store((var0 + 283860), (var5 if var1 else var4))
        i32_store((var0 + 283856), (var9 if var1 else var8))
        i32_store((var0 + 283852), (var12 if var1 else var7))
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop

