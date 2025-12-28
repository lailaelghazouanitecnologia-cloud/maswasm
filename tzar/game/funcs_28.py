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
# $func416
# ==========================================================
def func416(var0, var1, var2, var3):
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
    var7 = (i32_load(9142892) * var2)
    var20 = i32_load(9142440)
    var11 = (i32_load(9142440) + 2)
    var22 = ((i32_load(9142440) + 2) << 1)
    var13 = i32_load(38564)
    var14 = i32_load(38620)
    var15 = i32_load(38560)
    var8 = i32_load(9143004)
    var16 = i32_load(38500)
    var17 = i32_load(9671128)
    var18 = i32_load(9142840)
    var2 = 0
    while True:  # loop $label7
        var21 = var2
        var5 = (var2 << 2)
        var2 = (i32_load((((var2 << 2) | 4) + 8611904)) + var1)
        if (1 if var20 <= (i32_load((((var2 << 2) | 4) + 8611904)) + var1) else 0):
            break
        var5 = (i32_load((var5 + 8611904)) + var0)
        if (1 if var20 <= (i32_load((var5 + 8611904)) + var0) else 0):
            break
        if (1 if (var2 | var5) < 0 else 0):
            break
        var9 = (var5 + 1)
        var12 = (var2 + 1)
        var2 = i32_load((var18 + (((var5 + 1) + ((var2 + 1) * var11)) << 2)))
        if (1 if i32_load((var18 + (((var5 + 1) + ((var2 + 1) * var11)) << 2))) < 3 else 0):
            break
        var4 = (var17 + (var2 * 132))
        var6 = i32_load8_u((var17 + (var2 * 132)) + 122)
        var10 = ((i32_load8_u((var17 + (var2 * 132)) + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u((var17 + (var2 * 132)) + 122) * 404) + 9568096) + 316) == 0 else 0):
            break
        if (1 if var6 == var16 else 0):
            break
        var5 = i32_load16_u(var4 + 110)
        var19 = i32_load16_u(var4 + 120)
        if i32_load16_u(var4 + 120):
        else:
        if (1 if i32_load8_u(((var19 if i32_load8_u((var8 + (var5 + var7))) else var5) + (var5 + var7))) == 0 else 0):
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
        if (1 if i32_load(var10 + 264) == 2 else 0):
            break
        if (1 if i32_load(var10 + 188) != 55 else 0):
            break
        if (1 if var6 == var15 else 0):
            break
        if (1 if var6 == var14 else 0):
            break
        if (1 if var6 == var13 else 0):
            break
        if ((1 if var3 == -1 else 0) | (1 if var3 == var6 else 0)):
            break
        var2 = i32_load((var18 + ((var9 + ((var11 + var12) * var11)) << 2)))
        if (1 if i32_load((var18 + ((var9 + ((var11 + var12) * var11)) << 2))) < 3 else 0):
            break
        var4 = (var17 + (var2 * 132))
        var6 = i32_load8_u((var17 + (var2 * 132)) + 122)
        var10 = ((i32_load8_u((var17 + (var2 * 132)) + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u((var17 + (var2 * 132)) + 122) * 404) + 9568096) + 316) == 0 else 0):
            break
        if (1 if var6 == var16 else 0):
            break
        var5 = i32_load16_u(var4 + 110)
        var19 = i32_load16_u(var4 + 120)
        if i32_load16_u(var4 + 120):
        else:
        if i32_load8_u(((var19 if i32_load8_u((var8 + (var5 + var7))) else var5) + (var5 + var7))):
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
        if (1 if i32_load(var10 + 264) == 2 else 0):
            break
        if (1 if i32_load(var10 + 188) != 55 else 0):
            break
        if (1 if var6 == var15 else 0):
            break
        if (1 if var6 == var14 else 0):
            break
        if (1 if var6 == var13 else 0):
            break
        if ((1 if var3 == -1 else 0) | (1 if var3 == var6 else 0)):
            break
        var2 = i32_load((var18 + ((var9 + ((var12 + var22) * var11)) << 2)))
        if (1 if i32_load((var18 + ((var9 + ((var12 + var22) * var11)) << 2))) < 3 else 0):
            break
        var5 = (var17 + (var2 * 132))
        var4 = i32_load8_u((var17 + (var2 * 132)) + 122)
        var9 = ((i32_load8_u((var17 + (var2 * 132)) + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u((var17 + (var2 * 132)) + 122) * 404) + 9568096) + 316) == 0 else 0):
            break
        if (1 if var4 == var16 else 0):
            break
        var6 = i32_load16_u(var5 + 110)
        var12 = i32_load16_u(var5 + 120)
        if i32_load16_u(var5 + 120):
        else:
        if i32_load8_u(((var12 if i32_load8_u((var8 + (var6 + var7))) else var6) + (var6 + var7))):
            if (1 if i32_load8_u(var5 + 128) == 0 else 0):
                break
            break
        if (1 if i32_load8_u(var5 + 127) != 6 else 0):
            break
        if i32_load8_u(var5 + 128):
            break
        if (1 if i32_load8_u(var5 + 125) == 10 else 0):
            break
        if (1 if i32_load8_u(var5 + 126) == 2 else 0):
            break
        if (1 if i32_load(var5 + 64) == -1 else 0):
            break
        if (1 if i32_load(var9 + 264) == 2 else 0):
            break
        if (1 if i32_load(var9 + 188) != 55 else 0):
            break
        if (1 if var4 == var15 else 0):
            break
        if (1 if var4 == var14 else 0):
            break
        if (1 if var4 == var13 else 0):
            break
        if ((1 if var3 == -1 else 0) | (1 if var3 == var4 else 0)):
            break
        var2 = (var21 + 2)
        if (1 if var21 < 1678 else 0):
            continue
        break  # end loop
    var2 = 0
    return var2


