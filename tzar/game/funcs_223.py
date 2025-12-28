"""
Auto-generated from WAT. Contains 5 functions.
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
# $func719
# ==========================================================
def func719(var0, var1, var2):
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
    var6 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    if var2:
        var11 = i32_load(var0)
        var0 = 0
        while True:  # loop $label9
            var3 = (i32_load(9671128) + (i32_load((var1 + (var0 << 2))) * 132))
            # br_table ['$label0', '$label1', '$label1', '$label1', '$label1', '$label0', '$label1']
            _br_idx = (i32_load8_u((i32_load(9671128) + (i32_load((var1 + (var0 << 2))) * 132)) + 125) - 3)
            break  # br_table
            var8 = i32_load8_u(var3 + 128)
            var4 = i32_load16_u(var3 + 110)
            var5 = i32_load(9561692)
            var7 = (1 if i32_load(38676) == i32_load8_u(var3 + 122) else 0)
            if (1 if (1 if i32_load(38676) == i32_load8_u(var3 + 122) else 0) == 0 else 0):
                var9 = ((var5 + (var4 * 286704)) + 284176)
                break
            var9 = ((var5 + (var4 * 286704)) + 284312)
            if (1 if var8 == 0 else 0):
                break
            if (1 if var11 != 2 else 0):
                break
            i32_store8(var3 + 127, 0)
            var5 = i32_load(var3 + 40)
            if i32_load(var3 + 40):
                if i32_load8_u(9142916):
                    i32_store(var6 + 20, var5)
                    i32_store(var6 + 16, 0)
                    a_b()
                    i32_store8(var3 + 128, 0)
                    break
                i32_store(var6 + 4, var5)
                i32_store(var6, (var4 + 16))
                a_b()
            i32_store8(var3 + 128, 0)
            break
            var9 = i32_load(var9)
            if (1 if i32_load(var9) > i32_load(var3 + 72) else 0):
                break
            if (1 if var11 == 2 else 0):
                break
            if (1 if var8 == 0 else 0):
                func296(var3, (2 if var7 else 1))
                if var7:
                    break
                var4 = i32_load16_u(var3 + 110)
                var5 = i32_load(9561692)
                break
            if var7:
                break
            var8 = i32_load(((var5 + ((var4 & 65535) * 286704)) + 284204))
            var13 = i32_load(9215892)
            if (1 if i32_load(9215892) == 0 else 0):
                var5 = i32_load(var3 + 28)
                break
            var5 = i32_load(var3 + 28)
            var4 = 0
            var12 = i32_load(9142848)
            var7 = i32_load(9215884)
            while True:  # loop $label8
                var10 = (var4 << 2)
                if (1 if i32_load((var7 + ((var4 << 2) | 4))) != 21 else 0):
                    break
                if (1 if i32_load((var7 + (var10 | 8))) != var5 else 0):
                    break
                var10 = (var7 + var10)
                if (1 if i32_load((var7 + var10)) > var12 else 0):
                    break
                var4 = (var4 + 4)
                if (1 if (var4 + 4) < var13 else 0):
                    continue
                break  # end loop
            break
            i32_store(var10, (var12 + ((var8 & 0xFFFFFFFF) // 25)))
            var4 = ((i32_load(9561692) + (i32_load16_u(var3 + 110) * 286704)) + 281668)
            i32_store(((i32_load(9561692) + (i32_load16_u(var3 + 110) * 286704)) + 281668), (i32_load(var4) + var9))
            i32_store(var3 + 72, (i32_load(var3 + 72) - var9))
            if (1 if i32_load(var3 + 92) == 0 else 0):
                break
            var4 = i32_load8_u(9147141)
            if i32_load(9140316):
                if (1 if i32_load(9140320) != i32_load(var3 + 28) else 0):
                    break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var2 else 0):
                continue
            break  # end loop
    global global0
    global0 = (var6 + 32)


# ==========================================================
# $func721
# ==========================================================
def func721(var0, var1):
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
    var13 = 0.0
    var1 = (global0 - 112)
    global global0
    global0 = (global0 - 112)
    var2 = i32_load(9671128)
    var3 = (i32_load(9671128) + (var0 * 132))
    var8 = i32_load16_u(var3 + 116)
    var5 = i32_load16_u(var3 + 118)
    var3 = i32_load(9142440)
    if (1 if i32_load(9142440) <= var5 else 0):
        break
    if (1 if var3 <= var8 else 0):
        break
    if (1 if i32_load(9142832) == 0 else 0):
        if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
            break
    var0 = (var2 + (var0 * 132))
    var9 = (var2 + (var0 * 132))
    var3 = i32_load(9142872)
    var0 = i32_load16_u(var0 + 110)
    if (1 if i32_load(9142872) == i32_load16_u(var0 + 110) else 0):
        i32_store(var1 + 96, i32_load(39936))
        a_b()
        var3 = i32_load(9142872)
        var0 = i32_load16_u(var9 + 110)
    if (1 if i32_load8_u((i32_load(9143012) + ((i32_load(9142892) * var0) + var3))) == 0 else 0):
        var3 = -1
        break
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    var3 = 0
    var10 = i32_load(9142836)
    var6 = i32_load(i32_load(9142836) + 964)
    if (1 if i32_load(i32_load(9142836) + 964) == 0 else 0):
        break
    while True:  # loop $label4
        var11 = i32_load(9142440)
        var2 = i32_load(var10 + 960)
        var4 = (var3 << 2)
        var7 = i32_load((i32_load(var10 + 960) + ((var3 << 2) | 4)))
        var0 = (i32_load((i32_load(var10 + 960) + ((var3 << 2) | 4))) + var5)
        if (1 if i32_load(9142440) <= (i32_load((i32_load(var10 + 960) + ((var3 << 2) | 4))) + var5) else 0):
            break
        var4 = i32_load((var2 + var4))
        var2 = (i32_load((var2 + var4)) + var8)
        if (1 if var11 <= (i32_load((var2 + var4)) + var8) else 0):
            break
        if (1 if (var0 | var2) < 0 else 0):
            break
        if (1 if (((var4 * var4) + (var7 * var7)) - 1) <= 64 else 0):
            break
        func258(var2, var0)
        var3 = (var3 + 2)
        if (1 if (var3 + 2) < var6 else 0):
            continue
        break  # end loop
    var3 = 0
    if (1 if i32_load8_u(59181) == 0 else 0):
        break
    if i32_load8_u(9142917):
        break
    var0 = i32_load(9299880)
    if i32_load(9299880):
        var0 = (var0 - 1)
        i32_store(9299880, (var0 - 1))
        var3 = i32_load((i32_load(9299872) + (var0 << 2)))
        break
    var3 = i32_load(9163776)
    var0 = (i32_load(9163776) + 1)
    i32_store(9163776, (i32_load(9163776) + 1))
    var2 = i32_load(9163784)
    if (1 if var0 < i32_load(9163784) else 0):
        break
    i32_store(var1 + 80, var2)
    a_b()
    i32_store(9163784, (i32_load(9163784) + 40000))
    var7 = (var8 << 5)
    if i32_load8_u(9142916):
        var4 = (i32_load(9142440) * 96)
        var0 = 0
        var2 = i32_load(9142584)
        if (1 if i32_load(9142584) == 0 else 0):
            break
        if (1 if i32_load(var2 + 20) == 0 else 0):
            break
        var0 = i32_load(var2 + 28)
        if (1 if i32_load(var2 + 28) != 2147483647 else 0):
            break
        var0 = i32_load(59152)
        i32_store(59152, (i32_load(59152) + 1))
        var6 = i32_load(9568052)
        i32_store(var2 + 28, var0)
        var11 = i32_load(var2)
        var10 = i32_load(var2 + 4)
        var12 = i32_load(9568048)
        i32_store(9568048, (i32_load(9568048) + 1))
        i32_store(((var12 << 2) + 9563952), var2)
        i32_store(9568052, (var6 + ((var11 * (var10 + 2)) << 2)))
        var6 = i32_load(9568056)
        i32_store(var2 + 56, i32_load(9568056))
        i32_store(9568056, (var6 + ((var10 * i32_load(var2)) << 2)))
        var13 = float(var4)
        var2 = (i32_load(9142848) * 25)
        var9 = i32_load16_u(var9 + 110)
        i32_store(var1 + 76, var3)
        i32_store(var1 + 72, 0)
        i32_store((var1 - -64), 65535)
        i64_store(var1 + 56, 0)
        i32_store(var1 + 52, var2)
        i32_store(var1 + 48, var0)
        i64_store(var1 + 40, 0)
        i64_store(var1 + 32, 0)
        i64_store(var1 + 24, 0)
        f64_store(var1 + 16, float(((((var13 * 0.5) / var13) + 0.25) if var4 else var13)))
        i32_store(var1 + 68, ((var9 << 16) | 54))
        f64_store(var1 + 8, float((var5 << 5)))
        f64_store(var1, float(var7))
        a_b()
        break
    global global0
    global0 = (var1 + 112)


# ==========================================================
# $func734
# ==========================================================
def func734(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = i32_load(9671128)
    var3 = (i32_load(9671128) + (var0 * 132))
    var0 = (var2 + (var1 * 132))
    if (1 if i32_load8_u(var0 + 128) == 0 else 0):
        func296(var0, 1)
    var3 = i32_load(((i32_load(9561692) + (i32_load16_u(var3 + 110) * 286704)) + 284204))
    var6 = i32_load(9215892)
    if (1 if i32_load(9215892) == 0 else 0):
        var1 = i32_load((var2 + (var1 * 132)) + 28)
        break
    var1 = i32_load((var2 + (var1 * 132)) + 28)
    var0 = 0
    var5 = i32_load(9142848)
    var2 = i32_load(9215884)
    while True:  # loop $label3
        var4 = (var0 << 2)
        if (1 if i32_load((var2 + ((var0 << 2) | 4))) != 21 else 0):
            break
        if (1 if i32_load((var2 + (var4 | 8))) != var1 else 0):
            break
        var4 = (var2 + var4)
        if (1 if i32_load((var2 + var4)) > var5 else 0):
            break
        var0 = (var0 + 4)
        if (1 if (var0 + 4) < var6 else 0):
            continue
        break  # end loop
    return
    i32_store(var4, (var5 + ((var3 & 0xFFFFFFFF) // 25)))


# ==========================================================
# $Ce
# Export: Ce
# ==========================================================
def Ce(var0):
    """Export: Ce"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    func182()
    if (1 if var0 == 0 else 0):
        var5 = i32_load(9142440)
        if (1 if i32_load(9142440) > 0 else 0):
            var2 = var5
            while True:  # loop $label2
                var3 = (var4 + 1)
                var6 = i32_load(9142840)
                var0 = 0
                while True:  # loop $label1
                    var1 = var0
                    var0 = (var0 + 1)
                    if (1 if var1 >= var2 else 0):
                        break
                    if (1 if var2 <= var4 else 0):
                        break
                    i32_store((var6 + ((var3 + (var0 * (var2 + 2))) << 2)), 0)
                    var1 = (i32_load(9142440) + 2)
                    i32_store((var6 + ((var3 + ((var0 + (i32_load(9142440) + 2)) * var1)) << 2)), 0)
                    var1 = (i32_load(9142440) + 2)
                    i32_store((var6 + ((var3 + ((var0 + ((i32_load(9142440) + 2) << 1)) * var1)) << 2)), 0)
                    var2 = i32_load(9142440)
                    if (1 if var0 != var5 else 0):
                        continue
                    break  # end loop
                var4 = var3
                if (1 if var3 != var5 else 0):
                    continue
                break  # end loop
        func169()


