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
# $func777
# ==========================================================
def func777(var0, var1):
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
    var9 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var3 = i32_load(9671128)
    var0 = (i32_load(9671128) + (var0 * 132))
    var7 = ((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110) * 286704)) + 281776)
    var10 = ((var1 & 65535) + 1)
    var11 = (((var1 & 0xFFFFFFFF) >> 16) + 1)
    var5 = i32_load((i32_load(9142840) + ((((var1 & 65535) + 1) + ((((var1 & 0xFFFFFFFF) >> 16) + 1) * (i32_load(9142440) + 2))) << 2)))
    if (1 if i32_load((i32_load(9142840) + ((((var1 & 65535) + 1) + ((((var1 & 0xFFFFFFFF) >> 16) + 1) * (i32_load(9142440) + 2))) << 2))) < 3 else 0):
        break
    var1 = (var3 + (var5 * 132))
    var2 = i32_load(((i32_load8_u((var3 + (var5 * 132)) + 122) * 404) + 9568096) + 292)
    if (1 if i32_load(((i32_load8_u((var3 + (var5 * 132)) + 122) * 404) + 9568096) + 292) == 0 else 0):
        break
    var8 = i32_load8_u(var1 + 125)
    if (1 if i32_load8_u(var1 + 125) == 10 else 0):
        break
    var2 = (var2 * 96)
    var4 = (1 if (1 if var2 < 100 else 0) else (((var2 * 96) & 0xFFFFFFFF) // 100))
    var12 = (var3 + (var5 * 132))
    var6 = i32_load((var3 + (var5 * 132)) + 64)
    var2 = ((1 if (1 if var2 < 100 else 0) else (((var2 * 96) & 0xFFFFFFFF) // 100)) if (1 if var4 < var6 else 0) else i32_load((var3 + (var5 * 132)) + 64))
    if (1 if var8 == 3 else 0):
        break
    var8 = (var12 - -64)
    if (1 if var4 < var6 else 0):
        i32_store(var8, (var6 - var2))
        if (1 if i32_load((var3 + (var5 * 132)) + 92) == 0 else 0):
            break
        if i32_load8_u(9147141):
            break
        i32_store(var9 + 32, var2)
        a_b()
        break
    i32_store(var8, 0)
    func155(var0, var1, 0)
    func103(var1)
    i32_store(var7, (i32_load(var7) + var2))
    var3 = i32_load16_u(var12 + 110)
    var5 = i32_load(9561692)
    var6 = i32_load16_u(var0 + 110)
    var4 = i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 278556)
    if i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 278556):
        var4 = (var4 + ((i32_load8_u(var0 + 122) + (var3 * 255)) << 2))
        i32_store((var4 + ((i32_load8_u(var0 + 122) + (var3 * 255)) << 2)), (i32_load(var4) + var2))
    var3 = i32_load(((var5 + (var3 * 286704)) + 278564))
    if (1 if i32_load(((var5 + (var3 * 286704)) + 278564)) == 0 else 0):
        break
    var1 = (var3 + ((i32_load8_u(var1 + 122) + (var6 * 255)) << 2))
    i32_store((var3 + ((i32_load8_u(var1 + 122) + (var6 * 255)) << 2)), (i32_load(var1) + var2))
    var1 = (i32_load(9142440) + 2)
    var3 = i32_load((i32_load(9142840) + ((var10 + ((var11 + (i32_load(9142440) + 2)) * var1)) << 2)))
    if (1 if i32_load((i32_load(9142840) + ((var10 + ((var11 + (i32_load(9142440) + 2)) * var1)) << 2))) < 3 else 0):
        break
    var6 = i32_load(9671128)
    var1 = (i32_load(9671128) + (var3 * 132))
    var2 = i32_load(((i32_load8_u((i32_load(9671128) + (var3 * 132)) + 122) * 404) + 9568096) + 292)
    if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var3 * 132)) + 122) * 404) + 9568096) + 292) == 0 else 0):
        break
    var8 = i32_load8_u(var1 + 125)
    if (1 if i32_load8_u(var1 + 125) == 10 else 0):
        break
    var2 = (var2 * 96)
    var4 = (1 if (1 if var2 < 100 else 0) else (((var2 * 96) & 0xFFFFFFFF) // 100))
    var12 = (var6 + (var3 * 132))
    var5 = i32_load((var6 + (var3 * 132)) + 64)
    var2 = ((1 if (1 if var2 < 100 else 0) else (((var2 * 96) & 0xFFFFFFFF) // 100)) if (1 if var4 < var5 else 0) else i32_load((var6 + (var3 * 132)) + 64))
    if (1 if var8 == 3 else 0):
        break
    var8 = (var12 - -64)
    if (1 if var4 >= var5 else 0):
        i32_store(var8, 0)
        func155(var0, var1, 0)
        break
    i32_store(var8, (var5 - var2))
    if (1 if i32_load((var6 + (var3 * 132)) + 92) == 0 else 0):
        break
    if i32_load8_u(9147141):
        break
    i32_store(var9 + 16, var2)
    a_b()
    func103(var1)
    i32_store(var7, (i32_load(var7) + var2))
    var3 = i32_load16_u(var12 + 110)
    var5 = i32_load(9561692)
    var6 = i32_load16_u(var0 + 110)
    var4 = i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 278556)
    if i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 278556):
        var4 = (var4 + ((i32_load8_u(var0 + 122) + (var3 * 255)) << 2))
        i32_store((var4 + ((i32_load8_u(var0 + 122) + (var3 * 255)) << 2)), (i32_load(var4) + var2))
    var3 = i32_load(((var5 + (var3 * 286704)) + 278564))
    if (1 if i32_load(((var5 + (var3 * 286704)) + 278564)) == 0 else 0):
        break
    var1 = (var3 + ((i32_load8_u(var1 + 122) + (var6 * 255)) << 2))
    i32_store((var3 + ((i32_load8_u(var1 + 122) + (var6 * 255)) << 2)), (i32_load(var1) + var2))
    var1 = (i32_load(9142440) + 2)
    var3 = i32_load((i32_load(9142840) + ((var10 + ((var11 + ((i32_load(9142440) + 2) << 1)) * var1)) << 2)))
    if (1 if i32_load((i32_load(9142840) + ((var10 + ((var11 + ((i32_load(9142440) + 2) << 1)) * var1)) << 2))) < 3 else 0):
        break
    var6 = i32_load(9671128)
    var1 = (i32_load(9671128) + (var3 * 132))
    var2 = i32_load(((i32_load8_u((i32_load(9671128) + (var3 * 132)) + 122) * 404) + 9568096) + 292)
    if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var3 * 132)) + 122) * 404) + 9568096) + 292) == 0 else 0):
        break
    var4 = i32_load8_u(var1 + 125)
    if (1 if i32_load8_u(var1 + 125) == 10 else 0):
        break
    var2 = (var2 * 96)
    var10 = (1 if (1 if var2 < 100 else 0) else (((var2 * 96) & 0xFFFFFFFF) // 100))
    var11 = (var6 + (var3 * 132))
    var5 = i32_load((var6 + (var3 * 132)) + 64)
    var2 = ((1 if (1 if var2 < 100 else 0) else (((var2 * 96) & 0xFFFFFFFF) // 100)) if (1 if var5 > var10 else 0) else i32_load((var6 + (var3 * 132)) + 64))
    if (1 if var4 == 3 else 0):
        break
    var4 = (var11 - -64)
    if (1 if var5 <= var10 else 0):
        i32_store(var4, 0)
        func155(var0, var1, 0)
        break
    i32_store(var4, (var5 - var2))
    if (1 if i32_load((var6 + (var3 * 132)) + 92) == 0 else 0):
        break
    if i32_load8_u(9147141):
        break
    i32_store(var9, var2)
    a_b()
    func103(var1)
    i32_store(var7, (i32_load(var7) + var2))
    var7 = i32_load16_u(var11 + 110)
    var3 = i32_load(9561692)
    var5 = i32_load16_u(var0 + 110)
    var6 = i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 278556)
    if i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 278556):
        var0 = (var6 + ((i32_load8_u(var0 + 122) + (var7 * 255)) << 2))
        i32_store((var6 + ((i32_load8_u(var0 + 122) + (var7 * 255)) << 2)), (i32_load(var0) + var2))
    var0 = i32_load(((var3 + (var7 * 286704)) + 278564))
    if (1 if i32_load(((var3 + (var7 * 286704)) + 278564)) == 0 else 0):
        break
    var0 = (var0 + ((i32_load8_u(var1 + 122) + (var5 * 255)) << 2))
    i32_store((var0 + ((i32_load8_u(var1 + 122) + (var5 * 255)) << 2)), (i32_load(var0) + var2))
    global global0
    global0 = (var9 + 48)


# ==========================================================
# $func788
# ==========================================================
def func788(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    if (1 if i32_load8_u(var1 + 125) == 3 else 0):
        break
    if (1 if i32_load(var0 + 8) == 0 else 0):
        if (1 if i32_load(var0 + 104) < 7 else 0):
            break
        var2 = i32_load(var0 + 96)
        var4 = i32_load(var1 + 76)
        var3 = i32_load(var1 + 76)
        var5 = i32_load(var0 + 16)
        # br_table ['$label1', '$label2', '$label3', '$label4', '$label5', '$label6']
        _br_idx = i32_load(var0 + 16)
        break  # br_table
        var0 = i32_load(var2)
        if (1 if i32_load(var2) != 2147483647 else 0):
            i32_store(var1 + 52, var0)
        var0 = i32_load(var2 + 4)
        if (1 if i32_load(var2 + 4) != 2147483647 else 0):
            i32_store(var1 + 60, var0)
        var0 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 2147483647 else 0):
            break
        i32_store(var1 + 64, var0)
        if (1 if i32_load(var2 + 8) == 2147483647 else 0):
            break
        i32_store(var1 + 68, i32_load(var2 + 12))
        var0 = i32_load(var2 + 16)
        if (1 if i32_load(var2 + 16) == 2147483647 else 0):
            break
        i32_store(var1 + 72, var0)
        if (1 if i32_load(var2 + 16) == 2147483647 else 0):
            break
        var3 = i32_load(var2 + 20)
        i32_store(var1 + 76, i32_load(var2 + 20))
        var0 = i32_load(var2 + 24)
        if (1 if i32_load(var2 + 24) == 2147483647 else 0):
            break
        i32_store(var1 + 84, var0)
        break
        var0 = i32_load(var2)
        if (1 if i32_load(var2) != 2147483647 else 0):
            i32_store(var1 + 52, (i32_load(var1 + 52) + var0))
        var0 = i32_load(var2 + 4)
        if (1 if i32_load(var2 + 4) != 2147483647 else 0):
            i32_store(var1 + 60, (i32_load(var1 + 60) + var0))
        var0 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 2147483647 else 0):
            break
        i32_store(var1 + 64, (i32_load(var1 + 64) + var0))
        if (1 if i32_load(var2 + 8) == 2147483647 else 0):
            break
        i32_store(var1 + 68, (i32_load(var1 + 68) + i32_load(var2 + 12)))
        var0 = i32_load(var2 + 16)
        if (1 if i32_load(var2 + 16) == 2147483647 else 0):
            break
        i32_store(var1 + 72, (i32_load(var1 + 72) + var0))
        if (1 if i32_load(var2 + 16) == 2147483647 else 0):
            break
        var3 = (i32_load(var2 + 20) + var4)
        i32_store(var1 + 76, (i32_load(var2 + 20) + var4))
        var0 = i32_load(var2 + 24)
        if (1 if i32_load(var2 + 24) == 2147483647 else 0):
            break
        i32_store(var1 + 84, (i32_load(var1 + 84) + var0))
        break
        var0 = i32_load(var2)
        if (1 if i32_load(var2) != 2147483647 else 0):
            i32_store(var1 + 52, (i32_load(var1 + 52) - var0))
        var0 = i32_load(var2 + 4)
        if (1 if i32_load(var2 + 4) != 2147483647 else 0):
            i32_store(var1 + 60, (i32_load(var1 + 60) - var0))
        var0 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 2147483647 else 0):
            break
        i32_store(var1 + 64, (i32_load(var1 + 64) - var0))
        if (1 if i32_load(var2 + 8) == 2147483647 else 0):
            break
        i32_store(var1 + 68, (i32_load(var1 + 68) - i32_load(var2 + 12)))
        var0 = i32_load(var2 + 16)
        if (1 if i32_load(var2 + 16) == 2147483647 else 0):
            break
        i32_store(var1 + 72, (i32_load(var1 + 72) - var0))
        if (1 if i32_load(var2 + 16) == 2147483647 else 0):
            break
        var3 = (var4 - i32_load(var2 + 20))
        i32_store(var1 + 76, (var4 - i32_load(var2 + 20)))
        var0 = i32_load(var2 + 24)
        if (1 if i32_load(var2 + 24) == 2147483647 else 0):
            break
        i32_store(var1 + 84, (i32_load(var1 + 84) - var0))
        break
        var0 = i32_load(var2)
        if (1 if i32_load(var2) != 2147483647 else 0):
            i32_store(var1 + 52, (i32_load(var1 + 52) * var0))
        var0 = i32_load(var2 + 4)
        if (1 if i32_load(var2 + 4) != 2147483647 else 0):
            i32_store(var1 + 60, (i32_load(var1 + 60) * var0))
        var0 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 2147483647 else 0):
            break
        i32_store(var1 + 64, (i32_load(var1 + 64) * var0))
        if (1 if i32_load(var2 + 8) == 2147483647 else 0):
            break
        i32_store(var1 + 68, (i32_load(var1 + 68) * i32_load(var2 + 12)))
        var0 = i32_load(var2 + 16)
        if (1 if i32_load(var2 + 16) == 2147483647 else 0):
            break
        i32_store(var1 + 72, (i32_load(var1 + 72) * var0))
        if (1 if i32_load(var2 + 16) == 2147483647 else 0):
            break
        var3 = (i32_load(var2 + 20) * var4)
        i32_store(var1 + 76, (i32_load(var2 + 20) * var4))
        var0 = i32_load(var2 + 24)
        if (1 if i32_load(var2 + 24) == 2147483647 else 0):
            break
        i32_store(var1 + 84, (i32_load(var1 + 84) * var0))
        break
        var0 = i32_load(var2)
        if (1 if i32_load(var2) != 2147483647 else 0):
            i32_store(var1 + 52, ((i32_load(var1 + 52) & 0xFFFFFFFF) // var0))
        var0 = i32_load(var2 + 4)
        if (1 if i32_load(var2 + 4) != 2147483647 else 0):
            i32_store(var1 + 60, ((i32_load(var1 + 60) & 0xFFFFFFFF) // var0))
        var0 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 2147483647 else 0):
            break
        i32_store(var1 + 64, ((i32_load(var1 + 64) & 0xFFFFFFFF) // var0))
        if (1 if i32_load(var2 + 8) == 2147483647 else 0):
            break
        i32_store(var1 + 68, ((i32_load(var1 + 68) & 0xFFFFFFFF) // i32_load(var2 + 12)))
        var0 = i32_load(var2 + 16)
        if (1 if i32_load(var2 + 16) == 2147483647 else 0):
            break
        i32_store(var1 + 72, ((i32_load(var1 + 72) & 0xFFFFFFFF) // var0))
        if (1 if i32_load(var2 + 16) == 2147483647 else 0):
            break
        var3 = ((var4 & 0xFFFFFFFF) // i32_load(var2 + 20))
        i32_store(var1 + 76, ((var4 & 0xFFFFFFFF) // i32_load(var2 + 20)))
        var0 = i32_load(var2 + 24)
        if (1 if i32_load(var2 + 24) == 2147483647 else 0):
            break
        i32_store(var1 + 84, ((i32_load(var1 + 84) & 0xFFFFFFFF) // var0))
        var2 = ((i32_load8_u(var1 + 122) * 404) + 9568096)
        var0 = i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 264)
        if (1 if i32_load(var2 + 92) == 0 else 0):
            if (1 if var0 == 2 else 0):
                break
            i32_store(var1 + 52, 0)
        if (1 if var0 != 1 else 0):
            break
        i64_store(var1 + 72, 0)
        var3 = 0
        i32_store(var1 + 60, 0)
        var2 = i32_load(var1 + 64)
        if i32_load(var1 + 64):
            var0 = (2147483646 if (1 if var5 != 2 else 0) else 0)
            if (1 if i32_load(var1 + 52) >= 2147483647 else 0):
                i32_store(var1 + 52, var0)
            if (1 if i32_load(var1 + 60) >= 2147483647 else 0):
                i32_store(var1 + 60, var0)
            if (1 if var2 >= 2147483647 else 0):
                i32_store(var1 + 64, var0)
                var2 = var0
            var5 = i32_load(var1 + 68)
            if (1 if i32_load(var1 + 68) >= 2147483647 else 0):
                i32_store(var1 + 68, var0)
                var5 = var0
            if (1 if i32_load(var1 + 72) >= 2147483647 else 0):
                i32_store(var1 + 72, var0)
            if (1 if var3 >= 2147483647 else 0):
                i32_store(var1 + 76, var0)
                var3 = var0
            if (1 if i32_load(var1 + 84) >= 2147483647 else 0):
                i32_store(var1 + 84, var0)
            if (1 if var2 > var5 else 0):
                i32_store(var1 + 64, var5)
            if (1 if var3 == 0 else 0):
                break
            if var4:
                break
            break
        return
    if (1 if i32_load(var0 + 36) == 0 else 0):
        i32_store(var1 + 64, i32_load(var1 + 68))
        break
    i32_store(var1 + 72, i32_load(var1 + 76))
    if (1 if i32_load(var1 + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load(var1 + 28) else 0):
            break

