"""
Auto-generated from WAT. Contains 2 functions.
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
# $func927
# ==========================================================
def func927(var0, var1):
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
    if (1 if i32_load8_u(var1 + 125) != 13 else 0):
        break
    var6 = i32_load16_u(var1 + 112)
    var3 = i32_load16_u(var1 + 114)
    var7 = ((i32_load8_u(var1 + 122) * 404) + 9568096)
    var8 = i32_load16_u(var1 + 110)
    if func56(i32_load16_u(var1 + 112), i32_load16_u(var1 + 114), ((i32_load8_u(var1 + 122) * 404) + 9568096), i32_load16_u(var1 + 110), 0, 0, 1, 1, 0):
        var2 = var6
        var0 = var3
        break
    var4 = i32_load(9142440)
    var0 = 0
    while True:  # loop $label3
        var5 = var0
        var2 = (var0 << 2)
        var0 = (i32_load((((var0 << 2) | 4) + 8611904)) + var3)
        if (1 if var4 <= (i32_load((((var0 << 2) | 4) + 8611904)) + var3) else 0):
            break
        var2 = (i32_load((var2 + 8611904)) + var6)
        if (1 if var4 <= (i32_load((var2 + 8611904)) + var6) else 0):
            break
        if (1 if (var0 | var2) < 0 else 0):
            break
        if func56(var2, var0, var7, var8, 0, 0, 1, 1, 0):
            break
        var4 = i32_load(9142440)
        var0 = (var5 + 2)
        if (1 if var5 < 5198 else 0):
            continue
        break  # end loop
    break
    i32_store8(var1 + 125, 0)
    i32_store16(var1 + 114, var0)
    i32_store16(var1 + 112, var2)
    var0 = i32_load8_u(var1 + 122)
    if (1 if i32_load8_u(((i32_load8_u(var1 + 122) * 404) + 9568096) + 377) == 0 else 0):
        break
    var5 = ((var0 * 404) + 9568096)
    var4 = i32_load(((var0 * 404) + 9568096) + 216)
    if (1 if i32_load(((var0 * 404) + 9568096) + 216) <= 0 else 0):
        break
    var2 = i32_load16_u(var1 + 114)
    var7 = (i32_load16_u(var1 + 114) + i32_load(var5 + 220))
    if (1 if (i32_load16_u(var1 + 114) + i32_load(var5 + 220)) <= var2 else 0):
        break
    var6 = i32_load16_u(var1 + 112)
    var8 = (var4 + i32_load16_u(var1 + 112))
    var9 = i32_load(var5 + 372)
    var0 = var6
    while True:  # loop $label7
        var3 = (var0 + 1)
        var10 = (var0 - var6)
        var11 = i32_load(9142840)
        var0 = var2
        while True:  # loop $label6
            if i32_load8_u((var9 + (var10 + ((var0 - var2) * var4)))):
                var0 = (var0 + 1)
                break
            var12 = (i32_load(9142440) + 2)
            var0 = (var0 + 1)
            i32_store((var11 + (((((i32_load(9142440) + 2) + (var0 + 1)) * var12) + var3) << 2)), i32_load(var5 + 212))
            if (1 if var0 != var7 else 0):
                continue
            break  # end loop
        var0 = var3
        if (1 if var3 < var8 else 0):
            continue
        break  # end loop
    func29(var1, 1)
    if i32_load(var1 + 40):
        break
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var0 = i32_load8_u(var1 + 122)
    var3 = i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 216)
    if (1 if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 216) <= 0 else 0):
        break
    var0 = i32_load(((var0 * 404) + 9568096) + 220)
    if (1 if i32_load(((var0 * 404) + 9568096) + 220) <= 0 else 0):
        break
    var6 = i32_load16_u(var1 + 114)
    var5 = (var0 + i32_load16_u(var1 + 114))
    var2 = i32_load16_u(var1 + 112)
    var4 = (var3 + i32_load16_u(var1 + 112))
    var7 = i32_load(9147376)
    var3 = i32_load(9142440)
    while True:  # loop $label11
        var0 = var6
        if (1 if var2 < var3 else 0):
            while True:  # loop $label10
                if (1 if var0 < var3 else 0):
                    if i32_load16_u((var7 + (((var0 * var3) + var2) << 1))):
                        break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) < var5 else 0):
                    continue
                break  # end loop
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var4 else 0):
            continue
        break  # end loop
    break
    var0 = i32_load8_u(var1 + 122)
    if (1 if i32_load8_u(var1 + 122) != i32_load(38600) else 0):
        if (1 if i32_load(38472) != var0 else 0):
            break
    func286(var1)
    break
    if (1 if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 20) == 0 else 0):
        break
    if (1 if i32_load8_u(9142916) == 0 else 0):
        break


# ==========================================================
# $func928
# ==========================================================
def func928(var0, var1):
    var2 = 0
    var2 = i32_load(9671128)
    var0 = (var2 + (var0 * 132))
    func376((i32_load(9671128) + (i32_load((var2 + (var0 * 132)) + 96) * 132)), (var2 + (var1 * 132)))
    func29(var0, 1)

