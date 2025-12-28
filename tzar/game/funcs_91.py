"""
Auto-generated from WAT. Contains 9 functions.
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
# $Nd
# Export: Nd
# ==========================================================
def Nd(var0):
    """Export: Nd"""
    var1 = 0
    i32_store8(9216068, var0)
    if var0:
        while True:  # loop $label0
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != 356 else 0):
                continue
            break  # end loop


# ==========================================================
# $func501
# ==========================================================
def func501(var0):
    var1 = 0
    var2 = 0
    if (1 if var0 == 0 else 0):
        break
    var1 = i32_load(9671128)
    var2 = (i32_load(9671128) + (var0 * 132))
    if i32_load8_u((i32_load(9143004) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u((i32_load(9671128) + (var0 * 132)) + 110))))):
        break
    # br_table ['$label0', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label0', '$label1']
    _br_idx = (i32_load8_u(var2 + 125) - 4)
    break  # br_table
    var1 = i32_load8_u((var1 + (var0 * 132)) + 122)
    if (1 if i32_load8_u((var1 + (var0 * 132)) + 122) == i32_load(38552) else 0):
        break
    if (1 if i32_load(38892) == var1 else 0):
        break
    if (1 if i32_load(38816) == var1 else 0):
        break
    if (1 if i32_load(38872) == var1 else 0):
        break
    if (1 if i32_load(38584) == var1 else 0):
        break
    if (1 if i32_load(38796) != var1 else 0):
        break
    i32_store((9681808 if i32_load8_u(9681824) else 9681812), var0)


# ==========================================================
# $nb
# Export: nb
# ==========================================================
def nb(var0):
    """Export: nb"""
    var1 = 0
    var2 = 0
    var1 = (i32_load(9671128) + (i32_load(9173808) * 132))
    var0 = i32_load(((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 110) * 286704)) + 284340))
    var2 = (i32_load(9681804) + ((var0 * i32_load(((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 110) * 286704)) + 284340))) * ((i32_load8_u(9163792) + 1) & 255)))
    i32_store(9681804, (i32_load(9681804) + ((var0 * i32_load(((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 110) * 286704)) + 284340))) * ((i32_load8_u(9163792) + 1) & 255))))
    var1 = i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 124)
    if (1 if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 124) >= var2 else 0):
        var1 = var0
        if (1 if var2 >= var0 else 0):
            break
    i32_store(9681804, var1)


# ==========================================================
# $func504
# ==========================================================
def func504(var0):
    var1 = 0
    var0 = i32_load((i32_load(9671128) + (i32_load(9173808) * 132)) + 20)
    if (1 if i32_load((i32_load(9671128) + (i32_load(9173808) * 132)) + 20) == 0 else 0):
        break
    if (1 if i32_load(var0 + 8) < 3 else 0):
        break
    var0 = i32_load(var0)
    if i32_load(i32_load(var0)):
        break
    i32_store(9681804, i32_load(var0 + 4))
    i32_store(9681808, i32_load(var0 + 8))
    i32_store(9681812, i32_load(var0 + 12))
    i32_store(9681816, i32_load(var0 + 16))
    var1 = i32_load(var0 + 20)
    break
    i32_store(9681804, 50)
    i32_store(9681808, 0)
    i32_store(9681812, 0)
    i32_store(9681816, 0)
    i32_store(9681820, var1)


# ==========================================================
# $tb
# Export: tb
# ==========================================================
def tb(var0):
    """Export: tb"""
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
    var0 = i32_load(9681844)
    if (1 if i32_load(9681844) == 0 else 0):
        var0 = 0
        while True:  # loop $label0
            var3 = ((var0 * 404) + 9568096)
            var1 = (i32_load(((var0 * 404) + 9568096) + 236) + 10)
            var3 = i32_load(var3 + 180)
            if i32_load(var3 + 180):
                var1 = (i32_load(var3 + 68) + var1)
            else:
            var7 = (0 + (var1 + var2))
            var2 = (var0 | 1)
            if (1 if (var0 | 1) != 255 else 0):
                var2 = ((var2 * 404) + 9568096)
                var1 = (i32_load(((var2 * 404) + 9568096) + 236) + 10)
                var0 = (var0 + 2)
                var2 = i32_load(var2 + 180)
                if i32_load(var2 + 180):
                    var1 = (i32_load(var2 + 68) + var1)
                else:
                var2 = (0 + (var1 + var7))
                continue
            break  # end loop
        var0 = 0
        i32_store(9681848, var7)
        var4 = func26((-1 if (1 if var7 > 1073741823 else 0) else (var7 << 2)))
        i32_store(9681844, func26((-1 if (1 if var7 > 1073741823 else 0) else (var7 << 2))))
        while True:  # loop $label9
            var2 = ((var8 * 404) + 9568096)
            var3 = i32_load(((var8 * 404) + 9568096) + 180)
            var1 = (var4 + (var0 << 2))
            i32_store((var4 + (var0 << 2)), var8)
            i32_store(var1 + 4, (i32_load(var2 + 144) * -48))
            i32_store(var1 + 8, i32_load(var2 + 84))
            i32_store(var1 + 12, i32_load(var2 + 196))
            i32_store(var1 + 16, i32_load(var2 + 264))
            var6 = (var0 + 5)
            if (1 if var3 == 0 else 0):
                i32_store((var4 + (var6 << 2)), 0)
                break
            i32_store((var4 + (var6 << 2)), i32_load(var3 + 8))
            i32_store(0 + 24, i32_load(var3 + 12))
            var1 = i32_load(var2 + 236)
            i32_store(var1 + 28, i32_load(var2 + 236))
            var0 = (var0 + 8)
            if (1 if var1 == 0 else 0):
                break
            var10 = (var1 & 3)
            var2 = i32_load(var2 + 232)
            var11 = 0
            if (1 if var1 < 4 else 0):
                var1 = 0
                break
            var13 = (var1 & -4)
            var1 = 0
            var12 = 0
            while True:  # loop $label4
                var6 = (var4 + (var0 << 2))
                var9 = (var1 << 2)
                i32_store((var4 + (var0 << 2)), i32_load((var2 + (var1 << 2))))
                i32_store(var6 + 4, i32_load((var2 + (var9 | 4))))
                i32_store(var6 + 8, i32_load((var2 + (var9 | 8))))
                i32_store(var6 + 12, i32_load((var2 + (var9 | 12))))
                var1 = (var1 + 4)
                var0 = (var0 + 4)
                var12 = (var12 + 4)
                if (1 if (var12 + 4) != var13 else 0):
                    continue
                break  # end loop
            if (1 if var10 == 0 else 0):
                break
            while True:  # loop $label5
                i32_store((var4 + (var0 << 2)), i32_load((var2 + (var1 << 2))))
                var1 = (var1 + 1)
                var0 = (var0 + 1)
                var11 = (var11 + 1)
                if (1 if (var11 + 1) != var10 else 0):
                    continue
                break  # end loop
            if (1 if var3 == 0 else 0):
                i64_store((var4 + (var0 << 2)), 0)
                var0 = (var0 + 2)
                break
            i32_store((var4 + (var0 << 2)), i32_load(var3 + 68))
            var2 = (var0 + 1)
            var1 = 0
            if i32_load(var3 + 68):
                while True:  # loop $label7
                    var0 = var2
                    i32_store((var4 + (var2 << 2)), i32_load((var3 + (var1 << 2)) + 28))
                    var2 = (var0 + 1)
                    var1 = (var1 + 1)
                    if (1 if (var1 + 1) < i32_load(var3 + 68) else 0):
                        continue
                    break  # end loop
            i32_store((var4 + (var2 << 2)), i32_load(var3 + 112))
            var0 = (var0 + 2)
            var1 = 0
            if (1 if i32_load(var3 + 112) == 0 else 0):
                break
            while True:  # loop $label8
                i32_store((var4 + (var0 << 2)), i32_load((var3 + (var1 << 2)) + 72))
                var0 = (var0 + 1)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) < i32_load(var3 + 112) else 0):
                    continue
                break  # end loop
            var8 = (var8 + 1)
            if (1 if (var8 + 1) != 255 else 0):
                continue
            break  # end loop
        var0 = i32_load((i32_load(9561692) + (i32_load(9142872) * 286704)) + 283960)
        i32_store(var5, var4)
        i32_store(var5 + 4, var7)
        i32_store(var5 + 8, var0)
        a_b()
        break
    var2 = i32_load((i32_load(9561692) + (i32_load(9142872) * 286704)) + 283960)
    i32_store(var5 + 16, var0)
    i32_store(var5 + 20, i32_load(9681848))
    i32_store(var5 + 24, var2)
    a_b()
    global global0
    global0 = (var5 + 32)
    return (var5 + 16)


# ==========================================================
# $Va
# Export: Va
# ==========================================================
def Va(var0, var1):
    """Export: Va"""
    var2 = 0
    var3 = 0
    var4 = 0
    var4 = (var0 * 20)
    var3 = func26((-1 if (1 if (var0 * 20) < 0 else 0) else (var0 * 40)))
    i32_store(((var1 << 2) + 9142928), func26((-1 if (1 if (var0 * 20) < 0 else 0) else (var0 * 40))))
    if var4:
        var0 = 0
        while True:  # loop $label0
            i32_store16((var3 + (var0 << 1)), i32_load(((var0 << 2) + 9147392)))
            var2 = (var0 | 1)
            i32_store16((var3 + ((var0 | 1) << 1)), i32_load(((var2 << 2) + 9147392)))
            var2 = (var0 | 2)
            i32_store16((var3 + ((var0 | 2) << 1)), i32_load(((var2 << 2) + 9147392)))
            var2 = (var0 | 3)
            i32_store16((var3 + ((var0 | 3) << 1)), i32_load(((var2 << 2) + 9147392)))
            var0 = (var0 + 4)
            if (1 if (var0 + 4) != var4 else 0):
                continue
            break  # end loop
    i32_store16(((var1 << 1) + 9142944), var4)


# ==========================================================
# $N
# Export: N
# ==========================================================
def N(var0, var1):
    """Export: N"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if (1 if var0 == 0 else 0):
        return (1 if i32_load8_u(9147209) != 0 else 0)
    i32_store8(9147209, var1)
    var0 = 0
    var2 = i32_load(9142892)
    var3 = (i32_load(9142892) * var2)
    var2 = func26((i32_load(9142892) * var2))
    # Unknown: memory.fill []
    i32_store(9143012, var2)
    if (1 if var3 == 0 else 0):
        break
    var4 = i32_load(9143004)
    if (1 if var3 >= 4 else 0):
        var7 = (var3 & -4)
        while True:  # loop $label1
            i32_store8((var0 + var2), (i32_load8_u((var0 + var4)) ^ 1))
            var5 = (var0 | 1)
            i32_store8((var2 + (var0 | 1)), (i32_load8_u((var4 + var5)) ^ 1))
            var5 = (var0 | 2)
            i32_store8((var2 + (var0 | 2)), (i32_load8_u((var4 + var5)) ^ 1))
            var5 = (var0 | 3)
            i32_store8((var2 + (var0 | 3)), (i32_load8_u((var4 + var5)) ^ 1))
            var0 = (var0 + 4)
            var6 = (var6 + 4)
            if (1 if (var6 + 4) != var7 else 0):
                continue
            break  # end loop
    var3 = (var3 & 3)
    if (1 if (var3 & 3) == 0 else 0):
        break
    var6 = 0
    while True:  # loop $label2
        i32_store8((var0 + var2), (i32_load8_u((var0 + var4)) ^ 1))
        var0 = (var0 + 1)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) != var3 else 0):
            continue
        break  # end loop
    return var1


