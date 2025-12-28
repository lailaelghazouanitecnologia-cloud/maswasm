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
# $func805
# ==========================================================
def func805(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var8 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = i32_load(var0 + 12)
    var5 = (i32_load(var0 + 12) + 16)
    var9 = func234((i32_load(var0 + 12) + 16), 0)
    var1 = i32_load(var3)
    if (1 if i32_load(var3) == 0 else 0):
        break
    if (1 if i32_load8_u(9142916) == 0 else 0):
        while True:  # loop $label1
            var2 = (var5 + (var4 * 60))
            if (1 if i32_load((var5 + (var4 * 60)) + 32) == 3 else 0):
                i32_store(var2 + 28, (i32_load(9140308) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2)))
                i32_store(9568052, (i32_load(9568052) + ((i32_load(var2) * (i32_load(var2 + 4) + 2)) << 2)))
                var1 = i32_load(9568048)
                i32_store(9568048, (i32_load(9568048) + 1))
                i32_store(((var1 << 2) + 9563952), var2)
                var1 = i32_load(var3)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < var1 else 0):
                continue
            break
            break  # end loop
        raise RuntimeError('unreachable')
    while True:  # loop $label2
        var2 = (var5 + (var4 * 60))
        if (1 if i32_load((var5 + (var4 * 60)) + 32) == 3 else 0):
            var1 = i32_load(59152)
            i32_store(59152, (i32_load(59152) + 1))
            i32_store(var2 + 28, var1)
            var1 = i32_load(var2)
            var7 = i32_load(var2 + 4)
            var6 = i32_load(9568048)
            i32_store(9568048, (i32_load(9568048) + 1))
            i32_store(((var6 << 2) + 9563952), var2)
            i32_store(9568052, (i32_load(9568052) + ((var1 * (var7 + 2)) << 2)))
            var1 = i32_load(var3)
        var4 = (var4 + 1)
        if (1 if (var4 + 1) < var1 else 0):
            continue
        break  # end loop
    var2 = i32_load(9140308)
    var4 = i32_load(9568052)
    var1 = (i32_load(59156) << 2)
    var3 = (i32_load(9568052) % (i32_load(59156) << 2))
    if (i32_load(9568052) % (i32_load(59156) << 2)):
        var4 = ((var4 - var3) + var1)
        i32_store(9568052, ((var4 - var3) + var1))
    i32_store(9140308, (((var4 & 0xFFFFFFFF) >> 2) + var2))
    var1 = func26(20)
    var3 = i32_load(9568048)
    i32_store(var1 + 8, var4)
    i32_store(var1 + 4, var2)
    i32_store(var1, var3)
    var4 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    i32_store(var1 + 16, var0)
    i32_store(var1 + 12, var4)
    if (1 if var3 == 0 else 0):
        break
    var0 = 0
    var4 = 0
    if (1 if var3 >= 4 else 0):
        var7 = (var3 & -4)
        var2 = 0
        while True:  # loop $label4
            var5 = (var4 << 2)
            i32_store(((var4 << 2) + i32_load(var1 + 12)), i32_load((var5 + 9563952)))
            var6 = (var5 | 4)
            i32_store(((var5 | 4) + i32_load(var1 + 12)), i32_load((var6 + 9563952)))
            var6 = (var5 | 8)
            i32_store(((var5 | 8) + i32_load(var1 + 12)), i32_load((var6 + 9563952)))
            var5 = (var5 | 12)
            i32_store(((var5 | 12) + i32_load(var1 + 12)), i32_load((var5 + 9563952)))
            var4 = (var4 + 4)
            var2 = (var2 + 4)
            if (1 if (var2 + 4) != var7 else 0):
                continue
            break  # end loop
    var2 = (var3 & 3)
    if (1 if (var3 & 3) == 0 else 0):
        break
    while True:  # loop $label5
        var3 = (var4 << 2)
        i32_store(((var4 << 2) + i32_load(var1 + 12)), i32_load((var3 + 9563952)))
        var4 = (var4 + 1)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var2 else 0):
            continue
        break  # end loop
    func186((var8 + 12), 0, 59, var1)
    i32_store(9568052, 0)
    i32_store(9568048, 0)
    var0 = i32_load(9671136)
    if (1 if i32_load(9671136) >= 4 else 0):
        var2 = i32_load(9671128)
        var4 = 3
        while True:  # loop $label11
            var3 = (var2 + (var4 * 132))
            var1 = i32_load8_u((var2 + (var4 * 132)) + 125)
            if (1 if i32_load8_u((var2 + (var4 * 132)) + 125) == 3 else 0):
                break
            if (1 if var9 != i32_load8_u(var3 + 122) else 0):
                break
            var5 = i32_load(var3 + 40)
            var0 = i32_load(9299880)
            if (1 if i32_load(9299880) != i32_load(9299876) else 0):
                var2 = i32_load(9299872)
                break
            var2 = (i32_load(9299884) + var0)
            i32_store(9299876, (i32_load(9299884) + var0))
            var1 = i32_load(9299872)
            var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
            if var0:
                # Unknown: memory.copy []
            if var1:
                var0 = i32_load(9299880)
            i32_store(9299872, var2)
            var1 = i32_load8_u(var3 + 125)
            i32_store(9299880, (var0 + 1))
            i32_store((var2 + (var0 << 2)), var5)
            i32_store(var3 + 40, 0)
            var0 = (var1 & 255)
            var2 = ((1 if (var1 & 255) != 4 else 0) & (1 if var0 != 14 else 0))
            # br_table ['$label8', '$label9', '$label9', '$label9', '$label9', '$label9', '$label9', '$label9', '$label9', '$label9', '$label8', '$label9']
            _br_idx = (var0 - 4)
            break  # br_table
            var0 = ((i32_load8_u(var3 + 122) * 404) + 9568096)
            var1 = i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 356)
            if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 356):
                break
            var1 = 9142636
            var5 = i32_load(var0 + 216)
            var0 = i32_load(var0 + 220)
            var0 = (i32_load(var0 + 216) if (1 if var0 < var5 else 0) else i32_load(var0 + 220))
            var0 = ((6 if (1 if var0 >= 6 else 0) else (i32_load(var0 + 216) if (1 if var0 < var5 else 0) else i32_load(var0 + 220))) - 1)
            if (1 if ((6 if (1 if var0 >= 6 else 0) else (i32_load(var0 + 216) if (1 if var0 < var5 else 0) else i32_load(var0 + 220))) - 1) >= 5 else 0):
                break
            var1 = i32_load(((var0 << 2) + 10132))
            break
            var1 = ((i32_load8_u(var3 + 122) * 72) + 9263856)
            var0 = i32_load(9671136)
            var2 = i32_load(9671128)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < var0 else 0):
                continue
            break  # end loop
    if (1 if i32_load(9671176) == 0 else 0):
        break
    if (1 if i32_load(i32_load(9671168)) != var9 else 0):
        break
    global global0
    global0 = (var8 + 16)


