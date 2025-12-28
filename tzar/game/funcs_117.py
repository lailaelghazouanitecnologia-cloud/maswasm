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
# $func103
# ==========================================================
def func103(var0):
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
    var4 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var1 = i32_load(9142872)
    if (1 if i32_load(9142872) == 0 else 0):
        break
    if (1 if var1 != i32_load16_u(var0 + 110) else 0):
        break
    var10 = i32_load8_u(var0 + 122)
    if (1 if i32_load8_u(var0 + 122) == i32_load(38564) else 0):
        break
    if i32_load8_u(9142917):
        break
    var11 = i32_load16_u(var0 + 112)
    var1 = ((var10 * 404) + 9568096)
    var12 = i32_load16_u(var0 + 114)
    var7 = ((i32_load16_u(var0 + 112) + ((i32_load(((var10 * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1)) + ((i32_load16_u(var0 + 114) + ((i32_load(var1 + 220) & 0xFFFFFFFF) >> 1)) << 16))
    var2 = i32_load(9216048)
    if i32_load(9216048):
        var5 = i32_load(9142848)
        var6 = i32_load(9216040)
        while True:  # loop $label2
            var1 = (var3 << 2)
            var8 = i32_load((var6 + (var3 << 2)))
            var1 = ((var5 - i32_load((var6 + (var1 | 4)))) * 25)
            if (1 if ((var5 - i32_load((var6 + (var1 | 4)))) * 25) <= 19999 else 0):
                var1 = ((var8 & 65535) - var11)
                var1 = (((var8 & 0xFFFFFFFF) >> 16) - var12)
                if (1 if (((((var8 & 65535) - var11) * var1) + ((((var8 & 0xFFFFFFFF) >> 16) - var12) * var1)) - 1) >= 3601 else 0):
                    break
                break
            var9 = (((1 if var7 == var8 else 0) & (1 if var1 < 35000 else 0)) | var9)
            var3 = (var3 + 2)
            if (1 if (var3 + 2) < var2 else 0):
                continue
            break  # end loop
        var3 = 0
        var6 = i32_load(9216040)
        var5 = i32_load(9142848)
        while True:  # loop $label3
            var1 = (var6 + ((var3 << 2) | 4))
            if (1 if ((var5 - i32_load((var6 + ((var3 << 2) | 4)))) * 25) >= 35001 else 0):
                i32_store((var6 + (var3 << 2)), var7)
                i32_store(var1, i32_load(9142848))
                var0 = i32_load(((var10 * 404) + 9568096) + 264)
                i32_store(var4 + 28, (var9 & 1))
                i32_store(var4 + 20, var12)
                i32_store(var4 + 16, var11)
                i32_store(var4 + 24, (1 if var0 == 1 else 0))
                break
            var3 = (var3 + 2)
            if (1 if (var3 + 2) < var2 else 0):
                continue
            break  # end loop
    if (1 if i32_load(9216044) != var2 else 0):
        var1 = i32_load(9216040)
        break
    var1 = (i32_load(9216052) + var2)
    i32_store(9216044, (i32_load(9216052) + var2))
    var5 = i32_load(9216040)
    var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var2:
        # Unknown: memory.copy []
    if var5:
        var2 = i32_load(9216048)
    i32_store(9216040, var1)
    i32_store(9216048, (var2 + 1))
    i32_store((var1 + (var2 << 2)), var7)
    var5 = i32_load(9142848)
    var3 = i32_load(9216048)
    if (1 if i32_load(9216048) != i32_load(9216044) else 0):
        var2 = var1
        break
    var2 = (i32_load(9216052) + var3)
    i32_store(9216044, (i32_load(9216052) + var3))
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var3:
        # Unknown: memory.copy []
    i32_store(9216040, var2)
    var3 = i32_load(9216048)
    i32_store(9216048, (var3 + 1))
    i32_store((var2 + (var3 << 2)), var5)
    var2 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264)
    var1 = i32_load16_u(var0 + 112)
    var0 = i32_load16_u(var0 + 114)
    i32_store(var4 + 12, (var9 & 1))
    i32_store(var4 + 4, var0)
    i32_store(var4, var1)
    i32_store(var4 + 8, (1 if var2 == 1 else 0))
    global global0
    global0 = (var4 + 32)


# ==========================================================
# $func105
# ==========================================================
def func105(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var2 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) != i32_load(var0 + 4) else 0):
        var3 = i32_load(var0)
        break
    var3 = (i32_load(var0 + 12) + var2)
    i32_store(var0 + 4, (i32_load(var0 + 12) + var2))
    var4 = i32_load(var0)
    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var2:
        # Unknown: memory.copy []
    if var4:
        var2 = i32_load(var0 + 8)
    i32_store(var0, var3)
    i32_store(var0 + 8, (var2 + 1))
    i32_store((var3 + (var2 << 2)), var1)

