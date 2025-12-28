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
# $func298
# ==========================================================
def func298(var0, var1, var2, var3):
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
    var26 = 0
    var27 = 0
    var28 = 0
    var29 = 0
    var30 = 0
    var31 = 0
    var32 = 0
    var33 = 0
    var34 = 0
    var35 = 0
    var36 = 0
    var37 = 0
    var38 = 0
    var39 = 0
    var40 = 0
    var41 = 0
    var42 = 0
    var43 = 0
    var44 = 0
    var45 = 0
    var46 = 0
    var24 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(var24 + 12, var3)
    var29 = var0
    var16 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var26 = i32_load(var24 + 12)
    var33 = var1
    var22 = i32_load(var1)
    if (1 if i32_load(var1) == 0 else 0):
        var22 = 1
        var29 = (var16 + 7)
        break
    i32_store(var33, 0)
    i32_store(var16 + 48, 0)
    i64_store(var16 + 40, 0)
    i32_store(var16 + 12, 0)
    i32_store(var16 + 8, var2)
    var1 = (var16 + 8)
    if (1 if i32_load8_u(7784) != 49 else 0):
        break
    if (1 if var1 == 0 else 0):
        break
    i32_store(var1 + 24, 0)
    var0 = i32_load(var1 + 32)
    if (1 if i32_load(var1 + 32) == 0 else 0):
        i32_store(var1 + 40, 0)
        i32_store(var1 + 32, 417)
        var0 = 417
    if (1 if i32_load(var1 + 36) == 0 else 0):
        i32_store(var1 + 36, 418)
    # call_indirect via table[var0]
    var3 = call_indirect(var0)
    if (1 if call_indirect(var0) == 0 else 0):
        break
    i32_store(var1 + 28, var3)
    i32_store(var3 + 56, 0)
    i32_store(var3, var1)
    i32_store(var3 + 4, 16180)
    var0 = -2
    if (1 if var1 == 0 else 0):
        break
    if (1 if i32_load(var1 + 32) == 0 else 0):
        break
    var12 = i32_load(var1 + 36)
    if (1 if i32_load(var1 + 36) == 0 else 0):
        break
    var2 = i32_load(var1 + 28)
    if (1 if i32_load(var1 + 28) == 0 else 0):
        break
    if (1 if i32_load(var2) != var1 else 0):
        break
    if (1 if (i32_load(var2 + 4) - 16180) > 31 else 0):
        break
    var5 = i32_load(var2 + 56)
    if i32_load(var2 + 56):
        if (1 if i32_load(var2 + 40) != 15 else 0):
            break
    i32_store(var2 + 40, 15)
    i32_store(var2 + 12, 5)
    break
    # call_indirect via table[var12]
    i32_store(var2 + 56, 0)
    var12 = i32_load(var1 + 32)
    i32_store(var2 + 40, 15)
    i32_store(var2 + 12, 5)
    if (1 if var12 == 0 else 0):
        break
    if (1 if i32_load(var1 + 36) == 0 else 0):
        break
    var2 = i32_load(var1 + 28)
    if (1 if i32_load(var1 + 28) == 0 else 0):
        break
    if (1 if i32_load(var2) != var1 else 0):
        break
    if (1 if (i32_load(var2 + 4) - 16180) > 31 else 0):
        break
    var0 = 0
    i32_store(var2 + 52, 0)
    i64_store(var2 + 44, 0)
    i32_store(var2 + 32, 0)
    i32_store(var1 + 8, 0)
    i64_store(var1 + 20, 0)
    var12 = i32_load(var2 + 12)
    if i32_load(var2 + 12):
        i32_store(var1 + 48, (var12 & 1))
    i64_store(var2 + 60, 0)
    i32_store(var2 + 36, 0)
    i32_store(var2 + 24, 32768)
    i64_store(var2 + 16, -4294967296)
    i64_store(var2 + 4, 16180)
    i64_store(var2 + 7108, -4294967295)
    var12 = (var2 + 1332)
    i32_store(var2 + 112, (var2 + 1332))
    i32_store(var2 + 84, var12)
    i32_store(var2 + 80, var12)
    if (1 if var0 == 0 else 0):
        break
    # call_indirect via table[i32_load(var1 + 36)]
    i32_store(var1 + 28, 0)
    if var0:
        break
    i32_store(var16 + 24, 0)
    i32_store(var16 + 20, var29)
    var0 = 0
    while True:  # loop $label185
        if (1 if var0 == 0 else 0):
            i32_store(var16 + 24, var22)
            var22 = 0
        if (1 if i32_load(var16 + 12) == 0 else 0):
            i32_store(var16 + 12, var26)
            var26 = 0
        var12 = 0
        var20 = (global0 - 16)
        global global0
        global0 = (global0 - 16)
        var23 = -2
        var10 = (var16 + 8)
        if (1 if (var16 + 8) == 0 else 0):
            break
        if (1 if i32_load(var10 + 32) == 0 else 0):
            break
        if (1 if i32_load(var10 + 36) == 0 else 0):
            break
        var4 = i32_load(var10 + 28)
        if (1 if i32_load(var10 + 28) == 0 else 0):
            break
        if (1 if i32_load(var4) != var10 else 0):
            break
        var5 = i32_load(var4 + 4)
        if (1 if (i32_load(var4 + 4) - 16180) > 31 else 0):
            break
        var14 = i32_load(var10 + 12)
        if (1 if i32_load(var10 + 12) == 0 else 0):
            break
        var0 = i32_load(var10)
        if (1 if i32_load(var10) == 0 else 0):
            if i32_load(var10 + 4):
                break
        if (1 if var5 == 16191 else 0):
            i32_store(var4 + 4, 16192)
            var5 = 16192
        var39 = (var4 + 92)
        var30 = (var4 + 756)
        var31 = (var4 + 116)
        var34 = (var4 + 88)
        var32 = (var4 + 112)
        var27 = (var4 + 1332)
        var2 = i32_load(var4 + 64)
        var35 = i32_load(var10 + 4)
        var3 = i32_load(var10 + 4)
        var6 = i32_load(var4 + 60)
        var13 = i32_load(var10 + 16)
        var18 = i32_load(var10 + 16)
        while True:  # loop $label52
            var1 = -3
            var8 = 1
            # br_table ['$label8', '$label9', '$label10', '$label11', '$label12', '$label13', '$label14', '$label15', '$label16', '$label17', '$label18', '$label19', '$label19', '$label20', '$label21', '$label22', '$label23', '$label24', '$label25', '$label26', '$label27', '$label28', '$label29', '$label30', '$label31', '$label32', '$label33', '$label34', '$label35', '$label36', '$label37', '$label7']
            _br_idx = (var5 - 16180)
            break  # br_table
            var9 = i32_load(var4 + 76)
            var1 = var0
            var5 = var3
            break
            var8 = i32_load(var4 + 76)
            break
            var5 = i32_load(var4 + 108)
            break
            var5 = i32_load(var4 + 12)
            break
            if (1 if var2 >= 14 else 0):
                break
            if (1 if var3 == 0 else 0):
                break
            var1 = (var2 + 8)
            var5 = (var0 + 1)
            var8 = (var3 - 1)
            var6 = ((i32_load8_u(var0) << var2) + var6)
            if (1 if var2 <= 5 else 0):
                break
            var0 = var5
            var3 = var8
            var2 = var1
            break
            if (1 if var2 >= 32 else 0):
                break
            if (1 if var3 == 0 else 0):
                break
            var1 = (var0 + 1)
            var5 = (var3 - 1)
            var6 = ((i32_load8_u(var0) << var2) + var6)
            if (1 if var2 <= 23 else 0):
                break
            var0 = var1
            var3 = var5
            break
            if (1 if var2 >= 16 else 0):
                break
            if (1 if var3 == 0 else 0):
                break
            var1 = (var2 + 8)
            var5 = (var0 + 1)
            var8 = (var3 - 1)
            var6 = ((i32_load8_u(var0) << var2) + var6)
            if (1 if var2 <= 7 else 0):
                break
            var0 = var5
            var3 = var8
            var2 = var1
            break
            var7 = i32_load(var4 + 12)
            if (1 if i32_load(var4 + 12) == 0 else 0):
                break
            if (1 if var2 >= 16 else 0):
                break
            if (1 if var3 == 0 else 0):
                break
            var1 = (var2 + 8)
            var5 = (var0 + 1)
            var8 = (var3 - 1)
            var6 = ((i32_load8_u(var0) << var2) + var6)
            if (1 if var2 > 7 else 0):
                var0 = var5
                var3 = var8
                var2 = var1
                break
            if (1 if var8 == 0 else 0):
                var0 = var5
                var3 = 0
                var2 = var1
                var1 = var12
                break
            var2 = (var2 + 16)
            var3 = (var3 - 2)
            var6 = ((i32_load8_u(var0 + 1) << var1) + var6)
            var0 = (var0 + 2)
            if (1 if (var7 & 2) == 0 else 0):
                break
            if (1 if var6 != 35615 else 0):
                break
            if (1 if i32_load(var4 + 40) == 0 else 0):
                i32_store(var4 + 40, 15)
            var6 = 0
            var1 = func43(0, 0, 0)
            i32_store(var4 + 28, func43(0, 0, 0))
            i32_store16(var20 + 12, 35615)
            var1 = func43(var1, (var20 + 12), 2)
            i32_store(var4 + 4, 16181)
            i32_store(var4 + 28, var1)
            var2 = 0
            var5 = i32_load(var4 + 4)
            continue
            var1 = i32_load(var4 + 36)
            if i32_load(var4 + 36):
                i32_store(var1 + 48, -1)
            if (var7 & 1):
                if (1 if ((((var6 << 8) & 65280) + ((var6 & 0xFFFFFFFF) >> 8)) % 31) == 0 else 0):
                    break
            i32_store(var10 + 24, 4091)
            i32_store(var4 + 4, 16209)
            var5 = i32_load(var4 + 4)
            continue
            if (1 if (var6 & 15) != 8 else 0):
                i32_store(var10 + 24, 4966)
                i32_store(var4 + 4, 16209)
                var5 = i32_load(var4 + 4)
                continue
            var1 = ((var6 & 0xFFFFFFFF) >> 4)
            var8 = (((var6 & 0xFFFFFFFF) >> 4) & 15)
            var5 = ((((var6 & 0xFFFFFFFF) >> 4) & 15) + 8)
            var7 = i32_load(var4 + 40)
            if i32_load(var4 + 40):
            else:
                i32_store(var4 + 40, var5)
            if (1 if (var7 & (1 if var5 >= var5 else 0)) == 0 else 0):
                var2 = (var2 - 4)
                i32_store(var10 + 24, 4674)
                i32_store(var4 + 4, 16209)
                var6 = var1
                var5 = i32_load(var4 + 4)
                continue
            var2 = 0
            i32_store(var4 + 20, 0)
            i32_store(var4 + 24, (256 << var8))
            var1 = func89(0, 0, 0)
            i32_store(var4 + 28, func89(0, 0, 0))
            i32_store(var10 + 48, var1)
            i32_store(var4 + 4, (16189 if (var6 & 8192) else 16191))
            var6 = 0
            var5 = i32_load(var4 + 4)
            continue
            if (1 if var8 == 0 else 0):
                var0 = var5
                var3 = 0
                var2 = var1
                var1 = var12
                break
            var2 = (var2 + 16)
            var3 = (var3 - 2)
            var6 = ((i32_load8_u(var0 + 1) << var1) + var6)
            var0 = (var0 + 2)
            i32_store(var4 + 20, var6)
            if (1 if (var6 & 255) != 8 else 0):
                i32_store(var10 + 24, 4966)
                i32_store(var4 + 4, 16209)
                var5 = i32_load(var4 + 4)
                continue
            if (var6 & 57344):
                i32_store(var10 + 24, 2847)
                i32_store(var4 + 4, 16209)
                var5 = i32_load(var4 + 4)
                continue
            var1 = i32_load(var4 + 36)
            if i32_load(var4 + 36):
                i32_store(var1, (((var6 & 0xFFFFFFFF) >> 8) & 1))
            if (1 if (var6 & 512) == 0 else 0):
                break
            if (1 if (i32_load8_u(var4 + 12) & 4) == 0 else 0):
                break
            i32_store16(var20 + 12, var6)
            i32_store(var4 + 28, func43(i32_load(var4 + 28), (var20 + 12), 2))
            i32_store(var4 + 4, 16182)
            var2 = 0
            var6 = 0
            break
            if (1 if var2 > 31 else 0):
                break
            if (1 if var3 == 0 else 0):
                break
            var1 = (var0 + 1)
            var5 = (var3 - 1)
            var6 = ((i32_load8_u(var0) << var2) + var6)
            if (1 if var2 > 23 else 0):
                var0 = var1
                var3 = var5
                break
            var8 = (var2 + 8)
            if (1 if var5 == 0 else 0):
                var0 = var1
                var3 = 0
                var2 = var8
                var1 = var12
                break
            var1 = (var0 + 2)
            var5 = (var3 - 2)
            var6 = ((i32_load8_u(var0 + 1) << var8) + var6)
            if (1 if var2 > 15 else 0):
                var0 = var1
                var3 = var5
                break
            var8 = (var2 + 16)
            if (1 if var5 == 0 else 0):
                var0 = var1
                var3 = 0
                var2 = var8
                var1 = var12
                break
            var1 = (var0 + 3)
            var5 = (var3 - 3)
            var6 = ((i32_load8_u(var0 + 2) << var8) + var6)
            if (1 if var2 > 7 else 0):
                var0 = var1
                var3 = var5
                break
            var2 = (var2 + 24)
            if (1 if var5 == 0 else 0):
                var0 = var1
                var3 = 0
                var1 = var12
                break
            var3 = (var3 - 4)
            var6 = ((i32_load8_u(var0 + 3) << var2) + var6)
            var0 = (var0 + 4)
            var1 = i32_load(var4 + 36)
            if i32_load(var4 + 36):
                i32_store(var1 + 4, var6)
            if (1 if (i32_load8_u(var4 + 21) & 2) == 0 else 0):
                break
            if (1 if (i32_load8_u(var4 + 12) & 4) == 0 else 0):
                break
            i32_store(var20 + 12, var6)
            i32_store(var4 + 28, func43(i32_load(var4 + 28), (var20 + 12), 4))
            i32_store(var4 + 4, 16183)
            var2 = 0
            var6 = 0
            break
            if (1 if var2 > 15 else 0):
                break
            if (1 if var3 == 0 else 0):
                break
            var1 = (var0 + 1)
            var5 = (var3 - 1)
            var6 = ((i32_load8_u(var0) << var2) + var6)
            if (1 if var2 > 7 else 0):
                var0 = var1
                var3 = var5
                break
            var2 = (var2 + 8)
            if (1 if var5 == 0 else 0):
                var0 = var1
                var3 = 0
                var1 = var12
                break
            var3 = (var3 - 2)
            var6 = ((i32_load8_u(var0 + 1) << var2) + var6)
            var0 = (var0 + 2)
            var1 = i32_load(var4 + 36)
            if i32_load(var4 + 36):
                i32_store(var1 + 12, ((var6 & 0xFFFFFFFF) >> 8))
                i32_store(var1 + 8, (var6 & 255))
            if (1 if (i32_load8_u(var4 + 21) & 2) == 0 else 0):
                break
            if (1 if (i32_load8_u(var4 + 12) & 4) == 0 else 0):
                break
            i32_store16(var20 + 12, var6)
            i32_store(var4 + 28, func43(i32_load(var4 + 28), (var20 + 12), 2))
            i32_store(var4 + 4, 16184)
            var5 = 0
            var2 = 0
            var6 = 0
            var1 = i32_load(var4 + 20)
            if (i32_load(var4 + 20) & 1024):
                break
            break
            var1 = i32_load(var4 + 20)
            if (1 if (i32_load(var4 + 20) & 1024) == 0 else 0):
                var5 = var2
                break
            var5 = var6
            if (1 if var2 > 15 else 0):
                break
            if (1 if var3 == 0 else 0):
                var3 = 0
                var6 = var5
                var1 = var12
                break
            var8 = (var0 + 1)
            var7 = (var3 - 1)
            var6 = ((i32_load8_u(var0) << var2) + var5)
            if (1 if var2 > 7 else 0):
                var0 = var8
                var3 = var7
                break
            var2 = (var2 + 8)
            if (1 if var7 == 0 else 0):
                var0 = var8
                var3 = 0
                var1 = var12
                break
            var3 = (var3 - 2)
            var6 = ((i32_load8_u(var0 + 1) << var2) + var6)
            var0 = (var0 + 2)
            i32_store(var4 + 68, var6)
            var2 = i32_load(var4 + 36)
            if i32_load(var4 + 36):
                i32_store(var2 + 20, var6)
            var2 = 0
            if (1 if (var1 & 512) == 0 else 0):
                break
            if (1 if (i32_load8_u(var4 + 12) & 4) == 0 else 0):
                break
            i32_store16(var20 + 12, var6)
            i32_store(var4 + 28, func43(i32_load(var4 + 28), (var20 + 12), 2))
            var6 = 0
            break
            var8 = (var2 + 8)
            if (1 if var5 == 0 else 0):
                var0 = var1
                var3 = 0
                var2 = var8
                var1 = var12
                break
            var1 = (var0 + 2)
            var5 = (var3 - 2)
            var6 = ((i32_load8_u(var0 + 1) << var8) + var6)
            if (1 if var2 > 15 else 0):
                var0 = var1
                var3 = var5
                break
            var8 = (var2 + 16)
            if (1 if var5 == 0 else 0):
                var0 = var1
                var3 = 0
                var2 = var8
                var1 = var12
                break
            var1 = (var0 + 3)
            var5 = (var3 - 3)
            var6 = ((i32_load8_u(var0 + 2) << var8) + var6)
            if (1 if var2 > 7 else 0):
                var0 = var1
                var3 = var5
                break
            var2 = (var2 + 24)
            if (1 if var5 == 0 else 0):
                var0 = var1
                var3 = 0
                var1 = var12
                break
            var3 = (var3 - 4)
            var6 = ((i32_load8_u(var0 + 3) << var2) + var6)
            var0 = (var0 + 4)
            var1 = (((var6 << 24) | ((var6 & 65280) << 8)) | ((((var6 & 0xFFFFFFFF) >> 8) & 65280) | ((var6 & 0xFFFFFFFF) >> 24)))
            i32_store(var4 + 28, (((var6 << 24) | ((var6 & 65280) << 8)) | ((((var6 & 0xFFFFFFFF) >> 8) & 65280) | ((var6 & 0xFFFFFFFF) >> 24))))
            i32_store(var10 + 48, var1)
            i32_store(var4 + 4, 16190)
            var6 = 0
            var2 = 0
            if (1 if i32_load(var4 + 16) == 0 else 0):
                i32_store(var10 + 16, var13)
                i32_store(var10 + 12, var14)
                i32_store(var10 + 4, var3)
                i32_store(var10, var0)
                i32_store(var4 + 64, var2)
                i32_store(var4 + 60, var6)
                var23 = 2
                break
            var1 = func89(0, 0, 0)
            i32_store(var4 + 28, func89(0, 0, 0))
            i32_store(var10 + 48, var1)
            i32_store(var4 + 4, 16191)
            if (1 if i32_load(var4 + 8) == 0 else 0):
                if (1 if var2 < 3 else 0):
                    break
                break
            i32_store(var4 + 4, 16206)
            var6 = ((var6 & 0xFFFFFFFF) >> (var2 & 7))
            var2 = (var2 & -8)
            var5 = i32_load(var4 + 4)
            continue
            if (1 if var3 == 0 else 0):
                break
            var3 = (var3 - 1)
            var6 = ((i32_load8_u(var0) << var2) + var6)
            var0 = (var0 + 1)
            var1 = (var2 + 8)
            i32_store(var4 + 8, (var6 & 1))
            var5 = 16193
            # br_table ['$label68', '$label69', '$label70', '$label71']
            _br_idx = ((((var6 & 0xFFFFFFFF) >> 1) & 3) - 1)
            break  # br_table
            i32_store(var4 + 80, 26512)
            i64_store(var4 + 88, 21474836489)
            i32_store(var4 + 84, 28560)
            i32_store(var4 + 4, 16199)
            break
            var5 = 16196
            break
            i32_store(var10 + 24, 4719)
            var5 = 16209
            i32_store(var4 + 4, var5)
            var2 = (var1 - 3)
            var6 = ((var6 & 0xFFFFFFFF) >> 3)
            var5 = i32_load(var4 + 4)
            continue
            var6 = ((var6 & 0xFFFFFFFF) >> (var2 & 7))
            var2 = (var2 & -8)
            if (1 if (var2 & -8) > 31 else 0):
                break
            if (1 if var3 == 0 else 0):
                break
            var1 = (var2 + 8)
            var5 = (var0 + 1)
            var8 = (var3 - 1)
            var6 = ((i32_load8_u(var0) << var2) + var6)
            if (1 if var2 > 23 else 0):
                var0 = var5
                var3 = var8
                var2 = var1
                break
            if (1 if var8 == 0 else 0):
                var0 = var5
                var3 = 0
                var2 = var1
                var1 = var12
                break
            var5 = (var2 + 16)
            var8 = (var0 + 2)
            var7 = (var3 - 2)
            var6 = ((i32_load8_u(var0 + 1) << var1) + var6)
            if (1 if var2 > 15 else 0):
                var0 = var8
                var3 = var7
                var2 = var5
                break
            if (1 if var7 == 0 else 0):
                var0 = var8
                var3 = 0
                var2 = var5
                var1 = var12
                break
            var1 = (var2 + 24)
            var8 = (var0 + 3)
            var7 = (var3 - 3)
            var6 = ((i32_load8_u(var0 + 2) << var5) + var6)
            if var2:
                var0 = var8
                var3 = var7
                var2 = var1
                break
            if (1 if var7 == 0 else 0):
                var0 = var8
                var3 = 0
                var2 = var1
                var1 = var12
                break
            var2 = (var2 + 32)
            var3 = (var3 - 4)
            var6 = ((i32_load8_u(var0 + 3) << var1) + var6)
            var0 = (var0 + 4)
            var1 = (var6 & 65535)
            if (1 if (var6 & 65535) != (((var6 ^ -1) & 0xFFFFFFFF) >> 16) else 0):
                i32_store(var10 + 24, 3310)
                i32_store(var4 + 4, 16209)
                var5 = i32_load(var4 + 4)
                continue
            i32_store(var4 + 4, 16194)
            i32_store(var4 + 68, var1)
            var6 = 0
            var2 = 0
            i32_store(var4 + 4, 16195)
            var1 = i32_load(var4 + 68)
            if i32_load(var4 + 68):
                var1 = (var1 if (1 if var1 < var3 else 0) else var3)
                var1 = ((var1 if (1 if var1 < var3 else 0) else var3) if (1 if var1 < var13 else 0) else var13)
                if (1 if ((var1 if (1 if var1 < var3 else 0) else var3) if (1 if var1 < var13 else 0) else var13) == 0 else 0):
                    break
                var5 = func35(var14, var0, var1)
                i32_store(var4 + 68, (i32_load(var4 + 68) - var1))
                var14 = (var1 + var5)
                var13 = (var13 - var1)
                var0 = (var0 + var1)
                var3 = (var3 - var1)
                var5 = i32_load(var4 + 4)
                continue
            i32_store(var4 + 4, 16191)
            var5 = i32_load(var4 + 4)
            continue
            if (1 if var8 == 0 else 0):
                var0 = var5
                var3 = 0
                var2 = var1
                var1 = var12
                break
            var2 = (var2 + 16)
            var3 = (var3 - 2)
            var6 = ((i32_load8_u(var0 + 1) << var1) + var6)
            var0 = (var0 + 2)
            var1 = (var6 & 31)
            i32_store(var4 + 100, ((var6 & 31) + 257))
            var5 = (((var6 & 0xFFFFFFFF) >> 5) & 31)
            i32_store(var4 + 104, ((((var6 & 0xFFFFFFFF) >> 5) & 31) + 1))
            var7 = ((((var6 & 0xFFFFFFFF) >> 10) & 15) + 4)
            i32_store(var4 + 96, ((((var6 & 0xFFFFFFFF) >> 10) & 15) + 4))
            var2 = (var2 - 14)
            var6 = ((var6 & 0xFFFFFFFF) >> 14)
            if (1 if ((1 if var5 < 30 else 0) & (1 if var1 <= 29 else 0)) == 0 else 0):
                i32_store(var10 + 24, 3236)
                i32_store(var4 + 4, 16209)
                var5 = i32_load(var4 + 4)
                continue
            i32_store(var4 + 4, 16197)
            var5 = 0
            i32_store(var4 + 108, 0)
            break
            var5 = i32_load(var4 + 108)
            var7 = i32_load(var4 + 96)
            if (1 if i32_load(var4 + 108) < i32_load(var4 + 96) else 0):
                break
            break
            if (1 if var13 == 0 else 0):
                break
            i32_store8(var14, i32_load(var4 + 68))
            i32_store(var4 + 4, 16200)
            var13 = (var13 - 1)
            var14 = (var14 + 1)
            var5 = i32_load(var4 + 4)
            continue
            var5 = i32_load(var4 + 12)
            if (1 if i32_load(var4 + 12) == 0 else 0):
                var5 = 0
                break
            if (1 if var2 > 31 else 0):
                var8 = var0
                break
            if (1 if var3 == 0 else 0):
                break
            var1 = (var2 + 8)
            var8 = (var0 + 1)
            var7 = (var3 - 1)
            var6 = ((i32_load8_u(var0) << var2) + var6)
            if (1 if var2 > 23 else 0):
                var3 = var7
                var2 = var1
                break
            if (1 if var7 == 0 else 0):
                var0 = var8
                var3 = 0
                var2 = var1
                var1 = var12
                break
            var7 = (var2 + 16)
            var8 = (var0 + 2)
            var9 = (var3 - 2)
            var6 = ((i32_load8_u(var0 + 1) << var1) + var6)
            if (1 if var2 > 15 else 0):
                var3 = var9
                var2 = var7
                break
            if (1 if var9 == 0 else 0):
                var0 = var8
                var3 = 0
                var2 = var7
                var1 = var12
                break
            var1 = (var2 + 24)
            var8 = (var0 + 3)
            var9 = (var3 - 3)
            var6 = ((i32_load8_u(var0 + 2) << var7) + var6)
            if (1 if var2 > 7 else 0):
                var3 = var9
                var2 = var1
                break
            if (1 if var9 == 0 else 0):
                var0 = var8
                var3 = 0
                var2 = var1
                var1 = var12
                break
            var2 = (var2 + 32)
            var8 = (var0 + 4)
            var3 = (var3 - 4)
            var6 = ((i32_load8_u(var0 + 3) << var1) + var6)
            var0 = (var18 - var13)
            i32_store(var10 + 20, ((var18 - var13) + i32_load(var10 + 20)))
            i32_store(var4 + 32, (i32_load(var4 + 32) + var0))
            var1 = (var5 & 4)
            if (1 if (var5 & 4) == 0 else 0):
                break
            if (1 if var13 == var18 else 0):
                break
            var1 = (var14 - var0)
            var5 = i32_load(var4 + 28)
            if i32_load(var4 + 20):
                break
            var0 = func89(var5, var1, var0)
            i32_store(func43(var5, var1, var0) + 28, func89(var5, var1, var0))
            i32_store(var10 + 48, var0)
            var5 = i32_load(var4 + 12)
            var1 = (i32_load(var4 + 12) & 4)
            if (1 if var1 == 0 else 0):
                break
            if (1 if i32_load(var4 + 28) == (var6 if i32_load(var4 + 20) else (((var6 << 24) | ((var6 & 65280) << 8)) | ((((var6 & 0xFFFFFFFF) >> 8) & 65280) | ((var6 & 0xFFFFFFFF) >> 24)))) else 0):
                break
            i32_store(var10 + 24, 4137)
            i32_store(var4 + 4, 16209)
            var0 = var8
            var18 = var13
            var5 = i32_load(var4 + 4)
            continue
            i32_store(var4 + 4, 16192)
            break
            var0 = var8
            var6 = 0
            var2 = 0
            var18 = var13
            i32_store(var4 + 4, 16207)
            break
            while True:  # loop $label84
                if (1 if var2 <= 2 else 0):
                    if (1 if var3 == 0 else 0):
                        break
                    var3 = (var3 - 1)
                    var6 = ((i32_load8_u(var0) << var2) + var6)
                    var2 = (var2 + 8)
                    var0 = (var0 + 1)
                var1 = (var5 + 1)
                i32_store(var4 + 108, (var5 + 1))
                i32_store16((var4 + (i32_load16_u(((var5 << 1) + 26464)) << 1)) + 116, (var6 & 7))
                var2 = (var2 - 3)
                var6 = ((var6 & 0xFFFFFFFF) >> 3)
                var5 = var1
                if (1 if var1 != var7 else 0):
                    continue
                break  # end loop
            var5 = var7
            if (1 if var5 <= 18 else 0):
                var8 = 0
                var1 = var5
                var12 = ((3 - var5) & 3)
                if ((3 - var5) & 3):
                    while True:  # loop $label85
                        i32_store16((var4 + (i32_load16_u(((var1 << 1) + 26464)) << 1)) + 116, 0)
                        var1 = (var1 + 1)
                        var8 = (var8 + 1)
                        if (1 if (var8 + 1) != var12 else 0):
                            continue
                        break  # end loop
                if (1 if (var5 - 16) >= 3 else 0):
                    while True:  # loop $label86
                        var12 = (var4 + 116)
                        var5 = (var1 << 1)
                        i32_store16(((var4 + 116) + (i32_load16_u(((var1 << 1) + 26464)) << 1)), 0)
                        i32_store16((var12 + (i32_load16_u((var5 + 26466)) << 1)), 0)
                        i32_store16((var12 + (i32_load16_u((var5 + 26468)) << 1)), 0)
                        i32_store16((var12 + (i32_load16_u((var5 + 26470)) << 1)), 0)
                        var1 = (var1 + 4)
                        if (1 if (var1 + 4) != 19 else 0):
                            continue
                        break  # end loop
                i32_store(var4 + 108, 19)
            i32_store(var4 + 88, 7)
            i32_store(var4 + 80, var27)
            i32_store(var4 + 112, var27)
            var5 = 0
            var12 = func241(0, var31, 19, var32, var34, var30)
            if func241(0, var31, 19, var32, var34, var30):
                i32_store(var10 + 24, 2822)
                i32_store(var4 + 4, 16209)
                var5 = i32_load(var4 + 4)
                continue
            i32_store(var4 + 4, 16198)
            i32_store(var4 + 108, 0)
            var12 = 0
            var28 = i32_load(var4 + 100)
            var19 = (i32_load(var4 + 100) + i32_load(var4 + 104))
            if (1 if (i32_load(var4 + 100) + i32_load(var4 + 104)) > var5 else 0):
                var21 = ((-1 << i32_load(var4 + 88)) ^ -1)
                var17 = i32_load(var4 + 80)
                while True:  # loop $label103
                    var9 = var2
                    var8 = var3
                    var7 = var0
                    var15 = (var6 & var21)
                    var11 = i32_load8_u((var17 + ((var6 & var21) << 2)) + 1)
                    if (1 if i32_load8_u((var17 + ((var6 & var21) << 2)) + 1) <= var2 else 0):
                        var1 = var2
                        break
                    while True:  # loop $label89
                        if (1 if var8 == 0 else 0):
                            break
                        var11 = (i32_load8_u(var7) << var9)
                        var7 = (var7 + 1)
                        var8 = (var8 - 1)
                        var1 = (var9 + 8)
                        var9 = (var9 + 8)
                        var6 = (var6 + var11)
                        var15 = ((var6 + var11) & var21)
                        var11 = i32_load8_u((var17 + (((var6 + var11) & var21) << 2)) + 1)
                        if (1 if var1 < i32_load8_u((var17 + (((var6 + var11) & var21) << 2)) + 1) else 0):
                            continue
                        break  # end loop
                    var0 = var7
                    var3 = var8
                    var2 = i32_load16_u((var17 + (var15 << 2)) + 2)
                    if (1 if i32_load16_u((var17 + (var15 << 2)) + 2) <= 15 else 0):
                        var8 = (var5 + 1)
                        i32_store(var4 + 108, (var5 + 1))
                        i32_store16((var4 + (var5 << 1)) + 116, var2)
                        var2 = (var1 - var11)
                        var6 = ((var6 & 0xFFFFFFFF) >> var11)
                        var5 = var8
                        break
                    # br_table ['$label91', '$label92', '$label93']
                    _br_idx = (var2 - 16)
                    break  # br_table
                    var2 = (var11 + 2)
                    if (1 if (var11 + 2) > var1 else 0):
                        while True:  # loop $label95
                            if (1 if var3 == 0 else 0):
                                break
                            var3 = (var3 - 1)
                            var6 = ((i32_load8_u(var0) << var1) + var6)
                            var0 = (var0 + 1)
                            var1 = (var1 + 8)
                            if (1 if (var1 + 8) < var2 else 0):
                                continue
                            break  # end loop
                    var2 = (var1 - var11)
                    var1 = ((var6 & 0xFFFFFFFF) >> var11)
                    if (1 if var5 == 0 else 0):
                        i32_store(var10 + 24, 2894)
                        i32_store(var4 + 4, 16209)
                        var6 = var1
                        var5 = i32_load(var4 + 4)
                        continue
                    var2 = (var2 - 2)
                    var6 = ((var1 & 0xFFFFFFFF) >> 2)
                    var8 = ((var1 & 3) + 3)
                    break
                    var2 = (var11 + 3)
                    if (1 if (var11 + 3) > var1 else 0):
                        while True:  # loop $label97
                            if (1 if var3 == 0 else 0):
                                break
                            var3 = (var3 - 1)
                            var6 = ((i32_load8_u(var0) << var1) + var6)
                            var0 = (var0 + 1)
                            var1 = (var1 + 8)
                            if (1 if (var1 + 8) < var2 else 0):
                                continue
                            break  # end loop
                    var2 = ((var1 - var11) - 3)
                    var1 = ((var6 & 0xFFFFFFFF) >> var11)
                    var6 = ((((var6 & 0xFFFFFFFF) >> var11) & 0xFFFFFFFF) >> 3)
                    break
                    var2 = (var11 + 7)
                    if (1 if (var11 + 7) > var1 else 0):
                        while True:  # loop $label99
                            if (1 if var3 == 0 else 0):
                                break
                            var3 = (var3 - 1)
                            var6 = ((i32_load8_u(var0) << var1) + var6)
                            var0 = (var0 + 1)
                            var1 = (var1 + 8)
                            if (1 if (var1 + 8) < var2 else 0):
                                continue
                            break  # end loop
                    var2 = ((var1 - var11) - 7)
                    var1 = ((var6 & 0xFFFFFFFF) >> var11)
                    var6 = ((((var6 & 0xFFFFFFFF) >> var11) & 0xFFFFFFFF) >> 7)
                    var8 = ((var1 & 127) + 11)
                    var1 = 0
                    if (1 if (var5 + var8) > var19 else 0):
                        break
                    var9 = (var8 - 1)
                    var7 = 0
                    var11 = (var8 & 3)
                    if (var8 & 3):
                        while True:  # loop $label101
                            i32_store16((var4 + (var5 << 1)) + 116, var1)
                            var5 = (var5 + 1)
                            var8 = (var8 - 1)
                            var7 = (var7 + 1)
                            if (1 if (var7 + 1) != var11 else 0):
                                continue
                            break  # end loop
                    if (1 if var9 >= 3 else 0):
                        while True:  # loop $label102
                            var7 = (var4 + (var5 << 1))
                            i32_store16((var4 + (var5 << 1)) + 118, var1)
                            i32_store16(var7 + 116, var1)
                            i32_store16(var7 + 120, var1)
                            i32_store16(var7 + 122, var1)
                            var5 = (var5 + 4)
                            var8 = (var8 - 4)
                            if (var8 - 4):
                                continue
                            break  # end loop
                    i32_store(var4 + 108, var5)
                    if (1 if var5 < var19 else 0):
                        continue
                    break  # end loop
            if (1 if i32_load16_u(var4 + 628) == 0 else 0):
                i32_store(var10 + 24, 4054)
                i32_store(var4 + 4, 16209)
                var5 = i32_load(var4 + 4)
                continue
            i32_store(var4 + 88, 9)
            i32_store(var4 + 80, var27)
            i32_store(var4 + 112, var27)
            var12 = func241(1, var31, var28, var32, var34, var30)
            if func241(1, var31, var28, var32, var34, var30):
                i32_store(var10 + 24, 2794)
                i32_store(var4 + 4, 16209)
                var5 = i32_load(var4 + 4)
                continue
            i32_store(var4 + 92, 6)
            i32_store(var4 + 84, i32_load(var4 + 112))
            var12 = func241(2, (var31 + (i32_load(var4 + 100) << 1)), i32_load(var4 + 104), var32, var39, var30)
            if func241(2, (var31 + (i32_load(var4 + 100) << 1)), i32_load(var4 + 104), var32, var39, var30):
                i32_store(var10 + 24, 2872)
                i32_store(var4 + 4, 16209)
                var5 = i32_load(var4 + 4)
                continue
            i32_store(var4 + 4, 16199)
            var12 = 0
            i32_store(var4 + 4, 16200)
            if (1 if var3 < 6 else 0):
                break
            if (1 if var13 < 258 else 0):
                break
            i32_store(var10 + 16, var13)
            i32_store(var10 + 12, var14)
            i32_store(var10 + 4, var3)
            i32_store(var10, var0)
            i32_store(var4 + 64, var2)
            i32_store(var4 + 60, var6)
            var1 = i32_load(var10 + 16)
            var7 = i32_load(var10 + 12)
            var0 = (i32_load(var10 + 16) + i32_load(var10 + 12))
            var19 = ((i32_load(var10 + 16) + i32_load(var10 + 12)) + (var18 ^ -1))
            var14 = i32_load(var10 + 28)
            var9 = i32_load(i32_load(var10 + 28) + 52)
            var40 = ((var0 + (i32_load(i32_load(var10 + 28) + 52) ^ -1)) - var18)
            var21 = (var9 & 7)
            var41 = i32_load(var14 + 44)
            var42 = (var9 + i32_load(var14 + 44))
            var28 = (var0 - 257)
            var43 = (var7 + (var1 - var18))
            var2 = i32_load(var10)
            var36 = ((i32_load(var10) + i32_load(var10 + 4)) - 5)
            var44 = ((-1 << i32_load(var14 + 92)) ^ -1)
            var45 = ((-1 << i32_load(var14 + 88)) ^ -1)
            var37 = i32_load(var14 + 84)
            var38 = i32_load(var14 + 80)
            var6 = i32_load(var14 + 64)
            var11 = i32_load(var14 + 60)
            var8 = i32_load(var14 + 56)
            var46 = i32_load(var14 + 48)
            while True:  # loop $label131
                if (1 if var6 <= 14 else 0):
                    var11 = (((i32_load8_u(var2) << var6) + var11) + (i32_load8_u(var2 + 1) << (var6 + 8)))
                    var6 = (var6 + 16)
                    var2 = (var2 + 2)
                var3 = (var38 + ((var11 & var45) << 2))
                var0 = i32_load8_u((var38 + ((var11 & var45) << 2)) + 1)
                var6 = (var6 - i32_load8_u((var38 + ((var11 & var45) << 2)) + 1))
                var11 = ((var11 & 0xFFFFFFFF) >> var0)
                while True:  # loop $label111
                    var0 = i32_load8_u(var3)
                    if (1 if i32_load8_u(var3) == 0 else 0):
                        i32_store8(var7, i32_load8_u(var3 + 2))
                        var7 = (var7 + 1)
                        break
                    if (var0 & 16):
                        var13 = i32_load16_u(var3 + 2)
                        var0 = (var0 & 15)
                        if (1 if (var0 & 15) == 0 else 0):
                            var1 = var2
                            break
                        if (1 if var0 <= var6 else 0):
                            var1 = var2
                            break
                        var1 = (var2 + 1)
                        var11 = ((i32_load8_u(var2) << var6) + var11)
                        var6 = ((var6 + 8) - var0)
                        var13 = ((var11 & ((-1 << var0) ^ -1)) + var13)
                        var0 = ((var11 & 0xFFFFFFFF) >> var0)
                        if (1 if var6 <= 14 else 0):
                            var0 = (((i32_load8_u(var1) << var6) + var0) + (i32_load8_u(var1 + 1) << (var6 + 8)))
                            var6 = (var6 + 16)
                            var1 = (var1 + 2)
                        var3 = (var37 + ((var0 & var44) << 2))
                        var2 = i32_load8_u((var37 + ((var0 & var44) << 2)) + 1)
                        var6 = (var6 - i32_load8_u((var37 + ((var0 & var44) << 2)) + 1))
                        var11 = ((var0 & 0xFFFFFFFF) >> var2)
                        var0 = i32_load8_u(var3)
                        if (i32_load8_u(var3) & 16):
                            break
                        while True:  # loop $label109
                            if (1 if (var0 & 64) == 0 else 0):
                                var3 = ((var37 + (i32_load16_u(var3 + 2) << 2)) + ((var11 & ((-1 << var0) ^ -1)) << 2))
                                var0 = i32_load8_u(((var37 + (i32_load16_u(var3 + 2) << 2)) + ((var11 & ((-1 << var0) ^ -1)) << 2)) + 1)
                                var6 = (var6 - i32_load8_u(((var37 + (i32_load16_u(var3 + 2) << 2)) + ((var11 & ((-1 << var0) ^ -1)) << 2)) + 1))
                                var11 = ((var11 & 0xFFFFFFFF) >> var0)
                                var0 = i32_load8_u(var3)
                                if (1 if (i32_load8_u(var3) & 16) == 0 else 0):
                                    continue
                                break
                            break  # end loop
                        var13 = 4865
                        var2 = var1
                        break
                    if (1 if (var0 & 64) == 0 else 0):
                        var3 = ((var38 + (i32_load16_u(var3 + 2) << 2)) + ((var11 & ((-1 << var0) ^ -1)) << 2))
                        var0 = i32_load8_u(((var38 + (i32_load16_u(var3 + 2) << 2)) + ((var11 & ((-1 << var0) ^ -1)) << 2)) + 1)
                        var6 = (var6 - i32_load8_u(((var38 + (i32_load16_u(var3 + 2) << 2)) + ((var11 & ((-1 << var0) ^ -1)) << 2)) + 1))
                        var11 = ((var11 & 0xFFFFFFFF) >> var0)
                        continue
                    break  # end loop
                var13 = 4837
                if (var0 & 32):
                    break
                break
                var15 = i32_load16_u(var3 + 2)
                var3 = (var0 & 15)
                if (1 if (var0 & 15) <= var6 else 0):
                    var0 = var6
                    break
                var11 = ((i32_load8_u(var1) << var6) + var11)
                var0 = (var6 + 8)
                if (1 if var3 <= (var6 + 8) else 0):
                    break
                var11 = ((i32_load8_u(var1 + 1) << var0) + var11)
                var0 = (var6 + 16)
                var2 = (var1 + 2)
                var1 = (var11 & ((-1 << var3) ^ -1))
                var6 = (var0 - var3)
                var11 = ((var11 & 0xFFFFFFFF) >> var3)
                var17 = (var1 + var15)
                var0 = (var7 - var43)
                if (1 if (var1 + var15) > (var7 - var43) else 0):
                    var5 = (var17 - var0)
                    if (1 if (var17 - var0) <= var46 else 0):
                        break
                    if (1 if i32_load(var14 + 7108) == 0 else 0):
                        break
                    var13 = 4158
                    break
                    if (1 if var9 == 0 else 0):
                        var3 = (var8 + (var41 - var5))
                        if (1 if var5 >= var13 else 0):
                            break
                        var15 = (((var1 + var19) + var15) - var7)
                        var1 = 0
                        var0 = var5
                        var25 = (var5 & 7)
                        if (var5 & 7):
                            while True:  # loop $label116
                                i32_store8(var7, i32_load8_u(var3))
                                var0 = (var0 - 1)
                                var7 = (var7 + 1)
                                var3 = (var3 + 1)
                                var1 = (var1 + 1)
                                if (1 if (var1 + 1) != var25 else 0):
                                    continue
                                break  # end loop
                        if (1 if var15 < 7 else 0):
                            break
                        while True:  # loop $label118
                            i32_store8(var7, i32_load8_u(var3))
                            i32_store8(var7 + 1, i32_load8_u(var3 + 1))
                            i32_store8(var7 + 2, i32_load8_u(var3 + 2))
                            i32_store8(var7 + 3, i32_load8_u(var3 + 3))
                            i32_store8(var7 + 4, i32_load8_u(var3 + 4))
                            i32_store8(var7 + 5, i32_load8_u(var3 + 5))
                            i32_store8(var7 + 6, i32_load8_u(var3 + 6))
                            i32_store8(var7 + 7, i32_load8_u(var3 + 7))
                            var7 = (var7 + 8)
                            var3 = (var3 + 8)
                            var0 = (var0 - 8)
                            if (var0 - 8):
                                continue
                            break  # end loop
                        break
                    if (1 if var5 > var9 else 0):
                        var3 = (var8 + (var42 - var5))
                        var5 = (var5 - var9)
                        if (1 if var13 <= (var5 - var9) else 0):
                            break
                        var15 = (((var1 + var40) + var15) - var7)
                        var1 = 0
                        var0 = var5
                        var25 = (var5 & 7)
                        if (var5 & 7):
                            while True:  # loop $label119
                                i32_store8(var7, i32_load8_u(var3))
                                var0 = (var0 - 1)
                                var7 = (var7 + 1)
                                var3 = (var3 + 1)
                                var1 = (var1 + 1)
                                if (1 if (var1 + 1) != var25 else 0):
                                    continue
                                break  # end loop
                        if (1 if var15 >= 7 else 0):
                            while True:  # loop $label120
                                i32_store8(var7, i32_load8_u(var3))
                                i32_store8(var7 + 1, i32_load8_u(var3 + 1))
                                i32_store8(var7 + 2, i32_load8_u(var3 + 2))
                                i32_store8(var7 + 3, i32_load8_u(var3 + 3))
                                i32_store8(var7 + 4, i32_load8_u(var3 + 4))
                                i32_store8(var7 + 5, i32_load8_u(var3 + 5))
                                i32_store8(var7 + 6, i32_load8_u(var3 + 6))
                                i32_store8(var7 + 7, i32_load8_u(var3 + 7))
                                var7 = (var7 + 8)
                                var3 = (var3 + 8)
                                var0 = (var0 - 8)
                                if (var0 - 8):
                                    continue
                                break  # end loop
                        var13 = (var13 - var5)
                        if (1 if var9 >= (var13 - var5) else 0):
                            var3 = var8
                            break
                        var1 = 0
                        var0 = var9
                        var3 = var8
                        if var21:
                            while True:  # loop $label121
                                i32_store8(var7, i32_load8_u(var3))
                                var0 = (var0 - 1)
                                var7 = (var7 + 1)
                                var3 = (var3 + 1)
                                var1 = (var1 + 1)
                                if (1 if (var1 + 1) != var21 else 0):
                                    continue
                                break  # end loop
                        if (1 if var9 >= 8 else 0):
                            while True:  # loop $label122
                                i32_store8(var7, i32_load8_u(var3))
                                i32_store8(var7 + 1, i32_load8_u(var3 + 1))
                                i32_store8(var7 + 2, i32_load8_u(var3 + 2))
                                i32_store8(var7 + 3, i32_load8_u(var3 + 3))
                                i32_store8(var7 + 4, i32_load8_u(var3 + 4))
                                i32_store8(var7 + 5, i32_load8_u(var3 + 5))
                                i32_store8(var7 + 6, i32_load8_u(var3 + 6))
                                i32_store8(var7 + 7, i32_load8_u(var3 + 7))
                                var7 = (var7 + 8)
                                var3 = (var3 + 8)
                                var0 = (var0 - 8)
                                if (var0 - 8):
                                    continue
                                break  # end loop
                        var3 = (var7 - var17)
                        var13 = (var13 - var9)
                        break
                    var3 = (var8 + (var9 - var5))
                    if (1 if var5 >= var13 else 0):
                        break
                    var15 = (((var1 + var19) + var15) - var7)
                    var1 = 0
                    var0 = var5
                    var25 = (var5 & 7)
                    if (var5 & 7):
                        while True:  # loop $label123
                            i32_store8(var7, i32_load8_u(var3))
                            var0 = (var0 - 1)
                            var7 = (var7 + 1)
                            var3 = (var3 + 1)
                            var1 = (var1 + 1)
                            if (1 if (var1 + 1) != var25 else 0):
                                continue
                            break  # end loop
                    if (1 if var15 < 7 else 0):
                        break
                    while True:  # loop $label124
                        i32_store8(var7, i32_load8_u(var3))
                        i32_store8(var7 + 1, i32_load8_u(var3 + 1))
                        i32_store8(var7 + 2, i32_load8_u(var3 + 2))
                        i32_store8(var7 + 3, i32_load8_u(var3 + 3))
                        i32_store8(var7 + 4, i32_load8_u(var3 + 4))
                        i32_store8(var7 + 5, i32_load8_u(var3 + 5))
                        i32_store8(var7 + 6, i32_load8_u(var3 + 6))
                        i32_store8(var7 + 7, i32_load8_u(var3 + 7))
                        var7 = (var7 + 8)
                        var3 = (var3 + 8)
                        var0 = (var0 - 8)
                        if (var0 - 8):
                            continue
                        break  # end loop
                    var3 = (var7 - var17)
                    var13 = (var13 - var5)
                    if (1 if var13 < 3 else 0):
                        break
                    var0 = 0
                    var1 = (var13 - 3)
                    var5 = (((((var13 - 3) & 0xFFFFFFFF) // 3) + 1) & 3)
                    if (((((var13 - 3) & 0xFFFFFFFF) // 3) + 1) & 3):
                        while True:  # loop $label126
                            i32_store8(var7, i32_load8_u(var3))
                            i32_store8(var7 + 1, i32_load8_u(var3 + 1))
                            i32_store8(var7 + 2, i32_load8_u(var3 + 2))
                            var13 = (var13 - 3)
                            var7 = (var7 + 3)
                            var3 = (var3 + 3)
                            var0 = (var0 + 1)
                            if (1 if (var0 + 1) != var5 else 0):
                                continue
                            break  # end loop
                    if (1 if var1 < 9 else 0):
                        break
                    while True:  # loop $label127
                        i32_store8(var7, i32_load8_u(var3))
                        i32_store8(var7 + 1, i32_load8_u(var3 + 1))
                        i32_store8(var7 + 2, i32_load8_u(var3 + 2))
                        i32_store8(var7 + 3, i32_load8_u(var3 + 3))
                        i32_store8(var7 + 4, i32_load8_u(var3 + 4))
                        i32_store8(var7 + 5, i32_load8_u(var3 + 5))
                        i32_store8(var7 + 6, i32_load8_u(var3 + 6))
                        i32_store8(var7 + 7, i32_load8_u(var3 + 7))
                        i32_store8(var7 + 8, i32_load8_u(var3 + 8))
                        i32_store8(var7 + 9, i32_load8_u(var3 + 9))
                        i32_store8(var7 + 10, i32_load8_u(var3 + 10))
                        i32_store8(var7 + 11, i32_load8_u(var3 + 11))
                        var7 = (var7 + 12)
                        var3 = (var3 + 12)
                        var13 = (var13 - 12)
                        if (1 if (var13 - 12) > 2 else 0):
                            continue
                        break  # end loop
                    if (1 if var13 == 0 else 0):
                        break
                    i32_store8(var7, i32_load8_u(var3))
                    if (1 if var13 != 1 else 0):
                        break
                    var7 = (var7 + 1)
                    break
                var1 = (var7 - var17)
                while True:  # loop $label129
                    var0 = var7
                    var3 = var1
                    i32_store8(var7, i32_load8_u(var1))
                    i32_store8(var0 + 1, i32_load8_u(var1 + 1))
                    i32_store8(var0 + 2, i32_load8_u(var1 + 2))
                    var7 = (var0 + 3)
                    var1 = (var1 + 3)
                    var13 = (var13 - 3)
                    if (1 if (var13 - 3) > 2 else 0):
                        continue
                    break  # end loop
                if (1 if var13 == 0 else 0):
                    break
                i32_store8(var0 + 3, i32_load8_u(var1))
                if (1 if var13 == 1 else 0):
                    var7 = (var0 + 4)
                    break
                i32_store8(var0 + 4, i32_load8_u(var3 + 4))
                var7 = (var0 + 5)
                break
                i32_store8(var7 + 1, i32_load8_u(var3 + 1))
                var7 = (var7 + 2)
                if (1 if var2 >= var36 else 0):
                    break
                if (1 if var7 < var28 else 0):
                    continue
                break
                break  # end loop
            i32_store(var10 + 24, var13)
            i32_store(var1 + 4, 16209)
            i32_store(var10 + 12, var7)
            var0 = (var2 - ((var6 & 0xFFFFFFFF) >> 3))
            i32_store(var10, (var2 - ((var6 & 0xFFFFFFFF) >> 3)))
            i32_store(var10 + 16, ((var28 - var7) + 257))
            i32_store(var10 + 4, ((var36 - var0) + 5))
            var0 = (var6 & 7)
            i32_store(var14 + 64, (var6 & 7))
            i32_store(var14 + 60, (var11 & ((-1 << var0) ^ -1)))
            var2 = i32_load(var4 + 64)
            var6 = i32_load(var4 + 60)
            var3 = i32_load(var10 + 4)
            var0 = i32_load(var10)
            var13 = i32_load(var10 + 16)
            var14 = i32_load(var10 + 12)
            if (1 if i32_load(var4 + 4) != 16191 else 0):
                break
            i32_store(var4 + 7112, -1)
            var5 = i32_load(var4 + 4)
            continue
            i32_store(var4 + 7112, 0)
            var8 = var2
            var5 = var3
            var1 = var0
            var19 = i32_load(var4 + 80)
            var15 = ((-1 << i32_load(var4 + 88)) ^ -1)
            var11 = (i32_load(var4 + 80) + ((var6 & ((-1 << i32_load(var4 + 88)) ^ -1)) << 2))
            var9 = i32_load8_u((i32_load(var4 + 80) + ((var6 & ((-1 << i32_load(var4 + 88)) ^ -1)) << 2)) + 1)
            if (1 if i32_load8_u((i32_load(var4 + 80) + ((var6 & ((-1 << i32_load(var4 + 88)) ^ -1)) << 2)) + 1) <= var2 else 0):
                var7 = var2
                break
            while True:  # loop $label134
                if (1 if var5 == 0 else 0):
                    break
                var9 = (i32_load8_u(var1) << var8)
                var1 = (var1 + 1)
                var5 = (var5 - 1)
                var7 = (var8 + 8)
                var8 = (var8 + 8)
                var6 = (var6 + var9)
                var11 = (var19 + (((var6 + var9) & var15) << 2))
                var9 = i32_load8_u((var19 + (((var6 + var9) & var15) << 2)) + 1)
                if (1 if var7 < i32_load8_u((var19 + (((var6 + var9) & var15) << 2)) + 1) else 0):
                    continue
                break  # end loop
            var15 = i32_load16_u(var11 + 2)
            var8 = i32_load8_u(var11)
            if (1 if ((i32_load8_u(var11) - 1) & 255) > 14 else 0):
                var11 = var9
                var9 = 0
                var0 = var1
                var3 = var5
                break
            var3 = var5
            var0 = var1
            var2 = var7
            var21 = ((-1 << (var8 + var9)) ^ -1)
            var17 = (var19 + (((((var6 & ((-1 << (var8 + var9)) ^ -1)) & 0xFFFFFFFF) >> var9) + var15) << 2))
            var11 = i32_load8_u((var19 + (((((var6 & ((-1 << (var8 + var9)) ^ -1)) & 0xFFFFFFFF) >> var9) + var15) << 2)) + 1)
            if (1 if var7 >= (var9 + i32_load8_u((var19 + (((((var6 & ((-1 << (var8 + var9)) ^ -1)) & 0xFFFFFFFF) >> var9) + var15) << 2)) + 1)) else 0):
                var8 = var7
                break
            while True:  # loop $label138
                if (1 if var3 == 0 else 0):
                    break
                var11 = (i32_load8_u(var0) << var2)
                var0 = (var0 + 1)
                var3 = (var3 - 1)
                var8 = (var2 + 8)
                var2 = (var2 + 8)
                var6 = (var6 + var11)
                var17 = (var19 + ((((((var6 + var11) & var21) & 0xFFFFFFFF) >> var9) + var15) << 2))
                var11 = i32_load8_u((var19 + ((((((var6 + var11) & var21) & 0xFFFFFFFF) >> var9) + var15) << 2)) + 1)
                if (1 if (var9 + i32_load8_u((var19 + ((((((var6 + var11) & var21) & 0xFFFFFFFF) >> var9) + var15) << 2)) + 1)) > var8 else 0):
                    continue
                break  # end loop
            var7 = (var8 - var9)
            var6 = ((var6 & 0xFFFFFFFF) >> var9)
            var8 = i32_load8_u(var17)
            var15 = i32_load16_u(var17 + 2)
            i32_store(var4 + 68, (var15 & 65535))
            i32_store(var4 + 7112, (var9 + var11))
            var2 = (var7 - var11)
            var6 = ((var6 & 0xFFFFFFFF) >> var11)
            var1 = (var8 & 255)
            if (1 if (var8 & 255) == 0 else 0):
                i32_store(var4 + 4, 16205)
                var5 = i32_load(var4 + 4)
                continue
            if (var1 & 32):
                i32_store(var4 + 4, 16191)
                i32_store(var4 + 7112, -1)
                var5 = i32_load(var4 + 4)
                continue
            if (var1 & 64):
                i32_store(var10 + 24, 4837)
                i32_store(var4 + 4, 16209)
                var5 = i32_load(var4 + 4)
                continue
            i32_store(var4 + 4, 16201)
            var8 = (var1 & 15)
            i32_store(var4 + 76, (var1 & 15))
            var9 = var0
            var7 = var3
            if (1 if var8 == 0 else 0):
                var1 = i32_load(var4 + 68)
                break
            var5 = var2
            var1 = var0
            if (1 if var2 < var8 else 0):
                while True:  # loop $label141
                    if (1 if var3 == 0 else 0):
                        break
                    var3 = (var3 - 1)
                    var6 = ((i32_load8_u(var1) << var5) + var6)
                    var0 = (var1 + 1)
                    var1 = (var1 + 1)
                    var5 = (var5 + 8)
                    if (1 if (var5 + 8) < var8 else 0):
                        continue
                    break  # end loop
            i32_store(var4 + 7112, (i32_load(var4 + 7112) + var8))
            var1 = (i32_load(var4 + 68) + (var6 & ((-1 << var8) ^ -1)))
            i32_store(var4 + 68, (i32_load(var4 + 68) + (var6 & ((-1 << var8) ^ -1))))
            var2 = (var5 - var8)
            var6 = ((var6 & 0xFFFFFFFF) >> var8)
            i32_store(var4 + 4, 16202)
            i32_store(var4 + 7116, var1)
            var8 = var2
            var5 = var3
            var1 = var0
            var19 = i32_load(var4 + 84)
            var15 = ((-1 << i32_load(var4 + 92)) ^ -1)
            var11 = (i32_load(var4 + 84) + ((var6 & ((-1 << i32_load(var4 + 92)) ^ -1)) << 2))
            var9 = i32_load8_u((i32_load(var4 + 84) + ((var6 & ((-1 << i32_load(var4 + 92)) ^ -1)) << 2)) + 1)
            if (1 if i32_load8_u((i32_load(var4 + 84) + ((var6 & ((-1 << i32_load(var4 + 92)) ^ -1)) << 2)) + 1) <= var2 else 0):
                var7 = var2
                break
            while True:  # loop $label144
                if (1 if var5 == 0 else 0):
                    break
                var9 = (i32_load8_u(var1) << var8)
                var1 = (var1 + 1)
                var5 = (var5 - 1)
                var7 = (var8 + 8)
                var8 = (var8 + 8)
                var6 = (var6 + var9)
                var11 = (var19 + (((var6 + var9) & var15) << 2))
                var9 = i32_load8_u((var19 + (((var6 + var9) & var15) << 2)) + 1)
                if (1 if var7 < i32_load8_u((var19 + (((var6 + var9) & var15) << 2)) + 1) else 0):
                    continue
                break  # end loop
            var15 = i32_load16_u(var11 + 2)
            var8 = i32_load8_u(var11)
            if (1 if i32_load8_u(var11) >= 16 else 0):
                var11 = var9
                break
            var3 = var5
            var0 = var1
            var2 = var7
            var21 = ((-1 << (var8 + var9)) ^ -1)
            var17 = (var19 + (((((var6 & ((-1 << (var8 + var9)) ^ -1)) & 0xFFFFFFFF) >> var9) + var15) << 2))
            var11 = i32_load8_u((var19 + (((((var6 & ((-1 << (var8 + var9)) ^ -1)) & 0xFFFFFFFF) >> var9) + var15) << 2)) + 1)
            if (1 if var7 >= (var9 + i32_load8_u((var19 + (((((var6 & ((-1 << (var8 + var9)) ^ -1)) & 0xFFFFFFFF) >> var9) + var15) << 2)) + 1)) else 0):
                var8 = var7
                break
            while True:  # loop $label148
                if (1 if var3 == 0 else 0):
                    break
                var11 = (i32_load8_u(var0) << var2)
                var0 = (var0 + 1)
                var3 = (var3 - 1)
                var8 = (var2 + 8)
                var2 = (var2 + 8)
                var6 = (var6 + var11)
                var17 = (var19 + ((((((var6 + var11) & var21) & 0xFFFFFFFF) >> var9) + var15) << 2))
                var11 = i32_load8_u((var19 + ((((((var6 + var11) & var21) & 0xFFFFFFFF) >> var9) + var15) << 2)) + 1)
                if (1 if (var9 + i32_load8_u((var19 + ((((((var6 + var11) & var21) & 0xFFFFFFFF) >> var9) + var15) << 2)) + 1)) > var8 else 0):
                    continue
                break  # end loop
            var1 = var0
            var5 = var3
            var7 = (var8 - var9)
            var6 = ((var6 & 0xFFFFFFFF) >> var9)
            var8 = i32_load8_u(var17)
            var15 = i32_load16_u(var17 + 2)
            i32_store(i32_load(var4 + 7112) + 7112, ((i32_load(var4 + 7112) + var9) + var11))
            var2 = (var7 - var11)
            var6 = ((var6 & 0xFFFFFFFF) >> var11)
            if (var8 & 64):
                i32_store(var10 + 24, 4865)
                i32_store(var4 + 4, 16209)
                var0 = var1
                var3 = var5
                var5 = i32_load(var4 + 4)
                continue
            i32_store(var4 + 4, 16203)
            var9 = (var8 & 15)
            i32_store(var4 + 76, (var8 & 15))
            i32_store(var4 + 72, (var15 & 65535))
            if (1 if var9 == 0 else 0):
                var0 = var1
                var3 = var5
                break
            var8 = var2
            var3 = var5
            var7 = var1
            if (1 if var2 >= var9 else 0):
                var0 = var1
                break
            while True:  # loop $label152
                if (1 if var3 == 0 else 0):
                    break
                var3 = (var3 - 1)
                var6 = ((i32_load8_u(var7) << var8) + var6)
                var0 = (var7 + 1)
                var7 = (var7 + 1)
                var8 = (var8 + 8)
                if (1 if (var8 + 8) < var9 else 0):
                    continue
                break  # end loop
            i32_store(var4 + 7112, (i32_load(var4 + 7112) + var9))
            i32_store(var4 + 72, (i32_load(var4 + 72) + (var6 & ((-1 << var9) ^ -1))))
            var2 = (var8 - var9)
            var6 = ((var6 & 0xFFFFFFFF) >> var9)
            i32_store(var4 + 4, 16204)
            if var13:
                break
            var13 = 0
            break
            var1 = i32_load(var4 + 72)
            var5 = (var18 - var13)
            if (1 if i32_load(var4 + 72) > (var18 - var13) else 0):
                var1 = (var1 - var5)
                if (1 if (var1 - var5) <= i32_load(var4 + 48) else 0):
                    break
                if (1 if i32_load(var4 + 7108) == 0 else 0):
                    break
                i32_store(var10 + 24, 4158)
                i32_store(var4 + 4, 16209)
                var5 = i32_load(var4 + 4)
                continue
                var5 = i32_load(var4 + 52)
                if (1 if i32_load(var4 + 52) < var1 else 0):
                    var1 = (var1 - var5)
                    break
                var5 = (i32_load(var4 + 56) + (var5 - var1))
                var8 = i32_load(var4 + 68)
                break
            var5 = (var14 - var1)
            var8 = i32_load(var4 + 68)
            var1 = i32_load(var4 + 68)
            var7 = (var1 if (1 if var1 < var13 else 0) else var13)
            i32_store(var4 + 68, (var8 - (var1 if (1 if var1 < var13 else 0) else var13)))
            var9 = (var7 - 1)
            var8 = 0
            var11 = (var7 & 7)
            if (1 if (var7 & 7) == 0 else 0):
                break
            var1 = var7
            while True:  # loop $label158
                i32_store8(var14, i32_load8_u(var5))
                var1 = (var1 - 1)
                var14 = (var14 + 1)
                var5 = (var5 + 1)
                var8 = (var8 + 1)
                if (1 if (var8 + 1) != var11 else 0):
                    continue
                break  # end loop
            break
            var0 = (var0 + var3)
            var2 = (var2 + (var3 << 3))
            break
            var0 = (var1 + var5)
            var2 = (var2 + (var5 << 3))
            break
            var0 = (var1 + var5)
            var2 = (var7 + (var5 << 3))
            break
            var0 = (var0 + var3)
            var2 = (var2 + (var3 << 3))
            break
            var0 = (var7 + var9)
            var2 = (var2 + (var7 << 3))
            break
            var0 = (var1 + var5)
            var2 = (var7 + (var5 << 3))
            break
            var0 = (var0 + var3)
            var2 = (var2 + (var3 << 3))
            break
            i32_store(var10 + 24, 2894)
            i32_store(var4 + 4, 16209)
            var5 = i32_load(var4 + 4)
            continue
            var1 = var7
            if (1 if var9 >= 7 else 0):
                while True:  # loop $label160
                    i32_store8(var14, i32_load8_u(var5))
                    i32_store8(var14 + 1, i32_load8_u(var5 + 1))
                    i32_store8(var14 + 2, i32_load8_u(var5 + 2))
                    i32_store8(var14 + 3, i32_load8_u(var5 + 3))
                    i32_store8(var14 + 4, i32_load8_u(var5 + 4))
                    i32_store8(var14 + 5, i32_load8_u(var5 + 5))
                    i32_store8(var14 + 6, i32_load8_u(var5 + 6))
                    i32_store8(var14 + 7, i32_load8_u(var5 + 7))
                    var14 = (var14 + 8)
                    var5 = (var5 + 8)
                    var1 = (var1 - 8)
                    if (var1 - 8):
                        continue
                    break  # end loop
            var13 = (var13 - var7)
            if i32_load(var4 + 68):
                break
            i32_store(var4 + 4, 16200)
            var5 = i32_load(var4 + 4)
            continue
            var5 = i32_load(var4 + 4)
            continue
            var3 = 0
            var2 = var1
            var1 = var12
            break
            var1 = i32_load(var4 + 36)
            if i32_load(var4 + 36):
                i32_store(var1 + 16, 0)
            var2 = var5
            i32_store(var4 + 4, 16185)
            var8 = i32_load(var4 + 20)
            if (i32_load(var4 + 20) & 1024):
                var5 = i32_load(var4 + 68)
                var1 = (i32_load(var4 + 68) if (1 if var3 > var5 else 0) else var3)
                if (i32_load(var4 + 68) if (1 if var3 > var5 else 0) else var3):
                    var7 = i32_load(var4 + 36)
                    if (1 if i32_load(var4 + 36) == 0 else 0):
                        break
                    var11 = i32_load(var7 + 16)
                    if (1 if i32_load(var7 + 16) == 0 else 0):
                        break
                    var9 = i32_load(var7 + 24)
                    var5 = (i32_load(var7 + 20) - var5)
                    if (1 if i32_load(var7 + 24) <= (i32_load(var7 + 20) - var5) else 0):
                        break
                    var8 = i32_load(var4 + 20)
                    if (1 if (var8 & 512) == 0 else 0):
                        break
                    if (1 if (i32_load8_u(var4 + 12) & 4) == 0 else 0):
                        break
                    i32_store(var4 + 28, func43(i32_load(var4 + 28), var0, var1))
                    var5 = (i32_load(var4 + 68) - var1)
                    i32_store(var4 + 68, (i32_load(var4 + 68) - var1))
                    var3 = (var3 - var1)
                    var0 = (var0 + var1)
                if var5:
                    break
            i32_store(var4 + 4, 16186)
            i32_store(var4 + 68, 0)
            if (i32_load8_u(var4 + 21) & 8):
                var5 = 0
                if (1 if var3 == 0 else 0):
                    break
                while True:  # loop $label165
                    var1 = i32_load8_u((var0 + var5))
                    var8 = i32_load(var4 + 36)
                    if (1 if i32_load(var4 + 36) == 0 else 0):
                        break
                    var9 = i32_load(var8 + 28)
                    if (1 if i32_load(var8 + 28) == 0 else 0):
                        break
                    var7 = i32_load(var4 + 68)
                    if (1 if i32_load(var4 + 68) >= i32_load(var8 + 32) else 0):
                        break
                    i32_store(var4 + 68, (var7 + 1))
                    i32_store8((var7 + var9), var1)
                    var5 = (var5 + 1)
                    if (var1 if (1 if var3 > (var5 + 1) else 0) else 0):
                        continue
                    break  # end loop
                if (1 if (i32_load8_u(var4 + 21) & 2) == 0 else 0):
                    break
                if (1 if (i32_load8_u(var4 + 12) & 4) == 0 else 0):
                    break
                i32_store(var4 + 28, func43(i32_load(var4 + 28), var0, var5))
                var0 = (var0 + var5)
                var3 = (var3 - var5)
                if (1 if var1 == 0 else 0):
                    break
                break
            var1 = i32_load(var4 + 36)
            if (1 if i32_load(var4 + 36) == 0 else 0):
                break
            i32_store(var1 + 28, 0)
            i32_store(var4 + 4, 16187)
            i32_store(var4 + 68, 0)
            if (i32_load8_u(var4 + 21) & 16):
                var5 = 0
                if (1 if var3 == 0 else 0):
                    break
                while True:  # loop $label169
                    var1 = i32_load8_u((var0 + var5))
                    var8 = i32_load(var4 + 36)
                    if (1 if i32_load(var4 + 36) == 0 else 0):
                        break
                    var9 = i32_load(var8 + 36)
                    if (1 if i32_load(var8 + 36) == 0 else 0):
                        break
                    var7 = i32_load(var4 + 68)
                    if (1 if i32_load(var4 + 68) >= i32_load(var8 + 40) else 0):
                        break
                    i32_store(var4 + 68, (var7 + 1))
                    i32_store8((var7 + var9), var1)
                    var5 = (var5 + 1)
                    if (var1 if (1 if var3 > (var5 + 1) else 0) else 0):
                        continue
                    break  # end loop
                if (1 if (i32_load8_u(var4 + 21) & 2) == 0 else 0):
                    break
                if (1 if (i32_load8_u(var4 + 12) & 4) == 0 else 0):
                    break
                i32_store(var4 + 28, func43(i32_load(var4 + 28), var0, var5))
                var0 = (var0 + var5)
                var3 = (var3 - var5)
                if (1 if var1 == 0 else 0):
                    break
                break
            var1 = i32_load(var4 + 36)
            if (1 if i32_load(var4 + 36) == 0 else 0):
                break
            i32_store(var1 + 36, 0)
            i32_store(var4 + 4, 16188)
            var7 = i32_load(var4 + 20)
            if (i32_load(var4 + 20) & 512):
                if (1 if var2 > 15 else 0):
                    var5 = var0
                    break
                if (1 if var3 == 0 else 0):
                    break
                var1 = (var2 + 8)
                var5 = (var0 + 1)
                var8 = (var3 - 1)
                var6 = ((i32_load8_u(var0) << var2) + var6)
                if (1 if var2 > 7 else 0):
                    var3 = var8
                    var2 = var1
                    break
                if (1 if var8 == 0 else 0):
                    var0 = var5
                    var3 = 0
                    var2 = var1
                    var1 = var12
                    break
                var2 = (var2 + 16)
                var5 = (var0 + 2)
                var3 = (var3 - 2)
                var6 = ((i32_load8_u(var0 + 1) << var1) + var6)
                if (1 if (i32_load8_u(var4 + 12) & 4) == 0 else 0):
                    break
                if (1 if var6 == i32_load16_u(var4 + 28) else 0):
                    break
                i32_store(var10 + 24, 4325)
                i32_store(var4 + 4, 16209)
                var0 = var5
                var5 = i32_load(var4 + 4)
                continue
                var6 = 0
                var2 = 0
                var0 = var5
            var1 = i32_load(var4 + 36)
            if i32_load(var4 + 36):
                i32_store(var1 + 48, 1)
                i32_store(var1 + 44, (((var7 & 0xFFFFFFFF) >> 9) & 1))
            var1 = func43(0, 0, 0)
            i32_store(var4 + 28, func43(0, 0, 0))
            i32_store(var10 + 48, var1)
            i32_store(var4 + 4, 16191)
            var5 = i32_load(var4 + 4)
            continue
            var3 = 0
            var8 = var12
            var1 = var8
            break
            if (1 if var5 == 0 else 0):
                break
            if (1 if i32_load(var4 + 20) == 0 else 0):
                break
            if (1 if var2 > 31 else 0):
                var1 = var0
                break
            if (1 if var3 == 0 else 0):
                break
            var8 = (var2 + 8)
            var1 = (var0 + 1)
            var7 = (var3 - 1)
            var6 = ((i32_load8_u(var0) << var2) + var6)
            if (1 if var2 > 23 else 0):
                var3 = var7
                var2 = var8
                break
            if (1 if var7 == 0 else 0):
                var0 = var1
                var3 = 0
                var2 = var8
                var1 = var12
                break
            var7 = (var2 + 16)
            var1 = (var0 + 2)
            var9 = (var3 - 2)
            var6 = ((i32_load8_u(var0 + 1) << var8) + var6)
            if (1 if var2 > 15 else 0):
                var3 = var9
                var2 = var7
                break
            if (1 if var9 == 0 else 0):
                var0 = var1
                var3 = 0
                var2 = var7
                var1 = var12
                break
            var8 = (var2 + 24)
            var1 = (var0 + 3)
            var9 = (var3 - 3)
            var6 = ((i32_load8_u(var0 + 2) << var7) + var6)
            if (1 if var2 > 7 else 0):
                var3 = var9
                var2 = var8
                break
            if (1 if var9 == 0 else 0):
                var0 = var1
                var3 = 0
                var2 = var8
                var1 = var12
                break
            var2 = (var2 + 32)
            var1 = (var0 + 4)
            var3 = (var3 - 4)
            var6 = ((i32_load8_u(var0 + 3) << var8) + var6)
            var8 = 0
            if (1 if (var5 & 4) == 0 else 0):
                break
            if (1 if var6 == i32_load(var4 + 32) else 0):
                break
            i32_store(var10 + 24, 4114)
            i32_store(var4 + 4, 16209)
            var0 = var1
            var5 = i32_load(var4 + 4)
            continue
            break  # end loop
        var0 = var1
        var2 = 0
        break
        var3 = 0
        var1 = var12
        break
        var8 = var6
        i32_store(var4 + 4, 16208)
        var1 = 1
        var6 = var8
        i32_store(var10 + 16, var13)
        i32_store(var10 + 12, var14)
        i32_store(var10 + 4, var3)
        i32_store(var10, var0)
        i32_store(var4 + 64, var2)
        i32_store(var4 + 60, var6)
        if (1 if i32_load(var4 + 44) == 0 else 0):
            if (1 if var13 == var18 else 0):
                break
            if (1 if i32_load(var4 + 4) > 16208 else 0):
                break
        var2 = (var18 - var13)
        var0 = i32_load(var10 + 28)
        var12 = i32_load(i32_load(var10 + 28) + 56)
        if (1 if i32_load(i32_load(var10 + 28) + 56) == 0 else 0):
            var5 = 1
            # call_indirect via table[i32_load(var10 + 32)]
            var12 = call_indirect(i32_load(var10 + 32))
            i32_store(1 + 56, call_indirect(i32_load(var10 + 32)))
            if (1 if var12 == 0 else 0):
                break
        var3 = i32_load(var0 + 44)
        if (1 if i32_load(var0 + 44) == 0 else 0):
            i64_store(var0 + 48, 0)
            var3 = (1 << i32_load(var0 + 40))
            i32_store(var0 + 44, (1 << i32_load(var0 + 40)))
        if (1 if var2 >= var3 else 0):
            i32_store(var0 + 52, 0)
            break
        var5 = i32_load(var0 + 52)
        var3 = (var3 - var5)
        var12 = (1 if var2 > var3 else 0)
        var3 = ((var3 - var5) if (1 if var2 > var3 else 0) else var2)
        if var12:
            var2 = (var2 - var3)
            i32_store(var0 + 52, var2)
            break
        var5 = 0
        var2 = (i32_load(var0 + 52) + var3)
        var12 = i32_load(var0 + 44)
        i32_store(var0 + 52, ((i32_load(var0 + 52) + var3) if (1 if var2 != i32_load(var0 + 44) else 0) else 0))
        var2 = i32_load(var0 + 48)
        if (1 if i32_load(var0 + 48) >= var12 else 0):
            break
        i32_store(var0 + 48, (var2 + var3))
        break
        i32_store(var0 + 48, i32_load(var0 + 44))
        if 0:
            break
        var13 = i32_load(var10 + 16)
        var2 = i32_load(var10 + 4)
        i32_store(var10 + 8, (i32_load(var10 + 8) + (var35 - var2)))
        var0 = (var18 - var13)
        i32_store(var10 + 20, ((var18 - var13) + i32_load(var10 + 20)))
        i32_store(var4 + 32, (i32_load(var4 + 32) + var0))
        if (1 if (i32_load8_u(var4 + 12) & 4) == 0 else 0):
            break
        if (1 if var13 == var18 else 0):
            break
        var3 = (i32_load(var10 + 12) - var0)
        var12 = i32_load(var4 + 28)
        if i32_load(var4 + 20):
            break
        var0 = func89(var12, var3, var0)
        i32_store(func43(var12, var3, var0) + 28, func89(var12, var3, var0))
        i32_store(var10 + 48, var0)
        var0 = i32_load(var4 + 4)
        i32_store(var10 + 44, (((i32_load(var4 + 64) + ((1 if i32_load(var4 + 8) != 0 else 0) << 6)) + ((1 if i32_load(var4 + 4) == 16191 else 0) << 7)) + (256 if (1 if var0 == 16199 else 0) else ((1 if var0 == 16194 else 0) << 8))))
        var23 = (((var1 if var1 else -5) if (1 if var13 == var18 else 0) else var1) if (1 if var2 == var35 else 0) else var1)
        break
        i32_store(var4 + 4, 16210)
        var23 = -4
        global global0
        global0 = (var20 + 16)
        if (1 if var23 == 0 else 0):
            var0 = i32_load(var16 + 24)
            continue
        break  # end loop
    i32_store(var24 + 12, (i32_load(var24 + 12) - (i32_load(var16 + 12) + var26)))
    var0 = i32_load(var16 + 28)
    if (1 if (var16 + 7) != var29 else 0):
        i32_store(var33, var0)
        break
    var22 = ((1 if (1 if var23 == -5 else 0) else var22) if var0 else var22)
    var1 = (var16 + 8)
    if (1 if (var16 + 8) == 0 else 0):
        break
    if (1 if i32_load(var1 + 32) == 0 else 0):
        break
    var0 = i32_load(var1 + 36)
    if (1 if i32_load(var1 + 36) == 0 else 0):
        break
    var2 = i32_load(var1 + 28)
    if (1 if i32_load(var1 + 28) == 0 else 0):
        break
    if (1 if i32_load(var2) != var1 else 0):
        break
    if (1 if (i32_load(var2 + 4) - 16180) > 31 else 0):
        break
    var3 = i32_load(var2 + 56)
    if i32_load(var2 + 56):
        # call_indirect via table[var0]
        var2 = i32_load(var1 + 28)
        var0 = i32_load(var1 + 36)
    # call_indirect via table[var0]
    i32_store(var1 + 28, 0)
    # br_table ['$label188', '$label189', '$label189', '$label189', '$label189', '$label189', '$label6', '$label189']
    _br_idx = (var23 + 5)
    break  # br_table
    if (1 if var22 != (0 - i32_load(var16 + 24)) else 0):
        break
    global global0
    global0 = (var16 - -64)
    global global0
    global0 = (var24 + 16)
    return call_indirect(var0)

