"""
Auto-generated from WAT. Contains 7 functions.
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
# $func67
# ==========================================================
def func67(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0.0
    var7 = 0.0
    var8 = 0.0
    var9 = 0.0
    var10 = 0.0
    var11 = 0.0
    var12 = 0.0
    var13 = 0.0
    var3 = (global0 - 80)
    global global0
    global0 = (global0 - 80)
    if i32_load8_u(9142917):
        break
    var4 = i32_load8_u(var0 + 125)
    # br_table ['$label1', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label2', '$label1', '$label2']
    _br_idx = (i32_load8_u(var0 + 125) - 4)
    break  # br_table
    var2 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var1 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 356)
    if i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 356):
        break
    var1 = i32_load(var2 + 216)
    var2 = i32_load(var2 + 220)
    var1 = (i32_load(var2 + 216) if (1 if var1 > var2 else 0) else i32_load(var2 + 220))
    var1 = ((6 if (1 if var1 >= 6 else 0) else (i32_load(var2 + 216) if (1 if var1 > var2 else 0) else i32_load(var2 + 220))) - 1)
    if (1 if ((6 if (1 if var1 >= 6 else 0) else (i32_load(var2 + 216) if (1 if var1 > var2 else 0) else i32_load(var2 + 220))) - 1) > 4 else 0):
        var1 = 9142636
        break
    var1 = i32_load(((var1 << 2) + 10132))
    var1 = i32_load(var1)
    var2 = i32_load8_u(var0 + 122)
    if (1 if i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) == 6 else 0):
        var5 = i32_load(((var2 * 72) + 9263856) + 8)
        var1 = (i32_load(((var2 * 72) + 9263856) + 8) if var5 else var1)
    var4 = ((1 if var4 != 4 else 0) & (1 if var4 != 14 else 0))
    if (1 if ((1 if i32_load(38600) == var2 else 0) | (1 if i32_load(38472) == var2 else 0)) == 0 else 0):
        break
    if var1:
        break
    var1 = i32_load(((var2 * 72) + 9263856))
    i32_store8(var0 + 124, 0)
    if (1 if i32_load8_u(var0 + 129) == 8 else 0):
    if var1:
        break
    var1 = i32_load8_u(var0 + 122)
    if (1 if i32_load8_u(var0 + 125) == 1 else 0):
        var1 = i32_load(((var1 * 404) + 9568096) + 260)
        if i32_load(((var1 * 404) + 9568096) + 260):
            var2 = (32000 // var1)
            # Unknown: i32.extend16_s []
        else:
        var9 = (float(((32000 // var1) - (var2 % 25))) / 1.0)
        var2 = (i32_load8_u(var0 + 124) << 3)
        var6 = float(i32_load(((i32_load8_u(var0 + 124) << 3) + 8996)))
        var7 = ((float(((32000 // var1) - (var2 % 25))) / 1.0) * float(i32_load(((i32_load8_u(var0 + 124) << 3) + 8996))))
        var9 = float(i32_load((var2 + 8992)))
        var10 = (var9 * float(i32_load((var2 + 8992))))
        var2 = (i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4))) * 25)
        if var1:
            var1 = (32000 // var1)
            # Unknown: i32.extend16_s []
        else:
        var11 = float((-1 + var2))
        var12 = float(var7)
        var13 = float(var10)
        var1 = i32_load(var0 + 40)
        if i32_load8_u(9142916):
            i32_store(var3 + 72, var1)
            i64_store((var3 - -64), 0)
            f64_store(var3 + 56, var12)
            f64_store(var3 + 48, var13)
            a_b()
            break
        i32_store(var3 + 32, var1)
        f64_store(var3 + 24, float(var11))
        i64_store(var3 + 16, 0)
        f64_store(var3 + 8, var12)
        f64_store(var3, var13)
        a_b()
        var8 = (float(i32_load16_u(var0 + 112)) - var9)
        if ((1 if (float(i32_load16_u(var0 + 112)) - var9) < 4294967300.0 else 0) & (1 if var8 >= 0.0 else 0)):
            break
        i32_store16(int(var8) + 112, 0)
        var8 = (float(i32_load16_u(var0 + 114)) - var6)
        if ((1 if (float(i32_load16_u(var0 + 114)) - var6) < 4294967300.0 else 0) & (1 if var8 >= 0.0 else 0)):
            break
        i32_store16(int(var8) + 114, 0)
        if i32_load8_u(9142916):
        func288(var0, var10, var7)
        var7 = (var9 + float(i32_load16_u(var0 + 112)))
        if ((1 if (var9 + float(i32_load16_u(var0 + 112))) < 4294967300.0 else 0) & (1 if var7 >= 0.0 else 0)):
            break
        i32_store16(int(var7) + 112, 0)
        var6 = (var6 + float(i32_load16_u(var0 + 114)))
        if ((1 if (var6 + float(i32_load16_u(var0 + 114))) < 4294967300.0 else 0) & (1 if var6 >= 0.0 else 0)):
            i32_store16(var0 + 114, int(var6))
            break
        i32_store16(var0 + 114, 0)
        break
    # br_table ['$label9', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label10', '$label9', '$label11']
    _br_idx = (var1 + -64)
    break  # br_table
    if (1 if var1 != 10 else 0):
        break
    var2 = i32_load(9215884)
    var4 = i32_load(var0 + 44)
    # br_table ['$label12', '$label10', '$label10', '$label13', '$label10']
    _br_idx = (i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) - 1)
    break  # br_table
    break
    var2 = (i32_load(9671128) + (i32_load((var2 + ((var4 << 4) | 12))) * 132))
    if (1 if i32_load8_u((i32_load(9671128) + (i32_load((var2 + ((var4 << 4) | 12))) * 132)) + 125) == 10 else 0):
        break
    var2 = i32_load8_u(var2 + 122)
    # br_table ['$label15', '$label16', '$label14']
    _br_idx = (i32_load(((i32_load8_u(var2 + 122) * 404) + 9568096) + 188) - 1)
    break  # br_table
    break
    if (1 if var2 == i32_load(38500) else 0):
        break
    break
    break
    global global0
    global0 = (var3 + 80)
    return func86(var0)


# ==========================================================
# $func74
# ==========================================================
def func74(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 = 0
    if i32_load8_u(9147152):
        break
    var5 = i32_load16_u(var0 + 114)
    var4 = i32_load16_u(var0 + 112)
    if (1 if var1 == -1 else 0):
        break
    if (1 if i32_load8_u(59181) == 0 else 0):
        break
    var3 = i32_load(var0 + 44)
    if (1 if i32_load(var0 + 44) == 0 else 0):
        break
    var6 = i32_load(9215884)
    if (1 if i32_load((i32_load(9215884) + (var3 << 4)) + 12) == 1 else 0):
        break
    if (1 if i32_load8_u(var0 + 125) == 7 else 0):
        break
    if i32_load((var6 + ((var3 << 4) | 4))):
        break
    var1 = (var1 << 3)
    var5 = (var5 - i32_load(((var1 << 3) + 8996)))
    var4 = (var4 - i32_load((var1 + 8992)))
    var3 = i32_load(9142872)
    if (1 if i32_load(9142872) == 0 else 0):
        break
    if (1 if i32_load8_u((i32_load(9143012) + (i32_load16_u(var0 + 110) + (i32_load(9142892) * var3)))) == 0 else 0):
        break
    if (1 if ((1 if i32_load8_u(var0 + 125) != 3 else 0) | var2) == 0 else 0):
        break
    var3 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var1 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 220)
    var2 = i32_load(var3 + 216)
    # br_table ['$label3', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label4', '$label3', '$label4']
    _br_idx = (i32_load8_u(var0 + 125) - 4)
    break  # br_table
    break
    var0 = i32_load(var3 + 200)
    if (1 if i32_load(var3 + 200) == 0 else 0):
        break
    if (1 if i32_load(i32_load(9142424) + 48) < 2 else 0):
        break
    var6 = (i32_load(9142836) + (var0 * 80))
    var7 = i32_load((i32_load(9142836) + (var0 * 80)) + 324)
    if (1 if i32_load((i32_load(9142836) + (var0 * 80)) + 324) == 0 else 0):
        break
    var8 = (((var1 & 0xFFFFFFFF) >> 1) + var5)
    var9 = (((var2 & 0xFFFFFFFF) >> 1) + var4)
    var1 = i32_load(9142440)
    var10 = (var0 * var0)
    var0 = 0
    while True:  # loop $label7
        var4 = i32_load(var6 + 320)
        var3 = (var0 << 2)
        var2 = i32_load((i32_load(var6 + 320) + ((var0 << 2) | 4)))
        var5 = (var8 + i32_load((i32_load(var6 + 320) + ((var0 << 2) | 4))))
        if (1 if var1 <= (var8 + i32_load((i32_load(var6 + 320) + ((var0 << 2) | 4)))) else 0):
            break
        var4 = i32_load((var3 + var4))
        var3 = (var9 + i32_load((var3 + var4)))
        if (1 if var1 <= (var9 + i32_load((var3 + var4))) else 0):
            break
        if (1 if (var3 | var5) < 0 else 0):
            break
        if (1 if (((var4 * var4) + (var2 * var2)) - 1) > var10 else 0):
            break
        var1 = i32_load(9142440)
        var0 = (var0 + 2)
        if (1 if (var0 + 2) < var7 else 0):
            continue
        break  # end loop
    return func129(var3, var5, 0)


# ==========================================================
# $func77
# ==========================================================
def func77(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    if (1 if i32_load(var0 + 92) == 0 else 0):
        break
    var3 = i32_load(var0 + 28)
    if (1 if i32_load(var0 + 28) != i32_load(9213820) else 0):
        var2 = i32_load(9213808)
        if (1 if i32_load(9213808) == 0 else 0):
            break
        while True:  # loop $label2
            var4 = ((var1 << 2) + 9173808)
            if (1 if i32_load(((var1 << 2) + 9173808)) == var3 else 0):
                break
            var1 = (var1 + 1)
            if (1 if (var1 + 1) != var2 else 0):
                continue
            break  # end loop
        break
    i32_store(9213820, 0)
    if (1 if i32_load8_u(9147152) == 0 else 0):
        func52((207 if i32_load8_u(9143020) else 0), 0)
        a_b()
    func47(var0)
    return
    i32_store(var4, 0)
    var3 = (var2 - 1)
    i32_store(9213808, (var2 - 1))
    if (1 if var1 >= var3 else 0):
        break
    var4 = ((var2 - var1) - 2)
    var5 = ((var3 - var1) & 3)
    if ((var3 - var1) & 3):
        var2 = 0
        while True:  # loop $label4
            var1 = (var1 + 1)
            i32_store(((var1 << 2) + 9173808), i32_load((((var1 + 1) << 2) + 9173808)))
            var2 = (var2 + 1)
            if (1 if (var2 + 1) != var5 else 0):
                continue
            break  # end loop
    if (1 if var4 <= 2 else 0):
        break
    while True:  # loop $label5
        var2 = ((var1 << 2) + 9173808)
        var6 = i64_load(((var1 << 2) + 9173808) + 4)
        i32_store(var2 + 8, i32_load(var2 + 12))
        i64_store(var2, var6)
        var1 = (var1 + 4)
        i32_store(var2 + 12, i32_load((((var1 + 4) << 2) + 9173808)))
        if (1 if var1 != var3 else 0):
            continue
        break  # end loop
    func47(var0)
    if i32_load(9213808):
        return
    func45()
    if i32_load8_u(9147152):
        break
    func52((207 if i32_load8_u(9143020) else 0), 0)
    a_b()


# ==========================================================
# $func149
# ==========================================================
def func149(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0.0
    var3 = 100
    while True:  # loop $label1
        if var3:
            if var1:
                if i32_load(var1):
                    break
            var3 = (var3 - 1)
            if (1 if i32_load(var0) == var2 else 0):
                continue
            break
        break  # end loop
    if var1:
        break
    break
    var5 = 0
    var3 = global5
    if (1 if i32_load(var0) != var2 else 0):
        break
    var6 = float((1 if var3 else 100))
    var4 = global3
    while True:  # loop $label8
        if (1 if var3 == 0 else 0):
            if (1 if i32_load8_u(var4 + 41) != 1 else 0):
                break
        while True:  # loop $label6
            if i32_load(var4 + 36):
                break
            if (1 if func131(var0, var2, var6) == -73 else 0):
                continue
            break  # end loop
        break
        if (1 if i32_load(var0) == var2 else 0):
            continue
        break  # end loop
    if var5:
        break
    return var1


# ==========================================================
# $func156
# ==========================================================
def func156(var0, var1, param2):
    var2 = 0
    var3 = 0
    var4 = 0
    var2 = i32_load8_u(var0 + 125)
    var3 = ((i32_load8_u(var0 + 122) * 404) + 9568096)
    var4 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264)
    # br_table ['$label0', '$label1', '$label2']
    _br_idx = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 264)
    break  # br_table
    if (1 if i32_load(var3 + 268) != 1 else 0):
        break
    if i32_load(var0 + 52):
        break
    break
    if (1 if var4 != 4 else 0):
        break
    if (1 if i32_load(var0 + 52) == 0 else 0):
        break
    break
    if (1 if i32_load(var0 + 52) == 0 else 0):
        break
    if (1 if i32_load8_u(var0 + 126) == 2 else 0):
        break
    if i32_load(var0 + 36):
        break
    if (1 if var2 == 13 else 0):
        break
    func63(0  # stack underflow, var0, 22, 0, var1)
    return
    var1 = i32_load(((i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) * 40) + 9671200) + 32)
    if i32_load(((i32_load((i32_load(9215884) + (i32_load(var0 + 44) << 4)) + 4) * 40) + 9671200) + 32):
        # call_indirect via table[var1]
    i32_store(var0 + 44, 0)


# ==========================================================
# $func231
# ==========================================================
def func231(var0):
    var1 = 0
    var2 = 0
    var1 = (global0 - 48)
    global global0
    global0 = (global0 - 48)
    var2 = (var1 + 4)
    # Unknown: memory.fill []
    # Unknown: memory.copy []
    func436(9688272)
    i32_store(var0, i32_load(52428))
    i32_store(var0 + 4, i32_load(52432))
    func266(9688272)
    global global0
    global0 = (var1 + 48)


# ==========================================================
# $func248
# ==========================================================
def func248(var0, param1):
    var1 = 0
    var2 = 0
    var1 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    i32_store(var0 + 32, 1)
    var2 = (var0 + 4)
    if (1 if i32_load(var0 + 44) != i32_load(var0 + 48) else 0):
        while True:  # loop $label0
            func392((var1 + 4), var0)
            func54(var2)
            # call_indirect via table[i32_load(var1 + 4)]
            if (1 if i32_load(var0 + 44) != i32_load(var0 + 48) else 0):
                continue
            break  # end loop
    func54(var2)
    i32_store(var0 + 32, 0)
    global global0
    global0 = (var1 + 16)

