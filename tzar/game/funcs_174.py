"""
Auto-generated from WAT. Contains 6 functions.
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
# $hf
# Export: hf
# ==========================================================
def hf(var0, param1, param2):
    """Export: hf"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var1 = global3
    i32_store8(global3 + 40, 1)
    i32_store(var1 + 64, var0)
    i32_store8(var1 + 41, 0)
    var0 = (1 - 1)
    if (1 - 1):
        var2 = (var1 + 124)
        while True:  # loop $label0
            var0 = i32_atomic_load(var2)
            if i32_atomic_load(var2):
                continue
            break  # end loop
    func394(var1, i32_load(var1 + 120))
    var0 = i32_load(var1 + 120)
    if (1 if i32_atomic_load(i32_load(var1 + 120)) == 0 else 0):
        func390(var0)
        break
    i32_store(var0 + 56, 52368)
    i32_store(var0 + 52, i32_load(52420))
    i32_store(52420, var0)
    i32_store(i32_load(var0 + 52) + 56, var0)
    func54(52372)
    var2 = global3
    while True:  # loop $label2
        var0 = i32_load(var2 + 68)
        if i32_load(var2 + 68):
            var3 = i32_load(var0 + 4)
            var4 = i32_load(var0)
            i32_store(var2 + 68, i32_load(var0 + 8))
            # call_indirect via table[var4]
            continue
        break  # end loop
    var2 = 0
    var0 = global3
    if (1 if (i32_load8_u(global3 + 42) & 1) == 0 else 0):
        break
    while True:  # loop $label6
        func437(9688848)
        i32_store8(var0 + 42, (i32_load8_u(var0 + 42) & 254))
        var3 = 0
        while True:  # loop $label5
            var5 = (var3 << 2)
            var4 = i32_load(((var3 << 2) + 9688880))
            var6 = (i32_load(var0 + 72) + var5)
            var5 = i32_load((i32_load(var0 + 72) + var5))
            i32_store(var6, 0)
            if (1 if var5 == 0 else 0):
                break
            if (1 if var4 == 0 else 0):
                break
            if (1 if var4 == 425 else 0):
                break
            func266(9688848)
            # call_indirect via table[var4]
            func437(9688848)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != 128 else 0):
                continue
            break  # end loop
        func266(9688848)
        if (1 if (i32_load8_u(var0 + 42) & 1) == 0 else 0):
            break
        var3 = (1 if var2 < 3 else 0)
        var2 = (var2 + 1)
        if var3:
            continue
        break  # end loop
    var0 = (i32_load(9688040) - 1)
    i32_store(9688040, (i32_load(9688040) - 1))
    if (1 if var0 == 0 else 0):
        i32_store8(9688039, 0)
    func264()
    var0 = i32_load(var1 + 12)
    i32_store(i32_load(var1 + 12) + 8, i32_load(var1 + 8))
    i32_store(i32_load(var1 + 8) + 12, var0)
    i32_store(var1 + 8, var1)
    i32_store(var1 + 12, var1)
    func263()
    if (1 if global5 == 0 else 0):
        global global3
        global3 = 0
        global global4
        global4 = 0
        global global5
        global5 = 0
        global global6
        global6 = 1
        var0 = (var1 + 32)
        if (1 if 1 == 3 else 0):
            a_z(var1)
            return
        i32_atomic_store(var0, 0)
        func97(var0)
        return
    a_k(0)
    raise RuntimeError('unreachable')


# ==========================================================
# $func436
# ==========================================================
def func436(var0):
    var1 = 0
    var2 = 0
    if (1 if func267(var0) != 10 else 0):
        break
    var2 = 100
    while True:  # loop $label2
        if (1 if var2 == 0 else 0):
            break
        if (1 if i32_load(var0) == 0 else 0):
            break
        var2 = (var2 - 1)
        if (1 if i32_load(var0 + 4) == 0 else 0):
            continue
        break  # end loop
    if (1 if func267(var0) != 10 else 0):
        break
    var2 = (var0 + 4)
    while True:  # loop $label4
        var1 = i32_load(var0)
        if (1 if (i32_load(var0) & 2147483647) != 2147483647 else 0):
            break
        var1 = (var1 | -2147483648)
        var1 = func434(var0, var1, (i32_load(var0 + 8) ^ 128))
        if (1 if var1 == 0 else 0):
            break
        if (1 if var1 != 27 else 0):
            break
        if (1 if func267(var0) == 10 else 0):
            continue
        break  # end loop


