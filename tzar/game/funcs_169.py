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
# $func118
# ==========================================================
def func118(var0):
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
    var3 = (global0 - 96)
    global global0
    global0 = (global0 - 96)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var1 = i32_load(9142872)
    if (1 if i32_load(9142872) == 0 else 0):
        break
    if (1 if i32_load8_u((i32_load(9143012) + (i32_load16_u(var0 + 110) + (i32_load(9142892) * var1)))) == 0 else 0):
        break
    if (1 if i32_load8_u(var0 + 125) != 3 else 0):
        break
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 216) == 0 else 0):
        break
    while True:  # loop $label17
        var8 = 0
        while True:  # loop $label16
            var1 = i32_load(i32_load(9142424) + 48)
            var2 = ((1 if i32_load8_u(9147152) == 0 else 0) & (1 if i32_load(i32_load(9142424) + 48) != 0 else 0))
            if (1 if i32_load(var0 + 40) == 0 else 0):
                if (1 if var2 == 0 else 0):
                    break
                var2 = i32_load16_u((i32_load(9147376) + (((var9 + i32_load16_u(var0 + 112)) + (i32_load(9142440) * (var8 + i32_load16_u(var0 + 114)))) << 1)))
                if (1 if var1 == 2 else 0):
                    if (1 if var2 > 1 else 0):
                        break
                    break
                if (1 if var2 == 0 else 0):
                    break
                break
            if (1 if var2 == 0 else 0):
                break
            var2 = i32_load16_u((i32_load(9147376) + (((var9 + i32_load16_u(var0 + 112)) + (i32_load(9142440) * (var8 + i32_load16_u(var0 + 114)))) << 1)))
            if (1 if var1 == 2 else 0):
                if (1 if var2 <= 1 else 0):
                    break
                break
            if var2:
                break
            func77(var0)
            if (1 if i32_load(var0 + 40) == 0 else 0):
                break
            var1 = i32_load(var0 + 12)
            if i32_load(var0 + 12):
                var7 = 0
                if i32_load(var1 + 8):
                    while True:  # loop $label9
                        var5 = i32_load((i32_load(var1) + (var7 << 2)))
                        if (1 if i32_load((i32_load(var1) + (var7 << 2))) >= 1073741823 else 0):
                            var6 = (var5 - 1073741823)
                            var1 = i32_load(9299896)
                            if (1 if i32_load(9299896) != i32_load(9299892) else 0):
                                var2 = i32_load(9299888)
                                break
                            var2 = (i32_load(9299900) + var1)
                            i32_store(9299892, (i32_load(9299900) + var1))
                            var4 = i32_load(9299888)
                            var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                            if var1:
                                # Unknown: memory.copy []
                            if var4:
                                var1 = i32_load(9299896)
                            i32_store(9299888, var2)
                            i32_store(9299896, (var1 + 1))
                            i32_store((var2 + (var1 << 2)), var6)
                            break
                        var1 = i32_load(9299880)
                        if (1 if i32_load(9299880) != i32_load(9299876) else 0):
                            var2 = i32_load(9299872)
                            break
                        var2 = (i32_load(9299884) + var1)
                        i32_store(9299876, (i32_load(9299884) + var1))
                        var4 = i32_load(9299872)
                        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                        if var1:
                            # Unknown: memory.copy []
                        if var4:
                            var1 = i32_load(9299880)
                        i32_store(9299872, var2)
                        i32_store(9299880, (var1 + 1))
                        i32_store((var2 + (var1 << 2)), var5)
                        if i32_load8_u(9142916):
                            i32_store(var3 + 80, var5)
                            a_b()
                            break
                        i32_store(var3 + 72, var5)
                        i64_store((var3 - -64), -4602115869219225600)
                        i64_store(var3 + 56, 0)
                        i64_store(var3 + 48, 0)
                        a_b()
                        var7 = (var7 + 2)
                        var1 = i32_load(var0 + 12)
                        if (1 if (var7 + 2) < i32_load(i32_load(var0 + 12) + 8) else 0):
                            continue
                        break  # end loop
                i32_store(var1 + 8, 0)
            var1 = i32_load(var0 + 24)
            if (1 if i32_load(var0 + 24) == 0 else 0):
                break
            var4 = i32_load(var1 + 4)
            if (1 if i32_load(var1 + 4) == 0 else 0):
                break
            var1 = i32_load(var4 + 8)
            if (1 if i32_load(var4 + 8) == 0 else 0):
                break
            var2 = i32_load(var4)
            var7 = 0
            while True:  # loop $label15
                var10 = ((var7 | 1) << 2)
                var5 = i32_load((var2 + ((var7 | 1) << 2)))
                if i32_load((var2 + ((var7 | 1) << 2))):
                    if (1 if var5 >= 1073741823 else 0):
                        var11 = (var5 - 1073741823)
                        var1 = i32_load(9299896)
                        if (1 if i32_load(9299896) != i32_load(9299892) else 0):
                            var2 = i32_load(9299888)
                            break
                        var2 = (i32_load(9299900) + var1)
                        i32_store(9299892, (i32_load(9299900) + var1))
                        var6 = i32_load(9299888)
                        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                        if var1:
                            # Unknown: memory.copy []
                        if var6:
                            var1 = i32_load(9299896)
                        i32_store(9299888, var2)
                        i32_store(9299896, (var1 + 1))
                        i32_store((var2 + (var1 << 2)), var11)
                        break
                    var1 = i32_load(9299880)
                    if (1 if i32_load(9299880) != i32_load(9299876) else 0):
                        var2 = i32_load(9299872)
                        break
                    var2 = (i32_load(9299884) + var1)
                    i32_store(9299876, (i32_load(9299884) + var1))
                    var6 = i32_load(9299872)
                    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                    if var1:
                        # Unknown: memory.copy []
                    if var6:
                        var1 = i32_load(9299880)
                    i32_store(9299872, var2)
                    i32_store(9299880, (var1 + 1))
                    i32_store((var2 + (var1 << 2)), var5)
                    if i32_load8_u(9142916):
                        i32_store(var3 + 32, var5)
                        a_b()
                        break
                    i32_store(var3 + 24, var5)
                    i64_store(var3 + 16, -4602115869219225600)
                    i64_store(var3 + 8, 0)
                    i64_store(var3, 0)
                    a_b()
                    var2 = i32_load(var4)
                    i32_store((i32_load(var4) + var10), 0)
                    var1 = i32_load(var4 + 8)
                var7 = (var7 + 2)
                if (1 if (var7 + 2) < var1 else 0):
                    continue
                break  # end loop
            func38(i32_load(var0 + 40))
            i32_store(var0 + 40, 0)
            var8 = (var8 + 1)
            var1 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 216)
            if (1 if (var8 + 1) < i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 216) else 0):
                continue
            break  # end loop
        var9 = (var9 + 1)
        if (1 if (var9 + 1) < var1 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var3 + 96)


