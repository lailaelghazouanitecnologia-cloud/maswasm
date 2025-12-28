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
# $Xd
# Export: Xd
# ==========================================================
def Xd():
    """Export: Xd"""
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
    var20 = 0
    var21 = 0
    var22 = 0
    var23 = 0
    var24 = 0
    var25 = 0
    var26 = 0
    var27 = 0
    var28 = 0
    var29 = 0
    var30 = 0
    var31 = 0
    var32 = 0
    var33 = 0
    var34 = 0
    var35 = 0
    var36 = 0
    var37 = 0
    var38 = 0
    var39 = 0
    var40 = 0
    var41 = 0
    var42 = 0
    var43 = 0
    var44 = 0
    var45 = 0
    var46 = 0
    var47 = 0
    var48 = 0
    var49 = 0
    var50 = 0
    while True:  # loop $label1
        var2 = ((var0 * 404) + 9568096)
        if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 1 else 0):
            var1 = ((i32_load(var2 + 244) + ((i32_load(var2 + 364) + (var1 + i32_load(var2 + 236))) + (i32_load(var2 + 220) * i32_load(var2 + 216)))) + 55)
            var3 = 0
            while True:  # loop $label0
                var2 = (((var0 * 1020) + 9299904) + (var3 << 2))
                var1 = (var1 if (1 if i32_load((((var0 * 1020) + 9299904) + (var3 << 2))) == 100 else 0) else (var1 + 2))
                var1 = ((var1 if (1 if i32_load((((var0 * 1020) + 9299904) + (var3 << 2))) == 100 else 0) else (var1 + 2)) if (1 if i32_load(var2 + 4) == 100 else 0) else (var1 + 2))
                var1 = (((var1 if (1 if i32_load((((var0 * 1020) + 9299904) + (var3 << 2))) == 100 else 0) else (var1 + 2)) if (1 if i32_load(var2 + 4) == 100 else 0) else (var1 + 2)) if (1 if i32_load(var2 + 8) == 100 else 0) else (var1 + 2))
                var3 = (var3 + 3)
                if (1 if (var3 + 3) != 255 else 0):
                    continue
                break  # end loop
            var7 = (var7 + 1)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != 255 else 0):
            continue
        break  # end loop
    var2 = i32_load(9685864)
    if i32_load(9685864):
        i32_store(9685864, 0)
    var3 = (var7 * 55)
    var7 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    i32_store(9685864, func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2))))
    while True:  # loop $label20
        var0 = 0
        var1 = 0
        var2 = ((var11 * 404) + 9568096)
        if (1 if i32_load(((var11 * 404) + 9568096) + 264) == 1 else 0):
            while True:  # loop $label2
                var12 = ((var11 * 1020) + 9299904)
                var1 = (((var11 * 1020) + 9299904) + (var0 << 2))
                var5 = (var1 if (1 if i32_load((((var11 * 1020) + 9299904) + (var0 << 2))) == 100 else 0) else (var1 + 2))
                var5 = ((var1 if (1 if i32_load((((var11 * 1020) + 9299904) + (var0 << 2))) == 100 else 0) else (var1 + 2)) if (1 if i32_load(var1 + 4) == 100 else 0) else (var5 + 2))
                var1 = (((var1 if (1 if i32_load((((var11 * 1020) + 9299904) + (var0 << 2))) == 100 else 0) else (var1 + 2)) if (1 if i32_load(var1 + 4) == 100 else 0) else (var5 + 2)) if (1 if i32_load(var1 + 8) == 100 else 0) else (var5 + 2))
                var0 = (var0 + 3)
                if (1 if (var0 + 3) != 255 else 0):
                    continue
                break  # end loop
            var6 = i32_load(var2 + 104)
            var8 = i32_load(var2 + 68)
            var9 = i32_load(var2 + 72)
            var10 = i32_load(var2 + 76)
            var14 = i32_load(var2 + 80)
            var15 = i32_load(var2 + 116)
            var16 = i32_load(var2 + 236)
            var17 = i32_load(var2 + 92)
            var18 = i32_load(var2 + 276)
            var19 = i32_load(var2 + 96)
            var20 = i32_load(var2 + 224)
            var21 = i32_load(var2 + 204)
            var22 = i32_load(var2 + 200)
            var23 = i32_load(var2 + 228)
            var24 = i32_load(var2 + 208)
            var5 = i32_load(var2 + 220)
            var4 = i32_load(var2 + 216)
            var25 = i32_load(var2 + 192)
            var26 = i32_load(var2 + 188)
            var27 = i32_load(var2 + 84)
            var28 = i32_load(var2 + 136)
            var29 = i32_load(var2 + 140)
            var30 = i32_load(var2 + 176)
            var31 = i32_load(var2 + 112)
            var32 = i32_load(var2 + 364)
            var33 = i32_load(var2 + 272)
            var34 = i32_load(var2 + 212)
            var35 = i32_load(var2 + 280)
            var36 = i32_load(var2 + 328)
            var37 = i32_load8_u(var2 + 332)
            var38 = i32_load8_u(var2 + 353)
            var39 = i32_load8_u(var2 + 335)
            var40 = i32_load8_u(var2 + 336)
            var49 = i64_load(var2 + 284)
            var50 = i64_load(var2 + 292)
            var41 = i32_load(var2 + 300)
            var42 = i32_load(var2 + 308)
            var43 = i32_load(var2 + 312)
            var44 = i32_load(var2 + 324)
            var45 = i32_load(var2 + 320)
            var46 = i32_load(var2 + 340)
            var47 = i32_load(var2 + 344)
            var48 = i32_load8_u(var2 + 354)
            var0 = (var7 + (var13 * 220))
            i32_store((var7 + (var13 * 220)) + 192, i32_load(var2 + 244))
            i32_store(var0 + 188, var48)
            i32_store(var0 + 184, var47)
            i32_store(var0 + 180, var46)
            i32_store(var0 + 176, var45)
            i32_store(var0 + 172, var44)
            i32_store(var0 + 168, var43)
            i32_store(var0 + 164, var42)
            i32_store(var0 + 160, var41)
            i64_store(var0 + 152, var50)
            i64_store(var0 + 144, var49)
            i32_store(var0 + 140, var40)
            i32_store(var0 + 136, var39)
            i32_store(var0 + 132, var38)
            i32_store(var0 + 128, var37)
            i32_store(var0 + 124, var36)
            i32_store(var0 + 120, var35)
            i32_store(var0 + 116, var1)
            i32_store(var0 + 112, var34)
            i32_store(var0 + 108, var33)
            i32_store(var0 + 104, var32)
            i32_store(var0 + 100, var31)
            i32_store(var0 + 96, var30)
            i32_store(var0 + 92, var29)
            i32_store(var0 + 88, var28)
            i32_store(var0 + 84, var27)
            i32_store(var0 + 80, var26)
            i32_store(var0 + 76, var25)
            i32_store(var0 + 72, (var4 * var5))
            i32_store(var0 + 68, var5)
            i32_store(var0 + 64, var4)
            i32_store(var0 + 60, var24)
            i32_store(var0 + 56, var23)
            i32_store(var0 + 52, var22)
            i32_store(var0 + 48, var21)
            i32_store(var0 + 44, var20)
            i32_store(var0 + 40, var19)
            i32_store(var0 + 36, var18)
            i32_store(var0 + 32, var17)
            i32_store(var0 + 28, var16)
            i32_store(var0 + 24, var15)
            i32_store(var0 + 20, var14)
            i32_store(var0 + 16, var10)
            i32_store(var0 + 12, var9)
            i32_store(var0 + 8, var8)
            i32_store(var0 + 4, var6)
            i32_store(var0, var11)
            i64_store(var0 + 212, 0)
            i64_store(var0 + 204, 0)
            i64_store(var0 + 196, 0)
            var1 = i32_load(var2 + 236)
            if (1 if i32_load(var2 + 236) == 0 else 0):
                break
            var9 = (var1 & 3)
            var4 = i32_load(var2 + 232)
            var0 = 0
            if (1 if var1 < 4 else 0):
                var1 = 0
                break
            var10 = (var1 & -4)
            var1 = 0
            var5 = 0
            while True:  # loop $label5
                var6 = (var7 + (var3 << 2))
                var8 = (var1 << 2)
                i32_store((var7 + (var3 << 2)), i32_load((var4 + (var1 << 2))))
                i32_store(var6 + 4, i32_load((var4 + (var8 | 4))))
                i32_store(var6 + 8, i32_load((var4 + (var8 | 8))))
                i32_store(var6 + 12, i32_load((var4 + (var8 | 12))))
                var1 = (var1 + 4)
                var3 = (var3 + 4)
                var5 = (var5 + 4)
                if (1 if (var5 + 4) != var10 else 0):
                    continue
                break  # end loop
            if (1 if var9 == 0 else 0):
                break
            while True:  # loop $label6
                i32_store((var7 + (var3 << 2)), i32_load((var4 + (var1 << 2))))
                var1 = (var1 + 1)
                var3 = (var3 + 1)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var9 else 0):
                    continue
                break  # end loop
            var1 = (i32_load(var2 + 220) * i32_load(var2 + 216))
            if (1 if (i32_load(var2 + 220) * i32_load(var2 + 216)) == 0 else 0):
                break
            var8 = (var1 & 3)
            var4 = i32_load(var2 + 372)
            var5 = 0
            if (1 if var1 < 4 else 0):
                var1 = 0
                break
            var9 = (var1 & -4)
            var1 = 0
            var0 = 0
            while True:  # loop $label9
                var6 = (var7 + (var3 << 2))
                i32_store((var7 + (var3 << 2)), i32_load8_u((var1 + var4)))
                i32_store(var6 + 4, i32_load8_u((var4 + (var1 | 1))))
                i32_store(var6 + 8, i32_load8_u((var4 + (var1 | 2))))
                i32_store(var6 + 12, i32_load8_u((var4 + (var1 | 3))))
                var1 = (var1 + 4)
                var3 = (var3 + 4)
                var0 = (var0 + 4)
                if (1 if (var0 + 4) != var9 else 0):
                    continue
                break  # end loop
            if (1 if var8 == 0 else 0):
                break
            while True:  # loop $label10
                i32_store((var7 + (var3 << 2)), i32_load8_u((var1 + var4)))
                var1 = (var1 + 1)
                var3 = (var3 + 1)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var8 else 0):
                    continue
                break  # end loop
            var1 = i32_load(var2 + 364)
            if (1 if i32_load(var2 + 364) == 0 else 0):
                break
            var9 = (var1 & 3)
            var4 = i32_load(var2 + 24)
            var0 = 0
            if (1 if var1 < 4 else 0):
                var1 = 0
                break
            var10 = (var1 & -4)
            var1 = 0
            var5 = 0
            while True:  # loop $label13
                var6 = (var7 + (var3 << 2))
                var8 = (var1 << 2)
                i32_store((var7 + (var3 << 2)), i32_load((var4 + (var1 << 2))))
                i32_store(var6 + 4, i32_load((var4 + (var8 | 4))))
                i32_store(var6 + 8, i32_load((var4 + (var8 | 8))))
                i32_store(var6 + 12, i32_load((var4 + (var8 | 12))))
                var1 = (var1 + 4)
                var3 = (var3 + 4)
                var5 = (var5 + 4)
                if (1 if (var5 + 4) != var10 else 0):
                    continue
                break  # end loop
            if (1 if var9 == 0 else 0):
                break
            while True:  # loop $label14
                i32_store((var7 + (var3 << 2)), i32_load((var4 + (var1 << 2))))
                var1 = (var1 + 1)
                var3 = (var3 + 1)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var9 else 0):
                    continue
                break  # end loop
            var1 = 0
            while True:  # loop $label15
                var0 = i32_load((var12 + (var1 << 2)))
                if (1 if i32_load((var12 + (var1 << 2))) != 100 else 0):
                    var5 = (var7 + (var3 << 2))
                    i32_store((var7 + (var3 << 2)), var1)
                    i32_store(var5 + 4, var0)
                    var3 = (var3 + 2)
                var0 = (var1 | 1)
                if (1 if (var1 | 1) != 255 else 0):
                    var5 = i32_load((var12 + (var0 << 2)))
                    if (1 if i32_load((var12 + (var0 << 2))) != 100 else 0):
                        var4 = (var7 + (var3 << 2))
                        i32_store((var7 + (var3 << 2)), var0)
                        i32_store(var4 + 4, var5)
                        var3 = (var3 + 2)
                    var1 = (var1 + 2)
                    continue
                break  # end loop
            var1 = i32_load(var2 + 244)
            if (1 if i32_load(var2 + 244) == 0 else 0):
                break
            var6 = (var1 & 3)
            var2 = i32_load(var2 + 240)
            var8 = 0
            if (1 if var1 < 4 else 0):
                var1 = 0
                break
            var12 = (var1 & -4)
            var1 = 0
            var5 = 0
            while True:  # loop $label18
                var0 = (var7 + (var3 << 2))
                var4 = (var1 << 2)
                i32_store((var7 + (var3 << 2)), i32_load((var2 + (var1 << 2))))
                i32_store(var0 + 4, i32_load((var2 + (var4 | 4))))
                i32_store(var0 + 8, i32_load((var2 + (var4 | 8))))
                i32_store(var0 + 12, i32_load((var2 + (var4 | 12))))
                var1 = (var1 + 4)
                var3 = (var3 + 4)
                var5 = (var5 + 4)
                if (1 if (var5 + 4) != var12 else 0):
                    continue
                break  # end loop
            if (1 if var6 == 0 else 0):
                break
            while True:  # loop $label19
                i32_store((var7 + (var3 << 2)), i32_load((var2 + (var1 << 2))))
                var1 = (var1 + 1)
                var3 = (var3 + 1)
                var8 = (var8 + 1)
                if (1 if (var8 + 1) != var6 else 0):
                    continue
                break  # end loop
            var13 = (var13 + 1)
        var11 = (var11 + 1)
        if (1 if (var11 + 1) != 255 else 0):
            continue
        break  # end loop
    return (var13 * 55)


