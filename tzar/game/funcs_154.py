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
# $func770
# ==========================================================
def func770(var0, var1, var2):
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
    var23 = 0
    var24 = 0
    var25 = 0
    var26 = 0.0
    var27 = 0.0
    var28 = 0.0
    var29 = 0.0
    var30 = 0.0
    if (1 if var2 == 0 else 0):
        break
    if (1 if i32_load(var0) == 0 else 0):
        break
    var0 = 0
    while True:  # loop $label29
        var12 = (i32_load(9671128) + (i32_load((var1 + (var0 << 2))) * 132))
        if (1 if i32_load8_u((i32_load(9671128) + (i32_load((var1 + (var0 << 2))) * 132)) + 129) != 8 else 0):
            var3 = 0
            var4 = 0
            var14 = 0
            if (1 if i32_load8_u(var12 + 129) == 8 else 0):
                break
            if (1 if i32_load8_u(var12 + 125) == 3 else 0):
                break
            var6 = 5
            var7 = i32_load8_u(var12 + 122)
            if (1 if i32_load8_u(var12 + 122) == i32_load(38604) else 0):
                break
            if (1 if i32_load(38624) == var7 else 0):
                break
            var15 = -1
            if (1 if var7 == i32_load(38608) else 0):
                var4 = 1
                break
            if (1 if var7 == i32_load(38628) else 0):
                break
            var6 = 4
            var14 = -1
            var3 = 1
            if (1 if i32_load(38612) == var7 else 0):
                break
            if (1 if i32_load(38632) == var7 else 0):
                break
            if (1 if i32_load(38616) == var7 else 0):
                break
            if (1 if i32_load(39056) == var7 else 0):
                break
            var3 = 0
            var15 = 0
            break
            var14 = 1
            break
            var15 = 0
            break
            var14 = 0
            var6 = 5
            break
            var15 = 1
            var4 = 1
            var9 = 2
            var13 = i32_load(9142840)
            var8 = i32_load16_u(var12 + 112)
            var18 = (var14 + 1)
            var17 = (var4 * var9)
            var5 = (i32_load(9142440) + 2)
            var16 = ((var7 * 404) + 9568096)
            var10 = ((i32_load(9142440) + 2) * i32_load(((var7 * 404) + 9568096) + 208))
            var11 = i32_load16_u(var12 + 114)
            var19 = (var15 + 1)
            var20 = (var3 * var9)
            var16 = i32_load(var16 + 212)
            if (1 if i32_load((i32_load(9142840) + (((i32_load16_u(var12 + 112) + ((var14 + 1) + (var4 * var9))) + ((((i32_load(9142440) + 2) * i32_load(((var7 * 404) + 9568096) + 208)) + (i32_load16_u(var12 + 114) + ((var15 + 1) + (var3 * var9)))) * var5)) << 2))) != i32_load(var16 + 212) else 0):
                break
            var21 = (var9 + 1)
            if (1 if (var9 + 1) == var6 else 0):
                break
            if (1 if i32_load((var13 + ((((var18 + (var4 * var21)) + var8) + ((((var19 + (var3 * var21)) + var11) + var10) * var5)) << 2))) != var16 else 0):
                break
            var21 = (var9 + 2)
            if (1 if (var9 + 2) == var6 else 0):
                break
            if (1 if i32_load((var13 + ((((var18 + (var4 * var21)) + var8) + ((((var19 + (var3 * var21)) + var11) + var10) * var5)) << 2))) != var16 else 0):
                break
            var21 = (var9 + 3)
            if (1 if (var9 + 3) == var6 else 0):
                break
            if (1 if i32_load((var13 + ((((var18 + (var4 * var21)) + var8) + ((((var19 + (var3 * var21)) + var11) + var10) * var5)) << 2))) != var16 else 0):
                break
            var18 = ((var14 << 1) | 1)
            var15 = ((var15 << 1) | 1)
            if (1 if i32_load((var13 + ((((((var14 << 1) | 1) + var17) + var8) + ((((((var15 << 1) | 1) + var20) + var11) + var10) * var5)) << 2))) != var16 else 0):
                break
            var14 = (var9 + 1)
            if (1 if (var9 + 1) == var6 else 0):
                break
            if (1 if i32_load((var13 + ((((var18 + (var4 * var14)) + var8) + ((((var15 + (var3 * var14)) + var11) + var10) * var5)) << 2))) != var16 else 0):
                break
            var19 = (var9 + 2)
            if (1 if (var9 + 2) == var6 else 0):
                break
            if (1 if i32_load((var13 + ((((var18 + (var4 * var19)) + var8) + ((((var15 + (var3 * var19)) + var11) + var10) * var5)) << 2))) != var16 else 0):
                break
            var19 = (var9 + 3)
            if (1 if (var9 + 3) == var6 else 0):
                break
            if (1 if i32_load((var13 + ((((var18 + (var4 * var19)) + var8) + ((((var15 + (var3 * var19)) + var11) + var10) * var5)) << 2))) != var16 else 0):
                break
            var5 = (i32_load(9142440) + 2)
            var7 = ((var7 * 404) + 9568096)
            i32_store(((((var8 + var17) + ((((var11 + var20) + ((i32_load(9142440) + 2) * i32_load(((var7 * 404) + 9568096) + 208))) + 1) * var5)) << 2) + var13) + 4, i32_load(var7 + 212))
            if (1 if var6 == var14 else 0):
                break
            var5 = (i32_load(9142440) + 2)
            i32_store((((((var4 * var14) + var8) + (((((var3 * var14) + var11) + ((i32_load(9142440) + 2) * i32_load(var7 + 208))) + 1) * var5)) << 2) + var13) + 4, i32_load(var7 + 212))
            var5 = (var9 + 2)
            if (1 if (var9 + 2) == var6 else 0):
                break
            var5 = (i32_load(9142440) + 2)
            i32_store((((((var4 * var5) + var8) + (((((var3 * var5) + var11) + ((i32_load(9142440) + 2) * i32_load(var7 + 208))) + 1) * var5)) << 2) + var13) + 4, i32_load(var7 + 212))
            var6 = (var9 + 3)
            if (1 if var6 == (var9 + 3) else 0):
                break
            var3 = (i32_load(9142440) + 2)
            i32_store((((((var4 * var6) + var8) + (((((var3 * var6) + var11) + ((i32_load(9142440) + 2) * i32_load(var7 + 208))) + 1) * var3)) << 2) + var13) + 4, i32_load(var7 + 212))
            i32_store8(var12 + 129, 8)
            if (1 if i32_load(var12 + 92) == 0 else 0):
                break
            var3 = i32_load8_u(9147141)
            if i32_load(9140316):
                if (1 if i32_load(9140320) != i32_load(var12 + 28) else 0):
                    break
            break
        var3 = 0
        var6 = 0
        var15 = 0
        var13 = (global0 - 112)
        global global0
        global0 = (global0 - 112)
        if (1 if i32_load8_u(var12 + 129) != 8 else 0):
            break
        if (1 if i32_load8_u(var12 + 125) == 3 else 0):
            break
        var14 = i32_load8_u(var12 + 122)
        var19 = ((i32_load8_u(var12 + 122) * 404) + 9568096)
        var8 = 5
        if (1 if i32_load(38604) == var14 else 0):
            break
        if (1 if i32_load(38624) == var14 else 0):
            break
        var18 = -1
        if (1 if var14 == i32_load(38608) else 0):
            var6 = 1
            break
        if (1 if var14 == i32_load(38628) else 0):
            break
        var8 = 4
        var15 = -1
        var3 = 1
        if (1 if i32_load(38612) == var14 else 0):
            break
        if (1 if i32_load(38632) == var14 else 0):
            break
        if (1 if i32_load(38616) == var14 else 0):
            break
        if (1 if i32_load(39056) == var14 else 0):
            break
        var3 = 0
        var18 = 0
        break
        var15 = 1
        break
        var18 = 0
        break
        var15 = 0
        var8 = 5
        break
        var18 = 1
        var6 = 1
        var7 = 2
        var10 = i32_load(var19 + 212)
        var4 = i32_load(9142840)
        var21 = (var6 * var7)
        var11 = i32_load16_u(var12 + 112)
        var24 = ((var6 * var7) + i32_load16_u(var12 + 112))
        var23 = (var3 * var7)
        var9 = i32_load16_u(var12 + 114)
        var25 = ((var3 * var7) + i32_load16_u(var12 + 114))
        var5 = (i32_load(9142440) + 2)
        var16 = ((i32_load(9142440) + 2) * i32_load(var19 + 208))
        if (1 if i32_load(var19 + 212) != i32_load((i32_load(9142840) + ((((var6 * var7) + i32_load16_u(var12 + 112)) + (((((var3 * var7) + i32_load16_u(var12 + 114)) + ((i32_load(9142440) + 2) * i32_load(var19 + 208))) + 1) * var5)) << 2)) + 4) else 0):
            break
        var17 = (var7 + 1)
        if (1 if (var7 + 1) == var8 else 0):
            break
        if (1 if i32_load((((((var6 * var17) + var11) + (((((var3 * var17) + var9) + var16) + 1) * var5)) << 2) + var4) + 4) != var10 else 0):
            break
        var17 = (var7 + 2)
        if (1 if (var7 + 2) == var8 else 0):
            break
        if (1 if i32_load((((((var6 * var17) + var11) + (((((var3 * var17) + var9) + var16) + 1) * var5)) << 2) + var4) + 4) != var10 else 0):
            break
        var17 = (var7 + 3)
        if (1 if (var7 + 3) == var8 else 0):
            break
        if (1 if i32_load((((((var6 * var17) + var11) + (((((var3 * var17) + var9) + var16) + 1) * var5)) << 2) + var4) + 4) != var10 else 0):
            break
        var17 = (var15 + 1)
        var20 = (var18 + 1)
        if (1 if i32_load((var4 + (((((var15 + 1) + var21) + var11) + (((((var18 + 1) + var23) + var9) + var16) * var5)) << 2))) != var10 else 0):
            break
        var22 = (var7 + 1)
        if (1 if (var7 + 1) == var8 else 0):
            break
        if (1 if i32_load((var4 + ((((var17 + (var6 * var22)) + var11) + ((((var20 + (var3 * var22)) + var9) + var16) * var5)) << 2))) != var10 else 0):
            break
        var22 = (var7 + 2)
        if (1 if (var7 + 2) == var8 else 0):
            break
        if (1 if i32_load((var4 + ((((var17 + (var6 * var22)) + var11) + ((((var20 + (var3 * var22)) + var9) + var16) * var5)) << 2))) != var10 else 0):
            break
        var22 = (var7 + 3)
        if (1 if (var7 + 3) == var8 else 0):
            break
        if (1 if i32_load((var4 + ((((var17 + (var6 * var22)) + var11) + ((((var20 + (var3 * var22)) + var9) + var16) * var5)) << 2))) != var10 else 0):
            break
        var17 = ((var15 << 1) | 1)
        var18 = ((var18 << 1) | 1)
        if (1 if i32_load((var4 + ((((((var15 << 1) | 1) + var21) + var11) + ((((((var18 << 1) | 1) + var23) + var9) + var16) * var5)) << 2))) != var10 else 0):
            break
        var15 = (var7 + 1)
        if (1 if (var7 + 1) == var8 else 0):
            break
        if (1 if i32_load((var4 + ((((var17 + (var6 * var15)) + var11) + ((((var18 + (var3 * var15)) + var9) + var16) * var5)) << 2))) != var10 else 0):
            break
        var20 = (var7 + 2)
        if (1 if (var7 + 2) == var8 else 0):
            break
        if (1 if i32_load((var4 + ((((var17 + (var6 * var20)) + var11) + ((((var18 + (var3 * var20)) + var9) + var16) * var5)) << 2))) != var10 else 0):
            break
        var20 = (var7 + 3)
        if (1 if (var7 + 3) == var8 else 0):
            break
        if (1 if i32_load((var4 + ((((var17 + (var6 * var20)) + var11) + ((((var18 + (var3 * var20)) + var9) + var16) * var5)) << 2))) != var10 else 0):
            break
        var10 = (i32_load(9142440) + 2)
        var5 = ((var14 * 404) + 9568096)
        i32_store((((var24 + (((var25 + ((i32_load(9142440) + 2) * i32_load(((var14 * 404) + 9568096) + 208))) + 1) * var10)) << 2) + var4) + 4, i32_load(var12 + 28))
        if (1 if var8 == var15 else 0):
            break
        var10 = (i32_load(9142440) + 2)
        i32_store((((((var6 * var15) + var11) + (((((var3 * var15) + var9) + ((i32_load(9142440) + 2) * i32_load(var5 + 208))) + 1) * var10)) << 2) + var4) + 4, i32_load(var12 + 28))
        var10 = (var7 + 2)
        if (1 if (var7 + 2) == var8 else 0):
            break
        var10 = (i32_load(9142440) + 2)
        i32_store((((((var6 * var10) + var11) + (((((var3 * var10) + var9) + ((i32_load(9142440) + 2) * i32_load(var5 + 208))) + 1) * var10)) << 2) + var4) + 4, i32_load(var12 + 28))
        var8 = (var7 + 3)
        if (1 if var8 == (var7 + 3) else 0):
            break
        var3 = (i32_load(9142440) + 2)
        i32_store((((((var6 * var8) + var11) + (((((var3 * var8) + var9) + ((i32_load(9142440) + 2) * i32_load(var5 + 208))) + 1) * var3)) << 2) + var4) + 4, i32_load(var12 + 28))
        var3 = i32_load(var12 + 12)
        if (1 if i32_load(var12 + 12) == 0 else 0):
            break
        var8 = i32_load(i32_load(var3))
        if (1 if i32_load(i32_load(var3)) == 0 else 0):
            break
        if (1 if i32_load(var12 + 40) == 0 else 0):
            break
        var4 = i32_load(var19)
        var3 = 0
        if i32_load8_u(9142916):
            if (1 if var4 == 0 else 0):
                break
            if (1 if i32_load(var4 + 20) == 0 else 0):
                break
            var11 = i32_load8_u(var12 + 124)
            var3 = i32_load(var4 + 28)
            if (1 if i32_load(var4 + 28) == 2147483647 else 0):
                var3 = i32_load(59152)
                i32_store(59152, (i32_load(59152) + 1))
                var9 = i32_load(9568052)
                i32_store(var4 + 28, var3)
                var7 = i32_load(var4)
                var6 = i32_load(var4 + 4)
                var5 = i32_load(9568048)
                i32_store(9568048, (i32_load(9568048) + 1))
                i32_store(((var5 << 2) + 9563952), var4)
                i32_store(9568052, (var9 + ((var7 * (var6 + 2)) << 2)))
                var9 = i32_load(9568056)
                i32_store(var4 + 56, i32_load(9568056))
                i32_store(9568056, (var9 + ((var6 * i32_load(var4)) << 2)))
            var3 = (var3 + (var11 << 16))
            i32_store(var13 + 96, var8)
            i64_store(var13 + 88, -4616189618054758400)
            i32_store(var13 + 80, var3)
            a_b()
            break
        var11 = (i32_load(var4 + 16) << 16)
        var9 = i32_load(var4 + 20)
        if i32_load(var4 + 20):
            var7 = i32_load8_u(var12 + 124)
            var3 = i32_load(var4 + 28)
            if (1 if i32_load(var4 + 28) != 2147483647 else 0):
                var6 = i32_load(var4 + 4)
                break
            var5 = i32_load(var4)
            var10 = i32_load(9568052)
            var3 = ((i32_load(var4) + i32_load(9140308)) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2))
            i32_store(var4 + 28, ((i32_load(var4) + i32_load(9140308)) + ((i32_load(9568052) & 0xFFFFFFFF) >> 2)))
            var6 = i32_load(var4 + 4)
            i32_store(9568052, (var10 + ((var5 * (i32_load(var4 + 4) + 2)) << 2)))
            var5 = i32_load(9568048)
            i32_store(9568048, (i32_load(9568048) + 1))
            i32_store(((var5 << 2) + 9563952), var4)
        else:
        var26 = 0.0
        var3 = i32_load16_u(var12 + 110)
        f64_store(var13 + 56, float(var11))
        i32_store((var13 - -64), var8)
        i32_store(var13 + 48, (var3 + 16))
        f64_store(var13 + 32, float((var26 / float(i32_load(59156)))))
        f64_store(var13 + 40, float(float((i32_load(9142848) * 25))))
        a_b()
        var27 = (float(i32_load16_u(var12 + 112)) * 32.0)
        var3 = i32_load8_u(9142916)
        var28 = float(i32_load(var4 + 12))
        var29 = float(i32_load(var4 + 8))
        var30 = (float(i32_load16_u(var12 + 114)) * 32.0)
        var4 = i32_load(9142440)
        var26 = ((float(i32_load16_u(var12 + 114)) * 32.0) + (float(i32_load(9142440)) * 32.0))
        if (1 if ((float(i32_load16_u(var12 + 114)) * 32.0) + (float(i32_load(9142440)) * 32.0)) == -55.0 else 0):
            break
        if (1 if var3 == 0 else 0):
            break
        var26 = (((var26 * 0.5) / float((var4 * 96))) + 0.25)
        i32_store(var13 + 24, var8)
        f64_store(var13 + 16, float(var26))
        f64_store(var13 + 8, float((var30 - (0.0 if var3 else var28))))
        f64_store(var13, float((var27 - (0.0 if var3 else var29))))
        a_b()
        i32_store8(var12 + 129, 0)
        if (1 if i32_load(var12 + 92) == 0 else 0):
            break
        var3 = i32_load8_u(9147141)
        if i32_load(9140316):
            if (1 if i32_load(9140320) != i32_load(var12 + 28) else 0):
                break
        global global0
        global0 = (var13 + 112)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var2 else 0):
            continue
        break  # end loop
    return func28((1 if var3 != 0 else 0), 1)

