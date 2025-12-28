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
# $Te
# Export: Te
# ==========================================================
def Te(var0, var1, var2, var3, var4, var5, var6):
    """Export: Te"""
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
    var27 = 0
    var28 = 0
    var29 = 0
    var30 = 0
    var31 = 0
    var32 = 0
    var33 = 0
    var34 = 0
    var35 = 0
    var36 = 0
    var37 = 0
    var38 = 0
    var39 = 0
    var40 = 0
    var41 = 0
    var42 = 0
    var43 = 0
    var44 = 0
    var45 = 0
    var46 = 0
    var47 = 0
    var48 = 0
    var49 = 0
    var50 = 0
    var51 = 0
    var52 = 0
    var53 = 0
    var54 = 0
    var55 = 0
    var56 = 0
    var11 = (global0 - 400)
    global global0
    global0 = (global0 - 400)
    i32_store8(9687269, var5)
    i32_store(9687272, var0)
    i32_store(var11 + 396, var0)
    var0 = (-1 if (1 if var0 > -5 else 0) else ((var0 & -4) + 4))
    var10 = func26((-1 if (1 if var0 > -5 else 0) else ((var0 & -4) + 4)))
    # Unknown: memory.fill []
    var15 = i32_load(var10)
    i32_store(9684508, i32_load(var10))
    if i32_load8_u(9147152):
        if (1 if var15 >= 467 else 0):
            var0 = i32_load(var10 + 72)
            i32_store(9561760, i32_load(var10 + 72))
            break
        var0 = i32_load(9561760)
        if (1 if var0 == 0 else 0):
            break
        if (1 if var3 == 0 else 0):
            if (1 if var0 == i32_load(9561756) else 0):
                break
        i32_store(9561764, 0)
        break
    i32_store(9561760, 0)
    break
    i32_store(9561760, 0)
    func182()
    i32_store8(59182, 1)
    i32_store8(9681940, 1)
    i32_store(var11 + 64, i32_load(var10 + 48))
    var0 = i32_load(var10 + 36)
    if ((1 if i32_load(var10 + 36) <= var2 else 0) & (1 if var2 >= 2 else 0)):
        break
    var1 = i32_load(9687204)
    if i32_load(9687204):
        i32_store(9687204, 0)
    i32_store(9142892, var0)
    var1 = i32_load(var10 + 68)
    i32_store(9142872, ((1 if (1 if var0 <= var1 else 0) else i32_load(var10 + 68)) if var1 else 1))
    var56 = (i64_extend_u(var0) * 286704)
    var1 = (-1 if i32(((var56 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var0) * 286704)))
    var3 = func26((-1 if i32(((var56 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var0) * 286704))))
    # Unknown: memory.fill []
    i32_store(9561692, var3)
    var1 = i32_load(var10 + 48)
    i32_store(9142440, i32_load(var10 + 48))
    var21 = (var10 + 4)
    if (1 if var15 >= 491 else 0):
        var13 = i32_load(var10 + 76)
        var20 = i32_load(var10 + 60)
        var35 = i32_load(var10 + 56)
        var6 = i32_load(var10 + 24)
        if (1 if var15 <= 551 else 0):
            var3 = (var0 - 1)
            var8 = ((((var1 * var1) & 0xFFFFFFFF) >> 2) + 1)
            var12 = (var0 * var0)
            var23 = var6
            break
        var23 = 1
        var8 = ((((var1 * var1) & 0xFFFFFFFF) >> 2) + 1)
        var12 = (var0 * var0)
        var29 = i32_load(var10 + 144)
        if (1 if var15 < 565 else 0):
            break
        var33 = i32_load(var10 + 152)
        break
    var3 = (var0 - 1)
    var8 = ((((var1 * var1) & 0xFFFFFFFF) >> 2) + 1)
    var12 = (var0 * var0)
    var13 = i32_load(var10 + 76)
    var20 = i32_load(var10 + 60)
    var35 = i32_load(var10 + 56)
    var6 = 0
    if (1 if var15 < 473 else 0):
        break
    var6 = var23
    var23 = 0
    break
    var3 = var0
    var33 = ((3019 if (1 if var15 > 555 else 0) else 3011) * var3)
    var36 = 0
    var9 = i32_load(var10 + 12)
    var24 = i32_load(var10 + 16)
    var19 = i32_load(var10 + 20)
    var14 = i32_load(var21)
    var22 = i32_load(var10 + 40)
    var18 = i32_load(var10 + 84)
    i32_store8(9147212, 1)
    if (1 if var15 < 460 else 0):
        break
    i32_store8(9147208, (1 if i32_load(var10 + 8) != 0 else 0))
    i32_store8(9147209, (1 if i32_load(var10 + 124) != 0 else 0))
    if (1 if var15 < 467 else 0):
        break
    i32_store(9561752, i32_load(var10 + 72))
    var30 = i32_load(var10 + 148)
    i32_store(9561764, 0)
    i32_store(9142952, i32_load(var10 + 28))
    i32_store(9142956, i32_load(var10 + 32))
    i32_store(9147220, i32_load(var10 + 44))
    var0 = 0
    if (1 if var5 == 0 else 0):
        var0 = i32_load(var10 + 52)
    i32_store(59148, var0)
    i32_store(9142848, var0)
    i32_store(59176, var0)
    var0 = i32_load(var10 + 64)
    i32_store(9671136, i32_load(var10 + 64))
    if (1 if i32_load(9671132) < var0 else 0):
        var0 = (var0 + 10000)
        i32_store(9671132, (var0 + 10000))
        var4 = i32_load(9671128)
        var56 = (i64_extend_u(var0) * 132)
        var1 = i32((i64_extend_u(var0) * 132))
        var3 = (i32((i64_extend_u(var0) * 132)) + 4)
        var1 = func26((-1 if i32(((var56 & 0xFFFFFFFFFFFFFFFF) >> 32)) else (-1 if (1 if var1 > var3 else 0) else (i32((i64_extend_u(var0) * 132)) + 4))))
        i32_store(func26((-1 if i32(((var56 & 0xFFFFFFFFFFFFFFFF) >> 32)) else (-1 if (1 if var1 > var3 else 0) else (i32((i64_extend_u(var0) * 132)) + 4)))), var0)
        var3 = (var1 + 4)
        if var0:
            var7 = (var3 + (var0 * 132))
            var0 = var3
            while True:  # loop $label9
                # Unknown: memory.fill []
                var1 = func26(4)
                i32_store(var0 + 4, func26(4))
                i32_store(var0, var1)
                i32_store(var0 + 8, (var1 + 4))
                var0 = (var0 + 132)
                if (1 if (var0 + 132) != var7 else 0):
                    continue
                break  # end loop
        if var4:
            var16 = (var4 - 4)
            var0 = i32_load((var4 - 4))
            if i32_load((var4 - 4)):
                var1 = (var4 + (var0 * 132))
                while True:  # loop $label10
                    var0 = (var1 - 132)
                    var7 = i32_load((var1 - 132))
                    if i32_load((var1 - 132)):
                        i32_store((var1 - 128), var7)
                    var1 = var0
                    if (1 if var0 != var4 else 0):
                        continue
                    break  # end loop
        i32_store(9671128, var3)
    i32_store(9684364, i32_load(var10 + 88))
    i32_store(9684368, i32_load(var10 + 92))
    i32_store(9684372, i32_load(var10 + 96))
    f32_store(9684340, f32_load(var10 + 100))
    f32_store(9684344, f32_load(var10 + 104))
    f32_store(9684348, f32_load(var10 + 108))
    f32_store(9684352, f32_load(var10 + 112))
    f32_store(9684356, f32_load(var10 + 116))
    f32_store(9684360, f32_load(var10 + 120))
    if var23:
        i32_store(9147312, i32_load(var10 + 128))
        i32_store(9147316, i32_load(var10 + 132))
        i32_store(9147320, i32_load(var10 + 136))
        i32_store(9147324, i32_load(var10 + 140))
    var16 = ((var9 + var24) + var19)
    var17 = (32 if (1 if var15 < 552 else 0) else 64)
    var19 = ((32 if (1 if var15 < 552 else 0) else 64) + var14)
    var27 = (((var9 + var24) + var19) + ((32 if (1 if var15 < 552 else 0) else 64) + var14))
    var3 = ((((var9 + var24) + var19) + ((32 if (1 if var15 < 552 else 0) else 64) + var14)) + var13)
    var0 = i32_load(var10 + 84)
    if i32_load(var10 + 84):
        var1 = i32_load(9142424)
        if i32_load(9142424):
            i32_store(9142424, 0)
        var4 = (var0 << 2)
        var1 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        i32_store(9142428, var0)
        i32_store(9142424, var1)
        # Unknown: memory.copy []
        i32_store(var11 + 52, var0)
        i32_store(var11 + 48, var1)
        break
    var0 = i32_load(9142424)
    if i32_load(9142424):
        i32_store(9142424, 0)
    var0 = func26(188)
    i32_store(9142428, 47)
    i32_store(9142424, var0)
    # Unknown: memory.copy []
    var0 = i32_load(9142424)
    if i32_load8_u(9142917):
        i32_store(9142832, i32_load(var0 + 48))
        i32_store(var0 + 48, 0)
    var4 = i32_load(var0 + 16)
    i32_store8(9216060, (1 if i32_load(var0 + 16) == 991915600 else 0))
    var1 = i32_load(9142440)
    var7 = i32_load(9147132)
    i32_store(9147136, ((1 if i32_load(9142440) == 4096 else 0) & (1 if i32_load(9147132) != 0 else 0)))
    if (1 if var1 == 4096 else 0):
        i32_store(51784, 4)
        i32_store(51780, 3)
    if (1 if var4 == 991915600 else 0):
        i32_store(((i32_load(38460) * 404) + 9568096) + 244, 0)
        i32_store(((i32_load(38672) * 404) + 9568096) + 244, 0)
        i32_store(((i32_load(38732) * 404) + 9568096) + 244, 0)
    if var7:
        i32_store(9142872, 0)
    var18 = (var3 + var18)
    if (1 if i32_load(var0 + 32) == 0 else 0):
        break
    if i32_load(9684368):
        break
    i32_store(9684368, (i32_load(var0 + 56) * 1000))
    if (1 if var15 >= 556 else 0):
        var24 = 0
        if var30:
            break
        if (1 if i32_load(9142848) == 0 else 0):
            break
    var24 = 0
    if (1 if (i32_load(var0 + 48) - 1) > 1 else 0):
        break
    var24 = ((((var1 * var1) & 0xFFFFFFFF) >> 5) + 1)
    var0 = 0
    var1 = (var1 * var1)
    i32_store(9147288, func26((var1 * var1)))
    if var1:
        var1 = (var10 + (var18 << 2))
        while True:  # loop $label14
            i32_store8((i32_load(9147288) + var0), i32_load8_u((var0 + var1)))
            var0 = (var0 + 1)
            var3 = i32_load(9142440)
            if (1 if (var0 + 1) < (i32_load(9142440) * var3) else 0):
                continue
            break  # end loop
    if var14:
        var0 = i32_load(9681936)
        if (1 if i32_load(9681936) == 0 else 0):
            var0 = func26(16)
            var1 = (var14 << 2)
            var3 = (((var14 << 2) & 0xFFFFFFFF) // 3)
            i32_store(func26(16) + 4, (((var14 << 2) & 0xFFFFFFFF) // 3))
            i32_store(var0, func26((-1 if (1 if var1 > -1073741825 else 0) else (var3 << 2))))
            i64_store(var0 + 8, 206158430208)
            i32_store(9681936, var0)
        var4 = 0
        while True:  # loop $label19
            var9 = (var10 + ((var4 + var17) << 2))
            var25 = i32_load((var10 + ((var4 + var17) << 2)))
            var3 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) != i32_load(var0 + 4) else 0):
                var7 = i32_load(var0)
                break
            var7 = (i32_load(var0 + 12) + var3)
            i32_store(var0 + 4, (i32_load(var0 + 12) + var3))
            var1 = i32_load(var0)
            var7 = func26((-1 if (1 if var7 > 1073741823 else 0) else (var7 << 2)))
            if var3:
                # Unknown: memory.copy []
            if var1:
                var3 = i32_load(var0 + 8)
            i32_store(var0, var7)
            var1 = i32_load(9681936)
            i32_store(var0 + 8, (var3 + 1))
            i32_store((var7 + (var3 << 2)), var25)
            var25 = i32_load(var9 + 4)
            var3 = i32_load(var1 + 8)
            if (1 if i32_load(var1 + 8) != i32_load(var1 + 4) else 0):
                var7 = i32_load(var1)
                break
            var7 = (i32_load(var1 + 12) + var3)
            i32_store(var1 + 4, (i32_load(var1 + 12) + var3))
            var0 = i32_load(var1)
            var7 = func26((-1 if (1 if var7 > 1073741823 else 0) else (var7 << 2)))
            if var3:
                # Unknown: memory.copy []
            if var0:
                var3 = i32_load(var1 + 8)
            i32_store(var1, var7)
            var0 = i32_load(9681936)
            i32_store(var1 + 8, (var3 + 1))
            i32_store((var7 + (var3 << 2)), var25)
            var7 = i32_load(var9 + 8)
            var3 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) != i32_load(var0 + 4) else 0):
                var9 = i32_load(var0)
                break
            var9 = (i32_load(var0 + 12) + var3)
            i32_store(var0 + 4, (i32_load(var0 + 12) + var3))
            var1 = i32_load(var0)
            var9 = func26((-1 if (1 if var9 > 1073741823 else 0) else (var9 << 2)))
            if var3:
                # Unknown: memory.copy []
            if var1:
                var3 = i32_load(var0 + 8)
            i32_store(var0, var9)
            var1 = i32_load(9681936)
            i32_store(var0 + 8, (var3 + 1))
            i32_store((var9 + (var3 << 2)), var7)
            var3 = i32_load(var1 + 8)
            if (1 if i32_load(var1 + 8) != i32_load(var1 + 4) else 0):
                var9 = i32_load(var1)
                break
            var9 = (i32_load(var1 + 12) + var3)
            i32_store(var1 + 4, (i32_load(var1 + 12) + var3))
            var0 = i32_load(var1)
            var9 = func26((-1 if (1 if var9 > 1073741823 else 0) else (var9 << 2)))
            if var3:
                # Unknown: memory.copy []
            if var0:
                var3 = i32_load(var1 + 8)
            i32_store(var1, var9)
            var0 = i32_load(9681936)
            i32_store(var1 + 8, (var3 + 1))
            i32_store((var9 + (var3 << 2)), 0)
            var4 = (var4 + 3)
            if (1 if (var4 + 3) < var14 else 0):
                continue
            break  # end loop
    var25 = (var8 + var18)
    var31 = ((var8 + var18) + var12)
    var32 = (((var8 + var18) + var12) + (var12 if (1 if var15 > 466 else 0) else 0))
    var34 = ((((var8 + var18) + var12) + (var12 if (1 if var15 > 466 else 0) else 0)) + var12)
    var9 = (((((var8 + var18) + var12) + (var12 if (1 if var15 > 466 else 0) else 0)) + var12) + var12)
    var14 = ((((((var8 + var18) + var12) + (var12 if (1 if var15 > 466 else 0) else 0)) + var12) + var12) + var22)
    i32_store(9142912, var6)
    if var6:
        var0 = i32_load(9142908)
        if i32_load(9142908):
            i32_store(9142908, 0)
        var0 = (var6 << 2)
        var1 = func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2)))
        i32_store(9142908, func26((-1 if (1 if var6 > 1073741823 else 0) else (var6 << 2))))
        # Unknown: memory.copy []
        if (1 if i32_load8_u(9687268) == 0 else 0):
            break
        break
    if (1 if i32_load8_u(9687268) == 0 else 0):
        break
    var0 = i32_load(9142908)
    if i32_load(9142908):
        i32_store(9142908, 0)
    i32_store(9142912, 0)
    func272()
    func271()
    func220()
    func218()
    if (1 if var15 < 460 else 0):
        break
    if (1 if var16 == 0 else 0):
        break
    var18 = i32_load(var10 + 16)
    var0 = i32_load(9684448)
    var3 = i32_load(9684452)
    var1 = i32_load(var10 + 12)
    if (1 if i32_load(9684448) <= (i32_load(9684452) + i32_load(var10 + 12)) else 0):
        var4 = (i32_load(9684456) + (var0 + var1))
        i32_store(9684448, (i32_load(9684456) + (var0 + var1)))
        var0 = i32_load(9684444)
        var4 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
        if var3:
            # Unknown: memory.copy []
        if var0:
        i32_store(9684444, var4)
    if (1 if var1 == 0 else 0):
        break
    var3 = (var10 + (var19 << 2))
    var0 = 0
    var8 = i32_load(9684444)
    if (1 if var1 != 1 else 0):
        var16 = (var1 & -2)
        var4 = 0
        while True:  # loop $label23
            var7 = (var0 << 2)
            var17 = i32_load((var3 + (var0 << 2)))
            var26 = i32_load(9684452)
            i32_store(9684452, (i32_load(9684452) + 1))
            i32_store((var8 + (var26 << 2)), var17)
            var17 = i32_load((var3 + (var7 | 4)))
            var7 = i32_load(9684452)
            i32_store(9684452, (i32_load(9684452) + 1))
            i32_store((var8 + (var7 << 2)), var17)
            var0 = (var0 + 2)
            var4 = (var4 + 2)
            if (1 if (var4 + 2) != var16 else 0):
                continue
            break  # end loop
    if (1 if (var1 & 1) == 0 else 0):
        break
    var0 = i32_load((var3 + (var0 << 2)))
    var3 = i32_load(9684452)
    i32_store(9684452, (i32_load(9684452) + 1))
    i32_store((var8 + (var3 << 2)), var0)
    var0 = i32_load(9684464)
    var4 = i32_load(9684468)
    var3 = i32_load(var10 + 16)
    if (1 if i32_load(9684464) <= (i32_load(9684468) + i32_load(var10 + 16)) else 0):
        var8 = (i32_load(9684472) + (var0 + var3))
        i32_store(9684464, (i32_load(9684472) + (var0 + var3)))
        var0 = i32_load(9684460)
        var8 = func26((-1 if (1 if var8 > 1073741823 else 0) else (var8 << 2)))
        if var4:
            # Unknown: memory.copy []
        if var0:
        i32_store(9684460, var8)
    var19 = (var1 + var19)
    if (1 if var3 == 0 else 0):
        break
    var1 = (var10 + (var19 << 2))
    var0 = 0
    var8 = i32_load(9684460)
    if (1 if var3 != 1 else 0):
        var16 = (var3 & -2)
        var4 = 0
        while True:  # loop $label25
            var7 = (var0 << 2)
            var17 = i32_load((var1 + (var0 << 2)))
            var26 = i32_load(9684468)
            i32_store(9684468, (i32_load(9684468) + 1))
            i32_store((var8 + (var26 << 2)), var17)
            var17 = i32_load((var1 + (var7 | 4)))
            var7 = i32_load(9684468)
            i32_store(9684468, (i32_load(9684468) + 1))
            i32_store((var8 + (var7 << 2)), var17)
            var0 = (var0 + 2)
            var4 = (var4 + 2)
            if (1 if (var4 + 2) != var16 else 0):
                continue
            break  # end loop
    if (1 if (var3 & 1) == 0 else 0):
        break
    var0 = i32_load((var1 + (var0 << 2)))
    var1 = i32_load(9684468)
    i32_store(9684468, (i32_load(9684468) + 1))
    i32_store((var8 + (var1 << 2)), var0)
    var0 = i32_load(9684480)
    var3 = i32_load(9684484)
    var1 = i32_load(var10 + 20)
    if (1 if i32_load(9684480) <= (i32_load(9684484) + i32_load(var10 + 20)) else 0):
        var4 = (i32_load(9684488) + (var0 + var1))
        i32_store(9684480, (i32_load(9684488) + (var0 + var1)))
        var0 = i32_load(9684476)
        var4 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
        if var3:
            # Unknown: memory.copy []
        if var0:
        i32_store(9684476, var4)
    if (1 if var1 == 0 else 0):
        break
    var3 = (var10 + ((var18 + var19) << 2))
    var0 = 0
    var8 = i32_load(9684476)
    if (1 if var1 != 1 else 0):
        var19 = (var1 & -2)
        var4 = 0
        while True:  # loop $label26
            var7 = (var0 << 2)
            var18 = i32_load((var3 + (var0 << 2)))
            var16 = i32_load(9684484)
            i32_store(9684484, (i32_load(9684484) + 1))
            i32_store((var8 + (var16 << 2)), var18)
            var18 = i32_load((var3 + (var7 | 4)))
            var7 = i32_load(9684484)
            i32_store(9684484, (i32_load(9684484) + 1))
            i32_store((var8 + (var7 << 2)), var18)
            var0 = (var0 + 2)
            var4 = (var4 + 2)
            if (1 if (var4 + 2) != var19 else 0):
                continue
            break  # end loop
    if (1 if (var1 & 1) == 0 else 0):
        break
    var0 = i32_load((var3 + (var0 << 2)))
    var1 = i32_load(9684484)
    i32_store(9684484, (i32_load(9684484) + 1))
    i32_store((var8 + (var1 << 2)), var0)
    var19 = (var6 + var14)
    if (1 if var24 == 0 else 0):
        break
    var0 = 0
    i32_store8(9142904, 1)
    var1 = i32_load(9142440)
    var1 = (i32_load(9142440) * var1)
    var3 = ((i32_load(9142440) * var1) + 2)
    var4 = func26((-1 if (1 if var3 < 0 else 0) else (((i32_load(9142440) * var1) + 2) << 1)))
    i32_store(9147376, func26((-1 if (1 if var3 < 0 else 0) else (((i32_load(9142440) * var1) + 2) << 1))))
    if (1 if var1 == 0 else 0):
        break
    var7 = (var10 + (var19 << 2))
    if (1 if var1 != 1 else 0):
        var6 = (var1 & -2)
        var3 = 0
        while True:  # loop $label28
            var8 = (var7 + (((var0 & 0xFFFFFFFF) >> 3) & 536870908))
            i32_store16((var4 + (var0 << 1)), (((i32_load((var7 + (((var0 & 0xFFFFFFFF) >> 3) & 536870908))) & 0xFFFFFFFF) >> (var0 & 30)) & 1))
            var14 = (var0 | 1)
            i32_store16((var4 + ((var0 | 1) << 1)), (((i32_load(var8) & 0xFFFFFFFF) >> var14) & 1))
            var0 = (var0 + 2)
            var3 = (var3 + 2)
            if (1 if (var3 + 2) != var6 else 0):
                continue
            break  # end loop
    if (1 if (var1 & 1) == 0 else 0):
        break
    i32_store16((var4 + (var0 << 1)), (((i32_load((var7 + (((var0 & 0xFFFFFFFF) >> 3) & 536870908))) & 0xFFFFFFFF) >> var0) & 1))
    if var13:
        var3 = (var10 + (var27 << 2))
        var6 = (var11 + 288)
        var27 = (1 if var15 > 563 else 0)
        var0 = 0
        while True:  # loop $label47
            i64_store(var11 + 280, 0)
            i64_store(var11 + 272, 0)
            i64_store(var11 + 264, 0)
            i32_store(var11 + 388, 0)
            var1 = (var3 + (var0 << 2))
            var18 = i32_load((var3 + (var0 << 2)))
            var16 = i32_load(var1 + 4)
            var1 = i32_load(var1 + 8)
            i32_store(var11 + 368, i32_load(var1 + 8))
            var0 = (var0 + 3)
            if (1 if var1 == 0 else 0):
                break
            var17 = (var1 & 3)
            var8 = 0
            if (1 if var1 < 4 else 0):
                var1 = 0
                break
            var26 = (var1 & -4)
            var1 = 0
            var14 = 0
            while True:  # loop $label31
                var4 = (var1 << 1)
                var7 = (var3 + (var0 << 2))
                i32_store16((var6 + (var1 << 1)), i32_load((var3 + (var0 << 2))))
                i32_store16((var6 + (var4 | 2)), i32_load(var7 + 4))
                i32_store16((var6 + (var4 | 4)), i32_load(var7 + 8))
                i32_store16((var6 + (var4 | 6)), i32_load(var7 + 12))
                var1 = (var1 + 4)
                var0 = (var0 + 4)
                var14 = (var14 + 4)
                if (1 if (var14 + 4) != var26 else 0):
                    continue
                break  # end loop
            if (1 if var17 == 0 else 0):
                break
            while True:  # loop $label32
                i32_store16(((var1 << 1) + var11) + 288, i32_load((var3 + (var0 << 2))))
                var1 = (var1 + 1)
                var0 = (var0 + 1)
                var8 = (var8 + 1)
                if (1 if (var8 + 1) != var17 else 0):
                    continue
                break  # end loop
            var1 = (var3 + (var0 << 2))
            i32_store(var11 + 372, i32_load((var3 + (var0 << 2))))
            i32_store(var11 + 376, i32_load(var1 + 4))
            var4 = i32_load(var1 + 8)
            var7 = (var0 + 4)
            i32_store(var11 + 392, (var0 + 4))
            i32_store(var11 + 380, var4)
            i32_store(var11 + 384, i32_load(var1 + 12))
            if var27:
                i32_store(var11 + 392, (var0 + 5))
                i32_store(var11 + 388, i32_load((var3 + (var7 << 2))))
            var4 = 0
            if (1 if var18 == 0 else 0):
                break
            while True:  # loop $label37
                func381((var11 + 68), var3, (var11 + 392), 1, var15)
                var0 = i32_load(var11 + 268)
                var8 = i32_load(var11 + 272)
                if (1 if i32_load(var11 + 268) < i32_load(var11 + 272) else 0):
                    # Unknown: memory.copy []
                    i32_store(var11 + 268, (var0 + 196))
                    break
                var0 = i32_load(var11 + 264)
                var7 = (var0 - i32_load(var11 + 264))
                var14 = ((var0 - i32_load(var11 + 264)) // 196)
                var1 = (((var0 - i32_load(var11 + 264)) // 196) + 1)
                if (1 if (((var0 - i32_load(var11 + 264)) // 196) + 1) >= 21913099 else 0):
                    break
                var8 = ((var8 - var0) // 196)
                var17 = (((var8 - var0) // 196) << 1)
                var1 = (21913098 if (1 if var8 >= 10956549 else 0) else ((((var8 - var0) // 196) << 1) if (1 if var1 < var17 else 0) else var1))
                if (21913098 if (1 if var8 >= 10956549 else 0) else ((((var8 - var0) // 196) << 1) if (1 if var1 < var17 else 0) else var1)):
                    if (1 if var1 >= 21913099 else 0):
                        break
                else:
                var17 = 0
                var8 = (0 + (var14 * 196))
                # Unknown: memory.copy []
                var14 = (var8 + ((var7 // -196) * 196))
                # Unknown: memory.copy []
                i32_store(var11 + 272, (var17 + (var1 * 196)))
                i32_store(var11 + 268, (var8 + 196))
                i32_store(var11 + 264, var14)
                if (1 if var0 == 0 else 0):
                    break
                var4 = (var4 + 1)
                if (1 if var18 != (var4 + 1) else 0):
                    continue
                break
                break  # end loop
            func42()
            raise RuntimeError('unreachable')
            var4 = 0
            if (1 if var16 == 0 else 0):
                break
            while True:  # loop $label41
                func381((var11 + 68), var3, (var11 + 392), 0, var15)
                var0 = i32_load(var11 + 280)
                var8 = i32_load(var11 + 284)
                if (1 if i32_load(var11 + 280) < i32_load(var11 + 284) else 0):
                    # Unknown: memory.copy []
                    i32_store(var11 + 280, (var0 + 196))
                    break
                var0 = i32_load(var11 + 276)
                var7 = (var0 - i32_load(var11 + 276))
                var14 = ((var0 - i32_load(var11 + 276)) // 196)
                var1 = (((var0 - i32_load(var11 + 276)) // 196) + 1)
                if (1 if (((var0 - i32_load(var11 + 276)) // 196) + 1) >= 21913099 else 0):
                    break
                var8 = ((var8 - var0) // 196)
                var18 = (((var8 - var0) // 196) << 1)
                var1 = (21913098 if (1 if var8 >= 10956549 else 0) else ((((var8 - var0) // 196) << 1) if (1 if var1 < var18 else 0) else var1))
                if (21913098 if (1 if var8 >= 10956549 else 0) else ((((var8 - var0) // 196) << 1) if (1 if var1 < var18 else 0) else var1)):
                    if (1 if var1 >= 21913099 else 0):
                        break
                else:
                var18 = 0
                var8 = (0 + (var14 * 196))
                # Unknown: memory.copy []
                var14 = (var8 + ((var7 // -196) * 196))
                # Unknown: memory.copy []
                i32_store(var11 + 284, (var18 + (var1 * 196)))
                i32_store(var11 + 280, (var8 + 196))
                i32_store(var11 + 276, var14)
                if (1 if var0 == 0 else 0):
                    break
                var4 = (var4 + 1)
                if (1 if var16 != (var4 + 1) else 0):
                    continue
                break  # end loop
            break
            func68()
            raise RuntimeError('unreachable')
            func42()
            raise RuntimeError('unreachable')
            var7 = i32_load(9568068)
            if (1 if i32_load(9568068) != i32_load(9568072) else 0):
                i32_store(var7 + 8, 0)
                i64_store(var7, 0)
                var0 = i32_load(var11 + 268)
                var4 = i32_load(var11 + 264)
                var8 = (i32_load(var11 + 268) - i32_load(var11 + 264))
                var1 = ((i32_load(var11 + 268) - i32_load(var11 + 264)) // 196)
                if (1 if var0 != var4 else 0):
                    if (1 if var1 >= 21913099 else 0):
                        break
                    var0 = func26(var8)
                    i32_store(var7 + 4, func26(var8))
                    i32_store(var7, var0)
                    i32_store(var7 + 8, (var0 + (var1 * 196)))
                    var1 = i32_load(var11 + 264)
                    var4 = i32_load(var11 + 268)
                    if (1 if i32_load(var11 + 264) != i32_load(var11 + 268) else 0):
                        while True:  # loop $label43
                            # Unknown: memory.copy []
                            var0 = (var0 + 196)
                            var1 = (var1 + 196)
                            if (1 if (var1 + 196) != var4 else 0):
                                continue
                            break  # end loop
                    i32_store(var7 + 4, var0)
                i64_store(var7 + 12, 0)
                i32_store(var7 + 20, 0)
                var8 = i32_load(var11 + 280)
                var0 = i32_load(var11 + 276)
                var4 = (i32_load(var11 + 280) - i32_load(var11 + 276))
                var1 = ((i32_load(var11 + 280) - i32_load(var11 + 276)) // 196)
                if (1 if var0 != var8 else 0):
                    if (1 if var1 >= 21913099 else 0):
                        break
                    var0 = func26(var4)
                    i32_store(var7 + 16, func26(var4))
                    i32_store(var7 + 12, var0)
                    i32_store(var7 + 20, (var0 + (var1 * 196)))
                    var8 = i32_load(var11 + 276)
                    var1 = i32_load(var11 + 276)
                    var4 = i32_load(var11 + 280)
                    if (1 if i32_load(var11 + 280) != var8 else 0):
                        while True:  # loop $label45
                            # Unknown: memory.copy []
                            var0 = (var0 + 196)
                            var1 = (var1 + 196)
                            if (1 if (var1 + 196) != var4 else 0):
                                continue
                            break  # end loop
                    i32_store(var7 + 16, var0)
                # Unknown: memory.copy []
                i32_store(9568068, (var7 + 128))
                break
            var8 = i32_load(var11 + 276)
            if var8:
                i32_store(var11 + 280, var8)
            var0 = i32_load(var11 + 264)
            if i32_load(var11 + 264):
                i32_store(var11 + 268, var0)
            var0 = i32_load(var11 + 392)
            if (1 if i32_load(var11 + 392) < var13 else 0):
                continue
            break  # end loop
    var0 = 0
    var1 = func26(var12)
    # Unknown: memory.fill []
    i32_store(9143004, var1)
    var1 = func26(var12)
    # Unknown: memory.fill []
    i32_store(9143012, var1)
    var1 = func26(var12)
    # Unknown: memory.fill []
    i32_store(9143008, var1)
    var1 = func26(var12)
    # Unknown: memory.fill []
    i32_store(9143016, var1)
    if var12:
        var1 = (1 if var15 < 467 else 0)
        while True:  # loop $label48
            i32_store8((i32_load(9143004) + var0), (1 if i32_load((var10 + ((var0 + var25) << 2))) != 0 else 0))
            if (1 if var1 == 0 else 0):
                i32_store8((i32_load(9143012) + var0), (1 if i32_load((var10 + ((var0 + var32) << 2))) != 0 else 0))
            i32_store8((i32_load(9143016) + var0), i32_load((var10 + ((var0 + var34) << 2))))
            i32_store8((i32_load(9143008) + var0), (1 if i32_load((var10 + ((var0 + var31) << 2))) != 0 else 0))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var12 else 0):
                continue
            break  # end loop
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) >= 2 else 0):
        var12 = (var4 + 1)
        var0 = (var4 - 1)
        var7 = ((var4 - 1) & -4)
        var6 = (var0 & 3)
        var13 = (1 if (var4 - 2) < 3 else 0)
        var1 = 1
        while True:  # loop $label53
            var3 = 0
            var8 = (i32_load(9143012) + (var1 * var12))
            var0 = 1
            if (1 if var13 == 0 else 0):
                while True:  # loop $label51
                    if (1 if var0 == var1 else 0):
                        break
                    if (1 if var1 == (var0 + 1) else 0):
                        break
                    if (1 if var1 == (var0 + 2) else 0):
                        break
                    if (1 if var1 != (var0 + 3) else 0):
                        break
                    i32_store8(var8, 1)
                    var0 = (var0 + 4)
                    var3 = (var3 + 4)
                    if (1 if (var3 + 4) != var7 else 0):
                        continue
                    break  # end loop
            var3 = 0
            if var6:
                while True:  # loop $label52
                    if (1 if var0 == var1 else 0):
                        i32_store8(var8, 1)
                    var0 = (var0 + 1)
                    var3 = (var3 + 1)
                    if (1 if (var3 + 1) != var6 else 0):
                        continue
                    break  # end loop
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var4 else 0):
                continue
            break  # end loop
    if (1 if var15 > 466 else 0):
        break
    var0 = 0
    var3 = (var4 * var4)
    var1 = func26((var4 * var4))
    # Unknown: memory.fill []
    i32_store(9143012, var1)
    if (1 if var3 == 0 else 0):
        break
    var7 = (var3 & 3)
    var6 = i32_load(9143004)
    if (1 if var3 >= 4 else 0):
        var3 = (var3 & -4)
        var4 = 0
        while True:  # loop $label55
            i32_store8((var0 + var1), (i32_load8_u((var0 + var6)) ^ 1))
            var8 = (var0 | 1)
            i32_store8((var1 + (var0 | 1)), (i32_load8_u((var6 + var8)) ^ 1))
            var8 = (var0 | 2)
            i32_store8((var1 + (var0 | 2)), (i32_load8_u((var6 + var8)) ^ 1))
            var8 = (var0 | 3)
            i32_store8((var1 + (var0 | 3)), (i32_load8_u((var6 + var8)) ^ 1))
            var0 = (var0 + 4)
            var4 = (var4 + 4)
            if (1 if (var4 + 4) != var3 else 0):
                continue
            break  # end loop
    if (1 if var7 == 0 else 0):
        break
    var4 = 0
    while True:  # loop $label56
        i32_store8((var0 + var1), (i32_load8_u((var0 + var6)) ^ 1))
        var0 = (var0 + 1)
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var7 else 0):
            continue
        break  # end loop
    var1 = (4 if var5 else var22)
    i32_store(9215892, (4 if var5 else var22))
    if (1 if i32_load(9215888) <= var1 else 0):
        var0 = (var1 + 1024)
        i32_store(9215888, (var1 + 1024))
        var3 = i32_load(9215884)
        var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var3:
        i32_store(9215884, var0)
    var14 = (var19 + var24)
    var33 = ((var19 + var24) + var33)
    var6 = 0
    if (1 if i32_load(9142848) == 0 else 0):
        i32_store(9215892, 4)
        var24 = 1
        break
    if (1 if var1 == 0 else 0):
        var24 = 1
        break
    var7 = (var1 & 3)
    var3 = 0
    var6 = i32_load(9215884)
    var0 = 0
    if (1 if var1 >= 4 else 0):
        var8 = (var1 & -4)
        var4 = 0
        while True:  # loop $label58
            i32_store((var6 + (var0 << 2)), i32_load((var10 + ((var0 + var9) << 2))))
            var12 = (var0 | 1)
            i32_store((var6 + ((var0 | 1) << 2)), i32_load((var10 + ((var9 + var12) << 2))))
            var12 = (var0 | 2)
            i32_store((var6 + ((var0 | 2) << 2)), i32_load((var10 + ((var9 + var12) << 2))))
            var12 = (var0 | 3)
            i32_store((var6 + ((var0 | 3) << 2)), i32_load((var10 + ((var9 + var12) << 2))))
            var0 = (var0 + 4)
            var4 = (var4 + 4)
            if (1 if (var4 + 4) != var8 else 0):
                continue
            break  # end loop
    var24 = (1 if var1 == 0 else 0)
    if var7:
        while True:  # loop $label59
            i32_store((var6 + (var0 << 2)), i32_load((var10 + ((var0 + var9) << 2))))
            var0 = (var0 + 1)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var7 else 0):
                continue
            break  # end loop
    var6 = var1
    var22 = (var33 + var35)
    var13 = (253 if (1 if var15 < 552 else 0) else 255)
    var8 = 0
    var1 = i32_load(9142892)
    if var29:
        if (1 if var1 == 0 else 0):
            break
        var0 = (var20 + var22)
        while True:  # loop $label68
            var7 = i32_load(9561692)
            if (1 if var30 == 0 else 0):
                var3 = (var7 + (var8 * 286704))
                var1 = (var1 * var13)
                var1 = (-1 if (1 if var1 > 1073741823 else 0) else ((var1 * var13) << 2))
                i32_store((var7 + (var8 * 286704)) + 278556, func26((-1 if (1 if var1 > 1073741823 else 0) else ((var1 * var13) << 2))))
                var4 = (var3 + 278560)
                i32_store((var3 + 278560), func26(var1))
                var9 = (var3 + 278564)
                i32_store((var3 + 278564), func26(var1))
                var12 = func26(var1)
                i32_store((var3 + 278568), func26(var1))
                var19 = i32_load(var3 + 278556)
                var1 = 0
                while True:  # loop $label61
                    i32_store((var19 + (var1 << 2)), i32_load((var10 + (var0 << 2))))
                    var0 = (var0 + 1)
                    var1 = (var1 + 1)
                    var18 = i32_load(9142892)
                    if (1 if (var1 + 1) < (i32_load(9142892) * 255) else 0):
                        continue
                    break  # end loop
                if (1 if var18 == 0 else 0):
                    break
                var4 = i32_load(var4)
                var1 = 0
                while True:  # loop $label63
                    i32_store((var4 + (var1 << 2)), i32_load((var10 + (var0 << 2))))
                    var0 = (var0 + 1)
                    var1 = (var1 + 1)
                    var19 = i32_load(9142892)
                    if (1 if (var1 + 1) < (i32_load(9142892) * 255) else 0):
                        continue
                    break  # end loop
                if (1 if var19 == 0 else 0):
                    break
                var9 = i32_load(var9)
                var1 = 0
                while True:  # loop $label64
                    i32_store((var9 + (var1 << 2)), i32_load((var10 + (var0 << 2))))
                    var0 = (var0 + 1)
                    var1 = (var1 + 1)
                    var19 = i32_load(9142892)
                    var4 = (i32_load(9142892) * 255)
                    if (1 if (var1 + 1) < (i32_load(9142892) * 255) else 0):
                        continue
                    break  # end loop
                if (1 if var19 == 0 else 0):
                    break
                var1 = (1 if (1 if var4 <= 1 else 0) else var4)
                # Unknown: memory.copy []
                var0 = (var0 + var1)
                var12 = (var0 << 2)
                var1 = i32_load((var10 + (var0 << 2)))
                var4 = func26(16)
                var9 = (var1 + 21000)
                i32_store(func26(16) + 4, (var1 + 21000))
                var9 = func26((-1 if (1 if var9 > 1073741823 else 0) else (var9 << 2)))
                i32_store(var4 + 12, 21000)
                i32_store(var4, var9)
                i32_store((var3 + 278572), var4)
                var0 = (var0 + 1)
                if var1:
                    # Unknown: memory.copy []
                    var0 = (var0 + var1)
                i32_store(var4 + 8, var1)
            var3 = 0
            var4 = 0
            while True:  # loop $label65
                var1 = (var7 + (var8 * 286704))
                var9 = ((var7 + (var8 * 286704)) + (var4 << 2))
                var12 = (var10 + (var0 << 2))
                i32_store((((var7 + (var8 * 286704)) + (var4 << 2)) + 278576), i32_load((var10 + (var0 << 2))))
                i32_store((var9 + 278580), i32_load(var12 + 4))
                i32_store((var9 + 278584), i32_load(var12 + 8))
                var0 = (var0 + 3)
                var4 = (var4 + 3)
                if (1 if (var4 + 3) != 255 else 0):
                    continue
                break  # end loop
            while True:  # loop $label66
                var4 = (var1 + (var3 << 2))
                var7 = (var10 + (var0 << 2))
                i32_store(((var1 + (var3 << 2)) + 279596), i32_load((var10 + (var0 << 2))))
                i32_store((var4 + 279600), i32_load(var7 + 4))
                i32_store((var4 + 279604), i32_load(var7 + 8))
                var0 = (var0 + 3)
                var3 = (var3 + 3)
                if (1 if (var3 + 3) != 255 else 0):
                    continue
                break  # end loop
            var4 = 0
            while True:  # loop $label67
                var9 = (var1 + (var4 << 2))
                var7 = var0
                var3 = (var10 + (var0 << 2))
                i32_store(((var1 + (var4 << 2)) + 280616), i32_load((var10 + (var0 << 2))))
                i32_store((var9 + 280620), i32_load(var3 + 4))
                i32_store((var9 + 280624), i32_load(var3 + 8))
                var0 = (var0 + 3)
                var4 = (var4 + 3)
                if (1 if (var4 + 3) != 255 else 0):
                    continue
                break  # end loop
            i32_store((var1 + 281636), i32_load((var10 + (var0 << 2))))
            i32_store((var1 + 281640), i32_load(var3 + 16))
            i32_store((var1 + 281644), i32_load(var3 + 20))
            i32_store((var1 + 281648), i32_load(var3 + 24))
            i32_store((var1 + 281652), i32_load(var3 + 28))
            i32_store((var1 + 281656), i32_load(var3 + 32))
            i32_store((var1 + 281660), i32_load(var3 + 36))
            i32_store((var1 + 281664), i32_load(var3 + 40))
            i32_store((var1 + 281668), i32_load(var3 + 44))
            i32_store((var1 + 281672), i32_load(var3 + 48))
            i32_store((var1 + 281676), i32_load(var3 + 52))
            i32_store((var1 + 281680), i32_load(var3 + 56))
            i32_store((var1 + 281684), i32_load(var3 + 60))
            i32_store((var1 + 281688), i32_load((var3 - -64)))
            i32_store((var1 + 281692), i32_load(var3 + 68))
            i32_store((var1 + 281696), i32_load(var3 + 72))
            i32_store((var1 + 281700), i32_load(var3 + 76))
            i32_store((var1 + 281704), i32_load(var3 + 80))
            i32_store((var1 + 281708), i32_load(var3 + 84))
            i32_store((var1 + 281712), i32_load(var3 + 88))
            i32_store((var1 + 281716), i32_load(var3 + 92))
            i32_store((var1 + 281720), i32_load(var3 + 96))
            if (1 if var5 == 0 else 0):
                i32_store((var1 + 281724), i32_load(var3 + 100))
                i32_store((var1 + 281728), i32_load(var3 + 104))
                i32_store((var1 + 281732), i32_load(var3 + 108))
                i32_store((var1 + 281736), i32_load(var3 + 112))
            i32_store((var1 + 281740), i32_load(var3 + 116))
            i32_store((var1 + 281744), i32_load(var3 + 120))
            i32_store((var1 + 281748), i32_load(var3 + 124))
            i32_store((var1 + 281752), i32_load(var3 + 128))
            i32_store((var1 + 281756), i32_load(var3 + 132))
            i32_store((var1 + 281760), i32_load(var3 + 136))
            i32_store((var1 + 281764), i32_load(var3 + 140))
            i32_store((var1 + 281768), i32_load(var3 + 144))
            i32_store((var1 + 281772), i32_load(var3 + 148))
            i32_store((var1 + 281776), i32_load(var3 + 152))
            var0 = i32_load(var3 + 156)
            i32_store((var1 + 281784), var8)
            i32_store((var1 + 281780), var0)
            var0 = (var7 + 40)
            var8 = (var8 + 1)
            var1 = i32_load(9142892)
            if (1 if (var8 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
        break
    if (1 if var1 == 0 else 0):
        break
    var0 = 0
    while True:  # loop $label69
        func239(var0)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    var1 = i32_load(9561692)
    var0 = 39
    while True:  # loop $label70
        var3 = (var0 << 2)
        var4 = ((var1 + (var0 << 2)) + 283984)
        if (1 if i32_load(((var1 + (var0 << 2)) + 283984)) == 0 else 0):
            i32_store(var4, i32_load((var3 + 9561072)))
        var3 = ((var0 + 1) << 2)
        var4 = ((var1 + ((var0 + 1) << 2)) + 283984)
        if (1 if i32_load(((var1 + ((var0 + 1) << 2)) + 283984)) == 0 else 0):
            i32_store(var4, i32_load((var3 + 9561072)))
        var0 = (var0 + 2)
        if (1 if (var0 + 2) != 155 else 0):
            continue
        break  # end loop
    var12 = (1 if var15 < 552 else 0)
    if (1 if (1 if var15 < 552 else 0) >= i32_load(9142892) else 0):
        break
    var0 = (var10 + (var14 << 2))
    var21 = (var13 & 3)
    var14 = (155 if (1 if var15 > 481 else 0) else 40)
    var34 = ((155 if (1 if var15 > 481 else 0) else 40) & 184)
    var19 = (var14 & 3)
    var18 = (1 if var15 < 473 else 0)
    var26 = (1 if var15 < 482 else 0)
    var37 = (1 if var15 < 491 else 0)
    var38 = (1 if var15 < 556 else 0)
    var3 = 0
    while True:  # loop $label89
        var7 = (i32_load(9561692) + (var12 * 286704))
        i32_store((i32_load(9561692) + (var12 * 286704)) + 283908, var12)
        var1 = ((var3 << 2) + var0)
        if i32_load(var7 + 284616):
            i32_store(var7 + 40, i32_load(var1))
            i32_store(var7 + 44, i32_load(var1 + 4))
            i32_store(var7 + 48, i32_load(var1 + 8))
            i32_store(var7 + 52, i32_load(var1 + 12))
            i32_store(var7 + 56, i32_load(var1 + 16))
            i32_store(var7 + 60, i32_load(var1 + 20))
            i32_store((var7 - -64), i32_load(var1 + 24))
            i32_store(var7 + 68, i32_load(var1 + 28))
            i32_store(var7 + 72, i32_load(var1 + 32))
            i32_store(var7 + 76, i32_load(var1 + 36))
            break
        var4 = i32_load(var1)
        i32_store(var7, i32_load(var1))
        var8 = i32_load(var1 + 4)
        i32_store(var7 + 4, i32_load(var1 + 4))
        var9 = i32_load(var1 + 8)
        i32_store(var7 + 8, i32_load(var1 + 8))
        var16 = i32_load(var1 + 12)
        i32_store(var7 + 12, i32_load(var1 + 12))
        var17 = i32_load(var1 + 16)
        i32_store(var7 + 16, i32_load(var1 + 16))
        var29 = i32_load(var1 + 20)
        i32_store(var7 + 20, i32_load(var1 + 20))
        var27 = i32_load(var1 + 24)
        i32_store(var7 + 24, i32_load(var1 + 24))
        var25 = i32_load(var1 + 28)
        i32_store(var7 + 28, i32_load(var1 + 28))
        var31 = i32_load(var1 + 32)
        i32_store(var7 + 32, i32_load(var1 + 32))
        var32 = i32_load(var1 + 36)
        i32_store16(var7 + 76, i32_load(var1 + 36))
        i32_store16(var7 + 74, ((var31 & 0xFFFFFFFF) >> 16))
        i32_store16(var7 + 72, var31)
        i32_store16(var7 + 70, ((var25 & 0xFFFFFFFF) >> 16))
        i32_store16(var7 + 68, var25)
        i32_store16(var7 + 66, ((var27 & 0xFFFFFFFF) >> 16))
        i32_store16((var7 - -64), var27)
        i32_store16(var7 + 62, ((var29 & 0xFFFFFFFF) >> 16))
        i32_store16(var7 + 60, var29)
        i32_store16(var7 + 58, ((var17 & 0xFFFFFFFF) >> 16))
        i32_store16(var7 + 56, var17)
        i32_store16(var7 + 54, ((var16 & 0xFFFFFFFF) >> 16))
        i32_store16(var7 + 52, var16)
        i32_store16(var7 + 50, ((var9 & 0xFFFFFFFF) >> 16))
        i32_store16(var7 + 48, var9)
        i32_store16(var7 + 46, ((var8 & 0xFFFFFFFF) >> 16))
        i32_store16(var7 + 44, var8)
        i32_store16(var7 + 42, ((var4 & 0xFFFFFFFF) >> 16))
        i32_store16(var7 + 40, var4)
        i32_store16(var7 + 36, var32)
        var4 = ((var32 & 0xFFFFFFFF) >> 16)
        i32_store16(var7 + 78, ((var32 & 0xFFFFFFFF) >> 16))
        i32_store16(var7 + 38, var4)
        var4 = i32_load(var1 + 40)
        if (1 if i32_load(var1 + 40) == 0 else 0):
            break
        if var5:
            break
        var16 = (var10 + (var4 << 2))
        var4 = i32_load((var10 + (var4 << 2)))
        var8 = func26(16)
        i32_store(func26(16) + 4, var4)
        var17 = (var4 << 2)
        var9 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
        i32_store(var8 + 12, 20)
        i32_store(var8, var9)
        i32_store(var8 + 8, var4)
        if var4:
            # Unknown: memory.copy []
        i32_store(var7 + 281788, var8)
        var4 = i32_load(var1 + 44)
        if (1 if i32_load(var1 + 44) == 0 else 0):
            break
        if var5:
            break
        var16 = (var10 + (var4 << 2))
        var4 = i32_load((var10 + (var4 << 2)))
        var8 = func26(16)
        var9 = (var4 + 8)
        i32_store(func26(16) + 4, (var4 + 8))
        var9 = func26((-1 if (1 if var9 > 1073741823 else 0) else (var9 << 2)))
        i32_store(var8 + 12, 20)
        i32_store(var8, var9)
        i32_store(var8 + 8, var4)
        if var4:
            # Unknown: memory.copy []
        i32_store(var7 + 281792, var8)
        var9 = (var3 + 12)
        if (1 if var18 == 0 else 0):
            var4 = i32_load((var0 + (var9 << 2)))
            if (1 if i32_load((var0 + (var9 << 2))) == 0 else 0):
                break
            if var5:
                break
            var16 = (var10 + (var4 << 2))
            var4 = i32_load((var10 + (var4 << 2)))
            var8 = func26(16)
            i32_store(func26(16) + 4, var4)
            var17 = (var4 << 2)
            var9 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
            i32_store(var8 + 12, 20)
            i32_store(var8, var9)
            i32_store(var8 + 8, var4)
            if var4:
                # Unknown: memory.copy []
            i32_store(var7 + 281796, var8)
            var1 = i32_load(var1 + 52)
            if i32_load(var1 + 52):
                var9 = (var10 + (var1 << 2))
                var1 = i32_load((var10 + (var1 << 2)))
                var4 = func26(16)
                i32_store(func26(16) + 4, var1)
                var16 = (var1 << 2)
                var8 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                i32_store(var4 + 12, 20)
                i32_store(var4, var8)
                i32_store(var4 + 8, var1)
                if var1:
                    # Unknown: memory.copy []
                i32_store(var7 + 286680, var4)
            var9 = (var3 + 14)
        var1 = 0
        var8 = 0
        while True:  # loop $label76
            var3 = (var7 + (var8 * 36))
            var4 = (var0 + (var9 << 2))
            i32_store(((var7 + (var8 * 36)) + 269376), i32_load((var0 + (var9 << 2))))
            i32_store((var3 + 269380), i32_load(var4 + 4))
            i32_store((var3 + 269384), i32_load(var4 + 8))
            i32_store((var3 + 269388), i32_load(var4 + 12))
            i32_store((var3 + 269392), i32_load(var4 + 16))
            i32_store((var3 + 269396), i32_load(var4 + 20))
            i32_store((var3 + 269400), i32_load(var4 + 24))
            i32_store((var3 + 269404), i32_load(var4 + 28))
            i32_store((var3 + 269408), i32_load(var4 + 32))
            var9 = (var9 + 9)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != var13 else 0):
                continue
            break  # end loop
        var4 = 0
        while True:  # loop $label77
            var3 = (var7 + 281808)
            i32_store(((var7 + 281808) + (var1 << 2)), i32_load((var0 + ((var1 + var9) << 2))))
            var8 = (var1 | 1)
            i32_store((var3 + ((var1 | 1) << 2)), i32_load((var0 + ((var8 + var9) << 2))))
            var8 = (var1 | 2)
            i32_store((var3 + ((var1 | 2) << 2)), i32_load((var0 + ((var8 + var9) << 2))))
            var8 = (var1 | 3)
            i32_store((var3 + ((var1 | 3) << 2)), i32_load((var0 + ((var8 + var9) << 2))))
            var1 = (var1 + 4)
            var4 = (var4 + 4)
            if (1 if (var4 + 4) != 252 else 0):
                continue
            break  # end loop
        var3 = 0
        while True:  # loop $label78
            i32_store(((var7 + (var1 << 2)) + 281808), i32_load((var0 + ((var1 + var9) << 2))))
            var1 = (var1 + 1)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var21 else 0):
                continue
            break  # end loop
        var3 = (var9 + var13)
        var9 = 0
        var1 = 0
        var8 = 0
        if (1 if var5 == 0 else 0):
            while True:  # loop $label79
                var4 = (var7 + 282828)
                i32_store(((var7 + 282828) + (var1 << 2)), i32_load((var0 + ((var1 + var3) << 2))))
                var16 = (var1 | 1)
                i32_store((var4 + ((var1 | 1) << 2)), i32_load((var0 + ((var3 + var16) << 2))))
                var16 = (var1 | 2)
                i32_store((var4 + ((var1 | 2) << 2)), i32_load((var0 + ((var3 + var16) << 2))))
                var16 = (var1 | 3)
                i32_store((var4 + ((var1 | 3) << 2)), i32_load((var0 + ((var3 + var16) << 2))))
                var1 = (var1 + 4)
                var8 = (var8 + 4)
                if (1 if (var8 + 4) != 252 else 0):
                    continue
                break  # end loop
            while True:  # loop $label80
                i32_store(((var7 + (var1 << 2)) + 282828), i32_load((var0 + ((var1 + var3) << 2))))
                var1 = (var1 + 1)
                var9 = (var9 + 1)
                if (1 if (var9 + 1) != var21 else 0):
                    continue
                break  # end loop
        var3 = (var3 + var13)
        var1 = (var0 + ((var3 + var13) << 2))
        i32_store(var7 + 283848, i32_load((var0 + ((var3 + var13) << 2))))
        i32_store((var7 + 283852), i32_load(var1 + 4))
        i32_store((var7 + 283856), i32_load(var1 + 8))
        i32_store((var7 + 283860), i32_load(var1 + 12))
        i32_store(var7 + 283864, i32_load(var1 + 16))
        i32_store(var7 + 283872, i32_load(var1 + 20))
        i32_store(var7 + 283876, i32_load(var1 + 24))
        i32_store(var7 + 283960, i32_load(var1 + 28))
        i32_store(var7 + 283968, i32_load(var1 + 32))
        i32_store8(var7 + 283972, i32_load(var1 + 36))
        i32_store8((var7 + 283973), ((i32_load(var1 + 36) & 0xFFFFFFFF) >> 8))
        i32_store8((var7 + 283974), i32_load16_u(var1 + 38))
        var3 = (var3 + 10)
        var1 = 0
        var9 = 0
        while True:  # loop $label81
            var4 = (var7 + 283984)
            i32_store(((var7 + 283984) + (var1 << 2)), i32_load((var0 + ((var1 + var3) << 2))))
            var8 = (var1 | 1)
            i32_store((var4 + ((var1 | 1) << 2)), i32_load((var0 + ((var3 + var8) << 2))))
            var8 = (var1 | 2)
            i32_store((var4 + ((var1 | 2) << 2)), i32_load((var0 + ((var3 + var8) << 2))))
            var8 = (var1 | 3)
            i32_store((var4 + ((var1 | 3) << 2)), i32_load((var0 + ((var3 + var8) << 2))))
            var1 = (var1 + 4)
            var9 = (var9 + 4)
            if (1 if (var9 + 4) != var34 else 0):
                continue
            break  # end loop
        var9 = 0
        if var19:
            while True:  # loop $label82
                i32_store(((var7 + (var1 << 2)) + 283984), i32_load((var0 + ((var1 + var3) << 2))))
                var1 = (var1 + 1)
                var9 = (var9 + 1)
                if (1 if (var9 + 1) != var19 else 0):
                    continue
                break  # end loop
        var9 = 39
        if var26:
            while True:  # loop $label83
                var1 = (var9 << 2)
                i32_store((var4 + (var9 << 2)), i32_load((var1 + 9561072)))
                var8 = (var1 + 4)
                i32_store((var4 + (var1 + 4)), i32_load((var8 + 9561072)))
                var8 = (var1 + 8)
                i32_store((var4 + (var1 + 8)), i32_load((var8 + 9561072)))
                var1 = (var1 + 12)
                i32_store((var4 + (var1 + 12)), i32_load((var1 + 9561072)))
                var9 = (var9 + 4)
                if (1 if (var9 + 4) != 155 else 0):
                    continue
                break  # end loop
        var4 = (var7 + 283864)
        if (1 if var37 == 0 else 0):
            var1 = (var3 + var14)
            break
        i32_store((var7 + 284380), 4)
        i64_store((var7 + 284364), 19327352832002)
        i64_store((var7 + 284356), 85899345960)
        i64_store((var7 + 284384), 51539617552)
        i64_store((var7 + 284372), 137438953488)
        var1 = (var3 + var14)
        if var18:
            break
        var3 = (var0 + (var1 << 2))
        i32_store(var7 + 283868, i32_load((var0 + (var1 << 2))))
        i32_store(var7 + 283912, i32_load(var3 + 4))
        i32_store(var7 + 283916, i32_load(var3 + 8))
        i32_store(var7 + 283920, i32_load(var3 + 12))
        i32_store(var7 + 283964, i32_load(var3 + 16))
        i32_store(var7 + 283904, i32_load(var3 + 20))
        i32_store(var7 + 283880, i32_load(var3 + 24))
        var1 = (var1 + 7)
        i32_store(var7 + 283940, i32_load((var0 + ((var1 + 7) << 2))))
        break
        i32_store(var4, i32_load((var0 + (var1 << 2))))
        var3 = (var1 + 1)
        if var23:
            var4 = (var7 + 284616)
            i32_store(var7 + 281804, i32_load((var0 + (var3 << 2))))
            var3 = ((var1 << 2) + var0)
            i32_store(var7 + 283924, i32_load(((var1 << 2) + var0) + 8))
            i32_store(var7 + 283936, i32_load(var3 + 12))
            i32_store(var7 + 283948, i32_load(var3 + 16))
            i32_store(var7 + 283956, i32_load(var3 + 20))
            if (1 if var30 == 0 else 0):
                if (1 if i32_load8_u(9561832) == 0 else 0):
                    break
            i32_store(var4, i32_load(var3 + 24))
            i32_store8(var7 + 286700, (1 if i32_load(var3 + 28) != 0 else 0))
            i32_store8(var7 + 286701, (1 if i32_load(var3 + 32) != 0 else 0))
            var3 = (var1 + 9)
        if (1 if var38 == 0 else 0):
            var1 = (var0 + (var3 << 2))
            i32_store8(var7 + 286699, (1 if i32_load((var0 + (var3 << 2))) != 0 else 0))
            i32_store8(var7 + 92, i32_load(var1 + 4))
            i32_store8(var7 + 93, i32_load(var1 + 8))
            i32_store(var7 + 283964, i32_load(var1 + 12))
            i32_store(var7 + 283952, i32_load(var1 + 16))
            i32_store(var7 + 80, i32_load(var1 + 20))
            i32_store(var7 + 84, i32_load(var1 + 24))
            i32_store(var7 + 88, i32_load(var1 + 28))
            var3 = (var3 + 8)
        if (1 if var36 == 0 else 0):
            var4 = var3
            break
        var4 = (var3 + 1)
        var3 = i32_load((var0 + (var3 << 2)))
        if (1 if i32_load((var0 + (var3 << 2))) == 0 else 0):
            break
        if var5:
            break
        var1 = i32_load(9142892)
        var8 = (i32_load(9142892) << 2)
        var9 = func26((-1 if (1 if var1 > 1073741823 else 0) else (i32_load(9142892) << 2)))
        i32_store(var7 + 281800, func26((-1 if (1 if var1 > 1073741823 else 0) else (i32_load(9142892) << 2))))
        if (1 if var1 == 0 else 0):
            break
        # Unknown: memory.copy []
        var1 = (var0 + (var4 << 2))
        i32_store(var7 + 284608, i32_load((var0 + (var4 << 2))))
        i32_store(var7 + 286684, i32_load(var1 + 4))
        i32_store8(var7 + 286696, (1 if i32_load(var1 + 8) != 0 else 0))
        if (1 if var5 == 0 else 0):
            i32_store(var7 + 283976, i32_load(var1 + 12))
        i32_store(var7 + 283980, i32_load(var1 + 16))
        i32_store(var7 + 286688, i32_load(var1 + 20))
        i32_store(var7 + 283896, i32_load(var1 + 24))
        i32_store(var7 + 283900, i32_load(var1 + 28))
        if var5:
            i32_store8(var7 + 286699, 1)
        var3 = (var4 + 8)
        var12 = (var12 + 1)
        if (1 if (var12 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    break
    func42()
    raise RuntimeError('unreachable')
    func42()
    raise RuntimeError('unreachable')
    var1 = i32_load(9561692)
    i32_store16(var1 + 283972, 65535)
    i32_store8((var1 + 283974), 255)
    var0 = ((25 if (1 if var15 < 473 else 0) else 30) if (1 if var15 < 552 else 0) else (33 if (1 if var15 > 581 else 0) else 32))
    var8 = ((var20 & 0xFFFFFFFF) // ((25 if (1 if var15 < 473 else 0) else 30) if (1 if var15 < 552 else 0) else (33 if (1 if var15 > 581 else 0) else 32)))
    if var5:
        var1 = i32_load(9671136)
        var7 = func26((-1 if (1 if var1 > 1073741823 else 0) else (i32_load(9671136) << 2)))
    var4 = 3
    if (1 if var0 <= var20 else 0):
        var9 = (var10 + (var22 << 2))
        var19 = (1 if (1 if var8 <= 1 else 0) else var8)
        var18 = (var8 << 5)
        var16 = (var8 * 31)
        var17 = (var8 * 30)
        var29 = (var8 * 29)
        var27 = (var8 * 28)
        var25 = (var8 * 27)
        var31 = (var8 * 26)
        var32 = (var8 * 25)
        var36 = (var8 * 24)
        var34 = (var8 * 22)
        var26 = (var8 * 21)
        var37 = (var8 * 20)
        var38 = (var8 * 19)
        var39 = (var8 * 17)
        var40 = (var8 * 15)
        var41 = (var8 * 14)
        var42 = (var8 * 13)
        var43 = (var8 * 12)
        var44 = (var8 * 10)
        var45 = (var8 * 9)
        var46 = (var8 << 3)
        var47 = (var8 * 7)
        var48 = (var8 * 5)
        var49 = (var8 << 2)
        var50 = (var8 << 1)
        var30 = (var8 << 4)
        var51 = (var8 * 11)
        var52 = (var8 * 3)
        var53 = (var8 * 23)
        var12 = i32_load(9671136)
        var54 = (1 if var15 < 473 else 0)
        var55 = (1 if var15 < 582 else 0)
        var0 = 0
        while True:  # loop $label99
            var3 = i32_load((var9 + ((var0 + var52) << 2)))
            if (1 if i32_load((var9 + ((var0 + var52) << 2))) == 0 else 0):
                break
            if (1 if var3 >= var12 else 0):
                break
            var20 = (var9 + ((var0 + var53) << 2))
            var1 = i32_load((var9 + ((var0 + var53) << 2)))
            var14 = ((i32_load((var9 + ((var0 + var53) << 2))) & 0xFFFFFFFF) >> 24)
            if (var5 & (1 if ((i32_load((var9 + ((var0 + var53) << 2))) & 0xFFFFFFFF) >> 24) == 3 else 0)):
                break
            var21 = i32_load((var9 + ((var0 + var51) << 2)))
            if (var5 & (1 if i32_load((var9 + ((var0 + var51) << 2))) == 0 else 0)):
                break
            if (1 if var5 == 0 else 0):
                break
            if (1 if i32_load(9147132) == 0 else 0):
                break
            if (1 if i32_load(38788) != (var1 & 255) else 0):
                break
            if (1 if i32_load((var9 + ((var0 + var30) << 2))) > 2002 else 0):
                break
            if (1 if var5 == 0 else 0):
                var1 = var4
                var4 = var3
                break
            i32_store((var7 + (var3 << 2)), var4)
            var1 = (var4 + 1)
            var3 = (i32_load(9671128) + (var4 * 132))
            i32_store((i32_load(9671128) + (var4 * 132)) + 28, var4)
            var4 = i32_load((var9 + (var0 << 2)))
            if i32_load((var9 + (var0 << 2))):
                var22 = (var10 + (var4 << 2))
                var4 = i32_load((var10 + (var4 << 2)))
                var12 = func26(16)
                i32_store(func26(16) + 4, var4)
                var28 = (var4 << 2)
                var13 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
                i32_store(var12 + 12, 20)
                i32_store(var12, var13)
                i32_store(var12 + 8, var4)
                if var4:
                    # Unknown: memory.copy []
                i32_store(var3 + 16, var12)
            var4 = i32_load((var9 + ((var0 + var8) << 2)))
            if i32_load((var9 + ((var0 + var8) << 2))):
                var22 = (var10 + (var4 << 2))
                var4 = i32_load((var10 + (var4 << 2)))
                var12 = func26(16)
                i32_store(func26(16) + 4, var4)
                var28 = (var4 << 2)
                var13 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
                i32_store(var12 + 12, 20)
                i32_store(var12, var13)
                i32_store(var12 + 8, var4)
                if var4:
                    # Unknown: memory.copy []
                i32_store(var3 + 20, var12)
            var4 = i32_load((var9 + ((var0 + var50) << 2)))
            if i32_load((var9 + ((var0 + var50) << 2))):
                var22 = (var10 + (var4 << 2))
                var4 = i32_load((var10 + (var4 << 2)))
                if (1 if i32_load(var3 + 24) == 0 else 0):
                    var12 = func26(16)
                    i64_store(func26(16), 0)
                    i64_store(var12 + 8, 0)
                    i32_store(var3 + 24, var12)
                var12 = func26(16)
                i32_store(func26(16) + 4, var4)
                var28 = (var4 << 2)
                var13 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
                i32_store(var12 + 12, 20)
                i32_store(var12, var13)
                i32_store(var12 + 8, var4)
                if var4:
                    # Unknown: memory.copy []
                i32_store(i32_load(var3 + 24), var12)
            i32_store(var3 + 32, i32_load((var9 + ((var0 + var49) << 2))))
            i32_store(var3 + 36, i32_load((var9 + ((var0 + var48) << 2))))
            i32_store(var3 + 44, i32_load((var9 + ((var0 + var47) << 2))))
            i32_store(var3 + 92, i32_load((var9 + ((var0 + var46) << 2))))
            i32_store(var3 + 52, i32_load((var9 + ((var0 + var45) << 2))))
            var4 = i32_load((var9 + ((var0 + var44) << 2)))
            i32_store(var3 + 64, var21)
            i32_store(var3 + 60, var4)
            i32_store(var3 + 68, i32_load((var9 + ((var0 + var43) << 2))))
            i32_store(var3 + 72, i32_load((var9 + ((var0 + var42) << 2))))
            i32_store(var3 + 76, i32_load((var9 + ((var0 + var41) << 2))))
            i32_store(var3 + 80, i32_load((var9 + ((var0 + var40) << 2))))
            i32_store(var3 + 84, i32_load((var9 + ((var0 + var30) << 2))))
            i32_store(var3 + 88, i32_load((var9 + ((var0 + var39) << 2))))
            i32_store(var3 + 108, i32_load((var9 + ((var0 + var38) << 2))))
            i32_store(var3 + 112, i32_load((var9 + ((var0 + var37) << 2))))
            i32_store(var3 + 116, i32_load((var9 + ((var0 + var26) << 2))))
            i32_store16(var3 + 120, i32_load((var9 + ((var0 + var34) << 2))))
            var4 = i32_load(var20)
            i32_store8(var3 + 125, var14)
            i32_store8(var3 + 122, var4)
            i32_store8(var3 + 124, ((var4 & 0xFFFFFFFF) >> 16))
            i32_store8(var3 + 123, ((var4 & 0xFFFFFFFF) >> 8))
            var4 = i32_load((var9 + ((var0 + var36) << 2)))
            i32_store16(var3 + 126, i32_load((var9 + ((var0 + var36) << 2))))
            var12 = i32_load(9671136)
            if (1 if i32_load8_u(9142916) == 0 else 0):
                break
            var13 = (((var4 & 0xFFFFFFFF) >> 8) & 255)
            if (1 if (((var4 & 0xFFFFFFFF) >> 8) & 255) > 12 else 0):
                break
            if (1 if ((1 << var13) & 7184) == 0 else 0):
                break
            i32_store8(var3 + 127, 0)
            i32_store8(var3 + 129, ((var4 & 0xFFFFFFFF) >> 24))
            i32_store8(var3 + 128, ((var4 & 0xFFFFFFFF) >> 16))
            if var54:
                break
            i32_store(var3 + 96, i32_load((var9 + ((var0 + var32) << 2))))
            i32_store(var3 + 56, i32_load((var9 + ((var0 + var31) << 2))))
            var4 = i32_load((var9 + ((var0 + var25) << 2)))
            if i32_load((var9 + ((var0 + var25) << 2))):
                var14 = (var10 + (var4 << 2))
                var4 = i32_load((var10 + (var4 << 2)))
                if (1 if i32_load(var3 + 24) == 0 else 0):
                    var13 = func26(16)
                    i64_store(func26(16), 0)
                    i64_store(var13 + 8, 0)
                    i32_store(var3 + 24, var13)
                var13 = func26(16)
                i32_store(func26(16) + 4, var4)
                var21 = (var4 << 2)
                var20 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
                i32_store(var13 + 12, 20)
                i32_store(var13, var20)
                i32_store(var13 + 8, var4)
                if var4:
                    # Unknown: memory.copy []
                i32_store(i32_load(var3 + 24) + 12, var13)
            var4 = i32_load((var9 + ((var0 + var27) << 2)))
            if i32_load((var9 + ((var0 + var27) << 2))):
                var14 = (var10 + (var4 << 2))
                var4 = i32_load((var10 + (var4 << 2)))
                if (1 if i32_load(var3 + 24) == 0 else 0):
                    var13 = func26(16)
                    i64_store(func26(16), 0)
                    i64_store(var13 + 8, 0)
                    i32_store(var3 + 24, var13)
                var13 = func26(16)
                i32_store(func26(16) + 4, var4)
                var21 = (var4 << 2)
                var20 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
                i32_store(var13 + 12, 20)
                i32_store(var13, var20)
                i32_store(var13 + 8, var4)
                if var4:
                    # Unknown: memory.copy []
                i32_store(i32_load(var3 + 24) + 8, var13)
            var4 = i32_load((var9 + ((var0 + var29) << 2)))
            if (1 if i32_load((var9 + ((var0 + var29) << 2))) == 0 else 0):
                break
            var14 = (var10 + (var4 << 2))
            var13 = i32_load((var10 + (var4 << 2)))
            if (1 if i32_load(var3 + 24) == 0 else 0):
                var4 = func26(16)
                i64_store(func26(16), 0)
                i64_store(var4 + 8, 0)
                i32_store(var3 + 24, var4)
            var4 = func26(16)
            i32_store(func26(16) + 4, var13)
            var21 = (var13 << 2)
            var20 = func26((-1 if (1 if var13 > 1073741823 else 0) else (var13 << 2)))
            i32_store(var4 + 12, 20)
            i32_store(var4, var20)
            i32_store(var4 + 8, var13)
            if (1 if var13 == 0 else 0):
                i32_store(i32_load(var3 + 24) + 4, var4)
                break
            # Unknown: memory.copy []
            i32_store(i32_load(var3 + 24) + 4, var4)
            var22 = ((((var13 - 1) & 0xFFFFFFFF) >> 1) + 1)
            var21 = (((((var13 - 1) & 0xFFFFFFFF) >> 1) + 1) & 3)
            var14 = 0
            var4 = 0
            if (1 if var13 >= 7 else 0):
                var28 = (var22 & -4)
                var22 = 0
                while True:  # loop $label97
                    var13 = (var4 << 2)
                    i32_store((var20 + ((var4 << 2) | 4)), 0)
                    i32_store((var20 + (var13 | 12)), 0)
                    i32_store((var20 + (var13 | 20)), 0)
                    i32_store((var20 + (var13 | 28)), 0)
                    var4 = (var4 + 8)
                    var22 = (var22 + 4)
                    if (1 if (var22 + 4) != var28 else 0):
                        continue
                    break  # end loop
            if (1 if var21 == 0 else 0):
                break
            while True:  # loop $label98
                i32_store((var20 + ((var4 << 2) | 4)), 0)
                var4 = (var4 + 2)
                var14 = (var14 + 1)
                if (1 if (var14 + 1) != var21 else 0):
                    continue
                break  # end loop
            if var23:
                i32_store(var3 + 100, i32_load((var9 + ((var0 + var17) << 2))))
                i32_store(var3 + 104, i32_load((var9 + ((var0 + var16) << 2))))
            if var55:
                break
            i32_store8(var3 + 130, i32_load((var9 + ((var0 + var18) << 2))))
            var4 = var1
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var19 else 0):
                continue
            break  # end loop
    if i32_load(9142848):
        break
    if (1 if var15 > 518 else 0):
        break
    if (1 if var24 == 0 else 0):
        var1 = i32_load(9215884)
        var0 = 0
        while True:  # loop $label101
            var3 = (var0 << 2)
            if (1 if i32_load((var1 + ((var0 << 2) | 4))) == 22 else 0):
                i32_store((var1 + var3), 0)
            var0 = (var0 + 4)
            if (1 if (var0 + 4) < var6 else 0):
                continue
            break  # end loop
    var0 = i32_load(9671136)
    if (1 if i32_load(9671136) < 4 else 0):
        break
    var23 = (var0 - 3)
    var3 = ((var0 - 3) & 7)
    var6 = i32_load(9671128)
    var1 = 3
    if (1 if (var0 - 4) >= 7 else 0):
        var23 = (var23 & -8)
        var9 = 0
        while True:  # loop $label102
            var0 = (var6 + (var1 * 132))
            i32_store((var6 + (var1 * 132)) + 44, 0)
            i32_store(var0 + 176, 0)
            i32_store(var0 + 308, 0)
            i32_store(var0 + 440, 0)
            i32_store(var0 + 572, 0)
            i32_store(var0 + 704, 0)
            i32_store(var0 + 836, 0)
            i32_store(var0 + 968, 0)
            var1 = (var1 + 8)
            var9 = (var9 + 8)
            if (1 if (var9 + 8) != var23 else 0):
                continue
            break  # end loop
    if (1 if var3 == 0 else 0):
        break
    var0 = 0
    while True:  # loop $label103
        i32_store((var6 + (var1 * 132)) + 44, 0)
        var1 = (var1 + 1)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var3 else 0):
            continue
        break  # end loop
    if var35:
        var3 = (var10 + (var33 << 2))
        var23 = i32_load(9671128)
        var1 = 0
        while True:  # loop $label104
            var6 = (var1 << 2)
            var8 = i32_load((var3 + (var1 << 2)))
            if i32_load((var3 + (var1 << 2))):
                if var5:
                    i32_store((var7 + (var8 << 2)), var4)
                    var8 = var4
                    var4 = (var4 + 1)
                var0 = (var23 + (var8 * 132))
                i32_store((var23 + (var8 * 132)) + 28, var8)
                i32_store(var0 + 64, i32_load((var3 + (var6 | 4))))
                i32_store(var0 + 68, i32_load(((i32_load(38448) * 404) + 9568096) + 104))
                i32_store8(var0 + 124, i32_load((var3 + (var6 | 8))))
                i32_store(var0 + 112, i32_load((var3 + (var6 | 12))))
                i32_store8(var0 + 122, i32_load(38448))
            var1 = (var1 + 4)
            if (1 if (var1 + 4) < var35 else 0):
                continue
            break  # end loop
    if (1 if var5 == 0 else 0):
        break
    i32_store(9671136, var4)
    if (1 if var4 >= 4 else 0):
        var3 = i32_load(9671128)
        var9 = 3
        while True:  # loop $label108
            var0 = (var3 + (var9 * 132))
            var1 = i32_load((var3 + (var9 * 132)) + 36)
            if i32_load((var3 + (var9 * 132)) + 36):
                i32_store(var0 + 36, i32_load((var7 + (var1 << 2))))
            var1 = i32_load(var0 + 16)
            if (1 if i32_load(var0 + 16) == 0 else 0):
                break
            if (1 if i32_load(var1 + 8) == 0 else 0):
                break
            var4 = i32_load(var1)
            var0 = 0
            while True:  # loop $label107
                var5 = (var4 + (var0 << 2))
                i32_store((var4 + (var0 << 2)), i32_load((var7 + (i32_load(var5) << 2))))
                var0 = (var0 + 1)
                if (1 if (var0 + 1) < i32_load(var1 + 8) else 0):
                    continue
                break  # end loop
            var4 = i32_load(9671136)
            var9 = (var9 + 1)
            if (1 if (var9 + 1) < var4 else 0):
                continue
            break  # end loop
    if (1 if var7 == 0 else 0):
        break
    var7 = 1
    if (1 if var2 == 0 else 0):
        break
    i32_store(var11 + 32, (i32_load(9142892) - 1))
    var3 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var0 = i32_load(9561692)
    if (1 if i32_load((i32_load(9561692) + 570612)) == 0 else 0):
        break
    var1 = 1
    while True:  # loop $label110
        var0 = (var0 + (var1 * 286704))
        var2 = i32_load8_u((var0 + (var1 * 286704)) + 283972)
        var3 = i32_load8_u((var0 + 283974))
        var4 = i32_load8_u((var0 + 283973))
        i32_store(var11 + 20, i32_load(var0 + 284608))
        i32_store(var11 + 16, var0)
        i32_store(var11 + 24, ((var3 | (var4 << 8)) | (var2 << 16)))
        var1 = (var1 + 1)
        var3 = i32_load(9142892)
        if (1 if (var1 + 1) >= i32_load(9142892) else 0):
            break
        var0 = i32_load(9561692)
        if i32_load((i32_load(9561692) + (var1 * 286704)) + 283908):
            continue
        break  # end loop
    i32_store(var11, (var3 - 1))
    global global0
    global0 = (var11 + 400)
    return var7

