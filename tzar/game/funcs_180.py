"""
Auto-generated from WAT. Contains 2 functions.
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
# $func34
# ==========================================================
def func34(var0, var1, var2, var3, var4, var5):
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
    if (1 if i32_load(9147132) == 0 else 0):
        var7 = i32_load(9671136)
        break
    var18 = i32_load(9142848)
    if (1 if i32_load(9142848) == i32_load(9671144) else 0):
        break
    i32_store(9671148, 3)
    i32_store(9671144, var18)
    var6 = 3
    var7 = i32_load(9671136)
    if (1 if 3 < i32_load(9671136) else 0):
        var9 = i32_load(9671128)
        while True:  # loop $label3
            var8 = (var9 + (var6 * 132))
            if (1 if i32_load8_u((var9 + (var6 * 132)) + 125) == 3 else 0):
                if (1 if ((var18 - i32_load(var8 + 68)) * 25) > 70000 else 0):
                    break
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != var7 else 0):
                continue
            break  # end loop
    i32_store(9671148, var7)
    break
    i32_store(9671148, (var6 + 1))
    var7 = var6
    var19 = ((var0 * 404) + 9568096)
    if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 3 else 0):
        break
    var20 = i32_load(9561692)
    var16 = (var1 if (1 if var1 != 2147483647 else 0) else 0)
    if (1 if func56(var2, var3, var19, (var1 if (1 if var1 != 2147483647 else 0) else 0), 1, var7, 1, var5, 0) == 0 else 0):
        break
    var18 = (1 if var7 != i32_load(9671136) else 0)
    if (1 if (1 if var7 != i32_load(9671136) else 0) == 0 else 0):
        var8 = (var7 + 1)
        i32_store(9671136, (var7 + 1))
        var6 = i32_load(9671132)
        if (1 if var8 < i32_load(9671132) else 0):
            break
        var6 = (i32_load(9671140) + var6)
        i32_store(9671132, (i32_load(9671140) + var6))
        i32_store(9671128, func228(i32_load(9671128), var6, var8))
        break
    var9 = func26(4)
    var6 = (func26(4) + 4)
    var10 = (i32_load(9671128) + (var7 * 132))
    var8 = i32_load((i32_load(9671128) + (var7 * 132)))
    if i32_load((i32_load(9671128) + (var7 * 132))):
        i32_store(var10 + 4, var8)
    i32_store(var10 + 8, var6)
    i32_store(var10 + 4, var9)
    i32_store(var10, var9)
    # Unknown: memory.fill []
    var11 = i32_load(9671128)
    var21 = (i32_load(9671128) + (var7 * 132))
    i32_store((i32_load(9671128) + (var7 * 132)) + 28, var7)
    if (1 if i32_load(var19 + 264) != 2 else 0):
        if (1 if i32_load(((var0 * 404) + 9568096) + 188) == 55 else 0):
            break
        if (1 if i32_load(38500) != var0 else 0):
            break
        break
    if (1 if i32_load(38500) == var0 else 0):
        break
    if (1 if i32_load(38528) != var0 else 0):
        break
    i32_store16((var11 + (var7 * 132)) + 110, var16)
    if (1 if var1 != 2147483647 else 0):
        break
    if (1 if i32_load(((var0 * 404) + 9568096) + 188) != 55 else 0):
        break
    i32_store8((var11 + (var7 * 132)) + 126, 2)
    var8 = (var11 + (var7 * 132))
    i32_store16((var11 + (var7 * 132)) + 114, var3)
    i32_store16(var8 + 112, var2)
    i32_store8(var8 + 122, var0)
    var6 = ((var0 * 404) + 9568096)
    var1 = i32_load(((var0 * 404) + 9568096) + 168)
    i32_store8(var8 + 124, (i32_load(((var0 * 404) + 9568096) + 168) if var1 else var4))
    if var5:
        func420(var21)
        var10 = i32_load(((i32_load8_u(var8 + 122) * 72) + 9263856))
        i32_store(var8 + 64, (i32_load((((var20 + (var16 * 286704)) + (var0 * 36)) + 269388)) + i32_load(var6 + 104)))
        break
    var6 = i32_load(var6 + 356)
    if i32_load(var6 + 356):
        break
    var1 = ((var0 * 404) + 9568096)
    var4 = i32_load(((var0 * 404) + 9568096) + 216)
    var1 = i32_load(var1 + 220)
    var1 = (i32_load(((var0 * 404) + 9568096) + 216) if (1 if var1 < var4 else 0) else i32_load(var1 + 220))
    var1 = ((6 if (1 if var1 >= 6 else 0) else (i32_load(((var0 * 404) + 9568096) + 216) if (1 if var1 < var4 else 0) else i32_load(var1 + 220))) - 1)
    if (1 if ((6 if (1 if var1 >= 6 else 0) else (i32_load(((var0 * 404) + 9568096) + 216) if (1 if var1 < var4 else 0) else i32_load(var1 + 220))) - 1) > 4 else 0):
        var6 = 9142636
        break
    var6 = i32_load(((var1 << 2) + 10132))
    var10 = i32_load(var6)
    var1 = (var11 + (var7 * 132))
    i32_store8((var11 + (var7 * 132)) + 125, 4)
    i32_store(var1 + 64, 1)
    var1 = (((var20 + (var16 * 286704)) + (var0 << 2)) + 282828)
    i32_store((((var20 + (var16 * 286704)) + (var0 << 2)) + 282828), (i32_load(var1) + 1))
    var6 = (var11 + (var7 * 132))
    var4 = ((var0 * 404) + 9568096)
    var1 = ((var20 + (var16 * 286704)) + (var0 * 36))
    i32_store((var11 + (var7 * 132)) + 68, (i32_load(((var0 * 404) + 9568096) + 108) + i32_load((((var20 + (var16 * 286704)) + (var0 * 36)) + 269392))))
    i32_store(var6 + 52, (i32_load(var4 + 92) + i32_load((var1 + 269380))))
    i32_store(var6 + 60, (i32_load(var4 + 100) + i32_load((var1 + 269384))))
    i32_store(var6 + 84, (i32_load(var4 + 112) + i32_load((var1 + 269396))))
    var1 = (i32_load(var4 + 120) + i32_load((var1 + 269404)))
    i32_store(var6 + 72, (i32_load(var4 + 120) + i32_load((var1 + 269404))))
    i32_store(var6 + 76, var1)
    if (1 if var0 == i32_load(38528) else 0):
        i32_store(var6 + 80, 300)
    if (1 if var0 == i32_load(38500) else 0):
        var22 = i64_load(9147316)
        var4 = i32_load(9147312)
        i32_store(9147316, i32_load(9147312))
        var1 = i32_load(9147324)
        i64_store(9147320, var22)
        var1 = (var1 ^ (var1 << 11))
        var1 = ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8))) ^ var1)
        i32_store(9147312, ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8))) ^ var1))
        i32_store8(var8 + 124, (var1 % 9))
    if i32_load8_u(9147213):
        var1 = i32_load(i32_load(9142424) + 48)
        if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
            break
        var12 = i32_load(((var0 * 404) + 9568096) + 216)
        if (1 if i32_load(((var0 * 404) + 9568096) + 216) == 0 else 0):
            break
        if i32_load8_u(9147152):
            break
        var14 = i32_load(9142440)
        var15 = i32_load(9147376)
        if (1 if var1 != 2 else 0):
            var9 = (var12 & -2)
            var8 = (var12 & 1)
            var6 = 0
            while True:  # loop $label15
                var13 = (var2 + var17)
                var1 = 0
                var4 = 0
                if (1 if var12 != 1 else 0):
                    while True:  # loop $label14
                        var6 = ((1 if (i32_load16_u((var15 + ((var13 + (var14 * ((var1 | 1) + var3))) << 1))) | i32_load16_u((var15 + ((var13 + (var14 * (var1 + var3))) << 1)))) != 0 else 0) | var6)
                        var1 = (var1 + 2)
                        var4 = (var4 + 2)
                        if (1 if (var4 + 2) != var9 else 0):
                            continue
                        break  # end loop
                if var8:
                    var6 = ((1 if i32_load16_u((var15 + ((var13 + (var14 * (var1 + var3))) << 1))) != 0 else 0) | var6)
                var17 = (var17 + 1)
                if (1 if (var17 + 1) != var12 else 0):
                    continue
                break  # end loop
            break
        var9 = (var12 & -2)
        var8 = (var12 & 1)
        var6 = 0
        while True:  # loop $label18
            var13 = (var2 + var17)
            var1 = 0
            var4 = 0
            if (1 if var12 != 1 else 0):
                while True:  # loop $label17
                    var6 = (((1 if i32_load16_u((var15 + ((var13 + (var14 * ((var1 | 1) + var3))) << 1))) > 1 else 0) | (1 if i32_load16_u((var15 + ((var13 + (var14 * (var1 + var3))) << 1))) > 1 else 0)) | var6)
                    var1 = (var1 + 2)
                    var4 = (var4 + 2)
                    if (1 if (var4 + 2) != var9 else 0):
                        continue
                    break  # end loop
            if var8:
                var6 = ((1 if i32_load16_u((var15 + ((var13 + (var14 * (var1 + var3))) << 1))) > 1 else 0) | var6)
            var17 = (var17 + 1)
            if (1 if (var17 + 1) != var12 else 0):
                continue
            break  # end loop
        if (1 if (var6 & 1) == 0 else 0):
            break
        break
    if (1 if i32_load(var19 + 264) != 2 else 0):
        break
    if (1 if i32_load(((var0 * 404) + 9568096) + 268) == 1 else 0):
        i32_store(var6 + 52, 1)
        break
    if (1 if i32_load(38964) != var0 else 0):
        break
    i32_store((var11 + (var7 * 132)) + 80, ((D(12) * 10) + 10))
    if (1 if i32_load8_u(9147152) == 0 else 0):
        func240(var21, 500, var18)
        break
    i32_store((var11 + (var7 * 132)) + 32, -1)
    var0 = i32_load(((var0 * 404) + 9568096) + 280)
    if i32_load(((var0 * 404) + 9568096) + 280):
        var2 = (var20 + (var16 * 286704))
        var1 = (i32_load(var2 + 283976) + var0)
        i32_store((var20 + (var16 * 286704)) + 283976, (i32_load(var2 + 283976) + var0))
        if (1 if var0 < 0 else 0):
            i32_store8(var2 + 286700, 1)
        var0 = (var2 + 281748)
        if (1 if i32_load((var2 + 281748)) >= var1 else 0):
            break
        i32_store(var0, var1)
        break
    if (1 if i32_load(var19 + 264) != 1 else 0):
        break
    if var5:
        break
    i32_store((var11 + (var7 * 132)) + 88, i32_load(9142848))
    return var7


# ==========================================================
# $func126
# ==========================================================
def func126(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    var13 = 0.0
    var14 = 0.0
    var15 = 0.0
    var16 = 0.0
    var17 = 0.0
    var18 = 0.0
    var19 = 0.0
    var20 = 0.0
    var10 = ((var1 - 4) + (var3 // -2))
    var11 = (((var2 // -2) + var0) - 4)
    while True:  # loop $label5
        var0 = i32_load(38448)
        var8 = i32_load(i32_load(((i32_load(38448) * 72) + 9263856)) + 20)
        var1 = i32_load(9147320)
        var6 = ((i32_load(9147320) << 11) ^ var1)
        var1 = i32_load(9147312)
        var7 = i32_load(9147324)
        var7 = ((i32_load(9147324) << 11) ^ var7)
        var7 = (((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var7) & 0xFFFFFFFF) >> 8)) ^ var1) ^ var7)
        var6 = (((((((i32_load(9147320) << 11) ^ var1) & 0xFFFFFFFF) >> 8) ^ (((((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var7) & 0xFFFFFFFF) >> 8)) ^ var1) ^ var7) & 0xFFFFFFFF) >> 19)) ^ var6) ^ var7)
        i32_store(9147324, (((((((i32_load(9147320) << 11) ^ var1) & 0xFFFFFFFF) >> 8) ^ (((((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var7) & 0xFFFFFFFF) >> 8)) ^ var1) ^ var7) & 0xFFFFFFFF) >> 19)) ^ var6) ^ var7))
        var5 = i32_load(9147316)
        var5 = ((i32_load(9147316) << 11) ^ var5)
        var5 = (((((((i32_load(9147316) << 11) ^ var5) & 0xFFFFFFFF) >> 8) ^ ((var6 & 0xFFFFFFFF) >> 19)) ^ var5) ^ var6)
        i32_store(9147320, (((((((i32_load(9147316) << 11) ^ var5) & 0xFFFFFFFF) >> 8) ^ ((var6 & 0xFFFFFFFF) >> 19)) ^ var5) ^ var6))
        var1 = (var1 ^ (var1 << 11))
        var1 = ((((((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var5 & 0xFFFFFFFF) >> 19)) ^ var1) ^ var5)
        i32_store(9147316, ((((((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var5 & 0xFFFFFFFF) >> 19)) ^ var1) ^ var5))
        var9 = ((var7 << 11) ^ var7)
        var9 = (((((((var7 << 11) ^ var7) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var9) ^ var1)
        i32_store(9147312, (((((((var7 << 11) ^ var7) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var9) ^ var1))
        var1 = ((var10 + (var1 % var3)) + (var9 & 7))
        var6 = ((var11 + (var6 % var2)) + (var5 & 7))
        var7 = ((var7 % (var8 - 3)) + 3)
        if (1 if var4 == 0 else 0):
            break
        var8 = i32_load(9142416)
        var5 = i32_load(9142416)
        if (1 if var8 == 0 else 0):
            var5 = (i32_load(41092) if i32_load8_u(9147210) else (i32_load(9142892) - 1))
        var15 = (6.28318548 / float((4 if (1 if var5 < 3 else 0) else (var5 << (var5 & 1)))))
        var1 = ((i32_load(9142440) & 0xFFFFFFFF) >> 1)
        var5 = (var1 - ((i32_load(9142440) & 0xFFFFFFFF) >> 1))
        var6 = (var6 - var1)
        var13 = f32(func262(float((var1 - ((i32_load(9142440) & 0xFFFFFFFF) >> 1))), float((var6 - var1))))
        if (1 if (6.28318548 / float((4 if (1 if var5 < 3 else 0) else (var5 << (var5 & 1))))) < f32(func262(float((var1 - ((i32_load(9142440) & 0xFFFFFFFF) >> 1))), float((var6 - var1)))) else 0):
            break
        if (1 if var13 < 0.0 else 0):
            break
        var16 = f32(math.sqrt(float(((var6 * var6) + (var5 * var5)))))
        if (1 if f32(math.sqrt(float(((var6 * var6) + (var5 * var5))))) >= float(var1) else 0):
            break
        var17 = (var15 - var13)
        var1 = ((var0 * 404) + 9568096)
        var6 = (var7 & 255)
        var5 = 0
        while True:  # loop $label4
            if (1 if var8 == 0 else 0):
                var8 = (i32_load(41092) if i32_load8_u(9147210) else (i32_load(9142892) - 1))
            if (1 if var5 >= (4 if (1 if var8 < 3 else 0) else (var8 << (var8 & 1))) else 0):
                break
            var14 = ((var15 * float(var5)) + (var17 if (var5 & 1) else var13))
            var18 = func48(((var15 * float(var5)) + (var17 if (var5 & 1) else var13)))
            # Unknown: f64.convert_i32_u []
            # Unknown: f64.convert_i32_u []
            var19 = ((i32_load(9142440) & 0xFFFFFFFF) >> 1)
            var20 = (((0.5 - (i32_load(var1 + 220) * 0.5)) + float((var18 * var16))) + ((i32_load(9142440) & 0xFFFFFFFF) >> 1))
            if (1 if abs((((0.5 - (i32_load(var1 + 220) * 0.5)) + float((var18 * var16))) + ((i32_load(9142440) & 0xFFFFFFFF) >> 1))) < 2147483648.0 else 0):
                break
            var7 = -2147483648
            var14 = func49(var14)
            # Unknown: f64.convert_i32_u []
            var19 = (((0.5 - (i32_load(var1 + 216) * 0.5)) + float((var14 * var16))) + var19)
            if (1 if abs((((0.5 - (i32_load(var1 + 216) * 0.5)) + float((var14 * var16))) + var19)) < 2147483648.0 else 0):
                break
            var5 = (var5 + 1)
            var8 = i32_load(9142416)
            continue
            break  # end loop
        raise RuntimeError('unreachable')
        var12 = (var12 + 1)
        if (1 if (var12 + 1) != 55 else 0):
            continue
        break  # end loop
    return var0

