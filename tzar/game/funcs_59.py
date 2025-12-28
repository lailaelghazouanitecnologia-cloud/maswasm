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
# $func380
# ==========================================================
def func380(var0):
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
    # br_table ['$label0', '$label1', '$label2', '$label3', '$label4', '$label5', '$label6', '$label7', '$label8', '$label9', '$label10', '$label11', '$label12', '$label13', '$label14', '$label15', '$label16']
    _br_idx = i32_load(var0)
    break  # br_table
    var10 = func165(var0, 67)
    break
    var10 = func165(var0, 68)
    break
    var10 = func165(var0, 69)
    break
    # br_table ['$label17', '$label18', '$label19']
    _br_idx = i32_load(var0 + 4)
    break  # br_table
    var1 = i32_load(var0 + 88)
    if (1 if i32_load(var0 + 88) == 0 else 0):
        break
    var7 = i32_load(9142420)
    var9 = i32_load(9671128)
    var8 = i32_load(var0 + 80)
    var4 = i32_load(var0 + 32)
    var11 = (1 if i32_load(var0 + 32) == 0 else 0)
    var12 = (1 if i32_load8_u(var0 + 45) != 0 else 0)
    while True:  # loop $label24
        var5 = i32_load((var8 + (var2 << 2)))
        var16 = (var9 + (i32_load((var8 + (var2 << 2))) * 132))
        if (1 if (1 if i32_load8_u((var9 + (i32_load((var8 + (var2 << 2))) * 132)) + 125) == 3 else 0) != var12 else 0):
            var3 = i32_load(9140300)
            if (1 if i32_load(9684388) >= 2 else 0):
                var1 = 0
                if (1 if var3 == 0 else 0):
                    break
                while True:  # loop $label22
                    if (1 if i32_load(((var1 << 2) + 8451904)) == var5 else 0):
                        break
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != var3 else 0):
                        continue
                    break  # end loop
            var1 = var3
            if (1 if var3 > 39999 else 0):
                break
            i32_store(9140300, (var1 + 1))
            i32_store(((var1 << 2) + 8451904), var5)
            i32_store((var7 + (i32_load16_u(var16 + 110) << 2)), 1)
            var6 = (var6 | var11)
            var1 = i32_load(var0 + 88)
            break
        if (1 if var4 == 0 else 0):
            break
        break
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var1 else 0):
            continue
        break  # end loop
    var10 = ((1 if var4 != 0 else 0) | var6)
    break
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var7 = i32_load(9561692)
    var2 = i32_load(9142420)
    var6 = i32_load(var0 + 48)
    var5 = i32_load8_u(var0 + 45)
    var1 = 1
    while True:  # loop $label29
        var3 = i32_load((var6 + (var4 << 2)))
        var0 = (var1 << 2)
        if (1 if i32_load((var6 + (var1 << 2))) == 0 else 0):
            if (1 if var3 == 0 else 0):
                break
            if i32_load((var0 + var2)):
                break
            break
        if (1 if var3 == 0 else 0):
            break
        i32_store((var0 + var2), 0)
        var3 = (var7 + (var1 * 286704))
        var4 = (i32_load((var7 + (var1 * 286704)) + 283976) + 1)
        if (1 if (i32_load((var7 + (var1 * 286704)) + 283976) + 1) > (i32_load((var3 + 284136)) + i32_load(var3 + 283980)) else 0):
            if (1 if var5 == 0 else 0):
                break
            break
        if (1 if (1 if var5 != 0 else 0) == (1 if var4 > i32_load((var3 + 284000)) else 0) else 0):
            break
        var10 = 1
        i32_store((var0 + var2), 1)
        var1 = (var1 + 1)
        var4 = i32_load(9142892)
        if (1 if (var1 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    break
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var2 = i32_load(9561692)
    var3 = i32_load(9142420)
    var7 = i32_load(var0 + 48)
    var9 = i32_load8_u(var0 + 45)
    var1 = 1
    while True:  # loop $label39
        var4 = i32_load((var7 + (var4 << 2)))
        var6 = (var1 << 2)
        if (1 if i32_load((var7 + (var1 << 2))) == 0 else 0):
            if (1 if var4 == 0 else 0):
                break
            if i32_load((var3 + var6)):
                break
            break
        if (1 if var4 == 0 else 0):
            break
        i32_store((var3 + var6), 0)
        var4 = i32_load(var0 + 32)
        var5 = i32_load(var0 + 28)
        # br_table ['$label33', '$label34', '$label35', '$label36']
        _br_idx = i32_load(var0 + 16)
        break  # br_table
        if (1 if var9 == 0 else 0):
            break
        break
        break
        break
        if (1 if (1 if i32_load((((var2 + (var1 * 286704)) + (var5 << 2)) + 283984)) == var4 else 0) == (1 if var9 != 0 else 0) else 0):
            break
        var10 = 1
        i32_store((var3 + var6), 1)
        var1 = (var1 + 1)
        var4 = i32_load(9142892)
        if (1 if (var1 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    break
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var7 = i32_load(var0 + 80)
    var10 = i32_load(9561692)
    var3 = i32_load(9142420)
    var4 = i32_load(var0 + 48)
    var1 = 1
    if (1 if i32_load(var0 + 32) == 0 else 0):
        while True:  # loop $label46
            var2 = i32_load((var4 + (var2 << 2)))
            var5 = (var1 << 2)
            if (1 if i32_load((var4 + (var1 << 2))) == 0 else 0):
                if (1 if var2 == 0 else 0):
                    break
                if i32_load((var3 + var5)):
                    break
                break
            if (1 if var2 == 0 else 0):
                break
            i32_store((var3 + var5), 0)
            var9 = i32_load(var0 + 88)
            if (1 if i32_load(var0 + 88) == 0 else 0):
                break
            var2 = 0
            var5 = (i32_load(9142420) + var5)
            var8 = i32_load8_u(var0 + 45)
            while True:  # loop $label45
                var11 = (var2 << 2)
                if (1 if i32_load((var7 + (var2 << 2))) == 0 else 0):
                    break
                if (1 if (1 if i32_load((((var10 + (var1 * 286704)) + var11) + 281808)) != 0 else 0) == (1 if var8 != 0 else 0) else 0):
                    break
                var6 = 1
                i32_store(var5, 1)
                break
                var2 = (var2 + 1)
                if (1 if (var2 + 1) < var9 else 0):
                    continue
                break  # end loop
            var1 = (var1 + 1)
            var2 = i32_load(9142892)
            if (1 if (var1 + 1) < i32_load(9142892) else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    while True:  # loop $label52
        var2 = i32_load((var4 + (var2 << 2)))
        var5 = (var1 << 2)
        if (1 if i32_load((var4 + (var1 << 2))) == 0 else 0):
            if (1 if var2 == 0 else 0):
                break
            if i32_load((var3 + var5)):
                break
            break
        if (1 if var2 == 0 else 0):
            break
        i32_store((var3 + var5), 0)
        var9 = i32_load(var0 + 88)
        if (1 if i32_load(var0 + 88) == 0 else 0):
            break
        var2 = 0
        var8 = (i32_load(9142420) + var5)
        var11 = i32_load8_u(var0 + 45)
        while True:  # loop $label51
            var12 = (var2 << 2)
            if i32_load((var7 + (var2 << 2))):
                if (1 if (1 if i32_load((((var10 + (var1 * 286704)) + var12) + 281808)) != 0 else 0) == (1 if var11 != 0 else 0) else 0):
                    break
                i32_store(var8, 1)
                var9 = i32_load(var0 + 88)
                var6 = 1
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < var9 else 0):
                continue
            break
            break  # end loop
        var6 = 0
        i32_store((var3 + var5), 0)
        var1 = (var1 + 1)
        var2 = i32_load(9142892)
        if (1 if (var1 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    var10 = var6
    break
    var10 = func165(var0, 70)
    break
    var2 = i32_load(var0 + 4)
    if (1 if i32_load(var0 + 4) <= 2 else 0):
        # br_table ['$label53', '$label54', '$label55']
        _br_idx = var2
        break  # br_table
        var1 = i32_load(var0 + 88)
        if (1 if i32_load(var0 + 88) == 0 else 0):
            break
        var12 = i32_load(9142420)
        var16 = i32_load(9671128)
        var14 = i32_load(var0 + 80)
        var5 = i32_load(var0 + 32)
        var13 = (1 if i32_load(var0 + 32) == 0 else 0)
        var9 = i32_load8_u(var0 + 45)
        var2 = 0
        while True:  # loop $label67
            var8 = i32_load((var14 + (var2 << 2)))
            var11 = (var16 + (i32_load((var14 + (var2 << 2))) * 132))
            if (1 if i32_load8_u((var16 + (i32_load((var14 + (var2 << 2))) * 132)) + 125) == 3 else 0):
                if var9:
                    break
                break
            var3 = i32_load(var11 + 24)
            if i32_load(var11 + 24):
                var3 = i32_load(var3 + 12)
                if (1 if i32_load(var3 + 12) == 0 else 0):
                    var7 = 0
                    var3 = i32_load(var0 + 8)
                    var4 = (i32_load(var0 + 8) if (1 if var3 < 16777216 else 0) else 0)
                    break
                var3 = i32_load(var3)
                var7 = i32_load((i32_load(var3) + (i32_load(var0 + 36) << 2)))
                var4 = i32_load(var0 + 8)
                if (1 if i32_load(var0 + 8) < 16777216 else 0):
                    break
                var4 = i32_load((((var4 << 2) + var3) - 67108864))
                break
            var7 = 0
            var3 = i32_load(var0 + 8)
            var4 = (i32_load(var0 + 8) if (1 if var3 <= 16777215 else 0) else 0)
            # br_table ['$label59', '$label60', '$label61']
            _br_idx = i32_load(var0 + 28)
            break  # br_table
            break
            break
            if (1 if (1 if var4 == var7 else 0) == (1 if var9 != 0 else 0) else 0):
                break
            var3 = i32_load(9140300)
            if (1 if i32_load(9684388) >= 2 else 0):
                var1 = 0
                if (1 if var3 == 0 else 0):
                    break
                while True:  # loop $label65
                    if (1 if i32_load(((var1 << 2) + 8451904)) == var8 else 0):
                        break
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != var3 else 0):
                        continue
                    break  # end loop
            var1 = var3
            if (1 if var3 > 39999 else 0):
                break
            i32_store(9140300, (var1 + 1))
            i32_store(((var1 << 2) + 8451904), var8)
            i32_store((var12 + (i32_load16_u(var11 + 110) << 2)), 1)
            var6 = (var6 | var13)
            var1 = i32_load(var0 + 88)
            break
            if (1 if var5 == 0 else 0):
                break
            break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < var1 else 0):
                continue
            break  # end loop
        var10 = ((1 if var5 != 0 else 0) | var6)
        break
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) >= 2 else 0):
        var10 = i32_load(9561692)
        var6 = i32_load(9142420)
        var7 = i32_load(var0 + 48)
        var9 = (1 if i32_load8_u(var0 + 45) != 0 else 0)
        var1 = 1
        while True:  # loop $label76
            var2 = i32_load((var7 + (var2 << 2)))
            var4 = (var1 << 2)
            if (1 if i32_load((var7 + (var1 << 2))) == 0 else 0):
                if (1 if var2 == 0 else 0):
                    break
                if i32_load((var4 + var6)):
                    break
                break
            if (1 if var2 == 0 else 0):
                break
            i32_store((var4 + var6), 0)
            var2 = i32_load((var10 + (var1 * 286704)) + 286680)
            if (1 if i32_load((var10 + (var1 * 286704)) + 286680) == 0 else 0):
                var3 = 0
                var2 = i32_load(var0 + 8)
                var2 = (i32_load(var0 + 8) if (1 if var2 <= 16777215 else 0) else 0)
                break
            var8 = i32_load(var2)
            var3 = i32_load((i32_load(var2) + (i32_load(var0 + 36) << 2)))
            var2 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) < 16777216 else 0):
                break
            var2 = i32_load((((var2 << 2) + var8) - 67108864))
            # br_table ['$label72', '$label73', '$label74']
            _br_idx = i32_load(var0 + 28)
            break  # br_table
            break
            break
            if (1 if (1 if var2 == var3 else 0) == var9 else 0):
                break
            var5 = 1
            i32_store((var4 + var6), 1)
            var1 = (var1 + 1)
            var2 = i32_load(9142892)
            if (1 if (var1 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    var10 = var5
    break
    var7 = i32_load(9140300)
    var5 = i32_load(var0 + 32)
    i32_store(9140300, 0)
    if i32_load(9142892):
        var2 = i32_load(9142420)
        while True:  # loop $label77
            i32_store((var2 + (var1 << 2)), 0)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    if var7:
        var8 = (1 if var5 == 0 else 0)
        var11 = i32_load(9142420)
        var12 = i32_load(9671128)
        var16 = (1 if i32_load8_u(var0 + 45) != 0 else 0)
        var2 = 0
        while True:  # loop $label87
            var9 = i32_load(((var2 << 2) + 8451904))
            var14 = (var12 + (i32_load(((var2 << 2) + 8451904)) * 132))
            var1 = i32_load((var12 + (i32_load(((var2 << 2) + 8451904)) * 132)) + 24)
            if i32_load((var12 + (i32_load(((var2 << 2) + 8451904)) * 132)) + 24):
                var1 = i32_load(var1 + 12)
                if (1 if i32_load(var1 + 12) == 0 else 0):
                    var4 = 0
                    var1 = i32_load(var0 + 8)
                    var1 = (i32_load(var0 + 8) if (1 if var1 < 16777216 else 0) else 0)
                    break
                var3 = i32_load(var1)
                var4 = i32_load((i32_load(var1) + (i32_load(var0 + 36) << 2)))
                var1 = i32_load(var0 + 8)
                if (1 if i32_load(var0 + 8) < 16777216 else 0):
                    break
                var1 = i32_load((((var1 << 2) + var3) - 67108864))
                break
            var4 = 0
            var1 = i32_load(var0 + 8)
            var1 = (i32_load(var0 + 8) if (1 if var1 <= 16777215 else 0) else 0)
            # br_table ['$label79', '$label80', '$label81']
            _br_idx = i32_load(var0 + 28)
            break  # br_table
            break
            break
            if (1 if (1 if var1 == var4 else 0) != var16 else 0):
                var3 = i32_load(9140300)
                if (1 if i32_load(9684388) >= 2 else 0):
                    var1 = 0
                    if (1 if var3 == 0 else 0):
                        break
                    while True:  # loop $label85
                        if (1 if i32_load(((var1 << 2) + 8451904)) == var9 else 0):
                            break
                        var1 = (var1 + 1)
                        if (1 if (var1 + 1) != var3 else 0):
                            continue
                        break  # end loop
                var1 = var3
                if (1 if var3 > 39999 else 0):
                    break
                i32_store(9140300, (var1 + 1))
                i32_store(((var1 << 2) + 8451904), var9)
                i32_store((var11 + (i32_load16_u(var14 + 110) << 2)), 1)
                var6 = (var6 | var8)
                break
            if (1 if var5 == 0 else 0):
                break
            break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var7 else 0):
                continue
            break  # end loop
    var10 = ((1 if var5 != 0 else 0) | var6)
    break
    var1 = i32_load(9142892)
    if (1 if i32_load(9142892) == 0 else 0):
        break
    var12 = i32_load(9561692)
    var8 = i32_load(9142420)
    var16 = i32_load(var0 + 48)
    var2 = i32_load(var0 + 32)
    var17 = (1 if i32_load(var0 + 32) > 3 else 0)
    var18 = (var2 - 1)
    var22 = ((var2 - 4) << 2)
    while True:  # loop $label122
        var2 = i32_load((var16 + (var1 << 2)))
        var11 = (var9 << 2)
        if (1 if i32_load((var16 + (var9 << 2))) == 0 else 0):
            if (1 if var2 == 0 else 0):
                break
            if i32_load((var8 + var11)):
                break
            break
        if (1 if var2 == 0 else 0):
            break
        i32_store((var8 + var11), 0)
        var6 = i32_load(9140300)
        if (1 if var17 == 0 else 0):
            var5 = 0
            var19 = i32_load(9684388)
            var14 = i32_load(9671128)
            var20 = i32_load(38764)
            var21 = i32_load(38456)
            var3 = 0
            var2 = var6
            while True:  # loop $label106
                # br_table ['$label91', '$label92', '$label93', '$label94']
                _br_idx = var18
                break  # br_table
                var1 = ((var3 * 404) + 9568096)
                if i32_load(((var3 * 404) + 9568096) + 264):
                    break
                if (1 if i32_load(var1 + 268) == 1 else 0):
                    break
                if (1 if i32_load(var1 + 92) == 0 else 0):
                    break
                if (1 if var3 == var21 else 0):
                    break
                if (1 if var3 != var20 else 0):
                    break
                break
                if (1 if i32_load(((var3 * 404) + 9568096) + 264) == 1 else 0):
                    break
                break
                if i32_load(((var3 * 404) + 9568096) + 264):
                    break
                var1 = i32_load((((var12 + (var9 * 286704)) + (var3 << 2)) + 284636))
                if (1 if i32_load((((var12 + (var9 * 286704)) + (var3 << 2)) + 284636)) == 0 else 0):
                    break
                var23 = i32_load(var1 + 8)
                if (1 if i32_load(var1 + 8) == 0 else 0):
                    break
                var13 = i32_load8_u(var0 + 45)
                var24 = i32_load(var1)
                var4 = 0
                while True:  # loop $label105
                    var1 = i32_load((var24 + (var4 << 2)))
                    if (1 if i32_load((var24 + (var4 << 2))) == 0 else 0):
                        break
                    var15 = i32_load((var14 + (var1 * 132)) + 28)
                    var1 = (var14 + (i32_load((var14 + (var1 * 132)) + 28) * 132))
                    if (1 if i32_load8_u((var14 + (i32_load((var14 + (var1 * 132)) + 28) * 132)) + 125) == 3 else 0):
                        if var13:
                            break
                        break
                    var1 = i32_load(var1 + 24)
                    if i32_load(var1 + 24):
                        var1 = i32_load(var1 + 12)
                        if (1 if i32_load(var1 + 12) == 0 else 0):
                            var7 = 0
                            var1 = i32_load(var0 + 8)
                            var1 = (i32_load(var0 + 8) if (1 if var1 < 16777216 else 0) else 0)
                            break
                        var25 = i32_load(var1)
                        var7 = i32_load((i32_load(var1) + (i32_load(var0 + 36) << 2)))
                        var1 = i32_load(var0 + 8)
                        if (1 if i32_load(var0 + 8) < 16777216 else 0):
                            break
                        var1 = i32_load((((var1 << 2) + var25) - 67108864))
                        break
                    var7 = 0
                    var1 = i32_load(var0 + 8)
                    var1 = (i32_load(var0 + 8) if (1 if var1 <= 16777215 else 0) else 0)
                    # br_table ['$label99', '$label100', '$label101']
                    _br_idx = i32_load(var0 + 28)
                    break  # br_table
                    break
                    break
                    if (1 if (1 if var1 == var7 else 0) == (1 if var13 != 0 else 0) else 0):
                        break
                    var5 = (var5 + 1)
                    if (1 if var19 >= 2 else 0):
                        var1 = 0
                        if (1 if var2 == 0 else 0):
                            break
                        while True:  # loop $label104
                            if (1 if i32_load(((var1 << 2) + 8451904)) == var15 else 0):
                                break
                            var1 = (var1 + 1)
                            if (1 if (var1 + 1) != var2 else 0):
                                continue
                            break  # end loop
                    var1 = var2
                    if (1 if var2 > 39999 else 0):
                        break
                    var2 = (var1 + 1)
                    i32_store(9140300, (var1 + 1))
                    i32_store(((var1 << 2) + 8451904), var15)
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != var23 else 0):
                        continue
                    break  # end loop
                var3 = (var3 + 1)
                if (1 if (var3 + 1) != 255 else 0):
                    continue
                break  # end loop
            break
        var2 = i32_load((((var12 + (var9 * 286704)) + var22) + 284636))
        if (1 if i32_load((((var12 + (var9 * 286704)) + var22) + 284636)) == 0 else 0):
            break
        var15 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        var4 = 0
        var19 = i32_load(9684388)
        var3 = i32_load8_u(var0 + 45)
        var14 = i32_load(9671128)
        var20 = i32_load(var2)
        var5 = 0
        var2 = var6
        while True:  # loop $label118
            var1 = i32_load((var20 + (var4 << 2)))
            if (1 if i32_load((var20 + (var4 << 2))) == 0 else 0):
                break
            var13 = i32_load((var14 + (var1 * 132)) + 28)
            var1 = (var14 + (i32_load((var14 + (var1 * 132)) + 28) * 132))
            if (1 if i32_load8_u((var14 + (i32_load((var14 + (var1 * 132)) + 28) * 132)) + 125) == 3 else 0):
                if var3:
                    break
                break
            var1 = i32_load(var1 + 24)
            if i32_load(var1 + 24):
                var1 = i32_load(var1 + 12)
                if (1 if i32_load(var1 + 12) == 0 else 0):
                    var7 = 0
                    var1 = i32_load(var0 + 8)
                    var1 = (i32_load(var0 + 8) if (1 if var1 < 16777216 else 0) else 0)
                    break
                var21 = i32_load(var1)
                var7 = i32_load((i32_load(var1) + (i32_load(var0 + 36) << 2)))
                var1 = i32_load(var0 + 8)
                if (1 if i32_load(var0 + 8) < 16777216 else 0):
                    break
                var1 = i32_load((((var1 << 2) + var21) - 67108864))
                break
            var7 = 0
            var1 = i32_load(var0 + 8)
            var1 = (i32_load(var0 + 8) if (1 if var1 <= 16777215 else 0) else 0)
            # br_table ['$label112', '$label113', '$label114']
            _br_idx = i32_load(var0 + 28)
            break  # br_table
            break
            break
            if (1 if (1 if var1 == var7 else 0) == (1 if var3 != 0 else 0) else 0):
                break
            var5 = (var5 + 1)
            if (1 if var19 >= 2 else 0):
                var1 = 0
                if (1 if var2 == 0 else 0):
                    break
                while True:  # loop $label117
                    if (1 if i32_load(((var1 << 2) + 8451904)) == var13 else 0):
                        break
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != var2 else 0):
                        continue
                    break  # end loop
            var1 = var2
            if (1 if var2 > 39999 else 0):
                break
            var2 = (var1 + 1)
            i32_store(9140300, (var1 + 1))
            i32_store(((var1 << 2) + 8451904), var13)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var15 else 0):
                continue
            break  # end loop
        var1 = i32_load(var0 + 12)
        var4 = i32_load(var0 + 16)
        if i32_load(var0 + 16):
            break
        if (1 if var1 < var5 else 0):
            break
        break
        var1 = i32_load(var0 + 12)
        var4 = i32_load(var0 + 16)
        var5 = 0
        if (1 if var4 == 0 else 0):
            break
        if (1 if var1 <= var5 else 0):
            break
        var10 = 1
        i32_store((var8 + var11), 1)
        var1 = i32_load(var0 + 12)
        var4 = i32_load(var0 + 16)
        if (1 if var4 == 0 else 0):
            break
        if (1 if var1 > var5 else 0):
            break
        i32_store(9140300, var6)
        var9 = (var9 + 1)
        var1 = i32_load(9142892)
        if (1 if (var9 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    break
    # br_table ['$label123', '$label124', '$label125']
    _br_idx = i32_load(var0 + 4)
    break  # br_table
    var2 = 3
    if (1 if i32_load(9671136) > 3 else 0):
        while True:  # loop $label126
            if func233(var2, var0):
                i32_store(9684384, (i32_load(9684384) + 1))
                var1 = 1
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < i32_load(9671136) else 0):
                continue
            break  # end loop
    break
    if i32_load(var0 + 88):
        break
    break
    if i32_load(9140300):
        break
    break
    while True:  # loop $label130
        if func233(i32_load((i32_load(var0 + 80) + (var2 << 2))), var0):
            i32_store(9684384, (i32_load(9684384) + 1))
            var1 = 1
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < i32_load(var0 + 88) else 0):
            continue
        break  # end loop
    break
    while True:  # loop $label131
        if func233(i32_load(((var2 << 2) + 8451904)), var0):
            i32_store(9684384, (i32_load(9684384) + 1))
            var1 = 1
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < i32_load(9140300) else 0):
            continue
        break  # end loop
    if i32_load(9142892):
        var2 = i32_load(9142420)
        var0 = 0
        while True:  # loop $label132
            var3 = (var2 + (var0 << 2))
            i32_store((var2 + (var0 << 2)), (1 if i32_load(var3) == 2 else 0))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    var10 = var1
    break
    if (1 if i32_load8_u(9147210) == 0 else 0):
        break
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) >= 2 else 0):
        var7 = i32_load(9561692)
        var2 = i32_load(9142420)
        var3 = i32_load(var0 + 48)
        var10 = (1 if i32_load8_u(var0 + 45) == 0 else 0)
        var1 = 1
        while True:  # loop $label136
            var6 = i32_load((var3 + (var4 << 2)))
            var0 = (var1 << 2)
            if (1 if i32_load((var3 + (var1 << 2))) == 0 else 0):
                if (1 if var6 == 0 else 0):
                    break
                if i32_load((var0 + var2)):
                    break
                break
            if (1 if var6 == 0 else 0):
                break
            i32_store((var0 + var2), 0)
            var6 = (var7 + (var1 * 286704))
            if (1 if var10 == (1 if (i32_load((var7 + (var1 * 286704)) + 284616) | i32_load(var6 + 284628)) != 0 else 0) else 0):
                break
            var5 = 1
            i32_store((var0 + var2), 1)
            var1 = (var1 + 1)
            var4 = i32_load(9142892)
            if (1 if (var1 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    var10 = (var5 & 1)
    break
    var2 = (i32_load(9142848) * 25)
    var1 = i32_load(var0 + 12)
    var10 = ((1 if i32_load8_u(var0 + 45) != 0 else 0) ^ ((1 if (i32_load(9142848) * 25) < i32_load(var0 + 12) else 0) if i32_load(var0 + 16) else (1 if var1 < var2 else 0)))
    break
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var5 = i32_load(9561692)
    var2 = i32_load(9142420)
    var3 = i32_load(var0 + 48)
    var7 = i32_load8_u(var0 + 45)
    var1 = 1
    while True:  # loop $label140
        var6 = i32_load((var3 + (var4 << 2)))
        var0 = (var1 << 2)
        if (1 if i32_load((var3 + (var1 << 2))) == 0 else 0):
            if (1 if var6 == 0 else 0):
                break
            if i32_load((var0 + var2)):
                break
            break
        if (1 if var6 == 0 else 0):
            break
        i32_store((var0 + var2), 0)
        var6 = i32_load8_u((var5 + (var1 * 286704)) + 286696)
        if (1 if ((1 if i32_load8_u((var5 + (var1 * 286704)) + 286696) == 0 else 0) if var7 else (1 if var6 != 0 else 0)) != 1 else 0):
            break
        var10 = 1
        i32_store((var0 + var2), 1)
        var1 = (var1 + 1)
        var4 = i32_load(9142892)
        if (1 if (var1 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    break
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var5 = i32_load(9561692)
    var2 = i32_load(9142420)
    var3 = i32_load(var0 + 48)
    var7 = i32_load8_u(var0 + 45)
    var1 = 1
    while True:  # loop $label144
        var6 = i32_load((var3 + (var4 << 2)))
        var0 = (var1 << 2)
        if (1 if i32_load((var3 + (var1 << 2))) == 0 else 0):
            if (1 if var6 == 0 else 0):
                break
            if i32_load((var0 + var2)):
                break
            break
        if (1 if var6 == 0 else 0):
            break
        i32_store((var0 + var2), 0)
        var6 = i32_load8_u((var5 + (var1 * 286704)) + 286697)
        if (1 if ((1 if i32_load8_u((var5 + (var1 * 286704)) + 286697) == 0 else 0) if var7 else (1 if var6 != 0 else 0)) != 1 else 0):
            break
        var10 = 1
        i32_store((var0 + var2), 1)
        var1 = (var1 + 1)
        var4 = i32_load(9142892)
        if (1 if (var1 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    break
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) >= 2 else 0):
        var3 = i32_load(var0 + 80)
        var6 = i32_load(9561692)
        var4 = i32_load(9142420)
        var10 = i32_load(var0 + 48)
        var9 = i32_load8_u(var0 + 45)
        var1 = 1
        while True:  # loop $label154
            var2 = i32_load((var10 + (var2 << 2)))
            var5 = (var1 << 2)
            if (1 if i32_load((var10 + (var1 << 2))) == 0 else 0):
                if (1 if var2 == 0 else 0):
                    break
                if i32_load((var4 + var5)):
                    break
                break
            if (1 if var2 == 0 else 0):
                break
            i32_store((var4 + var5), 0)
            # br_table ['$label148', '$label149', '$label150', '$label151']
            _br_idx = i32_load(var0 + 16)
            break  # br_table
            if (1 if var9 == 0 else 0):
                break
            break
            var2 = 1
            var8 = i32_load(var3)
            if (1 if i32_load(var3) != -2147483647 else 0):
                var2 = (1 if i32_load((var6 + (var1 * 286704)) + 283848) >= var8 else 0)
            var8 = i32_load(var3 + 4)
            if (1 if i32_load(var3 + 4) != -2147483647 else 0):
                var2 = ((1 if i32_load(((var6 + (var1 * 286704)) + 283852)) >= var8 else 0) & var2)
            var8 = i32_load(var3 + 8)
            if (1 if i32_load(var3 + 8) != -2147483647 else 0):
                var2 = ((1 if i32_load(((var6 + (var1 * 286704)) + 283856)) >= var8 else 0) & var2)
            var8 = i32_load(var3 + 12)
            if (1 if i32_load(var3 + 12) == -2147483647 else 0):
                break
            var2 = ((1 if i32_load(((var6 + (var1 * 286704)) + 283860)) >= var8 else 0) & var2)
            break
            var2 = 1
            var8 = i32_load(var3)
            if (1 if i32_load(var3) != -2147483647 else 0):
                var2 = (1 if i32_load((var6 + (var1 * 286704)) + 283848) <= var8 else 0)
            var8 = i32_load(var3 + 4)
            if (1 if i32_load(var3 + 4) != -2147483647 else 0):
                var2 = ((1 if i32_load(((var6 + (var1 * 286704)) + 283852)) <= var8 else 0) & var2)
            var8 = i32_load(var3 + 8)
            if (1 if i32_load(var3 + 8) != -2147483647 else 0):
                var2 = ((1 if i32_load(((var6 + (var1 * 286704)) + 283856)) <= var8 else 0) & var2)
            var8 = i32_load(var3 + 12)
            if (1 if i32_load(var3 + 12) == -2147483647 else 0):
                break
            var2 = ((1 if i32_load(((var6 + (var1 * 286704)) + 283860)) <= var8 else 0) & var2)
            break
            var2 = 1
            var8 = i32_load(var3)
            if (1 if i32_load(var3) != -2147483647 else 0):
                var2 = (1 if i32_load((var6 + (var1 * 286704)) + 283848) == var8 else 0)
            var8 = i32_load(var3 + 4)
            if (1 if i32_load(var3 + 4) != -2147483647 else 0):
                var2 = ((1 if i32_load(((var6 + (var1 * 286704)) + 283852)) == var8 else 0) & var2)
            var8 = i32_load(var3 + 8)
            if (1 if i32_load(var3 + 8) != -2147483647 else 0):
                var2 = ((1 if i32_load(((var6 + (var1 * 286704)) + 283856)) == var8 else 0) & var2)
            var8 = i32_load(var3 + 12)
            if (1 if i32_load(var3 + 12) == -2147483647 else 0):
                break
            var2 = ((1 if i32_load(((var6 + (var1 * 286704)) + 283860)) == var8 else 0) & var2)
            if (1 if var2 == (1 if var9 != 0 else 0) else 0):
                break
            var7 = 1
            i32_store((var4 + var5), 1)
            var1 = (var1 + 1)
            var2 = i32_load(9142892)
            if (1 if (var1 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    var10 = var7
    break
    # br_table ['$label155', '$label156', '$label157']
    _br_idx = i32_load(var0 + 4)
    break  # br_table
    var4 = i32_load(var0 + 88)
    if (1 if i32_load(var0 + 88) == 0 else 0):
        break
    var9 = i32_load(9142420)
    var8 = i32_load(9671128)
    var11 = i32_load(var0 + 80)
    var5 = i32_load(var0 + 32)
    var12 = (1 if i32_load(var0 + 32) == 0 else 0)
    var16 = (1 if i32_load8_u(var0 + 45) != 0 else 0)
    while True:  # loop $label162
        var7 = i32_load((var11 + (var2 << 2)))
        var14 = (var8 + (i32_load((var11 + (var2 << 2))) * 132))
        var1 = i32_load8_u((var8 + (i32_load((var11 + (var2 << 2))) * 132)) + 125)
        if (1 if ((1 if i32_load8_u((var8 + (i32_load((var11 + (var2 << 2))) * 132)) + 125) != 3 else 0) & (1 if var1 != 14 else 0)) != var16 else 0):
            var3 = i32_load(9140300)
            if (1 if i32_load(9684388) >= 2 else 0):
                var1 = 0
                if (1 if var3 == 0 else 0):
                    break
                while True:  # loop $label160
                    if (1 if i32_load(((var1 << 2) + 8451904)) == var7 else 0):
                        break
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != var3 else 0):
                        continue
                    break  # end loop
            var1 = var3
            if (1 if var3 > 39999 else 0):
                break
            i32_store(9140300, (var1 + 1))
            i32_store(((var1 << 2) + 8451904), var7)
            i32_store((var9 + (i32_load16_u(var14 + 110) << 2)), 1)
            var6 = (var6 | var12)
            var4 = i32_load(var0 + 88)
            break
        if (1 if var5 == 0 else 0):
            break
        break
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var4 else 0):
            continue
        break  # end loop
    var10 = ((1 if var5 != 0 else 0) | var6)
    break
    var4 = i32_load(9140300)
    var3 = i32_load(var0 + 32)
    i32_store(9140300, 0)
    if i32_load(9142892):
        var2 = i32_load(9142420)
        while True:  # loop $label163
            i32_store((var2 + (var1 << 2)), 0)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    if var4:
        var7 = (1 if var3 == 0 else 0)
        var9 = i32_load(9142420)
        var8 = i32_load(9671128)
        var11 = (1 if i32_load8_u(var0 + 45) != 0 else 0)
        var2 = 0
        while True:  # loop $label168
            var5 = i32_load(((var2 << 2) + 8451904))
            var12 = (var8 + (i32_load(((var2 << 2) + 8451904)) * 132))
            var0 = i32_load8_u((var8 + (i32_load(((var2 << 2) + 8451904)) * 132)) + 125)
            if (1 if ((1 if i32_load8_u((var8 + (i32_load(((var2 << 2) + 8451904)) * 132)) + 125) != 3 else 0) & (1 if var0 != 14 else 0)) != var11 else 0):
                var0 = i32_load(9140300)
                if (1 if i32_load(9684388) >= 2 else 0):
                    var1 = 0
                    if (1 if var0 == 0 else 0):
                        break
                    while True:  # loop $label166
                        if (1 if i32_load(((var1 << 2) + 8451904)) == var5 else 0):
                            break
                        var1 = (var1 + 1)
                        if (1 if (var1 + 1) != var0 else 0):
                            continue
                        break  # end loop
                var1 = var0
                if (1 if var0 > 39999 else 0):
                    break
                i32_store(9140300, (var1 + 1))
                i32_store(((var1 << 2) + 8451904), var5)
                i32_store((var9 + (i32_load16_u(var12 + 110) << 2)), 1)
                var6 = (var6 | var7)
                break
            if (1 if var3 == 0 else 0):
                break
            break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var4 else 0):
                continue
            break  # end loop
    var10 = ((1 if var3 != 0 else 0) | var6)
    break
    var1 = i32_load(9142892)
    if (1 if i32_load(9142892) == 0 else 0):
        break
    var16 = i32_load(9561692)
    var11 = i32_load(9142420)
    var14 = i32_load(var0 + 48)
    var2 = i32_load(var0 + 32)
    var22 = (1 if i32_load(var0 + 32) > 3 else 0)
    var19 = (var2 - 1)
    var20 = ((var2 - 4) << 2)
    while True:  # loop $label192
        var2 = i32_load((var14 + (var1 << 2)))
        var12 = (var9 << 2)
        if (1 if i32_load((var14 + (var9 << 2))) == 0 else 0):
            if (1 if var2 == 0 else 0):
                break
            if i32_load((var11 + var12)):
                break
            break
        if (1 if var2 == 0 else 0):
            break
        i32_store((var11 + var12), 0)
        var6 = i32_load(9140300)
        if (1 if var22 == 0 else 0):
            var5 = 0
            var8 = i32_load(9671128)
            var21 = i32_load(38764)
            var23 = i32_load(38456)
            var24 = i32_load(9684388)
            var7 = 0
            var3 = var6
            while True:  # loop $label182
                # br_table ['$label172', '$label173', '$label174', '$label175']
                _br_idx = var19
                break  # br_table
                var2 = ((var7 * 404) + 9568096)
                if i32_load(((var7 * 404) + 9568096) + 264):
                    break
                if (1 if i32_load(var2 + 268) == 1 else 0):
                    break
                if (1 if i32_load(var2 + 92) == 0 else 0):
                    break
                if (1 if var7 == var23 else 0):
                    break
                if (1 if var7 != var21 else 0):
                    break
                break
                if (1 if i32_load(((var7 * 404) + 9568096) + 264) == 1 else 0):
                    break
                break
                if i32_load(((var7 * 404) + 9568096) + 264):
                    break
                var2 = i32_load((((var16 + (var9 * 286704)) + (var7 << 2)) + 284636))
                if (1 if i32_load((((var16 + (var9 * 286704)) + (var7 << 2)) + 284636)) == 0 else 0):
                    break
                var13 = i32_load(var2 + 8)
                if (1 if i32_load(var2 + 8) == 0 else 0):
                    break
                var15 = i32_load8_u(var0 + 45)
                var17 = i32_load(var2)
                var4 = 0
                var2 = var3
                if (1 if var24 >= 2 else 0):
                    while True:  # loop $label179
                        var1 = i32_load((var17 + (var4 << 2)))
                        if (1 if i32_load((var17 + (var4 << 2))) == 0 else 0):
                            break
                        var18 = i32_load((var8 + (var1 * 132)) + 28)
                        var1 = i32_load8_u((var8 + (i32_load((var8 + (var1 * 132)) + 28) * 132)) + 125)
                        if (1 if ((1 if i32_load8_u((var8 + (i32_load((var8 + (var1 * 132)) + 28) * 132)) + 125) != 3 else 0) & (1 if var1 != 14 else 0)) == (1 if var15 != 0 else 0) else 0):
                            break
                        var5 = (var5 + 1)
                        var1 = 0
                        if var2:
                            while True:  # loop $label178
                                if (1 if i32_load(((var1 << 2) + 8451904)) == var18 else 0):
                                    break
                                var1 = (var1 + 1)
                                if (1 if (var1 + 1) != var2 else 0):
                                    continue
                                break  # end loop
                            if (1 if var2 >= 40000 else 0):
                                break
                        var3 = (var2 + 1)
                        i32_store(9140300, (var2 + 1))
                        i32_store(((var2 << 2) + 8451904), var18)
                        var2 = var3
                        var4 = (var4 + 1)
                        if (1 if (var4 + 1) != var13 else 0):
                            continue
                        break
                        break  # end loop
                    raise RuntimeError('unreachable')
                while True:  # loop $label181
                    var1 = i32_load((var17 + (var4 << 2)))
                    if (1 if i32_load((var17 + (var4 << 2))) == 0 else 0):
                        break
                    var1 = i32_load((var8 + (var1 * 132)) + 28)
                    var18 = i32_load8_u((var8 + (i32_load((var8 + (var1 * 132)) + 28) * 132)) + 125)
                    if (1 if ((1 if i32_load8_u((var8 + (i32_load((var8 + (var1 * 132)) + 28) * 132)) + 125) != 3 else 0) & (1 if var18 != 14 else 0)) == (1 if var15 != 0 else 0) else 0):
                        break
                    var5 = (var5 + 1)
                    if (1 if var2 > 39999 else 0):
                        break
                    var3 = (var2 + 1)
                    i32_store(9140300, (var2 + 1))
                    i32_store(((var2 << 2) + 8451904), var1)
                    var2 = var3
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != var13 else 0):
                        continue
                    break  # end loop
                var7 = (var7 + 1)
                if (1 if (var7 + 1) != 255 else 0):
                    continue
                break  # end loop
            break
        var2 = i32_load((((var16 + (var9 * 286704)) + var20) + 284636))
        if (1 if i32_load((((var16 + (var9 * 286704)) + var20) + 284636)) == 0 else 0):
            break
        var8 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        var4 = 0
        var13 = i32_load(9684388)
        var15 = i32_load8_u(var0 + 45)
        var3 = i32_load(9671128)
        var17 = i32_load(var2)
        var5 = 0
        var2 = var6
        while True:  # loop $label188
            var1 = i32_load((var17 + (var4 << 2)))
            if (1 if i32_load((var17 + (var4 << 2))) == 0 else 0):
                break
            var7 = i32_load((var3 + (var1 * 132)) + 28)
            var1 = i32_load8_u((var3 + (i32_load((var3 + (var1 * 132)) + 28) * 132)) + 125)
            if (1 if ((1 if i32_load8_u((var3 + (i32_load((var3 + (var1 * 132)) + 28) * 132)) + 125) != 3 else 0) & (1 if var1 != 14 else 0)) == (1 if var15 != 0 else 0) else 0):
                break
            var5 = (var5 + 1)
            if (1 if var13 >= 2 else 0):
                var1 = 0
                if (1 if var2 == 0 else 0):
                    break
                while True:  # loop $label187
                    if (1 if i32_load(((var1 << 2) + 8451904)) == var7 else 0):
                        break
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != var2 else 0):
                        continue
                    break  # end loop
            var1 = var2
            if (1 if var2 > 39999 else 0):
                break
            var2 = (var1 + 1)
            i32_store(9140300, (var1 + 1))
            i32_store(((var1 << 2) + 8451904), var7)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var8 else 0):
                continue
            break  # end loop
        var1 = i32_load(var0 + 12)
        var4 = i32_load(var0 + 16)
        if i32_load(var0 + 16):
            break
        if (1 if var1 < var5 else 0):
            break
        break
        var1 = i32_load(var0 + 12)
        var4 = i32_load(var0 + 16)
        var5 = 0
        if (1 if var4 == 0 else 0):
            break
        if (1 if var1 <= var5 else 0):
            break
        var10 = 1
        i32_store((var11 + var12), 1)
        var1 = i32_load(var0 + 12)
        var4 = i32_load(var0 + 16)
        if (1 if var4 == 0 else 0):
            break
        if (1 if var1 > var5 else 0):
            break
        i32_store(9140300, var6)
        var9 = (var9 + 1)
        var1 = i32_load(9142892)
        if (1 if (var9 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    break
    var4 = i32_load(9140300)
    var3 = i32_load(var0 + 32)
    i32_store(9140300, 0)
    if i32_load(9142892):
        var2 = i32_load(9142420)
        while True:  # loop $label193
            i32_store((var2 + (var1 << 2)), 0)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    if var4:
        var7 = (1 if var3 == 0 else 0)
        var9 = i32_load(9142420)
        var8 = i32_load(9671128)
        var11 = (1 if i32_load8_u(var0 + 45) != 0 else 0)
        var2 = 0
        while True:  # loop $label198
            var5 = i32_load(((var2 << 2) + 8451904))
            var12 = (var8 + (i32_load(((var2 << 2) + 8451904)) * 132))
            if (1 if (1 if i32_load8_u((var8 + (i32_load(((var2 << 2) + 8451904)) * 132)) + 125) == 3 else 0) != var11 else 0):
                var0 = i32_load(9140300)
                if (1 if i32_load(9684388) >= 2 else 0):
                    var1 = 0
                    if (1 if var0 == 0 else 0):
                        break
                    while True:  # loop $label196
                        if (1 if i32_load(((var1 << 2) + 8451904)) == var5 else 0):
                            break
                        var1 = (var1 + 1)
                        if (1 if (var1 + 1) != var0 else 0):
                            continue
                        break  # end loop
                var1 = var0
                if (1 if var0 > 39999 else 0):
                    break
                i32_store(9140300, (var1 + 1))
                i32_store(((var1 << 2) + 8451904), var5)
                i32_store((var9 + (i32_load16_u(var12 + 110) << 2)), 1)
                var6 = (var6 | var7)
                break
            if (1 if var3 == 0 else 0):
                break
            break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var4 else 0):
                continue
            break  # end loop
    var10 = ((1 if var3 != 0 else 0) | var6)
    break
    var1 = i32_load(9142892)
    if (1 if i32_load(9142892) == 0 else 0):
        break
    var16 = i32_load(9561692)
    var11 = i32_load(9142420)
    var14 = i32_load(var0 + 48)
    var2 = i32_load(var0 + 32)
    var22 = (1 if i32_load(var0 + 32) > 3 else 0)
    var19 = (var2 - 1)
    var20 = ((var2 - 4) << 2)
    while True:  # loop $label223
        var2 = i32_load((var14 + (var1 << 2)))
        var12 = (var9 << 2)
        if (1 if i32_load((var14 + (var9 << 2))) == 0 else 0):
            if (1 if var2 == 0 else 0):
                break
            if i32_load((var11 + var12)):
                break
            break
        if (1 if var2 == 0 else 0):
            break
        i32_store((var11 + var12), 0)
        var6 = i32_load(9140300)
        if (1 if var22 == 0 else 0):
            var5 = 0
            var8 = i32_load(9671128)
            var21 = i32_load(38764)
            var23 = i32_load(38456)
            var24 = i32_load(9684388)
            var7 = 0
            var3 = var6
            while True:  # loop $label212
                # br_table ['$label202', '$label203', '$label204', '$label205']
                _br_idx = var19
                break  # br_table
                var2 = ((var7 * 404) + 9568096)
                if i32_load(((var7 * 404) + 9568096) + 264):
                    break
                if (1 if i32_load(var2 + 268) == 1 else 0):
                    break
                if (1 if i32_load(var2 + 92) == 0 else 0):
                    break
                if (1 if var7 == var23 else 0):
                    break
                if (1 if var7 != var21 else 0):
                    break
                break
                if (1 if i32_load(((var7 * 404) + 9568096) + 264) == 1 else 0):
                    break
                break
                if i32_load(((var7 * 404) + 9568096) + 264):
                    break
                var2 = i32_load((((var16 + (var9 * 286704)) + (var7 << 2)) + 285656))
                if (1 if i32_load((((var16 + (var9 * 286704)) + (var7 << 2)) + 285656)) == 0 else 0):
                    break
                var13 = i32_load(var2 + 8)
                if (1 if i32_load(var2 + 8) == 0 else 0):
                    break
                var15 = i32_load8_u(var0 + 45)
                var17 = i32_load(var2)
                var4 = 0
                var2 = var3
                if (1 if var24 >= 2 else 0):
                    while True:  # loop $label209
                        var1 = i32_load((var17 + (var4 << 2)))
                        if (1 if i32_load((var17 + (var4 << 2))) == 0 else 0):
                            break
                        var18 = i32_load((var8 + (var1 * 132)) + 28)
                        if (1 if (1 if i32_load8_u((var8 + (i32_load((var8 + (var1 * 132)) + 28) * 132)) + 125) == 3 else 0) == (1 if var15 != 0 else 0) else 0):
                            break
                        var5 = (var5 + 1)
                        var1 = 0
                        if var2:
                            while True:  # loop $label208
                                if (1 if i32_load(((var1 << 2) + 8451904)) == var18 else 0):
                                    break
                                var1 = (var1 + 1)
                                if (1 if (var1 + 1) != var2 else 0):
                                    continue
                                break  # end loop
                            if (1 if var2 >= 40000 else 0):
                                break
                        var3 = (var2 + 1)
                        i32_store(9140300, (var2 + 1))
                        i32_store(((var2 << 2) + 8451904), var18)
                        var2 = var3
                        var4 = (var4 + 1)
                        if (1 if (var4 + 1) != var13 else 0):
                            continue
                        break
                        break  # end loop
                    raise RuntimeError('unreachable')
                while True:  # loop $label211
                    var1 = i32_load((var17 + (var4 << 2)))
                    if (1 if i32_load((var17 + (var4 << 2))) == 0 else 0):
                        break
                    var1 = i32_load((var8 + (var1 * 132)) + 28)
                    if (1 if (1 if i32_load8_u((var8 + (i32_load((var8 + (var1 * 132)) + 28) * 132)) + 125) == 3 else 0) == (1 if var15 != 0 else 0) else 0):
                        break
                    var5 = (var5 + 1)
                    if (1 if var2 > 39999 else 0):
                        break
                    var3 = (var2 + 1)
                    i32_store(9140300, (var2 + 1))
                    i32_store(((var2 << 2) + 8451904), var1)
                    var2 = var3
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != var13 else 0):
                        continue
                    break  # end loop
                var7 = (var7 + 1)
                if (1 if (var7 + 1) != 255 else 0):
                    continue
                break  # end loop
            break
        var2 = i32_load((((var16 + (var9 * 286704)) + var20) + 285656))
        if (1 if i32_load((((var16 + (var9 * 286704)) + var20) + 285656)) == 0 else 0):
            break
        var7 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        var4 = 0
        var8 = i32_load8_u(var0 + 45)
        var3 = i32_load(9671128)
        var13 = i32_load(var2)
        var5 = 0
        var2 = var6
        if (1 if i32_load(9684388) >= 2 else 0):
            while True:  # loop $label217
                var1 = i32_load((var13 + (var4 << 2)))
                if (1 if i32_load((var13 + (var4 << 2))) == 0 else 0):
                    break
                var15 = i32_load((var3 + (var1 * 132)) + 28)
                if (1 if (1 if i32_load8_u((var3 + (i32_load((var3 + (var1 * 132)) + 28) * 132)) + 125) == 3 else 0) == (1 if var8 != 0 else 0) else 0):
                    break
                var5 = (var5 + 1)
                var1 = 0
                if var2:
                    while True:  # loop $label216
                        if (1 if i32_load(((var1 << 2) + 8451904)) == var15 else 0):
                            break
                        var1 = (var1 + 1)
                        if (1 if (var1 + 1) != var2 else 0):
                            continue
                        break  # end loop
                    if (1 if var2 >= 40000 else 0):
                        break
                var1 = (var2 + 1)
                i32_store(9140300, (var2 + 1))
                i32_store(((var2 << 2) + 8451904), var15)
                var2 = var1
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != var7 else 0):
                    continue
                break
                break  # end loop
            raise RuntimeError('unreachable')
        while True:  # loop $label219
            var1 = i32_load((var13 + (var4 << 2)))
            if (1 if i32_load((var13 + (var4 << 2))) == 0 else 0):
                break
            var15 = i32_load((var3 + (var1 * 132)) + 28)
            if (1 if (1 if i32_load8_u((var3 + (i32_load((var3 + (var1 * 132)) + 28) * 132)) + 125) == 3 else 0) == (1 if var8 != 0 else 0) else 0):
                break
            var5 = (var5 + 1)
            if (1 if var2 > 39999 else 0):
                break
            var1 = (var2 + 1)
            i32_store(9140300, (var2 + 1))
            i32_store(((var2 << 2) + 8451904), var15)
            var2 = var1
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var7 else 0):
                continue
            break  # end loop
        var1 = i32_load(var0 + 12)
        var4 = i32_load(var0 + 16)
        if i32_load(var0 + 16):
            break
        if (1 if var1 < var5 else 0):
            break
        break
        var1 = i32_load(var0 + 12)
        var4 = i32_load(var0 + 16)
        var5 = 0
        if (1 if var4 == 0 else 0):
            break
        if (1 if var1 <= var5 else 0):
            break
        var10 = 1
        i32_store((var11 + var12), 1)
        var1 = i32_load(var0 + 12)
        var4 = i32_load(var0 + 16)
        if (1 if var4 == 0 else 0):
            break
        if (1 if var1 > var5 else 0):
            break
        i32_store(9140300, var6)
        var9 = (var9 + 1)
        var1 = i32_load(9142892)
        if (1 if (var9 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    return (var10 & 1)