# ==========================================================
# $func834
# ==========================================================
def func834(var0, var1):
    var2 = 0
    var3 = 0
    i32_store8(9163793, var0)
    if (1 if var0 == 0 else 0):
        break
    if (1 if i32_load(9671176) == 0 else 0):
        break
    var1 = i32_load(38620)
    var2 = i32_load(38560)
    var0 = i32_load(i32_load(9671168))
    var2 = (i32_load(38620) if (1 if var0 == var2 else 0) else (i32_load(38560) if (1 if var0 == var1 else 0) else i32_load(i32_load(9671168))))
    var1 = ((i32_load(38620) if (1 if var0 == var2 else 0) else (i32_load(38560) if (1 if var0 == var1 else 0) else i32_load(i32_load(9671168)))) + 1)
    var1 = i32_load(38604)
    var1 = (((i32_load(38620) if (1 if var0 == var2 else 0) else (i32_load(38560) if (1 if var0 == var1 else 0) else i32_load(i32_load(9671168)))) + 1) if (1 if var0 == var1 else 0) else (var1 if (1 if var0 == i32_load(38608) else 0) else (var1 if (1 if var0 == i32_load(38612) else 0) else (i32_load(38604) if (1 if var0 == i32_load(38616) else 0) else var2))))
    var2 = i32_load(38624)
    if (1 if i32_load(38624) != var0 else 0):
        if (1 if var0 != i32_load(38628) else 0):
            break
    break
    var3 = i32_load(39056)
    if (1 if var0 == i32_load(38632) else 0):
        break
    var3 = (var2 if (1 if var0 == var3 else 0) else var1)
    if (1 if (var1 + 1) == (var2 if (1 if var0 == var3 else 0) else var1) else 0):
        break
    if i32_load(9671192):
        var0 = 0
        while True:  # loop $label3
            func38(i32_load((i32_load(9671184) + (var0 << 2))))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < i32_load(9671192) else 0):
                continue
            break  # end loop
    var0 = 0
    i32_store(9671192, 0)
    i32_store(9671176, 0)
    i32_store8(9142412, 0)
    if i32_load8_u(9684396):
        i32_store8(9684396, 0)
        a_b()
        var0 = i32_load(9671176)
    var1 = i32_load(9671172)
    if (1 if i32_load(9671172) > (var0 + 3) else 0):
        var1 = i32_load(9671168)
        break
    var1 = ((var1 + i32_load(9671180)) + 3)
    i32_store(9671172, ((var1 + i32_load(9671180)) + 3))
    var2 = i32_load(9671168)
    var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var0:
        # Unknown: memory.copy []
    if var2:
        var0 = i32_load(9671176)
    i32_store(9671168, var1)
    i32_store(9671176, (var0 + 1))
    i32_store((var1 + (var0 << 2)), var3)
    var0 = i32_load(9671176)
    i32_store(9671176, (i32_load(9671176) + 1))
    i32_store((var1 + (var0 << 2)), 0)
    var0 = i32_load(9671176)
    i32_store(9671176, (i32_load(9671176) + 1))
    i32_store((var1 + (var0 << 2)), 0)
    if (1 if i32_load8_u(9147152) == 0 else 0):
        break
    i32_store8(9142412, 1)
    return func132(2147483647, 2147483647)


