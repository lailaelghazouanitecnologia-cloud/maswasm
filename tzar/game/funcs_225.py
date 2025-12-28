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
# $func849
# ==========================================================
def func849(var0, var1):
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
    var15 = 0
    var16 = 0
    var17 = 0
    var18 = 0
    var19 = 0
    var20 = 0
    var21 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if i32_load8_u(9147152):
        break
    var17 = i32_load(9561692)
    var2 = i32_load(9671128)
    var4 = (var0 * 132)
    var0 = (i32_load(9671128) + (var0 * 132))
    var10 = i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110)
    var11 = (i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110) * 286704))
    var18 = i32_load8_u(var0 + 122)
    var19 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 68)
    var0 = ((i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 68) & 0xFFFFFFFF) >> 1)
    if (1 if i32_load(9671152) != var18 else 0):
        break
    var0 = ((i32_load(var11 + 283848) // 2) + var0)
    var7 = i32_load(9671136)
    var8 = ((func88(var11) & 0xFFFFFFFF) // 200)
    var3 = i32_load(9671132)
    if (1 if (i32_load(9671136) + ((func88(var11) & 0xFFFFFFFF) // 200)) < i32_load(9671132) else 0):
        break
    var8 = (i32_load(9671140) + (var3 + var8))
    i32_store(9671132, (i32_load(9671140) + (var3 + var8)))
    var2 = func228(var2, var8, var7)
    i32_store(9671128, func228(var2, var8, var7))
    var2 = (var2 + var4)
    var20 = i32_load16_u((var2 + var4) + 112)
    var8 = i32_load16_u(var2 + 114)
    var9 = ((var0 & 0xFFFFFFFF) // 100)
    var2 = (((var0 & 0xFFFFFFFF) // 100) * -100)
    var4 = i32_load(9671132)
    var7 = i32_load(9671136)
    if (1 if i32_load(9671132) <= (i32_load(9671136) + var9) else 0):
        var4 = (i32_load(9671140) + (var4 + var9))
        i32_store(9671132, (i32_load(9671140) + (var4 + var9)))
        i32_store(9671128, func228(i32_load(9671128), var4, var7))
    var13 = (100 if (1 if var0 >= 100 else 0) else 0)
    var0 = (var0 + var2)
    var7 = var8
    while True:  # loop $label9
        var6 = (var8 - var12)
        var2 = ((var12 << 1) | 1)
        var14 = (((var8 - var12) + ((var12 << 1) | 1)) - 1)
        var4 = (var20 - var12)
        var21 = (var2 + (var20 - var12))
        var15 = ((var2 + (var20 - var12)) - 1)
        var2 = var4
        while True:  # loop $label5
            var3 = i32_load(9142440)
            if (1 if var6 >= i32_load(9142440) else 0):
                break
            if (1 if (var2 | var6) < 0 else 0):
                break
            if (1 if var2 >= var3 else 0):
                break
            var3 = func34(i32_load(39064), 0, var2, var6, 0, 1)
            if func34(i32_load(39064), 0, var2, var6, 0, 1):
                var16 = (i32_load(9671128) + (var3 * 132))
                i64_store((i32_load(9671128) + (var3 * 132)) + 64, 2147483648500)
                i32_store(var16 + 52, (var0 + var13))
                var0 = 0
            var5 = (var5 + (1 if var3 != 0 else 0))
            if (1 if (var5 + (1 if var3 != 0 else 0)) >= var9 else 0):
                break
            var3 = i32_load(9142440)
            if (1 if var3 <= var14 else 0):
                break
            if (1 if (var2 | var14) < 0 else 0):
                break
            if (1 if var2 >= var3 else 0):
                break
            var3 = func34(i32_load(39064), 0, var2, var14, 0, 1)
            if func34(i32_load(39064), 0, var2, var14, 0, 1):
                var16 = (i32_load(9671128) + (var3 * 132))
                i64_store((i32_load(9671128) + (var3 * 132)) + 64, 2147483648500)
                i32_store(var16 + 52, (var0 + var13))
                var0 = 0
            var5 = (var5 + (1 if var3 != 0 else 0))
            if (1 if (var5 + (1 if var3 != 0 else 0)) >= var9 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < var21 else 0):
                continue
            break  # end loop
        var2 = (var6 + 1)
        if (1 if var14 > (var6 + 1) else 0):
            while True:  # loop $label8
                var3 = i32_load(9142440)
                if (1 if var2 >= i32_load(9142440) else 0):
                    break
                if (1 if (var2 | var4) < 0 else 0):
                    break
                if (1 if var3 <= var4 else 0):
                    break
                var3 = func34(i32_load(39064), 0, var4, var2, 0, 1)
                if func34(i32_load(39064), 0, var4, var2, 0, 1):
                    var6 = (i32_load(9671128) + (var3 * 132))
                    i64_store((i32_load(9671128) + (var3 * 132)) + 64, 2147483648500)
                    i32_store(var6 + 52, (var0 + var13))
                    var0 = 0
                var5 = (var5 + (1 if var3 != 0 else 0))
                if (1 if (var5 + (1 if var3 != 0 else 0)) >= var9 else 0):
                    break
                var3 = i32_load(9142440)
                if (1 if var2 >= var3 else 0):
                    break
                if (1 if (var2 | var15) < 0 else 0):
                    break
                if (1 if var3 <= var15 else 0):
                    break
                var3 = func34(i32_load(39064), 0, var15, var2, 0, 1)
                if func34(i32_load(39064), 0, var15, var2, 0, 1):
                    var6 = (i32_load(9671128) + (var3 * 132))
                    i64_store((i32_load(9671128) + (var3 * 132)) + 64, 2147483648500)
                    i32_store(var6 + 52, (var0 + var13))
                    var0 = 0
                var5 = (var5 + (1 if var3 != 0 else 0))
                if (1 if (var5 + (1 if var3 != 0 else 0)) >= var9 else 0):
                    break
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != var7 else 0):
                    continue
                break  # end loop
        var7 = (var7 + 1)
        var12 = (var12 + 1)
        if (1 if (var12 + 1) != 512 else 0):
            continue
        break  # end loop
    i32_store(var11 + 283956, (i32_load(var11 + 283956) + var19))
    if (1 if var10 == 0 else 0):
        break
    if (1 if i32_load(9671152) != var18 else 0):
        break
    if (1 if i32_load(9671136) >= 4 else 0):
        var0 = 3
        while True:  # loop $label11
            var2 = (i32_load(9671128) + (var0 * 132))
            if (1 if i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110) != var10 else 0):
                break
            if i32_load8_u(((i32_load8_u(var2 + 122) * 404) + 9568096) + 332):
                func78(var2, 0, 0, 1)
                break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < i32_load(9671136) else 0):
                continue
            break  # end loop
    var0 = (var17 + (var10 * 286704))
    i32_store((var17 + (var10 * 286704)) + 283976, 0)
    i32_store(var0 + 283848, 0)
    var2 = i32_load(var0 + 281788)
    if i32_load(var0 + 281788):
        i32_store(var2 + 8, 0)
    var0 = i32_load(var0 + 281792)
    if i32_load(var0 + 281792):
        i32_store(var0 + 8, 0)
    var0 = (var17 + (var10 * 286704))
    var2 = i32_load((var17 + (var10 * 286704)) + 281796)
    if i32_load((var17 + (var10 * 286704)) + 281796):
        i32_store(var2 + 8, 0)
    var2 = i32_load(var0 + 284628)
    var0 = i32_load(var0 + 284616)
    i32_store(var1 + 4, var11)
    i32_store(var1, 118)
    i32_store(var1 + 8, (var0 if var0 else var2))
    a_b()
    if (1 if i32_load(9142872) != var10 else 0):
        break
    a_b()
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $func855
# ==========================================================
def func855(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    if var2:
        var4 = i32_load(var0)
        var3 = i32_load(9671128)
        var0 = 0
        while True:  # loop $label0
            var5 = (var3 + (i32_load((var1 + (var0 << 2))) * 132))
            if (1 if i32_load8_u((var3 + (i32_load((var1 + (var0 << 2))) * 132)) + 125) != 3 else 0):
                var3 = i32_load(9671128)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var2 else 0):
                continue
            break  # end loop


# ==========================================================
# $func858
# ==========================================================
def func858(var0, var1):
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
    var15 = 0
    var4 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var1 = i32_load(9671128)
    if (1 if i32_load(9142848) < (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        func29((var1 + (var0 * 132)), 1)
        break
    var2 = (var0 * 132)
    var3 = (var1 + (var0 * 132))
    if (1 if i32_load8_u((var1 + (var0 * 132)) + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var3 + 128) == 0 else 0):
        break
    var1 = (var1 + (var0 * 132))
    i32_store8((var1 + (var0 * 132)) + 127, 0)
    var5 = i32_load(var1 + 40)
    if (1 if i32_load(var1 + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var4 + 20, var5)
        i32_store(var4 + 16, 0)
        a_b()
        break
    var1 = i32_load16_u(var1 + 110)
    i32_store(var4 + 4, var5)
    i32_store(var4, (var1 + 16))
    a_b()
    i32_store8(var3 + 128, 0)
    var1 = i32_load(9671128)
    var2 = (var1 + var2)
    var9 = i32_load16_u((var1 + var2) + 110)
    var3 = i32_load(9561692)
    var1 = i32_load16_u(var2 + 116)
    var5 = i32_load16_u(var2 + 118)
    var10 = (var1 - 2)
    var2 = (i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704))
    var1 = i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284272))
    var14 = (var10 + i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284272)))
    if (1 if (var1 - 2) >= (var10 + i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284272))) else 0):
        break
    var5 = (var5 - 2)
    var15 = (var1 + var5)
    if (1 if (var5 - 2) >= (var1 + var5) else 0):
        break
    var12 = i32_load((var2 + 284276))
    var1 = (var3 + (var9 * 286704))
    var7 = ((var3 + (var9 * 286704)) + 281768)
    var13 = (var1 + 283908)
    var8 = (var1 + 281764)
    var6 = i32_load(9142440)
    while True:  # loop $label7
        var3 = (var10 + 1)
        var1 = var5
        while True:  # loop $label6
            var2 = var1
            var1 = (var1 + 1)
            if (1 if var2 >= var6 else 0):
                break
            if (1 if (var2 | var10) < 0 else 0):
                break
            if (1 if var6 <= var10 else 0):
                break
            var11 = i32_load(9142840)
            var9 = (var6 + 2)
            var2 = i32_load((i32_load(9142840) + ((var3 + (var1 * (var6 + 2))) << 2)))
            if (1 if i32_load((i32_load(9142840) + ((var3 + (var1 * (var6 + 2))) << 2))) <= 2 else 0):
                break
            if (1 if var0 == var2 else 0):
                break
            var2 = (i32_load(9671128) + (var2 * 132))
            if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122) * 404) + 9568096) + 344) == 0 else 0):
                break
            if (1 if ((i32_load8_u(var2 + 125) - 9) & 255) < 2 else 0):
                break
            i32_store(var8, (i32_load(var8) + 1))
            if i32_load8_u((i32_load(9143004) + (i32_load(var13) + (i32_load(9142892) * i32_load16_u(var2 + 110))))):
                i32_store(var7, (i32_load(var7) + i32_load(var2 + 64)))
            func204(var2, var12)
            var6 = i32_load(9142440)
            var9 = (i32_load(9142440) + 2)
            var11 = i32_load(9142840)
            var2 = i32_load((var11 + ((var3 + ((var1 + var9) * var9)) << 2)))
            if (1 if i32_load((var11 + ((var3 + ((var1 + var9) * var9)) << 2))) < 3 else 0):
                break
            if (1 if var0 == var2 else 0):
                break
            var2 = (i32_load(9671128) + (var2 * 132))
            if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122) * 404) + 9568096) + 344) == 0 else 0):
                break
            if (1 if ((i32_load8_u(var2 + 125) - 9) & 255) < 2 else 0):
                break
            i32_store(var8, (i32_load(var8) + 1))
            if i32_load8_u((i32_load(9143004) + (i32_load(var13) + (i32_load(9142892) * i32_load16_u(var2 + 110))))):
                i32_store(var7, (i32_load(var7) + i32_load(var2 + 64)))
            func204(var2, var12)
            var11 = i32_load(9142840)
            var6 = i32_load(9142440)
            var2 = (var6 + 2)
            var2 = i32_load((var11 + ((var3 + ((var1 + ((var6 + 2) << 1)) * var2)) << 2)))
            if (1 if i32_load((var11 + ((var3 + ((var1 + ((var6 + 2) << 1)) * var2)) << 2))) < 3 else 0):
                break
            if (1 if var0 == var2 else 0):
                break
            var2 = (i32_load(9671128) + (var2 * 132))
            if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122) * 404) + 9568096) + 344) == 0 else 0):
                break
            if (1 if ((i32_load8_u(var2 + 125) - 9) & 255) < 2 else 0):
                break
            i32_store(var8, (i32_load(var8) + 1))
            if i32_load8_u((i32_load(9143004) + (i32_load(var13) + (i32_load(9142892) * i32_load16_u(var2 + 110))))):
                i32_store(var7, (i32_load(var7) + i32_load(var2 + 64)))
            func204(var2, var12)
            var6 = i32_load(9142440)
            if (1 if var1 != var15 else 0):
                continue
            break  # end loop
        var10 = var3
        if (1 if var3 != var14 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var4 + 32)


