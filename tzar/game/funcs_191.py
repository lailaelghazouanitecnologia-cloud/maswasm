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
# $tc
# Export: tc
# ==========================================================
def tc():
    """Export: tc"""
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var8 = i32_load(9671136)
    var6 = func26((-1 if (1 if var8 > 1073741823 else 0) else (i32_load(9671136) << 2)))
    if (1 if var8 <= 3 else 0):
        i32_store(9671136, 3)
        break
    var5 = i32_load(9671128)
    var0 = 3
    var1 = 3
    while True:  # loop $label3
        var7 = (var1 * 132)
        var2 = (var5 + (var1 * 132))
        if (1 if i32_load8_u((var5 + (var1 * 132)) + 125) == 3 else 0):
            break
        if (1 if var0 != var1 else 0):
            if (1 if var0 >= var1 else 0):
                break
            while True:  # loop $label2
                var3 = (var0 * 132)
                var4 = (var5 + (var0 * 132))
                if (1 if i32_load8_u((var5 + (var0 * 132)) + 125) == 3 else 0):
                    var8 = i32_load(9671136)
                    var5 = i32_load(9671128)
                    # Unknown: memory.copy []
                    i32_store((var3 + var5) + 28, var0)
                    i32_store8((var5 + var7) + 125, 3)
                    i32_store((var6 + (var1 << 2)), var0)
                    var0 = (var0 + 1)
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var1 else 0):
                    continue
                break  # end loop
            var0 = var1
            break
        i32_store((var6 + (var0 << 2)), var0)
        var0 = (var0 + 1)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < var8 else 0):
            continue
        break  # end loop
    i32_store(9671136, var0)
    if (1 if var0 < 4 else 0):
        break
    var7 = i32_load(9671128)
    var2 = 3
    while True:  # loop $label6
        var3 = (var7 + (var2 * 132))
        var1 = i32_load((var7 + (var2 * 132)) + 36)
        if i32_load((var7 + (var2 * 132)) + 36):
            i32_store(var3 + 36, i32_load((var6 + (var1 << 2))))
        var4 = i32_load(var3 + 16)
        if (1 if i32_load(var3 + 16) == 0 else 0):
            break
        if (1 if i32_load(var4 + 8) == 0 else 0):
            break
        var3 = i32_load(var4)
        var0 = 0
        while True:  # loop $label5
            var1 = (var3 + (var0 << 2))
            i32_store((var3 + (var0 << 2)), i32_load((var6 + (i32_load(var1) << 2))))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < i32_load(var4 + 8) else 0):
                continue
            break  # end loop
        var0 = i32_load(9671136)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var0 else 0):
            continue
        break  # end loop
    i32_store(9215892, 4)
    if i32_load(9142892):
        var7 = i32_load(9561692)
        var4 = 0
        while True:  # loop $label10
            var2 = (var7 + (var4 * 286704))
            var1 = i32_load((var7 + (var4 * 286704)) + 281788)
            if i32_load((var7 + (var4 * 286704)) + 281788):
                i32_store(var1 + 8, 0)
            var1 = i32_load(var2 + 281792)
            if i32_load(var2 + 281792):
                i32_store(var1 + 8, 0)
            var1 = i32_load(var2 + 281796)
            if i32_load(var2 + 281796):
                i32_store(var1 + 8, 0)
            var0 = 0
            while True:  # loop $label7
                var3 = (var2 + (var0 << 2))
                i32_store(((var2 + (var0 << 2)) + 282828), 0)
                var1 = i32_load((var3 + 284636))
                if i32_load((var3 + 284636)):
                    i32_store(var1 + 8, 0)
                if i32_load((var3 + 285656)):
                    i32_store(var1 + 8, 0)
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != 255 else 0):
                    continue
                break  # end loop
            var0 = 0
            var1 = i32_load(9142892)
            var3 = i32_load(var2 + 281800)
            if (1 if i32_load(var2 + 281800) == 0 else 0):
                break
            if (1 if var1 == 0 else 0):
                break
            while True:  # loop $label9
                i32_store((var3 + (var0 << 2)), 0)
                var0 = (var0 + 1)
                var1 = i32_load(9142892)
                if (1 if (var0 + 1) < i32_load(9142892) else 0):
                    continue
                break  # end loop
            i32_store16(var2 + 286700, 0)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) < var1 else 0):
                continue
            break  # end loop
    var5 = 3
    if (1 if i32_load(9671136) > 3 else 0):
        while True:  # loop $label12
            var0 = (i32_load(9671128) + (var5 * 132))
            func157((i32_load(9671128) + (var5 * 132)))
            var1 = i32_load(var0 + 20)
            if i32_load(var0 + 20):
                i32_store(var1 + 8, 0)
            i32_store(var0 + 44, 0)
            if (1 if i32_load8_u(var0 + 125) != 4 else 0):
                i32_store8(var0 + 125, 0)
            i32_store8(var0 + 123, 0)
            i32_store16(var0 + 108, 0)
            i32_store(var0 + 88, 0)
            i32_store(var0 + 96, 0)
            if (1 if i32_load8_u(var0 + 126) != 1 else 0):
                break
            var1 = (i32_load(9671128) + (i32_load(var0 + 28) * 132))
            i32_store8((i32_load(9671128) + (i32_load(var0 + 28) * 132)) + 126, 0)
            i32_store(var1 + 52, (i32_load(var1 + 52) - (((i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 296) * i32_load(((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 284144))) & 0xFFFFFFFF) // 100)))
            if (1 if i32_load(var1 + 92) == 0 else 0):
                break
            if i32_load(9140316):
                if (1 if i32_load(9140320) != i32_load(var1 + 28) else 0):
                    break
            i64_store(var0 + 100, 0)
            i32_store(var0 + 56, 0)
            i32_store16(var0 + 127, 0)
            i32_store(var0 + 32, -1)
            var1 = 8
            if (1 if i32_load8_u(var0 + 129) != 8 else 0):
                i32_store8(var0 + 129, 0)
                var1 = 0
            func144((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)), i32_load(var0 + 28), 0)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) < i32_load(9671136) else 0):
                continue
            break  # end loop


