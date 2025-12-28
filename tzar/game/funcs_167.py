"""
Auto-generated from WAT. Contains 9 functions.
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
# $func731
# ==========================================================
def func731(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    if i32_load8_u(9147141):
        break
    if (1 if var0 == 0 else 0):
        break
    if (1 if i32_load8_u(9163793) == 0 else 0):
        break
    var0 = 0
    var2 = 40928
    var3 = 40
    var4 = i32_load(9561692)
    var5 = i32_load(9142872)
    # br_table ['$label1', '$label2', '$label3']
    _br_idx = i32_load((i32_load(9561692) + (i32_load(9142872) * 286704)) + 283960)
    break  # br_table
    var2 = 40784
    var3 = 36
    break
    var2 = 40624
    var3 = 38
    var1 = i32_load(((var1 << 2) + 9684832))
    while True:  # loop $label4
        if (1 if var1 != i32_load((var2 + (var0 << 2))) else 0):
            var0 = (var0 + 2)
            if (1 if (var0 + 2) < var3 else 0):
                continue
            break
        break  # end loop
    var0 = i32_load((var2 + ((var0 << 2) | 4)))
    func45()
    var1 = i32_load((((var4 + (var5 * 286704)) + (i32_load(((var0 * 132) + 9216080) + 4) << 2)) + 284636))
    if (1 if i32_load((((var4 + (var5 * 286704)) + (i32_load(((var0 * 132) + 9216080) + 4) << 2)) + 284636)) == 0 else 0):
        break
    var2 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    var0 = 0
    while True:  # loop $label6
        var3 = i32_load((i32_load(var1) + (var0 << 2)))
        if i32_load((i32_load(var1) + (var0 << 2))):
            func44((i32_load(9671128) + (var3 * 132)), 0)
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != var2 else 0):
            continue
        break  # end loop
    i32_store(9685860, (i32_load(9685860) + 1))


# ==========================================================
# $func732
# ==========================================================
def func732(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    if (1 if i32_load(((var0 * 404) + 9568096) + 368) == 55 else 0):
        i32_store(var1 + 12, var0)
        var0 = i32_load(9213808)
        if i32_load8_u(9147210):
            func41(2, 9173808, var0, (var1 + 12), 1)
            break
        var3 = (var0 << 2)
        var2 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
        if var0:
            # Unknown: memory.copy []
        # call_indirect via table[i32_load(9213840)]
        break
    func242(var0)
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $func798
# ==========================================================
def func798(var0):
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
    var2 = (global0 - 40032)
    global global0
    global0 = (global0 - 40032)
    if i32_load8_u(9163792):
        var4 = i32_load(9213808)
        if i32_load(9213808):
            # Unknown: memory.copy []
        i32_store(9143000, 0)
        var0 = i32_load(9213820)
        if i32_load(9213820):
            func47((i32_load(9671128) + (var0 * 132)))
            i32_store(9213820, 0)
        func45()
        if var4:
            while True:  # loop $label5
                var8 = (i32_load(9671128) + (i32_load(((var2 + 32) + (var7 << 2))) * 132))
                var0 = i32_load((i32_load(9671128) + (i32_load(((var2 + 32) + (var7 << 2))) * 132)) + 16)
                if (1 if i32_load((i32_load(9671128) + (i32_load(((var2 + 32) + (var7 << 2))) * 132)) + 16) == 0 else 0):
                    break
                if (1 if i32_load(var0 + 8) == 0 else 0):
                    break
                var6 = 0
                while True:  # loop $label4
                    var0 = (i32_load(9671128) + (i32_load((i32_load(var0) + (var6 << 2))) * 132))
                    if i32_load((i32_load(9671128) + (i32_load((i32_load(var0) + (var6 << 2))) * 132)) + 92):
                        break
                    var3 = i32_load(9213808)
                    if (1 if i32_load(9213808) > 9999 else 0):
                        break
                    if (1 if i32_load8_u(var0 + 125) == 3 else 0):
                        break
                    i32_store(((var3 << 2) + 9173808), i32_load(var0 + 28))
                    var1 = 1
                    i32_store(9213808, (var3 + 1))
                    if (i32_load8_u(9142906) | i32_load8_u(9142916)):
                        break
                    var1 = 0
                    if i32_load8_u(9142917):
                        break
                    var1 = i32_load(9299880)
                    if i32_load(9299880):
                        var1 = (var1 - 1)
                        i32_store(9299880, (var1 - 1))
                        var1 = i32_load((i32_load(9299872) + (var1 << 2)))
                        break
                    var1 = i32_load(9163776)
                    var3 = (i32_load(9163776) + 1)
                    i32_store(9163776, (i32_load(9163776) + 1))
                    var5 = i32_load(9163784)
                    if (1 if var3 < i32_load(9163784) else 0):
                        break
                    i32_store(var2 + 16, var5)
                    a_b()
                    i32_store(9163784, (i32_load(9163784) + 40000))
                    i32_store(var0 + 92, var1)
                    if (1 if i32_load(var0 + 36) == 0 else 0):
                    if (1 if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264) != 1 else 0):
                        break
                    if i32_load(var0 + 80):
                        break
                    var3 = i32_load16_u(var0 + 116)
                    if (1 if i32_load16_u(var0 + 116) == 0 else 0):
                        break
                    var5 = i32_load16_u(var0 + 118)
                    if (1 if i32_load16_u(var0 + 118) == 0 else 0):
                        break
                    if (1 if i32_load8_u(9147152) == 0 else 0):
                        if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var0 + 110))))) == 0 else 0):
                            break
                        if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 20 else 0):
                            break
                        if (1 if i32_load8_u(var0 + 127) == 6 else 0):
                            break
                    var1 = 0
                    if i32_load8_u(9142917):
                        break
                    var1 = i32_load(9299880)
                    if i32_load(9299880):
                        var1 = (var1 - 1)
                        i32_store(9299880, (var1 - 1))
                        var1 = i32_load((i32_load(9299872) + (var1 << 2)))
                        break
                    var1 = i32_load(9163776)
                    var9 = (i32_load(9163776) + 1)
                    i32_store(9163776, (i32_load(9163776) + 1))
                    var10 = i32_load(9163784)
                    if (1 if var9 < i32_load(9163784) else 0):
                        break
                    i32_store(var2, var10)
                    a_b()
                    i32_store(9163784, (i32_load(9163784) + 40000))
                    var5 = i32_load16_u(var0 + 118)
                    var3 = i32_load16_u(var0 + 116)
                    i32_store(var0 + 80, var1)
                    var6 = (var6 + 1)
                    var0 = i32_load(var8 + 16)
                    if (1 if (var6 + 1) < i32_load(i32_load(var8 + 16) + 8) else 0):
                        continue
                    break  # end loop
                var7 = (var7 + 1)
                if (1 if (var7 + 1) != var4 else 0):
                    continue
                break  # end loop
        break
    i32_store(var2 + 32, 0)
    var0 = i32_load(9213808)
    if i32_load8_u(9147210):
        func41(6, 9173808, var0, (var2 + 32), 1)
        break
    var4 = (var0 << 2)
    var1 = func26((-1 if (1 if var0 > 1073741823 else 0) else (var0 << 2)))
    if var0:
        # Unknown: memory.copy []
    # call_indirect via table[i32_load(9213872)]
    global global0
    global0 = (var2 + 40032)


# ==========================================================
# $func810
# ==========================================================
def func810(var0):
    var1 = 0
    var2 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var2 = i32_load(var0 + 8)
    i32_store(var1 + 4, i32_load16_u(var0 + 42))
    i32_store(var1, var2)
    func383(func363(8863, var1), var0)
    global global0
    global0 = (var1 + 16)


# ==========================================================
# $func831
# ==========================================================
def func831(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    if i32_load8_u(9142388):
        var5 = i32_load(9561692)
        var3 = i32_load(var0)
        var7 = i32_load(9142892)
        if (1 if i32_load(9142892) < 2 else 0):
            break
        var6 = i32_load(59164)
        var0 = 1
        while True:  # loop $label1
            var8 = (var5 + (var0 * 286704))
            if (1 if var6 == i32_load((var5 + (var0 * 286704)) + 284616) else 0):
                var4 = var0
                break
            if (1 if var6 == i32_load(var8 + 284628) else 0):
                var4 = var0
                break
            var0 = (var0 + 1)
            if (1 if (var0 + 1) != var7 else 0):
                continue
            break  # end loop
        i32_store((var5 + (var4 * 286704)) + 284632, var3)
        if (1 if i32_load(9561744) >= var3 else 0):
            break
        i32_store(9561744, var3)
        if (1 if var2 == 0 else 0):
            break
        var0 = i32_load(9561736)
        if i32_load(9561736):
            i32_store(9561736, 0)
        var4 = (var2 << 2)
        var0 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
        i32_store(9561740, var2)
        i32_store(9561736, var0)
        # Unknown: memory.copy []
        if (1 if var3 < i32_load(9561748) else 0):
            i32_store(9561748, var3)


# ==========================================================
# $func844
# ==========================================================
def func844(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var2 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var5 = i32_load(9671128)
    var6 = i32_load(var1)
    var1 = (i32_load(9671128) + (i32_load(var1) * 132))
    var3 = i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 125)
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load(var1) * 132)) + 125) == 3 else 0):
        break
    var4 = i32_load(9561692)
    var8 = i32_load16_u(var1 + 110)
    if i32_load((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 283912):
        break
    var7 = i32_load(var0)
    var0 = i32_load(var0 + 4)
    i32_store(var2 + 12, 0)
    i64_store(var2 + 4, 0)
    i32_store(var2, var0)
    if var3:
        break
    if func66((var4 + (var8 * 286704)), var2, 1, 1):
        break
    var3 = i32_load(((var7 * 404) + 9568096) + 268)
    var4 = (i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704))
    i32_store((i32_load(9561692) + (i32_load16_u(var1 + 110) * 286704)) + 283912, (i32_load(var4 + 283912) + 1))
    func63(0  # stack underflow, var1, 34, ((var0 << 16) + var7), (((i32_load(i32_load(9142424) + 132) * ((500 if (1 if var3 == 1 else 0) else 250) * var0)) & 0xFFFFFFFF) // 100))
    if (1 if i32_load((var5 + (var6 * 132)) + 92) == 0 else 0):
        break
    var0 = i32_load8_u(9147141)
    if i32_load(9140316):
        if (1 if i32_load(9140320) != i32_load((var5 + (var6 * 132)) + 28) else 0):
            break
    global global0
    global0 = (var2 + 16)


# ==========================================================
# $func847
# ==========================================================
def func847(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    if (1 if var0 == 0 else 0):
        break
    var3 = ((var1 << 2) + 9215712)
    var0 = i32_load(((var1 << 2) + 9215712))
    if i32_load8_u(9163793):
        if (1 if var0 == 0 else 0):
            var0 = func26(16)
            i32_store(func26(16) + 4, 10000)
            i32_store(var0, func26(40000))
            i64_store(var0 + 8, 4294967296)
            i32_store(var3, var0)
        var1 = i32_load(9213808)
        i32_store(var0 + 8, i32_load(9213808))
        if (1 if var1 == 0 else 0):
            break
        var1 = i32_load(var0)
        var0 = 0
        while True:  # loop $label1
            var2 = (var0 << 2)
            i32_store((var1 + (var0 << 2)), i32_load((var2 + 9173808)))
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < i32_load(9213808) else 0):
                continue
            break  # end loop
        break
    if (1 if var0 == 0 else 0):
        break
    i32_store(9143000, 0)
    var0 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var0 * 132)))
        i32_store(9213820, 0)
    func45()
    var1 = i32_load(var3)
    if i32_load(i32_load(var3) + 8):
        var4 = i32_load(9671128)
        var0 = 0
        while True:  # loop $label3
            var2 = (var4 + (i32_load((i32_load(var1) + (var0 << 2))) * 132))
            if (1 if i32_load8_u((var4 + (i32_load((i32_load(var1) + (var0 << 2))) * 132)) + 125) == 3 else 0):
                break
            if (1 if i32_load8_u(9147152) == 0 else 0):
                if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var2 + 110))))) == 0 else 0):
                    break
                if (1 if i32_load((i32_load(9215884) + (i32_load(var2 + 44) << 4)) + 4) == 20 else 0):
                    break
                if (1 if i32_load8_u(var2 + 127) == 6 else 0):
                    break
            if i32_load8_u(9163792):
                if i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 264):
                    break
            func44(var2, 0)
            var1 = i32_load(var3)
            var4 = i32_load(9671128)
            var0 = (var0 + 1)
            if (1 if (var0 + 1) < i32_load(var1 + 8) else 0):
                continue
            break  # end loop


# ==========================================================
# $kd
# Export: kd
# ==========================================================
def kd(var0):
    """Export: kd"""
    var1 = 0
    var2 = 0
    var1 = i32_load8_u(9681940)
    var2 = i32_load(9142400)
    if (1 if i32_load(9142400) == 0 else 0):
        break
    if var1:
        break
    if (1 if i32_load8_u(59182) == 0 else 0):
        break
    if (1 if i32_load8_u(9142917) == 0 else 0):
        if var1:
            i32_store8(9681940, 0)
            var1 = i32_load(9142440)
            var1 = (i32_load(9142440) * var1)
            if (1 if ((i32_load(9142440) * var1) << 2) == 0 else 0):
                break
            # Unknown: memory.fill []
            break
        var1 = i32_load(9142440)
        var1 = (i32_load(9142440) * var1)
        var1 = (-1 if (var1 & 805306368) else ((i32_load(9142440) * var1) << 4))
        var2 = func26((-1 if (var1 & 805306368) else ((i32_load(9142440) * var1) << 4)))
        # Unknown: memory.fill []
        i32_store(9142400, var2)
        break
    i32_store8(9681940, 0)
    if (1 if var0 == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    if (1 if i32_load8_u(9147212) == 0 else 0):
        break
    if i32_load8_u(9142917):
        a_b()
    func152()
    if (1 if i32_load8_u(9147152) == 0 else 0):
    return (0 if i32_load8_u(9142917) else i32_load(9142400))


# ==========================================================
# $jd
# Export: jd
# ==========================================================
def jd(var0):
    """Export: jd"""
    var1 = 0
    var2 = 0
    var3 = 0
    var1 = i32_load8_u(9681940)
    var3 = i32_load(9142404)
    if (1 if i32_load(9142404) == 0 else 0):
        break
    if var1:
        break
    if (1 if i32_load8_u(59182) == 0 else 0):
        break
    if var1:
        i32_store8(9681940, 0)
        var1 = i32_load(9142440)
        if (1 if ((i32_load(9142440) * var1) * 3) == 0 else 0):
            break
        while True:  # loop $label3
            i32_store((var3 + (var2 << 2)), 0)
            var2 = (var2 + 1)
            var1 = i32_load(9142440)
            if (1 if (var2 + 1) < ((i32_load(9142440) * var1) * 3) else 0):
                continue
            break  # end loop
        break
    var1 = i32_load(9142440)
    var2 = (i32_load(9142440) * var1)
    var2 = (-1 if (1 if (var2 * 3) > 1073741823 else 0) else ((i32_load(9142440) * var1) * 12))
    var3 = func26((-1 if (1 if (var2 * 3) > 1073741823 else 0) else ((i32_load(9142440) * var1) * 12)))
    # Unknown: memory.fill []
    i32_store(9142404, var3)
    if (1 if var0 == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    if (1 if i32_load8_u(9147212) == 0 else 0):
        break
    func152()
    if (1 if i32_load8_u(9147152) == 0 else 0):
    return (0 if i32_load8_u(9142917) else i32_load(9142404))

