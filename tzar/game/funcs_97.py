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
# $func124
# ==========================================================
def func124(var0):
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
    var1 = (global0 - 112)
    global global0
    global0 = (global0 - 112)
    i32_store(9684420, var0)
    var4 = i32_load(9671128)
    var3 = (i32_load(9671128) + (var0 * 132))
    var7 = i32_load16_u((i32_load(9671128) + (var0 * 132)) + 88)
    var6 = i32_load16_u(var3 + 108)
    var8 = i32_load8_u(var3 + 122)
    func52(i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 144), i32_load16_u(var3 + 110))
    var2 = i32_load(var3 + 24)
    if (1 if i32_load(var3 + 24) == 0 else 0):
        break
    var2 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) == 0 else 0):
        break
    var5 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) == 0 else 0):
        break
    i32_store(var1 + 100, i32_load(var2))
    i32_store(var1 + 96, var5)
    a_b()
    break
    a_b()
    var2 = i32_load((var4 + (var0 * 132)) + 16)
    if i32_load((var4 + (var0 * 132)) + 16):
        var11 = i32_load(var2 + 8)
    if i32_load8_u(9147152):
        break
    if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var3 + 110))))) == 0 else 0):
        break
    var2 = (var4 + (var0 * 132))
    if (1 if i32_load((i32_load(9215884) + (i32_load((var4 + (var0 * 132)) + 44) << 4)) + 4) == 20 else 0):
        break
    var12 = (1 if i32_load8_u(var2 + 127) != 6 else 0)
    var2 = i32_load(9215884)
    var5 = (var4 + (var0 * 132))
    var9 = i32_load((var4 + (var0 * 132)) + 44)
    var10 = i32_load((i32_load(9215884) + (i32_load((var4 + (var0 * 132)) + 44) << 4)) + 4)
    # br_table ['$label3', '$label4', '$label4', '$label3', '$label5']
    _br_idx = (i32_load((i32_load(9215884) + (i32_load((var4 + (var0 * 132)) + 44) << 4)) + 4) - 2)
    break  # br_table
    if (1 if var10 != 34 else 0):
        break
    var13 = i32_load((var2 + (var9 << 4)))
    var9 = (var7 if var6 else 0)
    var10 = i32_load(var5 + 52)
    var2 = ((var8 * 404) + 9568096)
    var8 = i32_load(((var8 * 404) + 9568096) + 264)
    var14 = i32_load(var2 + 84)
    var2 = i32_load8_u(var3 + 122)
    if (1 if i32_load8_u(var5 + 125) == 9 else 0):
        var5 = 0
        if (1 if i32_load(38452) == var2 else 0):
            break
        if (1 if i32_load(38496) == var2 else 0):
            break
        if (1 if i32_load(38756) == var2 else 0):
            break
        if (1 if i32_load(38692) == var2 else 0):
            break
        if (1 if i32_load(38696) == var2 else 0):
            break
        if (1 if i32_load(38776) == var2 else 0):
            break
        if (1 if i32_load(38752) == var2 else 0):
            break
        if (1 if i32_load(38704) == var2 else 0):
            break
    var5 = i32_load((var4 + (var0 * 132)) + 60)
    var7 = 0
    var15 = i32_load16_u(var3 + 110)
    var6 = (i32_load(9561692) + (i32_load16_u(var3 + 110) * 286704))
    var16 = i32_load((i32_load(9561692) + (i32_load16_u(var3 + 110) * 286704)) + 284628)
    var6 = i32_load(var6 + 284616)
    var0 = (var4 + (var0 * 132))
    var17 = i64_load((var4 + (var0 * 132)) + 80)
    var18 = i64_load(var0 + 72)
    var4 = i32_load16_u(var3 + 108)
    i32_store(var1 + 48, var8)
    i32_store(var1 + 52, var10)
    i32_store(var1 + 56, var5)
    i64_store(var1 + 60, var18)
    i32_store(var1 + 68, var2)
    i64_store(var1 + 72, var17)
    i32_store(var1 + 80, var15)
    i32_store(var1 + 84, var9)
    i32_store(var1 + 88, var4)
    i32_store(var1 + 92, (var6 if var6 else var16))
    i32_store(var1 + 32, var11)
    i32_store(var1 + 36, var12)
    i32_store(var1 + 40, var13)
    i32_store(var1 + 44, var14)
    a_b()
    i64_store(var1 + 16, i64_load(var0 + 64))
    a_b()
    if i32_load(9147136):
        var2 = i32_load(9561692)
        var0 = i32_load16_u(var3 + 110)
        if i32_load16_u(var3 + 110):
            var7 = i32_load8_u((i32_load(9143004) + ((i32_load(9142892) * i32_load(9142872)) + var0)))
        var0 = i32_load((var2 + (var0 * 286704)) + 281800)
        if i32_load((var2 + (var0 * 286704)) + 281800):
        else:
        i32_store((1 if i32_load((var0 + (i32_load(9142872) << 2))) != 0 else 0) + 4, 0)
        i32_store(var1, var7)
        a_b()
    global global0
    global0 = (var1 + 112)
    return var1


