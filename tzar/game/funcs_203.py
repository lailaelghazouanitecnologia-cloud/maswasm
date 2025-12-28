"""
Auto-generated from WAT. Contains 2 functions.
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
# $Yb
# Export: Yb
# ==========================================================
def Yb(var0):
    """Export: Yb"""
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
    var2 = 3
    var1 = i32_load(9142892)
    if (1 if i32_load(9142892) >= 3 else 0):
        if (1 if i32_load(9671136) > 3 else 0):
            while True:  # loop $label2
                var1 = (i32_load(9671128) + (var2 * 132))
                if (1 if i32_load8_u((i32_load(9671128) + (var2 * 132)) + 125) == 3 else 0):
                    break
                var3 = i32_load16_u(var1 + 110)
                if (1 if var0 == i32_load16_u(var1 + 110) else 0):
                    break
                if (1 if var0 >= var3 else 0):
                    break
                var4 = (var3 - 1)
                i32_store16(var1 + 110, (var3 - 1))
                i32_store8(var1 + 127, 0)
                var3 = i32_load(var1 + 40)
                if (1 if i32_load(var1 + 40) == 0 else 0):
                    break
                if i32_load8_u(9142916):
                    i32_store(var5 + 20, var3)
                    i32_store(var5 + 16, 0)
                    a_b()
                    break
                i32_store(var5 + 4, var3)
                i32_store(var5, ((var4 & 65535) + 16))
                a_b()
                if (1 if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 20) == 0 else 0):
                    break
                var2 = (var2 + 1)
                if (1 if (var2 + 1) < i32_load(9671136) else 0):
                    continue
                break  # end loop
            var1 = i32_load(9142892)
        var9 = (var1 - 1)
        if (1 if (var1 - 1) >= 2 else 0):
            var4 = i32_load(9143004)
            var10 = (var1 & 1)
            var12 = (var1 - 3)
            var11 = (var1 - 2)
            var13 = ((var1 - 2) & -2)
            var3 = 1
            while True:  # loop $label4
                var6 = (var3 + (1 if var0 <= var3 else 0))
                var8 = 0
                var2 = 1
                if var12:
                    while True:  # loop $label3
                        var7 = (var2 + 1)
                        i32_store8((var4 + ((var1 * var2) + var3)), i32_load8_u((var4 + (var6 + ((var2 if (1 if var0 > var2 else 0) else (var2 + 1)) * var1)))))
                        var2 = (var2 + 2)
                        i32_store8((var4 + ((var1 * var7) + var3)), i32_load8_u((var4 + (var6 + ((var7 if (1 if var0 > var7 else 0) else (var2 + 2)) * var1)))))
                        var8 = (var8 + 2)
                        if (1 if (var8 + 2) != var13 else 0):
                            continue
                        break  # end loop
                if var10:
                    i32_store8((var4 + ((var1 * var2) + var3)), i32_load8_u((var4 + (var6 + ((var2 + (1 if var0 <= var2 else 0)) * var1)))))
                var3 = (var3 + 1)
                if (1 if (var3 + 1) != var9 else 0):
                    continue
                break  # end loop
            var10 = (var11 & -2)
            var11 = (var1 & 1)
            var4 = i32_load(9143012)
            var3 = 1
            while True:  # loop $label6
                var6 = (var3 + (1 if var0 <= var3 else 0))
                var2 = 1
                var8 = 0
                if var12:
                    while True:  # loop $label5
                        var7 = (var2 + 1)
                        i32_store8((var4 + ((var1 * var2) + var3)), i32_load8_u((var4 + (var6 + ((var2 if (1 if var0 > var2 else 0) else (var2 + 1)) * var1)))))
                        var2 = (var2 + 2)
                        i32_store8((var4 + ((var1 * var7) + var3)), i32_load8_u((var4 + (var6 + ((var7 if (1 if var0 > var7 else 0) else (var2 + 2)) * var1)))))
                        var8 = (var8 + 2)
                        if (1 if (var8 + 2) != var10 else 0):
                            continue
                        break  # end loop
                if var11:
                    i32_store8((var4 + ((var1 * var2) + var3)), i32_load8_u((var4 + (var6 + ((var2 + (1 if var0 <= var2 else 0)) * var1)))))
                var3 = (var3 + 1)
                if (1 if (var3 + 1) != var9 else 0):
                    continue
                break  # end loop
        i32_store(9142892, var9)
        if (1 if var0 < var9 else 0):
            var3 = i32_load(9561692)
            var1 = var0
            while True:  # loop $label7
                var2 = (var3 + (var1 * 286704))
                # Unknown: memory.copy []
                i32_store(var2 + 283908, var1)
                var1 = (var1 + 1)
                var2 = i32_load(9142892)
                if (1 if (var1 + 1) < i32_load(9142892) else 0):
                    continue
                break  # end loop
        else:
        func284(var0)
    global global0
    global0 = (var5 + 32)
    return 0


# ==========================================================
# $func851
# ==========================================================
def func851(var0, var1):
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
    var22 = 0
    var5 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var10 = ((var0 & 0xFFFFFFFF) >> 16)
    var15 = (((var0 & 0xFFFFFFFF) >> 16) + 3)
    var11 = (var0 & 65535)
    var16 = ((var0 & 65535) + 3)
    var17 = (var10 - 2)
    var7 = (var11 - 2)
    var8 = (i32_load(9671128) + (var1 * 132))
    var18 = i32_load(((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (var1 * 132)) + 110) * 286704)) + 284356))
    while True:  # loop $label6
        var14 = (var7 + 1)
        var0 = (var7 - var11)
        var19 = (((var7 - var11) * var0) - 1)
        var0 = var17
        while True:  # loop $label5
            var1 = var0
            var0 = (var0 - var10)
            if (1 if (var19 + ((var0 - var10) * var0)) > 4 else 0):
                break
            var0 = i32_load(9142440)
            if (1 if i32_load(9142440) <= var1 else 0):
                break
            if (1 if (var1 | var7) < 0 else 0):
                break
            if (1 if var0 <= var7 else 0):
                break
            var20 = ((var18 & 0xFFFFFFFF) >> ((1 if var7 != var11 else 0) | (1 if var1 != var10 else 0)))
            var21 = (var1 + 1)
            var0 = 0
            while True:  # loop $label4
                var4 = (i32_load(9142440) + 2)
                var4 = i32_load((i32_load(9142840) + ((var14 + ((var21 + ((i32_load(9142440) + 2) * var0)) * var4)) << 2)))
                if (1 if i32_load((i32_load(9142840) + ((var14 + ((var21 + ((i32_load(9142440) + 2) * var0)) * var4)) << 2))) < 3 else 0):
                    break
                var4 = (i32_load(9671128) + (var4 * 132))
                var6 = i32_load8_u((i32_load(9671128) + (var4 * 132)) + 122)
                var2 = i32_load(((i32_load8_u((i32_load(9671128) + (var4 * 132)) + 122) * 404) + 9568096) + 284)
                if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var4 * 132)) + 122) * 404) + 9568096) + 284) == 0 else 0):
                    break
                var9 = i32_load8_u(var4 + 125)
                if (1 if i32_load8_u(var4 + 125) == 10 else 0):
                    break
                var2 = (var2 * var20)
                var2 = (1 if (1 if var2 < 100 else 0) else (((var2 * var20) & 0xFFFFFFFF) // 100))
                var3 = i32_load(var4 + 64)
                var2 = ((1 if (1 if var2 < 100 else 0) else (((var2 * var20) & 0xFFFFFFFF) // 100)) if (1 if var2 < var3 else 0) else i32_load(var4 + 64))
                var3 = i32_load16_u(var4 + 110)
                var12 = i32_load(9561692)
                var22 = i32_load16_u(var8 + 110)
                var13 = i32_load((i32_load(9561692) + (i32_load16_u(var8 + 110) * 286704)) + 278556)
                if i32_load((i32_load(9561692) + (i32_load16_u(var8 + 110) * 286704)) + 278556):
                    var13 = (var13 + ((i32_load8_u(var8 + 122) + (var3 * 255)) << 2))
                    i32_store((var13 + ((i32_load8_u(var8 + 122) + (var3 * 255)) << 2)), (i32_load(var13) + var2))
                var3 = i32_load(((var12 + (var3 * 286704)) + 278564))
                if i32_load(((var12 + (var3 * 286704)) + 278564)):
                    var3 = (var3 + (((var22 * 255) + var6) << 2))
                    i32_store((var3 + (((var22 * 255) + var6) << 2)), (i32_load(var3) + var2))
                if (1 if var9 == 3 else 0):
                    break
                var3 = (var4 - -64)
                var6 = i32_load((var4 - -64))
                if (1 if var2 < i32_load((var4 - -64)) else 0):
                    i32_store(var3, (var6 - var2))
                    if (1 if i32_load(var4 + 92) == 0 else 0):
                        break
                    if i32_load8_u(9147141):
                        break
                    i32_store(var5, var2)
                    a_b()
                    break
                i32_store(var3, 0)
                var6 = i32_load(9561692)
                var3 = i32_load16_u(var8 + 110)
                var2 = (i32_load(9561692) + (i32_load16_u(var8 + 110) * 286704))
                if (1 if i32_load(9147132) == 0 else 0):
                    break
                if (1 if i32_load(9671152) != i32_load8_u(var4 + 122) else 0):
                    break
                var9 = i32_load16_u(var4 + 110)
                if (1 if var3 == i32_load16_u(var4 + 110) else 0):
                    break
                if (1 if var3 == 0 else 0):
                    break
                var3 = (var6 + (var9 * 286704))
                var9 = i32_load((var6 + (var9 * 286704)) + 284628)
                var6 = i32_load(var3 + 284616)
                var12 = i32_load(var2 + 284616)
                i32_store(var5 + 32, (i32_load(var2 + 284616) if var12 else i32_load(var2 + 284628)))
                i32_store(var5 + 28, var2)
                i32_store(var5 + 20, var3)
                i32_store(var5 + 16, 927)
                i32_store(var5 + 24, (var6 if var6 else var9))
                a_b()
                var3 = i32_load((var2 + 278560))
                if (1 if i32_load((var2 + 278560)) == 0 else 0):
                    var2 = i32_load16_u(var4 + 110)
                    break
                var2 = i32_load16_u(var4 + 110)
                var3 = (var3 + ((i32_load8_u(var8 + 122) + (i32_load16_u(var4 + 110) * 255)) << 2))
                i32_store((var3 + ((i32_load8_u(var8 + 122) + (i32_load16_u(var4 + 110) * 255)) << 2)), (i32_load(var3) + 1))
                var2 = i32_load(((i32_load(9561692) + (var2 * 286704)) + 278568))
                if i32_load(((i32_load(9561692) + (var2 * 286704)) + 278568)):
                    var2 = (var2 + ((i32_load8_u(var4 + 122) + (i32_load16_u(var8 + 110) * 255)) << 2))
                    i32_store((var2 + ((i32_load8_u(var4 + 122) + (i32_load16_u(var8 + 110) * 255)) << 2)), (i32_load(var2) + 1))
                i32_store16(var4 + 116, i32_load(var8 + 28))
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != 3 else 0):
                    continue
                break  # end loop
            var0 = (var1 + 1)
            if (1 if var1 != var15 else 0):
                continue
            break  # end loop
        var0 = (1 if var7 == var16 else 0)
        var7 = var14
        if (1 if var0 == 0 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var5 + 48)

