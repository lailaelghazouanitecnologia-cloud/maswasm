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
# $fe
# Export: fe
# ==========================================================
def fe(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11):
    """Export: fe"""
    if (1 if i32_load(9142892) <= var1 else 0):
        break
    if (1 if var0 == i32_load(38624) else 0):
        var0 = (i32_load(39056) if (1 if var11 == 3 else 0) else (i32_load(38632) if (1 if var11 == 2 else 0) else (i32_load(38628) if (1 if var11 == 1 else 0) else var0)))
    if (1 if i32_load(38604) == var0 else 0):
        var0 = (i32_load(38616) if (1 if var11 == 3 else 0) else (i32_load(38612) if (1 if var11 == 2 else 0) else (i32_load(38608) if (1 if var11 == 1 else 0) else var0)))
    var0 = ((i32_load(38620) if (1 if var0 == i32_load(38560) else 0) else var0) if var11 else var0)
    var0 = func34(((i32_load(38620) if (1 if var0 == i32_load(38560) else 0) else var0) if var11 else var0), var1, var2, var3, ((var4 if (1 if var0 == 7 else 0) else 0) if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 1 else 0) else var4), 1)
    if (1 if func34(((i32_load(38620) if (1 if var0 == i32_load(38560) else 0) else var0) if var11 else var0), var1, var2, var3, ((var4 if (1 if var0 == 7 else 0) else 0) if (1 if i32_load(((var0 * 404) + 9568096) + 264) == 1 else 0) else var4), 1) == 0 else 0):
        break
    var1 = i32_load(9671128)
    var2 = (i32_load(9671128) + (var0 * 132))
    i32_store((i32_load(9671128) + (var0 * 132)) + 60, var6)
    i32_store(var2 + 52, var5)
    if var7:
        i32_store(var2 + 64, var7)
    if var8:
        i32_store((var1 + (var0 * 132)) + 68, var8)
    var0 = (var1 + (var0 * 132))
    i32_store((var1 + (var0 * 132)) + 72, var10)
    i32_store(var0 + 84, var9)


# ==========================================================
# $func840
# ==========================================================
def func840(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var2 = (global0 - 32)
    global global0
    global0 = (global0 - 32)
    i32_store(var2 + 28, (var0 & 65535))
    i32_store(var2 + 24, ((var0 & 0xFFFFFFFF) >> 16))
    var3 = (var1 & 65535)
    var0 = (((var1 & 65535) * 404) + 9568096)
    var0 = i32_load(var2 + 28)
    var1 = i32_load(var2 + 24)
    var5 = i32_load(i32_load(9142424) + 48)
    if i32_load(i32_load(9142424) + 48):
        if (1 if i32_load8_u(9147152) == 0 else 0):
            break
    var3 = i32_load(9142440)
    break
    var3 = i32_load(9142440)
    var4 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var1) + var0) << 1)))
    if (1 if var5 == 2 else 0):
        if (1 if var4 > 1 else 0):
            break
        break
    if (1 if var4 == 0 else 0):
        break
    func80(float(var0), float(var1), i32_load(9142536), 32.0, float((var3 * 96)))
    var3 = ((var0 << 5) - i32_load(9142952))
    var3 = ((var1 << 5) - i32_load(9142956))
    if (1 if (((((var0 << 5) - i32_load(9142952)) * var3) + (((var1 << 5) - i32_load(9142956)) * var3)) - 1) > 9000000 else 0):
        break
    var4 = i32_load(i32_load(9142424) + 48)
    if (1 if i32_load(i32_load(9142424) + 48) == 0 else 0):
        break
    if i32_load8_u(9147152):
        break
    var3 = i32_load16_u((i32_load(9147376) + (((i32_load(9142440) * var1) + var0) << 1)))
    if (1 if var4 == 2 else 0):
        if (1 if var3 > 1 else 0):
            break
        break
    if (1 if var3 == 0 else 0):
        break
    i32_store(var2 + 8, var1)
    i32_store(var2 + 4, var0)
    i32_store(var2, i32_load(((((i32_load(9142848) + var0) % 10) << 2) + 57744)))
    a_b()
    global global0
    global0 = (var2 + 32)


