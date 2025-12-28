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
# $func106
# ==========================================================
def func106(var0, var1, var2, var3):
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
    var21 = 0
    var10 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if i32_load(9142848) >= (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        break
    var5 = i32_load8_u(var0 + 122)
    if (1 if i32_load(var0 + 56) == 1 else 0):
        if (1 if i32_load(((var5 * 404) + 9568096) + 268) == 1 else 0):
            break
    if (1 if i32_load8_u(((var5 * 404) + 9568096) + 336) == 0 else 0):
        break
    if (1 if i32_load16_u(var0 + 120) == 0 else 0):
        break
    break
    if i32_load16_u(var0 + 120):
        break
    var5 = i32_load8_u(var0 + 122)
    i32_store(var10 + 12, 0)
    var4 = ((var5 * 404) + 9568096)
    var14 = i32_load(((var5 * 404) + 9568096) + 200)
    var7 = i32_load(((var5 * 404) + 9568096) + 200)
    if (1 if i32_load(var4 + 268) == 1 else 0):
        var7 = i32_load(var4 + 224)
    var8 = i32_load16_u(var0 + 114)
    var11 = i32_load16_u(var0 + 112)
    var15 = i32_load16_u(var0 + 110)
    var16 = (i32_load16_u(var0 + 110) * 286704)
    var6 = i32_load(9561692)
    # br_table ['$label3', '$label4', '$label4', '$label4', '$label3', '$label4']
    _br_idx = i32_load(var4 + 264)
    break  # br_table
    var4 = ((var5 * 404) + 9568096)
    var9 = i32_load(((var5 * 404) + 9568096) + 216)
    if (1 if i32_load(((var5 * 404) + 9568096) + 216) == 0 else 0):
        break
    var13 = i32_load(var4 + 220)
    if (1 if i32_load(var4 + 220) == 0 else 0):
        break
    var4 = i32_load(9215880)
    if (1 if i32_load(9215880) == 0 else 0):
        break
    var17 = i32_load(9142432)
    if (1 if i32_load(9142432) == 0 else 0):
        break
    var18 = i32_load(9142440)
    var19 = i32_load(var4)
    var5 = 0
    while True:  # loop $label7
        var20 = (var5 + var11)
        var4 = 0
        while True:  # loop $label6
            var12 = i32_load((var17 + ((var20 + ((var4 + var8) * var18)) << 2)))
            if (1 if i32_load((var19 + (i32_load((var17 + ((var20 + ((var4 + var8) * var18)) << 2))) << 2))) == 0 else 0):
                break
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var13 else 0):
                continue
            break  # end loop
        var12 = 0
        var5 = (var5 + 1)
        if (1 if (var5 + 1) != var9 else 0):
            continue
        break  # end loop
    break
    var4 = i32_load(9142432)
    if (1 if i32_load(9142432) == 0 else 0):
        break
    var12 = i32_load((var4 + (((i32_load(9142440) * var8) + var11) << 2)))
    var16 = (var6 + var16)
    var4 = i32_load8_u(var0 + 127)
    i32_store(var10 + 8, 2147483647)
    if i32_load8_u(9216060):
        var5 = i32_load8_u(9671158)
        var6 = i32_load8_u(9671157)
        break
    var6 = i32_load8_u(9671157)
    var5 = i32_load8_u(9671158)
    if (1 if i32_load((var6 + (var15 * 286704)) + 283924) > (((var7 * var7) * (((i32_load8_u(9671157) + i32_load8_u(9671158)) + 1) & 255)) * 3) else 0):
        break
    if (1 if var4 == 6 else 0):
        break
    var6 = 0
    var4 = i32_load(9142892)
    if (1 if i32_load(9142892) == 0 else 0):
        break
    while True:  # loop $label14
        if i32_load8_u((i32_load(9143004) + ((var4 * var15) + var6))):
            var7 = i32_load(9561692)
            var2 = 0
            while True:  # loop $label13
                var3 = ((var2 * 404) + 9568096)
                if (1 if i32_load(((var2 * 404) + 9568096) + 264) == 2 else 0):
                    break
                if (1 if i32_load(var3 + 188) != 55 else 0):
                    break
                var5 = i32_load((((var7 + (var6 * 286704)) + (var2 << 2)) + 284636))
                if (1 if i32_load((((var7 + (var6 * 286704)) + (var2 << 2)) + 284636)) == 0 else 0):
                    break
                var4 = 0
                var8 = i32_load(var5 + 8)
                if (1 if i32_load(var5 + 8) == 0 else 0):
                    break
                while True:  # loop $label12
                    var3 = i32_load((i32_load(var5) + (var4 << 2)))
                    if (1 if i32_load((i32_load(var5) + (var4 << 2))) == 0 else 0):
                        break
                    var3 = (i32_load(9671128) + (var3 * 132))
                    if i32_load((i32_load(9671128) + (var3 * 132)) + 36):
                        break
                    var11 = i32_load16_u(var3 + 112)
                    var9 = (i32_load16_u(var0 + 112) - i32_load16_u(var3 + 112))
                    var9 = (var9 >> 31)
                    if (1 if (((i32_load16_u(var0 + 112) - i32_load16_u(var3 + 112)) ^ (var9 >> 31)) - var9) > var14 else 0):
                        break
                    var9 = i32_load16_u(var3 + 114)
                    var13 = (i32_load16_u(var0 + 114) - i32_load16_u(var3 + 114))
                    var13 = (var13 >> 31)
                    if (1 if (((i32_load16_u(var0 + 114) - i32_load16_u(var3 + 114)) ^ (var13 >> 31)) - var13) > var14 else 0):
                        break
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != var8 else 0):
                        continue
                    break  # end loop
                var2 = (var2 + 1)
                if (1 if (var2 + 1) != 255 else 0):
                    continue
                break  # end loop
            var4 = i32_load(9142892)
        var6 = (var6 + 1)
        if (1 if (var6 + 1) < var4 else 0):
            continue
        break  # end loop
    break
    var14 = (i32_load(9142836) + (var7 * 80))
    var9 = i32_load((i32_load(9142836) + (var7 * 80)) + 4)
    if (1 if i32_load((i32_load(9142836) + (var7 * 80)) + 4) == 0 else 0):
        break
    var13 = (var8 if (1 if var3 == -1 else 0) else var3)
    var11 = (var11 if (1 if var2 == -1 else 0) else var2)
    var17 = (var5 | 2)
    var2 = (1 if (var6 & 255) == 0 else 0)
    var18 = (1 if var4 == 6 else 0)
    var5 = i32_load(9142440)
    var6 = 0
    while True:  # loop $label17
        var3 = i32_load(var14)
        var4 = (var6 << 2)
        var7 = (i32_load((i32_load(var14) + ((var6 << 2) | 4))) + var13)
        if (1 if var5 <= (i32_load((i32_load(var14) + ((var6 << 2) | 4))) + var13) else 0):
            break
        var8 = (i32_load((var3 + var4)) + var11)
        if (1 if var5 <= (i32_load((var3 + var4)) + var11) else 0):
            break
        if (1 if (var7 | var8) < 0 else 0):
            break
        var19 = (var8 + 1)
        var20 = (var7 + 1)
        var3 = i32_load(9142840)
        var4 = var2
        while True:  # loop $label16
            var21 = (var5 + 2)
            var21 = i32_load((var3 + ((var19 + ((var20 + ((var5 + 2) * var4)) * var21)) << 2)))
            if (1 if i32_load((var3 + ((var19 + ((var20 + ((var5 + 2) * var4)) * var21)) << 2))) >= 3 else 0):
                var5 = i32_load(9142440)
                var3 = i32_load(9142840)
            var4 = (var4 + 1)
            if (1 if (var4 + 1) != var17 else 0):
                continue
            break  # end loop
        var6 = (var6 + 2)
        if (1 if (var6 + 2) < var9 else 0):
            continue
        break  # end loop
    var4 = i32_load(var10 + 12)
    global global0
    global0 = (var10 + 16)
    return var4


