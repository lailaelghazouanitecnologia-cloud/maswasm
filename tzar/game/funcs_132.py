"""
Auto-generated from WAT. Contains 5 functions.
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
# $Cd
# Export: Cd
# ==========================================================
def Cd(var0):
    """Export: Cd"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var1 = i32_load(9568088)
    if (i32_load(i32_load(9568088) + 104) if var0 else 1):
        return i32_load(var1 + 96)
    while True:  # loop $label1
        var3 = i32_load(var1 + 104)
        if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
            var2 = i32_load(var1 + 96)
            break
        var2 = (i32_load(var1 + 108) + var3)
        i32_store(var1 + 100, (i32_load(var1 + 108) + var3))
        var4 = i32_load(var1 + 96)
        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        if var3:
            # Unknown: memory.copy []
        if var4:
            var3 = i32_load(var1 + 104)
        i32_store(var1 + 96, var2)
        i32_store(var1 + 104, (var3 + 1))
        i32_store((var2 + (var3 << 2)), 0)
        var5 = (var5 + 1)
        if (1 if (var5 + 1) != var0 else 0):
            continue
        break  # end loop
    return var2


# ==========================================================
# $Re
# Export: Re
# ==========================================================
def Re(var0):
    """Export: Re"""
    var1 = 0
    var1 = i32_load(9687204)
    if i32_load(9687204):
        i32_store(9687204, 0)
    var1 = func26((var0 + 4))
    i32_store(9687208, var0)
    i32_store(9687204, var1)
    return var1


