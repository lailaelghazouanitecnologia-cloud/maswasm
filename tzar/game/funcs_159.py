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
# $func327
# ==========================================================
def func327(var0):
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
    i32_store(9143000, 0)
    var0 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var0 * 132)))
        i32_store(9213820, 0)
    func45()
    var10 = (i32_load(9561692) + (i32_load(9142872) * 286704))
    while True:  # loop $label11
        if (1 if i32_load(38456) != var4 else 0):
            if (1 if var4 != i32_load(38764) else 0):
                break
        var7 = i32_load(((var10 + (var4 << 2)) + 284636))
        if (1 if i32_load(((var10 + (var4 << 2)) + 284636)) == 0 else 0):
            break
        var8 = 0
        var9 = i32_load(var7 + 8)
        if (1 if i32_load(var7 + 8) == 0 else 0):
            break
        while True:  # loop $label10
            var0 = i32_load((i32_load(var7) + (var8 << 2)))
            if (1 if i32_load((i32_load(var7) + (var8 << 2))) == 0 else 0):
                break
            var5 = i32_load(9671128)
            var3 = (i32_load(9671128) + (var0 * 132))
            if (1 if i32_load8_u(9147152) == 0 else 0):
                if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var3 + 110))))) == 0 else 0):
                    break
                if (1 if i32_load((i32_load(9215884) + (i32_load(var3 + 44) << 4)) + 4) == 20 else 0):
                    break
                if (1 if i32_load8_u(var3 + 127) == 6 else 0):
                    break
            var6 = i32_load(var3 + 28)
            var0 = i32_load(9215928)
            if (1 if i32_load(9215928) == 0 else 0):
                break
            var1 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var2 = i32_load(var0)
            var0 = 0
            while True:  # loop $label3
                if (1 if i32_load((var5 + (i32_load((var2 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var1 else 0):
                    continue
                break  # end loop
            var0 = i32_load(9215932)
            if (1 if i32_load(9215932) == 0 else 0):
                break
            var1 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var2 = i32_load(var0)
            var0 = 0
            while True:  # loop $label5
                if (1 if i32_load((var5 + (i32_load((var2 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var1 else 0):
                    continue
                break  # end loop
            var0 = i32_load(9215936)
            if (1 if i32_load(9215936) == 0 else 0):
                break
            var1 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var2 = i32_load(var0)
            var0 = 0
            while True:  # loop $label7
                if (1 if i32_load((var5 + (i32_load((var2 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var1 else 0):
                    continue
                break  # end loop
            var0 = i32_load(9215940)
            if (1 if i32_load(9215940) == 0 else 0):
                break
            var1 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var2 = i32_load(var0)
            var0 = 0
            while True:  # loop $label9
                if (1 if i32_load((var5 + (i32_load((var2 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var1 else 0):
                    continue
                break  # end loop
            if i32_load(var3 + 36):
                break
            func44(var3, 0)
            var9 = i32_load(var7 + 8)
            var8 = (var8 + 1)
            if (1 if (var8 + 1) < var9 else 0):
                continue
            break  # end loop
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != 255 else 0):
            continue
        break  # end loop


# ==========================================================
# $func328
# ==========================================================
def func328(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    i32_store(9143000, 0)
    var0 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var0 * 132)))
        i32_store(9213820, 0)
    func45()
    var5 = (i32_load(9561692) + (i32_load(9142872) * 286704))
    var0 = 0
    while True:  # loop $label4
        var1 = ((var0 * 404) + 9568096)
        if i32_load(((var0 * 404) + 9568096) + 264):
            break
        if (1 if i32_load(var1 + 268) == 1 else 0):
            break
        if (1 if i32_load(var1 + 92) == 0 else 0):
            break
        if (1 if i32_load(38452) == var0 else 0):
            break
        if (1 if i32_load(38496) == var0 else 0):
            break
        if (1 if i32_load(38756) == var0 else 0):
            break
        if (1 if i32_load(38692) == var0 else 0):
            break
        if (1 if i32_load(38696) == var0 else 0):
            break
        if (1 if i32_load(38776) == var0 else 0):
            break
        if (1 if i32_load(38752) == var0 else 0):
            break
        if (1 if i32_load(38704) != var0 else 0):
            break
        var2 = i32_load(((var5 + (var0 << 2)) + 284636))
        if (1 if i32_load(((var5 + (var0 << 2)) + 284636)) == 0 else 0):
            break
        var3 = 0
        var4 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        while True:  # loop $label3
            var1 = i32_load((i32_load(var2) + (var3 << 2)))
            if (1 if i32_load((i32_load(var2) + (var3 << 2))) == 0 else 0):
                break
            var1 = (i32_load(9671128) + (var1 * 132))
            if (1 if i32_load8_u(9147152) == 0 else 0):
                if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var1 + 110))))) == 0 else 0):
                    break
                if (1 if i32_load((i32_load(9215884) + (i32_load(var1 + 44) << 4)) + 4) == 20 else 0):
                    break
                if (1 if i32_load8_u(var1 + 127) == 6 else 0):
                    break
            if (1 if func159(var1) == 0 else 0):
                break
            if i32_load(var1 + 36):
                break
            if (1 if i32_load8_u(var1 + 125) == 8 else 0):
                break
            if (1 if i32_load8_u(var1 + 123) == 63 else 0):
                break
            func44(var1, 0)
            var4 = i32_load(var2 + 8)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) < var4 else 0):
                continue
            break  # end loop
        var0 = (var0 + 1)
        if (1 if (var0 + 1) != 255 else 0):
            continue
        break  # end loop


# ==========================================================
# $func329
# ==========================================================
def func329(var0):
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
    i32_store(9143000, 0)
    var0 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var0 * 132)))
        i32_store(9213820, 0)
    func45()
    var10 = (i32_load(9561692) + (i32_load(9142872) * 286704))
    while True:  # loop $label13
        var0 = 0
        var1 = ((var3 * 404) + 9568096)
        if i32_load(((var3 * 404) + 9568096) + 264):
            break
        if (1 if i32_load(var1 + 268) == 1 else 0):
            break
        var0 = (1 if i32_load(var1 + 92) != 0 else 0)
        if (1 if var0 == 0 else 0):
            break
        if (1 if var3 == i32_load(38456) else 0):
            break
        if (1 if var3 == i32_load(38764) else 0):
            break
        if (1 if var3 == i32_load(38428) else 0):
            break
        var7 = i32_load(((var10 + (var3 << 2)) + 284636))
        if (1 if i32_load(((var10 + (var3 << 2)) + 284636)) == 0 else 0):
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
            var4 = i32_load(var0 + 8)
            if (1 if i32_load(var0 + 8) == 0 else 0):
                break
            var5 = i32_load(var0)
            var0 = 0
            while True:  # loop $label4
                if (1 if i32_load((var2 + (i32_load((var5 + (var0 << 2))) * 132)) + 28) == var6 else 0):
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
                if (1 if i32_load((var2 + (i32_load((var5 + (var0 << 2))) * 132)) + 28) == var6 else 0):
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
                if (1 if i32_load((var2 + (i32_load((var5 + (var0 << 2))) * 132)) + 28) == var6 else 0):
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
                if (1 if i32_load((var2 + (i32_load((var5 + (var0 << 2))) * 132)) + 28) == var6 else 0):
                    break
                var0 = (var0 + 1)
                if (1 if (var0 + 1) != var4 else 0):
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
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != 255 else 0):
            continue
        break  # end loop


# ==========================================================
# $func330
# ==========================================================
def func330(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    i32_store(9143000, 0)
    var0 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var0 * 132)))
        i32_store(9213820, 0)
    func45()
    var1 = i32_load((((i32_load(9561692) + (i32_load(9142872) * 286704)) + (i32_load(38528) << 2)) + 284636))
    if (1 if i32_load((((i32_load(9561692) + (i32_load(9142872) * 286704)) + (i32_load(38528) << 2)) + 284636)) == 0 else 0):
        break
    var3 = i32_load(var1 + 8)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        break
    while True:  # loop $label2
        var0 = i32_load((i32_load(var1) + (var2 << 2)))
        if (1 if i32_load((i32_load(var1) + (var2 << 2))) == 0 else 0):
            break
        var0 = (i32_load(9671128) + (var0 * 132))
        var4 = 1
        if i32_load8_u(9147152):
        else:
            if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var0 + 110))))) == 0 else 0):
                break
            if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 20 else 0):
                break
        if (1 if (1 if i32_load8_u(var0 + 127) != 6 else 0) == 0 else 0):
            break
        if (1 if i32_load(var0 + 80) < 450 else 0):
            break
        if (1 if func159(var0) == 0 else 0):
            break
        if i32_load(var0 + 36):
            break
        func44(var0, 0)
        var3 = i32_load(var1 + 8)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) < var3 else 0):
            continue
        break  # end loop
    return func28(0, 0)


