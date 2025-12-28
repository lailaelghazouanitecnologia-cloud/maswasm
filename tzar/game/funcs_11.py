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
# $func224
# ==========================================================
def func224(var0, var1, var2):
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
    var4 = i32_load(9142440)
    var6 = (i32_load(9142440) + 2)
    var7 = ((i32_load(9142440) + 2) if (1 if var1 != 2 else 0) else 0)
    var5 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var8 = (i32_load16_u(var0 + 114) + ((i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1))
    var9 = (i32_load16_u(var0 + 112) + ((i32_load(var5 + 216) & 0xFFFFFFFF) >> 1))
    var5 = i32_load(9671128)
    var10 = i32_load(9142840)
    if var2:
        while True:  # loop $label2
            var0 = var3
            var3 = (var3 << 2)
            var1 = (var8 + i32_load((((var3 << 2) | 4) + 8611904)))
            if (1 if var4 <= (var8 + i32_load((((var3 << 2) | 4) + 8611904))) else 0):
                break
            var3 = (var9 + i32_load((var3 + 8611904)))
            if (1 if var4 <= (var9 + i32_load((var3 + 8611904))) else 0):
                break
            if (1 if (var1 | var3) < 0 else 0):
                break
            var3 = i32_load((((var3 + (((var1 + var7) + 1) * var6)) << 2) + var10) + 4)
            if (1 if i32_load8_u((var5 + (i32_load((((var3 + (((var1 + var7) + 1) * var6)) << 2) + var10) + 4) * 132)) + 122) == var2 else 0):
                break
            var3 = (var0 + 2)
            if (1 if var0 <= 717 else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    if (1 if var1 == 2 else 0):
        var11 = i32_load(9142848)
        var12 = i32_load(38500)
        while True:  # loop $label5
            var0 = var3
            var2 = (var3 << 2)
            var1 = (var8 + i32_load((((var3 << 2) | 4) + 8611904)))
            if (1 if var4 <= (var8 + i32_load((((var3 << 2) | 4) + 8611904))) else 0):
                break
            var2 = (var9 + i32_load((var2 + 8611904)))
            if (1 if var4 <= (var9 + i32_load((var2 + 8611904))) else 0):
                break
            if (1 if (var1 | var2) < 0 else 0):
                break
            var3 = i32_load((((var2 + (((var1 + var7) + 1) * var6)) << 2) + var10) + 4)
            var1 = (var5 + (i32_load((((var2 + (((var1 + var7) + 1) * var6)) << 2) + var10) + 4) * 132))
            if (1 if var12 != i32_load8_u((var5 + (i32_load((((var2 + (((var1 + var7) + 1) * var6)) << 2) + var10) + 4) * 132)) + 122) else 0):
                break
            var1 = i32_load(var1 + 88)
            if (1 if i32_load(var1 + 88) == 0 else 0):
                break
            if (1 if ((var11 - var1) * 25) > 25000 else 0):
                break
            var3 = (var0 + 2)
            if (1 if var0 <= 717 else 0):
                continue
            break  # end loop
        break
    var11 = i32_load(38448)
    var0 = 0
    if (1 if var1 == 1 else 0):
        while True:  # loop $label7
            var1 = var0
            var2 = (var0 << 2)
            var0 = (var8 + i32_load((((var0 << 2) | 4) + 8611904)))
            if (1 if var4 <= (var8 + i32_load((((var0 << 2) | 4) + 8611904))) else 0):
                break
            var2 = (var9 + i32_load((var2 + 8611904)))
            if (1 if var4 <= (var9 + i32_load((var2 + 8611904))) else 0):
                break
            if (1 if (var0 | var2) < 0 else 0):
                break
            var3 = i32_load((((var2 + (((var0 + var7) + 1) * var6)) << 2) + var10) + 4)
            if (1 if var11 == i32_load8_u((var5 + (i32_load((((var2 + (((var0 + var7) + 1) * var6)) << 2) + var10) + 4) * 132)) + 122) else 0):
                break
            var0 = (var1 + 2)
            if (1 if var1 <= 717 else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    var12 = i32_load(38504)
    var13 = i32_load(38508)
    while True:  # loop $label11
        var2 = var0
        var3 = (var0 << 2)
        var0 = (var8 + i32_load((((var0 << 2) | 4) + 8611904)))
        if (1 if var4 <= (var8 + i32_load((((var0 << 2) | 4) + 8611904))) else 0):
            break
        var3 = (var9 + i32_load((var3 + 8611904)))
        if (1 if var4 <= (var9 + i32_load((var3 + 8611904))) else 0):
            break
        if (1 if (var0 | var3) < 0 else 0):
            break
        var3 = i32_load((((var3 + (((var0 + var7) + 1) * var6)) << 2) + var10) + 4)
        # br_table ['$label9', '$label10', '$label8', '$label9', '$label8']
        _br_idx = var1
        break  # br_table
        var0 = i32_load8_u((var5 + (var3 * 132)) + 122)
        if (1 if var13 == i32_load8_u((var5 + (var3 * 132)) + 122) else 0):
            break
        if (1 if var0 != var12 else 0):
            break
        break
        if (1 if var11 == i32_load8_u((var5 + (var3 * 132)) + 122) else 0):
            break
        var0 = (var2 + 2)
        if (1 if var2 <= 717 else 0):
            continue
        break  # end loop
    return 0
    return i32_load((var5 + (var3 * 132)) + 28)


# ==========================================================
# $func233
# ==========================================================
def func233(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var2 = i32_load(9671128)
    var5 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) != 3 else 0):
        return 0
    var4 = i32_load16_u(var5 + 116)
    if (1 if i32_load16_u(var5 + 116) == 0 else 0):
        return 0
    var0 = (i32_load16_u((var2 + (var0 * 132)) + 110) << 2)
    if (1 if i32_load(((i32_load16_u((var2 + (var0 * 132)) + 110) << 2) + i32_load(var1 + 48))) == 0 else 0):
        if (1 if i32_load((i32_load(9142420) + var0)) == 0 else 0):
            break
    var6 = i32_load16_u((var2 + (var4 * 132)) + 110)
    if (1 if i32_load((i32_load(var1 + 64) + (i32_load16_u((var2 + (var4 * 132)) + 110) << 2))) == 0 else 0):
        if (1 if i32_load((i32_load(9142420) + (var6 << 2))) == 0 else 0):
            break
    # br_table ['$label1', '$label2', '$label3']
    _br_idx = i32_load(var1 + 8)
    break  # br_table
    var7 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) == 0 else 0):
        break
    var2 = i32_load((var2 + (var4 * 132)) + 28)
    var1 = i32_load(var1 + 96)
    var0 = 0
    break
    var1 = i32_load(9140300)
    if (1 if i32_load(9140300) == 0 else 0):
        break
    var2 = i32_load((var2 + (var4 * 132)) + 28)
    var0 = 0
    break
    var1 = i32_load(var1 + 36)
    if (1 if i32_load(var1 + 36) <= 3 else 0):
        var2 = (var2 + (var4 * 132))
        var0 = i32_load8_u((var2 + (var4 * 132)) + 122)
        # br_table ['$label6', '$label7', '$label8', '$label9']
        _br_idx = (var1 - 1)
        break  # br_table
        var1 = ((var0 * 404) + 9568096)
        if i32_load(((var0 * 404) + 9568096) + 264):
            return 0
        if (1 if i32_load(var1 + 268) == 1 else 0):
            break
        if (1 if i32_load(((var0 * 404) + 9568096) + 92) == 0 else 0):
            break
        if (1 if i32_load(38456) == var0 else 0):
            break
        if (1 if i32_load(38764) != var0 else 0):
            break
        break
        if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 1 else 0):
            break
        break
        if i32_load(((var0 * 404) + 9568096) + 264):
            break
        var0 = 0
        var2 = i32_load(var2 + 28)
        var1 = i32_load(9140300)
        if (1 if i32_load(9684388) >= 2 else 0):
            if (1 if var1 == 0 else 0):
                var1 = 0
                break
            while True:  # loop $label12
                if (1 if i32_load(((var0 << 2) + 8451904)) == var2 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var1 else 0):
                    continue
                break  # end loop
        if (1 if var1 < 40000 else 0):
            break
        break
    var2 = (var2 + (var4 * 132))
    if (1 if i32_load8_u((var2 + (var4 * 132)) + 122) != (var1 - 4) else 0):
        break
    var0 = 0
    var2 = i32_load(var2 + 28)
    var1 = i32_load(9140300)
    if (1 if i32_load(9684388) >= 2 else 0):
        if (1 if var1 == 0 else 0):
            var1 = 0
            break
        while True:  # loop $label13
            if (1 if i32_load(((var0 << 2) + 8451904)) == var2 else 0):
                break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var1 else 0):
                continue
            break  # end loop
    if (1 if var1 < 40000 else 0):
        break
    break
    while True:  # loop $label14
        if (1 if i32_load((var1 + (var0 << 2))) != var2 else 0):
            var0 = (var0 + 1)
            if (1 if var7 != (var0 + 1) else 0):
                continue
            break
        break  # end loop
    var0 = 0
    var1 = i32_load(9140300)
    if (1 if i32_load(9684388) >= 2 else 0):
        if (1 if var1 == 0 else 0):
            var1 = 0
            break
        while True:  # loop $label15
            if (1 if i32_load(((var0 << 2) + 8451904)) == var2 else 0):
                break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var1 else 0):
                continue
            break  # end loop
    if (1 if var1 < 40000 else 0):
        break
    break
    while True:  # loop $label16
        if (1 if i32_load(((var0 << 2) + 8451904)) != var2 else 0):
            var0 = (var0 + 1)
            if (1 if var1 != (var0 + 1) else 0):
                continue
            break
        break  # end loop
    var0 = 0
    if (1 if i32_load(9684388) > 1 else 0):
        while True:  # loop $label17
            if (1 if i32_load(((var0 << 2) + 8451904)) == var2 else 0):
                break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var1 else 0):
                continue
            break  # end loop
    if (1 if var1 > 39999 else 0):
        break
    i32_store(9140300, (var1 + 1))
    i32_store(((var1 << 2) + 8451904), var2)
    i32_store16(var5 + 116, 0)
    i32_store((i32_load(9142420) + (var6 << 2)), 2)
    var3 = 1
    return var3


