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
# $func46
# ==========================================================
def func46(var0, var1):
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
    var4 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    a_b()
    i32_store(9681836, 0)
    i32_store8(9147141, 0)
    var3 = i32_load(9671120)
    if (1 if i32_load(9671120) == 0 else 0):
        break
    if (1 if i32_load8_u(59186) == 0 else 0):
        while True:  # loop $label10
            var2 = i32_load(((var5 << 2) + 9263072))
            i32_store8(i32_load(((var5 << 2) + 9263072)) + 20, 1)
            var9 = ((1 if i32_load(var2 + 128) != 0 else 0) + var9)
            if (1 if var6 == 0 else 0):
                var7 = 0
                var15 = i32_load(9215968)
                if i32_load(9215968):
                    var16 = i32_load(9561692)
                    var17 = i32_load(9215960)
                    while True:  # loop $label8
                        if i32_load8_u(var2 + 22):
                            break
                        var8 = (var16 + (i32_load((var17 + (var7 << 2))) * 286704))
                        var6 = i32_load(var2 + 4)
                        var18 = i32_load8_u(var2 + 23)
                        if i32_load8_u(var2 + 21):
                            break
                        if (1 if var18 == 0 else 0):
                            break
                        if (1 if i32_load(((var6 * 404) + 9568096) + 264) != 3 else 0):
                            break
                        if i32_load(((var8 + (var6 << 2)) + 281808)):
                            break
                        var21 = i32_load(var2 + 68)
                        if (1 if i32_load(var2 + 68) == 0 else 0):
                            break
                        var10 = 0
                        var3 = 1
                        var11 = 0
                        var13 = 0
                        while True:  # loop $label7
                            var14 = i32_load((var2 + (var10 << 2)) + 28)
                            var19 = i32_load(((i32_load((var2 + (var10 << 2)) + 28) * 404) + 9568096) + 264)
                            var20 = (1 if i32_load(((i32_load((var2 + (var10 << 2)) + 28) * 404) + 9568096) + 264) == 1 else 0)
                            var14 = i32_load(((var8 + (var14 << 2)) + 281808))
                            if (1 if i32_load(((var8 + (var14 << 2)) + 281808)) == 1 else 0):
                                break
                            var3 = ((1 if var19 != 3 else 0) & var3)
                            if var14:
                                break
                            var3 = ((1 if var19 != 0 else 0) & var3)
                            break
                            var13 = (var13 | var20)
                            var11 = (var11 | var20)
                            var10 = (var10 + 1)
                            if (1 if (var10 + 1) != var21 else 0):
                                continue
                            break  # end loop
                        if (((var3 & var13) if (var11 & 1) else var3) & 1):
                            break
                        if (1 if (i32_load(9671124) - 95) > 1 else 0):
                            break
                        if var18:
                            if i32_load8_u(((var6 * 404) + 9568096) + 354):
                                break
                        var3 = ((var6 * 404) + 9568096)
                        if (1 if i32_load(((var6 * 404) + 9568096) + 264) == 1 else 0):
                            if (1 if func180(var8, var6) >= i32_load(var3 + 204) else 0):
                                break
                            var17 = i32_load(9215960)
                            var16 = i32_load(9561692)
                            var15 = i32_load(9215968)
                        var7 = (var7 + 1)
                        if (1 if (var7 + 1) < var15 else 0):
                            continue
                        break  # end loop
                break
                i32_store8(var2 + 20, 0)
                var6 = i32_load8_u(59186)
                var3 = i32_load(9671120)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) < var3 else 0):
                continue
            break  # end loop
        break
    var2 = (var3 & 1)
    if (1 if var3 != 1 else 0):
        var6 = (var3 & -2)
        var3 = 0
        while True:  # loop $label11
            var7 = (var5 << 2)
            var8 = i32_load(((var5 << 2) + 9263072))
            i32_store8(i32_load(((var5 << 2) + 9263072)) + 20, 1)
            var8 = i32_load(var8 + 128)
            var7 = i32_load(((var7 | 4) + 9263072))
            i32_store8(i32_load(((var7 | 4) + 9263072)) + 20, 1)
            var9 = ((var9 + (1 if var8 != 0 else 0)) + (1 if i32_load(var7 + 128) != 0 else 0))
            var5 = (var5 + 2)
            var3 = (var3 + 2)
            if (1 if (var3 + 2) != var6 else 0):
                continue
            break  # end loop
    if (1 if var2 == 0 else 0):
        break
    var2 = i32_load(((var5 << 2) + 9263072))
    i32_store8(i32_load(((var5 << 2) + 9263072)) + 20, 1)
    var9 = (var9 + (1 if i32_load(var2 + 128) != 0 else 0))
    var5 = i32_load(9147120)
    if (1 if i32_load(9147120) == 0 else 0):
        break
    while True:  # loop $label14
        var2 = ((i32_load(9143000) * var5) + var12)
        if (1 if ((i32_load(9143000) * var5) + var12) >= i32_load(9671120) else 0):
            break
        var2 = i32_load(((var2 << 2) + 9263072))
        if (1 if i32_load8_u(i32_load(((var2 << 2) + 9263072)) + 23) == 0 else 0):
            var6 = 0
            break
        var5 = ((i32_load(var2 + 4) * 404) + 9568096)
        var6 = (1 if i32_load(((i32_load(var2 + 4) * 404) + 9568096) + 264) == 3 else 0)
        var5 = i32_load8_u(var5 + 354)
        var3 = i32_load8_u(var2 + 20)
        var7 = i32_load(var2 + 8)
        var8 = i32_load8_u(var2 + 24)
        var10 = i32_load(var2 + 12)
        var11 = i32_load(var2 + 124)
        var2 = i32_load(var2 + 128)
        i32_store(var4 + 32, 0)
        i32_store(var4 + 36, var5)
        i32_store(var4 + 40, var2)
        i32_store(var4 + 44, var6)
        i32_store(var4 + 48, var11)
        i32_store(var4 + 52, var9)
        i32_store(var4 + 56, var10)
        i32_store(var4 + 60, var8)
        i32_store(var4 + 20, var7)
        i32_store(var4 + 24, var3)
        i32_store(var4 + 16, var12)
        i32_store(var4 + 28, i32_load(((var12 << 2) + 9147392)))
        a_b()
        var12 = (var12 + 1)
        var5 = i32_load(9147120)
        if (1 if (var12 + 1) < i32_load(9147120) else 0):
            continue
        break  # end loop
    if var1:
        i32_store(var4, i32_load(9143000))
        i32_store(var4 + 4, (var0 if var0 else i32_load(9671120)))
        a_b()
    i32_store8(9684768, 0)
    global global0
    global0 = (var4 - -64)
    return var4


