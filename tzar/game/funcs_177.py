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
# $func811
# ==========================================================
def func811(var0, var1):
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
    # br_table ['$label0', '$label1', '$label2']
    _br_idx = (var0 - 1)
    break  # br_table
    break
    var0 = global3
    var15 = var0
    if (1 if var0 == global3 else 0):
    else:
    if 0:
    else:
        var6 = (global0 - 32)
        global global0
        global0 = (global0 - 32)
        i32_store(var6 + 28, var1)
        i32_store(var6 + 16, var1)
        i32_store(var6 + 24, 0)
        i32_store(var6 + 20, 422)
        i64_store(var6 + 8, i64_load(var6 + 20))
        var9 = (global0 - 16)
        global global0
        global0 = (global0 - 16)
        var0 = func372(9688236, var15)
        if (1 if func372(9688236, var15) == 0 else 0):
            var0 = i32_load(9688264)
            if (1 if i32_load(9688264) == i32_load(9688268) else 0):
                var16 = ((var0 << 1) if var0 else 1)
                var7 = (((var0 << 1) if var0 else 1) << 2)
                var0 = 0
                var10 = i32_load(9688260)
                if (1 if i32_load(9688260) == 0 else 0):
                    break
                if (1 if var7 >= -64 else 0):
                    i32_store(global3 + 28, 48)
                    break
                if (i32_load8_u(9690908) & 2):
                    if func55(9690912):
                        break
                var4 = (16 if (1 if var7 < 11 else 0) else ((var7 + 11) & -8))
                var1 = (var10 - 8)
                var8 = i32_load((var10 - 8) + 4)
                var2 = (i32_load((var10 - 8) + 4) & -8)
                if (1 if (var8 & 3) == 0 else 0):
                    if (1 if var4 < 256 else 0):
                        break
                    if (1 if (var4 + 4) <= var2 else 0):
                        var0 = var1
                        if (1 if (var2 - var4) <= (i32_load(9690448) << 1) else 0):
                            break
                    break
                var5 = (var1 + var2)
                if (1 if var2 >= var4 else 0):
                    var0 = (var2 - var4)
                    if (1 if (var2 - var4) < 16 else 0):
                        break
                    i32_store(var1 + 4, (((var8 & 1) | var4) | 2))
                    var2 = (var1 + var4)
                    i32_store((var1 + var4) + 4, (var0 | 3))
                    i32_store(var5 + 4, (i32_load(var5 + 4) | 1))
                    break
                if (1 if i32_load(9690488) == var5 else 0):
                    var2 = (i32_load(9690476) + var2)
                    if (1 if (i32_load(9690476) + var2) <= var4 else 0):
                        break
                    i32_store(var1 + 4, (((var8 & 1) | var4) | 2))
                    var0 = (var1 + var4)
                    var2 = (var2 - var4)
                    i32_store((var1 + var4) + 4, ((var2 - var4) | 1))
                    i32_store(9690476, var2)
                    i32_store(9690488, var0)
                    break
                if (1 if i32_load(9690484) == var5 else 0):
                    var2 = (i32_load(9690472) + var2)
                    if (1 if (i32_load(9690472) + var2) < var4 else 0):
                        break
                    var0 = (var2 - var4)
                    if (1 if (var2 - var4) >= 16 else 0):
                        i32_store(var1 + 4, (((var8 & 1) | var4) | 2))
                        var3 = (var1 + var4)
                        i32_store((var1 + var4) + 4, (var0 | 1))
                        var2 = (var1 + var2)
                        i32_store((var1 + var2), var0)
                        i32_store(var2 + 4, (i32_load(var2 + 4) & -2))
                        break
                    i32_store(var1 + 4, (((var8 & 1) | var2) | 2))
                    var0 = (var1 + var2)
                    i32_store((var1 + var2) + 4, (i32_load(var0 + 4) | 1))
                    var0 = 0
                    i32_store(9690484, var3)
                    i32_store(9690472, var0)
                    break
                var3 = i32_load(var5 + 4)
                if (i32_load(var5 + 4) & 2):
                    break
                var11 = ((var3 & -8) + var2)
                if (1 if ((var3 & -8) + var2) < var4 else 0):
                    break
                var13 = (var11 - var4)
                if (1 if var3 <= 255 else 0):
                    var0 = i32_load(var5 + 12)
                    var2 = i32_load(var5 + 8)
                    if (1 if i32_load(var5 + 12) == i32_load(var5 + 8) else 0):
                        i32_store(9690464, (i32_load(9690464) & rotl32(-2, ((var3 & 0xFFFFFFFF) >> 3))))
                        break
                    i32_store(var2 + 12, var0)
                    i32_store(var0 + 8, var2)
                    break
                var12 = i32_load(var5 + 24)
                var2 = i32_load(var5 + 12)
                if (1 if var5 != i32_load(var5 + 12) else 0):
                    var0 = i32_load(var5 + 8)
                    i32_store(i32_load(var5 + 8) + 12, var2)
                    i32_store(var2 + 8, var0)
                    break
                var3 = (var5 + 20)
                var0 = i32_load((var5 + 20))
                if i32_load((var5 + 20)):
                    break
                var3 = (var5 + 16)
                var0 = i32_load((var5 + 16))
                if i32_load((var5 + 16)):
                    break
                var2 = 0
                break
                while True:  # loop $label13
                    var14 = var3
                    var2 = var0
                    var3 = (var0 + 20)
                    var0 = i32_load((var0 + 20))
                    if i32_load((var0 + 20)):
                        continue
                    var3 = (var2 + 16)
                    var0 = i32_load(var2 + 16)
                    if i32_load(var2 + 16):
                        continue
                    break  # end loop
                i32_store(var14, 0)
                if (1 if var12 == 0 else 0):
                    break
                var0 = i32_load(var5 + 28)
                var3 = ((i32_load(var5 + 28) << 2) + 9690768)
                if (1 if i32_load(((i32_load(var5 + 28) << 2) + 9690768)) == var5 else 0):
                    i32_store(var3, var2)
                    if var2:
                        break
                    i32_store(9690468, (i32_load(9690468) & rotl32(-2, var0)))
                    break
                i32_store((var12 + (16 if (1 if i32_load(var12 + 16) == var5 else 0) else 20)), var2)
                if (1 if var2 == 0 else 0):
                    break
                i32_store(var2 + 24, var12)
                var0 = i32_load(var5 + 16)
                if i32_load(var5 + 16):
                    i32_store(var2 + 16, var0)
                    i32_store(var0 + 24, var2)
                var0 = i32_load(var5 + 20)
                if (1 if i32_load(var5 + 20) == 0 else 0):
                    break
                i32_store(var2 + 20, var0)
                i32_store(var0 + 24, var2)
                if (1 if var13 <= 15 else 0):
                    i32_store(var1 + 4, (((var8 & 1) | var11) | 2))
                    var0 = (var1 + var11)
                    i32_store((var1 + var11) + 4, (i32_load(var0 + 4) | 1))
                    break
                i32_store(var1 + 4, (((var8 & 1) | var4) | 2))
                var0 = (var1 + var4)
                i32_store((var1 + var4) + 4, (var13 | 3))
                var2 = (var1 + var11)
                i32_store((var1 + var11) + 4, (i32_load(var2 + 4) | 1))
                var0 = var1
                var0 = var0
                if (i32_load8_u(9690908) & 2):
                    func54(9690912)
                if var0:
                    break
                var0 = e()
                if (1 if e() == 0 else 0):
                    break
                var1 = i32_load((var10 - 4))
                var1 = ((-4 if (i32_load((var10 - 4)) & 3) else -8) + (var1 & -8))
                var0 = var0
                if (1 if var0 == 0 else 0):
                    break
                i32_store(9688268, var16)
                i32_store(9688260, var0)
            var0 = func393(var15)
            if (1 if func393(var15) == 0 else 0):
                break
            var1 = i32_load(9688264)
            i32_store(9688264, (i32_load(9688264) + 1))
            i32_store((i32_load(9688260) + (var1 << 2)), var0)
        break
        var1 = 0
        func54(9688236)
        if var1:
            i32_store(var9 + 8, i32_load(var6 + 16))
            i64_store(var9, i64_load(var6 + 8))
            var0 = (global0 - 48)
            global global0
            global0 = (global0 - 48)
            var3 = i32_load(var1 + 28)
            var2 = i32_atomic_load(i32_load(var1 + 28) + 124)
            while True:  # loop $label18
                if (1 if var2 == 0 else 0):
                    break
                var2 = (var2 + 1)
                if (1 if var2 != (var2 + 1) else 0):
                    continue
                break  # end loop
            if 1:
                var2 = (var1 + 4)
                i32_store(var0 + 32, i32_load(var9 + 8))
                i64_store(var0 + 24, i64_load(var9))
                var3 = func391(var1, (var0 + 24))
                func54(var2)
                if var3:
                    var3 = 2
                    var2 = i32_load(var1 + 28)
                    if (1 if var3 == 2 else 0):
                        break
                    i32_store(var0 + 44, var1)
                    i32_store(var0 + 16, var1)
                    i32_store(var0 + 40, 423)
                    i32_store(var0 + 36, 424)
                    i64_store(var0 + 8, i64_load(var0 + 36))
                    var3 = (global0 - 16)
                    global global0
                    global0 = (global0 - 16)
                    var14 = i32_load(var2 + 120)
                    i32_store(var3 + 8, i32_load(var0 + 16))
                    i64_store(var3, i64_load(var0 + 8))
                    func54((i32_load(var2 + 120) + 4))
                    if (1 if 2 == 2 else 0):
                        break
                    if i32_atomic_load(var2 + 128):
                        break
                    a_u()
                    global global0
                    global0 = (var3 + 16)
                var1 = i32_load(var1 + 28)
                if (1 if 1 == 1 else 0):
                    func111((var1 + 124), 2147483647)
            global global0
            global0 = (var0 + 48)
        global global0
        global0 = (var9 + 16)
        global global0
        global0 = (var6 + 32)
    return 0


