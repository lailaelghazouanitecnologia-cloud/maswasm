"""
Auto-generated from WAT. Contains 8 functions.
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
# $func852
# ==========================================================
def func852(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var7 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var2 = ((var0 & -32) - i32_load(9142952))
    var2 = ((var1 & -32) - i32_load(9142956))
    var2 = (((((var0 & -32) - i32_load(9142952)) * var2) + (((var1 & -32) - i32_load(9142956)) * var2)) - 1)
    var4 = ((var0 & 0xFFFFFFFF) >> 5)
    var5 = ((var1 & 0xFFFFFFFF) >> 5)
    var3 = i32_load(9142440)
    var6 = (i32_load(9142440) + 2)
    if (1 if i32_load((i32_load(9142840) + ((((var0 & 0xFFFFFFFF) >> 5) + (((((var1 & 0xFFFFFFFF) >> 5) + (i32_load(9142440) + 2)) + 1) * var6)) << 2)) + 4) == 1 else 0):
        if (1 if var2 > 9000000 else 0):
            var2 = 9142540
            break
        var6 = i32_load(39836)
        var2 = 9142540
        var8 = i32_load(i32_load(9142424) + 48)
        if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
            break
        if i32_load8_u(9147152):
            break
        var3 = i32_load16_u((i32_load(9147376) + (((var3 * var5) + var4) << 1)))
        if (1 if var8 == 2 else 0):
            if (1 if var3 > 1 else 0):
                break
            break
        if var3:
            break
        break
    if (1 if var2 > 9000000 else 0):
        var2 = 9142544
        break
    var6 = i32_load(39832)
    var2 = 9142544
    var8 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var3 = i32_load16_u((i32_load(9147376) + (((var3 * var5) + var4) << 1)))
    if (1 if var8 == 2 else 0):
        if (1 if var3 > 1 else 0):
            break
        break
    if (1 if var3 == 0 else 0):
        break
    i32_store(var7 + 8, var5)
    i32_store(var7 + 4, var4)
    i32_store(var7, var6)
    a_b()
    var3 = i32_load(var2)
    var6 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var2 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var5) + var4) << 1)))
    if (1 if var6 == 2 else 0):
        if (1 if var2 > 1 else 0):
            break
        break
    if (1 if var2 == 0 else 0):
        break
    var2 = (var4 * var5)
    # Unknown: f64.convert_i32_u []
    func80(float(((var0 + (((var4 * var5) * var4) & 31)) - 16)), float(((var1 + ((var2 * var5) & 31)) - 16)), var3, 1.0, f32((var1 * 0.7)))
    global global0
    global0 = (var7 + 16)


# ==========================================================
# $func856
# ==========================================================
def func856(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(var1 + 12, var0)
    var0 = i32_load(9213808)
    if i32_load8_u(9147210):
        func41(11, 9173808, var0, (var1 + 12), 1)
        break
    var3 = (var0 << 2)
    var2 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var0:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9213912)]
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $Ka
# Export: Ka
# ==========================================================
def Ka(var0):
    """Export: Ka"""
    var1 = 0
    if var0:
        if (1 if i32_load8_u(9147212) == 0 else 0):
            break
    var1 = i32_load(9142892)
    break
    var1 = i32_load(41092)
    i32_store(9142892, i32_load(41092))
    i32_store(41092, 1)
    i32_store8(9147210, 0)
    i32_store8(9142388, 0)
    i32_store(9142384, 0)
    if var0:
        break
    if (1 if var1 == 0 else 0):
        break
    i32_store(9142892, 0)
    var0 = i32_load(9561692)
    if i32_load(9561692):
        i32_store(9561692, 0)


# ==========================================================
# $func902
# ==========================================================
def func902(var0):
    var1 = 0
    var2 = 0
    var0 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var1 = i32_load(9173808)
    i32_store(var0 + 12, i32_load(9173808))
    i32_store(var0 + 8, i32_load(9213816))
    if i32_load8_u(9147210):
        func41(23, (var0 + 12), 1, (var0 + 8), 1)
        break
    var2 = func26(4)
    i32_store(func26(4), var1)
    # call_indirect via table[i32_load(9214008)]
    global global0
    global0 = (var0 + 16)


# ==========================================================
# $func917
# ==========================================================
def func917(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(var1 + 12, var0)
    var0 = i32_load(9213808)
    if i32_load8_u(9147210):
        func41(13, 9173808, var0, (var1 + 12), 1)
        break
    var3 = (var0 << 2)
    var2 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var0:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9213928)]
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $Wb
# Export: Wb
# ==========================================================
def Wb(var0):
    """Export: Wb"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var3 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if i32_load8_u(9147210):
        break
    if (1 if i32_load(9681888) >= 2 else 0):
        i32_store(9681892, var0)
        i32_store8(9681884, 1)
        i32_store8(9681885, 0)
        break
    if i32_load8_u(9681884):
        var1 = i32_load(9142880)
        if i32_load8_u(9142916):
            i32_store(var3 + 32, var1)
            a_b()
            break
        i32_store(var3 + 24, var1)
        i64_store(var3 + 16, -4602115869219225600)
        i64_store(var3 + 8, 0)
        i64_store(var3, 0)
        a_b()
        i32_store8(9681884, 0)
    if (1 if i32_load(9671176) == 0 else 0):
        break
    if i32_load(9671192):
        var1 = 0
        while True:  # loop $label3
            func38(i32_load((i32_load(9671184) + (var1 << 2))))
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < i32_load(9671192) else 0):
                continue
            break  # end loop
    i32_store(9671192, 0)
    i32_store(9671176, 0)
    i32_store8(9142412, 0)
    if (1 if i32_load8_u(9684396) == 0 else 0):
        break
    i32_store8(9684396, 0)
    a_b()
    var1 = i32_load(9671176)
    var2 = i32_load(9671172)
    if (1 if i32_load(9671172) > (var1 + 3) else 0):
        var2 = i32_load(9671168)
        break
    var2 = ((var2 + i32_load(9671180)) + 3)
    i32_store(9671172, ((var2 + i32_load(9671180)) + 3))
    var4 = i32_load(9671168)
    var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    if var1:
        # Unknown: memory.copy []
    if var4:
        var1 = i32_load(9671176)
    i32_store(9671168, var2)
    i32_store(9671176, (var1 + 1))
    i32_store((var2 + (var1 << 2)), var0)
    var0 = i32_load(9671176)
    i32_store(9671176, (i32_load(9671176) + 1))
    i32_store((var2 + (var0 << 2)), 0)
    var0 = i32_load(9671176)
    i32_store(9671176, (i32_load(9671176) + 1))
    i32_store((var2 + (var0 << 2)), 0)
    i32_store8(9142412, 1)
    global global0
    global0 = (var3 + 48)
    return af(var4)


