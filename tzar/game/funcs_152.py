"""
Auto-generated from WAT. Contains 7 functions.
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
# $func691
# ==========================================================
def func691(var0):
    var1 = 0
    var2 = 0
    var0 = i32_load(9213808)
    if i32_load8_u(9147210):
        func41(24, 9173808, var0, 0, 0)
        return
    var2 = (var0 << 2)
    var1 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var0:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9214016)]


# ==========================================================
# $func692
# ==========================================================
def func692(var0):
    var1 = 0
    var2 = 0
    var0 = i32_load(9213808)
    if i32_load8_u(9147210):
        func41(26, 9173808, var0, 0, 0)
        return
    var2 = (var0 << 2)
    var1 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var0:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9214032)]


# ==========================================================
# $Id
# Export: Id
# ==========================================================
def Id(var0, var1, var2):
    """Export: Id"""
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
    var14 = 0.0
    var15 = 0.0
    var16 = 0.0
    var3 = (global0 - 144)
    global global0
    global0 = (global0 - 144)
    if i32_load8_u(9684432):
        break
    i32_store(9142900, var2)
    i32_store8(9142409, 1)
    var14 = f32_load(40616)
    var15 = float(i32_load(9142856))
    var15 = f32_load(9671164)
    var16 = (((f32_load(40616) * float(var0)) + float(i32_load(9142952))) + ((float(i32_load(9142856)) - ((var14 * var15) / f32_load(9671164))) * 0.5))
    if (1 if abs((((f32_load(40616) * float(var0)) + float(i32_load(9142952))) + ((float(i32_load(9142856)) - ((var14 * var15) / f32_load(9671164))) * 0.5))) < 2147483650.0 else 0):
        break
    var0 = -2147483648
    i32_store(int(var16), -2147483648)
    var16 = float(i32_load(9142860))
    var14 = (((float(i32_load(9142860)) - ((var14 * var16) / var15)) * 0.5) + ((var14 * float(var1)) + float(i32_load(9142956))))
    if (1 if abs((((float(i32_load(9142860)) - ((var14 * var16) / var15)) * 0.5) + ((var14 * float(var1)) + float(i32_load(9142956))))) < 2147483650.0 else 0):
        break
    var1 = -2147483648
    i32_store(int(var14), -2147483648)
    var4 = i32_load(9684792)
    if (1 if i32_load(9684792) == 0 else 0):
        break
    if (1 if var2 == 2 else 0):
        i32_store(9684792, 0)
        var0 = i32_load(9684796)
        if i32_load8_u(9142916):
            i32_store(var3 + 32, var0)
            a_b()
            break
        i32_store(var3 + 24, var0)
        i64_store(var3 + 16, -4602115869219225600)
        i64_store(var3 + 8, 0)
        i64_store(var3, 0)
        a_b()
        break
    var2 = i32_load(var4)
    var6 = (var0 - i32_load(var4))
    var9 = i32_load(var4 + 8)
    var0 = 0
    var5 = (i32_load(var4 + 20) * i32_load(var4 + 16))
    if (i32_load(var4 + 20) * i32_load(var4 + 16)):
    else:
    var10 = ((i32_load(var4 + 4) // var5) - 0)
    var1 = (((i32_load(var4 + 4) // var5) - 0) // 32)
    var11 = i32_load(var4 + 12)
    var0 = (var6 // 32)
    var7 = ((var0 + (var2 // 32)) + (1 if (var2 & 31) != 0 else 0))
    if (1 if (var6 // 32) < ((var0 + (var2 // 32)) + (1 if (var2 & 31) != 0 else 0)) else 0):
        var2 = (i32_load(var4 + 4) // var5)
        var2 = ((((i32_load(var4 + 4) // var5) // 32) + var1) + (1 if (var2 & 31) != 0 else 0))
        var12 = (var1 if (1 if var1 > var2 else 0) else ((((i32_load(var4 + 4) // var5) // 32) + var1) + (1 if (var2 & 31) != 0 else 0)))
        var5 = (i32_load(9142440) + 2)
        var13 = i32_load(9142840)
        while True:  # loop $label5
            var0 = (var0 + 1)
            var2 = var1
            while True:  # loop $label3
                if (1 if var2 != var12 else 0):
                    var2 = (var2 + 1)
                    if (1 if i32_load((var13 + (((((var2 + 1) + var5) * var5) + var0) << 2))) != 1 else 0):
                        continue
                    break
                break  # end loop
            var8 = (1 if var0 >= var7 else 0)
            if (1 if var0 != var7 else 0):
                continue
            break  # end loop
        if (1 if var8 == 0 else 0):
            break
    var0 = (var6 + var9)
    var1 = (var10 + var11)
    func216(i32_load(9681936), i32_load(var4 + 52), (var6 + var9), (var10 + var11), func370(var4, var0, var1))
    var0 = i32_load(9684796)
    if i32_load8_u(9142916):
        i32_store(var3 + 128, var0)
        a_b()
        break
    i32_store(var3 + 120, var0)
    i64_store(var3 + 112, -4602115869219225600)
    i64_store(var3 + 104, 0)
    i64_store(var3 + 96, 0)
    a_b()
    if i32_load8_u(9163792):
        break
    i32_store(9684792, 0)
    var0 = i32_load(9684796)
    if i32_load8_u(9142916):
        i32_store(var3 + 80, var0)
        a_b()
        break
    i32_store(var3 + 72, var0)
    i64_store((var3 - -64), -4602115869219225600)
    i64_store(var3 + 56, 0)
    i64_store(var3 + 48, 0)
    a_b()
    global global0
    global0 = (var3 + 144)
    return (var3 + 48)


# ==========================================================
# $Fd
# Export: Fd
# ==========================================================
def Fd(var0):
    """Export: Fd"""
    var1 = 0
    var1 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    i32_store(40600, var0)
    if (1 if var0 == 0 else 0):
        var0 = i32_load(9142884)
        if i32_load8_u(9142916):
            i32_store(var1 + 32, var0)
            a_b()
            break
        i32_store(var1 + 24, var0)
        i64_store(var1 + 16, -4602115869219225600)
        i64_store(var1 + 8, 0)
        i64_store(var1, 0)
        a_b()
        break
    global global0
    global0 = (var1 + 48)


# ==========================================================
# $func726
# ==========================================================
def func726(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0.0
    var11 = 0.0
    var3 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var6 = ((var0 & 0xFFFFFFFF) >> 16)
    var4 = (((var0 & 0xFFFFFFFF) >> 16) << 5)
    var2 = (var0 * var6)
    var10 = float((((((var0 & 0xFFFFFFFF) >> 16) << 5) | (((var0 * var6) * var6) & 31)) - 16))
    var8 = (var0 & 65535)
    var5 = ((var0 & 65535) << 5)
    var11 = float(((((var0 & 65535) << 5) | ((var0 * var2) & 31)) - 16))
    var2 = 0
    if i32_load8_u(9142917):
        break
    var2 = i32_load(9299880)
    if i32_load(9299880):
        var2 = (var2 - 1)
        i32_store(9299880, (var2 - 1))
        var2 = i32_load((i32_load(9299872) + (var2 << 2)))
        break
    var2 = i32_load(9163776)
    var7 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var9 = i32_load(9163784)
    if (1 if var7 < i32_load(9163784) else 0):
        break
    i32_store(var3 + 16, var9)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    var5 = (var5 - i32_load(9142952))
    var4 = (var4 - i32_load(9142956))
    if (1 if ((((var5 - i32_load(9142952)) * var5) + ((var4 - i32_load(9142956)) * var4)) - 1) > 9000000 else 0):
        break
    var5 = i32_load(39828)
    var7 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var4 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var6) + var8) << 1)))
    if (1 if var7 == 2 else 0):
        if (1 if var4 > 1 else 0):
            break
        break
    if (1 if var4 == 0 else 0):
        break
    i32_store(var3 + 8, var6)
    i32_store(var3 + 4, var8)
    i32_store(var3, var5)
    a_b()
    if ((1 if var10 < 4294967300.0 else 0) & (1 if var10 >= 0.0 else 0)):
        break
    var0 = 0
    if ((1 if var11 < 4294967300.0 else 0) & (1 if var11 >= 0.0 else 0)):
        break
    global global0
    global0 = (var3 + 32)
    return func113(607, var2)


# ==========================================================
# $func737
# ==========================================================
def func737(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var2 = ((var1 * 404) + 9568096)
    var3 = i32_load(((var1 * 404) + 9568096) + 236)
    if i32_load(((var1 * 404) + 9568096) + 236):
        var7 = (i32_load(9561692) + (var0 * 286704))
        while True:  # loop $label5
            var9 = i32_load((i32_load(var2 + 232) + (var5 << 2)))
            var6 = i32_load(((var7 + (i32_load((i32_load(var2 + 232) + (var5 << 2))) << 2)) + 284636))
            if (1 if i32_load(((var7 + (i32_load((i32_load(var2 + 232) + (var5 << 2))) << 2)) + 284636)) == 0 else 0):
                break
            var0 = 0
            var8 = i32_load(var6 + 8)
            if (1 if i32_load(var6 + 8) == 0 else 0):
                break
            while True:  # loop $label4
                var1 = i32_load((i32_load(var6) + (var0 << 2)))
                if i32_load((i32_load(var6) + (var0 << 2))):
                    var1 = (i32_load(9671128) + (var1 * 132))
                    i32_store((i32_load(9671128) + (var1 * 132)) + 52, (i32_load(var1 + 52) + i32_load(var2 + 92)))
                    i32_store(var1 + 60, (i32_load(var1 + 60) + i32_load(var2 + 100)))
                    i32_store(var1 + 84, (i32_load(var1 + 84) + i32_load(var2 + 112)))
                    var3 = i32_load(var1 + 68)
                    # br_table ['$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label1', '$label2']
                    _br_idx = (i32_load8_u(var1 + 125) - 4)
                    break  # br_table
                    var4 = i32_load(var1 + 64)
                    i32_store(var1 + 64, ((((i32_load(var1 + 64) * i32_load(var2 + 104)) & 0xFFFFFFFF) // (1 if (1 if var3 <= 1 else 0) else var3)) + var4))
                    i32_store(var1 + 68, (i32_load(var2 + 104) + var3))
                    var4 = i32_load(var1 + 72)
                    var3 = i32_load(var2 + 120)
                    if (1 if i32_load(var2 + 120) == 0 else 0):
                        break
                    if var4:
                        break
                    var8 = i32_load(var6 + 8)
                    var4 = i32_load(var1 + 72)
                    var3 = i32_load(var2 + 120)
                    i32_store(var1 + 72, (var3 + var4))
                    i32_store(var1 + 76, (i32_load(var1 + 76) + var3))
                var0 = (var0 + 1)
                if (1 if (var0 + 1) < var8 else 0):
                    continue
                break  # end loop
            var3 = i32_load(var2 + 236)
            var0 = (var7 + (var9 * 36))
            var1 = ((var7 + (var9 * 36)) + 269380)
            i32_store(((var7 + (var9 * 36)) + 269380), (i32_load(var1) + i32_load(var2 + 92)))
            var1 = (var0 + 269384)
            i32_store((var0 + 269384), (i32_load(var1) + i32_load(var2 + 100)))
            var1 = (var0 + 269396)
            i32_store((var0 + 269396), (i32_load(var1) + i32_load(var2 + 112)))
            var1 = (var0 + 269388)
            i32_store((var0 + 269388), (i32_load(var1) + i32_load(var2 + 104)))
            var1 = (var0 + 269392)
            i32_store((var0 + 269392), (i32_load(var1) + i32_load(var2 + 108)))
            var0 = (var0 + 269404)
            i32_store((var0 + 269404), (i32_load(var0) + i32_load(var2 + 120)))
            var5 = (var5 + 1)
            if (1 if (var5 + 1) < var3 else 0):
                continue
            break  # end loop


# ==========================================================
# $func738
# ==========================================================
def func738(var0, var1):
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
    var2 = ((var1 * 404) + 9568096)
    var3 = i32_load(((var1 * 404) + 9568096) + 236)
    if i32_load(((var1 * 404) + 9568096) + 236):
        var8 = (i32_load(9561692) + (var0 * 286704))
        while True:  # loop $label5
            var9 = i32_load((i32_load(var2 + 232) + (var5 << 2)))
            var0 = ((i32_load((i32_load(var2 + 232) + (var5 << 2))) * 404) + 9568096)
            var6 = (((i32_load(var2 + 120) * i32_load(((i32_load((i32_load(var2 + 232) + (var5 << 2))) * 404) + 9568096) + 120)) & 0xFFFFFFFF) // 100)
            var10 = (((i32_load(var2 + 112) * i32_load(var0 + 112)) & 0xFFFFFFFF) // 100)
            var11 = (((i32_load(var2 + 100) * i32_load(var0 + 100)) & 0xFFFFFFFF) // 100)
            var12 = (((i32_load(var2 + 92) * i32_load(var0 + 92)) & 0xFFFFFFFF) // 100)
            var4 = (((i32_load(var2 + 104) * i32_load(var0 + 104)) & 0xFFFFFFFF) // 100)
            var7 = i32_load(((var8 + (var9 << 2)) + 284636))
            if (1 if i32_load(((var8 + (var9 << 2)) + 284636)) == 0 else 0):
                break
            var0 = 0
            var13 = i32_load(var7 + 8)
            if (1 if i32_load(var7 + 8) == 0 else 0):
                break
            while True:  # loop $label4
                var1 = i32_load((i32_load(var7) + (var0 << 2)))
                if i32_load((i32_load(var7) + (var0 << 2))):
                    var1 = (i32_load(9671128) + (var1 * 132))
                    # br_table ['$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label1', '$label2']
                    _br_idx = (i32_load8_u((i32_load(9671128) + (var1 * 132)) + 125) - 4)
                    break  # br_table
                    i32_store(var1 + 64, (i32_load(var1 + 64) + var4))
                    i32_store(var1 + 68, (i32_load(var1 + 68) + var4))
                    i32_store(var1 + 52, (i32_load(var1 + 52) + var12))
                    i32_store(var1 + 60, (i32_load(var1 + 60) + var11))
                    i32_store(var1 + 84, (i32_load(var1 + 84) + var10))
                    var3 = i32_load(var1 + 72)
                    if (1 if i32_load(var2 + 120) == 0 else 0):
                        break
                    if var3:
                        break
                    var13 = i32_load(var7 + 8)
                    var3 = i32_load(var1 + 72)
                    i32_store(var1 + 72, (var3 + var6))
                    i32_store(var1 + 76, (i32_load(var1 + 76) + var6))
                var0 = (var0 + 1)
                if (1 if (var0 + 1) < var13 else 0):
                    continue
                break  # end loop
            var3 = i32_load(var2 + 236)
            var0 = (var8 + (var9 * 36))
            var1 = ((var8 + (var9 * 36)) + 269388)
            i32_store(((var8 + (var9 * 36)) + 269388), (i32_load(var1) + var4))
            var1 = (var0 + 269392)
            i32_store((var0 + 269392), (i32_load(var1) + var4))
            var1 = (var0 + 269380)
            i32_store((var0 + 269380), (i32_load(var1) + var12))
            var1 = (var0 + 269384)
            i32_store((var0 + 269384), (i32_load(var1) + var11))
            var1 = (var0 + 269396)
            i32_store((var0 + 269396), (i32_load(var1) + var10))
            var0 = (var0 + 269404)
            i32_store((var0 + 269404), (i32_load(var0) + var6))
            var5 = (var5 + 1)
            if (1 if (var5 + 1) < var3 else 0):
                continue
            break  # end loop

