"""
Auto-generated from WAT. Contains 2 functions.
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
# $func83
# ==========================================================
def func83(var0, var1, var2, var3):
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
    var8 = (global0 - 96)
    global global0
    global0 = (global0 - 96)
    var6 = (var1 + 24)
    var7 = func39((var1 + 24), 1)
    # Unknown: memory.fill []
    if var7:
        var7 = func39(var6, 1)
        i32_store((var2 + (func39(var6, (8 if func39(var6, 1) else 1)) << 2)), 1)
        if (1 if var7 != 1 else 0):
            break
        i32_store((var2 + (func39(var6, 8) << 2)), 1)
        break
    # Unknown: memory.fill []
    var7 = (func39(var6, 4) + 4)
    if (1 if (func39(var6, 4) + 4) <= 19 else 0):
        if (1 if var7 > 0 else 0):
            while True:  # loop $label1
                i32_store((var8 + (i32_load8_u((var4 + 13808)) << 2)), func39(var6, 3))
                var4 = (var4 + 1)
                if (1 if (var4 + 1) != var7 else 0):
                    continue
                break  # end loop
        if (1 if func452(128, (var8 + 76)) == 0 else 0):
            break
        if (1 if func457((var8 + 76), 7, var8, 19) == 0 else 0):
            break
        var10 = var0
        if func39(var6, 1):
            var10 = (func39(var6, ((func39(var6, 3) << 1) + 2)) + 2)
            if (1 if (func39(var6, ((func39(var6, 3) << 1) + 2)) + 2) > var0 else 0):
                break
        if (1 if var0 <= 0 else 0):
            break
        var11 = 8
        while True:  # loop $label7
            if (1 if var10 == 0 else 0):
                break
            var4 = i32_load(var1 + 44)
            if (1 if i32_load(var1 + 44) >= 32 else 0):
                func135(var6)
                var4 = i32_load(var1 + 44)
            var7 = (i32_load(i32_load(var8 + 92)) + ((i32(((i64_load(var1 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((var4 & 63)))) & 127) << 2))
            i32_store(var1 + 44, (var4 + i32_load8_u((i32_load(i32_load(var8 + 92)) + ((i32(((i64_load(var1 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64_extend_u((var4 & 63)))) & 127) << 2)))))
            var4 = i32_load16_u(var7 + 2)
            if (1 if i32_load16_u(var7 + 2) <= 15 else 0):
                i32_store((var2 + (var5 << 2)), var4)
                var11 = (var4 if var4 else var11)
                var5 = (var5 + 1)
                break
            var12 = (i32_load8_u((var4 + 13814)) + func39(var6, i32_load8_u((var4 + 13811))))
            var7 = ((i32_load8_u((var4 + 13814)) + func39(var6, i32_load8_u((var4 + 13811)))) + var5)
            if (1 if ((i32_load8_u((var4 + 13814)) + func39(var6, i32_load8_u((var4 + 13811)))) + var5) > var0 else 0):
                break
            if (1 if var12 <= 0 else 0):
                break
            var9 = (var11 if (1 if var4 == 16 else 0) else 0)
            var13 = 0
            var4 = (var12 & 7)
            if (var12 & 7):
                while True:  # loop $label5
                    i32_store((var2 + (var5 << 2)), var9)
                    var5 = (var5 + 1)
                    var13 = (var13 + 1)
                    if (1 if (var13 + 1) != var4 else 0):
                        continue
                    break  # end loop
            if (1 if (var12 - 1) >= 7 else 0):
                while True:  # loop $label6
                    var4 = (var2 + (var5 << 2))
                    i32_store((var2 + (var5 << 2)), var9)
                    i32_store(var4 + 28, var9)
                    i32_store(var4 + 24, var9)
                    i32_store(var4 + 20, var9)
                    i32_store(var4 + 16, var9)
                    i32_store(var4 + 12, var9)
                    i32_store(var4 + 8, var9)
                    i32_store(var4 + 4, var9)
                    var5 = (var5 + 8)
                    if (1 if (var5 + 8) != var7 else 0):
                        continue
                    break  # end loop
            var5 = var7
            var10 = (var10 - 1)
            if (1 if var0 > var5 else 0):
                continue
            break  # end loop
        func116((var8 + 76))
        break
        func116((var8 + 76))
        # br_table ['$label8', '$label9', '$label9', '$label9', '$label9', '$label8', '$label9']
        _br_idx = i32_load(var1)
        break  # br_table
        i32_store(var1, 3)
        break
    a_c()
    raise RuntimeError('unreachable')
    if i32_load(var1 + 48):
        break
    var4 = func457(var3, 8, var2, var0)
    if func457(var3, 8, var2, var0):
        break
    var4 = 0
    # br_table ['$label11', '$label10', '$label10', '$label10', '$label10', '$label11', '$label10']
    _br_idx = i32_load(var1)
    break  # br_table
    i32_store(var1, 3)
    global global0
    global0 = (var8 + 96)
    return var4


# ==========================================================
# $func100
# ==========================================================
def func100(var0, var1, var2):
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
    var14 = 0.0
    var15 = 0.0
    var16 = 0.0
    var17 = 0.0
    var18 = 0.0
    var19 = 0.0
    var20 = 0.0
    var21 = 0.0
    var6 = (global0 - 96)
    global global0
    global0 = (global0 - 96)
    if i32_load8_u(9142906):
        var0 = i32_load(var0 + 40)
        if (1 if i32_load(var0 + 40) == 0 else 0):
            break
        if i32_load8_u(9142916):
            i32_store(var6 + 84, var0)
            i32_store(var6 + 80, -65281)
            a_b()
            break
        i32_store(var6 + 68, var0)
        i32_store(var6 + 64, 13)
        a_b()
        break
    if i32_load8_u(9142916):
        var1 = i32_load(var0 + 40)
        if (1 if i32_load(var0 + 40) == 0 else 0):
            break
        var0 = i32_load8_u(var0 + 125)
        i32_store(var6 + 52, var1)
        i32_store(var6 + 48, ((var0 << 8) | 1))
        a_b()
        break
    var4 = i32_load16_u(var0 + 114)
    var9 = i32_load16_u(var0 + 112)
    var10 = i32_load8_u(var0 + 122)
    var3 = i32_load(var0 + 44)
    if (1 if i32_load(var0 + 44) == 0 else 0):
        break
    var5 = i32_load(9215884)
    if (1 if i32_load((i32_load(9215884) + (var3 << 4)) + 12) == 1 else 0):
        break
    if (1 if i32_load8_u(var0 + 125) == 7 else 0):
        break
    var3 = (var3 << 4)
    if i32_load((var5 + ((var3 << 4) | 4))):
        break
    var7 = i32_load(((var10 * 404) + 9568096) + 260)
    var3 = (1 if (1 if var7 <= 1 else 0) else i32_load(((var10 * 404) + 9568096) + 260))
    var5 = (((i32_load((var3 + var5)) - i32_load(9142848)) * -25) + (32000 // (1 if (1 if var7 <= 1 else 0) else i32_load(((var10 * 404) + 9568096) + 260))))
    var8 = (i32_load8_u(var0 + 124) << 3)
    var11 = i32_load(((i32_load8_u(var0 + 124) << 3) + 8996))
    var12 = (i32_load(((i32_load8_u(var0 + 124) << 3) + 8996)) * var3)
    var7 = (((((i32_load((var3 + var5)) - i32_load(9142848)) * -25) + (32000 // (1 if (1 if var7 <= 1 else 0) else i32_load(((var10 * 404) + 9568096) + 260)))) * (i32_load(((i32_load8_u(var0 + 124) << 3) + 8996)) * var3)) // 1000)
    var8 = i32_load((var8 + 8992))
    var13 = (i32_load((var8 + 8992)) * var3)
    var3 = ((var5 * (i32_load((var8 + 8992)) * var3)) // 1000)
    var14 = float(var12)
    var4 = (var4 - var11)
    var9 = (var9 - var8)
    break
    var3 = 0
    var15 = 0.0
    var5 = ((var10 * 404) + 9568096)
    var8 = i32_load(((var10 * 404) + 9568096) + 216)
    if (1 if i32_load(var5 + 264) != 1 else 0):
        break
    if (1 if var8 < 2 else 0):
        break
    var5 = ((var10 * 404) + 9568096)
    var11 = i32_load(((var10 * 404) + 9568096) + 392)
    if i32_load(((var10 * 404) + 9568096) + 392):
        var3 = (var3 - i32_load(var5 + 384))
        var8 = i32_load(var5 + 396)
        break
    var3 = (var3 - 5)
    var11 = ((var8 << 5) | 10)
    var8 = ((i32_load(var5 + 220) << 5) | 10)
    var7 = (var7 - 5)
    func120(var0, var1, 1)
    var5 = 0
    var16 = float((var3 + (var9 << 5)))
    var17 = float((var7 + (var4 << 5)))
    var19 = float(var4)
    var20 = (float(var4) * 32.0)
    var7 = ((var10 * 404) + 9568096)
    var18 = float(var11)
    var4 = 0
    if i32_load8_u(9142917):
        break
    var1 = i32_load(9299880)
    if i32_load(9299880):
        var1 = (var1 - 1)
        i32_store(9299880, (var1 - 1))
        var4 = i32_load((i32_load(9299872) + (var1 << 2)))
        break
    var4 = i32_load(9163776)
    var1 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var3 = i32_load(9163784)
    if (1 if var1 < i32_load(9163784) else 0):
        break
    i32_store(var6 + 32, var3)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    var21 = float(var8)
    func120(var0, var4, 1)
    var18 = (var18 + var16)
    if i32_load8_u(9142917):
        break
    var1 = i32_load(9299880)
    if i32_load(9299880):
        var1 = (var1 - 1)
        i32_store(9299880, (var1 - 1))
        var5 = i32_load((i32_load(9299872) + (var1 << 2)))
        break
    var5 = i32_load(9163776)
    var1 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var4 = i32_load(9163784)
    if (1 if var1 < i32_load(9163784) else 0):
        break
    i32_store(var6 + 16, var4)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    func120(var0, var5, 1)
    var16 = (var21 + var17)
    var17 = (var19 * 32.0)
    var4 = 0
    if i32_load8_u(9142917):
        break
    var1 = i32_load(9299880)
    if i32_load(9299880):
        var1 = (var1 - 1)
        i32_store(9299880, (var1 - 1))
        var4 = i32_load((i32_load(9299872) + (var1 << 2)))
        break
    var4 = i32_load(9163776)
    var1 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var3 = i32_load(9163784)
    if (1 if var1 < i32_load(9163784) else 0):
        break
    i32_store(var6, var3)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    func120(var0, var4, 1)
    break
    global global0
    global0 = (var6 + 96)
    return func40(float((var3 + (var9 << 5))), float((var7 + (var4 << 5))), (((float(var4) * 32.0) + ((float(i32_load(9142440)) * 32.0) * float(i32_load(var5 + 208)))) + -1.0), var15, var14, 0.0, 0.0, 0.0, -1.0, i32_load((9142744 if (1 if var8 > 1 else 0) else 9142448)), var2, var1, 0, 0, 0, 0.0)

