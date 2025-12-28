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
# $func1115
# ==========================================================
def func1115(var0):
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
    var13 = 0
    var14 = 0
    var15 = 0
    var16 = 0
    var1 = i32_load(var0 + 40)
    var4 = i32_load(i32_load(i32_load(var0 + 40)))
    var3 = (i32_load(i32_load(i32_load(var0 + 40))) - 1)
    if (1 if (i32_load(i32_load(i32_load(var0 + 40))) - 1) < 12 else 0):
        if (((2077 & 0xFFFFFFFF) >> var3) & 1):
            break
    var3 = (1 if (var4 - 7) < 4 else 0)
    i64_store(var1 + 40, 0)
    i64_store(var1 + 48, 0)
    if (1 if func447(i32_load(var1 + 20), var0, (11 if var3 else 12)) == 0 else 0):
        break
    if (1 if (var4 - 11) < -4 else 0):
        break
    if (1 if var3 == 0 else 0):
        break
    func448()
    if i32_load(var0 + 92):
        var3 = i32_load(var1)
        var7 = i32_load(i32_load(var1))
        var2 = (i32_load(i32_load(var1)) - 1)
        if (1 if var4 <= 10 else 0):
            if (1 if var2 >= 12 else 0):
                break
            var4 = 0
            if (1 if (((2077 & 0xFFFFFFFF) >> var2) & 1) == 0 else 0):
                break
            break
        if (1 if var2 >= 12 else 0):
            break
        var4 = 0
        if (1 if (((2077 & 0xFFFFFFFF) >> var2) & 1) == 0 else 0):
            break
        break
    if (1 if var4 <= 10 else 0):
        var2 = i32_load(52304)
        if (1 if i32_load(52304) != i32_load(52332) else 0):
            i32_store(9687992, 399)
            i32_store(9687988, 400)
            i32_store(9687984, 401)
            i32_store(9687980, 402)
            i32_store(9687976, 403)
            i32_store(9687972, 399)
            i32_store(9687968, 400)
            i32_store(9687964, 401)
            i32_store(9687960, 404)
            i32_store(9687956, 402)
            i32_store(9687952, 405)
            i32_store(52332, var2)
        i32_store(var1 + 44, 265)
        if (1 if i32_load(var0 + 56) == 0 else 0):
            break
        var2 = i32_load(var0 + 12)
        var7 = (i32_load(var0 + 12) + 1)
        var2 = func58(1, (((i32_load(var0 + 12) + 1) & -2) + var2))
        i32_store(var1 + 40, func58(1, (((i32_load(var0 + 12) + 1) & -2) + var2)))
        if (1 if var2 == 0 else 0):
            break
        i32_store(var1 + 4, var2)
        var0 = i32_load(var0 + 12)
        i32_store(var1 + 44, 266)
        var0 = (var0 + var2)
        i32_store(var1 + 8, (var0 + var2))
        i32_store(var1 + 12, (var0 + (var7 >> 1)))
        func448()
        break
    i32_store(var1 + 44, 267)
    var5 = 1
    if (1 if var3 == 0 else 0):
        break
    # br_table ['$label8', '$label9', '$label9', '$label9', '$label9', '$label8', '$label9']
    _br_idx = (var4 - 5)
    break  # br_table
    i32_store(var1 + 48, 268)
    break
    var0 = (1 if var4 > 10 else 0)
    i32_store(var1 + 48, (269 if (1 if var4 > 10 else 0) else 270))
    if var0:
        break
    break
    var4 = (1 if (var7 - 11) < -4 else 0)
    var7 = i32_load(var0 + 96)
    var10 = (i32_load(var0 + 96) << 1)
    var15 = i64_extend_u((i32_load(var0 + 96) << 1))
    var8 = (var7 + 1)
    var9 = ((var7 + 1) & -2)
    var11 = (((var7 + 1) & -2) << 1)
    var15 = (((((0 if var4 else i64_extend_u((i32_load(var0 + 96) << 1))) + var15) + i64_extend_u((((var7 + 1) & -2) << 1))) << 2) + (283 if var4 else 367))
    if (1 if (((((0 if var4 else i64_extend_u((i32_load(var0 + 96) << 1))) + var15) + i64_extend_u((((var7 + 1) & -2) << 1))) << 2) + (283 if var4 else 367)) > 4294967295 else 0):
        break
    var12 = i32_load(var0 + 16)
    var13 = i32_load(var0 + 12)
    var6 = i32_load(var0 + 100)
    var14 = i32(var15)
    var2 = func58(1, i32(var15))
    i32_store(var1 + 40, func58(1, i32(var15)))
    if (1 if var2 == 0 else 0):
        break
    var5 = ((((var2 + var14) + (-283 if var4 else -367)) + 31) & -32)
    i32_store(var1 + 24, ((((var2 + var14) + (-283 if var4 else -367)) + 31) & -32))
    i32_store(var1 + 32, (var5 + 168))
    i32_store(var1 + 28, (var5 + 84))
    i32_store(var1 + 36, (0 if var4 else (var5 + 252)))
    if (1 if func90(var5, i32_load(var0 + 12), i32_load(var0 + 16), i32_load(var3 + 16), var7, var6, i32_load(var3 + 32), 1, var2) == 0 else 0):
        return 0
    var13 = ((var13 + 1) >> 1)
    var12 = ((var12 + 1) >> 1)
    var8 = (var8 >> 1)
    var14 = ((var6 + 1) >> 1)
    var2 = (var2 + (var10 << 2))
    if (1 if func90(i32_load(var1 + 28), ((var13 + 1) >> 1), ((var12 + 1) >> 1), i32_load(var3 + 20), (var8 >> 1), ((var6 + 1) >> 1), i32_load(var3 + 36), 1, (var2 + (var10 << 2))) == 0 else 0):
        return 0
    var5 = 1
    if (1 if func90(i32_load(var1 + 32), var13, var12, i32_load(var3 + 24), var8, var14, i32_load(var3 + 40), 1, (var2 + (var9 << 2))) == 0 else 0):
        return 0
    i32_store(var1 + 44, 271)
    if var4:
        break
    var5 = 0
    if (1 if func90(i32_load(var1 + 36), i32_load(var0 + 12), i32_load(var0 + 16), i32_load(var3 + 28), var7, var6, i32_load(var3 + 44), 1, (var2 + (var11 << 2))) == 0 else 0):
        break
    i32_store(var1 + 48, 272)
    break
    var4 = (1 if (var7 - 11) < -4 else 0)
    var6 = (252 if var4 else 336)
    var15 = (3 if var4 else 4)
    var3 = i32_load(var0 + 96)
    var10 = (var3 << 1)
    var15 = (i64_extend_u((var3 << 1)) * var15)
    var16 = ((i64_extend_u(((252 if var4 else 336) + 31)) + ((3 if var4 else 4) * i64_extend_s(i32_load(var0 + 96)))) + ((i64_extend_u((var3 << 1)) * var15) << 2))
    if (1 if ((i64_extend_u(((252 if var4 else 336) + 31)) + ((3 if var4 else 4) * i64_extend_s(i32_load(var0 + 96)))) + ((i64_extend_u((var3 << 1)) * var15) << 2)) > 4294967295 else 0):
        break
    var8 = i32_load(var0 + 16)
    var9 = i32_load(var0 + 12)
    var7 = i32_load(var0 + 100)
    var11 = i32(var16)
    var2 = func58(1, i32(var16))
    i32_store(var1 + 40, func58(1, i32(var16)))
    if (1 if var2 == 0 else 0):
        break
    var6 = (((var2 + var11) - var6) & -32)
    i32_store(var1 + 24, (((var2 + var11) - var6) & -32))
    i32_store(var1 + 32, (var6 + 168))
    i32_store(var1 + 28, (var6 + 84))
    i32_store(var1 + 36, (0 if var4 else (var6 + 252)))
    var6 = (var2 + (i32(var15) << 2))
    if (1 if func90(var6, i32_load(var0 + 12), i32_load(var0 + 16), (var2 + (i32(var15) << 2)), var3, var7, 0, 1, var2) == 0 else 0):
        break
    var9 = ((var9 + 1) >> 1)
    var8 = ((var8 + 1) >> 1)
    if (1 if func90(i32_load(var1 + 28), ((var9 + 1) >> 1), ((var8 + 1) >> 1), (var3 + var6), var3, var7, 0, 1, (var2 + (var10 << 2))) == 0 else 0):
        break
    if (1 if func90(i32_load(var1 + 32), var9, var8, (var6 + var10), var3, var7, 0, 1, (var2 + (var3 << 4))) == 0 else 0):
        break
    i32_store(var1 + 44, 273)
    var5 = i32_load(52304)
    if (1 if i32_load(52304) != i32_load(52324) else 0):
        i32_store(9687900, 392)
        i32_store(9687892, 393)
        i32_store(9687928, 394)
        i32_store(9687924, 395)
        i32_store(9687920, 392)
        i32_store(9687916, 393)
        i32_store(9687912, 396)
        i32_store(9687908, 394)
        i32_store(9687904, 395)
        i32_store(9687896, 397)
        i32_store(9687888, 398)
        i32_store(52324, var5)
    var5 = 1
    if var4:
        break
    var5 = 0
    if (1 if func90(i32_load(var1 + 36), i32_load(var0 + 12), i32_load(var0 + 16), (var6 + (var3 * 3)), var3, var7, 0, 1, (var2 + (var3 * 24))) == 0 else 0):
        break
    i32_store(var1 + 48, 274)
    var0 = i32_load(i32_load(var1))
    i32_store(var1 + 52, (275 if (1 if var0 == 5 else 0) else (275 if (1 if i32_load(i32_load(var1)) == 10 else 0) else 276)))
    func188()
    var5 = 1
    return var5