# ==========================================================
# $func438
# ==========================================================
def func438():
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var0 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    i32_store(var0 + 24, 0)
    i64_store(var0 + 16, 0)
    i64_store(var0 + 8, 0)
    if global4:
        a_q()
    if (i32_load8_u(9684264) & 15):
        if (1 if i32_load(global3 + 24) != (i32_load(9684268) & 2147483647) else 0):
            break
    var5 = i32_load(9684288)
    if i32_load(9684288):
        var2 = i32_load(9684296)
        break
    func175(9684320)
    var2 = 2
    i32_store(var0 + 20, 2)
    i32_store(var0 + 16, 0)
    var1 = i32_load(9684292)
    i32_store(var0 + 12, i32_load(9684292))
    var3 = (var0 + 8)
    i32_store(9684292, (var0 + 8))
    i32_store((var1 if i32_load(9684308) else 9684308), var3)
    func154(9684320)
    var3 = (var0 + 20)
    func54(9684264)
    var4 = global3
    var1 = (var0 + 4)
    if (var0 + 4):
        i32_store(var1, i32_load8_u(var4 + 40))
    i32_store8(var4 + 40, 2)
    if (1 if i32_load(var0 + 4) == 1 else 0):
        i32_store8(global3 + 40, 1)
    var4 = (1 if var5 == 0 else 0)
    var1 = func265(var3, var2, (1 if var5 == 0 else 0))
    if (1 if i32_load(var3) != var2 else 0):
        break
    while True:  # loop $label3
        if ((1 if var1 != 27 else 0) if var1 else 0):
            break
        var1 = func265(var3, var2, var4)
        if (1 if i32_load(var3) == var2 else 0):
            continue
        break  # end loop
    var1 = (var1 if (1 if var1 != 27 else 0) else 0)
    if var5:
        if (1 if var1 == 11 else 0):
            var1 = (11 if (1 if i32_load(9684296) == var2 else 0) else 0)
        if (1 if -1 != -2147483647 else 0):
            break
        func97(9684300)
        break
    if (1 if 2 == 0 else 0):
        func175(9684320)
        if (1 if i32_load(9684292) == (var0 + 8) else 0):
            i32_store(9684292, i32_load(var0 + 12))
            break
        var2 = i32_load(var0 + 8)
        if (1 if i32_load(var0 + 8) == 0 else 0):
            break
        i32_store(var2 + 4, i32_load(var0 + 12))
        if (1 if i32_load(9684308) == (var0 + 8) else 0):
            i32_store(9684308, i32_load(var0 + 8))
            break
        var2 = i32_load(var0 + 12)
        if (1 if i32_load(var0 + 12) == 0 else 0):
            break
        i32_store(var2, i32_load(var0 + 8))
        func154(9684320)
        var2 = i32_load(var0 + 24)
        if (1 if i32_load(var0 + 24) == 0 else 0):
            break
        if (1 if -1 != 1 else 0):
            break
        func97(i32_load(var0 + 24))
        break
    func175((var0 + 20))
    if i32_load(var0 + 12):
        break
    if (i32_load8_u(9684264) & 8):
        break
    var2 = i32_load(var0 + 8)
    if i32_load(var0 + 8):
        var1 = i32_load(9684268)
        if (1 if i32_load(9684268) > 0 else 0):
        var1 = (var2 + 12)
        i32_atomic_store((var2 + 12), 0)
        func111(var1, 2147483647)
        break
    if (i32_load8_u(9684264) & 8):
        break
    break
    var2 = func55(9684264)
    var3 = i32_load(var0 + 4)
    if (1 if i32_load(var0 + 4) <= 2 else 0):
        i32_store8(global3 + 40, var3)
    else:
    if (1 if (var2 if var2 else var1) != 11 else 0):
        break
    var1 = 1
    if (1 if 1 <= 2 else 0):
        i32_store8(global3 + 40, var1)
    else:
    global global0
    global0 = (var0 + 32)
    return 0


# ==========================================================
# $vc
# Export: vc
# ==========================================================
def vc():
    """Export: vc"""
    var0 = 0
    var0 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    func231(var0)
    i32_store(var0 + 12, 1)
    func186((var0 + 44), var0, 78, 0)
    global global0
    global0 = (var0 + 48)