# ==========================================================
# $func889
# ==========================================================
def func889(var0, var1):
    var2 = 0
    var3 = 0
    if (1 if i32_load8_u(var1 + 125) == 3 else 0):
        break
    var0 = i32_load(var0 + 36)
    if (1 if i32_load(var0 + 36) != 2147483646 else 0):
        break
    var0 = 0
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) == 0 else 0):
        break
    var3 = i32_load(9142420)
    while True:  # loop $label2
        if i32_load((var3 + (var0 << 2))):
            break
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var2 else 0):
            continue
        break  # end loop
    var0 = 2147483646
    if (1 if var2 >= 2147483647 else 0):
        break
    break
    if (1 if var0 == 2147483647 else 0):
        i32_store8(var1 + 126, 2)
        var0 = 0
        if (1 if i32_load(9142892) == 0 else 0):
            break
        var2 = 0
        if i32_load16_u(var1 + 110):
            break
        break
    if (1 if var0 >= i32_load(9142892) else 0):
        break
    if (1 if var0 == i32_load16_u(var1 + 110) else 0):
        break
    var2 = 0
    if (1 if i32_load8_u(var1 + 126) != 2 else 0):
        break
    if i32_load8_u(((i32_load8_u(var1 + 122) * 404) + 9568096) + 332):
        break
    i32_store8(var1 + 126, 0)
    var2 = 1
    func78(var1, var0, 0, 1)
    if (1 if i32_load8_u(var1 + 126) == 2 else 0):
        if (1 if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 264) != 2 else 0):
        func29(var1, 1)
    if (1 if var2 == 0 else 0):
        break
    func156(0  # stack underflow, var1, 500)

