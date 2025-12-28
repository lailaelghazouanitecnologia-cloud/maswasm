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
# $func174
# ==========================================================
def func174(var0, var1, var2):
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
    var3 = i32_load(var0)
    if (1 if i32_load(var0) == -1 else 0):
        var12 = 2
        var13 = i32_load(var0 + 4)
        var3 = i32_load(var0 + 8)
    var4 = i32_load(9142440)
    var5 = (i32_load(9142440) - 1)
    var6 = (var12 << 2)
    var16 = i32_load((var0 + ((var12 << 2) | 4)))
    var17 = (1 if i32_load((var0 + ((var12 << 2) | 4))) < var4 else 0)
    var6 = (var0 + var6)
    var18 = i32_load((var0 + var6) + 8)
    var21 = i32_load(9671136)
    var11 = (1 if i32_load((var0 + var6) + 8) > i32_load(9671136) else 0)
    var7 = (var12 | 5)
    var10 = i32_load(var6 + 12)
    if (1 if i32_load(var6 + 12) == 69 else 0):
        i32_store((var0 + (var7 << 2)), 1)
    var16 = (var16 if var17 else var5)
    var17 = (var3 if (1 if var3 < var4 else 0) else var5)
    var19 = i32_load(var6 + 16)
    var20 = i32_load((var0 + (var7 << 2)))
    var3 = ((var11 | (1 if i32_load((var0 + (var7 << 2))) != 0 else 0)) & (1 if var10 != 40 else 0))
    var8 = (5 if ((var11 | (1 if i32_load((var0 + (var7 << 2))) != 0 else 0)) & (1 if var10 != 40 else 0)) else 0)
    var9 = i32_load(var6 + 24)
    if var2:
        var14 = (1 if var3 else (1 if var11 else var13))
        var22 = (-1 if (1 if var14 > 1073741823 else 0) else ((1 if var3 else (1 if var11 else var13)) << 2))
        var6 = (var14 * 7)
        var23 = (1 if (1 if var6 <= 1 else 0) else (var14 * 7))
        var24 = (2 if var11 else 1)
        var13 = 0
        while True:  # loop $label16
            var7 = (i32_load(9671128) + (i32_load((var1 + (var13 << 2))) * 132))
            if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load((var1 + (var13 << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 1 else 0):
                break
            if (1 if var18 <= var21 else 0):
                break
            if (1 if var17 != i32_load16_u(var7 + 112) else 0):
                break
            if (1 if var16 == i32_load16_u(var7 + 114) else 0):
                break
            if (1 if i32_load((i32_load(9215884) + (i32_load(var7 + 44) << 4)) + 4) == 20 else 0):
                break
            if (1 if (i32_load8_u(var7 + 125) & -2) == 12 else 0):
                break
            var3 = i32_load(var7 + 20)
            if var14:
                if (1 if var3 == 0 else 0):
                    var3 = func26(16)
                    i32_store(func26(16) + 4, var14)
                    var6 = func26(var22)
                    i32_store(var3 + 12, 1)
                    i32_store(var3, var6)
                    i32_store(var7 + 20, var3)
                    i32_store(var3 + 8, 0)
                    var6 = (var3 + 8)
                    break
                i32_store(var3 + 8, 0)
                var6 = (var3 + 8)
                if (1 if i32_load(var3 + 4) == 0 else 0):
                    break
                var5 = i32_load(var3)
                var4 = 0
                break
                var5 = i32_load(var3 + 12)
                i32_store(var3 + 4, i32_load(var3 + 12))
                var4 = i32_load(var3)
                var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
                if var4:
                else:
                var4 = 0
                i32_store(var3, var5)
                var3 = i32_load(var7 + 20)
                i32_store(var6, (var4 + 1))
                i32_store((var5 + (var4 << 2)), var24)
                var4 = i32_load(var3 + 8)
                if (1 if i32_load(var3 + 8) != i32_load(var3 + 4) else 0):
                    var5 = i32_load(var3)
                    break
                var5 = (i32_load(var3 + 12) + var4)
                i32_store(var3 + 4, (i32_load(var3 + 12) + var4))
                var6 = i32_load(var3)
                var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
                if var4:
                    # Unknown: memory.copy []
                if var6:
                    var4 = i32_load(var3 + 8)
                i32_store(var3, var5)
                i32_store(var3 + 8, (var4 + 1))
                i32_store((var5 + (var4 << 2)), 2)
                var5 = 0
                while True:  # loop $label7
                    var25 = i32_load((var0 + ((var5 + var12) << 2)))
                    var4 = i32_load(var7 + 20)
                    var3 = i32_load(i32_load(var7 + 20) + 8)
                    if (1 if i32_load(i32_load(var7 + 20) + 8) != i32_load(var4 + 4) else 0):
                        var6 = i32_load(var4)
                        break
                    var6 = (i32_load(var4 + 12) + var3)
                    i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                    var15 = i32_load(var4)
                    var6 = func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2)))
                    if var3:
                        # Unknown: memory.copy []
                    if var15:
                        var3 = i32_load(var4 + 8)
                    i32_store(var4, var6)
                    i32_store(var4 + 8, (var3 + 1))
                    i32_store((var6 + (var3 << 2)), var25)
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var23 else 0):
                        continue
                    break  # end loop
                var4 = i32_load(var7 + 20)
                var3 = i32_load(i32_load(var7 + 20))
                i32_store(i32_load(i32_load(var7 + 20)) + 28, var8)
                if (1 if var11 == 0 else 0):
                    break
                i32_store(var3 + 16, 0)
                var15 = i32_load16_u(var7 + 112)
                var5 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var6 = var3
                    break
                var6 = (i32_load(var4 + 12) + var5)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var5))
                var6 = func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2)))
                if var5:
                    # Unknown: memory.copy []
                i32_store(var4, var6)
                var5 = i32_load(var4 + 8)
                var3 = i32_load(var7 + 20)
                i32_store(var4 + 8, (var5 + 1))
                i32_store((var6 + (var5 << 2)), var15)
                var15 = i32_load16_u(var7 + 114)
                var5 = i32_load(var3 + 8)
                if (1 if i32_load(var3 + 8) != i32_load(var3 + 4) else 0):
                    var6 = i32_load(var3)
                    break
                var6 = (i32_load(var3 + 12) + var5)
                i32_store(var3 + 4, (i32_load(var3 + 12) + var5))
                var4 = i32_load(var3)
                var6 = func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2)))
                if var5:
                    # Unknown: memory.copy []
                if var4:
                    var5 = i32_load(var3 + 8)
                i32_store(var3, var6)
                var4 = i32_load(var7 + 20)
                i32_store(var3 + 8, (var5 + 1))
                i32_store((var6 + (var5 << 2)), var15)
                var5 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var6 = i32_load(var4)
                    break
                var6 = (i32_load(var4 + 12) + var5)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var5))
                var3 = i32_load(var4)
                var6 = func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2)))
                if var5:
                    # Unknown: memory.copy []
                if var3:
                    var5 = i32_load(var4 + 8)
                i32_store(var4, var6)
                var3 = i32_load(var7 + 20)
                i32_store(var4 + 8, (var5 + 1))
                i32_store((var6 + (var5 << 2)), 0)
                var5 = i32_load(var3 + 8)
                if (1 if i32_load(var3 + 8) != i32_load(var3 + 4) else 0):
                    var6 = i32_load(var3)
                    break
                var6 = (i32_load(var3 + 12) + var5)
                i32_store(var3 + 4, (i32_load(var3 + 12) + var5))
                var4 = i32_load(var3)
                var6 = func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2)))
                if var5:
                    # Unknown: memory.copy []
                if var4:
                    var5 = i32_load(var3 + 8)
                i32_store(var3, var6)
                var4 = i32_load(var7 + 20)
                i32_store(var3 + 8, (var5 + 1))
                i32_store((var6 + (var5 << 2)), 0)
                var5 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var6 = i32_load(var4)
                    break
                var6 = (i32_load(var4 + 12) + var5)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var5))
                var3 = i32_load(var4)
                var6 = func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2)))
                if var5:
                    # Unknown: memory.copy []
                if var3:
                    var5 = i32_load(var4 + 8)
                i32_store(var4, var6)
                var3 = i32_load(var7 + 20)
                i32_store(var4 + 8, (var5 + 1))
                i32_store((var6 + (var5 << 2)), 0)
                var5 = i32_load(var3 + 8)
                if (1 if i32_load(var3 + 8) != i32_load(var3 + 4) else 0):
                    var6 = i32_load(var3)
                    break
                var6 = (i32_load(var3 + 12) + var5)
                i32_store(var3 + 4, (i32_load(var3 + 12) + var5))
                var4 = i32_load(var3)
                var6 = func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2)))
                if var5:
                    # Unknown: memory.copy []
                if var4:
                    var5 = i32_load(var3 + 8)
                i32_store(var3, var6)
                var4 = i32_load(var7 + 20)
                i32_store(var3 + 8, (var5 + 1))
                i32_store((var6 + (var5 << 2)), 5)
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var5 = i32_load(var4)
                    break
                var5 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var6 = i32_load(var4)
                var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
                if var3:
                    # Unknown: memory.copy []
                if var6:
                    var3 = i32_load(var4 + 8)
                i32_store(var4, var5)
                i32_store(var4 + 8, (var3 + 1))
                break
            if (1 if var3 == 0 else 0):
                break
            i32_store((var3 + 8), 0)
            var13 = (var13 + 1)
            if (1 if (var13 + 1) != var2 else 0):
                continue
            break  # end loop
    var7 = (0 if var11 else var18)
    var12 = (((9 if (1 if var10 == 6 else 0) else var8) if (0 if var11 else var18) else var8) if var9 else var8)
    if (1 if var20 == 0 else 0):
        break
    if (1 if var7 == 0 else 0):
        break
    if ((1 if var10 != 62 else 0) & (1 if var10 != 40 else 0)):
        break
    var12 = 14
    if (1 if var20 == 0 else 0):
        break
    if (1 if var9 == 0 else 0):
        break
    if (1 if var7 == 0 else 0):
        break
    if ((1 if var10 != 62 else 0) & (1 if var10 != 40 else 0)):
        break
    var12 = 15
    break
    var6 = var16
    if (1 if var7 == 0 else 0):
        break
    var0 = (i32_load(9671128) + (var7 * 132))
    var6 = i32_load16_u((i32_load(9671128) + (var7 * 132)) + 114)
    var13 = i32_load16_u(var0 + 112)
    if (1 if var9 == 0 else 0):
        break
    if (1 if var10 == 6 else 0):
        break
    if (1 if var12 != 15 else 0):
        break
    if (1 if var2 == 0 else 0):
        break
    # Unknown: memory.fill []
    var0 = 0
    while True:  # loop $label25
        var11 = i32_load(9671128)
        var3 = 2147483647
        var4 = 0
        while True:  # loop $label24
            if (1 if i32_load8_u((var4 + 9163808)) == 0 else 0):
                var8 = (var11 + (i32_load((var1 + (var4 << 2))) * 132))
                var14 = (i32_load16_u((var11 + (i32_load((var1 + (var4 << 2))) * 132)) + 114) - var6)
                var8 = (i32_load16_u(var8 + 112) - var13)
                var8 = (((i32_load16_u((var11 + (i32_load((var1 + (var4 << 2))) * 132)) + 114) - var6) * var14) + ((i32_load16_u(var8 + 112) - var13) * var8))
                var8 = (1 if var3 > var8 else 0)
                var3 = ((((i32_load16_u((var11 + (i32_load((var1 + (var4 << 2))) * 132)) + 114) - var6) * var14) + ((i32_load16_u(var8 + 112) - var13) * var8)) if (1 if var3 > var8 else 0) else var3)
                var5 = (var4 if var8 else var5)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var2 else 0):
                continue
            break  # end loop
        i32_store8((var5 + 9163808), 1)
        var3 = (var11 + (i32_load((var1 + (var5 << 2))) * 132))
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var2 else 0):
            continue
        break  # end loop
    break
    if (1 if var2 == 0 else 0):
        break
    var11 = ((var10 * 40) + 9671208)
    var4 = 0
    var8 = i32_load(9561692)
    var14 = i32_load(9671128)
    var5 = 2147483647
    var3 = 0
    while True:  # loop $label27
        var0 = (var14 + (i32_load((var1 + (var4 << 2))) * 132))
        if (1 if var10 == i32_load8_u((var14 + (i32_load((var1 + (var4 << 2))) * 132)) + 123) else 0):
            break
        var9 = i32_load(var11)
        if i32_load(var11):
            if (1 if i32_load((((var8 + (i32_load16_u(var0 + 110) * 286704)) + (var9 << 2)) + 283984)) > i32_load(var0 + 72) else 0):
                break
        var9 = (i32_load16_u(var0 + 114) - var6)
        var9 = (i32_load16_u(var0 + 112) - var13)
        var9 = (((i32_load16_u(var0 + 114) - var6) * var9) + ((i32_load16_u(var0 + 112) - var13) * var9))
        var9 = (1 if var5 > var9 else 0)
        var5 = ((((i32_load16_u(var0 + 114) - var6) * var9) + ((i32_load16_u(var0 + 112) - var13) * var9)) if (1 if var5 > var9 else 0) else var5)
        var3 = (i32_load(var0 + 28) if var9 else var3)
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var2 else 0):
            continue
        break  # end loop
    if (1 if var3 == 0 else 0):
        break
    return 9163808

