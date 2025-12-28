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
# $func641
# ==========================================================
def func641(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var1 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if i32_load8_u(9163793):
        break
    var4 = (i32_load(9671128) + (i32_load(9173808) * 132))
    var0 = i32_load16_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 112)
    var3 = (i32_load16_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 112) - 2)
    var5 = ((i32_load8_u(var4 + 122) * 404) + 9568096)
    var7 = ((var0 + i32_load(((i32_load8_u(var4 + 122) * 404) + 9568096) + 216)) + 2)
    if (1 if (i32_load16_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 112) - 2) >= ((var0 + i32_load(((i32_load8_u(var4 + 122) * 404) + 9568096) + 216)) + 2) else 0):
        break
    var6 = ((i32_load(var5 + 220) + i32_load16_u(var4 + 114)) + 2)
    while True:  # loop $label6
        var5 = (var3 + 1)
        var0 = (i32_load16_u(var4 + 114) - 2)
        if (1 if var6 > (i32_load16_u(var4 + 114) - 2) else 0):
            while True:  # loop $label5
                var2 = i32_load(9142440)
                if (1 if i32_load(9142440) <= var0 else 0):
                    break
                if (1 if (var0 | var3) < 0 else 0):
                    break
                if (1 if var2 > var3 else 0):
                    break
                break
                var8 = (var0 + 1)
                var2 = (var2 + 2)
                if i32_load((i32_load(9142840) + ((var5 + (((var0 + 1) + (var2 + 2)) * var2)) << 2))):
                    break
                i32_store(var1 + 8, var0)
                i32_store(var1 + 4, var3)
                i32_store(var1, i32_load(38636))
                i32_store(var1 + 12, i32_load16_u(var4 + 110))
                i64_store(var1 + 32, 4294967297)
                i64_store(var1 + 24, 4294967297)
                i64_store(var1 + 16, 4294967297)
                i32_store(var1 + 40, 0)
                var0 = i32_load(9213808)
                if i32_load8_u(9147210):
                    func41(4, 9173808, var0, var1, 11)
                    break
                var9 = (var0 << 2)
                var2 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
                if var0:
                    # Unknown: memory.copy []
                # call_indirect via table[i32_load(9213856)]
                var0 = var8
                if (1 if call_indirect(i32_load(9213856)) != var8 else 0):
                    continue
                break  # end loop
        var3 = var5
        if (1 if var5 != var7 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var1 + 48)
    return var0


