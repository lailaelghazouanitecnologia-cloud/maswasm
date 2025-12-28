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
# $func418
# ==========================================================
def func418(var0, var1):
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
    var10 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var2 = i32_load(9671128)
    var1 = (i32_load(9671128) + (var0 * 132))
    var3 = i32_load((i32_load(9671128) + (var0 * 132)) + 20)
    if (1 if i32_load((i32_load(9671128) + (var0 * 132)) + 20) == 0 else 0):
        break
    if (1 if i32_load(var3 + 8) == 0 else 0):
        break
    var4 = i32_load16_u(var1 + 110)
    var6 = i32_load(9561692)
    var8 = i32_load(i32_load(var3))
    var11 = ((i32_load(i32_load(var3)) - 2147483647) if (1 if var8 > 2147483646 else 0) else var8)
    var9 = ((((i32_load(i32_load(var3)) - 2147483647) if (1 if var8 > 2147483646 else 0) else var8) * 404) + 9568096)
    if (1 if i32_load(((((i32_load(i32_load(var3)) - 2147483647) if (1 if var8 > 2147483646 else 0) else var8) * 404) + 9568096) + 264) != 3 else 0):
        if (1 if i32_load(var9 + 280) == 0 else 0):
            break
        var3 = (var6 + (var4 * 286704))
        var5 = (i32_load((var6 + (var4 * 286704)) + 283976) + 1)
        if (1 if (i32_load((var6 + (var4 * 286704)) + 283976) + 1) > (i32_load((var3 + 284136)) + i32_load(var3 + 283980)) else 0):
            var1 = 57101
            if (1 if i32_load(var3 + 283908) == i32_load(9142872) else 0):
                break
            break
        if (1 if var5 <= i32_load((var3 + 284000)) else 0):
            break
        var1 = 57113
        if (1 if i32_load((var6 + (var4 * 286704)) + 283908) != i32_load(9142872) else 0):
            break
        a_b()
        var3 = (var2 + (var0 * 132))
        var11 = i32_load((var2 + (var0 * 132)) + 28)
        var0 = (var6 + (var4 * 286704))
        var2 = i32_load((var6 + (var4 * 286704)) + 281788)
        if (1 if i32_load((var6 + (var4 * 286704)) + 281788) == 0 else 0):
            var1 = func26(16)
            i32_store(func26(16) + 4, 20)
            i32_store(var1, func26(80))
            i64_store(var1 + 8, 85899345920)
            i32_store(var0 + 281788, var1)
            var4 = (var1 + 8)
            var0 = 0
            var1 = i32_load(var1)
            break
        var4 = (var2 + 8)
        var1 = i32_load(var2 + 8)
        var0 = i32_load(var2 + 4)
        if (1 if i32_load(var2 + 8) != i32_load(var2 + 4) else 0):
            var0 = var1
            var1 = i32_load(var2)
            break
        var1 = (i32_load(var2 + 12) + var0)
        i32_store(var2 + 4, (i32_load(var2 + 12) + var0))
        var6 = i32_load(var2)
        var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        if var0:
            # Unknown: memory.copy []
        if var6:
            var0 = i32_load(var2 + 8)
        i32_store(var2, var1)
        i32_store(var4, (var0 + 1))
        i32_store((var1 + (var0 << 2)), var11)
        var0 = i32_load(var3 + 44)
        if i32_load(var3 + 44):
            i32_store((i32_load(9215884) + (var0 << 4)), 0)
        i32_store(var3 + 44, 0)
        i32_store8(var3 + 125, 7)
        break
        var3 = (var2 + (var0 * 132))
        var5 = (1 if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 264) == 1 else 0)
        var7 = (i32_load16_u((var2 + (var0 * 132)) + 118) if (1 if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 264) == 1 else 0) else 0)
        var3 = (i32_load16_u(var3 + 116) if var5 else 0)
        if ((i32_load16_u((var2 + (var0 * 132)) + 118) if (1 if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 264) == 1 else 0) else 0) | (i32_load16_u(var3 + 116) if var5 else 0)):
            if func337((var10 + 12), (var10 + 8), var1, var9, var3, var7):
                break
            break
        if (1 if func338((var10 + 12), (var10 + 8), var1, var9) == 0 else 0):
            break
        var1 = (((var6 + (var4 * 286704)) + (var11 << 2)) + 282828)
        i32_store((((var6 + (var4 * 286704)) + (var11 << 2)) + 282828), (i32_load(var1) - 1))
        var2 = (var0 * 132)
        var9 = func34(var11, i32_load16_u(((var0 * 132) + i32_load(9671128)) + 110), i32_load(var10 + 12), i32_load(var10 + 8), 0, 1)
        if (1 if func34(var11, i32_load16_u(((var0 * 132) + i32_load(9671128)) + 110), i32_load(var10 + 12), i32_load(var10 + 8), 0, 1) == 0 else 0):
            break
        var1 = i32_load(9671128)
        var3 = i32_load((var2 + i32_load(9671128)) + 28)
        var2 = i32_load(9215928)
        if (1 if i32_load(9215928) == 0 else 0):
            break
        var5 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        var7 = i32_load(var2)
        var2 = 0
        while True:  # loop $label9
            if (1 if var3 != i32_load((var1 + (i32_load((var7 + (var2 << 2))) * 132)) + 28) else 0):
                var2 = (var2 + 1)
                if (1 if var5 != (var2 + 1) else 0):
                    continue
                break
            break  # end loop
        break
        var2 = i32_load(9215932)
        if (1 if i32_load(9215932) == 0 else 0):
            break
        var5 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        var7 = i32_load(var2)
        var2 = 0
        while True:  # loop $label12
            if (1 if var3 == i32_load((var1 + (i32_load((var7 + (var2 << 2))) * 132)) + 28) else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var2 = i32_load(9215936)
        if (1 if i32_load(9215936) == 0 else 0):
            break
        var5 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        var7 = i32_load(var2)
        var2 = 0
        while True:  # loop $label14
            if (1 if var3 == i32_load((var1 + (i32_load((var7 + (var2 << 2))) * 132)) + 28) else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var2 = i32_load(9215940)
        if (1 if i32_load(9215940) == 0 else 0):
            break
        var5 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        var7 = i32_load(var2)
        var2 = 0
        while True:  # loop $label16
            if (1 if var3 == i32_load((var1 + (i32_load((var7 + (var2 << 2))) * 132)) + 28) else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var2 = 0
        if (1 if 0 >= 6 else 0):
            func105(i32_load(((var2 << 2) + 9215904)), var9)
            var1 = i32_load(9671128)
        var2 = (var0 * 132)
        if (1 if i32_load(9142872) == i32_load16_u((var1 + (var0 * 132)) + 110) else 0):
            i32_store(var10, i32_load(39236))
            a_b()
        else:
        func69((var1 + var2), var9)
        break
    func238(var11, var4, i32_load((var2 + (var0 * 132)) + 28))
    var3 = 0
    var7 = i32_load(9671128)
    var9 = (i32_load(9671128) + (var0 * 132))
    var2 = i32_load((i32_load(9671128) + (var0 * 132)) + 20)
    var1 = (i32_load(var2 + 8) - 1)
    i32_store(i32_load((i32_load(9671128) + (var0 * 132)) + 20) + 8, (i32_load(var2 + 8) - 1))
    if var1:
        var5 = i32_load(var2)
        var1 = 0
        while True:  # loop $label17
            var1 = (var1 + 1)
            i32_store((var5 + (var1 << 2)), i32_load((var5 + ((var1 + 1) << 2))))
            var3 = i32_load(var2 + 8)
            if (1 if var1 < i32_load(var2 + 8) else 0):
                continue
            break  # end loop
    if (1 if var8 < 2147483647 else 0):
        break
    var5 = i32_load(((var11 * 404) + 9568096) + 180)
    if (1 if i32_load8_u(i32_load(((var11 * 404) + 9568096) + 180) + 23) == 0 else 0):
        break
    var1 = i32_load(var5 + 4)
    if (1 if i32_load(((i32_load(var5 + 4) * 404) + 9568096) + 264) != 3 else 0):
        break
    if i32_load((((var6 + (var4 * 286704)) + (var1 << 2)) + 281808)):
        break
    var15 = i32_load(var5 + 68)
    if i32_load(var5 + 68):
        var1 = 0
        var8 = 1
        var16 = (var6 + (var4 * 286704))
        var6 = 0
        var4 = 0
        while True:  # loop $label22
            var12 = i32_load((var5 + (var1 << 2)) + 28)
            var13 = i32_load(((i32_load((var5 + (var1 << 2)) + 28) * 404) + 9568096) + 264)
            var14 = (1 if i32_load(((i32_load((var5 + (var1 << 2)) + 28) * 404) + 9568096) + 264) == 1 else 0)
            var12 = i32_load(((var16 + (var12 << 2)) + 281808))
            if (1 if i32_load(((var16 + (var12 << 2)) + 281808)) == 1 else 0):
                break
            var8 = ((1 if var13 != 3 else 0) & var8)
            if var12:
                break
            var8 = ((1 if var13 != 0 else 0) & var8)
            break
            var4 = (var4 | var14)
            var6 = (var6 | var14)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var15 else 0):
                continue
            break  # end loop
        if (1 if (((var4 & var8) if (var6 & 1) else var8) & 1) == 0 else 0):
            break
    var6 = (var11 + 2147483647)
    if (1 if i32_load(var2 + 4) != var3 else 0):
        var1 = i32_load(var2)
        break
    var1 = (i32_load(var2 + 12) + var3)
    i32_store(var2 + 4, (i32_load(var2 + 12) + var3))
    var4 = i32_load(var2)
    var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var3:
        # Unknown: memory.copy []
    if var4:
        var3 = i32_load(var2 + 8)
    i32_store(var2, var1)
    var4 = i32_load(var9 + 20)
    i32_store(var2 + 8, (var3 + 1))
    i32_store((var1 + (var3 << 2)), var6)
    var3 = i32_load(var4 + 8)
    if var3:
        func230(var9)
        break
    func29(var9, 1)
    var1 = (var7 + (var0 * 132))
    if (1 if i32_load((var7 + (var0 * 132)) + 92) == 0 else 0):
        break
    var2 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var7 + (var0 * 132)) + 28) else 0):
            break
    if (1 if i32_load(9142872) != i32_load16_u(var1 + 110) else 0):
        break
    var0 = i32_load(((var11 * 404) + 9568096) + 180)
    if (1 if i32_load(((var11 * 404) + 9568096) + 180) == 0 else 0):
        break
    break
    i32_store((i32_load(9215884) + (i32_load((var2 + (var0 * 132)) + 44) << 4)), (i32_load(9142848) + 40))
    global global0
    global0 = (var10 + 16)
    return func53(i32_load(var0 + 12))

