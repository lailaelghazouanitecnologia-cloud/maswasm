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
# $func115
# ==========================================================
def func115(var0, var1, var2, var3, var4):
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
    if i32_load8_u(9142917):
        break
    if i32_load8_u(9142916):
        if i32_load(9142404):
            break
        var5 = i32_load(9142440)
        var5 = (i32_load(9142440) * var5)
        var6 = (-1 if (1 if (var5 * 3) > 1073741823 else 0) else ((i32_load(9142440) * var5) * 12))
        var5 = func26((-1 if (1 if (var5 * 3) > 1073741823 else 0) else ((i32_load(9142440) * var5) * 12)))
        # Unknown: memory.fill []
        i32_store(9142404, var5)
        break
    if i32_load(9142400):
        break
    var5 = i32_load(9142440)
    var5 = (i32_load(9142440) * var5)
    var6 = (-1 if (var5 & 805306368) else ((i32_load(9142440) * var5) << 4))
    var5 = func26((-1 if (var5 & 805306368) else ((i32_load(9142440) * var5) << 4)))
    # Unknown: memory.fill []
    i32_store(9142400, var5)
    if (1 if (((1 if i32_load8_u(9147212) == 0 else 0) & (var3 ^ -1)) | var4) == 0 else 0):
        break
    var9 = i32_load(9140324)
    if (1 if i32_load(9140324) == 0 else 0):
        break
    var6 = (var9 - 1)
    if (1 if var2 > 0 else 0):
        var18 = (var1 + var2)
        var10 = (var0 + var2)
        while True:  # loop $label6
            var9 = var6
            var15 = i32_load16_u(40596)
            var5 = (i32_load16_u(40596) + 2)
            i32_store16(40596, (i32_load16_u(40596) + 2))
            i32_store(9140296, 0)
            if (1 if (var5 & 65535) <= 65533 else 0):
                var7 = i32_load(9142440)
                break
            i32_store16(40596, 1)
            var7 = i32_load(9142440)
            var5 = (i32_load(9142440) * var7)
            if (1 if (i32_load(9142440) * var7) == 0 else 0):
                break
            # Unknown: memory.fill []
            var5 = var0
            while True:  # loop $label5
                var6 = var1
                while True:  # loop $label4
                    if (1 if var6 >= var7 else 0):
                        break
                    if (1 if (var5 | var6) < 0 else 0):
                        break
                    if (1 if var5 >= var7 else 0):
                        break
                    if (1 if var9 != i32_load8_s((i32_load(9147288) + ((var6 * var7) + var5))) else 0):
                        break
                    func96(var5, var6, var9, var15)
                    var7 = i32_load(9142440)
                    var6 = (var6 + 1)
                    if (1 if (var6 + 1) < var18 else 0):
                        continue
                    break  # end loop
                var5 = (var5 + 1)
                if (1 if (var5 + 1) < var10 else 0):
                    continue
                break  # end loop
            var6 = (var9 - 1)
            if var9:
                continue
            break  # end loop
        break
    var5 = i32_load(9142440)
    var18 = (i32_load(9142440) * var5)
    var10 = ((i32_load(9142440) * var5) << 1)
    var15 = i32_load(9142436)
    var7 = i32_load16_u(40596)
    if (var9 & 1):
        var7 = (var7 + 2)
        i32_store16(40596, (var7 + 2))
        if (1 if (var7 & 65535) < 65534 else 0):
            break
        var7 = 1
        i32_store16(40596, 1)
        if (1 if var18 == 0 else 0):
            break
        # Unknown: memory.fill []
        var7 = i32_load16_u(40596)
    else:
    var5 = var6
    if var6:
        while True:  # loop $label10
            var9 = var5
            var6 = (var7 + 2)
            i32_store16(40596, (var7 + 2))
            if (1 if (var6 & 65535) < 65534 else 0):
                break
            var6 = 1
            i32_store16(40596, 1)
            if (1 if var18 == 0 else 0):
                break
            # Unknown: memory.fill []
            var6 = i32_load16_u(40596)
            var7 = (var6 + 2)
            i32_store16(40596, (var6 + 2))
            if (1 if (var7 & 65535) < 65534 else 0):
                break
            var7 = 1
            i32_store16(40596, 1)
            if (1 if var18 == 0 else 0):
                break
            # Unknown: memory.fill []
            var7 = i32_load16_u(40596)
            var5 = (var9 - 2)
            if (1 if var9 != 1 else 0):
                continue
            break  # end loop
    i32_store(9140296, 0)
    if (1 if i32_load8_u(9147212) == 0 else 0):
        break
    if var3:
        break
    if (1 if var4 == 0 else 0):
        break
    var3 = i32_load(9140324)
    if (1 if i32_load(9140324) == 0 else 0):
        break
    if (1 if var2 <= 0 else 0):
        break
    var9 = (var1 + var2)
    var4 = (var0 + var2)
    var7 = i32_load(9142440)
    while True:  # loop $label17
        var3 = (var3 - 1)
        var5 = var0
        while True:  # loop $label16
            var6 = var1
            while True:  # loop $label15
                if (1 if var6 >= var7 else 0):
                    break
                if (1 if (var5 | var6) < 0 else 0):
                    break
                if (1 if var5 >= var7 else 0):
                    break
                func95(var5, var6, var3)
                var7 = i32_load(9142440)
                var6 = (var6 + 1)
                if (1 if (var6 + 1) < var9 else 0):
                    continue
                break  # end loop
            var5 = (var5 + 1)
            if (1 if (var5 + 1) < var4 else 0):
                continue
            break  # end loop
        if var3:
            continue
        break  # end loop
    var3 = i32_load(9140324)
    if (1 if i32_load(9140324) == 0 else 0):
        break
    var23 = (var1 + var2)
    var24 = (var0 + var2)
    var18 = (1 if var2 <= 0 else 0)
    while True:  # loop $label35
        i32_store(9140296, 0)
        var3 = (var3 - 1)
        if var18:
            break
        var7 = i32_load(9142440)
        var5 = var0
        while True:  # loop $label33
            var6 = var1
            while True:  # loop $label32
                if (1 if var6 >= var7 else 0):
                    break
                if (1 if (var5 | var6) < 0 else 0):
                    break
                if (1 if var5 >= var7 else 0):
                    break
                if (1 if var3 != i32_load8_s((i32_load(9147288) + ((var6 * var7) + var5))) else 0):
                    break
                var17 = 0
                var22 = 0
                var7 = 0
                var19 = 0
                var9 = (i32_load(9142440) * var6)
                var10 = i32_load(9140332)
                var8 = i32_load((i32_load(9140332) + (var3 << 2)))
                var11 = i32_load(i32_load((i32_load(9140332) + (var3 << 2))))
                if i32_load(var8 + 20):
                    var14 = i32_load8_u(9142916)
                    var19 = i32_load(var8 + 28)
                    if (1 if i32_load(var8 + 28) == 2147483647 else 0):
                        if var14:
                            var19 = i32_load(59152)
                            i32_store(59152, (i32_load(59152) + 1))
                            var13 = i32_load(9568052)
                            break
                        var13 = i32_load(9568052)
                        var19 = ((i32_load(9140308) + var11) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2))
                        var4 = var11
                        i32_store(var8 + 28, var19)
                        var15 = i32_load(var8 + 4)
                        var2 = i32_load(9568048)
                        i32_store(9568048, (i32_load(9568048) + 1))
                        i32_store(((var2 << 2) + 9563952), var8)
                        i32_store(9568052, (((var4 * (var15 + 2)) << 2) + var13))
                        if (1 if var14 == 0 else 0):
                            break
                        var2 = i32_load(9568056)
                        i32_store(var8 + 56, i32_load(9568056))
                        i32_store(9568056, (var2 + ((var15 * i32_load(var8)) << 2)))
                        break
                    if (1 if var14 == 0 else 0):
                        break
                    break
                if i32_load8_u(9142916):
                    break
                var22 = ((((var6 << 5) % var11) * var11) + ((var5 << 5) % var11))
                var17 = 1
                var20 = (var5 + var9)
                var15 = i32_load(var8 + 32)
                var9 = (var11 // 32)
                var21 = 55
                var11 = func373(var5, var6, var3)
                if (1 if func373(var5, var6, var3) < 0 else 0):
                    var16 = 0
                    var13 = 0
                    break
                var16 = 0
                var13 = 0
                if (1 if var3 <= var11 else 0):
                    break
                var12 = i32_load((var10 + (var11 << 2)))
                var7 = i32_load(i32_load((var10 + (var11 << 2))))
                if i32_load(var12 + 20):
                    var13 = i32_load(var12 + 28)
                    if (1 if i32_load(var12 + 28) == 2147483647 else 0):
                        if (1 if var17 == 0 else 0):
                            var13 = i32_load(59152)
                            i32_store(59152, (i32_load(59152) + 1))
                            var16 = i32_load(9568052)
                            break
                        var16 = i32_load(9568052)
                        var13 = ((i32_load(9140308) + var7) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2))
                        var4 = var7
                        i32_store(var12 + 28, var13)
                        var14 = 0
                        var10 = i32_load(var12 + 4)
                        var2 = i32_load(9568048)
                        i32_store(9568048, (i32_load(9568048) + 1))
                        i32_store(((var2 << 2) + 9563952), var12)
                        i32_store(9568052, (((var4 * (var10 + 2)) << 2) + var16))
                        if var17:
                            break
                        var2 = i32_load(9568056)
                        i32_store(var12 + 56, i32_load(9568056))
                        i32_store(9568056, (var2 + ((var10 * i32_load(var12)) << 2)))
                        break
                var14 = 0
                if (1 if var17 == 0 else 0):
                    break
                var14 = ((((var6 << 5) % var7) * var7) + ((var5 << 5) % var7))
                var16 = 0
                var7 = (var7 if (1 if i32_load(var12 + 32) != 23 else 0) else 0)
                var13 = (var13 + var14)
                var21 = func410(var20, var11)
                if (1 if func410(var20, var11) == 55 else 0):
                    var21 = 55
                    break
                var8 = (var8 + (i32_load(var8 + 44) << 2))
                var11 = i32_load((var8 + (i32_load(var8 + 44) << 2)))
                if i32_load(var8 + 20):
                    var12 = i32_load(var8 + 28)
                    if (1 if i32_load(var8 + 28) != 2147483647 else 0):
                        break
                    if (1 if var17 == 0 else 0):
                        var12 = i32_load(59152)
                        i32_store(59152, (i32_load(59152) + 1))
                        var16 = i32_load(9568052)
                        break
                    var16 = i32_load(9568052)
                    var12 = ((i32_load(9140308) + var11) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2))
                    var4 = var11
                    i32_store(var8 + 28, var12)
                    var14 = 0
                    var10 = i32_load(var8 + 4)
                    var2 = i32_load(9568048)
                    i32_store(9568048, (i32_load(9568048) + 1))
                    i32_store(((var2 << 2) + 9563952), var8)
                    i32_store(9568052, (((var4 * (var10 + 2)) << 2) + var16))
                    if var17:
                        break
                    var2 = i32_load(9568056)
                    i32_store(var8 + 56, i32_load(9568056))
                    i32_store(9568056, (var2 + ((var10 * i32_load(var8)) << 2)))
                    break
                var12 = 0
                var14 = 0
                if (1 if var17 == 0 else 0):
                    break
                var14 = (((i32_load((((var20 % 24) << 2) + 9824)) << 5) & 32) + ((var11 * var21) << 5))
                var16 = ((var11 // 32) << 16)
                var10 = (var12 + var14)
                if i32_load8_u(9142917):
                    break
                var4 = (var19 + var22)
                if (1 if var17 == 0 else 0):
                    var2 = (i32_load(9142404) + (var20 * 12))
                    i32_store((i32_load(9142404) + (var20 * 12)), var4)
                    i32_store(var2 + 8, ((var10 << 16) + var21))
                    i32_store(var2 + 4, var13)
                    break
                var2 = (i32_load(9142400) + (var20 << 4))
                f32_store((i32_load(9142400) + (var20 << 4)), float(var4))
                f32_store(var2 + 4, float(var13))
                f32_store(var2 + 8, float(var10))
                f32_store(var2 + 12, float(((var16 + (var9 if (1 if var15 != 23 else 0) else 0)) + ((var7 // 32) << 8))))
                if (1 if var21 != 55 else 0):
                    var2 = i32_load(9140296)
                    i32_store(9140296, (i32_load(9140296) + 1))
                    i32_store(((var2 << 2) + 59200), var20)
                var7 = i32_load(9142440)
                var6 = (var6 + 1)
                if (1 if (var6 + 1) < var23 else 0):
                    continue
                break  # end loop
            var5 = (var5 + 1)
            if (1 if (var5 + 1) < var24 else 0):
                continue
            break  # end loop
        var6 = 0
        if (1 if i32_load(9140296) == 0 else 0):
            break
        while True:  # loop $label34
            var2 = (i32_load(9147288) + i32_load(((var6 << 2) + 59200)))
            i32_store8((i32_load(9147288) + i32_load(((var6 << 2) + 59200))), (i32_load8_u(var2) ^ -1))
            var6 = (var6 + 1)
            if (1 if (var6 + 1) < i32_load(9140296) else 0):
                continue
            break  # end loop
        if var3:
            continue
        break  # end loop
    return i32_load(var8)

