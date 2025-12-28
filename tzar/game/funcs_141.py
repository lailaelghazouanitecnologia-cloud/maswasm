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
# $func101
# ==========================================================
def func101(var0):
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
    var14 = 0
    var15 = 0.0
    var16 = 0.0
    var17 = 0.0
    var18 = 0.0
    var19 = 0.0
    var20 = 0.0
    var21 = 0.0
    var3 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    var10 = i32_load(38560)
    var11 = i32_load16_u(var0 + 114)
    var6 = i32_load16_u(var0 + 112)
    var9 = i32_load8_u(var0 + 122)
    var12 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var1 = i32_load(var0 + 12)
    if (1 if i32_load(var0 + 12) == 0 else 0):
        break
    var7 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    while True:  # loop $label3
        var4 = (i32_load(var1) + (var2 << 2))
        if (1 if i32_load((i32_load(var1) + (var2 << 2)) + 4) == 0 else 0):
            func38(i32_load(var4))
            var1 = i32_load(var0 + 12)
            var7 = (i32_load(var1 + 8) - 2)
            i32_store(i32_load(var0 + 12) + 8, (i32_load(var1 + 8) - 2))
            if (1 if var2 < var7 else 0):
                var8 = i32_load(var1)
                var4 = var2
                while True:  # loop $label2
                    var5 = (var8 + (var4 << 2))
                    i32_store((var8 + (var4 << 2)), i32_load(var5 + 8))
                    var4 = (var4 + 1)
                    var7 = i32_load(var1 + 8)
                    if (1 if (var4 + 1) < i32_load(var1 + 8) else 0):
                        continue
                    break  # end loop
            var2 = (var2 - 2)
        var2 = (var2 + 2)
        if (1 if (var2 + 2) < var7 else 0):
            continue
        break  # end loop
    if (1 if i32_load(var12 + 20) == 0 else 0):
        break
    var16 = (float(var11) * 32.0)
    var17 = (((float(var11) * 32.0) + 192.0) if (1 if var9 == var10 else 0) else var16)
    var18 = ((((float(var11) * 32.0) + 192.0) if (1 if var9 == var10 else 0) else var16) + -1.0)
    var14 = ((var9 * 404) + 9568304)
    var20 = float(var16)
    var19 = (float(var6) * 32.0)
    var21 = float((float(var6) * 32.0))
    var11 = (var3 - -64)
    var7 = 0
    while True:  # loop $label8
        var1 = i32_load((var12 + (var7 << 2)))
        if (1 if i32_load(i32_load((var12 + (var7 << 2))) + 32) == 6 else 0):
            var2 = 7
            if i32_load8_u(40588):
                break
            break
        var4 = i32_load8_u(var0 + 127)
        var2 = (i32_load8_u(var0 + 127) if var4 else (i32_load16_u(var0 + 110) + 16))
        var15 = ((((float(i32_load(9142440)) * 32.0) * float(i32_load(var14))) + var17) + 1.0)
        var9 = func244(var1)
        func120(var0, func244(var1), 0)
        var13 = i32_load(var1 + 32)
        if i32_load8_u(9142916):
            if (1 if var13 == 6 else 0):
                var15 = (((float(i32_load(9142440)) * 32.0) * float(i32_load(var14))) + var17)
            if i32_load(var1 + 20):
                var6 = i32_load8_u(var0 + 124)
                var2 = i32_load(var1 + 28)
                if (1 if i32_load(var1 + 28) == 2147483647 else 0):
                    var2 = i32_load(59152)
                    i32_store(59152, (i32_load(59152) + 1))
                    var8 = i32_load(9568052)
                    i32_store(var1 + 28, var2)
                    var5 = i32_load(var1)
                    var10 = i32_load(var1 + 4)
                    var4 = i32_load(9568048)
                    i32_store(9568048, (i32_load(9568048) + 1))
                    i32_store(((var4 << 2) + 9563952), var1)
                    i32_store(9568052, (var8 + ((var5 * (var10 + 2)) << 2)))
                    var4 = i32_load(9568056)
                    i32_store(var1 + 56, i32_load(9568056))
                    i32_store(9568056, (var4 + ((var10 * i32_load(var1)) << 2)))
            else:
            var2 = 0
            var15 = (var15 + 1.0)
            var4 = i32_load16_u(var0 + 110)
            var1 = 1
            var5 = i32_load8_u(var0 + 122)
            if (1 if i32_load8_u(var0 + 122) == i32_load(38604) else 0):
                break
            if (1 if i32_load(38608) == var5 else 0):
                break
            if (1 if i32_load(38612) == var5 else 0):
                break
            if (1 if i32_load(38616) == var5 else 0):
                break
            if (1 if i32_load(38624) == var5 else 0):
                break
            if (1 if i32_load(38628) == var5 else 0):
                break
            if (1 if i32_load(38632) == var5 else 0):
                break
            var1 = (1 if i32_load(39056) == var5 else 0)
            if (1 if var15 > 0.0 else 0):
                var15 = (((var15 * 0.5) / float((i32_load(9142440) * 96))) + 0.25)
            i32_store(var3 + 76, var9)
            i32_store(var3 + 72, 0)
            i32_store(var11, (2130706431 if (1 if var13 == 6 else 0) else 0))
            i64_store(var3 + 56, 0)
            i32_store(var3 + 52, (0 - var1))
            i32_store(var3 + 48, var2)
            i64_store(var3 + 40, 0)
            i64_store(var3 + 32, 0)
            i64_store(var3 + 24, 0)
            f64_store(var3 + 16, float(var15))
            i32_store(var3 + 68, ((var4 << 16) | 65535))
            f64_store(var3 + 8, var20)
            f64_store(var3, var21)
            a_b()
            break
        var5 = (1 if var13 == 22 else 0)
        var4 = i32_load8_u(var0 + 124)
        var8 = 1
        var6 = i32_load8_u(var0 + 122)
        if (1 if i32_load8_u(var0 + 122) == i32_load(38604) else 0):
            break
        if (1 if i32_load(38608) == var6 else 0):
            break
        if (1 if i32_load(38612) == var6 else 0):
            break
        if (1 if i32_load(38616) == var6 else 0):
            break
        if (1 if i32_load(38624) == var6 else 0):
            break
        if (1 if i32_load(38628) == var6 else 0):
            break
        if (1 if i32_load(38632) == var6 else 0):
            break
        var8 = (1 if i32_load(39056) == var6 else 0)
        var7 = (var7 + 1)
        if (1 if (var7 + 1) < i32_load(var12 + 20) else 0):
            continue
        break  # end loop
    global global0
    global0 = (var3 + 80)
    return func40(var19, var16, var15, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, var1, var2, var9, var5, var4, var8, 0.0)


