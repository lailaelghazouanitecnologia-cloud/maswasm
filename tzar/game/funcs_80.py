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
# $func170
# ==========================================================
def func170(var0):
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
    if i32_load(9142912):
        var3 = i32_load(9142908)
        var9 = i32_load(i32_load(9142908) + 60)
        var6 = i32_load(var3)
        var7 = (var6 + (i32_load(var3 + 4) * 60))
        if (1 if i32_load(var3) < (var6 + (i32_load(var3 + 4) * 60)) else 0):
            var4 = var7
            while True:  # loop $label6
                var8 = i32_load(9142908)
                var1 = (i32_load(9142908) + (var6 << 2))
                var10 = i32_load((i32_load(9142908) + (var6 << 2)))
                var2 = ((i32_load((i32_load(9142908) + (var6 << 2))) * 404) + 9568096)
                var3 = i32_load(var1 + 4)
                i32_store(((i32_load((i32_load(9142908) + (var6 << 2))) * 404) + 9568096) + 108, i32_load(var1 + 4))
                i32_store(var2 + 104, var3)
                i32_store(var2 + 92, i32_load(var1 + 8))
                i32_store(var2 + 100, i32_load(var1 + 12))
                i32_store(var2 + 68, i32_load(var1 + 16))
                i32_store(var2 + 72, i32_load(var1 + 20))
                i32_store(var2 + 76, i32_load(var1 + 24))
                i32_store(var2 + 80, i32_load(var1 + 28))
                var3 = i32_load(var1 + 32)
                i32_store(var2 + 128, i32_load(var1 + 32))
                i32_store(var2 + 120, var3)
                i32_store(var2 + 116, i32_load(var1 + 36))
                i32_store(var2 + 276, i32_load(var1 + 40))
                i32_store(var2 + 96, i32_load(var1 + 44))
                i32_store(var2 + 224, i32_load(var1 + 48))
                i32_store(var2 + 260, i32_load(var1 + 52))
                i32_store(var2 + 204, i32_load(var1 + 56))
                i32_store(var2 + 200, i32_load(var1 + 60))
                var5 = i32_load((var1 - -64))
                i32_store(var2 + 236, i32_load((var1 - -64)))
                i32_store(var2 + 228, i32_load(var1 + 68))
                i32_store(var2 + 208, i32_load(var1 + 72))
                var3 = i32_load(var1 + 76)
                i32_store(var2 + 216, i32_load(var1 + 76))
                var11 = (var6 + 20)
                if (1 if var3 == i32_load(var2 + 220) else 0):
                    break
                i32_store(var2 + 220, var3)
                var3 = (var3 * var3)
                var12 = func26((var3 * var3))
                i32_store(var2 + 372, func26((var3 * var3)))
                if (1 if var3 == 0 else 0):
                    break
                # Unknown: memory.fill []
                i32_store(var2 + 192, i32_load((var8 + (var11 << 2))))
                i32_store(var2 + 188, i32_load(var1 + 84))
                i32_store(var2 + 84, i32_load(var1 + 88))
                i32_store(var2 + 136, i32_load(var1 + 92))
                i32_store(var2 + 140, i32_load(var1 + 96))
                i32_store(var2 + 176, i32_load(var1 + 100))
                var3 = i32_load(var1 + 104)
                i32_store(var2 + 364, i32_load(var1 + 104))
                i32_store(var2 + 272, i32_load(var1 + 108))
                i32_store(var2 + 212, i32_load(var1 + 112))
                i32_store(var2 + 124, i32_load(var1 + 116))
                var8 = i32_load(var1 + 120)
                i32_store(var2 + 280, i32_load(var1 + 124))
                i32_store(var2 + 328, i32_load(var1 + 128))
                i32_store8(var2 + 353, (1 if i32_load(var1 + 132) != 0 else 0))
                i32_store8(var2 + 335, (1 if i32_load(var1 + 136) != 0 else 0))
                i32_store8(var2 + 333, (1 if i32_load(var1 + 140) != 0 else 0))
                i32_store8(var2 + 334, (1 if i32_load(var1 + 144) != 0 else 0))
                i32_store8(var2 + 336, (1 if i32_load(var1 + 148) != 0 else 0))
                i32_store(var2 + 284, i32_load(var1 + 152))
                i32_store(var2 + 288, i32_load(var1 + 156))
                i32_store(var2 + 292, i32_load(var1 + 160))
                i32_store(var2 + 296, i32_load(var1 + 164))
                i32_store(var2 + 300, i32_load(var1 + 168))
                i32_store(var2 + 308, i32_load(var1 + 172))
                i32_store(var2 + 312, i32_load(var1 + 176))
                i32_store(var2 + 324, i32_load(var1 + 180))
                i32_store(var2 + 320, i32_load(var1 + 184))
                i32_store(var2 + 340, i32_load(var1 + 188))
                i32_store(var2 + 344, i32_load(var1 + 192))
                i32_store(var2 + 348, i32_load(var1 + 196))
                i32_store(var2 + 304, i32_load(var1 + 200))
                i32_store(var2 + 316, i32_load(var1 + 204))
                i32_store8(var2 + 352, (1 if i32_load(var1 + 208) != 0 else 0))
                i32_store8(var2 + 354, (1 if i32_load(var1 + 212) != 0 else 0))
                if var5:
                    i32_store(var2 + 232, func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2))))
                if var3:
                    i32_store(var2 + 24, func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2))))
                if i32_load(var2 + 236):
                    var3 = i32_load(var2 + 232)
                    var1 = 0
                    var5 = i32_load(9142908)
                    while True:  # loop $label1
                        i32_store((var3 + (var1 << 2)), i32_load((var5 + (var4 << 2))))
                        var4 = (var4 + 1)
                        var1 = (var1 + 1)
                        if (1 if (var1 + 1) < i32_load(var2 + 236) else 0):
                            continue
                        break  # end loop
                if i32_load(var2 + 364):
                    var3 = i32_load(var2 + 24)
                    var1 = 0
                    var5 = i32_load(9142908)
                    while True:  # loop $label2
                        i32_store((var3 + (var1 << 2)), i32_load((var5 + (var4 << 2))))
                        var4 = (var4 + 1)
                        var1 = (var1 + 1)
                        if (1 if (var1 + 1) < i32_load(var2 + 364) else 0):
                            continue
                        break  # end loop
                var1 = 0
                while True:  # loop $label3
                    var2 = ((var10 * 1020) + 9299904)
                    var3 = (((var10 * 1020) + 9299904) + (var1 << 2))
                    i64_store((((var10 * 1020) + 9299904) + (var1 << 2)), 429496729700)
                    i32_store(var3 + 16, 100)
                    i64_store(var3 + 8, 429496729700)
                    var1 = (var1 + 5)
                    if (1 if (var1 + 5) != 255 else 0):
                        continue
                    break  # end loop
                if (1 if var8 == 0 else 0):
                    break
                var1 = ((((var8 - 1) & 0xFFFFFFFF) >> 1) + 1)
                var10 = (((((var8 - 1) & 0xFFFFFFFF) >> 1) + 1) & 1)
                var5 = i32_load(9142908)
                if (1 if var8 >= 3 else 0):
                    var8 = (var1 & -2)
                    var3 = 0
                    while True:  # loop $label5
                        var1 = (var5 + (var4 << 2))
                        i32_store((var2 + (i32_load((var5 + (var4 << 2))) << 2)), i32_load(var1 + 4))
                        i32_store((var2 + (i32_load(var1 + 8) << 2)), i32_load(var1 + 12))
                        var4 = (var4 + 4)
                        var3 = (var3 + 2)
                        if (1 if (var3 + 2) != var8 else 0):
                            continue
                        break  # end loop
                if (1 if var10 == 0 else 0):
                    break
                var1 = (var5 + (var4 << 2))
                i32_store((var2 + (i32_load((var5 + (var4 << 2))) << 2)), i32_load(var1 + 4))
                var4 = (var4 + 2)
                var6 = (var6 + 60)
                if (1 if (var6 + 60) < var7 else 0):
                    continue
                break  # end loop
            var3 = i32_load(9142908)
        var6 = i32_load(var3 + 8)
        var7 = (var6 + (i32_load(var3 + 12) * 55))
        if (1 if i32_load(var3 + 8) < (var6 + (i32_load(var3 + 12) * 55)) else 0):
            var11 = (1 if var9 < 623 else 0)
            var12 = (1 if var9 > 622 else 0)
            var4 = var7
            while True:  # loop $label16
                var1 = (i32_load(9142908) + (var6 << 2))
                var13 = i32_load((i32_load(9142908) + (var6 << 2)))
                var2 = ((i32_load((i32_load(9142908) + (var6 << 2))) * 404) + 9568096)
                var3 = i32_load(var1 + 4)
                i32_store(((i32_load((i32_load(9142908) + (var6 << 2))) * 404) + 9568096) + 108, i32_load(var1 + 4))
                i32_store(var2 + 104, var3)
                i32_store(var2 + 68, i32_load(var1 + 8))
                i32_store(var2 + 72, i32_load(var1 + 12))
                i32_store(var2 + 76, i32_load(var1 + 16))
                i32_store(var2 + 80, i32_load(var1 + 20))
                i32_store(var2 + 116, i32_load(var1 + 24))
                var3 = i32_load(var1 + 28)
                i32_store(var2 + 236, i32_load(var1 + 28))
                i32_store(var2 + 92, i32_load(var1 + 32))
                i32_store(var2 + 276, i32_load(var1 + 36))
                i32_store(var2 + 96, i32_load(var1 + 40))
                i32_store(var2 + 224, i32_load(var1 + 44))
                i32_store(var2 + 204, i32_load(var1 + 48))
                i32_store(var2 + 200, i32_load(var1 + 52))
                i32_store(var2 + 228, i32_load(var1 + 56))
                i32_store(var2 + 208, i32_load(var1 + 60))
                var9 = i32_load((var1 - -64))
                i32_store(var2 + 216, i32_load((var1 - -64)))
                var10 = i32_load(var1 + 68)
                i32_store(var2 + 220, i32_load(var1 + 68))
                i32_store(var2 + 192, i32_load(var1 + 76))
                i32_store(var2 + 188, i32_load(var1 + 80))
                i32_store(var2 + 84, i32_load(var1 + 84))
                i32_store(var2 + 136, i32_load(var1 + 88))
                i32_store(var2 + 140, i32_load(var1 + 92))
                i32_store(var2 + 176, i32_load(var1 + 96))
                i32_store(var2 + 112, i32_load(var1 + 100))
                var5 = i32_load(var1 + 104)
                i32_store(var2 + 364, i32_load(var1 + 104))
                i32_store(var2 + 272, i32_load(var1 + 108))
                i32_store(var2 + 212, i32_load(var1 + 112))
                var8 = i32_load(var1 + 116)
                i32_store(var2 + 280, i32_load(var1 + 120))
                i32_store(var2 + 328, i32_load(var1 + 124))
                i32_store8(var2 + 332, (1 if i32_load(var1 + 128) != 0 else 0))
                i32_store8(var2 + 353, (1 if i32_load(var1 + 132) != 0 else 0))
                i32_store8(var2 + 335, (1 if i32_load(var1 + 136) != 0 else 0))
                i32_store8(var2 + 336, (1 if i32_load(var1 + 140) != 0 else 0))
                i32_store(var2 + 284, i32_load(var1 + 144))
                i32_store(var2 + 288, i32_load(var1 + 148))
                i32_store(var2 + 292, i32_load(var1 + 152))
                i32_store(var2 + 296, i32_load(var1 + 156))
                i32_store(var2 + 300, i32_load(var1 + 160))
                i32_store(var2 + 308, i32_load(var1 + 164))
                i32_store(var2 + 312, i32_load(var1 + 168))
                i32_store(var2 + 324, i32_load(var1 + 172))
                i32_store(var2 + 320, i32_load(var1 + 176))
                i32_store(var2 + 340, i32_load(var1 + 180))
                i32_store(var2 + 344, i32_load(var1 + 184))
                i32_store8(var2 + 354, (1 if i32_load(var1 + 188) != 0 else 0))
                if (1 if var11 == 0 else 0):
                    i32_store(var2 + 244, i32_load(var1 + 192))
                if var3:
                    i32_store(var2 + 232, func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2))))
                var3 = func26((var9 * var10))
                i32_store(var2 + 372, func26((var9 * var10)))
                if var5:
                    i32_store(var2 + 24, func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2))))
                if i32_load(var2 + 236):
                    var5 = i32_load(var2 + 232)
                    var1 = 0
                    var9 = i32_load(9142908)
                    while True:  # loop $label7
                        i32_store((var5 + (var1 << 2)), i32_load((var9 + (var4 << 2))))
                        var4 = (var4 + 1)
                        var1 = (var1 + 1)
                        if (1 if (var1 + 1) < i32_load(var2 + 236) else 0):
                            continue
                        break  # end loop
                var5 = (i32_load(var2 + 220) * i32_load(var2 + 216))
                if (1 if (i32_load(var2 + 220) * i32_load(var2 + 216)) == 0 else 0):
                    break
                var1 = 0
                var9 = i32_load(9142908)
                if (1 if var5 != 1 else 0):
                    var14 = (var5 & -2)
                    var10 = 0
                    while True:  # loop $label9
                        var15 = (var9 + (var4 << 2))
                        i32_store8((var1 + var3), (1 if i32_load((var9 + (var4 << 2))) != 0 else 0))
                        i32_store8((var3 + (var1 | 1)), (1 if i32_load(var15 + 4) != 0 else 0))
                        var1 = (var1 + 2)
                        var4 = (var4 + 2)
                        var10 = (var10 + 2)
                        if (1 if (var10 + 2) != var14 else 0):
                            continue
                        break  # end loop
                if (1 if (var5 & 1) == 0 else 0):
                    break
                i32_store8((var1 + var3), (1 if i32_load((var9 + (var4 << 2))) != 0 else 0))
                var4 = (var4 + 1)
                if i32_load(var2 + 364):
                    var3 = i32_load(var2 + 24)
                    var1 = 0
                    var5 = i32_load(9142908)
                    while True:  # loop $label10
                        i32_store((var3 + (var1 << 2)), i32_load((var5 + (var4 << 2))))
                        var4 = (var4 + 1)
                        var1 = (var1 + 1)
                        if (1 if (var1 + 1) < i32_load(var2 + 364) else 0):
                            continue
                        break  # end loop
                var1 = 0
                while True:  # loop $label11
                    var5 = ((var13 * 1020) + 9299904)
                    var3 = (((var13 * 1020) + 9299904) + (var1 << 2))
                    i64_store((((var13 * 1020) + 9299904) + (var1 << 2)), 429496729700)
                    i32_store(var3 + 16, 100)
                    i64_store(var3 + 8, 429496729700)
                    var1 = (var1 + 5)
                    if (1 if (var1 + 5) != 255 else 0):
                        continue
                    break  # end loop
                if (1 if var8 == 0 else 0):
                    break
                var1 = ((((var8 - 1) & 0xFFFFFFFF) >> 1) + 1)
                var10 = (((((var8 - 1) & 0xFFFFFFFF) >> 1) + 1) & 1)
                var9 = i32_load(9142908)
                if (1 if var8 >= 3 else 0):
                    var8 = (var1 & -2)
                    var3 = 0
                    while True:  # loop $label13
                        var1 = (var9 + (var4 << 2))
                        i32_store((var5 + (i32_load((var9 + (var4 << 2))) << 2)), i32_load(var1 + 4))
                        i32_store((var5 + (i32_load(var1 + 8) << 2)), i32_load(var1 + 12))
                        var4 = (var4 + 4)
                        var3 = (var3 + 2)
                        if (1 if (var3 + 2) != var8 else 0):
                            continue
                        break  # end loop
                if (1 if var10 == 0 else 0):
                    break
                var1 = (var9 + (var4 << 2))
                i32_store((var5 + (i32_load((var9 + (var4 << 2))) << 2)), i32_load(var1 + 4))
                var4 = (var4 + 2)
                if (1 if var12 == 0 else 0):
                    break
                var1 = i32_load(var2 + 244)
                if (1 if i32_load(var2 + 244) == 0 else 0):
                    break
                var3 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                i32_store(var2 + 240, func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2))))
                var2 = i32_load(var2 + 244)
                var1 = 0
                var5 = i32_load(9142908)
                while True:  # loop $label15
                    i32_store((var3 + (var1 << 2)), i32_load((var5 + (var4 << 2))))
                    var4 = (var4 + 1)
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) < var2 else 0):
                        continue
                    break  # end loop
                var6 = (var6 + 55)
                if (1 if (var6 + 55) < var7 else 0):
                    continue
                break  # end loop
            var3 = i32_load(9142908)
        var6 = i32_load(var3 + 16)
        var7 = (var6 + (i32_load(var3 + 20) * 23))
        if (1 if i32_load(var3 + 16) < (var6 + (i32_load(var3 + 20) * 23)) else 0):
            var4 = var7
            while True:  # loop $label19
                var1 = (var3 + (var6 << 2))
                var2 = ((i32_load((var3 + (var6 << 2))) * 404) + 9568096)
                var5 = i32_load(var1 + 4)
                if (1 if i32_load(var1 + 4) <= 4 else 0):
                else:
                i32_store(i32_load(((var5 << 2) + 10164)) + 368, 0)
                i32_store(var2 + 68, i32_load((var3 + ((var6 + 2) << 2))))
                i32_store(var2 + 116, i32_load(var1 + 12))
                var8 = i32_load(var1 + 16)
                i32_store(var2 + 244, i32_load(var1 + 16))
                i32_store(var2 + 72, i32_load(var1 + 20))
                i32_store(var2 + 76, i32_load(var1 + 24))
                i32_store(var2 + 80, i32_load(var1 + 28))
                var5 = i32_load(var1 + 32)
                i32_store(var2 + 236, i32_load(var1 + 32))
                i32_store8(var2 + 354, (1 if i32_load(var1 + 36) != 0 else 0))
                i32_store(var2 + 212, i32_load(var1 + 40))
                i32_store(var2 + 104, i32_load(var1 + 44))
                i32_store(var2 + 92, i32_load(var1 + 48))
                i32_store(var2 + 100, i32_load(var1 + 52))
                i32_store(var2 + 120, i32_load(var1 + 56))
                i32_store(var2 + 112, i32_load(var1 + 60))
                if var5:
                    i32_store(var2 + 232, func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2))))
                if var8:
                    var5 = func26((-1 if (1 if var8 > 1073741823 else 0) else (var8 << 2)))
                    i32_store(var2 + 240, func26((-1 if (1 if var8 > 1073741823 else 0) else (var8 << 2))))
                    var8 = i32_load(var2 + 244)
                    var1 = 0
                    while True:  # loop $label17
                        i32_store((var5 + (var1 << 2)), i32_load((var3 + (var4 << 2))))
                        var4 = (var4 + 1)
                        var1 = (var1 + 1)
                        if (1 if (var1 + 1) < var8 else 0):
                            continue
                        break  # end loop
                else:
                if var5:
                    var5 = i32_load(var2 + 232)
                    var1 = 0
                    while True:  # loop $label18
                        i32_store((var5 + (var1 << 2)), i32_load((var3 + (var4 << 2))))
                        var4 = (var4 + 1)
                        var1 = (var1 + 1)
                        if (1 if (var1 + 1) < i32_load(var2 + 236) else 0):
                            continue
                        break  # end loop
                var6 = (var6 + 23)
                if (1 if (var6 + 23) < var7 else 0):
                    continue
                break  # end loop
        var4 = (var3 + (i32_load(var3 + 24) << 2))
        var3 = 0
        while True:  # loop $label20
            var7 = (var3 << 2)
            i32_store(((var3 << 2) + 9561072), i32_load((var4 + var7)))
            var2 = (var7 + 4)
            i32_store(((var7 + 4) + 9561072), i32_load((var2 + var4)))
            var2 = (var7 + 8)
            i32_store(((var7 + 8) + 9561072), i32_load((var2 + var4)))
            var2 = (var7 + 12)
            i32_store(((var7 + 12) + 9561072), i32_load((var2 + var4)))
            var7 = (var7 + 16)
            i32_store(((var7 + 16) + 9561072), i32_load((var4 + var7)))
            var3 = (var3 + 5)
            if (1 if (var3 + 5) != 155 else 0):
                continue
            break  # end loop
        if i32_load8_u(9147152):
            break
        if ((var0 ^ 1) & (1 if i32_load8_u(9147212) != 0 else 0)):
            break
        if (1 if i32_load(9142892) == 0 else 0):
            break
        var2 = i32_load(9561692)
        var6 = 0
        while True:  # loop $label23
            var3 = 0
            while True:  # loop $label22
                var7 = (var2 + (var6 * 286704))
                var4 = ((var2 + (var6 * 286704)) + 283984)
                var0 = (var3 << 2)
                i32_store((((var2 + (var6 * 286704)) + 283984) + (var3 << 2)), i32_load((var0 + 9561072)))
                var1 = (var0 + 4)
                i32_store((var4 + (var0 + 4)), i32_load((var1 + 9561072)))
                var1 = (var0 + 8)
                i32_store((var4 + (var0 + 8)), i32_load((var1 + 9561072)))
                var1 = (var0 + 12)
                i32_store((var4 + (var0 + 12)), i32_load((var1 + 9561072)))
                var0 = (var0 + 16)
                i32_store((var4 + (var0 + 16)), i32_load((var0 + 9561072)))
                var3 = (var3 + 5)
                if (1 if (var3 + 5) != 155 else 0):
                    continue
                break  # end loop
            i32_store(var7 + 283868, i32_load((var7 + 284372)))
            var6 = (var6 + 1)
            if (1 if (var6 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    return func164()

