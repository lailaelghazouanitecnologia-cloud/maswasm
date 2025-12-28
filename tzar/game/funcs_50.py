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
# $func177
# ==========================================================
def func177(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11):
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
    var44 = 0
    var45 = 0
    var46 = 0
    var47 = 0
    var48 = 0
    var49 = 0
    var36 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if var8 >= 2 else 0):
        var10 = var0
        var8 = var1
        var15 = var2
        var11 = var6
        var20 = var7
        var0 = 0
        var1 = 0
        var19 = var9
        var6 = i32_load(var9)
        if i32_load(var9):
            var2 = ((var6 & 0xFFFFFFFF) >> 16)
            var6 = (var6 & 65535)
            if (1 if var10 == (var6 & 65535) else 0):
                var14 = ((1 if var2 == var8 else 0) | (1 if (var8 + 1) == var2 else 0))
                if (1 if (var10 + 1) == var6 else 0):
                    break
                if (1 if var14 == 0 else 0):
                    break
                break
            if (1 if (var10 + 1) != var6 else 0):
                break
            if (1 if var2 == var8 else 0):
                break
            if (1 if (var8 + 1) == var2 else 0):
                break
            if var14:
                break
            var7 = i32_load(9671128)
            var9 = i32_load(9142840)
            var16 = (var6 + 1)
            var12 = (i32_load(9142440) + 2)
            var14 = (var2 + ((i32_load(9142440) + 2) * var5))
            var21 = (((var2 + ((i32_load(9142440) + 2) * var5)) + 1) * var12)
            var13 = i32_load((i32_load(9142840) + (((var6 + 1) + (((var2 + ((i32_load(9142440) + 2) * var5)) + 1) * var12)) << 2)))
            if (1 if var4 != i32_load((i32_load(9142840) + (((var6 + 1) + (((var2 + ((i32_load(9142440) + 2) * var5)) + 1) * var12)) << 2))) else 0):
                if (1 if var13 == -1 else 0):
                    break
                if (1 if i32_load8_u((var7 + (var13 * 132)) + 125) != 1 else 0):
                    break
            var27 = (var6 + 2)
            var13 = i32_load((var9 + ((var21 + (var6 + 2)) << 2)))
            if (1 if var4 != i32_load((var9 + ((var21 + (var6 + 2)) << 2))) else 0):
                if (1 if var13 == -1 else 0):
                    break
                if (1 if i32_load8_u((var7 + (var13 * 132)) + 125) != 1 else 0):
                    break
            var13 = ((var14 + 2) * var12)
            var12 = i32_load((var9 + ((var16 + ((var14 + 2) * var12)) << 2)))
            if (1 if var4 != i32_load((var9 + ((var16 + ((var14 + 2) * var12)) << 2))) else 0):
                if (1 if var12 == -1 else 0):
                    break
                if (1 if i32_load8_u((var7 + (var12 * 132)) + 125) != 1 else 0):
                    break
            var9 = i32_load((var9 + ((var13 + var27) << 2)))
            if (1 if var4 != i32_load((var9 + ((var13 + var27) << 2))) else 0):
                if (1 if var9 == -1 else 0):
                    break
                if (1 if i32_load8_u((var7 + (var9 * 132)) + 125) != 1 else 0):
                    break
            var14 = 1
            var27 = 0
            var7 = i32_load16_u(40596)
            var9 = (i32_load16_u(40596) + 2)
            i32_store16(40596, (i32_load16_u(40596) + 2))
            var16 = i32_load(9142440)
            if (1 if (var9 & 65535) < 65534 else 0):
                break
            i32_store16(40596, 1)
            var9 = (var16 * var16)
            if (1 if (var16 * var16) == 0 else 0):
                break
            # Unknown: memory.fill []
            var17 = (var7 + 1)
            i32_store(59200, ((var2 << 16) + var6))
            var23 = i32_load(9142436)
            var21 = 1
            while True:  # loop $label17
                var31 = (var17 & 65535)
                var2 = i32_load(((var27 << 2) + 59200))
                var7 = ((i32_load(((var27 << 2) + 59200)) & 0xFFFFFFFF) >> 16)
                var9 = (var2 & 65535)
                var2 = (var23 + (((((i32_load(((var27 << 2) + 59200)) & 0xFFFFFFFF) >> 16) * var16) + (var2 & 65535)) << 1))
                if (1 if (var17 & 65535) != i32_load16_u((var23 + (((((i32_load(((var27 << 2) + 59200)) & 0xFFFFFFFF) >> 16) * var16) + (var2 & 65535)) << 1))) else 0):
                    i32_store16(var2, var17)
                    while True:  # loop $label13
                        var22 = 0
                        var33 = (i32_load(9142440) + 2)
                        var32 = ((i32_load(9142440) + 2) * var5)
                        var26 = i32_load(9671128)
                        var24 = i32_load(9142840)
                        while True:  # loop $label9
                            var2 = (var22 << 3)
                            var12 = (i32_load(((var22 << 3) + 8928)) + var9)
                            var13 = (i32_load((var2 + 8932)) + var7)
                            var25 = ((i32_load((var2 + 8932)) + var7) + 2)
                            if (1 if ((i32_load((var2 + 8932)) + var7) + 2) <= var13 else 0):
                                break
                            var28 = 0
                            var6 = var13
                            var29 = (var12 + 2)
                            if (1 if (var12 + 2) <= var12 else 0):
                                break
                            while True:  # loop $label7
                                var6 = (var6 + 1)
                                var34 = (((var6 + 1) + var32) * var33)
                                var2 = var12
                                while True:  # loop $label6
                                    var2 = (var2 + 1)
                                    var18 = i32_load((var24 + (((var2 + 1) + var34) << 2)))
                                    if (1 if var4 != i32_load((var24 + (((var2 + 1) + var34) << 2))) else 0):
                                        if (1 if var18 == -1 else 0):
                                            break
                                        if (1 if i32_load8_u((var26 + (var18 * 132)) + 125) != 1 else 0):
                                            break
                                    if (1 if var2 != var29 else 0):
                                        continue
                                    break  # end loop
                                var28 = (1 if var6 >= var25 else 0)
                                if (1 if var6 != var25 else 0):
                                    continue
                                break  # end loop
                            if (1 if var28 == 0 else 0):
                                break
                            if (1 if i32_load16_u((var23 + (((var13 * var16) + var12) << 1))) == var31 else 0):
                                break
                            var2 = (var12 - var10)
                            var2 = (var13 - var8)
                            if (1 if ((((var12 - var10) * var2) + ((var13 - var8) * var2)) - 1) > 1156 else 0):
                                break
                            i32_store(((var21 << 2) + 59200), ((var13 << 16) + var12))
                            var21 = (var21 + 1)
                            var22 = (var22 + 1)
                            if (1 if (var22 + 1) != 8 else 0):
                                continue
                            break  # end loop
                        var2 = (var8 - var7)
                        var6 = (var10 - var9)
                        if (1 if (var10 - var9) == 0 else 0):
                            break
                        if (1 if var7 == var8 else 0):
                            break
                        var6 = (var2 // var6)
                        var6 = (var6 >> 31)
                        var6 = (var6 if (1 if (((var2 // var6) ^ (var6 >> 31)) - var6) <= 1 else 0) else 0)
                        var2 = ((var6 if (1 if (((var2 // var6) ^ (var6 >> 31)) - var6) <= 1 else 0) else 0) // var2)
                        var2 = (var2 >> 31)
                        var2 = (var2 if (1 if ((((var6 if (1 if (((var2 // var6) ^ (var6 >> 31)) - var6) <= 1 else 0) else 0) // var2) ^ (var2 >> 31)) - var2) <= 1 else 0) else 0)
                        var2 = (-1 if (1 if var2 < 0 else 0) else (1 if var2 != 0 else 0))
                        var7 = ((-1 if (1 if var2 < 0 else 0) else (1 if var2 != 0 else 0)) + var7)
                        var6 = (-1 if (1 if var6 < 0 else 0) else (1 if var6 != 0 else 0))
                        var9 = ((-1 if (1 if var6 < 0 else 0) else (1 if var6 != 0 else 0)) + var9)
                        if (1 if ((-1 if (1 if var6 < 0 else 0) else (1 if var6 != 0 else 0)) + var9) != var10 else 0):
                            break
                        if (1 if var7 != var8 else 0):
                            break
                        i32_store(var11, (0 - var6))
                        i32_store(var20, (0 - var2))
                        break
                        i32_store16((var23 + (((var7 * var16) + var9) << 1)), var17)
                        var13 = (var7 + 2)
                        if (1 if (var7 + 2) <= var7 else 0):
                            continue
                        var25 = (var9 + 2)
                        if (1 if (var9 + 2) <= var9 else 0):
                            continue
                        var6 = 0
                        var28 = (i32_load(9142440) + 2)
                        var18 = ((i32_load(9142440) + 2) * var5)
                        var33 = i32_load(9671128)
                        var32 = i32_load(9142840)
                        var12 = var7
                        while True:  # loop $label16
                            var12 = (var12 + 1)
                            var26 = (((var12 + 1) + var18) * var28)
                            var2 = var9
                            while True:  # loop $label15
                                var2 = (var2 + 1)
                                var22 = i32_load((var32 + (((var2 + 1) + var26) << 2)))
                                if (1 if var4 != i32_load((var32 + (((var2 + 1) + var26) << 2))) else 0):
                                    if (1 if var22 == -1 else 0):
                                        break
                                    if (1 if i32_load8_u((var33 + (var22 * 132)) + 125) != 1 else 0):
                                        break
                                if (1 if var2 != var25 else 0):
                                    continue
                                break  # end loop
                            var6 = (1 if var12 >= var13 else 0)
                            if (1 if var12 != var13 else 0):
                                continue
                            break  # end loop
                        if (var6 & 1):
                            continue
                        break  # end loop
                var27 = (var27 + 1)
                if (1 if (var27 + 1) < var21 else 0):
                    continue
                break  # end loop
            if 0:
                break
            i32_store(var19, 0)
        var2 = (var3 - var8)
        var23 = i32_load(9142440)
        var6 = (var15 - var10)
        if (1 if (var15 - var10) == 0 else 0):
            break
        if (1 if var3 == var8 else 0):
            break
        var6 = (var2 // var6)
        var6 = (var6 >> 31)
        var6 = (var6 if (1 if (((var2 // var6) ^ (var6 >> 31)) - var6) <= 1 else 0) else 0)
        var2 = ((var6 if (1 if (((var2 // var6) ^ (var6 >> 31)) - var6) <= 1 else 0) else 0) // var2)
        var2 = (var2 >> 31)
        var2 = (var2 if (1 if ((((var6 if (1 if (((var2 // var6) ^ (var6 >> 31)) - var6) <= 1 else 0) else 0) // var2) ^ (var2 >> 31)) - var2) <= 1 else 0) else 0)
        var6 = (-1 if (1 if var6 < 0 else 0) else (1 if var6 != 0 else 0))
        i32_store(var11, (-1 if (1 if var6 < 0 else 0) else (1 if var6 != 0 else 0)))
        var2 = (-1 if (1 if var2 < 0 else 0) else (1 if var2 != 0 else 0))
        i32_store(var20, (-1 if (1 if var2 < 0 else 0) else (1 if var2 != 0 else 0)))
        var6 = (var6 + var10)
        var2 = (var2 + var8)
        var16 = i32_load(9142440)
        var21 = (i32_load(9142440) + 2)
        var27 = ((i32_load(9142440) + 2) * var5)
        var9 = i32_load(9671128)
        var12 = i32_load(9142840)
        var13 = 0
        while True:  # loop $label26
            if (1 if var6 != var15 else 0):
                break
            if (1 if var2 != var3 else 0):
                break
            break
            if (1 if var2 > 2147483645 else 0):
                break
            if (1 if var6 > 2147483645 else 0):
                break
            var14 = (var6 + 1)
            var17 = (var2 + 1)
            var22 = (((var2 + 1) + var27) * var21)
            var7 = i32_load((var12 + (((var6 + 1) + (((var2 + 1) + var27) * var21)) << 2)))
            if (1 if var4 != i32_load((var12 + (((var6 + 1) + (((var2 + 1) + var27) * var21)) << 2))) else 0):
                if (1 if var7 == -1 else 0):
                    break
                if (1 if i32_load8_u((var9 + (var7 * 132)) + 125) != 1 else 0):
                    break
            var25 = (var6 + 2)
            var7 = i32_load((var12 + ((var22 + (var6 + 2)) << 2)))
            if (1 if var4 != i32_load((var12 + ((var22 + (var6 + 2)) << 2))) else 0):
                if (1 if var7 == -1 else 0):
                    break
                if (1 if i32_load8_u((var9 + (var7 * 132)) + 125) != 1 else 0):
                    break
            var22 = (var2 + 2)
            var28 = (((var2 + 2) + var27) * var21)
            var7 = i32_load((var12 + ((var14 + (((var2 + 2) + var27) * var21)) << 2)))
            if (1 if var4 != i32_load((var12 + ((var14 + (((var2 + 2) + var27) * var21)) << 2))) else 0):
                if (1 if var7 == -1 else 0):
                    break
                if (1 if i32_load8_u((var9 + (var7 * 132)) + 125) != 1 else 0):
                    break
            var7 = i32_load((var12 + ((var25 + var28) << 2)))
            if (1 if var4 != i32_load((var12 + ((var25 + var28) << 2))) else 0):
                if (1 if var7 == -1 else 0):
                    break
                if (1 if i32_load8_u((var9 + (var7 * 132)) + 125) != 1 else 0):
                    break
            break
            if (1 if var17 < var22 else 0):
                break
            var14 = (var3 - var2)
            var7 = (var15 - var6)
            if (1 if (var15 - var6) == 0 else 0):
                break
            if (1 if var2 == var3 else 0):
                break
            var7 = (var14 // var7)
            var7 = (var7 >> 31)
            var7 = (var7 if (1 if (((var14 // var7) ^ (var7 >> 31)) - var7) <= 1 else 0) else 0)
            var14 = ((var7 if (1 if (((var14 // var7) ^ (var7 >> 31)) - var7) <= 1 else 0) else 0) // var14)
            var14 = (var14 >> 31)
            var14 = (var14 if (1 if ((((var7 if (1 if (((var14 // var7) ^ (var7 >> 31)) - var7) <= 1 else 0) else 0) // var14) ^ (var14 >> 31)) - var14) <= 1 else 0) else 0)
            var6 = ((-1 if (1 if var7 < 0 else 0) else (1 if var7 != 0 else 0)) + var6)
            var2 = ((-1 if (1 if var14 < 0 else 0) else (1 if var14 != 0 else 0)) + var2)
            var14 = 1
            var13 = (var13 + 1)
            if (1 if (var13 + 1) != 32 else 0):
                continue
            break
            break  # end loop
        var21 = i32_load16_u(40596)
        var7 = (i32_load16_u(40596) + 2)
        i32_store16(40596, (i32_load16_u(40596) + 2))
        var26 = (var6 + (var2 << 16))
        if (1 if (var7 & 65535) < 65534 else 0):
            break
        i32_store16(40596, 1)
        var7 = (var16 * var16)
        if (1 if (var16 * var16) == 0 else 0):
            break
        # Unknown: memory.fill []
        var33 = (var21 + 1)
        i32_store(59200, var26)
        var17 = i32_load(9142436)
        i32_store16((i32_load(9142436) + ((var6 + (var2 * var23)) << 1)), var21)
        var27 = 2147483647
        var18 = 1
        var2 = 0
        var25 = 0
        while True:  # loop $label44
            var35 = (3000 if (1 if var25 <= 3000 else 0) else var25)
            var12 = (var2 + 1)
            var2 = i32_load(((var2 << 2) + 59200))
            var9 = ((i32_load(((var2 << 2) + 59200)) & 0xFFFFFFFF) >> 16)
            var16 = (var2 & 65535)
            while True:  # loop $label43
                if (1 if var25 == var35 else 0):
                    break
                var25 = (var25 + 1)
                var14 = 0
                var31 = 0
                while True:  # loop $label42
                    var2 = (var14 << 4)
                    var6 = (i32_load(((var14 << 4) + 8932)) + var9)
                    if (1 if (i32_load(((var14 << 4) + 8932)) + var9) > 2147483645 else 0):
                        break
                    var7 = (i32_load((var2 + 8928)) + var16)
                    if (1 if (i32_load((var2 + 8928)) + var16) > 2147483645 else 0):
                        break
                    var13 = i32_load(9671128)
                    var22 = i32_load(9142840)
                    var29 = (var7 + 1)
                    var34 = (var6 + 1)
                    var28 = (i32_load(9142440) + 2)
                    var32 = ((i32_load(9142440) + 2) * var5)
                    var24 = (((var6 + 1) + ((i32_load(9142440) + 2) * var5)) * var28)
                    var2 = i32_load((i32_load(9142840) + (((var7 + 1) + (((var6 + 1) + ((i32_load(9142440) + 2) * var5)) * var28)) << 2)))
                    if (1 if i32_load((i32_load(9142840) + (((var7 + 1) + (((var6 + 1) + ((i32_load(9142440) + 2) * var5)) * var28)) << 2))) == var4 else 0):
                        break
                    if (1 if var2 == -1 else 0):
                        break
                    if (1 if i32_load8_u((var13 + (var2 * 132)) + 125) != 1 else 0):
                        break
                    var38 = (var7 + 2)
                    var24 = i32_load((var22 + (((var7 + 2) + var24) << 2)))
                    if (1 if i32_load((var22 + (((var7 + 2) + var24) << 2))) == var4 else 0):
                        break
                    if (1 if var24 == -1 else 0):
                        break
                    if (1 if i32_load8_u((var13 + (var24 * 132)) + 125) != 1 else 0):
                        break
                    var37 = (var6 + 2)
                    var39 = (((var6 + 2) + var32) * var28)
                    var24 = i32_load((var22 + ((var29 + (((var6 + 2) + var32) * var28)) << 2)))
                    if (1 if i32_load((var22 + ((var29 + (((var6 + 2) + var32) * var28)) << 2))) == var4 else 0):
                        break
                    if (1 if var24 == -1 else 0):
                        break
                    if (1 if i32_load8_u((var13 + (var24 * 132)) + 125) != 1 else 0):
                        break
                    var24 = i32_load((var22 + ((var38 + var39) << 2)))
                    if (1 if i32_load((var22 + ((var38 + var39) << 2))) == var4 else 0):
                        break
                    if (1 if var24 == -1 else 0):
                        break
                    if (1 if i32_load8_u((var13 + (var24 * 132)) + 125) != 1 else 0):
                        break
                    break
                    if (1 if var34 >= var37 else 0):
                        break
                    if (1 if var2 != -1 else 0):
                        break
                    break
                    if (1 if var2 == -1 else 0):
                        break
                    var2 = 0
                    var38 = (var17 + (((var6 * var23) + var7) << 1))
                    if (1 if i32_load16_u((var17 + (((var6 * var23) + var7) << 1))) == var21 else 0):
                        break
                    while True:  # loop $label40
                        var29 = (var2 << 3)
                        var24 = (i32_load(((var2 << 3) + 8932)) + var6)
                        if (1 if (i32_load(((var2 << 3) + 8932)) + var6) > 2147483645 else 0):
                            break
                        var29 = (i32_load((var29 + 8928)) + var7)
                        if (1 if (i32_load((var29 + 8928)) + var7) > 2147483645 else 0):
                            break
                        var37 = (var29 + 1)
                        var39 = (var24 + 1)
                        var40 = (((var24 + 1) + var32) * var28)
                        var34 = i32_load((var22 + (((var29 + 1) + (((var24 + 1) + var32) * var28)) << 2)))
                        if (1 if var4 != i32_load((var22 + (((var29 + 1) + (((var24 + 1) + var32) * var28)) << 2))) else 0):
                            if (1 if var34 == -1 else 0):
                                break
                            if (1 if i32_load8_u((var13 + (var34 * 132)) + 125) != 1 else 0):
                                break
                        var34 = (var29 + 2)
                        var29 = i32_load((var22 + (((var29 + 2) + var40) << 2)))
                        if (1 if var4 != i32_load((var22 + (((var29 + 2) + var40) << 2))) else 0):
                            if (1 if var29 == -1 else 0):
                                break
                            if (1 if i32_load8_u((var13 + (var29 * 132)) + 125) != 1 else 0):
                                break
                        var29 = (var24 + 2)
                        var40 = (((var24 + 2) + var32) * var28)
                        var24 = i32_load((var22 + ((var37 + (((var24 + 2) + var32) * var28)) << 2)))
                        if (1 if var4 != i32_load((var22 + ((var37 + (((var24 + 2) + var32) * var28)) << 2))) else 0):
                            if (1 if var24 == -1 else 0):
                                break
                            if (1 if i32_load8_u((var13 + (var24 * 132)) + 125) != 1 else 0):
                                break
                        var24 = i32_load((var22 + ((var34 + var40) << 2)))
                        if (1 if var4 != i32_load((var22 + ((var34 + var40) << 2))) else 0):
                            if (1 if var24 == -1 else 0):
                                break
                            if (1 if i32_load8_u((var13 + (var24 * 132)) + 125) != 1 else 0):
                                break
                        break
                        if (1 if var29 <= var39 else 0):
                            break
                        var2 = (var2 + 1)
                        if (1 if (var2 + 1) != 8 else 0):
                            continue
                        break
                        break  # end loop
                    var2 = ((var6 << 16) + var7)
                    if (1 if var31 == 0 else 0):
                        var0 = var7
                        var1 = var6
                        break
                    i32_store(((var18 << 2) + 59200), var2)
                    var18 = (var18 + 1)
                    i32_store16(var38, var21)
                    var6 = (var6 - var3)
                    var6 = (var7 - var15)
                    var6 = (((var6 - var3) * var6) + ((var7 - var15) * var6))
                    var6 = (1 if var6 < var27 else 0)
                    var27 = ((((var6 - var3) * var6) + ((var7 - var15) * var6)) if (1 if var6 < var27 else 0) else var27)
                    var30 = (var2 if var6 else var30)
                    var31 = (var31 + 1)
                    var14 = (var14 + 1)
                    if (1 if (var14 + 1) != 4 else 0):
                        continue
                    break  # end loop
                var16 = var0
                var9 = var1
                if var31:
                    continue
                break  # end loop
            if (1 if var12 >= var18 else 0):
                break
            var2 = var12
            if (1 if var25 < 3001 else 0):
                continue
            break  # end loop
        var6 = 0
        var12 = (i32_load(9142440) + 2)
        var16 = ((i32_load(9142440) + 2) * var5)
        var7 = 2147483647
        var0 = (var26 if (1 if var27 == 2147483647 else 0) else var30)
        var27 = (((var26 if (1 if var27 == 2147483647 else 0) else var30) & 0xFFFFFFFF) >> 16)
        var22 = (var0 & 65535)
        var1 = i32_load(9671128)
        var2 = i32_load(9142840)
        var13 = 55
        while True:  # loop $label48
            var9 = (var6 << 3)
            var0 = (i32_load(((var6 << 3) + 8928)) + var22)
            var9 = (i32_load((var9 + 8932)) + var27)
            if (1 if (i32_load((var9 + 8932)) + var27) > 2147483645 else 0):
                break
            if (1 if var0 > 2147483645 else 0):
                break
            var25 = (var0 + 1)
            var28 = (var9 + 1)
            var18 = (((var9 + 1) + var16) * var12)
            var14 = i32_load((var2 + (((var0 + 1) + (((var9 + 1) + var16) * var12)) << 2)))
            if (1 if var4 != i32_load((var2 + (((var0 + 1) + (((var9 + 1) + var16) * var12)) << 2))) else 0):
                if (1 if var14 == -1 else 0):
                    break
                if (1 if i32_load8_u((var1 + (var14 * 132)) + 125) != 1 else 0):
                    break
            var30 = (var0 + 2)
            var14 = i32_load((var2 + ((var18 + (var0 + 2)) << 2)))
            if (1 if var4 != i32_load((var2 + ((var18 + (var0 + 2)) << 2))) else 0):
                if (1 if var14 == -1 else 0):
                    break
                if (1 if i32_load8_u((var1 + (var14 * 132)) + 125) != 1 else 0):
                    break
            var18 = (var9 + 2)
            var31 = (((var9 + 2) + var16) * var12)
            var14 = i32_load((var2 + ((var25 + (((var9 + 2) + var16) * var12)) << 2)))
            if (1 if var4 != i32_load((var2 + ((var25 + (((var9 + 2) + var16) * var12)) << 2))) else 0):
                if (1 if var14 == -1 else 0):
                    break
                if (1 if i32_load8_u((var1 + (var14 * 132)) + 125) != 1 else 0):
                    break
            var14 = i32_load((var2 + ((var30 + var31) << 2)))
            if (1 if var4 != i32_load((var2 + ((var30 + var31) << 2))) else 0):
                if (1 if var14 == -1 else 0):
                    break
                if (1 if i32_load8_u((var1 + (var14 * 132)) + 125) != 1 else 0):
                    break
            break
            if (1 if var18 > var28 else 0):
                break
            var14 = (var9 - var3)
            var14 = (var0 - var15)
            var14 = (((var9 - var3) * var14) + ((var0 - var15) * var14))
            var14 = (1 if var7 > var14 else 0)
            var7 = ((((var9 - var3) * var14) + ((var0 - var15) * var14)) if (1 if var7 > var14 else 0) else var7)
            var13 = (((var9 << 16) + var0) if var14 else var13)
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != 8 else 0):
                continue
            break  # end loop
        i32_store(59200, var13)
        i32_store16((var17 + (((((var13 & 0xFFFFFFFF) >> 16) * var23) + (var13 & 65535)) << 1)), var33)
        var27 = 1
        var0 = 0
        while True:  # loop $label66
            var1 = var0
            var0 = (var0 + 1)
            var15 = i32_load(((var1 << 2) + 59200))
            var25 = ((i32_load(((var1 << 2) + 59200)) & 0xFFFFFFFF) >> 16)
            var28 = (var15 & 65535)
            var9 = 0
            while True:  # loop $label65
                var1 = (var9 << 3)
                var14 = i32_load(((var9 << 3) + 8928))
                var6 = (i32_load(((var9 << 3) + 8928)) + var28)
                var16 = i32_load((var1 + 8932))
                var2 = (i32_load((var1 + 8932)) + var25)
                if (1 if (i32_load((var1 + 8932)) + var25) > 2147483645 else 0):
                    break
                if (1 if var6 > 2147483645 else 0):
                    break
                var1 = i32_load(9671128)
                var3 = i32_load(9142840)
                var13 = (var6 + 1)
                var22 = (var2 + 1)
                var7 = (i32_load(9142440) + 2)
                var18 = ((i32_load(9142440) + 2) * var5)
                var30 = (((var2 + 1) + ((i32_load(9142440) + 2) * var5)) * var7)
                var12 = i32_load((i32_load(9142840) + (((var6 + 1) + (((var2 + 1) + ((i32_load(9142440) + 2) * var5)) * var7)) << 2)))
                if (1 if var4 != i32_load((i32_load(9142840) + (((var6 + 1) + (((var2 + 1) + ((i32_load(9142440) + 2) * var5)) * var7)) << 2))) else 0):
                    if (1 if var12 == -1 else 0):
                        break
                    if (1 if i32_load8_u((var1 + (var12 * 132)) + 125) != 1 else 0):
                        break
                var31 = (var6 + 2)
                var12 = i32_load((var3 + ((var30 + (var6 + 2)) << 2)))
                if (1 if var4 != i32_load((var3 + ((var30 + (var6 + 2)) << 2))) else 0):
                    if (1 if var12 == -1 else 0):
                        break
                    if (1 if i32_load8_u((var1 + (var12 * 132)) + 125) != 1 else 0):
                        break
                var12 = (var2 + 2)
                var18 = (((var2 + 2) + var18) * var7)
                var7 = i32_load((var3 + ((var13 + (((var2 + 2) + var18) * var7)) << 2)))
                if (1 if var4 != i32_load((var3 + ((var13 + (((var2 + 2) + var18) * var7)) << 2))) else 0):
                    if (1 if var7 == -1 else 0):
                        break
                    if (1 if i32_load8_u((var1 + (var7 * 132)) + 125) != 1 else 0):
                        break
                var3 = i32_load((var3 + ((var18 + var31) << 2)))
                if (1 if var4 != i32_load((var3 + ((var18 + var31) << 2))) else 0):
                    if (1 if var3 == -1 else 0):
                        break
                    if (1 if i32_load8_u((var1 + (var3 * 132)) + 125) != 1 else 0):
                        break
                break
                if (1 if var12 > var22 else 0):
                    break
                var13 = (var2 * var23)
                var18 = (var17 + (((var2 * var23) + var6) << 1))
                if (1 if i32_load16_u((var17 + (((var2 * var23) + var6) << 1))) == (var33 & 65535) else 0):
                    break
                var3 = (var6 + 1)
                var1 = i32_load(9142440)
                var30 = (1 if i32_load(9142440) <= var2 else 0)
                if (1 if i32_load(9142440) <= var2 else 0):
                    break
                if (1 if var1 <= var3 else 0):
                    break
                if (1 if (var2 | var3) < 0 else 0):
                    break
                if (1 if i32_load16_u((var17 + ((var3 + var13) << 1))) == var21 else 0):
                    break
                var12 = (var2 - 1)
                var22 = (1 if var1 <= (var2 - 1) else 0)
                if (1 if var1 <= (var2 - 1) else 0):
                    break
                if (1 if var1 <= var3 else 0):
                    break
                if (1 if (var3 | var12) < 0 else 0):
                    break
                if (1 if i32_load16_u((var17 + (((var12 * var23) + var3) << 1))) == var21 else 0):
                    break
                if var22:
                    break
                if (1 if var1 <= var6 else 0):
                    break
                if (1 if (var6 | var12) < 0 else 0):
                    break
                if (1 if i32_load16_u((var17 + (((var12 * var23) + var6) << 1))) == var21 else 0):
                    break
                var7 = (var6 - 1)
                if var22:
                    break
                if (1 if var1 <= var7 else 0):
                    break
                if (1 if (var7 | var12) < 0 else 0):
                    break
                if (1 if i32_load16_u((var17 + (((var12 * var23) + var7) << 1))) == var21 else 0):
                    break
                if var30:
                    break
                if (1 if var1 <= var7 else 0):
                    break
                if (1 if (var2 | var7) < 0 else 0):
                    break
                if (1 if i32_load16_u((var17 + ((var7 + var13) << 1))) == var21 else 0):
                    break
                var12 = (var2 + 1)
                var13 = (1 if var1 <= (var2 + 1) else 0)
                if (1 if var1 <= (var2 + 1) else 0):
                    break
                if (1 if var1 <= var7 else 0):
                    break
                if (1 if (var7 | var12) < 0 else 0):
                    break
                if (1 if i32_load16_u((var17 + (((var12 * var23) + var7) << 1))) == var21 else 0):
                    break
                if var13:
                    break
                if (1 if var1 <= var6 else 0):
                    break
                if (1 if (var6 | var12) < 0 else 0):
                    break
                if (1 if i32_load16_u((var17 + (((var12 * var23) + var6) << 1))) == var21 else 0):
                    break
                if var13:
                    break
                if (1 if var1 <= var3 else 0):
                    break
                if (1 if (var3 | var12) < 0 else 0):
                    break
                if (1 if i32_load16_u((var17 + (((var12 * var23) + var3) << 1))) != var21 else 0):
                    break
                i32_store(((var27 << 2) + 59200), ((var2 << 16) + var6))
                var3 = (var6 - var10)
                var3 = (var2 - var8)
                if (1 if ((((var6 - var10) * var3) + ((var2 - var8) * var3)) - 1) > 1089 else 0):
                    break
                if (1 if ((1 if var6 == var10 else 0) & (1 if var2 == var8 else 0)) == 0 else 0):
                    var13 = (1 if var2 == var8 else 0)
                    var12 = (var1 + 2)
                    var22 = ((var1 + 2) * var5)
                    var1 = i32_load(9671128)
                    var3 = i32_load(9142840)
                    while True:  # loop $label64
                        var14 = (var8 - var2)
                        var7 = (var10 - var6)
                        if (1 if (var10 - var6) == 0 else 0):
                            break
                        if (var13 & 1):
                            break
                        var7 = (var14 // var7)
                        var7 = (var7 >> 31)
                        var7 = (var7 if (1 if (((var14 // var7) ^ (var7 >> 31)) - var7) <= 1 else 0) else 0)
                        var13 = ((var7 if (1 if (((var14 // var7) ^ (var7 >> 31)) - var7) <= 1 else 0) else 0) // var14)
                        var13 = (var13 >> 31)
                        var14 = (var14 if (1 if ((((var7 if (1 if (((var14 // var7) ^ (var7 >> 31)) - var7) <= 1 else 0) else 0) // var14) ^ (var13 >> 31)) - var13) <= 1 else 0) else 0)
                        var16 = (-1 if (1 if var14 < 0 else 0) else (1 if var14 != 0 else 0))
                        var2 = ((-1 if (1 if var14 < 0 else 0) else (1 if var14 != 0 else 0)) + var2)
                        var14 = (-1 if (1 if var7 < 0 else 0) else (1 if var7 != 0 else 0))
                        var6 = ((-1 if (1 if var7 < 0 else 0) else (1 if var7 != 0 else 0)) + var6)
                        if (1 if i32_load16_u((var17 + (((((-1 if (1 if var14 < 0 else 0) else (1 if var14 != 0 else 0)) + var2) * var23) + ((-1 if (1 if var7 < 0 else 0) else (1 if var7 != 0 else 0)) + var6)) << 1))) != var21 else 0):
                            break
                        if (1 if var2 > 2147483645 else 0):
                            break
                        if (1 if var6 > 2147483645 else 0):
                            break
                        var13 = (var6 + 1)
                        var30 = (var2 + 1)
                        var31 = (((var2 + 1) + var22) * var12)
                        var7 = i32_load((var3 + (((var6 + 1) + (((var2 + 1) + var22) * var12)) << 2)))
                        if (1 if var4 != i32_load((var3 + (((var6 + 1) + (((var2 + 1) + var22) * var12)) << 2))) else 0):
                            if (1 if var7 == -1 else 0):
                                break
                            if (1 if i32_load8_u((var1 + (var7 * 132)) + 125) != 1 else 0):
                                break
                        var32 = (var6 + 2)
                        var7 = i32_load((var3 + ((var31 + (var6 + 2)) << 2)))
                        if (1 if var4 != i32_load((var3 + ((var31 + (var6 + 2)) << 2))) else 0):
                            if (1 if var7 == -1 else 0):
                                break
                            if (1 if i32_load8_u((var1 + (var7 * 132)) + 125) != 1 else 0):
                                break
                        var31 = (var2 + 2)
                        var26 = (((var2 + 2) + var22) * var12)
                        var7 = i32_load((var3 + ((var13 + (((var2 + 2) + var22) * var12)) << 2)))
                        if (1 if var4 != i32_load((var3 + ((var13 + (((var2 + 2) + var22) * var12)) << 2))) else 0):
                            if (1 if var7 == -1 else 0):
                                break
                            if (1 if i32_load8_u((var1 + (var7 * 132)) + 125) != 1 else 0):
                                break
                        var7 = i32_load((var3 + ((var26 + var32) << 2)))
                        if (1 if var4 != i32_load((var3 + ((var26 + var32) << 2))) else 0):
                            if (1 if var7 == -1 else 0):
                                break
                            if (1 if i32_load8_u((var1 + (var7 * 132)) + 125) != 1 else 0):
                                break
                        break
                        if (1 if var30 < var31 else 0):
                            break
                        var13 = (1 if var2 == var8 else 0)
                        if (1 if var6 != var10 else 0):
                            continue
                        if (1 if var2 != var8 else 0):
                            continue
                        break  # end loop
                i32_store(var11, (0 - var14))
                i32_store(var20, (0 - var16))
                i32_store(var19, var15)
                break
                var27 = (var27 + 1)
                i32_store16(var18, var33)
                var9 = (var9 + 1)
                if (1 if (var9 + 1) != 8 else 0):
                    continue
                break  # end loop
            var14 = 0
            if (1 if var0 < var27 else 0):
                continue
            break  # end loop
        var20 = var14
        break
    var8 = i32_load(var9)
    if i32_load(var9):
        var20 = 1
        if func365(var0, var1, (var8 & 65535), ((var8 & 0xFFFFFFFF) >> 16), var4, var5, var6, var7, i32_load8_u(var10)):
            break
        i32_store(var9, 0)
    i32_store(var6, (-1 if (1 if var0 > var2 else 0) else (1 if var0 != var2 else 0)))
    i32_store(var7, (-1 if (1 if var1 > var3 else 0) else (1 if var1 != var3 else 0)))
    var24 = (i32_load(9142440) + 2)
    var14 = ((i32_load(9142440) + 2) * var5)
    var32 = i32_load(9671128)
    var26 = i32_load(9142840)
    var20 = 1
    var8 = var0
    var12 = var1
    while True:  # loop $label69
        var27 = ((-1 if (1 if var2 < var8 else 0) else (1 if var2 != var8 else 0)) + var8)
        var21 = ((-1 if (1 if var3 < var12 else 0) else (1 if var3 != var12 else 0)) + var12)
        if ((1 if var2 == ((-1 if (1 if var2 < var8 else 0) else (1 if var2 != var8 else 0)) + var8) else 0) & (1 if ((-1 if (1 if var3 < var12 else 0) else (1 if var3 != var12 else 0)) + var12) == var3 else 0)):
            break
        var15 = i32_load((((var27 + (((var14 + var21) + 1) * var24)) << 2) + var26) + 4)
        if (1 if var4 != i32_load((((var27 + (((var14 + var21) + 1) * var24)) << 2) + var26) + 4) else 0):
            if (1 if var15 == -1 else 0):
                break
            if (1 if i32_load8_u((var32 + (var15 * 132)) + 125) != 1 else 0):
                break
        var8 = var27
        var12 = var21
        var16 = (var16 + 1)
        if (1 if (var16 + 1) != 32 else 0):
            continue
        break
        break  # end loop
    i32_store(var36 + 8, var12)
    i32_store(var36 + 12, var8)
    var28 = var4
    var20 = (i32_load(9142440) + 2)
    var12 = ((i32_load(9142440) + 2) * var5)
    var15 = i32_load(9671128)
    var13 = i32_load(9142840)
    var19 = i32_load(var36 + 8)
    var4 = (var21 - i32_load(var36 + 8))
    var22 = ((var21 - i32_load(var36 + 8)) * var4)
    var4 = var27
    var16 = (var27 + 1)
    var17 = i32_load(var36 + 12)
    var8 = ((var27 + 1) - i32_load(var36 + 12))
    if (1 if (((var21 - i32_load(var36 + 8)) * var4) + (((var27 + 1) - i32_load(var36 + 12)) * var8)) > 2 else 0):
        break
    var8 = i32_load((((var4 + (((var12 + var21) + 1) * var20)) << 2) + var13) + 8)
    if (1 if var28 != i32_load((((var4 + (((var12 + var21) + 1) * var20)) << 2) + var13) + 8) else 0):
        if (1 if var8 == -1 else 0):
            break
        if (1 if i32_load8_u((var15 + (var8 * 132)) + 125) != 1 else 0):
            break
    break
    var8 = (var4 - var17)
    var25 = ((var4 - var17) * var8)
    var8 = (var21 - 1)
    var23 = ((var21 - 1) - var19)
    if (1 if (((var4 - var17) * var8) + (((var21 - 1) - var19) * var23)) > 2 else 0):
        break
    var23 = i32_load((var13 + ((var16 + ((var12 + var21) * var20)) << 2)))
    if (1 if i32_load((var13 + ((var16 + ((var12 + var21) * var20)) << 2))) == var28 else 0):
        break
    if (1 if var23 == -1 else 0):
        break
    if (1 if i32_load8_u((var15 + (var23 * 132)) + 125) == 1 else 0):
        break
    var8 = (var21 + 1)
    var23 = (var4 - 1)
    var17 = ((var4 - 1) - var17)
    if (1 if (var22 + (((var4 - 1) - var17) * var17)) > 2 else 0):
        break
    var17 = i32_load((var13 + ((((var8 + var12) * var20) + var4) << 2)))
    if (1 if i32_load((var13 + ((((var8 + var12) * var20) + var4) << 2))) == var28 else 0):
        break
    if (1 if var17 == -1 else 0):
        break
    if (1 if i32_load8_u((var15 + (var17 * 132)) + 125) == 1 else 0):
        break
    var19 = (var8 - var19)
    if (1 if (((var8 - var19) * var19) + var25) > 2 else 0):
        break
    var20 = i32_load((var13 + ((var16 + (((var12 + var21) + 2) * var20)) << 2)))
    if (1 if i32_load((var13 + ((var16 + (((var12 + var21) + 2) * var20)) << 2))) == var28 else 0):
        break
    if (1 if var20 == -1 else 0):
        break
    if (1 if i32_load8_u((var15 + (var20 * 132)) + 125) == 1 else 0):
        break
    break
    var4 = var23
    var8 = var21
    i32_store(var36 + 12, var4)
    i32_store(var36 + 8, var8)
    if 1:
        var4 = i32_load(var36 + 12)
        var13 = i32_load(var36 + 8)
        break
    var4 = i32_load(var36 + 12)
    var12 = (i32_load(var36 + 12) + 1)
    var13 = i32_load(var36 + 8)
    var8 = (i32_load(var36 + 8) + 1)
    var19 = (((var14 + (i32_load(var36 + 8) + 1)) * var24) + var4)
    var20 = i32_load((((((var14 + (i32_load(var36 + 8) + 1)) * var24) + var4) << 2) + var26) + 8)
    if (1 if i32_load((((((var14 + (i32_load(var36 + 8) + 1)) * var24) + var4) << 2) + var26) + 8) == var28 else 0):
        break
    if (1 if var20 != -1 else 0):
        if (1 if i32_load8_u((var32 + (var20 * 132)) + 125) == 1 else 0):
            break
    var15 = var12
    break
    var17 = (var13 + var14)
    var16 = i32_load((var26 + ((((var13 + var14) * var24) + var12) << 2)))
    if (1 if var28 != i32_load((var26 + ((((var13 + var14) * var24) + var12) << 2))) else 0):
        var20 = (var13 - 1)
        if (1 if var16 == -1 else 0):
            var15 = var4
            break
        var15 = var4
        if (1 if i32_load8_u((var32 + (var16 * 132)) + 125) != 1 else 0):
            break
    var16 = i32_load((var26 + (var19 << 2)))
    if (1 if var28 != i32_load((var26 + (var19 << 2))) else 0):
        var15 = (var4 - 1)
        if (1 if var16 == -1 else 0):
            break
        var20 = var13
        if (1 if i32_load8_u((var32 + (var16 * 132)) + 125) != 1 else 0):
            break
    var12 = i32_load((var26 + ((((var17 + 2) * var24) + var12) << 2)))
    if (1 if i32_load((var26 + ((((var17 + 2) * var24) + var12) << 2))) == var28 else 0):
        break
    if (1 if var12 == -1 else 0):
        var15 = var4
        var20 = var8
        break
    var15 = var4
    var20 = var8
    if (1 if i32_load8_u((var32 + (var12 * 132)) + 125) != 1 else 0):
        break
    var20 = var21
    var15 = var27
    break
    var20 = var13
    var19 = (var13 - var20)
    var30 = (var4 - var15)
    var29 = (var14 + 1)
    var14 = var13
    var16 = var4
    var12 = var20
    var8 = var15
    while True:  # loop $label95
        var17 = (var14 + var30)
        var23 = (var16 + var19)
        var22 = (var8 + var19)
        var25 = (var12 + var30)
        var35 = i32_load(((((var8 + var19) + (var24 * (var29 + (var12 + var30)))) << 2) + var26) + 4)
        if (1 if i32_load(((((var8 + var19) + (var24 * (var29 + (var12 + var30)))) << 2) + var26) + 4) == var28 else 0):
            break
        if (1 if var35 != -1 else 0):
            if (1 if i32_load8_u((var32 + (var35 * 132)) + 125) == 1 else 0):
                break
        var35 = 0
        var38 = i32_load((((var23 + ((var17 + var29) * var24)) << 2) + var26) + 4)
        if (1 if var28 != i32_load((((var23 + ((var17 + var29) * var24)) << 2) + var26) + 4) else 0):
            if (1 if var38 == -1 else 0):
                break
            if var35:
                break
            if (1 if i32_load8_u((var32 + (var38 * 132)) + 125) != 1 else 0):
                break
            break
        if (1 if var35 == 0 else 0):
            break
        var19 = ((var18 << 2) + 59200)
        i32_store(((var18 << 2) + 59200), var23)
        i32_store(var19 + 8, var33)
        i32_store(var19 + 4, var17)
        i32_store(var19 + 12, (((var8 - var23) + ((var12 - var17) * 3)) + 4))
        var30 = (var12 - var14)
        var19 = (var8 - var16)
        var18 = (var18 + 4)
        var14 = var25
        var16 = var22
        break
        var19 = ((var18 << 2) + 59200)
        i32_store(((var18 << 2) + 59200), var16)
        i32_store(var19 + 8, var33)
        i32_store(var19 + 4, var14)
        i32_store(var19 + 12, (((var22 - var16) + ((var25 - var14) * 3)) + 13))
        var30 = (var14 - var12)
        var19 = (var16 - var8)
        var18 = (var18 + 4)
        var12 = var17
        var8 = var23
        break
        var33 = 0
        i32_store(59208, 0)
        i32_store(59204, var14)
        i32_store(59200, var16)
        i32_store(59212, (((var8 - var16) + ((var12 - var14) * 3)) + 13))
        var25 = (0 - var30)
        var30 = (0 - var19)
        var13 = var14
        var4 = var16
        var18 = 4
        var19 = var12
        var20 = var8
        while True:  # loop $label93
            var15 = (var13 + var25)
            var17 = (var4 + var30)
            var23 = (var20 + var30)
            var22 = (var19 + var25)
            var34 = i32_load(((((var20 + var30) + (var24 * (var29 + (var19 + var25)))) << 2) + var26) + 4)
            if (1 if i32_load(((((var20 + var30) + (var24 * (var29 + (var19 + var25)))) << 2) + var26) + 4) == var28 else 0):
                break
            if (1 if var34 != -1 else 0):
                if (1 if i32_load8_u((var32 + (var34 * 132)) + 125) == 1 else 0):
                    break
            var34 = 0
            var35 = i32_load((((var17 + ((var15 + var29) * var24)) << 2) + var26) + 4)
            if (1 if var28 != i32_load((((var17 + ((var15 + var29) * var24)) << 2) + var26) + 4) else 0):
                if (1 if var35 == -1 else 0):
                    break
                if var34:
                    break
                if (1 if i32_load8_u((var32 + (var35 * 132)) + 125) == 1 else 0):
                    break
                var25 = ((var18 << 2) + 59200)
                i32_store(((var18 << 2) + 59200), var4)
                i32_store(var25 + 8, var33)
                i32_store(var25 + 4, var13)
                i32_store(var25 + 12, (((var23 - var4) + ((var22 - var13) * 3)) + 13))
                var25 = (var13 - var19)
                var30 = (var4 - var20)
                var18 = (var18 + 4)
                var19 = var15
                var20 = var17
                break
            if (1 if var34 == 0 else 0):
                break
            var25 = ((var18 << 2) + 59200)
            i32_store(((var18 << 2) + 59200), var17)
            i32_store(var25 + 8, var33)
            i32_store(var25 + 4, var15)
            i32_store(var25 + 12, (((var20 - var17) + ((var19 - var15) * 3)) + 4))
            var25 = (var19 - var13)
            var30 = (var20 - var4)
            var18 = (var18 + 4)
            var13 = var22
            var4 = var23
            break
            var13 = var15
            var4 = var17
            var19 = var22
            var20 = var23
            var34 = 1
            var33 = (var33 + 1)
            if (1 if var8 != var20 else 0):
                continue
            if (1 if var12 != var19 else 0):
                continue
            if (1 if var4 != var16 else 0):
                continue
            if (1 if var13 != var14 else 0):
                continue
            break
            break  # end loop
        var8 = ((var18 << 2) + 59200)
        i32_store(((var18 << 2) + 59200), var4)
        i32_store(var8 + 8, var33)
        i32_store(var8 + 4, var13)
        i32_store(var8 + 12, (((var20 - var4) + ((var19 - var13) * 3)) + 13))
        var18 = (var18 + 4)
        var34 = 1
        break
        var14 = var17
        var16 = var23
        var12 = var25
        var8 = var22
        var33 = (var33 + 1)
        if (1 if var8 != var15 else 0):
            continue
        if (1 if var12 != var20 else 0):
            continue
        if (1 if var4 != var16 else 0):
            continue
        if (1 if var13 != var14 else 0):
            continue
        break  # end loop
    var20 = 0
    if (1 if var18 == 0 else 0):
        break
    var39 = (var18 - 4)
    var40 = ((var18 - 4) if var34 else var18)
    if (1 if ((var18 - 4) if var34 else var18) == 0 else 0):
        break
    var14 = ((var2 << 1) | 1)
    var43 = ((var27 << 1) | 1)
    var23 = (((var2 << 1) | 1) - ((var27 << 1) | 1))
    var17 = ((var3 << 1) | 1)
    var44 = ((var21 << 1) | 1)
    var22 = (((var3 << 1) | 1) - ((var21 << 1) | 1))
    var45 = ((var0 << 1) | 1)
    var25 = (var14 - ((var0 << 1) | 1))
    var46 = ((var1 << 1) | 1)
    var32 = (var17 - ((var1 << 1) | 1))
    var30 = 2147483647
    var27 = 2147483647
    while True:  # loop $label102
        var4 = var20
        var20 = (var20 + 4)
        var12 = ((((var20 + 4) % var18) << 2) + 59200)
        var15 = i32_load(((((var20 + 4) % var18) << 2) + 59200) + 12)
        var21 = (var15 << 2)
        var13 = i32_load(var12 + 4)
        var8 = ((((((3591 & 0xFFFFFFFF) >> i32_load(((((var20 + 4) % var18) << 2) + 59200) + 12)) & 1) + i32_load(((var15 << 2) + 9344))) + i32_load(var12 + 4)) << 1)
        var16 = i32_load(var12)
        var21 = ((i32_load(var12) + (i32_load((var21 + 9264)) + (((37449 & 0xFFFFFFFF) >> var15) & 1))) << 1)
        var12 = (var4 << 2)
        var26 = i32_load((((var4 << 2) | 12) + 59200))
        var29 = (var26 << 2)
        var15 = i32_load((var12 + 59200))
        var41 = ((((((37449 & 0xFFFFFFFF) >> i32_load((((var4 << 2) | 12) + 59200))) & 1) + i32_load(((var26 << 2) + 9264))) + i32_load((var12 + 59200))) << 1)
        var24 = (((i32_load(var12) + (i32_load((var21 + 9264)) + (((37449 & 0xFFFFFFFF) >> var15) & 1))) << 1) - ((((((37449 & 0xFFFFFFFF) >> i32_load((((var4 << 2) | 12) + 59200))) & 1) + i32_load(((var26 << 2) + 9264))) + i32_load((var12 + 59200))) << 1))
        var12 = i32_load(((var12 | 4) + 59200))
        var42 = ((i32_load(((var12 | 4) + 59200)) + (i32_load((var29 + 9344)) + (((3591 & 0xFFFFFFFF) >> var26) & 1))) << 1)
        var26 = (var8 - ((i32_load(((var12 | 4) + 59200)) + (i32_load((var29 + 9344)) + (((3591 & 0xFFFFFFFF) >> var26) & 1))) << 1))
        var29 = (((((((((3591 & 0xFFFFFFFF) >> i32_load(((((var20 + 4) % var18) << 2) + 59200) + 12)) & 1) + i32_load(((var15 << 2) + 9344))) + i32_load(var12 + 4)) << 1) - var17) * (((i32_load(var12) + (i32_load((var21 + 9264)) + (((37449 & 0xFFFFFFFF) >> var15) & 1))) << 1) - ((((((37449 & 0xFFFFFFFF) >> i32_load((((var4 << 2) | 12) + 59200))) & 1) + i32_load(((var26 << 2) + 9264))) + i32_load((var12 + 59200))) << 1))) + ((var8 - ((i32_load(((var12 | 4) + 59200)) + (i32_load((var29 + 9344)) + (((3591 & 0xFFFFFFFF) >> var26) & 1))) << 1)) * (var14 - var21)))
        var35 = (1 if (((((((((3591 & 0xFFFFFFFF) >> i32_load(((((var20 + 4) % var18) << 2) + 59200) + 12)) & 1) + i32_load(((var15 << 2) + 9344))) + i32_load(var12 + 4)) << 1) - var17) * (((i32_load(var12) + (i32_load((var21 + 9264)) + (((37449 & 0xFFFFFFFF) >> var15) & 1))) << 1) - ((((((37449 & 0xFFFFFFFF) >> i32_load((((var4 << 2) | 12) + 59200))) & 1) + i32_load(((var26 << 2) + 9264))) + i32_load((var12 + 59200))) << 1))) + ((var8 - ((i32_load(((var12 | 4) + 59200)) + (i32_load((var29 + 9344)) + (((3591 & 0xFFFFFFFF) >> var26) & 1))) << 1)) * (var14 - var21))) > 0 else 0)
        var38 = (1 if var29 != 0 else 0)
        var29 = (1 if var29 == 0 else 0)
        var47 = (var17 - var8)
        var48 = (var21 - var14)
        var37 = (((var17 - var8) * var25) + ((var21 - var14) * var32))
        var42 = (var17 - var42)
        var41 = (var41 - var14)
        var49 = (((var17 - var42) * var25) + ((var41 - var14) * var32))
        if (1 if (((1 if (((var17 - var8) * var25) + ((var21 - var14) * var32)) != 0 else 0) & ((1 if (((var17 - var42) * var25) + ((var41 - var14) * var32)) <= 0 else 0) ^ (1 if var37 > 0 else 0))) if var49 else (1 if var37 == 0 else 0)) == 0 else 0):
            var37 = (((var8 - var46) * var24) + (var26 * (var45 - var21)))
            if (1 if ((var38 & ((1 if (((var8 - var46) * var24) + (var26 * (var45 - var21))) <= 0 else 0) ^ var35)) if var37 else var29) == 0 else 0):
                break
        var37 = ((var23 * var47) + (var22 * var48))
        var41 = ((var23 * var42) + (var22 * var41))
        if (((1 if ((var23 * var47) + (var22 * var48)) != 0 else 0) & ((1 if ((var23 * var42) + (var22 * var41)) <= 0 else 0) ^ (1 if var37 > 0 else 0))) if var41 else (1 if var37 == 0 else 0)):
            break
        var8 = (((var8 - var44) * var24) + (var26 * (var43 - var21)))
        if ((var38 & ((1 if (((var8 - var44) * var24) + (var26 * (var43 - var21))) <= 0 else 0) ^ var35)) if var8 else var29):
            break
        if (1 if var12 == var13 else 0):
            var8 = (1 if var15 > var16 else 0)
            var13 = (var15 if (1 if var15 > var16 else 0) else var16)
            var21 = (var16 if var8 else var15)
            if (1 if (var16 if var8 else var15) > var0 else 0):
                break
            if (1 if var0 > var13 else 0):
                break
            var8 = (var1 - var12)
            break
        var8 = 0
        if (1 if var15 != var16 else 0):
            break
        var8 = (var0 - var15)
        var8 = ((var0 - var15) * var8)
        var16 = (1 if var12 > var13 else 0)
        var21 = (var12 if (1 if var12 > var13 else 0) else var13)
        var16 = (var13 if var16 else var12)
        if (1 if ((1 if (var12 if (1 if var12 > var13 else 0) else var13) >= var1 else 0) & (1 if var1 >= (var13 if var16 else var12) else 0)) == 0 else 0):
            var26 = (var1 - var13)
            var26 = (((var1 - var13) * var26) + var8)
            var24 = (var1 - var12)
            var8 = (var8 + ((var1 - var12) * var24))
            var8 = ((((var1 - var13) * var26) + var8) if (1 if var8 > var26 else 0) else (var8 + ((var1 - var12) * var24)))
        var15 = (var2 - var15)
        var15 = ((var2 - var15) * var15)
        if ((1 if var3 <= var21 else 0) & (1 if var3 >= var16 else 0)):
            break
        var13 = (var3 - var13)
        var13 = (((var3 - var13) * var13) + var15)
        var12 = (var3 - var12)
        var12 = (var15 + ((var3 - var12) * var12))
        break
        var8 = (var1 - var12)
        var8 = ((var1 - var12) * var8)
        var26 = (var0 - var16)
        var26 = (((var1 - var12) * var8) + ((var0 - var16) * var26))
        var24 = (var0 - var15)
        var8 = (var8 + ((var0 - var15) * var24))
        var8 = ((((var1 - var12) * var8) + ((var0 - var16) * var26)) if (1 if var8 > var26 else 0) else (var8 + ((var0 - var15) * var24)))
        if (1 if var2 < var21 else 0):
            break
        if (1 if var2 > var13 else 0):
            break
        var12 = (var3 - var12)
        break
        var12 = (var3 - var12)
        var12 = ((var3 - var12) * var12)
        var13 = (var2 - var16)
        var13 = (((var3 - var12) * var12) + ((var2 - var16) * var13))
        var15 = (var2 - var15)
        var12 = (var12 + ((var2 - var15) * var15))
        var12 = ((((var3 - var12) * var12) + ((var2 - var16) * var13)) if (1 if var12 > var13 else 0) else (var12 + ((var2 - var15) * var15)))
        var12 = (1 if var12 < var30 else 0)
        var30 = (((((var3 - var12) * var12) + ((var2 - var16) * var13)) if (1 if var12 > var13 else 0) else (var12 + ((var2 - var15) * var15))) if (1 if var12 < var30 else 0) else var30)
        var19 = (var4 if var12 else var19)
        var8 = (1 if var8 < var27 else 0)
        var27 = (var8 if (1 if var8 < var27 else 0) else var27)
        var31 = (var4 if var8 else var31)
        if (1 if var20 < var40 else 0):
            continue
        break  # end loop
    var20 = 0
    if (1 if var30 == 2147483647 else 0):
        break
    var20 = (1 if var19 != var31 else 0)
    if (1 if var19 == var31 else 0):
        break
    if var11:
        break
    var15 = ((var19 << 2) + 59200)
    var12 = i32_load(((var19 << 2) + 59200))
    var16 = i32_load(var15 + 8)
    var4 = i32_load(((((var19 + 4) % var18) << 2) + 59200))
    var22 = ((var31 + 4) % var18)
    var8 = i32_load(((((var31 + 4) % var18) << 2) + 59200))
    var14 = ((var31 << 2) + 59200)
    var11 = i32_load(((var31 << 2) + 59200))
    var20 = 0
    var13 = i32_load(var15 + 4)
    var15 = i32_load(((((var19 + 5) % var18) << 2) + 59200))
    if (1 if i32_load(var15 + 4) == i32_load(((((var19 + 5) % var18) << 2) + 59200)) else 0):
        if (1 if (var4 if (1 if var4 < var12 else 0) else var12) > var2 else 0):
            break
        if (1 if (var12 if (1 if var4 < var12 else 0) else var4) < var2 else 0):
            break
        var2 = (var2 - var12)
        var2 = (var2 >> 31)
        break
        if (1 if var4 >= var12 else 0):
            break
        if (1 if var2 >= var4 else 0):
            break
        break
        break
    if (1 if var4 != var12 else 0):
        break
    if (1 if (var15 if (1 if var13 > var15 else 0) else var13) > var3 else 0):
        break
    if (1 if (var13 if (1 if var13 > var15 else 0) else var15) < var3 else 0):
        break
    var2 = (var3 - var13)
    var2 = (var2 >> 31)
    break
    if (1 if var13 <= var15 else 0):
        break
    if (1 if var3 >= var15 else 0):
        break
    break
    var4 = ((((var15 - var13) if (1 if var3 > var15 else 0) else 0) if (1 if var13 < var15 else 0) else 0) + var16)
    var3 = i32_load(var14 + 4)
    var2 = i32_load(((((var31 + 5) % var18) << 2) + 59200))
    if (1 if i32_load(var14 + 4) == i32_load(((((var31 + 5) % var18) << 2) + 59200)) else 0):
        if (1 if (var8 if (1 if var8 < var11 else 0) else var11) > var0 else 0):
            break
        if (1 if (var11 if (1 if var8 < var11 else 0) else var8) < var0 else 0):
            break
        var2 = (var0 - var11)
        var2 = (var2 >> 31)
        break
        if (1 if var8 >= var11 else 0):
            break
        if (1 if var0 >= var8 else 0):
            break
        break
        break
    if (1 if var8 != var11 else 0):
        break
    if (1 if (var2 if (1 if var2 < var3 else 0) else var3) > var1 else 0):
        break
    if (1 if (var3 if (1 if var2 < var3 else 0) else var2) < var1 else 0):
        break
    var2 = (var1 - var3)
    var2 = (var2 >> 31)
    break
    if (1 if var2 >= var3 else 0):
        break
    if (1 if var1 >= var2 else 0):
        break
    break
    var2 = ((((var2 - var3) if (1 if var1 > var2 else 0) else 0) if (1 if var2 > var3 else 0) else 0) + i32_load(((var31 << 2) + 59208)))
    var2 = (var2 - var4)
    var3 = ((((var1 - var3) ^ (var2 >> 31)) - var2) if (1 if (var2 - var4) < 0 else 0) else ((1 if (var3 - var2) != ((((var2 - var3) if (1 if var1 > var2 else 0) else 0) if (1 if var2 > var3 else 0) else 0) + i32_load(((var31 << 2) + 59208))) else 0) << 2))
    var3 = (var2 >> 31)
    var2 = ((var2 ^ (var2 >> 31)) - var3)
    var2 = (var33 - var2)
    var2 = (var2 >> 31)
    var15 = (((((var1 - var3) ^ (var2 >> 31)) - var2) if (1 if (var2 - var4) < 0 else 0) else ((1 if (var3 - var2) != ((((var2 - var3) if (1 if var1 > var2 else 0) else 0) if (1 if var2 > var3 else 0) else 0) + i32_load(((var31 << 2) + 59208))) else 0) << 2)) if var34 else (var3 if (1 if ((var2 ^ (var2 >> 31)) - var3) < (((var33 - var2) ^ (var2 >> 31)) - var2) else 0) else (0 - var3)))
    if (1 if (((((var1 - var3) ^ (var2 >> 31)) - var2) if (1 if (var2 - var4) < 0 else 0) else ((1 if (var3 - var2) != ((((var2 - var3) if (1 if var1 > var2 else 0) else 0) if (1 if var2 > var3 else 0) else 0) + i32_load(((var31 << 2) + 59208))) else 0) << 2)) if var34 else (var3 if (1 if ((var2 ^ (var2 >> 31)) - var3) < (((var33 - var2) ^ (var2 >> 31)) - var2) else 0) else (0 - var3))) == 0 else 0):
        break
    while True:  # loop $label119
        var2 = ((var19 << 2) + 59200)
        var3 = i32_load(((var19 << 2) + 59200) + 12)
        if (1 if i32_load(((var19 << 2) + 59200) + 12) > 8 else 0):
            break
        var4 = (var12 - var0)
        var4 = (var4 >> 31)
        var4 = (((var12 - var0) ^ (var4 >> 31)) - var4)
        var2 = i32_load(var2 + 4)
        var8 = (i32_load(var2 + 4) - var1)
        var8 = (var8 >> 31)
        var8 = (((i32_load(var2 + 4) - var1) ^ (var8 >> 31)) - var8)
        if (1 if ((((var12 - var0) ^ (var4 >> 31)) - var4) if (1 if var4 > var8 else 0) else (((i32_load(var2 + 4) - var1) ^ (var8 >> 31)) - var8)) < 56 else 0):
            break
        if (1 if var19 == var31 else 0):
            break
        if (1 if var19 == var22 else 0):
            break
        var4 = (var19 - var31)
        var4 = (var4 >> 31)
        var4 = (((var19 - var31) ^ (var4 >> 31)) - var4)
        if (1 if (((var19 - var31) ^ (var4 >> 31)) - var4) == 4 else 0):
            break
        if (1 if var4 != var39 else 0):
            break
        var20 = ((var0 << 8) | 128)
        var4 = (var3 << 2)
        var25 = i32_load(((var3 << 2) + 9264))
        var30 = (i32_load(((var3 << 2) + 9264)) + (((((37449 & 0xFFFFFFFF) >> var3) & 1) + var12) << 8))
        var21 = (((var0 << 8) | 128) - (i32_load(((var3 << 2) + 9264)) + (((((37449 & 0xFFFFFFFF) >> var3) & 1) + var12) << 8)))
        var13 = ((var1 << 8) | 128)
        var33 = i32_load((var4 + 9344))
        var32 = (i32_load((var4 + 9344)) + (((((3591 & 0xFFFFFFFF) >> var3) & 1) + var2) << 8))
        var27 = (((var1 << 8) | 128) - (i32_load((var4 + 9344)) + (((((3591 & 0xFFFFFFFF) >> var3) & 1) + var2) << 8)))
        var3 = (var19 - var15)
        var26 = ((var18 if (1 if var3 < 0 else 0) else (0 - (var18 if (1 if (var19 - var15) >= var18 else 0) else 0))) + var3)
        var4 = ((var18 if (1 if var3 < 0 else 0) else (0 - (var18 if (1 if (var19 - var15) >= var18 else 0) else 0))) + var3)
        var8 = i32_load(((((var18 if (1 if var3 < 0 else 0) else (0 - (var18 if (1 if (var19 - var15) >= var18 else 0) else 0))) + var3) << 2) + 59200))
        while True:  # loop $label115
            var3 = (var4 + var15)
            var3 = ((var18 if (1 if var3 < 0 else 0) else (0 - (var18 if (1 if (var4 + var15) >= var18 else 0) else 0))) + var3)
            var11 = ((((var18 if (1 if var3 < 0 else 0) else (0 - (var18 if (1 if (var4 + var15) >= var18 else 0) else 0))) + var3) << 2) + 59200)
            var14 = i32_load(((((var18 if (1 if var3 < 0 else 0) else (0 - (var18 if (1 if (var4 + var15) >= var18 else 0) else 0))) + var3) << 2) + 59200) + 12)
            var17 = (var14 << 2)
            var16 = ((((((3591 & 0xFFFFFFFF) >> i32_load(((((var18 if (1 if var3 < 0 else 0) else (0 - (var18 if (1 if (var4 + var15) >= var18 else 0) else 0))) + var3) << 2) + 59200) + 12)) & 1) + i32_load(((var14 << 2) + 9344))) + i32_load(var11 + 4)) << 8)
            var11 = i32_load(var11)
            var14 = ((i32_load(var11) + (i32_load((var17 + 9264)) + (((37449 & 0xFFFFFFFF) >> var14) & 1))) << 8)
            var17 = (((var13 - ((((((3591 & 0xFFFFFFFF) >> i32_load(((((var18 if (1 if var3 < 0 else 0) else (0 - (var18 if (1 if (var4 + var15) >= var18 else 0) else 0))) + var3) << 2) + 59200) + 12)) & 1) + i32_load(((var14 << 2) + 9344))) + i32_load(var11 + 4)) << 8)) * var21) + ((((i32_load(var11) + (i32_load((var17 + 9264)) + (((37449 & 0xFFFFFFFF) >> var14) & 1))) << 8) - var20) * var27))
            var24 = ((var4 << 2) + 59200)
            var23 = i32_load(((var4 << 2) + 59200) + 12)
            var29 = (var23 << 2)
            var24 = ((((((3591 & 0xFFFFFFFF) >> i32_load(((var4 << 2) + 59200) + 12)) & 1) + i32_load(((var23 << 2) + 9344))) + i32_load(var24 + 4)) << 8)
            var8 = (((i32_load((var29 + 9264)) + (((37449 & 0xFFFFFFFF) >> var23) & 1)) + var8) << 8)
            var23 = (((var13 - ((((((3591 & 0xFFFFFFFF) >> i32_load(((var4 << 2) + 59200) + 12)) & 1) + i32_load(((var23 << 2) + 9344))) + i32_load(var24 + 4)) << 8)) * var21) + (((((i32_load((var29 + 9264)) + (((37449 & 0xFFFFFFFF) >> var23) & 1)) + var8) << 8) - var20) * var27))
            var17 = (var14 - var8)
            var23 = (var16 - var24)
            var8 = (((var14 - var8) * (var16 - var13)) + ((var16 - var24) * (var20 - var14)))
            var16 = (((var16 - var32) * var17) + (var23 * (var30 - var14)))
            var16 = ((((1 if (((var13 - ((((((3591 & 0xFFFFFFFF) >> i32_load(((((var18 if (1 if var3 < 0 else 0) else (0 - (var18 if (1 if (var4 + var15) >= var18 else 0) else 0))) + var3) << 2) + 59200) + 12)) & 1) + i32_load(((var14 << 2) + 9344))) + i32_load(var11 + 4)) << 8)) * var21) + ((((i32_load(var11) + (i32_load((var17 + 9264)) + (((37449 & 0xFFFFFFFF) >> var14) & 1))) << 8) - var20) * var27)) != 0 else 0) & ((1 if (((var13 - ((((((3591 & 0xFFFFFFFF) >> i32_load(((var4 << 2) + 59200) + 12)) & 1) + i32_load(((var23 << 2) + 9344))) + i32_load(var24 + 4)) << 8)) * var21) + (((((i32_load((var29 + 9264)) + (((37449 & 0xFFFFFFFF) >> var23) & 1)) + var8) << 8) - var20) * var27)) <= 0 else 0) ^ (1 if var17 > 0 else 0))) if var23 else (1 if var17 == 0 else 0)) | (((1 if (((var14 - var8) * (var16 - var13)) + ((var16 - var24) * (var20 - var14))) != 0 else 0) & ((1 if (((var16 - var32) * var17) + (var23 * (var30 - var14))) <= 0 else 0) ^ (1 if var8 > 0 else 0))) if var16 else (1 if var8 == 0 else 0)))
            if (1 if ((((1 if (((var13 - ((((((3591 & 0xFFFFFFFF) >> i32_load(((((var18 if (1 if var3 < 0 else 0) else (0 - (var18 if (1 if (var4 + var15) >= var18 else 0) else 0))) + var3) << 2) + 59200) + 12)) & 1) + i32_load(((var14 << 2) + 9344))) + i32_load(var11 + 4)) << 8)) * var21) + ((((i32_load(var11) + (i32_load((var17 + 9264)) + (((37449 & 0xFFFFFFFF) >> var14) & 1))) << 8) - var20) * var27)) != 0 else 0) & ((1 if (((var13 - ((((((3591 & 0xFFFFFFFF) >> i32_load(((var4 << 2) + 59200) + 12)) & 1) + i32_load(((var23 << 2) + 9344))) + i32_load(var24 + 4)) << 8)) * var21) + (((((i32_load((var29 + 9264)) + (((37449 & 0xFFFFFFFF) >> var23) & 1)) + var8) << 8) - var20) * var27)) <= 0 else 0) ^ (1 if var17 > 0 else 0))) if var23 else (1 if var17 == 0 else 0)) | (((1 if (((var14 - var8) * (var16 - var13)) + ((var16 - var24) * (var20 - var14))) != 0 else 0) & ((1 if (((var16 - var32) * var17) + (var23 * (var30 - var14))) <= 0 else 0) ^ (1 if var8 > 0 else 0))) if var16 else (1 if var8 == 0 else 0))) == 1 else 0):
                var14 = (1 if var4 != var31 else 0)
                var8 = var11
                var4 = var3
                if var14:
                    continue
            break  # end loop
        if (var16 ^ 1):
            break
        if ((1 if var19 == 0 else 0) & var34):
            var8 = var12
            var12 = var2
            break
        var3 = ((var26 << 2) + 59200)
        var4 = i32_load(((var26 << 2) + 59200))
        var8 = ((-1 if (1 if var4 < var12 else 0) else (1 if i32_load(((var26 << 2) + 59200)) != var12 else 0)) + var12)
        var3 = i32_load(var3 + 4)
        var12 = ((-1 if (1 if var2 > var3 else 0) else (1 if i32_load(var3 + 4) != var2 else 0)) + var2)
        i32_store8(var10, (((((-1 if (1 if var4 < var12 else 0) else (1 if i32_load(((var26 << 2) + 59200)) != var12 else 0)) + var12) - (var12 + var25)) + ((((-1 if (1 if var2 > var3 else 0) else (1 if i32_load(var3 + 4) != var2 else 0)) + var2) - (var2 + var33)) * 3)) + 4))
        i32_store(var9, ((var12 << 16) + var8))
        if (1 if var0 != var8 else 0):
            break
        if (1 if var1 != var12 else 0):
            break
        i32_store(var9, 0)
        break
        if (1 if var19 == var31 else 0):
            var20 = 0
            break
        else:
            var2 = (((var19 if var19 else var18) if (1 if var15 < 0 else 0) else var19) + var15)
            var19 = ((((var19 if var19 else var18) if (1 if var15 < 0 else 0) else var19) + var15) if (1 if var2 != var18 else 0) else 0)
            var12 = i32_load(((((((var19 if var19 else var18) if (1 if var15 < 0 else 0) else var19) + var15) if (1 if var2 != var18 else 0) else 0) << 2) + 59200))
            continue
        raise RuntimeError('unreachable')
        break  # end loop
    var20 = 1
    global global0
    global0 = (var36 + 16)
    return var20

