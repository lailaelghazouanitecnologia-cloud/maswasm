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
# $func771
# ==========================================================
def func771(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i64_store(var1 + 8, 1)
    if var0:
        break
    var0 = i32_load(9213808)
    if i32_load8_u(9147210):
        func41(28, 9173808, var0, (var1 + 8), 2)
        break
    var3 = (var0 << 2)
    var2 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var0:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9214048)]
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $func787
# ==========================================================
def func787(var0):
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
    var12 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if (1 if i32_load(9142872) != i32_load16_u(var0 + 110) else 0):
        break
    var22 = i32_load16_u(var0 + 114)
    var33 = i32_load16_u(var0 + 118)
    var1 = (i32_load16_u(var0 + 114) - i32_load16_u(var0 + 118))
    var23 = i32_load16_u(var0 + 112)
    var34 = i32_load16_u(var0 + 116)
    var1 = (i32_load16_u(var0 + 112) - i32_load16_u(var0 + 116))
    if (1 if (((i32_load16_u(var0 + 114) - i32_load16_u(var0 + 118)) * var1) + ((i32_load16_u(var0 + 112) - i32_load16_u(var0 + 116)) * var1)) > 4 else 0):
        break
    var26 = ((i32_load8_u(var0 + 124) & 0xFFFFFFFF) >> 1)
    var13 = i32_load(9142440)
    var24 = (i32_load(9142440) + 2)
    var25 = i32_load8_u(var0 + 122)
    var1 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var18 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var10 = i32_load(var1 + 200)
    var15 = (i32_load(var1 + 200) << 1)
    var17 = i32_load(var1 + 216)
    var30 = i32_load(var1 + 212)
    var27 = (var10 * var10)
    var31 = i32_load(9147376)
    var32 = i32_load(9142840)
    var8 = var22
    var9 = var23
    while True:  # loop $label26
        var14 = 0
        var5 = 0
        var6 = 0
        while True:  # loop $label10
            var1 = (var6 << 3)
            var7 = (i32_load(((var6 << 3) + 8992)) + var9)
            var11 = (i32_load((var1 + 8996)) + var8)
            var4 = (var17 + (i32_load((var1 + 8996)) + var8))
            if (1 if (var17 + (i32_load((var1 + 8996)) + var8)) > var11 else 0):
                var1 = (var7 + var17)
                var19 = (var7 if (1 if var1 < var7 else 0) else (var7 + var17))
                var20 = (var24 * i32_load(var18 + 208))
                var3 = 0
                var1 = var11
                while True:  # loop $label3
                    var1 = (var1 + 1)
                    var21 = (((var1 + 1) + var20) * var24)
                    var2 = var7
                    while True:  # loop $label1
                        if (1 if var2 != var19 else 0):
                            var2 = (var2 + 1)
                            if (1 if i32_load((var32 + (((var2 + 1) + var21) << 2))) == var30 else 0):
                                continue
                            break
                        break  # end loop
                    var3 = (1 if var1 >= var4 else 0)
                    if (1 if var1 != var4 else 0):
                        continue
                    break  # end loop
                if (1 if (var3 & 1) == 0 else 0):
                    break
            var3 = 0
            var4 = (var7 - var10)
            var19 = (var7 + var15)
            if (1 if (var7 - var10) >= (var7 + var15) else 0):
                break
            var1 = (var11 - var10)
            var20 = (var11 + var15)
            if (1 if (var11 - var10) >= (var11 + var15) else 0):
                break
            while True:  # loop $label8
                if (1 if var4 < var13 else 0):
                    var2 = (var4 - var7)
                    var21 = (((var4 - var7) * var2) - 1)
                    var2 = var1
                    while True:  # loop $label7
                        var28 = (var2 - var11)
                        if (1 if (var21 + ((var2 - var11) * var28)) > var27 else 0):
                            break
                        if (1 if var2 >= var13 else 0):
                            break
                        if (1 if (var2 | var4) < 0 else 0):
                            break
                        var3 = (var3 + (1 if i32_load16_u((var31 + (((var2 * var13) + var4) << 1))) == 0 else 0))
                        var2 = (var2 + 1)
                        if (1 if (var2 + 1) != var20 else 0):
                            continue
                        break  # end loop
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != var19 else 0):
                    continue
                break  # end loop
            if (1 if var3 > var5 else 0):
                break
            if (1 if var3 != var5 else 0):
                break
            if (1 if ((var14 & 0xFFFFFFFF) >> 1) != var26 else 0):
                break
            var5 = var3
            var14 = var6
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != 8 else 0):
                continue
            break  # end loop
        if (1 if var5 == 0 else 0):
            var4 = (var8 + 2)
            var14 = (var9 + 2)
            var7 = (var8 - 1)
            var11 = (var9 - 1)
            var26 = i32_load(var18 + 208)
            var27 = (var24 * i32_load(var18 + 208))
            var25 = ((var25 * 404) + 9568096)
            var10 = i32_load(9142432)
            var19 = (i32_load(9142432) + (((var13 * var22) + var23) << 2))
            var18 = i32_load(9215880)
            var16 = 1
            while True:  # loop $label24
                if (1 if var11 >= var14 else 0):
                    break
                if (1 if var4 <= var7 else 0):
                    break
                var20 = (var14 - 1)
                var21 = (var4 - 1)
                var1 = var11
                while True:  # loop $label23
                    if (1 if var1 < var13 else 0):
                        var28 = (1 if var1 == var20 else 0)
                        var35 = (1 if var1 == var11 else 0)
                        var2 = (var1 + var17)
                        var36 = (var1 if (1 if var1 > var2 else 0) else (var1 + var17))
                        var3 = var7
                        while True:  # loop $label22
                            if (1 if (var28 | ((var35 | (1 if var3 == var7 else 0)) | (1 if var3 == var21 else 0))) == 0 else 0):
                                break
                            if (1 if var3 >= var13 else 0):
                                break
                            if (1 if (var1 | var3) < 0 else 0):
                                break
                            var2 = 1
                            if (1 if var26 <= 1 else 0):
                                if var10:
                                else:
                                var15 = 0
                                # br_table ['$label13', '$label14', '$label14', '$label14', '$label13', '$label14']
                                _br_idx = i32_load(var25 + 264)
                                break  # br_table
                                if (1 if var10 == 0 else 0):
                                    var5 = 0
                                    break
                                var5 = i32_load(var19)
                                break
                                var5 = 0
                                if (1 if var17 == 0 else 0):
                                    break
                                if (1 if var10 == 0 else 0):
                                    break
                                var29 = i32_load(var25 + 220)
                                if (1 if i32_load(var25 + 220) == 0 else 0):
                                    break
                                if (1 if var18 == 0 else 0):
                                    break
                                var37 = i32_load(var18)
                                var6 = 0
                                while True:  # loop $label17
                                    var38 = (var6 + var23)
                                    var2 = 0
                                    while True:  # loop $label16
                                        var5 = i32_load((var10 + ((var38 + ((var2 + var22) * var13)) << 2)))
                                        if (1 if i32_load((var37 + (i32_load((var10 + ((var38 + ((var2 + var22) * var13)) << 2))) << 2))) == 0 else 0):
                                            break
                                        var2 = (var2 + 1)
                                        if (1 if (var2 + 1) != var29 else 0):
                                            continue
                                        break  # end loop
                                    var5 = 0
                                    var6 = (var6 + 1)
                                    if (1 if (var6 + 1) != var17 else 0):
                                        continue
                                    break  # end loop
                            else:
                            if (1 if 1 == 0 else 0):
                                break
                            if i32_load16_u((var31 + (((var3 * var13) + var1) << 1))):
                                break
                            var5 = 0
                            var6 = var3
                            var15 = (var3 + var17)
                            if (1 if (var3 + var17) <= var3 else 0):
                                break
                            while True:  # loop $label21
                                var6 = (var6 + 1)
                                var29 = (((var6 + 1) + var27) * var24)
                                var2 = var1
                                while True:  # loop $label19
                                    if (1 if var2 != var36 else 0):
                                        var2 = (var2 + 1)
                                        if (1 if i32_load((var32 + (((var2 + 1) + var29) << 2))) == var30 else 0):
                                            continue
                                        break
                                    break  # end loop
                                var5 = (1 if var6 >= var15 else 0)
                                if (1 if var6 != var15 else 0):
                                    continue
                                break  # end loop
                            if (var5 & 1):
                                break
                            var3 = (var3 + 1)
                            if (1 if (var3 + 1) != var4 else 0):
                                continue
                            break  # end loop
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != var14 else 0):
                        continue
                    break  # end loop
                var4 = (var4 + 1)
                var14 = (var14 + 1)
                var16 = (var16 + 1)
                var7 = (var8 - (var16 + 1))
                var11 = (var9 - var16)
                if (1 if var16 != 250 else 0):
                    continue
                break  # end loop
            break
        var1 = (var14 << 3)
        var8 = (i32_load(((var14 << 3) + 8996)) + var8)
        var9 = (i32_load((var1 + 8992)) + var9)
        var16 = (var16 + 1)
        if (1 if (var16 + 1) != 8 else 0):
            continue
        break
        break  # end loop
    var9 = var1
    var8 = var3
    if ((1 if var9 == var34 else 0) & (1 if var8 == var33 else 0)):
        break
    if ((1 if var9 == var23 else 0) & (1 if var8 == var22 else 0)):
        break
    if i32_load8_u(9147210):
        i32_store(var12 + 40, 0)
        i64_store(var12 + 32, 0)
        i64_store(var12 + 24, 270582939648)
        i32_store(var12 + 20, var8)
        i32_store(var12 + 16, var9)
        i32_store(var12 + 12, i32_load(var0 + 28))
        func41(5, (var12 + 12), 1, (var12 + 16), 7)
        break
    i32_store16(var0 + 118, var8)
    i32_store16(var0 + 116, var9)
    global global0
    global0 = (var12 + 48)
    return 0


