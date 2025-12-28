"""
Auto-generated from WAT. Contains 16 functions.
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
# $func390
# ==========================================================
def func390(var0):
    var1 = 0
    if (1 if i32_load(var0 + 4) >= 129 else 0):
        var1 = i32_load(9689392)
        if i32_load(9689392):
            while True:  # loop $label0
                var1 = i32_load(9689392)
                if i32_load(9689392):
                    continue
                break  # end loop


# ==========================================================
# $func434
# ==========================================================
def func434(var0, var1, var2):
    var3 = 0
    var4 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = global3
    var4 = (var2 + 12)
    if (var2 + 12):
        i32_store(var4, i32_load8_u(var3 + 40))
    i32_store8(var3 + 40, 1)
    var0 = func265(var0, var1, var2)
    var1 = i32_load(var2 + 12)
    if (1 if i32_load(var2 + 12) <= 2 else 0):
        i32_store8(global3 + 40, var1)
    else:
    global global0
    global0 = (var2 + 16)
    return var0


# ==========================================================
# $func591
# ==========================================================
def func591(var0, var1):
    if var0:
        if (1 if i32_load8_u(9147152) == 0 else 0):
            func52((207 if i32_load8_u(9143020) else 0), 0)
            a_b()
        func326(var0)


# ==========================================================
# $func592
# ==========================================================
def func592(var0, var1):
    if var0:
        if (1 if i32_load8_u(9147152) == 0 else 0):
            func52((207 if i32_load8_u(9143020) else 0), 0)
            a_b()
        func332(-1)


# ==========================================================
# $func593
# ==========================================================
def func593(var0, var1):
    if var0:
        if (1 if i32_load8_u(9147152) == 0 else 0):
            func52((207 if i32_load8_u(9143020) else 0), 0)
            a_b()
        func327(var0)


# ==========================================================
# $func594
# ==========================================================
def func594(var0, var1):
    if var0:
        if (1 if i32_load8_u(9147152) == 0 else 0):
            func52((207 if i32_load8_u(9143020) else 0), 0)
            a_b()
        func328(var0)


# ==========================================================
# $func595
# ==========================================================
def func595(var0, var1):
    if var0:
        if (1 if i32_load8_u(9147152) == 0 else 0):
            func52((207 if i32_load8_u(9143020) else 0), 0)
            a_b()
        func329(var0)


# ==========================================================
# $func598
# ==========================================================
def func598(var0, var1):
    if var0:
        if (1 if i32_load8_u(9147152) == 0 else 0):
            func52((207 if i32_load8_u(9143020) else 0), 0)
            a_b()
        func325(var0)


# ==========================================================
# $func599
# ==========================================================
def func599(var0, var1):
    if var0:
        if (1 if i32_load8_u(9147152) == 0 else 0):
            func52((207 if i32_load8_u(9143020) else 0), 0)
            a_b()
        func333(-1)


# ==========================================================
# $func600
# ==========================================================
def func600(var0, var1):
    if var0:
        if (1 if i32_load8_u(9147152) == 0 else 0):
            func52((207 if i32_load8_u(9143020) else 0), 0)
            a_b()
        func334(var0)


# ==========================================================
# $func601
# ==========================================================
def func601(var0, var1):
    if var0:
        if (1 if i32_load8_u(9147152) == 0 else 0):
            func52((207 if i32_load8_u(9143020) else 0), 0)
            a_b()


# ==========================================================
# $func602
# ==========================================================
def func602(var0, var1):
    if var0:
        if (1 if i32_load8_u(9147152) == 0 else 0):
            func52((207 if i32_load8_u(9143020) else 0), 0)
            a_b()
        func331(var0)


# ==========================================================
# $func648
# ==========================================================
def func648(var0, var1, var2):
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var0 = (i32_load(9561692) + (i32_load(var0) * 286704))
    var2 = i32_load((i32_load(9561692) + (i32_load(var0) * 286704)) + 284616)
    if (1 if i32_load((i32_load(9561692) + (i32_load(var0) * 286704)) + 284616) == 0 else 0):
        La(i32_load(var0 + 283908), 1)
        break
    i32_store(var1, var2)
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $func794
# ==========================================================
def func794():
    var0 = 0
    var0 = global1
    if (1 if i32_load(global1) == 0 else 0):
        i32_store(var0, 1)
        var0 = func372(9688236, global3)
        func54(9688236)
        if (1 if var0 == 0 else 0):
            break
        if i32_load(var0 + 32):
            break
        func248(0  # stack underflow, var0)
        i32_store(global1, 0)


# ==========================================================
# $we
# Export: we
# ==========================================================
def we(var0, var1, var2):
    """Export: we"""
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var3 = (global0 - 240)
    global global0
    global0 = (global0 - 240)
    i32_store8(40588, var0)
    i32_store16(var3 + 52, i32_load16_u(3837))
    i32_store16(var3 + 60, i32_load16_u(2478))
    i32_store8(var3 + 43, 5)
    i32_store(var3 + 32, i32_load(3119))
    i32_store8(var3 + 36, i32_load8_u(3123))
    i32_store8(var3 + 37, 0)
    i64_store(var3 + 44, i64_load(3829))
    i32_store8(var3 + 67, 6)
    i32_store16(var3 + 54, 2560)
    i32_store(var3 + 56, i32_load(2474))
    i32_store8(var3 + 79, 4)
    i32_store8(var3 + 62, 0)
    i32_store8(var3 + 72, 0)
    i32_store8(var3 + 100, 0)
    i32_store16(var3 + 84, i32_load16_u(3518))
    i32_store16(var3 + 108, i32_load16_u(4775))
    i32_store8(var3 + 91, 6)
    i32_store(var3 + 68, 2003791475)
    i32_store8(var3 + 103, 8)
    i32_store8(var3 + 86, 0)
    i64_store(var3 + 92, 7236828769417322866)
    i32_store8(var3 + 115, 6)
    i32_store8(var3 + 127, 5)
    i32_store8(var3 + 110, 0)
    i32_store(var3 + 80, i32_load(3514))
    i32_store(var3 + 104, i32_load(4771))
    i32_store8(var3 + 136, 0)
    i32_store8(var3 + 120, i32_load8_u(7806))
    i32_store8(var3 + 139, 8)
    i32_store8(var3 + 121, 0)
    i64_store(var3 + 128, 8606218855064367719)
    i32_store(var3 + 116, i32_load(7802))
    i32_store(59156, var2)
    i32_store(9687252, 0)
    i32_store(9568092, var1)
    var0 = i32_load8_u(9147213)
    if (i32_load8_u(9147213) | i32_load8_u(9147212)):
    else:
        var0 = i32_load(9142440)
        i32_store(9147288, func26((i32_load(9142440) * var0)))
        func402(var0)
    if (i32_load8_u(9147213) & 255):
        break
    if (1 if var1 >= 2 else 0):
        var2 = i32_load8_u(59184)
        var0 = (22 if i32_load8_u(59184) else 6)
        var4 = (2117 if var2 else 2133)
        if var2:
            var5 = (var0 | 15)
            var2 = func26(((var0 | 15) + 1))
            i32_store(var3 + 28, (var5 - 2147483647))
            i32_store(var3 + 20, var2)
            i32_store(var3 + 24, var0)
            break
        i32_store8(var3 + 31, var0)
        var2 = (var3 + 20)
        # Unknown: memory.copy []
        i32_store8((var0 + var2), 0)
        var0 = (var3 + 8)
        var0 = func211(var0, 8178)
        i32_store(var3 + 152, i32_load(func211(var0, 8178) + 8))
        i64_store(var3 + 144, i64_load(var0))
        i64_store(var0, 0)
        i32_store(var0 + 8, 0)
        var0 = i32_load8_u(var3 + 155)
        # Unknown: i32.extend8_s []
        var1 = (1 if i32_load8_u(var3 + 155) < 0 else 0)
        if (1 if i32_load8_s(var3 + 155) < 0 else 0):
        if (1 if i32_load8_s(var3 + 19) < 0 else 0):
        var0 = i32_load8_s(var3 + 31)
        if (1 if i32_load8_s(9681935) >= 0 else 0):
            if (1 if var0 >= 0 else 0):
                i64_store(9681924, i64_load(var3 + 20))
                i32_store(9681932, i32_load(var3 + 28))
                break
            var2 = i32_load(var3 + 20)
            var0 = i32_load(var3 + 24)
            var1 = (global0 - 16)
            global global0
            global0 = (global0 - 16)
            if (1 if var0 <= 10 else 0):
                i32_store8(9681935, ((i32_load8_u(9681935) & 128) | var0))
                i32_store8(9681935, (i32_load8_u(9681935) & 127))
                func122(9681924, var2, var0)
                i32_store8(var1 + 15, 0)
                i32_store8((var0 + 9681924), i32_load8_u(var1 + 15))
                break
            var4 = (i32_load8_u(9681935) & 127)
            global global0
            global0 = (var1 + 16)
            break
        var1 = (1 if var0 < 0 else 0)
        var2 = (i32_load(var3 + 20) if (1 if var0 < 0 else 0) else (var3 + 20))
        var0 = (i32_load(var3 + 24) if var1 else (var0 & 255))
        var1 = (global0 - 16)
        global global0
        global0 = (global0 - 16)
        var4 = (i32_load(9681932) & 2147483647)
        if (1 if var0 < (i32_load(9681932) & 2147483647) else 0):
            var4 = i32_load(9681924)
            i32_store(9681928, var0)
            func122(var4, var2, var0)
            i32_store8(var1 + 15, 0)
            i32_store8((var0 + var4), i32_load8_u(var1 + 15))
            break
        var4 = i32_load(9681928)
        global global0
        global0 = (var1 + 16)
        var0 = (var3 + 20)
        var1 = i32_load(var3 + 20)
        var2 = i32_load8_s(var3 + 31)
        var4 = (var3 + 144)
        # Unknown: memory.fill []
        i32_store(var3 + 144, 5522759)
        i32_store(var3 + 188, 102)
        i32_store(var3 + 180, 103)
        i32_store(var3 + 184, 56)
        i32_store(var3 + 196, (1 if i32_load8_u(59184) else (5 if i32_load8_u(59185) else 1)))
        func179(var4, (var1 if (1 if var2 < 0 else 0) else var0))
        if (1 if i32_load8_s(var3 + 31) >= 0 else 0):
            break
        break
    var0 = (var3 + 144)
    # Unknown: memory.fill []
    i32_store(var3 + 144, 5522759)
    i32_store(var3 + 188, 102)
    i32_store(var3 + 180, 103)
    i32_store(var3 + 184, 56)
    i32_store(var3 + 196, (1 if i32_load8_u(59184) else (5 if i32_load8_u(59185) else 1)))
    func179(var0, 7765)
    i32_store(var3 + 28, 0)
    i32_store8(var3 + 27, 0)
    i32_store8(var3 + 31, 7)
    i32_store(var3 + 20, i32_load(8172))
    i32_store(var3 + 23, i32_load(8175))
    var2 = ((var3 + 32) + (i32_load(i32_load(9142424) + 24) * 12))
    var0 = i32_load8_u(var2 + 11)
    # Unknown: i32.extend8_s []
    var5 = var0
    var4 = (i32_load(((var3 + 32) + (i32_load(i32_load(9142424) + 24) * 12)) + 4) if (1 if var0 < 0 else 0) else i32_load8_u(var2 + 11))
    var0 = ((i32_load(((var3 + 32) + (i32_load(i32_load(9142424) + 24) * 12)) + 4) if (1 if var0 < 0 else 0) else i32_load8_u(var2 + 11)) + 5)
    if (1 if ((i32_load(((var3 + 32) + (i32_load(i32_load(9142424) + 24) * 12)) + 4) if (1 if var0 < 0 else 0) else i32_load8_u(var2 + 11)) + 5) < 2147483632 else 0):
        if (1 if var0 <= 10 else 0):
            i32_store(var3 + 152, 0)
            i64_store(var3 + 144, 0)
            i32_store8(var3 + 155, var0)
            var1 = (var3 + 144)
            break
        var6 = ((var0 | 15) + 1)
        var1 = func26(((var0 | 15) + 1))
        i32_store(var3 + 148, var0)
        i32_store(var3 + 144, var1)
        i32_store(var3 + 152, (var6 | -2147483648))
        if var4:
            # Unknown: memory.copy []
        var0 = (var1 + var4)
        i32_store8((var1 + var4) + 5, 0)
        i32_store8(var0 + 4, i32_load8_u(7782))
        i32_store(var0, i32_load(7778))
        var0 = i32_load8_s(var3 + 155)
        var1 = (1 if i32_load8_s(var3 + 155) < 0 else 0)
        if (1 if i32_load8_s(var3 + 155) < 0 else 0):
        var0 = i32_load(var3 + 20)
        var1 = i32_load8_s(var3 + 31)
        var2 = (var3 + 144)
        # Unknown: memory.fill []
        i32_store(var3 + 144, 5522759)
        i32_store(var3 + 188, 104)
        i32_store(var3 + 180, 103)
        i32_store(var3 + 184, 56)
        i32_store(var3 + 196, (1 if i32_load8_u(59184) else (5 if i32_load8_u(59185) else 1)))
        func179(var2, (var0 if (1 if var1 < 0 else 0) else (var3 + 20)))
        if (1 if i32_load8_s(var3 + 31) < 0 else 0):
        if (1 if i32_load8_s(var3 + 139) < 0 else 0):
        if (1 if i32_load8_s(var3 + 127) < 0 else 0):
        if (1 if i32_load8_s(var3 + 115) < 0 else 0):
        if (1 if i32_load8_s(var3 + 103) < 0 else 0):
        if (1 if i32_load8_s(var3 + 91) < 0 else 0):
        if (1 if i32_load8_s(var3 + 79) < 0 else 0):
        if (1 if i32_load8_s(var3 + 67) < 0 else 0):
        if (1 if i32_load8_s(var3 + 55) < 0 else 0):
        if (1 if i32_load8_s(var3 + 43) < 0 else 0):
        global global0
        global0 = (var3 + 240)
        return af(i32_load(var3 + 32))
    func212()
    raise RuntimeError('unreachable')
    return af(i32_load(var3 + 44))


# ==========================================================
# $Ma
# Export: Ma
# ==========================================================
def Ma():
    """Export: Ma"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var1 = i32_load(9142892)
    if (1 if i32_load(9142892) >= 2 else 0):
        var2 = i32_load(9561692)
        var0 = 1
        while True:  # loop $label1
            var3 = (var2 + (var0 * 286704))
            var4 = i32_load((var2 + (var0 * 286704)) + 284616)
            if (1 if i32_load((var2 + (var0 * 286704)) + 284616) == 0 else 0):
                break
            if i32_load(var3 + 284632):
                break
            if (1 if i32_load(var3 + 283908) == i32_load(9142872) else 0):
                break
            La(var4, 0)
            var1 = i32_load(9142892)
            var2 = i32_load(9561692)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < var1 else 0):
                continue
            break  # end loop