# ==========================================================
# $xb
# Export: xb
# ==========================================================
def xb(var0):
    """Export: xb"""
    var1 = 0
    var2 = 0
    if (1 if var0 < 2 else 0):
        break
    if (1 if i32_load(9681888) != 1 else 0):
        break
    if (1 if i32_load(9671176) == 0 else 0):
        break
    var2 = i32_load(i32_load(9671168))
    i32_store8(9681884, 1)
    i32_store(9681892, var2)
    i32_store8(9681885, 0)
    if i32_load(9671192):
        while True:  # loop $label1
            func38(i32_load((i32_load(9671184) + (var1 << 2))))
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < i32_load(9671192) else 0):
                continue
            break  # end loop
    i32_store(9671192, 0)
    i32_store(9671176, 0)
    i32_store8(9142412, 0)
    if (1 if i32_load8_u(9684396) == 0 else 0):
        break
    i32_store8(9684396, 0)
    a_b()
    i32_store(9681888, var0)


# ==========================================================
# $func65
# ==========================================================
def func65(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    if i32_load8_u(9147152):
        break
    var3 = i32_load16_u(var0 + 114)
    var4 = i32_load16_u(var0 + 112)
    if (1 if i32_load8_u(59181) == 0 else 0):
        break
    if (1 if var1 == 0 else 0):
        break
    var1 = i32_load(var0 + 44)
    if (1 if i32_load(var0 + 44) == 0 else 0):
        break
    var2 = i32_load(9215884)
    if (1 if i32_load((i32_load(9215884) + (var1 << 4)) + 12) == 1 else 0):
        break
    if (1 if i32_load8_u(var0 + 125) == 7 else 0):
        break
    if i32_load((var2 + ((var1 << 4) | 4))):
        break
    var1 = (i32_load8_u(var0 + 124) << 3)
    var3 = (var3 - i32_load(((i32_load8_u(var0 + 124) << 3) + 8996)))
    var4 = (var4 - i32_load((var1 + 8992)))
    var1 = i32_load(9142872)
    if (1 if i32_load(9142872) == 0 else 0):
        break
    if (1 if i32_load8_u((i32_load(9143012) + (i32_load16_u(var0 + 110) + (i32_load(9142892) * var1)))) == 0 else 0):
        break
    var5 = i32_load8_u(var0 + 125)
    if (1 if i32_load8_u(var0 + 125) == 3 else 0):
        break
    var0 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var1 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 220)
    var2 = i32_load(var0 + 216)
    # br_table ['$label2', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label3', '$label2', '$label3']
    _br_idx = (var5 - 4)
    break  # br_table
    break
    var0 = i32_load(var0 + 200)
    if (1 if i32_load(var0 + 200) == 0 else 0):
        break
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    var5 = (i32_load(9142836) + (var0 * 80))
    var6 = i32_load((i32_load(9142836) + (var0 * 80)) + 324)
    if (1 if i32_load((i32_load(9142836) + (var0 * 80)) + 324) == 0 else 0):
        break
    var7 = (((var1 & 0xFFFFFFFF) >> 1) + var3)
    var8 = (((var2 & 0xFFFFFFFF) >> 1) + var4)
    var9 = (var0 * var0)
    var0 = 0
    while True:  # loop $label6
        var10 = i32_load(9142440)
        var3 = i32_load(var5 + 320)
        var2 = (var0 << 2)
        var4 = i32_load((i32_load(var5 + 320) + ((var0 << 2) | 4)))
        var1 = (var7 + i32_load((i32_load(var5 + 320) + ((var0 << 2) | 4))))
        if (1 if i32_load(9142440) <= (var7 + i32_load((i32_load(var5 + 320) + ((var0 << 2) | 4)))) else 0):
            break
        var2 = i32_load((var2 + var3))
        var3 = (var8 + i32_load((var2 + var3)))
        if (1 if var10 <= (var8 + i32_load((var2 + var3))) else 0):
            break
        if (1 if (var1 | var3) < 0 else 0):
            break
        if (1 if var9 >= (((var2 * var2) + (var4 * var4)) - 1) else 0):
            break
        func258(var3, var1)
        var0 = (var0 + 2)
        if (1 if (var0 + 2) < var6 else 0):
            continue
        break  # end loop
    return func129(var3, var1, 1)

