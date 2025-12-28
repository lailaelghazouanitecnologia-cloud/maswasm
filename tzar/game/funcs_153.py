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
# $func745
# ==========================================================
def func745(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var3 = i32_load(9671128)
    var4 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) != 3 else 0):
        var1 = i32_load(var4 + 16)
        if (1 if i32_load(var4 + 16) == 0 else 0):
            break
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        while True:  # loop $label1
            var5 = (var3 + (i32_load((i32_load(var1) + (var2 << 2))) * 132))
            var7 = i32_load((var3 + (i32_load((i32_load(var1) + (var2 << 2))) * 132)) + 64)
            var6 = i32_load(var5 + 68)
            if (1 if i32_load((var3 + (i32_load((i32_load(var1) + (var2 << 2))) * 132)) + 64) < i32_load(var5 + 68) else 0):
                var1 = (var7 + 2)
                i32_store((var5 - -64), ((var7 + 2) if (1 if var1 < var6 else 0) else var6))
                var3 = i32_load(9671128)
                var1 = i32_load(var4 + 16)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < i32_load(var1 + 8) else 0):
                continue
            break  # end loop


# ==========================================================
# $func762
# ==========================================================
def func762(var0, var1, var2):
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
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var4 = i32_load(9561692)
    var8 = i32_load(9671128)
    var9 = i32_load(var1)
    var1 = i32_load16_u((i32_load(9671128) + (i32_load(var1) * 132)) + 110)
    var3 = (i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (i32_load(var1) * 132)) + 110) * 286704))
    var6 = ((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (i32_load(var1) * 132)) + 110) * 286704)) + 283916)
    var5 = i32_load(var3 + 283916)
    if i32_load(var0 + 4):
        if var5:
            break
        var10 = (var4 + (var1 * 286704))
        var0 = i32_load(var0)
        var11 = (3 if (1 if var0 >= 3 else 0) else i32_load(var0))
        var0 = (((var4 + (var1 * 286704)) + ((3 if (1 if var0 >= 3 else 0) else i32_load(var0)) << 2)) + 283848)
        var3 = i32_load((((var4 + (var1 * 286704)) + ((3 if (1 if var0 >= 3 else 0) else i32_load(var0)) << 2)) + 283848))
        if (1 if i32_load((((var4 + (var1 * 286704)) + ((3 if (1 if var0 >= 3 else 0) else i32_load(var0)) << 2)) + 283848)) == 2147483647 else 0):
            break
        i32_store(var0, (var3 + 1000))
        var0 = 1
        i32_store8(var10 + 286701, 1)
        var3 = i32_load(9142892)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var7 = (var3 - 1)
        var12 = ((var3 - 1) & 1)
        var1 = (i32_load((var4 + (var1 * 286704)) + 283908) * var3)
        var4 = i32_load(9561692)
        var5 = i32_load(9143016)
        if (1 if var3 != 2 else 0):
            var7 = (var7 & -2)
            var3 = 0
            while True:  # loop $label2
                if i32_load8_u((var5 + (var0 + var1))):
                    i32_store8((var4 + (var0 * 286704)) + 286701, 1)
                var13 = (var0 + 1)
                if i32_load8_u((var5 + ((var0 + 1) + var1))):
                    i32_store8((var4 + (var13 * 286704)) + 286701, 1)
                var0 = (var0 + 2)
                var3 = (var3 + 2)
                if (1 if (var3 + 2) != var7 else 0):
                    continue
                break  # end loop
        if (1 if var12 == 0 else 0):
            break
        if (1 if i32_load8_u((var5 + (var0 + var1))) == 0 else 0):
            break
        i32_store8((var4 + (var0 * 286704)) + 286701, 1)
        i32_store(var6, 1200)
        i32_store(var10 + 283920, var11)
        break
    if (1 if var5 == 0 else 0):
        break
    i64_store(var2 + 8, 0)
    i64_store(var2, 0)
    i32_store((var2 + (i32_load((var4 + (var1 * 286704)) + 283920) << 2)), i32_load(var6))
    if func66(var3, var2, 1, 1):
        break
    i32_store(var6, 0)
    if (1 if i32_load((var8 + (var9 * 132)) + 92) == 0 else 0):
        break
    var0 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var8 + (var9 * 132)) + 28) else 0):
            break
    global global0
    global0 = (var2 + 16)


# ==========================================================
# $func763
# ==========================================================
def func763(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(var1 + 12, 1)
    i32_store(var1 + 8, var0)
    var0 = i32_load(9213808)
    if i32_load8_u(9147210):
        func41(38, 9173808, var0, (var1 + 8), 2)
        break
    var3 = (var0 << 2)
    var2 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var0:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9214128)]
    global global0
    global0 = (var1 + 16)

