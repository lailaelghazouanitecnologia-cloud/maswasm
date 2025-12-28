"""
Auto-generated from WAT. Contains 10 functions.
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
# $func977
# ==========================================================
def func977(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    if (1 if var3 < 2 else 0):
        break
    var5 = (var3 >> 1)
    var8 = (1 if (1 if var5 <= 1 else 0) else (var3 >> 1))
    var5 = 0
    if (1 if var4 == 0 else 0):
        while True:  # loop $label1
            var6 = (var1 + var5)
            var7 = (var0 + (var5 << 3))
            var6 = i32_load((var0 + (var5 << 3)) + 4)
            var7 = i32_load(var7)
            var9 = ((((i32_load((var0 + (var5 << 3)) + 4) & 0xFFFFFFFF) >> 15) & 510) + (((i32_load(var7) & 0xFFFFFFFF) >> 15) & 510))
            var10 = ((((var6 & 0xFFFFFFFF) >> 7) & 510) + (((var7 & 0xFFFFFFFF) >> 7) & 510))
            var6 = (((var6 << 1) & 510) + ((var7 << 1) & 510))
            i32_store8((var1 + var5), ((((i32_load8_u(var6) + ((((((((((i32_load((var0 + (var5 << 3)) + 4) & 0xFFFFFFFF) >> 15) & 510) + (((i32_load(var7) & 0xFFFFFFFF) >> 15) & 510)) * -9719) + (((((var6 & 0xFFFFFFFF) >> 7) & 510) + (((var7 & 0xFFFFFFFF) >> 7) & 510)) * -19081)) + ((((var6 << 1) & 510) + ((var7 << 1) & 510)) * 28800)) + 33685504) & 0xFFFFFFFF) >> 18)) + 1) & 0xFFFFFFFF) >> 1))
            var7 = (var2 + var5)
            i32_store8((var2 + var5), ((((i32_load8_u(var7) + ((((((var9 * 28800) + (var10 * -24116)) + (var6 * -4684)) + 33685504) & 0xFFFFFFFF) >> 18)) + 1) & 0xFFFFFFFF) >> 1))
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var8 else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    while True:  # loop $label2
        var7 = (var0 + (var5 << 3))
        var6 = i32_load((var0 + (var5 << 3)) + 4)
        var7 = i32_load(var7)
        var9 = ((((i32_load((var0 + (var5 << 3)) + 4) & 0xFFFFFFFF) >> 15) & 510) + (((i32_load(var7) & 0xFFFFFFFF) >> 15) & 510))
        var10 = ((((var6 & 0xFFFFFFFF) >> 7) & 510) + (((var7 & 0xFFFFFFFF) >> 7) & 510))
        var6 = (((var6 << 1) & 510) + ((var7 << 1) & 510))
        i32_store8((var1 + var5), ((((((((((i32_load((var0 + (var5 << 3)) + 4) & 0xFFFFFFFF) >> 15) & 510) + (((i32_load(var7) & 0xFFFFFFFF) >> 15) & 510)) * 67099145) + (((((var6 & 0xFFFFFFFF) >> 7) & 510) + (((var7 & 0xFFFFFFFF) >> 7) & 510)) * 67089783)) + ((((var6 << 1) & 510) + ((var7 << 1) & 510)) * 28800)) + 33685504) & 0xFFFFFFFF) >> 18))
        i32_store8((var2 + var5), ((((((var9 * 28800) + (var10 * 67084748)) + (var6 * 67104180)) + 33685504) & 0xFFFFFFFF) >> 18))
        var5 = (var5 + 1)
        if (1 if (var5 + 1) != var8 else 0):
            continue
        break  # end loop
    if (var3 & 1):
        var0 = i32_load((var0 + (var8 << 3)))
        var3 = (((i32_load((var0 + (var8 << 3))) & 0xFFFFFFFF) >> 14) & 1020)
        var5 = (((var0 & 0xFFFFFFFF) >> 6) & 1020)
        var6 = ((var0 << 2) & 1020)
        var0 = (((((((((i32_load((var0 + (var8 << 3))) & 0xFFFFFFFF) >> 14) & 1020) * 28800) + ((((var0 & 0xFFFFFFFF) >> 6) & 1020) * -24116)) + (((var0 << 2) & 1020) * -4684)) + 33685504) & 0xFFFFFFFF) >> 18)
        var3 = ((((((var3 * -9719) + (var5 * -19081)) + (var6 * 28800)) + 33685504) & 0xFFFFFFFF) >> 18)
        if var4:
            i32_store8((var1 + var8), var3)
            i32_store8((var2 + var8), var0)
            return
        var1 = (var1 + var8)
        i32_store8((var1 + var8), ((((var3 + i32_load8_u(var1)) + 1) & 0xFFFFFFFF) >> 1))
        var1 = (var2 + var8)
        i32_store8((var2 + var8), ((((var0 + i32_load8_u(var1)) + 1) & 0xFFFFFFFF) >> 1))


# ==========================================================
# $func978
# ==========================================================
def func978(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    if var0:
        if (1 if var3 <= 0 else 0):
            break
        var7 = (var3 & 1)
        if (1 if var3 != 1 else 0):
            var8 = (var3 & -2)
            var3 = 0
            while True:  # loop $label1
                i32_store8((var2 + var4), (i32_load8_u((var1 + var4)) + i32_load8_u((var0 + var4))))
                var5 = (var4 | 1)
                i32_store8((var2 + (var4 | 1)), (i32_load8_u((var1 + var5)) + i32_load8_u((var0 + var5))))
                var4 = (var4 + 2)
                var3 = (var3 + 2)
                if (1 if (var3 + 2) != var8 else 0):
                    continue
                break  # end loop
        if (1 if var7 == 0 else 0):
            break
        i32_store8((var2 + var4), (i32_load8_u((var1 + var4)) + i32_load8_u((var0 + var4))))
        return
    if (1 if var3 <= 0 else 0):
        break
    var7 = (var3 & 3)
    var0 = 0
    if (1 if var3 >= 4 else 0):
        var8 = (var3 & -4)
        var3 = 0
        while True:  # loop $label2
            var5 = (i32_load8_u((var1 + var4)) + var5)
            i32_store8((var2 + var4), (i32_load8_u((var1 + var4)) + var5))
            var6 = (var4 | 1)
            var5 = (i32_load8_u((var1 + var6)) + var5)
            i32_store8((var2 + (var4 | 1)), (i32_load8_u((var1 + var6)) + var5))
            var6 = (var4 | 2)
            var5 = (i32_load8_u((var1 + var6)) + var5)
            i32_store8((var2 + (var4 | 2)), (i32_load8_u((var1 + var6)) + var5))
            var6 = (var4 | 3)
            var5 = (i32_load8_u((var1 + var6)) + var5)
            i32_store8((var2 + (var4 | 3)), (i32_load8_u((var1 + var6)) + var5))
            var4 = (var4 + 4)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var8 else 0):
                continue
            break  # end loop
    if (1 if var7 == 0 else 0):
        break
    while True:  # loop $label3
        var5 = (i32_load8_u((var1 + var4)) + var5)
        i32_store8((var2 + var4), (i32_load8_u((var1 + var4)) + var5))
        var4 = (var4 + 1)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var7 else 0):
            continue
        break  # end loop


# ==========================================================
# $func980
# ==========================================================
def func980(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var2 = i32_load8_u((var0 - 32))
    var3 = (i32_load8_u((var0 - 32)) + 1)
    var1 = i32_load8_u((var0 - 33))
    var4 = ((((i32_load8_u((var0 - 32)) + 1) + i32_load8_u((var0 - 33))) & 0xFFFFFFFF) >> 1)
    i32_store8(var0 + 65, ((((i32_load8_u((var0 - 32)) + 1) + i32_load8_u((var0 - 33))) & 0xFFFFFFFF) >> 1))
    var5 = i32_load8_u((var0 - 31))
    var6 = (((var3 + i32_load8_u((var0 - 31))) & 0xFFFFFFFF) >> 1)
    i32_store8(var0 + 66, (((var3 + i32_load8_u((var0 - 31))) & 0xFFFFFFFF) >> 1))
    i32_store8(var0, var4)
    var3 = i32_load8_u((var0 - 30))
    var4 = ((((var5 + i32_load8_u((var0 - 30))) + 1) & 0xFFFFFFFF) >> 1)
    i32_store8(var0 + 67, ((((var5 + i32_load8_u((var0 - 30))) + 1) & 0xFFFFFFFF) >> 1))
    i32_store8(var0 + 1, var6)
    var6 = i32_load8_u((var0 - 29))
    i32_store8(var0 + 3, ((((var3 + i32_load8_u((var0 - 29))) + 1) & 0xFFFFFFFF) >> 1))
    i32_store8(var0 + 2, var4)
    var4 = i32_load8_u((var0 - 1))
    var7 = (i32_load8_u((var0 - 1)) + 2)
    var8 = i32_load8_u(var0 + 31)
    i32_store8(var0 + 96, (((((i32_load8_u((var0 - 1)) + 2) + i32_load8_u(var0 + 63)) + (i32_load8_u(var0 + 31) << 1)) & 0xFFFFFFFF) >> 2))
    var7 = (((var2 + (var7 + (var1 << 1))) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 97, (((var2 + (var7 + (var1 << 1))) & 0xFFFFFFFF) >> 2))
    var1 = (var1 + 2)
    i32_store8(var0 + 64, ((((var8 + (var1 + 2)) + (var4 << 1)) & 0xFFFFFFFF) >> 2))
    var1 = (((var5 + (var1 + (var2 << 1))) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 98, (((var5 + (var1 + (var2 << 1))) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 32, var7)
    var2 = ((((var3 + (var2 + (var5 << 1))) + 2) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 99, ((((var3 + (var2 + (var5 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 33, var1)
    i32_store8(var0 + 35, ((((var6 + (var5 + (var3 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 34, var2)


# ==========================================================
# $func981
# ==========================================================
def func981(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    if (1 if var2 > 0 else 0):
        var5 = i32_load8_s(var0 + 2)
        var6 = i32_load8_s(var0 + 1)
        var7 = i32_load8_s(var0)
        var0 = 0
        while True:  # loop $label0
            var4 = (var0 << 2)
            var4 = i32_load((var1 + var4))
            var8 = ((i32_load((var1 + var4)) << 16) >> 24)
            var9 = (((((i32_load((var1 + var4)) << 16) >> 24) * var7) >> 5) + ((var4 & 0xFFFFFFFF) >> 16))
            # Unknown: i32.extend8_s []
            i32_store((var3 + (var0 << 2)), (((((((((i32_load((var1 + var4)) << 16) >> 24) * var7) >> 5) + ((var4 & 0xFFFFFFFF) >> 16)) << 16) & 16711680) | (var4 & -16711936)) | ((((((var6 * var8) & 0xFFFFFFFF) >> 5) + var4) + (((var9 * var5) & 0xFFFFFFFF) >> 5)) & 255)))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var2 else 0):
                continue
            break  # end loop


# ==========================================================
# $func986
# ==========================================================
def func986(var0, var1):
    var2 = 0
    var2 = i32_load(var1 + 4)
    var0 = i32_load(var0)
    var0 = (((((i32_load(var1 + 4) ^ i32_load(var0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var0 & var2))
    var1 = i32_load(var1)
    return ((((((((((i32_load(var1 + 4) ^ i32_load(var0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var0 & var2)) ^ i32_load(var1)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var0 & var1))


# ==========================================================
# $func991
# ==========================================================
def func991(var0, var1):
    var2 = 0
    var2 = i32_load(var1)
    var0 = i32_load(var0)
    var0 = (((((i32_load(var1) ^ i32_load(var0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var0 & var2))
    var2 = (((((((i32_load(var1) ^ i32_load(var0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var0 & var2)) & 0xFFFFFFFF) >> 24)
    var1 = i32_load((var1 - 4))
    # Unknown: i32.extend16_s []
    var2 = ((((((((i32_load(var1) ^ i32_load(var0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var0 & var2)) & 0xFFFFFFFF) >> 24) + ((var2 - ((i32_load((var1 - 4)) & 0xFFFFFFFF) >> 24)) // 2))
    var2 = (var0 & 255)
    # Unknown: i32.extend16_s []
    var2 = ((var0 & 255) + ((var2 - (var1 & 255)) // 2))
    var2 = (((var0 & 0xFFFFFFFF) >> 16) & 255)
    # Unknown: i32.extend16_s []
    var2 = ((((var0 & 0xFFFFFFFF) >> 16) & 255) + ((var2 - (((var1 & 0xFFFFFFFF) >> 16) & 255)) // 2))
    var0 = (((var0 & 0xFFFFFFFF) >> 8) & 255)
    # Unknown: i32.extend16_s []
    var0 = ((((var0 & 0xFFFFFFFF) >> 8) & 255) + ((var0 - (((var1 & 0xFFFFFFFF) >> 8) & 255)) // 2))
    return (((((((((((((i32_load(var1) ^ i32_load(var0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var0 & var2)) & 0xFFFFFFFF) >> 24) + ((var2 - ((i32_load((var1 - 4)) & 0xFFFFFFFF) >> 24)) // 2)) if (1 if var2 < 256 else 0) else (((var2 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | (((var0 & 255) + ((var2 - (var1 & 255)) // 2)) if (1 if var2 < 256 else 0) else (((var2 ^ -1) & 0xFFFFFFFF) >> 24))) | ((((((var0 & 0xFFFFFFFF) >> 16) & 255) + ((var2 - (((var1 & 0xFFFFFFFF) >> 16) & 255)) // 2)) if (1 if var2 < 256 else 0) else (((var2 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | ((((((var0 & 0xFFFFFFFF) >> 8) & 255) + ((var0 - (((var1 & 0xFFFFFFFF) >> 8) & 255)) // 2)) if (1 if var0 < 256 else 0) else (((var0 ^ -1) & 0xFFFFFFFF) >> 24)) << 8))


# ==========================================================
# $func992
# ==========================================================
def func992(var0, var1):
    var2 = 0
    var3 = 0
    var3 = i32_load(var1)
    var0 = i32_load(var0)
    var1 = i32_load((var1 - 4))
    var2 = ((((i32_load(var1) & 0xFFFFFFFF) >> 24) + ((i32_load(var0) & 0xFFFFFFFF) >> 24)) - ((i32_load((var1 - 4)) & 0xFFFFFFFF) >> 24))
    var2 = (((var3 & 255) + (var0 & 255)) - (var1 & 255))
    var2 = (((((var3 & 0xFFFFFFFF) >> 16) & 255) + (((var0 & 0xFFFFFFFF) >> 16) & 255)) - (((var1 & 0xFFFFFFFF) >> 16) & 255))
    var0 = (((((var3 & 0xFFFFFFFF) >> 8) & 255) + (((var0 & 0xFFFFFFFF) >> 8) & 255)) - (((var1 & 0xFFFFFFFF) >> 8) & 255))
    return (((((((((i32_load(var1) & 0xFFFFFFFF) >> 24) + ((i32_load(var0) & 0xFFFFFFFF) >> 24)) - ((i32_load((var1 - 4)) & 0xFFFFFFFF) >> 24)) if (1 if var2 < 256 else 0) else (((var2 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | ((((var3 & 255) + (var0 & 255)) - (var1 & 255)) if (1 if var2 < 256 else 0) else (((var2 ^ -1) & 0xFFFFFFFF) >> 24))) | (((((((var3 & 0xFFFFFFFF) >> 16) & 255) + (((var0 & 0xFFFFFFFF) >> 16) & 255)) - (((var1 & 0xFFFFFFFF) >> 16) & 255)) if (1 if var2 < 256 else 0) else (((var2 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | (((((((var3 & 0xFFFFFFFF) >> 8) & 255) + (((var0 & 0xFFFFFFFF) >> 8) & 255)) - (((var1 & 0xFFFFFFFF) >> 8) & 255)) if (1 if var0 < 256 else 0) else (((var0 ^ -1) & 0xFFFFFFFF) >> 24)) << 8))


# ==========================================================
# $func993
# ==========================================================
def func993(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var4 = i32_load(var1)
    var0 = i32_load(var0)
    var1 = i32_load((var1 - 4))
    var2 = (i32_load((var1 - 4)) & 255)
    var3 = ((var0 & 255) - (i32_load((var1 - 4)) & 255))
    var3 = (var3 >> 31)
    var3 = ((var1 & 0xFFFFFFFF) >> 24)
    var5 = (((var0 & 0xFFFFFFFF) >> 24) - ((var1 & 0xFFFFFFFF) >> 24))
    var5 = (var5 >> 31)
    var5 = (((var1 & 0xFFFFFFFF) >> 8) & 255)
    var6 = ((((var0 & 0xFFFFFFFF) >> 8) & 255) - (((var1 & 0xFFFFFFFF) >> 8) & 255))
    var6 = (var6 >> 31)
    var3 = (((var4 & 0xFFFFFFFF) >> 24) - var3)
    var3 = (var3 >> 31)
    var2 = ((var4 & 255) - var2)
    var2 = (var2 >> 31)
    var2 = ((((var4 & 0xFFFFFFFF) >> 8) & 255) - var5)
    var2 = (var2 >> 31)
    var1 = (((var1 & 0xFFFFFFFF) >> 16) & 255)
    var4 = ((((var4 & 0xFFFFFFFF) >> 16) & 255) - (((var1 & 0xFFFFFFFF) >> 16) & 255))
    var4 = (var4 >> 31)
    var0 = ((((var0 & 0xFFFFFFFF) >> 16) & 255) - var1)
    var0 = (var0 >> 31)
    return (i32_load(var1) if (1 if ((((((((var0 & 255) - (i32_load((var1 - 4)) & 255)) ^ (var3 >> 31)) - var3) + (((((var0 & 0xFFFFFFFF) >> 24) - ((var1 & 0xFFFFFFFF) >> 24)) ^ (var5 >> 31)) - var5)) + ((((((var0 & 0xFFFFFFFF) >> 8) & 255) - (((var1 & 0xFFFFFFFF) >> 8) & 255)) ^ (var6 >> 31)) - var6)) - ((((((((var4 & 0xFFFFFFFF) >> 24) - var3) ^ (var3 >> 31)) - var3) + ((((var4 & 255) - var2) ^ (var2 >> 31)) - var2)) + ((((((var4 & 0xFFFFFFFF) >> 8) & 255) - var5) ^ (var2 >> 31)) - var2)) + ((((((var4 & 0xFFFFFFFF) >> 16) & 255) - (((var1 & 0xFFFFFFFF) >> 16) & 255)) ^ (var4 >> 31)) - var4))) + ((((((var0 & 0xFFFFFFFF) >> 16) & 255) - var1) ^ (var0 >> 31)) - var0)) <= 0 else 0) else i32_load(var0))


# ==========================================================
# $func994
# ==========================================================
def func994(var0, var1):
    var2 = 0
    var3 = 0
    var2 = i32_load(var1 + 4)
    var3 = i32_load(var1)
    var2 = (((((i32_load(var1 + 4) ^ i32_load(var1)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var2 & var3))
    var1 = i32_load((var1 - 4))
    var0 = i32_load(var0)
    var0 = (((((i32_load((var1 - 4)) ^ i32_load(var0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var0 & var1))
    return ((((((((((i32_load(var1 + 4) ^ i32_load(var1)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var2 & var3)) ^ (((((i32_load((var1 - 4)) ^ i32_load(var0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var0 & var1))) & 0xFFFFFFFF) >> 1) & 2139062143) + (var0 & var2))


# ==========================================================
# $func996
# ==========================================================
def func996(var0, var1, var2):
    var3 = 0
    if (1 if var1 > 0 else 0):
        var3 = (var0 + (var1 << 2))
        while True:  # loop $label0
            var1 = i32_load(var0)
            i32_store8(var2 + 2, i32_load(var0))
            i32_store8(var2 + 1, ((var1 & 0xFFFFFFFF) >> 8))
            i32_store8(var2, ((var1 & 0xFFFFFFFF) >> 16))
            var2 = (var2 + 3)
            var0 = (var0 + 4)
            if (1 if (var0 + 4) < var3 else 0):
                continue
            break  # end loop

