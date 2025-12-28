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
# $func350
# ==========================================================
def func350():
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
    var44 = 0
    var0 = i32_load(9142440)
    if i32_load(9142440):
        var4 = i32_load(9147288)
        var16 = var0
        while True:  # loop $label2
            var2 = (var1 + 1)
            var3 = i32_load(9142840)
            var6 = i32_load(9140332)
            var0 = 0
            while True:  # loop $label1
                var5 = i32_load8_s((var4 + ((var0 * var16) + var1)))
                if (1 if i32_load8_s((var4 + ((var0 * var16) + var1))) < 0 else 0):
                    break
                if (1 if i32_load(i32_load((var6 + ((var5 & 255) << 2))) + 32) != 23 else 0):
                    break
                var5 = (var0 + 1)
                i32_store((var3 + ((((var0 + 1) * (var16 + 2)) + var2) << 2)), 1)
                var16 = (i32_load(9142440) + 2)
                i32_store((var3 + ((((var5 + (i32_load(9142440) + 2)) * var16) + var2) << 2)), 1)
                var16 = i32_load(9142440)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) < var16 else 0):
                    continue
                break  # end loop
            var1 = var2
            if (1 if var2 < var16 else 0):
                continue
            break  # end loop
    var11 = i32_load(9142424)
    var0 = i32_load(i32_load(9142424) + 164)
    if (1 if i32_load(i32_load(9142424) + 164) == 0 else 0):
        i32_store(var11 + 164, 100)
        var0 = 100
    var1 = ((i32_load(38448) * 404) + 9568096)
    i32_store(((i32_load(38448) * 404) + 9568096) + 104, var0)
    i32_store(var1 + 108, i32_load(var11 + 164))
    var17 = (var16 * var16)
    var15 = i32_load(var11 + 116)
    if i32_load(var11 + 68):
        var0 = i32_load(9142892)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var1 = (var0 - 1)
        var4 = ((var0 - 1) & 3)
        var3 = 0
        var6 = i32_load(9561692)
        if (1 if (var0 - 2) < 3 else 0):
            var2 = 1
            break
        var5 = (var1 & -4)
        var2 = 1
        while True:  # loop $label5
            var1 = (var6 + (var2 * 286704))
            var7 = i32_load(((var6 + (var2 * 286704)) + 1144720))
            var8 = i32_load((var1 + 858016))
            var10 = i32_load((var1 + 571312))
            var1 = i32_load(var1 + 284608)
            var1 = (i32_load(var1 + 284608) if (1 if var1 > var12 else 0) else var12)
            var1 = (i32_load((var1 + 571312)) if (1 if var1 < var10 else 0) else (i32_load(var1 + 284608) if (1 if var1 > var12 else 0) else var12))
            var1 = (i32_load((var1 + 858016)) if (1 if var1 < var8 else 0) else (i32_load((var1 + 571312)) if (1 if var1 < var10 else 0) else (i32_load(var1 + 284608) if (1 if var1 > var12 else 0) else var12)))
            var12 = (i32_load(((var6 + (var2 * 286704)) + 1144720)) if (1 if var1 < var7 else 0) else (i32_load((var1 + 858016)) if (1 if var1 < var8 else 0) else (i32_load((var1 + 571312)) if (1 if var1 < var10 else 0) else (i32_load(var1 + 284608) if (1 if var1 > var12 else 0) else var12))))
            var2 = (var2 + 4)
            var9 = (var9 + 4)
            if (1 if (var9 + 4) != var5 else 0):
                continue
            break  # end loop
        break
    if i32_load(var11 + 64):
        var7 = 1
        var33 = float((((var16 & 0xFFFFFFFF) >> 1) - 37))
        var34 = ((float((((var16 & 0xFFFFFFFF) >> 1) - 37)) * 3.14159274) * var33)
        var1 = i32_load(9142416)
        var0 = i32_load(9142892)
        var2 = (i32_load(9142892) - 1)
        var1 = (i32_load(9142416) if var1 else (i32_load(41092) if i32_load8_u(9147210) else (i32_load(9142892) - 1)))
        var37 = float((4 if (1 if var1 < 3 else 0) else ((i32_load(9142416) if var1 else (i32_load(41092) if i32_load8_u(9147210) else (i32_load(9142892) - 1))) << (var1 & 1))))
        var33 = (var33 + -15.0)
        var36 = (6.28318548 / float(var2))
        var38 = ((6.28318548 / float(var2)) * 0.5)
        var9 = i32_load8_u(9147127)
        if (1 if var0 < 2 else 0):
            break
        var2 = i32_load(9561692)
        var6 = i32_load(9561692)
        var11 = 1
        while True:  # loop $label14
            if var9:
                if (1 if i32_load((var6 + (var11 * 286704)) + 284608) != 1 else 0):
                    break
            var35 = ((var36 * float((var7 - 1))) + var38)
            var39 = float(((i32_load(9142440) & 0xFFFFFFFF) >> 1))
            var40 = ((var33 * func48(((var36 * float((var7 - 1))) + var38))) + float(((i32_load(9142440) & 0xFFFFFFFF) >> 1)))
            if (1 if abs(((var33 * func48(((var36 * float((var7 - 1))) + var38))) + float(((i32_load(9142440) & 0xFFFFFFFF) >> 1)))) < 2147483650.0 else 0):
                break
            var4 = -2147483648
            var35 = ((var33 * func49(var35)) + var39)
            if (1 if abs(((var33 * func49(var35)) + var39)) < 2147483650.0 else 0):
                break
            var12 = -2147483648
            var1 = (-2147483648 - 25)
            var8 = (var12 + 50)
            if (1 if (-2147483648 - 25) >= (var12 + 50) else 0):
                break
            var3 = (var4 - 25)
            var10 = (var4 + 50)
            if (1 if (var4 - 25) >= (var4 + 50) else 0):
                break
            while True:  # loop $label13
                var2 = (var1 + 1)
                var0 = (var1 - var12)
                var13 = (((var1 - var12) * var0) - 1)
                var0 = var3
                while True:  # loop $label12
                    var5 = (var0 - var4)
                    if (1 if (var13 + ((var0 - var4) * var5)) > 625 else 0):
                        break
                    var5 = i32_load(9142440)
                    if (1 if i32_load(9142440) <= var0 else 0):
                        break
                    if (1 if (var0 | var1) < 0 else 0):
                        break
                    if (1 if var1 >= var5 else 0):
                        break
                    var5 = (i32_load(9147288) + ((var0 * var5) + var1))
                    var17 = i32_load8_s((i32_load(9147288) + ((var0 * var5) + var1)))
                    if (1 if i32_load8_s((i32_load(9147288) + ((var0 * var5) + var1))) < 0 else 0):
                        break
                    if (1 if i32_load(i32_load((i32_load(9140332) + ((var17 & 255) << 2))) + 32) != 23 else 0):
                        break
                    i32_store8(var5, i32_load(9147292))
                    var5 = i32_load(9142840)
                    var17 = (var0 + 1)
                    i32_store((i32_load(9142840) + ((((var0 + 1) * (i32_load(9142440) + 2)) + var2) << 2)), 0)
                    var15 = (i32_load(9142440) + 2)
                    i32_store((var5 + ((((var17 + (i32_load(9142440) + 2)) * var15) + var2) << 2)), 0)
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var10 else 0):
                        continue
                    break  # end loop
                var1 = var2
                if (1 if var2 != var8 else 0):
                    continue
                break  # end loop
            var2 = i32_load(9561692)
            var7 = (var7 + 1)
            var0 = (var6 + (var11 * 286704))
            i32_store((var6 + (var11 * 286704)) + 283900, var4)
            i32_store(var0 + 283896, var12)
            i32_store(var0 + 283876, var4)
            i32_store(var0 + 283872, var12)
            var0 = i32_load(9142892)
            var6 = var2
            var11 = (var11 + 1)
            if (1 if (var11 + 1) < var0 else 0):
                continue
            break  # end loop
        break
    var20 = i32_load(var11 + 168)
    if (1 if i32_load(var11 + 168) == 0 else 0):
        break
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var0 = (var2 - 1)
    var4 = ((var2 - 1) & 3)
    var3 = 0
    var6 = i32_load(9561692)
    if (1 if (var2 - 2) < 3 else 0):
        var0 = 1
        break
    var12 = (var0 & -4)
    var0 = 1
    while True:  # loop $label18
        var1 = (var6 + (var0 * 286704))
        var9 = i32_load(((var6 + (var0 * 286704)) + 1144720))
        var5 = i32_load((var1 + 858016))
        var11 = i32_load((var1 + 571312))
        var1 = i32_load(var1 + 284608)
        var1 = (i32_load(var1 + 284608) if (1 if var1 > var8 else 0) else var8)
        var1 = (i32_load((var1 + 571312)) if (1 if var1 < var11 else 0) else (i32_load(var1 + 284608) if (1 if var1 > var8 else 0) else var8))
        var1 = (i32_load((var1 + 858016)) if (1 if var1 < var5 else 0) else (i32_load((var1 + 571312)) if (1 if var1 < var11 else 0) else (i32_load(var1 + 284608) if (1 if var1 > var8 else 0) else var8)))
        var8 = (i32_load(((var6 + (var0 * 286704)) + 1144720)) if (1 if var1 < var9 else 0) else (i32_load((var1 + 858016)) if (1 if var1 < var5 else 0) else (i32_load((var1 + 571312)) if (1 if var1 < var11 else 0) else (i32_load(var1 + 284608) if (1 if var1 > var8 else 0) else var8))))
        var0 = (var0 + 4)
        var10 = (var10 + 4)
        if (1 if (var10 + 4) != var12 else 0):
            continue
        break  # end loop
    if var4:
        while True:  # loop $label19
            var1 = i32_load((var6 + (var0 * 286704)) + 284608)
            var8 = (i32_load((var6 + (var0 * 286704)) + 284608) if (1 if var1 > var8 else 0) else var8)
            var0 = (var0 + 1)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var4 else 0):
                continue
            break  # end loop
    if (1 if var8 != -1 else 0):
        break
    i32_store(9142416, 0)
    break
    # Unknown: memory.fill []
    i32_store(9142416, 0)
    var3 = i32_load(9561692)
    var0 = 0
    var9 = 0
    while True:  # loop $label23
        var1 = var0
        var0 = 1
        if (1 if var2 <= 1 else 0):
            break
        while True:  # loop $label22
            if (1 if var1 != i32_load((var3 + (var0 * 286704)) + 284608) else 0):
                var0 = (var0 + 1)
                if (1 if var2 != (var0 + 1) else 0):
                    continue
                break
            break  # end loop
        var0 = (var9 + 1)
        i32_store(9142416, (var9 + 1))
        i32_store(((var1 << 2) + 59200), var9)
        var9 = var0
        var0 = (var1 + 1)
        if (1 if var1 != var8 else 0):
            continue
        break  # end loop
    if (1 if var20 == 0 else 0):
        break
    if i32_load8_u(9147127):
        break
    var7 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var14 = i32_load(9142416)
    var12 = i32_load(9147316)
    var0 = i32_load(9147320)
    var5 = i32_load(9147312)
    var2 = i32_load(9147324)
    var10 = i32_load(9561692)
    var6 = var16
    var3 = 1
    while True:  # loop $label38
        if var20:
            var1 = ((var6 & 0xFFFFFFFF) >> 1)
            var13 = (((var6 & 0xFFFFFFFF) >> 1) - 35)
            var34 = (6.28318548 / float(var14))
            var36 = ((6.28318548 / float(var14)) + -0.122173049)
            var19 = ((var10 + (var3 * 286704)) + 284608)
            var33 = float(var1)
            var4 = 0
            while True:  # loop $label30
                var9 = i32_load(var19)
                var1 = var12
                i32_store(9147324, var12)
                var11 = var5
                i32_store(9147320, var5)
                var2 = ((var2 << 11) ^ var2)
                var12 = (((((var5 & 0xFFFFFFFF) >> 19) ^ ((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8)) ^ var5) ^ var2)
                i32_store(9147316, (((((var5 & 0xFFFFFFFF) >> 19) ^ ((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8)) ^ var5) ^ var2))
                var0 = ((var0 << 11) ^ var0)
                var5 = (((((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var12 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var12)
                i32_store(9147312, (((((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var12 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var12))
                var38 = float(((var5 % var13) + 22))
                var37 = f32(((float((var36 * float((var12 % 360)))) / 360.0) + float(((var34 * float(i32_load(((var9 << 2) + 59200)))) + 0.122173049))))
                var35 = ((float(((var5 % var13) + 22)) * func48(f32(((float((var36 * float((var12 % 360)))) / 360.0) + float(((var34 * float(i32_load(((var9 << 2) + 59200)))) + 0.122173049)))))) + var33)
                if (1 if abs(((float(((var5 % var13) + 22)) * func48(f32(((float((var36 * float((var12 % 360)))) / 360.0) + float(((var34 * float(i32_load(((var9 << 2) + 59200)))) + 0.122173049)))))) + var33)) < 2147483650.0 else 0):
                    break
                var8 = -2147483648
                var38 = ((var38 * func49(var37)) + var33)
                if (1 if abs(((var38 * func49(var37)) + var33)) < 2147483650.0 else 0):
                    break
                var9 = -2147483648
                if (1 if var3 < 2 else 0):
                    break
                var0 = ((-15 if (1 if var4 > 55 else 0) else 0) + var15)
                var2 = (((-15 if (1 if var4 > 55 else 0) else 0) + var15) * var0)
                var0 = 1
                while True:  # loop $label29
                    var21 = (var10 + (var0 * 286704))
                    var18 = (i32_load((var10 + (var0 * 286704)) + 283872) - var9)
                    var21 = (i32_load(var21 + 283876) - var8)
                    if (1 if var2 < ((((i32_load((var10 + (var0 * 286704)) + 283872) - var9) * var18) + ((i32_load(var21 + 283876) - var8) * var21)) - 1) else 0):
                        var0 = (var0 + 1)
                        if (1 if var3 != (var0 + 1) else 0):
                            continue
                        break
                    break  # end loop
                var2 = var1
                var0 = var11
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != 85 else 0):
                    continue
                break  # end loop
            break
        var11 = (var6 - 30)
        var13 = 0
        if (1 if var3 >= 2 else 0):
            while True:  # loop $label33
                var1 = var5
                i32_store(9147320, var5)
                var4 = var12
                i32_store(9147324, var12)
                var2 = ((var2 << 11) ^ var2)
                var12 = (((((var1 & 0xFFFFFFFF) >> 19) ^ ((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8)) ^ var1) ^ var2)
                i32_store(9147316, (((((var1 & 0xFFFFFFFF) >> 19) ^ ((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8)) ^ var1) ^ var2))
                var0 = ((var0 << 11) ^ var0)
                var5 = (((((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var12 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var12)
                i32_store(9147312, (((((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var12 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var12))
                var8 = ((var5 % var11) + 13)
                var9 = ((var12 % var11) + 13)
                var0 = ((-15 if (1 if var13 > 55 else 0) else 0) + var15)
                var2 = (((-15 if (1 if var13 > 55 else 0) else 0) + var15) * var0)
                var0 = 1
                while True:  # loop $label32
                    var19 = (var10 + (var0 * 286704))
                    var21 = (i32_load((var10 + (var0 * 286704)) + 283872) - var9)
                    var19 = (i32_load(var19 + 283876) - var8)
                    if (1 if var2 < ((((i32_load((var10 + (var0 * 286704)) + 283872) - var9) * var21) + ((i32_load(var19 + 283876) - var8) * var19)) - 1) else 0):
                        var0 = (var0 + 1)
                        if (1 if var3 != (var0 + 1) else 0):
                            continue
                        break
                    break  # end loop
                var2 = var4
                var0 = var1
                var13 = (var13 + 1)
                if (1 if (var13 + 1) != 85 else 0):
                    continue
                break  # end loop
            break
        i32_store(9147320, var5)
        i32_store(9147324, var12)
        var1 = ((var2 << 11) ^ var2)
        var1 = (((((var5 & 0xFFFFFFFF) >> 19) ^ ((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8)) ^ var5) ^ var1)
        i32_store(9147316, (((((var5 & 0xFFFFFFFF) >> 19) ^ ((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8)) ^ var5) ^ var1))
        var0 = ((var0 << 11) ^ var0)
        var0 = (((((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var1)
        i32_store(9147312, (((((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var1))
        var8 = ((var0 % var11) + 13)
        var9 = ((var1 % var11) + 13)
        var12 = i32_load(9561692)
        var1 = (var9 - 25)
        var5 = (var9 + 50)
        if (1 if (var9 - 25) >= (var9 + 50) else 0):
            break
        var4 = (var8 - 25)
        var11 = (var8 + 50)
        if (1 if (var8 - 25) >= (var8 + 50) else 0):
            break
        while True:  # loop $label37
            var2 = (var1 + 1)
            var0 = (var1 - var9)
            var7 = (((var1 - var9) * var0) - 1)
            var0 = var4
            while True:  # loop $label36
                var6 = (var0 - var8)
                if (1 if (var7 + ((var0 - var8) * var6)) > 625 else 0):
                    break
                var6 = i32_load(9142440)
                if (1 if i32_load(9142440) <= var0 else 0):
                    break
                if (1 if (var0 | var1) < 0 else 0):
                    break
                if (1 if var1 >= var6 else 0):
                    break
                var6 = (i32_load(9147288) + ((var0 * var6) + var1))
                var10 = i32_load8_s((i32_load(9147288) + ((var0 * var6) + var1)))
                if (1 if i32_load8_s((i32_load(9147288) + ((var0 * var6) + var1))) < 0 else 0):
                    break
                if (1 if i32_load(i32_load((i32_load(9140332) + ((var10 & 255) << 2))) + 32) != 23 else 0):
                    break
                i32_store8(var6, i32_load(9147292))
                var6 = i32_load(9142840)
                var10 = (var0 + 1)
                i32_store((i32_load(9142840) + ((((var0 + 1) * (i32_load(9142440) + 2)) + var2) << 2)), 0)
                var13 = (i32_load(9142440) + 2)
                i32_store((var6 + ((((var10 + (i32_load(9142440) + 2)) * var13) + var2) << 2)), 0)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var11 else 0):
                    continue
                break  # end loop
            var1 = var2
            if (1 if var2 != var5 else 0):
                continue
            break  # end loop
        var0 = (var12 + (var3 * 286704))
        i32_store((var12 + (var3 * 286704)) + 283900, var8)
        i32_store(var0 + 283896, var9)
        i32_store(var0 + 283876, var8)
        i32_store(var0 + 283872, var9)
        var7 = i32_load(9142892)
        var6 = i32_load(9142440)
        var14 = i32_load(9142416)
        var12 = i32_load(9147316)
        var0 = i32_load(9147320)
        var5 = i32_load(9147312)
        var2 = i32_load(9147324)
        var10 = i32_load(9561692)
        var3 = (var3 + 1)
        if (1 if (var3 + 1) < var7 else 0):
            continue
        break  # end loop
    break
    var10 = ((var16 & 0xFFFFFFFF) // 90)
    var19 = ((var16 & 0xFFFFFFFF) // ((var16 & 0xFFFFFFFF) // 90))
    var12 = (((i32_load(9142892) - 1) & 0xFFFFFFFF) >> 1)
    var0 = (((((i32_load(9142892) - 1) & 0xFFFFFFFF) >> 1) & 0xFFFFFFFF) // var10)
    var24 = ((((((i32_load(9142892) - 1) & 0xFFFFFFFF) >> 1) & 0xFFFFFFFF) // var10) + (1 if var12 != (var0 * var10) else 0))
    if (1 if ((((((i32_load(9142892) - 1) & 0xFFFFFFFF) >> 1) & 0xFFFFFFFF) // var10) + (1 if var12 != (var0 * var10) else 0)) == 0 else 0):
        break
    var25 = (((var16 & 0xFFFFFFFF) >> 1) - 82)
    var26 = (0 - var19)
    var27 = ((var19 & 0xFFFFFFFF) >> 1)
    var3 = var12
    var4 = 0
    var15 = 0
    while True:  # loop $label52
        var0 = (var12 - (var10 * var15))
        var0 = ((var12 - (var10 * var15)) if (1 if var0 < var10 else 0) else var10)
        if ((var12 - (var10 * var15)) if (1 if var0 < var10 else 0) else var10):
            var28 = (var3 if (1 if var3 < var10 else 0) else var10)
            var29 = (0 if (var0 & 1) else var27)
            var13 = (var25 + (var15 * -70))
            var21 = ((var25 + (var15 * -70)) + 50)
            var11 = (var13 - 25)
            var20 = 0
            while True:  # loop $label51
                var9 = var7
                var2 = var4
                var4 = -1
                var5 = 0
                var1 = i32_load(9142892)
                if (1 if i32_load(9142892) < 2 else 0):
                    break
                var0 = 1
                var7 = (var1 - 1)
                var8 = ((var1 - 1) & 1)
                var6 = i32_load(9561692)
                if (1 if var1 != 2 else 0):
                    var14 = (var7 & -2)
                    var1 = 0
                    while True:  # loop $label40
                        var7 = (var6 + (var0 * 286704))
                        if (1 if i32_load((var6 + (var0 * 286704)) + 284608) == 1 else 0):
                            var7 = i32_load(var7 + 284620)
                            var7 = ((1 if var2 < var7 else 0) & (1 if var4 > var7 else 0))
                            var4 = (i32_load(var7 + 284620) if ((1 if var2 < var7 else 0) & (1 if var4 > var7 else 0)) else var4)
                            var5 = (var0 if var7 else var5)
                        var18 = (var0 + 1)
                        var7 = (var6 + ((var0 + 1) * 286704))
                        if (1 if i32_load((var6 + ((var0 + 1) * 286704)) + 284608) == 1 else 0):
                            var7 = i32_load(var7 + 284620)
                            var7 = ((1 if var2 < var7 else 0) & (1 if var4 > var7 else 0))
                            var4 = (i32_load(var7 + 284620) if ((1 if var2 < var7 else 0) & (1 if var4 > var7 else 0)) else var4)
                            var5 = (var18 if var7 else var5)
                        var0 = (var0 + 2)
                        var1 = (var1 + 2)
                        if (1 if (var1 + 2) != var14 else 0):
                            continue
                        break  # end loop
                if (1 if var8 == 0 else 0):
                    break
                var1 = (var6 + (var0 * 286704))
                if (1 if i32_load((var6 + (var0 * 286704)) + 284608) != 1 else 0):
                    break
                var1 = i32_load(var1 + 284620)
                var1 = ((1 if var1 < var4 else 0) & (1 if var1 > var2 else 0))
                var4 = (i32_load(var1 + 284620) if ((1 if var1 < var4 else 0) & (1 if var1 > var2 else 0)) else var4)
                var5 = (var0 if var1 else var5)
                var20 = (var20 + 1)
                var8 = ((((i32_load(9142440) & 0xFFFFFFFF) >> 1) - var29) + ((var19 if (var20 & 1) else var26) * (((var20 + 1) & 0xFFFFFFFF) >> 1)))
                var7 = i32_load(9561692)
                if (1 if var11 >= var21 else 0):
                    break
                var1 = (var8 - 25)
                var14 = (var8 + 50)
                if (1 if (var8 - 25) >= (var8 + 50) else 0):
                    break
                while True:  # loop $label44
                    var2 = (var1 + 1)
                    var0 = (var1 - var8)
                    var18 = (((var1 - var8) * var0) - 1)
                    var0 = var11
                    while True:  # loop $label43
                        var6 = (var0 - var13)
                        if (1 if (var18 + ((var0 - var13) * var6)) > 625 else 0):
                            break
                        var6 = i32_load(9142440)
                        if (1 if i32_load(9142440) <= var0 else 0):
                            break
                        if (1 if (var0 | var1) < 0 else 0):
                            break
                        if (1 if var1 >= var6 else 0):
                            break
                        var6 = (i32_load(9147288) + ((var0 * var6) + var1))
                        var22 = i32_load8_s((i32_load(9147288) + ((var0 * var6) + var1)))
                        if (1 if i32_load8_s((i32_load(9147288) + ((var0 * var6) + var1))) < 0 else 0):
                            break
                        if (1 if i32_load(i32_load((i32_load(9140332) + ((var22 & 255) << 2))) + 32) != 23 else 0):
                            break
                        i32_store8(var6, i32_load(9147292))
                        var6 = i32_load(9142840)
                        var22 = (var0 + 1)
                        i32_store((i32_load(9142840) + ((((var0 + 1) * (i32_load(9142440) + 2)) + var2) << 2)), 0)
                        var23 = (i32_load(9142440) + 2)
                        i32_store((var6 + ((((var22 + (i32_load(9142440) + 2)) * var23) + var2) << 2)), 0)
                        var0 = (var0 + 1)
                        if (1 if (var0 + 1) != var21 else 0):
                            continue
                        break  # end loop
                    var1 = var2
                    if (1 if var2 != var14 else 0):
                        continue
                    break  # end loop
                var0 = (var7 + (var5 * 286704))
                i32_store((var7 + (var5 * 286704)) + 283900, var13)
                i32_store(var0 + 283896, var8)
                i32_store(var0 + 283876, var13)
                i32_store(var0 + 283872, var8)
                var6 = 0
                var14 = i32_load(9561692)
                var7 = -1
                var1 = i32_load(9142892)
                if (1 if i32_load(9142892) < 2 else 0):
                    break
                var0 = 1
                var2 = (var1 - 1)
                var5 = ((var1 - 1) & 1)
                if (1 if var1 != 2 else 0):
                    var18 = (var2 & -2)
                    var2 = 0
                    while True:  # loop $label46
                        var1 = (var14 + (var0 * 286704))
                        if (1 if i32_load((var14 + (var0 * 286704)) + 284608) == 2 else 0):
                            var1 = i32_load(var1 + 284620)
                            var1 = ((1 if var1 < var7 else 0) & (1 if var1 > var9 else 0))
                            var7 = (i32_load(var1 + 284620) if ((1 if var1 < var7 else 0) & (1 if var1 > var9 else 0)) else var7)
                            var6 = (var0 if var1 else var6)
                        var22 = (var0 + 1)
                        var1 = (var14 + ((var0 + 1) * 286704))
                        if (1 if i32_load((var14 + ((var0 + 1) * 286704)) + 284608) == 2 else 0):
                            var1 = i32_load(var1 + 284620)
                            var1 = ((1 if var1 < var7 else 0) & (1 if var1 > var9 else 0))
                            var7 = (i32_load(var1 + 284620) if ((1 if var1 < var7 else 0) & (1 if var1 > var9 else 0)) else var7)
                            var6 = (var22 if var1 else var6)
                        var0 = (var0 + 2)
                        var2 = (var2 + 2)
                        if (1 if (var2 + 2) != var18 else 0):
                            continue
                        break  # end loop
                if (1 if var5 == 0 else 0):
                    break
                var1 = (var14 + (var0 * 286704))
                if (1 if i32_load((var14 + (var0 * 286704)) + 284608) != 2 else 0):
                    break
                var1 = i32_load(var1 + 284620)
                var1 = ((1 if var1 < var7 else 0) & (1 if var1 > var9 else 0))
                var7 = (i32_load(var1 + 284620) if ((1 if var1 < var7 else 0) & (1 if var1 > var9 else 0)) else var7)
                var6 = (var0 if var1 else var6)
                var5 = (i32_load(9142440) - var13)
                var1 = (var8 - 25)
                var22 = (var8 + 50)
                if (1 if (var8 - 25) >= (var8 + 50) else 0):
                    break
                var9 = (var5 - 25)
                var23 = (var5 + 50)
                if (1 if (var5 - 25) >= (var5 + 50) else 0):
                    break
                while True:  # loop $label50
                    var2 = (var1 + 1)
                    var0 = (var1 - var8)
                    var30 = (((var1 - var8) * var0) - 1)
                    var0 = var9
                    while True:  # loop $label49
                        var18 = (var0 - var5)
                        if (1 if (var30 + ((var0 - var5) * var18)) > 625 else 0):
                            break
                        var18 = i32_load(9142440)
                        if (1 if i32_load(9142440) <= var0 else 0):
                            break
                        if (1 if (var0 | var1) < 0 else 0):
                            break
                        if (1 if var1 >= var18 else 0):
                            break
                        var18 = (i32_load(9147288) + ((var0 * var18) + var1))
                        var31 = i32_load8_s((i32_load(9147288) + ((var0 * var18) + var1)))
                        if (1 if i32_load8_s((i32_load(9147288) + ((var0 * var18) + var1))) < 0 else 0):
                            break
                        if (1 if i32_load(i32_load((i32_load(9140332) + ((var31 & 255) << 2))) + 32) != 23 else 0):
                            break
                        i32_store8(var18, i32_load(9147292))
                        var18 = i32_load(9142840)
                        var31 = (var0 + 1)
                        i32_store((i32_load(9142840) + ((((var0 + 1) * (i32_load(9142440) + 2)) + var2) << 2)), 0)
                        var32 = (i32_load(9142440) + 2)
                        i32_store((var18 + ((((var31 + (i32_load(9142440) + 2)) * var32) + var2) << 2)), 0)
                        var0 = (var0 + 1)
                        if (1 if (var0 + 1) != var23 else 0):
                            continue
                        break  # end loop
                    var1 = var2
                    if (1 if var2 != var22 else 0):
                        continue
                    break  # end loop
                var0 = (var14 + (var6 * 286704))
                i32_store((var14 + (var6 * 286704)) + 283900, var5)
                i32_store(var0 + 283896, var8)
                i32_store(var0 + 283876, var5)
                i32_store(var0 + 283872, var8)
                if (1 if var20 != var28 else 0):
                    continue
                break  # end loop
        var3 = (var3 - var10)
        var15 = (var15 + 1)
        if (1 if (var15 + 1) != var24 else 0):
            continue
        break  # end loop
    break
    var34 = (var34 / var37)
    if (1 if var9 == 0 else 0):
        break
    if (1 if var0 < 2 else 0):
        break
    var2 = i32_load(9561692)
    var6 = i32_load(9561692)
    var11 = 1
    while True:  # loop $label61
        if var9:
            if (1 if i32_load((var6 + (var11 * 286704)) + 284608) != 2 else 0):
                break
        var37 = ((var36 * float((var7 - 1))) + var38)
        var35 = float(((i32_load(9142440) & 0xFFFFFFFF) >> 1))
        var39 = ((var33 * func48(((var36 * float((var7 - 1))) + var38))) + float(((i32_load(9142440) & 0xFFFFFFFF) >> 1)))
        if (1 if abs(((var33 * func48(((var36 * float((var7 - 1))) + var38))) + float(((i32_load(9142440) & 0xFFFFFFFF) >> 1)))) < 2147483650.0 else 0):
            break
        var4 = -2147483648
        var37 = ((var33 * func49(var37)) + var35)
        if (1 if abs(((var33 * func49(var37)) + var35)) < 2147483650.0 else 0):
            break
        var12 = -2147483648
        var1 = (-2147483648 - 25)
        var8 = (var12 + 50)
        if (1 if (-2147483648 - 25) >= (var12 + 50) else 0):
            break
        var3 = (var4 - 25)
        var10 = (var4 + 50)
        if (1 if (var4 - 25) >= (var4 + 50) else 0):
            break
        while True:  # loop $label60
            var2 = (var1 + 1)
            var0 = (var1 - var12)
            var13 = (((var1 - var12) * var0) - 1)
            var0 = var3
            while True:  # loop $label59
                var5 = (var0 - var4)
                if (1 if (var13 + ((var0 - var4) * var5)) > 625 else 0):
                    break
                var5 = i32_load(9142440)
                if (1 if i32_load(9142440) <= var0 else 0):
                    break
                if (1 if (var0 | var1) < 0 else 0):
                    break
                if (1 if var1 >= var5 else 0):
                    break
                var5 = (i32_load(9147288) + ((var0 * var5) + var1))
                var17 = i32_load8_s((i32_load(9147288) + ((var0 * var5) + var1)))
                if (1 if i32_load8_s((i32_load(9147288) + ((var0 * var5) + var1))) < 0 else 0):
                    break
                if (1 if i32_load(i32_load((i32_load(9140332) + ((var17 & 255) << 2))) + 32) != 23 else 0):
                    break
                i32_store8(var5, i32_load(9147292))
                var5 = i32_load(9142840)
                var17 = (var0 + 1)
                i32_store((i32_load(9142840) + ((((var0 + 1) * (i32_load(9142440) + 2)) + var2) << 2)), 0)
                var15 = (i32_load(9142440) + 2)
                i32_store((var5 + ((((var17 + (i32_load(9142440) + 2)) * var15) + var2) << 2)), 0)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var10 else 0):
                    continue
                break  # end loop
            var1 = var2
            if (1 if var2 != var8 else 0):
                continue
            break  # end loop
        var2 = i32_load(9561692)
        var7 = (var7 + 1)
        var0 = (var6 + (var11 * 286704))
        i32_store((var6 + (var11 * 286704)) + 283900, var4)
        i32_store(var0 + 283896, var12)
        i32_store(var0 + 283876, var4)
        i32_store(var0 + 283872, var12)
        var0 = i32_load(9142892)
        var6 = var2
        var11 = (var11 + 1)
        if (1 if (var11 + 1) < var0 else 0):
            continue
        break  # end loop
    if ((1 if var34 < 4294967300.0 else 0) & (1 if var34 >= 0.0 else 0)):
        var17 = int(var34)
        break
    var17 = 0
    break
    if var4:
        while True:  # loop $label62
            var1 = i32_load((var6 + (var2 * 286704)) + 284608)
            var12 = (i32_load((var6 + (var2 * 286704)) + 284608) if (1 if var1 > var12 else 0) else var12)
            var2 = (var2 + 1)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var4 else 0):
                continue
            break  # end loop
    var6 = -1
    if (1 if var12 == -1 else 0):
        break
    # Unknown: memory.fill []
    i32_store(9142416, 0)
    var3 = i32_load(9561692)
    var2 = 0
    var4 = 0
    while True:  # loop $label66
        var1 = var2
        var2 = 1
        if (1 if var0 <= 1 else 0):
            break
        while True:  # loop $label65
            if (1 if var1 != i32_load((var3 + (var2 * 286704)) + 284608) else 0):
                var2 = (var2 + 1)
                if (1 if var0 != (var2 + 1) else 0):
                    continue
                break
            break  # end loop
        var4 = (var4 + 1)
        i32_store(9142416, (var4 + 1))
        i32_store(((var1 << 2) + 59200), 1)
        var2 = (var1 + 1)
        if (1 if var1 != var12 else 0):
            continue
        break  # end loop
    break
    var4 = 0
    i32_store(9142416, 0)
    var1 = 1
    var5 = 0
    if (1 if i32_load(var11 + 64) == 0 else 0):
        break
    break
    if (1 if i32_load(var11 + 64) == 0 else 0):
        break
    var1 = (var0 - 1)
    var10 = ((var0 - 1) & -4)
    var7 = (var1 & 3)
    var5 = 0
    var8 = i32_load(9561692)
    var13 = (1 if (var0 - 2) > 2 else 0)
    var1 = 0
    while True:  # loop $label73
        if i32_load(((var1 << 2) + 59200)):
            var3 = 0
            if (1 if var0 < 2 else 0):
                break
            var2 = 1
            var9 = 0
            var11 = 0
            if var13:
                while True:  # loop $label71
                    var6 = (var8 + (var2 * 286704))
                    var3 = ((((var3 + (1 if i32_load((var8 + (var2 * 286704)) + 284608) == var1 else 0)) + (1 if i32_load((var6 + 571312)) == var1 else 0)) + (1 if i32_load((var6 + 858016)) == var1 else 0)) + (1 if i32_load((var6 + 1144720)) == var1 else 0))
                    var2 = (var2 + 4)
                    var11 = (var11 + 4)
                    if (1 if (var11 + 4) != var10 else 0):
                        continue
                    break  # end loop
            if (1 if var7 == 0 else 0):
                break
            while True:  # loop $label72
                var3 = (var3 + (1 if i32_load((var8 + (var2 * 286704)) + 284608) == var1 else 0))
                var2 = (var2 + 1)
                var9 = (var9 + 1)
                if (1 if (var9 + 1) != var7 else 0):
                    continue
                break  # end loop
            var5 = (var3 if (1 if var3 > var5 else 0) else var5)
        var2 = (1 if var1 == var12 else 0)
        var1 = (var1 + 1)
        if (1 if var2 == 0 else 0):
            continue
        break  # end loop
    var1 = 0
    var6 = var12
    var2 = var4
    if (1 if var4 == 0 else 0):
        var2 = (i32_load(41092) if i32_load8_u(9147210) else (var0 - 1))
    var33 = ((float(((var16 & 0xFFFFFFFF) >> 1)) + f32((((20.0 if (1 if var5 < 5 else 0) else 14.0) * float(float(var5))) / -6.2831854820251465))) + -8.0)
    var34 = ((((float(((var16 & 0xFFFFFFFF) >> 1)) + f32((((20.0 if (1 if var5 < 5 else 0) else 14.0) * float(float(var5))) / -6.2831854820251465))) + -8.0) * (var33 * 3.14159274)) / float((4 if (1 if var2 < 3 else 0) else (var2 << (var2 & 1)))))
    if ((1 if ((((float(((var16 & 0xFFFFFFFF) >> 1)) + f32((((20.0 if (1 if var5 < 5 else 0) else 14.0) * float(float(var5))) / -6.2831854820251465))) + -8.0) * (var33 * 3.14159274)) / float((4 if (1 if var2 < 3 else 0) else (var2 << (var2 & 1))))) < 4294967300.0 else 0) & (1 if var34 >= 0.0 else 0)):
        break
    var17 = 0
    if var1:
        break
    var38 = (6.28318548 / float(var4))
    var37 = ((6.28318548 / float(var4)) * 0.5)
    var12 = 0
    var7 = 0
    while True:  # loop $label88
        if i32_load(((var7 << 2) + 59200)):
            if (1 if var0 < 2 else 0):
                var34 = 0.0
                var41 = 0.0
                break
            var3 = (var0 - 1)
            var4 = ((var0 - 1) & 3)
            var8 = 0
            var9 = i32_load(9561692)
            var2 = 1
            var1 = 0
            if (1 if (var0 - 2) >= 3 else 0):
                var5 = (var3 & -4)
                var10 = 0
                while True:  # loop $label76
                    var3 = (var9 + (var2 * 286704))
                    var1 = ((((var1 + (1 if var7 == i32_load((var9 + (var2 * 286704)) + 284608) else 0)) + (1 if var7 == i32_load((var3 + 571312)) else 0)) + (1 if var7 == i32_load((var3 + 858016)) else 0)) + (1 if var7 == i32_load((var3 + 1144720)) else 0))
                    var2 = (var2 + 4)
                    var10 = (var10 + 4)
                    if (1 if (var10 + 4) != var5 else 0):
                        continue
                    break  # end loop
            if var4:
                while True:  # loop $label77
                    var1 = (var1 + (1 if var7 == i32_load((var9 + (var2 * 286704)) + 284608) else 0))
                    var2 = (var2 + 1)
                    var8 = (var8 + 1)
                    if (1 if (var8 + 1) != var4 else 0):
                        continue
                    break  # end loop
            var34 = float(var1)
            var41 = float(float(var1))
            if (1 if var1 > 4 else 0):
                break
            var42 = 20.0
            if (1 if var0 >= 2 else 0):
                var13 = 0
                var11 = 1
                var34 = (6.28318548 / var34)
                var36 = f32(((var42 * var41) / 6.2831854820251465))
                var35 = ((var38 * float(var12)) + var37)
                # Unknown: f64.convert_i32_u []
                var41 = ((i32_load(9142440) & 0xFFFFFFFF) >> 1)
                var42 = ((float((var33 * func48(((var38 * float(var12)) + var37)))) + 0.5) + ((i32_load(9142440) & 0xFFFFFFFF) >> 1))
                if (1 if abs(((float((var33 * func48(((var38 * float(var12)) + var37)))) + 0.5) + ((i32_load(9142440) & 0xFFFFFFFF) >> 1))) < 2147483648.0 else 0):
                    break
                var42 = float(-2147483648)
                var41 = ((float((var33 * func49(var35))) + 0.5) + var41)
                if (1 if abs(((float((var33 * func49(var35))) + 0.5) + var41)) < 2147483648.0 else 0):
                    break
                var41 = float(-2147483648)
                var35 = (var34 * 0.5)
                var2 = i32_load(9561692)
                while True:  # loop $label87
                    var9 = (var2 + (var11 * 286704))
                    if (1 if var7 == i32_load((var2 + (var11 * 286704)) + 284608) else 0):
                        var39 = ((var34 * float(var13)) + var35)
                        var43 = ((float((func48(((var34 * float(var13)) + var35)) * var36)) + 0.5) + var42)
                        if (1 if abs(((float((func48(((var34 * float(var13)) + var35)) * var36)) + 0.5) + var42)) < 2147483648.0 else 0):
                            break
                        var4 = -2147483648
                        var43 = ((float((func49(var39) * var36)) + 0.5) + var41)
                        if (1 if abs(((float((func49(var39) * var36)) + 0.5) + var41)) < 2147483648.0 else 0):
                            break
                        var5 = -2147483648
                        var1 = (-2147483648 - 25)
                        var10 = (var5 + 50)
                        if (1 if (-2147483648 - 25) >= (var5 + 50) else 0):
                            break
                        var3 = (var4 - 25)
                        var15 = (var4 + 50)
                        if (1 if (var4 - 25) >= (var4 + 50) else 0):
                            break
                        while True:  # loop $label86
                            var2 = (var1 + 1)
                            var0 = (var1 - var5)
                            var20 = (((var1 - var5) * var0) - 1)
                            var0 = var3
                            while True:  # loop $label85
                                var8 = (var0 - var4)
                                if (1 if (var20 + ((var0 - var4) * var8)) > 625 else 0):
                                    break
                                var8 = i32_load(9142440)
                                if (1 if i32_load(9142440) <= var0 else 0):
                                    break
                                if (1 if (var0 | var1) < 0 else 0):
                                    break
                                if (1 if var1 >= var8 else 0):
                                    break
                                var8 = (i32_load(9147288) + ((var0 * var8) + var1))
                                var14 = i32_load8_s((i32_load(9147288) + ((var0 * var8) + var1)))
                                if (1 if i32_load8_s((i32_load(9147288) + ((var0 * var8) + var1))) < 0 else 0):
                                    break
                                if (1 if i32_load(i32_load((i32_load(9140332) + ((var14 & 255) << 2))) + 32) != 23 else 0):
                                    break
                                i32_store8(var8, i32_load(9147292))
                                var8 = i32_load(9142840)
                                var14 = (var0 + 1)
                                i32_store((i32_load(9142840) + ((((var0 + 1) * (i32_load(9142440) + 2)) + var2) << 2)), 0)
                                var19 = (i32_load(9142440) + 2)
                                i32_store((var8 + ((((var14 + (i32_load(9142440) + 2)) * var19) + var2) << 2)), 0)
                                var0 = (var0 + 1)
                                if (1 if (var0 + 1) != var15 else 0):
                                    continue
                                break  # end loop
                            var1 = var2
                            if (1 if var2 != var10 else 0):
                                continue
                            break  # end loop
                        var2 = i32_load(9561692)
                        i32_store(var9 + 283900, var4)
                        i32_store(var9 + 283896, var5)
                        i32_store(var9 + 283876, var4)
                        i32_store(var9 + 283872, var5)
                        var13 = (var13 + 1)
                        var0 = i32_load(9142892)
                    var11 = (var11 + 1)
                    if (1 if (var11 + 1) < var0 else 0):
                        continue
                    break  # end loop
            var12 = (var12 + 1)
        var1 = (1 if var6 == var7 else 0)
        var7 = (var7 + 1)
        if (1 if var1 == 0 else 0):
            continue
        break  # end loop
    break
    var20 = (var15 * var15)
    var2 = 0
    while True:  # loop $label106
        var7 = var2
        if (1 if i32_load(((var2 << 2) + 59200)) == 0 else 0):
            break
        var2 = i32_load(9561692)
        if (1 if var0 < 2 else 0):
            var33 = 0.0
            var41 = 0.0
            break
        var4 = (var0 - 1)
        var6 = ((var0 - 1) & 3)
        var1 = 1
        var9 = 0
        var3 = 0
        if (1 if (var0 - 2) >= 3 else 0):
            var5 = (var4 & -4)
            var10 = 0
            while True:  # loop $label91
                var4 = (var2 + (var1 * 286704))
                var3 = ((((var3 + (1 if var7 == i32_load((var2 + (var1 * 286704)) + 284608) else 0)) + (1 if var7 == i32_load((var4 + 571312)) else 0)) + (1 if var7 == i32_load((var4 + 858016)) else 0)) + (1 if var7 == i32_load((var4 + 1144720)) else 0))
                var1 = (var1 + 4)
                var10 = (var10 + 4)
                if (1 if (var10 + 4) != var5 else 0):
                    continue
                break  # end loop
        if var6:
            while True:  # loop $label92
                var3 = (var3 + (1 if var7 == i32_load((var2 + (var1 * 286704)) + 284608) else 0))
                var1 = (var1 + 1)
                var9 = (var9 + 1)
                if (1 if (var9 + 1) != var6 else 0):
                    continue
                break  # end loop
        var33 = float(var3)
        var41 = float(float(var3))
        if (1 if var3 > 4 else 0):
            break
        var34 = f32(((20.0 * var41) / 6.2831854820251465))
        var36 = (f32(((20.0 * var41) / 6.2831854820251465)) + 8.0)
        if (1 if abs((f32(((20.0 * var41) / 6.2831854820251465)) + 8.0)) < 2147483650.0 else 0):
            break
        var1 = -2147483648
        var13 = (-2147483648 + 15)
        var6 = 0
        var15 = ((i32_load(9142440) - var1) - 30)
        var4 = i32_load(9147316)
        var1 = i32_load(9147320)
        var11 = i32_load(9147312)
        var3 = i32_load(9147324)
        if (1 if var0 >= 2 else 0):
            while True:  # loop $label96
                var5 = var11
                i32_store(9147320, var11)
                i32_store(9147324, var4)
                var3 = ((var3 << 11) ^ var3)
                var8 = (((((var5 & 0xFFFFFFFF) >> 19) ^ ((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8)) ^ var5) ^ var3)
                i32_store(9147316, (((((var5 & 0xFFFFFFFF) >> 19) ^ ((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8)) ^ var5) ^ var3))
                var1 = ((var1 << 11) ^ var1)
                var11 = (((((((var1 << 11) ^ var1) & 0xFFFFFFFF) >> 8) ^ ((var8 & 0xFFFFFFFF) >> 19)) ^ var1) ^ var8)
                i32_store(9147312, (((((((var1 << 11) ^ var1) & 0xFFFFFFFF) >> 8) ^ ((var8 & 0xFFFFFFFF) >> 19)) ^ var1) ^ var8))
                var9 = (var13 + (var11 % var15))
                var10 = (var13 + (var8 % var15))
                var1 = 1
                while True:  # loop $label97
                    var3 = (var2 + (var1 * 286704))
                    var14 = i32_load((var2 + (var1 * 286704)) + 283872)
                    if (1 if i32_load((var2 + (var1 * 286704)) + 283872) == 0 else 0):
                        break
                    var14 = (var14 - var10)
                    var3 = (i32_load(var3 + 283876) - var9)
                    if (1 if ((((var14 - var10) * var14) + ((i32_load(var3 + 283876) - var9) * var3)) - 1) > var20 else 0):
                        break
                    var3 = var4
                    var1 = var5
                    var4 = var8
                    var6 = (var6 + 1)
                    if (1 if (var6 + 1) != 55 else 0):
                        continue
                    break
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != var0 else 0):
                        continue
                    break  # end loop
                break
                break  # end loop
            raise RuntimeError('unreachable')
        i32_store(9147320, var11)
        i32_store(9147324, var4)
        var3 = ((var3 << 11) ^ var3)
        var3 = (((((var11 & 0xFFFFFFFF) >> 19) ^ ((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8)) ^ var11) ^ var3)
        i32_store(9147316, (((((var11 & 0xFFFFFFFF) >> 19) ^ ((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8)) ^ var11) ^ var3))
        var1 = ((var1 << 11) ^ var1)
        var1 = (((((((var1 << 11) ^ var1) & 0xFFFFFFFF) >> 8) ^ ((var3 & 0xFFFFFFFF) >> 19)) ^ var1) ^ var3)
        i32_store(9147312, (((((((var1 << 11) ^ var1) & 0xFFFFFFFF) >> 8) ^ ((var3 & 0xFFFFFFFF) >> 19)) ^ var1) ^ var3))
        var9 = (var13 + (var1 % var15))
        var10 = (var13 + (var3 % var15))
        if (1 if var0 < 2 else 0):
            break
        var33 = (6.28318548 / var33)
        var36 = ((6.28318548 / var33) * 0.5)
        var41 = float(var9)
        var42 = float(var10)
        var11 = 1
        var13 = 0
        while True:  # loop $label105
            var6 = (var2 + (var11 * 286704))
            if (1 if var7 == i32_load((var2 + (var11 * 286704)) + 284608) else 0):
                var38 = ((var33 * float(var13)) + var36)
                var43 = ((float((func48(((var33 * float(var13)) + var36)) * var34)) + 0.5) + var41)
                if (1 if abs(((float((func48(((var33 * float(var13)) + var36)) * var34)) + 0.5) + var41)) < 2147483648.0 else 0):
                    break
                var4 = -2147483648
                var43 = ((float((func49(var38) * var34)) + 0.5) + var42)
                if (1 if abs(((float((func49(var38) * var34)) + 0.5) + var42)) < 2147483648.0 else 0):
                    break
                var9 = -2147483648
                var1 = (-2147483648 - 25)
                var8 = (var9 + 50)
                if (1 if (-2147483648 - 25) >= (var9 + 50) else 0):
                    break
                var3 = (var4 - 25)
                var10 = (var4 + 50)
                if (1 if (var4 - 25) >= (var4 + 50) else 0):
                    break
                while True:  # loop $label104
                    var2 = (var1 + 1)
                    var0 = (var1 - var9)
                    var15 = (((var1 - var9) * var0) - 1)
                    var0 = var3
                    while True:  # loop $label103
                        var5 = (var0 - var4)
                        if (1 if (var15 + ((var0 - var4) * var5)) > 625 else 0):
                            break
                        var5 = i32_load(9142440)
                        if (1 if i32_load(9142440) <= var0 else 0):
                            break
                        if (1 if (var0 | var1) < 0 else 0):
                            break
                        if (1 if var1 >= var5 else 0):
                            break
                        var5 = (i32_load(9147288) + ((var0 * var5) + var1))
                        var14 = i32_load8_s((i32_load(9147288) + ((var0 * var5) + var1)))
                        if (1 if i32_load8_s((i32_load(9147288) + ((var0 * var5) + var1))) < 0 else 0):
                            break
                        if (1 if i32_load(i32_load((i32_load(9140332) + ((var14 & 255) << 2))) + 32) != 23 else 0):
                            break
                        i32_store8(var5, i32_load(9147292))
                        var5 = i32_load(9142840)
                        var14 = (var0 + 1)
                        i32_store((i32_load(9142840) + ((((var0 + 1) * (i32_load(9142440) + 2)) + var2) << 2)), 0)
                        var19 = (i32_load(9142440) + 2)
                        i32_store((var5 + ((((var14 + (i32_load(9142440) + 2)) * var19) + var2) << 2)), 0)
                        var0 = (var0 + 1)
                        if (1 if (var0 + 1) != var10 else 0):
                            continue
                        break  # end loop
                    var1 = var2
                    if (1 if var2 != var8 else 0):
                        continue
                    break  # end loop
                i32_store(var6 + 283900, var4)
                i32_store(var6 + 283896, var9)
                i32_store(var6 + 283876, var4)
                i32_store(var6 + 283872, var9)
                var13 = (var13 + 1)
                var2 = i32_load(9561692)
                var0 = i32_load(9142892)
            var11 = (var11 + 1)
            if (1 if (var11 + 1) < var0 else 0):
                continue
            break  # end loop
        var2 = (var7 + 1)
        if (1 if var7 != var12 else 0):
            continue
        break  # end loop
    var2 = 0
    var0 = i32_load(9142440)
    if i32_load(9142440):
        var12 = i32_load(9147288)
        var2 = var0
        var3 = 0
        while True:  # loop $label109
            var4 = (var3 + 1)
            var1 = i32_load(9147292)
            var6 = i32_load(9142840)
            var0 = 0
            while True:  # loop $label108
                if (1 if i32_load8_s((var12 + ((var0 * var2) + var3))) != var1 else 0):
                    var0 = (var0 + 1)
                    break
                var0 = (var0 + 1)
                var9 = (var6 + ((((var0 + 1) * (var2 + 2)) + var4) << 2))
                if (1 if i32_load((var6 + ((((var0 + 1) * (var2 + 2)) + var4) << 2))) != 1 else 0):
                    break
                i32_store(var9, 0)
                var1 = (i32_load(9142440) + 2)
                i32_store((var6 + (((((i32_load(9142440) + 2) + var0) * var1) + var4) << 2)), 0)
                var2 = i32_load(9142440)
                var1 = i32_load(9147292)
                if (1 if var0 < var2 else 0):
                    continue
                break  # end loop
            var3 = var4
            if (1 if var4 < var2 else 0):
                continue
            break  # end loop
    var0 = 1
    if (1 if i32_load(9142892) > 1 else 0):
        while True:  # loop $label110
            var1 = (i32_load(9561692) + (var0 * 286704))
            if (1 if i32_load(var1 + 284624) == 0 else 0):
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    var0 = 47
    var8 = i32_load(9142428)
    if (1 if i32_load(9142428) > 47 else 0):
        var36 = (float(var17) * 1.52587891e-05)
        while True:  # loop $label145
            var13 = (i32_load(9142424) + (var0 << 2))
            var26 = i32_load((i32_load(9142424) + (var0 << 2)) + 16)
            var27 = ((var0 + 7) if i32_load((i32_load(9142424) + (var0 << 2)) + 16) else var0)
            var0 = i32_load(var13 + 4)
            if (1 if i32_load(var13 + 4) == 1 else 0):
                break
            var6 = i32_load(var13 + 8)
            var1 = i32_load(var13)
            # Unknown: f64.convert_i32_u []
            var2 = i32_load(var13 + 12)
            var41 = ((float((var36 * float(i32_load(var13)))) + 0.5) if i32_load(var13 + 12) else var1)
            if ((1 if ((float((var36 * float(i32_load(var13)))) + 0.5) if i32_load(var13 + 12) else var1) < 4294967296.0 else 0) & (1 if var41 >= 0.0 else 0)):
                break
            var1 = 0
            var28 = ((0 if var1 else 1) if var2 else var1)
            if (1 if ((0 if var1 else 1) if var2 else var1) == 0 else 0):
                break
            var11 = (2147483647 if (1 if var0 == 2 else 0) else var0)
            var12 = 0
            while True:  # loop $label144
                var0 = 0
                while True:  # loop $label139
                    var1 = 0
                    if (1 if i32_load(38504) != var6 else 0):
                        if (1 if var6 != i32_load(38508) else 0):
                            break
                    var44 = i64_load(9147316)
                    var1 = i32_load(9147312)
                    i32_store(9147316, i32_load(9147312))
                    var2 = i32_load(9147324)
                    i64_store(9147320, var44)
                    var2 = (var2 ^ (var2 << 11))
                    var1 = ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8))) ^ var2)
                    i32_store(9147312, ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8))) ^ var2))
                    var1 = (var1 % 3)
                    if (1 if i32_load(i32_load(9142424) + 64) == 0 else 0):
                        var2 = i32_load(9147324)
                        i32_store(9147324, i32_load(9147316))
                        var3 = i32_load(9147320)
                        var4 = i32_load(9147312)
                        i32_store(9147320, i32_load(9147312))
                        var2 = (var2 ^ (var2 << 11))
                        var2 = ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8))) ^ var2)
                        i32_store(9147316, ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8))) ^ var2))
                        var3 = (var3 ^ (var3 << 11))
                        var3 = ((((((var3 ^ (var3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var3) ^ var2)
                        i32_store(9147312, ((((((var3 ^ (var3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var3) ^ var2))
                        break
                    var3 = var1
                    var15 = 0
                    var20 = 0
                    var1 = i32_load(9142416)
                    var2 = i32_load(9142416)
                    if (1 if var1 == 0 else 0):
                        var2 = (i32_load(41092) if i32_load8_u(9147210) else (i32_load(9142892) - 1))
                    var33 = (6.28318548 / float((4 if (1 if var2 < 3 else 0) else (var2 << (var2 & 1)))))
                    var9 = i32_load(9147312)
                    var2 = i32_load(9147324)
                    var2 = ((i32_load(9147324) << 11) ^ var2)
                    var4 = (((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var2) & 0xFFFFFFFF) >> 8)) ^ var9) ^ var2)
                    var7 = ((((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var2) & 0xFFFFFFFF) >> 8)) ^ var9) ^ var2) % ((i32_load(9142440) & 0xFFFFFFFF) >> 1))
                    var8 = i32_load(9147316)
                    var5 = i32_load(9147320)
                    var2 = var1
                    if (1 if var1 == 0 else 0):
                        var2 = (i32_load(41092) if i32_load8_u(9147210) else (i32_load(9142892) - 1))
                    var34 = float(var7)
                    i32_store(9147320, var9)
                    i32_store(9147324, var8)
                    i32_store(9147316, var4)
                    var9 = ((var5 << 11) ^ var5)
                    var4 = (((((((var5 << 11) ^ var5) & 0xFFFFFFFF) >> 8) ^ ((var4 & 0xFFFFFFFF) >> 19)) ^ var9) ^ var4)
                    i32_store(9147312, (((((((var5 << 11) ^ var5) & 0xFFFFFFFF) >> 8) ^ ((var4 & 0xFFFFFFFF) >> 19)) ^ var9) ^ var4))
                    var38 = (((6.28318548 / float((4 if (1 if var2 < 3 else 0) else (var2 << (var2 & 1))))) * float((var4 % 100000))) / 100000.0)
                    var37 = (var33 - (((6.28318548 / float((4 if (1 if var2 < 3 else 0) else (var2 << (var2 & 1))))) * float((var4 % 100000))) / 100000.0))
                    var10 = ((var6 * 404) + 9568096)
                    var29 = (var3 & 255)
                    while True:  # loop $label138
                        if (1 if var1 == 0 else 0):
                            var1 = (i32_load(41092) if i32_load8_u(9147210) else (i32_load(9142892) - 1))
                        if (1 if (4 if (1 if var1 < 3 else 0) else (var1 << (var1 & 1))) > var15 else 0):
                            var35 = ((var33 * float(var15)) + (var37 if (var15 & 1) else var38))
                            var39 = func48(((var33 * float(var15)) + (var37 if (var15 & 1) else var38)))
                            # Unknown: f64.convert_i32_u []
                            # Unknown: f64.convert_i32_u []
                            var41 = ((i32_load(9142440) & 0xFFFFFFFF) >> 1)
                            var42 = (((0.5 - (i32_load(var10 + 220) * 0.5)) + float((var39 * var34))) + ((i32_load(9142440) & 0xFFFFFFFF) >> 1))
                            if (1 if abs((((0.5 - (i32_load(var10 + 220) * 0.5)) + float((var39 * var34))) + ((i32_load(9142440) & 0xFFFFFFFF) >> 1))) < 2147483648.0 else 0):
                                break
                            var9 = -2147483648
                            var35 = func49(var35)
                            # Unknown: f64.convert_i32_u []
                            var41 = (((0.5 - (i32_load(var10 + 216) * 0.5)) + float((var35 * var34))) + var41)
                            if (1 if abs((((0.5 - (i32_load(var10 + 216) * 0.5)) + float((var35 * var34))) + var41)) < 2147483648.0 else 0):
                                break
                            var7 = -2147483648
                            if (1 if func56(-2147483648, var9, var10, var11, 0, 0, 1, 1, 0) == 0 else 0):
                                var1 = 0
                                var17 = i32_load(9142440)
                                while True:  # loop $label137
                                    var8 = var1
                                    var1 = (var1 << 2)
                                    var2 = (i32_load((((var1 << 2) | 4) + 8611904)) + var9)
                                    if (1 if var17 <= (i32_load((((var1 << 2) | 4) + 8611904)) + var9) else 0):
                                        break
                                    var4 = (i32_load((var1 + 8611904)) + var7)
                                    if (1 if var17 <= (i32_load((var1 + 8611904)) + var7) else 0):
                                        break
                                    if (1 if (var2 | var4) < 0 else 0):
                                        break
                                    var1 = i32_load(var10 + 248)
                                    # br_table ['$label118', '$label119', '$label120', '$label121']
                                    _br_idx = (i32_load(var10 + 248) - 1)
                                    break  # br_table
                                    if (1 if func282(var4, var2, var10, 0, 0, 1) == 0 else 0):
                                        break
                                    break
                                    if (1 if func283(var4, var2, var10, 0, 0, 1, 1) == 0 else 0):
                                        break
                                    break
                                    var14 = i32_load(var10 + 216)
                                    if (1 if i32_load(var10 + 216) <= 0 else 0):
                                        break
                                    var19 = (i32_load(var10 + 220) + var2)
                                    if (1 if (i32_load(var10 + 220) + var2) <= var2 else 0):
                                        break
                                    var24 = (var4 + var14)
                                    var21 = i32_load(var10 + 372)
                                    var25 = (var17 + 2)
                                    var22 = ((var17 + 2) * i32_load(var10 + 208))
                                    var23 = i32_load(var10 + 212)
                                    var30 = i32_load(9142840)
                                    var3 = var4
                                    while True:  # loop $label128
                                        var5 = (var3 + 1)
                                        var18 = (var3 - var4)
                                        var1 = var2
                                        if (1 if var3 < var17 else 0):
                                            while True:  # loop $label125
                                                if (1 if i32_load8_u((var21 + (((var1 - var2) * var14) + var18))) == 0 else 0):
                                                    var1 = (var1 + 1)
                                                    break
                                                if (1 if var1 >= var17 else 0):
                                                    break
                                                if (1 if (var1 | var3) < 0 else 0):
                                                    break
                                                var1 = (var1 + 1)
                                                if (1 if i32_load((var30 + (((((var1 + 1) + var22) * var25) + var5) << 2))) != var23 else 0):
                                                    break
                                                if (1 if var1 != var19 else 0):
                                                    continue
                                                break
                                                break  # end loop
                                            raise RuntimeError('unreachable')
                                        while True:  # loop $label127
                                            if i32_load8_u((var21 + (((var1 - var2) * var14) + var18))):
                                                break
                                            var1 = (var1 + 1)
                                            if (1 if (var1 + 1) != var19 else 0):
                                                continue
                                            break  # end loop
                                        var3 = var5
                                        if (1 if var5 < var24 else 0):
                                            continue
                                        break  # end loop
                                    break
                                    var3 = i32_load(var10 + 208)
                                    if (1 if i32_load(var10 + 208) == 0 else 0):
                                        var14 = i32_load(var10 + 216)
                                        if (1 if i32_load(var10 + 216) <= 0 else 0):
                                            break
                                        var21 = (i32_load(var10 + 220) + var2)
                                        if (1 if (i32_load(var10 + 220) + var2) <= var2 else 0):
                                            break
                                        var22 = (var4 + var14)
                                        var18 = i32_load(var10 + 372)
                                        var19 = (var17 + 2)
                                        var23 = i32_load(9671128)
                                        var24 = i32_load(9142840)
                                        var3 = var4
                                        while True:  # loop $label133
                                            var5 = (var3 + 1)
                                            var25 = (var3 - var4)
                                            var1 = var2
                                            if (1 if var3 < var17 else 0):
                                                while True:  # loop $label130
                                                    if (1 if i32_load8_u((var18 + (((var1 - var2) * var14) + var25))) == 0 else 0):
                                                        var1 = (var1 + 1)
                                                        break
                                                    if (1 if var1 >= var17 else 0):
                                                        break
                                                    if (1 if (var1 | var3) < 0 else 0):
                                                        break
                                                    var1 = (var1 + 1)
                                                    if i32_load((var24 + ((((var1 + 1) * var19) + var5) << 2))):
                                                        break
                                                    if (1 if i32_load(((i32_load8_u((var23 + (i32_load((var24 + ((((var1 + var19) * var19) + var5) << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 1 else 0):
                                                        break
                                                    if (1 if var1 != var21 else 0):
                                                        continue
                                                    break
                                                    break  # end loop
                                                raise RuntimeError('unreachable')
                                            while True:  # loop $label132
                                                if i32_load8_u((var18 + (((var1 - var2) * var14) + var25))):
                                                    break
                                                var1 = (var1 + 1)
                                                if (1 if (var1 + 1) != var21 else 0):
                                                    continue
                                                break  # end loop
                                            var3 = var5
                                            if (1 if var5 < var22 else 0):
                                                continue
                                            break  # end loop
                                        break
                                    # br_table ['$label134', '$label135', '$label136']
                                    _br_idx = (var1 - 4)
                                    break  # br_table
                                    if (1 if func193(var4, var2, var10, var11, 0, 0, 1, 0) == 0 else 0):
                                        break
                                    break
                                    if (1 if func194(var4, var2, var10, var11, 0, 0, 1) == 0 else 0):
                                        break
                                    break
                                    if (1 if var3 > 2 else 0):
                                        break
                                    if func73(var4, var2, var10, 0, 0, 1):
                                        break
                                    var17 = i32_load(9142440)
                                    var1 = (var8 + 2)
                                    if (1 if var8 < 5198 else 0):
                                        continue
                                    break  # end loop
                            var4 = var7
                            var2 = var9
                            var20 = (1 if func34(var6, var11, var4, var2, var29, 1) else var20)
                            var15 = (var15 + 1)
                            var1 = i32_load(9142416)
                            continue
                        break  # end loop
                    var1 = var20
                    if (1 if var20 == 0 else 0):
                        var2 = (1 if var0 < 24 else 0)
                        var0 = (var0 + 1)
                        if var2:
                            continue
                    break  # end loop
                if (1 if var26 == 0 else 0):
                    break
                if (1 if var1 == 0 else 0):
                    break
                var0 = (i32_load(9671128) + (var1 * 132))
                var1 = i32_load(var13 + 20)
                if (1 if i32_load(var13 + 20) <= 2147483646 else 0):
                    i32_store(var0 + 52, var1)
                var1 = i32_load(var13 + 24)
                if (1 if i32_load(var13 + 24) <= 2147483646 else 0):
                    i32_store(var0 + 60, var1)
                var1 = i32_load(var13 + 28)
                if (1 if i32_load(var13 + 28) > 2147483646 else 0):
                    break
                i32_store(var0 + 64, var1)
                if (1 if i32_load(var13 + 28) > 2147483646 else 0):
                    break
                i32_store(var0 + 68, i32_load(var13 + 32))
                var2 = i32_load(var0 + 76)
                var1 = i32_load(var13 + 36)
                if (1 if i32_load(var13 + 36) > 2147483646 else 0):
                    break
                i32_store(var0 + 72, var1)
                if (1 if i32_load(var13 + 36) > 2147483646 else 0):
                    break
                i32_store(var0 + 76, i32_load(var13 + 40))
                var1 = i32_load(var13 + 44)
                if (1 if i32_load(var13 + 44) <= 2147483646 else 0):
                    i32_store(var0 + 84, var1)
                var3 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
                var1 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264)
                if (1 if i32_load(var3 + 92) == 0 else 0):
                    if (1 if var1 == 2 else 0):
                        break
                    i32_store(var0 + 52, 0)
                if (1 if var1 != 1 else 0):
                    break
                i32_store(var0 + 84, 0)
                i32_store(var0 + 72, 0)
                i32_store(var0 + 60, 0)
                var1 = i32_load(var0 + 64)
                if i32_load(var0 + 64):
                else:
                    i32_store((var0 - -64), -1)
                i32_store(var1 + 68, -1)
                var1 = i32_load(var0 + 72)
                i32_store(var0 + 76, i32_load(var0 + 72))
                if (1 if var1 == 0 else 0):
                    break
                if var2:
                    break
                var12 = (var12 + 1)
                if (1 if (var12 + 1) != var28 else 0):
                    continue
                break  # end loop
            var8 = i32_load(9142428)
            var0 = (var27 + 5)
            if (1 if (var27 + 5) < var8 else 0):
                continue
            break  # end loop
    i32_store(9684376, i32_load(9671136))
    if (1 if (i32_load(i32_load(9142424) + 60) << 1) < 200 else 0):
        break
    var16 = 0
    var1 = i32_load(9142440)
    if (1 if i32_load(9142440) <= 0 else 0):
        break
    while True:  # loop $label148
        var0 = 0
        while True:  # loop $label147
            var4 = i32_load(38448)
            var6 = i32_load(i32_load(((i32_load(38448) * 72) + 9263856)) + 20)
            var2 = i32_load(9147324)
            i32_store(9147324, i32_load(9147320))
            var12 = i32_load(9147316)
            var3 = i32_load(9147312)
            i32_store(9147316, i32_load(9147312))
            i32_store(9147320, var12)
            var2 = (var2 ^ (var2 << 11))
            var2 = ((var3 ^ (((var3 & 0xFFFFFFFF) >> 19) ^ (((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8))) ^ var2)
            i32_store(9147312, ((var3 ^ (((var3 & 0xFFFFFFFF) >> 19) ^ (((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8))) ^ var2))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var1 else 0):
                continue
            break  # end loop
        var16 = (var16 + 1)
        if (1 if (var16 + 1) != var1 else 0):
            continue
        break  # end loop
    i32_store(9684380, (i32_load(9671136) - i32_load(9684376)))
    var11 = 1
    if (1 if i32_load(9142892) > 1 else 0):
        while True:  # loop $label163
            var4 = (i32_load(9561692) + (var11 * 286704))
            if (1 if i32_load((i32_load(9561692) + (var11 * 286704)) + 284624) == 0 else 0):
                break
            var6 = i32_load(var4 + 283872)
            var9 = (i32_load(var4 + 283872) - 25)
            var7 = (var6 + 50)
            if (1 if (i32_load(var4 + 283872) - 25) >= (var6 + 50) else 0):
                break
            var12 = i32_load(var4 + 283876)
            var2 = (i32_load(var4 + 283876) - 25)
            var8 = (var12 + 50)
            if (1 if (i32_load(var4 + 283876) - 25) >= (var12 + 50) else 0):
                break
            while True:  # loop $label153
                var1 = (var9 + 1)
                var0 = (var9 - var6)
                var10 = (((var9 - var6) * var0) - 1)
                var0 = var2
                while True:  # loop $label152
                    var3 = (var0 - var12)
                    if (1 if (var10 + ((var0 - var12) * var3)) > 625 else 0):
                        break
                    var3 = i32_load(9142440)
                    if (1 if i32_load(9142440) <= var0 else 0):
                        break
                    if (1 if (var0 | var9) < 0 else 0):
                        break
                    if (1 if var3 <= var9 else 0):
                        break
                    var3 = (var3 + 2)
                    var3 = (i32_load(9671128) + (i32_load((i32_load(9142840) + ((var1 + (((var0 + (var3 + 2)) + 1) * var3)) << 2))) * 132))
                    if (1 if i32_load(38448) != i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9142840) + ((var1 + (((var0 + (var3 + 2)) + 1) * var3)) << 2))) * 132)) + 122) else 0):
                        break
                    var5 = func26(4)
                    var13 = (func26(4) + 4)
                    var16 = i32_load(var3)
                    if i32_load(var3):
                        i32_store(var3 + 4, var16)
                    i32_store(var3 + 8, var13)
                    i32_store(var3 + 4, var5)
                    i32_store(var3, var5)
                    # Unknown: memory.fill []
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var8 else 0):
                        continue
                    break  # end loop
                var9 = var1
                if (1 if var1 != var7 else 0):
                    continue
                break  # end loop
            var0 = i32_load(9142424)
            if (1 if (i32_load(i32_load(9142424) + 60) << 1) < 5 else 0):
                break
            if i32_load(var0 + 64):
                break
            var5 = 0
            if (1 if i32_load(9147128) == 9 else 0):
                break
            var12 = (var4 + 283876)
            var9 = (var4 + 283872)
            while True:  # loop $label162
                var3 = i32_load(var12)
                var4 = i32_load(var9)
                var0 = i32_load(9147324)
                i32_store(9147324, i32_load(9147320))
                var2 = i32_load(9147316)
                var1 = i32_load(9147312)
                i32_store(9147316, i32_load(9147312))
                i32_store(9147320, var2)
                var0 = (var0 ^ (var0 << 11))
                var0 = ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0)
                i32_store(9147312, ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0))
                var33 = ((float((var0 % 100)) / 100.0) * 6.28318548)
                var0 = i32_load(9142440)
                while True:  # loop $label155
                    var34 = var33
                    var33 = (func49(var33) * 20.0)
                    if (1 if abs((func49(var33) * 20.0)) < 2147483650.0 else 0):
                        break
                    var1 = -2147483648
                    var33 = (var34 + 1.57079637)
                    var1 = (var1 + var4)
                    if (1 if (var1 + var4) <= 0 else 0):
                        continue
                    if (1 if var0 <= var1 else 0):
                        continue
                    var34 = (func48(var34) * 20.0)
                    if (1 if abs((func48(var34) * 20.0)) < 2147483650.0 else 0):
                        break
                    var2 = (-2147483648 + var3)
                    if (1 if (-2147483648 + var3) <= 0 else 0):
                        continue
                    if (1 if var0 <= var2 else 0):
                        continue
                    break  # end loop
                var16 = (var2 - 10)
                var7 = (var1 - 10)
                var10 = 0
                var8 = i32_load(i32_load(9142424) + 64)
                while True:  # loop $label161
                    var1 = i32_load(38448)
                    var13 = i32_load(i32_load(((i32_load(38448) * 72) + 9263856)) + 20)
                    var0 = i32_load(9147320)
                    var3 = ((i32_load(9147320) << 11) ^ var0)
                    var2 = i32_load(9147312)
                    var0 = i32_load(9147324)
                    var0 = ((i32_load(9147324) << 11) ^ var0)
                    var0 = (((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var0) & 0xFFFFFFFF) >> 8)) ^ var2) ^ var0)
                    var3 = (((((((i32_load(9147320) << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ (((((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var0) & 0xFFFFFFFF) >> 8)) ^ var2) ^ var0) & 0xFFFFFFFF) >> 19)) ^ var3) ^ var0)
                    i32_store(9147324, (((((((i32_load(9147320) << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ (((((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var0) & 0xFFFFFFFF) >> 8)) ^ var2) ^ var0) & 0xFFFFFFFF) >> 19)) ^ var3) ^ var0))
                    var4 = i32_load(9147316)
                    var4 = ((i32_load(9147316) << 11) ^ var4)
                    var4 = (((((((i32_load(9147316) << 11) ^ var4) & 0xFFFFFFFF) >> 8) ^ ((var3 & 0xFFFFFFFF) >> 19)) ^ var4) ^ var3)
                    i32_store(9147320, (((((((i32_load(9147316) << 11) ^ var4) & 0xFFFFFFFF) >> 8) ^ ((var3 & 0xFFFFFFFF) >> 19)) ^ var4) ^ var3))
                    var2 = (var2 ^ (var2 << 11))
                    var2 = ((((((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var4 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var4)
                    i32_store(9147316, ((((((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var4 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var4))
                    var6 = ((var0 << 11) ^ var0)
                    var6 = (((((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var6) ^ var2)
                    i32_store(9147312, (((((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var6) ^ var2))
                    var6 = ((var16 + (var2 % 13)) + (var6 & 7))
                    var3 = ((var7 + (var3 % 13)) + (var4 & 7))
                    var4 = ((var0 % (var13 - 3)) + 3)
                    if (1 if var8 == 0 else 0):
                        break
                    var0 = i32_load(9142416)
                    var2 = i32_load(9142416)
                    if (1 if var0 == 0 else 0):
                        var2 = (i32_load(41092) if i32_load8_u(9147210) else (i32_load(9142892) - 1))
                    var34 = (6.28318548 / float((4 if (1 if var2 < 3 else 0) else (var2 << (var2 & 1)))))
                    var2 = ((i32_load(9142440) & 0xFFFFFFFF) >> 1)
                    var6 = (var6 - ((i32_load(9142440) & 0xFFFFFFFF) >> 1))
                    var3 = (var3 - var2)
                    var33 = f32(func262(float((var6 - ((i32_load(9142440) & 0xFFFFFFFF) >> 1))), float((var3 - var2))))
                    if (1 if (6.28318548 / float((4 if (1 if var2 < 3 else 0) else (var2 << (var2 & 1))))) < f32(func262(float((var6 - ((i32_load(9142440) & 0xFFFFFFFF) >> 1))), float((var3 - var2)))) else 0):
                        break
                    if (1 if var33 < 0.0 else 0):
                        break
                    var36 = f32(math.sqrt(float(((var3 * var3) + (var6 * var6)))))
                    if (1 if f32(math.sqrt(float(((var3 * var3) + (var6 * var6))))) >= float(var2) else 0):
                        break
                    var38 = (var34 - var33)
                    var3 = ((var1 * 404) + 9568096)
                    var2 = 0
                    while True:  # loop $label160
                        if (1 if var0 == 0 else 0):
                            var0 = (i32_load(41092) if i32_load8_u(9147210) else (i32_load(9142892) - 1))
                        if (1 if var2 >= (4 if (1 if var0 < 3 else 0) else (var0 << (var0 & 1))) else 0):
                            break
                        var37 = ((var34 * float(var2)) + (var38 if (var2 & 1) else var33))
                        var35 = func48(((var34 * float(var2)) + (var38 if (var2 & 1) else var33)))
                        # Unknown: f64.convert_i32_u []
                        # Unknown: f64.convert_i32_u []
                        var41 = ((i32_load(9142440) & 0xFFFFFFFF) >> 1)
                        var42 = (((0.5 - (i32_load(var3 + 220) * 0.5)) + float((var35 * var36))) + ((i32_load(9142440) & 0xFFFFFFFF) >> 1))
                        if (1 if abs((((0.5 - (i32_load(var3 + 220) * 0.5)) + float((var35 * var36))) + ((i32_load(9142440) & 0xFFFFFFFF) >> 1))) < 2147483648.0 else 0):
                            break
                        var0 = -2147483648
                        var37 = func49(var37)
                        # Unknown: f64.convert_i32_u []
                        var41 = (((0.5 - (i32_load(var3 + 216) * 0.5)) + float((var37 * var36))) + var41)
                        if (1 if abs((((0.5 - (i32_load(var3 + 216) * 0.5)) + float((var37 * var36))) + var41)) < 2147483648.0 else 0):
                            break
                        var2 = (var2 + 1)
                        var0 = i32_load(9142416)
                        continue
                        break  # end loop
                    raise RuntimeError('unreachable')
                    var10 = (var10 + 1)
                    if (1 if (var10 + 1) != 55 else 0):
                        continue
                    break  # end loop
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != 4 else 0):
                    continue
                break  # end loop
            var11 = (var11 + 1)
            if (1 if (var11 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    var0 = i32_load(9142424)
    if (1 if (i32_load(i32_load(9142424) + 60) << 1) <= 4 else 0):
        break
    if (1 if i32_load(var0 + 64) == 0 else 0):
        break
    var0 = i32_load(9561692)
    var3 = i32_load((i32_load(9561692) + 570580))
    var4 = i32_load((var0 + 570576))
    var0 = i32_load(9147324)
    i32_store(9147324, i32_load(9147320))
    var2 = i32_load(9147316)
    var1 = i32_load(9147312)
    i32_store(9147316, i32_load(9147312))
    i32_store(9147320, var2)
    var0 = (var0 ^ (var0 << 11))
    var0 = ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0)
    i32_store(9147312, ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0))
    var33 = ((float((var0 % 100)) / 100.0) * 6.28318548)
    var0 = i32_load(9142440)
    while True:  # loop $label166
        var34 = var33
        var33 = (func49(var33) * 20.0)
        if (1 if abs((func49(var33) * 20.0)) < 2147483650.0 else 0):
            break
        var1 = -2147483648
        var33 = (var34 + 1.57079637)
        var1 = (var1 + var4)
        if (1 if (var1 + var4) <= 0 else 0):
            continue
        if (1 if var0 <= var1 else 0):
            continue
        var34 = (func48(var34) * 20.0)
        if (1 if abs((func48(var34) * 20.0)) < 2147483650.0 else 0):
            break
        var2 = (-2147483648 + var3)
        if (1 if (-2147483648 + var3) <= 0 else 0):
            continue
        if (1 if var0 <= var2 else 0):
            continue
        break  # end loop
    var0 = i32_load(9561692)
    var3 = i32_load((i32_load(9561692) + 570580))
    var4 = i32_load((var0 + 570576))
    var0 = i32_load(9147324)
    i32_store(9147324, i32_load(9147320))
    var2 = i32_load(9147316)
    var1 = i32_load(9147312)
    i32_store(9147316, i32_load(9147312))
    i32_store(9147320, var2)
    var0 = (var0 ^ (var0 << 11))
    var0 = ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0)
    i32_store(9147312, ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0))
    var33 = ((float((var0 % 100)) / 100.0) * 6.28318548)
    var0 = i32_load(9142440)
    while True:  # loop $label169
        var34 = var33
        var33 = (func49(var33) * 20.0)
        if (1 if abs((func49(var33) * 20.0)) < 2147483650.0 else 0):
            break
        var1 = -2147483648
        var33 = (var34 + 1.57079637)
        var1 = (var1 + var4)
        if (1 if (var1 + var4) <= 0 else 0):
            continue
        if (1 if var0 <= var1 else 0):
            continue
        var34 = (func48(var34) * 20.0)
        if (1 if abs((func48(var34) * 20.0)) < 2147483650.0 else 0):
            break
        var2 = (-2147483648 + var3)
        if (1 if (-2147483648 + var3) <= 0 else 0):
            continue
        if (1 if var0 <= var2 else 0):
            continue
        break  # end loop
    var0 = i32_load(9561692)
    var3 = i32_load((i32_load(9561692) + 570580))
    var4 = i32_load((var0 + 570576))
    var0 = i32_load(9147324)
    i32_store(9147324, i32_load(9147320))
    var2 = i32_load(9147316)
    var1 = i32_load(9147312)
    i32_store(9147316, i32_load(9147312))
    i32_store(9147320, var2)
    var0 = (var0 ^ (var0 << 11))
    var0 = ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0)
    i32_store(9147312, ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0))
    var33 = ((float((var0 % 100)) / 100.0) * 6.28318548)
    var0 = i32_load(9142440)
    while True:  # loop $label172
        var34 = var33
        var33 = (func49(var33) * 20.0)
        if (1 if abs((func49(var33) * 20.0)) < 2147483650.0 else 0):
            break
        var1 = -2147483648
        var33 = (var34 + 1.57079637)
        var1 = (var1 + var4)
        if (1 if (var1 + var4) <= 0 else 0):
            continue
        if (1 if var0 <= var1 else 0):
            continue
        var34 = (func48(var34) * 20.0)
        if (1 if abs((func48(var34) * 20.0)) < 2147483650.0 else 0):
            break
        var2 = (-2147483648 + var3)
        if (1 if (-2147483648 + var3) <= 0 else 0):
            continue
        if (1 if var0 <= var2 else 0):
            continue
        break  # end loop
    var0 = i32_load(9561692)
    var3 = i32_load((i32_load(9561692) + 570580))
    var4 = i32_load((var0 + 570576))
    var0 = i32_load(9147324)
    i32_store(9147324, i32_load(9147320))
    var2 = i32_load(9147316)
    var1 = i32_load(9147312)
    i32_store(9147316, i32_load(9147312))
    i32_store(9147320, var2)
    var0 = (var0 ^ (var0 << 11))
    var0 = ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0)
    i32_store(9147312, ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0))
    var33 = ((float((var0 % 100)) / 100.0) * 6.28318548)
    var0 = i32_load(9142440)
    while True:  # loop $label175
        var34 = var33
        var33 = (func49(var33) * 20.0)
        if (1 if abs((func49(var33) * 20.0)) < 2147483650.0 else 0):
            break
        var1 = -2147483648
        var33 = (var34 + 1.57079637)
        var1 = (var1 + var4)
        if (1 if (var1 + var4) <= 0 else 0):
            continue
        if (1 if var0 <= var1 else 0):
            continue
        var34 = (func48(var34) * 20.0)
        if (1 if abs((func48(var34) * 20.0)) < 2147483650.0 else 0):
            break
        var2 = (-2147483648 + var3)
        if (1 if (-2147483648 + var3) <= 0 else 0):
            continue
        if (1 if var0 <= var2 else 0):
            continue
        break  # end loop
    var0 = 0
    var2 = i32_load(9561692)
    var1 = i32_load(((i32_load(9561692) + (i32_load(38508) << 2)) + 284636))
    if (1 if i32_load(((i32_load(9561692) + (i32_load(38508) << 2)) + 284636)) == 0 else 0):
        break
    var3 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    while True:  # loop $label178
        var2 = i32_load((i32_load(var1) + (var0 << 2)))
        if i32_load((i32_load(var1) + (var0 << 2))):
            func408(i32_load(38492), (i32_load(9671128) + (var2 * 132)))
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var3 else 0):
            continue
        break  # end loop
    var2 = i32_load(9561692)
    var0 = 0
    var1 = i32_load(((var2 + (i32_load(38504) << 2)) + 284636))
    if (1 if i32_load(((var2 + (i32_load(38504) << 2)) + 284636)) == 0 else 0):
        break
    var2 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    while True:  # loop $label180
        var3 = i32_load((i32_load(var1) + (var0 << 2)))
        if i32_load((i32_load(var1) + (var0 << 2))):
            func408(i32_load(38492), (i32_load(9671128) + (var3 * 132)))
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var2 else 0):
            continue
        break  # end loop
    return func126(var1, var2, 13, 13, (1 if i32_load(i32_load(9142424) + 64) != 0 else 0))

