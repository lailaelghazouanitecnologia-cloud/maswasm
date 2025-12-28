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
# $func451
# ==========================================================
def func451(var0, var1, var2, var3):
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
    var9 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var4 = 2
    if (1 if var1 <= 0 else 0):
        break
    if (1 if var0 <= 0 else 0):
        break
    if (1 if var3 == 0 else 0):
        break
    if (1 if var2 == 0 else 0):
        break
    if i32_load(var2 + 8):
        var5 = var0
        var6 = var1
        var0 = i32_load(var2 + 20)
        var1 = i32_load(var2 + 24)
        var7 = (i32_load(var2 + 12) & -2)
        var8 = (i32_load(var2 + 16) & -2)
        if (1 if ((i32_load(var2 + 12) & -2) | (i32_load(var2 + 16) & -2)) < 0 else 0):
            break
        if (1 if var0 <= 0 else 0):
            break
        if (1 if var1 <= 0 else 0):
            break
        var10 = ((((((1 if var0 <= var5 else 0) & (1 if var5 > var7 else 0)) & (1 if (var5 - var7) >= var0 else 0)) & (1 if var6 > var8 else 0)) & (1 if var1 <= var6 else 0)) & (1 if (var6 - var8) >= var1 else 0))
        if (1 if var10 == 0 else 0):
            break
    if (1 if i32_load(var2 + 28) == 0 else 0):
        break
    i32_store(var9 + 12, i32_load(var2 + 32))
    i32_store(var9 + 8, i32_load(var2 + 36))
    if (1 if func444(var0, var1, (var9 + 12), (var9 + 8)) == 0 else 0):
        break
    var1 = i32_load(var9 + 8)
    var0 = i32_load(var9 + 12)
    i32_store(var3 + 8, var1)
    i32_store(var3 + 4, var0)
    if (1 if var0 <= 0 else 0):
        break
    if (1 if var1 <= 0 else 0):
        break
    var5 = i32_load(var3)
    if (1 if i32_load(var3) > 12 else 0):
        break
    if (1 if i32_load(var3 + 12) > 0 else 0):
        break
    if i32_load(var3 + 80):
        break
    var12 = i64_extend_u(var0)
    var6 = i32_load8_u((var5 + 10296))
    if (1 if (i64_extend_u(var0) * i64_extend_u(i32_load8_u((var5 + 10296)))) > 2147483647 else 0):
        break
    var13 = i64_extend_u(var1)
    var10 = (var0 * var6)
    var14 = (i64_extend_u(var1) * i64_extend_s((var0 * var6)))
    var4 = 1
    if (1 if var5 < 11 else 0):
        var12 = 0
        var0 = 0
        break
    var6 = (1 if var5 == 12 else 0)
    var12 = ((var12 * var13) if (1 if var5 == 12 else 0) else 0)
    var11 = (var0 if var6 else 0)
    var0 = (((var0 + 1) & 0xFFFFFFFF) >> 1)
    var13 = (i64_extend_u((((var0 + 1) & 0xFFFFFFFF) >> 1)) * i64_extend_u((((var1 + 1) & 0xFFFFFFFF) >> 1)))
    var15 = ((i64_extend_u((((var0 + 1) & 0xFFFFFFFF) >> 1)) * i64_extend_u((((var1 + 1) & 0xFFFFFFFF) >> 1))) << 1)
    var1 = func58((((i64_extend_u((((var0 + 1) & 0xFFFFFFFF) >> 1)) * i64_extend_u((((var1 + 1) & 0xFFFFFFFF) >> 1))) << 1) + (var12 + var14)), 1)
    if (1 if func58((((i64_extend_u((((var0 + 1) & 0xFFFFFFFF) >> 1)) * i64_extend_u((((var1 + 1) & 0xFFFFFFFF) >> 1))) << 1) + (var12 + var14)), 1) == 0 else 0):
        break
    i32_store(var3 + 16, var1)
    i32_store(var3 + 80, var1)
    var6 = i32(var14)
    if (1 if var5 >= 11 else 0):
        i32_store(var3 + 48, var6)
        i32_store(var3 + 32, var10)
        var4 = i32(var13)
        i32_store(var3 + 52, i32(var13))
        i32_store(var3 + 36, var0)
        var1 = (var1 + var6)
        i32_store(var3 + 20, (var1 + var6))
        i32_store(var3 + 56, var4)
        i32_store(var3 + 40, var0)
        i32_store(var3 + 24, (var1 + var4))
        if (1 if var5 == 12 else 0):
            i32_store(var3 + 28, (var1 + i32(var15)))
        i32_store(var3 + 44, var11)
        i64_store32(var3 + 60, var12)
        break
    i32_store(var3 + 24, var6)
    i32_store(var3 + 20, var10)
    var6 = 2
    var1 = i32_load(var3)
    if (1 if i32_load(var3) > 12 else 0):
        break
    var5 = i32_load(var3 + 8)
    var0 = i32_load(var3 + 4)
    if (1 if var1 >= 11 else 0):
        var4 = i32_load(var3 + 40)
        var4 = (var4 >> 31)
        var10 = ((i32_load(var3 + 40) ^ (var4 >> 31)) - var4)
        var4 = ((var0 + 1) // 2)
        var7 = i32_load(var3 + 36)
        var7 = (var7 >> 31)
        var7 = ((i32_load(var3 + 36) ^ (var7 >> 31)) - var7)
        var8 = i32_load(var3 + 32)
        var8 = (var8 >> 31)
        var8 = ((i32_load(var3 + 32) ^ (var8 >> 31)) - var8)
        var12 = i64_extend_s(var0)
        var14 = i64_extend_s((var5 - 1))
        var13 = i64_extend_s(var4)
        var15 = i64_extend_s((((var5 + 1) // 2) - 1))
        var5 = (((((1 if ((i32_load(var3 + 40) ^ (var4 >> 31)) - var4) >= ((var0 + 1) // 2) else 0) & ((1 if ((i32_load(var3 + 36) ^ (var7 >> 31)) - var7) >= var4 else 0) & ((1 if ((i32_load(var3 + 32) ^ (var8 >> 31)) - var8) >= var0 else 0) & (((1 if i64_load32_u(var3 + 48) >= (i64_extend_s(var0) + (i64_extend_s((var5 - 1)) * i64_extend_u(var8))) else 0) & (1 if i64_load32_u(var3 + 52) >= (i64_extend_s(var4) + (i64_extend_s((((var5 + 1) // 2) - 1)) * i64_extend_u(var7))) else 0)) & (1 if i64_load32_u(var3 + 56) >= ((i64_extend_u(var10) * var15) + var13) else 0))))) & (1 if i32_load(var3 + 16) != 0 else 0)) & (1 if i32_load(var3 + 20) != 0 else 0)) & (1 if i32_load(var3 + 24) != 0 else 0))
        if (1 if var1 != 12 else 0):
            break
        var1 = i32_load(var3 + 44)
        var1 = (var1 >> 31)
        var1 = ((i32_load(var3 + 44) ^ (var1 >> 31)) - var1)
        if ((((1 if var0 <= ((i32_load(var3 + 44) ^ (var1 >> 31)) - var1) else 0) & (1 if i64_load32_u(var3 + 60) >= ((i64_extend_u(var1) * var14) + var12) else 0)) & (1 if i32_load(var3 + 28) != 0 else 0)) & var5):
            break
        break
    var4 = i32_load(var3 + 20)
    var4 = (var4 >> 31)
    var4 = ((i32_load(var3 + 20) ^ (var4 >> 31)) - var4)
    var1 = i32_load8_u((var1 + 10296))
    if (((1 if ((i32_load(var3 + 20) ^ (var4 >> 31)) - var4) >= (var0 * i32_load8_u((var1 + 10296))) else 0) & (1 if i64_load32_u(var3 + 24) >= ((i64_extend_s((var5 - 1)) * i64_extend_u(var4)) + (i64_extend_s(var0) * i64_extend_u(var1))) else 0)) & (1 if i32_load(var3 + 16) != 0 else 0)):
        break
    break
    if (1 if var5 == 0 else 0):
        break
    var6 = 0
    var4 = var6
    if (1 if var2 == 0 else 0):
        break
    if var4:
        break
    if (1 if i32_load(var2 + 48) == 0 else 0):
        var4 = 0
        break
    var2 = i32_load(var3 + 16)
    var5 = i32_load(var3 + 8)
    if (1 if i32_load(var3) <= 10 else 0):
        var0 = (var3 + 20)
        var1 = i32_load((var3 + 20))
        i32_store(var3 + 16, (var2 + (i32_load((var3 + 20)) * (var5 - 1))))
        break
    var4 = 0
    var0 = i32_load(var3 + 32)
    i32_store(var3 + 32, (0 - i32_load(var3 + 32)))
    var1 = i32_load(var3 + 36)
    i32_store(var3 + 36, (0 - i32_load(var3 + 36)))
    var6 = i32_load(var3 + 40)
    i32_store(var3 + 40, (0 - i32_load(var3 + 40)))
    var12 = (i64_extend_s(var5) - 1)
    var5 = i32((i64_extend_s(var5) - 1))
    i32_store(var3 + 16, (var2 + (var0 * i32((i64_extend_s(var5) - 1)))))
    var0 = i32(((var12 & 0xFFFFFFFFFFFFFFFF) >> 1))
    i32_store(var3 + 20, (i32_load(var3 + 20) + (var1 * i32(((var12 & 0xFFFFFFFFFFFFFFFF) >> 1)))))
    i32_store(var3 + 24, (i32_load(var3 + 24) + (var0 * var6)))
    var2 = i32_load(var3 + 28)
    if (1 if i32_load(var3 + 28) == 0 else 0):
        break
    var0 = (var3 + 44)
    var1 = i32_load((var3 + 44))
    i32_store(var3 + 28, (var2 + (i32_load((var3 + 44)) * var5)))
    var4 = 0
    i32_store(var0, (0 - var1))
    global global0
    global0 = (var9 + 16)
    return var4


# ==========================================================
# $func452
# ==========================================================
def func452(var0, var1):
    var2 = 0
    var3 = 0
    i32_store(var1 + 8, 0)
    i32_store(var1 + 16, var1)
    var3 = func58(i64_extend_s(var0), 4)
    if func58(i64_extend_s(var0), 4):
        i32_store(var1 + 4, var3)
        var2 = 1
    else:
    i32_store(var0 + 12, 0)
    i32_store(var1, var3)
    return var2

