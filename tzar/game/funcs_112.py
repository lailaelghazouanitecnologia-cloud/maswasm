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
# $func192
# ==========================================================
def func192(var0, var1, var2):
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
    var3 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    while True:  # loop $label31
        var11 = (var1 - 16)
        var12 = (var1 - 20)
        var8 = (var1 - 28)
        while True:  # loop $label32
            var4 = var0
            while True:  # loop $label35
                var10 = (var1 - var4)
                var9 = ((var1 - var4) // 28)
                # br_table ['$label0', '$label0', '$label1', '$label2', '$label3', '$label4', '$label5']
                _br_idx = ((var1 - var4) // 28)
                break  # br_table
                var0 = (var1 - 28)
                if (1 if (i32_load((var1 - 28) + 12) * i32_load(var0 + 8)) <= (i32_load(var4 + 12) * i32_load((var4 + 8))) else 0):
                    break
                i32_store(var3 + 40, i32_load((var4 + 24)))
                i64_store(var3 + 32, i64_load((var4 + 16)))
                i64_store(var3 + 24, i64_load(var4 + 8))
                i64_store(var3 + 16, i64_load(var4))
                i32_store(var4 + 24, i32_load(var0 + 24))
                i64_store(var4 + 16, i64_load(var0 + 16))
                i64_store(var4 + 8, i64_load(var0 + 8))
                i64_store(var4, i64_load(var0))
                i32_store(var0 + 24, i32_load(var3 + 40))
                i64_store(var0 + 16, i64_load(var3 + 32))
                i64_store(var0 + 8, i64_load(var3 + 24))
                i64_store(var0, i64_load(var3 + 16))
                break
                var1 = (var1 - 28)
                var2 = (i32_load(((var1 - 28) + 12)) * i32_load(var1 + 8))
                var0 = (var4 + 28)
                var5 = (i32_load(var4 + 40) * i32_load(var4 + 36))
                if (1 if (i32_load(var4 + 40) * i32_load(var4 + 36)) <= (i32_load(var4 + 12) * i32_load(var4 + 8)) else 0):
                    if (1 if var2 <= var5 else 0):
                        break
                    i32_store(var3 + 40, i32_load(var0 + 24))
                    i64_store(var3 + 32, i64_load(var0 + 16))
                    i64_store(var3 + 24, i64_load(var0 + 8))
                    i64_store(var3 + 16, i64_load(var0))
                    i32_store(var0 + 24, i32_load(var1 + 24))
                    i64_store(var0 + 16, i64_load(var1 + 16))
                    i64_store(var0 + 8, i64_load(var1 + 8))
                    i64_store(var0, i64_load(var1))
                    i32_store(var1 + 24, i32_load(var3 + 40))
                    i64_store(var1 + 16, i64_load(var3 + 32))
                    i64_store(var1 + 8, i64_load(var3 + 24))
                    i64_store(var1, i64_load(var3 + 16))
                    if (1 if (i32_load(var4 + 40) * i32_load(var4 + 36)) <= (i32_load(var4 + 12) * i32_load((var4 + 8))) else 0):
                        break
                    i32_store(var3 + 40, i32_load((var4 + 24)))
                    i64_store(var3 + 32, i64_load((var4 + 16)))
                    i64_store(var3 + 24, i64_load(var4 + 8))
                    i64_store(var3 + 16, i64_load(var4))
                    i32_store(var4 + 24, i32_load(var0 + 24))
                    i64_store(var4 + 16, i64_load(var0 + 16))
                    i64_store(var4 + 8, i64_load(var0 + 8))
                    i64_store(var4, i64_load(var0))
                    i32_store(var0 + 24, i32_load(var3 + 40))
                    i64_store(var0 + 16, i64_load(var3 + 32))
                    i64_store(var0 + 8, i64_load(var3 + 24))
                    i64_store(var0, i64_load(var3 + 16))
                    break
                if (1 if var2 > var5 else 0):
                    i32_store(var3 + 40, i32_load((var4 + 24)))
                    i64_store(var3 + 32, i64_load((var4 + 16)))
                    i64_store(var3 + 24, i64_load((var4 + 8)))
                    i64_store(var3 + 16, i64_load(var4))
                    i32_store(var4 + 24, i32_load(var1 + 24))
                    i64_store(var4 + 16, i64_load(var1 + 16))
                    i64_store(var4 + 8, i64_load(var1 + 8))
                    i64_store(var4, i64_load(var1))
                    i32_store(var1 + 24, i32_load(var3 + 40))
                    i64_store(var1 + 16, i64_load(var3 + 32))
                    i64_store(var1 + 8, i64_load(var3 + 24))
                    i64_store(var1, i64_load(var3 + 16))
                    break
                i32_store(var3 + 40, i32_load((var4 + 24)))
                i64_store(var3 + 32, i64_load((var4 + 16)))
                i64_store(var3 + 24, i64_load((var4 + 8)))
                i64_store(var3 + 16, i64_load(var4))
                i32_store(var4 + 24, i32_load(var0 + 24))
                i64_store(var4 + 16, i64_load(var0 + 16))
                i64_store(var4 + 8, i64_load(var0 + 8))
                i64_store(var4, i64_load(var0))
                i32_store(var0 + 24, i32_load(var3 + 40))
                i64_store(var0 + 16, i64_load(var3 + 32))
                i64_store(var0 + 8, i64_load(var3 + 24))
                i64_store(var0, i64_load(var3 + 16))
                if (1 if (i32_load(var1 + 12) * i32_load(var1 + 8)) <= (i32_load(var4 + 40) * i32_load(var4 + 36)) else 0):
                    break
                i32_store(var3 + 40, i32_load(var0 + 24))
                i64_store(var3 + 32, i64_load(var0 + 16))
                i64_store(var3 + 24, i64_load(var0 + 8))
                i64_store(var3 + 16, i64_load(var0))
                i32_store(var0 + 24, i32_load(var1 + 24))
                i64_store(var0 + 16, i64_load(var1 + 16))
                i64_store(var0 + 8, i64_load(var1 + 8))
                i64_store(var0, i64_load(var1))
                i32_store(var1 + 24, i32_load(var3 + 40))
                i64_store(var1 + 16, i64_load(var3 + 32))
                i64_store(var1 + 8, i64_load(var3 + 24))
                i64_store(var1, i64_load(var3 + 16))
                break
                break
                if (1 if var10 <= 867 else 0):
                    var5 = (i32_load(var4 + 68) * i32_load((var4 - -64)))
                    var0 = (var4 + 28)
                    var2 = (var4 + 56)
                    var6 = (i32_load(var4 + 40) * i32_load(var4 + 36))
                    var7 = (i32_load(var4 + 12) * i32_load(var4 + 8))
                    if (1 if (i32_load(var4 + 40) * i32_load(var4 + 36)) <= (i32_load(var4 + 12) * i32_load(var4 + 8)) else 0):
                        if (1 if var5 <= var6 else 0):
                            break
                        i32_store(var3 + 40, i32_load(var0 + 24))
                        i64_store(var3 + 32, i64_load(var0 + 16))
                        i64_store(var3 + 24, i64_load(var0 + 8))
                        i64_store(var3 + 16, i64_load(var0))
                        i32_store(var0 + 24, i32_load((var2 + 24)))
                        i64_store(var0 + 16, i64_load((var2 + 16)))
                        i64_store(var0 + 8, i64_load((var2 + 8)))
                        i64_store(var0, i64_load(var2))
                        i32_store(var2 + 24, i32_load(var3 + 40))
                        i64_store(var2 + 16, i64_load(var3 + 32))
                        i64_store(var2 + 8, i64_load(var3 + 24))
                        i64_store(var2, i64_load(var3 + 16))
                        if (1 if (i32_load(var4 + 40) * i32_load(var4 + 36)) <= var7 else 0):
                            break
                        i32_store(var3 + 40, i32_load((var4 + 24)))
                        i64_store(var3 + 32, i64_load((var4 + 16)))
                        i64_store(var3 + 24, i64_load((var4 + 8)))
                        i64_store(var3 + 16, i64_load(var4))
                        i32_store(var4 + 24, i32_load(var0 + 24))
                        i64_store(var4 + 16, i64_load(var0 + 16))
                        i64_store(var4 + 8, i64_load(var0 + 8))
                        i64_store(var4, i64_load(var0))
                        i32_store(var0 + 24, i32_load(var3 + 40))
                        i64_store(var0 + 16, i64_load(var3 + 32))
                        i64_store(var0 + 8, i64_load(var3 + 24))
                        i64_store(var0, i64_load(var3 + 16))
                        break
                    if (1 if var5 > var6 else 0):
                        i32_store(var3 + 40, i32_load((var4 + 24)))
                        i64_store(var3 + 32, i64_load((var4 + 16)))
                        i64_store(var3 + 24, i64_load((var4 + 8)))
                        i64_store(var3 + 16, i64_load(var4))
                        i32_store(var4 + 24, i32_load((var2 + 24)))
                        i64_store(var4 + 16, i64_load((var2 + 16)))
                        i64_store(var4 + 8, i64_load((var2 + 8)))
                        i64_store(var4, i64_load(var2))
                        i32_store(var2 + 24, i32_load(var3 + 40))
                        i64_store(var2 + 16, i64_load(var3 + 32))
                        i64_store(var2 + 8, i64_load(var3 + 24))
                        i64_store(var2, i64_load(var3 + 16))
                        break
                    i32_store(var3 + 40, i32_load((var4 + 24)))
                    i64_store(var3 + 32, i64_load((var4 + 16)))
                    i64_store(var3 + 24, i64_load((var4 + 8)))
                    i64_store(var3 + 16, i64_load(var4))
                    i32_store(var4 + 24, i32_load(var0 + 24))
                    i64_store(var4 + 16, i64_load(var0 + 16))
                    i64_store(var4 + 8, i64_load(var0 + 8))
                    i64_store(var4, i64_load(var0))
                    i32_store(var0 + 24, i32_load(var3 + 40))
                    i64_store(var0 + 16, i64_load(var3 + 32))
                    i64_store(var0 + 8, i64_load(var3 + 24))
                    i64_store(var0, i64_load(var3 + 16))
                    if (1 if var5 <= (i32_load(var4 + 40) * i32_load(var4 + 36)) else 0):
                        break
                    i32_store(var3 + 40, i32_load(var0 + 24))
                    i64_store(var3 + 32, i64_load(var0 + 16))
                    i64_store(var3 + 24, i64_load(var0 + 8))
                    i64_store(var3 + 16, i64_load(var0))
                    i32_store(var0 + 24, i32_load((var2 + 24)))
                    i64_store(var0 + 16, i64_load((var2 + 16)))
                    i64_store(var0 + 8, i64_load((var2 + 8)))
                    i64_store(var0, i64_load(var2))
                    i32_store(var2 + 24, i32_load(var3 + 40))
                    i64_store(var2 + 16, i64_load(var3 + 32))
                    i64_store(var2 + 8, i64_load(var3 + 24))
                    i64_store(var2, i64_load(var3 + 16))
                    var6 = (var4 + 84)
                    if (1 if (var4 + 84) == var1 else 0):
                        break
                    while True:  # loop $label9
                        var7 = i32_load(var6 + 12)
                        var9 = i32_load(var6 + 8)
                        var8 = (i32_load(var6 + 12) * i32_load(var6 + 8))
                        if (1 if (i32_load(var6 + 12) * i32_load(var6 + 8)) > (i32_load(var2 + 12) * i32_load(var2 + 8)) else 0):
                            var14 = i64_load(var6)
                            i32_store(var3 + 24, i32_load(var6 + 24))
                            i64_store(var3 + 16, i64_load(var6 + 16))
                            var5 = var6
                            while True:  # loop $label8
                                var0 = var2
                                i64_store(var5, i64_load(var2))
                                i32_store(var5 + 24, i32_load(var0 + 24))
                                i64_store(var5 + 16, i64_load(var0 + 16))
                                i64_store(var5 + 8, i64_load(var0 + 8))
                                if (1 if var0 == var4 else 0):
                                    var0 = var4
                                    break
                                var5 = var0
                                var2 = (var0 - 28)
                                if (1 if var8 > (i32_load((var0 - 28) + 12) * i32_load(var2 + 8)) else 0):
                                    continue
                                break  # end loop
                            i32_store(var0 + 12, var7)
                            i32_store(var0 + 8, var9)
                            i64_store(var0, var14)
                            i64_store(var0 + 16, i64_load(var3 + 16))
                            i32_store(var0 + 24, i32_load(var3 + 24))
                        var2 = var6
                        var0 = (var6 + 28)
                        var6 = (var6 + 28)
                        if (1 if var0 != var1 else 0):
                            continue
                        break  # end loop
                    break
                if (1 if var2 == 0 else 0):
                    if (1 if var1 == var4 else 0):
                        break
                    var8 = (((var9 - 2) & 0xFFFFFFFF) >> 1)
                    var0 = (((var9 - 2) & 0xFFFFFFFF) >> 1)
                    while True:  # loop $label13
                        var7 = var0
                        if (1 if var8 < var0 else 0):
                            break
                        var2 = (var7 << 1)
                        var6 = ((var7 << 1) | 1)
                        var0 = (var4 + (((var7 << 1) | 1) * 28))
                        var2 = (var2 + 2)
                        if (1 if var9 > (var2 + 2) else 0):
                            var2 = (1 if (i32_load(var0 + 12) * i32_load(var0 + 8)) > (i32_load(var0 + 40) * i32_load(var0 + 36)) else 0)
                            var6 = (var2 if (1 if (i32_load(var0 + 12) * i32_load(var0 + 8)) > (i32_load(var0 + 40) * i32_load(var0 + 36)) else 0) else var6)
                            var0 = ((var0 + 28) if var2 else var0)
                        var5 = (var4 + (var7 * 28))
                        var11 = i32_load((var4 + (var7 * 28)) + 12)
                        var12 = i32_load(var5 + 8)
                        var13 = (i32_load((var4 + (var7 * 28)) + 12) * i32_load(var5 + 8))
                        if (1 if (i32_load((var4 + (var7 * 28)) + 12) * i32_load(var5 + 8)) < (i32_load(var0 + 12) * i32_load(var0 + 8)) else 0):
                            break
                        var14 = i64_load(var5)
                        i32_store(var3 + 24, i32_load(var5 + 24))
                        i64_store(var3 + 16, i64_load(var5 + 16))
                        while True:  # loop $label12
                            var2 = var0
                            i64_store(var5, i64_load(var0))
                            i32_store(var5 + 24, i32_load(var0 + 24))
                            i64_store(var5 + 16, i64_load(var0 + 16))
                            i64_store(var5 + 8, i64_load(var0 + 8))
                            if (1 if var6 > var8 else 0):
                                break
                            var5 = (var6 << 1)
                            var6 = ((var6 << 1) | 1)
                            var0 = (var4 + (((var6 << 1) | 1) * 28))
                            var5 = (var5 + 2)
                            if (1 if var9 > (var5 + 2) else 0):
                                var5 = (1 if (i32_load(var0 + 12) * i32_load(var0 + 8)) > (i32_load(var0 + 40) * i32_load(var0 + 36)) else 0)
                                var6 = (var5 if (1 if (i32_load(var0 + 12) * i32_load(var0 + 8)) > (i32_load(var0 + 40) * i32_load(var0 + 36)) else 0) else var6)
                                var0 = ((var0 + 28) if var5 else var0)
                            var5 = var2
                            if (1 if (i32_load(var0 + 12) * i32_load(var0 + 8)) <= var13 else 0):
                                continue
                            break  # end loop
                        i32_store(var2 + 12, var11)
                        i32_store(var2 + 8, var12)
                        i64_store(var2, var14)
                        i64_store(var2 + 16, i64_load(var3 + 16))
                        i32_store(var2 + 24, i32_load(var3 + 24))
                        var0 = (var7 - 1)
                        if var7:
                            continue
                        break  # end loop
                    var0 = ((var10 & 0xFFFFFFFF) // 28)
                    while True:  # loop $label19
                        i32_store(var3 + 40, i32_load(var4 + 24))
                        i64_store(var3 + 32, i64_load(var4 + 16))
                        i64_store(var3 + 24, i64_load(var4 + 8))
                        i64_store(var3 + 16, i64_load(var4))
                        var6 = var0
                        var9 = (((var0 - 2) & 0xFFFFFFFF) >> 1)
                        var2 = 0
                        var5 = var4
                        while True:  # loop $label15
                            var8 = (var2 << 1)
                            var7 = ((var2 << 1) | 1)
                            var0 = (((var2 * 28) + var5) + 28)
                            var2 = (var8 + 2)
                            if (1 if var6 <= (var8 + 2) else 0):
                                var2 = var7
                                break
                            var7 = (1 if (i32_load(var0 + 12) * i32_load(var0 + 8)) > (i32_load(var0 + 40) * i32_load(var0 + 36)) else 0)
                            var2 = (var2 if (1 if (i32_load(var0 + 12) * i32_load(var0 + 8)) > (i32_load(var0 + 40) * i32_load(var0 + 36)) else 0) else var7)
                            var0 = ((var0 + 28) if var7 else var0)
                            i64_store(var5, i64_load(var0))
                            i32_store(var5 + 24, i32_load((var0 + 24)))
                            i64_store(var5 + 16, i64_load((var0 + 16)))
                            i64_store(var5 + 8, i64_load((var0 + 8)))
                            var5 = var0
                            if (1 if var2 <= var9 else 0):
                                continue
                            break  # end loop
                        var1 = (var1 - 28)
                        if (1 if (var1 - 28) == var0 else 0):
                            i64_store(var0, i64_load(var3 + 16))
                            i32_store(var0 + 24, i32_load(var3 + 40))
                            i64_store(var0 + 16, i64_load(var3 + 32))
                            i64_store(var0 + 8, i64_load(var3 + 24))
                            break
                        i64_store(var0, i64_load(var1))
                        i32_store(var0 + 24, i32_load((var1 + 24)))
                        i64_store(var0 + 16, i64_load((var1 + 16)))
                        i64_store(var0 + 8, i64_load((var1 + 8)))
                        i64_store(var1, i64_load(var3 + 16))
                        i64_store(var1 + 8, i64_load(var3 + 24))
                        i64_store(var1 + 16, i64_load(var3 + 32))
                        i32_store(var1 + 24, i32_load(var3 + 40))
                        var2 = ((var0 - var4) + 28)
                        if (1 if ((var0 - var4) + 28) < 29 else 0):
                            break
                        var7 = i32_load(var0 + 12)
                        var9 = i32_load(var0 + 8)
                        var8 = (i32_load(var0 + 12) * i32_load(var0 + 8))
                        var10 = (((((var2 & 0xFFFFFFFF) // 28) - 2) & 0xFFFFFFFF) >> 1)
                        var2 = (var4 + ((((((var2 & 0xFFFFFFFF) // 28) - 2) & 0xFFFFFFFF) >> 1) * 28))
                        if (1 if (i32_load(var0 + 12) * i32_load(var0 + 8)) >= (i32_load((var4 + ((((((var2 & 0xFFFFFFFF) // 28) - 2) & 0xFFFFFFFF) >> 1) * 28)) + 12) * i32_load(var2 + 8)) else 0):
                            break
                        var14 = i64_load(var0)
                        i32_store(var3 + 8, i32_load(var0 + 24))
                        i64_store(var3, i64_load(var0 + 16))
                        while True:  # loop $label18
                            var5 = var2
                            i64_store(var0, i64_load(var2))
                            i32_store(var0 + 24, i32_load(var5 + 24))
                            i64_store(var0 + 16, i64_load(var5 + 16))
                            i64_store(var0 + 8, i64_load(var5 + 8))
                            if (1 if var10 == 0 else 0):
                                break
                            var0 = var5
                            var10 = (((var10 - 1) & 0xFFFFFFFF) >> 1)
                            var2 = (var4 + ((((var10 - 1) & 0xFFFFFFFF) >> 1) * 28))
                            if (1 if (i32_load((var4 + ((((var10 - 1) & 0xFFFFFFFF) >> 1) * 28)) + 12) * i32_load(var2 + 8)) > var8 else 0):
                                continue
                            break  # end loop
                        i32_store(var5 + 12, var7)
                        i32_store(var5 + 8, var9)
                        i64_store(var5, var14)
                        i64_store(var5 + 16, i64_load(var3))
                        i32_store(var5 + 24, i32_load(var3 + 8))
                        var0 = (var6 - 1)
                        if (1 if var6 > 2 else 0):
                            continue
                        break  # end loop
                    break
                var7 = (var4 + (((var9 & 0xFFFFFFFF) >> 1) * 28))
                if (1 if var10 >= 27973 else 0):
                    var0 = (((var9 & 0xFFFFFFFF) >> 2) * 28)
                    break
                var0 = (i32_load(var11) * i32_load(var12))
                var5 = (i32_load((var7 + 12)) * i32_load((var7 + 8)))
                if (1 if (i32_load((var7 + 12)) * i32_load((var7 + 8))) <= (i32_load((var4 + 12)) * i32_load((var4 + 8))) else 0):
                    if (1 if var0 <= var5 else 0):
                        break
                    var0 = var7
                    i32_store(var3 + 40, i32_load((var7 + 24)))
                    i64_store(var3 + 32, i64_load((var0 + 16)))
                    i64_store(var3 + 24, i64_load(var0 + 8))
                    i64_store(var3 + 16, i64_load(var0))
                    i32_store(var0 + 24, i32_load(var8 + 24))
                    i64_store(var0 + 16, i64_load(var8 + 16))
                    i64_store(var0 + 8, i64_load(var8 + 8))
                    i64_store(var0, i64_load(var8))
                    i32_store(var8 + 24, i32_load(var3 + 40))
                    i64_store(var8 + 16, i64_load(var3 + 32))
                    i64_store(var8 + 8, i64_load(var3 + 24))
                    i64_store(var8, i64_load(var3 + 16))
                    if (1 if (i32_load(var0 + 12) * i32_load(var0 + 8)) <= (i32_load(var4 + 12) * i32_load(var4 + 8)) else 0):
                        break
                    i32_store(var3 + 40, i32_load((var4 + 24)))
                    i64_store(var3 + 32, i64_load((var4 + 16)))
                    i64_store(var3 + 24, i64_load(var4 + 8))
                    i64_store(var3 + 16, i64_load(var4))
                    i32_store(var4 + 24, i32_load(var0 + 24))
                    i64_store(var4 + 16, i64_load(var7 + 16))
                    i64_store(var4 + 8, i64_load(var7 + 8))
                    i64_store(var4, i64_load(var7))
                    i32_store(var0 + 24, i32_load(var3 + 40))
                    i64_store(var7 + 16, i64_load(var3 + 32))
                    i64_store(var7 + 8, i64_load(var3 + 24))
                    i64_store(var7, i64_load(var3 + 16))
                    break
                if (1 if var0 > var5 else 0):
                    i32_store(var3 + 40, i32_load((var4 + 24)))
                    i64_store(var3 + 32, i64_load((var4 + 16)))
                    i64_store(var3 + 24, i64_load(var4 + 8))
                    i64_store(var3 + 16, i64_load(var4))
                    i32_store(var4 + 24, i32_load(var8 + 24))
                    i64_store(var4 + 16, i64_load(var8 + 16))
                    i64_store(var4 + 8, i64_load(var8 + 8))
                    i64_store(var4, i64_load(var8))
                    i32_store(var8 + 24, i32_load(var3 + 40))
                    i64_store(var8 + 16, i64_load(var3 + 32))
                    i64_store(var8 + 8, i64_load(var3 + 24))
                    i64_store(var8, i64_load(var3 + 16))
                    break
                i32_store(var3 + 40, i32_load((var4 + 24)))
                i64_store(var3 + 32, i64_load((var4 + 16)))
                i64_store(var3 + 24, i64_load(var4 + 8))
                i64_store(var3 + 16, i64_load(var4))
                var0 = var7
                i32_store(var4 + 24, i32_load((var7 + 24)))
                i64_store(var4 + 16, i64_load((var0 + 16)))
                i64_store(var4 + 8, i64_load(var0 + 8))
                i64_store(var4, i64_load(var0))
                i32_store(var0 + 24, i32_load(var3 + 40))
                i64_store(var0 + 16, i64_load(var3 + 32))
                i64_store(var0 + 8, i64_load(var3 + 24))
                i64_store(var0, i64_load(var3 + 16))
                if (1 if (i32_load(var11) * i32_load(var12)) <= (i32_load(var0 + 12) * i32_load(var0 + 8)) else 0):
                    break
                i32_store(var3 + 40, i32_load(var0 + 24))
                i64_store(var3 + 32, i64_load(var7 + 16))
                i64_store(var3 + 24, i64_load(var7 + 8))
                i64_store(var3 + 16, i64_load(var7))
                i32_store(var0 + 24, i32_load(var8 + 24))
                i64_store(var7 + 16, i64_load(var8 + 16))
                i64_store(var7 + 8, i64_load(var8 + 8))
                i64_store(var7, i64_load(var8))
                i32_store(var8 + 24, i32_load(var3 + 40))
                i64_store(var8 + 16, i64_load(var3 + 32))
                i64_store(var8 + 8, i64_load(var3 + 24))
                i64_store(var8, i64_load(var3 + 16))
                var10 = 2
                var2 = (var2 - 1)
                var5 = var8
                var9 = var4
                var4 = (i32_load((var4 + 12)) * i32_load((var4 + 8)))
                var13 = (i32_load(var7 + 12) * i32_load(var7 + 8))
                if (1 if (i32_load((var4 + 12)) * i32_load((var4 + 8))) > (i32_load(var7 + 12) * i32_load(var7 + 8)) else 0):
                    var0 = var8
                    break
                while True:  # loop $label25
                    var0 = (var5 - 28)
                    if (1 if (var5 - 28) == var9 else 0):
                        var5 = (var9 + 28)
                        if (1 if var4 > (i32_load(var11) * i32_load(var12)) else 0):
                            break
                        if (1 if var5 == var8 else 0):
                            break
                        while True:  # loop $label24
                            if (1 if (i32_load(var5 + 12) * i32_load((var5 + 8))) < var4 else 0):
                                i32_store(var3 + 40, i32_load((var5 + 24)))
                                i64_store(var3 + 32, i64_load((var5 + 16)))
                                i64_store(var3 + 24, i64_load(var5 + 8))
                                i64_store(var3 + 16, i64_load(var5))
                                i32_store(var5 + 24, i32_load(var8 + 24))
                                i64_store(var5 + 16, i64_load(var8 + 16))
                                i64_store(var5 + 8, i64_load(var8 + 8))
                                i64_store(var5, i64_load(var8))
                                i32_store(var8 + 24, i32_load(var3 + 40))
                                i64_store(var8 + 16, i64_load(var3 + 32))
                                i64_store(var8 + 8, i64_load(var3 + 24))
                                i64_store(var8, i64_load(var3 + 16))
                                var5 = (var5 + 28)
                                break
                            var5 = (var5 + 28)
                            if (1 if (var5 + 28) != var8 else 0):
                                continue
                            break  # end loop
                        break
                    var6 = (var5 - 28)
                    var5 = var0
                    if (1 if (i32_load(var6 + 12) * i32_load(var6 + 8)) <= var13 else 0):
                        continue
                    break  # end loop
                i32_store(var3 + 40, i32_load((var9 + 24)))
                i64_store(var3 + 32, i64_load((var9 + 16)))
                i64_store(var3 + 24, i64_load(var9 + 8))
                i64_store(var3 + 16, i64_load(var9))
                i32_store(var9 + 24, i32_load((var0 + 24)))
                i64_store(var9 + 16, i64_load((var0 + 16)))
                i64_store(var9 + 8, i64_load((var0 + 8)))
                i64_store(var9, i64_load(var0))
                i32_store(var0 + 24, i32_load(var3 + 40))
                i64_store(var0 + 16, i64_load(var3 + 32))
                i64_store(var0 + 8, i64_load(var3 + 24))
                i64_store(var0, i64_load(var3 + 16))
                var10 = (var10 + 1)
                var6 = (var9 + 28)
                if (1 if (var9 + 28) >= var0 else 0):
                    break
                while True:  # loop $label29
                    var5 = (i32_load(var7 + 12) * i32_load(var7 + 8))
                    while True:  # loop $label27
                        var4 = var6
                        var6 = (var6 + 28)
                        if (1 if (i32_load(var4 + 12) * i32_load(var4 + 8)) > var5 else 0):
                            continue
                        break  # end loop
                    while True:  # loop $label28
                        var0 = (var0 - 28)
                        if (1 if (i32_load((var0 - 28) + 12) * i32_load((var0 + 8))) <= var5 else 0):
                            continue
                        break  # end loop
                    if (1 if var0 < var4 else 0):
                        var6 = var4
                        break
                    else:
                        i32_store(var3 + 40, i32_load(var4 + 24))
                        i64_store(var3 + 32, i64_load(var4 + 16))
                        i64_store(var3 + 24, i64_load(var4 + 8))
                        i64_store(var3 + 16, i64_load(var4))
                        i32_store(var4 + 24, i32_load((var0 + 24)))
                        i64_store(var4 + 16, i64_load((var0 + 16)))
                        i64_store(var4 + 8, i64_load(var0 + 8))
                        i64_store(var4, i64_load(var0))
                        i32_store(var0 + 24, i32_load(var3 + 40))
                        i64_store(var0 + 16, i64_load(var3 + 32))
                        i64_store(var0 + 8, i64_load(var3 + 24))
                        i64_store(var0, i64_load(var3 + 16))
                        var7 = (var0 if (1 if var4 == var7 else 0) else var7)
                        var10 = (var10 + 1)
                        continue
                    raise RuntimeError('unreachable')
                    break  # end loop
                raise RuntimeError('unreachable')
                break
                if (1 if var6 == var7 else 0):
                    break
                if (1 if (i32_load(var7 + 12) * i32_load((var7 + 8))) <= (i32_load(var6 + 12) * i32_load((var6 + 8))) else 0):
                    break
                i32_store(var3 + 40, i32_load((var6 + 24)))
                i64_store(var3 + 32, i64_load((var6 + 16)))
                i64_store(var3 + 24, i64_load(var6 + 8))
                i64_store(var3 + 16, i64_load(var6))
                i32_store(var6 + 24, i32_load((var7 + 24)))
                i64_store(var6 + 16, i64_load((var7 + 16)))
                i64_store(var6 + 8, i64_load(var7 + 8))
                i64_store(var6, i64_load(var7))
                i32_store(var7 + 24, i32_load(var3 + 40))
                i64_store(var7 + 16, i64_load(var3 + 32))
                i64_store(var7 + 8, i64_load(var3 + 24))
                i64_store(var7, i64_load(var3 + 16))
                var10 = (var10 + 1)
                if (1 if var10 == 0 else 0):
                    var4 = func419(var9, var6)
                    var0 = (var6 + 28)
                    if func419((var6 + 28), var1):
                        var0 = var9
                        var1 = var6
                        if (1 if var4 == 0 else 0):
                            continue
                        break
                    if var4:
                        continue
                if (1 if ((var6 - var9) // 28) < ((var1 - var6) // 28) else 0):
                    var0 = (var6 + 28)
                    continue
                var0 = var9
                var1 = var6
                continue
                var0 = var8
                if (1 if var8 == var5 else 0):
                    break
                while True:  # loop $label36
                    var6 = (i32_load(var9 + 12) * i32_load(var9 + 8))
                    while True:  # loop $label33
                        var4 = var5
                        var5 = (var5 + 28)
                        if (1 if var6 <= (i32_load(var4 + 12) * i32_load((var4 + 8))) else 0):
                            continue
                        break  # end loop
                    while True:  # loop $label34
                        var0 = (var0 - 28)
                        if (1 if var6 > (i32_load((var0 - 28) + 12) * i32_load((var0 + 8))) else 0):
                            continue
                        break  # end loop
                    if (1 if var0 <= var4 else 0):
                        continue
                    i32_store(var3 + 40, i32_load((var4 + 24)))
                    i64_store(var3 + 32, i64_load((var4 + 16)))
                    i64_store(var3 + 24, i64_load(var4 + 8))
                    i64_store(var3 + 16, i64_load(var4))
                    i32_store(var4 + 24, i32_load((var0 + 24)))
                    i64_store(var4 + 16, i64_load((var0 + 16)))
                    i64_store(var4 + 8, i64_load(var0 + 8))
                    i64_store(var4, i64_load(var0))
                    i32_store(var0 + 24, i32_load(var3 + 40))
                    i64_store(var0 + 16, i64_load(var3 + 32))
                    i64_store(var0 + 8, i64_load(var3 + 24))
                    i64_store(var0, i64_load(var3 + 16))
                    continue
                    break  # end loop
                raise RuntimeError('unreachable')
                break  # end loop
            break  # end loop
        break  # end loop
    global global0
    global0 = (var3 + 48)
    return func192((var6 + 28), var1, var2)

