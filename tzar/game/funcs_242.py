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
# $func133
# ==========================================================
def func133(var0, var1, var2):
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
    var11 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var16 = i32_load8_u(9216060)
    var17 = i32_load(var0 + 40)
    var22 = i32_load(var0 + 36)
    var25 = i32_load(var0 + 32)
    var12 = i32_load(var0 + 28)
    var13 = i32_load(var0 + 24)
    var20 = i32_load(var0 + 20)
    var21 = i32_load(var0 + 16)
    var9 = i32_load(var0 + 12)
    var23 = i32_load(var0 + 8)
    var24 = i32_load(var0 + 4)
    var5 = i32_load(var0)
    if (1 if i32_load8_u(9142412) == 0 else 0):
        var8 = i32_load(9561692)
        var7 = i32_load(((var5 * 404) + 9568096) + 180)
        if (1 if i32_load(((var5 * 404) + 9568096) + 180) == 0 else 0):
            break
        if (1 if i32_load8_u(var7 + 23) == 0 else 0):
            break
        var0 = i32_load(var7 + 4)
        if (1 if i32_load(((i32_load(var7 + 4) * 404) + 9568096) + 264) != 3 else 0):
            break
        if i32_load((((var8 + (var9 * 286704)) + (var0 << 2)) + 281808)):
            break
        var19 = i32_load(var7 + 68)
        if (1 if i32_load(var7 + 68) == 0 else 0):
            break
        var0 = 0
        var4 = 1
        var14 = (var8 + (var9 * 286704))
        while True:  # loop $label5
            var18 = i32_load((var7 + (var0 << 2)) + 28)
            var10 = i32_load(((i32_load((var7 + (var0 << 2)) + 28) * 404) + 9568096) + 264)
            var15 = (1 if i32_load(((i32_load((var7 + (var0 << 2)) + 28) * 404) + 9568096) + 264) == 1 else 0)
            var18 = i32_load(((var14 + (var18 << 2)) + 281808))
            if (1 if i32_load(((var14 + (var18 << 2)) + 281808)) == 1 else 0):
                break
            var4 = ((1 if var10 != 3 else 0) & var4)
            if var18:
                break
            var4 = ((1 if var10 != 0 else 0) & var4)
            break
            var3 = (var3 | var15)
            var6 = (var6 | var15)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var19 else 0):
                continue
            break  # end loop
        if (1 if (((var3 & var4) if (var6 & 1) else var4) & 1) == 0 else 0):
            break
        if i32_load8_u((var8 + (var9 * 286704)) + 286696):
            break
    if (1 if var21 == 0 else 0):
        break
    if (1 if var20 == 0 else 0):
        break
    var18 = (var23 + 1)
    var26 = (var24 + 1)
    var27 = (var20 - 1)
    var28 = (var21 - 1)
    var19 = ((var5 << 2) + 9560016)
    var29 = ((var5 * 72) + 9263856)
    var7 = ((var5 * 404) + 9568096)
    var16 = (((((((((((((((0 if var16 else var17) if (1 if var5 != i32_load(38500) else 0) else 0) if (1 if var5 != i32_load(38636) else 0) else 0) if (1 if var5 != i32_load(39056) else 0) else 0) if (1 if var5 != i32_load(38632) else 0) else 0) if (1 if var5 != i32_load(38628) else 0) else 0) if (1 if var5 != i32_load(38624) else 0) else 0) if (1 if var5 != i32_load(38616) else 0) else 0) if (1 if var5 != i32_load(38612) else 0) else 0) if (1 if var5 != i32_load(38608) else 0) else 0) if (1 if var5 != i32_load(38604) else 0) else 0) if (1 if var5 != i32_load(38472) else 0) else 0) if (1 if var5 != i32_load(38600) else 0) else 0) if (1 if var5 != i32_load(38620) else 0) else 0) if (1 if var5 != i32_load(38560) else 0) else 0)
    var30 = (1 if var13 == 0 else 0)
    var31 = (1 if var12 == 0 else 0)
    var32 = (1 if var5 > 254 else 0)
    var33 = (var5 * 36)
    var15 = 0
    while True:  # loop $label33
        var34 = ((1 if var15 == var28 else 0) & (1 if var25 != 0 else 0))
        var17 = (var15 + var24)
        var35 = (var30 | (1 if var15 != 0 else 0))
        var0 = 0
        while True:  # loop $label32
            if (1 if (((1 if var0 == var27 else 0) & (1 if var22 != 0 else 0)) | ((1 if (var35 & (var31 | (1 if var0 != 0 else 0))) == 0 else 0) | var34)) == 0 else 0):
                break
            var3 = i32_load(9142440)
            var4 = (var0 + var23)
            if (1 if i32_load(9142440) <= (var0 + var23) else 0):
                break
            if (1 if (var4 | var17) < 0 else 0):
                break
            if (1 if var3 <= var17 else 0):
                break
            var10 = i32_load8_u(9142412)
            if (1 if i32_load8_u(9142412) == 0 else 0):
                if var32:
                    break
                if (1 if i32_load(var7 + 264) != 1 else 0):
                    break
            var12 = i32_load(38500)
            var13 = (1 if var5 == i32_load(38500) else 0)
            var6 = (1 if var5 == i32_load(38500) else 0)
            if (1 if i32_load(38636) == var5 else 0):
                var8 = i32_load(9561692)
                var3 = (i32_load(9561692) + (var9 * 286704))
                var14 = (i32_load((i32_load(9561692) + (var9 * 286704)) + 283976) + 1)
                if (1 if (i32_load((i32_load(9561692) + (var9 * 286704)) + 283976) + 1) > (i32_load((var3 + 284136)) + i32_load(var3 + 283980)) else 0):
                    break
                var6 = 1
                if (1 if var14 > i32_load((var3 + 284000)) else 0):
                    break
            var16 = (0 if i32_load(i32_load(9142424) + 156) else var16)
            if var2:
                break
            if i32_load8_u(9147210):
                break
            if (1 if var10 == 0 else 0):
                break
            var9 = i32_load(9142872)
            var6 = 1
            break
            var8 = (i32_load(9561692) + (var9 * 286704))
            var3 = i32_load((((i32_load(9561692) + (var9 * 286704)) + var33) + 269376))
            var3 = (i32_load((((i32_load(9561692) + (var9 * 286704)) + var33) + 269376)) if var3 else 100)
            i32_store(var11 + 32, (((i32_load((((i32_load(9561692) + (var9 * 286704)) + var33) + 269376)) if var3 else 100) * i32_load(var7 + 68)) // 100))
            i32_store(var11 + 36, ((i32_load(var7 + 72) * var3) // 100))
            i32_store(var11 + 40, ((i32_load(var7 + 76) * var3) // 100))
            i32_store(var11 + 44, ((i32_load(var7 + 80) * var3) // 100))
            var10 = (1 if var16 == 0 else 0)
            var3 = func66(var8, (var11 + 32), (1 if var16 == 0 else 0), 1)
            if (var10 if var3 else 0):
                break
            if (1 if func180(var8, var5) >= i32_load(var7 + 204) else 0):
                break
            var3 = (var3 ^ 1)
            var9 = (var9 if (1 if var5 != i32_load(38620) else 0) else 0)
            var8 = (1 if var5 == i32_load(38560) else 0)
            if i32_load(var29):
                break
            if i32_load(var19):
                break
            i32_store(var19, i32_load(9671136))
            var9 = (0 if var8 else var9)
            if var6:
            else:
            var8 = func34((0 if var8 else var9), var17, var4, 0, 1, (1 if i32_load(i32_load(9142424) + 156) != 0 else 0))
            if var2:
                break
            if (1 if i32_load8_u(9142412) == 0 else 0):
                break
            var3 = (i32_load(9671128) + (var8 * 132))
            var4 = i32_load8_u((i32_load(9671128) + (var8 * 132)) + 122)
            var6 = ((i32_load8_u((i32_load(9671128) + (var8 * 132)) + 122) * 404) + 9568096)
            if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var8 * 132)) + 122) * 404) + 9568096) + 264) == 2 else 0):
                if (1 if i32_load(var6 + 268) == 1 else 0):
                    break
            if (1 if i32_load(38964) != var4 else 0):
                break
            i32_store(var3 + 80, 100)
            break
            i32_store(var3 + 52, 1)
            break
            if var8:
                if (var3 | (1 if var16 == 0 else 0)):
                    break
                var3 = (var8 * 132)
                if (1 if i32_load8_u(((var8 * 132) + i32_load(9671128)) + 125) != 4 else 0):
                    break
                func181((i32_load(9561692) + (var9 * 286704)), var8, -1)
                var3 = (i32_load(9671128) + var3)
                i32_store8((i32_load(9671128) + var3) + 127, 14)
                i32_store8(var3 + 125, 14)
                var3 = i32_load(var3 + 40)
                if (1 if i32_load(var3 + 40) == 0 else 0):
                    break
                if i32_load8_u(9142916):
                    i32_store(var11 + 20, var3)
                    i32_store(var11 + 16, -65536)
                    a_b()
                    break
                i32_store(var11 + 4, var3)
                i32_store(var11, 14)
                a_b()
                if (1 if var5 == i32_load(38636) else 0):
                    break
                if (1 if var22 == 2 else 0):
                    break
                var13 = (1 if var13 else 4)
                var36 = (1 if var5 == var12 else 0)
                if (1 if var5 == var12 else 0):
                    break
                var3 = i32_load(9142424)
                if (1 if i32_load(i32_load(9142424) + 124) == 0 else 0):
                    break
                if i32_load(var3 + 156):
                    break
                if (1 if var2 == 0 else 0):
                    break
                var4 = 0
                var3 = i32_load(9671128)
                while True:  # loop $label18
                    var6 = (var3 + (i32_load((var1 + (var4 << 2))) * 132))
                    if (1 if i32_load8_u((var3 + (i32_load((var1 + (var4 << 2))) * 132)) + 125) == 3 else 0):
                        break
                    if (1 if i32_load((i32_load(9215884) + (i32_load(var6 + 44) << 4)) + 4) == 4 else 0):
                        break
                    if (1 if i32_load8_u(var6 + 123) == 4 else 0):
                        break
                    var3 = i32_load(9671128)
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != var2 else 0):
                        continue
                    break  # end loop
                break
                if (1 if var2 == 0 else 0):
                    break
                var6 = 0
                var37 = i32_load(9215884)
                var14 = i32_load(9671128)
                var3 = -1
                var12 = 0
                while True:  # loop $label21
                    var10 = (var14 + (i32_load((var1 + (var6 << 2))) * 132))
                    var4 = (var18 - i32_load16_u((var14 + (i32_load((var1 + (var6 << 2))) * 132)) + 114))
                    var4 = (var26 - i32_load16_u(var10 + 112))
                    var4 = (((var18 - i32_load16_u((var14 + (i32_load((var1 + (var6 << 2))) * 132)) + 114)) * var4) + ((var26 - i32_load16_u(var10 + 112)) * var4))
                    if (1 if (((var18 - i32_load16_u((var14 + (i32_load((var1 + (var6 << 2))) * 132)) + 114)) * var4) + ((var26 - i32_load16_u(var10 + 112)) * var4)) >= var3 else 0):
                        break
                    if (1 if var36 == 0 else 0):
                        if (1 if i32_load((var37 + (i32_load(var10 + 44) << 4)) + 4) == 4 else 0):
                            break
                        if (1 if i32_load8_u(var10 + 123) != 4 else 0):
                            break
                        break
                    if (1 if i32_load8_u(var10 + 123) != 1 else 0):
                        break
                    var38 = (var14 + (i32_load(var10 + 32) * 132))
                    if (1 if i32_load8_u((var14 + (i32_load(var10 + 32) * 132)) + 125) == 10 else 0):
                        break
                    if (1 if i32_load(((i32_load8_u(var38 + 122) * 404) + 9568096) + 188) == 2 else 0):
                        break
                    var12 = i32_load(var10 + 28)
                    var3 = var4
                    var6 = (var6 + 1)
                    if (1 if var2 != (var6 + 1) else 0):
                        continue
                    break  # end loop
                break
            if (1 if var3 == 0 else 0):
                break
            var3 = (i32_load(9561692) + (var9 * 286704))
            var4 = i32_load((i32_load(9561692) + (var9 * 286704)) + 283848)
            if (1 if i32_load((i32_load(9561692) + (var9 * 286704)) + 283848) != 2147483647 else 0):
                i32_store((var3 + 283848), (i32_load(var7 + 68) + var4))
            var4 = (var3 + 283852)
            var6 = i32_load((var3 + 283852))
            if (1 if i32_load((var3 + 283852)) != 2147483647 else 0):
                i32_store(var4, (i32_load(var7 + 72) + var6))
            var4 = (var3 + 283856)
            var6 = i32_load((var3 + 283856))
            if (1 if i32_load((var3 + 283856)) != 2147483647 else 0):
                i32_store(var4, (i32_load(var7 + 76) + var6))
            var4 = (var3 + 283860)
            var6 = i32_load((var3 + 283860))
            if (1 if i32_load((var3 + 283860)) != 2147483647 else 0):
                i32_store(var4, (i32_load(var7 + 80) + var6))
            var4 = (var3 + 281692)
            i32_store((var3 + 281692), (i32_load(var4) - i32_load(var7 + 68)))
            var4 = (var3 + 281696)
            i32_store((var3 + 281696), (i32_load(var4) - i32_load(var7 + 72)))
            var4 = (var3 + 281700)
            i32_store((var3 + 281700), (i32_load(var4) - i32_load(var7 + 76)))
            var4 = i32_load(var7 + 80)
            i32_store8(var3 + 286701, 1)
            var6 = (var3 + 281704)
            i32_store((var3 + 281704), (i32_load(var6) - var4))
            var6 = i32_load(9142892)
            if (1 if i32_load(9142892) < 2 else 0):
                break
            var4 = 1
            var13 = (var6 - 1)
            var14 = ((var6 - 1) & 1)
            var8 = (i32_load(var3 + 283908) * var6)
            var10 = i32_load(9561692)
            var12 = i32_load(9143016)
            if (1 if var6 != 2 else 0):
                var6 = (var13 & -2)
                var3 = 0
                while True:  # loop $label23
                    if i32_load8_u((var12 + (var4 + var8))):
                        i32_store8((var10 + (var4 * 286704)) + 286701, 1)
                    var13 = (var4 + 1)
                    if i32_load8_u((var12 + ((var4 + 1) + var8))):
                        i32_store8((var10 + (var13 * 286704)) + 286701, 1)
                    var4 = (var4 + 2)
                    var3 = (var3 + 2)
                    if (1 if (var3 + 2) != var6 else 0):
                        continue
                    break  # end loop
            if (1 if var14 == 0 else 0):
                break
            if (1 if i32_load8_u((var12 + (var4 + var8))) == 0 else 0):
                break
            i32_store8((var10 + (var4 * 286704)) + 286701, 1)
            break
            var0 = 57101
            if (1 if i32_load((var8 + (var9 * 286704)) + 283908) == i32_load(9142872) else 0):
                break
            break
            var0 = 57113
            if (1 if i32_load((var8 + (var9 * 286704)) + 283908) != i32_load(9142872) else 0):
                break
            a_b()
            break
            var1 = (i32_load(9671128) + (var8 * 132))
            var0 = (global0 - 32)
            global global0
            global0 = (global0 - 32)
            if (1 if i32_load8_u(var1 + 125) == 3 else 0):
                break
            var3 = i32_load(9561692)
            var4 = i32_load16_u(var1 + 110)
            var5 = (i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704))
            if i32_load((((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + (i32_load(38452) << 2)) + 281808)):
                break
            var2 = (var3 + (var4 * 286704))
            var7 = (i32_load((var3 + (var4 * 286704)) + 283976) + 1)
            if (1 if (i32_load((var3 + (var4 * 286704)) + 283976) + 1) > (i32_load((var2 + 284136)) + i32_load(var2 + 283980)) else 0):
                var1 = 57101
                if (1 if i32_load(var2 + 283908) == i32_load(9142872) else 0):
                    break
                break
            if (1 if i32_load((var2 + 284000)) >= var7 else 0):
                var1 = i32_load(var1 + 28)
                var7 = i32_load(var5 + 283868)
                if i32_load(var5 + 283868):
                    var2 = 0
                    var5 = (var1 * 132)
                    while True:  # loop $label27
                        var9 = (i32_load(9671128) + var5)
                        var6 = i32_load(38452)
                        if (1 if func59((var0 + 28), (var0 + 24), (i32_load(9671128) + var5), ((i32_load(38452) * 404) + 9568096)) == 0 else 0):
                            break
                        var9 = func34(var6, i32_load16_u(var9 + 110), i32_load(var0 + 28), i32_load(var0 + 24), 0, 1)
                        if (1 if func34(var6, i32_load16_u(var9 + 110), i32_load(var0 + 28), i32_load(var0 + 24), 0, 1) == 0 else 0):
                            break
                        func69((i32_load(9671128) + var5), var9)
                        var2 = (var2 + 1)
                        if (1 if (var2 + 1) != var7 else 0):
                            continue
                        break  # end loop
                var2 = (i32_load(9671128) + (var1 * 132))
                var1 = i32_load16_u((i32_load(9671128) + (var1 * 132)) + 112)
                var5 = ((i32_load16_u((i32_load(9671128) + (var1 * 132)) + 112) << 5) - i32_load(9142952))
                var2 = i32_load16_u(var2 + 114)
                var5 = ((i32_load16_u(var2 + 114) << 5) - i32_load(9142956))
                if (1 if (((((i32_load16_u((i32_load(9671128) + (var1 * 132)) + 112) << 5) - i32_load(9142952)) * var5) + (((i32_load16_u(var2 + 114) << 5) - i32_load(9142956)) * var5)) - 1) > 9000000 else 0):
                    break
                var7 = i32_load(39876)
                var9 = i32_load(i32_load(9142424) + 48)
                if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
                    break
                if i32_load8_u(9147152):
                    break
                var5 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var2) + var1) << 1)))
                if (1 if var9 != 2 else 0):
                    break
                if (1 if var5 > 1 else 0):
                    break
                break
            var1 = 57113
            if (1 if i32_load((var3 + (var4 * 286704)) + 283908) != i32_load(9142872) else 0):
                break
            a_b()
            break
            if (1 if var5 == 0 else 0):
                break
            i32_store(var0 + 8, var2)
            i32_store(var0 + 4, var1)
            i32_store(var0, var7)
            a_b()
            var1 = (var3 + (var4 * 286704))
            i32_store((((var3 + (var4 * 286704)) + (i32_load(39144) << 2)) + 281808), 55)
            i32_store(var1 + 283864, (i32_load(var1 + 283864) + 1))
            var2 = i32_load(9213808)
            if (1 if i32_load(9213808) == 0 else 0):
                break
            var3 = i32_load(38464)
            var1 = 0
            var4 = i32_load(9671128)
            while True:  # loop $label31
                if (1 if i32_load8_u((var4 + (i32_load(((var1 << 2) + 9173808)) * 132)) + 122) != var3 else 0):
                    var1 = (var1 + 1)
                    if (1 if var2 != (var1 + 1) else 0):
                        continue
                    break
                break  # end loop
            global global0
            global0 = (var0 + 32)
            break
            if (1 if var12 == 0 else 0):
                break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var20 else 0):
                continue
            break  # end loop
        var15 = (var15 + 1)
        if (1 if (var15 + 1) != var21 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var11 + 48)
    return var0

