"""
Auto-generated from WAT. Contains 8 functions.
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
# $func1068
# ==========================================================
def func1068(var0):
    var1 = 0
    var1 = (i64_load8_u(var0 + 31) * 72340172838076673)
    i64_store(var0 + 32, (i64_load8_u(var0 + 31) * 72340172838076673))
    i64_store(var0 + 40, var1)
    var1 = (i64_load8_u(var0 + 63) * 72340172838076673)
    i64_store(var0 + 64, (i64_load8_u(var0 + 63) * 72340172838076673))
    i64_store(var0 + 72, var1)
    var1 = (i64_load8_u(var0 + 95) * 72340172838076673)
    i64_store(var0 + 96, (i64_load8_u(var0 + 95) * 72340172838076673))
    i64_store(var0 + 104, var1)
    var1 = (i64_load8_u(var0 + 127) * 72340172838076673)
    i64_store(var0 + 128, (i64_load8_u(var0 + 127) * 72340172838076673))
    i64_store(var0 + 136, var1)
    var1 = (i64_load8_u(var0 + 159) * 72340172838076673)
    i64_store(var0 + 168, (i64_load8_u(var0 + 159) * 72340172838076673))
    i64_store(var0 + 160, var1)
    var1 = (i64_load8_u((var0 - 1)) * 72340172838076673)
    i64_store(var0, (i64_load8_u((var0 - 1)) * 72340172838076673))
    i64_store(var0 + 8, var1)
    var1 = (i64_load8_u(var0 + 191) * 72340172838076673)
    i64_store(var0 + 200, (i64_load8_u(var0 + 191) * 72340172838076673))
    i64_store(var0 + 192, var1)
    var1 = (i64_load8_u(var0 + 223) * 72340172838076673)
    i64_store(var0 + 232, (i64_load8_u(var0 + 223) * 72340172838076673))
    i64_store(var0 + 224, var1)
    var1 = (i64_load8_u(var0 + 255) * 72340172838076673)
    i64_store(var0 + 264, (i64_load8_u(var0 + 255) * 72340172838076673))
    i64_store(var0 + 256, var1)
    var1 = (i64_load8_u(var0 + 287) * 72340172838076673)
    i64_store(var0 + 296, (i64_load8_u(var0 + 287) * 72340172838076673))
    i64_store(var0 + 288, var1)
    var1 = (i64_load8_u(var0 + 319) * 72340172838076673)
    i64_store(var0 + 328, (i64_load8_u(var0 + 319) * 72340172838076673))
    i64_store(var0 + 320, var1)
    var1 = (i64_load8_u(var0 + 351) * 72340172838076673)
    i64_store(var0 + 360, (i64_load8_u(var0 + 351) * 72340172838076673))
    i64_store(var0 + 352, var1)
    var1 = (i64_load8_u(var0 + 383) * 72340172838076673)
    i64_store(var0 + 392, (i64_load8_u(var0 + 383) * 72340172838076673))
    i64_store(var0 + 384, var1)
    var1 = (i64_load8_u(var0 + 415) * 72340172838076673)
    i64_store(var0 + 424, (i64_load8_u(var0 + 415) * 72340172838076673))
    i64_store(var0 + 416, var1)
    var1 = (i64_load8_u(var0 + 447) * 72340172838076673)
    i64_store(var0 + 456, (i64_load8_u(var0 + 447) * 72340172838076673))
    i64_store(var0 + 448, var1)
    var1 = (i64_load8_u(var0 + 479) * 72340172838076673)
    i64_store(var0 + 488, (i64_load8_u(var0 + 479) * 72340172838076673))
    i64_store(var0 + 480, var1)


# ==========================================================
# $func1069
# ==========================================================
def func1069(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var3 = i32_load8_u(var0 + 31)
    var4 = i32_load8_u(var0 + 63)
    var2 = ((((i32_load8_u(var0 + 31) + i32_load8_u(var0 + 63)) + 1) & 0xFFFFFFFF) >> 1)
    i32_store8(var0 + 98, ((((i32_load8_u(var0 + 31) + i32_load8_u(var0 + 63)) + 1) & 0xFFFFFFFF) >> 1))
    var7 = i32_load8_u(var0 + 95)
    i32_store8(var0 + 96, ((((var4 + i32_load8_u(var0 + 95)) + 1) & 0xFFFFFFFF) >> 1))
    i32_store8(var0 + 64, var2)
    var6 = i32_load8_u((var0 - 1))
    var1 = (i32_load8_u((var0 - 1)) + 1)
    var2 = i32_load8_u((var0 - 33))
    var5 = ((((i32_load8_u((var0 - 1)) + 1) + i32_load8_u((var0 - 33))) & 0xFFFFFFFF) >> 1)
    i32_store8(var0 + 34, ((((i32_load8_u((var0 - 1)) + 1) + i32_load8_u((var0 - 33))) & 0xFFFFFFFF) >> 1))
    var1 = (((var1 + var3) & 0xFFFFFFFF) >> 1)
    i32_store8(var0 + 66, (((var1 + var3) & 0xFFFFFFFF) >> 1))
    i32_store8(var0, var5)
    i32_store8(var0 + 32, var1)
    var1 = i32_load8_u((var0 - 32))
    var5 = (var6 + 2)
    var8 = (((i32_load8_u((var0 - 32)) + ((var6 + 2) + (var2 << 1))) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 35, (((i32_load8_u((var0 - 32)) + ((var6 + 2) + (var2 << 1))) & 0xFFFFFFFF) >> 2))
    var9 = i32_load8_u((var0 - 31))
    i32_store8(var0 + 3, ((((i32_load8_u((var0 - 30)) + (var1 + (i32_load8_u((var0 - 31)) << 1))) + 2) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 2, ((((var9 + (var2 + (var1 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    var1 = (var3 + 2)
    var2 = (((var2 + ((var3 + 2) + (var6 << 1))) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 67, (((var2 + ((var3 + 2) + (var6 << 1))) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 1, var8)
    var3 = ((((var4 + var5) + (var3 << 1)) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 99, ((((var4 + var5) + (var3 << 1)) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 33, var2)
    i32_store8(var0 + 97, ((((var1 + var7) + (var4 << 1)) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 65, var3)


# ==========================================================
# $func1070
# ==========================================================
def func1070(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    if (1 if var0 == 0 else 0):
        if (1 if var3 <= 0 else 0):
            break
        var0 = (var3 & 3)
        if (1 if var3 >= 4 else 0):
            var8 = (var3 & -4)
            var3 = 0
            while True:  # loop $label1
                var5 = (i32_load8_u((var1 + var4)) + var5)
                i32_store8((var2 + var4), (i32_load8_u((var1 + var4)) + var5))
                var7 = (var4 | 1)
                var5 = (i32_load8_u((var1 + var7)) + var5)
                i32_store8((var2 + (var4 | 1)), (i32_load8_u((var1 + var7)) + var5))
                var7 = (var4 | 2)
                var5 = (i32_load8_u((var1 + var7)) + var5)
                i32_store8((var2 + (var4 | 2)), (i32_load8_u((var1 + var7)) + var5))
                var7 = (var4 | 3)
                var5 = (i32_load8_u((var1 + var7)) + var5)
                i32_store8((var2 + (var4 | 3)), (i32_load8_u((var1 + var7)) + var5))
                var4 = (var4 + 4)
                var3 = (var3 + 4)
                if (1 if (var3 + 4) != var8 else 0):
                    continue
                break  # end loop
        if (1 if var0 == 0 else 0):
            break
        while True:  # loop $label2
            var5 = (i32_load8_u((var1 + var4)) + var5)
            i32_store8((var2 + var4), (i32_load8_u((var1 + var4)) + var5))
            var4 = (var4 + 1)
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != var0 else 0):
                continue
            break  # end loop
        break
    if (1 if var3 <= 0 else 0):
        break
    var5 = i32_load8_u(var0)
    var6 = i32_load8_u(var0)
    while True:  # loop $label3
        var6 = i32_load8_u((var0 + var4))
        var5 = (((var5 & 255) - (var6 & 255)) + i32_load8_u((var0 + var4)))
        var5 = ((((var5 & 255) - (var6 & 255)) + i32_load8_u((var0 + var4))) if (1 if var5 > 0 else 0) else 0)
        var5 = (i32_load8_u((var1 + var4)) + (255 if (1 if var5 >= 255 else 0) else ((((var5 & 255) - (var6 & 255)) + i32_load8_u((var0 + var4))) if (1 if var5 > 0 else 0) else 0)))
        i32_store8((var2 + var4), (i32_load8_u((var1 + var4)) + (255 if (1 if var5 >= 255 else 0) else ((((var5 & 255) - (var6 & 255)) + i32_load8_u((var0 + var4))) if (1 if var5 > 0 else 0) else 0))))
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var3 else 0):
            continue
        break  # end loop


# ==========================================================
# $func1074
# ==========================================================
def func1074(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if (1 if var2 <= 0 else 0):
        break
    var5 = (var2 & 3)
    if (1 if var2 >= 4 else 0):
        var7 = (var2 & -4)
        var2 = 0
        while True:  # loop $label1
            i32_store8((var1 + var3), ((i32_load((var0 + (var3 << 2))) & 0xFFFFFFFF) >> 8))
            var4 = (var3 | 1)
            i32_store8((var1 + (var3 | 1)), ((i32_load((var0 + (var4 << 2))) & 0xFFFFFFFF) >> 8))
            var4 = (var3 | 2)
            i32_store8((var1 + (var3 | 2)), ((i32_load((var0 + (var4 << 2))) & 0xFFFFFFFF) >> 8))
            var4 = (var3 | 3)
            i32_store8((var1 + (var3 | 3)), ((i32_load((var0 + (var4 << 2))) & 0xFFFFFFFF) >> 8))
            var3 = (var3 + 4)
            var2 = (var2 + 4)
            if (1 if (var2 + 4) != var7 else 0):
                continue
            break  # end loop
    if (1 if var5 == 0 else 0):
        break
    while True:  # loop $label2
        i32_store8((var1 + var3), ((i32_load((var0 + (var3 << 2))) & 0xFFFFFFFF) >> 8))
        var3 = (var3 + 1)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) != var5 else 0):
            continue
        break  # end loop


# ==========================================================
# $func1075
# ==========================================================
def func1075(var0, var1, var2, var3, var4, var5):
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
    var6 = 1
    if (1 if var3 <= 0 else 0):
        break
    if (1 if var2 <= 0 else 0):
        break
    var14 = (var2 & -4)
    var12 = (var2 & 3)
    var6 = 255
    var15 = (1 if var2 < 4 else 0)
    while True:  # loop $label3
        var2 = 0
        var7 = 0
        if (1 if var15 == 0 else 0):
            while True:  # loop $label1
                var8 = i32_load8_u((var0 + (var2 << 2)))
                i32_store8((var2 + var4), i32_load8_u((var0 + (var2 << 2))))
                var9 = (var2 | 1)
                var9 = i32_load8_u((var0 + (var9 << 2)))
                i32_store8((var4 + (var2 | 1)), i32_load8_u((var0 + (var9 << 2))))
                var10 = (var2 | 2)
                var10 = i32_load8_u((var0 + (var10 << 2)))
                i32_store8((var4 + (var2 | 2)), i32_load8_u((var0 + (var10 << 2))))
                var11 = (var2 | 3)
                var11 = i32_load8_u((var0 + (var11 << 2)))
                i32_store8((var4 + (var2 | 3)), i32_load8_u((var0 + (var11 << 2))))
                var6 = (var11 & (var10 & (var9 & (var6 & var8))))
                var2 = (var2 + 4)
                var7 = (var7 + 4)
                if (1 if (var7 + 4) != var14 else 0):
                    continue
                break  # end loop
        var7 = 0
        if var12:
            while True:  # loop $label2
                var8 = i32_load8_u((var0 + (var2 << 2)))
                i32_store8((var2 + var4), i32_load8_u((var0 + (var2 << 2))))
                var2 = (var2 + 1)
                var6 = (var6 & var8)
                var7 = (var7 + 1)
                if (1 if (var7 + 1) != var12 else 0):
                    continue
                break  # end loop
        var4 = (var4 + var5)
        var0 = (var0 + var1)
        var13 = (var13 + 1)
        if (1 if (var13 + 1) != var3 else 0):
            continue
        break  # end loop
    var6 = (1 if (var6 & 255) == 255 else 0)
    return var6


# ==========================================================
# $func1081
# ==========================================================
def func1081(var0, var1):
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
    var2 = i32_load(var0 + 20)
    var9 = i32_load(var0 + 32)
    var5 = i32_load(var0 + 24)
    var6 = i32_load(var0 + 28)
    var10 = i32_load(var0 + 36)
    var3 = i32_load(var1)
    var1 = i32_load(var3 + 20)
    var4 = (i32_load(i32_load(var1) + 16) + (i32_load(var3 + 20) * i32_load(var0 + 8)))
    var7 = i32_load(var0 + 12)
    var3 = i32_load(((i32_load(var3) << 2) + 9687952))
    var8 = i32_load(var0 + 16)
    if (1 if i32_load(var0 + 16) <= 0 else 0):
        break
    if (1 if var8 != 1 else 0):
        var12 = (var8 & -2)
        while True:  # loop $label1
            # call_indirect via table[var3]
            var2 = (var2 + var9)
            var4 = (var1 + var4)
            # call_indirect via table[var3]
            var5 = (var5 + var10)
            var6 = (var6 + var10)
            var4 = (var1 + var4)
            var2 = (var2 + var9)
            var11 = (var11 + 2)
            if (1 if (var11 + 2) != var12 else 0):
                continue
            break  # end loop
    if (1 if (var8 & 1) == 0 else 0):
        break
    # call_indirect via table[var3]
    return i32_load(var0 + 16)


# ==========================================================
# $func1086
# ==========================================================
def func1086(var0, var1):
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
    var2 = i32_load(var0 + 16)
    var8 = i32_load(var0 + 12)
    var13 = ((i32_load(var0 + 12) + 1) // 2)
    var9 = i32_load(var1)
    var10 = i32_load(var9 + 20)
    var3 = i32_load(var0 + 8)
    var6 = (i32_load(i32_load(var1) + 16) + (i32_load(var9 + 20) * i32_load(var0 + 8)))
    var11 = i32_load(((i32_load(var9) << 2) + 9687824))
    var4 = i32_load(var0 + 28)
    var5 = i32_load(var0 + 24)
    var7 = i32_load(var0 + 20)
    if (1 if var3 == 0 else 0):
        # call_indirect via table[var11]
        break
    # call_indirect via table[var11]
    var10 = (var2 + 1)
    var12 = (var2 + var3)
    if (1 if var2 >= 3 else 0):
        var2 = (var3 + 2)
        while True:  # loop $label1
            var3 = i32_load(var0 + 32)
            var7 = (var7 + (i32_load(var0 + 32) << 1))
            var3 = i32_load(var0 + 36)
            var5 = (var5 + i32_load(var0 + 36))
            var4 = (var3 + var4)
            var3 = i32_load(var9 + 20)
            var6 = (var6 + (i32_load(var9 + 20) << 1))
            # call_indirect via table[var11]
            var2 = (var2 + 2)
            if (1 if (var2 + 2) < var12 else 0):
                continue
            break  # end loop
    var2 = (var7 + i32_load(var0 + 32))
    if (1 if i32_load(var0 + 88) > (i32_load(var0 + 84) + var12) else 0):
        # Unknown: memory.copy []
        # Unknown: memory.copy []
        # Unknown: memory.copy []
        return (var10 - 1)
    if (1 if (var12 & 1) == 0 else 0):
        # call_indirect via table[var11]
    return var10


# ==========================================================
# $U
# Export: U
# ==========================================================
def U(var0):
    """Export: U"""
    var0 = (i32_load(9561692) + (var0 * 286704))
    i32_store16((i32_load(9561692) + (var0 * 286704)), i32_load(9147392))
    i32_store16(var0 + 2, i32_load(9147396))
    i32_store16(var0 + 4, i32_load(9147400))
    i32_store16(var0 + 6, i32_load(9147404))
    i32_store16(var0 + 8, i32_load(9147408))
    i32_store16(var0 + 10, i32_load(9147412))
    i32_store16(var0 + 12, i32_load(9147416))
    i32_store16(var0 + 14, i32_load(9147420))
    i32_store16(var0 + 16, i32_load(9147424))
    i32_store16(var0 + 18, i32_load(9147428))
    i32_store16(var0 + 20, i32_load(9147432))
    i32_store16(var0 + 22, i32_load(9147436))
    i32_store16(var0 + 24, i32_load(9147440))
    i32_store16(var0 + 26, i32_load(9147444))
    i32_store16(var0 + 28, i32_load(9147448))
    i32_store16(var0 + 30, i32_load(9147452))
    i32_store16(var0 + 32, i32_load(9147456))
    i32_store16(var0 + 34, i32_load(9147460))
    i32_store16(var0 + 36, i32_load(9147464))
    i32_store16(var0 + 38, i32_load(9147468))

