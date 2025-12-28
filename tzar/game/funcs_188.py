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
# $func315
# ==========================================================
def func315(var0, var1, var2):
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
    var9 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = i32_load(9142892)
    if ((1 if var1 != 2147483647 else 0) & (1 if i32_load(9142892) <= var1 else 0)):
        break
    var11 = i32_load(var0 + 16)
    # br_table ['$label1', '$label2', '$label3', '$label4']
    _br_idx = i32_load(var0 + 4)
    break  # br_table
    var8 = i32_load(var0 + 88)
    if (1 if i32_load(var0 + 88) == 0 else 0):
        break
    var6 = i32_load(var0 + 12)
    if (1 if i32_load(var0 + 12) == 0 else 0):
        break
    var5 = ((var11 * 404) + 9568096)
    var2 = 0
    var4 = var6
    while True:  # loop $label8
        if (1 if var4 == 0 else 0):
            var4 = 0
            break
        var3 = 0
        var7 = (var2 << 2)
        if (1 if i32_load8_u((i32_load(9671128) + (i32_load(((var2 << 2) + i32_load(var0 + 80))) * 132)) + 125) == 3 else 0):
            break
        while True:  # loop $label7
            var4 = (i32_load(9671128) + (i32_load((i32_load(var0 + 80) + var7)) * 132))
            if (1 if i32_load8_u((i32_load(9671128) + (i32_load((i32_load(var0 + 80) + var7)) * 132)) + 125) != 3 else 0):
                if (1 if func59((var9 + 12), (var9 + 8), var4, var5) == 0 else 0):
                    break
                var4 = func34(var11, var1, i32_load(var9 + 12), i32_load(var9 + 8), 0, 1)
                if (1 if func34(var11, var1, i32_load(var9 + 12), i32_load(var9 + 8), 0, 1) == 0 else 0):
                    break
                if (1 if i32_load(var0 + 104) < 7 else 0):
                    break
                func148(var4, i32_load(var0 + 96), 0)
                var6 = i32_load(var0 + 12)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) < var6 else 0):
                continue
            break  # end loop
        var8 = i32_load(var0 + 88)
        var4 = var6
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var8 else 0):
            continue
        break  # end loop
    break
    if (1 if var3 == 0 else 0):
        break
    var17 = ((var11 * 404) + 9568096)
    var2 = i32_load(var0 + 36)
    if (1 if i32_load(var0 + 36) <= 3 else 0):
        var14 = (var2 - 1)
        while True:  # loop $label23
            var2 = i32_load(var0 + 64)
            var4 = (var8 << 2)
            if (1 if i32_load((i32_load(var0 + 64) + (var8 << 2))) == 0 else 0):
                if (1 if i32_load((var2 + (var3 << 2))) == 0 else 0):
                    break
                if (1 if i32_load((i32_load(9142420) + var4)) == 0 else 0):
                    break
            var5 = 0
            var15 = i32_load(9561692)
            while True:  # loop $label22
                # br_table ['$label10', '$label11', '$label12', '$label13']
                _br_idx = var14
                break  # br_table
                if (1 if i32_load(((var5 * 404) + 9568096) + 264) == 1 else 0):
                    break
                break
                if (1 if i32_load(((var5 * 404) + 9568096) + 264) == 0 else 0):
                    break
                break
                var2 = ((var5 * 404) + 9568096)
                if i32_load(((var5 * 404) + 9568096) + 264):
                    break
                if (1 if i32_load(var2 + 268) == 1 else 0):
                    break
                if (1 if i32_load(var2 + 92) == 0 else 0):
                    break
                if (1 if i32_load(38456) == var5 else 0):
                    break
                if (1 if i32_load(38764) == var5 else 0):
                    break
                var13 = i32_load((((var15 + (var8 * 286704)) + (var5 << 2)) + 284636))
                if (1 if i32_load((((var15 + (var8 * 286704)) + (var5 << 2)) + 284636)) == 0 else 0):
                    break
                var10 = 0
                var12 = i32_load(var13 + 8)
                if (1 if i32_load(var13 + 8) == 0 else 0):
                    break
                while True:  # loop $label21
                    var2 = i32_load((i32_load(var13) + (var10 << 2)))
                    if (1 if i32_load((i32_load(var13) + (var10 << 2))) == 0 else 0):
                        break
                    if (1 if i32_load(var0 + 12) == 0 else 0):
                        break
                    var6 = 0
                    var18 = (i32_load(9671128) + (var2 * 132))
                    while True:  # loop $label20
                        if (1 if func59((var9 + 12), (var9 + 8), var18, var17) == 0 else 0):
                            break
                        var2 = func34(var11, var1, i32_load(var9 + 12), i32_load(var9 + 8), 0, 1)
                        if (1 if func34(var11, var1, i32_load(var9 + 12), i32_load(var9 + 8), 0, 1) == 0 else 0):
                            break
                        if (1 if i32_load(var0 + 104) < 7 else 0):
                            break
                        var3 = (i32_load(9671128) + (var2 * 132))
                        var7 = i32_load(var0 + 96)
                        var2 = i32_load(i32_load(var0 + 96))
                        if (1 if i32_load(i32_load(var0 + 96)) <= 2147483646 else 0):
                            i32_store(var3 + 52, var2)
                        var2 = i32_load(var7 + 4)
                        if (1 if i32_load(var7 + 4) <= 2147483646 else 0):
                            i32_store(var3 + 60, var2)
                        var2 = i32_load(var7 + 8)
                        if (1 if i32_load(var7 + 8) > 2147483646 else 0):
                            break
                        i32_store(var3 + 64, var2)
                        if (1 if i32_load(var7 + 8) > 2147483646 else 0):
                            break
                        i32_store(var3 + 68, i32_load(var7 + 12))
                        var4 = i32_load(var3 + 76)
                        var2 = i32_load(var3 + 76)
                        var16 = i32_load(var7 + 16)
                        if (1 if i32_load(var7 + 16) > 2147483646 else 0):
                            break
                        i32_store(var3 + 72, var16)
                        if (1 if i32_load(var7 + 16) > 2147483646 else 0):
                            break
                        var2 = i32_load(var7 + 20)
                        i32_store(var3 + 76, i32_load(var7 + 20))
                        var7 = i32_load(var7 + 24)
                        if (1 if i32_load(var7 + 24) <= 2147483646 else 0):
                            i32_store(var3 + 84, var7)
                        var16 = ((i32_load8_u(var3 + 122) * 404) + 9568096)
                        var7 = i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 264)
                        if (1 if i32_load(var16 + 92) == 0 else 0):
                            if (1 if var7 == 2 else 0):
                                break
                            i32_store(var3 + 52, 0)
                        if (1 if var7 != 1 else 0):
                            break
                        var2 = 0
                        i32_store(var3 + 72, 0)
                        i32_store(var3 + 60, 0)
                        i32_store(var3 + 76, 0)
                        i32_store(var3 + 84, 0)
                        if (1 if i32_load(var3 + 64) == 0 else 0):
                            i32_store((var3 - -64), -1)
                        if (1 if var2 == 0 else 0):
                            break
                        if var4:
                            break
                        var6 = (var6 + 1)
                        if (1 if (var6 + 1) < i32_load(var0 + 12) else 0):
                            continue
                        break  # end loop
                    var10 = (var10 + 1)
                    if (1 if (var10 + 1) != var12 else 0):
                        continue
                    break  # end loop
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != 255 else 0):
                    continue
                break  # end loop
            var3 = i32_load(9142892)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) < var3 else 0):
                continue
            break  # end loop
        break
    var13 = ((var2 - 4) << 2)
    while True:  # loop $label32
        var2 = i32_load(var0 + 64)
        var4 = (var8 << 2)
        if (1 if i32_load((i32_load(var0 + 64) + (var8 << 2))) == 0 else 0):
            if (1 if i32_load((var2 + (var3 << 2))) == 0 else 0):
                break
            if (1 if i32_load((i32_load(9142420) + var4)) == 0 else 0):
                break
        var7 = i32_load((((i32_load(9561692) + (var8 * 286704)) + var13) + 284636))
        if (1 if i32_load((((i32_load(9561692) + (var8 * 286704)) + var13) + 284636)) == 0 else 0):
            break
        var10 = 0
        var14 = i32_load(var7 + 8)
        if (1 if i32_load(var7 + 8) == 0 else 0):
            break
        while True:  # loop $label31
            var2 = i32_load((i32_load(var7) + (var10 << 2)))
            if (1 if i32_load((i32_load(var7) + (var10 << 2))) == 0 else 0):
                break
            if (1 if i32_load(var0 + 12) == 0 else 0):
                break
            var6 = 0
            var15 = (i32_load(9671128) + (var2 * 132))
            while True:  # loop $label30
                if (1 if func59((var9 + 12), (var9 + 8), var15, var17) == 0 else 0):
                    break
                var2 = func34(var11, var1, i32_load(var9 + 12), i32_load(var9 + 8), 0, 1)
                if (1 if func34(var11, var1, i32_load(var9 + 12), i32_load(var9 + 8), 0, 1) == 0 else 0):
                    break
                if (1 if i32_load(var0 + 104) < 7 else 0):
                    break
                var3 = (i32_load(9671128) + (var2 * 132))
                var5 = i32_load(var0 + 96)
                var2 = i32_load(i32_load(var0 + 96))
                if (1 if i32_load(i32_load(var0 + 96)) <= 2147483646 else 0):
                    i32_store(var3 + 52, var2)
                var2 = i32_load(var5 + 4)
                if (1 if i32_load(var5 + 4) <= 2147483646 else 0):
                    i32_store(var3 + 60, var2)
                var2 = i32_load(var5 + 8)
                if (1 if i32_load(var5 + 8) > 2147483646 else 0):
                    break
                i32_store(var3 + 64, var2)
                if (1 if i32_load(var5 + 8) > 2147483646 else 0):
                    break
                i32_store(var3 + 68, i32_load(var5 + 12))
                var4 = i32_load(var3 + 76)
                var2 = i32_load(var3 + 76)
                var12 = i32_load(var5 + 16)
                if (1 if i32_load(var5 + 16) > 2147483646 else 0):
                    break
                i32_store(var3 + 72, var12)
                if (1 if i32_load(var5 + 16) > 2147483646 else 0):
                    break
                var2 = i32_load(var5 + 20)
                i32_store(var3 + 76, i32_load(var5 + 20))
                var5 = i32_load(var5 + 24)
                if (1 if i32_load(var5 + 24) <= 2147483646 else 0):
                    i32_store(var3 + 84, var5)
                var12 = ((i32_load8_u(var3 + 122) * 404) + 9568096)
                var5 = i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 264)
                if (1 if i32_load(var12 + 92) == 0 else 0):
                    if (1 if var5 == 2 else 0):
                        break
                    i32_store(var3 + 52, 0)
                if (1 if var5 != 1 else 0):
                    break
                var2 = 0
                i32_store(var3 + 72, 0)
                i32_store(var3 + 60, 0)
                i32_store(var3 + 76, 0)
                i32_store(var3 + 84, 0)
                if (1 if i32_load(var3 + 64) == 0 else 0):
                    i32_store((var3 - -64), -1)
                if (1 if var2 == 0 else 0):
                    break
                if var4:
                    break
                var6 = (var6 + 1)
                if (1 if (var6 + 1) < i32_load(var0 + 12) else 0):
                    continue
                break  # end loop
            var10 = (var10 + 1)
            if (1 if (var10 + 1) != var14 else 0):
                continue
            break  # end loop
        var3 = i32_load(9142892)
        var8 = (var8 + 1)
        if (1 if (var8 + 1) < var3 else 0):
            continue
        break  # end loop
    break
    var8 = i32_load(9140300)
    if (1 if i32_load(9140300) == 0 else 0):
        break
    var5 = ((var11 * 404) + 9568096)
    var4 = i32_load(var0 + 12)
    while True:  # loop $label36
        var3 = 0
        var7 = (i32_load(9671128) + (i32_load(((var6 << 2) + 8451904)) * 132))
        var10 = i32_load16_u((i32_load(9671128) + (i32_load(((var6 << 2) + 8451904)) * 132)) + 110)
        if (1 if (((1 if i32_load((i32_load(9142420) + (i32_load16_u((i32_load(9671128) + (i32_load(((var6 << 2) + 8451904)) * 132)) + 110) << 2))) != 0 else 0) & (1 if var1 == var10 else 0)) | var2) != 1 else 0):
            break
        if (1 if var4 == 0 else 0):
            break
        while True:  # loop $label35
            if (1 if func59((var9 + 12), (var9 + 8), var7, var5) == 0 else 0):
                break
            var4 = func34(var11, var1, i32_load(var9 + 12), i32_load(var9 + 8), 0, 1)
            if (1 if func34(var11, var1, i32_load(var9 + 12), i32_load(var9 + 8), 0, 1) == 0 else 0):
                break
            if (1 if i32_load(var0 + 104) < 7 else 0):
                break
            func148(var4, i32_load(var0 + 96), 0)
            var3 = (var3 + 1)
            var4 = i32_load(var0 + 12)
            if (1 if (var3 + 1) < i32_load(var0 + 12) else 0):
                continue
            break  # end loop
        var8 = i32_load(9140300)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) < var8 else 0):
            continue
        break  # end loop
    break
    if (1 if i32_load(var0 + 12) == 0 else 0):
        break
    var10 = ((var11 * 404) + 9568096)
    var2 = 0
    while True:  # loop $label41
        var8 = i32_load(var0 + 20)
        var3 = 0
        var5 = i32_load(var0 + 28)
        if i32_load(var0 + 28):
            var19 = i64_load(9147316)
            var4 = i32_load(9147312)
            i32_store(9147316, i32_load(9147312))
            var6 = i32_load(9147324)
            i64_store(9147320, var19)
            var6 = (var6 ^ (var6 << 11))
            var4 = ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var6 ^ (var6 << 11)) & 0xFFFFFFFF) >> 8))) ^ var6)
            i32_store(9147312, ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var6 ^ (var6 << 11)) & 0xFFFFFFFF) >> 8))) ^ var6))
        else:
        var8 = (0 + var8)
        var3 = i32_load(var0 + 24)
        var5 = i32_load(var0 + 40)
        if i32_load(var0 + 40):
            var19 = i64_load(9147316)
            var4 = i32_load(9147312)
            i32_store(9147316, i32_load(9147312))
            var6 = i32_load(9147324)
            i64_store(9147320, var19)
            var6 = (var6 ^ (var6 << 11))
            var4 = ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var6 ^ (var6 << 11)) & 0xFFFFFFFF) >> 8))) ^ var6)
            i32_store(9147312, ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var6 ^ (var6 << 11)) & 0xFFFFFFFF) >> 8))) ^ var6))
        else:
        var5 = (0 + var3)
        if func56((var4 % var5), (0 + var3), var10, var1, 0, 0, 1, 1, 0):
            var3 = var8
            var4 = var5
            break
        var4 = 0
        var6 = i32_load(9142440)
        while True:  # loop $label39
            var7 = var4
            var3 = (var4 << 2)
            var4 = (i32_load((((var4 << 2) | 4) + 8611904)) + var5)
            if (1 if var6 <= (i32_load((((var4 << 2) | 4) + 8611904)) + var5) else 0):
                break
            var3 = (i32_load((var3 + 8611904)) + var8)
            if (1 if var6 <= (i32_load((var3 + 8611904)) + var8) else 0):
                break
            if (1 if (var3 | var4) < 0 else 0):
                break
            if func56(var3, var4, var10, var1, 0, 0, 1, 1, 0):
                break
            var6 = i32_load(9142440)
            var4 = (var7 + 2)
            if (1 if var7 < 5198 else 0):
                continue
            break  # end loop
        break
        var4 = func34(var11, var1, var3, var4, 0, 1)
        if (1 if func34(var11, var1, var3, var4, 0, 1) == 0 else 0):
            break
        if (1 if i32_load(var0 + 104) < 7 else 0):
            break
        func148(var4, i32_load(var0 + 96), 0)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < i32_load(var0 + 12) else 0):
            continue
        break  # end loop
    global global0
    global0 = (var9 + 16)
    return var8

