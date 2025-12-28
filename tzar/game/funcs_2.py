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
# $func88
# ==========================================================
def func88(var0):
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
    if i32_load8_u(9216060):
        if i32_load8_u(var0 + 286696):
            break
        if (1 if i32_load(var0 + 284616) == 0 else 0):
            break
        if (1 if i32_load(var0 + 283976) == 0 else 0):
            break
        var0 = (((i32_load(var0 + 283848) + i32_load((var0 + 281692))) - i32_load(var0 + 283956)) + 100000)
        return ((((i32_load(var0 + 283848) + i32_load((var0 + 281692))) - i32_load(var0 + 283956)) + 100000) if (1 if var0 > 0 else 0) else 0)
    var5 = i32_load(9142892)
    if i32_load(9142892):
        var10 = i32_load((var0 + 281784))
        var6 = (i32_load((var0 + 281784)) * 255)
        var7 = (var5 * var10)
        var0 = 0
        var8 = i32_load(9561692)
        var9 = i32_load(9143004)
        while True:  # loop $label3
            if i32_load8_u((var9 + (var0 + var7))):
                var2 = ((var8 + (var0 * 286704)) + 278564)
                var1 = 0
                while True:  # loop $label2
                    var3 = ((var1 * 404) + 9568096)
                    if (1 if i32_load(((var1 * 404) + 9568096) + 264) != 1 else 0):
                        break
                    if (1 if i32_load(var3 + 268) == 1 else 0):
                        break
                    var11 = ((((i32_load(var3 + 328) * i32_load((i32_load(var2) + ((var1 + var6) << 2)))) & 0xFFFFFFFF) // 100) + var11)
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != 255 else 0):
                        continue
                    break  # end loop
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var5 else 0):
                continue
            break  # end loop
        var0 = 0
        var3 = 0
        while True:  # loop $label6
            if i32_load8_u((var9 + (var0 + var7))):
                var4 = ((var8 + (var0 * 286704)) + 278564)
                var1 = 0
                while True:  # loop $label5
                    var2 = ((var1 * 404) + 9568096)
                    if (1 if i32_load(((var1 * 404) + 9568096) + 264) == 1 else 0):
                        if (1 if i32_load(var2 + 268) != 1 else 0):
                            break
                    var3 = ((((i32_load(var2 + 328) * i32_load((i32_load(var4) + ((var1 + var6) << 2)))) & 0xFFFFFFFF) // 100) + var3)
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != 255 else 0):
                        continue
                    break  # end loop
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var5 else 0):
                continue
            break  # end loop
        var2 = 0
        var0 = 0
        while True:  # loop $label10
            if i32_load8_u((var9 + (var2 + var7))):
                break
            if (1 if var2 == var10 else 0):
                break
            var12 = ((var8 + (var2 * 286704)) + 278564)
            var1 = 0
            while True:  # loop $label9
                var4 = ((var1 * 404) + 9568096)
                if (1 if i32_load(((var1 * 404) + 9568096) + 264) == 1 else 0):
                    if (1 if i32_load(var4 + 268) != 1 else 0):
                        break
                var0 = ((((i32_load(var4 + 328) * i32_load((i32_load(var12) + ((var1 + var6) << 2)))) & 0xFFFFFFFF) // 100) + var0)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != 255 else 0):
                    continue
                break  # end loop
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var4 = (var3 - var0)
        var0 = 0
        var3 = 0
        while True:  # loop $label14
            if i32_load8_u((var9 + (var0 + var7))):
                break
            if (1 if var0 == var10 else 0):
                break
            var12 = ((var8 + (var0 * 286704)) + 278564)
            var1 = 0
            while True:  # loop $label13
                var2 = ((var1 * 404) + 9568096)
                if (1 if i32_load(((var1 * 404) + 9568096) + 264) != 1 else 0):
                    break
                if (1 if i32_load(var2 + 268) == 1 else 0):
                    break
                var3 = ((((i32_load(var2 + 328) * i32_load((i32_load(var12) + ((var1 + var6) << 2)))) & 0xFFFFFFFF) // 100) + var3)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != 255 else 0):
                    continue
                break  # end loop
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var5 else 0):
                continue
            break  # end loop
    else:
    var0 = ((((var11 - var3) // 850) + (var4 // 50)) + 0)
    var1 = (((((var11 - var3) // 850) + (var4 // 50)) + 0) if (1 if var0 > 0 else 0) else 0)
    return var1


# ==========================================================
# $func89
# ==========================================================
def func89(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var3 = (var0 & 65535)
    var4 = ((var0 & 0xFFFFFFFF) >> 16)
    if (1 if var2 == 1 else 0):
        var0 = (var3 + i32_load8_u(var1))
        var0 = (((var3 + i32_load8_u(var1)) - 65521) if (1 if var0 > 65520 else 0) else var0)
        var1 = ((((var3 + i32_load8_u(var1)) - 65521) if (1 if var0 > 65520 else 0) else var0) + var4)
        var2 = (((((var3 + i32_load8_u(var1)) - 65521) if (1 if var0 > 65520 else 0) else var0) + var4) << 16)
        break
    if var1:
        if (1 if var2 >= 16 else 0):
            if (1 if var2 > 5551 else 0):
                while True:  # loop $label2
                    var2 = (var2 - 5552)
                    var5 = 347
                    var0 = var1
                    while True:  # loop $label1
                        var3 = (var3 + i32_load8_u(var0))
                        var3 = (var3 + i32_load8_u(var0 + 1))
                        var3 = (var3 + i32_load8_u(var0 + 2))
                        var3 = (var3 + i32_load8_u(var0 + 3))
                        var3 = (var3 + i32_load8_u(var0 + 4))
                        var3 = (var3 + i32_load8_u(var0 + 5))
                        var3 = (var3 + i32_load8_u(var0 + 6))
                        var3 = (var3 + i32_load8_u(var0 + 7))
                        var3 = (var3 + i32_load8_u(var0 + 8))
                        var3 = (var3 + i32_load8_u(var0 + 9))
                        var3 = (var3 + i32_load8_u(var0 + 10))
                        var3 = (var3 + i32_load8_u(var0 + 11))
                        var3 = (var3 + i32_load8_u(var0 + 12))
                        var3 = (var3 + i32_load8_u(var0 + 13))
                        var3 = (var3 + i32_load8_u(var0 + 14))
                        var3 = (var3 + i32_load8_u(var0 + 15))
                        var4 = (((((((((((((((((var3 + i32_load8_u(var0)) + var4) + (var3 + i32_load8_u(var0 + 1))) + (var3 + i32_load8_u(var0 + 2))) + (var3 + i32_load8_u(var0 + 3))) + (var3 + i32_load8_u(var0 + 4))) + (var3 + i32_load8_u(var0 + 5))) + (var3 + i32_load8_u(var0 + 6))) + (var3 + i32_load8_u(var0 + 7))) + (var3 + i32_load8_u(var0 + 8))) + (var3 + i32_load8_u(var0 + 9))) + (var3 + i32_load8_u(var0 + 10))) + (var3 + i32_load8_u(var0 + 11))) + (var3 + i32_load8_u(var0 + 12))) + (var3 + i32_load8_u(var0 + 13))) + (var3 + i32_load8_u(var0 + 14))) + (var3 + i32_load8_u(var0 + 15)))
                        var0 = (var0 + 16)
                        var5 = (var5 - 1)
                        if (var5 - 1):
                            continue
                        break  # end loop
                    var4 = (var4 % 65521)
                    var3 = (var3 % 65521)
                    var1 = (var1 + 5552)
                    if (1 if var2 > 5551 else 0):
                        continue
                    break  # end loop
                if (1 if var2 == 0 else 0):
                    break
                if (1 if var2 < 16 else 0):
                    break
            while True:  # loop $label5
                var0 = (var3 + i32_load8_u(var1))
                var0 = (var0 + i32_load8_u(var1 + 1))
                var0 = (var0 + i32_load8_u(var1 + 2))
                var0 = (var0 + i32_load8_u(var1 + 3))
                var0 = (var0 + i32_load8_u(var1 + 4))
                var0 = (var0 + i32_load8_u(var1 + 5))
                var0 = (var0 + i32_load8_u(var1 + 6))
                var0 = (var0 + i32_load8_u(var1 + 7))
                var0 = (var0 + i32_load8_u(var1 + 8))
                var0 = (var0 + i32_load8_u(var1 + 9))
                var0 = (var0 + i32_load8_u(var1 + 10))
                var0 = (var0 + i32_load8_u(var1 + 11))
                var0 = (var0 + i32_load8_u(var1 + 12))
                var0 = (var0 + i32_load8_u(var1 + 13))
                var0 = (var0 + i32_load8_u(var1 + 14))
                var3 = (var0 + i32_load8_u(var1 + 15))
                var4 = (((((((((((((((((var3 + i32_load8_u(var1)) + var4) + (var0 + i32_load8_u(var1 + 1))) + (var0 + i32_load8_u(var1 + 2))) + (var0 + i32_load8_u(var1 + 3))) + (var0 + i32_load8_u(var1 + 4))) + (var0 + i32_load8_u(var1 + 5))) + (var0 + i32_load8_u(var1 + 6))) + (var0 + i32_load8_u(var1 + 7))) + (var0 + i32_load8_u(var1 + 8))) + (var0 + i32_load8_u(var1 + 9))) + (var0 + i32_load8_u(var1 + 10))) + (var0 + i32_load8_u(var1 + 11))) + (var0 + i32_load8_u(var1 + 12))) + (var0 + i32_load8_u(var1 + 13))) + (var0 + i32_load8_u(var1 + 14))) + (var0 + i32_load8_u(var1 + 15)))
                var1 = (var1 + 16)
                var2 = (var2 - 16)
                if (1 if (var2 - 16) > 15 else 0):
                    continue
                break  # end loop
            if (1 if var2 == 0 else 0):
                break
            var6 = (var2 - 1)
            var7 = (var2 & 3)
            if (var2 & 3):
                var5 = 0
                var0 = var1
                while True:  # loop $label7
                    var2 = (var2 - 1)
                    var3 = (var3 + i32_load8_u(var0))
                    var4 = ((var3 + i32_load8_u(var0)) + var4)
                    var1 = (var0 + 1)
                    var0 = (var0 + 1)
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var7 else 0):
                        continue
                    break  # end loop
            if (1 if var6 < 3 else 0):
                break
            while True:  # loop $label8
                var0 = (var3 + i32_load8_u(var1))
                var5 = ((var3 + i32_load8_u(var1)) + i32_load8_u(var1 + 1))
                var6 = (((var3 + i32_load8_u(var1)) + i32_load8_u(var1 + 1)) + i32_load8_u(var1 + 2))
                var3 = ((((var3 + i32_load8_u(var1)) + i32_load8_u(var1 + 1)) + i32_load8_u(var1 + 2)) + i32_load8_u(var1 + 3))
                var4 = (((((var3 + i32_load8_u(var1)) + i32_load8_u(var1 + 1)) + i32_load8_u(var1 + 2)) + i32_load8_u(var1 + 3)) + (var6 + (var5 + (var0 + var4))))
                var1 = (var1 + 4)
                var2 = (var2 - 4)
                if (var2 - 4):
                    continue
                break  # end loop
            var4 = (var4 % 65521)
            var3 = (var3 % 65521)
            break
        if (1 if var2 == 0 else 0):
            break
        var7 = (var2 & 3)
        if (1 if (var2 & 3) == 0 else 0):
            var0 = var2
            break
        var0 = var2
        var5 = var1
        while True:  # loop $label11
            var0 = (var0 - 1)
            var3 = (var3 + i32_load8_u(var5))
            var4 = ((var3 + i32_load8_u(var5)) + var4)
            var1 = (var5 + 1)
            var5 = (var5 + 1)
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != var7 else 0):
                continue
            break  # end loop
        if (1 if var2 < 4 else 0):
            break
        while True:  # loop $label12
            var2 = (var3 + i32_load8_u(var1))
            var5 = ((var3 + i32_load8_u(var1)) + i32_load8_u(var1 + 1))
            var6 = (((var3 + i32_load8_u(var1)) + i32_load8_u(var1 + 1)) + i32_load8_u(var1 + 2))
            var3 = ((((var3 + i32_load8_u(var1)) + i32_load8_u(var1 + 1)) + i32_load8_u(var1 + 2)) + i32_load8_u(var1 + 3))
            var4 = (((((var3 + i32_load8_u(var1)) + i32_load8_u(var1 + 1)) + i32_load8_u(var1 + 2)) + i32_load8_u(var1 + 3)) + (var6 + (var5 + (var2 + var4))))
            var1 = (var1 + 4)
            var0 = (var0 - 4)
            if (var0 - 4):
                continue
            break  # end loop
    else:
    return 1


# ==========================================================
# $func90
# ==========================================================
def func90(var0, var1, var2, var3, var4, var5, var6, var7, var8):
    var9 = 0
    var9 = ((i64_extend_s(var4) * i64_extend_s(var7)) << 3)
    if (1 if ((i64_extend_s(var4) * i64_extend_s(var7)) << 3) <= 4294967295 else 0):
        i32_store(var0 + 72, var6)
        i32_store(var0 + 68, var3)
        i64_store(var0 + 60, 0)
        i32_store(var0 + 56, var5)
        i32_store(var0 + 52, var4)
        i32_store(var0 + 48, var2)
        i32_store(var0 + 44, var1)
        i32_store(var0 + 76, var8)
        i32_store(var0 + 8, var7)
        i32_store(var0 + 4, (1 if var2 < var5 else 0))
        i32_store(var0, (1 if var1 < var4 else 0))
        i32_store(var0 + 80, (var8 + ((var4 * var7) << 2)))
        # Unknown: memory.fill []
        var3 = i32_load(var0)
        var6 = ((var1 - 1) if i32_load(var0) else var4)
        i32_store(var0 + 40, ((var1 - 1) if i32_load(var0) else var4))
        var1 = ((var4 - 1) if var3 else var1)
        i32_store(var0 + 36, ((var4 - 1) if var3 else var1))
        if (1 if var3 == 0 else 0):
            i64_store32(var0 + 12, ((4294967296 & 0xFFFFFFFFFFFFFFFF) // i64_extend_s(var6)))
        var3 = i32_load(var0 + 4)
        var6 = (1 if i32_load(var0 + 4) != 0 else 0)
        var4 = (var5 - (1 if i32_load(var0 + 4) != 0 else 0))
        i32_store(var0 + 32, (var5 - (1 if i32_load(var0 + 4) != 0 else 0)))
        var2 = (var2 - var6)
        i32_store(var0 + 28, (var2 - var6))
        if (1 if var3 == 0 else 0):
            i32_store(var0 + 24, var2)
            var9 = (((i64_extend_u(var5) << 32) & 0xFFFFFFFFFFFFFFFF) // (i64_extend_s(var2) * i64_extend_s(var1)))
            i64_store32(var0 + 20, (4294967296 if (1 if var9 >= 4294967296 else 0) else (((i64_extend_u(var5) << 32) & 0xFFFFFFFFFFFFFFFF) // (i64_extend_s(var2) * i64_extend_s(var1)))))
            break
        i32_store(var0 + 24, var4)
        var4 = var1
        i64_store32(var0 + 16, ((4294967296 & 0xFFFFFFFFFFFFFFFF) // i64_extend_s(var4)))
        var0 = i32_load(52304)
        if (1 if i32_load(52304) != i32_load(52320) else 0):
            i32_store(9687812, 381)
            i32_store(9687808, 382)
            i32_store(9687804, 383)
            i32_store(9687800, 384)
            i32_store(52320, var0)
    else:
    return 0

