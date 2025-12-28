"""
Auto-generated from WAT. Contains 15 functions.
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
# $Wc
# Export: Wc
# ==========================================================
def Wc(var0):
    """Export: Wc"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var1 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var2 = i32_load(9568088)
    i64_store(i32_load(9568088) + 4, 0)
    i32_store(var2, var0)
    i64_store(var2 + 36, 0)
    i64_store(var2 + 28, 0)
    i64_store(var2 + 20, 0)
    i64_store(var2 + 12, 0)
    i32_store(var2 + 104, 0)
    i32_store(var2 + 88, 0)
    i32_store(var2 + 72, 0)
    i32_store(var2 + 56, 0)
    var3 = i32_load8_u(var2 + 45)
    var4 = i32_load8_u(var2 + 44)
    var5 = i32_load(var2 + 96)
    i32_store(var1 + 40, i32_load(var2 + 80))
    i64_store(var1 + 16, 0)
    i64_store(var1 + 24, 0)
    i64_store(var1 + 32, 0)
    i32_store(var1 + 44, 0)
    i32_store(var1 + 48, var5)
    i32_store(var1 + 56, var4)
    i32_store(var1 + 60, var3)
    i32_store(var1 + 52, i32_load(9684428))
    i32_store(var1, var0)
    i32_store(var1 + 4, 0)
    i64_store(var1 + 8, 0)
    a_b()
    global global0
    global0 = (var1 - -64)


# ==========================================================
# $func893
# ==========================================================
def func893(var0, var1):
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if var0 == 0 else 0):
        break
    if (1 if i32_load(9213808) == 0 else 0):
        break
    var0 = i32_load8_u(9142917)
    var2 = i32_load(9140320)
    if i32_load(9140320):
        if var0:
            break
        var0 = i32_load(9671128)
        var0 = (var0 + (var2 * 132))
        var2 = i32_load((var0 + (var2 * 132)) + 36)
        var2 = (i32_load(9671128) + ((i32_load((var0 + (var2 * 132)) + 36) if var2 else i32_load(var0 + 28)) * 132))
        var0 = i32_load8_u((i32_load(9671128) + ((i32_load((var0 + (var2 * 132)) + 36) if var2 else i32_load(var0 + 28)) * 132)) + 122)
        var3 = (((i32_load(((i32_load8_u((i32_load(9671128) + ((i32_load((var0 + (var2 * 132)) + 36) if var2 else i32_load(var0 + 28)) * 132)) + 122) * 404) + 9568096) + 220) << 4) & 2147483632) + (i32_load16_u(var2 + 114) << 5))
        break
    if var0:
        break
    var0 = i32_load(9671128)
    var0 = (var0 + (i32_load(9173808) * 132))
    var2 = i32_load((var0 + (i32_load(9173808) * 132)) + 36)
    var2 = (i32_load(9671128) + ((i32_load((var0 + (i32_load(9173808) * 132)) + 36) if var2 else i32_load(var0 + 28)) * 132))
    var0 = i32_load8_u((i32_load(9671128) + ((i32_load((var0 + (i32_load(9173808) * 132)) + 36) if var2 else i32_load(var0 + 28)) * 132)) + 122)
    var3 = (((i32_load(((i32_load8_u((i32_load(9671128) + ((i32_load((var0 + (i32_load(9173808) * 132)) + 36) if var2 else i32_load(var0 + 28)) * 132)) + 122) * 404) + 9568096) + 220) << 4) & 2147483632) + (i32_load16_u(var2 + 114) << 5))
    var2 = (var2 + 112)
    var0 = i32_load(((var0 * 404) + 9568096) + 216)
    var2 = i32_load16_u(var2)
    i32_store(var1 + 4, var3)
    i32_store(var1, (((var0 << 4) & 2147483632) + (var2 << 5)))
    global global0
    global0 = (var1 + 16)
    return var1


# ==========================================================
# $ed
# Export: ed
# ==========================================================
def ed(var0, var1, var2, var3, var4, var5):
    """Export: ed"""
    var6 = 0
    var6 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    i32_store(9142860, var1)
    i32_store(9142856, var0)
    i32_store(9142864, var2)
    i32_store(9142868, var3)
    if (1 if var3 > 489 else 0):
        break
    var0 = i32_load(9142884)
    if i32_load8_u(9142916):
        i32_store(var6 + 32, var0)
        a_b()
        break
    i32_store(var6 + 24, var0)
    i64_store(var6 + 16, -4602115869219225600)
    i64_store(var6 + 8, 0)
    i64_store(var6, 0)
    a_b()
    i32_store(9147148, var5)
    i32_store(9147144, var4)
    global global0
    global0 = (var6 + 48)