# ==========================================================
# $xa
# Export: xa
# ==========================================================
def xa():
    """Export: xa"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if (1 if i32_load8_u(9147126) == 0 else 0):
        var0 = i32_load(9142892)
        var1 = i32_load(41092)
        var2 = i32_load8_u(9147212)
        var5 = (i32_load(9142892) if i32_load8_u(9147212) else i32_load(41092))
        var6 = (((i32_load(9142892) if i32_load8_u(9147212) else i32_load(41092)) * 45) - 41)
        var3 = func26((-1 if (1 if var6 > 1073741823 else 0) else ((((i32_load(9142892) if i32_load8_u(9147212) else i32_load(41092)) * 45) - 41) << 2)))
        i32_store(func26((-1 if (1 if var6 > 1073741823 else 0) else ((((i32_load(9142892) if i32_load8_u(9147212) else i32_load(41092)) * 45) - 41) << 2))) + 8, var2)
        i32_store(var3 + 4, var1)
        i32_store(var3, var0)
        i32_store(var3 + 12, i32_load8_u(9561848))
        if (1 if var5 >= 2 else 0):
            var7 = i32_load(9561692)
            var2 = 4
            var4 = 1
            while True:  # loop $label0
                var1 = (var3 + (var2 << 2))
                var0 = (var7 + (var4 * 286704))
                i32_store((var3 + (var2 << 2)), i32_load16_u((var7 + (var4 * 286704))))
                i32_store(var1 + 4, i32_load16_u(var0 + 2))
                i32_store(var1 + 8, i32_load16_u(var0 + 4))
                i32_store(var1 + 12, i32_load16_u(var0 + 6))
                i32_store(var1 + 16, i32_load16_u(var0 + 8))
                i32_store(var1 + 20, i32_load16_u(var0 + 10))
                i32_store(var1 + 24, i32_load16_u(var0 + 12))
                i32_store(var1 + 28, i32_load16_u(var0 + 14))
                i32_store(var1 + 32, i32_load16_u(var0 + 16))
                i32_store(var1 + 36, i32_load16_u(var0 + 18))
                i32_store(var1 + 40, i32_load16_u(var0 + 20))
                i32_store(var1 + 44, i32_load16_u(var0 + 22))
                i32_store(var1 + 48, i32_load16_u(var0 + 24))
                i32_store(var1 + 52, i32_load16_u(var0 + 26))
                i32_store(var1 + 56, i32_load16_u(var0 + 28))
                i32_store(var1 + 60, i32_load16_u(var0 + 30))
                i32_store((var1 - -64), i32_load16_u(var0 + 32))
                i32_store(var1 + 68, i32_load16_u(var0 + 34))
                i32_store(var1 + 72, i32_load16_u(var0 + 36))
                i32_store(var1 + 76, i32_load16_u(var0 + 38))
                i32_store(var1 + 80, i32_load16_u(var0 + 40))
                i32_store(var1 + 84, i32_load16_u(var0 + 42))
                i32_store(var1 + 88, i32_load16_u(var0 + 44))
                i32_store(var1 + 92, i32_load16_u(var0 + 46))
                i32_store(var1 + 96, i32_load16_u(var0 + 48))
                i32_store(var1 + 100, i32_load16_u(var0 + 50))
                i32_store(var1 + 104, i32_load16_u(var0 + 52))
                i32_store(var1 + 108, i32_load16_u(var0 + 54))
                i32_store(var1 + 112, i32_load16_u(var0 + 56))
                i32_store(var1 + 116, i32_load16_u(var0 + 58))
                i32_store(var1 + 120, i32_load16_u(var0 + 60))
                i32_store(var1 + 124, i32_load16_u(var0 + 62))
                i32_store(var1 + 128, i32_load16_u((var0 - -64)))
                i32_store(var1 + 132, i32_load16_u(var0 + 66))
                i32_store(var1 + 136, i32_load16_u(var0 + 68))
                i32_store(var1 + 140, i32_load16_u(var0 + 70))
                i32_store(var1 + 144, i32_load16_u(var0 + 72))
                i32_store(var1 + 148, i32_load16_u(var0 + 74))
                i32_store(var1 + 152, i32_load16_u(var0 + 76))
                i32_store(var1 + 156, i32_load16_u(var0 + 78))
                i32_store(var1 + 160, i32_load(var0 + 284608))
                i32_store(var1 + 164, i32_load(var0 + 283960))
                i32_store(var1 + 168, i32_load(var0 + 284616))
                i32_store(var1 + 172, ((i32_load8_u((var0 + 283974)) | (i32_load8_u((var0 + 283973)) << 8)) | (i32_load8_u(var0 + 283972) << 16)))
                i32_store(var1 + 176, i32_load(var0 + 286684))
                var2 = (var2 + 45)
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != var5 else 0):
                    continue
                break  # end loop
        func71(14, var3, var6, 0, 0, 0)