# ==========================================================
# $Cb
# Export: Cb
# ==========================================================
def Cb():
    """Export: Cb"""
    var0 = 0
    var0 = (global0 - 192)
    global global0
    global0 = (global0 - 192)
    i32_store(var0 + 128, i32_load(38468))
    i32_store(var0 + 132, i32_load(38476))
    i32_store(var0 + 136, i32_load(38524))
    i32_store(var0 + 140, i32_load(38488))
    i32_store(var0 + 144, i32_load(38484))
    i32_store(var0 + 148, i32_load(38464))
    i32_store(var0 + 152, i32_load(38520))
    i32_store(var0 + 156, i32_load(38516))
    i32_store(var0 + 160, i32_load(38512))
    i32_store(var0 + 164, i32_load(38552))
    i32_store(var0 + 168, i32_load(38480))
    i32_store(var0 + 172, i32_load(38536))
    i32_store(var0 + 176, i32_load(38540))
    i32_store(var0 + 180, i32_load(38544))
    i32_store(var0 + 184, i32_load(38532))
    i32_store(var0 + 64, i32_load(38668))
    i32_store(var0 + 68, i32_load(38820))
    i32_store(var0 + 72, i32_load(38800))
    i32_store(var0 + 76, i32_load(38848))
    i32_store(var0 + 80, i32_load(38840))
    i32_store(var0 + 84, i32_load(38836))
    i32_store(var0 + 88, i32_load(38808))
    i32_store(var0 + 92, i32_load(38844))
    i32_store(var0 + 96, i32_load(38792))
    i32_store(var0 + 100, i32_load(38816))
    i32_store(var0 + 104, i32_load(38784))
    i32_store(var0 + 108, i32_load(38804))
    i32_store(var0 + 112, i32_load(38812))
    i32_store(var0 + 116, i32_load(38780))
    i32_store(var0 + 120, i32_load(38824))
    i32_store(var0, i32_load(38664))
    i32_store(var0 + 4, i32_load(38700))
    i32_store(var0 + 8, i32_load(38876))
    i32_store(var0 + 12, i32_load(38916))
    i32_store(var0 + 16, i32_load(38908))
    i32_store(var0 + 20, i32_load(38904))
    i32_store(var0 + 24, i32_load(38884))
    i32_store(var0 + 28, i32_load(38912))
    i32_store(var0 + 32, i32_load(38868))
    i32_store(var0 + 36, i32_load(38892))
    i32_store(var0 + 40, i32_load(38860))
    i32_store(var0 + 44, i32_load(38880))
    i32_store(var0 + 48, i32_load(38888))
    i32_store(var0 + 52, i32_load(38856))
    i32_store(var0 + 56, i32_load(38896))
    func259((var0 + 128), 0)
    func259((var0 - -64), 1)
    func259(var0, 2)
    global global0
    global0 = (var0 + 192)


