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
# $func276
# ==========================================================
def func276(var0, var1, var2, var3, var4):
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
    var7 = (global0 - 128)
    global global0
    global0 = (global0 - 128)
    i64_store(var7 + 120, 0)
    i64_store(var7 + 112, 0)
    i64_store(var7 + 104, 0)
    i64_store(var7 + 96, 0)
    i64_store(var7 + 88, 0)
    i64_store(var7 + 80, 0)
    i64_store(var7 + 72, 0)
    i64_store(var7 + 64, 0)
    if var3:
        if (1 if var2 == 0 else 0):
            break
        if (1 if ((var0 if var4 else 0) if (var0 | var4) else 1) == 0 else 0):
            break
        if (1 if var1 <= 0 else 0):
            break
        if (1 if var3 > 0 else 0):
            while True:  # loop $label4
                var6 = i32_load((var2 + (var5 << 2)))
                if (1 if i32_load((var2 + (var5 << 2))) > 15 else 0):
                    break
                var6 = ((var7 - -64) + (var6 << 2))
                i32_store(((var7 - -64) + (var6 << 2)), (i32_load(var6) + 1))
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var3 else 0):
                    continue
                break  # end loop
        else:
        if (1 if 0 == var3 else 0):
            break
        i32_store(var7 + 4, 0)
        var6 = i32_load(var7 + 68)
        if (1 if i32_load(var7 + 68) > 2 else 0):
            break
        i32_store(var7 + 8, var6)
        var5 = i32_load(var7 + 72)
        if (1 if i32_load(var7 + 72) > 4 else 0):
            break
        var6 = (var5 + var6)
        i32_store(var7 + 12, (var5 + var6))
        var5 = i32_load(var7 + 76)
        if (1 if i32_load(var7 + 76) > 8 else 0):
            break
        var6 = (var5 + var6)
        i32_store(var7 + 16, (var5 + var6))
        var5 = i32_load(var7 + 80)
        if (1 if i32_load(var7 + 80) > 16 else 0):
            break
        var6 = (var5 + var6)
        i32_store(var7 + 20, (var5 + var6))
        var5 = i32_load(var7 + 84)
        if (1 if i32_load(var7 + 84) > 32 else 0):
            break
        var6 = (var5 + var6)
        i32_store(var7 + 24, (var5 + var6))
        var5 = i32_load(var7 + 88)
        if (1 if i32_load(var7 + 88) > 64 else 0):
            break
        var6 = (var5 + var6)
        i32_store(var7 + 28, (var5 + var6))
        var5 = i32_load(var7 + 92)
        if (1 if i32_load(var7 + 92) > 128 else 0):
            break
        var6 = (var5 + var6)
        i32_store(var7 + 32, (var5 + var6))
        var5 = i32_load(var7 + 96)
        if (1 if i32_load(var7 + 96) > 256 else 0):
            break
        var6 = (var5 + var6)
        i32_store(var7 + 36, (var5 + var6))
        var5 = i32_load(var7 + 100)
        if (1 if i32_load(var7 + 100) > 512 else 0):
            break
        var6 = (var5 + var6)
        i32_store(var7 + 40, (var5 + var6))
        var5 = i32_load(var7 + 104)
        if (1 if i32_load(var7 + 104) > 1024 else 0):
            break
        var6 = (var5 + var6)
        i32_store(var7 + 44, (var5 + var6))
        var5 = i32_load(var7 + 108)
        if (1 if i32_load(var7 + 108) > 2048 else 0):
            break
        var6 = (var5 + var6)
        i32_store(var7 + 48, (var5 + var6))
        var5 = i32_load(var7 + 112)
        if (1 if i32_load(var7 + 112) > 4096 else 0):
            break
        var6 = (var5 + var6)
        i32_store(var7 + 52, (var5 + var6))
        var5 = i32_load(var7 + 116)
        if (1 if i32_load(var7 + 116) > 8192 else 0):
            break
        var6 = (var5 + var6)
        i32_store(var7 + 56, (var5 + var6))
        var5 = i32_load(var7 + 120)
        if (1 if i32_load(var7 + 120) > 16384 else 0):
            break
        var13 = (var5 + var6)
        i32_store(var7 + 60, (var5 + var6))
        var5 = 0
        if (1 if var3 > 0 else 0):
            if var4:
                while True:  # loop $label6
                    var6 = i32_load((var2 + (var5 << 2)))
                    if (1 if i32_load((var2 + (var5 << 2))) > 0 else 0):
                        var8 = (var7 + (var6 << 2))
                        var6 = i32_load((var7 + (var6 << 2)))
                        if (1 if i32_load((var7 + (var6 << 2))) >= var3 else 0):
                            break
                        i32_store(var8, (var6 + 1))
                        i32_store16((var4 + (var6 << 1)), var5)
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var3 else 0):
                        continue
                    break
                    break  # end loop
                raise RuntimeError('unreachable')
            if (1 if var3 != 1 else 0):
                var6 = (var3 & -2)
                while True:  # loop $label8
                    var10 = (var5 << 2)
                    var9 = i32_load((var2 + (var5 << 2)))
                    if (1 if i32_load((var2 + (var5 << 2))) > 0 else 0):
                        var9 = (var7 + (var9 << 2))
                        i32_store((var7 + (var9 << 2)), (i32_load(var9) + 1))
                    var10 = i32_load((var2 + (var10 | 4)))
                    if (1 if i32_load((var2 + (var10 | 4))) > 0 else 0):
                        var10 = (var7 + (var10 << 2))
                        i32_store((var7 + (var10 << 2)), (i32_load(var10) + 1))
                    var5 = (var5 + 2)
                    var8 = (var8 + 2)
                    if (1 if (var8 + 2) != var6 else 0):
                        continue
                    break  # end loop
            if (1 if (var3 & 1) == 0 else 0):
                break
            var2 = i32_load((var2 + (var5 << 2)))
            if (1 if i32_load((var2 + (var5 << 2))) <= 0 else 0):
                break
            var2 = (var7 + (var2 << 2))
            i32_store((var7 + (var2 << 2)), (i32_load(var2) + 1))
            var13 = i32_load(var7 + 60)
        var6 = (1 << var1)
        var16 = 1
        if (1 if var13 == 1 else 0):
            if (1 if var4 == 0 else 0):
                var11 = var6
                break
            var2 = (i32_load16_u(var4) << 16)
            var5 = var6
            while True:  # loop $label9
                var1 = (var5 - 1)
                i32_store((var0 + ((var5 - 1) << 2)), var2)
                var3 = (1 if var5 > 1 else 0)
                var5 = var1
                if var3:
                    continue
                break  # end loop
            var11 = var6
            break
        var14 = 1
        var3 = 0
        var9 = 0
        if (1 if var1 <= 0 else 0):
            break
        if (1 if var0 == 0 else 0):
            var5 = 1
            while True:  # loop $label11
                var2 = (var16 << 1)
                var16 = ((var16 << 1) - i32_load(((var7 - -64) + (var5 << 2))))
                if (1 if ((var16 << 1) - i32_load(((var7 - -64) + (var5 << 2)))) < 0 else 0):
                    break
                var14 = (var2 + var14)
                var2 = (1 if var1 != var5 else 0)
                var5 = (var5 + 1)
                if var2:
                    continue
                break  # end loop
            break
        var15 = 2
        var12 = 1
        while True:  # loop $label17
            var18 = (var16 << 1)
            var19 = ((var7 - -64) + (var12 << 2))
            var2 = i32_load(((var7 - -64) + (var12 << 2)))
            var16 = ((var16 << 1) - i32_load(((var7 - -64) + (var12 << 2))))
            if (1 if ((var16 << 1) - i32_load(((var7 - -64) + (var12 << 2)))) < 0 else 0):
                break
            if (1 if var2 > 0 else 0):
                if ((var15 - 1) & var6):
                    break
                var20 = (var12 & 255)
                var17 = (1 << (var12 - 1))
                var10 = (var2 + var9)
                while True:  # loop $label16
                    var2 = (var0 + (var3 << 2))
                    var8 = ((i32_load16_u((var4 + (var9 << 1))) << 16) | var20)
                    var5 = var6
                    while True:  # loop $label14
                        var5 = (var5 - var15)
                        i32_store((var2 + ((var5 - var15) << 2)), var8)
                        if (1 if var5 > 0 else 0):
                            continue
                        break  # end loop
                    var8 = var17
                    while True:  # loop $label15
                        var2 = var8
                        var8 = ((var8 & 0xFFFFFFFF) >> 1)
                        if (var2 & var3):
                            continue
                        break  # end loop
                    var3 = ((((var2 - 1) & var3) + var2) if var2 else var3)
                    var9 = (var9 + 1)
                    if (1 if (var9 + 1) != var10 else 0):
                        continue
                    break  # end loop
                i32_store(var19, 0)
                var9 = var10
            var14 = (var14 + var18)
            var15 = (var15 << 1)
            var2 = (1 if var1 == var12 else 0)
            var12 = (var12 + 1)
            if (1 if var2 == 0 else 0):
                continue
            break  # end loop
        break
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    if (1 if var1 <= 14 else 0):
        break
    var17 = var6
    break
    var22 = (var6 - 1)
    var10 = -1
    var15 = 2
    var12 = var0
    var13 = var1
    var17 = var6
    while True:  # loop $label27
        var11 = 0
        var23 = (var16 << 1)
        var18 = (var13 + 1)
        var21 = ((var7 - -64) + ((var13 + 1) << 2))
        var2 = i32_load(((var7 - -64) + ((var13 + 1) << 2)))
        var16 = ((var16 << 1) - i32_load(((var7 - -64) + ((var13 + 1) << 2))))
        if (1 if ((var16 << 1) - i32_load(((var7 - -64) + ((var13 + 1) << 2)))) < 0 else 0):
            break
        if (1 if var2 > 0 else 0):
            var20 = (1 << var13)
            var24 = (var15 - 1)
            var19 = (var18 - var1)
            var25 = ((var18 - var1) & 255)
            var26 = (1 << var19)
            while True:  # loop $label26
                var11 = (var3 & var22)
                if (1 if var10 != (var3 & var22) else 0):
                    var5 = var18
                    var8 = var26
                    var2 = var26
                    var10 = var19
                    if (1 if var13 <= 13 else 0):
                        while True:  # loop $label20
                            var2 = (var8 - i32_load(((var7 - -64) + (var5 << 2))))
                            if (1 if (var8 - i32_load(((var7 - -64) + (var5 << 2)))) <= 0 else 0):
                                var2 = var5
                                break
                            var8 = (var2 << 1)
                            var2 = 15
                            var5 = (var5 + 1)
                            if (1 if (var5 + 1) != 15 else 0):
                                continue
                            break  # end loop
                        var10 = (var2 - var1)
                        var2 = (1 << (var2 - var1))
                    var17 = (var2 + var17)
                    if var0:
                        break
                    var6 = var2
                    var10 = var11
                    break
                if var0:
                    break
                break
                var5 = (var0 + (var11 << 2))
                i32_store8((var0 + (var11 << 2)), (var1 + var10))
                var5 = (var12 + (var6 << 2))
                i32_store16(var5 + 2, ((((((var12 + (var6 << 2)) if var0 else var12) - var0) & 0xFFFFFFFF) >> 2) - var11))
                var6 = var2
                var10 = var11
                var12 = var5
                if (var6 & var24):
                    break
                var2 = (var9 + 1)
                var8 = (var12 + (((var3 & 0xFFFFFFFF) >> var1) << 2))
                var9 = ((i32_load16_u((var4 + (var9 << 1))) << 16) | var25)
                var5 = var6
                while True:  # loop $label24
                    var5 = (var5 - var15)
                    i32_store((var8 + ((var5 - var15) << 2)), var9)
                    if (1 if var5 > 0 else 0):
                        continue
                    break  # end loop
                var9 = var2
                var8 = var20
                while True:  # loop $label25
                    var2 = var8
                    var8 = ((var8 & 0xFFFFFFFF) >> 1)
                    if (var2 & var3):
                        continue
                    break  # end loop
                var5 = i32_load(var21)
                i32_store(var21, (i32_load(var21) - 1))
                var3 = ((((var2 - 1) & var3) + var2) if var2 else var3)
                if (1 if var5 > 1 else 0):
                    continue
                break  # end loop
        var14 = (var14 + var23)
        var15 = (var15 << 1)
        var13 = var18
        if (1 if var18 != 15 else 0):
            continue
        break  # end loop
    var13 = i32_load(var7 + 60)
    var11 = (var17 if (1 if ((var13 << 1) - 1) == var14 else 0) else 0)
    global global0
    global0 = (var7 + 128)
    return var11
    a_c()
    raise RuntimeError('unreachable')
    return 4694


