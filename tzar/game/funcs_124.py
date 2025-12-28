"""
Auto-generated from WAT. Contains 4 functions.
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
# $func310
# ==========================================================
def func310(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var5 = (var2 - var1)
    var6 = ((var2 - var1) >> 2)
    var3 = i32_load(var0 + 8)
    var4 = i32_load(var0)
    if (1 if ((var2 - var1) >> 2) <= ((i32_load(var0 + 8) - i32_load(var0)) >> 2) else 0):
        var5 = (i32_load(var0 + 4) - var4)
        var3 = (var1 + (i32_load(var0 + 4) - var4))
        var8 = (var5 >> 2)
        var5 = ((var1 + (i32_load(var0 + 4) - var4)) if (1 if var6 > (var5 >> 2) else 0) else var2)
        var7 = (((var1 + (i32_load(var0 + 4) - var4)) if (1 if var6 > (var5 >> 2) else 0) else var2) - var1)
        if (1 if var1 != var5 else 0):
            # Unknown: memory.copy []
        if (1 if var6 > var8 else 0):
            var1 = i32_load(var0 + 4)
            if (1 if var2 != var5 else 0):
                while True:  # loop $label0
                    i32_store(var1, i32_load(var3))
                    var1 = (var1 + 4)
                    var3 = (var3 + 4)
                    if (1 if (var3 + 4) != var2 else 0):
                        continue
                    break  # end loop
            i32_store(var0 + 4, var1)
            return var7
        i32_store(var0 + 4, (var4 + var7))
        return var1
    if var4:
        i32_store(var0 + 4, var4)
        i32_store(var0 + 8, 0)
        i64_store(var0, 0)
        var3 = 0
    if (1 if var5 < 0 else 0):
        break
    var4 = (var3 >> 1)
    var3 = (1073741823 if (1 if var3 >= 2147483644 else 0) else ((var3 >> 1) if (1 if var4 > var6 else 0) else var6))
    if (1 if (1073741823 if (1 if var3 >= 2147483644 else 0) else ((var3 >> 1) if (1 if var4 > var6 else 0) else var6)) >= 1073741824 else 0):
        break
    var4 = (var3 << 2)
    var3 = func26((var3 << 2))
    i32_store(var0 + 4, func26((var3 << 2)))
    i32_store(var0, var3)
    i32_store(var0 + 8, (var3 + var4))
    if (1 if var1 != var2 else 0):
        var0 = (((var5 - 4) & -4) + 4)
        # Unknown: memory.copy []
    else:
    i32_store((var0 + var3) + 4, var3)
    return (((var5 - 4) & -4) + 4)
    func42()
    raise RuntimeError('unreachable')
    return var1


# ==========================================================
# $func311
# ==========================================================
def func311(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var6 = (var2 - var1)
    var5 = ((var2 - var1) // 196)
    var3 = i32_load(var0 + 8)
    var4 = i32_load(var0)
    if (1 if ((var2 - var1) // 196) <= ((i32_load(var0 + 8) - i32_load(var0)) // 196) else 0):
        var6 = ((i32_load(var0 + 4) - var4) // 196)
        var3 = (var1 + (((i32_load(var0 + 4) - var4) // 196) * 196))
        var7 = ((var1 + (((i32_load(var0 + 4) - var4) // 196) * 196)) if (1 if var5 > var6 else 0) else var2)
        var8 = (((var1 + (((i32_load(var0 + 4) - var4) // 196) * 196)) if (1 if var5 > var6 else 0) else var2) - var1)
        if (1 if var1 != var7 else 0):
            # Unknown: memory.copy []
        if (1 if var5 > var6 else 0):
            var1 = i32_load(var0 + 4)
            if (1 if var2 != var7 else 0):
                while True:  # loop $label0
                    # Unknown: memory.copy []
                    var1 = (var1 + 196)
                    var3 = (var3 + 196)
                    if (1 if (var3 + 196) != var2 else 0):
                        continue
                    break  # end loop
            i32_store(var0 + 4, var1)
            return 196
        i32_store(var0 + 4, (var4 + ((var8 // 196) * 196)))
        return var3
    if var4:
        i32_store(var0 + 4, var4)
        i32_store(var0 + 8, 0)
        i64_store(var0, 0)
        var3 = 0
    if (1 if var5 >= 21913099 else 0):
        break
    var3 = (var3 // 196)
    var4 = ((var3 // 196) << 1)
    var3 = (21913098 if (1 if var3 >= 10956549 else 0) else (((var3 // 196) << 1) if (1 if var4 > var5 else 0) else var5))
    if (1 if (21913098 if (1 if var3 >= 10956549 else 0) else (((var3 // 196) << 1) if (1 if var4 > var5 else 0) else var5)) >= 21913099 else 0):
        break
    var4 = (var3 * 196)
    var3 = func26((var3 * 196))
    i32_store(var0 + 4, func26((var3 * 196)))
    i32_store(var0, var3)
    i32_store(var0 + 8, (var3 + var4))
    if (1 if var1 != var2 else 0):
        var0 = (var6 - 196)
        var0 = (((var6 - 196) - (var0 % 196)) + 196)
        # Unknown: memory.copy []
    else:
    i32_store((var0 + var3) + 4, var3)
    return (((var6 - 196) - (var0 % 196)) + 196)
    func42()
    raise RuntimeError('unreachable')
    return var1


# ==========================================================
# $qc
# Export: qc
# ==========================================================
def qc(var0, var1):
    """Export: qc"""
    var2 = 0
    var3 = 0
    var4 = 0
    if (1 if i32_load(51776) == 0 else 0):
        i32_store8(9215872, 1)
        var2 = i32_load(9216016)
        if (1 if i32_load(9216016) != i32_load(9216012) else 0):
            var3 = i32_load(9216008)
            break
        var3 = (i32_load(9216020) + var2)
        i32_store(9216012, (i32_load(9216020) + var2))
        var4 = i32_load(9216008)
        var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
        if var2:
            # Unknown: memory.copy []
        if var4:
            var2 = i32_load(9216016)
        i32_store(9216008, var3)
        i32_store(9216016, (var2 + 1))
        i32_store((var3 + (var2 << 2)), var0)
        var0 = i32_load(9216016)
        if (1 if i32_load(9216016) != i32_load(9216012) else 0):
            var2 = var3
            break
        var2 = (i32_load(9216020) + var0)
        i32_store(9216012, (i32_load(9216020) + var0))
        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        if var0:
            # Unknown: memory.copy []
        i32_store(9216008, var2)
        var0 = i32_load(9216016)
        i32_store(9216016, (var0 + 1))
        i32_store((var2 + (var0 << 2)), var1)
        return
    if var1:
        var1 = (var0 + 9686896)
        if i32_load8_u((var0 + 9686896)):
            break
        i32_store8(var1, 1)
        var1 = i32_load(((var0 << 2) + 9685872))
        if (1 if i32_load(((var0 << 2) + 9685872)) == 0 else 0):
            break
        # call_indirect via table[var1]
        return
    i32_store8((var0 + 9686896), 0)
    var1 = i32_load(((var0 << 2) + 9685872))
    if (1 if i32_load(((var0 << 2) + 9685872)) == 0 else 0):
        break
    # call_indirect via table[var1]


# ==========================================================
# $func344
# ==========================================================
def func344():
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var0 = i32_load(9561704)
    i32_store(9561716, i32_load(9561704))
    if (1 if i32_load(9561700) != var0 else 0):
        var1 = i32_load(9561696)
        break
    var1 = (i32_load(9561708) + var0)
    i32_store(9561700, (i32_load(9561708) + var0))
    var2 = i32_load(9561696)
    var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var0:
        # Unknown: memory.copy []
    if var2:
        var0 = i32_load(9561704)
    i32_store(9561696, var1)
    i32_store(9561704, (var0 + 1))
    i32_store((var1 + (var0 << 2)), 0)
    var3 = (i32_load(9142848) + 10)
    i32_store(9561712, (i32_load(9142848) + 10))
    var0 = i32_load(9561704)
    if (1 if i32_load(9561704) != i32_load(9561700) else 0):
        var2 = var1
        break
    var2 = (i32_load(9561708) + var0)
    i32_store(9561700, (i32_load(9561708) + var0))
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(9561696, var2)
    var0 = i32_load(9561704)
    i32_store(9561704, (var0 + 1))
    i32_store((var2 + (var0 << 2)), var3)
    var0 = i32_load(9561704)
    if (1 if i32_load(9561704) != i32_load(9561700) else 0):
        var1 = var2
        break
    var1 = (i32_load(9561708) + var0)
    i32_store(9561700, (i32_load(9561708) + var0))
    var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(9561696, var1)
    var0 = i32_load(9561704)
    i32_store(9561704, (var0 + 1))
    i32_store((var1 + (var0 << 2)), 3)