# ==========================================================
# $func331
# ==========================================================
def func331(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    i32_store(9143000, 0)
    var0 = i32_load(9213820)
    if i32_load(9213820):
        func47((i32_load(9671128) + (var0 * 132)))
        i32_store(9213820, 0)
    func45()
    var5 = (i32_load(9561692) + (i32_load(9142872) * 286704))
    while True:  # loop $label3
        var0 = ((var1 * 404) + 9568096)
        if i32_load(((var1 * 404) + 9568096) + 264):
            break
        var2 = i32_load(var0 + 268)
        if (1 if i32_load(var0 + 268) == 1 else 0):
            break
        if (1 if i32_load(var0 + 92) == 0 else 0):
            break
        if (1 if i32_load(var0 + 224) < 2 else 0):
            break
        if (1 if var1 == i32_load(38456) else 0):
            break
        if (1 if var1 == i32_load(38764) else 0):
            break
        if (1 if var1 == i32_load(38932) else 0):
            break
        if (1 if var2 == 2 else 0):
            break
        var2 = i32_load(((var5 + (var1 << 2)) + 284636))
        if (1 if i32_load(((var5 + (var1 << 2)) + 284636)) == 0 else 0):
            break
        var3 = 0
        var4 = i32_load(var2 + 8)
        if (1 if i32_load(var2 + 8) == 0 else 0):
            break
        while True:  # loop $label2
            var0 = i32_load((i32_load(var2) + (var3 << 2)))
            if (1 if i32_load((i32_load(var2) + (var3 << 2))) == 0 else 0):
                break
            var0 = (i32_load(9671128) + (var0 * 132))
            if (1 if i32_load8_u(9147152) == 0 else 0):
                if (1 if i32_load8_u((i32_load(9143008) + (i32_load(9142872) + (i32_load(9142892) * i32_load16_u(var0 + 110))))) == 0 else 0):
                    break
                if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 20 else 0):
                    break
                if (1 if i32_load8_u(var0 + 127) == 6 else 0):
                    break
            if (1 if func159(var0) == 0 else 0):
                break
            if i32_load(var0 + 36):
                break
            if (1 if i32_load8_u(var0 + 125) == 8 else 0):
                break
            if (1 if i32_load8_u(var0 + 123) == 63 else 0):
                break
            func44(var0, 0)
            var4 = i32_load(var2 + 8)
            var3 = (var3 + 1)
            if (1 if (var3 + 1) < var4 else 0):
                continue
            break  # end loop
        var1 = (var1 + 1)
        if (1 if (var1 + 1) != 255 else 0):
            continue
        break  # end loop

