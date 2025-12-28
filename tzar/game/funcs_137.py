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
# $Pc
# Export: Pc
# ==========================================================
def Pc(var0):
    """Export: Pc"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var3 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    if (1 if var0 == 2 else 0):
        var0 = i32_load(9568088)
        var2 = i32_load(i32_load(9568088) + 104)
        var1 = i32_load(var0 + 88)
        var6 = i32_load(var0 + 96)
        i32_store(var3, i32_load(var0 + 80))
        i32_store(var3 + 4, var1)
        i32_store(var3 + 8, var6)
        i32_store(var3 + 12, var2)
        var2 = 0
        var0 = (global0 - 32)
        global global0
        global0 = (global0 - 32)
        var6 = i32_load(9684424)
        if i32_load(i32_load(9684424) + 8):
            while True:  # loop $label1
                var1 = (i32_load(9671128) + (i32_load((i32_load(var6) + (var2 << 2))) * 132))
                var4 = i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 156)
                i32_store8((i32_load(9671128) + (i32_load((i32_load(var6) + (var2 << 2))) * 132)) + 127, i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 156))
                var5 = i32_load(var1 + 40)
                if (1 if i32_load(var1 + 40) == 0 else 0):
                    break
                var1 = (var4 if var4 else (i32_load16_u(var1 + 110) + 16))
                if i32_load8_u(9142916):
                    var4 = 0
                    if (1 if var1 <= 15 else 0):
                        var1 = (var1 << 4)
                        var4 = ((((i32_load(((var1 << 4) + 1748)) << 8) + i32_load((var1 + 1744))) + (i32_load((var1 + 1752)) << 16)) + (i32_load((var1 + 1756)) << 24))
                    i32_store(var0 + 20, var5)
                    i32_store(var0 + 16, var4)
                    a_b()
                    break
                i32_store(var0 + 4, var5)
                i32_store(var0, var1)
                a_b()
                var2 = (var2 + 1)
                if (1 if (var2 + 1) < i32_load(var6 + 8) else 0):
                    continue
                break  # end loop
        global global0
        global0 = (var0 + 32)
        break
    if (1 if i32_load(9213808) == 0 else 0):
        break
    var2 = i32_load(9684424)
    if (1 if var0 == 0 else 0):
        while True:  # loop $label7
            var4 = i32_load(((var6 << 2) + 9173808))
            var7 = i32_load(9671128)
            var5 = i32_load(var2 + 8)
            if (1 if i32_load(var2 + 8) == 0 else 0):
                break
            var1 = i32_load(var2)
            var0 = 0
            while True:  # loop $label4
                if (1 if var4 != i32_load((var1 + (var0 << 2))) else 0):
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var5 else 0):
                        continue
                    break
                break  # end loop
            if (1 if var0 < 0 else 0):
                break
            var5 = (var5 - 1)
            i32_store(var2 + 8, (var5 - 1))
            if (1 if var0 >= var5 else 0):
                break
            while True:  # loop $label5
                var0 = (var0 + 1)
                i32_store((var1 + (var0 << 2)), i32_load((var1 + ((var0 + 1) << 2))))
                if (1 if var0 < i32_load(var2 + 8) else 0):
                    continue
                break  # end loop
            var0 = (var7 + (var4 * 132))
            var1 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 156)
            i32_store8((var7 + (var4 * 132)) + 127, i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 156))
            var4 = i32_load(var0 + 40)
            if (1 if i32_load(var0 + 40) == 0 else 0):
                break
            var0 = (var1 if var1 else (i32_load16_u(var0 + 110) + 16))
            if i32_load8_u(9142916):
                var1 = 0
                if (1 if var0 <= 15 else 0):
                    var0 = (var0 << 4)
                    var1 = ((((i32_load(((var0 << 4) + 1748)) << 8) + i32_load((var0 + 1744))) + (i32_load((var0 + 1752)) << 16)) + (i32_load((var0 + 1756)) << 24))
                i32_store(var3 + 36, var4)
                i32_store(var3 + 32, var1)
                a_b()
                break
            i32_store(var3 + 20, var4)
            i32_store(var3 + 16, var0)
            a_b()
            var6 = (var6 + 1)
            if (1 if (var6 + 1) < i32_load(9213808) else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    while True:  # loop $label12
        var4 = i32_load(((var6 << 2) + 9173808))
        var7 = i32_load(9671128)
        var1 = i32_load(var2 + 8)
        if i32_load(var2 + 8):
            var5 = i32_load(var2)
            var0 = 0
            while True:  # loop $label9
                if (1 if i32_load((var5 + (var0 << 2))) == var4 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var1 else 0):
                    continue
                break  # end loop
        if (1 if i32_load(var2 + 4) != var1 else 0):
            var0 = i32_load(var2)
            break
        var0 = (i32_load(var2 + 12) + var1)
        i32_store(var2 + 4, (i32_load(var2 + 12) + var1))
        var5 = i32_load(var2)
        var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var1:
            # Unknown: memory.copy []
        if var5:
            var1 = i32_load(var2 + 8)
        i32_store(var2, var0)
        i32_store(var2 + 8, (var1 + 1))
        i32_store((var0 + (var1 << 2)), var4)
        var0 = i32_load((var7 + (var4 * 132)) + 40)
        if (1 if i32_load((var7 + (var4 * 132)) + 40) == 0 else 0):
            break
        if i32_load8_u(9142916):
            i32_store(var3 + 68, var0)
            i32_store(var3 + 64, -16711936)
            a_b()
            break
        i32_store(var3 + 52, var0)
        i32_store(var3 + 48, 0)
        a_b()
        var6 = (var6 + 1)
        if (1 if (var6 + 1) < i32_load(9213808) else 0):
            continue
        break  # end loop
    global global0
    global0 = (var3 + 80)


# ==========================================================
# $Vc
# Export: Vc
# ==========================================================
def Vc(var0, var1):
    """Export: Vc"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var3 = (64 if var1 else 48)
    var2 = i32_load(9568088)
    var4 = ((i32_load(9568088) - -64) if var1 else (var2 + 48))
    var1 = i32_load(((i32_load(9568088) - -64) if var1 else (var2 + 48)) + 8)
    if (1 if var0 < i32_load(((i32_load(9568088) - -64) if var1 else (var2 + 48)) + 8) else 0):
        var2 = i32_load((var2 + var3))
        break
    var6 = i32_load(9142892)
    var7 = (i32_load(9142892) + 1)
    if (1 if (i32_load(9142892) + 1) <= var1 else 0):
        var2 = i32_load((var2 + var3))
        break
    var3 = (var2 + var3)
    while True:  # loop $label3
        if (1 if i32_load(var4 + 4) != var1 else 0):
            var2 = i32_load(var3)
            break
        var2 = (i32_load(var4 + 12) + var1)
        i32_store(var4 + 4, (i32_load(var4 + 12) + var1))
        var5 = i32_load(var3)
        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        if var1:
            # Unknown: memory.copy []
        if var5:
            var1 = i32_load(var4 + 8)
        i32_store(var3, var2)
        i32_store(var4 + 8, (var1 + 1))
        i32_store((var2 + (var1 << 2)), 1)
        var1 = i32_load(var4 + 8)
        if (1 if i32_load(var4 + 8) < var7 else 0):
            continue
        break  # end loop
    i32_store((var2 + (var6 << 2)), 0)
    return i32_load((var2 + (var0 << 2)))


