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
# $func197
# ==========================================================
def func197(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var4 = (global0 - 32)
    var5 = (i32_load(var2 + 12) * i32_load(var2 + 8))
    var6 = (i32_load(var1 + 12) * i32_load(var1 + 8))
    if (1 if (i32_load(var1 + 12) * i32_load(var1 + 8)) <= (i32_load(var0 + 12) * i32_load(var0 + 8)) else 0):
        if (1 if var5 <= var6 else 0):
            break
        i32_store(var4 + 24, i32_load(var1 + 24))
        i64_store(var4 + 16, i64_load(var1 + 16))
        i64_store(var4 + 8, i64_load(var1 + 8))
        i64_store(var4, i64_load(var1))
        i32_store(var1 + 24, i32_load(var2 + 24))
        i64_store(var1 + 16, i64_load(var2 + 16))
        i64_store(var1 + 8, i64_load(var2 + 8))
        i64_store(var1, i64_load(var2))
        i32_store(var2 + 24, i32_load(var4 + 24))
        i64_store(var2 + 16, i64_load(var4 + 16))
        i64_store(var2 + 8, i64_load(var4 + 8))
        i64_store(var2, i64_load(var4))
        if (1 if (i32_load(var1 + 12) * i32_load(var1 + 8)) <= (i32_load(var0 + 12) * i32_load(var0 + 8)) else 0):
            break
        i32_store(var4 + 24, i32_load(var0 + 24))
        i64_store(var4 + 16, i64_load(var0 + 16))
        i64_store(var4 + 8, i64_load(var0 + 8))
        i64_store(var4, i64_load(var0))
        i32_store(var0 + 24, i32_load(var1 + 24))
        i64_store(var0 + 16, i64_load(var1 + 16))
        i64_store(var0 + 8, i64_load(var1 + 8))
        i64_store(var0, i64_load(var1))
        i32_store(var1 + 24, i32_load(var4 + 24))
        i64_store(var1 + 16, i64_load(var4 + 16))
        i64_store(var1 + 8, i64_load(var4 + 8))
        i64_store(var1, i64_load(var4))
        break
    if (1 if var5 > var6 else 0):
        i32_store(var4 + 24, i32_load(var0 + 24))
        i64_store(var4 + 16, i64_load(var0 + 16))
        i64_store(var4 + 8, i64_load(var0 + 8))
        i64_store(var4, i64_load(var0))
        i32_store(var0 + 24, i32_load(var2 + 24))
        i64_store(var0 + 16, i64_load(var2 + 16))
        i64_store(var0 + 8, i64_load(var2 + 8))
        i64_store(var0, i64_load(var2))
        i32_store(var2 + 24, i32_load(var4 + 24))
        i64_store(var2 + 16, i64_load(var4 + 16))
        i64_store(var2 + 8, i64_load(var4 + 8))
        i64_store(var2, i64_load(var4))
        break
    i32_store(var4 + 24, i32_load(var0 + 24))
    i64_store(var4 + 16, i64_load(var0 + 16))
    i64_store(var4 + 8, i64_load(var0 + 8))
    i64_store(var4, i64_load(var0))
    i32_store(var0 + 24, i32_load(var1 + 24))
    i64_store(var0 + 16, i64_load(var1 + 16))
    i64_store(var0 + 8, i64_load(var1 + 8))
    i64_store(var0, i64_load(var1))
    i32_store(var1 + 24, i32_load(var4 + 24))
    i64_store(var1 + 16, i64_load(var4 + 16))
    i64_store(var1 + 8, i64_load(var4 + 8))
    i64_store(var1, i64_load(var4))
    if (1 if (i32_load(var2 + 12) * i32_load(var2 + 8)) <= (i32_load(var1 + 12) * i32_load(var1 + 8)) else 0):
        break
    i32_store(var4 + 24, i32_load(var1 + 24))
    i64_store(var4 + 16, i64_load(var1 + 16))
    i64_store(var4 + 8, i64_load(var1 + 8))
    i64_store(var4, i64_load(var1))
    i32_store(var1 + 24, i32_load(var2 + 24))
    i64_store(var1 + 16, i64_load(var2 + 16))
    i64_store(var1 + 8, i64_load(var2 + 8))
    i64_store(var1, i64_load(var2))
    i32_store(var2 + 24, i32_load(var4 + 24))
    i64_store(var2 + 16, i64_load(var4 + 16))
    i64_store(var2 + 8, i64_load(var4 + 8))
    i64_store(var2, i64_load(var4))
    var5 = 2
    if (1 if (i32_load(var3 + 12) * i32_load(var3 + 8)) > (i32_load(var2 + 12) * i32_load(var2 + 8)) else 0):
        i32_store(var4 + 24, i32_load(var2 + 24))
        i64_store(var4 + 16, i64_load(var2 + 16))
        i64_store(var4 + 8, i64_load(var2 + 8))
        i64_store(var4, i64_load(var2))
        i32_store(var2 + 24, i32_load(var3 + 24))
        i64_store(var2 + 16, i64_load(var3 + 16))
        i64_store(var2 + 8, i64_load(var3 + 8))
        i64_store(var2, i64_load(var3))
        i32_store(var3 + 24, i32_load(var4 + 24))
        i64_store(var3 + 16, i64_load(var4 + 16))
        i64_store(var3 + 8, i64_load(var4 + 8))
        i64_store(var3, i64_load(var4))
        if (1 if (i32_load(var2 + 12) * i32_load(var2 + 8)) <= (i32_load(var1 + 12) * i32_load(var1 + 8)) else 0):
            return (var5 + 1)
        i32_store(var4 + 24, i32_load(var1 + 24))
        i64_store(var4 + 16, i64_load(var1 + 16))
        i64_store(var4 + 8, i64_load(var1 + 8))
        i64_store(var4, i64_load(var1))
        i32_store(var1 + 24, i32_load(var2 + 24))
        i64_store(var1 + 16, i64_load(var2 + 16))
        i64_store(var1 + 8, i64_load(var2 + 8))
        i64_store(var1, i64_load(var2))
        i32_store(var2 + 24, i32_load(var4 + 24))
        i64_store(var2 + 16, i64_load(var4 + 16))
        i64_store(var2 + 8, i64_load(var4 + 8))
        i64_store(var2, i64_load(var4))
        if (1 if (i32_load(var1 + 12) * i32_load(var1 + 8)) <= (i32_load(var0 + 12) * i32_load(var0 + 8)) else 0):
            return (var5 + 2)
        i32_store(var4 + 24, i32_load(var0 + 24))
        i64_store(var4 + 16, i64_load(var0 + 16))
        i64_store(var4 + 8, i64_load(var0 + 8))
        i64_store(var4, i64_load(var0))
        i32_store(var0 + 24, i32_load(var1 + 24))
        i64_store(var0 + 16, i64_load(var1 + 16))
        i64_store(var0 + 8, i64_load(var1 + 8))
        i64_store(var0, i64_load(var1))
        i32_store(var1 + 24, i32_load(var4 + 24))
        i64_store(var1 + 16, i64_load(var4 + 16))
        i64_store(var1 + 8, i64_load(var4 + 8))
        i64_store(var1, i64_load(var4))
    else:
    return var5


# ==========================================================
# $func205
# ==========================================================
def func205(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var3 = i32_load8_u(var0 + 122)
    if (1 if i32_load8_u(var0 + 122) == i32_load(38500) else 0):
        break
    var2 = i32_load16_u(var0 + 110)
    var1 = (i32_load(9142892) * var1)
    var4 = i32_load(9143004)
    var5 = i32_load16_u(var0 + 120)
    if i32_load16_u(var0 + 120):
    else:
    if (1 if i32_load8_u(((var5 if i32_load8_u((var4 + (var1 + var2))) else var2) + (var2 + var1))) == 0 else 0):
        var2 = 0
        if (1 if i32_load8_u(var0 + 127) != 6 else 0):
            break
        if (1 if i32_load8_u(var0 + 128) == 0 else 0):
            break
        break
    var2 = 0
    if i32_load8_u(var0 + 128):
        break
    if (1 if i32_load8_u(var0 + 125) == 10 else 0):
        break
    if (1 if i32_load8_u(var0 + 126) == 2 else 0):
        break
    var0 = i32_load(var0 + 64)
    if (1 if i32_load(var0 + 64) == -1 else 0):
        break
    var1 = ((var3 * 404) + 9568096)
    var4 = i32_load(((var3 * 404) + 9568096) + 264)
    if (1 if i32_load(((var3 * 404) + 9568096) + 264) == 2 else 0):
        break
    var2 = ((((((1 if i32_load(var1 + 188) == 55 else 0) & (1 if i32_load(38560) != var3 else 0)) & (1 if i32_load(38620) != var3 else 0)) & (1 if i32_load(38564) != var3 else 0)) & (1 if var4 == 1 else 0)) & (1 if var0 > 1 else 0))
    return var2


# ==========================================================
# $func208
# ==========================================================
def func208(var0, var1, var2, var3):
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
    var21 = 0
    var22 = 0
    var8 = (i32_load(9142892) * var2)
    var19 = i32_load(9142440)
    var10 = (i32_load(9142440) + 2)
    var22 = ((i32_load(9142440) + 2) << 1)
    var12 = i32_load(38564)
    var13 = i32_load(38620)
    var14 = i32_load(38560)
    var9 = i32_load(9143004)
    var15 = i32_load(38500)
    var16 = i32_load(9671128)
    var17 = i32_load(9142840)
    var2 = 0
    while True:  # loop $label10
        var20 = var2
        var4 = (var2 << 2)
        var2 = (i32_load((((var2 << 2) | 4) + 8611904)) + var1)
        if (1 if var19 <= (i32_load((((var2 << 2) | 4) + 8611904)) + var1) else 0):
            break
        var4 = (i32_load((var4 + 8611904)) + var0)
        if (1 if var19 <= (i32_load((var4 + 8611904)) + var0) else 0):
            break
        if (1 if (var2 | var4) < 0 else 0):
            break
        var11 = (var4 + 1)
        var21 = (var2 + 1)
        var2 = i32_load((var17 + (((var4 + 1) + ((var2 + 1) * var10)) << 2)))
        if (1 if i32_load((var17 + (((var4 + 1) + ((var2 + 1) * var10)) << 2))) < 3 else 0):
            break
        var7 = 0
        var4 = (var16 + (var2 * 132))
        var6 = i32_load8_u((var16 + (var2 * 132)) + 122)
        if (1 if var15 == i32_load8_u((var16 + (var2 * 132)) + 122) else 0):
            break
        var5 = i32_load16_u(var4 + 110)
        var18 = i32_load16_u(var4 + 120)
        if i32_load16_u(var4 + 120):
        else:
        if (1 if i32_load8_u(((var18 if i32_load8_u((var9 + (var5 + var8))) else var5) + (var5 + var8))) == 0 else 0):
            if (1 if i32_load8_u(var4 + 127) != 6 else 0):
                break
            if (1 if i32_load8_u(var4 + 128) == 0 else 0):
                break
            break
        if i32_load8_u(var4 + 128):
            break
        if (1 if i32_load8_u(var4 + 125) == 10 else 0):
            break
        if (1 if i32_load8_u(var4 + 126) == 2 else 0):
            break
        if (1 if i32_load(var4 + 64) == -1 else 0):
            break
        var5 = ((var6 * 404) + 9568096)
        if (1 if i32_load(((var6 * 404) + 9568096) + 264) == 2 else 0):
            break
        var7 = ((((1 if i32_load(var5 + 188) == 55 else 0) & (1 if var6 != var14 else 0)) & (1 if var6 != var13 else 0)) & (1 if var6 != var12 else 0))
        if var7:
            break
        if (1 if i32_load(var4 + 84) >= var3 else 0):
            break
        if i32_load(((var6 * 404) + 9568096) + 304):
            break
        var2 = i32_load((var17 + ((var11 + ((var10 + var21) * var10)) << 2)))
        if (1 if i32_load((var17 + ((var11 + ((var10 + var21) * var10)) << 2))) < 3 else 0):
            break
        var7 = 0
        var4 = (var16 + (var2 * 132))
        var6 = i32_load8_u((var16 + (var2 * 132)) + 122)
        if (1 if var15 == i32_load8_u((var16 + (var2 * 132)) + 122) else 0):
            break
        var5 = i32_load16_u(var4 + 110)
        var18 = i32_load16_u(var4 + 120)
        if i32_load16_u(var4 + 120):
        else:
        if i32_load8_u(((var18 if i32_load8_u((var9 + (var5 + var8))) else var5) + (var5 + var8))):
            if (1 if i32_load8_u(var4 + 128) == 0 else 0):
                break
            break
        if (1 if i32_load8_u(var4 + 127) != 6 else 0):
            break
        if i32_load8_u(var4 + 128):
            break
        if (1 if i32_load8_u(var4 + 125) == 10 else 0):
            break
        if (1 if i32_load8_u(var4 + 126) == 2 else 0):
            break
        if (1 if i32_load(var4 + 64) == -1 else 0):
            break
        var5 = ((var6 * 404) + 9568096)
        if (1 if i32_load(((var6 * 404) + 9568096) + 264) == 2 else 0):
            break
        var7 = ((((1 if i32_load(var5 + 188) == 55 else 0) & (1 if var6 != var14 else 0)) & (1 if var6 != var13 else 0)) & (1 if var6 != var12 else 0))
        if var7:
            break
        if (1 if i32_load(var4 + 84) >= var3 else 0):
            break
        if i32_load(((var6 * 404) + 9568096) + 304):
            break
        var2 = i32_load((var17 + ((var11 + ((var21 + var22) * var10)) << 2)))
        if (1 if i32_load((var17 + ((var11 + ((var21 + var22) * var10)) << 2))) < 3 else 0):
            break
        var6 = 0
        var4 = (var16 + (var2 * 132))
        var5 = i32_load8_u((var16 + (var2 * 132)) + 122)
        if (1 if var15 == i32_load8_u((var16 + (var2 * 132)) + 122) else 0):
            break
        var7 = i32_load16_u(var4 + 110)
        var11 = i32_load16_u(var4 + 120)
        if i32_load16_u(var4 + 120):
        else:
        if i32_load8_u(((var11 if i32_load8_u((var9 + (var7 + var8))) else var7) + (var7 + var8))):
            if (1 if i32_load8_u(var4 + 128) == 0 else 0):
                break
            break
        if (1 if i32_load8_u(var4 + 127) != 6 else 0):
            break
        if i32_load8_u(var4 + 128):
            break
        if (1 if i32_load8_u(var4 + 125) == 10 else 0):
            break
        if (1 if i32_load8_u(var4 + 126) == 2 else 0):
            break
        if (1 if i32_load(var4 + 64) == -1 else 0):
            break
        var7 = ((var5 * 404) + 9568096)
        if (1 if i32_load(((var5 * 404) + 9568096) + 264) == 2 else 0):
            break
        var6 = ((((1 if i32_load(var7 + 188) == 55 else 0) & (1 if var5 != var14 else 0)) & (1 if var5 != var13 else 0)) & (1 if var5 != var12 else 0))
        if var6:
            break
        if (1 if i32_load(var4 + 84) >= var3 else 0):
            break
        if i32_load(((var5 * 404) + 9568096) + 304):
            break
        var2 = (var20 + 2)
        if (1 if var20 < 1678 else 0):
            continue
        break  # end loop
    var2 = 0
    return var2


# ==========================================================
# $func209
# ==========================================================
def func209(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = var0
    if (var0 & 3):
        while True:  # loop $label1
            if (1 if i32_load8_u(var1) == 0 else 0):
                break
            var1 = (var1 + 1)
            if ((var1 + 1) & 3):
                continue
            break  # end loop
    while True:  # loop $label2
        var2 = var1
        var1 = (var1 + 4)
        var3 = i32_load(var2)
        if (1 if (((i32_load(var2) ^ -1) & (var3 - 16843009)) & -2139062144) == 0 else 0):
            continue
        break  # end loop
    while True:  # loop $label3
        var1 = var2
        var2 = (var2 + 1)
        if i32_load8_u(var1):
            continue
        break  # end loop
    return (var1 - var0)


# ==========================================================
# $func218
# ==========================================================
def func218():
    i32_store(9561212, 13)
    i64_store(9561204, 25769803779)
    i64_store(9561196, 35184372088835)
    i64_store(9561188, 64424509441)
    i64_store(9561180, 8589934595)
    i64_store(9561172, 12884901903)
    i64_store(9561164, 2)
    i64_store(9561156, 8589934594)
    i64_store(9561132, 51539607568)
    i64_store(9561124, 51539607565)
    i64_store(9561116, 21474836489)
    i64_store(9561108, 4294967296)
    i64_store(9561100, 4)
    i64_store(9561092, 100)
    i64_store(9561080, 42949672970)
    i64_store(9561072, 42949672970)
    i32_store(9561152, 21)
    i64_store(9561452, 19327352832002)
    i32_store(9561148, 17)
    i64_store(9561444, 85899345960)
    i64_store(9561336, 429496729616)
    i64_store(9561324, 257698037810000)
    i64_store(9561316, 107374183000)
    i64_store(9561308, 644245334400)
    i64_store(9561284, 85899345950000)
    i64_store(9561276, 1073741824020)
    i64_store(9561268, 171798691847)
    i64_store(9561260, 214748364850)
    i64_store(9561252, 257698037764)
    i64_store(9561244, 25769804776)
    i64_store(9561236, 128849018880050)
    i64_store(9561228, 21474836484)
    i32_store(9561292, 50000)
    i32_store(9561216, 1)
    i64_store(9561140, 81604378628)
    i64_store(9561468, 42949672960004)
    i32_store(9561440, 100)
    i64_store(9561432, 34359738468)
    i64_store(9561424, 214748364814)
    i64_store(9561416, 214748364804)
    i64_store(9561408, 429496730200)
    i64_store(9561400, 34359738388)
    i64_store(9561392, 773094113290)
    i64_store(9561384, 257698038360)
    i64_store(9561376, 214748364850)
    i64_store(9561368, 214748364870)
    i64_store(9561360, 85899345920005)
    i64_store(9561352, 128849018950)
    i64_store(9561344, 2147483648300)
    i32_store(9561476, 12)
    i64_store(9561460, 137438953488)

