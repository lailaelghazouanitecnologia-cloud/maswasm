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
# $func533
# ==========================================================
def func533(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var2 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var3 = i32_load(9671128)
    var4 = (i32_load(9671128) + (var1 * 132))
    var6 = (var3 + (var0 * 132))
    if (1 if i32_load8_u((var3 + (var0 * 132)) + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var6 + 128) == 0 else 0):
        break
    var5 = (var3 + (var0 * 132))
    i32_store8((var3 + (var0 * 132)) + 127, 0)
    var7 = i32_load(var5 + 40)
    if (1 if i32_load(var5 + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var2 + 20, var7)
        i32_store(var2 + 16, 0)
        a_b()
        break
    var5 = i32_load16_u(var5 + 110)
    i32_store(var2 + 4, var7)
    i32_store(var2, (var5 + 16))
    a_b()
    i32_store8(var6 + 128, 0)
    if (1 if i32_load(38528) != i32_load8_u(var4 + 122) else 0):
        break
    if (1 if i32_load(9142848) < (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        break
    func78(var4, i32_load16_u((var3 + (var0 * 132)) + 110), 0, 0)
    if (1 if i32_load((var3 + (var1 * 132)) + 92) == 0 else 0):
        break
    var4 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var3 + (var1 * 132)) + 28) else 0):
            break
    func29((var3 + (var0 * 132)), 1)
    global global0
    global0 = (var2 + 32)


# ==========================================================
# $func629
# ==========================================================
def func629(var0, var1, var2):
    var3 = 0
    var4 = 0
    var3 = i32_load(var0)
    var4 = i32_load(9687204)
    if i32_load(9687204):
        i32_store(9687204, 0)
    var4 = func26((var3 + 4))
    i32_store(9687208, var3)
    i32_store(9687204, var4)
    if var2:
        # Unknown: memory.copy []
    var1 = 0
    var2 = i32_load(9687204)
    if i32_load(9687204):
        i32_store(9687204, 0)
    var0 = i32_load(var0 + 8)
    i32_store(9147312, i32_load(var0 + 8))
    i32_store(9147324, (var0 ^ -1))
    i32_store(9147320, (var0 ^ -1515870811))
    i32_store(9147316, (var0 ^ 1515870810))
    var0 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var2 = i32_load(9142384)
    var3 = i32_load(9561692)
    var1 = 1
    while True:  # loop $label1
        if (1 if i32_load((var3 + (var1 * 286704)) + 284616) == var2 else 0):
            break
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var0 else 0):
            continue
        break  # end loop
    var1 = 0
    i32_store8(9147210, 1)
    i32_store(9142872, var1)
    if (1 if i32_load8_u(9147208) == 0 else 0):
        var0 = i32_load(9142892)
    if (1 if var0 >= 2 else 0):
        var3 = i32_load(9561692)
        var1 = 1
        while True:  # loop $label3
            var2 = (var3 + (var1 * 286704))
            if (1 if i32_load((var3 + (var1 * 286704)) + 284616) == 0 else 0):
                break
            if (1 if i32_load(var2 + 286684) == 0 else 0):
                break
            i32_store((var2 + 286684), 0)
            var0 = i32_load(9142892)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < var0 else 0):
                continue
            break  # end loop


# ==========================================================
# $func634
# ==========================================================
def func634(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var1 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var2 = (i32_load(9671128) + (var0 * 132))
    var5 = i32_load16_u(var2 + 116)
    var6 = i32_load16_u(var2 + 118)
    var2 = i32_load(9142440)
    if (1 if i32_load(9142440) <= var6 else 0):
        break
    if (1 if var2 <= var5 else 0):
        break
    var4 = ((var5 << 5) - i32_load(9142952))
    var4 = ((var6 << 5) - i32_load(9142956))
    if (1 if (((((var5 << 5) - i32_load(9142952)) * var4) + (((var6 << 5) - i32_load(9142956)) * var4)) - 1) > 9000000 else 0):
        break
    var4 = i32_load(39940)
    var3 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var2 = i32_load16_u((i32_load(9147376) + (((var2 * var6) + var5) << 1)))
    if (1 if var3 == 2 else 0):
        if (1 if var2 > 1 else 0):
            break
        break
    if (1 if var2 == 0 else 0):
        break
    i32_store(var1 + 56, var6)
    i32_store(var1 + 52, var5)
    i32_store(var1 + 48, var4)
    a_b()
    var9 = i32_load(9671136)
    if (1 if i32_load(9671136) < 4 else 0):
        break
    var4 = 3
    while True:  # loop $label7
        var7 = (var4 * 132)
        var2 = ((var4 * 132) + i32_load(9671128))
        if (1 if i32_load8_u(((var4 * 132) + i32_load(9671128)) + 125) != 3 else 0):
            break
        if (1 if ((i32_load(9142848) - i32_load(var2 + 68)) * 25) > 6999 else 0):
            break
        var3 = (i32_load16_u(var2 + 112) - var5)
        var3 = (i32_load16_u(var2 + 114) - var6)
        var3 = i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284348))
        if (1 if ((((i32_load16_u(var2 + 112) - var5) * var3) + ((i32_load16_u(var2 + 114) - var6) * var3)) - 1) > (i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284348)) * var3) else 0):
            break
        if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 348) == 0 else 0):
            break
        var3 = i32_load(var2 + 40)
        if (1 if i32_load(var2 + 40) == 0 else 0):
            break
        if i32_load8_u(9142916):
            i32_store(var1 + 32, var3)
            a_b()
            break
        i32_store(var1 + 24, var3)
        i64_store(var1 + 16, -4602115869219225600)
        i64_store(var1 + 8, 0)
        i64_store(var1, 0)
        a_b()
        if (1 if func34(i32_load(38660), i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110), i32_load16_u(var2 + 112), i32_load16_u(var2 + 114), 0, 1) == 0 else 0):
            break
        var3 = (i32_load(9671128) + var7)
        var2 = i32_load16_u((i32_load(9671128) + var7) + 114)
        var3 = i32_load16_u(var3 + 112)
        var10 = i32_load(i32_load(9142424) + 48)
        if i32_load(i32_load(9142424) + 48):
            if (1 if i32_load8_u(9147152) == 0 else 0):
                break
        var7 = i32_load(9142440)
        break
        var7 = i32_load(9142440)
        var8 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var2) + var3) << 1)))
        if (1 if var10 == 2 else 0):
            if (1 if var8 > 1 else 0):
                break
            break
        if (1 if var8 == 0 else 0):
            break
        func80(float(var3), float(var2), i32_load(9142536), 32.0, float((var7 * 96)))
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var9 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var1 - -64)