# ==========================================================
# $Uc
# Export: Uc
# ==========================================================
def Uc(var0, var1, var2):
    """Export: Uc"""
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var9 = (64 if var2 else 48)
    var5 = i32_load(9568088)
    var3 = ((i32_load(9568088) - -64) if var2 else (var5 + 48))
    var2 = i32_load(((i32_load(9568088) - -64) if var2 else (var5 + 48)) + 8)
    var6 = (i32_load(9142892) + 1)
    if (1 if i32_load(((i32_load(9568088) - -64) if var2 else (var5 + 48)) + 8) < (i32_load(9142892) + 1) else 0):
        var7 = (var5 + var9)
        while True:  # loop $label1
            if (1 if i32_load(var3 + 4) != var2 else 0):
                var4 = i32_load(var7)
                break
            var4 = (i32_load(var3 + 12) + var2)
            i32_store(var3 + 4, (i32_load(var3 + 12) + var2))
            var8 = i32_load(var7)
            var4 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
            if var2:
                # Unknown: memory.copy []
            if var8:
                var2 = i32_load(var3 + 8)
            i32_store(var7, var4)
            i32_store(var3 + 8, (var2 + 1))
            i32_store((var4 + (var2 << 2)), 1)
            var2 = i32_load(var3 + 8)
            if (1 if i32_load(var3 + 8) < var6 else 0):
                continue
            break  # end loop
    if (1 if var2 > var6 else 0):
        i32_store(var3 + 8, var6)
    i32_store((i32_load((var5 + var9)) + (var0 << 2)), var1)

