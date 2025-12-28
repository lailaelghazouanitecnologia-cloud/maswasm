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
# $func397
# ==========================================================
def func397(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if (1 if var2 == 0 else 0):
        break
    var3 = i32_load(59176)
    while True:  # loop $label1
        var4 = ((var5 << 2) + var1)
        if (1 if i32_load(((var5 << 2) + var1) + 4) > var3 else 0):
            break
        var5 = (i32_load(var4 + 8) + var5)
        if (1 if (i32_load(var4 + 8) + var5) < var2 else 0):
            continue
        break  # end loop
    if (1 if var2 > var5 else 0):
        while True:  # loop $label3
            var7 = i32_load((var1 + (var5 << 2)))
            var3 = i32_load(9561704)
            if (1 if i32_load(9561704) != i32_load(9561700) else 0):
                var4 = i32_load(9561696)
                break
            var4 = (i32_load(9561708) + var3)
            i32_store(9561700, (i32_load(9561708) + var3))
            var6 = i32_load(9561696)
            var4 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
            if var3:
                # Unknown: memory.copy []
            if var6:
                var3 = i32_load(9561704)
            i32_store(9561696, var4)
            i32_store(9561704, (var3 + 1))
            i32_store((var4 + (var3 << 2)), var7)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var2 else 0):
                continue
            break  # end loop
    if (1 if var0 > i32_load(59160) else 0):
        i32_store(59160, var0)
    if (1 if var0 > i32_load(59176) else 0):
        i32_store(59176, var0)


