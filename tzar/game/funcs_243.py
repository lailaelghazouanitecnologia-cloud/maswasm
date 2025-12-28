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
# $func247
# ==========================================================
def func247(var0, var1):
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
    var6 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    if (1 if i32_load8_u(var1 + 125) == 3 else 0):
        break
    var9 = i32_load(var0 + 16)
    # br_table ['$label1', '$label2', '$label3', '$label4', '$label5']
    _br_idx = i32_load(var0 + 8)
    break  # br_table
    var4 = (5 if (1 if var9 == 1 else 0) else 0)
    var3 = (i32_load(var0 + 24) + ((i32_load(var0 + 40) & 0xFFFFFFFF) >> 1))
    var2 = (i32_load(var0 + 20) + ((i32_load(var0 + 28) & 0xFFFFFFFF) >> 1))
    break
    var2 = i32_load(var0 + 36)
    i64_store(var6 + 16, i64_load(var0 + 72))
    i64_store(var6 + 8, i64_load(var0 + 64))
    var7 = func300(var2, (var6 + 8), var1)
    break
    var4 = i32_load(var0 + 104)
    if (1 if i32_load(var0 + 104) == 0 else 0):
        break
    var11 = i32_load(var0 + 96)
    var12 = i32_load16_u(var1 + 114)
    var13 = i32_load16_u(var1 + 112)
    var14 = i32_load(9671128)
    var8 = i32_load(var1 + 28)
    var2 = 2147483647
    var0 = 0
    while True:  # loop $label7
        var3 = i32_load((var11 + (var0 << 2)))
        if (1 if var8 != i32_load((var11 + (var0 << 2))) else 0):
            var3 = (var14 + (var3 * 132))
            var10 = ((i32_load16_u((var14 + (var3 * 132)) + 114) - var12) << 1)
            var10 = ((i32_load16_u(var3 + 112) - var13) << 1)
            var10 = ((((i32_load16_u((var14 + (var3 * 132)) + 114) - var12) << 1) * var10) + (((i32_load16_u(var3 + 112) - var13) << 1) * var10))
            var10 = (1 if var2 > var10 else 0)
            var2 = (((((i32_load16_u((var14 + (var3 * 132)) + 114) - var12) << 1) * var10) + (((i32_load16_u(var3 + 112) - var13) << 1) * var10)) if (1 if var2 > var10 else 0) else var2)
            var7 = (i32_load(var3 + 28) if var10 else var7)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var4 else 0):
            continue
        break  # end loop
    break
    var4 = i32_load(9140300)
    if (1 if i32_load(9140300) == 0 else 0):
        break
    var11 = i32_load16_u(var1 + 114)
    var12 = i32_load16_u(var1 + 112)
    var13 = i32_load(9671128)
    var14 = i32_load(var1 + 28)
    var2 = 2147483647
    var0 = 0
    while True:  # loop $label8
        var3 = i32_load(((var0 << 2) + 8451904))
        if (1 if var14 != i32_load(((var0 << 2) + 8451904)) else 0):
            var3 = (var13 + (var3 * 132))
            var8 = ((i32_load16_u((var13 + (var3 * 132)) + 114) - var11) << 1)
            var8 = ((i32_load16_u(var3 + 112) - var12) << 1)
            var8 = ((((i32_load16_u((var13 + (var3 * 132)) + 114) - var11) << 1) * var8) + (((i32_load16_u(var3 + 112) - var12) << 1) * var8))
            var8 = (1 if var2 > var8 else 0)
            var2 = (((((i32_load16_u((var13 + (var3 * 132)) + 114) - var11) << 1) * var8) + (((i32_load16_u(var3 + 112) - var12) << 1) * var8)) if (1 if var2 > var8 else 0) else var2)
            var7 = (i32_load(var3 + 28) if var8 else var7)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var4 else 0):
            continue
        break  # end loop
    var4 = 0
    var2 = 0
    var3 = 0
    if (1 if var7 == 0 else 0):
        break
    # br_table ['$label9', '$label10', '$label11', '$label12', '$label13', '$label14', '$label15', '$label16', '$label17']
    _br_idx = var9
    break  # br_table
    if (1 if var7 == 0 else 0):
        var7 = 0
        break
    i32_store(var6 + 32, i32_load(var1 + 28))
    var5 = func161((i32_load(9671128) + (var7 * 132)), (var6 + 32), 1)
    break
    var5 = 6
    break
    var5 = 1
    break
    var5 = 4
    break
    var5 = 25
    break
    i64_store(var6 + 48, 4294967296)
    i32_store(var6 + 36, var3)
    i32_store(var6 + 32, var2)
    i32_store(var6 + 40, var7)
    i32_store(var6 + 56, 0)
    i32_store(var6 + 44, (6 if var7 else 0))
    i32_store(var6 + 28, i32_load(var1 + 28))
    break
    if var7:
        var0 = (i32_load(9671128) + (var7 * 132))
        var2 = ((i32_load8_u((i32_load(9671128) + (var7 * 132)) + 122) * 404) + 9568096)
        var3 = (((i32_load(((i32_load8_u((i32_load(9671128) + (var7 * 132)) + 122) * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1) + i32_load16_u(var0 + 114))
        var2 = (i32_load16_u(var0 + 112) + ((i32_load(var2 + 216) & 0xFFFFFFFF) >> 1))
    i64_store(var6 + 52, 0)
    i64_store(var6 + 44, 0)
    i32_store(var6 + 40, -1)
    i32_store(var6 + 36, var3)
    i32_store(var6 + 32, var2)
    i32_store(var6 + 28, i32_load(var1 + 28))
    break
    if (1 if var9 != 8 else 0):
        break
    if (1 if var7 == 0 else 0):
        break
    var2 = i32_load(var1 + 20)
    if (1 if i32_load(var1 + 20) == 0 else 0):
        var0 = func26(16)
        i32_store(func26(16) + 4, 7)
        i32_store(var0, func26(28))
        i64_store(var0 + 8, 4294967296)
        i32_store(var1 + 20, var0)
        var5 = (var0 + 8)
        break
    var3 = 0
    i32_store(var2 + 8, 0)
    var5 = (var2 + 8)
    if (1 if i32_load(var2 + 4) == 0 else 0):
        break
    var0 = var2
    var4 = i32_load(var0)
    var3 = 0
    break
    var0 = i32_load(var2 + 12)
    i32_store(var2 + 4, i32_load(var2 + 12))
    var9 = i32_load(var2)
    var4 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    var0 = var2
    if var9:
        var3 = i32_load(var2 + 8)
        var0 = i32_load(var1 + 20)
    i32_store(var2, var4)
    i32_store(var5, (var3 + 1))
    i32_store((var4 + (var3 << 2)), 1)
    var3 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) != i32_load(var0 + 4) else 0):
        var4 = i32_load(var0)
        var2 = var0
        break
    var2 = (i32_load(var0 + 12) + var3)
    i32_store(var0 + 4, (i32_load(var0 + 12) + var3))
    var5 = i32_load(var0)
    var4 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var3:
        # Unknown: memory.copy []
    var2 = var0
    if var5:
        var3 = i32_load(var0 + 8)
        var2 = i32_load(var1 + 20)
    i32_store(var0, var4)
    i32_store(var0 + 8, (var3 + 1))
    i32_store((var4 + (var3 << 2)), 2)
    var3 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) != i32_load(var2 + 4) else 0):
        var4 = i32_load(var2)
        var0 = var2
        break
    var0 = (i32_load(var2 + 12) + var3)
    i32_store(var2 + 4, (i32_load(var2 + 12) + var3))
    var5 = i32_load(var2)
    var4 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var3:
        # Unknown: memory.copy []
    var0 = var2
    if var5:
        var3 = i32_load(var2 + 8)
        var0 = i32_load(var1 + 20)
    i32_store(var2, var4)
    i32_store(var2 + 8, (var3 + 1))
    i32_store((var4 + (var3 << 2)), 0)
    var3 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) != i32_load(var0 + 4) else 0):
        var4 = i32_load(var0)
        var2 = var0
        break
    var2 = (i32_load(var0 + 12) + var3)
    i32_store(var0 + 4, (i32_load(var0 + 12) + var3))
    var5 = i32_load(var0)
    var4 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var3:
        # Unknown: memory.copy []
    var2 = var0
    if var5:
        var3 = i32_load(var0 + 8)
        var2 = i32_load(var1 + 20)
    i32_store(var0, var4)
    i32_store(var0 + 8, (var3 + 1))
    i32_store((var4 + (var3 << 2)), 0)
    var3 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) != i32_load(var2 + 4) else 0):
        var4 = i32_load(var2)
        var0 = var2
        break
    var0 = (i32_load(var2 + 12) + var3)
    i32_store(var2 + 4, (i32_load(var2 + 12) + var3))
    var5 = i32_load(var2)
    var4 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var3:
        # Unknown: memory.copy []
    var0 = var2
    if var5:
        var3 = i32_load(var2 + 8)
        var0 = i32_load(var1 + 20)
    i32_store(var2, var4)
    i32_store(var2 + 8, (var3 + 1))
    i32_store((var4 + (var3 << 2)), var7)
    var3 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) != i32_load(var0 + 4) else 0):
        var4 = i32_load(var0)
        var2 = var0
        break
    var2 = (i32_load(var0 + 12) + var3)
    i32_store(var0 + 4, (i32_load(var0 + 12) + var3))
    var5 = i32_load(var0)
    var4 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var3:
        # Unknown: memory.copy []
    var2 = var0
    if var5:
        var3 = i32_load(var0 + 8)
        var2 = i32_load(var1 + 20)
    i32_store(var0, var4)
    i32_store(var0 + 8, (var3 + 1))
    i32_store((var4 + (var3 << 2)), 0)
    var3 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) != i32_load(var2 + 4) else 0):
        var4 = i32_load(var2)
        var0 = var2
        break
    var0 = (i32_load(var2 + 12) + var3)
    i32_store(var2 + 4, (i32_load(var2 + 12) + var3))
    var5 = i32_load(var2)
    var4 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var3:
        # Unknown: memory.copy []
    var0 = var2
    if var5:
        var3 = i32_load(var2 + 8)
        var0 = i32_load(var1 + 20)
    i32_store(var2, var4)
    i32_store(var2 + 8, (var3 + 1))
    i32_store((var4 + (var3 << 2)), 0)
    var3 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) != i32_load(var0 + 4) else 0):
        var4 = i32_load(var0)
        var2 = var0
        break
    var2 = (i32_load(var0 + 12) + var3)
    i32_store(var0 + 4, (i32_load(var0 + 12) + var3))
    var5 = i32_load(var0)
    var4 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var3:
        # Unknown: memory.copy []
    var2 = var0
    if var5:
        var3 = i32_load(var0 + 8)
        var2 = i32_load(var1 + 20)
    i32_store(var0, var4)
    i32_store(var0 + 8, (var3 + 1))
    i32_store((var4 + (var3 << 2)), 5)
    var0 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) != i32_load(var2 + 4) else 0):
        var3 = i32_load(var2)
        break
    var3 = (i32_load(var2 + 12) + var0)
    i32_store(var2 + 4, (i32_load(var2 + 12) + var0))
    var4 = i32_load(var2)
    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var0:
        # Unknown: memory.copy []
    if var4:
        var0 = i32_load(var2 + 8)
    i32_store(var2, var3)
    i32_store(var2 + 8, (var0 + 1))
    i32_store((var3 + (var0 << 2)), 0)
    break
    var0 = (var9 - 9)
    if (1 if (var9 - 9) > 21 else 0):
        break
    var5 = i32_load(((var0 << 2) + 10196))
    if (1 if var7 == 0 else 0):
        break
    if (1 if i32_load8_u(((var5 * 40) + 9671200) + 16) == 0 else 0):
        break
    var0 = (var7 * 132)
    var7 = 0
    var0 = (var0 + i32_load(9671128))
    var2 = ((i32_load8_u((var0 + i32_load(9671128)) + 122) * 404) + 9568096)
    var3 = (((i32_load(((i32_load8_u((var0 + i32_load(9671128)) + 122) * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1) + i32_load16_u(var0 + 114))
    var2 = (i32_load16_u(var0 + 112) + ((i32_load(var2 + 216) & 0xFFFFFFFF) >> 1))
    global global0
    global0 = (var6 - -64)

