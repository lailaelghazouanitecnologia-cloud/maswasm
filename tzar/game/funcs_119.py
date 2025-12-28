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
# $func114
# ==========================================================
def func114(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    if var0:
        # Unknown: memory.fill []
    i32_store(9142848, 0)
    i32_store(9142440, 0)
    i32_store(59176, 0)
    i32_store(9140328, 0)
    i32_store(9142872, 0)
    i32_store(9561752, 0)
    i32_store(9561756, 0)
    var1 = i32_load(9568068)
    var2 = i32_load(9568064)
    if (1 if i32_load(9568068) != i32_load(9568064) else 0):
        while True:  # loop $label0
            var0 = (var1 - 128)
            var3 = i32_load((var1 - 128) + 12)
            if i32_load((var1 - 128) + 12):
                i32_store((var1 - 112), var3)
            var3 = i32_load(var0)
            if i32_load(var0):
                i32_store((var1 - 124), var3)
            var1 = var0
            if (1 if var0 != var2 else 0):
                continue
            break  # end loop
        i32_store(9568068, var2)
    i32_store(9684468, 0)
    i32_store(9684452, 0)
    i32_store(9684484, 0)
    var0 = i32_load(9143004)
    if i32_load(9143004):
        i32_store(9143004, 0)
    var0 = i32_load(9143008)
    if i32_load(9143008):
        i32_store(9143008, 0)
    var0 = i32_load(9147288)
    if i32_load(9147288):
        i32_store(9147288, 0)
    var0 = i32_load(9147376)
    if i32_load(9147376):
        i32_store(9147376, 0)
    var0 = i32_load(9142400)
    if i32_load(9142400):
        i32_store(9142400, 0)
    var0 = i32_load(9142840)
    if i32_load(9142840):
        i32_store(9142840, 0)
    var0 = i32_load(9142432)
    if i32_load(9142432):
        i32_store(9142432, 0)
    var0 = i32_load(9142436)
    if i32_load(9142436):
        i32_store(9142436, 0)
    if i32_load(9671136):
        var2 = i32_load(9671128)
        if i32_load(9671128):
            var4 = (var2 - 4)
            var0 = i32_load((var2 - 4))
            if i32_load((var2 - 4)):
                var1 = (var2 + (var0 * 132))
                while True:  # loop $label1
                    var0 = (var1 - 132)
                    var3 = i32_load((var1 - 132))
                    if i32_load((var1 - 132)):
                        i32_store((var1 - 128), var3)
                    var1 = var0
                    if (1 if var0 != var2 else 0):
                        continue
                    break  # end loop
            i32_store(9671128, 0)
        i32_store(9671132, 10000)
        var0 = func26(1320004)
        i32_store(func26(1320004), 10000)
        var2 = (var0 + 1320004)
        var3 = (var0 + 4)
        var0 = (var0 + 4)
        while True:  # loop $label2
            # Unknown: memory.fill []
            var1 = func26(4)
            i32_store(var0 + 4, func26(4))
            i32_store(var0, var1)
            i32_store(var0 + 8, (var1 + 4))
            var0 = (var0 + 132)
            if (1 if (var0 + 132) != var2 else 0):
                continue
            break  # end loop
        i32_store(9671128, var3)
        i64_store(9671136, 42949672960003)
    var0 = i32_load(9681936)
    if i32_load(9681936):
        i32_store(var0 + 8, 0)
    if i32_load(9215892):
        i64_store(9215888, 1024)
        var3 = 0
        var0 = i32_load(9215884)
        if (1 if i32_load(9215884) == 0 else 0):
            var2 = func26(4096)
            break
        var3 = i32_load(9215892)
        var0 = i32_load(9215888)
        var1 = func26((-1 if (1 if var0 > 1073741823 else 0) else (i32_load(9215888) << 2)))
        i32_store(9215884, func26((-1 if (1 if var0 > 1073741823 else 0) else (i32_load(9215888) << 2))))
        if (1 if var0 != var3 else 0):
            var2 = var1
            break
        var2 = (i32_load(9215896) + var0)
        i32_store(9215888, (i32_load(9215896) + var0))
        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        if var0:
            # Unknown: memory.copy []
        var3 = i32_load(9215892)
        var0 = i32_load(9215888)
        i32_store(9215884, var2)
        var1 = (var3 + 1)
        i32_store(9215892, (var3 + 1))
        i32_store((var2 + (var3 << 2)), 0)
        if (1 if var0 != var1 else 0):
            var3 = var2
            break
        var1 = (i32_load(9215896) + var0)
        i32_store(9215888, (i32_load(9215896) + var0))
        var3 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        if var0:
            # Unknown: memory.copy []
        i32_store(9215884, var3)
        var1 = i32_load(9215892)
        i32_store(9215892, (var1 + 1))
        i32_store((var3 + (var1 << 2)), 0)
        var0 = i32_load(9215892)
        if (1 if i32_load(9215892) != i32_load(9215888) else 0):
            var1 = var3
            break
        var1 = (i32_load(9215896) + var0)
        i32_store(9215888, (i32_load(9215896) + var0))
        var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
        if var0:
            # Unknown: memory.copy []
        i32_store(9215884, var1)
        var0 = i32_load(9215892)
        i32_store(9215892, (var0 + 1))
        i32_store((var1 + (var0 << 2)), 0)
        var0 = i32_load(9215892)
        if (1 if i32_load(9215892) != i32_load(9215888) else 0):
            var2 = var1
            break
        var2 = (i32_load(9215896) + var0)
        i32_store(9215888, (i32_load(9215896) + var0))
        var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        if var0:
            # Unknown: memory.copy []
        i32_store(9215884, var2)
        var0 = i32_load(9215892)
        i32_store(9215892, (var0 + 1))
        i32_store((var2 + (var0 << 2)), 0)
    return af(var1)


# ==========================================================
# $func116
# ==========================================================
def func116(var0):
    var1 = 0
    if (1 if var0 == 0 else 0):
        break
    var1 = i32_load(var0 + 8)
    i32_store(var0, 0)
    i64_store(var0 + 8, 0)
    if (1 if var1 == 0 else 0):
        break
    while True:  # loop $label1
        var0 = i32_load(var1 + 8)
        var1 = var0
        if var0:
            continue
        break  # end loop


# ==========================================================
# $func120
# ==========================================================
def func120(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var4 = i32_load(var0 + 12)
    if (1 if i32_load(var0 + 12) == 0 else 0):
        var3 = func26(16)
        i32_store(func26(16) + 4, 3)
        i32_store(var3, func26(12))
        i64_store(var3 + 8, 4294967296)
        i32_store(var0 + 12, var3)
        var8 = (var3 + 8)
        var6 = i32_load(var3)
        break
    var8 = (var4 + 8)
    var3 = i32_load(var4 + 8)
    var5 = i32_load(var4 + 4)
    if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
        var5 = var3
        var3 = var4
        var6 = i32_load(var4)
        break
    var3 = (i32_load(var4 + 12) + var5)
    i32_store(var4 + 4, (i32_load(var4 + 12) + var5))
    var7 = i32_load(var4)
    var6 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var5:
        # Unknown: memory.copy []
    var3 = var4
    if var7:
        var5 = i32_load(var4 + 8)
        var3 = i32_load(var0 + 12)
    i32_store(var4, var6)
    i32_store(var8, (var5 + 1))
    i32_store((var6 + (var5 << 2)), var1)
    var0 = i32_load(var3 + 8)
    if (1 if i32_load(var3 + 8) != i32_load(var3 + 4) else 0):
        var5 = i32_load(var3)
        break
    var1 = (i32_load(var3 + 12) + var0)
    i32_store(var3 + 4, (i32_load(var3 + 12) + var0))
    var4 = i32_load(var3)
    var5 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var0:
        # Unknown: memory.copy []
    if var4:
        var0 = i32_load(var3 + 8)
    i32_store(var3, var5)
    i32_store(var3 + 8, (var0 + 1))
    i32_store((var5 + (var0 << 2)), var2)


# ==========================================================
# $func144
# ==========================================================
def func144(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var5 = (i32_load(9671128) + (var1 * 132))
    var0 = ((var0 + ((i32_load(38428) if i32_load16_u(var5 + 120) else i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122)) << 2)) + 284636)
    var4 = i32_load(((var0 + ((i32_load(38428) if i32_load16_u(var5 + 120) else i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122)) << 2)) + 284636))
    if (1 if i32_load(((var0 + ((i32_load(38428) if i32_load16_u(var5 + 120) else i32_load8_u((i32_load(9671128) + (var1 * 132)) + 122)) << 2)) + 284636)) == 0 else 0):
        var4 = func26(16)
        i32_store(func26(16) + 4, 55)
        i32_store(var4, func26(220))
        i64_store(var4 + 8, 665719930880)
        i32_store(var0, var4)
        var7 = (var4 + 8)
        break
    var7 = (var4 + 8)
    var3 = i32_load(var4 + 8)
    var6 = i32_load(var4 + 4)
    if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
        break
    if (1 if var6 == 0 else 0):
        var3 = 0
        break
    var5 = i32_load(var4)
    var0 = 0
    var3 = 0
    while True:  # loop $label2
        var8 = i32_load((var5 + (var0 << 2)))
        if i32_load((var5 + (var0 << 2))):
            i32_store((var5 + (var3 << 2)), var8)
            var6 = i32_load(var4 + 8)
            var3 = (var3 + 1)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) < var6 else 0):
            continue
        break  # end loop
    i32_store(var4 + 8, var3)
    var0 = i32_load(var4 + 4)
    if var2:
        if (1 if var0 != var3 else 0):
            var6 = i32_load(var4)
            break
        var2 = (i32_load(var4 + 12) + var3)
        i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
        var0 = i32_load(var4)
        var6 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        if var3:
            # Unknown: memory.copy []
        if var0:
            var3 = i32_load(var7)
        i32_store(var4, var6)
        i32_store(var7, (var3 + 1))
        i32_store((var6 + (var3 << 2)), -1)
        var5 = i32_load(var7)
        if (1 if i32_load(var7) == 0 else 0):
            break
        var0 = 0
        while True:  # loop $label9
            var4 = (var6 + (var0 << 2))
            if (1 if var1 < i32_load((var6 + (var0 << 2))) else 0):
                var3 = (var5 - 1)
                if (1 if (var5 - 1) <= var0 else 0):
                    break
                var8 = ((var5 - var0) - 2)
                var9 = ((var3 - var0) & 3)
                if (1 if ((var3 - var0) & 3) == 0 else 0):
                    var2 = var5
                    break
                var7 = 0
                while True:  # loop $label7
                    var2 = var3
                    i32_store((var6 + (var3 << 2)), i32_load((((var5 << 2) + var6) - 8)))
                    var3 = (var3 - 1)
                    var5 = var2
                    var7 = (var7 + 1)
                    if (1 if (var7 + 1) != var9 else 0):
                        continue
                    break  # end loop
                if (1 if var8 < 3 else 0):
                    break
                while True:  # loop $label8
                    var5 = (var6 + (var3 << 2))
                    i32_store((var6 + (var3 << 2)), i32_load((((var2 << 2) + var6) - 8)))
                    var2 = (var5 - 8)
                    i32_store((var5 - 4), i32_load((var5 - 8)))
                    var2 = (var3 - 3)
                    var5 = (var6 + ((var3 - 3) << 2))
                    i32_store(var2, i32_load((var6 + ((var3 - 3) << 2))))
                    var3 = (var3 - 4)
                    i32_store(var5, i32_load((var6 + ((var3 - 4) << 2))))
                    if (1 if var0 < var3 else 0):
                        continue
                    break  # end loop
                break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var5 else 0):
                continue
            break  # end loop
        break
    if (1 if var0 != var3 else 0):
        var0 = i32_load(var4)
        break
    var0 = (i32_load(var4 + 12) + var3)
    i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
    var2 = i32_load(var4)
    var0 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var3:
        # Unknown: memory.copy []
    if var2:
        var3 = i32_load(var7)
    i32_store(var4, var0)
    i32_store(var7, (var3 + 1))
    var4 = (var0 + (var3 << 2))
    i32_store(var4, var1)


