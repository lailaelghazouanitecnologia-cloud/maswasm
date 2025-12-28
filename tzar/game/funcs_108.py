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
# $md
# Export: md
# ==========================================================
def md(var0):
    """Export: md"""
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
    var2 = i32_load(9142440)
    var1 = (i32_load(9142440) * var2)
    # br_table ['$label0', '$label1', '$label2', '$label3', '$label4', '$label5', '$label6', '$label7', '$label8']
    _br_idx = ((var0 - 1) if var0 else i32_load(i32_load(9142424) + 28))
    break  # br_table
    if (1 if var1 == 0 else 0):
        break
    var2 = 0
    var0 = 0
    if (1 if (var1 - 1) >= 3 else 0):
        var4 = (var1 & -4)
        while True:  # loop $label10
            i32_store8((i32_load(9147288) + var0), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 1)), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 2)), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 3)), i32_load(9147292))
            var0 = (var0 + 4)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var4 else 0):
                continue
            break  # end loop
    var1 = (var1 & 3)
    if (1 if (var1 & 3) == 0 else 0):
        break
    while True:  # loop $label11
        i32_store8((i32_load(9147288) + var0), i32_load(9147292))
        var0 = (var0 + 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var1 else 0):
            continue
        break  # end loop
    var2 = 0
    if i32_load(9147300):
        while True:  # loop $label12
            var0 = i32_load(9684504)
            var1 = (var2 << 2)
            var2 = (var2 + 8)
            if (1 if (var2 + 8) < i32_load(9147300) else 0):
                continue
            break  # end loop
    break
    if (1 if var1 == 0 else 0):
        break
    var2 = 0
    var0 = 0
    if (1 if (var1 - 1) >= 3 else 0):
        var4 = (var1 & -4)
        while True:  # loop $label14
            i32_store8((i32_load(9147288) + var0), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 1)), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 2)), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 3)), i32_load(9147292))
            var0 = (var0 + 4)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var4 else 0):
                continue
            break  # end loop
    var1 = (var1 & 3)
    if (1 if (var1 & 3) == 0 else 0):
        break
    while True:  # loop $label15
        i32_store8((i32_load(9147288) + var0), i32_load(9147292))
        var0 = (var0 + 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var1 else 0):
            continue
        break  # end loop
    var2 = 0
    if i32_load(9147300):
        while True:  # loop $label16
            var0 = i32_load(9684504)
            var1 = (var2 << 2)
            var2 = (var2 + 8)
            if (1 if (var2 + 8) < i32_load(9147300) else 0):
                continue
            break  # end loop
    break
    if (1 if var1 == 0 else 0):
        break
    var2 = 0
    var0 = 0
    if (1 if (var1 - 1) >= 3 else 0):
        var4 = (var1 & -4)
        while True:  # loop $label18
            i32_store8((i32_load(9147288) + var0), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 1)), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 2)), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 3)), i32_load(9147292))
            var0 = (var0 + 4)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var4 else 0):
                continue
            break  # end loop
    var1 = (var1 & 3)
    if (1 if (var1 & 3) == 0 else 0):
        break
    while True:  # loop $label19
        i32_store8((i32_load(9147288) + var0), i32_load(9147292))
        var0 = (var0 + 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var1 else 0):
            continue
        break  # end loop
    var2 = 0
    if i32_load(9147300):
        while True:  # loop $label20
            var0 = i32_load(9684504)
            var1 = (var2 << 2)
            var2 = (var2 + 8)
            if (1 if (var2 + 8) < i32_load(9147300) else 0):
                continue
            break  # end loop
    break
    if (1 if var1 == 0 else 0):
        break
    var2 = 0
    var0 = 0
    if (1 if (var1 - 1) >= 3 else 0):
        var4 = (var1 & -4)
        while True:  # loop $label22
            i32_store8((i32_load(9147288) + var0), i32_load(9147296))
            i32_store8((i32_load(9147288) + (var0 | 1)), i32_load(9147296))
            i32_store8((i32_load(9147288) + (var0 | 2)), i32_load(9147296))
            i32_store8((i32_load(9147288) + (var0 | 3)), i32_load(9147296))
            var0 = (var0 + 4)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var4 else 0):
                continue
            break  # end loop
    var1 = (var1 & 3)
    if (1 if (var1 & 3) == 0 else 0):
        break
    while True:  # loop $label23
        i32_store8((i32_load(9147288) + var0), i32_load(9147296))
        var0 = (var0 + 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var1 else 0):
            continue
        break  # end loop
    var2 = 0
    if (1 if i32_load(9147300) == 0 else 0):
        break
    while True:  # loop $label24
        var0 = i32_load(9684504)
        var1 = (var2 << 2)
        var2 = (var2 + 8)
        if (1 if (var2 + 8) < i32_load(9147300) else 0):
            continue
        break  # end loop
    break
    if (1 if var1 == 0 else 0):
        break
    var2 = 0
    var0 = 0
    if (1 if (var1 - 1) >= 3 else 0):
        var4 = (var1 & -4)
        while True:  # loop $label26
            i32_store8((i32_load(9147288) + var0), i32_load(9147296))
            i32_store8((i32_load(9147288) + (var0 | 1)), i32_load(9147296))
            i32_store8((i32_load(9147288) + (var0 | 2)), i32_load(9147296))
            i32_store8((i32_load(9147288) + (var0 | 3)), i32_load(9147296))
            var0 = (var0 + 4)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var4 else 0):
                continue
            break  # end loop
    var1 = (var1 & 3)
    if (1 if (var1 & 3) == 0 else 0):
        break
    while True:  # loop $label27
        i32_store8((i32_load(9147288) + var0), i32_load(9147296))
        var0 = (var0 + 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var1 else 0):
            continue
        break  # end loop
    var2 = 0
    if i32_load(9147300):
        while True:  # loop $label28
            var0 = i32_load(9684504)
            var1 = (var2 << 2)
            var2 = (var2 + 8)
            if (1 if (var2 + 8) < i32_load(9147300) else 0):
                continue
            break  # end loop
    break
    if (1 if var1 == 0 else 0):
        break
    var2 = 0
    var0 = 0
    if (1 if (var1 - 1) >= 3 else 0):
        var4 = (var1 & -4)
        while True:  # loop $label30
            i32_store8((i32_load(9147288) + var0), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 1)), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 2)), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 3)), i32_load(9147292))
            var0 = (var0 + 4)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var4 else 0):
                continue
            break  # end loop
    var1 = (var1 & 3)
    if (1 if (var1 & 3) == 0 else 0):
        break
    while True:  # loop $label31
        i32_store8((i32_load(9147288) + var0), i32_load(9147292))
        var0 = (var0 + 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var1 else 0):
            continue
        break  # end loop
    var2 = 0
    if i32_load(9147300):
        while True:  # loop $label32
            var0 = i32_load(9684504)
            var1 = (var2 << 2)
            var2 = (var2 + 8)
            if (1 if (var2 + 8) < i32_load(9147300) else 0):
                continue
            break  # end loop
    break
    if (1 if var1 == 0 else 0):
        break
    var2 = 0
    var0 = 0
    if (1 if (var1 - 1) >= 3 else 0):
        var4 = (var1 & -4)
        while True:  # loop $label34
            i32_store8((i32_load(9147288) + var0), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 1)), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 2)), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 3)), i32_load(9147292))
            var0 = (var0 + 4)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var4 else 0):
                continue
            break  # end loop
    var1 = (var1 & 3)
    if (1 if (var1 & 3) == 0 else 0):
        break
    while True:  # loop $label35
        i32_store8((i32_load(9147288) + var0), i32_load(9147292))
        var0 = (var0 + 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var1 else 0):
            continue
        break  # end loop
    var2 = 0
    if i32_load(9147300):
        while True:  # loop $label36
            var0 = i32_load(9684504)
            var1 = (var2 << 2)
            var2 = (var2 + 8)
            if (1 if (var2 + 8) < i32_load(9147300) else 0):
                continue
            break  # end loop
    break
    if (1 if var1 == 0 else 0):
        break
    var2 = 0
    var0 = 0
    if (1 if (var1 - 1) >= 3 else 0):
        var4 = (var1 & -4)
        while True:  # loop $label38
            i32_store8((i32_load(9147288) + var0), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 1)), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 2)), i32_load(9147292))
            i32_store8((i32_load(9147288) + (var0 | 3)), i32_load(9147292))
            var0 = (var0 + 4)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var4 else 0):
                continue
            break  # end loop
    var1 = (var1 & 3)
    if (1 if (var1 & 3) == 0 else 0):
        break
    while True:  # loop $label39
        i32_store8((i32_load(9147288) + var0), i32_load(9147292))
        var0 = (var0 + 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var1 else 0):
            continue
        break  # end loop
    var2 = 0
    if (1 if i32_load(9147300) == 0 else 0):
        break
    while True:  # loop $label40
        var0 = i32_load(9684504)
        var1 = (var2 << 2)
        var2 = (var2 + 8)
        if (1 if (var2 + 8) < i32_load(9147300) else 0):
            continue
        break  # end loop
    if (1 if i32_load(i32_load(9142424) + 64) == 0 else 0):
        break
    var1 = i32_load(9142440)
    if (1 if i32_load(9142440) <= 0 else 0):
        break
    var8 = (var1 & -2)
    var9 = (var1 & 1)
    var3 = ((var1 & 0xFFFFFFFF) >> 1)
    var0 = (((var1 & 0xFFFFFFFF) >> 1) - 20)
    var4 = ((((var1 & 0xFFFFFFFF) >> 1) - 20) * var0)
    var2 = 0
    while True:  # loop $label44
        var0 = (var2 - var3)
        var6 = (((var2 - var3) * var0) - 1)
        var0 = 0
        var5 = 0
        if (1 if var1 != 1 else 0):
            while True:  # loop $label42
                var7 = (var0 - var3)
                if (1 if var4 < (var6 + ((var0 - var3) * var7)) else 0):
                    i32_store8((i32_load(9147288) + ((i32_load(9142440) * var0) + var2)), i32_load(9147296))
                var7 = (var0 | 1)
                var10 = ((var0 | 1) - var3)
                if (1 if var4 < (var6 + (((var0 | 1) - var3) * var10)) else 0):
                    i32_store8((i32_load(9147288) + ((i32_load(9142440) * var7) + var2)), i32_load(9147296))
                var0 = (var0 + 2)
                var5 = (var5 + 2)
                if (1 if (var5 + 2) != var8 else 0):
                    continue
                break  # end loop
        if (1 if var9 == 0 else 0):
            break
        var5 = (var0 - var3)
        if (1 if (var6 + ((var0 - var3) * var5)) <= var4 else 0):
            break
        i32_store8((i32_load(9147288) + ((i32_load(9142440) * var0) + var2)), i32_load(9147296))
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var1 else 0):
            continue
        break  # end loop
    return i32_load(9147288)

