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
# $func776
# ==========================================================
def func776(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0.0
    var9 = 0.0
    var10 = 0.0
    var11 = 0.0
    var12 = 0.0
    var13 = 0.0
    var14 = 0.0
    var15 = 0.0
    var16 = 0.0
    var17 = 0.0
    var4 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var3 = i32_load(9671128)
    var2 = (i32_load(9671128) + (var0 * 132))
    if (1 if i32_load(9142848) < (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        func29(var2, 1)
        break
    if (1 if i32_load8_u(var2 + 125) == 3 else 0):
        break
    var1 = (var3 + (var0 * 132))
    if (1 if i32_load8_u((var3 + (var0 * 132)) + 128) == 0 else 0):
        break
    i32_store8(var1 + 127, 0)
    var5 = i32_load(var1 + 40)
    if (1 if i32_load(var1 + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var4 + 36, var5)
        i32_store(var4 + 32, 0)
        a_b()
        break
    var6 = i32_load16_u(var1 + 110)
    i32_store(var4 + 20, var5)
    i32_store(var4 + 16, (var6 + 16))
    a_b()
    i32_store8(var1 + 128, 0)
    var3 = (var3 + (var0 * 132))
    var1 = i32_load16_u(var3 + 112)
    var2 = ((i32_load16_u(var3 + 112) << 5) - i32_load(9142952))
    var2 = i32_load16_u(var3 + 114)
    var5 = ((i32_load16_u(var3 + 114) << 5) - i32_load(9142956))
    if (1 if (((((i32_load16_u(var3 + 112) << 5) - i32_load(9142952)) * var2) + (((i32_load16_u(var3 + 114) << 5) - i32_load(9142956)) * var5)) - 1) > 9000000 else 0):
        break
    var6 = i32_load(39872)
    var7 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var5 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var2) + var1) << 1)))
    if (1 if var7 == 2 else 0):
        if (1 if var5 > 1 else 0):
            break
        break
    if (1 if var5 == 0 else 0):
        break
    i32_store(var4 + 8, var2)
    i32_store(var4 + 4, var1)
    i32_store(var4, var6)
    a_b()
    var2 = i32_load16_u(var3 + 114)
    var1 = i32_load16_u(var3 + 112)
    var8 = 3.0
    var15 = float((var1 & 65535))
    var10 = (float(i32_load16_u(var3 + 116)) - float((var1 & 65535)))
    var16 = float((var2 & 65535))
    var9 = (float(i32_load16_u(var3 + 118)) - float((var2 & 65535)))
    var12 = math.sqrt((((float(i32_load16_u(var3 + 116)) - float((var1 & 65535))) * var10) + ((float(i32_load16_u(var3 + 118)) - float((var2 & 65535))) * var9)))
    if (1 if (1 if math.sqrt((((float(i32_load16_u(var3 + 116)) - float((var1 & 65535))) * var10) + ((float(i32_load16_u(var3 + 118)) - float((var2 & 65535))) * var9))) > 3.0 else 0) == 0 else 0):
        break
    var9 = (var9 / var12)
    var14 = (var10 / var12)
    var3 = i32_load(9142440)
    while True:  # loop $label19
        var10 = ((var14 * var8) + var15)
        var17 = (float(((var14 * var8) + var15)) + 0.5)
        if (1 if abs((float(((var14 * var8) + var15)) + 0.5)) < 2147483648.0 else 0):
            break
        var2 = -2147483648
        var13 = ((var9 * var8) + var16)
        var17 = (float(((var9 * var8) + var16)) + 0.5)
        if (1 if abs((float(((var9 * var8) + var16)) + 0.5)) < 2147483648.0 else 0):
            break
        var1 = -2147483648
        if (1 if -2147483648 >= var3 else 0):
            break
        if (1 if (var1 | var2) < 0 else 0):
            break
        if (1 if var2 >= var3 else 0):
            break
        var2 = ((var1 << 16) + var2)
        if ((1 if var8 < 4294967300.0 else 0) & (1 if var8 >= 0.0 else 0)):
            break
        var1 = (0 * 50)
        var11 = (var13 * 32.0)
        if ((1 if (var13 * 32.0) < 4294967300.0 else 0) & (1 if var11 >= 0.0 else 0)):
            break
        var3 = 0
        var11 = (var10 * 32.0)
        if ((1 if (var10 * 32.0) < 4294967300.0 else 0) & (1 if var11 >= 0.0 else 0)):
            break
        var3 = i32_load(9142440)
        var17 = (float((var9 + var10)) + 0.5)
        if (1 if abs((float((var9 + var10)) + 0.5)) < 2147483648.0 else 0):
            break
        var2 = -2147483648
        var17 = (float((var14 + var13)) + 0.5)
        if (1 if abs((float((var14 + var13)) + 0.5)) < 2147483648.0 else 0):
            break
        var1 = -2147483648
        if (1 if -2147483648 >= var3 else 0):
            break
        if (1 if (var1 | var2) < 0 else 0):
            break
        if (1 if var2 >= var3 else 0):
            break
        var2 = ((var1 << 16) + var2)
        if ((1 if var8 < 4294967300.0 else 0) & (1 if var8 >= 0.0 else 0)):
            break
        var3 = i32_load(9142440)
        var17 = (float((var10 - var9)) + 0.5)
        if (1 if abs((float((var10 - var9)) + 0.5)) < 2147483648.0 else 0):
            break
        var2 = -2147483648
        var17 = (float((var13 - var9)) + 0.5)
        if (1 if abs((float((var13 - var9)) + 0.5)) < 2147483648.0 else 0):
            break
        var1 = -2147483648
        if (1 if -2147483648 >= var3 else 0):
            break
        if (1 if (var1 | var2) < 0 else 0):
            break
        if (1 if var2 >= var3 else 0):
            break
        var2 = ((var1 << 16) + var2)
        if ((1 if var8 < 4294967300.0 else 0) & (1 if var8 >= 0.0 else 0)):
            break
        var3 = i32_load(9142440)
        var8 = (var8 + 1.0)
        if (1 if (var8 + 1.0) < var12 else 0):
            continue
        break  # end loop
    global global0
    global0 = (var4 + 48)
    return int(var8)


