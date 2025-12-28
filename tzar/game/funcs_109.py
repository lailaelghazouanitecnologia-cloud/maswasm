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
# $func226
# ==========================================================
def func226(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    i32_store(var0 + 8, 0)
    i64_store(var0, 0)
    var2 = i32_load(var1 + 4)
    var4 = i32_load(var1)
    var5 = (i32_load(var1 + 4) - i32_load(var1))
    var3 = ((i32_load(var1 + 4) - i32_load(var1)) // 196)
    if (1 if var2 != var4 else 0):
        if (1 if var3 >= 21913099 else 0):
            break
        var2 = func26(var5)
        i32_store(var0 + 4, func26(var5))
        i32_store(var0, var2)
        i32_store(var0 + 8, (var2 + (var3 * 196)))
        var3 = i32_load(var1)
        var4 = i32_load(var1 + 4)
        if (1 if i32_load(var1) != i32_load(var1 + 4) else 0):
            while True:  # loop $label1
                # Unknown: memory.copy []
                var2 = (var2 + 196)
                var3 = (var3 + 196)
                if (1 if (var3 + 196) != var4 else 0):
                    continue
                break  # end loop
        i32_store(var0 + 4, var2)
    i64_store(var0 + 12, 0)
    i32_store(var0 + 20, 0)
    var2 = i32_load(var1 + 16)
    var4 = i32_load(var1 + 12)
    var5 = (i32_load(var1 + 16) - i32_load(var1 + 12))
    var3 = ((i32_load(var1 + 16) - i32_load(var1 + 12)) // 196)
    if (1 if var2 != var4 else 0):
        if (1 if var3 >= 21913099 else 0):
            break
        var2 = func26(var5)
        i32_store(var0 + 16, func26(var5))
        i32_store(var0 + 12, var2)
        i32_store(var0 + 20, (var2 + (var3 * 196)))
        var3 = i32_load(var1 + 12)
        var4 = i32_load(var1 + 16)
        if (1 if i32_load(var1 + 12) != i32_load(var1 + 16) else 0):
            while True:  # loop $label3
                # Unknown: memory.copy []
                var2 = (var2 + 196)
                var3 = (var3 + 196)
                if (1 if (var3 + 196) != var4 else 0):
                    continue
                break  # end loop
        i32_store(var0 + 16, var2)
    # Unknown: memory.copy []
    return var0
    func42()
    raise RuntimeError('unreachable')
    func42()
    raise RuntimeError('unreachable')
    return 104


# ==========================================================
# $func289
# ==========================================================
def func289(var0, var1, var2):
    var3 = 0
    var4 = 0
    var3 = i32_load8_u(var0 + 122)
    if (1 if i32_load16_u(var0 + 108) == 0 else 0):
        break
    # br_table ['$label1', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label0', '$label1', '$label2']
    _br_idx = (var3 + -64)
    break  # br_table
    if (1 if var3 == 10 else 0):
        break
    break
    var1 = ((1 if i32_load8_u(9142916) == 0 else 0) | var1)
    var4 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        break
    if (1 if i32_load(var4 + 8) < 3 else 0):
        break
    if i32_load(i32_load(var4)):
        break
    var4 = ((var3 * 72) + 9263856)
    if (1 if i32_load(((var3 * 72) + 9263856) + 68) == 0 else 0):
        break
    break
    var4 = i32_load(var0 + 88)
    # br_table ['$label6', '$label7', '$label8', '$label9']
    _br_idx = (i32_load(var0 + 88) & 65535)
    break  # br_table
    break
    var4 = ((var4 & 0xFFFFFFFF) >> 16)
    if (1 if ((var4 & 0xFFFFFFFF) >> 16) == i32_load(38984) else 0):
        break
    if (1 if i32_load(38528) == var4 else 0):
        break
    break
    break
    var3 = i32_load(((var3 * 72) + 9263908))
    var1 = ((1 if i32_load(((var3 * 72) + 9263908)) != i32_load(var0 + 48) else 0) | var1)
    if (1 if ((1 if i32_load(((var3 * 72) + 9263908)) != i32_load(var0 + 48) else 0) | var1) == 1 else 0):
    return var1


# ==========================================================
# $Aa
# Export: Aa
# ==========================================================
def Aa(var0, var1):
    """Export: Aa"""
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
    var33 = 0
    var34 = 0
    var35 = 0
    var3 = (var0 + var1)
    if (1 if (var0 + var1) == 0 else 0):
        break
    var4 = i32_load8_u(9147212)
    if (1 if var3 >= i32_load((9142892 if i32_load8_u(9147212) else 41092)) else 0):
        break
    var2 = i32_load(9561692)
    var1 = (i32_load(9561692) + (var0 * 286704))
    var5 = i32_load((i32_load(9561692) + (var0 * 286704)) + 284616)
    var6 = i32_load16_u(var1 + 38)
    var7 = i32_load16_u(var1 + 36)
    var8 = i32_load16_u(var1 + 34)
    var9 = i32_load16_u(var1 + 32)
    var10 = i32_load16_u(var1 + 30)
    var11 = i32_load16_u(var1 + 28)
    var12 = i32_load16_u(var1 + 26)
    var13 = i32_load16_u(var1 + 24)
    var14 = i32_load16_u(var1 + 22)
    var15 = i32_load16_u(var1 + 20)
    var16 = i32_load16_u(var1 + 18)
    var17 = i32_load16_u(var1 + 16)
    var18 = i32_load16_u(var1 + 14)
    var19 = i32_load16_u(var1 + 12)
    var20 = i32_load16_u(var1 + 10)
    var21 = i32_load16_u(var1 + 8)
    var22 = i32_load16_u(var1 + 6)
    var23 = i32_load16_u(var1 + 4)
    var24 = i32_load16_u(var1 + 2)
    var25 = i32_load16_u(var1)
    if (1 if var4 == 0 else 0):
        var4 = i32_load(var1 + 286684)
        var26 = i32_load(var1 + 284608)
        var27 = i32_load(var1 + 283960)
        var28 = i32_load16_u(var1 + 283972)
        var29 = i32_load8_u((var1 + 283974))
        var31 = i64_load(var1 + 40)
        var32 = i64_load(var1 + 48)
        var33 = i64_load(var1 + 56)
        var34 = i64_load((var1 - -64))
        var35 = i64_load(var1 + 72)
        var30 = (var3 * 286704)
        var2 = (var2 + (var3 * 286704))
        # Unknown: memory.copy []
        i32_store(var1 + 283908, var0)
        i32_store(var2 + 284616, var5)
        i64_store(var2 + 72, var35)
        i64_store((var2 - -64), var34)
        i64_store(var2 + 56, var33)
        i64_store(var2 + 48, var32)
        i64_store(var2 + 40, var31)
        i32_store16(var2 + 38, var6)
        i32_store16(var2 + 36, var7)
        i32_store16(var2 + 34, var8)
        i32_store16(var2 + 32, var9)
        i32_store16(var2 + 30, var10)
        i32_store16(var2 + 28, var11)
        i32_store16(var2 + 26, var12)
        i32_store16(var2 + 24, var13)
        i32_store16(var2 + 22, var14)
        i32_store16(var2 + 20, var15)
        i32_store16(var2 + 18, var16)
        i32_store16(var2 + 16, var17)
        i32_store16(var2 + 14, var18)
        i32_store16(var2 + 12, var19)
        i32_store16(var2 + 10, var20)
        i32_store16(var2 + 8, var21)
        i32_store16(var2 + 6, var22)
        i32_store16(var2 + 4, var23)
        i32_store16(var2 + 2, var24)
        i32_store16(var2, var25)
        i32_store8((var2 + 283974), var29)
        i32_store16(var2 + 283972, var28)
        i32_store(var2 + 283960, var27)
        i32_store(var2 + 284608, var26)
        i32_store(var2 + 286684, var4)
        i32_store((i32_load(9561692) + var30) + 283908, var3)
        break
    var4 = (var1 + 284616)
    var0 = (var2 + (var3 * 286704))
    var2 = ((var2 + (var3 * 286704)) + 284616)
    var3 = i32_load(var0 + 284616)
    if i32_load(var0 + 284616):
        i32_store16(var1, i32_load16_u(var0))
        i32_store16(var1 + 2, i32_load16_u(var0 + 2))
        i32_store16(var1 + 4, i32_load16_u(var0 + 4))
        i32_store16(var1 + 6, i32_load16_u(var0 + 6))
        i32_store16(var1 + 8, i32_load16_u(var0 + 8))
        i32_store16(var1 + 10, i32_load16_u(var0 + 10))
        i32_store16(var1 + 12, i32_load16_u(var0 + 12))
        i32_store16(var1 + 14, i32_load16_u(var0 + 14))
        i32_store16(var1 + 16, i32_load16_u(var0 + 16))
        i32_store16(var1 + 18, i32_load16_u(var0 + 18))
        i32_store16(var1 + 20, i32_load16_u(var0 + 20))
        i32_store16(var1 + 22, i32_load16_u(var0 + 22))
        i32_store16(var1 + 24, i32_load16_u(var0 + 24))
        i32_store16(var1 + 26, i32_load16_u(var0 + 26))
        i32_store16(var1 + 28, i32_load16_u(var0 + 28))
        i32_store16(var1 + 30, i32_load16_u(var0 + 30))
        i32_store16(var1 + 32, i32_load16_u(var0 + 32))
        i32_store16(var1 + 34, i32_load16_u(var0 + 34))
        i32_store16(var1 + 36, i32_load16_u(var0 + 36))
        i32_store16(var1 + 38, i32_load16_u(var0 + 38))
        break
    i64_store(var1 + 32, i64_load(var1 + 72))
    i64_store(var1 + 24, i64_load((var1 - -64)))
    i64_store(var1 + 16, i64_load(var1 + 56))
    i64_store(var1 + 8, i64_load(var1 + 48))
    i64_store(var1, i64_load(var1 + 40))
    i32_store(var4, var3)
    i32_store(var2, var5)
    i32_store16(var0 + 38, var6)
    i32_store16(var0 + 36, var7)
    i32_store16(var0 + 34, var8)
    i32_store16(var0 + 32, var9)
    i32_store16(var0 + 30, var10)
    i32_store16(var0 + 28, var11)
    i32_store16(var0 + 26, var12)
    i32_store16(var0 + 24, var13)
    i32_store16(var0 + 22, var14)
    i32_store16(var0 + 20, var15)
    i32_store16(var0 + 18, var16)
    i32_store16(var0 + 16, var17)
    i32_store16(var0 + 14, var18)
    i32_store16(var0 + 12, var19)
    i32_store16(var0 + 10, var20)
    i32_store16(var0 + 8, var21)
    i32_store16(var0 + 6, var22)
    i32_store16(var0 + 4, var23)
    i32_store16(var0 + 2, var24)
    i32_store16(var0, var25)
    xa()


# ==========================================================
# $func623
# ==========================================================
def func623(var0, var1):
    var0 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 127) == 2 else 0):
        i32_store8(var0 + 127, var1)


# ==========================================================
# $Qd
# Export: Qd
# ==========================================================
def Qd(var0):
    """Export: Qd"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var0 = ((i32_load(9143000) * i32_load(9147120)) + var0)
    if i32_load8_u(9147141):
        var1 = i32_load((i32_load(9671128) + (i32_load(9173808) * 132)) + 16)
        if (1 if i32_load((i32_load(9671128) + (i32_load(9173808) * 132)) + 16) == 0 else 0):
            break
        if (1 if var0 >= i32_load(var1 + 8) else 0):
            break
        return
    if (1 if var0 >= i32_load(9671120) else 0):
        break
    if i32_load(9681836):
        return
    var1 = (i32_load(9671128) + (i32_load(9173808) * 132))
    var3 = i32_load16_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 110)
    var4 = i32_load(i32_load(((var0 << 2) + 9263072)) + 12)
    var1 = i32_load8_u(var1 + 122)
    var5 = i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 196)
    var2 = 1
    if (1 if i32_load(38540) == var1 else 0):
        break
    if (1 if i32_load(38812) == var1 else 0):
        break
    var2 = (1 if i32_load(38888) == var1 else 0)


# ==========================================================
# $Ab
# Export: Ab
# ==========================================================
def Ab(var0, var1):
    """Export: Ab"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var0 = (i32_load(9561692) + (var0 * 286704))
    i32_store8((i32_load(9561692) + (var0 * 286704)) + 283972, ((var1 & 0xFFFFFFFF) >> 16))
    i32_store8((var0 + 283974), var1)
    i32_store8((var0 + 283973), ((var1 & 0xFFFFFFFF) >> 8))
    while True:  # loop $label2
        var4 = i32_load(((var0 + (var3 << 2)) + 284636))
        if (1 if i32_load(((var0 + (var3 << 2)) + 284636)) == 0 else 0):
            break
        var1 = 0
        var2 = i32_load(var4 + 8)
        if (1 if i32_load(var4 + 8) == 0 else 0):
            break
        while True:  # loop $label1
            var5 = i32_load((i32_load(var4) + (var1 << 2)))
            if i32_load((i32_load(var4) + (var1 << 2))):
                var2 = (i32_load(9671128) + (var5 * 132))
                var2 = i32_load(var4 + 8)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < var2 else 0):
                continue
            break  # end loop
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != 255 else 0):
            continue
        break  # end loop