# ==========================================================
# $Ed
# Export: Ed
# ==========================================================
def Ed(var0, var1):
    """Export: Ed"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var4 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var2 = i32_load(9568088)
    if var1:
        var0 = i32_load(var2 + 80)
        i32_store(var4 + 4, i32_load(var2 + 88))
        i32_store(var4, var0)
        break
    i32_store(var2 + 88, 0)
    var1 = i32_load(var2 + 84)
    if (1 if var0 >= i32_load(var2 + 84) else 0):
        var1 = (i32_load(var2 + 92) + (var0 + var1))
        i32_store(var2 + 84, (i32_load(var2 + 92) + (var0 + var1)))
        var3 = i32_load(var2 + 80)
        var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        if var3:
        i32_store(var2 + 80, var1)
    if (1 if var0 == 0 else 0):
        break
    var7 = (var0 & 1)
    var3 = i32_load(var2 + 80)
    var1 = 0
    if (1 if var0 != 1 else 0):
        var8 = (var0 & -2)
        var0 = 0
        while True:  # loop $label1
            var5 = (var1 << 2)
            var6 = i32_load(((var1 << 2) + 9147392))
            var9 = i32_load(var2 + 88)
            i32_store(var2 + 88, (i32_load(var2 + 88) + 1))
            i32_store((var3 + (var9 << 2)), var6)
            var5 = i32_load(((var5 | 4) + 9147392))
            var6 = i32_load(var2 + 88)
            i32_store(var2 + 88, (i32_load(var2 + 88) + 1))
            i32_store((var3 + (var6 << 2)), var5)
            var1 = (var1 + 2)
            var0 = (var0 + 2)
            if (1 if (var0 + 2) != var8 else 0):
                continue
            break  # end loop
    if (1 if var7 == 0 else 0):
        break
    var0 = i32_load(((var1 << 2) + 9147392))
    var1 = i32_load(var2 + 88)
    i32_store(var2 + 88, (i32_load(var2 + 88) + 1))
    i32_store((var3 + (var1 << 2)), var0)
    global global0
    global0 = (var4 + 16)


# ==========================================================
# $func954
# ==========================================================
def func954(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var0 = i32_load(9568064)
    if i32_load(9568064):
        var3 = i32_load(9568068)
        var1 = var0
        if (1 if i32_load(9568068) != var0 else 0):
            while True:  # loop $label0
                var1 = (var3 - 128)
                var2 = i32_load((var3 - 128) + 12)
                if i32_load((var3 - 128) + 12):
                    i32_store((var3 - 112), var2)
                var2 = i32_load(var1)
                if i32_load(var1):
                    i32_store((var3 - 124), var2)
                var3 = var1
                if (1 if var1 != var0 else 0):
                    continue
                break  # end loop
            var1 = i32_load(9568064)
        i32_store(9568068, var0)