# ==========================================================
# $func369
# ==========================================================
def func369(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0.0
    var5 = 0.0
    var6 = 0.0
    if (1 if i32_load(9671176) == 0 else 0):
        break
    if i32_load(9671192):
        while True:  # loop $label1
            func38(i32_load((i32_load(9671184) + (var2 << 2))))
            var2 = (var2 + 1)
            if (1 if (var2 + 1) < i32_load(9671192) else 0):
                continue
            break  # end loop
    i32_store(9671192, 0)
    i32_store(9671176, 0)
    i32_store8(9142412, 0)
    if (1 if i32_load8_u(9684396) == 0 else 0):
        break
    i32_store8(9684396, 0)
    a_b()
    var2 = i32_load(9671176)
    var1 = i32_load(9671172)
    if (1 if i32_load(9671172) > (var2 + 3) else 0):
        var1 = i32_load(9671168)
        break
    var1 = ((var1 + i32_load(9671180)) + 3)
    i32_store(9671172, ((var1 + i32_load(9671180)) + 3))
    var3 = i32_load(9671168)
    var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var2:
        # Unknown: memory.copy []
    if var3:
        var2 = i32_load(9671176)
    i32_store(9671168, var1)
    i32_store(9671176, (var2 + 1))
    i32_store((var1 + (var2 << 2)), var0)
    var0 = i32_load(9671176)
    i32_store(9671176, (i32_load(9671176) + 1))
    i32_store((var1 + (var0 << 2)), 0)
    var0 = i32_load(9671176)
    i32_store(9671176, (i32_load(9671176) + 1))
    i32_store((var1 + (var0 << 2)), 0)
    if (1 if i32_load8_u(9147336) == 0 else 0):
        var4 = float(i32_load(9142860))
        var4 = f32_load(40616)
        var6 = f32_load(9671164)
        var5 = (((float(i32_load(9142860)) - ((var4 * f32_load(40616)) / f32_load(9671164))) * 0.5) + ((var4 * float(i32_load(9681444))) + float(i32_load(9142956))))
        if (1 if abs((((float(i32_load(9142860)) - ((var4 * f32_load(40616)) / f32_load(9671164))) * 0.5) + ((var4 * float(i32_load(9681444))) + float(i32_load(9142956))))) < 2147483650.0 else 0):
            break
        var0 = -2147483648
        var5 = float(i32_load(9142856))
        var4 = (((var4 * float(i32_load(9681440))) + float(i32_load(9142952))) + ((float(i32_load(9142856)) - ((var4 * var5) / var6)) * 0.5))
        if (1 if abs((((var4 * float(i32_load(9681440))) + float(i32_load(9142952))) + ((float(i32_load(9142856)) - ((var4 * var5) / var6)) * 0.5))) < 2147483650.0 else 0):
            break
    return func132(-2147483648, var0)