# ==========================================================
# $func814
# ==========================================================
def func814(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var4 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var3 = i32_load(9142892)
    if i32_load8_u(9147210):
        if (1 if var3 < 2 else 0):
            break
        var2 = i32_load(59164)
        var6 = i32_load(9561692)
        var1 = 1
        while True:  # loop $label2
            var5 = (var6 + (var1 * 286704))
            if (1 if i32_load((var6 + (var1 * 286704)) + 284616) == var2 else 0):
                break
            if (1 if i32_load(var5 + 284628) == var2 else 0):
                break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var3 else 0):
                continue
            break  # end loop
        var1 = 0
        break
    var1 = i32_load(9142872)
    if (1 if var3 < 2 else 0):
        break
    var5 = i32_load(var0)
    var6 = i32_load(9561692)
    var2 = 1
    while True:  # loop $label4
        var7 = (var6 + (var2 * 286704))
        if (1 if i32_load((var6 + (var2 * 286704)) + 284616) == var5 else 0):
            break
        if (1 if i32_load(var7 + 284628) == var5 else 0):
            break
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var3 else 0):
            continue
        break
        break  # end loop
    if (1 if var2 >= var3 else 0):
        break
    if (1 if var1 == var2 else 0):
        break
    if (1 if i32_load(9147136) == 0 else 0):
        break
    var11 = i32_load(var0 + 4)
    var9 = (var6 + (var2 * 286704))
    var8 = ((var6 + (var2 * 286704)) + 281800)
    var0 = i32_load(var9 + 281800)
    if (1 if i32_load(var9 + 281800) == 0 else 0):
        var5 = (-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2))
        var0 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
        # Unknown: memory.fill []
        i32_store(var8, var0)
    var5 = (var6 + (var1 * 286704))
    var10 = ((var6 + (var1 * 286704)) + 281800)
    var7 = i32_load(var5 + 281800)
    if i32_load(var5 + 281800):
    else:
        var0 = (-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2))
        var7 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
        # Unknown: memory.fill []
        i32_store(var10, var7)
    var0 = i32_load((i32_load(var8) + (var1 << 2)))
    if i32_load((i32_load(var8) + (var1 << 2))):
        if (1 if ((i32_load(9142848) - var0) * 25) < 60000 else 0):
            break
    var0 = i32_load8_u((i32_load(9143004) + (var2 + (var1 * var3))))
    if (1 if var11 == 0 else 0):
        if var0:
            break
        if (1 if i32_load(9142872) != var2 else 0):
            break
        var0 = (var6 + (var1 * 286704))
        var3 = i32_load((var6 + (var1 * 286704)) + 284628)
        var0 = i32_load(var0 + 284616)
        i32_store(var4 + 4, var5)
        i32_store(var4, 914)
        i32_store(var4 + 8, (var0 if var0 else var3))
        a_b()
        func176(var2, var1, 1)
        break
    if (1 if var0 == 0 else 0):
        break
    if (1 if i32_load(9147132) == 0 else 0):
        break
    if (1 if i32_load(9142440) != 4096 else 0):
        break
    if (1 if func385(var5) > 2 else 0):
        break
    var7 = i32_load(var10)
    if i32_load((var7 + (var2 << 2))):
        if (1 if i32_load(9147132) == 0 else 0):
            break
        if (1 if i32_load(9142440) != 4096 else 0):
            break
        if (1 if func385(var9) < 3 else 0):
            break
        a_b()
        break
        func176(var2, var1, 0)
        if (1 if i32_load(9142872) != var2 else 0):
            break
        var0 = (var6 + (var1 * 286704))
        var1 = i32_load((var6 + (var1 * 286704)) + 284628)
        var0 = i32_load(var0 + 284616)
        i32_store(var4 + 36, var5)
        i32_store(var4 + 32, 916)
        i32_store(var4 + 40, (var0 if var0 else var1))
        a_b()
        break
    i32_store((i32_load(var8) + (var1 << 2)), i32_load(9142848))
    if (1 if i32_load(9142872) != var2 else 0):
        break
    i32_store(var4 + 16, i32_load((var6 + (var1 * 286704)) + 284616))
    a_b()
    global global0
    global0 = (var4 + 48)
    return (var4 + 16)


