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
# $La
# Export: La
# ==========================================================
def La(var0, var1):
    """Export: La"""
    var2 = 0
    var3 = 0
    if i32_load(9147132):
        var1 = i32_load(9561776)
        if (1 if i32_load(9561776) != i32_load(9561772) else 0):
            var2 = i32_load(9561768)
            break
        var2 = (i32_load(9561780) + var1)
        i32_store(9561772, (i32_load(9561780) + var1))
        var3 = i32_load(9561768)
        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        if var1:
            # Unknown: memory.copy []
        if var3:
            var1 = i32_load(9561776)
        i32_store(9561768, var2)
        i32_store(9561776, (var1 + 1))
        i32_store((var2 + (var1 << 2)), var0)
        var3 = (i32_load(59176) + 10)
        var1 = i32_load(9561776)
        if (1 if i32_load(9561776) != i32_load(9561772) else 0):
            var0 = var2
            break
        var0 = (i32_load(9561780) + var1)
        i32_store(9561772, (i32_load(9561780) + var1))
        var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var1:
            # Unknown: memory.copy []
        i32_store(9561768, var0)
        var1 = i32_load(9561776)
        i32_store(9561776, (var1 + 1))
        i32_store((var0 + (var1 << 2)), var3)
        return
    if (1 if var1 == 0 else 0):
        var2 = i32_load(9142892)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var3 = i32_load(9561692)
        var1 = 1
        while True:  # loop $label4
            if (1 if var0 == i32_load((var3 + (var1 * 286704)) + 284616) else 0):
                var0 = var1
                break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var2 else 0):
                continue
            break  # end loop
        break
    if (1 if var0 == 0 else 0):
        break
    if (1 if (i32_load8_u(9147213) | i32_load8_u(9147214)) == 0 else 0):
        break
    if (1 if i32_load(9142892) > (var0 - 1) else 0):
        var1 = i32_load(9561692)
        if (i32_load8_u(9147125) | (1 if i32_load8_u(9147213) == 0 else 0)):
            if (1 if i32_load8_u(9147126) == 0 else 0):
                break
        var3 = i32_load((var1 + (var0 * 286704)) + 284616)
        var2 = i32_load(9561776)
        if (1 if i32_load(9561776) != i32_load(9561772) else 0):
            var0 = i32_load(9561768)
            break
        var0 = (i32_load(9561780) + var2)
        i32_store(9561772, (i32_load(9561780) + var2))
        var1 = i32_load(9561768)
        var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var2:
            # Unknown: memory.copy []
        if var1:
            var2 = i32_load(9561776)
        i32_store(9561768, var0)
        i32_store(9561776, (var2 + 1))
        i32_store((var0 + (var2 << 2)), var3)
        var3 = (i32_load(59176) + 10)
        var2 = i32_load(9561776)
        if (1 if i32_load(9561776) != i32_load(9561772) else 0):
            var1 = var0
            break
        var1 = (i32_load(9561780) + var2)
        i32_store(9561772, (i32_load(9561780) + var2))
        var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        if var2:
            # Unknown: memory.copy []
        i32_store(9561768, var1)
        var2 = i32_load(9561776)
        i32_store(9561776, (var2 + 1))
        i32_store((var1 + (var2 << 2)), var3)
        break
        var0 = (var0 * 286704)
        var0 = (i32_load(9561692) + var0)
        i32_store((i32_load(9561692) + var0) + 284628, i32_load(var0 + 284616))
        i32_store(var0 + 284616, 0)


