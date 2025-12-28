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
# $func200
# ==========================================================
def func200(var0, var1, var2, var3):
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
    var7 = i32_load(9561692)
    var5 = i32_load16_u(var0 + 110)
    var10 = (i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704))
    if (1 if i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 286684) == 0 else 0):
        break
    var12 = i32_load8_u(var0 + 122)
    var31 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) == 1 else 0):
        break
    if (1 if i32_load(38456) == var12 else 0):
        break
    if (1 if i32_load(38764) == var12 else 0):
        break
    var4 = i32_load(var10 + 283904)
    if (1 if (i32_load(var10 + 283904) | var1) == 0 else 0):
        break
    if (1 if var1 == 0 else 0):
        var25 = (i32_load(9142892) * var5)
        var26 = ((var12 * 404) + 9568096)
        var27 = i32_load(9671128)
        var17 = (i32_load(9671128) + (i32_load(var0 + 28) * 132))
        var10 = i32_load(9142432)
        var28 = i32_load16_u(var0 + 112)
        var18 = i32_load(9142440)
        var29 = i32_load16_u(var0 + 114)
        var32 = (i32_load(9142432) + ((i32_load16_u(var0 + 112) + (i32_load(9142440) * i32_load16_u(var0 + 114))) << 2))
        var16 = i32_load(9215880)
        var33 = i32_load(38564)
        var34 = i32_load(38620)
        var35 = i32_load(38560)
        var30 = i32_load(9143004)
        var36 = i32_load(38500)
        var12 = 2147483647
        var37 = (var7 + (var4 * 286704))
        var1 = 0
        while True:  # loop $label20
            var7 = i32_load(((var37 + (var19 << 2)) + 284636))
            if (1 if i32_load(((var37 + (var19 << 2)) + 284636)) == 0 else 0):
                break
            var38 = i32_load(var7 + 8)
            if (1 if i32_load(var7 + 8) == 0 else 0):
                break
            var39 = i32_load(var7)
            var20 = 0
            while True:  # loop $label19
                var7 = i32_load((var39 + (var20 << 2)))
                if (1 if i32_load((var39 + (var20 << 2))) == 0 else 0):
                    break
                var5 = (var27 + (var7 * 132))
                var21 = i32_load16_u((var27 + (var7 * 132)) + 114)
                var7 = (i32_load16_u((var27 + (var7 * 132)) + 114) - var29)
                var22 = i32_load16_u(var5 + 112)
                var7 = (i32_load16_u(var5 + 112) - var28)
                var7 = (((i32_load16_u((var27 + (var7 * 132)) + 114) - var29) * var7) + ((i32_load16_u(var5 + 112) - var28) * var7))
                if (1 if (((i32_load16_u((var27 + (var7 * 132)) + 114) - var29) * var7) + ((i32_load16_u(var5 + 112) - var28) * var7)) >= var12 else 0):
                    break
                var9 = i32_load8_u(var5 + 122)
                if (1 if func162(var0, i32_load8_u(var5 + 122), 0, 0) == 0 else 0):
                    break
                if (1 if var9 == var36 else 0):
                    break
                var4 = i32_load16_u(var5 + 110)
                var6 = i32_load16_u(var5 + 120)
                if i32_load16_u(var5 + 120):
                else:
                if (1 if i32_load8_u(((var6 if i32_load8_u((var30 + (var4 + var25))) else var4) + (var4 + var25))) == 0 else 0):
                    if (1 if i32_load8_u(var5 + 127) != 6 else 0):
                        break
                    if (1 if i32_load8_u(var5 + 128) == 0 else 0):
                        break
                    break
                if i32_load8_u(var5 + 128):
                    break
                if (1 if i32_load8_u(var5 + 125) == 10 else 0):
                    break
                if (1 if i32_load8_u(var5 + 126) == 2 else 0):
                    break
                var23 = i32_load(var5 + 64)
                if (1 if i32_load(var5 + 64) == -1 else 0):
                    break
                var13 = ((var9 * 404) + 9568096)
                var4 = i32_load(((var9 * 404) + 9568096) + 264)
                if (1 if i32_load(((var9 * 404) + 9568096) + 264) == 2 else 0):
                    break
                if (1 if i32_load(var13 + 188) != 55 else 0):
                    break
                if (1 if var9 == var35 else 0):
                    break
                if (1 if var9 == var34 else 0):
                    break
                if (1 if var9 == var33 else 0):
                    break
                if i32_load(var5 + 36):
                    break
                # br_table ['$label5', '$label6', '$label6', '$label6', '$label5', '$label6']
                _br_idx = var4
                break  # br_table
                var8 = 0
                var11 = i32_load(var13 + 216)
                if (1 if i32_load(var13 + 216) == 0 else 0):
                    break
                var14 = i32_load(var13 + 220)
                if (1 if i32_load(var13 + 220) == 0 else 0):
                    break
                if (1 if var16 == 0 else 0):
                    break
                if (1 if var10 == 0 else 0):
                    break
                var15 = i32_load(var16)
                var6 = 0
                while True:  # loop $label9
                    var24 = (var6 + var22)
                    var4 = 0
                    while True:  # loop $label8
                        var8 = i32_load((var10 + ((var24 + ((var4 + var21) * var18)) << 2)))
                        if (1 if i32_load((var15 + (i32_load((var10 + ((var24 + ((var4 + var21) * var18)) << 2))) << 2))) == 0 else 0):
                            break
                        var4 = (var4 + 1)
                        if (1 if (var4 + 1) != var14 else 0):
                            continue
                        break  # end loop
                    var8 = 0
                    var6 = (var6 + 1)
                    if (1 if (var6 + 1) != var11 else 0):
                        continue
                    break  # end loop
                break
                if (1 if var10 == 0 else 0):
                    var8 = 0
                    break
                var8 = i32_load((var10 + (((var18 * var21) + var22) << 2)))
                # br_table ['$label10', '$label11', '$label11', '$label11', '$label10', '$label11']
                _br_idx = var31
                break  # br_table
                var6 = 0
                var14 = i32_load(var26 + 216)
                if (1 if i32_load(var26 + 216) == 0 else 0):
                    break
                var15 = i32_load(var26 + 220)
                if (1 if i32_load(var26 + 220) == 0 else 0):
                    break
                if (1 if var16 == 0 else 0):
                    break
                if (1 if var10 == 0 else 0):
                    break
                var24 = i32_load(var16)
                var11 = 0
                while True:  # loop $label14
                    var40 = (var11 + var28)
                    var4 = 0
                    while True:  # loop $label13
                        var6 = i32_load((var10 + ((var40 + ((var4 + var29) * var18)) << 2)))
                        if (1 if i32_load((var24 + (i32_load((var10 + ((var40 + ((var4 + var29) * var18)) << 2))) << 2))) == 0 else 0):
                            break
                        var4 = (var4 + 1)
                        if (1 if (var4 + 1) != var15 else 0):
                            continue
                        break  # end loop
                    var6 = 0
                    var11 = (var11 + 1)
                    if (1 if (var11 + 1) != var14 else 0):
                        continue
                    break  # end loop
                break
                if (1 if var10 == 0 else 0):
                    var6 = 0
                    break
                var6 = i32_load(var32)
                if (1 if var6 != var8 else 0):
                    break
                var4 = i32_load(var5 + 100)
                if i32_load(var5 + 100):
                    var4 = (var27 + (var4 * 132))
                    if (1 if (var23 + 5) < (((i32_load((((i32_load8_u((var27 + (var4 * 132)) + 122) * 1020) + 9299904) + (var9 << 2))) * i32_load(var4 + 52)) & 0xFFFFFFFF) // 100) else 0):
                        break
                var4 = i32_load(((i32_load8_u(var17 + 122) * 404) + 9568096) + 228)
                if (1 if i32_load(((i32_load8_u(var17 + 122) * 404) + 9568096) + 228) == 0 else 0):
                    break
                var9 = i32_load(var13 + 216)
                if (1 if i32_load(var13 + 216) == 0 else 0):
                    break
                var13 = (var4 * var4)
                var11 = i32_load16_u(var17 + 114)
                var23 = i32_load16_u(var17 + 112)
                var4 = 0
                var6 = 1
                while True:  # loop $label18
                    var8 = (var11 - (var4 + var21))
                    var14 = ((var11 - (var4 + var21)) * var8)
                    var8 = 0
                    while True:  # loop $label16
                        var15 = (var23 - (var8 + var22))
                        if (1 if var13 > (((var23 - (var8 + var22)) * var15) + var14) else 0):
                            var8 = (var8 + 1)
                            if (1 if var9 != (var8 + 1) else 0):
                                continue
                            break
                        break  # end loop
                    if (1 if (var6 & 1) == 0 else 0):
                        break
                    break
                    var4 = (var4 + 1)
                    var6 = (1 if (var4 + 1) < var9 else 0)
                    if (1 if var4 != var9 else 0):
                        continue
                    break  # end loop
                break
                var1 = i32_load(var5 + 28)
                var12 = var7
                var20 = (var20 + 1)
                if (1 if (var20 + 1) != var38 else 0):
                    continue
                break  # end loop
            var19 = (var19 + 1)
            if (1 if (var19 + 1) != 255 else 0):
                continue
            break  # end loop
        if (1 if var1 == 0 else 0):
            break
    if (1 if var2 == 0 else 0):
        if var3:
            i32_store8(var0 + 125, 0)
        return 1
    i32_store(var0 + 32, var1)
    return 1
    i32_store8(var0 + 129, 0)
    return 0


# ==========================================================
# $func323
# ==========================================================
def func323(var0, var1):
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
    var2 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        break
    if (1 if i32_load(var2 + 8) < 2 else 0):
        break
    var2 = i32_load(var2)
    if (1 if i32_load(i32_load(var2)) != 2 else 0):
        break
    var10 = i32_load(var2 + 4)
    var2 = i32_load16_u(var0 + 110)
    var4 = i32_load(9561692)
    var3 = i32_load(var0 + 88)
    var11 = ((i32_load(var0 + 88) & 0xFFFFFFFF) >> 16)
    var5 = i32_load16_u(var0 + 108)
    var14 = i32_load(var0 + 28)
    var7 = i32_load(9671128)
    var6 = (var3 & 65535)
    # br_table ['$label1', '$label2', '$label3', '$label4', '$label3']
    _br_idx = (var3 & 65535)
    break  # br_table
    break
    break
    break
    if (1 if i32_load(38528) == var11 else 0):
        break
    if (1 if i32_load(((var11 * 404) + 9568096) + 268) == 3 else 0):
        break
    if (1 if i32_load(38712) == i32_load8_u(var0 + 122) else 0):
        break
    var3 = ((var4 + (var2 * 286704)) + 281648)
    i32_store(((var4 + (var2 * 286704)) + 281648), (i32_load(var3) + var5))
    var8 = (var4 + (var2 * 286704))
    var3 = (((var4 + (var2 * 286704)) + (var6 << 2)) + 283848)
    var6 = i32_load((((var4 + (var2 * 286704)) + (var6 << 2)) + 283848))
    if (1 if i32_load((((var4 + (var2 * 286704)) + (var6 << 2)) + 283848)) == 2147483647 else 0):
        break
    i32_store(var3, (var5 + var6))
    var3 = 1
    i32_store8(var8 + 286701, 1)
    var5 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var9 = (var5 - 1)
    var12 = ((var5 - 1) & 1)
    var4 = (i32_load((var4 + (var2 * 286704)) + 283908) * var5)
    var6 = i32_load(9561692)
    var8 = i32_load(9143016)
    if (1 if var5 != 2 else 0):
        var5 = (var9 & -2)
        var2 = 0
        while True:  # loop $label7
            if i32_load8_u((var8 + (var3 + var4))):
                i32_store8((var6 + (var3 * 286704)) + 286701, 1)
            var9 = (var3 + 1)
            if i32_load8_u((var8 + ((var3 + 1) + var4))):
                i32_store8((var6 + (var9 * 286704)) + 286701, 1)
            var3 = (var3 + 2)
            var2 = (var2 + 2)
            if (1 if (var2 + 2) != var5 else 0):
                continue
            break  # end loop
    if (1 if var12 == 0 else 0):
        break
    if (1 if i32_load8_u((var8 + (var3 + var4))) == 0 else 0):
        break
    i32_store8((var6 + (var3 * 286704)) + 286701, 1)
    i32_store16(var0 + 108, 0)
    if (1 if var1 == 0 else 0):
        i32_store8(var0 + 125, 0)
        if (1 if i32_load(var0 + 92) == 0 else 0):
            break
        if i32_load(9140316):
            if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
                break
        var1 = ((var11 * 404) + 9568096)
        if (1 if i32_load(((var11 * 404) + 9568096) + 268) == 3 else 0):
            var6 = i32_load(9142440)
            var12 = (i32_load(9142440) + 2)
            var15 = ((i32_load(9142440) + 2) * i32_load(var1 + 208))
            var8 = i32_load16_u(var0 + 112)
            var16 = (i32_load16_u(var0 + 112) + 29)
            var9 = i32_load16_u(var0 + 114)
            var17 = (i32_load16_u(var0 + 114) + 29)
            var10 = (var9 - 30)
            var2 = (var8 - 30)
            var18 = i32_load(9671128)
            var19 = i32_load(9142840)
            var5 = 2147483647
            var7 = 0
            while True:  # loop $label11
                var4 = (var2 + 1)
                if (1 if var2 < var6 else 0):
                    var1 = (var8 - var2)
                    var20 = ((var8 - var2) * var1)
                    var1 = var10
                    while True:  # loop $label10
                        var3 = var1
                        if (1 if var6 <= var1 else 0):
                            break
                        if (1 if (var2 | var3) < 0 else 0):
                            break
                        var1 = (var9 - var3)
                        var13 = (((var9 - var3) * var1) + var20)
                        if (1 if (((var9 - var3) * var1) + var20) >= var5 else 0):
                            break
                        var1 = i32_load((var19 + (((((var3 + var15) + 1) * var12) + var4) << 2)))
                        if (1 if i32_load((var19 + (((((var3 + var15) + 1) * var12) + var4) << 2))) == 0 else 0):
                            break
                        var13 = (1 if var11 == i32_load8_u((var18 + (var1 * 132)) + 122) else 0)
                        var5 = (var13 if (1 if var11 == i32_load8_u((var18 + (var1 * 132)) + 122) else 0) else var5)
                        var7 = (var1 if var13 else var7)
                        var1 = (var3 + 1)
                        if (1 if var3 != var17 else 0):
                            continue
                        break  # end loop
                var1 = (1 if var2 != var16 else 0)
                var2 = var4
                if var1:
                    continue
                break  # end loop
            if var7:
                return func28(1, 1)
            func404(var14)
            return ((var4 + (var2 * 286704)) + 281664)
        if (1 if var11 == i32_load(38528) else 0):
            break
        var2 = (var7 + (var10 * 132))
        var1 = i32_load((var7 + (var10 * 132)) + 28)
        if (1 if i32_load((var7 + (var10 * 132)) + 28) == 0 else 0):
            break
        if (1 if i32_load8_u(var2 + 125) == 10 else 0):
            break
        if (1 if i32_load(((i32_load8_u((var7 + (var10 * 132)) + 122) * 404) + 9568096) + 188) < 4 else 0):
            break
        func29(var0, 1)
        return ((var4 + (var2 * 286704)) + 281644)
        if i32_load8_u(9142916):
        else:
        return var0
        func404(var14)
    return ((var4 + (var2 * 286704)) + 281640)

