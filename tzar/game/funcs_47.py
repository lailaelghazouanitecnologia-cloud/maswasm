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
# $func57
# ==========================================================
def func57(var0):
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
    var10 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    if (1 if i32_load8_u(9142917) == 0 else 0):
        i32_store(9143000, var0)
        i32_store(9671120, 0)
        i32_store(9263840, 0)
        var11 = i32_load(9671128)
        var7 = i32_load(9561692)
        var12 = i32_load(9142872)
        var5 = (i32_load(9561692) + (i32_load(9142872) * 286704))
        while True:  # loop $label4
            var1 = i32_load(((var5 + (var3 << 2)) + 284636))
            if (1 if i32_load(((var5 + (var3 << 2)) + 284636)) == 0 else 0):
                break
            var6 = i32_load(var1 + 8)
            if (1 if i32_load(var1 + 8) == 0 else 0):
                break
            var8 = i32_load(var1)
            var1 = 0
            if (1 if var6 != 1 else 0):
                var13 = (var6 & -2)
                var4 = 0
                while True:  # loop $label3
                    var9 = (var1 << 2)
                    var14 = i32_load((var8 + (var1 << 2)))
                    if (1 if i32_load((var8 + (var1 << 2))) == 0 else 0):
                        break
                    var14 = i32_load((var11 + (var14 * 132)) + 24)
                    if (1 if i32_load((var11 + (var14 * 132)) + 24) == 0 else 0):
                        break
                    var2 = ((1 if i32_load(var14 + 8) != 0 else 0) | var2)
                    var9 = i32_load((var8 + (var9 | 4)))
                    if (1 if i32_load((var8 + (var9 | 4))) == 0 else 0):
                        break
                    var9 = i32_load((var11 + (var9 * 132)) + 24)
                    if (1 if i32_load((var11 + (var9 * 132)) + 24) == 0 else 0):
                        break
                    var2 = ((1 if i32_load(var9 + 8) != 0 else 0) | var2)
                    var1 = (var1 + 2)
                    var4 = (var4 + 2)
                    if (1 if (var4 + 2) != var13 else 0):
                        continue
                    break  # end loop
            if (1 if (var6 & 1) == 0 else 0):
                break
            var1 = i32_load((var8 + (var1 << 2)))
            if (1 if i32_load((var8 + (var1 << 2))) == 0 else 0):
                break
            var1 = i32_load((var11 + (var1 * 132)) + 24)
            if (1 if i32_load((var11 + (var1 * 132)) + 24) == 0 else 0):
                break
            var2 = ((1 if i32_load(var1 + 8) != 0 else 0) | var2)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != 255 else 0):
                continue
            break  # end loop
        var1 = 1
        i32_store(9671120, 1)
        i32_store8(9262828, 1)
        i32_store(9263072, 9262808)
        var3 = (((1 if i32_load((var7 + (var12 * 286704)) + 283936) != 0 else 0) | var2) & 1)
        i32_store8(9256756, (((1 if i32_load((var7 + (var12 * 286704)) + 283936) != 0 else 0) | var2) & 1))
        var6 = i32_load8_u(9143020)
        if (var3 if i32_load8_u(9143020) else 1):
            i32_store(9671120, 2)
            i32_store(9263076, 9256736)
            var1 = 2
        var3 = i32_load((((var7 + (var12 * 286704)) + (i32_load(38428) << 2)) + 281808))
        i32_store8(9256888, (1 if i32_load((((var7 + (var12 * 286704)) + (i32_load(38428) << 2)) + 281808)) != 0 else 0))
        if var3:
            break
        if (1 if var6 == 0 else 0):
            break
        var2 = var1
        break
        var2 = (var1 + 1)
        i32_store(9671120, (var1 + 1))
        i32_store(((var1 << 2) + 9263072), 9256868)
        var4 = 0
        while True:  # loop $label11
            var3 = ((var4 * 404) + 9568096)
            if (1 if i32_load(((var4 * 404) + 9568096) + 264) != 2 else 0):
                break
            if (1 if i32_load(var3 + 268) > 2 else 0):
                break
            var3 = i32_load(((var7 + (var4 << 2)) + 284636))
            if (1 if i32_load(((var7 + (var4 << 2)) + 284636)) == 0 else 0):
                break
            var8 = i32_load(var3 + 8)
            if (1 if i32_load(var3 + 8) == 0 else 0):
                break
            var3 = i32_load(var3)
            var1 = 0
            while True:  # loop $label10
                var5 = i32_load((var3 + (var1 << 2)))
                if (1 if i32_load((var3 + (var1 << 2))) == 0 else 0):
                    break
                var5 = i32_load((var11 + (var5 * 132)) + 36)
                if (1 if i32_load((var11 + (var5 * 132)) + 36) == 0 else 0):
                    break
                if (1 if var12 == i32_load16_u((var11 + (var5 * 132)) + 110) else 0):
                    break
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var8 else 0):
                    continue
                break  # end loop
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != 255 else 0):
                continue
            break  # end loop
        i32_store8(9257020, 0)
        if var6:
            i32_store8(9257152, 0)
            var1 = var2
            break
        i32_store8(9257152, 0)
        i32_store(((var2 << 2) + 9263072), 9257000)
        var1 = (var2 + 1)
        break
        var1 = (var2 + 1)
        i32_store(9671120, (var2 + 1))
        i32_store8(9257020, 1)
        i32_store8(9257152, 0)
        i32_store(((var2 << 2) + 9263072), 9257000)
        if (1 if var6 == 0 else 0):
            break
        var3 = i32_load(9142912)
        i32_store8(9257284, (1 if i32_load(9142912) != 0 else 0))
        if var3:
            break
        var3 = var1
        if var6:
            break
        break
        i32_store(((var1 << 2) + 9263072), 9257132)
        i32_store8(9257284, (1 if i32_load(9142912) != 0 else 0))
        var1 = (var1 + 1)
        var3 = (var1 + 1)
        i32_store(9671120, (var1 + 1))
        i32_store(((var1 << 2) + 9263072), 9257264)
        var2 = 0
        var8 = i32_load(9215884)
        var4 = (var7 + (var12 * 286704))
        var1 = i32_load(((var7 + (var12 * 286704)) + 284676))
        if (1 if i32_load(((var7 + (var12 * 286704)) + 284676)) == 0 else 0):
            break
        var5 = i32_load(var1 + 8)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        var13 = i32_load(var1)
        var1 = 0
        while True:  # loop $label18
            var2 = i32_load((var13 + (var1 << 2)))
            if (1 if i32_load((var13 + (var1 << 2))) == 0 else 0):
                break
            var2 = (var11 + (var2 * 132))
            if (1 if i32_load8_u((var11 + (var2 * 132)) + 122) != 10 else 0):
                break
            var9 = i32_load(var2 + 44)
            if (1 if ((1 if i32_load((var8 + (i32_load(var2 + 44) << 4)) + 4) == 22 else 0) | (1 if var9 == 0 else 0)) == 0 else 0):
                break
            if i32_load8_u(var2 + 125):
                break
            if i32_load(var2 + 36):
                break
            if (1 if i32_load8_u(var2 + 129) == 10 else 0):
                break
            var2 = 1
            break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var5 else 0):
                continue
            break  # end loop
        var2 = 0
        var1 = i32_load((var4 + 284952))
        if (1 if i32_load((var4 + 284952)) == 0 else 0):
            break
        var5 = i32_load(var1 + 8)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        var13 = i32_load(var1)
        var1 = 0
        while True:  # loop $label21
            var4 = i32_load((var13 + (var1 << 2)))
            if (1 if i32_load((var13 + (var1 << 2))) == 0 else 0):
                break
            var4 = (var11 + (var4 * 132))
            if (1 if i32_load8_u((var11 + (var4 * 132)) + 122) != 79 else 0):
                break
            var9 = i32_load(var4 + 44)
            if (1 if ((1 if i32_load((var8 + (i32_load(var4 + 44) << 4)) + 4) == 22 else 0) | (1 if var9 == 0 else 0)) == 0 else 0):
                break
            if i32_load8_u(var4 + 125):
                break
            if i32_load(var4 + 36):
                break
            if (1 if i32_load8_u(var4 + 129) == 10 else 0):
                break
            var2 = 1
            break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var5 else 0):
                continue
            break  # end loop
        var1 = i32_load(((var7 + (var12 * 286704)) + 284892))
        if (1 if i32_load(((var7 + (var12 * 286704)) + 284892)) == 0 else 0):
            break
        var5 = i32_load(var1 + 8)
        if (1 if i32_load(var1 + 8) == 0 else 0):
            break
        var13 = i32_load(var1)
        var1 = 0
        while True:  # loop $label25
            var4 = i32_load((var13 + (var1 << 2)))
            if (1 if i32_load((var13 + (var1 << 2))) == 0 else 0):
                break
            var4 = (var11 + (var4 * 132))
            if (1 if i32_load8_u((var11 + (var4 * 132)) + 122) != 64 else 0):
                break
            var9 = i32_load(var4 + 44)
            if (1 if ((1 if i32_load((var8 + (i32_load(var4 + 44) << 4)) + 4) == 22 else 0) | (1 if var9 == 0 else 0)) == 0 else 0):
                break
            if i32_load8_u(var4 + 125):
                break
            if i32_load(var4 + 36):
                break
            if (1 if i32_load8_u(var4 + 129) == 10 else 0):
                break
            i32_store8(9257416, 1)
            break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var5 else 0):
                continue
            break  # end loop
        i32_store8(9257416, var2)
        if (1 if (var2 | (1 if var6 == 0 else 0)) != 1 else 0):
            break
        var1 = (var3 + 1)
        i32_store(9671120, (var3 + 1))
        i32_store(((var3 << 2) + 9263072), 9257396)
        if var6:
            var3 = var1
            break
        var3 = (var3 + 2)
        i32_store(9671120, (var3 + 2))
        i32_store8(9257548, 1)
        i32_store(((var1 << 2) + 9263072), 9257528)
        var1 = 0
        var4 = i32_load(38764)
        var8 = i32_load(38456)
        var5 = (var7 + (var12 * 286704))
        while True:  # loop $label29
            var2 = ((var1 * 404) + 9568096)
            if i32_load(((var1 * 404) + 9568096) + 264):
                break
            if (1 if i32_load(var2 + 268) == 1 else 0):
                break
            if (1 if i32_load(var2 + 92) == 0 else 0):
                break
            if (1 if var1 == var8 else 0):
                break
            if (1 if var1 == var4 else 0):
                break
            if i32_load(((var5 + (var1 << 2)) + 281808)):
                break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != 255 else 0):
                continue
            break  # end loop
        i32_store8(9261640, 0)
        if (1 if var6 == 0 else 0):
            break
        var2 = var3
        break
        i32_store8(9261640, 1)
        var2 = (var3 + 1)
        i32_store(9671120, (var3 + 1))
        i32_store(((var3 << 2) + 9263072), 9261620)
        var3 = (var7 + (var12 * 286704))
        if (1 if i32_load((((var7 + (var12 * 286704)) + (var8 << 2)) + 281808)) == 0 else 0):
            var3 = i32_load(((var3 + (var4 << 2)) + 281808))
            i32_store8(9261772, (1 if i32_load(((var3 + (var4 << 2)) + 281808)) != 0 else 0))
            if var3:
                break
            if (1 if var6 == 0 else 0):
                break
            var1 = var2
            break
        i32_store8(9261772, 1)
        var1 = (var2 + 1)
        i32_store(9671120, (var2 + 1))
        i32_store(((var2 << 2) + 9263072), 9261752)
        var3 = (var7 + (var12 * 286704))
        if i32_load((((var7 + (var12 * 286704)) + (i32_load(38440) << 2)) + 281808)):
            break
        if i32_load(((var3 + (i32_load(38772) << 2)) + 281808)):
            break
        var3 = i32_load((((var7 + (var12 * 286704)) + (i32_load(38928) << 2)) + 281808))
        i32_store8(9262432, (1 if i32_load((((var7 + (var12 * 286704)) + (i32_load(38928) << 2)) + 281808)) != 0 else 0))
        if var3:
            break
        if (1 if var6 == 0 else 0):
            break
        var2 = var1
        break
        i32_store8(9262432, 1)
        var2 = (var1 + 1)
        i32_store(9671120, (var1 + 1))
        i32_store(((var1 << 2) + 9263072), 9262412)
        var3 = 0
        var1 = i32_load((((var7 + (var12 * 286704)) + (i32_load(38528) << 2)) + 284636))
        if i32_load((((var7 + (var12 * 286704)) + (i32_load(38528) << 2)) + 284636)):
            var5 = i32_load(var1 + 8)
            if i32_load(var1 + 8):
                var13 = i32_load(var1)
                var1 = 0
                var3 = 1
                while True:  # loop $label38
                    var9 = i32_load((var13 + (var1 << 2)))
                    if i32_load((var13 + (var1 << 2))):
                        if (1 if i32_load((var11 + (var9 * 132)) + 80) > 449 else 0):
                            break
                    var1 = (var1 + 1)
                    var3 = (1 if (var1 + 1) < var5 else 0)
                    if (1 if var1 != var5 else 0):
                        continue
                    break  # end loop
            i32_store8(9262564, var3)
            if (1 if var6 == 0 else 0):
                break
            var3 = var2
            break
        i32_store8(9262564, 0)
        if (1 if var6 == 0 else 0):
            break
        var3 = var2
        break
        i32_store8(9262564, (var3 & 1))
        var3 = (var2 + 1)
        i32_store(9671120, (var2 + 1))
        i32_store(((var2 << 2) + 9263072), 9262544)
        var1 = 0
        var11 = i32_load(38932)
        var5 = (var7 + (var12 * 286704))
        while True:  # loop $label43
            if (1 if i32_load(((var5 + (var1 << 2)) + 281808)) == 0 else 0):
                break
            var2 = ((var1 * 404) + 9568096)
            if i32_load(((var1 * 404) + 9568096) + 264):
                break
            var13 = i32_load(var2 + 268)
            if (1 if i32_load(var2 + 268) == 1 else 0):
                break
            if (1 if i32_load(var2 + 92) == 0 else 0):
                break
            if (1 if var13 == 2 else 0):
                break
            if (1 if var1 == var11 else 0):
                break
            if (1 if var1 == var8 else 0):
                break
            if (1 if var1 == var4 else 0):
                break
            if (1 if i32_load(var2 + 224) > 1 else 0):
                break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != 255 else 0):
                continue
            break  # end loop
        i32_store8(9262036, 0)
        if (1 if var6 == 0 else 0):
            break
        var2 = var3
        break
        i32_store8(9262036, 1)
        var2 = (var3 + 1)
        i32_store(9671120, (var3 + 1))
        i32_store(((var3 << 2) + 9263072), 9262016)
        var1 = 0
        var4 = i32_load(38704)
        var11 = i32_load(38752)
        var8 = i32_load(38776)
        var5 = i32_load(38696)
        var13 = i32_load(38692)
        var9 = i32_load(38756)
        var14 = i32_load(38496)
        var15 = i32_load(38452)
        var16 = (var7 + (var12 * 286704))
        while True:  # loop $label48
            if (1 if i32_load(((var16 + (var1 << 2)) + 281808)) == 0 else 0):
                break
            var3 = ((var1 * 404) + 9568096)
            if i32_load(((var1 * 404) + 9568096) + 264):
                break
            if (1 if i32_load(var3 + 268) == 1 else 0):
                break
            if (1 if i32_load(var3 + 92) == 0 else 0):
                break
            if (1 if var1 == var15 else 0):
                break
            if (1 if var1 == var14 else 0):
                break
            if (1 if var1 == var9 else 0):
                break
            if (1 if var1 == var13 else 0):
                break
            if (1 if var1 == var5 else 0):
                break
            if (1 if var1 == var8 else 0):
                break
            if (1 if var1 == var11 else 0):
                break
            if (1 if var1 == var4 else 0):
                break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != 255 else 0):
                continue
            break  # end loop
        i32_store8(9261904, 0)
        if (1 if var6 == 0 else 0):
            break
        var3 = var2
        break
        i32_store8(9261904, 1)
        var3 = (var2 + 1)
        i32_store(9671120, (var2 + 1))
        i32_store(((var2 << 2) + 9263072), 9261884)
        var1 = 0
        var7 = (var7 + (var12 * 286704))
        while True:  # loop $label53
            if (1 if i32_load(((var7 + (var1 << 2)) + 281808)) == 0 else 0):
                break
            var2 = ((var1 * 404) + 9568096)
            if i32_load(((var1 * 404) + 9568096) + 264):
                break
            if (1 if i32_load(var2 + 268) == 1 else 0):
                break
            if (1 if i32_load(var2 + 92) == 0 else 0):
                break
            if (1 if i32_load(var2 + 224) == 1 else 0):
                break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != 255 else 0):
                continue
            break  # end loop
        i32_store8(9262168, 0)
        if var6:
            var2 = var3
            break
        var2 = var3
        break
        var2 = (var3 + 1)
        i32_store(9671120, (var3 + 1))
        i32_store8(9262168, 1)
        i32_store(((var3 << 2) + 9263072), 9262148)
        if (1 if var6 == 0 else 0):
            break
        i32_store8(9257548, 1)
        var1 = 9257528
        var3 = (var2 + 1)
        i32_store(9671120, (var2 + 1))
        i32_store(((var2 << 2) + 9263072), var1)
        var2 = var3
        var1 = 0
        var4 = i32_load(9147120)
        if (1 if i32_load(9147120) == 0 else 0):
            break
        while True:  # loop $label58
            var0 = i32_load(9143000)
            var2 = ((i32_load(9143000) * var4) + var1)
            if (1 if ((i32_load(9143000) * var4) + var1) == i32_load(9671120) else 0):
                break
            var0 = i32_load(((var2 << 2) + 9263072))
            var3 = i32_load8_u(i32_load(((var2 << 2) + 9263072)) + 20)
            var0 = i32_load(var0 + 8)
            i64_store(var10 + 32, 0)
            i64_store(var10 + 40, 0)
            i64_store(var10 + 48, 0)
            i64_store(var10 + 56, 4294967295)
            i32_store(var10 + 20, var0)
            i32_store(var10 + 24, var3)
            i32_store(var10 + 28, 0)
            i32_store(var10 + 16, var1)
            a_b()
            var1 = (var1 + 1)
            var4 = i32_load(9147120)
            if (1 if (var1 + 1) < i32_load(9147120) else 0):
                continue
            break  # end loop
        var2 = i32_load(9671120)
        var0 = i32_load(9143000)
        i32_store(var10 + 4, var2)
        i32_store(var10, var0)
        a_b()
        i32_store8(9684768, 1)
    global global0
    global0 = (var10 - -64)
    return var10

