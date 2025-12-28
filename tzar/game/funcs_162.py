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
# $func364
# ==========================================================
def func364(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var5 = i32_load(var0)
    var3 = ((i32_load(var0) * 404) + 9568096)
    var6 = (1 if (1 if i32_load(((i32_load(var0) * 404) + 9568096) + 368) != 55 else 0) else var2)
    if (1 if (1 if (1 if i32_load(((i32_load(var0) * 404) + 9568096) + 368) != 55 else 0) else var2) == 0 else 0):
        break
    var7 = (var3 + 68)
    var2 = 0
    while True:  # loop $label2
        var0 = (i32_load(9671128) + (i32_load((var1 + (var2 << 2))) * 132))
        var4 = (i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (i32_load((var1 + (var2 << 2))) * 132)) + 110) * 286704))
        var8 = ((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (i32_load((var1 + (var2 << 2))) * 132)) + 110) * 286704)) + (var5 << 2))
        if i32_load((((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (i32_load((var1 + (var2 << 2))) * 132)) + 110) * 286704)) + (var5 << 2)) + 281808)):
            break
        if i32_load8_u(var0 + 125):
            break
        if func66(var4, var7, 1, 1):
            break
        if (1 if i32_load(var3 + 368) != 55 else 0):
            i32_store((var8 + 282828), 1)
        i32_store8(var0 + 125, 5)
        func63(0  # stack underflow, var0, 5, var5, ((((i32_load(var3 + 116) * i32_load(i32_load(9142424) + 132)) * 1000) & 0xFFFFFFFF) // 100))
        if (1 if i32_load(var0 + 92) == 0 else 0):
            break
        var4 = i32_load8_u(9147141)
        if i32_load(9140316):
            if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
                break
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var6 else 0):
            continue
        break  # end loop


