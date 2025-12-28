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
# $func243
# ==========================================================
def func243(var0, var1, var2):
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
    var20 = 0
    var21 = 0
    var6 = (i32_load(9142892) * var2)
    var19 = i32_load(9142440)
    var10 = (i32_load(9142440) + 2)
    var21 = ((i32_load(9142440) + 2) << 1)
    var12 = i32_load(38564)
    var13 = i32_load(38620)
    var14 = i32_load(38560)
    var7 = i32_load(9143004)
    var15 = i32_load(38500)
    var16 = i32_load(9671128)
    var17 = i32_load(9142840)
    var2 = 0
    while True:  # loop $label7
        var20 = var2
        var3 = (var2 << 2)
        var2 = (i32_load((((var2 << 2) | 4) + 8611904)) + var1)
        if (1 if var19 <= (i32_load((((var2 << 2) | 4) + 8611904)) + var1) else 0):
            break
        var3 = (i32_load((var3 + 8611904)) + var0)
        if (1 if var19 <= (i32_load((var3 + 8611904)) + var0) else 0):
            break
        if (1 if (var2 | var3) < 0 else 0):
            break
        var8 = (var3 + 1)
        var11 = (var2 + 1)
        var2 = i32_load((var17 + (((var3 + 1) + ((var2 + 1) * var10)) << 2)))
        if (1 if i32_load((var17 + (((var3 + 1) + ((var2 + 1) * var10)) << 2))) < 3 else 0):
            break
        var3 = (var16 + (var2 * 132))
        if (1 if i32_load((var16 + (var2 * 132)) + 64) >= i32_load(var3 + 68) else 0):
            break
        var4 = i32_load8_u(var3 + 122)
        var9 = ((i32_load8_u(var3 + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 300) == 0 else 0):
            break
        if (1 if var4 == var15 else 0):
            break
        var5 = i32_load16_u(var3 + 110)
        var18 = i32_load16_u(var3 + 120)
        if i32_load16_u(var3 + 120):
        else:
        if (1 if i32_load8_u(((var18 if i32_load8_u((var7 + (var5 + var6))) else var5) + (var5 + var6))) == 0 else 0):
            if (1 if i32_load8_u(var3 + 127) != 6 else 0):
                break
            if (1 if i32_load8_u(var3 + 128) == 0 else 0):
                break
            break
        if i32_load8_u(var3 + 128):
            break
        if (1 if i32_load8_u(var3 + 125) == 10 else 0):
            break
        if (1 if i32_load8_u(var3 + 126) == 2 else 0):
            break
        if (1 if i32_load(var9 + 264) == 2 else 0):
            break
        if (1 if i32_load(var9 + 188) != 55 else 0):
            break
        if (1 if var4 == var14 else 0):
            break
        if (1 if var4 == var13 else 0):
            break
        if (1 if var4 == var12 else 0):
            break
        var2 = i32_load((var17 + ((var8 + ((var10 + var11) * var10)) << 2)))
        if (1 if i32_load((var17 + ((var8 + ((var10 + var11) * var10)) << 2))) < 3 else 0):
            break
        var3 = (var16 + (var2 * 132))
        if (1 if i32_load((var16 + (var2 * 132)) + 64) >= i32_load(var3 + 68) else 0):
            break
        var4 = i32_load8_u(var3 + 122)
        var9 = ((i32_load8_u(var3 + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 300) == 0 else 0):
            break
        if (1 if var4 == var15 else 0):
            break
        var5 = i32_load16_u(var3 + 110)
        var18 = i32_load16_u(var3 + 120)
        if i32_load16_u(var3 + 120):
        else:
        if i32_load8_u(((var18 if i32_load8_u((var7 + (var5 + var6))) else var5) + (var5 + var6))):
            if (1 if i32_load8_u(var3 + 128) == 0 else 0):
                break
            break
        if (1 if i32_load8_u(var3 + 127) != 6 else 0):
            break
        if i32_load8_u(var3 + 128):
            break
        if (1 if i32_load8_u(var3 + 125) == 10 else 0):
            break
        if (1 if i32_load8_u(var3 + 126) == 2 else 0):
            break
        if (1 if i32_load(var9 + 264) == 2 else 0):
            break
        if (1 if i32_load(var9 + 188) != 55 else 0):
            break
        if (1 if var4 == var14 else 0):
            break
        if (1 if var4 == var13 else 0):
            break
        if (1 if var4 == var12 else 0):
            break
        var2 = i32_load((var17 + ((var8 + ((var11 + var21) * var10)) << 2)))
        if (1 if i32_load((var17 + ((var8 + ((var11 + var21) * var10)) << 2))) < 3 else 0):
            break
        var3 = (var16 + (var2 * 132))
        if (1 if i32_load((var16 + (var2 * 132)) + 64) >= i32_load(var3 + 68) else 0):
            break
        var5 = i32_load8_u(var3 + 122)
        var8 = ((i32_load8_u(var3 + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 300) == 0 else 0):
            break
        if (1 if var5 == var15 else 0):
            break
        var4 = i32_load16_u(var3 + 110)
        var11 = i32_load16_u(var3 + 120)
        if i32_load16_u(var3 + 120):
        else:
        if i32_load8_u(((var11 if i32_load8_u((var7 + (var4 + var6))) else var4) + (var4 + var6))):
            if (1 if i32_load8_u(var3 + 128) == 0 else 0):
                break
            break
        if (1 if i32_load8_u(var3 + 127) != 6 else 0):
            break
        if i32_load8_u(var3 + 128):
            break
        if (1 if i32_load8_u(var3 + 125) == 10 else 0):
            break
        if (1 if i32_load8_u(var3 + 126) == 2 else 0):
            break
        if (1 if i32_load(var8 + 264) == 2 else 0):
            break
        if (1 if i32_load(var8 + 188) != 55 else 0):
            break
        if (1 if var5 == var14 else 0):
            break
        if (1 if var5 == var13 else 0):
            break
        if (1 if var5 == var12 else 0):
            break
        var2 = (var20 + 2)
        if (1 if var20 < 1678 else 0):
            continue
        break  # end loop
    var2 = 0
    return var2


# ==========================================================
# $func250
# ==========================================================
def func250(var0, var1, var2):
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
    var20 = 0
    var21 = 0
    var13 = i32_load(9142440)
    var5 = (i32_load(9142440) + 2)
    var20 = i32_load(38564)
    var14 = i32_load(9671128)
    var9 = i32_load(9142840)
    while True:  # loop $label10
        var15 = var3
        var3 = (var3 << 2)
        var7 = (i32_load((((var3 << 2) | 4) + 8611904)) + var1)
        if (1 if var13 <= (i32_load((((var3 << 2) | 4) + 8611904)) + var1) else 0):
            break
        var8 = (i32_load((var3 + 8611904)) + var0)
        if (1 if var13 <= (i32_load((var3 + 8611904)) + var0) else 0):
            break
        if (1 if (var7 | var8) < 0 else 0):
            break
        var16 = (var7 + 1)
        var21 = i32_load((((var8 + (((var7 + 1) + var5) * var5)) << 2) + var9) + 4)
        var3 = (var14 + (i32_load((((var8 + (((var7 + 1) + var5) * var5)) << 2) + var9) + 4) * 132))
        if (1 if var20 != i32_load8_u((var14 + (i32_load((((var8 + (((var7 + 1) + var5) * var5)) << 2) + var9) + 4) * 132)) + 122) else 0):
            break
        # br_table ['$label0', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label0', '$label1']
        _br_idx = (i32_load8_u(var3 + 125) - 4)
        break  # br_table
        var10 = (var8 + 2)
        var17 = (var8 if (1 if var8 > var10 else 0) else (var8 + 2))
        var11 = 1
        var18 = (var7 - 1)
        var4 = (var8 - 1)
        var19 = ((var5 + var7) * var5)
        var3 = (var7 + 2)
        var12 = (var7 if (1 if var3 < var7 else 0) else (var7 + 2))
        if ((1 if var16 == (var7 if (1 if var3 < var7 else 0) else (var7 + 2)) else 0) | (1 if var7 > 2147483645 else 0)):
            while True:  # loop $label5
                var6 = (var4 + 1)
                var3 = var18
                if (1 if var4 != var8 else 0):
                    while True:  # loop $label3
                        var3 = (var3 + 1)
                        var4 = i32_load((var9 + (((((var3 + 1) + var5) * var5) + var6) << 2)))
                        if (1 if i32_load((var9 + (((((var3 + 1) + var5) * var5) + var6) << 2))) == 0 else 0):
                            break
                        if (1 if var2 == var4 else 0):
                            break
                        if (1 if var3 != var12 else 0):
                            continue
                        break
                        break  # end loop
                    raise RuntimeError('unreachable')
                var3 = i32_load((var9 + ((var6 + var19) << 2)))
                if (1 if i32_load((var9 + ((var6 + var19) << 2))) == 0 else 0):
                    break
                if (1 if var2 == var3 else 0):
                    break
                var11 = (1 if var6 < var10 else 0)
                var4 = var6
                if (1 if var6 != var17 else 0):
                    continue
                break
                break  # end loop
            raise RuntimeError('unreachable')
        while True:  # loop $label9
            var6 = (var4 + 1)
            var3 = var18
            if (1 if var4 == var8 else 0):
                var4 = i32_load((var9 + ((var6 + var19) << 2)))
                if (1 if i32_load((var9 + ((var6 + var19) << 2))) == 0 else 0):
                    break
                var3 = var16
                if (1 if var2 == var4 else 0):
                    break
                while True:  # loop $label6
                    var4 = (var3 + 1)
                    if (1 if var3 != var7 else 0):
                        var3 = i32_load((var9 + ((((var4 + var5) * var5) + var6) << 2)))
                        if (1 if i32_load((var9 + ((((var4 + var5) * var5) + var6) << 2))) == 0 else 0):
                            break
                        if (1 if var2 == var3 else 0):
                            break
                    var3 = var4
                    if (1 if var4 != var12 else 0):
                        continue
                    break  # end loop
                break
            while True:  # loop $label8
                var3 = (var3 + 1)
                var4 = i32_load((var9 + (((((var3 + 1) + var5) * var5) + var6) << 2)))
                if (1 if i32_load((var9 + (((((var3 + 1) + var5) * var5) + var6) << 2))) == 0 else 0):
                    break
                if (1 if var2 == var4 else 0):
                    break
                if (1 if var3 != var12 else 0):
                    continue
                break  # end loop
            var11 = (1 if var6 < var10 else 0)
            var4 = var6
            if (1 if var6 != var17 else 0):
                continue
            break  # end loop
        if (1 if var11 == 0 else 0):
            break
        return i32_load((var14 + (var21 * 132)) + 28)
        var3 = (var15 + 2)
        if (1 if var15 < 878 else 0):
            continue
        break  # end loop
    return 0

