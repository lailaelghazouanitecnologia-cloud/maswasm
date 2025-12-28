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
# $func28
# ==========================================================
def func28(var0, var1):
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
    var9 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    if i32_load8_u(9147152):
        break
    if (1 if i32_load(40600) == 0 else 0):
        break
    if (1 if var0 == 0 else 0):
        i32_store(9671120, 0)
        i32_store(9263840, 0)
        i32_store(9671124, 0)
        while True:  # loop $label1
            var0 = ((var4 * 132) + 9216080)
            i32_store(((var4 * 132) + 9216080) + 116, 0)
            i32_store(var0 + 16, 0)
            i32_store16(var0 + 21, 0)
            i64_store(var0 + 124, 0)
            i32_store8(var0 + 24, 0)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != 356 else 0):
                continue
            break  # end loop
        # Unknown: memory.fill []
        i32_store(9215968, 0)
        var0 = i32_load(9213808)
        i32_store8(59186, (1 if i32_load(9213808) != 0 else 0))
        if (1 if var0 == 0 else 0):
            i32_store(9263840, 0)
            break
        var23 = i32_load(9671128)
        while True:  # loop $label39
            var8 = (var23 + (i32_load(((var24 << 2) + 9173808)) * 132))
            var6 = i32_load16_u((var23 + (i32_load(((var24 << 2) + 9173808)) * 132)) + 110)
            if (1 if var10 == 0 else 0):
                break
            var0 = 0
            var3 = i32_load(9215960)
            while True:  # loop $label4
                if (1 if var6 != i32_load((var3 + (var0 << 2))) else 0):
                    var0 = (var0 + 1)
                    if (1 if var10 != (var0 + 1) else 0):
                        continue
                    break
                break  # end loop
            var3 = var6
            break
            if (1 if i32_load(9215964) != var10 else 0):
                var0 = i32_load(9215960)
                break
            var0 = (i32_load(9215972) + var10)
            i32_store(9215964, (i32_load(9215972) + var10))
            var3 = i32_load(9215960)
            var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
            if var10:
                # Unknown: memory.copy []
            if var3:
                var23 = i32_load(9671128)
                var10 = i32_load(9215968)
            i32_store(9215960, var0)
            var3 = i32_load16_u(var8 + 110)
            i32_store(9215968, (var10 + 1))
            i32_store((var0 + (var10 << 2)), var6)
            var10 = i32_load(9215968)
            var25 = i32_load8_u(var8 + 125)
            if (1 if ((i32_load8_u(var8 + 125) - 9) & 255) < 3 else 0):
                break
            var2 = i32_load8_u(var8 + 122)
            var14 = ((i32_load8_u(var8 + 122) * 404) + 9568096)
            if (1 if i32_load8_u(((i32_load8_u(var8 + 122) * 404) + 9568096) + 353) == 0 else 0):
                i32_store8(59186, 0)
            var15 = i32_load(9561692)
            if (1 if var25 != 5 else 0):
                if (1 if i32_load((i32_load(9215884) + (i32_load(var8 + 44) << 4)) + 4) != 34 else 0):
                    break
            var6 = func26(4)
            i32_store(func26(4), 6)
            var13 = 1
            break
            if (1 if var2 == i32_load(38852) else 0):
                if i32_load((var15 + (var3 * 286704)) + 283912):
                    break
            var6 = i32_load(var14 + 232)
            var13 = i32_load(var14 + 236)
            var0 = i32_load(var8 + 24)
            if (1 if i32_load(var8 + 24) == 0 else 0):
                break
            var4 = i32_load(var0)
            if (1 if i32_load(var0) == 0 else 0):
                break
            var0 = i32_load(var4)
            if (1 if i32_load(var4) == 0 else 0):
                break
            var13 = i32_load(var4 + 8)
            var6 = var0
            var12 = i32_load(var8 + 20)
            if (1 if i32_load(var8 + 20) == 0 else 0):
                break
            if (1 if i32_load(var14 + 264) != 1 else 0):
                break
            if (1 if i32_load(38540) == var2 else 0):
                break
            if (1 if i32_load(38812) == var2 else 0):
                break
            if (1 if i32_load(38888) == var2 else 0):
                break
            if var13:
                var7 = i32_load((var15 + (var3 * 286704)) + 281796)
                var2 = 0
                while True:  # loop $label15
                    var5 = ((i32_load((var6 + (var2 << 2))) * 132) + 9216080)
                    var17 = i32_load(((i32_load((var6 + (var2 << 2))) * 132) + 9216080) + 4)
                    i32_store(((i32_load(((i32_load((var6 + (var2 << 2))) * 132) + 9216080) + 4) << 2) + 9143024), var2)
                    i32_store8(var5 + 21, 1)
                    var2 = (var2 + 1)
                    if (1 if var7 == 0 else 0):
                        break
                    if (1 if i32_load8_u(var5 + 23) == 0 else 0):
                        break
                    var11 = i32_load(var7 + 8)
                    if (1 if i32_load(var7 + 8) == 0 else 0):
                        break
                    var16 = ((((var11 - 1) & 0xFFFFFFFF) >> 1) + 1)
                    var19 = (((((var11 - 1) & 0xFFFFFFFF) >> 1) + 1) & 1)
                    var18 = i32_load(var8 + 28)
                    var4 = i32_load(var7)
                    var0 = 0
                    if (1 if var11 >= 3 else 0):
                        var20 = (var16 & -2)
                        var11 = 0
                        while True:  # loop $label14
                            var16 = (var0 << 2)
                            if (1 if i32_load((var4 + (var0 << 2))) != var18 else 0):
                                break
                            if (1 if i32_load((var4 + (var16 | 4))) != var17 else 0):
                                break
                            i32_store(var5 + 128, 2147483647)
                            if (1 if i32_load((var4 + (var16 | 8))) != var18 else 0):
                                break
                            if (1 if i32_load((var4 + (var16 | 12))) != var17 else 0):
                                break
                            i32_store(var5 + 128, 2147483647)
                            var0 = (var0 + 4)
                            var11 = (var11 + 2)
                            if (1 if (var11 + 2) != var20 else 0):
                                continue
                            break  # end loop
                    if (1 if var19 == 0 else 0):
                        break
                    var0 = (var0 << 2)
                    if (1 if i32_load((var4 + (var0 << 2))) != var18 else 0):
                        break
                    if (1 if i32_load((var4 + (var0 | 4))) != var17 else 0):
                        break
                    i32_store(var5 + 128, 2147483647)
                    if (1 if var2 != var13 else 0):
                        continue
                    break  # end loop
            if i32_load(var12 + 8):
                var11 = i32_load(var12)
                var7 = 0
                while True:  # loop $label20
                    var5 = i32_load((var11 + (var7 << 2)))
                    if (1 if i32_load((var11 + (var7 << 2))) >= 2147483647 else 0):
                        var5 = (var5 - 2147483647)
                        var0 = ((i32_load((((var5 - 2147483647) << 2) + 9143024)) << 2) + 9147392)
                        var2 = i32_load(((i32_load((((var5 - 2147483647) << 2) + 9143024)) << 2) + 9147392))
                        var4 = (1073741824 if (1 if var2 <= 1073741824 else 0) else i32_load(((i32_load((((var5 - 2147483647) << 2) + 9143024)) << 2) + 9147392)))
                        break
                    var0 = ((i32_load(((var5 << 2) + 9143024)) << 2) + 9147392)
                    var4 = i32_load(((i32_load(((var5 << 2) + 9143024)) << 2) + 9147392))
                    if (1 if i32_load(((i32_load(((var5 << 2) + 9143024)) << 2) + 9147392)) > 1073741823 else 0):
                        break
                    i32_store(var0, (var4 + 1))
                    var7 = (var7 + 1)
                    var0 = 0
                    if var13:
                        while True:  # loop $label19
                            var2 = ((i32_load((var6 + (var0 << 2))) * 132) + 9216080)
                            if (1 if i32_load8_u(((i32_load((var6 + (var0 << 2))) * 132) + 9216080) + 23) == 0 else 0):
                                break
                            if (1 if i32_load(var2 + 4) != var5 else 0):
                                break
                            if i32_load(var2 + 128):
                                break
                            i32_store(var2 + 128, var7)
                            var0 = (var0 + 1)
                            if (1 if (var0 + 1) != var13 else 0):
                                continue
                            break  # end loop
                    if (1 if var7 < i32_load(var12 + 8) else 0):
                        continue
                    break  # end loop
            var2 = i32_load((var15 + (var3 * 286704)) + 281796)
            if (1 if i32_load((var15 + (var3 * 286704)) + 281796) == 0 else 0):
                break
            if (1 if i32_load8_u(var8 + 125) == 14 else 0):
                break
            var4 = i32_load(var2 + 8)
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            var5 = i32_load(var2)
            var0 = 0
            while True:  # loop $label21
                var7 = (var0 << 2)
                if (1 if i32_load((var5 + (var0 << 2))) == i32_load(var8 + 28) else 0):
                    var4 = ((i32_load(((i32_load((var5 + (var7 | 4))) << 2) + 9143024)) << 2) + 9147392)
                    var4 = i32_load(var4)
                    i32_store(((i32_load(((i32_load((var5 + (var7 | 4))) << 2) + 9143024)) << 2) + 9147392), ((1073741824 if (1 if var4 <= 1073741824 else 0) else i32_load(var4)) + 1))
                    var4 = i32_load(var2 + 8)
                var0 = (var0 + 2)
                if (1 if (var0 + 2) < var4 else 0):
                    continue
                break  # end loop
            if (1 if var13 == 0 else 0):
                break
            var12 = 0
            var4 = (var15 + (var3 * 286704))
            var17 = (((var15 + (var3 * 286704)) + (i32_load(39144) << 2)) + 281808)
            var18 = (var4 + 281796)
            var16 = ((i32_load(9143364) << 2) + 9147392)
            var19 = (var4 + 283868)
            var20 = (var4 + 283916)
            var7 = i32_load(9213808)
            while True:  # loop $label38
                var0 = i32_load((var6 + (var12 << 2)))
                if (1 if i32_load((var6 + (var12 << 2))) <= 317 else 0):
                    # br_table ['$label22', '$label23', '$label22', '$label24']
                    _br_idx = (var0 - 186)
                    break  # br_table
                    if (1 if var0 != 4 else 0):
                        break
                    break
                if (1 if var0 != 318 else 0):
                    if (1 if var0 != 350 else 0):
                        break
                    var0 = 350
                    if (1 if i32_load(var8 + 84) >= 3 else 0):
                        break
                    break
                var0 = (323 if i32_load(var20) else 318)
                var3 = ((var0 * 132) + 9216080)
                var26 = i32_load(((var0 * 132) + 9216080) + 12)
                if (1 if i32_load(((var0 * 132) + 9216080) + 12) != 85 else 0):
                    break
                if (1 if i32_load(var17) != 1 else 0):
                    break
                i32_store(var16, i32_load(var19))
                var2 = i32_load8_u(var3 + 23)
                if i32_load8_u(var3 + 23):
                    var0 = i32_load(var3 + 4)
                    if (1 if i32_load(((i32_load(var3 + 4) * 404) + 9568096) + 264) != 3 else 0):
                        break
                    var0 = (var4 + (var0 << 2))
                    if i32_load(((var4 + (var0 << 2)) + 281808)):
                        i32_store(var3 + 124, 1)
                    if (1 if i32_load((var0 + 282828)) == 0 else 0):
                        break
                    i32_store(var3 + 124, 2)
                    break
                # br_table ['$label27', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label26', '$label27', '$label26']
                _br_idx = (var25 - 4)
                break  # br_table
                i32_store8(var3 + 22, 1)
                i32_store(var3 + 124, 3)
                var27 = (i32_load(var3 + 16) + 1)
                i32_store(var3 + 16, (i32_load(var3 + 16) + 1))
                var0 = 0
                var5 = i32_load(var8 + 24)
                if (1 if i32_load(var8 + 24) == 0 else 0):
                    break
                var5 = i32_load(var5)
                if (1 if i32_load(var5) == 0 else 0):
                    break
                if (1 if i32_load(var5) == 0 else 0):
                    break
                var0 = (1 if var12 >= i32_load(var14 + 236) else 0)
                i32_store8(var3 + 21, var0)
                if (1 if var7 != 1 else 0):
                    break
                var11 = i32_load(var8 + 20)
                if (1 if i32_load(var8 + 20) == 0 else 0):
                    break
                if (1 if var2 == 0 else 0):
                    break
                if (1 if i32_load(var14 + 264) != 1 else 0):
                    break
                # br_table ['$label30', '$label29', '$label29', '$label30', '$label29']
                _br_idx = i32_load(((i32_load(var3 + 4) * 404) + 9568096) + 264)
                break  # br_table
                i32_store8(var3 + 21, 1)
                var28 = i32_load(var3 + 68)
                if (1 if i32_load(var3 + 68) == 0 else 0):
                    break
                var2 = 0
                while True:  # loop $label35
                    var15 = i32_load((var3 + (var2 << 2)) + 28)
                    if (1 if i32_load(((i32_load((var3 + (var2 << 2)) + 28) * 404) + 9568096) + 264) != 3 else 0):
                        break
                    var21 = i32_load(var11 + 8)
                    if i32_load(var11 + 8):
                        var22 = i32_load(var11)
                        var5 = 0
                        while True:  # loop $label33
                            var0 = i32_load((var22 + (var5 << 2)))
                            if (1 if ((i32_load((var22 + (var5 << 2))) - 2147483647) if (1 if var0 > 2147483646 else 0) else var0) == var15 else 0):
                                break
                            var5 = (var5 + 1)
                            if (1 if (var5 + 1) != var21 else 0):
                                continue
                            break  # end loop
                    var0 = i32_load(var18)
                    if (1 if i32_load(var18) == 0 else 0):
                        break
                    var21 = i32_load(var0 + 8)
                    if (1 if i32_load(var0 + 8) == 0 else 0):
                        break
                    var22 = i32_load(var8 + 28)
                    var5 = i32_load(var0)
                    var0 = 0
                    while True:  # loop $label34
                        var29 = (var0 << 2)
                        if (1 if var22 == i32_load((var5 + (var0 << 2))) else 0):
                            if (1 if i32_load((var5 + (var29 | 4))) == var15 else 0):
                                break
                        var0 = (var0 + 2)
                        if (1 if (var0 + 2) < var21 else 0):
                            continue
                        break  # end loop
                    i32_store8(var3 + 21, 0)
                    break
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) != var28 else 0):
                        continue
                    break  # end loop
                var2 = i32_load(var14 + 164)
                if (1 if i32_load(var14 + 164) < 2 else 0):
                    break
                var5 = i32_load(var14 + 160)
                var0 = 1
                while True:  # loop $label37
                    var11 = (var5 + (var0 << 2))
                    if (1 if var26 != i32_load((var5 + (var0 << 2))) else 0):
                        var0 = (var0 + 2)
                        if (1 if (var0 + 2) < var2 else 0):
                            continue
                        break
                    break  # end loop
                if (1 if var0 < 0 else 0):
                    break
                var0 = i32_load((var11 - 4))
                var2 = i32_load(var3 + 116)
                if i32_load(var3 + 116):
                    var2 = (1 if var0 == var2 else 0)
                    var0 = 1
                    if var2:
                        break
                i32_store(var3 + 116, var0)
                if (1 if var7 != var27 else 0):
                    break
                var0 = i32_load(9671120)
                i32_store(9671120, (i32_load(9671120) + 1))
                i32_store(((var0 << 2) + 9263072), var3)
                var12 = (var12 + 1)
                if (1 if (var12 + 1) != var13 else 0):
                    continue
                break  # end loop
            var24 = (var24 + 1)
            if (1 if (var24 + 1) < i32_load(9213808) else 0):
                continue
            break  # end loop
        var0 = 0
        i32_store(9263840, 0)
        var8 = i32_load(9671120)
        if (1 if i32_load(9671120) == 0 else 0):
            break
        var6 = 0
        while True:  # loop $label41
            var3 = i32_load(((var0 << 2) + 9263072))
            if (1 if i32_load(((var0 << 2) + 9263072)) == 0 else 0):
                break
            var10 = i32_load(var3 + 116)
            if (1 if i32_load(var3 + 116) < 2 else 0):
                break
            var2 = ((var6 << 2) + 9263328)
            i32_store(((var6 << 2) + 9263328), var10)
            i32_store(var2 + 4, i32_load(var3 + 12))
            var6 = (var6 + 2)
            i32_store(9263840, (var6 + 2))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var8 else 0):
                continue
            break  # end loop
    var0 = i32_load(9213820)
    if i32_load(9213820):
        if var1:
            break
        var1 = ((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096)
        var6 = i32_load(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 48)
        if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 48) == 0 else 0):
            break
        i32_store(var9 + 64, i32_load((i32_load(var1 + 44) + ((i32_load(9142848) % var6) << 2))))
        a_b()
        var0 = i32_load(9213820)
        break
    if i32_load8_u(9147336):
        a_b()
    var3 = i32_load(9213808)
    # br_table ['$label43', '$label44', '$label45']
    _br_idx = i32_load(9213808)
    break  # br_table
    if var1:
        break
    var0 = ((i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) * 404) + 9568096)
    var1 = i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) * 404) + 9568096) + 48)
    if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) * 404) + 9568096) + 48) == 0 else 0):
        break
    i32_store(var9 + 48, i32_load((i32_load(var0 + 44) + ((i32_load(9142848) % var1) << 2))))
    a_b()
    break
    var8 = i32_load(38528)
    var13 = i32_load(9671128)
    var1 = i32_load(i32_load(9215960))
    var4 = 0
    var6 = 0
    var5 = 0
    var7 = 0
    var11 = 0
    var2 = 0
    var12 = 0
    var10 = 0
    while True:  # loop $label47
        var0 = (var13 + (i32_load(((var4 << 2) + 9173808)) * 132))
        var14 = i32_load8_u(var0 + 122)
        var5 = ((0 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) else i32_load((var13 + (i32_load(((var4 << 2) + 9173808)) * 132)) + 84)) + var5)
        var11 = (i32_load(var0 + 60) + var11)
        var2 = (i32_load(var0 + 52) + var2)
        var12 = (i32_load(var0 + 68) + var12)
        var10 = (i32_load(var0 + 64) + var10)
        var7 = ((i32_load(var0 + 80) if (1 if var8 == var14 else 0) else 0) + var7)
        var0 = i32_load(var0 + 16)
        if i32_load(var0 + 16):
        else:
        var6 = (0 + var6)
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var3 else 0):
            continue
        break  # end loop
    func52(189, 0)
    var0 = (i32_load(9561692) + (var1 * 286704))
    var3 = i32_load((i32_load(9561692) + (var1 * 286704)) + 284628)
    var0 = i32_load(var0 + 284616)
    i32_store(var9 + 20, var2)
    i32_store(var9 + 24, var11)
    i32_store(var9 + 28, var7)
    i32_store(var9 + 32, var5)
    i32_store(var9 + 36, var6)
    i32_store(var9 + 16, (var0 if var0 else var3))
    i32_store(var9, i32_load(9213808))
    i32_store(var9 + 4, var10)
    i32_store(var9 + 8, var12)
    i32_store(var9 + 12, var1)
    a_b()
    break
    if i32_load8_u(9147152):
        break
    func52((207 if i32_load8_u(9143020) else 0), 0)
    a_b()
    global global0
    global0 = (var9 + 80)
    return func57(0)

