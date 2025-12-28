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
# $Zd
# Export: Zd
# ==========================================================
def Zd():
    """Export: Zd"""
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
    while True:  # loop $label1
        var3 = ((var1 * 404) + 9568096)
        if (1 if i32_load(((var1 * 404) + 9568096) + 264) == 1 else 0):
            var0 = (((i32_load(var3 + 364) + (var0 + i32_load(var3 + 236))) + (i32_load(var3 + 220) * i32_load(var3 + 216))) + 56)
            var3 = 0
            while True:  # loop $label0
                var0 = (((var1 * 1020) + 9299904) + (var3 << 2))
                var6 = (var0 if (1 if i32_load((((var1 * 1020) + 9299904) + (var3 << 2))) == 100 else 0) else (var0 + 2))
                var6 = ((var0 if (1 if i32_load((((var1 * 1020) + 9299904) + (var3 << 2))) == 100 else 0) else (var0 + 2)) if (1 if i32_load(var0 + 4) == 100 else 0) else (var6 + 2))
                var0 = (((var0 if (1 if i32_load((((var1 * 1020) + 9299904) + (var3 << 2))) == 100 else 0) else (var0 + 2)) if (1 if i32_load(var0 + 4) == 100 else 0) else (var6 + 2)) if (1 if i32_load(var0 + 8) == 100 else 0) else (var6 + 2))
                var3 = (var3 + 3)
                if (1 if (var3 + 3) != 255 else 0):
                    continue
                break  # end loop
            var2 = (var2 + 1)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != 255 else 0):
            continue
        break  # end loop
    var3 = i32_load(9685864)
    if i32_load(9685864):
        i32_store(9685864, 0)
    var3 = (var2 * 56)
    var6 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    i32_store(9685864, func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2))))
    while True:  # loop $label16
        var1 = 0
        var0 = 0
        var2 = ((var11 * 404) + 9568096)
        if (1 if i32_load(((var11 * 404) + 9568096) + 264) == 1 else 0):
            while True:  # loop $label2
                var15 = ((var11 * 1020) + 9299904)
                var0 = (((var11 * 1020) + 9299904) + (var1 << 2))
                var4 = (var0 if (1 if i32_load((((var11 * 1020) + 9299904) + (var1 << 2))) == 100 else 0) else (var0 + 2))
                var4 = ((var0 if (1 if i32_load((((var11 * 1020) + 9299904) + (var1 << 2))) == 100 else 0) else (var0 + 2)) if (1 if i32_load(var0 + 4) == 100 else 0) else (var4 + 2))
                var0 = (((var0 if (1 if i32_load((((var11 * 1020) + 9299904) + (var1 << 2))) == 100 else 0) else (var0 + 2)) if (1 if i32_load(var0 + 4) == 100 else 0) else (var4 + 2)) if (1 if i32_load(var0 + 8) == 100 else 0) else (var4 + 2))
                var1 = (var1 + 3)
                if (1 if (var1 + 3) != 255 else 0):
                    continue
                break  # end loop
            var10 = i32_load(var2 + 104)
            var12 = i32_load(var2 + 68)
            var14 = i32_load(var2 + 72)
            var16 = i32_load(var2 + 76)
            var17 = i32_load(var2 + 80)
            var18 = i32_load(var2 + 116)
            var4 = i32_load(var2 + 236)
            var19 = i32_load(var2 + 92)
            var20 = i32_load(var2 + 276)
            var21 = i32_load(var2 + 224)
            var22 = i32_load(var2 + 204)
            var23 = i32_load(var2 + 200)
            var24 = i32_load(var2 + 228)
            var25 = i32_load(var2 + 208)
            var5 = i32_load(var2 + 220)
            var7 = i32_load(var2 + 216)
            var8 = i32_load(var2 + 192)
            var26 = i32_load(var2 + 188)
            var27 = i32_load(var2 + 84)
            var28 = i32_load(var2 + 136)
            var29 = i32_load(var2 + 140)
            var30 = i32_load(var2 + 176)
            var9 = i32_load(var2 + 364)
            var31 = i32_load(var2 + 272)
            var32 = i32_load(var2 + 212)
            var1 = (var6 + (var13 * 224))
            i32_store((var6 + (var13 * 224)) + 108, var0)
            i32_store(var1 + 104, var32)
            i32_store(var1 + 100, var31)
            i32_store(var1 + 96, var9)
            i32_store(var1 + 92, var30)
            i32_store(var1 + 88, var29)
            i32_store(var1 + 84, var28)
            i32_store(var1 + 80, var27)
            i32_store(var1 + 76, var26)
            i32_store(var1 + 72, var8)
            var8 = (var5 * var7)
            i32_store(var1 + 68, (var5 * var7))
            i32_store(var1 + 64, var5)
            i32_store(var1 + 60, var7)
            i32_store(var1 + 56, var25)
            i32_store(var1 + 52, var24)
            i32_store(var1 + 48, var23)
            i32_store(var1 + 44, var22)
            i32_store(var1 + 40, var21)
            i32_store(var1 + 36, var20)
            i32_store(var1 + 32, var19)
            i32_store(var1 + 28, var4)
            i32_store(var1 + 24, var18)
            i32_store(var1 + 20, var17)
            i32_store(var1 + 16, var16)
            i32_store(var1 + 12, var14)
            i32_store(var1 + 8, var12)
            i32_store(var1 + 4, var10)
            i32_store(var1, var11)
            # Unknown: memory.fill []
            if (1 if var4 == 0 else 0):
                break
            var10 = (var4 & 3)
            var5 = i32_load(var2 + 232)
            var1 = 0
            if (1 if var4 < 4 else 0):
                var0 = 0
                break
            var14 = (var4 & -4)
            var0 = 0
            var12 = 0
            while True:  # loop $label5
                var4 = (var6 + (var3 << 2))
                var7 = (var0 << 2)
                i32_store((var6 + (var3 << 2)), i32_load((var5 + (var0 << 2))))
                i32_store(var4 + 4, i32_load((var5 + (var7 | 4))))
                i32_store(var4 + 8, i32_load((var5 + (var7 | 8))))
                i32_store(var4 + 12, i32_load((var5 + (var7 | 12))))
                var0 = (var0 + 4)
                var3 = (var3 + 4)
                var12 = (var12 + 4)
                if (1 if (var12 + 4) != var14 else 0):
                    continue
                break  # end loop
            if (1 if var10 == 0 else 0):
                break
            while True:  # loop $label6
                i32_store((var6 + (var3 << 2)), i32_load((var5 + (var0 << 2))))
                var0 = (var0 + 1)
                var3 = (var3 + 1)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var10 else 0):
                    continue
                break  # end loop
            if (1 if var8 == 0 else 0):
                break
            var7 = (var8 & 3)
            var4 = i32_load(var2 + 372)
            var10 = 0
            if (1 if var8 < 4 else 0):
                var0 = 0
                break
            var8 = (var8 & -4)
            var0 = 0
            var1 = 0
            while True:  # loop $label9
                var5 = (var6 + (var3 << 2))
                i32_store((var6 + (var3 << 2)), i32_load8_u((var0 + var4)))
                i32_store(var5 + 4, i32_load8_u((var4 + (var0 | 1))))
                i32_store(var5 + 8, i32_load8_u((var4 + (var0 | 2))))
                i32_store(var5 + 12, i32_load8_u((var4 + (var0 | 3))))
                var0 = (var0 + 4)
                var3 = (var3 + 4)
                var1 = (var1 + 4)
                if (1 if (var1 + 4) != var8 else 0):
                    continue
                break  # end loop
            if (1 if var7 == 0 else 0):
                break
            while True:  # loop $label10
                i32_store((var6 + (var3 << 2)), i32_load8_u((var0 + var4)))
                var0 = (var0 + 1)
                var3 = (var3 + 1)
                var10 = (var10 + 1)
                if (1 if (var10 + 1) != var7 else 0):
                    continue
                break  # end loop
            if (1 if var9 == 0 else 0):
                break
            var5 = (var9 & 3)
            var2 = i32_load(var2 + 24)
            var8 = 0
            if (1 if var9 < 4 else 0):
                var0 = 0
                break
            var7 = (var9 & -4)
            var0 = 0
            var1 = 0
            while True:  # loop $label13
                var4 = (var6 + (var3 << 2))
                var9 = (var0 << 2)
                i32_store((var6 + (var3 << 2)), i32_load((var2 + (var0 << 2))))
                i32_store(var4 + 4, i32_load((var2 + (var9 | 4))))
                i32_store(var4 + 8, i32_load((var2 + (var9 | 8))))
                i32_store(var4 + 12, i32_load((var2 + (var9 | 12))))
                var0 = (var0 + 4)
                var3 = (var3 + 4)
                var1 = (var1 + 4)
                if (1 if (var1 + 4) != var7 else 0):
                    continue
                break  # end loop
            if (1 if var5 == 0 else 0):
                break
            while True:  # loop $label14
                i32_store((var6 + (var3 << 2)), i32_load((var2 + (var0 << 2))))
                var0 = (var0 + 1)
                var3 = (var3 + 1)
                var8 = (var8 + 1)
                if (1 if (var8 + 1) != var5 else 0):
                    continue
                break  # end loop
            var0 = 0
            while True:  # loop $label15
                var2 = i32_load((var15 + (var0 << 2)))
                if (1 if i32_load((var15 + (var0 << 2))) != 100 else 0):
                    var1 = (var6 + (var3 << 2))
                    i32_store((var6 + (var3 << 2)), var0)
                    i32_store(var1 + 4, var2)
                    var3 = (var3 + 2)
                var2 = (var0 | 1)
                if (1 if (var0 | 1) != 255 else 0):
                    var1 = i32_load((var15 + (var2 << 2)))
                    if (1 if i32_load((var15 + (var2 << 2))) != 100 else 0):
                        var4 = (var6 + (var3 << 2))
                        i32_store((var6 + (var3 << 2)), var2)
                        i32_store(var4 + 4, var1)
                        var3 = (var3 + 2)
                    var0 = (var0 + 2)
                    continue
                break  # end loop
            var13 = (var13 + 1)
        var11 = (var11 + 1)
        if (1 if (var11 + 1) != 255 else 0):
            continue
        break  # end loop
    return (var13 * 56)


