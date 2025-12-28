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
# $ve
# Export: ve
# ==========================================================
def ve(var0):
    """Export: ve"""
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
    var10 = i32_load(var0 + 32)
    var4 = i32_load(var0 + 12)
    i32_store(9140308, 0)
    var2 = (var4 + 16)
    var3 = i32_load(var4)
    var6 = i32_load(var4 + 12)
    if i32_load(var4 + 12):
        var1 = i32_load(var4 + 8)
        i32_store(9147292, i32_load(var4 + 4))
        i32_store(9147296, var1)
        var7 = i32_load(9687256)
        i32_store(9687256, var0)
        i32_store(9140324, 0)
        if var3:
            var9 = (var3 & 1)
            if (1 if var3 == 1 else 0):
                var0 = 0
                break
            var8 = (var3 & -2)
            var0 = 0
            var1 = 0
            while True:  # loop $label5
                var11 = ((var5 * 60) + var2)
                # br_table ['$label1', '$label2', '$label1', '$label2']
                _br_idx = (i32_load(((var5 * 60) + var2) + 32) - 23)
                break  # br_table
                var0 = (var0 + 1)
                i32_store(9140324, (var0 + 1))
                # br_table ['$label3', '$label4', '$label3', '$label4']
                _br_idx = (i32_load(var11 + 92) - 23)
                break  # br_table
                var0 = (var0 + 1)
                i32_store(9140324, (var0 + 1))
                var5 = (var5 + 2)
                var1 = (var1 + 2)
                if (1 if (var1 + 2) != var8 else 0):
                    continue
                break  # end loop
            var1 = ((var5 * 15) + 8)
            if (1 if var9 == 0 else 0):
                break
            # br_table ['$label7', '$label6', '$label7', '$label6']
            _br_idx = (i32_load((var2 + (var1 << 2))) - 23)
            break  # br_table
            var0 = (var0 + 1)
            i32_store(9140324, (var0 + 1))
        else:
        i32_store((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)), func26(0))
        i32_store(9684504, (var4 + var6))
        i32_store(9684500, var2)
        i32_store(9687244, var3)
        i32_store(9147300, (((var10 - var6) & 0xFFFFFFFF) >> 2))
        i32_store(9140324, 0)
        if (1 if var7 == 0 else 0):
            break
        if (1 if var3 == 0 else 0):
            break
        var0 = 0
        if (1 if var3 != 1 else 0):
            var5 = (var3 & -2)
            var1 = 0
            while True:  # loop $label12
                var4 = (var2 + (var0 * 60))
                var10 = i32_load((var2 + (var0 * 60)) + 28)
                if (1 if i32_load((var2 + (var0 * 60)) + 28) > 9999 else 0):
                    break
                var9 = i32_load(var4 + 32)
                if (1 if i32_load(var4 + 32) > 22 else 0):
                    break
                if (1 if ((1 << var9) & 4194400) == 0 else 0):
                    break
                i32_store(((var10 * 404) + 9568096) + 20, 0)
                var10 = i32_load(var4 + 88)
                if (1 if i32_load(var4 + 88) > 9999 else 0):
                    break
                var4 = i32_load(var4 + 92)
                if (1 if i32_load(var4 + 92) > 22 else 0):
                    break
                if (1 if ((1 << var4) & 4194400) == 0 else 0):
                    break
                i32_store(((var10 * 404) + 9568096) + 20, 0)
                var0 = (var0 + 2)
                var1 = (var1 + 2)
                if (1 if (var1 + 2) != var5 else 0):
                    continue
                break  # end loop
            var0 = (var0 * 15)
        if (1 if (var3 & 1) == 0 else 0):
            break
        var0 = (var2 + (var0 << 2))
        var1 = i32_load((var2 + (var0 << 2)) + 28)
        if (1 if i32_load((var2 + (var0 << 2)) + 28) > 9999 else 0):
            break
        var0 = i32_load(var0 + 32)
        if (1 if i32_load(var0 + 32) > 22 else 0):
            break
        if (1 if ((1 << var0) & 4194400) == 0 else 0):
            break
        i32_store(((var1 * 404) + 9568096) + 20, 0)
        var4 = 1
        if i32_load8_u(59182):
            break
        var2 = i32_load(9671136)
        if (1 if i32_load(9671136) < 4 else 0):
            break
        var5 = i32_load(9671128)
        var0 = 3
        while True:  # loop $label36
            var3 = (var5 + (var0 * 132))
            if (1 if i32_load8_u((var5 + (var0 * 132)) + 125) == 3 else 0):
                break
            var10 = i32_load(var3 + 48)
            if (1 if i32_load(var3 + 48) == 0 else 0):
                break
            var1 = i32_load8_u(var3 + 122)
            # br_table ['$label15', '$label16', '$label17', '$label18', '$label19', '$label14', '$label14', '$label20', '$label21', '$label22', '$label23', '$label24', '$label25', '$label26', '$label27', '$label28', '$label29', '$label30', '$label31', '$label32', '$label33', '$label34', '$label14']
            _br_idx = i32_load(var10 + 32)
            break  # br_table
            break
            break
            break
            break
            break
            break
            break
            break
            break
            break
            break
            break
            break
            break
            break
            break
            break
            break
            break
            i32_store(((var1 * 72) + 9263872) + 48, i32_load(((var1 * 72) + 9263880)))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var2 else 0):
                continue
            break  # end loop
        func383(((var1 * 72) + 9263924), var7)
        break
    i32_store(9687248, var3)
    i32_store(9684496, var2)
    var4 = 0
    var3 = i32_load(9142524)
    var2 = i32_load(9142532)
    var0 = 0
    while True:  # loop $label44
        var5 = ((var0 * 404) + 9568096)
        if (1 if i32_load(((var0 * 404) + 9568096) + 264) != 2 else 0):
            break
        var1 = var2
        # br_table ['$label39', '$label40', '$label38']
        _br_idx = i32_load(var5 + 268)
        break  # br_table
        var1 = var3
        i32_store(((var0 * 72) + 9263856), var1)
        var5 = (var0 | 1)
        if (1 if (var0 | 1) != 255 else 0):
            var7 = ((var5 * 404) + 9568096)
            if (1 if i32_load(((var5 * 404) + 9568096) + 264) != 2 else 0):
                break
            var1 = var2
            # br_table ['$label42', '$label43', '$label41']
            _br_idx = i32_load(var7 + 268)
            break  # br_table
            var1 = var3
            i32_store(((var5 * 72) + 9263856), var1)
            var0 = (var0 + 2)
            continue
        break  # end loop
    if (1 if ((1 if var6 == 0 else 0) | var4) == 0 else 0):
        if i32_load8_u(9687269):
            var3 = 3
            if (1 if i32_load(9671136) > 3 else 0):
                while True:  # loop $label50
                    var0 = (i32_load(9671128) + (var3 * 132))
                    func157((i32_load(9671128) + (var3 * 132)))
                    var1 = i32_load(var0 + 20)
                    if i32_load(var0 + 20):
                        i32_store(var1 + 8, 0)
                    i32_store(var0 + 44, 0)
                    if (1 if i32_load8_u(var0 + 125) != 4 else 0):
                        i32_store8(var0 + 125, 0)
                    i32_store8(var0 + 123, 0)
                    i32_store16(var0 + 108, 0)
                    i32_store(var0 + 88, 0)
                    i32_store(var0 + 96, 0)
                    if (1 if i32_load8_u(var0 + 126) != 1 else 0):
                        break
                    var1 = (i32_load(9671128) + (i32_load(var0 + 28) * 132))
                    i32_store8((i32_load(9671128) + (i32_load(var0 + 28) * 132)) + 126, 0)
                    i32_store(var1 + 52, (i32_load(var1 + 52) - (((i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 296) * i32_load(((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 284144))) & 0xFFFFFFFF) // 100)))
                    if (1 if i32_load(var1 + 92) == 0 else 0):
                        break
                    if i32_load(9140316):
                        if (1 if i32_load(9140320) != i32_load(var1 + 28) else 0):
                            break
                    i64_store(var0 + 100, 0)
                    i32_store(var0 + 56, 0)
                    i32_store16(var0 + 127, 0)
                    i32_store(var0 + 32, -1)
                    if (1 if i32_load8_u(var0 + 129) != 8 else 0):
                        i32_store8(var0 + 129, 0)
                    if (1 if i32_load(9147132) == 0 else 0):
                        break
                    if (1 if i32_load(38788) != i32_load8_u(var0 + 122) else 0):
                        break
                    i32_store(var0 + 84, (i32_load(var0 + 84) + 1))
                    # br_table ['$label47', '$label48', '$label48', '$label48', '$label48', '$label48', '$label48', '$label48', '$label48', '$label48', '$label47', '$label48']
                    _br_idx = (i32_load8_u(var0 + 125) - 4)
                    break  # br_table
                    var1 = i32_load16_u(var0 + 110)
                    var2 = i32_load8_u(var0 + 122)
                    var4 = i32_load(9561692)
                    break
                    var4 = i32_load(9561692)
                    var1 = i32_load16_u(var0 + 110)
                    var2 = i32_load8_u(var0 + 122)
                    var0 = (((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + (i32_load8_u(var0 + 122) << 2)) + 282828)
                    i32_store((((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + (i32_load8_u(var0 + 122) << 2)) + 282828), (i32_load(var0) + 1))
                    var0 = (var4 + (var1 * 286704))
                    var2 = i32_load(((var2 * 404) + 9568096) + 280)
                    var1 = (i32_load(((var2 * 404) + 9568096) + 280) + i32_load(var0 + 283976))
                    i32_store((var4 + (var1 * 286704)) + 283976, (i32_load(((var2 * 404) + 9568096) + 280) + i32_load(var0 + 283976)))
                    if (1 if var2 < 0 else 0):
                        i32_store8(var0 + 286700, 1)
                    var0 = (var0 + 281748)
                    if (1 if var1 > i32_load((var0 + 281748)) else 0):
                        i32_store(var0, var1)
                    var3 = (var3 + 1)
                    if (1 if (var3 + 1) < i32_load(9671136) else 0):
                        continue
                    break  # end loop
        i32_store8(9687268, 1)
        var2 = 0
        var10 = 0
        var13 = (global0 - 16)
        global global0
        global0 = (global0 - 16)
        while True:  # loop $label83
            var5 = ((var10 * 404) + 9568096)
            var17 = i32_load(((var10 * 404) + 9568096) + 224)
            var0 = i32_load(var5 + 200)
            var18 = (i32_load(var5 + 200) if (1 if var0 > var2 else 0) else var2)
            var19 = (1 if i32_load(((var10 * 404) + 9568096) + 224) > (i32_load(var5 + 200) if (1 if var0 > var2 else 0) else var2) else 0)
            var20 = i32_load(var5 + 216)
            if i32_load(var5 + 216):
                var21 = i32_load(var5 + 220)
                var4 = 0
                var1 = i32_load(var5 + 216)
                var22 = (i32_load(var5 + 216) + 2)
                if (1 if (i32_load(var5 + 216) + 2) <= 0 else 0):
                    break
                var3 = i32_load(var5 + 220)
                var11 = (i32_load(var5 + 220) + 2)
                if (1 if (i32_load(var5 + 220) + 2) <= 0 else 0):
                    break
                var2 = i32_load(var5 + 372)
                var23 = ((1 if var1 != 0 else 0) & (1 if var3 != 0 else 0))
                while True:  # loop $label73
                    if (1 if var4 == 0 else 0):
                        if (1 if var23 == 0 else 0):
                            break
                        if (1 if i32_load8_u(var2) == 0 else 0):
                            break
                        var4 = 0
                        var0 = 0
                        break
                    var12 = (var4 - 1)
                    var14 = (1 if (var4 - 1) >= var1 else 0)
                    if (1 if (var4 - 1) >= var1 else 0):
                        break
                    if (1 if var3 == 0 else 0):
                        break
                    if (1 if i32_load8_u((var2 + var12)) == 0 else 0):
                        break
                    var0 = 0
                    break
                    var6 = (var4 - 2)
                    var24 = (1 if var4 == 1 else 0)
                    if (1 if var4 == 1 else 0):
                        break
                    if (1 if var1 <= var6 else 0):
                        break
                    if (1 if var3 == 0 else 0):
                        break
                    if (1 if i32_load8_u((var2 + var6)) == 0 else 0):
                        break
                    var0 = 0
                    break
                    var15 = (1 if var1 <= var4 else 0)
                    if (1 if var1 <= var4 else 0):
                        break
                    if (1 if var3 == 0 else 0):
                        break
                    if (1 if i32_load8_u((var2 + var4)) == 0 else 0):
                        break
                    var0 = 0
                    break
                    var0 = 1
                    if (1 if var11 == 1 else 0):
                        break
                    while True:  # loop $label67
                        var9 = (var0 - 1)
                        if var14:
                            break
                        if (1 if var3 <= var9 else 0):
                            break
                        if i32_load8_u((var2 + ((var1 * var9) + var12))):
                            break
                        if var15:
                            break
                        if (1 if var3 <= var9 else 0):
                            break
                        if i32_load8_u((var2 + ((var1 * var9) + var4))):
                            break
                        var8 = (var0 - 2)
                        var16 = (1 if var0 < 2 else 0)
                        if (1 if var0 < 2 else 0):
                            break
                        if var14:
                            break
                        if (1 if var3 <= var8 else 0):
                            break
                        if i32_load8_u((var2 + ((var1 * var8) + var12))):
                            break
                        var7 = 0
                        if var24:
                            break
                        var7 = 1
                        if (1 if var1 <= var6 else 0):
                            break
                        if (1 if var3 <= var9 else 0):
                            break
                        if i32_load8_u((var2 + ((var1 * var9) + var6))):
                            break
                        if var14:
                            break
                        if (1 if var0 >= var3 else 0):
                            break
                        if i32_load8_u((var2 + ((var0 * var1) + var12))):
                            break
                        if var16:
                            break
                        if var15:
                            break
                        if (1 if var3 <= var8 else 0):
                            break
                        if i32_load8_u((var2 + ((var1 * var8) + var4))):
                            break
                        if ((1 if var7 == 0 else 0) | var16):
                            break
                        if (1 if var1 <= var6 else 0):
                            break
                        if (1 if var3 <= var8 else 0):
                            break
                        if i32_load8_u((var2 + ((var1 * var8) + var6))):
                            break
                        if (1 if var7 == 0 else 0):
                            break
                        if (1 if var1 <= var6 else 0):
                            break
                        if (1 if var0 >= var3 else 0):
                            break
                        if i32_load8_u((var2 + ((var0 * var1) + var6))):
                            break
                        if var15:
                            break
                        if (1 if var0 >= var3 else 0):
                            break
                        if i32_load8_u((var2 + ((var0 * var1) + var4))):
                            break
                        var0 = (var0 + 1)
                        if (1 if (var0 + 1) != var11 else 0):
                            continue
                        break  # end loop
                    break
                    var0 = 1
                    if (1 if var11 == 1 else 0):
                        break
                    while True:  # loop $label72
                        if (1 if var1 == 0 else 0):
                            break
                        var6 = (var0 - 1)
                        if (1 if (var0 - 1) >= var3 else 0):
                            break
                        if i32_load8_u((var2 + (var1 * var6))):
                            break
                        if (1 if var0 < 2 else 0):
                            break
                        if (1 if var1 == 0 else 0):
                            break
                        var6 = (var0 - 2)
                        if (1 if (var0 - 2) >= var3 else 0):
                            break
                        if i32_load8_u((var2 + (var1 * var6))):
                            break
                        if (1 if var1 == 0 else 0):
                            break
                        if (1 if var0 >= var3 else 0):
                            break
                        if (1 if i32_load8_u((var2 + (var0 * var1))) == 0 else 0):
                            break
                        var4 = 0
                        break
                        var0 = (var0 + 1)
                        if (1 if var11 != (var0 + 1) else 0):
                            continue
                        break  # end loop
                    break
                    i32_store(var13 + 12, var4)
                    i32_store(var13 + 8, var0)
                    break
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != var22 else 0):
                        continue
                    break  # end loop
                var11 = (var21 + 2)
                var7 = (var20 + 2)
                var0 = ((var21 + 2) * (var20 + 2))
                var9 = func26((-1 if (var0 & 1610612736) else (((var21 + 2) * (var20 + 2)) << 3)))
                i32_store(var5 + 56, func26((-1 if (var0 & 1610612736) else (((var21 + 2) * (var20 + 2)) << 3))))
                var1 = i32_load(var13 + 12)
                i32_store(var9, i32_load(var13 + 12))
                var3 = i32_load(var13 + 8)
                i32_store(var9 + 4, i32_load(var13 + 8))
                if var0:
                    # Unknown: memory.fill []
                var6 = 2
                i32_store(((((var3 * var7) + var1) << 2) + 59200), 1)
                var1 = 0
                while True:  # loop $label82
                    var4 = var1
                    var1 = (var1 << 2)
                    var0 = i32_load((var9 + (var1 << 2)))
                    var2 = i32_load((var9 + (var1 | 4)))
                    var3 = (var0 + 1)
                    var8 = ((((1 if i32_load((var9 + (var1 << 2))) > -2 else 0) & (1 if i32_load((var9 + (var1 | 4))) >= 0 else 0)) & (1 if (var0 + 1) < var7 else 0)) & (1 if var2 < var11 else 0))
                    var1 = (var4 + 2)
                    if var4:
                        if (1 if var8 == 0 else 0):
                            break
                        var4 = ((((var2 * var7) + var3) << 2) + 59200)
                        if i32_load(((((var2 * var7) + var3) << 2) + 59200)):
                            break
                        if (1 if func93(var3, var2, var5) == 0 else 0):
                            break
                        var8 = (var9 + (var6 << 2))
                        i32_store((var9 + (var6 << 2)), var3)
                        i32_store(var8 + 4, var2)
                        i32_store(var4, 1)
                        var6 = (var6 + 2)
                        var4 = (1 if var0 < 0 else 0)
                        if (1 if var0 < 0 else 0):
                            break
                        if (1 if var2 <= 0 else 0):
                            break
                        if (1 if var0 >= var7 else 0):
                            break
                        if (1 if var2 > var11 else 0):
                            break
                        var3 = (var2 - 1)
                        var8 = (((((var2 - 1) * var7) + var0) << 2) + 59200)
                        if i32_load((((((var2 - 1) * var7) + var0) << 2) + 59200)):
                            break
                        if (1 if func93(var0, var3, var5) == 0 else 0):
                            break
                        var12 = (var9 + (var6 << 2))
                        i32_store((var9 + (var6 << 2)), var0)
                        i32_store(var12 + 4, var3)
                        i32_store(var8, 1)
                        var6 = (var6 + 2)
                        if (1 if var0 <= 0 else 0):
                            break
                        if (1 if var2 < 0 else 0):
                            break
                        if (1 if var0 > var7 else 0):
                            break
                        if (1 if var2 >= var11 else 0):
                            break
                        var3 = (var0 - 1)
                        var8 = ((((var0 - 1) + (var2 * var7)) << 2) + 59200)
                        if i32_load(((((var0 - 1) + (var2 * var7)) << 2) + 59200)):
                            break
                        if (1 if func93(var3, var2, var5) == 0 else 0):
                            break
                        var12 = (var9 + (var6 << 2))
                        i32_store((var9 + (var6 << 2)), var3)
                        i32_store(var12 + 4, var2)
                        i32_store(var8, 1)
                        var6 = (var6 + 2)
                        if var4:
                            break
                        if (1 if var2 < -1 else 0):
                            break
                        if (1 if var0 >= var7 else 0):
                            break
                        var2 = (var2 + 1)
                        if (1 if (var2 + 1) >= var11 else 0):
                            break
                        var8 = ((((var2 * var7) + var0) << 2) + 59200)
                        if i32_load(((((var2 * var7) + var0) << 2) + 59200)):
                            break
                        if func93(var0, var2, var5):
                            break
                        break
                    if (1 if var8 == 0 else 0):
                        break
                    var8 = ((((var2 * var7) + var3) << 2) + 59200)
                    if i32_load(((((var2 * var7) + var3) << 2) + 59200)):
                        break
                    if (1 if func93(var3, var2, var5) == 0 else 0):
                        break
                    var0 = var3
                    break
                    var4 = (1 if var0 < 0 else 0)
                    if (1 if var0 < 0 else 0):
                        break
                    if (1 if var2 <= 0 else 0):
                        break
                    if (1 if var0 >= var7 else 0):
                        break
                    if (1 if var2 > var11 else 0):
                        break
                    var3 = (var2 - 1)
                    var8 = (((((var2 - 1) * var7) + var0) << 2) + 59200)
                    if i32_load((((((var2 - 1) * var7) + var0) << 2) + 59200)):
                        break
                    if (1 if func93(var0, var3, var5) == 0 else 0):
                        break
                    var2 = var3
                    break
                    if (1 if var0 <= 0 else 0):
                        break
                    if (1 if var2 < 0 else 0):
                        break
                    if (1 if var0 > var7 else 0):
                        break
                    if (1 if var2 >= var11 else 0):
                        break
                    var3 = (var0 - 1)
                    var8 = ((((var0 - 1) + (var2 * var7)) << 2) + 59200)
                    if i32_load(((((var0 - 1) + (var2 * var7)) << 2) + 59200)):
                        break
                    if (1 if func93(var3, var2, var5) == 0 else 0):
                        break
                    var0 = var3
                    break
                    if var4:
                        break
                    if (1 if var2 < -1 else 0):
                        break
                    if (1 if var0 >= var7 else 0):
                        break
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) >= var11 else 0):
                        break
                    var8 = ((((var2 * var7) + var0) << 2) + 59200)
                    if i32_load(((((var2 * var7) + var0) << 2) + 59200)):
                        break
                    if (1 if func93(var0, var2, var5) == 0 else 0):
                        break
                    var3 = (var9 + (var6 << 2))
                    i32_store((var9 + (var6 << 2)), var0)
                    i32_store(var3 + 4, var2)
                    i32_store(var8, 1)
                    var6 = (var6 + 2)
                    if (1 if var1 < var6 else 0):
                        continue
                    break  # end loop
                i32_store(var5 + 60, var6)
            var2 = (var17 if var19 else var18)
            var10 = (var10 + 1)
            if (1 if (var10 + 1) != 255 else 0):
                continue
            break  # end loop
        var0 = 0
        var25 = (i64_extend_u((var2 + 5)) * 80)
        var1 = (-1 if i32(((var25 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u((var2 + 5)) * 80)))
        var3 = func26((-1 if i32(((var25 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u((var2 + 5)) * 80))))
        # Unknown: memory.fill []
        i32_store(9142836, var3)
        while True:  # loop $label84
            var1 = ((var0 * 404) + 9568096)
            var3 = i32_load(((var0 * 404) + 9568096) + 200)
            if i32_load(((var0 * 404) + 9568096) + 200):
                func232(var3)
                func232((i32_load(var1 + 200) + 4))
            var7 = 1
            func232(i32_load(var1 + 224))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != 255 else 0):
                continue
            break  # end loop
        var3 = -1
        var10 = 2
        var6 = 0
        var2 = 0
        while True:  # loop $label90
            var4 = (var3 + 1)
            var9 = (var10 - 1)
            var0 = (var6 << 1)
            var11 = ((var6 << 1) + 2)
            var12 = ((var0 - 1) & 3)
            var1 = var3
            while True:  # loop $label89
                var8 = 0
                if (1 if ((1 if var1 != var9 else 0) & (1 if var1 != var3 else 0)) == 0 else 0):
                    var0 = var3
                    while True:  # loop $label85
                        var5 = ((var2 << 2) + 8611904)
                        i32_store(((var2 << 2) + 8611904), var1)
                        i32_store(var5 + 4, var0)
                        var0 = (var0 + 1)
                        var2 = (var2 + 2)
                        var8 = (var8 + 1)
                        if (1 if (var8 + 1) != var12 else 0):
                            continue
                        break  # end loop
                    if (1 if var11 < 3 else 0):
                        break
                    while True:  # loop $label87
                        var5 = ((var2 << 2) + 8611904)
                        i32_store(((var2 << 2) + 8611904), var1)
                        i32_store(var5 + 28, (var0 + 3))
                        i32_store(var5 + 24, var1)
                        i32_store(var5 + 20, (var0 + 2))
                        i32_store(var5 + 16, var1)
                        i32_store(var5 + 12, (var0 + 1))
                        i32_store(var5 + 8, var1)
                        i32_store(var5 + 4, var0)
                        var2 = (var2 + 8)
                        var0 = (var0 + 4)
                        if (1 if (var0 + 4) != var10 else 0):
                            continue
                        break  # end loop
                    break
                var0 = ((var2 << 2) + 8611904)
                i32_store(((var2 << 2) + 8611904), var1)
                i32_store(var0 + 4, var3)
                var2 = (var2 + 2)
                var0 = var4
                if (1 if var6 == -1 else 0):
                    break
                while True:  # loop $label88
                    if (1 if var0 == var9 else 0):
                        var5 = ((var2 << 2) + 8611904)
                        i32_store(((var2 << 2) + 8611904), var1)
                        i32_store(var5 + 4, var0)
                        var2 = (var2 + 2)
                    var5 = (var0 + 1)
                    if (1 if var9 == (var0 + 1) else 0):
                        var8 = ((var2 << 2) + 8611904)
                        i32_store(((var2 << 2) + 8611904), var1)
                        i32_store(var8 + 4, var5)
                        var2 = (var2 + 2)
                    var0 = (var0 + 2)
                    if (1 if (var0 + 2) != var10 else 0):
                        continue
                    break  # end loop
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var10 else 0):
                    continue
                break  # end loop
            var6 = (var6 + 1)
            var3 = (var7 ^ -1)
            var7 = (var7 + 1)
            var10 = (var10 + 1)
            if (1 if (var10 + 1) != 129 else 0):
                continue
            break  # end loop
        global global0
        global0 = (var13 + 16)
        if i32_load8_u(9147212):
            break
        if i32_load8_u(9147213):
            break
        if i32_load8_u(9147152):
            break
        var0 = i32_load(i32_load(9142424) + 184)
        i32_store(9147312, i32_load(i32_load(9142424) + 184))
        i32_store(9147324, (var0 ^ -1))
        i32_store(9147320, (var0 ^ -1515870811))
        i32_store(9147316, (var0 ^ 1515870810))
        Nb()
    i32_store(9687252, (i32_load(9687252) + 1))
    return func350()

