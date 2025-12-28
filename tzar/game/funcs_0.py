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
# $func35
# ==========================================================
def func35(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    if (1 if var2 >= 512 else 0):
        # Unknown: memory.copy []
        return var0
    var4 = (var0 + var2)
    if (1 if ((var0 ^ var1) & 3) == 0 else 0):
        if (1 if (var0 & 3) == 0 else 0):
            break
        if (1 if var2 == 0 else 0):
            break
        var2 = (var0 ^ -1)
        var3 = (var0 + 1)
        var3 = ((var0 ^ -1) + (var4 if (1 if var3 < var4 else 0) else (var0 + 1)))
        var2 = (var2 & 3)
        var2 = ((((var0 ^ -1) + (var4 if (1 if var3 < var4 else 0) else (var0 + 1))) if (1 if var2 > var3 else 0) else (var2 & 3)) + 1)
        # Unknown: memory.copy []
        var1 = (var1 + var2)
        var2 = (var0 + var2)
        var3 = (var4 & -4)
        if (1 if (var4 & -4) < 64 else 0):
            break
        var5 = (var3 + -64)
        if (1 if var2 > (var3 + -64) else 0):
            break
        while True:  # loop $label2
            i32_store(var2, i32_load(var1))
            i32_store(var2 + 4, i32_load(var1 + 4))
            i32_store(var2 + 8, i32_load(var1 + 8))
            i32_store(var2 + 12, i32_load(var1 + 12))
            i32_store(var2 + 16, i32_load(var1 + 16))
            i32_store(var2 + 20, i32_load(var1 + 20))
            i32_store(var2 + 24, i32_load(var1 + 24))
            i32_store(var2 + 28, i32_load(var1 + 28))
            i32_store(var2 + 32, i32_load(var1 + 32))
            i32_store(var2 + 36, i32_load(var1 + 36))
            i32_store(var2 + 40, i32_load(var1 + 40))
            i32_store(var2 + 44, i32_load(var1 + 44))
            i32_store(var2 + 48, i32_load(var1 + 48))
            i32_store(var2 + 52, i32_load(var1 + 52))
            i32_store(var2 + 56, i32_load(var1 + 56))
            i32_store(var2 + 60, i32_load(var1 + 60))
            var1 = (var1 - -64)
            var2 = (var2 - -64)
            if (1 if (var2 - -64) <= var5 else 0):
                continue
            break  # end loop
        if (1 if var2 >= var3 else 0):
            break
        var5 = (var2 + 4)
        var3 = ((((var2 ^ -1) + (var3 if (1 if var3 > var5 else 0) else (var2 + 4))) & -4) + 4)
        # Unknown: memory.copy []
        var1 = (var1 + var3)
        var2 = (var2 + var3)
        break
    if (1 if var4 < 4 else 0):
        var2 = var0
        break
    var3 = (var4 - 4)
    if (1 if var0 > (var4 - 4) else 0):
        var2 = var0
        break
    var2 = var0
    while True:  # loop $label4
        i32_store8(var2, i32_load8_u(var1))
        i32_store8(var2 + 1, i32_load8_u(var1 + 1))
        i32_store8(var2 + 2, i32_load8_u(var1 + 2))
        i32_store8(var2 + 3, i32_load8_u(var1 + 3))
        var1 = (var1 + 4)
        var2 = (var2 + 4)
        if (1 if (var2 + 4) <= var3 else 0):
            continue
        break  # end loop
    if (1 if var2 < var4 else 0):
        # Unknown: memory.copy []
    return var0


# ==========================================================
# $func43
# ==========================================================
def func43(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    if (1 if var1 == 0 else 0):
        break
    var3 = (var0 ^ -1)
    if (1 if var2 >= 23 else 0):
        if (1 if (var1 & 3) == 0 else 0):
            break
        var3 = (i32_load(((((i32_load8_u(var1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8))
        var5 = (var1 + 1)
        var0 = (var2 - 1)
        if (1 if (var2 - 1) == 0 else 0):
            break
        if (1 if (var5 & 3) == 0 else 0):
            break
        var3 = (i32_load(((((i32_load8_u(var1 + 1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8))
        var5 = (var1 + 2)
        var0 = (var2 - 2)
        if (1 if (var2 - 2) == 0 else 0):
            break
        if (1 if (var5 & 3) == 0 else 0):
            break
        var3 = (i32_load(((((i32_load8_u(var1 + 2) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8))
        var5 = (var1 + 3)
        var0 = (var2 - 3)
        if (1 if (var2 - 3) == 0 else 0):
            break
        if (1 if (var5 & 3) == 0 else 0):
            break
        var3 = (i32_load(((((i32_load8_u(var1 + 3) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8))
        var1 = (var1 + 4)
        var2 = (var2 - 4)
        break
        var2 = var0
        var1 = var5
        break
        var2 = var0
        var1 = var5
        break
        var2 = var0
        var1 = var5
        var0 = ((var2 & 0xFFFFFFFF) // 20)
        var11 = (((var2 & 0xFFFFFFFF) // 20) * -20)
        var10 = (var0 - 1)
        if (1 if (var0 - 1) == 0 else 0):
            break
        var5 = ((var0 * 20) - 20)
        var0 = var1
        while True:  # loop $label6
            var4 = (i32_load(var0 + 16) ^ var9)
            var9 = (i32_load((((((i32_load(var0 + 16) ^ var9) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (i32_load(((((var4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (i32_load(((((var4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ i32_load((((var4 & 255) << 2) + 19248)))))
            var4 = (i32_load(var0 + 12) ^ var8)
            var8 = (i32_load((((((i32_load(var0 + 12) ^ var8) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (i32_load(((((var4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (i32_load(((((var4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ i32_load((((var4 & 255) << 2) + 19248)))))
            var4 = (i32_load(var0 + 8) ^ var6)
            var6 = (i32_load((((((i32_load(var0 + 8) ^ var6) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (i32_load(((((var4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (i32_load(((((var4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ i32_load((((var4 & 255) << 2) + 19248)))))
            var4 = (i32_load(var0 + 4) ^ var7)
            var7 = (i32_load((((((i32_load(var0 + 4) ^ var7) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (i32_load(((((var4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (i32_load(((((var4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ i32_load((((var4 & 255) << 2) + 19248)))))
            var4 = (i32_load(var0) ^ var3)
            var3 = (i32_load((((((i32_load(var0) ^ var3) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (i32_load(((((var4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (i32_load(((((var4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ i32_load((((var4 & 255) << 2) + 19248)))))
            var0 = (var0 + 20)
            var10 = (var10 - 1)
            if (var10 - 1):
                continue
            break  # end loop
        var1 = (var1 + var5)
        var2 = (var2 + var11)
        var0 = (i32_load(var1) ^ var3)
        var0 = ((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = (((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = ((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = ((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8))
        var0 = (((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = ((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = (((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = ((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8))
        var0 = (((((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = ((((((((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = (((((((((((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = ((i32_load(var1 + 12) ^ (i32_load(((((((((((((((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var8)) ^ ((var0 & 0xFFFFFFFF) >> 8))
        var0 = (((((i32_load(var1 + 12) ^ (i32_load(((((((((((((((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var8)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = ((((((((i32_load(var1 + 12) ^ (i32_load(((((((((((((((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var8)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = (((((((((((i32_load(var1 + 12) ^ (i32_load(((((((((((((((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var8)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = ((i32_load(var1 + 16) ^ (i32_load(((((((((((((((i32_load(var1 + 12) ^ (i32_load(((((((((((((((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var8)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var9)) ^ ((var0 & 0xFFFFFFFF) >> 8))
        var0 = (((((i32_load(var1 + 16) ^ (i32_load(((((((((((((((i32_load(var1 + 12) ^ (i32_load(((((((((((((((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var8)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var9)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = ((((((((i32_load(var1 + 16) ^ (i32_load(((((((((((((((i32_load(var1 + 12) ^ (i32_load(((((((((((((((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var8)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var9)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var0 = (((((((((((i32_load(var1 + 16) ^ (i32_load(((((((((((((((i32_load(var1 + 12) ^ (i32_load(((((((((((((((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var8)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var9)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var3 = ((((((((((((((i32_load(var1 + 16) ^ (i32_load(((((((((((((((i32_load(var1 + 12) ^ (i32_load(((((((((((((((i32_load(var1 + 8) ^ (i32_load(((((((((((((((i32_load(var1 + 4) ^ (i32_load((((((((((((((i32_load(var1) ^ var3) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var7)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var6)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var8)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ var9)) ^ ((var0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load((((var0 & 255) << 2) + 18224)))
        var1 = (var1 + 20)
    if (1 if var2 > 7 else 0):
        while True:  # loop $label7
            var0 = (i32_load(((((i32_load8_u(var1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8))
            var0 = ((((i32_load(((((i32_load8_u(var1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 1) ^ var0) & 255) << 2) + 18224)))
            var0 = (((((((i32_load(((((i32_load8_u(var1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 1) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 2) ^ var0) & 255) << 2) + 18224)))
            var0 = ((((((((((i32_load(((((i32_load8_u(var1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 1) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 2) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 3) ^ var0) & 255) << 2) + 18224)))
            var0 = (((((((((((((i32_load(((((i32_load8_u(var1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 1) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 2) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 3) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 4) ^ var0) & 255) << 2) + 18224)))
            var0 = ((((((((((((((((i32_load(((((i32_load8_u(var1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 1) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 2) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 3) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 4) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 5) ^ var0) & 255) << 2) + 18224)))
            var0 = (((((((((((((((((((i32_load(((((i32_load8_u(var1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 1) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 2) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 3) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 4) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 5) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 6) ^ var0) & 255) << 2) + 18224)))
            var3 = ((((((((((((((((((((((i32_load(((((i32_load8_u(var1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 1) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 2) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 3) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 4) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 5) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 6) ^ var0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ i32_load(((((i32_load8_u(var1 + 7) ^ var0) & 255) << 2) + 18224)))
            var1 = (var1 + 8)
            var2 = (var2 - 8)
            if (1 if (var2 - 8) > 7 else 0):
                continue
            break  # end loop
    if (1 if var2 == 0 else 0):
        break
    if (var2 & 1):
        var3 = (i32_load(((((i32_load8_u(var1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8))
        var1 = (var1 + 1)
    else:
    var0 = var2
    if (1 if var2 == 1 else 0):
        break
    while True:  # loop $label9
        var2 = (i32_load(((((i32_load8_u(var1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8))
        var3 = (i32_load((((((i32_load(((((i32_load8_u(var1) ^ var3) & 255) << 2) + 18224)) ^ ((var3 & 0xFFFFFFFF) >> 8)) ^ i32_load8_u(var1 + 1)) & 255) << 2) + 18224)) ^ ((var2 & 0xFFFFFFFF) >> 8))
        var1 = (var1 + 2)
        var0 = (var0 - 2)
        if (var0 - 2):
            continue
        break  # end loop
    return (var3 ^ -1)


# ==========================================================
# $func50
# ==========================================================
def func50(var0):
    var1 = 0
    var1 = i32_load(var0 + 5820)
    if (1 if i32_load(var0 + 5820) == 16 else 0):
        var1 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var1 + i32_load(var0 + 8)), i32_load8_u(var0 + 5816))
        var1 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var1 + i32_load(var0 + 8)), i32_load8_u((var0 + 5817)))
        i32_store16(var0 + 5816, 0)
        break
    if (1 if var1 < 8 else 0):
        break
    var1 = i32_load(var0 + 20)
    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
    i32_store8((var1 + i32_load(var0 + 8)), i32_load8_u(var0 + 5816))
    i32_store16(var0 + 5816, i32_load8_u((var0 + 5817)))
    i32_store(0 + 5820, (i32_load(var0 + 5820) - 8))
    return var0

