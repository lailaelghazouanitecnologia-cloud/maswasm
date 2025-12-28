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
# $func963
# ==========================================================
def func963(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    if (1 if var4 > 0 else 0):
        while True:  # loop $label0
            var7 = i32_load8_u((var2 + var5))
            var11 = i32_load8_u((var1 + var5))
            var8 = i32_load8_u((var0 + var5))
            var6 = (var3 + (var5 << 2))
            i32_store8((var3 + (var5 << 2)) + 3, 255)
            var8 = (((var8 * 19077) & 0xFFFFFFFF) >> 8)
            var9 = ((((var8 * 19077) & 0xFFFFFFFF) >> 8) + (((var11 * 33050) & 0xFFFFFFFF) >> 8))
            var10 = (((((var8 * 19077) & 0xFFFFFFFF) >> 8) + (((var11 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8(var6 + 2, ((((((((var8 * 19077) & 0xFFFFFFFF) >> 8) + (((var11 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var10 < 16384 else 0) else (255 if (1 if var9 >= 17685 else 0) else 0)))
            var9 = ((((var7 * 26149) & 0xFFFFFFFF) >> 8) + var8)
            var10 = (((((var7 * 26149) & 0xFFFFFFFF) >> 8) + var8) - 14234)
            i32_store8(var6, ((((((((var7 * 26149) & 0xFFFFFFFF) >> 8) + var8) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var10 < 16384 else 0) else (255 if (1 if var9 >= 14234 else 0) else 0)))
            var6 = (var8 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var7 * 13320) & 0xFFFFFFFF) >> 8)))
            var7 = ((var8 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var7 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var6 + 1, (((((var8 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var7 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var6 >= -8708 else 0) else 0)))
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var4 else 0):
                continue
            break  # end loop


# ==========================================================
# $func964
# ==========================================================
def func964(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    if (1 if var4 > 0 else 0):
        while True:  # loop $label0
            var6 = i32_load8_u((var2 + var5))
            var8 = (var3 + (var5 << 1))
            var7 = (((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8)
            var10 = i32_load8_u((var1 + var5))
            var9 = ((((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u((var1 + var5)) * 33050) & 0xFFFFFFFF) >> 8))
            var11 = (((((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u((var1 + var5)) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8((var3 + (var5 << 1)) + 1, (((((((((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u((var1 + var5)) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var11 < 16384 else 0) else (240 if (1 if var9 >= 17685 else 0) else 0)) | 15))
            var8 = ((((var6 * 26149) & 0xFFFFFFFF) >> 8) + var7)
            var9 = (((((var6 * 26149) & 0xFFFFFFFF) >> 8) + var7) - 14234)
            var6 = (var7 - ((((var10 * 6419) & 0xFFFFFFFF) >> 8) + (((var6 * 13320) & 0xFFFFFFFF) >> 8)))
            var7 = ((var7 - ((((var10 * 6419) & 0xFFFFFFFF) >> 8) + (((var6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var8, ((((((((((var6 * 26149) & 0xFFFFFFFF) >> 8) + var7) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (240 if (1 if var8 >= 14234 else 0) else 0)) & 240) | (((((var7 - ((((var10 * 6419) & 0xFFFFFFFF) >> 8) + (((var6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (1 if var7 < 16384 else 0) else (15 if (1 if var6 >= -8708 else 0) else 0))))
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var4 else 0):
                continue
            break  # end loop


# ==========================================================
# $func965
# ==========================================================
def func965(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    if (1 if var4 > 0 else 0):
        while True:  # loop $label0
            var6 = i32_load8_u((var2 + var5))
            var7 = (var3 + (var5 * 3))
            var10 = (((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8)
            var11 = i32_load8_u((var1 + var5))
            var8 = ((((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u((var1 + var5)) * 33050) & 0xFFFFFFFF) >> 8))
            var9 = (((((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u((var1 + var5)) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8((var3 + (var5 * 3)) + 2, ((((((((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u((var1 + var5)) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var8 >= 17685 else 0) else 0)))
            var8 = ((((var6 * 26149) & 0xFFFFFFFF) >> 8) + var10)
            var9 = (((((var6 * 26149) & 0xFFFFFFFF) >> 8) + var10) - 14234)
            i32_store8(var7, ((((((((var6 * 26149) & 0xFFFFFFFF) >> 8) + var10) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var8 >= 14234 else 0) else 0)))
            var6 = (var10 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var6 * 13320) & 0xFFFFFFFF) >> 8)))
            var7 = ((var10 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var7 + 1, (((((var10 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var6 >= -8708 else 0) else 0)))
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var4 else 0):
                continue
            break  # end loop


# ==========================================================
# $func966
# ==========================================================
def func966(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    if (1 if var4 > 0 else 0):
        while True:  # loop $label0
            var8 = (var3 + (var5 << 1))
            var7 = (((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8)
            var6 = i32_load8_u((var2 + var5))
            var9 = ((((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u((var2 + var5)) * 26149) & 0xFFFFFFFF) >> 8))
            var10 = (((((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u((var2 + var5)) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            var9 = i32_load8_u((var1 + var5))
            var6 = (var7 - ((((i32_load8_u((var1 + var5)) * 6419) & 0xFFFFFFFF) >> 8) + (((var6 * 13320) & 0xFFFFFFFF) >> 8)))
            var10 = ((var7 - ((((i32_load8_u((var1 + var5)) * 6419) & 0xFFFFFFFF) >> 8) + (((var6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            var6 = (((((var7 - ((((i32_load8_u((var1 + var5)) * 6419) & 0xFFFFFFFF) >> 8) + (((var6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var10 < 16384 else 0) else (255 if (1 if var6 >= -8708 else 0) else 0))
            i32_store8((var3 + (var5 << 1)), ((((((((((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u((var2 + var5)) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var10 < 16384 else 0) else (248 if (1 if var9 >= 14234 else 0) else 0)) & 248) | (((((((var7 - ((((i32_load8_u((var1 + var5)) * 6419) & 0xFFFFFFFF) >> 8) + (((var6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var10 < 16384 else 0) else (255 if (1 if var6 >= -8708 else 0) else 0)) & 0xFFFFFFFF) >> 5)))
            var7 = ((((var9 * 33050) & 0xFFFFFFFF) >> 8) + var7)
            var8 = (((((var9 * 33050) & 0xFFFFFFFF) >> 8) + var7) - 17685)
            i32_store8(var8 + 1, (((var6 << 3) & 224) | ((((((((var9 * 33050) & 0xFFFFFFFF) >> 8) + var7) - 17685) & 0xFFFFFFFF) >> 9) if (1 if var8 < 16384 else 0) else (31 if (1 if var7 >= 17685 else 0) else 0))))
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var4 else 0):
                continue
            break  # end loop


# ==========================================================
# $func967
# ==========================================================
def func967(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    if (1 if var4 > 0 else 0):
        while True:  # loop $label0
            var7 = i32_load8_u((var1 + var5))
            var11 = i32_load8_u((var2 + var5))
            var8 = i32_load8_u((var0 + var5))
            var6 = (var3 + (var5 << 2))
            i32_store8((var3 + (var5 << 2)) + 3, 255)
            var8 = (((var8 * 19077) & 0xFFFFFFFF) >> 8)
            var9 = ((((var8 * 19077) & 0xFFFFFFFF) >> 8) + (((var11 * 26149) & 0xFFFFFFFF) >> 8))
            var10 = (((((var8 * 19077) & 0xFFFFFFFF) >> 8) + (((var11 * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            i32_store8(var6 + 2, ((((((((var8 * 19077) & 0xFFFFFFFF) >> 8) + (((var11 * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var10 < 16384 else 0) else (255 if (1 if var9 >= 14234 else 0) else 0)))
            var9 = ((((var7 * 33050) & 0xFFFFFFFF) >> 8) + var8)
            var10 = (((((var7 * 33050) & 0xFFFFFFFF) >> 8) + var8) - 17685)
            i32_store8(var6, ((((((((var7 * 33050) & 0xFFFFFFFF) >> 8) + var8) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var10 < 16384 else 0) else (255 if (1 if var9 >= 17685 else 0) else 0)))
            var6 = (var8 - ((((var7 * 6419) & 0xFFFFFFFF) >> 8) + (((var11 * 13320) & 0xFFFFFFFF) >> 8)))
            var7 = ((var8 - ((((var7 * 6419) & 0xFFFFFFFF) >> 8) + (((var11 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var6 + 1, (((((var8 - ((((var7 * 6419) & 0xFFFFFFFF) >> 8) + (((var11 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var6 >= -8708 else 0) else 0)))
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var4 else 0):
                continue
            break  # end loop


# ==========================================================
# $func968
# ==========================================================
def func968(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    if (1 if var4 > 0 else 0):
        while True:  # loop $label0
            var6 = i32_load8_u((var1 + var5))
            var7 = (var3 + (var5 * 3))
            var10 = (((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8)
            var11 = i32_load8_u((var2 + var5))
            var8 = ((((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u((var2 + var5)) * 26149) & 0xFFFFFFFF) >> 8))
            var9 = (((((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u((var2 + var5)) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            i32_store8((var3 + (var5 * 3)) + 2, ((((((((i32_load8_u((var0 + var5)) * 19077) & 0xFFFFFFFF) >> 8) + (((i32_load8_u((var2 + var5)) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var8 >= 14234 else 0) else 0)))
            var8 = ((((var6 * 33050) & 0xFFFFFFFF) >> 8) + var10)
            var9 = (((((var6 * 33050) & 0xFFFFFFFF) >> 8) + var10) - 17685)
            i32_store8(var7, ((((((((var6 * 33050) & 0xFFFFFFFF) >> 8) + var10) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var9 < 16384 else 0) else (255 if (1 if var8 >= 17685 else 0) else 0)))
            var6 = (var10 - ((((var6 * 6419) & 0xFFFFFFFF) >> 8) + (((var11 * 13320) & 0xFFFFFFFF) >> 8)))
            var7 = ((var10 - ((((var6 * 6419) & 0xFFFFFFFF) >> 8) + (((var11 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var7 + 1, (((((var10 - ((((var6 * 6419) & 0xFFFFFFFF) >> 8) + (((var11 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var6 >= -8708 else 0) else 0)))
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var4 else 0):
                continue
            break  # end loop


# ==========================================================
# $func969
# ==========================================================
def func969(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    if (1 if var4 > 0 else 0):
        while True:  # loop $label0
            var7 = i32_load8_u((var2 + var5))
            var11 = i32_load8_u((var1 + var5))
            var8 = i32_load8_u((var0 + var5))
            var6 = (var3 + (var5 << 2))
            i32_store8((var3 + (var5 << 2)), 255)
            var8 = (((var8 * 19077) & 0xFFFFFFFF) >> 8)
            var9 = ((((var8 * 19077) & 0xFFFFFFFF) >> 8) + (((var11 * 33050) & 0xFFFFFFFF) >> 8))
            var10 = (((((var8 * 19077) & 0xFFFFFFFF) >> 8) + (((var11 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            i32_store8(var6 + 3, ((((((((var8 * 19077) & 0xFFFFFFFF) >> 8) + (((var11 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (1 if var10 < 16384 else 0) else (255 if (1 if var9 >= 17685 else 0) else 0)))
            var9 = ((((var7 * 26149) & 0xFFFFFFFF) >> 8) + var8)
            var10 = (((((var7 * 26149) & 0xFFFFFFFF) >> 8) + var8) - 14234)
            i32_store8(var6 + 1, ((((((((var7 * 26149) & 0xFFFFFFFF) >> 8) + var8) - 14234) & 0xFFFFFFFF) >> 6) if (1 if var10 < 16384 else 0) else (255 if (1 if var9 >= 14234 else 0) else 0)))
            var6 = (var8 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var7 * 13320) & 0xFFFFFFFF) >> 8)))
            var7 = ((var8 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var7 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            i32_store8(var6 + 2, (((((var8 - ((((var11 * 6419) & 0xFFFFFFFF) >> 8) + (((var7 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (1 if var7 < 16384 else 0) else (255 if (1 if var6 >= -8708 else 0) else 0)))
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var4 else 0):
                continue
            break  # end loop


# ==========================================================
# $func974
# ==========================================================
def func974(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    if (1 if var2 <= 0 else 0):
        break
    if (1 if var3 == 0 else 0):
        while True:  # loop $label2
            var3 = i32_load8_u((var1 + var4))
            if (1 if i32_load8_u((var1 + var4)) == 255 else 0):
                break
            if (1 if var3 == 0 else 0):
                i32_store8((var0 + var4), 0)
                break
            var5 = (var0 + var4)
            i32_store8((var0 + var4), (((((var3 * i32_load8_u(var5)) * 65793) + 8388608) & 0xFFFFFFFF) >> 24))
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var2 else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    while True:  # loop $label4
        var3 = i32_load8_u((var1 + var4))
        if (1 if i32_load8_u((var1 + var4)) == 255 else 0):
            break
        if (1 if var3 == 0 else 0):
            i32_store8((var0 + var4), 0)
            break
        var5 = (var0 + var4)
        i32_store8((var0 + var4), ((((i32_load8_u(var5) * ((-16777216 & 0xFFFFFFFF) // var3)) + 8388608) & 0xFFFFFFFF) >> 24))
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var2 else 0):
            continue
        break  # end loop


# ==========================================================
# $func975
# ==========================================================
def func975(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    if (1 if var1 <= 0 else 0):
        break
    if (1 if var2 == 0 else 0):
        while True:  # loop $label1
            var5 = (var0 + (var4 << 2))
            var2 = i32_load((var0 + (var4 << 2)))
            if (1 if i32_load((var0 + (var4 << 2))) <= -16777217 else 0):
                var3 = 0
                if (1 if var2 >= 16777216 else 0):
                    var3 = (((var2 & 0xFFFFFFFF) >> 24) * 65793)
                else:
                i32_store(((((var2 & -16777216) | (((((((var2 & 0xFFFFFFFF) >> 24) * 65793) * (var2 & 255)) + 8388608) & 0xFFFFFFFF) >> 24)) | (((((var3 * (((var2 & 0xFFFFFFFF) >> 8) & 255)) + 8388608) & 0xFFFFFFFF) >> 16) & 65280)) | (((((var3 * (((var2 & 0xFFFFFFFF) >> 16) & 255)) + 8388608) & 0xFFFFFFFF) >> 8) & 16711680)), 0)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var1 else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    while True:  # loop $label2
        var5 = (var0 + (var4 << 2))
        var2 = i32_load((var0 + (var4 << 2)))
        if (1 if i32_load((var0 + (var4 << 2))) <= -16777217 else 0):
            var3 = 0
            if (1 if var2 >= 16777216 else 0):
                var3 = ((-16777216 & 0xFFFFFFFF) // ((var2 & 0xFFFFFFFF) >> 24))
            else:
            i32_store(((((var2 & -16777216) | ((((((-16777216 & 0xFFFFFFFF) // ((var2 & 0xFFFFFFFF) >> 24)) * (var2 & 255)) + 8388608) & 0xFFFFFFFF) >> 24)) | (((((var3 * (((var2 & 0xFFFFFFFF) >> 8) & 255)) + 8388608) & 0xFFFFFFFF) >> 16) & 65280)) | (((((var3 * (((var2 & 0xFFFFFFFF) >> 16) & 255)) + 8388608) & 0xFFFFFFFF) >> 8) & 16711680)), 0)
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var1 else 0):
            continue
        break  # end loop
    return var5


# ==========================================================
# $func976
# ==========================================================
def func976(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    if (1 if var3 > 0 else 0):
        while True:  # loop $label0
            var5 = i32_load16_u(var0 + 2)
            var6 = i32_load16_u(var0)
            var7 = i32_load16_u(var0 + 4)
            var8 = (((i32_load16_u(var0 + 2) * -19081) + (i32_load16_u(var0) * -9719)) + (i32_load16_u(var0 + 4) * 28800))
            var9 = ((((i32_load16_u(var0 + 2) * -19081) + (i32_load16_u(var0) * -9719)) + (i32_load16_u(var0 + 4) * 28800)) + 33685504)
            i32_store8((var1 + var4), (((((((i32_load16_u(var0 + 2) * -19081) + (i32_load16_u(var0) * -9719)) + (i32_load16_u(var0 + 4) * 28800)) + 33685504) & 0xFFFFFFFF) >> 18) if (1 if var9 < 67108864 else 0) else (-33685504 if (1 if var8 < -33685504 else 0) else 255)))
            var5 = (((var5 * -24116) + (var6 * 28800)) + (var7 * -4684))
            var6 = ((((var5 * -24116) + (var6 * 28800)) + (var7 * -4684)) + 33685504)
            i32_store8((var2 + var4), (((((((var5 * -24116) + (var6 * 28800)) + (var7 * -4684)) + 33685504) & 0xFFFFFFFF) >> 18) if (1 if var6 < 67108864 else 0) else (-33685504 if (1 if var5 < -33685504 else 0) else 255)))
            var0 = (var0 + 8)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var3 else 0):
                continue
            break  # end loop

