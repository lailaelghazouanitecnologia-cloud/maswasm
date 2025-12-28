"""
Auto-generated from WAT. Contains 4 functions.
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
# $func669
# ==========================================================
def func669(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var6 = i32_load(9671128)
    var3 = (i32_load(9671128) + (var0 * 132))
    if ((1 if var2 == 0 else 0) & (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 3 else 0)):
        break
    var2 = i32_load(var3 + 44)
    var4 = (i32_load(var3 + 44) << 2)
    var5 = i32_load(9215884)
    var2 = i32_load((i32_load(9215884) + (var2 << 4)) + 12)
    # br_table ['$label1', '$label2', '$label3', '$label4', '$label5', '$label0']
    _br_idx = i32_load(var1 + 28)
    break  # br_table
    if (1 if i32_load((var5 + ((var4 << 2) | 4))) == 6 else 0):
        break
    break
    if (1 if i32_load((var5 + ((var4 << 2) | 4))) == 4 else 0):
        break
    break
    if (1 if i32_load((var5 + ((var4 << 2) | 4))) == 13 else 0):
        break
    break
    if (1 if i32_load((var5 + ((var4 << 2) | 4))) == 46 else 0):
        break
    break
    var2 = i32_load((var6 + (var0 * 132)) + 36)
    if (1 if i32_load((var6 + (var0 * 132)) + 36) == 0 else 0):
        break
    var0 = 0
    if (1 if var2 == 0 else 0):
        break
    if (1 if i32_load(var3 + 28) == var2 else 0):
        break
    var3 = i32_load(9671128)
    if i32_load(var1 + 8):
        var0 = i32_load(var1 + 104)
        if (1 if i32_load(var1 + 104) == 0 else 0):
            break
        var2 = i32_load((var3 + (var2 * 132)) + 28)
        var3 = i32_load(var1 + 96)
        var1 = 0
        while True:  # loop $label9
            if (1 if var2 != i32_load((var3 + (var1 << 2))) else 0):
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var0 else 0):
                    continue
                break
            break  # end loop
        var0 = 1
        if (1 if var1 < 0 else 0):
            break
        break
    var2 = i32_load8_u((var3 + (var2 * 132)) + 122)
    var1 = i32_load(var1 + 36)
    if (1 if i32_load(var1 + 36) <= 3 else 0):
        # br_table ['$label10', '$label11', '$label12', '$label13']
        _br_idx = (var1 - 1)
        break  # br_table
        var0 = 1
        var1 = ((var2 * 404) + 9568096)
        if i32_load(((var2 * 404) + 9568096) + 264):
            break
        if (1 if i32_load(var1 + 268) == 1 else 0):
            break
        var0 = (1 if i32_load(((var2 * 404) + 9568096) + 92) == 0 else 0)
        var0 = ((var0 | (1 if i32_load(38456) == var2 else 0)) | (1 if i32_load(38764) == var2 else 0))
        break
        var0 = (1 if i32_load(((var2 * 404) + 9568096) + 264) != 0 else 0)
        break
        var0 = (1 if i32_load(((var2 * 404) + 9568096) + 264) != 1 else 0)
        break
    var0 = 1
    if (1 if (var1 - 4) == var2 else 0):
        break
    var0 = 0
    var7 = var0
    return var7


# ==========================================================
# $func670
# ==========================================================
def func670(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var4 = i32_load(9671128)
    if ((1 if var2 == 0 else 0) & (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 3 else 0)):
        break
    var2 = i32_load(var1 + 96)
    # br_table ['$label1', '$label2', '$label3', '$label4']
    _br_idx = i32_load(var1 + 36)
    break  # br_table
    var1 = (var4 + (var0 * 132))
    var3 = i32_load(var2)
    if (1 if i32_load(var2) != 2147483647 else 0):
        if (1 if i32_load(var1 + 52) < var3 else 0):
            break
    var3 = i32_load(var2 + 4)
    if (1 if i32_load(var2 + 4) != 2147483647 else 0):
        if (1 if i32_load(var1 + 60) < var3 else 0):
            break
    var1 = i32_load(var2 + 8)
    var3 = (1 if i32_load(var2 + 8) == 2147483647 else 0)
    if (1 if (1 if i32_load(var2 + 8) == 2147483647 else 0) == 0 else 0):
        if (1 if i32_load((var4 + (var0 * 132)) + 64) < var1 else 0):
            break
    if (1 if var3 == 0 else 0):
        if (1 if i32_load((var4 + (var0 * 132)) + 68) < i32_load(var2 + 12) else 0):
            break
    var1 = i32_load(var2 + 16)
    var3 = (1 if i32_load(var2 + 16) == 2147483647 else 0)
    if (1 if (1 if i32_load(var2 + 16) == 2147483647 else 0) == 0 else 0):
        if (1 if i32_load((var4 + (var0 * 132)) + 72) < var1 else 0):
            break
    if (1 if var3 == 0 else 0):
        if (1 if i32_load((var4 + (var0 * 132)) + 76) < i32_load(var2 + 20) else 0):
            break
    var1 = i32_load(var2 + 24)
    if (1 if i32_load(var2 + 24) == 2147483647 else 0):
        break
    if (1 if i32_load((var4 + (var0 * 132)) + 84) >= var1 else 0):
        break
    break
    var1 = (var4 + (var0 * 132))
    var3 = i32_load(var2)
    if (1 if i32_load(var2) != 2147483647 else 0):
        if (1 if i32_load(var1 + 52) > var3 else 0):
            break
    var3 = i32_load(var2 + 4)
    if (1 if i32_load(var2 + 4) != 2147483647 else 0):
        if (1 if i32_load(var1 + 60) > var3 else 0):
            break
    var1 = i32_load(var2 + 8)
    var3 = (1 if i32_load(var2 + 8) == 2147483647 else 0)
    if (1 if (1 if i32_load(var2 + 8) == 2147483647 else 0) == 0 else 0):
        if (1 if i32_load((var4 + (var0 * 132)) + 64) > var1 else 0):
            break
    if (1 if var3 == 0 else 0):
        if (1 if i32_load((var4 + (var0 * 132)) + 68) > i32_load(var2 + 12) else 0):
            break
    var1 = i32_load(var2 + 16)
    var3 = (1 if i32_load(var2 + 16) == 2147483647 else 0)
    if (1 if (1 if i32_load(var2 + 16) == 2147483647 else 0) == 0 else 0):
        if (1 if i32_load((var4 + (var0 * 132)) + 72) > var1 else 0):
            break
    if (1 if var3 == 0 else 0):
        if (1 if i32_load((var4 + (var0 * 132)) + 76) > i32_load(var2 + 20) else 0):
            break
    var1 = i32_load(var2 + 24)
    if (1 if i32_load(var2 + 24) == 2147483647 else 0):
        break
    if (1 if i32_load((var4 + (var0 * 132)) + 84) <= var1 else 0):
        break
    break
    var1 = (var4 + (var0 * 132))
    var3 = i32_load(var2)
    if (1 if i32_load(var2) != 2147483647 else 0):
        if (1 if i32_load(var1 + 52) != var3 else 0):
            break
    var3 = i32_load(var2 + 4)
    if (1 if i32_load(var2 + 4) != 2147483647 else 0):
        if (1 if i32_load(var1 + 60) != var3 else 0):
            break
    var1 = i32_load(var2 + 8)
    var3 = (1 if i32_load(var2 + 8) == 2147483647 else 0)
    if (1 if (1 if i32_load(var2 + 8) == 2147483647 else 0) == 0 else 0):
        if (1 if i32_load((var4 + (var0 * 132)) + 64) != var1 else 0):
            break
    if (1 if var3 == 0 else 0):
        if (1 if i32_load((var4 + (var0 * 132)) + 68) != i32_load(var2 + 12) else 0):
            break
    var1 = i32_load(var2 + 16)
    var3 = (1 if i32_load(var2 + 16) == 2147483647 else 0)
    if (1 if (1 if i32_load(var2 + 16) == 2147483647 else 0) == 0 else 0):
        if (1 if i32_load((var4 + (var0 * 132)) + 72) != var1 else 0):
            break
    if (1 if var3 == 0 else 0):
        if (1 if i32_load((var4 + (var0 * 132)) + 76) != i32_load(var2 + 20) else 0):
            break
    var1 = i32_load(var2 + 24)
    if (1 if i32_load(var2 + 24) == 2147483647 else 0):
        break
    if (1 if i32_load((var4 + (var0 * 132)) + 84) != var1 else 0):
        break
    var5 = 1
    return var5


# ==========================================================
# $func671
# ==========================================================
def func671(var0, var1, var2):
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
    var6 = i32_load(9671128)
    if ((1 if var2 == 0 else 0) & (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 3 else 0)):
        break
    if (1 if i32_load(var1 + 8) == 0 else 0):
        var5 = i32_load(var1 + 104)
        if (1 if i32_load(var1 + 104) == 0 else 0):
            break
        var4 = (var6 + (var0 * 132))
        var2 = (i32_load(var1 + 28) << 1)
        var9 = ((i32_load(var1 + 28) << 1) * var2)
        var10 = i32_load(var1 + 96)
        var2 = 0
        if i32_load(var1 + 36):
            break
        while True:  # loop $label3
            var1 = (var6 + (i32_load((var10 + (var2 << 2))) * 132))
            if (1 if i32_load8_u((var6 + (i32_load((var10 + (var2 << 2))) * 132)) + 125) == 3 else 0):
                break
            var3 = ((i32_load16_u(var4 + 112) - i32_load16_u(var1 + 112)) << 1)
            var3 = ((i32_load16_u(var4 + 114) - i32_load16_u(var1 + 114)) << 1)
            if (1 if (((((i32_load16_u(var4 + 112) - i32_load16_u(var1 + 112)) << 1) * var3) + (((i32_load16_u(var4 + 114) - i32_load16_u(var1 + 114)) << 1) * var3)) - 1) > var9 else 0):
                break
            if (1 if i32_load(var1 + 28) == var0 else 0):
                break
            var3 = 1
            break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var3 = 0
        break
    var5 = i32_load(9142892)
    if (1 if i32_load(9142892) == 0 else 0):
        break
    var9 = i32_load(var1 + 64)
    var10 = (i32_load(var1 + 64) + (var5 << 2))
    var4 = (var6 + (var0 * 132))
    var3 = 1
    var0 = (i32_load(var1 + 28) << 1)
    var7 = ((i32_load(var1 + 28) << 1) * var0)
    var0 = 0
    var15 = i32_load(9561692)
    var16 = i32_load(9142420)
    var1 = i32_load(var1 + 36)
    if (1 if i32_load(var1 + 36) <= 3 else 0):
        var12 = i32_load(38764)
        var13 = i32_load(38456)
        var11 = (var1 - 1)
        while True:  # loop $label13
            var1 = (var0 << 2)
            if (1 if i32_load((var9 + (var0 << 2))) == 0 else 0):
                if (1 if i32_load(var10) == 0 else 0):
                    break
                if (1 if i32_load((var1 + var16)) == 0 else 0):
                    break
            var1 = 0
            while True:  # loop $label12
                # br_table ['$label5', '$label6', '$label7', '$label8']
                _br_idx = var11
                break  # br_table
                if (1 if i32_load(((var1 * 404) + 9568096) + 264) == 1 else 0):
                    break
                break
                if (1 if i32_load(((var1 * 404) + 9568096) + 264) == 0 else 0):
                    break
                break
                var2 = ((var1 * 404) + 9568096)
                if i32_load(((var1 * 404) + 9568096) + 264):
                    break
                if (1 if i32_load(var2 + 268) == 1 else 0):
                    break
                if (1 if i32_load(var2 + 92) == 0 else 0):
                    break
                if (1 if var1 == var13 else 0):
                    break
                if (1 if var1 == var12 else 0):
                    break
                var2 = i32_load((((var15 + (var0 * 286704)) + (var1 << 2)) + 284636))
                if (1 if i32_load((((var15 + (var0 * 286704)) + (var1 << 2)) + 284636)) == 0 else 0):
                    break
                var17 = i32_load(var2 + 8)
                if (1 if i32_load(var2 + 8) == 0 else 0):
                    break
                var18 = i32_load(var2)
                var2 = 0
                while True:  # loop $label11
                    var8 = i32_load((var18 + (var2 << 2)))
                    if (1 if i32_load((var18 + (var2 << 2))) == 0 else 0):
                        break
                    var8 = (var6 + (var8 * 132))
                    var14 = ((i32_load16_u(var4 + 112) - i32_load16_u((var6 + (var8 * 132)) + 112)) << 1)
                    var14 = ((i32_load16_u(var4 + 114) - i32_load16_u(var8 + 114)) << 1)
                    if (1 if (((((i32_load16_u(var4 + 112) - i32_load16_u((var6 + (var8 * 132)) + 112)) << 1) * var14) + (((i32_load16_u(var4 + 114) - i32_load16_u(var8 + 114)) << 1) * var14)) - 1) > var7 else 0):
                        break
                    if (1 if i32_load(var8 + 28) != i32_load(var4 + 28) else 0):
                        break
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != var17 else 0):
                        continue
                    break  # end loop
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != 255 else 0):
                    continue
                break  # end loop
            var0 = (var0 + 1)
            var3 = (1 if (var0 + 1) < var5 else 0)
            if (1 if var0 != var5 else 0):
                continue
            break  # end loop
        break
    var8 = ((var1 - 4) << 2)
    while True:  # loop $label17
        var1 = (var0 << 2)
        if (1 if i32_load((var9 + (var0 << 2))) == 0 else 0):
            if (1 if i32_load(var10) == 0 else 0):
                break
            if (1 if i32_load((var1 + var16)) == 0 else 0):
                break
        var1 = i32_load((((var15 + (var0 * 286704)) + var8) + 284636))
        if (1 if i32_load((((var15 + (var0 * 286704)) + var8) + 284636)) == 0 else 0):
            break
        var12 = i32_load(var1 + 8)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        var13 = i32_load(var1)
        var2 = 0
        while True:  # loop $label16
            var1 = i32_load((var13 + (var2 << 2)))
            if (1 if i32_load((var13 + (var2 << 2))) == 0 else 0):
                break
            var1 = (var6 + (var1 * 132))
            var11 = ((i32_load16_u(var4 + 112) - i32_load16_u((var6 + (var1 * 132)) + 112)) << 1)
            var11 = ((i32_load16_u(var4 + 114) - i32_load16_u(var1 + 114)) << 1)
            if (1 if (((((i32_load16_u(var4 + 112) - i32_load16_u((var6 + (var1 * 132)) + 112)) << 1) * var11) + (((i32_load16_u(var4 + 114) - i32_load16_u(var1 + 114)) << 1) * var11)) - 1) > var7 else 0):
                break
            if (1 if i32_load(var1 + 28) != i32_load(var4 + 28) else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var12 else 0):
                continue
            break  # end loop
        var0 = (var0 + 1)
        var3 = (1 if (var0 + 1) < var5 else 0)
        if (1 if var0 != var5 else 0):
            continue
        break  # end loop
    break
    while True:  # loop $label18
        var3 = 0
        var1 = (var6 + (i32_load((var10 + (var2 << 2))) * 132))
        if (1 if i32_load8_u((var6 + (i32_load((var10 + (var2 << 2))) * 132)) + 125) == 3 else 0):
            break
        var7 = ((i32_load16_u(var4 + 112) - i32_load16_u(var1 + 112)) << 1)
        var7 = ((i32_load16_u(var4 + 114) - i32_load16_u(var1 + 114)) << 1)
        if (1 if (((((i32_load16_u(var4 + 112) - i32_load16_u(var1 + 112)) << 1) * var7) + (((i32_load16_u(var4 + 114) - i32_load16_u(var1 + 114)) << 1) * var7)) - 1) > var9 else 0):
            break
        if (1 if i32_load(var1 + 28) == var0 else 0):
            break
        var3 = 1
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var5 else 0):
            continue
        break  # end loop
    return var3


# ==========================================================
# $func672
# ==========================================================
def func672(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var3 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) != 3 else 0):
        break
    if var2:
        break
    return 0
    var0 = i32_load16_u(var3 + 114)
    var5 = i32_load16_u(var3 + 112)
    var2 = i32_load(var1 + 20)
    var3 = ((i32_load8_u(var3 + 122) * 404) + 9568096)
    var6 = (i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 216) - 1)
    if (i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 216) - 1):
        var3 = i32_load(var3 + 220)
        var7 = (1 if var2 > var5 else 0)
        if (1 if var2 > var5 else 0):
            break
        if (1 if (i32_load(var1 + 28) + var2) <= var5 else 0):
            break
        var8 = i32_load(var1 + 24)
        if (1 if i32_load(var1 + 24) > var0 else 0):
            break
        var4 = 1
        if (1 if (i32_load(var1 + 40) + var8) > var0 else 0):
            break
        var3 = (var3 - 1)
        var4 = (var5 + var6)
        if (1 if var2 > (var5 + var6) else 0):
            break
        if (1 if (i32_load(var1 + 28) + var2) <= var4 else 0):
            break
        var6 = i32_load(var1 + 24)
        if (1 if var0 >= i32_load(var1 + 24) else 0):
            var4 = 1
            if (1 if (i32_load(var1 + 40) + var6) > var0 else 0):
                break
        var6 = i32_load(var1 + 24)
        var0 = (var0 + var3)
        if (1 if i32_load(var1 + 24) > (var0 + var3) else 0):
            break
        var4 = 1
        if (1 if (i32_load(var1 + 40) + var6) > var0 else 0):
            break
        break
    if (1 if var2 > var5 else 0):
        break
    if (1 if (i32_load(var1 + 28) + var2) <= var5 else 0):
        break
    var2 = i32_load(var1 + 24)
    if (1 if i32_load(var1 + 24) > var0 else 0):
        break
    var4 = (1 if (i32_load(var1 + 40) + var2) > var0 else 0)
    break
    var0 = (var0 + var3)
    if var7:
        return 0
    if (1 if var5 >= (i32_load(var1 + 28) + var2) else 0):
        return 0
    var4 = 0
    var2 = i32_load(var1 + 24)
    if (1 if i32_load(var1 + 24) > var0 else 0):
        break
    return (1 if (i32_load(var1 + 40) + var2) > var0 else 0)
    return var4