# ==========================================================
# $func53
# ==========================================================
def func53(var0):
    var1 = 0
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
    var9 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if i32_load8_u(9216068):
        var11 = i32_load(9561692)
        var10 = i32_load(9142872)
        var12 = (i32_load(9561692) + (i32_load(9142872) * 286704))
        var2 = 1
        var7 = ((var0 * 132) + 9216080)
        if (1 if i32_load8_u(((var0 * 132) + 9216080) + 23) == 0 else 0):
            break
        var2 = 0
        var1 = i32_load(var7 + 4)
        # br_table ['$label0', '$label1', '$label1', '$label2', '$label1']
        _br_idx = i32_load(((i32_load(var7 + 4) * 404) + 9568096) + 264)
        break  # br_table
        var2 = 1
        break
        if i32_load(((var12 + (var1 << 2)) + 281808)):
            break
        var14 = i32_load(var7 + 68)
        if (1 if i32_load(var7 + 68) == 0 else 0):
            break
        var1 = 1
        if (1 if var2 == 1 else 0):
            var2 = 0
            while True:  # loop $label6
                var5 = i32_load((var7 + (var3 << 2)) + 28)
                var8 = i32_load(((i32_load((var7 + (var3 << 2)) + 28) * 404) + 9568096) + 264)
                var4 = (1 if i32_load(((i32_load((var7 + (var3 << 2)) + 28) * 404) + 9568096) + 264) == 1 else 0)
                var5 = i32_load(((var12 + (var5 << 2)) + 281808))
                if (1 if i32_load(((var12 + (var5 << 2)) + 281808)) == 1 else 0):
                    break
                var1 = ((1 if var8 != 3 else 0) & var1)
                if var5:
                    break
                var1 = ((1 if var8 != 0 else 0) & var1)
                break
                var6 = (var4 | var6)
                var2 = (var2 | var4)
                var3 = (var3 + 1)
                if (1 if (var3 + 1) != var14 else 0):
                    continue
                break  # end loop
            break
        var2 = 0
        while True:  # loop $label10
            var5 = i32_load((var7 + (var3 << 2)) + 28)
            var8 = i32_load(((i32_load((var7 + (var3 << 2)) + 28) * 404) + 9568096) + 264)
            var4 = (1 if i32_load(((i32_load((var7 + (var3 << 2)) + 28) * 404) + 9568096) + 264) == 1 else 0)
            var5 = (var12 + (var5 << 2))
            var5 = (i32_load(((var12 + (var5 << 2)) + 282828)) + i32_load((var5 + 281808)))
            if (1 if (i32_load(((var12 + (var5 << 2)) + 282828)) + i32_load((var5 + 281808))) == 1 else 0):
                break
            var1 = ((1 if var8 != 3 else 0) & var1)
            if var5:
                break
            var1 = ((1 if var8 != 0 else 0) & var1)
            break
            var6 = (var4 | var6)
            var2 = (var2 | var4)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var14 else 0):
                continue
            break  # end loop
        var14 = (((var1 & var6) if (var2 & 1) else var1) & 1)
        if (1 if i32_load8_u(var7 + 23) == 0 else 0):
            var3 = -1
            var12 = 0
            var2 = 0
            break
        var2 = i32_load(var7 + 4)
        if (1 if i32_load(var7 + 4) == i32_load(38604) else 0):
            break
        if (1 if i32_load(38608) == var2 else 0):
            break
        if (1 if i32_load(38612) == var2 else 0):
            break
        if (1 if i32_load(38616) == var2 else 0):
            break
        if (1 if i32_load(38624) == var2 else 0):
            break
        if (1 if i32_load(38628) == var2 else 0):
            break
        if (1 if i32_load(38632) == var2 else 0):
            break
        if (1 if i32_load(39056) != var2 else 0):
            break
        var13 = (var11 + (var10 * 286704))
        var1 = ((var11 + (var10 * 286704)) + 282828)
        var6 = (i32_load(9561044) << 2)
        var7 = (i32_load(9561040) << 2)
        var8 = (i32_load(9561048) << 2)
        var4 = (i32_load(9561052) << 2)
        var5 = (i32_load(9561056) << 2)
        var16 = (i32_load(9561060) << 2)
        var17 = (i32_load(9561064) << 2)
        var15 = (i32_load(9561068) << 2)
        var3 = (((((((i32_load((((var11 + (var10 * 286704)) + 282828) + (i32_load(9561044) << 2))) + i32_load((var1 + (i32_load(9561040) << 2)))) + i32_load((var1 + (i32_load(9561048) << 2)))) + i32_load((var1 + (i32_load(9561052) << 2)))) + i32_load((var1 + (i32_load(9561056) << 2)))) + i32_load((var1 + (i32_load(9561060) << 2)))) + i32_load((var1 + (i32_load(9561064) << 2)))) + i32_load((var1 + (i32_load(9561068) << 2))))
        var1 = (var13 + 281808)
        break
        var1 = ((var11 + (var10 * 286704)) + (var2 << 2))
        var3 = i32_load((((var11 + (var10 * 286704)) + (var2 << 2)) + 282828))
        var16 = i32_load((var1 + 281808))
        var1 = ((var2 * 404) + 9568096)
        var17 = i32_load8_u(((var2 * 404) + 9568096) + 354)
        var13 = 0
        var7 = i32_load(var1 + 264)
        if (1 if i32_load(var1 + 264) == 1 else 0):
            var14 = (var14 & (1 if func180(var12, var2) < i32_load(var1 + 204) else 0))
            var7 = i32_load(var1 + 264)
        var12 = (var3 if (1 if var7 == 1 else 0) else 0)
        var5 = ((var0 * 132) + 9216080)
        var15 = i32_load(((var0 * 132) + 9216080) + 112)
        if (1 if i32_load(((var0 * 132) + 9216080) + 112) == 0 else 0):
            var3 = -1
            break
        var8 = 0
        var18 = i32_load(9671128)
        var3 = -1
        var19 = (var11 + (var10 * 286704))
        while True:  # loop $label20
            var1 = i32_load(((var19 + (i32_load((var5 + (var8 << 2)) + 72) << 2)) + 284636))
            if (1 if i32_load(((var19 + (i32_load((var5 + (var8 << 2)) + 72) << 2)) + 284636)) == 0 else 0):
                break
            var20 = i32_load(var1 + 8)
            if (1 if i32_load(var1 + 8) == 0 else 0):
                break
            var21 = i32_load(var1)
            var6 = 0
            while True:  # loop $label19
                var1 = i32_load((var21 + (var6 << 2)))
                if (1 if i32_load((var21 + (var6 << 2))) == 0 else 0):
                    break
                var1 = i32_load((var18 + (var1 * 132)) + 20)
                if (1 if i32_load((var18 + (var1 * 132)) + 20) == 0 else 0):
                    break
                var22 = i32_load(var1 + 8)
                if (1 if i32_load(var1 + 8) == 0 else 0):
                    break
                var23 = i32_load(var1)
                var1 = 0
                while True:  # loop $label18
                    var4 = i32_load((var23 + (var1 << 2)))
                    var24 = (1 if var4 > 2147483646 else 0)
                    if (1 if var2 == ((i32_load((var23 + (var1 << 2))) - 2147483647) if (1 if var4 > 2147483646 else 0) else var4) else 0):
                        var12 = (var12 + (1 if var4 < 2147483647 else 0))
                        var13 = (var13 + var24)
                        var3 = (var1 if (1 if var1 < var3 else 0) else var3)
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != var22 else 0):
                        continue
                    break  # end loop
                var6 = (var6 + 1)
                if (1 if (var6 + 1) != var20 else 0):
                    continue
                break  # end loop
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != var15 else 0):
                continue
            break  # end loop
        var1 = i32_load((var11 + (var10 * 286704)) + 281796)
        if (1 if i32_load((var11 + (var10 * 286704)) + 281796) == 0 else 0):
            break
        var10 = i32_load(var1 + 8)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        var4 = ((((var10 - 1) & 0xFFFFFFFF) >> 1) + 1)
        var8 = (((((var10 - 1) & 0xFFFFFFFF) >> 1) + 1) & 3)
        var11 = i32_load(var1)
        var6 = 0
        if (1 if var10 < 7 else 0):
            var1 = 0
            break
        var5 = (var4 & -4)
        var1 = 0
        var4 = 0
        while True:  # loop $label23
            var10 = (var1 << 2)
            var13 = ((((var13 + (1 if i32_load((var11 + ((var1 << 2) | 4))) == var2 else 0)) + (1 if i32_load((var11 + (var10 | 12))) == var2 else 0)) + (1 if i32_load((var11 + (var10 | 20))) == var2 else 0)) + (1 if i32_load((var11 + (var10 | 28))) == var2 else 0))
            var1 = (var1 + 8)
            var4 = (var4 + 4)
            if (1 if (var4 + 4) != var5 else 0):
                continue
            break  # end loop
        if (1 if var8 == 0 else 0):
            break
        while True:  # loop $label24
            var13 = (var13 + (1 if i32_load((var11 + ((var1 << 2) | 4))) == var2 else 0))
            var1 = (var1 + 2)
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != var8 else 0):
                continue
            break  # end loop
        var2 = (1 if var7 == 3 else 0)
        var15 = (1 if var7 == 0 else 0)
        var1 = (1 if var7 == 1 else 0)
        i32_store(var9 + 36, var17)
        i32_store(var9 + 32, var1)
        i32_store(var9 + 28, var15)
        i32_store(var9 + 24, var2)
        i32_store(var9 + 20, var3)
        i32_store(var9 + 16, var13)
        i32_store(var9 + 12, var12)
        i32_store(var9 + 8, var0)
        i32_store(var9 + 4, var16)
        i32_store(var9, var14)
        a_b()
    global global0
    global0 = (var9 + 48)
    return var9

