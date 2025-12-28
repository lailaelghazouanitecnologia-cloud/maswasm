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
# $func317
# ==========================================================
def func317(var0):
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
    var33 = 0.0
    var34 = 0.0
    var35 = 0.0
    var36 = 0.0
    var37 = 0.0
    var38 = 0.0
    var39 = 0.0
    var40 = 0.0
    var41 = 0.0
    var42 = 0.0
    var43 = 0.0
    var44 = 0.0
    var1 = i32_load(var0 + 283960)
    var25 = (i32_load(var0 + 283960) if (1 if var1 <= 2 else 0) else 0)
    var2 = i32_load(9142428)
    if (1 if i32_load(9142428) >= 48 else 0):
        var4 = 47
        var26 = 1
        var1 = -1
        while True:  # loop $label42
            var6 = (i32_load(9142424) + (var4 << 2))
            var29 = i32_load((i32_load(9142424) + (var4 << 2)) + 16)
            var30 = ((var4 + 7) if i32_load((i32_load(9142424) + (var4 << 2)) + 16) else var4)
            if (1 if i32_load(var6 + 4) != 1 else 0):
                break
            var17 = i32_load(var6 + 8)
            if (1 if i32_load(var6 + 8) < 0 else 0):
                var17 = i32_load((((var25 + (var17 ^ -1)) << 2) + 9681488))
            var12 = i32_load(var6)
            var13 = i32_load(var6 + 12)
            var40 = 0.0
            if (1 if var3 == 0 else 0):
                break
            if (1 if var3 != var12 else 0):
                break
            if (1 if var1 != var13 else 0):
                break
            var40 = (3.14159274 / float(var3))
            if (1 if var12 == 0 else 0):
                var3 = 0
                var1 = var13
                break
            var41 = (6.28318548 / float(var12))
            var9 = ((var17 * 404) + 9568096)
            var35 = float(var13)
            var23 = 0
            while True:  # loop $label41
                var33 = ((var41 * float(var23)) + var40)
                var24 = i32_load(var0 + 283908)
                var1 = i32_load(var0 + 283876)
                var2 = i32_load(var0 + 283872)
                var20 = 0
                var27 = i32_load(var9 + 264)
                if (1 if i32_load(var9 + 264) == 0 else 0):
                    var44 = (((float(var33) * -8.0) / 6.2831854820251465) + 10.5)
                    if ((1 if (((float(var33) * -8.0) / 6.2831854820251465) + 10.5) < 4294967296.0 else 0) & (1 if var44 >= 0.0 else 0)):
                        break
                    var20 = (0 & 7)
                var28 = i32_load(var9 + 220)
                var42 = (float(i32_load(var9 + 220)) * -0.5)
                var34 = (((var35 * func48(var33)) + (float(i32_load(var9 + 220)) * -0.5)) + 0.5)
                var7 = i32_load(var9 + 216)
                var43 = (float(i32_load(var9 + 216)) * -0.5)
                var36 = (((var35 * func49(var33)) + (float(i32_load(var9 + 216)) * -0.5)) + 0.5)
                var38 = float(var1)
                var39 = float(var2)
                var37 = (var33 + 0.196349546)
                var33 = (var33 + 6.28318548)
                if (1 if (var33 + 0.196349546) >= (var33 + 6.28318548) else 0):
                    var8 = i32_load(9142440)
                    var14 = (i32_load(9142440) + 2)
                    var18 = i32_load(9142840)
                    break
                if (1 if var7 <= 0 else 0):
                    var33 = (var34 + var38)
                    if (1 if abs((var34 + var38)) < 2147483650.0 else 0):
                        break
                    var3 = -2147483648
                    var33 = (var36 + var39)
                    if (1 if (1 if abs((var36 + var39)) < 2147483650.0 else 0) == 0 else 0):
                        break
                    break
                var18 = i32_load(9142840)
                var10 = i32_load(var9 + 372)
                var8 = i32_load(9142440)
                var14 = (i32_load(9142440) + 2)
                var19 = ((i32_load(9142440) + 2) * i32_load(var9 + 208))
                var15 = i32_load(var9 + 212)
                while True:  # loop $label21
                    var34 = (var34 + var38)
                    if (1 if abs((var34 + var38)) < 2147483650.0 else 0):
                        break
                    var3 = -2147483648
                    var11 = (var3 + var28)
                    var1 = (1 if -2147483648 >= (var3 + var28) else 0)
                    var34 = (var36 + var39)
                    if (1 if abs((var36 + var39)) < 2147483650.0 else 0):
                        break
                    var4 = -2147483648
                    if var1:
                        break
                    var21 = (var4 + var7)
                    var2 = var4
                    if (1 if var27 == 1 else 0):
                        while True:  # loop $label15
                            var5 = (var2 + 1)
                            var16 = (var2 - var4)
                            var1 = var3
                            if (1 if var2 >= var8 else 0):
                                while True:  # loop $label11
                                    if i32_load8_u((var10 + (((var1 - var3) * var7) + var16))):
                                        break
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) != var11 else 0):
                                        continue
                                    break
                                    break  # end loop
                                raise RuntimeError('unreachable')
                            while True:  # loop $label14
                                if (1 if i32_load8_u((var10 + (((var1 - var3) * var7) + var16))) == 0 else 0):
                                    var1 = (var1 + 1)
                                    break
                                if (1 if var1 >= var8 else 0):
                                    break
                                if (1 if (var1 | var2) < 0 else 0):
                                    break
                                var1 = (var1 + 1)
                                if (1 if i32_load((var18 + (((((var1 + 1) + var19) * var14) + var5) << 2))) != var15 else 0):
                                    break
                                if (1 if i32_load((var18 + (((var1 * var14) + var5) << 2))) != var15 else 0):
                                    break
                                if (1 if var1 != var11 else 0):
                                    continue
                                break  # end loop
                            var2 = var5
                            if (1 if var5 < var21 else 0):
                                continue
                            break
                            break  # end loop
                        raise RuntimeError('unreachable')
                    while True:  # loop $label20
                        var5 = (var2 + 1)
                        var16 = (var2 - var4)
                        var1 = var3
                        if (1 if var2 < var8 else 0):
                            while True:  # loop $label17
                                if (1 if i32_load8_u((var10 + (((var1 - var3) * var7) + var16))) == 0 else 0):
                                    var1 = (var1 + 1)
                                    break
                                if (1 if var1 >= var8 else 0):
                                    break
                                if (1 if (var1 | var2) < 0 else 0):
                                    break
                                var1 = (var1 + 1)
                                if (1 if i32_load((var18 + (((((var1 + 1) + var19) * var14) + var5) << 2))) != var15 else 0):
                                    break
                                if (1 if var1 != var11 else 0):
                                    continue
                                break
                                break  # end loop
                            raise RuntimeError('unreachable')
                        while True:  # loop $label19
                            if i32_load8_u((var10 + (((var1 - var3) * var7) + var16))):
                                break
                            var1 = (var1 + 1)
                            if (1 if (var1 + 1) != var11 else 0):
                                continue
                            break  # end loop
                        var2 = var5
                        if (1 if var5 < var21 else 0):
                            continue
                        break  # end loop
                    break
                    var34 = (((var35 * func48(var37)) + var42) + 0.5)
                    var36 = (((var35 * func49(var37)) + var43) + 0.5)
                    var37 = (var37 + 0.196349546)
                    if (1 if (1 if (var37 + 0.196349546) >= var33 else 0) == 0 else 0):
                        continue
                    break  # end loop
                var33 = (var34 + var38)
                if (1 if abs((var34 + var38)) < 2147483650.0 else 0):
                    break
                var31 = -2147483648
                var33 = (var36 + var39)
                if (1 if abs((var36 + var39)) < 2147483650.0 else 0):
                    break
                var32 = -2147483648
                var1 = 0
                while True:  # loop $label36
                    var10 = var1
                    var1 = (var1 << 2)
                    var3 = (i32_load((((var1 << 2) | 4) + 8611904)) + var31)
                    if (1 if var8 <= (i32_load((((var1 << 2) | 4) + 8611904)) + var31) else 0):
                        break
                    var5 = (i32_load((var1 + 8611904)) + var32)
                    if (1 if var8 <= (i32_load((var1 + 8611904)) + var32) else 0):
                        break
                    if (1 if (var3 | var5) < 0 else 0):
                        break
                    if (1 if var7 <= 0 else 0):
                        break
                    var11 = (var3 + var28)
                    if (1 if (var3 + var28) <= var3 else 0):
                        break
                    var21 = (var5 + var7)
                    var15 = i32_load(var9 + 372)
                    var16 = (i32_load(var9 + 208) * var14)
                    var19 = i32_load(var9 + 212)
                    var4 = var5
                    var2 = var5
                    if (1 if var27 == 1 else 0):
                        while True:  # loop $label30
                            var2 = (var4 + 1)
                            var22 = (var4 - var5)
                            var1 = var3
                            if (1 if var4 >= var8 else 0):
                                while True:  # loop $label26
                                    if i32_load8_u((var15 + (((var1 - var3) * var7) + var22))):
                                        break
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) != var11 else 0):
                                        continue
                                    break
                                    break  # end loop
                                raise RuntimeError('unreachable')
                            while True:  # loop $label29
                                if (1 if i32_load8_u((var15 + (((var1 - var3) * var7) + var22))) == 0 else 0):
                                    var1 = (var1 + 1)
                                    break
                                if (1 if var1 >= var8 else 0):
                                    break
                                if (1 if (var1 | var4) < 0 else 0):
                                    break
                                var1 = (var1 + 1)
                                if (1 if i32_load((var18 + (((((var1 + 1) + var16) * var14) + var2) << 2))) != var19 else 0):
                                    break
                                if (1 if i32_load((var18 + (((var1 * var14) + var2) << 2))) != var19 else 0):
                                    break
                                if (1 if var1 != var11 else 0):
                                    continue
                                break  # end loop
                            var4 = var2
                            if (1 if var2 < var21 else 0):
                                continue
                            break
                            break  # end loop
                        raise RuntimeError('unreachable')
                    while True:  # loop $label35
                        var4 = (var2 + 1)
                        var22 = (var2 - var5)
                        var1 = var3
                        if (1 if var2 < var8 else 0):
                            while True:  # loop $label32
                                if (1 if i32_load8_u((var15 + (((var1 - var3) * var7) + var22))) == 0 else 0):
                                    var1 = (var1 + 1)
                                    break
                                if (1 if var1 >= var8 else 0):
                                    break
                                if (1 if (var1 | var2) < 0 else 0):
                                    break
                                var1 = (var1 + 1)
                                if (1 if i32_load((var18 + (((((var1 + 1) + var16) * var14) + var4) << 2))) != var19 else 0):
                                    break
                                if (1 if var1 != var11 else 0):
                                    continue
                                break
                                break  # end loop
                            raise RuntimeError('unreachable')
                        while True:  # loop $label34
                            if i32_load8_u((var15 + (((var1 - var3) * var7) + var22))):
                                break
                            var1 = (var1 + 1)
                            if (1 if (var1 + 1) != var11 else 0):
                                continue
                            break  # end loop
                        var2 = var4
                        if (1 if var4 < var21 else 0):
                            continue
                        break  # end loop
                    break
                    var1 = (var10 + 2)
                    if (1 if var10 < 13118 else 0):
                        continue
                    break  # end loop
                break
                var4 = -2147483648
                var1 = func34(var17, var24, var4, var3, var20, 1)
                if var26:
                    i32_store(var0 + 284624, var1)
                if (1 if i32_load(var9 + 268) == 1 else 0):
                    i32_store((i32_load(9671128) + (var1 * 132)) + 56, 1)
                if (1 if var29 == 0 else 0):
                    break
                if (1 if var1 == 0 else 0):
                    break
                var1 = (i32_load(9671128) + (var1 * 132))
                var2 = i32_load(var6 + 20)
                if (1 if i32_load(var6 + 20) <= 2147483646 else 0):
                    i32_store(var1 + 52, var2)
                var2 = i32_load(var6 + 24)
                if (1 if i32_load(var6 + 24) <= 2147483646 else 0):
                    i32_store(var1 + 60, var2)
                var2 = i32_load(var6 + 28)
                if (1 if i32_load(var6 + 28) > 2147483646 else 0):
                    break
                i32_store(var1 + 64, var2)
                if (1 if i32_load(var6 + 28) > 2147483646 else 0):
                    break
                i32_store(var1 + 68, i32_load(var6 + 32))
                var4 = i32_load(var1 + 76)
                var2 = i32_load(var6 + 36)
                if (1 if i32_load(var6 + 36) > 2147483646 else 0):
                    break
                i32_store(var1 + 72, var2)
                if (1 if i32_load(var6 + 36) > 2147483646 else 0):
                    break
                i32_store(var1 + 76, i32_load(var6 + 40))
                var2 = i32_load(var6 + 44)
                if (1 if i32_load(var6 + 44) <= 2147483646 else 0):
                    i32_store(var1 + 84, var2)
                var3 = ((i32_load8_u(var1 + 122) * 404) + 9568096)
                var2 = i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 264)
                if (1 if i32_load(var3 + 92) == 0 else 0):
                    if (1 if var2 == 2 else 0):
                        break
                    i32_store(var1 + 52, 0)
                if (1 if var2 != 1 else 0):
                    break
                i32_store(var1 + 84, 0)
                i32_store(var1 + 72, 0)
                i32_store(var1 + 60, 0)
                var2 = i32_load(var1 + 64)
                if i32_load(var1 + 64):
                else:
                    i32_store((var1 - -64), -1)
                i32_store(var2 + 68, -1)
                var2 = i32_load(var1 + 72)
                i32_store(var1 + 76, i32_load(var1 + 72))
                if (1 if var2 == 0 else 0):
                    break
                if var4:
                    break
                var26 = 0
                var23 = (var23 + 1)
                if (1 if (var23 + 1) != var12 else 0):
                    continue
                break  # end loop
            var2 = i32_load(9142428)
            var1 = var13
            var3 = var12
            var4 = (var30 + 5)
            if (1 if (var30 + 5) < var2 else 0):
                continue
            break  # end loop
        if (1 if var1 != -1 else 0):
            break
    var12 = i32_load(var0 + 283908)
    var33 = 0.0
    var10 = i32_load(((var25 << 2) + 9681488))
    var2 = ((i32_load(((var25 << 2) + 9681488)) * 404) + 9568096)
    var6 = (0 if i32_load(((i32_load(((var25 << 2) + 9681488)) * 404) + 9568096) + 264) else 2)
    var34 = (float(i32_load(var2 + 220)) * -0.5)
    var36 = (float(i32_load(var2 + 216)) * -0.5)
    var37 = float(i32_load(var0 + 283876))
    var38 = float(i32_load(var0 + 283872))
    while True:  # loop $label47
        var35 = (var33 + 0.196349546)
        var39 = ((((func48(var33) * 0.0) + var34) + 0.5) + var37)
        if (1 if abs(((((func48(var33) * 0.0) + var34) + 0.5) + var37)) < 2147483650.0 else 0):
            break
        var4 = -2147483648
        var0 = (1 if var35 >= 6.28318548 else 0)
        var33 = ((((func49(var33) * 0.0) + var36) + 0.5) + var38)
        if (1 if abs(((((func49(var33) * 0.0) + var36) + 0.5) + var38)) < 2147483650.0 else 0):
            break
        var3 = -2147483648
        if var0:
            break
        var33 = var35
        if (1 if func73(var3, var4, var2, 0, 0, 1) == 0 else 0):
            continue
        break  # end loop
    break
    var13 = i32_load(9142440)
    var0 = 0
    while True:  # loop $label51
        var1 = var0
        var5 = (var0 << 2)
        var0 = (i32_load((((var0 << 2) | 4) + 8611904)) + var4)
        if (1 if var13 <= (i32_load((((var0 << 2) | 4) + 8611904)) + var4) else 0):
            break
        var5 = (i32_load((var5 + 8611904)) + var3)
        if (1 if var13 <= (i32_load((var5 + 8611904)) + var3) else 0):
            break
        if (1 if (var0 | var5) < 0 else 0):
            break
        if func73(var5, var0, var2, 0, 0, 1):
            break
        var13 = i32_load(9142440)
        var0 = (var1 + 2)
        if (1 if var1 < 13118 else 0):
            continue
        break  # end loop
    break
    i32_store(0 + 284624, func34(var10, var12, var5, var0, var6, 1))
    return func34(var10, var12, var3, var4, var6, 1)

