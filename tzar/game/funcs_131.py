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
# $Ic
# Export: Ic
# ==========================================================
def Ic(var0):
    """Export: Ic"""
    var1 = 0
    var2 = 0
    if (1 if i32_load(9142892) == 0 else 0):
        break
    var1 = i32_load(9561692)
    if (1 if i32_load(9561692) == 0 else 0):
        break
    var0 = (var0 + 1)
    i32_store(9142892, (var0 + 1))
    var2 = (i64_extend_u(var0) * 286704)
    var0 = (-1 if i32(((var2 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var0) * 286704)))
    var1 = func26((-1 if i32(((var2 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var0) * 286704))))
    # Unknown: memory.fill []
    i32_store(9561692, var1)


# ==========================================================
# $ye
# Export: ye
# ==========================================================
def ye(var0):
    """Export: ye"""
    var1 = 0
    var2 = 0
    i32_store8(9147152, 1)
    if (1 if i32_load8_u(9147212) == 0 else 0):
        i32_store(9142892, 3)
        var1 = i32_load(9142424)
        if i32_load(9142424):
            i32_store(9142424, 0)
        var2 = (var0 << 2)
        var1 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        i32_store(9142428, var0)
        i32_store(9142424, var1)
        if var0:
            # Unknown: memory.copy []
        else:
        i32_store(i32_load(var1), var0)
    return var2


# ==========================================================
# $func604
# ==========================================================
def func604(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var7 = i32_load(9561692)
    while True:  # loop $label4
        var0 = ((var3 * 404) + 9568096)
        if (1 if i32_load(((var3 * 404) + 9568096) + 264) != 2 else 0):
            break
        if (1 if i32_load(var0 + 268) > 2 else 0):
            break
        var4 = i32_load(((var7 + (var3 << 2)) + 284636))
        if (1 if i32_load(((var7 + (var3 << 2)) + 284636)) == 0 else 0):
            break
        var5 = 0
        var0 = i32_load(var4 + 8)
        if (1 if i32_load(var4 + 8) == 0 else 0):
            break
        while True:  # loop $label3
            var1 = i32_load((i32_load(var4) + (var5 << 2)))
            if (1 if i32_load((i32_load(var4) + (var5 << 2))) == 0 else 0):
                break
            var2 = i32_load(9671128)
            var1 = (i32_load(9671128) + (var1 * 132))
            var6 = i32_load((i32_load(9671128) + (var1 * 132)) + 36)
            if (1 if i32_load((i32_load(9671128) + (var1 * 132)) + 36) == 0 else 0):
                break
            if (1 if i32_load(9142872) != i32_load16_u((var2 + (var6 * 132)) + 110) else 0):
                break
            var6 = i32_load(var1 + 28)
            var1 = i32_load(9681836)
            if (1 if i32_load(9681836) != i32_load(9681832) else 0):
                var0 = i32_load(9681828)
                break
            var0 = (i32_load(9681840) + var1)
            i32_store(9681832, (i32_load(9681840) + var1))
            var2 = i32_load(9681828)
            var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
            if var1:
                # Unknown: memory.copy []
            if var2:
                var1 = i32_load(9681836)
            i32_store(9681828, var0)
            i32_store(9681836, (var1 + 1))
            i32_store((var0 + (var1 << 2)), var6)
            var0 = i32_load(var4 + 8)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) < var0 else 0):
                continue
            break  # end loop
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != 255 else 0):
            continue
        break  # end loop
    func172(1)


