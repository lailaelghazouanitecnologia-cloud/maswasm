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
# $func321
# ==========================================================
def func321(var0, var1, var2):
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
    if (1 if var2 >= 0 else 0):
        var11 = i32_load16_u(var1 + 2)
        var8 = (4 if i32_load16_u(var1 + 2) else 3)
        var5 = (7 if var11 else 138)
        var9 = (var0 + 5817)
        var6 = -1
        while True:  # loop $label12
            var10 = var11
            var14 = var13
            var13 = (var13 + 1)
            var11 = i32_load16_u((var1 + ((var13 + 1) << 2)) + 2)
            var3 = (var4 + 1)
            if (1 if (var4 + 1) >= var5 else 0):
                break
            if (1 if var10 != var11 else 0):
                break
            var4 = var3
            break
            if (1 if var3 < var8 else 0):
                var4 = (var0 + (var10 << 2))
                var5 = ((var0 + (var10 << 2)) + 2686)
                var7 = (var4 + 2684)
                var4 = i32_load(var0 + 5820)
                while True:  # loop $label3
                    var12 = i32_load16_u(var5)
                    var8 = i32_load16_u(var7)
                    var6 = (i32_load16_u(var0 + 5816) | (i32_load16_u(var7) << var4))
                    i32_store16(var0 + 5816, (i32_load16_u(var0 + 5816) | (i32_load16_u(var7) << var4)))
                    if (1 if (16 - var12) < var4 else 0):
                        var4 = i32_load(var0 + 20)
                        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                        i32_store8((var4 + i32_load(var0 + 8)), var6)
                        var4 = i32_load(var0 + 20)
                        i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                        i32_store8((var4 + i32_load(var0 + 8)), i32_load8_u(var9))
                        var4 = i32_load(var0 + 5820)
                        i32_store16(var0 + 5816, ((var8 & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
                        break
                    var4 = (var4 + var12)
                    i32_store(((var4 + var12) - 16) + 5820, (var4 + var12))
                    var3 = (var3 - 1)
                    if (var3 - 1):
                        continue
                    break  # end loop
                break
            if var10:
                if (1 if var6 == var10 else 0):
                    var5 = i32_load(var0 + 5820)
                    var4 = var3
                    break
                var3 = (var0 + (var10 << 2))
                var7 = i32_load16_u(((var0 + (var10 << 2)) + 2686))
                var8 = i32_load16_u((var3 + 2684))
                var3 = i32_load(var0 + 5820)
                var6 = (i32_load16_u(var0 + 5816) | (i32_load16_u((var3 + 2684)) << i32_load(var0 + 5820)))
                i32_store16(var0 + 5816, (i32_load16_u(var0 + 5816) | (i32_load16_u((var3 + 2684)) << i32_load(var0 + 5820))))
                if (1 if (16 - var7) < var3 else 0):
                    var3 = i32_load(var0 + 20)
                    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                    i32_store8((var3 + i32_load(var0 + 8)), var6)
                    var3 = i32_load(var0 + 20)
                    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                    i32_store8((var3 + i32_load(var0 + 8)), i32_load8_u(var9))
                    var3 = i32_load(var0 + 5820)
                    i32_store16(var0 + 5816, ((var8 & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
                    break
                var5 = (var3 + var7)
                i32_store(((var3 + var7) - 16) + 5820, (var3 + var7))
                var8 = i32_load16_u(var0 + 2748)
                var3 = (i32_load16_u(var0 + 5816) | (i32_load16_u(var0 + 2748) << var5))
                var7 = i32_load16_u(var0 + 2750)
                if (1 if (16 - i32_load16_u(var0 + 2750)) < var5 else 0):
                    i32_store16(var0 + 5816, var3)
                    var6 = i32_load(var0 + 20)
                    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                    i32_store8((var6 + i32_load(var0 + 8)), var3)
                    var3 = i32_load(var0 + 20)
                    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                    i32_store8((var3 + i32_load(var0 + 8)), i32_load8_u(var9))
                    var3 = i32_load(var0 + 5820)
                    var5 = ((var7 + i32_load(var0 + 5820)) - 16)
                    var3 = ((var8 & 0xFFFFFFFF) >> (16 - var3))
                    break
                var5 = (var5 + var7)
                i32_store(var0 + 5820, var5)
                var6 = (var4 + 65533)
                if (1 if var5 >= 15 else 0):
                    var3 = (var3 | (var6 << var5))
                    i32_store16(var0 + 5816, (var3 | (var6 << var5)))
                    var4 = i32_load(var0 + 20)
                    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                    i32_store8((var4 + i32_load(var0 + 8)), var3)
                    var4 = i32_load(var0 + 20)
                    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                    i32_store8((var4 + i32_load(var0 + 8)), i32_load8_u(var9))
                    var4 = i32_load(var0 + 5820)
                    i32_store16(var0 + 5816, (((var6 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
                    break
                i32_store16(var0 + 5816, (var3 | (var6 << var5)))
                break
            var3 = i32_load16_u(var0 + 5816)
            var6 = i32_load(var0 + 5820)
            if (1 if var4 <= 9 else 0):
                var8 = i32_load16_u(var0 + 2752)
                var3 = (var3 | (i32_load16_u(var0 + 2752) << var6))
                var7 = i32_load16_u(var0 + 2754)
                if (1 if (16 - i32_load16_u(var0 + 2754)) < var6 else 0):
                    i32_store16(var0 + 5816, var3)
                    var6 = i32_load(var0 + 20)
                    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                    i32_store8((var6 + i32_load(var0 + 8)), var3)
                    var3 = i32_load(var0 + 20)
                    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                    i32_store8((var3 + i32_load(var0 + 8)), i32_load8_u(var9))
                    var3 = i32_load(var0 + 5820)
                    var5 = ((var7 + i32_load(var0 + 5820)) - 16)
                    var3 = ((var8 & 0xFFFFFFFF) >> (16 - var3))
                    break
                var5 = (var6 + var7)
                i32_store(var0 + 5820, var5)
                var6 = (var4 + 65534)
                if (1 if var5 >= 14 else 0):
                    var3 = (var3 | (var6 << var5))
                    i32_store16(var0 + 5816, (var3 | (var6 << var5)))
                    var4 = i32_load(var0 + 20)
                    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                    i32_store8((var4 + i32_load(var0 + 8)), var3)
                    var4 = i32_load(var0 + 20)
                    i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                    i32_store8((var4 + i32_load(var0 + 8)), i32_load8_u(var9))
                    var4 = i32_load(var0 + 5820)
                    i32_store16(var0 + 5816, (((var6 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
                    break
                i32_store16(var0 + 5816, (var3 | (var6 << var5)))
                break
            var8 = i32_load16_u(var0 + 2756)
            var3 = (var3 | (i32_load16_u(var0 + 2756) << var6))
            var7 = i32_load16_u(var0 + 2758)
            if (1 if (16 - i32_load16_u(var0 + 2758)) < var6 else 0):
                i32_store16(var0 + 5816, var3)
                var6 = i32_load(var0 + 20)
                i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                i32_store8((var6 + i32_load(var0 + 8)), var3)
                var3 = i32_load(var0 + 20)
                i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                i32_store8((var3 + i32_load(var0 + 8)), i32_load8_u(var9))
                var3 = i32_load(var0 + 5820)
                var5 = ((var7 + i32_load(var0 + 5820)) - 16)
                var3 = ((var8 & 0xFFFFFFFF) >> (16 - var3))
                break
            var5 = (var6 + var7)
            i32_store(var0 + 5820, var5)
            var6 = (var4 + 65526)
            if (1 if var5 >= 10 else 0):
                var3 = (var3 | (var6 << var5))
                i32_store16(var0 + 5816, (var3 | (var6 << var5)))
                var4 = i32_load(var0 + 20)
                i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                i32_store8((var4 + i32_load(var0 + 8)), var3)
                var4 = i32_load(var0 + 20)
                i32_store(var0 + 20, (i32_load(var0 + 20) + 1))
                i32_store8((var4 + i32_load(var0 + 8)), i32_load8_u(var9))
                var4 = i32_load(var0 + 5820)
                i32_store16(var0 + 5816, (((var6 & 65535) & 0xFFFFFFFF) >> (16 - i32_load(var0 + 5820))))
                break
            i32_store16(var0 + 5816, (var3 | (var6 << var5)))
            i32_store((var4 - 9) + 5820, (var5 + 7))
            var4 = 0
            if (1 if var11 == 0 else 0):
                var5 = 138
                break
            var3 = (1 if var10 == var11 else 0)
            var5 = (6 if (1 if var10 == var11 else 0) else 7)
            var8 = (3 if var3 else 4)
            var6 = var10
            if (1 if var2 != var14 else 0):
                continue
            break  # end loop
    return 3


# ==========================================================
# $func335
# ==========================================================
def func335(var0, var1, var2, var3):
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
    var19 = 0
    var20 = 0
    var21 = 0
    var22 = 0
    var23 = 0
    var24 = 0
    var25 = 0
    var18 = (var1 - 30)
    var19 = ((var1 - 30) + 60)
    var6 = (var0 - 30)
    var20 = ((var0 - 30) + 60)
    var8 = i32_load(9142440)
    var10 = (i32_load(9142440) + 2)
    var21 = ((i32_load(9142440) + 2) * i32_load(((var2 * 404) + 9568096) + 208))
    var22 = (var8 + 4)
    var23 = i32_load(9671128)
    var11 = i32_load(9142840)
    var9 = 2147483647
    var24 = (1 if i32_load(38500) != var2 else 0)
    while True:  # loop $label3
        var12 = (var6 + 1)
        if (1 if var6 < var8 else 0):
            var4 = (var0 - var6)
            var25 = ((var0 - var6) * var4)
            var5 = var18
            while True:  # loop $label2
                if (1 if var5 >= var8 else 0):
                    break
                if (1 if (var5 | var6) < 0 else 0):
                    break
                var4 = (var1 - var5)
                var13 = (((var1 - var5) * var4) + var25)
                if (1 if (((var1 - var5) * var4) + var25) >= var9 else 0):
                    break
                var7 = i32_load((var11 + ((var12 + (((var5 + var21) + 1) * var10)) << 2)))
                if (1 if i32_load((var11 + ((var12 + (((var5 + var21) + 1) * var10)) << 2))) == 0 else 0):
                    break
                if (1 if var3 == var7 else 0):
                    break
                var14 = (var23 + (var7 * 132))
                var15 = (1 if i32_load8_u((var23 + (var7 * 132)) + 122) != var2 else 0)
                var4 = (var9 if (1 if i32_load8_u((var23 + (var7 * 132)) + 122) != var2 else 0) else var13)
                var17 = (var16 if var15 else var7)
                if var15:
                    break
                if var24:
                    break
                var17 = var7
                var4 = var13
                if i32_load((((i32_load16_u(var14 + 112) + ((var22 + i32_load16_u(var14 + 114)) * var10)) << 2) + var11) + 8):
                    break
                var16 = var17
                var9 = var4
                var5 = (var5 + 1)
                if (1 if (var5 + 1) < var19 else 0):
                    continue
                break  # end loop
        var6 = var12
        if (1 if var12 < var20 else 0):
            continue
        break  # end loop
    return var16


# ==========================================================
# $func336
# ==========================================================
def func336(var0, var1, var2):
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
    var19 = 0
    var20 = 0
    var12 = (var0 + 29)
    var13 = (var1 + 29)
    var14 = (var1 - 30)
    var4 = (var0 - 30)
    var7 = i32_load(9142440)
    var8 = (i32_load(9142440) + 2)
    var15 = i32_load(38564)
    var16 = i32_load(9671128)
    var17 = i32_load(9142840)
    var9 = 2147483647
    while True:  # loop $label3
        var11 = (var4 + 1)
        if (1 if var4 < var7 else 0):
            var3 = (var4 - var0)
            var18 = ((var4 - var0) * var3)
            var3 = var14
            while True:  # loop $label2
                var5 = var3
                if (1 if var7 <= var3 else 0):
                    break
                if (1 if (var4 | var5) < 0 else 0):
                    break
                var3 = (var5 - var1)
                var3 = (((var5 - var1) * var3) + var18)
                if (1 if (((var5 - var1) * var3) + var18) >= var9 else 0):
                    break
                var6 = (var16 + (i32_load((var17 + ((var11 + (((var5 + var8) + 1) * var8)) << 2))) * 132))
                if (1 if i32_load((var16 + (i32_load((var17 + ((var11 + (((var5 + var8) + 1) * var8)) << 2))) * 132)) + 64) >= i32_load(var6 + 68) else 0):
                    break
                if (1 if i32_load16_u(var6 + 110) != var2 else 0):
                    break
                var19 = i32_load8_u(var6 + 122)
                var20 = ((i32_load8_u(var6 + 122) * 404) + 9568096)
                if (1 if i32_load(((i32_load8_u(var6 + 122) * 404) + 9568096) + 264) != 1 else 0):
                    break
                if (1 if i32_load(var20 + 188) != 55 else 0):
                    break
                if (1 if var15 != var19 else 0):
                    break
                # br_table ['$label1', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label1', '$label0']
                _br_idx = (i32_load8_u(var6 + 125) - 4)
                break  # br_table
                var10 = i32_load(var6 + 28)
                var9 = var3
                var3 = (var5 + 1)
                if (1 if var5 < var13 else 0):
                    continue
                break  # end loop
        var3 = (1 if var4 < var12 else 0)
        var4 = var11
        if var3:
            continue
        break  # end loop
    return var10


# ==========================================================
# $D
# Export: D
# ==========================================================
def D(var0):
    """Export: D"""
    var1 = 0
    var2 = 0
    var3 = 0
    var3 = i64_load(9147316)
    var1 = i32_load(9147312)
    i32_store(9147316, i32_load(9147312))
    var2 = i32_load(9147324)
    i64_store(9147320, var3)
    var2 = (var2 ^ (var2 << 11))
    var1 = ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8))) ^ var2)
    i32_store(9147312, ((var1 ^ (((var1 & 0xFFFFFFFF) >> 19) ^ (((var2 ^ (var2 << 11)) & 0xFFFFFFFF) >> 8))) ^ var2))
    return (var1 % var0)


# ==========================================================
# $func353
# ==========================================================
def func353(var0, var1, var2):
    # br_table ['$label0', '$label1', '$label2', '$label3', '$label1', '$label2', '$label4', '$label5', '$label6', '$label7', '$label3', '$label2', '$label3', '$label3', '$label1', '$label2', '$label8', '$label9', '$label10']
    _br_idx = (var1 - 9)
    break  # br_table
    var1 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 4))
    i32_store(var0, i32_load(var1))
    return
    var1 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 4))
    i64_store(var0, i64_load16_s(var1))
    return
    var1 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 4))
    i64_store(var0, i64_load16_u(var1))
    return
    var1 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 4))
    i64_store(var0, i64_load8_s(var1))
    return
    var1 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 4))
    i64_store(var0, i64_load8_u(var1))
    return
    var1 = ((i32_load(var2) + 7) & -8)
    i32_store(var2, (((i32_load(var2) + 7) & -8) + 8))
    f64_store(var0, f64_load(var1))
    return
    raise RuntimeError('unreachable')
    return
    var1 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 4))
    i64_store(var0, i64_load32_s(var1))
    return
    var1 = i32_load(var2)
    i32_store(var2, (i32_load(var2) + 4))
    i64_store(var0, i64_load32_u(var1))
    return
    var1 = ((i32_load(var2) + 7) & -8)
    i32_store(var2, (((i32_load(var2) + 7) & -8) + 8))
    i64_store(var0, i64_load(var1))


# ==========================================================
# $func358
# ==========================================================
def func358(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var2 = 4
    if ((var0 | var1) & 3):
        break
    while True:  # loop $label1
        if (1 if i32_load(var0) != i32_load(var1) else 0):
            break
        var1 = (var1 + 4)
        var0 = (var0 + 4)
        var2 = (var2 - 4)
        if (1 if (var2 - 4) > 3 else 0):
            continue
        break  # end loop
    if (1 if var2 == 0 else 0):
        break
    while True:  # loop $label3
        var3 = i32_load8_u(var0)
        var4 = i32_load8_u(var1)
        if (1 if i32_load8_u(var0) == i32_load8_u(var1) else 0):
            var1 = (var1 + 1)
            var0 = (var0 + 1)
            var2 = (var2 - 1)
            if (var2 - 1):
                continue
            break
        break  # end loop
    return (var3 - var4)
    return 0