# ==========================================================
# $func234
# ==========================================================
def func234(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var7 = (var0 - 16)
    if i32_load((var0 - 16)):
        while True:  # loop $label28
            var2 = (var0 + (var5 * 60))
            i32_store(9681920, (i32_load(9681920) + ((i32_load((var0 + (var5 * 60))) * i32_load(var2 + 4)) << 2)))
            var3 = i32_load(var2 + 28)
            var6 = i32_load(var2 + 32)
            # br_table ['$label0', '$label1', '$label0', '$label1', '$label1', '$label2', '$label1']
            _br_idx = (i32_load(var2 + 32) - 23)
            break  # br_table
            var4 = i32_load(9140324)
            i32_store(9140324, (i32_load(9140324) + 1))
            break
            var4 = i32_load(9140328)
            i32_store(9140328, (i32_load(9140328) + 1))
            i32_store(((var4 << 2) + 9140336), var2)
            if (1 if var3 <= 9999 else 0):
                # br_table ['$label4', '$label5', '$label6', '$label7', '$label8', '$label9', '$label10', '$label11', '$label12', '$label13', '$label14', '$label15', '$label16', '$label17', '$label18', '$label19', '$label20', '$label21', '$label22', '$label23', '$label24', '$label25', '$label26', '$label27']
                _br_idx = var6
                break  # br_table
                i32_store(((var3 * 72) + 9263856) + 4, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 8, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 28, var2)
                break
                i32_store(((var3 * 72) + 9263856), var2)
                break
                i32_store(((var3 * 72) + 9263856) + 4, var2)
                break
                var4 = ((var3 * 404) + 9568096)
                var6 = i32_load(var4 + 20)
                i32_store(((var3 * 404) + 9568096) + 20, (i32_load(var4 + 20) + 1))
                i32_store((var4 + (var6 << 2)), var2)
                break
                var4 = ((var3 * 404) + 9568096)
                var6 = i32_load(var4 + 20)
                i32_store(((var3 * 404) + 9568096) + 20, (i32_load(var4 + 20) + 1))
                i32_store((var4 + (var6 << 2)), var2)
                break
                i32_store(((var3 * 72) + 9263856) + 40, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 44, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 32, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 36, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 52, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 20, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 60, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 48, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 68, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 12, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 56, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 64, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 68, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 16, var2)
                break
                i32_store(((var3 * 72) + 9263856) + 24, var2)
                break
                var4 = ((var3 * 404) + 9568096)
                var6 = i32_load(var4 + 20)
                i32_store(((var3 * 404) + 9568096) + 20, (i32_load(var4 + 20) + 1))
                i32_store((var4 + (var6 << 2)), var2)
                break
            if (1 if var3 > 19999 else 0):
                break
            var3 = (var3 - 10000)
            if (1 if (var3 - 10000) > 95 else 0):
                break
            i32_store(((var3 << 2) + 9142448), var2)
            i32_store(var2 + 28, 2147483647)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) < i32_load(var7) else 0):
                continue
            break  # end loop
    if var1:
        var0 = 0
        while True:  # loop $label30
            var1 = ((var0 * 72) + 9263856)
            if (1 if i32_load(((var0 * 72) + 9263856)) == 0 else 0):
                i32_store(var1, i32_load(var1 + 4))
            var4 = i32_load(var1 + 8)
            if (1 if i32_load(var1 + 8) == 0 else 0):
                if i32_load(((var0 * 404) + 9568096) + 264):
                    break
                var4 = i32_load(var1 + 12)
                i32_store(var1 + 8, i32_load(var1 + 12))
                if (1 if var4 == 0 else 0):
                    break
            var1 = i32_load(((var0 * 404) + 9568096) + 276)
            if (1 if i32_load(((var0 * 404) + 9568096) + 276) == 0 else 0):
                break
            if (1 if i32_load(var4 + 24) > 99 else 0):
                break
            i32_store(var4 + 24, (((i32_load(var4 + 16) * 1000) & 0xFFFFFFFF) // var1))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != 255 else 0):
                continue
            break  # end loop
        break
    var2 = ((var3 * 404) + 9568096)
    var1 = ((var3 * 72) + 9263856)
    var0 = 0
    while True:  # loop $label33
        if (1 if var0 != var3 else 0):
            break
        if (1 if i32_load(var1) == 0 else 0):
            i32_store(var1, i32_load(var1 + 4))
        var5 = i32_load(var1 + 8)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            if i32_load(var2 + 264):
                break
            var5 = i32_load(var1 + 12)
            i32_store(var1 + 8, i32_load(var1 + 12))
            if (1 if var5 == 0 else 0):
                break
        var4 = i32_load(var2 + 276)
        if (1 if i32_load(var2 + 276) == 0 else 0):
            break
        if (1 if i32_load(var5 + 24) > 99 else 0):
            break
        i32_store(var5 + 24, (((i32_load(var5 + 16) * 1000) & 0xFFFFFFFF) // var4))
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != 255 else 0):
            continue
        break  # end loop
    return var3

