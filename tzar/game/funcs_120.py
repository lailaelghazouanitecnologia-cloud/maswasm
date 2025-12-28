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
# $func169
# ==========================================================
def func169():
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
    var18 = 0
    var19 = 0
    var14 = (global0 - 16)
    global global0
    global0 = (global0 - 16)
    var0 = i32_load(9140328)
    if i32_load(9140328):
        var5 = i32_load(9142440)
        while True:  # loop $label7
            var1 = i32_load(((var15 << 2) + 9140336))
            var17 = i32_load(i32_load(((var15 << 2) + 9140336)) + 44)
            if (1 if ((var5 * i32_load(i32_load(((var15 << 2) + 9140336)) + 44)) * var5) >= 65536 else 0):
                var2 = i32_load(9147316)
                var0 = i32_load(9147320)
                var18 = 0
                var4 = i32_load(9147312)
                var3 = i32_load(9147324)
                while True:  # loop $label6
                    var10 = i32_load(var1 + 8)
                    var11 = i32_load(var1)
                    i32_store(9147320, var2)
                    i32_store(9147324, var0)
                    i32_store(9147316, var4)
                    var12 = i32_load(var1 + 12)
                    var13 = i32_load(var1 + 4)
                    var16 = i32_load(var1 + 20)
                    var8 = i32_load(var1 + 16)
                    i32_store(9147320, var4)
                    i32_store(9147324, var2)
                    var6 = ((var3 << 11) ^ var3)
                    var9 = (((((var4 & 0xFFFFFFFF) >> 19) ^ ((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8)) ^ var4) ^ var6)
                    i32_store(9147316, (((((var4 & 0xFFFFFFFF) >> 19) ^ ((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8)) ^ var4) ^ var6))
                    var0 = ((var0 << 11) ^ var0)
                    var6 = (((((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var9 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var9)
                    i32_store(9147312, (((((((var0 << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ ((var9 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var9))
                    var0 = (var5 << 5)
                    var8 = (var8 * var16)
                    var19 = (var6 % (var12 + ((var5 << 5) - (var13 // (var8 * var16)))))
                    var3 = (((var6 % (var12 + ((var5 << 5) - (var13 // (var8 * var16))))) - i32_load(var1 + 12)) // 32)
                    var10 = (var9 % (var10 + (var0 - var11)))
                    var7 = (((var9 % (var10 + (var0 - var11))) - i32_load(var1 + 8)) // 32)
                    var0 = i32_load(var1)
                    var11 = ((var7 + (i32_load(var1) // 32)) + (1 if (var0 & 31) != 0 else 0))
                    if (1 if (((var9 % (var10 + (var0 - var11))) - i32_load(var1 + 8)) // 32) < ((var7 + (i32_load(var1) // 32)) + (1 if (var0 & 31) != 0 else 0)) else 0):
                        var12 = 0
                        var0 = (i32_load(var1 + 4) // var8)
                        var0 = ((((i32_load(var1 + 4) // var8) // 32) + var3) + (1 if (var0 & 31) != 0 else 0))
                        var16 = (var3 if (1 if var0 < var3 else 0) else ((((i32_load(var1 + 4) // var8) // 32) + var3) + (1 if (var0 & 31) != 0 else 0)))
                        var13 = (var5 + 2)
                        var8 = i32_load(9142840)
                        while True:  # loop $label2
                            var7 = (var7 + 1)
                            var0 = var3
                            while True:  # loop $label0
                                if (1 if var0 != var16 else 0):
                                    var0 = (var0 + 1)
                                    if (1 if i32_load((var8 + (((((var0 + 1) + var13) * var13) + var7) << 2))) != 1 else 0):
                                        continue
                                    break
                                break  # end loop
                            var12 = (1 if var7 >= var11 else 0)
                            if (1 if var7 != var11 else 0):
                                continue
                            break  # end loop
                        if (1 if var12 == 0 else 0):
                            break
                    var0 = 0
                    var3 = i32_load(var1 + 52)
                    var6 = i32_load(9681936)
                    if (1 if (i32_load8_u(9568060) | i32_load8_u(9147152)) == 0 else 0):
                        break
                    if i32_load8_u(9142917):
                        break
                    var2 = i32_load(9299880)
                    if i32_load(9299880):
                        var2 = (var2 - 1)
                        i32_store(9299880, (var2 - 1))
                        var0 = i32_load((i32_load(9299872) + (var2 << 2)))
                        break
                    var0 = i32_load(9163776)
                    var4 = (i32_load(9163776) + 1)
                    i32_store(9163776, (i32_load(9163776) + 1))
                    var2 = i32_load(9163784)
                    if (1 if var4 < i32_load(9163784) else 0):
                        break
                    i32_store(var14, var2)
                    a_b()
                    i32_store(9163784, (i32_load(9163784) + 40000))
                    func216(var6, var3, var10, var19, var0)
                    var5 = i32_load(9142440)
                    var17 = i32_load(var1 + 44)
                    var9 = i32_load(9147316)
                    var4 = i32_load(9147320)
                    var6 = i32_load(9147312)
                    var2 = i32_load(9147324)
                    var3 = var2
                    var2 = var9
                    var0 = var4
                    var4 = var6
                    var18 = (var18 + 1)
                    if (1 if (var18 + 1) < ((((var5 * var17) * var5) & 0xFFFFFFFF) >> 16) else 0):
                        continue
                    break  # end loop
                var0 = i32_load(9140328)
            var15 = (var15 + 1)
            if (1 if (var15 + 1) < var0 else 0):
                continue
            break  # end loop
    global global0
    global0 = (var14 + 16)


# ==========================================================
# $func179
# ==========================================================
def func179(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    if (1 if var0 == 0 else 0):
        break
    if (1 if var1 == 0 else 0):
        break
    if (global4 if (i32_load(var0 + 52) & 64) else 0):
        break
    var2 = func252(1, 208)
    if (1 if func252(1, 208) == 0 else 0):
        break
    var3 = i32_load(52364)
    i32_store(52364, (i32_load(52364) + 1))
    i32_store(var2, var3)
    i32_store(var2 + 4, i32_load(var0 + 32))
    i32_store(var2 + 168, i32_load(var0 + 56))
    i32_store(var2 + 164, i32_load(var0 + 52))
    i32_store(var2 + 172, i32_load(var0 + 60))
    i32_store(var2 + 196, i32_load(var0 + 84))
    i32_store(var2 + 200, i32_load(var0 + 88))
    var5 = (var2 + 112)
    var3 = var0
    if (((var2 + 112) ^ var0) & 3):
        var4 = i32_load8_u(var3)
        break
    if (var3 & 3):
        while True:  # loop $label3
            var4 = i32_load8_u(var3)
            i32_store8(var5, i32_load8_u(var3))
            if (1 if var4 == 0 else 0):
                break
            var5 = (var5 + 1)
            var3 = (var3 + 1)
            if ((var3 + 1) & 3):
                continue
            break  # end loop
    var4 = i32_load(var3)
    if (((i32_load(var3) ^ -1) & (var4 - 16843009)) & -2139062144):
        break
    while True:  # loop $label4
        i32_store(var5, var4)
        var4 = i32_load(var3 + 4)
        var5 = (var5 + 4)
        var3 = (var3 + 4)
        if (1 if (((var4 - 16843009) & (var4 ^ -1)) & -2139062144) == 0 else 0):
            continue
        break  # end loop
    i32_store8(var5, var4)
    if (1 if (var4 & 255) == 0 else 0):
        break
    while True:  # loop $label5
        var4 = i32_load8_u(var3 + 1)
        i32_store8(var5 + 1, i32_load8_u(var3 + 1))
        var5 = (var5 + 1)
        var3 = (var3 + 1)
        if var4:
            continue
        break  # end loop
    i32_store(var2 + 152, i32_load(var0 + 40))
    i32_store(var2 + 148, i32_load(var0 + 36))
    i32_store(var2 + 156, i32_load(var0 + 44))
    i32_store(var2 + 160, i32_load(var0 + 48))
    var1 = func121(var1)
    i32_store(var2 + 8, func121(var1))
    if (1 if var1 == 0 else 0):
        func246(var2)
        return
    var1 = i32_load(var0 + 64)
    if i32_load(var0 + 64):
        var1 = func121(var1)
        i32_store(var2 + 176, func121(var1))
        if (1 if var1 == 0 else 0):
            break
    var1 = i32_load(var0 + 68)
    if i32_load(var0 + 68):
        var1 = func121(var1)
        i32_store(var2 + 180, func121(var1))
        if (1 if var1 == 0 else 0):
            break
    var1 = i32_load(var0 + 72)
    if i32_load(var0 + 72):
        var1 = func121(var1)
        i32_store(var2 + 184, func121(var1))
        if (1 if var1 == 0 else 0):
            break
    var1 = i32_load(var0 + 80)
    if i32_load(var0 + 80):
        var1 = func121(var1)
        i32_store(var2 + 192, func121(var1))
        if (1 if var1 == 0 else 0):
            break
    var5 = i32_load(var0 + 76)
    if i32_load(var0 + 76):
        var1 = 0
        while True:  # loop $label7
            var0 = var1
            var1 = (var1 + 1)
            if i32_load((var5 + (var0 << 2))):
                continue
            break  # end loop
        var3 = func252(1, ((var0 << 2) + 4))
        if (1 if func252(1, ((var0 << 2) + 4)) == 0 else 0):
            break
        if var0:
            var1 = 0
            while True:  # loop $label9
                var4 = (var1 << 2)
                var4 = func121(i32_load((var4 + var5)))
                i32_store((var3 + (var1 << 2)), func121(i32_load((var4 + var5))))
                if (1 if var4 == 0 else 0):
                    if var1:
                        var0 = 0
                        while True:  # loop $label8
                            var0 = (var0 + 1)
                            if (1 if (var0 + 1) != var1 else 0):
                                continue
                            break  # end loop
                    break
                var1 = (var1 + 1)
                if (1 if (var1 + 1) != var0 else 0):
                    continue
                break  # end loop
        i32_store((var3 + (var0 << 2)), 0)
        i32_store(var2 + 188, var3)
    a_m(var2)
    return
    func246(var2)


# ==========================================================
# $func181
# ==========================================================
def func181(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var4 = i32_load(var0 + 281796)
    if (1 if i32_load(var0 + 281796) == 0 else 0):
        var3 = func26(16)
        i32_store(func26(16) + 4, 20)
        i32_store(var3, func26(80))
        i64_store(var3 + 8, 85899345920)
        i32_store(var0 + 281796, var3)
        var8 = (var3 + 8)
        var6 = i32_load(var3)
        break
    var8 = (var4 + 8)
    var3 = i32_load(var4 + 8)
    var5 = i32_load(var4 + 4)
    if (1 if i32_load(var4 + 8) != i32_load(var4 + 4) else 0):
        var5 = var3
        var3 = var4
        var6 = i32_load(var4)
        break
    var3 = (i32_load(var4 + 12) + var5)
    i32_store(var4 + 4, (i32_load(var4 + 12) + var5))
    var7 = i32_load(var4)
    var6 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var5:
        # Unknown: memory.copy []
    var3 = var4
    if var7:
        var5 = i32_load(var4 + 8)
        var3 = i32_load(var0 + 281796)
    i32_store(var4, var6)
    i32_store(var8, (var5 + 1))
    i32_store((var6 + (var5 << 2)), var1)
    var0 = i32_load(var3 + 8)
    if (1 if i32_load(var3 + 8) != i32_load(var3 + 4) else 0):
        var5 = i32_load(var3)
        break
    var1 = (i32_load(var3 + 12) + var0)
    i32_store(var3 + 4, (i32_load(var3 + 12) + var0))
    var4 = i32_load(var3)
    var5 = func26((-1 if (1 if var1 > 1073741823 else 0) else (var1 << 2)))
    if var0:
        # Unknown: memory.copy []
    if var4:
        var0 = i32_load(var3 + 8)
    i32_store(var3, var5)
    i32_store(var3 + 8, (var0 + 1))
    i32_store((var5 + (var0 << 2)), var2)


# ==========================================================
# $func201
# ==========================================================
def func201(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var1 = i32_load(var0 + 24)
    if (1 if i32_load(var0 + 24) == 0 else 0):
        var1 = func26(16)
        i64_store(func26(16), 0)
        i64_store(var1 + 8, 0)
        i32_store(var0 + 24, var1)
    if (1 if i32_load(var1 + 8) == 0 else 0):
        var2 = func26(16)
        i32_store(func26(16) + 4, 20)
        i32_store(var2, func26(80))
        i64_store(var2 + 8, 8589934592)
        i32_store(var1 + 8, var2)
        var1 = i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 196)
        var6 = ((i32_load((i32_load(9561692) + (i32_load16_u(var0 + 110) * 286704)) + 283936) * 20) % i32_load16_u(((i32_load(((i32_load8_u(var0 + 122) * 404) + 9568096) + 196) << 1) + 9142944)))
        var7 = ((var1 << 2) + 9142928)
        while True:  # loop $label1
            var8 = i32_load16_u((i32_load(var7) + ((var5 + var6) << 1)))
            if i32_load16_u((i32_load(var7) + ((var5 + var6) << 1))):
                var1 = i32_load(i32_load(var0 + 24) + 8)
                var2 = i32_load(i32_load(i32_load(var0 + 24) + 8) + 8)
                if (1 if i32_load(i32_load(i32_load(var0 + 24) + 8) + 8) != i32_load(var1 + 4) else 0):
                    var3 = i32_load(var1)
                    break
                var3 = (i32_load(var1 + 12) + var2)
                i32_store(var1 + 4, (i32_load(var1 + 12) + var2))
                var4 = i32_load(var1)
                var3 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
                if var2:
                    # Unknown: memory.copy []
                if var4:
                    var2 = i32_load(var1 + 8)
                i32_store(var1, var3)
                i32_store(var1 + 8, (var2 + 1))
                i32_store((var3 + (var2 << 2)), var8)
            var5 = (var5 + 1)
            if (1 if (var5 + 1) != 20 else 0):
                continue
            break  # end loop


# ==========================================================
# $func207
# ==========================================================
def func207(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var3 = i32_load(var0 + 20)
    if (1 if i32_load(var0 + 20) == 0 else 0):
        var2 = func26(16)
        i32_store(func26(16) + 4, 2)
        var3 = func26(8)
        i32_store(var2 + 12, 16)
        i32_store(var2, var3)
        i32_store(var0 + 20, var2)
        i32_store(var2 + 8, 0)
        var7 = (var2 + 8)
        break
    i32_store(var3 + 8, 0)
    var7 = (var3 + 8)
    if (1 if i32_load(var3 + 4) == 0 else 0):
        break
    var2 = var3
    var6 = i32_load(var2)
    break
    var2 = i32_load(var3 + 12)
    i32_store(var3 + 4, i32_load(var3 + 12))
    var5 = i32_load(var3)
    var6 = func26((-1 if (1 if var2 > 1073741823 else 0) else (var2 << 2)))
    var2 = var3
    if var5:
        var4 = i32_load(var3 + 8)
        var2 = i32_load(var0 + 20)
    i32_store(var3, var6)
    i32_store(var7, (var4 + 1))
    i32_store((var6 + (var4 << 2)), 2)
    var0 = i32_load(var2 + 8)
    if (1 if i32_load(var2 + 8) != i32_load(var2 + 4) else 0):
        var4 = i32_load(var2)
        break
    var3 = (i32_load(var2 + 12) + var0)
    i32_store(var2 + 4, (i32_load(var2 + 12) + var0))
    var5 = i32_load(var2)
    var4 = func26((-1 if (1 if var3 > 1073741823 else 0) else (var3 << 2)))
    if var0:
        # Unknown: memory.copy []
    if var5:
        var0 = i32_load(var2 + 8)
    i32_store(var2, var4)
    i32_store(var2 + 8, (var0 + 1))
    i32_store((var4 + (var0 << 2)), var1)

