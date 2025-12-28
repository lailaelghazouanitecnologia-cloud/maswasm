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
# $nc
# Export: nc
# ==========================================================
def nc():
    """Export: nc"""
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
    var11 = 0
    var12 = 0
    var13 = 0
    var14 = 0
    var15 = 0
    var16 = 0
    var17 = 0
    var9 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if i32_load8_u(9684336):
        a_b()
        i32_store8(9684336, 0)
    if i32_load8_u(9147152):
        func152()
        break
    if (i32_load8_u(9140304) | i32_load8_u(9140312)):
        break
    var1 = (i32_load(59160) + i32_load(40592))
    i32_store(59160, (i32_load(59160) + i32_load(40592)))
    var0 = i32_load(9682196)
    if i32_load(9682196):
        i32_store(59160, (var0 + var1))
        i32_store(9682196, 0)
    if (1 if i32_load(51776) == 0 else 0):
        break
    if i32_load8_u(9215872):
        if i32_load(9215984):
            var1 = 0
            while True:  # loop $label1
                var0 = i32_load(9215976)
                var2 = (var1 << 2)
                var1 = (var1 + 8)
                if (1 if (var1 + 8) < i32_load(9215984) else 0):
                    continue
                break  # end loop
        var1 = 0
        i32_store(9215984, 0)
        if i32_load(9216000):
            while True:  # loop $label2
                var0 = (i32_load(9215992) + (var1 << 2))
                var1 = (var1 + 3)
                if (1 if (var1 + 3) < i32_load(9216000) else 0):
                    continue
                break  # end loop
        var1 = 0
        i32_store(9216000, 0)
        if i32_load(9216016):
            while True:  # loop $label3
                var0 = i32_load(9216008)
                var2 = (var1 << 2)
                qc(i32_load((i32_load(9216008) + (var1 << 2))), (1 if i32_load((var0 + (var2 | 4))) != 0 else 0))
                var1 = (var1 + 2)
                if (1 if (var1 + 2) < i32_load(9216016) else 0):
                    continue
                break  # end loop
        var1 = 0
        i32_store(9216016, 0)
        if i32_load(9216032):
            while True:  # loop $label4
                var0 = i32_load(9216024)
                var2 = (var1 << 2)
                var1 = (var1 + 4)
                if (1 if (var1 + 4) < i32_load(9216032) else 0):
                    continue
                break  # end loop
        i32_store(9216032, 0)
        i32_store8(9215872, 0)
    var1 = i32_load(9142848)
    if (1 if i32_load8_u(9147210) == 0 else 0):
        break
    if (1 if var1 == 0 else 0):
        break
    if ((var1 * 25) % 250):
        break
    if (1 if var1 <= i32_load(59148) else 0):
        break
    if ((1 if i32_load8_u(9142388) == 0 else 0) | (1 if i32_load8_u(9147125) == 0 else 0)):
        if (1 if i32_load(59176) < var1 else 0):
            break
    var1 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    if (1 if i32_load(9561792) == 0 else 0):
        break
    while True:  # loop $label25
        var0 = i32_load(9561784)
        var2 = (var10 << 2)
        var3 = (i32_load(9561784) + (var10 << 2))
        var5 = i32_load((i32_load(9561784) + (var10 << 2)))
        if (1 if i32_load((i32_load(9561784) + (var10 << 2))) == 0 else 0):
            break
        if (1 if i32_load(9142848) != i32_load((var0 + (var2 | 4))) else 0):
            break
        var14 = i32_load((var0 + (var2 | 28)))
        var15 = i32_load((var0 + (var2 | 24)))
        var16 = i32_load((var0 + (var2 | 20)))
        var6 = i32_load((var0 + (var2 | 16)))
        var11 = i32_load((var0 + (var2 | 12)))
        var12 = i32_load((var0 + (var2 | 8)))
        i32_store(var3, 0)
        var2 = i32_load(9142892)
        var4 = (1 if i32_load(9142892) < 2 else 0)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var3 = i32_load(9561692)
        var0 = 1
        while True:  # loop $label10
            if var12:
                if (1 if i32_load((var3 + (var0 * 286704)) + 283948) == var12 else 0):
                    break
            if var6:
                if (1 if i32_load((var3 + (var0 * 286704)) + 283952) == var6 else 0):
                    break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var2 else 0):
                continue
            break
            break  # end loop
        var3 = i32_load((var3 + (var0 * 286704)) + 283908)
        if i32_load((var3 + (var0 * 286704)) + 283908):
            break
        if var4:
            break
        var3 = i32_load(9561692)
        var0 = 1
        while True:  # loop $label18
            var4 = (var3 + (var0 * 286704))
            if (1 if i32_load((var3 + (var0 * 286704)) + 283976) == 0 else 0):
                if i32_load8_u(var4 + 286699):
                    break
            if i32_load(var4 + 284616):
                break
            var3 = i32_load(var4 + 283908)
            var0 = i32_load(var4 + 281800)
            if i32_load(var4 + 281800):
                i32_store((var4 + 281800), 0)
                var2 = i32_load(9142892)
            var0 = 1
            if (1 if var2 >= 2 else 0):
                while True:  # loop $label15
                    if (1 if var0 != var3 else 0):
                        func176(var3, var0, 1)
                        var2 = i32_load(9142892)
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) < var2 else 0):
                        continue
                    break  # end loop
            var0 = i32_load(9142384)
            if (1 if var3 == 0 else 0):
                break
            break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var2 else 0):
                continue
            break  # end loop
        if (1 if var5 == i32_load(9142384) else 0):
            break
        break
        if (1 if var0 != var5 else 0):
            break
        break
        var2 = (1 if var5 == i32_load(9142384) else 0)
        i32_store(var1 + 68, var5)
        var0 = (i32_load(9561692) + (var3 * 286704))
        i32_store(var1 + 64, (i32_load(9561692) + (var3 * 286704)))
        i32_store(var1 + 52, var5)
        i32_store(var1 + 48, (var0 + 80))
        i32_store(var0 + 283952, var6)
        i32_store(var0 + 283948, var12)
        i32_store(var0 + 284616, var5)
        i32_store(var0 + 283964, var15)
        i32_store8(var0 + 92, var16)
        i32_store8(var0 + 286699, 0)
        i32_store8(var0 + 93, var14)
        i32_store8((var0 + 283974), var11)
        i32_store8((var0 + 283973), ((var11 & 0xFFFFFFFF) >> 8))
        i32_store8(var0 + 283972, ((var11 & 0xFFFFFFFF) >> 16))
        if var2:
            i32_store(9142872, i32_load(var0 + 283908))
            var4 = i32_load(9142892)
            if (1 if i32_load(9142892) >= 2 else 0):
                var6 = i32_load(9561692)
                var2 = 1
                while True:  # loop $label20
                    var3 = (var6 + (var2 * 286704))
                    var11 = i32_load((var6 + (var2 * 286704)) + 284616)
                    if i32_load((var6 + (var2 * 286704)) + 284616):
                        var4 = i32_load8_u(var3 + 92)
                        var6 = i32_load(var3 + 283948)
                        var12 = i32_load8_u(var3 + 283972)
                        var14 = i32_load8_u((var3 + 283974))
                        var15 = i32_load8_u((var3 + 283973))
                        var16 = i32_load(var3 + 283964)
                        var17 = i32_load8_u(var3 + 93)
                        i32_store(var1 + 40, (var3 + 80))
                        i32_store(var1 + 36, var17)
                        i32_store(var1 + 32, var16)
                        i32_store(var1 + 44, ((var14 | (var15 << 8)) | (var12 << 16)))
                        i32_store(var1 + 28, var6)
                        i32_store(var1 + 24, var4)
                        i32_store(var1 + 20, var3)
                        i32_store(var1 + 16, var11)
                        var6 = i32_load(9561692)
                        var4 = i32_load(9142892)
                    var2 = (var2 + 1)
                    if (1 if (var2 + 1) < var4 else 0):
                        continue
                    break  # end loop
            func346()
            if (1 if i32_load(var0 + 283976) == 0 else 0):
                break
            var0 = i32_load(((var0 + (i32_load(9671152) << 2)) + 284636))
            if (1 if i32_load(((var0 + (i32_load(9671152) << 2)) + 284636)) == 0 else 0):
                break
            var2 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var3 = i32_load(var0)
            var0 = 0
            while True:  # loop $label22
                var4 = i32_load((var3 + (var0 << 2)))
                if (1 if i32_load((var3 + (var0 << 2))) == 0 else 0):
                    var0 = (var0 + 1)
                    if (1 if var2 != (var0 + 1) else 0):
                        continue
                    break
                break  # end loop
            if i32_load8_u(9142917):
                break
            var0 = i32_load(9671128)
            var0 = (var0 + (var4 * 132))
            var2 = i32_load((var0 + (var4 * 132)) + 36)
            var0 = (i32_load(9671128) + ((i32_load((var0 + (var4 * 132)) + 36) if var2 else i32_load(var0 + 28)) * 132))
            var2 = ((i32_load8_u((i32_load(9671128) + ((i32_load((var0 + (var4 * 132)) + 36) if var2 else i32_load(var0 + 28)) * 132)) + 122) * 404) + 9568096)
            var3 = i32_load(((i32_load8_u((i32_load(9671128) + ((i32_load((var0 + (var4 * 132)) + 36) if var2 else i32_load(var0 + 28)) * 132)) + 122) * 404) + 9568096) + 220)
            var4 = i32_load16_u(var0 + 114)
            i32_store(var1, (((i32_load(var2 + 216) << 4) & 2147483632) + (i32_load16_u(var0 + 112) << 5)))
            i32_store(var1 + 4, (((var3 << 4) & 2147483632) + (var4 << 5)))
            if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
                break
            if i32_load8_u(9147152):
                break
            var4 = i32_load(9671136)
            if (1 if i32_load(9671136) < 4 else 0):
                break
            var6 = i32_load(9671128)
            var2 = 3
            while True:  # loop $label24
                var0 = (var6 + (var2 * 132))
                if (1 if i32_load8_u((var6 + (var2 * 132)) + 125) == 3 else 0):
                    break
                if (1 if i32_load(var0 + 28) == 0 else 0):
                    break
                if i32_load(var0 + 36):
                    break
                var4 = i32_load(9671136)
                var6 = i32_load(9671128)
                var2 = (var2 + 1)
                if (1 if (var2 + 1) < var4 else 0):
                    continue
                break  # end loop
            break
        var13 = (var13 + (1 if var5 != 0 else 0))
        var10 = (var10 + 8)
        if (1 if (var10 + 8) < i32_load(9561792) else 0):
            continue
        break  # end loop
    if var13:
        break
    i32_store(9561792, 0)
    global global0
    global0 = (var1 + 80)
    if i32_load8_u(9147125):
        break
    if (1 if i32_load(9561776) == 0 else 0):
        break
    var1 = i32_load(9561768)
    while True:  # loop $label29
        var3 = (var8 << 2)
        var5 = i32_load((var1 + (var8 << 2)))
        var4 = (1 if i32_load((var1 + (var8 << 2))) != 0 else 0)
        if (1 if var5 == 0 else 0):
            break
        if (1 if i32_load((var1 + (var3 | 4))) != i32_load(9142848) else 0):
            break
        var6 = i32_load(9142892)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var10 = i32_load(9561692)
        var2 = 1
        while True:  # loop $label28
            var0 = (var10 + (var2 * 286704))
            if (1 if var5 == i32_load((var10 + (var2 * 286704)) + 284616) else 0):
                i32_store((var1 + var3), 0)
                if i32_load(9147132):
                    i32_store8(var0 + 286699, 1)
                    break
                var1 = (var0 + 284616)
                i32_store(var0 + 284628, i32_load((var0 + 284616)))
                i32_store(var1, 0)
                var1 = i32_load(9561768)
                break
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var6 else 0):
                continue
            break  # end loop
        var7 = (var4 + var7)
        var8 = (var8 + 2)
        if (1 if (var8 + 2) < i32_load(9561776) else 0):
            continue
        break  # end loop
    if var7:
        break
    i32_store(9561776, 0)
    var1 = i32_load(59172)
    var0 = (i32_load(9561696) + (i32_load(59172) << 2))
    var3 = i32_load((i32_load(9561696) + (i32_load(59172) << 2)) + 8)
    if (1 if i32_load((i32_load(9561696) + (i32_load(59172) << 2)) + 8) >= 4 else 0):
        var1 = 3
        while True:  # loop $label31
            var2 = (var0 + (var1 << 2))
            i32_store(59164, i32_load((var0 + (var1 << 2))))
            var7 = i32_load(var2 + 8)
            var5 = (var1 + 4)
            var8 = (i32_load(var2 + 8) + (var1 + 4))
            var4 = i32_load(var2 + 12)
            var1 = ((i32_load(var2 + 8) + (var1 + 4)) + i32_load(var2 + 12))
            var2 = i32_load(var2 + 4)
            if (1 if i32_load(var2 + 4) > 255 else 0):
                break
            var2 = ((var2 << 3) + 9213824)
            var6 = i32_load(((var2 << 3) + 9213824))
            if (1 if i32_load(((var2 << 3) + 9213824)) == 0 else 0):
                break
            var8 = ((var0 + (var8 << 2)) if var4 else 0)
            var5 = ((var0 + (var5 << 2)) if var7 else 0)
            var4 = i32_load(var2 + 4)
            if i32_load(var2 + 4):
                # call_indirect via table[var4]
                if (1 if call_indirect(var4) == 0 else 0):
                    break
            else:
            # call_indirect via table[var6]
            i32_store(59164, 0)
            if (1 if var1 < var3 else 0):
                continue
            break  # end loop
    else:
    i32_store(i32_load(59172), (var1 + var3))
    var1 = i32_load(9142848)
    if (1 if i32_load(9147132) == 0 else 0):
        break
    if i32_load8_u(9684337):
        break
    if (1 if var1 < 11 else 0):
        break
    if (1 if i32_load(59160) > (var1 + 1) else 0):
        break
    a_b()
    i32_store8(9684337, 1)
    if i32_load((i32_load(9561692) + (i32_load(9142872) * 286704)) + 283976):
        break
    Za()
    if (1 if i32_load(51776) == 2 else 0):
        i32_store(51776, 0)
        func231(var9)
        i32_store(var9 + 12, 1)
        func186((var9 + 44), var9, 66, 0)
        break
    i32_store(51776, 0)
    if (1 if i32_load(9684288) == 0 else 0):
        var8 = 0
        var7 = -1
        var0 = (global0 - 16)
        global global0
        global0 = (global0 - 16)
        i32_store(var0 + 12, 0)
        func175(9684320)
        var1 = i32_load(9684308)
        var2 = (1 if i32_load(9684308) != 0 else 0)
        if (1 if var1 == 0 else 0):
            break
        while True:  # loop $label35
            if 1:
                i32_store(var0 + 12, (i32_load(var0 + 12) + 1))
                i32_store(var1 + 16, (var0 + 12))
                break
            var8 = (var8 if var8 else var1)
            var7 = (var7 - 1)
            var1 = i32_load(var1)
            var2 = (1 if i32_load(var1) != 0 else 0)
            if (1 if var7 == 0 else 0):
                break
            if var1:
                continue
            break  # end loop
        if var2:
            var7 = (var1 + 4)
            var2 = i32_load(var1 + 4)
            if (1 if i32_load(var1 + 4) == 0 else 0):
                break
            i32_store(var2, 0)
            break
        var7 = 9684292
        i32_store(var7, 0)
        i32_store(9684308, var1)
        func154(9684320)
        var1 = i32_load(var0 + 12)
        if i32_load(var0 + 12):
            while True:  # loop $label37
                var1 = i32_load(var0 + 12)
                if i32_load(var0 + 12):
                    continue
                break  # end loop
        if var8:
            func154((var8 + 12))
        global global0
        global0 = (var0 + 16)
        break
    if i32_load(9684300):
        func111(9684296, 2147483647)
    func54(9684264)
    global global0
    global0 = (var9 + 48)
    return 9684296

