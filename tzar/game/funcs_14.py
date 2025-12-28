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
# $func260
# ==========================================================
def func260(var0, var1):
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
    var21 = 0
    var22 = 0
    var10 = (global0 - 32)
    var9 = i32_load(var1)
    var2 = i32_load(var1 + 8)
    var4 = i32_load(i32_load(var1 + 8))
    var8 = i32_load(var2 + 12)
    i64_store(var0 + 5200, 2461016260608)
    var14 = -1
    var2 = 0
    if (1 if var8 > 0 else 0):
        while True:  # loop $label1
            var3 = (var9 + (var2 << 2))
            if i32_load16_u((var9 + (var2 << 2))):
                var3 = (i32_load(var0 + 5200) + 1)
                i32_store(var0 + 5200, (i32_load(var0 + 5200) + 1))
                i32_store(((var0 + (var3 << 2)) + 2908), var2)
                i32_store8(((var0 + var2) + 5208), 0)
                var14 = var2
                break
            i32_store16(var3 + 2, 0)
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var8 else 0):
                continue
            break  # end loop
        var2 = i32_load(var0 + 5200)
        if (1 if i32_load(var0 + 5200) > 1 else 0):
            break
    while True:  # loop $label3
        var2 = (var2 + 1)
        i32_store(var0 + 5200, (var2 + 1))
        var3 = (var14 + 1)
        var7 = (1 if var14 < 2 else 0)
        var2 = ((var14 + 1) if (1 if var14 < 2 else 0) else 0)
        i32_store(((var0 + (var2 << 2)) + 2908), ((var14 + 1) if (1 if var14 < 2 else 0) else 0))
        var5 = (var2 << 2)
        i32_store16((var9 + (var2 << 2)), 1)
        i32_store8(((var0 + var2) + 5208), 0)
        i32_store(var0 + 5800, (i32_load(var0 + 5800) - 1))
        if var4:
            i32_store(var0 + 5804, (i32_load(var0 + 5804) - i32_load16_u((var4 + var5) + 2)))
        var14 = (var3 if var7 else var14)
        var2 = i32_load(var0 + 5200)
        if (1 if i32_load(var0 + 5200) < 2 else 0):
            continue
        break  # end loop
    i32_store(var1 + 4, var14)
    var2 = ((var2 & 0xFFFFFFFF) >> 1)
    while True:  # loop $label8
        var7 = var2
        var6 = i32_load(((var0 + (var2 << 2)) + 2908))
        var3 = (var2 << 1)
        var5 = i32_load(var0 + 5200)
        if (1 if (var2 << 1) > i32_load(var0 + 5200) else 0):
            break
        var11 = ((var0 + var6) + 5208)
        var12 = (var9 + (var6 << 2))
        var4 = var7
        while True:  # loop $label7
            if (1 if var3 >= var5 else 0):
                var2 = var3
                break
            var2 = (var0 + 2908)
            var5 = (var3 | 1)
            var13 = i32_load(((var0 + 2908) + ((var3 | 1) << 2)))
            var15 = i32_load16_u((var9 + (i32_load(((var0 + 2908) + ((var3 | 1) << 2))) << 2)))
            var16 = i32_load((var2 + (var3 << 2)))
            var2 = i32_load16_u((var9 + (i32_load((var2 + (var3 << 2))) << 2)))
            if (1 if i32_load16_u((var9 + (i32_load(((var0 + 2908) + ((var3 | 1) << 2))) << 2))) >= i32_load16_u((var9 + (i32_load((var2 + (var3 << 2))) << 2))) else 0):
                if (1 if var2 != var15 else 0):
                    var2 = var3
                    break
                var2 = var3
                var3 = (var0 + 5208)
                if (1 if i32_load8_u(((var0 + 5208) + var13)) > i32_load8_u((var3 + var16)) else 0):
                    break
            var2 = var5
            var5 = i32_load16_u(var12)
            var3 = i32_load(((var0 + (var2 << 2)) + 2908))
            var13 = i32_load16_u((var9 + (i32_load(((var0 + (var2 << 2)) + 2908)) << 2)))
            if (1 if i32_load16_u(var12) < i32_load16_u((var9 + (i32_load(((var0 + (var2 << 2)) + 2908)) << 2))) else 0):
                var2 = var4
                break
            if (1 if var5 != var13 else 0):
                break
            if (1 if i32_load8_u(var11) > i32_load8_u(((var0 + var3) + 5208)) else 0):
                break
            var2 = var4
            break
            i32_store(((var0 + (var4 << 2)) + 2908), var3)
            var4 = var2
            var3 = (var2 << 1)
            var5 = i32_load(var0 + 5200)
            if (1 if (var2 << 1) <= i32_load(var0 + 5200) else 0):
                continue
            break  # end loop
        i32_store(((var0 + (var2 << 2)) + 2908), var6)
        var2 = (var7 - 1)
        if (1 if var7 > 1 else 0):
            continue
        break  # end loop
    var3 = i32_load(var0 + 5200)
    while True:  # loop $label17
        var7 = var8
        var5 = (var3 - 1)
        i32_store(var0 + 5200, (var3 - 1))
        var12 = i32_load(var0 + 2912)
        var11 = i32_load(((var0 + (var3 << 2)) + 2908))
        i32_store(var0 + 2912, i32_load(((var0 + (var3 << 2)) + 2908)))
        var2 = 1
        if (1 if var3 < 3 else 0):
            break
        var6 = ((var0 + var11) + 5208)
        var3 = 2
        var13 = (var9 + (var11 << 2))
        var4 = 1
        while True:  # loop $label12
            if (1 if var3 >= var5 else 0):
                var2 = var3
                break
            var2 = (var0 + 2908)
            var8 = (var3 | 1)
            var5 = i32_load(((var0 + 2908) + ((var3 | 1) << 2)))
            var15 = i32_load16_u((var9 + (i32_load(((var0 + 2908) + ((var3 | 1) << 2))) << 2)))
            var16 = i32_load((var2 + (var3 << 2)))
            var2 = i32_load16_u((var9 + (i32_load((var2 + (var3 << 2))) << 2)))
            if (1 if i32_load16_u((var9 + (i32_load(((var0 + 2908) + ((var3 | 1) << 2))) << 2))) >= i32_load16_u((var9 + (i32_load((var2 + (var3 << 2))) << 2))) else 0):
                if (1 if var2 != var15 else 0):
                    var2 = var3
                    break
                var2 = var3
                var3 = (var0 + 5208)
                if (1 if i32_load8_u(((var0 + 5208) + var5)) > i32_load8_u((var3 + var16)) else 0):
                    break
            var2 = var8
            var8 = i32_load16_u(var13)
            var3 = i32_load(((var0 + (var2 << 2)) + 2908))
            var5 = i32_load16_u((var9 + (i32_load(((var0 + (var2 << 2)) + 2908)) << 2)))
            if (1 if i32_load16_u(var13) < i32_load16_u((var9 + (i32_load(((var0 + (var2 << 2)) + 2908)) << 2))) else 0):
                var2 = var4
                break
            if (1 if var5 != var8 else 0):
                break
            if (1 if i32_load8_u(var6) > i32_load8_u(((var0 + var3) + 5208)) else 0):
                break
            var2 = var4
            break
            i32_store(((var0 + (var4 << 2)) + 2908), var3)
            var4 = var2
            var3 = (var2 << 1)
            var5 = i32_load(var0 + 5200)
            if (1 if (var2 << 1) <= i32_load(var0 + 5200) else 0):
                continue
            break  # end loop
        var3 = 2
        var6 = (var0 + 2908)
        i32_store(((var0 + 2908) + (var2 << 2)), var11)
        var4 = (i32_load(var0 + 5204) - 1)
        i32_store(var0 + 5204, (i32_load(var0 + 5204) - 1))
        var2 = i32_load(var0 + 2912)
        i32_store((var6 + (var4 << 2)), var12)
        var4 = (i32_load(var0 + 5204) - 1)
        i32_store(var0 + 5204, (i32_load(var0 + 5204) - 1))
        i32_store((var6 + (var4 << 2)), var2)
        var13 = (var9 + (var7 << 2))
        var4 = (var9 + (var2 << 2))
        var8 = (var9 + (var12 << 2))
        i32_store16((var9 + (var7 << 2)), (i32_load16_u((var9 + (var2 << 2))) + i32_load16_u((var9 + (var12 << 2)))))
        var11 = (var0 + 5208)
        var15 = ((var0 + 5208) + var7)
        var5 = i32_load8_u((var11 + var12))
        var2 = i32_load8_u((var2 + var11))
        i32_store8(((var0 + 5208) + var7), ((i32_load8_u((var11 + var12)) if (1 if var2 < var5 else 0) else i32_load8_u((var2 + var11))) + 1))
        i32_store16(var4 + 2, var7)
        i32_store16(var8 + 2, var7)
        i32_store(var0 + 2912, var7)
        var4 = 1
        var2 = 1
        var5 = i32_load(var0 + 5200)
        if (1 if i32_load(var0 + 5200) < 2 else 0):
            break
        while True:  # loop $label16
            if (1 if var3 >= var5 else 0):
                break
            var8 = (var3 | 1)
            var5 = i32_load((var6 + ((var3 | 1) << 2)))
            var2 = i32_load16_u((var9 + (i32_load((var6 + ((var3 | 1) << 2))) << 2)))
            var12 = i32_load((var6 + (var3 << 2)))
            var16 = i32_load16_u((var9 + (i32_load((var6 + (var3 << 2))) << 2)))
            if (1 if i32_load16_u((var9 + (i32_load((var6 + ((var3 | 1) << 2))) << 2))) >= i32_load16_u((var9 + (i32_load((var6 + (var3 << 2))) << 2))) else 0):
                if (1 if var2 != var16 else 0):
                    break
                if (1 if i32_load8_u((var5 + var11)) > i32_load8_u((var11 + var12)) else 0):
                    break
            var2 = var8
            var8 = i32_load16_u(var13)
            var3 = i32_load(((var0 + (var2 << 2)) + 2908))
            var5 = i32_load16_u((var9 + (i32_load(((var0 + (var2 << 2)) + 2908)) << 2)))
            if (1 if i32_load16_u(var13) < i32_load16_u((var9 + (i32_load(((var0 + (var2 << 2)) + 2908)) << 2))) else 0):
                var2 = var4
                break
            if (1 if var5 != var8 else 0):
                break
            if (1 if i32_load8_u(var15) > i32_load8_u(((var0 + var3) + 5208)) else 0):
                break
            var2 = var4
            break
            i32_store(((var0 + (var4 << 2)) + 2908), var3)
            var4 = var2
            var3 = (var2 << 1)
            var5 = i32_load(var0 + 5200)
            if (1 if (var2 << 1) <= i32_load(var0 + 5200) else 0):
                continue
            break  # end loop
        var8 = (var7 + 1)
        i32_store(((var0 + (var2 << 2)) + 2908), var7)
        var3 = i32_load(var0 + 5200)
        if (1 if i32_load(var0 + 5200) > 1 else 0):
            continue
        break  # end loop
    var2 = (i32_load(var0 + 5204) - 1)
    i32_store(var0 + 5204, (i32_load(var0 + 5204) - 1))
    var4 = (var0 + 2908)
    i32_store(((var0 + 2908) + (var2 << 2)), i32_load(var0 + 2912))
    var5 = i32_load(var1 + 4)
    var2 = i32_load(var1 + 8)
    var3 = i32_load(i32_load(var1 + 8) + 16)
    var11 = i32_load(var2 + 8)
    var16 = i32_load(var2 + 4)
    var12 = i32_load(var2)
    var7 = i32_load(var1)
    var17 = (var0 + 2900)
    i64_store((var0 + 2900), 0)
    var18 = (var0 + 2892)
    i64_store((var0 + 2892), 0)
    var19 = (var0 + 2884)
    i64_store((var0 + 2884), 0)
    var20 = (var0 + 2876)
    i64_store((var0 + 2876), 0)
    var8 = 0
    i32_store16((var7 + (i32_load((var4 + (i32_load(var0 + 5204) << 2))) << 2)) + 2, 0)
    var1 = i32_load(var0 + 5204)
    if (1 if i32_load(var0 + 5204) > 571 else 0):
        break
    var2 = (var1 + 1)
    var4 = 0
    while True:  # loop $label20
        var1 = i32_load(((var0 + (var2 << 2)) + 2908))
        var21 = (i32_load(((var0 + (var2 << 2)) + 2908)) << 2)
        var13 = (var7 + (i32_load(((var0 + (var2 << 2)) + 2908)) << 2))
        var6 = i32_load16_u((var7 + (i32_load16_u(var13 + 2) << 2)) + 2)
        var22 = (1 if var3 <= var6 else 0)
        var15 = (var3 if (1 if var3 <= var6 else 0) else (i32_load16_u((var7 + (i32_load16_u(var13 + 2) << 2)) + 2) + 1))
        i32_store16((var7 + (i32_load(((var0 + (var2 << 2)) + 2908)) << 2)) + 2, (var3 if (1 if var3 <= var6 else 0) else (i32_load16_u((var7 + (i32_load16_u(var13 + 2) << 2)) + 2) + 1)))
        if (1 if var1 > var5 else 0):
            break
        var6 = ((var0 + (var15 << 1)) + 2876)
        i32_store16(((var0 + (var15 << 1)) + 2876), (i32_load16_u(var6) + 1))
        var6 = 0
        if (1 if var1 >= var11 else 0):
            var6 = i32_load((var16 + ((var1 - var11) << 2)))
        var1 = i32_load16_u(var13)
        i32_store(var0 + 5800, (i32_load(var0 + 5800) + (i32_load16_u(var13) * (var6 + var15))))
        if (1 if var12 == 0 else 0):
            break
        i32_store(var0 + 5804, (i32_load(var0 + 5804) + ((var6 + i32_load16_u((var12 + var21) + 2)) * var1)))
        var4 = (var4 + var22)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != 573 else 0):
            continue
        break  # end loop
    if (1 if var4 == 0 else 0):
        break
    var6 = ((var0 + (var3 << 1)) + 2876)
    while True:  # loop $label22
        var2 = var3
        while True:  # loop $label21
            var1 = var2
            var2 = (var2 - 1)
            var11 = ((var0 + ((var2 - 1) << 1)) + 2876)
            var12 = i32_load16_u(((var0 + ((var2 - 1) << 1)) + 2876))
            if (1 if i32_load16_u(((var0 + ((var2 - 1) << 1)) + 2876)) == 0 else 0):
                continue
            break  # end loop
        i32_store16(var11, (var12 - 1))
        var1 = ((var0 + (var1 << 1)) + 2876)
        i32_store16(((var0 + (var1 << 1)) + 2876), (i32_load16_u(var1) + 2))
        i32_store16(var6, (i32_load16_u(var6) - 1))
        var1 = (1 if var4 > 2 else 0)
        var4 = (var4 - 2)
        if var1:
            continue
        break  # end loop
    if (1 if var3 == 0 else 0):
        break
    var2 = 573
    while True:  # loop $label24
        var4 = i32_load16_u(((var0 + (var3 << 1)) + 2876))
        if i32_load16_u(((var0 + (var3 << 1)) + 2876)):
            while True:  # loop $label23
                var2 = (var2 - 1)
                var1 = i32_load(((var0 + ((var2 - 1) << 2)) + 2908))
                if (1 if i32_load(((var0 + ((var2 - 1) << 2)) + 2908)) > var5 else 0):
                    continue
                var1 = (var7 + (var1 << 2))
                var6 = i32_load16_u((var7 + (var1 << 2)) + 2)
                if (1 if i32_load16_u((var7 + (var1 << 2)) + 2) != var3 else 0):
                    i32_store(var0 + 5800, (i32_load(var0 + 5800) + (i32_load16_u(var1) * (var3 - var6))))
                    i32_store16(var1 + 2, var3)
                var4 = (var4 - 1)
                if (var4 - 1):
                    continue
                break  # end loop
        var3 = (var3 - 1)
        if (var3 - 1):
            continue
        break  # end loop
    var1 = (i32_load16_u(var20) << 1)
    i32_store16(var10 + 2, (i32_load16_u(var20) << 1))
    var1 = ((var1 + i32_load16_u((var0 + 2878))) << 1)
    i32_store16(var10 + 4, ((var1 + i32_load16_u((var0 + 2878))) << 1))
    var1 = ((var1 + i32_load16_u((var0 + 2880))) << 1)
    i32_store16(var10 + 6, ((var1 + i32_load16_u((var0 + 2880))) << 1))
    var1 = ((var1 + i32_load16_u((var0 + 2882))) << 1)
    i32_store16(var10 + 8, ((var1 + i32_load16_u((var0 + 2882))) << 1))
    var1 = ((var1 + i32_load16_u(var19)) << 1)
    i32_store16(var10 + 10, ((var1 + i32_load16_u(var19)) << 1))
    var1 = ((var1 + i32_load16_u((var0 + 2886))) << 1)
    i32_store16(var10 + 12, ((var1 + i32_load16_u((var0 + 2886))) << 1))
    var1 = ((var1 + i32_load16_u((var0 + 2888))) << 1)
    i32_store16(var10 + 14, ((var1 + i32_load16_u((var0 + 2888))) << 1))
    var1 = ((var1 + i32_load16_u((var0 + 2890))) << 1)
    i32_store16(var10 + 16, ((var1 + i32_load16_u((var0 + 2890))) << 1))
    var1 = ((var1 + i32_load16_u(var18)) << 1)
    i32_store16(var10 + 18, ((var1 + i32_load16_u(var18)) << 1))
    var1 = ((var1 + i32_load16_u((var0 + 2894))) << 1)
    i32_store16(var10 + 20, ((var1 + i32_load16_u((var0 + 2894))) << 1))
    var1 = ((var1 + i32_load16_u((var0 + 2896))) << 1)
    i32_store16(var10 + 22, ((var1 + i32_load16_u((var0 + 2896))) << 1))
    var1 = ((var1 + i32_load16_u((var0 + 2898))) << 1)
    i32_store16(var10 + 24, ((var1 + i32_load16_u((var0 + 2898))) << 1))
    var1 = ((i32_load16_u(var17) + var1) << 1)
    i32_store16(var10 + 26, ((i32_load16_u(var17) + var1) << 1))
    var1 = ((i32_load16_u((var0 + 2902)) + var1) << 1)
    i32_store16(var10 + 28, ((i32_load16_u((var0 + 2902)) + var1) << 1))
    i32_store16(var10 + 30, ((var1 + i32_load16_u((var0 + 2904))) << 1))
    if (1 if var14 >= 0 else 0):
        while True:  # loop $label28
            var7 = (var9 + (var8 << 2))
            var0 = i32_load16_u((var9 + (var8 << 2)) + 2)
            if i32_load16_u((var9 + (var8 << 2)) + 2):
                var1 = (var10 + (var0 << 1))
                var2 = i32_load16_u(var1)
                i32_store16((var10 + (var0 << 1)), (i32_load16_u(var1) + 1))
                var1 = (var0 & 3)
                var3 = 0
                if (1 if var0 < 4 else 0):
                    var0 = 0
                    break
                var6 = (var0 & 65532)
                var0 = 0
                var4 = 0
                while True:  # loop $label26
                    var5 = ((((var2 & 0xFFFFFFFF) >> 3) & 1) | (((((var2 & 0xFFFFFFFF) >> 2) & 1) | ((var2 & 2) | ((var0 | (var2 & 1)) << 2))) << 1))
                    var0 = (((((var2 & 0xFFFFFFFF) >> 3) & 1) | (((((var2 & 0xFFFFFFFF) >> 2) & 1) | ((var2 & 2) | ((var0 | (var2 & 1)) << 2))) << 1)) << 1)
                    var2 = ((var2 & 0xFFFFFFFF) >> 4)
                    var4 = (var4 + 4)
                    if (1 if (var4 + 4) != var6 else 0):
                        continue
                    break  # end loop
                if var1:
                    while True:  # loop $label27
                        var5 = (var0 | (var2 & 1))
                        var0 = ((var0 | (var2 & 1)) << 1)
                        var2 = ((var2 & 0xFFFFFFFF) >> 1)
                        var3 = (var3 + 1)
                        if (1 if (var3 + 1) != var1 else 0):
                            continue
                        break  # end loop
                i32_store16(var7, var5)
            var0 = (1 if var8 != var14 else 0)
            var8 = (var8 + 1)
            if var0:
                continue
            break  # end loop
    return 0  # Stack underflow

