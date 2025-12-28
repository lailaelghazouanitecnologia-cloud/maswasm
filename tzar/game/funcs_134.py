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
# $Wd
# Export: Wd
# ==========================================================
def Wd():
    """Export: Wd"""
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
    var51 = 0
    var52 = 0
    var53 = 0
    var54 = 0
    var55 = 0
    var56 = 0
    while True:  # loop $label3
        var3 = ((var1 * 404) + 9568096)
        # br_table ['$label0', '$label1', '$label1', '$label1', '$label0', '$label1']
        _br_idx = i32_load(((var1 * 404) + 9568096) + 264)
        break  # br_table
        var2 = ((i32_load(var3 + 364) + (var2 + i32_load(var3 + 236))) + 60)
        var3 = 0
        while True:  # loop $label2
            var2 = (((var1 * 1020) + 9299904) + (var3 << 2))
            var5 = (var2 if (1 if i32_load((((var1 * 1020) + 9299904) + (var3 << 2))) == 100 else 0) else (var2 + 2))
            var5 = ((var2 if (1 if i32_load((((var1 * 1020) + 9299904) + (var3 << 2))) == 100 else 0) else (var2 + 2)) if (1 if i32_load(var2 + 4) == 100 else 0) else (var5 + 2))
            var2 = (((var2 if (1 if i32_load((((var1 * 1020) + 9299904) + (var3 << 2))) == 100 else 0) else (var2 + 2)) if (1 if i32_load(var2 + 4) == 100 else 0) else (var5 + 2)) if (1 if i32_load(var2 + 8) == 100 else 0) else (var5 + 2))
            var3 = (var3 + 3)
            if (1 if (var3 + 3) != 255 else 0):
                continue
            break  # end loop
        var0 = (var0 + 1)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != 255 else 0):
            continue
        break  # end loop
    var1 = i32_load(9685864)
    if i32_load(9685864):
        i32_store(9685864, 0)
    var3 = (var0 * 60)
    var5 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    i32_store(9685864, func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2))))
    while True:  # loop $label16
        var1 = ((var10 * 404) + 9568096)
        # br_table ['$label4', '$label5', '$label5', '$label5', '$label4', '$label5']
        _br_idx = i32_load(((var10 * 404) + 9568096) + 264)
        break  # br_table
        var0 = 0
        var2 = 0
        while True:  # loop $label6
            var13 = ((var10 * 1020) + 9299904)
            var2 = (((var10 * 1020) + 9299904) + (var0 << 2))
            var4 = (var2 if (1 if i32_load((((var10 * 1020) + 9299904) + (var0 << 2))) == 100 else 0) else (var2 + 2))
            var4 = ((var2 if (1 if i32_load((((var10 * 1020) + 9299904) + (var0 << 2))) == 100 else 0) else (var2 + 2)) if (1 if i32_load(var2 + 4) == 100 else 0) else (var4 + 2))
            var2 = (((var2 if (1 if i32_load((((var10 * 1020) + 9299904) + (var0 << 2))) == 100 else 0) else (var2 + 2)) if (1 if i32_load(var2 + 4) == 100 else 0) else (var4 + 2)) if (1 if i32_load(var2 + 8) == 100 else 0) else (var4 + 2))
            var0 = (var0 + 3)
            if (1 if (var0 + 3) != 255 else 0):
                continue
            break  # end loop
        var4 = i32_load(var1 + 104)
        var6 = i32_load(var1 + 92)
        var7 = i32_load(var1 + 100)
        var8 = i32_load(var1 + 68)
        var9 = i32_load(var1 + 72)
        var11 = i32_load(var1 + 76)
        var14 = i32_load(var1 + 80)
        var15 = i32_load(var1 + 120)
        var16 = i32_load(var1 + 116)
        var17 = i32_load(var1 + 276)
        var18 = i32_load(var1 + 96)
        var19 = i32_load(var1 + 224)
        var20 = i32_load(var1 + 260)
        var21 = i32_load(var1 + 204)
        var22 = i32_load(var1 + 200)
        var23 = i32_load(var1 + 236)
        var24 = i32_load(var1 + 228)
        var25 = i32_load(var1 + 208)
        var26 = i32_load(var1 + 216)
        var27 = i32_load(var1 + 192)
        var28 = i32_load(var1 + 188)
        var29 = i32_load(var1 + 84)
        var30 = i32_load(var1 + 136)
        var31 = i32_load(var1 + 140)
        var32 = i32_load(var1 + 176)
        var33 = i32_load(var1 + 364)
        var34 = i32_load(var1 + 272)
        var35 = i32_load(var1 + 212)
        var36 = i32_load(var1 + 124)
        var37 = i32_load(var1 + 280)
        var38 = i32_load(var1 + 328)
        var39 = i32_load8_u(var1 + 353)
        var40 = i32_load8_u(var1 + 335)
        var41 = i32_load8_u(var1 + 333)
        var42 = i32_load8_u(var1 + 334)
        var43 = i32_load8_u(var1 + 336)
        var55 = i64_load(var1 + 284)
        var56 = i64_load(var1 + 292)
        var44 = i32_load(var1 + 300)
        var45 = i32_load(var1 + 308)
        var46 = i32_load(var1 + 312)
        var47 = i32_load(var1 + 324)
        var48 = i32_load(var1 + 320)
        var49 = i32_load(var1 + 340)
        var50 = i32_load(var1 + 344)
        var51 = i32_load(var1 + 348)
        var52 = i32_load(var1 + 304)
        var53 = i32_load(var1 + 316)
        var54 = i32_load8_u(var1 + 352)
        var0 = (var5 + (var12 * 240))
        i32_store((var5 + (var12 * 240)) + 212, i32_load8_u(var1 + 354))
        i32_store(var0 + 208, var54)
        i32_store(var0 + 204, var53)
        i32_store(var0 + 200, var52)
        i32_store(var0 + 196, var51)
        i32_store(var0 + 192, var50)
        i32_store(var0 + 188, var49)
        i32_store(var0 + 184, var48)
        i32_store(var0 + 180, var47)
        i32_store(var0 + 176, var46)
        i32_store(var0 + 172, var45)
        i32_store(var0 + 168, var44)
        i64_store(var0 + 160, var56)
        i64_store(var0 + 152, var55)
        i32_store(var0 + 148, var43)
        i32_store(var0 + 144, var42)
        i32_store(var0 + 140, var41)
        i32_store(var0 + 136, var40)
        i32_store(var0 + 132, var39)
        i32_store(var0 + 128, var38)
        i32_store(var0 + 124, var37)
        i32_store(var0 + 120, var2)
        i32_store(var0 + 116, var36)
        i32_store(var0 + 112, var35)
        i32_store(var0 + 108, var34)
        i32_store(var0 + 104, var33)
        i32_store(var0 + 100, var32)
        i32_store(var0 + 96, var31)
        i32_store(var0 + 92, var30)
        i32_store(var0 + 88, var29)
        i32_store(var0 + 84, var28)
        i32_store(var0 + 80, var27)
        i32_store(var0 + 76, var26)
        i32_store(var0 + 72, var25)
        i32_store(var0 + 68, var24)
        i32_store(var0 + 64, var23)
        i32_store(var0 + 60, var22)
        i32_store(var0 + 56, var21)
        i32_store(var0 + 52, var20)
        i32_store(var0 + 48, var19)
        i32_store(var0 + 44, var18)
        i32_store(var0 + 40, var17)
        i32_store(var0 + 36, var16)
        i32_store(var0 + 32, var15)
        i32_store(var0 + 28, var14)
        i32_store(var0 + 24, var11)
        i32_store(var0 + 20, var9)
        i32_store(var0 + 16, var8)
        i32_store(var0 + 12, var7)
        i32_store(var0 + 8, var6)
        i32_store(var0 + 4, var4)
        i32_store(var0, var10)
        i64_store(var0 + 232, 0)
        i64_store(var0 + 224, 0)
        i64_store(var0 + 216, 0)
        var2 = i32_load(var1 + 236)
        if (1 if i32_load(var1 + 236) == 0 else 0):
            break
        var8 = (var2 & 3)
        var0 = i32_load(var1 + 232)
        var4 = 0
        if (1 if var2 < 4 else 0):
            var2 = 0
            break
        var11 = (var2 & -4)
        var2 = 0
        var9 = 0
        while True:  # loop $label9
            var6 = (var5 + (var3 << 2))
            var7 = (var2 << 2)
            i32_store((var5 + (var3 << 2)), i32_load((var0 + (var2 << 2))))
            i32_store(var6 + 4, i32_load((var0 + (var7 | 4))))
            i32_store(var6 + 8, i32_load((var0 + (var7 | 8))))
            i32_store(var6 + 12, i32_load((var0 + (var7 | 12))))
            var2 = (var2 + 4)
            var3 = (var3 + 4)
            var9 = (var9 + 4)
            if (1 if (var9 + 4) != var11 else 0):
                continue
            break  # end loop
        if (1 if var8 == 0 else 0):
            break
        while True:  # loop $label10
            i32_store((var5 + (var3 << 2)), i32_load((var0 + (var2 << 2))))
            var2 = (var2 + 1)
            var3 = (var3 + 1)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var8 else 0):
                continue
            break  # end loop
        var0 = i32_load(var1 + 364)
        if (1 if i32_load(var1 + 364) == 0 else 0):
            break
        var7 = (var0 & 3)
        var1 = i32_load(var1 + 24)
        var8 = 0
        if (1 if var0 < 4 else 0):
            var2 = 0
            break
        var9 = (var0 & -4)
        var2 = 0
        var4 = 0
        while True:  # loop $label13
            var0 = (var5 + (var3 << 2))
            var6 = (var2 << 2)
            i32_store((var5 + (var3 << 2)), i32_load((var1 + (var2 << 2))))
            i32_store(var0 + 4, i32_load((var1 + (var6 | 4))))
            i32_store(var0 + 8, i32_load((var1 + (var6 | 8))))
            i32_store(var0 + 12, i32_load((var1 + (var6 | 12))))
            var2 = (var2 + 4)
            var3 = (var3 + 4)
            var4 = (var4 + 4)
            if (1 if (var4 + 4) != var9 else 0):
                continue
            break  # end loop
        if (1 if var7 == 0 else 0):
            break
        while True:  # loop $label14
            i32_store((var5 + (var3 << 2)), i32_load((var1 + (var2 << 2))))
            var2 = (var2 + 1)
            var3 = (var3 + 1)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != var7 else 0):
                continue
            break  # end loop
        var2 = 0
        while True:  # loop $label15
            var1 = i32_load((var13 + (var2 << 2)))
            if (1 if i32_load((var13 + (var2 << 2))) != 100 else 0):
                var0 = (var5 + (var3 << 2))
                i32_store((var5 + (var3 << 2)), var2)
                i32_store(var0 + 4, var1)
                var3 = (var3 + 2)
            var1 = (var2 | 1)
            if (1 if (var2 | 1) != 255 else 0):
                var0 = i32_load((var13 + (var1 << 2)))
                if (1 if i32_load((var13 + (var1 << 2))) != 100 else 0):
                    var4 = (var5 + (var3 << 2))
                    i32_store((var5 + (var3 << 2)), var1)
                    i32_store(var4 + 4, var0)
                    var3 = (var3 + 2)
                var2 = (var2 + 2)
                continue
            break  # end loop
        var12 = (var12 + 1)
        var10 = (var10 + 1)
        if (1 if (var10 + 1) != 255 else 0):
            continue
        break  # end loop
    return (var12 * 60)


# ==========================================================
# $Ud
# Export: Ud
# ==========================================================
def Ud(var0):
    """Export: Ud"""
    var1 = 0
    if (1 if var0 != 2147483647 else 0):
        if var0:
            break
        return i32_load(9142908)
    return 0
    var1 = i32_load(9142908)
    if i32_load(9142908):
        i32_store(9142908, 0)
    i32_store(9142912, var0)
    var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    i32_store(9142908, func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2))))
    return var0