# ==========================================================
# $func29
# ==========================================================
def func29(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    if (1 if i32_load8_u(var0 + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var0 + 129) == 5 else 0):
        if func200(var0, 0, 0, 1):
            break
    var3 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        break
    if (1 if i32_load(var3 + 8) < 3 else 0):
        break
    var5 = i32_load(var3)
    var7 = i32_load(i32_load(var3))
    if (1 if (i32_load(i32_load(var3)) - 1) > 1 else 0):
        break
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) == 1 else 0):
        break
    var2 = i32_load(var5 + 4)
    var6 = (var5 + (i32_load(var5 + 4) << 2))
    var4 = i32_load(var0 + 32)
    if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 0 else 0):
        if var4:
            break
        if (1 if i32_load(var6) != i32_load16_u(var0 + 116) else 0):
            break
        if (1 if i32_load(var6 + 4) == i32_load16_u(var0 + 118) else 0):
            break
        break
    if (1 if var4 == 0 else 0):
        break
    break
    if (1 if var4 == i32_load(var6 + 8) else 0):
        break
    if (1 if var4 != i32_load(var6 + 8) else 0):
        break
    var2 = (var2 + 7)
    i32_store(var5 + 4, (var2 + 7))
    var8 = 1
    if (1 if var7 != 2 else 0):
        break
    if (1 if var2 < i32_load(var3 + 8) else 0):
        break
    var2 = 2
    i32_store(var5 + 4, 2)
    if (1 if i32_load(var3 + 8) <= var2 else 0):
        i32_store(var3 + 8, 0)
        break
    i32_store8(var0 + 125, 0)
    var4 = i32_load(9671128)
    var2 = (var5 + (var2 << 2))
    var3 = i32_load((var5 + (var2 << 2)) + 8)
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load((var5 + (var2 << 2)) + 8) * 132)) + 125) == 3 else 0):
        if (1 if i32_load(var2 + 12) != 69 else 0):
            break
        var3 = func236((var4 + (i32_load(var0 + 28) * 132)), (var4 + (var3 * 132)))
        if (1 if func236((var4 + (i32_load(var0 + 28) * 132)), (var4 + (var3 * 132))) == 0 else 0):
            break
        i32_store(var2 + 8, var3)
        if (1 if i32_load8_u((var4 + (var3 * 132)) + 125) == 3 else 0):
            break
    var5 = (5 if i32_load(var2 + 20) else 0)
    var4 = i32_load(var2 + 16)
    var7 = i32_load(var2 + 4)
    var9 = i32_load(var2)
    var10 = i32_load(var2 + 12)
    var2 = 250
    if (1 if var8 == 0 else 0):
        break
    if (1 if i32_load(var6) != i32_load16_u(var0 + 112) else 0):
        break
    var2 = (250 if (1 if i32_load(var6 + 4) != i32_load16_u(var0 + 114) else 0) else 0)
    if (1 if func30(func86(var0), var0, var3, var10, var9, var7, var4, var5, var2, 0) == 0 else 0):
        break
    if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4))) > i32_load(9142848) else 0):
        break
    i32_store8(var0 + 125, 0)
    i32_store8(var0 + 123, 0)
    if (1 if var1 == 0 else 0):
        break
    var1 = i32_load(var0 + 48)
    if (1 if i32_load(var0 + 48) == 0 else 0):
        break
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 72) + 9263856)) == var1 else 0):
        if i32_load(var1 + 32):
            break
    if i32_load8_u(9147152):
        break
    func156(func86(var0), var0, 500)


