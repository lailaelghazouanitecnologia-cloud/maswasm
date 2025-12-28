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
# $func352
# ==========================================================
def func352(var0, var1, var2, var3, var4):
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
    var7 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    i32_store(var7 + 76, var1)
    var21 = (var7 + 55)
    var17 = (var7 + 56)
    while True:  # loop $label4
        var9 = var1
        if (1 if var5 > (var13 ^ 2147483647) else 0):
            break
        var13 = (var5 + var13)
        var5 = var9
        var6 = i32_load8_u(var9)
        if i32_load8_u(var9):
            while True:  # loop $label64
                var1 = (var6 & 255)
                if (1 if (var6 & 255) == 0 else 0):
                    var1 = var5
                    break
                if (1 if var1 != 37 else 0):
                    break
                var6 = var5
                while True:  # loop $label3
                    if (1 if i32_load8_u(var6 + 1) != 37 else 0):
                        var1 = var6
                        break
                    var5 = (var5 + 1)
                    var10 = i32_load8_u(var6 + 2)
                    var1 = (var6 + 2)
                    var6 = (var6 + 2)
                    if (1 if var10 == 37 else 0):
                        continue
                    break  # end loop
                var5 = (var5 - var9)
                var22 = (var13 ^ 2147483647)
                if (1 if (var5 - var9) > (var13 ^ 2147483647) else 0):
                    break
                if var0:
                if var5:
                    continue
                i32_store(var7 + 76, var1)
                var5 = (var1 + 1)
                var15 = -1
                if (1 if (i32_load8_s(var1 + 1) - 48) >= 10 else 0):
                    break
                if (1 if i32_load8_u(var1 + 2) != 36 else 0):
                    break
                var5 = (var1 + 3)
                var15 = (i32_load8_s(var1 + 1) - 48)
                var18 = 1
                i32_store(var7 + 76, var5)
                var11 = 0
                var6 = i32_load8_s(var5)
                var1 = (i32_load8_s(var5) - 32)
                if (1 if (i32_load8_s(var5) - 32) > 31 else 0):
                    var10 = var5
                    break
                var10 = var5
                var1 = (1 << var1)
                if (1 if ((1 << var1) & 75913) == 0 else 0):
                    break
                while True:  # loop $label7
                    var10 = (var5 + 1)
                    i32_store(var7 + 76, (var5 + 1))
                    var11 = (var1 | var11)
                    var6 = i32_load8_s(var5 + 1)
                    var1 = (i32_load8_s(var5 + 1) - 32)
                    if (1 if (i32_load8_s(var5 + 1) - 32) >= 32 else 0):
                        break
                    var5 = var10
                    var1 = (1 << var1)
                    if ((1 << var1) & 75913):
                        continue
                    break  # end loop
                if (1 if var6 == 42 else 0):
                    if (1 if (i32_load8_s(var10 + 1) - 48) >= 10 else 0):
                        break
                    if (1 if i32_load8_u(var10 + 2) != 36 else 0):
                        break
                    i32_store((((i32_load8_s(var10 + 1) << 2) + var4) - 192), 10)
                    var6 = (var10 + 3)
                    var18 = 1
                    break
                    if var18:
                        break
                    var6 = (var10 + 1)
                    if (1 if var0 == 0 else 0):
                        i32_store(var7 + 76, var6)
                        var18 = 0
                        var16 = 0
                        break
                    var1 = i32_load(var2)
                    i32_store(var2, (i32_load(var2) + 4))
                    var18 = 0
                    var16 = i32_load(var1)
                    i32_store(var7 + 76, var6)
                    if (1 if var16 >= 0 else 0):
                        break
                    var16 = (0 - var16)
                    var11 = (var11 | 8192)
                    break
                var16 = func371((var7 + 76))
                if (1 if func371((var7 + 76)) < 0 else 0):
                    break
                var6 = i32_load(var7 + 76)
                var5 = 0
                var8 = -1
                if (1 if i32_load8_u(var6) != 46 else 0):
                    var1 = var6
                    break
                if (1 if i32_load8_u(var6 + 1) == 42 else 0):
                    if (1 if (i32_load8_s(var6 + 2) - 48) >= 10 else 0):
                        break
                    if (1 if i32_load8_u(var6 + 3) != 36 else 0):
                        break
                    i32_store((((i32_load8_s(var6 + 2) << 2) + var4) - 192), 10)
                    var1 = (var6 + 4)
                    break
                    if var18:
                        break
                    var1 = (var6 + 2)
                    if (1 if var0 == 0 else 0):
                        break
                    var6 = i32_load(var2)
                    i32_store(var2, (i32_load(var2) + 4))
                    var8 = i32_load(var6)
                    i32_store(var7 + 76, var1)
                    break
                i32_store(var7 + 76, (var6 + 1))
                var8 = func371((var7 + 76))
                var1 = i32_load(var7 + 76)
                var19 = 1
                while True:  # loop $label16
                    var14 = var5
                    var10 = 28
                    var12 = var1
                    var5 = i32_load8_s(var1)
                    if (1 if (i32_load8_s(var1) - 123) < -58 else 0):
                        break
                    var1 = (var12 + 1)
                    var5 = i32_load8_u(((var5 + (var14 * 58)) + 31711))
                    if (1 if (i32_load8_u(((var5 + (var14 * 58)) + 31711)) - 1) < 8 else 0):
                        continue
                    break  # end loop
                i32_store(var7 + 76, var1)
                if (1 if var5 != 27 else 0):
                    if (1 if var5 == 0 else 0):
                        break
                    if (1 if var15 >= 0 else 0):
                        i32_store((var4 + (var15 << 2)), var5)
                        i64_store(var7 + 64, i64_load((var3 + (var15 << 3))))
                        break
                    if (1 if var0 == 0 else 0):
                        break
                    func353((var7 - -64), var5, var2)
                    break
                if (1 if var15 >= 0 else 0):
                    break
                var5 = 0
                if (1 if var0 == 0 else 0):
                    continue
                var6 = (var11 & -65537)
                var11 = ((var11 & -65537) if (var11 & 8192) else var11)
                var15 = 0
                var20 = 2107
                var10 = var17
                var5 = i32_load8_s(var12)
                var5 = (((i32_load8_s(var12) & -33) if (1 if (var5 & 15) == 3 else 0) else var5) if var14 else var5)
                # br_table ['$label20', '$label21', '$label21', '$label21', '$label21', '$label21', '$label21', '$label21', '$label21', '$label22', '$label21', '$label23', '$label24', '$label22', '$label22', '$label22', '$label21', '$label24', '$label21', '$label21', '$label21', '$label21', '$label25', '$label26', '$label27', '$label21', '$label21', '$label28', '$label21', '$label29', '$label21', '$label21', '$label20', '$label30']
                _br_idx = ((((i32_load8_s(var12) & -33) if (1 if (var5 & 15) == 3 else 0) else var5) if var14 else var5) - 88)
                break  # br_table
                # br_table ['$label22', '$label21', '$label31', '$label21', '$label22', '$label22', '$label22', '$label32']
                _br_idx = (var5 - 65)
                break  # br_table
                if (1 if var5 == 83 else 0):
                    break
                break
                var23 = i64_load(var7 + 64)
                break
                var5 = 0
                # br_table ['$label35', '$label36', '$label37', '$label38', '$label39', '$label4', '$label40', '$label41', '$label4']
                _br_idx = (var14 & 255)
                break  # br_table
                i32_store(i32_load(var7 + 64), var13)
                continue
                i32_store(i32_load(var7 + 64), var13)
                continue
                i64_store(i32_load(var7 + 64), i64_extend_s(var13))
                continue
                i32_store16(i32_load(var7 + 64), var13)
                continue
                i32_store8(i32_load(var7 + 64), var13)
                continue
                i32_store(i32_load(var7 + 64), var13)
                continue
                i64_store(i32_load(var7 + 64), i64_extend_s(var13))
                continue
                var8 = (8 if (1 if var8 <= 8 else 0) else var8)
                var11 = (var11 | 8)
                var5 = 120
                var9 = var17
                var23 = i64_load(var7 + 64)
                if (1 if i64_load(var7 + 64) != 0 else 0):
                    var12 = (var5 & 32)
                    while True:  # loop $label42
                        var9 = (var9 - 1)
                        i32_store8((var9 - 1), (i32_load8_u(((i32(var23) & 15) + 32240)) | var12))
                        var6 = (1 if var23 > 15 else 0)
                        var23 = ((var23 & 0xFFFFFFFFFFFFFFFF) >> 4)
                        if var6:
                            continue
                        break  # end loop
                if (1 if i64_load(var7 + 64) == 0 else 0):
                    break
                if (1 if (var11 & 8) == 0 else 0):
                    break
                var20 = (((var5 & 0xFFFFFFFF) >> 4) + 2107)
                var15 = 2
                break
                var5 = var17
                var23 = i64_load(var7 + 64)
                if (1 if i64_load(var7 + 64) != 0 else 0):
                    while True:  # loop $label44
                        var5 = (var5 - 1)
                        i32_store8((var5 - 1), ((i32(var23) & 7) | 48))
                        var9 = (1 if var23 > 7 else 0)
                        var23 = ((var23 & 0xFFFFFFFFFFFFFFFF) >> 3)
                        if var9:
                            continue
                        break  # end loop
                var9 = var5
                if (1 if (var11 & 8) == 0 else 0):
                    break
                var5 = (var17 - var9)
                var8 = (var8 if (1 if var5 < var8 else 0) else ((var17 - var9) + 1))
                break
                var23 = i64_load(var7 + 64)
                if (1 if i64_load(var7 + 64) < 0 else 0):
                    var23 = (0 - var23)
                    i64_store(var7 + 64, (0 - var23))
                    var15 = 1
                    break
                if (var11 & 2048):
                    var15 = 1
                    break
                var15 = (var11 & 1)
                var20 = (2109 if (var11 & 1) else 2107)
                var6 = var17
                if (1 if var23 < 4294967296 else 0):
                    var24 = var23
                    break
                while True:  # loop $label46
                    var6 = (var6 - 1)
                    var24 = ((var23 & 0xFFFFFFFFFFFFFFFF) // 10)
                    i32_store8((var6 - 1), (i32((var23 - (((var23 & 0xFFFFFFFFFFFFFFFF) // 10) * 10))) | 48))
                    var5 = (1 if var23 > 42949672959 else 0)
                    var23 = var24
                    if var5:
                        continue
                    break  # end loop
                var9 = i32(var24)
                if i32(var24):
                    while True:  # loop $label47
                        var6 = (var6 - 1)
                        var5 = ((var9 & 0xFFFFFFFF) // 10)
                        i32_store8((var6 - 1), ((var9 - (((var9 & 0xFFFFFFFF) // 10) * 10)) | 48))
                        var12 = (1 if var9 > 9 else 0)
                        var9 = var5
                        if var12:
                            continue
                        break  # end loop
                var9 = var6
                if (var19 if (1 if var8 < 0 else 0) else 0):
                    break
                var11 = ((var11 & -65537) if var19 else var11)
                var24 = i64_load(var7 + 64)
                if (1 if i64_load(var7 + 64) != 0 else 0):
                    break
                if var8:
                    break
                var9 = var17
                var8 = 0
                break
                var5 = ((1 if var24 == 0 else 0) + (var17 - var9))
                var8 = (var8 if (1 if var5 < var8 else 0) else ((1 if var24 == 0 else 0) + (var17 - var9)))
                break
                var10 = (2147483647 if (1 if var8 >= 2147483647 else 0) else var8)
                var12 = (2147483647 if (1 if var8 >= 2147483647 else 0) else var8)
                var11 = (1 if (2147483647 if (1 if var8 >= 2147483647 else 0) else var8) != 0 else 0)
                var5 = i32_load(var7 + 64)
                var9 = (i32_load(var7 + 64) if var5 else 8568)
                var14 = (i32_load(var7 + 64) if var5 else 8568)
                if (1 if ((i32_load(var7 + 64) if var5 else 8568) & 3) == 0 else 0):
                    break
                if (1 if var12 == 0 else 0):
                    break
                while True:  # loop $label51
                    if (1 if i32_load8_u(var14) == 0 else 0):
                        break
                    var12 = (var12 - 1)
                    var11 = (1 if (var12 - 1) != 0 else 0)
                    var14 = (var14 + 1)
                    if (1 if ((var14 + 1) & 3) == 0 else 0):
                        break
                    if var12:
                        continue
                    break  # end loop
                if (1 if var11 == 0 else 0):
                    break
                if (1 if i32_load8_u(var14) == 0 else 0):
                    break
                if (1 if var12 < 4 else 0):
                    break
                while True:  # loop $label54
                    var5 = i32_load(var14)
                    if (((i32_load(var14) ^ -1) & (var5 - 16843009)) & -2139062144):
                        break
                    var14 = (var14 + 4)
                    var12 = (var12 - 4)
                    if (1 if (var12 - 4) > 3 else 0):
                        continue
                    break  # end loop
                if (1 if var12 == 0 else 0):
                    break
                while True:  # loop $label56
                    if (1 if i32_load8_u(var14) == 0 else 0):
                        break
                    var14 = (var14 + 1)
                    var12 = (var12 - 1)
                    if (var12 - 1):
                        continue
                    break  # end loop
                var5 = 0
                var5 = ((0 - var9) if var5 else var10)
                var10 = (((0 - var9) if var5 else var10) + var9)
                if (1 if var8 >= 0 else 0):
                    var11 = var6
                    var8 = var5
                    break
                var11 = var6
                var8 = var5
                if i32_load8_u(var10):
                    break
                break
                if var8:
                    break
                var5 = 0
                func107(var0, 32, var16, 0, var11)
                break
                i32_store(var7 + 12, 0)
                i64_store32(var7 + 8, i64_load(var7 + 64))
                var5 = (var7 + 8)
                i32_store(var7 + 64, (var7 + 8))
                var8 = -1
                var6 = var5
                var5 = 0
                while True:  # loop $label61
                    var9 = i32_load(var6)
                    if (1 if i32_load(var6) == 0 else 0):
                        break
                    var10 = func278((var7 + 4), var9)
                    var9 = (1 if func278((var7 + 4), var9) < 0 else 0)
                    if (1 if func278((var7 + 4), var9) < 0 else 0):
                        break
                    if (1 if var10 > (var8 - var5) else 0):
                        break
                    var6 = (var6 + 4)
                    var5 = (var5 + var10)
                    if (1 if var8 > (var5 + var10) else 0):
                        continue
                    break
                    break  # end loop
                if var9:
                    break
                var10 = 61
                if (1 if var5 < 0 else 0):
                    break
                func107(var0, 32, var16, var5, var11)
                if (1 if var5 == 0 else 0):
                    var5 = 0
                    break
                var10 = 0
                var6 = i32_load(var7 + 64)
                while True:  # loop $label63
                    var9 = i32_load(var6)
                    if (1 if i32_load(var6) == 0 else 0):
                        break
                    var9 = func278((var7 + 4), var9)
                    var10 = (func278((var7 + 4), var9) + var10)
                    if (1 if (func278((var7 + 4), var9) + var10) > var5 else 0):
                        break
                    var6 = (var6 + 4)
                    if (1 if var5 > var10 else 0):
                        continue
                    break  # end loop
                func107(var0, 32, var16, var5, (var11 ^ 8192))
                var5 = (var16 if (1 if var5 < var16 else 0) else var5)
                continue
                if (var19 if (1 if var8 < 0 else 0) else 0):
                    break
                var10 = 61
                raise RuntimeError('unreachable')
                i64_store8(var7 + 55, i64_load(var7 + 64))
                var8 = 1
                var9 = var21
                var11 = var6
                break
                var6 = i32_load8_u(var5 + 1)
                var5 = (var5 + 1)
                continue
                break  # end loop
            raise RuntimeError('unreachable')
        if var0:
            break
        if (1 if var18 == 0 else 0):
            break
        var5 = 1
        while True:  # loop $label66
            var0 = i32_load((var4 + (var5 << 2)))
            if i32_load((var4 + (var5 << 2))):
                func353((var3 + (var5 << 3)), var0, var2)
                var13 = 1
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != 10 else 0):
                    continue
                break
            break  # end loop
        var13 = 1
        if (1 if var5 >= 10 else 0):
            break
        while True:  # loop $label67
            if i32_load((var4 + (var5 << 2))):
                break
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != 10 else 0):
                continue
            break  # end loop
        break
        var10 = 28
        break
        var12 = (var10 - var9)
        var6 = (var8 if (1 if var8 > var12 else 0) else (var10 - var9))
        if (1 if (var8 if (1 if var8 > var12 else 0) else (var10 - var9)) > (var15 ^ 2147483647) else 0):
            break
        var10 = 61
        var8 = (var6 + var15)
        var5 = (var16 if (1 if var8 < var16 else 0) else (var6 + var15))
        if (1 if (var16 if (1 if var8 < var16 else 0) else (var6 + var15)) > var22 else 0):
            break
        func107(var0, 32, var5, var8, var11)
        func107(var0, 48, var5, var8, (var11 ^ 65536))
        func107(var0, 48, var6, var12, 0)
        func107(var0, 32, var5, var8, (var11 ^ 8192))
        continue
        break  # end loop
    var13 = 0
    break
    var10 = 61
    i32_store((global3 + 28), var10)
    var13 = -1
    global global0
    global0 = (var7 + 80)
    return var13

