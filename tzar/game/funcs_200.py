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
# $func471
# ==========================================================
def func471(var0, var1):
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
    var6 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var11 = ((var1 & 0xFFFFFFFF) >> 16)
    var14 = (((var1 & 0xFFFFFFFF) >> 16) + 3)
    var12 = (var11 + 2)
    var13 = (var11 + 1)
    var8 = (var1 & 65535)
    var15 = ((var1 & 65535) + 2)
    var7 = (i32_load(9671128) + (var0 * 132))
    var1 = i32_load(9142440)
    while True:  # loop $label6
        var0 = var8
        var8 = (var8 + 1)
        if (1 if var1 <= var11 else 0):
            break
        if (1 if var0 >= var1 else 0):
            break
        var1 = i32_load((i32_load(9142840) + ((var8 + (var13 * (var1 + 2))) << 2)))
        if (1 if i32_load((i32_load(9142840) + ((var8 + (var13 * (var1 + 2))) << 2))) < 3 else 0):
            break
        var1 = (i32_load(9671128) + (var1 * 132))
        var5 = i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122)
        var2 = ((i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122) * 404) + 9568096) + 264) != 4 else 0):
            break
        var9 = i32_load(9561692)
        var10 = i32_load16_u(var7 + 110)
        var4 = (i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704))
        var2 = (i32_load(var2 + 312) * i32_load(((i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704)) + 284188)))
        var2 = (1 if (1 if var2 < 100 else 0) else (((i32_load(var2 + 312) * i32_load(((i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704)) + 284188))) & 0xFFFFFFFF) // 100))
        var3 = i32_load16_u(var1 + 110)
        var4 = i32_load(var4 + 278556)
        if i32_load(var4 + 278556):
            var4 = (var4 + ((i32_load8_u(var7 + 122) + (var3 * 255)) << 2))
            i32_store((var4 + ((i32_load8_u(var7 + 122) + (var3 * 255)) << 2)), (i32_load(var4) + var2))
        var3 = i32_load(((var9 + (var3 * 286704)) + 278564))
        if i32_load(((var9 + (var3 * 286704)) + 278564)):
            var3 = (var3 + (((var10 * 255) + var5) << 2))
            i32_store((var3 + (((var10 * 255) + var5) << 2)), (i32_load(var3) + var2))
        if (1 if i32_load8_u(var1 + 125) == 3 else 0):
            break
        var3 = (var1 - -64)
        var5 = i32_load(var1 + 64)
        if (1 if var2 >= i32_load(var1 + 64) else 0):
            i32_store(var3, 0)
            break
        i32_store(var3, (var5 - var2))
        if (1 if i32_load(var1 + 92) == 0 else 0):
            break
        if i32_load8_u(9147141):
            break
        i32_store(var6 + 32, var2)
        a_b()
        var1 = i32_load(9142440)
        if (1 if var1 <= var13 else 0):
            break
        if (1 if var0 >= var1 else 0):
            break
        var1 = i32_load((i32_load(9142840) + ((var8 + (var12 * (var1 + 2))) << 2)))
        if (1 if i32_load((i32_load(9142840) + ((var8 + (var12 * (var1 + 2))) << 2))) < 3 else 0):
            break
        var1 = (i32_load(9671128) + (var1 * 132))
        var5 = i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122)
        var2 = ((i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122) * 404) + 9568096) + 264) != 4 else 0):
            break
        var9 = i32_load(9561692)
        var10 = i32_load16_u(var7 + 110)
        var4 = (i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704))
        var2 = (i32_load(var2 + 312) * i32_load(((i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704)) + 284188)))
        var2 = (1 if (1 if var2 < 100 else 0) else (((i32_load(var2 + 312) * i32_load(((i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704)) + 284188))) & 0xFFFFFFFF) // 100))
        var3 = i32_load16_u(var1 + 110)
        var4 = i32_load(var4 + 278556)
        if i32_load(var4 + 278556):
            var4 = (var4 + ((i32_load8_u(var7 + 122) + (var3 * 255)) << 2))
            i32_store((var4 + ((i32_load8_u(var7 + 122) + (var3 * 255)) << 2)), (i32_load(var4) + var2))
        var3 = i32_load(((var9 + (var3 * 286704)) + 278564))
        if i32_load(((var9 + (var3 * 286704)) + 278564)):
            var3 = (var3 + (((var10 * 255) + var5) << 2))
            i32_store((var3 + (((var10 * 255) + var5) << 2)), (i32_load(var3) + var2))
        if (1 if i32_load8_u(var1 + 125) == 3 else 0):
            break
        var3 = (var1 - -64)
        var5 = i32_load(var1 + 64)
        if (1 if var2 >= i32_load(var1 + 64) else 0):
            i32_store(var3, 0)
            break
        i32_store(var3, (var5 - var2))
        if (1 if i32_load(var1 + 92) == 0 else 0):
            break
        if i32_load8_u(9147141):
            break
        i32_store(var6 + 16, var2)
        a_b()
        var1 = i32_load(9142440)
        if (1 if var1 <= var12 else 0):
            break
        if (1 if var0 >= var1 else 0):
            break
        var1 = i32_load((i32_load(9142840) + ((var8 + (var14 * (var1 + 2))) << 2)))
        if (1 if i32_load((i32_load(9142840) + ((var8 + (var14 * (var1 + 2))) << 2))) < 3 else 0):
            break
        var1 = (i32_load(9671128) + (var1 * 132))
        var5 = i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122)
        var2 = ((i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122) * 404) + 9568096)
        if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122) * 404) + 9568096) + 264) != 4 else 0):
            break
        var9 = i32_load(9561692)
        var10 = i32_load16_u(var7 + 110)
        var4 = (i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704))
        var2 = (i32_load(var2 + 312) * i32_load(((i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704)) + 284188)))
        var2 = (1 if (1 if var2 < 100 else 0) else (((i32_load(var2 + 312) * i32_load(((i32_load(9561692) + (i32_load16_u(var7 + 110) * 286704)) + 284188))) & 0xFFFFFFFF) // 100))
        var3 = i32_load16_u(var1 + 110)
        var4 = i32_load(var4 + 278556)
        if i32_load(var4 + 278556):
            var4 = (var4 + ((i32_load8_u(var7 + 122) + (var3 * 255)) << 2))
            i32_store((var4 + ((i32_load8_u(var7 + 122) + (var3 * 255)) << 2)), (i32_load(var4) + var2))
        var3 = i32_load(((var9 + (var3 * 286704)) + 278564))
        if i32_load(((var9 + (var3 * 286704)) + 278564)):
            var3 = (var3 + (((var10 * 255) + var5) << 2))
            i32_store((var3 + (((var10 * 255) + var5) << 2)), (i32_load(var3) + var2))
        if (1 if i32_load8_u(var1 + 125) == 3 else 0):
            break
        var3 = (var1 - -64)
        var5 = i32_load(var1 + 64)
        if (1 if var2 >= i32_load(var1 + 64) else 0):
            i32_store(var3, 0)
            break
        i32_store(var3, (var5 - var2))
        if (1 if i32_load(var1 + 92) == 0 else 0):
            break
        if i32_load8_u(9147141):
            break
        i32_store(var6, var2)
        a_b()
        var1 = i32_load(9142440)
        if (1 if var0 != var15 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var6 + 48)


# ==========================================================
# $func508
# ==========================================================
def func508(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    if var2:
        while True:  # loop $label4
            var0 = (i32_load(9671128) + (i32_load((var1 + (var5 << 2))) * 132))
            var6 = i32_load8_u((i32_load(9671128) + (i32_load((var1 + (var5 << 2))) * 132)) + 122)
            var3 = ((i32_load8_u((i32_load(9671128) + (i32_load((var1 + (var5 << 2))) * 132)) + 122) * 404) + 9568096)
            var4 = i32_load8_u(9147152)
            if (0 if i32_load8_u(9147152) else i32_load8_u(((i32_load8_u((i32_load(9671128) + (i32_load((var1 + (var5 << 2))) * 132)) + 122) * 404) + 9568096) + 332)):
                break
            if var4:
                break
            if (1 if i32_load(var3 + 264) == 1 else 0):
                if (1 if i32_load(var0 + 84) < i32_load(var3 + 112) else 0):
                    break
            var4 = i32_load16_u(var0 + 110)
            var3 = i32_load(9561692)
            if (1 if i32_load(9147132) == 0 else 0):
                break
            if (1 if i32_load(9142440) != 4096 else 0):
                break
            if (1 if i32_load(9671152) != var6 else 0):
                break
            if (1 if i32_load((var3 + (var4 * 286704)) + 283976) > 1 else 0):
                break
            var3 = i32_load(((var3 + (var4 * 286704)) + 278568))
            if (1 if i32_load(((var3 + (var4 * 286704)) + 278568)) == 0 else 0):
                break
            # br_table ['$label1', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label1', '$label3']
            _br_idx = (i32_load8_u(var0 + 125) - 4)
            break  # br_table
            var4 = (var3 + (((var4 * 255) + var6) << 2))
            i32_store((var3 + (((var4 * 255) + var6) << 2)), (i32_load(var4) + 1))
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var2 else 0):
                continue
            break  # end loop


# ==========================================================
# $be
# Export: be
# ==========================================================
def be():
    """Export: be"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var0 = i32_load(9142440)
    if (1 if i32_load(9142440) <= 0 else 0):
        var1 = var0
        break
    var4 = i32_load(9671128)
    var5 = i32_load(9142840)
    var1 = var0
    while True:  # loop $label2
        var6 = (var6 + 1)
        var3 = 0
        while True:  # loop $label1
            var2 = (var1 + 2)
            var3 = (var3 + 1)
            var2 = (var4 + (i32_load((var5 + ((var6 + (((var1 + 2) + (var3 + 1)) * var2)) << 2))) * 132))
            if (1 if i32_load8_u((var4 + (i32_load((var5 + ((var6 + (((var1 + 2) + (var3 + 1)) * var2)) << 2))) * 132)) + 122) == 7 else 0):
                i32_store8(var2 + 122, 0)
                var4 = i32_load(9671128)
                var5 = i32_load(9142840)
                var1 = i32_load(9142440)
            if (1 if var0 != var3 else 0):
                continue
            break  # end loop
        if (1 if var0 != var6 else 0):
            continue
        break  # end loop
    if (1 if ((var1 * var1) * 80) > 65535 else 0):
        while True:  # loop $label3
            var3 = i32_load(9147312)
            var0 = i32_load(9147324)
            var0 = ((i32_load(9147324) << 11) ^ var0)
            var4 = (((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var0) & 0xFFFFFFFF) >> 8)) ^ var3) ^ var0)
            i32_store(9147324, (((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var0) & 0xFFFFFFFF) >> 8)) ^ var3) ^ var0))
            var0 = i32_load(9147320)
            var0 = ((i32_load(9147320) << 11) ^ var0)
            var5 = (((((((i32_load(9147320) << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var4 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var4)
            i32_store(9147320, (((((((i32_load(9147320) << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var4 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var4))
            var0 = i32_load(9147316)
            var0 = ((i32_load(9147316) << 11) ^ var0)
            var2 = (((((((i32_load(9147316) << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var5 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var5)
            i32_store(9147316, (((((((i32_load(9147316) << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var5 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var5))
            var0 = (var3 ^ (var3 << 11))
            var0 = ((((((var3 ^ (var3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var2)
            i32_store(9147312, ((((((var3 ^ (var3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var2))
            var7 = (var7 + 1)
            var1 = i32_load(9142440)
            if (1 if (var7 + 1) < ((((i32_load(9142440) * var1) * 80) & 0xFFFFFFFF) >> 16) else 0):
                continue
            break  # end loop


# ==========================================================
# $ae
# Export: ae
# ==========================================================
def ae():
    """Export: ae"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var1 = i32_load(9142440)
    if (1 if i32_load(9142440) > 0 else 0):
        var5 = i32_load(9671128)
        var6 = i32_load(9142840)
        var0 = var1
        while True:  # loop $label1
            var4 = (var4 + 1)
            var3 = 0
            while True:  # loop $label0
                var2 = (var0 + 2)
                var3 = (var3 + 1)
                var2 = (var5 + (i32_load((var6 + ((var4 + (((var0 + 2) + (var3 + 1)) * var2)) << 2))) * 132))
                if (1 if ((i32_load8_u((var5 + (i32_load((var6 + ((var4 + (((var0 + 2) + (var3 + 1)) * var2)) << 2))) * 132)) + 122) - 21) & 255) <= 1 else 0):
                    i32_store8(var2 + 122, 0)
                    var5 = i32_load(9671128)
                    var6 = i32_load(9142840)
                    var0 = i32_load(9142440)
                if (1 if var1 != var3 else 0):
                    continue
                break  # end loop
            if (1 if var1 != var4 else 0):
                continue
            break  # end loop
    var3 = 0
    var5 = 0
    var0 = i32_load(9142440)
    var0 = ((i32_load(9142440) << 3) * var0)
    if (1 if ((i32_load(9142440) << 3) * var0) >= 65536 else 0):
        var6 = ((var0 & 0xFFFFFFFF) >> 16)
        while True:  # loop $label2
            var0 = i32_load(9147324)
            var1 = i32_load(9147312)
            i32_store(9147324, i32_load(9147312))
            var2 = i32_load(9147320)
            var0 = (var0 ^ (var0 << 11))
            var4 = ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0)
            i32_store(9147320, ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0))
            var1 = i32_load(9147316)
            var0 = (var2 ^ (var2 << 11))
            var2 = ((((((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var4 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var4)
            i32_store(9147316, ((((((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var4 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var4))
            var0 = (var1 ^ (var1 << 11))
            var1 = ((((((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var2)
            i32_store(9147312, ((((((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var2))
            var0 = i32_load(9142440)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var6 else 0):
                continue
            break  # end loop
        while True:  # loop $label3
            var0 = i32_load(9147324)
            var1 = i32_load(9147312)
            i32_store(9147324, i32_load(9147312))
            var2 = i32_load(9147320)
            var0 = (var0 ^ (var0 << 11))
            var3 = ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0)
            i32_store(9147320, ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var0 ^ (var0 << 11)) & 0xFFFFFFFF) >> 8))) ^ var0))
            var1 = i32_load(9147316)
            var0 = (var2 ^ (var2 << 11))
            var2 = ((((((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var3 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var3)
            i32_store(9147316, ((((((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var3 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var3))
            var0 = (var1 ^ (var1 << 11))
            var1 = ((((((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var2)
            i32_store(9147312, ((((((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var2))
            var0 = i32_load(9142440)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var6 else 0):
                continue
            break  # end loop