# ==========================================================
# $func308
# ==========================================================
def func308(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var4 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var7 = (var4 + 32)
    var3 = (var4 + 32)
    var2 = (var4 + 21)
    var5 = ((var4 + 32) - (var4 + 21))
    if (1 if ((var4 + 32) - (var4 + 21)) <= 9 else 0):
        var6 = (((32 - clz32((var1 | 1))) * 1233) >> 12)
        if (1 if var5 < ((((32 - clz32((var1 | 1))) * 1233) >> 12) + (1 if i32_load(((var6 << 2) + 32256)) <= var1 else 0)) else 0):
            break
    if (1 if var1 <= 999999 else 0):
        if (1 if var1 <= 9999 else 0):
            if (1 if var1 <= 99 else 0):
                if (1 if var1 <= 9 else 0):
                    i32_store8(var2, (var1 + 48))
                    break
                break
            if (1 if var1 <= 999 else 0):
                var3 = ((var1 & 0xFFFFFFFF) // 100)
                i32_store8(var2, (((var1 & 0xFFFFFFFF) // 100) + 48))
                break
            break
        if (1 if var1 <= 99999 else 0):
            var3 = ((var1 & 0xFFFFFFFF) // 10000)
            i32_store8(var2, (((var1 & 0xFFFFFFFF) // 10000) + 48))
            break
        break
    if (1 if var1 <= 99999999 else 0):
        if (1 if var1 <= 9999999 else 0):
            var3 = ((var1 & 0xFFFFFFFF) // 1000000)
            i32_store8(var2, (((var1 & 0xFFFFFFFF) // 1000000) + 48))
            break
        break
    if (1 if var1 <= 999999999 else 0):
        var3 = ((var1 & 0xFFFFFFFF) // 100000000)
        i32_store8(var2, (((var1 & 0xFFFFFFFF) // 100000000) + 48))
        break
    var3 = ((var1 & 0xFFFFFFFF) // 100000000)
    var3 = func213(func104(var2, ((var1 & 0xFFFFFFFF) // 100000000)), (var1 - (var3 * 100000000)))
    i32_store(func213((var2 + 1), (var1 - (var3 * 100000000))) + 16, 0)
    i32_store(var4 + 12, var3)
    var5 = i32_load(var4 + 12)
    var6 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var4 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = (var5 - var2)
    if (1 if (var5 - var2) <= 2147483631 else 0):
        if (1 if var3 < 11 else 0):
            i32_store8(var0 + 11, ((i32_load8_u(var0 + 11) & 128) | var3))
            i32_store8(var0 + 11, (i32_load8_u(var0 + 11) & 127))
            var1 = var0
            break
        if (1 if var3 >= 11 else 0):
            var1 = ((var3 + 16) & -16)
            var1 = (var1 - 1)
        else:
        func314(var0, (((var3 + 16) & -16) if (1 if var1 == 11 else 0) else (var1 - 1)), (10 + 1))
        var1 = i32_load(var4 + 8)
        i32_store(var0, i32_load(var4 + 8))
        i32_store(var0 + 8, ((i32_load(var0 + 8) & -2147483648) | (i32_load(var4 + 12) & 2147483647)))
        i32_store(var0 + 8, (i32_load(var0 + 8) | -2147483648))
        i32_store(var0 + 4, var3)
        while True:  # loop $label3
            if (1 if var2 != var5 else 0):
                i32_store8(var1, i32_load8_u(var2))
                var1 = (var1 + 1)
                var2 = (var2 + 1)
                continue
            break  # end loop
        i32_store8(var4 + 7, 0)
        i32_store8(var1, i32_load8_u(var4 + 7))
        global global0
        global0 = (var4 + 16)
        break
    func212()
    raise RuntimeError('unreachable')
    global global0
    global0 = (var6 + 16)
    global global0
    global0 = var7
    return (var4 + 8)

