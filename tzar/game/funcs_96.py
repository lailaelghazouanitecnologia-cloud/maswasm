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
# $func61
# ==========================================================
def func61(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9):
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
    var23 = i32_load(i32_load(9142424) + 64)
    if (1 if var0 == 3 else 0):
        if i32_load8_u(9216060):
            break
    var10 = i32_load(9142440)
    var18 = ((((i32_load(9142440) & 0xFFFFFFFF) >> 1) - 20) if var23 else var10)
    var26 = (((((((i32_load(9142440) & 0xFFFFFFFF) >> 1) - 20) if var23 else var10) * (var1 * var18)) // 65536) if (1 if var2 == 1 else 0) else var1)
    if (1 if (((((((i32_load(9142440) & 0xFFFFFFFF) >> 1) - 20) if var23 else var10) * (var1 * var18)) // 65536) if (1 if var2 == 1 else 0) else var1) == 0 else 0):
        break
    var38 = float(var18)
    var27 = (1 if var7 != 2147483647 else 0)
    while True:  # loop $label18
        var1 = i32_load(9147320)
        var2 = i32_load(9147312)
        i32_store(9147320, i32_load(9147312))
        var11 = i32_load(9147316)
        i32_store(9147316, var2)
        var10 = (var1 ^ (var1 << 11))
        var1 = i32_load(9147324)
        var1 = ((i32_load(9147324) << 11) ^ var1)
        var1 = ((var2 ^ (((var2 & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var1) & 0xFFFFFFFF) >> 8))) ^ var1)
        var10 = ((((((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((((var2 ^ (((var2 & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var1) & 0xFFFFFFFF) >> 8))) ^ var1) & 0xFFFFFFFF) >> 19)) ^ var10) ^ var1)
        if (1 if var8 == 0 else 0):
            var14 = ((var2 << 11) ^ var2)
            var2 = ((var11 << 11) ^ var11)
            var2 = (((((((var11 << 11) ^ var11) & 0xFFFFFFFF) >> 8) ^ ((var10 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var10)
            var11 = (((((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8) ^ (((((((((var11 << 11) ^ var11) & 0xFFFFFFFF) >> 8) ^ ((var10 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var10) & 0xFFFFFFFF) >> 19)) ^ var14) ^ var2)
            var13 = ((((((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8) ^ (((((((((var11 << 11) ^ var11) & 0xFFFFFFFF) >> 8) ^ ((var10 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var10) & 0xFFFFFFFF) >> 19)) ^ var14) ^ var2) % var18)
            var12 = (var2 % var18)
            var19 = ((var10 % 7) - 3)
            break
        i32_store(9147324, var2)
        var1 = ((var1 << 11) ^ var1)
        var2 = ((var2 << 11) ^ var2)
        var11 = ((var11 << 11) ^ var11)
        var14 = (((((((var11 << 11) ^ var11) & 0xFFFFFFFF) >> 8) ^ ((var10 & 0xFFFFFFFF) >> 19)) ^ var11) ^ var10)
        var2 = (((((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8) ^ (((((((((var11 << 11) ^ var11) & 0xFFFFFFFF) >> 8) ^ ((var10 & 0xFFFFFFFF) >> 19)) ^ var11) ^ var10) & 0xFFFFFFFF) >> 19)) ^ var2) ^ var14)
        var11 = (((((((var1 << 11) ^ var1) & 0xFFFFFFFF) >> 8) ^ (((((((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8) ^ (((((((((var11 << 11) ^ var11) & 0xFFFFFFFF) >> 8) ^ ((var10 & 0xFFFFFFFF) >> 19)) ^ var11) ^ var10) & 0xFFFFFFFF) >> 19)) ^ var2) ^ var14) & 0xFFFFFFFF) >> 19)) ^ var1) ^ var2)
        var19 = ((((((((var1 << 11) ^ var1) & 0xFFFFFFFF) >> 8) ^ (((((((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8) ^ (((((((((var11 << 11) ^ var11) & 0xFFFFFFFF) >> 8) ^ ((var10 & 0xFFFFFFFF) >> 19)) ^ var11) ^ var10) & 0xFFFFFFFF) >> 19)) ^ var2) ^ var14) & 0xFFFFFFFF) >> 19)) ^ var1) ^ var2) & 3)
        var1 = (var14 % var18)
        var12 = (var1 & 1)
        var13 = (0 if (var1 & 1) else (var14 % var18))
        var12 = ((0 - var12) & var1)
        var1 = var10
        var10 = var14
        var20 = (var2 & 3)
        var1 = ((var1 << 11) ^ var1)
        var1 = (((((var11 & 0xFFFFFFFF) >> 19) ^ ((((var1 << 11) ^ var1) & 0xFFFFFFFF) >> 8)) ^ var11) ^ var1)
        var15 = ((((((var11 & 0xFFFFFFFF) >> 19) ^ ((((var1 << 11) ^ var1) & 0xFFFFFFFF) >> 8)) ^ var11) ^ var1) % var3)
        if var27:
            var14 = var11
            var11 = var2
            var2 = var10
            break
        var14 = var1
        var1 = ((var10 << 11) ^ var10)
        var1 = (var1 ^ ((((((var10 << 11) ^ var10) & 0xFFFFFFFF) >> 8) ^ ((var14 & 0xFFFFFFFF) >> 19)) ^ var1))
        var24 = (((var1 ^ ((((((var10 << 11) ^ var10) & 0xFFFFFFFF) >> 8) ^ ((var14 & 0xFFFFFFFF) >> 19)) ^ var1)) % 3) + 1)
        i32_store(9147320, var14)
        i32_store(9147324, var11)
        i32_store(9147316, var1)
        var2 = ((var2 << 11) ^ var2)
        var1 = ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ ((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8))) ^ var2)
        i32_store(9147312, ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ ((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8))) ^ var2))
        var28 = ((var1 % var4) + var6)
        if ((var1 % var4) + var6):
            var14 = (var5 + var15)
            var21 = ((var5 + var15) << 1)
            var25 = (var14 * var14)
            var22 = 0
            while True:  # loop $label17
                var13 = (var13 + var19)
                var12 = (var12 + var20)
                var1 = i32_load(9142440)
                if (1 if var9 == 0 else 0):
                    if (1 if var1 <= var13 else 0):
                        break
                    if (1 if (var12 | var13) < 0 else 0):
                        break
                    if (1 if var1 <= var12 else 0):
                        break
                    if (var22 % var24):
                        break
                    var1 = i32_load(9147324)
                    i32_store(9147324, i32_load(9147316))
                    var2 = i32_load(9147320)
                    var10 = i32_load(9147312)
                    i32_store(9147320, i32_load(9147312))
                    var1 = (var1 ^ (var1 << 11))
                    var1 = ((var10 ^ (((var10 & 0xFFFFFFFF) >> 19) ^ (((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8))) ^ var1)
                    i32_store(9147316, ((var10 ^ (((var10 & 0xFFFFFFFF) >> 19) ^ (((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8))) ^ var1))
                    var2 = (var2 ^ (var2 << 11))
                    var2 = ((((((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var1)
                    i32_store(9147312, ((((((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var1))
                    var19 = ((var2 % 7) - 3)
                    var20 = ((var1 % 7) - 3)
                    break
                if (1 if var1 <= var12 else 0):
                    var12 = (var12 % var1)
                    break
                if (1 if var12 >= 0 else 0):
                    break
                var12 = (var1 - (var12 % var1))
                if (1 if var1 <= var13 else 0):
                    var13 = (var13 % var1)
                    break
                if (1 if var13 >= 0 else 0):
                    break
                var13 = (var1 - (var13 % var1))
                if (var22 % var24):
                    break
                var1 = i32_load(9147324)
                i32_store(9147324, i32_load(9147316))
                var2 = i32_load(9147320)
                var10 = i32_load(9147312)
                i32_store(9147320, i32_load(9147312))
                var1 = (var1 ^ (var1 << 11))
                var1 = ((var10 ^ (((var10 & 0xFFFFFFFF) >> 19) ^ (((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8))) ^ var1)
                i32_store(9147316, ((var10 ^ (((var10 & 0xFFFFFFFF) >> 19) ^ (((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8))) ^ var1))
                var2 = (var2 ^ (var2 << 11))
                var2 = ((((((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var1)
                i32_store(9147312, ((((((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var1))
                var2 = ((var19 + (var2 % 3)) - 1)
                var2 = (-3 if (1 if var2 <= -3 else 0) else ((var19 + (var2 % 3)) - 1))
                var19 = (3 if (1 if var2 >= 3 else 0) else (-3 if (1 if var2 <= -3 else 0) else ((var19 + (var2 % 3)) - 1)))
                var1 = ((var20 + (var1 % 3)) - 1)
                var1 = (-3 if (1 if var1 <= -3 else 0) else ((var20 + (var1 % 3)) - 1))
                var20 = (3 if (1 if var1 >= 3 else 0) else (-3 if (1 if var1 <= -3 else 0) else ((var20 + (var1 % 3)) - 1)))
                if var23:
                    var1 = i32_load(9142416)
                    var2 = i32_load(9142416)
                    if (1 if var1 == 0 else 0):
                        var2 = (i32_load(41092) if i32_load8_u(9147210) else (i32_load(9142892) - 1))
                    var33 = func262(float(var13), float(var12))
                    var36 = f32(math.sqrt(float(((var13 * var13) + (var12 * var12)))))
                    if (1 if f32(math.sqrt(float(((var13 * var13) + (var12 * var12))))) >= var38 else 0):
                        break
                    var35 = f32(var33)
                    if (1 if f32(var33) < 0.0 else 0):
                        break
                    var37 = (6.28318548 / float((4 if (1 if var2 < 3 else 0) else (var2 << (var2 & 1)))))
                    if (1 if (6.28318548 / float((4 if (1 if var2 < 3 else 0) else (var2 << (var2 & 1))))) < var35 else 0):
                        break
                    var39 = (var37 - var35)
                    var15 = 0
                    while True:  # loop $label13
                        var2 = var1
                        if (1 if var1 == 0 else 0):
                            var2 = (i32_load(41092) if i32_load8_u(9147210) else (i32_load(9142892) - 1))
                        if (1 if var15 >= (4 if (1 if var2 < 3 else 0) else (var2 << (var2 & 1))) else 0):
                            break
                        var40 = ((var37 * float(var15)) + (var39 if (var15 & 1) else var35))
                        var2 = i32_load(9142440)
                        # Unknown: f64.convert_i32_u []
                        var33 = ((i32_load(9142440) & 0xFFFFFFFF) >> 1)
                        var34 = ((float((func49(((var37 * float(var15)) + (var39 if (var15 & 1) else var35))) * var36)) + 0.5) + ((i32_load(9142440) & 0xFFFFFFFF) >> 1))
                        if (1 if abs(((float((func49(((var37 * float(var15)) + (var39 if (var15 & 1) else var35))) * var36)) + 0.5) + ((i32_load(9142440) & 0xFFFFFFFF) >> 1))) < 2147483648.0 else 0):
                            break
                        var16 = -2147483648
                        var33 = ((float((func48(var40) * var36)) + 0.5) + var33)
                        if (1 if abs(((float((func48(var40) * var36)) + 0.5) + var33)) < 2147483648.0 else 0):
                            break
                        var17 = -2147483648
                        if (1 if int(var33) <= -2147483648 else 0):
                            break
                        if (1 if var2 <= var16 else 0):
                            break
                        if (1 if (var16 | var17) < 0 else 0):
                            break
                        var11 = (var16 - var14)
                        var29 = (var16 + var21)
                        if (1 if (var16 - var14) >= (var16 + var21) else 0):
                            break
                        var10 = (var17 - var14)
                        var30 = (var17 + var21)
                        if (1 if (var17 - var14) >= (var17 + var21) else 0):
                            break
                        while True:  # loop $label12
                            var1 = (var11 - var16)
                            var31 = (((var11 - var16) * var1) - 1)
                            var2 = var10
                            while True:  # loop $label11
                                var1 = (var2 - var17)
                                if (1 if (var31 + ((var2 - var17) * var1)) > var25 else 0):
                                    break
                                var1 = i32_load(9142440)
                                if (1 if i32_load(9142440) <= var2 else 0):
                                    break
                                if (1 if (var2 | var11) < 0 else 0):
                                    break
                                if (1 if var1 <= var11 else 0):
                                    break
                                i32_store8((i32_load(9147288) + ((var1 * var2) + var11)), var0)
                                var2 = (var2 + 1)
                                if (1 if (var2 + 1) != var30 else 0):
                                    continue
                                break  # end loop
                            var11 = (var11 + 1)
                            if (1 if (var11 + 1) != var29 else 0):
                                continue
                            break  # end loop
                        var1 = i32_load(9142416)
                        var15 = (var15 + 1)
                        continue
                        break  # end loop
                    raise RuntimeError('unreachable')
                var11 = (var12 - var14)
                var15 = (var12 + var21)
                if (1 if (var12 - var14) >= (var12 + var21) else 0):
                    break
                var1 = (var13 - var14)
                var16 = (var13 + var21)
                if (1 if (var13 - var14) >= (var13 + var21) else 0):
                    break
                while True:  # loop $label16
                    var2 = (var11 - var12)
                    var17 = (((var11 - var12) * var2) - 1)
                    var2 = var1
                    while True:  # loop $label15
                        var10 = (var2 - var13)
                        if (1 if (var17 + ((var2 - var13) * var10)) > var25 else 0):
                            break
                        var10 = i32_load(9142440)
                        if (1 if i32_load(9142440) <= var2 else 0):
                            break
                        if (1 if (var2 | var11) < 0 else 0):
                            break
                        if (1 if var10 <= var11 else 0):
                            break
                        i32_store8((i32_load(9147288) + ((var2 * var10) + var11)), var0)
                        var2 = (var2 + 1)
                        if (1 if (var2 + 1) != var16 else 0):
                            continue
                        break  # end loop
                    var11 = (var11 + 1)
                    if (1 if (var11 + 1) != var15 else 0):
                        continue
                    break  # end loop
                var22 = (var22 + 1)
                if (1 if (var22 + 1) < var28 else 0):
                    continue
                break  # end loop
        var32 = (var32 + 1)
        if (1 if (var32 + 1) != var26 else 0):
            continue
        break  # end loop
    return var2

