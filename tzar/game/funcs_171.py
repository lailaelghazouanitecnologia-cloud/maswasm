"""
Auto-generated from WAT. Contains 1 functions.
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
# $func324
# ==========================================================
def func324():
    var0 = 0
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
    var15 = 0
    var16 = 0
    var17 = 0
    var18 = 0
    var19 = 0
    var20 = 0.0
    var21 = 0.0
    var22 = 0.0
    var23 = 0.0
    var24 = 0.0
    var25 = 0
    var26 = 0
    var27 = 0.0
    var9 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    i32_store(9143000, 0)
    var1 = i32_load(59144)
    var2 = i32_load(59136)
    var0 = i32_load(59140)
    var4 = i32_load(59132)
    var6 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var6 * 132)))
        i32_store(9213820, 0)
    if (1 if i32_load8_u(9163792) == 0 else 0):
        func45()
    if (1 if i32_load8_u(9147152) == 0 else 0):
        func52((207 if i32_load8_u(9143020) else 0), 0)
        a_b()
    if (1 if ((var4 - var2) if (1 if var2 < var4 else 0) else (var2 - var4)) > 12 else 0):
        break
    if (1 if ((var0 - var1) if (1 if var0 > var1 else 0) else (var1 - var0)) > 12 else 0):
        break
    var2 = func141(var4, var0)
    if (1 if (1 if (a_f() - f64_load(9681904)) < 500.0 else 0) == 0 else 0):
        break
    if (1 if var2 < 3 else 0):
        break
    var1 = (i32_load(9681912) - var4)
    var1 = (i32_load(9681916) - var0)
    if (1 if ((((i32_load(9681912) - var4) * var1) + ((i32_load(9681916) - var0) * var1)) - 1) > 100 else 0):
        break
    var6 = i32_load(9671128)
    var1 = (i32_load(9671128) + (var2 * 132))
    if (1 if i32_load8_u(9147152) == 0 else 0):
        if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var1 + 110))))) == 0 else 0):
            break
        var5 = (var6 + (var2 * 132))
        if (1 if i32_load((i32_load(9215884) + (i32_load((var6 + (var2 * 132)) + 44) << 4)) + 4) == 20 else 0):
            break
        if (1 if i32_load8_u(var5 + 127) == 6 else 0):
            break
        if i32_load8_u(9163793):
        else:
        var15 = -1
        var2 = (var6 + (var2 * 132))
        var1 = i32_load8_u((var6 + (var2 * 132)) + 125)
        var10 = i32_load8_u(var2 + 122)
        if (1 if i32_load8_u(9163792) == 0 else 0):
            func45()
        var20 = f32_load(40616)
        var21 = float(i32_load(9142860))
        var22 = f32_load(9671164)
        var23 = ((f32_load(40616) * float(i32_load(9142860))) / f32_load(9671164))
        var24 = math.ceil(((((f32_load(40616) * float(i32_load(9142860))) / f32_load(9671164)) + 32.0) * 0.03125))
        if (1 if abs(math.ceil(((((f32_load(40616) * float(i32_load(9142860))) / f32_load(9671164)) + 32.0) * 0.03125))) < 2147483650.0 else 0):
            break
        var0 = -2147483648
        var21 = ((((var21 - var23) * 0.5) + float(i32_load(9142956))) * 0.03125)
        if (1 if abs(((((var21 - var23) * 0.5) + float(i32_load(9142956))) * 0.03125)) < 2147483650.0 else 0):
            break
        var2 = -2147483648
        var20 = float(i32_load(9142856))
        var21 = ((var20 * float(i32_load(9142856))) / var22)
        var22 = math.ceil(((((var20 * float(i32_load(9142856))) / var22) + 32.0) * 0.03125))
        if (1 if abs(math.ceil(((((var20 * float(i32_load(9142856))) / var22) + 32.0) * 0.03125))) < 2147483650.0 else 0):
            break
        var6 = -2147483648
        var20 = ((((var20 - var21) * 0.5) + float(i32_load(9142952))) * 0.03125)
        if (1 if abs(((((var20 - var21) * 0.5) + float(i32_load(9142952))) * 0.03125)) < 2147483650.0 else 0):
            break
        var4 = -2147483648
        if (1 if var6 <= 0 else 0):
            break
        if (1 if var0 <= 0 else 0):
            break
        var13 = ((1 if var1 == 4 else 0) | (1 if var1 == 14 else 0))
        var16 = (var0 + var2)
        var17 = (var4 + var6)
        var18 = ((var10 * 404) + 9568360)
        var3 = i32_load(9142440)
        while True:  # loop $label20
            var6 = (var4 + 1)
            var0 = var2
            while True:  # loop $label19
                if (1 if (var0 | var4) < 0 else 0):
                    break
                if (1 if var3 <= var4 else 0):
                    break
                if (1 if var0 < var3 else 0):
                    break
                break
                var1 = 0
                var14 = (var0 + 1)
                var19 = (var4 if (1 if var0 < var4 else 0) else var0)
                if (1 if (var4 if (1 if var0 < var4 else 0) else var0) >= var3 else 0):
                    break
                while True:  # loop $label18
                    if (1 if var3 <= var19 else 0):
                        break
                    var5 = (var3 + 2)
                    var5 = i32_load((i32_load(9142840) + ((var6 + ((var14 + ((var3 + 2) * var1)) * var5)) << 2)))
                    if (1 if i32_load((i32_load(9142840) + ((var6 + ((var14 + ((var3 + 2) * var1)) * var5)) << 2))) < 3 else 0):
                        break
                    var7 = i32_load(i32_load(9142424) + 48)
                    var8 = i32_load8_u(9147152)
                    if (1 if (0 if i32_load8_u(9147152) else i32_load(i32_load(9142424) + 48)) == 0 else 0):
                        var5 = (i32_load(9671128) + (var5 * 132))
                        if (1 if var8 == 0 else 0):
                            break
                        break
                    var8 = i32_load16_u((i32_load(9147376) + (((var0 * var3) + var4) << 1)))
                    if (1 if var7 != 2 else 0):
                        if var8:
                            break
                        break
                    if (1 if var8 < 2 else 0):
                        break
                    var5 = (i32_load(9671128) + (var5 * 132))
                    if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var5 + 110))))) == 0 else 0):
                        break
                    if (1 if i32_load((i32_load(9215884) + (i32_load(var5 + 44) << 4)) + 4) == 20 else 0):
                        break
                    if (1 if i32_load8_u(var5 + 127) == 6 else 0):
                        break
                    var7 = i32_load8_u(var5 + 125)
                    var8 = ((1 if i32_load8_u(var5 + 125) == 4 else 0) | (1 if var7 == 14 else 0))
                    if (1 if (var13 & ((1 if i32_load8_u(var5 + 125) == 4 else 0) | (1 if var7 == 14 else 0))) == 0 else 0):
                        if (var8 | var13):
                            break
                        if (1 if var7 != 5 else 0):
                            break
                        break
                    if (1 if var7 == 5 else 0):
                        break
                    var8 = i32_load8_u(var5 + 122)
                    var11 = i32_load8_u(9163793)
                    var12 = i32_load8_u(9163794)
                    if i32_load8_u(9163794):
                        break
                    if var11:
                        break
                    if (1 if var8 == var10 else 0):
                        break
                    if (1 if var12 == 0 else 0):
                        break
                    var12 = ((var8 * 404) + 9568096)
                    if i32_load(((var8 * 404) + 9568096) + 264):
                        break
                    if (1 if i32_load(var12 + 268) == 1 else 0):
                        break
                    if (1 if i32_load(var12 + 92) == 0 else 0):
                        break
                    if (1 if i32_load(38456) == var8 else 0):
                        break
                    if (1 if i32_load(38764) == var8 else 0):
                        break
                    if (1 if var7 != 8 else 0):
                        break
                    if (1 if var11 == 0 else 0):
                        break
                    if (1 if func287(var5) != var15 else 0):
                        break
                    if (1 if var8 != var10 else 0):
                        break
                    if (1 if i32_load(var18) == 1 else 0):
                        break
                    func44(var5, 0)
                    var3 = i32_load(9142440)
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != 3 else 0):
                        continue
                    break  # end loop
                var0 = var14
                if (1 if (var0 + 1) > var14 else 0):
                    continue
                break  # end loop
            var4 = var6
            if (1 if var6 < var17 else 0):
                continue
            break  # end loop
        break
    var4 = i32_load16_u(var1 + 110)
    var6 = i32_load8_u(var1 + 126)
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var0 = i32_load(var1 + 24)
    if (1 if i32_load(var1 + 24) == 0 else 0):
        break
    var0 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) == 0 else 0):
        break
    var5 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) == 0 else 0):
        break
    i32_store(var2 + 4, i32_load(var0))
    i32_store(var2, var5)
    a_b()
    break
    a_b()
    global global0
    global0 = (var2 + 16)
    var2 = i32_load(var1 + 52)
    var25 = i64_load(var1 + 64)
    var0 = i32_load(var1 + 60)
    var26 = i64_load(var1 + 72)
    var5 = i32_load(var1 + 84)
    var8 = i32_load8_u(var1 + 122)
    var3 = i32_load(var1 + 28)
    i32_store(var9 + 36, (2147483647 if (1 if var6 == 2 else 0) else var4))
    i32_store(var9 + 32, var3)
    i32_store(var9 + 28, var8)
    i32_store(var9 + 24, var5)
    i64_store(var9 + 16, var26)
    i32_store(var9 + 4, var0)
    i64_store(var9 + 8, var25)
    i32_store(var9, var2)
    func44(var1, 0)
    break
    var2 = (var2 // 32)
    var4 = (var4 // 32)
    var6 = ((var2 // 32) if (1 if var2 < var4 else 0) else (var4 // 32))
    var5 = (((var2 // 32) if (1 if var2 < var4 else 0) else (var4 // 32)) if (1 if var6 > 0 else 0) else 0)
    var2 = (var2 if (1 if var2 > var4 else 0) else var4)
    var4 = i32_load(9142440)
    var6 = (i32_load(9142440) - 1)
    var13 = ((var2 if (1 if var2 > var4 else 0) else var4) if (1 if var2 < var4 else 0) else (i32_load(9142440) - 1))
    if (1 if (((var2 // 32) if (1 if var2 < var4 else 0) else (var4 // 32)) if (1 if var6 > 0 else 0) else 0) > ((var2 if (1 if var2 > var4 else 0) else var4) if (1 if var2 < var4 else 0) else (i32_load(9142440) - 1)) else 0):
        break
    var1 = (var1 // 32)
    var2 = (var0 // 32)
    var0 = ((var1 // 32) if (1 if var1 < var2 else 0) else (var0 // 32))
    var8 = (((var1 // 32) if (1 if var1 < var2 else 0) else (var0 // 32)) if (1 if var0 > 0 else 0) else 0)
    var1 = (var1 if (1 if var1 > var2 else 0) else var2)
    var1 = ((var1 if (1 if var1 > var2 else 0) else var2) if (1 if var1 < var4 else 0) else var6)
    if (1 if (((var1 // 32) if (1 if var1 < var2 else 0) else (var0 // 32)) if (1 if var0 > 0 else 0) else 0) > ((var1 if (1 if var1 > var2 else 0) else var2) if (1 if var1 < var4 else 0) else var6) else 0):
        break
    var14 = (var1 + 1)
    var4 = 0
    while True:  # loop $label34
        var2 = var5
        while True:  # loop $label33
            var6 = (var2 + 1)
            var1 = var8
            while True:  # loop $label32
                var3 = i32_load(9142440)
                var0 = var1
                if (1 if ((1 if i32_load(9142440) > var1 else 0) & (1 if var2 < var3 else 0)) == 0 else 0):
                    var1 = (var0 + 1)
                    break
                var1 = (var0 + 1)
                var7 = (var3 + 2)
                var7 = i32_load((i32_load(9142840) + ((var6 + (((var0 + 1) + ((var3 + 2) * var4)) * var7)) << 2)))
                if (1 if i32_load((i32_load(9142840) + ((var6 + (((var0 + 1) + ((var3 + 2) * var4)) * var7)) << 2))) < 3 else 0):
                    break
                var10 = i32_load8_u(9147152)
                var11 = i32_load(i32_load(9142424) + 48)
                if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
                    break
                if var10:
                    break
                var0 = i32_load16_u((i32_load(9147376) + (((var0 * var3) + var2) << 1)))
                if (1 if var11 == 2 else 0):
                    if (1 if var0 > 1 else 0):
                        break
                    break
                if (1 if var0 == 0 else 0):
                    break
                var3 = (i32_load(9671128) + (var7 * 132))
                break
                var3 = (i32_load(9671128) + (var7 * 132))
                if var10:
                    break
                if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var3 + 110))))) == 0 else 0):
                    break
                if (1 if i32_load((i32_load(9215884) + (i32_load(var3 + 44) << 4)) + 4) == 20 else 0):
                    break
                if (1 if i32_load8_u(var3 + 127) == 6 else 0):
                    break
                if (1 if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 264) == 1 else 0):
                    break
                if i32_load(var3 + 92):
                    break
                var7 = i32_load(9213808)
                if (1 if i32_load(9213808) > 9999 else 0):
                    break
                if (1 if i32_load8_u(var3 + 125) == 3 else 0):
                    break
                var0 = 1
                var10 = i32_load(var3 + 28)
                i32_store(9213808, (var7 + 1))
                i32_store(((var7 << 2) + 9173808), var10)
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
                var7 = (i32_load(9163776) + 1)
                i32_store(9163776, (i32_load(9163776) + 1))
                var10 = i32_load(9163784)
                if (1 if var7 < i32_load(9163784) else 0):
                    break
                i32_store(var9 + 64, var10)
                a_b()
                i32_store(9163784, (i32_load(9163784) + 40000))
                i32_store(var3 + 92, var0)
                if (1 if i32_load(var3 + 36) == 0 else 0):
                if (1 if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 264) != 1 else 0):
                    break
                if i32_load(var3 + 80):
                    break
                var7 = i32_load16_u(var3 + 116)
                if (1 if i32_load16_u(var3 + 116) == 0 else 0):
                    break
                var10 = i32_load16_u(var3 + 118)
                if (1 if i32_load16_u(var3 + 118) == 0 else 0):
                    break
                if (1 if i32_load8_u(9147152) == 0 else 0):
                    if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var3 + 110))))) == 0 else 0):
                        break
                    if (1 if i32_load((i32_load(9215884) + (i32_load(var3 + 44) << 4)) + 4) == 20 else 0):
                        break
                    if (1 if i32_load8_u(var3 + 127) == 6 else 0):
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
                var11 = (i32_load(9163776) + 1)
                i32_store(9163776, (i32_load(9163776) + 1))
                var12 = i32_load(9163784)
                if (1 if var11 < i32_load(9163784) else 0):
                    break
                i32_store(var9 + 48, var12)
                a_b()
                i32_store(9163784, (i32_load(9163784) + 40000))
                var10 = i32_load16_u(var3 + 118)
                var7 = i32_load16_u(var3 + 116)
                i32_store(var3 + 80, var0)
                if (1 if var1 != var14 else 0):
                    continue
                break  # end loop
            var1 = (1 if var2 != var13 else 0)
            var2 = var6
            if var1:
                continue
            break  # end loop
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != 3 else 0):
            continue
        break  # end loop
    break
    var27 = a_f()
    i32_store(9681912, var4)
    f64_store(9681904, var27)
    i32_store(9681916, var0)
    if (1 if var2 < 3 else 0):
        break
    var0 = i32_load(9671128)
    var1 = (i32_load(9671128) + (var2 * 132))
    if (1 if i32_load8_u(9147152) == 0 else 0):
        if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var1 + 110))))) == 0 else 0):
            break
        var4 = (var0 + (var2 * 132))
        if (1 if i32_load((i32_load(9215884) + (i32_load((var0 + (var2 * 132)) + 44) << 4)) + 4) == 20 else 0):
            break
        if (1 if i32_load8_u(var4 + 127) == 6 else 0):
            break
    if (1 if i32_load(var1 + 92) == 0 else 0):
        break
    if (1 if i32_load8_u(9163792) == 0 else 0):
        break
    func77(var1)
    break
    func44(var1, 0)
    break
    var2 = (var0 + (var2 * 132))
    if (i32_load8_u(9163792) | i32_load8_u((var0 + (var2 * 132)) + 128)):
        break
    i32_store(9213820, i32_load(var2 + 28))
    func44(var1, 1)
    global global0
    global0 = (var9 + 80)
    return func28(0, 0)

