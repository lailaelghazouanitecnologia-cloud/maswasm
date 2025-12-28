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
# $func355
# ==========================================================
def func355(var0, var1, var2):
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
    var13 = 0.0
    var14 = 0
    var9 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    var6 = (var1 // 32)
    var3 = i32_load(9681892)
    var4 = i32_load(9142880)
    var7 = (var0 // 32)
    if (1 if (var0 // 32) != i32_load(9687260) else 0):
        break
    if (1 if var6 != i32_load(9687264) else 0):
        break
    if var2:
        break
    if (1 if var3 >= 0 else 0):
        break
    i32_store(9687264, var6)
    i32_store(9687260, var7)
    if (1 if var3 < 0 else 0):
        var3 = (i32_load(9681888) << 4)
        var5 = (var1 - (i32_load(9681888) << 4))
        var3 = (var0 - var3)
        if (1 if i32_load8_u(9142916) == 0 else 0):
            break
        break
    var3 = (i32_load(9681888) << 4)
    var5 = ((var6 << 5) - (i32_load(9681888) << 4))
    var3 = ((var7 << 5) - var3)
    if (1 if i32_load8_u(9142916) == 0 else 0):
        break
    var13 = ((0.0 / float((i32_load(9142440) * 96))) + 0.25)
    i32_store(var9 + 72, var4)
    f64_store((var9 - -64), float(var13))
    f64_store(var9 + 56, float(float(var5)))
    f64_store(var9 + 48, float(float(var3)))
    a_b()
    if (1 if i32_load8_u(9142916) == 0 else 0):
        i64_store(var9 + 16, 0)
        i64_store(var9 + 24, 0)
        i32_store(var9 + 32, var4)
        var13 = f32((float((i32_load(9681888) << 5)) + 0.5))
        f64_store(var9 + 8, float(f32((float((i32_load(9681888) << 5)) + 0.5))))
        f64_store(var9, float((-var13)))
        a_b()
    if (1 if (((1 if i32_load(9142900) == 0 else 0) & (1 if i32_load8_u(9142409) != 0 else 0)) | var2) == 0 else 0):
        break
    var2 = i32_load(9681892)
    if (1 if i32_load(9681892) < 0 else 0):
        var0 = i32_load(9681888)
        var2 = (i32_load(9681888) << 4)
        func401((var0 - (i32_load(9681888) << 4)), (var1 - var2), (var0 << 5))
        break
    var0 = i32_load(9681888)
    var1 = (i32_load(9681888) // 2)
    var6 = (var6 - (i32_load(9681888) // 2))
    var7 = (var7 - var1)
    if i32_load8_u(9681885):
        if (1 if i32_load(i32_load((i32_load(9140332) + (var2 << 2))) + 32) != 23 else 0):
            break
        func401((var7 << 5), (var6 << 5), (var0 << 5))
        var2 = i32_load(9681888)
        if (1 if i32_load(9681888) <= 0 else 0):
            break
        var8 = (var2 + var6)
        var10 = (var2 + var7)
        var1 = i32_load(9142440)
        var0 = var7
        while True:  # loop $label9
            var3 = (var0 + 1)
            var2 = var6
            while True:  # loop $label8
                if (1 if var1 <= var2 else 0):
                    break
                if (1 if (var0 | var2) < 0 else 0):
                    break
                if (1 if var0 < var1 else 0):
                    break
                break
                var5 = i32_load(9142840)
                var1 = (var1 + 2)
                var4 = (var2 + 1)
                var11 = (i32_load(9142840) + ((((var1 + 2) * (var2 + 1)) + var3) << 2))
                if (1 if i32_load((i32_load(9142840) + ((((var1 + 2) * (var2 + 1)) + var3) << 2))) == 0 else 0):
                    i32_store(var11, 1)
                    var1 = (i32_load(9142440) + 2)
                var1 = (((var1 + var4) * var1) + var3)
                var11 = i32_load((var5 + ((((var1 + var4) * var1) + var3) << 2)))
                if (1 if i32_load((var5 + ((((var1 + var4) * var1) + var3) << 2))) >= 3 else 0):
                    var5 = i32_load(9142840)
                    var1 = (i32_load(9142440) + 2)
                else:
                i32_store(((var1 << 2) + var5), 1)
                i32_store8((i32_load(9147288) + ((i32_load(9142440) * var2) + var0)), i32_load(9681892))
                var1 = i32_load(9142440)
                var2 = var4
                if (1 if ((((i32_load(9142440) + 2) + var4) * var1) + var3) > var4 else 0):
                    continue
                break  # end loop
            var0 = var3
            if (1 if var3 < var10 else 0):
                continue
            break  # end loop
        break
    if (1 if var0 <= 0 else 0):
        break
    var4 = (var0 + var6)
    var5 = (var0 + var7)
    var1 = i32_load(9142440)
    var0 = var7
    while True:  # loop $label15
        var3 = (var0 + 1)
        var2 = var6
        while True:  # loop $label14
            if (1 if var1 <= var2 else 0):
                break
            if (1 if (var0 | var2) < 0 else 0):
                break
            if (1 if var0 < var1 else 0):
                break
            var2 = (var2 + 1)
            break
            var2 = (var2 + 1)
            var8 = (var1 + 2)
            var8 = i32_load((i32_load(9142840) + ((var3 + (((var2 + 1) + (var1 + 2)) * var8)) << 2)))
            if (1 if i32_load((i32_load(9142840) + ((var3 + (((var2 + 1) + (var1 + 2)) * var8)) << 2))) < 3 else 0):
                break
            var10 = i32_load(38448)
            var8 = (i32_load(9671128) + (var8 * 132))
            if (1 if i32_load(38448) != i32_load8_u((i32_load(9671128) + (var8 * 132)) + 122) else 0):
                break
            if (1 if i32_load(9681892) != var10 else 0):
                break
            var1 = i32_load(9142440)
            if (1 if var2 < var4 else 0):
                continue
            break  # end loop
        var0 = var3
        if (1 if var3 < var5 else 0):
            continue
        break  # end loop
    var0 = i32_load(9681888)
    if (1 if i32_load(9681888) <= 0 else 0):
        break
    var8 = (var0 + var6)
    var10 = (var0 + var7)
    var1 = i32_load(9142440)
    var0 = var7
    while True:  # loop $label18
        var11 = (var0 - var7)
        var2 = var6
        while True:  # loop $label17
            if (1 if var1 <= var2 else 0):
                break
            if (1 if (var0 | var2) < 0 else 0):
                break
            if (1 if var0 >= var1 else 0):
                break
            var3 = i32_load(9681892)
            var12 = (1 if i32_load(9681892) != i32_load(38448) else 0)
            if (1 if (1 if i32_load(9681892) != i32_load(38448) else 0) == 0 else 0):
                var14 = i64_load(9147316)
                var4 = i32_load(9147312)
                i32_store(9147316, i32_load(9147312))
                var5 = i32_load(9147324)
                i64_store(9147320, var14)
                var5 = (var5 ^ (var5 << 11))
                var4 = ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var5 ^ (var5 << 11)) & 0xFFFFFFFF) >> 8))) ^ var5)
                i32_store(9147312, ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var5 ^ (var5 << 11)) & 0xFFFFFFFF) >> 8))) ^ var5))
                if (1 if i32_load(9681896) < (var4 % 100) else 0):
                    break
            var4 = i32_load(9681900)
            if i32_load(9681900):
                var5 = ((var3 * 404) + 9568096)
                if (var11 % (i32_load(((var3 * 404) + 9568096) + 216) + var4)):
                    break
                if ((var2 - var6) % (i32_load(var5 + 220) + var4)):
                    break
            var1 = 0
            if (1 if var12 == 0 else 0):
                var5 = i32_load(i32_load(((var3 * 72) + 9263856)) + 20)
                var1 = i32_load(9147324)
                i32_store(9147324, i32_load(9147320))
                var12 = i32_load(9147316)
                var4 = i32_load(9147312)
                i32_store(9147316, i32_load(9147312))
                i32_store(9147320, var12)
                var1 = (var1 ^ (var1 << 11))
                var1 = ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8))) ^ var1)
                i32_store(9147312, ((var4 ^ (((var4 & 0xFFFFFFFF) >> 19) ^ (((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8))) ^ var1))
                var1 = ((var1 % (var5 - 3)) + 3)
            var1 = i32_load(9142440)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < var8 else 0):
                continue
            break  # end loop
        var0 = (var0 + 1)
        if (1 if (var0 + 1) < var10 else 0):
            continue
        break  # end loop
    break
    if (1 if var0 <= 0 else 0):
        break
    var10 = (var0 + var6)
    var11 = (var0 + var7)
    var1 = i32_load(9142440)
    var0 = var7
    while True:  # loop $label23
        var3 = (var0 + 1)
        var2 = var6
        while True:  # loop $label22
            if (1 if var1 <= var2 else 0):
                break
            if (1 if (var0 | var2) < 0 else 0):
                break
            if (1 if var0 < var1 else 0):
                break
            break
            var5 = i32_load(9142840)
            var4 = (var2 + 1)
            var8 = (((var2 + 1) * (var1 + 2)) + var3)
            var12 = (i32_load(9671128) + (i32_load((i32_load(9142840) + ((((var2 + 1) * (var1 + 2)) + var3) << 2))) * 132))
            if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9142840) + ((((var2 + 1) * (var1 + 2)) + var3) << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 4 else 0):
                var1 = i32_load(9142440)
                var8 = (((i32_load(9142440) + 2) * var4) + var3)
                var5 = i32_load(9142840)
            var8 = (var5 + (var8 << 2))
            if (1 if i32_load((var5 + (var8 << 2))) == 1 else 0):
                i32_store(var8, 0)
                var1 = (i32_load(9142440) + 2)
                i32_store((var5 + (((((i32_load(9142440) + 2) + var4) * var1) + var3) << 2)), 0)
                var1 = i32_load(9142440)
            i32_store8((i32_load(9147288) + ((var1 * var2) + var0)), i32_load(9681892))
            var1 = i32_load(9142440)
            var2 = var4
            if (1 if func32((var2 + 1), var12, 0) > var4 else 0):
                continue
            break  # end loop
        var0 = var3
        if (1 if var3 < var11 else 0):
            continue
        break  # end loop
    var2 = i32_load(9681888)
    var6 = (var6 - 4)
    var3 = (var2 + 8)
    var7 = (var7 - 4)
    if (1 if var2 >= -7 else 0):
        var4 = (var3 + var6)
        var5 = (var3 + var7)
        var1 = i32_load(9142440)
        var0 = var7
        while True:  # loop $label26
            var2 = var6
            while True:  # loop $label25
                if (1 if var1 <= var2 else 0):
                    break
                if (1 if (var0 | var2) < 0 else 0):
                    break
                if (1 if var0 >= var1 else 0):
                    break
                var8 = (i32_load(9147288) + ((var1 * var2) + var0))
                var10 = i32_load8_s((i32_load(9147288) + ((var1 * var2) + var0)))
                if (1 if i32_load8_s((i32_load(9147288) + ((var1 * var2) + var0))) >= 0 else 0):
                    break
                i32_store8(var8, (var10 ^ -1))
                var1 = i32_load(9142440)
                var2 = (var2 + 1)
                if (1 if (var2 + 1) < var4 else 0):
                    continue
                break  # end loop
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < var5 else 0):
                continue
            break  # end loop
    global global0
    global0 = (var9 + 80)
    return 0