# ==========================================================
# $qa
# Export: qa
# ==========================================================
def qa():
    """Export: qa"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var3 = i32_load(9561728)
    var1 = i32_load(9561704)
    if (1 if i32_load(9561704) == 0 else 0):
        break
    var4 = i32_load(var3 + 4)
    var5 = i32_load(9561696)
    while True:  # loop $label1
        var6 = ((var0 << 2) + var5)
        if (1 if i32_load(((var0 << 2) + var5) + 4) >= var4 else 0):
            break
        var0 = (i32_load(var6 + 8) + var0)
        if (1 if (i32_load(var6 + 8) + var0) < var1 else 0):
            continue
        break  # end loop
    var0 = 0
    i32_store(9561704, var0)
    if i32_load(9561732):
        while True:  # loop $label3
            var5 = i32_load((var3 + (var2 << 2)))
            if (1 if i32_load(9561700) != var0 else 0):
                var1 = i32_load(9561696)
                break
            var1 = (i32_load(9561708) + var0)
            i32_store(9561700, (i32_load(9561708) + var0))
            var4 = i32_load(9561696)
            var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
            if var0:
                # Unknown: memory.copy []
            if var4:
                var3 = i32_load(9561728)
                var0 = i32_load(9561704)
            i32_store(9561696, var1)
            i32_store(9561704, (var0 + 1))
            i32_store((var1 + (var0 << 2)), var5)
            var0 = i32_load(9561704)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < i32_load(9561732) else 0):
                continue
            break  # end loop
    i32_store(9561828, var0)
    if (1 if i32_load(9561700) != var0 else 0):
        var2 = i32_load(9561696)
        break
    var2 = (i32_load(9561708) + var0)
    i32_store(9561700, (i32_load(9561708) + var0))
    var1 = i32_load(9561696)
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var0:
        # Unknown: memory.copy []
    if var1:
        var3 = i32_load(9561728)
        var0 = i32_load(9561704)
    i32_store(9561696, var2)
    i32_store(9561704, (var0 + 1))
    i32_store((var2 + (var0 << 2)), 0)
    var3 = (i32_load((((i32_load(9561732) << 2) + var3) - 8)) + 10)
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
    i32_store((var1 + (var0 << 2)), var3)
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
    i32_store((var2 + (var0 << 2)), 3)
    var2 = i32_load(9561728)
    if i32_load(9561728):
        i32_store(9561728, 0)


# ==========================================================
# $pa
# Export: pa
# ==========================================================
def pa(var0):
    """Export: pa"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var0 = (i32_load(9561836) + var0)
    i32_store(9561824, (i32_load(9561836) + var0))
    var3 = (((var0 * 250) & 0xFFFFFFFF) // 25)
    i32_store(59176, (((var0 * 250) & 0xFFFFFFFF) // 25))
    var0 = i32_load(59160)
    if (1 if i32_load(59160) < var3 else 0):
        if (1 if ((var3 - var0) * 25) > 249 else 0):
            break
        break
    if (1 if var0 <= var3 else 0):
        break
    i32_store(59160, var3)
    var0 = 0
    var1 = i32_load(9561704)
    if i32_load(9561704):
        var0 = i32_load(9561828)
        i32_store((i32_load(9561696) + (i32_load(9561828) << 2)) + 8, (var1 - var0))
        var0 = i32_load(9561704)
    i32_store(9561828, var0)
    if (1 if i32_load(9561700) != var0 else 0):
        var2 = i32_load(9561696)
        break
    var1 = (i32_load(9561708) + var0)
    i32_store(9561700, (i32_load(9561708) + var0))
    var4 = i32_load(9561696)
    var2 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var0:
        # Unknown: memory.copy []
    if var4:
        var0 = i32_load(9561704)
    i32_store(9561696, var2)
    i32_store(9561704, (var0 + 1))
    i32_store((var2 + (var0 << 2)), 0)
    var4 = (var3 + 10)
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
    i32_store((var1 + (var0 << 2)), var4)
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
    i32_store((var2 + (var0 << 2)), 3)


# ==========================================================
# $ra
# Export: ra
# ==========================================================
def ra(var0):
    """Export: ra"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var1 = i32_load(9561728)
    if (1 if i32_load(i32_load(9561728) + 4) == -1 else 0):
        var0 = i32_load(var1 + 8)
        i32_store(59164, i32_load(var1 + 8))
        if (1 if var0 == i32_load(9142384) else 0):
            break
        var0 = 3
        var4 = i32_load(9561732)
        if (1 if i32_load(9561732) <= 3 else 0):
            break
        while True:  # loop $label3
            var2 = (var1 + (var0 << 2))
            var3 = i32_load((var1 + (var0 << 2)) + 4)
            var5 = (var0 + 3)
            var6 = (i32_load((var1 + (var0 << 2)) + 4) + (var0 + 3))
            var7 = i32_load(var2 + 8)
            var0 = ((i32_load((var1 + (var0 << 2)) + 4) + (var0 + 3)) + i32_load(var2 + 8))
            var2 = i32_load(var2)
            if (1 if i32_load(var2) > 255 else 0):
                break
            var2 = ((var2 << 3) + 9213824)
            var8 = i32_load(((var2 << 3) + 9213824))
            if (1 if i32_load(((var2 << 3) + 9213824)) == 0 else 0):
                break
            var6 = ((var1 + (var6 << 2)) if var7 else 0)
            var5 = ((var1 + (var5 << 2)) if var3 else 0)
            var7 = i32_load(var2 + 4)
            if i32_load(var2 + 4):
                # call_indirect via table[var7]
                if (1 if call_indirect(var7) == 0 else 0):
                    break
            else:
            # call_indirect via table[var8]
            if (1 if var0 < var4 else 0):
                continue
            break  # end loop
        i32_store(59164, 0)
        var1 = i32_load(9561728)
        if i32_load(9561728):
            break
        break
    if i32_load8_u(9140304):
        break
    var1 = i32_load(9561704)
    if (1 if i32_load(9561704) != i32_load(9561700) else 0):
        var3 = i32_load(9561696)
        break
    var3 = (i32_load(9561708) + var1)
    i32_store(9561700, (i32_load(9561708) + var1))
    var2 = i32_load(9561696)
    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var1:
        # Unknown: memory.copy []
    if var2:
        var1 = i32_load(9561704)
    i32_store(9561696, var3)
    i32_store(9561704, (var1 + 1))
    var4 = 2
    i32_store((var3 + (var1 << 2)), var0)
    var1 = i32_load(9561728)
    if (1 if i32_load(9561732) > 2 else 0):
        while True:  # loop $label6
            var5 = i32_load((var1 + (var4 << 2)))
            var0 = i32_load(9561704)
            if (1 if i32_load(9561704) == i32_load(9561700) else 0):
                var2 = (i32_load(9561708) + var0)
                i32_store(9561700, (i32_load(9561708) + var0))
                var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                if var0:
                    # Unknown: memory.copy []
                i32_store(9561696, var2)
                var1 = i32_load(9561728)
                var3 = var2
                var0 = i32_load(9561704)
            i32_store(9561704, (var0 + 1))
            i32_store((var3 + (var0 << 2)), var5)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < i32_load(9561732) else 0):
                continue
            break  # end loop
    if var1:
        break
    break
    i32_store(59164, 0)
    return af(var1)

