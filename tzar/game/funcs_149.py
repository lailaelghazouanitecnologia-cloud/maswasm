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
# $Lc
# Export: Lc
# ==========================================================
def Lc(var0):
    """Export: Lc"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var1 = (global0 - 128)
    global global0
    global0 = (global0 - 128)
    i64_store(var1 + 8, 0)
    i64_store(var1 + 16, 0)
    i64_store(var1, 0)
    i64_store(var1 + 104, 4294967296)
    i64_store(var1 + 120, 0)
    i64_store(var1 + 112, 2147483648000)
    var3 = i32_load(9568068)
    if (1 if i32_load(9568068) != i32_load(9568072) else 0):
        i32_store(var3 + 8, 0)
        i64_store(var3, 0)
        var4 = i32_load(var1 + 4)
        var2 = i32_load(var1)
        var5 = (i32_load(var1 + 4) - i32_load(var1))
        var0 = ((i32_load(var1 + 4) - i32_load(var1)) // 196)
        if (1 if var2 != var4 else 0):
            if (1 if var0 >= 21913099 else 0):
                break
            var2 = func26(var5)
            i32_store(var3 + 4, func26(var5))
            i32_store(var3, var2)
            i32_store(var3 + 8, (var2 + (var0 * 196)))
            var0 = i32_load(var1)
            var4 = i32_load(var1 + 4)
            if (1 if i32_load(var1) != i32_load(var1 + 4) else 0):
                while True:  # loop $label1
                    # Unknown: memory.copy []
                    var2 = (var2 + 196)
                    var0 = (var0 + 196)
                    if (1 if (var0 + 196) != var4 else 0):
                        continue
                    break  # end loop
            i32_store(var3 + 4, var2)
        i64_store(var3 + 12, 0)
        i32_store(var3 + 20, 0)
        var4 = i32_load(var1 + 16)
        var2 = i32_load(var1 + 12)
        var5 = (i32_load(var1 + 16) - i32_load(var1 + 12))
        var0 = ((i32_load(var1 + 16) - i32_load(var1 + 12)) // 196)
        if (1 if var2 != var4 else 0):
            if (1 if var0 >= 21913099 else 0):
                break
            var2 = func26(var5)
            i32_store(var3 + 16, func26(var5))
            i32_store(var3 + 12, var2)
            i32_store(var3 + 20, (var2 + (var0 * 196)))
            var4 = i32_load(var1 + 12)
            var5 = i32_load(var1 + 16)
            if (1 if i32_load(var1 + 12) != i32_load(var1 + 16) else 0):
                var0 = var4
                while True:  # loop $label3
                    # Unknown: memory.copy []
                    var2 = (var2 + 196)
                    var0 = (var0 + 196)
                    if (1 if (var0 + 196) != var5 else 0):
                        continue
                    break  # end loop
            i32_store(var3 + 16, var2)
        # Unknown: memory.copy []
        var0 = (var3 + 128)
        i32_store(9568068, (var3 + 128))
        break
    var0 = i32_load(9568068)
    var4 = i32_load(var1 + 12)
    var3 = i32_load(9568064)
    if var4:
        i32_store(var1 + 16, var4)
    var4 = i32_load(var1)
    if i32_load(var1):
        i32_store(var1 + 4, var4)
    global global0
    global0 = (var1 + 128)
    return (((var0 - var3) >> 7) - 1)
    func42()
    raise RuntimeError('unreachable')
    func42()
    raise RuntimeError('unreachable')
    return af(var4)


# ==========================================================
# $Ha
# Export: Ha
# ==========================================================
def Ha():
    """Export: Ha"""
    var0 = 0
    var0 = i32_load(9561692)
    if i32_load(9561692):
        i32_store(9561692, 0)
    i32_store8(9147212, 0)
    i32_store(9142912, 0)
    i32_store(9142892, 0)

