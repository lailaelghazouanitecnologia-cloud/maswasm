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
# $ze
# Export: ze
# ==========================================================
def ze(var0):
    """Export: ze"""
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
    var25 = 0.0
    var26 = 0.0
    if (1 if var0 == 0 else 0):
        break
    var21 = i32_load(9142440)
    if (1 if i32_load(9142440) > 0 else 0):
        while True:  # loop $label12
            var3 = 0
            while True:  # loop $label11
                var2 = 0
                var25 = 0.0
                var26 = 0.0
                var17 = ((i32_load(9142440) * var3) + var5)
                var22 = (((i32_load(9142440) * var3) + var5) + i32_load(9147288))
                var1 = i32_load8_u((((i32_load(9142440) * var3) + var5) + i32_load(9147288)))
                # Unknown: i32.extend8_s []
                var7 = i32_load8_u((((i32_load(9142440) * var3) + var5) + i32_load(9147288)))
                var12 = ((i32_load8_u((((i32_load(9142440) * var3) + var5) + i32_load(9147288))) + 128) if (1 if var7 < 0 else 0) else var7)
                if (1 if ((i32_load8_u((((i32_load(9142440) * var3) + var5) + i32_load(9147288))) + 128) if (1 if var7 < 0 else 0) else var7) <= 15 else 0):
                    var7 = i32_load(i32_load(9142424) + 24)
                    break
                var16 = (((var12 & 0xFFFFFFFF) >> 4) - 1)
                var4 = ((var1 & 0xFFFFFFFF) >> 7)
                var10 = i32_load((i32_load(9561728) + (var17 << 2)))
                if (1 if i32_load((i32_load(9561728) + (var17 << 2))) < 4 else 0):
                    var1 = (((var1 << 4) | ((((var1 << 24) + 1879048192) & 0xFFFFFFFF) >> 28)) & 255)
                    var9 = ((1 if (((var1 << 4) | ((((var1 << 24) + 1879048192) & 0xFFFFFFFF) >> 28)) & 255) < 14 else 0) & ((10965 & 0xFFFFFFFF) >> var1))
                    break
                var9 = 1
                var1 = (((var10 << 1) & 6) | var4)
                if (1 if (((var10 << 1) & 6) | var4) == 0 else 0):
                    var1 = i32_load(i32_load(9142424) + 24)
                    var16 = (5 if (1 if var1 == 2 else 0) else (4 if (1 if i32_load(i32_load(9142424) + 24) == 3 else 0) else 7))
                    break
                var16 = (var1 - 1)
                var13 = i32_load(9140332)
                var1 = i32_load((i32_load(9140332) + (var16 << 2)))
                var7 = i32_load(i32_load((i32_load(9140332) + (var16 << 2))))
                if (1 if i32_load(var1 + 20) == 0 else 0):
                    break
                var2 = i32_load(var1 + 28)
                if (1 if i32_load(var1 + 28) != 2147483647 else 0):
                    break
                var14 = i32_load8_u(9142916)
                if i32_load8_u(9142916):
                    var2 = i32_load(59152)
                    i32_store(59152, (i32_load(59152) + 1))
                    var8 = i32_load(9568052)
                    break
                var8 = i32_load(9568052)
                var2 = ((i32_load(9140308) + var7) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2))
                var15 = var7
                i32_store(var1 + 28, var2)
                var11 = i32_load(var1 + 4)
                var18 = i32_load(9568048)
                i32_store(9568048, (i32_load(9568048) + 1))
                i32_store(((var18 << 2) + 9563952), var1)
                i32_store(9568052, (((var15 * (var11 + 2)) << 2) + var8))
                if (1 if var14 == 0 else 0):
                    break
                var8 = i32_load(9568056)
                i32_store(var1 + 56, i32_load(9568056))
                i32_store(9568056, (var8 + ((var11 * i32_load(var1)) << 2)))
                var14 = (var5 << 5)
                var15 = (var3 << 5)
                var2 = ((((var5 << 5) % var7) + var2) + (((var3 << 5) % var7) * var7))
                var18 = i32_load(var1 + 32)
                if var9:
                    var4 = 0
                    break
                var1 = (((var10 % 4) << 1) | var4)
                if (1 if (((var10 % 4) << 1) | var4) == 0 else 0):
                    var1 = i32_load(i32_load(9142424) + 24)
                    break
                var1 = i32_load(((5 if (1 if var1 == 2 else 0) else (4 if (1 if i32_load(i32_load(9142424) + 24) == 3 else 0) else 7)) + ((var1 - 1) << 2)))
                var4 = i32_load(i32_load(((5 if (1 if var1 == 2 else 0) else (4 if (1 if i32_load(i32_load(9142424) + 24) == 3 else 0) else 7)) + ((var1 - 1) << 2))))
                var10 = 0
                var9 = 0
                if (1 if i32_load(var1 + 20) == 0 else 0):
                    break
                var9 = i32_load(var1 + 28)
                if (1 if i32_load(var1 + 28) != 2147483647 else 0):
                    break
                var13 = i32_load8_u(9142916)
                if i32_load8_u(9142916):
                    var9 = i32_load(59152)
                    i32_store(59152, (i32_load(59152) + 1))
                    var8 = i32_load(9568052)
                    break
                var8 = i32_load(9568052)
                var9 = ((i32_load(9140308) + var4) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2))
                var19 = var4
                i32_store(var1 + 28, var9)
                var11 = i32_load(var1 + 4)
                var20 = i32_load(9568048)
                i32_store(9568048, (i32_load(9568048) + 1))
                i32_store(((var20 << 2) + 9563952), var1)
                i32_store(9568052, (((var19 * (var11 + 2)) << 2) + var8))
                if (1 if var13 == 0 else 0):
                    break
                var8 = i32_load(9568056)
                i32_store(var1 + 56, i32_load(9568056))
                i32_store(9568056, (var8 + ((var11 * i32_load(var1)) << 2)))
                var8 = (var12 & 15)
                var12 = (1 if i32_load(var1 + 32) == 23 else 0)
                var11 = ((13 - (var12 & 15)) if (1 if i32_load(var1 + 32) == 23 else 0) else var8)
                var13 = (((var14 % var4) + var9) + ((var15 % var4) * var4))
                var14 = (var2 if var12 else (((var14 % var4) + var9) + ((var15 % var4) * var4)))
                var15 = (var4 // 32)
                var1 = (var1 + (i32_load(var1 + 44) << 2))
                var8 = i32_load((var1 + (i32_load(var1 + 44) << 2)))
                if (1 if i32_load(var1 + 20) == 0 else 0):
                    break
                var10 = i32_load(var1 + 28)
                if (1 if i32_load(var1 + 28) != 2147483647 else 0):
                    break
                var19 = i32_load8_u(9142916)
                if i32_load8_u(9142916):
                    var10 = i32_load(59152)
                    i32_store(59152, (i32_load(59152) + 1))
                    var4 = i32_load(9568052)
                    break
                var4 = i32_load(9568052)
                var10 = ((i32_load(9140308) + var8) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2))
                var20 = var8
                i32_store(var1 + 28, var10)
                var9 = i32_load(var1 + 4)
                var23 = i32_load(9568048)
                i32_store(9568048, (i32_load(9568048) + 1))
                i32_store(((var23 << 2) + 9563952), var1)
                i32_store(9568052, (((var20 * (var9 + 2)) << 2) + var4))
                if (1 if var19 == 0 else 0):
                    break
                var4 = i32_load(9568056)
                i32_store(var1 + 56, i32_load(9568056))
                i32_store(9568056, (var4 + ((var9 * i32_load(var1)) << 2)))
                var2 = (var13 if var12 else var2)
                var26 = float(((var10 + ((var8 * var11) << 5)) + ((i32_load((((var17 % 24) << 2) + 9824)) << 5) & 32)))
                var4 = ((var8 // 32) << 16)
                var25 = float(var14)
                var8 = (0 if var12 else (var15 << 8))
                var1 = (i32_load(9142400) + (var17 << 4))
                f32_store((i32_load(9142400) + (var17 << 4)), float(var2))
                f32_store(var1 + 4, var25)
                f32_store(var1 + 8, var26)
                f32_store(var1 + 12, float(((var8 + ((var7 // 32) if (1 if var18 != 23 else 0) else 0)) + var4)))
                i32_store8(var22, var16)
                var3 = (var3 + 1)
                if (1 if (var3 + 1) != var21 else 0):
                    continue
                break  # end loop
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var21 else 0):
                continue
            break  # end loop
    var2 = i32_load(9140328)
    if (1 if i32_load(9140328) == 0 else 0):
        break
    var1 = 0
    var3 = i32_load(9142440)
    var5 = (i32_load(9142440) * var3)
    var3 = 0
    if (1 if var2 >= 4 else 0):
        var4 = (var2 & -4)
        while True:  # loop $label14
            var7 = (var3 << 2)
            var6 = ((((var5 * i32_load(i32_load((((var3 << 2) | 12) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + ((((((var5 * i32_load(i32_load((var7 + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + var6) + (((var5 * i32_load(i32_load(((var7 | 4) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)) + (((var5 * i32_load(i32_load(((var7 | 8) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)))
            var3 = (var3 + 4)
            var24 = (var24 + 4)
            if (1 if (var24 + 4) != var4 else 0):
                continue
            break  # end loop
    var2 = (var2 & 3)
    if (1 if (var2 & 3) == 0 else 0):
        break
    while True:  # loop $label15
        var6 = ((((var5 * i32_load(i32_load(((var3 << 2) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + var6)
        var3 = (var3 + 1)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var2 else 0):
            continue
        break  # end loop
    if i32_load(9681936):
        break
    var3 = func26(16)
    var5 = (var6 << 2)
    i32_store(func26(16) + 4, (var6 << 2))
    i32_store(var3, func26((-1 if (1 if var5 > 1073741823 else 0) else (var6 << 4))))
    i64_store(var3 + 8, 206158430208)
    i32_store(9681936, var3)
    var1 = 0
    var7 = i32_load(9142440)
    if (1 if i32_load(9142440) > 0 else 0):
        while True:  # loop $label19
            var5 = (var1 + 1)
            var3 = 0
            while True:  # loop $label18
                var2 = i32_load(9142440)
                var6 = i32_load8_s((i32_load(9147288) + ((i32_load(9142440) * var3) + var1)))
                if (1 if i32_load8_s((i32_load(9147288) + ((i32_load(9142440) * var3) + var1))) >= 0 else 0):
                    if (1 if i32_load(i32_load((i32_load(9140332) + ((var6 & 255) << 2))) + 32) == 23 else 0):
                        break
                var6 = i32_load(9142840)
                var3 = (var3 + 1)
                var2 = (((var3 + 1) * (var2 + 2)) + var5)
                var4 = (i32_load(9671128) + (i32_load((i32_load(9142840) + ((((var3 + 1) * (var2 + 2)) + var5) << 2))) * 132))
                if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9142840) + ((((var3 + 1) * (var2 + 2)) + var5) << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 4 else 0):
                    var2 = (((i32_load(9142440) + 2) * var3) + var5)
                    var6 = i32_load(9142840)
                var2 = (var6 + (var2 << 2))
                if (1 if i32_load((var6 + (var2 << 2))) != 1 else 0):
                    break
                i32_store(var2, 0)
                var2 = (i32_load(9142440) + 2)
                i32_store((var6 + (((((i32_load(9142440) + 2) + var3) * var2) + var5) << 2)), 0)
                break
                var6 = i32_load(9142840)
                var2 = (var2 + 2)
                var3 = (var3 + 1)
                var4 = (i32_load(9142840) + ((((var2 + 2) * (var3 + 1)) + var5) << 2))
                if (1 if i32_load((i32_load(9142840) + ((((var2 + 2) * (var3 + 1)) + var5) << 2))) == 0 else 0):
                    i32_store(var4, 1)
                    var2 = (i32_load(9142440) + 2)
                var2 = (((var2 + var3) * var2) + var5)
                var4 = i32_load((var6 + ((((var2 + var3) * var2) + var5) << 2)))
                if (1 if i32_load((var6 + ((((var2 + var3) * var2) + var5) << 2))) >= 3 else 0):
                    var6 = (i32_load(9142440) + 2)
                    var2 = ((((i32_load(9142440) + 2) + var3) * var6) + var5)
                    var6 = i32_load(9142840)
                i32_store((var6 + (var2 << 2)), 1)
                if (1 if var3 != var7 else 0):
                    continue
                break  # end loop
            var1 = var5
            if (1 if var5 != var7 else 0):
                continue
            break  # end loop
    if (1 if var0 == 0 else 0):
    return func115(0, 0, i32_load(9142440), 0, 0)

