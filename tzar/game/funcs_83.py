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
# $func238
# ==========================================================
def func238(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var5 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var6 = i32_load(9561692)
    var3 = (i32_load(9561692) + (var1 * 286704))
    var7 = (((i32_load(9561692) + (var1 * 286704)) + (var0 << 2)) + 281808)
    if i32_load((((i32_load(9561692) + (var1 * 286704)) + (var0 << 2)) + 281808)):
        break
    if (1 if i32_load(var3 + 283908) == i32_load(9142872) else 0):
        i32_store(var5 + 16, i32_load(39232))
        a_b()
    var4 = i32_load(((var0 * 404) + 9568096) + 368)
    if ((1 if var2 == 0 else 0) & (1 if i32_load(((var0 * 404) + 9568096) + 368) == 55 else 0)):
        break
    var3 = (var3 + 283908)
    if var4:
        # call_indirect via table[var4]
        if (1 if var4 == 55 else 0):
            break
    i32_store(var7, 1)
    if (1 if i32_load(var3) == i32_load(9142872) else 0):
        i32_store(var5, (i32_load(i32_load(((var0 * 404) + 9568096) + 180) + 8) * 48))
        a_b()
    if i32_load8_u(9142905):
        break
    i32_store((((var6 + (var1 * 286704)) + (var0 << 2)) + 280616), ((i32_load(9142848) * 25) - ((((i32_load(((var0 * 404) + 9568096) + 116) * i32_load(i32_load(9142424) + 132)) * 1000) & 0xFFFFFFFF) // 100)))
    i32_store((((var6 + (var1 * 286704)) + (var0 << 2)) + 282828), 0)
    if (1 if i32_load(var3) != i32_load(9142872) else 0):
        break
    var2 = ((var0 * 404) + 9568096)
    if (1 if i32_load(((var0 * 404) + 9568096) + 244) == 0 else 0):
        break
    var1 = 0
    while True:  # loop $label5
        var6 = i32_load((i32_load(var2 + 240) + (var1 << 2)))
        if i32_load8_u(9147141):
            break
        var0 = 0
        var3 = i32_load(9671120)
        if (1 if i32_load(9671120) == 0 else 0):
            break
        while True:  # loop $label4
            var4 = i32_load(((var0 << 2) + 9263072))
            if (1 if i32_load(((var0 << 2) + 9263072)) == 0 else 0):
                break
            if (1 if i32_load(var4 + 12) != var6 else 0):
                break
            if i32_load8_u(var4 + 24):
                break
            break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var3 else 0):
                continue
            break  # end loop
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < i32_load(var2 + 244) else 0):
            continue
        break  # end loop
    global global0
    global0 = (var5 + 32)


# ==========================================================
# $func239
# ==========================================================
def func239(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var2 = (var0 * 286704)
    var1 = ((var0 * 286704) + i32_load(9561692))
    i32_store((((var0 * 286704) + i32_load(9561692)) + 281784), var0)
    if (1 if i32_load(9147132) == 0 else 0):
        var0 = i32_load(9142892)
        var0 = (-1 if (1 if (var0 * 255) > 1073741823 else 0) else (i32_load(9142892) * 1020))
        var3 = func26((-1 if (1 if (var0 * 255) > 1073741823 else 0) else (i32_load(9142892) * 1020)))
        # Unknown: memory.fill []
        i32_store(var1 + 278556, var3)
        var1 = func26(var0)
        # Unknown: memory.fill []
        i32_store(((i32_load(9561692) + var2) + 278560), var1)
        var1 = func26(var0)
        # Unknown: memory.fill []
        i32_store(((i32_load(9561692) + var2) + 278564), var1)
        var1 = func26(var0)
        # Unknown: memory.fill []
        i32_store(((i32_load(9561692) + var2) + 278568), var1)
        var0 = func26(16)
        i32_store(func26(16) + 4, 21000)
        i32_store(var0, func26(84000))
        i64_store(var0 + 8, 90194313216000)
        i32_store(((i32_load(9561692) + var2) + 278572), var0)

