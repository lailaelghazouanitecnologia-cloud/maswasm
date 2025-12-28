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
# $func827
# ==========================================================
def func827(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = i32_load(9671128)
    var0 = (var1 + (var0 * 132))
    var1 = i32_load((var1 + (var0 * 132)) + 32)
    var3 = i32_load8_u((i32_load(9671128) + (i32_load((var1 + (var0 * 132)) + 32) * 132)) + 122)
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load((var1 + (var0 * 132)) + 32) * 132)) + 122) != i32_load(38448) else 0):
        break
    var1 = func335(i32_load16_u(var0 + 112), i32_load16_u(var0 + 114), var3, var1)
    if (1 if func335(i32_load16_u(var0 + 112), i32_load16_u(var0 + 114), var3, var1) == 0 else 0):
        break
    i32_store(var0 + 32, var1)
    func140(var0)
    var2 = 1
    return var2


# ==========================================================
# $func95
# ==========================================================
def func95(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    while True:  # loop $label9
        var3 = i32_load(9142440)
        var4 = ((i32_load(9142440) * var1) + var0)
        var6 = (((i32_load(9142440) * var1) + var0) + i32_load(9147288))
        var7 = i32_load8_u((((i32_load(9142440) * var1) + var0) + i32_load(9147288)))
        # Unknown: i32.extend8_s []
        var8 = i32_load8_u((((i32_load(9142440) * var1) + var0) + i32_load(9147288)))
        if (1 if i32_load8_u((((i32_load(9142440) * var1) + var0) + i32_load(9147288))) != var2 else 0):
            break
        var5 = func373(var0, var1, var2)
        if (1 if func373(var0, var1, var2) < 0 else 0):
            break
        if (1 if var2 <= var5 else 0):
            break
        if (1 if func410(var4, var5) != 55 else 0):
            break
        if (1 if var8 < 0 else 0):
            break
        if (1 if i32_load(i32_load((i32_load(9140332) + (var7 << 2))) + 32) != 23 else 0):
            break
        var4 = i32_load(9142840)
        var7 = (var0 + 1)
        var8 = (var1 + 1)
        i32_store((i32_load(9142840) + (((var0 + 1) + ((var1 + 1) * (var3 + 2))) << 2)), 0)
        var3 = (i32_load(9142440) + 2)
        i32_store((var4 + (((((i32_load(9142440) + 2) + var8) * var3) + var7) << 2)), 0)
        i32_store8(var6, var5)
        var5 = (var0 + 1)
        var3 = i32_load(9142440)
        if (1 if i32_load(9142440) <= var1 else 0):
            break
        if (1 if var3 <= var5 else 0):
            break
        if (1 if (var1 | var5) < 0 else 0):
            break
        func95(var5, var1, var2)
        var3 = i32_load(9142440)
        var6 = (var1 - 1)
        if (1 if var3 <= (var1 - 1) else 0):
            break
        if (1 if var3 <= var5 else 0):
            break
        if (1 if (var5 | var6) < 0 else 0):
            break
        func95(var5, var6, var2)
        var3 = i32_load(9142440)
        if (1 if var3 <= var6 else 0):
            break
        if (1 if var0 >= var3 else 0):
            break
        if (1 if (var0 | var6) < 0 else 0):
            break
        func95(var0, var6, var2)
        var3 = i32_load(9142440)
        var4 = (var0 - 1)
        if (1 if var3 <= var6 else 0):
            break
        if (1 if var3 <= var4 else 0):
            break
        if (1 if (var4 | var6) < 0 else 0):
            break
        func95(var4, var6, var2)
        var3 = i32_load(9142440)
        if (1 if var1 >= var3 else 0):
            break
        if (1 if var3 <= var4 else 0):
            break
        if (1 if (var1 | var4) < 0 else 0):
            break
        func95(var4, var1, var2)
        var3 = i32_load(9142440)
        var1 = (var1 + 1)
        if (1 if var3 <= (var1 + 1) else 0):
            break
        if (1 if var3 <= var4 else 0):
            break
        if (1 if (var1 | var4) < 0 else 0):
            break
        func95(var4, var1, var2)
        var3 = i32_load(9142440)
        if (1 if var1 >= var3 else 0):
            break
        if (1 if var0 >= var3 else 0):
            break
        if (1 if (var0 | var1) < 0 else 0):
            break
        func95(var0, var1, var2)
        var3 = i32_load(9142440)
        if (1 if var1 >= var3 else 0):
            break
        if (1 if var3 <= var5 else 0):
            break
        var0 = var5
        if (1 if (var5 | var1) >= 0 else 0):
            continue
        break  # end loop


# ==========================================================
# $func96
# ==========================================================
def func96(var0, var1, var2, var3):
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
    var20 = 0
    var21 = 0
    var22 = 0
    var23 = 0
    while True:  # loop $label17
        var6 = i32_load(9142440)
        var13 = (i32_load(9142440) * var1)
        var23 = ((i32_load(9142440) * var1) + var0)
        var15 = (i32_load(9142436) + (((i32_load(9142440) * var1) + var0) << 1))
        if (1 if i32_load16_u((i32_load(9142436) + (((i32_load(9142440) * var1) + var0) << 1))) == var3 else 0):
            break
        var7 = (var0 + 1)
        var16 = ((var0 + 1) | var1)
        var12 = i32_load(9147288)
        var4 = -1
        var8 = (1 if var1 >= var6 else 0)
        if (1 if var1 >= var6 else 0):
            break
        if (1 if var6 <= var7 else 0):
            break
        if (1 if var16 < 0 else 0):
            break
        var4 = i32_load8_s((var12 + (var7 + var13)))
        var4 = (-1 if (1 if var4 < 0 else 0) else (-1 if (1 if var2 == var4 else 0) else i32_load8_s((var12 + (var7 + var13)))))
        var10 = (var1 - 1)
        var17 = ((var1 - 1) | var7)
        var11 = 0
        var14 = (1 if var6 <= var10 else 0)
        if (1 if var6 <= var10 else 0):
            break
        if (1 if var6 <= var7 else 0):
            break
        if (1 if var17 < 0 else 0):
            break
        var5 = i32_load8_s((var12 + ((var6 * var10) + var7)))
        if (1 if i32_load8_s((var12 + ((var6 * var10) + var7))) < 0 else 0):
            break
        if (1 if var2 == var5 else 0):
            break
        if (1 if var4 == -1 else 0):
            var4 = var5
            break
        var11 = (1 if var4 != var5 else 0)
        var18 = (var0 | var10)
        if var14:
            break
        if (1 if var0 >= var6 else 0):
            break
        if (1 if var18 < 0 else 0):
            break
        var5 = i32_load8_s((var12 + ((var6 * var10) + var0)))
        if (1 if i32_load8_s((var12 + ((var6 * var10) + var0))) < 0 else 0):
            break
        if (1 if var2 == var5 else 0):
            break
        if (1 if var4 == -1 else 0):
            var4 = var5
            break
        var11 = (1 if (1 if var4 != var5 else 0) else var11)
        var9 = (var0 - 1)
        var19 = (var10 | (var0 - 1))
        if var14:
            break
        if (1 if var6 <= var9 else 0):
            break
        if (1 if var19 < 0 else 0):
            break
        var5 = i32_load8_s((var12 + ((var6 * var10) + var9)))
        if (1 if i32_load8_s((var12 + ((var6 * var10) + var9))) < 0 else 0):
            break
        if (1 if var2 == var5 else 0):
            break
        if (1 if var4 == -1 else 0):
            var4 = var5
            break
        var11 = (1 if (1 if var4 != var5 else 0) else var11)
        var20 = (var1 | var9)
        if var8:
            break
        if (1 if var6 <= var9 else 0):
            break
        if (1 if var20 < 0 else 0):
            break
        var5 = i32_load8_s((var12 + (var9 + var13)))
        if (1 if i32_load8_s((var12 + (var9 + var13))) < 0 else 0):
            break
        if (1 if var2 == var5 else 0):
            break
        if (1 if var4 == -1 else 0):
            var4 = var5
            break
        var11 = (1 if (1 if var4 != var5 else 0) else var11)
        var8 = (var1 + 1)
        var21 = ((var1 + 1) | var9)
        var22 = (1 if var6 <= var8 else 0)
        if (1 if var6 <= var8 else 0):
            break
        if (1 if var6 <= var9 else 0):
            break
        if (1 if var21 < 0 else 0):
            break
        var5 = i32_load8_s((var12 + ((var6 * var8) + var9)))
        if (1 if i32_load8_s((var12 + ((var6 * var8) + var9))) < 0 else 0):
            break
        if (1 if var2 == var5 else 0):
            break
        if (1 if var4 == -1 else 0):
            var4 = var5
            break
        var11 = (1 if (1 if var4 != var5 else 0) else var11)
        var13 = (var0 | var8)
        if var22:
            break
        if (1 if var0 >= var6 else 0):
            break
        if (1 if var13 < 0 else 0):
            break
        var5 = i32_load8_s((var12 + ((var6 * var8) + var0)))
        if (1 if i32_load8_s((var12 + ((var6 * var8) + var0))) < 0 else 0):
            break
        if (1 if var2 == var5 else 0):
            break
        if (1 if var4 == -1 else 0):
            var4 = var5
            break
        var11 = (1 if (1 if var4 != var5 else 0) else var11)
        var14 = (var7 | var8)
        if var22:
            break
        if (1 if var6 <= var7 else 0):
            break
        if (1 if var14 < 0 else 0):
            break
        var5 = i32_load8_s((var12 + ((var6 * var8) + var7)))
        if (1 if i32_load8_s((var12 + ((var6 * var8) + var7))) < 0 else 0):
            break
        if (1 if var2 == var5 else 0):
            break
        if (1 if var4 == -1 else 0):
            break
        var11 = (1 if (1 if var4 != var5 else 0) else var11)
        if (1 if var11 == 0 else 0):
            break
        if (1 if i32_load(9147292) >= var2 else 0):
            break
        i32_store16(var15, var3)
        var15 = (var12 + var23)
        var4 = i32_load8_s((var12 + var23))
        if (1 if i32_load8_s((var12 + var23)) < 0 else 0):
            break
        if (1 if i32_load(i32_load((i32_load(9140332) + ((var4 & 255) << 2))) + 32) != 23 else 0):
            break
        var5 = i32_load(9142840)
        i32_store((i32_load(9142840) + ((((var6 + 2) * var8) + var7) << 2)), 0)
        var4 = (i32_load(9142440) + 2)
        i32_store((var5 + (((((i32_load(9142440) + 2) + var8) * var4) + var7) << 2)), 0)
        i32_store8(var15, i32_load(9147292))
        var4 = i32_load(9142440)
        if (1 if i32_load(9142440) <= var7 else 0):
            break
        if (1 if var1 >= var4 else 0):
            break
        if (1 if var16 < 0 else 0):
            break
        if (1 if i32_load8_s((i32_load(9147288) + ((var1 * var4) + var7))) != var2 else 0):
            break
        func96(var7, var1, var2, var3)
        var4 = i32_load(9142440)
        if (1 if var4 <= var7 else 0):
            break
        if (1 if var4 <= var10 else 0):
            break
        if (1 if var17 < 0 else 0):
            break
        if (1 if i32_load8_s((i32_load(9147288) + ((var4 * var10) + var7))) != var2 else 0):
            break
        func96(var7, var10, var2, var3)
        var4 = i32_load(9142440)
        if (1 if var0 >= var4 else 0):
            break
        if (1 if var4 <= var10 else 0):
            break
        if (1 if var18 < 0 else 0):
            break
        if (1 if i32_load8_s((i32_load(9147288) + ((var4 * var10) + var0))) != var2 else 0):
            break
        func96(var0, var10, var2, var3)
        var4 = i32_load(9142440)
        if (1 if var4 <= var9 else 0):
            break
        if (1 if var4 <= var10 else 0):
            break
        if (1 if var19 < 0 else 0):
            break
        if (1 if i32_load8_s((i32_load(9147288) + ((var4 * var10) + var9))) != var2 else 0):
            break
        func96(var9, var10, var2, var3)
        var4 = i32_load(9142440)
        if (1 if var4 <= var9 else 0):
            break
        if (1 if var1 >= var4 else 0):
            break
        if (1 if var20 < 0 else 0):
            break
        if (1 if i32_load8_s((i32_load(9147288) + ((var1 * var4) + var9))) != var2 else 0):
            break
        func96(var9, var1, var2, var3)
        var4 = i32_load(9142440)
        if (1 if var4 <= var9 else 0):
            break
        if (1 if var4 <= var8 else 0):
            break
        if (1 if var21 < 0 else 0):
            break
        if (1 if i32_load8_s((i32_load(9147288) + ((var4 * var8) + var9))) != var2 else 0):
            break
        func96(var9, var8, var2, var3)
        var4 = i32_load(9142440)
        if (1 if var0 >= var4 else 0):
            break
        if (1 if var4 <= var8 else 0):
            break
        if (1 if var13 < 0 else 0):
            break
        if (1 if i32_load8_s((i32_load(9147288) + ((var4 * var8) + var0))) != var2 else 0):
            break
        func96(var0, var8, var2, var3)
        var4 = i32_load(9142440)
        if (1 if var4 <= var7 else 0):
            break
        if (1 if var4 <= var8 else 0):
            break
        if (1 if var14 < 0 else 0):
            break
        var0 = var7
        var1 = var8
        if (1 if i32_load8_s((i32_load(9147288) + (var7 + (var8 * var4)))) == var2 else 0):
            continue
        break  # end loop

