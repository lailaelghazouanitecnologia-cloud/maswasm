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
# $func911
# ==========================================================
def func911(var0, var1, param2):
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
    var4 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var5 = i32_load(9671128)
    var9 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var9 + 128) == 0 else 0):
        break
    var2 = (var5 + (var0 * 132))
    i32_store8((var5 + (var0 * 132)) + 127, 0)
    var3 = i32_load(var2 + 40)
    if (1 if i32_load(var2 + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var4 + 20, var3)
        i32_store(var4 + 16, 0)
        a_b()
        break
    var2 = i32_load16_u(var2 + 110)
    i32_store(var4 + 4, var3)
    i32_store(var4, (var2 + 16))
    a_b()
    i32_store8(var9 + 128, 0)
    i64_store(var4 + 40, i64_load(9672))
    i64_store(var4 + 32, i64_load(9664))
    if (1 if i32_load8_u(var9 + 125) == 1 else 0):
        var10 = (var5 + (var0 * 132))
        var2 = i32_load16_u((var5 + (var0 * 132)) + 114)
        var7 = (var5 + (var1 * 132))
        var3 = i32_load16_u((var5 + (var1 * 132)) + 114)
        var7 = i32_load16_u(var7 + 112)
        var10 = i32_load16_u(var10 + 112)
        if (1 if i32_load16_u(var7 + 112) != i32_load16_u(var10 + 112) else 0):
            break
        if (1 if var2 < var3 else 0):
            break
        if (1 if var2 > var3 else 0):
            break
        var6 = (1 if var2 != var3 else 0)
        break
        var6 = (1 if (1 if var2 < var3 else 0) else (-1 if (1 if var2 > var3 else 0) else 0))
        var2 = (1 if (1 if var7 > var10 else 0) else (-1 if (1 if var7 < var10 else 0) else 0))
        var3 = 6
        var2 = (((var6 * 3) + var2) + 4)
        if (1 if (((var6 * 3) + var2) + 4) <= 8 else 0):
            var3 = i32_load8_u((var2 + 10184))
        var2 = (var5 + (var0 * 132))
        i32_store8((var5 + (var0 * 132)) + 124, var3)
        var3 = i32_load(((i32_load((i32_load(9215884) + (i32_load(var2 + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if i32_load(((i32_load((i32_load(9215884) + (i32_load(var2 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            # call_indirect via table[var3]
        if (1 if i32_load8_u(var9 + 125) == 3 else 0):
            break
        var9 = i32_load(var2 + 44)
        if i32_load(var2 + 44):
            var7 = i32_load(9142848)
            var3 = i32_load(9215884)
            i32_store((i32_load(9215884) + (var9 << 4)) + 4, 62)
            i32_store((var3 + (i32_load(var2 + 44) << 4)) + 8, i32_load((var5 + (var0 * 132)) + 28))
            i32_store((var3 + (i32_load(var2 + 44) << 4)) + 12, var1)
            i32_store((var3 + (i32_load(var2 + 44) << 4)), (var7 + 20))
            break
        i32_store(var2 + 44, ((Ua(500, 62, i32_load((var5 + (var0 * 132)) + 28), var1) & 0xFFFFFFFF) >> 2))
        break
    var2 = (var5 + (var0 * 132))
    var17 = (var5 + (var0 * 132))
    var2 = i32_load16_u(var2 + 110)
    if (1 if i32_load16_u(var2 + 110) == i32_load16_u((var5 + (var1 * 132)) + 110) else 0):
        break
    if (1 if i32_load(9142848) < (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        break
    if func66((i32_load(9561692) + (var2 * 286704)), (var4 + 32), 1, 1):
        break
    var2 = (var5 + (var1 * 132))
    if (1 if i32_load8_u((var5 + (var1 * 132)) + 125) == 3 else 0):
        break
    func78((var5 + (var1 * 132)), i32_load16_u(var17 + 110), 1, 0)
    if (1 if i32_load(var2 + 92) == 0 else 0):
        break
    var2 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var5 + (var1 * 132)) + 28) else 0):
            break
    var2 = (var5 + (var1 * 132))
    var7 = i32_load16_u((var5 + (var1 * 132)) + 114)
    var10 = i32_load16_u(var2 + 112)
    var12 = i32_load(i32_load(9142424) + 48)
    if i32_load(i32_load(9142424) + 48):
        if (1 if i32_load8_u(9147152) == 0 else 0):
            break
    var3 = i32_load(9142440)
    break
    var3 = i32_load(9142440)
    var6 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var7) + var10) << 1)))
    if (1 if var12 == 2 else 0):
        if (1 if var6 > 1 else 0):
            break
        break
    if (1 if var6 == 0 else 0):
        break
    func80(float(var10), float(var7), i32_load(9142776), 32.0, float((var3 * 96)))
    var7 = i32_load16_u(var2 + 114)
    var10 = i32_load16_u(var2 + 112)
    var12 = (var5 + (var1 * 132))
    var2 = 0
    while True:  # loop $label18
        var8 = i32_load(9142440)
        var3 = var2
        var6 = (var2 << 2)
        var2 = (i32_load((((var2 << 2) | 4) + 8611904)) + var7)
        if (1 if i32_load(9142440) <= (i32_load((((var2 << 2) | 4) + 8611904)) + var7) else 0):
            break
        var11 = (i32_load((var6 + 8611904)) + var10)
        if (1 if var8 <= (i32_load((var6 + 8611904)) + var10) else 0):
            break
        if (1 if (var2 | var11) < 0 else 0):
            break
        var6 = i32_load(9142840)
        var11 = (var11 + 1)
        var14 = (var2 + 1)
        var2 = i32_load((i32_load(9142840) + (((var11 + 1) + ((var2 + 1) * (var8 + 2))) << 2)))
        if (1 if i32_load((i32_load(9142840) + (((var11 + 1) + ((var2 + 1) * (var8 + 2))) << 2))) < 3 else 0):
            break
        var2 = (i32_load(9671128) + (var2 * 132))
        var15 = (i32_load((i32_load(9671128) + (var2 * 132)) + 44) << 2)
        var13 = ((i32_load((i32_load(9671128) + (var2 * 132)) + 44) << 2) | 1)
        var8 = i32_load(9215884)
        var16 = i32_load(var12 + 28)
        if (1 if i32_load(var12 + 28) != i32_load(var2 + 32) else 0):
            break
        if i32_load((var8 + (var13 << 2))):
            break
        if (1 if i32_load8_u(var2 + 123) != 6 else 0):
            break
        i32_store(var2 + 116, i32_load(var2 + 112))
        i32_store(var2 + 32, 0)
        i32_store8(var2 + 123, 0)
        break
        if (1 if i32_load((var8 + (var13 << 2))) != 6 else 0):
            break
        if (1 if i32_load((var8 + ((var15 << 2) | 12))) != var16 else 0):
            break
        func29(var2, 1)
        var6 = i32_load(9142840)
        var2 = (i32_load(9142440) + 2)
        var2 = i32_load((var6 + ((var11 + ((var14 + (i32_load(9142440) + 2)) * var2)) << 2)))
        if (1 if i32_load((var6 + ((var11 + ((var14 + (i32_load(9142440) + 2)) * var2)) << 2))) < 3 else 0):
            break
        var2 = (i32_load(9671128) + (var2 * 132))
        var15 = (i32_load((i32_load(9671128) + (var2 * 132)) + 44) << 2)
        var13 = ((i32_load((i32_load(9671128) + (var2 * 132)) + 44) << 2) | 1)
        var8 = i32_load(9215884)
        var16 = i32_load(var12 + 28)
        if (1 if i32_load(var12 + 28) != i32_load(var2 + 32) else 0):
            break
        if i32_load((var8 + (var13 << 2))):
            break
        if (1 if i32_load8_u(var2 + 123) == 6 else 0):
            break
        if (1 if i32_load((var8 + (var13 << 2))) != 6 else 0):
            break
        if (1 if i32_load((var8 + ((var15 << 2) | 12))) != var16 else 0):
            break
        func29(var2, 1)
        var6 = i32_load(9142840)
        break
        i32_store(var2 + 116, i32_load(var2 + 112))
        i32_store(var2 + 32, 0)
        i32_store8(var2 + 123, 0)
        var2 = (i32_load(9142440) + 2)
        var2 = i32_load((var6 + ((var11 + ((var14 + ((i32_load(9142440) + 2) << 1)) * var2)) << 2)))
        if (1 if i32_load((var6 + ((var11 + ((var14 + ((i32_load(9142440) + 2) << 1)) * var2)) << 2))) < 3 else 0):
            break
        var2 = (i32_load(9671128) + (var2 * 132))
        var11 = (i32_load((i32_load(9671128) + (var2 * 132)) + 44) << 2)
        var8 = ((i32_load((i32_load(9671128) + (var2 * 132)) + 44) << 2) | 1)
        var6 = i32_load(9215884)
        var14 = i32_load(var12 + 28)
        if (1 if i32_load(var12 + 28) != i32_load(var2 + 32) else 0):
            break
        if i32_load((var6 + (var8 << 2))):
            break
        if (1 if i32_load8_u(var2 + 123) == 6 else 0):
            break
        if (1 if i32_load((var6 + (var8 << 2))) != 6 else 0):
            break
        if (1 if i32_load((var6 + ((var11 << 2) | 12))) != var14 else 0):
            break
        func29(var2, 1)
        break
        i32_store(var2 + 116, i32_load(var2 + 112))
        i32_store(var2 + 32, 0)
        i32_store8(var2 + 123, 0)
        var2 = (var3 + 2)
        if (1 if var3 < 13118 else 0):
            continue
        break  # end loop
    var2 = i32_load16_u(var17 + 110)
    var3 = i32_load(var4 + 32)
    if i32_load(var4 + 32):
        if (1 if i32_load(var4 + 48) < var3 else 0):
            break
    var3 = i32_load(var4 + 36)
    if i32_load(var4 + 36):
        if (1 if i32_load(var4 + 52) < var3 else 0):
            break
    var3 = i32_load(var4 + 40)
    if i32_load(var4 + 40):
        if (1 if i32_load(var4 + 56) < var3 else 0):
            break
    var3 = i32_load(var4 + 44)
    if i32_load(var4 + 44):
        if (1 if i32_load(var4 + 60) < var3 else 0):
            break
    var3 = (var5 + (var0 * 132))
    var7 = i32_load8_u((var5 + (var0 * 132)) + 129)
    if (1 if (i32_load8_u((var5 + (var0 * 132)) + 129) & 254) != 14 else 0):
        break
    if (1 if i32_load(var3 + 96) == 0 else 0):
        if (1 if i32_load8_u(var9 + 125) != 1 else 0):
            break
    i32_store8(var9 + 125, 0)
    var0 = (var5 + (var0 * 132))
    i32_store((var5 + (var0 * 132)) + 44, 0)
    var0 = func416(i32_load16_u(var0 + 112), i32_load16_u(var0 + 114), var2, (-1 if (1 if var7 != 15 else 0) else i32_load8_u((var5 + (var1 * 132)) + 122)))
    if func416(i32_load16_u(var0 + 112), i32_load16_u(var0 + 114), var2, (-1 if (1 if var7 != 15 else 0) else i32_load8_u((var5 + (var1 * 132)) + 122))):
        break
    func29(var9, 1)
    break
    func29(var9, 1)
    global global0
    global0 = (var4 - -64)
    return func28((1 if var2 != 0 else 0), 1)