# ==========================================================
# $func774
# ==========================================================
def func774(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var1 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    var2 = i32_load(9671128)
    if (1 if i32_load(9142848) < (i32_load(i32_load(9142424) + 72) * 2400) else 0):
        func29((var2 + (var0 * 132)), 1)
        break
    var5 = (var0 * 132)
    var3 = (var2 + (var0 * 132))
    if (1 if i32_load8_u((var2 + (var0 * 132)) + 125) == 3 else 0):
        break
    if (1 if i32_load8_u(var3 + 128) == 0 else 0):
        break
    var2 = (var2 + (var0 * 132))
    i32_store8((var2 + (var0 * 132)) + 127, 0)
    var4 = i32_load(var2 + 40)
    if (1 if i32_load(var2 + 40) == 0 else 0):
        break
    if i32_load8_u(9142916):
        i32_store(var1 + 20, var4)
        i32_store(var1 + 16, 0)
        a_b()
        break
    var2 = i32_load16_u(var2 + 110)
    i32_store(var1 + 4, var4)
    i32_store(var1, (var2 + 16))
    a_b()
    i32_store8(var3 + 128, 0)
    var2 = i32_load(9671128)
    var2 = (var2 + var5)
    var3 = i32_load16_u(var2 + 116)
    var2 = i32_load16_u(var2 + 118)
    global global0
    global0 = (var1 + 32)

