"""
Auto-generated from WAT. Contains 3 functions.
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
# $func1073
# ==========================================================
def func1073(var0, var1, var2, var3, var4, var5):
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    var13 = 0
    var14 = 0
    if (1 if var4 <= 15 else 0):
        var13 = (i32_load((var1 + (var4 << 2))) + (var2 * 11))
        var9 = i32_load(var0 + 12)
        var8 = i32_load(var0 + 8)
        while True:  # loop $label9
            var11 = i32_load8_u(var13)
            if (1 if var9 >= 0 else 0):
                break
            var2 = i32_load(var0 + 16)
            if (1 if i32_load(var0 + 16) == 0 else 0):
                break
            if (1 if i32_load(var0 + 24) > var2 else 0):
                var6 = i64_load(var2)
                i32_store(var0 + 16, (var2 + 7))
                var9 = (var9 + 56)
                i32_store(var0 + 12, (var9 + 56))
                i64_store(var0, ((i64_load(var0) << 56) | ((((((var6 << 56) | ((var6 & 65280) << 40)) | (((var6 & 16711680) << 24) | ((var6 & 4278190080) << 8))) | ((((var6 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var6 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var6 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                break
            func36(var0)
            var9 = i32_load(var0 + 12)
            var2 = (((var8 * var11) & 0xFFFFFFFF) >> 8)
            var6 = i64_load(var0)
            var7 = i64_extend_u(var9)
            var12 = (1 if (((var8 * var11) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var9))) else 0)
            if (1 if (1 if (((var8 * var11) & 0xFFFFFFFF) >> 8) >= i32(((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var9))) else 0) == 0 else 0):
                var2 = (var2 + 1)
                var6 = (var6 - (i64_extend_u((var2 + 1)) << var7))
                i64_store(var0, (var6 - (i64_extend_u((var2 + 1)) << var7)))
                var2 = (var8 - var2)
            if (1 if var2 <= 126 else 0):
                var9 = (var9 - i32_load8_u((var2 + 17632)))
                i32_store(var0 + 12, (var9 - i32_load8_u((var2 + 17632))))
                var2 = i32_load8_u((var2 + 17760))
            i32_store(var0 + 8, var2)
            var11 = var4
            var8 = var4
            if var12:
                break
            while True:  # loop $label5
                var8 = i32_load8_u(var13 + 1)
                if (1 if var9 >= 0 else 0):
                    break
                var4 = i32_load(var0 + 16)
                if (1 if i32_load(var0 + 16) == 0 else 0):
                    break
                if (1 if i32_load(var0 + 24) > var4 else 0):
                    var7 = i64_load(var4)
                    var9 = (var9 + 56)
                    i32_store(var0 + 12, (var9 + 56))
                    i32_store(var0 + 16, (var4 + 7))
                    var6 = ((var6 << 56) | ((((((var7 << 56) | ((var7 & 65280) << 40)) | (((var7 & 16711680) << 24) | ((var7 & 4278190080) << 8))) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var7 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                    i64_store(var0, ((var6 << 56) | ((((((var7 << 56) | ((var7 & 65280) << 40)) | (((var7 & 16711680) << 24) | ((var7 & 4278190080) << 8))) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var7 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                    break
                func36(var0)
                var6 = i64_load(var0)
                var9 = i32_load(var0 + 12)
                var8 = (((var2 * var8) & 0xFFFFFFFF) >> 8)
                var7 = i64_extend_u(var9)
                var10 = i32(((var6 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var9)))
                if (1 if (((var2 * var8) & 0xFFFFFFFF) >> 8) >= i32(((var6 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var9))) else 0):
                    break
                var4 = (var8 + 1)
                var6 = (var6 - (i64_extend_u((var8 + 1)) << var7))
                i64_store(var0, (var6 - (i64_extend_u((var8 + 1)) << var7)))
                var2 = (var2 - var4)
                if (1 if (var2 - var4) <= 126 else 0):
                    var9 = (var9 - i32_load8_u((var2 + 17632)))
                    i32_store(var0 + 12, (var9 - i32_load8_u((var2 + 17632))))
                    var2 = i32_load8_u((var2 + 17760))
                i32_store(var0 + 8, var2)
                var4 = (var11 + 1)
                var12 = i32_load((var1 + ((var11 + 1) << 2)))
                if (1 if var8 >= var10 else 0):
                    var8 = 16
                    var13 = var12
                    var11 = var4
                    if (1 if var4 != 16 else 0):
                        continue
                    break
                break  # end loop
            var10 = i32_load8_u(var13 + 2)
            if (1 if var9 >= 0 else 0):
                break
            var8 = i32_load(var0 + 16)
            if (1 if i32_load(var0 + 16) == 0 else 0):
                break
            if (1 if i32_load(var0 + 24) > var8 else 0):
                var7 = i64_load(var8)
                var9 = (var9 + 56)
                i32_store(var0 + 12, (var9 + 56))
                i32_store(var0 + 16, (var8 + 7))
                var6 = ((var6 << 56) | ((((((var7 << 56) | ((var7 & 65280) << 40)) | (((var7 & 16711680) << 24) | ((var7 & 4278190080) << 8))) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var7 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                i64_store(var0, ((var6 << 56) | ((((((var7 << 56) | ((var7 & 65280) << 40)) | (((var7 & 16711680) << 24) | ((var7 & 4278190080) << 8))) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var7 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var7 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                break
            func36(var0)
            var6 = i64_load(var0)
            var9 = i32_load(var0 + 12)
            var10 = (((var2 * var10) & 0xFFFFFFFF) >> 8)
            var8 = (((var2 * var10) & 0xFFFFFFFF) >> 8)
            var7 = i64_extend_u(var9)
            var14 = i32(((var6 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var9)))
            if (1 if i32(((var6 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var9))) > var10 else 0):
                var8 = (var10 + 1)
                i64_store(var0, (var6 - (i64_extend_u((var10 + 1)) << var7)))
                var8 = (var2 - var8)
            if (1 if var8 <= 126 else 0):
                var9 = (var9 - i32_load8_u((var8 + 17632)))
                i32_store(var0 + 12, (var9 - i32_load8_u((var8 + 17632))))
            else:
            i32_store(i32_load8_u((var8 + 17760)) + 8, var8)
            if (1 if var10 >= var14 else 0):
                var10 = 1
                break
            var10 = func463(var0, var13)
            var9 = i32_load(var0 + 12)
            var13 = (var12 + 22)
            if (1 if var9 >= 0 else 0):
                break
            var2 = i32_load(var0 + 16)
            if (1 if i32_load(var0 + 16) == 0 else 0):
                break
            if (1 if i32_load(var0 + 24) > var2 else 0):
                var6 = i64_load(var2)
                i32_store(var0 + 16, (var2 + 7))
                i64_store(var0, ((i64_load(var0) << 56) | ((((((var6 << 56) | ((var6 & 65280) << 40)) | (((var6 & 16711680) << 24) | ((var6 & 4278190080) << 8))) | ((((var6 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var6 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var6 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                break
            func36(var0)
            var2 = i32_load(var0 + 12)
            var9 = (i32_load(var0 + 12) - 1)
            i32_store((var9 + 56) + 12, (i32_load(var0 + 12) - 1))
            var8 = i32_load(var0 + 8)
            var12 = ((i32_load(var0 + 8) & 0xFFFFFFFF) >> 1)
            var6 = i64_load(var0)
            var7 = i64_extend_u(var2)
            var2 = ((((i32_load(var0 + 8) & 0xFFFFFFFF) >> 1) - i32(((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2)))) >> 31)
            var8 = ((((((i32_load(var0 + 8) & 0xFFFFFFFF) >> 1) - i32(((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2)))) >> 31) + var8) | 1)
            i32_store(var0 + 8, ((((((i32_load(var0 + 8) & 0xFFFFFFFF) >> 1) - i32(((i64_load(var0) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(var2)))) >> 31) + var8) | 1))
            i64_store(var0, (var6 - (i64_extend_u((var2 & (var12 + 1))) << var7)))
            i32_store16((var5 + (i32_load8_u((var11 + 13968)) << 1)), (i32_load((var3 + ((1 if var11 > 0 else 0) << 2))) * ((var2 ^ var10) - var2)))
            if (1 if var11 < 15 else 0):
                continue
            break  # end loop
    var8 = 16
    return var8
    a_c()
    raise RuntimeError('unreachable')
    return 3339


# ==========================================================
# $func1082
# ==========================================================
def func1082(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var5 = i32_load(var1 + 24)
    var4 = i32_load(var0 + 16)
    var2 = i32_load(i32_load(var1))
    if ((1 if ((1 if i32_load(i32_load(var1)) <= 12 else 0) if ((1 << var2) & 4154) else 0) == 0 else 0) & (1 if (var2 - 11) < -4 else 0)):
        break
    var2 = i32_load(var0 + 104)
    if (1 if i32_load(var0 + 104) == 0 else 0):
        break
    func445(i32_load(var0 + 20), i32_load(var0 + 32), var2, i32_load(var0), i32_load(var0 + 12), var4, 0)
    if (1 if var4 <= 0 else 0):
        return 0
    var7 = ((var4 + 1) >> 1)
    var6 = i32_load(var0 + 32)
    var3 = i32_load(var0 + 20)
    var2 = var4
    while True:  # loop $label1
        var9 = func82(var5, var2, var3, var6)
        var3 = (var3 + (func82(var5, var2, var3, var6) * var6))
        var8 = (func187(var5) + var8)
        var2 = (var2 - var9)
        if (1 if (var2 - var9) > 0 else 0):
            continue
        break  # end loop
    if (1 if var4 > 0 else 0):
        var4 = i32_load(var1 + 28)
        var5 = i32_load(var0 + 36)
        var3 = i32_load(var0 + 24)
        var2 = var7
        while True:  # loop $label2
            var6 = func82(var4, var2, var3, var5)
            var3 = (var3 + (var5 * var6))
            var2 = (var2 - var6)
            if (1 if (var2 - var6) > 0 else 0):
                continue
            break  # end loop
        var3 = i32_load(var0 + 28)
        var1 = i32_load(var1 + 32)
        var0 = i32_load(var0 + 36)
        while True:  # loop $label3
            var2 = func82(var1, var7, var3, var0)
            var3 = (var3 + (var0 * var2))
            var7 = (var7 - var2)
            if (1 if (var7 - var2) > 0 else 0):
                continue
            break  # end loop
    return var8


# ==========================================================
# $func1084
# ==========================================================
def func1084(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var5 = i32_load(var1)
    var7 = i32_load(i32_load(var1) + 28)
    var4 = i32_load(var5 + 44)
    var6 = i32_load(var1 + 16)
    var3 = (i32_load(i32_load(var1) + 28) + (i32_load(var5 + 44) * i32_load(var1 + 16)))
    var8 = i32_load(var0 + 104)
    if i32_load(var0 + 104):
        var4 = i32_load(var0 + 16)
        if (1 if i32_load(var0 + 16) > 0 else 0):
            var9 = (i32_load(var5 + 16) + (i32_load(var5 + 32) * var6))
            var6 = i32_load(var1 + 36)
            var7 = i32_load(var0)
            var0 = 0
            while True:  # loop $label0
                var10 = func82(var6, var4, var8, var7)
                var8 = (var8 + (func82(var6, var4, var8, var7) * var7))
                var0 = (func187(var6) + var0)
                var4 = (var4 - var10)
                if (1 if (var4 - var10) > 0 else 0):
                    continue
                break  # end loop
            if (1 if var0 != var2 else 0):
                break
            if (1 if var2 <= 0 else 0):
                break
            func445(var9, i32_load(var5 + 32), var3, i32_load(var5 + 44), i32_load(i32_load(var1 + 36) + 52), var2, 1)
            return 0
        if (1 if var2 == 0 else 0):
            break
        a_c()
        raise RuntimeError('unreachable')
    if (1 if var7 == 0 else 0):
        break
    if (1 if i32_load(var0 + 100) < (var2 + var6) else 0):
        break
    if (1 if var2 <= 0 else 0):
        break
    var1 = i32_load(var0 + 96)
    if (1 if var2 >= 8 else 0):
        var5 = (var2 & -8)
        var0 = 0
        while True:  # loop $label4
            # Unknown: memory.fill []
            var3 = (var3 + var4)
            # Unknown: memory.fill []
            var3 = (var3 + var4)
            # Unknown: memory.fill []
            var3 = (var3 + var4)
            # Unknown: memory.fill []
            var3 = (var3 + var4)
            # Unknown: memory.fill []
            var3 = (var3 + var4)
            # Unknown: memory.fill []
            var3 = (var3 + var4)
            # Unknown: memory.fill []
            var3 = (var3 + var4)
            # Unknown: memory.fill []
            var3 = (var3 + var4)
            var0 = (var0 + 8)
            if (1 if (var0 + 8) != var5 else 0):
                continue
            break  # end loop
    var2 = (var2 & 7)
    if (1 if (var2 & 7) == 0 else 0):
        break
    var0 = 0
    while True:  # loop $label5
        # Unknown: memory.fill []
        var3 = (var3 + var4)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var2 else 0):
            continue
        break  # end loop
    return 0
    a_c()
    raise RuntimeError('unreachable')
    return 5759

