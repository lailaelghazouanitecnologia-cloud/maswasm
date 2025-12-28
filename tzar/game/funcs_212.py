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
# $pc
# Export: pc
# ==========================================================
def pc(var0, var1, var2):
    """Export: pc"""
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
    var15 = 0.0
    var16 = 0.0
    var17 = 0.0
    var18 = 0.0
    var19 = 0.0
    var20 = 0.0
    var5 = (global0 - 96)
    global global0
    global0 = (global0 - 96)
    if i32_load8_u(9684432):
        break
    if (1 if i32_load(51776) == 0 else 0):
        i32_store8(9215872, 1)
        var3 = i32_load(9216000)
        if (1 if i32_load(9216000) != i32_load(9215996) else 0):
            var4 = i32_load(9215992)
            break
        var4 = (i32_load(9216004) + var3)
        i32_store(9215996, (i32_load(9216004) + var3))
        var6 = i32_load(9215992)
        var4 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
        if var3:
            # Unknown: memory.copy []
        if var6:
            var3 = i32_load(9216000)
        i32_store(9215992, var4)
        i32_store(9216000, (var3 + 1))
        i32_store((var4 + (var3 << 2)), var0)
        var0 = i32_load(9216000)
        if (1 if i32_load(9216000) != i32_load(9215996) else 0):
            var3 = var4
            break
        var3 = (i32_load(9216004) + var0)
        i32_store(9215996, (i32_load(9216004) + var0))
        var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
        if var0:
            # Unknown: memory.copy []
        i32_store(9215992, var3)
        var0 = i32_load(9216000)
        i32_store(9216000, (var0 + 1))
        i32_store((var3 + (var0 << 2)), var1)
        var1 = i32_load(9216000)
        if (1 if i32_load(9216000) != i32_load(9215996) else 0):
            var0 = var3
            break
        var0 = (i32_load(9216004) + var1)
        i32_store(9215996, (i32_load(9216004) + var1))
        var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var1:
            # Unknown: memory.copy []
        i32_store(9215992, var0)
        var1 = i32_load(9216000)
        i32_store(9216000, (var1 + 1))
        i32_store((var0 + (var1 << 2)), var2)
        break
    if var2:
        i32_store(9681444, var1)
        i32_store(9681440, var0)
        break
    var1 = i32_load(9681444)
    var0 = i32_load(9681440)
    var15 = float(i32_load(9142860))
    var15 = f32_load(40616)
    var16 = f32_load(9671164)
    var17 = (((float(i32_load(9142860)) - ((var15 * f32_load(40616)) / f32_load(9671164))) * 0.5) + ((var15 * float(var1)) + float(i32_load(9142956))))
    if (1 if abs((((float(i32_load(9142860)) - ((var15 * f32_load(40616)) / f32_load(9671164))) * 0.5) + ((var15 * float(var1)) + float(i32_load(9142956))))) < 2147483650.0 else 0):
        break
    var1 = -2147483648
    var17 = float(i32_load(9142856))
    var15 = (((var15 * float(var0)) + float(i32_load(9142952))) + ((float(i32_load(9142856)) - ((var15 * var17) / var16)) * 0.5))
    if (1 if abs((((var15 * float(var0)) + float(i32_load(9142952))) + ((float(i32_load(9142856)) - ((var15 * var17) / var16)) * 0.5))) < 2147483650.0 else 0):
        break
    var0 = -2147483648
    if i32_load8_u(9681884):
        break
    var2 = i32_load8_u(9142409)
    if i32_load8_u(9142409):
        if i32_load(9142900):
            break
    if i32_load(9684792):
        var2 = i32_load(9684792)
        var6 = i32_load(i32_load(9684792))
        var7 = (var0 - i32_load(i32_load(9684792)))
        var10 = i32_load(var2 + 8)
        var1 = (i32_load(var2 + 20) * i32_load(var2 + 16))
        if (i32_load(var2 + 20) * i32_load(var2 + 16)):
        else:
        var11 = ((i32_load(var2 + 4) // var1) - 0)
        var0 = (((i32_load(var2 + 4) // var1) - 0) // 32)
        var12 = i32_load(var2 + 12)
        var3 = (var7 // 32)
        var6 = ((var3 + (var6 // 32)) + (1 if (var6 & 31) != 0 else 0))
        if (1 if (var7 // 32) >= ((var3 + (var6 // 32)) + (1 if (var6 & 31) != 0 else 0)) else 0):
            var8 = i32_load(9142440)
            var4 = 1
            break
        var1 = (i32_load(var2 + 4) // var1)
        var1 = ((((i32_load(var2 + 4) // var1) // 32) + var0) + (1 if (var1 & 31) != 0 else 0))
        var13 = (var0 if (1 if var0 > var1 else 0) else ((((i32_load(var2 + 4) // var1) // 32) + var0) + (1 if (var1 & 31) != 0 else 0)))
        var8 = i32_load(9142440)
        var9 = (i32_load(9142440) + 2)
        var14 = i32_load(9142840)
        while True:  # loop $label9
            var3 = (var3 + 1)
            var1 = var0
            while True:  # loop $label8
                if (1 if var1 != var13 else 0):
                    var1 = (var1 + 1)
                    if (1 if i32_load((var14 + (((((var1 + 1) + var9) * var9) + var3) << 2))) != 1 else 0):
                        continue
                    break
                break  # end loop
            var4 = (1 if var3 >= var6 else 0)
            if (1 if var3 != var6 else 0):
                continue
            break  # end loop
        break
    if i32_load(9671176):
        break
    if (1 if var2 == 0 else 0):
        break
    var15 = float(var1)
    var16 = float(i32_load(59140))
    var2 = (1 if var15 < var16 else 0)
    var17 = (float(var1) if (1 if var15 < var16 else 0) else float(i32_load(59140)))
    var18 = float(var0)
    var19 = float(i32_load(59132))
    var3 = (1 if var18 < var19 else 0)
    var20 = (float(var0) if (1 if var18 < var19 else 0) else float(i32_load(59132)))
    if (1 if i32_load8_u(59183) == 0 else 0):
        var15 = abs((var15 - var16))
        break
    var15 = (var17 * 0.03125)
    if (1 if abs((var17 * 0.03125)) < 2147483650.0 else 0):
        break
    var17 = float((-2147483648 << 5))
    var15 = (math.ceil((abs((int(var15) - float((-2147483648 << 5)))) * 0.03125)) * 32.0)
    var16 = (var20 * 0.03125)
    if (1 if abs((var20 * 0.03125)) < 2147483650.0 else 0):
        break
    var20 = float((-2147483648 << 5))
    var18 = (math.ceil((abs((int(var16) - float((-2147483648 << 5)))) * 0.03125)) * 32.0)
    if (1 if i32_load8_u(9142410) == 0 else 0):
        i32_store8(9142410, 1)
    if i32_load8_u(9142916):
        break
    var3 = i32_load(9142876)
    var16 = 0.0
    var2 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    if i32_load8_u(9142916):
        var16 = ((0.0 / float((i32_load(9142440) * 96))) + 0.25)
    i32_store(var2 + 24, var3)
    f64_store(var2 + 16, float(var16))
    f64_store(var2 + 8, float((var17 + -0.0)))
    f64_store(var2, float((var20 + -0.0)))
    a_b()
    global global0
    global0 = (var2 + 32)
    if i32_load8_u(9142916):
        break
    i64_store((var5 - -64), 0)
    i64_store(var5 + 72, 0)
    i32_store(var5 + 80, i32_load(9142876))
    f64_store(var5 + 56, float(var15))
    f64_store(var5 + 48, float((-var18)))
    a_b()
    var2 = (var0 // 32)
    var4 = i32_load(9142440)
    var6 = (var1 // 32)
    if (1 if i32_load(9142440) <= (var1 // 32) else 0):
        break
    if (1 if (var2 | var6) < 0 else 0):
        break
    if (1 if var2 >= var4 else 0):
        break
    var7 = i32_load8_u(9147152)
    if (1 if (0 if i32_load8_u(9147152) else i32_load(i32_load(9142424) + 48)) == 0 else 0):
        var3 = i32_load(40604)
        break
    var3 = i32_load(40604)
    if i32_load16_u((i32_load(9147376) + (((var4 * var6) + var2) << 1))):
        break
    if (1 if var3 != -1 else 0):
        break
    break
    var3 = i32_load(40604)
    if (1 if i32_load(40604) != -1 else 0):
        break
    if i32_load(9216064):
        break
    i32_store(41088, 2)
    i64_store(var5 + 32, 2)
    break
    if (1 if var3 != -1 else 0):
        break
    if var7:
        break
    if i32_load(9216064):
        break
    var0 = func141(var0, var1)
    if func141(var0, var1):
        var1 = i32_load(9213808)
        if i32_load(9213808):
            break
    i32_store(41088, 2)
    i64_store(var5 + 16, 2)
    break
    var0 = func161((i32_load(9671128) + (var0 * 132)), 9173808, var1)
    if func161((i32_load(9671128) + (var0 * 132)), 9173808, var1):
        break
    i32_store(41088, 2)
    i64_store(var5, 2)
    break
    if (1 if i32_load8_u(((var3 * 40) + 9671200) + 17) == 0 else 0):
        break
    global global0
    global0 = (var5 + 96)
    return func145(var3, (1 if func141(var0, var1) == 0 else 0))


# ==========================================================
# $ee
# Export: ee
# ==========================================================
def ee(var0, var1, var2):
    """Export: ee"""
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
    var8 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    func182()
    var0 = (var0 + 1)
    i32_store(9142892, (var0 + 1))
    i32_store16(9147208, 1)
    var3 = i32_load(9561692)
    if i32_load(9561692):
    else:
    var14 = (i64_extend_u(var0) * 286704)
    var3 = (i32_load(9142892) if i32(((var14 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var0) * 286704)))
    var0 = func26((i32_load(9142892) if i32(((var14 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var0) * 286704))))
    # Unknown: memory.fill []
    i32_store(9561692, var0)
    i32_store8((var0 + 283974), 255)
    i32_store16(var0 + 283972, 65535)
    i32_store(var8 + 16, var2)
    var10 = i32_load(9142424)
    i32_store(i32_load(9142424) + 24, var1)
    i32_store(var10, var2)
    i32_store8(9681940, 1)
    var6 = i32_load(9142892)
    var3 = (i32_load(9142892) * var6)
    var5 = func26((i32_load(9142892) * var6))
    # Unknown: memory.fill []
    i32_store(9143004, var5)
    var0 = func26(var3)
    # Unknown: memory.fill []
    i32_store(9143012, var0)
    if (1 if var3 == 0 else 0):
        break
    var2 = 0
    var0 = 0
    if (1 if var3 >= 4 else 0):
        var7 = (var3 & -4)
        var1 = 0
        while True:  # loop $label1
            i32_store8((var0 + var5), (1 if i32_load(((var0 << 2) + 9147392)) != 0 else 0))
            var4 = (var0 | 1)
            i32_store8((var5 + (var0 | 1)), (1 if i32_load(((var4 << 2) + 9147392)) != 0 else 0))
            var4 = (var0 | 2)
            i32_store8((var5 + (var0 | 2)), (1 if i32_load(((var4 << 2) + 9147392)) != 0 else 0))
            var4 = (var0 | 3)
            i32_store8((var5 + (var0 | 3)), (1 if i32_load(((var4 << 2) + 9147392)) != 0 else 0))
            var0 = (var0 + 4)
            var1 = (var1 + 4)
            if (1 if (var1 + 4) != var7 else 0):
                continue
            break  # end loop
    var1 = (var3 & 3)
    if (1 if (var3 & 3) == 0 else 0):
        break
    while True:  # loop $label2
        i32_store8((var0 + var5), (1 if i32_load(((var0 << 2) + 9147392)) != 0 else 0))
        var0 = (var0 + 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var1 else 0):
            continue
        break  # end loop
    var1 = func26(var3)
    # Unknown: memory.fill []
    i32_store(9143008, var1)
    if (1 if var6 >= 2 else 0):
        var0 = (var6 - 1)
        var12 = ((var6 - 1) & -4)
        var11 = (var0 & 3)
        var13 = (1 if (var6 - 2) < 3 else 0)
        var2 = 1
        while True:  # loop $label5
            var7 = (var2 * var6)
            var4 = 0
            var0 = 1
            if (1 if var13 == 0 else 0):
                while True:  # loop $label3
                    i32_store8((var1 + (var0 + var7)), (1 if var0 == var2 else 0))
                    var9 = (var0 + 1)
                    i32_store8((var1 + ((var0 + 1) + var7)), (1 if var2 == var9 else 0))
                    var9 = (var0 + 2)
                    i32_store8((var1 + ((var0 + 2) + var7)), (1 if var2 == var9 else 0))
                    var9 = (var0 + 3)
                    i32_store8((var1 + ((var0 + 3) + var7)), (1 if var2 == var9 else 0))
                    var0 = (var0 + 4)
                    var4 = (var4 + 4)
                    if (1 if (var4 + 4) != var12 else 0):
                        continue
                    break  # end loop
            var4 = 0
            if var11:
                while True:  # loop $label4
                    i32_store8((var1 + (var0 + var7)), (1 if var0 == var2 else 0))
                    var0 = (var0 + 1)
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != var11 else 0):
                        continue
                    break  # end loop
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var6 else 0):
                continue
            break  # end loop
    var0 = func26(var3)
    # Unknown: memory.fill []
    i32_store(9143016, var0)
    var2 = func26(var3)
    # Unknown: memory.fill []
    i32_store(9143012, var2)
    if (1 if var3 == 0 else 0):
        break
    var1 = 0
    var0 = 0
    if (1 if var3 >= 4 else 0):
        var7 = (var3 & -4)
        var6 = 0
        while True:  # loop $label7
            i32_store8((var0 + var2), (i32_load8_u((var0 + var5)) ^ 1))
            var4 = (var0 | 1)
            i32_store8((var2 + (var0 | 1)), (i32_load8_u((var4 + var5)) ^ 1))
            var4 = (var0 | 2)
            i32_store8((var2 + (var0 | 2)), (i32_load8_u((var4 + var5)) ^ 1))
            var4 = (var0 | 3)
            i32_store8((var2 + (var0 | 3)), (i32_load8_u((var4 + var5)) ^ 1))
            var0 = (var0 + 4)
            var6 = (var6 + 4)
            if (1 if (var6 + 4) != var7 else 0):
                continue
            break  # end loop
    var3 = (var3 & 3)
    if (1 if (var3 & 3) == 0 else 0):
        break
    while True:  # loop $label8
        i32_store8((var0 + var2), (i32_load8_u((var0 + var5)) ^ 1))
        var0 = (var0 + 1)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != var3 else 0):
            continue
        break  # end loop
    i32_store(var8, var10)
    i32_store(var8 + 4, i32_load(9142428))
    global global0
    global0 = (var8 + 32)
    return var8