# ==========================================================
# $func725
# ==========================================================
def func725(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var0 = i32_load(9671128)
    var5 = (var0 + (i32_load(var1) * 132))
    var1 = i32_load((var0 + (i32_load(var1) * 132)) + 36)
    var3 = (i32_load(9671128) + (i32_load((var0 + (i32_load(var1) * 132)) + 36) * 132))
    var2 = i32_load8_u((i32_load(9671128) + (i32_load((var0 + (i32_load(var1) * 132)) + 36) * 132)) + 122)
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load((var0 + (i32_load(var1) * 132)) + 36) * 132)) + 122) == i32_load(38528) else 0):
        break
    var4 = i32_load8_u(var5 + 122)
    if (1 if i32_load(((i32_load8_u(var5 + 122) * 404) + 9568096) + 268) == 0 else 0):
        if (1 if i32_load8_u(((var2 * 404) + 9568096) + 335) == 0 else 0):
            break
        func376(var5, var3)
        break
    var6 = (var0 + (var1 * 132))
    if (1 if i32_load((var0 + (var1 * 132)) + 72) == 0 else 0):
        break
    var0 = i32_load(var6 + 24)
    if (1 if i32_load(var6 + 24) == 0 else 0):
        break
    var1 = i32_load(var0)
    if (1 if i32_load(var0) == 0 else 0):
        break
    var0 = i32_load(var1)
    if i32_load(var1):
        break
    var1 = func26(16)
    var7 = ((var2 * 404) + 9568096)
    var2 = i32_load(((var2 * 404) + 9568096) + 236)
    var0 = (i32_load(((var2 * 404) + 9568096) + 236) + 2)
    i32_store(func26(16) + 4, (i32_load(((var2 * 404) + 9568096) + 236) + 2))
    var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    i32_store(var1, func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2))))
    i64_store(var1 + 8, 4294967296)
    if var2:
        var3 = 0
        var4 = 0
        while True:  # loop $label5
            var8 = i32_load((i32_load(var7 + 232) + (var4 << 2)))
            if (1 if i32_load(var1 + 4) != var3 else 0):
                var2 = var0
                break
            var2 = (i32_load(var1 + 12) + var3)
            i32_store(var1 + 4, (i32_load(var1 + 12) + var3))
            var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
            if var3:
                # Unknown: memory.copy []
            i32_store(var1, var2)
            i32_store(var1 + 8, (var3 + 1))
            i32_store((var2 + (var3 << 2)), var8)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < i32_load(var7 + 236) else 0):
                var3 = i32_load(var1 + 8)
                var0 = var2
                continue
            break  # end loop
        var0 = var2
    var3 = i32_load(var6 + 24)
    if (1 if i32_load(var6 + 24) == 0 else 0):
        var3 = func26(16)
        i64_store(func26(16), 0)
        i64_store(var3 + 8, 0)
        i32_store(var6 + 24, var3)
    i32_store(var3, var1)
    var4 = i32_load8_u(var5 + 122)
    var4 = i32_load(((var4 * 404) + 9568096) + 172)
    var2 = i32_load(var1 + 8)
    if i32_load(var1 + 8):
        var3 = 0
        while True:  # loop $label6
            if (1 if i32_load((var0 + (var3 << 2))) == var4 else 0):
                break
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var2 else 0):
                continue
            break  # end loop
    if (1 if i32_load(var1 + 4) != var2 else 0):
        var3 = var0
        break
    var3 = (i32_load(var1 + 12) + var2)
    i32_store(var1 + 4, (i32_load(var1 + 12) + var2))
    var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var2:
        # Unknown: memory.copy []
    i32_store(var1, var3)
    var2 = i32_load(var1 + 8)
    i32_store(var1 + 8, (var2 + 1))
    i32_store((var3 + (var2 << 2)), var4)