# ==========================================================
# $func86
# ==========================================================
def func86(var0):
    var1 = 0
    var2 = 0
    var3 = 0.0
    var1 = i32_load8_u(var0 + 122)
    if (1 if i32_load16_u(var0 + 108) == 0 else 0):
        break
    # br_table ['$label1', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label1', '$label2']
    _br_idx = (var1 + -64)
    break  # br_table
    if (1 if var1 == 10 else 0):
        break
    var2 = ((var1 * 72) + 9263856)
    break
    var2 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        break
    if (1 if i32_load(var2 + 8) < 3 else 0):
        break
    if i32_load(i32_load(var2)):
        break
    var2 = ((var1 * 72) + 9263856)
    if (1 if i32_load(((var1 * 72) + 9263856) + 68) == 0 else 0):
        break
    break
    var2 = i32_load(var0 + 88)
    # br_table ['$label6', '$label7', '$label8', '$label9']
    _br_idx = (i32_load(var0 + 88) & 65535)
    break  # br_table
    break
    var2 = ((var2 & 0xFFFFFFFF) >> 16)
    if (1 if ((var2 & 0xFFFFFFFF) >> 16) == i32_load(38984) else 0):
        break
    if (1 if i32_load(38528) == var2 else 0):
        break
    break
    break
    var2 = ((var1 * 72) + 9263908)
    var3 = -1.0
    if (1 if i32_load(38472) == var1 else 0):
        break
    if (1 if i32_load(38600) == var1 else 0):
        break
    return func37(var0, i32_load(var2), var3, 0)


