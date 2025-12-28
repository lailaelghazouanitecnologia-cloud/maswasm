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
# $func558
# ==========================================================
def func558(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    i32_store(9143000, 0)
    var0 = i32_load(9142872)
    var1 = i32_load(9561692)
    var2 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var2 * 132)))
        i32_store(9213820, 0)
    func45()
    var0 = i32_load((((var1 + (var0 * 286704)) + (i32_load(38452) << 2)) + 284636))
    if (1 if i32_load((((var1 + (var0 * 286704)) + (i32_load(38452) << 2)) + 284636)) == 0 else 0):
        break
    var2 = i32_load(var0 + 8)
    if (1 if i32_load(var0 + 8) == 0 else 0):
        break
    var1 = 0
    while True:  # loop $label1
        var3 = i32_load((i32_load(var0) + (var1 << 2)))
        if i32_load((i32_load(var0) + (var1 << 2))):
            func44((i32_load(9671128) + (var3 * 132)), 0)
            var2 = i32_load(var0 + 8)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < var2 else 0):
            continue
        break  # end loop


# ==========================================================
# $func596
# ==========================================================
def func596(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    if var0:
        if (1 if i32_load8_u(9147152) == 0 else 0):
            func52((207 if i32_load8_u(9143020) else 0), 0)
            a_b()
        i32_store(9143000, 0)
        var0 = i32_load(9213820)
        if i32_load(9213820):
            func47((i32_load(9671128) + (var0 * 132)))
            i32_store(9213820, 0)
        func45()
        var10 = (i32_load(9561692) + (i32_load(9142872) * 286704))
        while True:  # loop $label13
            var0 = 0
            var1 = ((var5 * 404) + 9568096)
            if i32_load(((var5 * 404) + 9568096) + 264):
                break
            if (1 if i32_load(var1 + 268) == 1 else 0):
                break
            var0 = (1 if i32_load(var1 + 92) != 0 else 0)
            if (1 if var0 == 0 else 0):
                break
            if (1 if var5 == i32_load(38456) else 0):
                break
            if (1 if var5 == i32_load(38764) else 0):
                break
            var7 = i32_load(((var10 + (var5 << 2)) + 284636))
            if (1 if i32_load(((var10 + (var5 << 2)) + 284636)) == 0 else 0):
                break
            var8 = 0
            var9 = i32_load(var7 + 8)
            if (1 if i32_load(var7 + 8) == 0 else 0):
                break
            while True:  # loop $label12
                var0 = i32_load((i32_load(var7) + (var8 << 2)))
                if (1 if i32_load((i32_load(var7) + (var8 << 2))) == 0 else 0):
                    break
                var2 = i32_load(9671128)
                var1 = (i32_load(9671128) + (var0 * 132))
                if (1 if i32_load8_u(9147152) == 0 else 0):
                    if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var1 + 110))))) == 0 else 0):
                        break
                    if (1 if i32_load((i32_load(9215884) + (i32_load(var1 + 44) << 4)) + 4) == 20 else 0):
                        break
                    if (1 if i32_load8_u(var1 + 127) == 6 else 0):
                        break
                var6 = i32_load(var1 + 28)
                var0 = i32_load(9215928)
                if (1 if i32_load(9215928) == 0 else 0):
                    break
                var3 = i32_load(var0 + 8)
                if (1 if i32_load(var0 + 8) == 0 else 0):
                    break
                var4 = i32_load(var0)
                var0 = 0
                while True:  # loop $label4
                    if (1 if i32_load((var2 + (i32_load((var4 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                        break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var3 else 0):
                        continue
                    break  # end loop
                var0 = i32_load(9215932)
                if (1 if i32_load(9215932) == 0 else 0):
                    break
                var3 = i32_load(var0 + 8)
                if (1 if i32_load(var0 + 8) == 0 else 0):
                    break
                var4 = i32_load(var0)
                var0 = 0
                while True:  # loop $label6
                    if (1 if i32_load((var2 + (i32_load((var4 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                        break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var3 else 0):
                        continue
                    break  # end loop
                var0 = i32_load(9215936)
                if (1 if i32_load(9215936) == 0 else 0):
                    break
                var3 = i32_load(var0 + 8)
                if (1 if i32_load(var0 + 8) == 0 else 0):
                    break
                var4 = i32_load(var0)
                var0 = 0
                while True:  # loop $label8
                    if (1 if i32_load((var2 + (i32_load((var4 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                        break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var3 else 0):
                        continue
                    break  # end loop
                var0 = i32_load(9215940)
                if (1 if i32_load(9215940) == 0 else 0):
                    break
                var3 = i32_load(var0 + 8)
                if (1 if i32_load(var0 + 8) == 0 else 0):
                    break
                var4 = i32_load(var0)
                var0 = 0
                while True:  # loop $label10
                    if (1 if i32_load((var2 + (i32_load((var4 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                        break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var3 else 0):
                        continue
                    break  # end loop
                if i32_load(var1 + 36):
                    break
                if (1 if i32_load8_u(var1 + 125) == 8 else 0):
                    var2 = i32_load((i32_load(9215884) + (i32_load(var1 + 44) << 4)) + 4)
                    if (1 if i32_load((i32_load(9215884) + (i32_load(var1 + 44) << 4)) + 4) == 43 else 0):
                        break
                    var0 = i32_load8_u(var1 + 123)
                    if (1 if i32_load8_u(var1 + 123) == 43 else 0):
                        break
                    if (1 if var2 == 15 else 0):
                        break
                    if (1 if var0 == 15 else 0):
                        break
                    if (1 if var2 == 28 else 0):
                        break
                    if (1 if var0 == 28 else 0):
                        break
                    if (1 if var2 == 27 else 0):
                        break
                    if (1 if var0 == 27 else 0):
                        break
                    if (1 if var0 != 63 else 0):
                        break
                    break
                if (1 if i32_load8_u(var1 + 123) == 63 else 0):
                    break
                func44(var1, 0)
                var9 = i32_load(var7 + 8)
                var8 = (var8 + 1)
                if (1 if (var8 + 1) < var9 else 0):
                    continue
                break  # end loop
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != 255 else 0):
                continue
            break  # end loop


# ==========================================================
# $func597
# ==========================================================
def func597(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    if var0:
        if (1 if i32_load8_u(9147152) == 0 else 0):
            func52((207 if i32_load8_u(9143020) else 0), 0)
            a_b()
        var1 = 0
        i32_store(9143000, 0)
        var0 = i32_load(9213820)
        if i32_load(9213820):
            func47((i32_load(9671128) + (var0 * 132)))
            i32_store(9213820, 0)
        func45()
        var10 = (i32_load(9561692) + (i32_load(9142872) * 286704))
        while True:  # loop $label13
            var0 = 0
            var2 = ((var1 * 404) + 9568096)
            if i32_load(((var1 * 404) + 9568096) + 264):
                break
            if (1 if i32_load(var2 + 268) == 1 else 0):
                break
            var0 = (1 if i32_load(var2 + 92) != 0 else 0)
            if (1 if var0 == 0 else 0):
                break
            if (1 if var1 == i32_load(38428) else 0):
                break
            if (1 if var1 == i32_load(38456) else 0):
                break
            if (1 if var1 == i32_load(38764) else 0):
                break
            if (1 if var1 == i32_load(38440) else 0):
                break
            if (1 if var1 == i32_load(38772) else 0):
                break
            if (1 if var1 == i32_load(38928) else 0):
                break
            var7 = i32_load(((var10 + (var1 << 2)) + 284636))
            if (1 if i32_load(((var10 + (var1 << 2)) + 284636)) == 0 else 0):
                break
            var8 = 0
            var9 = i32_load(var7 + 8)
            if (1 if i32_load(var7 + 8) == 0 else 0):
                break
            while True:  # loop $label12
                var0 = i32_load((i32_load(var7) + (var8 << 2)))
                if (1 if i32_load((i32_load(var7) + (var8 << 2))) == 0 else 0):
                    break
                var3 = i32_load(9671128)
                var2 = (i32_load(9671128) + (var0 * 132))
                if (1 if i32_load8_u(9147152) == 0 else 0):
                    if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var2 + 110))))) == 0 else 0):
                        break
                    if (1 if i32_load((i32_load(9215884) + (i32_load(var2 + 44) << 4)) + 4) == 20 else 0):
                        break
                    if (1 if i32_load8_u(var2 + 127) == 6 else 0):
                        break
                var6 = i32_load(var2 + 28)
                var0 = i32_load(9215928)
                if (1 if i32_load(9215928) == 0 else 0):
                    break
                var4 = i32_load(var0 + 8)
                if (1 if i32_load(var0 + 8) == 0 else 0):
                    break
                var5 = i32_load(var0)
                var0 = 0
                while True:  # loop $label4
                    if (1 if i32_load((var3 + (i32_load((var5 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                        break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var4 else 0):
                        continue
                    break  # end loop
                var0 = i32_load(9215932)
                if (1 if i32_load(9215932) == 0 else 0):
                    break
                var4 = i32_load(var0 + 8)
                if (1 if i32_load(var0 + 8) == 0 else 0):
                    break
                var5 = i32_load(var0)
                var0 = 0
                while True:  # loop $label6
                    if (1 if i32_load((var3 + (i32_load((var5 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                        break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var4 else 0):
                        continue
                    break  # end loop
                var0 = i32_load(9215936)
                if (1 if i32_load(9215936) == 0 else 0):
                    break
                var4 = i32_load(var0 + 8)
                if (1 if i32_load(var0 + 8) == 0 else 0):
                    break
                var5 = i32_load(var0)
                var0 = 0
                while True:  # loop $label8
                    if (1 if i32_load((var3 + (i32_load((var5 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                        break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var4 else 0):
                        continue
                    break  # end loop
                var0 = i32_load(9215940)
                if (1 if i32_load(9215940) == 0 else 0):
                    break
                var4 = i32_load(var0 + 8)
                if (1 if i32_load(var0 + 8) == 0 else 0):
                    break
                var5 = i32_load(var0)
                var0 = 0
                while True:  # loop $label10
                    if (1 if i32_load((var3 + (i32_load((var5 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                        break
                    var0 = (var0 + 1)
                    if (1 if (var0 + 1) != var4 else 0):
                        continue
                    break  # end loop
                if i32_load(var2 + 36):
                    break
                if (1 if i32_load8_u(var2 + 125) == 8 else 0):
                    var3 = i32_load((i32_load(9215884) + (i32_load(var2 + 44) << 4)) + 4)
                    if (1 if i32_load((i32_load(9215884) + (i32_load(var2 + 44) << 4)) + 4) == 43 else 0):
                        break
                    var0 = i32_load8_u(var2 + 123)
                    if (1 if i32_load8_u(var2 + 123) == 43 else 0):
                        break
                    if (1 if var3 == 15 else 0):
                        break
                    if (1 if var0 == 15 else 0):
                        break
                    if (1 if var3 == 28 else 0):
                        break
                    if (1 if var0 == 28 else 0):
                        break
                    if (1 if var3 == 27 else 0):
                        break
                    if (1 if var0 == 27 else 0):
                        break
                    if (1 if var0 != 63 else 0):
                        break
                    break
                if (1 if i32_load8_u(var2 + 123) == 63 else 0):
                    break
                func44(var2, 0)
                var9 = i32_load(var7 + 8)
                var8 = (var8 + 1)
                if (1 if (var8 + 1) < var9 else 0):
                    continue
                break  # end loop
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != 255 else 0):
                continue
            break  # end loop


# ==========================================================
# $pd
# Export: pd
# ==========================================================
def pd(var0):
    """Export: pd"""
    var1 = 0
    i32_store(9143000, 0)
    var1 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var1 * 132)))
        i32_store(9213820, 0)
    func45()
    i32_store8(9142906, var0)


# ==========================================================
# $Ae
# Export: Ae
# ==========================================================
def Ae(var0):
    """Export: Ae"""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    if i32_load8_u(9142916):
        i32_store(9603804, 0)
        i32_store(9577140, 0)
        i32_store(9576736, 0)
        i32_store(9571080, 0)
    var1 = i32_load8_u(9147152)
    if (1 if i32_load8_u(9147212) == 0 else 0):
        if var1:
            break
        break
    if i32_load8_u(9147210):
        break
    if i32_load(9142848):
        break
    i32_store(9147312, var0)
    i32_store(9147324, (var0 ^ -1))
    i32_store(9147320, (var0 ^ -1515870811))
    i32_store(9147316, (var0 ^ 1515870810))
    if var1:
        break
    break
    var1 = 0
    i32_store(9142872, 1)
    var3 = i32_load(9142440)
    if (i32_load(9142440) * var3):
        while True:  # loop $label4
            i32_store8((i32_load(9147288) + var1), i32_load(9147292))
            var1 = (var1 + 1)
            var3 = i32_load(9142440)
            if (1 if (var1 + 1) < (i32_load(9142440) * var3) else 0):
                continue
            break  # end loop
    i32_store(9147312, var0)
    i32_store(9142892, 2)
    i32_store(9147324, (var0 ^ -1))
    i32_store(9147320, (var0 ^ -1515870811))
    i32_store(9147316, (var0 ^ 1515870810))
    var0 = i32_load(9561692)
    if i32_load(9561692):
    else:
    var5 = (i64_extend_u(2) * 286704)
    var1 = (i32_load(9142892) if i32(((var5 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(2) * 286704)))
    var0 = func26((i32_load(9142892) if i32(((var5 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64_extend_u(2) * 286704))))
    # Unknown: memory.fill []
    i32_store(9561692, var0)
    i32_store((var0 + 571312), 1)
    i32_store((var0 + 286712), 6553701)
    i64_store((var0 + 286704), 32088563964837972)
    i32_store((var0 + 570612), 1)
    i32_store((var0 + 570572), i32_load(9561460))
    # Unknown: memory.copy []
    var1 = i32_load(9142424)
    i32_store((var0 + 570704), i32_load(i32_load(9142424) + 40))
    i32_store((var0 + 570840), i32_load(var1 + 36))
    var1 = i32_load(42128)
    i32_store8((var0 + 570678), i32_load(42128))
    i64_store((var0 + 570560), 21474836485000)
    i64_store((var0 + 570552), 21474836485000)
    i32_store8((var0 + 283974), 255)
    i32_store16(var0 + 283972, 65535)
    i32_store8((var0 + 570677), ((var1 & 0xFFFFFFFF) >> 8))
    i32_store8((var0 + 570676), ((var1 & 0xFFFFFFFF) >> 16))
    var4 = (1 if i32_load8_u(9147212) != 0 else 0)
    var1 = 0
    var3 = i32_load(9142892)
    i32_store(9142420, func26((-1 if (1 if var3 > 1073741823 else 0) else (i32_load(9142892) << 2))))
    var0 = i32_load(9142424)
    var2 = i32_load(i32_load(9142424) + 136)
    i32_store(40592, (1 if (1 if var2 <= 99 else 0) else (1 if i32_load8_u(9147210) else ((i32_load(i32_load(9142424) + 136) & 0xFFFFFFFF) // 100))))
    var2 = i32_load(var0 + 140)
    i32_store(51760, (i32_load(var0 + 140) * 1000))
    f32_store(9682176, float(var2))
    var2 = i32_load(var0 + 144)
    i32_store(51764, (i32_load(var0 + 144) * 1000))
    f32_store(9682180, float(var2))
    var2 = i32_load(var0 + 148)
    i32_store(51768, (i32_load(var0 + 148) * 1000))
    f32_store(9682184, float(var2))
    var0 = i32_load(var0 + 152)
    i32_store(51772, (i32_load(var0 + 152) * 1000))
    f32_store(9682188, float(var0))
    if var4:
        break
    if (1 if var3 == 0 else 0):
        break
    while True:  # loop $label5
        func239(var1)
        var1 = (var1 + 1)
        if (1 if (var1 + 1) < i32_load(9142892) else 0):
            continue
        break  # end loop
    return Xb(5)

