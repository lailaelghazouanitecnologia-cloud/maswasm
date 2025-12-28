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
# $func230
# ==========================================================
def func230(var0):
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
    var4 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var6 = (i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704))
    var1 = i32_load(var0 + 20)
    while True:  # loop $label8
        var2 = i32_load(i32_load(var1))
        if (1 if i32_load(i32_load(var1)) < 2147483647 else 0):
            break
        var2 = ((var2 - 2147483647) if (1 if var2 > 2147483646 else 0) else var2)
        var1 = i32_load(((var6 + (((var2 - 2147483647) if (1 if var2 > 2147483646 else 0) else var2) * 36)) + 269376))
        var3 = (i32_load(((var6 + (((var2 - 2147483647) if (1 if var2 > 2147483646 else 0) else var2) * 36)) + 269376)) if var1 else 100)
        var1 = ((var2 * 404) + 9568096)
        i32_store(var4, (((i32_load(((var6 + (((var2 - 2147483647) if (1 if var2 > 2147483646 else 0) else var2) * 36)) + 269376)) if var1 else 100) * i32_load(((var2 * 404) + 9568096) + 68)) // 100))
        i32_store(var4 + 4, ((i32_load(var1 + 72) * var3) // 100))
        i32_store(var4 + 8, ((i32_load(var1 + 76) * var3) // 100))
        i32_store(var4 + 12, ((i32_load(var1 + 80) * var3) // 100))
        var7 = i32_load(var1 + 180)
        if (1 if i32_load8_u(i32_load(var1 + 180) + 23) == 0 else 0):
            break
        var1 = i32_load(var7 + 4)
        if (1 if i32_load(((i32_load(var7 + 4) * 404) + 9568096) + 264) != 3 else 0):
            break
        if i32_load(((var6 + (var1 << 2)) + 281808)):
            break
        var12 = i32_load(var7 + 68)
        if i32_load(var7 + 68):
            var3 = 0
            var5 = 1
            var1 = 0
            var8 = 0
            while True:  # loop $label5
                var9 = i32_load((var7 + (var3 << 2)) + 28)
                var10 = i32_load(((i32_load((var7 + (var3 << 2)) + 28) * 404) + 9568096) + 264)
                var11 = (1 if i32_load(((i32_load((var7 + (var3 << 2)) + 28) * 404) + 9568096) + 264) == 1 else 0)
                var9 = i32_load(((var6 + (var9 << 2)) + 281808))
                if (1 if i32_load(((var6 + (var9 << 2)) + 281808)) == 1 else 0):
                    break
                var5 = ((1 if var10 != 3 else 0) & var5)
                if var9:
                    break
                var5 = ((1 if var10 != 0 else 0) & var5)
                break
                var8 = (var8 | var11)
                var1 = (var1 | var11)
                var3 = (var3 + 1)
                if (1 if (var3 + 1) != var12 else 0):
                    continue
                break  # end loop
            if (1 if (((var5 & var8) if (var1 & 1) else var5) & 1) == 0 else 0):
                break
        if (1 if func66(var6, var4, 0, 1) == 0 else 0):
            break
        func181(var6, i32_load(var0 + 28), var2)
        var1 = i32_load(var0 + 20)
        var2 = (i32_load(var1 + 8) - 1)
        i32_store(i32_load(var0 + 20) + 8, (i32_load(var1 + 8) - 1))
        if var2:
            var2 = i32_load(var1)
            var3 = 0
            while True:  # loop $label7
                var3 = (var3 + 1)
                i32_store((var2 + (var3 << 2)), i32_load((var2 + ((var3 + 1) << 2))))
                if (1 if var3 < i32_load(var1 + 8) else 0):
                    continue
                break  # end loop
        if i32_load(var1 + 8):
            continue
        break
        break  # end loop
    if (1 if var2 != -1 else 0):
        break
    var1 = i32_load(var0 + 44)
    if i32_load(var0 + 44):
        i32_store((i32_load(9215884) + (var1 << 4)), 0)
    i32_store(var0 + 44, 0)
    func29(var0, 1)
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    var1 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
            break
    break
    var1 = ((var2 * 404) + 9568096)
    var1 = ((i32_load(((var2 * 404) + 9568096) + 116) * i32_load((i32_load(9142424) + (132 if i32_load(var1 + 264) else 128)))) * 1000)
    var2 = (1 if ((i32_load(((var2 * 404) + 9568096) + 116) * i32_load((i32_load(9142424) + (132 if i32_load(var1 + 264) else 128)))) * 1000) < 100 else 0)
    var1 = ((var1 & 0xFFFFFFFF) // 100)
    if (1 if i32_load(9142872) != i32_load16_u(var0 + 110) else 0):
        break
    var3 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 180)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 180) == 0 else 0):
        break
    var1 = (25 if var2 else var1)
    var2 = i32_load(var0 + 44)
    if i32_load(var0 + 44):
        i32_store((i32_load(9215884) + (var2 << 4)), (i32_load(9142848) + ((var1 & 0xFFFFFFFF) // 25)))
        break
    func63(func53(i32_load(var3 + 12)), var0, 2, 0, var1)
    global global0
    global0 = (var4 + 16)


# ==========================================================
# $func285
# ==========================================================
def func285(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var7 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var8 = i32_load(9561692)
    var6 = i32_load16_u(var0 + 110)
    var3 = i32_load8_u(var0 + 122)
    if (1 if i32_load8_u(var0 + 122) == i32_load(38608) else 0):
        break
    if (1 if var3 == i32_load(38612) else 0):
        break
    var2 = (i32_load(39056) if (1 if i32_load(38616) == var3 else 0) else var1)
    var4 = (i32_load(38632) + ((i32_load(39056) if (1 if i32_load(38616) == var3 else 0) else var1) * 36))
    var5 = ((var1 * 404) + 9568096)
    var9 = (i32_load(((i32_load(38632) + ((i32_load(39056) if (1 if i32_load(38616) == var3 else 0) else var1) * 36)) + 269380)) + i32_load(((var1 * 404) + 9568096) + 92))
    i32_store(i32_load(38628) + 52, (i32_load(((i32_load(38632) + ((i32_load(39056) if (1 if i32_load(38616) == var3 else 0) else var1) * 36)) + 269380)) + i32_load(((var1 * 404) + 9568096) + 92)))
    var10 = (i32_load((var4 + 269384)) + i32_load(var5 + 100))
    i32_store(var0 + 60, (i32_load((var4 + 269384)) + i32_load(var5 + 100)))
    if i32_load8_u(((var3 * 404) + 9568096) + 334):
        var3 = i32_load(var0 + 84)
        i32_store(var0 + 52, (i32_load(var0 + 84) + var9))
        i32_store(var0 + 60, ((((var3 + 1) & 0xFFFFFFFF) >> 1) + var10))
    i32_store(var0 + 64, ((((i32_load((var4 + 269388)) + i32_load(var5 + 104)) * (((i32_load(var0 + 64) * 100) & 0xFFFFFFFF) // i32_load(var0 + 68))) & 0xFFFFFFFF) // 100))
    i32_store(var0 + 68, (i32_load((var4 + 269392)) + i32_load(var5 + 108)))
    var3 = i32_load(var5 + 120)
    if (1 if i32_load(var5 + 120) > i32_load(var0 + 76) else 0):
        if (1 if i32_load(var0 + 72) == 0 else 0):
            var3 = i32_load(var5 + 120)
        i32_store(var0 + 76, var3)
        i32_store(var0 + 72, var3)
    var3 = ((var8 + (var6 * 286704)) + 281808)
    var5 = i32_load8_u(var0 + 122)
    var4 = (((var8 + (var6 * 286704)) + 281808) + (i32_load8_u(var0 + 122) << 2))
    i32_store((((var8 + (var6 * 286704)) + 281808) + (i32_load8_u(var0 + 122) << 2)), (i32_load(var4) - 1))
    i32_store8(var0 + 122, var2)
    var2 = (var3 + ((var2 & 255) << 2))
    i32_store((var3 + ((var2 & 255) << 2)), (i32_load(var2) + 1))
    var3 = i32_load8_u(var0 + 122)
    var2 = i32_load(((i32_load8_u(var0 + 122) * 72) + 9263856))
    if (1 if var3 == i32_load(38600) else 0):
        func277(i32_load16_u(var0 + 112), i32_load16_u(var0 + 114), i32_load16_u(var0 + 110))
        if (1 if i32_load8_u(9147329) == 0 else 0):
            break
        if (1 if i32_load8_u(9147334) == 0 else 0):
            break
        var2 = i32_load(9142464)
        i32_store8(var0 + 124, (i32_load16_u(var0 + 114) % 5))
        break
        if (1 if i32_load8_u(9147331) == 0 else 0):
            break
        if (1 if i32_load8_u(9147332) == 0 else 0):
            break
        var2 = i32_load(9142468)
        i32_store8(var0 + 124, (i32_load16_u(var0 + 112) % 7))
        break
        i32_store8(var0 + 124, 0)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) == 0 else 0):
        if i32_load16_u(var0 + 108):
            i32_store(var0 + 88, 0)
            i32_store16(var0 + 108, 0)
        if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 0 else 0):
            i32_store8(var0 + 123, 0)
            i32_store(var0 + 32, 0)
            i32_store(var0 + 116, i32_load(var0 + 112))
            break
        func29(var0, 1)
        break
    if (1 if i32_load8_u(var0 + 129) == 8 else 0):
    var3 = (var6 * 286704)
    func144(((var6 * 286704) + var8), i32_load(var0 + 28), 1)
    var2 = i32_load((((var3 + var8) + (var5 << 2)) + 284636))
    if (1 if i32_load((((var3 + var8) + (var5 << 2)) + 284636)) == 0 else 0):
        break
    var3 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) == 0 else 0):
        break
    var4 = i32_load(var0 + 28)
    var9 = i32_load(var2)
    var2 = 0
    while True:  # loop $label6
        var10 = (var9 + (var2 << 2))
        if (1 if var4 != i32_load((var9 + (var2 << 2))) else 0):
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var3 else 0):
                continue
            break
        break  # end loop
    if (1 if var2 < 0 else 0):
        break
    i32_store(var10, 0)
    if (1 if i32_load8_u(9142916) == 0 else 0):
        break
    var2 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    var3 = i32_load8_u(var0 + 122)
    var4 = i32_load16_u(var0 + 110)
    i32_store(var7 + 4, var2)
    i32_store(var7, (var3 | (var4 << 16)))
    a_b()
    var2 = (var8 + (var6 * 286704))
    var6 = (i32_load(((var1 * 404) + 9568096) + 280) - i32_load(((var5 * 404) + 9568096) + 280))
    var1 = ((i32_load(((var1 * 404) + 9568096) + 280) - i32_load(((var5 * 404) + 9568096) + 280)) + i32_load(var2 + 283976))
    i32_store((var8 + (var6 * 286704)) + 283976, ((i32_load(((var1 * 404) + 9568096) + 280) - i32_load(((var5 * 404) + 9568096) + 280)) + i32_load(var2 + 283976)))
    if (1 if var6 < 0 else 0):
        i32_store8(var2 + 286700, 1)
    var2 = (var2 + 281748)
    if (1 if var1 > i32_load((var2 + 281748)) else 0):
        i32_store(var2, var1)
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    var1 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
            break
    global global0
    global0 = (var7 + 16)
    return func28((1 if var1 != 0 else 0), 1)


# ==========================================================
# $func290
# ==========================================================
def func290(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    if i32_load16_u(var0 + 120):
        func119(0  # stack underflow, var0, 0, 1)
        var2 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
        if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 216):
            var5 = i32_load(9142840)
            var6 = i32_load16_u(var0 + 114)
            var7 = i32_load16_u(var0 + 112)
            while True:  # loop $label1
                var4 = (var4 + 1)
                var8 = ((var4 + 1) + var7)
                var1 = 0
                while True:  # loop $label0
                    var1 = (var1 + 1)
                    var3 = (i32_load(9142440) + 2)
                    i32_store((var5 + ((var8 + ((((var1 + 1) + var6) + ((i32_load(9142440) + 2) * i32_load(var2 + 208))) * var3)) << 2)), i32_load(var2 + 212))
                    var3 = i32_load(var2 + 216)
                    if (1 if var1 < i32_load(var2 + 216) else 0):
                        continue
                    break  # end loop
                if (1 if var3 > var4 else 0):
                    continue
                break  # end loop
        var1 = i32_load(38428)
        i32_store8(var0 + 122, i32_load(38428))
        if i32_load16_u(var0 + 108):
            i32_store(var0 + 88, 0)
            i32_store16(var0 + 108, 0)
        var4 = (((var1 & 255) * 404) + 9568096)
        if i32_load((((var1 & 255) * 404) + 9568096) + 216):
            var5 = i32_load(9142840)
            var6 = i32_load16_u(var0 + 114)
            var7 = i32_load16_u(var0 + 112)
            var2 = 0
            while True:  # loop $label3
                var2 = (var2 + 1)
                var8 = ((var2 + 1) + var7)
                var1 = 0
                while True:  # loop $label2
                    var1 = (var1 + 1)
                    var3 = (i32_load(9142440) + 2)
                    i32_store((var5 + ((var8 + ((((var1 + 1) + var6) + ((i32_load(9142440) + 2) * i32_load(var4 + 208))) * var3)) << 2)), i32_load(var0 + 28))
                    var3 = i32_load(var4 + 216)
                    if (1 if var1 < i32_load(var4 + 216) else 0):
                        continue
                    break  # end loop
                if (1 if var2 < var3 else 0):
                    continue
                break  # end loop
        i32_store(i32_load(var0 + 24), 0)
        i32_store16(var0 + 120, 0)
        i32_store(9143000, 0)
        if (1 if i32_load(var0 + 92) == 0 else 0):
            break
        var1 = i32_load8_u(9147141)
        if i32_load(9140316):
            if (1 if i32_load(9140320) != i32_load(var0 + 28) else 0):
                break
        func29(var0, 1)


# ==========================================================
# $func296
# ==========================================================
def func296(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var3 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    i32_store8(var0 + 128, var1)
    var1 = i32_load16_u(var0 + 112)
    var2 = ((i32_load16_u(var0 + 112) << 5) - i32_load(9142952))
    var2 = i32_load16_u(var0 + 114)
    var4 = ((i32_load16_u(var0 + 114) << 5) - i32_load(9142956))
    if (1 if (((((i32_load16_u(var0 + 112) << 5) - i32_load(9142952)) * var2) + (((i32_load16_u(var0 + 114) << 5) - i32_load(9142956)) * var4)) - 1) > 9000000 else 0):
        break
    var5 = i32_load(39860)
    var6 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var4 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var2) + var1) << 1)))
    if (1 if var6 == 2 else 0):
        if (1 if var4 > 1 else 0):
            break
        break
    if (1 if var4 == 0 else 0):
        break
    i32_store(var3 + 40, var2)
    i32_store(var3 + 36, var1)
    i32_store(var3 + 32, var5)
    a_b()
    var4 = i32_load8_u(9142916)
    var1 = (8 if i32_load8_u((i32_load(9143004) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var0 + 110))))) else (11 if i32_load8_u(9142916) else 3))
    i32_store8(var0 + 127, (8 if i32_load8_u((i32_load(9143004) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var0 + 110))))) else (11 if i32_load8_u(9142916) else 3)))
    var2 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    if var4:
        i32_store(var3 + 20, var2)
        var1 = (var1 << 4)
        i32_store(var3 + 16, ((((i32_load(((var1 << 4) + 1748)) << 8) + i32_load((var1 + 1744))) + (i32_load((var1 + 1752)) << 16)) + (i32_load((var1 + 1756)) << 24)))
        a_b()
        break
    i32_store(var3 + 4, var2)
    i32_store(var3, var1)
    a_b()
    i32_store8(var0 + 129, 0)
    var1 = i32_load(9215884)
    var2 = i32_load(var0 + 44)
    if (1 if i32_load(var0 + 44) == 0 else 0):
        var2 = 1
        break
    var2 = ((var2 << 2) | 1)
    if i32_load((var1 + (((var2 << 2) | 1) << 2))):
        break
    if (1 if i32_load8_u(var0 + 123) != 6 else 0):
        break
    i32_store8(var0 + 123, 0)
    i32_store(var0 + 32, 0)
    i32_store(var0 + 116, i32_load(var0 + 112))
    if (1 if i32_load((var1 + (var2 << 2))) == 6 else 0):
        func29(var0, 1)
    global global0
    global0 = (var3 + 48)