# ==========================================================
# $func366
# ==========================================================
def func366():
    var0 = 0
    var1 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if i32_load(9690440) == 0 else 0):
        i32_store(9690460, 2)
        i64_store(9690452, -1)
        i64_store(9690444, 17592186048512)
        i32_store(9690908, 2)
        i32_store(var1 + 12, 0)
        var0 = (global0 - 32)
        i64_store((global0 - 32) + 24, 0)
        i64_store(var0 + 16, 0)
        i64_store(var0 + 8, 0)
        i64_store(9690912, i64_load(var0 + 8))
        i64_store(9690928, i64_load(var0 + 24))
        i64_store(9690920, i64_load(var0 + 16))
        var0 = (var1 + 12)
        if (var1 + 12):
            i32_store(9690912, i32_load(var0))
        i32_store(9690440, (((var1 + 8) & -16) ^ 1431655768))
    func54(9690960)
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $rc
# Export: rc
# ==========================================================
def rc(var0, var1, var2, var3, param4, param5):
    """Export: rc"""
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
    var8 = (global0 - 40000)
    global global0
    global0 = (global0 - 40000)
    if (1 if i32_load(51776) == 0 else 0):
        i32_store8(9215872, 1)
        func216(9216024, var0, var1, var2, var3)
        break
    var1 = (1 if var1 == 2147483647 else 0)
    i32_store(9213812, (0 if (1 if var1 == 2147483647 else 0) else var1))
    if var2:
        var11 = ((var2 * 132) + 9216080)
        if (1 if i32_load8_u(((var2 * 132) + 9216080) + 23) == 0 else 0):
            break
        var4 = i32_load(9142872)
        var6 = i32_load(9561692)
        var5 = i32_load(9213808)
        if i32_load(9213808):
            # Unknown: memory.copy []
        i32_store(9213808, 0)
        var7 = i32_load((((var6 + (var4 * 286704)) + (var3 << 2)) + 284636))
        if (1 if i32_load((((var6 + (var4 * 286704)) + (var3 << 2)) + 284636)) == 0 else 0):
            break
        var0 = i32_load(var7 + 8)
        if (1 if i32_load(var7 + 8) == 0 else 0):
            break
        var1 = 0
        var9 = i32_load(9671128)
        var10 = i32_load(var7)
        if (1 if i32_load8_u(9147152) == 0 else 0):
            var6 = ((var6 + (var4 * 286704)) + 283908)
            var12 = i32_load(9215884)
            var13 = i32_load(9142892)
            var14 = i32_load(9143008)
            var3 = 0
            while True:  # loop $label3
                var4 = i32_load((var10 + (var1 << 2)))
                if (1 if i32_load((var10 + (var1 << 2))) == 0 else 0):
                    break
                var4 = (var9 + (var4 * 132))
                if (1 if i32_load8_u((var14 + (i32_load(var6) + (var13 * i32_load16_u((var9 + (var4 * 132)) + 110))))) == 0 else 0):
                    break
                if (1 if i32_load((var12 + (i32_load(var4 + 44) << 4)) + 4) == 20 else 0):
                    break
                if (1 if i32_load8_u(var4 + 127) == 6 else 0):
                    break
                i32_store(((var3 << 2) + 9173808), i32_load(var4 + 28))
                var3 = (var3 + 1)
                i32_store(9213808, (var3 + 1))
                var0 = i32_load(var7 + 8)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) < var0 else 0):
                    continue
                break  # end loop
            break
        var3 = 0
        while True:  # loop $label5
            var4 = i32_load((var10 + (var1 << 2)))
            if i32_load((var10 + (var1 << 2))):
                i32_store(((var3 << 2) + 9173808), i32_load((var9 + (var4 * 132)) + 28))
                var3 = (var3 + 1)
                i32_store(9213808, (var3 + 1))
                var0 = i32_load(var7 + 8)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < var0 else 0):
                continue
            break  # end loop
        if (1 if var3 == 0 else 0):
            break
        var0 = i32_load(var11)
        if (1 if i32_load(var11) == 12 else 0):
            i32_store(9213808, 0)
        # call_indirect via table[var0]
        if var5:
            # Unknown: memory.copy []
        i32_store(9213808, var5)
        break
    var2 = ((0 if var1 else (i32_load(9143000) * i32_load(9147120))) + var0)
    var3 = i32_load(9671120)
    if (1 if ((0 if var1 else (i32_load(9143000) * i32_load(9147120))) + var0) >= i32_load(9671120) else 0):
        var1 = i32_load(9681836)
        if (1 if (i32_load(9681836) | i32_load8_u(9147141)) == 0 else 0):
            break
        if (1 if var0 < var3 else 0):
            break
        break
    var1 = i32_load(9681836)
    i32_store(9213816, var0)
    if var1:
        var0 = (global0 - 16)
        global global0
        global0 = (global0 - 16)
        func45()
        var1 = i32_load(9143000)
        i32_store(9143000, 0)
        var2 = (i32_load(9213816) + (var1 * i32_load(9147120)))
        if (1 if (i32_load(9213816) + (var1 * i32_load(9147120))) <= i32_load(9681836) else 0):
            var1 = i32_load(9671128)
            var3 = i32_load((i32_load(9681828) + (var2 << 2)))
            var2 = (i32_load(9671128) + (i32_load((i32_load(9681828) + (var2 << 2))) * 132))
            if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load((i32_load(9681828) + (var2 << 2))) * 132)) + 122) * 404) + 9568096) + 264) != 2 else 0):
                break
            var5 = i32_load(var2 + 36)
            if (1 if i32_load(var2 + 36) == 0 else 0):
                break
            var1 = (var1 + (var5 * 132))
            func44((var1 + (var5 * 132)), 0)
            if i32_load8_u(9142917):
                break
            var2 = i32_load(var1 + 36)
            var1 = (i32_load(9671128) + ((i32_load(var1 + 36) if var2 else i32_load(var1 + 28)) * 132))
            var2 = i32_load8_u((i32_load(9671128) + ((i32_load(var1 + 36) if var2 else i32_load(var1 + 28)) * 132)) + 122)
            var3 = (((i32_load(((i32_load8_u((i32_load(9671128) + ((i32_load(var1 + 36) if var2 else i32_load(var1 + 28)) * 132)) + 122) * 404) + 9568096) + 220) << 4) & 2147483632) + (i32_load16_u(var1 + 114) << 5))
            break
            func44(var2, 0)
            if i32_load8_u(9142917):
                break
            var1 = (var1 + (var3 * 132))
            var2 = i32_load((var1 + (var3 * 132)) + 36)
            var1 = (i32_load(9671128) + ((i32_load((var1 + (var3 * 132)) + 36) if var2 else i32_load(var1 + 28)) * 132))
            var2 = i32_load8_u((i32_load(9671128) + ((i32_load((var1 + (var3 * 132)) + 36) if var2 else i32_load(var1 + 28)) * 132)) + 122)
            var3 = (((i32_load(((i32_load8_u((i32_load(9671128) + ((i32_load((var1 + (var3 * 132)) + 36) if var2 else i32_load(var1 + 28)) * 132)) + 122) * 404) + 9568096) + 220) << 4) & 2147483632) + (i32_load16_u(var1 + 114) << 5))
            var1 = (var1 + 112)
            var2 = i32_load(((var2 * 404) + 9568096) + 216)
            var1 = i32_load16_u(var1)
            i32_store(var0 + 4, var3)
            i32_store(var0, (((var2 << 4) & 2147483632) + (var1 << 5)))
        global global0
        global0 = (var0 + 16)
        break
    if i32_load8_u(9147141):
        func377(func28(0, 0), var1)
        break
    var0 = i32_load(((var2 << 2) + 9263072))
    if (1 if i32_load(((var2 << 2) + 9263072)) == 0 else 0):
        break
    var1 = i32_load(var0)
    if i32_load8_u(var0 + 20):
        # call_indirect via table[var1]
        break
    if (1 if var1 != 5 else 0):
        break
    if (1 if i32_load(9213812) != 2 else 0):
        break
    func242(i32_load(var0 + 4))
    global global0
    global0 = (var8 + 40000)
    return call_indirect(var1)


# ==========================================================
# $func394
# ==========================================================
def func394(var0, param1):
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var2 = (var0 + 4)
    if (1 if i32_load(var0 + 44) != i32_load(var0 + 48) else 0):
        while True:  # loop $label0
            func392((var1 + 4), var0)
            var3 = i32_load(var1 + 8)
            if i32_load(var1 + 8):
                # call_indirect via table[var3]
            if (1 if i32_load(var0 + 44) != i32_load(var0 + 48) else 0):
                continue
            break  # end loop
    func54(var2)
    i32_atomic_store(var0, 0)
    global global0
    global0 = (var1 + 16)

