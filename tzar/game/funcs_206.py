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
# $func139
# ==========================================================
def func139(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    var5 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var4 = i32_load(var0 + 36)
    if (1 if i32_load(var0 + 36) == 0 else 0):
        break
    var6 = i32_load(9671128)
    var8 = (i32_load(9671128) + (var4 * 132))
    var9 = ((i32_load8_u(var8 + 122) * 404) + 9568096)
    var7 = (var0 if (1 if i32_load(((i32_load8_u(var8 + 122) * 404) + 9568096) + 264) == 1 else 0) else (i32_load(9671128) + (var4 * 132)))
    i32_store(var5 + 12, i32_load16_u((var0 if (1 if i32_load(((i32_load8_u(var8 + 122) * 404) + 9568096) + 264) == 1 else 0) else (i32_load(9671128) + (var4 * 132))) + 112))
    i32_store(var5 + 8, i32_load16_u(var7 + 114))
    if var2:
        break
    if var3:
        break
    var3 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var7 = (var6 + (var4 * 132))
    var10 = i32_load16_u((var6 + (var4 * 132)) + 118)
    var7 = i32_load16_u(var7 + 116)
    var10 = (i32_load16_u(var7 + 116) | var10)
    var11 = ((i32_load16_u((var6 + (var4 * 132)) + 118) if (i32_load16_u(var7 + 116) | var10) else i32_load16_u(var0 + 114)) & 65535)
    var7 = ((var7 if var10 else i32_load16_u(var0 + 112)) & 65535)
    if (((i32_load16_u((var6 + (var4 * 132)) + 118) if (i32_load16_u(var7 + 116) | var10) else i32_load16_u(var0 + 114)) & 65535) | ((var7 if var10 else i32_load16_u(var0 + 112)) & 65535)):
        if func337((var5 + 12), (var5 + 8), var8, var3, var7, var11):
            break
        break
    if (1 if func338((var5 + 12), (var5 + 8), var8, var3) == 0 else 0):
        break
    if (1 if i32_load(var9 + 264) != 4 else 0):
        break
    var1 = (var6 + (var4 * 132))
    if (1 if i32_load8_u((var6 + (var4 * 132)) + 125) != 3 else 0):
        break
    var3 = (i32_load16_u(var1 + 112) - i32_load(var5 + 12))
    var1 = (i32_load16_u(var1 + 114) - i32_load(var5 + 8))
    if (1 if ((((i32_load16_u(var1 + 112) - i32_load(var5 + 12)) * var3) + ((i32_load16_u(var1 + 114) - i32_load(var5 + 8)) * var1)) - 1) < 17 else 0):
        break
    break
    i32_store(var0 + 36, 0)
    if var2:
        break
    i32_store16(var0 + 112, i32_load(var5 + 12))
    i32_store16(var0 + 114, i32_load(var5 + 8))
    if (1 if i32_load(var0 + 40) == 0 else 0):
        break
    var3 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 216):
        var9 = i32_load(9142840)
        var7 = i32_load16_u(var0 + 114)
        var10 = i32_load16_u(var0 + 112)
        var1 = 0
        while True:  # loop $label7
            var1 = (var1 + 1)
            var11 = ((var1 + 1) + var10)
            var2 = 0
            while True:  # loop $label6
                var2 = (var2 + 1)
                var12 = (i32_load(9142440) + 2)
                i32_store((var9 + ((var11 + ((((var2 + 1) + var7) + ((i32_load(9142440) + 2) * i32_load(var3 + 208))) * var12)) << 2)), i32_load(var0 + 28))
                var12 = i32_load(var3 + 216)
                if (1 if var2 < i32_load(var3 + 216) else 0):
                    continue
                break  # end loop
            if (1 if var1 < var12 else 0):
                continue
            break  # end loop
    func29(var0, 1)
    func118(var0)
    var1 = i32_load(var0 + 92)
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    var1 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) != 2 else 0):
        break
    if (1 if i32_load(var1 + 268) != 2 else 0):
        break
    var1 = (var6 + (var4 * 132))
    i32_store((var6 + (var4 * 132)) + 52, (i32_load(var1 + 52) - i32_load(var0 + 52)))
    i32_store(var1 + 60, (i32_load(var1 + 60) - i32_load(var0 + 60)))
    var1 = i32_load((var6 + (var4 * 132)) + 16)
    if (1 if i32_load((var6 + (var4 * 132)) + 16) == 0 else 0):
        break
    var9 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    var0 = i32_load(var0 + 28)
    var3 = i32_load(var1)
    var2 = 0
    while True:  # loop $label12
        if (1 if var0 == i32_load((var3 + (var2 << 2))) else 0):
            var0 = (var9 - 1)
            i32_store(var1 + 8, (var9 - 1))
            if (1 if var0 > var2 else 0):
                while True:  # loop $label11
                    var2 = (var2 + 1)
                    i32_store((var3 + (var2 << 2)), i32_load((var3 + ((var2 + 1) << 2))))
                    var0 = i32_load(var1 + 8)
                    if (1 if var2 < i32_load(var1 + 8) else 0):
                        continue
                    break  # end loop
            if var0:
                break
            break
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var9 else 0):
            continue
        break  # end loop
    break
    if (1 if i32_load(((i32_load8_u(var8 + 122) * 404) + 9568096) + 264) != 1 else 0):
        break
    var1 = i32_load(9215892)
    if (1 if i32_load(9215892) < 5 else 0):
        break
    var3 = i32_load((var6 + (var4 * 132)) + 28)
    var0 = i32_load(9215884)
    var2 = 4
    while True:  # loop $label14
        var8 = (var2 << 2)
        if (1 if i32_load((var0 + ((var2 << 2) | 4))) != 57 else 0):
            break
        if (1 if i32_load((var0 + (var8 | 8))) != var3 else 0):
            break
        i32_store((var0 + (var2 << 2)), 0)
        break
        var2 = (var2 + 4)
        if (1 if (var2 + 4) < var1 else 0):
            continue
        break  # end loop
    break
    if (1 if var1 == 0 else 0):
        break
    var0 = (var6 + (var4 * 132))
    if (1 if i32_load((var6 + (var4 * 132)) + 92) == 0 else 0):
        break
    if (1 if i32_load8_u(9147152) == 0 else 0):
        var1 = (var6 + (var4 * 132))
        if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u((var6 + (var4 * 132)) + 110))))) == 0 else 0):
            break
        if (1 if i32_load((i32_load(9215884) + (i32_load(var1 + 44) << 4)) + 4) == 20 else 0):
            break
        if (1 if i32_load8_u((var6 + (var4 * 132)) + 127) == 6 else 0):
            break
    if (1 if i32_load8_u(9147141) == 0 else 0):
        break
    var1 = i32_load((var6 + (var4 * 132)) + 16)
    if (1 if i32_load((var6 + (var4 * 132)) + 16) == 0 else 0):
        break
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    Ya(1)
    break
    i32_store8(9147141, 0)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var6 + (var4 * 132)) + 28) else 0):
            break
    var0 = i32_load(var0 + 24)
    if (1 if i32_load(var0 + 24) == 0 else 0):
        break
    var1 = i32_load(var0 + 4)
    if (1 if i32_load(var0 + 4) == 0 else 0):
        break
    var3 = i32_load((var6 + (var4 * 132)) + 16)
    var2 = 0
    var4 = i32_load(9671128)
    while True:  # loop $label17
        var0 = 0
        if var3:
        else:
        if (1 if 0 > var2 else 0):
            var0 = (var2 << 2)
            var2 = (var2 + 1)
            if (1 if i32_load(((i32_load8_u((var4 + (i32_load((var0 + i32_load(var3))) * 132)) + 122) * 404) + 9568096) + 264) != 2 else 0):
                continue
            break
        break  # end loop
    var3 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    var0 = i32_load(var1)
    var2 = 0
    while True:  # loop $label21
        var4 = (var2 << 2)
        if i32_load((var0 + (var2 << 2))):
            break
        var4 = i32_load((var0 + (var4 | 4)))
        if (1 if i32_load((var0 + (var4 | 4))) == 0 else 0):
            break
        func38(var4)
        var0 = (i32_load(var1 + 8) - 1)
        i32_store(var1 + 8, (i32_load(var1 + 8) - 1))
        if (1 if var0 > var2 else 0):
            var4 = i32_load(var1)
            var3 = var2
            while True:  # loop $label19
                var3 = (var3 + 1)
                i32_store((var4 + (var3 << 2)), i32_load((var4 + ((var3 + 1) << 2))))
                var0 = i32_load(var1 + 8)
                if (1 if var3 < i32_load(var1 + 8) else 0):
                    continue
                break  # end loop
        var0 = (var0 - 1)
        i32_store(var1 + 8, (var0 - 1))
        if (1 if var0 <= var2 else 0):
            break
        var0 = i32_load(var1)
        while True:  # loop $label20
            var2 = (var2 + 1)
            i32_store((var0 + (var2 << 2)), i32_load((var0 + ((var2 + 1) << 2))))
            if (1 if var2 < i32_load(var1 + 8) else 0):
                continue
            break  # end loop
        break
        var2 = (var2 + 2)
        if (1 if (var2 + 2) < var3 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var5 + 16)
    return i32_load(var3 + 8)