# ==========================================================
# $func119
# ==========================================================
def func119(var0, var1, var2, param3):
    var3 = 0
    var4 = 0
    var3 = i32_load(((i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) * 40) + 9671200) + 32)
    if i32_load(((i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) * 40) + 9671200) + 32):
        # call_indirect via table[var3]
    var3 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        break
    if (1 if i32_load(var3 + 8) < 3 else 0):
        break
    if (1 if (i32_load(i32_load(var3)) - 1) > 1 else 0):
        break
    i32_store(var3 + 8, 0)
    i32_store8(var0 + 129, 0)
    i32_store(var0 + 32, 0)
    i32_store8(var0 + 123, 0)
    if (1 if i32_load8_u(59181) == 0 else 0):
        break
    var3 = i32_load(var0 + 44)
    if (1 if i32_load(var0 + 44) == 0 else 0):
        break
    var4 = i32_load(9215884)
    if (1 if i32_load((i32_load(9215884) + (var3 << 4)) + 12) == 1 else 0):
        break
    if (1 if i32_load8_u(var0 + 125) == 7 else 0):
        break
    if i32_load((var4 + ((var3 << 4) | 4))):
        break
    var3 = (i32_load8_u(var0 + 124) << 3)
    i32_store8(var0 + 125, var1)
    if var2:
        var1 = i32_load(var0 + 44)
        if i32_load(var0 + 44):
            i32_store((i32_load(9215884) + (var1 << 4)), 0)
        i32_store(var0 + 44, 0)
    func92(var0, 0.0, 0.0)