# ==========================================================
# $Mc
# Export: Mc
# ==========================================================
def Mc(var0):
    """Export: Mc"""
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
    var10 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    var3 = func26(4)
    var7 = func26(4)
    var8 = func26(4)
    var9 = func26(4)
    var1 = i32_load(9568076)
    if (1 if var0 == 1 else 0):
        var0 = i32_load(var1 + 16)
        if (1 if i32_load(var1 + 16) != i32_load(var1 + 20) else 0):
            i64_store(var0, 0)
            i32_store(var0 + 108, 1)
            i64_store(var0 + 100, 1)
            i32_store(var0 + 96, var9)
            i32_store(var0 + 92, 1)
            i64_store(var0 + 84, 1)
            i32_store(var0 + 80, var8)
            i32_store(var0 + 76, 1)
            i64_store(var0 + 68, 1)
            i32_store(var0 + 64, var7)
            i32_store(var0 + 60, 1)
            i64_store(var0 + 52, 1)
            i32_store(var0 + 48, var3)
            i64_store(var0 + 39, 0)
            i64_store(var0 + 32, 0)
            i64_store(var0 + 24, 0)
            i64_store(var0 + 16, 0)
            i64_store(var0 + 8, 0)
            # Unknown: memory.copy []
            i32_store(var0 + 192, 0)
            var0 = (var0 + 196)
            i32_store(var1 + 16, (var0 + 196))
            break
        var4 = i32_load((var1 + 12))
        var6 = (var0 - i32_load((var1 + 12)))
        var0 = ((var0 - i32_load((var1 + 12))) // 196)
        var2 = (((var0 - i32_load((var1 + 12))) // 196) + 1)
        if (1 if (((var0 - i32_load((var1 + 12))) // 196) + 1) >= 21913099 else 0):
            break
        var11 = (var0 << 1)
        var2 = (21913098 if (1 if var0 >= 10956549 else 0) else ((var0 << 1) if (1 if var2 < var11 else 0) else var2))
        if (21913098 if (1 if var0 >= 10956549 else 0) else ((var0 << 1) if (1 if var2 < var11 else 0) else var2)):
            if (1 if var2 >= 21913099 else 0):
                break
            var5 = func26((var2 * 196))
        var0 = (var5 + (var0 * 196))
        i64_store((var5 + (var0 * 196)), 0)
        i32_store(var0 + 192, 0)
        i32_store(var0 + 108, 1)
        i64_store(var0 + 100, 1)
        i32_store(var0 + 96, var9)
        i32_store(var0 + 92, 1)
        i64_store(var0 + 84, 1)
        i32_store(var0 + 80, var8)
        i32_store(var0 + 76, 1)
        i64_store(var0 + 68, 1)
        i32_store(var0 + 64, var7)
        i32_store(var0 + 60, 1)
        i64_store(var0 + 52, 1)
        i32_store(var0 + 48, var3)
        i64_store(var0 + 39, 0)
        i64_store(var0 + 32, 0)
        i64_store(var0 + 24, 0)
        i64_store(var0 + 16, 0)
        i64_store(var0 + 8, 0)
        var3 = (var0 + ((var6 // -196) * 196))
        # Unknown: memory.copy []
        i32_store(var1 + 20, (var5 + (var2 * 196)))
        var0 = (var0 + 196)
        i32_store(var1 + 16, (var0 + 196))
        i32_store(var1 + 12, var3)
        if (1 if var4 == 0 else 0):
            break
        var1 = i32_load(9568076)
        var0 = i32_load(i32_load(9568076) + 16)
        var1 = (var1 + 12)
        break
    var0 = i32_load(var1 + 4)
    if (1 if i32_load(var1 + 4) != i32_load(var1 + 8) else 0):
        i64_store(var0, 0)
        i32_store(var0 + 108, 1)
        i64_store(var0 + 100, 1)
        i32_store(var0 + 96, var9)
        i32_store(var0 + 92, 1)
        i64_store(var0 + 84, 1)
        i32_store(var0 + 80, var8)
        i32_store(var0 + 76, 1)
        i64_store(var0 + 68, 1)
        i32_store(var0 + 64, var7)
        i32_store(var0 + 60, 1)
        i64_store(var0 + 52, 1)
        i32_store(var0 + 48, var3)
        i64_store(var0 + 39, 0)
        i64_store(var0 + 32, 0)
        i64_store(var0 + 24, 0)
        i64_store(var0 + 16, 0)
        i64_store(var0 + 8, 0)
        # Unknown: memory.copy []
        i32_store(var0 + 192, 0)
        i32_store(var1 + 4, (var0 + 196))
        break
    var4 = i32_load(var1)
    var6 = (var0 - i32_load(var1))
    var0 = ((var0 - i32_load(var1)) // 196)
    var2 = (((var0 - i32_load(var1)) // 196) + 1)
    if (1 if (((var0 - i32_load(var1)) // 196) + 1) >= 21913099 else 0):
        break
    var11 = (var0 << 1)
    var2 = (21913098 if (1 if var0 >= 10956549 else 0) else ((var0 << 1) if (1 if var2 < var11 else 0) else var2))
    if (21913098 if (1 if var0 >= 10956549 else 0) else ((var0 << 1) if (1 if var2 < var11 else 0) else var2)):
        if (1 if var2 >= 21913099 else 0):
            break
        var5 = func26((var2 * 196))
    var0 = (var5 + (var0 * 196))
    i64_store((var5 + (var0 * 196)), 0)
    i32_store(var0 + 192, 0)
    i32_store(var0 + 108, 1)
    i64_store(var0 + 100, 1)
    i32_store(var0 + 96, var9)
    i32_store(var0 + 92, 1)
    i64_store(var0 + 84, 1)
    i32_store(var0 + 80, var8)
    i32_store(var0 + 76, 1)
    i64_store(var0 + 68, 1)
    i32_store(var0 + 64, var7)
    i32_store(var0 + 60, 1)
    i64_store(var0 + 52, 1)
    i32_store(var0 + 48, var3)
    i64_store(var0 + 39, 0)
    i64_store(var0 + 32, 0)
    i64_store(var0 + 24, 0)
    i64_store(var0 + 16, 0)
    i64_store(var0 + 8, 0)
    var3 = (var0 + ((var6 // -196) * 196))
    # Unknown: memory.copy []
    i32_store(var1 + 8, (var5 + (var2 * 196)))
    i32_store(var1 + 4, (var0 + 196))
    i32_store(var1, var3)
    if (1 if var4 == 0 else 0):
        break
    var1 = i32_load(9568076)
    var0 = i32_load(i32_load(9568076) + 4)
    var1 = i32_load(var1)
    global global0
    global0 = (var10 + 80)
    return (((var0 - var1) // 196) - 1)
    func42()
    raise RuntimeError('unreachable')
    func68()
    raise RuntimeError('unreachable')
    func42()
    raise RuntimeError('unreachable')
    return af(var4)


# ==========================================================
# $Ue
# Export: Ue
# ==========================================================
def Ue(var0, var1):
    """Export: Ue"""
    if (i32_load(9142912) if var0 else 1):
        var0 = i32_load(9142908)
        if i32_load(9142908):
            i32_store(9142908, 0)
        i32_store(9142912, 0)
        func272()
        func271()
        func220()
        func218()