# ==========================================================
# $func422
# ==========================================================
def func422(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0.0
    var5 = 0.0
    var6 = 0.0
    var2 = i32_reinterpret_f32(var0)
    var1 = (i32_reinterpret_f32(var0) & 2147483647)
    if (1 if (i32_reinterpret_f32(var0) & 2147483647) >= 1283457024 else 0):
        # Unknown: f32.copysign []
        return (1.57079625 if (1 if (i32_reinterpret_f32(var0) & 2147483647) > 2139095040 else 0) else var0)
    if (1 if var1 <= 1054867455 else 0):
        if (1 if var1 >= 964689920 else 0):
            break
        break
    var0 = abs(var0)
    if (1 if var1 <= 1066926079 else 0):
        if (1 if var1 <= 1060110335 else 0):
            var0 = (((var0 + var0) + -1.0) / (var0 + 2.0))
            break
        var0 = ((var0 + -1.0) / (var0 + 1.0))
        break
    if (1 if var1 <= 1075576831 else 0):
        var0 = ((var0 + -1.5) / ((var0 * 1.5) + 1.0))
        break
    var0 = (-1.0 / var0)
    var3 = 3
    var5 = (var0 * var0)
    var4 = ((var0 * var0) * var5)
    var6 = (((var0 * var0) * var5) * ((var4 * -0.106480174) + -0.199991584))
    var4 = (var5 * ((var4 * ((var4 * 0.0616876073) + 0.142536357)) + 0.333333284))
    if (1 if var1 <= 1054867455 else 0):
        return (var0 - (var0 * (var6 + var4)))
    var1 = (var3 << 2)
    var0 = (f32_load(((var3 << 2) + 28896)) - (((var0 * (var6 + var4)) - f32_load((var1 + 28912))) - var0))
    var0 = ((-(f32_load(((var3 << 2) + 28896)) - (((var0 * (var6 + var4)) - f32_load((var1 + 28912))) - var0))) if (1 if var2 < 0 else 0) else var0)
    return var0


# ==========================================================
# $func424
# ==========================================================
def func424(var0):
    var1 = 0.0
    var2 = 0.0
    var3 = 0.0
    var4 = 0
    var5 = 0
    var6 = 0
    var6 = i64_reinterpret_f64(var0)
    var4 = (i32(((i64_reinterpret_f64(var0) & 0xFFFFFFFFFFFFFFFF) >> 32)) & 2147483647)
    if (1 if (i32(((i64_reinterpret_f64(var0) & 0xFFFFFFFFFFFFFFFF) >> 32)) & 2147483647) >= 1141899264 else 0):
        # Unknown: f64.copysign []
        return (1.5707963267948966 if (1 if (i64_reinterpret_f64(var0) & 9223372036854775807) > 9218868437227405312 else 0) else var0)
    if (1 if var4 <= 1071382527 else 0):
        if (1 if var4 >= 1044381696 else 0):
            break
        break
    var0 = abs(var0)
    if (1 if var4 <= 1072889855 else 0):
        if (1 if var4 <= 1072037887 else 0):
            var0 = (((var0 + var0) + -1.0) / (var0 + 2.0))
            break
        var0 = ((var0 + -1.0) / (var0 + 1.0))
        break
    if (1 if var4 <= 1073971199 else 0):
        var0 = ((var0 + -1.5) / ((var0 * 1.5) + 1.0))
        break
    var0 = (-1.0 / var0)
    var5 = 3
    var2 = (var0 * var0)
    var1 = ((var0 * var0) * var2)
    var3 = (((var0 * var0) * var2) * ((var1 * ((var1 * ((var1 * ((var1 * -0.036531572744216916) + -0.058335701337905735)) + -0.0769187620504483)) + -0.11111110405462356)) + -0.19999999999876483))
    var1 = (var2 * ((var1 * ((var1 * ((var1 * ((var1 * ((var1 * 0.016285820115365782) + 0.049768779946159324)) + 0.06661073137387531)) + 0.09090887133436507)) + 0.14285714272503466)) + 0.3333333333333293))
    if (1 if var4 <= 1071382527 else 0):
        return (var0 - (var0 * (var3 + var1)))
    var4 = (var5 << 3)
    var0 = (f64_load(((var5 << 3) + 28736)) - (((var0 * (var3 + var1)) - f64_load((var4 + 28768))) - var0))
    var0 = ((-(f64_load(((var5 << 3) + 28736)) - (((var0 * (var3 + var1)) - f64_load((var4 + 28768))) - var0))) if (1 if var6 < 0 else 0) else var0)
    return var0


# ==========================================================
# $func425
# ==========================================================
def func425(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var1 = i32_load(9681952)
    var2 = (var0 + (i32_load(9681952) << 2))
    if (1 if i32_load(((var0 + (i32_load(9681952) << 2)) + 282828)) != (0 - i32_load((var2 + 281808))) else 0):
        break
    var1 = i32_load(9681956)
    var2 = (var0 + (i32_load(9681956) << 2))
    if (1 if i32_load(((var0 + (i32_load(9681956) << 2)) + 282828)) != (0 - i32_load((var2 + 281808))) else 0):
        break
    var1 = i32_load(9681960)
    var2 = (var0 + (i32_load(9681960) << 2))
    if (1 if i32_load(((var0 + (i32_load(9681960) << 2)) + 282828)) != (0 - i32_load((var2 + 281808))) else 0):
        break
    var1 = i32_load(9681964)
    var2 = (var0 + (i32_load(9681964) << 2))
    if (1 if i32_load(((var0 + (i32_load(9681964) << 2)) + 282828)) != (0 - i32_load((var2 + 281808))) else 0):
        break
    var1 = i32_load(9681968)
    var2 = (var0 + (i32_load(9681968) << 2))
    if (1 if i32_load(((var0 + (i32_load(9681968) << 2)) + 282828)) != (0 - i32_load((var2 + 281808))) else 0):
        break
    var1 = i32_load(9681972)
    var2 = (var0 + (i32_load(9681972) << 2))
    if (1 if i32_load(((var0 + (i32_load(9681972) << 2)) + 282828)) != (0 - i32_load((var2 + 281808))) else 0):
        break
    var2 = i32_load(var0 + 283960)
    break
    var2 = i32_load(((var1 * 404) + 9568096) + 196)
    i32_store(var0 + 283960, i32_load(((var1 * 404) + 9568096) + 196))
    if (1 if var2 > 2 else 0):
        break
    var5 = i32_load(9671136)
    if (1 if i32_load(9671136) == 0 else 0):
        break
    var6 = ((var2 << 2) + 9681964)
    var7 = i32_load(var0 + 283908)
    var1 = 0
    var3 = i32_load(9671128)
    while True:  # loop $label5
        var4 = (var3 + (var1 * 132))
        if (1 if var7 != i32_load16_u((var3 + (var1 * 132)) + 110) else 0):
            break
        if (1 if i32_load(var6) != i32_load8_u(var4 + 122) else 0):
            break
        if (1 if i32_load8_u(var4 + 125) == 3 else 0):
            break
        var1 = (var3 + (var1 * 132))
        i32_store(var0 + 283872, i32_load16_u((var3 + (var1 * 132)) + 112))
        break
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var5 else 0):
            continue
        break  # end loop
    if (1 if var5 == 0 else 0):
        break
    var4 = ((var2 << 2) + 9681952)
    var6 = i32_load(var0 + 283908)
    var1 = 0
    var2 = i32_load(9671128)
    while True:  # loop $label7
        var3 = (var2 + (var1 * 132))
        if (1 if var6 != i32_load16_u((var2 + (var1 * 132)) + 110) else 0):
            break
        if (1 if i32_load(var4) != i32_load8_u(var3 + 122) else 0):
            break
        if (1 if i32_load8_u(var3 + 125) == 3 else 0):
            break
        var1 = (var2 + (var1 * 132))
        i32_store(var0 + 283872, i32_load16_u((var2 + (var1 * 132)) + 112))
        break
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var5 else 0):
            continue
        break  # end loop
    break
    var1 = (var1 + 114)
    i32_store(var0 + 283876, i32_load16_u(var1))


