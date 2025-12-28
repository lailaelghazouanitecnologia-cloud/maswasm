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
# $cc
# Export: cc
# ==========================================================
def cc():
    """Export: cc"""
    var0 = 0
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
    var13 = 0
    var14 = 0
    var15 = 0
    var16 = 0
    var17 = 0
    var18 = 0
    var3 = i32_load(9671136)
    var12 = i32_load8_u(9671158)
    var14 = (3 if i32_load8_u(9671158) else 2)
    var10 = i32_load8_u(9671157)
    var11 = (1 if i32_load8_u(9671157) == 0 else 0)
    var2 = i32_load(9142440)
    if (1 if i32_load(9671136) <= (((3 if i32_load8_u(9671158) else 2) - (1 if i32_load8_u(9671157) == 0 else 0)) * (i32_load(9142440) * var2)) else 0):
        if (1 if var3 < 4 else 0):
            break
        var6 = i32_load(38448)
        var7 = i32_load(9671128)
        var1 = 3
        while True:  # loop $label2
            var4 = (var7 + (var1 * 132))
            if (1 if i32_load8_u((var7 + (var1 * 132)) + 125) == 3 else 0):
                break
            if (1 if var6 == i32_load8_u(var4 + 122) else 0):
                break
            var4 = i32_load16_u(var4 + 112)
            var0 = (((((i32_load16_u(var4 + 114) + (var2 * i32_load16_u(var4 + 112))) * var2) + var4) * var1) + var0)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var3 else 0):
                continue
            break  # end loop
        break
    if (1 if var2 == 0 else 0):
        break
    var7 = i32_load(9142840)
    var6 = (var2 + 2)
    var8 = (0 if var10 else (var2 + 2))
    var15 = (var2 & -2)
    var13 = (var2 & 1)
    var16 = (var2 - 1)
    while True:  # loop $label5
        var4 = var1
        var9 = (var1 * var2)
        var1 = (var1 + 1)
        var3 = 0
        var5 = 0
        if var16:
            while True:  # loop $label3
                var18 = (var3 | 1)
                var17 = i32_load((var7 + ((var1 + (((var3 | 1) + var8) * var6)) << 2)))
                if i32_load((var7 + ((var1 + (((var3 | 1) + var8) * var6)) << 2))):
                    var0 = ((var17 * (((var3 + var9) * var2) + var4)) + var0)
                var3 = (var3 + 2)
                var17 = i32_load((var7 + ((var1 + (((var3 + 2) + var8) * var6)) << 2)))
                if i32_load((var7 + ((var1 + (((var3 + 2) + var8) * var6)) << 2))):
                    var0 = ((var17 * (((var9 + var18) * var2) + var4)) + var0)
                var5 = (var5 + 2)
                if (1 if (var5 + 2) != var15 else 0):
                    continue
                break  # end loop
        if (1 if var13 == 0 else 0):
            break
        var5 = i32_load((var7 + ((var1 + (((var3 + var8) + 1) * var6)) << 2)))
        if (1 if i32_load((var7 + ((var1 + (((var3 + var8) + 1) * var6)) << 2))) == 0 else 0):
            break
        var0 = ((var5 * (((var3 + var9) * var2) + var4)) + var0)
        if (1 if var1 != var2 else 0):
            continue
        break  # end loop
    if (1 if (var10 | var12) == 0 else 0):
        break
    var12 = (var2 & -2)
    var15 = (var2 & 1)
    var8 = (var6 << var11)
    var1 = 0
    while True:  # loop $label8
        var4 = var1
        var9 = (var1 * var2)
        var1 = (var1 + 1)
        var3 = 0
        var5 = 0
        if var16:
            while True:  # loop $label6
                var11 = (var3 | 1)
                var13 = i32_load((var7 + ((var1 + (((var3 | 1) + var8) * var6)) << 2)))
                if i32_load((var7 + ((var1 + (((var3 | 1) + var8) * var6)) << 2))):
                    var0 = ((var13 * (((var3 + var9) * var2) + var4)) + var0)
                var3 = (var3 + 2)
                var13 = i32_load((var7 + ((var1 + (((var3 + 2) + var8) * var6)) << 2)))
                if i32_load((var7 + ((var1 + (((var3 + 2) + var8) * var6)) << 2))):
                    var0 = ((var13 * (((var9 + var11) * var2) + var4)) + var0)
                var5 = (var5 + 2)
                if (1 if (var5 + 2) != var12 else 0):
                    continue
                break  # end loop
        if (1 if var15 == 0 else 0):
            break
        var5 = i32_load((var7 + ((var1 + (((var3 + var8) + 1) * var6)) << 2)))
        if (1 if i32_load((var7 + ((var1 + (((var3 + var8) + 1) * var6)) << 2))) == 0 else 0):
            break
        var0 = ((var5 * (((var3 + var9) * var2) + var4)) + var0)
        if (1 if var1 != var2 else 0):
            continue
        break  # end loop
    var1 = (2 if var10 else 3)
    if (1 if (2 if var10 else 3) == var14 else 0):
        break
    var9 = (var2 & -2)
    var12 = (var2 & 1)
    var10 = (var1 * var6)
    var1 = 0
    while True:  # loop $label11
        var4 = var1
        var8 = (var1 * var2)
        var1 = (var1 + 1)
        var3 = 0
        var5 = 0
        if var16:
            while True:  # loop $label9
                var14 = (var3 | 1)
                var11 = i32_load((var7 + ((var1 + (((var3 | 1) + var10) * var6)) << 2)))
                if i32_load((var7 + ((var1 + (((var3 | 1) + var10) * var6)) << 2))):
                    var0 = ((var11 * (((var3 + var8) * var2) + var4)) + var0)
                var3 = (var3 + 2)
                var11 = i32_load((var7 + ((var1 + (((var3 + 2) + var10) * var6)) << 2)))
                if i32_load((var7 + ((var1 + (((var3 + 2) + var10) * var6)) << 2))):
                    var0 = ((var11 * (((var8 + var14) * var2) + var4)) + var0)
                var5 = (var5 + 2)
                if (1 if (var5 + 2) != var9 else 0):
                    continue
                break  # end loop
        if (1 if var12 == 0 else 0):
            break
        var5 = i32_load((var7 + ((var1 + (((var3 + var10) + 1) * var6)) << 2)))
        if (1 if i32_load((var7 + ((var1 + (((var3 + var10) + 1) * var6)) << 2))) == 0 else 0):
            break
        var0 = ((var5 * (((var3 + var8) * var2) + var4)) + var0)
        if (1 if var1 != var2 else 0):
            continue
        break  # end loop
    return var0


