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
# $func531
# ==========================================================
def func531(var0, var1, var2):
    var3 = 0
    var4 = 0
    if var2:
        var3 = i32_load(9671128)
        var0 = 0
        while True:  # loop $label0
            var4 = (var3 + (i32_load((var1 + (var0 << 2))) * 132))
            if (1 if i32_load8_u((var3 + (i32_load((var1 + (var0 << 2))) * 132)) + 125) != 3 else 0):
                func304(var4)
                var3 = i32_load(9671128)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var2 else 0):
                continue
            break  # end loop


# ==========================================================
# $func540
# ==========================================================
def func540(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    if var2:
        var6 = i32_load(9215884)
        var7 = i32_load(9671128)
        while True:  # loop $label3
            var4 = 12
            var0 = (var7 + (i32_load((var1 + (var3 << 2))) * 132))
            # br_table ['$label0', '$label1', '$label1', '$label1', '$label1', '$label1', '$label2', '$label1']
            _br_idx = i32_load((var6 + (i32_load((var7 + (i32_load((var1 + (var3 << 2))) * 132)) + 44) << 4)) + 4)
            break  # br_table
            i32_store8(var0 + 123, 0)
            i32_store(var0 + 32, 0)
            i32_store(var0 + 116, i32_load(var0 + 112))
            var4 = 6
            var5 = i32_load(var0 + 20)
            if (1 if i32_load(var0 + 20) == 0 else 0):
                break
            if (1 if i32_load(var5 + 8) < 3 else 0):
                break
            if (1 if (i32_load(i32_load(var5)) - 1) > 1 else 0):
                break
            i32_store(var5 + 8, 0)
            break
            func29(var0, 1)
            var6 = i32_load(9215884)
            var7 = i32_load(9671128)
            var4 = 6
            i32_store8(var0 + 129, var4)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) != var2 else 0):
                continue
            break  # end loop


# ==========================================================
# $func622
# ==========================================================
def func622(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var3 = i32_load(9671128)
    var4 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) == 3 else 0):
        break
    if var1:
        if (1 if i32_load8_u((var3 + (var0 * 132)) + 127) != 6 else 0):
            break
    var1 = (var3 + (var0 * 132))
    i32_store8((var3 + (var0 * 132)) + 127, 0)
    if (1 if i32_load8_u(9142916) == 0 else 0):
        break
    var5 = i32_load(var1 + 40)
    if (1 if i32_load(var1 + 40) == 0 else 0):
        break
    i32_store(var2 + 4, var5)
    i32_store(var2, 0)
    a_b()
    func29(var4, 1)
    if (1 if i32_load(var1 + 92) == 0 else 0):
        break
    var1 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var3 + (var0 * 132)) + 28) else 0):
            break
    global global0
    global0 = (var2 + 16)


