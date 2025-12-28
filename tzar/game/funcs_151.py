"""
Auto-generated from WAT. Contains 4 functions.
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
# $func620
# ==========================================================
def func620(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i64_store(var1 + 8, 0)
    var0 = i32_load(9213808)
    if i32_load8_u(9147210):
        func41(38, 9173808, var0, (var1 + 8), 2)
        break
    var3 = (var0 << 2)
    var2 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var0:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9214128)]
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $func624
# ==========================================================
def func624(var0, var1):
    var2 = 0
    var3 = 0
    var3 = i32_load(9561692)
    var1 = (i32_load(9561692) + (var0 * 286704))
    if i32_load((((i32_load(9561692) + (var0 * 286704)) + (i32_load(38452) << 2)) + 281808)):
        break
    var2 = (i32_load(var1 + 283868) + 1)
    i32_store(var1 + 283868, (i32_load(var1 + 283868) + 1))
    if (1 if var2 >= (i32_load((var1 + 284372)) + (i32_load((var1 + 284380)) * i32_load(var1 + 283864))) else 0):
        break
    var1 = (var3 + (var0 * 286704))
    if (1 if var2 >= i32_load(((var3 + (var0 * 286704)) + 284376)) else 0):
        break
    var0 = 0
    var1 = i32_load(9213808)
    if (1 if i32_load(9213808) == 0 else 0):
        break
    var2 = i32_load(38464)
    var3 = i32_load(9671128)
    while True:  # loop $label2
        if (1 if i32_load8_u((var3 + (i32_load(((var0 << 2) + 9173808)) * 132)) + 122) != var2 else 0):
            var0 = (var0 + 1)
            if (1 if var1 != (var0 + 1) else 0):
                continue
            break
        break  # end loop


# ==========================================================
# $Sa
# Export: Sa
# ==========================================================
def Sa(var0, var1):
    """Export: Sa"""
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
    var7 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    if (i32_load8_u(9147212) | i32_load8_u(9147210)):
        if (1 if i32_load(9142892) == 0 else 0):
            break
        i32_store(9142892, 0)
        var2 = i32_load(9561692)
        if i32_load(9561692):
            i32_store(9561692, 0)
    var4 = i32_load(9142892)
    if i32_load(9142892):
        break
    var4 = 6
    var2 = 0
    var0 = (var0 + var4)
    var5 = (2 if (1 if var0 <= 2 else 0) else (var0 + var4))
    i32_store(9142892, (2 if (1 if var0 <= 2 else 0) else (var0 + var4)))
    var0 = i32_load(9561692)
    var11 = (i64_extend_u(var5) * 286704)
    var6 = (-1 if i32(((var11 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var5) * 286704)))
    var3 = func26((-1 if i32(((var11 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var5) * 286704))))
    # Unknown: memory.fill []
    if var0:
        var5 = (var5 if (1 if var4 > var5 else 0) else var4)
        var4 = ((var5 if (1 if var4 > var5 else 0) else var4) & 3)
        if (1 if (var5 - 1) >= 3 else 0):
            var6 = (var5 & 2147483644)
            var5 = 0
            while True:  # loop $label2
                var8 = (var2 * 286704)
                # Unknown: memory.copy []
                var8 = ((var2 | 1) * 286704)
                # Unknown: memory.copy []
                var8 = ((var2 | 2) * 286704)
                # Unknown: memory.copy []
                var8 = ((var2 | 3) * 286704)
                # Unknown: memory.copy []
                var2 = (var2 + 4)
                var5 = (var5 + 4)
                if (1 if (var5 + 4) != var6 else 0):
                    continue
                break  # end loop
        if var4:
            var5 = 0
            while True:  # loop $label3
                var6 = (var2 * 286704)
                # Unknown: memory.copy []
                var2 = (var2 + 1)
                var5 = (var5 + 1)
                if (1 if (var5 + 1) != var4 else 0):
                    continue
                break  # end loop
        var5 = i32_load(9142892)
    i32_store(9561692, var3)
    i32_store(var7 + 32, (var5 - 1))
    if (1 if i32_load(9142892) >= 2 else 0):
        var0 = 1
        while True:  # loop $label10
            var2 = (i32_load(9561692) + (var0 * 286704))
            var8 = ((i32_load(9561692) + (var0 * 286704)) + 283908)
            if i32_load(var2 + 283908):
                var5 = (var0 - 1)
                var4 = i32_load8_u(var2 + 283972)
                var6 = i32_load8_u((var2 + 283973))
                var3 = i32_load8_u((var2 + 283974))
                break
            i64_store(var2 + 283848, 1717986918800)
            var5 = (var0 - 1)
            i32_store(var2 + 284608, ((((var0 - 1) & 0xFFFFFFFF) // 3) + 1))
            i64_store((var2 + 283856), 1717986918800)
            if (1 if var0 <= 1 else 0):
                i32_store16(var2, i32_load16_u(9563904))
                i32_store16(var2 + 2, i32_load16_u(9563906))
                i32_store16(var2 + 4, i32_load16_u(9563908))
                i32_store16(var2 + 6, i32_load16_u(9563910))
                i32_store16(var2 + 8, i32_load16_u(9563912))
                i32_store16(var2 + 10, i32_load16_u(9563914))
                i32_store16(var2 + 12, i32_load16_u(9563916))
                i32_store16(var2 + 14, i32_load16_u(9563918))
                i32_store16(var2 + 16, i32_load16_u(9563920))
                i32_store16(var2 + 18, i32_load16_u(9563922))
                i32_store16(var2 + 20, i32_load16_u(9563924))
                i32_store16(var2 + 22, i32_load16_u(9563926))
                i32_store16(var2 + 24, i32_load16_u(9563928))
                i32_store16(var2 + 26, i32_load16_u(9563930))
                i32_store16(var2 + 28, i32_load16_u(9563932))
                i32_store16(var2 + 30, i32_load16_u(9563934))
                i32_store16(var2 + 32, i32_load16_u(9563936))
                i32_store16(var2 + 34, i32_load16_u(9563938))
                i32_store16(var2 + 36, i32_load16_u(9563940))
                i32_store16(var2 + 38, i32_load16_u(9563942))
                var3 = i32_load(9563944)
                if (1 if var1 >= 3 else 0):
                    break
                i32_store(var2 + 283960, var1)
                break
            var11 = i64_load(9147316)
            var3 = i32_load(9147312)
            i32_store(9147316, i32_load(9147312))
            var4 = i32_load(9147324)
            i64_store(9147320, var11)
            var4 = (var4 ^ (var4 << 11))
            var3 = ((var3 ^ (((var3 & 0xFFFFFFFF) >> 19) ^ (((var4 ^ (var4 << 11)) & 0xFFFFFFFF) >> 8))) ^ var4)
            i32_store(9147312, ((var3 ^ (((var3 & 0xFFFFFFFF) >> 19) ^ (((var4 ^ (var4 << 11)) & 0xFFFFFFFF) >> 8))) ^ var4))
            i32_store(var2 + 283960, (var3 % 3))
            var6 = (var2 + 283960)
            if (1 if var0 <= 8 else 0):
                break
            var11 = i64_load(9147316)
            var3 = i32_load(9147312)
            i32_store(9147316, i32_load(9147312))
            var4 = i32_load(9147324)
            i64_store(9147320, var11)
            var4 = (var4 ^ (var4 << 11))
            var3 = ((var3 ^ (((var3 & 0xFFFFFFFF) >> 19) ^ (((var4 ^ (var4 << 11)) & 0xFFFFFFFF) >> 8))) ^ var4)
            i32_store(9147312, ((var3 ^ (((var3 & 0xFFFFFFFF) >> 19) ^ (((var4 ^ (var4 << 11)) & 0xFFFFFFFF) >> 8))) ^ var4))
            var3 = (var3 % 16777215)
            # br_table ['$label7', '$label8', '$label9', '$label5']
            _br_idx = i32_load(var6)
            break  # br_table
            i32_store(var2 + 283964, i32_load(((((i32_load(9561840) + var3) & 31) << 2) + 1472)))
            break
            i32_store(var2 + 283964, i32_load(((((i32_load(9561840) + var3) % 15) << 2) + 1600)))
            break
            i32_store(var2 + 283964, i32_load(((((i32_load(9561840) + var3) % 17) << 2) + 1664)))
            var4 = ((var3 & 0xFFFFFFFF) >> 16)
            i32_store8(var2 + 283972, ((var3 & 0xFFFFFFFF) >> 16))
            i32_store8((var2 + 283974), var3)
            var6 = ((var3 & 0xFFFFFFFF) >> 8)
            i32_store8((var2 + 283973), ((var3 & 0xFFFFFFFF) >> 8))
            var9 = i32_load(var2 + 284608)
            var10 = i32_load(var2 + 283960)
            i32_store(var7 + 16, var5)
            i32_store(var7 + 8, var10)
            i32_store(var7 + 4, var9)
            i32_store(var7, var2)
            i32_store(var7 + 12, (((var3 & 255) | ((var6 & 255) << 8)) | ((var4 & 255) << 16)))
            i32_store(var8, var0)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < i32_load(9142892) else 0):
                continue
            break  # end loop
    global global0
    global0 = (var7 + 48)
    return var7


# ==========================================================
# $func664
# ==========================================================
def func664(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var5 = i32_load(var1)
    i32_store(41092, i32_load(var1 + 4))
    i32_store8(9147212, (1 if i32_load(var1 + 8) != 0 else 0))
    i32_store8(9561848, (1 if i32_load(var1 + 12) != 0 else 0))
    var3 = i32_load(9142892)
    if (1 if i32_load8_u(9147210) == 0 else 0):
        if var3:
            i32_store(9142892, 0)
            var0 = i32_load(9561692)
            if i32_load(9561692):
                i32_store(9561692, 0)
        i32_store(9142892, var5)
        i32_store8(9147210, 1)
        var9 = (i64_extend_u(var5) * 286704)
        var0 = (-1 if i32(((var9 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var5) * 286704)))
        var2 = func26((-1 if i32(((var9 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var5) * 286704))))
        # Unknown: memory.fill []
        break
    if (1 if var3 == var5 else 0):
        break
    var0 = 0
    i32_store(9142892, var5)
    var9 = (i64_extend_u(var5) * 286704)
    var7 = (-1 if i32(((var9 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var5) * 286704)))
    var2 = func26((-1 if i32(((var9 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(var5) * 286704))))
    # Unknown: memory.fill []
    var7 = i32_load(9561692)
    var3 = (var3 if (1 if var3 < var5 else 0) else var5)
    if (var3 if (1 if var3 < var5 else 0) else var5):
        if (1 if var3 >= 4 else 0):
            var8 = (var3 & -4)
            var5 = 0
            while True:  # loop $label2
                var4 = (var0 * 286704)
                # Unknown: memory.copy []
                var4 = ((var0 | 1) * 286704)
                # Unknown: memory.copy []
                var4 = ((var0 | 2) * 286704)
                # Unknown: memory.copy []
                var4 = ((var0 | 3) * 286704)
                # Unknown: memory.copy []
                var0 = (var0 + 4)
                var5 = (var5 + 4)
                if (1 if (var5 + 4) != var8 else 0):
                    continue
                break  # end loop
        var3 = (var3 & 3)
        if (1 if (var3 & 3) == 0 else 0):
            break
        var5 = 0
        while True:  # loop $label4
            var8 = (var0 * 286704)
            # Unknown: memory.copy []
            var0 = (var0 + 1)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != var3 else 0):
                continue
            break  # end loop
        break
    if (1 if var7 == 0 else 0):
        break
    var5 = i32_load(9142892)
    i32_store(9561692, var2)
    var7 = 1
    var0 = i32_load8_u(9147212)
    var8 = (var5 if i32_load8_u(9147212) else i32_load(41092))
    if (1 if (var5 if i32_load8_u(9147212) else i32_load(41092)) > 1 else 0):
        var5 = 4
        while True:  # loop $label5
            var2 = (var1 + (var5 << 2))
            var3 = i32_load((var1 + (var5 << 2)) + 12)
            var4 = i32_load(var2)
            var6 = i32_load(var2 + 4)
            var0 = (i32_load(9561692) + (var7 * 286704))
            i32_store16((i32_load(9561692) + (var7 * 286704)) + 4, i32_load(var2 + 8))
            i32_store16(var0 + 2, var6)
            i32_store16(var0, var4)
            i32_store16(var0 + 6, var3)
            var3 = i32_load(var2 + 28)
            var4 = i32_load(var2 + 16)
            var6 = i32_load(var2 + 20)
            i32_store16(var0 + 12, i32_load(var2 + 24))
            i32_store16(var0 + 10, var6)
            i32_store16(var0 + 8, var4)
            i32_store16(var0 + 14, var3)
            var3 = i32_load(var2 + 44)
            var4 = i32_load(var2 + 32)
            var6 = i32_load(var2 + 36)
            i32_store16(var0 + 20, i32_load(var2 + 40))
            i32_store16(var0 + 18, var6)
            i32_store16(var0 + 16, var4)
            i32_store16(var0 + 22, var3)
            var3 = i32_load(var2 + 60)
            var4 = i32_load(var2 + 48)
            var6 = i32_load(var2 + 52)
            i32_store16(var0 + 28, i32_load(var2 + 56))
            i32_store16(var0 + 26, var6)
            i32_store16(var0 + 24, var4)
            i32_store16(var0 + 30, var3)
            var3 = i32_load(var2 + 76)
            var4 = i32_load((var2 - -64))
            var6 = i32_load(var2 + 68)
            i32_store16(var0 + 36, i32_load(var2 + 72))
            i32_store16(var0 + 34, var6)
            i32_store16(var0 + 32, var4)
            i32_store16(var0 + 38, var3)
            var3 = i32_load(var2 + 92)
            var4 = i32_load(var2 + 80)
            var6 = i32_load(var2 + 84)
            i32_store16(var0 + 44, i32_load(var2 + 88))
            i32_store16(var0 + 42, var6)
            i32_store16(var0 + 40, var4)
            i32_store16(var0 + 46, var3)
            var3 = i32_load(var2 + 108)
            var4 = i32_load(var2 + 96)
            var6 = i32_load(var2 + 100)
            i32_store16(var0 + 52, i32_load(var2 + 104))
            i32_store16(var0 + 50, var6)
            i32_store16(var0 + 48, var4)
            i32_store16(var0 + 54, var3)
            var3 = i32_load(var2 + 124)
            var4 = i32_load(var2 + 112)
            var6 = i32_load(var2 + 116)
            i32_store16(var0 + 60, i32_load(var2 + 120))
            i32_store16(var0 + 58, var6)
            i32_store16(var0 + 56, var4)
            i32_store16(var0 + 62, var3)
            var3 = i32_load(var2 + 140)
            var4 = i32_load(var2 + 128)
            var6 = i32_load(var2 + 132)
            i32_store16(var0 + 68, i32_load(var2 + 136))
            i32_store16(var0 + 66, var6)
            i32_store16((var0 - -64), var4)
            i32_store16(var0 + 70, var3)
            var3 = i32_load(var2 + 144)
            var4 = i32_load(var2 + 148)
            var6 = i32_load(var2 + 152)
            i32_store16(var0 + 78, i32_load(var2 + 156))
            i32_store16(var0 + 76, var6)
            i32_store16(var0 + 74, var4)
            i32_store16(var0 + 72, var3)
            i32_store(var0 + 284608, i32_load(var2 + 160))
            i32_store(var0 + 283960, i32_load(var2 + 164))
            i32_store(var0 + 284616, i32_load(var2 + 168))
            var3 = i32_load(var2 + 172)
            i32_store8((var0 + 283974), i32_load(var2 + 172))
            i32_store8((var0 + 283973), ((var3 & 0xFFFFFFFF) >> 8))
            i32_store8(var0 + 283972, ((var3 & 0xFFFFFFFF) >> 16))
            var2 = i32_load(var2 + 176)
            i32_store(var0 + 283908, var7)
            i32_store(var0 + 286684, var2)
            var5 = (var5 + 45)
            var7 = (var7 + 1)
            if (1 if (var7 + 1) != var8 else 0):
                continue
            break  # end loop
    else:
    if (var0 & 255):
    return 0