# ==========================================================
# $func182
# ==========================================================
def func182():
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var0 = 3
    if (1 if i32_load(9671136) > 3 else 0):
        while True:  # loop $label0
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < i32_load(9671136) else 0):
                continue
            break  # end loop
    var6 = i32_load(9142892)
    if (1 if i32_load(9142892) == 0 else 0):
        break
    var4 = i32_load(9561692)
    while True:  # loop $label2
        var0 = 0
        while True:  # loop $label3
            var2 = (var4 + (var5 * 286704))
            var3 = ((var4 + (var5 * 286704)) + (var0 << 2))
            var1 = i32_load((((var4 + (var5 * 286704)) + (var0 << 2)) + 285656))
            if i32_load((((var4 + (var5 * 286704)) + (var0 << 2)) + 285656)):
                i32_store(var1 + 8, 0)
            var1 = i32_load((var3 + 284636))
            if i32_load((var3 + 284636)):
                i32_store(var1 + 8, 0)
            var1 = (var0 | 1)
            if (1 if (var0 | 1) == 255 else 0):
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var6 else 0):
                    continue
                break
            var3 = (var2 + (var1 << 2))
            var1 = i32_load(((var2 + (var1 << 2)) + 285656))
            if i32_load(((var2 + (var1 << 2)) + 285656)):
                i32_store(var1 + 8, 0)
            var1 = i32_load((var3 + 284636))
            if i32_load((var3 + 284636)):
                i32_store(var1 + 8, 0)
            var0 = (var0 + 2)
            continue
            break  # end loop
        raise RuntimeError('unreachable')
        break  # end loop
    raise RuntimeError('unreachable')
    var4 = i32_load(9671128)
    if i32_load(9671128):
        var3 = (var4 - 4)
        var1 = i32_load((var4 - 4))
        if i32_load((var4 - 4)):
            var0 = (var4 + (var1 * 132))
            while True:  # loop $label4
                var1 = (var0 - 132)
                var2 = i32_load((var0 - 132))
                if i32_load((var0 - 132)):
                    i32_store((var0 - 128), var2)
                var0 = var1
                if (1 if var1 != var4 else 0):
                    continue
                break  # end loop
        i32_store(9671128, 0)
    i32_store(9671132, 10000)
    var1 = func26(1320004)
    i32_store(func26(1320004), 10000)
    var3 = (var1 + 1320004)
    var1 = (var1 + 4)
    var0 = (var1 + 4)
    while True:  # loop $label5
        # Unknown: memory.fill []
        var2 = func26(4)
        i32_store(var0 + 4, func26(4))
        i32_store(var0, var2)
        i32_store(var0 + 8, (var2 + 4))
        var0 = (var0 + 132)
        if (1 if (var0 + 132) != var3 else 0):
            continue
        break  # end loop
    i32_store(9671128, var1)
    i64_store(9671136, 42949672960003)
    i32_store(9163776, 4)
    i32_store(9684796, 0)
    i32_store(i32_load(9681936) + 8, 0)
    i32_store(9299880, 0)

