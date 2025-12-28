"""
Auto-generated from WAT. Contains 13 functions.
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
# $func1035
# ==========================================================
def func1035(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var1 = i32_load8_u(var0 + 31)
    var3 = (i32_load8_u(var0 + 31) + 2)
    var2 = i32_load8_u(var0 + 63)
    i32_store8(var0 + 96, (((i32_load8_u(var0 + 95) + ((i32_load8_u(var0 + 31) + 2) + (i32_load8_u(var0 + 63) << 1))) & 0xFFFFFFFF) >> 2))
    var4 = i32_load8_u((var0 - 1))
    var5 = (i32_load8_u((var0 - 1)) + 2)
    var1 = (((var2 + ((i32_load8_u((var0 - 1)) + 2) + (var1 << 1))) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 97, (((var2 + ((i32_load8_u((var0 - 1)) + 2) + (var1 << 1))) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 64, var1)
    var2 = i32_load8_u((var0 - 33))
    var1 = (((i32_load8_u((var0 - 33)) + (var3 + (var4 << 1))) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 98, (((i32_load8_u((var0 - 33)) + (var3 + (var4 << 1))) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 65, var1)
    i32_store8(var0 + 32, var1)
    var3 = i32_load8_u((var0 - 32))
    var1 = ((((var5 + i32_load8_u((var0 - 32))) + (var2 << 1)) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 99, ((((var5 + i32_load8_u((var0 - 32))) + (var2 << 1)) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 66, var1)
    i32_store8(var0 + 33, var1)
    i32_store8(var0, var1)
    var5 = i32_load8_u((var0 - 29))
    var1 = i32_load8_u((var0 - 30))
    var4 = i32_load8_u((var0 - 31))
    var2 = (((((var2 + i32_load8_u((var0 - 31))) + (var3 << 1)) + 2) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 67, (((((var2 + i32_load8_u((var0 - 31))) + (var3 << 1)) + 2) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 34, var2)
    i32_store8(var0 + 1, var2)
    var2 = (((((var1 + var3) + (var4 << 1)) + 2) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 35, (((((var1 + var3) + (var4 << 1)) + 2) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 2, var2)
    i32_store8(var0 + 3, (((((var4 + var5) + (var1 << 1)) + 2) & 0xFFFFFFFF) >> 2))


# ==========================================================
# $func1045
# ==========================================================
def func1045(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    if (1 if var2 <= 0 else 0):
        break
    var1 = i32_load((var3 - 4))
    if (1 if var2 != 1 else 0):
        var7 = (var2 & -2)
        while True:  # loop $label1
            var4 = (var5 << 2)
            var8 = i32_load((var0 + var4))
            var9 = (((i32_load((var0 + var4)) & -16711936) + (var1 & -16711936)) & -16711936)
            var1 = (((var8 & 16711935) + (var1 & 16711935)) & 16711935)
            i32_store((var3 + (var5 << 2)), ((((i32_load((var0 + var4)) & -16711936) + (var1 & -16711936)) & -16711936) | (((var8 & 16711935) + (var1 & 16711935)) & 16711935)))
            var4 = (var4 | 4)
            var4 = i32_load((var0 + var4))
            var1 = ((((i32_load((var0 + var4)) & -16711936) + var9) & -16711936) | (((var4 & 16711935) + var1) & 16711935))
            i32_store((var3 + (var4 | 4)), ((((i32_load((var0 + var4)) & -16711936) + var9) & -16711936) | (((var4 & 16711935) + var1) & 16711935)))
            var5 = (var5 + 2)
            var6 = (var6 + 2)
            if (1 if (var6 + 2) != var7 else 0):
                continue
            break  # end loop
    if (1 if (var2 & 1) == 0 else 0):
        break
    var2 = (var5 << 2)
    var0 = i32_load((var0 + var2))
    i32_store((var3 + (var5 << 2)), ((((i32_load((var0 + var2)) & -16711936) + (var1 & -16711936)) & -16711936) | (((var0 & 16711935) + (var1 & 16711935)) & 16711935)))


# ==========================================================
# $func1050
# ==========================================================
def func1050(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    if (1 if var2 <= 0 else 0):
        break
    var1 = 0
    if (1 if var2 != 1 else 0):
        var6 = (var2 & -2)
        while True:  # loop $label1
            var4 = (var1 << 2)
            i32_store((var3 + (var1 << 2)), (i32_load((var0 + var4)) - 16777216))
            var4 = (var4 | 4)
            i32_store((var3 + (var4 | 4)), (i32_load((var0 + var4)) - 16777216))
            var1 = (var1 + 2)
            var5 = (var5 + 2)
            if (1 if (var5 + 2) != var6 else 0):
                continue
            break  # end loop
    if (1 if (var2 & 1) == 0 else 0):
        break
    var1 = (var1 << 2)
    i32_store((var3 + (var1 << 2)), (i32_load((var0 + var1)) - 16777216))


# ==========================================================
# $func1051
# ==========================================================
def func1051(var0, var1, var2, var3, var4, var5):
    var6 = 0
    var7 = 0
    if (1 if var3 > 0 else 0):
        while True:  # loop $label0
            i32_store((var5 + (var7 << 2)), ((i32_load8_u((var2 + var6)) | ((i32_load8_u((var0 + var6)) << 16) | (i32_load8_u((var1 + var6)) << 8))) | -16777216))
            var6 = (var4 + var6)
            var7 = (var7 + 1)
            if (1 if (var7 + 1) != var3 else 0):
                continue
            break  # end loop


# ==========================================================
# $func1053
# ==========================================================
def func1053(var0, var1, var2, var3, var4, var5):
    var6 = 0
    var7 = 0
    var8 = 0
    if (1 if var3 >= var4 else 0):
        break
    if (1 if var5 <= 0 else 0):
        break
    var7 = (var5 & -4)
    var6 = (var5 & 3)
    var8 = (1 if var5 < 4 else 0)
    while True:  # loop $label3
        var5 = 0
        if (1 if var8 == 0 else 0):
            while True:  # loop $label1
                i32_store8(var2, ((i32_load((var1 + (i32_load8_u(var0) << 2))) & 0xFFFFFFFF) >> 8))
                i32_store8(var2 + 1, ((i32_load((var1 + (i32_load8_u(var0 + 1) << 2))) & 0xFFFFFFFF) >> 8))
                i32_store8(var2 + 2, ((i32_load((var1 + (i32_load8_u(var0 + 2) << 2))) & 0xFFFFFFFF) >> 8))
                i32_store8(var2 + 3, ((i32_load((var1 + (i32_load8_u(var0 + 3) << 2))) & 0xFFFFFFFF) >> 8))
                var2 = (var2 + 4)
                var0 = (var0 + 4)
                var5 = (var5 + 4)
                if (1 if (var5 + 4) != var7 else 0):
                    continue
                break  # end loop
        var5 = 0
        if var6:
            while True:  # loop $label2
                i32_store8(var2, ((i32_load((var1 + (i32_load8_u(var0) << 2))) & 0xFFFFFFFF) >> 8))
                var2 = (var2 + 1)
                var0 = (var0 + 1)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var6 else 0):
                    continue
                break  # end loop
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != var4 else 0):
            continue
        break  # end loop


# ==========================================================
# $func1054
# ==========================================================
def func1054(var0, var1, var2, var3, var4, var5):
    var6 = 0
    var7 = 0
    var8 = 0
    if (1 if var3 >= var4 else 0):
        break
    if (1 if var5 <= 0 else 0):
        break
    var7 = (var5 & -4)
    var6 = (var5 & 3)
    var8 = (1 if var5 < 4 else 0)
    while True:  # loop $label3
        var5 = 0
        if (1 if var8 == 0 else 0):
            while True:  # loop $label1
                i32_store(var2, i32_load((var1 + (((i32_load(var0) & 0xFFFFFFFF) >> 6) & 1020))))
                i32_store(var2 + 4, i32_load((var1 + (((i32_load(var0 + 4) & 0xFFFFFFFF) >> 6) & 1020))))
                i32_store(var2 + 8, i32_load((var1 + (((i32_load(var0 + 8) & 0xFFFFFFFF) >> 6) & 1020))))
                i32_store(var2 + 12, i32_load((var1 + (((i32_load(var0 + 12) & 0xFFFFFFFF) >> 6) & 1020))))
                var2 = (var2 + 16)
                var0 = (var0 + 16)
                var5 = (var5 + 4)
                if (1 if (var5 + 4) != var7 else 0):
                    continue
                break  # end loop
        var5 = 0
        if var6:
            while True:  # loop $label2
                i32_store(var2, i32_load((var1 + (((i32_load(var0) & 0xFFFFFFFF) >> 6) & 1020))))
                var2 = (var2 + 4)
                var0 = (var0 + 4)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var6 else 0):
                    continue
                break  # end loop
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != var4 else 0):
            continue
        break  # end loop


# ==========================================================
# $func1055
# ==========================================================
def func1055(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var2 = i32_load8_u((var0 - 29))
    var5 = (i32_load8_u((var0 - 29)) + 2)
    var3 = i32_load8_u((var0 - 31))
    var1 = i32_load8_u((var0 - 30))
    var4 = (((((i32_load8_u((var0 - 29)) + 2) + i32_load8_u((var0 - 31))) + (i32_load8_u((var0 - 30)) << 1)) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 32, (((((i32_load8_u((var0 - 29)) + 2) + i32_load8_u((var0 - 31))) + (i32_load8_u((var0 - 30)) << 1)) & 0xFFFFFFFF) >> 2))
    var1 = (var1 + 2)
    i32_store8(var0, (((((var1 + 2) + i32_load8_u((var0 - 32))) + (var3 << 1)) & 0xFFFFFFFF) >> 2))
    var3 = i32_load8_u((var0 - 28))
    var1 = (((i32_load8_u((var0 - 28)) + (var1 + (var2 << 1))) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 64, (((i32_load8_u((var0 - 28)) + (var1 + (var2 << 1))) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 1, var4)
    i32_store8(var0 + 33, var1)
    var4 = i32_load8_u((var0 - 27))
    var2 = (((i32_load8_u((var0 - 27)) + (var5 + (var3 << 1))) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 96, (((i32_load8_u((var0 - 27)) + (var5 + (var3 << 1))) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 2, var1)
    i32_store8(var0 + 65, var2)
    i32_store8(var0 + 34, var2)
    i32_store8(var0 + 3, var2)
    var2 = i32_load8_u((var0 - 26))
    var3 = ((((i32_load8_u((var0 - 26)) + (var3 + (var4 << 1))) + 2) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 97, ((((i32_load8_u((var0 - 26)) + (var3 + (var4 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    var1 = i32_load8_u((var0 - 25))
    var4 = ((((i32_load8_u((var0 - 25)) + (var4 + (var2 << 1))) + 2) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 98, ((((i32_load8_u((var0 - 25)) + (var4 + (var2 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 35, var3)
    i32_store8(var0 + 66, var3)
    i32_store8(var0 + 99, (((((var1 + var2) + (var1 << 1)) + 2) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 67, var4)


# ==========================================================
# $func1057
# ==========================================================
def func1057(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    if var0:
    else:
    var0 = 0
    if (1 if var3 <= 0 else 0):
        break
    var5 = (var3 & 3)
    if (1 if var3 < 4 else 0):
        var3 = 0
        break
    var8 = (var3 & -4)
    var3 = 0
    while True:  # loop $label2
        var0 = (i32_load8_u((var1 + var3)) + var0)
        i32_store8((var2 + var3), (i32_load8_u((var1 + var3)) + var0))
        var4 = (var3 | 1)
        var0 = (i32_load8_u((var1 + var4)) + var0)
        i32_store8((var2 + (var3 | 1)), (i32_load8_u((var1 + var4)) + var0))
        var4 = (var3 | 2)
        var0 = (i32_load8_u((var1 + var4)) + var0)
        i32_store8((var2 + (var3 | 2)), (i32_load8_u((var1 + var4)) + var0))
        var4 = (var3 | 3)
        var0 = (i32_load8_u((var1 + var4)) + var0)
        i32_store8((var2 + (var3 | 3)), (i32_load8_u((var1 + var4)) + var0))
        var3 = (var3 + 4)
        var7 = (var7 + 4)
        if (1 if (var7 + 4) != var8 else 0):
            continue
        break  # end loop
    if (1 if var5 == 0 else 0):
        break
    while True:  # loop $label3
        var0 = (i32_load8_u((var1 + var3)) + var0)
        i32_store8((var2 + var3), (i32_load8_u((var1 + var3)) + var0))
        var3 = (var3 + 1)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) != var5 else 0):
            continue
        break  # end loop
    return i32_load8_u(var0)


# ==========================================================
# $func1059
# ==========================================================
def func1059(var0, var1):
    var2 = 0
    while True:  # loop $label0
        if (1 if var1 <= 0 else 0):
            return 0
        var1 = (var1 - 1)
        var2 = i32_load8_u(var0)
        var0 = (var0 + 1)
        if (1 if var2 == 255 else 0):
            continue
        break  # end loop
    return 1


# ==========================================================
# $func1060
# ==========================================================
def func1060(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    if (1 if var1 <= 0 else 0):
        break
    while True:  # loop $label1
        if (1 if i32_load8_u((var0 + var2)) == 255 else 0):
            var2 = (var2 + 4)
            var4 = (1 if var1 < 2 else 0)
            var1 = (var1 - 1)
            if (1 if var4 == 0 else 0):
                continue
            break
        break  # end loop
    var3 = 1
    return var3


# ==========================================================
# $func1061
# ==========================================================
def func1061(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var1 = i32_load8_u(var0 + 95)
    i32_store8(var0 + 99, i32_load8_u(var0 + 95))
    i32_store8(var0 + 98, var1)
    i32_store8(var0 + 97, var1)
    i32_store8(var0 + 96, var1)
    var4 = i32_load8_u(var0 + 31)
    var3 = (i32_load8_u(var0 + 31) + 1)
    var2 = i32_load8_u(var0 + 63)
    var5 = ((((i32_load8_u(var0 + 31) + 1) + i32_load8_u(var0 + 63)) & 0xFFFFFFFF) >> 1)
    i32_store8(var0 + 32, ((((i32_load8_u(var0 + 31) + 1) + i32_load8_u(var0 + 63)) & 0xFFFFFFFF) >> 1))
    var6 = i32_load8_u((var0 - 1))
    i32_store8(var0, (((var3 + i32_load8_u((var0 - 1))) & 0xFFFFFFFF) >> 1))
    var3 = ((((var1 + var2) + 1) & 0xFFFFFFFF) >> 1)
    i32_store8(var0 + 64, ((((var1 + var2) + 1) & 0xFFFFFFFF) >> 1))
    i32_store8(var0 + 2, var5)
    i32_store8(var0 + 34, var3)
    var3 = (((((var1 + var4) + (var2 << 1)) + 2) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 33, (((((var1 + var4) + (var2 << 1)) + 2) & 0xFFFFFFFF) >> 2))
    var2 = (var2 + 2)
    i32_store8(var0 + 1, ((((var6 + (var2 + 2)) + (var4 << 1)) & 0xFFFFFFFF) >> 2))
    var2 = ((((var1 + var2) + (var1 << 1)) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 65, ((((var1 + var2) + (var1 << 1)) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 3, var3)
    i32_store8(var0 + 35, var2)
    i32_store8(var0 + 67, var1)
    i32_store8(var0 + 66, var1)


# ==========================================================
# $func1066
# ==========================================================
def func1066(var0):
    i64_store(var0 + 32, (i64_load8_u(var0 + 31) * 72340172838076673))
    i64_store(var0 + 64, (i64_load8_u(var0 + 63) * 72340172838076673))
    i64_store(var0 + 96, (i64_load8_u(var0 + 95) * 72340172838076673))
    i64_store(var0 + 128, (i64_load8_u(var0 + 127) * 72340172838076673))
    i64_store(var0 + 160, (i64_load8_u(var0 + 159) * 72340172838076673))
    i64_store(var0 + 192, (i64_load8_u(var0 + 191) * 72340172838076673))
    i64_store(var0 + 224, (i64_load8_u(var0 + 223) * 72340172838076673))
    i64_store(var0, (i64_load8_u((var0 - 1)) * 72340172838076673))


# ==========================================================
# $func1067
# ==========================================================
def func1067(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var2 = i32_load8_u(var0 + 63)
    var3 = (i32_load8_u(var0 + 63) + 2)
    var1 = i32_load8_u(var0 + 95)
    i32_store(var0 + 96, ((((((i32_load8_u(var0 + 63) + 2) + i32_load8_u(var0 + 95)) + (var1 << 1)) & 0xFFFFFFFF) >> 2) * 16843009))
    var4 = i32_load8_u(var0 + 31)
    var5 = (i32_load8_u(var0 + 31) + 2)
    i32_store(var0 + 64, ((((var1 + ((i32_load8_u(var0 + 31) + 2) + (var2 << 1))) & 0xFFFFFFFF) >> 2) * 16843009))
    var1 = i32_load8_u((var0 - 1))
    i32_store(var0 + 32, (((((var3 + i32_load8_u((var0 - 1))) + (var4 << 1)) & 0xFFFFFFFF) >> 2) * 16843009))
    i32_store(var0, (((((var5 + i32_load8_u((var0 - 33))) + (var1 << 1)) & 0xFFFFFFFF) >> 2) * 16843009))