# ==========================================================
# $ce
# Export: ce
# ==========================================================
def ce():
    """Export: ce"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    i32_store8(9147213, 1)
    i32_store8(9147152, 0)
    i32_store8(9681884, 0)
    var0 = i32_load(9142440)
    var0 = (i32_load(9142440) * var0)
    var0 = (-1 if (1 if var0 < 0 else 0) else ((i32_load(9142440) * var0) << 1))
    var1 = func26((-1 if (1 if var0 < 0 else 0) else ((i32_load(9142440) * var0) << 1)))
    # Unknown: memory.fill []
    i32_store(9142436, var1)
    var0 = i32_load(9142872)
    if (1 if ((1 if i32_load(9142872) != 2147483647 else 0) if var0 else 0) == 0 else 0):
        i32_store(9142872, 1)
    la()
    if (1 if i32_load8_u(9147152) == 0 else 0):
        func52((207 if i32_load8_u(9143020) else 0), 0)
        a_b()
    var1 = i32_load(9671136)
    if (1 if i32_load(9671136) >= 4 else 0):
        var2 = i32_load(9671128)
        var0 = 3
        while True:  # loop $label1
            var3 = (var2 + (var0 * 132))
            if (1 if i32_load8_u((var2 + (var0 * 132)) + 125) == 3 else 0):
                break
            if (1 if i32_load(var3 + 28) == 0 else 0):
                break
            if (1 if i32_load(var3 + 32) != -1 else 0):
                break
            i32_store(var3 + 32, 0)
            func240(var3, 500, 0)
            var1 = i32_load(9671136)
            var2 = i32_load(9671128)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < var1 else 0):
                continue
            break  # end loop
    var0 = i32_load(9142424)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load(9147376):
    else:
        var2 = i32_load(9142440)
        var2 = ((i32_load(9142440) * var2) + 2)
        var2 = (-1 if (1 if var2 < 0 else 0) else (((i32_load(9142440) * var2) + 2) << 1))
        var3 = func26((-1 if (1 if var2 < 0 else 0) else (((i32_load(9142440) * var2) + 2) << 1)))
        # Unknown: memory.fill []
        i32_store(9147376, var3)
    if (1 if (1 if i32_load(var0 + 48) != 0 else 0) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    if (1 if var1 < 4 else 0):
        break
    var2 = i32_load(9671128)
    var0 = 3
    while True:  # loop $label5
        var3 = (var2 + (var0 * 132))
        if (1 if i32_load8_u((var2 + (var0 * 132)) + 125) == 3 else 0):
            break
        if (1 if i32_load(var3 + 28) == 0 else 0):
            break
        if i32_load(var3 + 36):
            break
        var1 = i32_load(9671136)
        var2 = i32_load(9671128)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) < var1 else 0):
            continue
        break  # end loop
    if (1 if var1 < 4 else 0):
        break
    var0 = 3
    while True:  # loop $label7
        var1 = (i32_load(9671128) + (var0 * 132))
        if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 3 else 0):
            break
        if (1 if i32_load(var1 + 28) == 0 else 0):
            break
        if func292(var1):
            break
        func158(var1)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) < i32_load(9671136) else 0):
            continue
        break  # end loop
    return 0


# ==========================================================
# $ff
# Export: ff
# ==========================================================
def ff(var0, var1, var2, var3):
    """Export: ff"""
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0.0
    var8 = 0.0
    var4 = (global0 - 192)
    global global0
    global0 = (global0 - 192)
    if var3:
        i32_atomic_store(var4 + 8, 0)
        i32_store(var4 + 184, 0)
        break
    var5 = func799()
    i32_store(func799() + 16, var1)
    i32_store(var5 + 4, var0)
    i32_store(var5, -2129657856)
    i32_store(var5 + 188, (1 - var3))
    var0 = 0
    if (1 if var1 > 0 else 0):
        while True:  # loop $label1
            var6 = (var0 + 1)
            i64_store((var5 + ((var0 + 1) << 3)) + 16, i64_load((var2 + (var0 << 3))))
            var0 = var6
            if (1 if var6 != var1 else 0):
                continue
            break  # end loop
    if var3:
        func384(var4)
        if i32_atomic_load(var4 + 8):
            break
        var7 = a_f()
        var8 = (var7 + inf)
        if (1 if a_f() < (var7 + inf) else 0):
            var0 = (var4 + 8)
            while True:  # loop $label4
                var1 = i32_atomic_load(var0)
                var7 = a_f()
                if var1:
                    break
                if (1 if var7 < var8 else 0):
                    continue
                break  # end loop
            if var1:
                break
        break
    func384(var5)
    var7 = 0.0
    global global0
    global0 = (var4 + 192)
    return var7

