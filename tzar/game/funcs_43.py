"""
Auto-generated from WAT. Contains 9 functions.
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
# $func1102
# ==========================================================
def func1102(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    if (1 if var2 != 1 else 0):
        while True:  # loop $label0
            var3 = (i32_load8_u(var1) + ((i32_load8_u(var0) - 120) >> 4))
            var3 = ((i32_load8_u(var1) + ((i32_load8_u(var0) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)
            i32_store8(var1, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1) + ((i32_load8_u(var0) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)))
            var3 = (i32_load8_u(var1 + 1) + ((i32_load8_u(var0 + 1) - 120) >> 4))
            var3 = ((i32_load8_u(var1 + 1) + ((i32_load8_u(var0 + 1) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)
            i32_store8(var1 + 1, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1 + 1) + ((i32_load8_u(var0 + 1) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)))
            var3 = (i32_load8_u(var1 + 2) + ((i32_load8_u(var0 + 2) - 120) >> 4))
            var3 = ((i32_load8_u(var1 + 2) + ((i32_load8_u(var0 + 2) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)
            i32_store8(var1 + 2, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1 + 2) + ((i32_load8_u(var0 + 2) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)))
            var3 = (i32_load8_u(var1 + 3) + ((i32_load8_u(var0 + 3) - 120) >> 4))
            var3 = ((i32_load8_u(var1 + 3) + ((i32_load8_u(var0 + 3) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)
            i32_store8(var1 + 3, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1 + 3) + ((i32_load8_u(var0 + 3) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)))
            var3 = (i32_load8_u(var1 + 4) + ((i32_load8_u(var0 + 4) - 120) >> 4))
            var3 = ((i32_load8_u(var1 + 4) + ((i32_load8_u(var0 + 4) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)
            i32_store8(var1 + 4, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1 + 4) + ((i32_load8_u(var0 + 4) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)))
            var3 = (i32_load8_u(var1 + 5) + ((i32_load8_u(var0 + 5) - 120) >> 4))
            var3 = ((i32_load8_u(var1 + 5) + ((i32_load8_u(var0 + 5) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)
            i32_store8(var1 + 5, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1 + 5) + ((i32_load8_u(var0 + 5) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)))
            var3 = (i32_load8_u(var1 + 6) + ((i32_load8_u(var0 + 6) - 120) >> 4))
            var3 = ((i32_load8_u(var1 + 6) + ((i32_load8_u(var0 + 6) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)
            i32_store8(var1 + 6, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1 + 6) + ((i32_load8_u(var0 + 6) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)))
            var3 = (i32_load8_u(var1 + 7) + ((i32_load8_u(var0 + 7) - 120) >> 4))
            var3 = ((i32_load8_u(var1 + 7) + ((i32_load8_u(var0 + 7) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)
            i32_store8(var1 + 7, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1 + 7) + ((i32_load8_u(var0 + 7) - 120) >> 4)) if (1 if var3 > 0 else 0) else 0)))
            var0 = (var0 + 8)
            var1 = (var1 + var2)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != 8 else 0):
                continue
            break  # end loop
        break
    var5 = i32_load8_u(var1 + 6)
    while True:  # loop $label2
        var4 = (i32_load8_u(var1) + ((i32_load8_u(var0) - 120) >> 4))
        var4 = ((i32_load8_u(var1) + ((i32_load8_u(var0) - 120) >> 4)) if (1 if var4 > 0 else 0) else 0)
        i32_store8(var1, (255 if (1 if var4 >= 255 else 0) else ((i32_load8_u(var1) + ((i32_load8_u(var0) - 120) >> 4)) if (1 if var4 > 0 else 0) else 0)))
        var4 = (i32_load8_u(var1 + 1) + ((i32_load8_u(var0 + 1) - 120) >> 4))
        var4 = ((i32_load8_u(var1 + 1) + ((i32_load8_u(var0 + 1) - 120) >> 4)) if (1 if var4 > 0 else 0) else 0)
        i32_store8(var1 + 1, (255 if (1 if var4 >= 255 else 0) else ((i32_load8_u(var1 + 1) + ((i32_load8_u(var0 + 1) - 120) >> 4)) if (1 if var4 > 0 else 0) else 0)))
        var4 = (i32_load8_u(var1 + 2) + ((i32_load8_u(var0 + 2) - 120) >> 4))
        var4 = ((i32_load8_u(var1 + 2) + ((i32_load8_u(var0 + 2) - 120) >> 4)) if (1 if var4 > 0 else 0) else 0)
        i32_store8(var1 + 2, (255 if (1 if var4 >= 255 else 0) else ((i32_load8_u(var1 + 2) + ((i32_load8_u(var0 + 2) - 120) >> 4)) if (1 if var4 > 0 else 0) else 0)))
        var4 = (i32_load8_u(var1 + 3) + ((i32_load8_u(var0 + 3) - 120) >> 4))
        var4 = ((i32_load8_u(var1 + 3) + ((i32_load8_u(var0 + 3) - 120) >> 4)) if (1 if var4 > 0 else 0) else 0)
        i32_store8(var1 + 3, (255 if (1 if var4 >= 255 else 0) else ((i32_load8_u(var1 + 3) + ((i32_load8_u(var0 + 3) - 120) >> 4)) if (1 if var4 > 0 else 0) else 0)))
        var4 = (i32_load8_u(var1 + 4) + ((i32_load8_u(var0 + 4) - 120) >> 4))
        var4 = ((i32_load8_u(var1 + 4) + ((i32_load8_u(var0 + 4) - 120) >> 4)) if (1 if var4 > 0 else 0) else 0)
        i32_store8(var1 + 4, (255 if (1 if var4 >= 255 else 0) else ((i32_load8_u(var1 + 4) + ((i32_load8_u(var0 + 4) - 120) >> 4)) if (1 if var4 > 0 else 0) else 0)))
        var4 = (i32_load8_u(var1 + 5) + ((i32_load8_u(var0 + 5) - 120) >> 4))
        var4 = ((i32_load8_u(var1 + 5) + ((i32_load8_u(var0 + 5) - 120) >> 4)) if (1 if var4 > 0 else 0) else 0)
        i32_store8(var1 + 5, (255 if (1 if var4 >= 255 else 0) else ((i32_load8_u(var1 + 5) + ((i32_load8_u(var0 + 5) - 120) >> 4)) if (1 if var4 > 0 else 0) else 0)))
        var5 = ((var5 & 255) + ((i32_load8_u(var0 + 6) - 120) >> 4))
        var5 = (((var5 & 255) + ((i32_load8_u(var0 + 6) - 120) >> 4)) if (1 if var5 > 0 else 0) else 0)
        i32_store8(var1 + 6, (255 if (1 if var5 >= 255 else 0) else (((var5 & 255) + ((i32_load8_u(var0 + 6) - 120) >> 4)) if (1 if var5 > 0 else 0) else 0)))
        var5 = (i32_load8_u(var1 + 7) + ((i32_load8_u(var0 + 7) - 120) >> 4))
        var5 = ((i32_load8_u(var1 + 7) + ((i32_load8_u(var0 + 7) - 120) >> 4)) if (1 if var5 > 0 else 0) else 0)
        var5 = (255 if (1 if var5 >= 255 else 0) else ((i32_load8_u(var1 + 7) + ((i32_load8_u(var0 + 7) - 120) >> 4)) if (1 if var5 > 0 else 0) else 0))
        i32_store8(var1 + 7, (255 if (1 if var5 >= 255 else 0) else ((i32_load8_u(var1 + 7) + ((i32_load8_u(var0 + 7) - 120) >> 4)) if (1 if var5 > 0 else 0) else 0)))
        var0 = (var0 + 8)
        var1 = (var1 + var2)
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != 8 else 0):
            continue
        break  # end loop


# ==========================================================
# $func1103
# ==========================================================
def func1103(var0, var1, var2, var3, var4, var5):
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
    if (1 if var3 <= 0 else 0):
        break
    if (1 if var2 <= 0 else 0):
        break
    var14 = (var2 & -4)
    var12 = (var2 & 3)
    var6 = 255
    var15 = (1 if var2 < 4 else 0)
    while True:  # loop $label3
        var2 = 0
        var7 = 0
        if (1 if var15 == 0 else 0):
            while True:  # loop $label1
                var8 = i32_load8_u((var0 + var2))
                i32_store8((var4 + (var2 << 2)), i32_load8_u((var0 + var2)))
                var9 = (var2 | 1)
                var9 = i32_load8_u((var0 + var9))
                i32_store8((var4 + ((var2 | 1) << 2)), i32_load8_u((var0 + var9)))
                var10 = (var2 | 2)
                var10 = i32_load8_u((var0 + var10))
                i32_store8((var4 + ((var2 | 2) << 2)), i32_load8_u((var0 + var10)))
                var11 = (var2 | 3)
                var11 = i32_load8_u((var0 + var11))
                i32_store8((var4 + ((var2 | 3) << 2)), i32_load8_u((var0 + var11)))
                var6 = (var11 & (var10 & (var9 & (var6 & var8))))
                var2 = (var2 + 4)
                var7 = (var7 + 4)
                if (1 if (var7 + 4) != var14 else 0):
                    continue
                break  # end loop
        var7 = 0
        if var12:
            while True:  # loop $label2
                var8 = i32_load8_u((var0 + var2))
                i32_store8((var4 + (var2 << 2)), i32_load8_u((var0 + var2)))
                var2 = (var2 + 1)
                var6 = (var6 & var8)
                var7 = (var7 + 1)
                if (1 if (var7 + 1) != var12 else 0):
                    continue
                break  # end loop
        var4 = (var4 + var5)
        var0 = (var0 + var1)
        var13 = (var13 + 1)
        if (1 if (var13 + 1) != var3 else 0):
            continue
        break  # end loop
    var6 = (1 if var6 != 255 else 0)
    return var6


# ==========================================================
# $func1104
# ==========================================================
def func1104(var0, var1, var2, var3, var4, var5):
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    if (1 if var3 <= 0 else 0):
        break
    if (1 if var2 <= 0 else 0):
        break
    var9 = (var2 & -4)
    var7 = (var2 & 3)
    var10 = (1 if var2 < 4 else 0)
    var11 = (var5 << 2)
    while True:  # loop $label3
        var2 = 0
        var5 = 0
        if (1 if var10 == 0 else 0):
            while True:  # loop $label1
                i32_store((var4 + (var2 << 2)), (i32_load8_u((var0 + var2)) << 8))
                var6 = (var2 | 1)
                i32_store((var4 + ((var2 | 1) << 2)), (i32_load8_u((var0 + var6)) << 8))
                var6 = (var2 | 2)
                i32_store((var4 + ((var2 | 2) << 2)), (i32_load8_u((var0 + var6)) << 8))
                var6 = (var2 | 3)
                i32_store((var4 + ((var2 | 3) << 2)), (i32_load8_u((var0 + var6)) << 8))
                var2 = (var2 + 4)
                var5 = (var5 + 4)
                if (1 if (var5 + 4) != var9 else 0):
                    continue
                break  # end loop
        var5 = 0
        if var7:
            while True:  # loop $label2
                i32_store((var4 + (var2 << 2)), (i32_load8_u((var0 + var2)) << 8))
                var2 = (var2 + 1)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var7 else 0):
                    continue
                break  # end loop
        var0 = (var0 + var1)
        var4 = (var4 + var11)
        var8 = (var8 + 1)
        if (1 if (var8 + 1) != var3 else 0):
            continue
        break  # end loop


# ==========================================================
# $func1105
# ==========================================================
def func1105(var0):
    var1 = 0
    var1 = ((i64_extend_u(((((i32_load8_u(var0 + 223) + (i32_load8_u((var0 - 25)) + (i32_load8_u(var0 + 191) + (i32_load8_u((var0 - 26)) + (i32_load8_u(var0 + 159) + (i32_load8_u((var0 - 27)) + (i32_load8_u(var0 + 127) + (i32_load8_u((var0 - 28)) + (i32_load8_u(var0 + 95) + (i32_load8_u((var0 - 29)) + (i32_load8_u(var0 + 63) + (i32_load8_u((var0 - 30)) + (i32_load8_u(var0 + 31) + (i32_load8_u((var0 - 31)) + (i32_load8_u((var0 - 32)) + i32_load8_u((var0 - 1))))))))))))))))) + 8) & 0xFFFFFFFF) >> 4)) & 255) * 72340172838076673)
    i64_store(var0 + 224, ((i64_extend_u(((((i32_load8_u(var0 + 223) + (i32_load8_u((var0 - 25)) + (i32_load8_u(var0 + 191) + (i32_load8_u((var0 - 26)) + (i32_load8_u(var0 + 159) + (i32_load8_u((var0 - 27)) + (i32_load8_u(var0 + 127) + (i32_load8_u((var0 - 28)) + (i32_load8_u(var0 + 95) + (i32_load8_u((var0 - 29)) + (i32_load8_u(var0 + 63) + (i32_load8_u((var0 - 30)) + (i32_load8_u(var0 + 31) + (i32_load8_u((var0 - 31)) + (i32_load8_u((var0 - 32)) + i32_load8_u((var0 - 1))))))))))))))))) + 8) & 0xFFFFFFFF) >> 4)) & 255) * 72340172838076673))
    i64_store(var0 + 192, var1)
    i64_store(var0 + 160, var1)
    i64_store(var0 + 128, var1)
    i64_store(var0 + 96, var1)
    i64_store(var0 + 64, var1)
    i64_store(var0 + 32, var1)
    i64_store(var0, var1)


# ==========================================================
# $func1106
# ==========================================================
def func1106(var0):
    var1 = 0
    var1 = ((i64_extend_u(((((i32_load8_u(var0 + 223) + (i32_load8_u(var0 + 191) + (i32_load8_u(var0 + 159) + (i32_load8_u(var0 + 127) + (i32_load8_u(var0 + 95) + (i32_load8_u(var0 + 63) + (i32_load8_u((var0 - 1)) + i32_load8_u(var0 + 31)))))))) + 4) & 0xFFFFFFFF) >> 3)) & 255) * 72340172838076673)
    i64_store(var0 + 224, ((i64_extend_u(((((i32_load8_u(var0 + 223) + (i32_load8_u(var0 + 191) + (i32_load8_u(var0 + 159) + (i32_load8_u(var0 + 127) + (i32_load8_u(var0 + 95) + (i32_load8_u(var0 + 63) + (i32_load8_u((var0 - 1)) + i32_load8_u(var0 + 31)))))))) + 4) & 0xFFFFFFFF) >> 3)) & 255) * 72340172838076673))
    i64_store(var0 + 192, var1)
    i64_store(var0 + 160, var1)
    i64_store(var0 + 128, var1)
    i64_store(var0 + 96, var1)
    i64_store(var0 + 64, var1)
    i64_store(var0 + 32, var1)
    i64_store(var0, var1)


# ==========================================================
# $func1107
# ==========================================================
def func1107(var0):
    i64_store(var0 + 224, -9187201950435737472)
    i64_store(var0 + 192, -9187201950435737472)
    i64_store(var0 + 160, -9187201950435737472)
    i64_store(var0 + 128, -9187201950435737472)
    i64_store(var0 + 96, -9187201950435737472)
    i64_store(var0 + 64, -9187201950435737472)
    i64_store(var0 + 32, -9187201950435737472)
    i64_store(var0, -9187201950435737472)


# ==========================================================
# $func1108
# ==========================================================
def func1108(var0):
    var1 = 0
    var1 = ((i64_extend_u(((((i32_load8_u((var0 - 25)) + (i32_load8_u((var0 - 26)) + (i32_load8_u((var0 - 27)) + (i32_load8_u((var0 - 28)) + (i32_load8_u((var0 - 29)) + (i32_load8_u((var0 - 30)) + (i32_load8_u((var0 - 32)) + i32_load8_u((var0 - 31))))))))) + 4) & 0xFFFFFFFF) >> 3)) & 255) * 72340172838076673)
    i64_store(var0 + 224, ((i64_extend_u(((((i32_load8_u((var0 - 25)) + (i32_load8_u((var0 - 26)) + (i32_load8_u((var0 - 27)) + (i32_load8_u((var0 - 28)) + (i32_load8_u((var0 - 29)) + (i32_load8_u((var0 - 30)) + (i32_load8_u((var0 - 32)) + i32_load8_u((var0 - 31))))))))) + 4) & 0xFFFFFFFF) >> 3)) & 255) * 72340172838076673))
    i64_store(var0 + 192, var1)
    i64_store(var0 + 160, var1)
    i64_store(var0 + 128, var1)
    i64_store(var0 + 96, var1)
    i64_store(var0 + 64, var1)
    i64_store(var0 + 32, var1)
    i64_store(var0, var1)


# ==========================================================
# $func1109
# ==========================================================
def func1109(var0):
    var1 = 0
    var1 = ((((((i32_load8_u(var0 + 95) + (i32_load8_u((var0 - 29)) + (i32_load8_u(var0 + 63) + (i32_load8_u((var0 - 30)) + (i32_load8_u(var0 + 31) + (i32_load8_u((var0 - 31)) + (i32_load8_u((var0 - 32)) + i32_load8_u((var0 - 1))))))))) + 4) & 0xFFFFFFFF) >> 3) & 255) * 16843009)
    i32_store(var0 + 96, ((((((i32_load8_u(var0 + 95) + (i32_load8_u((var0 - 29)) + (i32_load8_u(var0 + 63) + (i32_load8_u((var0 - 30)) + (i32_load8_u(var0 + 31) + (i32_load8_u((var0 - 31)) + (i32_load8_u((var0 - 32)) + i32_load8_u((var0 - 1))))))))) + 4) & 0xFFFFFFFF) >> 3) & 255) * 16843009))
    i32_store(var0 + 64, var1)
    i32_store(var0 + 32, var1)
    i32_store(var0, var1)


# ==========================================================
# $func1110
# ==========================================================
def func1110(var0):
    var1 = 0
    var1 = ((i64_extend_u(((((i32_load8_u((var0 - 17)) + (i32_load8_u(var0 + 479) + (i32_load8_u((var0 - 18)) + (i32_load8_u(var0 + 447) + (i32_load8_u((var0 - 19)) + (i32_load8_u(var0 + 415) + (i32_load8_u((var0 - 20)) + (i32_load8_u(var0 + 383) + (i32_load8_u((var0 - 21)) + (i32_load8_u(var0 + 351) + (i32_load8_u((var0 - 22)) + (i32_load8_u(var0 + 319) + (i32_load8_u((var0 - 23)) + (i32_load8_u(var0 + 287) + (i32_load8_u((var0 - 24)) + (i32_load8_u(var0 + 255) + (i32_load8_u((var0 - 25)) + (i32_load8_u(var0 + 223) + (i32_load8_u((var0 - 26)) + (i32_load8_u(var0 + 191) + (i32_load8_u((var0 - 27)) + (i32_load8_u(var0 + 159) + (i32_load8_u((var0 - 28)) + (i32_load8_u(var0 + 127) + (i32_load8_u((var0 - 29)) + (i32_load8_u(var0 + 95) + (i32_load8_u((var0 - 30)) + (i32_load8_u(var0 + 63) + (i32_load8_u((var0 - 31)) + (i32_load8_u(var0 + 31) + (i32_load8_u((var0 - 1)) + i32_load8_u((var0 - 32))))))))))))))))))))))))))))))))) + 16) & 0xFFFFFFFF) >> 5)) & 255) * 72340172838076673)
    i64_store(var0 + 8, ((i64_extend_u(((((i32_load8_u((var0 - 17)) + (i32_load8_u(var0 + 479) + (i32_load8_u((var0 - 18)) + (i32_load8_u(var0 + 447) + (i32_load8_u((var0 - 19)) + (i32_load8_u(var0 + 415) + (i32_load8_u((var0 - 20)) + (i32_load8_u(var0 + 383) + (i32_load8_u((var0 - 21)) + (i32_load8_u(var0 + 351) + (i32_load8_u((var0 - 22)) + (i32_load8_u(var0 + 319) + (i32_load8_u((var0 - 23)) + (i32_load8_u(var0 + 287) + (i32_load8_u((var0 - 24)) + (i32_load8_u(var0 + 255) + (i32_load8_u((var0 - 25)) + (i32_load8_u(var0 + 223) + (i32_load8_u((var0 - 26)) + (i32_load8_u(var0 + 191) + (i32_load8_u((var0 - 27)) + (i32_load8_u(var0 + 159) + (i32_load8_u((var0 - 28)) + (i32_load8_u(var0 + 127) + (i32_load8_u((var0 - 29)) + (i32_load8_u(var0 + 95) + (i32_load8_u((var0 - 30)) + (i32_load8_u(var0 + 63) + (i32_load8_u((var0 - 31)) + (i32_load8_u(var0 + 31) + (i32_load8_u((var0 - 1)) + i32_load8_u((var0 - 32))))))))))))))))))))))))))))))))) + 16) & 0xFFFFFFFF) >> 5)) & 255) * 72340172838076673))
    i64_store(var0, var1)
    i64_store(var0 + 32, var1)
    i64_store(var0 + 40, var1)
    i64_store(var0 + 64, var1)
    i64_store(var0 + 72, var1)
    i64_store(var0 + 96, var1)
    i64_store(var0 + 104, var1)
    i64_store(var0 + 128, var1)
    i64_store(var0 + 136, var1)
    i64_store(var0 + 160, var1)
    i64_store(var0 + 168, var1)
    i64_store(var0 + 192, var1)
    i64_store(var0 + 200, var1)
    i64_store(var0 + 232, var1)
    i64_store(var0 + 224, var1)
    i64_store(var0 + 264, var1)
    i64_store(var0 + 256, var1)
    i64_store(var0 + 296, var1)
    i64_store(var0 + 288, var1)
    i64_store(var0 + 328, var1)
    i64_store(var0 + 320, var1)
    i64_store(var0 + 360, var1)
    i64_store(var0 + 352, var1)
    i64_store(var0 + 392, var1)
    i64_store(var0 + 384, var1)
    i64_store(var0 + 424, var1)
    i64_store(var0 + 416, var1)
    i64_store(var0 + 456, var1)
    i64_store(var0 + 448, var1)
    i64_store(var0 + 488, var1)
    i64_store(var0 + 480, var1)

