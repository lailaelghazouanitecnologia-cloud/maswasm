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
# $func822
# ==========================================================
def func822(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    while True:  # loop $label7
        if (1 if i32_load(var0 + 116) > 261 else 0):
            break
        var2 = i32_load(var0 + 116)
        if var1:
            break
        if (1 if var2 >= 262 else 0):
            break
        return 0
        if (1 if var2 == 0 else 0):
            break
        if (1 if var2 > 2 else 0):
            break
        var2 = i32_load(var0 + 96)
        i32_store(var0 + 120, i32_load(var0 + 96))
        i32_store(var0 + 100, i32_load(var0 + 112))
        var4 = 2
        i32_store(var0 + 96, 2)
        break
        var4 = 2
        var3 = i32_load(var0 + 108)
        var2 = (i32_load(var0 + 84) & (i32_load8_u((i32_load(var0 + 108) + i32_load(var0 + 56)) + 2) ^ (i32_load(var0 + 72) << i32_load(var0 + 88))))
        i32_store(var0 + 72, (i32_load(var0 + 84) & (i32_load8_u((i32_load(var0 + 108) + i32_load(var0 + 56)) + 2) ^ (i32_load(var0 + 72) << i32_load(var0 + 88)))))
        var2 = (i32_load(var0 + 68) + (var2 << 1))
        var5 = i32_load16_u((i32_load(var0 + 68) + (var2 << 1)))
        i32_store16((i32_load(var0 + 64) + ((var3 & i32_load(var0 + 52)) << 1)), i32_load16_u((i32_load(var0 + 68) + (var2 << 1))))
        i32_store16(var2, var3)
        var2 = i32_load(var0 + 96)
        i32_store(var0 + 120, i32_load(var0 + 96))
        i32_store(var0 + 100, i32_load(var0 + 112))
        i32_store(var0 + 96, 2)
        if (1 if var5 == 0 else 0):
            break
        if (1 if var2 >= i32_load(var0 + 128) else 0):
            break
        if (1 if (i32_load(var0 + 44) - 262) < (var3 - var5) else 0):
            break
        var4 = func359(var0, var5)
        i32_store(var0 + 96, func359(var0, var5))
        if (1 if var4 > 5 else 0):
            break
        if (1 if i32_load(var0 + 136) != 1 else 0):
            if (1 if var4 != 3 else 0):
                break
            var4 = 3
            if (1 if (i32_load(var0 + 108) - i32_load(var0 + 112)) < 4097 else 0):
                break
        var4 = 2
        i32_store(var0 + 96, 2)
        var2 = i32_load(var0 + 120)
        if (1 if var2 < 3 else 0):
            break
        if (1 if var2 < var4 else 0):
            break
        var3 = i32_load(var0 + 5792)
        i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
        var5 = i32_load(var0 + 116)
        var6 = i32_load(var0 + 108)
        var3 = (i32_load(var0 + 108) + (i32_load(var0 + 100) ^ -1))
        i32_store8((var3 + i32_load(var0 + 5784)), (i32_load(var0 + 108) + (i32_load(var0 + 100) ^ -1)))
        var4 = i32_load(var0 + 5792)
        i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
        i32_store8((var4 + i32_load(var0 + 5784)), ((var3 & 0xFFFFFFFF) >> 8))
        var4 = i32_load(var0 + 5792)
        i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
        var2 = (var2 - 3)
        i32_store8((var4 + i32_load(var0 + 5784)), (var2 - 3))
        var2 = (((i32_load8_u(((var2 & 255) + 23984)) << 2) + var0) + 1176)
        i32_store16((((i32_load8_u(((var2 & 255) + 23984)) << 2) + var0) + 1176), (i32_load16_u(var2) + 1))
        var2 = ((var3 - 1) & 65535)
        var2 = ((var0 + (i32_load8_u(((((var3 - 1) & 65535) if (1 if var2 < 256 else 0) else (((var2 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2440)
        i32_store16(((var0 + (i32_load8_u(((((var3 - 1) & 65535) if (1 if var2 < 256 else 0) else (((var2 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2440), (i32_load16_u(var2) + 1))
        var2 = i32_load(var0 + 120)
        var4 = (i32_load(var0 + 120) - 2)
        i32_store(var0 + 120, (i32_load(var0 + 120) - 2))
        i32_store(var0 + 116, ((i32_load(var0 + 116) - var2) + 1))
        var5 = ((var5 + var6) - 3)
        var2 = i32_load(var0 + 108)
        var6 = i32_load(var0 + 5796)
        var8 = i32_load(var0 + 5792)
        while True:  # loop $label6
            var3 = var2
            var2 = (var2 + 1)
            i32_store(var0 + 108, (var2 + 1))
            if (1 if var2 <= var5 else 0):
                var7 = (i32_load(var0 + 84) & (i32_load8_u((var3 + i32_load(var0 + 56)) + 3) ^ (i32_load(var0 + 72) << i32_load(var0 + 88))))
                i32_store(var0 + 72, (i32_load(var0 + 84) & (i32_load8_u((var3 + i32_load(var0 + 56)) + 3) ^ (i32_load(var0 + 72) << i32_load(var0 + 88)))))
                var7 = (i32_load(var0 + 68) + (var7 << 1))
                i32_store16((i32_load(var0 + 64) + ((i32_load(var0 + 52) & var2) << 1)), i32_load16_u((i32_load(var0 + 68) + (var7 << 1))))
                i32_store16(var7, var2)
            var4 = (var4 - 1)
            i32_store(var0 + 120, (var4 - 1))
            if var4:
                continue
            break  # end loop
        i32_store(var0 + 96, 2)
        i32_store(var0 + 104, 0)
        var3 = (var3 + 2)
        i32_store(var0 + 108, (var3 + 2))
        if (1 if var6 != var8 else 0):
            continue
        var4 = 0
        var2 = i32_load(var0 + 92)
        if (1 if i32_load(var0 + 92) >= 0 else 0):
        else:
        i32_store(var0 + 92, i32_load(var0 + 108))
        var2 = i32_load(var0)
        var3 = i32_load(i32_load(var0) + 28)
        var4 = i32_load(var3 + 20)
        var5 = i32_load(var2 + 16)
        var4 = (i32_load(var3 + 20) if (1 if var4 < var5 else 0) else i32_load(var2 + 16))
        if (1 if (i32_load(var3 + 20) if (1 if var4 < var5 else 0) else i32_load(var2 + 16)) == 0 else 0):
            break
        i32_store(var2 + 12, (i32_load(var2 + 12) + var4))
        i32_store(var3 + 16, (i32_load(var3 + 16) + var4))
        i32_store(var2 + 20, (i32_load(var2 + 20) + var4))
        i32_store(var2 + 16, (i32_load(var2 + 16) - var4))
        var2 = i32_load(var3 + 20)
        i32_store(var3 + 20, (i32_load(var3 + 20) - var4))
        if (1 if var2 != var4 else 0):
            break
        i32_store(var3 + 16, i32_load(var3 + 8))
        if i32_load(i32_load(var0) + 16):
            continue
        return 0
        if i32_load(var0 + 104):
            var2 = i32_load8_u(((i32_load(var0 + 108) + i32_load(var0 + 56)) - 1))
            var3 = i32_load(var0 + 5792)
            i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
            i32_store8((var3 + i32_load(var0 + 5784)), 0)
            var3 = i32_load(var0 + 5792)
            i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
            i32_store8((var3 + i32_load(var0 + 5784)), 0)
            var3 = i32_load(var0 + 5792)
            i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
            i32_store8((var3 + i32_load(var0 + 5784)), var2)
            var2 = (var0 + (var2 << 2))
            i32_store16(((var0 + (var2 << 2)) + 148), (i32_load16_u(var2 + 148) + 1))
            if (1 if i32_load(var0 + 5792) != i32_load(var0 + 5796) else 0):
                break
            var4 = 0
            var2 = i32_load(var0 + 92)
            if (1 if i32_load(var0 + 92) >= 0 else 0):
            else:
            i32_store(var0 + 92, i32_load(var0 + 108))
            var2 = i32_load(var0)
            var3 = i32_load(i32_load(var0) + 28)
            var4 = i32_load(var3 + 20)
            var5 = i32_load(var2 + 16)
            var4 = (i32_load(var3 + 20) if (1 if var4 < var5 else 0) else i32_load(var2 + 16))
            if (1 if (i32_load(var3 + 20) if (1 if var4 < var5 else 0) else i32_load(var2 + 16)) == 0 else 0):
                break
            i32_store(var2 + 12, (i32_load(var2 + 12) + var4))
            i32_store(var3 + 16, (i32_load(var3 + 16) + var4))
            i32_store(var2 + 20, (i32_load(var2 + 20) + var4))
            i32_store(var2 + 16, (i32_load(var2 + 16) - var4))
            var2 = i32_load(var3 + 20)
            i32_store(var3 + 20, (i32_load(var3 + 20) - var4))
            if (1 if var2 != var4 else 0):
                break
            i32_store(var3 + 16, i32_load(var3 + 8))
            i32_store(var0 + 108, (i32_load(var0 + 108) + 1))
            i32_store(var0 + 116, (i32_load(var0 + 116) - 1))
            if i32_load(i32_load(var0) + 16):
                continue
            return 0
        else:
            i32_store(var0 + 104, 1)
            i32_store(var0 + 108, (i32_load(var0 + 108) + 1))
            i32_store(var0 + 116, (i32_load(var0 + 116) - 1))
            continue
        raise RuntimeError('unreachable')
        break  # end loop
    if i32_load(var0 + 104):
        var2 = i32_load8_u(((i32_load(var0 + 108) + i32_load(var0 + 56)) - 1))
        var3 = i32_load(var0 + 5792)
        i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
        i32_store8((var3 + i32_load(var0 + 5784)), 0)
        var3 = i32_load(var0 + 5792)
        i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
        i32_store8((var3 + i32_load(var0 + 5784)), 0)
        var3 = i32_load(var0 + 5792)
        i32_store(var0 + 5792, (i32_load(var0 + 5792) + 1))
        i32_store8((var3 + i32_load(var0 + 5784)), var2)
        var2 = (var0 + (var2 << 2))
        i32_store16(((var0 + (var2 << 2)) + 148), (i32_load16_u(var2 + 148) + 1))
        i32_store(var0 + 104, 0)
    var2 = i32_load(var0 + 108)
    i32_store(var0 + 5812, (2 if (1 if var2 >= 2 else 0) else i32_load(var0 + 108)))
    if (1 if var1 == 4 else 0):
        var4 = 0
        var1 = i32_load(var0 + 92)
        if (1 if i32_load(var0 + 92) >= 0 else 0):
        else:
        i32_store(var0 + 92, i32_load(var0 + 108))
        var1 = i32_load(var0)
        var2 = i32_load(i32_load(var0) + 28)
        var3 = i32_load(var2 + 20)
        var4 = i32_load(var1 + 16)
        var3 = (i32_load(var2 + 20) if (1 if var3 < var4 else 0) else i32_load(var1 + 16))
        if (1 if (i32_load(var2 + 20) if (1 if var3 < var4 else 0) else i32_load(var1 + 16)) == 0 else 0):
            break
        i32_store(var1 + 12, (i32_load(var1 + 12) + var3))
        i32_store(var2 + 16, (i32_load(var2 + 16) + var3))
        i32_store(var1 + 20, (i32_load(var1 + 20) + var3))
        i32_store(var1 + 16, (i32_load(var1 + 16) - var3))
        var1 = i32_load(var2 + 20)
        i32_store(var2 + 20, (i32_load(var2 + 20) - var3))
        if (1 if var1 != var3 else 0):
            break
        i32_store(var2 + 16, i32_load(var2 + 8))
        return (3 if i32_load(i32_load(var0) + 16) else 2)
    if (1 if i32_load(var0 + 5792) == 0 else 0):
        break
    var4 = 0
    var1 = i32_load(var0 + 92)
    if (1 if i32_load(var0 + 92) >= 0 else 0):
    else:
    i32_store(var0 + 92, i32_load(var0 + 108))
    var1 = i32_load(var0)
    var2 = i32_load(i32_load(var0) + 28)
    var3 = i32_load(var2 + 20)
    var4 = i32_load(var1 + 16)
    var3 = (i32_load(var2 + 20) if (1 if var3 < var4 else 0) else i32_load(var1 + 16))
    if (1 if (i32_load(var2 + 20) if (1 if var3 < var4 else 0) else i32_load(var1 + 16)) == 0 else 0):
        break
    i32_store(var1 + 12, (i32_load(var1 + 12) + var3))
    i32_store(var2 + 16, (i32_load(var2 + 16) + var3))
    i32_store(var1 + 20, (i32_load(var1 + 20) + var3))
    i32_store(var1 + 16, (i32_load(var1 + 16) - var3))
    var1 = i32_load(var2 + 20)
    i32_store(var2 + 20, (i32_load(var2 + 20) - var3))
    if (1 if var1 != var3 else 0):
        break
    i32_store(var2 + 16, i32_load(var2 + 8))
    if i32_load(i32_load(var0) + 16):
        break
    return 0
    return 1

