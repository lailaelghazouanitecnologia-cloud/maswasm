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
# $sc
# Export: sc
# ==========================================================
def sc(var0):
    """Export: sc"""
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
    var50 = 0
    var51 = 0
    var52 = 0
    var12 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    if (1 if var0 == 0 else 0):
        func45()
    if i32_load8_u(9147152):
        i32_store(9147132, i32_load8_u(9216060))
    if i32_load8_u(9142917):
        i32_store(i32_load(9142424) + 48, i32_load(9142832))
    var9 = i32_load(9142892)
    var31 = (i32_load(9142892) * 3020)
    var34 = i32_load(9681936)
    var35 = (i32_load(i32_load(9681936) + 8) * 3)
    var17 = (((i32_load(i32_load(9681936) + 8) * 3) & 0xFFFFFFFF) >> 2)
    var21 = i32_load(9142440)
    var11 = (i32_load(9142440) * var21)
    var25 = ((((i32_load(9142440) * var21) & 0xFFFFFFFF) >> 2) + 1)
    var7 = i32_load(9142848)
    var26 = i32_load(9215892)
    var10 = (var9 * var9)
    var36 = i32_load(9671136)
    var22 = i32_load(9142912)
    var27 = i32_load(9684484)
    var28 = i32_load(9684468)
    var29 = i32_load(9684452)
    var30 = (i32_load(9684484) + (i32_load(9684468) + i32_load(9684452)))
    var13 = i32_load(9147132)
    if i32_load(9147132):
        break
    if (1 if var7 == 0 else 0):
        break
    if (1 if (i32_load(i32_load(9142424) + 48) - 1) > 1 else 0):
        break
    var33 = (((var11 & 0xFFFFFFFF) >> 5) + 1)
    var5 = (var17 - -64)
    var23 = (i32_load(9142912) + ((i32_load(9684484) + (i32_load(9684468) + i32_load(9684452))) + ((((var11 & 0xFFFFFFFF) >> 5) + 1) + (((((var17 - -64) + var31) + var26) + (var10 << 2)) + var25))))
    var24 = i32_load(9142428)
    var3 = i32_load(9568068)
    var32 = i32_load(9568064)
    var14 = ((i32_load(9568068) - i32_load(9568064)) >> 7)
    var39 = (1 if var3 == var32 else 0)
    if (1 if (1 if var3 == var32 else 0) == 0 else 0):
        var15 = (1 if (1 if var14 <= 1 else 0) else var14)
        while True:  # loop $label3
            var3 = (var32 + (var8 << 7))
            var2 = ((var2 + i32_load((var32 + (var8 << 7)) + 104)) + 8)
            var4 = i32_load(var3 + 4)
            var6 = i32_load(var3)
            if (1 if i32_load(var3 + 4) != i32_load(var3) else 0):
                var4 = ((var4 - var6) // 196)
                var19 = (1 if (1 if var4 <= 1 else 0) else ((var4 - var6) // 196))
                var1 = 0
                while True:  # loop $label1
                    var4 = (var6 + (var1 * 196))
                    var2 = ((((((var2 + i32_load((var6 + (var1 * 196)) + 192)) + i32_load(var4 + 56)) + i32_load(var4 + 72)) + i32_load(var4 + 88)) + i32_load(var4 + 104)) + 19)
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != var19 else 0):
                        continue
                    break  # end loop
            var1 = i32_load(var3 + 16)
            var4 = i32_load(var3 + 12)
            if (1 if i32_load(var3 + 16) != i32_load(var3 + 12) else 0):
                var3 = ((var1 - var4) // 196)
                var6 = (1 if (1 if var3 <= 1 else 0) else ((var1 - var4) // 196))
                var1 = 0
                while True:  # loop $label2
                    var3 = (var4 + (var1 * 196))
                    var2 = ((((((var2 + i32_load((var4 + (var1 * 196)) + 192)) + i32_load(var3 + 56)) + i32_load(var3 + 72)) + i32_load(var3 + 88)) + i32_load(var3 + 104)) + 19)
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != var6 else 0):
                        continue
                    break  # end loop
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != var15 else 0):
                continue
            break  # end loop
    var6 = (var23 + var24)
    var3 = 0
    if (1 if var36 == 0 else 0):
        var8 = 0
        var23 = 0
        break
    var23 = 0
    var15 = i32_load(38448)
    var19 = i32_load(9671128)
    var8 = 0
    var1 = 0
    while True:  # loop $label6
        var4 = (var19 + (var1 * 132))
        if (1 if i32_load8_u((var19 + (var1 * 132)) + 122) == var15 else 0):
            var8 = (var8 + 4)
            break
        var18 = i32_load(var4 + 16)
        if i32_load(var4 + 16):
            var6 = ((var6 + i32_load(var18 + 8)) + 1)
        var18 = i32_load(var4 + 20)
        if i32_load(var4 + 20):
            var6 = ((var6 + i32_load(var18 + 8)) + 1)
        var23 = (var23 + 33)
        var4 = i32_load(var4 + 24)
        if (1 if i32_load(var4 + 24) == 0 else 0):
            break
        var18 = i32_load(var4)
        if i32_load(var4):
            var6 = ((var6 + i32_load(var18 + 8)) + 1)
        var18 = i32_load(var4 + 12)
        if i32_load(var4 + 12):
            var6 = ((var6 + i32_load(var18 + 8)) + 1)
        var18 = i32_load(var4 + 8)
        if i32_load(var4 + 8):
            var6 = ((var6 + i32_load(var18 + 8)) + 1)
        var4 = i32_load(var4 + 4)
        if (1 if i32_load(var4 + 4) == 0 else 0):
            break
        var6 = ((var6 + i32_load(var4 + 8)) + 1)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var36 else 0):
            continue
        break  # end loop
    var15 = (((802 if var13 else ((var9 * 1020) + 802)) * var9) if (var7 | var13) else 0)
    if var9:
        var19 = (var9 + 1)
        var18 = ((1 if var7 == 0 else 0) | (1 if var13 != 0 else 0))
        var37 = i32_load(9561692)
        var1 = 0
        while True:  # loop $label8
            var4 = (var37 + (var1 * 286704))
            var20 = i32_load((var37 + (var1 * 286704)) + 281788)
            if i32_load((var37 + (var1 * 286704)) + 281788):
                var3 = ((var3 + i32_load(var20 + 8)) + 1)
            var20 = i32_load(var4 + 281792)
            if i32_load(var4 + 281792):
                var3 = ((var3 + i32_load(var20 + 8)) + 1)
            var20 = i32_load(var4 + 281796)
            if i32_load(var4 + 281796):
                var3 = ((var3 + i32_load(var20 + 8)) + 1)
            var20 = i32_load(var4 + 286680)
            if i32_load(var4 + 286680):
                var3 = ((var3 + i32_load(var20 + 8)) + 1)
            var20 = (var19 if i32_load(var4 + 281800) else 0)
            if var18:
                break
            var4 = i32_load((var4 + 278572))
            if (1 if i32_load((var4 + 278572)) == 0 else 0):
                break
            var15 = ((var15 + i32_load(var4 + 8)) + 1)
            var3 = (var3 + var20)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var9 else 0):
                continue
            break  # end loop
    var1 = 0
    var18 = (((((var2 + var6) + var8) + var23) + var3) + var15)
    var37 = ((((((var2 + var6) + var8) + var23) + var3) + var15) << 2)
    var3 = (-1 if (1 if var18 > 1073741823 else 0) else ((((((var2 + var6) + var8) + var23) + var3) + var15) << 2))
    var4 = func26((-1 if (1 if var18 > 1073741823 else 0) else ((((((var2 + var6) + var8) + var23) + var3) + var15) << 2)))
    # Unknown: memory.fill []
    var3 = i32_load(9142872)
    var6 = i32_load(59168)
    i32_store(var4 + 4, var17)
    i32_store(var4, var6)
    var6 = i32_load8_u(9147208)
    i32_store(var4 + 24, var22)
    i32_store(var4 + 20, var27)
    i32_store(var4 + 16, var28)
    i32_store(var4 + 12, var29)
    i32_store(var4 + 8, var6)
    i32_store(var4 + 28, (0 if var13 else i32_load(9142952)))
    var6 = i32_load(9142956)
    i32_store(var4 + 40, var26)
    i32_store(var4 + 36, var9)
    i32_store(var4 + 32, (0 if var13 else var6))
    var9 = i32_load(9163776)
    i32_store(var4 + 68, (0 if var13 else var3))
    i32_store(var4 + 64, var36)
    i32_store(var4 + 60, var23)
    i32_store(var4 + 56, var8)
    i32_store(var4 + 52, var7)
    i32_store(var4 + 48, var21)
    i32_store(var4 + 44, (0 if var13 else var9))
    var3 = i32_load(9561752)
    i32_store(var4 + 76, var2)
    i32_store(var4 + 72, var3)
    var21 = i32_load(9142424)
    var3 = i32_load(i32_load(9142424) + 48)
    i32_store(var4 + 84, var24)
    i32_store(var4 + 80, var3)
    i32_store(var4 + 88, i32_load(9684364))
    i32_store(var4 + 92, i32_load(9684368))
    i32_store(var4 + 96, i32_load(9684372))
    f32_store(var4 + 100, f32_load(9684340))
    f32_store(var4 + 104, f32_load(9684344))
    f32_store(var4 + 108, f32_load(9684348))
    f32_store(var4 + 112, f32_load(9684352))
    f32_store(var4 + 116, f32_load(9684356))
    f32_store(var4 + 120, f32_load(9684360))
    i32_store(var4 + 124, i32_load8_u(9147209))
    i32_store(var4 + 128, i32_load(9147312))
    i32_store(var4 + 132, i32_load(9147316))
    i32_store(var4 + 136, i32_load(9147320))
    var3 = i32_load(9147324)
    i32_store(var4 + 152, var31)
    i32_store(var4 + 148, var13)
    i32_store(var4 + 144, var15)
    i32_store(var4 + 140, var3)
    var20 = (var5 + var30)
    var25 = (var2 + (var5 + var30))
    var2 = (var24 + (var2 + (var5 + var30)))
    var24 = (var25 + (var24 + (var2 + (var5 + var30))))
    var27 = ((var25 + (var24 + (var2 + (var5 + var30)))) + var10)
    var28 = (((var25 + (var24 + (var2 + (var5 + var30)))) + var10) + var10)
    var29 = ((((var25 + (var24 + (var2 + (var5 + var30)))) + var10) + var10) + var10)
    var30 = (((((var25 + (var24 + (var2 + (var5 + var30)))) + var10) + var10) + var10) + var10)
    var19 = ((((((var25 + (var24 + (var2 + (var5 + var30)))) + var10) + var10) + var10) + var10) + var26)
    var22 = (var22 + ((((((var25 + (var24 + (var2 + (var5 + var30)))) + var10) + var10) + var10) + var10) + var26))
    var9 = ((var22 + ((((((var25 + (var24 + (var2 + (var5 + var30)))) + var10) + var10) + var10) + var10) + var26)) + var33)
    var40 = (var31 + ((var22 + ((((((var25 + (var24 + (var2 + (var5 + var30)))) + var10) + var10) + var10) + var10) + var26)) + var33))
    var31 = (var8 + (var31 + ((var22 + ((((((var25 + (var24 + (var2 + (var5 + var30)))) + var10) + var10) + var10) + var10) + var26)) + var33)))
    var3 = ((var8 + (var31 + ((var22 + ((((((var25 + (var24 + (var2 + (var5 + var30)))) + var10) + var10) + var10) + var10) + var26)) + var33))) + var23)
    i32_store(var12 + 28, (var15 + ((var8 + (var31 + ((var22 + ((((((var25 + (var24 + (var2 + (var5 + var30)))) + var10) + var10) + var10) + var10) + var26)) + var33))) + var23)))
    if (1 if var11 == 0 else 0):
        break
    var2 = (var4 + (var2 << 2))
    var6 = i32_load(9147288)
    if (1 if var11 >= 4 else 0):
        var8 = (var11 & -4)
        var7 = 0
        while True:  # loop $label10
            var16 = i32_load8_s((var1 + var6))
            i32_store8((var1 + var2), (((i32_load8_s((var1 + var6)) & 0xFFFFFFFF) >> 7) ^ var16))
            var16 = (var1 | 1)
            var16 = i32_load8_s((var6 + var16))
            i32_store8((var2 + (var1 | 1)), (((i32_load8_s((var6 + var16)) & 0xFFFFFFFF) >> 7) ^ var16))
            var16 = (var1 | 2)
            var16 = i32_load8_s((var6 + var16))
            i32_store8((var2 + (var1 | 2)), (((i32_load8_s((var6 + var16)) & 0xFFFFFFFF) >> 7) ^ var16))
            var16 = (var1 | 3)
            var16 = i32_load8_s((var6 + var16))
            i32_store8((var2 + (var1 | 3)), (((i32_load8_s((var6 + var16)) & 0xFFFFFFFF) >> 7) ^ var16))
            var1 = (var1 + 4)
            var7 = (var7 + 4)
            if (1 if (var7 + 4) != var8 else 0):
                continue
            break  # end loop
    var8 = (var11 & 3)
    if (1 if (var11 & 3) == 0 else 0):
        break
    var7 = 0
    while True:  # loop $label11
        var16 = i32_load8_s((var1 + var6))
        i32_store8((var1 + var2), (((i32_load8_s((var1 + var6)) & 0xFFFFFFFF) >> 7) ^ var16))
        var1 = (var1 + 1)
        var7 = (var7 + 1)
        if (1 if (var7 + 1) != var8 else 0):
            continue
        break  # end loop
    if (1 if var33 == 0 else 0):
        break
    var1 = i32_load(9147376)
    if (1 if i32_load(9147376) == 0 else 0):
        break
    if var13:
        break
    if (1 if var11 == 0 else 0):
        break
    var6 = (var4 + (var22 << 2))
    var2 = 0
    if (1 if var11 != 1 else 0):
        var13 = (var11 & -2)
        var7 = 0
        while True:  # loop $label13
            var8 = (var6 + (((var2 & 0xFFFFFFFF) >> 3) & 536870908))
            var22 = (i32_load(var8) | ((1 if i32_load16_u((var1 + (var2 << 1))) != 0 else 0) << (var2 & 30)))
            i32_store((var6 + (((var2 & 0xFFFFFFFF) >> 3) & 536870908)), (i32_load(var8) | ((1 if i32_load16_u((var1 + (var2 << 1))) != 0 else 0) << (var2 & 30))))
            var8 = (var2 | 1)
            i32_store(var8, (((1 if i32_load16_u((var1 + ((var2 | 1) << 1))) != 0 else 0) << var8) | var22))
            var2 = (var2 + 2)
            var7 = (var7 + 2)
            if (1 if (var7 + 2) != var13 else 0):
                continue
            break  # end loop
    if (1 if (var11 & 1) == 0 else 0):
        break
    var6 = (var6 + (((var2 & 0xFFFFFFFF) >> 3) & 536870908))
    i32_store((var6 + (((var2 & 0xFFFFFFFF) >> 3) & 536870908)), (i32_load(var6) | ((1 if i32_load16_u((var1 + (var2 << 1))) != 0 else 0) << var2)))
    if (1 if var35 >= 4 else 0):
        var7 = i32_load(var34)
        var2 = 0
        while True:  # loop $label14
            var6 = (var2 << 2)
            var1 = ((var2 << 2) + var4)
            var6 = (var7 + (((var6 & 0xFFFFFFFF) // 3) << 2))
            i32_store(((var2 << 2) + var4) + 256, i32_load((var7 + (((var6 & 0xFFFFFFFF) // 3) << 2))))
            i32_store(var1 + 260, i32_load(var6 + 4))
            i32_store(var1 + 264, i32_load(var6 + 8))
            var2 = (var2 + 3)
            if (1 if (var2 + 3) < var17 else 0):
                continue
            break  # end loop
    var2 = i32_load(9684452)
    if (1 if i32_load(9684452) == 0 else 0):
        break
    var13 = (var2 & 3)
    var8 = 0
    var1 = i32_load(9684444)
    if (1 if var2 < 4 else 0):
        var2 = 0
        break
    var17 = (var2 & -4)
    var2 = 0
    var7 = 0
    while True:  # loop $label17
        var6 = (var4 + (var5 << 2))
        var11 = (var2 << 2)
        i32_store((var4 + (var5 << 2)), i32_load((var1 + (var2 << 2))))
        i32_store(var6 + 4, i32_load((var1 + (var11 | 4))))
        i32_store(var6 + 8, i32_load((var1 + (var11 | 8))))
        i32_store(var6 + 12, i32_load((var1 + (var11 | 12))))
        var2 = (var2 + 4)
        var5 = (var5 + 4)
        var7 = (var7 + 4)
        if (1 if (var7 + 4) != var17 else 0):
            continue
        break  # end loop
    if (1 if var13 == 0 else 0):
        break
    while True:  # loop $label18
        i32_store((var4 + (var5 << 2)), i32_load((var1 + (var2 << 2))))
        var2 = (var2 + 1)
        var5 = (var5 + 1)
        var8 = (var8 + 1)
        if (1 if (var8 + 1) != var13 else 0):
            continue
        break  # end loop
    var2 = i32_load(9684468)
    if (1 if i32_load(9684468) == 0 else 0):
        break
    var13 = (var2 & 3)
    var8 = 0
    var1 = i32_load(9684460)
    if (1 if var2 < 4 else 0):
        var2 = 0
        break
    var17 = (var2 & -4)
    var2 = 0
    var7 = 0
    while True:  # loop $label21
        var6 = (var4 + (var5 << 2))
        var11 = (var2 << 2)
        i32_store((var4 + (var5 << 2)), i32_load((var1 + (var2 << 2))))
        i32_store(var6 + 4, i32_load((var1 + (var11 | 4))))
        i32_store(var6 + 8, i32_load((var1 + (var11 | 8))))
        i32_store(var6 + 12, i32_load((var1 + (var11 | 12))))
        var2 = (var2 + 4)
        var5 = (var5 + 4)
        var7 = (var7 + 4)
        if (1 if (var7 + 4) != var17 else 0):
            continue
        break  # end loop
    if (1 if var13 == 0 else 0):
        break
    while True:  # loop $label22
        i32_store((var4 + (var5 << 2)), i32_load((var1 + (var2 << 2))))
        var2 = (var2 + 1)
        var5 = (var5 + 1)
        var8 = (var8 + 1)
        if (1 if (var8 + 1) != var13 else 0):
            continue
        break  # end loop
    var2 = i32_load(9684484)
    if (1 if i32_load(9684484) == 0 else 0):
        break
    var13 = (var2 & 3)
    var8 = 0
    var1 = i32_load(9684476)
    if (1 if var2 < 4 else 0):
        var2 = 0
        break
    var17 = (var2 & -4)
    var2 = 0
    var7 = 0
    while True:  # loop $label25
        var6 = (var4 + (var5 << 2))
        var11 = (var2 << 2)
        i32_store((var4 + (var5 << 2)), i32_load((var1 + (var2 << 2))))
        i32_store(var6 + 4, i32_load((var1 + (var11 | 4))))
        i32_store(var6 + 8, i32_load((var1 + (var11 | 8))))
        i32_store(var6 + 12, i32_load((var1 + (var11 | 12))))
        var2 = (var2 + 4)
        var5 = (var5 + 4)
        var7 = (var7 + 4)
        if (1 if (var7 + 4) != var17 else 0):
            continue
        break  # end loop
    if (1 if var13 == 0 else 0):
        break
    while True:  # loop $label26
        i32_store((var4 + (var5 << 2)), i32_load((var1 + (var2 << 2))))
        var2 = (var2 + 1)
        var5 = (var5 + 1)
        var8 = (var8 + 1)
        if (1 if (var8 + 1) != var13 else 0):
            continue
        break  # end loop
    i32_store(var12 + 24, var20)
    if (1 if var39 == 0 else 0):
        var14 = (1 if (1 if var14 <= 1 else 0) else var14)
        var13 = 0
        while True:  # loop $label30
            var2 = i32_load(var12 + 24)
            var1 = (var4 + (i32_load(var12 + 24) << 2))
            var8 = (var32 + (var13 << 7))
            var17 = i32_load((var32 + (var13 << 7)) + 4)
            var7 = i32_load(var8)
            i32_store((var4 + (i32_load(var12 + 24) << 2)), ((i32_load((var32 + (var13 << 7)) + 4) - i32_load(var8)) // 196))
            var11 = i32_load(var8 + 16)
            var5 = i32_load(var8 + 12)
            i32_store(var1 + 4, ((i32_load(var8 + 16) - i32_load(var8 + 12)) // 196))
            i32_store(var1 + 8, i32_load(var8 + 104))
            var1 = (var2 + 3)
            if i32_load(var8 + 104):
                var6 = 0
                while True:  # loop $label27
                    i32_store((var4 + (var1 << 2)), i32_load16_u((var8 + (var6 << 1)) + 24))
                    var1 = (var1 + 1)
                    var6 = (var6 + 1)
                    if (1 if (var6 + 1) < i32_load(var8 + 104) else 0):
                        continue
                    break  # end loop
            var2 = (var4 + (var1 << 2))
            i32_store((var4 + (var1 << 2)), i32_load(var8 + 108))
            i32_store(var2 + 4, i32_load(var8 + 112))
            i32_store(var2 + 8, i32_load(var8 + 116))
            i32_store(var2 + 12, i32_load(var8 + 120))
            var6 = i32_load(var8 + 124)
            i32_store(var12 + 24, (var1 + 5))
            i32_store(var2 + 16, var6)
            var1 = 0
            var2 = 0
            if (1 if var7 != var17 else 0):
                while True:  # loop $label28
                    func382((var7 + (var1 * 196)), var4, (var12 + 24))
                    var1 = (var1 + 1)
                    var7 = i32_load(var8)
                    if (1 if (var1 + 1) < ((i32_load(var8 + 4) - i32_load(var8)) // 196) else 0):
                        continue
                    break  # end loop
                var11 = i32_load(var8 + 16)
                var5 = i32_load(var8 + 12)
            if (1 if var5 != var11 else 0):
                while True:  # loop $label29
                    func382((var5 + (var2 * 196)), var4, (var12 + 24))
                    var2 = (var2 + 1)
                    var5 = i32_load(var8 + 12)
                    if (1 if (var2 + 1) < ((i32_load(var8 + 16) - i32_load(var8 + 12)) // 196) else 0):
                        continue
                    break  # end loop
            var13 = (var13 + 1)
            if (1 if (var13 + 1) != var14 else 0):
                continue
            break  # end loop
    if (1 if var15 == 0 else 0):
        break
    var8 = 0
    var17 = i32_load(9142892)
    if (1 if i32_load(9142892) == 0 else 0):
        break
    var1 = (var17 * 255)
    var1 = (1 if (1 if var1 <= 1 else 0) else (var17 * 255))
    var13 = ((1 if (1 if var1 <= 1 else 0) else (var17 * 255)) & -4)
    var11 = (var1 & 3)
    var33 = i32_load(9147132)
    var32 = i32_load(9561692)
    var34 = (var1 - 1)
    var35 = (1 if (var1 - 1) > 2 else 0)
    while True:  # loop $label45
        if var33:
            break
        var15 = (var32 + (var8 * 286704))
        var6 = i32_load((var32 + (var8 * 286704)) + 278556)
        var7 = 0
        var2 = 0
        var1 = 0
        if var35:
            while True:  # loop $label33
                var14 = (var4 + (var3 << 2))
                var5 = (var2 << 2)
                i32_store((var4 + (var3 << 2)), i32_load((var6 + (var2 << 2))))
                i32_store(var14 + 4, i32_load((var6 + (var5 | 4))))
                i32_store(var14 + 8, i32_load((var6 + (var5 | 8))))
                i32_store(var14 + 12, i32_load((var6 + (var5 | 12))))
                var2 = (var2 + 4)
                var3 = (var3 + 4)
                var1 = (var1 + 4)
                if (1 if (var1 + 4) != var13 else 0):
                    continue
                break  # end loop
        if var11:
            while True:  # loop $label34
                i32_store((var4 + (var3 << 2)), i32_load((var6 + (var2 << 2))))
                var2 = (var2 + 1)
                var3 = (var3 + 1)
                var7 = (var7 + 1)
                if (1 if (var7 + 1) != var11 else 0):
                    continue
                break  # end loop
        var6 = i32_load((var15 + 278560))
        var7 = 0
        var2 = 0
        var1 = 0
        var22 = (1 if var34 < 3 else 0)
        if (1 if (1 if var34 < 3 else 0) == 0 else 0):
            while True:  # loop $label35
                var14 = (var4 + (var3 << 2))
                var5 = (var2 << 2)
                i32_store((var4 + (var3 << 2)), i32_load((var6 + (var2 << 2))))
                i32_store(var14 + 4, i32_load((var6 + (var5 | 4))))
                i32_store(var14 + 8, i32_load((var6 + (var5 | 8))))
                i32_store(var14 + 12, i32_load((var6 + (var5 | 12))))
                var2 = (var2 + 4)
                var3 = (var3 + 4)
                var1 = (var1 + 4)
                if (1 if (var1 + 4) != var13 else 0):
                    continue
                break  # end loop
        if var11:
            while True:  # loop $label36
                i32_store((var4 + (var3 << 2)), i32_load((var6 + (var2 << 2))))
                var2 = (var2 + 1)
                var3 = (var3 + 1)
                var7 = (var7 + 1)
                if (1 if (var7 + 1) != var11 else 0):
                    continue
                break  # end loop
        var6 = i32_load((var15 + 278564))
        var7 = 0
        var2 = 0
        var1 = 0
        if (1 if var22 == 0 else 0):
            while True:  # loop $label37
                var14 = (var4 + (var3 << 2))
                var5 = (var2 << 2)
                i32_store((var4 + (var3 << 2)), i32_load((var6 + (var2 << 2))))
                i32_store(var14 + 4, i32_load((var6 + (var5 | 4))))
                i32_store(var14 + 8, i32_load((var6 + (var5 | 8))))
                i32_store(var14 + 12, i32_load((var6 + (var5 | 12))))
                var2 = (var2 + 4)
                var3 = (var3 + 4)
                var1 = (var1 + 4)
                if (1 if (var1 + 4) != var13 else 0):
                    continue
                break  # end loop
        if var11:
            while True:  # loop $label38
                i32_store((var4 + (var3 << 2)), i32_load((var6 + (var2 << 2))))
                var2 = (var2 + 1)
                var3 = (var3 + 1)
                var7 = (var7 + 1)
                if (1 if (var7 + 1) != var11 else 0):
                    continue
                break  # end loop
        var6 = i32_load((var15 + 278568))
        var7 = 0
        var2 = 0
        var1 = 0
        if (1 if var22 == 0 else 0):
            while True:  # loop $label39
                var5 = (var4 + (var3 << 2))
                var14 = (var2 << 2)
                i32_store((var4 + (var3 << 2)), i32_load((var6 + (var2 << 2))))
                i32_store(var5 + 4, i32_load((var6 + (var14 | 4))))
                i32_store(var5 + 8, i32_load((var6 + (var14 | 8))))
                var5 = (var3 + 3)
                i32_store((var4 + ((var3 + 3) << 2)), i32_load((var6 + (var14 | 12))))
                var2 = (var2 + 4)
                var3 = (var3 + 4)
                var1 = (var1 + 4)
                if (1 if (var1 + 4) != var13 else 0):
                    continue
                break  # end loop
        if var11:
            while True:  # loop $label40
                var5 = var3
                i32_store((var4 + (var3 << 2)), i32_load((var6 + (var2 << 2))))
                var2 = (var2 + 1)
                var3 = (var3 + 1)
                var7 = (var7 + 1)
                if (1 if (var7 + 1) != var11 else 0):
                    continue
                break  # end loop
        var1 = i32_load((var15 + 278572))
        i32_store((var4 + (var3 << 2)), i32_load(i32_load((var15 + 278572)) + 8))
        var3 = (var5 + 2)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        var5 = i32_load(var1)
        var2 = 0
        while True:  # loop $label41
            i32_store((var4 + (var3 << 2)), i32_load((var5 + (var2 << 2))))
            var3 = (var3 + 1)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < i32_load(var1 + 8) else 0):
                continue
            break  # end loop
        var1 = 0
        var6 = 0
        while True:  # loop $label42
            var5 = (var4 + (var3 << 2))
            var2 = (var32 + (var8 * 286704))
            var7 = ((var32 + (var8 * 286704)) + (var6 << 2))
            i32_store((var4 + (var3 << 2)), i32_load((((var32 + (var8 * 286704)) + (var6 << 2)) + 278576)))
            i32_store(var5 + 4, i32_load((var7 + 278580)))
            i32_store(var5 + 8, i32_load((var7 + 278584)))
            var3 = (var3 + 3)
            var6 = (var6 + 3)
            if (1 if (var6 + 3) != 255 else 0):
                continue
            break  # end loop
        while True:  # loop $label43
            var5 = (var4 + (var3 << 2))
            var6 = (var2 + (var1 << 2))
            i32_store((var4 + (var3 << 2)), i32_load(((var2 + (var1 << 2)) + 279596)))
            i32_store(var5 + 4, i32_load((var6 + 279600)))
            i32_store(var5 + 8, i32_load((var6 + 279604)))
            var3 = (var3 + 3)
            var1 = (var1 + 3)
            if (1 if (var1 + 3) != 255 else 0):
                continue
            break  # end loop
        var6 = 0
        while True:  # loop $label44
            var5 = var3
            var1 = (var4 + (var3 << 2))
            var3 = (var2 + (var6 << 2))
            i32_store((var4 + (var3 << 2)), i32_load(((var2 + (var6 << 2)) + 280616)))
            i32_store(var1 + 4, i32_load((var3 + 280620)))
            i32_store(var1 + 8, i32_load((var3 + 280624)))
            var3 = (var5 + 3)
            var6 = (var6 + 3)
            if (1 if (var6 + 3) != 255 else 0):
                continue
            break  # end loop
        i32_store((var4 + (var3 << 2)), i32_load((var2 + 281636)))
        i32_store(var1 + 16, i32_load((var2 + 281640)))
        i32_store(var1 + 20, i32_load((var2 + 281644)))
        i32_store(var1 + 24, i32_load((var2 + 281648)))
        i32_store(var1 + 28, i32_load((var2 + 281652)))
        i32_store(var1 + 32, i32_load((var2 + 281656)))
        i32_store(var1 + 36, i32_load((var2 + 281660)))
        i32_store(var1 + 40, i32_load((var2 + 281664)))
        i32_store(var1 + 44, i32_load((var2 + 281668)))
        i32_store(var1 + 48, i32_load((var2 + 281672)))
        i32_store(var1 + 52, i32_load((var2 + 281676)))
        i32_store(var1 + 56, i32_load((var2 + 281680)))
        i32_store(var1 + 60, i32_load((var2 + 281684)))
        i32_store((var1 - -64), i32_load((var2 + 281688)))
        i32_store(var1 + 68, i32_load((var2 + 281692)))
        i32_store(var1 + 72, i32_load((var2 + 281696)))
        i32_store(var1 + 76, i32_load((var2 + 281700)))
        i32_store(var1 + 80, i32_load((var2 + 281704)))
        i32_store(var1 + 84, i32_load((var2 + 281708)))
        i32_store(var1 + 88, i32_load((var2 + 281712)))
        i32_store(var1 + 92, i32_load((var2 + 281716)))
        i32_store(var1 + 96, i32_load((var2 + 281720)))
        i32_store(var1 + 100, i32_load((var2 + 281724)))
        i32_store(var1 + 104, i32_load((var2 + 281728)))
        i32_store(var1 + 108, i32_load((var2 + 281732)))
        i32_store(var1 + 112, i32_load((var2 + 281736)))
        i32_store(var1 + 116, i32_load((var2 + 281740)))
        i32_store(var1 + 120, i32_load((var2 + 281744)))
        i32_store(var1 + 124, i32_load((var2 + 281748)))
        i32_store(var1 + 128, i32_load((var2 + 281752)))
        i32_store(var1 + 132, i32_load((var2 + 281756)))
        i32_store(var1 + 136, i32_load((var2 + 281760)))
        i32_store(var1 + 140, i32_load((var2 + 281764)))
        i32_store(var1 + 144, i32_load((var2 + 281768)))
        i32_store(var1 + 148, i32_load((var2 + 281772)))
        i32_store(var1 + 152, i32_load((var2 + 281776)))
        i32_store(var1 + 156, i32_load((var2 + 281780)))
        var3 = (var5 + 40)
        var8 = (var8 + 1)
        if (1 if (var8 + 1) != var17 else 0):
            continue
        break  # end loop
    var3 = 0
    var5 = i32_load(9142428)
    if (1 if i32_load(9142428) == 0 else 0):
        break
    if (1 if var5 >= 4 else 0):
        var1 = (var5 & -4)
        var2 = 0
        while True:  # loop $label47
            i32_store((var4 + ((var3 + var25) << 2)), i32_load((var21 + (var3 << 2))))
            var6 = (var3 | 1)
            i32_store((var4 + (((var3 | 1) + var25) << 2)), i32_load((var21 + (var6 << 2))))
            var6 = (var3 | 2)
            i32_store((var4 + (((var3 | 2) + var25) << 2)), i32_load((var21 + (var6 << 2))))
            var6 = (var3 | 3)
            i32_store((var4 + (((var3 | 3) + var25) << 2)), i32_load((var21 + (var6 << 2))))
            var3 = (var3 + 4)
            var2 = (var2 + 4)
            if (1 if (var2 + 4) != var1 else 0):
                continue
            break  # end loop
    var5 = (var5 & 3)
    if (1 if (var5 & 3) == 0 else 0):
        break
    var2 = 0
    while True:  # loop $label48
        i32_store((var4 + ((var3 + var25) << 2)), i32_load((var21 + (var3 << 2))))
        var3 = (var3 + 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var5 else 0):
            continue
        break  # end loop
    if (1 if var10 == 0 else 0):
        break
    var1 = 0
    var5 = i32_load(9143004)
    var3 = 0
    if (1 if var10 >= 4 else 0):
        var2 = (var10 & -4)
        var6 = 0
        while True:  # loop $label50
            i32_store((var4 + ((var3 + var24) << 2)), i32_load8_u((var3 + var5)))
            var7 = (var3 | 1)
            i32_store((var4 + (((var3 | 1) + var24) << 2)), i32_load8_u((var5 + var7)))
            var7 = (var3 | 2)
            i32_store((var4 + (((var3 | 2) + var24) << 2)), i32_load8_u((var5 + var7)))
            var7 = (var3 | 3)
            i32_store((var4 + (((var3 | 3) + var24) << 2)), i32_load8_u((var5 + var7)))
            var3 = (var3 + 4)
            var6 = (var6 + 4)
            if (1 if (var6 + 4) != var2 else 0):
                continue
            break  # end loop
    var2 = (var10 & 3)
    if (var10 & 3):
        while True:  # loop $label51
            i32_store((var4 + ((var3 + var24) << 2)), i32_load8_u((var3 + var5)))
            var3 = (var3 + 1)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var2 else 0):
                continue
            break  # end loop
    if (1 if var10 == 0 else 0):
        break
    var1 = 0
    var5 = i32_load(9143008)
    var3 = 0
    if (1 if var10 >= 4 else 0):
        var2 = (var10 & -4)
        var6 = 0
        while True:  # loop $label52
            i32_store((var4 + ((var3 + var27) << 2)), i32_load8_u((var3 + var5)))
            var7 = (var3 | 1)
            i32_store((var4 + (((var3 | 1) + var27) << 2)), i32_load8_u((var5 + var7)))
            var7 = (var3 | 2)
            i32_store((var4 + (((var3 | 2) + var27) << 2)), i32_load8_u((var5 + var7)))
            var7 = (var3 | 3)
            i32_store((var4 + (((var3 | 3) + var27) << 2)), i32_load8_u((var5 + var7)))
            var3 = (var3 + 4)
            var6 = (var6 + 4)
            if (1 if (var6 + 4) != var2 else 0):
                continue
            break  # end loop
    var2 = (var10 & 3)
    if (var10 & 3):
        while True:  # loop $label53
            i32_store((var4 + ((var3 + var27) << 2)), i32_load8_u((var3 + var5)))
            var3 = (var3 + 1)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var2 else 0):
                continue
            break  # end loop
    if (1 if var10 == 0 else 0):
        break
    var1 = 0
    var5 = i32_load(9143012)
    var3 = 0
    if (1 if var10 >= 4 else 0):
        var2 = (var10 & -4)
        var6 = 0
        while True:  # loop $label54
            i32_store((var4 + ((var3 + var28) << 2)), i32_load8_u((var3 + var5)))
            var7 = (var3 | 1)
            i32_store((var4 + (((var3 | 1) + var28) << 2)), i32_load8_u((var5 + var7)))
            var7 = (var3 | 2)
            i32_store((var4 + (((var3 | 2) + var28) << 2)), i32_load8_u((var5 + var7)))
            var7 = (var3 | 3)
            i32_store((var4 + (((var3 | 3) + var28) << 2)), i32_load8_u((var5 + var7)))
            var3 = (var3 + 4)
            var6 = (var6 + 4)
            if (1 if (var6 + 4) != var2 else 0):
                continue
            break  # end loop
    var2 = (var10 & 3)
    if (var10 & 3):
        while True:  # loop $label55
            i32_store((var4 + ((var3 + var28) << 2)), i32_load8_u((var3 + var5)))
            var3 = (var3 + 1)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var2 else 0):
                continue
            break  # end loop
    if (1 if var10 == 0 else 0):
        break
    var1 = 0
    var5 = i32_load(9143016)
    var3 = 0
    if (1 if var10 >= 4 else 0):
        var2 = (var10 & -4)
        var6 = 0
        while True:  # loop $label56
            i32_store((var4 + ((var3 + var29) << 2)), i32_load8_u((var3 + var5)))
            var7 = (var3 | 1)
            i32_store((var4 + (((var3 | 1) + var29) << 2)), i32_load8_u((var5 + var7)))
            var7 = (var3 | 2)
            i32_store((var4 + (((var3 | 2) + var29) << 2)), i32_load8_u((var5 + var7)))
            var7 = (var3 | 3)
            i32_store((var4 + (((var3 | 3) + var29) << 2)), i32_load8_u((var5 + var7)))
            var3 = (var3 + 4)
            var6 = (var6 + 4)
            if (1 if (var6 + 4) != var2 else 0):
                continue
            break  # end loop
    var2 = (var10 & 3)
    if (1 if (var10 & 3) == 0 else 0):
        break
    while True:  # loop $label57
        i32_store((var4 + ((var3 + var29) << 2)), i32_load8_u((var3 + var5)))
        var3 = (var3 + 1)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var2 else 0):
            continue
        break  # end loop
    if (1 if var26 == 0 else 0):
        break
    var1 = 0
    var5 = i32_load(9215884)
    var3 = 0
    if (1 if var26 >= 4 else 0):
        var2 = (var26 & -4)
        var6 = 0
        while True:  # loop $label59
            i32_store((var4 + ((var3 + var30) << 2)), i32_load((var5 + (var3 << 2))))
            var7 = (var3 | 1)
            i32_store((var4 + (((var3 | 1) + var30) << 2)), i32_load((var5 + (var7 << 2))))
            var7 = (var3 | 2)
            i32_store((var4 + (((var3 | 2) + var30) << 2)), i32_load((var5 + (var7 << 2))))
            var7 = (var3 | 3)
            i32_store((var4 + (((var3 | 3) + var30) << 2)), i32_load((var5 + (var7 << 2))))
            var3 = (var3 + 4)
            var6 = (var6 + 4)
            if (1 if (var6 + 4) != var2 else 0):
                continue
            break  # end loop
    var2 = (var26 & 3)
    if (1 if (var26 & 3) == 0 else 0):
        break
    while True:  # loop $label60
        i32_store((var4 + ((var3 + var30) << 2)), i32_load((var5 + (var3 << 2))))
        var3 = (var3 + 1)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var2 else 0):
            continue
        break  # end loop
    var3 = 0
    var2 = i32_load(9142912)
    if (1 if i32_load(9142912) == 0 else 0):
        break
    var5 = i32_load(9142908)
    if (1 if var2 >= 4 else 0):
        var6 = (var2 & -4)
        var1 = 0
        while True:  # loop $label62
            i32_store((var4 + ((var3 + var19) << 2)), i32_load((var5 + (var3 << 2))))
            var7 = (var3 | 1)
            i32_store((var4 + (((var3 | 1) + var19) << 2)), i32_load((var5 + (var7 << 2))))
            var7 = (var3 | 2)
            i32_store((var4 + (((var3 | 2) + var19) << 2)), i32_load((var5 + (var7 << 2))))
            var7 = (var3 | 3)
            i32_store((var4 + (((var3 | 3) + var19) << 2)), i32_load((var5 + (var7 << 2))))
            var3 = (var3 + 4)
            var1 = (var1 + 4)
            if (1 if (var1 + 4) != var6 else 0):
                continue
            break  # end loop
    var2 = (var2 & 3)
    if (1 if (var2 & 3) == 0 else 0):
        break
    var1 = 0
    while True:  # loop $label63
        i32_store((var4 + ((var3 + var19) << 2)), i32_load((var5 + (var3 << 2))))
        var3 = (var3 + 1)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var2 else 0):
            continue
        break  # end loop
    if i32_load8_u(9142917):
        i32_store(var21 + 48, 0)
    var6 = 0
    var7 = 0
    if i32_load(9142892):
        var3 = var9
        while True:  # loop $label78
            var9 = (var4 + ((var3 + var6) << 2))
            var1 = (i32_load(9561692) + (var7 * 286704))
            i32_store((var4 + ((var3 + var6) << 2)), i32_load((i32_load(9561692) + (var7 * 286704))))
            i32_store(var9 + 4, i32_load(var1 + 4))
            i32_store(var9 + 8, i32_load(var1 + 8))
            i32_store(var9 + 12, i32_load(var1 + 12))
            i32_store(var9 + 16, i32_load(var1 + 16))
            i32_store(var9 + 20, i32_load(var1 + 20))
            i32_store(var9 + 24, i32_load(var1 + 24))
            i32_store(var9 + 28, i32_load(var1 + 28))
            i32_store(var9 + 32, i32_load(var1 + 32))
            i32_store(var9 + 36, i32_load(var1 + 36))
            var2 = i32_load(var1 + 281788)
            if (1 if i32_load(var1 + 281788) == 0 else 0):
                break
            i32_store(var9 + 40, i32_load(var12 + 28))
            var5 = i32_load(var2 + 8)
            var8 = i32_load(var12 + 28)
            i32_store(var12 + 28, (i32_load(var12 + 28) + 1))
            i32_store((var4 + (var8 << 2)), var5)
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            var8 = i32_load(var2)
            var5 = 0
            while True:  # loop $label65
                var10 = i32_load((var8 + (var5 << 2)))
                var11 = i32_load(var12 + 28)
                i32_store(var12 + 28, (i32_load(var12 + 28) + 1))
                i32_store((var4 + (var11 << 2)), var10)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) < i32_load(var2 + 8) else 0):
                    continue
                break  # end loop
            var2 = i32_load(var1 + 281792)
            if (1 if i32_load(var1 + 281792) == 0 else 0):
                break
            i32_store(var9 + 44, i32_load(var12 + 28))
            var5 = i32_load(var2 + 8)
            var8 = i32_load(var12 + 28)
            i32_store(var12 + 28, (i32_load(var12 + 28) + 1))
            i32_store((var4 + (var8 << 2)), var5)
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            var8 = i32_load(var2)
            var5 = 0
            while True:  # loop $label67
                var10 = i32_load((var8 + (var5 << 2)))
                var11 = i32_load(var12 + 28)
                i32_store(var12 + 28, (i32_load(var12 + 28) + 1))
                i32_store((var4 + (var11 << 2)), var10)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) < i32_load(var2 + 8) else 0):
                    continue
                break  # end loop
            var2 = i32_load(var1 + 281796)
            if (1 if i32_load(var1 + 281796) == 0 else 0):
                break
            i32_store(var9 + 48, i32_load(var12 + 28))
            var5 = i32_load(var2 + 8)
            var8 = i32_load(var12 + 28)
            i32_store(var12 + 28, (i32_load(var12 + 28) + 1))
            i32_store((var4 + (var8 << 2)), var5)
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            var8 = i32_load(var2)
            var5 = 0
            while True:  # loop $label69
                var10 = i32_load((var8 + (var5 << 2)))
                var11 = i32_load(var12 + 28)
                i32_store(var12 + 28, (i32_load(var12 + 28) + 1))
                i32_store((var4 + (var11 << 2)), var10)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) < i32_load(var2 + 8) else 0):
                    continue
                break  # end loop
            var2 = i32_load(var1 + 286680)
            if (1 if i32_load(var1 + 286680) == 0 else 0):
                break
            i32_store(var9 + 52, i32_load(var12 + 28))
            var5 = i32_load(var2 + 8)
            var9 = i32_load(var12 + 28)
            i32_store(var12 + 28, (i32_load(var12 + 28) + 1))
            i32_store((var4 + (var9 << 2)), var5)
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            var9 = i32_load(var2)
            var5 = 0
            while True:  # loop $label71
                var8 = i32_load((var9 + (var5 << 2)))
                var10 = i32_load(var12 + 28)
                i32_store(var12 + 28, (i32_load(var12 + 28) + 1))
                i32_store((var4 + (var10 << 2)), var8)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) < i32_load(var2 + 8) else 0):
                    continue
                break  # end loop
            var5 = (var6 + 14)
            var6 = 0
            while True:  # loop $label72
                var9 = var5
                var5 = (var4 + ((var5 + var3) << 2))
                var2 = (var1 + (var6 * 36))
                i32_store((var4 + ((var5 + var3) << 2)), i32_load(((var1 + (var6 * 36)) + 269376)))
                i32_store(var5 + 4, i32_load((var2 + 269380)))
                i32_store(var5 + 8, i32_load((var2 + 269384)))
                i32_store(var5 + 12, i32_load((var2 + 269388)))
                i32_store(var5 + 16, i32_load((var2 + 269392)))
                i32_store(var5 + 20, i32_load((var2 + 269396)))
                i32_store(var5 + 24, i32_load((var2 + 269400)))
                i32_store(var5 + 28, i32_load((var2 + 269404)))
                i32_store(var5 + 32, i32_load((var2 + 269408)))
                var5 = (var9 + 9)
                var6 = (var6 + 1)
                if (1 if (var6 + 1) != 255 else 0):
                    continue
                break  # end loop
            var6 = (var3 + var5)
            var5 = 0
            while True:  # loop $label73
                var2 = (var1 + 281808)
                i32_store((var4 + ((var5 + var6) << 2)), i32_load(((var1 + 281808) + (var5 << 2))))
                var8 = (var5 + 1)
                i32_store((var4 + ((var6 + (var5 + 1)) << 2)), i32_load((var2 + (var8 << 2))))
                var8 = (var5 + 2)
                i32_store((var4 + ((var6 + (var5 + 2)) << 2)), i32_load((var2 + (var8 << 2))))
                var5 = (var5 + 3)
                if (1 if (var5 + 3) != 255 else 0):
                    continue
                break  # end loop
            var2 = (var6 + 255)
            var5 = 0
            while True:  # loop $label74
                var8 = (var1 + 282828)
                i32_store((var4 + ((var2 + var5) << 2)), i32_load(((var1 + 282828) + (var5 << 2))))
                var10 = (var5 + 1)
                i32_store((var4 + ((var2 + (var5 + 1)) << 2)), i32_load((var8 + (var10 << 2))))
                var10 = (var5 + 2)
                i32_store((var4 + ((var2 + (var5 + 2)) << 2)), i32_load((var8 + (var10 << 2))))
                var5 = (var5 + 3)
                if (1 if (var5 + 3) != 255 else 0):
                    continue
                break  # end loop
            var2 = ((var6 << 2) + var4)
            i32_store((((var6 << 2) + var4) + 2040), i32_load(var1 + 283848))
            i32_store((var2 + 2044), i32_load((var1 + 283852)))
            i32_store((var2 + 2048), i32_load((var1 + 283856)))
            i32_store((var2 + 2052), i32_load((var1 + 283860)))
            i32_store((var2 + 2056), i32_load(var1 + 283864))
            if i32_load8_u(9147152):
                func425(var1)
            var5 = 0
            if i32_load(9147132):
            else:
            i32_store(0, i32_load(var1 + 283872))
            if i32_load(9147132):
            else:
            i32_store(0, i32_load(var1 + 283876))
            i32_store((var2 + 2068), i32_load(var1 + 283960))
            i32_store((var2 + 2072), i32_load(var1 + 283968))
            i32_store((var2 + 2076), (i32_load16_u(var1 + 283972) | (i32_load8_u((var1 + 283974)) << 16)))
            var6 = (var6 + 520)
            while True:  # loop $label75
                var8 = (var1 + 283984)
                i32_store((var4 + ((var5 + var6) << 2)), i32_load(((var1 + 283984) + (var5 << 2))))
                var10 = (var5 | 1)
                i32_store((var4 + ((var6 + (var5 | 1)) << 2)), i32_load((var8 + (var10 << 2))))
                var10 = (var5 | 2)
                i32_store((var4 + ((var6 + (var5 | 2)) << 2)), i32_load((var8 + (var10 << 2))))
                var8 = (var5 | 3)
                if (1 if (var5 | 3) != 155 else 0):
                    i32_store((var4 + ((var6 + var8) << 2)), i32_load(((var1 + (var8 << 2)) + 283984)))
                    var5 = (var5 + 4)
                    continue
                break  # end loop
            i32_store((var2 + 2700), i32_load(var1 + 283868))
            i32_store((var2 + 2704), i32_load(var1 + 283912))
            i32_store((var2 + 2708), i32_load(var1 + 283916))
            i32_store((var2 + 2712), i32_load(var1 + 283920))
            i32_store((var2 + 2716), i32_load(var1 + 283964))
            i32_store((var2 + 2720), i32_load(var1 + 283904))
            i32_store((var2 + 2724), i32_load(var1 + 283880))
            i32_store((var2 + 2728), i32_load(var1 + 283940))
            i32_store((var2 + 2732), i32_load(var1 + 281804))
            i32_store((var2 + 2736), i32_load(var1 + 283924))
            i32_store((var2 + 2740), i32_load(var1 + 283936))
            i32_store((var2 + 2744), i32_load(var1 + 283948))
            i32_store((var2 + 2748), i32_load(var1 + 283956))
            i32_store((var2 + 2752), i32_load(var1 + 284616))
            i32_store((var2 + 2756), i32_load8_u(var1 + 286700))
            i32_store((var2 + 2760), i32_load8_u(var1 + 286701))
            i32_store((var2 + 2764), i32_load8_u(var1 + 286699))
            i32_store((var2 + 2768), i32_load8_u(var1 + 92))
            i32_store((var2 + 2772), i32_load8_u(var1 + 93))
            i32_store((var2 + 2776), i32_load(var1 + 283964))
            i32_store((var2 + 2780), i32_load(var1 + 283952))
            i32_store((var2 + 2784), i32_load(var1 + 80))
            i32_store((var2 + 2788), i32_load(var1 + 84))
            i32_store((var2 + 2792), i32_load(var1 + 88))
            var6 = i32_load(var1 + 281800)
            if (1 if i32_load(var1 + 281800) == 0 else 0):
                break
            i32_store((var2 + 2796), i32_load(var12 + 28))
            var5 = 0
            if (1 if i32_load(9142892) == 0 else 0):
                break
            while True:  # loop $label77
                var8 = i32_load((var6 + (var5 << 2)))
                var10 = i32_load(var12 + 28)
                i32_store(var12 + 28, (i32_load(var12 + 28) + 1))
                i32_store((var4 + (var10 << 2)), var8)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) < i32_load(9142892) else 0):
                    continue
                break  # end loop
            i32_store((var2 + 2800), i32_load(var1 + 284608))
            i32_store((var2 + 2804), i32_load(var1 + 286684))
            i32_store((var2 + 2808), i32_load8_u(var1 + 286696))
            i32_store((var2 + 2812), i32_load(var1 + 283976))
            i32_store((var2 + 2816), i32_load(var1 + 283980))
            i32_store((var2 + 2820), i32_load(var1 + 286688))
            if i32_load(9147132):
            else:
            i32_store(0, i32_load(var1 + 283896))
            if i32_load(9147132):
            else:
            i32_store(0, i32_load(var1 + 283900))
            var6 = (var9 + 717)
            var7 = (var7 + 1)
            if (1 if (var7 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    if (1 if var36 >= 4 else 0):
        var9 = ((var23 & 0xFFFFFFFF) // 33)
        var26 = (((var23 & 0xFFFFFFFF) // 33) << 5)
        var23 = (var9 * 31)
        var15 = (var9 * 30)
        var21 = (var9 * 29)
        var25 = (var9 * 28)
        var24 = (var9 * 27)
        var27 = (var9 * 26)
        var28 = (var9 * 25)
        var29 = (var9 * 24)
        var30 = (var9 * 23)
        var19 = (var9 * 22)
        var14 = (var9 * 21)
        var17 = (var9 * 20)
        var32 = (var9 * 19)
        var22 = (var9 * 18)
        var33 = (var9 * 17)
        var34 = (var9 << 4)
        var35 = (var9 * 15)
        var39 = (var9 * 14)
        var20 = (var9 * 13)
        var16 = (var9 * 12)
        var41 = (var9 * 11)
        var42 = (var9 * 10)
        var43 = (var9 * 9)
        var8 = 3
        var44 = (var9 << 3)
        var45 = (var9 * 7)
        var46 = (var9 * 6)
        var47 = (var9 * 5)
        var48 = (var9 << 2)
        var49 = (var9 * 3)
        var50 = (var9 << 1)
        var13 = i32_load(9147132)
        var51 = i32_load(38448)
        var52 = i32_load(9671128)
        var3 = i32_load(var12 + 28)
        var7 = 0
        var11 = 0
        while True:  # loop $label92
            var5 = (var52 + (var8 * 132))
            var10 = i32_load8_u((var52 + (var8 * 132)) + 122)
            if (1 if i32_load8_u((var52 + (var8 * 132)) + 122) == var51 else 0):
                var1 = (var4 + ((var11 + var40) << 2))
                i32_store((var4 + ((var11 + var40) << 2)), i32_load(var5 + 28))
                i32_store(var1 + 4, i32_load(var5 + 64))
                i32_store(var1 + 8, i32_load8_u(var5 + 124))
                i32_store(var1 + 12, i32_load(var5 + 112))
                var11 = (var11 + 4)
                break
            var2 = i32_load(var5 + 16)
            if (1 if i32_load(var5 + 16) == 0 else 0):
                break
            i32_store((var4 + ((var7 + var31) << 2)), var3)
            i32_store((var4 + (var3 << 2)), i32_load(var2 + 8))
            var3 = (var3 + 1)
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            var6 = i32_load(var2)
            var1 = 0
            while True:  # loop $label81
                i32_store((var4 + (var3 << 2)), i32_load((var6 + (var1 << 2))))
                var3 = (var3 + 1)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) < i32_load(var2 + 8) else 0):
                    continue
                break  # end loop
            var2 = i32_load(var5 + 20)
            if (1 if i32_load(var5 + 20) == 0 else 0):
                break
            i32_store((var4 + (((var7 + var31) + var9) << 2)), var3)
            i32_store((var4 + (var3 << 2)), i32_load(var2 + 8))
            var3 = (var3 + 1)
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            var6 = i32_load(var2)
            var1 = 0
            while True:  # loop $label83
                i32_store((var4 + (var3 << 2)), i32_load((var6 + (var1 << 2))))
                var3 = (var3 + 1)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) < i32_load(var2 + 8) else 0):
                    continue
                break  # end loop
            var2 = i32_load(var5 + 24)
            if (1 if i32_load(var5 + 24) == 0 else 0):
                break
            var6 = i32_load(var2)
            if (1 if i32_load(var2) == 0 else 0):
                break
            i32_store((var4 + (((var7 + var31) + var50) << 2)), var3)
            i32_store((var4 + (var3 << 2)), i32_load(var6 + 8))
            var3 = (var3 + 1)
            if (1 if i32_load(var6 + 8) == 0 else 0):
                break
            var38 = i32_load(var6)
            var1 = 0
            while True:  # loop $label85
                i32_store((var4 + (var3 << 2)), i32_load((var38 + (var1 << 2))))
                var3 = (var3 + 1)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) < i32_load(var6 + 8) else 0):
                    continue
                break  # end loop
            var1 = (var7 + var31)
            i32_store((var4 + (((var7 + var31) + var49) << 2)), i32_load(var5 + 28))
            i32_store((var4 + ((var1 + var48) << 2)), i32_load(var5 + 32))
            i32_store((var4 + ((var1 + var47) << 2)), i32_load(var5 + 36))
            i32_store((var4 + ((var1 + var46) << 2)), (0 if var13 else i32_load(var5 + 40)))
            i32_store((var4 + ((var1 + var45) << 2)), i32_load(var5 + 44))
            var6 = i32_load(var5 + 48)
            if i32_load(var5 + 48):
                if var13:
                else:
                i32_store(0, i32_load(var6 + 32))
            i32_store((var4 + ((var1 + var43) << 2)), i32_load(var5 + 52))
            i32_store((var4 + ((var1 + var42) << 2)), i32_load(var5 + 60))
            i32_store((var4 + ((var1 + var41) << 2)), i32_load(var5 + 64))
            i32_store((var4 + ((var1 + var16) << 2)), i32_load(var5 + 68))
            i32_store((var4 + ((var1 + var20) << 2)), i32_load(var5 + 72))
            i32_store((var4 + ((var1 + var39) << 2)), i32_load(var5 + 76))
            i32_store((var4 + ((var1 + var35) << 2)), i32_load(var5 + 80))
            i32_store((var4 + ((var1 + var34) << 2)), i32_load(var5 + 84))
            i32_store((var4 + ((var1 + var33) << 2)), i32_load(var5 + 88))
            i32_store((var4 + ((var1 + var22) << 2)), (0 if var13 else i32_load(var5 + 92)))
            i32_store((var4 + ((var1 + var32) << 2)), i32_load(var5 + 108))
            i32_store((var4 + ((var1 + var17) << 2)), i32_load(var5 + 112))
            i32_store((var4 + ((var1 + var14) << 2)), i32_load(var5 + 116))
            i32_store((var4 + ((var1 + var19) << 2)), i32_load16_u(var5 + 120))
            i32_store((var4 + ((var1 + var30) << 2)), ((((i32_load8_u(var5 + 123) << 8) | (i32_load8_u(var5 + 124) << 16)) | (i32_load8_u(var5 + 125) << 24)) | var10))
            i32_store((var4 + ((var1 + var29) << 2)), i32_load(var5 + 126))
            i32_store((var4 + ((var1 + var28) << 2)), i32_load(var5 + 96))
            i32_store((var4 + ((var1 + var27) << 2)), i32_load(var5 + 56))
            if (1 if var2 == 0 else 0):
                break
            var10 = i32_load(var2 + 12)
            if (1 if i32_load(var2 + 12) == 0 else 0):
                break
            i32_store((var4 + ((var1 + var24) << 2)), var3)
            i32_store((var4 + (var3 << 2)), i32_load(var10 + 8))
            var3 = (var3 + 1)
            if (1 if i32_load(var10 + 8) == 0 else 0):
                break
            var38 = i32_load(var10)
            var6 = 0
            while True:  # loop $label88
                i32_store((var4 + (var3 << 2)), i32_load((var38 + (var6 << 2))))
                var3 = (var3 + 1)
                var6 = (var6 + 1)
                if (1 if (var6 + 1) < i32_load(var10 + 8) else 0):
                    continue
                break  # end loop
            var10 = i32_load(var2 + 8)
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            i32_store((var4 + ((var1 + var25) << 2)), var3)
            i32_store((var4 + (var3 << 2)), i32_load(var10 + 8))
            var3 = (var3 + 1)
            if (1 if i32_load(var10 + 8) == 0 else 0):
                break
            var38 = i32_load(var10)
            var6 = 0
            while True:  # loop $label90
                i32_store((var4 + (var3 << 2)), i32_load((var38 + (var6 << 2))))
                var3 = (var3 + 1)
                var6 = (var6 + 1)
                if (1 if (var6 + 1) < i32_load(var10 + 8) else 0):
                    continue
                break  # end loop
            var2 = i32_load(var2 + 4)
            if (1 if i32_load(var2 + 4) == 0 else 0):
                break
            i32_store((var4 + ((var1 + var21) << 2)), var3)
            i32_store((var4 + (var3 << 2)), i32_load(var2 + 8))
            var3 = (var3 + 1)
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            var10 = i32_load(var2)
            var6 = 0
            while True:  # loop $label91
                i32_store((var4 + (var3 << 2)), i32_load((var10 + (var6 << 2))))
                var3 = (var3 + 1)
                var6 = (var6 + 1)
                if (1 if (var6 + 1) < i32_load(var2 + 8) else 0):
                    continue
                break  # end loop
            i32_store((var4 + ((var1 + var15) << 2)), i32_load(var5 + 100))
            i32_store((var4 + ((var1 + var23) << 2)), i32_load(var5 + 104))
            i32_store((var4 + ((var1 + var26) << 2)), i32_load8_u(var5 + 130))
            var7 = (var7 + 1)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != var36 else 0):
                continue
            break  # end loop
    var5 = i32_load(9687204)
    if i32_load(9687204):
        i32_store(9687204, 0)
    var5 = func26(var37)
    i32_store(9687204, func26(var37))
    i32_store(var5, var18)
    i32_store(var12 + 24, var37)
    i32_store(9147396, var18)
    var5 = (i32_load(var12 + 24) + 4)
    i32_store(9147392, (i32_load(var12 + 24) + 4))
    i32_store(var12 + 24, var5)
    var9 = i32_load(9687204)
    if (1 if var0 == 0 else 0):
        var5 = var9
        break
    var5 = 0
    var3 = 0
    var0 = i32_load(var12 + 24)
    if i32_load(var12 + 24):
        var1 = -1
        while True:  # loop $label94
            var4 = (var1 ^ i32_load8_u((var3 + var9)))
            var1 = (((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1)
            var4 = (((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1)
            var1 = (((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1)
            var4 = (((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1)
            var1 = (((((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1)
            var4 = (((((((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1)
            var1 = (((((((((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1)
            var4 = (((((((((((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1)
            var1 = (((((((((((((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1)
            var4 = (((((((((((((((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1)
            var1 = (((((((((((((((((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1)
            var4 = (((((((((((((((((((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1)
            var1 = (((((((((((((((((((((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1)
            var4 = (((((((((((((((((((((((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1)
            var1 = (((((((((((((((((((((((((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1)
            var1 = (((((((((((((((((((((((((((((((((var1 ^ i32_load8_u((var3 + var9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (var4 & 1) else var1)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var0 else 0):
                continue
            break  # end loop
        var3 = (var1 ^ -1)
    i32_store(var12, var9)
    i32_store(var12 + 4, var0)
    i32_store(var12 + 8, var3)
    i32_store(var12 + 12, ((i32_load(9142848) & 0xFFFFFFFF) // 10))
    global global0
    global0 = (var12 + 32)
    return var5

