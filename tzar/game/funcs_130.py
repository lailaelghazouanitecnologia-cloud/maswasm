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
# $hb
# Export: hb
# ==========================================================
def hb(var0):
    """Export: hb"""
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
    var25 = 0
    if (1 if i32_load8_u(9142905) == 0 else 0):
        break
    if (1 if i32_load8_u(9147127) == 0 else 0):
        func361()
    var9 = i32_load(9681680)
    if i32_load(9681680):
        i32_store(9681680, 0)
    var9 = i32_load(9142892)
    var0 = (i32_load(9142892) * var0)
    var13 = func26((-1 if (1 if var0 > 1073741823 else 0) else ((i32_load(9142892) * var0) << 2)))
    i32_store(9681680, func26((-1 if (1 if var0 > 1073741823 else 0) else ((i32_load(9142892) * var0) << 2))))
    if (1 if var9 < 2 else 0):
        break
    var17 = i32_load(38528)
    var20 = i32_load(9561720)
    var15 = i32_load(9143004)
    var16 = i32_load(9561692)
    var21 = i32_load8_u(9147127)
    var18 = 1
    while True:  # loop $label33
        var10 = 1
        while True:  # loop $label2
            if (1 if i32_load((var16 + (var10 * 286704)) + 283944) == var18 else 0):
                break
            var10 = (var10 + 1)
            if (1 if (var10 + 1) != var9 else 0):
                continue
            break  # end loop
        var10 = var9
        var3 = (var16 + (var10 * 286704))
        var19 = ((var16 + (var10 * 286704)) + 278556)
        if var21:
            var0 = (var13 + (var11 << 2))
            i32_store((var13 + (var11 << 2)), i32_load(var3 + 283884))
            i32_store(var0 + 4, i32_load(var3 + 283888))
            var11 = (var11 + 2)
        var4 = (var13 + (var11 << 2))
        i32_store((var13 + (var11 << 2)), i32_load(var3 + 283892))
        i32_store(var4 + 4, i32_load(var3 + 284608))
        var8 = (var11 + 2)
        var22 = (var3 + 284608)
        var12 = (var3 + 281784)
        var0 = i32_load((var3 + 281784))
        var5 = (i32_load((var3 + 281784)) * 255)
        var14 = (var0 * var9)
        var1 = 0
        var2 = 0
        while True:  # loop $label5
            if (1 if i32_load8_u((var15 + (var1 + var14))) == 0 else 0):
                break
            var7 = ((var16 + (var1 * 286704)) + 278568)
            var0 = 0
            while True:  # loop $label4
                if (1 if i32_load(((var0 * 404) + 9568096) + 264) != 1 else 0):
                    var2 = (i32_load((i32_load(var7) + ((var0 + var5) << 2))) + var2)
                var6 = (var0 | 1)
                if (1 if (var0 | 1) == 255 else 0):
                    break
                if (1 if i32_load(((var6 * 404) + 9568096) + 264) != 1 else 0):
                    var2 = (i32_load((i32_load(var7) + ((var5 + var6) << 2))) + var2)
                var0 = (var0 + 2)
                continue
                break  # end loop
            raise RuntimeError('unreachable')
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var9 else 0):
                continue
            break  # end loop
        i32_store((var13 + (var8 << 2)), var2)
        var8 = (var11 + 3)
        var23 = (var3 + 278568)
        var7 = i32_load((var3 + 278568))
        var1 = 0
        var2 = 0
        while True:  # loop $label9
            var6 = (var1 * 255)
            var0 = 0
            while True:  # loop $label8
                if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 1 else 0):
                    break
                if (1 if var0 == var17 else 0):
                    break
                var2 = (i32_load((var7 + ((var0 + var6) << 2))) + var2)
                var5 = (var0 | 1)
                if (1 if (var0 | 1) != 255 else 0):
                    if (1 if i32_load(((var5 * 404) + 9568096) + 264) == 1 else 0):
                        break
                    if (1 if var5 == var17 else 0):
                        break
                    var2 = (i32_load((var7 + ((var5 + var6) << 2))) + var2)
                    var0 = (var0 + 2)
                    continue
                break  # end loop
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var9 else 0):
                continue
            break  # end loop
        i32_store((var13 + (var8 << 2)), var2)
        var6 = i32_load(var12)
        var7 = (i32_load(var12) * var9)
        var8 = i32_load(var19)
        var1 = 0
        var2 = 0
        while True:  # loop $label11
            if i32_load8_u((var15 + (var1 + var7))):
                var14 = (var1 * 255)
                var0 = 0
                while True:  # loop $label10
                    var5 = (var8 + ((var0 + var14) << 2))
                    var2 = (i32_load((var8 + ((var0 + var14) << 2)) + 16) + (i32_load(var5 + 12) + (i32_load(var5 + 8) + (i32_load(var5 + 4) + (i32_load(var5) + var2)))))
                    var0 = (var0 + 5)
                    if (1 if (var0 + 5) != 255 else 0):
                        continue
                    break  # end loop
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var9 else 0):
                continue
            break  # end loop
        var6 = (var6 * 255)
        var1 = 0
        var5 = 0
        while True:  # loop $label14
            if (1 if i32_load8_u((var15 + (var1 + var7))) == 0 else 0):
                break
            var8 = ((var16 + (var1 * 286704)) + 278564)
            var0 = 0
            while True:  # loop $label13
                if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 1 else 0):
                    var5 = (i32_load((i32_load(var8) + ((var0 + var6) << 2))) + var5)
                var14 = (var0 | 1)
                if (1 if (var0 | 1) == 255 else 0):
                    break
                if (1 if i32_load(((var14 * 404) + 9568096) + 264) == 1 else 0):
                    var5 = (i32_load((i32_load(var8) + ((var6 + var14) << 2))) + var5)
                var0 = (var0 + 2)
                continue
                break  # end loop
            raise RuntimeError('unreachable')
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var9 else 0):
                continue
            break  # end loop
        i32_store(var4 + 24, var5)
        i32_store(var4 + 20, (var2 - var5))
        i32_store(var4 + 16, var2)
        var24 = (var11 + 7)
        var6 = (i32_load(var12) * var9)
        var25 = (var3 + 278564)
        var7 = i32_load((var3 + 278564))
        var1 = 0
        var2 = 0
        while True:  # loop $label16
            if i32_load8_u((var15 + (var1 + var6))):
                var8 = (var1 * 255)
                var0 = 0
                while True:  # loop $label15
                    var5 = (var7 + ((var0 + var8) << 2))
                    var2 = (i32_load((var7 + ((var0 + var8) << 2)) + 16) + (i32_load(var5 + 12) + (i32_load(var5 + 8) + (i32_load(var5 + 4) + (i32_load(var5) + var2)))))
                    var0 = (var0 + 5)
                    if (1 if (var0 + 5) != 255 else 0):
                        continue
                    break  # end loop
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var9 else 0):
                continue
            break  # end loop
        var1 = 0
        var5 = 0
        while True:  # loop $label19
            if (1 if i32_load8_u((var15 + (var1 + var6))) == 0 else 0):
                break
            var8 = (var1 * 255)
            var0 = 0
            while True:  # loop $label18
                if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 1 else 0):
                    var5 = (i32_load((var7 + ((var0 + var8) << 2))) + var5)
                var14 = (var0 | 1)
                if (1 if (var0 | 1) == 255 else 0):
                    break
                if (1 if i32_load(((var14 * 404) + 9568096) + 264) == 1 else 0):
                    var5 = (i32_load((var7 + ((var8 + var14) << 2))) + var5)
                var0 = (var0 + 2)
                continue
                break  # end loop
            raise RuntimeError('unreachable')
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var9 else 0):
                continue
            break  # end loop
        i32_store((var13 + (var24 << 2)), var2)
        i32_store(var4 + 36, var5)
        i32_store(var4 + 32, (var2 - var5))
        i32_store(var4 + 40, i32_load(var3 + 283956))
        var0 = (var3 + 281676)
        var1 = (var3 + 281640)
        i32_store(var4 + 44, (i32_load((var3 + 281676)) + i32_load((var3 + 281640))))
        i32_store(var4 + 48, i32_load(var1))
        i32_store(var4 + 52, i32_load(var0))
        var0 = (var3 + 281680)
        var1 = (var3 + 281644)
        i32_store(var4 + 56, (i32_load((var3 + 281680)) + i32_load((var3 + 281644))))
        i32_store(var4 + 60, i32_load(var1))
        i32_store((var4 - -64), i32_load(var0))
        var0 = (var3 + 281684)
        var1 = (var3 + 281656)
        var2 = (var3 + 281648)
        var5 = (var3 + 281660)
        var7 = (var3 + 281652)
        i32_store(var4 + 68, (i32_load((var3 + 281684)) + (i32_load((var3 + 281656)) + (i32_load((var3 + 281648)) + (i32_load((var3 + 281660)) + i32_load((var3 + 281652)))))))
        i32_store(var4 + 72, i32_load(var7))
        i32_store(var4 + 76, i32_load(var5))
        i32_store(var4 + 80, i32_load(var2))
        i32_store(var4 + 84, i32_load(var1))
        i32_store(var4 + 88, i32_load(var0))
        var0 = (var3 + 281688)
        var1 = (var3 + 281664)
        i32_store(var4 + 92, (i32_load((var3 + 281688)) + i32_load((var3 + 281664))))
        i32_store(var4 + 96, i32_load(var1))
        i32_store(var4 + 100, i32_load(var0))
        i32_store(var4 + 104, i32_load((var3 + 281636)))
        i32_store(var4 + 108, i32_load((var3 + 281744)))
        i32_store(var4 + 112, i32_load((var3 + 281672)))
        i32_store(var4 + 116, i32_load((var3 + 281668)))
        i32_store(var4 + 120, i32_load((var3 + 281748)))
        var0 = 0
        var2 = 0
        while True:  # loop $label22
            if (i32_load(((var0 * 404) + 9568096) + 264) & -5):
                break
            if (1 if var0 == var17 else 0):
                break
            var2 = (i32_load(((var3 + (var0 << 2)) + 278576)) + var2)
            var1 = (var0 | 1)
            if (1 if (var0 | 1) != 255 else 0):
                if (i32_load(((var1 * 404) + 9568096) + 264) & -5):
                    break
                if (1 if var1 == var17 else 0):
                    break
                var2 = (i32_load(((var3 + (var1 << 2)) + 278576)) + var2)
                var0 = (var0 + 2)
                continue
            break  # end loop
        i32_store(var4 + 124, var2)
        var6 = (var11 + 32)
        var0 = i32_load(var12)
        var5 = (i32_load(var12) * 255)
        var8 = (var0 * var9)
        var1 = 0
        var2 = 0
        while True:  # loop $label25
            if (1 if i32_load8_u((var15 + (var1 + var8))) == 0 else 0):
                break
            var12 = ((var16 + (var1 * 286704)) + 278568)
            var0 = 0
            while True:  # loop $label24
                if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 1 else 0):
                    var2 = (i32_load((i32_load(var12) + ((var0 + var5) << 2))) + var2)
                var7 = (var0 | 1)
                if (1 if (var0 | 1) == 255 else 0):
                    break
                if (1 if i32_load(((var7 * 404) + 9568096) + 264) == 1 else 0):
                    var2 = (i32_load((i32_load(var12) + ((var5 + var7) << 2))) + var2)
                var0 = (var0 + 2)
                continue
                break  # end loop
            raise RuntimeError('unreachable')
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var9 else 0):
                continue
            break  # end loop
        i32_store((var13 + (var6 << 2)), var2)
        var5 = i32_load(var23)
        var1 = 0
        var2 = 0
        while True:  # loop $label27
            var12 = (var1 * 255)
            var0 = 0
            while True:  # loop $label26
                if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 1 else 0):
                    var2 = (i32_load((var5 + ((var0 + var12) << 2))) + var2)
                var7 = (var0 | 1)
                if (1 if (var0 | 1) != 255 else 0):
                    if (1 if i32_load(((var7 * 404) + 9568096) + 264) == 1 else 0):
                        var2 = (i32_load((var5 + ((var7 + var12) << 2))) + var2)
                    var0 = (var0 + 2)
                    continue
                break  # end loop
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var9 else 0):
                continue
            break  # end loop
        i32_store(var4 + 132, var2)
        i32_store(var4 + 136, i32_load((var3 + 281740)))
        i32_store(var4 + 140, i32_load((var3 + 281724)))
        i32_store(var4 + 144, i32_load((var3 + 281728)))
        i32_store(var4 + 148, i32_load((var3 + 281732)))
        i32_store(var4 + 152, i32_load((var3 + 281736)))
        i32_store(var4 + 156, i32_load((var3 + 281692)))
        i32_store(var4 + 160, i32_load((var3 + 281696)))
        i32_store(var4 + 164, i32_load((var3 + 281700)))
        i32_store(var4 + 168, i32_load((var3 + 281704)))
        i32_store(var4 + 172, i32_load((var3 + 281708)))
        i32_store(var4 + 176, i32_load((var3 + 281712)))
        i32_store(var4 + 180, i32_load((var3 + 281716)))
        i32_store(var4 + 184, i32_load((var3 + 281720)))
        var0 = i32_load(var22)
        if i32_load(var22):
            if (1 if var0 == var20 else 0):
                break
        i32_store((var13 + ((var11 + 47) << 2)), (1 if i32_load8_u(var3 + 286697) != 0 else 0))
        var0 = i32_load((var3 + 278572))
        i32_store(var4 + 192, i32_load(i32_load((var3 + 278572)) + 8))
        i32_store(var4 + 196, i32_load(var3 + 283944))
        i32_store(var4 + 200, i32_load(var0))
        var1 = 0
        var2 = func26(1020)
        # Unknown: memory.fill []
        var12 = (var9 * var10)
        var7 = (var11 + 51)
        while True:  # loop $label30
            if i32_load8_u((var15 + (var1 + var12))):
                var10 = (var1 * 255)
                var5 = i32_load(var25)
                var0 = 0
                while True:  # loop $label29
                    var6 = (var2 + (var0 << 2))
                    i32_store((var2 + (var0 << 2)), (i32_load(var6) + i32_load((var5 + ((var0 + var10) << 2)))))
                    var6 = (var0 + 1)
                    var8 = (var2 + ((var0 + 1) << 2))
                    i32_store((var2 + ((var0 + 1) << 2)), (i32_load(var8) + i32_load((var5 + ((var6 + var10) << 2)))))
                    var6 = (var0 + 2)
                    var8 = (var2 + ((var0 + 2) << 2))
                    i32_store((var2 + ((var0 + 2) << 2)), (i32_load(var8) + i32_load((var5 + ((var6 + var10) << 2)))))
                    var0 = (var0 + 3)
                    if (1 if (var0 + 3) != 255 else 0):
                        continue
                    break  # end loop
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var9 else 0):
                continue
            break  # end loop
        i32_store((var13 + (var7 << 2)), var2)
        i32_store(var4 + 216, (var3 + 280616))
        i32_store(var4 + 212, (var3 + 279596))
        i32_store(var4 + 208, (var3 + 278576))
        var1 = 0
        var10 = func26(1020)
        # Unknown: memory.fill []
        var7 = (var11 + 55)
        while True:  # loop $label32
            if i32_load8_u((var15 + (var1 + var12))):
                var2 = (var1 * 255)
                var5 = i32_load(var19)
                var0 = 0
                while True:  # loop $label31
                    var6 = (var10 + (var0 << 2))
                    i32_store((var10 + (var0 << 2)), (i32_load(var6) + i32_load((var5 + ((var0 + var2) << 2)))))
                    var6 = (var0 + 1)
                    var8 = (var10 + ((var0 + 1) << 2))
                    i32_store((var10 + ((var0 + 1) << 2)), (i32_load(var8) + i32_load((var5 + ((var2 + var6) << 2)))))
                    var6 = (var0 + 2)
                    var8 = (var10 + ((var0 + 2) << 2))
                    i32_store((var10 + ((var0 + 2) << 2)), (i32_load(var8) + i32_load((var5 + ((var2 + var6) << 2)))))
                    var0 = (var0 + 3)
                    if (1 if (var0 + 3) != 255 else 0):
                        continue
                    break  # end loop
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var9 else 0):
                continue
            break  # end loop
        i32_store((var13 + (var7 << 2)), var10)
        i32_store(var4 + 224, i32_load(var3 + 283908))
        i32_store(var4 + 228, i32_load(var3 + 283960))
        var0 = i32_load(var3 + 284616)
        if i32_load(var3 + 284616):
        else:
        i32_store(var0, i32_load(var3 + 284628))
        i32_store(var4 + 236, var3)
        i32_store(var4 + 240, ((i32_load8_u((var3 + 283974)) | (i32_load8_u((var3 + 283973)) << 8)) | (i32_load8_u(var3 + 283972) << 16)))
        var11 = (var11 + 61)
        var18 = (var18 + 1)
        if (1 if (var18 + 1) != var9 else 0):
            continue
        break  # end loop
    return var13

