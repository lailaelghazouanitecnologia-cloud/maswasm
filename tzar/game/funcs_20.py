"""
Auto-generated from WAT. Contains 3 functions.
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
# $func299
# ==========================================================
def func299(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var3 = i32_load(9142892)
    if i32_load(9142892):
        while True:  # loop $label9
            var2 = i32_load(var0 + 48)
            var4 = (var5 << 2)
            if (1 if i32_load((i32_load(var0 + 48) + (var5 << 2))) == 0 else 0):
                if (1 if i32_load((var2 + (var3 << 2))) == 0 else 0):
                    break
                if (1 if i32_load((i32_load(9142420) + var4)) == 0 else 0):
                    break
            var2 = 0
            var7 = i32_load(9561692)
            var8 = i32_load(var0 + 32)
            if (1 if i32_load(var0 + 32) <= 3 else 0):
                while True:  # loop $label7
                    # br_table ['$label1', '$label2', '$label3', '$label4']
                    _br_idx = (var8 - 1)
                    break  # br_table
                    var3 = ((var2 * 404) + 9568096)
                    if i32_load(((var2 * 404) + 9568096) + 264):
                        break
                    if (1 if i32_load(var3 + 268) == 1 else 0):
                        break
                    if (1 if i32_load(var3 + 92) == 0 else 0):
                        break
                    if (1 if i32_load(38456) == var2 else 0):
                        break
                    if (1 if i32_load(38764) != var2 else 0):
                        break
                    break
                    if (1 if i32_load(((var2 * 404) + 9568096) + 264) == 1 else 0):
                        break
                    break
                    if i32_load(((var2 * 404) + 9568096) + 264):
                        break
                    var6 = i32_load((((var7 + (var5 * 286704)) + (var2 << 2)) + 284636))
                    if (1 if i32_load((((var7 + (var5 * 286704)) + (var2 << 2)) + 284636)) == 0 else 0):
                        break
                    var3 = 0
                    var4 = i32_load(var6 + 8)
                    if (1 if i32_load(var6 + 8) == 0 else 0):
                        break
                    while True:  # loop $label6
                        var9 = i32_load((i32_load(var6) + (var3 << 2)))
                        if i32_load((i32_load(var6) + (var3 << 2))):
                            # call_indirect via table[var1]
                            var4 = i32_load(var6 + 8)
                        var3 = (var3 + 1)
                        if (1 if (var3 + 1) < var4 else 0):
                            continue
                        break  # end loop
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != 255 else 0):
                        continue
                    break
                    break  # end loop
                raise RuntimeError('unreachable')
            var2 = i32_load((((var7 + (var5 * 286704)) + (var8 << 2)) + 284620))
            if (1 if i32_load((((var7 + (var5 * 286704)) + (var8 << 2)) + 284620)) == 0 else 0):
                break
            var3 = 0
            var4 = i32_load(var2 + 8)
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            while True:  # loop $label8
                var6 = i32_load((i32_load(var2) + (var3 << 2)))
                if i32_load((i32_load(var2) + (var3 << 2))):
                    # call_indirect via table[var1]
                    var4 = i32_load(var2 + 8)
                var3 = (var3 + 1)
                if (1 if (var3 + 1) < var4 else 0):
                    continue
                break  # end loop
            var5 = (var5 + 1)
            var3 = i32_load(9142892)
            if (1 if (var5 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop


# ==========================================================
# $func300
# ==========================================================
def func300(var0, var1, var2):
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
    var6 = i32_load(9142892)
    if (1 if i32_load(9142892) == 0 else 0):
        break
    var11 = i32_load(var1)
    var12 = (i32_load(var1) + (var6 << 2))
    var13 = i32_load16_u(var2 + 114)
    var14 = i32_load16_u(var2 + 112)
    var15 = i32_load(var2 + 28)
    var16 = i32_load(9671128)
    var17 = i32_load(9561692)
    var18 = i32_load(9142420)
    var1 = 2147483647
    if (1 if var0 <= 3 else 0):
        var7 = i32_load(38764)
        var8 = i32_load(38456)
        var9 = (var0 - 1)
        while True:  # loop $label10
            var0 = (var3 << 2)
            if (1 if i32_load((var11 + (var3 << 2))) == 0 else 0):
                if (1 if i32_load(var12) == 0 else 0):
                    break
                if (1 if i32_load((var0 + var18)) == 0 else 0):
                    break
            var0 = 0
            while True:  # loop $label9
                # br_table ['$label2', '$label3', '$label4', '$label5']
                _br_idx = var9
                break  # br_table
                if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 1 else 0):
                    break
                break
                if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 0 else 0):
                    break
                break
                var2 = ((var0 * 404) + 9568096)
                if i32_load(((var0 * 404) + 9568096) + 264):
                    break
                if (1 if i32_load(var2 + 268) == 1 else 0):
                    break
                if (1 if i32_load(var2 + 92) == 0 else 0):
                    break
                if (1 if var0 == var8 else 0):
                    break
                if (1 if var0 == var7 else 0):
                    break
                var2 = i32_load((((var17 + (var3 * 286704)) + (var0 << 2)) + 284636))
                if (1 if i32_load((((var17 + (var3 * 286704)) + (var0 << 2)) + 284636)) == 0 else 0):
                    break
                var10 = i32_load(var2 + 8)
                if (1 if i32_load(var2 + 8) == 0 else 0):
                    break
                var19 = i32_load(var2)
                var2 = 0
                while True:  # loop $label8
                    var4 = i32_load((var19 + (var2 << 2)))
                    if (1 if i32_load((var19 + (var2 << 2))) == 0 else 0):
                        break
                    var4 = (var16 + (var4 * 132))
                    var20 = i32_load((var16 + (var4 * 132)) + 28)
                    if (1 if i32_load((var16 + (var4 * 132)) + 28) == var15 else 0):
                        break
                    var21 = ((i32_load16_u(var4 + 114) - var13) << 1)
                    var4 = ((i32_load16_u(var4 + 112) - var14) << 1)
                    var4 = ((((i32_load16_u(var4 + 114) - var13) << 1) * var21) + (((i32_load16_u(var4 + 112) - var14) << 1) * var4))
                    var4 = (1 if var1 > var4 else 0)
                    var1 = (((((i32_load16_u(var4 + 114) - var13) << 1) * var21) + (((i32_load16_u(var4 + 112) - var14) << 1) * var4)) if (1 if var1 > var4 else 0) else var1)
                    var5 = (var20 if var4 else var5)
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != var10 else 0):
                        continue
                    break  # end loop
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != 255 else 0):
                    continue
                break  # end loop
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var6 else 0):
                continue
            break  # end loop
        break
    var4 = ((var0 - 4) << 2)
    var0 = 0
    while True:  # loop $label14
        var2 = (var0 << 2)
        if (1 if i32_load((var11 + (var0 << 2))) == 0 else 0):
            if (1 if i32_load(var12) == 0 else 0):
                break
            if (1 if i32_load((var2 + var18)) == 0 else 0):
                break
        var2 = i32_load((((var17 + (var0 * 286704)) + var4) + 284636))
        if (1 if i32_load((((var17 + (var0 * 286704)) + var4) + 284636)) == 0 else 0):
            break
        var7 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        var8 = i32_load(var2)
        var2 = 0
        while True:  # loop $label13
            var3 = i32_load((var8 + (var2 << 2)))
            if (1 if i32_load((var8 + (var2 << 2))) == 0 else 0):
                break
            var3 = (var16 + (var3 * 132))
            var9 = i32_load((var16 + (var3 * 132)) + 28)
            if (1 if i32_load((var16 + (var3 * 132)) + 28) == var15 else 0):
                break
            var10 = ((i32_load16_u(var3 + 114) - var13) << 1)
            var3 = ((i32_load16_u(var3 + 112) - var14) << 1)
            var3 = ((((i32_load16_u(var3 + 114) - var13) << 1) * var10) + (((i32_load16_u(var3 + 112) - var14) << 1) * var3))
            var3 = (1 if var1 > var3 else 0)
            var1 = (((((i32_load16_u(var3 + 114) - var13) << 1) * var10) + (((i32_load16_u(var3 + 112) - var14) << 1) * var3)) if (1 if var1 > var3 else 0) else var1)
            var5 = (var9 if var3 else var5)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var7 else 0):
                continue
            break  # end loop
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var6 else 0):
            continue
        break  # end loop
    return var5


# ==========================================================
# $func301
# ==========================================================
def func301(var0, var1, var2, var3):
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
    var7 = (i32_load(9142892) * var2)
    var21 = i32_load(9142440)
    var13 = (i32_load(9142440) + 2)
    var23 = ((i32_load(9142440) + 2) << 1)
    var8 = i32_load(9215884)
    var15 = i32_load(38564)
    var16 = i32_load(38620)
    var17 = i32_load(38560)
    var9 = i32_load(9143004)
    var18 = i32_load(38500)
    var10 = i32_load(9671128)
    var19 = i32_load(9142840)
    var2 = 0
    while True:  # loop $label7
        var22 = var2
        var4 = (var2 << 2)
        var2 = (i32_load((((var2 << 2) | 4) + 8611904)) + var1)
        if (1 if var21 <= (i32_load((((var2 << 2) | 4) + 8611904)) + var1) else 0):
            break
        var4 = (i32_load((var4 + 8611904)) + var0)
        if (1 if var21 <= (i32_load((var4 + 8611904)) + var0) else 0):
            break
        if (1 if (var2 | var4) < 0 else 0):
            break
        var11 = (var4 + 1)
        var14 = (var2 + 1)
        var2 = i32_load((var19 + (((var4 + 1) + ((var2 + 1) * var13)) << 2)))
        if (1 if i32_load((var19 + (((var4 + 1) + ((var2 + 1) * var13)) << 2))) < 3 else 0):
            break
        var4 = (var10 + (var2 * 132))
        var6 = i32_load8_u((var10 + (var2 * 132)) + 122)
        var12 = ((i32_load8_u((var10 + (var2 * 132)) + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u((var10 + (var2 * 132)) + 122) * 404) + 9568096) + 340) == 0 else 0):
            break
        if (1 if var6 == var18 else 0):
            break
        var5 = i32_load16_u(var4 + 110)
        var20 = i32_load16_u(var4 + 120)
        if i32_load16_u(var4 + 120):
        else:
        if (1 if i32_load8_u(((var20 if i32_load8_u((var9 + (var5 + var7))) else var5) + (var5 + var7))) == 0 else 0):
            if (1 if i32_load8_u(var4 + 127) != 6 else 0):
                break
            if (1 if i32_load8_u(var4 + 128) == 0 else 0):
                break
            break
        if i32_load8_u(var4 + 128):
            break
        if (1 if i32_load8_u(var4 + 125) == 10 else 0):
            break
        if (1 if i32_load8_u(var4 + 126) == 2 else 0):
            break
        if (1 if i32_load(var4 + 64) == -1 else 0):
            break
        if (1 if i32_load(var12 + 264) == 2 else 0):
            break
        if (1 if i32_load(var12 + 188) != 55 else 0):
            break
        if (1 if var6 == var17 else 0):
            break
        if (1 if var6 == var16 else 0):
            break
        if (1 if var6 == var15 else 0):
            break
        if (1 if ((1 if var3 == -1 else 0) | (1 if var3 == var6 else 0)) == 0 else 0):
            break
        var5 = i32_load(var4 + 104)
        if (1 if i32_load(var4 + 104) == 0 else 0):
            break
        var5 = i32_load((var10 + (var5 * 132)) + 44)
        if (1 if i32_load((var8 + (i32_load((var10 + (var5 * 132)) + 44) << 4)) + 4) != 40 else 0):
            break
        if (1 if i32_load((var8 + ((var5 << 4) | 12))) != i32_load(var4 + 28) else 0):
            break
        var2 = i32_load((var19 + ((var11 + ((var13 + var14) * var13)) << 2)))
        if (1 if i32_load((var19 + ((var11 + ((var13 + var14) * var13)) << 2))) < 3 else 0):
            break
        var4 = (var10 + (var2 * 132))
        var6 = i32_load8_u((var10 + (var2 * 132)) + 122)
        var12 = ((i32_load8_u((var10 + (var2 * 132)) + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u((var10 + (var2 * 132)) + 122) * 404) + 9568096) + 340) == 0 else 0):
            break
        if (1 if var6 == var18 else 0):
            break
        var5 = i32_load16_u(var4 + 110)
        var20 = i32_load16_u(var4 + 120)
        if i32_load16_u(var4 + 120):
        else:
        if i32_load8_u(((var20 if i32_load8_u((var9 + (var5 + var7))) else var5) + (var5 + var7))):
            if (1 if i32_load8_u(var4 + 128) == 0 else 0):
                break
            break
        if (1 if i32_load8_u(var4 + 127) != 6 else 0):
            break
        if i32_load8_u(var4 + 128):
            break
        if (1 if i32_load8_u(var4 + 125) == 10 else 0):
            break
        if (1 if i32_load8_u(var4 + 126) == 2 else 0):
            break
        if (1 if i32_load(var4 + 64) == -1 else 0):
            break
        if (1 if i32_load(var12 + 264) == 2 else 0):
            break
        if (1 if i32_load(var12 + 188) != 55 else 0):
            break
        if (1 if var6 == var17 else 0):
            break
        if (1 if var6 == var16 else 0):
            break
        if (1 if var6 == var15 else 0):
            break
        if (1 if ((1 if var3 == -1 else 0) | (1 if var3 == var6 else 0)) == 0 else 0):
            break
        var5 = i32_load(var4 + 104)
        if (1 if i32_load(var4 + 104) == 0 else 0):
            break
        var5 = i32_load((var10 + (var5 * 132)) + 44)
        if (1 if i32_load((var8 + (i32_load((var10 + (var5 * 132)) + 44) << 4)) + 4) != 40 else 0):
            break
        if (1 if i32_load((var8 + ((var5 << 4) | 12))) != i32_load(var4 + 28) else 0):
            break
        var2 = i32_load((var19 + ((var11 + ((var14 + var23) * var13)) << 2)))
        if (1 if i32_load((var19 + ((var11 + ((var14 + var23) * var13)) << 2))) < 3 else 0):
            break
        var4 = (var10 + (var2 * 132))
        var5 = i32_load8_u((var10 + (var2 * 132)) + 122)
        var11 = ((i32_load8_u((var10 + (var2 * 132)) + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u((var10 + (var2 * 132)) + 122) * 404) + 9568096) + 340) == 0 else 0):
            break
        if (1 if var5 == var18 else 0):
            break
        var6 = i32_load16_u(var4 + 110)
        var14 = i32_load16_u(var4 + 120)
        if i32_load16_u(var4 + 120):
        else:
        if i32_load8_u(((var14 if i32_load8_u((var9 + (var6 + var7))) else var6) + (var6 + var7))):
            if (1 if i32_load8_u(var4 + 128) == 0 else 0):
                break
            break
        if (1 if i32_load8_u(var4 + 127) != 6 else 0):
            break
        if i32_load8_u(var4 + 128):
            break
        if (1 if i32_load8_u(var4 + 125) == 10 else 0):
            break
        if (1 if i32_load8_u(var4 + 126) == 2 else 0):
            break
        if (1 if i32_load(var4 + 64) == -1 else 0):
            break
        if (1 if i32_load(var11 + 264) == 2 else 0):
            break
        if (1 if i32_load(var11 + 188) != 55 else 0):
            break
        if (1 if var5 == var17 else 0):
            break
        if (1 if var5 == var16 else 0):
            break
        if (1 if var5 == var15 else 0):
            break
        if (1 if ((1 if var3 == -1 else 0) | (1 if var3 == var5 else 0)) == 0 else 0):
            break
        var5 = i32_load(var4 + 104)
        if (1 if i32_load(var4 + 104) == 0 else 0):
            break
        var5 = i32_load((var10 + (var5 * 132)) + 44)
        if (1 if i32_load((var8 + (i32_load((var10 + (var5 * 132)) + 44) << 4)) + 4) != 40 else 0):
            break
        if (1 if i32_load((var8 + ((var5 << 4) | 12))) != i32_load(var4 + 28) else 0):
            break
        var2 = (var22 + 2)
        if (1 if var22 < 5198 else 0):
            continue
        break  # end loop
    var2 = 0
    return var2