# ==========================================================
# $func138
# ==========================================================
def func138(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var1 = (global0 - 144)
    global global0
    global0 = (global0 - 144)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    func77(var0)
    var2 = i32_load(var0 + 40)
    if i32_load8_u(9142916):
        i32_store(var1 + 128, var2)
        a_b()
        break
    i32_store(var1 + 120, var2)
    i64_store(var1 + 112, -4602115869219225600)
    i64_store(var1 + 104, 0)
    i64_store(var1 + 96, 0)
    a_b()
    var2 = i32_load(var0 + 24)
    if (1 if i32_load(var0 + 24) == 0 else 0):
        break
    var3 = i32_load(var2 + 4)
    if (1 if i32_load(var2 + 4) == 0 else 0):
        break
    if (1 if i32_load(var3 + 8) == 0 else 0):
        break
    var2 = 0
    var5 = (var1 - -64)
    while True:  # loop $label4
        var4 = i32_load((i32_load(var3) + ((var2 << 2) | 4)))
        if (1 if i32_load((i32_load(var3) + ((var2 << 2) | 4))) == 0 else 0):
            break
        if i32_load8_u(9142916):
            i32_store(var1 + 80, var4)
            a_b()
            break
        i32_store(var1 + 72, var4)
        i64_store(var5, -4602115869219225600)
        i64_store(var1 + 56, 0)
        i64_store(var1 + 48, 0)
        a_b()
        var2 = (var2 + 2)
        if (1 if (var2 + 2) < i32_load(var3 + 8) else 0):
            continue
        break  # end loop
    var3 = i32_load(var0 + 12)
    if (1 if i32_load(var0 + 12) == 0 else 0):
        break
    if (1 if i32_load(var3 + 8) == 0 else 0):
        break
    var2 = 0
    while True:  # loop $label6
        var3 = i32_load((i32_load(var3) + (var2 << 2)))
        if i32_load8_u(9142916):
            i32_store(var1 + 32, var3)
            a_b()
            break
        i32_store(var1 + 24, var3)
        i64_store(var1 + 16, -4602115869219225600)
        i64_store(var1 + 8, 0)
        i64_store(var1, 0)
        a_b()
        var2 = (var2 + 2)
        var3 = i32_load(var0 + 12)
        if (1 if (var2 + 2) < i32_load(i32_load(var0 + 12) + 8) else 0):
            continue
        break  # end loop
    global global0
    global0 = (var1 + 144)


# ==========================================================
# $func158
# ==========================================================
def func158(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    func77(var0)
    if i32_load(var0 + 40):
        var1 = i32_load(var0 + 12)
        if i32_load(var0 + 12):
            if i32_load(var1 + 8):
                while True:  # loop $label0
                    func38(i32_load((i32_load(var1) + (var2 << 2))))
                    var2 = (var2 + 2)
                    var1 = i32_load(var0 + 12)
                    if (1 if (var2 + 2) < i32_load(i32_load(var0 + 12) + 8) else 0):
                        continue
                    break  # end loop
            i32_store(var1 + 8, 0)
        var1 = i32_load(var0 + 24)
        if (1 if i32_load(var0 + 24) == 0 else 0):
            break
        var3 = i32_load(var1 + 4)
        if (1 if i32_load(var1 + 4) == 0 else 0):
            break
        var1 = i32_load(var3 + 8)
        if (1 if i32_load(var3 + 8) == 0 else 0):
            break
        var4 = i32_load(var3)
        var2 = 0
        while True:  # loop $label2
            var5 = ((var2 | 1) << 2)
            var6 = i32_load((var4 + ((var2 | 1) << 2)))
            if i32_load((var4 + ((var2 | 1) << 2))):
                func38(var6)
                var4 = i32_load(var3)
                i32_store((i32_load(var3) + var5), 0)
                var1 = i32_load(var3 + 8)
            var2 = (var2 + 2)
            if (1 if (var2 + 2) < var1 else 0):
                continue
            break  # end loop
        func38(i32_load(var0 + 40))
        i32_store(var0 + 40, 0)

