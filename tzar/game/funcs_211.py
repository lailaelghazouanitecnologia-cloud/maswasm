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
# $oc
# Export: oc
# ==========================================================
def oc(var0, var1, var2, var3, var4, var5, var6, var7, param8):
    """Export: oc"""
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
    var19 = 0.0
    var20 = 0.0
    var21 = 0.0
    var8 = (global0 - 128)
    global global0
    global0 = (global0 - 128)
    if i32_load8_u(9684432):
        break
    if (1 if i32_load(51776) == 0 else 0):
        i32_store8(9215872, 1)
        var9 = i32_load(9215984)
        if (1 if i32_load(9215984) != i32_load(9215980) else 0):
            var10 = i32_load(9215976)
            break
        var10 = (i32_load(9215988) + var9)
        i32_store(9215980, (i32_load(9215988) + var9))
        var11 = i32_load(9215976)
        var10 = func26((-1 if (1 if var10 > 1073741823 else 0) else (var10 << 2)))
        if var9:
            # Unknown: memory.copy []
        if var11:
            var9 = i32_load(9215984)
        i32_store(9215976, var10)
        i32_store(9215984, (var9 + 1))
        i32_store((var10 + (var9 << 2)), var0)
        var0 = i32_load(9215984)
        if (1 if i32_load(9215984) != i32_load(9215980) else 0):
            var9 = var10
            break
        var9 = (i32_load(9215988) + var0)
        i32_store(9215980, (i32_load(9215988) + var0))
        var9 = func26((-1 if (1 if var9 > 1073741823 else 0) else (var9 << 2)))
        if var0:
            # Unknown: memory.copy []
        i32_store(9215976, var9)
        var0 = i32_load(9215984)
        i32_store(9215984, (var0 + 1))
        i32_store((var9 + (var0 << 2)), var1)
        var1 = i32_load(9215984)
        if (1 if i32_load(9215984) != i32_load(9215980) else 0):
            var0 = var9
            break
        var0 = (i32_load(9215988) + var1)
        i32_store(9215980, (i32_load(9215988) + var1))
        var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var1:
            # Unknown: memory.copy []
        i32_store(9215976, var0)
        var1 = i32_load(9215984)
        i32_store(9215984, (var1 + 1))
        i32_store((var0 + (var1 << 2)), var2)
        var1 = i32_load(9215984)
        if (1 if i32_load(9215984) != i32_load(9215980) else 0):
            var2 = var0
            break
        var2 = (i32_load(9215988) + var1)
        i32_store(9215980, (i32_load(9215988) + var1))
        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        if var1:
            # Unknown: memory.copy []
        i32_store(9215976, var2)
        var1 = i32_load(9215984)
        i32_store(9215984, (var1 + 1))
        i32_store((var2 + (var1 << 2)), var3)
        var1 = i32_load(9215984)
        if (1 if i32_load(9215984) != i32_load(9215980) else 0):
            var0 = var2
            break
        var0 = (i32_load(9215988) + var1)
        i32_store(9215980, (i32_load(9215988) + var1))
        var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var1:
            # Unknown: memory.copy []
        i32_store(9215976, var0)
        var1 = i32_load(9215984)
        i32_store(9215984, (var1 + 1))
        i32_store((var0 + (var1 << 2)), var4)
        var4 = i32_load(9215984)
        if (1 if i32_load(9215984) != i32_load(9215980) else 0):
            var1 = var0
            break
        var1 = (i32_load(9215988) + var4)
        i32_store(9215980, (i32_load(9215988) + var4))
        var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        if var4:
            # Unknown: memory.copy []
        i32_store(9215976, var1)
        var4 = i32_load(9215984)
        i32_store(9215984, (var4 + 1))
        i32_store((var1 + (var4 << 2)), var5)
        var4 = i32_load(9215984)
        if (1 if i32_load(9215984) != i32_load(9215980) else 0):
            var0 = var1
            break
        var0 = (i32_load(9215988) + var4)
        i32_store(9215980, (i32_load(9215988) + var4))
        var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var4:
            # Unknown: memory.copy []
        i32_store(9215976, var0)
        var4 = i32_load(9215984)
        i32_store(9215984, (var4 + 1))
        i32_store((var0 + (var4 << 2)), var6)
        var4 = i32_load(9215984)
        if (1 if i32_load(9215984) != i32_load(9215980) else 0):
            var1 = var0
            break
        var1 = (i32_load(9215988) + var4)
        i32_store(9215980, (i32_load(9215988) + var4))
        var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        if var4:
            # Unknown: memory.copy []
        i32_store(9215976, var1)
        var4 = i32_load(9215984)
        i32_store(9215984, (var4 + 1))
        i32_store((var1 + (var4 << 2)), var7)
        break
    i32_store8(9163793, var6)
    i32_store8(9163792, var5)
    i32_store8(9163794, var7)
    if var3:
        break
    if i32_load8_u(9142409):
        break
    if (1 if var4 == 0 else 0):
        break
    i32_store8(9142409, 0)
    if (1 if i32_load8_u(9142410) == 0 else 0):
        break
    if i32_load8_u(59183):
        break
    if i32_load8_u(9142916):
        break
    i64_store(var8 + 80, -4602115869219225600)
    i32_store(var8 + 88, i32_load(9142876))
    i64_store(var8 + 64, 0)
    i64_store(var8 + 72, 0)
    a_b()
    if var4:
        break
    var19 = float(i32_load(9142860))
    var19 = f32_load(40616)
    var21 = f32_load(9671164)
    var20 = (((float(i32_load(9142860)) - ((var19 * f32_load(40616)) / f32_load(9671164))) * 0.5) + ((var19 * float(var1)) + float(i32_load(9142956))))
    if (1 if abs((((float(i32_load(9142860)) - ((var19 * f32_load(40616)) / f32_load(9671164))) * 0.5) + ((var19 * float(var1)) + float(i32_load(9142956))))) < 2147483650.0 else 0):
        break
    var1 = -2147483648
    var20 = float(i32_load(9142856))
    var19 = (((var19 * float(var0)) + float(i32_load(9142952))) + ((float(i32_load(9142856)) - ((var19 * var20) / var21)) * 0.5))
    if (1 if abs((((var19 * float(var0)) + float(i32_load(9142952))) + ((float(i32_load(9142856)) - ((var19 * var20) / var21)) * 0.5))) < 2147483650.0 else 0):
        var0 = int(var19)
        break
    var0 = -2147483648
    i32_store(59144, var1)
    i32_store(59136, var0)
    if i32_load(9684792):
        break
    var4 = i32_load8_u(9681884)
    var7 = i32_load(9671176)
    if i32_load(9671176):
        break
    if var4:
        break
    if var2:
        break
    if (1 if i32_load8_u(59183) == 0 else 0):
        break
    var0 = i32_load(59132)
    var1 = i32_load(59136)
    var2 = i32_load(9568088)
    var3 = i32_load(59144)
    var4 = i32_load(59140)
    var5 = ((i32_load(59144) if (1 if var3 < var4 else 0) else i32_load(59140)) // 32)
    i32_store(i32_load(9568088) + 24, ((i32_load(59144) if (1 if var3 < var4 else 0) else i32_load(59140)) // 32))
    var6 = ((var1 if (1 if var0 > var1 else 0) else var0) // 32)
    i32_store(var2 + 20, ((var1 if (1 if var0 > var1 else 0) else var0) // 32))
    var3 = ((var3 if (1 if var3 > var4 else 0) else var4) - (var5 << 5))
    var3 = (var3 >> 31)
    var3 = ((((var3 if (1 if var3 > var4 else 0) else var4) - (var5 << 5)) ^ (var3 >> 31)) - var3)
    i32_store(var2 + 40, (((((((var3 if (1 if var3 > var4 else 0) else var4) - (var5 << 5)) ^ (var3 >> 31)) - var3) & 0xFFFFFFFF) >> 5) + (1 if (var3 & 31) != 0 else 0)))
    var0 = ((var1 if (1 if var0 < var1 else 0) else var0) - (var6 << 5))
    var0 = (var0 >> 31)
    var0 = ((((var1 if (1 if var0 < var1 else 0) else var0) - (var6 << 5)) ^ (var0 >> 31)) - var0)
    i32_store(var2 + 28, (((((((var1 if (1 if var0 < var1 else 0) else var0) - (var6 << 5)) ^ (var0 >> 31)) - var0) & 0xFFFFFFFF) >> 5) + (1 if (var0 & 31) != 0 else 0)))
    break
    if (1 if var3 == 2 else 0):
        i32_store(59140, var1)
        i32_store(59132, var0)
    if (1 if var2 != 2 else 0):
        break
    if (1 if var4 == 0 else 0):
        break
    var1 = i32_load(9142880)
    var0 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if i32_load8_u(9142916):
        i32_store(var0 + 32, var1)
        a_b()
        break
    i32_store(var0 + 24, var1)
    i64_store(var0 + 16, -4602115869219225600)
    i64_store(var0 + 8, 0)
    i64_store(var0, 0)
    a_b()
    global global0
    global0 = (var0 + 48)
    i32_store8(9681884, 0)
    break
    if var4:
        break
    var3 = i32_load(9142440)
    var6 = ((var1 & 0xFFFFFFFF) >> 5)
    var5 = ((var0 & 0xFFFFFFFF) >> 5)
    var4 = ((1 if i32_load(9142440) > ((var1 & 0xFFFFFFFF) >> 5) else 0) & (1 if var3 > ((var0 & 0xFFFFFFFF) >> 5) else 0))
    if (1 if var2 == 2 else 0):
        if (1 if var4 == 0 else 0):
            break
        var4 = i32_load8_u(9147152)
        if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
            break
        if var4:
            break
        if (1 if i32_load16_u((i32_load(9147376) + (((var3 * var6) + var5) << 1))) == 0 else 0):
            break
        var2 = func141(var0, var1)
        if (1 if i32_load(40604) != -1 else 0):
            i32_store(40604, -1)
            i32_store(9142896, 0)
            if i32_load(9216064):
                break
            i32_store(41088, 2)
            i64_store(var8 + 16, 2)
            break
        if var7:
            var0 = 0
            if (1 if i32_load(9142396) == 0 else 0):
                break
            while True:  # loop $label20
                func38(i32_load((i32_load(9142392) + (var0 << 2))))
                var0 = (var0 + 1)
                if (1 if (var0 + 1) < i32_load(9142396) else 0):
                    continue
                break  # end loop
            i32_store(9142396, 0)
            var0 = i32_load(9142392)
            if (1 if i32_load(9142392) == 0 else 0):
                break
            var0 = 0
            if (1 if i32_load(9671176) == 0 else 0):
                break
            if i32_load(9671192):
                while True:  # loop $label22
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
            break
        var7 = i32_load(9213808)
        if (1 if i32_load(9213808) == 0 else 0):
            break
        if var4:
            break
        var4 = 0
        var3 = 0
        var9 = i32_load(9671128)
        var10 = (var2 if i32_load((i32_load(9671128) + (var2 * 132)) + 40) else 0)
        if (var2 if i32_load((i32_load(9671128) + (var2 * 132)) + 40) else 0):
            var3 = (var9 + (var10 * 132))
            var4 = func161((var9 + (var10 * 132)), 9173808, var7)
            if (1 if func161((var9 + (var10 * 132)), 9173808, var7) == 0 else 0):
                var7 = 0
                var11 = i32_load8_u(var3 + 122)
                if (1 if i32_load8_u(var3 + 122) == i32_load(38560) else 0):
                    break
                if (1 if i32_load(38620) == var11 else 0):
                    break
            if i32_load(var3 + 40):
                var7 = (var9 + (var10 * 132))
                func415((func295(var3, i32_load(9142872)) | (1 if i32_load16_u(var7 + 110) == 0 else 0)), i32_load(var3 + 40))
            var7 = var2
            var2 = ((1 if var4 == 6 else 0) & (1 if i32_load8_u(9163793) != 0 else 0))
            var3 = (0 if ((1 if var4 == 6 else 0) & (1 if i32_load8_u(9163793) != 0 else 0)) else var4)
            var4 = (0 if var2 else var7)
        if i32_load8_u(9163792):
            var0 = func245()
            func105(9684812, var5)
            func105(9684812, var6)
            func105(9684812, var4)
            func105(9684812, var3)
            func105(9684812, i32_load8_u(9163793))
            func105(9684812, var0)
            var1 = i32_load(9671128)
            if var4:
                var2 = (var1 + (var4 * 132))
                var3 = ((i32_load8_u((var1 + (var4 * 132)) + 122) * 404) + 9568096)
                var6 = (((i32_load(((i32_load8_u((var1 + (var4 * 132)) + 122) * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1) + i32_load16_u(var2 + 114))
            else:
            break
        i32_store(var8 + 108, var3)
        i32_store(var8 + 104, var4)
        i32_store(var8 + 100, var6)
        i32_store(var8 + 96, var5)
        i32_store(var8 + 112, 0)
        i32_store(var8 + 116, i32_load8_u(9163793))
        i32_store(var8 + 120, i32_load8_u(9163794))
        func360((var8 + 96), i32_load(9213808))
        var2 = ((i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) * 404) + 9568096)
        var5 = i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) * 404) + 9568096) + 64)
        if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) * 404) + 9568096) + 64):
            i32_store(var8, i32_load((i32_load(var2 + 52) + ((i32_load(9142848) % var5) << 2))))
            a_b()
        if (var3 | var4):
            break
        var2 = func245()
        func254(i32_load(9142576), var2)
        break
    if (1 if var4 == 0 else 0):
        if (1 if i32_load8_u(9142410) == 0 else 0):
            break
        break
    var2 = i32_load8_u(9147152)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if var2:
        break
    if (1 if i32_load16_u((i32_load(9147376) + (((var3 * var6) + var5) << 1))) == 0 else 0):
        break
    var3 = func141(var0, var1)
    var0 = i32_load(9216064)
    if i32_load(9216064):
        # call_indirect via table[var0]
        i32_store(9216064, 0)
        break
    # br_table ['$label26', '$label27', '$label27', '$label28', '$label27']
    _br_idx = var7
    break  # br_table
    if i32_load8_u(9142412):
        break
    var0 = i32_load(i32_load(9671168))
    if (1 if i32_load(i32_load(9671168)) == i32_load(38600) else 0):
        break
    if (1 if var0 == i32_load(38472) else 0):
        break
    if (1 if i32_load(9684800) == 0 else 0):
        break
    var2 = (i32_load(9561692) + (i32_load((i32_load(9215960) if i32_load(9215968) else 9142872)) * 286704))
    var1 = i32_load((((i32_load(9561692) + (i32_load((i32_load(9215960) if i32_load(9215968) else 9142872)) * 286704)) + (var0 * 36)) + 269376))
    var1 = (i32_load((((i32_load(9561692) + (i32_load((i32_load(9215960) if i32_load(9215968) else 9142872)) * 286704)) + (var0 * 36)) + 269376)) if var1 else 100)
    var0 = ((var0 * 404) + 9568096)
    i32_store(var8 + 96, (((i32_load((((i32_load(9561692) + (i32_load((i32_load(9215960) if i32_load(9215968) else 9142872)) * 286704)) + (var0 * 36)) + 269376)) if var1 else 100) * i32_load(((var0 * 404) + 9568096) + 68)) // 100))
    i32_store(var8 + 100, ((i32_load(var0 + 72) * var1) // 100))
    i32_store(var8 + 104, ((i32_load(var0 + 76) * var1) // 100))
    i32_store(var8 + 108, ((i32_load(var0 + 80) * var1) // 100))
    if i32_load8_u(9163793):
        break
    var0 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    var1 = i32_load(var8 + 96)
    if (1 if i32_load(var8 + 96) == 0 else 0):
        break
    if (1 if i32_load(var0 + 64) >= var1 else 0):
        break
    i32_store(var0 + 48, 0)
    a_b()
    var1 = i32_load(var8 + 100)
    if (1 if i32_load(var8 + 100) == 0 else 0):
        break
    if (1 if i32_load(var0 + 68) >= var1 else 0):
        break
    i32_store(var0 + 32, 1)
    a_b()
    var1 = i32_load(var8 + 104)
    if (1 if i32_load(var8 + 104) == 0 else 0):
        break
    if (1 if i32_load(var0 + 72) >= var1 else 0):
        break
    i32_store(var0 + 16, 2)
    a_b()
    var1 = i32_load(var8 + 108)
    if (1 if i32_load(var8 + 108) == 0 else 0):
        break
    if (1 if i32_load(var0 + 76) >= var1 else 0):
        break
    i32_store(var0, 3)
    a_b()
    var1 = i32_load(var8 + 96)
    if i32_load(var8 + 96):
        if (1 if i32_load(var0 + 64) < var1 else 0):
            break
    var1 = i32_load(var8 + 100)
    if i32_load(var8 + 100):
        if (1 if i32_load(var0 + 68) < var1 else 0):
            break
    var1 = i32_load(var8 + 104)
    if i32_load(var8 + 104):
        if (1 if i32_load(var0 + 72) < var1 else 0):
            break
    var1 = i32_load(var8 + 108)
    if i32_load(var8 + 108):
        if (1 if i32_load(var0 + 76) < var1 else 0):
            break
    var1 = 1
    global global0
    global0 = (var0 + 80)
    if (1 if var1 == 0 else 0):
        break
    var6 = 0
    var4 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var7 = i32_load(9671176)
    if (1 if i32_load(9671176) >= 3 else 0):
        while True:  # loop $label41
            var0 = (i32_load(9671168) + (var6 * 12))
            var2 = (i32_load(9684776) + i32_load((i32_load(9671168) + (var6 * 12)) + 8))
            var3 = (i32_load(9684772) + i32_load(var0 + 4))
            var9 = i32_load(var0)
            if ((1 if i32_load(var0) != i32_load(38472) else 0) & (1 if var9 != i32_load(38600) else 0)):
                break
            if (1 if i32_load8_u(9142410) == 0 else 0):
                break
            var5 = i32_load8_u(9684791)
            var10 = i32_load8_u(9684790)
            var11 = i32_load8_u(9684789)
            var12 = i32_load8_u(9684788)
            var13 = i32_load(9684784)
            var15 = i32_load(9684780)
            break
            var15 = 1
            if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
                var13 = 1
                var12 = 1
                var11 = 1
                var10 = 1
                var5 = 1
                break
            var13 = 1
            var12 = 1
            var11 = 1
            var10 = 1
            var5 = 1
            if i32_load8_u(9147152):
                break
            var0 = ((var9 * 404) + 9568096)
            var1 = i32_load(((var9 * 404) + 9568096) + 216)
            if (1 if i32_load(((var9 * 404) + 9568096) + 216) <= 0 else 0):
                break
            var0 = i32_load(var0 + 220)
            if (1 if i32_load(var0 + 220) <= 0 else 0):
                break
            var16 = (var0 + var2)
            var17 = (var1 + var3)
            var18 = i32_load(9147376)
            var14 = i32_load(9142440)
            var1 = var3
            while True:  # loop $label39
                var0 = var2
                if (1 if var1 < var14 else 0):
                    while True:  # loop $label38
                        if (1 if var0 >= var14 else 0):
                            break
                        if (1 if (var0 | var1) < 0 else 0):
                            break
                        if i32_load16_u((var18 + (((var0 * var14) + var1) << 1))):
                            break
                        var0 = (var0 + 1)
                        if (1 if (var0 + 1) < var16 else 0):
                            continue
                        break  # end loop
                var1 = (var1 + 1)
                if (1 if (var1 + 1) < var17 else 0):
                    continue
                break  # end loop
            break
            var1 = i32_load(38500)
            i32_store(var4 + 8, var2)
            i32_store(var4 + 4, var3)
            var2 = i32_load(9215968)
            var3 = i32_load(9215960)
            var0 = i32_load8_u(9142412)
            i32_store(var4, var9)
            var2 = i32_load((9142872 if var0 else (var3 if var2 else 9142872)))
            i32_store(var4 + 32, var10)
            i32_store(var4 + 28, var11)
            i32_store(var4 + 24, var12)
            i32_store(var4 + 20, var13)
            i32_store(var4 + 16, var15)
            i32_store(var4 + 12, var2)
            i32_store(var4 + 40, i32_load8_u(9163793))
            i32_store(var4 + 36, (((2 if (1 if var1 == var9 else 0) else var5) if (1 if var7 > 3 else 0) else var5) if var6 else var5))
            if var0:
                if i32_load8_u(9147210):
                    func41(4, 0, 0, var4, 11)
                    break
                # call_indirect via table[i32_load(9213856)]
                break
            var0 = i32_load(9213808)
            if i32_load8_u(9147210):
                func41(4, 9173808, var0, var4, 11)
                break
            var2 = (var0 << 2)
            var1 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
            if var0:
                # Unknown: memory.copy []
            # call_indirect via table[i32_load(9213856)]
            var7 = i32_load(9671176)
            var6 = (var6 + 1)
            if (1 if (var6 + 1) < ((var7 & 0xFFFFFFFF) // 3) else 0):
                continue
            break  # end loop
    if i32_load8_u(9163792):
        if (1 if i32_load(i32_load(9671168)) != i32_load(38636) else 0):
            break
    if (1 if var7 == 0 else 0):
        break
    if i32_load(9671192):
        var0 = 0
        while True:  # loop $label43
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
    var0 = 0
    if (1 if i32_load(9142396) == 0 else 0):
        break
    while True:  # loop $label45
        func38(i32_load((i32_load(9142392) + (var0 << 2))))
        var0 = (var0 + 1)
        if (1 if (var0 + 1) < i32_load(9142396) else 0):
            continue
        break  # end loop
    i32_store(9142396, 0)
    var0 = i32_load(9142392)
    if (1 if i32_load(9142392) == 0 else 0):
        break
    i32_store(9684784, 1)
    i32_store(9684780, 1)
    global global0
    global0 = (var4 + 48)
    break
    var0 = i32_load(40604)
    if (1 if i32_load(40604) == -1 else 0):
        break
    if var2:
        break
    var1 = var0
    if (1 if var0 == 65 else 0):
        i32_store(40604, 0)
        var3 = 0
        var1 = 0
    var3 = ((var1 * 40) + 9671200)
    var1 = (0 if i32_load8_u(((var1 * 40) + 9671200) + 16) else var3)
    var4 = i32_load(9142896)
    if (0 if var1 else i32_load8_u(var3 + 17)):
        break
    if (1 if i32_load8_u(9163792) == 0 else 0):
        i32_store(40604, -1)
        i32_store(41088, 2)
        i32_store(9142896, 0)
        i64_store(var8 + 48, 2)
    if (1 if var1 == 0 else 0):
        break
    var2 = (i32_load(9671128) + (var1 * 132))
    if (1 if i32_load((i32_load(9671128) + (var1 * 132)) + 40) == 0 else 0):
        break
    func415((func295(var2, i32_load(9142872)) | (1 if i32_load16_u(var2 + 110) == 0 else 0)), i32_load(var2 + 40))
    i32_store(var8 + 100, var6)
    i32_store(var8 + 96, var5)
    i32_store(var8 + 104, (-1 if (1 if var0 == 65 else 0) else var1))
    var0 = i32_load(var3)
    i32_store(var8 + 112, var4)
    i32_store(var8 + 108, var0)
    i32_store(var8 + 116, i32_load8_u(9163793))
    i32_store(var8 + 120, i32_load8_u(9163794))
    func360((var8 + 96), i32_load(9213808))
    var0 = ((i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) * 404) + 9568096)
    var1 = i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) * 404) + 9568096) + 64)
    if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) * 404) + 9568096) + 64) == 0 else 0):
        break
    i32_store(var8 + 32, i32_load((i32_load(var0 + 52) + ((i32_load(9142848) % var1) << 2))))
    a_b()
    break
    i32_store8(9142410, 0)
    global global0
    global0 = (var8 + 128)
    return func324()