# ==========================================================
# $zd
# Export: zd
# ==========================================================
def zd(var0):
    """Export: zd"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var4 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var1 = i32_load(9568088)
    if i32_load(i32_load(9568088) + 104):
        var0 = i32_load(var1 + 96)
        break
    var3 = i32_load(var1 + 100)
    if (1 if var0 == 0 else 0):
        if (1 if var3 == 0 else 0):
            break
        var3 = i32_load(var1 + 96)
        var0 = 0
        break
    if var3:
        var3 = i32_load(var1 + 96)
        var0 = 0
        break
    var0 = i32_load(var1 + 108)
    i32_store(var1 + 100, i32_load(var1 + 108))
    var2 = i32_load(var1 + 96)
    var3 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var2:
    else:
    var0 = 0
    i32_store(var1 + 96, var3)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var3 + (var0 << 2)), 2147483647)
    var0 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var2 = var3
        break
    var2 = (i32_load(var1 + 108) + var0)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var0))
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var2)
    var0 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var2 + (var0 << 2)), 2147483647)
    var0 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var3 = var2
        break
    var3 = (i32_load(var1 + 108) + var0)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var0))
    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var3)
    var0 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var3 + (var0 << 2)), 2147483647)
    var0 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var2 = var3
        break
    var2 = (i32_load(var1 + 108) + var0)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var0))
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var2)
    var0 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var2 + (var0 << 2)), 2147483647)
    var0 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var3 = var2
        break
    var3 = (i32_load(var1 + 108) + var0)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var0))
    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var3)
    var0 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var3 + (var0 << 2)), 2147483647)
    var0 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var2 = var3
        break
    var2 = (i32_load(var1 + 108) + var0)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var0))
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var2)
    var0 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var2 + (var0 << 2)), 2147483647)
    var0 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var3 = var2
        break
    var3 = (i32_load(var1 + 108) + var0)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var0))
    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var3)
    var0 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var3 + (var0 << 2)), 2147483647)
    var2 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var0 = var3
        break
    var0 = (i32_load(var1 + 108) + var2)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var2))
    var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var2:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var0)
    var2 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var2 + 1))
    i32_store((var0 + (var2 << 2)), 2147483647)
    i32_store(var0 + 20, 0)
    i32_store(var0 + 12, 50)
    break
    var0 = i32_load(var1 + 108)
    i32_store(var1 + 100, i32_load(var1 + 108))
    var2 = i32_load(var1 + 96)
    var3 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var2:
    else:
    var0 = 0
    i32_store(var1 + 96, var3)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var3 + (var0 << 2)), 0)
    var0 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var2 = var3
        break
    var2 = (i32_load(var1 + 108) + var0)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var0))
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var2)
    var0 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var2 + (var0 << 2)), 0)
    var0 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var3 = var2
        break
    var3 = (i32_load(var1 + 108) + var0)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var0))
    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var3)
    var0 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var3 + (var0 << 2)), 0)
    var0 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var2 = var3
        break
    var2 = (i32_load(var1 + 108) + var0)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var0))
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var2)
    var0 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var2 + (var0 << 2)), 0)
    var0 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var3 = var2
        break
    var3 = (i32_load(var1 + 108) + var0)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var0))
    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var3)
    var0 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var3 + (var0 << 2)), 0)
    var0 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var2 = var3
        break
    var2 = (i32_load(var1 + 108) + var0)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var0))
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var2)
    var0 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var2 + (var0 << 2)), 0)
    var0 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var3 = var2
        break
    var3 = (i32_load(var1 + 108) + var0)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var0))
    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var0:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var3)
    var0 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var0 + 1))
    i32_store((var3 + (var0 << 2)), 0)
    var2 = i32_load(var1 + 104)
    if (1 if i32_load(var1 + 104) != i32_load(var1 + 100) else 0):
        var0 = var3
        break
    var0 = (i32_load(var1 + 108) + var2)
    i32_store(var1 + 100, (i32_load(var1 + 108) + var2))
    var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var2:
        # Unknown: memory.copy []
    i32_store(var1 + 96, var0)
    var2 = i32_load(var1 + 104)
    i32_store(var1 + 104, (var2 + 1))
    i32_store((var0 + (var2 << 2)), 0)
    i64_store(var0 + 8, 214748364850)
    i32_store(var0, 5)
    var3 = 50
    var2 = i32_load(var0 + 8)
    var5 = i64_load(var0)
    var6 = i64_load(var0 + 16)
    var7 = i64_load(var0 + 24)
    i32_store(var4 + 32, 0)
    i64_store(var4 + 24, var7)
    i64_store(var4 + 16, var6)
    i32_store(var4 + 12, var3)
    i64_store(var4, var5)
    i32_store(var4 + 8, var2)
    global global0
    global0 = (var4 + 48)
    return var4


# ==========================================================
# $Ad
# Export: Ad
# ==========================================================
def Ad(var0):
    """Export: Ad"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var1 = i32_load(9568088)
    if (i32_load(i32_load(9568088) + 88) if var0 else 1):
        return i32_load(var1 + 80)
    while True:  # loop $label1
        var3 = i32_load(var1 + 88)
        if (1 if i32_load(var1 + 88) != i32_load(var1 + 84) else 0):
            var2 = i32_load(var1 + 80)
            break
        var2 = (i32_load(var1 + 92) + var3)
        i32_store(var1 + 84, (i32_load(var1 + 92) + var3))
        var4 = i32_load(var1 + 80)
        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        if var3:
            # Unknown: memory.copy []
        if var4:
            var3 = i32_load(var1 + 88)
        i32_store(var1 + 80, var2)
        i32_store(var1 + 88, (var3 + 1))
        i32_store((var2 + (var3 << 2)), 0)
        var5 = (var5 + 1)
        if (1 if (var5 + 1) != var0 else 0):
            continue
        break  # end loop
    return var2

