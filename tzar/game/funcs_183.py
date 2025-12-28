"""
Auto-generated from WAT. Contains 1 functions.
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
# $func772
# ==========================================================
def func772(var0, var1, var2):
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
    var21 = 0
    var22 = 0
    var23 = 0
    var24 = 0
    var25 = 0
    var26 = 0
    var27 = 0
    var28 = 0
    var29 = 0
    var30 = 0
    var31 = 0
    var32 = 0
    var33 = 0
    var34 = 0
    var35 = 0
    var36 = 0
    var37 = 0
    var38 = 0
    var39 = 0
    var40 = 0
    var41 = 0
    var42 = 0
    var43 = 0
    var44 = 0.0
    var45 = 0.0
    var46 = 0.0
    var47 = 0.0
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var10 = i32_load(59164)
    var1 = i32_load(9561692)
    var0 = 1
    while True:  # loop $label1
        if (1 if var10 != i32_load((var1 + (var0 * 286704)) + 284616) else 0):
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var2 else 0):
                continue
            break
        break  # end loop
    if (1 if i32_load8_u(9216060) == 0 else 0):
        break
    if i32_load((((var1 + (var0 * 286704)) + (i32_load(9671152) << 2)) + 281808)):
        break
    var17 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var1 = i32_load(9561692)
    var16 = var0
    var13 = (i32_load(9561692) + (var0 * 286704))
    # Unknown: memory.fill []
    func239(i32_load(var13 + 283908))
    i32_store(var13 + 283976, 0)
    i32_store(var13 + 283956, 0)
    var0 = i32_load(var13 + 281788)
    if i32_load(var13 + 281788):
        i32_store(var0 + 8, 0)
    var0 = i32_load(var13 + 281792)
    if i32_load(var13 + 281792):
        i32_store(var0 + 8, 0)
    var2 = (var1 + (var16 * 286704))
    var0 = i32_load((var1 + (var16 * 286704)) + 281796)
    if i32_load((var1 + (var16 * 286704)) + 281796):
        i32_store(var0 + 8, 0)
    var23 = i32_load(9561692)
    while True:  # loop $label3
        var0 = (var2 + (var4 * 36))
        i32_store(((var2 + (var4 * 36)) + 269408), 0)
        i64_store((var0 + 269400), 0)
        i64_store((var0 + 269392), 0)
        i64_store((var0 + 269384), 0)
        i64_store((var0 + 269376), 0)
        var0 = (var2 + (var4 << 2))
        i32_store(((var2 + (var4 << 2)) + 282828), 0)
        i32_store((var0 + 281808), 0)
        var3 = 0
        while True:  # loop $label2
            var6 = (var2 + 283984)
            var7 = (var3 << 2)
            var10 = (var23 + 283984)
            i32_store(((var2 + 283984) + (var3 << 2)), i32_load(((var23 + 283984) + var7)))
            var0 = (var7 + 4)
            i32_store((var6 + (var7 + 4)), i32_load((var0 + var10)))
            var0 = (var7 + 8)
            i32_store((var6 + (var7 + 8)), i32_load((var0 + var10)))
            var0 = (var7 + 12)
            i32_store((var6 + (var7 + 12)), i32_load((var0 + var10)))
            var0 = (var7 + 16)
            i32_store((var6 + (var7 + 16)), i32_load((var0 + var10)))
            var3 = (var3 + 5)
            if (1 if (var3 + 5) != 155 else 0):
                continue
            break  # end loop
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != 255 else 0):
            continue
        break  # end loop
    i32_store((var1 + (var16 * 286704)) + 283848, i32_load(i32_load(9142424) + 4))
    i32_store8(9682192, 1)
    var3 = i32_load(9142440)
    var45 = float(((((i32_load(51780) * var3) & 0xFFFFFFFF) // 100) + 20))
    var44 = (float(((((i32_load(9142440) * i32_load(51784)) & 0xFFFFFFFF) // 100) - 20)) - float(((((i32_load(51780) * var3) & 0xFFFFFFFF) // 100) + 20)))
    if ((1 if (float(((((i32_load(9142440) * i32_load(51784)) & 0xFFFFFFFF) // 100) - 20)) - float(((((i32_load(51780) * var3) & 0xFFFFFFFF) // 100) + 20))) < 4294967300.0 else 0) & (1 if var44 >= 0.0 else 0)):
        break
    var5 = 0
    var18 = ((var3 & 0xFFFFFFFF) >> 1)
    var27 = i32_load(9684492)
    var19 = i32_load(9142432)
    var2 = i32_load(9147316)
    var1 = i32_load(9147320)
    var7 = i32_load(9147312)
    var0 = i32_load(9147324)
    if (1 if i32_load(9147132) == 0 else 0):
        break
    if (1 if var3 != 4096 else 0):
        break
    var20 = (var3 + 2)
    var36 = (var3 - 30)
    var37 = i32_load(38448)
    var38 = i32_load(9671128)
    var28 = i32_load(9142840)
    while True:  # loop $label21
        var6 = var1
        var1 = var7
        i32_store(9147320, var7)
        var10 = var2
        i32_store(9147324, var2)
        var0 = ((var0 << 11) ^ var0)
        var2 = (((((var7 & 0xFFFFFFFF) >> 19) ^ ((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8)) ^ var7) ^ var0)
        i32_store(9147316, (((((var7 & 0xFFFFFFFF) >> 19) ^ ((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8)) ^ var7) ^ var0))
        var0 = (var6 ^ (var6 << 11))
        var7 = ((((((var6 ^ (var6 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var2)
        i32_store(9147312, ((((((var6 ^ (var6 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var2))
        var29 = (var2 % 4066)
        var8 = ((var2 % 4066) + 15)
        var0 = (((var2 % 4066) + 15) - var18)
        var30 = (var7 % var36)
        var9 = ((var7 % var36) + 15)
        var0 = (((var7 % var36) + 15) - var18)
        if (1 if ((((((var2 % 4066) + 15) - var18) * var0) + ((((var7 % var36) + 15) - var18) * var0)) - 1) < 65537 else 0):
            break
        var24 = 1
        var5 = (30 if (1 if var15 > 500 else 0) else 60)
        var3 = (var8 - (30 if (1 if var15 > 500 else 0) else 60))
        var0 = (var5 << 1)
        var31 = ((var5 << 1) + var8)
        if (1 if (var8 - (30 if (1 if var15 > 500 else 0) else 60)) >= ((var5 << 1) + var8) else 0):
            break
        var6 = (var9 - var5)
        var39 = (var0 + var9)
        if (1 if (var9 - var5) >= (var0 + var9) else 0):
            break
        var24 = 0
        var32 = (i32_load(9142892) * var16)
        var33 = i32_load(9142440)
        var34 = (i32_load(9142440) + 2)
        var40 = i32_load(38564)
        var41 = i32_load(38620)
        var42 = i32_load(38560)
        var35 = i32_load(9143004)
        var43 = i32_load(38500)
        var12 = i32_load(9671128)
        var14 = i32_load(9142840)
        var21 = (var5 * var5)
        while True:  # loop $label11
            var5 = (var3 + 1)
            if (1 if var3 < var33 else 0):
                var0 = (var3 - var8)
                var25 = (((var3 - var8) * var0) - 1)
                var0 = var6
                while True:  # loop $label10
                    var4 = (var0 - var9)
                    if (1 if (var25 + ((var0 - var9) * var4)) > var21 else 0):
                        break
                    if (1 if var0 >= var33 else 0):
                        break
                    if (1 if (var0 | var3) < 0 else 0):
                        break
                    var4 = i32_load((var14 + ((var5 + (((var0 + var34) + 1) * var34)) << 2)))
                    if (1 if i32_load((var14 + ((var5 + (((var0 + var34) + 1) * var34)) << 2))) < 3 else 0):
                        break
                    var11 = (var12 + (var4 * 132))
                    var22 = i32_load8_u((var12 + (var4 * 132)) + 122)
                    if (1 if var43 == i32_load8_u((var12 + (var4 * 132)) + 122) else 0):
                        break
                    var26 = i32_load16_u(var11 + 110)
                    var4 = i32_load16_u(var11 + 120)
                    if i32_load16_u(var11 + 120):
                    else:
                    if i32_load8_u(((var4 if i32_load8_u((var35 + (var26 + var32))) else var26) + (var26 + var32))):
                        if (1 if i32_load8_u(var11 + 128) == 0 else 0):
                            break
                        break
                    if (1 if i32_load8_u(var11 + 127) != 6 else 0):
                        break
                    if i32_load8_u(var11 + 128):
                        break
                    if (1 if i32_load8_u(var11 + 125) == 10 else 0):
                        break
                    if (1 if i32_load8_u(var11 + 126) == 2 else 0):
                        break
                    if (1 if i32_load(var11 + 64) == -1 else 0):
                        break
                    var4 = ((var22 * 404) + 9568096)
                    if (1 if i32_load(((var22 * 404) + 9568096) + 264) == 2 else 0):
                        break
                    if (1 if i32_load(var4 + 188) != 55 else 0):
                        break
                    if (1 if var22 == var42 else 0):
                        break
                    if (1 if var22 == var41 else 0):
                        break
                    if (1 if var22 != var40 else 0):
                        break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var39 else 0):
                        continue
                    break  # end loop
            var24 = (1 if var5 >= var31 else 0)
            var3 = var5
            if (1 if var5 != var31 else 0):
                continue
            break  # end loop
        if (1 if var24 == 0 else 0):
            break
        var14 = (var29 + 33)
        var12 = 0
        var4 = (var29 + 6)
        var0 = (var29 + 6)
        var6 = (var30 + 6)
        var21 = (var30 + 33)
        if (1 if (var30 + 6) < (var30 + 33) else 0):
            while True:  # loop $label15
                var5 = (var0 + 1)
                if (1 if var0 <= 4095 else 0):
                    var0 = (var0 - var8)
                    var25 = (((var0 - var8) * var0) - 1)
                    var0 = var6
                    while True:  # loop $label14
                        var3 = (var0 - var9)
                        if (1 if (var25 + ((var0 - var9) * var3)) > 81 else 0):
                            break
                        if (1 if var0 > 4095 else 0):
                            break
                        if (1 if i32_load((var28 + (((((var0 + var20) + 1) * var20) + var5) << 2))) == 1 else 0):
                            break
                        var0 = (var0 + 1)
                        if (1 if (var0 + 1) != var21 else 0):
                            continue
                        break  # end loop
                var12 = (1 if var5 >= var14 else 0)
                var0 = var5
                if (1 if var5 != var14 else 0):
                    continue
                break  # end loop
            if (1 if var12 == 0 else 0):
                break
        var12 = 0
        while True:  # loop $label19
            var5 = (var4 + 1)
            if (1 if var4 <= 4095 else 0):
                var0 = (var4 - var8)
                var4 = (((var4 - var8) * var0) - 1)
                var0 = var6
                while True:  # loop $label18
                    var3 = (var0 - var9)
                    if (1 if (var4 + ((var0 - var9) * var3)) > 81 else 0):
                        break
                    if (1 if var0 > 4095 else 0):
                        break
                    var3 = i32_load((var28 + (((((var0 + var20) + 1) * var20) + var5) << 2)))
                    if (1 if i32_load((var28 + (((((var0 + var20) + 1) * var20) + var5) << 2))) < 3 else 0):
                        break
                    if (1 if var37 == i32_load8_u((var38 + (var3 * 132)) + 122) else 0):
                        break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var21 else 0):
                        continue
                    break  # end loop
            var12 = (1 if var5 >= var14 else 0)
            var4 = var5
            if (1 if var5 != var14 else 0):
                continue
            break  # end loop
        if (1 if var12 == 0 else 0):
            break
        if var19:
        else:
        if (1 if 0 == var27 else 0):
            break
        var0 = var10
        var15 = (var15 + 1)
        if (1 if (var15 + 1) != 2000 else 0):
            continue
        break  # end loop
    break
    while True:  # loop $label25
        var10 = var7
        i32_store(9147320, var7)
        i32_store(9147324, var2)
        var0 = ((var0 << 11) ^ var0)
        var6 = (((((var7 & 0xFFFFFFFF) >> 19) ^ ((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8)) ^ var7) ^ var0)
        i32_store(9147316, (((((var7 & 0xFFFFFFFF) >> 19) ^ ((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8)) ^ var7) ^ var0))
        var0 = ((var1 << 11) ^ var1)
        var7 = (((((((var1 << 11) ^ var1) & 0xFFFFFFFF) >> 8) ^ ((var6 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var6)
        i32_store(9147312, (((((((var1 << 11) ^ var1) & 0xFFFFFFFF) >> 8) ^ ((var6 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var6))
        var46 = ((float((var6 % 10000)) * 6.28318548) / 10000.0)
        var44 = (var45 + float((var7 % var5)))
        var47 = (float((func48(((float((var6 % 10000)) * 6.28318548) / 10000.0)) * (var45 + float((var7 % var5))))) + 0.5)
        if (1 if abs((float((func48(((float((var6 % 10000)) * 6.28318548) / 10000.0)) * (var45 + float((var7 % var5))))) + 0.5)) < 2147483648.0 else 0):
            break
        var9 = (-2147483648 + var18)
        var47 = (float((func49(var46) * var44)) + 0.5)
        if (1 if abs((float((func49(var46) * var44)) + 0.5)) < 2147483648.0 else 0):
            break
        var8 = (-2147483648 + var18)
        if var19:
        else:
        if (1 if 0 == var27 else 0):
            break
        var0 = var2
        var1 = var10
        var2 = var6
        var15 = (var15 + 1)
        if (1 if (var15 + 1) != 2000 else 0):
            continue
        break  # end loop
    break
    if (1 if i32_load(9142872) != var16 else 0):
        break
    if i32_load8_u(9142917):
        break
    i32_store(var17 + 4, (var9 << 5))
    i32_store(var17, (var8 << 5))
    var23 = i32_load(9561692)
    var0 = (var23 + (var16 * 286704))
    i32_store((var23 + (var16 * 286704)) + 283900, var9)
    i32_store(var0 + 283896, var8)
    i32_store(var0 + 283876, var9)
    i32_store(var0 + 283872, var8)
    i32_store8(9682192, 0)
    global global0
    global0 = (var17 + 16)
    return func317(var13)

