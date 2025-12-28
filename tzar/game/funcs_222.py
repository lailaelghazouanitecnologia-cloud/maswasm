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
# $func689
# ==========================================================
def func689(var0, var1, param2):
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
    var40 = 0.0
    var9 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var21 = i32_load(9671128)
    var7 = (i32_load(9671128) + (var0 * 132))
    var12 = i32_load16_u((i32_load(9671128) + (var0 * 132)) + 114)
    var17 = i32_load16_u(var7 + 112)
    var23 = i32_load8_u(var7 + 122)
    if (1 if i32_load8_u(9216060) == 0 else 0):
        break
    var14 = i32_load16_u(var7 + 110)
    if (1 if i32_load16_u(var7 + 110) == 0 else 0):
        break
    var4 = (var21 + (i32_load((i32_load(9142840) + ((var17 + ((i32_load(9142440) + 2) * (var12 + 1))) << 2)) + 4) * 132))
    if (1 if i32_load(39064) != i32_load8_u((var21 + (i32_load((i32_load(9142840) + ((var17 + ((i32_load(9142440) + 2) * (var12 + 1))) << 2)) + 4) * 132)) + 122) else 0):
        break
    var10 = i32_load(9561692)
    var6 = (i32_load(9561692) + (var14 * 286704))
    var2 = i32_load((i32_load(9561692) + (var14 * 286704)) + 283848)
    if (1 if i32_load((i32_load(9561692) + (var14 * 286704)) + 283848) == 2147483647 else 0):
        break
    i32_store((var6 + 283848), (i32_load(var4 + 52) + var2))
    var2 = 1
    i32_store8(var6 + 286701, 1)
    var3 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var5 = (var3 - 1)
    var11 = ((var3 - 1) & 1)
    var14 = (i32_load((var10 + (var14 * 286704)) + 283908) * var3)
    var10 = i32_load(9561692)
    var8 = i32_load(9143016)
    if (1 if var3 != 2 else 0):
        var24 = (var5 & -2)
        var3 = 0
        while True:  # loop $label2
            if i32_load8_u((var8 + (var2 + var14))):
                i32_store8((var10 + (var2 * 286704)) + 286701, 1)
            var5 = (var2 + 1)
            if i32_load8_u((var8 + ((var2 + 1) + var14))):
                i32_store8((var10 + (var5 * 286704)) + 286701, 1)
            var2 = (var2 + 2)
            var3 = (var3 + 2)
            if (1 if (var3 + 2) != var24 else 0):
                continue
            break  # end loop
    if (1 if var11 == 0 else 0):
        break
    if (1 if i32_load8_u((var8 + (var2 + var14))) == 0 else 0):
        break
    i32_store8((var10 + (var2 * 286704)) + 286701, 1)
    var2 = (var6 + 281640)
    i32_store((var6 + 281640), (i32_load(var2) + i32_load(var4 + 52)))
    if i32_load8_u(9142917):
        break
    if (1 if i32_load(9142872) != i32_load16_u(var7 + 110) else 0):
        break
    a_b()
    if (1 if var1 == 1 else 0):
        break
    if (1 if i32_load8_u(59181) == 0 else 0):
        break
    if (1 if i32_load8_u(var7 + 125) == 7 else 0):
        break
    var2 = (i32_load8_u((var21 + (var0 * 132)) + 124) << 3)
    var18 = (var21 + (var0 * 132))
    var3 = i32_load8_u((var21 + (var0 * 132)) + 129)
    # br_table ['$label4', '$label5', '$label5', '$label5', '$label4', '$label5']
    _br_idx = (i32_load8_u((var21 + (var0 * 132)) + 129) - 5)
    break  # br_table
    var2 = i32_load8_u(var18 + 123)
    # br_table ['$label6', '$label5', '$label5', '$label5', '$label5', '$label5', '$label6', '$label7']
    _br_idx = i32_load8_u(var18 + 123)
    break  # br_table
    if (1 if var2 == 69 else 0):
        break
    if (1 if var2 != 35 else 0):
        break
    if (1 if (var1 & 1) == 0 else 0):
        break
    if (1 if var3 != 9 else 0):
        break
    var2 = i32_load((var21 + (var0 * 132)) + 32)
    if (1 if i32_load((var21 + (var0 * 132)) + 32) == 0 else 0):
        break
    var2 = func106(var7, i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122), -1, -1)
    if (1 if func106(var7, i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122), -1, -1) == 0 else 0):
        break
    i32_store((var21 + (var0 * 132)) + 32, var2)
    i32_store8(var18 + 123, 6)
    var2 = i32_load8_u(var18 + 123)
    if i32_load8_u(var18 + 123):
        break
    if (1 if i32_load16_u(var18 + 108) == 0 else 0):
        break
    var11 = 0
    var2 = (var21 + (var0 * 132))
    var3 = i32_load((var21 + (var0 * 132)) + 32)
    if (1 if i32_load((var21 + (var0 * 132)) + 32) == 0 else 0):
        break
    var4 = i32_load(var2 + 88)
    if (1 if i32_load(var2 + 88) == 0 else 0):
        break
    var2 = i32_load8_u(var7 + 122)
    # br_table ['$label11', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label11', '$label12']
    _br_idx = (i32_load8_u(var7 + 122) + -64)
    break  # br_table
    if (1 if var2 != 10 else 0):
        break
    var3 = (i32_load(9671128) + (var3 * 132))
    # br_table ['$label10', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label10', '$label13']
    _br_idx = (i32_load8_u((i32_load(9671128) + (var3 * 132)) + 125) - 4)
    break  # br_table
    var2 = 3
    var3 = i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 192)
    var4 = (var4 & 65535)
    if ((1 if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 192) != ((var4 & 65535) if (1 if var4 != 3 else 0) else 0) else 0) & (1 if var3 != 4 else 0)):
        break
    i32_store8(var18 + 123, 3)
    break
    if var2:
        break
    var11 = 0
    break
    var5 = ((var23 * 404) + 9568320)
    while True:  # loop $label20
        var6 = var2
        var14 = (var2 & 255)
        var2 = (((var2 & 255) * 40) + 9671200)
        var3 = i32_load((((var2 & 255) * 40) + 9671200) + 28)
        if i32_load((((var2 & 255) * 40) + 9671200) + 28):
            # call_indirect via table[var3]
            if call_indirect(var3):
                break
        var3 = var5
        var4 = i32_load(var2 + 4)
        # br_table ['$label16', '$label17', '$label18', '$label17']
        _br_idx = (i32_load(var2 + 4) + 2)
        break  # br_table
        break
        var3 = (((i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704)) + (var4 << 2)) + 283984)
        var4 = i32_load(var3)
        var2 = i32_load8_u(var18 + 123)
        if (1 if var14 != i32_load8_u(var18 + 123) else 0):
            continue
        break  # end loop
    var11 = (4 if (1 if (var6 & 255) == 69 else 0) else var4)
    var3 = (var21 + (var0 * 132))
    var2 = i32_load((var21 + (var0 * 132)) + 32)
    if (1 if i32_load((var21 + (var0 * 132)) + 32) == i32_load(var3 + 28) else 0):
        break
    if var2:
        break
    var4 = i32_load(((var23 * 404) + 9568096) + 216)
    if (1 if i32_load(((var23 * 404) + 9568096) + 216) == 0 else 0):
        break
    var2 = (var21 + (var0 * 132))
    var14 = (var21 + (var0 * 132))
    var10 = i32_load16_u(var2 + 116)
    var5 = 0
    var6 = 1
    while True:  # loop $label24
        if (1 if var10 == (var5 + var17) else 0):
            var8 = i32_load16_u(var14 + 118)
            var2 = 0
            while True:  # loop $label23
                if (1 if (var2 + var12) == var8 else 0):
                    break
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != var4 else 0):
                    continue
                break  # end loop
        var5 = (var5 + 1)
        var6 = (1 if (var5 + 1) < var4 else 0)
        if (1 if var4 != var5 else 0):
            continue
        break
        break  # end loop
    if (var6 & 1):
        break
    var24 = var3
    var28 = ((var23 * 404) + 9568096)
    var14 = i32_load(((var23 * 404) + 9568096) + 208)
    var6 = ((i32_load8_u(var7 + 122) * 404) + 9568096)
    if i32_load(((i32_load8_u(var7 + 122) * 404) + 9568096) + 216):
        var3 = (var6 + 216)
        var5 = (var6 + 208)
        var10 = i32_load(9142840)
        var8 = i32_load16_u(var7 + 114)
        var13 = i32_load16_u(var7 + 112)
        var4 = 0
        while True:  # loop $label26
            var4 = (var4 + 1)
            var15 = ((var4 + 1) + var13)
            var2 = 0
            while True:  # loop $label25
                var2 = (var2 + 1)
                var16 = (i32_load(9142440) + 2)
                i32_store((var10 + ((var15 + ((((var2 + 1) + var8) + ((i32_load(9142440) + 2) * i32_load(var5))) * var16)) << 2)), i32_load(var6 + 212))
                var16 = i32_load(var3)
                if (1 if var2 < i32_load(var3) else 0):
                    continue
                break  # end loop
            if (1 if var4 < var16 else 0):
                continue
            break  # end loop
    var2 = i32_load(var24 + 32)
    if i32_load(var24 + 32):
        var4 = i32_load(9671128)
        var13 = (i32_load(9671128) + (var2 * 132))
        if (1 if i32_load8_u((i32_load(9671128) + (var2 * 132)) + 125) != 3 else 0):
            if (1 if i32_load8_u(var13 + 128) == 0 else 0):
                break
            if (1 if i32_load8_u((i32_load(9143004) + (i32_load16_u(var7 + 110) + (i32_load(9142892) * i32_load16_u((var4 + (var2 * 132)) + 110))))) == 0 else 0):
                break
        break
        if (1 if var11 < 2 else 0):
            break
        var2 = (var4 + (var2 * 132))
        var4 = i32_load8_u((var4 + (var2 * 132)) + 122)
        var6 = ((i32_load8_u((var4 + (var2 * 132)) + 122) * 404) + 9568096)
        var16 = i32_load(((i32_load8_u((var4 + (var2 * 132)) + 122) * 404) + 9568096) + 216)
        var10 = i32_load16_u(var2 + 112)
        var19 = (i32_load(((i32_load8_u((var4 + (var2 * 132)) + 122) * 404) + 9568096) + 216) + i32_load16_u(var2 + 112))
        if (1 if (i32_load(((i32_load8_u((var4 + (var2 * 132)) + 122) * 404) + 9568096) + 216) + i32_load16_u(var2 + 112)) > var10 else 0):
            var8 = i32_load16_u(var2 + 114)
            var20 = (i32_load16_u(var2 + 114) + i32_load(var6 + 220))
            if (1 if (i32_load16_u(var2 + 114) + i32_load(var6 + 220)) > var8 else 0):
                break
        var6 = 1
        break
        var22 = i32_load(((var4 * 404) + 9568096) + 372)
        var6 = 2147483647
        var4 = var10
        while True:  # loop $label32
            var25 = (var4 - var10)
            var2 = (var4 - var17)
            var26 = ((var4 - var17) * var2)
            var2 = var8
            while True:  # loop $label31
                var15 = (var2 - var12)
                var15 = (((var2 - var12) * var15) + var26)
                var15 = ((1 if i32_load8_u((var22 + (var25 + ((var2 - var8) * var16)))) != 0 else 0) & (1 if var6 > var15 else 0))
                var6 = ((((var2 - var12) * var15) + var26) if ((1 if i32_load8_u((var22 + (var25 + ((var2 - var8) * var16)))) != 0 else 0) & (1 if var6 > var15 else 0)) else var6)
                var5 = (var4 if var15 else var5)
                var3 = (var2 if var15 else var3)
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != var20 else 0):
                    continue
                break  # end loop
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var19 else 0):
                continue
            break  # end loop
        i32_store(var9 + 24, var3)
        i32_store(var9 + 28, var5)
        if (1 if var6 == 2147483647 else 0):
            break
        var2 = (var17 - var5)
        var2 = (var12 - var3)
        if (1 if ((((var17 - var5) * var2) + ((var12 - var3) * var2)) - 1) > (var11 * var11) else 0):
            break
        break
        var6 = 1
        var2 = func235((var9 + 28), (var9 + 24), var7, var13, 0)
        if (1 if var11 > 1 else 0):
            break
        if var2:
            break
        var32 = i32_load8_u(var18 + 123)
        var33 = i32_load16_u(var7 + 112)
        var22 = i32_load16_u(var7 + 114)
        var25 = i32_load(((var23 * 404) + 9568096) + 212)
        var26 = ((i32_load8_u(var13 + 122) * 404) + 9568096)
        var4 = 2147483647
        var34 = i32_load16_u(var13 + 112)
        var15 = i32_load16_u(var13 + 112)
        var35 = i32_load16_u(var13 + 114)
        var16 = i32_load16_u(var13 + 114)
        var27 = 1
        var11 = 1
        while True:  # loop $label44
            var15 = (var15 + 1)
            var16 = (var16 + 1)
            var5 = (var34 - var11)
            var2 = i32_load(var26 + 216)
            var3 = (var11 << 1)
            var10 = (var5 + (i32_load(var26 + 216) + (var11 << 1)))
            if (1 if (var34 - var11) >= (var5 + (i32_load(var26 + 216) + (var11 << 1))) else 0):
                break
            var6 = (var35 - var11)
            var8 = i32_load(var26 + 220)
            var3 = (var6 + (var3 + i32_load(var26 + 220)))
            if (1 if (var35 - var11) >= (var6 + (var3 + i32_load(var26 + 220))) else 0):
                break
            var36 = (var10 - 1)
            var37 = (var3 - 1)
            var38 = (var2 + var15)
            var29 = (var8 + var16)
            var19 = 0
            var3 = var5
            while True:  # loop $label42
                var10 = (var3 + 1)
                var2 = (var3 - var33)
                var30 = ((var3 - var33) * var2)
                var31 = i32_load(9142840)
                if (1 if var3 == var36 else 0):
                    break
                if (1 if var3 == var5 else 0):
                    break
                var2 = var6
                while True:  # loop $label36
                    if ((1 if var2 != var6 else 0) & (1 if var2 != var37 else 0)):
                        break
                    var8 = i32_load(9142440)
                    if (1 if i32_load(9142440) <= var2 else 0):
                        break
                    if (1 if (var2 | var3) < 0 else 0):
                        break
                    if (1 if var3 >= var8 else 0):
                        break
                    var8 = (var8 + 2)
                    if (1 if i32_load((var31 + ((var10 + (((var2 + ((var8 + 2) * var14)) + 1) * var8)) << 2))) != var25 else 0):
                        break
                    var8 = (var2 - var22)
                    var8 = (((var2 - var22) * var8) + var30)
                    if (1 if (((var2 - var22) * var8) + var30) >= var4 else 0):
                        break
                    i32_store(var9 + 28, var3)
                    i32_store(var9 + 24, var2)
                    var19 = 1
                    var4 = var8
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != var29 else 0):
                        continue
                    break  # end loop
                break
                var13 = i32_load(9142440)
                var2 = var6
                while True:  # loop $label41
                    if (1 if var2 >= var13 else 0):
                        break
                    if (1 if (var2 | var3) < 0 else 0):
                        break
                    if (1 if var3 < var13 else 0):
                        break
                    break
                    var20 = (var2 + 1)
                    var8 = (var13 + 2)
                    if (1 if var25 != i32_load((var31 + ((var10 + (((var2 + 1) + ((var13 + 2) * var14)) * var8)) << 2))) else 0):
                        break
                    var8 = (var2 - var22)
                    var8 = (((var2 - var22) * var8) + var30)
                    if (1 if var4 <= (((var2 - var22) * var8) + var30) else 0):
                        break
                    i32_store(var9 + 28, var3)
                    i32_store(var9 + 24, var2)
                    var13 = i32_load(9142440)
                    var19 = 1
                    var4 = var8
                    var2 = var20
                    if (1 if var20 != var20 else 0):
                        continue
                    break  # end loop
                var3 = var10
                if (1 if var10 != var38 else 0):
                    continue
                break  # end loop
            if var19:
                break
            var27 = (1 if var11 < 19 else 0)
            var11 = (var11 + 1)
            if (1 if (var11 + 1) != 20 else 0):
                continue
            break  # end loop
        if var27:
            var6 = (1 if var32 == 0 else 0)
            break
        func140(var7)
        break
    var2 = (var21 + (var0 * 132))
    var5 = i32_load16_u((var21 + (var0 * 132)) + 116)
    i32_store(var9 + 28, i32_load16_u((var21 + (var0 * 132)) + 116))
    var10 = i32_load16_u(var2 + 118)
    i32_store(var9 + 24, i32_load16_u(var2 + 118))
    if (1 if var11 < 2 else 0):
        break
    var3 = i32_load(((var23 * 404) + 9568096) + 216)
    if (1 if i32_load(((var23 * 404) + 9568096) + 216) == 0 else 0):
        break
    var8 = (var11 * var11)
    var6 = 0
    var4 = 1
    while True:  # loop $label48
        var2 = (var5 - (var6 + var17))
        var11 = (((var5 - (var6 + var17)) * var2) - 1)
        var2 = 0
        while True:  # loop $label46
            var13 = (var10 - (var2 + var12))
            if (1 if var8 < (var11 + ((var10 - (var2 + var12)) * var13)) else 0):
                var2 = (var2 + 1)
                if (1 if var3 != (var2 + 1) else 0):
                    continue
                break
            break  # end loop
        if (var4 & 1):
            break
        break
        var6 = (var6 + 1)
        var4 = (1 if (var6 + 1) < var3 else 0)
        if (1 if var3 != var6 else 0):
            continue
        break  # end loop
    var6 = 1
    var2 = (i32_load(9142440) + 2)
    if (1 if i32_load((i32_load(9142840) + ((var5 + (((var10 + ((i32_load(9142440) + 2) * var14)) + 1) * var2)) << 2)) + 4) < 3 else 0):
        break
    var29 = i32_load(var28 + 208)
    var2 = ((var23 * 404) + 9568096)
    var30 = i32_load(((var23 * 404) + 9568096) + 212)
    var15 = i32_load(var2 + 216)
    var31 = i32_load(var9 + 24)
    var32 = i32_load(var9 + 28)
    var13 = 1
    while True:  # loop $label60
        var2 = ((var13 << 1) | 1)
        var8 = (var32 - var13)
        var33 = (((var13 << 1) | 1) + (var32 - var13))
        var16 = ((((var13 << 1) | 1) + (var32 - var13)) - 1)
        var11 = (var31 - var13)
        var19 = (var2 + (var31 - var13))
        var20 = ((var2 + (var31 - var13)) - 1)
        var2 = var8
        var4 = 2147483647
        while True:  # loop $label59
            var3 = (var2 - var17)
            var22 = ((var2 - var17) * var3)
            var3 = var11
            var5 = var11
            var34 = (var2 + var15)
            if (1 if var2 < (var2 + var15) else 0):
                while True:  # loop $label54
                    if (1 if var2 == var8 else 0):
                        break
                    if (1 if var3 == var11 else 0):
                        break
                    if (1 if var3 == var20 else 0):
                        break
                    if (1 if var2 != var16 else 0):
                        break
                    var5 = i32_load(9142440)
                    if (1 if i32_load(9142440) <= var3 else 0):
                        break
                    if (1 if (var2 | var3) < 0 else 0):
                        break
                    if (1 if var2 >= var5 else 0):
                        break
                    var25 = (var3 + var15)
                    if (1 if var3 < (var3 + var15) else 0):
                        var35 = (var5 + 2)
                        var36 = ((var5 + 2) * var29)
                        var26 = 0
                        var37 = i32_load(9671128)
                        var38 = i32_load(9142840)
                        var10 = var3
                        while True:  # loop $label53
                            var10 = (var10 + 1)
                            var39 = (((var10 + 1) + var36) * var35)
                            var5 = var2
                            while True:  # loop $label52
                                var5 = (var5 + 1)
                                var27 = i32_load((var38 + (((var5 + 1) + var39) << 2)))
                                if (1 if var30 != i32_load((var38 + (((var5 + 1) + var39) << 2))) else 0):
                                    if (1 if var27 == -1 else 0):
                                        break
                                    if (1 if i32_load8_u((var37 + (var27 * 132)) + 125) != 1 else 0):
                                        break
                                if (1 if var5 != var34 else 0):
                                    continue
                                break  # end loop
                            var26 = (1 if var10 >= var25 else 0)
                            if (1 if var10 != var25 else 0):
                                continue
                            break  # end loop
                        if (1 if var26 == 0 else 0):
                            break
                    var5 = (var3 - var12)
                    var5 = (((var3 - var12) * var5) + var22)
                    if (1 if (((var3 - var12) * var5) + var22) >= var4 else 0):
                        break
                    i32_store(var9 + 28, var2)
                    i32_store(var9 + 24, var3)
                    var4 = var5
                    var3 = (var3 + 1)
                    if (1 if (var3 + 1) < var19 else 0):
                        continue
                    break
                    break  # end loop
                raise RuntimeError('unreachable')
            while True:  # loop $label58
                if (1 if var2 == var8 else 0):
                    break
                if (1 if var5 == var11 else 0):
                    break
                if (1 if var5 == var20 else 0):
                    break
                if (1 if var2 != var16 else 0):
                    break
                var3 = i32_load(9142440)
                if (1 if i32_load(9142440) <= var5 else 0):
                    break
                if (1 if (var2 | var5) < 0 else 0):
                    break
                if (1 if var2 >= var3 else 0):
                    break
                var3 = (var5 - var12)
                var3 = (((var5 - var12) * var3) + var22)
                if (1 if (((var5 - var12) * var3) + var22) >= var4 else 0):
                    break
                i32_store(var9 + 28, var2)
                i32_store(var9 + 24, var5)
                var4 = var3
                var5 = (var5 + 1)
                if (1 if (var5 + 1) < var19 else 0):
                    continue
                break  # end loop
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < var33 else 0):
                continue
            break  # end loop
        if (1 if var4 == 2147483647 else 0):
            var13 = (var13 + 1)
            if (1 if (var13 + 1) != 20 else 0):
                continue
        break  # end loop
    var5 = ((var23 * 404) + 9568096)
    var10 = i32_load(((var23 * 404) + 9568096) + 216)
    if (1 if i32_load(((var23 * 404) + 9568096) + 216) == 0 else 0):
        break
    var3 = 0
    var8 = i32_load(var9 + 24)
    var11 = i32_load(var9 + 28)
    var4 = 1
    while True:  # loop $label64
        var2 = 0
        if (1 if var11 == (var3 + var17) else 0):
            while True:  # loop $label63
                if (1 if (var2 + var12) == var8 else 0):
                    break
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != var10 else 0):
                    continue
                break  # end loop
        var3 = (var3 + 1)
        var4 = (1 if (var3 + 1) < var10 else 0)
        if (1 if var3 != var10 else 0):
            continue
        break
        break  # end loop
    var2 = i32_load8_u(var18 + 129)
    if (1 if (var6 | (1 if i32_load8_u(var18 + 129) != 5 else 0)) == 0 else 0):
        i32_store8(var18 + 129, 0)
        var2 = 0
    var3 = i32_load8_u(var18 + 123)
    if ((1 if i32_load8_u(var18 + 123) == 0 else 0) | var6):
        break
    if ((1 if var3 == 6 else 0) & (1 if var2 != 9 else 0)):
        break
    func140(var7)
    break
    if (var4 & 1):
        break
    if (1 if i32_load8_u(var18 + 129) == 6 else 0):
        break
    var2 = ((var23 * 404) + 9568096)
    var3 = ((var23 * 404) + 9568096)
    var11 = i32_load(var9 + 28)
    var4 = i32_load(var9 + 24)
    var2 = (var21 + (var0 * 132))
    var18 = (var21 + (var0 * 132))
    if func177(var17, var12, i32_load(var9 + 28), i32_load(var9 + 24), i32_load(var2 + 212), var14, (var9 + 20), (var9 + 16), i32_load(var5 + 216), ((var21 + (var0 * 132)) + 56), (var2 + 130), 0):
        break
    var2 = i32_load(var24 + 32)
    if (1 if i32_load(var24 + 32) == 0 else 0):
        break
    var6 = (var17 - var11)
    var6 = (var12 - var4)
    if (1 if ((((var17 - var11) * var6) + ((var12 - var4) * var6)) - 1) > 196 else 0):
        break
    var4 = i32_load(var9 + 24)
    var11 = i32_load(var9 + 28)
    if (1 if i32_load(var9 + 28) != var17 else 0):
        break
    if (1 if var4 != var12 else 0):
        break
    break
    i32_store(var9 + 12, 0)
    var6 = (var9 + 20)
    var10 = (var9 + 16)
    var8 = i32_load(var5 + 216)
    if (1 if i32_load(var5 + 216) == 0 else 0):
        break
    var24 = (var17 + 1)
    var13 = (var12 + 1)
    var5 = 0
    var15 = (i32_load(9142440) + 2)
    var16 = (var14 * (i32_load(9142440) + 2))
    var19 = i32_load(var3 + 212)
    var20 = i32_load(9142840)
    var22 = i32_load(var9 + 16)
    var25 = i32_load(var9 + 20)
    var14 = 0
    while True:  # loop $label72
        var26 = ((var5 + var24) + var25)
        var2 = 0
        while True:  # loop $label70
            if (1 if var19 == i32_load((var20 + ((var26 + ((((var2 + var13) + var22) + var16) * var15)) << 2))) else 0):
                var2 = (var2 + 1)
                if (1 if var8 != (var2 + 1) else 0):
                    continue
                break
            break  # end loop
        var14 = 1
        var5 = (var5 + 1)
        if (1 if (var5 + 1) != var8 else 0):
            continue
        break  # end loop
    if (1 if var14 == 0 else 0):
        break
    var2 = i32_load(var18 + 56)
    var18 = (((i32_load(var18 + 56) & 0xFFFFFFFF) >> 16) if var2 else var4)
    var4 = ((((i32_load(var18 + 56) & 0xFFFFFFFF) >> 16) if var2 else var4) + (i32_load(var9 + 16) - var12))
    var13 = ((var2 & 65535) if var2 else var11)
    var2 = (((var2 & 65535) if var2 else var11) + (i32_load(var9 + 20) - var17))
    var4 = ((((((i32_load(var18 + 56) & 0xFFFFFFFF) >> 16) if var2 else var4) + (i32_load(var9 + 16) - var12)) * var4) + ((((var2 & 65535) if var2 else var11) + (i32_load(var9 + 20) - var17)) * var2))
    var10 = 0
    var15 = (i32_load(9142440) + 2)
    var16 = ((i32_load(9142440) + 2) * i32_load(var28 + 208))
    var19 = i32_load(9142840)
    var20 = i32_load(var3 + 212)
    var11 = 55
    var28 = (1 if var8 <= 0 else 0)
    while True:  # loop $label77
        var2 = (var10 << 3)
        var3 = (i32_load(((var10 << 3) + 8932)) + var12)
        var5 = (i32_load((var2 + 8928)) + var17)
        if var28:
            break
        var14 = (var5 + var8)
        var2 = (var3 + var8)
        var22 = ((var3 + var8) if (1 if var2 > var3 else 0) else var3)
        var24 = 1
        var6 = var5
        while True:  # loop $label74
            var6 = (var6 + 1)
            var2 = var3
            while True:  # loop $label76
                if (1 if var2 == var22 else 0):
                    if (1 if var6 < var14 else 0):
                        continue
                    if (1 if var24 == 0 else 0):
                        break
                    break
                var2 = (var2 + 1)
                if (1 if i32_load((var19 + (((((var2 + 1) + var16) * var15) + var6) << 2))) == var20 else 0):
                    continue
                break  # end loop
            var24 = 0
            if (1 if var6 < var14 else 0):
                continue
            break  # end loop
        break
        var2 = (var3 - var18)
        var2 = (var5 - var13)
        var2 = (((var3 - var18) * var2) + ((var5 - var13) * var2))
        var2 = (1 if var2 < var4 else 0)
        var4 = ((((var3 - var18) * var2) + ((var5 - var13) * var2)) if (1 if var2 < var4 else 0) else var4)
        var11 = (var10 if var2 else var11)
        var10 = (var10 + 1)
        if (1 if (var10 + 1) != 8 else 0):
            continue
        break  # end loop
    if (1 if var11 == 55 else 0):
        break
    var2 = (var11 << 3)
    var10 = ((var11 << 3) + 8932)
    var6 = (var2 + 8928)
    var3 = i32_load(var6)
    if (1 if (i32_load(var6) - 2) < -3 else 0):
        break
    var2 = i32_load(var10)
    if (1 if i32_load(var10) > 1 else 0):
        break
    if (1 if var2 < -1 else 0):
        break
    var4 = i32_load(9142440)
    var6 = (var2 + var12)
    if (1 if i32_load(9142440) <= (var2 + var12) else 0):
        break
    var5 = (var3 + var17)
    if (1 if (var6 | (var3 + var17)) < 0 else 0):
        break
    if (1 if var4 > var5 else 0):
        break
    func140(var7)
    break
    var5 = i32_load(((var23 * 404) + 9568096) + 260)
    if (1 if i32_load(((var23 * 404) + 9568096) + 260) == 0 else 0):
        break
    var4 = i32_load(((i32_load8_u(var7 + 122) * 404) + 9568096) + 260)
    if i32_load(((i32_load8_u(var7 + 122) * 404) + 9568096) + 260):
        var4 = (32000 // var4)
        # Unknown: i32.extend16_s []
    else:
    var40 = 1.0
    var0 = (var21 + (var0 * 132))
    var6 = i32_load8_u((var21 + (var0 * 132)) + 124)
    var4 = 6
    var12 = (((var2 * 3) + var3) + 4)
    if (1 if (((var2 * 3) + var3) + 4) <= 8 else 0):
        var4 = i32_load8_u((var12 + 10184))
    i32_store8(var0 + 124, var4)
    var12 = (1 if var1 == 1 else 0)
    var4 = func289(var7, ((1 if var1 == 1 else 0) | (1 if var6 != (var4 & 255) else 0)), 0.0)
    if var12:
        break
    if var4:
        break
    if i32_load8_u(9147124):
        break
    var4 = (1 if i32_load8_u(9142916) == 0 else 0)
    break
    var40 = (32000.0 / var40)
    func92(var7, ((32000.0 / var40) * float(var3)), (var40 * float(var2)))
    var12 = i32_load8_u(9142916)
    var4 = (1 if i32_load8_u(9142916) == 0 else 0)
    if (1 if var1 != 1 else 0):
        break
    if (1 if var12 == 0 else 0):
        break
    if var4:
        break
    if (1 if var6 == i32_load8_u(var0 + 124) else 0):
        break
    if (1 if i32_load8_u(59181) == 0 else 0):
    i32_store16(var7 + 112, (i32_load16_u(var7 + 112) + var3))
    i32_store16(var7 + 114, (i32_load16_u(var7 + 114) + var2))
    var0 = ((i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704)) + 281740)
    i32_store(((i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704)) + 281740), (i32_load(var0) + 1))
    var0 = i32_load(9215884)
    i32_store((i32_load(9215884) + (i32_load(var7 + 44) << 4)) + 12, (var1 + 1))
    i32_store((var0 + (i32_load(var7 + 44) << 4)), (i32_load(9142848) + (((32000 // var5) & 0xFFFFFFFF) // 25)))
    i32_store8(var7 + 125, 1)
    var0 = 0
    var2 = ((i32_load8_u(var7 + 122) * 404) + 9568096)
    if i32_load(((i32_load8_u(var7 + 122) * 404) + 9568096) + 216):
        var3 = i32_load(9142840)
        var4 = i32_load16_u(var7 + 114)
        var6 = i32_load16_u(var7 + 112)
        while True:  # loop $label86
            var0 = (var0 + 1)
            var5 = ((var0 + 1) + var6)
            var1 = 0
            while True:  # loop $label85
                var1 = (var1 + 1)
                var12 = (i32_load(9142440) + 2)
                i32_store((var3 + ((var5 + ((((var1 + 1) + var4) + ((i32_load(9142440) + 2) * i32_load(var2 + 208))) * var12)) << 2)), i32_load(var7 + 28))
                var12 = i32_load(var2 + 216)
                if (1 if var1 < i32_load(var2 + 216) else 0):
                    continue
                break  # end loop
            if (1 if var0 < var12 else 0):
                continue
            break  # end loop
    func118(var7)
    break
    func140(var7)
    global global0
    global0 = (var9 + 32)
    return func160(var7, var3, var2)