# ==========================================================
# $func433
# ==========================================================
def func433(var0):
    var1 = 0
    var1 = i32_load(var0 + 72)
    i32_store(var0 + 72, ((i32_load(var0 + 72) - 1) | var1))
    var1 = i32_load(var0)
    if (i32_load(var0) & 8):
        i32_store(var0, (var1 | 32))
        return -1
    i64_store(var0 + 4, 0)
    var1 = i32_load(var0 + 44)
    i32_store(var0 + 28, i32_load(var0 + 44))
    i32_store(var0 + 20, var1)
    i32_store(var0 + 16, (var1 + i32_load(var0 + 48)))
    return 0


# ==========================================================
# $func441
# ==========================================================
def func441(var0, var1, var2, var3):
    i32_store8(var0 + 53, 1)
    if (1 if i32_load(var0 + 4) != var2 else 0):
        break
    i32_store8(var0 + 52, 1)
    var2 = i32_load(var0 + 16)
    if (1 if i32_load(var0 + 16) == 0 else 0):
        i32_store(var0 + 36, 1)
        i32_store(var0 + 24, var3)
        i32_store(var0 + 16, var1)
        if (1 if var3 != 1 else 0):
            break
        if (1 if i32_load(var0 + 48) == 1 else 0):
            break
        break
    if (1 if var1 == var2 else 0):
        var2 = i32_load(var0 + 24)
        if (1 if i32_load(var0 + 24) == 2 else 0):
            i32_store(var0 + 24, var3)
            var2 = var3
        if (1 if i32_load(var0 + 48) != 1 else 0):
            break
        if (1 if var2 == 1 else 0):
            break
        break
    i32_store(var0 + 36, (i32_load(var0 + 36) + 1))
    i32_store8(var0 + 54, 1)


