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
# $func45
# ==========================================================
def func45():
    var0 = 0
    var1 = 0
    if i32_load(9213808):
        while True:  # loop $label0
            var1 = ((var0 << 2) + 9173808)
            func47((i32_load(9671128) + (i32_load(((var0 << 2) + 9173808)) * 132)))
            i32_store(var1, 0)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < i32_load(9213808) else 0):
                continue
            break  # end loop
    var0 = 0
    i32_store(40604, -1)
    i32_store(9140316, 0)
    i32_store(9213808, 0)
    i32_store(9140320, 0)
    if (1 if i32_load(9142396) == 0 else 0):
        break
    while True:  # loop $label2
        func38(i32_load((i32_load(9142392) + (var0 << 2))))
        var0 = (var0 + 1)
        if (1 if (var0 + 1) < i32_load(9142396) else 0):
            continue
        break  # end loop
    i32_store(9142396, 0)
    var0 = i32_load(9142392)
    if (1 if i32_load(9142392) == 0 else 0):
        break
    if (1 if i32_load(9671176) == 0 else 0):
        break
    if i32_load(9671192):
        var0 = 0
        while True:  # loop $label4
            func38(i32_load((i32_load(9671184) + (var0 << 2))))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < i32_load(9671192) else 0):
                continue
            break  # end loop
    i32_store(9671192, 0)
    i32_store(9671176, 0)
    i32_store8(9142412, 0)
    if (1 if i32_load8_u(9684396) == 0 else 0):
        break
    i32_store8(9684396, 0)
    a_b()


# ==========================================================
# $func47
# ==========================================================
def func47(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if i32_load8_u(9142906):
        var3 = i32_load(var0 + 40)
        if (1 if i32_load(var0 + 40) == 0 else 0):
            break
        var1 = i32_load8_u(var0 + 127)
        var1 = (i32_load8_u(var0 + 127) if var1 else 16)
        if i32_load8_u(9142916):
            if (1 if var1 <= 15 else 0):
                var1 = (var1 << 4)
                var4 = ((((i32_load(((var1 << 4) + 1748)) << 8) + i32_load((var1 + 1744))) + (i32_load((var1 + 1752)) << 16)) + (i32_load((var1 + 1756)) << 24))
            i32_store(var2 + 36, var3)
            i32_store(var2 + 32, var4)
            a_b()
            break
        i32_store(var2 + 20, var3)
        i32_store(var2 + 16, var1)
        a_b()
        break
    if i32_load8_u(9142916):
        var1 = i32_load(var0 + 40)
        if (1 if i32_load(var0 + 40) == 0 else 0):
            break
        var3 = i32_load8_u(var0 + 125)
        i32_store(var2 + 4, var1)
        i32_store(var2, (var3 << 8))
        a_b()
        break
    var1 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) != 1 else 0):
        break
    if (1 if i32_load(var1 + 216) < 2 else 0):
        break
    var4 = i32_load(var0 + 12)
    if (1 if i32_load(var0 + 12) == 0 else 0):
        break
    var5 = i32_load(var4 + 8)
    if (1 if i32_load(var4 + 8) == 0 else 0):
        break
    var1 = 0
    while True:  # loop $label3
        var3 = (i32_load(var4) + (var1 << 2))
        if (1 if i32_load((i32_load(var4) + (var1 << 2)) + 4) == 1 else 0):
            func38(i32_load(var3))
            var4 = i32_load(var0 + 12)
            var5 = (i32_load(var4 + 8) - 2)
            i32_store(i32_load(var0 + 12) + 8, (i32_load(var4 + 8) - 2))
            if (1 if var1 < var5 else 0):
                var6 = i32_load(var4)
                var3 = var1
                while True:  # loop $label2
                    var5 = (var6 + (var3 << 2))
                    i32_store((var6 + (var3 << 2)), i32_load(var5 + 8))
                    var3 = (var3 + 1)
                    var5 = i32_load(var4 + 8)
                    if (1 if (var3 + 1) < i32_load(var4 + 8) else 0):
                        continue
                    break  # end loop
            var1 = (var1 - 2)
        var1 = (var1 + 2)
        if (1 if (var1 + 2) < var5 else 0):
            continue
        break  # end loop
    break
    func38(i32_load(var0 + 92))
    i32_store(var0 + 92, 0)
    var1 = i32_load(var0 + 80)
    if (1 if i32_load(var0 + 80) == 0 else 0):
        break
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) != 1 else 0):
        break
    func38(var1)
    i32_store(var0 + 80, 0)
    global global0
    global0 = (var2 + 48)


