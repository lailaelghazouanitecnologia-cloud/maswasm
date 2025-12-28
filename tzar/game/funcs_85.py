"""
Auto-generated from WAT. Contains 4 functions.
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
# $func313
# ==========================================================
def func313(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var2 = func443(8)
    i32_store(func443(8), 32876)
    i32_store(var2, 32988)
    var3 = func209(var0)
    var1 = func26((func209(var0) + 13))
    i32_store(func26((func209(var0) + 13)) + 8, 0)
    i32_store(var1 + 4, var3)
    i32_store(var1, var3)
    var1 = (var1 + 12)
    # Unknown: memory.copy []
    i32_store(var2 + 4, var1)
    i32_store(var2, 33036)
    a_i()
    raise RuntimeError('unreachable')


# ==========================================================
# $func320
# ==========================================================
def func320(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var3 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    if (1 if i32_load8_u(9142917) == 0 else 0):
        if (1 if var0 == 0 else 0):
            if (1 if i32_load8_u(9142916) == 0 else 0):
                var0 = i32_load(9299880)
                if i32_load(9299880):
                    var0 = (var0 - 1)
                    i32_store(9299880, (var0 - 1))
                    var0 = i32_load((i32_load(9299872) + (var0 << 2)))
                    break
                var0 = i32_load(9163776)
                var1 = (i32_load(9163776) + 1)
                i32_store(9163776, (i32_load(9163776) + 1))
                var2 = i32_load(9163784)
                if (1 if var1 >= i32_load(9163784) else 0):
                    break
                i32_store(9142888, var0)
                break
                i32_store(var3 + 64, var2)
                a_b()
                i32_store(9142888, var0)
                i32_store(9163784, (i32_load(9163784) + 40000))
                if (1 if i32_load8_u(9142916) == 0 else 0):
                    break
            var0 = i32_load(9299896)
            if i32_load(9299896):
                var0 = (var0 - 1)
                i32_store(9299896, (var0 - 1))
                var0 = i32_load((i32_load(9299888) + (var0 << 2)))
                break
            var0 = i32_load(9163780)
            var1 = (i32_load(9163780) + 1)
            i32_store(9163780, (i32_load(9163780) + 1))
            var2 = i32_load(9163788)
            if (1 if var1 < i32_load(9163788) else 0):
                break
            i32_store(var3 + 48, var2)
            a_b()
            i32_store(9163788, (i32_load(9163788) + 40000))
            var0 = (var0 + 1073741823)
            break
            if i32_load8_u(9142917):
                i32_store(9142884, 0)
                break
            var0 = i32_load(9299880)
            if i32_load(9299880):
                var0 = (var0 - 1)
                i32_store(9299880, (var0 - 1))
                var0 = i32_load((i32_load(9299872) + (var0 << 2)))
                break
            var0 = i32_load(9163776)
            var1 = (i32_load(9163776) + 1)
            i32_store(9163776, (i32_load(9163776) + 1))
            var2 = i32_load(9163784)
            if (1 if var1 < i32_load(9163784) else 0):
                break
            i32_store(var3 + 32, var2)
            a_b()
            i32_store(9163784, (i32_load(9163784) + 40000))
            i32_store(9142884, var0)
            if i32_load8_u(9142917):
                break
            var0 = i32_load(9299880)
            if i32_load(9299880):
                var0 = (var0 - 1)
                i32_store(9299880, (var0 - 1))
                var1 = i32_load((i32_load(9299872) + (var0 << 2)))
                break
            var0 = 0
            var1 = i32_load(9163776)
            var2 = (i32_load(9163776) + 1)
            i32_store(9163776, (i32_load(9163776) + 1))
            var4 = i32_load(9163784)
            if (1 if var2 >= i32_load(9163784) else 0):
                break
            i32_store(9142876, var1)
            break
            i32_store(var3 + 16, var4)
            a_b()
            i32_store(9142876, var1)
            i32_store(9163784, (i32_load(9163784) + 40000))
            if i32_load8_u(9142917):
                break
            var0 = i32_load(9299880)
            if i32_load(9299880):
                var0 = (var0 - 1)
                i32_store(9299880, (var0 - 1))
                var0 = i32_load((i32_load(9299872) + (var0 << 2)))
                break
            var0 = i32_load(9163776)
            var1 = (i32_load(9163776) + 1)
            i32_store(9163776, (i32_load(9163776) + 1))
            var2 = i32_load(9163784)
            if (1 if var1 < i32_load(9163784) else 0):
                break
            i32_store(var3, var2)
            a_b()
            i32_store(9163784, (i32_load(9163784) + 40000))
            break
            var0 = 0
            i32_store(9142876, 0)
            i32_store(9142880, var0)
        var0 = i32_load(9142640)
        if (1 if i32_load(9142640) == 0 else 0):
            break
        if (1 if i32_load(var0 + 20) == 0 else 0):
            break
        var1 = i32_load8_u(9142916)
        if (1 if i32_load(var0 + 28) != 2147483647 else 0):
            break
        if var1:
            var2 = i32_load(59152)
            i32_store(59152, (i32_load(59152) + 1))
            var4 = i32_load(9568052)
            var5 = i32_load(var0)
            break
        var5 = i32_load(var0)
        var4 = i32_load(9568052)
        var2 = ((i32_load(var0) + i32_load(9140308)) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2))
        i32_store(var0 + 28, var2)
        var2 = i32_load(var0 + 4)
        var6 = i32_load(9568048)
        i32_store(9568048, (i32_load(9568048) + 1))
        i32_store(((var6 << 2) + 9563952), var0)
        i32_store(9568052, (((var5 * (var2 + 2)) << 2) + var4))
        if (1 if var1 == 0 else 0):
            break
        var1 = i32_load(9568056)
        i32_store(var0 + 56, i32_load(9568056))
        i32_store(9568056, (var1 + ((var2 * i32_load(var0)) << 2)))
        if i32_load8_u(9142916):
            break
        break
        if var1:
            break
    global global0
    global0 = (var3 + 80)


# ==========================================================
# $func322
# ==========================================================
def func322(var0, var1, var2):
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
    var6 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var7 = i32_load(9561692)
    if i32_load(9147132):
        if (1 if i32_load(9142440) == 4096 else 0):
            break
    var3 = i32_load(var2)
    break
    var3 = i32_load(var2)
    if (1 if (i32_load(var2) + i32_load(((var7 + (var1 * 286704)) + 281724))) < 1000001 else 0):
        break
    if (1 if i32_load(9142872) != var1 else 0):
        break
    i64_store(var6, 4294967296000930)
    a_b()
    break
    if (1 if var3 < 0 else 0):
        break
    var4 = i32_load(var2 + 4)
    if (1 if i32_load(var2 + 4) < 0 else 0):
        break
    var5 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) < 0 else 0):
        break
    var8 = i32_load(var2 + 12)
    if (1 if i32_load(var2 + 12) < 0 else 0):
        break
    if var3:
        break
    if var4:
        break
    if var5:
        break
    if (1 if var8 == 0 else 0):
        break
    if i32_load8_u((i32_load(9143004) + ((i32_load(9142892) * var1) + var0))):
        break
    var11 = (var7 + (var1 * 286704))
    if func66((var7 + (var1 * 286704)), var2, 1, 0):
        break
    var4 = (var7 + (var1 * 286704))
    var3 = ((var7 + (var1 * 286704)) + 281724)
    i32_store(((var7 + (var1 * 286704)) + 281724), (i32_load(var3) + i32_load(var2)))
    var3 = (var7 + (var0 * 286704))
    var5 = ((var7 + (var0 * 286704)) + 281708)
    i32_store(((var7 + (var0 * 286704)) + 281708), (i32_load(var5) + i32_load(var2)))
    var5 = (var4 + 281728)
    i32_store((var4 + 281728), (i32_load(var5) + i32_load(var2 + 4)))
    var5 = (var3 + 281712)
    i32_store((var3 + 281712), (i32_load(var5) + i32_load(var2 + 4)))
    var5 = (var4 + 281732)
    i32_store((var4 + 281732), (i32_load(var5) + i32_load(var2 + 8)))
    var5 = (var3 + 281716)
    i32_store((var3 + 281716), (i32_load(var5) + i32_load(var2 + 8)))
    var4 = (var4 + 281736)
    i32_store((var4 + 281736), (i32_load(var4) + i32_load(var2 + 12)))
    var4 = (var3 + 281720)
    i32_store((var3 + 281720), (i32_load(var4) + i32_load(var2 + 12)))
    var4 = i32_load(var3 + 283848)
    if (1 if i32_load(var3 + 283848) != 2147483647 else 0):
        i32_store((var3 + 283848), (i32_load(var2) + var4))
    var3 = (var3 + 283852)
    var4 = i32_load((var3 + 283852))
    if (1 if i32_load((var3 + 283852)) != 2147483647 else 0):
        i32_store(var3, (i32_load(var2 + 4) + var4))
    var3 = (var7 + (var0 * 286704))
    var4 = ((var7 + (var0 * 286704)) + 283856)
    var5 = i32_load(((var7 + (var0 * 286704)) + 283856))
    if (1 if i32_load(((var7 + (var0 * 286704)) + 283856)) != 2147483647 else 0):
        i32_store(var4, (i32_load(var2 + 8) + var5))
    var3 = (var3 + 283860)
    var4 = i32_load((var3 + 283860))
    if (1 if i32_load((var3 + 283860)) != 2147483647 else 0):
        i32_store(var3, (i32_load(var2 + 12) + var4))
    var3 = 1
    var5 = (var7 + (var0 * 286704))
    i32_store8((var7 + (var0 * 286704)) + 286701, 1)
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var9 = (var4 - 1)
    var12 = ((var4 - 1) & 1)
    var5 = (i32_load(var5 + 283908) * var4)
    var8 = i32_load(9561692)
    var10 = i32_load(9143016)
    if (1 if var4 != 2 else 0):
        var9 = (var9 & -2)
        var4 = 0
        while True:  # loop $label5
            if i32_load8_u((var10 + (var3 + var5))):
                i32_store8((var8 + (var3 * 286704)) + 286701, 1)
            var13 = (var3 + 1)
            if i32_load8_u((var10 + ((var3 + 1) + var5))):
                i32_store8((var8 + (var13 * 286704)) + 286701, 1)
            var3 = (var3 + 2)
            var4 = (var4 + 2)
            if (1 if (var4 + 2) != var9 else 0):
                continue
            break  # end loop
    if (1 if var12 == 0 else 0):
        break
    if (1 if i32_load8_u((var10 + (var3 + var5))) == 0 else 0):
        break
    i32_store8((var8 + (var3 * 286704)) + 286701, 1)
    if (1 if i32_load(9142872) != var0 else 0):
        break
    var14 = i64_load(var2)
    var15 = i64_load(var2 + 8)
    i32_store(var6 + 36, i32_load((var7 + (var1 * 286704)) + 284616))
    i32_store(var6 + 32, var11)
    i64_store(var6 + 24, var15)
    i64_store(var6 + 16, var14)
    a_b()
    global global0
    global0 = (var6 + 48)


# ==========================================================
# $func370
# ==========================================================
def func370(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var4 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if (i32_load8_u(9568060) | i32_load8_u(9147152)) == 0 else 0):
        break
    if i32_load8_u(9142917):
        break
    var3 = i32_load(9299880)
    if i32_load(9299880):
        var3 = (var3 - 1)
        i32_store(9299880, (var3 - 1))
        var3 = i32_load((i32_load(9299872) + (var3 << 2)))
        break
    var3 = i32_load(9163776)
    var5 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var6 = i32_load(9163784)
    if (1 if var5 < i32_load(9163784) else 0):
        break
    i32_store(var4, var6)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    global global0
    global0 = (var4 + 16)
    return var3

