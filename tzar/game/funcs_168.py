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
# $ud
# Export: ud
# ==========================================================
def ud(var0):
    """Export: ud"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var2 = i32_load(9143000)
    var3 = ((1 if i32_load(9143000) == 0 else 0) & (1 if var0 < 0 else 0))
    if (1 if ((1 if i32_load(9143000) == 0 else 0) & (1 if var0 < 0 else 0)) == 0 else 0):
        break
    if (1 if i32_load(9671124) != 1 else 0):
        break
    var0 = 0
    # br_table ['$label1', '$label2', '$label3']
    _br_idx = i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) * 404) + 9568096) + 196)
    break  # br_table
    i32_store(9671124, 1)
    while True:  # loop $label4
        var2 = (var0 << 2)
        var1 = ((i32_load(((var0 << 2) + 1072)) * 132) + 9216080)
        i32_store(((i32_load(((var0 << 2) + 1072)) * 132) + 9216080) + 116, 0)
        i32_store(var1 + 16, 0)
        i32_store16(var1 + 21, 0)
        i64_store(var1 + 124, 0)
        i32_store((var2 + 9263072), var1)
        i32_store8(var1 + 24, (1 if var0 > 7 else 0))
        var1 = 28
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != 28 else 0):
            continue
        break  # end loop
    break
    i32_store(9671124, 1)
    while True:  # loop $label6
        var2 = (var0 << 2)
        var1 = ((i32_load(((var0 << 2) + 1312)) * 132) + 9216080)
        i32_store(((i32_load(((var0 << 2) + 1312)) * 132) + 9216080) + 116, 0)
        i32_store(var1 + 16, 0)
        i32_store16(var1 + 21, 0)
        i64_store(var1 + 124, 0)
        i32_store((var2 + 9263072), var1)
        i32_store8(var1 + 24, (1 if var0 > 7 else 0))
        var1 = 28
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != 28 else 0):
            continue
        break  # end loop
    break
    i32_store(9671124, 1)
    while True:  # loop $label7
        var2 = (var0 << 2)
        var1 = ((i32_load(((var0 << 2) + 1184)) * 132) + 9216080)
        i32_store(((i32_load(((var0 << 2) + 1184)) * 132) + 9216080) + 116, 0)
        i32_store(var1 + 16, 0)
        i32_store16(var1 + 21, 0)
        i64_store(var1 + 124, 0)
        i32_store((var2 + 9263072), var1)
        i32_store8(var1 + 24, (1 if var0 > 7 else 0))
        var1 = 30
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != 30 else 0):
            continue
        break  # end loop
    i32_store(9671120, var1)
    return func46(8, 1)
    var1 = i32_load(9681836)
    var4 = i32_load8_u(9147141)
    if (1 if i32_load8_u(9147141) == 0 else 0):
        break
    var5 = i32_load(i32_load((i32_load(9671128) + (i32_load(9173808) * 132)) + 16) + 8)
    if var3:
        break
    var0 = (var0 + var2)
    if (1 if ((var0 + var2) * i32_load(9147120)) >= var5 else 0):
        break
    i32_store(9143000, var0)
    if var1:
        func172(0)
        return (var1 if var1 else i32_load(9671120))
    if var4:
        Ya(1)
        return
    if i32_load8_u(9684768):
        a_b()
        return func57(i32_load(9143000))
    return func46(0, 1)


# ==========================================================
# $func102
# ==========================================================
def func102(var0, var1, var2):
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
    var17 = 0.0
    var3 = (global0 - 192)
    global global0
    global0 = (global0 - 192)
    if i32_load8_u(9142917):
        break
    var7 = i32_load8_u(var0 + 122)
    var5 = i32_load8_u(var0 + 122)
    var6 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        var4 = i32_load(9299880)
        if i32_load(9299880):
            var4 = (var4 - 1)
            i32_store(9299880, (var4 - 1))
            var6 = i32_load((i32_load(9299872) + (var4 << 2)))
            break
        var6 = i32_load(9163776)
        var4 = (i32_load(9163776) + 1)
        i32_store(9163776, (i32_load(9163776) + 1))
        var5 = i32_load(9163784)
        if (1 if var4 < i32_load(9163784) else 0):
            break
        i32_store(var3 + 176, var5)
        a_b()
        i32_store(9163784, (i32_load(9163784) + 40000))
        var5 = i32_load8_u(var0 + 122)
        i32_store(var0 + 40, var6)
    if (1 if (var1 | i32_load(((var5 * 72) + 9263856))) == 0 else 0):
        var0 = ((var5 << 2) + 9560016)
        if i32_load(((var5 << 2) + 9560016)):
            break
        i32_store(var0, i32_load(9671136))
        break
    if i32_load8_u(9142916):
        i32_store(var0 + 48, var1)
        var4 = i32_load8_u(var0 + 127)
        if (1 if ((i32_load8_u(var0 + 127) - 1) & 255) <= 13 else 0):
            var4 = (var4 << 4)
            var8 = ((((i32_load(((var4 << 4) + 1748)) << 8) + i32_load((var4 + 1744))) + (i32_load((var4 + 1752)) << 16)) + (i32_load((var4 + 1756)) << 24))
        var4 = i32_load16_u(var0 + 114)
        var10 = (i32_load16_u(var0 + 114) << 5)
        var11 = (i32_load16_u(var0 + 112) << 5)
        var14 = i32_load(9142440)
        var17 = float(((((i32_load(9142440) * i32_load(((var5 * 404) + 9568096) + 208)) + var4) << 5) | 1))
        if (1 if var1 == 0 else 0):
            break
        if (1 if i32_load(var1 + 20) == 0 else 0):
            break
        var12 = i32_load8_u(var0 + 124)
        var4 = i32_load(var1 + 28)
        if (1 if i32_load(var1 + 28) == 2147483647 else 0):
            var4 = i32_load(59152)
            i32_store(59152, (i32_load(59152) + 1))
            var13 = i32_load(9568052)
            i32_store(var1 + 28, var4)
            var15 = i32_load(var1)
            var9 = i32_load(var1 + 4)
            var16 = i32_load(9568048)
            i32_store(9568048, (i32_load(9568048) + 1))
            i32_store(((var16 << 2) + 9563952), var1)
            i32_store(9568052, (var13 + ((var15 * (var9 + 2)) << 2)))
            var13 = i32_load(9568056)
            i32_store(var1 + 56, i32_load(9568056))
            i32_store(9568056, (var13 + ((var9 * i32_load(var1)) << 2)))
        var4 = (var4 + (var12 << 16))
        var9 = i32_load16_u(var0 + 110)
        var12 = i32_load8_u(var0 + 125)
        i32_store(var3 + 172, var6)
        i32_store(var3 + 160, var8)
        i64_store(var3 + 152, 0)
        i32_store(var3 + 148, 0)
        i32_store(var3 + 144, var4)
        i64_store(var3 + 136, 0)
        i64_store(var3 + 128, 0)
        i64_store(var3 + 120, 0)
        i32_store(var3 + 168, (var12 << 8))
        i32_store(var3 + 164, ((var9 << 16) | var5))
        f64_store(var3 + 112, float((((var17 * 0.5) / float((var14 * 96))) + 0.25)))
        f64_store(var3 + 104, float(var10))
        f64_store(var3 + 96, float(var11))
        a_b()
        break
    if var1:
    func92(var0, 0.0, 0.0)
    if var2:
        break
    if (1 if i32_load(((var7 * 404) + 9568096) + 20) == 0 else 0):
        break
    if (1 if var1 == i32_load(9142592) else 0):
        var4 = 4
        break
    if (1 if var1 == i32_load(9142596) else 0):
        var4 = 14
        break
    if (1 if var1 == i32_load(9142600) else 0):
        var4 = 16
        break
    if (1 if var1 == i32_load(9142604) else 0):
        var4 = 9
        break
    if (1 if var1 == i32_load(9142636) else 0):
        var4 = 35
        break
    if (1 if i32_load(9142500) != var1 else 0):
        break
    var4 = 15
    var2 = 37
    var1 = 0
    if i32_load8_u(9142917):
        break
    var1 = i32_load(9299880)
    if i32_load(9299880):
        var1 = (var1 - 1)
        i32_store(9299880, (var1 - 1))
        var1 = i32_load((i32_load(9299872) + (var1 << 2)))
        break
    var1 = i32_load(9163776)
    var6 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var5 = i32_load(9163784)
    if (1 if var6 < i32_load(9163784) else 0):
        break
    i32_store(var3 + 80, var5)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    func120(var0, var1, 0)
    var9 = i32_load(9142440)
    var6 = (i32_load16_u(var0 + 114) << 5)
    var17 = (((float(i32_load(9142440)) * 32.0) * float(i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 208))) + float((i32_load16_u(var0 + 114) << 5)))
    var4 = (var4 + var6)
    var5 = ((i32_load16_u(var0 + 112) << 5) + var2)
    if i32_load8_u(9142916):
        var17 = (var17 + 30.0)
        var6 = 0
        var2 = i32_load(9142740)
        if (1 if i32_load(9142740) == 0 else 0):
            break
        if (1 if i32_load(var2 + 20) == 0 else 0):
            break
        var6 = i32_load(var2 + 28)
        if (1 if i32_load(var2 + 28) != 2147483647 else 0):
            break
        var6 = i32_load(59152)
        i32_store(59152, (i32_load(59152) + 1))
        var8 = i32_load(9568052)
        i32_store(var2 + 28, var6)
        var10 = i32_load(var2)
        var7 = i32_load(var2 + 4)
        var11 = i32_load(9568048)
        i32_store(9568048, (i32_load(9568048) + 1))
        i32_store(((var11 << 2) + 9563952), var2)
        i32_store(9568052, (var8 + ((var10 * (var7 + 2)) << 2)))
        var8 = i32_load(9568056)
        i32_store(var2 + 56, i32_load(9568056))
        i32_store(9568056, (var8 + ((var7 * i32_load(var2)) << 2)))
        var0 = i32_load16_u(var0 + 110)
        i32_store(var3 + 76, var1)
        i32_store(var3 + 72, 0)
        i32_store((var3 - -64), 0)
        i64_store(var3 + 56, 0)
        i32_store(var3 + 52, 0)
        i32_store(var3 + 48, var6)
        i64_store(var3 + 40, 0)
        i64_store(var3 + 32, 0)
        i64_store(var3 + 24, 0)
        if (1 if var17 > 0.0 else 0):
        else:
        f64_store((((var17 * 0.5) / float((var9 * 96))) + 0.25) + 16, float(var17))
        i32_store(var3 + 68, ((var0 << 16) | 65535))
        f64_store(var3 + 8, float(var4))
        f64_store(var3, float(var5))
        a_b()
        break
    global global0
    global0 = (var3 + 192)
    return func40(float(var5), float(var4), var17, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, i32_load(9142740), (i32_load16_u(var0 + 110) + 16), var1, 1, 0, 0, 0.0)

