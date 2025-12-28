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
# $qe
# Export: qe
# ==========================================================
def qe(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12):
    """Export: qe"""
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
    if (1 if var9 <= 254 else 0):
        var20 = ((1 if i32_load(((var9 * 404) + 9568096) + 264) == 0 else 0) & (1 if var11 > 1 else 0))
    var22 = (var6 * var7)
    var19 = ((var2 & 0xFFFFFFFF) // (var6 * var7))
    var17 = i32_load(9687232)
    if (1 if var11 == 1 else 0):
        # br_table ['$label0', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label2', '$label1']
        _br_idx = (var10 - 6)
        break  # br_table
        var16 = (var1 * var2)
        break
        var16 = (var1 * var2)
        if (1 if (var1 * var2) == 0 else 0):
            break
        var2 = 0
        if (1 if var16 >= 4 else 0):
            var18 = (var16 & -4)
            var12 = 0
            while True:  # loop $label5
                var13 = (var2 << 2)
                var14 = (var17 + (var2 << 2))
                if (1 if i32_load((var17 + (var2 << 2))) == -16712192 else 0):
                    i32_store(var14, 0)
                var14 = (var17 + (var13 | 4))
                if (1 if i32_load((var17 + (var13 | 4))) == -16712192 else 0):
                    i32_store(var14, 0)
                var14 = (var17 + (var13 | 8))
                if (1 if i32_load((var17 + (var13 | 8))) == -16712192 else 0):
                    i32_store(var14, 0)
                var13 = (var17 + (var13 | 12))
                if (1 if i32_load((var17 + (var13 | 12))) == -16712192 else 0):
                    i32_store(var13, 0)
                var2 = (var2 + 4)
                var12 = (var12 + 4)
                if (1 if (var12 + 4) != var18 else 0):
                    continue
                break  # end loop
        var12 = (var16 & 3)
        if (1 if (var16 & 3) == 0 else 0):
            break
        while True:  # loop $label6
            var13 = (var17 + (var2 << 2))
            if (1 if i32_load((var17 + (var2 << 2))) == -16712192 else 0):
                i32_store(var13, 0)
            var2 = (var2 + 1)
            var15 = (var15 + 1)
            if (1 if (var15 + 1) != var12 else 0):
                continue
            break  # end loop
        break
        var16 = (var1 * var2)
        if (1 if (var1 * var2) == 0 else 0):
            break
        var2 = 0
        while True:  # loop $label8
            var15 = (var2 << 2)
            var12 = (var17 + (var2 << 2))
            var13 = i32_load8_u((var17 + (var2 << 2)))
            if (1 if i32_load8_u((var17 + (var2 << 2))) == i32_load8_u(var12 + 1) else 0):
                if (1 if var13 == i32_load8_u((var17 + (var15 | 2))) else 0):
                    break
            i32_store(var12, 0)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var16 else 0):
                continue
            break  # end loop
        if (1 if var16 == 0 else 0):
            break
        var15 = 0
        var2 = 0
        if (1 if var16 >= 4 else 0):
            var18 = (var16 & -4)
            var12 = 0
            while True:  # loop $label9
                var13 = (var2 << 2)
                var14 = (var17 + (var2 << 2))
                if (1 if i32_load((var17 + (var2 << 2))) == -16711936 else 0):
                    i32_store(var14, 0)
                var14 = (var17 + (var13 | 4))
                if (1 if i32_load((var17 + (var13 | 4))) == -16711936 else 0):
                    i32_store(var14, 0)
                var14 = (var17 + (var13 | 8))
                if (1 if i32_load((var17 + (var13 | 8))) == -16711936 else 0):
                    i32_store(var14, 0)
                var13 = (var17 + (var13 | 12))
                if (1 if i32_load((var17 + (var13 | 12))) == -16711936 else 0):
                    i32_store(var13, 0)
                var2 = (var2 + 4)
                var12 = (var12 + 4)
                if (1 if (var12 + 4) != var18 else 0):
                    continue
                break  # end loop
        var12 = (var16 & 3)
        if (1 if (var16 & 3) == 0 else 0):
            break
        while True:  # loop $label10
            var13 = (var17 + (var2 << 2))
            if (1 if i32_load((var17 + (var2 << 2))) == -16711936 else 0):
                i32_store(var13, 0)
            var2 = (var2 + 1)
            var15 = (var15 + 1)
            if (1 if (var15 + 1) != var12 else 0):
                continue
            break  # end loop
        break
    if (1 if var10 != 22 else 0):
        break
    var13 = (var1 * var2)
    if (1 if (var1 * var2) == 0 else 0):
        break
    var2 = 0
    while True:  # loop $label11
        var12 = i32_load(9687232)
        var15 = (var2 << 2)
        var18 = (i32_load(9687232) + (var2 << 2))
        var16 = (var15 | 2)
        var15 = (var15 | 1)
        var12 = (((i32_load8_u((var12 + (var15 | 2))) + (i32_load8_u((var12 + (var15 | 1))) + i32_load8_u(var18))) & 0xFFFFFFFF) // 3)
        i32_store8((i32_load(9687232) + (var2 << 2)), (((i32_load8_u((var12 + (var15 | 2))) + (i32_load8_u((var12 + (var15 | 1))) + i32_load8_u(var18))) & 0xFFFFFFFF) // 3))
        i32_store8((i32_load(9687232) + var15), var12)
        i32_store8((i32_load(9687232) + var16), var12)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var13 else 0):
            continue
        break  # end loop
    var12 = -1
    if (1 if var22 == 0 else 0):
        break
    if (1 if var1 <= 0 else 0):
        break
    var15 = var19
    var14 = 0
    var16 = -1
    while True:  # loop $label15
        var13 = 0
        var18 = (var19 * var24)
        if (1 if (var19 * var24) < (var18 + var19) else 0):
            while True:  # loop $label14
                var2 = var18
                while True:  # loop $label13
                    if i32_load((var17 + (((var1 * var2) + var13) << 2))):
                        var23 = (var2 % var19)
                        var21 = ((var2 % var19) if (1 if var21 < var23 else 0) else var21)
                        var16 = (var23 if (1 if var16 > var23 else 0) else var16)
                        var14 = (var13 if (1 if var13 > var14 else 0) else var14)
                        var12 = (var13 if (1 if var12 > var13 else 0) else var12)
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != var15 else 0):
                        continue
                    break  # end loop
                var13 = (var13 + 1)
                if (1 if (var13 + 1) != var1 else 0):
                    continue
                break  # end loop
        var15 = (var15 + var19)
        var24 = (var24 + 1)
        if (1 if (var24 + 1) != var22 else 0):
            continue
        break  # end loop
    break
    var16 = -1
    var14 = 0
    var23 = ((var21 - var16) + 1)
    var24 = ((var14 - var12) + 1)
    if var20:
        var2 = (((var22 * var23) * var24) << 2)
        var25 = func26((((var22 * var23) * var24) << 2))
        # Unknown: memory.fill []
    if (1 if var22 == 0 else 0):
        var2 = i32_load(9687232)
        break
    var17 = 0
    var2 = i32_load(9687232)
    var26 = (var14 + 1)
    if (1 if ((1 if var12 < (var14 + 1) else 0) & var20) == 0 else 0):
        break
    var27 = i32_load(9687236)
    var28 = (var21 + 1)
    var14 = (var21 + 1)
    var15 = 0
    while True:  # loop $label20
        var13 = (var17 * var19)
        var20 = ((var17 * var19) + var16)
        if (1 if ((var17 * var19) + var16) < (var13 + var28) else 0):
            while True:  # loop $label19
                var29 = (var1 * var20)
                var13 = var12
                while True:  # loop $label18
                    var18 = ((var13 + var29) << 2)
                    if i32_load8_u((var27 + ((var13 + var29) << 2))):
                        var21 = (var15 + var25)
                        var30 = (((i32_load8_u((var2 + (var18 | 2))) + (i32_load8_u((var2 + (var18 | 1))) + i32_load8_u((var2 + var18)))) & 0xFFFFFFFF) // 3)
                        i32_store8((var15 + var25) + 2, (((i32_load8_u((var2 + (var18 | 2))) + (i32_load8_u((var2 + (var18 | 1))) + i32_load8_u((var2 + var18)))) & 0xFFFFFFFF) // 3))
                        i32_store16(var21, ((var30 & 255) * 257))
                        i32_store8(var21 + 3, i32_load8_u((var2 + (var18 | 3))))
                    var15 = (var15 + 4)
                    var13 = (var13 + 1)
                    if (1 if (var13 + 1) < var26 else 0):
                        continue
                    break  # end loop
                var20 = (var20 + 1)
                if (1 if (var20 + 1) != var14 else 0):
                    continue
                break  # end loop
        var14 = (var14 + var19)
        var17 = (var17 + 1)
        if (1 if (var17 + 1) != var22 else 0):
            continue
        break  # end loop
    if var2:
        i32_store(9687232, 0)
    var1 = i32_load(9687236)
    if i32_load(9687236):
        i32_store(9687236, 0)
    var2 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    var15 = i32_load(9687224)
    var1 = i32_load(9687220)
    var13 = (var2 << 2)
    i32_store((i32_load(9687220) + (var2 << 2)), var24)
    var19 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var19 << 2)), (var22 * var23))
    var19 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var19 << 2)), (var4 - ((var12 & 0xFFFFFFFF) // var11)))
    var4 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var4 << 2)), (var5 - ((var16 & 0xFFFFFFFF) // var11)))
    var4 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var4 << 2)), var6)
    var4 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var4 << 2)), var7)
    var4 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var4 << 2)), var3)
    var3 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var3 << 2)), var9)
    var3 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var3 << 2)), var10)
    var3 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var3 << 2)), (var15 - var13))
    var3 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var3 << 2)), 0)
    var3 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var3 << 2)), var8)
    var3 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var3 << 2)), var11)
    var3 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 1))
    i32_store((var1 + (var3 << 2)), var0)
    var0 = i32_load(9687228)
    i32_store(9687228, (i32_load(9687228) + 2))
    i32_store((var1 + (var0 << 2)) + 4, 0)
    if var25:
    return var2