# ==========================================================
# $func398
# ==========================================================
def func398(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    if (1 if i32_load8_u(9142917) == 0 else 0):
        var5 = (var0 + 2147483647)
        var4 = ((i32_load(9142848) * 25) + 150)
        var1 = i32_load(9299864)
        if i32_load(9299864):
            var0 = 0
            var3 = i32_load(9299856)
            while True:  # loop $label1
                var2 = (var3 + (var0 << 2))
                if (1 if i32_load((var3 + (var0 << 2))) == 0 else 0):
                    break
                var0 = (var0 + 2)
                if (1 if (var0 + 2) < var1 else 0):
                    continue
                break  # end loop
        if (1 if i32_load(9299860) != var1 else 0):
            var2 = i32_load(9299856)
            break
        var0 = (i32_load(9299868) + var1)
        i32_store(9299860, (i32_load(9299868) + var1))
        var3 = i32_load(9299856)
        var2 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var1:
            # Unknown: memory.copy []
        if var3:
            var1 = i32_load(9299864)
        i32_store(9299856, var2)
        i32_store(9299864, (var1 + 1))
        i32_store((var2 + (var1 << 2)), var4)
        var0 = i32_load(9299864)
        if (1 if i32_load(9299864) != i32_load(9299860) else 0):
            var1 = var2
            break
        var1 = (i32_load(9299868) + var0)
        i32_store(9299860, (i32_load(9299868) + var0))
        var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        if var0:
            # Unknown: memory.copy []
        i32_store(9299856, var1)
        var0 = i32_load(9299864)
        i32_store(9299864, (var0 + 1))
        break
        i32_store(var2, var4)
        i32_store((var3 + ((var0 << 2) | 4)), var5)
    return (var1 + (var0 << 2))


# ==========================================================
# $func432
# ==========================================================
def func432(var0, param1, param2, param3):
    var1 = 0
    var1 = i32_load(var0)
    if (1 if i32_load(var0) <= 201326591 else 0):
        if (1 if var1 <= 100663327 else 0):
            if (1 if var1 <= 67108863 else 0):
                # br_table ['$label0', '$label1', '$label2', '$label3']
                _br_idx = (var1 - 33554432)
                break  # br_table
                if (1 if var1 == -2129657856 else 0):
                    break
                if var1:
                    break
                # call_indirect via table[i32_load(var0 + 4)]
                break
            # br_table ['$label5', '$label1', '$label6', '$label7']
            _br_idx = (var1 - 67108872)
            break  # br_table
            if (1 if var1 == 67108864 else 0):
                break
            if (1 if var1 != 100663296 else 0):
                break
            # call_indirect via table[i32_load(var0 + 4)]
            break
        if (1 if var1 <= 134217759 else 0):
            # br_table ['$label9', '$label1', '$label10', '$label11']
            _br_idx = (var1 - 100663336)
            break  # br_table
            if (1 if var1 == 100663328 else 0):
                break
            if (1 if var1 != 134217728 else 0):
                break
            # call_indirect via table[i32_load(var0 + 4)]
            break
        if (1 if var1 <= 167772159 else 0):
            # br_table ['$label13', '$label1', '$label14', '$label15']
            _br_idx = (var1 - 134217896)
            break  # br_table
        if (1 if var1 == 167772160 else 0):
            break
        if (1 if var1 != 167772840 else 0):
            break
        # call_indirect via table[i32_load(var0 + 4)]
        break
    if (1 if var1 <= 603979775 else 0):
        if (1 if var1 <= 335544319 else 0):
            if (1 if var1 <= 268435455 else 0):
                if (1 if var1 == 201326592 else 0):
                    break
                if (1 if var1 != 234881024 else 0):
                    break
                # call_indirect via table[i32_load(var0 + 4)]
                break
            if (1 if var1 == 268435456 else 0):
                break
            if (1 if var1 != 301989888 else 0):
                break
            # call_indirect via table[i32_load(var0 + 4)]
            break
        if (1 if var1 <= 536870911 else 0):
            if (1 if var1 == 335544320 else 0):
                break
            if (1 if var1 != 369098752 else 0):
                break
            # call_indirect via table[i32_load(var0 + 4)]
            break
        if (1 if var1 == 536870912 else 0):
            break
        if (1 if var1 != 570425344 else 0):
            break
        # call_indirect via table[i32_load(var0 + 4)]
        i32_store(i32_load(var0 + 16) + 176, call_indirect(i32_load(var0 + 4)))
        break
    if (1 if var1 <= 704643071 else 0):
        if (1 if var1 <= 654311423 else 0):
            if (1 if var1 == 603979776 else 0):
                break
            if (1 if var1 != 637534208 else 0):
                break
            # call_indirect via table[i32_load(var0 + 4)]
            i32_store(i32_load(var0 + 32) + 176, call_indirect(i32_load(var0 + 4)))
            break
        if (1 if var1 == 654311424 else 0):
            break
        if (1 if var1 != 671088640 else 0):
            break
        # call_indirect via table[i32_load(var0 + 4)]
        i32_store(i32_load(var0 + 40) + 176, call_indirect(i32_load(var0 + 4)))
        break
    if (1 if var1 <= 771751935 else 0):
        if (1 if var1 == 704643072 else 0):
            break
        if (1 if var1 != 738197504 else 0):
            break
        # call_indirect via table[i32_load(var0 + 4)]
        i32_store(i32_load(var0 + 56) + 176, call_indirect(i32_load(var0 + 4)))
        break
    if (1 if var1 == 771751936 else 0):
        break
    if (1 if var1 == 805306368 else 0):
        break
    if (1 if var1 != 838860800 else 0):
        break
    # call_indirect via table[i32_load(var0 + 4)]
    i32_store(i32_load(var0 + 80) + 176, call_indirect(i32_load(var0 + 4)))
    break
    i32_store(i32_load(var0 + 32) + 176, a_t())
    break
    f64_store((var0 + 24) + 176, a_o())
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    if (1 if var1 != 134217760 else 0):
        break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    break
    # call_indirect via table[i32_load(var0 + 4)]
    i32_store(var0 + 176, call_indirect(i32_load(var0 + 4)))
    break
    # call_indirect via table[i32_load(var0 + 4)]
    i32_store(i32_load(var0 + 24) + 176, call_indirect(i32_load(var0 + 4)))
    break
    # call_indirect via table[i32_load(var0 + 4)]
    i32_store(i32_load(var0 + 48) + 176, call_indirect(i32_load(var0 + 4)))
    break
    # call_indirect via table[i32_load(var0 + 4)]
    i32_store(i32_load((var0 - -64)) + 176, call_indirect(i32_load(var0 + 4)))
    break
    # call_indirect via table[i32_load(var0 + 4)]
    i32_store(i32_load(var0 + 72) + 176, call_indirect(i32_load(var0 + 4)))
    if i32_load(var0 + 188):
        if var0:
        return af(var0)
    i32_atomic_store(var0 + 8, 1)
    func111((var0 + 8), 2147483647)
    return af(i32_load(var0 + 184))


# ==========================================================
# $func457
# ==========================================================
def func457(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var9 = (global0 - 1024)
    global global0
    global0 = (global0 - 1024)
    var6 = func276(0, var1, var2, var3, 0)
    if (1 if var3 < 2329 else 0):
        if (1 if var0 == 0 else 0):
            break
        if (1 if var6 == 0 else 0):
            break
        var4 = i32_load(var0 + 16)
        var7 = i32_load(i32_load(var0 + 16) + 4)
        var8 = i32_load(var4 + 12)
        if (1 if (i32_load(i32_load(var0 + 16) + 4) + (var6 << 2)) >= (i32_load(var4) + (i32_load(var4 + 12) << 2)) else 0):
            var4 = 0
            var5 = func58(1, 16)
            if (1 if func58(1, 16) == 0 else 0):
                break
            var8 = (var6 if (1 if var6 > var8 else 0) else var8)
            var7 = func58(i64_extend_s((var6 if (1 if var6 > var8 else 0) else var8)), 4)
            if (1 if func58(i64_extend_s((var6 if (1 if var6 > var8 else 0) else var8)), 4) == 0 else 0):
                break
            i32_store(var5 + 8, 0)
            i32_store(var5 + 4, var7)
            i32_store(var5, var7)
            i32_store(var5 + 12, var8)
            i32_store(i32_load(var0 + 16) + 8, var5)
            i32_store(var0 + 16, var5)
        if (1 if var3 <= 512 else 0):
            break
        var4 = func58(i64_extend_u(var3), 2)
        if (1 if func58(i64_extend_u(var3), 2) == 0 else 0):
            var4 = 0
            break
        var4 = var6
        global global0
        global0 = (var9 + 1024)
        return var4
    a_c()
    raise RuntimeError('unreachable')
    return 4778

