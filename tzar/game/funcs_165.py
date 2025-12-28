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
# $func465
# ==========================================================
def func465(var0, var1, param2):
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
    var47 = 0
    var48 = 0
    var49 = 0
    var50 = 0
    var51 = 0
    var29 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var22 = i32_load(var0 + 2324)
    var37 = i32_load(var0 + 172)
    var5 = i32_load8_u((i32_load(var0 + 2352) + 10321))
    var10 = i32_load(var0 + 2312)
    var26 = i32_load(var0 + 2328)
    var12 = i32_load(var0 + 2320)
    var13 = i32_load(var0 + 2316)
    var16 = i32_load(var0 + 320)
    var33 = i32_load(var0 + 176)
    if (1 if i32_load(var0 + 160) == 2 else 0):
        func273(0  # stack underflow, 0  # stack underflow, 0  # stack underflow, 0  # stack underflow, var0, (var0 + 172))
    if (1 if i32_load(var0 + 180) == 0 else 0):
        break
    var15 = i32_load(var0 + 308)
    if (1 if i32_load(var0 + 308) >= i32_load(var0 + 316) else 0):
        break
    var27 = i32_load(var0 + 176)
    while True:  # loop $label3
        var8 = (i32_load(var0 + 184) + (var15 << 2))
        var4 = i32_load8_u((i32_load(var0 + 184) + (var15 << 2)))
        if (1 if i32_load8_u((i32_load(var0 + 184) + (var15 << 2))) == 0 else 0):
            break
        if (1 if var4 <= 2 else 0):
            break
        var6 = i32_load(var0 + 172)
        var2 = i32_load(var0 + 2324)
        var3 = ((i32_load(var0 + 2312) + ((i32_load(var0 + 172) * i32_load(var0 + 2324)) << 4)) + (var15 << 4))
        if (1 if i32_load(var0 + 2352) == 1 else 0):
            if (1 if var15 > 0 else 0):
                # call_indirect via table[i32_load(9687508)]
            if i32_load8_u(var8 + 2):
                # call_indirect via table[i32_load(9687516)]
            if (1 if var27 > 0 else 0):
                # call_indirect via table[i32_load(9687504)]
            if (1 if i32_load8_u(var8 + 2) == 0 else 0):
                break
            # call_indirect via table[i32_load(9687512)]
            break
        var7 = i32_load8_u(var8 + 1)
        var11 = (var15 << 3)
        var14 = i32_load(var0 + 2328)
        var6 = ((var6 * i32_load(var0 + 2328)) << 3)
        var9 = ((var15 << 3) + (((var6 * i32_load(var0 + 2328)) << 3) + i32_load(var0 + 2320)))
        var11 = ((i32_load(var0 + 2316) + var6) + var11)
        var6 = i32_load8_u(var8 + 3)
        if (1 if var15 > 0 else 0):
            var17 = (var4 + 4)
            # call_indirect via table[i32_load(9687476)]
            # call_indirect via table[i32_load(9687484)]
        if i32_load8_u(var8 + 2):
            # call_indirect via table[i32_load(9687492)]
            # call_indirect via table[i32_load(9687500)]
        if (1 if var27 > 0 else 0):
            var17 = (var4 + 4)
            # call_indirect via table[i32_load(9687472)]
            # call_indirect via table[i32_load(9687480)]
        if (1 if i32_load8_u(var8 + 2) == 0 else 0):
            break
        # call_indirect via table[i32_load(9687488)]
        # call_indirect via table[i32_load(9687496)]
        var15 = (var15 + 1)
        if (1 if (var15 + 1) < i32_load(var0 + 316) else 0):
            continue
        break  # end loop
    var8 = ((var22 * var37) << 4)
    var38 = (var5 * var22)
    var11 = (var10 - (var5 * var22))
    var3 = ((var26 * var37) << 3)
    var34 = (((var5 & 0xFFFFFFFF) >> 1) * var26)
    var26 = (var12 - (((var5 & 0xFFFFFFFF) >> 1) * var26))
    var27 = (var13 - var34)
    if (1 if i32_load(var0 + 584) == 0 else 0):
        break
    var7 = i32_load(var0 + 308)
    var2 = i32_load(var0 + 316)
    if (1 if i32_load(var0 + 308) >= i32_load(var0 + 316) else 0):
        break
    var6 = (var0 + 596)
    while True:  # loop $label7
        var22 = (i32_load(var0 + 188) + (var7 * 800))
        var10 = i32_load8_u((i32_load(var0 + 188) + (var7 * 800)) + 796)
        if (1 if i32_load8_u((i32_load(var0 + 188) + (var7 * 800)) + 796) >= 4 else 0):
            var14 = i32_load(var0 + 2328)
            var9 = ((i32_load(var0 + 2328) * i32_load(var0 + 172)) << 3)
            var12 = i32_load(var0 + 2320)
            var13 = i32_load(var0 + 2316)
            var4 = i32_load(var0 + 592)
            var15 = i32_load(var0 + 588)
            var2 = 0
            while True:  # loop $label5
                var15 = (var6 + (var15 << 2))
                var17 = (i32_load(var15) - i32_load((var6 + (var4 << 2))))
                i32_store((var6 + (var15 << 2)), ((i32_load(var15) - i32_load((var6 + (var4 << 2)))) & 2147483647))
                var4 = (i32_load(var0 + 588) + 1)
                var15 = ((i32_load(var0 + 588) + 1) if (1 if var4 != 55 else 0) else 0)
                i32_store(var0 + 588, ((i32_load(var0 + 588) + 1) if (1 if var4 != 55 else 0) else 0))
                var4 = (i32_load(var0 + 592) + 1)
                var4 = ((i32_load(var0 + 592) + 1) if (1 if var4 != 55 else 0) else 0)
                i32_store(var0 + 592, ((i32_load(var0 + 592) + 1) if (1 if var4 != 55 else 0) else 0))
                i32_store8((var2 + var29), ((((((var17 << 1) >> 24) * var10) & 0xFFFFFFFF) >> 8) ^ 128))
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != 64 else 0):
                    continue
                break  # end loop
            var2 = 0
            var10 = (var7 << 3)
            # call_indirect via table[i32_load(9687520)]
            var22 = i32_load8_u(var22 + 796)
            var4 = i32_load(var0 + 592)
            var15 = i32_load(var0 + 588)
            while True:  # loop $label6
                var15 = (var6 + (var15 << 2))
                var13 = (i32_load(var15) - i32_load((var6 + (var4 << 2))))
                i32_store((var6 + (var15 << 2)), ((i32_load(var15) - i32_load((var6 + (var4 << 2)))) & 2147483647))
                var4 = (i32_load(var0 + 588) + 1)
                var15 = ((i32_load(var0 + 588) + 1) if (1 if var4 != 55 else 0) else 0)
                i32_store(var0 + 588, ((i32_load(var0 + 588) + 1) if (1 if var4 != 55 else 0) else 0))
                var4 = (i32_load(var0 + 592) + 1)
                var4 = ((i32_load(var0 + 592) + 1) if (1 if var4 != 55 else 0) else 0)
                i32_store(var0 + 592, ((i32_load(var0 + 592) + 1) if (1 if var4 != 55 else 0) else 0))
                i32_store8((var2 + var29), ((((((var13 << 1) >> 24) * var22) & 0xFFFFFFFF) >> 8) ^ 128))
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != 64 else 0):
                    continue
                break  # end loop
            # call_indirect via table[i32_load(9687520)]
            var2 = i32_load(var0 + 316)
        var7 = (var7 + 1)
        if (1 if (var7 + 1) < var2 else 0):
            continue
        break  # end loop
    var22 = (var8 + var11)
    var26 = (var3 + var26)
    var27 = (var3 + var27)
    var39 = (var16 - 1)
    if (1 if i32_load(var1 + 44) == 0 else 0):
        break
    var7 = (var33 << 4)
    var6 = ((var33 << 4) + 16)
    if var33:
        var4 = var22
        var3 = var27
        var2 = var26
        break
    var2 = (i32_load(var0 + 2320) + var3)
    var3 = (i32_load(var0 + 2316) + var3)
    var4 = (i32_load(var0 + 2312) + var8)
    var15 = 0
    i32_store(var1 + 28, var2)
    i32_store(var1 + 24, var3)
    i32_store(var1 + 20, var4)
    var4 = 0
    i32_store(var1 + 104, 0)
    var2 = (var6 - (var5 if (1 if var33 < var39 else 0) else 0))
    var3 = i32_load(var1 + 88)
    var35 = ((var6 - (var5 if (1 if var33 < var39 else 0) else 0)) if (1 if var2 < var3 else 0) else i32_load(var1 + 88))
    if (1 if i32_load(var0 + 2392) == 0 else 0):
        break
    if (1 if var15 >= var35 else 0):
        break
    var4 = (var35 - var15)
    var2 = 0
    var17 = 0
    if var0:
        if (1 if var15 < 0 else 0):
            break
        if (1 if var4 <= 0 else 0):
            break
        var14 = (var4 + var15)
        var6 = i32_load(var1 + 88)
        if (1 if (var4 + var15) > i32_load(var1 + 88) else 0):
            break
        var30 = i32_load(var1)
        if i32_load(var0 + 2400):
            break
        var3 = i32_load(var0 + 2388)
        if (1 if i32_load(var0 + 2388) == 0 else 0):
            var2 = func134(1, 144)
            i32_store(var0 + 2388, func134(1, 144))
            if (1 if var2 == 0 else 0):
                break
            if i32_load(var0 + 2404):
                break
            var3 = func58((i64_load32_s(var1 + 88) * i64_load32_s(var1)), 1)
            i32_store(var0 + 2404, func58((i64_load32_s(var1 + 88) * i64_load32_s(var1)), 1))
            if var3:
                i32_store(var0 + 2412, 0)
                i32_store(var0 + 2408, var3)
                break
            if (1 if func99(var0, 1, 8400) == 0 else 0):
                break
            var3 = i32_load(var0 + 2408)
            var7 = i32_load(var0 + 2392)
            if (1 if i32_load(var0 + 2392) == 0 else 0):
                break
            if (1 if var3 == 0 else 0):
                break
            var2 = i32_load(var0 + 2388)
            var8 = i32_load(var0 + 2396)
            var5 = i32_load(52304)
            if (1 if i32_load(52304) != i32_load(52312) else 0):
                i32_store(9687564, 337)
                i32_store(9687560, 338)
                i32_store(9687556, 339)
                i32_store(9687552, 340)
                i32_store(9687548, 341)
                i32_store(9687544, 342)
                i32_store(9687540, 343)
                i32_store(52312, var5)
                i32_store(9687536, 0)
            i32_store(var2 + 136, var3)
            var3 = i32_load(var1)
            i32_store(var2, i32_load(var1))
            var5 = i32_load(var1 + 4)
            i32_store(var2 + 4, i32_load(var1 + 4))
            if (1 if var3 <= 0 else 0):
                break
            if (1 if var5 <= 0 else 0):
                break
            if (1 if var8 < 2 else 0):
                break
            var3 = (i32_load8_u(var7) & 3)
            i32_store(var2 + 8, (i32_load8_u(var7) & 3))
            i32_store(var2 + 12, (((i32_load8_u(var7) & 0xFFFFFFFF) >> 2) & 3))
            var5 = (((i32_load8_u(var7) & 0xFFFFFFFF) >> 4) & 3)
            i32_store(var2 + 16, (((i32_load8_u(var7) & 0xFFFFFFFF) >> 4) & 3))
            if (1 if var3 > 1 else 0):
                break
            if (1 if var5 > 1 else 0):
                break
            if (1 if i32_load8_u(var7) > 63 else 0):
                break
            var3 = (var2 + 24)
            if (var2 + 24):
                # Unknown: memory.fill []
            var8 = (var8 - 1)
            i32_store(var3 + 52, 262)
            i32_store(var3 + 48, 263)
            i32_store(var3 + 44, 264)
            i32_store(var3 + 40, 0)
            i32_store((var2 - -64), var2)
            i32_store(var2 + 24, i32_load(var1))
            i32_store(var2 + 28, i32_load(var1 + 4))
            i32_store(var2 + 96, i32_load(var1 + 72))
            i32_store(var2 + 100, i32_load(var1 + 76))
            i32_store(var2 + 104, i32_load(var1 + 80))
            i32_store(var2 + 108, i32_load(var1 + 84))
            i32_store(var2 + 112, i32_load(var1 + 88))
            # br_table ['$label20', '$label21', '$label22']
            _br_idx = i32_load(var2 + 8)
            break  # br_table
            break
            a_c()
            raise RuntimeError('unreachable')
            var3 = func134(1, 288)
            if (1 if func134(1, 288) == 0 else 0):
                break
            var5 = (var7 + 1)
            i64_store(var3, 8589934592)
            func453()
            if var2:
                var14 = i32_load(var2)
                i32_store(var3 + 100, i32_load(var2))
                var7 = i32_load(var2 + 4)
                i32_store(var3 + 8, (var2 + 24))
                i32_store(var3 + 104, var7)
                i32_store(var2 + 28, var7)
                i32_store(var2 + 24, var14)
                i32_store((var2 - -64), var2)
                i32_store(var3, 0)
                if (1 if func153(i32_load(var2), i32_load(var2 + 4), 1, var3, 0) == 0 else 0):
                    break
                if (1 if i32_load(var3 + 192) != 1 else 0):
                    break
                if (1 if i32_load(var3 + 196) != 3 else 0):
                    break
                if (1 if i32_load(var3 + 120) > 0 else 0):
                    break
                var5 = i32_load(var3 + 164)
                if (1 if i32_load(var3 + 164) <= 0 else 0):
                    break
                var14 = i32_load(var3 + 168)
                var7 = 0
                while True:  # loop $label28
                    var8 = (var14 + (var7 * 548))
                    if i32_load8_u(i32_load((var14 + (var7 * 548)) + 4)):
                        break
                    if i32_load8_u(i32_load(var8 + 8)):
                        break
                    if i32_load8_u(i32_load(var8 + 12)):
                        break
                    var7 = (var7 + 1)
                    if (1 if var5 != (var7 + 1) else 0):
                        continue
                    break  # end loop
                break
                i32_store(var2 + 132, 0)
                var8 = i32_load(var3 + 100)
                var7 = i32_load(var2)
                if (1 if i32_load(var3 + 100) > i32_load(var2) else 0):
                    break
                var51 = (i64_load32_s(var3 + 104) * i64_extend_s(var8))
                var8 = (var7 & 65535)
                var7 = func58(((i64_load32_s(var3 + 104) * i64_extend_s(var8)) + (i64_extend_u((var7 & 65535)) + (i64_extend_s(var7) << 4))), 4)
                i32_store(var3 + 16, func58(((i64_load32_s(var3 + 104) * i64_extend_s(var8)) + (i64_extend_u((var7 & 65535)) + (i64_extend_s(var7) << 4))), 4))
                if var7:
                    break
                i32_store(var3 + 20, 0)
                # br_table ['$label31', '$label25', '$label25', '$label25', '$label25', '$label31', '$label25']
                _br_idx = i32_load(var3)
                break  # br_table
                i32_store(var2 + 132, 1)
                i32_store(var3 + 20, 0)
                var7 = func58((i64_load32_s(var3 + 104) * i64_load32_s(var3 + 100)), 1)
                i32_store(var3 + 16, func58((i64_load32_s(var3 + 104) * i64_load32_s(var3 + 100)), 1))
                if var7:
                    break
                # br_table ['$label31', '$label25', '$label25', '$label25', '$label25', '$label31', '$label25']
                _br_idx = i32_load(var3)
                break  # br_table
                i32_store(var3 + 20, ((var7 + (i32(var51) << 2)) + (var8 << 2)))
                i32_store(var2 + 20, var3)
                break
                i32_store(var3, 1)
                func191(var3)
                break
            a_c()
            raise RuntimeError('unreachable')
            a_c()
            raise RuntimeError('unreachable')
            if 5601:
                break
            var4 = i32_load(i32_load(var0 + 2388) + 20)
            if i32_load(i32_load(var0 + 2388) + 20):
            else:
            break
            var3 = i32_load(var0 + 2388)
            if (1 if i32_load(i32_load(var0 + 2388) + 16) != 1 else 0):
                i32_store(var0 + 2416, 0)
                break
            var4 = (var6 - var15)
            var14 = (var4 + var15)
        if (1 if var6 < var14 else 0):
            break
        var31 = i32_load(var3 + 112)
        if (1 if i32_load(var3 + 8) == 0 else 0):
            var2 = i32_load(var0 + 2392)
            var6 = i32_load(var3)
            var7 = (i32_load(var3) * var15)
            var8 = ((i32_load(var0 + 2392) + (i32_load(var3) * var15)) + 1)
            if (1 if ((i32_load(var0 + 2392) + (i32_load(var3) * var15)) + 1) > (var2 + i32_load(var0 + 2396)) else 0):
                break
            if (1 if i32_load(((i32_load(var3 + 12) << 2) + 9687552)) == 0 else 0):
                break
            var2 = i32_load(var0 + 2412)
            if (1 if var4 <= 0 else 0):
                break
            var5 = (var4 & 1)
            var7 = (i32_load(var0 + 2408) + var7)
            if (1 if var4 != 1 else 0):
                var9 = (var4 & -2)
                var4 = 0
                while True:  # loop $label39
                    # call_indirect via table[i32_load(((i32_load(var3 + 12) << 2) + 9687552))]
                    var8 = (var6 + var8)
                    var2 = (var6 + var7)
                    # call_indirect via table[i32_load(((i32_load(var3 + 12) << 2) + 9687552))]
                    var8 = (var6 + var8)
                    var7 = (var2 + var6)
                    var4 = (var4 + 2)
                    if (1 if (var4 + 2) != var9 else 0):
                        continue
                    break  # end loop
            if (1 if var5 == 0 else 0):
                break
            # call_indirect via table[i32_load(((i32_load(var3 + 12) << 2) + 9687552))]
            var2 = var7
            i32_store(var0 + 2412, var2)
            break
        if (1 if i32_load(var3 + 20) == 0 else 0):
            break
        var9 = i32_load(var3 + 20)
        if i32_load(var3 + 20):
            var10 = i32_load(var9 + 104)
            if (1 if var14 <= i32_load(var9 + 104) else 0):
                var12 = 1
                if (1 if i32_load(var9 + 108) >= var14 else 0):
                    break
                if (1 if i32_load(var3 + 132) == 0 else 0):
                    func188()
                    if (1 if i32_load(var3 + 132) == 0 else 0):
                        break
                    var10 = i32_load(var9 + 104)
                var13 = i32_load(var9 + 112)
                var16 = i32_load(var9 + 100)
                var4 = (var13 // i32_load(var9 + 100))
                var12 = (i32_load(var9 + 112) - ((var13 // i32_load(var9 + 100)) * var16))
                var23 = i32_load(var9 + 148)
                var24 = i32_load(var9 + 16)
                var25 = (var14 * var16)
                var3 = (1 if var13 >= (var14 * var16) else 0)
                if (1 if (1 if var13 >= (var14 * var16) else 0) == 0 else 0):
                    var2 = i32_load(var9 + 152)
                    if i32_load(var9 + 152):
                    else:
                    var2 = 0
                    if (1 if 0 >= i32_load(var9 + 164) else 0):
                        break
                    var17 = (i32_load(var9 + 168) + (var2 * 548))
                var20 = (var10 * var16)
                if (1 if (var10 * var16) >= var13 else 0):
                    if (1 if var10 >= var14 else 0):
                        if (1 if i32_load(var9 + 120) > 0 else 0):
                            break
                        var7 = i32_load(var9 + 164)
                        if (1 if i32_load(var9 + 164) <= 0 else 0):
                            break
                        var6 = i32_load(var9 + 168)
                        var5 = 0
                        while True:  # loop $label47
                            var2 = (var6 + (var5 * 548))
                            if i32_load8_u(i32_load((var6 + (var5 * 548)) + 4)):
                                break
                            if i32_load8_u(i32_load(var2 + 8)):
                                break
                            if i32_load8_u(i32_load(var2 + 12)):
                                break
                            var5 = (var5 + 1)
                            if (1 if var7 != (var5 + 1) else 0):
                                continue
                            break  # end loop
                        break
                        a_c()
                        raise RuntimeError('unreachable')
                        if var3:
                            break
                        if i32_load(var9 + 48):
                            break
                        var18 = (var9 + 24)
                        while True:  # loop $label73
                            if (1 if (var12 & var23) == 0 else 0):
                                var2 = i32_load(var9 + 152)
                                if i32_load(var9 + 152):
                                else:
                                var2 = 0
                                if (1 if 0 >= i32_load(var9 + 164) else 0):
                                    break
                                var17 = (i32_load(var9 + 168) + (var2 * 548))
                            if var17:
                                var5 = i32_load(var9 + 44)
                                if (1 if i32_load(var9 + 44) >= 32 else 0):
                                    func135(var18)
                                    var5 = i32_load(var9 + 44)
                                var51 = i64_load(var9 + 24)
                                var10 = (i32_load(var17) + ((i32(((i64_load(var9 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((var5 & 63)))) & 255) << 2))
                                var2 = i32_load8_u((i32_load(var17) + ((i32(((i64_load(var9 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((var5 & 63)))) & 255) << 2)))
                                if (1 if i32_load8_u((i32_load(var17) + ((i32(((i64_load(var9 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((var5 & 63)))) & 255) << 2))) >= 9 else 0):
                                    var5 = (var5 + 8)
                                    var10 = ((var10 + (i32_load16_u(var10 + 2) << 2)) + ((i32(((var51 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var5 + 8) & 63)))) & ((-1 << (var2 - 8)) ^ -1)) << 2))
                                else:
                                var3 = ((var2 & 255) + var5)
                                i32_store(i32_load8_u(((var10 + (i32_load16_u(var10 + 2) << 2)) + ((i32(((var51 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var5 + 8) & 63)))) & ((-1 << (var2 - 8)) ^ -1)) << 2))) + 44, ((var2 & 255) + var5))
                                var2 = i32_load16_u(var10 + 2)
                                if (1 if i32_load16_u(var10 + 2) <= 255 else 0):
                                    i32_store8((var13 + var24), var2)
                                    var13 = (var13 + 1)
                                    var12 = (var12 + 1)
                                    if (1 if (var12 + 1) < var16 else 0):
                                        break
                                    var2 = (var4 + 1)
                                    var12 = 0
                                    if (1 if var4 >= var14 else 0):
                                        var4 = var2
                                        break
                                    if (var2 & 15):
                                        var4 = var2
                                        break
                                    var4 = var2
                                    break
                                var11 = 1
                                if (1 if var2 > 279 else 0):
                                    break
                                var7 = (var2 - 256)
                                if (1 if (var2 - 256) >= 4 else 0):
                                    var3 = (((var2 - 258) & 0xFFFFFFFF) >> 1)
                                    var7 = (func39(var18, (((var2 - 258) & 0xFFFFFFFF) >> 1)) + (((var2 & 1) | 2) << var3))
                                    var51 = i64_load(var9 + 24)
                                    var3 = i32_load(var9 + 44)
                                var5 = (i32_load(var17 + 16) + ((i32(((var51 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((var3 & 63)))) & 255) << 2))
                                var2 = i32_load8_u((i32_load(var17 + 16) + ((i32(((var51 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((var3 & 63)))) & 255) << 2)))
                                if (1 if i32_load8_u((i32_load(var17 + 16) + ((i32(((var51 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((var3 & 63)))) & 255) << 2))) >= 9 else 0):
                                    var3 = (var3 + 8)
                                    var5 = ((var5 + (i32_load16_u(var5 + 2) << 2)) + ((i32(((var51 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var3 + 8) & 63)))) & ((-1 << (var2 - 8)) ^ -1)) << 2))
                                else:
                                var2 = ((var2 & 255) + var3)
                                i32_store(i32_load8_u(((var5 + (i32_load16_u(var5 + 2) << 2)) + ((i32(((var51 & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u(((var3 + 8) & 63)))) & ((-1 << (var2 - 8)) ^ -1)) << 2))) + 44, ((var2 & 255) + var3))
                                var5 = i32_load16_u(var5 + 2)
                                if (1 if var2 >= 32 else 0):
                                    func135(var18)
                                if (1 if var5 >= 4 else 0):
                                    var2 = (((var5 - 2) & 0xFFFFFFFF) >> 1)
                                    var5 = (func39(var18, (((var5 - 2) & 0xFFFFFFFF) >> 1)) + (((var5 & 1) | 2) << var2))
                                if (1 if (var5 + 1) >= 121 else 0):
                                    break
                                var2 = i32_load8_u((var5 + 13840))
                                var2 = (((((i32_load8_u((var5 + 13840)) & 0xFFFFFFFF) >> 4) * var16) - (var2 & 15)) + 8)
                                var2 = (1 if (1 if var2 <= 1 else 0) else (((((i32_load8_u((var5 + 13840)) & 0xFFFFFFFF) >> 4) * var16) - (var2 & 15)) + 8))
                                if (1 if var13 < (1 if (1 if var2 <= 1 else 0) else (((((i32_load8_u((var5 + 13840)) & 0xFFFFFFFF) >> 4) * var16) - (var2 & 15)) + 8)) else 0):
                                    break
                                var6 = (var7 + 1)
                                if (1 if (var7 + 1) > (var20 - var13) else 0):
                                    break
                                var5 = (var13 + var24)
                                var11 = ((var13 + var24) - var2)
                                if (1 if var6 < 8 else 0):
                                    break
                                # br_table ['$label54', '$label55', '$label53', '$label56', '$label53']
                                _br_idx = (var2 - 1)
                                break  # br_table
                                break
                                break
                                var10 = i32_load(var11)
                                if (1 if (var5 & 3) == 0 else 0):
                                    var2 = var6
                                    break
                                i32_store8(var5, i32_load8_u(var11))
                                var10 = rotl32(var10, 24)
                                var11 = (var11 + 1)
                                var5 = (var5 + 1)
                                if (1 if ((var5 + 1) & 3) == 0 else 0):
                                    var3 = var6
                                    var2 = var7
                                    break
                                i32_store8(var5, i32_load8_u(var11))
                                var2 = (var7 - 1)
                                var10 = rotl32(var10, 24)
                                var11 = (var11 + 1)
                                var5 = (var5 + 1)
                                if (1 if ((var5 + 1) & 3) == 0 else 0):
                                    var3 = var7
                                    break
                                i32_store8(var5, i32_load8_u(var11))
                                var8 = (var7 - 2)
                                var10 = rotl32(var10, 24)
                                var11 = (var11 + 1)
                                var5 = (var5 + 1)
                                if ((var5 + 1) & 3):
                                    break
                                var3 = var2
                                var2 = var8
                                break
                                if (1 if var2 >= var6 else 0):
                                    break
                                if (1 if var7 > 2147483646 else 0):
                                    break
                                var3 = 0
                                var10 = 0
                                if (1 if var7 >= 3 else 0):
                                    var2 = (var6 & -4)
                                    var7 = 0
                                    while True:  # loop $label63
                                        i32_store8((var5 + var10), i32_load8_u((var10 + var11)))
                                        var8 = (var10 | 1)
                                        i32_store8((var5 + (var10 | 1)), i32_load8_u((var8 + var11)))
                                        var8 = (var10 | 2)
                                        i32_store8((var5 + (var10 | 2)), i32_load8_u((var8 + var11)))
                                        var8 = (var10 | 3)
                                        i32_store8((var5 + (var10 | 3)), i32_load8_u((var8 + var11)))
                                        var10 = (var10 + 4)
                                        var7 = (var7 + 4)
                                        if (1 if (var7 + 4) != var2 else 0):
                                            continue
                                        break  # end loop
                                var2 = (var6 & 3)
                                if (1 if (var6 & 3) == 0 else 0):
                                    break
                                while True:  # loop $label64
                                    i32_store8((var5 + var10), i32_load8_u((var10 + var11)))
                                    var10 = (var10 + 1)
                                    var3 = (var3 + 1)
                                    if (1 if (var3 + 1) != var2 else 0):
                                        continue
                                    break  # end loop
                                break
                            a_c()
                            raise RuntimeError('unreachable')
                            # Unknown: memory.copy []
                            break
                            i32_store8(var5, i32_load8_u(var11))
                            var2 = (var7 - 3)
                            var10 = rotl32(var10, 24)
                            var5 = (var5 + 1)
                            var11 = (var11 + 1)
                            var3 = var8
                            if (1 if var3 < 5 else 0):
                                break
                            var8 = ((var2 & 0xFFFFFFFF) >> 2)
                            var21 = (((var2 & 0xFFFFFFFF) >> 2) & 7)
                            var3 = 0
                            var7 = 0
                            if (1 if (var8 - 1) >= 7 else 0):
                                var36 = (var8 & 1073741816)
                                var28 = 0
                                while True:  # loop $label66
                                    var8 = (var7 << 2)
                                    i32_store((var5 + (var7 << 2)), var10)
                                    i32_store((var5 + (var8 | 4)), var10)
                                    i32_store((var5 + (var8 | 8)), var10)
                                    i32_store((var5 + (var8 | 12)), var10)
                                    i32_store((var5 + (var8 | 16)), var10)
                                    i32_store((var5 + (var8 | 20)), var10)
                                    i32_store((var5 + (var8 | 24)), var10)
                                    i32_store((var5 + (var8 | 28)), var10)
                                    var7 = (var7 + 8)
                                    var28 = (var28 + 8)
                                    if (1 if (var28 + 8) != var36 else 0):
                                        continue
                                    break  # end loop
                            if var21:
                                while True:  # loop $label67
                                    i32_store((var5 + (var7 << 2)), var10)
                                    var7 = (var7 + 1)
                                    var3 = (var3 + 1)
                                    if (1 if (var3 + 1) != var21 else 0):
                                        continue
                                    break  # end loop
                            var3 = (var2 & -4)
                            if (1 if (var2 & -4) >= var2 else 0):
                                break
                            var7 = (var2 + (var3 ^ -1))
                            var10 = 0
                            var8 = (var2 & 3)
                            if (var2 & 3):
                                while True:  # loop $label68
                                    i32_store8((var3 + var5), i32_load8_u((var3 + var11)))
                                    var3 = (var3 + 1)
                                    var10 = (var10 + 1)
                                    if (1 if (var10 + 1) != var8 else 0):
                                        continue
                                    break  # end loop
                            if (1 if var7 < 3 else 0):
                                break
                            while True:  # loop $label69
                                i32_store8((var3 + var5), i32_load8_u((var3 + var11)))
                                var7 = (var3 + 1)
                                i32_store8((var5 + (var3 + 1)), i32_load8_u((var7 + var11)))
                                var7 = (var3 + 2)
                                i32_store8((var5 + (var3 + 2)), i32_load8_u((var7 + var11)))
                                var7 = (var3 + 3)
                                i32_store8((var5 + (var3 + 3)), i32_load8_u((var7 + var11)))
                                var3 = (var3 + 4)
                                if (1 if (var3 + 4) != var2 else 0):
                                    continue
                                break  # end loop
                            var13 = (var6 + var13)
                            var12 = (var6 + var12)
                            if (1 if var16 <= (var6 + var12) else 0):
                                while True:  # loop $label71
                                    var12 = (var12 - var16)
                                    var2 = var4
                                    var4 = (var4 + 1)
                                    if (1 if var2 >= var14 else 0):
                                        break
                                    if (var4 & 15):
                                        break
                                    if (1 if var12 >= var16 else 0):
                                        continue
                                    break  # end loop
                            if (1 if var13 >= var25 else 0):
                                break
                            if (1 if (var12 & var23) == 0 else 0):
                                break
                            var2 = i32_load(var9 + 152)
                            if i32_load(var9 + 152):
                            else:
                            var2 = 0
                            if (1 if 0 >= i32_load(var9 + 164) else 0):
                                break
                            var17 = (i32_load(var9 + 168) + (var2 * 548))
                            var2 = i32_load(var9 + 40)
                            var3 = i32_load(var9 + 36)
                            if (1 if i32_load(var9 + 40) > i32_load(var9 + 36) else 0):
                                break
                            if i32_load(var9 + 48):
                                i32_store(var9 + 48, 1)
                                break
                            var5 = 0
                            if (1 if var2 == var3 else 0):
                                var5 = (1 if i32_load(var9 + 44) > 64 else 0)
                            i32_store(var9 + 48, var5)
                            if var5:
                                break
                            if (1 if var13 < var25 else 0):
                                continue
                            break  # end loop
                        var11 = 0
                        var4 = i32_load(var9 + 40)
                        var2 = i32_load(var9 + 36)
                        if (1 if i32_load(var9 + 40) <= i32_load(var9 + 36) else 0):
                            if i32_load(var9 + 48):
                                break
                            if (1 if var2 != var4 else 0):
                                break
                            var4 = (1 if i32_load(var9 + 44) > 64 else 0)
                            i32_store(var9 + 48, (1 if i32_load(var9 + 44) > 64 else 0))
                            if (1 if var11 == 0 else 0):
                                if (1 if var4 == 0 else 0):
                                    break
                                if (1 if var13 >= var20 else 0):
                                    break
                            var12 = 0
                            # br_table ['$label76', '$label42', '$label42', '$label42', '$label42', '$label76', '$label42']
                            _br_idx = i32_load(var9)
                            break  # br_table
                            i32_store(var9, (5 if var4 else 3))
                            break
                            i32_store(var9 + 112, var13)
                            break
                        break
                    a_c()
                    raise RuntimeError('unreachable')
                a_c()
                raise RuntimeError('unreachable')
                break
            a_c()
            raise RuntimeError('unreachable')
        a_c()
        raise RuntimeError('unreachable')
        var12 = func275(var9, i32_load(var9 + 16), i32_load(var9 + 100), i32_load(var9 + 104), var14, 277)
        break
        a_c()
        raise RuntimeError('unreachable')
        a_c()
        raise RuntimeError('unreachable')
        if (1 if 3953 == 0 else 0):
            break
        if (1 if var14 >= var31 else 0):
            i32_store(var0 + 2400, 1)
            break
        if (1 if i32_load(var0 + 2400) == 0 else 0):
            break
        var4 = i32_load(var0 + 2388)
        if i32_load(var0 + 2388):
            func190(i32_load(var4 + 20))
            i32_store(var4 + 20, 0)
        i32_store(var0 + 2388, 0)
        var4 = i32_load(var0 + 2416)
        if (1 if i32_load(var0 + 2416) <= 0 else 0):
            break
        var2 = i32_load(var1 + 76)
        var3 = i32_load(var1 + 84)
        var7 = (i32_load(var1 + 76) + (i32_load(var0 + 2408) + (i32_load(var1 + 84) * var30)))
        var16 = (i32_load(var1 + 80) - var2)
        var23 = (i32_load(var1 + 88) - var3)
        var6 = 0
        var10 = 0
        var31 = 0
        var25 = (global0 - 256)
        global global0
        global0 = (global0 - 256)
        var2 = (var4 // 25)
        if (1 if var4 > 100 else 0):
            break
        if (1 if var7 == 0 else 0):
            break
        if (1 if var16 <= 0 else 0):
            break
        if (1 if var23 <= 0 else 0):
            break
        var6 = 1
        var42 = (var23 - 1)
        var36 = (var16 - 1)
        var4 = ((((var16 - 1) & 0xFFFFFFFF) >> 1) if (1 if ((var2 << 1) | 1) > var16 else 0) else var2)
        var13 = ((((var23 - 1) & 0xFFFFFFFF) >> 1) if (1 if ((var4 << 1) | 1) > var23 else 0) else ((((var16 - 1) & 0xFFFFFFFF) >> 1) if (1 if ((var2 << 1) | 1) > var16 else 0) else var2))
        if (1 if ((((var23 - 1) & 0xFFFFFFFF) >> 1) if (1 if ((var4 << 1) | 1) > var23 else 0) else ((((var16 - 1) & 0xFFFFFFFF) >> 1) if (1 if ((var2 << 1) | 1) > var16 else 0) else var2)) <= 0 else 0):
            break
        var6 = 0
        var20 = (var16 << 1)
        var19 = (var13 << 1)
        var2 = (var20 * ((var13 << 1) + 2))
        var9 = func58(1, (((var16 << 1) + (var20 * ((var13 << 1) + 2))) + 4094))
        if (1 if func58(1, (((var16 << 1) + (var20 * ((var13 << 1) + 2))) + 4094)) == 0 else 0):
            break
        var24 = (0 - var13)
        var4 = (var19 | 1)
        var12 = (var9 + (((var19 | 1) * var16) << 1))
        var11 = ((var9 + (((var19 | 1) * var16) << 1)) - var20)
        # Unknown: memory.fill []
        # Unknown: memory.fill []
        var17 = (var2 + var9)
        var18 = (var4 * var4)
        var28 = 255
        var3 = 0
        var14 = 255
        var4 = var7
        while True:  # loop $label81
            var6 = var3
            var8 = var14
            var2 = 0
            while True:  # loop $label80
                var5 = i32_load8_u((var2 + var4))
                i32_store8((var25 + i32_load8_u((var2 + var4))), 1)
                var21 = (1 if var5 > var6 else 0)
                var3 = (var5 if (1 if var5 > var6 else 0) else var3)
                var31 = (var5 if var21 else var31)
                var21 = (1 if var5 < var8 else 0)
                var14 = (var5 if (1 if var5 < var8 else 0) else var14)
                var28 = (var5 if var21 else var28)
                var6 = (var6 if (1 if var5 < var6 else 0) else var5)
                var8 = (var8 if (1 if var5 > var8 else 0) else var5)
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != var16 else 0):
                    continue
                break  # end loop
            var4 = (var4 + var30)
            var10 = (var10 + 1)
            if (1 if (var10 + 1) != var23 else 0):
                continue
            break  # end loop
        var8 = (var3 - var14)
        var5 = (var17 + var20)
        var6 = -1
        var2 = 0
        var4 = 0
        while True:  # loop $label83
            if i32_load8_u((var4 + var25)):
                var2 = (var2 + 1)
                if (1 if var6 >= 0 else 0):
                    var3 = (var4 - var6)
                    var8 = ((var4 - var6) if (1 if var3 < var8 else 0) else var8)
            else:
            var3 = var6
            var6 = (var4 | 1)
            if (1 if i32_load8_u((var25 + (var4 | 1))) == 0 else 0):
                var6 = var3
                break
            var2 = (var2 + 1)
            if (1 if var3 < 0 else 0):
                break
            var3 = (var6 - var3)
            var8 = ((var6 - var3) if (1 if var3 < var8 else 0) else var8)
            var4 = (var4 + 2)
            if (1 if (var4 + 2) != 256 else 0):
                continue
            break  # end loop
        var3 = (var8 << 2)
        var6 = ((var8 * 12) >> 2)
        var8 = ((var8 << 2) - ((var8 * 12) >> 2))
        var21 = (var5 + 2046)
        var4 = 1
        while True:  # loop $label85
            var5 = (var4 << 1)
            if (1 if var4 <= var6 else 0):
                break
            if (1 if var3 <= var4 else 0):
                break
            var14 = (((((var3 - var4) * var6) // var8) & 0xFFFFFFFF) >> 2)
            i32_store16((var21 + (var4 << 1)), (((((var3 - var4) * var6) // var8) & 0xFFFFFFFF) >> 2))
            i32_store16((var21 - var5), (0 - var14))
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != 1024 else 0):
                continue
            break  # end loop
        i32_store16(var21, 0)
        var18 = ((262144 & 0xFFFFFFFF) // var18)
        if (1 if var2 < 3 else 0):
            break
        if (1 if var23 <= var24 else 0):
            break
        var10 = (var13 + 2)
        var40 = (var16 & 1)
        var43 = (var16 & -2)
        var44 = (var20 - 2)
        var20 = (var13 ^ -1)
        var5 = (var16 - var13)
        var41 = (var13 - 1)
        var8 = (var13 + 1)
        var45 = ((var13 + 1) & -2)
        var46 = (var8 & 1)
        var47 = (var12 + (var36 << 1))
        var48 = (var17 + (var8 << 1))
        var49 = (var12 + ((var8 + var13) << 1))
        var50 = (1 if (var16 - 2) == var19 else 0)
        var2 = var9
        var3 = var7
        while True:  # loop $label94
            var14 = 0
            var4 = 0
            var6 = 0
            if var36:
                while True:  # loop $label87
                    var19 = (var4 << 1)
                    var14 = (i32_load8_u((var3 + var4)) + (var14 & 65535))
                    var32 = ((i32_load8_u((var3 + var4)) + (var14 & 65535)) + i32_load16_u((var11 + var19)))
                    var19 = (var2 + var19)
                    i32_store16((var12 + (var4 << 1)), (((i32_load8_u((var3 + var4)) + (var14 & 65535)) + i32_load16_u((var11 + var19))) - i32_load16_u((var2 + var19))))
                    i32_store16(var19, var32)
                    var32 = (var4 | 1)
                    var19 = ((var4 | 1) << 1)
                    var14 = (i32_load8_u((var3 + var32)) + (var14 & 65535))
                    var32 = ((i32_load8_u((var3 + var32)) + (var14 & 65535)) + i32_load16_u((var11 + var19)))
                    var19 = (var2 + var19)
                    i32_store16((var12 + ((var4 | 1) << 1)), (((i32_load8_u((var3 + var32)) + (var14 & 65535)) + i32_load16_u((var11 + var19))) - i32_load16_u((var2 + var19))))
                    i32_store16(var19, var32)
                    var4 = (var4 + 2)
                    var6 = (var6 + 2)
                    if (1 if (var6 + 2) != var43 else 0):
                        continue
                    break  # end loop
            if var40:
                var6 = (var4 << 1)
                var4 = (i32_load16_u((var6 + var11)) + (var14 + i32_load8_u((var3 + var4))))
                var6 = (var2 + var6)
                i32_store16((var12 + (var4 << 1)), ((i32_load16_u((var6 + var11)) + (var14 + i32_load8_u((var3 + var4)))) - i32_load16_u((var2 + var6))))
                i32_store16(var6, var4)
            var14 = (var2 + (var16 << 1))
            var19 = (1 if (var2 + (var16 << 1)) == var12 else 0)
            var4 = 0
            var6 = 0
            if (1 if var13 <= var24 else 0):
                while True:  # loop $label88
                    i32_store16((var17 + (var4 << 1)), (((var18 * ((i32_load16_u((var12 + ((var13 - var4) << 1))) + i32_load16_u((var12 + ((var4 + var41) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                    var11 = (var4 | 1)
                    i32_store16((var17 + ((var4 | 1) << 1)), (((var18 * ((i32_load16_u((var12 + ((var13 - var11) << 1))) + i32_load16_u((var12 + ((var4 + var13) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                    var4 = (var4 + 2)
                    var6 = (var6 + 2)
                    if (1 if (var6 + 2) != var45 else 0):
                        continue
                    break  # end loop
                if var46:
                    i32_store16((var17 + (var4 << 1)), (((var18 * ((i32_load16_u((var12 + ((var13 - var4) << 1))) + i32_load16_u((var12 + ((var4 + var41) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                var4 = var8
                if (1 if var8 >= var5 else 0):
                    break
                var6 = var8
                if (1 if var40 == 0 else 0):
                    i32_store16(var48, (((var18 * ((i32_load16_u(var49) - i32_load16_u(var12)) & 65535)) & 0xFFFFFFFF) >> 16))
                    var6 = var10
                var4 = var5
                if var50:
                    break
                while True:  # loop $label90
                    i32_store16((var17 + (var6 << 1)), (((var18 * ((i32_load16_u((var12 + ((var6 + var13) << 1))) - i32_load16_u((var12 + ((var6 + var20) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                    var4 = (var6 + 1)
                    i32_store16((var17 + ((var6 + 1) << 1)), (((var18 * ((i32_load16_u((var12 + ((var4 + var13) << 1))) - i32_load16_u((var12 + ((var6 - var13) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                    var6 = (var6 + 2)
                    if (1 if (var6 + 2) != var5 else 0):
                        continue
                    break  # end loop
                var4 = var5
                if (1 if var4 < var16 else 0):
                    while True:  # loop $label91
                        i32_store16((var17 + (var4 << 1)), (((var18 * (((i32_load16_u(var47) << 1) - (i32_load16_u((var12 + ((var44 - (var4 + var13)) << 1))) + i32_load16_u((var12 + ((var4 + var20) << 1))))) & 65535)) & 0xFFFFFFFF) >> 16))
                        var4 = (var4 + 1)
                        if (1 if (var4 + 1) != var16 else 0):
                            continue
                        break  # end loop
                var4 = 0
                while True:  # loop $label93
                    var11 = (var4 + var7)
                    var6 = i32_load8_u((var4 + var7))
                    if (1 if var31 <= i32_load8_u((var4 + var7)) else 0):
                        break
                    if (1 if var6 <= var28 else 0):
                        break
                    var6 = (i32_load16_s((var21 + ((i32_load16_u((var17 + (var4 << 1))) - (var6 << 2)) << 1))) + var6)
                    var6 = ((i32_load16_s((var21 + ((i32_load16_u((var17 + (var4 << 1))) - (var6 << 2)) << 1))) + var6) if (1 if var6 > 0 else 0) else 0)
                    i32_store8(var11, (255 if (1 if var6 >= 255 else 0) else ((i32_load16_s((var21 + ((i32_load16_u((var17 + (var4 << 1))) - (var6 << 2)) << 1))) + var6) if (1 if var6 > 0 else 0) else 0)))
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != var16 else 0):
                        continue
                    break  # end loop
                var7 = (var7 + var30)
            var3 = (((var30 if (1 if var24 < var42 else 0) else 0) if (1 if var24 >= 0 else 0) else 0) + var3)
            var11 = var2
            var2 = (var9 if var19 else var14)
            var24 = (var24 + 1)
            if (1 if (var24 + 1) != var23 else 0):
                continue
            break  # end loop
        var6 = 1
        global global0
        global0 = (var25 + 256)
        if (1 if var6 == 0 else 0):
            break
        var2 = (i32_load(var0 + 2408) + (var15 * var30))
        break
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    i64_store(var0 + 2404, 0)
    var4 = i32_load(var0 + 2388)
    if i32_load(var0 + 2388):
        func190(i32_load(var4 + 20))
        i32_store(var4 + 20, 0)
    i32_store(var0 + 2388, 0)
    var4 = 0
    i32_store(af(var4) + 104, 0)
    if (1 if var4 == 0 else 0):
        break
    var2 = i32_load(var1 + 84)
    if (1 if var15 < i32_load(var1 + 84) else 0):
        var3 = (var2 - var15)
        if ((var2 - var15) & 1):
            break
        i32_store(var1 + 20, (i32_load(var1 + 20) + (i32_load(var0 + 2324) * var3)))
        var7 = (i32_load(var0 + 2328) * (var3 >> 1))
        i32_store(var1 + 24, ((i32_load(var0 + 2328) * (var3 >> 1)) + i32_load(var1 + 24)))
        i32_store(var1 + 28, (i32_load(var1 + 28) + var7))
        if (1 if var4 == 0 else 0):
            var4 = 0
            break
        var4 = (var4 + (i32_load(var1) * var3))
        i32_store(var1 + 104, (var4 + (i32_load(var1) * var3)))
        var15 = var2
    if (1 if var15 >= var35 else 0):
        break
    var3 = i32_load(var1 + 76)
    i32_store(var1 + 20, (i32_load(var1 + 76) + i32_load(var1 + 20)))
    var7 = (var3 >> 1)
    i32_store(var1 + 24, ((var3 >> 1) + i32_load(var1 + 24)))
    i32_store(var1 + 28, (i32_load(var1 + 28) + var7))
    if var4:
        i32_store(var1 + 104, (var3 + var4))
    i32_store(var1 + 8, (var15 - var2))
    i32_store(var1 + 16, (var35 - var15))
    i32_store(var1 + 12, (i32_load(var1 + 80) - var3))
    # call_indirect via table[i32_load(var1 + 44)]
    var2 = call_indirect(i32_load(var1 + 44))
    if (1 if i32_load(var0 + 168) != (var37 + 1) else 0):
        break
    if (1 if var33 >= var39 else 0):
        break
    # Unknown: memory.copy []
    var1 = (0 - var34)
    # Unknown: memory.copy []
    # Unknown: memory.copy []
    break
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    var2 = func99(var0, 3, 8467)
    global global0
    global0 = (var29 - -64)
    return var2

