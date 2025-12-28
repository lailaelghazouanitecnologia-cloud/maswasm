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
# $func921
# ==========================================================
def func921(var0):
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
    var11 = 0
    var12 = 0
    var13 = 0
    var14 = 0
    var15 = 0
    var16 = 0
    var17 = 0
    var18 = 0
    var19 = 0
    var9 = i32_load8_u(var0 + 122)
    var5 = 1
    var12 = i32_load(9671128)
    var13 = i32_load(var0 + 32)
    var1 = (i32_load(9671128) + (i32_load(var0 + 32) * 132))
    var14 = i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 122)
    var15 = i32_load8_u(var1 + 125)
    if (1 if func162(var0, i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 122), i32_load8_u(var1 + 125), i32_load(var1 + 28)) == 0 else 0):
        break
    if (1 if i32_load(38564) != var14 else 0):
        break
    if (1 if i32_load(((var9 * 404) + 9568096) + 268) == 2 else 0):
        break
    var8 = i32_load(var0 + 84)
    var1 = i32_load(9561692)
    var6 = i32_load16_u(var0 + 110)
    var3 = (i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704))
    if (1 if i32_load(var0 + 84) >= i32_load(((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 284316)) else 0):
        break
    var7 = i32_load((var3 + 284012))
    var2 = 10
    if i32_load(((var3 + (i32_load(38488) << 2)) + 281808)):
        break
    var3 = (var1 + (var6 * 286704))
    if i32_load((((var1 + (var6 * 286704)) + (i32_load(38848) << 2)) + 281808)):
        break
    var2 = (10 if i32_load(((var3 + (i32_load(38916) << 2)) + 281808)) else 0)
    if (1 if var8 >= (var2 + var7) else 0):
        break
    if (1 if i32_load(((var1 + (var6 * 286704)) + 284008)) == 0 else 0):
        break
    var1 = (var12 + (var13 * 132))
    var6 = i32_load16_u((var12 + (var13 * 132)) + 112)
    if (1 if var15 == 3 else 0):
        var2 = i32_load16_u(var1 + 114)
        var1 = i32_load(var0 + 28)
        break
    var5 = i32_load(9142840)
    var3 = (i32_load(9142440) + 2)
    var2 = i32_load16_u(var1 + 114)
    var8 = ((i32_load(9142440) + 2) + i32_load16_u(var1 + 114))
    var7 = (((i32_load(9142440) + 2) + i32_load16_u(var1 + 114)) * var3)
    var4 = i32_load((i32_load(9142840) + (((((i32_load(9142440) + 2) + i32_load16_u(var1 + 114)) * var3) + var6) << 2)))
    if (1 if i32_load((i32_load(9142840) + (((((i32_load(9142440) + 2) + i32_load16_u(var1 + 114)) * var3) + var6) << 2))) == 0 else 0):
        break
    var1 = i32_load(var0 + 28)
    if (1 if var4 == i32_load(var0 + 28) else 0):
        break
    var10 = (((var2 + 1) + var3) * var3)
    var4 = i32_load((var5 + (((((var2 + 1) + var3) * var3) + var6) << 2)))
    if (1 if i32_load((var5 + (((((var2 + 1) + var3) * var3) + var6) << 2))) == 0 else 0):
        break
    if (1 if var1 == var4 else 0):
        break
    var4 = i32_load((var5 + ((((var8 + 2) * var3) + var6) << 2)))
    if (1 if i32_load((var5 + ((((var8 + 2) * var3) + var6) << 2))) == 0 else 0):
        break
    if (1 if var1 == var4 else 0):
        break
    var4 = (var6 + 1)
    var11 = i32_load((var5 + (((var6 + 1) + var7) << 2)))
    if (1 if i32_load((var5 + (((var6 + 1) + var7) << 2))) == 0 else 0):
        break
    if (1 if var1 == var11 else 0):
        break
    var4 = i32_load((var5 + ((((var8 + 2) * var3) + var4) << 2)))
    if (1 if i32_load((var5 + ((((var8 + 2) * var3) + var4) << 2))) == 0 else 0):
        break
    if (1 if var1 == var4 else 0):
        break
    var4 = (var6 + 2)
    var7 = i32_load((var5 + ((var7 + (var6 + 2)) << 2)))
    if (1 if i32_load((var5 + ((var7 + (var6 + 2)) << 2))) == 0 else 0):
        break
    if (1 if var1 == var7 else 0):
        break
    var7 = i32_load((var5 + ((var4 + var10) << 2)))
    if (1 if i32_load((var5 + ((var4 + var10) << 2))) == 0 else 0):
        break
    if (1 if var1 == var7 else 0):
        break
    var5 = i32_load((var5 + ((((var8 + 2) * var3) + var4) << 2)))
    if (1 if i32_load((var5 + ((((var8 + 2) * var3) + var4) << 2))) == 0 else 0):
        break
    if (1 if var1 == var5 else 0):
        break
    if (1 if i32_load(((var9 * 404) + 9568096) + 224) > 1 else 0):
        break
    var1 = func250(var6, var2, var1)
    if (1 if func250(var6, var2, var1) == 0 else 0):
        break
    i32_store(var0 + 32, var1)
    i32_store(var0 + 56, 0)
    return 0
    var5 = 0
    var1 = i32_load(((var9 * 404) + 9568096) + 228)
    if (1 if i32_load(((var9 * 404) + 9568096) + 228) == 0 else 0):
        break
    var4 = i32_load(((var14 * 404) + 9568096) + 216)
    if (1 if i32_load(((var14 * 404) + 9568096) + 216) == 0 else 0):
        break
    var16 = (var4 & -4)
    var11 = (var4 & 3)
    var2 = (var12 + (var13 * 132))
    var17 = i32_load16_u((var12 + (var13 * 132)) + 114)
    var6 = i32_load16_u(var2 + 112)
    var3 = (var1 * var1)
    var18 = i32_load16_u(var0 + 114)
    var9 = i32_load16_u(var0 + 112)
    var19 = (1 if var4 < 4 else 0)
    var10 = 0
    var2 = 1
    while True:  # loop $label7
        var1 = (var18 - (var10 + var17))
        var8 = ((var18 - (var10 + var17)) * var1)
        var1 = 0
        var7 = 0
        if (1 if var19 == 0 else 0):
            while True:  # loop $label5
                var2 = (var9 - (var1 + var6))
                var2 = (var9 - ((var1 | 1) + var6))
                var2 = (var9 - ((var1 | 2) + var6))
                var2 = (var9 - ((var1 | 3) + var6))
                var2 = ((((var2 if (1 if (var8 + ((var9 - (var1 + var6)) * var2)) < var3 else 0) else 0) if (1 if (var8 + ((var9 - ((var1 | 1) + var6)) * var2)) < var3 else 0) else 0) if (1 if (var8 + ((var9 - ((var1 | 2) + var6)) * var2)) < var3 else 0) else 0) if (1 if (var8 + ((var9 - ((var1 | 3) + var6)) * var2)) < var3 else 0) else 0)
                var1 = (var1 + 4)
                var7 = (var7 + 4)
                if (1 if (var7 + 4) != var16 else 0):
                    continue
                break  # end loop
        var7 = 0
        if var11:
            while True:  # loop $label6
                var2 = (var9 - (var1 + var6))
                var2 = (var2 if (1 if (var8 + ((var9 - (var1 + var6)) * var2)) < var3 else 0) else 0)
                var1 = (var1 + 1)
                var7 = (var7 + 1)
                if (1 if (var7 + 1) != var11 else 0):
                    continue
                break  # end loop
        var10 = (var10 + 1)
        if (1 if (var10 + 1) != var4 else 0):
            continue
        break  # end loop
    var2 = (var2 & 1)
    var1 = (var12 + (var13 * 132))
    if (1 if var15 == 10 else 0):
        break
    if (1 if var15 == 3 else 0):
        break
    if i32_load(var1 + 36):
        break
    if i32_load8_u(var1 + 128):
        break
    if (1 if var2 == 0 else 0):
        break
    var1 = func106(var0, (-1 if (1 if i32_load8_u(var0 + 129) != 9 else 0) else var14), i32_load16_u(var1 + 112), i32_load16_u(var1 + 114))
    if func106(var0, (-1 if (1 if i32_load8_u(var0 + 129) != 9 else 0) else var14), i32_load16_u(var1 + 112), i32_load16_u(var1 + 114)):
        i32_store(var0 + 32, var1)
        i32_store(var0 + 56, 0)
        if i32_load8_u(var0 + 129):
            break
        i32_store8(var0 + 129, 5)
        return 0
    if (1 if i32_load8_u(var0 + 129) == 5 else 0):
        if func200(var0, 0, 1, 0):
            break
    var5 = 1
    return var5

