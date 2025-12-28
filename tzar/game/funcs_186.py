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
# $func132
# ==========================================================
def func132(var0, var1):
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
    var24 = 0
    var25 = 0
    var26 = 0
    var27 = 0
    var28 = 0
    var29 = 0
    var30 = 0
    var31 = 0
    var32 = 0.0
    var33 = 0.0
    var10 = (global0 - 96)
    global global0
    global0 = (global0 - 96)
    var15 = i32_load(9671176)
    if (1 if i32_load(9671176) >= 4 else 0):
        var14 = ((var15 & 0xFFFFFFFF) // 3)
        var9 = i32_load(9671168)
        while True:  # loop $label0
            var8 = (var9 + (var2 * 12))
            var6 = ((i32_load((var9 + (var2 * 12))) * 404) + 9568096)
            var19 = (i32_load(((i32_load((var9 + (var2 * 12))) * 404) + 9568096) + 220) + i32_load(var8 + 8))
            var3 = ((i32_load(((i32_load((var9 + (var2 * 12))) * 404) + 9568096) + 220) + i32_load(var8 + 8)) if (1 if var3 < var19 else 0) else var3)
            var19 = (i32_load(var6 + 216) + i32_load(var8 + 4))
            var5 = ((i32_load(var6 + 216) + i32_load(var8 + 4)) if (1 if var5 < var19 else 0) else var5)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var14 else 0):
                continue
            break  # end loop
        var5 = (var5 << 4)
        var3 = (var3 << 4)
    if (1 if var15 >= 3 else 0):
        var26 = i32_load(9671192)
        var19 = ((var1 - var3) // 32)
        var31 = ((var0 - var5) // 32)
        var27 = (1 if var0 == 2147483647 else 0)
        while True:  # loop $label32
            var6 = (i32_load(9671168) + (var21 * 12))
            var3 = i32_load((i32_load(9671168) + (var21 * 12)))
            var7 = ((i32_load((i32_load(9671168) + (var21 * 12))) * 404) + 9568096)
            if i32_load8_u(9142409):
                break
            var11 = ((var3 * 72) + 9263856)
            if i32_load(((var3 * 72) + 9263856)):
                break
            var2 = ((var3 << 2) + 9560016)
            if i32_load(((var3 << 2) + 9560016)):
                break
            i32_store(var2, i32_load(9671136))
            var23 = (1 if var3 == i32_load(38472) else 0)
            if (1 if (1 if var3 == i32_load(38472) else 0) == 0 else 0):
                if (1 if var3 != i32_load(38600) else 0):
                    break
            i32_store8(9142410, 1)
            var6 = (i32_load(var7 + 216) << 4)
            var13 = ((i32_load(59140) - (i32_load(var7 + 216) << 4)) // 32)
            var11 = ((i32_load(59132) - var6) // 32)
            var2 = i32_load(9142440)
            var4 = ((var1 - (i32_load(var7 + 220) << 4)) // 32)
            if (1 if i32_load(9142440) <= ((var1 - (i32_load(var7 + 220) << 4)) // 32) else 0):
                break
            var7 = ((var0 - var6) // 32)
            if (1 if var2 <= ((var0 - var6) // 32) else 0):
                break
            if (1 if (var4 | var7) < 0 else 0):
                break
            var2 = (var13 - var4)
            var2 = (var2 >> 31)
            var17 = (((var13 - var4) ^ (var2 >> 31)) - var2)
            var14 = ((((var13 - var4) ^ (var2 >> 31)) - var2) + 1)
            var2 = (var11 - var7)
            var2 = (var2 >> 31)
            var18 = (((var11 - var7) ^ (var2 >> 31)) - var2)
            var9 = ((((var11 - var7) ^ (var2 >> 31)) - var2) + 1)
            var22 = 1
            var15 = 1
            var24 = 1
            var16 = 1
            if (1 if i32_load8_u(9163792) == 0 else 0):
                var5 = (1 if var7 >= var11 else 0)
                var3 = (1 if var7 < var11 else 0)
                var8 = (1 if var17 < var18 else 0)
                var16 = ((1 if var7 >= var11 else 0) if (1 if var17 < var18 else 0) else (1 if var7 < var11 else 0))
                var6 = (1 if var4 < var13 else 0)
                var2 = (1 if var4 >= var13 else 0)
                var24 = ((1 if var4 < var13 else 0) if var8 else (1 if var4 >= var13 else 0))
                var15 = (var3 if var8 else var5)
                var22 = (var2 if var8 else var6)
            i32_store8(9684791, var15)
            i32_store8(9684790, var22)
            i32_store8(9684789, var16)
            var5 = 0
            i32_store8(9684788, var24)
            var7 = (var11 if (1 if var7 > var11 else 0) else var7)
            i32_store(9684772, (var11 if (1 if var7 > var11 else 0) else var7))
            var13 = (var13 if (1 if var4 > var13 else 0) else var4)
            i32_store(9684776, (var13 if (1 if var4 > var13 else 0) else var4))
            i32_store(9684780, var9)
            i32_store(9684784, var14)
            var2 = (var18 - 1)
            var3 = (((1 - var17) * ((var18 - 1) if (1 if var2 <= var18 else 0) else 0)) if (1 if var17 > 1 else 0) else 0)
            if (1 if i32_load(9142396) == 0 else 0):
                break
            while True:  # loop $label9
                var11 = i32_load((i32_load(9142392) + (var5 << 2)))
                if (1 if i32_load((i32_load(9142392) + (var5 << 2))) >= 1073741823 else 0):
                    var6 = (var11 - 1073741823)
                    var4 = i32_load(9299896)
                    if (1 if i32_load(9299896) != i32_load(9299892) else 0):
                        var2 = i32_load(9299888)
                        break
                    var2 = (i32_load(9299900) + var4)
                    i32_store(9299892, (i32_load(9299900) + var4))
                    var8 = i32_load(9299888)
                    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                    if var4:
                        # Unknown: memory.copy []
                    if var8:
                        var4 = i32_load(9299896)
                    i32_store(9299888, var2)
                    i32_store(9299896, (var4 + 1))
                    i32_store((var2 + (var4 << 2)), var6)
                    break
                var4 = i32_load(9299880)
                if (1 if i32_load(9299880) != i32_load(9299876) else 0):
                    var2 = i32_load(9299872)
                    break
                var2 = (i32_load(9299884) + var4)
                i32_store(9299876, (i32_load(9299884) + var4))
                var6 = i32_load(9299872)
                var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                if var4:
                    # Unknown: memory.copy []
                if var6:
                    var4 = i32_load(9299880)
                i32_store(9299872, var2)
                i32_store(9299880, (var4 + 1))
                i32_store((var2 + (var4 << 2)), var11)
                if i32_load8_u(9142916):
                    i32_store(var10 + 48, var11)
                    a_b()
                    break
                i32_store(var10 + 40, var11)
                i64_store(var10 + 32, -4602115869219225600)
                i64_store(var10 + 24, 0)
                i64_store(var10 + 16, 0)
                a_b()
                var5 = (var5 + 1)
                if (1 if (var5 + 1) < i32_load(9142396) else 0):
                    continue
                break  # end loop
            i32_store(9142396, 0)
            var2 = i32_load(9142392)
            if (1 if i32_load(9142392) == 0 else 0):
                break
            var12 = 0
            var2 = (var3 + (var9 * var14))
            i32_store(9142392, func26((-1 if (1 if var2 > 1073741823 else 0) else ((var3 + (var9 * var14)) << 2))))
            while True:  # loop $label17
                var32 = (float(var12) / 100.0)
                var28 = (var7 + var12)
                var29 = ((var7 + var12) + 1)
                var2 = (1 if var12 == 0 else 0)
                var11 = ((1 if var12 == 0 else 0) | (1 if var12 >= var18 else 0))
                var8 = (var22 & (1 if var12 == var18 else 0))
                var14 = (var2 & var24)
                var33 = float((var28 << 5))
                var3 = 0
                while True:  # loop $label16
                    var6 = var3
                    if (1 if ((var15 & (1 if var3 == var17 else 0)) | ((var14 | (var16 & (1 if var3 == 0 else 0))) | var8)) == 0 else 0):
                        break
                    var2 = i32_load(9142440)
                    if (1 if i32_load(9142440) <= var6 else 0):
                        break
                    if (1 if var2 <= var12 else 0):
                        break
                    if (1 if var11 == 0 else 0):
                        break
                    if (1 if var6 == 0 else 0):
                        break
                    if (1 if var6 >= var17 else 0):
                        break
                    break
                    var9 = i32_load(((i32_load((38472 if var23 else 38600)) * 72) + 9263856))
                    if (1 if i32_load(((i32_load((38472 if var23 else 38600)) * 72) + 9263856)) == 0 else 0):
                        break
                    var2 = 0
                    if i32_load8_u(9142917):
                        break
                    var2 = i32_load(9299880)
                    if i32_load(9299880):
                        var2 = (var2 - 1)
                        i32_store(9299880, (var2 - 1))
                        var2 = i32_load((i32_load(9299872) + (var2 << 2)))
                        break
                    var2 = i32_load(9163776)
                    var5 = (i32_load(9163776) + 1)
                    i32_store(9163776, (i32_load(9163776) + 1))
                    var3 = i32_load(9163784)
                    if (1 if var5 < i32_load(9163784) else 0):
                        break
                    i32_store(var10, var3)
                    a_b()
                    i32_store(9163784, (i32_load(9163784) + 40000))
                    var3 = i32_load(9142396)
                    i32_store(9142396, (i32_load(9142396) + 1))
                    i32_store((i32_load(9142392) + (var3 << 2)), var2)
                    var5 = i32_load(9142840)
                    var30 = i32_load(9142440)
                    var4 = (i32_load(9142440) + 2)
                    var25 = (var6 + var13)
                    var3 = ((var6 + var13) + 1)
                    if i32_load((i32_load(9142840) + (((((i32_load(9142440) + 2) + ((var6 + var13) + 1)) * var4) + var29) << 2))):
                        break
                    if i32_load((var5 + (((var3 * var4) + var29) << 2))):
                        break
                    var3 = 0
                    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
                        break
                    if i32_load8_u(9147152):
                        break
                    if i32_load16_u((i32_load(9147376) + (((var25 * var30) + var28) << 1))):
                        break
                    var3 = 1
                    var3 = (var6 + 1)
                    if (1 if var6 != var17 else 0):
                        continue
                    break  # end loop
                var2 = (1 if var12 != var18 else 0)
                var12 = (var12 + 1)
                if var2:
                    continue
                break  # end loop
            break
            if (1 if var27 == 0 else 0):
                var2 = var19
                if (1 if var15 > 3 else 0):
                    break
                var2 = (((var1 - (i32_load(var7 + 220) << 4)) & 0xFFFFFFFF) >> 5)
                break
            var2 = i32_load(9684776)
            var3 = i32_load(9684772)
            if var27:
                break
            if var21:
                break
            if (1 if i32_load(9684772) != var3 else 0):
                break
            if (1 if i32_load(9684776) == var2 else 0):
                break
            if (1 if var21 == 0 else 0):
                i32_store(9684776, var2)
                i32_store(9684772, var3)
            var3 = (i32_load(var6 + 4) + var3)
            var16 = 0
            var13 = i32_load(9142440)
            var6 = (i32_load(var6 + 8) + var2)
            if (1 if i32_load(9142440) <= (i32_load(var6 + 8) + var2) else 0):
                break
            if (1 if var3 >= var13 else 0):
                break
            if (1 if (var3 | var6) < 0 else 0):
                break
            if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
                break
            if i32_load8_u(9147152):
                break
            var5 = i32_load(var7 + 216)
            if (1 if i32_load(var7 + 216) <= 0 else 0):
                break
            var2 = i32_load(var7 + 220)
            if (1 if i32_load(var7 + 220) <= 0 else 0):
                break
            var8 = (var2 + var6)
            var14 = (var3 + var5)
            var9 = i32_load(9147376)
            var2 = var3
            while True:  # loop $label24
                var5 = var6
                if (1 if var2 < var13 else 0):
                    while True:  # loop $label23
                        if (1 if var5 >= var13 else 0):
                            break
                        if (1 if (var2 | var5) < 0 else 0):
                            break
                        if i32_load16_u((var9 + (((var5 * var13) + var2) << 1))):
                            break
                        var5 = (var5 + 1)
                        if (1 if (var5 + 1) < var8 else 0):
                            continue
                        break  # end loop
                var2 = (var2 + 1)
                if (1 if (var2 + 1) < var14 else 0):
                    continue
                break  # end loop
            break
            var16 = func56(var3, var6, var7, i32_load(9142872), 0, 0, 1, 1, 0)
            i32_store(9684800, var16)
            var14 = (var16 ^ 1)
            if (1 if var26 == 0 else 0):
                var2 = 0
                if i32_load8_u(9142917):
                    break
                var2 = i32_load(9299880)
                if i32_load(9299880):
                    var2 = (var2 - 1)
                    i32_store(9299880, (var2 - 1))
                    var2 = i32_load((i32_load(9299872) + (var2 << 2)))
                    break
                var2 = i32_load(9163776)
                var9 = (i32_load(9163776) + 1)
                i32_store(9163776, (i32_load(9163776) + 1))
                var5 = i32_load(9163784)
                if (1 if var9 < i32_load(9163784) else 0):
                    break
                i32_store(var10 + 80, var5)
                a_b()
                i32_store(9163784, (i32_load(9163784) + 40000))
                var5 = i32_load(9671192)
                if (1 if i32_load(9671192) != i32_load(9671188) else 0):
                    var4 = i32_load(9671184)
                    break
                var9 = (i32_load(9671196) + var5)
                i32_store(9671188, (i32_load(9671196) + var5))
                var8 = i32_load(9671184)
                var4 = func26((-1 if (1 if var9 > 1073741823 else 0) else (var9 << 2)))
                if var5:
                    # Unknown: memory.copy []
                if var8:
                    var5 = i32_load(9671192)
                i32_store(9671184, var4)
                i32_store(9671192, (var5 + 1))
                i32_store((var4 + (var5 << 2)), var2)
                break
            var2 = i32_load((i32_load(9671184) + (var20 << 2)))
            var20 = (var20 + 1)
            var5 = 0
            var32 = float((var3 << 5))
            var33 = float((var6 << 5))
            var4 = i32_load(var7 + 20)
            if (1 if i32_load(var7 + 20) == 0 else 0):
                break
            while True:  # loop $label31
                var3 = (var7 + (var5 << 2))
                var2 = i32_load((var7 + (var5 << 2)))
                if (1 if i32_load(i32_load((var7 + (var5 << 2))) + 32) != 6 else 0):
                    if (1 if var26 == 0 else 0):
                        var4 = 0
                        if i32_load8_u(9142917):
                            break
                        var2 = i32_load(9299880)
                        if i32_load(9299880):
                            var2 = (var2 - 1)
                            i32_store(9299880, (var2 - 1))
                            var4 = i32_load((i32_load(9299872) + (var2 << 2)))
                            break
                        var4 = i32_load(9163776)
                        var6 = (i32_load(9163776) + 1)
                        i32_store(9163776, (i32_load(9163776) + 1))
                        var2 = i32_load(9163784)
                        if (1 if var6 < i32_load(9163784) else 0):
                            break
                        i32_store(var10 + 64, var2)
                        a_b()
                        i32_store(9163784, (i32_load(9163784) + 40000))
                        var2 = i32_load(9671192)
                        if (1 if i32_load(9671192) != i32_load(9671188) else 0):
                            var12 = i32_load(9671184)
                            break
                        var6 = (i32_load(9671196) + var2)
                        i32_store(9671188, (i32_load(9671196) + var2))
                        var9 = i32_load(9671184)
                        var12 = func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2)))
                        if var2:
                            # Unknown: memory.copy []
                        if var9:
                            var2 = i32_load(9671192)
                        i32_store(9671184, var12)
                        i32_store(9671192, (var2 + 1))
                        i32_store((var12 + (var2 << 2)), var4)
                        var2 = i32_load(var3)
                        break
                    var4 = i32_load((i32_load(9671184) + (var20 << 2)))
                    var20 = (var20 + 1)
                    var4 = i32_load(var7 + 20)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) < var4 else 0):
                    continue
                break  # end loop
            var21 = (var21 + 1)
            var15 = i32_load(9671176)
            if (1 if (var21 + 1) < ((i32_load(9671176) & 0xFFFFFFFF) // 3) else 0):
                continue
            break  # end loop
    global global0
    global0 = (var10 + 96)
    return func40(var32, var33, float((i32_load(9142440) * 96)), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, var2, var14, var4, 0, 0, 0, 0.0)

