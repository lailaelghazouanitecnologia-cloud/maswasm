"""
Auto-generated from WAT. Contains 7 functions.
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
# $func186
# ==========================================================
def func186(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var5 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if (1 if var0 == 0 else 0):
        break
    if (1 if i32_load(9688320) == 0 else 0):
        i32_store(9688320, 43)
    if (1 if i32_load8_u(9688037) == 0 else 0):
        var7 = i32_load8_s(9688039)
        if (1 if i32_load8_s(9688039) == 0 else 0):
            break
        var4 = -2147483647
        if (1 if var7 < 0 else 0):
            i32_store8(9688039, 0)
        if (1 if var4 == 0 else 0):
            break
        while True:  # loop $label2
            var7 = ((var4 + 2147483647) if (1 if var4 < 0 else 0) else var4)
            var4 = (var7 - 2147483647)
            if (1 if (var7 - 2147483647) == var7 else 0):
                break
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != 10 else 0):
                continue
            break  # end loop
        var4 = (1 + 1)
        while True:  # loop $label3
            if (1 if var4 < 0 else 0):
                func439(9688228, var4)
                var4 = (var4 + 2147483647)
            var4 = (var4 | -2147483648)
            if (1 if var4 != (var4 | -2147483648) else 0):
                continue
            break  # end loop
        var4 = i32_load(9688232)
        if i32_load(9688232):
            while True:  # loop $label5
                if (1 if var4 == 0 else 0):
                    break
                if (1 if i32_load(var4 + 76) >= 0 else 0):
                    break
                i32_store(var4 + 76, 0)
                var4 = i32_load(var4 + 56)
                if i32_load(var4 + 56):
                    continue
                break  # end loop
        if (1 if i32_load(9688228) >= 0 else 0):
            break
        if (1 if 2147483647 == -2147483647 else 0):
            break
        func97(9688228)
        var4 = i32_load(9688032)
        if (1 if i32_load(9688032) == 0 else 0):
            break
        if (1 if i32_load(var4 + 76) >= 0 else 0):
            break
        i32_store(var4 + 76, 0)
        var4 = i32_load(52736)
        if (1 if i32_load(52736) == 0 else 0):
            break
        if (1 if i32_load(var4 + 76) >= 0 else 0):
            break
        i32_store(var4 + 76, 0)
        var4 = i32_load(52584)
        if (1 if i32_load(52584) == 0 else 0):
            break
        if (1 if i32_load(var4 + 76) >= 0 else 0):
            break
        i32_store(var4 + 76, 0)
        i32_store8(9688037, 1)
    # Unknown: memory.fill []
    if (1 if (var1 + 1) >= 2 else 0):
        # Unknown: memory.copy []
        var4 = i32_load(var5 + 4)
        if i32_load(var5 + 4):
            break
    var4 = a_w()
    i32_store(var5 + 4, a_w())
    var1 = (i32_load(52436) + 148)
    var6 = ((i32_load(52436) + 148) + (0 if i32_load(var5 + 12) else (var4 + 15)))
    var4 = e()
    func98(e(), 0, var1)
    i32_store(var4 + 48, var6)
    i32_store(var4 + 44, var4)
    i32_store(var4, var4)
    var1 = i32_load(9688320)
    i32_store(9688320, (i32_load(9688320) + 1))
    i32_store(var4 + 76, (var4 + 76))
    i32_store(var4 + 24, var1)
    i32_store(var4 + 96, 9688068)
    i32_store(var4 + 32, (3 if i32_load(var5 + 16) else 2))
    var6 = i32_load(var5 + 4)
    i32_store(var4 + 56, i32_load(var5 + 4))
    var1 = ((var4 + 139) & -4)
    i32_store(var4 + 116, ((var4 + 139) & -4))
    var1 = (var1 + 6)
    if i32_load(52436):
        var1 = ((var1 + 3) & -4)
        i32_store(var4 + 72, ((var1 + 3) & -4))
        var1 = (i32_load(52436) + var1)
    var7 = i32_load(var5 + 12)
    i32_store(var4 + 52, (i32_load(var5 + 12) if var7 else (((var1 + var6) + 15) & -16)))
    func430(var4)
    var1 = global3
    func264()
    var6 = i32_load(var1 + 12)
    i32_store(var4 + 8, var1)
    i32_store(var4 + 12, var6)
    i32_store(var6 + 8, var4)
    i32_store(i32_load(var4 + 8) + 12, var4)
    func263()
    var1 = i32_load(9688040)
    i32_store(9688040, (i32_load(9688040) + 1))
    if (1 if var1 == 0 else 0):
        i32_store8(9688039, 1)
    if a_y():
        var0 = (i32_load(9688040) - 1)
        i32_store(9688040, (i32_load(9688040) - 1))
        if (1 if var0 == 0 else 0):
            i32_store8(9688039, 0)
        func264()
        var0 = i32_load(var4 + 12)
        i32_store(i32_load(var4 + 12) + 8, i32_load(var4 + 8))
        i32_store(i32_load(var4 + 8) + 12, var0)
        i32_store(var4 + 12, var4)
        i32_store(var4 + 8, var4)
        func263()
        break
    i32_store(var0, var4)
    global global0
    global0 = (var5 + 48)


# ==========================================================
# $func227
# ==========================================================
def func227():
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if i32_load8_u(9142411):
        break
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    var5 = i32_load(9142440)
    if (1 if i32_load(9142440) <= 0 else 0):
        var1 = var5
        break
    var2 = i32_load(9142840)
    var1 = var5
    while True:  # loop $label6
        var6 = (var7 + 1)
        var3 = 0
        while True:  # loop $label5
            var0 = (i32_load(9147376) + (((var1 * var3) + var7) << 1))
            i32_store16((i32_load(9147376) + (((var1 * var3) + var7) << 1)), (i32_load16_u(var0) + 2))
            var4 = (var1 + 2)
            var3 = (var3 + 1)
            var0 = i32_load((var2 + ((((var1 + 2) * (var3 + 1)) + var6) << 2)))
            if (1 if i32_load((var2 + ((((var1 + 2) * (var3 + 1)) + var6) << 2))) < 3 else 0):
                break
            var0 = (i32_load(9671128) + (var0 * 132))
            if i32_load((i32_load(9671128) + (var0 * 132)) + 40):
                break
            var1 = i32_load(9142440)
            var4 = (i32_load(9142440) + 2)
            var2 = i32_load(9142840)
            var0 = i32_load((var2 + ((((var3 + var4) * var4) + var6) << 2)))
            if (1 if i32_load((var2 + ((((var3 + var4) * var4) + var6) << 2))) < 3 else 0):
                break
            var0 = (i32_load(9671128) + (var0 * 132))
            if i32_load((i32_load(9671128) + (var0 * 132)) + 40):
                break
            var1 = i32_load(9142440)
            var4 = (i32_load(9142440) + 2)
            var2 = i32_load(9142840)
            var0 = i32_load((var2 + (((((var4 << 1) + var3) * var4) + var6) << 2)))
            if (1 if i32_load((var2 + (((((var4 << 1) + var3) * var4) + var6) << 2))) < 3 else 0):
                break
            var0 = (i32_load(9671128) + (var0 * 132))
            if i32_load((i32_load(9671128) + (var0 * 132)) + 40):
                break
            var2 = i32_load(9142840)
            var1 = i32_load(9142440)
            if (1 if var3 != var5 else 0):
                continue
            break  # end loop
        var7 = var6
        if (1 if var6 != var5 else 0):
            continue
        break  # end loop
    i32_store8(9142904, 1)
    i32_store8(9142411, 1)
    i32_store(40612, (var1 - 1))
    i32_store(40608, 0)
    a_b()


# ==========================================================
# $func240
# ==========================================================
def func240(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var3 = i32_load8_u(var0 + 122)
    var4 = i32_load(9561692)
    var5 = i32_load16_u(var0 + 110)
    func156(0  # stack underflow, var0, var1)
    var1 = ((var3 * 404) + 9568096)
    if (1 if i32_load(((var3 * 404) + 9568096) + 264) == 4 else 0):
        i32_store8(9671157, 1)
    if (1 if i32_load(var1 + 208) == 2 else 0):
        i32_store8(9671158, 1)
    func144(((var5 * 286704) + var4), i32_load(var0 + 28), var2)
    if (1 if i32_load(var0 + 76) == 0 else 0):
        break
    if (1 if i32_load(38528) == i32_load8_u(var0 + 122) else 0):
        break
    if (1 if i32_load8_u(var0 + 126) != 2 else 0):
        break
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) == 2 else 0):
        break
    var1 = i32_load8_u(var0 + 122)
    if (1 if i32_load8_u(var0 + 122) == i32_load(38996) else 0):
        var1 = i32_load8_u(var0 + 122)
    if (1 if i32_load(38540) == var1 else 0):
        break
    if (1 if i32_load(38812) == var1 else 0):
        break
    if (1 if i32_load(38888) != var1 else 0):
        break
    # br_table ['$label3', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label3', '$label4']
    _br_idx = (i32_load8_u(var0 + 125) - 4)
    break  # br_table


# ==========================================================
# $func249
# ==========================================================
def func249(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var1 = (global0 - 144)
    global global0
    global0 = (global0 - 144)
    # Unknown: memory.fill []
    i32_store(var1 + 52, 5522759)
    i32_store(var1 + 92, 56)
    i32_store(var1 + 88, 57)
    i32_store(var1 + 104, (1 if i32_load8_u(59184) else (5 if i32_load8_u(59185) else 1)))
    var2 = (var1 + 12)
    var0 = i32_load8_u(9681935)
    # Unknown: i32.extend8_s []
    var3 = (1 if i32_load8_u(9681935) < 0 else 0)
    var5 = (i32_load(9681924) if (1 if i32_load8_u(9681935) < 0 else 0) else 9681924)
    var0 = (i32_load(9681928) if var3 else var0)
    var6 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if ((i32_load8_u(var2 + 11) & 0xFFFFFFFF) >> 7):
        break
    var3 = (i32_load8_u(var2 + 11) & 127)
    if (1 if (i32_load8_u(var2 + 11) & 127) >= 0 else 0):
        if ((i32_load8_u(var2 + 11) & 0xFFFFFFFF) >> 7):
        else:
        var4 = 10
        if (1 if ((i32_load(var2 + 8) & 2147483647) - 1) <= (10 - var3) else 0):
            if (1 if var0 == 0 else 0):
                break
            if ((i32_load8_u(var2 + 11) & 0xFFFFFFFF) >> 7):
                break
            var4 = var2
            if var3:
                # Unknown: memory.copy []
            else:
            # Unknown: memory.copy []
            var0 = (var0 + var3)
            func312(var2, (var0 + var3))
            i32_store8(var6 + 15, 0)
            i32_store8((var0 + var4), i32_load8_u(var6 + 15))
            break
        global global0
        global0 = (var6 + 16)
        break
    a_g()
    raise RuntimeError('unreachable')
    var0 = var2
    i32_store(func163(var2, var4, ((var0 + var3) - var4), var3, 0, 0, var0, var5) + 32, i32_load(var2 + 8))
    i64_store(var1 + 24, i64_load(var0))
    i64_store(var0, 0)
    i32_store(var0 + 8, 0)
    var0 = func211((var1 + 24), 7778)
    i32_store(var1 + 48, i32_load(func211((var1 + 24), 7778) + 8))
    i64_store(var1 + 40, i64_load(var0))
    i64_store(var0, 0)
    i32_store(var0 + 8, 0)
    if (1 if i32_load8_s(var1 + 35) < 0 else 0):
    if (1 if i32_load8_s(var1 + 23) < 0 else 0):
    var0 = (i32_load(var1 + 40) if (1 if i32_load8_s(var1 + 51) < 0 else 0) else (var1 + 40))
    i32_store(var1, (i32_load(var1 + 40) if (1 if i32_load8_s(var1 + 51) < 0 else 0) else (var1 + 40)))
    func179((var1 + 52), var0)
    if (1 if i32_load8_s(var1 + 51) < 0 else 0):
    global global0
    global0 = (var1 + 144)
    return af(i32_load(var1 + 40))


# ==========================================================
# $func257
# ==========================================================
def func257(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var3 = i32_load(9142840)
    var0 = (var0 + 1)
    var4 = (var1 + 1)
    var1 = (i32_load(9142440) + 2)
    var2 = i32_load((i32_load(9142840) + (((var0 + 1) + ((var1 + 1) * (i32_load(9142440) + 2))) << 2)))
    if (1 if i32_load((i32_load(9142840) + (((var0 + 1) + ((var1 + 1) * (i32_load(9142440) + 2))) << 2))) < 3 else 0):
        break
    var2 = (i32_load(9671128) + (var2 * 132))
    if i32_load((i32_load(9671128) + (var2 * 132)) + 40):
        break
    var1 = (i32_load(9142440) + 2)
    var3 = i32_load(9142840)
    var2 = i32_load((var3 + ((var0 + ((var1 + var4) * var1)) << 2)))
    if (1 if i32_load((var3 + ((var0 + ((var1 + var4) * var1)) << 2))) < 3 else 0):
        break
    var2 = (i32_load(9671128) + (var2 * 132))
    if i32_load((i32_load(9671128) + (var2 * 132)) + 40):
        break
    var1 = (i32_load(9142440) + 2)
    var3 = i32_load(9142840)
    var0 = i32_load((var3 + ((var0 + ((var4 + (var1 << 1)) * var1)) << 2)))
    if (1 if i32_load((var3 + ((var0 + ((var4 + (var1 << 1)) * var1)) << 2))) < 3 else 0):
        break
    var0 = (i32_load(9671128) + (var0 * 132))
    if i32_load((i32_load(9671128) + (var0 * 132)) + 40):
        break


# ==========================================================
# $func258
# ==========================================================
def func258(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var3 = i32_load(9142840)
    var0 = (var0 + 1)
    var4 = (var1 + 1)
    var1 = (i32_load(9142440) + 2)
    var2 = i32_load((i32_load(9142840) + (((var0 + 1) + ((var1 + 1) * (i32_load(9142440) + 2))) << 2)))
    if (1 if i32_load((i32_load(9142840) + (((var0 + 1) + ((var1 + 1) * (i32_load(9142440) + 2))) << 2))) < 3 else 0):
        break
    var2 = (i32_load(9671128) + (var2 * 132))
    if i32_load((i32_load(9671128) + (var2 * 132)) + 40):
        break
    if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 264) == 0 else 0):
        break
    var1 = (i32_load(9142440) + 2)
    var3 = i32_load(9142840)
    var2 = i32_load((var3 + ((var0 + ((var1 + var4) * var1)) << 2)))
    if (1 if i32_load((var3 + ((var0 + ((var1 + var4) * var1)) << 2))) < 3 else 0):
        break
    var2 = (i32_load(9671128) + (var2 * 132))
    if i32_load((i32_load(9671128) + (var2 * 132)) + 40):
        break
    if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 264) == 0 else 0):
        break
    var1 = (i32_load(9142440) + 2)
    var3 = i32_load(9142840)
    var0 = i32_load((var3 + ((var0 + ((var4 + (var1 << 1)) * var1)) << 2)))
    if (1 if i32_load((var3 + ((var0 + ((var4 + (var1 << 1)) * var1)) << 2))) < 3 else 0):
        break
    var0 = (i32_load(9671128) + (var0 * 132))
    if i32_load((i32_load(9671128) + (var0 * 132)) + 40):
        break
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) == 0 else 0):
        break


# ==========================================================
# $func264
# ==========================================================
def func264():
    var0 = 0
    var1 = 0
    var0 = i32_load(global3 + 24)
    if (1 if i32_load(global3 + 24) != i32_load(9688308) else 0):
        var1 = var0
        if var0:
            while True:  # loop $label0
                var1 = var0
                if var0:
                    continue
                break  # end loop
        return
    i32_store(9688312, (i32_load(9688312) + 1))

