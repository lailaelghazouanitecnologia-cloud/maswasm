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
# $func408
# ==========================================================
def func408(var0, var1):
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
    var8 = i32_load16_u(var1 + 114)
    var5 = (i32_load16_u(var1 + 114) - 1)
    var4 = ((var0 * 404) + 9568096)
    var15 = i32_load(((var0 * 404) + 9568096) + 220)
    var9 = i32_load16_u(var1 + 112)
    var0 = (i32_load16_u(var1 + 112) - 1)
    var3 = ((i32_load16_u(var1 + 112) - 1) - i32_load(var4 + 216))
    var1 = ((i32_load8_u(var1 + 122) * 404) + 9568096)
    var16 = i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 220)
    var10 = (i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 220) + var8)
    var11 = i32_load(var1 + 216)
    var12 = (i32_load(var1 + 216) + var9)
    if (1 if ((i32_load(var1 + 216) + var9) + 1) < var9 else 0):
        break
    var7 = (var10 + 1)
    if (1 if (var10 + 1) < var8 else 0):
        break
    while True:  # loop $label5
        var4 = (var0 + 1)
        var1 = var5
        while True:  # loop $label4
            var2 = i32_load(9142440)
            if (1 if i32_load(9142440) <= var1 else 0):
                break
            if (1 if (var0 | var1) < 0 else 0):
                break
            if (1 if var0 < var2 else 0):
                break
            var1 = (var1 + 1)
            break
            var1 = (var1 + 1)
            var2 = (var2 + 2)
            var2 = (i32_load(9671128) + (i32_load((i32_load(9142840) + ((var4 + (((var1 + 1) + (var2 + 2)) * var2)) << 2))) * 132))
            if (1 if i32_load(38448) != i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9142840) + ((var4 + (((var1 + 1) + (var2 + 2)) * var2)) << 2))) * 132)) + 122) else 0):
                break
            var13 = func26(4)
            var14 = (func26(4) + 4)
            var6 = i32_load(var2)
            if i32_load(var2):
                i32_store(var2 + 4, var6)
            i32_store(var2 + 8, var14)
            i32_store(var2 + 4, var13)
            i32_store(var2, var13)
            # Unknown: memory.fill []
            if (1 if var1 != var7 else 0):
                continue
            break  # end loop
        var1 = (1 if var0 != var12 else 0)
        var0 = var4
        if var1:
            continue
        break  # end loop
    var13 = (var11 + 1)
    var0 = (var3 - 2)
    var14 = (var3 + var11)
    if (1 if (var3 - 2) >= (var3 + var11) else 0):
        break
    var2 = (var8 - 2)
    if (1 if (var8 - 2) >= var10 else 0):
        break
    while True:  # loop $label11
        var4 = (var0 + 1)
        var1 = var2
        while True:  # loop $label10
            var3 = i32_load(9142440)
            if (1 if i32_load(9142440) <= var1 else 0):
                break
            if (1 if (var0 | var1) < 0 else 0):
                break
            if (1 if var0 < var3 else 0):
                break
            var1 = (var1 + 1)
            break
            var1 = (var1 + 1)
            var3 = (var3 + 2)
            var3 = (i32_load(9671128) + (i32_load((i32_load(9142840) + ((var4 + (((var1 + 1) + (var3 + 2)) * var3)) << 2))) * 132))
            if (1 if i32_load(38448) != i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9142840) + ((var4 + (((var1 + 1) + (var3 + 2)) * var3)) << 2))) * 132)) + 122) else 0):
                break
            var6 = func26(4)
            var17 = (func26(4) + 4)
            var7 = i32_load(var3)
            if i32_load(var3):
                i32_store(var3 + 4, var7)
            i32_store(var3 + 8, var17)
            i32_store(var3 + 4, var6)
            i32_store(var3, var6)
            # Unknown: memory.fill []
            if (1 if var1 != var10 else 0):
                continue
            break  # end loop
        var0 = var4
        if (1 if var4 != var14 else 0):
            continue
        break  # end loop
    var3 = (var9 + var13)
    var0 = (var9 - 2)
    if (1 if (var9 - 2) >= var12 else 0):
        break
    var1 = (var5 - var15)
    var4 = ((var5 - var15) - 2)
    var15 = (var1 + var16)
    if (1 if ((var5 - var15) - 2) >= (var1 + var16) else 0):
        break
    while True:  # loop $label17
        var5 = (var0 + 1)
        var1 = var4
        while True:  # loop $label16
            var2 = i32_load(9142440)
            if (1 if i32_load(9142440) <= var1 else 0):
                break
            if (1 if (var0 | var1) < 0 else 0):
                break
            if (1 if var0 < var2 else 0):
                break
            var1 = (var1 + 1)
            break
            var1 = (var1 + 1)
            var2 = (var2 + 2)
            var2 = (i32_load(9671128) + (i32_load((i32_load(9142840) + ((var5 + (((var1 + 1) + (var2 + 2)) * var2)) << 2))) * 132))
            if (1 if i32_load(38448) != i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9142840) + ((var5 + (((var1 + 1) + (var2 + 2)) * var2)) << 2))) * 132)) + 122) else 0):
                break
            var6 = func26(4)
            var14 = (func26(4) + 4)
            var7 = i32_load(var2)
            if i32_load(var2):
                i32_store(var2 + 4, var7)
            i32_store(var2 + 8, var14)
            i32_store(var2 + 4, var6)
            i32_store(var2, var6)
            # Unknown: memory.fill []
            if (1 if var1 != var15 else 0):
                continue
            break  # end loop
        var0 = var5
        if (1 if var5 != var12 else 0):
            continue
        break  # end loop
    var0 = (var3 - 2)
    var6 = (var3 + var11)
    if (1 if (var3 - 2) >= (var3 + var11) else 0):
        break
    var4 = (var8 - 2)
    if (1 if (var8 - 2) >= var10 else 0):
        break
    while True:  # loop $label23
        var5 = (var0 + 1)
        var1 = var4
        while True:  # loop $label22
            var2 = i32_load(9142440)
            if (1 if i32_load(9142440) <= var1 else 0):
                break
            if (1 if (var0 | var1) < 0 else 0):
                break
            if (1 if var0 < var2 else 0):
                break
            var1 = (var1 + 1)
            break
            var1 = (var1 + 1)
            var2 = (var2 + 2)
            var2 = (i32_load(9671128) + (i32_load((i32_load(9142840) + ((var5 + (((var1 + 1) + (var2 + 2)) * var2)) << 2))) * 132))
            if (1 if i32_load(38448) != i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9142840) + ((var5 + (((var1 + 1) + (var2 + 2)) * var2)) << 2))) * 132)) + 122) else 0):
                break
            var3 = func26(4)
            var7 = (func26(4) + 4)
            var11 = i32_load(var2)
            if i32_load(var2):
                i32_store(var2 + 4, var11)
            i32_store(var2 + 8, var7)
            i32_store(var2 + 4, var3)
            i32_store(var2, var3)
            # Unknown: memory.fill []
            if (1 if var1 != var10 else 0):
                continue
            break  # end loop
        var0 = var5
        if (1 if var5 != var6 else 0):
            continue
        break  # end loop
    var0 = (var9 - 2)
    if (1 if (var9 - 2) >= var12 else 0):
        break
    var1 = (var8 + var13)
    var4 = ((var8 + var13) - 2)
    var9 = (var1 + var16)
    if (1 if ((var8 + var13) - 2) >= (var1 + var16) else 0):
        break
    while True:  # loop $label29
        var5 = (var0 + 1)
        var1 = var4
        while True:  # loop $label28
            var2 = i32_load(9142440)
            if (1 if i32_load(9142440) <= var1 else 0):
                break
            if (1 if (var0 | var1) < 0 else 0):
                break
            if (1 if var0 < var2 else 0):
                break
            var1 = (var1 + 1)
            break
            var1 = (var1 + 1)
            var2 = (var2 + 2)
            var2 = (i32_load(9671128) + (i32_load((i32_load(9142840) + ((var5 + (((var1 + 1) + (var2 + 2)) * var2)) << 2))) * 132))
            if (1 if i32_load(38448) != i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9142840) + ((var5 + (((var1 + 1) + (var2 + 2)) * var2)) << 2))) * 132)) + 122) else 0):
                break
            var3 = func26(4)
            var10 = (func26(4) + 4)
            var8 = i32_load(var2)
            if i32_load(var2):
                i32_store(var2 + 4, var8)
            i32_store(var2 + 8, var10)
            i32_store(var2 + 4, var3)
            i32_store(var2, var3)
            # Unknown: memory.fill []
            if (1 if var1 != var9 else 0):
                continue
            break  # end loop
        var0 = var5
        if (1 if var5 != var12 else 0):
            continue
        break  # end loop

