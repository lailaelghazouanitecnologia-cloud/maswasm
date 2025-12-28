"""
Auto-generated from WAT. Contains 6 functions.
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
# $func262
# ==========================================================
def func262(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if (1 if ((1 if (i64_reinterpret_f64(var0) & 9223372036854775807) < 9218868437227405313 else 0) & (1 if (i64_reinterpret_f64(var1) & 9223372036854775807) <= 9218868437227405312 else 0)) == 0 else 0):
        return (var0 + var1)
    var7 = i64_reinterpret_f64(var1)
    var2 = i32(((i64_reinterpret_f64(var1) & 0xFFFFFFFFFFFFFFFF) >> 32))
    var5 = i32(var7)
    if (1 if ((i32(((i64_reinterpret_f64(var1) & 0xFFFFFFFFFFFFFFFF) >> 32)) - 1072693248) | i32(var7)) == 0 else 0):
        return func424(var0)
    var6 = (((var2 & 0xFFFFFFFF) >> 30) & 2)
    var7 = i64_reinterpret_f64(var0)
    var3 = ((((var2 & 0xFFFFFFFF) >> 30) & 2) | i32(((i64_reinterpret_f64(var0) & 0xFFFFFFFFFFFFFFFF) >> 63)))
    var4 = (i32(((var7 & 0xFFFFFFFFFFFFFFFF) >> 32)) & 2147483647)
    if (1 if ((i32(((var7 & 0xFFFFFFFFFFFFFFFF) >> 32)) & 2147483647) | i32(var7)) == 0 else 0):
        # br_table ['$label0', '$label1', '$label2']
        _br_idx = (var3 - 2)
        break  # br_table
        return 3.141592653589793
        return -3.141592653589793
    var2 = (var2 & 2147483647)
    if (1 if ((var2 & 2147483647) | var5) == 0 else 0):
        # Unknown: f64.copysign []
        return var0
    if (1 if var2 == 2146435072 else 0):
        if (1 if var4 != 2146435072 else 0):
            break
        return f64_load(((var3 << 3) + 28800))
    if (1 if ((1 if var4 != 2146435072 else 0) & (1 if (var2 + 67108864) >= var4 else 0)) == 0 else 0):
        # Unknown: f64.copysign []
        return var0
    if var6:
        if (1 if (var4 + 67108864) < var2 else 0):
            break
    var0 = func424(abs((var0 / var1)))
    # br_table ['$label2', '$label5', '$label6', '$label7']
    _br_idx = var3
    break  # br_table
    return (-var0)
    return (3.141592653589793 - (var0 + -1.2246467991473532e-16))
    return ((var0 + -1.2246467991473532e-16) + -3.141592653589793)
    var0 = f64_load(((var3 << 3) + 28832))
    return var0


# ==========================================================
# $func266
# ==========================================================
def func266(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    if (1 if i32_load(var0 + 12) == i32_load(global3 + 24) else 0):
        i32_store(var0 + 12, 0)
    while True:  # loop $label0
        var3 = i32_load(var0 + 4)
        var1 = i32_load(var0)
        var2 = (var1 & 2147483647)
        var4 = (((var1 - 1) if (1 if (var1 & 2147483647) != 1 else 0) else 0) if (1 if var2 != 2147483647 else 0) else 0)
        if (1 if (((var1 - 1) if (1 if (var1 & 2147483647) != 1 else 0) else 0) if (1 if var2 != 2147483647 else 0) else 0) != var1 else 0):
            continue
        break  # end loop
    if var4:
        break
    if ((1 if var3 == 0 else 0) & (1 if var1 >= 0 else 0)):
        break
    func111(var0, var2)


# ==========================================================
# $func268
# ==========================================================
def func268(var0, var1, var2, var3, var4, var5):
    var6 = 0
    var7 = 0
    var8 = 0
    if (1 if var0 == 0 else 0):
        break
    if (1 if var2 == 0 else 0):
        break
    var6 = (var1 >> 31)
    if (1 if ((var1 ^ (var1 >> 31)) - var6) < var4 else 0):
        break
    var6 = (var3 >> 31)
    if (1 if ((var3 ^ (var3 >> 31)) - var6) < var4 else 0):
        break
    if (1 if var5 <= 0 else 0):
        break
    var8 = (var5 & 3)
    if (1 if (var5 & 3) == 0 else 0):
        var6 = var5
        break
    var6 = var5
    while True:  # loop $label4
        # Unknown: memory.copy []
        var2 = (var2 + var3)
        var0 = (var0 + var1)
        var6 = (var6 - 1)
        var7 = (var7 + 1)
        if (1 if (var7 + 1) != var8 else 0):
            continue
        break  # end loop
    if (1 if var5 < 4 else 0):
        break
    while True:  # loop $label5
        # Unknown: memory.copy []
        var2 = (var2 + var3)
        var0 = (var0 + var1)
        # Unknown: memory.copy []
        var2 = (var2 + var3)
        var0 = (var0 + var1)
        # Unknown: memory.copy []
        var2 = (var2 + var3)
        var0 = (var0 + var1)
        # Unknown: memory.copy []
        var2 = (var2 + var3)
        var0 = (var0 + var1)
        var5 = (var6 - 5)
        var6 = (var6 - 4)
        if (1 if var5 < -2 else 0):
            continue
        break  # end loop
    return
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func269
# ==========================================================
def func269(var0, var1, var2):
    var3 = 0
    if var0:
        if (1 if var1 == 0 else 0):
            break
        if (1 if var2 >= -8 else 0):
            break
        i64_store(var0 + 20, 0)
        i32_store(var0 + 12, var2)
        i32_store(var0 + 8, var1)
        var2 = (8 if (1 if var2 >= 8 else 0) else var2)
        if (1 if (8 if (1 if var2 >= 8 else 0) else var2) == 0 else 0):
            break
        var3 = i64_load8_u(var1)
        if (1 if var2 == 1 else 0):
            break
        var3 = ((i64_load8_u(var1 + 1) << 8) | var3)
        if (1 if var2 == 2 else 0):
            break
        var3 = ((i64_load8_u(var1 + 2) << 16) | var3)
        if (1 if var2 == 3 else 0):
            break
        var3 = ((i64_load8_u(var1 + 3) << 24) | var3)
        if (1 if var2 == 4 else 0):
            break
        var3 = ((i64_load8_u(var1 + 4) << 32) | var3)
        if (1 if var2 == 5 else 0):
            break
        var3 = ((i64_load8_u(var1 + 5) << 40) | var3)
        if (1 if var2 == 6 else 0):
            break
        var3 = ((i64_load8_u(var1 + 6) << 48) | var3)
        if (1 if var2 == 7 else 0):
            break
        var3 = ((i64_load8_u(var1 + 7) << 56) | var3)
        i32_store(var0 + 16, var2)
        i64_store(var0, var3)
        return
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    return 3628


# ==========================================================
# $func270
# ==========================================================
def func270(var0, var1, var2):
    var3 = 0
    var4 = 0
    if var0:
        if (1 if var1 == 0 else 0):
            break
        if (1 if var2 < 0 else 0):
            break
        i32_store(var0 + 28, 0)
        i64_store(var0, 0)
        i64_store(var0 + 8, -34359738114)
        i32_store(var0 + 16, var1)
        var4 = (var1 + var2)
        i32_store(var0 + 20, (var1 + var2))
        var4 = ((var4 - 7) if (1 if var2 > 7 else 0) else var1)
        i32_store(var0 + 24, ((var4 - 7) if (1 if var2 > 7 else 0) else var1))
        if (1 if var1 < var4 else 0):
            var3 = i64_load(var1)
            i32_store(var0 + 12, 48)
            i32_store(var0 + 16, (var1 + 7))
            i64_store(var0, ((((((var3 << 56) | ((var3 & 65280) << 40)) | (((var3 & 16711680) << 24) | ((var3 & 4278190080) << 8))) | ((((var3 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((var3 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((var3 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
            return
        i32_store(var0 + 12, 0)
        if var2:
            i32_store(var0 + 16, (var1 + 1))
            i64_store(var0, i64_load8_u(var1))
            return
        i32_store(var0 + 28, 1)
        return
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $func274
# ==========================================================
def func274(var0, var1):
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
    var16 = 0
    var17 = 0
    var18 = 0
    var3 = i32_load(var0 + 8)
    if (1 if var1 <= i32_load(i32_load(var0 + 8) + 88) else 0):
        var5 = i32_load(var0 + 108)
        var8 = i32_load(var3 + 40)
        var7 = i32_load(((var3 + 84) if (1 if i32_load(i32_load(var3 + 40) + 12) < 2 else 0) else (var0 + 108)))
        var7 = (i32_load(var0 + 108) if (1 if var5 > var7 else 0) else i32_load(((var3 + 84) if (1 if i32_load(i32_load(var3 + 40) + 12) < 2 else 0) else (var0 + 108))))
        if (1 if (i32_load(var0 + 108) if (1 if var5 > var7 else 0) else i32_load(((var3 + 84) if (1 if i32_load(i32_load(var3 + 40) + 12) < 2 else 0) else (var0 + 108)))) >= var1 else 0):
            break
        if (1 if i32_load(var0 + 192) != 1 else 0):
            break
        var2 = (var0 + 196)
        if (1 if i32_load((var0 + 196)) != 3 else 0):
            break
        var5 = var7
        var4 = (i32_load(var0 + 16) + (var7 * i32_load(var0 + 100)))
        var9 = i32_load(var3)
        var3 = (i32_load(var8 + 136) + (i32_load(var3) * var5))
        var6 = (i32_load(var8 + 136) + (i32_load(var3) * var5))
        var12 = i32_load(var2 + 16)
        var10 = i32_load(var2 + 8)
        var2 = i32_load(var2 + 4)
        if i32_load(var2 + 4):
            if (1 if var1 <= var5 else 0):
                break
            if (1 if var10 <= 0 else 0):
                break
            var15 = ((8 & 0xFFFFFFFF) >> var2)
            var13 = ((-1 << ((8 & 0xFFFFFFFF) >> var2)) ^ -1)
            var14 = ((-1 << var2) ^ -1)
            var17 = (var10 & -2)
            var18 = (var10 & 1)
            while True:  # loop $label6
                var11 = 0
                var2 = 0
                var16 = 0
                if (1 if var10 != 1 else 0):
                    while True:  # loop $label5
                        if (1 if (var11 & var14) == 0 else 0):
                            var2 = i32_load8_u(var4)
                            var4 = (var4 + 1)
                        i32_store8(var6, ((i32_load((var12 + ((var2 & var13) << 2))) & 0xFFFFFFFF) >> 8))
                        if ((var11 | 1) & var14):
                            var2 = ((var2 & 0xFFFFFFFF) >> var15)
                            break
                        var2 = i32_load8_u(var4)
                        var4 = (var4 + 1)
                        i32_store8(var6 + 1, ((i32_load((var12 + ((var2 & var13) << 2))) & 0xFFFFFFFF) >> 8))
                        var11 = (var11 + 2)
                        var2 = ((var2 & 0xFFFFFFFF) >> var15)
                        var6 = (var6 + 2)
                        var16 = (var16 + 2)
                        if (1 if (var16 + 2) != var17 else 0):
                            continue
                        break  # end loop
                if var18:
                    if (1 if (var11 & var14) == 0 else 0):
                        var2 = i32_load8_u(var4)
                        var4 = (var4 + 1)
                    i32_store8(var6, ((i32_load((var12 + ((var2 & var13) << 2))) & 0xFFFFFFFF) >> 8))
                    var6 = (var6 + 1)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var1 else 0):
                    continue
                break  # end loop
            break
        # call_indirect via table[i32_load(9687568)]
        var5 = i32_load(var8 + 12)
        if (1 if i32_load(var8 + 12) == 0 else 0):
            break
        if (1 if i32_load(((var5 << 2) + 9687552)) == 0 else 0):
            break
        var5 = i32_load(var8 + 140)
        var4 = (var1 - var7)
        if ((var1 - var7) & 1):
            # call_indirect via table[i32_load(((i32_load(var8 + 12) << 2) + 9687552))]
            var7 = (var7 + 1)
            var5 = var3
        else:
        var2 = var3
        if (1 if var4 != 1 else 0):
            var3 = var5
            while True:  # loop $label8
                # call_indirect via table[i32_load(((i32_load(var8 + 12) << 2) + 9687552))]
                var3 = (var2 + var9)
                # call_indirect via table[i32_load(((i32_load(var8 + 12) << 2) + 9687552))]
                var2 = (var3 + var9)
                var7 = (var7 + 2)
                if (1 if (var7 + 2) != var1 else 0):
                    continue
                break  # end loop
        i32_store(var8 + 140, var3)
        i32_store(var0 + 108, var1)
        i32_store(var0 + 116, var1)
        return call_indirect(i32_load(((i32_load(var8 + 12) << 2) + 9687552)))
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    return 3488

