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
# $func463
# ==========================================================
def func463(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var7 = i32_load(var0 + 8)
    var5 = i32_load8_u(var1 + 3)
    var4 = i32_load(var0 + 12)
    if (1 if i32_load(var0 + 12) >= 0 else 0):
        break
    var6 = i32_load(var0 + 16)
    if (1 if i32_load(var0 + 16) == 0 else 0):
        break
    if (1 if i32_load(var0 + 24) > var6 else 0):
        var3 = i64_load(var6)
        i32_store(var0 + 16, (var6 + 7))
        i64_store(var0, ((i64_load(var0) << 56) | ((((((var3 << 56) | ((var3 & 65280) << 40)) | (((var3 & 16711680) << 24) | ((var3 & 4278190080) << 8))) | ((((var3 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var3 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var3 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
        var4 = (var4 + 56)
        break
    func36(var0)
    var4 = i32_load(var0 + 12)
    var5 = (((var5 * var7) & 0xFFFFFFFF) >> 8)
    var3 = i64_load(var0)
    var2 = i64_extend_u(var4)
    var8 = i32(((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4)))
    if (1 if (((var5 * var7) & 0xFFFFFFFF) >> 8) < i32(((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4))) else 0):
        var3 = (var3 - (i64_extend_u((var5 + 1)) << var2))
        i64_store(var0, (var3 - (i64_extend_u((var5 + 1)) << var2)))
        break
    var6 = (var5 + 1)
    var7 = (clz32((var5 + 1)) ^ 24)
    var4 = ((var7 - var5) - (clz32((var5 + 1)) ^ 24))
    i32_store(var4 + 12, ((var7 - var5) - (clz32((var5 + 1)) ^ 24)))
    var6 = ((var6 << var7) - 1)
    i32_store(var0 + 8, ((var6 << var7) - 1))
    if (1 if var5 >= var8 else 0):
        var7 = i32_load8_u(var1 + 4)
        if (1 if var4 >= 0 else 0):
            break
        var5 = i32_load(var0 + 16)
        if (1 if i32_load(var0 + 16) == 0 else 0):
            break
        if (1 if i32_load(var0 + 24) > var5 else 0):
            var2 = i64_load(var5)
            i32_store(var0 + 16, (var5 + 7))
            var3 = ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
            i64_store(var0, ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
            var4 = (var4 + 56)
            break
        func36(var0)
        var3 = i64_load(var0)
        var4 = i32_load(var0 + 12)
        var5 = (((var6 * var7) & 0xFFFFFFFF) >> 8)
        var2 = i64_extend_u(var4)
        var7 = (1 if (((var6 * var7) & 0xFFFFFFFF) >> 8) >= i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4))) else 0)
        if (1 if (1 if (((var6 * var7) & 0xFFFFFFFF) >> 8) >= i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4))) else 0) == 0 else 0):
            var3 = (var3 - (i64_extend_u((var5 + 1)) << var2))
            i64_store(var0, (var3 - (i64_extend_u((var5 + 1)) << var2)))
            break
        var5 = (var5 + 1)
        var6 = (clz32((var5 + 1)) ^ 24)
        var4 = ((var6 - var5) - (clz32((var5 + 1)) ^ 24))
        i32_store(var4 + 12, ((var6 - var5) - (clz32((var5 + 1)) ^ 24)))
        var6 = ((var5 << var6) - 1)
        i32_store(var0 + 8, ((var5 << var6) - 1))
        if var7:
            break
        var5 = i32_load8_u(var1 + 5)
        if (1 if var4 >= 0 else 0):
            break
        var1 = i32_load(var0 + 16)
        if (1 if i32_load(var0 + 16) == 0 else 0):
            break
        if (1 if i32_load(var0 + 24) > var1 else 0):
            var2 = i64_load(var1)
            i32_store(var0 + 16, (var1 + 7))
            var3 = ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
            i64_store(var0, ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
            var4 = (var4 + 56)
            break
        func36(var0)
        var3 = i64_load(var0)
        var4 = i32_load(var0 + 12)
        var1 = (((var5 * var6) & 0xFFFFFFFF) >> 8)
        var2 = i64_extend_u(var4)
        if (1 if (((var5 * var6) & 0xFFFFFFFF) >> 8) < i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4))) else 0):
            i64_store(var0, (var3 - (i64_extend_u((var1 + 1)) << var2)))
            var5 = 4
            break
        var5 = 3
        var1 = (var1 + 1)
        var4 = (clz32((var1 + 1)) ^ 24)
        i32_store(var4 + 12, ((var6 - var1) - (clz32((var1 + 1)) ^ 24)))
        break
    var7 = i32_load8_u(var1 + 6)
    if (1 if var4 >= 0 else 0):
        break
    var5 = i32_load(var0 + 16)
    if (1 if i32_load(var0 + 16) == 0 else 0):
        break
    if (1 if i32_load(var0 + 24) > var5 else 0):
        var2 = i64_load(var5)
        i32_store(var0 + 16, (var5 + 7))
        var3 = ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
        i64_store(var0, ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
        var4 = (var4 + 56)
        break
    func36(var0)
    var3 = i64_load(var0)
    var4 = i32_load(var0 + 12)
    var5 = (((var6 * var7) & 0xFFFFFFFF) >> 8)
    var2 = i64_extend_u(var4)
    var7 = i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4)))
    if (1 if (((var6 * var7) & 0xFFFFFFFF) >> 8) < i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4))) else 0):
        var3 = (var3 - (i64_extend_u((var5 + 1)) << var2))
        i64_store(var0, (var3 - (i64_extend_u((var5 + 1)) << var2)))
        break
    var6 = (var5 + 1)
    var8 = (clz32((var5 + 1)) ^ 24)
    var4 = ((var6 - var5) - (clz32((var5 + 1)) ^ 24))
    i32_store(var4 + 12, ((var6 - var5) - (clz32((var5 + 1)) ^ 24)))
    var6 = ((var6 << var8) - 1)
    i32_store(var0 + 8, ((var6 << var8) - 1))
    if (1 if var5 >= var7 else 0):
        var5 = i32_load8_u(var1 + 7)
        if (1 if var4 >= 0 else 0):
            break
        var1 = i32_load(var0 + 16)
        if (1 if i32_load(var0 + 16) == 0 else 0):
            break
        if (1 if i32_load(var0 + 24) > var1 else 0):
            var2 = i64_load(var1)
            i32_store(var0 + 16, (var1 + 7))
            var3 = ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
            i64_store(var0, ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
            var4 = (var4 + 56)
            break
        func36(var0)
        var3 = i64_load(var0)
        var4 = i32_load(var0 + 12)
        var1 = (((var5 * var6) & 0xFFFFFFFF) >> 8)
        var2 = i64_extend_u(var4)
        var7 = i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4)))
        if (1 if (((var5 * var6) & 0xFFFFFFFF) >> 8) < i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4))) else 0):
            var3 = (var3 - (i64_extend_u((var1 + 1)) << var2))
            i64_store(var0, (var3 - (i64_extend_u((var1 + 1)) << var2)))
            break
        var5 = (var1 + 1)
        var6 = (clz32((var1 + 1)) ^ 24)
        var4 = ((var6 - var1) - (clz32((var1 + 1)) ^ 24))
        i32_store(var4 + 12, ((var6 - var1) - (clz32((var1 + 1)) ^ 24)))
        var6 = ((var5 << var6) - 1)
        i32_store(var0 + 8, ((var5 << var6) - 1))
        if (1 if var1 >= var7 else 0):
            if (1 if var4 >= 0 else 0):
                break
            var1 = i32_load(var0 + 16)
            if (1 if i32_load(var0 + 16) == 0 else 0):
                break
            if (1 if i32_load(var0 + 24) > var1 else 0):
                var2 = i64_load(var1)
                i32_store(var0 + 16, (var1 + 7))
                var3 = ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                i64_store(var0, ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                var4 = (var4 + 56)
                break
            func36(var0)
            var3 = i64_load(var0)
            var4 = i32_load(var0 + 12)
            var1 = (((var6 * 159) & 0xFFFFFFFF) >> 8)
            var2 = i64_extend_u(var4)
            if (1 if (((var6 * 159) & 0xFFFFFFFF) >> 8) < i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4))) else 0):
                i64_store(var0, (var3 - (i64_extend_u((var1 + 1)) << var2)))
                var5 = 6
                break
            var5 = 5
            var1 = (var1 + 1)
            var4 = (clz32((var1 + 1)) ^ 24)
            i32_store(var4 + 12, ((var6 - var1) - (clz32((var1 + 1)) ^ 24)))
            break
        if (1 if var4 >= 0 else 0):
            break
        var1 = i32_load(var0 + 16)
        if (1 if i32_load(var0 + 16) == 0 else 0):
            break
        if (1 if i32_load(var0 + 24) > var1 else 0):
            var2 = i64_load(var1)
            i32_store(var0 + 16, (var1 + 7))
            var3 = ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
            i64_store(var0, ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
            var4 = (var4 + 56)
            break
        func36(var0)
        var3 = i64_load(var0)
        var4 = i32_load(var0 + 12)
        var1 = (((var6 * 165) & 0xFFFFFFFF) >> 8)
        var2 = i64_extend_u(var4)
        if (1 if (((var6 * 165) & 0xFFFFFFFF) >> 8) < i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4))) else 0):
            var3 = (var3 - (i64_extend_u((var1 + 1)) << var2))
            i64_store(var0, (var3 - (i64_extend_u((var1 + 1)) << var2)))
            var1 = (var6 - var1)
            break
        var1 = (var1 + 1)
        var6 = 7
        var5 = (clz32(var1) ^ 24)
        var4 = (var4 - (clz32(var1) ^ 24))
        i32_store(var0 + 12, (var4 - (clz32(var1) ^ 24)))
        var5 = ((var1 << var5) - 1)
        i32_store(var0 + 8, ((var1 << var5) - 1))
        if (1 if var4 >= 0 else 0):
            break
        var1 = i32_load(var0 + 16)
        if (1 if i32_load(var0 + 16) == 0 else 0):
            break
        if (1 if i32_load(var0 + 24) > var1 else 0):
            var2 = i64_load(var1)
            i32_store(var0 + 16, (var1 + 7))
            var3 = ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
            i64_store(var0, ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
            var4 = (var4 + 56)
            break
        func36(var0)
        var3 = i64_load(var0)
        var4 = i32_load(var0 + 12)
        var1 = (((var5 * 145) & 0xFFFFFFFF) >> 8)
        var2 = i64_extend_u(var4)
        var7 = i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4)))
        if (1 if (((var5 * 145) & 0xFFFFFFFF) >> 8) < i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4))) else 0):
            i64_store(var0, (var3 - (i64_extend_u((var1 + 1)) << var2)))
            break
        var5 = (var1 + 1)
        var4 = (clz32((var1 + 1)) ^ 24)
        i32_store(var4 + 12, ((var5 - var1) - (clz32((var1 + 1)) ^ 24)))
        i32_store(var0 + 8, ((var5 << var4) - 1))
        return (var6 + (1 if var1 < var7 else 0))
    var7 = i32_load8_u(var1 + 8)
    if (1 if var4 >= 0 else 0):
        break
    var5 = i32_load(var0 + 16)
    if (1 if i32_load(var0 + 16) == 0 else 0):
        break
    if (1 if i32_load(var0 + 24) > var5 else 0):
        var2 = i64_load(var5)
        i32_store(var0 + 16, (var5 + 7))
        var3 = ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
        i64_store(var0, ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
        var4 = (var4 + 56)
        break
    func36(var0)
    var3 = i64_load(var0)
    var4 = i32_load(var0 + 12)
    var5 = (((var6 * var7) & 0xFFFFFFFF) >> 8)
    var2 = i64_extend_u(var4)
    var8 = i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4)))
    if (1 if (((var6 * var7) & 0xFFFFFFFF) >> 8) < i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4))) else 0):
        var3 = (var3 - (i64_extend_u((var5 + 1)) << var2))
        i64_store(var0, (var3 - (i64_extend_u((var5 + 1)) << var2)))
        var7 = 10
        break
    var7 = 9
    var6 = (var5 + 1)
    var9 = (clz32((var5 + 1)) ^ 24)
    var4 = ((var6 - var5) - (clz32((var5 + 1)) ^ 24))
    i32_store(var4 + 12, ((var6 - var5) - (clz32((var5 + 1)) ^ 24)))
    var6 = ((var6 << var9) - 1)
    i32_store(var0 + 8, ((var6 << var9) - 1))
    var7 = i32_load8_u((var1 + var7))
    if (1 if var4 >= 0 else 0):
        break
    var1 = i32_load(var0 + 16)
    if (1 if i32_load(var0 + 16) == 0 else 0):
        break
    if (1 if i32_load(var0 + 24) > var1 else 0):
        var2 = i64_load(var1)
        i32_store(var0 + 16, (var1 + 7))
        var3 = ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
        i64_store(var0, ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
        var4 = (var4 + 56)
        break
    func36(var0)
    var3 = i64_load(var0)
    var4 = i32_load(var0 + 12)
    var1 = (((var6 * var7) & 0xFFFFFFFF) >> 8)
    var2 = i64_extend_u(var4)
    var7 = i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4)))
    if (1 if (((var6 * var7) & 0xFFFFFFFF) >> 8) < i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4))) else 0):
        var3 = (var3 - (i64_extend_u((var1 + 1)) << var2))
        i64_store(var0, (var3 - (i64_extend_u((var1 + 1)) << var2)))
        break
    var6 = (var1 + 1)
    var9 = (clz32((var1 + 1)) ^ 24)
    var4 = ((var6 - var1) - (clz32((var1 + 1)) ^ 24))
    i32_store(var4 + 12, ((var6 - var1) - (clz32((var1 + 1)) ^ 24)))
    var6 = ((var6 << var9) - 1)
    i32_store(var0 + 8, ((var6 << var9) - 1))
    var9 = (((1 if var5 < var8 else 0) << 1) | (1 if var1 < var7 else 0))
    var5 = i32_load((((((1 if var5 < var8 else 0) << 1) | (1 if var1 < var7 else 0)) << 2) + 13984))
    var1 = i32_load8_u(i32_load((((((1 if var5 < var8 else 0) << 1) | (1 if var1 < var7 else 0)) << 2) + 13984)))
    if (1 if i32_load8_u(i32_load((((((1 if var5 < var8 else 0) << 1) | (1 if var1 < var7 else 0)) << 2) + 13984))) == 0 else 0):
        var7 = 0
        break
    var7 = 0
    while True:  # loop $label26
        if (1 if var4 >= 0 else 0):
            break
        var8 = i32_load(var0 + 16)
        if (1 if i32_load(var0 + 16) == 0 else 0):
            break
        if (1 if i32_load(var0 + 24) > var8 else 0):
            var2 = i64_load(var8)
            i32_store(var0 + 16, (var8 + 7))
            var3 = ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
            i64_store(var0, ((var3 << 56) | ((((((var2 << 56) | ((var2 & 65280) << 40)) | (((var2 & 16711680) << 24) | ((var2 & 4278190080) << 8))) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
            var4 = (var4 + 56)
            break
        func36(var0)
        var3 = i64_load(var0)
        var4 = i32_load(var0 + 12)
        var1 = (((var6 * (var1 & 255)) & 0xFFFFFFFF) >> 8)
        var2 = i64_extend_u(var4)
        var8 = i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4)))
        if (1 if (((var6 * (var1 & 255)) & 0xFFFFFFFF) >> 8) < i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var4))) else 0):
            var3 = (var3 - (i64_extend_u((var1 + 1)) << var2))
            i64_store(var0, (var3 - (i64_extend_u((var1 + 1)) << var2)))
            break
        var6 = (var1 + 1)
        var10 = (clz32((var1 + 1)) ^ 24)
        var4 = ((var6 - var1) - (clz32((var1 + 1)) ^ 24))
        i32_store(var4 + 12, ((var6 - var1) - (clz32((var1 + 1)) ^ 24)))
        var6 = ((var6 << var10) - 1)
        i32_store(var0 + 8, ((var6 << var10) - 1))
        var7 = ((var7 << 1) | (1 if var1 < var8 else 0))
        var1 = i32_load8_u(var5 + 1)
        var5 = (var5 + 1)
        if var1:
            continue
        break  # end loop
    return ((var7 + (8 << var9)) + 3)
    a_c()
    raise RuntimeError('unreachable')
    i32_store(var0 + 8, ((var1 << var4) - 1))
    return var5

