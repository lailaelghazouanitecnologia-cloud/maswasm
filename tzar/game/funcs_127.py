"""
Auto-generated from WAT. Contains 5 functions.
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
# $func462
# ==========================================================
def func462(var0, var1, var2):
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
    var5 = i32_load(var1 + 8)
    var6 = i32_load(var1 + 12)
    if (1 if i32_load(var1 + 8) >= i32_load(var1 + 12) else 0):
        var3 = i32_load(var2 + 12)
        var8 = (var6 - i32_load(var2 + 12))
        if (1 if (var6 - i32_load(var2 + 12)) <= 0 else 0):
            break
        var9 = (i32_load(var1 + 4) + var3)
        var10 = i32_load(var1)
        var3 = i32_load(var0 + 24)
        var6 = i32_load(var0 + 28)
        if (1 if i32_load(var0 + 24) < i32_load(var0 + 28) else 0):
            i32_store(var3 + 12, var8)
            i32_store(var3 + 8, var5)
            i32_store(var3 + 4, var9)
            i32_store(var3, var10)
            i32_store(var0 + 24, (var3 + 16))
            break
        var3 = i32_load((var0 + 20))
        var11 = (var3 - i32_load((var0 + 20)))
        var12 = ((var3 - i32_load((var0 + 20))) >> 4)
        var4 = (((var3 - i32_load((var0 + 20))) >> 4) + 1)
        if (1 if (((var3 - i32_load((var0 + 20))) >> 4) + 1) >= 268435456 else 0):
            break
        var6 = (var6 - var3)
        var7 = ((var6 - var3) >> 3)
        var6 = (268435455 if (1 if var6 >= 2147483632 else 0) else (((var6 - var3) >> 3) if (1 if var4 < var7 else 0) else var4))
        if (268435455 if (1 if var6 >= 2147483632 else 0) else (((var6 - var3) >> 3) if (1 if var4 < var7 else 0) else var4)):
            if (1 if var6 >= 268435456 else 0):
                break
        else:
        var7 = 0
        var4 = (0 + (var12 << 4))
        i32_store((0 + (var12 << 4)) + 12, var8)
        i32_store(var4 + 8, var5)
        i32_store(var4 + 4, var9)
        i32_store(var4, var10)
        # Unknown: memory.copy []
        i32_store(var0 + 28, (var7 + (var6 << 4)))
        i32_store(var0 + 24, (var4 + 16))
        i32_store(var0 + 20, var7)
        if (1 if var3 == 0 else 0):
            break
        var3 = i32_load(var2 + 8)
        var5 = (i32_load(var1 + 8) - i32_load(var2 + 8))
        if (1 if (i32_load(var1 + 8) - i32_load(var2 + 8)) <= 0 else 0):
            break
        var6 = (i32_load(var1) + var3)
        var7 = i32_load(var2 + 12)
        var8 = i32_load(var1 + 4)
        var1 = i32_load(var0 + 24)
        var3 = i32_load(var0 + 28)
        if (1 if i32_load(var0 + 24) < i32_load(var0 + 28) else 0):
            i32_store(var1 + 12, var7)
            i32_store(var1 + 8, var5)
            i32_store(var1 + 4, var8)
            i32_store(var1, var6)
            break
        var1 = i32_load((var0 + 20))
        var9 = (var1 - i32_load((var0 + 20)))
        var10 = ((var1 - i32_load((var0 + 20))) >> 4)
        var2 = (((var1 - i32_load((var0 + 20))) >> 4) + 1)
        if (1 if (((var1 - i32_load((var0 + 20))) >> 4) + 1) >= 268435456 else 0):
            break
        var3 = (var3 - var1)
        var4 = ((var3 - var1) >> 3)
        var3 = (268435455 if (1 if var3 >= 2147483632 else 0) else (((var3 - var1) >> 3) if (1 if var2 < var4 else 0) else var2))
        if (268435455 if (1 if var3 >= 2147483632 else 0) else (((var3 - var1) >> 3) if (1 if var2 < var4 else 0) else var2)):
            if (1 if var3 >= 268435456 else 0):
                break
        else:
        var4 = 0
        var2 = (0 + (var10 << 4))
        i32_store((0 + (var10 << 4)) + 12, var7)
        i32_store(var2 + 8, var5)
        i32_store(var2 + 4, var8)
        i32_store(var2, var6)
        # Unknown: memory.copy []
        i32_store(var0 + 28, (var4 + (var3 << 4)))
        i32_store(var0 + 24, (var2 + 16))
        i32_store(var0 + 20, var4)
        if (1 if var1 == 0 else 0):
            break
        return af(var1)
    var3 = i32_load(var2 + 8)
    var8 = (var5 - i32_load(var2 + 8))
    if (1 if (var5 - i32_load(var2 + 8)) <= 0 else 0):
        break
    var9 = (i32_load(var1) + var3)
    var10 = i32_load(var1 + 4)
    var3 = i32_load(var0 + 24)
    var5 = i32_load(var0 + 28)
    if (1 if i32_load(var0 + 24) < i32_load(var0 + 28) else 0):
        i32_store(var3 + 12, var6)
        i32_store(var3 + 8, var8)
        i32_store(var3 + 4, var10)
        i32_store(var3, var9)
        i32_store(var0 + 24, (var3 + 16))
        break
    var3 = i32_load((var0 + 20))
    var11 = (var3 - i32_load((var0 + 20)))
    var12 = ((var3 - i32_load((var0 + 20))) >> 4)
    var4 = (((var3 - i32_load((var0 + 20))) >> 4) + 1)
    if (1 if (((var3 - i32_load((var0 + 20))) >> 4) + 1) >= 268435456 else 0):
        break
    var5 = (var5 - var3)
    var7 = ((var5 - var3) >> 3)
    var5 = (268435455 if (1 if var5 >= 2147483632 else 0) else (((var5 - var3) >> 3) if (1 if var4 < var7 else 0) else var4))
    if (268435455 if (1 if var5 >= 2147483632 else 0) else (((var5 - var3) >> 3) if (1 if var4 < var7 else 0) else var4)):
        if (1 if var5 >= 268435456 else 0):
            break
    else:
    var7 = 0
    var4 = (0 + (var12 << 4))
    i32_store((0 + (var12 << 4)) + 12, var6)
    i32_store(var4 + 8, var8)
    i32_store(var4 + 4, var10)
    i32_store(var4, var9)
    # Unknown: memory.copy []
    i32_store(var0 + 28, (var7 + (var5 << 4)))
    i32_store(var0 + 24, (var4 + 16))
    i32_store(var0 + 20, var7)
    if (1 if var3 == 0 else 0):
        break
    var3 = i32_load(var2 + 12)
    var5 = (i32_load(var1 + 12) - i32_load(var2 + 12))
    if (1 if (i32_load(var1 + 12) - i32_load(var2 + 12)) <= 0 else 0):
        break
    var6 = (i32_load(var1 + 4) + var3)
    var7 = i32_load(var2 + 8)
    var8 = i32_load(var1)
    var1 = i32_load(var0 + 24)
    var3 = i32_load(var0 + 28)
    if (1 if i32_load(var0 + 24) < i32_load(var0 + 28) else 0):
        i32_store(var1 + 12, var5)
        i32_store(var1 + 8, var7)
        i32_store(var1 + 4, var6)
        i32_store(var1, var8)
        break
    var1 = i32_load((var0 + 20))
    var9 = (var1 - i32_load((var0 + 20)))
    var10 = ((var1 - i32_load((var0 + 20))) >> 4)
    var2 = (((var1 - i32_load((var0 + 20))) >> 4) + 1)
    if (1 if (((var1 - i32_load((var0 + 20))) >> 4) + 1) >= 268435456 else 0):
        break
    var3 = (var3 - var1)
    var4 = ((var3 - var1) >> 3)
    var3 = (268435455 if (1 if var3 >= 2147483632 else 0) else (((var3 - var1) >> 3) if (1 if var2 < var4 else 0) else var2))
    if (268435455 if (1 if var3 >= 2147483632 else 0) else (((var3 - var1) >> 3) if (1 if var2 < var4 else 0) else var2)):
        if (1 if var3 >= 268435456 else 0):
            break
    else:
    var4 = 0
    var2 = (0 + (var10 << 4))
    i32_store((0 + (var10 << 4)) + 12, var5)
    i32_store(var2 + 8, var7)
    i32_store(var2 + 4, var6)
    i32_store(var2, var8)
    # Unknown: memory.copy []
    i32_store(var0 + 28, (var4 + (var3 << 4)))
    i32_store(var0 + 24, (var2 + 16))
    i32_store(var0 + 20, var4)
    if (1 if var1 == 0 else 0):
        break
    return af(var1)
    func42()
    raise RuntimeError('unreachable')
    func68()
    raise RuntimeError('unreachable')
    func42()
    raise RuntimeError('unreachable')
    func42()
    raise RuntimeError('unreachable')
    func42()
    raise RuntimeError('unreachable')
    i32_store(var0 + 24, (var1 + 16))
    return var9


# ==========================================================
# $cd
# Export: cd
# ==========================================================
def cd(var0, var1):
    """Export: cd"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var1 = ((9684460 if (1 if var1 == 1 else 0) else 9684476) if var1 else 9684444)
    i32_store(((9684460 if (1 if var1 == 1 else 0) else 9684476) if var1 else 9684444) + 8, 0)
    var2 = i32_load(var1 + 4)
    if (1 if var0 >= i32_load(var1 + 4) else 0):
        var2 = (i32_load(var1 + 12) + (var0 + var2))
        i32_store(var1 + 4, (i32_load(var1 + 12) + (var0 + var2)))
        var3 = i32_load(var1)
        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        if var3:
        i32_store(var1, var2)
    if (1 if var0 == 0 else 0):
        break
    var6 = (var0 & 1)
    var3 = i32_load(var1)
    var2 = 0
    if (1 if var0 != 1 else 0):
        var7 = (var0 & -2)
        var0 = 0
        while True:  # loop $label1
            var4 = (var2 << 2)
            var5 = i32_load(((var2 << 2) + 9147392))
            var8 = i32_load(var1 + 8)
            i32_store(var1 + 8, (i32_load(var1 + 8) + 1))
            i32_store((var3 + (var8 << 2)), var5)
            var4 = i32_load(((var4 | 4) + 9147392))
            var5 = i32_load(var1 + 8)
            i32_store(var1 + 8, (i32_load(var1 + 8) + 1))
            i32_store((var3 + (var5 << 2)), var4)
            var2 = (var2 + 2)
            var0 = (var0 + 2)
            if (1 if (var0 + 2) != var7 else 0):
                continue
            break  # end loop
    if (1 if var6 == 0 else 0):
        break
    var0 = i32_load(((var2 << 2) + 9147392))
    var1 = i32_load(var1 + 8)
    i32_store(var1 + 8, (i32_load(var1 + 8) + 1))
    i32_store((var3 + (var1 << 2)), var0)