# ==========================================================
# $func901
# ==========================================================
def func901(var0, var1):
    var2 = 0
    var3 = 0
    var1 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var2 = i32_load(9671128)
    var3 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var3 + 128) == 0 else 0):
        break
    var0 = (var2 + (var0 * 132))
    i32_store8((var2 + (var0 * 132)) + 127, 0)
    var2 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var1 + 20, var2)
        i32_store(var1 + 16, 0)
        a_b()
        break
    var0 = i32_load16_u(var0 + 110)
    i32_store(var1 + 4, var2)
    i32_store(var1, (var0 + 16))
    a_b()
    i32_store8(var3 + 128, 0)
    global global0
    global0 = (var1 + 32)


# ==========================================================
# $func907
# ==========================================================
def func907(var0):
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
    var6 = i32_load(9671128)
    var2 = i32_load(var0 + 32)
    var3 = (i32_load(9671128) + (i32_load(var0 + 32) * 132))
    var4 = i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 122)
    if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 122) * 404) + 9568096) + 188) != 55 else 0):
        break
    if (1 if i32_load(var3 + 64) < i32_load(var3 + 68) else 0):
        if (1 if i32_load8_u((var6 + (var2 * 132)) + 125) != 3 else 0):
            break
    var4 = i32_load(((var4 * 404) + 9568096) + 192)
    if (1 if i32_load(((var4 * 404) + 9568096) + 192) > 3 else 0):
        break
    var1 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        break
    if (1 if i32_load(var1 + 8) < 3 else 0):
        break
    if (1 if (i32_load(i32_load(var1)) - 1) < 2 else 0):
        break
    var1 = 0
    var2 = i32_load8_u(var0 + 129)
    if i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 286684):
        # br_table ['$label3', '$label4', '$label1', '$label5', '$label1']
        _br_idx = (var2 - 1)
        break  # br_table
    # br_table ['$label3', '$label4', '$label4', '$label5', '$label4']
    _br_idx = (var2 - 1)
    break  # br_table
    var1 = i32_load(38504)
    break
    var1 = i32_load(38508)
    var1 = func224(var3, var4, var1)
    if (1 if func224(var3, var4, var1) == 0 else 0):
        break
    i32_store8(var0 + 123, 1)
    i32_store(var0 + 32, var1)
    i32_store((var6 + (var1 * 132)) + 88, i32_load(9142848))
    return 0
    var8 = i32_load16_u(var0 + 112)
    var12 = (i32_load16_u(var0 + 112) + 29)
    var9 = i32_load16_u(var0 + 114)
    var13 = (i32_load16_u(var0 + 114) + 29)
    var10 = i32_load(9142440)
    var11 = (i32_load(9142440) + 2)
    var14 = (var9 - 30)
    var3 = (var8 - 30)
    var15 = i32_load(9142840)
    var7 = 2147483647
    var16 = i32_load16_u(var0 + 110)
    while True:  # loop $label8
        var4 = (var3 + 1)
        if (1 if var3 < var10 else 0):
            var1 = (var3 - var8)
            var17 = ((var3 - var8) * var1)
            var1 = var14
            while True:  # loop $label7
                var2 = var1
                if (1 if var10 <= var1 else 0):
                    break
                if (1 if (var2 | var3) < 0 else 0):
                    break
                var1 = (var2 - var9)
                var1 = (((var2 - var9) * var1) + var17)
                if (1 if (((var2 - var9) * var1) + var17) >= var7 else 0):
                    break
                var1 = (var6 + (i32_load((var15 + (((((var2 + var11) + 1) * var11) + var4) << 2))) * 132))
                var18 = ((1 if i32_load8_u((var6 + (i32_load((var15 + (((((var2 + var11) + 1) * var11) + var4) << 2))) * 132)) + 125) == 4 else 0) & (1 if i32_load16_u(var1 + 110) == var16 else 0))
                var7 = (var1 if ((1 if i32_load8_u((var6 + (i32_load((var15 + (((((var2 + var11) + 1) * var11) + var4) << 2))) * 132)) + 125) == 4 else 0) & (1 if i32_load16_u(var1 + 110) == var16 else 0)) else var7)
                var5 = (i32_load(var1 + 28) if var18 else var5)
                var1 = (var2 + 1)
                if (1 if var2 != var13 else 0):
                    continue
                break  # end loop
        var1 = (1 if var3 == var12 else 0)
        var3 = var4
        if (1 if var1 == 0 else 0):
            continue
        break  # end loop
    if (1 if var5 == 0 else 0):
        return 1
    i32_store(var0 + 32, var5)
    return 0


