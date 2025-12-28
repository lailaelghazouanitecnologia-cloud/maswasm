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
# $func196
# ==========================================================
def func196(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var5 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var6 = func197(var0, var1, var2, var3)
    if (1 if (i32_load(var4 + 12) * i32_load(var4 + 8)) <= (i32_load(var3 + 12) * i32_load(var3 + 8)) else 0):
        break
    i32_store(var5 + 24, i32_load(var3 + 24))
    i64_store(var5 + 16, i64_load(var3 + 16))
    i64_store(var5 + 8, i64_load(var3 + 8))
    i64_store(var5, i64_load(var3))
    i32_store(var3 + 24, i32_load(var4 + 24))
    i64_store(var3 + 16, i64_load(var4 + 16))
    i64_store(var3 + 8, i64_load(var4 + 8))
    i64_store(var3, i64_load(var4))
    i32_store(var4 + 24, i32_load(var5 + 24))
    i64_store(var4 + 16, i64_load(var5 + 16))
    i64_store(var4 + 8, i64_load(var5 + 8))
    i64_store(var4, i64_load(var5))
    if (1 if (i32_load(var3 + 12) * i32_load(var3 + 8)) <= (i32_load(var2 + 12) * i32_load(var2 + 8)) else 0):
        var6 = (var6 + 1)
        break
    i32_store(var5 + 24, i32_load(var2 + 24))
    i64_store(var5 + 16, i64_load(var2 + 16))
    i64_store(var5 + 8, i64_load(var2 + 8))
    i64_store(var5, i64_load(var2))
    i32_store(var2 + 24, i32_load(var3 + 24))
    i64_store(var2 + 16, i64_load(var3 + 16))
    i64_store(var2 + 8, i64_load(var3 + 8))
    i64_store(var2, i64_load(var3))
    i32_store(var3 + 24, i32_load(var5 + 24))
    i64_store(var3 + 16, i64_load(var5 + 16))
    i64_store(var3 + 8, i64_load(var5 + 8))
    i64_store(var3, i64_load(var5))
    if (1 if (i32_load(var2 + 12) * i32_load(var2 + 8)) <= (i32_load(var1 + 12) * i32_load(var1 + 8)) else 0):
        var6 = (var6 + 2)
        break
    i32_store(var5 + 24, i32_load(var1 + 24))
    i64_store(var5 + 16, i64_load(var1 + 16))
    i64_store(var5 + 8, i64_load(var1 + 8))
    i64_store(var5, i64_load(var1))
    i32_store(var1 + 24, i32_load(var2 + 24))
    i64_store(var1 + 16, i64_load(var2 + 16))
    i64_store(var1 + 8, i64_load(var2 + 8))
    i64_store(var1, i64_load(var2))
    i32_store(var2 + 24, i32_load(var5 + 24))
    i64_store(var2 + 16, i64_load(var5 + 16))
    i64_store(var2 + 8, i64_load(var5 + 8))
    i64_store(var2, i64_load(var5))
    if (1 if (i32_load(var1 + 12) * i32_load(var1 + 8)) <= (i32_load(var0 + 12) * i32_load(var0 + 8)) else 0):
        var6 = (var6 + 3)
        break
    i32_store(var5 + 24, i32_load(var0 + 24))
    i64_store(var5 + 16, i64_load(var0 + 16))
    i64_store(var5 + 8, i64_load(var0 + 8))
    i64_store(var5, i64_load(var0))
    i32_store(var0 + 24, i32_load(var1 + 24))
    i64_store(var0 + 16, i64_load(var1 + 16))
    i64_store(var0 + 8, i64_load(var1 + 8))
    i64_store(var0, i64_load(var1))
    i32_store(var1 + 24, i32_load(var5 + 24))
    i64_store(var1 + 16, i64_load(var5 + 16))
    i64_store(var1 + 8, i64_load(var5 + 8))
    i64_store(var1, i64_load(var5))
    var6 = (var6 + 4)
    global global0
    global0 = (var5 + 32)
    return var6


# ==========================================================
# $func199
# ==========================================================
def func199(var0):
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
    var11 = 0.0
    var12 = 0.0
    var13 = 0.0
    var14 = 0.0
    var15 = 0.0
    var2 = (global0 - 112)
    global global0
    global0 = (global0 - 112)
    var1 = i32_load(var0 + 12)
    if (1 if i32_load(var0 + 12) == 0 else 0):
        break
    var8 = i32_load(i32_load(var1))
    if (1 if i32_load(i32_load(var1)) == 0 else 0):
        break
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    var1 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096))
    if i32_load8_u(9142916):
        if (1 if var1 == 0 else 0):
            break
        if (1 if i32_load(var1 + 20) == 0 else 0):
            break
        var4 = i32_load(var1 + 28)
        if (1 if i32_load(var1 + 28) != 2147483647 else 0):
            break
        var4 = i32_load(59152)
        i32_store(59152, (i32_load(59152) + 1))
        var3 = i32_load(9568052)
        i32_store(var1 + 28, var4)
        var6 = i32_load(var1)
        var0 = i32_load(var1 + 4)
        var5 = i32_load(9568048)
        i32_store(9568048, (i32_load(9568048) + 1))
        i32_store(((var5 << 2) + 9563952), var1)
        i32_store(9568052, (var3 + ((var6 * (var0 + 2)) << 2)))
        var3 = i32_load(9568056)
        i32_store(var1 + 56, i32_load(9568056))
        i32_store(9568056, (var3 + ((var0 * i32_load(var1)) << 2)))
        i32_store(var2 + 96, var8)
        i32_store(var2 + 80, var4)
        f64_store(var2 + 88, float(float((i32_load(9142848) * 25))))
        a_b()
        break
    var6 = i32_load(var1 + 16)
    var5 = i32_load(var1 + 20)
    if (1 if i32_load(var1 + 20) == 0 else 0):
        var7 = i32_load(var1)
        break
    var7 = i32_load8_u(var0 + 124)
    var3 = i32_load(var1 + 28)
    if (1 if i32_load(var1 + 28) != 2147483647 else 0):
        var4 = i32_load(var1 + 4)
        break
    var9 = i32_load(var1)
    var10 = i32_load(9568052)
    var3 = ((i32_load(var1) + i32_load(9140308)) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2))
    i32_store(var1 + 28, ((i32_load(var1) + i32_load(9140308)) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2)))
    var4 = i32_load(var1 + 4)
    i32_store(9568052, (var10 + ((var9 * (i32_load(var1 + 4) + 2)) << 2)))
    var9 = i32_load(9568048)
    i32_store(9568048, (i32_load(9568048) + 1))
    i32_store(((var9 << 2) + 9563952), var1)
    var7 = i32_load(var1)
    var4 = (((((var7 * i32_load(var1)) * var4) & 0xFFFFFFFF) // var5) + var3)
    var3 = 0
    var5 = (var5 * var6)
    if (var5 * var6):
        var3 = (i32_load(var1 + 4) // var5)
    var5 = i32_load16_u(var0 + 110)
    f64_store(var2 + 56, float((var6 << 16)))
    i32_store((var2 - -64), var8)
    i32_store(var2 + 48, (var5 + 16))
    f64_store(var2 + 40, float(float((i32_load(9142848) * 25))))
    f64_store(var2 + 32, float((float((((var3 * var7) * 6) + var4)) / float(i32_load(59156)))))
    a_b()
    var12 = (float(i32_load16_u(var0 + 114)) * 32.0)
    var13 = (float(i32_load16_u(var0 + 112)) * 32.0)
    if (1 if i32_load8_u(9142916) == 0 else 0):
        var11 = float(i32_load(var1 + 8))
        var15 = 32.0
        break
    var15 = float(((16.0 / float((i32_load(9142440) * 96))) + 0.25))
    var14 = 0.0
    i32_store(var2 + 24, var8)
    f64_store(var2 + 16, var15)
    f64_store(var2 + 8, float((var12 - var14)))
    f64_store(var2, float((var13 - var11)))
    a_b()
    global global0
    global0 = (var2 + 112)
    return var2


# ==========================================================
# $func221
# ==========================================================
def func221(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var0 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var1 = i32_load16_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 110)
    i32_store(9671124, 240)
    i32_store(9671120, 0)
    var2 = i32_load(9561692)
    a_b()
    var2 = (var2 + (var1 * 286704))
    var1 = i32_load((var2 + (var1 * 286704)) + 281792)
    if (1 if i32_load((var2 + (var1 * 286704)) + 281792) == 0 else 0):
        break
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    var2 = (var2 + 281792)
    while True:  # loop $label1
        var4 = (var3 << 2)
        if i32_load(((var3 << 2) + i32_load(var1))):
            var1 = i32_load(9671120)
            i32_store(9671120, (i32_load(9671120) + 1))
            i32_store(((var1 << 2) + 9263072), 9256340)
            var1 = i32_load(((i32_load16_u((i32_load(i32_load(var2)) + var4)) * 404) + 9568096) + 144)
            i64_store(var0 + 40, 4294967295)
            i64_store(var0 + 32, 0)
            i64_store(var0 + 24, 0)
            i64_store(var0 + 16, 1)
            i64_store(var0 + 8, 1)
            i32_store(var0, var3)
            i32_store(var0 + 4, (0 - var1))
            a_b()
            var1 = i32_load(var2)
        var3 = (var3 + 1)
        if (1 if (var3 + 1) < i32_load(var1 + 8) else 0):
            continue
        break  # end loop
    global global0
    global0 = (var0 + 48)


# ==========================================================
# $func244
# ==========================================================
def func244(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var2 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    if (1 if i32_load8_u(9142916) == 0 else 0):
        break
    var0 = i32_load(var0 + 32)
    if ((1 if i32_load(var0 + 32) != 27 else 0) & (1 if var0 != 6 else 0)):
        break
    var0 = i32_load(9299896)
    if i32_load(9299896):
        var0 = (var0 - 1)
        i32_store(9299896, (var0 - 1))
        var1 = i32_load((i32_load(9299888) + (var0 << 2)))
        break
    var1 = i32_load(9163780)
    var0 = (i32_load(9163780) + 1)
    i32_store(9163780, (i32_load(9163780) + 1))
    var3 = i32_load(9163788)
    if (1 if var0 < i32_load(9163788) else 0):
        break
    i32_store(var2 + 16, var3)
    a_b()
    i32_store(9163788, (i32_load(9163788) + 40000))
    var1 = (var1 + 1073741823)
    break
    if i32_load8_u(9142917):
        break
    var0 = i32_load(9299880)
    if i32_load(9299880):
        var0 = (var0 - 1)
        i32_store(9299880, (var0 - 1))
        var1 = i32_load((i32_load(9299872) + (var0 << 2)))
        break
    var1 = i32_load(9163776)
    var0 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var3 = i32_load(9163784)
    if (1 if var0 < i32_load(9163784) else 0):
        break
    i32_store(var2, var3)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    global global0
    global0 = (var2 + 32)
    return var1


# ==========================================================
# $func245
# ==========================================================
def func245():
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if i32_load8_u(9142917):
        break
    var0 = i32_load(9299880)
    if i32_load(9299880):
        var0 = (var0 - 1)
        i32_store(9299880, (var0 - 1))
        var0 = i32_load((i32_load(9299872) + (var0 << 2)))
        break
    var0 = i32_load(9163776)
    var2 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var3 = i32_load(9163784)
    if (1 if var2 < i32_load(9163784) else 0):
        break
    i32_store(var1, var3)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    global global0
    global0 = (var1 + 16)
    return var0


# ==========================================================
# $func252
# ==========================================================
def func252(var0, var1):
    var2 = 0
    var3 = 0
    if (1 if var0 == 0 else 0):
        break
    var3 = (i64_extend_u(var0) * i64_extend_u(var1))
    var2 = i32((i64_extend_u(var0) * i64_extend_u(var1)))
    if (1 if (var0 | var1) < 65536 else 0):
        break
    var2 = (-1 if i32(((var3 & 0xFFFFFFFFFFFFFFFF) >> 32)) else var2)
    var0 = e()
    if (1 if e() == 0 else 0):
        break
    if (1 if (i32_load8_u((var0 - 4)) & 3) == 0 else 0):
        break
    func98(var0, 0, var2)
    return var0


# ==========================================================
# $func259
# ==========================================================
def func259(var0, var1):
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
    var2 = (global0 - 128)
    global global0
    global0 = (global0 - 128)
    while True:  # loop $label1
        var4 = ((i32_load((var0 + (var7 << 2))) * 404) + 9568096)
        var3 = i32_load(((i32_load((var0 + (var7 << 2))) * 404) + 9568096) + 84)
        var5 = i32_load(var4 + 100)
        var6 = i32_load(var4 + 92)
        var8 = i32_load(var4 + 104)
        var13 = i64_load(var4 + 76)
        var9 = i32_load(var4 + 88)
        var14 = i64_load(var4 + 68)
        var10 = i32_load(var4 + 264)
        i32_store(var2 + 80, i32_load(i32_load(var4 + 180) + 8))
        i32_store(var2 + 84, var10)
        i64_store(var2 + 88, var14)
        i32_store(var2 + 112, var9)
        i32_store(var2 + 108, var7)
        i32_store(var2 + 104, var1)
        i64_store(var2 + 96, var13)
        i32_store(var2 + 68, var8)
        i32_store(var2 + 72, var6)
        i32_store(var2 + 76, var5)
        i32_store(var2 + 64, var3)
        var3 = i32_load(var4 + 236)
        if i32_load(var4 + 236):
            var5 = 0
            while True:  # loop $label0
                var6 = ((i32_load((i32_load(var4 + 232) + (var5 << 2))) * 132) + 9216080)
                if i32_load8_u(((i32_load((i32_load(var4 + 232) + (var5 << 2))) * 132) + 9216080) + 23):
                    var3 = ((i32_load(var6 + 4) * 404) + 9568096)
                    var8 = i32_load(((i32_load(var6 + 4) * 404) + 9568096) + 84)
                    var9 = i32_load(var3 + 100)
                    var10 = i32_load(var3 + 92)
                    var11 = i32_load(var3 + 104)
                    var13 = i64_load(var3 + 76)
                    var12 = i32_load(var3 + 88)
                    var14 = i64_load(var3 + 68)
                    var3 = i32_load(var3 + 264)
                    i32_store(var2 + 16, i32_load(var6 + 8))
                    i32_store(var2 + 20, var3)
                    i64_store(var2 + 24, var14)
                    i32_store(var2 + 48, var12)
                    i64_store(var2 + 40, 0)
                    i64_store(var2 + 32, var13)
                    i32_store(var2 + 4, var11)
                    i32_store(var2 + 8, var10)
                    i32_store(var2 + 12, var9)
                    i32_store(var2, var8)
                    var3 = i32_load(var4 + 236)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) < var3 else 0):
                    continue
                break  # end loop
        var7 = (var7 + 1)
        if (1 if (var7 + 1) != 15 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var2 + 128)