# ==========================================================
# $Fe
# Export: Fe
# ==========================================================
def Fe(var0):
    """Export: Fe"""
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
    var2 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var3 = 1
    var1 = 1
    # br_table ['$label1', '$label2', '$label3']
    _br_idx = var0
    break  # br_table
    var10 = (var0 - 2)
    var11 = (var0 - 1)
    while True:  # loop $label7
        i32_store8(9147208, 1)
        var8 = (i32_load(9561692) + (var0 * 286704))
        if (1 if var0 <= 1 else 0):
            break
        var3 = (var6 + var11)
        var9 = ((var6 + var11) & 3)
        var5 = i32_load(9143004)
        var1 = 1
        if (1 if (var6 + var10) >= 3 else 0):
            var12 = (var3 & -4)
            var3 = 0
            while True:  # loop $label5
                i32_store(((var1 << 2) + 9147392), i32_load8_u((var5 + ((var1 * var4) + var0))))
                var7 = (var1 + 1)
                i32_store((((var1 + 1) << 2) + 9147392), i32_load8_u((var5 + ((var4 * var7) + var0))))
                var7 = (var1 + 2)
                i32_store((((var1 + 2) << 2) + 9147392), i32_load8_u((var5 + ((var4 * var7) + var0))))
                var7 = (var1 + 3)
                i32_store((((var1 + 3) << 2) + 9147392), i32_load8_u((var5 + ((var4 * var7) + var0))))
                var1 = (var1 + 4)
                var3 = (var3 + 4)
                if (1 if (var3 + 4) != var12 else 0):
                    continue
                break  # end loop
        var3 = 0
        if (1 if var9 == 0 else 0):
            break
        while True:  # loop $label6
            i32_store(((var1 << 2) + 9147392), i32_load8_u((var5 + ((var1 * var4) + var0))))
            var1 = (var1 + 1)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var9 else 0):
                continue
            break  # end loop
        var1 = i32_load8_u(var8 + 283972)
        var3 = i32_load8_u((var8 + 283974))
        var4 = i32_load8_u((var8 + 283973))
        i32_store(var2 + 52, var8)
        i32_store(var2 + 48, var0)
        i32_store(var2 + 56, ((var3 | (var4 << 8)) | (var1 << 16)))
        i32_store(var2 + 60, 0)
        var6 = (var6 + 1)
        var0 = (var0 + 1)
        var4 = i32_load(9142892)
        if (1 if (var0 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    break
    while True:  # loop $label8
        var0 = (i32_load(9561692) + (var3 * 286704))
        if i32_load8_u(9147208):
            i32_store8(9147208, 0)
        var1 = i32_load8_u(var0 + 283972)
        var4 = i32_load8_u((var0 + 283974))
        var5 = i32_load8_u((var0 + 283973))
        i32_store(var2 + 12, i32_load(var0 + 284608))
        i32_store(var2 + 4, var0)
        i32_store(var2, var3)
        i32_store(var2 + 8, ((var4 | (var5 << 8)) | (var1 << 16)))
        var3 = (var3 + 1)
        if (1 if (var3 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    break
    while True:  # loop $label9
        var0 = (i32_load(9561692) + (var1 * 286704))
        var3 = i32_load8_u((i32_load(9561692) + (var1 * 286704)) + 283972)
        var4 = i32_load8_u((var0 + 283974))
        var5 = i32_load8_u((var0 + 283973))
        var6 = i32_load(var0 + 286684)
        var13 = i64_load((var0 + 283856))
        i64_store(var2 + 32, i64_load(var0 + 283848))
        i64_store(var2 + 40, var13)
        i32_store(var2 + 16, var1)
        i32_store(var2 + 24, var0)
        i32_store(var2 + 28, var6)
        i32_store(var2 + 20, ((var4 | (var5 << 8)) | (var3 << 16)))
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    global global0
    global0 = (var2 - -64)


# ==========================================================
# $Ub
# Export: Ub
# ==========================================================
def Ub(var0, var1, var2):
    """Export: Ub"""
    var3 = 0
    var3 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(var3 + 12, var2)
    i32_store(var3 + 8, var1)
    i32_store(var3 + 4, var0)
    if i32_load8_u(9147210):
        func41(40, 0, 0, (var3 + 4), 3)
        break
    # call_indirect via table[i32_load(9214144)]
    global global0
    global0 = (var3 + 16)


# ==========================================================
# $kb
# Export: kb
# ==========================================================
def kb():
    """Export: kb"""
    var0 = 0
    var1 = 0
    var2 = 0
    var0 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var1 = i32_load(9173808)
    i32_store(var0 + 12, i32_load(9173808))
    i32_store(var0 + 4, i32_load((i32_load(9681476) + (i32_load(9681468) << 2))))
    i32_store(var0 + 8, i32_load(9681472))
    if i32_load8_u(9147210):
        func41(12, (var0 + 12), 1, (var0 + 4), 2)
        break
    var2 = func26(4)
    i32_store(func26(4), var1)
    # call_indirect via table[i32_load(9213920)]
    global global0
    global0 = (var0 + 16)

