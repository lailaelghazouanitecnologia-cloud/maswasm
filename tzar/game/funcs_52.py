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
# $func189
# ==========================================================
def func189(var0, var1, var2, var3, var4):
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
    var13 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if var1 < var2 else 0):
        if (1 if i32_load(var0 + 12) < var2 else 0):
            break
        var8 = i32_load(var0 + 8)
        # br_table ['$label1', '$label2', '$label3', '$label4', '$label5']
        _br_idx = i32_load(var0)
        break  # br_table
        # call_indirect via table[i32_load(9687572)]
        break
        if var1:
            var7 = var4
            break
        var5 = (i32_load(var3) - 16777216)
        i32_store(var4, (i32_load(var3) - 16777216))
        if (1 if var8 < 2 else 0):
            break
        var9 = (var4 + 4)
        var10 = (var3 + 4)
        var7 = (var8 - 1)
        var12 = ((var8 - 1) & 1)
        if (1 if var8 != 2 else 0):
            var15 = (var7 & -2)
            var7 = 0
            while True:  # loop $label8
                var11 = (var6 << 2)
                var14 = i32_load((var10 + var11))
                var16 = (((i32_load((var10 + var11)) & -16711936) + (var5 & -16711936)) & -16711936)
                var5 = (((var14 & 16711935) + (var5 & 16711935)) & 16711935)
                i32_store((var9 + (var6 << 2)), ((((i32_load((var10 + var11)) & -16711936) + (var5 & -16711936)) & -16711936) | (((var14 & 16711935) + (var5 & 16711935)) & 16711935)))
                var11 = (var11 | 4)
                var11 = i32_load((var10 + var11))
                var5 = ((((i32_load((var10 + var11)) & -16711936) + var16) & -16711936) | (((var11 & 16711935) + var5) & 16711935))
                i32_store((var9 + (var11 | 4)), ((((i32_load((var10 + var11)) & -16711936) + var16) & -16711936) | (((var11 & 16711935) + var5) & 16711935)))
                var6 = (var6 + 2)
                var7 = (var7 + 2)
                if (1 if (var7 + 2) != var15 else 0):
                    continue
                break  # end loop
        if (1 if var12 == 0 else 0):
            break
        var6 = (var6 << 2)
        var6 = i32_load((var6 + var10))
        i32_store((var9 + (var6 << 2)), ((((i32_load((var6 + var10)) & -16711936) + (var5 & -16711936)) & -16711936) | (((var6 & 16711935) + (var5 & 16711935)) & 16711935)))
        var5 = (var8 << 2)
        var7 = (var4 + (var8 << 2))
        var3 = (var3 + var5)
        var9 = 1
        if (1 if 1 >= var2 else 0):
            break
        var12 = (0 - var8)
        if (1 if var8 < 2 else 0):
            while True:  # loop $label11
                if (1 if var7 == 0 else 0):
                    break
                var5 = i32_load(var3)
                var6 = i32_load((var7 + (var12 << 2)))
                i32_store(var7, ((((i32_load(var3) & -16711936) + (i32_load((var7 + (var12 << 2))) & -16711936)) & -16711936) | (((var5 & 16711935) + (var6 & 16711935)) & 16711935)))
                var5 = (var8 << 2)
                var7 = (var7 + (var8 << 2))
                var3 = (var3 + var5)
                var9 = (var9 + 1)
                if (1 if (var9 + 1) != var2 else 0):
                    continue
                break
                break  # end loop
            raise RuntimeError('unreachable')
        var5 = i32_load(var0 + 4)
        var15 = (1 << i32_load(var0 + 4))
        var16 = (0 - (1 << i32_load(var0 + 4)))
        var17 = (var15 - 1)
        var18 = ((((var15 - 1) + var8) & 0xFFFFFFFF) >> var5)
        var10 = (i32_load(var0 + 16) + ((((((var15 - 1) + var8) & 0xFFFFFFFF) >> var5) * (var9 >> var5)) << 2))
        while True:  # loop $label13
            if (1 if var7 == 0 else 0):
                break
            var5 = i32_load(var3)
            var19 = (var12 << 2)
            var6 = i32_load((var7 + (var12 << 2)))
            i32_store(var7, ((((i32_load(var3) & -16711936) + (i32_load((var7 + (var12 << 2))) & -16711936)) & -16711936) | (((var5 & 16711935) + (var6 & 16711935)) & 16711935)))
            var5 = 1
            var6 = var10
            while True:  # loop $label12
                var11 = (var5 << 2)
                var20 = (var7 + var11)
                var14 = ((var5 & var16) + var15)
                var14 = (1 if var8 > var14 else 0)
                var11 = (((var5 & var16) + var15) if (1 if var8 > var14 else 0) else var8)
                # call_indirect via table[i32_load(((((i32_load(var6) & 0xFFFFFFFF) >> 6) & 60) + 9687600))]
                var6 = (var6 + 4)
                var5 = var11
                if var14:
                    continue
                break  # end loop
            var5 = (var8 << 2)
            var7 = (var7 + (var8 << 2))
            var3 = (var3 + var5)
            var9 = (var9 + 1)
            var10 = (var10 + ((0 if ((var9 + 1) & var17) else var18) << 2))
            if (1 if var2 != var9 else 0):
                continue
            break  # end loop
        if (1 if i32_load(var0 + 12) == var2 else 0):
            break
        var0 = (var8 << 2)
        # Unknown: memory.copy []
        break
        var0 = i32_load(var0 + 4)
        var6 = (1 << i32_load(var0 + 4))
        var11 = ((1 << i32_load(var0 + 4)) - 1)
        var12 = (((((1 << i32_load(var0 + 4)) - 1) + var8) & 0xFFFFFFFF) >> var0)
        var0 = (i32_load(var0 + 16) + (((((((1 << i32_load(var0 + 4)) - 1) + var8) & 0xFFFFFFFF) >> var0) * (var1 >> var0)) << 2))
        var7 = (var8 & (0 - var6))
        var9 = (var8 - (var8 & (0 - var6)))
        while True:  # loop $label16
            i32_store8(var13 + 14, 0)
            i32_store16(var13 + 12, 0)
            var15 = (var3 + (var8 << 2))
            if (1 if var7 <= 0 else 0):
                var5 = var0
                break
            var14 = (var3 + (var7 << 2))
            var5 = var0
            while True:  # loop $label15
                var10 = i32_load(var5)
                i32_store8(var13 + 12, i32_load(var5))
                i32_store8(var13 + 14, ((var10 & 0xFFFFFFFF) >> 16))
                i32_store8(var13 + 13, ((var10 & 0xFFFFFFFF) >> 8))
                # call_indirect via table[i32_load(9687792)]
                var5 = (var5 + 4)
                var10 = (var6 << 2)
                var4 = (var4 + (var6 << 2))
                var3 = (var3 + var10)
                if (1 if (var3 + var10) < var14 else 0):
                    continue
                break  # end loop
            if (1 if var3 < var15 else 0):
                var5 = i32_load(var5)
                i32_store8(var13 + 12, i32_load(var5))
                i32_store8(var13 + 14, ((var5 & 0xFFFFFFFF) >> 16))
                i32_store8(var13 + 13, ((var5 & 0xFFFFFFFF) >> 8))
                # call_indirect via table[i32_load(9687792)]
                var5 = (var9 << 2)
                var4 = (var4 + (var9 << 2))
                var3 = (var3 + var5)
            var1 = (var1 + 1)
            var0 = (var0 + ((0 if ((var1 + 1) & var11) else var12) << 2))
            if (1 if var1 != var2 else 0):
                continue
            break  # end loop
        break
        var5 = i32_load(var0 + 4)
        if (1 if var3 != var4 else 0):
            break
        if (1 if var5 <= 0 else 0):
            break
        var4 = (var2 - var1)
        var4 = ((((((var8 + (1 << var5)) - 1) & 0xFFFFFFFF) >> var5) * var4) << 2)
        var6 = ((var3 + ((var8 * (var2 - var1)) << 2)) - ((((((var8 + (1 << var5)) - 1) & 0xFFFFFFFF) >> var5) * var4) << 2))
        # Unknown: memory.copy []
        var9 = i32_load(var0 + 16)
        var7 = i32_load(var0 + 8)
        var0 = i32_load(var0 + 4)
        if i32_load(var0 + 4):
            if (1 if var7 <= 0 else 0):
                break
            var8 = ((8 & 0xFFFFFFFF) >> var0)
            var10 = ((-1 << ((8 & 0xFFFFFFFF) >> var0)) ^ -1)
            var11 = ((-1 << var0) ^ -1)
            var15 = (var7 & -2)
            var14 = (var7 & 1)
            while True:  # loop $label20
                var4 = 0
                var5 = 0
                var12 = 0
                if (1 if var7 != 1 else 0):
                    while True:  # loop $label19
                        if (var4 & var11):
                        else:
                            var5 = i32_load8_u(var6 + 1)
                        var0 = (var6 + 4)
                        i32_store(var3, i32_load((var9 + ((var5 & var10) << 2))))
                        if ((var4 | 1) & var11):
                            var6 = var0
                            break
                        var6 = (var0 + 4)
                        var5 = i32_load8_u(var0 + 1)
                        i32_store(var9 + 4, i32_load((var10 + ((((var5 & 0xFFFFFFFF) >> var8) & i32_load8_u(var0 + 1)) << 2))))
                        var4 = (var4 + 2)
                        var5 = ((var5 & 0xFFFFFFFF) >> var8)
                        var3 = (var3 + 8)
                        var12 = (var12 + 2)
                        if (1 if (var12 + 2) != var15 else 0):
                            continue
                        break  # end loop
                if var14:
                    if (1 if (var4 & var11) == 0 else 0):
                        var5 = i32_load8_u(var6 + 1)
                        var6 = (var6 + 4)
                    i32_store(var3, i32_load((var9 + ((var5 & var10) << 2))))
                    var3 = (var3 + 4)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var2 else 0):
                    continue
                break  # end loop
            break
        # call_indirect via table[i32_load(9687796)]
        break
        var7 = i32_load(var0 + 16)
        if var5:
            if (1 if var8 <= 0 else 0):
                break
            var11 = ((8 & 0xFFFFFFFF) >> var5)
            var9 = ((-1 << ((8 & 0xFFFFFFFF) >> var5)) ^ -1)
            var10 = ((-1 << var5) ^ -1)
            var15 = (var8 & -2)
            var14 = (var8 & 1)
            while True:  # loop $label23
                var5 = 0
                var6 = 0
                var12 = 0
                if (1 if var8 != 1 else 0):
                    while True:  # loop $label22
                        if (var5 & var10):
                        else:
                            var6 = i32_load8_u(var3 + 1)
                        var0 = (var3 + 4)
                        i32_store(var4, i32_load((var7 + ((var6 & var9) << 2))))
                        if ((var5 | 1) & var10):
                            var6 = ((var6 & 0xFFFFFFFF) >> var11)
                            break
                        var6 = i32_load8_u(var0 + 1)
                        var3 = (var0 + 4)
                        i32_store(var4 + 4, i32_load((var7 + ((var6 & var9) << 2))))
                        var5 = (var5 + 2)
                        var6 = ((var6 & 0xFFFFFFFF) >> var11)
                        var4 = (var4 + 8)
                        var12 = (var12 + 2)
                        if (1 if (var12 + 2) != var15 else 0):
                            continue
                        break  # end loop
                if var14:
                    if (1 if (var5 & var10) == 0 else 0):
                        var6 = i32_load8_u(var3 + 1)
                        var3 = (var3 + 4)
                    i32_store(var4, i32_load((var7 + ((var6 & var9) << 2))))
                    var4 = (var4 + 4)
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var2 else 0):
                    continue
                break  # end loop
            break
        # call_indirect via table[i32_load(9687796)]
        global global0
        global0 = (var13 + 16)
        return call_indirect(i32_load(9687796))
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    a_c()
    raise RuntimeError('unreachable')
    return 7559