# ==========================================================
# $func288
# ==========================================================
def func288(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0.0
    var7 = 0.0
    var3 = (global0 - 96)
    global global0
    global0 = (global0 - 96)
    var0 = i32_load(var0 + 24)
    if (1 if i32_load(var0 + 24) == 0 else 0):
        break
    var4 = i32_load(var0 + 4)
    if (1 if i32_load(var0 + 4) == 0 else 0):
        break
    if (1 if i32_load(var4 + 8) == 0 else 0):
        break
    var6 = float(var2)
    var7 = float(var1)
    var0 = 0
    while True:  # loop $label3
        var5 = i32_load((i32_load(var4) + ((var0 << 2) | 4)))
        if (1 if i32_load((i32_load(var4) + ((var0 << 2) | 4))) == 0 else 0):
            break
        if i32_load8_u(9142916):
            i32_store(var3 + 88, var5)
            i64_store(var3 + 80, 0)
            f64_store(var3 + 72, var6)
            f64_store(var3 + 64, var7)
            a_b()
            break
        i64_store(var3 + 32, 0)
        i32_store(var3 + 48, var5)
        f64_store(var3 + 40, float(float((i32_load(9142848) * 25))))
        f64_store(var3 + 16, var7)
        f64_store(var3 + 24, var6)
        a_b()
        if (1 if i32_load8_u(9142916) == 0 else 0):
            break
        i32_store(var3 + 4, var5)
        i32_store(var3, (i32_load(9142848) * 25))
        a_b()
        var0 = (var0 + 2)
        if (1 if (var0 + 2) < i32_load(var4 + 8) else 0):
            continue
        break  # end loop
    global global0
    global0 = (var3 + 96)

