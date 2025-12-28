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
# $func688
# ==========================================================
def func688(var0):
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
    var26 = 0
    var27 = 0
    var28 = 0
    var29 = 0
    var30 = 0
    var31 = 0
    var32 = 0
    var33 = 0
    var34 = 0
    var35 = 0
    var36 = 0
    var37 = 0
    var38 = 0
    var39 = 0
    var40 = 0
    var41 = 0
    var42 = 0
    var43 = 0
    var44 = 0
    var45 = 0
    var46 = 0
    var47 = 0
    var48 = 0
    var49 = 0
    var50 = 0
    var51 = 0
    var52 = 0
    var53 = 0
    var54 = 0
    var55 = 0
    var56 = 0
    var57 = 0
    var58 = 0
    var59 = 0
    var60 = 0
    var61 = 0
    var62 = 0
    var63 = 0
    var64 = 0
    var65 = 0
    var66 = 0.0
    var67 = 0.0
    var68 = 0.0
    var69 = 0.0
    var70 = 0.0
    var71 = 0.0
    var72 = 0.0
    var73 = 0.0
    var74 = 0.0
    var75 = 0.0
    var76 = 0.0
    var77 = 0.0
    var78 = 0.0
    var79 = 0.0
    var80 = 0.0
    var81 = 0.0
    var82 = 0.0
    var83 = 0.0
    var84 = 0.0
    var85 = 0.0
    var86 = 0.0
    var87 = 0.0
    var88 = 0.0
    var89 = 0.0
    var90 = 0.0
    var91 = 0.0
    var92 = 0.0
    var93 = 0.0
    var94 = 0.0
    var95 = 0.0
    var96 = 0.0
    var97 = 0.0
    var98 = 0.0
    var99 = 0.0
    var100 = 0.0
    var101 = 0.0
    var102 = 0.0
    var103 = 0.0
    var104 = 0.0
    var105 = 0.0
    var106 = 0.0
    var107 = 0
    var0 = (global0 + -64)
    global global0
    global0 = (global0 + -64)
    var1 = i32_load(59160)
    var2 = i32_load(9142848)
    var53 = (1 if (i32_load(59160) - i32_load(9142848)) > 5 else 0)
    if (1 if var1 > var2 else 0):
        while True:  # loop $label607
            a_b()
            func152()
            if i32_load8_u(9140312):
                i32_store(51776, 1)
                while True:  # loop $label0
                    if i32_load(51776):
                        continue
                    break  # end loop
                func54(9684264)
            var2 = 0
            var4 = 0
            var5 = 0
            var13 = (global0 - 112)
            global global0
            global0 = (global0 - 112)
            var3 = i32_load8_u(9147210)
            if (1 if i32_load8_u(9147210) == 0 else 0):
                break
            var1 = i32_load(9142848)
            if (1 if i32_load(9142848) == 0 else 0):
                break
            if (1 if i32_load(9142872) == 0 else 0):
                break
            if ((var1 * 25) % 10000):
                break
            var1 = (global0 - 32)
            global global0
            global0 = (global0 - 32)
            var6 = i32_load(9142892)
            if (1 if i32_load(9142892) == 0 else 0):
                break
            var7 = i32_load(9682200)
            var10 = i32_load(9682204)
            var9 = i32_load(9142872)
            var16 = i32_load(9561692)
            while True:  # loop $label5
                if (1 if var5 == 0 else 0):
                    break
                if (1 if var5 == var9 else 0):
                    break
                var3 = (var16 + (var5 * 286704))
                if (1 if i32_load((var16 + (var5 * 286704)) + 284616) == 0 else 0):
                    break
                if i32_load8_u(var3 + 286699):
                    break
                if (1 if i32_load(var3 + 283932) != var10 else 0):
                    break
                if (1 if var7 == i32_load(var3 + 283928) else 0):
                    var2 = (var2 + 1)
                    break
                var2 = (var2 - 1)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var6 else 0):
                    continue
                break  # end loop
            if (1 if var2 >= 0 else 0):
                break
            a_b()
            i64_store(var1 + 8, 13)
            i64_store(var1, 532575944827)
            a_b()
            a_b()
            break
            var2 = cc()
            i32_store(9682200, cc())
            var5 = i32_load(9142848)
            i32_store(9682204, i32_load(9142848))
            i32_store(var1 + 28, var5)
            i32_store(var1 + 24, var2)
            if i32_load8_u(9147210):
                func41(20, 0, 0, (var1 + 24), 2)
                break
            # call_indirect via table[i32_load(9213984)]
            global global0
            global0 = (var1 + 32)
            var3 = i32_load8_u(9147210)
            if (1 if (var3 & 255) == 0 else 0):
                break
            if (1 if i32_load8_u(9216060) == 0 else 0):
                break
            var1 = i32_load(9142848)
            if (1 if i32_load(9142848) == 0 else 0):
                break
            if ((var1 * 25) % 60000):
                break
            if (1 if i32_load(9142872) == 0 else 0):
                break
            if i32_load8_u(9561832):
                break
            if i32_load8_u(9561801):
                i32_store(var13 + 80, i32_load(9142840))
                var1 = (i32_load(9142440) + 2)
                i32_store(var13 + 84, (((i32_load(9142440) + 2) * var1) * 3))
            var1 = i32_load(9568068)
            var2 = i32_load(9568064)
            if (1 if i32_load(9568068) != i32_load(9568064) else 0):
                var1 = ((var1 - var2) >> 7)
                var29 = (1 if (1 if var1 <= 1 else 0) else ((var1 - var2) >> 7))
                while True:  # loop $label114
                    var10 = (i32_load(9568064) + (var4 << 7))
                    if (1 if (i32_load((i32_load(9568064) + (var4 << 7)) + 108) - 1) < i32_load(var10 + 120) else 0):
                        break
                    var1 = i32_load(9142848)
                    var2 = i32_load(var10 + 116)
                    if i32_load(var10 + 116):
                        if ((var1 * 25) % var2):
                            break
                    if var1:
                        if (1 if i32_load(var10 + 112) > ((var1 - i32_load(var10 + 124)) * 25) else 0):
                            break
                    var1 = i32_load(var10 + 4)
                    var5 = i32_load(var10)
                    var2 = ((i32_load(var10 + 4) - i32_load(var10)) // 196)
                    i32_store(9684388, ((i32_load(var10 + 4) - i32_load(var10)) // 196))
                    i32_store(9140300, 0)
                    i32_store(9684384, 0)
                    if i32_load(9142892):
                        var3 = 0
                        var6 = i32_load(9142420)
                        while True:  # loop $label9
                            i32_store((var6 + (var3 << 2)), 0)
                            var3 = (var3 + 1)
                            if (1 if (var3 + 1) < i32_load(9142892) else 0):
                                continue
                            break  # end loop
                    var5 = (1 if var1 == var5 else 0)
                    if (1 if var1 == var5 else 0):
                        break
                    var6 = (1 if (1 if var2 <= 1 else 0) else var2)
                    var1 = 0
                    var3 = 0
                    while True:  # loop $label12
                        var7 = (i32_load(var10) + (var3 * 196))
                        if (1 if i32_load8_u((i32_load(var10) + (var3 * 196)) + 44) == 0 else 0):
                            if (1 if func380(var7) == 0 else 0):
                                break
                        var3 = (var3 + 1)
                        var1 = (1 if (var3 + 1) >= var2 else 0)
                        if (1 if var3 != var6 else 0):
                            continue
                        break
                        break  # end loop
                    var2 = (var1 & 1)
                    var1 = 1
                    if var2:
                        break
                    var1 = 0
                    i32_store(9684384, 0)
                    i32_store(9140300, 0)
                    if (1 if i32_load(9142892) == 0 else 0):
                        break
                    var2 = i32_load(9142420)
                    var3 = 0
                    while True:  # loop $label14
                        i32_store((var2 + (var3 << 2)), 0)
                        var3 = (var3 + 1)
                        if (1 if (var3 + 1) < i32_load(9142892) else 0):
                            continue
                        break  # end loop
                    if var5:
                        break
                    var3 = 0
                    while True:  # loop $label15
                        var2 = (i32_load(var10) + (var3 * 196))
                        if i32_load8_u((i32_load(var10) + (var3 * 196)) + 44):
                            var1 = (func380(var2) | var1)
                        var3 = (var3 + 1)
                        if (1 if (var3 + 1) != var6 else 0):
                            continue
                        break  # end loop
                    if (1 if ((var1 | var5) & 1) == 0 else 0):
                        break
                    var24 = i32_load(var10 + 16)
                    var28 = i32_load(var10 + 12)
                    var1 = ((i32_load(var10 + 16) - i32_load(var10 + 12)) // 196)
                    var23 = (1 if (1 if var1 <= 1 else 0) else ((i32_load(var10 + 16) - i32_load(var10 + 12)) // 196))
                    var5 = 0
                    while True:  # loop $label113
                        var3 = 0
                        if (1 if var24 != var28 else 0):
                            while True:  # loop $label112
                                var6 = (i32_load(var10 + 12) + (var3 * 196))
                                var1 = 0
                                var16 = 0
                                var15 = (global0 - 32)
                                global global0
                                global0 = (global0 - 32)
                                # br_table ['$label16', '$label17', '$label18', '$label19', '$label20', '$label21', '$label22', '$label23', '$label24', '$label25', '$label26', '$label27', '$label28', '$label29', '$label30', '$label31', '$label32']
                                _br_idx = i32_load(var6)
                                break  # br_table
                                var1 = i32_load(var6 + 32)
                                if (1 if i32_load(var6 + 32) != 2147483646 else 0):
                                    break
                                var2 = i32_load(9142892)
                                if (1 if i32_load(9142892) == 0 else 0):
                                    break
                                var7 = i32_load(9142420)
                                var1 = 0
                                while True:  # loop $label34
                                    if i32_load((var7 + (var1 << 2))):
                                        var7 = i32_load(9142420)
                                        var2 = i32_load(9142892)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                # br_table ['$label35', '$label36', '$label37']
                                _br_idx = i32_load(var6 + 4)
                                break  # br_table
                                func299(var6, 71)
                                break
                                var2 = i32_load(var6 + 88)
                                if (1 if i32_load(var6 + 88) == 0 else 0):
                                    break
                                var7 = i32_load(9671128)
                                while True:  # loop $label39
                                    var9 = (var7 + (i32_load((i32_load(var6 + 80) + (var1 << 2))) * 132))
                                    if (1 if i32_load8_u((var7 + (i32_load((i32_load(var6 + 80) + (var1 << 2))) * 132)) + 125) != 3 else 0):
                                        func247(var6, var9)
                                        var7 = i32_load(9671128)
                                        var2 = i32_load(var6 + 88)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                var2 = i32_load(9140300)
                                if (1 if i32_load(9140300) == 0 else 0):
                                    break
                                var7 = i32_load(9142420)
                                var9 = i32_load(9671128)
                                while True:  # loop $label40
                                    var16 = (var9 + (i32_load(((var1 << 2) + 8451904)) * 132))
                                    if i32_load((var7 + (i32_load16_u((var9 + (i32_load(((var1 << 2) + 8451904)) * 132)) + 110) << 2))):
                                        func247(var6, var16)
                                        var7 = i32_load(9142420)
                                        var9 = i32_load(9671128)
                                        var2 = i32_load(9140300)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                func123(var6, 72)
                                break
                                # br_table ['$label41', '$label42', '$label43']
                                _br_idx = i32_load(var6 + 4)
                                break  # br_table
                                var1 = i32_load(9142892)
                                if (1 if i32_load(9142892) == 0 else 0):
                                    break
                                while True:  # loop $label53
                                    var2 = i32_load(var6 + 48)
                                    var7 = (var16 << 2)
                                    if (1 if i32_load((i32_load(var6 + 48) + (var16 << 2))) == 0 else 0):
                                        if (1 if i32_load((var2 + (var1 << 2))) == 0 else 0):
                                            break
                                        if (1 if i32_load((i32_load(9142420) + var7)) == 0 else 0):
                                            break
                                    var2 = 0
                                    var11 = i32_load(9561692)
                                    var12 = i32_load(var6 + 32)
                                    if (1 if i32_load(var6 + 32) <= 3 else 0):
                                        while True:  # loop $label51
                                            # br_table ['$label45', '$label46', '$label47', '$label48']
                                            _br_idx = (var12 - 1)
                                            break  # br_table
                                            var1 = ((var2 * 404) + 9568096)
                                            if i32_load(((var2 * 404) + 9568096) + 264):
                                                break
                                            if (1 if i32_load(var1 + 268) == 1 else 0):
                                                break
                                            if (1 if i32_load(var1 + 92) == 0 else 0):
                                                break
                                            if (1 if i32_load(38456) == var2 else 0):
                                                break
                                            if (1 if i32_load(38764) != var2 else 0):
                                                break
                                            break
                                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) == 1 else 0):
                                                break
                                            break
                                            if i32_load(((var2 * 404) + 9568096) + 264):
                                                break
                                            var9 = i32_load((((var11 + (var16 * 286704)) + (var2 << 2)) + 284636))
                                            if (1 if i32_load((((var11 + (var16 * 286704)) + (var2 << 2)) + 284636)) == 0 else 0):
                                                break
                                            var1 = 0
                                            var7 = i32_load(var9 + 8)
                                            if (1 if i32_load(var9 + 8) == 0 else 0):
                                                break
                                            while True:  # loop $label50
                                                var14 = i32_load((i32_load(var9) + (var1 << 2)))
                                                if i32_load((i32_load(var9) + (var1 << 2))):
                                                    var7 = i32_load(var9 + 8)
                                                var1 = (var1 + 1)
                                                if (1 if (var1 + 1) < var7 else 0):
                                                    continue
                                                break  # end loop
                                            var2 = (var2 + 1)
                                            if (1 if (var2 + 1) != 255 else 0):
                                                continue
                                            break
                                            break  # end loop
                                        raise RuntimeError('unreachable')
                                    var2 = i32_load((((var11 + (var16 * 286704)) + (var12 << 2)) + 284620))
                                    if (1 if i32_load((((var11 + (var16 * 286704)) + (var12 << 2)) + 284620)) == 0 else 0):
                                        break
                                    var1 = 0
                                    var7 = i32_load(var2 + 8)
                                    if (1 if i32_load(var2 + 8) == 0 else 0):
                                        break
                                    while True:  # loop $label52
                                        var9 = i32_load((i32_load(var2) + (var1 << 2)))
                                        if i32_load((i32_load(var2) + (var1 << 2))):
                                            var7 = i32_load(var2 + 8)
                                        var1 = (var1 + 1)
                                        if (1 if (var1 + 1) < var7 else 0):
                                            continue
                                        break  # end loop
                                    var16 = (var16 + 1)
                                    var1 = i32_load(9142892)
                                    if (1 if (var16 + 1) < i32_load(9142892) else 0):
                                        continue
                                    break  # end loop
                                break
                                var2 = i32_load(var6 + 88)
                                if (1 if i32_load(var6 + 88) == 0 else 0):
                                    break
                                var7 = i32_load(9671128)
                                while True:  # loop $label54
                                    var9 = (var7 + (i32_load((i32_load(var6 + 80) + (var1 << 2))) * 132))
                                    if (1 if i32_load8_u((var7 + (i32_load((i32_load(var6 + 80) + (var1 << 2))) * 132)) + 125) != 3 else 0):
                                        var7 = i32_load(9671128)
                                        var2 = i32_load(var6 + 88)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                var2 = i32_load(9140300)
                                if (1 if i32_load(9140300) == 0 else 0):
                                    break
                                var7 = i32_load(9142420)
                                var6 = i32_load(9671128)
                                while True:  # loop $label55
                                    var9 = (var6 + (i32_load(((var1 << 2) + 8451904)) * 132))
                                    if i32_load((var7 + (i32_load16_u((var6 + (i32_load(((var1 << 2) + 8451904)) * 132)) + 110) << 2))):
                                        var7 = i32_load(9142420)
                                        var6 = i32_load(9671128)
                                        var2 = i32_load(9140300)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                func123(var6, 73)
                                break
                                func123(var6, 74)
                                break
                                func123(var6, 75)
                                break
                                var2 = i32_load(9142892)
                                if (1 if i32_load(9142892) < 2 else 0):
                                    break
                                var1 = 1
                                while True:  # loop $label57
                                    var7 = i32_load(var6 + 48)
                                    var9 = (var1 << 2)
                                    if (1 if i32_load((i32_load(var6 + 48) + (var1 << 2))) == 0 else 0):
                                        if (1 if i32_load((var7 + (var2 << 2))) == 0 else 0):
                                            break
                                        if (1 if i32_load((i32_load(9142420) + var9)) == 0 else 0):
                                            break
                                    var7 = (i32_load(9561692) + (var1 * 286704))
                                    if i32_load8_u((i32_load(9561692) + (var1 * 286704)) + 286696):
                                        break
                                    if i32_load8_u(var7 + 286697):
                                        break
                                    i32_store8((var7 + 286697), 1)
                                    if (1 if i32_load(var7 + 283908) == i32_load(9142872) else 0):
                                        a_b()
                                    var9 = i32_load(var7 + 284628)
                                    var2 = i32_load(var7 + 284616)
                                    i32_store(var15 + 4, var7)
                                    i32_store(var15, 119)
                                    i32_store(var15 + 8, (var2 if var2 else var9))
                                    a_b()
                                    func227()
                                    var2 = i32_load(9142892)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                if (1 if var2 < 2 else 0):
                                    break
                                var7 = i32_load(9561692)
                                var1 = 1
                                while True:  # loop $label58
                                    var6 = (var7 + (var1 * 286704))
                                    if (1 if i32_load8_u((var7 + (var1 * 286704)) + 286697) == 0 else 0):
                                        var7 = i32_load(9561692)
                                        var2 = i32_load(9142892)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                var2 = i32_load(9142892)
                                if (1 if i32_load(9142892) < 2 else 0):
                                    break
                                var1 = 1
                                while True:  # loop $label60
                                    var7 = i32_load(var6 + 48)
                                    var9 = (var1 << 2)
                                    if (1 if i32_load((i32_load(var6 + 48) + (var1 << 2))) == 0 else 0):
                                        if (1 if i32_load((var7 + (var2 << 2))) == 0 else 0):
                                            break
                                        if (1 if i32_load((i32_load(9142420) + var9)) == 0 else 0):
                                            break
                                    var2 = i32_load(9142892)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                var2 = i32_load(9142892)
                                if (1 if i32_load(9142892) < 2 else 0):
                                    break
                                var1 = 1
                                while True:  # loop $label62
                                    var7 = i32_load(var6 + 48)
                                    var9 = (var1 << 2)
                                    if (1 if i32_load((i32_load(var6 + 48) + (var1 << 2))) == 0 else 0):
                                        if (1 if i32_load((var7 + (var2 << 2))) == 0 else 0):
                                            break
                                        if (1 if i32_load((i32_load(9142420) + var9)) == 0 else 0):
                                            break
                                    if (1 if i32_load((i32_load(9561692) + (var1 * 286704)) + 283908) != i32_load(9142872) else 0):
                                        break
                                    var2 = i32_load(var6 + 80)
                                    i32_store(var15 + 20, i32_load(var6 + 88))
                                    i32_store(var15 + 16, var2)
                                    a_b()
                                    var2 = i32_load(9142892)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                var2 = i32_load(9142892)
                                if (1 if i32_load(9142892) < 2 else 0):
                                    break
                                var1 = 1
                                while True:  # loop $label70
                                    var7 = i32_load(var6 + 48)
                                    var9 = (var1 << 2)
                                    if (1 if i32_load((i32_load(var6 + 48) + (var1 << 2))) == 0 else 0):
                                        if (1 if i32_load((var7 + (var2 << 2))) == 0 else 0):
                                            break
                                        if (1 if i32_load((i32_load(9142420) + var9)) == 0 else 0):
                                            break
                                    var2 = (i32_load(9561692) + (var1 * 286704))
                                    var7 = i32_load(var6 + 80)
                                    # br_table ['$label64', '$label65', '$label66', '$label67', '$label68', '$label69']
                                    _br_idx = i32_load(var6 + 16)
                                    break  # br_table
                                    var9 = i32_load(var7)
                                    if (1 if i32_load(var7) != -2147483647 else 0):
                                        i32_store(var2 + 283848, var9)
                                    var9 = i32_load(var7 + 4)
                                    if (1 if i32_load(var7 + 4) != -2147483647 else 0):
                                        i32_store((var2 + 283852), var9)
                                    var9 = i32_load(var7 + 8)
                                    if (1 if i32_load(var7 + 8) != -2147483647 else 0):
                                        i32_store((var2 + 283856), var9)
                                    var7 = i32_load(var7 + 12)
                                    if (1 if i32_load(var7 + 12) == -2147483647 else 0):
                                        break
                                    i32_store((var2 + 283860), var7)
                                    break
                                    var9 = i32_load(var7)
                                    if (1 if i32_load(var7) != -2147483647 else 0):
                                        i32_store(var2 + 283848, (i32_load(var2 + 283848) + var9))
                                    var9 = i32_load(var7 + 4)
                                    if (1 if i32_load(var7 + 4) != -2147483647 else 0):
                                        var16 = (var2 + 283852)
                                        i32_store((var2 + 283852), (i32_load(var16) + var9))
                                    var9 = i32_load(var7 + 8)
                                    if (1 if i32_load(var7 + 8) != -2147483647 else 0):
                                        var16 = (var2 + 283856)
                                        i32_store((var2 + 283856), (i32_load(var16) + var9))
                                    var7 = i32_load(var7 + 12)
                                    if (1 if i32_load(var7 + 12) == -2147483647 else 0):
                                        break
                                    var2 = (var2 + 283860)
                                    i32_store((var2 + 283860), (i32_load(var2) + var7))
                                    break
                                    var9 = i32_load(var7)
                                    if (1 if i32_load(var7) != -2147483647 else 0):
                                        i32_store(var2 + 283848, (i32_load(var2 + 283848) - var9))
                                    var9 = i32_load(var7 + 4)
                                    if (1 if i32_load(var7 + 4) != -2147483647 else 0):
                                        var16 = (var2 + 283852)
                                        i32_store((var2 + 283852), (i32_load(var16) - var9))
                                    var9 = i32_load(var7 + 8)
                                    if (1 if i32_load(var7 + 8) != -2147483647 else 0):
                                        var16 = (var2 + 283856)
                                        i32_store((var2 + 283856), (i32_load(var16) - var9))
                                    var7 = i32_load(var7 + 12)
                                    if (1 if i32_load(var7 + 12) == -2147483647 else 0):
                                        break
                                    var2 = (var2 + 283860)
                                    i32_store((var2 + 283860), (i32_load(var2) - var7))
                                    break
                                    var9 = i32_load(var7)
                                    if (1 if i32_load(var7) != -2147483647 else 0):
                                        i32_store(var2 + 283848, (i32_load(var2 + 283848) * var9))
                                    var9 = i32_load(var7 + 4)
                                    if (1 if i32_load(var7 + 4) != -2147483647 else 0):
                                        var16 = (var2 + 283852)
                                        i32_store((var2 + 283852), (i32_load(var16) * var9))
                                    var9 = i32_load(var7 + 8)
                                    if (1 if i32_load(var7 + 8) != -2147483647 else 0):
                                        var16 = (var2 + 283856)
                                        i32_store((var2 + 283856), (i32_load(var16) * var9))
                                    var7 = i32_load(var7 + 12)
                                    if (1 if i32_load(var7 + 12) == -2147483647 else 0):
                                        break
                                    var2 = (var2 + 283860)
                                    i32_store((var2 + 283860), (i32_load(var2) * var7))
                                    break
                                    var9 = i32_load(var7)
                                    if (1 if i32_load(var7) != -2147483647 else 0):
                                        i32_store(var2 + 283848, (i32_load(var2 + 283848) // var9))
                                    var9 = i32_load(var7 + 4)
                                    if (1 if i32_load(var7 + 4) != -2147483647 else 0):
                                        var16 = (var2 + 283852)
                                        i32_store((var2 + 283852), (i32_load(var16) // var9))
                                    var9 = i32_load(var7 + 8)
                                    if (1 if i32_load(var7 + 8) != -2147483647 else 0):
                                        var16 = (var2 + 283856)
                                        i32_store((var2 + 283856), (i32_load(var16) // var9))
                                    var7 = i32_load(var7 + 12)
                                    if (1 if i32_load(var7 + 12) == -2147483647 else 0):
                                        break
                                    var2 = (var2 + 283860)
                                    i32_store((var2 + 283860), (i32_load(var2) // var7))
                                    var2 = i32_load(9142892)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                if (1 if i32_load(var6 + 4) <= 2 else 0):
                                    func123(var6, 76)
                                    break
                                var2 = i32_load(9142892)
                                if (1 if i32_load(9142892) < 2 else 0):
                                    break
                                var1 = 1
                                while True:  # loop $label80
                                    var7 = i32_load(var6 + 48)
                                    var9 = (var1 << 2)
                                    if (1 if i32_load((i32_load(var6 + 48) + (var1 << 2))) == 0 else 0):
                                        if (1 if i32_load((var7 + (var2 << 2))) == 0 else 0):
                                            break
                                        if (1 if i32_load((i32_load(9142420) + var9)) == 0 else 0):
                                            break
                                    var12 = 0
                                    var16 = (i32_load(9561692) + (var1 * 286704))
                                    if (1 if i32_load((i32_load(9561692) + (var1 * 286704)) + 286680) == 0 else 0):
                                        var2 = func26(16)
                                        i32_store(func26(16) + 4, 16)
                                        i32_store(var2, func26(64))
                                        i64_store(var2 + 8, 4294967296)
                                        i32_store(var16 + 286680, var2)
                                        while True:  # loop $label73
                                            var2 = i32_load(var16 + 286680)
                                            var7 = i32_load(i32_load(var16 + 286680) + 8)
                                            if (1 if i32_load(i32_load(var16 + 286680) + 8) != i32_load(var2 + 4) else 0):
                                                var9 = i32_load(var2)
                                                break
                                            var9 = (i32_load(var2 + 12) + var7)
                                            i32_store(var2 + 4, (i32_load(var2 + 12) + var7))
                                            var11 = i32_load(var2)
                                            var9 = func26((-1 if (1 if var9 > 1073741823 else 0) else (var9 << 2)))
                                            if var7:
                                                # Unknown: memory.copy []
                                            if var11:
                                                var7 = i32_load(var2 + 8)
                                            i32_store(var2, var9)
                                            i32_store(var2 + 8, (var7 + 1))
                                            i32_store((var9 + (var7 << 2)), 0)
                                            var12 = (var12 + 1)
                                            if (1 if (var12 + 1) != 16 else 0):
                                                continue
                                            break  # end loop
                                    var7 = i32_load(var16 + 286680)
                                    var2 = i32_load(var6 + 8)
                                    if (1 if i32_load(var6 + 8) >= 16777216 else 0):
                                        var2 = i32_load(((i32_load(var7) + (var2 << 2)) - 67108864))
                                    var9 = i32_load(var6 + 36)
                                    # br_table ['$label74', '$label75', '$label76', '$label77', '$label78', '$label79']
                                    _br_idx = i32_load(var6 + 28)
                                    break  # br_table
                                    i32_store((i32_load(var7) + (var9 << 2)), var2)
                                    break
                                    var7 = (i32_load(var7) + (var9 << 2))
                                    i32_store((i32_load(var7) + (var9 << 2)), (i32_load(var7) + var2))
                                    break
                                    var7 = (i32_load(var7) + (var9 << 2))
                                    i32_store((i32_load(var7) + (var9 << 2)), (i32_load(var7) - var2))
                                    break
                                    var7 = (i32_load(var7) + (var9 << 2))
                                    i32_store((i32_load(var7) + (var9 << 2)), (i32_load(var7) * var2))
                                    break
                                    var7 = (i32_load(var7) + (var9 << 2))
                                    i32_store((i32_load(var7) + (var9 << 2)), ((i32_load(var7) & 0xFFFFFFFF) // var2))
                                    var2 = i32_load(9142892)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                var2 = i32_load(9142892)
                                if (1 if i32_load(9142892) < 2 else 0):
                                    break
                                var1 = 1
                                while True:  # loop $label90
                                    var7 = i32_load(var6 + 48)
                                    var9 = (var1 << 2)
                                    if (1 if i32_load((i32_load(var6 + 48) + (var1 << 2))) == 0 else 0):
                                        if (1 if i32_load((var7 + (var2 << 2))) == 0 else 0):
                                            break
                                        if (1 if i32_load((i32_load(9142420) + var9)) == 0 else 0):
                                            break
                                    var12 = (i32_load(9561692) + (var1 * 286704))
                                    var16 = 0
                                    var7 = i32_load(var6 + 88)
                                    if i32_load(var6 + 88):
                                        while True:  # loop $label89
                                            var18 = (var16 << 2)
                                            if (1 if i32_load(((var16 << 2) + i32_load(var6 + 80))) == 0 else 0):
                                                break
                                            if (1 if var16 > 254 else 0):
                                                break
                                            if i32_load(((var12 + var18) + 282828)):
                                                var9 = ((var16 * 404) + 9568164)
                                                var14 = 0
                                                while True:  # loop $label88
                                                    var17 = i32_load(((var12 + (var14 << 2)) + 284636))
                                                    if (1 if i32_load(((var12 + (var14 << 2)) + 284636)) == 0 else 0):
                                                        break
                                                    var20 = 0
                                                    if (1 if i32_load(var17 + 8) == 0 else 0):
                                                        break
                                                    while True:  # loop $label87
                                                        var2 = i32_load((i32_load(var17) + (var20 << 2)))
                                                        if (1 if i32_load((i32_load(var17) + (var20 << 2))) == 0 else 0):
                                                            break
                                                        var26 = i32_load(9215884)
                                                        var11 = (i32_load(9671128) + (var2 * 132))
                                                        var2 = i32_load((i32_load(9671128) + (var2 * 132)) + 44)
                                                        if (1 if i32_load((i32_load(9215884) + (i32_load((i32_load(9671128) + (var2 * 132)) + 44) << 4)) + 4) != 5 else 0):
                                                            break
                                                        if (1 if i32_load((var26 + ((var2 << 4) | 12))) != var16 else 0):
                                                            break
                                                        i32_store8(var11 + 125, 0)
                                                        var2 = (i32_load(9561692) + (i32_load16_u(var11 + 110) * 286704))
                                                        i32_store((((i32_load(9561692) + (i32_load16_u(var11 + 110) * 286704)) + var18) + 282828), 0)
                                                        var7 = i32_load(var2 + 283848)
                                                        if (1 if i32_load(var2 + 283848) != 2147483647 else 0):
                                                            i32_store((var2 + 283848), (i32_load(var9) + var7))
                                                        var7 = (var2 + 283852)
                                                        var21 = i32_load((var2 + 283852))
                                                        if (1 if i32_load((var2 + 283852)) != 2147483647 else 0):
                                                            i32_store(var7, (i32_load(var9 + 4) + var21))
                                                        var7 = (var2 + 283856)
                                                        var21 = i32_load((var2 + 283856))
                                                        if (1 if i32_load((var2 + 283856)) != 2147483647 else 0):
                                                            i32_store(var7, (i32_load(var9 + 8) + var21))
                                                        var7 = (var2 + 283860)
                                                        var21 = i32_load((var2 + 283860))
                                                        if (1 if i32_load((var2 + 283860)) != 2147483647 else 0):
                                                            i32_store(var7, (i32_load(var9 + 12) + var21))
                                                        var7 = (var2 + 281692)
                                                        i32_store((var2 + 281692), (i32_load(var7) - i32_load(var9)))
                                                        var7 = (var2 + 281696)
                                                        i32_store((var2 + 281696), (i32_load(var7) - i32_load(var9 + 4)))
                                                        var7 = (var2 + 281700)
                                                        i32_store((var2 + 281700), (i32_load(var7) - i32_load(var9 + 8)))
                                                        var7 = i32_load(var9 + 12)
                                                        i32_store8(var2 + 286701, 1)
                                                        var21 = (var2 + 281704)
                                                        i32_store((var2 + 281704), (i32_load(var21) - var7))
                                                        var21 = i32_load(9142892)
                                                        if (1 if i32_load(9142892) < 2 else 0):
                                                            break
                                                        var7 = 1
                                                        var40 = (var21 - 1)
                                                        var43 = ((var21 - 1) & 1)
                                                        var2 = (i32_load(var2 + 283908) * var21)
                                                        var8 = i32_load(9561692)
                                                        var19 = i32_load(9143016)
                                                        if (1 if var21 != 2 else 0):
                                                            var40 = (var40 & -2)
                                                            var21 = 0
                                                            while True:  # loop $label86
                                                                if i32_load8_u((var19 + (var2 + var7))):
                                                                    i32_store8((var8 + (var7 * 286704)) + 286701, 1)
                                                                var30 = (var7 + 1)
                                                                if i32_load8_u((var19 + ((var7 + 1) + var2))):
                                                                    i32_store8((var8 + (var30 * 286704)) + 286701, 1)
                                                                var7 = (var7 + 2)
                                                                var21 = (var21 + 2)
                                                                if (1 if (var21 + 2) != var40 else 0):
                                                                    continue
                                                                break  # end loop
                                                        if (1 if var43 == 0 else 0):
                                                            break
                                                        if (1 if i32_load8_u((var19 + (var2 + var7))) == 0 else 0):
                                                            break
                                                        i32_store8((var8 + (var7 * 286704)) + 286701, 1)
                                                        var2 = i32_load(var11 + 44)
                                                        if i32_load(var11 + 44):
                                                            i32_store((var26 + (var2 << 4)), 0)
                                                        i32_store(var11 + 44, 0)
                                                        if (1 if i32_load(var11 + 92) == 0 else 0):
                                                            break
                                                        var2 = i32_load8_u(9147141)
                                                        if i32_load(9140316):
                                                            if (1 if i32_load(9140320) != i32_load(var11 + 28) else 0):
                                                                break
                                                        var20 = (var20 + 1)
                                                        if (1 if (var20 + 1) < i32_load(var17 + 8) else 0):
                                                            continue
                                                        break  # end loop
                                                    var14 = (var14 + 1)
                                                    if (1 if (var14 + 1) != 255 else 0):
                                                        continue
                                                    break  # end loop
                                            func238(var16, i32_load(var12 + 283908), 0)
                                            var7 = i32_load(var6 + 88)
                                            var16 = (var16 + 1)
                                            if (1 if (var16 + 1) < var7 else 0):
                                                continue
                                            break  # end loop
                                    var2 = i32_load(9142892)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                var2 = i32_load(9142892)
                                if (1 if i32_load(9142892) < 2 else 0):
                                    break
                                var1 = 1
                                while True:  # loop $label103
                                    var7 = i32_load(var6 + 48)
                                    var9 = (var1 << 2)
                                    if (1 if i32_load((i32_load(var6 + 48) + (var1 << 2))) == 0 else 0):
                                        if (1 if i32_load((var7 + (var2 << 2))) == 0 else 0):
                                            break
                                        if (1 if i32_load((i32_load(9142420) + var9)) == 0 else 0):
                                            break
                                    var11 = (i32_load(9561692) + (var1 * 286704))
                                    var16 = (global0 - 32)
                                    global global0
                                    global0 = (global0 - 32)
                                    if (1 if i32_load(var6 + 88) != 7 else 0):
                                        break
                                    var2 = i32_load(9142892)
                                    if (1 if i32_load(9142892) < 2 else 0):
                                        break
                                    var7 = 1
                                    while True:  # loop $label102
                                        var9 = i32_load(var6 + 64)
                                        var12 = (var7 << 2)
                                        if (1 if i32_load((i32_load(var6 + 64) + (var7 << 2))) == 0 else 0):
                                            if (1 if i32_load((var9 + (var2 << 2))) == 0 else 0):
                                                break
                                            if (1 if i32_load((i32_load(9142420) + var12)) == 0 else 0):
                                                break
                                        var12 = i32_load(var11 + 283908)
                                        if (1 if i32_load(var11 + 283908) == var7 else 0):
                                            break
                                        var9 = i32_load(var6 + 80)
                                        var14 = i32_load(i32_load(var6 + 80))
                                        if (1 if i32_load(i32_load(var6 + 80)) == 2147483647 else 0):
                                            break
                                        var17 = i32_load(9143004)
                                        var20 = (i32_load(9143004) + (var12 + (var2 * var7)))
                                        if (1 if var14 == i32_load8_u((i32_load(9143004) + (var12 + (var2 * var7)))) else 0):
                                            break
                                        var9 = (1 if var14 != 0 else 0)
                                        i32_store8(var20, (1 if var14 != 0 else 0))
                                        i32_store8((var17 + ((var2 * var12) + var7)), var9)
                                        la()
                                        var9 = i32_load(var6 + 80)
                                        var2 = i32_load(var9 + 4)
                                        if (1 if i32_load(var9 + 4) == 2147483647 else 0):
                                            break
                                        var12 = i32_load(var11 + 283908)
                                        if (1 if var2 == i32_load8_u((i32_load(9143012) + (i32_load(var11 + 283908) + (i32_load(9142892) * var7)))) else 0):
                                            break
                                        func414(3, var2, var7, var12, 1)
                                        var9 = i32_load(var6 + 80)
                                        var2 = i32_load(var9 + 8)
                                        if (1 if i32_load(var9 + 8) == 2147483647 else 0):
                                            break
                                        var12 = i32_load(var11 + 283908)
                                        if (1 if i32_load(var11 + 283908) == var7 else 0):
                                            break
                                        var14 = i32_load(9142892)
                                        if (1 if i32_load(9142892) <= var7 else 0):
                                            break
                                        var14 = (i32_load(9143008) + ((var12 * var14) + var7))
                                        if (1 if var2 == i32_load8_u((i32_load(9143008) + ((var12 * var14) + var7))) else 0):
                                            break
                                        if i32_load(9147132):
                                            if (1 if i32_load(9142440) == 4096 else 0):
                                                break
                                        i32_store8(var14, (1 if var2 != 0 else 0))
                                        if (1 if i32_load(9142872) != var7 else 0):
                                            break
                                        var9 = (i32_load(9561692) + (var12 * 286704))
                                        var14 = i32_load((i32_load(9561692) + (var12 * 286704)) + 284628)
                                        var12 = i32_load(var9 + 284616)
                                        i32_store(var16 + 16, (450 if var2 else 532))
                                        i32_store(var16 + 20, var9)
                                        i32_store(var16 + 24, (var12 if var12 else var14))
                                        a_b()
                                        var9 = i32_load(var6 + 80)
                                        var2 = i32_load(var9 + 12)
                                        if (1 if i32_load(var9 + 12) == 2147483647 else 0):
                                            if (1 if i32_load(var9 + 16) != 2147483647 else 0):
                                                break
                                            if (1 if i32_load(var9 + 20) != 2147483647 else 0):
                                                break
                                            if (1 if i32_load(var9 + 24) == 2147483647 else 0):
                                                break
                                            var17 = i32_load(9142892)
                                            var12 = i32_load(var11 + 283908)
                                            var20 = (i32_load(9143016) + ((i32_load(9142892) * i32_load(var11 + 283908)) + var7))
                                            var14 = i32_load8_u((i32_load(9143016) + ((i32_load(9142892) * i32_load(var11 + 283908)) + var7)))
                                            break
                                        var17 = i32_load(9142892)
                                        var12 = i32_load(var11 + 283908)
                                        var20 = (i32_load(9143016) + ((i32_load(9142892) * i32_load(var11 + 283908)) + var7))
                                        var14 = i32_load8_u((i32_load(9143016) + ((i32_load(9142892) * i32_load(var11 + 283908)) + var7)))
                                        if var2:
                                            break
                                        var2 = (var14 & 254)
                                        var21 = i32_load(var9 + 16)
                                        if (1 if i32_load(var9 + 16) == 2147483647 else 0):
                                            break
                                        if (1 if var21 == 0 else 0):
                                            var2 = (var2 & 253)
                                            break
                                        var2 = (var2 | 2)
                                        var21 = i32_load(var9 + 20)
                                        if (1 if i32_load(var9 + 20) == 2147483647 else 0):
                                            break
                                        if (1 if var21 == 0 else 0):
                                            var2 = (var2 & 251)
                                            break
                                        var2 = (var2 | 4)
                                        var9 = i32_load(var9 + 24)
                                        if (1 if i32_load(var9 + 24) == 2147483647 else 0):
                                            break
                                        if (1 if var9 == 0 else 0):
                                            var2 = (var2 & 247)
                                            break
                                        var2 = (var2 | 8)
                                        if (1 if var7 == var12 else 0):
                                            break
                                        if (1 if var7 >= var17 else 0):
                                            break
                                        if (1 if var2 == var14 else 0):
                                            break
                                        var9 = i32_load(9142424)
                                        if i32_load(i32_load(9142424) + 180):
                                            if (1 if i32_load(9142848) < (i32_load(var9 + 72) * 2400) else 0):
                                                break
                                        if i32_load(9147132):
                                            if (1 if i32_load(9142440) == 4096 else 0):
                                                break
                                        i32_store8(var20, var2)
                                        var9 = i32_load(9561692)
                                        i32_store8((i32_load(9561692) + (var7 * 286704)) + 286701, 1)
                                        if (1 if i32_load(9142872) != var7 else 0):
                                            break
                                        var9 = (var9 + (var12 * 286704))
                                        var14 = i32_load((var9 + (var12 * 286704)) + 284628)
                                        var12 = i32_load(var9 + 284616)
                                        i32_store(var16 + 4, var9)
                                        i32_store(var16, var2)
                                        i32_store(var16 + 8, (var12 if var12 else var14))
                                        a_b()
                                        var7 = (var7 + 1)
                                        var2 = i32_load(9142892)
                                        if (1 if (var7 + 1) < i32_load(9142892) else 0):
                                            continue
                                        break  # end loop
                                    global global0
                                    global0 = (var16 + 32)
                                    var2 = i32_load(9142892)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                func123(var6, 77)
                                break
                                var2 = i32_load(9142892)
                                if (1 if i32_load(9142892) < 2 else 0):
                                    break
                                var7 = i32_load(9561692)
                                var11 = i32_load(9142420)
                                var16 = i32_load(var6 + 48)
                                var1 = 1
                                while True:  # loop $label111
                                    var9 = (var1 << 2)
                                    if (1 if i32_load((var16 + (var1 << 2))) == 0 else 0):
                                        if (1 if i32_load((var16 + (var2 << 2))) == 0 else 0):
                                            break
                                        if (1 if i32_load((var9 + var11)) == 0 else 0):
                                            break
                                    var2 = i32_load(var6 + 32)
                                    var9 = i32_load(var6 + 28)
                                    # br_table ['$label105', '$label106', '$label107', '$label108', '$label109', '$label110']
                                    _br_idx = i32_load(var6 + 16)
                                    break  # br_table
                                    i32_store((((var7 + (var1 * 286704)) + (var9 << 2)) + 283984), var2)
                                    break
                                    var9 = (((var7 + (var1 * 286704)) + (var9 << 2)) + 283984)
                                    i32_store((((var7 + (var1 * 286704)) + (var9 << 2)) + 283984), (i32_load(var9) + var2))
                                    break
                                    var9 = (((var7 + (var1 * 286704)) + (var9 << 2)) + 283984)
                                    i32_store((((var7 + (var1 * 286704)) + (var9 << 2)) + 283984), (i32_load(var9) - var2))
                                    break
                                    var9 = (((var7 + (var1 * 286704)) + (var9 << 2)) + 283984)
                                    i32_store((((var7 + (var1 * 286704)) + (var9 << 2)) + 283984), (i32_load(var9) * var2))
                                    break
                                    var9 = (((var7 + (var1 * 286704)) + (var9 << 2)) + 283984)
                                    i32_store((((var7 + (var1 * 286704)) + (var9 << 2)) + 283984), ((i32_load(var9) & 0xFFFFFFFF) // var2))
                                    var2 = i32_load(9142892)
                                    var1 = (var1 + 1)
                                    if (1 if (var1 + 1) < var2 else 0):
                                        continue
                                    break  # end loop
                                break
                                global global0
                                global0 = (var15 + 32)
                                var3 = (var3 + 1)
                                if (1 if (var3 + 1) != var23 else 0):
                                    continue
                                break  # end loop
                        var1 = (i32_load(var10 + 120) + 1)
                        i32_store(var10 + 120, (i32_load(var10 + 120) + 1))
                        var5 = (var5 + 1)
                        if (1 if (var5 + 1) < i32_load(9684384) else 0):
                            if (1 if (i32_load(var10 + 108) - 1) >= var1 else 0):
                                continue
                        break  # end loop
                    i32_store(var10 + 124, i32_load(9142848))
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != var29 else 0):
                        continue
                    break  # end loop
            var4 = i32_load(9142892)
            if (1 if i32_load(9142892) < 2 else 0):
                break
            var3 = i32_load(9142848)
            var14 = (i32_load(i32_load(9142424) + 120) - 1)
            var10 = 1
            while True:  # loop $label165
                var6 = (i32_load(9561692) + (var10 * 286704))
                if (1 if var3 == 0 else 0):
                    break
                # br_table ['$label117', '$label118', '$label116']
                _br_idx = var14
                break  # br_table
                if (1 if ((var3 * 25) % 1000) == 0 else 0):
                    break
                break
                if ((var3 * 25) % 60000):
                    break
                i32_store8(var6 + 286701, 1)
                if (1 if var4 < 2 else 0):
                    break
                var3 = 1
                var1 = (var4 - 1)
                var9 = ((var4 - 1) & 1)
                var2 = (i32_load(var6 + 283908) * var4)
                var5 = i32_load(9561692)
                var7 = i32_load(9143016)
                if (1 if var4 != 2 else 0):
                    var4 = (var1 & -2)
                    var1 = 0
                    while True:  # loop $label121
                        if i32_load8_u((var7 + (var2 + var3))):
                            i32_store8((var5 + (var3 * 286704)) + 286701, 1)
                        var16 = (var3 + 1)
                        if i32_load8_u((var7 + ((var3 + 1) + var2))):
                            i32_store8((var5 + (var16 * 286704)) + 286701, 1)
                        var3 = (var3 + 2)
                        var1 = (var1 + 2)
                        if (1 if (var1 + 2) != var4 else 0):
                            continue
                        break  # end loop
                if (1 if var9 == 0 else 0):
                    break
                if (1 if i32_load8_u((var7 + (var2 + var3))) == 0 else 0):
                    break
                i32_store8((var5 + (var3 * 286704)) + 286701, 1)
                var1 = i32_load(9142424)
                i32_store(var6 + 283848, (i32_load(var6 + 283848) + i32_load(i32_load(9142424) + 100)))
                var2 = (var6 + 283852)
                i32_store((var6 + 283852), (i32_load(var2) + i32_load(var1 + 104)))
                var2 = (var6 + 283856)
                i32_store((var6 + 283856), (i32_load(var2) + i32_load(var1 + 108)))
                var2 = (var6 + 283860)
                i32_store((var6 + 283860), (i32_load(var2) + i32_load(var1 + 112)))
                if i32_load8_u(var6 + 286700):
                    var7 = (var6 + 286700)
                    var1 = i32_load(var6 + 281788)
                    if (1 if i32_load(var6 + 281788) == 0 else 0):
                        break
                    var3 = i32_load(var1 + 8)
                    if (1 if i32_load(var1 + 8) == 0 else 0):
                        break
                    var9 = (var6 + 281788)
                    var2 = (var1 + 8)
                    var16 = (var6 + 284000)
                    var15 = (var6 + 284136)
                    var11 = (var6 + 283980)
                    var12 = (var6 + 283976)
                    while True:  # loop $label125
                        var5 = i32_load(var12)
                        if (1 if i32_load(var12) >= (i32_load(var15) + i32_load(var11)) else 0):
                            break
                        if (1 if var5 >= i32_load(var16) else 0):
                            break
                        var5 = i32_load(var1)
                        var4 = i32_load(i32_load(var1))
                        var17 = (var3 - 1)
                        i32_store(var2, (var3 - 1))
                        var3 = 0
                        if var17:
                            while True:  # loop $label123
                                var3 = (var3 + 1)
                                i32_store((var5 + (var3 << 2)), i32_load((var5 + ((var3 + 1) << 2))))
                                if (1 if var3 < i32_load(var2) else 0):
                                    continue
                                break  # end loop
                        var2 = (i32_load(9671128) + (var4 * 132))
                        var5 = i32_load8_u((i32_load(9671128) + (var4 * 132)) + 125)
                        if (1 if i32_load8_u((i32_load(9671128) + (var4 * 132)) + 125) == 3 else 0):
                            break
                        var3 = i32_load(var2 + 20)
                        if (1 if i32_load(var2 + 20) == 0 else 0):
                            break
                        if (1 if i32_load(var3 + 8) == 0 else 0):
                            break
                        if (1 if var5 != 7 else 0):
                            break
                        i32_store8(var2 + 125, 6)
                        var1 = i32_load(var9)
                        var2 = (var1 + 8)
                        var3 = i32_load(var1 + 8)
                        if i32_load(var1 + 8):
                            continue
                        break  # end loop
                    i32_store8(var7, 0)
                if i32_load8_u(var6 + 286701):
                    var2 = 0
                    var5 = (global0 - 80)
                    global global0
                    global0 = (global0 - 80)
                    var1 = i32_load(var6 + 281796)
                    if (1 if i32_load(var6 + 281796) == 0 else 0):
                        break
                    if (1 if i32_load(var1 + 8) == 0 else 0):
                        break
                    while True:  # loop $label138
                        var1 = (i32_load(var1) + (var2 << 2))
                        var3 = (i32_load(9671128) + (i32_load((i32_load(var1) + (var2 << 2))) * 132))
                        var9 = i32_load(var1 + 4)
                        if (1 if i32_load(var1 + 4) == -1 else 0):
                            var4 = i32_load8_u(var3 + 122)
                            var1 = i32_load(((var6 + (i32_load8_u(var3 + 122) * 36)) + 269376))
                            var1 = (i32_load(((var6 + (i32_load8_u(var3 + 122) * 36)) + 269376)) if var1 else 100)
                            var4 = ((var4 * 404) + 9568096)
                            var7 = ((i32_load(((var6 + (i32_load8_u(var3 + 122) * 36)) + 269376)) if var1 else 100) * i32_load(((var4 * 404) + 9568096) + 68))
                            var9 = (((i32_load(((var6 + (i32_load8_u(var3 + 122) * 36)) + 269376)) if var1 else 100) * i32_load(((var4 * 404) + 9568096) + 68)) // 100)
                            i32_store(var5 + 48, (((i32_load(((var6 + (i32_load8_u(var3 + 122) * 36)) + 269376)) if var1 else 100) * i32_load(((var4 * 404) + 9568096) + 68)) // 100))
                            var16 = (i32_load(var4 + 72) * var1)
                            var15 = ((i32_load(var4 + 72) * var1) // 100)
                            i32_store(var5 + 52, ((i32_load(var4 + 72) * var1) // 100))
                            var11 = (i32_load(var4 + 76) * var1)
                            var12 = ((i32_load(var4 + 76) * var1) // 100)
                            i32_store(var5 + 56, ((i32_load(var4 + 76) * var1) // 100))
                            var1 = (i32_load(var4 + 80) * var1)
                            var4 = ((i32_load(var4 + 80) * var1) // 100)
                            i32_store(var5 + 60, ((i32_load(var4 + 80) * var1) // 100))
                            if (1 if (var7 - 100) <= -200 else 0):
                                if (1 if i32_load(var5 + 64) < var9 else 0):
                                    break
                            if (1 if (var16 - 100) <= -200 else 0):
                                if (1 if i32_load(var5 + 68) < var15 else 0):
                                    break
                            if (1 if (var11 - 100) <= -200 else 0):
                                if (1 if i32_load(var5 + 72) < var12 else 0):
                                    break
                            if (1 if (var1 - 100) <= -200 else 0):
                                if (1 if i32_load(var5 + 76) < var4 else 0):
                                    break
                            if func66(var6, (var5 + 48), 1, 1):
                                break
                            i32_store8(var3 + 125, 4)
                            var1 = i32_load(var3 + 40)
                            if (1 if i32_load(var3 + 40) == 0 else 0):
                                break
                            if (1 if i32_load8_u(9142916) == 0 else 0):
                                break
                            var4 = i32_load(var3 + 92)
                            i32_store(var5 + 36, var1)
                            i32_store(var5 + 32, ((1 if var4 != 0 else 0) | 1024))
                            a_b()
                            var1 = i32_load(var3 + 40)
                            i32_store8(var3 + 127, 0)
                            if (1 if var1 == 0 else 0):
                                break
                            if i32_load8_u(9142916):
                                i32_store(var5 + 20, var1)
                                i32_store(var5 + 16, 0)
                                a_b()
                                break
                            var3 = i32_load16_u(var3 + 110)
                            i32_store(var5 + 4, var1)
                            i32_store(var5, (var3 + 16))
                            a_b()
                            var3 = i32_load(var6 + 281796)
                            var4 = (i32_load(var3 + 8) - 1)
                            i32_store(i32_load(var6 + 281796) + 8, (i32_load(var3 + 8) - 1))
                            if (1 if var2 < var4 else 0):
                                var7 = i32_load(var3)
                                var1 = var2
                                while True:  # loop $label130
                                    var1 = (var1 + 1)
                                    i32_store((var7 + (var1 << 2)), i32_load((var7 + ((var1 + 1) << 2))))
                                    var4 = i32_load(var3 + 8)
                                    if (1 if var1 < i32_load(var3 + 8) else 0):
                                        continue
                                    break  # end loop
                            var1 = (var4 - 1)
                            i32_store(var3 + 8, (var4 - 1))
                            if (1 if var1 > var2 else 0):
                                var4 = i32_load(var3)
                                var1 = var2
                                while True:  # loop $label131
                                    var1 = (var1 + 1)
                                    i32_store((var4 + (var1 << 2)), i32_load((var4 + ((var1 + 1) << 2))))
                                    if (1 if var1 < i32_load(var3 + 8) else 0):
                                        continue
                                    break  # end loop
                            var2 = (var2 - 2)
                            break
                        var1 = i32_load(((var6 + (var9 * 36)) + 269376))
                        var4 = (i32_load(((var6 + (var9 * 36)) + 269376)) if var1 else 100)
                        var1 = ((var9 * 404) + 9568096)
                        var7 = ((i32_load(((var6 + (var9 * 36)) + 269376)) if var1 else 100) * i32_load(((var9 * 404) + 9568096) + 68))
                        var16 = (((i32_load(((var6 + (var9 * 36)) + 269376)) if var1 else 100) * i32_load(((var9 * 404) + 9568096) + 68)) // 100)
                        i32_store(var5 + 48, (((i32_load(((var6 + (var9 * 36)) + 269376)) if var1 else 100) * i32_load(((var9 * 404) + 9568096) + 68)) // 100))
                        var15 = (i32_load(var1 + 72) * var4)
                        var11 = ((i32_load(var1 + 72) * var4) // 100)
                        i32_store(var5 + 52, ((i32_load(var1 + 72) * var4) // 100))
                        var12 = (i32_load(var1 + 76) * var4)
                        var17 = ((i32_load(var1 + 76) * var4) // 100)
                        i32_store(var5 + 56, ((i32_load(var1 + 76) * var4) // 100))
                        var4 = (i32_load(var1 + 80) * var4)
                        var20 = ((i32_load(var1 + 80) * var4) // 100)
                        i32_store(var5 + 60, ((i32_load(var1 + 80) * var4) // 100))
                        if (1 if (var7 - 100) <= -200 else 0):
                            if (1 if i32_load(var5 + 64) < var16 else 0):
                                break
                        if (1 if (var15 - 100) <= -200 else 0):
                            if (1 if i32_load(var5 + 68) < var11 else 0):
                                break
                        if (1 if (var12 - 100) <= -200 else 0):
                            if (1 if i32_load(var5 + 72) < var17 else 0):
                                break
                        if (1 if (var4 - 100) <= -200 else 0):
                            if (1 if i32_load(var5 + 76) < var20 else 0):
                                break
                        var16 = i32_load(var1 + 180)
                        if (1 if i32_load8_u(i32_load(var1 + 180) + 23) == 0 else 0):
                            break
                        var1 = i32_load(var16 + 4)
                        if (1 if i32_load(((i32_load(var16 + 4) * 404) + 9568096) + 264) != 3 else 0):
                            break
                        if i32_load(((var6 + (var1 << 2)) + 281808)):
                            break
                        var17 = i32_load(var16 + 68)
                        if i32_load(var16 + 68):
                            var1 = 0
                            var7 = 1
                            var4 = 0
                            var15 = 0
                            while True:  # loop $label135
                                var20 = i32_load((var16 + (var1 << 2)) + 28)
                                var11 = i32_load(((i32_load((var16 + (var1 << 2)) + 28) * 404) + 9568096) + 264)
                                var12 = (1 if i32_load(((i32_load((var16 + (var1 << 2)) + 28) * 404) + 9568096) + 264) == 1 else 0)
                                var20 = i32_load(((var6 + (var20 << 2)) + 281808))
                                if (1 if i32_load(((var6 + (var20 << 2)) + 281808)) == 1 else 0):
                                    break
                                var7 = ((1 if var11 != 3 else 0) & var7)
                                if var20:
                                    break
                                var7 = ((1 if var11 != 0 else 0) & var7)
                                break
                                var15 = (var12 | var15)
                                var4 = (var4 | var12)
                                var1 = (var1 + 1)
                                if (1 if (var1 + 1) != var17 else 0):
                                    continue
                                break  # end loop
                            if (1 if (((var7 & var15) if (var4 & 1) else var7) & 1) == 0 else 0):
                                break
                        if (1 if func183(var3, var6, var9, 0, 1, 1, 0, 1, 0) == 0 else 0):
                            break
                        var7 = i32_load(var6 + 281796)
                        var4 = (i32_load(var7 + 8) - 1)
                        i32_store(i32_load(var6 + 281796) + 8, (i32_load(var7 + 8) - 1))
                        if (1 if var2 < var4 else 0):
                            var9 = i32_load(var7)
                            var1 = var2
                            while True:  # loop $label136
                                var1 = (var1 + 1)
                                i32_store((var9 + (var1 << 2)), i32_load((var9 + ((var1 + 1) << 2))))
                                var4 = i32_load(var7 + 8)
                                if (1 if var1 < i32_load(var7 + 8) else 0):
                                    continue
                                break  # end loop
                        var1 = (var4 - 1)
                        i32_store(var7 + 8, (var4 - 1))
                        if (1 if var1 > var2 else 0):
                            var4 = i32_load(var7)
                            var1 = var2
                            while True:  # loop $label137
                                var1 = (var1 + 1)
                                i32_store((var4 + (var1 << 2)), i32_load((var4 + ((var1 + 1) << 2))))
                                if (1 if var1 < i32_load(var7 + 8) else 0):
                                    continue
                                break  # end loop
                        var2 = (var2 - 2)
                        if (1 if i32_load(var3 + 92) == 0 else 0):
                            break
                        var1 = i32_load8_u(9147141)
                        if i32_load(9140316):
                            if (1 if i32_load(9140320) != i32_load(var3 + 28) else 0):
                                break
                        var2 = (var2 + 2)
                        var1 = i32_load(var6 + 281796)
                        if (1 if (var2 + 2) < i32_load(i32_load(var6 + 281796) + 8) else 0):
                            continue
                        break  # end loop
                    global global0
                    global0 = (var5 + 80)
                    i32_store8((var6 + 286701), 0)
                var3 = i32_load(9142848)
                if ((i32_load(9142848) * 25) % 10000):
                    break
                if i32_load8_u(9142905):
                    break
                if i32_load8_u(9216060):
                    break
                var7 = func88(var6)
                var4 = i32_load((var6 + 278572))
                var3 = i32_load(i32_load((var6 + 278572)) + 8)
                if (1 if i32_load(i32_load((var6 + 278572)) + 8) != i32_load(var4 + 4) else 0):
                    var5 = i32_load(var4)
                    break
                var2 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var1 = i32_load(var4)
                var5 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                if var3:
                    # Unknown: memory.copy []
                if var1:
                    var3 = i32_load(var4 + 8)
                i32_store(var4, var5)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var5 + (var3 << 2)), var7)
                var3 = 0
                var7 = i32_load(38528)
                var2 = 0
                while True:  # loop $label143
                    if (i32_load(((var3 * 404) + 9568096) + 264) & -5):
                        break
                    if (1 if var3 == var7 else 0):
                        break
                    var2 = (i32_load(((var6 + (var3 << 2)) + 278576)) + var2)
                    var1 = (var3 | 1)
                    if (1 if (var3 | 1) != 255 else 0):
                        if (i32_load(((var1 * 404) + 9568096) + 264) & -5):
                            break
                        if (1 if var1 == var7 else 0):
                            break
                        var2 = (i32_load(((var6 + (var1 << 2)) + 278576)) + var2)
                        var3 = (var3 + 2)
                        continue
                    break  # end loop
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var1 = var5
                    break
                var1 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                if var3:
                    # Unknown: memory.copy []
                if var5:
                    var3 = i32_load(var4 + 8)
                i32_store(var4, var1)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var1 + (var3 << 2)), var2)
                var2 = 0
                var7 = i32_load(9142892)
                if i32_load(9142892):
                    var2 = i32_load((var6 + 281784))
                    var9 = (i32_load((var6 + 281784)) * 255)
                    var11 = (var2 * var7)
                    var5 = 0
                    var12 = i32_load(9561692)
                    var17 = i32_load(9143004)
                    var2 = 0
                    while True:  # loop $label147
                        if (1 if i32_load8_u((var17 + (var5 + var11))) == 0 else 0):
                            break
                        var16 = ((var12 + (var5 * 286704)) + 278568)
                        var3 = 0
                        while True:  # loop $label146
                            if (1 if i32_load(((var3 * 404) + 9568096) + 264) != 1 else 0):
                                var2 = (i32_load((i32_load(var16) + ((var3 + var9) << 2))) + var2)
                            var15 = (var3 | 1)
                            if (1 if (var3 | 1) == 255 else 0):
                                break
                            if (1 if i32_load(((var15 * 404) + 9568096) + 264) != 1 else 0):
                                var2 = (i32_load((i32_load(var16) + ((var9 + var15) << 2))) + var2)
                            var3 = (var3 + 2)
                            continue
                            break  # end loop
                        raise RuntimeError('unreachable')
                        var5 = (var5 + 1)
                        if (1 if (var5 + 1) != var7 else 0):
                            continue
                        break  # end loop
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var5 = var1
                    break
                var5 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
                if var3:
                    # Unknown: memory.copy []
                if var1:
                    var3 = i32_load(var4 + 8)
                i32_store(var4, var5)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var5 + (var3 << 2)), var2)
                var2 = 0
                var11 = i32_load(9142892)
                if i32_load(9142892):
                    var9 = i32_load((var6 + 278568))
                    var7 = 0
                    var16 = i32_load(38528)
                    while True:  # loop $label152
                        var15 = (var7 * 255)
                        var3 = 0
                        while True:  # loop $label151
                            if (1 if i32_load(((var3 * 404) + 9568096) + 264) == 1 else 0):
                                break
                            if (1 if var3 == var16 else 0):
                                break
                            var2 = (i32_load((var9 + ((var3 + var15) << 2))) + var2)
                            var1 = (var3 | 1)
                            if (1 if (var3 | 1) != 255 else 0):
                                if (1 if i32_load(((var1 * 404) + 9568096) + 264) == 1 else 0):
                                    break
                                if (1 if var1 == var16 else 0):
                                    break
                                var2 = (i32_load((var9 + ((var1 + var15) << 2))) + var2)
                                var3 = (var3 + 2)
                                continue
                            break  # end loop
                        var7 = (var7 + 1)
                        if (1 if (var7 + 1) != var11 else 0):
                            continue
                        break  # end loop
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var1 = var5
                    break
                var1 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                if var3:
                    # Unknown: memory.copy []
                if var5:
                    var3 = i32_load(var4 + 8)
                i32_store(var4, var1)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var1 + (var3 << 2)), var2)
                var5 = (i32_load((var6 + 281676)) + i32_load((var6 + 281640)))
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var2 = var1
                    break
                var2 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                if var3:
                    # Unknown: memory.copy []
                i32_store(var4, var2)
                var3 = i32_load(var4 + 8)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var2 + (var3 << 2)), var5)
                var5 = (i32_load((var6 + 281680)) + i32_load((var6 + 281644)))
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var1 = var2
                    break
                var1 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                if var3:
                    # Unknown: memory.copy []
                i32_store(var4, var1)
                var3 = i32_load(var4 + 8)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var1 + (var3 << 2)), var5)
                var5 = (i32_load((var6 + 281656)) + (i32_load((var6 + 281660)) + (i32_load((var6 + 281652)) + (i32_load((var6 + 281684)) + i32_load((var6 + 281648))))))
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var2 = var1
                    break
                var2 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                if var3:
                    # Unknown: memory.copy []
                i32_store(var4, var2)
                var3 = i32_load(var4 + 8)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var2 + (var3 << 2)), var5)
                var5 = (i32_load((var6 + 281688)) + i32_load((var6 + 281664)))
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var1 = var2
                    break
                var1 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                if var3:
                    # Unknown: memory.copy []
                i32_store(var4, var1)
                var3 = i32_load(var4 + 8)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var1 + (var3 << 2)), var5)
                var5 = i32_load(var6 + 283976)
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var2 = var1
                    break
                var2 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                if var3:
                    # Unknown: memory.copy []
                i32_store(var4, var2)
                var3 = i32_load(var4 + 8)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var2 + (var3 << 2)), var5)
                var1 = (var6 + 281808)
                var5 = ((i32_load(((var6 + 281808) + (i32_load(38732) << 2))) + i32_load((var1 + (i32_load(38460) << 2)))) + i32_load((var1 + (i32_load(38672) << 2))))
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var1 = var2
                    break
                var1 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                if var3:
                    # Unknown: memory.copy []
                i32_store(var4, var1)
                var3 = i32_load(var4 + 8)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var1 + (var3 << 2)), var5)
                var5 = i32_load(var6 + 283936)
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var2 = var1
                    break
                var2 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                if var3:
                    # Unknown: memory.copy []
                i32_store(var4, var2)
                var3 = i32_load(var4 + 8)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var2 + (var3 << 2)), var5)
                var5 = i32_load(var13 + 96)
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var1 = var2
                    break
                var1 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                if var3:
                    # Unknown: memory.copy []
                i32_store(var4, var1)
                var3 = i32_load(var4 + 8)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var1 + (var3 << 2)), var5)
                var5 = i32_load(var13 + 100)
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var2 = var1
                    break
                var2 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                if var3:
                    # Unknown: memory.copy []
                i32_store(var4, var2)
                var3 = i32_load(var4 + 8)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var2 + (var3 << 2)), var5)
                var5 = i32_load(var13 + 104)
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var1 = var2
                    break
                var1 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var1 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                if var3:
                    # Unknown: memory.copy []
                i32_store(var4, var1)
                var3 = i32_load(var4 + 8)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var1 + (var3 << 2)), var5)
                var5 = i32_load(var13 + 108)
                var3 = i32_load(var4 + 8)
                if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
                    var2 = var1
                    break
                var2 = (i32_load(var4 + 12) + var3)
                i32_store(var4 + 4, (i32_load(var4 + 12) + var3))
                var2 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
                if var3:
                    # Unknown: memory.copy []
                i32_store(var4, var2)
                var3 = i32_load(var4 + 8)
                i32_store(var4 + 8, (var3 + 1))
                i32_store((var2 + (var3 << 2)), var5)
                var3 = i32_load(9142848)
                var10 = (var10 + 1)
                var4 = i32_load(9142892)
                if (1 if (var10 + 1) < i32_load(9142892) else 0):
                    continue
                break  # end loop
            if (1 if var4 < 2 else 0):
                break
            var2 = i32_load(39164)
            var1 = i32_load(9561692)
            var3 = 1
            while True:  # loop $label167
                var5 = (var1 + (var3 * 286704))
                if (1 if i32_load((((var1 + (var3 * 286704)) + (var2 << 2)) + 281808)) != 1 else 0):
                    break
                var6 = i32_load((var5 + 284240))
                if ((i32_load(9142848) * 25) % (i32_load((var5 + 284240)) - (var6 % 25))):
                    break
                var4 = i32_load(9142892)
                var2 = i32_load(39164)
                var1 = i32_load(9561692)
                var3 = (var3 + 1)
                if (1 if (var3 + 1) < var4 else 0):
                    continue
                break  # end loop
            if ((i32_load(9142848) * 25) % 2000):
                break
            func346()
            var4 = i32_load(9142892)
            if (1 if i32_load(9142892) < 2 else 0):
                break
            var7 = 1
            while True:  # loop $label173
                var4 = 0
                var10 = i32_load(9561692)
                while True:  # loop $label172
                    var2 = ((var4 * 404) + 9568096)
                    if (1 if i32_load(((var4 * 404) + 9568096) + 264) != 1 else 0):
                        break
                    if (1 if i32_load(var2 + 112) == 0 else 0):
                        break
                    var5 = i32_load((((var10 + (var7 * 286704)) + (var4 << 2)) + 284636))
                    if (1 if i32_load((((var10 + (var7 * 286704)) + (var4 << 2)) + 284636)) == 0 else 0):
                        break
                    var9 = i32_load(var5 + 8)
                    if (1 if i32_load(var5 + 8) == 0 else 0):
                        break
                    var3 = 0
                    while True:  # loop $label171
                        var1 = i32_load((i32_load(var5) + (var3 << 2)))
                        if (1 if i32_load((i32_load(var5) + (var3 << 2))) == 0 else 0):
                            break
                        var1 = (i32_load(9671128) + (var1 * 132))
                        var16 = i32_load((i32_load(9671128) + (var1 * 132)) + 84)
                        var6 = i32_load(var2 + 112)
                        if (1 if i32_load((i32_load(9671128) + (var1 * 132)) + 84) >= i32_load(var2 + 112) else 0):
                            break
                        var16 = (var16 + 10)
                        i32_store(var1 + 84, ((var16 + 10) if (1 if var6 > var16 else 0) else var6))
                        if (1 if i32_load(var1 + 92) == 0 else 0):
                            break
                        if i32_load(9140316):
                            if (1 if i32_load(9140320) != i32_load(var1 + 28) else 0):
                                break
                        var3 = (var3 + 1)
                        if (1 if (var3 + 1) != var9 else 0):
                            continue
                        break  # end loop
                    var4 = (var4 + 1)
                    if (1 if (var4 + 1) != 255 else 0):
                        continue
                    break  # end loop
                var7 = (var7 + 1)
                var4 = i32_load(9142892)
                if (1 if (var7 + 1) < i32_load(9142892) else 0):
                    continue
                break  # end loop
            var3 = (i32_load(9142848) * 25)
            if ((i32_load(9142848) * 25) % 7000):
                break
            i32_store(9684392, 0)
            if i32_load8_u(9216060):
                break
            if (1 if var4 == 0 else 0):
                var4 = 0
                break
            var10 = i32_load(9143004)
            var2 = i32_load(9561692)
            var7 = 0
            while True:  # loop $label178
                var1 = 0
                var6 = 0
                var5 = 0
                while True:  # loop $label177
                    var3 = 0
                    if i32_load8_u((var10 + ((var4 * var5) + var7))):
                        while True:  # loop $label176
                            var9 = ((var3 * 404) + 9568096)
                            var16 = i32_load(((var3 * 404) + 9568096) + 264)
                            if (1 if i32_load(((var3 * 404) + 9568096) + 264) == 3 else 0):
                                break
                            if (1 if i32_load(var9 + 188) != 55 else 0):
                                break
                            if (1 if var16 == 2 else 0):
                                break
                            var1 = (i32_load((((var2 + (var5 * 286704)) + (var3 << 2)) + 281808)) + var1)
                            var3 = (var3 + 1)
                            if (1 if (var3 + 1) != 255 else 0):
                                continue
                            break  # end loop
                        var6 = (var6 + 1)
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) != var4 else 0):
                        continue
                    break  # end loop
                i32_store((var2 + (var7 * 286704)) + 283924, (var1 + (var6 * 255)))
                var7 = (var7 + 1)
                var4 = i32_load(9142892)
                if (1 if (var7 + 1) < i32_load(9142892) else 0):
                    continue
                break  # end loop
            var3 = (i32_load(9142848) * 25)
            if (var3 % 1025):
                break
            if i32_load8_u(9216060):
                i32_store8(9682192, 1)
                var7 = i32_load(9142428)
                if (1 if i32_load(9142428) >= 48 else 0):
                    var1 = i32_load(9142440)
                    var16 = ((i32_load(9142440) & 0xFFFFFFFF) >> 1)
                    # Unknown: f64.convert_i32_u []
                    var66 = f32(((var1 * var1) * 1.52587890625e-05))
                    var1 = (((i32_load(51784) * var1) & 0xFFFFFFFF) // 100)
                    var17 = ((((i32_load(51784) * var1) & 0xFFFFFFFF) // 100) * var1)
                    var3 = 47
                    while True:  # loop $label193
                        var2 = (i32_load(9142424) + (var3 << 2))
                        var20 = i32_load((i32_load(9142424) + (var3 << 2)) + 16)
                        var21 = ((var3 + 7) if i32_load((i32_load(9142424) + (var3 << 2)) + 16) else var3)
                        var1 = i32_load(var2 + 4)
                        if (1 if i32_load(var2 + 4) == 1 else 0):
                            break
                        var4 = i32_load(var2 + 8)
                        var15 = (2147483647 if (1 if var1 == 2 else 0) else var1)
                        var1 = i32_load(var2)
                        # Unknown: f64.convert_i32_u []
                        var5 = i32_load(var2 + 12)
                        var105 = ((float((var66 * float(i32_load(var2)))) + 0.5) if i32_load(var2 + 12) else var1)
                        if ((1 if ((float((var66 * float(i32_load(var2)))) + 0.5) if i32_load(var2 + 12) else var1) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                            break
                        var1 = 0
                        var11 = ((0 if var1 else 1) if var5 else var1)
                        var10 = i32_load(9561692)
                        var9 = (var4 << 2)
                        var6 = i32_load(((i32_load(9561692) + (var4 << 2)) + 281808))
                        if (1 if var15 != 2147483647 else 0):
                            break
                        if (1 if i32_load(((var4 * 404) + 9568096) + 264) != 1 else 0):
                            break
                        var1 = i32_load(9142892)
                        if (1 if i32_load(9142892) < 2 else 0):
                            break
                        var5 = (var1 - 1)
                        var12 = ((var1 - 1) & 3)
                        var3 = 1
                        if (1 if (var1 - 2) >= 3 else 0):
                            var14 = (var5 & -4)
                            var5 = 0
                            while True:  # loop $label183
                                var1 = ((var10 + (var3 * 286704)) + var9)
                                var6 = (i32_load((((var10 + (var3 * 286704)) + var9) + 1141920)) + (i32_load((var1 + 855216)) + (i32_load((var1 + 568512)) + (i32_load((var1 + 281808)) + var6))))
                                var3 = (var3 + 4)
                                var5 = (var5 + 4)
                                if (1 if (var5 + 4) != var14 else 0):
                                    continue
                                break  # end loop
                        var1 = 0
                        if (1 if var12 == 0 else 0):
                            break
                        while True:  # loop $label184
                            var6 = (i32_load((((var10 + (var3 * 286704)) + var9) + 281808)) + var6)
                            var3 = (var3 + 1)
                            var1 = (var1 + 1)
                            if (1 if (var1 + 1) != var12 else 0):
                                continue
                            break  # end loop
                        if (1 if var6 >= var11 else 0):
                            break
                        var8 = (var2 + 20)
                        var12 = ((var4 * 404) + 9568096)
                        var5 = 0
                        while True:  # loop $label192
                            var1 = i32_load(9147324)
                            var3 = i32_load(9147316)
                            i32_store(9147324, i32_load(9147316))
                            var7 = i32_load(9147320)
                            var10 = i32_load(9147312)
                            i32_store(9147320, i32_load(9147312))
                            var1 = (var1 ^ (var1 << 11))
                            var2 = ((var10 ^ (((var10 & 0xFFFFFFFF) >> 19) ^ (((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8))) ^ var1)
                            i32_store(9147316, ((var10 ^ (((var10 & 0xFFFFFFFF) >> 19) ^ (((var1 ^ (var1 << 11)) & 0xFFFFFFFF) >> 8))) ^ var1))
                            var1 = (var7 ^ (var7 << 11))
                            var1 = ((((((var7 ^ (var7 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var1) ^ var2)
                            i32_store(9147312, ((((((var7 ^ (var7 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var2 & 0xFFFFFFFF) >> 19)) ^ var1) ^ var2))
                            var14 = i32_load(9142440)
                            var7 = (var1 % i32_load(9142440))
                            var9 = (var2 % var14)
                            var19 = i32_load(var12 + 264)
                            if (1 if (i32_load(var12 + 264) - 1) >= 2 else 0):
                                if (1 if i32_load8_u((i32_load(9147288) + ((var7 * var14) + var9))) != 3 else 0):
                                    break
                                if var19:
                                    break
                                i32_store(9147320, var2)
                                i32_store(9147324, var10)
                                i32_store(9147316, var1)
                                var2 = ((var3 << 11) ^ var3)
                                var1 = (((((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var1)
                                i32_store(9147312, (((((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var1))
                                break
                            var14 = (var9 - var16)
                            var14 = (var7 - var16)
                            if (1 if ((((var9 - var16) * var14) + ((var7 - var16) * var14)) - 1) <= var17 else 0):
                                break
                            if (1 if var4 != i32_load(38504) else 0):
                                break
                            i32_store(9147320, var2)
                            i32_store(9147324, var10)
                            i32_store(9147316, var1)
                            var2 = ((var3 << 11) ^ var3)
                            var1 = (((((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var1)
                            i32_store(9147312, (((((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var2) ^ var1))
                            var1 = func34(var15, (var2 % var14), var7, (var1 & 7), (var1 % 3), 1)
                            if (1 if func34(var15, (var2 % var14), var7, (var1 & 7), (var1 % 3), 1) == 0 else 0):
                                break
                            if var20:
                                func148(var1, var8, 1)
                            if (1 if i32_load(var12 + 216) != 1 else 0):
                                break
                            var2 = i32_load(i32_load(9142424) + 48)
                            if i32_load(i32_load(9142424) + 48):
                                if (1 if i32_load8_u(9147152) == 0 else 0):
                                    break
                            var3 = i32_load(9142440)
                            break
                            var3 = i32_load(9142440)
                            var1 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var7) + var9) << 1)))
                            if (1 if var2 == 2 else 0):
                                if (1 if var1 > 1 else 0):
                                    break
                                break
                            if (1 if var1 == 0 else 0):
                                break
                            func80(float(var9), float(var7), i32_load(9142536), 32.0, float((var3 * 96)))
                            var6 = (var6 + 1)
                            var5 = (var5 + 1)
                            if ((1 if var6 < var11 else 0) & (1 if var5 < 200 else 0)):
                                continue
                            break  # end loop
                        var7 = i32_load(9142428)
                        var3 = (var21 + 5)
                        if (1 if (var21 + 5) < var7 else 0):
                            continue
                        break  # end loop
                    var4 = i32_load(9142892)
                i32_store8(9682192, 0)
            var5 = 1
            if (1 if var4 > 1 else 0):
                while True:  # loop $label201
                    var4 = i32_load((((i32_load(9561692) + (var5 * 286704)) + (i32_load(38528) << 2)) + 284636))
                    if (1 if i32_load((((i32_load(9561692) + (var5 * 286704)) + (i32_load(38528) << 2)) + 284636)) == 0 else 0):
                        break
                    var3 = 0
                    var7 = 0
                    var9 = i32_load(var4 + 8)
                    if (1 if i32_load(var4 + 8) == 0 else 0):
                        break
                    while True:  # loop $label200
                        var1 = i32_load((i32_load(var4) + (var3 << 2)))
                        if (1 if i32_load((i32_load(var4) + (var3 << 2))) == 0 else 0):
                            break
                        var2 = i32_load(9671128)
                        var10 = (var2 + (var1 * 132))
                        var16 = i32_load((var2 + (var1 * 132)) + 28)
                        var1 = (i32_load(9671128) + (i32_load((var2 + (var1 * 132)) + 28) * 132))
                        var15 = i32_load8_u((i32_load(9671128) + (i32_load((var2 + (var1 * 132)) + 28) * 132)) + 125)
                        # br_table ['$label196', '$label197', '$label197', '$label197', '$label197', '$label197', '$label197', '$label197', '$label197', '$label198', '$label197']
                        _br_idx = (i32_load8_u((i32_load(9671128) + (i32_load((var2 + (var1 * 132)) + 28) * 132)) + 125) - 3)
                        break  # br_table
                        var6 = i32_load(var1 + 72)
                        var2 = i32_load(var1 + 76)
                        if (1 if i32_load(var1 + 72) < i32_load(var1 + 76) else 0):
                            var6 = (i32_load(((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 284072)) + var6)
                            var6 = ((i32_load(((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 284072)) + var6) if (1 if var2 > var6 else 0) else var2)
                            i32_store(var1 + 72, ((i32_load(((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 284072)) + var6) if (1 if var2 > var6 else 0) else var2))
                        var11 = i32_load(var1 + 96)
                        if (1 if i32_load(var1 + 96) == 0 else 0):
                            break
                        var11 = (i32_load(9671128) + (var11 * 132))
                        if (1 if (i32_load8_u((i32_load(9671128) + (var11 * 132)) + 125) & 251) != 3 else 0):
                            if (1 if i32_load(var11 + 32) == var16 else 0):
                                break
                        i32_store(var1 + 96, 0)
                        var16 = 0
                        if (1 if var15 == 1 else 0):
                            break
                        if (1 if var2 != var6 else 0):
                            break
                        if var16:
                            break
                        if i32_load(var1 + 36):
                            break
                        func403(var1)
                        var6 = i32_load(var1 + 80)
                        var16 = (i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704))
                        var2 = i32_load(((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 284320))
                        if (1 if i32_load(var1 + 80) >= i32_load(((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 284320)) else 0):
                            break
                        var1 = (i32_load((var16 + 284076)) + var6)
                        i32_store(var1 + 80, ((i32_load((var16 + 284076)) + var6) if (1 if var1 < var2 else 0) else var2))
                        if (1 if i32_load(var10 + 92) == 0 else 0):
                            break
                        if i32_load(9140316):
                            if (1 if i32_load(9140320) != i32_load(var10 + 28) else 0):
                                break
                        var7 = 1
                        var3 = (var3 + 1)
                        if (1 if (var3 + 1) != var9 else 0):
                            continue
                        break  # end loop
                    if (1 if (var7 & 1) == 0 else 0):
                        break
                    var5 = (var5 + 1)
                    if (1 if (var5 + 1) < i32_load(9142892) else 0):
                        continue
                    break  # end loop
            var3 = i32_load(9142424)
            var9 = i32_load(i32_load(9142424) + 32)
            if (1 if i32_load(i32_load(9142424) + 32) == 0 else 0):
                break
            var1 = (i32_load(9142848) * 25)
            var16 = i32_load(var3 + 56)
            if (1 if (i32_load(9142848) * 25) < (i32_load(var3 + 56) * 1000) else 0):
                break
            var2 = i32_load(9684364)
            var4 = i32_load(var3 + 84)
            var5 = i32_load(9684372)
            if (1 if i32_load(9684372) <= var1 else 0):
                if ((1 if var2 >= var4 else 0) if var2 else 0):
                    break
                var6 = i32_load(9142440)
                var67 = float((i32_load(9142440) << 4))
                var66 = (float((i32_load(9142440) << 4)) * 1.41421294)
                if var2:
                    break
                var70 = var66
                break
            if var2:
                break
            var6 = i32_load(9142440)
            var67 = float((i32_load(9142440) << 4))
            var70 = (float((i32_load(9142440) << 4)) * 1.41421294)
            var66 = (float((i32_load(9142440) << 4)) * 1.41421294)
            var2 = 0
            f32_store(9684348, var67)
            f32_store(9684356, var70)
            f32_store(9684352, var67)
            break
            var70 = f32_load(9684360)
            f32_store(9684356, f32_load(9684360))
            var67 = f32_load(9684352)
            var68 = f32_load(9684348)
            f32_store(9684344, var67)
            f32_store(9684340, var68)
            var5 = (var2 + 1)
            i32_store(9684364, (var2 + 1))
            var66 = ((math.floor((((var66 * float((var4 - var5))) / float(var4)) * 0.03125)) * 32.0) + 0.5)
            f32_store(9684360, ((math.floor((((var66 * float((var4 - var5))) / float(var4)) * 0.03125)) * 32.0) + 0.5))
            var71 = float((i32_load(var3 + 92) << 5))
            if (1 if float((i32_load(var3 + 92) << 5)) > var66 else 0):
                f32_store(9684360, var71)
                var66 = var71
            var69 = var67
            var71 = var68
            # br_table ['$label206', '$label207', '$label208']
            _br_idx = (i32_load(var3 + 20) - 1)
            break  # br_table
            var4 = i32_load(9147324)
            i32_store(9147324, i32_load(9147316))
            var7 = i32_load(9147320)
            var10 = i32_load(9147312)
            i32_store(9147320, i32_load(9147312))
            var4 = (var4 ^ (var4 << 11))
            var4 = ((var10 ^ (((var10 & 0xFFFFFFFF) >> 19) ^ (((var4 ^ (var4 << 11)) & 0xFFFFFFFF) >> 8))) ^ var4)
            i32_store(9147316, ((var10 ^ (((var10 & 0xFFFFFFFF) >> 19) ^ (((var4 ^ (var4 << 11)) & 0xFFFFFFFF) >> 8))) ^ var4))
            var7 = (var7 ^ (var7 << 11))
            var7 = ((((((var7 ^ (var7 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var4 & 0xFFFFFFFF) >> 19)) ^ var7) ^ var4)
            i32_store(9147312, ((((((var7 ^ (var7 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var4 & 0xFFFFFFFF) >> 19)) ^ var7) ^ var4))
            var10 = (var6 << 5)
            var69 = float(((var6 << 5) - 32))
            var71 = (float(var6) * 32.0)
            var71 = (((float(var6) * 32.0) if (1 if var70 > var71 else 0) else var70) - var66)
            if (1 if abs((((float(var6) * 32.0) if (1 if var70 > var71 else 0) else var70) - var66)) < 2147483650.0 else 0):
                break
            var4 = -2147483648
            var4 = (int(var71) if (1 if var4 <= 2 else 0) else -2147483648)
            var71 = (var4 + float((((2 % (int(var71) if (1 if var4 <= 2 else 0) else -2147483648)) << 1) - var4)))
            var71 = (var68 if (1 if var71 < 0.0 else 0) else (var4 + float((((2 % (int(var71) if (1 if var4 <= 2 else 0) else -2147483648)) << 1) - var4))))
            var73 = float(var10)
            var71 = ((math.floor(((0.0 if (1 if var71 >= float(var10) else 0) else (var68 if (1 if var71 < 0.0 else 0) else (var4 + float((((2 % (int(var71) if (1 if var4 <= 2 else 0) else -2147483648)) << 1) - var4))))) * 0.03125)) * 32.0) + 0.5)
            f32_store(float(((var6 << 5) - 32)), ((math.floor(((0.0 if (1 if var71 >= float(var10) else 0) else (var68 if (1 if var71 < 0.0 else 0) else (var4 + float((((2 % (int(var71) if (1 if var4 <= 2 else 0) else -2147483648)) << 1) - var4))))) * 0.03125)) * 32.0) + 0.5))
            var69 = (var67 + float((((var7 % var4) << 1) - var4)))
            var69 = (0.0 if (1 if var69 < 0.0 else 0) else (var67 + float((((var7 % var4) << 1) - var4))))
            break
            var4 = i32_load(9147324)
            i32_store(9147324, i32_load(9147316))
            var7 = i32_load(9147320)
            var10 = i32_load(9147312)
            i32_store(9147320, i32_load(9147312))
            var4 = (var4 ^ (var4 << 11))
            var4 = ((var10 ^ (((var10 & 0xFFFFFFFF) >> 19) ^ (((var4 ^ (var4 << 11)) & 0xFFFFFFFF) >> 8))) ^ var4)
            i32_store(9147316, ((var10 ^ (((var10 & 0xFFFFFFFF) >> 19) ^ (((var4 ^ (var4 << 11)) & 0xFFFFFFFF) >> 8))) ^ var4))
            var6 = (var6 << 5)
            var71 = (float((var4 % (var6 << 5))) + 0.5)
            f32_store(9684348, (float((var4 % (var6 << 5))) + 0.5))
            var7 = (var7 ^ (var7 << 11))
            var4 = ((((((var7 ^ (var7 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var4 & 0xFFFFFFFF) >> 19)) ^ var7) ^ var4)
            i32_store(9147312, ((((((var7 ^ (var7 << 11)) & 0xFFFFFFFF) >> 8) ^ ((var4 & 0xFFFFFFFF) >> 19)) ^ var7) ^ var4))
            var69 = (float((var4 % var6)) + 0.5)
            f32_store(((math.floor(((var69 if (1 if var69 >= var73 else 0) else (0.0 if (1 if var69 < 0.0 else 0) else (var67 + float((((var7 % var4) << 1) - var4))))) * 0.03125)) * 32.0) + 0.5), (float((var4 % var6)) + 0.5))
            i32_store(9684368, var1)
            var3 = i32_load(var3 + 96)
            if var2:
                var1 = ((var3 * 1000) + var1)
                i32_store(9684368, ((var3 * 1000) + var1))
            f64_store(var13 + 32, float(var70))
            i32_store(var13 + 40, var1)
            i32_store(var13 + 76, var5)
            f64_store(var13 + 48, float((var71 - var68)))
            f64_store(var13 + 56, float((var69 - var67)))
            f64_store((var13 - -64), float((var66 - var70)))
            var2 = ((((var2 * var3) + var16) * 1000) + ((var5 * var9) * 60000))
            i32_store(9684372, ((((var2 * var3) + var16) * 1000) + ((var5 * var9) * 60000)))
            i32_store(var13 + 72, (var2 - var1))
            f64_store(var13 + 16, float(var68))
            f64_store(var13 + 24, float(var67))
            a_b()
            var1 = (i32_load(9142848) * 25)
            var5 = i32_load(9684372)
            var67 = 1.0
            var1 = i32_load(9684368)
            var66 = (float(var1) - float(i32_load(9684368)))
            var70 = float((var5 - var1))
            if (1 if (float(var1) - float(i32_load(9684368))) > float((var5 - var1)) else 0):
                break
            if (1 if var1 == var5 else 0):
                break
            var67 = 0.0
            if (1 if var66 < 0.0 else 0):
                break
            var67 = (var66 / var70)
            if (1 if i32_load(9671136) < 4 else 0):
                break
            var66 = f32_load(9684344)
            var105 = ((float((((f32_load(9684352) - f32_load(9684344)) * var67) + var66)) + 0.5) * 0.03125)
            if (1 if abs(((float((((f32_load(9684352) - f32_load(9684344)) * var67) + var66)) + 0.5) * 0.03125)) < 2147483648.0 else 0):
                break
            var4 = (-2147483648 << 1)
            var66 = f32_load(9684340)
            var105 = (float(((((f32_load(9684348) - f32_load(9684340)) * var67) + var66) * 0.03125)) + 0.5)
            if (1 if abs((float(((((f32_load(9684348) - f32_load(9684340)) * var67) + var66) * 0.03125)) + 0.5)) < 2147483648.0 else 0):
                break
            var6 = (-2147483648 << 1)
            var66 = f32_load(9684356)
            var105 = (float(((((f32_load(9684360) - f32_load(9684356)) * var67) + var66) * 0.03125)) + 0.5)
            if (1 if abs((float(((((f32_load(9684360) - f32_load(9684356)) * var67) + var66) * 0.03125)) + 0.5)) < 2147483648.0 else 0):
                break
            var1 = (-2147483648 << 1)
            var7 = ((-2147483648 << 1) * var1)
            var3 = 3
            while True:  # loop $label216
                var3 = ((i32_load(9684380) if (1 if var3 == i32_load(9684376) else 0) else 0) + var3)
                var1 = (i32_load(9671128) + (((i32_load(9684380) if (1 if var3 == i32_load(9684376) else 0) else 0) + var3) * 132))
                if (1 if i32_load8_u((i32_load(9671128) + (((i32_load(9684380) if (1 if var3 == i32_load(9684376) else 0) else 0) + var3) * 132)) + 125) == 3 else 0):
                    break
                var2 = ((i32_load8_u(var1 + 122) * 404) + 9568096)
                var5 = ((i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 220) - var4) + (i32_load16_u(var1 + 114) << 1))
                var5 = ((i32_load(var2 + 216) - var6) + (i32_load16_u(var1 + 112) << 1))
                if (1 if (((((i32_load(((i32_load8_u(var1 + 122) * 404) + 9568096) + 220) - var4) + (i32_load16_u(var1 + 114) << 1)) * var5) + (((i32_load(var2 + 216) - var6) + (i32_load16_u(var1 + 112) << 1)) * var5)) - 1) <= var7 else 0):
                    break
                var5 = i32_load(var2 + 264)
                if ((1 if i32_load(var2 + 264) == 1 else 0) & (1 if i32_load(var2 + 188) != 55 else 0)):
                    break
                if (1 if var5 == 2 else 0):
                    break
                if (1 if i32_load(var1 + 64) == -1 else 0):
                    break
                if i32_load(var1 + 36):
                    break
                func103(var1)
                if (1 if i32_load8_u(var1 + 125) == 3 else 0):
                    break
                var2 = (var1 - -64)
                var10 = i32_load((var1 - -64))
                var5 = i32_load(i32_load(9142424) + 88)
                if (1 if i32_load((var1 - -64)) <= i32_load(i32_load(9142424) + 88) else 0):
                    i32_store(var2, 0)
                    break
                i32_store(var2, (var10 - var5))
                if (1 if i32_load(var1 + 92) == 0 else 0):
                    break
                if i32_load8_u(9147141):
                    break
                i32_store(var13, var5)
                a_b()
                var3 = (var3 + 1)
                if (1 if (var3 + 1) < i32_load(9671136) else 0):
                    continue
                break  # end loop
            global global0
            global0 = (var13 + 112)
            i32_store8(9147140, 1)
            if (1 if i32_load(9215892) >= 5 else 0):
                var1 = i32_load(9215884)
                var2 = 4
                while True:  # loop $label218
                    var5 = (var2 << 2)
                    if (1 if i32_load((var1 + (var2 << 2))) != i32_load(9142848) else 0):
                        break
                    i32_store(9671116, var2)
                    var3 = ((var2 | 2) << 2)
                    var4 = ((var2 | 3) << 2)
                    var6 = ((var2 | 1) << 2)
                    # call_indirect via table[i32_load(((i32_load((var1 + ((var2 | 1) << 2))) * 40) + 9671200) + 20)]
                    var1 = i32_load(9215884)
                    var5 = (i32_load(9215884) + var5)
                    if (1 if i32_load((i32_load(9215884) + var5)) == i32_load(9142848) else 0):
                        i32_store(var5, 0)
                    if (1 if i32_load8_u(59128) == 0 else 0):
                        break
                    var5 = i32_load((var1 + var4))
                    var3 = i32_load((var1 + var3))
                    var4 = i32_load((var1 + var6))
                    var6 = i32_load((i32_load(9671128) + 1690568))
                    i32_store(var0 + 48, i32_load((var1 + (i32_load((i32_load(9671128) + 1690568)) << 4))))
                    i32_store(var0 + 52, var6)
                    i32_store(var0 + 56, i32_load(9142848))
                    i32_store(var0 + 32, i32_load(9671116))
                    i32_store(var0 + 36, var4)
                    i32_store(var0 + 40, var3)
                    i32_store(var0 + 44, var5)
                    var1 = i32_load(9215884)
                    var2 = (var2 + 4)
                    if (1 if (var2 + 4) < i32_load(9215892) else 0):
                        continue
                    break  # end loop
            var1 = i32_load(9142848)
            var2 = (i32_load(9142848) + 1)
            i32_store(9142848, (i32_load(9142848) + 1))
            i32_store8(9147140, 0)
            var2 = (var2 * 25)
            if (((var2 * 25) % 1025) if var1 else 0):
            else:
                if (1 if i32_load(9213808) != 1 else 0):
                    break
                var1 = (i32_load(9671128) + (i32_load(9173808) * 132))
                if (1 if i32_load(((i32_load8_u((i32_load(9671128) + (i32_load(9173808) * 132)) + 122) * 404) + 9568096) + 264) != 1 else 0):
                    break
                var2 = i32_load(var1 + 44)
                if (1 if i32_load(var1 + 44) == 0 else 0):
                    break
                var2 = i32_load((i32_load(9215884) + (var2 << 4)) + 4)
                # br_table ['$label220', '$label219', '$label219', '$label220', '$label221']
                _br_idx = (i32_load((i32_load(9215884) + (var2 << 4)) + 4) - 2)
                break  # br_table
                if (1 if var2 != 34 else 0):
                    break
                if (1 if i32_load(var1 + 92) == 0 else 0):
                    break
                if i32_load(9140316):
                    if (1 if i32_load(9140320) != i32_load(var1 + 28) else 0):
                        break
                var51 = 0
                var54 = 0
                var55 = 0
                var56 = 0
                var57 = 0
                var58 = 0
                var59 = 0
                var60 = 0
                var61 = 0
                var19 = (global0 - 96)
                global global0
                global0 = (global0 - 96)
                if (1 if i32_load(9142892) >= 2 else 0):
                    var40 = 1
                    while True:  # loop $label602
                        var62 = (var40 * 286704)
                        var8 = ((var40 * 286704) + i32_load(9561692))
                        if (1 if i32_load(((var40 * 286704) + i32_load(9561692)) + 286684) == 0 else 0):
                            break
                        var9 = (var8 + 283960)
                        var1 = i32_load(var8 + 283960)
                        if (1 if i32_load(var8 + 283960) >= 3 else 0):
                            func425(var8)
                            var1 = i32_load(var9)
                            if (1 if i32_load(var9) > 2 else 0):
                                break
                        var13 = i32_load(((var1 << 2) + 9940))
                        if (1 if i32_load(var8 + 283872) == 0 else 0):
                            if (1 if i32_load(var8 + 283876) == 0 else 0):
                                break
                        var5 = (var8 + 286684)
                        i64_store(var19 + 72, 0)
                        i64_store(var19 + 64, 0)
                        var12 = i32_load(var19 + 80)
                        var14 = i32_load(var19 + 84)
                        var11 = i32_load(var19 + 88)
                        var17 = i32_load(var19 + 92)
                        f32_store(var19 + 48, float(i32_load(var8 + 283984)))
                        f32_store(var19 + 52, float(i32_load((var8 + 283988))))
                        f32_store(var19 + 56, float(i32_load((var8 + 283992))))
                        var1 = i32_load((var8 + 283996))
                        var2 = 0
                        i32_store(9140296, 0)
                        f32_store(var19 + 60, float(var1))
                        while True:  # loop $label223
                            var1 = (var8 + (var2 * 1056))
                            var3 = ((var8 + (var2 * 1056)) + 1150)
                            if i32_load8_u(((var8 + (var2 * 1056)) + 1150)):
                                i32_store8((var1 + 1151), 0)
                                i32_store((var1 + 1140), 0)
                                i32_store(var1 + 624, 0)
                                i32_store(var1 + 96, 0)
                                i64_store(var1 + 104, 0)
                                i32_store8(var3, 0)
                            var2 = (var2 + 1)
                            if (1 if (var2 + 1) != 255 else 0):
                                continue
                            break  # end loop
                        var16 = 0
                        var6 = i32_load(i32_load(9142424) + 40)
                        if (1 if i32_load(var9) == i32_load(39224) else 0):
                            break
                        var16 = 1
                        var1 = (var8 + (i32_load(38528) << 2))
                        if (1 if i32_load(((var8 + (i32_load(38528) << 2)) + 282828)) != (0 - i32_load((var1 + 281808))) else 0):
                            break
                        if (1 if var11 > 999 else 0):
                            break
                        var1 = (var8 + (i32_load(38500) << 2))
                        var16 = (1 if (i32_load(((var8 + (i32_load(38500) << 2)) + 282828)) + i32_load((var1 + 281808))) > 14 else 0)
                        var7 = (1 if i32_load(var8 + 283976) < 200 else 0)
                        if (1 if i32_load(var8 + 283940) == 0 else 0):
                            break
                        var1 = i32_load(38720)
                        var2 = (var8 + (i32_load(38720) << 2))
                        var4 = (i32_load(((var8 + (i32_load(38720) << 2)) + 282828)) + i32_load((var2 + 281808)))
                        var3 = 3
                        var2 = ((var1 * 404) + 9568096)
                        if (1 if i32_load(((var1 * 404) + 9568096) + 264) <= 1 else 0):
                            var3 = (i32_load(var5) * 3)
                            var3 = (1 if (1 if var3 < 100 else 0) else (((i32_load(var5) * 3) & 0xFFFFFFFF) // 100))
                        if (1 if var3 <= var4 else 0):
                            break
                        if i32_load8_u(var2 + 354):
                            break
                        var2 = (var8 + (var1 * 1056))
                        i32_store8(((var8 + (var1 * 1056)) + 1150), 1)
                        var4 = (var3 - var4)
                        i32_store(var2 + 108, (var3 - var4))
                        var66 = float(var3)
                        f32_store(var2 + 100, (280.0 / float(var3)))
                        f32_store(var2 + 96, ((float(var4) * 280.0) / var66))
                        var2 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var2 << 2) + 8451904), var1)
                        var3 = 2
                        var1 = i32_load(38716)
                        var2 = (var8 + (i32_load(38716) << 2))
                        var4 = (i32_load(((var8 + (i32_load(38716) << 2)) + 282828)) + i32_load((var2 + 281808)))
                        var2 = ((var1 * 404) + 9568096)
                        if (1 if i32_load(((var1 * 404) + 9568096) + 264) <= 1 else 0):
                            var3 = (i32_load(var5) << 1)
                            var3 = (1 if (1 if var3 < 100 else 0) else (((i32_load(var5) << 1) & 0xFFFFFFFF) // 100))
                        if (1 if var3 <= var4 else 0):
                            break
                        if i32_load8_u(var2 + 354):
                            break
                        var2 = (var8 + (var1 * 1056))
                        i32_store8(((var8 + (var1 * 1056)) + 1150), 1)
                        var4 = (var3 - var4)
                        i32_store(var2 + 108, (var3 - var4))
                        var66 = float(var3)
                        f32_store(var2 + 100, (220.0 / float(var3)))
                        f32_store(var2 + 96, ((float(var4) * 220.0) / var66))
                        var2 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var2 << 2) + 8451904), var1)
                        var1 = (200 if var7 else var6)
                        var2 = i32_load(var9)
                        if (1 if i32_load(var9) == i32_load(57156) else 0):
                            var4 = i32_load(38444)
                            var2 = (var8 + (i32_load(38444) << 2))
                            var6 = i32_load(((var8 + (i32_load(38444) << 2)) + 281808))
                            var7 = i32_load((var2 + 282828))
                            var1 = (((var1 * 125) & 0xFFFFFFFF) // 100)
                            var2 = (((var1 * 35) & 0xFFFFFFFF) // 100)
                            var48 = ((((var1 * 125) & 0xFFFFFFFF) // 100) - (((var1 * 35) & 0xFFFFFFFF) // 100))
                            # Unknown: f64.convert_i32_u []
                            var106 = ((((var1 * 125) & 0xFFFFFFFF) // 100) - (((var1 * 35) & 0xFFFFFFFF) // 100))
                            var105 = (((((var1 * 125) & 0xFFFFFFFF) // 100) - (((var1 * 35) & 0xFFFFFFFF) // 100)) * 0.2)
                            if ((1 if (((((var1 * 125) & 0xFFFFFFFF) // 100) - (((var1 * 35) & 0xFFFFFFFF) // 100)) * 0.2) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                                break
                            var1 = 0
                            var3 = 0
                            var10 = ((var4 * 404) + 9568096)
                            if (1 if i32_load(((var4 * 404) + 9568096) + 264) <= 1 else 0):
                                var3 = (i32_load(var5) * var1)
                                var3 = (1 if (1 if var3 < 100 else 0) else (((i32_load(var5) * var1) & 0xFFFFFFFF) // 100))
                            var7 = (var6 + var7)
                            if (1 if (var6 + var7) >= var3 else 0):
                                break
                            if i32_load8_u(var10 + 354):
                                break
                            var6 = (var8 + (var4 * 1056))
                            i32_store8(((var8 + (var4 * 1056)) + 1150), 1)
                            var7 = (var3 - var7)
                            i32_store(var6 + 108, (var3 - var7))
                            var66 = float(var3)
                            f32_store(var6 + 100, (90.0 / float(var3)))
                            f32_store(var6 + 96, ((float(var7) * 90.0) / var66))
                            var3 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var3 << 2) + 8451904), var4)
                            var4 = i32_load(38436)
                            var3 = (var8 + (i32_load(38436) << 2))
                            var6 = i32_load(((var8 + (i32_load(38436) << 2)) + 281808))
                            var7 = i32_load((var3 + 282828))
                            var10 = ((var4 * 404) + 9568096)
                            var15 = (1 if i32_load(((var4 * 404) + 9568096) + 264) > 1 else 0)
                            var105 = (var106 * 0.4)
                            if ((1 if (var106 * 0.4) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                                break
                            var3 = 0
                            if (1 if var15 == 0 else 0):
                                var3 = (i32_load(var5) * var3)
                                var3 = (1 if (1 if var3 < 100 else 0) else (((i32_load(var5) * var3) & 0xFFFFFFFF) // 100))
                            var7 = (var6 + var7)
                            if (1 if (var6 + var7) >= var3 else 0):
                                break
                            if i32_load8_u(var10 + 354):
                                break
                            var6 = (var8 + (var4 * 1056))
                            i32_store8(((var8 + (var4 * 1056)) + 1150), 1)
                            var7 = (var3 - var7)
                            i32_store(var6 + 108, (var3 - var7))
                            var66 = float(var3)
                            f32_store(var6 + 100, (120.0 / float(var3)))
                            f32_store(var6 + 96, ((float(var7) * 120.0) / var66))
                            var3 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var3 << 2) + 8451904), var4)
                            var4 = i32_load(57152)
                            var3 = (var8 + (i32_load(57152) << 2))
                            var7 = (i32_load(((var8 + (i32_load(57152) << 2)) + 282828)) + i32_load((var3 + 281808)))
                            var3 = var1
                            var6 = ((var4 * 404) + 9568096)
                            if (1 if i32_load(((var4 * 404) + 9568096) + 264) <= 1 else 0):
                                var3 = (i32_load(var5) * var1)
                                var3 = (1 if (1 if var3 < 100 else 0) else (((i32_load(var5) * var1) & 0xFFFFFFFF) // 100))
                            if (1 if var3 <= var7 else 0):
                                break
                            if i32_load8_u(var6 + 354):
                                break
                            var6 = (var8 + (var4 * 1056))
                            i32_store8(((var8 + (var4 * 1056)) + 1150), 1)
                            var7 = (var3 - var7)
                            i32_store(var6 + 108, (var3 - var7))
                            var66 = float(var3)
                            f32_store(var6 + 100, (120.0 / float(var3)))
                            f32_store(var6 + 96, ((float(var7) * 120.0) / var66))
                            var3 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var3 << 2) + 8451904), var4)
                            var3 = i32_load(38424)
                            var4 = (var8 + (i32_load(38424) << 2))
                            var6 = (i32_load(((var8 + (i32_load(38424) << 2)) + 282828)) + i32_load((var4 + 281808)))
                            var4 = ((var3 * 404) + 9568096)
                            if (1 if i32_load(((var3 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = (i32_load(var5) * var1)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * var1) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var6 else 0):
                                break
                            if i32_load8_u(var4 + 354):
                                break
                            var4 = (var8 + (var3 * 1056))
                            i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                            var6 = (var1 - var6)
                            i32_store(var4 + 108, (var1 - var6))
                            var66 = float(var1)
                            f32_store(var4 + 100, (80.0 / float(var1)))
                            f32_store(var4 + 96, ((float(var6) * 80.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var3)
                            var1 = i32_load(var8 + 283868)
                            if (1 if i32_load(var8 + 283868) != (i32_load((var8 + 284372)) + (i32_load((var8 + 284380)) * i32_load(var8 + 283864))) else 0):
                                if (1 if var1 < i32_load((var8 + 284376)) else 0):
                                    break
                            var3 = i32_load(38636)
                            var1 = (var8 + (i32_load(38636) << 2))
                            var6 = (i32_load(((var8 + (i32_load(38636) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var4 = ((var3 * 404) + 9568096)
                            if (1 if i32_load(((var3 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var6 else 0):
                                break
                            if i32_load8_u(var4 + 354):
                                break
                            var4 = (var8 + (var3 * 1056))
                            i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                            var6 = (var1 - var6)
                            i32_store(var4 + 108, (var1 - var6))
                            var66 = float(var1)
                            f32_store(var4 + 100, (46.0 / float(var1)))
                            f32_store(var4 + 96, ((float(var6) * 46.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var3)
                            var3 = i32_load(38476)
                            var1 = (var8 + (i32_load(38476) << 2))
                            var6 = (i32_load(((var8 + (i32_load(38476) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 34
                            var4 = ((var3 * 404) + 9568096)
                            if (1 if i32_load(((var3 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = (i32_load(var5) * 34)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 34) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var6 else 0):
                                break
                            if i32_load8_u(var4 + 354):
                                break
                            var4 = (var8 + (var3 * 1056))
                            i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                            var6 = (var1 - var6)
                            i32_store(var4 + 108, (var1 - var6))
                            var66 = float(var1)
                            f32_store(var4 + 100, (121.0 / float(var1)))
                            f32_store(var4 + 96, ((float(var6) * 121.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var3)
                            var1 = (var8 + (var13 << 2))
                            var3 = (i32_load(((var8 + (var13 << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = ((var13 * 404) + 9568096)
                            if (1 if i32_load(((var13 * 404) + 9568096) + 264) <= 1 else 0):
                                var2 = (i32_load(var5) * var2)
                                var2 = (1 if (1 if var2 < 100 else 0) else (((i32_load(var5) * var2) & 0xFFFFFFFF) // 100))
                            if (1 if var2 <= var3 else 0):
                                break
                            if i32_load8_u(var1 + 354):
                                break
                            var1 = (var8 + (var13 * 1056))
                            i32_store8(((var8 + (var13 * 1056)) + 1150), 1)
                            var3 = (var2 - var3)
                            i32_store(var1 + 108, (var2 - var3))
                            var66 = float(var2)
                            f32_store(var1 + 100, (400.0 / float(var2)))
                            f32_store(var1 + 96, ((float(var3) * 400.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var13)
                            if (1 if var11 <= 1999 else 0):
                                var2 = i32_load(39096)
                                var1 = (var8 + (i32_load(39096) << 2))
                                var4 = (i32_load(((var8 + (i32_load(39096) << 2)) + 282828)) + i32_load((var1 + 281808)))
                                var1 = 1
                                var3 = ((var2 * 404) + 9568096)
                                if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                    var1 = i32_load(var5)
                                    var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                                if (1 if var1 <= var4 else 0):
                                    break
                                if i32_load8_u(var3 + 354):
                                    break
                                var3 = (var8 + (var2 * 1056))
                                i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                                var4 = (var1 - var4)
                                i32_store(var3 + 108, (var1 - var4))
                                var66 = float(var1)
                                f32_store(var3 + 100, (1001.0 / float(var1)))
                                f32_store(var3 + 96, ((float(var4) * 1001.0) / var66))
                                var1 = i32_load(9140296)
                                i32_store(9140296, (i32_load(9140296) + 1))
                                i32_store(((var1 << 2) + 8451904), var2)
                                break
                            if (1 if var11 > 7999999 else 0):
                                break
                            if var16:
                                var2 = i32_load(38528)
                                var1 = (var8 + (i32_load(38528) << 2))
                                var4 = (i32_load(((var8 + (i32_load(38528) << 2)) + 282828)) + i32_load((var1 + 281808)))
                                var1 = 60
                                var3 = ((var2 * 404) + 9568096)
                                if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                    var1 = (i32_load(var5) * 60)
                                    var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 60) & 0xFFFFFFFF) // 100))
                                if (1 if var1 <= var4 else 0):
                                    break
                                if i32_load8_u(var3 + 354):
                                    break
                                var3 = (var8 + (var2 * 1056))
                                i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                                var4 = (var1 - var4)
                                i32_store(var3 + 108, (var1 - var4))
                                var66 = float(var1)
                                f32_store(var3 + 100, (200.0 / float(var1)))
                                f32_store(var3 + 96, ((float(var4) * 200.0) / var66))
                                var1 = i32_load(9140296)
                                i32_store(9140296, (i32_load(9140296) + 1))
                                i32_store(((var1 << 2) + 8451904), var2)
                                var1 = i32_load(38512)
                                var2 = (var8 + (i32_load(38512) << 2))
                                var3 = (i32_load(((var8 + (i32_load(38512) << 2)) + 282828)) + i32_load((var2 + 281808)))
                                var2 = 14
                                var4 = ((var1 * 404) + 9568096)
                                if (1 if i32_load(((var1 * 404) + 9568096) + 264) <= 1 else 0):
                                    var2 = (i32_load(var5) * 14)
                                    var2 = (1 if (1 if var2 < 100 else 0) else (((i32_load(var5) * 14) & 0xFFFFFFFF) // 100))
                                if (1 if var2 <= var3 else 0):
                                    break
                                if i32_load8_u(var4 + 354):
                                    break
                                var66 = 301.0
                                var67 = float(var2)
                                f32_store((var8 + (var1 * 1056)) + 100, (301.0 / float(var2)))
                                break
                            var1 = i32_load(38500)
                            var2 = (var8 + (i32_load(38500) << 2))
                            var3 = (i32_load(((var8 + (i32_load(38500) << 2)) + 282828)) + i32_load((var2 + 281808)))
                            var2 = 15
                            var4 = ((var1 * 404) + 9568096)
                            if (1 if i32_load(((var1 * 404) + 9568096) + 264) <= 1 else 0):
                                var2 = (i32_load(var5) * 15)
                                var2 = (1 if (1 if var2 < 100 else 0) else (((i32_load(var5) * 15) & 0xFFFFFFFF) // 100))
                            if (1 if var2 <= var3 else 0):
                                break
                            if i32_load8_u(var4 + 354):
                                break
                            var66 = 800.0
                            var67 = float(var2)
                            f32_store((var8 + (var1 * 1056)) + 100, (800.0 / float(var2)))
                            var2 = (var2 - var3)
                            var3 = (var8 + (var1 * 1056))
                            i32_store8(((var8 + (var1 * 1056)) + 1150), 1)
                            i32_store(var3 + 108, var2)
                            f32_store(var3 + 96, ((var66 * float(var2)) / var67))
                            var2 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var2 << 2) + 8451904), var1)
                            if (1 if var14 > 79999 else 0):
                                break
                            var2 = i32_load(39076)
                            var1 = (var8 + (i32_load(39076) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39076) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (152.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 152.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39100)
                            var1 = (var8 + (i32_load(39100) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39100) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (151.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 151.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            if (1 if var12 > 79999 else 0):
                                break
                            var2 = i32_load(39068)
                            var1 = (var8 + (i32_load(39068) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39068) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (150.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 150.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            if (1 if var17 > 39999 else 0):
                                break
                            var2 = i32_load(39072)
                            var1 = (var8 + (i32_load(39072) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39072) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (110.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 110.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            if var16:
                                break
                            var2 = i32_load(39084)
                            var1 = (var8 + (i32_load(39084) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39084) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (200.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 200.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(38492)
                            var1 = (var8 + (i32_load(38492) << 2))
                            var4 = (i32_load(((var8 + (i32_load(38492) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 7
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = (i32_load(var5) * 7)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 7) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (800.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 800.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39088)
                            var1 = (var8 + (i32_load(39088) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39088) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (95.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 95.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39080)
                            var1 = (var8 + (i32_load(39080) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39080) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (95.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 95.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39092)
                            var1 = (var8 + (i32_load(39092) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39092) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (95.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 95.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39112)
                            var1 = (var8 + (i32_load(39112) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39112) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (40.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 40.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39124)
                            var1 = (var8 + (i32_load(39124) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39124) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (41.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 41.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39116)
                            var1 = (var8 + (i32_load(39116) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39116) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (42.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 42.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39180)
                            var1 = (var8 + (i32_load(39180) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39180) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (40.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 40.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39140)
                            var1 = (var8 + (i32_load(39140) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39140) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (41.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 41.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39148)
                            var1 = (var8 + (i32_load(39148) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39148) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (31.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 31.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(38440)
                            var1 = (var8 + (i32_load(38440) << 2))
                            var4 = (i32_load(((var8 + (i32_load(38440) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 3
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = (i32_load(var5) * 3)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 3) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (30.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 30.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var1 = 2
                            var2 = i32_load(38808)
                            var3 = (var8 + (i32_load(38808) << 2))
                            var4 = (i32_load(((var8 + (i32_load(38808) << 2)) + 282828)) + i32_load((var3 + 281808)))
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = (i32_load(var5) << 1)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) << 1) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (71.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 71.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(38456)
                            var1 = (var8 + (i32_load(38456) << 2))
                            var4 = (i32_load(((var8 + (i32_load(38456) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 5
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = (i32_load(var5) * 5)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (70.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 70.0) / var66))
                            var3 = i32_load(9140296)
                            var1 = (i32_load(9140296) + 1)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var3 << 2) + 8451904), var2)
                            break
                        if (1 if i32_load(39220) == var2 else 0):
                            var4 = i32_load(38756)
                            var2 = (var8 + (i32_load(38756) << 2))
                            var6 = i32_load(((var8 + (i32_load(38756) << 2)) + 281808))
                            var7 = i32_load((var2 + 282828))
                            var1 = (((var1 * 125) & 0xFFFFFFFF) // 100)
                            var2 = (((var1 * 35) & 0xFFFFFFFF) // 100)
                            var48 = ((((var1 * 125) & 0xFFFFFFFF) // 100) - (((var1 * 35) & 0xFFFFFFFF) // 100))
                            # Unknown: f64.convert_i32_u []
                            var106 = ((((var1 * 125) & 0xFFFFFFFF) // 100) - (((var1 * 35) & 0xFFFFFFFF) // 100))
                            var105 = (((((var1 * 125) & 0xFFFFFFFF) // 100) - (((var1 * 35) & 0xFFFFFFFF) // 100)) * 0.3)
                            if ((1 if (((((var1 * 125) & 0xFFFFFFFF) // 100) - (((var1 * 35) & 0xFFFFFFFF) // 100)) * 0.3) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                                break
                            var1 = 0
                            var3 = 0
                            var10 = ((var4 * 404) + 9568096)
                            if (1 if i32_load(((var4 * 404) + 9568096) + 264) <= 1 else 0):
                                var3 = (i32_load(var5) * var1)
                                var3 = (1 if (1 if var3 < 100 else 0) else (((i32_load(var5) * var1) & 0xFFFFFFFF) // 100))
                            var7 = (var6 + var7)
                            if (1 if (var6 + var7) >= var3 else 0):
                                break
                            if i32_load8_u(var10 + 354):
                                break
                            var6 = (var8 + (var4 * 1056))
                            i32_store8(((var8 + (var4 * 1056)) + 1150), 1)
                            var7 = (var3 - var7)
                            i32_store(var6 + 108, (var3 - var7))
                            var66 = float(var3)
                            f32_store(var6 + 100, (90.0 / float(var3)))
                            f32_store(var6 + 96, ((float(var7) * 90.0) / var66))
                            var3 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var3 << 2) + 8451904), var4)
                            var4 = i32_load(38740)
                            var3 = (var8 + (i32_load(38740) << 2))
                            var6 = i32_load(((var8 + (i32_load(38740) << 2)) + 281808))
                            var7 = i32_load((var3 + 282828))
                            var10 = ((var4 * 404) + 9568096)
                            var15 = (1 if i32_load(((var4 * 404) + 9568096) + 264) > 1 else 0)
                            var105 = (var106 * 0.1)
                            if ((1 if (var106 * 0.1) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                                break
                            var3 = 0
                            if (1 if var15 == 0 else 0):
                                var3 = (i32_load(var5) * var3)
                                var3 = (1 if (1 if var3 < 100 else 0) else (((i32_load(var5) * var3) & 0xFFFFFFFF) // 100))
                            var7 = (var6 + var7)
                            if (1 if (var6 + var7) >= var3 else 0):
                                break
                            if i32_load8_u(var10 + 354):
                                break
                            var6 = (var8 + (var4 * 1056))
                            i32_store8(((var8 + (var4 * 1056)) + 1150), 1)
                            var7 = (var3 - var7)
                            i32_store(var6 + 108, (var3 - var7))
                            var66 = float(var3)
                            f32_store(var6 + 100, (120.0 / float(var3)))
                            f32_store(var6 + 96, ((float(var7) * 120.0) / var66))
                            var3 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var3 << 2) + 8451904), var4)
                            var4 = i32_load(38736)
                            var3 = (var8 + (i32_load(38736) << 2))
                            var7 = (i32_load(((var8 + (i32_load(38736) << 2)) + 282828)) + i32_load((var3 + 281808)))
                            var3 = var1
                            var6 = ((var4 * 404) + 9568096)
                            if (1 if i32_load(((var4 * 404) + 9568096) + 264) <= 1 else 0):
                                var3 = (i32_load(var5) * var1)
                                var3 = (1 if (1 if var3 < 100 else 0) else (((i32_load(var5) * var1) & 0xFFFFFFFF) // 100))
                            if (1 if var3 <= var7 else 0):
                                break
                            if i32_load8_u(var6 + 354):
                                break
                            var6 = (var8 + (var4 * 1056))
                            i32_store8(((var8 + (var4 * 1056)) + 1150), 1)
                            var7 = (var3 - var7)
                            i32_store(var6 + 108, (var3 - var7))
                            var66 = float(var3)
                            f32_store(var6 + 100, (120.0 / float(var3)))
                            f32_store(var6 + 96, ((float(var7) * 120.0) / var66))
                            var3 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var3 << 2) + 8451904), var4)
                            var3 = i32_load(38776)
                            var4 = (var8 + (i32_load(38776) << 2))
                            var6 = (i32_load(((var8 + (i32_load(38776) << 2)) + 282828)) + i32_load((var4 + 281808)))
                            var4 = ((var3 * 404) + 9568096)
                            if (1 if i32_load(((var3 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = (i32_load(var5) * var1)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * var1) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var6 else 0):
                                break
                            if i32_load8_u(var4 + 354):
                                break
                            var4 = (var8 + (var3 * 1056))
                            i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                            var6 = (var1 - var6)
                            i32_store(var4 + 108, (var1 - var6))
                            var66 = float(var1)
                            f32_store(var4 + 100, (80.0 / float(var1)))
                            f32_store(var4 + 96, ((float(var6) * 80.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var3)
                            var3 = i32_load(38820)
                            var6 = ((i32_load(38820) * 404) + 9568096)
                            var7 = i32_load(((i32_load(38820) * 404) + 9568096) + 264)
                            var1 = (var8 + (var3 << 2))
                            var4 = (i32_load(((var8 + (var3 << 2)) + 282828)) + i32_load((var1 + 281808)))
                            if (1 if (i32_load(((var8 + (var3 << 2)) + 282828)) + i32_load((var1 + 281808))) <= 16 else 0):
                                var1 = 17
                                if (1 if var7 <= 1 else 0):
                                    var1 = (i32_load(var5) * 17)
                                    var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 17) & 0xFFFFFFFF) // 100))
                                if (1 if var1 <= var4 else 0):
                                    break
                                if i32_load8_u(var6 + 354):
                                    break
                                var67 = 130.0
                                break
                            var1 = 34
                            if (1 if var7 <= 1 else 0):
                                var1 = (i32_load(var5) * 34)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 34) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var6 + 354):
                                break
                            var67 = 20.0
                            var66 = float(var1)
                            var6 = (var8 + (var3 * 1056))
                            i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                            var1 = (var1 - var4)
                            i32_store(var6 + 108, (var1 - var4))
                            f32_store(var6 + 100, (var67 / var66))
                            f32_store(var6 + 96, ((var67 * float(var1)) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var3)
                            var3 = i32_load(38800)
                            var1 = (var8 + (i32_load(38800) << 2))
                            var6 = (i32_load(((var8 + (i32_load(38800) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var4 = ((var3 * 404) + 9568096)
                            if (1 if i32_load(((var3 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var6 else 0):
                                break
                            if i32_load8_u(var4 + 354):
                                break
                            var4 = (var8 + (var3 * 1056))
                            i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                            var6 = (var1 - var6)
                            i32_store(var4 + 108, (var1 - var6))
                            var66 = float(var1)
                            f32_store(var4 + 100, (181.0 / float(var1)))
                            f32_store(var4 + 96, ((float(var6) * 181.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var3)
                            var3 = i32_load(38824)
                            var1 = (var8 + (i32_load(38824) << 2))
                            var6 = (i32_load(((var8 + (i32_load(38824) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var4 = ((var3 * 404) + 9568096)
                            if (1 if i32_load(((var3 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var6 else 0):
                                break
                            if i32_load8_u(var4 + 354):
                                break
                            var4 = (var8 + (var3 * 1056))
                            i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                            var6 = (var1 - var6)
                            i32_store(var4 + 108, (var1 - var6))
                            var66 = float(var1)
                            f32_store(var4 + 100, (180.0 / float(var1)))
                            f32_store(var4 + 96, ((float(var6) * 180.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var3)
                            var3 = i32_load(38812)
                            var1 = (var8 + (i32_load(38812) << 2))
                            var6 = (i32_load(((var8 + (i32_load(38812) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var4 = ((var3 * 404) + 9568096)
                            if (1 if i32_load(((var3 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var6 else 0):
                                break
                            if i32_load8_u(var4 + 354):
                                break
                            var4 = (var8 + (var3 * 1056))
                            i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                            var6 = (var1 - var6)
                            i32_store(var4 + 108, (var1 - var6))
                            var66 = float(var1)
                            f32_store(var4 + 100, (180.0 / float(var1)))
                            f32_store(var4 + 96, ((float(var6) * 180.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var3)
                            var3 = i32_load(39192)
                            var1 = (var8 + (i32_load(39192) << 2))
                            var6 = (i32_load(((var8 + (i32_load(39192) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var4 = ((var3 * 404) + 9568096)
                            if (1 if i32_load(((var3 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var6 else 0):
                                break
                            if i32_load8_u(var4 + 354):
                                break
                            var4 = (var8 + (var3 * 1056))
                            i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                            var6 = (var1 - var6)
                            i32_store(var4 + 108, (var1 - var6))
                            var66 = float(var1)
                            f32_store(var4 + 100, (95.0 / float(var1)))
                            f32_store(var4 + 96, ((float(var6) * 95.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var3)
                            var3 = i32_load(38848)
                            var1 = (var8 + (i32_load(38848) << 2))
                            var6 = (i32_load(((var8 + (i32_load(38848) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var4 = ((var3 * 404) + 9568096)
                            if (1 if i32_load(((var3 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var6 else 0):
                                break
                            if i32_load8_u(var4 + 354):
                                break
                            var4 = (var8 + (var3 * 1056))
                            i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                            var6 = (var1 - var6)
                            i32_store(var4 + 108, (var1 - var6))
                            var66 = float(var1)
                            f32_store(var4 + 100, (131.0 / float(var1)))
                            f32_store(var4 + 96, ((float(var6) * 131.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var3)
                            var1 = (var8 + (var13 << 2))
                            var3 = (i32_load(((var8 + (var13 << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = ((var13 * 404) + 9568096)
                            if (1 if i32_load(((var13 * 404) + 9568096) + 264) <= 1 else 0):
                                var2 = (i32_load(var5) * var2)
                                var2 = (1 if (1 if var2 < 100 else 0) else (((i32_load(var5) * var2) & 0xFFFFFFFF) // 100))
                            if (1 if var2 <= var3 else 0):
                                break
                            if i32_load8_u(var1 + 354):
                                break
                            var1 = (var8 + (var13 * 1056))
                            i32_store8(((var8 + (var13 * 1056)) + 1150), 1)
                            var3 = (var2 - var3)
                            i32_store(var1 + 108, (var2 - var3))
                            var66 = float(var2)
                            f32_store(var1 + 100, (400.0 / float(var2)))
                            f32_store(var1 + 96, ((float(var3) * 400.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var13)
                            if (1 if i32_load((var8 + 283856)) > 1999 else 0):
                                break
                            var2 = i32_load(39212)
                            var1 = (var8 + (i32_load(39212) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39212) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (1001.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 1001.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            if (1 if var11 > 7999999 else 0):
                                break
                            if var16:
                                var2 = i32_load(38528)
                                var4 = ((i32_load(38528) * 404) + 9568096)
                                var6 = i32_load(((i32_load(38528) * 404) + 9568096) + 264)
                                var1 = (var8 + (var2 << 2))
                                var3 = (i32_load(((var8 + (var2 << 2)) + 282828)) + i32_load((var1 + 281808)))
                                if (1 if (i32_load(((var8 + (var2 << 2)) + 282828)) + i32_load((var1 + 281808))) <= 8 else 0):
                                    var1 = 60
                                    if (1 if var6 <= 1 else 0):
                                        var1 = (i32_load(var5) * 60)
                                        var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 60) & 0xFFFFFFFF) // 100))
                                    if (1 if var1 <= var3 else 0):
                                        break
                                    if i32_load8_u(var4 + 354):
                                        break
                                    var67 = 200.0
                                    break
                                var1 = 60
                                if (1 if var6 <= 1 else 0):
                                    var1 = (i32_load(var5) * 60)
                                    var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 60) & 0xFFFFFFFF) // 100))
                                if (1 if var1 <= var3 else 0):
                                    break
                                if i32_load8_u(var4 + 354):
                                    break
                                var67 = 80.0
                                var66 = float(var1)
                                var4 = (var8 + (var2 * 1056))
                                i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                                var1 = (var1 - var3)
                                i32_store(var4 + 108, (var1 - var3))
                                f32_store(var4 + 100, (var67 / var66))
                                f32_store(var4 + 96, ((var67 * float(var1)) / var66))
                                var1 = i32_load(9140296)
                                i32_store(9140296, (i32_load(9140296) + 1))
                                i32_store(((var1 << 2) + 8451904), var2)
                                var1 = i32_load(38792)
                                var2 = (var8 + (i32_load(38792) << 2))
                                var3 = (i32_load(((var8 + (i32_load(38792) << 2)) + 282828)) + i32_load((var2 + 281808)))
                                var2 = 14
                                var4 = ((var1 * 404) + 9568096)
                                if (1 if i32_load(((var1 * 404) + 9568096) + 264) <= 1 else 0):
                                    var2 = (i32_load(var5) * 14)
                                    var2 = (1 if (1 if var2 < 100 else 0) else (((i32_load(var5) * 14) & 0xFFFFFFFF) // 100))
                                if (1 if var2 <= var3 else 0):
                                    break
                                if i32_load8_u(var4 + 354):
                                    break
                                var66 = 275.0
                                var67 = float(var2)
                                f32_store((var8 + (var1 * 1056)) + 100, (275.0 / float(var2)))
                                break
                            var2 = i32_load(38500)
                            var1 = (var8 + (i32_load(38500) << 2))
                            var4 = (i32_load(((var8 + (i32_load(38500) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 15
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = (i32_load(var5) * 15)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 15) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (800.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 800.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var1 = i32_load(39084)
                            var2 = (var8 + (i32_load(39084) << 2))
                            var3 = (i32_load(((var8 + (i32_load(39084) << 2)) + 282828)) + i32_load((var2 + 281808)))
                            var2 = 1
                            var4 = ((var1 * 404) + 9568096)
                            if (1 if i32_load(((var1 * 404) + 9568096) + 264) <= 1 else 0):
                                var2 = i32_load(var5)
                                var2 = (1 if (1 if var2 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var2 <= var3 else 0):
                                break
                            if i32_load8_u(var4 + 354):
                                break
                            var66 = 200.0
                            var67 = float(var2)
                            f32_store((var8 + (var1 * 1056)) + 100, (200.0 / float(var2)))
                            var2 = (var2 - var3)
                            var3 = (var8 + (var1 * 1056))
                            i32_store8(((var8 + (var1 * 1056)) + 1150), 1)
                            i32_store(var3 + 108, var2)
                            f32_store(var3 + 96, ((var66 * float(var2)) / var67))
                            var2 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var2 << 2) + 8451904), var1)
                            if (1 if var14 > 79999 else 0):
                                break
                            var2 = i32_load(39076)
                            var1 = (var8 + (i32_load(39076) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39076) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (152.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 152.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            if (1 if var12 > 79999 else 0):
                                break
                            var2 = i32_load(39068)
                            var1 = (var8 + (i32_load(39068) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39068) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (150.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 150.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            if (1 if var17 > 39999 else 0):
                                break
                            var2 = i32_load(39072)
                            var1 = (var8 + (i32_load(39072) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39072) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (125.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 125.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(38788)
                            var1 = (var8 + (i32_load(38788) << 2))
                            var4 = (i32_load(((var8 + (i32_load(38788) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 4
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = (i32_load(var5) << 2)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) << 2) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (800.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 800.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39204)
                            var1 = (var8 + (i32_load(39204) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39204) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (125.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 125.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39112)
                            var1 = (var8 + (i32_load(39112) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39112) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (60.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 60.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39080)
                            var1 = (var8 + (i32_load(39080) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39080) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (95.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 95.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39088)
                            var1 = (var8 + (i32_load(39088) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39088) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (95.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 95.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39196)
                            var1 = (var8 + (i32_load(39196) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39196) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (95.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 95.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39092)
                            var1 = (var8 + (i32_load(39092) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39092) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (50.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 50.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39116)
                            var1 = (var8 + (i32_load(39116) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39116) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (44.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 44.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39120)
                            var1 = (var8 + (i32_load(39120) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39120) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (44.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 44.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39180)
                            var1 = (var8 + (i32_load(39180) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39180) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (40.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 40.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39140)
                            var1 = (var8 + (i32_load(39140) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39140) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (42.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 42.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39208)
                            var1 = (var8 + (i32_load(39208) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39208) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (75.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 75.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(39200)
                            var1 = (var8 + (i32_load(39200) << 2))
                            var4 = (i32_load(((var8 + (i32_load(39200) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (31.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 31.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(38772)
                            var1 = (var8 + (i32_load(38772) << 2))
                            var4 = (i32_load(((var8 + (i32_load(38772) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 3
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = (i32_load(var5) * 3)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 3) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (30.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 30.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(38836)
                            var1 = (var8 + (i32_load(38836) << 2))
                            var4 = (i32_load(((var8 + (i32_load(38836) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 1
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = i32_load(var5)
                                var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (37.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 37.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var1 = 2
                            var2 = i32_load(38808)
                            var3 = (var8 + (i32_load(38808) << 2))
                            var4 = (i32_load(((var8 + (i32_load(38808) << 2)) + 282828)) + i32_load((var3 + 281808)))
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = (i32_load(var5) << 1)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) << 1) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (36.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 36.0) / var66))
                            var1 = i32_load(9140296)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var1 << 2) + 8451904), var2)
                            var2 = i32_load(38764)
                            var1 = (var8 + (i32_load(38764) << 2))
                            var4 = (i32_load(((var8 + (i32_load(38764) << 2)) + 282828)) + i32_load((var1 + 281808)))
                            var1 = 5
                            var3 = ((var2 * 404) + 9568096)
                            if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                                var1 = (i32_load(var5) * 5)
                                var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 5) & 0xFFFFFFFF) // 100))
                            if (1 if var1 <= var4 else 0):
                                break
                            if i32_load8_u(var3 + 354):
                                break
                            var3 = (var8 + (var2 * 1056))
                            i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                            var4 = (var1 - var4)
                            i32_store(var3 + 108, (var1 - var4))
                            var66 = float(var1)
                            f32_store(var3 + 100, (35.0 / float(var1)))
                            f32_store(var3 + 96, ((float(var4) * 35.0) / var66))
                            var3 = i32_load(9140296)
                            var1 = (i32_load(9140296) + 1)
                            i32_store(9140296, (i32_load(9140296) + 1))
                            i32_store(((var3 << 2) + 8451904), var2)
                            break
                        var3 = i32_load(38692)
                        var2 = (var8 + (i32_load(38692) << 2))
                        var4 = i32_load(((var8 + (i32_load(38692) << 2)) + 281808))
                        var6 = i32_load((var2 + 282828))
                        var1 = (((var1 * 150) & 0xFFFFFFFF) // 100)
                        var2 = (((var1 * 35) & 0xFFFFFFFF) // 100)
                        var48 = ((((var1 * 150) & 0xFFFFFFFF) // 100) - (((var1 * 35) & 0xFFFFFFFF) // 100))
                        # Unknown: f64.convert_i32_u []
                        var106 = ((((var1 * 150) & 0xFFFFFFFF) // 100) - (((var1 * 35) & 0xFFFFFFFF) // 100))
                        var105 = (((((var1 * 150) & 0xFFFFFFFF) // 100) - (((var1 * 35) & 0xFFFFFFFF) // 100)) * 0.4)
                        if ((1 if (((((var1 * 150) & 0xFFFFFFFF) // 100) - (((var1 * 35) & 0xFFFFFFFF) // 100)) * 0.4) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                            break
                        var1 = 0
                        var7 = ((var3 * 404) + 9568096)
                        if (1 if i32_load(((var3 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = (i32_load(var5) * var1)
                            var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * var1) & 0xFFFFFFFF) // 100))
                        var6 = (var4 + var6)
                        if (1 if (var4 + var6) >= var1 else 0):
                            break
                        if i32_load8_u(var7 + 354):
                            break
                        var4 = (var8 + (var3 * 1056))
                        i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                        var6 = (var1 - var6)
                        i32_store(var4 + 108, (var1 - var6))
                        var66 = float(var1)
                        f32_store(var4 + 100, (90.0 / float(var1)))
                        f32_store(var4 + 96, ((float(var6) * 90.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var3)
                        var4 = i32_load(38684)
                        var1 = (var8 + (i32_load(38684) << 2))
                        var6 = i32_load(((var8 + (i32_load(38684) << 2)) + 281808))
                        var7 = i32_load((var1 + 282828))
                        var10 = ((var4 * 404) + 9568096)
                        var15 = (1 if i32_load(((var4 * 404) + 9568096) + 264) > 1 else 0)
                        var105 = (var106 * 0.3)
                        if ((1 if (var106 * 0.3) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                            break
                        var1 = 0
                        var3 = 0
                        if (1 if var15 == 0 else 0):
                            var3 = (i32_load(var5) * var1)
                            var3 = (1 if (1 if var3 < 100 else 0) else (((i32_load(var5) * var1) & 0xFFFFFFFF) // 100))
                        var7 = (var6 + var7)
                        if (1 if (var6 + var7) >= var3 else 0):
                            break
                        if i32_load8_u(var10 + 354):
                            break
                        var6 = (var8 + (var4 * 1056))
                        i32_store8(((var8 + (var4 * 1056)) + 1150), 1)
                        var7 = (var3 - var7)
                        i32_store(var6 + 108, (var3 - var7))
                        var66 = float(var3)
                        f32_store(var6 + 100, (120.0 / float(var3)))
                        f32_store(var6 + 96, ((float(var7) * 120.0) / var66))
                        var3 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var3 << 2) + 8451904), var4)
                        var3 = i32_load(38680)
                        var4 = (var8 + (i32_load(38680) << 2))
                        var6 = (i32_load(((var8 + (i32_load(38680) << 2)) + 282828)) + i32_load((var4 + 281808)))
                        var4 = ((var3 * 404) + 9568096)
                        if (1 if i32_load(((var3 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = (i32_load(var5) * var1)
                            var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * var1) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var6 else 0):
                            break
                        if i32_load8_u(var4 + 354):
                            break
                        var4 = (var8 + (var3 * 1056))
                        i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                        var6 = (var1 - var6)
                        i32_store(var4 + 108, (var1 - var6))
                        var66 = float(var1)
                        f32_store(var4 + 100, (120.0 / float(var1)))
                        f32_store(var4 + 96, ((float(var6) * 120.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var3)
                        var3 = i32_load(38700)
                        var1 = (var8 + (i32_load(38700) << 2))
                        var6 = (i32_load(((var8 + (i32_load(38700) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 17
                        var4 = ((var3 * 404) + 9568096)
                        if (1 if i32_load(((var3 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = (i32_load(var5) * 17)
                            var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 17) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var6 else 0):
                            break
                        if i32_load8_u(var4 + 354):
                            break
                        var4 = (var8 + (var3 * 1056))
                        i32_store8(((var8 + (var3 * 1056)) + 1150), 1)
                        var6 = (var1 - var6)
                        i32_store(var4 + 108, (var1 - var6))
                        var66 = float(var1)
                        f32_store(var4 + 100, (130.0 / float(var1)))
                        f32_store(var4 + 96, ((float(var6) * 130.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var3)
                        var1 = (var8 + (var13 << 2))
                        var3 = (i32_load(((var8 + (var13 << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = ((var13 * 404) + 9568096)
                        if (1 if i32_load(((var13 * 404) + 9568096) + 264) <= 1 else 0):
                            var2 = (i32_load(var5) * var2)
                            var2 = (1 if (1 if var2 < 100 else 0) else (((i32_load(var5) * var2) & 0xFFFFFFFF) // 100))
                        if (1 if var2 <= var3 else 0):
                            break
                        if i32_load8_u(var1 + 354):
                            break
                        var1 = (var8 + (var13 * 1056))
                        i32_store8(((var8 + (var13 * 1056)) + 1150), 1)
                        var3 = (var2 - var3)
                        i32_store(var1 + 108, (var2 - var3))
                        var66 = float(var2)
                        f32_store(var1 + 100, (1000.0 / float(var2)))
                        f32_store(var1 + 96, ((float(var3) * 1000.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var13)
                        var2 = i32_load(39096)
                        var1 = (var8 + (i32_load(39096) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39096) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (1001.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 1001.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(38500)
                        var1 = (var8 + (i32_load(38500) << 2))
                        var4 = (i32_load(((var8 + (i32_load(38500) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 24
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = (i32_load(var5) * 24)
                            var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 24) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (800.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 800.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39172)
                        var1 = (var8 + (i32_load(39172) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39172) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (50.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 50.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39176)
                        var1 = (var8 + (i32_load(39176) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39176) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (40.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 40.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39076)
                        var1 = (var8 + (i32_load(39076) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39076) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (50.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 50.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39068)
                        var1 = (var8 + (i32_load(39068) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39068) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (50.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 50.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39072)
                        var1 = (var8 + (i32_load(39072) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39072) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (50.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 50.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39084)
                        var1 = (var8 + (i32_load(39084) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39084) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (60.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 60.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39152)
                        var1 = (var8 + (i32_load(39152) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39152) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (59.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 59.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var1 = i32_load(38864)
                        var2 = ((i32_load(38864) * 404) + 9568096)
                        if (1 if i32_load(((i32_load(38864) * 404) + 9568096) + 264) > 1 else 0):
                            break
                        var3 = (var8 + (var1 << 2))
                        if (1 if i32_load(((var8 + (var1 << 2)) + 282828)) != (0 - i32_load((var3 + 281808))) else 0):
                            break
                        if i32_load8_u(var2 + 354):
                            break
                        var2 = (var8 + (var1 * 1056))
                        i32_store8(((var8 + (var1 * 1056)) + 1150), 1)
                        i32_store(var2 + 108, 1)
                        i64_store(var2 + 96, 4692750812812673024)
                        var2 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var2 << 2) + 8451904), var1)
                        var2 = i32_load(39080)
                        var1 = (var8 + (i32_load(39080) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39080) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (50.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 50.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39088)
                        var1 = (var8 + (i32_load(39088) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39088) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (50.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 50.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39092)
                        var1 = (var8 + (i32_load(39092) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39092) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (50.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 50.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39116)
                        var1 = (var8 + (i32_load(39116) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39116) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (46.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 46.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39184)
                        var1 = (var8 + (i32_load(39184) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39184) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (46.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 46.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39180)
                        var1 = (var8 + (i32_load(39180) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39180) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (42.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 42.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39160)
                        var1 = (var8 + (i32_load(39160) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39160) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (31.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 31.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(39156)
                        var1 = (var8 + (i32_load(39156) << 2))
                        var4 = (i32_load(((var8 + (i32_load(39156) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 1
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = i32_load(var5)
                            var1 = (1 if (1 if var1 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (25.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 25.0) / var66))
                        var1 = i32_load(9140296)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var1 << 2) + 8451904), var2)
                        var2 = i32_load(38928)
                        var1 = (var8 + (i32_load(38928) << 2))
                        var4 = (i32_load(((var8 + (i32_load(38928) << 2)) + 282828)) + i32_load((var1 + 281808)))
                        var1 = 3
                        var3 = ((var2 * 404) + 9568096)
                        if (1 if i32_load(((var2 * 404) + 9568096) + 264) <= 1 else 0):
                            var1 = (i32_load(var5) * 3)
                            var1 = (1 if (1 if var1 < 100 else 0) else (((i32_load(var5) * 3) & 0xFFFFFFFF) // 100))
                        if (1 if var1 <= var4 else 0):
                            break
                        if i32_load8_u(var3 + 354):
                            break
                        var3 = (var8 + (var2 * 1056))
                        i32_store8(((var8 + (var2 * 1056)) + 1150), 1)
                        var4 = (var1 - var4)
                        i32_store(var3 + 108, (var1 - var4))
                        var66 = float(var1)
                        f32_store(var3 + 100, (30.0 / float(var1)))
                        f32_store(var3 + 96, ((float(var4) * 30.0) / var66))
                        var3 = i32_load(9140296)
                        var1 = (i32_load(9140296) + 1)
                        i32_store(9140296, (i32_load(9140296) + 1))
                        i32_store(((var3 << 2) + 8451904), var2)
                        break
                        var1 = i32_load(9140296)
                        var15 = 0
                        var73 = 0.0
                        var75 = 0.0
                        var76 = 0.0
                        var80 = 0.0
                        var68 = 0.0
                        var66 = 0.0
                        var67 = 0.0
                        var70 = 0.0
                        if var1:
                            while True:  # loop $label328
                                var1 = i32_load(((var15 << 2) + 8451904))
                                var20 = (var8 + (i32_load(((var15 << 2) + 8451904)) * 1056))
                                var71 = f32_load((var8 + (i32_load(((var15 << 2) + 8451904)) * 1056)) + 96)
                                var2 = ((var1 * 404) + 9568096)
                                var3 = i32_load(((var1 * 404) + 9568096) + 180)
                                var10 = i32_load(i32_load(((var1 * 404) + 9568096) + 180) + 112)
                                if i32_load(i32_load(((var1 * 404) + 9568096) + 180) + 112):
                                    var69 = (var71 + 1.0)
                                    var1 = 0
                                    while True:  # loop $label324
                                        var6 = i32_load((var3 + (var1 << 2)) + 72)
                                        var21 = ((i32_load((var3 + (var1 << 2)) + 72) * 404) + 9568096)
                                        if (1 if i32_load(((i32_load((var3 + (var1 << 2)) + 72) * 404) + 9568096) + 196) == i32_load(var9) else 0):
                                            var4 = (var8 + (var6 * 1056))
                                            var26 = ((var8 + (var6 * 1056)) + 1150)
                                            if i32_load8_u(((var8 + (var6 * 1056)) + 1150)):
                                                break
                                            var7 = (var8 + (var6 << 2))
                                            var18 = (i32_load(((var8 + (var6 << 2)) + 282828)) + i32_load((var7 + 281808)))
                                            var7 = 1
                                            if (1 if i32_load(var21 + 264) <= 1 else 0):
                                                var7 = i32_load(var5)
                                                var7 = (1 if (1 if var7 < 100 else 0) else ((i32_load(var5) & 0xFFFFFFFF) // 100))
                                            if (1 if var7 <= var18 else 0):
                                                break
                                            if i32_load8_u(var21 + 354):
                                                break
                                            var10 = (var7 - var18)
                                            i32_store(var4 + 108, (var7 - var18))
                                            var74 = float(var7)
                                            f32_store(var4 + 100, (var69 / float(var7)))
                                            i32_store8(var26, 1)
                                            f32_store(var4 + 96, ((var69 * float(var10)) / var74))
                                            var7 = i32_load(9140296)
                                            i32_store(9140296, (i32_load(9140296) + 1))
                                            i32_store(((var7 << 2) + 8451904), var6)
                                            var10 = i32_load(var3 + 112)
                                            i32_store(var4 + 104, (i32_load(var4 + 104) + (i32_load(var20 + 108) * i32_load(var2 + 116))))
                                        var1 = (var1 + 1)
                                        if (1 if (var1 + 1) < var10 else 0):
                                            continue
                                        break  # end loop
                                var6 = i32_load(var3 + 68)
                                if i32_load(var3 + 68):
                                    var71 = (var71 + 1.0)
                                    var1 = 0
                                    while True:  # loop $label327
                                        var7 = i32_load((var3 + (var1 << 2)) + 28)
                                        var10 = (var8 + (i32_load((var3 + (var1 << 2)) + 28) * 1056))
                                        var18 = ((var8 + (i32_load((var3 + (var1 << 2)) + 28) * 1056)) + 1150)
                                        if i32_load8_u(((var8 + (i32_load((var3 + (var1 << 2)) + 28) * 1056)) + 1150)):
                                            break
                                        var4 = (var8 + (var7 << 2))
                                        if (1 if i32_load(((var8 + (var7 << 2)) + 282828)) != (0 - i32_load((var4 + 281808))) else 0):
                                            break
                                        var4 = 1
                                        var21 = ((var7 * 404) + 9568096)
                                        var26 = i32_load(((var7 * 404) + 9568096) + 264)
                                        if (1 if i32_load(((var7 * 404) + 9568096) + 264) == 3 else 0):
                                            break
                                        if (1 if i32_load(var21 + 196) != i32_load(var9) else 0):
                                            break
                                        if (1 if var26 > 1 else 0):
                                            break
                                        var26 = i32_load(var5)
                                        if (1 if i32_load(var5) < 100 else 0):
                                            break
                                        var4 = ((var26 & 0xFFFFFFFF) // 100)
                                        if i32_load8_u(var21 + 354):
                                            break
                                        i32_store(var10 + 108, var4)
                                        var69 = float(var4)
                                        f32_store(var10 + 100, (var71 / float(var4)))
                                        i32_store8(var18, 1)
                                        f32_store(var10 + 96, ((var71 * var69) / var69))
                                        var4 = i32_load(9140296)
                                        i32_store(9140296, (i32_load(9140296) + 1))
                                        i32_store(((var4 << 2) + 8451904), var7)
                                        var6 = i32_load(var3 + 68)
                                        var1 = (var1 + 1)
                                        if (1 if (var1 + 1) < var6 else 0):
                                            continue
                                        break  # end loop
                                var1 = i32_load(var20 + 108)
                                var71 = float((i32_load(var20 + 108) * i32_load(var2 + 80)))
                                var68 = (var68 + float((i32_load(var20 + 108) * i32_load(var2 + 80))))
                                var69 = float((var1 * i32_load(var2 + 76)))
                                var66 = (var66 + float((var1 * i32_load(var2 + 76))))
                                var74 = float((var1 * i32_load(var2 + 72)))
                                var67 = (var67 + float((var1 * i32_load(var2 + 72))))
                                var79 = float((var1 * i32_load(var2 + 68)))
                                var70 = (var70 + float((var1 * i32_load(var2 + 68))))
                                var71 = f32_load(var20 + 96)
                                var73 = ((var71 * f32_load(var20 + 96)) + var73)
                                var75 = ((var69 * var71) + var75)
                                var76 = ((var74 * var71) + var76)
                                var80 = ((var79 * var71) + var80)
                                var15 = (var15 + 1)
                                if (1 if (var15 + 1) < i32_load(9140296) else 0):
                                    continue
                                break  # end loop
                        var43 = (var8 + 283872)
                        var3 = 0
                        var74 = float(var17)
                        var68 = (var68 - float(var17))
                        var79 = (0.0 if (1 if var68 < 0.0 else 0) else (var68 - float(var17)))
                        var90 = f32_load(var19 + 60)
                        var81 = float(var11)
                        var66 = (var66 - float(var11))
                        var82 = (0.0 if (1 if var66 < 0.0 else 0) else (var66 - float(var11)))
                        var91 = f32_load(var19 + 56)
                        var71 = float(var14)
                        var66 = (var67 - float(var14))
                        var83 = (0.0 if (1 if var66 < 0.0 else 0) else (var67 - float(var14)))
                        var92 = f32_load(var19 + 52)
                        var84 = float(var12)
                        var66 = (var70 - float(var12))
                        var85 = (0.0 if (1 if var66 < 0.0 else 0) else (var70 - float(var12)))
                        var93 = f32_load(var19 + 48)
                        var1 = (var8 + (var13 * 1056))
                        var66 = (((0.0 if (1 if var66 < 0.0 else 0) else (var70 - float(var12))) / (f32_load(var19 + 48) / f32_load(9682176))) + float(i32_load((var8 + (var13 * 1056)) + 104)))
                        if ((1 if (((0.0 if (1 if var66 < 0.0 else 0) else (var70 - float(var12))) / (f32_load(var19 + 48) / f32_load(9682176))) + float(i32_load((var8 + (var13 * 1056)) + 104))) < 4294967300.0 else 0) & (1 if var66 >= 0.0 else 0)):
                            break
                        var66 = (int(var66) + float(0))
                        if ((1 if (int(var66) + float(0)) < 4294967300.0 else 0) & (1 if var66 >= 0.0 else 0)):
                            break
                        var66 = (int(var66) + float(0))
                        if ((1 if (int(var66) + float(0)) < 4294967300.0 else 0) & (1 if var66 >= 0.0 else 0)):
                            break
                        var66 = (int(var66) + float(0))
                        if ((1 if (int(var66) + float(0)) < 4294967300.0 else 0) & (1 if var66 >= 0.0 else 0)):
                            i32_store(var1 + 104, int(var66))
                            break
                        i32_store(var1 + 104, 0)
                        var1 = 0
                        while True:  # loop $label333
                            var2 = (var8 + (var1 << 2))
                            var2 = ((i32_load(((var1 * 404) + 9568096) + 280) * (i32_load(((var8 + (var1 << 2)) + 281808)) + i32_load((var2 + 282828)))) + var3)
                            var5 = (var1 | 1)
                            if (1 if (var1 | 1) != 255 else 0):
                                var5 = (var8 + (var5 << 2))
                                var3 = (var2 + (i32_load(((var5 * 404) + 9568096) + 280) * (i32_load(((var8 + (var5 << 2)) + 281808)) + i32_load((var5 + 282828)))))
                                var1 = (var1 + 2)
                                continue
                            break  # end loop
                        var1 = 0
                        var3 = i32_load(i32_load(9142424) + 36)
                        while True:  # loop $label334
                            var5 = i32_load(((var1 * 404) + 9568096) + 176)
                            if i32_load(((var1 * 404) + 9568096) + 176):
                                var4 = (var8 + (var1 << 2))
                                var3 = (var3 + (var5 * (i32_load(((var8 + (var1 << 2)) + 281808)) + i32_load((var4 + 282828)))))
                            var5 = (var1 | 1)
                            if (1 if (var1 | 1) != 255 else 0):
                                var4 = i32_load(((var5 * 404) + 9568096) + 176)
                                if i32_load(((var5 * 404) + 9568096) + 176):
                                    var5 = (var8 + (var5 << 2))
                                    var3 = ((var4 * (i32_load(((var8 + (var5 << 2)) + 281808)) + i32_load((var5 + 282828)))) + var3)
                                var1 = (var1 + 2)
                                continue
                            break  # end loop
                        if (1 if (var2 + 10) <= var3 else 0):
                            break
                        var2 = i32_load(((var8 + (var13 << 2)) + 284636))
                        if (1 if i32_load(((var8 + (var13 << 2)) + 284636)) == 0 else 0):
                            break
                        var4 = i32_load(var2 + 8)
                        if i32_load(var2 + 8):
                            var3 = 0
                            var6 = i32_load(9215884)
                            var7 = i32_load(9671128)
                            var10 = i32_load(var2)
                            var1 = 0
                            while True:  # loop $label337
                                var5 = i32_load((var10 + (var1 << 2)))
                                if (1 if i32_load((var10 + (var1 << 2))) == 0 else 0):
                                    break
                                var5 = (var7 + (var5 * 132))
                                var15 = i32_load((var7 + (var5 * 132)) + 44)
                                if (1 if ((1 if i32_load((var6 + (i32_load((var7 + (var5 * 132)) + 44) << 4)) + 4) == 22 else 0) | (1 if var15 == 0 else 0)) == 0 else 0):
                                    break
                                if i32_load8_u(var5 + 125):
                                    break
                                if i32_load(var5 + 36):
                                    break
                                var3 = (var3 if (1 if i32_load8_u(var5 + 129) == 10 else 0) else i32_load(var5 + 28))
                                var1 = (var1 + 1)
                                if (1 if (var1 + 1) != var4 else 0):
                                    continue
                                break  # end loop
                            if var3:
                                break
                            if (1 if var2 == 0 else 0):
                                break
                        var4 = i32_load(var2 + 8)
                        if (1 if i32_load(var2 + 8) == 0 else 0):
                            break
                        var6 = i32_load(var8 + 283876)
                        var7 = i32_load(var43)
                        var3 = 0
                        var10 = i32_load(9671128)
                        var15 = i32_load(var2)
                        var2 = 2147483647
                        var1 = 0
                        while True:  # loop $label339
                            var5 = i32_load((var15 + (var1 << 2)))
                            if i32_load((var15 + (var1 << 2))):
                                var5 = (var10 + (var5 * 132))
                                var11 = (var6 - i32_load16_u((var10 + (var5 * 132)) + 114))
                                var11 = (var7 - i32_load16_u(var5 + 112))
                                var11 = (((var6 - i32_load16_u((var10 + (var5 * 132)) + 114)) * var11) + ((var7 - i32_load16_u(var5 + 112)) * var11))
                                var11 = (1 if var2 > var11 else 0)
                                var2 = ((((var6 - i32_load16_u((var10 + (var5 * 132)) + 114)) * var11) + ((var7 - i32_load16_u(var5 + 112)) * var11)) if (1 if var2 > var11 else 0) else var2)
                                var3 = (i32_load(var5 + 28) if var11 else var3)
                            var1 = (var1 + 1)
                            if (1 if (var1 + 1) != var4 else 0):
                                continue
                            break  # end loop
                        if (1 if var3 == 0 else 0):
                            break
                        var52 = (var8 + 283876)
                        var7 = i32_load(var8 + 283876)
                        var2 = 0
                        var10 = i32_load(9142848)
                        var6 = i32_load(9671128)
                        var9 = i32_load(var43)
                        var5 = 2147483647
                        var12 = 0
                        while True:  # loop $label343
                            var1 = i32_load(((var8 + (var12 << 2)) + 284636))
                            if (1 if i32_load(((var8 + (var12 << 2)) + 284636)) == 0 else 0):
                                break
                            var15 = i32_load(var1 + 8)
                            if (1 if i32_load(var1 + 8) == 0 else 0):
                                break
                            var11 = i32_load(var1)
                            var1 = 0
                            while True:  # loop $label342
                                var3 = i32_load((var11 + (var1 << 2)))
                                if (1 if i32_load((var11 + (var1 << 2))) == 0 else 0):
                                    break
                                var4 = (var6 + (var3 * 132))
                                var3 = (var7 - i32_load16_u((var6 + (var3 * 132)) + 114))
                                var3 = (var9 - i32_load16_u(var4 + 112))
                                var3 = (((var7 - i32_load16_u((var6 + (var3 * 132)) + 114)) * var3) + ((var9 - i32_load16_u(var4 + 112)) * var3))
                                if (1 if (((var7 - i32_load16_u((var6 + (var3 * 132)) + 114)) * var3) + ((var9 - i32_load16_u(var4 + 112)) * var3)) >= var5 else 0):
                                    break
                                if (1 if i32_load8_u(var4 + 125) != 4 else 0):
                                    break
                                if (1 if ((var10 - i32_load(var4 + 88)) * 25) < 30001 else 0):
                                    break
                                var2 = i32_load(var4 + 28)
                                var5 = var3
                                var1 = (var1 + 1)
                                if (1 if (var1 + 1) != var15 else 0):
                                    continue
                                break  # end loop
                            var12 = (var12 + 1)
                            if (1 if (var12 + 1) != 132 else 0):
                                continue
                            break  # end loop
                        if (1 if var2 == 0 else 0):
                            break
                        var5 = i32_load(((var8 + (var13 << 2)) + 284636))
                        if (1 if i32_load(((var8 + (var13 << 2)) + 284636)) == 0 else 0):
                            break
                        var3 = i32_load(var5 + 8)
                        if (1 if i32_load(var5 + 8) == 0 else 0):
                            break
                        var10 = (var6 + (var2 * 132))
                        var9 = i32_load16_u((var6 + (var2 * 132)) + 114)
                        var15 = i32_load16_u(var10 + 112)
                        var7 = 0
                        var11 = i32_load(9215884)
                        var12 = i32_load(var5)
                        var4 = 2147483647
                        var1 = 0
                        while True:  # loop $label346
                            var2 = i32_load((var12 + (var1 << 2)))
                            if (1 if i32_load((var12 + (var1 << 2))) == 0 else 0):
                                break
                            var2 = (var6 + (var2 * 132))
                            var14 = i32_load((var6 + (var2 * 132)) + 44)
                            if (1 if ((1 if i32_load((var11 + (i32_load((var6 + (var2 * 132)) + 44) << 4)) + 4) == 22 else 0) | (1 if var14 == 0 else 0)) == 0 else 0):
                                break
                            if i32_load8_u(var2 + 125):
                                break
                            if i32_load(var2 + 36):
                                break
                            var14 = (var9 - i32_load16_u(var2 + 114))
                            var14 = (var15 - i32_load16_u(var2 + 112))
                            var14 = (((var9 - i32_load16_u(var2 + 114)) * var14) + ((var15 - i32_load16_u(var2 + 112)) * var14))
                            var14 = (1 if var4 > var14 else 0)
                            var4 = ((((var9 - i32_load16_u(var2 + 114)) * var14) + ((var15 - i32_load16_u(var2 + 112)) * var14)) if (1 if var4 > var14 else 0) else var4)
                            var7 = (i32_load(var2 + 28) if var14 else var7)
                            var1 = (var1 + 1)
                            if (1 if (var1 + 1) != var3 else 0):
                                continue
                            break  # end loop
                        if (1 if var7 == 0 else 0):
                            if (1 if var3 == 0 else 0):
                                break
                            var4 = i32_load(var5)
                            var7 = 0
                            var2 = 2147483647
                            var1 = 0
                            while True:  # loop $label347
                                var5 = i32_load((var4 + (var1 << 2)))
                                if i32_load((var4 + (var1 << 2))):
                                    var5 = (var6 + (var5 * 132))
                                    var11 = (var9 - i32_load16_u((var6 + (var5 * 132)) + 114))
                                    var11 = (var15 - i32_load16_u(var5 + 112))
                                    var11 = (((var9 - i32_load16_u((var6 + (var5 * 132)) + 114)) * var11) + ((var15 - i32_load16_u(var5 + 112)) * var11))
                                    var11 = (1 if var2 > var11 else 0)
                                    var2 = ((((var9 - i32_load16_u((var6 + (var5 * 132)) + 114)) * var11) + ((var15 - i32_load16_u(var5 + 112)) * var11)) if (1 if var2 > var11 else 0) else var2)
                                    var7 = (i32_load(var5 + 28) if var11 else var7)
                                var1 = (var1 + 1)
                                if (1 if (var1 + 1) != var3 else 0):
                                    continue
                                break  # end loop
                            if (1 if var7 == 0 else 0):
                                break
                        var1 = (var6 + (var7 * 132))
                        i32_store8((var6 + (var7 * 132)) + 129, 0)
                        i64_store(var19 + 40, 0)
                        i64_store(var19 + 32, 0)
                        var12 = 0
                        var30 = (var8 + (var13 << 2))
                        var49 = ((var8 + (var13 << 2)) + 284636)
                        var1 = i32_load(((var8 + (var13 << 2)) + 284636))
                        if (1 if i32_load(((var8 + (var13 << 2)) + 284636)) == 0 else 0):
                            break
                        var5 = i32_load(var1 + 8)
                        if (1 if i32_load(var1 + 8) == 0 else 0):
                            break
                        var3 = i32_load(9671128)
                        var4 = i32_load(var1)
                        var1 = 0
                        while True:  # loop $label350
                            var2 = i32_load((var4 + (var1 << 2)))
                            if (1 if i32_load((var4 + (var1 << 2))) == 0 else 0):
                                break
                            var2 = i32_load8_u((var3 + (var2 * 132)) + 129)
                            if (1 if ((i32_load8_u((var3 + (var2 * 132)) + 129) - 1) & 255) <= 3 else 0):
                                var2 = ((var2 << 2) - 4)
                                var6 = (((var2 << 2) - 4) + (var19 + 32))
                                f32_store((((var2 << 2) - 4) + (var19 + 32)), (f32_load(var6) + 1.0))
                                var6 = ((var19 - -64) + var2)
                                f32_store(((var19 - -64) + var2), (f32_load(var6) + (f32_load(((var19 + 48) + var2)) / (f32_load((var2 + 9682176)) + 3.0))))
                                break
                            if (1 if var2 != 10 else 0):
                                break
                            f32_store(var19 + 40, (f32_load(var19 + 40) + 1.0))
                            f32_store(var19 + 72, f32((float(f32_load(var19 + 72)) + 1.1904761904761905)))
                            var12 = (var12 + 1)
                            var1 = (var1 + 1)
                            if (1 if (var1 + 1) != var5 else 0):
                                continue
                            break  # end loop
                        var86 = (f32_load(var19 + 76) + 9.99999975e-06)
                        var87 = (f32_load(var19 + 72) + 9.99999975e-06)
                        var88 = (f32_load(var19 + 68) + 9.99999975e-06)
                        var89 = (f32_load(var19 + 64) + 9.99999975e-06)
                        var63 = (var8 + 283908)
                        var44 = (var8 + 283860)
                        var31 = (var8 + 283856)
                        var32 = (var8 + 283852)
                        var33 = (var8 + 283848)
                        var26 = i32_load(9140296)
                        var94 = (-var74)
                        var95 = (-var81)
                        var96 = (-var71)
                        var97 = (-var84)
                        while True:  # loop $label378
                            if (1 if var26 >= 2 else 0):
                                var13 = (var26 - 2)
                                var1 = 0
                                while True:  # loop $label355
                                    var2 = var1
                                    if (1 if (var26 - var1) < 2 else 0):
                                        break
                                    var4 = 1
                                    var5 = (var26 + (var2 ^ -1))
                                    var10 = ((var26 + (var2 ^ -1)) & 1)
                                    var1 = i32_load(8451904)
                                    if (1 if var2 != var13 else 0):
                                        var9 = (var5 & -2)
                                        var6 = 0
                                        while True:  # loop $label354
                                            var7 = (var8 + 96)
                                            var3 = ((var4 << 2) + 8451904)
                                            var5 = i32_load(((var4 << 2) + 8451904))
                                            if (1 if (1 if f32_load(((var8 + 96) + (var1 * 1056))) < f32_load((var7 + (i32_load(((var4 << 2) + 8451904)) * 1056))) else 0) == 0 else 0):
                                                var1 = var5
                                                break
                                            i32_store((var3 - 4), var5)
                                            i32_store(var3, var1)
                                            var5 = i32_load(var3 + 4)
                                            if (1 if (1 if f32_load((var7 + (var1 * 1056))) < f32_load((var7 + (i32_load(var3 + 4) * 1056))) else 0) == 0 else 0):
                                                var1 = var5
                                                break
                                            i32_store(var3, var5)
                                            i32_store(var3 + 4, var1)
                                            var4 = (var4 + 2)
                                            var6 = (var6 + 2)
                                            if (1 if (var6 + 2) != var9 else 0):
                                                continue
                                            break  # end loop
                                    if (1 if var10 == 0 else 0):
                                        break
                                    var3 = (var8 + 96)
                                    var5 = ((var4 << 2) + 8451904)
                                    var4 = i32_load(((var4 << 2) + 8451904))
                                    if (1 if (1 if f32_load(((var8 + 96) + (var1 * 1056))) < f32_load((var3 + (i32_load(((var4 << 2) + 8451904)) * 1056))) else 0) == 0 else 0):
                                        break
                                    i32_store((var5 - 4), var4)
                                    i32_store(var5, var1)
                                    var1 = (var2 + 1)
                                    if (1 if var2 != var13 else 0):
                                        continue
                                    break  # end loop
                            if var26:
                                var15 = 0
                                var21 = i32_load(9561692)
                                var27 = i32_load(9143016)
                                var18 = i32_load(9142892)
                                var34 = i32_load(9142848)
                                var25 = i32_load(9215884)
                                var22 = i32_load(9671128)
                                var45 = i32_load(38788)
                                var46 = i32_load(38864)
                                var36 = i32_load(38492)
                                var39 = i32_load(38500)
                                while True:  # loop $label383
                                    var11 = i32_load(((var15 << 2) + 8451904))
                                    if (1 if i32_load(((var15 << 2) + 8451904)) == var39 else 0):
                                        break
                                    if (1 if var11 == var36 else 0):
                                        break
                                    if (1 if var11 == var46 else 0):
                                        break
                                    if (1 if var11 == var45 else 0):
                                        break
                                    var3 = 2147483647
                                    var17 = 0
                                    var4 = 0
                                    var5 = ((var11 * 404) + 9568096)
                                    var20 = i32_load(((var11 * 404) + 9568096) + 180)
                                    var13 = i32_load(i32_load(((var11 * 404) + 9568096) + 180) + 112)
                                    if i32_load(i32_load(((var11 * 404) + 9568096) + 180) + 112):
                                        while True:  # loop $label364
                                            var1 = i32_load(((var8 + (i32_load((var20 + (var4 << 2)) + 72) << 2)) + 284636))
                                            if (1 if i32_load(((var8 + (i32_load((var20 + (var4 << 2)) + 72) << 2)) + 284636)) == 0 else 0):
                                                break
                                            var10 = i32_load(var1 + 8)
                                            if (1 if i32_load(var1 + 8) == 0 else 0):
                                                break
                                            var9 = i32_load(var1)
                                            var1 = 0
                                            while True:  # loop $label363
                                                var2 = var3
                                                var3 = i32_load((var9 + (var1 << 2)))
                                                if (1 if i32_load((var9 + (var1 << 2))) == 0 else 0):
                                                    var3 = var2
                                                    break
                                                var6 = (var22 + (var3 * 132))
                                                var7 = i32_load8_u((var22 + (var3 * 132)) + 125)
                                                if (1 if ((1 if i32_load8_u((var22 + (var3 * 132)) + 125) <= 14 else 0) if ((1 << var7) & 17424) else 0) == 0 else 0):
                                                    var3 = i32_load(var6 + 44)
                                                    if var7:
                                                        break
                                                    if (1 if ((1 if var3 == 0 else 0) | (1 if i32_load((var25 + (var3 << 4)) + 4) == 22 else 0)) == 0 else 0):
                                                        break
                                                    if i32_load(var6 + 36):
                                                        break
                                                    if (1 if i32_load8_u(var6 + 129) != 10 else 0):
                                                        break
                                                    var3 = (((var3 - var34) * 25) + 1)
                                                    if (1 if (((var3 - var34) * 25) + 1) < var2 else 0):
                                                        break
                                                    var3 = var2
                                                    break
                                                    var3 = 0
                                                    if var2:
                                                        break
                                                    break
                                                var3 = (2147483647 if (1 if var2 >= 2147483647 else 0) else var2)
                                                break
                                                if var3:
                                                    break
                                                var17 = i32_load(var6 + 28)
                                                var3 = 0
                                                var1 = (var1 + 1)
                                                if (1 if (var1 + 1) != var10 else 0):
                                                    continue
                                                break  # end loop
                                            var4 = (var4 + 1)
                                            if (1 if (var4 + 1) != var13 else 0):
                                                continue
                                            break  # end loop
                                    var14 = (var8 + (var11 * 1056))
                                    var1 = i32_load(((var8 + (var11 * 36)) + 269376))
                                    var1 = (i32_load(((var8 + (var11 * 36)) + 269376)) if var1 else 100)
                                    var35 = ((i32_load(((var8 + (var11 * 36)) + 269376)) if var1 else 100) * i32_load(var5 + 80))
                                    var29 = (((i32_load(((var8 + (var11 * 36)) + 269376)) if var1 else 100) * i32_load(var5 + 80)) // 100)
                                    var41 = (i32_load(var5 + 76) * var1)
                                    var24 = ((i32_load(var5 + 76) * var1) // 100)
                                    var38 = (i32_load(var5 + 72) * var1)
                                    var28 = ((i32_load(var5 + 72) * var1) // 100)
                                    var42 = (var1 * i32_load(var5 + 68))
                                    var23 = ((var1 * i32_load(var5 + 68)) // 100)
                                    if (1 if var15 == 0 else 0):
                                        break
                                    if (1 if var11 == -1 else 0):
                                        break
                                    var98 = (-(var74 - float(var29)))
                                    var99 = (-(var81 - float(var24)))
                                    var100 = (-(var71 - float(var28)))
                                    var101 = (-(var84 - float(var23)))
                                    var102 = f32_load(var14 + 96)
                                    var4 = 0
                                    while True:  # loop $label368
                                        var5 = i32_load(((var4 << 2) + 8451904))
                                        var1 = ((i32_load(((var4 << 2) + 8451904)) * 404) + 9568096)
                                        var2 = i32_load(((var8 + (var5 * 36)) + 269376))
                                        var2 = (i32_load(((var8 + (var5 * 36)) + 269376)) if var2 else 100)
                                        var5 = (var8 + (var5 * 1056))
                                        var66 = float(i32_load((var8 + (var5 * 1056)) + 108))
                                        var66 = math.ceil((float(i32_load((var8 + (var5 * 1056)) + 108)) - ((var102 * var66) / f32_load(var5 + 96))))
                                        var103 = (float(((i32_load(((i32_load(((var4 << 2) + 8451904)) * 404) + 9568096) + 80) * (i32_load(((var8 + (var5 * 36)) + 269376)) if var2 else 100)) // 100)) * math.ceil((float(i32_load((var8 + (var5 * 1056)) + 108)) - ((var102 * var66) / f32_load(var5 + 96)))))
                                        var70 = ((float(((i32_load(((i32_load(((var4 << 2) + 8451904)) * 404) + 9568096) + 80) * (i32_load(((var8 + (var5 * 36)) + 269376)) if var2 else 100)) // 100)) * math.ceil((float(i32_load((var8 + (var5 * 1056)) + 108)) - ((var102 * var66) / f32_load(var5 + 96))))) + var94)
                                        var72 = (float(((i32_load(var1 + 76) * var2) // 100)) * var66)
                                        var69 = ((float(((i32_load(var1 + 76) * var2) // 100)) * var66) + var95)
                                        var5 = (1 if ((float(((i32_load(var1 + 76) * var2) // 100)) * var66) + var95) < 0.0 else 0)
                                        var77 = (float(((i32_load(var1 + 72) * var2) // 100)) * var66)
                                        var67 = ((float(((i32_load(var1 + 72) * var2) // 100)) * var66) + var96)
                                        var68 = (0.0 if (1 if var67 < 0.0 else 0) else ((float(((i32_load(var1 + 72) * var2) // 100)) * var66) + var96))
                                        var67 = 0.0
                                        var104 = (float(((var2 * i32_load(var1 + 68)) // 100)) * var66)
                                        var78 = ((float(((var2 * i32_load(var1 + 68)) // 100)) * var66) + var97)
                                        var78 = (0.0 if (1 if var78 < 0.0 else 0) else ((float(((var2 * i32_load(var1 + 68)) // 100)) * var66) + var97))
                                        if (1 if (0.0 if (1 if var78 < 0.0 else 0) else ((float(((var2 * i32_load(var1 + 68)) // 100)) * var66) + var97)) > 0.0 else 0):
                                            var67 = (var78 / var89)
                                            var67 = ((var78 / var89) if (1 if var67 > 0.0 else 0) else 0.0)
                                        if (1 if var68 > 0.0 else 0):
                                            var68 = (var68 / var88)
                                            var67 = ((var68 / var88) if (1 if var67 < var68 else 0) else var67)
                                        var68 = (0.0 if var5 else var69)
                                        if (1 if (0.0 if var5 else var69) > 0.0 else 0):
                                            var68 = (var68 / var87)
                                            var67 = ((var68 / var87) if (1 if var67 < var68 else 0) else var67)
                                        var70 = (0.0 if (1 if var70 < 0.0 else 0) else var70)
                                        if (1 if (0.0 if (1 if var70 < 0.0 else 0) else var70) > 0.0 else 0):
                                            var70 = (var70 / var86)
                                            var67 = ((var70 / var86) if (1 if var67 < var70 else 0) else var67)
                                        var1 = i32_load(var1 + 116)
                                        var69 = float(i32_load(var1 + 116))
                                        var70 = var66
                                        if (1 if var1 == 0 else 0):
                                            break
                                        var70 = (var67 / var69)
                                        if (1 if (1 if (var67 / var69) > var66 else 0) == 0 else 0):
                                            break
                                        var70 = var66
                                        var78 = (var72 + var99)
                                        var2 = (1 if (var72 + var99) < 0.0 else 0)
                                        var68 = (var77 + var100)
                                        var72 = (0.0 if (1 if var68 < 0.0 else 0) else (var77 + var100))
                                        var68 = 0.0
                                        var77 = (var104 + var101)
                                        var77 = (0.0 if (1 if var77 < 0.0 else 0) else (var104 + var101))
                                        if (1 if (0.0 if (1 if var77 < 0.0 else 0) else (var104 + var101)) > 0.0 else 0):
                                            var68 = (var77 / var89)
                                            var68 = ((var77 / var89) if (1 if var68 > 0.0 else 0) else 0.0)
                                        if (1 if var72 > 0.0 else 0):
                                            var72 = (var72 / var88)
                                            var68 = ((var72 / var88) if (1 if var68 < var72 else 0) else var68)
                                        var72 = (0.0 if var2 else var78)
                                        if (1 if (0.0 if var2 else var78) > 0.0 else 0):
                                            var72 = (var72 / var87)
                                            var68 = ((var72 / var87) if (1 if var68 < var72 else 0) else var68)
                                        var72 = (var103 + var98)
                                        var72 = (0.0 if (1 if var72 < 0.0 else 0) else (var103 + var98))
                                        if (1 if (0.0 if (1 if var72 < 0.0 else 0) else (var103 + var98)) > 0.0 else 0):
                                            var72 = (var72 / var86)
                                            var68 = ((var72 / var86) if (1 if var68 < var72 else 0) else var68)
                                        var70 = ((((var66 - var70) + 1.0) * var69) + var67)
                                        var67 = var66
                                        if (1 if var1 == 0 else 0):
                                            break
                                        var67 = (var68 / var69)
                                        if (1 if (1 if (var68 / var69) > var66 else 0) == 0 else 0):
                                            break
                                        var67 = var66
                                        if (1 if var70 < 0.0 else 0):
                                            break
                                        if (1 if abs((var70 - ((((var66 - var67) + 1.0) * var69) + var68))) > 1.0 else 0):
                                            break
                                        var4 = (var4 + 1)
                                        if (1 if (var4 + 1) != var15 else 0):
                                            continue
                                        break  # end loop
                                    if (1 if var17 == 0 else 0):
                                        break
                                    var9 = i32_load(var44)
                                    var10 = i32_load(var31)
                                    var13 = i32_load(var32)
                                    var5 = i32_load(var33)
                                    if (1 if var18 >= 2 else 0):
                                        var37 = i32_load(var63)
                                        var1 = 1
                                        var2 = var9
                                        var3 = var10
                                        var4 = var13
                                        var6 = var5
                                        while True:  # loop $label373
                                            var7 = i32_load8_u((var27 + ((var1 * var18) + var37)))
                                            if (1 if (i32_load8_u((var27 + ((var1 * var18) + var37))) & 1) == 0 else 0):
                                                break
                                            if (1 if var6 == 2147483647 else 0):
                                                break
                                            var5 = i32_load((var21 + (var1 * 286704)) + 283848)
                                            var5 = (2147483647 if (1 if var5 == 2147483647 else 0) else (i32_load((var21 + (var1 * 286704)) + 283848) + var6))
                                            var6 = (2147483647 if (1 if var5 == 2147483647 else 0) else (i32_load((var21 + (var1 * 286704)) + 283848) + var6))
                                            if (1 if (var7 & 2) == 0 else 0):
                                                break
                                            if (1 if var4 == 2147483647 else 0):
                                                break
                                            var13 = i32_load(((var21 + (var1 * 286704)) + 283852))
                                            var13 = (2147483647 if (1 if var13 == 2147483647 else 0) else (var4 + i32_load(((var21 + (var1 * 286704)) + 283852))))
                                            var4 = (2147483647 if (1 if var13 == 2147483647 else 0) else (var4 + i32_load(((var21 + (var1 * 286704)) + 283852))))
                                            if (1 if (var7 & 4) == 0 else 0):
                                                break
                                            if (1 if var3 == 2147483647 else 0):
                                                break
                                            var10 = i32_load(((var21 + (var1 * 286704)) + 283856))
                                            var10 = (2147483647 if (1 if var10 == 2147483647 else 0) else (var3 + i32_load(((var21 + (var1 * 286704)) + 283856))))
                                            var3 = (2147483647 if (1 if var10 == 2147483647 else 0) else (var3 + i32_load(((var21 + (var1 * 286704)) + 283856))))
                                            if (1 if (var7 & 8) == 0 else 0):
                                                break
                                            if (1 if var2 == 2147483647 else 0):
                                                break
                                            var7 = i32_load(((var21 + (var1 * 286704)) + 283860))
                                            var9 = (2147483647 if (1 if var7 == 2147483647 else 0) else (var2 + i32_load(((var21 + (var1 * 286704)) + 283860))))
                                            var2 = (2147483647 if (1 if var7 == 2147483647 else 0) else (var2 + i32_load(((var21 + (var1 * 286704)) + 283860))))
                                            var1 = (var1 + 1)
                                            if (1 if (var1 + 1) != var18 else 0):
                                                continue
                                            break  # end loop
                                    if ((1 if var5 < var23 else 0) & (1 if (var42 - 100) <= -200 else 0)):
                                        break
                                    if ((1 if var13 < var28 else 0) & (1 if (var38 - 100) <= -200 else 0)):
                                        break
                                    if ((1 if var10 < var24 else 0) & (1 if (var41 - 100) <= -200 else 0)):
                                        break
                                    if ((1 if var9 < var29 else 0) & (1 if (var35 - 100) <= -200 else 0)):
                                        break
                                    if (1 if i32_load8_u(var20 + 23) == 0 else 0):
                                        break
                                    var1 = i32_load(var20 + 4)
                                    if (1 if i32_load(((i32_load(var20 + 4) * 404) + 9568096) + 264) != 3 else 0):
                                        break
                                    if i32_load(((var8 + (var1 << 2)) + 281808)):
                                        break
                                    var4 = i32_load(var20 + 68)
                                    if i32_load(var20 + 68):
                                        var1 = 0
                                        var7 = 1
                                        var3 = 0
                                        var6 = 0
                                        while True:  # loop $label377
                                            var13 = i32_load((var20 + (var1 << 2)) + 28)
                                            var2 = i32_load(((i32_load((var20 + (var1 << 2)) + 28) * 404) + 9568096) + 264)
                                            var5 = (1 if i32_load(((i32_load((var20 + (var1 << 2)) + 28) * 404) + 9568096) + 264) == 1 else 0)
                                            var13 = i32_load(((var8 + (var13 << 2)) + 281808))
                                            if (1 if i32_load(((var8 + (var13 << 2)) + 281808)) == 1 else 0):
                                                break
                                            var7 = ((1 if var2 != 3 else 0) & var7)
                                            if var13:
                                                break
                                            var7 = ((1 if var2 != 0 else 0) & var7)
                                            break
                                            var6 = (var5 | var6)
                                            var3 = (var3 | var5)
                                            var1 = (var1 + 1)
                                            if (1 if (var1 + 1) != var4 else 0):
                                                continue
                                            break  # end loop
                                        if (1 if (((var6 & var7) if (var3 & 1) else var7) & 1) == 0 else 0):
                                            break
                                    if (1 if func461(var11, var17, var8) == 0 else 0):
                                        var2 = i32_load(9140296)
                                        var26 = (i32_load(9140296) - 1)
                                        i32_store(9140296, (i32_load(9140296) - 1))
                                        if (1 if var15 >= var26 else 0):
                                            continue
                                        var5 = ((var2 - var15) - 2)
                                        var1 = 0
                                        var2 = ((var2 + (var15 ^ -1)) & 3)
                                        if ((var2 + (var15 ^ -1)) & 3):
                                            while True:  # loop $label379
                                                var15 = (var15 + 1)
                                                i32_store(((var15 << 2) + 8451904), i32_load((((var15 + 1) << 2) + 8451904)))
                                                var1 = (var1 + 1)
                                                if (1 if (var1 + 1) != var2 else 0):
                                                    continue
                                                break  # end loop
                                        if (1 if var5 < 3 else 0):
                                            continue
                                        while True:  # loop $label380
                                            var1 = ((var15 << 2) + 8451904)
                                            var107 = i64_load(((var15 << 2) + 8451904) + 4)
                                            i32_store(var1 + 8, i32_load(var1 + 12))
                                            i64_store(var1, var107)
                                            var15 = (var15 + 4)
                                            i32_store(var1 + 12, i32_load((((var15 + 4) << 2) + 8451904)))
                                            if (1 if var15 != var26 else 0):
                                                continue
                                            break  # end loop
                                        continue
                                    var1 = (i32_load(var14 + 108) - 1)
                                    i32_store(var14 + 108, (i32_load(var14 + 108) - 1))
                                    f32_store(var14 + 96, (f32_load(var14 + 96) - f32_load(var14 + 100)))
                                    var2 = i32_load(9140296)
                                    var26 = i32_load(9140296)
                                    if var1:
                                        continue
                                    var26 = (var2 - 1)
                                    i32_store(9140296, (var2 - 1))
                                    if (1 if var15 >= var26 else 0):
                                        continue
                                    var5 = ((var2 - var15) - 2)
                                    var1 = 0
                                    var2 = ((var2 + (var15 ^ -1)) & 3)
                                    if ((var2 + (var15 ^ -1)) & 3):
                                        while True:  # loop $label381
                                            var15 = (var15 + 1)
                                            i32_store(((var15 << 2) + 8451904), i32_load((((var15 + 1) << 2) + 8451904)))
                                            var1 = (var1 + 1)
                                            if (1 if (var1 + 1) != var2 else 0):
                                                continue
                                            break  # end loop
                                    if (1 if var5 < 3 else 0):
                                        continue
                                    while True:  # loop $label382
                                        var1 = ((var15 << 2) + 8451904)
                                        var107 = i64_load(((var15 << 2) + 8451904) + 4)
                                        i32_store(var1 + 8, i32_load(var1 + 12))
                                        i64_store(var1, var107)
                                        var15 = (var15 + 4)
                                        i32_store(var1 + 12, i32_load((((var15 + 4) << 2) + 8451904)))
                                        if (1 if var15 != var26 else 0):
                                            continue
                                        break  # end loop
                                    continue
                                    var15 = (var15 + 1)
                                    if (1 if (var15 + 1) != var26 else 0):
                                        continue
                                    break  # end loop
                            break  # end loop
                        if (1 if var16 == 0 else 0):
                            break
                        var1 = (var8 + (i32_load(38528) << 2))
                        var2 = i32_load(((var8 + (i32_load(38528) << 2)) + 284636))
                        if (1 if i32_load(((var8 + (i32_load(38528) << 2)) + 284636)) == 0 else 0):
                            break
                        var4 = i32_load(var2 + 8)
                        if (1 if i32_load(var2 + 8) == 0 else 0):
                            break
                        var5 = (500 if (1 if i32_load((var1 + 281808)) > 24 else 0) else 452)
                        var1 = 0
                        while True:  # loop $label386
                            var3 = i32_load((i32_load(var2) + (var1 << 2)))
                            if (1 if i32_load((i32_load(var2) + (var1 << 2))) == 0 else 0):
                                break
                            var3 = (i32_load(9671128) + (var3 * 132))
                            if (1 if i32_load((i32_load(9671128) + (var3 * 132)) + 80) < var5 else 0):
                                break
                            var4 = i32_load(var2 + 8)
                            var1 = (var1 + 1)
                            if (1 if (var1 + 1) < var4 else 0):
                                continue
                            break  # end loop
                        if (1 if var85 != 0.0 else 0):
                            break
                        if (1 if var83 != 0.0 else 0):
                            break
                        if (1 if var82 != 0.0 else 0):
                            break
                        if (1 if var79 == 0.0 else 0):
                            break
                        var17 = i32_load(((var8 + (i32_load(38528) << 2)) + 281808))
                        if (1 if i32_load(((var8 + (i32_load(38528) << 2)) + 281808)) < 8 else 0):
                            break
                        if (1 if var17 < 40 else 0):
                            var17 = ((((var17 * 30) & 0xFFFFFFFF) // 100) + 8)
                            break
                        var17 = ((((var17 * 20) & 0xFFFFFFFF) // 100) + 20)
                        var66 = ((var73 * var79) / (var90 / f32_load(9682188)))
                        var70 = ((var80 * var85) / (var93 / f32_load(9682176)))
                        var68 = (((var76 * var83) / (var92 / f32_load(9682180))) * 2.5)
                        var69 = ((var75 * var82) / (var91 / f32_load(9682184)))
                        var66 = (var66 + (((((var80 * var85) / (var93 / f32_load(9682176))) + 0.0) + (((var76 * var83) / (var92 / f32_load(9682180))) * 2.5)) + ((var75 * var82) / (var91 / f32_load(9682184)))))
                        var73 = (((var73 * var79) / (var90 / f32_load(9682188))) / (var66 + (((((var80 * var85) / (var93 / f32_load(9682176))) + 0.0) + (((var76 * var83) / (var92 / f32_load(9682180))) * 2.5)) + ((var75 * var82) / (var91 / f32_load(9682184))))))
                        var67 = float(i32_load((var30 + 281808)))
                        var105 = (float(((((var73 * var79) / (var90 / f32_load(9682188))) / (var66 + (((((var80 * var85) / (var93 / f32_load(9682176))) + 0.0) + (((var76 * var83) / (var92 / f32_load(9682180))) * 2.5)) + ((var75 * var82) / (var91 / f32_load(9682184)))))) * float(i32_load((var30 + 281808))))) + 0.5)
                        if ((1 if (float(((((var73 * var79) / (var90 / f32_load(9682188))) / (var66 + (((((var80 * var85) / (var93 / f32_load(9682176))) + 0.0) + (((var76 * var83) / (var92 / f32_load(9682180))) * 2.5)) + ((var75 * var82) / (var91 / f32_load(9682184)))))) * float(i32_load((var30 + 281808))))) + 0.5) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                            break
                        var3 = 0
                        i32_store(int(var105) + 28, 0)
                        var69 = (var69 / var66)
                        var105 = (float(((var69 / var66) * var67)) + 0.5)
                        if ((1 if (float(((var69 / var66) * var67)) + 0.5) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                            break
                        var1 = 0
                        i32_store(int(var105) + 24, 0)
                        var68 = (var68 / var66)
                        var105 = (float(((var68 / var66) * var67)) + 0.5)
                        if ((1 if (float(((var68 / var66) * var67)) + 0.5) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                            break
                        var2 = 0
                        i32_store(int(var105) + 20, 0)
                        var70 = (var70 / var66)
                        var105 = (float(((var70 / var66) * var67)) + 0.5)
                        if ((1 if (float(((var70 / var66) * var67)) + 0.5) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                            break
                        var5 = 0
                        i32_store(int(var105) + 16, 0)
                        var66 = (f32_load(var19 + 40) - float(var12))
                        if ((1 if (f32_load(var19 + 40) - float(var12)) < 4294967300.0 else 0) & (1 if var66 >= 0.0 else 0)):
                            break
                        var4 = 0
                        if var16:
                            var10 = (var4 + var17)
                            if (1 if var1 < (var4 + var17) else 0):
                                var10 = var1
                                break
                            i32_store(var19 + 24, var10)
                            var66 = float((var1 - var10))
                            var67 = (1.0 - var69)
                            # Unknown: f64.convert_i32_u []
                            var105 = ((float(((var73 * float((var1 - var10))) / (1.0 - var69))) + 0.5) + var3)
                            if ((1 if ((float(((var73 * float((var1 - var10))) / (1.0 - var69))) + 0.5) + var3) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                                break
                            var3 = 0
                            i32_store(int(var105) + 28, 0)
                            # Unknown: f64.convert_i32_u []
                            var105 = ((float(((var68 * var66) / var67)) + 0.5) + var2)
                            if ((1 if ((float(((var68 * var66) / var67)) + 0.5) + var2) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                                break
                            var2 = 0
                            i32_store(int(var105) + 20, 0)
                            # Unknown: f64.convert_i32_u []
                            var105 = ((float(((var70 * var66) / var67)) + 0.5) + var5)
                            if ((1 if ((float(((var70 * var66) / var67)) + 0.5) + var5) < 4294967296.0 else 0) & (1 if var105 >= 0.0 else 0)):
                                var5 = int(var105)
                                i32_store(var19 + 16, int(var105))
                                break
                            var5 = 0
                            i32_store(var19 + 16, 0)
                            break
                        var6 = i32_load(((i32_load(38500) * 404) + 9568168))
                        if i32_load(((i32_load(38500) * 404) + 9568168)):
                            if ((1 if var71 < 4294967300.0 else 0) & (1 if var71 >= 0.0 else 0)):
                                break
                        else:
                        var10 = (200 + var4)
                        if (1 if ((0 & 0xFFFFFFFF) // var6) < (200 + var4) else 0):
                            var10 = var1
                            break
                        i32_store(var19 + 24, var10)
                        var66 = (float((var1 - var10)) + float(var2))
                        if ((1 if (float((var1 - var10)) + float(var2)) < 4294967300.0 else 0) & (1 if var66 >= 0.0 else 0)):
                            break
                        var2 = 0
                        i32_store(int(var66) + 20, 0)
                        var7 = i32_load(var49)
                        if (1 if i32_load(var49) == 0 else 0):
                            break
                        var6 = i32_load(var7 + 8)
                        if (1 if i32_load(var7 + 8) == 0 else 0):
                            break
                        var73 = float(var3)
                        var75 = float(var2)
                        var76 = float(var5)
                        var71 = float(var10)
                        var3 = 0
                        while True:  # loop $label437
                            var1 = i32_load((i32_load(var7) + (var3 << 2)))
                            if (1 if i32_load((i32_load(var7) + (var3 << 2))) == 0 else 0):
                                break
                            var5 = 1
                            var2 = 2
                            var1 = (i32_load(9671128) + (var1 * 132))
                            var10 = i32_load8_u((i32_load(9671128) + (var1 * 132)) + 129)
                            # br_table ['$label402', '$label403', '$label404', '$label405', '$label406', '$label406', '$label406', '$label406', '$label406', '$label404', '$label406']
                            _br_idx = (i32_load8_u((i32_load(9671128) + (var1 * 132)) + 129) - 1)
                            break  # br_table
                            var2 = 0
                            break
                            var2 = 3
                            break
                            var2 = 55
                            if (1 if f32_load(var19 + 36) != 0.0 else 0):
                                break
                            # br_table ['$label408', '$label407', '$label407', '$label408', '$label407']
                            _br_idx = var2
                            break  # br_table
                            var4 = i32_load(9142840)
                            var13 = (i32_load(9142440) + 2)
                            var9 = ((i32_load(9142440) + 2) + i32_load16_u(var1 + 114))
                            var14 = ((((i32_load(9142440) + 2) + i32_load16_u(var1 + 114)) + 1) * var13)
                            var5 = i32_load16_u(var1 + 112)
                            var15 = (i32_load16_u(var1 + 112) + 2)
                            if (1 if i32_load((i32_load(9142840) + ((((((i32_load(9142440) + 2) + i32_load16_u(var1 + 114)) + 1) * var13) + (i32_load16_u(var1 + 112) + 2)) << 2))) == 0 else 0):
                                var5 = var2
                                break
                            var11 = (var9 * var13)
                            if (1 if i32_load((var4 + (((var9 * var13) + var15) << 2))) == 0 else 0):
                                var5 = var2
                                break
                            var20 = (var5 + 1)
                            if (1 if i32_load((var4 + ((var11 + (var5 + 1)) << 2))) == 0 else 0):
                                var5 = var2
                                break
                            if (1 if i32_load((var4 + ((var5 + var11) << 2))) == 0 else 0):
                                var5 = var2
                                break
                            if (1 if i32_load((var4 + ((var5 + var14) << 2))) == 0 else 0):
                                var5 = var2
                                break
                            var13 = ((var9 + 2) * var13)
                            if (1 if i32_load((var4 + ((((var9 + 2) * var13) + var5) << 2))) == 0 else 0):
                                var5 = var2
                                break
                            if (1 if i32_load((var4 + ((var13 + var20) << 2))) == 0 else 0):
                                var5 = var2
                                break
                            var5 = var2
                            if i32_load((var4 + ((var13 + var15) << 2))):
                                break
                            var2 = (var5 << 2)
                            if (1 if f32_load(((var5 << 2) + (var19 + 32))) > float(i32_load(((var19 + 16) + var2))) else 0):
                                break
                            var2 = var5
                            if (1 if var10 == 10 else 0):
                                break
                            var5 = i32_load(var1 + 44)
                            if (1 if ((1 if i32_load((i32_load(9215884) + (i32_load(var1 + 44) << 4)) + 4) == 22 else 0) | (1 if var5 == 0 else 0)) == 0 else 0):
                                break
                            if i32_load8_u(var1 + 125):
                                break
                            if (1 if i32_load(var1 + 36) == 0 else 0):
                                break
                            break
                            if (1 if var10 != 10 else 0):
                                var2 = var5
                                break
                            var2 = i32_load(var1 + 44)
                            if (1 if ((1 if i32_load((i32_load(9215884) + (i32_load(var1 + 44) << 4)) + 4) == 22 else 0) | (1 if var2 == 0 else 0)) == 0 else 0):
                                break
                            if i32_load8_u(var1 + 125):
                                break
                            var2 = var5
                            if i32_load(var1 + 36):
                                break
                            i32_store(var19 + 12, 0)
                            var66 = f32_load(var19 + 40)
                            if ((1 if f32_load(var19 + 40) >= var71 else 0) & var16):
                                i32_store8(var19 + 14, 1)
                            var66 = ((var66 + 1.0) / var71)
                            var67 = ((f32_load(var19 + 32) + 1.0) / var76)
                            var5 = (1 if var67 < 99999.0 else 0)
                            var68 = (((f32_load(var19 + 32) + 1.0) / var76) if (1 if var67 < 99999.0 else 0) else 99999.0)
                            var4 = (1 if var2 == 0 else 0)
                            var15 = ((1 if var2 == 0 else 0) | (1 if i32_load8_u(var19 + 12) != 0 else 0))
                            var70 = (99999.0 if ((1 if var2 == 0 else 0) | (1 if i32_load8_u(var19 + 12) != 0 else 0)) else (((f32_load(var19 + 32) + 1.0) / var76) if (1 if var67 < 99999.0 else 0) else 99999.0))
                            var67 = ((f32_load(var19 + 36) + 1.0) / var75)
                            var11 = (1 if var67 < var70 else 0)
                            var13 = (1 if var2 == 1 else 0)
                            var14 = ((1 if var2 == 1 else 0) | (1 if i32_load8_u(var19 + 13) != 0 else 0))
                            var69 = ((99999.0 if ((1 if var2 == 0 else 0) | (1 if i32_load8_u(var19 + 12) != 0 else 0)) else (((f32_load(var19 + 32) + 1.0) / var76) if (1 if var67 < 99999.0 else 0) else 99999.0)) if ((1 if var2 == 1 else 0) | (1 if i32_load8_u(var19 + 13) != 0 else 0)) else (((f32_load(var19 + 36) + 1.0) / var75) if (1 if var67 < var70 else 0) else var70))
                            var6 = (1 if ((var66 + 1.0) / var71) < ((99999.0 if ((1 if var2 == 0 else 0) | (1 if i32_load8_u(var19 + 12) != 0 else 0)) else (((f32_load(var19 + 32) + 1.0) / var76) if (1 if var67 < 99999.0 else 0) else 99999.0)) if ((1 if var2 == 1 else 0) | (1 if i32_load8_u(var19 + 13) != 0 else 0)) else (((f32_load(var19 + 36) + 1.0) / var75) if (1 if var67 < var70 else 0) else var70)) else 0)
                            var9 = (1 if var2 == 2 else 0)
                            var10 = ((1 if var2 == 2 else 0) | (1 if i32_load8_u(var19 + 14) != 0 else 0))
                            var5 = (0 if var5 else 5)
                            var70 = ((f32_load(var19 + 44) + 1.0) / var73)
                            var20 = i32_load(var1 + 28)
                            var21 = i32_load8_u(var1 + 129)
                            if i32_load8_u(var19 + 15):
                                break
                            if (1 if var2 == 3 else 0):
                                break
                            if (1 if var70 < (var69 if var10 else (var66 if var6 else var69)) else 0):
                                break
                            var15 = (5 if var15 else var5)
                            var15 = ((5 if var15 else var5) if var14 else (1 if var11 else var15))
                            # br_table ['$label413', '$label414', '$label415', '$label412', '$label416']
                            _br_idx = (((5 if var15 else var5) if var14 else (1 if var11 else var15)) if var10 else (2 if var6 else var15))
                            break  # br_table
                            var6 = 2
                            var10 = 1
                            if func143(var1, var16):
                                break
                            break
                            var10 = 0
                            var6 = 0
                            if func87(var1, i32_load(38504)):
                                break
                            break
                            var10 = 0
                            var6 = 3
                            if (1 if func87(var1, i32_load(38508)) == 0 else 0):
                                break
                            break
                            var6 = 1
                            var10 = 0
                            if func142(var1, 0):
                                break
                            i32_store8((i32_load(9671128) + (var20 * 132)) + 129, var21)
                            i32_store8(((var19 + 12) | var6), 1)
                            var15 = ((1 if i32_load8_u(var19 + 12) != 0 else 0) | var4)
                            var69 = (99999.0 if ((1 if i32_load8_u(var19 + 12) != 0 else 0) | var4) else var68)
                            var11 = (1 if var67 < var69 else 0)
                            var14 = ((1 if i32_load8_u(var19 + 13) != 0 else 0) | var13)
                            var69 = ((99999.0 if ((1 if i32_load8_u(var19 + 12) != 0 else 0) | var4) else var68) if ((1 if i32_load8_u(var19 + 13) != 0 else 0) | var13) else (var67 if (1 if var67 < var69 else 0) else var69))
                            var6 = (1 if var66 < ((99999.0 if ((1 if i32_load8_u(var19 + 12) != 0 else 0) | var4) else var68) if ((1 if i32_load8_u(var19 + 13) != 0 else 0) | var13) else (var67 if (1 if var67 < var69 else 0) else var69)) else 0)
                            var10 = ((1 if i32_load8_u(var19 + 14) != 0 else 0) | var9)
                            var20 = i32_load8_u(var1 + 129)
                            var21 = i32_load(var1 + 28)
                            if i32_load8_u(var19 + 15):
                                break
                            if (1 if var2 == 3 else 0):
                                break
                            if (1 if var70 < (var69 if var10 else (var66 if var6 else var69)) else 0):
                                break
                            var15 = (5 if var15 else var5)
                            var15 = ((5 if var15 else var5) if var14 else (1 if var11 else var15))
                            # br_table ['$label421', '$label422', '$label423', '$label420', '$label416']
                            _br_idx = (((5 if var15 else var5) if var14 else (1 if var11 else var15)) if var10 else (2 if var6 else var15))
                            break  # br_table
                            var10 = 0
                            var6 = 0
                            if func87(var1, i32_load(38504)):
                                break
                            break
                            var6 = 2
                            var10 = 1
                            if func143(var1, var16):
                                break
                            break
                            var6 = 1
                            var10 = 0
                            if func142(var1, 0):
                                break
                            break
                            var10 = 0
                            var6 = 3
                            if func87(var1, i32_load(38508)):
                                break
                            i32_store8((i32_load(9671128) + (var21 * 132)) + 129, var20)
                            i32_store8(((var19 + 12) | var6), 1)
                            var15 = ((1 if i32_load8_u(var19 + 12) != 0 else 0) | var4)
                            var69 = (99999.0 if ((1 if i32_load8_u(var19 + 12) != 0 else 0) | var4) else var68)
                            var11 = (1 if var67 < var69 else 0)
                            var14 = ((1 if i32_load8_u(var19 + 13) != 0 else 0) | var13)
                            var69 = ((99999.0 if ((1 if i32_load8_u(var19 + 12) != 0 else 0) | var4) else var68) if ((1 if i32_load8_u(var19 + 13) != 0 else 0) | var13) else (var67 if (1 if var67 < var69 else 0) else var69))
                            var6 = (1 if var66 < ((99999.0 if ((1 if i32_load8_u(var19 + 12) != 0 else 0) | var4) else var68) if ((1 if i32_load8_u(var19 + 13) != 0 else 0) | var13) else (var67 if (1 if var67 < var69 else 0) else var69)) else 0)
                            var10 = ((1 if i32_load8_u(var19 + 14) != 0 else 0) | var9)
                            var20 = i32_load8_u(var1 + 129)
                            var21 = i32_load(var1 + 28)
                            if i32_load8_u(var19 + 15):
                                break
                            if (1 if var2 == 3 else 0):
                                break
                            if (1 if var70 < (var69 if var10 else (var66 if var6 else var69)) else 0):
                                break
                            var15 = (5 if var15 else var5)
                            var15 = ((5 if var15 else var5) if var14 else (1 if var11 else var15))
                            # br_table ['$label427', '$label428', '$label429', '$label426', '$label416']
                            _br_idx = (((5 if var15 else var5) if var14 else (1 if var11 else var15)) if var10 else (2 if var6 else var15))
                            break  # br_table
                            var10 = 0
                            var6 = 0
                            if func87(var1, i32_load(38504)):
                                break
                            break
                            var6 = 2
                            var10 = 1
                            if func143(var1, var16):
                                break
                            break
                            var6 = 1
                            var10 = 0
                            if func142(var1, 0):
                                break
                            break
                            var10 = 0
                            var6 = 3
                            if func87(var1, i32_load(38508)):
                                break
                            i32_store8((i32_load(9671128) + (var21 * 132)) + 129, var20)
                            i32_store8(((var19 + 12) | var6), 1)
                            var10 = ((1 if i32_load8_u(var19 + 12) != 0 else 0) | var4)
                            var68 = (99999.0 if ((1 if i32_load8_u(var19 + 12) != 0 else 0) | var4) else var68)
                            var15 = (1 if var67 < var68 else 0)
                            var13 = ((1 if i32_load8_u(var19 + 13) != 0 else 0) | var13)
                            var67 = ((99999.0 if ((1 if i32_load8_u(var19 + 12) != 0 else 0) | var4) else var68) if ((1 if i32_load8_u(var19 + 13) != 0 else 0) | var13) else (var67 if (1 if var67 < var68 else 0) else var68))
                            var4 = (1 if var66 < ((99999.0 if ((1 if i32_load8_u(var19 + 12) != 0 else 0) | var4) else var68) if ((1 if i32_load8_u(var19 + 13) != 0 else 0) | var13) else (var67 if (1 if var67 < var68 else 0) else var68)) else 0)
                            var6 = ((1 if i32_load8_u(var19 + 14) != 0 else 0) | var9)
                            var9 = i32_load8_u(var1 + 129)
                            var11 = i32_load(var1 + 28)
                            if i32_load8_u(var19 + 15):
                                break
                            if (1 if var2 == 3 else 0):
                                break
                            if (1 if var70 < (var67 if var6 else (var66 if var4 else var67)) else 0):
                                break
                            var5 = (5 if var10 else var5)
                            var5 = ((5 if var10 else var5) if var13 else (1 if var15 else var5))
                            # br_table ['$label433', '$label434', '$label435', '$label432', '$label416']
                            _br_idx = (((5 if var10 else var5) if var13 else (1 if var15 else var5)) if var6 else (2 if var4 else var5))
                            break  # br_table
                            var10 = 0
                            var6 = 0
                            if func87(var1, i32_load(38504)):
                                break
                            break
                            var6 = 2
                            var10 = 1
                            if func143(var1, var16):
                                break
                            break
                            var6 = 1
                            var10 = 0
                            if func142(var1, 0):
                                break
                            break
                            var10 = 0
                            var6 = 3
                            if func87(var1, i32_load(38508)):
                                break
                            i32_store8((i32_load(9671128) + (var11 * 132)) + 129, var9)
                            i32_store8(((var19 + 12) | var6), 1)
                            break
                            if (1 if var2 <= 3 else 0):
                                var1 = ((var19 + 32) + (var2 << 2))
                                f32_store(((var19 + 32) + (var2 << 2)), (f32_load(var1) + -1.0))
                            var1 = (var6 << 2)
                            var2 = ((var6 << 2) | (var19 + 32))
                            f32_store(((var6 << 2) | (var19 + 32)), (f32_load(var2) + 1.0))
                            var2 = ((var19 - -64) | var1)
                            f32_store(((var19 - -64) | var1), (f32_load(var2) + (f32_load(((var19 + 48) | var1)) / f32_load((var1 + 9682176)))))
                            var12 = (var12 + (var10 & var16))
                            var6 = i32_load(var7 + 8)
                            var3 = (var3 + 1)
                            if (1 if (var3 + 1) < var6 else 0):
                                continue
                            break  # end loop
                        if (1 if (var16 & (1 if var12 == 0 else 0)) == 0 else 0):
                            break
                        if (1 if var17 == 0 else 0):
                            break
                        var1 = i32_load(var49)
                        if (1 if i32_load(var49) == 0 else 0):
                            break
                        var5 = i32_load(var1 + 8)
                        if (1 if i32_load(var1 + 8) == 0 else 0):
                            break
                        var4 = 0
                        var6 = i32_load(9671128)
                        var7 = i32_load(var1)
                        var3 = 2147483647
                        var1 = 0
                        while True:  # loop $label438
                            var2 = i32_load((var7 + (var1 << 2)))
                            if i32_load((var7 + (var1 << 2))):
                                var2 = (var6 + (var2 * 132))
                                var13 = (i32_load16_u((var6 + (var2 * 132)) + 114) - i32_load(var52))
                                var13 = (i32_load16_u(var2 + 112) - i32_load(var43))
                                var13 = (((i32_load16_u((var6 + (var2 * 132)) + 114) - i32_load(var52)) * var13) + ((i32_load16_u(var2 + 112) - i32_load(var43)) * var13))
                                var13 = ((1 if i32_load8_u(var2 + 125) == 0 else 0) & (1 if var3 > var13 else 0))
                                var3 = ((((i32_load16_u((var6 + (var2 * 132)) + 114) - i32_load(var52)) * var13) + ((i32_load16_u(var2 + 112) - i32_load(var43)) * var13)) if ((1 if i32_load8_u(var2 + 125) == 0 else 0) & (1 if var3 > var13 else 0)) else var3)
                                var4 = (i32_load(var2 + 28) if var13 else var4)
                            var1 = (var1 + 1)
                            if (1 if (var1 + 1) != var5 else 0):
                                continue
                            break  # end loop
                        if (1 if var4 == 0 else 0):
                            break
                        var44 = 0
                        var16 = 0
                        var26 = 0
                        while True:  # loop $label543
                            var3 = i32_load(((var26 * 404) + 9568096) + 264)
                            if (1 if i32_load(((var26 * 404) + 9568096) + 264) != 1 else 0):
                                break
                            var2 = i32_load(((var8 + (var26 << 2)) + 284636))
                            if (1 if i32_load(((var8 + (var26 << 2)) + 284636)) == 0 else 0):
                                break
                            var4 = i32_load(var2 + 8)
                            if (1 if i32_load(var2 + 8) == 0 else 0):
                                break
                            var1 = 0
                            var6 = i32_load(9671128)
                            var7 = i32_load(var2)
                            while True:  # loop $label441
                                var2 = i32_load((var7 + (var1 << 2)))
                                if (1 if i32_load((var7 + (var1 << 2))) == 0 else 0):
                                    break
                                var5 = (var6 + (var2 * 132))
                                var2 = i32_load((var6 + (var2 * 132)) + 68)
                                var13 = i32_load(var5 + 64)
                                if (1 if i32_load((var6 + (var2 * 132)) + 68) <= i32_load(var5 + 64) else 0):
                                    break
                                var2 = (var2 - var13)
                                if (1 if (var2 - var13) <= var16 else 0):
                                    break
                                var61 = i32_load(var5 + 28)
                                var16 = var2
                                var1 = (var1 + 1)
                                if (1 if (var1 + 1) != var4 else 0):
                                    continue
                                break  # end loop
                            if var3:
                                break
                            if (1 if var26 == i32_load(38460) else 0):
                                break
                            if (1 if var26 == i32_load(38732) else 0):
                                break
                            if (1 if var26 == i32_load(38672) else 0):
                                break
                            var45 = i32_load(((var8 + (var26 << 2)) + 284636))
                            if (1 if i32_load(((var8 + (var26 << 2)) + 284636)) == 0 else 0):
                                break
                            var46 = 0
                            if (1 if i32_load(var45 + 8) == 0 else 0):
                                break
                            while True:  # loop $label542
                                var1 = i32_load((i32_load(var45) + (var46 << 2)))
                                if (1 if i32_load((i32_load(var45) + (var46 << 2))) == 0 else 0):
                                    break
                                var29 = i32_load(9671128)
                                var18 = (i32_load(9671128) + (var1 * 132))
                                var44 = (var44 + (1 if i32_load8_u((i32_load(9671128) + (var1 * 132)) + 129) == 0 else 0))
                                if (1 if i32_load8_u(var18 + 127) == 6 else 0):
                                    break
                                if (1 if var26 != i32_load(38440) else 0):
                                    break
                                var2 = i32_load16_u(var18 + 110)
                                var5 = (i32_load(9561692) + (i32_load16_u(var18 + 110) * 286704))
                                if (1 if i32_load(var18 + 72) < i32_load(((i32_load(9561692) + (i32_load16_u(var18 + 110) * 286704)) + 284168)) else 0):
                                    break
                                var36 = i32_load16_u(var18 + 114)
                                var39 = i32_load16_u(var18 + 112)
                                var1 = i32_load(((i32_load8_u(var18 + 122) * 404) + 9568096) + 200)
                                if (1 if i32_load(((i32_load8_u(var18 + 122) * 404) + 9568096) + 200) < 0 else 0):
                                    break
                                var20 = (var36 - var1)
                                var3 = ((var1 << 1) | 1)
                                var42 = ((var36 - var1) + ((var1 << 1) | 1))
                                var13 = (var39 - var1)
                                var37 = ((var39 - var1) + var3)
                                var6 = 0
                                var24 = (i32_load(9142892) * var2)
                                var31 = i32_load(9142440)
                                var30 = (i32_load(9142440) + 2)
                                var47 = ((i32_load(9142440) + 2) << 1)
                                var41 = i32_load((var5 + 284180))
                                var2 = (i32_load((var5 + 284180)) - 3)
                                var9 = (((i32_load((var5 + 284180)) - 3) + var39) - var1)
                                var21 = ((var2 + var36) - var1)
                                var32 = i32_load(38564)
                                var33 = i32_load(38620)
                                var27 = i32_load(38560)
                                var28 = i32_load(9143004)
                                var34 = i32_load(38500)
                                var25 = i32_load(9142840)
                                while True:  # loop $label462
                                    var11 = (var13 + 1)
                                    if (1 if var13 < var31 else 0):
                                        var12 = (var13 - 3)
                                        var64 = ((var13 - 3) + var41)
                                        var7 = var21
                                        var2 = var20
                                        while True:  # loop $label461
                                            var10 = var2
                                            var2 = (var2 + 1)
                                            if (1 if var10 >= var31 else 0):
                                                break
                                            if (1 if (var10 | var13) < 0 else 0):
                                                break
                                            var14 = (var10 - 3)
                                            var65 = ((1 if var12 >= var64 else 0) | (1 if (var10 - 3) >= (var14 + var41) else 0))
                                            var5 = 1
                                            while True:  # loop $label460
                                                var1 = i32_load((var25 + ((var11 + ((var2 + (var5 * var30)) * var30)) << 2)))
                                                if (1 if i32_load((var25 + ((var11 + ((var2 + (var5 * var30)) * var30)) << 2))) < 3 else 0):
                                                    break
                                                var1 = (var29 + (var1 * 132))
                                                var3 = i32_load8_u((var29 + (var1 * 132)) + 122)
                                                if (1 if var34 == i32_load8_u((var29 + (var1 * 132)) + 122) else 0):
                                                    break
                                                var4 = i32_load16_u(var1 + 110)
                                                var15 = i32_load16_u(var1 + 120)
                                                if i32_load16_u(var1 + 120):
                                                else:
                                                if i32_load8_u(((var15 if i32_load8_u((var28 + (var4 + var24))) else var4) + (var4 + var24))):
                                                    if (1 if i32_load8_u(var1 + 128) == 0 else 0):
                                                        break
                                                    break
                                                if (1 if i32_load8_u(var1 + 127) != 6 else 0):
                                                    break
                                                if i32_load8_u(var1 + 128):
                                                    break
                                                if (1 if i32_load8_u(var1 + 125) == 10 else 0):
                                                    break
                                                if (1 if i32_load8_u(var1 + 126) == 2 else 0):
                                                    break
                                                if (1 if i32_load(var1 + 64) == -1 else 0):
                                                    break
                                                var1 = ((var3 * 404) + 9568096)
                                                if (1 if i32_load(((var3 * 404) + 9568096) + 264) == 2 else 0):
                                                    break
                                                if (1 if i32_load(var1 + 188) != 55 else 0):
                                                    break
                                                if (1 if var3 == var27 else 0):
                                                    break
                                                if (1 if var3 == var33 else 0):
                                                    break
                                                if (1 if var3 == var32 else 0):
                                                    break
                                                if (1 if i32_load(var1 + 288) == 0 else 0):
                                                    break
                                                var3 = 0
                                                var4 = var12
                                                if (1 if var65 == 0 else 0):
                                                    while True:  # loop $label459
                                                        var15 = (var4 + 1)
                                                        var1 = var14
                                                        if (1 if var4 < var31 else 0):
                                                            while True:  # loop $label458
                                                                var17 = var1
                                                                var1 = (var1 + 1)
                                                                if (1 if var17 >= var31 else 0):
                                                                    break
                                                                if (1 if (var4 | var17) < 0 else 0):
                                                                    break
                                                                var17 = i32_load((var25 + ((var15 + (var1 * var30)) << 2)))
                                                                if (1 if i32_load((var25 + ((var15 + (var1 * var30)) << 2))) <= 2 else 0):
                                                                    break
                                                                var23 = (var29 + (var17 * 132))
                                                                var22 = i32_load8_u((var29 + (var17 * 132)) + 122)
                                                                var38 = ((i32_load8_u((var29 + (var17 * 132)) + 122) * 404) + 9568096)
                                                                if (1 if i32_load(((i32_load8_u((var29 + (var17 * 132)) + 122) * 404) + 9568096) + 288) == 0 else 0):
                                                                    break
                                                                if (1 if i32_load8_u(var23 + 125) == 10 else 0):
                                                                    break
                                                                var17 = -4
                                                                if (1 if var22 == var34 else 0):
                                                                    break
                                                                var35 = i32_load16_u(var23 + 110)
                                                                var50 = i32_load16_u(var23 + 120)
                                                                if i32_load16_u(var23 + 120):
                                                                else:
                                                                if i32_load8_u(((var50 if i32_load8_u((var28 + (var24 + var35))) else var35) + (var35 + var24))):
                                                                    if (1 if i32_load8_u(var23 + 128) == 0 else 0):
                                                                        break
                                                                    break
                                                                if (1 if i32_load8_u(var23 + 127) != 6 else 0):
                                                                    break
                                                                if i32_load8_u(var23 + 128):
                                                                    break
                                                                if (1 if i32_load8_u(var23 + 126) == 2 else 0):
                                                                    break
                                                                if (1 if i32_load(var23 + 64) == -1 else 0):
                                                                    break
                                                                if (1 if i32_load(var38 + 264) == 2 else 0):
                                                                    break
                                                                if (1 if i32_load(var38 + 188) != 55 else 0):
                                                                    break
                                                                if (1 if var22 == var27 else 0):
                                                                    break
                                                                if (1 if var22 == var33 else 0):
                                                                    break
                                                                var17 = (1 if (1 if var22 != var32 else 0) else -4)
                                                                var3 = (var3 + var17)
                                                                var17 = i32_load((var25 + ((var15 + ((var1 + var30) * var30)) << 2)))
                                                                if (1 if i32_load((var25 + ((var15 + ((var1 + var30) * var30)) << 2))) < 3 else 0):
                                                                    break
                                                                var23 = (var29 + (var17 * 132))
                                                                var22 = i32_load8_u((var29 + (var17 * 132)) + 122)
                                                                var38 = ((i32_load8_u((var29 + (var17 * 132)) + 122) * 404) + 9568096)
                                                                if (1 if i32_load(((i32_load8_u((var29 + (var17 * 132)) + 122) * 404) + 9568096) + 288) == 0 else 0):
                                                                    break
                                                                if (1 if i32_load8_u(var23 + 125) == 10 else 0):
                                                                    break
                                                                var17 = -4
                                                                if (1 if var22 == var34 else 0):
                                                                    break
                                                                var35 = i32_load16_u(var23 + 110)
                                                                var50 = i32_load16_u(var23 + 120)
                                                                if i32_load16_u(var23 + 120):
                                                                else:
                                                                if i32_load8_u(((var50 if i32_load8_u((var28 + (var24 + var35))) else var35) + (var35 + var24))):
                                                                    if (1 if i32_load8_u(var23 + 128) == 0 else 0):
                                                                        break
                                                                    break
                                                                if (1 if i32_load8_u(var23 + 127) != 6 else 0):
                                                                    break
                                                                if i32_load8_u(var23 + 128):
                                                                    break
                                                                if (1 if i32_load8_u(var23 + 126) == 2 else 0):
                                                                    break
                                                                if (1 if i32_load(var23 + 64) == -1 else 0):
                                                                    break
                                                                if (1 if i32_load(var38 + 264) == 2 else 0):
                                                                    break
                                                                if (1 if i32_load(var38 + 188) != 55 else 0):
                                                                    break
                                                                if (1 if var22 == var27 else 0):
                                                                    break
                                                                if (1 if var22 == var33 else 0):
                                                                    break
                                                                var17 = (1 if (1 if var22 != var32 else 0) else -4)
                                                                var3 = (var3 + var17)
                                                                var17 = i32_load((var25 + ((var15 + ((var1 + var47) * var30)) << 2)))
                                                                if (1 if i32_load((var25 + ((var15 + ((var1 + var47) * var30)) << 2))) < 3 else 0):
                                                                    break
                                                                var23 = (var29 + (var17 * 132))
                                                                var22 = i32_load8_u((var29 + (var17 * 132)) + 122)
                                                                var38 = ((i32_load8_u((var29 + (var17 * 132)) + 122) * 404) + 9568096)
                                                                if (1 if i32_load(((i32_load8_u((var29 + (var17 * 132)) + 122) * 404) + 9568096) + 288) == 0 else 0):
                                                                    break
                                                                if (1 if i32_load8_u(var23 + 125) == 10 else 0):
                                                                    break
                                                                var17 = -4
                                                                if (1 if var22 == var34 else 0):
                                                                    break
                                                                var35 = i32_load16_u(var23 + 110)
                                                                var50 = i32_load16_u(var23 + 120)
                                                                if i32_load16_u(var23 + 120):
                                                                else:
                                                                if i32_load8_u(((var50 if i32_load8_u((var28 + (var24 + var35))) else var35) + (var35 + var24))):
                                                                    if (1 if i32_load8_u(var23 + 128) == 0 else 0):
                                                                        break
                                                                    break
                                                                if (1 if i32_load8_u(var23 + 127) != 6 else 0):
                                                                    break
                                                                if i32_load8_u(var23 + 128):
                                                                    break
                                                                if (1 if i32_load8_u(var23 + 126) == 2 else 0):
                                                                    break
                                                                if (1 if i32_load(var23 + 64) == -1 else 0):
                                                                    break
                                                                if (1 if i32_load(var38 + 264) == 2 else 0):
                                                                    break
                                                                if (1 if i32_load(var38 + 188) != 55 else 0):
                                                                    break
                                                                if (1 if var22 == var27 else 0):
                                                                    break
                                                                if (1 if var22 == var33 else 0):
                                                                    break
                                                                var17 = (1 if (1 if var22 != var32 else 0) else -4)
                                                                var3 = (var3 + var17)
                                                                if (1 if var1 != var7 else 0):
                                                                    continue
                                                                break  # end loop
                                                        var4 = var15
                                                        if (1 if var15 != var9 else 0):
                                                            continue
                                                        break  # end loop
                                                var1 = (1 if var3 > var6 else 0)
                                                var54 = (var13 if (1 if var3 > var6 else 0) else var54)
                                                var55 = (var10 if var1 else var55)
                                                var6 = (var3 if var1 else var6)
                                                var5 = (var5 + 1)
                                                if (1 if (var5 + 1) != 3 else 0):
                                                    continue
                                                break  # end loop
                                            var7 = (var7 + 1)
                                            if (1 if var2 < var42 else 0):
                                                continue
                                            break  # end loop
                                    var9 = (var9 + 1)
                                    var13 = var11
                                    if (1 if var11 < var37 else 0):
                                        continue
                                    break  # end loop
                                if (1 if var6 == 0 else 0):
                                    break
                                break
                                if (1 if i32_load8_u(var18 + 123) != 14 else 0):
                                    break
                                i32_store16(var18 + 118, var36)
                                i32_store16(var18 + 116, var39)
                                i32_store(var18 + 32, 0)
                                i32_store8(var18 + 123, 0)
                                break
                                if (1 if var26 != i32_load(38772) else 0):
                                    break
                                var5 = i32_load16_u(var18 + 110)
                                if (1 if i32_load(var18 + 72) < i32_load(((i32_load(9561692) + (i32_load16_u(var18 + 110) * 286704)) + 284252)) else 0):
                                    break
                                var22 = i32_load16_u(var18 + 114)
                                var36 = i32_load16_u(var18 + 112)
                                var1 = i32_load(((i32_load8_u(var18 + 122) * 404) + 9568096) + 200)
                                if (1 if i32_load(((i32_load8_u(var18 + 122) * 404) + 9568096) + 200) < 0 else 0):
                                    break
                                var9 = (var22 - var1)
                                var3 = ((var1 << 1) | 1)
                                var39 = ((var22 - var1) + ((var1 << 1) | 1))
                                var2 = (var36 - var1)
                                var35 = (var3 + (var36 - var1))
                                var28 = 0
                                var14 = (i32_load(9142892) * var5)
                                var23 = i32_load(9142440)
                                var21 = (i32_load(9142440) + 2)
                                var41 = ((i32_load(9142440) + 2) << 1)
                                var34 = i32_load(9147132)
                                var30 = i32_load(38564)
                                var31 = i32_load(38620)
                                var32 = i32_load(38560)
                                var20 = i32_load(9143004)
                                var33 = i32_load(38500)
                                var27 = i32_load(9142840)
                                while True:  # loop $label482
                                    var10 = (var2 + 1)
                                    if (1 if var2 < var23 else 0):
                                        var15 = (var2 - 3)
                                        var38 = (var2 + 3)
                                        var3 = var9
                                        while True:  # loop $label481
                                            var7 = var3
                                            var3 = (var3 + 1)
                                            if (1 if var7 >= var23 else 0):
                                                break
                                            if (1 if (var2 | var7) < 0 else 0):
                                                break
                                            var42 = (var7 + 4)
                                            var11 = (var7 - 3)
                                            var17 = 1
                                            while True:  # loop $label480
                                                var1 = i32_load((var27 + ((var10 + ((var3 + (var17 * var21)) * var21)) << 2)))
                                                if (1 if i32_load((var27 + ((var10 + ((var3 + (var17 * var21)) * var21)) << 2))) < 3 else 0):
                                                    break
                                                var1 = (var29 + (var1 * 132))
                                                var6 = i32_load8_u((var29 + (var1 * 132)) + 122)
                                                if (1 if var33 == i32_load8_u((var29 + (var1 * 132)) + 122) else 0):
                                                    break
                                                var5 = i32_load16_u(var1 + 110)
                                                var4 = i32_load16_u(var1 + 120)
                                                if i32_load16_u(var1 + 120):
                                                else:
                                                if i32_load8_u(((var4 if i32_load8_u((var20 + (var5 + var14))) else var5) + (var5 + var14))):
                                                    if (1 if i32_load8_u(var1 + 128) == 0 else 0):
                                                        break
                                                    break
                                                if (1 if i32_load8_u(var1 + 127) != 6 else 0):
                                                    break
                                                if i32_load8_u(var1 + 128):
                                                    break
                                                if (1 if i32_load8_u(var1 + 125) == 10 else 0):
                                                    break
                                                if (1 if i32_load8_u(var1 + 126) == 2 else 0):
                                                    break
                                                if (1 if i32_load(var1 + 64) == -1 else 0):
                                                    break
                                                var1 = ((var6 * 404) + 9568096)
                                                if (1 if i32_load(((var6 * 404) + 9568096) + 264) == 2 else 0):
                                                    break
                                                if (1 if i32_load(var1 + 188) != 55 else 0):
                                                    break
                                                if (1 if var6 == var32 else 0):
                                                    break
                                                if (1 if var6 == var31 else 0):
                                                    break
                                                var5 = 0
                                                var4 = var15
                                                if (1 if var6 == var30 else 0):
                                                    break
                                                while True:  # loop $label479
                                                    var13 = (var4 + 1)
                                                    var1 = var11
                                                    if (1 if var4 < var23 else 0):
                                                        while True:  # loop $label478
                                                            var6 = var1
                                                            var1 = (var1 + 1)
                                                            if (1 if var6 >= var23 else 0):
                                                                break
                                                            if (1 if (var4 | var6) < 0 else 0):
                                                                break
                                                            var12 = i32_load((var27 + ((var13 + (var1 * var21)) << 2)))
                                                            if (1 if i32_load((var27 + ((var13 + (var1 * var21)) << 2))) > 2 else 0):
                                                                var6 = -4
                                                                var12 = (var29 + (var12 * 132))
                                                                var24 = i32_load8_u((var29 + (var12 * 132)) + 122)
                                                                if (1 if var33 == i32_load8_u((var29 + (var12 * 132)) + 122) else 0):
                                                                    break
                                                                var25 = i32_load16_u(var12 + 110)
                                                                var37 = i32_load16_u(var12 + 120)
                                                                if i32_load16_u(var12 + 120):
                                                                else:
                                                                if i32_load8_u(((var37 if i32_load8_u((var20 + (var14 + var25))) else var25) + (var25 + var14))):
                                                                    if (1 if i32_load8_u(var12 + 128) == 0 else 0):
                                                                        break
                                                                    break
                                                                if (1 if i32_load8_u(var12 + 127) != 6 else 0):
                                                                    break
                                                                if i32_load8_u(var12 + 128):
                                                                    break
                                                                if (1 if i32_load8_u(var12 + 125) == 10 else 0):
                                                                    break
                                                                if (1 if i32_load8_u(var12 + 126) == 2 else 0):
                                                                    break
                                                                if (1 if i32_load(var12 + 64) == -1 else 0):
                                                                    break
                                                                var25 = ((var24 * 404) + 9568096)
                                                                if (1 if i32_load(((var24 * 404) + 9568096) + 264) == 2 else 0):
                                                                    break
                                                                if (1 if i32_load(var25 + 188) != 55 else 0):
                                                                    break
                                                                if (1 if var24 == var32 else 0):
                                                                    break
                                                                if (1 if var24 == var31 else 0):
                                                                    break
                                                                var6 = (1 if (1 if var24 != var30 else 0) else -4)
                                                                if var34:
                                                                    break
                                                                var25 = i32_load(var12 + 64)
                                                                if (1 if i32_load(((var24 * 404) + 9568096) + 264) != 1 else 0):
                                                                    break
                                                                var5 = ((i32_load(var12 + 52) + var25) + (((var25 & 0xFFFFFFFF) // 800) * var6))
                                                            var12 = i32_load((var27 + ((var13 + ((var1 + var21) * var21)) << 2)))
                                                            if (1 if i32_load((var27 + ((var13 + ((var1 + var21) * var21)) << 2))) >= 3 else 0):
                                                                var6 = -4
                                                                var12 = (var29 + (var12 * 132))
                                                                var24 = i32_load8_u((var29 + (var12 * 132)) + 122)
                                                                if (1 if var33 == i32_load8_u((var29 + (var12 * 132)) + 122) else 0):
                                                                    break
                                                                var25 = i32_load16_u(var12 + 110)
                                                                var37 = i32_load16_u(var12 + 120)
                                                                if i32_load16_u(var12 + 120):
                                                                else:
                                                                if i32_load8_u(((var37 if i32_load8_u((var20 + (var14 + var25))) else var25) + (var25 + var14))):
                                                                    if (1 if i32_load8_u(var12 + 128) == 0 else 0):
                                                                        break
                                                                    break
                                                                if (1 if i32_load8_u(var12 + 127) != 6 else 0):
                                                                    break
                                                                if i32_load8_u(var12 + 128):
                                                                    break
                                                                if (1 if i32_load8_u(var12 + 125) == 10 else 0):
                                                                    break
                                                                if (1 if i32_load8_u(var12 + 126) == 2 else 0):
                                                                    break
                                                                if (1 if i32_load(var12 + 64) == -1 else 0):
                                                                    break
                                                                var25 = ((var24 * 404) + 9568096)
                                                                if (1 if i32_load(((var24 * 404) + 9568096) + 264) == 2 else 0):
                                                                    break
                                                                if (1 if i32_load(var25 + 188) != 55 else 0):
                                                                    break
                                                                if (1 if var24 == var32 else 0):
                                                                    break
                                                                if (1 if var24 == var31 else 0):
                                                                    break
                                                                var6 = (1 if (1 if var24 != var30 else 0) else -4)
                                                                if var34:
                                                                    break
                                                                var25 = i32_load(var12 + 64)
                                                                if (1 if i32_load(((var24 * 404) + 9568096) + 264) != 1 else 0):
                                                                    break
                                                                var5 = ((i32_load(var12 + 52) + var25) + (((var25 & 0xFFFFFFFF) // 800) * var6))
                                                            var12 = i32_load((var27 + ((var13 + ((var1 + var41) * var21)) << 2)))
                                                            if (1 if i32_load((var27 + ((var13 + ((var1 + var41) * var21)) << 2))) < 3 else 0):
                                                                break
                                                            var6 = -4
                                                            var12 = (var29 + (var12 * 132))
                                                            var24 = i32_load8_u((var29 + (var12 * 132)) + 122)
                                                            if (1 if var33 == i32_load8_u((var29 + (var12 * 132)) + 122) else 0):
                                                                break
                                                            var25 = i32_load16_u(var12 + 110)
                                                            var37 = i32_load16_u(var12 + 120)
                                                            if i32_load16_u(var12 + 120):
                                                            else:
                                                            if i32_load8_u(((var37 if i32_load8_u((var20 + (var14 + var25))) else var25) + (var25 + var14))):
                                                                if (1 if i32_load8_u(var12 + 128) == 0 else 0):
                                                                    break
                                                                break
                                                            if (1 if i32_load8_u(var12 + 127) != 6 else 0):
                                                                break
                                                            if i32_load8_u(var12 + 128):
                                                                break
                                                            if (1 if i32_load8_u(var12 + 125) == 10 else 0):
                                                                break
                                                            if (1 if i32_load8_u(var12 + 126) == 2 else 0):
                                                                break
                                                            if (1 if i32_load(var12 + 64) == -1 else 0):
                                                                break
                                                            var25 = ((var24 * 404) + 9568096)
                                                            if (1 if i32_load(((var24 * 404) + 9568096) + 264) == 2 else 0):
                                                                break
                                                            if (1 if i32_load(var25 + 188) != 55 else 0):
                                                                break
                                                            if (1 if var24 == var32 else 0):
                                                                break
                                                            if (1 if var24 == var31 else 0):
                                                                break
                                                            var6 = (1 if (1 if var24 != var30 else 0) else -4)
                                                            if var34:
                                                                break
                                                            var25 = i32_load(var12 + 64)
                                                            if (1 if i32_load(((var24 * 404) + 9568096) + 264) != 1 else 0):
                                                                break
                                                            var5 = ((i32_load(var12 + 52) + var25) + (((var25 & 0xFFFFFFFF) // 800) * var6))
                                                            if (1 if var1 < var42 else 0):
                                                                continue
                                                            break  # end loop
                                                    var1 = (1 if var4 < var38 else 0)
                                                    var4 = var13
                                                    if var1:
                                                        continue
                                                    break  # end loop
                                                var1 = (1 if var5 > var28 else 0)
                                                var56 = (var2 if (1 if var5 > var28 else 0) else var56)
                                                var57 = (var7 if var1 else var57)
                                                var28 = (var5 if var1 else var28)
                                                var17 = (var17 + 1)
                                                if (1 if (var17 + 1) != 3 else 0):
                                                    continue
                                                break  # end loop
                                            if (1 if var3 < var39 else 0):
                                                continue
                                            break  # end loop
                                    var2 = var10
                                    if (1 if var10 < var35 else 0):
                                        continue
                                    break  # end loop
                                if (1 if var28 < 191 else 0):
                                    break
                                break
                                if (1 if i32_load8_u(var18 + 123) != 26 else 0):
                                    break
                                i32_store16(var18 + 118, var22)
                                i32_store16(var18 + 116, var36)
                                i32_store(var18 + 32, 0)
                                i32_store8(var18 + 123, 0)
                                break
                                if (1 if var26 != i32_load(38928) else 0):
                                    break
                                var1 = i32_load(var18 + 72)
                                var2 = i32_load16_u(var18 + 110)
                                var5 = (i32_load(9561692) + (i32_load16_u(var18 + 110) * 286704))
                                if (1 if i32_load(var18 + 72) >= i32_load(((i32_load(9561692) + (i32_load16_u(var18 + 110) * 286704)) + 284280)) else 0):
                                    var36 = i32_load16_u(var18 + 114)
                                    var39 = i32_load16_u(var18 + 112)
                                    var1 = i32_load(((i32_load8_u(var18 + 122) * 404) + 9568096) + 200)
                                    if (1 if i32_load(((i32_load8_u(var18 + 122) * 404) + 9568096) + 200) < 0 else 0):
                                        break
                                    var15 = (var36 - var1)
                                    var3 = ((var1 << 1) | 1)
                                    var35 = ((var36 - var1) + ((var1 << 1) | 1))
                                    var13 = (var39 - var1)
                                    var41 = ((var39 - var1) + var3)
                                    var34 = i32_load((var5 + 284272))
                                    var24 = 0
                                    var17 = (i32_load(9142892) * var2)
                                    var28 = i32_load(9142440)
                                    var21 = (i32_load(9142440) + 2)
                                    var38 = ((i32_load(9142440) + 2) << 1)
                                    var25 = i32_load(9147132)
                                    var23 = i32_load(38564)
                                    var30 = i32_load(38620)
                                    var31 = i32_load(38560)
                                    var20 = i32_load(9143004)
                                    var32 = i32_load(38500)
                                    var33 = i32_load(9142840)
                                    while True:  # loop $label499
                                        var9 = (var13 + 1)
                                        if (1 if var13 < var28 else 0):
                                            var11 = (var13 - 2)
                                            var42 = ((var13 - 2) + var34)
                                            var6 = var15
                                            while True:  # loop $label498
                                                var4 = var6
                                                var6 = (var6 + 1)
                                                if (1 if var4 >= var28 else 0):
                                                    break
                                                if (1 if (var4 | var13) < 0 else 0):
                                                    break
                                                var12 = (var4 - 2)
                                                var37 = ((var4 - 2) + var34)
                                                var10 = 1
                                                while True:  # loop $label497
                                                    var1 = i32_load((var33 + ((var9 + ((var6 + (var10 * var21)) * var21)) << 2)))
                                                    if (1 if i32_load((var33 + ((var9 + ((var6 + (var10 * var21)) * var21)) << 2))) < 3 else 0):
                                                        break
                                                    var1 = (var29 + (var1 * 132))
                                                    var2 = i32_load8_u((var29 + (var1 * 132)) + 122)
                                                    if (1 if var32 == i32_load8_u((var29 + (var1 * 132)) + 122) else 0):
                                                        break
                                                    var5 = i32_load16_u(var1 + 110)
                                                    var3 = i32_load16_u(var1 + 120)
                                                    if i32_load16_u(var1 + 120):
                                                    else:
                                                    if i32_load8_u(((var3 if i32_load8_u((var20 + (var5 + var17))) else var5) + (var5 + var17))):
                                                        if (1 if i32_load8_u(var1 + 128) == 0 else 0):
                                                            break
                                                        break
                                                    if (1 if i32_load8_u(var1 + 127) != 6 else 0):
                                                        break
                                                    if i32_load8_u(var1 + 128):
                                                        break
                                                    var5 = i32_load8_u(var1 + 125)
                                                    if (1 if i32_load8_u(var1 + 125) == 10 else 0):
                                                        break
                                                    if (1 if i32_load8_u(var1 + 126) == 2 else 0):
                                                        break
                                                    if (1 if i32_load(var1 + 64) == -1 else 0):
                                                        break
                                                    var1 = ((var2 * 404) + 9568096)
                                                    if (1 if i32_load(((var2 * 404) + 9568096) + 264) == 2 else 0):
                                                        break
                                                    if (1 if i32_load(var1 + 188) != 55 else 0):
                                                        break
                                                    if (1 if var2 == var31 else 0):
                                                        break
                                                    if (1 if var2 == var30 else 0):
                                                        break
                                                    if (1 if var2 == var23 else 0):
                                                        break
                                                    if (1 if i32_load(var1 + 344) == 0 else 0):
                                                        break
                                                    if (1 if ((var5 - 11) & 255) > 253 else 0):
                                                        break
                                                    var5 = 0
                                                    var3 = var11
                                                    if (1 if var34 > 0 else 0):
                                                        while True:  # loop $label496
                                                            var7 = (var3 + 1)
                                                            var1 = var12
                                                            if (1 if var3 < var28 else 0):
                                                                while True:  # loop $label495
                                                                    var2 = var1
                                                                    var1 = (var1 + 1)
                                                                    if (1 if var2 >= var28 else 0):
                                                                        break
                                                                    if (1 if (var2 | var3) < 0 else 0):
                                                                        break
                                                                    var14 = i32_load((var33 + ((var7 + (var1 * var21)) << 2)))
                                                                    if (1 if i32_load((var33 + ((var7 + (var1 * var21)) << 2))) > 2 else 0):
                                                                        var2 = 0
                                                                        var14 = (var29 + (var14 * 132))
                                                                        if (1 if i32_load8_u((var29 + (var14 * 132)) + 127) == 6 else 0):
                                                                            break
                                                                        var2 = -4
                                                                        var27 = i32_load8_u(var14 + 122)
                                                                        if (1 if var32 == i32_load8_u(var14 + 122) else 0):
                                                                            break
                                                                        var22 = i32_load16_u(var14 + 110)
                                                                        var47 = i32_load16_u(var14 + 120)
                                                                        if i32_load16_u(var14 + 120):
                                                                        else:
                                                                        if (1 if i32_load8_u(((var47 if i32_load8_u((var20 + (var17 + var22))) else var22) + (var22 + var17))) == 0 else 0):
                                                                            break
                                                                        if i32_load8_u(var14 + 128):
                                                                            break
                                                                        if (1 if i32_load8_u(var14 + 125) == 10 else 0):
                                                                            break
                                                                        if (1 if i32_load8_u(var14 + 126) == 2 else 0):
                                                                            break
                                                                        if (1 if i32_load(var14 + 64) == -1 else 0):
                                                                            break
                                                                        var22 = ((var27 * 404) + 9568096)
                                                                        if (1 if i32_load(((var27 * 404) + 9568096) + 264) == 2 else 0):
                                                                            break
                                                                        if (1 if i32_load(var22 + 188) != 55 else 0):
                                                                            break
                                                                        if (1 if var27 == var31 else 0):
                                                                            break
                                                                        if (1 if var27 == var30 else 0):
                                                                            break
                                                                        var2 = (1 if (1 if var23 != var27 else 0) else -4)
                                                                        if var25:
                                                                            break
                                                                        var27 = i32_load(var14 + 64)
                                                                        if (1 if i32_load(((i32_load8_u(var14 + 122) * 404) + 9568096) + 264) != 1 else 0):
                                                                            break
                                                                        var5 = ((i32_load(var14 + 52) + var27) + (((var27 & 0xFFFFFFFF) // 800) * var2))
                                                                    var14 = i32_load((var33 + ((var7 + ((var1 + var21) * var21)) << 2)))
                                                                    if (1 if i32_load((var33 + ((var7 + ((var1 + var21) * var21)) << 2))) >= 3 else 0):
                                                                        var2 = 0
                                                                        var14 = (var29 + (var14 * 132))
                                                                        if (1 if i32_load8_u((var29 + (var14 * 132)) + 127) == 6 else 0):
                                                                            break
                                                                        var2 = -4
                                                                        var27 = i32_load8_u(var14 + 122)
                                                                        if (1 if var32 == i32_load8_u(var14 + 122) else 0):
                                                                            break
                                                                        var22 = i32_load16_u(var14 + 110)
                                                                        var47 = i32_load16_u(var14 + 120)
                                                                        if i32_load16_u(var14 + 120):
                                                                        else:
                                                                        if (1 if i32_load8_u(((var47 if i32_load8_u((var20 + (var17 + var22))) else var22) + (var22 + var17))) == 0 else 0):
                                                                            break
                                                                        if i32_load8_u(var14 + 128):
                                                                            break
                                                                        if (1 if i32_load8_u(var14 + 125) == 10 else 0):
                                                                            break
                                                                        if (1 if i32_load8_u(var14 + 126) == 2 else 0):
                                                                            break
                                                                        if (1 if i32_load(var14 + 64) == -1 else 0):
                                                                            break
                                                                        var22 = ((var27 * 404) + 9568096)
                                                                        if (1 if i32_load(((var27 * 404) + 9568096) + 264) == 2 else 0):
                                                                            break
                                                                        if (1 if i32_load(var22 + 188) != 55 else 0):
                                                                            break
                                                                        if (1 if var27 == var31 else 0):
                                                                            break
                                                                        if (1 if var27 == var30 else 0):
                                                                            break
                                                                        var2 = (1 if (1 if var23 != var27 else 0) else -4)
                                                                        if var25:
                                                                            break
                                                                        var27 = i32_load(var14 + 64)
                                                                        if (1 if i32_load(((i32_load8_u(var14 + 122) * 404) + 9568096) + 264) != 1 else 0):
                                                                            break
                                                                        var5 = ((i32_load(var14 + 52) + var27) + (((var27 & 0xFFFFFFFF) // 800) * var2))
                                                                    var14 = i32_load((var33 + ((var7 + ((var1 + var38) * var21)) << 2)))
                                                                    if (1 if i32_load((var33 + ((var7 + ((var1 + var38) * var21)) << 2))) < 3 else 0):
                                                                        break
                                                                    var2 = 0
                                                                    var14 = (var29 + (var14 * 132))
                                                                    if (1 if i32_load8_u((var29 + (var14 * 132)) + 127) == 6 else 0):
                                                                        break
                                                                    var2 = -4
                                                                    var27 = i32_load8_u(var14 + 122)
                                                                    if (1 if var32 == i32_load8_u(var14 + 122) else 0):
                                                                        break
                                                                    var22 = i32_load16_u(var14 + 110)
                                                                    var47 = i32_load16_u(var14 + 120)
                                                                    if i32_load16_u(var14 + 120):
                                                                    else:
                                                                    if (1 if i32_load8_u(((var47 if i32_load8_u((var20 + (var17 + var22))) else var22) + (var22 + var17))) == 0 else 0):
                                                                        break
                                                                    if i32_load8_u(var14 + 128):
                                                                        break
                                                                    if (1 if i32_load8_u(var14 + 125) == 10 else 0):
                                                                        break
                                                                    if (1 if i32_load8_u(var14 + 126) == 2 else 0):
                                                                        break
                                                                    if (1 if i32_load(var14 + 64) == -1 else 0):
                                                                        break
                                                                    var22 = ((var27 * 404) + 9568096)
                                                                    if (1 if i32_load(((var27 * 404) + 9568096) + 264) == 2 else 0):
                                                                        break
                                                                    if (1 if i32_load(var22 + 188) != 55 else 0):
                                                                        break
                                                                    if (1 if var27 == var31 else 0):
                                                                        break
                                                                    if (1 if var27 == var30 else 0):
                                                                        break
                                                                    var2 = (1 if (1 if var23 != var27 else 0) else -4)
                                                                    if var25:
                                                                        break
                                                                    var27 = i32_load(var14 + 64)
                                                                    if (1 if i32_load(((i32_load8_u(var14 + 122) * 404) + 9568096) + 264) != 1 else 0):
                                                                        break
                                                                    var5 = ((i32_load(var14 + 52) + var27) + (((var27 & 0xFFFFFFFF) // 800) * var2))
                                                                    if (1 if var1 < var37 else 0):
                                                                        continue
                                                                    break  # end loop
                                                            var3 = var7
                                                            if (1 if var7 < var42 else 0):
                                                                continue
                                                            break  # end loop
                                                    var1 = (1 if var5 > var24 else 0)
                                                    var24 = (var5 if (1 if var5 > var24 else 0) else var24)
                                                    var58 = (var4 if var1 else var58)
                                                    var59 = (var13 if var1 else var59)
                                                    var10 = (var10 + 1)
                                                    if (1 if (var10 + 1) != 3 else 0):
                                                        continue
                                                    break  # end loop
                                                if (1 if var6 < var35 else 0):
                                                    continue
                                                break  # end loop
                                        var13 = var9
                                        if (1 if var9 < var41 else 0):
                                            continue
                                        break  # end loop
                                    if (1 if var24 == 0 else 0):
                                        break
                                    break
                                    if (1 if i32_load8_u(var18 + 123) != 39 else 0):
                                        break
                                    i32_store16(var18 + 118, var36)
                                    i32_store16(var18 + 116, var39)
                                    i32_store(var18 + 32, 0)
                                    i32_store8(var18 + 123, 0)
                                    break
                                if (1 if var1 < i32_load((var5 + 284284)) else 0):
                                    break
                                var11 = i32_load16_u(var18 + 114)
                                var12 = i32_load16_u(var18 + 112)
                                var1 = i32_load(((i32_load8_u(var18 + 122) * 404) + 9568096) + 200)
                                if (1 if i32_load(((i32_load8_u(var18 + 122) * 404) + 9568096) + 200) < 0 else 0):
                                    break
                                var3 = (var11 - var1)
                                var5 = ((var1 << 1) | 1)
                                var33 = ((var11 - var1) + ((var1 << 1) | 1))
                                var7 = (var12 - var1)
                                var27 = ((var12 - var1) + var5)
                                var13 = 0
                                var10 = (i32_load(9142892) * var2)
                                var20 = i32_load(9142440)
                                var14 = (i32_load(9142440) + 2)
                                var34 = ((i32_load(9142440) + 2) << 1)
                                var21 = i32_load(38456)
                                var24 = i32_load(38764)
                                var28 = i32_load(38564)
                                var23 = i32_load(38620)
                                var30 = i32_load(38560)
                                var9 = i32_load(9143004)
                                var31 = i32_load(38500)
                                var32 = i32_load(9142840)
                                var4 = 0
                                while True:  # loop $label505
                                    var2 = (var7 + 1)
                                    if (1 if var7 < var20 else 0):
                                        var1 = (var7 - var12)
                                        var25 = ((var7 - var12) * var1)
                                        var1 = var3
                                        while True:  # loop $label504
                                            var5 = var1
                                            var1 = (var1 + 1)
                                            if (1 if var5 >= var20 else 0):
                                                break
                                            if (1 if (var5 | var7) < 0 else 0):
                                                break
                                            var5 = (var5 - var11)
                                            var15 = (((var5 - var11) * var5) + var25)
                                            var5 = i32_load((var32 + ((var2 + ((var1 + var14) * var14)) << 2)))
                                            if (1 if i32_load((var32 + ((var2 + ((var1 + var14) * var14)) << 2))) <= 2 else 0):
                                                break
                                            var5 = (var29 + (var5 * 132))
                                            var6 = i32_load8_u((var29 + (var5 * 132)) + 122)
                                            if (1 if var31 == i32_load8_u((var29 + (var5 * 132)) + 122) else 0):
                                                break
                                            var17 = i32_load16_u(var5 + 110)
                                            var22 = i32_load16_u(var5 + 120)
                                            if i32_load16_u(var5 + 120):
                                            else:
                                            if i32_load8_u(((var22 if i32_load8_u((var9 + (var10 + var17))) else var17) + (var17 + var10))):
                                                if (1 if i32_load8_u(var5 + 128) == 0 else 0):
                                                    break
                                                break
                                            if (1 if i32_load8_u(var5 + 127) != 6 else 0):
                                                break
                                            if i32_load8_u(var5 + 128):
                                                break
                                            if (1 if i32_load8_u(var5 + 125) == 10 else 0):
                                                break
                                            if (1 if i32_load8_u(var5 + 126) == 2 else 0):
                                                break
                                            if (1 if i32_load(var5 + 64) == -1 else 0):
                                                break
                                            var17 = ((var6 * 404) + 9568096)
                                            if (1 if i32_load(((var6 * 404) + 9568096) + 264) == 2 else 0):
                                                break
                                            if (1 if i32_load(var17 + 188) != 55 else 0):
                                                break
                                            if (1 if var6 == var30 else 0):
                                                break
                                            if (1 if var6 == var23 else 0):
                                                break
                                            if (1 if var6 == var28 else 0):
                                                break
                                            if (1 if i32_load(var17 + 340) == 0 else 0):
                                                break
                                            if ((1 if var6 != var24 else 0) & (1 if var6 != var21 else 0)):
                                                break
                                            var5 = (1 if var13 > var15 else 0)
                                            var4 = (i32_load(var5 + 28) if (1 if var13 > var15 else 0) else var4)
                                            var13 = (var15 if var5 else var13)
                                            var5 = i32_load((var32 + ((var2 + ((var1 + var34) * var14)) << 2)))
                                            if (1 if i32_load((var32 + ((var2 + ((var1 + var34) * var14)) << 2))) < 3 else 0):
                                                break
                                            var5 = (var29 + (var5 * 132))
                                            var6 = i32_load8_u((var29 + (var5 * 132)) + 122)
                                            if (1 if var31 == i32_load8_u((var29 + (var5 * 132)) + 122) else 0):
                                                break
                                            var17 = i32_load16_u(var5 + 110)
                                            var22 = i32_load16_u(var5 + 120)
                                            if i32_load16_u(var5 + 120):
                                            else:
                                            if (1 if i32_load8_u(((var22 if i32_load8_u((var9 + (var10 + var17))) else var17) + (var17 + var10))) == 0 else 0):
                                                if (1 if i32_load8_u(var5 + 127) != 6 else 0):
                                                    break
                                            if i32_load8_u(var5 + 128):
                                                break
                                            if (1 if i32_load8_u(var5 + 125) == 10 else 0):
                                                break
                                            if (1 if i32_load8_u(var5 + 126) == 2 else 0):
                                                break
                                            if (1 if i32_load(var5 + 64) == -1 else 0):
                                                break
                                            var17 = ((var6 * 404) + 9568096)
                                            if (1 if i32_load(((var6 * 404) + 9568096) + 264) == 2 else 0):
                                                break
                                            if (1 if i32_load(var17 + 188) != 55 else 0):
                                                break
                                            if (1 if var6 == var30 else 0):
                                                break
                                            if (1 if var6 == var23 else 0):
                                                break
                                            if (1 if var6 == var28 else 0):
                                                break
                                            if (1 if i32_load(var17 + 340) == 0 else 0):
                                                break
                                            if ((1 if var6 != var24 else 0) & (1 if var6 != var21 else 0)):
                                                break
                                            var5 = (1 if var13 > var15 else 0)
                                            var4 = (i32_load(var5 + 28) if (1 if var13 > var15 else 0) else var4)
                                            var13 = (var15 if var5 else var13)
                                            if (1 if var1 < var33 else 0):
                                                continue
                                            break  # end loop
                                    var7 = var2
                                    if (1 if var2 < var27 else 0):
                                        continue
                                    break  # end loop
                                if (1 if var13 == 0 else 0):
                                    break
                                break
                                if (1 if i32_load8_u(var18 + 123) != 40 else 0):
                                    break
                                i32_store16(var18 + 118, var11)
                                i32_store16(var18 + 116, var12)
                                i32_store(var18 + 32, 0)
                                i32_store8(var18 + 123, 0)
                                break
                                if (1 if i32_load(38456) != var26 else 0):
                                    if (1 if var26 != i32_load(38764) else 0):
                                        break
                                var23 = i32_load(9215884)
                                var1 = i32_load(var18 + 44)
                                var2 = i32_load((i32_load(9215884) + (i32_load(var18 + 44) << 4)) + 4)
                                if (1 if ((1 if i32_load((i32_load(9215884) + (i32_load(var18 + 44) << 4)) + 4) == 22 else 0) | (1 if var1 == 0 else 0)) == 0 else 0):
                                    break
                                if i32_load8_u(var18 + 125):
                                    break
                                if (1 if i32_load(var18 + 36) == 0 else 0):
                                    break
                                if (1 if var2 == 69 else 0):
                                    break
                                if (1 if i32_load8_u(var18 + 123) != 69 else 0):
                                    break
                                var5 = i32_load16_u(var18 + 110)
                                var3 = (i32_load(9561692) + (i32_load16_u(var18 + 110) * 286704))
                                if (1 if i32_load(var18 + 72) < i32_load(((i32_load(9561692) + (i32_load16_u(var18 + 110) * 286704)) + 284148)) else 0):
                                    break
                                var1 = i32_load(((i32_load8_u(var18 + 122) * 404) + 9568096) + 200)
                                if (1 if i32_load(((i32_load8_u(var18 + 122) * 404) + 9568096) + 200) < 0 else 0):
                                    break
                                var2 = (i32_load16_u(var18 + 114) - var1)
                                var4 = ((var1 << 1) | 1)
                                var36 = ((i32_load16_u(var18 + 114) - var1) + ((var1 << 1) | 1))
                                var13 = (i32_load16_u(var18 + 112) - var1)
                                var41 = ((i32_load16_u(var18 + 112) - var1) + var4)
                                var30 = i32_load((var3 + 284140))
                                var39 = ((i32_load((var3 + 284140)) & 0xFFFFFFFF) >> 1)
                                var17 = 0
                                var20 = (i32_load(9142892) * var5)
                                var28 = i32_load(9142440)
                                var14 = (i32_load(9142440) + 2)
                                var35 = ((i32_load(9142440) + 2) << 1)
                                var31 = i32_load(38564)
                                var32 = i32_load(38620)
                                var33 = i32_load(38560)
                                var21 = i32_load(9143004)
                                var27 = i32_load(38500)
                                var24 = i32_load(9142840)
                                while True:  # loop $label526
                                    var5 = var13
                                    var13 = (var13 + 1)
                                    if (1 if var5 >= var28 else 0):
                                        break
                                    if (1 if var30 <= 0 else 0):
                                        var1 = var2
                                        while True:  # loop $label511
                                            var3 = var1
                                            var1 = (var1 + 1)
                                            if (1 if var3 >= var28 else 0):
                                                break
                                            if (1 if (var3 | var5) < 0 else 0):
                                                break
                                            var3 = ((var17 if (1 if var17 > 0 else 0) else 0) if (1 if i32_load((var24 + ((var13 + ((var1 + var14) * var14)) << 2))) > 2 else 0) else var17)
                                            var17 = ((((var17 if (1 if var17 > 0 else 0) else 0) if (1 if i32_load((var24 + ((var13 + ((var1 + var14) * var14)) << 2))) > 2 else 0) else var17) if (1 if var3 > 0 else 0) else 0) if (1 if i32_load((var24 + ((var13 + ((var1 + var35) * var14)) << 2))) > 2 else 0) else var3)
                                            if (1 if var1 < var36 else 0):
                                                continue
                                            break  # end loop
                                        break
                                    var9 = (var5 - var39)
                                    var38 = ((var5 - var39) + var30)
                                    var6 = var2
                                    while True:  # loop $label525
                                        var3 = var6
                                        var6 = (var6 + 1)
                                        if (1 if var3 >= var28 else 0):
                                            break
                                        if (1 if (var3 | var5) < 0 else 0):
                                            break
                                        var15 = (var3 - var39)
                                        var42 = ((var3 - var39) + var30)
                                        var34 = 1
                                        while True:  # loop $label524
                                            var1 = i32_load((var24 + ((var13 + ((var6 + (var14 * var34)) * var14)) << 2)))
                                            if (1 if i32_load((var24 + ((var13 + ((var6 + (var14 * var34)) * var14)) << 2))) >= 3 else 0):
                                                var11 = (var29 + (var1 * 132))
                                                var25 = ((var29 + (var1 * 132)) - -64)
                                                var12 = 0
                                                var7 = var9
                                                while True:  # loop $label523
                                                    var4 = (var7 + 1)
                                                    var1 = var15
                                                    if (1 if var7 < var28 else 0):
                                                        while True:  # loop $label522
                                                            var10 = var1
                                                            var1 = (var1 + 1)
                                                            if (1 if var10 >= var28 else 0):
                                                                break
                                                            if (1 if (var7 | var10) < 0 else 0):
                                                                break
                                                            if (1 if i32_load((var24 + ((var4 + (var1 * var14)) << 2))) <= 2 else 0):
                                                                break
                                                            var10 = i32_load8_u(var11 + 122)
                                                            if (1 if var27 == i32_load8_u(var11 + 122) else 0):
                                                                break
                                                            var22 = i32_load16_u(var11 + 110)
                                                            var37 = i32_load16_u(var11 + 120)
                                                            if i32_load16_u(var11 + 120):
                                                            else:
                                                            if i32_load8_u(((var37 if i32_load8_u((var21 + (var20 + var22))) else var22) + (var22 + var20))):
                                                                if (1 if i32_load8_u(var11 + 128) == 0 else 0):
                                                                    break
                                                                break
                                                            if (1 if i32_load8_u(var11 + 127) != 6 else 0):
                                                                break
                                                            if i32_load8_u(var11 + 128):
                                                                break
                                                            if (1 if i32_load8_u(var11 + 125) == 10 else 0):
                                                                break
                                                            if (1 if i32_load8_u(var11 + 126) == 2 else 0):
                                                                break
                                                            if (1 if i32_load(var25) == -1 else 0):
                                                                break
                                                            var22 = ((var10 * 404) + 9568096)
                                                            if (1 if i32_load(((var10 * 404) + 9568096) + 264) == 2 else 0):
                                                                break
                                                            if (1 if i32_load(var22 + 188) != 55 else 0):
                                                                break
                                                            if (1 if var10 == var33 else 0):
                                                                break
                                                            if (1 if var10 == var32 else 0):
                                                                break
                                                            if (1 if var10 != var31 else 0):
                                                                break
                                                            if (1 if i32_load((var23 + (i32_load(var11 + 44) << 4)) + 4) != 6 else 0):
                                                                if (1 if i32_load8_u(var11 + 123) != 6 else 0):
                                                                    break
                                                            var12 = (var12 + (1 if i32_load8_u(var11 + 126) != 1 else 0))
                                                            if (1 if i32_load((var24 + ((var4 + ((var1 + var14) * var14)) << 2))) < 3 else 0):
                                                                break
                                                            var10 = i32_load8_u(var11 + 122)
                                                            if (1 if var27 == i32_load8_u(var11 + 122) else 0):
                                                                break
                                                            var22 = i32_load16_u(var11 + 110)
                                                            var37 = i32_load16_u(var11 + 120)
                                                            if i32_load16_u(var11 + 120):
                                                            else:
                                                            if i32_load8_u(((var37 if i32_load8_u((var21 + (var20 + var22))) else var22) + (var22 + var20))):
                                                                if (1 if i32_load8_u(var11 + 128) == 0 else 0):
                                                                    break
                                                                break
                                                            if (1 if i32_load8_u(var11 + 127) != 6 else 0):
                                                                break
                                                            if i32_load8_u(var11 + 128):
                                                                break
                                                            if (1 if i32_load8_u(var11 + 125) == 10 else 0):
                                                                break
                                                            if (1 if i32_load8_u(var11 + 126) == 2 else 0):
                                                                break
                                                            if (1 if i32_load(var25) == -1 else 0):
                                                                break
                                                            var22 = ((var10 * 404) + 9568096)
                                                            if (1 if i32_load(((var10 * 404) + 9568096) + 264) == 2 else 0):
                                                                break
                                                            if (1 if i32_load(var22 + 188) != 55 else 0):
                                                                break
                                                            if (1 if var10 == var33 else 0):
                                                                break
                                                            if (1 if var10 == var32 else 0):
                                                                break
                                                            if (1 if var10 != var31 else 0):
                                                                break
                                                            if (1 if i32_load((var23 + (i32_load(var11 + 44) << 4)) + 4) != 6 else 0):
                                                                if (1 if i32_load8_u(var11 + 123) != 6 else 0):
                                                                    break
                                                            var12 = (var12 + (1 if i32_load8_u(var11 + 126) != 1 else 0))
                                                            if (1 if i32_load((var24 + ((var4 + ((var1 + var35) * var14)) << 2))) < 3 else 0):
                                                                break
                                                            var10 = i32_load8_u(var11 + 122)
                                                            if (1 if var27 == i32_load8_u(var11 + 122) else 0):
                                                                break
                                                            var22 = i32_load16_u(var11 + 110)
                                                            var37 = i32_load16_u(var11 + 120)
                                                            if i32_load16_u(var11 + 120):
                                                            else:
                                                            if i32_load8_u(((var37 if i32_load8_u((var21 + (var20 + var22))) else var22) + (var22 + var20))):
                                                                if (1 if i32_load8_u(var11 + 128) == 0 else 0):
                                                                    break
                                                                break
                                                            if (1 if i32_load8_u(var11 + 127) != 6 else 0):
                                                                break
                                                            if i32_load8_u(var11 + 128):
                                                                break
                                                            if (1 if i32_load8_u(var11 + 125) == 10 else 0):
                                                                break
                                                            if (1 if i32_load8_u(var11 + 126) == 2 else 0):
                                                                break
                                                            if (1 if i32_load(var25) == -1 else 0):
                                                                break
                                                            var22 = ((var10 * 404) + 9568096)
                                                            if (1 if i32_load(((var10 * 404) + 9568096) + 264) == 2 else 0):
                                                                break
                                                            if (1 if i32_load(var22 + 188) != 55 else 0):
                                                                break
                                                            if (1 if var10 == var33 else 0):
                                                                break
                                                            if (1 if var10 == var32 else 0):
                                                                break
                                                            if (1 if var10 != var31 else 0):
                                                                break
                                                            if (1 if i32_load((var23 + (i32_load(var11 + 44) << 4)) + 4) != 6 else 0):
                                                                if (1 if i32_load8_u(var11 + 123) != 6 else 0):
                                                                    break
                                                            var12 = (var12 + (1 if i32_load8_u(var11 + 126) != 1 else 0))
                                                            if (1 if var1 < var42 else 0):
                                                                continue
                                                            break  # end loop
                                                    var7 = var4
                                                    if (1 if var4 < var38 else 0):
                                                        continue
                                                    break  # end loop
                                                var1 = (1 if var12 > var17 else 0)
                                                var17 = (var12 if (1 if var12 > var17 else 0) else var17)
                                                var60 = (var5 if var1 else var60)
                                                var51 = (var3 if var1 else var51)
                                            var34 = (var34 + 1)
                                            if (1 if (var34 + 1) != 3 else 0):
                                                continue
                                            break  # end loop
                                        if (1 if var6 < var36 else 0):
                                            continue
                                        break  # end loop
                                    if (1 if var13 < var41 else 0):
                                        continue
                                    break  # end loop
                                if (1 if var17 == 0 else 0):
                                    break
                                if (1 if i32_load8_u(var18 + 123) == 9 else 0):
                                    break
                                var2 = 0
                                var5 = i32_load(9671128)
                                while True:  # loop $label530
                                    var1 = ((var2 * 404) + 9568096)
                                    if i32_load(((var2 * 404) + 9568096) + 264):
                                        break
                                    if (1 if i32_load(var1 + 268) == 1 else 0):
                                        break
                                    if (1 if i32_load(var1 + 92) == 0 else 0):
                                        break
                                    var1 = i32_load(((var8 + (var2 << 2)) + 284636))
                                    if (1 if i32_load(((var8 + (var2 << 2)) + 284636)) == 0 else 0):
                                        break
                                    var3 = i32_load(var1 + 8)
                                    if (1 if i32_load(var1 + 8) == 0 else 0):
                                        break
                                    var4 = i32_load(var1)
                                    var1 = 0
                                    while True:  # loop $label528
                                        var6 = i32_load((var4 + (var1 << 2)))
                                        if (1 if i32_load((var4 + (var1 << 2))) == 0 else 0):
                                            var1 = (var1 + 1)
                                            if (1 if var3 != (var1 + 1) else 0):
                                                continue
                                            break
                                        break  # end loop
                                    var7 = i32_load((var5 + (var6 * 132)) + 28)
                                    if (1 if i32_load((var5 + (var6 * 132)) + 28) == i32_load(var18 + 28) else 0):
                                        break
                                    if var7:
                                        break
                                    var2 = (var2 + 1)
                                    if (1 if (var2 + 1) != 132 else 0):
                                        continue
                                    break
                                    break  # end loop
                                var2 = i32_load(var18 + 20)
                                if (1 if i32_load(var18 + 20) == 0 else 0):
                                    var2 = func26(16)
                                    i32_store(func26(16) + 4, 7)
                                    i32_store(var2, func26(28))
                                    i64_store(var2 + 8, 4294967296)
                                    i32_store(var18 + 20, var2)
                                    var5 = (var2 + 8)
                                    break
                                i32_store(var2 + 8, 0)
                                var5 = (var2 + 8)
                                if (1 if i32_load(var2 + 4) == 0 else 0):
                                    break
                                var6 = i32_load(var2)
                                var3 = 0
                                break
                                var1 = i32_load(var2 + 12)
                                i32_store(var2 + 4, i32_load(var2 + 12))
                                var3 = i32_load(var2)
                                var6 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
                                if var3:
                                else:
                                var3 = 0
                                i32_store(var2, var6)
                                var2 = i32_load(var18 + 20)
                                i32_store(var5, (var3 + 1))
                                i32_store((var6 + (var3 << 2)), 1)
                                var6 = i32_load(var2 + 8)
                                if (1 if i32_load(var2 + 8) != i32_load(var2 + 4) else 0):
                                    var5 = i32_load(var2)
                                    break
                                var5 = (i32_load(var2 + 12) + var6)
                                i32_store(var2 + 4, (i32_load(var2 + 12) + var6))
                                var1 = i32_load(var2)
                                var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
                                if var6:
                                    # Unknown: memory.copy []
                                if var1:
                                    var6 = i32_load(var2 + 8)
                                i32_store(var2, var5)
                                var1 = i32_load(var18 + 20)
                                i32_store(var2 + 8, (var6 + 1))
                                i32_store((var5 + (var6 << 2)), 2)
                                var6 = i32_load(var1 + 8)
                                if (1 if i32_load(var1 + 8) != i32_load(var1 + 4) else 0):
                                    var5 = i32_load(var1)
                                    break
                                var5 = (i32_load(var1 + 12) + var6)
                                i32_store(var1 + 4, (i32_load(var1 + 12) + var6))
                                var2 = i32_load(var1)
                                var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
                                if var6:
                                    # Unknown: memory.copy []
                                if var2:
                                    var6 = i32_load(var1 + 8)
                                i32_store(var1, var5)
                                var2 = i32_load(var18 + 20)
                                i32_store(var1 + 8, (var6 + 1))
                                i32_store((var5 + (var6 << 2)), 0)
                                var6 = i32_load(var2 + 8)
                                if (1 if i32_load(var2 + 8) != i32_load(var2 + 4) else 0):
                                    var5 = i32_load(var2)
                                    break
                                var5 = (i32_load(var2 + 12) + var6)
                                i32_store(var2 + 4, (i32_load(var2 + 12) + var6))
                                var1 = i32_load(var2)
                                var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
                                if var6:
                                    # Unknown: memory.copy []
                                if var1:
                                    var6 = i32_load(var2 + 8)
                                i32_store(var2, var5)
                                var1 = i32_load(var18 + 20)
                                i32_store(var2 + 8, (var6 + 1))
                                i32_store((var5 + (var6 << 2)), 0)
                                var6 = i32_load(var1 + 8)
                                if (1 if i32_load(var1 + 8) != i32_load(var1 + 4) else 0):
                                    var5 = i32_load(var1)
                                    break
                                var5 = (i32_load(var1 + 12) + var6)
                                i32_store(var1 + 4, (i32_load(var1 + 12) + var6))
                                var2 = i32_load(var1)
                                var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
                                if var6:
                                    # Unknown: memory.copy []
                                if var2:
                                    var6 = i32_load(var1 + 8)
                                i32_store(var1, var5)
                                var2 = i32_load(var18 + 20)
                                i32_store(var1 + 8, (var6 + 1))
                                i32_store((var5 + (var6 << 2)), var7)
                                var6 = i32_load(var2 + 8)
                                if (1 if i32_load(var2 + 8) != i32_load(var2 + 4) else 0):
                                    var5 = i32_load(var2)
                                    break
                                var5 = (i32_load(var2 + 12) + var6)
                                i32_store(var2 + 4, (i32_load(var2 + 12) + var6))
                                var1 = i32_load(var2)
                                var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
                                if var6:
                                    # Unknown: memory.copy []
                                if var1:
                                    var6 = i32_load(var2 + 8)
                                i32_store(var2, var5)
                                var1 = i32_load(var18 + 20)
                                i32_store(var2 + 8, (var6 + 1))
                                i32_store((var5 + (var6 << 2)), 0)
                                var6 = i32_load(var1 + 8)
                                if (1 if i32_load(var1 + 8) != i32_load(var1 + 4) else 0):
                                    var5 = i32_load(var1)
                                    break
                                var5 = (i32_load(var1 + 12) + var6)
                                i32_store(var1 + 4, (i32_load(var1 + 12) + var6))
                                var2 = i32_load(var1)
                                var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
                                if var6:
                                    # Unknown: memory.copy []
                                if var2:
                                    var6 = i32_load(var1 + 8)
                                i32_store(var1, var5)
                                var2 = i32_load(var18 + 20)
                                i32_store(var1 + 8, (var6 + 1))
                                i32_store((var5 + (var6 << 2)), 0)
                                var6 = i32_load(var2 + 8)
                                if (1 if i32_load(var2 + 8) != i32_load(var2 + 4) else 0):
                                    var5 = i32_load(var2)
                                    break
                                var5 = (i32_load(var2 + 12) + var6)
                                i32_store(var2 + 4, (i32_load(var2 + 12) + var6))
                                var1 = i32_load(var2)
                                var5 = func26((-1 if (1 if var5 > 1073741823 else 0) else (var5 << 2)))
                                if var6:
                                    # Unknown: memory.copy []
                                if var1:
                                    var6 = i32_load(var2 + 8)
                                i32_store(var2, var5)
                                var1 = i32_load(var18 + 20)
                                i32_store(var2 + 8, (var6 + 1))
                                i32_store((var5 + (var6 << 2)), 5)
                                var2 = i32_load(var1 + 8)
                                if (1 if i32_load(var1 + 8) != i32_load(var1 + 4) else 0):
                                    var4 = i32_load(var1)
                                    break
                                var3 = (i32_load(var1 + 12) + var2)
                                i32_store(var1 + 4, (i32_load(var1 + 12) + var2))
                                var5 = i32_load(var1)
                                var4 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
                                if var2:
                                    # Unknown: memory.copy []
                                if var5:
                                    var2 = i32_load(var1 + 8)
                                i32_store(var1, var4)
                                i32_store(var1 + 8, (var2 + 1))
                                i32_store((var4 + (var2 << 2)), 0)
                                var46 = (var46 + 1)
                                if (1 if (var46 + 1) < i32_load(var45 + 8) else 0):
                                    continue
                                break  # end loop
                            var26 = (var26 + 1)
                            if (1 if (var26 + 1) != 132 else 0):
                                continue
                            break  # end loop
                        if (1 if var16 == 0 else 0):
                            break
                        var5 = i32_load(var49)
                        if (1 if i32_load(var49) == 0 else 0):
                            break
                        var1 = 0
                        var6 = i32_load(var5 + 8)
                        if (1 if i32_load(var5 + 8) == 0 else 0):
                            break
                        while True:  # loop $label546
                            var2 = i32_load((i32_load(var5) + (var1 << 2)))
                            if (1 if i32_load((i32_load(var5) + (var1 << 2))) == 0 else 0):
                                break
                            var2 = (i32_load(9671128) + (var2 * 132))
                            var3 = i32_load((i32_load(9671128) + (var2 * 132)) + 44)
                            if (1 if ((1 if i32_load((i32_load(9215884) + (i32_load((i32_load(9671128) + (var2 * 132)) + 44) << 4)) + 4) == 22 else 0) | (1 if var3 == 0 else 0)) == 0 else 0):
                                break
                            if i32_load8_u(var2 + 125):
                                break
                            if i32_load(var2 + 36):
                                break
                            if (1 if i32_load8_u(var2 + 129) == 10 else 0):
                                break
                            i32_store8(var2 + 129, 0)
                            var6 = i32_load(var5 + 8)
                            var1 = (var1 + 1)
                            if (1 if (var1 + 1) < var6 else 0):
                                continue
                            break  # end loop
                        if (1 if var44 == 0 else 0):
                            break
                        var33 = i32_load(var8 + 286688)
                        var27 = ((((100 - i32_load(var8 + 286688)) * var48) & 0xFFFFFFFF) // 100)
                        var9 = 0
                        var34 = (1 if i32_load(9142848) < (i32_load(i32_load(9142424) + 72) * 2400) else 0)
                        if (1 if (1 if i32_load(9142848) < (i32_load(i32_load(9142424) + 72) * 2400) else 0) == 0 else 0):
                            var4 = 0
                            var105 = (math.sqrt(float(i32_load(var8 + 283880))) + 9.0)
                            if (1 if abs((math.sqrt(float(i32_load(var8 + 283880))) + 9.0)) < 2147483648.0 else 0):
                                break
                            var25 = -2147483648
                            if (1 if -2147483648 < 2 else 0):
                                break
                            var24 = i32_load(var8 + 283872)
                            var5 = (i32_load(var8 + 283872) - 1)
                            var28 = i32_load(var8 + 283876)
                            var3 = (i32_load(var8 + 283876) - 1)
                            var10 = (var24 + 2)
                            var13 = (var28 + 2)
                            var9 = (i32_load(9142892) * i32_load(var8 + 283908))
                            var23 = i32_load(9142440)
                            var15 = (i32_load(9142440) + 2)
                            var22 = ((i32_load(9142440) + 2) << 1)
                            var14 = i32_load(38564)
                            var17 = i32_load(38620)
                            var20 = i32_load(38560)
                            var16 = i32_load(9143004)
                            var21 = i32_load(38500)
                            var18 = i32_load(9671128)
                            var26 = i32_load(9142840)
                            var11 = 1
                            while True:  # loop $label561
                                if (1 if var5 >= var10 else 0):
                                    break
                                if (1 if var3 >= var13 else 0):
                                    break
                                var48 = (var10 - 1)
                                var49 = (var13 - 1)
                                var30 = 1
                                var1 = var5
                                while True:  # loop $label560
                                    var6 = var1
                                    var1 = (var1 + 1)
                                    if (1 if var6 >= var23 else 0):
                                        break
                                    var45 = (1 if var6 == var48 else 0)
                                    var46 = (1 if var5 == var6 else 0)
                                    var31 = 1
                                    var2 = var3
                                    while True:  # loop $label558
                                        if (1 if (var45 | ((var46 | (1 if var2 == var3 else 0)) | (1 if var2 == var49 else 0))) == 0 else 0):
                                            break
                                        if (1 if var2 >= var23 else 0):
                                            break
                                        if (1 if (var2 | var6) < 0 else 0):
                                            break
                                        var32 = (var2 + 1)
                                        var4 = i32_load((var26 + ((var1 + ((var2 + 1) * var15)) << 2)))
                                        if (1 if i32_load((var26 + ((var1 + ((var2 + 1) * var15)) << 2))) <= 2 else 0):
                                            break
                                        var7 = (var18 + (var4 * 132))
                                        var12 = i32_load8_u((var18 + (var4 * 132)) + 122)
                                        if (1 if var21 == i32_load8_u((var18 + (var4 * 132)) + 122) else 0):
                                            break
                                        var29 = i32_load16_u(var7 + 110)
                                        var36 = i32_load16_u(var7 + 120)
                                        if i32_load16_u(var7 + 120):
                                        else:
                                        if i32_load8_u(((var36 if i32_load8_u((var16 + (var9 + var29))) else var29) + (var29 + var9))):
                                            if (1 if i32_load8_u(var7 + 128) == 0 else 0):
                                                break
                                            break
                                        if (1 if i32_load8_u(var7 + 127) != 6 else 0):
                                            break
                                        if i32_load8_u(var7 + 128):
                                            break
                                        if (1 if i32_load8_u(var7 + 125) == 10 else 0):
                                            break
                                        if (1 if i32_load8_u(var7 + 126) == 2 else 0):
                                            break
                                        if (1 if i32_load(var7 + 64) == -1 else 0):
                                            break
                                        var7 = ((var12 * 404) + 9568096)
                                        if (1 if i32_load(((var12 * 404) + 9568096) + 264) == 2 else 0):
                                            break
                                        if (1 if i32_load(var7 + 188) != 55 else 0):
                                            break
                                        if (1 if var12 == var20 else 0):
                                            break
                                        if (1 if var12 == var17 else 0):
                                            break
                                        if (1 if var12 != var14 else 0):
                                            break
                                        var4 = i32_load((var26 + ((var1 + ((var15 + var32) * var15)) << 2)))
                                        if (1 if i32_load((var26 + ((var1 + ((var15 + var32) * var15)) << 2))) < 3 else 0):
                                            break
                                        var7 = (var18 + (var4 * 132))
                                        var12 = i32_load8_u((var18 + (var4 * 132)) + 122)
                                        if (1 if var21 == i32_load8_u((var18 + (var4 * 132)) + 122) else 0):
                                            break
                                        var29 = i32_load16_u(var7 + 110)
                                        var36 = i32_load16_u(var7 + 120)
                                        if i32_load16_u(var7 + 120):
                                        else:
                                        if i32_load8_u(((var36 if i32_load8_u((var16 + (var9 + var29))) else var29) + (var29 + var9))):
                                            if (1 if i32_load8_u(var7 + 128) == 0 else 0):
                                                break
                                            break
                                        if (1 if i32_load8_u(var7 + 127) != 6 else 0):
                                            break
                                        if i32_load8_u(var7 + 128):
                                            break
                                        if (1 if i32_load8_u(var7 + 125) == 10 else 0):
                                            break
                                        if (1 if i32_load8_u(var7 + 126) == 2 else 0):
                                            break
                                        if (1 if i32_load(var7 + 64) == -1 else 0):
                                            break
                                        var7 = ((var12 * 404) + 9568096)
                                        if (1 if i32_load(((var12 * 404) + 9568096) + 264) == 2 else 0):
                                            break
                                        if (1 if i32_load(var7 + 188) != 55 else 0):
                                            break
                                        if (1 if var12 == var20 else 0):
                                            break
                                        if (1 if var12 == var17 else 0):
                                            break
                                        if (1 if var12 != var14 else 0):
                                            break
                                        var4 = i32_load((var26 + ((var1 + ((var22 + var32) * var15)) << 2)))
                                        if (1 if i32_load((var26 + ((var1 + ((var22 + var32) * var15)) << 2))) < 3 else 0):
                                            break
                                        var7 = (var18 + (var4 * 132))
                                        var12 = i32_load8_u((var18 + (var4 * 132)) + 122)
                                        if (1 if var21 == i32_load8_u((var18 + (var4 * 132)) + 122) else 0):
                                            break
                                        var29 = i32_load16_u(var7 + 110)
                                        var32 = i32_load16_u(var7 + 120)
                                        if i32_load16_u(var7 + 120):
                                        else:
                                        if i32_load8_u(((var32 if i32_load8_u((var16 + (var9 + var29))) else var29) + (var29 + var9))):
                                            if (1 if i32_load8_u(var7 + 128) == 0 else 0):
                                                break
                                            break
                                        if (1 if i32_load8_u(var7 + 127) != 6 else 0):
                                            break
                                        if i32_load8_u(var7 + 128):
                                            break
                                        if (1 if i32_load8_u(var7 + 125) == 10 else 0):
                                            break
                                        if (1 if i32_load8_u(var7 + 126) == 2 else 0):
                                            break
                                        if (1 if i32_load(var7 + 64) == -1 else 0):
                                            break
                                        var7 = ((var12 * 404) + 9568096)
                                        if (1 if i32_load(((var12 * 404) + 9568096) + 264) == 2 else 0):
                                            break
                                        if (1 if i32_load(var7 + 188) != 55 else 0):
                                            break
                                        if (1 if var12 == var20 else 0):
                                            break
                                        if (1 if var12 == var17 else 0):
                                            break
                                        if (1 if var12 != var14 else 0):
                                            break
                                        var2 = (var2 + 1)
                                        var31 = (1 if (var2 + 1) < var13 else 0)
                                        if (1 if var2 != var13 else 0):
                                            continue
                                        break
                                        break  # end loop
                                    if var31:
                                        break
                                    var30 = (1 if var1 < var10 else 0)
                                    if (1 if var1 != var10 else 0):
                                        continue
                                    break
                                    break  # end loop
                                if var30:
                                    break
                                var13 = (var13 + 1)
                                var10 = (var10 + 1)
                                var11 = (var11 + 1)
                                var3 = (var28 - (var11 + 1))
                                var5 = (var24 - var11)
                                if (1 if var11 != var25 else 0):
                                    continue
                                break  # end loop
                            var4 = 0
                            var9 = var4
                        if (1 if var33 == 0 else 0):
                            break
                        if (1 if var44 <= (var27 + 55) else 0):
                            break
                        if var9:
                            break
                        if var34:
                            break
                        var6 = i32_load(9142892)
                        if (1 if i32_load(9142892) < 2 else 0):
                            break
                        var13 = (var6 * var40)
                        var7 = i32_load(9561692)
                        var1 = (i32_load(9561692) + var62)
                        var9 = ((i32_load(9561692) + var62) + 283876)
                        var16 = (var1 + 283872)
                        var3 = 0
                        var15 = i32_load(9143004)
                        var2 = 1
                        var10 = 2147483647
                        while True:  # loop $label568
                            if (1 if var2 == var40 else 0):
                                break
                            var5 = (var7 + (var2 * 286704))
                            if i32_load8_u((var7 + (var2 * 286704)) + 286696):
                                break
                            if (1 if i32_load8_u((var15 + (var2 + var13))) == 0 else 0):
                                break
                            var1 = (i32_load(var5 + 283876) - i32_load(var9))
                            var1 = (i32_load(var5 + 283872) - i32_load(var16))
                            var11 = (((i32_load(var5 + 283876) - i32_load(var9)) * var1) + ((i32_load(var5 + 283872) - i32_load(var16)) * var1))
                            if (1 if (((i32_load(var5 + 283876) - i32_load(var9)) * var1) + ((i32_load(var5 + 283872) - i32_load(var16)) * var1)) >= var10 else 0):
                                break
                            var1 = 0
                            var4 = 1
                            while True:  # loop $label567
                                if i32_load(((var5 + (var1 << 2)) + 281808)):
                                    if (1 if i32_load8_u(((var1 * 404) + 9568096) + 376) == 0 else 0):
                                        break
                                var4 = (var1 | 1)
                                if (1 if i32_load(((var5 + ((var1 | 1) << 2)) + 281808)) == 0 else 0):
                                    break
                                if i32_load8_u(((var4 * 404) + 9568096) + 376):
                                    break
                                var4 = 1
                                break
                                var4 = (1 if var4 < 131 else 0)
                                var1 = (var1 + 2)
                                if (1 if (var1 + 2) != 132 else 0):
                                    continue
                                break  # end loop
                            var1 = (var4 & 1)
                            var3 = (var2 if (var4 & 1) else var3)
                            var10 = (var11 if var1 else var10)
                            var2 = (var2 + 1)
                            if (1 if (var2 + 1) != var6 else 0):
                                continue
                            break  # end loop
                        if (1 if var3 == 0 else 0):
                            break
                        i32_store(var8 + 283904, var3)
                        var13 = (var7 + (var3 * 286704))
                        var11 = ((var7 + (var3 * 286704)) + 283880)
                        var12 = (var13 + 283876)
                        var14 = (var13 + 283872)
                        var5 = 0
                        var17 = i32_load(38564)
                        var20 = i32_load(38620)
                        var21 = i32_load(38560)
                        var18 = i32_load(9142892)
                        var16 = i32_load(9143004)
                        var26 = i32_load(38500)
                        var29 = i32_load(9671128)
                        var1 = i32_load(9142440)
                        var24 = (i32_load(9142440) * var1)
                        var7 = 2147483647
                        var9 = 0
                        while True:  # loop $label574
                            var1 = i32_load(((var13 + (var5 << 2)) + 284636))
                            if (1 if i32_load(((var13 + (var5 << 2)) + 284636)) == 0 else 0):
                                break
                            var28 = i32_load(var1 + 8)
                            if (1 if i32_load(var1 + 8) == 0 else 0):
                                break
                            var23 = i32_load(var1)
                            var2 = 0
                            while True:  # loop $label573
                                var1 = i32_load((var23 + (var2 << 2)))
                                if (1 if i32_load((var23 + (var2 << 2))) == 0 else 0):
                                    break
                                var3 = (var29 + (var1 * 132))
                                var1 = i32_load16_u((var29 + (var1 * 132)) + 114)
                                var4 = (i32_load16_u((var29 + (var1 * 132)) + 114) - i32_load(var12))
                                var4 = i32_load16_u(var3 + 112)
                                var6 = (i32_load16_u(var3 + 112) - i32_load(var14))
                                var1 = (var1 - i32_load(var52))
                                var1 = (var4 - i32_load(var43))
                                var6 = i32_load8_u(var3 + 122)
                                var30 = ((i32_load8_u(var3 + 122) * 404) + 9568096)
                                var44 = i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 264)
                                var1 = ((var24 if (1 if (((i32_load16_u((var29 + (var1 * 132)) + 114) - i32_load(var12)) * var4) + ((i32_load16_u(var3 + 112) - i32_load(var14)) * var6)) > (i32_load(var11) + 100) else 0) else 0) + ((((var1 - i32_load(var52)) * var1) + ((var4 - i32_load(var43)) * var1)) * (3 if (1 if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 264) == 4 else 0) else 1)))
                                if (1 if ((var24 if (1 if (((i32_load16_u((var29 + (var1 * 132)) + 114) - i32_load(var12)) * var4) + ((i32_load16_u(var3 + 112) - i32_load(var14)) * var6)) > (i32_load(var11) + 100) else 0) else 0) + ((((var1 - i32_load(var52)) * var1) + ((var4 - i32_load(var43)) * var1)) * (3 if (1 if i32_load(((i32_load8_u(var3 + 122) * 404) + 9568096) + 264) == 4 else 0) else 1))) >= var7 else 0):
                                    break
                                var4 = 0
                                if (1 if var6 == var26 else 0):
                                    break
                                var10 = i32_load16_u(var3 + 110)
                                var15 = (var18 * i32_load(var63))
                                var31 = i32_load16_u(var3 + 120)
                                if i32_load16_u(var3 + 120):
                                else:
                                if (1 if i32_load8_u(((var31 if i32_load8_u((var16 + (var10 + var15))) else var10) + (var10 + var15))) == 0 else 0):
                                    if (1 if i32_load8_u(var3 + 127) != 6 else 0):
                                        break
                                    if (1 if i32_load8_u(var3 + 128) == 0 else 0):
                                        break
                                    break
                                if i32_load8_u(var3 + 128):
                                    break
                                if (1 if i32_load8_u(var3 + 125) == 10 else 0):
                                    break
                                if (1 if i32_load8_u(var3 + 126) == 2 else 0):
                                    break
                                if (1 if i32_load(var3 + 64) == -1 else 0):
                                    break
                                if (1 if var44 == 2 else 0):
                                    break
                                var4 = ((((1 if i32_load(var30 + 188) == 55 else 0) & (1 if var6 != var21 else 0)) & (1 if var6 != var20 else 0)) & (1 if var6 != var17 else 0))
                                if (1 if var4 == 0 else 0):
                                    break
                                if i32_load(var3 + 36):
                                    break
                                if (1 if i32_load8_u(var3 + 125) == 10 else 0):
                                    break
                                var9 = i32_load(var3 + 28)
                                var7 = var1
                                var2 = (var2 + 1)
                                if (1 if (var2 + 1) != var28 else 0):
                                    continue
                                break  # end loop
                            var5 = (var5 + 1)
                            if (1 if (var5 + 1) != 132 else 0):
                                continue
                            break  # end loop
                        if (1 if var9 == 0 else 0):
                            break
                        var2 = 0
                        var11 = (var9 * 132)
                        var7 = i32_load8_u(((var9 * 132) + i32_load(9671128)) + 122)
                        var16 = ((i32_load8_u(((var9 * 132) + i32_load(9671128)) + 122) * 404) + 9568096)
                        while True:  # loop $label589
                            var1 = ((var2 * 404) + 9568096)
                            if i32_load(((var2 * 404) + 9568096) + 264):
                                break
                            if (1 if i32_load(var1 + 268) == 1 else 0):
                                break
                            if (1 if i32_load(var1 + 92) == 0 else 0):
                                break
                            if (1 if i32_load(38456) == var2 else 0):
                                break
                            if (1 if i32_load(38764) == var2 else 0):
                                break
                            var15 = i32_load(((var8 + (var2 << 2)) + 284636))
                            if (1 if i32_load(((var8 + (var2 << 2)) + 284636)) == 0 else 0):
                                break
                            var1 = 0
                            var6 = i32_load(var15 + 8)
                            if (1 if i32_load(var15 + 8) == 0 else 0):
                                break
                            while True:  # loop $label588
                                var5 = i32_load((i32_load(var15) + (var1 << 2)))
                                if (1 if i32_load((i32_load(var15) + (var1 << 2))) == 0 else 0):
                                    break
                                var12 = i32_load(9671128)
                                var4 = (i32_load(9671128) + (var5 * 132))
                                if i32_load8_u((i32_load(9671128) + (var5 * 132)) + 129):
                                    break
                                if i32_load(var4 + 36):
                                    break
                                if (1 if i32_load(9142848) >= (i32_load(i32_load(9142424) + 72) * 2400) else 0):
                                    break
                                if (1 if i32_load(var4 + 56) == 1 else 0):
                                else:
                                if 0:
                                    break
                                if (1 if i32_load(38564) != var7 else 0):
                                    break
                                var3 = i32_load8_u(var4 + 122)
                                var13 = i32_load(var16 + 264)
                                if (1 if i32_load(var16 + 188) == 55 else 0):
                                    break
                                if (1 if var13 != 1 else 0):
                                    break
                                if (1 if i32_load(38500) != var7 else 0):
                                    break
                                if (1 if var13 == 4 else 0):
                                    if (1 if i32_load(((var3 * 404) + 9568096) + 224) == 1 else 0):
                                        break
                                var5 = ((var3 * 404) + 9568096)
                                if (1 if i32_load(((var3 * 404) + 9568096) + 272) == 0 else 0):
                                    if (1 if i32_load(38648) != var3 else 0):
                                        break
                                if (1 if i32_load(var16 + 208) == 2 else 0):
                                    break
                                if (1 if i32_load(38564) != var7 else 0):
                                    break
                                if i32_load8_u(var5 + 334):
                                    break
                                if (1 if i32_load(var5 + 268) != 2 else 0):
                                    break
                                if (1 if var3 != i32_load(38728) else 0):
                                    if (1 if i32_load(38996) != var3 else 0):
                                        break
                                if var13:
                                    break
                                if (1 if i32_load(var16 + 268) == 2 else 0):
                                    break
                                if i32_load8_u(var5 + 379):
                                    break
                                var3 = i32_load(var5 + 24)
                                if (1 if i32_load(var5 + 24) == 0 else 0):
                                    break
                                var10 = 0
                                var13 = i32_load(var5 + 364)
                                if (1 if i32_load(var5 + 364) == 0 else 0):
                                    break
                                while True:  # loop $label583
                                    if (1 if i32_load((var3 + (var10 << 2))) == var7 else 0):
                                        break
                                    var10 = (var10 + 1)
                                    if (1 if var13 != (var10 + 1) else 0):
                                        continue
                                    break  # end loop
                                break
                                if i32_load8_u(var4 + 123):
                                    break
                                if (1 if i32_load8_u(9147152) == 0 else 0):
                                    if (1 if i32_load8_u((i32_load(9143008) + (i32_load16_u(var4 + 110) * (i32_load(9142892) + 1)))) == 0 else 0):
                                        break
                                    if (1 if i32_load((i32_load(9215884) + (i32_load(var4 + 44) << 4)) + 4) == 20 else 0):
                                        break
                                    if (1 if i32_load8_u(var4 + 127) == 6 else 0):
                                        break
                                var5 = i32_load(var5 + 228)
                                if (1 if i32_load(var5 + 228) == 0 else 0):
                                    break
                                var3 = (var11 + var12)
                                var10 = i32_load(((i32_load8_u((var11 + var12) + 122) * 404) + 9568096) + 216)
                                if (1 if i32_load(((i32_load8_u((var11 + var12) + 122) * 404) + 9568096) + 216) == 0 else 0):
                                    break
                                var12 = i32_load16_u(var3 + 114)
                                var14 = i32_load16_u(var4 + 114)
                                var17 = i32_load16_u(var3 + 112)
                                var20 = i32_load16_u(var4 + 112)
                                var21 = (var5 * var5)
                                var3 = 0
                                var13 = 1
                                while True:  # loop $label587
                                    var5 = (var14 - (var3 + var12))
                                    var18 = ((var14 - (var3 + var12)) * var5)
                                    var5 = 0
                                    while True:  # loop $label585
                                        var26 = (var20 - (var5 + var17))
                                        if (1 if var21 > (((var20 - (var5 + var17)) * var26) + var18) else 0):
                                            var5 = (var5 + 1)
                                            if (1 if var10 != (var5 + 1) else 0):
                                                continue
                                            break
                                        break  # end loop
                                    if (1 if (var13 & 1) == 0 else 0):
                                        break
                                    break
                                    var3 = (var3 + 1)
                                    var13 = (1 if (var3 + 1) < var10 else 0)
                                    if (1 if var3 != var10 else 0):
                                        continue
                                    break  # end loop
                                break
                                i32_store8(var4 + 129, 5)
                                var6 = i32_load(var15 + 8)
                                var1 = (var1 + 1)
                                if (1 if (var1 + 1) < var6 else 0):
                                    continue
                                break  # end loop
                            var2 = (var2 + 1)
                            if (1 if (var2 + 1) != 132 else 0):
                                continue
                            break  # end loop
                        break
                        var6 = i32_load(9142892)
                        if (1 if i32_load(9142892) < 2 else 0):
                            break
                        var13 = (var6 * var40)
                        var7 = i32_load(9561692)
                        var1 = (i32_load(9561692) + var62)
                        var9 = ((i32_load(9561692) + var62) + 283876)
                        var16 = (var1 + 283872)
                        var3 = 0
                        var15 = i32_load(9143004)
                        var2 = 1
                        var10 = 2147483647
                        while True:  # loop $label594
                            if (1 if var2 == var40 else 0):
                                break
                            var5 = (var7 + (var2 * 286704))
                            if i32_load8_u((var7 + (var2 * 286704)) + 286696):
                                break
                            if (1 if i32_load8_u((var15 + (var2 + var13))) == 0 else 0):
                                break
                            var1 = (i32_load(var5 + 283876) - i32_load(var9))
                            var1 = (i32_load(var5 + 283872) - i32_load(var16))
                            var11 = (((i32_load(var5 + 283876) - i32_load(var9)) * var1) + ((i32_load(var5 + 283872) - i32_load(var16)) * var1))
                            if (1 if (((i32_load(var5 + 283876) - i32_load(var9)) * var1) + ((i32_load(var5 + 283872) - i32_load(var16)) * var1)) >= var10 else 0):
                                break
                            var1 = 0
                            var4 = 1
                            while True:  # loop $label593
                                if i32_load(((var5 + (var1 << 2)) + 281808)):
                                    if (1 if i32_load8_u(((var1 * 404) + 9568096) + 376) == 0 else 0):
                                        break
                                var4 = (var1 | 1)
                                if (1 if i32_load(((var5 + ((var1 | 1) << 2)) + 281808)) == 0 else 0):
                                    break
                                if i32_load8_u(((var4 * 404) + 9568096) + 376):
                                    break
                                var4 = 1
                                break
                                var4 = (1 if var4 < 131 else 0)
                                var1 = (var1 + 2)
                                if (1 if (var1 + 2) != 132 else 0):
                                    continue
                                break  # end loop
                            var1 = (var4 & 1)
                            var3 = (var2 if (var4 & 1) else var3)
                            var10 = (var11 if var1 else var10)
                            var2 = (var2 + 1)
                            if (1 if (var2 + 1) != var6 else 0):
                                continue
                            break  # end loop
                        if (1 if var3 == 0 else 0):
                            break
                        var1 = (var7 + (var3 * 286704))
                        var2 = i32_load((var7 + (var3 * 286704)) + 283876)
                        var5 = i32_load(var52)
                        var2 = (var5 - var2)
                        var2 = i32_load(var43)
                        var1 = i32_load(var1 + 283872)
                        var5 = (i32_load(var43) - i32_load(var1 + 283872))
                        var66 = f32(math.sqrt(float((((var5 - var2) * var2) + ((i32_load(var43) - i32_load(var1 + 283872)) * var5)))))
                        var67 = ((float(i32_load((var7 + (var3 * 286704)) + 283876)) - float(i32_load(var52))) / f32(math.sqrt(float((((var5 - var2) * var2) + ((i32_load(var43) - i32_load(var1 + 283872)) * var5))))))
                        var66 = ((float(var1) - float(var2)) / var66)
                        var70 = f32(math.sqrt(float(i32_load(var8 + 283880))))
                        var1 = 0
                        while True:  # loop $label601
                            var2 = ((var1 * 404) + 9568096)
                            if i32_load(((var1 * 404) + 9568096) + 264):
                                break
                            if (1 if i32_load(var2 + 268) == 1 else 0):
                                break
                            if (1 if i32_load(var2 + 92) == 0 else 0):
                                break
                            if (1 if i32_load(38456) == var1 else 0):
                                break
                            if (1 if i32_load(38764) == var1 else 0):
                                break
                            var68 = (var70 + float((6 if (1 if i32_load(var2 + 224) > 1 else 0) else 10)))
                            var105 = (float((var66 * (var70 + float((6 if (1 if i32_load(var2 + 224) > 1 else 0) else 10))))) + 0.5)
                            if (1 if abs((float((var66 * (var70 + float((6 if (1 if i32_load(var2 + 224) > 1 else 0) else 10))))) + 0.5)) < 2147483648.0 else 0):
                                break
                            var5 = -2147483648
                            var4 = i32_load(var43)
                            var2 = i32_load(9142440)
                            var105 = (float((var67 * var68)) + 0.5)
                            if (1 if abs((float((var67 * var68)) + 0.5)) < 2147483648.0 else 0):
                                break
                            var3 = (-2147483648 + i32_load(var52))
                            if (1 if int(var105) <= (-2147483648 + i32_load(var52)) else 0):
                                break
                            var4 = (var4 + var5)
                            if (1 if var2 <= (var4 + var5) else 0):
                                break
                            if (1 if (var3 | var4) < 0 else 0):
                                break
                            var2 = i32_load8_s((i32_load(9147288) + ((var2 * var3) + var4)))
                            if (1 if i32_load8_s((i32_load(9147288) + ((var2 * var3) + var4))) >= 0 else 0):
                                if (1 if i32_load(i32_load((i32_load(9140332) + ((var2 & 255) << 2))) + 32) == 23 else 0):
                                    break
                            var7 = i32_load(((var8 + (var1 << 2)) + 284636))
                            if (1 if i32_load(((var8 + (var1 << 2)) + 284636)) == 0 else 0):
                                break
                            var6 = i32_load(var7 + 8)
                            if (1 if i32_load(var7 + 8) == 0 else 0):
                                break
                            var13 = (var3 if (1 if var3 > var4 else 0) else var4)
                            var2 = 0
                            while True:  # loop $label600
                                var5 = i32_load((i32_load(var7) + (var2 << 2)))
                                if (1 if i32_load((i32_load(var7) + (var2 << 2))) == 0 else 0):
                                    break
                                var5 = (i32_load(9671128) + (var5 * 132))
                                if i32_load8_u((i32_load(9671128) + (var5 * 132)) + 129):
                                    break
                                if i32_load(var5 + 36):
                                    break
                                if i32_load8_u(var5 + 123):
                                    break
                                if (1 if i32_load8_u(9147152) == 0 else 0):
                                    if (1 if i32_load8_u((i32_load(9143008) + (i32_load16_u(var5 + 110) * (i32_load(9142892) + 1)))) == 0 else 0):
                                        break
                                    if (1 if i32_load((i32_load(9215884) + (i32_load(var5 + 44) << 4)) + 4) == 20 else 0):
                                        break
                                    if (1 if i32_load8_u(var5 + 127) == 6 else 0):
                                        break
                                    if (1 if i32_load(9142440) > var13 else 0):
                                        break
                                    break
                                if (1 if i32_load(9142440) <= var13 else 0):
                                    break
                                var10 = (i32_load16_u(var5 + 112) - var4)
                                var10 = (i32_load16_u(var5 + 114) - var3)
                                if (1 if ((((i32_load16_u(var5 + 112) - var4) * var10) + ((i32_load16_u(var5 + 114) - var3) * var10)) - 1) < 37 else 0):
                                    break
                                var6 = i32_load(var7 + 8)
                                var2 = (var2 + 1)
                                if (1 if (var2 + 1) < var6 else 0):
                                    continue
                                break  # end loop
                            var1 = (var1 + 1)
                            if (1 if (var1 + 1) != 132 else 0):
                                continue
                            break  # end loop
                        var40 = (var40 + 1)
                        if (1 if (var40 + 1) < i32_load(9142892) else 0):
                            continue
                        break  # end loop
                i32_store(9687188, (i32_load(9687188) + 1))
                global global0
                global0 = (var19 + 96)
            if (1 if ((i32_load(9142848) * 25) % 5000) == 0 else 0):
                a_b()
                var53 = 0
            if i32_load8_u(59128):
                i32_store(var0 + 16, i32_load((i32_load(9215884) + (i32_load((i32_load(9671128) + 1690568)) << 4))))
                i32_store(var0 + 20, i32_load(9142848))
            jc((i32_load(9142848) * 25))
            if i32_load8_u(9147124):
                i32_store8(9147124, 0)
            if (1 if i32_load8_u(9142904) == 0 else 0):
                break
            if i32_load8_u(9147152):
                break
            if (((i32_load(9142848) * 25) - 25) % i32_load(51788)):
                break
            i32_store(var0, i32_load(9147376))
            i32_store(var0 + 4, i32_load(9142440))
            i32_store(var0 + 8, i32_load(40608))
            i32_store(var0 + 12, i32_load(40612))
            a_b()
            i32_store(40608, 2147483647)
            i32_store(40612, -2147483647)
            i32_store8(9142904, 0)
            if i32_load8_u(9147210):
            else:
            var5 = (1 if 1 == 0 else 0)
            a_b()
            var2 = i32_load(59160)
            var1 = i32_load(9142848)
            if var5:
                break
            if (1 if var1 >= var2 else 0):
                break
            if (1 if i32_load8_u(9215872) == 0 else 0):
                break
            if ((1 if (var1 + 20) < var2 else 0) & var5):
                a_b()
            i32_store(51776, 1)
            while True:  # loop $label606
                if i32_load(51776):
                    continue
                break  # end loop
            func54(9684264)
            var2 = i32_load(59160)
            var1 = i32_load(9142848)
            if (1 if var1 < var2 else 0):
                continue
            break  # end loop
    if var53:
        a_b()
    global global0
    global0 = (var0 - -64)
    return 0

