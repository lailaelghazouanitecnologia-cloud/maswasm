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
# $func194
# ==========================================================
def func194(var0, var1, var2, var3, var4, var5, var6):
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
    var7 = i32_load(var2 + 208)
    if var6:
        var6 = 0
        var14 = i32_load(9142440)
        var18 = (1 if i32_load(9142440) <= var1 else 0)
        if (1 if i32_load(9142440) <= var1 else 0):
            break
        var17 = (var0 | var1)
        if (1 if (var0 | var1) < 0 else 0):
            break
        if (1 if var0 >= var14 else 0):
            break
        var10 = i32_load(9142840)
        var16 = (var0 + 1)
        var11 = (var14 + 2)
        var7 = ((var14 + 2) * var7)
        var19 = (var1 + ((var14 + 2) * var7))
        var20 = ((var0 + 1) + (((var1 + ((var14 + 2) * var7)) + 1) * var11))
        if (1 if i32_load((i32_load(9142840) + (((var0 + 1) + (((var1 + ((var14 + 2) * var7)) + 1) * var11)) << 2))) != i32_load(var2 + 212) else 0):
            break
        if i32_load((((i32_load(9561692) + (var3 * 286704)) + (i32_load(38452) << 2)) + 281808)):
            break
        var8 = (var0 - 1)
        var15 = (var7 + 1)
        var12 = (var1 - 2)
        var13 = i32_load(38464)
        var7 = i32_load(9671128)
        var2 = (var0 - 2)
        if (1 if (var0 - 2) >= var14 else 0):
            break
        if (1 if var12 >= var14 else 0):
            break
        if (1 if (var2 | var12) < 0 else 0):
            break
        var9 = i32_load((var10 + ((var8 + ((var12 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var8 + ((var12 + var15) * var11)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var9 * 132))
        if (1 if i32_load16_u((var7 + (var9 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label2', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label2', '$label1']
        _br_idx = (i32_load8_u((var7 + (var9 * 132)) + 125) - 4)
        break  # br_table
        var6 = (var1 - 1)
        if (1 if var14 <= (var1 - 1) else 0):
            break
        if (1 if (var2 | var6) < 0 else 0):
            break
        var9 = i32_load((var10 + ((var8 + (var11 * var19)) << 2)))
        if (1 if i32_load((var10 + ((var8 + (var11 * var19)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var9 * 132))
        if (1 if i32_load16_u((var7 + (var9 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label3', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label3', '$label1']
        _br_idx = (i32_load8_u((var7 + (var9 * 132)) + 125) - 4)
        break  # br_table
        if var18:
            break
        if (1 if (var1 | var2) < 0 else 0):
            break
        var9 = i32_load((var10 + ((var8 + ((var1 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var8 + ((var1 + var15) * var11)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var9 * 132))
        if (1 if i32_load16_u((var7 + (var9 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label4', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label4', '$label1']
        _br_idx = (i32_load8_u((var7 + (var9 * 132)) + 125) - 4)
        break  # br_table
        var6 = (var1 + 1)
        if (1 if var14 <= (var1 + 1) else 0):
            break
        if (1 if (var2 | var6) < 0 else 0):
            break
        var9 = i32_load((var10 + ((var8 + ((var6 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var8 + ((var6 + var15) * var11)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var9 * 132))
        if (1 if i32_load16_u((var7 + (var9 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label5', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label5', '$label1']
        _br_idx = (i32_load8_u((var7 + (var9 * 132)) + 125) - 4)
        break  # br_table
        var9 = (var1 + 2)
        if (1 if (var1 + 2) >= var14 else 0):
            var6 = 0
            break
        var6 = 0
        if (1 if (var2 | var9) < 0 else 0):
            break
        var2 = i32_load((var10 + ((var8 + ((var9 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var8 + ((var9 + var15) * var11)) << 2))) < 3 else 0):
            break
        var9 = (var7 + (var2 * 132))
        if (1 if var3 != i32_load16_u((var7 + (var2 * 132)) + 110) else 0):
            break
        if (1 if var13 != i32_load8_u(var9 + 122) else 0):
            break
        var2 = i32_load8_u((var7 + (var2 * 132)) + 125)
        var6 = (0 - ((1 if i32_load8_u((var7 + (var2 * 132)) + 125) != 14 else 0) & (1 if var2 != 4 else 0)))
        if (1 if var8 >= var14 else 0):
            break
        if (1 if var12 >= var14 else 0):
            break
        if (1 if (var8 | var12) < 0 else 0):
            break
        var9 = i32_load((var10 + ((((var12 + var15) * var11) + var0) << 2)))
        if (1 if i32_load((var10 + ((((var12 + var15) * var11) + var0) << 2))) < 3 else 0):
            break
        var2 = (var7 + (var9 * 132))
        if (1 if i32_load16_u((var7 + (var9 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var2 + 122) else 0):
            break
        var2 = 1
        # br_table ['$label7', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label7', '$label8']
        _br_idx = (i32_load8_u((var7 + (var9 * 132)) + 125) - 4)
        break  # br_table
        var2 = (var1 - 1)
        if (1 if var14 <= (var1 - 1) else 0):
            break
        if (1 if (var2 | var8) < 0 else 0):
            break
        var9 = i32_load((var10 + (((var11 * var19) + var0) << 2)))
        if (1 if i32_load((var10 + (((var11 * var19) + var0) << 2))) < 3 else 0):
            break
        var2 = (var7 + (var9 * 132))
        if (1 if i32_load16_u((var7 + (var9 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var2 + 122) else 0):
            break
        var2 = 1
        # br_table ['$label9', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label9', '$label8']
        _br_idx = (i32_load8_u((var7 + (var9 * 132)) + 125) - 4)
        break  # br_table
        if var18:
            break
        if (1 if (var1 | var8) < 0 else 0):
            break
        var9 = i32_load((var10 + ((((var1 + var15) * var11) + var0) << 2)))
        if (1 if i32_load((var10 + ((((var1 + var15) * var11) + var0) << 2))) < 3 else 0):
            break
        var2 = (var7 + (var9 * 132))
        if (1 if i32_load16_u((var7 + (var9 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var2 + 122) else 0):
            break
        var2 = 1
        # br_table ['$label10', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label10', '$label8']
        _br_idx = (i32_load8_u((var7 + (var9 * 132)) + 125) - 4)
        break  # br_table
        var2 = (var1 + 1)
        if (1 if var14 <= (var1 + 1) else 0):
            break
        if (1 if (var2 | var8) < 0 else 0):
            break
        var9 = i32_load((var10 + ((((var2 + var15) * var11) + var0) << 2)))
        if (1 if i32_load((var10 + ((((var2 + var15) * var11) + var0) << 2))) < 3 else 0):
            break
        var2 = (var7 + (var9 * 132))
        if (1 if i32_load16_u((var7 + (var9 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var2 + 122) else 0):
            break
        var2 = 1
        # br_table ['$label11', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label11', '$label8']
        _br_idx = (i32_load8_u((var7 + (var9 * 132)) + 125) - 4)
        break  # br_table
        var2 = (var1 + 2)
        if (1 if var14 <= (var1 + 2) else 0):
            break
        if (1 if (var2 | var8) < 0 else 0):
            break
        var8 = i32_load((var10 + ((((var2 + var15) * var11) + var0) << 2)))
        if (1 if i32_load((var10 + ((((var2 + var15) * var11) + var0) << 2))) < 3 else 0):
            break
        var2 = (var7 + (var8 * 132))
        if (1 if i32_load16_u((var7 + (var8 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var2 + 122) else 0):
            break
        var2 = 1
        # br_table ['$label6', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label8', '$label6', '$label8']
        _br_idx = (i32_load8_u((var7 + (var8 * 132)) + 125) - 4)
        break  # br_table
        var2 = var6
        var9 = (1 if var12 >= var14 else 0)
        if (1 if var12 >= var14 else 0):
            break
        if (1 if (var0 | var12) < 0 else 0):
            break
        var8 = i32_load((var10 + ((var16 + ((var12 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var16 + ((var12 + var15) * var11)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var8 * 132))
        if (1 if i32_load16_u((var7 + (var8 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label12', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label12', '$label13']
        _br_idx = (i32_load8_u((var7 + (var8 * 132)) + 125) - 4)
        break  # br_table
        var6 = (var1 - 1)
        if (1 if var14 <= (var1 - 1) else 0):
            break
        if (1 if (var0 | var6) < 0 else 0):
            break
        var8 = i32_load((var10 + ((var16 + (var11 * var19)) << 2)))
        if (1 if i32_load((var10 + ((var16 + (var11 * var19)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var8 * 132))
        if (1 if i32_load16_u((var7 + (var8 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label14', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label14', '$label13']
        _br_idx = (i32_load8_u((var7 + (var8 * 132)) + 125) - 4)
        break  # br_table
        if var18:
            break
        if (1 if var17 < 0 else 0):
            break
        var8 = i32_load((var10 + ((var16 + ((var1 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var16 + ((var1 + var15) * var11)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var8 * 132))
        if (1 if i32_load16_u((var7 + (var8 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label15', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label15', '$label13']
        _br_idx = (i32_load8_u((var7 + (var8 * 132)) + 125) - 4)
        break  # br_table
        var6 = (var1 + 1)
        if (1 if var14 <= (var1 + 1) else 0):
            break
        if (1 if (var0 | var6) < 0 else 0):
            break
        var8 = i32_load((var10 + ((var16 + ((var6 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var16 + ((var6 + var15) * var11)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var8 * 132))
        if (1 if i32_load16_u((var7 + (var8 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label16', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label16', '$label13']
        _br_idx = (i32_load8_u((var7 + (var8 * 132)) + 125) - 4)
        break  # br_table
        var6 = (var1 + 2)
        if (1 if var14 <= (var1 + 2) else 0):
            break
        if (1 if (var0 | var6) < 0 else 0):
            break
        var8 = i32_load((var10 + ((var16 + ((var6 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var16 + ((var6 + var15) * var11)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var8 * 132))
        if (1 if i32_load16_u((var7 + (var8 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label17', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label13', '$label17', '$label13']
        _br_idx = (i32_load8_u((var7 + (var8 * 132)) + 125) - 4)
        break  # br_table
        var6 = var2
        var8 = (var0 + 2)
        if (1 if var14 <= var16 else 0):
            break
        if var9:
            break
        if (1 if (var12 | var16) < 0 else 0):
            break
        var17 = i32_load((var10 + ((var8 + ((var12 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var8 + ((var12 + var15) * var11)) << 2))) < 3 else 0):
            break
        var2 = (var7 + (var17 * 132))
        if (1 if i32_load16_u((var7 + (var17 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var2 + 122) else 0):
            break
        var2 = 1
        # br_table ['$label19', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label19', '$label20']
        _br_idx = (i32_load8_u((var7 + (var17 * 132)) + 125) - 4)
        break  # br_table
        var2 = (var1 - 1)
        if (1 if var14 <= (var1 - 1) else 0):
            break
        if (1 if (var2 | var16) < 0 else 0):
            break
        var17 = i32_load((var10 + ((var8 + (var11 * var19)) << 2)))
        if (1 if i32_load((var10 + ((var8 + (var11 * var19)) << 2))) < 3 else 0):
            break
        var2 = (var7 + (var17 * 132))
        if (1 if i32_load16_u((var7 + (var17 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var2 + 122) else 0):
            break
        var2 = 1
        # br_table ['$label21', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label21', '$label20']
        _br_idx = (i32_load8_u((var7 + (var17 * 132)) + 125) - 4)
        break  # br_table
        if var18:
            break
        if (1 if (var1 | var16) < 0 else 0):
            break
        var17 = i32_load((var10 + ((var8 + ((var1 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var8 + ((var1 + var15) * var11)) << 2))) < 3 else 0):
            break
        var2 = (var7 + (var17 * 132))
        if (1 if i32_load16_u((var7 + (var17 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var2 + 122) else 0):
            break
        var2 = 1
        # br_table ['$label22', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label22', '$label20']
        _br_idx = (i32_load8_u((var7 + (var17 * 132)) + 125) - 4)
        break  # br_table
        var2 = (var1 + 1)
        if (1 if var14 <= (var1 + 1) else 0):
            break
        if (1 if (var2 | var16) < 0 else 0):
            break
        var17 = i32_load((var10 + ((var8 + ((var2 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var8 + ((var2 + var15) * var11)) << 2))) < 3 else 0):
            break
        var2 = (var7 + (var17 * 132))
        if (1 if i32_load16_u((var7 + (var17 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var2 + 122) else 0):
            break
        var2 = 1
        # br_table ['$label23', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label23', '$label20']
        _br_idx = (i32_load8_u((var7 + (var17 * 132)) + 125) - 4)
        break  # br_table
        var2 = (var1 + 2)
        if (1 if var14 <= (var1 + 2) else 0):
            break
        if (1 if (var2 | var16) < 0 else 0):
            break
        var16 = i32_load((var10 + ((var8 + ((var2 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var8 + ((var2 + var15) * var11)) << 2))) < 3 else 0):
            break
        var2 = (var7 + (var16 * 132))
        if (1 if i32_load16_u((var7 + (var16 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var2 + 122) else 0):
            break
        var2 = 1
        # br_table ['$label18', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label18', '$label20']
        _br_idx = (i32_load8_u((var7 + (var16 * 132)) + 125) - 4)
        break  # br_table
        var2 = var6
        if (1 if var8 >= var14 else 0):
            break
        var0 = (var0 + 3)
        if var9:
            break
        if (1 if (var8 | var12) < 0 else 0):
            break
        var12 = i32_load((var10 + ((var0 + ((var12 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var0 + ((var12 + var15) * var11)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var12 * 132))
        if (1 if i32_load16_u((var7 + (var12 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label25', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label25', '$label26']
        _br_idx = (i32_load8_u((var7 + (var12 * 132)) + 125) - 4)
        break  # br_table
        var6 = (var1 - 1)
        if (1 if var14 <= (var1 - 1) else 0):
            break
        if (1 if (var6 | var8) < 0 else 0):
            break
        var12 = i32_load((var10 + ((var0 + (var11 * var19)) << 2)))
        if (1 if i32_load((var10 + ((var0 + (var11 * var19)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var12 * 132))
        if (1 if i32_load16_u((var7 + (var12 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label27', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label27', '$label26']
        _br_idx = (i32_load8_u((var7 + (var12 * 132)) + 125) - 4)
        break  # br_table
        if var18:
            break
        if (1 if (var1 | var8) < 0 else 0):
            break
        var12 = i32_load((var10 + ((var0 + ((var1 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var0 + ((var1 + var15) * var11)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var12 * 132))
        if (1 if i32_load16_u((var7 + (var12 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label28', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label28', '$label26']
        _br_idx = (i32_load8_u((var7 + (var12 * 132)) + 125) - 4)
        break  # br_table
        var6 = (var1 + 1)
        if (1 if var14 <= (var1 + 1) else 0):
            break
        if (1 if (var6 | var8) < 0 else 0):
            break
        var12 = i32_load((var10 + ((var0 + ((var6 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var0 + ((var6 + var15) * var11)) << 2))) < 3 else 0):
            break
        var6 = (var7 + (var12 * 132))
        if (1 if i32_load16_u((var7 + (var12 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var6 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label29', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label29', '$label26']
        _br_idx = (i32_load8_u((var7 + (var12 * 132)) + 125) - 4)
        break  # br_table
        var1 = (var1 + 2)
        if (1 if var14 <= (var1 + 2) else 0):
            break
        if (1 if (var1 | var8) < 0 else 0):
            break
        var0 = i32_load((var10 + ((var0 + ((var1 + var15) * var11)) << 2)))
        if (1 if i32_load((var10 + ((var0 + ((var1 + var15) * var11)) << 2))) < 3 else 0):
            break
        var1 = (var7 + (var0 * 132))
        if (1 if i32_load16_u((var7 + (var0 * 132)) + 110) != var3 else 0):
            break
        if (1 if var13 != i32_load8_u(var1 + 122) else 0):
            break
        var6 = 1
        # br_table ['$label24', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label24', '$label26']
        _br_idx = (i32_load8_u((var7 + (var0 * 132)) + 125) - 4)
        break  # br_table
        var6 = var2
        if (1 if (var6 & 1) == 0 else 0):
            break
        if var4:
            break
        break
    var6 = 1
    if (1 if var4 == 0 else 0):
        break
    var2 = (i32_load(9142440) + 2)
    var20 = ((var0 + (((var1 + ((i32_load(9142440) + 2) * var7)) + 1) * var2)) + 1)
    var10 = i32_load(9142840)
    i32_store((var10 + (var20 << 2)), var5)
    var6 = 1
    return (var6 & 1)

