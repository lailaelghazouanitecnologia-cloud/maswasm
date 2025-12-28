"""
Auto-generated from WAT. Contains 3 functions.
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
# $func573
# ==========================================================
def func573(var0, var1, var2):
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
    var3 = i32_load(var0 + 4)
    var11 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 4) == i32_load(var0 + 8) else 0):
        break
    var4 = i32_load(9671128)
    var3 = (i32_load(9671128) + (var3 * 132))
    var7 = ((i32_load8_u((i32_load(9671128) + (var3 * 132)) + 122) * 404) + 9568096)
    var5 = (var4 + (var11 * 132))
    var6 = ((i32_load8_u((var4 + (var11 * 132)) + 122) * 404) + 9568096)
    var9 = ((((i32_load(((i32_load8_u((i32_load(9671128) + (var3 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + i32_load16_u(var3 + 112)) - (((i32_load(((i32_load8_u((var4 + (var11 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + i32_load16_u(var5 + 112)))
    var3 = ((i32_load16_u(var3 + 114) + ((i32_load(var7 + 220) & 0xFFFFFFFF) >> 1)) - (i32_load16_u(var5 + 114) + ((i32_load(var6 + 220) & 0xFFFFFFFF) >> 1)))
    if (1 if (((((((i32_load(((i32_load8_u((i32_load(9671128) + (var3 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + i32_load16_u(var3 + 112)) - (((i32_load(((i32_load8_u((var4 + (var11 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + i32_load16_u(var5 + 112))) * var9) + (((i32_load16_u(var3 + 114) + ((i32_load(var7 + 220) & 0xFFFFFFFF) >> 1)) - (i32_load16_u(var5 + 114) + ((i32_load(var6 + 220) & 0xFFFFFFFF) >> 1))) * var3)) - 1) < 82 else 0):
        break
    if (1 if var2 == 0 else 0):
        break
    var9 = i32_load(var0)
    var3 = i32_load(9561692)
    while True:  # loop $label11
        var7 = (var4 + (i32_load((var1 + (var12 << 2))) * 132))
        var6 = i32_load(((i32_load8_u((var4 + (i32_load((var1 + (var12 << 2))) * 132)) + 122) * 404) + 9568096) + 124)
        if (1 if i32_load(((i32_load8_u((var4 + (i32_load((var1 + (var12 << 2))) * 132)) + 122) * 404) + 9568096) + 124) == 0 else 0):
            break
        var5 = (var3 + (i32_load16_u(var7 + 110) * 286704))
        if (1 if i32_load((((var3 + (i32_load16_u(var7 + 110) * 286704)) + (i32_load(39104) << 2)) + 281808)) == 0 else 0):
            break
        var3 = i32_load((var5 + 284340))
        var13 = (var9 if (1 if var3 < var9 else 0) else i32_load((var5 + 284340)))
        var14 = (1 if var6 < var9 else 0)
        var4 = i32_load(var7 + 20)
        if (1 if i32_load(var7 + 20) == 0 else 0):
            var4 = func26(16)
            i32_store(func26(16) + 4, 7)
            var3 = func26(28)
            i32_store(var4 + 12, 16)
            i32_store(var4, var3)
            i32_store(var7 + 20, var4)
            i32_store(var4 + 8, 0)
            var8 = (var4 + 8)
            break
        i32_store(var4 + 8, 0)
        var8 = (var4 + 8)
        if (1 if i32_load(var4 + 4) == 0 else 0):
            break
        var5 = i32_load(var4)
        var3 = 0
        break
        var3 = i32_load(var4 + 12)
        i32_store(var4 + 4, i32_load(var4 + 12))
        var10 = i32_load(var4)
        var5 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
        if var10:
        else:
        var3 = 0
        i32_store(var4, var5)
        var4 = i32_load(var7 + 20)
        var10 = (var6 if var14 else var13)
        i32_store(var8, (var3 + 1))
        i32_store((var5 + (var3 << 2)), 0)
        var3 = i32_load(var4 + 8)
        if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
            var5 = i32_load(var4)
            break
        var5 = (i32_load(var4 + 12) + var3)
        i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
        var6 = i32_load(var4)
        var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
        if var3:
            # Unknown: memory.copy []
        if var6:
            var3 = i32_load(var4 + 8)
        i32_store(var4, var5)
        var6 = i32_load(var7 + 20)
        i32_store(var4 + 8, (var3 + 1))
        i32_store((var5 + (var3 << 2)), var10)
        var8 = i32_load(var0 + 4)
        var3 = i32_load(var6 + 8)
        if (1 if i32_load(var6 + 8) != i32_load(var6 + 4) else 0):
            var5 = i32_load(var6)
            break
        var5 = (i32_load(var6 + 12) + var3)
        i32_store(var6 + 4, (i32_load(var6 + 12) + var3))
        var4 = i32_load(var6)
        var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
        if var3:
            # Unknown: memory.copy []
        if var4:
            var3 = i32_load(var6 + 8)
        i32_store(var6, var5)
        var4 = i32_load(var7 + 20)
        i32_store(var6 + 8, (var3 + 1))
        i32_store((var5 + (var3 << 2)), var8)
        var8 = i32_load(var0 + 8)
        var3 = i32_load(var4 + 8)
        if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
            var5 = i32_load(var4)
            break
        var5 = (i32_load(var4 + 12) + var3)
        i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
        var6 = i32_load(var4)
        var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
        if var3:
            # Unknown: memory.copy []
        if var6:
            var3 = i32_load(var4 + 8)
        i32_store(var4, var5)
        var6 = i32_load(var7 + 20)
        i32_store(var4 + 8, (var3 + 1))
        i32_store((var5 + (var3 << 2)), var8)
        var8 = i32_load(var0 + 12)
        var3 = i32_load(var6 + 8)
        if (1 if i32_load(var6 + 8) != i32_load(var6 + 4) else 0):
            var5 = i32_load(var6)
            break
        var5 = (i32_load(var6 + 12) + var3)
        i32_store(var6 + 4, (i32_load(var6 + 12) + var3))
        var4 = i32_load(var6)
        var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
        if var3:
            # Unknown: memory.copy []
        if var4:
            var3 = i32_load(var6 + 8)
        i32_store(var6, var5)
        var4 = i32_load(var7 + 20)
        i32_store(var6 + 8, (var3 + 1))
        i32_store((var5 + (var3 << 2)), var8)
        var8 = i32_load(var0 + 16)
        var3 = i32_load(var4 + 8)
        if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
            var5 = i32_load(var4)
            break
        var5 = (i32_load(var4 + 12) + var3)
        i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
        var6 = i32_load(var4)
        var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
        if var3:
            # Unknown: memory.copy []
        if var6:
            var3 = i32_load(var4 + 8)
        i32_store(var4, var5)
        var6 = i32_load(var7 + 20)
        i32_store(var4 + 8, (var3 + 1))
        i32_store((var5 + (var3 << 2)), var8)
        var4 = i32_load(var6 + 8)
        if (1 if i32_load(var6 + 8) != i32_load(var6 + 4) else 0):
            var3 = i32_load(var6)
            break
        var3 = (i32_load(var6 + 12) + var4)
        i32_store(var6 + 4, (i32_load(var6 + 12) + var4))
        var5 = i32_load(var6)
        var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
        if var4:
            # Unknown: memory.copy []
        if var5:
            var4 = i32_load(var6 + 8)
        i32_store(var6, var3)
        i32_store(var6 + 8, (var4 + 1))
        i32_store((var3 + (var4 << 2)), 1)
        var3 = i32_load(9561692)
        var4 = i32_load(9671128)
        var12 = (var12 + 1)
        if (1 if (var12 + 1) != var2 else 0):
            continue
        break  # end loop
    return (var4 << 2)


# ==========================================================
# $func625
# ==========================================================
def func625(var0, var1):
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
    if (1 if var0 == var1 else 0):
        break
    var2 = i32_load(9671128)
    var3 = (i32_load(9671128) + (var0 * 132))
    var7 = (var2 + (var1 * 132))
    var8 = i32_load8_u((var2 + (var1 * 132)) + 122)
    if func297(var7, var0):
        i32_store8(var3 + 129, 0)
        i32_store(var3 + 36, var1)
        var4 = i32_load(var3 + 44)
        if i32_load(var3 + 44):
            i32_store((i32_load(9215884) + (var4 << 4)), 0)
        i32_store(var3 + 44, 0)
        var4 = (var2 + (var0 * 132))
        var5 = i32_load((var2 + (var0 * 132)) + 20)
        if i32_load((var2 + (var0 * 132)) + 20):
            i32_store(var5 + 8, 0)
        var4 = ((i32_load8_u(var4 + 122) * 404) + 9568096)
        if i32_load(((i32_load8_u(var4 + 122) * 404) + 9568096) + 216):
            var0 = (var2 + (var0 * 132))
            var9 = i32_load16_u((var2 + (var0 * 132)) + 114)
            var10 = i32_load16_u(var0 + 112)
            var11 = i32_load(9142840)
            var5 = 0
            while True:  # loop $label2
                var5 = (var5 + 1)
                var12 = ((var5 + 1) + var10)
                var0 = 0
                while True:  # loop $label1
                    var0 = (var0 + 1)
                    var6 = (i32_load(9142440) + 2)
                    i32_store((var11 + ((var12 + ((((var0 + 1) + var9) + ((i32_load(9142440) + 2) * i32_load(var4 + 208))) * var6)) << 2)), i32_load(var4 + 212))
                    var6 = i32_load(var4 + 216)
                    if (1 if var0 < i32_load(var4 + 216) else 0):
                        continue
                    break  # end loop
                if (1 if var5 < var6 else 0):
                    continue
                break  # end loop
        func138(var3)
        var0 = (var2 + (var1 * 132))
        if (1 if i32_load((var2 + (var1 * 132)) + 92) == 0 else 0):
            break
        if i32_load(9140316):
            if (1 if i32_load(9140320) != i32_load((var2 + (var1 * 132)) + 28) else 0):
                break
        if (1 if i32_load8_u(9147141) == 0 else 0):
            break
        if (1 if i32_load(var0 + 92) == 0 else 0):
            break
        if (1 if i32_load8_u(9147152) == 0 else 0):
            var0 = (var2 + (var1 * 132))
            if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u((var2 + (var1 * 132)) + 110))))) == 0 else 0):
                break
            if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 20 else 0):
                break
            if (1 if i32_load8_u((var2 + (var1 * 132)) + 127) == 6 else 0):
                break
        var0 = i32_load((var2 + (var1 * 132)) + 16)
        if (1 if i32_load((var2 + (var1 * 132)) + 16) == 0 else 0):
            break
        if (1 if i32_load(var0 + 8) == 0 else 0):
            break
        Ya(1)
        var3 = (var2 + (var1 * 132))
        if (1 if i32_load((var2 + (var1 * 132)) + 88) == 0 else 0):
            break
        if (1 if i32_load(((var8 * 404) + 9568096) + 264) != 4 else 0):
            break
        var0 = (var2 + (var1 * 132))
        if (1 if i32_load8_u((var2 + (var1 * 132)) + 129) != 7 else 0):
            i32_store8(var0 + 129, 7)
        var4 = i32_load(var0 + 16)
        if i32_load(var0 + 16):
        else:
        var5 = (var2 + (var1 * 132))
        if (1 if 0 < i32_load((var2 + (var1 * 132)) + 80) else 0):
            break
        var1 = i32_load(var3 + 88)
        if (1 if i32_load(var3 + 88) == 0 else 0):
            break
        var2 = i32_load(9142440)
        i32_store(var5 + 80, 0)
        i32_store(var3 + 88, 0)
        i32_store8(var0 + 129, 0)
        var0 = ((var1 & 0xFFFFFFFF) // var2)
        return func28(1, 1)
    func29(var3, 1)
    return func74(var3, -1, 0)


# ==========================================================
# $func626
# ==========================================================
def func626(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var2 = 1
    var3 = i32_load(9671128)
    var5 = i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122)
    var1 = i32_load(var1)
    var6 = (var3 + (i32_load(var1) * 132))
    var4 = i32_load8_u((var3 + (i32_load(var1) * 132)) + 122)
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) == i32_load8_u((var3 + (i32_load(var1) * 132)) + 122) else 0):
        break
    if (1 if i32_load(((var4 * 404) + 9568096) + 140) == 2 else 0):
        if (1 if i32_load(((var5 * 404) + 9568096) + 216) > 1 else 0):
            break
    if (1 if i32_load((var3 + (var0 * 132)) + 36) == var1 else 0):
        break
    var2 = 0
    if (1 if i32_load((i32_load(9561692) + (i32_load16_u((var3 + (var1 * 132)) + 110) * 286704)) + 286684) == 0 else 0):
        break
    if (1 if i32_load(((var4 * 404) + 9568096) + 264) != 4 else 0):
        break
    var1 = (var3 + (var1 * 132))
    if i32_load8_u((var3 + (var1 * 132)) + 125):
        break
    if (1 if i32_load8_u(var1 + 129) == 7 else 0):
        break
    return var2