# ==========================================================
# $func140
# ==========================================================
def func140(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    i32_store8(var0 + 125, 7)
    func92(var0, 0.0, 0.0)
    if i32_load8_u(9142916):
    var1 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 216):
        var5 = i32_load(9142840)
        var6 = i32_load16_u(var0 + 114)
        var7 = i32_load16_u(var0 + 112)
        while True:  # loop $label1
            var2 = (var2 + 1)
            var8 = ((var2 + 1) + var7)
            var3 = 0
            while True:  # loop $label0
                var3 = (var3 + 1)
                var4 = (i32_load(9142440) + 2)
                i32_store((var5 + ((var8 + ((((var3 + 1) + var6) + ((i32_load(9142440) + 2) * i32_load(var1 + 208))) * var4)) << 2)), i32_load(var0 + 28))
                var4 = i32_load(var1 + 216)
                if (1 if var3 < i32_load(var1 + 216) else 0):
                    continue
                break  # end loop
            if (1 if var2 < var4 else 0):
                continue
            break  # end loop
    var1 = i32_load(var1 + 260)
    if i32_load(var1 + 260):
        i32_store((i32_load(9215884) + (i32_load(var0 + 44) << 4)), (i32_load(9142848) + (((32000 // var1) & 0xFFFFFFFF) // 25)))

