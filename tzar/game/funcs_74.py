"""
Auto-generated from WAT. Contains 9 functions.
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
# $func1040
# ==========================================================
def func1040(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if var1:
        if (1 if var2 > 0 else 0):
            var6 = (var1 - 4)
            var1 = i32_load((var3 - 4))
            while True:  # loop $label0
                var4 = (var5 << 2)
                var7 = i32_load((var4 + var6))
                var1 = (((((i32_load((var4 + var6)) ^ var1) & 0xFFFFFFFF) >> 1) & 2139062143) + (var1 & var7))
                var4 = i32_load((var0 + var4))
                var1 = (((((((((i32_load((var4 + var6)) ^ var1) & 0xFFFFFFFF) >> 1) & 2139062143) + (var1 & var7)) & -16711936) + (i32_load((var0 + var4)) & -16711936)) & -16711936) | (((var1 & 16711935) + (var4 & 16711935)) & 16711935))
                i32_store((var3 + (var5 << 2)), (((((((((i32_load((var4 + var6)) ^ var1) & 0xFFFFFFFF) >> 1) & 2139062143) + (var1 & var7)) & -16711936) + (i32_load((var0 + var4)) & -16711936)) & -16711936) | (((var1 & 16711935) + (var4 & 16711935)) & 16711935)))
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func1041
# ==========================================================
def func1041(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    if var1:
        if (1 if var2 > 0 else 0):
            var4 = i32_load((var3 - 4))
            while True:  # loop $label0
                var5 = (var6 << 2)
                var7 = (var1 + var5)
                var8 = i32_load((var1 + var5) + 4)
                var4 = (((((i32_load((var1 + var5) + 4) ^ var4) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var8))
                var7 = i32_load(var7)
                var4 = ((((((((((i32_load((var1 + var5) + 4) ^ var4) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var8)) ^ i32_load(var7)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var7))
                var5 = i32_load((var0 + var5))
                var4 = ((((((((((((((i32_load((var1 + var5) + 4) ^ var4) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var8)) ^ i32_load(var7)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var7)) & -16711936) + (i32_load((var0 + var5)) & -16711936)) & -16711936) | (((var4 & 16711935) + (var5 & 16711935)) & 16711935))
                i32_store((var3 + (var6 << 2)), ((((((((((((((i32_load((var1 + var5) + 4) ^ var4) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var8)) ^ i32_load(var7)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var7)) & -16711936) + (i32_load((var0 + var5)) & -16711936)) & -16711936) | (((var4 & 16711935) + (var5 & 16711935)) & 16711935)))
                var6 = (var6 + 1)
                if (1 if (var6 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func1042
# ==========================================================
def func1042(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    if var1:
        if (1 if var2 > 0 else 0):
            var5 = (var1 - 4)
            while True:  # loop $label0
                var1 = (var4 << 2)
                var6 = i32_load((var0 + var1))
                var1 = i32_load((var1 + var5))
                i32_store((var3 + (var4 << 2)), ((((i32_load((var0 + var1)) & -16711936) + (i32_load((var1 + var5)) & -16711936)) & -16711936) | (((var6 & 16711935) + (var1 & 16711935)) & 16711935)))
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func1043
# ==========================================================
def func1043(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    if var1:
        if (1 if var2 > 0 else 0):
            var5 = (var1 + 4)
            while True:  # loop $label0
                var1 = (var4 << 2)
                var6 = i32_load((var0 + var1))
                var1 = i32_load((var1 + var5))
                i32_store((var3 + (var4 << 2)), ((((i32_load((var0 + var1)) & -16711936) + (i32_load((var1 + var5)) & -16711936)) & -16711936) | (((var6 & 16711935) + (var1 & 16711935)) & 16711935)))
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func1044
# ==========================================================
def func1044(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    if var1:
        if (1 if var2 > 0 else 0):
            while True:  # loop $label0
                var4 = (var5 << 2)
                var6 = i32_load((var0 + var4))
                var4 = i32_load((var1 + var4))
                i32_store((var3 + (var5 << 2)), ((((i32_load((var0 + var4)) & -16711936) + (i32_load((var1 + var4)) & -16711936)) & -16711936) | (((var6 & 16711935) + (var4 & 16711935)) & 16711935)))
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func1046
# ==========================================================
def func1046(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    if var1:
        if (1 if var2 > 0 else 0):
            var5 = i32_load((var3 - 4))
            while True:  # loop $label0
                var8 = (var7 << 2)
                var6 = (var1 + var8)
                var4 = i32_load((var1 + var8))
                var5 = (((((i32_load((var1 + var8)) ^ var5) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var5))
                var4 = (((((((i32_load((var1 + var8)) ^ var5) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var5)) & 0xFFFFFFFF) >> 24)
                var6 = i32_load((var6 - 4))
                # Unknown: i32.extend16_s []
                var4 = ((((((((i32_load((var1 + var8)) ^ var5) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var5)) & 0xFFFFFFFF) >> 24) + ((var4 - ((i32_load((var6 - 4)) & 0xFFFFFFFF) >> 24)) // 2))
                var4 = (var5 & 255)
                # Unknown: i32.extend16_s []
                var4 = ((var5 & 255) + ((var4 - (var6 & 255)) // 2))
                var4 = (((var5 & 0xFFFFFFFF) >> 16) & 255)
                # Unknown: i32.extend16_s []
                var4 = ((((var5 & 0xFFFFFFFF) >> 16) & 255) + ((var4 - (((var6 & 0xFFFFFFFF) >> 16) & 255)) // 2))
                var5 = (((var5 & 0xFFFFFFFF) >> 8) & 255)
                # Unknown: i32.extend16_s []
                var5 = ((((var5 & 0xFFFFFFFF) >> 8) & 255) + ((var5 - (((var6 & 0xFFFFFFFF) >> 8) & 255)) // 2))
                var5 = (((((((((((((i32_load((var1 + var8)) ^ var5) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var5)) & 0xFFFFFFFF) >> 24) + ((var4 - ((i32_load((var6 - 4)) & 0xFFFFFFFF) >> 24)) // 2)) if (1 if var4 < 256 else 0) else (((var4 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | (((var5 & 255) + ((var4 - (var6 & 255)) // 2)) if (1 if var4 < 256 else 0) else (((var4 ^ -1) & 0xFFFFFFFF) >> 24))) | ((((((var5 & 0xFFFFFFFF) >> 16) & 255) + ((var4 - (((var6 & 0xFFFFFFFF) >> 16) & 255)) // 2)) if (1 if var4 < 256 else 0) else (((var4 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | ((((((var5 & 0xFFFFFFFF) >> 8) & 255) + ((var5 - (((var6 & 0xFFFFFFFF) >> 8) & 255)) // 2)) if (1 if var5 < 256 else 0) else (((var5 ^ -1) & 0xFFFFFFFF) >> 24)) << 8))
                var6 = i32_load((var0 + var8))
                var5 = (((((((((((((((((i32_load((var1 + var8)) ^ var5) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var5)) & 0xFFFFFFFF) >> 24) + ((var4 - ((i32_load((var6 - 4)) & 0xFFFFFFFF) >> 24)) // 2)) if (1 if var4 < 256 else 0) else (((var4 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | (((var5 & 255) + ((var4 - (var6 & 255)) // 2)) if (1 if var4 < 256 else 0) else (((var4 ^ -1) & 0xFFFFFFFF) >> 24))) | ((((((var5 & 0xFFFFFFFF) >> 16) & 255) + ((var4 - (((var6 & 0xFFFFFFFF) >> 16) & 255)) // 2)) if (1 if var4 < 256 else 0) else (((var4 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | ((((((var5 & 0xFFFFFFFF) >> 8) & 255) + ((var5 - (((var6 & 0xFFFFFFFF) >> 8) & 255)) // 2)) if (1 if var5 < 256 else 0) else (((var5 ^ -1) & 0xFFFFFFFF) >> 24)) << 8)) & -16711936) + (i32_load((var0 + var8)) & -16711936)) & -16711936) | (((var5 & 16711935) + (var6 & 16711935)) & 16711935))
                i32_store((var3 + (var7 << 2)), (((((((((((((((((i32_load((var1 + var8)) ^ var5) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var5)) & 0xFFFFFFFF) >> 24) + ((var4 - ((i32_load((var6 - 4)) & 0xFFFFFFFF) >> 24)) // 2)) if (1 if var4 < 256 else 0) else (((var4 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | (((var5 & 255) + ((var4 - (var6 & 255)) // 2)) if (1 if var4 < 256 else 0) else (((var4 ^ -1) & 0xFFFFFFFF) >> 24))) | ((((((var5 & 0xFFFFFFFF) >> 16) & 255) + ((var4 - (((var6 & 0xFFFFFFFF) >> 16) & 255)) // 2)) if (1 if var4 < 256 else 0) else (((var4 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | ((((((var5 & 0xFFFFFFFF) >> 8) & 255) + ((var5 - (((var6 & 0xFFFFFFFF) >> 8) & 255)) // 2)) if (1 if var5 < 256 else 0) else (((var5 ^ -1) & 0xFFFFFFFF) >> 24)) << 8)) & -16711936) + (i32_load((var0 + var8)) & -16711936)) & -16711936) | (((var5 & 16711935) + (var6 & 16711935)) & 16711935)))
                var7 = (var7 + 1)
                if (1 if (var7 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func1047
# ==========================================================
def func1047(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    if var1:
        if (1 if var2 > 0 else 0):
            var4 = i32_load((var3 - 4))
            while True:  # loop $label0
                var9 = (var8 << 2)
                var6 = (var1 + var9)
                var7 = i32_load((var1 + var9))
                var6 = i32_load((var6 - 4))
                var5 = ((((i32_load((var1 + var9)) & 0xFFFFFFFF) >> 24) + ((var4 & 0xFFFFFFFF) >> 24)) - ((i32_load((var6 - 4)) & 0xFFFFFFFF) >> 24))
                var5 = (((var7 & 255) + (var4 & 255)) - (var6 & 255))
                var5 = (((((var7 & 0xFFFFFFFF) >> 16) & 255) + (((var4 & 0xFFFFFFFF) >> 16) & 255)) - (((var6 & 0xFFFFFFFF) >> 16) & 255))
                var4 = (((((var7 & 0xFFFFFFFF) >> 8) & 255) + (((var4 & 0xFFFFFFFF) >> 8) & 255)) - (((var6 & 0xFFFFFFFF) >> 8) & 255))
                var4 = (((((((((i32_load((var1 + var9)) & 0xFFFFFFFF) >> 24) + ((var4 & 0xFFFFFFFF) >> 24)) - ((i32_load((var6 - 4)) & 0xFFFFFFFF) >> 24)) if (1 if var5 < 256 else 0) else (((var5 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | ((((var7 & 255) + (var4 & 255)) - (var6 & 255)) if (1 if var5 < 256 else 0) else (((var5 ^ -1) & 0xFFFFFFFF) >> 24))) | (((((((var7 & 0xFFFFFFFF) >> 16) & 255) + (((var4 & 0xFFFFFFFF) >> 16) & 255)) - (((var6 & 0xFFFFFFFF) >> 16) & 255)) if (1 if var5 < 256 else 0) else (((var5 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | (((((((var7 & 0xFFFFFFFF) >> 8) & 255) + (((var4 & 0xFFFFFFFF) >> 8) & 255)) - (((var6 & 0xFFFFFFFF) >> 8) & 255)) if (1 if var4 < 256 else 0) else (((var4 ^ -1) & 0xFFFFFFFF) >> 24)) << 8))
                var7 = i32_load((var0 + var9))
                var4 = (((((((((((((i32_load((var1 + var9)) & 0xFFFFFFFF) >> 24) + ((var4 & 0xFFFFFFFF) >> 24)) - ((i32_load((var6 - 4)) & 0xFFFFFFFF) >> 24)) if (1 if var5 < 256 else 0) else (((var5 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | ((((var7 & 255) + (var4 & 255)) - (var6 & 255)) if (1 if var5 < 256 else 0) else (((var5 ^ -1) & 0xFFFFFFFF) >> 24))) | (((((((var7 & 0xFFFFFFFF) >> 16) & 255) + (((var4 & 0xFFFFFFFF) >> 16) & 255)) - (((var6 & 0xFFFFFFFF) >> 16) & 255)) if (1 if var5 < 256 else 0) else (((var5 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | (((((((var7 & 0xFFFFFFFF) >> 8) & 255) + (((var4 & 0xFFFFFFFF) >> 8) & 255)) - (((var6 & 0xFFFFFFFF) >> 8) & 255)) if (1 if var4 < 256 else 0) else (((var4 ^ -1) & 0xFFFFFFFF) >> 24)) << 8)) & -16711936) + (i32_load((var0 + var9)) & -16711936)) & -16711936) | (((var4 & 16711935) + (var7 & 16711935)) & 16711935))
                i32_store((var3 + (var8 << 2)), (((((((((((((i32_load((var1 + var9)) & 0xFFFFFFFF) >> 24) + ((var4 & 0xFFFFFFFF) >> 24)) - ((i32_load((var6 - 4)) & 0xFFFFFFFF) >> 24)) if (1 if var5 < 256 else 0) else (((var5 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | ((((var7 & 255) + (var4 & 255)) - (var6 & 255)) if (1 if var5 < 256 else 0) else (((var5 ^ -1) & 0xFFFFFFFF) >> 24))) | (((((((var7 & 0xFFFFFFFF) >> 16) & 255) + (((var4 & 0xFFFFFFFF) >> 16) & 255)) - (((var6 & 0xFFFFFFFF) >> 16) & 255)) if (1 if var5 < 256 else 0) else (((var5 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | (((((((var7 & 0xFFFFFFFF) >> 8) & 255) + (((var4 & 0xFFFFFFFF) >> 8) & 255)) - (((var6 & 0xFFFFFFFF) >> 8) & 255)) if (1 if var4 < 256 else 0) else (((var4 ^ -1) & 0xFFFFFFFF) >> 24)) << 8)) & -16711936) + (i32_load((var0 + var9)) & -16711936)) & -16711936) | (((var4 & 16711935) + (var7 & 16711935)) & 16711935)))
                var8 = (var8 + 1)
                if (1 if (var8 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func1048
# ==========================================================
def func1048(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    if var1:
        if (1 if var2 > 0 else 0):
            var5 = i32_load((var3 - 4))
            while True:  # loop $label0
                var12 = (var10 << 2)
                var6 = (var1 + var12)
                var7 = i32_load((var1 + var12))
                var6 = i32_load((var6 - 4))
                var4 = (i32_load((var6 - 4)) & 255)
                var8 = ((var5 & 255) - (i32_load((var6 - 4)) & 255))
                var8 = (var8 >> 31)
                var8 = ((var6 & 0xFFFFFFFF) >> 24)
                var9 = (((var5 & 0xFFFFFFFF) >> 24) - ((var6 & 0xFFFFFFFF) >> 24))
                var9 = (var9 >> 31)
                var9 = (((var6 & 0xFFFFFFFF) >> 8) & 255)
                var11 = ((((var5 & 0xFFFFFFFF) >> 8) & 255) - (((var6 & 0xFFFFFFFF) >> 8) & 255))
                var11 = (var11 >> 31)
                var4 = ((var7 & 255) - var4)
                var4 = (var4 >> 31)
                var4 = (((var7 & 0xFFFFFFFF) >> 24) - var8)
                var4 = (var4 >> 31)
                var4 = ((((var7 & 0xFFFFFFFF) >> 8) & 255) - var9)
                var4 = (var4 >> 31)
                var7 = (((var6 & 0xFFFFFFFF) >> 16) & 255)
                var6 = ((((var7 & 0xFFFFFFFF) >> 16) & 255) - (((var6 & 0xFFFFFFFF) >> 16) & 255))
                var6 = (var6 >> 31)
                var5 = ((((var5 & 0xFFFFFFFF) >> 16) & 255) - var7)
                var5 = (var5 >> 31)
                var5 = (i32_load((var1 + var12)) if (1 if ((((((((var5 & 255) - (i32_load((var6 - 4)) & 255)) ^ (var8 >> 31)) - var8) + (((((var5 & 0xFFFFFFFF) >> 24) - ((var6 & 0xFFFFFFFF) >> 24)) ^ (var9 >> 31)) - var9)) + ((((((var5 & 0xFFFFFFFF) >> 8) & 255) - (((var6 & 0xFFFFFFFF) >> 8) & 255)) ^ (var11 >> 31)) - var11)) - (((((((var7 & 255) - var4) ^ (var4 >> 31)) - var4) + (((((var7 & 0xFFFFFFFF) >> 24) - var8) ^ (var4 >> 31)) - var4)) + ((((((var7 & 0xFFFFFFFF) >> 8) & 255) - var9) ^ (var4 >> 31)) - var4)) + ((((((var7 & 0xFFFFFFFF) >> 16) & 255) - (((var6 & 0xFFFFFFFF) >> 16) & 255)) ^ (var6 >> 31)) - var6))) + ((((((var5 & 0xFFFFFFFF) >> 16) & 255) - var7) ^ (var5 >> 31)) - var5)) <= 0 else 0) else var5)
                var7 = i32_load((var0 + var12))
                var5 = (((((i32_load((var1 + var12)) if (1 if ((((((((var5 & 255) - (i32_load((var6 - 4)) & 255)) ^ (var8 >> 31)) - var8) + (((((var5 & 0xFFFFFFFF) >> 24) - ((var6 & 0xFFFFFFFF) >> 24)) ^ (var9 >> 31)) - var9)) + ((((((var5 & 0xFFFFFFFF) >> 8) & 255) - (((var6 & 0xFFFFFFFF) >> 8) & 255)) ^ (var11 >> 31)) - var11)) - (((((((var7 & 255) - var4) ^ (var4 >> 31)) - var4) + (((((var7 & 0xFFFFFFFF) >> 24) - var8) ^ (var4 >> 31)) - var4)) + ((((((var7 & 0xFFFFFFFF) >> 8) & 255) - var9) ^ (var4 >> 31)) - var4)) + ((((((var7 & 0xFFFFFFFF) >> 16) & 255) - (((var6 & 0xFFFFFFFF) >> 16) & 255)) ^ (var6 >> 31)) - var6))) + ((((((var5 & 0xFFFFFFFF) >> 16) & 255) - var7) ^ (var5 >> 31)) - var5)) <= 0 else 0) else var5) & -16711936) + (i32_load((var0 + var12)) & -16711936)) & -16711936) | (((var5 & 16711935) + (var7 & 16711935)) & 16711935))
                i32_store((var3 + (var10 << 2)), (((((i32_load((var1 + var12)) if (1 if ((((((((var5 & 255) - (i32_load((var6 - 4)) & 255)) ^ (var8 >> 31)) - var8) + (((((var5 & 0xFFFFFFFF) >> 24) - ((var6 & 0xFFFFFFFF) >> 24)) ^ (var9 >> 31)) - var9)) + ((((((var5 & 0xFFFFFFFF) >> 8) & 255) - (((var6 & 0xFFFFFFFF) >> 8) & 255)) ^ (var11 >> 31)) - var11)) - (((((((var7 & 255) - var4) ^ (var4 >> 31)) - var4) + (((((var7 & 0xFFFFFFFF) >> 24) - var8) ^ (var4 >> 31)) - var4)) + ((((((var7 & 0xFFFFFFFF) >> 8) & 255) - var9) ^ (var4 >> 31)) - var4)) + ((((((var7 & 0xFFFFFFFF) >> 16) & 255) - (((var6 & 0xFFFFFFFF) >> 16) & 255)) ^ (var6 >> 31)) - var6))) + ((((((var5 & 0xFFFFFFFF) >> 16) & 255) - var7) ^ (var5 >> 31)) - var5)) <= 0 else 0) else var5) & -16711936) + (i32_load((var0 + var12)) & -16711936)) & -16711936) | (((var5 & 16711935) + (var7 & 16711935)) & 16711935)))
                var10 = (var10 + 1)
                if (1 if (var10 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func1049
# ==========================================================
def func1049(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    if var1:
        if (1 if var2 > 0 else 0):
            var4 = i32_load((var3 - 4))
            while True:  # loop $label0
                var5 = (var7 << 2)
                var6 = (var1 + var5)
                var8 = i32_load((var1 + var5) + 4)
                var9 = i32_load(var6)
                var8 = (((((i32_load((var1 + var5) + 4) ^ i32_load(var6)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var8 & var9))
                var6 = i32_load((var6 - 4))
                var4 = (((((i32_load((var6 - 4)) ^ var4) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var6))
                var4 = ((((((((((i32_load((var1 + var5) + 4) ^ i32_load(var6)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var8 & var9)) ^ (((((i32_load((var6 - 4)) ^ var4) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var6))) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var8))
                var5 = i32_load((var0 + var5))
                var4 = ((((((((((((((i32_load((var1 + var5) + 4) ^ i32_load(var6)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var8 & var9)) ^ (((((i32_load((var6 - 4)) ^ var4) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var6))) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var8)) & -16711936) + (i32_load((var0 + var5)) & -16711936)) & -16711936) | (((var4 & 16711935) + (var5 & 16711935)) & 16711935))
                i32_store((var3 + (var7 << 2)), ((((((((((((((i32_load((var1 + var5) + 4) ^ i32_load(var6)) & 0xFFFFFFFF) >> 1) & 2139062143) + (var8 & var9)) ^ (((((i32_load((var6 - 4)) ^ var4) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var6))) & 0xFFFFFFFF) >> 1) & 2139062143) + (var4 & var8)) & -16711936) + (i32_load((var0 + var5)) & -16711936)) & -16711936) | (((var4 & 16711935) + (var5 & 16711935)) & 16711935)))
                var7 = (var7 + 1)
                if (1 if (var7 + 1) != var2 else 0):
                    continue
                break  # end loop
        return
    a_c()
    raise RuntimeError('unreachable')

