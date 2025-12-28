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
# $func70
# ==========================================================
def func70(var0, var1, var2, var3):
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
    if (1 if i32_load(var0 + 132) > 0 else 0):
        var7 = i32_load(var0)
        if (1 if i32_load(i32_load(var0) + 44) == 2 else 0):
            var4 = -201342849
            while True:  # loop $label3
                if (1 if (var4 & 1) == 0 else 0):
                    break
                if (1 if i32_load16_u((var0 + (var5 << 2)) + 148) == 0 else 0):
                    break
                var4 = 0
                break
                if (1 if (var4 & 2) == 0 else 0):
                    break
                if (1 if i32_load16_u((var0 + ((var5 << 2) | 4)) + 148) == 0 else 0):
                    break
                var4 = 0
                break
                var4 = ((var4 & 0xFFFFFFFF) >> 2)
                var5 = (var5 + 2)
                if (1 if (var5 + 2) != 32 else 0):
                    continue
                break  # end loop
            if i32_load16_u(var0 + 184):
                break
            if i32_load16_u(var0 + 188):
                break
            if i32_load16_u(var0 + 200):
                break
            var5 = 32
            while True:  # loop $label5
                var4 = (var5 << 2)
                if i32_load16_u((var0 + (var5 << 2)) + 148):
                    break
                if i32_load16_u((var0 + (var4 | 4)) + 148):
                    break
                if i32_load16_u((var0 + (var4 | 8)) + 148):
                    break
                if i32_load16_u((var0 + (var4 | 12)) + 148):
                    break
                var4 = 0
                var5 = (var5 + 4)
                if (1 if (var5 + 4) != 256 else 0):
                    continue
                break  # end loop
            break
            var4 = 1
            i32_store(var7 + 44, var4)
        var4 = i32_load16_u(var0 + 150)
        var13 = (var0 + 148)
        var11 = i32_load((var0 + 2844))
        i32_store16(((var0 + 148) + (i32_load((var0 + 2844)) << 2)) + 6, 65535)
        if (1 if var11 >= 0 else 0):
            var12 = (7 if var4 else 138)
            var10 = (4 if var4 else 3)
            var8 = -1
            var7 = 0
            while True:  # loop $label10
                var5 = var4
                var14 = var7
                var7 = (var7 + 1)
                var4 = i32_load16_u((var13 + ((var7 + 1) << 2)) + 2)
                var9 = (var6 + 1)
                if (1 if (var6 + 1) >= var12 else 0):
                    break
                if (1 if var4 != var5 else 0):
                    break
                var6 = var9
                break
                if (1 if var9 < var10 else 0):
                    var6 = ((var0 + (var5 << 2)) + 2684)
                    i32_store16(((var0 + (var5 << 2)) + 2684), (i32_load16_u(var6) + var9))
                    break
                if var5:
                    if (1 if var5 != var8 else 0):
                        var6 = ((var0 + (var5 << 2)) + 2684)
                        i32_store16(((var0 + (var5 << 2)) + 2684), (i32_load16_u(var6) + 1))
                    i32_store16(var0 + 2748, (i32_load16_u(var0 + 2748) + 1))
                    break
                if (1 if var6 <= 9 else 0):
                    i32_store16(var0 + 2752, (i32_load16_u(var0 + 2752) + 1))
                    break
                i32_store16(var0 + 2756, (i32_load16_u(var0 + 2756) + 1))
                var6 = 0
                if (1 if var4 == 0 else 0):
                    var10 = 3
                    break
                var8 = (1 if var4 == var5 else 0)
                var10 = (3 if (1 if var4 == var5 else 0) else 4)
                var12 = (6 if var8 else 7)
                var8 = var5
                if (1 if var11 != var14 else 0):
                    continue
                break  # end loop
        var4 = i32_load16_u((var0 + 2442))
        var13 = (var0 + 2440)
        var11 = i32_load((var0 + 2856))
        i32_store16(((var0 + 2440) + (i32_load((var0 + 2856)) << 2)) + 6, 65535)
        var6 = 0
        if (1 if var11 >= 0 else 0):
            var12 = (7 if var4 else 138)
            var10 = (4 if var4 else 3)
            var8 = -1
            var7 = 0
            while True:  # loop $label15
                var5 = var4
                var14 = var7
                var7 = (var7 + 1)
                var4 = i32_load16_u((var13 + ((var7 + 1) << 2)) + 2)
                var9 = (var6 + 1)
                if (1 if (var6 + 1) >= var12 else 0):
                    break
                if (1 if var4 != var5 else 0):
                    break
                var6 = var9
                break
                if (1 if var9 < var10 else 0):
                    var6 = ((var0 + (var5 << 2)) + 2684)
                    i32_store16(((var0 + (var5 << 2)) + 2684), (i32_load16_u(var6) + var9))
                    break
                if var5:
                    if (1 if var5 != var8 else 0):
                        var6 = ((var0 + (var5 << 2)) + 2684)
                        i32_store16(((var0 + (var5 << 2)) + 2684), (i32_load16_u(var6) + 1))
                    i32_store16(var0 + 2748, (i32_load16_u(var0 + 2748) + 1))
                    break
                if (1 if var6 <= 9 else 0):
                    i32_store16(var0 + 2752, (i32_load16_u(var0 + 2752) + 1))
                    break
                i32_store16(var0 + 2756, (i32_load16_u(var0 + 2756) + 1))
                var6 = 0
                if (1 if var4 == 0 else 0):
                    var10 = 3
                    break
                var8 = (1 if var4 == var5 else 0)
                var10 = (3 if (1 if var4 == var5 else 0) else 4)
                var12 = (6 if var8 else 7)
                var8 = var5
                if (1 if var11 != var14 else 0):
                    continue
                break  # end loop
        if i32_load16_u((var0 + 2746)):
            break
        if i32_load16_u((var0 + 2690)):
            break
        if i32_load16_u((var0 + 2742)):
            break
        if i32_load16_u((var0 + 2694)):
            break
        if i32_load16_u((var0 + 2738)):
            break
        if i32_load16_u((var0 + 2698)):
            break
        if i32_load16_u((var0 + 2734)):
            break
        if i32_load16_u((var0 + 2702)):
            break
        if i32_load16_u((var0 + 2730)):
            break
        if i32_load16_u((var0 + 2706)):
            break
        if i32_load16_u((var0 + 2726)):
            break
        if i32_load16_u((var0 + 2710)):
            break
        if i32_load16_u((var0 + 2722)):
            break
        if i32_load16_u((var0 + 2714)):
            break
        if i32_load16_u((var0 + 2718)):
            break
        var7 = (3 if i32_load16_u((var0 + 2686)) else 2)
        var4 = (i32_load(var0 + 5800) + ((3 if i32_load16_u((var0 + 2686)) else 2) * 3))
        i32_store(var0 + 5800, ((i32_load(var0 + 5800) + ((3 if i32_load16_u((var0 + 2686)) else 2) * 3)) + 17))
        var5 = (((i32_load(var0 + 5804) + 10) & 0xFFFFFFFF) >> 3)
        var4 = (((var4 + 27) & 0xFFFFFFFF) >> 3)
        if (1 if (((i32_load(var0 + 5804) + 10) & 0xFFFFFFFF) >> 3) <= (((var4 + 27) & 0xFFFFFFFF) >> 3) else 0):
            break
        if (1 if i32_load(var0 + 136) == 4 else 0):
            break
        break
    var5 = (var2 + 5)
    var4 = var5
    if (1 if var1 == 0 else 0):
        break
    if (1 if (var2 + 4) > var4 else 0):
        break
    break
    var1 = i32_load(var0 + 5820)
    if (1 if var4 == var5 else 0):
        var2 = (var3 + 2)
        if (1 if var1 >= 14 else 0):
            var1 = (i32_load16_u(var0 + 5816) | (var2 << var1))
            i32_store16(var0 + 5816, (i32_load16_u(var0 + 5816) | (var2 << var1)))
            var4 = i32_load(var0 + 20)
            i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
            i32_store8((var4 + i32_load(var0 + 8)), var1)
            var1 = i32_load(var0 + 20)
            i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
            i32_store8((var1 + i32_load(var0 + 8)), i32_load8_u((var0 + 5817)))
            var1 = i32_load(var0 + 5820)
            i32_store16(var0 + 5816, (((var2 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
            break
        i32_store16(var0 + 5816, (i32_load16_u(var0 + 5816) | (var2 << var1)))
        i32_store((var1 - 13) + 5820, (var1 + 3))
        break
    var2 = (var3 + 4)
    if (1 if var1 >= 14 else 0):
        var1 = (i32_load16_u(var0 + 5816) | (var2 << var1))
        i32_store16(var0 + 5816, (i32_load16_u(var0 + 5816) | (var2 << var1)))
        var4 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var4 + i32_load(var0 + 8)), var1)
        var1 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var1 + i32_load(var0 + 8)), i32_load8_u((var0 + 5817)))
        var1 = i32_load(var0 + 5820)
        var6 = (((var2 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820)))
        break
    var6 = (i32_load16_u(var0 + 5816) | (var2 << var1))
    var4 = (var1 + 3)
    i32_store((var1 - 13) + 5820, (var1 + 3))
    var8 = i32_load((var0 + 2844))
    var1 = (i32_load((var0 + 2844)) + 65280)
    var2 = i32_load((var0 + 2856))
    if (1 if var4 >= 12 else 0):
        var4 = (var6 | (var1 << var4))
        i32_store16(var0 + 5816, (var6 | (var1 << var4)))
        var6 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var6 + i32_load(var0 + 8)), var4)
        var4 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var4 + i32_load(var0 + 8)), i32_load8_u((var0 + 5817)))
        var1 = i32_load(var0 + 5820)
        var4 = (((var1 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820)))
        var5 = (var1 - 11)
        break
    var5 = (var4 + 5)
    var4 = (var6 | (var1 << var4))
    i32_store(var0 + 5820, var5)
    if (1 if var5 >= 12 else 0):
        var1 = (var4 | (var2 << var5))
        i32_store16(var0 + 5816, (var4 | (var2 << var5)))
        var4 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var4 + i32_load(var0 + 8)), var1)
        var1 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var1 + i32_load(var0 + 8)), i32_load8_u((var0 + 5817)))
        var1 = i32_load(var0 + 5820)
        var6 = (((var2 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820)))
        break
    var6 = (var4 | (var2 << var5))
    var1 = (var5 + 5)
    i32_store((var1 - 11) + 5820, (var5 + 5))
    var5 = (var7 + 65533)
    if (1 if var1 >= 13 else 0):
        var1 = (var6 | (var5 << var1))
        i32_store16(var0 + 5816, (var6 | (var5 << var1)))
        var4 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var4 + i32_load(var0 + 8)), var1)
        var1 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var1 + i32_load(var0 + 8)), i32_load8_u((var0 + 5817)))
        var4 = i32_load(var0 + 5820)
        var1 = (((var5 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820)))
        var4 = (var4 - 12)
        break
    var4 = (var1 + 4)
    var1 = (var6 | (var5 << var1))
    i32_store(var0 + 5820, var4)
    var5 = 0
    var6 = (var0 + 5817)
    while True:  # loop $label27
        var9 = i32_load16_u(((var0 + (i32_load8_u((var5 + 25920)) << 2)) + 2686))
        var1 = (var1 | (i32_load16_u(((var0 + (i32_load8_u((var5 + 25920)) << 2)) + 2686)) << var4))
        i32_store16(var0 + 5816, (var1 | (i32_load16_u(((var0 + (i32_load8_u((var5 + 25920)) << 2)) + 2686)) << var4)))
        if (1 if var4 >= 14 else 0):
            var4 = i32_load(var0 + 20)
            i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
            i32_store8((var4 + i32_load(var0 + 8)), var1)
            var1 = i32_load(var0 + 20)
            i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
            i32_store8((var1 + i32_load(var0 + 8)), i32_load8_u(var6))
            var4 = i32_load(var0 + 5820)
            var1 = ((var9 & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820)))
            i32_store16(var0 + 5816, ((var9 & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
            break
        var4 = (var4 + 3)
        i32_store((var4 - 13) + 5820, (var4 + 3))
        var9 = (1 if var5 != var7 else 0)
        var5 = (var5 + 1)
        if var9:
            continue
        break  # end loop
    var1 = (var0 + 148)
    var4 = (var0 + 2440)
    func367(var0)
    if var3:
        var1 = i32_load(var0 + 5820)
        if (1 if i32_load(var0 + 5820) >= 9 else 0):
            var1 = i32_load(var0 + 20)
            i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
            i32_store8((var1 + i32_load(var0 + 8)), i32_load8_u(var0 + 5816))
            var1 = i32_load(var0 + 20)
            i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
            i32_store8((var1 + i32_load(var0 + 8)), i32_load8_u((var0 + 5817)))
            break
        if (1 if var1 <= 0 else 0):
            break
        var1 = i32_load(var0 + 20)
        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
        i32_store8((var1 + i32_load(var0 + 8)), i32_load8_u(var0 + 5816))
        i32_store(var0 + 5820, 0)
        i32_store16(var0 + 5816, 0)
    return func406(var0, var1, var4)