# ==========================================================
# $func775
# ==========================================================
def func775(var0, var1):
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
    var21 = 0.0
    var8 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var2 = ((var1 & 0xFFFFFFFF) >> 16)
    var1 = (var1 & 65535)
    var12 = i32_load(9671128)
    var13 = (i32_load(9671128) + (var0 * 132))
    var4 = i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110)
    var11 = i32_load(9561692)
    if i32_load8_u(9142917):
        break
    var6 = i32_load(9299880)
    if i32_load(9299880):
        var6 = (var6 - 1)
        i32_store(9299880, (var6 - 1))
        var6 = i32_load((i32_load(9299872) + (var6 << 2)))
        break
    var6 = i32_load(9163776)
    var5 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var9 = i32_load(9163784)
    if (1 if var5 < i32_load(9163784) else 0):
        break
    i32_store(var8 + 48, var9)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    var14 = (var1 << 5)
    var15 = (var2 << 5)
    var5 = i32_load(9142572)
    if (1 if i32_load(9142572) == 0 else 0):
        break
    var9 = i32_load(var5 + 16)
    var5 = i32_load(var5 + 24)
    if (1 if i32_load(var5 + 24) >= 100 else 0):
        var21 = f32_load((((var5 + var9) << 2) + 32700))
        if (1 if ((1 if f32_load((((var5 + var9) << 2) + 32700)) < 4294967300.0 else 0) & (1 if var21 >= 0.0 else 0)) == 0 else 0):
            break
        var3 = int(var21)
        break
    var3 = ((var9 * 1000) // var5)
    var6 = (var14 - i32_load(9142952))
    var6 = (var15 - i32_load(9142956))
    if (1 if ((((var14 - i32_load(9142952)) * var6) + ((var15 - i32_load(9142956)) * var6)) - 1) > 9000000 else 0):
        break
    var5 = i32_load(39868)
    var9 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var6 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var2) + var1) << 1)))
    if (1 if var9 == 2 else 0):
        if (1 if var6 > 1 else 0):
            break
        break
    if (1 if var6 == 0 else 0):
        break
    i32_store(var8 + 40, var2)
    i32_store(var8 + 36, var1)
    i32_store(var8 + 32, var5)
    a_b()
    var6 = (var1 - 3)
    var1 = (i32_load(9561692) + (i32_load16_u(var13 + 110) * 286704))
    var5 = i32_load(((i32_load(9561692) + (i32_load16_u(var13 + 110) * 286704)) + 284180))
    var17 = (var6 + i32_load(((i32_load(9561692) + (i32_load16_u(var13 + 110) * 286704)) + 284180)))
    if (1 if (var1 - 3) >= (var6 + i32_load(((i32_load(9561692) + (i32_load16_u(var13 + 110) * 286704)) + 284180))) else 0):
        break
    var14 = (var2 - 3)
    var18 = (var5 + var14)
    if (1 if (var2 - 3) >= (var5 + var14) else 0):
        break
    var19 = i32_load((var1 + 284184))
    var1 = (var11 + (var4 * 286704))
    var15 = ((var11 + (var4 * 286704)) + 281752)
    var16 = (var1 + 281780)
    var11 = (var12 + (var0 * 132))
    var4 = i32_load(9142440)
    while True:  # loop $label17
        var12 = (var6 + 1)
        var0 = var14
        while True:  # loop $label16
            var1 = var0
            var0 = (var0 + 1)
            if (1 if var1 >= var4 else 0):
                break
            if (1 if (var1 | var6) < 0 else 0):
                break
            if (1 if var4 <= var6 else 0):
                break
            var1 = 0
            var3 = i32_load(9142840)
            while True:  # loop $label15
                var2 = (var4 + 2)
                var2 = i32_load((var3 + ((var12 + ((var0 + ((var4 + 2) * var1)) * var2)) << 2)))
                if (1 if i32_load((var3 + ((var12 + ((var0 + ((var4 + 2) * var1)) * var2)) << 2))) < 3 else 0):
                    break
                var2 = (i32_load(9671128) + (var2 * 132))
                var7 = i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122)
                var5 = i32_load(((i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122) * 404) + 9568096) + 288)
                if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122) * 404) + 9568096) + 288) == 0 else 0):
                    break
                if (1 if i32_load8_u(var2 + 125) == 10 else 0):
                    break
                var3 = i32_load(9561692)
                var4 = i32_load(var2 + 64)
                var9 = i32_load((((i32_load8_u(var11 + 122) * 1020) + 9299904) + (var7 << 2)))
                var5 = ((((((var9 * var19) & 0xFFFFFFFF) // 100) * var5) & 0xFFFFFFFF) // 100)
                var5 = ((i32_load(var2 + 64) - (1 if i32_load((((i32_load8_u(var11 + 122) * 1020) + 9299904) + (var7 << 2))) == 100 else 0)) if (1 if var4 < var5 else 0) else ((((((var9 * var19) & 0xFFFFFFFF) // 100) * var5) & 0xFFFFFFFF) // 100))
                if (1 if ((1 if ((i32_load(var2 + 64) - (1 if i32_load((((i32_load8_u(var11 + 122) * 1020) + 9299904) + (var7 << 2))) == 100 else 0)) if (1 if var4 < var5 else 0) else ((((((var9 * var19) & 0xFFFFFFFF) // 100) * var5) & 0xFFFFFFFF) // 100)) == var4 else 0) & (1 if var9 > 100 else 0)) == 0 else 0):
                    var4 = i32_load16_u(var2 + 110)
                    break
                var10 = i32_load16_u(var13 + 110)
                var4 = (var3 + (i32_load16_u(var13 + 110) * 286704))
                if (1 if i32_load(9147132) == 0 else 0):
                    break
                if (1 if i32_load(9671152) != var7 else 0):
                    break
                var7 = i32_load16_u(var2 + 110)
                if (1 if var10 == i32_load16_u(var2 + 110) else 0):
                    break
                if (1 if var10 == 0 else 0):
                    break
                var3 = (var3 + (var7 * 286704))
                var10 = i32_load((var3 + (var7 * 286704)) + 284628)
                var7 = i32_load(var3 + 284616)
                var20 = i32_load(var4 + 284616)
                i32_store(var8 + 16, (i32_load(var4 + 284616) if var20 else i32_load(var4 + 284628)))
                i32_store(var8 + 12, var4)
                i32_store(var8 + 4, var3)
                i32_store(var8, 927)
                i32_store(var8 + 8, (var7 if var7 else var10))
                a_b()
                var3 = i32_load((var4 + 278560))
                if i32_load((var4 + 278560)):
                    var4 = i32_load16_u(var2 + 110)
                    var3 = (var3 + ((i32_load8_u(var11 + 122) + (i32_load16_u(var2 + 110) * 255)) << 2))
                    i32_store((var3 + ((i32_load8_u(var11 + 122) + (i32_load16_u(var2 + 110) * 255)) << 2)), (i32_load(var3) + 1))
                    break
                var4 = i32_load16_u(var2 + 110)
                var3 = i32_load(9561692)
                var7 = i32_load(((i32_load(9561692) + (var4 * 286704)) + 278568))
                if i32_load(((i32_load(9561692) + (var4 * 286704)) + 278568)):
                    var7 = (var7 + ((i32_load8_u(var2 + 122) + (i32_load16_u(var13 + 110) * 255)) << 2))
                    i32_store((var7 + ((i32_load8_u(var2 + 122) + (i32_load16_u(var13 + 110) * 255)) << 2)), (i32_load(var7) + 1))
                i32_store16(var2 + 116, i32_load(var11 + 28))
                i32_store(var16, (i32_load(var16) + var5))
                i32_store(var15, (i32_load(var15) + 1))
                var7 = i32_load16_u(var13 + 110)
                var10 = i32_load((var3 + (i32_load16_u(var13 + 110) * 286704)) + 278556)
                if i32_load((var3 + (i32_load16_u(var13 + 110) * 286704)) + 278556):
                    var10 = (var10 + ((i32_load8_u(var11 + 122) + (var4 * 255)) << 2))
                    i32_store((var10 + ((i32_load8_u(var11 + 122) + (var4 * 255)) << 2)), (i32_load(var10) + var5))
                var3 = i32_load(((var3 + (var4 * 286704)) + 278564))
                if i32_load(((var3 + (var4 * 286704)) + 278564)):
                    var3 = (var3 + ((i32_load8_u(var2 + 122) + (var7 * 255)) << 2))
                    i32_store((var3 + ((i32_load8_u(var2 + 122) + (var7 * 255)) << 2)), (i32_load(var3) + var5))
                var3 = (global0 - 48)
                global global0
                global0 = (global0 - 48)
                if (1 if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 288) == 0 else 0):
                    break
                var4 = i32_load8_u(var2 + 125)
                if (1 if i32_load8_u(var2 + 125) == 10 else 0):
                    break
                if (1 if var4 == 3 else 0):
                    break
                if (1 if i32_load8_u(var2 + 128) == 0 else 0):
                    break
                i32_store8(var2 + 127, 0)
                var4 = i32_load(var2 + 40)
                if (1 if i32_load(var2 + 40) == 0 else 0):
                    break
                if i32_load8_u(9142916):
                    i32_store(var3 + 36, var4)
                    i32_store(var3 + 32, 0)
                    a_b()
                    break
                var7 = i32_load16_u(var2 + 110)
                i32_store(var3 + 20, var4)
                i32_store(var3 + 16, (var7 + 16))
                a_b()
                i32_store8(var2 + 128, 0)
                i32_store8(var2 + 127, 2)
                if (1 if i32_load8_u(9142916) == 0 else 0):
                    break
                var4 = i32_load(var2 + 40)
                if (1 if i32_load(var2 + 40) == 0 else 0):
                    break
                i32_store(var3 + 4, var4)
                i32_store(var3, -419430656)
                a_b()
                func119(func60(var2, 1.0), var2, 0, 0)
                i32_store8(var2 + 125, 9)
                var4 = i32_load(var2 + 64)
                if (1 if var5 >= i32_load(var2 + 64) else 0):
                    if (1 if var9 < 101 else 0):
                        break
                    i32_store(var2 + 64, 0)
                    break
                i32_store(func32(var2, var2, 0) + 64, (var4 - var5))
                func63(var3, var2, 20, 0, i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284200)))
                func77(var2)
                global global0
                global0 = (var3 + 48)
                func103(var2)
                var3 = i32_load(9142840)
                var4 = i32_load(9142440)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != 3 else 0):
                    continue
                break  # end loop
            if (1 if var0 != var18 else 0):
                continue
            break  # end loop
        var6 = var12
        if (1 if var12 != var17 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var8 - -64)
    return 1061

