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
# $func1078
# ==========================================================
def func1078(var0, var1, var2):
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
    var4 = i32_load(var0 + 36)
    if (1 if i32_load((i32_load(var0 + 36) - -64)) >= i32_load(var4 + 56) else 0):
        break
    var6 = i32_load(var0)
    var9 = i32_load(i32_load(var0))
    var10 = ((1 if i32_load(i32_load(var0)) == 4 else 0) | (1 if var9 == 9 else 0))
    var7 = i32_load(var6 + 20)
    var11 = (i32_load(var6 + 16) + (i32_load(var6 + 20) * var1))
    var12 = i32_load(var4 + 52)
    if (1 if i32_load(var4 + 24) > 0 else 0):
        break
    if (1 if var2 <= 0 else 0):
        break
    var5 = (var11 + (0 if var10 else 3))
    while True:  # loop $label4
        if (1 if i32_load(i32_load(var0) + 8) <= (var1 + var3) else 0):
            break
        func91(0  # stack underflow, var4)
        # call_indirect via table[i32_load(9687300)]
        var8 = (call_indirect(i32_load(9687300)) | var8)
        var3 = (var3 + 1)
        var7 = i32_load(var6 + 20)
        var4 = i32_load(var0 + 36)
        if (1 if i32_load((i32_load(var0 + 36) - -64)) >= i32_load(var4 + 56) else 0):
            break
        if (1 if i32_load(var4 + 24) > 0 else 0):
            break
        var5 = (var5 + var7)
        if (1 if var2 > var3 else 0):
            continue
        break  # end loop
    var5 = (1 if var8 != 0 else 0)
    if (1 if (var9 - 7) > 3 else 0):
        break
    if (1 if var5 == 0 else 0):
        break
    # call_indirect via table[i32_load(9687292)]
    return var3
    a_c()
    raise RuntimeError('unreachable')
    return 5680


# ==========================================================
# $func1080
# ==========================================================
def func1080(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var1 = i32_load(var1)
    var6 = i32_load(i32_load(var1) + 24)
    var7 = i32_load(var1 + 40)
    var2 = i32_load(var1 + 20)
    var3 = i32_load(var1 + 36)
    var4 = i32_load(var1 + 32)
    var5 = i32_load(var0 + 8)
    var4 = i32_load(var0 + 12)
    var8 = i32_load(var0 + 16)
    func268(i32_load(var0 + 20), i32_load(var0 + 32), (i32_load(var1 + 16) + (i32_load(var1 + 32) * i32_load(var0 + 8))), var4, i32_load(var0 + 12), i32_load(var0 + 16))
    var5 = (var5 >> 1)
    var2 = ((var4 + 1) // 2)
    var3 = ((var8 + 1) // 2)
    func268(i32_load(var0 + 24), i32_load(var0 + 36), (var2 + (var3 * (var5 >> 1))), i32_load(var1 + 36), ((var4 + 1) // 2), ((var8 + 1) // 2))
    func268(i32_load(var0 + 28), i32_load(var0 + 36), (var6 + (var5 * var7)), i32_load(var1 + 40), var2, var3)
    return i32_load(var0 + 16)


# ==========================================================
# $func1083
# ==========================================================
def func1083(var0, var1):
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
    var6 = i32_load(var0 + 16)
    if (1 if i32_load(var0 + 16) <= 0 else 0):
        return 0
    var11 = ((var6 + 1) >> 1)
    var2 = i32_load(var1 + 24)
    while True:  # loop $label5
        var2 = i32_load(var0 + 32)
        var12 = func82(var2, (var6 - var7), (i32_load(var0 + 20) + (i32_load(var0 + 32) * var7)), var2)
        var2 = i32_load(var1 + 28)
        var3 = i32_load(i32_load(var1 + 28) + 32)
        var3 = (((i32_load(i32_load(var1 + 28) + 32) + i32_load(var2 + 24)) - 1) // var3)
        var2 = (var11 - var4)
        if ((((i32_load(i32_load(var1 + 28) + 32) + i32_load(var2 + 24)) - 1) // var3) if (1 if var2 > var3 else 0) else (var11 - var4)):
            var3 = i32_load(var0 + 36)
            var3 = func82(i32_load(var1 + 28), var2, (i32_load(var0 + 24) + (i32_load(var0 + 36) * var4)), var3)
            var2 = i32_load(var0 + 36)
            if (1 if func82(i32_load(var1 + 28), var2, (i32_load(var0 + 24) + (i32_load(var0 + 36) * var4)), var3) != func82(i32_load(var1 + 32), var2, (i32_load(var0 + 28) + (i32_load(var0 + 36) * var4)), var2) else 0):
                break
            var4 = (var3 + var4)
        var3 = 0
        var2 = i32_load(var1 + 24)
        if (1 if i32_load((i32_load(var1 + 24) - -64)) >= i32_load(var2 + 56) else 0):
            break
        var8 = i32_load(var1)
        var13 = i32_load(((i32_load(i32_load(var1)) << 2) + 9687888))
        var14 = (i32_load(var1 + 16) + var9)
        var10 = (i32_load(var8 + 16) + ((i32_load(var1 + 16) + var9) * i32_load(var8 + 20)))
        while True:  # loop $label4
            if (1 if i32_load(var2 + 24) > 0 else 0):
                break
            var5 = i32_load(var1 + 28)
            if (1 if i32_load((i32_load(var1 + 28) - -64)) >= i32_load(var5 + 56) else 0):
                break
            var5 = i32_load(var5 + 24)
            if (1 if i32_load(var5 + 24) > 0 else 0):
                break
            if (1 if i32_load(i32_load(var1) + 8) <= (var3 + var14) else 0):
                break
            if (1 if var5 != i32_load(i32_load(var1 + 32) + 24) else 0):
                break
            func91(0  # stack underflow, var2)
            func91(0  # stack underflow, i32_load(var1 + 28))
            func91(0  # stack underflow, i32_load(var1 + 32))
            var2 = i32_load(var1 + 24)
            # call_indirect via table[var13]
            var3 = (var3 + 1)
            var10 = (var10 + i32_load(var8 + 20))
            var2 = i32_load(var1 + 24)
            if (1 if i32_load((i32_load(var1 + 24) - -64)) < i32_load(var2 + 56) else 0):
                continue
            break  # end loop
        var9 = (var3 + var9)
        var7 = (var7 + var12)
        if (1 if var6 > (var7 + var12) else 0):
            continue
        break  # end loop
    return var9
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    return 7626


# ==========================================================
# $func1085
# ==========================================================
def func1085(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if (1 if i32_load(var0 + 104) == 0 else 0):
        break
    if (1 if var2 <= 0 else 0):
        break
    var4 = (i32_load(var1 + 16) + var2)
    var3 = i32_load(var1 + 36)
    while True:  # loop $label1
        var5 = i32_load(var0 + 8)
        var6 = i32_load(var3 + 60)
        var7 = i32_load(var0)
        # call_indirect via table[i32_load(var1 + 52)]
        var2 = (var2 - call_indirect(i32_load(var1 + 52)))
        if (1 if (var2 - call_indirect(i32_load(var1 + 52))) > 0 else 0):
            continue
        break  # end loop
    return 0


# ==========================================================
# $func37
# ==========================================================
def func37(var0, var1, var2, var3):
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
    var18 = 0.0
    var19 = 0.0
    var20 = 0.0
    var21 = 0.0
    var5 = (global0 - 128)
    global global0
    global0 = (global0 - 128)
    if (1 if var1 == 0 else 0):
        break
    var11 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    var12 = i32_load(9142848)
    i32_store(var0 + 48, var1)
    var10 = i32_load16_u(var0 + 110)
    var4 = i32_load16_u(var0 + 120)
    var7 = i32_load8_u(var0 + 122)
    if i32_load(var0 + 92):
        var8 = 13
        if i32_load8_u(9142906):
            break
    var8 = (((var4 if var4 else var10) & 65535) + 16)
    if (1 if i32_load8_u(9142916) == 0 else 0):
        var4 = i32_load8_u(var0 + 127)
        var10 = ((var7 * 404) + 9568096)
        if (1 if (i32_load8_u(var0 + 127) | i32_load(((var7 * 404) + 9568096) + 156)) == 0 else 0):
            break
        var8 = i32_load(var10 + 156)
        var8 = (i32_load(var10 + 156) if var8 else var4)
        break
    var4 = i32_load8_u(var0 + 127)
    var8 = (i32_load8_u(var0 + 127) if var4 else var8)
    var10 = i32_load(((var7 * 404) + 9568096) + 264)
    var14 = i32_load(var1 + 32)
    var15 = i32_load(var1 + 24)
    var7 = i32_load(var1)
    var16 = i32_load(var1 + 16)
    var4 = (i32_load(var1 + 16) * i32_load(var1 + 20))
    if (i32_load(var1 + 16) * i32_load(var1 + 20)):
        var20 = float(float((i32_load(var1 + 4) // var4)))
    if (1 if var3 == 0 else 0):
        if i32_load8_u(9147152):
            var4 = i32_load8_u(var0 + 125)
            break
        var4 = i32_load(9142872)
        if (1 if i32_load(9142872) == 0 else 0):
            break
        if (1 if i32_load8_u((i32_load(9143012) + (i32_load16_u(var0 + 110) + (i32_load(9142892) * var4)))) == 0 else 0):
            break
        var4 = i32_load8_u(var0 + 125)
        if (1 if i32_load8_u(var0 + 125) == 3 else 0):
            break
        # br_table ['$label4', '$label5', '$label5', '$label5', '$label5', '$label5', '$label5', '$label5', '$label5', '$label5', '$label4', '$label5']
        _br_idx = (var4 - 4)
        break  # br_table
        var4 = i32_load8_u(var0 + 122)
        var6 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
        var9 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 216)
        var6 = i32_load(var6 + 220)
        break
        var4 = i32_load8_u(var0 + 122)
        var6 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 200)
        if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 200) == 0 else 0):
            break
        var9 = i32_load16_u(var0 + 114)
        var4 = ((var4 * 404) + 9568096)
        var9 = i32_load(var0 + 48)
        var18 = math.ceil(((float(((i32_load16_u(var0 + 114) + ((i32_load(((var4 * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1)) << 5)) - ((float(var9) * 32.0) - float(i32_load(i32_load(var0 + 48) + 12)))) * 0.03125))
        if (1 if abs(math.ceil(((float(((i32_load16_u(var0 + 114) + ((i32_load(((var4 * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1)) << 5)) - ((float(var9) * 32.0) - float(i32_load(i32_load(var0 + 48) + 12)))) * 0.03125))) < 2147483650.0 else 0):
            break
        var13 = (-2147483648 * 10)
        var6 = i32_load16_u(var0 + 112)
        var18 = math.ceil(((float(((i32_load16_u(var0 + 112) + ((i32_load(var4 + 216) & 0xFFFFFFFF) >> 1)) << 5)) - ((float(var6) * 32.0) - float(i32_load(var9 + 8)))) * 0.03125))
        if (1 if abs(math.ceil(((float(((i32_load16_u(var0 + 112) + ((i32_load(var4 + 216) & 0xFFFFFFFF) >> 1)) << 5)) - ((float(var6) * 32.0) - float(i32_load(var9 + 8)))) * 0.03125))) < 2147483650.0 else 0):
            break
        var18 = float((int(var18) + ((-2147483648 + var13) << 8)))
        var21 = float(var18)
    if (1 if i32_load8_u(9142916) == 0 else 0):
        i32_store(var5 + 112, var11)
        f64_store(var5 + 104, var21)
        i64_store(var5 + 96, -4616189618054758400)
        f64_store(var5 + 88, var20)
        f64_store(var5 + 80, float(float(var7)))
        a_b()
    var2 = (float((var12 * 25)) if (1 if var2 == 0.0 else 0) else var2)
    var13 = i32_load(var1 + 20)
    if i32_load(var1 + 20):
        var12 = i32_load8_u(var0 + 124)
        var11 = i32_load8_u(9142916)
        var4 = i32_load(var1 + 28)
        if (1 if i32_load(var1 + 28) == 2147483647 else 0):
            if var11:
                var4 = i32_load(59152)
                i32_store(59152, (i32_load(59152) + 1))
                var6 = i32_load(9568052)
                var9 = i32_load(var1)
                break
            var9 = i32_load(var1)
            var6 = i32_load(9568052)
            var4 = ((i32_load(var1) + i32_load(9140308)) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2))
            i32_store(var1 + 28, var4)
            var7 = i32_load(var1 + 4)
            var17 = i32_load(9568048)
            i32_store(9568048, (i32_load(9568048) + 1))
            i32_store(((var17 << 2) + 9563952), var1)
            i32_store(9568052, (((var9 * (var7 + 2)) << 2) + var6))
            if (1 if var11 == 0 else 0):
                break
            var3 = i32_load(9568056)
            i32_store(var1 + 56, i32_load(9568056))
            i32_store(9568056, (var3 + ((var7 * i32_load(var1)) << 2)))
            break
        if var11:
            break
        var7 = i32_load(var1 + 4)
        var2 = (var2 + -0.0)
        var19 = float((((((i32_load(var1) * var12) * var7) & 0xFFFFFFFF) // var13) + var4))
        var1 = i32_load(var0 + 40)
        break
    var2 = (var2 + -0.0)
    var4 = 0
    var1 = i32_load(var0 + 40)
    if i32_load8_u(9142916):
        break
    i32_store(var5 + 16, ((15 if (1 if var10 == 1 else 0) else var8) if var3 else var8))
    f64_store(var5 + 24, float(float(((((200 if (1 if var14 == 27 else 0) else (0 if (var10 & -5) else 100)) + var16) << 16) + var15))))
    i32_store(var5 + 32, var1)
    f64_store(var5 + 8, float(var2))
    f64_store(var5, float((var19 / float(i32_load(59156)))))
    a_b()
    break
    var2 = (var2 + -0.0)
    var4 = (var4 + (var12 << 16))
    i32_store(var5, i32_load(var0 + 40))
    i32_store(var5 + 48, var4)
    f64_store(var5 + 56, float(var2))
    a_b()
    if i32_load8_u(9142916):
        break
    global global0
    global0 = (var5 + 128)
    return func60(var0, 1.0)

