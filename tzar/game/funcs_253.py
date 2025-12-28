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
# $func461
# ==========================================================
def func461(var0, var1, var2):
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
    var24 = 0
    var25 = 0
    var26 = 0
    var27 = 0
    var28 = 0
    var29 = 0
    var30 = 0
    var31 = 0
    var32 = 0
    var33 = 0
    var34 = 0
    var35 = 0
    var36 = 0
    var37 = 0
    var38 = 0
    var4 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var3 = 1
    var6 = ((var0 * 404) + 9568096)
    # br_table ['$label0', '$label1', '$label2', '$label3', '$label0', '$label2']
    _br_idx = i32_load(((var0 * 404) + 9568096) + 264)
    break  # br_table
    i64_store(var4 + 4, 1)
    i32_store(var4, var0)
    i32_store(var4 + 44, var1)
    func417(var4, (var4 + 44), 1)
    break
    var11 = i32_load(9671128)
    var23 = i32_load(var2 + 283876)
    var24 = i32_load(var2 + 283872)
    if (1 if i32_load(var6 + 188) != 2 else 0):
        break
    var9 = i32_load(9142440)
    var12 = (i32_load(9142440) + 2)
    var14 = ((var0 * 404) + 9568096)
    var16 = i32_load(9142840)
    var3 = 0
    while True:  # loop $label12
        var7 = var3
        var0 = (var3 << 2)
        var2 = (i32_load((((var3 << 2) | 4) + 8611904)) + var23)
        if (1 if var9 <= (i32_load((((var3 << 2) | 4) + 8611904)) + var23) else 0):
            break
        var6 = (i32_load((var0 + 8611904)) + var24)
        if (1 if var9 <= (i32_load((var0 + 8611904)) + var24) else 0):
            break
        if (1 if (var2 | var6) < 0 else 0):
            break
        var13 = i32_load(var14 + 216)
        if (1 if i32_load(var14 + 216) <= 0 else 0):
            break
        var17 = (i32_load(var14 + 220) + var2)
        if (1 if (i32_load(var14 + 220) + var2) <= var2 else 0):
            break
        var15 = (var6 + var13)
        var8 = i32_load(var14 + 372)
        var0 = var6
        while True:  # loop $label11
            var5 = (var0 + 1)
            var10 = (var0 - var6)
            var3 = var2
            if (1 if var0 < var9 else 0):
                while True:  # loop $label8
                    if (1 if i32_load8_u((var8 + (((var3 - var2) * var13) + var10))) == 0 else 0):
                        var3 = (var3 + 1)
                        break
                    if (1 if var3 >= var9 else 0):
                        break
                    if (1 if (var0 | var3) < 0 else 0):
                        break
                    var3 = (var3 + 1)
                    if i32_load((var16 + ((((var3 + 1) * var12) + var5) << 2))):
                        break
                    if (1 if i32_load(((i32_load8_u((var11 + (i32_load((var16 + ((((var3 + var12) * var12) + var5) << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 1 else 0):
                        break
                    if (1 if var3 != var17 else 0):
                        continue
                    break
                    break  # end loop
                raise RuntimeError('unreachable')
            while True:  # loop $label10
                if i32_load8_u((var8 + (((var3 - var2) * var13) + var10))):
                    break
                var3 = (var3 + 1)
                if (1 if (var3 + 1) != var17 else 0):
                    continue
                break  # end loop
            var0 = var5
            if (1 if var5 < var15 else 0):
                continue
            break  # end loop
        var0 = i32_load(38500)
        i32_store(var4 + 8, var2)
        i32_store(var4 + 4, var6)
        i32_store(var4, var0)
        var0 = (var1 * 132)
        var1 = (var11 + (var1 * 132))
        var2 = i32_load16_u((var11 + (var1 * 132)) + 110)
        i32_store(var4 + 40, 0)
        i64_store(var4 + 32, 4294967297)
        i64_store(var4 + 24, 4294967297)
        i64_store(var4 + 16, 4294967297)
        i32_store(var4 + 12, var2)
        i32_store(var4 + 44, i32_load(var1 + 28))
        var3 = 1
        i32_store8((i32_load(9671128) + var0) + 129, 3)
        break
        var3 = (var7 + 2)
        if (1 if var7 <= 3357 else 0):
            continue
        break  # end loop
    var3 = 0
    break
    i32_store(var4, var0)
    i32_store(var4 + 44, var1)
    func364(var4, (var4 + 44), 1)
    break
    if (1 if var0 == i32_load(38636) else 0):
        var3 = 0
        var6 = (var11 + (var1 * 132))
        var5 = i32_load16_u((var11 + (var1 * 132)) + 112)
        var2 = (i32_load16_u((var11 + (var1 * 132)) + 112) - 2)
        var9 = ((i32_load8_u(var6 + 122) * 404) + 9568096)
        var14 = ((var5 + i32_load(((i32_load8_u(var6 + 122) * 404) + 9568096) + 216)) + 2)
        if (1 if (i32_load16_u((var11 + (var1 * 132)) + 112) - 2) >= ((var5 + i32_load(((i32_load8_u(var6 + 122) * 404) + 9568096) + 216)) + 2) else 0):
            break
        var6 = i32_load16_u(var6 + 114)
        var7 = (i32_load16_u(var6 + 114) - 2)
        var13 = ((i32_load(var9 + 220) + var6) + 2)
        if (1 if (i32_load16_u(var6 + 114) - 2) >= ((i32_load(var9 + 220) + var6) + 2) else 0):
            break
        var9 = i32_load(9142440)
        var12 = (i32_load(9142440) + 2)
        var16 = i32_load(9142840)
        while True:  # loop $label16
            var5 = (var2 + 1)
            var3 = var7
            if (1 if var2 < var9 else 0):
                while True:  # loop $label15
                    var6 = var3
                    var3 = (var3 + 1)
                    if (1 if var6 >= var9 else 0):
                        break
                    if (1 if (var2 | var6) < 0 else 0):
                        break
                    if (1 if i32_load((var16 + ((var5 + ((var3 + var12) * var12)) << 2))) == 0 else 0):
                        break
                    if (1 if var3 != var13 else 0):
                        continue
                    break  # end loop
            var3 = 0
            var2 = var5
            if (1 if var5 != var14 else 0):
                continue
            break
            break  # end loop
        i32_store(var4 + 8, var6)
        i32_store(var4 + 4, var2)
        i32_store(var4, var0)
        var0 = (var11 + (var1 * 132))
        var1 = i32_load16_u((var11 + (var1 * 132)) + 110)
        i32_store(var4 + 40, 0)
        i64_store(var4 + 32, 4294967297)
        i64_store(var4 + 24, 4294967297)
        i64_store(var4 + 16, 4294967297)
        i32_store(var4 + 12, var1)
        i32_store(var4 + 44, i32_load(var0 + 28))
        var3 = 1
        break
    var1 = (var11 + (var1 * 132))
    var32 = (var11 + (var1 * 132))
    i32_store8(var1 + 129, 0)
    var12 = ((1 if i32_load(38512) != var0 else 0) & (1 if i32_load(38792) != var0 else 0))
    var13 = (1 if ((1 if i32_load(38512) != var0 else 0) & (1 if i32_load(38792) != var0 else 0)) else 2)
    var33 = (13 if var12 else 10)
    var1 = ((var0 * 404) + 9568096)
    var16 = i32_load(((var0 * 404) + 9568096) + 220)
    var34 = (i32_load(((var0 * 404) + 9568096) + 220) // 2)
    var17 = i32_load(var1 + 216)
    var35 = (i32_load(var1 + 216) // 2)
    var36 = i32_load(var2 + 283908)
    var25 = i32_load(9142440)
    var3 = 0
    while True:  # loop $label32
        var14 = var3
        var3 = (var3 << 2)
        var26 = i32_load((((var3 << 2) | 4) + 8611904))
        var1 = (i32_load((((var3 << 2) | 4) + 8611904)) + var23)
        if (1 if var25 <= (i32_load((((var3 << 2) | 4) + 8611904)) + var23) else 0):
            break
        var27 = i32_load((var3 + 8611904))
        var3 = (i32_load((var3 + 8611904)) + var24)
        if (1 if var25 <= (i32_load((var3 + 8611904)) + var24) else 0):
            break
        if (1 if (var1 | var3) < 0 else 0):
            break
        var18 = 0
        var6 = (var13 << 1)
        var5 = ((var13 << 1) + var17)
        var11 = var3
        var3 = (var3 - var13)
        var7 = i32_load(var2 + 283872)
        var9 = ((((var13 << 1) + var17) + ((var3 - var13) << 1)) - (i32_load(var2 + 283872) << 1))
        var8 = (var6 + var16)
        var9 = var1
        var6 = (var1 - var13)
        var1 = i32_load(var2 + 283876)
        var10 = (((var6 + var16) + ((var1 - var13) << 1)) - (i32_load(var2 + 283876) << 1))
        var10 = (var33 << 1)
        if (1 if (((((((var13 << 1) + var17) + ((var3 - var13) << 1)) - (i32_load(var2 + 283872) << 1)) * var9) + ((((var6 + var16) + ((var1 - var13) << 1)) - (i32_load(var2 + 283876) << 1)) * var10)) - 1) <= ((var33 << 1) * var10) else 0):
            break
        var18 = 1
        if (1 if var5 <= 0 else 0):
            break
        if (1 if var8 <= 0 else 0):
            break
        var20 = (var6 + var8)
        var28 = (var3 + var5)
        var29 = (var9 + var16)
        var30 = (var11 + var17)
        var15 = i32_load(9142440)
        var8 = (i32_load(9142440) + 2)
        var21 = i32_load(9671128)
        var10 = i32_load(9142840)
        if var12:
            var19 = (var1 - 3)
            var31 = (var1 + 3)
            var37 = (var7 - 3)
            var38 = (var7 + 3)
            while True:  # loop $label27
                if (1 if var3 >= var15 else 0):
                    break
                if ((1 if var3 < var38 else 0) & (1 if var3 > var37 else 0)):
                    break
                var5 = (var3 + 1)
                var1 = var6
                if ((1 if var3 < var11 else 0) | (1 if var3 >= var30 else 0)):
                    while True:  # loop $label22
                        if (1 if var1 >= var15 else 0):
                            break
                        if (1 if (var1 | var3) < 0 else 0):
                            break
                        var7 = (var1 + 1)
                        var22 = i32_load((var10 + ((var5 + (((var1 + 1) + var8) * var8)) << 2)))
                        if (1 if i32_load((var10 + ((var5 + (((var1 + 1) + var8) * var8)) << 2))) == 0 else 0):
                            break
                        if (1 if i32_load(((i32_load8_u((var21 + (var22 * 132)) + 122) * 404) + 9568096) + 264) != 1 else 0):
                            break
                        break
                        if (1 if var1 >= var31 else 0):
                            break
                        if (1 if var1 <= var19 else 0):
                            break
                        break
                        var1 = var7
                        if (1 if var7 < var20 else 0):
                            continue
                        break
                        break  # end loop
                    raise RuntimeError('unreachable')
                while True:  # loop $label26
                    if (1 if var1 >= var15 else 0):
                        break
                    if (1 if (var1 | var3) < 0 else 0):
                        break
                    var7 = (var1 + 1)
                    if (1 if ((1 if var1 < var29 else 0) & (1 if var1 >= var9 else 0)) == 0 else 0):
                        var22 = i32_load((var10 + ((var5 + ((var7 + var8) * var8)) << 2)))
                        if (1 if i32_load((var10 + ((var5 + ((var7 + var8) * var8)) << 2))) == 0 else 0):
                            break
                        if (1 if i32_load(((i32_load8_u((var21 + (var22 * 132)) + 122) * 404) + 9568096) + 264) != 1 else 0):
                            break
                        break
                    if i32_load((var10 + ((((var7 + var8) * var8) + var5) << 2))):
                        break
                    if (1 if i32_load((var10 + (((var7 * var8) + var5) << 2))) == 0 else 0):
                        break
                    break
                    if (1 if var1 >= var31 else 0):
                        break
                    if (1 if var1 <= var19 else 0):
                        break
                    break
                    var1 = var7
                    if (1 if var7 < var20 else 0):
                        continue
                    break  # end loop
                var3 = var5
                if (1 if var5 < var28 else 0):
                    continue
                break  # end loop
            break
        while True:  # loop $label30
            var5 = var3
            if (1 if var3 < var15 else 0):
                var3 = (var5 + 1)
                var19 = ((1 if var5 < var30 else 0) & (1 if var5 >= var11 else 0))
                var1 = var6
                while True:  # loop $label29
                    var18 = 0
                    var7 = var1
                    if (1 if var15 <= var1 else 0):
                        break
                    if (1 if (var5 | var7) < 0 else 0):
                        break
                    var1 = (var7 + 1)
                    if (1 if (((1 if var7 >= var9 else 0) & var19) & (1 if var7 < var29 else 0)) == 0 else 0):
                        var7 = i32_load((var10 + ((var3 + ((var1 + var8) * var8)) << 2)))
                        if (1 if i32_load((var10 + ((var3 + ((var1 + var8) * var8)) << 2))) == 0 else 0):
                            break
                        if (1 if i32_load(((i32_load8_u((var21 + (var7 * 132)) + 122) * 404) + 9568096) + 264) != 1 else 0):
                            break
                        break
                    if i32_load((var10 + ((((var1 + var8) * var8) + var3) << 2))):
                        break
                    if i32_load((var10 + (((var1 * var8) + var3) << 2))):
                        break
                    if (1 if var1 < var20 else 0):
                        continue
                    break  # end loop
                if (1 if var3 < var28 else 0):
                    continue
            break  # end loop
        var18 = (1 if var5 < var15 else 0)
        break
        if (1 if 0 == 0 else 0):
            break
        if (1 if func108((var11 + var35), (var9 + var34), var36, 9) == 0 else 0):
            break
        var1 = ((var26 * var26) + (var27 * var27))
        if (1 if ((var26 * var26) + (var27 * var27)) > i32_load(var2 + 283880) else 0):
            i32_store(var2 + 283880, var1)
        func261(var0, var11, var9, var32)
        var3 = 1
        break
        var3 = (var14 + 2)
        if (1 if var14 <= 116157 else 0):
            continue
        break  # end loop
    var3 = 0
    global global0
    global0 = (var4 + 48)
    return var3

