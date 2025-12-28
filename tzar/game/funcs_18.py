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
# $func273
# ==========================================================
def func273(var0, var1, param2, param3, param4, param5):
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
    var3 = i32_load(var1)
    var10 = i32_load(var1 + 4)
    var2 = i32_load(var0 + 2308)
    i32_store8(i32_load(var0 + 2308) + 823, 129)
    i32_store8(var2 + 807, 129)
    i32_store8(var2 + 791, 129)
    i32_store8(var2 + 775, 129)
    i32_store8(var2 + 759, 129)
    i32_store8(var2 + 743, 129)
    i32_store8(var2 + 727, 129)
    i32_store8(var2 + 711, 129)
    i32_store8(var2 + 695, 129)
    i32_store8(var2 + 679, 129)
    i32_store8(var2 + 663, 129)
    i32_store8(var2 + 647, 129)
    i32_store8(var2 + 631, 129)
    i32_store8(var2 + 615, 129)
    i32_store8(var2 + 599, 129)
    i32_store8(var2 + 583, 129)
    i32_store8(var2 + 519, 129)
    i32_store8(var2 + 487, 129)
    i32_store8(var2 + 455, 129)
    i32_store8(var2 + 423, 129)
    i32_store8(var2 + 391, 129)
    i32_store8(var2 + 359, 129)
    i32_store8(var2 + 327, 129)
    i32_store8(var2 + 295, 129)
    i32_store8(var2 + 263, 129)
    i32_store8(var2 + 231, 129)
    i32_store8(var2 + 199, 129)
    i32_store8(var2 + 167, 129)
    i32_store8(var2 + 135, 129)
    i32_store8(var2 + 103, 129)
    i32_store8(var2 + 71, 129)
    i32_store8(var2 + 39, 129)
    if (1 if var10 > 0 else 0):
        i32_store8(var2 + 551, 129)
        i32_store8(var2 + 567, 129)
        i32_store8(var2 + 7, 129)
        break
    i64_store(var2 + 7, 9187201950435737471)
    i64_store(var2 + 20, 9187201950435737471)
    i64_store(var2 + 15, 9187201950435737471)
    i32_store8(var2 + 559, 127)
    i64_store(var2 + 551, 9187201950435737471)
    i32_store8(var2 + 575, 127)
    i64_store(var2 + 567, 9187201950435737471)
    if (1 if i32_load(var0 + 300) > 0 else 0):
        var12 = (var2 + 600)
        var13 = (var2 + 584)
        var11 = (var2 + 40)
        var14 = (5 if var10 else 6)
        var17 = (var3 << 3)
        var18 = (var3 << 4)
        var15 = ((1 if var10 == 0 else 0) << 2)
        var19 = (1 if var10 <= 0 else 0)
        while True:  # loop $label15
            var5 = (i32_load(var1 + 16) + (var8 * 800))
            if var8:
                i32_store(var2 + 4, i32_load(var2 + 20))
                i32_store(var2 + 36, i32_load(var2 + 52))
                i32_store(var2 + 68, i32_load(var2 + 84))
                i32_store(var2 + 100, i32_load(var2 + 116))
                i32_store(var2 + 132, i32_load(var2 + 148))
                i32_store(var2 + 164, i32_load(var2 + 180))
                i32_store(var2 + 196, i32_load(var2 + 212))
                i32_store(var2 + 228, i32_load(var2 + 244))
                i32_store(var2 + 260, i32_load(var2 + 276))
                i32_store(var2 + 292, i32_load(var2 + 308))
                i32_store(var2 + 324, i32_load(var2 + 340))
                i32_store(var2 + 356, i32_load(var2 + 372))
                i32_store(var2 + 388, i32_load(var2 + 404))
                i32_store(var2 + 420, i32_load(var2 + 436))
                i32_store(var2 + 452, i32_load(var2 + 468))
                i32_store(var2 + 484, i32_load(var2 + 500))
                i32_store(var2 + 516, i32_load(var2 + 532))
                i32_store(var2 + 548, i32_load(var2 + 556))
                i32_store(var2 + 564, i32_load(var2 + 572))
                i32_store(var2 + 580, i32_load(var2 + 588))
                i32_store(var2 + 596, i32_load(var2 + 604))
                i32_store(var2 + 612, i32_load(var2 + 620))
                i32_store(var2 + 628, i32_load(var2 + 636))
                i32_store(var2 + 644, i32_load(var2 + 652))
                i32_store(var2 + 660, i32_load(var2 + 668))
                i32_store(var2 + 676, i32_load(var2 + 684))
                i32_store(var2 + 692, i32_load(var2 + 700))
                i32_store(var2 + 708, i32_load(var2 + 716))
                i32_store(var2 + 724, i32_load(var2 + 732))
                i32_store(var2 + 740, i32_load(var2 + 748))
                i32_store(var2 + 756, i32_load(var2 + 764))
                i32_store(var2 + 772, i32_load(var2 + 780))
                i32_store(var2 + 788, i32_load(var2 + 796))
                i32_store(var2 + 804, i32_load(var2 + 812))
                i32_store(var2 + 820, i32_load(var2 + 828))
            var7 = (i32_load(var0 + 2296) + (var8 << 5))
            var6 = i32_load(var5 + 788)
            if (1 if var19 == 0 else 0):
                i64_store(var2 + 8, i64_load(var7))
                i64_store(var2 + 16, i64_load(var7 + 8))
                i64_store(var2 + 552, i64_load(var7 + 16))
                i64_store(var2 + 568, i64_load(var7 + 24))
                if i32_load8_u(var5 + 768):
                    break
                break
            if (1 if i32_load8_u(var5 + 768) == 0 else 0):
                break
            var3 = i32_load(var2 + 24)
            break
            if (1 if (i32_load(var0 + 300) - 1) <= var8 else 0):
                var3 = i32_load8_u(var7 + 15)
                i32_store(var2 + 24, (i32_load8_u(var7 + 15) * 16843009))
                var3 = (var3 | (var3 << 8))
                var3 = ((var3 | (var3 << 8)) | (var3 << 16))
                break
            var3 = i32_load(var7 + 32)
            i32_store(var2 + 24, i32_load(var7 + 32))
            i32_store(var2 + 280, var3)
            i32_store(var2 + 408, var3)
            i32_store(var2 + 152, var3)
            var3 = 0
            while True:  # loop $label8
                var4 = (var11 + i32_load16_u(((var3 << 1) + 10336)))
                # call_indirect via table[i32_load(((i32_load8_u((var3 + var5) + 769) << 2) + 9687376))]
                var9 = (var5 + (var3 << 5))
                # br_table ['$label4', '$label5', '$label6', '$label7']
                _br_idx = (((var6 & 0xFFFFFFFF) >> 30) - 1)
                break  # br_table
                # call_indirect via table[i32_load(9687452)]
                break
                # call_indirect via table[i32_load(9687456)]
                break
                # call_indirect via table[i32_load(9687464)]
                var6 = (var6 << 2)
                var3 = (var3 + 1)
                if (1 if (var3 + 1) != 16 else 0):
                    continue
                break  # end loop
            var16 = (var15 if var8 else var14)
            break
            var3 = i32_load8_u(var5 + 769)
            var16 = (var15 if var8 else var14)
            # call_indirect via table[i32_load((((i32_load8_u(var5 + 769) if var3 else (var15 if var8 else var14)) << 2) + 9687344))]
            var3 = 0
            if (1 if var6 == 0 else 0):
                break
            while True:  # loop $label14
                var4 = (var5 + (var3 << 5))
                var9 = (var11 + i32_load16_u(((var3 << 1) + 10336)))
                # br_table ['$label10', '$label11', '$label12', '$label13']
                _br_idx = (((var6 & 0xFFFFFFFF) >> 30) - 1)
                break  # br_table
                # call_indirect via table[i32_load(9687452)]
                break
                # call_indirect via table[i32_load(9687456)]
                break
                # call_indirect via table[i32_load(9687464)]
                var6 = (var6 << 2)
                var3 = (var3 + 1)
                if (1 if (var3 + 1) != 16 else 0):
                    continue
                break  # end loop
            var3 = i32_load(var5 + 792)
            var6 = i32_load8_u(var5 + 785)
            var6 = (((i32_load8_u(var5 + 785) if var6 else var16) << 2) + 9687424)
            # call_indirect via table[i32_load((((i32_load8_u(var5 + 785) if var6 else var16) << 2) + 9687424))]
            # call_indirect via table[i32_load(var6)]
            if (var3 & 255):
                # call_indirect via table[i32_load((9687460 if (var3 & 170) else 9687468))]
            if (var3 & 65280):
                # call_indirect via table[i32_load((9687460 if (var3 & 43520) else 9687468))]
            if (1 if (i32_load(var0 + 304) - 1) > var10 else 0):
                i64_store(var7, i64_load(var2 + 520))
                i64_store(var7 + 8, i64_load(var2 + 528))
                i64_store(var7 + 16, i64_load(var2 + 808))
                i64_store(var7 + 24, i64_load(var2 + 824))
            var5 = i32_load(var0 + 2320)
            var7 = i32_load(var0 + 2316)
            var6 = i32_load(var0 + 2328)
            var3 = ((i32_load(var0 + 2312) + (var8 << 4)) + (var18 * i32_load(var0 + 2324)))
            i64_store(((i32_load(var0 + 2312) + (var8 << 4)) + (var18 * i32_load(var0 + 2324))), i64_load(var11))
            i64_store(var3 + 8, i64_load(var11 + 8))
            var4 = (var3 + i32_load(var0 + 2324))
            i64_store((var3 + i32_load(var0 + 2324)), i64_load(var2 + 72))
            i64_store(var4 + 8, i64_load(var2 + 80))
            var4 = (var3 + (i32_load(var0 + 2324) << 1))
            i64_store((var3 + (i32_load(var0 + 2324) << 1)), i64_load(var2 + 104))
            i64_store(var4 + 8, i64_load(var2 + 112))
            var4 = (var3 + (i32_load(var0 + 2324) * 3))
            i64_store((var3 + (i32_load(var0 + 2324) * 3)), i64_load(var2 + 136))
            i64_store(var4 + 8, i64_load(var2 + 144))
            var4 = (var3 + (i32_load(var0 + 2324) << 2))
            i64_store((var3 + (i32_load(var0 + 2324) << 2)), i64_load(var2 + 168))
            i64_store(var4 + 8, i64_load(var2 + 176))
            var4 = (var3 + (i32_load(var0 + 2324) * 5))
            i64_store((var3 + (i32_load(var0 + 2324) * 5)), i64_load(var2 + 200))
            i64_store(var4 + 8, i64_load(var2 + 208))
            var4 = (var3 + (i32_load(var0 + 2324) * 6))
            i64_store((var3 + (i32_load(var0 + 2324) * 6)), i64_load(var2 + 232))
            i64_store(var4 + 8, i64_load(var2 + 240))
            var4 = (var3 + (i32_load(var0 + 2324) * 7))
            i64_store((var3 + (i32_load(var0 + 2324) * 7)), i64_load(var2 + 264))
            i64_store(var4 + 8, i64_load(var2 + 272))
            var4 = (var3 + (i32_load(var0 + 2324) << 3))
            i64_store((var3 + (i32_load(var0 + 2324) << 3)), i64_load(var2 + 296))
            i64_store(var4 + 8, i64_load(var2 + 304))
            var4 = (var3 + (i32_load(var0 + 2324) * 9))
            i64_store((var3 + (i32_load(var0 + 2324) * 9)), i64_load(var2 + 328))
            i64_store(var4 + 8, i64_load(var2 + 336))
            var4 = (var3 + (i32_load(var0 + 2324) * 10))
            i64_store((var3 + (i32_load(var0 + 2324) * 10)), i64_load(var2 + 360))
            i64_store(var4 + 8, i64_load(var2 + 368))
            var4 = (var3 + (i32_load(var0 + 2324) * 11))
            i64_store((var3 + (i32_load(var0 + 2324) * 11)), i64_load(var2 + 392))
            i64_store(var4 + 8, i64_load(var2 + 400))
            var4 = (var3 + (i32_load(var0 + 2324) * 12))
            i64_store((var3 + (i32_load(var0 + 2324) * 12)), i64_load(var2 + 424))
            i64_store(var4 + 8, i64_load(var2 + 432))
            var4 = (var3 + (i32_load(var0 + 2324) * 13))
            i64_store((var3 + (i32_load(var0 + 2324) * 13)), i64_load(var2 + 456))
            i64_store(var4 + 8, i64_load(var2 + 464))
            var4 = (var3 + (i32_load(var0 + 2324) * 14))
            i64_store((var3 + (i32_load(var0 + 2324) * 14)), i64_load(var2 + 488))
            i64_store(var4 + 8, i64_load(var2 + 496))
            var3 = (var3 + (i32_load(var0 + 2324) * 15))
            i64_store((var3 + (i32_load(var0 + 2324) * 15)), i64_load(var2 + 520))
            i64_store(var3 + 8, i64_load(var2 + 528))
            var6 = (var6 * var17)
            var4 = (var8 << 3)
            var3 = ((var6 * var17) + (var7 + (var8 << 3)))
            i64_store(((var6 * var17) + (var7 + (var8 << 3))), i64_load(var2 + 584))
            var5 = ((var4 + var5) + var6)
            i64_store(((var4 + var5) + var6), i64_load(var2 + 600))
            i64_store((var3 + i32_load(var0 + 2328)), i64_load(var2 + 616))
            i64_store((var5 + i32_load(var0 + 2328)), i64_load(var2 + 632))
            i64_store((var3 + (i32_load(var0 + 2328) << 1)), i64_load(var2 + 648))
            i64_store((var5 + (i32_load(var0 + 2328) << 1)), i64_load(var2 + 664))
            i64_store((var3 + (i32_load(var0 + 2328) * 3)), i64_load(var2 + 680))
            i64_store((var5 + (i32_load(var0 + 2328) * 3)), i64_load(var2 + 696))
            i64_store((var3 + (i32_load(var0 + 2328) << 2)), i64_load(var2 + 712))
            i64_store((var5 + (i32_load(var0 + 2328) << 2)), i64_load(var2 + 728))
            i64_store((var3 + (i32_load(var0 + 2328) * 5)), i64_load(var2 + 744))
            i64_store((var5 + (i32_load(var0 + 2328) * 5)), i64_load(var2 + 760))
            i64_store((var3 + (i32_load(var0 + 2328) * 6)), i64_load(var2 + 776))
            i64_store((var5 + (i32_load(var0 + 2328) * 6)), i64_load(var2 + 792))
            i64_store((var3 + (i32_load(var0 + 2328) * 7)), i64_load(var2 + 808))
            i64_store((var5 + (i32_load(var0 + 2328) * 7)), i64_load(var2 + 824))
            var8 = (var8 + 1)
            if (1 if (var8 + 1) < i32_load(var0 + 300) else 0):
                continue
            break  # end loop


