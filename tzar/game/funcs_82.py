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
# $func235
# ==========================================================
def func235(var0, var1, var2, var3, var4):
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
    var24 = 0
    var25 = 0
    var26 = 0
    var27 = 0
    var28 = 0
    var29 = 0
    var30 = 0
    var31 = 0
    var17 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var12 = i32_load16_u(var3 + 112)
    var25 = i32_load8_u(var3 + 122)
    if (1 if i32_load8_u(var3 + 122) == 20 else 0):
        var2 = 0
        var3 = i32_load16_u(var3 + 114)
        var4 = (i32_load(9142440) + 2)
        if i32_load((i32_load(9142840) + ((var12 + (((i32_load16_u(var3 + 114) + (i32_load(9142440) + 2)) + 2) * var4)) << 2)) + 8):
            break
        var2 = 1
        i32_store(var0, (var12 + 1))
        i32_store(var1, (var3 + 1))
        break
    var26 = i32_load8_u(var2 + 122)
    var6 = ((i32_load8_u(var2 + 122) * 404) + 9568096)
    var20 = i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 212)
    var21 = i32_load(var6 + 208)
    var23 = i32_load16_u(var2 + 114)
    var27 = i32_load16_u(var2 + 112)
    var24 = (var12 - 1)
    var14 = i32_load16_u(var3 + 114)
    var22 = (i32_load16_u(var3 + 114) - 1)
    if (1 if i32_load(((var25 * 404) + 9568096) + 264) == 2 else 0):
        var2 = 1
        var8 = i32_load(9142840)
        var6 = (var12 + 1)
        var4 = (var14 + 1)
        var5 = i32_load(9142440)
        var3 = (i32_load(9142440) + 2)
        if (1 if i32_load((i32_load(9142840) + (((var12 + 1) + (((var14 + 1) + (i32_load(9142440) + 2)) * var3)) << 2))) == 0 else 0):
            i32_store(var0, var12)
            i32_store(var1, var14)
            break
        var2 = (var24 - var27)
        var7 = ((var24 - var27) * var2)
        var2 = 2147483647
        if (1 if var5 <= var22 else 0):
            break
        if (1 if (var22 | var24) < 0 else 0):
            break
        if (1 if var5 <= var24 else 0):
            break
        if (1 if i32_load((var8 + (((((var3 * var21) + var14) * var3) + var12) << 2))) != var20 else 0):
            break
        var3 = (var22 - var23)
        var3 = (((var22 - var23) * var3) + var7)
        if (1 if (((var22 - var23) * var3) + var7) == 2147483647 else 0):
            break
        i32_store(var0, var24)
        i32_store(var1, var22)
        var5 = i32_load(9142440)
        var2 = var3
        if (1 if var5 <= var14 else 0):
            break
        if (1 if var12 == 0 else 0):
            break
        if (1 if var5 <= var24 else 0):
            break
        var3 = (var5 + 2)
        if (1 if i32_load((var8 + ((((var4 + ((var5 + 2) * var21)) * var3) + var12) << 2))) != var20 else 0):
            break
        var3 = (var14 - var23)
        var3 = (((var14 - var23) * var3) + var7)
        if (1 if (((var14 - var23) * var3) + var7) >= var2 else 0):
            break
        i32_store(var0, var24)
        i32_store(var1, var14)
        var5 = i32_load(9142440)
        var2 = var3
        if (1 if var4 >= var5 else 0):
            break
        if (1 if (var4 | var24) < 0 else 0):
            break
        if (1 if var5 <= var24 else 0):
            break
        var3 = (var5 + 2)
        if (1 if i32_load((var8 + (((((var14 + ((var5 + 2) * var21)) + 2) * var3) + var12) << 2))) != var20 else 0):
            break
        var3 = (var4 - var23)
        var3 = (((var4 - var23) * var3) + var7)
        if (1 if (((var4 - var23) * var3) + var7) >= var2 else 0):
            break
        i32_store(var0, var24)
        i32_store(var1, var4)
        var5 = i32_load(9142440)
        var2 = var3
        var3 = (var12 - var27)
        var7 = ((var12 - var27) * var3)
        if (1 if var5 <= var22 else 0):
            break
        if (1 if var14 == 0 else 0):
            break
        if (1 if var5 <= var12 else 0):
            break
        var3 = (var5 + 2)
        if (1 if i32_load((var8 + ((var6 + ((((var5 + 2) * var21) + var14) * var3)) << 2))) != var20 else 0):
            break
        var3 = (var22 - var23)
        var3 = (((var22 - var23) * var3) + var7)
        if (1 if (((var22 - var23) * var3) + var7) >= var2 else 0):
            break
        i32_store(var0, var12)
        i32_store(var1, var22)
        var5 = i32_load(9142440)
        var2 = var3
        if (1 if var5 <= var14 else 0):
            break
        if (1 if var5 <= var12 else 0):
            break
        var3 = (var5 + 2)
        if (1 if i32_load((var8 + ((var6 + ((var4 + ((var5 + 2) * var21)) * var3)) << 2))) != var20 else 0):
            break
        var3 = (var14 - var23)
        var3 = (((var14 - var23) * var3) + var7)
        if (1 if (((var14 - var23) * var3) + var7) >= var2 else 0):
            break
        i32_store(var0, var12)
        i32_store(var1, var14)
        var5 = i32_load(9142440)
        var2 = var3
        if (1 if var4 >= var5 else 0):
            break
        if (1 if var5 <= var12 else 0):
            break
        var3 = (var5 + 2)
        if (1 if i32_load((var8 + ((var6 + (((var14 + ((var5 + 2) * var21)) + 2) * var3)) << 2))) != var20 else 0):
            break
        var3 = (var4 - var23)
        var3 = (((var4 - var23) * var3) + var7)
        if (1 if (((var4 - var23) * var3) + var7) >= var2 else 0):
            break
        i32_store(var0, var12)
        i32_store(var1, var4)
        var5 = i32_load(9142440)
        var2 = var3
        var12 = (var12 + 2)
        var3 = (var6 - var27)
        var7 = ((var6 - var27) * var3)
        if (1 if var5 <= var22 else 0):
            break
        if (1 if (var6 | var22) < 0 else 0):
            break
        if (1 if var5 <= var6 else 0):
            break
        var3 = (var5 + 2)
        if (1 if i32_load((var8 + ((var12 + ((((var5 + 2) * var21) + var14) * var3)) << 2))) != var20 else 0):
            break
        var3 = (var22 - var23)
        var3 = (((var22 - var23) * var3) + var7)
        if (1 if (((var22 - var23) * var3) + var7) >= var2 else 0):
            break
        i32_store(var0, var6)
        i32_store(var1, var22)
        var5 = i32_load(9142440)
        var2 = var3
        if (1 if var5 <= var14 else 0):
            break
        if (1 if var5 <= var6 else 0):
            break
        var3 = (var5 + 2)
        if (1 if i32_load((var8 + ((var12 + ((var4 + ((var5 + 2) * var21)) * var3)) << 2))) != var20 else 0):
            break
        var3 = (var14 - var23)
        var3 = (((var14 - var23) * var3) + var7)
        if (1 if (((var14 - var23) * var3) + var7) >= var2 else 0):
            break
        i32_store(var0, var6)
        i32_store(var1, var14)
        var5 = i32_load(9142440)
        var2 = var3
        if (1 if var4 >= var5 else 0):
            break
        if (1 if var5 <= var6 else 0):
            break
        var3 = (var5 + 2)
        if (1 if i32_load((var8 + ((var12 + (((var14 + ((var5 + 2) * var21)) + 2) * var3)) << 2))) != var20 else 0):
            break
        var3 = (var4 - var23)
        var3 = (((var4 - var23) * var3) + var7)
        if (1 if (((var4 - var23) * var3) + var7) >= var2 else 0):
            break
        i32_store(var0, var6)
        i32_store(var1, var4)
        var2 = var3
        var2 = (1 if var2 != 2147483647 else 0)
        break
    if (1 if var25 != i32_load(38508) else 0):
        if (1 if i32_load(38504) != var25 else 0):
            break
    # br_table ['$label11', '$label10', '$label10', '$label11', '$label10']
    _br_idx = (i32_load8_u(var2 + 129) - 1)
    break  # br_table
    var29 = ((var26 * 404) + 9568312)
    var5 = i32_load(9142440)
    var6 = 0
    while True:  # loop $label29
        var8 = var6
        var6 = (var6 << 2)
        var9 = (i32_load((((var6 << 2) | 4) + 9488)) + i32_load16_u(var3 + 114))
        var10 = ((i32_load((((var6 << 2) | 4) + 9488)) + i32_load16_u(var3 + 114)) - 1)
        if (1 if var5 <= ((i32_load((((var6 << 2) | 4) + 9488)) + i32_load16_u(var3 + 114)) - 1) else 0):
            break
        var7 = (i32_load((var6 + 9488)) + i32_load16_u(var3 + 112))
        var13 = ((i32_load((var6 + 9488)) + i32_load16_u(var3 + 112)) - 1)
        if (1 if var5 <= ((i32_load((var6 + 9488)) + i32_load16_u(var3 + 112)) - 1) else 0):
            break
        if (1 if (var10 | var13) < 0 else 0):
            break
        var15 = i32_load(9142840)
        var6 = (var5 + 2)
        if i32_load((i32_load(9142840) + (((((var5 + 2) + var9) * var6) + var7) << 2))):
            break
        if var4:
            i32_store(var17 + 4, 0)
            i32_store8(var17 + 3, 0)
            var6 = func177(i32_load16_u(var2 + 112), i32_load16_u(var2 + 114), var13, var10, var20, var21, (var17 + 12), (var17 + 8), i32_load(var29), (var17 + 4), (var17 + 3), 0)
            var5 = i32_load(9142440)
            if (1 if var6 == 0 else 0):
                break
            var15 = i32_load(9142840)
        var6 = (var5 + 2)
        var18 = i32_load16_u(var2 + 110)
        var19 = i32_load(9671128)
        var30 = (1 if var5 <= var10 else 0)
        if (1 if var5 <= var10 else 0):
            break
        if (1 if var5 <= var7 else 0):
            break
        if (1 if (var7 | var10) < 0 else 0):
            break
        var11 = (var19 + (i32_load((((var7 + ((var6 + var9) * var6)) << 2) + var15) + 4) * 132))
        if (1 if i32_load16_u((var19 + (i32_load((((var7 + ((var6 + var9) * var6)) << 2) + var15) + 4) * 132)) + 110) != var18 else 0):
            break
        # br_table ['$label14', '$label13', '$label13', '$label14', '$label13']
        _br_idx = i32_load(((i32_load8_u(var11 + 122) * 404) + 9568096) + 192)
        break  # br_table
        if (1 if i32_load8_u(var11 + 125) == 0 else 0):
            break
        var16 = (var9 - 2)
        var28 = (1 if var5 <= (var9 - 2) else 0)
        if (1 if var5 <= (var9 - 2) else 0):
            break
        if (1 if var5 <= var7 else 0):
            break
        if (1 if (var7 | var16) < 0 else 0):
            break
        var11 = (var19 + (i32_load((((var7 + ((var6 + var10) * var6)) << 2) + var15) + 4) * 132))
        if (1 if i32_load16_u((var19 + (i32_load((((var7 + ((var6 + var10) * var6)) << 2) + var15) + 4) * 132)) + 110) != var18 else 0):
            break
        # br_table ['$label17', '$label16', '$label16', '$label17', '$label16']
        _br_idx = i32_load(((i32_load8_u(var11 + 122) * 404) + 9568096) + 192)
        break  # br_table
        if (1 if i32_load8_u(var11 + 125) == 0 else 0):
            break
        if var28:
            break
        if (1 if var5 <= var13 else 0):
            break
        if (1 if (var13 | var16) < 0 else 0):
            break
        var11 = (var19 + (i32_load((var15 + ((var7 + ((var6 + var10) * var6)) << 2))) * 132))
        if (1 if i32_load16_u((var19 + (i32_load((var15 + ((var7 + ((var6 + var10) * var6)) << 2))) * 132)) + 110) != var18 else 0):
            break
        # br_table ['$label19', '$label18', '$label18', '$label19', '$label18']
        _br_idx = i32_load(((i32_load8_u(var11 + 122) * 404) + 9568096) + 192)
        break  # br_table
        if (1 if i32_load8_u(var11 + 125) == 0 else 0):
            break
        var11 = (var7 - 2)
        if var28:
            break
        if (1 if var5 <= var11 else 0):
            break
        if (1 if (var11 | var16) < 0 else 0):
            break
        var16 = (var19 + (i32_load((var15 + ((var13 + ((var6 + var10) * var6)) << 2))) * 132))
        if (1 if i32_load16_u((var19 + (i32_load((var15 + ((var13 + ((var6 + var10) * var6)) << 2))) * 132)) + 110) != var18 else 0):
            break
        # br_table ['$label21', '$label20', '$label20', '$label21', '$label20']
        _br_idx = i32_load(((i32_load8_u(var16 + 122) * 404) + 9568096) + 192)
        break  # br_table
        if (1 if i32_load8_u(var16 + 125) == 0 else 0):
            break
        if var30:
            break
        if (1 if var5 <= var11 else 0):
            break
        if (1 if (var10 | var11) < 0 else 0):
            break
        var16 = (var19 + (i32_load((var15 + ((var13 + ((var6 + var9) * var6)) << 2))) * 132))
        if (1 if i32_load16_u((var19 + (i32_load((var15 + ((var13 + ((var6 + var9) * var6)) << 2))) * 132)) + 110) != var18 else 0):
            break
        # br_table ['$label23', '$label22', '$label22', '$label23', '$label22']
        _br_idx = i32_load(((i32_load8_u(var16 + 122) * 404) + 9568096) + 192)
        break  # br_table
        if (1 if i32_load8_u(var16 + 125) == 0 else 0):
            break
        var16 = (1 if var5 <= var9 else 0)
        if (1 if var5 <= var9 else 0):
            break
        if (1 if var5 <= var11 else 0):
            break
        if (1 if (var9 | var11) < 0 else 0):
            break
        var11 = (var19 + (i32_load((var15 + ((var13 + (((var6 + var9) + 1) * var6)) << 2))) * 132))
        if (1 if i32_load16_u((var19 + (i32_load((var15 + ((var13 + (((var6 + var9) + 1) * var6)) << 2))) * 132)) + 110) != var18 else 0):
            break
        # br_table ['$label25', '$label24', '$label24', '$label25', '$label24']
        _br_idx = i32_load(((i32_load8_u(var11 + 122) * 404) + 9568096) + 192)
        break  # br_table
        if (1 if i32_load8_u(var11 + 125) == 0 else 0):
            break
        if var16:
            break
        if (1 if var5 <= var13 else 0):
            break
        if (1 if (var9 | var13) < 0 else 0):
            break
        var11 = (var19 + (i32_load((var15 + ((var7 + (((var6 + var9) + 1) * var6)) << 2))) * 132))
        if (1 if i32_load16_u((var19 + (i32_load((var15 + ((var7 + (((var6 + var9) + 1) * var6)) << 2))) * 132)) + 110) != var18 else 0):
            break
        # br_table ['$label27', '$label26', '$label26', '$label27', '$label26']
        _br_idx = i32_load(((i32_load8_u(var11 + 122) * 404) + 9568096) + 192)
        break  # br_table
        if (1 if i32_load8_u(var11 + 125) == 0 else 0):
            break
        if var16:
            break
        if (1 if var5 <= var7 else 0):
            break
        if (1 if (var7 | var9) < 0 else 0):
            break
        var6 = (var19 + (i32_load((((var7 + (((var6 + var9) + 1) * var6)) << 2) + var15) + 4) * 132))
        if (1 if i32_load16_u((var19 + (i32_load((((var7 + (((var6 + var9) + 1) * var6)) << 2) + var15) + 4) * 132)) + 110) != var18 else 0):
            break
        # br_table ['$label28', '$label12', '$label12', '$label28', '$label12']
        _br_idx = i32_load(((i32_load8_u(var6 + 122) * 404) + 9568096) + 192)
        break  # br_table
        if i32_load8_u(var6 + 125):
            break
        i32_store(var0, var13)
        i32_store(var1, var10)
        var2 = 1
        break
        var6 = (var8 + 2)
        if (1 if var8 < 38 else 0):
            continue
        break  # end loop
    var6 = ((var25 * 404) + 9568096)
    var13 = (i32_load(((var25 * 404) + 9568096) + 220) + 2)
    var7 = (i32_load(var6 + 216) + 2)
    if (1 if var4 == 0 else 0):
        break
    var3 = (var7 * var13)
    if (1 if (var7 * var13) == 0 else 0):
        break
    # Unknown: memory.fill []
    var3 = 2147483647
    var28 = i32_load(var6 + 60)
    if i32_load(var6 + 60):
        var29 = ((var26 * 404) + 9568312)
        var30 = ((var25 * 404) + 9568152)
        var5 = 0
        while True:  # loop $label41
            var6 = i32_load(var30)
            var9 = (var5 << 2)
            var8 = i32_load((i32_load(var30) + ((var5 << 2) | 4)))
            var18 = (i32_load((i32_load(var30) + ((var5 << 2) | 4))) + var22)
            var10 = ((i32_load((i32_load(var30) + ((var5 << 2) | 4))) + var22) - var23)
            var9 = i32_load((var6 + var9))
            var19 = (i32_load((var6 + var9)) + var24)
            var6 = ((i32_load((var6 + var9)) + var24) - var27)
            var6 = ((((i32_load((i32_load(var30) + ((var5 << 2) | 4))) + var22) - var23) * var10) + (((i32_load((var6 + var9)) + var24) - var27) * var6))
            if (1 if ((((i32_load((i32_load(var30) + ((var5 << 2) | 4))) + var22) - var23) * var10) + (((i32_load((var6 + var9)) + var24) - var27) * var6)) >= var3 else 0):
                break
            var10 = i32_load(9142440)
            if (1 if i32_load(9142440) <= var18 else 0):
                break
            if (1 if (var18 | var19) < 0 else 0):
                break
            if (1 if var10 <= var19 else 0):
                break
            var10 = (var10 + 2)
            var10 = i32_load((i32_load(9142840) + (((var9 + var12) + (((var8 + var14) + ((var10 + 2) * var21)) * var10)) << 2)))
            if (1 if var20 != i32_load((i32_load(9142840) + (((var9 + var12) + (((var8 + var14) + ((var10 + 2) * var21)) * var10)) << 2))) else 0):
                if (1 if var10 == -1 else 0):
                    break
                if (1 if i32_load8_u((i32_load(9671128) + (var10 * 132)) + 125) != 1 else 0):
                    break
            if (1 if var4 == 0 else 0):
                break
            if (1 if var5 == 0 else 0):
                break
            var10 = (var9 + 1)
            var16 = (1 if var9 < -1 else 0)
            if (1 if var9 < -1 else 0):
                break
            if (1 if var8 < 0 else 0):
                break
            if (1 if var7 <= var10 else 0):
                break
            if (1 if var8 >= var13 else 0):
                break
            # br_table ['$label31', '$label32', '$label34']
            _br_idx = (i32_load(((((var7 * var8) + var10) << 2) + 8451904)) - 1)
            break  # br_table
            var11 = (var8 - 1)
            var31 = (1 if var9 < 0 else 0)
            if (1 if var9 < 0 else 0):
                break
            if (1 if var8 <= 0 else 0):
                break
            if (1 if var7 <= var9 else 0):
                break
            if (1 if var8 > var13 else 0):
                break
            # br_table ['$label31', '$label32', '$label35']
            _br_idx = (i32_load(((((var7 * var11) + var9) << 2) + 8451904)) - 1)
            break  # br_table
            var25 = (var9 - 1)
            var26 = (1 if var9 <= 0 else 0)
            if (1 if var9 <= 0 else 0):
                break
            if (1 if var8 < 0 else 0):
                break
            if (1 if var7 < var9 else 0):
                break
            if (1 if var8 >= var13 else 0):
                break
            # br_table ['$label31', '$label32', '$label36']
            _br_idx = (i32_load(((((var7 * var8) + var25) << 2) + 8451904)) - 1)
            break  # br_table
            var15 = (var8 + 1)
            if var31:
                break
            if (1 if var8 < -1 else 0):
                break
            if (1 if var7 <= var9 else 0):
                break
            if (1 if var13 <= var15 else 0):
                break
            # br_table ['$label31', '$label32', '$label37']
            _br_idx = (i32_load(((((var7 * var15) + var9) << 2) + 8451904)) - 1)
            break  # br_table
            if var16:
                break
            if (1 if var8 <= 0 else 0):
                break
            if (1 if var7 <= var10 else 0):
                break
            if (1 if var8 > var13 else 0):
                break
            # br_table ['$label31', '$label32', '$label38']
            _br_idx = (i32_load(((((var7 * var11) + var10) << 2) + 8451904)) - 1)
            break  # br_table
            if var26:
                break
            if (1 if var8 <= 0 else 0):
                break
            if (1 if var7 < var9 else 0):
                break
            if (1 if var8 > var13 else 0):
                break
            # br_table ['$label31', '$label32', '$label39']
            _br_idx = (i32_load(((((var7 * var11) + var25) << 2) + 8451904)) - 1)
            break  # br_table
            if var26:
                break
            if (1 if var8 < -1 else 0):
                break
            if (1 if var7 < var9 else 0):
                break
            if (1 if var13 <= var15 else 0):
                break
            # br_table ['$label31', '$label32', '$label40']
            _br_idx = (i32_load(((((var7 * var15) + var25) << 2) + 8451904)) - 1)
            break  # br_table
            if var16:
                break
            if (1 if var8 < -1 else 0):
                break
            if (1 if var7 <= var10 else 0):
                break
            if (1 if var13 <= var15 else 0):
                break
            # br_table ['$label31', '$label32', '$label33']
            _br_idx = (i32_load(((((var7 * var15) + var10) << 2) + 8451904)) - 1)
            break  # br_table
            i32_store(var17 + 4, 0)
            i32_store8(var17 + 3, 0)
            var8 = func177(i32_load16_u(var2 + 112), i32_load16_u(var2 + 114), var19, var18, var20, var21, (var17 + 12), (var17 + 8), i32_load(var29), (var17 + 4), (var17 + 3), 1)
            i32_store(((((var7 * var8) + var9) << 2) + 8451904), (2 if func177(i32_load16_u(var2 + 112), i32_load16_u(var2 + 114), var19, var18, var20, var21, (var17 + 12), (var17 + 8), i32_load(var29), (var17 + 4), (var17 + 3), 1) else 1))
            if (1 if var8 == 0 else 0):
                break
            i32_store(var0, var19)
            i32_store(var1, var18)
            var3 = var6
            var5 = (var5 + 2)
            if (1 if (var5 + 2) < var28 else 0):
                continue
            break  # end loop
    var2 = (1 if var3 != 2147483647 else 0)
    global global0
    global0 = (var17 + 16)
    return var2