# ==========================================================
# $func908
# ==========================================================
def func908(var0):
    i32_store(9681476, 9681696)
    i32_store(9681464, 0)
    i32_store(9681468, 0)
    i32_store(9681472, i32_load(((i32_load(9681696) * 404) + 9568096) + 68))


# ==========================================================
# $Bc
# Export: Bc
# ==========================================================
def Bc(var0, var1, var2, var3, var4):
    """Export: Bc"""
    var5 = 0
    var5 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if (1 if i32_load8_u(9142916) == 0 else 0):
        i32_store(var5 + 32, var3)
        f64_store(var5 + 24, float(var4))
        f64_store(var5 + 16, float(var2))
        f64_store(var5 + 8, float(var1))
        f64_store(var5, float(var0))
        a_b()
    global global0
    global0 = (var5 + 48)


# ==========================================================
# $func913
# ==========================================================
def func913(var0):
    var1 = 0
    var1 = i32_load8_u(var0 + 129)
    if (1 if (i32_load8_u(var0 + 129) & 254) != 14 else 0):
        break
    var1 = func416(i32_load16_u(var0 + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110), (-1 if (1 if var1 != 15 else 0) else i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 122)))
    if (1 if func416(i32_load16_u(var0 + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110), (-1 if (1 if var1 != 15 else 0) else i32_load8_u((i32_load(9671128) + (i32_load(var0 + 32) * 132)) + 122))) == 0 else 0):
        break
    i32_store(var0 + 32, var1)
    return 0


# ==========================================================
# $bf
# Export: bf
# ==========================================================
def bf():
    """Export: bf"""
    var0 = 0
    var1 = 0
    var2 = 0
    var0 = global1
    var2 = global3
    var1 = i32_load(global3 + 116)
    if i32_load(global3 + 116):
        i32_store(var2 + 116, 0)
        global global1
        global1 = var1
        # Unknown: memory.fill []
        return var1
    if (global2 if var0 else 1):
        global global2
        global2 = 1
        var0 = e()
    global global1
    global1 = var0
    # Unknown: memory.fill []
    return var0