# ==========================================================
# $func131
# ==========================================================
def func131(var0, var1, var2):
    var3 = 0
    var4 = 0.0
    if (var0 & 3):
    else:
        func429()
        if (1 if global6 == 0 else 0):
            var4 = a_f()
            var2 = (var4 + var2)
            if (1 if a_f() > (var4 + var2) else 0):
                break
            while True:  # loop $label2
                var3 = 0
                if (1 if (var0 if (1 if var0 == var3 else 0) else 0) == 0 else 0):
                    break
                func429()
                if (1 if var1 == i32_atomic_load(var0) else 0):
                    if (1 if a_f() > var2 else 0):
                        break
                    continue
                break  # end loop
            break
            return -73
        var3 = (1 if var2 != inf else 0)
        var2 = ((var2 * 1000.0) * 1000.0)
        if (1 if abs(((var2 * 1000.0) * 1000.0)) < 9.223372036854776e+18 else 0):
            break
        var0 = (-9223372036854775808 if var3 else -1)
    return (var0 if (1 if var0 == 1 else 0) else (var1 if (1 if (-9223372036854775808 if var3 else -1) == 2 else 0) else int(var2)))


# ==========================================================
# $Ya
# Export: Ya
# ==========================================================
def Ya(var0):
    """Export: Ya"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var1 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    if (1 if i32_load(9213808) != 1 else 0):
        break
    var2 = i32_load(9671128)
    var3 = i32_load(9173808)
    if (1 if (0 if var0 else i32_load8_u(9147141)) == 0 else 0):
        var3 = (var2 + (var3 * 132))
        var2 = i32_load((var2 + (var3 * 132)) + 16)
        if (1 if i32_load((var2 + (var3 * 132)) + 16) == 0 else 0):
            break
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        var2 = 0
        a_b()
        i32_store8(9147141, 1)
        if (1 if var0 == 0 else 0):
            i32_store(9143000, 0)
        i32_store(9671120, 0)
        var0 = i32_load(9147120)
        if (1 if i32_load(9147120) == 0 else 0):
            break
        while True:  # loop $label2
            var0 = ((i32_load(9143000) * var0) + var2)
            var4 = i32_load(var3 + 16)
            if (1 if ((i32_load(9143000) * var0) + var2) >= i32_load(i32_load(var3 + 16) + 8) else 0):
                break
            i32_store(9671120, (i32_load(9671120) + 1))
            var0 = i32_load(((i32_load8_u((i32_load(9671128) + (i32_load((i32_load(var4) + (var0 << 2))) * 132)) + 122) * 404) + 9568096) + 144)
            i64_store(var1 + 32, 1)
            i64_store(var1 + 40, 0)
            i64_store(var1 + 48, 0)
            i64_store(var1 + 56, 4294967295)
            i64_store(var1 + 24, 1)
            i32_store(var1 + 20, (0 - var0))
            i32_store(var1 + 16, var2)
            a_b()
            var2 = (var2 + 1)
            var0 = i32_load(9147120)
            if (1 if (var2 + 1) < i32_load(9147120) else 0):
                continue
            break  # end loop
        var0 = i32_load(i32_load(var3 + 16) + 8)
        i32_store(var1, i32_load(9143000))
        i32_store(var1 + 4, var0)
        a_b()
        break
    i32_store8(9147141, 0)
    i32_store(9143000, 0)
    if (1 if i32_load((var2 + (var3 * 132)) + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var2 + (var3 * 132)) + 28) else 0):
            break
    global global0
    global0 = (var1 - -64)


# ==========================================================
# $func148
# ==========================================================
def func148(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var4 = i32_load(9671128)
    var5 = (i32_load(9671128) + (var0 * 132))
    var3 = i32_load(var1)
    if (1 if i32_load(var1) <= 2147483646 else 0):
        i32_store(var5 + 52, var3)
    var3 = i32_load(var1 + 4)
    if (1 if i32_load(var1 + 4) <= 2147483646 else 0):
        i32_store((var4 + (var0 * 132)) + 60, var3)
    var3 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) > 2147483646 else 0):
        break
    var7 = (var4 + (var0 * 132))
    i32_store((var4 + (var0 * 132)) + 64, var3)
    if (1 if i32_load(var1 + 8) > 2147483646 else 0):
        break
    i32_store(var7 + 68, i32_load(var1 + 12))
    var7 = i32_load(var5 + 76)
    var3 = i32_load(var5 + 76)
    var6 = i32_load(var1 + 16)
    if (1 if i32_load(var1 + 16) > 2147483646 else 0):
        break
    i32_store((var4 + (var0 * 132)) + 72, var6)
    if (1 if i32_load(var1 + 16) > 2147483646 else 0):
        break
    var3 = i32_load(var1 + 20)
    i32_store(var5 + 76, i32_load(var1 + 20))
    var1 = i32_load(var1 + 24)
    if (1 if i32_load(var1 + 24) <= 2147483646 else 0):
        i32_store((var4 + (var0 * 132)) + 84, var1)
    var6 = ((i32_load8_u((var4 + (var0 * 132)) + 122) * 404) + 9568096)
    var1 = i32_load(((i32_load8_u((var4 + (var0 * 132)) + 122) * 404) + 9568096) + 264)
    if (1 if i32_load(var6 + 92) == 0 else 0):
        if (1 if var1 == 2 else 0):
            break
        i32_store((var4 + (var0 * 132)) + 52, 0)
    if (1 if var1 != 1 else 0):
        break
    var3 = 0
    var1 = (var4 + (var0 * 132))
    i32_store((var4 + (var0 * 132)) + 72, 0)
    i32_store(var1 + 60, 0)
    i32_store(var5 + 76, 0)
    i32_store(var1 + 84, 0)
    var6 = (var4 + (var0 * 132))
    var1 = i32_load((var4 + (var0 * 132)) + 64)
    if (1 if i32_load((var4 + (var0 * 132)) + 64) == 0 else 0):
        i32_store((var6 - -64), -1)
        var1 = -1
    if var2:
        var2 = (var4 + (var0 * 132))
        i32_store((var4 + (var0 * 132)) + 68, var1)
        var3 = i32_load(var2 + 72)
        i32_store(var5 + 76, i32_load(var2 + 72))
    if (1 if var3 == 0 else 0):
        break
    if var7:
        break


# ==========================================================
# $func152
# ==========================================================
def func152():
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var4 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if i32_load8_u(9142917):
        break
    if (1 if i32_load(9568048) == 0 else 0):
        break
    var1 = i32_load(9140308)
    var3 = i32_load(9568052)
    var0 = (i32_load(59156) << 2)
    var2 = (i32_load(9568052) % (i32_load(59156) << 2))
    if (i32_load(9568052) % (i32_load(59156) << 2)):
        var3 = ((var3 - var2) + var0)
        i32_store(9568052, ((var3 - var2) + var0))
    i32_store(9140308, (((var3 & 0xFFFFFFFF) >> 2) + var1))
    func231(var4)
    i32_store(var4 + 12, 1)
    var0 = func26(16)
    var2 = i32_load(9568048)
    i32_store(var0 + 4, var1)
    i32_store(var0, var2)
    i32_store(var0 + 8, i32_load(9568052))
    i32_store(var0 + 12, func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2))))
    if (1 if var2 == 0 else 0):
        break
    var3 = 0
    if (1 if var2 >= 4 else 0):
        var6 = (var2 & -4)
        while True:  # loop $label2
            var1 = (var3 << 2)
            i32_store(((var3 << 2) + i32_load(var0 + 12)), i32_load((var1 + 9563952)))
            var5 = (var1 | 4)
            i32_store(((var1 | 4) + i32_load(var0 + 12)), i32_load((var5 + 9563952)))
            var5 = (var1 | 8)
            i32_store(((var1 | 8) + i32_load(var0 + 12)), i32_load((var5 + 9563952)))
            var1 = (var1 | 12)
            i32_store(((var1 | 12) + i32_load(var0 + 12)), i32_load((var1 + 9563952)))
            var3 = (var3 + 4)
            var7 = (var7 + 4)
            if (1 if (var7 + 4) != var6 else 0):
                continue
            break  # end loop
    var2 = (var2 & 3)
    if (1 if (var2 & 3) == 0 else 0):
        break
    while True:  # loop $label3
        var1 = (var3 << 2)
        i32_store(((var3 << 2) + i32_load(var0 + 12)), i32_load((var1 + 9563952)))
        var3 = (var3 + 1)
        var8 = (var8 + 1)
        if (1 if (var8 + 1) != var2 else 0):
            continue
        break  # end loop
    func186((var4 + 44), var4, 65, var0)
    i32_store(9568052, 0)
    i32_store(9568048, 0)
    global global0
    global0 = (var4 + 48)