# ==========================================================
# $func55
# ==========================================================
def func55(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if (i32_load8_u(var0) & 15):
        break
    if 10:
        break
    return 0
    var2 = i32_load(var0)
    if (1 if (i32_load(var0) & 15) == 0 else 0):
        if (1 if 10 == 0 else 0):
            break
        var2 = i32_load(var0)
    var1 = func185(var0)
    if (1 if func185(var0) != 10 else 0):
        break
    var3 = (var0 + 8)
    var4 = (var0 + 4)
    var1 = 100
    while True:  # loop $label3
        if (1 if var1 == 0 else 0):
            break
        if (1 if i32_load(var4) == 0 else 0):
            break
        var1 = (var1 - 1)
        if (1 if i32_load(var3) == 0 else 0):
            continue
        break  # end loop
    var1 = func185(var0)
    if (1 if func185(var0) != 10 else 0):
        break
    var5 = ((var2 ^ -1) & 128)
    var6 = (1 if (var2 & 4) == 0 else 0)
    var2 = (1 if (var2 & 3) != 2 else 0)
    while True:  # loop $label7
        var1 = i32_load(var0 + 4)
        var7 = (i32_load(var0 + 4) & 1073741823)
        if (1 if ((i32_load(var0 + 4) & 1073741823) | ((1 if var1 != 0 else 0) & var6)) == 0 else 0):
            break
        if var2:
            break
        if (1 if var7 != i32_load(global3 + 24) else 0):
            break
        break
        var1 = (var1 | -2147483648)
        var1 = func434(var4, var1, var5)
        if (1 if var1 == 27 else 0):
            break
        if var1:
            break
        var1 = func185(var0)
        if (1 if func185(var0) == 10 else 0):
            continue
        break  # end loop
    return var1


# ==========================================================
# $func63
# ==========================================================
def func63(var0, var1, var2, var3, param4):
    var4 = 0
    var5 = 0
    var6 = 0
    var4 = i32_load(((i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) * 40) + 9671200) + 32)
    if i32_load(((i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) * 40) + 9671200) + 32):
        # call_indirect via table[var4]
    if (1 if i32_load8_u(var0 + 125) == 3 else 0):
        break
    var5 = i32_load(var0 + 44)
    if i32_load(var0 + 44):
        var6 = i32_load(9142848)
        var4 = i32_load(9215884)
        i32_store((i32_load(9215884) + (var5 << 4)) + 4, var1)
        i32_store((var4 + (i32_load(var0 + 44) << 4)) + 8, i32_load(var0 + 28))
        i32_store((var4 + (i32_load(var0 + 44) << 4)) + 12, var2)
        if var3:
            i32_store((var4 + (i32_load(var0 + 44) << 4)), (var6 + ((var3 & 0xFFFFFFFF) // 25)))
            return
        i32_store((var4 + (i32_load(var0 + 44) << 4)), i32_load(9142848))
        # call_indirect via table[i32_load(((var1 * 40) + 9671200) + 20)]
        var0 = (i32_load(9215884) + (i32_load(var0 + 44) << 4))
        if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4))) != i32_load(9142848) else 0):
            break
        i32_store(var0, 0)
        return
    i32_store(var0 + 44, ((Ua(var3, var1, i32_load(var0 + 28), var2) & 0xFFFFFFFF) >> 2))