# ==========================================================
# $za
# Export: za
# ==========================================================
def za(var0):
    """Export: za"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var2 = i32_load(9142892)
    i32_store(9142892, var0)
    var7 = (i64_extend_u(var0) * 286704)
    var1 = (-1 if i32(((var7 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var0) * 286704)))
    var5 = func26((-1 if i32(((var7 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var0) * 286704))))
    # Unknown: memory.fill []
    var1 = i32_load(9561692)
    var2 = (var2 if (1 if var0 > var2 else 0) else var0)
    if (var2 if (1 if var0 > var2 else 0) else var0):
        if (1 if var2 >= 4 else 0):
            var6 = (var2 & -4)
            var0 = 0
            while True:  # loop $label0
                var4 = (var3 * 286704)
                # Unknown: memory.copy []
                var4 = ((var3 | 1) * 286704)
                # Unknown: memory.copy []
                var4 = ((var3 | 2) * 286704)
                # Unknown: memory.copy []
                var4 = ((var3 | 3) * 286704)
                # Unknown: memory.copy []
                var3 = (var3 + 4)
                var0 = (var0 + 4)
                if (1 if (var0 + 4) != var6 else 0):
                    continue
                break  # end loop
        var2 = (var2 & 3)
        if (1 if (var2 & 3) == 0 else 0):
            break
        var0 = 0
        while True:  # loop $label2
            var6 = (var3 * 286704)
            # Unknown: memory.copy []
            var3 = (var3 + 1)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var2 else 0):
                continue
            break  # end loop
        break
    if (1 if var1 == 0 else 0):
        break
    i32_store(9561692, var5)


# ==========================================================
# $qd
# Export: qd
# ==========================================================
def qd(var0):
    """Export: qd"""
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
    var7 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if i32_load8_u(9142916):
        var1 = i32_load(9142892)
        var12 = (var1 * 3)
        var2 = func26((-1 if (1 if (var1 * 3) > 1073741823 else 0) else (i32_load(9142892) * 12)))
        if (1 if var1 == 0 else 0):
            break
        var6 = i32_load(9142872)
        var10 = (i32_load(9142872) * var1)
        var11 = i32_load(9143012)
        var8 = i32_load(9143004)
        var3 = i32_load(9561692)
        if (1 if var0 == 0 else 0):
            var0 = 0
            while True:  # loop $label1
                var9 = (var2 + (var4 << 2))
                var5 = (var3 + (var0 * 286704))
                i32_store((var2 + (var4 << 2)), ((i32_load16_u((var3 + (var0 * 286704)) + 283972) | (i32_load8_u((var5 + 283974)) << 16)) | -16777216))
                i32_store(var9 + 4, i32_load8_u((var8 + ((i32_load(var5 + 283908) * var1) + var6))))
                i32_store(var9 + 8, i32_load8_u((var11 + (i32_load(var5 + 283908) + var10))))
                var4 = (var4 + 3)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var1 else 0):
                    continue
                break  # end loop
            break
        i32_store(var2, ((i32_load16_u(var3 + 283972) | (i32_load8_u((var3 + 283974)) << 16)) | -16777216))
        i32_store(var2 + 4, i32_load8_u((var8 + ((i32_load(var3 + 283908) * var1) + var6))))
        i32_store(var2 + 8, i32_load8_u((var11 + (i32_load(var3 + 283908) + var10))))
        var0 = 1
        if (1 if var1 == 1 else 0):
            break
        var4 = 3
        while True:  # loop $label2
            var5 = (var2 + (var4 << 2))
            if (1 if var0 != var6 else 0):
            else:
            i32_store((-16776961 if i32_load8_u((var8 + (var6 + (var0 * var1)))) else -16711936), -65536)
            var9 = (var3 + (var0 * 286704))
            i32_store(var5 + 4, i32_load8_u((var8 + ((i32_load((var3 + (var0 * 286704)) + 283908) * var1) + var6))))
            i32_store(var5 + 8, i32_load8_u((var11 + (i32_load(var9 + 283908) + var10))))
            var4 = (var4 + 3)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var1 else 0):
                continue
            break  # end loop
        i32_store(var7 + 4, var12)
        i32_store(var7, var2)
    global global0
    global0 = (var7 + 16)
    return af(var2)


# ==========================================================
# $func492
# ==========================================================
def func492(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = i32_load(var1 + 24)
    if (1 if i32_load(var1 + 24) == 0 else 0):
        var2 = func26(16)
        i64_store(func26(16), 0)
        i64_store(var2 + 8, 0)
        i32_store(var1 + 24, var2)
    if (1 if i32_load(var2 + 12) == 0 else 0):
        var3 = func26(16)
        i32_store(func26(16) + 4, 16)
        i32_store(var3, func26(64))
        i64_store(var3 + 8, 4294967296)
        i32_store(var2 + 12, var3)
        while True:  # loop $label1
            var2 = i32_load(i32_load(var1 + 24) + 12)
            var3 = i32_load(i32_load(i32_load(var1 + 24) + 12) + 8)
            if (1 if i32_load(i32_load(i32_load(var1 + 24) + 12) + 8) != i32_load(var2 + 4) else 0):
                var4 = i32_load(var2)
                break
            var4 = (i32_load(var2 + 12) + var3)
            i32_store(var2 + 4, (i32_load(var2 + 12) + var3))
            var5 = i32_load(var2)
            var4 = func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2)))
            if var3:
                # Unknown: memory.copy []
            if var5:
                var3 = i32_load(var2 + 8)
            i32_store(var2, var4)
            i32_store(var2 + 8, (var3 + 1))
            i32_store((var4 + (var3 << 2)), 0)
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != 16 else 0):
                continue
            break  # end loop
    var1 = i32_load(i32_load(var1 + 24) + 12)
    var2 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) >= 16777216 else 0):
        var2 = i32_load(((i32_load(var1) + (var2 << 2)) - 67108864))
    var3 = i32_load(var0 + 36)
    # br_table ['$label2', '$label3', '$label4', '$label5', '$label6', '$label7']
    _br_idx = i32_load(var0 + 28)
    break  # br_table
    i32_store((i32_load(var1) + (var3 << 2)), var2)
    return
    var0 = (i32_load(var1) + (var3 << 2))
    i32_store((i32_load(var1) + (var3 << 2)), (i32_load(var0) + var2))
    return
    var0 = (i32_load(var1) + (var3 << 2))
    i32_store((i32_load(var1) + (var3 << 2)), (i32_load(var0) - var2))
    return
    var0 = (i32_load(var1) + (var3 << 2))
    i32_store((i32_load(var1) + (var3 << 2)), (i32_load(var0) * var2))
    return
    var0 = (i32_load(var1) + (var3 << 2))
    i32_store((i32_load(var1) + (var3 << 2)), ((i32_load(var0) & 0xFFFFFFFF) // var2))

