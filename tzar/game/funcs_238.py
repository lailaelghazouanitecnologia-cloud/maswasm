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
# $func897
# ==========================================================
def func897(var0, var1):
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
    var20 = 0
    var21 = 0
    var22 = 0
    var23 = 0
    var7 = i32_load(9671128)
    var15 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 3 else 0):
        break
    var9 = i32_load8_u(var15 + 122)
    var18 = i32_load16_u(var15 + 110)
    if (1 if i32_load16_u(var15 + 110) == 0 else 0):
        break
    if i32_load8_u(((var9 * 404) + 9568096) + 332):
        break
    var0 = (var7 + (var0 * 132))
    if (1 if i32_load8_u((var7 + (var0 * 132)) + 126) != 2 else 0):
        break
    i32_store8(var0 + 126, 0)
    break
    var4 = ((var9 * 404) + 9568096)
    var10 = i32_load(((var9 * 404) + 9568096) + 216)
    var1 = (var7 + (var0 * 132))
    var3 = i32_load16_u((var7 + (var0 * 132)) + 114)
    var1 = i32_load16_u(var1 + 112)
    if (1 if i32_load8_u(9216060) == 0 else 0):
        break
    if i32_load(var4 + 264):
        break
    var4 = i32_load(9561692)
    var8 = i32_load(9142840)
    var13 = (var1 + 2)
    var11 = (i32_load(9142440) + 2)
    var14 = (var3 + (i32_load(9142440) + 2))
    var16 = (((var3 + (i32_load(9142440) + 2)) + 1) * var11)
    var2 = i32_load((i32_load(9142840) + (((var1 + 2) + (((var3 + (i32_load(9142440) + 2)) + 1) * var11)) << 2)))
    if (1 if (i32_load((i32_load(9142840) + (((var1 + 2) + (((var3 + (i32_load(9142440) + 2)) + 1) * var11)) << 2))) - 3) > -5 else 0):
        break
    var10 = (var7 + (var2 * 132))
    var3 = i32_load16_u((var7 + (var2 * 132)) + 110)
    if (1 if i32_load16_u((var7 + (var2 * 132)) + 110) == 0 else 0):
        break
    if (1 if i32_load((((var4 + (var3 * 286704)) + (var9 << 2)) + 281808)) > 1500 else 0):
        break
    var1 = (var10 + 110)
    break
    var10 = (var11 * var14)
    var2 = i32_load((var8 + ((var13 + (var11 * var14)) << 2)))
    if (1 if (i32_load((var8 + ((var13 + (var11 * var14)) << 2))) - 3) > -5 else 0):
        break
    var5 = (var7 + (var2 * 132))
    var3 = i32_load16_u((var7 + (var2 * 132)) + 110)
    if (1 if i32_load16_u((var7 + (var2 * 132)) + 110) == 0 else 0):
        break
    if (1 if i32_load((((var4 + (var3 * 286704)) + (var9 << 2)) + 281808)) >= 1501 else 0):
        break
    var1 = (var5 + 110)
    break
    var5 = (var1 + 1)
    var2 = i32_load((var8 + (((var1 + 1) + var10) << 2)))
    if (1 if (i32_load((var8 + (((var1 + 1) + var10) << 2))) - 3) > -5 else 0):
        break
    var12 = (var7 + (var2 * 132))
    var3 = i32_load16_u((var7 + (var2 * 132)) + 110)
    if (1 if i32_load16_u((var7 + (var2 * 132)) + 110) == 0 else 0):
        break
    if (1 if i32_load((((var4 + (var3 * 286704)) + (var9 << 2)) + 281808)) >= 1501 else 0):
        break
    var1 = (var12 + 110)
    break
    var2 = i32_load((var8 + ((var1 + var10) << 2)))
    if (1 if (i32_load((var8 + ((var1 + var10) << 2))) - 3) > -5 else 0):
        break
    var10 = (var7 + (var2 * 132))
    var3 = i32_load16_u((var7 + (var2 * 132)) + 110)
    if (1 if i32_load16_u((var7 + (var2 * 132)) + 110) == 0 else 0):
        break
    if (1 if i32_load((((var4 + (var3 * 286704)) + (var9 << 2)) + 281808)) >= 1501 else 0):
        break
    var1 = (var10 + 110)
    break
    var2 = i32_load((var8 + ((var1 + var16) << 2)))
    if (1 if (i32_load((var8 + ((var1 + var16) << 2))) - 3) > -5 else 0):
        break
    var10 = (var7 + (var2 * 132))
    var3 = i32_load16_u((var7 + (var2 * 132)) + 110)
    if (1 if i32_load16_u((var7 + (var2 * 132)) + 110) == 0 else 0):
        break
    if (1 if i32_load((((var4 + (var3 * 286704)) + (var9 << 2)) + 281808)) >= 1501 else 0):
        break
    var1 = (var10 + 110)
    break
    var1 = ((var14 + 2) * var11)
    var2 = i32_load((var8 + ((var1 + ((var14 + 2) * var11)) << 2)))
    if (1 if (i32_load((var8 + ((var1 + ((var14 + 2) * var11)) << 2))) - 3) > -5 else 0):
        break
    var11 = (var7 + (var2 * 132))
    var3 = i32_load16_u((var7 + (var2 * 132)) + 110)
    if (1 if i32_load16_u((var7 + (var2 * 132)) + 110) == 0 else 0):
        break
    if (1 if i32_load((((var4 + (var3 * 286704)) + (var9 << 2)) + 281808)) >= 1501 else 0):
        break
    var1 = (var11 + 110)
    break
    var2 = i32_load((var8 + ((var1 + var5) << 2)))
    if (1 if (i32_load((var8 + ((var1 + var5) << 2))) - 3) > -5 else 0):
        break
    var11 = (var7 + (var2 * 132))
    var3 = i32_load16_u((var7 + (var2 * 132)) + 110)
    if (1 if i32_load16_u((var7 + (var2 * 132)) + 110) == 0 else 0):
        break
    if (1 if i32_load((((var4 + (var3 * 286704)) + (var9 << 2)) + 281808)) >= 1501 else 0):
        break
    var1 = (var11 + 110)
    break
    var2 = i32_load((var8 + ((var1 + var13) << 2)))
    if (1 if (i32_load((var8 + ((var1 + var13) << 2))) - 3) > -5 else 0):
        break
    var1 = (var7 + (var2 * 132))
    var3 = i32_load16_u((var7 + (var2 * 132)) + 110)
    if (1 if i32_load16_u((var7 + (var2 * 132)) + 110) == 0 else 0):
        break
    if (1 if i32_load((((var4 + (var3 * 286704)) + (var9 << 2)) + 281808)) >= 1501 else 0):
        break
    var1 = (var1 + 110)
    break
    var11 = i32_load(9142892)
    if i32_load(9142892):
        # Unknown: memory.fill []
    var19 = (var1 + var10)
    if (1 if (var1 + var10) <= var1 else 0):
        break
    var20 = (i32_load(((var9 * 404) + 9568096) + 220) + var3)
    if (1 if (i32_load(((var9 * 404) + 9568096) + 220) + var3) <= var3 else 0):
        break
    var14 = i32_load(9142840)
    var16 = i32_load(9142440)
    var13 = (i32_load(9142440) + 2)
    var21 = ((i32_load(9142440) + 2) << 1)
    var22 = i32_load(((var9 * 404) + 9568096) + 372)
    var4 = var1
    while True:  # loop $label24
        var23 = (var4 - var1)
        var8 = var3
        while True:  # loop $label23
            var2 = 0
            if i32_load8_u((var22 + (var23 + ((var8 - var3) * var10)))):
                while True:  # loop $label22
                    var12 = (var2 << 3)
                    var5 = (i32_load(((var2 << 3) + 8932)) + var8)
                    if (1 if var16 <= (i32_load(((var2 << 3) + 8932)) + var8) else 0):
                        break
                    var12 = (i32_load((var12 + 8928)) + var4)
                    if (1 if var16 <= (i32_load((var12 + 8928)) + var4) else 0):
                        break
                    if (1 if (var5 | var12) < 0 else 0):
                        break
                    var12 = (var12 + 1)
                    var5 = (var5 + 1)
                    var6 = i32_load((var14 + (((var12 + 1) + ((var5 + 1) * var13)) << 2)))
                    if (1 if i32_load((var14 + (((var12 + 1) + ((var5 + 1) * var13)) << 2))) < 3 else 0):
                        break
                    if (1 if var0 == var6 else 0):
                        break
                    var6 = (var7 + (var6 * 132))
                    var17 = i32_load16_u((var7 + (var6 * 132)) + 110)
                    if (1 if i32_load16_u((var7 + (var6 * 132)) + 110) == 0 else 0):
                        break
                    var6 = i32_load8_u(var6 + 122)
                    if i32_load(((i32_load8_u(var6 + 122) * 404) + 9568096) + 264):
                        break
                    # br_table ['$label14', '$label15', '$label15', '$label15', '$label15', '$label15', '$label15', '$label15', '$label15', '$label15', '$label15', '$label15', '$label15', '$label15', '$label15', '$label14', '$label16']
                    _br_idx = (var6 + -64)
                    break  # br_table
                    if (1 if var6 == 10 else 0):
                        break
                    var6 = ((var17 << 2) + 59200)
                    i32_store(((var17 << 2) + 59200), (i32_load(var6) + 1))
                    var6 = i32_load((var14 + ((var12 + ((var5 + var13) * var13)) << 2)))
                    if (1 if i32_load((var14 + ((var12 + ((var5 + var13) * var13)) << 2))) < 3 else 0):
                        break
                    if (1 if var0 == var6 else 0):
                        break
                    var6 = (var7 + (var6 * 132))
                    var17 = i32_load16_u((var7 + (var6 * 132)) + 110)
                    if (1 if i32_load16_u((var7 + (var6 * 132)) + 110) == 0 else 0):
                        break
                    var6 = i32_load8_u(var6 + 122)
                    if i32_load(((i32_load8_u(var6 + 122) * 404) + 9568096) + 264):
                        break
                    # br_table ['$label17', '$label18', '$label18', '$label18', '$label18', '$label18', '$label18', '$label18', '$label18', '$label18', '$label18', '$label18', '$label18', '$label18', '$label18', '$label17', '$label19']
                    _br_idx = (var6 + -64)
                    break  # br_table
                    if (1 if var6 == 10 else 0):
                        break
                    var6 = ((var17 << 2) + 59200)
                    i32_store(((var17 << 2) + 59200), (i32_load(var6) + 1))
                    var5 = i32_load((var14 + ((var12 + ((var5 + var21) * var13)) << 2)))
                    if (1 if i32_load((var14 + ((var12 + ((var5 + var21) * var13)) << 2))) < 3 else 0):
                        break
                    if (1 if var0 == var5 else 0):
                        break
                    var5 = (var7 + (var5 * 132))
                    var12 = i32_load16_u((var7 + (var5 * 132)) + 110)
                    if (1 if i32_load16_u((var7 + (var5 * 132)) + 110) == 0 else 0):
                        break
                    var5 = i32_load8_u(var5 + 122)
                    if i32_load(((i32_load8_u(var5 + 122) * 404) + 9568096) + 264):
                        break
                    # br_table ['$label13', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label20', '$label13', '$label21']
                    _br_idx = (var5 + -64)
                    break  # br_table
                    if (1 if var5 == 10 else 0):
                        break
                    var5 = ((var12 << 2) + 59200)
                    i32_store(((var12 << 2) + 59200), (i32_load(var5) + 1))
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != 8 else 0):
                        continue
                    break  # end loop
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != var20 else 0):
                continue
            break  # end loop
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var19 else 0):
            continue
        break  # end loop
    if (1 if var11 == 0 else 0):
        break
    var3 = 0
    var2 = 0
    var1 = 0
    if (1 if var11 >= 4 else 0):
        var8 = (var11 & -4)
        var4 = 0
        while True:  # loop $label25
            var13 = (var2 | 3)
            var14 = (var2 | 2)
            var10 = (var2 | 1)
            var1 = (var2 if (1 if i32_load(((var2 << 2) + 59200)) > i32_load(((var1 << 2) + 59200)) else 0) else var1)
            var1 = ((var2 | 1) if (1 if i32_load(((var10 << 2) + 59200)) > i32_load(((var1 << 2) + 59200)) else 0) else (var2 if (1 if i32_load(((var2 << 2) + 59200)) > i32_load(((var1 << 2) + 59200)) else 0) else var1))
            var1 = ((var2 | 2) if (1 if i32_load(((var14 << 2) + 59200)) > i32_load(((var1 << 2) + 59200)) else 0) else ((var2 | 1) if (1 if i32_load(((var10 << 2) + 59200)) > i32_load(((var1 << 2) + 59200)) else 0) else (var2 if (1 if i32_load(((var2 << 2) + 59200)) > i32_load(((var1 << 2) + 59200)) else 0) else var1)))
            var1 = ((var2 | 3) if (1 if i32_load(((var13 << 2) + 59200)) > i32_load(((var1 << 2) + 59200)) else 0) else ((var2 | 2) if (1 if i32_load(((var14 << 2) + 59200)) > i32_load(((var1 << 2) + 59200)) else 0) else ((var2 | 1) if (1 if i32_load(((var10 << 2) + 59200)) > i32_load(((var1 << 2) + 59200)) else 0) else (var2 if (1 if i32_load(((var2 << 2) + 59200)) > i32_load(((var1 << 2) + 59200)) else 0) else var1))))
            var2 = (var2 + 4)
            var4 = (var4 + 4)
            if (1 if (var4 + 4) != var8 else 0):
                continue
            break  # end loop
    var4 = (var11 & 3)
    if (var11 & 3):
        while True:  # loop $label26
            var1 = (var2 if (1 if i32_load(((var2 << 2) + 59200)) > i32_load(((var1 << 2) + 59200)) else 0) else var1)
            var2 = (var2 + 1)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var4 else 0):
                continue
            break  # end loop
    if (1 if var1 == var18 else 0):
        break
    if (1 if var1 == 0 else 0):
        break
    var3 = i32_load8_u(((var9 * 404) + 9568096) + 332)
    var4 = (var7 + (var0 * 132))
    i32_store8((var7 + (var0 * 132)) + 126, 0)
    var1 = (1 if var3 == 0 else 0)
    func78(var15, var1, (1 if var3 == 0 else 0), 1)
    if var1:
        break
    i32_store8(var4 + 126, 2)
    return
    var4 = (var7 + (var0 * 132))
    i32_store8((var7 + (var0 * 132)) + 126, 0)
    func78(var15, var3, 1, 1)
    var0 = (var7 + (var2 * 132))
    if (1 if i32_load(9142872) != i32_load16_u(var1) else 0):
        break
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    func44(var15, 0)
    var0 = i32_load(var0 + 32)
    if (1 if i32_load(var0 + 32) == i32_load(var4 + 28) else 0):
        break
    var1 = (var7 + (var2 * 132))
    var3 = i32_load16_u((var7 + (var2 * 132)) + 118)
    var4 = i32_load16_u(var1 + 116)
    if var0:
        break
    if var4:
        break
    if (1 if var3 == 0 else 0):
        break