# ==========================================================
# $func690
# ==========================================================
def func690(var0, var1, var2, var3, var4):
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var7 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var4 = 1
    var6 = i32_load(9671128)
    var10 = (i32_load(9671128) + (var0 * 132))
    var8 = i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122)
    var9 = ((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096)
    if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 264) == 1 else 0):
        var1 = i32_load(var1)
        if i32_load(var1):
            var1 = (var6 + (var1 * 132))
            var5 = ((i32_load8_u(var1 + 122) * 404) + 9568096)
            var4 = (i32_load16_u((var6 + (var1 * 132)) + 114) + ((i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1))
            break
        var4 = i32_load(var3)
        var1 = i32_load(var2)
        var5 = (var6 + (var0 * 132))
        i32_store16((var6 + (var0 * 132)) + 118, var4)
        i32_store16(var5 + 116, var1)
        var4 = 1
        var1 = (i32_load(9142440) + 2)
        if (1 if i32_load((i32_load(9142840) + ((i32_load(var2) + (((i32_load(var3) + ((i32_load(9142440) + 2) * i32_load(((var8 * 404) + 9568096) + 208))) + 1) * var1)) << 2)) + 4) == i32_load(var5 + 28) else 0):
            var0 = i32_load(var5 + 80)
            if (1 if i32_load(var5 + 80) == 0 else 0):
                break
            if (1 if i32_load(var9 + 264) != 1 else 0):
                break
            func38(var0)
            i32_store(var5 + 80, 0)
            i32_store16(var5 + 116, 0)
            i32_store16(var5 + 118, 0)
            break
        if (1 if i32_load(var5 + 92) == 0 else 0):
            break
        var0 = (var6 + (var0 * 132))
        var1 = i32_load((var6 + (var0 * 132)) + 80)
        if (1 if i32_load((var6 + (var0 * 132)) + 80) == 0 else 0):
            break
        if (1 if i32_load(var9 + 264) != 1 else 0):
            break
        func38(var1)
        i32_store(var0 + 80, 0)
        func203(var10)
        break
    if (1 if i32_load(var9 + 260) == 0 else 0):
        break
    if (1 if i32_load(var1) != var0 else 0):
        break
    i32_store(var1, 0)
    if (1 if i32_load((i32_load(9215884) + (i32_load((var6 + (var0 * 132)) + 44) << 4)) + 4) != 6 else 0):
        break
    func304(var10)
    break
    var4 = 0
    var0 = ((var8 * 404) + 9568096)
    var5 = i32_load(((var8 * 404) + 9568096) + 212)
    # br_table ['$label5', '$label6', '$label2']
    _br_idx = i32_load(((var8 * 404) + 9568096) + 212)
    break  # br_table
    var0 = i32_load(var2)
    var1 = i32_load(var3)
    var6 = (i32_load(9142440) + 2)
    if (1 if (i32_load((i32_load(9142840) + ((i32_load(var2) + (((i32_load(var3) + (i32_load(9142440) + 2)) + 1) * var6)) << 2)) + 4) - 3) < -2 else 0):
        break
    break
    if (1 if i32_load(var0 + 208) > 1 else 0):
        break
    var0 = i32_load(var2)
    var1 = i32_load(var3)
    var6 = (i32_load(9142440) + 2)
    if (1 if i32_load((i32_load(9142840) + ((i32_load(var2) + (((i32_load(var3) + (i32_load(9142440) + 2)) + 1) * var6)) << 2)) + 4) != 1 else 0):
        break
    i32_store(var7 + 12, var0)
    i32_store(var7 + 8, var1)
    var4 = 1
    if (1 if func167((var7 + 12), (var7 + 8), 1, var5, i32_load(((var8 * 404) + 9568096) + 216)) == 0 else 0):
        break
    i32_store(var2, i32_load(var7 + 12))
    i32_store(var3, i32_load(var7 + 8))
    var4 = 0
    global global0
    global0 = (var7 + 16)
    return var4


# ==========================================================
# $func717
# ==========================================================
def func717(var0, var1):
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
    var4 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var5 = i32_load(9671128)
    var6 = (i32_load(9671128) + (var0 * 132))
    var3 = i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125)
    if (1 if i32_load8_u((i32_load(9671128) + (var0 * 132)) + 125) != 3 else 0):
        if (1 if i32_load8_u(var6 + 128) == 2 else 0):
            if (1 if (var1 & 1) == 0 else 0):
                break
            var2 = (var5 + (var0 * 132))
            var3 = i32_load((var5 + (var0 * 132)) + 72)
            if i32_load((var5 + (var0 * 132)) + 72):
                var3 = (var3 - 1)
                i32_store(var2 + 72, (var3 - 1))
                var7 = ((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 281668)
                i32_store(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 281668), (i32_load(var7) + 1))
                if var3:
                    break
            i32_store8(var2 + 127, 0)
            var3 = i32_load(var2 + 40)
            if i32_load(var2 + 40):
                if i32_load8_u(9142916):
                    i32_store(var4 + 20, var3)
                    i32_store(var4 + 16, 0)
                    a_b()
                    i32_store8(var6 + 128, 0)
                    break
                var2 = i32_load16_u(var2 + 110)
                i32_store(var4 + 4, var3)
                i32_store(var4, (var2 + 16))
                a_b()
            i32_store8(var6 + 128, 0)
            break
        if (1 if var3 == 8 else 0):
            var2 = (var5 + (var0 * 132))
            var7 = (i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704))
            var3 = (i32_load(var2 + 72) + i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284068)))
            i32_store((var5 + (var0 * 132)) + 72, (i32_load(var2 + 72) + i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284068))))
            var9 = i32_load8_u(var2 + 123)
            var7 = i32_load(((var7 + (i32_load(((i32_load8_u(var2 + 123) * 40) + 9671200) + 8) << 2)) + 283984))
            if (1 if i32_load(((var7 + (i32_load(((i32_load8_u(var2 + 123) * 40) + 9671200) + 8) << 2)) + 283984)) > var3 else 0):
                break
            if (1 if var3 <= i32_load(var2 + 76) else 0):
                break
            var3 = (var5 + (var0 * 132))
            i32_store8((var5 + (var0 * 132)) + 127, 0)
            if (1 if i32_load8_u(9142916) == 0 else 0):
                break
            var3 = i32_load(var3 + 40)
            if (1 if i32_load(var3 + 40) == 0 else 0):
                break
            i32_store(var4 + 36, var3)
            i32_store(var4 + 32, 0)
            a_b()
            var8 = (var5 + (var0 * 132))
            var3 = i32_load((var5 + (var0 * 132)) + 32)
            var9 = ((var9 * 40) + 9671200)
            if (1 if i32_load8_u(((var9 * 40) + 9671200) + 17) == 0 else 0):
                break
            var10 = i32_load(9671128)
            var11 = (i32_load(9671128) + (var3 * 132))
            var12 = (i32_load16_u((i32_load(9671128) + (var3 * 132)) + 112) - i32_load16_u(var8 + 112))
            var8 = (i32_load16_u(var11 + 114) - i32_load16_u(var8 + 114))
            var8 = i32_load(var9 + 4)
            if (1 if ((((i32_load16_u((i32_load(9671128) + (var3 * 132)) + 112) - i32_load16_u(var8 + 112)) * var12) + ((i32_load16_u(var11 + 114) - i32_load16_u(var8 + 114)) * var8)) - 1) <= (i32_load(var9 + 4) * var8) else 0):
                if (1 if i32_load8_u((var10 + (var3 * 132)) + 125) != 3 else 0):
                    break
            func29(var6, 1)
            break
            i32_store(var2 + 72, (i32_load(var2 + 72) - var7))
            var2 = ((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 281668)
            i32_store(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 281668), (i32_load(var2) + var7))
            # call_indirect via table[i32_load(var9 + 20)]
            i32_store8(var6 + 125, 0)
            break
        var6 = (var5 + (var0 * 132))
        var2 = i32_load((var5 + (var0 * 132)) + 72)
        var7 = i32_load(var6 + 76)
        if (1 if i32_load((var5 + (var0 * 132)) + 72) < i32_load(var6 + 76) else 0):
            if (1 if var3 != 9 else 0):
                var2 = (i32_load(((i32_load(9561692) + (i32_load16_u((var5 + (var0 * 132)) + 110) * 286704)) + 284068)) + var2)
                i32_store(var6 + 72, (i32_load(((i32_load(9561692) + (i32_load16_u((var5 + (var0 * 132)) + 110) * 286704)) + 284068)) + var2))
            if (1 if var2 < var7 else 0):
                break
        i32_store(var6 + 72, var7)
        var2 = i32_load(9684420)
        var0 = (var5 + (var0 * 132))
        if (1 if i32_load(9684420) != i32_load((var5 + (var0 * 132)) + 28) else 0):
            break
        if (1 if i32_load(var0 + 92) == 0 else 0):
            break
        if i32_load(9140316):
            if (1 if i32_load(9140320) != var2 else 0):
                break
        var5 = i32_load(9215884)
        var2 = (i32_load(9215884) + (i32_load(9671116) << 2))
        i32_store((i32_load(9215884) + (i32_load(9671116) << 2)), (i32_load(var2) + ((i32_load(((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 284156)) & 0xFFFFFFFF) // 25)))
        i32_store((var5 + (i32_load(9671116) << 2)) + 12, (var1 + 1))
    global global0
    global0 = (var4 + 48)

