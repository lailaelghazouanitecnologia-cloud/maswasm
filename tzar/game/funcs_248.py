"""
Auto-generated from WAT. Contains 3 functions.
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
# $func841
# ==========================================================
def func841(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var2 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var7 = i32_load(9671128)
    var4 = i32_load(var1)
    var5 = (i32_load(9671128) + (i32_load(var1) * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 125) == 3 else 0):
        break
    var1 = i32_load(var5 + 20)
    if (1 if i32_load(var5 + 20) == 0 else 0):
        break
    var1 = i32_load(var0)
    var0 = i32_load((i32_load(var1) + (i32_load(var0) << 2)))
    if (1 if i32_load((i32_load(var1) + (i32_load(var0) << 2))) == 0 else 0):
        break
    var6 = (var0 - 1)
    var3 = (((var0 - 1) * 404) + 9568096)
    var8 = i32_load(9561692)
    var7 = i32_load16_u((var7 + (var4 * 132)) + 110)
    var0 = (i32_load(9561692) + (i32_load16_u((var7 + (var4 * 132)) + 110) * 286704))
    var9 = i32_load((((i32_load(9561692) + (i32_load16_u((var7 + (var4 * 132)) + 110) * 286704)) + (i32_load(39136) << 2)) + 281808))
    i32_store(var2, (((i32_load((((var0 - 1) * 404) + 9568096) + 68) * 144) // 10) + (120 if (1 if i32_load((((i32_load(9561692) + (i32_load16_u((var7 + (var4 * 132)) + 110) * 286704)) + (i32_load(39136) << 2)) + 281808)) == 1 else 0) else 0)))
    i32_store(var2 + 4, ((i32_load(var3 + 72) * 144) // 10))
    i32_store(var2 + 8, ((i32_load(var3 + 76) * 144) // 10))
    i32_store(var2 + 12, ((i32_load(var3 + 80) * 144) // 10))
    var3 = (i32_load(var0 + 283976) + 1)
    if (1 if (i32_load(var0 + 283976) + 1) > (i32_load((var0 + 284136)) + i32_load(var0 + 283980)) else 0):
        var1 = 57101
        if (1 if i32_load(var0 + 283908) == i32_load(9142872) else 0):
            break
        break
    if (1 if var3 <= i32_load((var0 + 284000)) else 0):
        break
    var1 = 57113
    if (1 if i32_load((var8 + (var7 * 286704)) + 283908) != i32_load(9142872) else 0):
        break
    a_b()
    break
    if func66(var0, var2, 1, 1):
        break
    var0 = i32_load(i32_load(var5 + 20))
    if (1 if var1 >= 7 else 0):
        break
    var3 = (var1 + 1)
    var5 = (var0 + ((var1 + 1) << 2))
    i32_store((var0 + (var1 << 2)), i32_load((var0 + ((var1 + 1) << 2))))
    if (1 if var3 == 7 else 0):
        break
    var3 = (var1 + 2)
    i32_store(var5, i32_load((var0 + ((var1 + 2) << 2))))
    if (1 if var3 == 7 else 0):
        break
    var3 = (var1 + 3)
    var5 = (var0 + ((var1 + 3) << 2))
    i32_store((var0 + (var3 << 2)), i32_load((var0 + ((var1 + 3) << 2))))
    if (1 if var3 == 7 else 0):
        break
    var3 = (var1 + 4)
    i32_store(var5, i32_load((var0 + ((var1 + 4) << 2))))
    if (1 if var3 == 7 else 0):
        break
    var3 = (var1 + 5)
    var5 = (var0 + ((var1 + 5) << 2))
    i32_store((var0 + (var3 << 2)), i32_load((var0 + ((var1 + 5) << 2))))
    if (1 if var3 == 7 else 0):
        break
    var3 = (var1 + 6)
    i32_store(var5, i32_load((var0 + ((var1 + 6) << 2))))
    if (1 if var3 == 7 else 0):
        break
    i32_store((var0 + (var3 << 2)), i32_load(((var1 << 2) + var0) + 28))
    var1 = 0
    i32_store(var0 + 28, 0)
    var0 = ((var8 + (var7 * 286704)) + 281744)
    i32_store(((var8 + (var7 * 286704)) + 281744), (i32_load(var0) + 9))
    var0 = ((var6 * 404) + 9568096)
    if (1 if var9 == 1 else 0):
        var5 = (var4 * 132)
        while True:  # loop $label5
            var3 = (i32_load(9671128) + var5)
            if (1 if func59((var2 + 28), (var2 + 24), (i32_load(9671128) + var5), var0) == 0 else 0):
                break
            var8 = func34(var6, i32_load16_u(var3 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1)
            if (1 if func34(var6, i32_load16_u(var3 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1) == 0 else 0):
                break
            var7 = i32_load(9671128)
            var3 = (i32_load(9671128) + (var8 * 132))
            if i32_load((i32_load(9671128) + (var8 * 132)) + 28):
                i32_store(var3 + 84, 4)
                i32_store(var3 + 52, (i32_load(var3 + 52) + 4))
                i32_store(var3 + 60, (i32_load(var3 + 60) + 2))
            func69((var5 + var7), var8)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != 9 else 0):
                continue
            break  # end loop
        break
    var1 = (i32_load(9671128) + (var4 * 132))
    if (1 if func59((var2 + 28), (var2 + 24), (i32_load(9671128) + (var4 * 132)), var0) == 0 else 0):
        break
    var1 = func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1)
    if (1 if func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1) == 0 else 0):
        break
    func69((i32_load(9671128) + (var4 * 132)), var1)
    var1 = (i32_load(9671128) + (var4 * 132))
    if (1 if func59((var2 + 28), (var2 + 24), (i32_load(9671128) + (var4 * 132)), var0) == 0 else 0):
        break
    var1 = func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1)
    if (1 if func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1) == 0 else 0):
        break
    func69((i32_load(9671128) + (var4 * 132)), var1)
    var1 = (i32_load(9671128) + (var4 * 132))
    if (1 if func59((var2 + 28), (var2 + 24), (i32_load(9671128) + (var4 * 132)), var0) == 0 else 0):
        break
    var1 = func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1)
    if (1 if func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1) == 0 else 0):
        break
    func69((i32_load(9671128) + (var4 * 132)), var1)
    var1 = (i32_load(9671128) + (var4 * 132))
    if (1 if func59((var2 + 28), (var2 + 24), (i32_load(9671128) + (var4 * 132)), var0) == 0 else 0):
        break
    var1 = func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1)
    if (1 if func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1) == 0 else 0):
        break
    func69((i32_load(9671128) + (var4 * 132)), var1)
    var1 = (i32_load(9671128) + (var4 * 132))
    if (1 if func59((var2 + 28), (var2 + 24), (i32_load(9671128) + (var4 * 132)), var0) == 0 else 0):
        break
    var1 = func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1)
    if (1 if func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1) == 0 else 0):
        break
    func69((i32_load(9671128) + (var4 * 132)), var1)
    var1 = (i32_load(9671128) + (var4 * 132))
    if (1 if func59((var2 + 28), (var2 + 24), (i32_load(9671128) + (var4 * 132)), var0) == 0 else 0):
        break
    var1 = func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1)
    if (1 if func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1) == 0 else 0):
        break
    func69((i32_load(9671128) + (var4 * 132)), var1)
    var1 = (i32_load(9671128) + (var4 * 132))
    if (1 if func59((var2 + 28), (var2 + 24), (i32_load(9671128) + (var4 * 132)), var0) == 0 else 0):
        break
    var1 = func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1)
    if (1 if func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1) == 0 else 0):
        break
    func69((i32_load(9671128) + (var4 * 132)), var1)
    var1 = (i32_load(9671128) + (var4 * 132))
    if (1 if func59((var2 + 28), (var2 + 24), (i32_load(9671128) + (var4 * 132)), var0) == 0 else 0):
        break
    var1 = func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1)
    if (1 if func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1) == 0 else 0):
        break
    func69((i32_load(9671128) + (var4 * 132)), var1)
    var1 = (i32_load(9671128) + (var4 * 132))
    if (1 if func59((var2 + 28), (var2 + 24), (i32_load(9671128) + (var4 * 132)), var0) == 0 else 0):
        break
    var0 = func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1)
    if (1 if func34(var6, i32_load16_u(var1 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1) == 0 else 0):
        break
    func69((i32_load(9671128) + (var4 * 132)), var0)
    if (1 if i32_load(9671124) != 95 else 0):
        break
    if (1 if i32_load(9173808) != var4 else 0):
        break
    global global0
    global0 = (var2 + 32)


# ==========================================================
# $func846
# ==========================================================
def func846(var0, var1, var2):
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
    var2 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var4 = i32_load(9671128)
    var6 = i32_load(var1)
    var7 = (i32_load(9671128) + (i32_load(var1) * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 125) == 3 else 0):
        break
    var1 = i32_load(var7 + 20)
    if (1 if i32_load(var7 + 20) == 0 else 0):
        break
    var3 = i32_load(var0)
    var1 = (i32_load(var0) + 8)
    var0 = i32_load((i32_load(var1) + ((i32_load(var0) + 8) << 2)))
    if (1 if i32_load((i32_load(var1) + ((i32_load(var0) + 8) << 2))) == 0 else 0):
        break
    var9 = (var0 - 1)
    var0 = (((var0 - 1) * 404) + 9568096)
    i32_store(var2, (((i32_load((((var0 - 1) * 404) + 9568096) + 68) * 36) // 10) + 620))
    i32_store(var2 + 4, ((i32_load(var0 + 72) * 36) // 10))
    i32_store(var2 + 8, ((i32_load(var0 + 76) * 36) // 10))
    i32_store(var2 + 12, ((i32_load(var0 + 80) * 36) // 10))
    var8 = i32_load(9561692)
    var10 = (var4 + (var6 * 132))
    var4 = i32_load16_u((var4 + (var6 * 132)) + 110)
    var0 = (i32_load(9561692) + (i32_load16_u((var4 + (var6 * 132)) + 110) * 286704))
    var5 = (i32_load((i32_load(9561692) + (i32_load16_u((var4 + (var6 * 132)) + 110) * 286704)) + 283976) + 1)
    if (1 if (i32_load((i32_load(9561692) + (i32_load16_u((var4 + (var6 * 132)) + 110) * 286704)) + 283976) + 1) > (i32_load((var0 + 284136)) + i32_load(var0 + 283980)) else 0):
        var1 = 57101
        if (1 if i32_load(var0 + 283908) == i32_load(9142872) else 0):
            break
        break
    if (1 if var5 <= i32_load((var0 + 284000)) else 0):
        break
    var1 = 57113
    if (1 if i32_load((var8 + (var4 * 286704)) + 283908) != i32_load(9142872) else 0):
        break
    a_b()
    break
    if func66((var8 + (var4 * 286704)), var2, 1, 1):
        break
    var0 = i32_load(i32_load(var7 + 20))
    if (1 if var1 > 14 else 0):
        break
    var11 = ((3 - var3) & 3)
    if ((3 - var3) & 3):
        var5 = 0
        while True:  # loop $label4
            var1 = (var1 + 1)
            i32_store((var0 + (var1 << 2)), i32_load((var0 + ((var1 + 1) << 2))))
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var11 else 0):
                continue
            break  # end loop
    if (1 if (var3 - 4) <= 2 else 0):
        break
    while True:  # loop $label5
        var3 = (var0 + (var1 << 2))
        var12 = i64_load((var0 + (var1 << 2)) + 4)
        i32_store(var3 + 8, i32_load(var3 + 12))
        i64_store(var3, var12)
        var1 = (var1 + 4)
        i32_store(var3 + 12, i32_load((var0 + ((var1 + 4) << 2))))
        if (1 if var1 != 15 else 0):
            continue
        break  # end loop
    i32_store(var0 + 60, 0)
    var1 = 0
    if func59((var2 + 28), (var2 + 24), var7, ((var9 * 404) + 9568096)):
        var1 = func34(var9, i32_load16_u(var10 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1)
    var0 = (i32_load(9671128) + (var1 * 132))
    if i32_load((i32_load(9671128) + (var1 * 132)) + 28):
        var1 = i32_load(((i32_load(9561692) + (i32_load16_u(var10 + 110) * 286704)) + 284248))
        i32_store(var0 + 84, i32_load(((i32_load(9561692) + (i32_load16_u(var10 + 110) * 286704)) + 284248)))
        func201(var0)
        var3 = (var8 + (var4 * 286704))
        i32_store((var8 + (var4 * 286704)) + 283936, (i32_load(var3 + 283936) + 1))
        var3 = (var3 + 281636)
        i32_store((var3 + 281636), (i32_load(var3) + 1))
        i32_store(var0 + 52, (var1 + i32_load(var0 + 52)))
        i32_store(var0 + 60, (i32_load(var0 + 60) + ((var1 & 0xFFFFFFFF) >> 1)))
        func69((i32_load(9671128) + (var6 * 132)), i32_load(var0 + 28))
    if (1 if i32_load(9671124) != 96 else 0):
        break
    if (1 if i32_load(9173808) != var6 else 0):
        break
    global global0
    global0 = (var2 + 32)


# ==========================================================
# $func853
# ==========================================================
def func853(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if (1 if var1 == 0 else 0):
        break
    var3 = i32_load(9671128)
    var6 = (i32_load(9671128) + (var0 * 132))
    var7 = i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125)
    var1 = i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125)
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 3 else 0):
        break
    if (1 if var1 == 12 else 0):
        break
    var1 = (var3 + (var0 * 132))
    var2 = i32_load((var3 + (var0 * 132)) + 72)
    var5 = i32_load(var1 + 76)
    if (1 if i32_load((var3 + (var0 * 132)) + 72) < i32_load(var1 + 76) else 0):
        var2 = (i32_load(((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 284072)) + var2)
        var2 = ((i32_load(((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 284072)) + var2) if (1 if var2 < var5 else 0) else var5)
        i32_store(var1 + 72, ((i32_load(((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 284072)) + var2) if (1 if var2 < var5 else 0) else var5))
    var4 = i32_load(var1 + 96)
    if i32_load(var1 + 96):
        var4 = (i32_load(9671128) + (var4 * 132))
        if (1 if (i32_load8_u((i32_load(9671128) + (var4 * 132)) + 125) & 251) != 3 else 0):
            if (1 if i32_load(var4 + 32) == var0 else 0):
                break
        i32_store(var1 + 96, 0)
    var4 = 0
    if (1 if var2 != var5 else 0):
        break
    if var4:
        break
    if i32_load((var3 + (var0 * 132)) + 36):
        break
    if (1 if var7 == 1 else 0):
        break
    func403(var6)
    var0 = (var3 + (var0 * 132))
    var3 = i32_load((var3 + (var0 * 132)) + 80)
    var2 = (i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704))
    var1 = i32_load(((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 284320))
    if (1 if i32_load((var3 + (var0 * 132)) + 80) >= i32_load(((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 284320)) else 0):
        break
    var0 = (i32_load((var2 + 284076)) + var3)
    i32_store(var0 + 80, ((i32_load((var2 + 284076)) + var3) if (1 if var0 < var1 else 0) else var1))
    return 0  # Stack underflow

