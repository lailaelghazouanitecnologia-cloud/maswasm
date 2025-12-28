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
# $Sb
# Export: Sb
# ==========================================================
def Sb(var0, var1):
    """Export: Sb"""
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
    var26 = 0
    var4 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if i32_load8_u(9147152):
        break
    if i32_load(9147132):
        break
    if var0:
        var23 = i32_load(9561692)
        var18 = i32_load(9142872)
        var22 = (i32_load(9561692) + (i32_load(9142872) * 286704))
        var0 = ((i32_load(9561692) + (i32_load(9142872) * 286704)) + (i32_load(9681952) << 2))
        var24 = i32_load((((i32_load(9561692) + (i32_load(9142872) * 286704)) + (i32_load(9681952) << 2)) + 281808))
        var14 = i32_load(38508)
        var15 = i32_load(38500)
        var7 = i32_load(38448)
        var19 = i32_load(38504)
        var20 = i32_load(38528)
        var3 = i32_load(9215884)
        var6 = i32_load(9671128)
        var0 = i32_load((var0 + 284636))
        if (1 if i32_load((var0 + 284636)) == 0 else 0):
            break
        var16 = i32_load(var0 + 8)
        if (1 if i32_load(var0 + 8) == 0 else 0):
            break
        var21 = i32_load(var0)
        var1 = 0
        while True:  # loop $label10
            var0 = i32_load((var21 + (var1 << 2)))
            if (1 if i32_load((var21 + (var1 << 2))) == 0 else 0):
                break
            var2 = (var6 + (var0 * 132))
            var5 = i32_load8_u((var6 + (var0 * 132)) + 123)
            if (1 if i32_load8_u((var6 + (var0 * 132)) + 123) != 1 else 0):
                var0 = i32_load(var2 + 44)
                var17 = i32_load((var3 + (i32_load(var2 + 44) << 4)) + 4)
                if ((1 if i32_load((var3 + (i32_load(var2 + 44) << 4)) + 4) != 1 else 0) & (1 if var5 != 3 else 0)):
                    break
                if (1 if var17 == 1 else 0):
                    break
                break
            var0 = i32_load8_u((var6 + (i32_load(var2 + 32) * 132)) + 122)
            if (1 if i32_load16_u(var2 + 90) == i32_load8_u((var6 + (i32_load(var2 + 32) * 132)) + 122) else 0):
                break
            if (1 if var0 == var19 else 0):
                break
            if (1 if var0 == var7 else 0):
                break
            if (1 if var0 == var15 else 0):
                break
            if (1 if var0 == var14 else 0):
                break
            if (1 if i32_load8_u(var2 + 129) == 10 else 0):
                break
            if (1 if var5 == 4 else 0):
                break
            var0 = i32_load((var3 + (i32_load(var2 + 44) << 4)) + 4)
            if (1 if i32_load((var3 + (i32_load(var2 + 44) << 4)) + 4) == 4 else 0):
                break
            var13 = (var13 + ((1 if var5 == 6 else 0) | (1 if var0 == 6 else 0)))
            break
            var9 = (var9 + 1)
            break
            var8 = (var8 + 1)
            break
            var11 = (var11 + 1)
            break
            var10 = (var10 + 1)
            break
            var12 = (var12 + 1)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var16 else 0):
                continue
            break  # end loop
        var0 = (var22 + (i32_load(9681956) << 2))
        var22 = i32_load(((var22 + (i32_load(9681956) << 2)) + 281808))
        var0 = i32_load((var0 + 284636))
        if (1 if i32_load((var0 + 284636)) == 0 else 0):
            break
        var16 = i32_load(var0 + 8)
        if (1 if i32_load(var0 + 8) == 0 else 0):
            break
        var21 = i32_load(var0)
        var1 = 0
        while True:  # loop $label20
            var0 = i32_load((var21 + (var1 << 2)))
            if (1 if i32_load((var21 + (var1 << 2))) == 0 else 0):
                break
            var2 = (var6 + (var0 * 132))
            var5 = i32_load8_u((var6 + (var0 * 132)) + 123)
            if (1 if i32_load8_u((var6 + (var0 * 132)) + 123) != 1 else 0):
                var0 = i32_load(var2 + 44)
                var17 = (1 if i32_load((var3 + (i32_load(var2 + 44) << 4)) + 4) == 1 else 0)
                if ((1 if (1 if i32_load((var3 + (i32_load(var2 + 44) << 4)) + 4) == 1 else 0) == 0 else 0) & (1 if var5 != 3 else 0)):
                    break
                if (1 if var17 == 0 else 0):
                    break
                break
            var0 = i32_load8_u((var6 + (i32_load(var2 + 32) * 132)) + 122)
            if (1 if i32_load8_u((var6 + (i32_load((var3 + ((var0 << 4) | 12))) * 132)) + 122) == i32_load8_u((var6 + (i32_load(var2 + 32) * 132)) + 122) else 0):
                break
            if (1 if var0 == var19 else 0):
                break
            if (1 if var0 == var7 else 0):
                break
            if (1 if var0 == var15 else 0):
                break
            if (1 if var0 == var14 else 0):
                break
            if (1 if i32_load8_u(var2 + 129) == 10 else 0):
                break
            if (1 if var5 == 4 else 0):
                break
            var0 = i32_load((var3 + (i32_load(var2 + 44) << 4)) + 4)
            if (1 if i32_load((var3 + (i32_load(var2 + 44) << 4)) + 4) == 4 else 0):
                break
            var13 = (var13 + ((1 if var5 == 6 else 0) | (1 if var0 == 6 else 0)))
            break
            var10 = (var10 + 1)
            break
            var11 = (var11 + 1)
            break
            var8 = (var8 + 1)
            break
            var9 = (var9 + 1)
            break
            var12 = (var12 + 1)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var16 else 0):
                continue
            break  # end loop
        var16 = (var23 + (var18 * 286704))
        var0 = ((var23 + (var18 * 286704)) + (i32_load(9681960) << 2))
        var21 = i32_load((((var23 + (var18 * 286704)) + (i32_load(9681960) << 2)) + 281808))
        var0 = i32_load((var0 + 284636))
        if (1 if i32_load((var0 + 284636)) == 0 else 0):
            break
        var17 = i32_load(var0 + 8)
        if (1 if i32_load(var0 + 8) == 0 else 0):
            break
        var25 = i32_load(var0)
        var1 = 0
        while True:  # loop $label30
            var0 = i32_load((var25 + (var1 << 2)))
            if (1 if i32_load((var25 + (var1 << 2))) == 0 else 0):
                break
            var2 = (var6 + (var0 * 132))
            var5 = i32_load8_u((var6 + (var0 * 132)) + 123)
            if (1 if i32_load8_u((var6 + (var0 * 132)) + 123) != 1 else 0):
                var0 = i32_load(var2 + 44)
                var26 = (1 if i32_load((var3 + (i32_load(var2 + 44) << 4)) + 4) == 1 else 0)
                if ((1 if (1 if i32_load((var3 + (i32_load(var2 + 44) << 4)) + 4) == 1 else 0) == 0 else 0) & (1 if var5 != 3 else 0)):
                    break
                if (1 if var26 == 0 else 0):
                    break
                break
            var0 = i32_load8_u((var6 + (i32_load(var2 + 32) * 132)) + 122)
            if (1 if i32_load8_u((var6 + (i32_load((var3 + ((var0 << 4) | 12))) * 132)) + 122) == i32_load8_u((var6 + (i32_load(var2 + 32) * 132)) + 122) else 0):
                break
            if (1 if var0 == var19 else 0):
                break
            if (1 if var0 == var7 else 0):
                break
            if (1 if var0 == var15 else 0):
                break
            if (1 if var0 == var14 else 0):
                break
            if (1 if i32_load8_u(var2 + 129) == 10 else 0):
                break
            if (1 if var5 == 4 else 0):
                break
            var0 = i32_load((var3 + (i32_load(var2 + 44) << 4)) + 4)
            if (1 if i32_load((var3 + (i32_load(var2 + 44) << 4)) + 4) == 4 else 0):
                break
            var13 = (var13 + ((1 if var5 == 6 else 0) | (1 if var0 == 6 else 0)))
            break
            var10 = (var10 + 1)
            break
            var11 = (var11 + 1)
            break
            var8 = (var8 + 1)
            break
            var9 = (var9 + 1)
            break
            var12 = (var12 + 1)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var17 else 0):
                continue
            break  # end loop
        var3 = 0
        var2 = 0
        var14 = 0
        var15 = 0
        var0 = (i32_load(9142848) * 25)
        var1 = ((((i32_load(9142848) * 25) & 0xFFFFFFFF) // 10000) * 15)
        var7 = i32_load((var16 + 278572))
        if (1 if ((((i32_load(9142848) * 25) & 0xFFFFFFFF) // 10000) * 15) >= i32_load(i32_load((var16 + 278572)) + 8) else 0):
            break
        if (1 if var0 < 40000 else 0):
            break
        var0 = (i32_load(var7) + (var1 << 2))
        var15 = (i32_load((i32_load(var7) + (var1 << 2)) + 28) - i32_load((var0 - 212)))
        var14 = (i32_load(var0 + 24) - i32_load((var0 - 216)))
        var2 = (i32_load(var0 + 20) - i32_load((var0 - 220)))
        var6 = (i32_load(var0 + 16) - i32_load((var0 - 224)))
        var19 = i32_load(9142892)
        if (1 if i32_load(9142892) >= 2 else 0):
            var20 = (var18 * var19)
            var5 = i32_load(9143004)
            var1 = 1
            while True:  # loop $label33
                var0 = (var23 + (var1 * 286704))
                if i32_load8_u((var5 + (i32_load((var23 + (var1 * 286704)) + 283908) + var20))):
                    break
                if (1 if var3 > 999 else 0):
                    break
                var18 = i32_load8_u(var0 + 283972)
                var16 = i32_load8_u((var0 + 283974))
                var17 = i32_load8_u((var0 + 283973))
                var7 = ((var3 << 2) + 9147392)
                i32_store(((var3 << 2) + 9147392) + 4, var0)
                i32_store(var7, ((var16 | (var17 << 8)) | (var18 << 16)))
                var18 = i32_load(var0 + 284616)
                i32_store(var7 + 8, (i32_load(var0 + 284616) if var18 else i32_load(var0 + 284628)))
                var3 = (var3 + 7)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var19 else 0):
                    continue
                break  # end loop
        i32_store(var4 + 44, var3)
        i32_store(var4 + 40, var15)
        i32_store(var4 + 36, var14)
        i32_store(var4 + 32, var2)
        i32_store(var4 + 28, var6)
        i32_store(var4 + 24, ((var22 + var24) + var21))
        i32_store(var4 + 20, var13)
        i32_store(var4 + 16, var12)
        i32_store(var4 + 12, var10)
        i32_store(var4 + 8, var11)
        i32_store(var4 + 4, var8)
        i32_store(var4, var9)
        a_b()
        break
    a_b()
    global global0
    global0 = (var4 + 48)
    return 0

