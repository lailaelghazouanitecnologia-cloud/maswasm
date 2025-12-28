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
# $func187
# ==========================================================
def func187(var0):
    var1 = 0
    var2 = 0
    var2 = (var0 - -64)
    if (1 if i32_load((var0 - -64)) >= i32_load(var0 + 56) else 0):
        break
    while True:  # loop $label1
        if (1 if i32_load(var0 + 24) > 0 else 0):
            break
        func91(0  # stack underflow, var0)
        var1 = (var1 + 1)
        if (1 if i32_load(var2) < i32_load(var0 + 56) else 0):
            continue
        break  # end loop
    return var1


# ==========================================================
# $func203
# ==========================================================
def func203(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) != 1 else 0):
        break
    if i32_load(var0 + 80):
        break
    var3 = i32_load16_u(var0 + 116)
    if (1 if i32_load16_u(var0 + 116) == 0 else 0):
        break
    var4 = i32_load16_u(var0 + 118)
    if (1 if i32_load16_u(var0 + 118) == 0 else 0):
        break
    if (1 if i32_load8_u(9147152) == 0 else 0):
        if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var0 + 110))))) == 0 else 0):
            break
        if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 20 else 0):
            break
        if (1 if i32_load8_u(var0 + 127) == 6 else 0):
            break
    if i32_load8_u(9142917):
        break
    var1 = i32_load(9299880)
    if i32_load(9299880):
        var1 = (var1 - 1)
        i32_store(9299880, (var1 - 1))
        var1 = i32_load((i32_load(9299872) + (var1 << 2)))
        break
    var1 = i32_load(9163776)
    var5 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var6 = i32_load(9163784)
    if (1 if var5 < i32_load(9163784) else 0):
        break
    i32_store(var2, var6)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    var4 = i32_load16_u(var0 + 118)
    var3 = i32_load16_u(var0 + 116)
    i32_store(var0 + 80, var1)
    global global0
    global0 = (var2 + 16)


