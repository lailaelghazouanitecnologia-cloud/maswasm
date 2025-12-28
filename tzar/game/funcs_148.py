"""
Auto-generated from WAT. Contains 10 functions.
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
# $func521
# ==========================================================
def func521(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var6 = i32_load(9671128)
    var4 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) != 3 else 0):
        var7 = i32_load16_u(var4 + 110)
        var8 = i32_load(9561692)
        var1 = i32_load(var4 + 20)
        if (1 if i32_load(var4 + 20) == 0 else 0):
            var1 = func26(16)
            i32_store(func26(16) + 4, 17)
            var2 = func26(68)
            i32_store(var1 + 12, 1)
            i32_store(var1, var2)
            i32_store(var4 + 20, var1)
            # Unknown: memory.fill []
            i32_store(var1 + 8, 17)
            break
        var2 = i32_load(var1 + 4)
        if (1 if i32_load(var1 + 4) > 16 else 0):
            break
        var3 = i32_load(var1 + 8)
        if (1 if var2 <= (i32_load(var1 + 8) + 17) else 0):
            var5 = ((var2 + i32_load(var1 + 12)) + 17)
            i32_store(var1 + 4, ((var2 + i32_load(var1 + 12)) + 17))
            var2 = i32_load(var1)
            var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
            if var3:
                # Unknown: memory.copy []
            if var2:
            i32_store(var1, var5)
            var1 = i32_load(var4 + 20)
        # Unknown: memory.fill []
        var5 = (var8 + (var7 * 286704))
        if (1 if i32_load((((var8 + (var7 * 286704)) + (i32_load(39128) << 2)) + 281808)) != 1 else 0):
            break
        var1 = i32_load(var1)
        var9 = i64_load(i32_load(var1) + 16)
        i64_store(var1 + 12, i64_load(var1 + 8))
        var2 = i32_load(var1 + 24)
        i64_store(var1 + 20, var9)
        i64_store(var1 + 4, i64_load(var1))
        i32_store(var1 + 28, var2)
        var9 = i64_load(9147316)
        var2 = i32_load(9147312)
        i32_store(9147316, i32_load(9147312))
        var3 = i32_load(9147324)
        i64_store(9147320, var9)
        var3 = (var3 ^ (var3 << 11))
        var2 = ((var2 ^ (((var2 & 0xFFFFFFFF) >> 19) ^ (((var3 ^ (var3 << 11)) & 0xFFFFFFFF) >> 8))) ^ var3)
        i32_store(9147312, ((var2 ^ (((var2 & 0xFFFFFFFF) >> 19) ^ (((var3 ^ (var3 << 11)) & 0xFFFFFFFF) >> 8))) ^ var3))
        i32_store(var1, (i32_load((((var2 % 19) << 2) + 9682096)) + 1))
        if (1 if i32_load(9671124) != 95 else 0):
            break
        if (1 if i32_load(9173808) != i32_load((var6 + (var0 * 132)) + 28) else 0):
            break
        if (1 if i32_load(((var5 + (i32_load(39132) << 2)) + 281808)) != 1 else 0):
            break
        var1 = i32_load(i32_load(var4 + 20))
        var9 = i64_load(i32_load(i32_load(var4 + 20)) + 40)
        i64_store(var1 + 36, i64_load(var1 + 32))
        var10 = i64_load(var1 + 48)
        i64_store(var1 + 44, var9)
        var2 = i32_load(var1 + 56)
        i64_store(var1 + 52, var10)
        i32_store(var1 + 60, var2)
        var9 = i64_load(9147316)
        var2 = i32_load(9147312)
        i32_store(9147316, i32_load(9147312))
        var3 = i32_load(9147324)
        i64_store(9147320, var9)
        var3 = (var3 ^ (var3 << 11))
        var2 = ((var2 ^ (((var2 & 0xFFFFFFFF) >> 19) ^ (((var3 ^ (var3 << 11)) & 0xFFFFFFFF) >> 8))) ^ var3)
        i32_store(9147312, ((var2 ^ (((var2 & 0xFFFFFFFF) >> 19) ^ (((var3 ^ (var3 << 11)) & 0xFFFFFFFF) >> 8))) ^ var3))
        i32_store(var1 + 32, (i32_load((((var2 % 19) << 2) + 9682096)) + 1))
        if (1 if i32_load(9671124) != 96 else 0):
            break
        if (1 if i32_load(9173808) != i32_load((var6 + (var0 * 132)) + 28) else 0):
            break
        var1 = i32_load(((i32_load(9561692) + (i32_load16_u(var4 + 110) * 286704)) + 284236))


# ==========================================================
# $func522
# ==========================================================
def func522(var0, var1):
    var2 = 0
    var3 = 0
    if (1 if var0 == 0 else 0):
        break
    var0 = i32_load(9213808)
    if (1 if i32_load(9213808) == 0 else 0):
        break
    if (1 if i32_load8_u(9163792) == 0 else 0):
        break
    var1 = i32_load(9140316)
    i32_store(9140316, (i32_load(9140316) + 1))
    var0 = (i32_load(9671128) + (i32_load((((var1 % var0) << 2) + 9173808)) * 132))
    var1 = i32_load(9140320)
    if (1 if i32_load(9140320) == 0 else 0):
        break
    var2 = i32_load(9671128)
    var3 = i32_load((i32_load(9671128) + (var1 * 132)) + 92)
    if (1 if i32_load((i32_load(9671128) + (var1 * 132)) + 92) == 0 else 0):
        break
    var0 = i32_load(var0 + 28)
    i32_store(9140320, i32_load(var0 + 28))


# ==========================================================
# $func526
# ==========================================================
def func526(var0, var1):
    var2 = 0
    if (1 if var0 == 0 else 0):
        var0 = i32_load(9213808)
        if i32_load8_u(9147210):
            func41(10, 9173808, var0, 0, 0)
            return
        var2 = (var0 << 2)
        var1 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var0:
            # Unknown: memory.copy []
        # call_indirect via table[i32_load(9213904)]


# ==========================================================
# $lb
# Export: lb
# ==========================================================
def lb():
    """Export: lb"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var0 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    i32_store(var0, i32_load(9681804))
    i32_store(var0 + 4, i32_load(9681808))
    i32_store(var0 + 8, i32_load(9681812))
    i32_store(var0 + 12, i32_load(9681816))
    i32_store(var0 + 16, i32_load(9681820))
    var1 = i32_load(9213808)
    if i32_load8_u(9147210):
        func41(33, 9173808, var1, var0, 5)
        break
    var3 = (var1 << 2)
    var2 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var1:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9214088)]
    global global0
    global0 = (var0 + 32)


