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
# $func94
# ==========================================================
def func94(var0, var1, var2):
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
    var12 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    if (1 if i32_load(var0 + 283908) == 0 else 0):
        break
    if (1 if var1 == 0 else 0):
        break
    if var2:
        break
    var3 = i32_load(var0 + 284628)
    var2 = i32_load(var0 + 284616)
    i32_store(var12 + 68, var0)
    i32_store(var12 + 64, 94)
    i32_store(var12 + 72, (var2 if var2 else var3))
    a_b()
    var2 = 1
    i32_store8(var0 + 286699, 1)
    if i32_load8_u(9147125):
        i32_store(var12 + 48, i32_load(var0 + 283908))
        a_b()
        var2 = i32_load8_u(var0 + 286699)
    var3 = i32_load(var0 + 283908)
    var4 = i32_load8_u(var0 + 286696)
    i32_store(var12 + 40, var2)
    i32_store(var12 + 36, var4)
    i32_store(var12 + 32, var3)
    a_b()
    if i32_load8_u(9147125):
        break
    var2 = i32_load(var0 + 283908)
    var3 = i32_load8_u(var0 + 286696)
    if i32_load8_u(var0 + 286696):
        break
    if i32_load8_u(9147152):
        break
    if i32_load8_u(9142905):
        break
    if (1 if var2 != i32_load(9142872) else 0):
        break
    a_b()
    if (1 if i32_load(i32_load(9142424) + 160) == 0 else 0):
        if i32_load8_u(9147210):
            break
    func227()
    var3 = i32_load(var0 + 284628)
    var2 = i32_load(var0 + 284616)
    i32_store(var12 + 20, var0)
    i32_store(var12 + 16, 118)
    i32_store(var12 + 24, (var2 if var2 else var3))
    a_b()
    if (1 if i32_load(var0 + 283956) == 0 else 0):
        i32_store(var0 + 283956, (((i32_load(9142848) * 25) & 0xFFFFFFFF) // 1000))
    if (1 if var1 == 0 else 0):
        i32_store8(var0 + 286696, 1)
    if i32_load8_u(9147127):
        var1 = 0
        var3 = (global0 - 16)
        global global0
        global0 = (global0 - 16)
        var4 = i32_load(9142892)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var6 = i32_load(9143004)
        var5 = i32_load(var0 + 283908)
        var14 = i32_load(9561692)
        var2 = 1
        while True:  # loop $label6
            var16 = (var14 + (var2 * 286704))
            var9 = i32_load((var14 + (var2 * 286704)) + 283908)
            if i32_load8_u((var6 + ((i32_load((var14 + (var2 * 286704)) + 283908) * var4) + var5))):
                break
            if i32_load8_u(var16 + 286696):
                break
            var1 = (var1 + (1 if var5 != var9 else 0))
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var4 else 0):
                continue
            break  # end loop
        if (1 if var1 == 0 else 0):
            break
        i32_store(var3, (i32_load(var0 + 283848) // var1))
        i32_store(var3 + 4, (i32_load((var0 + 283852)) // var1))
        i32_store(var3 + 8, (i32_load((var0 + 283856)) // var1))
        i32_store(var3 + 12, (i32_load((var0 + 283860)) // var1))
        if (1 if var4 < 2 else 0):
            break
        var1 = i32_load(9143004)
        var5 = i32_load(9561692)
        var2 = 1
        while True:  # loop $label8
            var6 = i32_load(var0 + 283908)
            var16 = (var5 + (var2 * 286704))
            var14 = i32_load((var5 + (var2 * 286704)) + 283908)
            if i32_load8_u((var1 + (i32_load(var0 + 283908) + (i32_load((var5 + (var2 * 286704)) + 283908) * var4)))):
                break
            if i32_load8_u(var16 + 286696):
                break
            if (1 if var6 == var14 else 0):
                break
            func322(var14, var6, var3)
            var4 = i32_load(9142892)
            var1 = i32_load(9143004)
            var5 = i32_load(9561692)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < var4 else 0):
                continue
            break  # end loop
        global global0
        global0 = (var3 + 16)
    var16 = 0
    var14 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var6 = i32_load(9561692)
    var4 = 1
    while True:  # loop $label14
        if (1 if var2 < 2 else 0):
            var2 = 1
            break
        var3 = (var6 + (var4 * 286704))
        var9 = (var2 * var4)
        var5 = 0
        var7 = i32_load(9143004)
        var1 = 1
        while True:  # loop $label12
            if (1 if var1 == var4 else 0):
                break
            var10 = i32_load8_u((var7 + (var1 + var9)))
            var15 = (var6 + (var1 * 286704))
            var18 = i32_load8_u((var6 + (var1 * 286704)) + 286699)
            var5 = (((1 if i32_load8_u((var7 + (var1 + var9))) != 0 else 0) | var5) if i32_load8_u((var6 + (var1 * 286704)) + 286699) else var5)
            if (1 if var10 == 0 else 0):
                break
            if var18:
                break
            if (1 if i32_load8_u(var15 + 286696) == 0 else 0):
                break
            var5 = 1
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var2 else 0):
                continue
            break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var2 else 0):
                continue
            break  # end loop
        if (1 if (var5 & 1) == 0 else 0):
            break
        i32_store(9561720, i32_load(var3 + 284608))
        var16 = 1
        if i32_load8_u(var3 + 286696):
            break
        if i32_load8_u(var3 + 286697):
            break
        i32_store8((var3 + 286697), 1)
        if (1 if i32_load(var3 + 283908) == i32_load(9142872) else 0):
            a_b()
        var2 = i32_load(var3 + 284628)
        var1 = i32_load(var3 + 284616)
        i32_store(var14 + 20, var3)
        i32_store(var14 + 16, 119)
        i32_store(var14 + 24, (var1 if var1 else var2))
        a_b()
        func227()
        var2 = i32_load(9142892)
        var6 = i32_load(9561692)
        var4 = (var4 + 1)
        if (1 if (var4 + 1) < var2 else 0):
            continue
        break  # end loop
    if (1 if (var16 & (1 if i32_load8_u(9142905) == 0 else 0)) == 0 else 0):
        break
    i32_store8(9142905, 1)
    var1 = (i32_load(9142848) * 25)
    i32_store(9561724, (1 if (1 if var1 < 1000 else 0) else (((i32_load(9142848) * 25) & 0xFFFFFFFF) // 1000)))
    if (1 if var2 >= 2 else 0):
        var3 = i32_load(9561692)
        var1 = 1
        while True:  # loop $label15
            var4 = (var3 + (var1 * 286704))
            if (1 if i32_load((var3 + (var1 * 286704)) + 283956) == 0 else 0):
                i32_store((var4 + 283956), i32_load(9561724))
                var2 = i32_load(9142892)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < var2 else 0):
                continue
            break  # end loop
    if i32_load8_u(9147127):
        func361()
        var2 = i32_load(9142892)
        var18 = ((i32_load(9142892) * 54) - 54)
        var19 = func26((-1 if (1 if var18 > 1073741823 else 0) else (((i32_load(9142892) * 54) - 54) << 2)))
        if (1 if var2 >= 2 else 0):
            var3 = i32_load(9561692)
            var1 = 1
            while True:  # loop $label17
                if (1 if i32_load((var3 + (var1 * 286704)) + 283944) == 1 else 0):
                    var20 = i32_load((var3 + (var1 * 286704)) + 283884)
                    break
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var2 else 0):
                    continue
                break  # end loop
            if (1 if var2 > 1 else 0):
                break
        var7 = i32_load(9561720)
        break
        var16 = 1
        while True:  # loop $label59
            var5 = 0
            var1 = i32_load(9561692)
            var4 = (i32_load(9561692) + (var16 * 286704))
            if var20:
            else:
            i32_store((((i32_load((var1 + (var16 * 286704)) + 283884) * 155) & 0xFFFFFFFF) // var20) + 283884, 0)
            var3 = ((var16 * 216) + var19)
            i32_store((((var16 * 216) + var19) - 216), i32_load(var4 + 283944))
            i32_store((var3 - 212), i32_load(var4 + 283960))
            i32_store((var3 - 208), i32_load(var4 + 284608))
            i32_store((var3 - 204), i32_load(var4 + 283892))
            var17 = (var4 + 283884)
            var6 = i32_load(9142892)
            if i32_load(9142892):
                var10 = (var4 + 281784)
                var1 = i32_load((var4 + 281784))
                var7 = (i32_load((var4 + 281784)) * 255)
                var13 = (var1 * var6)
                var15 = i32_load(9561692)
                var9 = i32_load(9143004)
                var2 = 0
                while True:  # loop $label22
                    if (1 if i32_load8_u((var9 + (var5 + var13))) == 0 else 0):
                        break
                    var8 = ((var15 + (var5 * 286704)) + 278568)
                    var1 = 0
                    while True:  # loop $label21
                        if (1 if i32_load(((var1 * 404) + 9568096) + 264) != 1 else 0):
                            var2 = (i32_load((i32_load(var8) + ((var1 + var7) << 2))) + var2)
                        var11 = (var1 | 1)
                        if (1 if (var1 | 1) == 255 else 0):
                            break
                        if (1 if i32_load(((var11 * 404) + 9568096) + 264) != 1 else 0):
                            var2 = (i32_load((i32_load(var8) + ((var7 + var11) << 2))) + var2)
                        var1 = (var1 + 2)
                        continue
                        break  # end loop
                    raise RuntimeError('unreachable')
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var6 else 0):
                        continue
                    break  # end loop
                i32_store((var3 - 200), var2)
                var8 = i32_load((var4 + 278568))
                var5 = 0
                var11 = i32_load(38528)
                var2 = 0
                while True:  # loop $label26
                    var13 = (var5 * 255)
                    var1 = 0
                    while True:  # loop $label25
                        if (1 if i32_load(((var1 * 404) + 9568096) + 264) == 1 else 0):
                            break
                        if (1 if var1 == var11 else 0):
                            break
                        var2 = (i32_load((var8 + ((var1 + var13) << 2))) + var2)
                        var7 = (var1 | 1)
                        if (1 if (var1 | 1) != 255 else 0):
                            if (1 if i32_load(((var7 * 404) + 9568096) + 264) == 1 else 0):
                                break
                            if (1 if var7 == var11 else 0):
                                break
                            var2 = (i32_load((var8 + ((var7 + var13) << 2))) + var2)
                            var1 = (var1 + 2)
                            continue
                        break  # end loop
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var6 else 0):
                        continue
                    break  # end loop
                i32_store((var3 - 196), var2)
                var1 = i32_load(var10)
                var7 = (i32_load(var10) * 255)
                var13 = (var1 * var6)
                var5 = 0
                var2 = 0
                while True:  # loop $label29
                    if (1 if i32_load8_u((var9 + (var5 + var13))) == 0 else 0):
                        break
                    var8 = ((var15 + (var5 * 286704)) + 278564)
                    var1 = 0
                    while True:  # loop $label28
                        if (1 if i32_load(((var1 * 404) + 9568096) + 264) != 1 else 0):
                            var2 = (i32_load((i32_load(var8) + ((var1 + var7) << 2))) + var2)
                        var11 = (var1 | 1)
                        if (1 if (var1 | 1) == 255 else 0):
                            break
                        if (1 if i32_load(((var11 * 404) + 9568096) + 264) != 1 else 0):
                            var2 = (i32_load((i32_load(var8) + ((var7 + var11) << 2))) + var2)
                        var1 = (var1 + 2)
                        continue
                        break  # end loop
                    raise RuntimeError('unreachable')
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var6 else 0):
                        continue
                    break  # end loop
                i32_store((var3 - 192), var2)
                var8 = (i32_load(var10) * var6)
                var7 = i32_load((var4 + 278564))
                var5 = 0
                var2 = 0
                while True:  # loop $label32
                    if (1 if i32_load8_u((var9 + (var5 + var8))) == 0 else 0):
                        break
                    var10 = (var5 * 255)
                    var1 = 0
                    while True:  # loop $label31
                        if (1 if i32_load(((var1 * 404) + 9568096) + 264) != 1 else 0):
                            var2 = (i32_load((var7 + ((var1 + var10) << 2))) + var2)
                        var15 = (var1 | 1)
                        if (1 if (var1 | 1) == 255 else 0):
                            break
                        if (1 if i32_load(((var15 * 404) + 9568096) + 264) != 1 else 0):
                            var2 = (i32_load((var7 + ((var10 + var15) << 2))) + var2)
                        var1 = (var1 + 2)
                        continue
                        break  # end loop
                    raise RuntimeError('unreachable')
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var6 else 0):
                        continue
                    break  # end loop
                break
            var2 = 0
            i32_store((var3 - 192), 0)
            i64_store((var3 - 200), 0)
            var15 = (var4 + 284608)
            i32_store((var3 - 188), var2)
            var8 = (var4 + 281676)
            i32_store((var3 - 184), (i32_load((var4 + 281676)) + i32_load((var4 + 281640))))
            var11 = (var4 + 281680)
            i32_store((var3 - 180), (i32_load((var4 + 281680)) + i32_load((var4 + 281644))))
            var13 = (var4 + 281684)
            var21 = (var4 + 281656)
            var22 = (var4 + 281660)
            var23 = (var4 + 281652)
            var24 = (var4 + 281648)
            i32_store((var3 - 176), (i32_load((var4 + 281684)) + (i32_load((var4 + 281656)) + (i32_load((var4 + 281660)) + (i32_load((var4 + 281652)) + i32_load((var4 + 281648)))))))
            var25 = (var4 + 281688)
            i32_store((var3 - 172), (i32_load((var4 + 281688)) + i32_load((var4 + 281664))))
            i32_store((var3 - 168), i32_load(var4 + 283872))
            i32_store((var3 - 164), i32_load(var4 + 283876))
            i32_store((var3 - 160), i32_load(var4 + 283948))
            i32_store((var3 - 156), i32_load(var4 + 283956))
            i32_store((var3 - 152), i32_load(var17))
            if (1 if var6 == 0 else 0):
                var2 = 0
                i32_store((var3 - 148), 0)
                break
            var1 = i32_load((var4 + 281784))
            var9 = (i32_load((var4 + 281784)) * 255)
            var17 = (var1 * var6)
            var5 = 0
            var26 = i32_load(9561692)
            var27 = i32_load(9143004)
            var2 = 0
            while True:  # loop $label37
                if (1 if i32_load8_u((var27 + (var5 + var17))) == 0 else 0):
                    break
                var7 = ((var26 + (var5 * 286704)) + 278568)
                var1 = 0
                while True:  # loop $label36
                    if (1 if i32_load(((var1 * 404) + 9568096) + 264) == 1 else 0):
                        var2 = (i32_load((i32_load(var7) + ((var1 + var9) << 2))) + var2)
                    var10 = (var1 | 1)
                    if (1 if (var1 | 1) == 255 else 0):
                        break
                    if (1 if i32_load(((var10 * 404) + 9568096) + 264) == 1 else 0):
                        var2 = (i32_load((i32_load(var7) + ((var9 + var10) << 2))) + var2)
                    var1 = (var1 + 2)
                    continue
                    break  # end loop
                raise RuntimeError('unreachable')
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var6 else 0):
                    continue
                break  # end loop
            i32_store((var3 - 148), var2)
            var9 = i32_load((var4 + 278568))
            var5 = 0
            var2 = 0
            while True:  # loop $label39
                var7 = (var5 * 255)
                var1 = 0
                while True:  # loop $label38
                    if (1 if i32_load(((var1 * 404) + 9568096) + 264) == 1 else 0):
                        var2 = (i32_load((var9 + ((var1 + var7) << 2))) + var2)
                    var10 = (var1 | 1)
                    if (1 if (var1 | 1) != 255 else 0):
                        if (1 if i32_load(((var10 * 404) + 9568096) + 264) == 1 else 0):
                            var2 = (i32_load((var9 + ((var7 + var10) << 2))) + var2)
                        var1 = (var1 + 2)
                        continue
                    break  # end loop
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var6 else 0):
                    continue
                break  # end loop
            i32_store((var3 - 144), var2)
            i32_store((var3 - 140), i32_load((var4 + 281740)))
            i32_store((var3 - 136), i32_load((var4 + 281724)))
            i32_store((var3 - 132), i32_load((var4 + 281728)))
            i32_store((var3 - 128), i32_load((var4 + 281732)))
            i32_store((var3 - 124), i32_load((var4 + 281736)))
            i32_store((var3 - 120), i32_load((var4 + 281744)))
            i32_store((var3 - 116), i32_load((var4 + 281668)))
            i32_store((var3 - 112), i32_load((var4 + 281748)))
            i32_store((var3 - 108), i32_load((var4 + 281636)))
            var7 = i32_load(9561720)
            var1 = i32_load(var15)
            if i32_load(var15):
                if (1 if var1 == var7 else 0):
                    break
            i32_store((var3 - 104), (1 if i32_load8_u(var4 + 286697) != 0 else 0))
            i32_store((var3 - 100), ((i32_load8_u((var4 + 283974)) | (i32_load8_u((var4 + 283973)) << 8)) | (i32_load8_u(var4 + 283972) << 16)))
            i32_store((var3 - 96), i32_load(var8))
            i32_store((var3 - 92), i32_load(var11))
            i32_store((var3 - 88), i32_load(var13))
            i32_store((var3 - 84), i32_load(var25))
            i32_store((var3 - 80), i32_load(var23))
            i32_store((var3 - 76), i32_load(var24))
            i32_store((var3 - 72), i32_load(var21))
            i32_store((var3 - 68), i32_load(var22))
            i32_store((var3 + -64), i32_load((var4 + 281708)))
            i32_store((var3 - 60), i32_load((var4 + 281712)))
            i32_store((var3 - 56), i32_load((var4 + 281716)))
            i32_store((var3 - 52), i32_load((var4 + 281720)))
            i32_store((var3 - 48), i32_load((var4 + 281692)))
            i32_store((var3 - 44), i32_load((var4 + 281696)))
            i32_store((var3 - 40), i32_load((var4 + 281700)))
            i32_store((var3 - 36), i32_load((var4 + 281704)))
            var1 = 0
            var9 = i32_load(38528)
            var2 = 0
            while True:  # loop $label43
                if (i32_load(((var1 * 404) + 9568096) + 264) & -5):
                    break
                if (1 if var1 == var9 else 0):
                    break
                var2 = (i32_load(((var4 + (var1 << 2)) + 278576)) + var2)
                var5 = (var1 | 1)
                if (1 if (var1 | 1) != 255 else 0):
                    if (i32_load(((var5 * 404) + 9568096) + 264) & -5):
                        break
                    if (1 if var5 == var9 else 0):
                        break
                    var2 = (i32_load(((var4 + (var5 << 2)) + 278576)) + var2)
                    var1 = (var1 + 2)
                    continue
                break  # end loop
            i32_store((var3 - 32), var2)
            i32_store((var3 - 28), i32_load(var4 + 283888))
            i32_store((var3 - 24), i32_load((var4 + 281672)))
            if var6:
                var10 = (var4 + 281784)
                var1 = i32_load((var4 + 281784))
                var8 = (i32_load((var4 + 281784)) * 255)
                var17 = (var1 * var6)
                var5 = 0
                var15 = i32_load(9561692)
                var9 = i32_load(9143004)
                var2 = 0
                while True:  # loop $label46
                    if (1 if i32_load8_u((var9 + (var5 + var17))) == 0 else 0):
                        break
                    var11 = ((var15 + (var5 * 286704)) + 278564)
                    var1 = 0
                    while True:  # loop $label45
                        if (1 if i32_load(((var1 * 404) + 9568096) + 264) == 1 else 0):
                            var2 = (i32_load((i32_load(var11) + ((var1 + var8) << 2))) + var2)
                        var13 = (var1 | 1)
                        if (1 if (var1 | 1) == 255 else 0):
                            break
                        if (1 if i32_load(((var13 * 404) + 9568096) + 264) == 1 else 0):
                            var2 = (i32_load((i32_load(var11) + ((var8 + var13) << 2))) + var2)
                        var1 = (var1 + 2)
                        continue
                        break  # end loop
                    raise RuntimeError('unreachable')
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var6 else 0):
                        continue
                    break  # end loop
                i32_store((var3 - 20), var2)
                var13 = (i32_load(var10) * var6)
                var4 = i32_load((var4 + 278564))
                var5 = 0
                var2 = 0
                while True:  # loop $label49
                    if (1 if i32_load8_u((var9 + (var5 + var13))) == 0 else 0):
                        break
                    var8 = (var5 * 255)
                    var1 = 0
                    while True:  # loop $label48
                        if (1 if i32_load(((var1 * 404) + 9568096) + 264) == 1 else 0):
                            var2 = (i32_load((var4 + ((var1 + var8) << 2))) + var2)
                        var11 = (var1 | 1)
                        if (1 if (var1 | 1) == 255 else 0):
                            break
                        if (1 if i32_load(((var11 * 404) + 9568096) + 264) == 1 else 0):
                            var2 = (i32_load((var4 + ((var8 + var11) << 2))) + var2)
                        var1 = (var1 + 2)
                        continue
                        break  # end loop
                    raise RuntimeError('unreachable')
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var6 else 0):
                        continue
                    break  # end loop
                var5 = 0
                i32_store((var3 - 12), 0)
                i32_store((var3 - 16), var2)
                var4 = i32_load(var10)
                var11 = (i32_load(var10) * 255)
                var13 = (var4 * var6)
                var2 = 0
                while True:  # loop $label53
                    if i32_load8_u((var9 + (var5 + var13))):
                        break
                    if (1 if var4 == var5 else 0):
                        break
                    var17 = ((var15 + (var5 * 286704)) + 278564)
                    var1 = 0
                    while True:  # loop $label52
                        var8 = ((var1 * 404) + 9568096)
                        if (1 if i32_load(((var1 * 404) + 9568096) + 264) == 1 else 0):
                            if (1 if i32_load(var8 + 268) != 1 else 0):
                                break
                        var2 = ((((i32_load(var8 + 328) * i32_load((i32_load(var17) + ((var1 + var11) << 2)))) & 0xFFFFFFFF) // 100) + var2)
                        var1 = (var1 + 1)
                        if (1 if (var1 + 1) != 255 else 0):
                            continue
                        break  # end loop
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var6 else 0):
                        continue
                    break  # end loop
                i32_store((var3 - 8), var2)
                var5 = i32_load(var10)
                var8 = (i32_load(var10) * 255)
                var11 = (var5 * var6)
                var4 = 0
                var2 = 0
                while True:  # loop $label57
                    if i32_load8_u((var9 + (var4 + var11))):
                        break
                    if (1 if var4 == var5 else 0):
                        break
                    var13 = ((var15 + (var4 * 286704)) + 278564)
                    var1 = 0
                    while True:  # loop $label56
                        var10 = ((var1 * 404) + 9568096)
                        if (1 if i32_load(((var1 * 404) + 9568096) + 264) != 1 else 0):
                            break
                        if (1 if i32_load(var10 + 268) == 1 else 0):
                            break
                        var2 = ((((i32_load(var10 + 328) * i32_load((i32_load(var13) + ((var1 + var8) << 2)))) & 0xFFFFFFFF) // 100) + var2)
                        var1 = (var1 + 1)
                        if (1 if (var1 + 1) != 255 else 0):
                            continue
                        break  # end loop
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != var6 else 0):
                        continue
                    break  # end loop
                break
            i64_store((var3 - 12), 0)
            i64_store((var3 - 20), 0)
            var2 = 0
            i32_store((var3 - 4), var2)
            var16 = (var16 + 1)
            if (1 if (var16 + 1) < var6 else 0):
                continue
            break  # end loop
        i32_store(var14 + 8, var7)
        i32_store(var14 + 4, var18)
        i32_store(var14, var19)
    global global0
    global0 = (var14 + 32)
    var3 = i32_load8_u(var0 + 286696)
    var2 = i32_load(var0 + 283908)
    i32_store(var12 + 8, i32_load8_u(var0 + 286699))
    i32_store(var12 + 4, var3)
    i32_store(var12, var2)
    a_b()
    global global0
    global0 = (var12 + 80)
    return var12