# ==========================================================
# $func941
# ==========================================================
def func941(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var3 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var4 = i32_load(var0 + 28)
    i32_store(var3 + 16, i32_load(var0 + 28))
    var5 = i32_load(var0 + 20)
    i32_store(var3 + 28, var2)
    i32_store(var3 + 24, var1)
    var1 = (var5 - var4)
    i32_store(var3 + 20, (var5 - var4))
    var5 = (var1 + var2)
    var7 = 2
    var1 = (var3 + 16)
    var4 = a_h()
    if a_h():
        i32_store(global3 + 28, var4)
    else:
    if 0:
        var4 = var1
        break
    while True:  # loop $label3
        var6 = i32_load(var3 + 12)
        if (1 if var5 == i32_load(var3 + 12) else 0):
            break
        if (1 if var6 < 0 else 0):
            var4 = var1
            break
        var8 = i32_load(var1 + 4)
        var9 = (1 if var6 > i32_load(var1 + 4) else 0)
        var4 = (var1 + ((1 if var6 > i32_load(var1 + 4) else 0) << 3))
        var8 = (var6 - (var8 if var9 else 0))
        i32_store((var1 + ((1 if var6 > i32_load(var1 + 4) else 0) << 3)), ((var6 - (var8 if var9 else 0)) + i32_load(var4)))
        var1 = (var1 + (12 if var9 else 4))
        i32_store((var1 + (12 if var9 else 4)), (i32_load(var1) - var8))
        var5 = (var5 - var6)
        var1 = var4
        var7 = (var7 - var9)
        var6 = a_h()
        if a_h():
            i32_store(global3 + 28, var6)
        else:
        if (1 if 0 == 0 else 0):
            continue
        break  # end loop
    if (1 if var5 != -1 else 0):
        break
    var1 = i32_load(var0 + 44)
    i32_store(var0 + 28, i32_load(var0 + 44))
    i32_store(var0 + 20, var1)
    i32_store(var0 + 16, (var1 + i32_load(var0 + 48)))
    break
    i32_store(var0 + 28, 0)
    i64_store(var0 + 16, 0)
    i32_store(var0, (i32_load(var0) | 32))
    if (1 if var7 == 2 else 0):
        break
    var0 = (var2 - i32_load(var4 + 4))
    global global0
    global0 = (var3 + 32)
    return var0


# ==========================================================
# $func942
# ==========================================================
def func942(var0, var1, var2):
    var3 = 0
    var3 = i32_load(var0 + 60)
    var0 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var2 = a_j()
    if a_j():
        i32_store(global3 + 28, var2)
    else:
    var2 = 0
    var1 = i64_load(var0 + 8)
    global global0
    global0 = (var0 + 16)
    return (-1 if var2 else var1)


# ==========================================================
# $func946
# ==========================================================
def func946(var0, var1, var2, var3, var4):
    if func79(var0, i32_load(var1 + 8), var4):
        if (1 if i32_load(var1 + 4) != var2 else 0):
            break
        if (1 if i32_load(var1 + 28) == 1 else 0):
            break
        i32_store(var1 + 28, var3)
        return
    if func79(var0, i32_load(var1), var4):
        if (1 if var2 != i32_load(var1 + 16) else 0):
            if (1 if i32_load(var1 + 20) != var2 else 0):
                break
        if (1 if var3 != 1 else 0):
            break
        i32_store(var1 + 32, 1)
        return
        i32_store(var1 + 32, var3)
        if (1 if i32_load(var1 + 44) == 4 else 0):
            break
        i32_store16(var1 + 52, 0)
        var0 = i32_load(var0 + 8)
        # call_indirect via table[i32_load(i32_load(var0) + 20)]
        if i32_load8_u(var1 + 53):
            i32_store(var1 + 44, 3)
            if (1 if i32_load8_u(var1 + 52) == 0 else 0):
                break
            break
        i32_store(var1 + 44, 4)
        i32_store(var1 + 20, var2)
        i32_store(var1 + 40, (i32_load(var1 + 40) + 1))
        if (1 if i32_load(var1 + 36) != 1 else 0):
            break
        if (1 if i32_load(var1 + 24) != 2 else 0):
            break
        i32_store8(var1 + 54, 1)
        return
    var0 = i32_load(var0 + 8)
    # call_indirect via table[i32_load(i32_load(var0) + 24)]


# ==========================================================
# $func947
# ==========================================================
def func947(var0, var1, var2, var3, var4, var5):
    if func79(var0, i32_load(var1 + 8), var5):
        func441(var1, var2, var3, var4)
        return
    var0 = i32_load(var0 + 8)
    # call_indirect via table[i32_load(i32_load(var0) + 20)]


# ==========================================================
# $func948
# ==========================================================
def func948(var0, var1, var2, var3):
    if func79(var0, i32_load(var1 + 8), 0):
        func442(var1, var2, var3)
        return
    var0 = i32_load(var0 + 8)
    # call_indirect via table[i32_load(i32_load(var0) + 28)]


# ==========================================================
# $func949
# ==========================================================
def func949(var0, var1, var2, var3, var4):
    if func79(var0, i32_load(var1 + 8), var4):
        if (1 if i32_load(var1 + 4) != var2 else 0):
            break
        if (1 if i32_load(var1 + 28) == 1 else 0):
            break
        i32_store(var1 + 28, var3)
        return
    if (1 if func79(var0, i32_load(var1), var4) == 0 else 0):
        break
    if (1 if var2 != i32_load(var1 + 16) else 0):
        if (1 if i32_load(var1 + 20) != var2 else 0):
            break
    if (1 if var3 != 1 else 0):
        break
    i32_store(var1 + 32, 1)
    return
    i32_store(var1 + 20, var2)
    i32_store(var1 + 32, var3)
    i32_store(var1 + 40, (i32_load(var1 + 40) + 1))
    if (1 if i32_load(var1 + 36) != 1 else 0):
        break
    if (1 if i32_load(var1 + 24) != 2 else 0):
        break
    i32_store8(var1 + 54, 1)
    i32_store(var1 + 44, 4)

