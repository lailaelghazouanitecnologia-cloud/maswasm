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
# $func153
# ==========================================================
def func153(var0, var1, var2, var3, var4):
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
    var26 = 0
    var27 = 0
    var28 = 0
    var29 = 0
    var30 = 0
    var31 = 0
    var17 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var25 = (var3 + 120)
    var12 = (var3 + 24)
    if (1 if var2 == 0 else 0):
        break
    while True:  # loop $label10
        if (1 if func39(var12, 1) == 0 else 0):
            break
        var5 = i32_load(var3 + 192)
        var10 = func39(var12, 2)
        var7 = i32_load(var3 + 276)
        var13 = (1 << var10)
        if (i32_load(var3 + 276) & (1 << var10)):
            break
        i32_store(var3 + 276, (var7 | var13))
        var5 = (var3 + (var5 * 20))
        var18 = ((var3 + (var5 * 20)) + 212)
        i32_store(((var3 + (var5 * 20)) + 212), 0)
        i32_store(var5 + 208, var1)
        i32_store(var5 + 204, var0)
        i32_store(var5 + 196, var10)
        var7 = i32_load(var3 + 192)
        i32_store(var3 + 192, (i32_load(var3 + 192) + 1))
        if (1 if var7 >= 4 else 0):
            break
        var7 = 1
        # br_table ['$label3', '$label3', '$label4', '$label5', '$label6']
        _br_idx = var10
        break  # br_table
        var0 = (func39(var12, 8) + 1)
        if (1 if (func39(var12, 8) + 1) > 16 else 0):
            break
        if (1 if var0 > 4 else 0):
            break
        var7 = (2 if (1 if var0 > 2 else 0) else 3)
        var11 = i32_load(var5 + 204)
        i32_store(var5 + 200, var7)
        if (1 if func153(var0, 1, 0, var3, var18) == 0 else 0):
            break
        var6 = ((8 & 0xFFFFFFFF) >> i32_load(var5 + 200))
        var5 = func58(i64_extend_u((1 << ((8 & 0xFFFFFFFF) >> i32_load(var5 + 200)))), 4)
        if func58(i64_extend_u((1 << ((8 & 0xFFFFFFFF) >> i32_load(var5 + 200)))), 4):
            var15 = i32_load(var18)
            i32_store(var5, i32_load(i32_load(var18)))
            var9 = 4
            if (1 if var0 < 2 else 0):
                break
            var0 = (var0 << 2)
            var9 = (5 if (1 if var0 <= 5 else 0) else (var0 << 2))
            var8 = ((5 if (1 if var0 <= 5 else 0) else (var0 << 2)) & 1)
            var10 = 4
            if (1 if var0 >= 6 else 0):
                var14 = ((var9 & 2147483644) - 6)
                var13 = 0
                while True:  # loop $label9
                    var0 = (var5 + var10)
                    i32_store8((var5 + var10), (i32_load8_u((var0 - 4)) + i32_load8_u((var10 + var15))))
                    var21 = (var10 | 1)
                    i32_store8((var5 + (var10 | 1)), (i32_load8_u((var0 - 3)) + i32_load8_u((var15 + var21))))
                    var10 = (var10 + 2)
                    var0 = (1 if var13 == var14 else 0)
                    var13 = (var13 + 2)
                    if (1 if var0 == 0 else 0):
                        continue
                    break  # end loop
            if (1 if var8 == 0 else 0):
                break
            var0 = (var5 + var10)
            i32_store8((var5 + var10), (i32_load8_u((var0 - 4)) + i32_load8_u((var10 + var15))))
            var0 = (4 << var6)
            if (1 if var9 < (4 << var6) else 0):
                # Unknown: memory.fill []
            var0 = ((((var11 + (1 << var7)) - 1) & 0xFFFFFFFF) >> var7)
            i32_store(var18, var5)
            continue
        var13 = 1
        var7 = i32_load(var3)
        # br_table ['$label11', '$label12', '$label12', '$label12', '$label12', '$label11', '$label12']
        _br_idx = i32_load(var3)
        break  # br_table
        a_c()
        raise RuntimeError('unreachable')
        var7 = (func39(var12, 3) + 2)
        i32_store(var5 + 200, (func39(var12, 3) + 2))
        var10 = ((-1 << var7) ^ -1)
        var7 = func153((((((-1 << var7) ^ -1) + i32_load(var5 + 204)) & 0xFFFFFFFF) >> var7), (((i32_load(var5 + 208) + var10) & 0xFFFFFFFF) >> var7), 0, var3, var18)
        if var7:
            continue
        break  # end loop
    break
    var18 = 0
    if (1 if func39(var12, 1) == 0 else 0):
        break
    var18 = func39(var12, 4)
    if (1 if (func39(var12, 4) - 1) < 11 else 0):
        break
    var13 = 3
    var10 = 0
    # br_table ['$label11', '$label14', '$label14', '$label14', '$label14', '$label11', '$label14']
    _br_idx = i32_load(var3)
    break  # br_table
    i32_store(var17 + 12, 0)
    i32_store(var17 + 8, 0)
    var15 = (var3 + 172)
    if i32_load((var3 + 172)):
        break
    if i32_load(var3 + 188):
        break
    var10 = 1
    if (1 if var2 == 0 else 0):
        var13 = 0
        var7 = 1
        break
    var13 = 0
    var7 = 1
    if (1 if func39(var12, 1) == 0 else 0):
        break
    var7 = 0
    var5 = (func39(var12, 3) + 2)
    var12 = (1 << (func39(var12, 3) + 2))
    var9 = ((((var0 + (1 << (func39(var12, 3) + 2))) - 1) & 0xFFFFFFFF) >> var5)
    var12 = ((((var1 + var12) - 1) & 0xFFFFFFFF) >> var5)
    if (1 if func153(((((var0 + (1 << (func39(var12, 3) + 2))) - 1) & 0xFFFFFFFF) >> var5), ((((var1 + var12) - 1) & 0xFFFFFFFF) >> var5), 0, var3, (var17 + 12)) == 0 else 0):
        break
    i32_store(var3 + 152, var5)
    var5 = (var9 * var12)
    if (1 if (var9 * var12) <= 0 else 0):
        break
    var7 = i32_load(var17 + 12)
    if (1 if var5 != 1 else 0):
        var6 = (var5 & -2)
        var12 = 0
        while True:  # loop $label20
            var11 = (var13 << 2)
            var9 = (var7 + (var13 << 2))
            var9 = i32_load16_u(var9 + 1)
            i32_store((var7 + (var13 << 2)), i32_load16_u(var9 + 1))
            var11 = (var7 + (var11 | 4))
            var11 = i32_load16_u(var11 + 1)
            i32_store((var7 + (var11 | 4)), i32_load16_u(var11 + 1))
            var10 = (var10 if (1 if var9 < var10 else 0) else (var9 + 1))
            var10 = ((var10 if (1 if var9 < var10 else 0) else (var9 + 1)) if (1 if var10 > var11 else 0) else (var11 + 1))
            var13 = (var13 + 2)
            var12 = (var12 + 2)
            if (1 if (var12 + 2) != var6 else 0):
                continue
            break  # end loop
    if (1 if (var5 & 1) == 0 else 0):
        break
    var7 = (var7 + (var13 << 2))
    var7 = i32_load16_u(var7 + 1)
    i32_store((var7 + (var13 << 2)), i32_load16_u(var7 + 1))
    var10 = (var10 if (1 if var7 < var10 else 0) else (var7 + 1))
    if (1 if var10 > 1000 else 0):
        break
    var13 = 0
    if (1 if var10 > (var0 * var1) else 0):
        break
    var7 = var10
    break
    var13 = func58(i64_extend_u(var10), 4)
    if (1 if func58(i64_extend_u(var10), 4) == 0 else 0):
        var7 = 0
        var13 = 0
        # br_table ['$label22', '$label18', '$label18', '$label18', '$label18', '$label22', '$label18']
        _br_idx = i32_load(var3)
        break  # br_table
        i32_store(var3, 1)
        break
    # Unknown: memory.fill []
    if (1 if var5 <= 0 else 0):
        var7 = 0
        break
    var6 = (var5 & 1)
    var11 = i32_load(var17 + 12)
    if (1 if var5 == 1 else 0):
        var7 = 0
        var5 = 0
        break
    var8 = (var5 & -2)
    var7 = 0
    var5 = 0
    var9 = 0
    while True:  # loop $label24
        var14 = (var7 << 2)
        var21 = (var11 + (var7 << 2))
        var24 = (var13 + (i32_load((var11 + (var7 << 2))) << 2))
        var12 = i32_load((var13 + (i32_load((var11 + (var7 << 2))) << 2)))
        if (1 if i32_load((var13 + (i32_load((var11 + (var7 << 2))) << 2))) == -1 else 0):
            i32_store(var24, var5)
            var12 = var5
            var5 = (var5 + 1)
        i32_store(var21, var12)
        var14 = (var11 + (var14 | 4))
        var21 = (var13 + (i32_load((var11 + (var14 | 4))) << 2))
        var12 = i32_load((var13 + (i32_load((var11 + (var14 | 4))) << 2)))
        if (1 if i32_load((var13 + (i32_load((var11 + (var14 | 4))) << 2))) == -1 else 0):
            i32_store(var21, var5)
            var12 = var5
            var5 = (var5 + 1)
        i32_store(var14, var12)
        var7 = (var7 + 2)
        var9 = (var9 + 2)
        if (1 if (var9 + 2) != var8 else 0):
            continue
        break  # end loop
    if (1 if var6 == 0 else 0):
        var7 = var5
        break
    var9 = (var11 + (var7 << 2))
    var7 = (var13 + (i32_load((var11 + (var7 << 2))) << 2))
    var12 = i32_load((var13 + (i32_load((var11 + (var7 << 2))) << 2)))
    if (1 if i32_load((var13 + (i32_load((var11 + (var7 << 2))) << 2))) != -1 else 0):
    else:
        i32_store(var7, var5)
        var12 = var5
    var7 = (var5 + 1)
    i32_store(var9, var12)
    if i32_load(var3 + 48):
        var7 = 0
        break
    var9 = 0
    if (1 if var7 > var10 else 0):
        break
    if ((1 if var13 == 0 else 0) & (1 if var7 != var10 else 0)):
        break
    var12 = i32_load16_u(((var18 << 1) + 13776))
    var11 = (1 << var18)
    var9 = func134(i64_extend_s((280 if (1 if var18 <= 0 else 0) else ((1 << var18) + 280))), 4)
    var5 = func58(i64_extend_s(var7), 548)
    if (1 if var7 < 65537 else 0):
        break
    if (1 if var5 == 0 else 0):
        break
    a_c()
    raise RuntimeError('unreachable')
    i32_store(var17 + 8, var5)
    if (1 if var5 == 0 else 0):
        break
    if (1 if var9 == 0 else 0):
        break
    if (1 if func452((var7 * var12), var15) == 0 else 0):
        break
    if (1 if var10 > 0 else 0):
        var21 = (280 if (1 if var18 <= 0 else 0) else (var11 + 280))
        var5 = ((280 if (1 if var18 <= 0 else 0) else (var11 + 280)) - 1)
        var29 = (((280 if (1 if var18 <= 0 else 0) else (var11 + 280)) - 1) & -4)
        var24 = (var5 & 3)
        var30 = (1 if (var21 - 2) < 3 else 0)
        var12 = 0
        while True:  # loop $label41
            var5 = var12
            if (1 if var13 == 0 else 0):
                break
            var5 = i32_load((var13 + (var12 << 2)))
            if (1 if i32_load((var13 + (var12 << 2))) != -1 else 0):
                break
            if (1 if func83(var21, var3, var9, 0) == 0 else 0):
                break
            if (1 if func83(256, var3, var9, 0) == 0 else 0):
                break
            if (1 if func83(256, var3, var9, 0) == 0 else 0):
                break
            if (1 if func83(256, var3, var9, 0) == 0 else 0):
                break
            if func83(40, var3, var9, 0):
                break
            break
            var11 = i32_load(var17 + 8)
            var6 = func83(var21, var3, var9, var15)
            var11 = (var11 + (var5 * 548))
            var5 = i32_load(i32_load(var15 + 16) + 4)
            i32_store((var11 + (var5 * 548)), i32_load(i32_load(var15 + 16) + 4))
            if (1 if var6 == 0 else 0):
                break
            var19 = i32_load8_u(var5)
            var5 = i32_load(var15 + 16)
            i32_store(i32_load(var15 + 16) + 4, (i32_load(var5 + 4) + (var6 << 2)))
            var14 = i32_load(var9)
            if (1 if var21 < 2 else 0):
                break
            var8 = 0
            var5 = 1
            if (1 if var30 == 0 else 0):
                while True:  # loop $label31
                    var6 = (var9 + (var5 << 2))
                    var22 = i32_load((var9 + (var5 << 2)) + 12)
                    var16 = i32_load(var6 + 8)
                    var20 = i32_load(var6 + 4)
                    var6 = i32_load(var6)
                    var6 = (i32_load(var6) if (1 if var6 > var14 else 0) else var14)
                    var6 = (i32_load(var6 + 4) if (1 if var6 < var20 else 0) else (i32_load(var6) if (1 if var6 > var14 else 0) else var14))
                    var6 = (i32_load(var6 + 8) if (1 if var6 < var16 else 0) else (i32_load(var6 + 4) if (1 if var6 < var20 else 0) else (i32_load(var6) if (1 if var6 > var14 else 0) else var14)))
                    var14 = (i32_load((var9 + (var5 << 2)) + 12) if (1 if var6 < var22 else 0) else (i32_load(var6 + 8) if (1 if var6 < var16 else 0) else (i32_load(var6 + 4) if (1 if var6 < var20 else 0) else (i32_load(var6) if (1 if var6 > var14 else 0) else var14))))
                    var5 = (var5 + 4)
                    var8 = (var8 + 4)
                    if (1 if (var8 + 4) != var29 else 0):
                        continue
                    break  # end loop
            var6 = 0
            if (1 if var24 == 0 else 0):
                break
            while True:  # loop $label32
                var8 = i32_load((var9 + (var5 << 2)))
                var14 = (i32_load((var9 + (var5 << 2))) if (1 if var8 > var14 else 0) else var14)
                var5 = (var5 + 1)
                var6 = (var6 + 1)
                if (1 if (var6 + 1) != var24 else 0):
                    continue
                break  # end loop
            var5 = func83(256, var3, var9, var15)
            var6 = i32_load(i32_load(var15 + 16) + 4)
            i32_store(var11 + 4, i32_load(i32_load(var15 + 16) + 4))
            if (1 if var5 == 0 else 0):
                break
            var22 = i32_load8_u(var6)
            var6 = i32_load(var15 + 16)
            i32_store(i32_load(var15 + 16) + 4, (i32_load(var6 + 4) + (var5 << 2)))
            var6 = i32_load(var9)
            var8 = 1
            while True:  # loop $label33
                var5 = (var9 + (var8 << 2))
                var16 = i32_load((var9 + (var8 << 2)) + 16)
                var20 = i32_load(var5 + 12)
                var26 = i32_load(var5 + 8)
                var23 = i32_load(var5 + 4)
                var5 = i32_load(var5)
                var5 = (i32_load(var5) if (1 if var5 > var6 else 0) else var6)
                var5 = (i32_load(var5 + 4) if (1 if var5 < var23 else 0) else (i32_load(var5) if (1 if var5 > var6 else 0) else var6))
                var5 = (i32_load(var5 + 8) if (1 if var5 < var26 else 0) else (i32_load(var5 + 4) if (1 if var5 < var23 else 0) else (i32_load(var5) if (1 if var5 > var6 else 0) else var6)))
                var5 = (i32_load(var5 + 12) if (1 if var5 < var20 else 0) else (i32_load(var5 + 8) if (1 if var5 < var26 else 0) else (i32_load(var5 + 4) if (1 if var5 < var23 else 0) else (i32_load(var5) if (1 if var5 > var6 else 0) else var6))))
                var6 = (i32_load((var9 + (var8 << 2)) + 16) if (1 if var5 < var16 else 0) else (i32_load(var5 + 12) if (1 if var5 < var20 else 0) else (i32_load(var5 + 8) if (1 if var5 < var26 else 0) else (i32_load(var5 + 4) if (1 if var5 < var23 else 0) else (i32_load(var5) if (1 if var5 > var6 else 0) else var6)))))
                var8 = (var8 + 5)
                if (1 if (var8 + 5) != 256 else 0):
                    continue
                break  # end loop
            var5 = func83(256, var3, var9, var15)
            var8 = i32_load(i32_load(var15 + 16) + 4)
            i32_store(var11 + 8, i32_load(i32_load(var15 + 16) + 4))
            if (1 if var5 == 0 else 0):
                break
            var16 = 0
            if (1 if var22 == 0 else 0):
                var16 = (1 if i32_load8_u(var8) == 0 else 0)
            var20 = (var6 + var14)
            var26 = i32_load8_u(var8)
            var6 = i32_load(var15 + 16)
            i32_store(i32_load(var15 + 16) + 4, (i32_load(var6 + 4) + (var5 << 2)))
            var6 = i32_load(var9)
            var8 = 1
            while True:  # loop $label34
                var5 = (var9 + (var8 << 2))
                var14 = i32_load((var9 + (var8 << 2)) + 16)
                var23 = i32_load(var5 + 12)
                var27 = i32_load(var5 + 8)
                var28 = i32_load(var5 + 4)
                var5 = i32_load(var5)
                var5 = (i32_load(var5) if (1 if var5 > var6 else 0) else var6)
                var5 = (i32_load(var5 + 4) if (1 if var5 < var28 else 0) else (i32_load(var5) if (1 if var5 > var6 else 0) else var6))
                var5 = (i32_load(var5 + 8) if (1 if var5 < var27 else 0) else (i32_load(var5 + 4) if (1 if var5 < var28 else 0) else (i32_load(var5) if (1 if var5 > var6 else 0) else var6)))
                var5 = (i32_load(var5 + 12) if (1 if var5 < var23 else 0) else (i32_load(var5 + 8) if (1 if var5 < var27 else 0) else (i32_load(var5 + 4) if (1 if var5 < var28 else 0) else (i32_load(var5) if (1 if var5 > var6 else 0) else var6))))
                var6 = (i32_load((var9 + (var8 << 2)) + 16) if (1 if var5 < var14 else 0) else (i32_load(var5 + 12) if (1 if var5 < var23 else 0) else (i32_load(var5 + 8) if (1 if var5 < var27 else 0) else (i32_load(var5 + 4) if (1 if var5 < var28 else 0) else (i32_load(var5) if (1 if var5 > var6 else 0) else var6)))))
                var8 = (var8 + 5)
                if (1 if (var8 + 5) != 256 else 0):
                    continue
                break  # end loop
            var5 = func83(256, var3, var9, var15)
            var8 = i32_load(i32_load(var15 + 16) + 4)
            i32_store(var11 + 12, i32_load(i32_load(var15 + 16) + 4))
            if (1 if var5 == 0 else 0):
                break
            if var16:
            else:
            var14 = (1 if 1 == 0 else 0)
            var16 = (var6 + var20)
            var20 = i32_load8_u(var8)
            var6 = i32_load(var15 + 16)
            i32_store(i32_load(var15 + 16) + 4, (i32_load(var6 + 4) + (var5 << 2)))
            var6 = i32_load(var9)
            var8 = 1
            while True:  # loop $label35
                var5 = (var9 + (var8 << 2))
                var23 = i32_load((var9 + (var8 << 2)) + 16)
                var27 = i32_load(var5 + 12)
                var28 = i32_load(var5 + 8)
                var31 = i32_load(var5 + 4)
                var5 = i32_load(var5)
                var5 = (i32_load(var5) if (1 if var5 > var6 else 0) else var6)
                var5 = (i32_load(var5 + 4) if (1 if var5 < var31 else 0) else (i32_load(var5) if (1 if var5 > var6 else 0) else var6))
                var5 = (i32_load(var5 + 8) if (1 if var5 < var28 else 0) else (i32_load(var5 + 4) if (1 if var5 < var31 else 0) else (i32_load(var5) if (1 if var5 > var6 else 0) else var6)))
                var5 = (i32_load(var5 + 12) if (1 if var5 < var27 else 0) else (i32_load(var5 + 8) if (1 if var5 < var28 else 0) else (i32_load(var5 + 4) if (1 if var5 < var31 else 0) else (i32_load(var5) if (1 if var5 > var6 else 0) else var6))))
                var6 = (i32_load((var9 + (var8 << 2)) + 16) if (1 if var5 < var23 else 0) else (i32_load(var5 + 12) if (1 if var5 < var27 else 0) else (i32_load(var5 + 8) if (1 if var5 < var28 else 0) else (i32_load(var5 + 4) if (1 if var5 < var31 else 0) else (i32_load(var5) if (1 if var5 > var6 else 0) else var6)))))
                var8 = (var8 + 5)
                if (1 if (var8 + 5) != 256 else 0):
                    continue
                break  # end loop
            var5 = func83(40, var3, var9, var15)
            var8 = i32_load(i32_load(var15 + 16) + 4)
            i32_store(var11 + 16, i32_load(i32_load(var15 + 16) + 4))
            if (1 if var5 == 0 else 0):
                break
            var22 = (var20 + (var26 + (var19 + var22)))
            var8 = i32_load8_u(var8)
            var19 = i32_load(var15 + 16)
            i32_store(i32_load(var15 + 16) + 4, (i32_load(var19 + 4) + (var5 << 2)))
            i32_store(var11 + 28, 0)
            i32_store(var11 + 20, var14)
            if (1 if var14 == 0 else 0):
                break
            var5 = ((i32_load16_u(i32_load(var11 + 8) + 2) | (i32_load16_u(i32_load(var11 + 4) + 2) << 16)) | (i32_load16_u(i32_load(var11 + 12) + 2) << 24))
            i32_store(var11 + 24, ((i32_load16_u(i32_load(var11 + 8) + 2) | (i32_load16_u(i32_load(var11 + 4) + 2) << 16)) | (i32_load16_u(i32_load(var11 + 12) + 2) << 24)))
            if (1 if var22 != (0 - var8) else 0):
                break
            var8 = i32_load16_u(i32_load(var11) + 2)
            if (1 if i32_load16_u(i32_load(var11) + 2) > 255 else 0):
                break
            i32_store(var11 + 28, 1)
            i32_store(var11 + 24, ((var8 << 8) | var5))
            i32_store(var11 + 32, 0)
            break
            var5 = (var6 + var16)
            i32_store(var11 + 32, (1 if (var6 + var16) < 6 else 0))
            if (1 if var5 > 5 else 0):
                break
            var22 = i32_load(var11)
            var5 = 0
            while True:  # loop $label40
                var6 = (var11 + (var5 << 3))
                var8 = i32_load((var22 + (var5 << 2)))
                var14 = ((i32_load((var22 + (var5 << 2))) & 0xFFFFFFFF) >> 16)
                if (1 if var8 >= 16777216 else 0):
                    i32_store(var6 + 36, ((var8 & 255) | 256))
                    i32_store(var6 + 40, var14)
                    break
                var8 = (var8 & 255)
                i32_store(var6 + 36, (var8 & 255))
                var14 = (var14 << 8)
                i32_store(var6 + 40, (var14 << 8))
                if (1 if var8 >= 9 else 0):
                    break
                var16 = ((var5 & 0xFFFFFFFF) >> var8)
                var19 = (i32_load(var11 + 4) + (((var5 & 0xFFFFFFFF) >> var8) << 2))
                var20 = i32_load16_u((i32_load(var11 + 4) + (((var5 & 0xFFFFFFFF) >> var8) << 2)) + 2)
                var19 = i32_load8_u(var19)
                var8 = (var8 + i32_load8_u(var19))
                i32_store(var6 + 36, (var8 + i32_load8_u(var19)))
                var14 = ((var20 << 16) | var14)
                i32_store(var6 + 40, ((var20 << 16) | var14))
                if (1 if var8 >= 9 else 0):
                    break
                var16 = ((var16 & 0xFFFFFFFF) >> var19)
                var19 = (i32_load(var11 + 8) + (((var16 & 0xFFFFFFFF) >> var19) << 2))
                var20 = i32_load16_u((i32_load(var11 + 8) + (((var16 & 0xFFFFFFFF) >> var19) << 2)) + 2)
                var19 = i32_load8_u(var19)
                var8 = (var8 + i32_load8_u(var19))
                i32_store(var6 + 36, (var8 + i32_load8_u(var19)))
                var14 = (var14 | var20)
                i32_store(var6 + 40, (var14 | var20))
                if (1 if var8 >= 9 else 0):
                    break
                var16 = (i32_load(var11 + 12) + (((var16 & 0xFFFFFFFF) >> var19) << 2))
                var19 = i32_load16_u((i32_load(var11 + 12) + (((var16 & 0xFFFFFFFF) >> var19) << 2)) + 2)
                var8 = (var8 + i32_load8_u(var16))
                i32_store(var6 + 36, (var8 + i32_load8_u(var16)))
                i32_store(var6 + 40, ((var19 << 24) | var14))
                if (1 if var8 >= 9 else 0):
                    break
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != 64 else 0):
                    continue
                break  # end loop
            var12 = (var12 + 1)
            if (1 if (var12 + 1) != var10 else 0):
                continue
            break  # end loop
    break
    break
    # br_table ['$label43', '$label25', '$label25', '$label25', '$label25', '$label43', '$label25']
    _br_idx = i32_load(var3)
    break  # br_table
    i32_store(var3, 1)
    func116(var15)
    func151(i32_load(var17 + 8))
    i32_store(var17 + 8, 0)
    break
    a_c()
    raise RuntimeError('unreachable')
    if 4903:
        break
    var7 = i32_load(var17 + 8)
    func116(var15)
    func151(var7)
    var7 = i32_load(var3)
    var13 = 3
    var10 = 0
    # br_table ['$label11', '$label14', '$label14', '$label14', '$label14', '$label11', '$label14']
    _br_idx = var7
    break  # br_table
    var5 = i32_load(var17 + 12)
    i32_store(var3 + 164, var7)
    i32_store(var3 + 160, var5)
    i32_store(var3 + 168, i32_load(var17 + 8))
    if (1 if var18 > 0 else 0):
        i32_store(var3 + 120, (1 << var18))
        if func455((var3 + 124), var18):
            break
        var13 = 1
        var10 = 0
        # br_table ['$label11', '$label14', '$label14', '$label14', '$label14', '$label11', '$label14']
        _br_idx = i32_load(var3)
        break  # br_table
    i32_store(var25, 0)
    i32_store(var3 + 104, var1)
    i32_store(var3 + 100, var0)
    var5 = i32_load(var3 + 152)
    i32_store(var3 + 148, (((-1 << i32_load(var3 + 152)) ^ -1) if var5 else -1))
    i32_store(var3 + 156, ((((var0 + (1 << var5)) - 1) & 0xFFFFFFFF) >> var5))
    if var2:
        break
    var10 = func58((i64_extend_s(var0) * i64_extend_s(var1)), 4)
    if (1 if func58((i64_extend_s(var0) * i64_extend_s(var1)), 4) == 0 else 0):
        var13 = 1
        var10 = 0
        # br_table ['$label11', '$label14', '$label14', '$label14', '$label14', '$label11', '$label14']
        _br_idx = i32_load(var3)
        break  # br_table
    if (1 if func275(var3, var10, var0, var1, var1, 0) == 0 else 0):
        break
    if i32_load(var3 + 48):
        break
    if var4:
        break
    a_c()
    raise RuntimeError('unreachable')
    i32_store(var3, var13)
    var10 = 0
    func116((var3 + 172))
    func151(i32_load(var3 + 168))
    func136((var3 + 124))
    func136((var3 + 136))
    # Unknown: memory.fill []
    break
    i32_store(var3 + 4, 1)
    if (1 if var4 == 0 else 0):
        break
    i32_store(var4, 0)
    i32_store(var3 + 112, 0)
    break
    i32_store(var4, var10)
    i32_store(var3 + 112, 0)
    func116(var15)
    func151(i32_load(var3 + 168))
    func136((var3 + 124))
    func136((var3 + 136))
    # Unknown: memory.fill []
    break
    i32_store(var3 + 112, 0)
    var0 = 1
    global global0
    global0 = (var17 + 16)
    return var0
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    return 3404

