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
# $func407
# ==========================================================
def func407(var0, var1, var2, var3, var4):
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
    var10 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var14 = i32_load(var1)
    i32_store(var1, 0)
    i32_store(var10 + 48, 0)
    i64_store(var10 + 40, 0)
    var5 = (var10 + 8)
    var7 = -6
    if (1 if i32_load8_u(7784) != 49 else 0):
        break
    var7 = -2
    if (1 if var5 == 0 else 0):
        break
    i32_store(var5 + 24, 0)
    var8 = i32_load(var5 + 32)
    if (1 if i32_load(var5 + 32) == 0 else 0):
        i32_store(var5 + 40, 0)
        i32_store(var5 + 32, 417)
        var8 = 417
    if (1 if i32_load(var5 + 36) == 0 else 0):
        i32_store(var5 + 36, 418)
    var9 = (6 if (1 if var4 == -1 else 0) else var4)
    if (1 if (6 if (1 if var4 == -1 else 0) else var4) > 9 else 0):
        break
    var7 = -4
    # call_indirect via table[var8]
    var4 = call_indirect(var8)
    if (1 if call_indirect(var8) == 0 else 0):
        break
    i32_store(var5 + 28, var4)
    i32_store(var4 + 28, 0)
    i32_store(var4 + 24, 1)
    i32_store(var4 + 4, 42)
    i32_store(var4, var5)
    i32_store(var4 + 80, 15)
    i32_store(var4 + 76, 32768)
    i32_store(var4 + 48, 15)
    i32_store(var4 + 84, 32767)
    i32_store(var4 + 44, 32768)
    i32_store(var4 + 88, 5)
    i32_store(var4 + 52, 32767)
    # call_indirect via table[i32_load(var5 + 32)]
    i32_store(2 + 56, call_indirect(i32_load(var5 + 32)))
    # call_indirect via table[i32_load(var5 + 32)]
    i32_store(2 + 64, call_indirect(i32_load(var5 + 32)))
    # call_indirect via table[i32_load(var5 + 32)]
    var7 = call_indirect(i32_load(var5 + 32))
    i32_store(var4 + 5824, 0)
    i32_store(var4 + 68, var7)
    i32_store(var4 + 5788, 16384)
    # call_indirect via table[i32_load(var5 + 32)]
    var7 = call_indirect(i32_load(var5 + 32))
    i32_store(4 + 8, call_indirect(i32_load(var5 + 32)))
    var8 = i32_load(var4 + 5788)
    i32_store(var4 + 12, (i32_load(var4 + 5788) << 2))
    if (1 if i32_load(var4 + 56) == 0 else 0):
        break
    if (1 if i32_load(var4 + 64) == 0 else 0):
        break
    if (1 if i32_load(var4 + 68) == 0 else 0):
        break
    if var7:
        break
    i32_store(var4 + 4, 666)
    i32_store(var5 + 24, i32_load(28712))
    func400(var5)
    break
    i32_store(var4 + 136, 0)
    i32_store(var4 + 132, var9)
    i32_store8(var4 + 36, 8)
    i32_store(var4 + 5784, (var7 + var8))
    i32_store(var4 + 5796, ((var8 * 3) - 3))
    var7 = -2
    if (1 if var5 == 0 else 0):
        break
    if (1 if i32_load(var5 + 32) == 0 else 0):
        break
    if (1 if i32_load(var5 + 36) == 0 else 0):
        break
    var4 = i32_load(var5 + 28)
    if (1 if i32_load(var5 + 28) == 0 else 0):
        break
    if (1 if i32_load(var4) != var5 else 0):
        break
    var8 = i32_load(var4 + 4)
    # br_table ['$label5', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label5', '$label4', '$label4', '$label4', '$label5', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label5', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label5', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label5', '$label6']
    _br_idx = (i32_load(var4 + 4) - 57)
    break  # br_table
    if (1 if var8 == 666 else 0):
        break
    if (1 if var8 != 42 else 0):
        break
    i32_store(var5 + 44, 2)
    i32_store(var5 + 8, 0)
    i64_store(var5 + 20, 0)
    i32_store(var4 + 20, 0)
    i32_store(var4 + 16, i32_load(var4 + 8))
    var7 = i32_load(var4 + 24)
    if (1 if i32_load(var4 + 24) < 0 else 0):
        var7 = (0 - var7)
        i32_store(var4 + 24, (0 - var7))
    var7 = (1 if var7 == 2 else 0)
    i32_store(var4 + 4, (57 if (1 if var7 == 2 else 0) else 42))
    if var7:
        break
    i32_store(func43(0, 0, 0) + 48, func89(0, 0, 0))
    i32_store(var4 + 40, -2)
    i32_store(var4 + 5820, 0)
    i32_store16(var4 + 5816, 0)
    i32_store((var4 + 2872), 24280)
    i32_store(var4 + 2864, (var4 + 2684))
    i32_store((var4 + 2860), 24260)
    i32_store(var4 + 2852, (var4 + 2440))
    i32_store((var4 + 2848), 24240)
    i32_store(var4 + 2840, (var4 + 148))
    func367(var4)
    var7 = 0
    if (1 if var7 == 0 else 0):
        var4 = i32_load(var5 + 28)
        i32_store(i32_load(var5 + 28) + 60, (i32_load(var4 + 44) << 1))
        var5 = i32_load(var4 + 68)
        var8 = ((i32_load(var4 + 76) << 1) - 2)
        i32_store16((i32_load(var4 + 68) + ((i32_load(var4 + 76) << 1) - 2)), 0)
        func98(var5, 0, var8)
        i32_store(var4 + 5812, 0)
        i64_store(var4 + 116, 8589934592)
        i64_store(var4 + 104, 0)
        i64_store(var4 + 92, 8589934592)
        i32_store(var4 + 72, 0)
        var5 = (i32_load(var4 + 132) * 12)
        i32_store(var4 + 144, i32_load16_u(((i32_load(var4 + 132) * 12) + 23348)))
        i32_store(var4 + 140, i32_load16_u((var5 + 23344)))
        i32_store(var4 + 128, i32_load16_u((var5 + 23346)))
        i32_store(var4 + 124, i32_load16_u((var5 + 23350)))
    if (1 if var7 == 0 else 0):
        i32_store(var10 + 24, 0)
        i32_store(var10 + 20, var0)
        i32_store(var10 + 12, 0)
        i32_store(var10 + 8, var2)
        while True:  # loop $label85
            if (1 if var6 == 0 else 0):
                i32_store(var10 + 24, var14)
                var14 = 0
            var5 = (var10 + 8)
            if (1 if i32_load(var10 + 12) == 0 else 0):
                i32_store(var10 + 12, var3)
                break
            if var3:
                break
            var3 = 0
            var9 = 4
            var8 = 0
            var4 = -2
            if (1 if var5 == 0 else 0):
                break
            if (1 if i32_load(var5 + 32) == 0 else 0):
                break
            if (1 if i32_load(var5 + 36) == 0 else 0):
                break
            var2 = i32_load(var5 + 28)
            if (1 if i32_load(var5 + 28) == 0 else 0):
                break
            if (1 if i32_load(var2) != var5 else 0):
                break
            var7 = i32_load(var2 + 4)
            # br_table ['$label11', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label11', '$label10', '$label10', '$label10', '$label11', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label11', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label11', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label11', '$label12']
            _br_idx = (i32_load(var2 + 4) - 57)
            break  # br_table
            if (1 if var7 == 666 else 0):
                break
            if (1 if var7 != 42 else 0):
                break
            if (1 if var9 > 5 else 0):
                break
            if (1 if i32_load(var5 + 12) == 0 else 0):
                break
            var4 = i32_load(var5 + 4)
            if i32_load(var5 + 4):
                if (1 if i32_load(var5) == 0 else 0):
                    break
            if (1 if var9 == 4 else 0):
                break
            if (1 if var7 != 666 else 0):
                break
            i32_store(var5 + 24, i32_load(28704))
            break
            if (1 if i32_load(var5 + 16) == 0 else 0):
                break
            var0 = i32_load(var2 + 40)
            i32_store(var2 + 40, var9)
            if i32_load(var2 + 20):
                var8 = i32_load(var2 + 20)
                var7 = i32_load(var5 + 16)
                var0 = (i32_load(var2 + 20) if (1 if var7 > var8 else 0) else i32_load(var5 + 16))
                if (1 if (i32_load(var2 + 20) if (1 if var7 > var8 else 0) else i32_load(var5 + 16)) == 0 else 0):
                    break
                i32_store(var5 + 12, (i32_load(var5 + 12) + var0))
                i32_store(var2 + 16, (i32_load(var2 + 16) + var0))
                i32_store(var5 + 20, (i32_load(var5 + 20) + var0))
                var7 = (i32_load(var5 + 16) - var0)
                i32_store(var5 + 16, (i32_load(var5 + 16) - var0))
                var4 = i32_load(var2 + 20)
                var8 = (i32_load(var2 + 20) - var0)
                i32_store(var2 + 20, (i32_load(var2 + 20) - var0))
                if (1 if var0 != var4 else 0):
                    break
                i32_store(var2 + 16, i32_load(var2 + 8))
                if var7:
                    var7 = i32_load(var2 + 4)
                    break
                break
            if var4:
                break
            if (1 if var9 == 4 else 0):
                break
            if (1 if ((var9 << 1) + (-9 if (1 if var9 > 4 else 0) else 0)) > ((var0 << 1) + (-9 if (1 if var0 > 4 else 0) else 0)) else 0):
                break
            break
            if (1 if var7 != 42 else 0):
                if (1 if var7 != 666 else 0):
                    break
                if (1 if i32_load(var5 + 4) == 0 else 0):
                    break
                break
            if (1 if i32_load(var2 + 24) == 0 else 0):
                i32_store(var2 + 4, 113)
                break
            var6 = ((i32_load(var2 + 48) << 12) - 30720)
            var4 = 0
            if (1 if i32_load(var2 + 136) > 1 else 0):
                break
            var0 = i32_load(var2 + 132)
            if (1 if i32_load(var2 + 132) < 2 else 0):
                break
            var4 = 64
            if (1 if var0 < 6 else 0):
                break
            var4 = (128 if (1 if var0 == 6 else 0) else 192)
            i32_store(var2 + 20, (var8 + 1))
            var0 = (var4 | var6)
            var0 = (((var4 | var6) | 32) if i32_load(var2 + 108) else var0)
            i32_store8((i32_load(var2 + 8) + var8), (((((var4 | var6) | 32) if i32_load(var2 + 108) else var0) & 0xFFFFFFFF) >> 8))
            var4 = i32_load(var2 + 20)
            i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
            i32_store8((var4 + i32_load(var2 + 8)), (((var0 % 31) | var0) ^ 31))
            if i32_load(var2 + 108):
                var0 = i32_load(var5 + 48)
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), ((var0 & 0xFFFFFFFF) >> 24))
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), ((var0 & 0xFFFFFFFF) >> 16))
                var0 = i32_load(var5 + 48)
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), ((var0 & 0xFFFFFFFF) >> 8))
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), var0)
            i32_store(var5 + 48, func89(0, 0, 0))
            i32_store(var2 + 4, 113)
            func130(var5)
            if i32_load(var2 + 20):
                break
            var7 = i32_load(var2 + 4)
            if (1 if var7 == 57 else 0):
                i32_store(var5 + 48, func43(0, 0, 0))
                var0 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var0 + i32_load(var2 + 8)), 31)
                var0 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var0 + i32_load(var2 + 8)), 139)
                var0 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var0 + i32_load(var2 + 8)), 8)
                var0 = i32_load(var2 + 28)
                if (1 if i32_load(var2 + 28) == 0 else 0):
                    var0 = i32_load(var2 + 20)
                    i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                    i32_store8((var0 + i32_load(var2 + 8)), 0)
                    var0 = i32_load(var2 + 20)
                    i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                    i32_store8((var0 + i32_load(var2 + 8)), 0)
                    var0 = i32_load(var2 + 20)
                    i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                    i32_store8((var0 + i32_load(var2 + 8)), 0)
                    var0 = i32_load(var2 + 20)
                    i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                    i32_store8((var0 + i32_load(var2 + 8)), 0)
                    var0 = i32_load(var2 + 20)
                    i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                    i32_store8((var0 + i32_load(var2 + 8)), 0)
                    var4 = 2
                    var0 = i32_load(var2 + 132)
                    if (1 if i32_load(var2 + 132) != 9 else 0):
                        var4 = (4 if (1 if i32_load(var2 + 136) > 1 else 0) else ((1 if var0 < 2 else 0) << 2))
                    var0 = i32_load(var2 + 20)
                    i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                    i32_store8((var0 + i32_load(var2 + 8)), var4)
                    var0 = i32_load(var2 + 20)
                    i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                    i32_store8((var0 + i32_load(var2 + 8)), 3)
                    i32_store(var2 + 4, 113)
                    func130(var5)
                    if (1 if i32_load(var2 + 20) == 0 else 0):
                        break
                    break
                var6 = i32_load(var0 + 36)
                var7 = i32_load(var0 + 28)
                var8 = i32_load(var0 + 16)
                var11 = i32_load(var0 + 44)
                var0 = i32_load(var0)
                var12 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                var4 = 2
                i32_store8((var12 + i32_load(var2 + 8)), ((((((1 if var11 != 0 else 0) << 1) | (1 if var0 != 0 else 0)) | ((1 if var8 != 0 else 0) << 2)) | ((1 if var7 != 0 else 0) << 3)) | ((1 if var6 != 0 else 0) << 4)))
                var0 = i32_load(i32_load(var2 + 28) + 4)
                var6 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var6 + i32_load(var2 + 8)), var0)
                var0 = i32_load(i32_load(var2 + 28) + 4)
                var6 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var6 + i32_load(var2 + 8)), ((var0 & 0xFFFFFFFF) >> 8))
                var0 = i32_load16_u(i32_load(var2 + 28) + 6)
                var6 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var6 + i32_load(var2 + 8)), var0)
                var0 = i32_load8_u(i32_load(var2 + 28) + 7)
                var6 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var6 + i32_load(var2 + 8)), var0)
                var0 = i32_load(var2 + 132)
                if (1 if i32_load(var2 + 132) != 9 else 0):
                    var4 = (4 if (1 if i32_load(var2 + 136) > 1 else 0) else ((1 if var0 < 2 else 0) << 2))
                var0 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var0 + i32_load(var2 + 8)), var4)
                var0 = i32_load(i32_load(var2 + 28) + 12)
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), var0)
                var0 = i32_load(var2 + 28)
                if i32_load(i32_load(var2 + 28) + 16):
                    var0 = i32_load(var0 + 20)
                    var4 = i32_load(var2 + 20)
                    i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                    i32_store8((var4 + i32_load(var2 + 8)), var0)
                    var0 = i32_load(i32_load(var2 + 28) + 20)
                    var4 = i32_load(var2 + 20)
                    i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                    i32_store8((var4 + i32_load(var2 + 8)), ((var0 & 0xFFFFFFFF) >> 8))
                else:
                if i32_load(var0 + 44):
                    i32_store(var5 + 48, func43(i32_load(var5 + 48), i32_load(var2 + 8), i32_load(var2 + 20)))
                i32_store(var2 + 4, 69)
                i32_store(var2 + 32, 0)
                break
            else:
            # br_table ['$label25', '$label22', '$label22', '$label22', '$label26', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label27', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label22', '$label28', '$label22']
            _br_idx = (var7 - 69)
            break  # br_table
            var0 = i32_load(var2 + 28)
            var8 = i32_load(i32_load(var2 + 28) + 16)
            if i32_load(i32_load(var2 + 28) + 16):
                var11 = i32_load(var2 + 12)
                var4 = i32_load(var2 + 20)
                var7 = i32_load(var2 + 32)
                var6 = (i32_load16_u(var0 + 20) - i32_load(var2 + 32))
                if (1 if i32_load(var2 + 12) < (i32_load(var2 + 20) + (i32_load16_u(var0 + 20) - i32_load(var2 + 32))) else 0):
                    var7 = (var11 - var4)
                    var0 = i32_load(var2 + 12)
                    i32_store(var2 + 20, i32_load(var2 + 12))
                    if (1 if i32_load(i32_load(var2 + 28) + 44) == 0 else 0):
                        break
                    if (1 if var0 <= var4 else 0):
                        break
                    i32_store(var5 + 48, func43(i32_load(var5 + 48), (i32_load(var2 + 8) + var4), (var0 - var4)))
                    i32_store(var2 + 32, (i32_load(var2 + 32) + var7))
                    var0 = i32_load(var5 + 28)
                    var4 = i32_load(var0 + 20)
                    var8 = i32_load(var5 + 16)
                    var4 = (i32_load(var0 + 20) if (1 if var4 < var8 else 0) else i32_load(var5 + 16))
                    if (1 if (i32_load(var0 + 20) if (1 if var4 < var8 else 0) else i32_load(var5 + 16)) == 0 else 0):
                        break
                    i32_store(var5 + 12, (i32_load(var5 + 12) + var4))
                    i32_store(var0 + 16, (i32_load(var0 + 16) + var4))
                    i32_store(var5 + 20, (i32_load(var5 + 20) + var4))
                    i32_store(var5 + 16, (i32_load(var5 + 16) - var4))
                    var8 = i32_load(var0 + 20)
                    i32_store(var0 + 20, (i32_load(var0 + 20) - var4))
                    if (1 if var4 != var8 else 0):
                        break
                    i32_store(var0 + 16, i32_load(var0 + 8))
                    if i32_load(var2 + 20):
                        break
                    var6 = (var6 - var7)
                    var8 = i32_load(var2 + 12)
                    if (1 if (var6 - var7) > i32_load(var2 + 12) else 0):
                        while True:  # loop $label33
                            var0 = i32_load(var2 + 12)
                            i32_store(var2 + 20, i32_load(var2 + 12))
                            if (1 if i32_load(i32_load(var2 + 28) + 44) == 0 else 0):
                                break
                            if (1 if var0 == 0 else 0):
                                break
                            i32_store(var5 + 48, func43(i32_load(var5 + 48), i32_load(var2 + 8), var0))
                            i32_store(var2 + 32, (i32_load(var2 + 32) + var8))
                            var0 = i32_load(var5 + 28)
                            var4 = i32_load(var0 + 20)
                            var7 = i32_load(var5 + 16)
                            var4 = (i32_load(var0 + 20) if (1 if var4 < var7 else 0) else i32_load(var5 + 16))
                            if (1 if (i32_load(var0 + 20) if (1 if var4 < var7 else 0) else i32_load(var5 + 16)) == 0 else 0):
                                break
                            i32_store(var5 + 12, (i32_load(var5 + 12) + var4))
                            i32_store(var0 + 16, (i32_load(var0 + 16) + var4))
                            i32_store(var5 + 20, (i32_load(var5 + 20) + var4))
                            i32_store(var5 + 16, (i32_load(var5 + 16) - var4))
                            var7 = i32_load(var0 + 20)
                            i32_store(var0 + 20, (i32_load(var0 + 20) - var4))
                            if (1 if var4 != var7 else 0):
                                break
                            i32_store(var0 + 16, i32_load(var0 + 8))
                            if i32_load(var2 + 20):
                                break
                            var6 = (var6 - var8)
                            var8 = i32_load(var2 + 12)
                            if (1 if (var6 - var8) > i32_load(var2 + 12) else 0):
                                continue
                            break  # end loop
                    var7 = i32_load(var2 + 32)
                    var8 = i32_load(i32_load(var2 + 28) + 16)
                    var4 = 0
                var0 = (i32_load(var2 + 20) + var6)
                i32_store(var2 + 20, (i32_load(var2 + 20) + var6))
                if (1 if i32_load(i32_load(var2 + 28) + 44) == 0 else 0):
                    break
                if (1 if var0 <= var4 else 0):
                    break
                i32_store(var5 + 48, func43(i32_load(var5 + 48), (i32_load(var2 + 8) + var4), (var0 - var4)))
                i32_store(var2 + 32, 0)
            i32_store(var2 + 4, 73)
            if i32_load(i32_load(var2 + 28) + 28):
                var6 = i32_load(var2 + 20)
                while True:  # loop $label38
                    var4 = i32_load(var2 + 20)
                    if (1 if i32_load(var2 + 20) != i32_load(var2 + 12) else 0):
                        break
                    if (1 if i32_load(i32_load(var2 + 28) + 44) == 0 else 0):
                        break
                    if (1 if var4 <= var6 else 0):
                        break
                    i32_store(var5 + 48, func43(i32_load(var5 + 48), (i32_load(var2 + 8) + var6), (var4 - var6)))
                    var0 = i32_load(var5 + 28)
                    var4 = i32_load(var0 + 20)
                    var6 = i32_load(var5 + 16)
                    var4 = (i32_load(var0 + 20) if (1 if var4 < var6 else 0) else i32_load(var5 + 16))
                    if (1 if (i32_load(var0 + 20) if (1 if var4 < var6 else 0) else i32_load(var5 + 16)) == 0 else 0):
                        break
                    i32_store(var5 + 12, (i32_load(var5 + 12) + var4))
                    i32_store(var0 + 16, (i32_load(var0 + 16) + var4))
                    i32_store(var5 + 20, (i32_load(var5 + 20) + var4))
                    i32_store(var5 + 16, (i32_load(var5 + 16) - var4))
                    var6 = i32_load(var0 + 20)
                    i32_store(var0 + 20, (i32_load(var0 + 20) - var4))
                    if (1 if var4 != var6 else 0):
                        break
                    i32_store(var0 + 16, i32_load(var0 + 8))
                    var4 = 0
                    var6 = 0
                    if (1 if i32_load(var2 + 20) == 0 else 0):
                        break
                    break
                    var0 = i32_load(i32_load(var2 + 28) + 28)
                    var7 = i32_load(var2 + 32)
                    i32_store(var2 + 32, (i32_load(var2 + 32) + 1))
                    var0 = i32_load8_u((var0 + var7))
                    i32_store(var2 + 20, (var4 + 1))
                    i32_store8((i32_load(var2 + 8) + var4), var0)
                    if var0:
                        continue
                    break  # end loop
                if (1 if i32_load(i32_load(var2 + 28) + 44) == 0 else 0):
                    break
                var0 = i32_load(var2 + 20)
                if (1 if i32_load(var2 + 20) <= var6 else 0):
                    break
                i32_store(var5 + 48, func43(i32_load(var5 + 48), (i32_load(var2 + 8) + var6), (var0 - var6)))
                i32_store(var2 + 32, 0)
            i32_store(var2 + 4, 91)
            if (1 if i32_load(i32_load(var2 + 28) + 36) == 0 else 0):
                break
            var6 = i32_load(var2 + 20)
            while True:  # loop $label44
                var4 = i32_load(var2 + 20)
                if (1 if i32_load(var2 + 20) != i32_load(var2 + 12) else 0):
                    break
                if (1 if i32_load(i32_load(var2 + 28) + 44) == 0 else 0):
                    break
                if (1 if var4 <= var6 else 0):
                    break
                i32_store(var5 + 48, func43(i32_load(var5 + 48), (i32_load(var2 + 8) + var6), (var4 - var6)))
                var0 = i32_load(var5 + 28)
                var4 = i32_load(var0 + 20)
                var6 = i32_load(var5 + 16)
                var4 = (i32_load(var0 + 20) if (1 if var4 < var6 else 0) else i32_load(var5 + 16))
                if (1 if (i32_load(var0 + 20) if (1 if var4 < var6 else 0) else i32_load(var5 + 16)) == 0 else 0):
                    break
                i32_store(var5 + 12, (i32_load(var5 + 12) + var4))
                i32_store(var0 + 16, (i32_load(var0 + 16) + var4))
                i32_store(var5 + 20, (i32_load(var5 + 20) + var4))
                i32_store(var5 + 16, (i32_load(var5 + 16) - var4))
                var6 = i32_load(var0 + 20)
                i32_store(var0 + 20, (i32_load(var0 + 20) - var4))
                if (1 if var4 != var6 else 0):
                    break
                i32_store(var0 + 16, i32_load(var0 + 8))
                var4 = 0
                var6 = 0
                if (1 if i32_load(var2 + 20) == 0 else 0):
                    break
                break
                var0 = i32_load(i32_load(var2 + 28) + 36)
                var7 = i32_load(var2 + 32)
                i32_store(var2 + 32, (i32_load(var2 + 32) + 1))
                var0 = i32_load8_u((var0 + var7))
                i32_store(var2 + 20, (var4 + 1))
                i32_store8((i32_load(var2 + 8) + var4), var0)
                if var0:
                    continue
                break  # end loop
            if (1 if i32_load(i32_load(var2 + 28) + 44) == 0 else 0):
                break
            var0 = i32_load(var2 + 20)
            if (1 if i32_load(var2 + 20) <= var6 else 0):
                break
            i32_store(var5 + 48, func43(i32_load(var5 + 48), (i32_load(var2 + 8) + var6), (var0 - var6)))
            i32_store(var2 + 4, 103)
            if i32_load(i32_load(var2 + 28) + 44):
                var4 = i32_load(var2 + 20)
                if (1 if i32_load(var2 + 12) < (i32_load(var2 + 20) + 2) else 0):
                    func130(var5)
                    if i32_load(var2 + 20):
                        break
                    var4 = 0
                var0 = i32_load(var5 + 48)
                i32_store(var2 + 20, (var4 + 1))
                i32_store8((i32_load(var2 + 8) + var4), var0)
                var0 = i32_load(var5 + 48)
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), ((var0 & 0xFFFFFFFF) >> 8))
                i32_store(var5 + 48, func43(0, 0, 0))
            i32_store(var2 + 4, 113)
            func130(var5)
            if (1 if i32_load(var2 + 20) == 0 else 0):
                break
            break
            break
            if i32_load(var5 + 4):
                break
            if i32_load(var2 + 116):
                break
            if (1 if var9 == 0 else 0):
                break
            if (1 if i32_load(var2 + 4) == 666 else 0):
                break
            var0 = i32_load(var2 + 132)
            if (1 if i32_load(var2 + 132) == 0 else 0):
                break
            # br_table ['$label49', '$label50', '$label51']
            _br_idx = (i32_load(var2 + 136) - 2)
            break  # br_table
            while True:  # loop $label55
                if i32_load(var2 + 116):
                    break
                if i32_load(var2 + 116):
                    break
                if var9:
                    break
                break
                i32_store(var2 + 96, 0)
                var0 = i32_load8_u((i32_load(var2 + 56) + i32_load(var2 + 108)))
                var4 = i32_load(var2 + 5792)
                i32_store(var2 + 5792, (i32_load(var2 + 5792) + 1))
                i32_store8((var4 + i32_load(var2 + 5784)), 0)
                var4 = i32_load(var2 + 5792)
                i32_store(var2 + 5792, (i32_load(var2 + 5792) + 1))
                i32_store8((var4 + i32_load(var2 + 5784)), 0)
                var4 = i32_load(var2 + 5792)
                i32_store(var2 + 5792, (i32_load(var2 + 5792) + 1))
                i32_store8((var4 + i32_load(var2 + 5784)), var0)
                var0 = (var2 + (var0 << 2))
                i32_store16((var2 + (var0 << 2)) + 148, (i32_load16_u(var0 + 148) + 1))
                i32_store(var2 + 116, (i32_load(var2 + 116) - 1))
                var4 = (i32_load(var2 + 108) + 1)
                i32_store(var2 + 108, (i32_load(var2 + 108) + 1))
                if (1 if i32_load(var2 + 5792) != i32_load(var2 + 5796) else 0):
                    continue
                var0 = i32_load(var2 + 92)
                if (1 if i32_load(var2 + 92) >= 0 else 0):
                else:
                i32_store(var2 + 92, i32_load(var2 + 108))
                var0 = i32_load(var2)
                var4 = i32_load(i32_load(var2) + 28)
                var6 = i32_load(var4 + 20)
                var7 = i32_load(var0 + 16)
                var6 = (i32_load(var4 + 20) if (1 if var6 < var7 else 0) else i32_load(var0 + 16))
                if (1 if (i32_load(var4 + 20) if (1 if var6 < var7 else 0) else i32_load(var0 + 16)) == 0 else 0):
                    break
                i32_store(var0 + 12, (i32_load(var0 + 12) + var6))
                i32_store(var4 + 16, (i32_load(var4 + 16) + var6))
                i32_store(var0 + 20, (i32_load(var0 + 20) + var6))
                i32_store(var0 + 16, (i32_load(var0 + 16) - var6))
                var0 = i32_load(var4 + 20)
                i32_store(var4 + 20, (i32_load(var4 + 20) - var6))
                if (1 if var0 != var6 else 0):
                    break
                i32_store(var4 + 16, i32_load(var4 + 8))
                if i32_load(i32_load(var2) + 16):
                    continue
                break  # end loop
            break
            i32_store(var2 + 5812, 0)
            if (1 if var9 == 4 else 0):
                var0 = i32_load(var2 + 92)
                if (1 if i32_load(var2 + 92) >= 0 else 0):
                else:
                i32_store(var2 + 92, i32_load(var2 + 108))
                var0 = i32_load(var2)
                var4 = i32_load(i32_load(var2) + 28)
                var6 = i32_load(var4 + 20)
                var7 = i32_load(var0 + 16)
                var6 = (i32_load(var4 + 20) if (1 if var6 < var7 else 0) else i32_load(var0 + 16))
                if (1 if (i32_load(var4 + 20) if (1 if var6 < var7 else 0) else i32_load(var0 + 16)) == 0 else 0):
                    break
                i32_store(var0 + 12, (i32_load(var0 + 12) + var6))
                i32_store(var4 + 16, (i32_load(var4 + 16) + var6))
                i32_store(var0 + 20, (i32_load(var0 + 20) + var6))
                i32_store(var0 + 16, (i32_load(var0 + 16) - var6))
                var0 = i32_load(var4 + 20)
                i32_store(var4 + 20, (i32_load(var4 + 20) - var6))
                if (1 if var0 != var6 else 0):
                    break
                i32_store(var4 + 16, i32_load(var4 + 8))
                break
            if (1 if i32_load(var2 + 5792) == 0 else 0):
                break
            var0 = i32_load(var2 + 92)
            if (1 if i32_load(var2 + 92) >= 0 else 0):
            else:
            i32_store(var2 + 92, i32_load(var2 + 108))
            var0 = i32_load(var2)
            var4 = i32_load(i32_load(var2) + 28)
            var6 = i32_load(var4 + 20)
            var7 = i32_load(var0 + 16)
            var6 = (i32_load(var4 + 20) if (1 if var6 < var7 else 0) else i32_load(var0 + 16))
            if (1 if (i32_load(var4 + 20) if (1 if var6 < var7 else 0) else i32_load(var0 + 16)) == 0 else 0):
                break
            i32_store(var0 + 12, (i32_load(var0 + 12) + var6))
            i32_store(var4 + 16, (i32_load(var4 + 16) + var6))
            i32_store(var0 + 20, (i32_load(var0 + 20) + var6))
            i32_store(var0 + 16, (i32_load(var0 + 16) - var6))
            var0 = i32_load(var4 + 20)
            i32_store(var4 + 20, (i32_load(var4 + 20) - var6))
            if (1 if var0 != var6 else 0):
                break
            i32_store(var4 + 16, i32_load(var4 + 8))
            if i32_load(i32_load(var2) + 16):
                break
            break
            break
            while True:  # loop $label75
                var8 = i32_load(var2 + 116)
                if (1 if i32_load(var2 + 116) >= 259 else 0):
                    i32_store(var2 + 96, 0)
                    break
                var8 = i32_load(var2 + 116)
                if var9:
                    break
                if (1 if var8 >= 259 else 0):
                    break
                break
                if var8:
                    i32_store(var2 + 96, 0)
                    if (1 if var8 > 2 else 0):
                        break
                    var12 = i32_load(var2 + 108)
                    break
                i32_store(var2 + 5812, 0)
                if (1 if var9 == 4 else 0):
                    var0 = i32_load(var2 + 92)
                    if (1 if i32_load(var2 + 92) >= 0 else 0):
                    else:
                    i32_store(var2 + 92, i32_load(var2 + 108))
                    var0 = i32_load(var2)
                    var4 = i32_load(i32_load(var2) + 28)
                    var6 = i32_load(var4 + 20)
                    var7 = i32_load(var0 + 16)
                    var6 = (i32_load(var4 + 20) if (1 if var6 < var7 else 0) else i32_load(var0 + 16))
                    if (1 if (i32_load(var4 + 20) if (1 if var6 < var7 else 0) else i32_load(var0 + 16)) == 0 else 0):
                        break
                    i32_store(var0 + 12, (i32_load(var0 + 12) + var6))
                    i32_store(var4 + 16, (i32_load(var4 + 16) + var6))
                    i32_store(var0 + 20, (i32_load(var0 + 20) + var6))
                    i32_store(var0 + 16, (i32_load(var0 + 16) - var6))
                    var0 = i32_load(var4 + 20)
                    i32_store(var4 + 20, (i32_load(var4 + 20) - var6))
                    if (1 if var0 != var6 else 0):
                        break
                    i32_store(var4 + 16, i32_load(var4 + 8))
                    break
                if (1 if i32_load(var2 + 5792) == 0 else 0):
                    break
                var0 = i32_load(var2 + 92)
                if (1 if i32_load(var2 + 92) >= 0 else 0):
                else:
                i32_store(var2 + 92, i32_load(var2 + 108))
                var0 = i32_load(var2)
                var4 = i32_load(i32_load(var2) + 28)
                var6 = i32_load(var4 + 20)
                var7 = i32_load(var0 + 16)
                var6 = (i32_load(var4 + 20) if (1 if var6 < var7 else 0) else i32_load(var0 + 16))
                if (1 if (i32_load(var4 + 20) if (1 if var6 < var7 else 0) else i32_load(var0 + 16)) == 0 else 0):
                    break
                i32_store(var0 + 12, (i32_load(var0 + 12) + var6))
                i32_store(var4 + 16, (i32_load(var4 + 16) + var6))
                i32_store(var0 + 20, (i32_load(var0 + 20) + var6))
                i32_store(var0 + 16, (i32_load(var0 + 16) - var6))
                var0 = i32_load(var4 + 20)
                i32_store(var4 + 20, (i32_load(var4 + 20) - var6))
                if (1 if var0 != var6 else 0):
                    break
                i32_store(var4 + 16, i32_load(var4 + 8))
                if i32_load(i32_load(var2) + 16):
                    break
                break
                break
                var12 = i32_load(var2 + 108)
                if (1 if i32_load(var2 + 108) == 0 else 0):
                    var12 = 0
                    break
                var13 = (i32_load(var2 + 56) + var12)
                var0 = ((i32_load(var2 + 56) + var12) - 1)
                var7 = i32_load8_u(((i32_load(var2 + 56) + var12) - 1))
                if (1 if i32_load8_u(((i32_load(var2 + 56) + var12) - 1)) != i32_load8_u(var13) else 0):
                    break
                if (1 if var7 != i32_load8_u(var0 + 2) else 0):
                    break
                if (1 if var7 != i32_load8_u(var0 + 3) else 0):
                    break
                var15 = (var13 + 258)
                var4 = -1
                while True:  # loop $label73
                    var6 = (var4 + var13)
                    if (1 if var7 != i32_load8_u((var4 + var13) + 4) else 0):
                        break
                    if (1 if var7 != i32_load8_u(var6 + 5) else 0):
                        break
                    if (1 if var7 != i32_load8_u(var6 + 6) else 0):
                        break
                    if (1 if var7 != i32_load8_u(var6 + 7) else 0):
                        break
                    var0 = (var4 + 8)
                    var11 = (var13 + (var4 + 8))
                    if (1 if var7 != i32_load8_u((var13 + (var4 + 8))) else 0):
                        break
                    if (1 if var7 != i32_load8_u(var6 + 9) else 0):
                        break
                    if (1 if i32_load8_u(var6 + 10) == var7 else 0):
                        var11 = (var6 + 11)
                        if (1 if var7 != i32_load8_u((var6 + 11)) else 0):
                            break
                        var6 = (1 if var4 < 247 else 0)
                        var4 = var0
                        if var6:
                            continue
                        break
                    break  # end loop
                var11 = (var6 + 10)
                break
                var11 = (var6 + 9)
                break
                var11 = (var6 + 7)
                break
                var11 = (var6 + 6)
                break
                var11 = (var6 + 5)
                break
                var11 = (var6 + 4)
                var0 = ((var11 - var15) + 258)
                var0 = (((var11 - var15) + 258) if (1 if var0 < var8 else 0) else var8)
                i32_store(var2 + 96, (((var11 - var15) + 258) if (1 if var0 < var8 else 0) else var8))
                if (1 if var0 < 3 else 0):
                    break
                var4 = i32_load(var2 + 5792)
                i32_store(var2 + 5792, (i32_load(var2 + 5792) + 1))
                i32_store8((var4 + i32_load(var2 + 5784)), 1)
                var4 = i32_load(var2 + 5792)
                i32_store(var2 + 5792, (i32_load(var2 + 5792) + 1))
                i32_store8((var4 + i32_load(var2 + 5784)), 0)
                var4 = i32_load(var2 + 5792)
                i32_store(var2 + 5792, (i32_load(var2 + 5792) + 1))
                var0 = (var0 - 3)
                i32_store8((var4 + i32_load(var2 + 5784)), (var0 - 3))
                var0 = (((i32_load8_u(((var0 & 255) + 23984)) << 2) + var2) + 1176)
                i32_store16((((i32_load8_u(((var0 & 255) + 23984)) << 2) + var2) + 1176), (i32_load16_u(var0) + 1))
                var0 = ((var2 + (i32_load8_u(23472) << 2)) + 2440)
                i32_store16(((var2 + (i32_load8_u(23472) << 2)) + 2440), (i32_load16_u(var0) + 1))
                var0 = i32_load(var2 + 96)
                i32_store(var2 + 96, 0)
                i32_store(var2 + 116, (i32_load(var2 + 116) - var0))
                var8 = (var0 + i32_load(var2 + 108))
                i32_store(var2 + 108, (var0 + i32_load(var2 + 108)))
                break
                var0 = i32_load8_u((i32_load(var2 + 56) + var12))
                var4 = i32_load(var2 + 5792)
                i32_store(var2 + 5792, (i32_load(var2 + 5792) + 1))
                i32_store8((var4 + i32_load(var2 + 5784)), 0)
                var4 = i32_load(var2 + 5792)
                i32_store(var2 + 5792, (i32_load(var2 + 5792) + 1))
                i32_store8((var4 + i32_load(var2 + 5784)), 0)
                var4 = i32_load(var2 + 5792)
                i32_store(var2 + 5792, (i32_load(var2 + 5792) + 1))
                i32_store8((var4 + i32_load(var2 + 5784)), var0)
                var0 = (var2 + (var0 << 2))
                i32_store16((var2 + (var0 << 2)) + 148, (i32_load16_u(var0 + 148) + 1))
                i32_store(var2 + 116, (i32_load(var2 + 116) - 1))
                var8 = (i32_load(var2 + 108) + 1)
                i32_store(var2 + 108, (i32_load(var2 + 108) + 1))
                if (1 if i32_load(var2 + 5792) != i32_load(var2 + 5796) else 0):
                    continue
                var0 = i32_load(var2 + 92)
                if (1 if i32_load(var2 + 92) >= 0 else 0):
                else:
                i32_store(var2 + 92, i32_load(var2 + 108))
                var0 = i32_load(var2)
                var4 = i32_load(i32_load(var2) + 28)
                var6 = i32_load(var4 + 20)
                var7 = i32_load(var0 + 16)
                var6 = (i32_load(var4 + 20) if (1 if var6 < var7 else 0) else i32_load(var0 + 16))
                if (1 if (i32_load(var4 + 20) if (1 if var6 < var7 else 0) else i32_load(var0 + 16)) == 0 else 0):
                    break
                i32_store(var0 + 12, (i32_load(var0 + 12) + var6))
                i32_store(var4 + 16, (i32_load(var4 + 16) + var6))
                i32_store(var0 + 20, (i32_load(var0 + 20) + var6))
                i32_store(var0 + 16, (i32_load(var0 + 16) - var6))
                var0 = i32_load(var4 + 20)
                i32_store(var4 + 20, (i32_load(var4 + 20) - var6))
                if (1 if var0 != var6 else 0):
                    break
                i32_store(var4 + 16, i32_load(var4 + 8))
                if i32_load(i32_load(var2) + 16):
                    continue
                break  # end loop
            break
            # call_indirect via table[i32_load(((var0 * 12) + 23352))]
            var0 = call_indirect(i32_load(((var0 * 12) + 23352)))
            if (1 if (call_indirect(i32_load(((var0 * 12) + 23352))) & -2) == 2 else 0):
                i32_store(var2 + 4, 666)
            if (1 if (var0 & -3) == 0 else 0):
                var4 = 0
                if i32_load(var5 + 16):
                    break
                break
            if (1 if var0 != 1 else 0):
                break
            # br_table ['$label77', '$label78', '$label78', '$label78', '$label79', '$label78']
            _br_idx = (var9 - 1)
            break  # br_table
            var0 = i32_load(var2 + 5820)
            var4 = (i32_load16_u(var2 + 5816) | (2 << i32_load(var2 + 5820)))
            i32_store16(var2 + 5816, (i32_load16_u(var2 + 5816) | (2 << i32_load(var2 + 5820))))
            if (1 if var0 >= 14 else 0):
                var0 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var0 + i32_load(var2 + 8)), var4)
                var0 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var0 + i32_load(var2 + 8)), i32_load8_u((var2 + 5817)))
                var0 = i32_load(var2 + 5820)
                var4 = ((2 & 0xFFFFFFFF) >> (16 - i32_load(var2 + 5820)))
                i32_store16(var2 + 5816, ((2 & 0xFFFFFFFF) >> (16 - i32_load(var2 + 5820))))
                break
            var0 = (var0 + 3)
            i32_store((var0 - 13) + 5820, (var0 + 3))
            if (1 if var0 >= 10 else 0):
                var0 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var0 + i32_load(var2 + 8)), var4)
                var0 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var0 + i32_load(var2 + 8)), i32_load8_u((var2 + 5817)))
                var4 = 0
                i32_store16(var2 + 5816, 0)
                break
            var0 = (var0 + 7)
            i32_store((i32_load(var2 + 5820) - 9) + 5820, (var0 + 7))
            if (1 if var0 == 16 else 0):
                var0 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var0 + i32_load(var2 + 8)), var4)
                var0 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var0 + i32_load(var2 + 8)), i32_load8_u((var2 + 5817)))
                i32_store16(var2 + 5816, 0)
                break
            if (1 if var0 < 8 else 0):
                break
            var0 = i32_load(var2 + 20)
            i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
            i32_store8((var0 + i32_load(var2 + 8)), var4)
            i32_store16(var2 + 5816, i32_load8_u((var2 + 5817)))
            i32_store(0 + 5820, (i32_load(var2 + 5820) - 8))
            break
            if (1 if var9 != 3 else 0):
                break
            var0 = i32_load(var2 + 68)
            var4 = ((i32_load(var2 + 76) << 1) - 2)
            i32_store16((i32_load(var2 + 68) + ((i32_load(var2 + 76) << 1) - 2)), 0)
            func98(var0, 0, var4)
            if i32_load(var2 + 116):
                break
            i32_store(var2 + 5812, 0)
            i32_store(var2 + 92, 0)
            i32_store(var2 + 108, 0)
            func130(var5)
            if i32_load(var5 + 16):
                break
            break
            var4 = 0
            if (1 if var9 != 4 else 0):
                break
            var4 = 1
            var6 = i32_load(var2 + 24)
            if (1 if i32_load(var2 + 24) <= 0 else 0):
                break
            var0 = i32_load(var5 + 48)
            if (1 if var6 == 2 else 0):
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), var0)
                var0 = i32_load(var5 + 48)
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), ((var0 & 0xFFFFFFFF) >> 8))
                var0 = i32_load16_u(var5 + 50)
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), var0)
                var0 = i32_load8_u(var5 + 51)
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), var0)
                var0 = i32_load(var5 + 8)
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), var0)
                var0 = i32_load(var5 + 8)
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), ((var0 & 0xFFFFFFFF) >> 8))
                var0 = i32_load16_u(var5 + 10)
                var4 = i32_load(var2 + 20)
                i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
                i32_store8((var4 + i32_load(var2 + 8)), var0)
                var4 = i32_load8_u(var5 + 11)
                break
            var4 = i32_load(var2 + 20)
            i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
            i32_store8((var4 + i32_load(var2 + 8)), ((var0 & 0xFFFFFFFF) >> 24))
            var4 = i32_load(var2 + 20)
            i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
            i32_store8((var4 + i32_load(var2 + 8)), ((var0 & 0xFFFFFFFF) >> 16))
            var4 = i32_load(var5 + 48)
            var0 = i32_load(var2 + 20)
            i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
            i32_store8((var0 + i32_load(var2 + 8)), ((var4 & 0xFFFFFFFF) >> 8))
            var0 = i32_load(var2 + 20)
            i32_store(var2 + 20, (i32_load(var2 + 20) + 1))
            i32_store8((var0 + i32_load(var2 + 8)), var4)
            func130(var5)
            var0 = i32_load(var2 + 24)
            if (1 if i32_load(var2 + 24) > 0 else 0):
                i32_store(var2 + 24, (0 - var0))
            var4 = (1 if i32_load(var2 + 20) == 0 else 0)
            break
            i32_store(var5 + 24, i32_load(28716))
            break
            i32_store(var2 + 40, -1)
            if (1 if 0 == 0 else 0):
                var6 = i32_load(var10 + 24)
                continue
            break  # end loop
        i32_store(var1, i32_load(var10 + 28))
        func400((var10 + 8))
    global global0
    global0 = (var10 - -64)
    return -5

