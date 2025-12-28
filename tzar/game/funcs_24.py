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
# $func365
# ==========================================================
def func365(var0, var1, var2, var3, var4, var5, var6, var7, var8):
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
    var9 = (var8 << 2)
    var10 = i32_load(((var8 << 2) + 9344))
    var14 = i32_load((var9 + 9264))
    var11 = i32_load(9142440)
    if (((28728 & 0xFFFFFFFF) >> var8) & 1):
        var8 = ((var14 * 5) + var2)
        if (1 if (((var14 * 5) + var2) if (1 if var2 > var8 else 0) else var2) > var0 else 0):
            break
        if (1 if (var2 if (1 if var2 > var8 else 0) else var8) < var0 else 0):
            break
        var8 = (var1 - var3)
        break
        var9 = (var1 - var3)
        var9 = ((var1 - var3) * var9)
        var8 = (var0 - var8)
        var8 = (((var1 - var3) * var9) + ((var0 - var8) * var8))
        var12 = (var0 - var2)
        var9 = (var9 + ((var0 - var2) * var12))
        break
    if (1 if (((74898 & 0xFFFFFFFF) >> var8) & 1) == 0 else 0):
        break
    var8 = (var0 - var2)
    var8 = ((var0 - var2) * var8)
    var9 = ((var10 * 5) + var3)
    var12 = (1 if var3 > var9 else 0)
    if ((1 if var1 >= (((var10 * 5) + var3) if (1 if var3 > var9 else 0) else var3) else 0) & (1 if (var3 if var12 else var9) >= var1 else 0)):
        break
    var9 = (var1 - var9)
    var9 = (((var1 - var9) * var9) + var8)
    var8 = (var1 - var3)
    var8 = (var8 + ((var1 - var3) * var8))
    if (1 if ((((var1 - var9) * var9) + var8) if (1 if var8 > var9 else 0) else (var8 + ((var1 - var3) * var8))) == 0 else 0):
        break
    var12 = (var11 + 2)
    var15 = (((var11 + 2) * var5) + 1)
    var13 = i32_load(9142840)
    if (1 if var3 >= var11 else 0):
        break
    if (1 if var2 >= var11 else 0):
        break
    if (1 if (var2 | var3) < 0 else 0):
        break
    var8 = var2
    var9 = var3
    if (1 if i32_load((((var2 + ((var15 + var3) * var12)) << 2) + var13) + 4) == var4 else 0):
        break
    var8 = (var2 + var14)
    var9 = (var3 + var10)
    if (1 if var11 <= (var3 + var10) else 0):
        break
    if (1 if var8 >= var11 else 0):
        break
    if (1 if (var8 | var9) < 0 else 0):
        break
    if (1 if i32_load((((var8 + ((var9 + var15) * var12)) << 2) + var13) + 4) == var4 else 0):
        break
    var8 = (var8 + var14)
    var9 = (var9 + var10)
    if (1 if var11 <= (var9 + var10) else 0):
        break
    if (1 if var8 >= var11 else 0):
        break
    if (1 if (var8 | var9) < 0 else 0):
        break
    if (1 if i32_load((((var8 + ((var9 + var15) * var12)) << 2) + var13) + 4) == var4 else 0):
        break
    var8 = (var8 + var14)
    var9 = (var9 + var10)
    if (1 if var11 <= (var9 + var10) else 0):
        break
    if (1 if var8 >= var11 else 0):
        break
    if (1 if (var8 | var9) < 0 else 0):
        break
    if (1 if i32_load((((var8 + ((var9 + var15) * var12)) << 2) + var13) + 4) == var4 else 0):
        break
    var8 = (var8 + var14)
    var9 = (var9 + var10)
    if (1 if var11 <= (var9 + var10) else 0):
        break
    if (1 if var8 >= var11 else 0):
        break
    if (1 if (var8 | var9) < 0 else 0):
        break
    if (1 if i32_load((((var8 + ((var9 + var15) * var12)) << 2) + var13) + 4) == var4 else 0):
        break
    var9 = (var9 + var10)
    if (1 if var11 <= (var9 + var10) else 0):
        break
    var8 = (var8 + var14)
    if (1 if var11 <= (var8 + var14) else 0):
        break
    if (1 if (var8 | var9) < 0 else 0):
        break
    if (1 if i32_load((((var8 + ((var9 + var15) * var12)) << 2) + var13) + 4) != var4 else 0):
        break
    var2 = (var2 - var0)
    var2 = (var2 >> 31)
    var2 = (((var2 - var0) ^ (var2 >> 31)) - var2)
    var3 = (var3 - var1)
    var3 = (var3 >> 31)
    var3 = (((var3 - var1) ^ (var3 >> 31)) - var3)
    var15 = (((((var2 - var0) ^ (var2 >> 31)) - var2) if (1 if var2 > var3 else 0) else (((var3 - var1) ^ (var3 >> 31)) - var3)) << 5)
    i32_store(59200, (var8 + (var9 << 16)))
    var24 = i32_load(9142436)
    var13 = 1
    var10 = 1
    while True:  # loop $label23
        var2 = i32_load(((var25 << 2) + 59200))
        var8 = ((i32_load(((var25 << 2) + 59200)) & 0xFFFFFFFF) >> 16)
        var9 = (var2 & 65535)
        var2 = ((((i32_load(((var25 << 2) + 59200)) & 0xFFFFFFFF) >> 16) * var11) + (var2 & 65535))
        if (1 if var13 == 0 else 0):
            if (1 if i32_load16_u((var24 + (var2 << 1))) == (var14 & 65535) else 0):
                break
        var20 = i32_load(9142436)
        var21 = (i32_load(9142436) + (var2 << 1))
        var17 = i32_load(9142440)
        var19 = (i32_load(9142440) + 2)
        var22 = ((i32_load(9142440) + 2) * var5)
        var18 = (((i32_load(9142440) + 2) * var5) + 1)
        var23 = i32_load(9671128)
        var12 = i32_load(9142840)
        while True:  # loop $label22
            var2 = (var1 - var8)
            var3 = (var0 - var9)
            if (1 if (var0 - var9) == 0 else 0):
                break
            if (1 if var1 == var8 else 0):
                break
            var3 = (var2 // var3)
            var3 = (var3 >> 31)
            var3 = (var3 if (1 if (((var2 // var3) ^ (var3 >> 31)) - var3) <= 1 else 0) else 0)
            var2 = ((var3 if (1 if (((var2 // var3) ^ (var3 >> 31)) - var3) <= 1 else 0) else 0) // var2)
            var2 = (var2 >> 31)
            var2 = (var2 if (1 if ((((var3 if (1 if (((var2 // var3) ^ (var3 >> 31)) - var3) <= 1 else 0) else 0) // var2) ^ (var2 >> 31)) - var2) <= 1 else 0) else 0)
            var16 = (-1 if (1 if var2 < 0 else 0) else (1 if var2 != 0 else 0))
            var2 = ((-1 if (1 if var2 < 0 else 0) else (1 if var2 != 0 else 0)) + var8)
            var26 = (-1 if (1 if var3 < 0 else 0) else (1 if var3 != 0 else 0))
            var3 = ((-1 if (1 if var3 < 0 else 0) else (1 if var3 != 0 else 0)) + var9)
            if (1 if ((-1 if (1 if var3 < 0 else 0) else (1 if var3 != 0 else 0)) + var9) != var0 else 0):
                break
            if (1 if var1 != var2 else 0):
                break
            i32_store(var6, (0 - var26))
            i32_store(var7, (0 - var16))
            return 1
            if (1 if var13 == 0 else 0):
                i32_store16((var20 + (((var2 * var11) + var3) << 1)), var14)
            var16 = i32_load((((var3 + (var19 * (var2 + var18))) << 2) + var12) + 4)
            if (1 if i32_load((((var3 + (var19 * (var2 + var18))) << 2) + var12) + 4) == var4 else 0):
                break
            if (1 if var16 != -1 else 0):
                if (1 if i32_load8_u((var23 + (var16 * 132)) + 125) == 1 else 0):
                    break
            if (1 if var13 == 0 else 0):
                var2 = (var9 + 1)
                var3 = i32_load(9142436)
                var13 = i32_load(9671128)
                var20 = (var9 + 2)
                var23 = ((var8 + var18) * var19)
                var17 = i32_load((var12 + (((var9 + 2) + ((var8 + var18) * var19)) << 2)))
                if (1 if var4 != i32_load((var12 + (((var9 + 2) + ((var8 + var18) * var19)) << 2))) else 0):
                    if (1 if var17 == -1 else 0):
                        break
                    if (1 if i32_load8_u((var13 + (var17 * 132)) + 125) != 1 else 0):
                        break
                if (1 if i32_load16_u((var3 + (((var8 * var11) + var2) << 1))) == (var14 & 65535) else 0):
                    break
                i32_store(((var10 << 2) + 59200), ((var8 << 16) + var2))
                var10 = (var10 + 1)
                if (1 if (var10 + 1) <= var15 else 0):
                    break
                break
            var2 = i32_load16_u(40596)
            var3 = (i32_load16_u(40596) + 2)
            i32_store16(40596, (i32_load16_u(40596) + 2))
            if (1 if (var3 & 65535) < 65534 else 0):
                break
            i32_store16(40596, 1)
            var3 = (var17 * var17)
            if (1 if (var17 * var17) == 0 else 0):
                break
            # Unknown: memory.fill []
            var14 = (var2 + 1)
            i32_store(((var10 << 2) + 59200), ((var8 << 16) + var9))
            var10 = (var10 + 1)
            break
            var17 = (var8 - 1)
            var21 = ((var8 + var22) * var19)
            var16 = i32_load((var12 + ((var2 + ((var8 + var22) * var19)) << 2)))
            if (1 if var4 != i32_load((var12 + ((var2 + ((var8 + var22) * var19)) << 2))) else 0):
                if (1 if var16 == -1 else 0):
                    break
                if (1 if i32_load8_u((var13 + (var16 * 132)) + 125) != 1 else 0):
                    break
            if (1 if i32_load16_u((var3 + (((var11 * var17) + var9) << 1))) == (var14 & 65535) else 0):
                break
            i32_store(((var10 << 2) + 59200), ((var17 << 16) + var9))
            var10 = (var10 + 1)
            if (1 if (var10 + 1) <= var15 else 0):
                break
            break
            var16 = (var9 - 1)
            var22 = i32_load((var12 + ((var9 + var23) << 2)))
            if (1 if var4 != i32_load((var12 + ((var9 + var23) << 2))) else 0):
                if (1 if var22 == -1 else 0):
                    break
                if (1 if i32_load8_u((var13 + (var22 * 132)) + 125) != 1 else 0):
                    break
            if (1 if i32_load16_u((var3 + (((var8 * var11) + var16) << 1))) == (var14 & 65535) else 0):
                break
            i32_store(((var10 << 2) + 59200), ((var8 << 16) + var16))
            var10 = (var10 + 1)
            if (1 if (var10 + 1) <= var15 else 0):
                break
            break
            var8 = (var8 + 1)
            var19 = ((var18 + (var8 + 1)) * var19)
            var18 = i32_load((var12 + ((var2 + ((var18 + (var8 + 1)) * var19)) << 2)))
            if (1 if var4 != i32_load((var12 + ((var2 + ((var18 + (var8 + 1)) * var19)) << 2))) else 0):
                if (1 if var18 == -1 else 0):
                    break
                if (1 if i32_load8_u((var13 + (var18 * 132)) + 125) != 1 else 0):
                    break
            if (1 if i32_load16_u((var3 + (((var8 * var11) + var9) << 1))) == (var14 & 65535) else 0):
                break
            i32_store(((var10 << 2) + 59200), ((var8 << 16) + var9))
            var10 = (var10 + 1)
            if (1 if (var10 + 1) <= var15 else 0):
                break
            break
            var18 = i32_load((var12 + ((var20 + var21) << 2)))
            if (1 if var4 != i32_load((var12 + ((var20 + var21) << 2))) else 0):
                if (1 if var18 == -1 else 0):
                    break
                if (1 if i32_load8_u((var13 + (var18 * 132)) + 125) != 1 else 0):
                    break
            if (1 if i32_load16_u((var3 + (((var11 * var17) + var2) << 1))) == (var14 & 65535) else 0):
                break
            i32_store(((var10 << 2) + 59200), ((var17 << 16) + var2))
            var10 = (var10 + 1)
            if (1 if (var10 + 1) <= var15 else 0):
                break
            break
            var18 = i32_load((var12 + ((var9 + var21) << 2)))
            if (1 if var4 != i32_load((var12 + ((var9 + var21) << 2))) else 0):
                if (1 if var18 == -1 else 0):
                    break
                if (1 if i32_load8_u((var13 + (var18 * 132)) + 125) != 1 else 0):
                    break
            if (1 if i32_load16_u((var3 + (((var11 * var17) + var16) << 1))) == (var14 & 65535) else 0):
                break
            i32_store(((var10 << 2) + 59200), ((var17 << 16) + var16))
            var10 = (var10 + 1)
            if (1 if (var10 + 1) <= var15 else 0):
                break
            break
            var9 = i32_load((var12 + ((var9 + var19) << 2)))
            if (1 if var4 != i32_load((var12 + ((var9 + var19) << 2))) else 0):
                if (1 if var9 == -1 else 0):
                    break
                if (1 if i32_load8_u((var13 + (var9 * 132)) + 125) != 1 else 0):
                    break
            if (1 if i32_load16_u((var3 + (((var8 * var11) + var16) << 1))) == (var14 & 65535) else 0):
                break
            i32_store(((var10 << 2) + 59200), ((var8 << 16) + var16))
            var10 = (var10 + 1)
            if (1 if (var10 + 1) <= var15 else 0):
                break
            break
            var9 = i32_load((var12 + ((var19 + var20) << 2)))
            if (1 if var4 != i32_load((var12 + ((var19 + var20) << 2))) else 0):
                if (1 if var9 == -1 else 0):
                    break
                if (1 if i32_load8_u((var13 + (var9 * 132)) + 125) != 1 else 0):
                    break
            if (1 if i32_load16_u((var3 + (((var8 * var11) + var2) << 1))) == (var14 & 65535) else 0):
                break
            i32_store(((var10 << 2) + 59200), ((var8 << 16) + var2))
            var10 = (var10 + 1)
            if (1 if (var10 + 1) <= var15 else 0):
                break
            break
            i32_store16(var21, var14)
            var9 = var3
            var8 = var2
            continue
            break  # end loop
        raise RuntimeError('unreachable')
        var13 = 0
        var25 = (var25 + 1)
        if (1 if (var25 + 1) < var10 else 0):
            continue
        break  # end loop
    return 0
    return 0

