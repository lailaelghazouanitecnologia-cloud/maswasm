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
# $func81
# ==========================================================
def func81(var0, var1, var2, var3):
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
    var16 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var5 = i32_load8_u(var0 + 122)
    var6 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 188) != 55 else 0):
        if (1 if i32_load(var6 + 264) == 1 else 0):
            break
    var8 = i32_load8_u(var1 + 122)
    var2 = (i32_load((((i32_load8_u(var1 + 122) * 1020) + 9299904) + (var5 << 2))) * var2)
    var6 = (((i32_load((((i32_load8_u(var1 + 122) * 1020) + 9299904) + (var5 << 2))) * var2) & 0xFFFFFFFF) // 100)
    if (1 if var2 < 100 else 0):
        break
    var4 = i32_load8_u(var0 + 125)
    if (1 if i32_load8_u(var0 + 125) == 9 else 0):
        var2 = 0
        if (1 if i32_load(38452) == var5 else 0):
            break
        if (1 if i32_load(38496) == var5 else 0):
            break
        if (1 if i32_load(38756) == var5 else 0):
            break
        if (1 if i32_load(38692) == var5 else 0):
            break
        if (1 if i32_load(38696) == var5 else 0):
            break
        if (1 if i32_load(38776) == var5 else 0):
            break
        if (1 if i32_load(38752) == var5 else 0):
            break
        if (1 if i32_load(38704) == var5 else 0):
            break
    var2 = i32_load(var0 + 60)
    var7 = (var6 * var6)
    var2 = (var2 + var6)
    var7 = i32_load(var0 + 64)
    var2 = ((1 if (1 if var2 > var7 else 0) else (((var6 * var6) & 0xFFFFFFFF) // (var2 + var6))) if (1 if i32_load(var0 + 64) != -1 else 0) else 0)
    var10 = i32_load(9561692)
    var11 = i32_load16_u(var1 + 110)
    var6 = (i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704))
    if (1 if i32_load(38564) == var5 else 0):
        break
    var7 = (var2 if (1 if var2 < var7 else 0) else var7)
    var9 = i32_load16_u(var0 + 110)
    var12 = i32_load(var6 + 278556)
    if i32_load(var6 + 278556):
        var8 = (var12 + (((var9 * 255) + var8) << 2))
        i32_store((var12 + (((var9 * 255) + var8) << 2)), (i32_load(var8) + var7))
    var9 = i32_load(((var10 + (var9 * 286704)) + 278564))
    if (1 if i32_load(((var10 + (var9 * 286704)) + 278564)) == 0 else 0):
        break
    var5 = (var9 + (((var11 * 255) + var5) << 2))
    i32_store((var9 + (((var11 * 255) + var5) << 2)), (i32_load(var5) + var7))
    if (1 if var4 == 3 else 0):
        break
    var5 = i32_load(var0 + 64)
    if (1 if var2 < i32_load(var0 + 64) else 0):
        i32_store(var0 + 64, (var5 - var2))
        if (1 if i32_load(var0 + 92) == 0 else 0):
            break
        if i32_load8_u(9147141):
            break
        i32_store(var16, var2)
        a_b()
        break
    var5 = ((1 if var4 == 4 else 0) | (1 if var4 == 14 else 0))
    i32_store(var0 + 64, 0)
    if (1 if i32_load(i32_load(9142424) + 120) != 3 else 0):
        break
    if (1 if i32_load8_u((i32_load(9143004) + (i32_load16_u(var1 + 110) + (i32_load(9142892) * i32_load16_u(var0 + 110))))) == 0 else 0):
        break
    if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264):
        break
    var2 = 1
    i32_store8(var6 + 286701, 1)
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var12 = (var4 - 1)
    var14 = ((var4 - 1) & 1)
    var7 = (i32_load(var6 + 283908) * var4)
    var9 = i32_load(9561692)
    var8 = i32_load(9143016)
    if (1 if var4 != 2 else 0):
        var4 = (var12 & -2)
        var6 = 0
        while True:  # loop $label6
            if i32_load8_u((var8 + (var2 + var7))):
                i32_store8((var9 + (var2 * 286704)) + 286701, 1)
            var12 = (var2 + 1)
            if i32_load8_u((var8 + (var7 + (var2 + 1)))):
                i32_store8((var9 + (var12 * 286704)) + 286701, 1)
            var2 = (var2 + 2)
            var6 = (var6 + 2)
            if (1 if (var6 + 2) != var4 else 0):
                continue
            break  # end loop
    if (1 if var14 == 0 else 0):
        break
    if (1 if i32_load8_u((var8 + (var2 + var7))) == 0 else 0):
        break
    i32_store8((var9 + (var2 * 286704)) + 286701, 1)
    var2 = (var10 + (var11 * 286704))
    var6 = i32_load(9142424)
    i32_store((var10 + (var11 * 286704)) + 283848, (i32_load(var2 + 283848) + i32_load(i32_load(9142424) + 100)))
    var4 = (var2 + 283852)
    i32_store((var2 + 283852), (i32_load(var4) + i32_load(var6 + 104)))
    var4 = (var2 + 283856)
    i32_store((var2 + 283856), (i32_load(var4) + i32_load(var6 + 108)))
    var2 = (var2 + 283860)
    i32_store((var2 + 283860), (i32_load(var2) + i32_load(var6 + 112)))
    func155(var1, var0, var5)
    var6 = i32_load8_u(var0 + 122)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) == 0 else 0):
        var2 = i32_load(38472)
        break
    var2 = i32_load(38472)
    if ((1 if i32_load(38600) != var6 else 0) & (1 if i32_load(38472) != var6 else 0)):
        break
    if (1 if var5 == 0 else 0):
        break
    if (1 if (var5 & (1 if var2 == var6 else 0)) == 0 else 0):
        var9 = i32_load16_u(var0 + 110)
        break
    i32_store(59200, i32_load(var0 + 28))
    var6 = i32_load(9671128)
    var2 = 1
    var4 = 0
    while True:  # loop $label13
        var10 = (var6 + (i32_load(((var4 << 2) + 59200)) * 132))
        var8 = i32_load16_u(var10 + 112)
        var14 = (i32_load16_u(var10 + 112) + 1)
        var7 = i32_load(9142440)
        var5 = (i32_load(9142440) + 2)
        var9 = i32_load16_u(var0 + 110)
        var11 = i32_load(38472)
        var6 = i32_load(9671128)
        var12 = i32_load(9142840)
        var10 = i32_load16_u(var10 + 114)
        var17 = (1 if var7 <= i32_load16_u(var10 + 114) else 0)
        if (1 if var7 <= i32_load16_u(var10 + 114) else 0):
            break
        if (1 if var7 <= var14 else 0):
            break
        var13 = (var6 + (i32_load((((var8 + (((var5 + var10) + 1) * var5)) << 2) + var12) + 8) * 132))
        if (1 if var11 != i32_load8_u((var6 + (i32_load((((var8 + (((var5 + var10) + 1) * var5)) << 2) + var12) + 8) * 132)) + 122) else 0):
            break
        if (1 if i32_load8_u(var13 + 125) != 4 else 0):
            break
        if (1 if i32_load16_u(var13 + 110) != var9 else 0):
            break
        i32_store(((var2 << 2) + 59200), i32_load(var13 + 28))
        var2 = (var2 + 1)
        if (1 if var10 == 0 else 0):
            break
        if (1 if var7 <= (var10 - 1) else 0):
            break
        if (1 if var7 <= var8 else 0):
            break
        var13 = (var6 + (i32_load((var12 + ((var14 + ((var5 + var10) * var5)) << 2))) * 132))
        if (1 if var11 != i32_load8_u((var6 + (i32_load((var12 + ((var14 + ((var5 + var10) * var5)) << 2))) * 132)) + 122) else 0):
            break
        if (1 if i32_load8_u(var13 + 125) != 4 else 0):
            break
        if (1 if i32_load16_u(var13 + 110) != var9 else 0):
            break
        i32_store(((var2 << 2) + 59200), i32_load(var13 + 28))
        var2 = (var2 + 1)
        var15 = (var10 + 1)
        if var17:
            break
        if (1 if var7 <= (var8 - 1) else 0):
            break
        if (1 if var8 == 0 else 0):
            break
        var13 = (var6 + (i32_load((var12 + ((((var5 + var15) * var5) + var8) << 2))) * 132))
        if (1 if var11 != i32_load8_u((var6 + (i32_load((var12 + ((((var5 + var15) * var5) + var8) << 2))) * 132)) + 122) else 0):
            break
        if (1 if i32_load8_u(var13 + 125) != 4 else 0):
            break
        if (1 if i32_load16_u(var13 + 110) != var9 else 0):
            break
        i32_store(((var2 << 2) + 59200), i32_load(var13 + 28))
        var2 = (var2 + 1)
        if (1 if var7 <= var15 else 0):
            break
        if (1 if var7 <= var8 else 0):
            break
        var5 = (var6 + (i32_load((var12 + ((var14 + (((var5 + var10) + 2) * var5)) << 2))) * 132))
        if (1 if var11 != i32_load8_u((var6 + (i32_load((var12 + ((var14 + (((var5 + var10) + 2) * var5)) << 2))) * 132)) + 122) else 0):
            break
        if (1 if i32_load8_u(var5 + 125) != 4 else 0):
            break
        if (1 if i32_load16_u(var5 + 110) != var9 else 0):
            break
        i32_store(((var2 << 2) + 59200), i32_load(var5 + 28))
        var2 = (var2 + 1)
        if (1 if var4 > 34 else 0):
            break
        var4 = (var4 + 1)
        if (1 if (var4 + 1) < var2 else 0):
            continue
        break  # end loop
    if (1 if i32_load8_u((i32_load(9143004) + (i32_load16_u(var1 + 110) + (i32_load(9142892) * var9)))) == 0 else 0):
        break
    if (1 if var3 == 0 else 0):
        break
    var0 = i32_load(9561692)
    var6 = i32_load16_u(var1 + 110)
    if (1 if i32_load(((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 284008)) == 0 else 0):
        break
    if (1 if i32_load8_u(((i32_load8_u(var1 + 122) * 404) + 9568096) + 334) == 0 else 0):
        break
    var2 = (i32_load(var1 + 80) + 100)
    i32_store(var1 + 80, (i32_load(var1 + 80) + 100))
    var3 = i32_load(var1 + 84)
    var5 = (var0 + (var6 * 286704))
    if (1 if i32_load(var1 + 84) < i32_load(((var0 + (var6 * 286704)) + 284388)) else 0):
        break
    if (1 if i32_load(((var5 + (i32_load(39180) << 2)) + 281808)) != 1 else 0):
        break
    var12 = i32_load16_u(var1 + 114)
    var17 = i32_load(var1 + 28)
    var15 = i32_load16_u(var1 + 112)
    var0 = i32_load(((i32_load(9561692) + (var6 * 286704)) + 284336))
    var2 = (i32_load16_u(var1 + 112) - i32_load(((i32_load(9561692) + (var6 * 286704)) + 284336)))
    var3 = (var0 << 1)
    var18 = ((var0 << 1) + var15)
    if (1 if (i32_load16_u(var1 + 112) - i32_load(((i32_load(9561692) + (var6 * 286704)) + 284336))) >= ((var0 << 1) + var15) else 0):
        break
    var5 = (var12 - var0)
    var19 = (var3 + var12)
    if (1 if (var12 - var0) >= (var3 + var12) else 0):
        break
    var20 = (var0 * var0)
    var21 = (var6 * 286704)
    while True:  # loop $label24
        var3 = (var2 + 1)
        var0 = (var2 - var15)
        var22 = (((var2 - var15) * var0) - 1)
        var0 = var5
        while True:  # loop $label23
            var4 = (var0 - var12)
            if (1 if (var22 + ((var0 - var12) * var4)) > var20 else 0):
                break
            var4 = i32_load(9142440)
            if (1 if i32_load(9142440) <= var0 else 0):
                break
            if (1 if (var0 | var2) < 0 else 0):
                break
            if (1 if var2 >= var4 else 0):
                break
            var23 = (var0 + 1)
            var14 = 0
            while True:  # loop $label22
                var4 = (i32_load(9142440) + 2)
                var4 = i32_load((i32_load(9142840) + ((var3 + ((var23 + ((i32_load(9142440) + 2) * var14)) * var4)) << 2)))
                if (1 if i32_load((i32_load(9142840) + ((var3 + ((var23 + ((i32_load(9142440) + 2) * var14)) * var4)) << 2))) < 3 else 0):
                    break
                if (1 if var4 == var17 else 0):
                    break
                var4 = (i32_load(9671128) + (var4 * 132))
                if (1 if i32_load16_u((i32_load(9671128) + (var4 * 132)) + 110) != var6 else 0):
                    break
                var10 = i32_load8_u(var4 + 122)
                if (1 if i32_load8_u(((i32_load8_u(var4 + 122) * 404) + 9568096) + 334) == 0 else 0):
                    break
                var8 = i32_load(var4 + 84)
                if (1 if i32_load(var4 + 84) > 10 else 0):
                    break
                var7 = (i32_load(var4 + 80) + 100)
                i32_store(var4 + 80, (i32_load(var4 + 80) + 100))
                var9 = (i32_load(9561692) + var21)
                if (1 if var7 < (((var8 * 100) & 0xFFFFFFFF) // i32_load(((i32_load(9561692) + var21) + 284008))) else 0):
                    break
                var11 = i32_load((var9 + 284012))
                var7 = 10
                if i32_load(((var9 + (i32_load(38488) << 2)) + 281808)):
                    break
                if i32_load(((var9 + (i32_load(38848) << 2)) + 281808)):
                    break
                var7 = (10 if i32_load(((var9 + (i32_load(38916) << 2)) + 281808)) else 0)
                if (1 if var8 >= (var7 + var11) else 0):
                    break
                i32_store(var4 + 80, 0)
                var7 = (var8 + 1)
                i32_store(var4 + 84, (var8 + 1))
                var8 = (var9 + 281672)
                i32_store((var9 + 281672), (i32_load(var8) + 1))
                if (1 if i32_load((var9 + 284388)) == var7 else 0):
                    var7 = i32_load(var4 + 24)
                    if (1 if i32_load(var4 + 24) == 0 else 0):
                        var7 = func26(16)
                        i64_store(func26(16), 0)
                        i64_store(var7 + 8, 0)
                        i32_store(var4 + 24, var7)
                    if (1 if i32_load(var7 + 8) == 0 else 0):
                        var8 = func26(16)
                        i32_store(func26(16) + 4, 20)
                        i32_store(var8, func26(80))
                        i64_store(var8 + 8, 8589934592)
                        i32_store(var7 + 8, var8)
                        var10 = 0
                        var7 = i32_load(((i32_load8_u(var4 + 122) * 404) + 9568096) + 196)
                        var24 = ((i32_load((i32_load(9561692) + (i32_load16_u(var4 + 110) * 286704)) + 283936) * 20) % i32_load16_u(((i32_load(((i32_load8_u(var4 + 122) * 404) + 9568096) + 196) << 1) + 9142944)))
                        var25 = ((var7 << 2) + 9142928)
                        while True:  # loop $label21
                            var26 = i32_load16_u((i32_load(var25) + ((var10 + var24) << 1)))
                            if i32_load16_u((i32_load(var25) + ((var10 + var24) << 1))):
                                var8 = i32_load(i32_load(var4 + 24) + 8)
                                var7 = i32_load(i32_load(i32_load(var4 + 24) + 8) + 8)
                                if (1 if i32_load(i32_load(i32_load(var4 + 24) + 8) + 8) != i32_load(var8 + 4) else 0):
                                    var11 = i32_load(var8)
                                    break
                                var11 = (i32_load(var8 + 12) + var7)
                                i32_store(var8 + 4, (i32_load(var8 + 12) + var7))
                                var13 = i32_load(var8)
                                var11 = func26((-1 if (1 if var11 > 1073741823 else 0) else (var11 << 2)))
                                if var7:
                                    # Unknown: memory.copy []
                                if var13:
                                    var7 = i32_load(var8 + 8)
                                i32_store(var8, var11)
                                i32_store(var8 + 8, (var7 + 1))
                                i32_store((var11 + (var7 << 2)), var26)
                            var10 = (var10 + 1)
                            if (1 if (var10 + 1) != 20 else 0):
                                continue
                            break  # end loop
                    i32_store(var9 + 283936, (i32_load(var9 + 283936) + 1))
                    var7 = (var9 + 281636)
                    i32_store((var9 + 281636), (i32_load(var7) + 1))
                    var10 = i32_load8_u(var4 + 122)
                var7 = (var9 + 284020)
                i32_store(var4 + 64, (i32_load(var4 + 64) + i32_load((var9 + 284020))))
                i32_store(var4 + 68, (i32_load(var4 + 68) + i32_load(var7)))
                var7 = i32_load(var4 + 84)
                var9 = (i32_load(var4 + 84) & 1)
                var8 = (1 if i32_load(((var10 * 404) + 9568096) + 224) > 1 else 0)
                i32_store(var4 + 52, (i32_load(var4 + 52) + ((i32_load(var4 + 84) & 1) if (1 if i32_load(((var10 * 404) + 9568096) + 224) > 1 else 0) else 1)))
                i32_store(var4 + 60, (i32_load(var4 + 60) + ((1 if (var7 & 3) == 1 else 0) if var8 else var9)))
                if (1 if i32_load(var4 + 92) == 0 else 0):
                    break
                if i32_load(9140316):
                    if (1 if i32_load(9140320) != i32_load(var4 + 28) else 0):
                        break
                var14 = (var14 + 1)
                if (1 if (var14 + 1) != 3 else 0):
                    continue
                break  # end loop
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var19 else 0):
                continue
            break  # end loop
        var2 = var3
        if (1 if var3 != var18 else 0):
            continue
        break  # end loop
    var6 = i32_load16_u(var1 + 110)
    var3 = i32_load(var1 + 84)
    var2 = i32_load(var1 + 80)
    var0 = i32_load(9561692)
    if (1 if var2 < (((var3 * 100) & 0xFFFFFFFF) // i32_load(((var0 + (var6 * 286704)) + 284008))) else 0):
        break
    var5 = (var0 + (var6 * 286704))
    var4 = i32_load(((var0 + (var6 * 286704)) + 284012))
    var2 = 10
    if i32_load(((var5 + (i32_load(38488) << 2)) + 281808)):
        break
    if i32_load(((var5 + (i32_load(38848) << 2)) + 281808)):
        break
    var2 = (10 if i32_load((((var0 + (var6 * 286704)) + (i32_load(38916) << 2)) + 281808)) else 0)
    if (1 if var3 >= (var2 + var4) else 0):
        break
    func198(var1)
    break
    var2 = i32_load(9671128)
    var3 = i32_load(var1 + 28)
    if (1 if i32_load8_u((i32_load(9143004) + (i32_load16_u(var0 + 110) + (i32_load(9142892) * i32_load16_u((i32_load(9671128) + (i32_load(var1 + 28) * 132)) + 110))))) == 0 else 0):
        break
    if (1 if i32_load8_u(var0 + 126) == 2 else 0):
        break
    var4 = i32_load(9215884)
    var5 = i32_load(var0 + 44)
    var6 = i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4)
    if (1 if ((1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 22 else 0) | (1 if var5 == 0 else 0)) == 0 else 0):
        break
    if i32_load8_u(var0 + 125):
        break
    if i32_load(var0 + 36):
        break
    var1 = i32_load8_u(var0 + 122)
    if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 260):
        break
    if (1 if i32_load8_u(var0 + 129) != 5 else 0):
        break
    if (1 if var6 != 6 else 0):
        break
    var7 = i32_load16_u(var0 + 114)
    var6 = (var2 + (var3 * 132))
    var1 = (i32_load16_u(var0 + 114) - i32_load16_u((var2 + (var3 * 132)) + 114))
    var9 = i32_load16_u(var0 + 112)
    var1 = (i32_load16_u(var0 + 112) - i32_load16_u(var6 + 112))
    var1 = (((i32_load16_u(var0 + 114) - i32_load16_u((var2 + (var3 * 132)) + 114)) * var1) + ((i32_load16_u(var0 + 112) - i32_load16_u(var6 + 112)) * var1))
    var6 = ((i32_load8_u(var6 + 122) * 404) + 9568096)
    if (1 if i32_load(((i32_load8_u(var6 + 122) * 404) + 9568096) + 264) == 1 else 0):
        var1 = (var1 if (1 if i32_load(var6 + 268) == 1 else 0) else (var1 + 100))
    var6 = (var2 + (i32_load((var4 + ((var5 << 4) | 12))) * 132))
    var5 = (var7 - i32_load16_u((var2 + (i32_load((var4 + ((var5 << 4) | 12))) * 132)) + 114))
    var5 = (var9 - i32_load16_u(var6 + 112))
    var5 = (((var7 - i32_load16_u((var2 + (i32_load((var4 + ((var5 << 4) | 12))) * 132)) + 114)) * var5) + ((var9 - i32_load16_u(var6 + 112)) * var5))
    var6 = i32_load8_u(var6 + 122)
    if (1 if i32_load(((i32_load8_u(var6 + 122) * 404) + 9568096) + 264) == 1 else 0):
    else:
    if (1 if var5 <= var1 else 0):
        break
    var1 = i32_load8_u(var0 + 122)
    var1 = ((var1 * 404) + 9568096)
    if (1 if i32_load(((var1 * 404) + 9568096) + 228) == 0 else 0):
        if i32_load(var1 + 260):
            break
    var6 = i32_load(var0 + 28)
    var5 = i32_load(((i32_load8_u((var2 + (i32_load(var0 + 28) * 132)) + 122) * 404) + 9568096) + 228)
    if (1 if i32_load(((i32_load8_u((var2 + (i32_load(var0 + 28) * 132)) + 122) * 404) + 9568096) + 228) == 0 else 0):
        break
    var1 = i32_load(((i32_load8_u((var2 + (var3 * 132)) + 122) * 404) + 9568096) + 216)
    if (1 if i32_load(((i32_load8_u((var2 + (var3 * 132)) + 122) * 404) + 9568096) + 216) == 0 else 0):
        break
    var4 = (var2 + (var3 * 132))
    var7 = i32_load16_u((var2 + (var3 * 132)) + 114)
    var2 = (var2 + (var6 * 132))
    var9 = i32_load16_u((var2 + (var6 * 132)) + 114)
    var8 = i32_load16_u(var4 + 112)
    var10 = i32_load16_u(var2 + 112)
    var5 = (var5 * var5)
    var6 = 0
    var4 = 1
    while True:  # loop $label32
        var2 = (var9 - (var6 + var7))
        var11 = ((var9 - (var6 + var7)) * var2)
        var2 = 0
        while True:  # loop $label30
            var12 = (var10 - (var2 + var8))
            if (1 if var5 > (((var10 - (var2 + var8)) * var12) + var11) else 0):
                var2 = (var2 + 1)
                if (1 if var1 != (var2 + 1) else 0):
                    continue
                break
            break  # end loop
        if (1 if var4 == 0 else 0):
            break
        break
        var6 = (var6 + 1)
        var4 = (1 if (var6 + 1) < var1 else 0)
        if (1 if var1 != var6 else 0):
            continue
        break  # end loop
    break
    func103(var0)
    global global0
    global0 = (var16 + 16)
    return func28(1, 1)

