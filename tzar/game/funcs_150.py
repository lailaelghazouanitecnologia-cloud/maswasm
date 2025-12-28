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
# $bd
# Export: bd
# ==========================================================
def bd(var0, var1, var2):
    """Export: bd"""
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
    var3 = (global0 - 336)
    global global0
    global0 = (global0 - 336)
    if (1 if var1 == 0 else 0):
        # br_table ['$label0', '$label1', '$label2']
        _br_idx = var0
        break  # br_table
        var2 = (i32_load(9568064) + (var2 << 7))
        var0 = ((i32_load(9568064) + (var2 << 7)) + 128)
        var1 = i32_load(9568068)
        if (1 if ((i32_load(9568064) + (var2 << 7)) + 128) != i32_load(9568068) else 0):
            while True:  # loop $label3
                var6 = i32_load(var2)
                if i32_load(var2):
                    i32_store(var2 + 4, var6)
                    i32_store(var2 + 8, 0)
                i32_store(var2, i32_load(var0))
                i32_store(var2 + 4, i32_load(var0 + 4))
                i32_store(var2 + 8, i32_load(var0 + 8))
                i32_store(var0 + 8, 0)
                i64_store(var0, 0)
                var6 = i32_load(var2 + 12)
                if i32_load(var2 + 12):
                    i32_store(var2 + 16, var6)
                    i32_store(var2 + 20, 0)
                i32_store(var2 + 12, i32_load(var0 + 12))
                i32_store(var2 + 16, i32_load(var0 + 16))
                i32_store(var2 + 20, i32_load(var0 + 20))
                i32_store(var0 + 20, 0)
                i64_store(var0 + 12, 0)
                # Unknown: memory.copy []
                var2 = (var2 + 128)
                var0 = (var0 + 128)
                if (1 if (var0 + 128) != var1 else 0):
                    continue
                break  # end loop
            var0 = i32_load(9568068)
        if (1 if var0 != var2 else 0):
            while True:  # loop $label4
                var1 = (var0 - 128)
                var6 = i32_load((var0 - 128) + 12)
                if i32_load((var0 - 128) + 12):
                    i32_store((var0 - 112), var6)
                var6 = i32_load(var1)
                if i32_load(var1):
                    i32_store((var0 - 124), var6)
                var0 = var1
                if (1 if var1 != var2 else 0):
                    continue
                break  # end loop
        i32_store(9568068, var2)
        break
        var6 = i32_load(9568076)
        var1 = (i32_load(i32_load(9568076)) + (var2 * 196))
        var0 = (var1 + 196)
        var0 = (i32_load(var6 + 4) - var0)
        # Unknown: memory.copy []
        i32_store(var6 + 4, (var1 + ((var0 // 196) * 196)))
        break
        var6 = i32_load(9568076)
        var1 = (i32_load(i32_load(9568076) + 12) + (var2 * 196))
        var0 = (var1 + 196)
        var0 = (i32_load(var6 + 16) - var0)
        # Unknown: memory.copy []
        i32_store(var6 + 16, (var1 + ((var0 // 196) * 196)))
        break
    var7 = i32_load(9568076)
    if (1 if i32_load(9568076) == 0 else 0):
        break
    if (1 if var0 == 0 else 0):
        i64_store(var3 + 224, 0)
        i64_store(var3 + 216, 0)
        i64_store(var3 + 208, 0)
        var0 = 0
        i32_store(var3 + 332, 0)
        i32_store(var3 + 316, i32_load(var7 + 108))
        i32_store(var3 + 320, i32_load(var7 + 112))
        i32_store(var3 + 324, i32_load(var7 + 116))
        i32_store(var3 + 328, i32_load(var7 + 120))
        i32_store(var3 + 312, i32_load(var7 + 104))
        var8 = i32_load(var7 + 104)
        if (1 if i32_load(var7 + 104) == 0 else 0):
            break
        if (1 if var8 >= 4 else 0):
            var2 = (var8 & -4)
            while True:  # loop $label7
                var4 = (var3 + 232)
                var9 = (var0 << 1)
                var5 = (var7 + 24)
                i32_store16(((var3 + 232) + (var0 << 1)), i32_load16_u(((var7 + 24) + var9)))
                var1 = (var9 | 2)
                i32_store16((var4 + (var9 | 2)), i32_load16_u((var1 + var5)))
                var1 = (var9 | 4)
                i32_store16((var4 + (var9 | 4)), i32_load16_u((var1 + var5)))
                var1 = (var9 | 6)
                i32_store16((var4 + (var9 | 6)), i32_load16_u((var1 + var5)))
                var0 = (var0 + 4)
                var6 = (var6 + 4)
                if (1 if (var6 + 4) != var2 else 0):
                    continue
                break  # end loop
        var6 = (var8 & 3)
        if (1 if (var8 & 3) == 0 else 0):
            break
        var2 = 0
        while True:  # loop $label8
            var1 = (var0 << 1)
            i32_store16((var3 + (var0 << 1)) + 232, i32_load16_u((var1 + var7) + 24))
            var0 = (var0 + 1)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var6 else 0):
                continue
            break  # end loop
        if (1 if i32_load(var7 + 4) == i32_load(var7) else 0):
            break
        var1 = 0
        var4 = 0
        var0 = 0
        var2 = 0
        while True:  # loop $label13
            i64_store(var3 + 47, 0)
            i64_store(var3 + 40, 0)
            i64_store(var3 + 32, 0)
            i64_store(var3 + 24, 0)
            i64_store(var3 + 16, 0)
            i64_store(var3 + 8, 0)
            i32_store(var3 + 60, 1)
            i32_store(var3 + 56, func26(4))
            i32_store(var3 + 76, 1)
            i64_store(var3 + 64, 4294967296)
            i32_store(var3 + 72, func26(4))
            i32_store(var3 + 92, 1)
            i64_store(var3 + 80, 4294967296)
            i32_store(var3 + 88, func26(4))
            i32_store(var3 + 108, 1)
            i64_store(var3 + 96, 4294967296)
            i32_store(var3 + 104, func26(4))
            i32_store(var3 + 200, 0)
            i64_store(var3 + 112, 4294967296)
            func255((var3 + 8), (i32_load(var7) + (var2 * 196)))
            if (1 if var0 != var4 else 0):
                # Unknown: memory.copy []
                var0 = (var0 + 196)
                i32_store(var3 + 212, (var0 + 196))
                break
            var4 = (var4 - var1)
            var5 = ((var4 - var1) // 196)
            var6 = (((var4 - var1) // 196) + 1)
            if (1 if (((var4 - var1) // 196) + 1) >= 21913099 else 0):
                break
            var0 = (var5 << 1)
            var8 = (21913098 if (1 if var5 >= 10956549 else 0) else ((var5 << 1) if (1 if var0 > var6 else 0) else var6))
            if (21913098 if (1 if var5 >= 10956549 else 0) else ((var5 << 1) if (1 if var0 > var6 else 0) else var6)):
                if (1 if var8 >= 21913099 else 0):
                    break
            else:
            var0 = 0
            var5 = (0 + (var5 * 196))
            # Unknown: memory.copy []
            var6 = (var5 + ((var4 // -196) * 196))
            # Unknown: memory.copy []
            var4 = (var0 + (var8 * 196))
            i32_store(var3 + 216, (var0 + (var8 * 196)))
            var0 = (var5 + 196)
            i32_store(var3 + 212, (var5 + 196))
            i32_store(var3 + 208, var6)
            if var1:
            var1 = var6
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < ((i32_load(var7 + 4) - i32_load(var7)) // 196) else 0):
                continue
            break  # end loop
        break
    var2 = i32_load(9568088)
    if (1 if i32_load(9568088) == 0 else 0):
        break
    i64_store(var3 + 47, 0)
    i64_store(var3 + 40, 0)
    i64_store(var3 + 32, 0)
    i64_store(var3 + 24, 0)
    i64_store(var3 + 16, 0)
    i32_store(var3 + 60, 1)
    i64_store(var3 + 8, 0)
    var1 = func26(4)
    i32_store(var3 + 76, 1)
    i64_store((var3 - -64), 4294967296)
    i32_store(var3 + 56, var1)
    var1 = func26(4)
    i32_store(var3 + 92, 1)
    i64_store(var3 + 80, 4294967296)
    i32_store(var3 + 72, var1)
    var1 = func26(4)
    i32_store(var3 + 108, 1)
    i64_store(var3 + 96, 4294967296)
    i32_store(var3 + 88, var1)
    var1 = func26(4)
    i64_store(var3 + 112, 4294967296)
    i32_store(var3 + 104, var1)
    i32_store(var3 + 200, 0)
    var9 = (var3 + 8)
    func255((var3 + 8), var2)
    var2 = i32_load(9568076)
    var1 = (1 if var0 == 1 else 0)
    var11 = (i32_load(9568076) if (1 if var0 == 1 else 0) else (var2 + 12))
    var0 = i32_load((i32_load(9568076) if (1 if var0 == 1 else 0) else (var2 + 12)))
    var5 = ((i32_load((var2 + (0 if var1 else 12))) + (i32_load(9568084) * 196)) - var0)
    var4 = (((i32_load((var2 + (0 if var1 else 12))) + (i32_load(9568084) * 196)) - var0) // 196)
    var7 = (i32_load((i32_load(9568076) if (1 if var0 == 1 else 0) else (var2 + 12))) + ((((i32_load((var2 + (0 if var1 else 12))) + (i32_load(9568084) * 196)) - var0) // 196) * 196))
    var2 = i32_load(var11 + 4)
    var1 = i32_load(var11 + 8)
    if (1 if i32_load(var11 + 4) < i32_load(var11 + 8) else 0):
        if (1 if var2 == var7 else 0):
            # Unknown: memory.copy []
            i32_store(var11 + 4, (var7 + 196))
            break
        var0 = var2
        var6 = (var7 + 196)
        var5 = (var2 - (var7 + 196))
        var1 = (var7 + (((var2 - (var7 + 196)) // 196) * 196))
        if (1 if var2 > (var7 + (((var2 - (var7 + 196)) // 196) * 196)) else 0):
            while True:  # loop $label15
                # Unknown: memory.copy []
                var0 = (var0 + 196)
                var1 = (var1 + 196)
                if (1 if (var1 + 196) < var2 else 0):
                    continue
                break  # end loop
        i32_store(var11 + 4, var0)
        if (1 if var2 != var6 else 0):
            # Unknown: memory.copy []
        else:
        # Unknown: memory.copy []
        break
    var6 = (((var2 - var0) // 196) + 1)
    if (1 if (((var2 - var0) // 196) + 1) < 21913099 else 0):
        var2 = ((var1 - var0) // 196)
        var1 = (((var1 - var0) // 196) << 1)
        var2 = (21913098 if (1 if var2 >= 10956549 else 0) else ((((var1 - var0) // 196) << 1) if (1 if var1 > var6 else 0) else var6))
        if (21913098 if (1 if var2 >= 10956549 else 0) else ((((var1 - var0) // 196) << 1) if (1 if var1 > var6 else 0) else var6)):
            if (1 if var2 >= 21913099 else 0):
                break
        else:
        var8 = 0
        var6 = (var4 * 196)
        var1 = (var8 + (var4 * 196))
        var2 = (var2 * 196)
        if (1 if var6 != (var2 * 196) else 0):
            var2 = (var2 + var8)
            break
        if (1 if var1 > var8 else 0):
            var2 = var1
            var1 = (var1 + (((var4 + 1) // -2) * 196))
            break
        var6 = (1 if (1 if (var5 + 195) < 391 else 0) else (var4 << 1))
        if (1 if (1 if (1 if (var5 + 195) < 391 else 0) else (var4 << 1)) >= 21913099 else 0):
            break
        var2 = (var6 * 196)
        var1 = func26((var6 * 196))
        var2 = (func26((var6 * 196)) + var2)
        var1 = (var1 + (((var6 & 0xFFFFFFFF) >> 2) * 196))
        if (1 if var8 == 0 else 0):
            break
        var0 = i32_load(var11)
        # Unknown: memory.copy []
        var5 = (var7 - var0)
        var6 = (var1 + (((var7 - var0) // -196) * 196))
        # Unknown: memory.copy []
        var1 = (var1 + 196)
        var0 = (i32_load(var11 + 4) - var7)
        # Unknown: memory.copy []
        i32_store(var11 + 8, var2)
        var2 = i32_load(var11)
        i32_store(var11, var6)
        i32_store(var11 + 4, (var1 + ((var0 // 196) * 196)))
        if var2:
        break
    func42()
    raise RuntimeError('unreachable')
    func68()
    raise RuntimeError('unreachable')
    break
    func42()
    raise RuntimeError('unreachable')
    if (1 if i32_load(var7 + 16) == i32_load(var7 + 12) else 0):
        break
    var1 = 0
    var4 = 0
    var0 = 0
    var2 = 0
    while True:  # loop $label21
        i64_store(var3 + 47, 0)
        i64_store(var3 + 40, 0)
        i64_store(var3 + 32, 0)
        i64_store(var3 + 24, 0)
        i64_store(var3 + 16, 0)
        i64_store(var3 + 8, 0)
        i32_store(var3 + 60, 1)
        i32_store(var3 + 56, func26(4))
        i32_store(var3 + 76, 1)
        i64_store(var3 + 64, 4294967296)
        i32_store(var3 + 72, func26(4))
        i32_store(var3 + 92, 1)
        i64_store(var3 + 80, 4294967296)
        i32_store(var3 + 88, func26(4))
        i32_store(var3 + 108, 1)
        i64_store(var3 + 96, 4294967296)
        i32_store(var3 + 104, func26(4))
        i32_store(var3 + 200, 0)
        i64_store(var3 + 112, 4294967296)
        func255((var3 + 8), (i32_load(var7 + 12) + (var2 * 196)))
        if (1 if var0 != var4 else 0):
            # Unknown: memory.copy []
            var0 = (var0 + 196)
            i32_store(var3 + 224, (var0 + 196))
            break
        var4 = (var4 - var1)
        var5 = ((var4 - var1) // 196)
        var6 = (((var4 - var1) // 196) + 1)
        if (1 if (((var4 - var1) // 196) + 1) >= 21913099 else 0):
            break
        var0 = (var5 << 1)
        var8 = (21913098 if (1 if var5 >= 10956549 else 0) else ((var5 << 1) if (1 if var0 > var6 else 0) else var6))
        if (21913098 if (1 if var5 >= 10956549 else 0) else ((var5 << 1) if (1 if var0 > var6 else 0) else var6)):
            if (1 if var8 >= 21913099 else 0):
                break
        else:
        var0 = 0
        var5 = (0 + (var5 * 196))
        # Unknown: memory.copy []
        var6 = (var5 + ((var4 // -196) * 196))
        # Unknown: memory.copy []
        var4 = (var0 + (var8 * 196))
        i32_store(var3 + 228, (var0 + (var8 * 196)))
        var0 = (var5 + 196)
        i32_store(var3 + 224, (var5 + 196))
        i32_store(var3 + 220, var6)
        if var1:
        var1 = var6
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < ((i32_load(var7 + 16) - i32_load(var7 + 12)) // 196) else 0):
            continue
        break  # end loop
    break
    func68()
    raise RuntimeError('unreachable')
    func42()
    raise RuntimeError('unreachable')
    var11 = i32_load(9568064)
    var0 = (i32_load(9568064) + (i32_load(9568080) << 7))
    var6 = (var3 + 208)
    var12 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var7 = ((var0 - var11) >> 7)
    var1 = i32_load(9568068)
    var2 = i32_load(9568072)
    if (1 if i32_load(9568068) < i32_load(9568072) else 0):
        if (1 if var0 == var1 else 0):
            i32_store(9568068, (func226(var0, var6) + 128))
            break
        var5 = i32_load(9568068)
        var9 = i32_load(9568068)
        var2 = var0
        var8 = (var0 + 128)
        var0 = (var0 + (var5 - (var0 + 128)))
        if (1 if var1 > (var0 + (var5 - (var0 + 128))) else 0):
            var4 = var0
            while True:  # loop $label23
                i32_store(var9 + 8, 0)
                i64_store(var9, 0)
                i32_store(var9, i32_load(var4))
                i32_store(var9 + 4, i32_load(var4 + 4))
                i32_store(var9 + 8, i32_load(var4 + 8))
                i32_store(var4 + 8, 0)
                i64_store(var4, 0)
                i32_store(var9 + 20, 0)
                i64_store(var9 + 12, 0)
                i32_store(var9 + 12, i32_load(var4 + 12))
                i32_store(var9 + 16, i32_load(var4 + 16))
                i32_store(var9 + 20, i32_load(var4 + 20))
                i32_store(var4 + 20, 0)
                i64_store(var4 + 12, 0)
                # Unknown: memory.copy []
                var9 = (var9 + 128)
                var4 = (var4 + 128)
                if (1 if (var4 + 128) < var1 else 0):
                    continue
                break  # end loop
        i32_store(9568068, var9)
        if (1 if var5 != var8 else 0):
            while True:  # loop $label24
                var1 = (var5 - 128)
                var8 = i32_load((var5 - 128))
                if i32_load((var5 - 128)):
                    var4 = (var5 - 124)
                    i32_store((var5 - 124), var8)
                    i64_store(var4, 0)
                    i32_store(var1, 0)
                var4 = (var0 - 128)
                i32_store(var1, i32_load((var0 - 128)))
                i32_store(var1 + 4, i32_load(var4 + 4))
                i32_store(var1 + 8, i32_load(var4 + 8))
                i64_store(var4 + 4, 0)
                i32_store(var4, 0)
                var9 = i32_load(var1 + 12)
                if i32_load(var1 + 12):
                    var8 = (var5 - 112)
                    i32_store((var5 - 112), var9)
                    i64_store(var8, 0)
                    i32_store(var1 + 12, 0)
                i32_store(var1 + 12, i32_load(var4 + 12))
                var8 = (var5 - 128)
                i32_store((var5 - 128) + 16, i32_load(var4 + 16))
                i32_store(var8 + 20, i32_load(var4 + 20))
                i32_store(var4 + 20, 0)
                i64_store(var4 + 12, 0)
                # Unknown: memory.copy []
                var5 = var1
                var0 = var4
                if (1 if var4 != var2 else 0):
                    continue
                break  # end loop
        var0 = (var6 + (((1 if var2 <= var6 else 0) & (1 if i32_load(9568068) > var6 else 0)) << 7))
        if (1 if (var6 + (((1 if var2 <= var6 else 0) & (1 if i32_load(9568068) > var6 else 0)) << 7)) != var2 else 0):
        # Unknown: memory.copy []
        break
    var5 = (((var1 - var11) >> 7) + 1)
    if (1 if (((var1 - var11) >> 7) + 1) >= 33554432 else 0):
        break
    i32_store(var12 + 28, 9568072)
    var2 = (var2 - var11)
    var1 = ((var2 - var11) >> 6)
    var5 = (33554431 if (1 if var2 >= 2147483520 else 0) else (((var2 - var11) >> 6) if (1 if var1 > var5 else 0) else var5))
    if (33554431 if (1 if var2 >= 2147483520 else 0) else (((var2 - var11) >> 6) if (1 if var1 > var5 else 0) else var5)):
        if (1 if var5 >= 33554432 else 0):
            break
    else:
    var2 = 0
    i32_store(func26((var5 << 7)) + 12, 0)
    var1 = (var2 + (var7 << 7))
    i32_store(var12 + 20, (var2 + (var7 << 7)))
    i32_store(var12 + 24, (var2 + (var5 << 7)))
    i32_store(var12 + 16, var1)
    var2 = (var12 + 12)
    var11 = i32_load((var12 + 12) + 8)
    if (1 if i32_load((var12 + 12) + 8) != i32_load(var2 + 12) else 0):
        break
    var10 = i32_load(var2 + 4)
    var7 = i32_load(var2)
    if (1 if i32_load(var2 + 4) > i32_load(var2) else 0):
        var5 = (((((var10 - var7) >> 7) + 1) // -2) << 7)
        var1 = (var10 + (((((var10 - var7) >> 7) + 1) // -2) << 7))
        if (1 if var10 != var11 else 0):
            while True:  # loop $label28
                var4 = i32_load(var1)
                if i32_load(var1):
                    i32_store(var1 + 4, var4)
                    i32_store(var1 + 8, 0)
                    i64_store(var1, 0)
                i32_store(var1, i32_load(var10))
                i32_store(var1 + 4, i32_load(var10 + 4))
                i32_store(var1 + 8, i32_load(var10 + 8))
                i32_store(var10 + 8, 0)
                i64_store(var10, 0)
                var4 = i32_load(var1 + 12)
                if i32_load(var1 + 12):
                    i32_store(var1 + 16, var4)
                    i32_store(var1 + 20, 0)
                    i64_store(var1 + 12, 0)
                i32_store(var1 + 12, i32_load(var10 + 12))
                i32_store(var1 + 16, i32_load(var10 + 16))
                i32_store(var1 + 20, i32_load(var10 + 20))
                i32_store(var10 + 20, 0)
                i64_store(var10 + 12, 0)
                # Unknown: memory.copy []
                var1 = (var1 + 128)
                var10 = (var10 + 128)
                if (1 if (var10 + 128) != var11 else 0):
                    continue
                break  # end loop
            var11 = i32_load(var2 + 4)
        i32_store(var2 + 8, var1)
        i32_store(var2 + 4, (var5 + var11))
        break
    var5 = (1 if (1 if var7 == var11 else 0) else ((var11 - var7) >> 6))
    if (1 if (1 if (1 if var7 == var11 else 0) else ((var11 - var7) >> 6)) < 33554432 else 0):
        var1 = (var5 << 7)
        var9 = func26((var5 << 7))
        var8 = (func26((var5 << 7)) + var1)
        var5 = (var9 + ((var5 << 5) & -128))
        if (1 if var10 == var11 else 0):
            break
        var4 = (var5 + (var11 - var10))
        var1 = var5
        while True:  # loop $label30
            i32_store(var1, i32_load(var10))
            i32_store(var1 + 4, i32_load(var10 + 4))
            i32_store(var1 + 8, i32_load(var10 + 8))
            i32_store(var10 + 8, 0)
            i64_store(var10, 0)
            i32_store(var1 + 12, i32_load(var10 + 12))
            i32_store(var1 + 16, i32_load(var10 + 16))
            i32_store(var1 + 20, i32_load(var10 + 20))
            i32_store(var10 + 20, 0)
            i64_store(var10 + 12, 0)
            # Unknown: memory.copy []
            var10 = (var10 + 128)
            var1 = (var1 + 128)
            if (1 if (var1 + 128) != var4 else 0):
                continue
            break  # end loop
        i32_store(var2 + 12, var8)
        var1 = i32_load(var2 + 8)
        i32_store(var2 + 8, var4)
        var8 = i32_load(var2 + 4)
        i32_store(var2 + 4, var5)
        var7 = i32_load(var2)
        i32_store(var2, var9)
        if (1 if var1 == var8 else 0):
            break
        while True:  # loop $label32
            var5 = (var1 - 128)
            var4 = i32_load((var1 - 128) + 12)
            if i32_load((var1 - 128) + 12):
                i32_store((var1 - 112), var4)
            var4 = i32_load(var5)
            if i32_load(var5):
                i32_store((var1 - 124), var4)
            var1 = var5
            if (1 if var5 != var8 else 0):
                continue
            break  # end loop
        break
    func68()
    raise RuntimeError('unreachable')
    i32_store(var2 + 12, var8)
    i32_store(var2 + 8, var5)
    i32_store(var2 + 4, var5)
    i32_store(var2, var9)
    if (1 if var7 == 0 else 0):
        break
    i32_store(var2 + 8, (i32_load(var2 + 8) + 128))
    var6 = var2
    var4 = i32_load(var2 + 4)
    var5 = i32_load(var2 + 4)
    var8 = i32_load(9568064)
    var1 = var0
    if (1 if i32_load(9568064) != var0 else 0):
        while True:  # loop $label33
            var5 = (var4 - 128)
            i64_store((var4 - 128), 0)
            i32_store(var5 + 8, 0)
            var2 = (var0 - 128)
            i32_store(var5, i32_load((var0 - 128)))
            i32_store(var5 + 4, i32_load(var2 + 4))
            i32_store(var5 + 8, i32_load(var2 + 8))
            i32_store(var2 + 8, 0)
            i64_store(var2, 0)
            i32_store(var5 + 20, 0)
            i64_store(var5 + 12, 0)
            i32_store(var5 + 12, i32_load(var2 + 12))
            i32_store(var5 + 16, i32_load(var2 + 16))
            i32_store(var5 + 20, i32_load(var2 + 20))
            i32_store(var2 + 20, 0)
            i64_store(var2 + 12, 0)
            # Unknown: memory.copy []
            var4 = var5
            var0 = var2
            if (1 if var2 != var8 else 0):
                continue
            break  # end loop
    i32_store(var6 + 4, var5)
    var4 = i32_load(var6 + 8)
    var0 = i32_load(9568068)
    if (1 if var1 != i32_load(9568068) else 0):
        while True:  # loop $label34
            i32_store(var4 + 8, 0)
            i64_store(var4, 0)
            i32_store(var4, i32_load(var1))
            i32_store(var4 + 4, i32_load(var1 + 4))
            i32_store(var4 + 8, i32_load(var1 + 8))
            i32_store(var1 + 8, 0)
            i64_store(var1, 0)
            i32_store(var4 + 20, 0)
            i64_store(var4 + 12, 0)
            i32_store(var4 + 12, i32_load(var1 + 12))
            i32_store(var4 + 16, i32_load(var1 + 16))
            i32_store(var4 + 20, i32_load(var1 + 20))
            i32_store(var1 + 20, 0)
            i64_store(var1 + 12, 0)
            # Unknown: memory.copy []
            var4 = (var4 + 128)
            var1 = (var1 + 128)
            if (1 if (var1 + 128) != var0 else 0):
                continue
            break  # end loop
        var5 = i32_load(var6 + 4)
    i32_store(var6 + 8, var4)
    var0 = i32_load(9568064)
    i32_store(9568064, var5)
    i32_store(var6 + 4, var0)
    var0 = i32_load(9568068)
    i32_store(9568068, i32_load(var6 + 8))
    i32_store(var6 + 8, var0)
    var0 = i32_load(9568072)
    i32_store(9568072, i32_load(var6 + 12))
    i32_store(var6 + 12, var0)
    i32_store(var6, i32_load(var6 + 4))
    var1 = i32_load(var12 + 20)
    var0 = i32_load(var12 + 16)
    if (1 if i32_load(var12 + 20) != i32_load(var12 + 16) else 0):
        while True:  # loop $label35
            var6 = (var1 - 128)
            i32_store(var12 + 20, (var1 - 128))
            var2 = i32_load(var6 + 12)
            if i32_load(var6 + 12):
                i32_store((var1 - 112), var2)
            var2 = i32_load(var6)
            if i32_load(var6):
                i32_store((var1 - 124), var2)
            var1 = i32_load(var12 + 20)
            if (1 if i32_load(var12 + 20) != var0 else 0):
                continue
            break  # end loop
    var0 = i32_load(var12 + 12)
    if (1 if i32_load(var12 + 12) == 0 else 0):
        break
    global global0
    global0 = (var12 + 32)
    break
    func42()
    raise RuntimeError('unreachable')
    func68()
    raise RuntimeError('unreachable')
    var0 = i32_load(var3 + 220)
    if i32_load(var3 + 220):
        i32_store(var3 + 224, var0)
    var0 = i32_load(var3 + 208)
    if (1 if i32_load(var3 + 208) == 0 else 0):
        break
    i32_store(var3 + 212, var0)
    global global0
    global0 = (var3 + 336)
    return af(var0)