# ==========================================================
# $func442
# ==========================================================
def func442(var0, var1, var2):
    var3 = 0
    var3 = i32_load(var0 + 16)
    if (1 if i32_load(var0 + 16) == 0 else 0):
        i32_store(var0 + 36, 1)
        i32_store(var0 + 24, var2)
        i32_store(var0 + 16, var1)
        return
    if (1 if var1 == var3 else 0):
        if (1 if i32_load(var0 + 24) != 2 else 0):
            break
        i32_store(var0 + 24, var2)
        return
    i32_store8(var0 + 54, 1)
    i32_store(var0 + 24, 2)
    i32_store(var0 + 36, (i32_load(var0 + 36) + 1))


# ==========================================================
# $func445
# ==========================================================
def func445(var0, var1, var2, var3, var4, var5, var6):
    var7 = 0
    var8 = 0
    if (1 if var5 <= 0 else 0):
        break
    var7 = (var5 & 1)
    if (1 if var5 != 1 else 0):
        var8 = (var5 & -2)
        var5 = 0
        while True:  # loop $label1
            # call_indirect via table[i32_load(9687288)]
            var0 = (var0 + var1)
            var2 = (var2 + var3)
            # call_indirect via table[i32_load(9687288)]
            var2 = (var2 + var3)
            var0 = (var0 + var1)
            var5 = (var5 + 2)
            if (1 if (var5 + 2) != var8 else 0):
                continue
            break  # end loop
    if (1 if var7 == 0 else 0):
        break
    # call_indirect via table[i32_load(9687288)]

