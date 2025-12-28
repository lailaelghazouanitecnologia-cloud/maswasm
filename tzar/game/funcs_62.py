"""
Auto-generated from WAT. Contains 10 functions.
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
# $func454
# ==========================================================
def func454(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    # br_table ['$label0', '$label1', '$label2', '$label3', '$label4', '$label5', '$label6', '$label7', '$label8', '$label9', '$label10', '$label11']
    _br_idx = var2
    break  # br_table
    # call_indirect via table[i32_load(9687580)]
    return
    # call_indirect via table[i32_load(9687580)]
    break
    # call_indirect via table[i32_load(9687584)]
    return
    # Unknown: memory.copy []
    return
    # Unknown: memory.copy []
    break
    if (1 if var1 <= 0 else 0):
        break
    var2 = (var0 + (var1 << 2))
    while True:  # loop $label14
        var1 = i32_load(var0)
        i32_store(var3, (((i32_load(var0) << 24) | ((var1 & 65280) << 8)) | ((((var1 & 0xFFFFFFFF) >> 8) & 65280) | ((var1 & 0xFFFFFFFF) >> 24))))
        var3 = (var3 + 4)
        var0 = (var0 + 4)
        if (1 if (var0 + 4) < var2 else 0):
            continue
        break  # end loop
    break
    if (1 if var1 > 0 else 0):
        var5 = (var0 + (var1 << 2))
        var2 = var3
        while True:  # loop $label15
            var4 = i32_load(var0)
            i32_store(var2, (((i32_load(var0) << 24) | ((var4 & 65280) << 8)) | ((((var4 & 0xFFFFFFFF) >> 8) & 65280) | ((var4 & 0xFFFFFFFF) >> 24))))
            var2 = (var2 + 4)
            var0 = (var0 + 4)
            if (1 if (var0 + 4) < var5 else 0):
                continue
            break  # end loop
    # call_indirect via table[i32_load(9687292)]
    return
    # call_indirect via table[i32_load(9687588)]
    return
    # call_indirect via table[i32_load(9687588)]
    # call_indirect via table[i32_load(9687296)]
    return
    # call_indirect via table[i32_load(9687592)]
    return
    a_c()
    raise RuntimeError('unreachable')
    # call_indirect via table[i32_load(9687576)]
    return
    # call_indirect via table[i32_load(9687292)]


# ==========================================================
# $func456
# ==========================================================
def func456(var0, var1):
    var2 = 0
    if var0:
        if (1 if var1 == 0 else 0):
            break
        var2 = i32_load(var0 + 8)
        if (1 if i32_load(var0 + 8) != i32_load(var1 + 8) else 0):
            break
        # Unknown: memory.copy []
        return
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')


# ==========================================================
# $Rc
# Export: Rc
# ==========================================================
def Rc(var0):
    """Export: Rc"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var1 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var3 = i32_load(9671128)
    if (1 if i32_load8_u(9142917) == 0 else 0):
        var2 = (var3 + (var0 * 132))
        var4 = i32_load((var3 + (var0 * 132)) + 36)
        var2 = (var3 + ((i32_load((var3 + (var0 * 132)) + 36) if var4 else i32_load(var2 + 28)) * 132))
        var4 = ((i32_load8_u((var3 + ((i32_load((var3 + (var0 * 132)) + 36) if var4 else i32_load(var2 + 28)) * 132)) + 122) * 404) + 9568096)
        var5 = i32_load(((i32_load8_u((var3 + ((i32_load((var3 + (var0 * 132)) + 36) if var4 else i32_load(var2 + 28)) * 132)) + 122) * 404) + 9568096) + 216)
        var6 = i32_load16_u(var2 + 112)
        i32_store(var1 + 36, (((i32_load(var4 + 220) << 4) & 2147483632) + (i32_load16_u(var2 + 114) << 5)))
        i32_store(var1 + 32, (((var5 << 4) & 2147483632) + (var6 << 5)))
    var0 = i32_load((var3 + (var0 * 132)) + 40)
    if (1 if i32_load((var3 + (var0 * 132)) + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var1 + 20, var0)
        i32_store(var1 + 16, -65281)
        a_b()
        break
    i32_store(var1 + 4, var0)
    i32_store(var1, 13)
    a_b()
    global global0
    global0 = (var1 + 48)


# ==========================================================
# $fd
# Export: fd
# ==========================================================
def fd():
    """Export: fd"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var0 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var1 = (i32_load(9561692) + (i32_load(9142872) * 286704))
    i64_store(var0 + 16, i64_load(var0 + 32))
    i64_store(var0 + 24, i64_load(var0 + 40))
    var2 = i32_load((var1 + 284000))
    var3 = i32_load((var1 + 284136))
    var4 = i32_load(var1 + 283980)
    i32_store(var0, i32_load(var1 + 283976))
    var1 = (var3 + var4)
    i32_store(var0 + 4, (var2 if (1 if var1 > var2 else 0) else (var3 + var4)))
    global global0
    global0 = (var0 + 48)


# ==========================================================
# $func489
# ==========================================================
def func489(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var4 = 0
    var0 = i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122)
    if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 212) != 1 else 0):
        break
    var5 = i32_load(var2)
    var6 = i32_load(var3)
    var7 = (i32_load(9142440) + 2)
    if (1 if (i32_load((i32_load(9142840) + ((i32_load(var2) + (((i32_load(var3) + (i32_load(9142440) + 2)) + 1) * var7)) << 2)) + 4) - 3) > -3 else 0):
        break
    i32_store(var1 + 12, var5)
    i32_store(var1 + 8, var6)
    if func167((var1 + 12), (var1 + 8), 1, 1, i32_load(((var0 * 404) + 9568096) + 216)):
        i32_store(var2, i32_load(var1 + 12))
        i32_store(var3, i32_load(var1 + 8))
        break
    var4 = 1
    global global0
    global0 = (var1 + 16)
    return var4


# ==========================================================
# $func497
# ==========================================================
def func497(var0):
    var1 = 0
    var1 = i32_load8_u(var0 + 129)
    if (1 if (i32_load8_u(var0 + 129) & 254) != 14 else 0):
        break
    var1 = func301(i32_load16_u(var0 + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110), (-1 if (1 if var1 != 15 else 0) else i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 122)))
    if (1 if func301(i32_load16_u(var0 + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110), (-1 if (1 if var1 != 15 else 0) else i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 122))) == 0 else 0):
        break
    i32_store(var0 + 32, var1)
    return 0


# ==========================================================
# $func519
# ==========================================================
def func519(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var2 = i32_load(9671128)
    var3 = i32_load(var0 + 32)
    var4 = (i32_load(9671128) + (i32_load(var0 + 32) * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 125) == 3 else 0):
        var1 = i32_load(var0 + 84)
        break
    var1 = i32_load(var0 + 84)
    if (1 if i32_load(var0 + 84) > i32_load(var4 + 84) else 0):
        break
    var2 = (var2 + (var3 * 132))
    var1 = func208(i32_load16_u((var2 + (var3 * 132)) + 112), i32_load16_u(var2 + 114), i32_load16_u(var0 + 110), var1)
    if (1 if func208(i32_load16_u((var2 + (var3 * 132)) + 112), i32_load16_u(var2 + 114), i32_load16_u(var0 + 110), var1) == 0 else 0):
        return 1
    i32_store(var0 + 32, var1)
    return 0


# ==========================================================
# $Rb
# Export: Rb
# ==========================================================
def Rb():
    """Export: Rb"""
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
    var2 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var3 = i32_load(9561692)
    var1 = 1
    while True:  # loop $label1
        var0 = (var3 + (var1 * 286704))
        var4 = func88(var0)
        i32_store((var3 + (var1 * 286704)) + 283884, func88(var0))
        i32_store(var0 + 283892, var4)
        var1 = (var1 + 1)
        var0 = i32_load(9142892)
        if (1 if (var1 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    if (1 if var0 < 2 else 0):
        break
    var4 = 1
    while True:  # loop $label4
        var0 = (var3 + (var4 * 286704))
        i32_store((var3 + (var4 * 286704)) + 283944, 1)
        var1 = i32_load(9142892)
        if (1 if i32_load(9142892) >= 2 else 0):
            var5 = (var0 + 283944)
            var7 = (var0 + 283884)
            var6 = 1
            var0 = 1
            while True:  # loop $label3
                if (1 if var0 == var4 else 0):
                    break
                var9 = i32_load((var3 + (var0 * 286704)) + 283884)
                var8 = i32_load(var7)
                if (1 if i32_load((var3 + (var0 * 286704)) + 283884) <= i32_load(var7) else 0):
                    if (1 if var8 != var9 else 0):
                        break
                    if (1 if var0 <= var4 else 0):
                        break
                var6 = (var6 + 1)
                i32_store(var5, (var6 + 1))
                var1 = i32_load(9142892)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) < var1 else 0):
                    continue
                break  # end loop
        var4 = (var4 + 1)
        if (1 if (var4 + 1) < var1 else 0):
            continue
        break  # end loop
    if (1 if var1 < 2 else 0):
        break
    var4 = 1
    while True:  # loop $label10
        var5 = i32_load(9561692)
        var0 = 1
        if (1 if var1 <= 1 else 0):
            break
        while True:  # loop $label6
            if (1 if var4 == i32_load((var5 + (var0 * 286704)) + 283944) else 0):
                break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var1 else 0):
                continue
            break  # end loop
        var0 = var1
        var3 = (var5 + (var0 * 286704))
        if i32_load(9147132):
            if (1 if i32_load(var3 + 284616) == 0 else 0):
                break
        var6 = 0
        var7 = i32_load(9142872)
        var9 = ((i32_load(9142872) * var1) + var0)
        if (1 if i32_load8_u((((i32_load(9142872) * var1) + var0) + i32_load(9143004))) == 0 else 0):
            break
        var6 = 1
        var8 = i32_load(var3 + 281800)
        if (1 if i32_load(var3 + 281800) == 0 else 0):
            break
        var8 = i32_load((var8 + (var7 << 2)))
        if (1 if i32_load((var8 + (var7 << 2))) == 0 else 0):
            break
        var6 = (3 if (1 if ((i32_load(9142848) - var8) * 25) < 60000 else 0) else 2)
        var5 = i32_load((var5 + (var7 * 286704)) + 281800)
        if i32_load((var5 + (var7 * 286704)) + 281800):
            var6 = (4 if i32_load((var5 + (var0 << 2))) else var6)
        var8 = func88(var3)
        var12 = ((i32_load8_u((var3 + 283974)) | (i32_load8_u((var3 + 283973)) << 8)) | (i32_load8_u(var3 + 283972) << 16))
        var10 = i32_load(9143012)
        var1 = (var7 + (var0 * var1))
        var13 = i32_load8_u((i32_load(9143012) + (var7 + (var0 * var1))))
        var10 = i32_load8_u((var9 + var10))
        if i32_load8_u(9216060):
            break
        if i32_load8_u(var3 + 286696):
            break
        var5 = (1 if i32_load8_u(var3 + 286699) != 0 else 0)
        var14 = i32_load(var3 + 284628)
        var7 = i32_load(var3 + 284616)
        var15 = i32_load(var3 + 284608)
        var11 = i32_load(9143016)
        var16 = i32_load8_u((i32_load(9143016) + var1))
        var1 = i32_load(9143008)
        var17 = i32_load8_u((var1 + i32_load(9143008)))
        var11 = i32_load8_u((var9 + var11))
        var1 = i32_load8_u((var1 + var9))
        i32_store(var2 + 16, var10)
        i32_store(var2 + 20, var13)
        i32_store(var2 + 24, var5)
        i32_store(var2 + 28, var1)
        i32_store(var2 + 32, var6)
        i32_store(var2 + 40, var11)
        i32_store(var2 + 44, var0)
        i32_store(var2 + 48, var17)
        i32_store(var2 + 52, var16)
        i32_store(var2 + 56, var15)
        i32_store(var2 + 36, (var7 if var7 else var14))
        i32_store(var2, var4)
        i32_store(var2 + 4, var3)
        i32_store(var2 + 8, var8)
        i32_store(var2 + 12, var12)
        a_b()
        var1 = i32_load(9142892)
        var4 = (var4 + 1)
        if (1 if (var4 + 1) < var1 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var2 - -64)
    return var2


# ==========================================================
# $Zc
# Export: Zc
# ==========================================================
def Zc(var0, var1, var2):
    """Export: Zc"""
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
    var3 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    i32_store(9684428, var1)
    var4 = i32_load((i32_load(9568076) + (12 if (1 if var1 != 1 else 0) else 0)))
    i32_store(9568084, var0)
    var0 = (var4 + (var0 * 196))
    i32_store(9568088, (var4 + (var0 * 196)))
    if (1 if var2 == 0 else 0):
        var11 = i64_load(var0 + 4)
        var12 = i64_load(var0 + 12)
        var2 = i32_load(var0 + 96)
        var4 = i32_load8_u(var0 + 44)
        var5 = i32_load8_u(var0 + 45)
        var6 = i32_load(var0 + 104)
        var7 = i32_load(var0 + 80)
        var8 = i32_load(var0 + 88)
        var13 = i64_load(var0 + 32)
        var9 = i32_load(var0 + 40)
        var10 = i32_load(var0)
        i32_store(var3 + 20, i32_load(var0 + 28))
        i32_store(var3 + 24, var9)
        i64_store(var3 + 28, var13)
        i32_store(var3 + 36, var8)
        i32_store(var3 + 40, var7)
        i32_store(var3 + 44, var6)
        i32_store(var3 + 60, var5)
        i32_store(var3 + 56, var4)
        i32_store(var3 + 52, var1)
        i32_store(var3 + 48, var2)
        i64_store(var3 + 12, var12)
        i64_store(var3 + 4, var11)
        i32_store(var3, var10)
        a_b()
    global global0
    global0 = (var3 - -64)


# ==========================================================
# $ka
# Export: ka
# ==========================================================
def ka(var0, var1):
    """Export: ka"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var3 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var4 = i32_load(9561696)
    var6 = i32_load(9561704)
    if i32_load(9561704):
        while True:  # loop $label1
            var5 = ((var2 << 2) + var4)
            if (1 if i32_load(((var2 << 2) + var4) + 4) >= var0 else 0):
                break
            var2 = (i32_load(var5 + 8) + var2)
            if (1 if (i32_load(var5 + 8) + var2) < var6 else 0):
                continue
            break  # end loop
        var2 = 0
        var0 = 0
        while True:  # loop $label3
            var5 = ((var0 << 2) + var4)
            if (1 if i32_load(((var0 << 2) + var4) + 4) >= var1 else 0):
                break
            var0 = (i32_load(var5 + 8) + var0)
            if (1 if (i32_load(var5 + 8) + var0) < var6 else 0):
                continue
            break  # end loop
    var0 = 0
    i32_store(var3 + 4, (var0 - var2))
    i32_store(var3, (var4 + (var2 << 2)))
    global global0
    global0 = (var3 + 16)