# ==========================================================
# $func780
# ==========================================================
def func780(var0, var1):
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
    var18 = 0
    var19 = 0
    var20 = 0
    var1 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var2 = i32_load(9671128)
    if (1 if i32_load(9142848) < (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        func29((var2 + (var0 * 132)), 1)
        break
    var5 = (var0 * 132)
    var3 = (var2 + (var0 * 132))
    if (1 if i32_load8_u((var2 + (var0 * 132)) + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var3 + 128) == 0 else 0):
        break
    var2 = (var2 + (var0 * 132))
    i32_store8((var2 + (var0 * 132)) + 127, 0)
    var4 = i32_load(var2 + 40)
    if (1 if i32_load(var2 + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var1 + 20, var4)
        i32_store(var1 + 16, 0)
        a_b()
        break
    var2 = i32_load16_u(var2 + 110)
    i32_store(var1 + 4, var4)
    i32_store(var1, (var2 + 16))
    a_b()
    i32_store8(var3 + 128, 0)
    var2 = i32_load(9671128)
    var2 = (var2 + var5)
    var3 = i32_load16_u(var2 + 116)
    var4 = i32_load16_u(var2 + 118)
    var3 = (i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704))
    var6 = i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284364))
    var11 = (var3 - i32_load(((i32_load(9561692) + (i32_load16_u(var2 + 110) * 286704)) + 284364)))
    var2 = (var6 << 1)
    var13 = (var6 << 1)
    var14 = i32_load((var3 + 284368))
    var12 = i32_load((var3 + 284360))
    if i32_load((var3 + 284360)):
        var15 = var2
        var16 = var0
        var17 = (var4 - var6)
        var18 = (var6 + (var4 - var6))
        var19 = (var6 + var11)
        var8 = i32_load(9142440)
        var5 = i32_load(9147316)
        var3 = i32_load(9147320)
        var0 = i32_load(9147312)
        var4 = i32_load(9147324)
        var20 = (var6 * var6)
        while True:  # loop $label5
            i32_store(9147320, var0)
            var2 = var5
            i32_store(9147324, var5)
            var4 = ((var4 << 11) ^ var4)
            var5 = (((((var0 & 0xFFFFFFFF) >> 19) ^ ((((var4 << 11) ^ var4) & 0xFFFFFFFF) >> 8)) ^ var0) ^ var4)
            i32_store(9147316, (((((var0 & 0xFFFFFFFF) >> 19) ^ ((((var4 << 11) ^ var4) & 0xFFFFFFFF) >> 8)) ^ var0) ^ var4))
            var3 = ((var3 << 11) ^ var3)
            var4 = (((((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8) ^ ((var5 & 0xFFFFFFFF) >> 19)) ^ var3) ^ var5)
            i32_store(9147312, (((((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8) ^ ((var5 & 0xFFFFFFFF) >> 19)) ^ var3) ^ var5))
            var3 = (var5 % var13)
            var9 = ((var4 % var15) + var17)
            if (1 if var8 <= ((var4 % var15) + var17) else 0):
                break
            var10 = (var3 + var11)
            if (1 if var8 <= (var3 + var11) else 0):
                break
            if (1 if (var9 | var10) < 0 else 0):
                break
            if var6:
                var3 = var0
                var0 = var4
                var4 = var2
                var2 = (var10 - var19)
                var2 = (var9 - var18)
                if (1 if ((((var10 - var19) * var2) + ((var9 - var18) * var2)) - 1) > var20 else 0):
                    break
            var8 = i32_load(9142440)
            var5 = i32_load(9147316)
            var3 = i32_load(9147320)
            var0 = i32_load(9147312)
            var4 = i32_load(9147324)
            break
            var3 = var0
            var0 = var4
            var4 = var2
            var7 = (var7 + 1)
            if (1 if (var7 + 1) != var12 else 0):
                continue
            break  # end loop
    global global0
    global0 = (var1 + 32)


# ==========================================================
# $func785
# ==========================================================
def func785(var0, var1, var2):
    if var2:
        var0 = 0
        while True:  # loop $label0
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var2 else 0):
                continue
            break  # end loop

