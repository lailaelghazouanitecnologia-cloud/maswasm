"""
Auto-generated from WAT. Contains 1 functions.
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
# $func32
# ==========================================================
def func32(var0, var1, param2):
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
    var13 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if i32_load8_u(var0 + 125) == 3 else 0):
        break
    var10 = i32_load8_u(var0 + 122)
    var14 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var8 = i32_load16_u(var0 + 110)
    var9 = i32_load(9561692)
    var4 = i32_load(((var10 * 72) + 9263856) + 28)
    if var1:
        break
    var5 = i32_load8_u(9147152)
    if i32_load8_u(9147152):
        break
    if (1 if i32_load8_u(9147211) == 0 else 0):
        break
    var6 = ((var10 * 404) + 9568096)
    var7 = i32_load(((var10 * 404) + 9568096) + 40)
    if (1 if i32_load(((var10 * 404) + 9568096) + 40) == 0 else 0):
        break
    var2 = i32_load16_u(var0 + 112)
    var3 = ((i32_load16_u(var0 + 112) << 5) - i32_load(9142952))
    var3 = i32_load16_u(var0 + 114)
    var11 = ((i32_load16_u(var0 + 114) << 5) - i32_load(9142956))
    if (1 if (((((i32_load16_u(var0 + 112) << 5) - i32_load(9142952)) * var3) + (((i32_load16_u(var0 + 114) << 5) - i32_load(9142956)) * var11)) - 1) > 9000000 else 0):
        break
    var6 = i32_load(var6 + 36)
    var11 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if var5:
        break
    var5 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var3) + var2) << 1)))
    if (1 if var11 == 2 else 0):
        if (1 if var5 > 1 else 0):
            break
        break
    if (1 if var5 == 0 else 0):
        break
    i32_store(var13, i32_load((var6 + (((i32_load(9142848) + var2) % var7) << 2))))
    i32_store(var13 + 4, var2)
    i32_store(var13 + 8, var3)
    a_b()
    var15 = i32_load8_u(var0 + 124)
    if (1 if i32_load(var14 + 264) != 1 else 0):
        break
    var2 = ((var10 * 404) + 9568096)
    var3 = i32_load(((var10 * 404) + 9568096) + 360)
    if i32_load(((var10 * 404) + 9568096) + 360):
        var4 = i32_load(var3)
        break
    var3 = i32_load(var2 + 216)
    var2 = i32_load(var2 + 220)
    var2 = (i32_load(var2 + 216) if (1 if var2 < var3 else 0) else i32_load(var2 + 220))
    # br_table ['$label4', '$label5', '$label6', '$label7', '$label8', '$label9']
    _br_idx = ((6 if (1 if var2 >= 6 else 0) else (i32_load(var2 + 216) if (1 if var2 < var3 else 0) else i32_load(var2 + 220))) - 1)
    break  # br_table
    break
    break
    break
    break
    break
    var4 = (i32_load(9142632) if (1 if var2 > 5 else 0) else var4)
    i32_store8(var0 + 124, 0)
    if i32_load8_u(9147152):
        func77(var0)
        i32_store(var0 + 28, 0)
    if (1 if i32_load8_u(9147213) == 0 else 0):
        break
    if (1 if var1 == 0 else 0):
        if (1 if i32_load8_u(9147152) == 0 else 0):
            break
    var2 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    func38(var2)
    break
    if (1 if i32_load(38448) == i32_load8_u(var0 + 122) else 0):
        i32_store8(var0 + 124, (i32_load(var0 + 28) % 3))
        break
    if var4:
        i32_store8(var0 + 124, 0)
        func92(var0, 0.0, 0.0)
        if (1 if i32_load(var4 + 24) == 0 else 0):
            break
        var2 = i32_load(var0 + 40)
        if (1 if i32_load(var0 + 40) == 0 else 0):
            break
        func254(var4, var2)
        break
    var2 = i32_load(var0 + 40)
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    func38(var2)
    var11 = i32_load(var0 + 36)
    if i32_load(var0 + 36):
    var2 = i32_load(((i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) * 40) + 9671200) + 32)
    if i32_load(((i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) * 40) + 9671200) + 32):
        # call_indirect via table[var2]
    if i32_load(9147132):
        var6 = i32_load(var0 + 28)
        var7 = i32_load(9671128)
        var3 = i32_load(9215904)
        if (1 if i32_load(9215904) == 0 else 0):
            break
        var5 = i32_load(var3 + 8)
        if (1 if i32_load(var3 + 8) == 0 else 0):
            break
        var4 = i32_load(var3)
        var2 = 0
        while True:  # loop $label15
            if (1 if i32_load((var7 + (i32_load((var4 + (var2 << 2))) * 132)) + 28) == var6 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var3 = i32_load(9215908)
        if (1 if i32_load(9215908) == 0 else 0):
            break
        var5 = i32_load(var3 + 8)
        if (1 if i32_load(var3 + 8) == 0 else 0):
            break
        var4 = i32_load(var3)
        var2 = 0
        while True:  # loop $label17
            if (1 if i32_load((var7 + (i32_load((var4 + (var2 << 2))) * 132)) + 28) == var6 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var3 = i32_load(9215912)
        if (1 if i32_load(9215912) == 0 else 0):
            break
        var5 = i32_load(var3 + 8)
        if (1 if i32_load(var3 + 8) == 0 else 0):
            break
        var4 = i32_load(var3)
        var2 = 0
        while True:  # loop $label19
            if (1 if i32_load((var7 + (i32_load((var4 + (var2 << 2))) * 132)) + 28) == var6 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var3 = i32_load(9215916)
        if (1 if i32_load(9215916) == 0 else 0):
            break
        var5 = i32_load(var3 + 8)
        if (1 if i32_load(var3 + 8) == 0 else 0):
            break
        var4 = i32_load(var3)
        var2 = 0
        while True:  # loop $label21
            if (1 if i32_load((var7 + (i32_load((var4 + (var2 << 2))) * 132)) + 28) == var6 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var3 = i32_load(9215920)
        if (1 if i32_load(9215920) == 0 else 0):
            break
        var5 = i32_load(var3 + 8)
        if (1 if i32_load(var3 + 8) == 0 else 0):
            break
        var4 = i32_load(var3)
        var2 = 0
        while True:  # loop $label23
            if (1 if i32_load((var7 + (i32_load((var4 + (var2 << 2))) * 132)) + 28) == var6 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var3 = i32_load(9215924)
        if (1 if i32_load(9215924) == 0 else 0):
            break
        var5 = i32_load(var3 + 8)
        if (1 if i32_load(var3 + 8) == 0 else 0):
            break
        var4 = i32_load(var3)
        var2 = 0
        while True:  # loop $label25
            if (1 if i32_load((var7 + (i32_load((var4 + (var2 << 2))) * 132)) + 28) == var6 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var3 = i32_load(9215928)
        if (1 if i32_load(9215928) == 0 else 0):
            break
        var5 = i32_load(var3 + 8)
        if (1 if i32_load(var3 + 8) == 0 else 0):
            break
        var4 = i32_load(var3)
        var2 = 0
        while True:  # loop $label27
            if (1 if i32_load((var7 + (i32_load((var4 + (var2 << 2))) * 132)) + 28) == var6 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var3 = i32_load(9215932)
        if (1 if i32_load(9215932) == 0 else 0):
            break
        var5 = i32_load(var3 + 8)
        if (1 if i32_load(var3 + 8) == 0 else 0):
            break
        var4 = i32_load(var3)
        var2 = 0
        while True:  # loop $label29
            if (1 if i32_load((var7 + (i32_load((var4 + (var2 << 2))) * 132)) + 28) == var6 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var3 = i32_load(9215936)
        if (1 if i32_load(9215936) == 0 else 0):
            break
        var5 = i32_load(var3 + 8)
        if (1 if i32_load(var3 + 8) == 0 else 0):
            break
        var4 = i32_load(var3)
        var2 = 0
        while True:  # loop $label31
            if (1 if i32_load((var7 + (i32_load((var4 + (var2 << 2))) * 132)) + 28) == var6 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        var3 = i32_load(9215940)
        if (1 if i32_load(9215940) == 0 else 0):
            break
        var5 = i32_load(var3 + 8)
        if (1 if i32_load(var3 + 8) == 0 else 0):
            break
        var4 = i32_load(var3)
        var2 = 0
        while True:  # loop $label33
            if (1 if i32_load((var7 + (i32_load((var4 + (var2 << 2))) * 132)) + 28) == var6 else 0):
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
        break
        var5 = (var5 - 1)
        i32_store(var3 + 8, (var5 - 1))
        if (1 if var2 >= var5 else 0):
            break
        while True:  # loop $label34
            var2 = (var2 + 1)
            i32_store((var4 + (var2 << 2)), i32_load((var4 + ((var2 + 1) << 2))))
            if (1 if var2 < i32_load(var3 + 8) else 0):
                continue
            break  # end loop
    if (1 if i32_load8_u(9147213) == 0 else 0):
        break
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    var3 = i32_load(var0 + 12)
    if (1 if i32_load(var0 + 12) == 0 else 0):
        break
    if i32_load(var3 + 8):
        var4 = 0
        while True:  # loop $label36
            func38(i32_load((i32_load(var3) + (var4 << 2))))
            var4 = (var4 + 2)
            var3 = i32_load(var0 + 12)
            if (1 if (var4 + 2) < i32_load(i32_load(var0 + 12) + 8) else 0):
                continue
            break  # end loop
    i32_store(var3 + 8, 0)
    var12 = i32_load8_u(var0 + 125)
    if (1 if i32_load8_u(var0 + 125) != 4 else 0):
        break
    var2 = i32_load8_u(var0 + 122)
    if (1 if i32_load8_u(var0 + 122) == i32_load(38600) else 0):
        break
    if (1 if i32_load(38472) == var2 else 0):
        break
    if i32_load8_u(9216060):
        break
    var2 = ((var10 * 404) + 9568164)
    var3 = (var9 + (var8 * 286704))
    var4 = i32_load((var9 + (var8 * 286704)) + 283848)
    if (1 if i32_load((var9 + (var8 * 286704)) + 283848) != 2147483647 else 0):
        i32_store((var3 + 283848), (i32_load(var2) + var4))
    var3 = (var3 + 283852)
    var4 = i32_load((var3 + 283852))
    if (1 if i32_load((var3 + 283852)) != 2147483647 else 0):
        i32_store(var3, (i32_load(var2 + 4) + var4))
    var3 = (var9 + (var8 * 286704))
    var4 = ((var9 + (var8 * 286704)) + 283856)
    var5 = i32_load(((var9 + (var8 * 286704)) + 283856))
    if (1 if i32_load(((var9 + (var8 * 286704)) + 283856)) != 2147483647 else 0):
        i32_store(var4, (i32_load(var2 + 8) + var5))
    var3 = (var3 + 283860)
    var4 = i32_load((var3 + 283860))
    if (1 if i32_load((var3 + 283860)) != 2147483647 else 0):
        i32_store(var3, (i32_load(var2 + 12) + var4))
    var3 = (var9 + (var8 * 286704))
    var4 = ((var9 + (var8 * 286704)) + 281692)
    i32_store(((var9 + (var8 * 286704)) + 281692), (i32_load(var4) - i32_load(var2)))
    var4 = (var3 + 281696)
    i32_store((var3 + 281696), (i32_load(var4) - i32_load(var2 + 4)))
    var4 = (var3 + 281700)
    i32_store((var3 + 281700), (i32_load(var4) - i32_load(var2 + 8)))
    var2 = i32_load(var2 + 12)
    var4 = 1
    i32_store8(var3 + 286701, 1)
    var5 = (var3 + 281704)
    i32_store((var3 + 281704), (i32_load(var5) - var2))
    var2 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var5 = (var2 - 1)
    var16 = ((var2 - 1) & 1)
    var3 = (i32_load(var3 + 283908) * var2)
    var6 = i32_load(9561692)
    var7 = i32_load(9143016)
    if (1 if var2 != 2 else 0):
        var2 = (var5 & -2)
        var5 = 0
        while True:  # loop $label38
            if i32_load8_u((var7 + (var3 + var4))):
                i32_store8((var6 + (var4 * 286704)) + 286701, 1)
            var17 = (var4 + 1)
            if i32_load8_u((var7 + ((var4 + 1) + var3))):
                i32_store8((var6 + (var17 * 286704)) + 286701, 1)
            var4 = (var4 + 2)
            var5 = (var5 + 2)
            if (1 if (var5 + 2) != var2 else 0):
                continue
            break  # end loop
    if (1 if var16 == 0 else 0):
        break
    if (1 if i32_load8_u((var7 + (var3 + var4))) == 0 else 0):
        break
    i32_store8((var6 + (var4 * 286704)) + 286701, 1)
    if (1 if var11 == 0 else 0):
    func202(var0, 0, 1)
    if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 34 else 0):
        var2 = (var9 + (var8 * 286704))
        i32_store((var9 + (var8 * 286704)) + 283912, (i32_load(var2 + 283912) - 1))
    func157(var0)
    var7 = (var9 + (var8 * 286704))
    var4 = i32_load((var9 + (var8 * 286704)) + 281796)
    if (1 if i32_load((var9 + (var8 * 286704)) + 281796) == 0 else 0):
        break
    var5 = i32_load(var4 + 8)
    if (1 if i32_load(var4 + 8) == 0 else 0):
        break
    var6 = i32_load(var4)
    var2 = 0
    var12 = (var9 + (var8 * 286704))
    while True:  # loop $label42
        var3 = (var6 + (var2 << 2))
        if (1 if i32_load((var6 + (var2 << 2))) == i32_load(var0 + 28) else 0):
            var3 = ((var12 + (i32_load(var3 + 4) << 2)) + 282828)
            i32_store(((var12 + (i32_load(var3 + 4) << 2)) + 282828), (i32_load(var3) - 1))
            var5 = (i32_load(var4 + 8) - 1)
            i32_store(var4 + 8, (i32_load(var4 + 8) - 1))
            var3 = var2
            if (1 if var5 > var2 else 0):
                while True:  # loop $label40
                    var3 = (var3 + 1)
                    i32_store((var6 + (var3 << 2)), i32_load((var6 + ((var3 + 1) << 2))))
                    var5 = i32_load(var4 + 8)
                    if (1 if var3 < i32_load(var4 + 8) else 0):
                        continue
                    break  # end loop
            var5 = (var5 - 1)
            i32_store(var4 + 8, (var5 - 1))
            var3 = var2
            if (1 if var5 > var2 else 0):
                while True:  # loop $label41
                    var3 = (var3 + 1)
                    i32_store((var6 + (var3 << 2)), i32_load((var6 + ((var3 + 1) << 2))))
                    var5 = i32_load(var4 + 8)
                    if (1 if var3 < i32_load(var4 + 8) else 0):
                        continue
                    break  # end loop
            var2 = (var2 - 2)
        var2 = (var2 + 2)
        if (1 if (var2 + 2) < var5 else 0):
            continue
        break  # end loop
    var5 = i32_load(var7 + 281788)
    if (1 if i32_load(var7 + 281788) == 0 else 0):
        break
    var3 = i32_load(var5 + 8)
    if (1 if i32_load(var5 + 8) == 0 else 0):
        break
    var6 = i32_load(var5)
    var2 = 0
    while True:  # loop $label45
        if (1 if i32_load((var6 + (var2 << 2))) == i32_load(var0 + 28) else 0):
            var3 = (var3 - 1)
            i32_store(var5 + 8, (var3 - 1))
            var4 = var2
            if (1 if var2 < var3 else 0):
                while True:  # loop $label44
                    var4 = (var4 + 1)
                    i32_store((var6 + (var4 << 2)), i32_load((var6 + ((var4 + 1) << 2))))
                    var3 = i32_load(var5 + 8)
                    if (1 if var4 < i32_load(var5 + 8) else 0):
                        continue
                    break  # end loop
            var2 = (var2 - 1)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var3 else 0):
            continue
        break  # end loop
    if (1 if var11 == 0 else 0):
    var6 = ((var8 * 286704) + var9)
    var5 = (i32_load(38428) if i32_load16_u(var0 + 120) else i32_load8_u(var0 + 122))
    # br_table ['$label46', '$label47', '$label47', '$label47', '$label47', '$label47', '$label47', '$label47', '$label47', '$label47', '$label46', '$label47']
    _br_idx = (i32_load8_u(var0 + 125) - 4)
    break  # br_table
    var2 = (((var9 + (var8 * 286704)) + (var5 << 2)) + 281808)
    i32_store((((var9 + (var8 * 286704)) + (var5 << 2)) + 281808), (i32_load(var2) - 1))
    i32_store8(var0 + 125, 3)
    if i32_load16_u(var0 + 110):
        func387(var6)
    var3 = i32_load(((var10 * 404) + 9568096) + 176)
    if (1 if i32_load(((var10 * 404) + 9568096) + 176) == 0 else 0):
        break
    var2 = (var9 + (var8 * 286704))
    i32_store((var9 + (var8 * 286704)) + 283980, (i32_load(var2 + 283980) - var3))
    var4 = i32_load(var2 + 283976)
    if (1 if var3 >= -2147483647 else 0):
        i32_store8(var2 + 286700, 1)
    var2 = (var2 + 281748)
    if (1 if i32_load((var2 + 281748)) >= var4 else 0):
        break
    i32_store(var2, var4)
    break
    var2 = (((var9 + (var8 * 286704)) + (var5 << 2)) + 282828)
    i32_store((((var9 + (var8 * 286704)) + (var5 << 2)) + 282828), (i32_load(var2) - 1))
    i32_store8(var0 + 125, 3)
    if (1 if i32_load8_u(9147152) == 0 else 0):
        func77(var0)
    if (1 if i32_load(9142872) != i32_load16_u(var0 + 110) else 0):
        break
    var2 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 180)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 180) == 0 else 0):
        break
    if (1 if i32_load(var0 + 84) < 12 else 0):
        break
    if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264):
        break
    var2 = (var9 + (var8 * 286704))
    i32_store((var9 + (var8 * 286704)) + 283936, (i32_load(var2 + 283936) - 1))
    var2 = (var9 + (var8 * 286704))
    var4 = i32_load(((var10 * 404) + 9568096) + 280)
    var3 = (i32_load(var2 + 283976) - i32_load(((var10 * 404) + 9568096) + 280))
    i32_store((var9 + (var8 * 286704)) + 283976, (i32_load(var2 + 283976) - i32_load(((var10 * 404) + 9568096) + 280)))
    if (1 if (var4 - 1) >= 0 else 0):
        i32_store8(var2 + 286700, 1)
    var2 = (var2 + 281748)
    if (1 if var3 > i32_load((var2 + 281748)) else 0):
        i32_store(var2, var3)
    if (1 if var5 != i32_load(38452) else 0):
        break
    var2 = (var9 + (var8 * 286704))
    if i32_load((((var9 + (var8 * 286704)) + (var5 << 2)) + 281808)):
        break
    var4 = 0
    i32_store(((var2 + (i32_load(39144) << 2)) + 281808), 1)
    i32_store(var2 + 283868, i32_load((var2 + 284380)))
    var2 = i32_load(((var2 + (i32_load(38636) << 2)) + 284636))
    if (1 if i32_load(((var2 + (i32_load(38636) << 2)) + 284636)) == 0 else 0):
        break
    var3 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) == 0 else 0):
        break
    while True:  # loop $label52
        var7 = i32_load((i32_load(var2) + (var4 << 2)))
        if i32_load((i32_load(var2) + (var4 << 2))):
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != var3 else 0):
            continue
        break  # end loop
    var2 = (var9 + (var8 * 286704))
    if i32_load((((var9 + (var8 * 286704)) + (var5 << 2)) + 281808)):
        break
    if (1 if i32_load(var2 + 283908) != i32_load(9142872) else 0):
        break
    var3 = ((var10 * 404) + 9568096)
    if (1 if i32_load(((var10 * 404) + 9568096) + 244) == 0 else 0):
        break
    var2 = 0
    while True:  # loop $label57
        var11 = i32_load((i32_load(var3 + 240) + (var2 << 2)))
        if i32_load8_u(9147141):
            break
        var4 = 0
        var12 = i32_load(9671120)
        if (1 if i32_load(9671120) == 0 else 0):
            break
        while True:  # loop $label56
            var7 = i32_load(((var4 << 2) + 9263072))
            if (1 if i32_load(((var4 << 2) + 9263072)) == 0 else 0):
                break
            if (1 if i32_load(var7 + 12) != var11 else 0):
                break
            if i32_load8_u(var7 + 24):
                break
            break
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var12 else 0):
                continue
            break  # end loop
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < i32_load(var3 + 244) else 0):
            continue
        break  # end loop
    var2 = i32_load(var0 + 44)
    if i32_load(var0 + 44):
        i32_store((i32_load(9215884) + (var2 << 4)), 0)
    i32_store(var0 + 64, 0)
    i32_store(var0 + 44, 0)
    var2 = i32_load(9142848)
    i32_store8(var0 + 122, var5)
    i32_store16(var0 + 116, 0)
    i32_store(var0 + 68, var2)
    if i32_load8_u(9147152):
        break
    var3 = i32_load(var0 + 28)
    var2 = i32_load((((var9 + (var8 * 286704)) + (var5 << 2)) + 284636))
    if (1 if i32_load((((var9 + (var8 * 286704)) + (var5 << 2)) + 284636)) == 0 else 0):
        break
    var5 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) == 0 else 0):
        break
    var2 = i32_load(var2)
    var4 = 0
    while True:  # loop $label60
        var8 = (var2 + (var4 << 2))
        if (1 if var3 != i32_load((var2 + (var4 << 2))) else 0):
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var5 else 0):
                continue
            break
        break  # end loop
    if (1 if var4 < 0 else 0):
        break
    i32_store(var8, 0)
    var3 = i32_load(var0 + 28)
    func388(var6, var3)
    if (1 if i32_load(38528) != i32_load8_u(var0 + 122) else 0):
        break
    if i32_load8_u(9147152):
        break
    if (1 if i32_load8_u(9216060) == 0 else 0):
        break
    if (1 if i32_load(var14 + 264) == 2 else 0):
        break
    if var1:
        break
    if i32_load8_u(9147152):
        break
    if (1 if i32_load(((var10 * 404) + 9568096) + 68) == 0 else 0):
        break
    global global0
    global0 = (var13 + 16)
    return func46(0, 0)