# ==========================================================
# $func343
# ==========================================================
def func343():
    var0 = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0.0
    var10 = 0.0
    var11 = 0.0
    var12 = 0.0
    var0 = i32_load(9142440)
    # Unknown: f64.convert_i32_u []
    var9 = (((f32(((i32_load(9142440) * var0) * 1.52587890625e-05)) * float((i32_load(i32_load(9142424) + 60) * 160))) / 40.0) + 0.5)
    if ((1 if (((f32(((i32_load(9142440) * var0) * 1.52587890625e-05)) * float((i32_load(i32_load(9142424) + 60) * 160))) / 40.0) + 0.5) < 4294967300.0 else 0) & (1 if var9 >= 0.0 else 0)):
        break
    var7 = 0
    if 0:
        while True:  # loop $label3
            var2 = i32_load(9142440)
            var8 = i32_load(i32_load(9142424) + 64)
            if i32_load(i32_load(9142424) + 64):
                var3 = i32_load(9147312)
                var0 = i32_load(9147324)
                var0 = ((i32_load(9147324) << 11) ^ var0)
                var1 = (((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var0) & 0xFFFFFFFF) >> 8)) ^ var3) ^ var0)
                var4 = ((var2 & 0xFFFFFFFF) >> 1)
                var9 = float(((((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var0) & 0xFFFFFFFF) >> 8)) ^ var3) ^ var0) % (((var2 & 0xFFFFFFFF) >> 1) - 20)))
                var5 = i32_load(9147320)
                var2 = i32_load(9147316)
                var0 = i32_load(9142416)
                if (1 if i32_load(9142416) == 0 else 0):
                    var0 = (i32_load(41092) if i32_load8_u(9147210) else (i32_load(9142892) - 1))
                var0 = ((var5 << 11) ^ var5)
                var0 = (((((((var5 << 11) ^ var5) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var1)
                var10 = (((6.28318548 / float((4 if (1 if var0 < 3 else 0) else (var0 << (var0 & 1))))) * float(((((((((var5 << 11) ^ var5) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var1) % 100000))) / 100000.0)
                # Unknown: f64.convert_i32_u []
                var11 = var4
                var12 = ((float((func48((((6.28318548 / float((4 if (1 if var0 < 3 else 0) else (var0 << (var0 & 1))))) * float(((((((((var5 << 11) ^ var5) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var1) % 100000))) / 100000.0)) * var9)) + 0.5) + var4)
                if (1 if abs(((float((func48((((6.28318548 / float((4 if (1 if var0 < 3 else 0) else (var0 << (var0 & 1))))) * float(((((((((var5 << 11) ^ var5) & 0xFFFFFFFF) >> 8) ^ ((var1 & 0xFFFFFFFF) >> 19)) ^ var0) ^ var1) % 100000))) / 100000.0)) * var9)) + 0.5) + var4)) < 2147483648.0 else 0):
                    break
                var5 = -2147483648
                var11 = ((float((func49(var10) * var9)) + 0.5) + var11)
                if (1 if abs(((float((func49(var10) * var9)) + 0.5) + var11)) < 2147483648.0 else 0):
                    var4 = int(var11)
                    break
                var4 = -2147483648
                break
            var0 = i32_load(9147320)
            var0 = ((i32_load(9147320) << 11) ^ var0)
            var3 = i32_load(9147312)
            var1 = i32_load(9147324)
            var1 = ((i32_load(9147324) << 11) ^ var1)
            var1 = (((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var1) & 0xFFFFFFFF) >> 8)) ^ var3) ^ var1)
            var0 = (((((((i32_load(9147320) << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ (((((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var1) & 0xFFFFFFFF) >> 8)) ^ var3) ^ var1) & 0xFFFFFFFF) >> 19)) ^ var0) ^ var1)
            var5 = ((((((((i32_load(9147320) << 11) ^ var0) & 0xFFFFFFFF) >> 8) ^ (((((((i32_load(9147312) & 0xFFFFFFFF) >> 19) ^ ((((i32_load(9147324) << 11) ^ var1) & 0xFFFFFFFF) >> 8)) ^ var3) ^ var1) & 0xFFFFFFFF) >> 19)) ^ var0) ^ var1) % var2)
            var4 = (var1 % var2)
            var2 = i32_load(9147316)
            i32_store(9147320, var0)
            i32_store(9147324, var1)
            var0 = ((var2 << 11) ^ var2)
            var0 = ((var0 ^ (((var0 & 0xFFFFFFFF) >> 19) ^ ((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8))) ^ var0)
            i32_store(9147316, ((var0 ^ (((var0 & 0xFFFFFFFF) >> 19) ^ ((((var2 << 11) ^ var2) & 0xFFFFFFFF) >> 8))) ^ var0))
            var1 = ((var3 << 11) ^ var3)
            var1 = (((((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8) ^ ((var0 & 0xFFFFFFFF) >> 19)) ^ var1) ^ var0)
            i32_store(9147312, (((((((var3 << 11) ^ var3) & 0xFFFFFFFF) >> 8) ^ ((var0 & 0xFFFFFFFF) >> 19)) ^ var1) ^ var0))
            var6 = (var6 + 1)
            if (1 if (var6 + 1) != var7 else 0):
                continue
            break  # end loop
    return func126(var4, var5, ((var0 % 25) + 10), ((var1 % 25) + 10), (1 if var8 != 0 else 0))