# ==========================================================
# $func277
# ==========================================================
def func277(var0, var1, var2):
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
    var6 = i32_load(9142440)
    var7 = (i32_load(9142440) + 2)
    var8 = i32_load(39056)
    var9 = i32_load(38632)
    var10 = i32_load(38628)
    var11 = i32_load(38624)
    var12 = i32_load(38616)
    var13 = i32_load(38612)
    var14 = i32_load(38608)
    var15 = i32_load(38604)
    var16 = i32_load(38472)
    var17 = i32_load(38600)
    var18 = i32_load(9671128)
    var19 = i32_load(9142840)
    while True:  # loop $label2
        var4 = (var5 << 3)
        var3 = (i32_load(((var5 << 3) + 9172)) + var1)
        if (1 if var6 <= (i32_load(((var5 << 3) + 9172)) + var1) else 0):
            break
        var4 = (i32_load((var4 + 9168)) + var0)
        if (1 if var6 <= (i32_load((var4 + 9168)) + var0) else 0):
            break
        if (1 if (var3 | var4) < 0 else 0):
            break
        var3 = i32_load((((var4 + (((var3 + var7) + 1) * var7)) << 2) + var19) + 4)
        if (1 if i32_load((((var4 + (((var3 + var7) + 1) * var7)) << 2) + var19) + 4) < 3 else 0):
            break
        var3 = (var18 + (var3 * 132))
        if (1 if i32_load16_u((var18 + (var3 * 132)) + 110) != var2 else 0):
            break
        var4 = 1
        var3 = i32_load8_u(var3 + 122)
        if (1 if var17 == i32_load8_u(var3 + 122) else 0):
            break
        if (1 if var3 == var16 else 0):
            break
        if (1 if var3 == var15 else 0):
            break
        if (1 if var3 == var14 else 0):
            break
        if (1 if var3 == var13 else 0):
            break
        if (1 if var3 == var12 else 0):
            break
        if (1 if var3 == var11 else 0):
            break
        if (1 if var3 == var10 else 0):
            break
        if (1 if var3 == var9 else 0):
            break
        if (1 if var3 == var8 else 0):
            break
        var4 = 0
        i32_store8((var5 + 9147328), var4)
        var5 = (var5 + 1)
        if (1 if (var5 + 1) != 8 else 0):
            continue
        break  # end loop