# ==========================================================
# $_b
# Export: _b
# ==========================================================
def _b():
    """Export: _b"""
    var0 = 0
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
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store16(9147213, 1)
    i32_store8(9147124, 1)
    var0 = i32_load(9142848)
    i32_store(59160, i32_load(9142848))
    if i32_load8_u(9147152):
        break
    if (1 if i32_load8_u(9147212) == 0 else 0):
        break
    if i32_load(9147132):
        break
    i32_store(9561836, ((var0 & 0xFFFFFFFF) // 10))
    func52((207 if i32_load8_u(9143020) else 0), 0)
    a_b()
    if (1 if i32_load8_u(9147210) == 0 else 0):
        break
    if (1 if i32_load8_u(9142388) == 0 else 0):
        break
    if (1 if i32_load8_u(9147125) == 0 else 0):
        break
    func344()
    if (1 if i32_load(9147132) == 0 else 0):
        var3 = i32_load(9561692)
        var5 = i32_load(9142872)
        var1 = (i32_load(9561692) + (i32_load(9142872) * 286704))
        var0 = i32_load((i32_load(9561692) + (i32_load(9142872) * 286704)) + 283896)
        if i32_load((i32_load(9561692) + (i32_load(9142872) * 286704)) + 283896):
            break
        var0 = 0
        if i32_load(var1 + 283900):
            break
        var4 = (var1 + 283896)
        var6 = (var1 + 283900)
        var7 = (var3 + (var5 * 286704))
        var1 = 0
        while True:  # loop $label6
            var0 = i32_load(((var7 + (var1 << 2)) + 284636))
            if (1 if i32_load(((var7 + (var1 << 2)) + 284636)) == 0 else 0):
                break
            var8 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var9 = i32_load(var0)
            var0 = 0
            while True:  # loop $label5
                var10 = i32_load((var9 + (var0 << 2)))
                if (1 if i32_load((var9 + (var0 << 2))) == 0 else 0):
                    var0 = (var0 + 1)
                    if (1 if var8 != (var0 + 1) else 0):
                        continue
                    break
                break  # end loop
            var1 = (i32_load(9671128) + (var10 * 132))
            var4 = ((i32_load8_u((i32_load(9671128) + (var10 * 132)) + 122) * 404) + 9568096)
            var0 = (((i32_load(((i32_load8_u((i32_load(9671128) + (var10 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + i32_load16_u(var1 + 112))
            i32_store(var4, (((i32_load(((i32_load8_u((i32_load(9671128) + (var10 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + i32_load16_u(var1 + 112)))
            i32_store(var6, (i32_load16_u(var1 + 114) + ((i32_load(var4 + 220) & 0xFFFFFFFF) >> 1)))
            break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != 255 else 0):
                continue
            break  # end loop
        var0 = 0
        if i32_load8_u(9142917):
            break
        var1 = (var3 + (var5 * 286704))
        var3 = i32_load((var3 + (var5 * 286704)) + 283900)
        i32_store(var2, (var0 << 5))
        i32_store(var2 + 4, (var3 << 5))
        var0 = i32_load(var1 + 284624)
        if (1 if i32_load(var1 + 284624) == 0 else 0):
            break
        if i32_load8_u(9142917):
            break
        func44((i32_load(9671128) + (var0 * 132)), 0)
        la()
        break
    i32_store(9142872, 0)
    global global0
    global0 = (var2 + 16)


# ==========================================================
# $func547
# ==========================================================
def func547(var0):
    var1 = 0
    var2 = 0
    var0 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var1 = i32_load(9173808)
    i32_store(var0 + 12, i32_load(9173808))
    if i32_load8_u(9147210):
        func41(3, (var0 + 12), 1, 0, 0)
        break
    var2 = func26(4)
    i32_store(func26(4), var1)
    # call_indirect via table[i32_load(9213848)]
    global global0
    global0 = (var0 + 16)


# ==========================================================
# $Tb
# Export: Tb
# ==========================================================
def Tb(var0, var1, var2, var3, var4):
    """Export: Tb"""
    var5 = 0
    var5 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    i32_store(var5 + 16, var4)
    i32_store(var5 + 12, var3)
    i32_store(var5 + 8, var2)
    i32_store(var5 + 4, var1)
    i32_store(var5, var0)
    if i32_load8_u(9147210):
        func41(41, 0, 0, var5, 5)
        break
    # call_indirect via table[i32_load(9214152)]
    global global0
    global0 = (var5 + 32)


# ==========================================================
# $func559
# ==========================================================
def func559(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var1 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    i32_store8(9163792, var0)
    if var0:
        break
    if i32_load(9684820):
        var6 = 2
        var0 = i32_load(9684820)
        var7 = ((((i32_load(9684820) * 7) & 0xFFFFFFFF) // 6) + 2)
        var4 = func26((((((i32_load(9684820) * 7) & 0xFFFFFFFF) // 6) + 2) << 2))
        i32_store(func26((((((i32_load(9684820) * 7) & 0xFFFFFFFF) // 6) + 2) << 2)) + 4, ((var0 & 0xFFFFFFFF) // 6))
        i32_store(var4, -1)
        if var0:
            while True:  # loop $label1
                var0 = (var4 + (var6 << 2))
                var5 = i32_load(9684812)
                var8 = (var3 << 2)
                var2 = (i32_load(9684812) + (var3 << 2))
                i32_store((var4 + (var6 << 2)), i32_load((i32_load(9684812) + (var3 << 2))))
                i32_store(var0 + 4, i32_load((var5 + (var8 | 4))))
                i32_store(var0 + 8, i32_load(var2 + 8))
                var5 = i32_load(var2 + 12)
                i32_store(var0 + 16, 0)
                i32_store(var0 + 12, var5)
                var5 = i32_load(var2 + 16)
                i32_store(var0 + 24, 0)
                i32_store(var0 + 20, var5)
                func38(i32_load(var2 + 20))
                var6 = (var6 + 7)
                var3 = (var3 + 6)
                if (1 if (var3 + 6) < i32_load(9684820) else 0):
                    continue
                break  # end loop
        var0 = i32_load(9213808)
        if i32_load8_u(9147210):
            func41(5, 9173808, var0, var4, var7)
            break
        var3 = (var0 << 2)
        var2 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var0:
            # Unknown: memory.copy []
        # call_indirect via table[i32_load(9213864)]
        i32_store(9684820, 0)
    if (1 if i32_load(9671176) == 0 else 0):
        break
    if i32_load(9671192):
        var0 = 0
        while True:  # loop $label4
            func38(i32_load((i32_load(9671184) + (var0 << 2))))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < i32_load(9671192) else 0):
                continue
            break  # end loop
    i32_store(9671192, 0)
    i32_store(9671176, 0)
    i32_store8(9142412, 0)
    if (1 if i32_load8_u(9684396) == 0 else 0):
        break
    i32_store8(9684396, 0)
    a_b()
    i32_store(40604, -1)
    if (1 if i32_load(9684792) == 0 else 0):
        break
    i32_store(9684792, 0)
    var0 = i32_load(9684796)
    if i32_load8_u(9142916):
        i32_store(var1 + 32, var0)
        a_b()
        break
    i32_store(var1 + 24, var0)
    i64_store(var1 + 16, -4602115869219225600)
    i64_store(var1 + 8, 0)
    i64_store(var1, 0)
    a_b()
    global global0
    global0 = (var1 + 48)


# ==========================================================
# $func580
# ==========================================================
def func580(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if i32_load8_u(9163793):
        i32_store(var1 + 8, var0)
        i32_store(var1 + 12, i32_load8_u(9163792))
        var0 = i32_load(9213808)
        if i32_load8_u(9147210):
            func41(42, 9173808, var0, (var1 + 8), 2)
            break
        var3 = (var0 << 2)
        var2 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var0:
            # Unknown: memory.copy []
        # call_indirect via table[i32_load(9214160)]
        break
    i32_store(40604, var0)
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $func581
# ==========================================================
def func581(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if var0 != 18 else 0):
        i32_store(40604, var0)
        break
    if (1 if i32_load8_u(9163793) == 0 else 0):
        i32_store(40604, 18)
        if i32_load(9216064):
            break
        i32_store(41088, 10)
        i64_store(var1, 10)
        break
    i32_store(var1 + 12, 0)
    var0 = i32_load(9213808)
    if i32_load8_u(9147210):
        func41(13, 9173808, var0, (var1 + 12), 1)
        break
    var3 = (var0 << 2)
    var2 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var0:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9213928)]
    global global0
    global0 = (var1 + 16)

