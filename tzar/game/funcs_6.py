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
# $func165
# ==========================================================
def func165(var0, var1):
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
    # br_table ['$label0', '$label1', '$label2']
    _br_idx = i32_load(var0 + 4)
    break  # br_table
    if (1 if i32_load(var0 + 88) == 0 else 0):
        break
    var7 = i32_load(var0 + 32)
    var8 = (1 if i32_load(var0 + 32) == 0 else 0)
    while True:  # loop $label8
        var4 = i32_load((i32_load(var0 + 80) + (var6 << 2)))
        # call_indirect via table[var1]
        if (1 if call_indirect(var1) != (1 if i32_load8_u(var0 + 45) != 0 else 0) else 0):
            var3 = i32_load(9140300)
            if (1 if i32_load(9684388) >= 2 else 0):
                var2 = 0
                if (1 if var3 == 0 else 0):
                    break
                while True:  # loop $label6
                    if (1 if i32_load(((var2 << 2) + 8451904)) == var4 else 0):
                        break
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != var3 else 0):
                        continue
                    break  # end loop
            var2 = var3
            if (1 if var3 > 39999 else 0):
                break
            i32_store(9140300, (var2 + 1))
            i32_store(((var2 << 2) + 8451904), var4)
            i32_store((i32_load(9142420) + (i32_load16_u((i32_load(9671128) + (var4 * 132)) + 110) << 2)), 1)
            var5 = (var5 | var8)
            break
        if var7:
            break
        var6 = (var6 + 1)
        if (1 if (var6 + 1) < i32_load(var0 + 88) else 0):
            continue
        break  # end loop
    var7 = ((1 if var7 != 0 else 0) | var5)
    break
    var8 = i32_load(9140300)
    var4 = i32_load(var0 + 32)
    i32_store(9140300, 0)
    if i32_load(9142892):
        var3 = i32_load(9142420)
        while True:  # loop $label10
            i32_store((var3 + (var2 << 2)), 0)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    if var8:
        var9 = (1 if var4 == 0 else 0)
        while True:  # loop $label15
            var7 = i32_load(((var6 << 2) + 8451904))
            # call_indirect via table[var1]
            if (1 if call_indirect(var1) != (1 if i32_load8_u(var0 + 45) != 0 else 0) else 0):
                var3 = i32_load(9140300)
                if (1 if i32_load(9684388) >= 2 else 0):
                    var2 = 0
                    if (1 if var3 == 0 else 0):
                        break
                    while True:  # loop $label13
                        if (1 if i32_load(((var2 << 2) + 8451904)) == var7 else 0):
                            break
                        var2 = (var2 + 1)
                        if (1 if (var2 + 1) != var3 else 0):
                            continue
                        break  # end loop
                var2 = var3
                if (1 if var3 > 39999 else 0):
                    break
                i32_store(9140300, (var2 + 1))
                i32_store(((var2 << 2) + 8451904), var7)
                i32_store((i32_load(9142420) + (i32_load16_u((i32_load(9671128) + (var7 * 132)) + 110) << 2)), 1)
                var5 = (var5 | var9)
                break
            if var4:
                break
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != var8 else 0):
                continue
            break  # end loop
    var7 = ((1 if var4 != 0 else 0) | var5)
    break
    var7 = 0
    break
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) == 0 else 0):
        break
    var3 = i32_load(var0 + 32)
    var13 = (1 if i32_load(var0 + 32) > 3 else 0)
    var14 = (var3 - 1)
    var15 = ((var3 - 4) << 2)
    while True:  # loop $label38
        var3 = i32_load(var0 + 48)
        var2 = i32_load((i32_load(var0 + 48) + (var2 << 2)))
        var9 = (var8 << 2)
        if (1 if i32_load((var3 + (var8 << 2))) == 0 else 0):
            if (1 if var2 == 0 else 0):
                break
            if i32_load((i32_load(9142420) + var9)):
                break
            break
        if (1 if var2 == 0 else 0):
            break
        i32_store((i32_load(9142420) + var9), 0)
        var6 = 0
        var16 = i32_load(9140300)
        var10 = i32_load(9561692)
        var4 = 0
        if (1 if var13 == 0 else 0):
            while True:  # loop $label28
                # br_table ['$label19', '$label20', '$label21', '$label22']
                _br_idx = var14
                break  # br_table
                var2 = ((var4 * 404) + 9568096)
                if i32_load(((var4 * 404) + 9568096) + 264):
                    break
                if (1 if i32_load(var2 + 268) == 1 else 0):
                    break
                if (1 if i32_load(var2 + 92) == 0 else 0):
                    break
                if (1 if i32_load(38456) == var4 else 0):
                    break
                if (1 if i32_load(38764) != var4 else 0):
                    break
                break
                if (1 if i32_load(((var4 * 404) + 9568096) + 264) == 1 else 0):
                    break
                break
                if i32_load(((var4 * 404) + 9568096) + 264):
                    break
                var11 = i32_load((((var10 + (var8 * 286704)) + 284636) + (var4 << 2)))
                if (1 if i32_load((((var10 + (var8 * 286704)) + 284636) + (var4 << 2))) == 0 else 0):
                    break
                var5 = 0
                var17 = i32_load(var11 + 8)
                if (1 if i32_load(var11 + 8) == 0 else 0):
                    break
                while True:  # loop $label27
                    var2 = i32_load((i32_load(var11) + (var5 << 2)))
                    if (1 if i32_load((i32_load(var11) + (var5 << 2))) == 0 else 0):
                        break
                    var2 = (i32_load(9671128) + (var2 * 132))
                    # call_indirect via table[var1]
                    if (1 if call_indirect(var1) == (1 if i32_load8_u(var0 + 45) != 0 else 0) else 0):
                        break
                    var6 = (var6 + 1)
                    var3 = i32_load(9140300)
                    var12 = i32_load(var2 + 28)
                    if (1 if i32_load(9684388) >= 2 else 0):
                        var2 = 0
                        if (1 if var3 == 0 else 0):
                            break
                        while True:  # loop $label26
                            if (1 if i32_load(((var2 << 2) + 8451904)) == var12 else 0):
                                break
                            var2 = (var2 + 1)
                            if (1 if (var2 + 1) != var3 else 0):
                                continue
                            break  # end loop
                    var2 = var3
                    if (1 if var3 > 39999 else 0):
                        break
                    i32_store(9140300, (var2 + 1))
                    i32_store(((var2 << 2) + 8451904), var12)
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var17 else 0):
                        continue
                    break  # end loop
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != 255 else 0):
                    continue
                break
                break  # end loop
            raise RuntimeError('unreachable')
        var4 = i32_load((((var10 + (var8 * 286704)) + 284636) + var15))
        if (1 if i32_load((((var10 + (var8 * 286704)) + 284636) + var15)) == 0 else 0):
            break
        var5 = 0
        var11 = i32_load(var4 + 8)
        if (1 if i32_load(var4 + 8) == 0 else 0):
            break
        while True:  # loop $label34
            var2 = i32_load((i32_load(var4) + (var5 << 2)))
            if (1 if i32_load((i32_load(var4) + (var5 << 2))) == 0 else 0):
                break
            var2 = (i32_load(9671128) + (var2 * 132))
            # call_indirect via table[var1]
            if (1 if call_indirect(var1) == (1 if i32_load8_u(var0 + 45) != 0 else 0) else 0):
                break
            var6 = (var6 + 1)
            var3 = i32_load(9140300)
            var10 = i32_load(var2 + 28)
            if (1 if i32_load(9684388) >= 2 else 0):
                var2 = 0
                if (1 if var3 == 0 else 0):
                    break
                while True:  # loop $label33
                    if (1 if i32_load(((var2 << 2) + 8451904)) == var10 else 0):
                        break
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != var3 else 0):
                        continue
                    break  # end loop
            var2 = var3
            if (1 if var3 > 39999 else 0):
                break
            i32_store(9140300, (var2 + 1))
            i32_store(((var2 << 2) + 8451904), var10)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var11 else 0):
                continue
            break  # end loop
        var2 = i32_load(var0 + 12)
        var5 = i32_load(var0 + 16)
        if i32_load(var0 + 16):
            break
        if (1 if var2 < var6 else 0):
            break
        break
        var2 = i32_load(var0 + 12)
        var5 = i32_load(var0 + 16)
        if (1 if var5 == 0 else 0):
            break
        if (1 if var2 <= var6 else 0):
            break
        var7 = 1
        i32_store((i32_load(9142420) + var9), 1)
        var2 = i32_load(var0 + 12)
        var5 = i32_load(var0 + 16)
        if (1 if var5 == 0 else 0):
            break
        if (1 if var2 > var6 else 0):
            break
        i32_store(9140300, var16)
        var8 = (var8 + 1)
        var2 = i32_load(9142892)
        if (1 if (var8 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    return (var7 & 1)


# ==========================================================
# $func166
# ==========================================================
def func166(var0, var1, var2, var3):
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
    var7 = i32_load(9142432)
    if i32_load(9142432):
        var10 = (var1 << 1)
        var11 = (var0 << 1)
        var12 = i32_load(9142440)
        var13 = i32_load((var7 + (((i32_load(9142440) * var1) + var0) << 2)))
        var14 = i32_load(9671128)
        var0 = 2147483647
        var16 = (i32_load(9561692) + (var2 * 286704))
        while True:  # loop $label4
            var9 = ((var6 * 404) + 9568096)
            var1 = i32_load(((var6 * 404) + 9568096) + 192)
            if ((1 if var3 != i32_load(((var6 * 404) + 9568096) + 192) else 0) & (1 if var1 != 4 else 0)):
                break
            var1 = i32_load(((var16 + (var6 << 2)) + 284636))
            if (1 if i32_load(((var16 + (var6 << 2)) + 284636)) == 0 else 0):
                break
            var17 = i32_load(var1 + 8)
            if (1 if i32_load(var1 + 8) == 0 else 0):
                break
            var18 = i32_load(var1)
            var1 = 0
            while True:  # loop $label3
                var4 = i32_load((var18 + (var1 << 2)))
                if (1 if i32_load((var18 + (var1 << 2))) == 0 else 0):
                    break
                var5 = (var14 + (var4 * 132))
                var19 = i32_load16_u((var14 + (var4 * 132)) + 114)
                var4 = (var10 - (i32_load(var9 + 220) + (i32_load16_u((var14 + (var4 * 132)) + 114) << 1)))
                var15 = i32_load16_u(var5 + 112)
                var4 = (var11 - (i32_load(var9 + 216) + (i32_load16_u(var5 + 112) << 1)))
                var4 = (((var10 - (i32_load(var9 + 220) + (i32_load16_u((var14 + (var4 * 132)) + 114) << 1))) * var4) + ((var11 - (i32_load(var9 + 216) + (i32_load16_u(var5 + 112) << 1))) * var4))
                if (1 if (((var10 - (i32_load(var9 + 220) + (i32_load16_u((var14 + (var4 * 132)) + 114) << 1))) * var4) + ((var11 - (i32_load(var9 + 216) + (i32_load16_u(var5 + 112) << 1))) * var4)) >= var0 else 0):
                    break
                var15 = ((i32_load8_u(var5 + 122) * 404) + 9568096)
                if (1 if i32_load((var7 + (((var15 + ((i32_load(((i32_load8_u(var5 + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1)) + (var12 * (((i32_load(var15 + 220) & 0xFFFFFFFF) >> 1) + var19))) << 2))) != var13 else 0):
                    break
                if (1 if i32_load16_u(var5 + 110) != var2 else 0):
                    break
                # br_table ['$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label1', '$label2']
                _br_idx = (i32_load8_u(var5 + 125) - 4)
                break  # br_table
                var8 = i32_load(var5 + 28)
                var0 = var4
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var17 else 0):
                    continue
                break  # end loop
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != 255 else 0):
                continue
            break  # end loop
        break
    var9 = (var1 << 1)
    var10 = (var0 << 1)
    var11 = i32_load(9671128)
    var0 = 2147483647
    var12 = (i32_load(9561692) + (var2 * 286704))
    while True:  # loop $label10
        var7 = ((var5 * 404) + 9568096)
        var1 = i32_load(((var5 * 404) + 9568096) + 192)
        if ((1 if var3 != i32_load(((var5 * 404) + 9568096) + 192) else 0) & (1 if var1 != 4 else 0)):
            break
        var1 = i32_load(((var12 + (var5 << 2)) + 284636))
        if (1 if i32_load(((var12 + (var5 << 2)) + 284636)) == 0 else 0):
            break
        var13 = i32_load(var1 + 8)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        var14 = i32_load(var1)
        var1 = 0
        while True:  # loop $label9
            var4 = i32_load((var14 + (var1 << 2)))
            if (1 if i32_load((var14 + (var1 << 2))) == 0 else 0):
                break
            var6 = (var11 + (var4 * 132))
            var4 = (var9 - (i32_load(var7 + 220) + (i32_load16_u((var11 + (var4 * 132)) + 114) << 1)))
            var4 = (var10 - (i32_load(var7 + 216) + (i32_load16_u(var6 + 112) << 1)))
            var4 = (((var9 - (i32_load(var7 + 220) + (i32_load16_u((var11 + (var4 * 132)) + 114) << 1))) * var4) + ((var10 - (i32_load(var7 + 216) + (i32_load16_u(var6 + 112) << 1))) * var4))
            if (1 if (((var9 - (i32_load(var7 + 220) + (i32_load16_u((var11 + (var4 * 132)) + 114) << 1))) * var4) + ((var10 - (i32_load(var7 + 216) + (i32_load16_u(var6 + 112) << 1))) * var4)) >= var0 else 0):
                break
            if (1 if i32_load16_u(var6 + 110) != var2 else 0):
                break
            # br_table ['$label7', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label7', '$label8']
            _br_idx = (i32_load8_u(var6 + 125) - 4)
            break  # br_table
            var8 = i32_load(var6 + 28)
            var0 = var4
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var13 else 0):
                continue
            break  # end loop
        var5 = (var5 + 1)
        if (1 if (var5 + 1) != 255 else 0):
            continue
        break  # end loop
    return var8