# ==========================================================
# $func195
# ==========================================================
def func195():
    var0 = 0
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
    var11 = 0.0
    var12 = 0.0
    var1 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var0 = i32_load(9681808)
    if i32_load(9681808):
        var6 = i32_load(((i32_load8_u((i32_load(9671128) + (var0 * 132)) + 122) * 404) + 9568096) + 144)
    var2 = i32_load(9681812)
    if (1 if i32_load(9681812) == 0 else 0):
        break
    var5 = i32_load(9671128)
    var3 = i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122)
    var7 = i32_load(((i32_load8_u((i32_load(9671128) + (var2 * 132)) + 122) * 404) + 9568096) + 144)
    if (1 if var0 == 0 else 0):
        break
    if (1 if var0 == var2 else 0):
        break
    var0 = (var5 + (var0 * 132))
    var8 = ((i32_load8_u((var5 + (var0 * 132)) + 122) * 404) + 9568096)
    var9 = i32_load16_u(var0 + 112)
    var2 = (var5 + (var2 * 132))
    var5 = i32_load16_u((var5 + (var2 * 132)) + 112)
    var3 = ((var3 * 404) + 9568096)
    var10 = ((((i32_load(((i32_load8_u((var5 + (var0 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + i32_load16_u(var0 + 112)) - (i32_load16_u((var5 + (var2 * 132)) + 112) + ((i32_load(((var3 * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1)))
    var0 = i32_load16_u(var0 + 114)
    var2 = i32_load16_u(var2 + 114)
    var3 = ((i32_load16_u(var0 + 114) + ((i32_load(var8 + 220) & 0xFFFFFFFF) >> 1)) - (i32_load16_u(var2 + 114) + ((i32_load(var3 + 220) & 0xFFFFFFFF) >> 1)))
    if (1 if (((((((i32_load(((i32_load8_u((var5 + (var0 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + i32_load16_u(var0 + 112)) - (i32_load16_u((var5 + (var2 * 132)) + 112) + ((i32_load(((var3 * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1))) * var10) + (((i32_load16_u(var0 + 114) + ((i32_load(var8 + 220) & 0xFFFFFFFF) >> 1)) - (i32_load16_u(var2 + 114) + ((i32_load(var3 + 220) & 0xFFFFFFFF) >> 1))) * var3)) - 1) < 82 else 0):
        break
    var4 = i32_load(9681804)
    var12 = 0.800000012
    var0 = (var0 - var2)
    var0 = (var9 - var5)
    var3 = (i32_load(9561692) + (i32_load(9142872) * 286704))
    if (1 if i32_load((((i32_load(9561692) + (i32_load(9142872) * 286704)) + (i32_load(39108) << 2)) + 281808)) != 1 else 0):
    else:
    var11 = ((((0.800000012 if (1 if i32_load(((var3 + (i32_load(39168) << 2)) + 281808)) == 1 else 0) else 0.75) * float((0.800000012 * float(var4)))) / 500.0) + 0.5)
    if ((1 if ((((0.800000012 if (1 if i32_load(((var3 + (i32_load(39168) << 2)) + 281808)) == 1 else 0) else 0.75) * float((0.800000012 * float(var4)))) / 500.0) + 0.5) < 4294967296.0 else 0) & (1 if var11 >= 0.0 else 0)):
        var4 = int(var11)
        break
    var4 = 0
    i32_store(var1 + 16, i32_load(9681820))
    i32_store(var1 + 20, var4)
    i32_store(var1 + 4, var6)
    i32_store(var1 + 8, var7)
    i32_store(var1, i32_load(9681804))
    i32_store(var1 + 12, i32_load(9681816))
    global global0
    global0 = (var1 + 32)
    return var1