# ==========================================================
# $func222
# ==========================================================
def func222(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var0 = 0
    i32_store(9671124, 95)
    i32_store(9671120, 0)
    var3 = (i32_load(9671128) + (i32_load(9173808) * 132))
    var1 = i32_load((i32_load(9671128) + (i32_load(9173808) * 132)) + 20)
    if (1 if i32_load((i32_load(9671128) + (i32_load(9173808) * 132)) + 20) == 0 else 0):
        break
    var1 = i32_load(var1)
    var2 = i32_load(i32_load(var1))
    if i32_load(i32_load(var1)):
        i32_store(9263072, i32_load(((var2 * 404) + 9567872)))
        i32_store(9671120, 1)
        var1 = i32_load(i32_load(var3 + 20))
        var0 = 1
    var2 = i32_load(var1 + 4)
    if i32_load(var1 + 4):
        i32_store(((var0 << 2) + 9263072), i32_load(((var2 * 404) + 9567872)))
        var0 = (var0 + 1)
        i32_store(9671120, (var0 + 1))
        var1 = i32_load(i32_load(var3 + 20))
    var2 = i32_load(var1 + 8)
    if i32_load(var1 + 8):
        i32_store(((var0 << 2) + 9263072), i32_load(((var2 * 404) + 9567872)))
        var0 = (var0 + 1)
        i32_store(9671120, (var0 + 1))
        var1 = i32_load(i32_load(var3 + 20))
    var2 = i32_load(var1 + 12)
    if i32_load(var1 + 12):
        i32_store(((var0 << 2) + 9263072), i32_load(((var2 * 404) + 9567872)))
        var0 = (var0 + 1)
        i32_store(9671120, (var0 + 1))
        var1 = i32_load(i32_load(var3 + 20))
    var2 = i32_load(var1 + 16)
    if i32_load(var1 + 16):
        i32_store(((var0 << 2) + 9263072), i32_load(((var2 * 404) + 9567872)))
        var0 = (var0 + 1)
        i32_store(9671120, (var0 + 1))
        var1 = i32_load(i32_load(var3 + 20))
    var2 = i32_load(var1 + 20)
    if i32_load(var1 + 20):
        i32_store(((var0 << 2) + 9263072), i32_load(((var2 * 404) + 9567872)))
        var0 = (var0 + 1)
        i32_store(9671120, (var0 + 1))
        var1 = i32_load(i32_load(var3 + 20))
    var2 = i32_load(var1 + 24)
    if i32_load(var1 + 24):
        i32_store(((var0 << 2) + 9263072), i32_load(((var2 * 404) + 9567872)))
        var0 = (var0 + 1)
        i32_store(9671120, (var0 + 1))
    else:
    var1 = i32_load(var1 + 28)
    if (1 if i32_load(var1 + 28) == 0 else 0):
        break
    i32_store(((var0 << 2) + 9263072), i32_load(((var1 * 404) + 9567872)))
    i32_store(9671120, (var0 + 1))
    return func46(0, 1)


# ==========================================================
# $func223
# ==========================================================
def func223(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var0 = 0
    i32_store(9671124, 96)
    i32_store(9671120, 0)
    var3 = (i32_load(9671128) + (i32_load(9173808) * 132))
    var1 = i32_load((i32_load(9671128) + (i32_load(9173808) * 132)) + 20)
    if (1 if i32_load((i32_load(9671128) + (i32_load(9173808) * 132)) + 20) == 0 else 0):
        break
    var1 = i32_load(var1)
    var2 = i32_load(i32_load(var1) + 32)
    if i32_load(i32_load(var1) + 32):
        i32_store(9263072, i32_load(((var2 * 404) + 9567872)))
        i32_store(9671120, 1)
        var1 = i32_load(i32_load(var3 + 20))
        var0 = 1
    var2 = i32_load(var1 + 36)
    if i32_load(var1 + 36):
        i32_store(((var0 << 2) + 9263072), i32_load(((var2 * 404) + 9567872)))
        var0 = (var0 + 1)
        i32_store(9671120, (var0 + 1))
        var1 = i32_load(i32_load(var3 + 20))
    var2 = i32_load(var1 + 40)
    if i32_load(var1 + 40):
        i32_store(((var0 << 2) + 9263072), i32_load(((var2 * 404) + 9567872)))
        var0 = (var0 + 1)
        i32_store(9671120, (var0 + 1))
        var1 = i32_load(i32_load(var3 + 20))
    var2 = i32_load(var1 + 44)
    if i32_load(var1 + 44):
        i32_store(((var0 << 2) + 9263072), i32_load(((var2 * 404) + 9567872)))
        var0 = (var0 + 1)
        i32_store(9671120, (var0 + 1))
        var1 = i32_load(i32_load(var3 + 20))
    var2 = i32_load(var1 + 48)
    if i32_load(var1 + 48):
        i32_store(((var0 << 2) + 9263072), i32_load(((var2 * 404) + 9567872)))
        var0 = (var0 + 1)
        i32_store(9671120, (var0 + 1))
        var1 = i32_load(i32_load(var3 + 20))
    var2 = i32_load(var1 + 52)
    if i32_load(var1 + 52):
        i32_store(((var0 << 2) + 9263072), i32_load(((var2 * 404) + 9567872)))
        var0 = (var0 + 1)
        i32_store(9671120, (var0 + 1))
        var1 = i32_load(i32_load(var3 + 20))
    var2 = i32_load(var1 + 56)
    if i32_load(var1 + 56):
        i32_store(((var0 << 2) + 9263072), i32_load(((var2 * 404) + 9567872)))
        var0 = (var0 + 1)
        i32_store(9671120, (var0 + 1))
    else:
    var1 = i32_load(var1 + 60)
    if (1 if i32_load(var1 + 60) == 0 else 0):
        break
    i32_store(((var0 << 2) + 9263072), i32_load(((var1 * 404) + 9567872)))
    i32_store(9671120, (var0 + 1))
    return func46(0, 1)


# ==========================================================
# $func232
# ==========================================================
def func232(var0):
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
    if (1 if var0 == 0 else 0):
        break
    var8 = i32_load(9142836)
    var2 = (i32_load(9142836) + (var0 * 80))
    if i32_load((i32_load(9142836) + (var0 * 80))):
        break
    var2 = (var0 + 1)
    var6 = ((var0 + 1) * var2)
    var9 = func26((-1 if (var6 & 402653184) else (((var0 + 1) * var2) << 5)))
    i32_store(var2, func26((-1 if (var6 & 402653184) else (((var0 + 1) * var2) << 5))))
    var10 = (var0 << 1)
    var2 = (0 - var0)
    if (1 if (var0 << 1) > (0 - var0) else 0):
        var4 = (var8 + (var0 * 80))
        var12 = (var0 * var0)
        var3 = var2
        while True:  # loop $label2
            var13 = ((var3 * var3) - 1)
            var1 = var2
            while True:  # loop $label1
                if (1 if var12 >= (var13 + (var1 * var1)) else 0):
                    var7 = i32_load(var4 + 4)
                    i32_store(var4 + 4, (i32_load(var4 + 4) + 1))
                    i32_store((var9 + (var7 << 2)), var3)
                    var7 = i32_load(var4 + 4)
                    i32_store(var4 + 4, (i32_load(var4 + 4) + 1))
                    i32_store((var9 + (var7 << 2)), var1)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var10 else 0):
                    continue
                break  # end loop
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var10 else 0):
                continue
            break  # end loop
    var6 = (-1 if (var6 & 805306368) else (var6 << 4))
    var14 = (var0 * var0)
    var8 = (var8 + (var0 * 80))
    while True:  # loop $label7
        var2 = (var15 << 2)
        var11 = (var8 + (var15 << 2))
        var16 = func26(var6)
        i32_store((var8 + (var15 << 2)) + 8, func26(var6))
        var17 = i32_load((var2 + 9264))
        var5 = (i32_load((var2 + 9264)) - var0)
        var9 = (var10 + var17)
        if (1 if (i32_load((var2 + 9264)) - var0) >= (var10 + var17) else 0):
            break
        var4 = i32_load((var2 + 9344))
        var2 = (i32_load((var2 + 9344)) - var0)
        var12 = (var4 + var10)
        if (1 if (i32_load((var2 + 9344)) - var0) >= (var4 + var10) else 0):
            break
        while True:  # loop $label6
            var13 = ((var5 * var5) - 1)
            var1 = (var5 - var17)
            var7 = (((var5 - var17) * var1) - 1)
            var1 = var2
            while True:  # loop $label5
                var3 = (var1 - var4)
                if (1 if (var7 + ((var1 - var4) * var3)) > var14 else 0):
                    break
                if (1 if (var13 + (var1 * var1)) <= var14 else 0):
                    break
                var3 = i32_load(var11 + 44)
                i32_store(var11 + 44, (i32_load(var11 + 44) + 1))
                i32_store((var16 + (var3 << 2)), var5)
                var3 = i32_load(var11 + 44)
                i32_store(var11 + 44, (i32_load(var11 + 44) + 1))
                i32_store((var16 + (var3 << 2)), var1)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var12 else 0):
                    continue
                break  # end loop
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var9 else 0):
                continue
            break  # end loop
        var15 = (var15 + 1)
        if (1 if (var15 + 1) != 9 else 0):
            continue
        break  # end loop

