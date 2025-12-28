"""
Auto-generated from WAT. Contains 2 functions.
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
# $func464
# ==========================================================
def func464(var0):
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
    var11 = i32_load(var0)
    var16 = i32_load(var0 + 12)
    var12 = i32_load(var0 + 4)
    var8 = i32_load(var0 + 8)
    var6 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    if (1 if i32_load8_u(9142916) == 0 else 0):
        if var11:
            while True:  # loop $label0
                var3 = i32_load((var16 + (var2 << 2)))
                var5 = ((i32_load(i32_load((var16 + (var2 << 2)))) * (i32_load(var3 + 4) + 2)) << 2)
                var4 = (((i32_load(i32_load((var16 + (var2 << 2)))) * (i32_load(var3 + 4) + 2)) << 2) + var4)
                if i32_load(var3 + 56):
                    var3 = (var4 + var5)
                    var1 = (((var4 + var5) - var8) if (1 if var3 > (var1 + var8) else 0) else var1)
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != var11 else 0):
                    continue
                break  # end loop
        var13 = (i32_load(9684256) & 511)
        i32_store(9684256, ((i32_load(9684256) & 511) + 1))
        var7 = func26((var1 + var8))
        i32_store(((var13 << 2) + 9682208), func26((var1 + var8)))
        if var11:
            while True:  # loop $label5
                var3 = i32_load((var16 + (var14 << 2)))
                var15 = i32_load(i32_load((var16 + (var14 << 2))) + 4)
                var4 = i32_load(var3)
                var9 = (i32_load(i32_load((var16 + (var14 << 2))) + 4) * i32_load(var3))
                var17 = i32_load(var3 + 36)
                var5 = (var4 << 2)
                var18 = i32_load(var3 + 40)
                var1 = 1
                if ((1 if var15 < 16384 else 0) & (1 if var4 <= 16383 else 0)):
                    break
                while True:  # loop $label3
                    var4 = ((var9 & 0xFFFFFFFF) // var1)
                    if (var9 - (((var9 & 0xFFFFFFFF) // var1) * var1)):
                        break
                    if (1 if var4 >= 16384 else 0):
                        break
                    var4 = var1
                    break
                    var4 = 16384
                    var2 = (var1 + 1)
                    if (1 if (var1 + 1) == 16384 else 0):
                        break
                    var19 = ((var9 & 0xFFFFFFFF) // var2)
                    if (1 if var9 == (((var9 & 0xFFFFFFFF) // var2) * var2) else 0):
                        var4 = var2
                        if (1 if var19 < 16384 else 0):
                            break
                    var1 = (var1 + 2)
                    continue
                    break  # end loop
                raise RuntimeError('unreachable')
                if var5:
                    # Unknown: memory.fill []
                var2 = (var5 + var10)
                var9 = ((var15 + 2) * var5)
                var1 = 0
                if var5:
                    while True:  # loop $label4
                        i32_store8((var7 + ((var1 + var2) + ((i32_load(var3) * i32_load(var3 + 4)) << 2))), 0)
                        i32_store8((var7 + ((var2 + (var1 | 1)) + ((i32_load(var3) * i32_load(var3 + 4)) << 2))), 0)
                        var1 = (var1 + 2)
                        if (1 if (var1 + 2) != var5 else 0):
                            continue
                        break  # end loop
                var10 = (var9 + var10)
                var14 = (var14 + 1)
                if (1 if (var14 + 1) != var11 else 0):
                    continue
                break  # end loop
        i32_store(var6 + 12, var13)
        i32_store(var6 + 8, var7)
        i32_store(var6 + 4, var12)
        i32_store(var6, var8)
        if var12:
            break
        break
    var15 = i32_load(9684260)
    if i32_load(9684260):
        break
    if (1 if i32_load8_u(9142918) == 0 else 0):
        break
    if var11:
        while True:  # loop $label18
            var3 = i32_load((var16 + (var14 << 2)))
            var4 = i32_load(i32_load((var16 + (var14 << 2))) + 4)
            var1 = i32_load(var3)
            var7 = (i32_load(i32_load((var16 + (var14 << 2))) + 4) * i32_load(var3))
            var10 = (var3 + i32_load(var3 + 36))
            var2 = 1
            if ((1 if var4 < 16384 else 0) & (1 if var1 <= 16383 else 0)):
                break
            while True:  # loop $label11
                var1 = ((var7 & 0xFFFFFFFF) // var2)
                if (var7 - (((var7 & 0xFFFFFFFF) // var2) * var2)):
                    break
                if (1 if var1 >= 16384 else 0):
                    break
                var1 = var2
                break
                var1 = 16384
                var4 = (var2 + 1)
                if (1 if (var2 + 1) == 16384 else 0):
                    break
                var5 = ((var7 & 0xFFFFFFFF) // var4)
                if (1 if var7 == (((var7 & 0xFFFFFFFF) // var4) * var4) else 0):
                    var1 = var4
                    if (1 if var5 < 16384 else 0):
                        break
                var2 = (var2 + 2)
                continue
                break  # end loop
            raise RuntimeError('unreachable')
            var13 = (i32_load(9684256) & 511)
            i32_store(9684256, ((i32_load(9684256) & 511) + 1))
            var9 = (var7 << 2)
            var5 = func26((var7 << 2))
            i32_store(((var13 << 2) + 9682208), func26((var7 << 2)))
            var10 = i32_load(var3 + 32)
            # br_table ['$label12', '$label13', '$label12', '$label13']
            _br_idx = (i32_load(var3 + 32) - 23)
            break  # br_table
            var8 = 0
            var4 = 0
            var12 = 0
            var1 = 0
            var2 = 0
            if (1 if var7 == 0 else 0):
                break
            while True:  # loop $label15
                if i32_load8_u((var5 + (var2 | 3))):
                    var8 = (var8 + i32_load8_u((var2 + var5)))
                    var12 = (var12 + i32_load8_u((var5 + (var2 | 2))))
                    var4 = (var4 + i32_load8_u((var5 + (var2 | 1))))
                    var1 = (var1 + 1)
                var2 = (var2 + 4)
                if (1 if var9 > (var2 + 4) else 0):
                    continue
                break  # end loop
            break
            var8 = 0
            if (1 if var10 != 27 else 0):
                break
            if (1 if i32_load8_u(9142916) == 0 else 0):
                break
            var2 = 0
            if (1 if var7 == 0 else 0):
                break
            while True:  # loop $label17
                i32_store8((var5 + (var2 | 3)), (((i32_load8_u((var5 + (var2 | 2))) + (i32_load8_u((var5 + (var2 | 1))) + i32_load8_u((var2 + var5)))) & 0xFFFFFFFF) // 3))
                var2 = (var2 + 4)
                if (1 if (var2 + 4) < var9 else 0):
                    continue
                break  # end loop
            var10 = i32_load(var3 + 32)
            break
            var8 = ((((var8 & 0xFFFFFFFF) // var1) + (((var4 & 0xFFFFFFFF) // var1) << 8)) + (((var12 & 0xFFFFFFFF) // var1) << 16))
            var1 = i32_load((var3 + (48 if i32_load8_u(9142918) else 56)))
            var4 = i32_load(var3 + 16)
            var20 = i64_load(var3)
            var2 = i32_load(var3 + 28)
            var21 = i64_load(var3 + 8)
            i64_store(var6 + 32, i64_load(var3 + 20))
            i64_store(var6 + 40, var21)
            i32_store(var6 + 48, var10)
            i32_store(var6 + 52, var8)
            i32_store(var6 + 56, var1)
            i32_store(var6 + 60, var2)
            i32_store((var6 - -64), var13)
            i32_store(var6 + 16, var5)
            i64_store(var6 + 20, var20)
            i32_store(var6 + 28, var4)
            a_b()
            i32_store(9684260, (i32_load(9684260) + var9))
            var14 = (var14 + 1)
            if (1 if (var14 + 1) != var11 else 0):
                continue
            break  # end loop
    if var15:
        break
    a_b()
    global global0
    global0 = (var6 + 80)
    var1 = i32_load(var0 + 12)
    if i32_load(var0 + 12):
    hf(af(var1), af(var0), 0)
    a_l()
    raise RuntimeError('unreachable')
    return 0


# ==========================================================
# $Vb
# Export: Vb
# ==========================================================
def Vb(var0, var1, var2):
    """Export: Vb"""
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var4 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if i32_load8_u(9147210) == 0 else 0):
        func176(var2, i32_load(9142872), (1 if var1 == 0 else 0))
        break
    if (1 if var1 == 0 else 0):
        break
    if (1 if i32_load(9147132) == 0 else 0):
        break
    if (1 if i32_load(9142440) != 4096 else 0):
        break
    var5 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var2 = 1
    var6 = (var5 - 1)
    var10 = ((var5 - 1) & 1)
    var7 = i32_load((i32_load(9561692) + (i32_load(9142872) * 286704)) + 283908)
    var8 = (i32_load((i32_load(9561692) + (i32_load(9142872) * 286704)) + 283908) * var5)
    var9 = i32_load(9143004)
    if (1 if var5 != 2 else 0):
        var6 = (var6 & -2)
        var5 = 0
        while True:  # loop $label2
            var3 = (var2 + 1)
            var3 = ((var3 + ((1 if i32_load8_u((var9 + (var2 + var8))) == 0 else 0) & (1 if var2 != var7 else 0))) + ((1 if i32_load8_u((var9 + ((var2 + 1) + var8))) == 0 else 0) & (1 if var3 != var7 else 0)))
            var2 = (var2 + 2)
            var5 = (var5 + 2)
            if (1 if (var5 + 2) != var6 else 0):
                continue
            break  # end loop
    if var10:
    else:
    if (1 if var3 < 3 else 0):
        break
    a_b()
    i64_store(var4, 12884902817)
    a_b()
    break
    i32_store(var4 + 12, var1)
    i32_store(var4 + 8, var0)
    func41(45, 0, 0, (var4 + 8), 2)
    global global0
    global0 = (var4 + 16)
    return var4

