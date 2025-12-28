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
# $Fb
# Export: Fb
# ==========================================================
def Fb():
    """Export: Fb"""
    var0 = 0
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
    var5 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    i64_store(var5 + 20, 0)
    i32_store(var5 + 28, 0)
    var8 = i32_load(9687244)
    var0 = (i32_load(9687244) + i32_load(9687248))
    if (i32_load(9687244) + i32_load(9687248)):
        var3 = i32_load(var5 + 28)
        var8 = i32_load(var5 + 24)
        if (1 if var0 <= ((i32_load(var5 + 28) - i32_load(var5 + 24)) // 20) else 0):
            if var0:
                var0 = ((var0 * 20) - 20)
                var0 = ((((var0 * 20) - 20) - (var0 % 20)) + 20)
                # Unknown: memory.fill []
            else:
            i32_store((var0 + var8) + 24, var8)
            break
        var8 = i32_load(var5 + 20)
        var4 = (var8 - i32_load(var5 + 20))
        var6 = ((var8 - i32_load(var5 + 20)) // 20)
        var2 = (((var8 - i32_load(var5 + 20)) // 20) + var0)
        if (1 if (((var8 - i32_load(var5 + 20)) // 20) + var0) < 214748365 else 0):
            var3 = ((var3 - var8) // 20)
            var7 = (((var3 - var8) // 20) << 1)
            var2 = (214748364 if (1 if var3 >= 107374182 else 0) else ((((var3 - var8) // 20) << 1) if (1 if var2 < var7 else 0) else var2))
            if (214748364 if (1 if var3 >= 107374182 else 0) else ((((var3 - var8) // 20) << 1) if (1 if var2 < var7 else 0) else var2)):
                if (1 if var2 >= 214748365 else 0):
                    break
                var9 = func26((var2 * 20))
            var3 = ((var6 * 20) + var9)
            var0 = ((var0 * 20) - 20)
            var0 = ((((var0 * 20) - 20) - (var0 % 20)) + 20)
            # Unknown: memory.fill []
            var6 = (var3 + ((var4 // -20) * 20))
            # Unknown: memory.copy []
            i32_store(var5 + 28, (var9 + (var2 * 20)))
            i32_store(var5 + 24, (var0 + var3))
            i32_store(var5 + 20, var6)
            if var8:
            break
        func42()
        raise RuntimeError('unreachable')
        func68()
        raise RuntimeError('unreachable')
    else:
    if var8:
        while True:  # loop $label2
            var0 = (i32_load(9684500) + (var1 * 60))
            var23 = i64_load((i32_load(9684500) + (var1 * 60)))
            var24 = i64_load(var0 + 16)
            var8 = (i32_load(var5 + 20) + (var1 * 20))
            i32_store((i32_load(var5 + 20) + (var1 * 20)) + 16, (var0 + 48))
            i64_store(var8 + 8, var24)
            i64_store(var8, var23)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < i32_load(9687244) else 0):
                continue
            break  # end loop
    var8 = 0
    if i32_load(9687248):
        while True:  # loop $label3
            var0 = (i32_load(9684496) + (var8 * 60))
            var23 = i64_load((i32_load(9684496) + (var8 * 60)))
            var24 = i64_load(var0 + 16)
            var9 = (i32_load(var5 + 20) + (var1 * 20))
            i32_store((i32_load(var5 + 20) + (var1 * 20)) + 16, (var0 + 48))
            i64_store(var9 + 8, var24)
            i64_store(var9, var23)
            var1 = (var1 + 1)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) < i32_load(9687248) else 0):
                continue
            break  # end loop
    i32_store(var5 + 16, 0)
    i64_store(var5 + 8, 0)
    var4 = i32_load(var5 + 24)
    var3 = i32_load(var5 + 20)
    if (1 if i32_load(var5 + 24) == i32_load(var5 + 20) else 0):
        var8 = 0
        break
    var1 = 0
    var8 = 0
    var9 = 0
    while True:  # loop $label10
        var2 = (var3 + (var9 * 20))
        var0 = i32_load((var3 + (var9 * 20)) + 4)
        var6 = i32_load(var2 + 12)
        var7 = i32_load(var2 + 8)
        i32_store(i32_load(var2 + 16), var8)
        var0 = (var6 * var7)
        var6 = ((var0 & 0xFFFFFFFF) // (var6 * var7))
        if var0:
            var0 = (var0 + var8)
            while True:  # loop $label8
                var7 = (var8 * 3)
                var10 = i32_load(var2)
                var3 = i32_load(var5 + 16)
                if (1 if i32_load(var5 + 16) > var1 else 0):
                    i32_store(var1 + 24, -1)
                    i64_store(var1 + 16, -1)
                    i32_store(var1 + 12, var6)
                    i32_store(var1 + 8, var10)
                    i32_store(var1 + 4, var7)
                    i32_store(var1, var9)
                    var1 = (var1 + 28)
                    i32_store(var5 + 12, (var1 + 28))
                    break
                var4 = i32_load(var5 + 8)
                var11 = (var1 - i32_load(var5 + 8))
                var12 = ((var1 - i32_load(var5 + 8)) // 28)
                var1 = (((var1 - i32_load(var5 + 8)) // 28) + 1)
                if (1 if (((var1 - i32_load(var5 + 8)) // 28) + 1) >= 153391690 else 0):
                    break
                var3 = ((var3 - var4) // 28)
                var14 = (((var3 - var4) // 28) << 1)
                var3 = (153391689 if (1 if var3 >= 76695844 else 0) else ((((var3 - var4) // 28) << 1) if (1 if var1 < var14 else 0) else var1))
                if (153391689 if (1 if var3 >= 76695844 else 0) else ((((var3 - var4) // 28) << 1) if (1 if var1 < var14 else 0) else var1)):
                    if (1 if var3 >= 153391690 else 0):
                        break
                else:
                var14 = 0
                var1 = (0 + (var12 * 28))
                i32_store((0 + (var12 * 28)) + 24, -1)
                i64_store(var1 + 16, -1)
                i32_store(var1 + 12, var6)
                i32_store(var1 + 8, var10)
                i32_store(var1 + 4, var7)
                i32_store(var1, var9)
                var7 = (var1 + ((var11 // -28) * 28))
                # Unknown: memory.copy []
                i32_store(var5 + 16, (var14 + (var3 * 28)))
                var1 = (var1 + 28)
                i32_store(var5 + 12, (var1 + 28))
                i32_store(var5 + 8, var7)
                if (1 if var4 == 0 else 0):
                    break
                var8 = (var8 + 1)
                if (1 if var0 != (var8 + 1) else 0):
                    continue
                break
                break  # end loop
            func42()
            raise RuntimeError('unreachable')
            func68()
            raise RuntimeError('unreachable')
            var3 = i32_load(var5 + 20)
            var4 = i32_load(var5 + 24)
            var8 = var0
        var9 = (var9 + 1)
        if (1 if (var9 + 1) < ((var4 - var3) // 20) else 0):
            continue
        break  # end loop
    var14 = i32_load(var5 + 8)
    var2 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    i32_store(var2 + 24, 8192)
    i32_store(var2 + 28, 8192)
    var1 = i32_load(var5 + 8)
    var0 = i32_load(var5 + 12)
    var1 = ((i32_load(var5 + 12) - i32_load(var5 + 8)) // 28)
    var19 = func26((-1 if (1 if (var1 * 3) > 1073741823 else 0) else (((i32_load(var5 + 12) - i32_load(var5 + 8)) // 28) * 12)))
    i32_store(9687240, func26((-1 if (1 if (var1 * 3) > 1073741823 else 0) else (((i32_load(var5 + 12) - i32_load(var5 + 8)) // 28) * 12))))
    i32_store(var2 + 20, 0)
    i64_store(var2 + 12, 0)
    var9 = i32_load(var5 + 8)
    var20 = i32_load(var5 + 12)
    if (1 if i32_load(var5 + 8) != i32_load(var5 + 12) else 0):
        while True:  # loop $label28
            var7 = (i32_load(var9 + 8) + 8)
            var15 = i32_load(var2 + 28)
            if (1 if (i32_load(var9 + 8) + 8) > i32_load(var2 + 28) else 0):
                break
            var10 = (i32_load(var9 + 12) + 8)
            var17 = i32_load(var2 + 24)
            if (1 if (i32_load(var9 + 12) + 8) > i32_load(var2 + 24) else 0):
                break
            var3 = i32_load(var2 + 16)
            var18 = i32_load(var2 + 12)
            if (1 if i32_load(var2 + 16) != i32_load(var2 + 12) else 0):
                var1 = ((var3 - var18) >> 5)
                var21 = (1 if (1 if var1 <= 1 else 0) else ((var3 - var18) >> 5))
                var11 = 0
                while True:  # loop $label19
                    var1 = (var18 + (var11 << 5))
                    var0 = i32_load((var18 + (var11 << 5)) + 24)
                    var12 = i32_load(var1 + 20)
                    if (1 if i32_load((var18 + (var11 << 5)) + 24) == i32_load(var1 + 20) else 0):
                        break
                    var0 = ((var0 - var12) >> 4)
                    var22 = (1 if (1 if var0 <= 1 else 0) else ((var0 - var12) >> 4))
                    var6 = 2147483647
                    var0 = 0
                    var4 = -1
                    while True:  # loop $label14
                        var13 = (var12 + (var0 << 4))
                        var16 = i32_load((var12 + (var0 << 4)) + 8)
                        if (1 if i32_load((var12 + (var0 << 4)) + 8) < var7 else 0):
                            break
                        var13 = i32_load(var13 + 12)
                        if (1 if i32_load(var13 + 12) < var10 else 0):
                            break
                        var13 = (var13 - var10)
                        var16 = (var16 - var7)
                        var13 = ((var13 - var10) if (1 if var13 < var16 else 0) else (var16 - var7))
                        var13 = (1 if var6 > var13 else 0)
                        var6 = (((var13 - var10) if (1 if var13 < var16 else 0) else (var16 - var7)) if (1 if var6 > var13 else 0) else var6)
                        var4 = (var0 if var13 else var4)
                        var0 = (var0 + 1)
                        if (1 if (var0 + 1) != var22 else 0):
                            continue
                        break  # end loop
                    if (1 if var4 == -1 else 0):
                        break
                    var0 = (var12 + (var4 << 4))
                    i32_store(var2 + 32, i32_load((var12 + (var4 << 4))))
                    var3 = i32_load(var0 + 4)
                    i32_store(var2 + 44, var10)
                    i32_store(var2 + 40, var7)
                    i32_store(var2 + 36, var3)
                    i64_store(var2 + 56, i64_load(var0 + 8))
                    i64_store(var2 + 48, i64_load(var0))
                    var3 = i32_load(var1 + 24)
                    if (1 if var4 != (((i32_load(var1 + 24) - var12) >> 4) - 1) else 0):
                        var4 = (var3 - 16)
                        i64_store(var0, i64_load((var3 - 16)))
                        i64_store(var0 + 8, i64_load(var4 + 8))
                    else:
                    i32_store(i32_load(var1 + 24) + 24, (var3 - 16))
                    var0 = i32_load(var1 + 12)
                    if (1 if i32_load(var1 + 12) != i32_load(var1 + 16) else 0):
                        i64_store(var0, i64_load(var2 + 32))
                        i64_store(var0 + 8, i64_load(var2 + 40))
                        i32_store(var1 + 12, (var0 + 16))
                        break
                    var0 = i32_load(var1 + 8)
                    var4 = (var0 - i32_load(var1 + 8))
                    var7 = ((var0 - i32_load(var1 + 8)) >> 4)
                    var3 = (((var0 - i32_load(var1 + 8)) >> 4) + 1)
                    if (1 if (((var0 - i32_load(var1 + 8)) >> 4) + 1) >= 268435456 else 0):
                        break
                    var6 = (var4 >> 3)
                    var3 = (268435455 if (1 if var4 >= 2147483632 else 0) else ((var4 >> 3) if (1 if var3 < var6 else 0) else var3))
                    if (268435455 if (1 if var4 >= 2147483632 else 0) else ((var4 >> 3) if (1 if var3 < var6 else 0) else var3)):
                        if (1 if var3 >= 268435456 else 0):
                            break
                    else:
                    var6 = 0
                    var7 = (0 + (var7 << 4))
                    i64_store((0 + (var7 << 4)), i64_load(var2 + 32))
                    i64_store(var7 + 8, i64_load(var2 + 40))
                    # Unknown: memory.copy []
                    i32_store(var1 + 8, var6)
                    i32_store(var1 + 12, (var7 + 16))
                    i32_store(var1 + 16, (var6 + (var3 << 4)))
                    if (1 if var0 == 0 else 0):
                        break
                    var1 = i32_load(var2 + 32)
                    var0 = (i32_load(var2 + 36) + 4)
                    i32_store(var9 + 20, (i32_load(var2 + 36) + 4))
                    var1 = (var1 + 4)
                    i32_store(var9 + 16, (var1 + 4))
                    break
                    var11 = (var11 + 1)
                    if (1 if (var11 + 1) != var21 else 0):
                        continue
                    break  # end loop
            if (1 if i32_load(var2 + 20) > var3 else 0):
                i64_store(var3 + 8, 0)
                i32_store(var3 + 4, var17)
                i32_store(var3, var15)
                i64_store(var3 + 16, 0)
                i64_store(var3 + 24, 0)
                var1 = func26(16)
                i32_store(func26(16) + 12, var17)
                i32_store(var1 + 8, var15)
                i64_store(var1, 0)
                var0 = (var1 + 16)
                i32_store(var3 + 28, (var1 + 16))
                i32_store(var3 + 24, var0)
                i32_store(var3 + 20, var1)
                var0 = (var3 + 32)
                i32_store(var2 + 16, (var3 + 32))
                break
            var0 = i32_load(var2 + 16)
            var1 = (var0 - 32)
            var0 = i32_load((var0 - 32) + 24)
            var3 = i32_load(var1 + 20)
            if (1 if i32_load((var0 - 32) + 24) == i32_load(var1 + 20) else 0):
                break
            var0 = ((var0 - var3) >> 4)
            var11 = (1 if (1 if var0 <= 1 else 0) else ((var0 - var3) >> 4))
            var6 = 2147483647
            var0 = 0
            var4 = -1
            while True:  # loop $label22
                var12 = (var3 + (var0 << 4))
                var15 = i32_load((var3 + (var0 << 4)) + 8)
                if (1 if i32_load((var3 + (var0 << 4)) + 8) < var7 else 0):
                    break
                var12 = i32_load(var12 + 12)
                if (1 if i32_load(var12 + 12) < var10 else 0):
                    break
                var12 = (var12 - var10)
                var15 = (var15 - var7)
                var12 = ((var12 - var10) if (1 if var12 < var15 else 0) else (var15 - var7))
                var12 = (1 if var6 > var12 else 0)
                var6 = (((var12 - var10) if (1 if var12 < var15 else 0) else (var15 - var7)) if (1 if var6 > var12 else 0) else var6)
                var4 = (var0 if var12 else var4)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var11 else 0):
                    continue
                break  # end loop
            if (1 if var4 == -1 else 0):
                break
            var6 = (var4 << 4)
            var0 = (var3 + (var4 << 4))
            i32_store(var2 + 48, i32_load((var3 + (var4 << 4))))
            var0 = i32_load(var0 + 4)
            i32_store(var2 + 60, var10)
            i32_store(var2 + 56, var7)
            i32_store(var2 + 52, var0)
            var0 = (var2 + 48)
            var3 = (global0 - 16)
            global global0
            global0 = (global0 - 16)
            var10 = i32_load(var1 + 20)
            var6 = (var6 + i32_load(var1 + 20))
            i64_store(var3 + 8, i64_load((var6 + i32_load(var1 + 20)) + 8))
            i64_store(var3, i64_load(var6))
            var7 = i32_load(var1 + 24)
            if (1 if var4 != (((i32_load(var1 + 24) - var10) >> 4) - 1) else 0):
                var4 = (var7 - 16)
                i64_store(var6, i64_load((var7 - 16)))
                i64_store(var6 + 8, i64_load(var4 + 8))
            else:
            i32_store(i32_load(var1 + 24) + 24, (var7 - 16))
            var4 = i32_load(var1 + 12)
            if (1 if i32_load(var1 + 12) != i32_load(var1 + 16) else 0):
                i64_store(var4, i64_load(var0))
                i64_store(var4 + 8, i64_load(var0 + 8))
                i32_store(var1 + 12, (var4 + 16))
                break
            var4 = i32_load(var1 + 8)
            var6 = (var4 - i32_load(var1 + 8))
            var11 = ((var4 - i32_load(var1 + 8)) >> 4)
            var7 = (((var4 - i32_load(var1 + 8)) >> 4) + 1)
            if (1 if (((var4 - i32_load(var1 + 8)) >> 4) + 1) >= 268435456 else 0):
                break
            var10 = (var6 >> 3)
            var7 = (268435455 if (1 if var6 >= 2147483632 else 0) else ((var6 >> 3) if (1 if var7 < var10 else 0) else var7))
            if (268435455 if (1 if var6 >= 2147483632 else 0) else ((var6 >> 3) if (1 if var7 < var10 else 0) else var7)):
                if (1 if var7 >= 268435456 else 0):
                    break
            else:
            var10 = 0
            var11 = (0 + (var11 << 4))
            i64_store((0 + (var11 << 4)), i64_load(var0))
            i64_store(var11 + 8, i64_load(var0 + 8))
            # Unknown: memory.copy []
            i32_store(var1 + 16, (var10 + (var7 << 4)))
            i32_store(var1 + 12, (var11 + 16))
            i32_store(var1 + 8, var10)
            if (1 if var4 == 0 else 0):
                break
            global global0
            global0 = (var3 + 16)
            break
            func42()
            raise RuntimeError('unreachable')
            func68()
            raise RuntimeError('unreachable')
            var1 = i32_load(var2 + 48)
            var0 = (i32_load(var2 + 52) + 4)
            i32_store(var9 + 20, (i32_load(var2 + 52) + 4))
            var1 = (var1 + 4)
            i32_store(var9 + 16, (var1 + 4))
            var11 = (((i32_load(var2 + 16) - i32_load(var2 + 12)) >> 5) - 1)
            i32_store(var9 + 24, var11)
            var4 = (i32_load(var9 + 4) << 2)
            var3 = (var19 + (i32_load(var9 + 4) << 2))
            f32_store((var19 + (i32_load(var9 + 4) << 2)), float(var1))
            f32_store(var3 + 4, float(var0))
            i32_store((var4 + i32_load(9687240)) + 8, var11)
            break
            func42()
            raise RuntimeError('unreachable')
            func68()
            raise RuntimeError('unreachable')
            i64_store(var9 + 16, -1)
            i32_store(var9 + 24, -1)
            var9 = (var9 + 28)
            if (1 if (var9 + 28) != var20 else 0):
                continue
            break  # end loop
    var9 = i32_load(var2 + 12)
    if i32_load(var2 + 12):
        var0 = i32_load(var2 + 16)
        var1 = var9
        if (1 if i32_load(var2 + 16) != var9 else 0):
            while True:  # loop $label29
                var1 = (var0 - 32)
                var4 = i32_load((var0 - 32) + 20)
                if i32_load((var0 - 32) + 20):
                    i32_store((var0 - 8), var4)
                var4 = i32_load((var0 - 24))
                if i32_load((var0 - 24)):
                    i32_store((var0 - 20), var4)
                var0 = var1
                if (1 if var1 != var9 else 0):
                    continue
                break  # end loop
            var1 = i32_load(var2 + 12)
        i32_store(var2 + 16, var9)
    global global0
    global0 = (var2 - -64)
    i32_store(var5 + 4, (var8 * 3))
    i32_store(var5, i32_load(9687240))
    if var14:
    var1 = i32_load(var5 + 20)
    if i32_load(var5 + 20):
        i32_store(var5 + 24, var1)
    global global0
    global0 = (var5 + 32)
    return af(var1)

