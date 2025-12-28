"""
Auto-generated from WAT. Contains 4 functions.
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
# $func426
# ==========================================================
def func426(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var8 = i32_load(9561692)
    var2 = (i32_load(9561692) + (var0 * 286704))
    var4 = i32_load((i32_load(9561692) + (var0 * 286704)) + 281792)
    if i32_load((i32_load(9561692) + (var0 * 286704)) + 281792):
        var1 = i32_load(var4)
        break
    var4 = func26(16)
    i32_store(func26(16) + 4, 8)
    var1 = func26(32)
    i32_store(var4, func26(32))
    i64_store(var4 + 8, 4294967296)
    i32_store((var2 + 281792), var4)
    var9 = i64_load(var1 + 8)
    i64_store(var1 + 4, i64_load(var1))
    var10 = i64_load(var1 + 16)
    i64_store(var1 + 12, var9)
    var2 = i32_load(var1 + 24)
    i64_store(var1 + 20, var10)
    i32_store(var1 + 28, var2)
    var6 = i32_load(9147316)
    var2 = i32_load(9147320)
    var7 = i32_load(9147312)
    var3 = i32_load(9147324)
    var3 = ((i32_load(9147324) << 11) ^ var3)
    var3 = (((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var3) & 0xFFFFFFFF) >> 8)) ^ var7) ^ var3)
    var5 = ((((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var3) & 0xFFFFFFFF) >> 8)) ^ var7) ^ var3) & 3)
    if (1 if ((((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var3) & 0xFFFFFFFF) >> 8)) ^ var7) ^ var3) & 3) <= 1 else 0):
        var2 = ((var2 << 11) ^ var2)
        var2 = (((((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8) ^ ((var3 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var3)
        var5 = i32_load(((((((((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8) ^ ((var3 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var3) % 18) << 2) + 9681984))
        i32_store(9147320, var3)
        i32_store(9147324, var7)
        i32_store(9147316, var2)
        var3 = ((var6 << 11) ^ var6)
        var2 = (((((((var6 << 11) ^ var6) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var3) ^ var2)
        i32_store(9147312, (((((((var6 << 11) ^ var6) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var3) ^ var2))
        var2 = (var2 % 11)
        break
    var2 = ((var2 << 11) ^ var2)
    var2 = (((((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8) ^ ((var3 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var3)
    if (1 if var5 == 2 else 0):
        var5 = i32_load((((var2 % 5) << 2) + 9682064))
        i32_store(9147324, var7)
        i32_store(9147320, var3)
        i32_store(9147316, var2)
        var3 = ((var6 << 11) ^ var6)
        var2 = (((((((var6 << 11) ^ var6) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var3) ^ var2)
        i32_store(9147312, (((((((var6 << 11) ^ var6) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var3) ^ var2))
        if (1 if var5 == i32_load(38964) else 0):
            break
        if (1 if var5 == i32_load(38980) else 0):
            break
        break
        break
    var5 = i32_load((((var2 % 3) << 2) + 9682084))
    i32_store(9147320, var3)
    i32_store(9147324, var7)
    i32_store(9147316, var2)
    var3 = ((var6 << 11) ^ var6)
    var2 = (((((((var6 << 11) ^ var6) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var3) ^ var2)
    i32_store(9147312, (((((((var6 << 11) ^ var6) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var3) ^ var2))
    var2 = ((var2 % 21) + 5)
    i32_store(var1, ((var2 << 16) + var5))
    var1 = i32_load(var4 + 8)
    if (1 if i32_load(var4 + 8) <= 7 else 0):
        i32_store(var4 + 8, (var1 + 1))
    if (1 if i32_load(9671124) != 240 else 0):
        break
    if (1 if i32_load(9142872) != var0 else 0):
        break
    func221(var1)
    return ((var2 % 71) + 30)


# ==========================================================
# $Xb
# Export: Xb
# ==========================================================
def Xb(var0):
    """Export: Xb"""
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
    var6 = i32_load(9142892)
    var3 = (i32_load(9142892) + 1)
    i32_store(9142892, (i32_load(9142892) + 1))
    var12 = (i64_extend_u(var3) * 286704)
    var3 = (-1 if i32(((var12 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var3) * 286704)))
    var4 = func26((-1 if i32(((var12 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var3) * 286704))))
    # Unknown: memory.fill []
    var1 = i32_load(9561692)
    if var6:
        if (1 if var6 >= 4 else 0):
            var5 = (var6 & -4)
            var3 = 0
            while True:  # loop $label0
                var7 = (var2 * 286704)
                # Unknown: memory.copy []
                var7 = ((var2 | 1) * 286704)
                # Unknown: memory.copy []
                var7 = ((var2 | 2) * 286704)
                # Unknown: memory.copy []
                var7 = ((var2 | 3) * 286704)
                # Unknown: memory.copy []
                var2 = (var2 + 4)
                var3 = (var3 + 4)
                if (1 if (var3 + 4) != var5 else 0):
                    continue
                break  # end loop
        var6 = (var6 & 3)
        if (1 if (var6 & 3) == 0 else 0):
            break
        var3 = 0
        while True:  # loop $label2
            var5 = (var2 * 286704)
            # Unknown: memory.copy []
            var2 = (var2 + 1)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var6 else 0):
                continue
            break  # end loop
        break
    if var1:
        break
    var3 = 0
    i32_store(9561692, var4)
    var2 = (var4 + (var6 * 286704))
    var6 = 1
    break
    i32_store(9561692, var4)
    var6 = i32_load(9142892)
    var3 = (i32_load(9142892) - 1)
    var2 = (var4 + ((i32_load(9142892) - 1) * 286704))
    if (1 if var3 <= 8 else 0):
        break
    var12 = i64_load(9147316)
    var1 = i32_load(9147312)
    i32_store(9147316, i32_load(9147312))
    var5 = i32_load(9147324)
    i64_store(9147320, var12)
    var5 = (var5 ^ (var5 << 11))
    var1 = ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var5 ^ (var5 << 11)) & 0xFFFFFFFF) >> 8))) ^ var5)
    i32_store(9147312, ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var5 ^ (var5 << 11)) & 0xFFFFFFFF) >> 8))) ^ var5))
    break
    var5 = i32_load(((var6 << 2) + 42120))
    var1 = (var4 + (var3 * 286704))
    var7 = (100 if (1 if var3 != 1 else 0) else 0)
    i32_store((var4 + (var3 * 286704)) + 286688, (100 if (1 if var3 != 1 else 0) else 0))
    i32_store(var1 + 286684, var7)
    i32_store8(var1 + 283972, ((var5 & 0xFFFFFFFF) >> 16))
    i32_store(var1 + 283960, 3)
    i32_store8((var1 + 283974), var5)
    i32_store8((var1 + 283973), ((var5 & 0xFFFFFFFF) >> 8))
    var1 = (var6 * 20)
    var5 = ((var6 * 20) - 60)
    if (1 if ((var6 * 20) - 60) < i32_load16_u(9142944) else 0):
        var7 = i32_load(9142928)
        i32_store16(var2, i32_load16_u((i32_load(9142928) + (var5 << 1))))
        var1 = (var7 + (var1 << 1))
        i32_store16(var2 + 2, i32_load16_u(((var7 + (var1 << 1)) - 118)))
        i32_store16(var2 + 4, i32_load16_u((var1 - 116)))
        i32_store16(var2 + 6, i32_load16_u((var1 - 114)))
        i32_store16(var2 + 8, i32_load16_u((var1 - 112)))
        i32_store16(var2 + 10, i32_load16_u((var1 - 110)))
        i32_store16(var2 + 12, i32_load16_u((var1 - 108)))
        i32_store16(var2 + 14, i32_load16_u((var1 - 106)))
        i32_store16(var2 + 16, i32_load16_u((var1 - 104)))
        i32_store16(var2 + 18, i32_load16_u((var1 - 102)))
        i32_store16(var2 + 20, i32_load16_u((var1 - 100)))
        i32_store16(var2 + 22, i32_load16_u((var1 - 98)))
        i32_store16(var2 + 24, i32_load16_u((var1 - 96)))
        i32_store16(var2 + 26, i32_load16_u((var1 - 94)))
        i32_store16(var2 + 28, i32_load16_u((var1 - 92)))
        i32_store16(var2 + 30, i32_load16_u((var1 - 90)))
        i32_store16(var2 + 32, i32_load16_u((var1 - 88)))
        i32_store16(var2 + 34, i32_load16_u((var1 - 86)))
        i32_store16(var2 + 36, i32_load16_u((var1 - 84)))
        i32_store16(var2 + 38, i32_load16_u((var1 - 82)))
        break
    var1 = (var4 + (var3 * 286704))
    i32_store((var4 + (var3 * 286704)) + 284608, var3)
    i32_store(var1 + 283908, var3)
    i32_store(var1 + 283868, i32_load(9561460))
    # Unknown: memory.copy []
    var2 = i32_load(9142424)
    i32_store((var1 + 284000), i32_load(i32_load(9142424) + 40))
    i32_store((var1 + 284136), i32_load(var2 + 36))
    if (1 if var6 >= 3 else 0):
        i32_store(var1 + 283848, i32_load((var4 + 570552)))
        i32_store((var1 + 283852), i32_load((var4 + 570556)))
        i32_store((var1 + 283856), i32_load((var4 + 570560)))
        i32_store((var1 + 283860), i32_load((var4 + 570564)))
    var3 = i32_load(9142892)
    if i32_load(9142892):
        var2 = i32_load(9561692)
        var5 = 0
        while True:  # loop $label10
            var1 = (var2 + (var5 * 286704))
            if i32_load((var2 + (var5 * 286704)) + 281800):
                var2 = (-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2))
                var4 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
                # Unknown: memory.fill []
                var10 = (var1 + 281800)
                var1 = i32_load((var1 + 281800))
                var7 = (var3 - 1)
                if (var3 - 1):
                    var9 = 0
                    var2 = 0
                    if (1 if (var3 - 2) >= 3 else 0):
                        var11 = (var7 & -4)
                        var6 = 0
                        while True:  # loop $label6
                            var3 = (var2 << 2)
                            i32_store((var4 + (var2 << 2)), i32_load((var1 + var3)))
                            var8 = (var3 | 4)
                            i32_store((var4 + (var3 | 4)), i32_load((var1 + var8)))
                            var8 = (var3 | 8)
                            i32_store((var4 + (var3 | 8)), i32_load((var1 + var8)))
                            var3 = (var3 | 12)
                            i32_store((var4 + (var3 | 12)), i32_load((var1 + var3)))
                            var2 = (var2 + 4)
                            var6 = (var6 + 4)
                            if (1 if (var6 + 4) != var11 else 0):
                                continue
                            break  # end loop
                    var3 = (var7 & 3)
                    if (1 if (var7 & 3) == 0 else 0):
                        break
                    while True:  # loop $label8
                        var6 = (var2 << 2)
                        i32_store((var4 + (var2 << 2)), i32_load((var1 + var6)))
                        var2 = (var2 + 1)
                        var9 = (var9 + 1)
                        if (1 if (var9 + 1) != var3 else 0):
                            continue
                        break  # end loop
                    break
                if (1 if var1 == 0 else 0):
                    break
                var3 = i32_load(9142892)
                i32_store(var10, var4)
                var2 = i32_load(9561692)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) < var3 else 0):
                continue
            break  # end loop
    if (1 if var0 != 5 else 0):
    func284(0)
    return 0


# ==========================================================
# $func493
# ==========================================================
def func493(var0, var1):
    var2 = 0
    var2 = i32_load(9671128)
    var1 = (i32_load(9671128) + (var0 * 132))
    i32_store8((i32_load(9671128) + (var0 * 132)) + 126, 0)
    i32_store(var1 + 52, (i32_load(var1 + 52) - (((i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 296) * i32_load(((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 284144))) & 0xFFFFFFFF) // 100)))
    if (1 if i32_load(var1 + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var2 + (var0 * 132)) + 28) else 0):
            break


# ==========================================================
# $nd
# Export: nd
# ==========================================================
def nd(var0):
    """Export: nd"""
    var1 = 0
    if (1 if var0 == 0 else 0):
        break
    var1 = i32_load(9681936)
    if (1 if i32_load(9681936) == 0 else 0):
        break
    if i32_load(var1 + 8):
        var0 = 0
        while True:  # loop $label1
            func38(i32_load((i32_load(var1) + ((var0 << 2) | 12))))
            var0 = (var0 + 4)
            var1 = i32_load(9681936)
            if (1 if (var0 + 4) < i32_load(i32_load(9681936) + 8) else 0):
                continue
            break  # end loop
    i32_store(var1 + 8, 0)
    return i32_load(9147288)

