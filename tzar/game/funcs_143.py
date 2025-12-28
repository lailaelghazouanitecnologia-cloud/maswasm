"""
Auto-generated from WAT. Contains 9 functions.
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
# $func191
# ==========================================================
def func191(var0):
    var1 = 0
    var2 = 0
    func116((var0 + 172))
    func151(i32_load(var0 + 168))
    func136((var0 + 124))
    func136((var0 + 136))
    # Unknown: memory.fill []
    i32_store(var0 + 16, 0)
    if (1 if i32_load(var0 + 192) > 0 else 0):
        while True:  # loop $label0
            var2 = (var0 + (var1 * 20))
            i32_store(var2 + 212, 0)
            var1 = (var1 + 1)
            if (1 if (var1 + 1) < i32_load(var0 + 192) else 0):
                continue
            break  # end loop
    i32_store(var0 + 276, 0)
    i32_store(var0 + 192, 0)
    i32_store(var0 + 12, 0)
    i32_store(var0 + 280, 0)


# ==========================================================
# $func198
# ==========================================================
def func198(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = i32_load(9561692)
    i32_store(var0 + 80, 0)
    var2 = (i32_load(var0 + 84) + 1)
    i32_store(var0 + 84, (i32_load(var0 + 84) + 1))
    var1 = (var1 + (i32_load16_u(var0 + 110) * 286704))
    var3 = ((var1 + (i32_load16_u(var0 + 110) * 286704)) + 281672)
    i32_store(((var1 + (i32_load16_u(var0 + 110) * 286704)) + 281672), (i32_load(var3) + 1))
    if (1 if i32_load((var1 + 284388)) == var2 else 0):
        func201(var0)
        i32_store(var1 + 283936, (i32_load(var1 + 283936) + 1))
        var2 = (var1 + 281636)
        i32_store((var1 + 281636), (i32_load(var2) + 1))
    var1 = (var1 + 284020)
    i32_store(var0 + 64, (i32_load(var0 + 64) + i32_load((var1 + 284020))))
    i32_store(var0 + 68, (i32_load(var0 + 68) + i32_load(var1)))
    var1 = i32_load(var0 + 84)
    var2 = (i32_load(var0 + 84) & 1)
    var3 = (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 224) > 1 else 0)
    i32_store(var0 + 52, (i32_load(var0 + 52) + ((i32_load(var0 + 84) & 1) if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 224) > 1 else 0) else 1)))
    i32_store(var0 + 60, (i32_load(var0 + 60) + ((1 if (var1 & 3) == 1 else 0) if var3 else var2)))
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
            break


# ==========================================================
# $func206
# ==========================================================
def func206(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var4 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if i32_load8_u(var0 + 126) == 1 else 0):
        break
    var1 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 296)
    var2 = (i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704))
    var3 = i32_load(((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 284144))
    i32_store8(var0 + 126, 1)
    i32_store(var0 + 52, (i32_load(var0 + 52) + (((var1 * var3) & 0xFFFFFFFF) // 100)))
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
            break
    var1 = i32_load16_u(var0 + 114)
    var2 = i32_load16_u(var0 + 112)
    var6 = i32_load(i32_load(9142424) + 48)
    if i32_load(i32_load(9142424) + 48):
        if (1 if i32_load8_u(9147152) == 0 else 0):
            break
    var3 = i32_load(9142440)
    break
    var3 = i32_load(9142440)
    var5 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var1) + var2) << 1)))
    if (1 if var6 == 2 else 0):
        if (1 if var5 > 1 else 0):
            break
        break
    if (1 if var5 == 0 else 0):
        break
    func80(float(var2), float(var1), i32_load(9142460), 32.0, float((var3 * 96)))
    var1 = i32_load16_u(var0 + 114)
    var2 = i32_load16_u(var0 + 112)
    var0 = ((var2 << 5) - i32_load(9142952))
    var0 = ((var1 << 5) - i32_load(9142956))
    if (1 if (((((var2 << 5) - i32_load(9142952)) * var0) + (((var1 << 5) - i32_load(9142956)) * var0)) - 1) > 9000000 else 0):
        break
    var3 = i32_load(39884)
    var5 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var0 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var1) + var2) << 1)))
    if (1 if var5 == 2 else 0):
        if (1 if var0 > 1 else 0):
            break
        break
    if (1 if var0 == 0 else 0):
        break
    i32_store(var4 + 8, var1)
    i32_store(var4 + 4, var2)
    i32_store(var4, var3)
    a_b()
    global global0
    global0 = (var4 + 16)


# ==========================================================
# $func210
# ==========================================================
def func210(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var5 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if ((i32_load8_u(var0 + 11) & 0xFFFFFFFF) >> 7):
    else:
    var4 = 10
    if ((i32_load8_u(var0 + 11) & 0xFFFFFFFF) >> 7):
        break
    var3 = (i32_load8_u(var0 + 11) & 127)
    if (1 if 10 <= (i32_load(var0 + 4) - (i32_load8_u(var0 + 11) & 127)) else 0):
        if (1 if var2 == 0 else 0):
            break
        if ((i32_load8_u(var0 + 11) & 0xFFFFFFFF) >> 7):
            break
        var4 = var0
        func122((var0 + var3), var1, var2)
        var1 = (var2 + var3)
        func312(var0, (var2 + var3))
        i32_store8(var5 + 15, 0)
        i32_store8((var1 + var4), i32_load8_u(var5 + 15))
        break
    global global0
    global0 = (var5 + 16)
    return var0


# ==========================================================
# $func242
# ==========================================================
def func242(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var1 = i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122)
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) == i32_load(38540) else 0):
        break
    if (1 if i32_load(38812) == var1 else 0):
        break
    if (1 if i32_load(38888) != var1 else 0):
        break
    i32_store(var2 + 4, i32_load(9213816))
    var1 = i32_load8_u(9147210)
    var0 = i32_load(9213808)
    if (1 if i32_load(9671124) == 95 else 0):
        if var1:
            func41(7, 9173808, var0, (var2 + 4), 1)
            break
        var3 = (var0 << 2)
        var1 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var0:
            # Unknown: memory.copy []
        # call_indirect via table[i32_load(9213880)]
        break
    if var1:
        func41(8, 9173808, var0, (var2 + 4), 1)
        break
    var3 = (var0 << 2)
    var1 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var0:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9213888)]
    break
    var4 = i32_load8_u(9163793)
    var1 = i32_load8_u(9163792)
    var3 = i32_load8_u(9163794)
    var5 = i32_load(9213812)
    var6 = i32_load8_u(9685856)
    i32_store(var2 + 4, var0)
    var0 = (0 if var6 else var5)
    var0 = (1 if var0 == 1 else 0)
    i32_store(var2 + 12, (0 if (1 if var0 == 1 else 0) else (0 if var6 else var5)))
    var4 = (-1 if var4 else (5 if var1 else (100 if var3 else 1)))
    i32_store(var2 + 8, (-1 if var0 else ((-1 if var3 else (-1 if var4 else (5 if var1 else (100 if var3 else 1)))) if var1 else var4)))
    var0 = i32_load(9213808)
    if i32_load8_u(9147210):
        func41(0, 9173808, var0, (var2 + 4), 3)
        break
    var3 = (var0 << 2)
    var1 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var0:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9213824)]
    global global0
    global0 = (var2 + 16)


# ==========================================================
# $func254
# ==========================================================
def func254(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0.0
    if (1 if var0 == 0 else 0):
        break
    var3 = i32_load(var0 + 16)
    var0 = i32_load(var0 + 24)
    if (1 if i32_load(var0 + 24) >= 100 else 0):
        var4 = f32_load((((var0 + var3) << 2) + 32700))
        if (1 if ((1 if f32_load((((var0 + var3) << 2) + 32700)) < 4294967300.0 else 0) & (1 if var4 >= 0.0 else 0)) == 0 else 0):
            break
        var2 = int(var4)
        break
    var2 = ((var3 * 1000) // var0)


# ==========================================================
# $func294
# ==========================================================
def func294(var0):
    var1 = 0
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    var1 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
            break


# ==========================================================
# $func297
# ==========================================================
def func297(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var3 = i32_load8_u(var0 + 122)
    var2 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 136)
    var4 = ((((i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 136) * 150) & 0xFFFFFFFF) // 100) if (1 if i32_load((((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + (i32_load(39216) << 2)) + 281808)) == 1 else 0) else var2)
    var2 = i32_load(var0 + 16)
    if (1 if i32_load(var0 + 16) == 0 else 0):
        var2 = func26(16)
        i32_store(func26(16) + 4, var4)
        i32_store(var2, func26((-1 if (1 if var4 > 1073741823 else 0) else (var4 << 2))))
        i64_store(var2 + 8, 4294967296)
        i32_store(var0 + 16, var2)
    if (1 if i32_load(((var3 * 404) + 9568096) + 264) != 1 else 0):
        break
    if i32_load(var2 + 8):
        break
    var2 = i32_load(var0 + 16)
    var0 = i32_load(var2 + 8)
    if (1 if var4 > i32_load(var2 + 8) else 0):
        if (1 if i32_load(var2 + 4) != var0 else 0):
            var5 = i32_load(var2)
            var3 = var0
            break
        var3 = (i32_load(var2 + 12) + var0)
        i32_store(var2 + 4, (i32_load(var2 + 12) + var0))
        var6 = i32_load(var2)
        var5 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
        if var0:
            # Unknown: memory.copy []
        var3 = var0
        if var6:
            var3 = i32_load(var2 + 8)
        i32_store(var2, var5)
        i32_store(var2 + 8, (var3 + 1))
        i32_store((var5 + (var3 << 2)), var1)
    return (1 if var0 < var4 else 0)


# ==========================================================
# $func318
# ==========================================================
def func318(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var0 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = i32_load8_u(9147152)
    if (1 if i32_load8_u(9147152) == 0 else 0):
        var4 = i32_load(var1)
        break
    var4 = i32_load(9142440)
    var5 = i32_load(var1)
    if (1 if i32_load(9142440) == i32_load(var1) else 0):
        break
    i32_store(var0, var5)
    var3 = i32_load8_u(9147152)
    break
    i32_store(9142440, var4)
    if (1 if var3 == 0 else 0):
        break
    var3 = i32_load(var1 + 24)
    var4 = i32_load(9142424)
    if (1 if i32_load(var1 + 24) == i32_load(i32_load(9142424) + 24) else 0):
        break
    i32_store(var4 + 24, var3)
    Gb(var2)
    i32_store(9142424, 0)
    var4 = (var2 << 2)
    var3 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    i32_store(9142428, var2)
    i32_store(9142424, var3)
    if var2:
        # Unknown: memory.copy []
    global global0
    global0 = (var0 + 16)

