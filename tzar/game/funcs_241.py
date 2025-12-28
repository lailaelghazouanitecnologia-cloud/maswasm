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
# $de
# Export: de
# ==========================================================
def de(var0, var1):
    """Export: de"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    # br_table ['$label0', '$label1', '$label2', '$label3', '$label4']
    _br_idx = var1
    break  # br_table
    var2 = i32_load(9671136)
    if (1 if i32_load(9671136) < 4 else 0):
        break
    var1 = 3
    var3 = i32_load(9671128)
    if (1 if var0 > 3 else 0):
        break
    var6 = (var0 - 1)
    while True:  # loop $label11
        var4 = (var3 + (var1 * 132))
        if (1 if i32_load(((i32_load16_u((var3 + (var1 * 132)) + 110) << 2) + 9151488)) == 0 else 0):
            break
        if (1 if i32_load8_u(var4 + 125) == 3 else 0):
            break
        var0 = i32_load8_u(var4 + 122)
        # br_table ['$label7', '$label8', '$label9', '$label10']
        _br_idx = var6
        break  # br_table
        if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 1 else 0):
            break
        break
        if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 0 else 0):
            break
        break
        var5 = ((var0 * 404) + 9568096)
        if i32_load(((var0 * 404) + 9568096) + 264):
            break
        if (1 if i32_load(var5 + 268) == 1 else 0):
            break
        if (1 if i32_load(var5 + 92) == 0 else 0):
            break
        if (1 if i32_load(38456) == var0 else 0):
            break
        if (1 if i32_load(38764) == var0 else 0):
            break
        func256(var4, i32_load(9151484))
        var2 = i32_load(9671136)
        var3 = i32_load(9671128)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < var2 else 0):
            continue
        break  # end loop
    break
    var2 = i32_load(9671136)
    if (1 if i32_load(9671136) < 4 else 0):
        break
    var1 = 3
    var3 = i32_load(9671128)
    if (1 if var0 > 3 else 0):
        break
    var6 = (var0 - 1)
    while True:  # loop $label18
        var4 = (var3 + (var1 * 132))
        if (1 if i32_load(((i32_load16_u((var3 + (var1 * 132)) + 110) << 2) + 9151488)) == 0 else 0):
            break
        if (1 if i32_load8_u(var4 + 125) == 3 else 0):
            break
        var0 = i32_load8_u(var4 + 122)
        # br_table ['$label14', '$label15', '$label16', '$label17']
        _br_idx = var6
        break  # br_table
        if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 1 else 0):
            break
        break
        if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 0 else 0):
            break
        break
        var5 = ((var0 * 404) + 9568096)
        if i32_load(((var0 * 404) + 9568096) + 264):
            break
        if (1 if i32_load(var5 + 268) == 1 else 0):
            break
        if (1 if i32_load(var5 + 92) == 0 else 0):
            break
        if (1 if i32_load(38456) == var0 else 0):
            break
        if (1 if i32_load(38764) == var0 else 0):
            break
        var2 = i32_load(9671136)
        var3 = i32_load(9671128)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < var2 else 0):
            continue
        break  # end loop
    break
    if (1 if i32_load(9671136) < 4 else 0):
        break
    var5 = (var0 - 4)
    var6 = (var0 - 1)
    var1 = 3
    while True:  # loop $label24
        var3 = (i32_load(9671128) + (var1 * 132))
        if (1 if i32_load(((i32_load16_u((i32_load(9671128) + (var1 * 132)) + 110) << 2) + 9151488)) == 0 else 0):
            break
        if (1 if i32_load8_u(var3 + 125) == 3 else 0):
            break
        var2 = i32_load8_u(var3 + 122)
        if (1 if var0 <= 3 else 0):
            # br_table ['$label20', '$label21', '$label22', '$label23']
            _br_idx = var6
            break  # br_table
            var4 = ((var2 * 404) + 9568096)
            if i32_load(((var2 * 404) + 9568096) + 264):
                break
            if (1 if i32_load(var4 + 268) == 1 else 0):
                break
            if (1 if i32_load(var4 + 92) == 0 else 0):
                break
            if (1 if i32_load(38456) == var2 else 0):
                break
            if (1 if i32_load(38764) != var2 else 0):
                break
            break
            if (1 if i32_load(((var2 * 404) + 9568096) + 264) == 1 else 0):
                break
            break
            if (1 if i32_load(((var2 * 404) + 9568096) + 264) == 0 else 0):
                break
            break
        if (1 if var2 != var5 else 0):
            break
        func368(i32_load(var3 + 28))
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < i32_load(9671136) else 0):
            continue
        break  # end loop
    break
    var4 = (var0 - 4)
    while True:  # loop $label26
        var0 = (var3 + (var1 * 132))
        if (1 if i32_load(((i32_load16_u((var3 + (var1 * 132)) + 110) << 2) + 9151488)) == 0 else 0):
            break
        if (1 if i32_load8_u(var0 + 125) == 3 else 0):
            break
        if (1 if var4 != i32_load8_u(var0 + 122) else 0):
            break
        var2 = i32_load(9671136)
        var3 = i32_load(9671128)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < var2 else 0):
            continue
        break  # end loop
    break
    var4 = (var0 - 4)
    while True:  # loop $label28
        var0 = (var3 + (var1 * 132))
        if (1 if i32_load(((i32_load16_u((var3 + (var1 * 132)) + 110) << 2) + 9151488)) == 0 else 0):
            break
        if (1 if i32_load8_u(var0 + 125) == 3 else 0):
            break
        if (1 if var4 != i32_load8_u(var0 + 122) else 0):
            break
        func256(var0, i32_load(9151484))
        var2 = i32_load(9671136)
        var3 = i32_load(9671128)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < var2 else 0):
            continue
        break  # end loop
    return
    i32_store(9143000, 0)
    var1 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var1 * 132)))
        i32_store(9213820, 0)
    func45()
    if (1 if i32_load(9671136) >= 4 else 0):
        var5 = (var0 - 4)
        var6 = (var0 - 1)
        var1 = 3
        while True:  # loop $label34
            var3 = (i32_load(9671128) + (var1 * 132))
            if (1 if i32_load(((i32_load16_u((i32_load(9671128) + (var1 * 132)) + 110) << 2) + 9151488)) == 0 else 0):
                break
            if (1 if i32_load8_u(var3 + 125) == 3 else 0):
                break
            var2 = i32_load8_u(var3 + 122)
            if (1 if var0 <= 3 else 0):
                # br_table ['$label30', '$label31', '$label32', '$label33']
                _br_idx = var6
                break  # br_table
                var4 = ((var2 * 404) + 9568096)
                if i32_load(((var2 * 404) + 9568096) + 264):
                    break
                if (1 if i32_load(var4 + 268) == 1 else 0):
                    break
                if (1 if i32_load(var4 + 92) == 0 else 0):
                    break
                if (1 if i32_load(38456) == var2 else 0):
                    break
                if (1 if i32_load(38764) != var2 else 0):
                    break
                break
                if (1 if i32_load(((var2 * 404) + 9568096) + 264) == 1 else 0):
                    break
                break
                if (1 if i32_load(((var2 * 404) + 9568096) + 264) == 0 else 0):
                    break
                break
            if (1 if var2 != var5 else 0):
                break
            func44(var3, 0)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < i32_load(9671136) else 0):
                continue
            break  # end loop