# ==========================================================
# $func265
# ==========================================================
def func265(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0.0
    var6 = 0.0
    var7 = 0.0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = global5
    if global5:
        break
    var4 = global3
    if (1 if i32_load8_u(global3 + 40) != 1 else 0):
        break
    if (1 if i32_load8_u(var4 + 41) != 1 else 0):
        break
    var5 = float((1 if var3 else 100))
    var7 = (a_f() + inf)
    var3 = global3
    while True:  # loop $label4
        if i32_load(var3 + 36):
            var0 = 11
            break
        var6 = (var7 - a_f())
        if (1 if (var7 - a_f()) <= 0.0 else 0):
            break
        var4 = func131(var0, var1, (var5 if (1 if var5 < var6 else 0) else var6))
        if (1 if func131(var0, var1, (var5 if (1 if var5 < var6 else 0) else var6)) == -73 else 0):
            continue
        break  # end loop
    break
    var0 = (0 - func131(var0, var1, inf))
    var0 = (((0 - func131(var0, var1, inf)) if (1 if (var0 & -17) == 11 else 0) else 0) if (1 if var0 != 73 else 0) else var0)
    if (1 if (((0 - func131(var0, var1, inf)) if (1 if (var0 & -17) == 11 else 0) else 0) if (1 if var0 != 73 else 0) else var0) != 27 else 0):
        break
    var0 = (27 if i32_load(9688304) else 0)
    global global0
    global0 = (var2 + 16)
    return var0


# ==========================================================
# $func286
# ==========================================================
def func286(var0):
    func277(i32_load16_u(var0 + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110))
    if (1 if i32_load8_u(9147329) == 0 else 0):
        break
    if (1 if i32_load8_u(9147334) == 0 else 0):
        break
    i32_store8(var0 + 124, (i32_load16_u(var0 + 114) % 5))
    return
    if (1 if i32_load8_u(9147331) == 0 else 0):
        break
    if (1 if i32_load8_u(9147332) == 0 else 0):
        break
    i32_store8(var0 + 124, (i32_load16_u(var0 + 112) % 7))
    return


# ==========================================================
# $func291
# ==========================================================
def func291(var0, var1, var2, var3):
    if (1 if i32_load8_u(var0 + 125) == 1 else 0):
        func63(0  # stack underflow, var0, var1, var2, var3)
        return
    i32_store((i32_load(9215884) + (i32_load(var0 + 44) << 4)), (i32_load(9142848) + ((var3 & 0xFFFFFFFF) // 25)))


# ==========================================================
# $func325
# ==========================================================
def func325(var0):
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
    i32_store(9143000, 0)
    var0 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var0 * 132)))
        i32_store(9213820, 0)
    func45()
    var10 = (i32_load(9561692) + (i32_load(9142872) * 286704))
    while True:  # loop $label12
        if (1 if var4 == i32_load(38440) else 0):
            break
        if (1 if var4 == i32_load(38772) else 0):
            break
        if (1 if var4 != i32_load(38928) else 0):
            break
        var7 = i32_load(((var10 + (var4 << 2)) + 284636))
        if (1 if i32_load(((var10 + (var4 << 2)) + 284636)) == 0 else 0):
            break
        var8 = 0
        var9 = i32_load(var7 + 8)
        if (1 if i32_load(var7 + 8) == 0 else 0):
            break
        while True:  # loop $label11
            var0 = i32_load((i32_load(var7) + (var8 << 2)))
            if (1 if i32_load((i32_load(var7) + (var8 << 2))) == 0 else 0):
                break
            var5 = i32_load(9671128)
            var1 = (i32_load(9671128) + (var0 * 132))
            if (1 if i32_load8_u(9147152) == 0 else 0):
                if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var1 + 110))))) == 0 else 0):
                    break
                if (1 if i32_load((i32_load(9215884) + (i32_load(var1 + 44) << 4)) + 4) == 20 else 0):
                    break
                if (1 if i32_load8_u(var1 + 127) == 6 else 0):
                    break
            var6 = i32_load(var1 + 28)
            var0 = i32_load(9215928)
            if (1 if i32_load(9215928) == 0 else 0):
                break
            var2 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var3 = i32_load(var0)
            var0 = 0
            while True:  # loop $label4
                if (1 if i32_load((var5 + (i32_load((var3 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var2 else 0):
                    continue
                break  # end loop
            var0 = i32_load(9215932)
            if (1 if i32_load(9215932) == 0 else 0):
                break
            var2 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var3 = i32_load(var0)
            var0 = 0
            while True:  # loop $label6
                if (1 if i32_load((var5 + (i32_load((var3 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var2 else 0):
                    continue
                break  # end loop
            var0 = i32_load(9215936)
            if (1 if i32_load(9215936) == 0 else 0):
                break
            var2 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var3 = i32_load(var0)
            var0 = 0
            while True:  # loop $label8
                if (1 if i32_load((var5 + (i32_load((var3 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var2 else 0):
                    continue
                break  # end loop
            var0 = i32_load(9215940)
            if (1 if i32_load(9215940) == 0 else 0):
                break
            var2 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var3 = i32_load(var0)
            var0 = 0
            while True:  # loop $label10
                if (1 if i32_load((var5 + (i32_load((var3 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var2 else 0):
                    continue
                break  # end loop
            if i32_load(var1 + 36):
                break
            if (1 if i32_load8_u(var1 + 125) == 8 else 0):
                break
            func44(var1, 0)
            var9 = i32_load(var7 + 8)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) < var9 else 0):
                continue
            break  # end loop
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != 255 else 0):
            continue
        break  # end loop


# ==========================================================
# $func326
# ==========================================================
def func326(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    i32_store(9143000, 0)
    var0 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var0 * 132)))
        i32_store(9213820, 0)
    func45()
    var5 = (i32_load(9561692) + (i32_load(9142872) * 286704))
    while True:  # loop $label3
        var0 = ((var1 * 404) + 9568096)
        if i32_load(((var1 * 404) + 9568096) + 264):
            break
        if (1 if i32_load(var0 + 268) == 1 else 0):
            break
        if (1 if i32_load(var0 + 92) == 0 else 0):
            break
        if (1 if i32_load(var0 + 224) > 1 else 0):
            break
        var2 = i32_load(((var5 + (var1 << 2)) + 284636))
        if (1 if i32_load(((var5 + (var1 << 2)) + 284636)) == 0 else 0):
            break
        var3 = 0
        var4 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        while True:  # loop $label2
            var0 = i32_load((i32_load(var2) + (var3 << 2)))
            if (1 if i32_load((i32_load(var2) + (var3 << 2))) == 0 else 0):
                break
            var0 = (i32_load(9671128) + (var0 * 132))
            if (1 if i32_load8_u(9147152) == 0 else 0):
                if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var0 + 110))))) == 0 else 0):
                    break
                if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 20 else 0):
                    break
                if (1 if i32_load8_u(var0 + 127) == 6 else 0):
                    break
            if (1 if func159(var0) == 0 else 0):
                break
            if i32_load(var0 + 36):
                break
            if (1 if i32_load8_u(var0 + 125) == 8 else 0):
                break
            if (1 if i32_load8_u(var0 + 123) == 63 else 0):
                break
            func44(var0, 0)
            var4 = i32_load(var2 + 8)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) < var4 else 0):
                continue
            break  # end loop
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != 255 else 0):
            continue
        break  # end loop