# ==========================================================
# $func819
# ==========================================================
def func819(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    if (1 if var1 == -1 else 0):
        break
    if var1:
        func38(var1)
    if (1 if i32_load(i32_load(9142424) + 48) < 2 else 0):
        break
    var6 = i32_load(9142836)
    var7 = i32_load(i32_load(9142836) + 964)
    if (1 if i32_load(i32_load(9142836) + 964) == 0 else 0):
        break
    var8 = ((var0 & 0xFFFFFFFF) >> 16)
    var9 = (var0 & 65535)
    var0 = i32_load(9142440)
    var1 = 0
    while True:  # loop $label2
        var2 = i32_load(var6 + 960)
        var3 = (var1 << 2)
        var4 = i32_load((i32_load(var6 + 960) + ((var1 << 2) | 4)))
        var5 = (i32_load((i32_load(var6 + 960) + ((var1 << 2) | 4))) + var8)
        if (1 if var0 <= (i32_load((i32_load(var6 + 960) + ((var1 << 2) | 4))) + var8) else 0):
            break
        var2 = i32_load((var2 + var3))
        var3 = (i32_load((var2 + var3)) + var9)
        if (1 if var0 <= (i32_load((var2 + var3)) + var9) else 0):
            break
        if (1 if (var3 | var5) < 0 else 0):
            break
        if (1 if (((var2 * var2) + (var4 * var4)) - 1) > 64 else 0):
            break
        var0 = i32_load(9142440)
        var1 = (var1 + 2)
        if (1 if (var1 + 2) < var7 else 0):
            continue
        break  # end loop

