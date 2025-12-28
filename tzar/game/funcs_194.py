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
# $rd
# Export: rd
# ==========================================================
def rd(var0, var1, var2, var3, var4):
    """Export: rd"""
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
    var7 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    i32_store(9163784, var1)
    i32_store(9163788, var1)
    i32_store8(9142906, var4)
    i32_store8(59181, (1 if var2 == 3 else 0))
    i32_store8(9568060, (1 if var3 != 0 else 0))
    var1 = i32_load8_u(9142916)
    f32_store(9671164, (1.0 if i32_load8_u(9142916) else var0))
    if (1 if var2 <= 2 else 0):
        i32_store(51788, i32_load(((var2 << 2) + 10152)))
    if var1:
        var4 = (global0 - 16)
        global global0
        global0 = (global0 - 16)
        var1 = func26(8160)
        while True:  # loop $label0
            var2 = (var5 << 2)
            var3 = ((var6 * 404) + 9568096)
            i32_store((var1 + (var5 << 2)), i32_load(((var6 * 404) + 9568096) + 200))
            i32_store((var1 + (var2 | 4)), i32_load(var3 + 216))
            i32_store((var1 + (var2 | 8)), i32_load(var3 + 220))
            i32_store((var1 + (var2 | 12)), (1 if (i32_load(var3 + 264) & -5) == 0 else 0))
            i32_store((var1 + (var2 | 16)), i32_load(var3 + 384))
            i32_store((var1 + (var2 | 20)), i32_load(var3 + 388))
            i32_store((var1 + (var2 | 24)), i32_load(var3 + 392))
            i32_store((var1 + (var2 | 28)), i32_load(var3 + 396))
            var5 = (var5 + 8)
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != 255 else 0):
                continue
            break  # end loop
        i32_store(var4 + 4, 2040)
        i32_store(var4, var1)
        global global0
        global0 = (var4 + 16)
    func320(0)
    if i32_load8_u(9147212):
        if (1 if i32_load8_u(9147152) == 0 else 0):
            break
        var1 = i32_load(9561752)
        if (1 if i32_load(9561752) == 0 else 0):
            break
        if (1 if var1 == i32_load(9561756) else 0):
            break
        i32_store(9147288, 0)
        i32_store(9142892, 0)
        break
        func319()
        break
    var1 = i32_load(9671136)
    if (1 if i32_load(9671136) < 4 else 0):
        break
    var4 = i32_load(9671128)
    var2 = 3
    while True:  # loop $label6
        var3 = (var4 + (var2 * 132))
        if (1 if i32_load8_u((var4 + (var2 * 132)) + 125) == 3 else 0):
            break
        if (1 if i32_load(var3 + 28) == 0 else 0):
            break
        if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
            break
        var1 = i32_load(9671136)
        var4 = i32_load(9671128)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var1 else 0):
            continue
        break  # end loop
    var2 = 3
    if (1 if var1 <= 3 else 0):
        break
    while True:  # loop $label14
        var3 = (var4 + (var2 * 132))
        if (1 if i32_load8_u((var4 + (var2 * 132)) + 125) == 3 else 0):
            break
        if (1 if i32_load(var3 + 28) == 0 else 0):
            break
        var5 = 0
        var6 = i32_load8_u(var3 + 122)
        var1 = i32_load(i32_load(9142424) + 48)
        if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
            break
        var4 = i32_load(((var6 * 404) + 9568096) + 216)
        if (1 if i32_load(((var6 * 404) + 9568096) + 216) == 0 else 0):
            break
        if i32_load8_u(9147152):
            break
        var9 = i32_load(9142440)
        var12 = i32_load(9147376)
        var13 = i32_load16_u(var3 + 112)
        var8 = i32_load16_u(var3 + 114)
        if (1 if var1 == 2 else 0):
            while True:  # loop $label11
                var14 = (var5 + var13)
                var1 = 0
                while True:  # loop $label10
                    if (1 if i32_load16_u((var12 + ((var14 + (var9 * (var1 + var8))) << 1))) > 1 else 0):
                        break
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) != var4 else 0):
                        continue
                    break  # end loop
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var4 else 0):
                    continue
                break
                break  # end loop
            raise RuntimeError('unreachable')
        while True:  # loop $label13
            var14 = (var5 + var13)
            var1 = 0
            while True:  # loop $label12
                if i32_load16_u((var12 + ((var14 + (var9 * (var1 + var8))) << 1))):
                    break
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var4 else 0):
                    continue
                break  # end loop
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var4 else 0):
                continue
            break  # end loop
        break
        var1 = i32_load(9671136)
        var4 = i32_load(9671128)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var1 else 0):
            continue
        break  # end loop
    if (1 if i32_load(9142892) == 0 else 0):
        break
    var3 = i32_load(9142424)
    var4 = i32_load(9561692)
    var1 = 0
    while True:  # loop $label15
        var2 = (var4 + (var1 * 286704))
        i32_store((var4 + (var1 * 286704)) + 283868, i32_load(9561460))
        # Unknown: memory.copy []
        i32_store((var2 + 284000), i32_load(var3 + 40))
        i32_store((var2 + 284136), i32_load(var3 + 36))
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    var4 = 0
    var3 = i32_load(9140328)
    if (1 if i32_load(9140328) == 0 else 0):
        break
    var1 = i32_load(9142440)
    var1 = (i32_load(9142440) * var1)
    var2 = 0
    if (1 if var3 >= 4 else 0):
        var6 = (var3 & -4)
        while True:  # loop $label17
            var5 = (var2 << 2)
            var4 = ((((var1 * i32_load(i32_load((((var2 << 2) | 12) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + ((((((var1 * i32_load(i32_load((var5 + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + var4) + (((var1 * i32_load(i32_load(((var5 | 4) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)) + (((var1 * i32_load(i32_load(((var5 | 8) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)))
            var2 = (var2 + 4)
            var10 = (var10 + 4)
            if (1 if (var10 + 4) != var6 else 0):
                continue
            break  # end loop
    var3 = (var3 & 3)
    if (1 if (var3 & 3) == 0 else 0):
        break
    while True:  # loop $label18
        var4 = ((((var1 * i32_load(i32_load(((var2 << 2) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + var4)
        var2 = (var2 + 1)
        var11 = (var11 + 1)
        if (1 if (var11 + 1) != var3 else 0):
            continue
        break  # end loop
    var1 = i32_load(9681936)
    if (1 if i32_load(9681936) == 0 else 0):
        var1 = func26(16)
        var2 = (var4 << 2)
        i32_store(func26(16) + 4, (var4 << 2))
        i32_store(var1, func26((-1 if (1 if var2 > 1073741823 else 0) else (var4 << 4))))
        i64_store(var1 + 8, 206158430208)
        i32_store(9681936, var1)
    if (1 if (i32_load8_u(9147212) | i32_load8_u(9147152)) == 0 else 0):
        func169()
        break
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    var5 = i32_load(var1)
    var10 = i32_load(9684500)
    var3 = i32_load(9684496)
    var11 = 0
    while True:  # loop $label24
        var6 = (var11 << 2)
        var9 = i32_load((var5 + (var11 << 2)))
        var12 = i32_load((var5 + (var6 | 8)))
        var13 = i32_load((var5 + (var6 | 4)))
        var2 = 0
        var8 = i32_load((var3 - 16))
        if i32_load((var3 - 16)):
            while True:  # loop $label21
                var4 = (var3 + (var2 * 60))
                if (1 if i32_load((var3 + (var2 * 60)) + 52) == var9 else 0):
                    break
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != var8 else 0):
                    continue
                break  # end loop
        var2 = 0
        var8 = i32_load((var10 - 16))
        if (1 if i32_load((var10 - 16)) == 0 else 0):
            break
        while True:  # loop $label23
            var4 = (var10 + (var2 * 60))
            if (1 if i32_load((var10 + (var2 * 60)) + 52) == var9 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var8 else 0):
                continue
            break  # end loop
        break
        var2 = func370(var4, var13, var12)
        var1 = i32_load(9681936)
        var5 = i32_load(i32_load(9681936))
        i32_store((i32_load(i32_load(9681936)) + (var6 | 12)), var2)
        var10 = i32_load(9684500)
        var3 = i32_load(9684496)
        var11 = (var11 + 4)
        if (1 if (var11 + 4) < i32_load(var1 + 8) else 0):
            continue
        break  # end loop
    if (1 if i32_load8_u(9147212) == 0 else 0):
        break
    if (1 if i32_load(i32_load(9142424) + 32) == 0 else 0):
        break
    var1 = i32_load(9684368)
    i32_store(var7 + 24, i32_load(9684368))
    i32_store(var7 + 60, i32_load(9684364))
    var0 = f32_load(9684356)
    f64_store(var7 + 16, float(f32_load(9684356)))
    i32_store(var7 + 56, (i32_load(9684372) - var1))
    var15 = f32_load(9684340)
    f64_store(var7 + 32, float((f32_load(9684348) - f32_load(9684340))))
    var16 = f32_load(9684344)
    f64_store(var7 + 40, float((f32_load(9684352) - f32_load(9684344))))
    f64_store(var7 + 48, float((f32_load(9684360) - var0)))
    f64_store(var7, float(var15))
    f64_store(var7 + 8, float(var16))
    a_b()
    func152()
    global global0
    global0 = (var7 - -64)


# ==========================================================
# $func743
# ==========================================================
def func743(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0.0
    var7 = 0.0
    var8 = 0.0
    if (1 if i32_load(9671176) == 0 else 0):
        break
    if i32_load(9671192):
        var0 = 0
        while True:  # loop $label1
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
    if i32_load(9681456):
        var3 = i32_load(9681448)
        while True:  # loop $label3
            var5 = i32_load((var3 + (var4 << 2)))
            var0 = i32_load(9671176)
            if (1 if i32_load(9671176) != i32_load(9671172) else 0):
                var1 = i32_load(9671168)
                break
            var1 = (i32_load(9671180) + var0)
            i32_store(9671172, (i32_load(9671180) + var0))
            var2 = i32_load(9671168)
            var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
            if var0:
                # Unknown: memory.copy []
            if var2:
                var3 = i32_load(9681448)
                var0 = i32_load(9671176)
            i32_store(9671168, var1)
            i32_store(9671176, (var0 + 1))
            i32_store((var1 + (var0 << 2)), var5)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < i32_load(9681456) else 0):
                continue
            break  # end loop
    var6 = float(i32_load(9142860))
    var6 = f32_load(40616)
    var8 = f32_load(9671164)
    var7 = (((float(i32_load(9142860)) - ((var6 * f32_load(40616)) / f32_load(9671164))) * 0.5) + ((var6 * float(i32_load(9681444))) + float(i32_load(9142956))))
    if (1 if abs((((float(i32_load(9142860)) - ((var6 * f32_load(40616)) / f32_load(9671164))) * 0.5) + ((var6 * float(i32_load(9681444))) + float(i32_load(9142956))))) < 2147483650.0 else 0):
        break
    var0 = -2147483648
    var7 = float(i32_load(9142856))
    var6 = (((var6 * float(i32_load(9681440))) + float(i32_load(9142952))) + ((float(i32_load(9142856)) - ((var6 * var7) / var8)) * 0.5))
    if (1 if abs((((var6 * float(i32_load(9681440))) + float(i32_load(9142952))) + ((float(i32_load(9142856)) - ((var6 * var7) / var8)) * 0.5))) < 2147483650.0 else 0):
        return func132(int(var6), var0)
    return func132(-2147483648, var0)


# ==========================================================
# $Ye
# Export: Ye
# ==========================================================
def Ye():
    """Export: Ye"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var5 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = i32_load(9684496)
    var1 = i32_load((i32_load(9684496) - 16))
    if (1 if i32_load((i32_load(9684496) - 16)) == 0 else 0):
        break
    if (1 if var1 >= 4 else 0):
        var4 = (var1 & -4)
        while True:  # loop $label1
            var2 = ((var0 * 60) + var3)
            i32_store(((var0 * 60) + var3) + 208, 2147483647)
            i32_store(var2 + 148, 2147483647)
            i32_store(var2 + 88, 2147483647)
            i32_store(var2 + 28, 2147483647)
            var0 = (var0 + 4)
            var6 = (var6 + 4)
            if (1 if (var6 + 4) != var4 else 0):
                continue
            break  # end loop
    var2 = (var1 & 3)
    if (1 if (var1 & 3) == 0 else 0):
        break
    var1 = 0
    while True:  # loop $label2
        i32_store(((var0 * 60) + var3) + 28, 2147483647)
        var0 = (var0 + 1)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var2 else 0):
            continue
        break  # end loop
    i32_store(9140308, 0)
    hd()
    func319()
    var0 = i32_load(9142440)
    var0 = (i32_load(9142440) * var0)
    i32_store(9142400, func26((-1 if (var0 & 805306368) else ((i32_load(9142440) * var0) << 4))))
    var1 = 0
    var3 = i32_load(9140328)
    if (1 if i32_load(9140328) == 0 else 0):
        break
    var6 = 0
    var0 = i32_load(9142440)
    var2 = (i32_load(9142440) * var0)
    var0 = 0
    if (1 if var3 >= 4 else 0):
        var7 = (var3 & -4)
        while True:  # loop $label4
            var4 = (var0 << 2)
            var1 = ((((var2 * i32_load(i32_load((((var0 << 2) | 12) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + ((((((var2 * i32_load(i32_load((var4 + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + var1) + (((var2 * i32_load(i32_load(((var4 | 4) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)) + (((var2 * i32_load(i32_load(((var4 | 8) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)))
            var0 = (var0 + 4)
            var8 = (var8 + 4)
            if (1 if (var8 + 4) != var7 else 0):
                continue
            break  # end loop
    var3 = (var3 & 3)
    if (1 if (var3 & 3) == 0 else 0):
        break
    while True:  # loop $label5
        var1 = ((((var2 * i32_load(i32_load(((var0 << 2) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + var1)
        var0 = (var0 + 1)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) != var3 else 0):
            continue
        break  # end loop
    if (1 if i32_load(9681936) == 0 else 0):
        var0 = func26(16)
        var2 = (var1 << 2)
        i32_store(func26(16) + 4, (var1 << 2))
        i32_store(var0, func26((-1 if (1 if var2 > 1073741823 else 0) else (var1 << 4))))
        i64_store(var0 + 8, 206158430208)
        i32_store(9681936, var0)
    i32_store8(59182, 0)
    if (1 if i32_load8_u(9142917) == 0 else 0):
        var0 = (i32_load(9142440) << 4)
        i32_store(var5, (i32_load(9142440) << 4))
        i32_store(var5 + 4, var0)
    global global0
    global0 = (var5 + 16)