# ==========================================================
# $func699
# ==========================================================
def func699(var0):
    i32_store(9671124, 1)
    i32_store(9242200, 0)
    i32_store(9242100, 0)
    i32_store16(9242105, 0)
    i64_store(9242208, 0)
    i32_store(9263072, 9242084)
    i32_store(9242596, 0)
    i32_store(9242496, 0)
    i32_store8(9242108, 0)
    i32_store16(9242501, 0)
    i64_store(9242604, 0)
    i32_store(9263076, 9242480)
    i32_store(9242728, 0)
    i32_store(9242628, 0)
    i32_store8(9242504, 0)
    i32_store16(9242633, 0)
    i64_store(9242736, 0)
    i32_store(9263080, 9242612)
    i32_store(9242992, 0)
    i32_store(9242892, 0)
    i32_store8(9242636, 0)
    i32_store16(9242897, 0)
    i64_store(9243000, 0)
    i32_store(9263084, 9242876)
    i32_store(9243156, 0)
    i32_store(9243256, 0)
    i32_store8(9242900, 0)
    i32_store16(9243161, 0)
    i64_store(9243264, 0)
    i32_store(9263088, 9243140)
    i32_store(9243288, 0)
    i32_store(9243388, 0)
    i32_store8(9243164, 0)
    i32_store16(9243293, 0)
    i32_store(9243400, 0)
    i32_store(9243396, 0)
    i32_store(9263092, 9243272)
    i32_store(9243520, 0)
    i32_store(9243420, 0)
    i32_store8(9243296, 0)
    i32_store16(9243425, 0)
    i64_store(9243528, 0)
    i32_store(9263096, 9243404)
    i32_store(9243784, 0)
    i32_store(9243684, 0)
    i32_store8(9243428, 0)
    i32_store16(9243689, 0)
    i64_store(9243792, 0)
    i32_store(9263100, 9243668)
    i32_store(9262792, 0)
    i32_store(9262692, 0)
    i32_store8(9243692, 0)
    i32_store16(9262697, 0)
    i64_store(9262800, 0)
    i32_store(9263104, 9262676)
    i32_store8(9262700, 0)
    i32_store(9671120, 9)
    a_b()