# ==========================================================
# $func309
# ==========================================================
def func309(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var5 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var4 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(var4 + 12, var0)
    i32_store(var4 + 8, (var0 + var1))
    i32_store(var3 + 24, i32_load(var4 + 12))
    i32_store(var3 + 28, i32_load(var4 + 8))
    global global0
    global0 = (var4 + 16)
    var4 = i32_load(var3 + 24)
    var7 = i32_load(var3 + 28)
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var6 = (var7 - var4)
    if (1 if var4 != var7 else 0):
        # Unknown: memory.copy []
    i32_store(var1 + 12, (var4 + var6))
    i32_store(var1 + 8, (var2 + var6))
    i32_store(var3 + 16, i32_load(var1 + 12))
    i32_store(var3 + 20, i32_load(var1 + 8))
    global global0
    global0 = (var1 + 16)
    i32_store(var3 + 12, (var0 + (i32_load(var3 + 16) - var0)))
    i32_store(var3 + 8, (var2 + (i32_load(var3 + 20) - var2)))
    i32_store(var5 + 8, i32_load(var3 + 12))
    i32_store(var5 + 12, i32_load(var3 + 8))
    global global0
    global0 = (var3 + 32)
    var0 = i32_load(var5 + 12)
    global global0
    global0 = (var5 + 16)
    return var0


# ==========================================================
# $func312
# ==========================================================
def func312(var0, var1):
    if ((i32_load8_u(var0 + 11) & 0xFFFFFFFF) >> 7):
        i32_store(var0 + 4, var1)
        return
    i32_store8(var0 + 11, ((i32_load8_u(var0 + 11) & 128) | var1))
    i32_store8(var0 + 11, (i32_load8_u(var0 + 11) & 127))

