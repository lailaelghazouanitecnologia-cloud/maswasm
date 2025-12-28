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
# $func894
# ==========================================================
def func894(var0, var1):
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
    var4 = (i32_load(9671128) + (var1 * 132))
    var12 = ((1 if i32_load(38572) != i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122) else 0) << 1)
    var10 = i32_load(var4 + 52)
    var4 = 0
    var2 = i32_load(9142440)
    var0 = ((var0 & 0xFFFFFFFF) // i32_load(9142440))
    var8 = (var0 - (((var0 & 0xFFFFFFFF) // i32_load(9142440)) * var2))
    if (1 if ((var0 - (((var0 & 0xFFFFFFFF) // i32_load(9142440)) * var2)) | var0) < 0 else 0):
        break
    var2 = i32_load(9142440)
    var6 = (var0 if (1 if var0 > var8 else 0) else var8)
    if (1 if i32_load(9142440) <= (var0 if (1 if var0 > var8 else 0) else var8) else 0):
        break
    var3 = i32_load(9671128)
    var11 = (i32_load(9671128) + (var1 * 132))
    var5 = (var8 + 1)
    var9 = (var0 + 1)
    var1 = i32_load((i32_load(9142840) + (((var8 + 1) + ((var0 + 1) * (var2 + 2))) << 2)))
    if (1 if i32_load((i32_load(9142840) + (((var8 + 1) + ((var0 + 1) * (var2 + 2))) << 2))) >= 3 else 0):
        var4 = (var3 + (var1 * 132))
        var2 = i32_load8_u((var3 + (var1 * 132)) + 125)
        var7 = (((1 if i32_load8_u((var3 + (var1 * 132)) + 125) == 4 else 0) | (1 if var2 == 14 else 0)) & (1 if i32_load(var4 + 64) == 1 else 0))
        if (1 if var2 != 10 else 0):
        if var7:
            break
        i32_store(59200, i32_load((var3 + (var1 * 132)) + 28))
        var2 = i32_load(9142440)
        var4 = 1
    if (1 if var2 <= var6 else 0):
        break
    var3 = i32_load(9142840)
    var1 = (var2 + 2)
    var6 = i32_load((i32_load(9142840) + ((var5 + ((var9 + (var2 + 2)) * var1)) << 2)))
    if (1 if i32_load((i32_load(9142840) + ((var5 + ((var9 + (var2 + 2)) * var1)) << 2))) >= 3 else 0):
        var3 = i32_load(9671128)
        var1 = (i32_load(9671128) + (var6 * 132))
        var2 = i32_load8_u((i32_load(9671128) + (var6 * 132)) + 125)
        var7 = (((1 if i32_load8_u((i32_load(9671128) + (var6 * 132)) + 125) == 4 else 0) | (1 if var2 == 14 else 0)) & (1 if i32_load(var1 + 64) == 1 else 0))
        if (1 if var2 != 10 else 0):
        if var7:
            break
        i32_store(((var4 << 2) + 59200), i32_load((var3 + (var6 * 132)) + 28))
        var4 = (var4 + 1)
        var3 = i32_load(9142840)
        var2 = i32_load(9142440)
        var1 = (i32_load(9142440) + 2)
    if (1 if i32_load((var3 + (((var1 * var9) + var5) << 2))) != 1 else 0):
        break
    if (1 if i32_load((var3 + ((((var1 + var9) * var1) + var5) << 2))) == 1 else 0):
        break
    var6 = 0
    var7 = i32_load(((i32_load(9561692) + (i32_load(38560) << 2)) + 284636))
    if (1 if i32_load(((i32_load(9561692) + (i32_load(38560) << 2)) + 284636)) == 0 else 0):
        break
    var13 = i32_load(var7 + 8)
    if (1 if i32_load(var7 + 8) == 0 else 0):
        break
    while True:  # loop $label3
        var1 = i32_load((i32_load(var7) + (var6 << 2)))
        if (1 if i32_load((i32_load(var7) + (var6 << 2))) == 0 else 0):
            break
        var1 = (i32_load(9671128) + (var1 * 132))
        var2 = i32_load16_u((i32_load(9671128) + (var1 * 132)) + 112)
        if (1 if i32_load16_u((i32_load(9671128) + (var1 * 132)) + 112) >= var8 else 0):
            break
        var3 = i32_load16_u(var1 + 114)
        if (1 if i32_load16_u(var1 + 114) >= var0 else 0):
            break
        var14 = ((i32_load(38560) * 404) + 9568096)
        if (1 if (var2 + i32_load(((i32_load(38560) * 404) + 9568096) + 216)) <= var8 else 0):
            break
        if (1 if (i32_load(var14 + 220) + var3) <= var0 else 0):
            break
        var13 = i32_load(var7 + 8)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) < var13 else 0):
            continue
        break  # end loop
    var2 = i32_load(9142440)
    var1 = (i32_load(9142440) + 2)
    var3 = i32_load(9142840)
    if (1 if var12 == 0 else 0):
        break
    if (1 if i32_load((var3 + ((((var1 + var9) * var1) + var5) << 2))) == 1 else 0):
        break
    var1 = ((var12 << 1) | 1)
    var9 = (((((var12 << 1) | 1) * var1) << 1) - 2)
    if (1 if (((((var12 << 1) | 1) * var1) << 1) - 2) == 0 else 0):
        break
    var6 = 0
    while True:  # loop $label8
        var3 = (var6 << 2)
        var1 = (i32_load((((var6 << 2) | 4) + 8611904)) + var0)
        if (1 if var2 <= (i32_load((((var6 << 2) | 4) + 8611904)) + var0) else 0):
            break
        var5 = (i32_load((var3 + 8611904)) + var8)
        if (1 if var2 <= (i32_load((var3 + 8611904)) + var8) else 0):
            break
        if (1 if (var1 | var5) < 0 else 0):
            break
        var3 = i32_load(9142840)
        var7 = (var5 + 1)
        var13 = (var1 + 1)
        var1 = i32_load((i32_load(9142840) + (((var5 + 1) + ((var1 + 1) * (var2 + 2))) << 2)))
        if (1 if i32_load((i32_load(9142840) + (((var5 + 1) + ((var1 + 1) * (var2 + 2))) << 2))) < 3 else 0):
            break
        var5 = (i32_load(9671128) + (var1 * 132))
        if (1 if i32_load8_u((i32_load(9671128) + (var1 * 132)) + 125) == 10 else 0):
            break
        var1 = ((i32_load8_u(var5 + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u(var5 + 122) * 404) + 9568096) + 188) != 55 else 0):
            if (1 if i32_load(var1 + 264) == 1 else 0):
                break
        if var4:
            var14 = i32_load(var5 + 28)
            var1 = 0
            while True:  # loop $label6
                if (1 if i32_load(((var1 << 2) + 59200)) == var14 else 0):
                    break
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var4 else 0):
                    continue
                break  # end loop
        var1 = ((var10 & 0xFFFFFFFF) // var12)
        if (1 if ((var10 & 0xFFFFFFFF) // var12) == 0 else 0):
            break
        i32_store(((var4 << 2) + 59200), i32_load(var5 + 28))
        var4 = (var4 + 1)
        var3 = i32_load(9142840)
        var2 = i32_load(9142440)
        var1 = (var2 + 2)
        var1 = i32_load((var3 + ((var7 + ((var13 + (var2 + 2)) * var1)) << 2)))
        if (1 if i32_load((var3 + ((var7 + ((var13 + (var2 + 2)) * var1)) << 2))) < 3 else 0):
            break
        var3 = (i32_load(9671128) + (var1 * 132))
        if (1 if i32_load8_u((i32_load(9671128) + (var1 * 132)) + 125) == 10 else 0):
            break
        var1 = ((i32_load8_u(var3 + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 188) != 55 else 0):
            if (1 if i32_load(var1 + 264) == 1 else 0):
                break
        if var4:
            var5 = i32_load(var3 + 28)
            var1 = 0
            while True:  # loop $label7
                if (1 if i32_load(((var1 << 2) + 59200)) == var5 else 0):
                    break
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var4 else 0):
                    continue
                break  # end loop
        var1 = ((var10 & 0xFFFFFFFF) // var12)
        if (1 if ((var10 & 0xFFFFFFFF) // var12) == 0 else 0):
            break
        i32_store(((var4 << 2) + 59200), i32_load(var3 + 28))
        var4 = (var4 + 1)
        var2 = i32_load(9142440)
        var6 = (var6 + 2)
        if (1 if (var6 + 2) < var9 else 0):
            continue
        break  # end loop


# ==========================================================
# $func918
# ==========================================================
def func918(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var3 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var5 = i32_load(var0 + 4)
    var4 = 38932
    var7 = i32_load(var0)
    # br_table ['$label0', '$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label3', '$label4', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label5', '$label2']
    _br_idx = (i32_load(var0) - 15)
    break  # br_table
    var4 = 38728
    break
    var4 = 38724
    break
    var4 = 38936
    break
    var4 = 38940
    if (1 if i32_load(var4) == -1 else 0):
        break
    if (1 if var2 == 0 else 0):
        break
    var5 = ((var3 + 16) | ((1 if var5 == 0 else 0) << 3))
    var0 = 0
    while True:  # loop $label6
        var4 = i32_load((var1 + (var0 << 2)))
        var6 = i32_load(9671128)
        i64_store(var3 + 16, 8589934591)
        var4 = (var6 + (var4 * 132))
        i32_store(var3 + 24, i32_load16_u((var6 + (var4 * 132)) + 112))
        var6 = i32_load16_u(var4 + 114)
        i32_store(var3 + 48, 0)
        i64_store(var3 + 40, 0)
        i32_store(var3 + 36, var7)
        i32_store(var3 + 32, 0)
        i32_store(var3 + 28, var6)
        i32_store(var3 + 12, i32_load(var4 + 28))
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var2 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var3 - -64)


# ==========================================================
# $func920
# ==========================================================
def func920(var0, var1):
    var2 = 0
    var2 = i32_load(9671128)
    var1 = (i32_load(9671128) + (var1 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var1 * 132)) + 125) != 3 else 0):
        var0 = (var2 + (var0 * 132))