# ==========================================================
# $func163
# ==========================================================
def func163(var0, var1, var2, var3, var4, var5, var6, var7):
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var12 = 0
    var8 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if var2 <= ((var1 ^ -1) + 2147483631) else 0):
        if ((i32_load8_u(var0 + 11) & 0xFFFFFFFF) >> 7):
            break
        var9 = var0
        if (1 if var1 < 1073741799 else 0):
            i32_store(var8 + 12, (var1 << 1))
            i32_store(var8 + 4, (var1 + var2))
            var2 = (global0 - 16)
            global global0
            global0 = (global0 - 16)
            var10 = (var8 + 4)
            var11 = (var8 + 12)
            var12 = (1 if i32_load((var8 + 4)) < i32_load((var8 + 12)) else 0)
            global global0
            global0 = (var2 + 16)
            var2 = i32_load((var11 if var12 else var10))
            if (1 if i32_load((var11 if var12 else var10)) >= 11 else 0):
                var2 = ((var2 + 16) & -16)
                var2 = (var2 - 1)
            else:
        else:
        func314((((var2 + 16) & -16) if (1 if var2 == 11 else 0) else (var2 - 1)), (10 + 1), 2147483631)
        var2 = i32_load(var8 + 4)
        if var4:
            func122(var2, var9, var4)
        if var6:
            func122((var2 + var4), var7, var6)
        var10 = (var4 + var5)
        var7 = (var3 - (var4 + var5))
        if (1 if var3 != var10 else 0):
            func122(((var2 + var4) + var6), ((var4 + var9) + var5), var7)
        if (1 if var1 != 10 else 0):
        i32_store(var0, var2)
        i32_store(var0 + 8, ((i32_load(var0 + 8) & -2147483648) | (i32_load(var8 + 8) & 2147483647)))
        i32_store(var0 + 8, (i32_load(var0 + 8) | -2147483648))
        var0 = ((var4 + var6) + var7)
        i32_store(var0 + 4, ((var4 + var6) + var7))
        i32_store8(var8 + 12, 0)
        i32_store8((var0 + var2), i32_load8_u(var8 + 12))
        global global0
        global0 = (var8 + 16)
        return af(var9)
    func212()
    raise RuntimeError('unreachable')
    return var0

