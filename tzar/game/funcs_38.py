"""
Auto-generated from WAT. Contains 10 functions.
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
# $func997
# ==========================================================
def func997(var0, var1, var2):
    var3 = 0
    if (1 if var1 > 0 else 0):
        var3 = (var0 + (var1 << 2))
        while True:  # loop $label0
            var1 = i32_load(var0)
            i32_store8(var2 + 2, i32_load(var0))
            i32_store8(var2 + 3, ((var1 & 0xFFFFFFFF) >> 24))
            i32_store8(var2 + 1, ((var1 & 0xFFFFFFFF) >> 8))
            i32_store8(var2, ((var1 & 0xFFFFFFFF) >> 16))
            var2 = (var2 + 4)
            var0 = (var0 + 4)
            if (1 if (var0 + 4) < var3 else 0):
                continue
            break  # end loop


# ==========================================================
# $func998
# ==========================================================
def func998(var0, var1, var2):
    var3 = 0
    if (1 if var1 > 0 else 0):
        var3 = (var0 + (var1 << 2))
        while True:  # loop $label0
            var1 = i32_load(var0)
            i32_store8(var2 + 1, ((i32_load(var0) & 240) | ((var1 & 0xFFFFFFFF) >> 28)))
            i32_store8(var2, ((((var1 & 0xFFFFFFFF) >> 16) & 240) | (((var1 & 0xFFFFFFFF) >> 12) & 15)))
            var2 = (var2 + 2)
            var0 = (var0 + 4)
            if (1 if (var0 + 4) < var3 else 0):
                continue
            break  # end loop


# ==========================================================
# $func999
# ==========================================================
def func999(var0, var1, var2):
    var3 = 0
    if (1 if var1 > 0 else 0):
        var3 = (var0 + (var1 << 2))
        while True:  # loop $label0
            var1 = i32_load(var0)
            i32_store8(var2 + 1, ((((i32_load(var0) & 0xFFFFFFFF) >> 5) & 224) | (((var1 & 0xFFFFFFFF) >> 3) & 31)))
            i32_store8(var2, ((((var1 & 0xFFFFFFFF) >> 16) & 248) | (((var1 & 0xFFFFFFFF) >> 13) & 7)))
            var2 = (var2 + 2)
            var0 = (var0 + 4)
            if (1 if (var0 + 4) < var3 else 0):
                continue
            break  # end loop


# ==========================================================
# $func1000
# ==========================================================
def func1000(var0, var1, var2):
    var3 = 0
    if (1 if var1 > 0 else 0):
        var3 = (var0 + (var1 << 2))
        while True:  # loop $label0
            var1 = i32_load(var0)
            i32_store8(var2, i32_load(var0))
            i32_store8(var2 + 2, ((var1 & 0xFFFFFFFF) >> 16))
            i32_store8(var2 + 1, ((var1 & 0xFFFFFFFF) >> 8))
            var2 = (var2 + 3)
            var0 = (var0 + 4)
            if (1 if (var0 + 4) < var3 else 0):
                continue
            break  # end loop


# ==========================================================
# $func1001
# ==========================================================
def func1001(var0, var1, var2):
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    if (1 if var1 <= 0 else 0):
        break
    if (1 if var1 != 1 else 0):
        var7 = (var1 & -2)
        while True:  # loop $label1
            var3 = (var4 << 2)
            var5 = i32_load((var0 + var3))
            var8 = ((i32_load((var0 + var3)) & 0xFFFFFFFF) >> 8)
            i32_store((var2 + (var4 << 2)), (((((((i32_load((var0 + var3)) & 0xFFFFFFFF) >> 8) & 255) + (var5 & 16711935)) + (var8 << 16)) & 16711935) | (var5 & -16711936)))
            var3 = (var3 | 4)
            var3 = i32_load((var0 + var3))
            var5 = ((i32_load((var0 + var3)) & 0xFFFFFFFF) >> 8)
            i32_store((var2 + (var3 | 4)), (((((((i32_load((var0 + var3)) & 0xFFFFFFFF) >> 8) & 255) + (var3 & 16711935)) + (var5 << 16)) & 16711935) | (var3 & -16711936)))
            var4 = (var4 + 2)
            var6 = (var6 + 2)
            if (1 if (var6 + 2) != var7 else 0):
                continue
            break  # end loop
    if (1 if (var1 & 1) == 0 else 0):
        break
    var1 = (var4 << 2)
    var0 = i32_load((var0 + var1))
    var1 = ((i32_load((var0 + var1)) & 0xFFFFFFFF) >> 8)
    i32_store((var2 + (var4 << 2)), (((((((i32_load((var0 + var1)) & 0xFFFFFFFF) >> 8) & 255) + (var0 & 16711935)) + (var1 << 16)) & 16711935) | (var0 & -16711936)))


# ==========================================================
# $func1002
# ==========================================================
def func1002(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var5 = i32_load8_u((var0 - 31))
    var1 = (i32_load8_u((var0 - 31)) + 1)
    var2 = i32_load8_u((var0 - 30))
    var3 = ((((i32_load8_u((var0 - 31)) + 1) + i32_load8_u((var0 - 30))) & 0xFFFFFFFF) >> 1)
    i32_store8(var0 + 64, ((((i32_load8_u((var0 - 31)) + 1) + i32_load8_u((var0 - 30))) & 0xFFFFFFFF) >> 1))
    var6 = i32_load8_u((var0 - 32))
    i32_store8(var0, (((var1 + i32_load8_u((var0 - 32))) & 0xFFFFFFFF) >> 1))
    var1 = i32_load8_u((var0 - 29))
    var4 = ((((var2 + i32_load8_u((var0 - 29))) + 1) & 0xFFFFFFFF) >> 1)
    i32_store8(var0 + 65, ((((var2 + i32_load8_u((var0 - 29))) + 1) & 0xFFFFFFFF) >> 1))
    i32_store8(var0 + 1, var3)
    var3 = i32_load8_u((var0 - 28))
    var7 = ((((var1 + i32_load8_u((var0 - 28))) + 1) & 0xFFFFFFFF) >> 1)
    i32_store8(var0 + 66, ((((var1 + i32_load8_u((var0 - 28))) + 1) & 0xFFFFFFFF) >> 1))
    i32_store8(var0 + 2, var4)
    i32_store8(var0 + 3, var7)
    var4 = (var1 + 2)
    var7 = ((((var5 + (var1 + 2)) + (var2 << 1)) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 96, ((((var5 + (var1 + 2)) + (var2 << 1)) & 0xFFFFFFFF) >> 2))
    var2 = (var2 + 2)
    i32_store8(var0 + 32, ((((var6 + (var2 + 2)) + (var5 << 1)) & 0xFFFFFFFF) >> 2))
    var5 = (((var3 + (var2 + (var1 << 1))) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 97, (((var3 + (var2 + (var1 << 1))) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 33, var7)
    var6 = i32_load8_u((var0 - 25))
    var2 = i32_load8_u((var0 - 26))
    var1 = i32_load8_u((var0 - 27))
    var4 = (((i32_load8_u((var0 - 27)) + (var4 + (var3 << 1))) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 98, (((i32_load8_u((var0 - 27)) + (var4 + (var3 << 1))) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 34, var5)
    i32_store8(var0 + 99, ((((var6 + (var1 + (var2 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 67, ((((var2 + (var3 + (var1 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 35, var4)


# ==========================================================
# $func1007
# ==========================================================
def func1007(var0):
    var1 = 0
    var1 = i64_load((var0 - 32))
    i64_store(var0 + 224, i64_load((var0 - 32)))
    i64_store(var0 + 192, var1)
    i64_store(var0 + 160, var1)
    i64_store(var0 + 128, var1)
    i64_store(var0 + 96, var1)
    i64_store(var0 + 64, var1)
    i64_store(var0 + 32, var1)
    i64_store(var0, var1)


# ==========================================================
# $func1008
# ==========================================================
def func1008(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = i32_load8_u((var0 - 30))
    var3 = (i32_load8_u((var0 - 30)) + 2)
    var1 = i32_load8_u((var0 - 29))
    var4 = (((i32_load8_u((var0 - 28)) + ((i32_load8_u((var0 - 30)) + 2) + (i32_load8_u((var0 - 29)) << 1))) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 99, (((i32_load8_u((var0 - 28)) + ((i32_load8_u((var0 - 30)) + 2) + (i32_load8_u((var0 - 29)) << 1))) & 0xFFFFFFFF) >> 2))
    var5 = i32_load8_u((var0 - 31))
    var6 = (i32_load8_u((var0 - 31)) + 2)
    var2 = (((var1 + ((i32_load8_u((var0 - 31)) + 2) + (var2 << 1))) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 98, (((var1 + ((i32_load8_u((var0 - 31)) + 2) + (var2 << 1))) & 0xFFFFFFFF) >> 2))
    var1 = i32_load8_u((var0 - 32))
    var3 = ((((var3 + i32_load8_u((var0 - 32))) + (var5 << 1)) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 97, ((((var3 + i32_load8_u((var0 - 32))) + (var5 << 1)) & 0xFFFFFFFF) >> 2))
    var1 = ((((var6 + i32_load8_u((var0 - 33))) + (var1 << 1)) & 0xFFFFFFFF) >> 2)
    i32_store8(var0 + 96, ((((var6 + i32_load8_u((var0 - 33))) + (var1 << 1)) & 0xFFFFFFFF) >> 2))
    i32_store8(var0 + 67, var4)
    i32_store8(var0 + 66, var2)
    i32_store8(var0 + 65, var3)
    i32_store8(var0 + 64, var1)
    i32_store8(var0 + 35, var4)
    i32_store8(var0 + 34, var2)
    i32_store8(var0 + 33, var3)
    i32_store8(var0 + 32, var1)
    i32_store8(var0 + 3, var4)
    i32_store8(var0 + 2, var2)
    i32_store8(var0 + 1, var3)
    i32_store8(var0, var1)


# ==========================================================
# $func1009
# ==========================================================
def func1009(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var3 = (var0 - 32)
    var1 = i64_load((var0 - 32))
    i64_store(var0, i64_load((var0 - 32)))
    i64_store(var0 + 32, var1)
    i64_store(var0 + 64, var1)
    i64_store(var0 + 96, var1)
    i64_store(var0 + 128, var1)
    i64_store(var0 + 160, var1)
    i64_store(var0 + 192, var1)
    i64_store(var0 + 224, var1)
    var1 = i64_load(var3 + 8)
    i64_store(var0 + 8, i64_load(var3 + 8))
    i64_store(var0 + 40, var1)
    i64_store(var0 + 72, var1)
    i64_store(var0 + 104, var1)
    i64_store(var0 + 136, var1)
    i64_store(var0 + 168, var1)
    i64_store(var0 + 200, var1)
    i64_store(var0 + 232, var1)
    var1 = i64_load(var3 + 8)
    i64_store(var0 + 264, i64_load(var3 + 8))
    var2 = i64_load(var3)
    i64_store(var0 + 256, i64_load(var3))
    i64_store(var0 + 296, var1)
    i64_store(var0 + 288, var2)
    i64_store(var0 + 328, var1)
    i64_store(var0 + 320, var2)
    i64_store(var0 + 360, var1)
    i64_store(var0 + 352, var2)
    i64_store(var0 + 384, var2)
    i64_store(var0 + 392, var1)
    i64_store(var0 + 424, var1)
    i64_store(var0 + 416, var2)
    i64_store(var0 + 448, var2)
    i64_store(var0 + 456, var1)
    i64_store(var0 + 488, var1)
    i64_store(var0 + 480, var2)


# ==========================================================
# $func1020
# ==========================================================
def func1020(var0, var1):
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
    var20 = 0
    var21 = 0
    var22 = 0
    var23 = 0
    var24 = 0
    var25 = 0
    var26 = 0
    var27 = 0
    var28 = 0
    var29 = 0
    var30 = 0
    var3 = i32_load16_s(var0)
    var6 = i32_load16_s(var0 + 24)
    var4 = (i32_load16_s(var0) - i32_load16_s(var0 + 24))
    var2 = i32_load16_s(var0 + 8)
    var7 = i32_load16_s(var0 + 16)
    var11 = (i32_load16_s(var0 + 8) - i32_load16_s(var0 + 16))
    var8 = (((i32_load16_s(var0) - i32_load16_s(var0 + 24)) - (i32_load16_s(var0 + 8) - i32_load16_s(var0 + 16))) + 3)
    var5 = i32_load16_s(var0 + 6)
    var9 = i32_load16_s(var0 + 30)
    var12 = (i32_load16_s(var0 + 6) - i32_load16_s(var0 + 30))
    var13 = i32_load16_s(var0 + 14)
    var14 = i32_load16_s(var0 + 22)
    var18 = (i32_load16_s(var0 + 14) - i32_load16_s(var0 + 22))
    var10 = ((i32_load16_s(var0 + 6) - i32_load16_s(var0 + 30)) - (i32_load16_s(var0 + 14) - i32_load16_s(var0 + 22)))
    var15 = ((((i32_load16_s(var0) - i32_load16_s(var0 + 24)) - (i32_load16_s(var0 + 8) - i32_load16_s(var0 + 16))) + 3) - ((i32_load16_s(var0 + 6) - i32_load16_s(var0 + 30)) - (i32_load16_s(var0 + 14) - i32_load16_s(var0 + 22))))
    var16 = i32_load16_s(var0 + 2)
    var17 = i32_load16_s(var0 + 26)
    var19 = (i32_load16_s(var0 + 2) - i32_load16_s(var0 + 26))
    var20 = i32_load16_s(var0 + 10)
    var21 = i32_load16_s(var0 + 18)
    var22 = (i32_load16_s(var0 + 10) - i32_load16_s(var0 + 18))
    var23 = ((i32_load16_s(var0 + 2) - i32_load16_s(var0 + 26)) - (i32_load16_s(var0 + 10) - i32_load16_s(var0 + 18)))
    var24 = i32_load16_s(var0 + 4)
    var25 = i32_load16_s(var0 + 28)
    var26 = (i32_load16_s(var0 + 4) - i32_load16_s(var0 + 28))
    var27 = i32_load16_s(var0 + 12)
    var0 = i32_load16_s(var0 + 20)
    var28 = (i32_load16_s(var0 + 12) - i32_load16_s(var0 + 20))
    var29 = ((i32_load16_s(var0 + 4) - i32_load16_s(var0 + 28)) - (i32_load16_s(var0 + 12) - i32_load16_s(var0 + 20)))
    var30 = (((i32_load16_s(var0 + 2) - i32_load16_s(var0 + 26)) - (i32_load16_s(var0 + 10) - i32_load16_s(var0 + 18))) - ((i32_load16_s(var0 + 4) - i32_load16_s(var0 + 28)) - (i32_load16_s(var0 + 12) - i32_load16_s(var0 + 20))))
    i32_store16(var1 + 480, (((((((i32_load16_s(var0) - i32_load16_s(var0 + 24)) - (i32_load16_s(var0 + 8) - i32_load16_s(var0 + 16))) + 3) - ((i32_load16_s(var0 + 6) - i32_load16_s(var0 + 30)) - (i32_load16_s(var0 + 14) - i32_load16_s(var0 + 22)))) - (((i32_load16_s(var0 + 2) - i32_load16_s(var0 + 26)) - (i32_load16_s(var0 + 10) - i32_load16_s(var0 + 18))) - ((i32_load16_s(var0 + 4) - i32_load16_s(var0 + 28)) - (i32_load16_s(var0 + 12) - i32_load16_s(var0 + 20))))) & 0xFFFFFFFF) >> 3))
    var8 = (var8 + var10)
    var10 = (var23 + var29)
    i32_store16(var1 + 448, ((((var8 + var10) - (var23 + var29)) & 0xFFFFFFFF) >> 3))
    i32_store16(var1 + 416, (((var15 + var30) & 0xFFFFFFFF) >> 3))
    i32_store16(var1 + 384, (((var8 + var10) & 0xFFFFFFFF) >> 3))
    var3 = (var3 + var6)
    var6 = (var2 + var7)
    var2 = (((var3 + var6) - (var2 + var7)) + 3)
    var7 = (var5 + var9)
    var8 = (var13 + var14)
    var5 = ((var5 + var9) - (var13 + var14))
    var9 = ((((var3 + var6) - (var2 + var7)) + 3) - ((var5 + var9) - (var13 + var14)))
    var13 = (var16 + var17)
    var14 = (var20 + var21)
    var10 = ((var16 + var17) - (var20 + var21))
    var15 = (var24 + var25)
    var0 = (var0 + var27)
    var16 = ((var24 + var25) - (var0 + var27))
    var17 = (((var16 + var17) - (var20 + var21)) - ((var24 + var25) - (var0 + var27)))
    i32_store16(var1 + 352, (((((((var3 + var6) - (var2 + var7)) + 3) - ((var5 + var9) - (var13 + var14))) - (((var16 + var17) - (var20 + var21)) - ((var24 + var25) - (var0 + var27)))) & 0xFFFFFFFF) >> 3))
    var2 = (var2 + var5)
    var5 = (var10 + var16)
    i32_store16(var1 + 320, ((((var2 + var5) - (var10 + var16)) & 0xFFFFFFFF) >> 3))
    i32_store16(var1 + 288, (((var9 + var17) & 0xFFFFFFFF) >> 3))
    i32_store16(var1 + 256, (((var2 + var5) & 0xFFFFFFFF) >> 3))
    var4 = ((var4 + var11) + 3)
    var2 = (var12 + var18)
    var11 = (((var4 + var11) + 3) - (var12 + var18))
    var5 = (var19 + var22)
    var9 = (var26 + var28)
    var12 = ((var19 + var22) - (var26 + var28))
    i32_store16(var1 + 224, ((((((var4 + var11) + 3) - (var12 + var18)) - ((var19 + var22) - (var26 + var28))) & 0xFFFFFFFF) >> 3))
    var4 = (var2 + var4)
    var2 = (var5 + var9)
    i32_store16(var1 + 192, ((((var2 + var4) - (var5 + var9)) & 0xFFFFFFFF) >> 3))
    i32_store16(var1 + 160, (((var11 + var12) & 0xFFFFFFFF) >> 3))
    i32_store16(var1 + 128, (((var2 + var4) & 0xFFFFFFFF) >> 3))
    var3 = ((var3 + var6) + 3)
    var6 = (var7 + var8)
    var4 = (((var3 + var6) + 3) - (var7 + var8))
    var2 = (var13 + var14)
    var0 = (var0 + var15)
    var7 = ((var13 + var14) - (var0 + var15))
    i32_store16(var1 + 96, ((((((var3 + var6) + 3) - (var7 + var8)) - ((var13 + var14) - (var0 + var15))) & 0xFFFFFFFF) >> 3))
    var3 = (var3 + var6)
    var0 = (var0 + var2)
    i32_store16(var1 + 64, ((((var3 + var6) - (var0 + var2)) & 0xFFFFFFFF) >> 3))
    i32_store16(var1 + 32, (((var4 + var7) & 0xFFFFFFFF) >> 3))
    i32_store16(var1, (((var0 + var3) & 0xFFFFFFFF) >> 3))