# ==========================================================
# $func790
# ==========================================================
def func790(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    # br_table ['$label0', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label1', '$label0', '$label1']
    _br_idx = (i32_load8_u(var1 + 125) - 3)
    break  # br_table
    func119(0  # stack underflow, var1, 13, 1)
    var0 = ((i32_load8_u(var1 + 122) * 404) + 9568096)
    var0 = i32_load8_u(var1 + 125)
    var0 = ((i32_load8_u(var1 + 122) * 404) + 9568096)
    if i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 216):
        var5 = i32_load(9142840)
        var6 = i32_load16_u(var1 + 114)
        var7 = i32_load16_u(var1 + 112)
        while True:  # loop $label3
            var2 = (var2 + 1)
            var8 = ((var2 + 1) + var7)
            var3 = 0
            while True:  # loop $label2
                var3 = (var3 + 1)
                var4 = (i32_load(9142440) + 2)
                i32_store((var5 + ((var8 + ((((var3 + 1) + var6) + ((i32_load(9142440) + 2) * i32_load(var0 + 208))) * var4)) << 2)), i32_load(var0 + 212))
                var4 = i32_load(var0 + 216)
                if (1 if var3 < i32_load(var0 + 216) else 0):
                    continue
                break  # end loop
            if (1 if var2 < var4 else 0):
                continue
            break  # end loop
    func138(var1)


# ==========================================================
# $func903
# ==========================================================
def func903(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var2 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var8 = (i32_load(9671128) + (i32_load(var1) * 132))
    var6 = (i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (i32_load(var1) * 132)) + 110) * 286704))
    var3 = i32_load((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (i32_load(var1) * 132)) + 110) * 286704)) + 281792)
    if (1 if i32_load((i32_load(9561692) + (i32_load16_u((i32_load(9671128) + (i32_load(var1) * 132)) + 110) * 286704)) + 281792) == 0 else 0):
        break
    var0 = i32_load(var0)
    if (1 if i32_load(var0) >= i32_load(var3 + 8) else 0):
        break
    i64_store(var2 + 8, 0)
    i64_store(var2, 0)
    var9 = (var6 + 281792)
    var3 = i32_load((i32_load(i32_load((var6 + 281792))) + (var0 << 2)))
    var7 = ((i32_load((i32_load(i32_load((var6 + 281792))) + (var0 << 2))) & 0xFFFFFFFF) >> 16)
    var3 = (var3 & 65535)
    var4 = (((var3 & 65535) * 404) + 9568096)
    # br_table ['$label1', '$label2', '$label3', '$label4']
    _br_idx = i32_load((((var3 & 65535) * 404) + 9568096) + 268)
    break  # br_table
    var5 = (var7 * 150)
    i32_store(var2, ((((var7 * 150) * i32_load(var4 + 68)) & 0xFFFFFFFF) // 100))
    i32_store(var2 + 4, (((i32_load(var4 + 72) * var5) & 0xFFFFFFFF) // 100))
    i32_store(var2 + 8, (((i32_load(var4 + 76) * var5) & 0xFFFFFFFF) // 100))
    i32_store(var2 + 12, (((i32_load(var4 + 80) * var5) & 0xFFFFFFFF) // 100))
    break
    if (1 if i32_load(38972) == var3 else 0):
        break
    if (1 if i32_load(38976) == var3 else 0):
        break
    break
    i32_store((20 if (1 if i32_load(38968) == var3 else 0) else 4), (8 * var7))
    break
    i32_store(var2, (var7 << 4))
    if func66(var6, var2, 1, 1):
        break
    if (1 if func59((var2 + 28), (var2 + 24), var8, ((var3 * 404) + 9568096)) == 0 else 0):
        break
    var5 = func34(var3, i32_load16_u(var8 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1)
    if (1 if func34(var3, i32_load16_u(var8 + 110), i32_load(var2 + 28), i32_load(var2 + 24), 0, 1) == 0 else 0):
        break
    var6 = i32_load(9671128)
    var10 = (i32_load(9671128) + (var5 * 132))
    i32_store((i32_load(9671128) + (var5 * 132)) + 56, i32_load16_u(var8 + 110))
    if (1 if i32_load(var4 + 268) == 1 else 0):
        break
    if (1 if var3 == i32_load(38972) else 0):
        break
    if (1 if var3 == i32_load(38952) else 0):
        break
    if (1 if var3 != i32_load(38960) else 0):
        break
    break
    if (1 if i32_load(38976) != var3 else 0):
        if (1 if var3 != i32_load(38956) else 0):
            break
    break
    if (1 if i32_load(38968) == var3 else 0):
        break
    if (1 if i32_load(38964) == var3 else 0):
        break
    if (1 if var3 != i32_load(38980) else 0):
        break
    i32_store(((var6 + (var5 * 132)) + 72), var7)
    var3 = i32_load(var9)
    var4 = (i32_load(var3 + 8) - 1)
    i32_store(i32_load(var9) + 8, (i32_load(var3 + 8) - 1))
    if (1 if var0 < var4 else 0):
        var4 = i32_load(var3)
        while True:  # loop $label12
            var0 = (var0 + 1)
            i32_store((var4 + (var0 << 2)), i32_load((var4 + ((var0 + 1) << 2))))
            if (1 if var0 < i32_load(var3 + 8) else 0):
                continue
            break  # end loop
    if (1 if i32_load(9671124) != 240 else 0):
        break
    if (1 if i32_load(9142872) != i32_load16_u((var6 + (i32_load(var1) * 132)) + 110) else 0):
        break
    func221(var0)
    global global0
    global0 = (var2 + 32)
    return ((var6 + (var5 * 132)) + 60)

