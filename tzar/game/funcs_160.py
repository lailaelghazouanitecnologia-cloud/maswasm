"""
Auto-generated from WAT. Contains 3 functions.
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
# $func332
# ==========================================================
def func332(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var1 = i32_load(9142872)
    var3 = i32_load(9561692)
    if (1 if var0 != -1 else 0):
        if (1 if i32_load8_u(9163792) == 0 else 0):
            break
    i32_store(9143000, 0)
    var2 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var2 * 132)))
        i32_store(9213820, 0)
    func45()
    var4 = i32_load((((var3 + (var1 * 286704)) + (i32_load(38428) << 2)) + 284636))
    if (1 if i32_load((((var3 + (var1 * 286704)) + (i32_load(38428) << 2)) + 284636)) == 0 else 0):
        break
    var1 = i32_load(var4 + 8)
    if (1 if i32_load(var4 + 8) == 0 else 0):
        break
    var3 = 0
    if (1 if var0 == -1 else 0):
        while True:  # loop $label3
            var2 = i32_load((i32_load(var4) + (var3 << 2)))
            if (1 if i32_load((i32_load(var4) + (var3 << 2))) == 0 else 0):
                break
            var2 = (i32_load(9671128) + (var2 * 132))
            if (1 if i32_load8_u(9147152) == 0 else 0):
                if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var2 + 110))))) == 0 else 0):
                    break
                if (1 if i32_load((i32_load(9215884) + (i32_load(var2 + 44) << 4)) + 4) == 20 else 0):
                    break
                if (1 if i32_load8_u(var2 + 127) == 6 else 0):
                    break
            func44(var2, 0)
            var1 = i32_load(var4 + 8)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) < var1 else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    while True:  # loop $label6
        var1 = i32_load((i32_load(var4) + (var3 << 2)))
        if (1 if i32_load((i32_load(var4) + (var3 << 2))) == 0 else 0):
            break
        var1 = (i32_load(9671128) + (var1 * 132))
        if i32_load8_u(9163792):
            if (1 if i32_load8_u(9147152) == 0 else 0):
                if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var1 + 110))))) == 0 else 0):
                    break
                if (1 if i32_load((i32_load(9215884) + (i32_load(var1 + 44) << 4)) + 4) == 20 else 0):
                    break
                if (1 if i32_load8_u(var1 + 127) == 6 else 0):
                    break
            func44(var1, 0)
            break
        var6 = i32_load(var1 + 28)
        var2 = i32_load(9681836)
        if (1 if i32_load(9681836) != i32_load(9681832) else 0):
            var1 = i32_load(9681828)
            break
        var1 = (i32_load(9681840) + var2)
        i32_store(9681832, (i32_load(9681840) + var2))
        var5 = i32_load(9681828)
        var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        if var2:
            # Unknown: memory.copy []
        if var5:
            var2 = i32_load(9681836)
        i32_store(9681828, var1)
        i32_store(9681836, (var2 + 1))
        i32_store((var1 + (var2 << 2)), var6)
        var3 = (var3 + 1)
        if (1 if (var3 + 1) < i32_load(var4 + 8) else 0):
            continue
        break  # end loop
    if (1 if var0 != -1 else 0):
        if (1 if i32_load8_u(9163792) == 0 else 0):
            break
    return
    func172(1)


# ==========================================================
# $func333
# ==========================================================
def func333(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var1 = i32_load(9142872)
    var2 = i32_load(9561692)
    if (1 if var0 != -1 else 0):
        if (1 if i32_load8_u(9163792) == 0 else 0):
            break
    i32_store(9143000, 0)
    var3 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var3 * 132)))
        i32_store(9213820, 0)
    func45()
    var7 = (var2 + (var1 * 286704))
    var8 = (1 if var0 == -1 else 0)
    var3 = 0
    while True:  # loop $label7
        var4 = i32_load(((var7 + (var3 << 2)) + 284636))
        if (1 if i32_load(((var7 + (var3 << 2)) + 284636)) == 0 else 0):
            break
        var5 = 0
        if (1 if i32_load(var4 + 8) == 0 else 0):
            break
        while True:  # loop $label6
            var1 = i32_load((i32_load(var4) + (var5 << 2)))
            if (1 if i32_load((i32_load(var4) + (var5 << 2))) == 0 else 0):
                break
            var1 = (i32_load(9671128) + (var1 * 132))
            if (1 if i32_load((i32_load(9671128) + (var1 * 132)) + 84) >= 12 else 0):
                if (1 if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 264) == 0 else 0):
                    break
            var2 = i32_load(var1 + 24)
            if (1 if i32_load(var1 + 24) == 0 else 0):
                break
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            if (1 if var8 == 0 else 0):
                if (1 if i32_load8_u(9163792) == 0 else 0):
                    break
            if (1 if i32_load8_u(9147152) == 0 else 0):
                if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var1 + 110))))) == 0 else 0):
                    break
                if (1 if i32_load((i32_load(9215884) + (i32_load(var1 + 44) << 4)) + 4) == 20 else 0):
                    break
                if (1 if i32_load8_u(var1 + 127) == 6 else 0):
                    break
            func44(var1, 0)
            break
            var9 = i32_load(var1 + 28)
            var1 = i32_load(9681836)
            if (1 if i32_load(9681836) != i32_load(9681832) else 0):
                var2 = i32_load(9681828)
                break
            var2 = (i32_load(9681840) + var1)
            i32_store(9681832, (i32_load(9681840) + var1))
            var6 = i32_load(9681828)
            var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
            if var1:
                # Unknown: memory.copy []
            if var6:
                var1 = i32_load(9681836)
            i32_store(9681828, var2)
            i32_store(9681836, (var1 + 1))
            i32_store((var2 + (var1 << 2)), var9)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) < i32_load(var4 + 8) else 0):
                continue
            break  # end loop
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != 255 else 0):
            continue
        break  # end loop
    if (1 if var0 != -1 else 0):
        if (1 if i32_load8_u(9163792) == 0 else 0):
            break
    return
    func172(1)


# ==========================================================
# $func334
# ==========================================================
def func334(var0):
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
    var11 = 0
    var12 = 0
    var13 = 0
    var5 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    i32_store(9143000, 0)
    var0 = i32_load(9142872)
    var2 = i32_load(9561692)
    var3 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var3 * 132)))
        i32_store(9213820, 0)
    func45()
    var11 = (var2 + (var0 * 286704))
    while True:  # loop $label14
        var12 = i32_load(((var7 << 2) + 9940))
        var8 = i32_load(((var11 + (i32_load(((var7 << 2) + 9940)) << 2)) + 284636))
        if (1 if i32_load(((var11 + (i32_load(((var7 << 2) + 9940)) << 2)) + 284636)) == 0 else 0):
            break
        var9 = 0
        var10 = i32_load(var8 + 8)
        if (1 if i32_load(var8 + 8) == 0 else 0):
            break
        while True:  # loop $label13
            var0 = i32_load((i32_load(var8) + (var9 << 2)))
            if (1 if i32_load((i32_load(var8) + (var9 << 2))) == 0 else 0):
                break
            var6 = i32_load(9671128)
            var2 = (i32_load(9671128) + (var0 * 132))
            var0 = i32_load((i32_load(9671128) + (var0 * 132)) + 44)
            if (1 if ((1 if i32_load((i32_load(9215884) + (i32_load((i32_load(9671128) + (var0 * 132)) + 44) << 4)) + 4) == 22 else 0) | (1 if var0 == 0 else 0)) == 0 else 0):
                break
            if i32_load8_u(var2 + 125):
                break
            if i32_load(var2 + 36):
                break
            var3 = i32_load(var2 + 28)
            var0 = i32_load(9215928)
            if (1 if i32_load(9215928) == 0 else 0):
                break
            var1 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var4 = i32_load(var0)
            var0 = 0
            while True:  # loop $label3
                if (1 if var3 != i32_load((var6 + (i32_load((var4 + (var0 << 2))) * 132)) + 28) else 0):
                    var0 = (var0 + 1)
                    if (1 if var1 != (var0 + 1) else 0):
                        continue
                    break
                break  # end loop
            var1 = 1
            break
            var0 = i32_load(9215932)
            if (1 if i32_load(9215932) == 0 else 0):
                break
            var1 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var4 = i32_load(var0)
            var0 = 0
            while True:  # loop $label6
                if (1 if var3 == i32_load((var6 + (i32_load((var4 + (var0 << 2))) * 132)) + 28) else 0):
                    var1 = 1
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var1 else 0):
                    continue
                break  # end loop
            var0 = i32_load(9215936)
            if (1 if i32_load(9215936) == 0 else 0):
                break
            var1 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var4 = i32_load(var0)
            var0 = 0
            while True:  # loop $label8
                if (1 if var3 == i32_load((var6 + (i32_load((var4 + (var0 << 2))) * 132)) + 28) else 0):
                    var1 = 1
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var1 else 0):
                    continue
                break  # end loop
            var1 = 0
            var0 = i32_load(9215940)
            if (1 if i32_load(9215940) == 0 else 0):
                break
            var4 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var13 = i32_load(var0)
            var0 = 0
            while True:  # loop $label9
                var1 = (1 if i32_load((var6 + (i32_load((var13 + (var0 << 2))) * 132)) + 28) == var3 else 0)
                if (1 if i32_load((var6 + (i32_load((var13 + (var0 << 2))) * 132)) + 28) == var3 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var4 else 0):
                    continue
                break  # end loop
            if var1:
                break
            if (1 if var12 != i32_load8_u(var2 + 122) else 0):
                break
            if (1 if i32_load8_u(var2 + 129) == 10 else 0):
                break
            if i32_load(var2 + 92):
                break
            var1 = i32_load(9213808)
            if (1 if i32_load(9213808) > 9999 else 0):
                break
            var0 = 1
            i32_store(9213808, (var1 + 1))
            i32_store(((var1 << 2) + 9173808), var3)
            if (i32_load8_u(9142906) | i32_load8_u(9142916)):
                break
            var0 = 0
            if i32_load8_u(9142917):
                break
            var0 = i32_load(9299880)
            if i32_load(9299880):
                var0 = (var0 - 1)
                i32_store(9299880, (var0 - 1))
                var0 = i32_load((i32_load(9299872) + (var0 << 2)))
                break
            var0 = i32_load(9163776)
            var3 = (i32_load(9163776) + 1)
            i32_store(9163776, (i32_load(9163776) + 1))
            var1 = i32_load(9163784)
            if (1 if var3 < i32_load(9163784) else 0):
                break
            i32_store(var5 + 16, var1)
            a_b()
            i32_store(9163784, (i32_load(9163784) + 40000))
            i32_store(var2 + 92, var0)
            if (1 if i32_load(var2 + 36) == 0 else 0):
            func203(var2)
            if i32_load8_u(9163792):
                break
            var10 = i32_load(var8 + 8)
            var9 = (var9 + 1)
            if (1 if (var9 + 1) < var10 else 0):
                continue
            break  # end loop
        var7 = (var7 + 1)
        if (1 if (var7 + 1) != 3 else 0):
            continue
        break  # end loop
    if (1 if i32_load(9213808) == 0 else 0):
        break
    break
    if i32_load8_u(9142917):
        break
    var0 = i32_load(var2 + 36)
    var0 = (i32_load(9671128) + ((i32_load(var2 + 36) if var0 else i32_load(var2 + 28)) * 132))
    var2 = ((i32_load8_u((i32_load(9671128) + ((i32_load(var2 + 36) if var0 else i32_load(var2 + 28)) * 132)) + 122) * 404) + 9568096)
    var3 = i32_load(((i32_load8_u((i32_load(9671128) + ((i32_load(var2 + 36) if var0 else i32_load(var2 + 28)) * 132)) + 122) * 404) + 9568096) + 220)
    var1 = i32_load16_u(var0 + 114)
    i32_store(var5, (((i32_load(var2 + 216) << 4) & 2147483632) + (i32_load16_u(var0 + 112) << 5)))
    i32_store(var5 + 4, (((var3 << 4) & 2147483632) + (var1 << 5)))
    global global0
    global0 = (var5 + 32)

