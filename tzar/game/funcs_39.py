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
# $func1023
# ==========================================================
def func1023(var0, var1):
    var2 = 0
    var0 = ((i32_load16_s(var0) + 4) >> 3)
    var2 = (((i32_load16_s(var0) + 4) >> 3) + i32_load8_u(var1))
    var2 = ((((i32_load16_s(var0) + 4) >> 3) + i32_load8_u(var1)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1, (255 if (1 if var2 >= 255 else 0) else ((((i32_load16_s(var0) + 4) >> 3) + i32_load8_u(var1)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 1))
    var2 = ((var0 + i32_load8_u(var1 + 1)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 1, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 1)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 2))
    var2 = ((var0 + i32_load8_u(var1 + 2)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 2, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 2)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 3))
    var2 = ((var0 + i32_load8_u(var1 + 3)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 3, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 3)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 32))
    var2 = ((var0 + i32_load8_u(var1 + 32)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 32, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 32)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 33))
    var2 = ((var0 + i32_load8_u(var1 + 33)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 33, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 33)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 34))
    var2 = ((var0 + i32_load8_u(var1 + 34)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 34, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 34)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 35))
    var2 = ((var0 + i32_load8_u(var1 + 35)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 35, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 35)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 64))
    var2 = ((var0 + i32_load8_u(var1 + 64)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 64, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 64)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 65))
    var2 = ((var0 + i32_load8_u(var1 + 65)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 65, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 65)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 66))
    var2 = ((var0 + i32_load8_u(var1 + 66)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 66, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 66)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 67))
    var2 = ((var0 + i32_load8_u(var1 + 67)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 67, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 67)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 96))
    var2 = ((var0 + i32_load8_u(var1 + 96)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 96, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 96)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 97))
    var2 = ((var0 + i32_load8_u(var1 + 97)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 97, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 97)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var0 + i32_load8_u(var1 + 98))
    var2 = ((var0 + i32_load8_u(var1 + 98)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 98, (255 if (1 if var2 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 98)) if (1 if var2 > 0 else 0) else 0)))
    var0 = (var0 + i32_load8_u(var1 + 99))
    var0 = ((var0 + i32_load8_u(var1 + 99)) if (1 if var0 > 0 else 0) else 0)
    i32_store8(var1 + 99, (255 if (1 if var0 >= 255 else 0) else ((var0 + i32_load8_u(var1 + 99)) if (1 if var0 > 0 else 0) else 0)))


# ==========================================================
# $func1024
# ==========================================================
def func1024(var0, var1):
    if i32_load16_u(var0):
        # call_indirect via table[i32_load(9687464)]
    if i32_load16_u(var0 + 32):
        # call_indirect via table[i32_load(9687464)]
    if i32_load16_u(var0 + 64):
        # call_indirect via table[i32_load(9687464)]
    if i32_load16_u(var0 + 96):
        # call_indirect via table[i32_load(9687464)]


# ==========================================================
# $func1025
# ==========================================================
def func1025(var0, var1):
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var4 = i32_load16_s(var0 + 2)
    var5 = (((i32_load16_s(var0 + 2) * 20091) >> 16) + var4)
    var3 = i32_load16_s(var0 + 8)
    var7 = ((i32_load16_s(var0 + 8) * 35468) >> 16)
    var6 = (i32_load16_s(var0) + 4)
    var2 = (((i32_load16_s(var0 + 8) * 35468) >> 16) + (i32_load16_s(var0) + 4))
    var0 = (i32_load8_u(var1 + 32) + (((((i32_load16_s(var0 + 2) * 20091) >> 16) + var4) + (((i32_load16_s(var0 + 8) * 35468) >> 16) + (i32_load16_s(var0) + 4))) >> 3))
    var0 = ((i32_load8_u(var1 + 32) + (((((i32_load16_s(var0 + 2) * 20091) >> 16) + var4) + (((i32_load16_s(var0 + 8) * 35468) >> 16) + (i32_load16_s(var0) + 4))) >> 3)) if (1 if var0 > 0 else 0) else 0)
    i32_store8(var1 + 32, (255 if (1 if var0 >= 255 else 0) else ((i32_load8_u(var1 + 32) + (((((i32_load16_s(var0 + 2) * 20091) >> 16) + var4) + (((i32_load16_s(var0 + 8) * 35468) >> 16) + (i32_load16_s(var0) + 4))) >> 3)) if (1 if var0 > 0 else 0) else 0)))
    var0 = ((var4 * 35468) >> 16)
    var4 = (i32_load8_u(var1 + 33) + ((var2 + ((var4 * 35468) >> 16)) >> 3))
    var4 = ((i32_load8_u(var1 + 33) + ((var2 + ((var4 * 35468) >> 16)) >> 3)) if (1 if var4 > 0 else 0) else 0)
    i32_store8(var1 + 33, (255 if (1 if var4 >= 255 else 0) else ((i32_load8_u(var1 + 33) + ((var2 + ((var4 * 35468) >> 16)) >> 3)) if (1 if var4 > 0 else 0) else 0)))
    var4 = (i32_load8_u(var1 + 34) + ((var2 - var0) >> 3))
    var4 = ((i32_load8_u(var1 + 34) + ((var2 - var0) >> 3)) if (1 if var4 > 0 else 0) else 0)
    i32_store8(var1 + 34, (255 if (1 if var4 >= 255 else 0) else ((i32_load8_u(var1 + 34) + ((var2 - var0) >> 3)) if (1 if var4 > 0 else 0) else 0)))
    var2 = (i32_load8_u(var1 + 35) + ((var2 - var5) >> 3))
    var2 = ((i32_load8_u(var1 + 35) + ((var2 - var5) >> 3)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 35, (255 if (1 if var2 >= 255 else 0) else ((i32_load8_u(var1 + 35) + ((var2 - var5) >> 3)) if (1 if var2 > 0 else 0) else 0)))
    var4 = (var3 + ((var3 * 20091) >> 16))
    var2 = ((var3 + ((var3 * 20091) >> 16)) + var6)
    var3 = (i32_load8_u(var1) + ((((var3 + ((var3 * 20091) >> 16)) + var6) + var5) >> 3))
    var3 = ((i32_load8_u(var1) + ((((var3 + ((var3 * 20091) >> 16)) + var6) + var5) >> 3)) if (1 if var3 > 0 else 0) else 0)
    i32_store8(var1, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1) + ((((var3 + ((var3 * 20091) >> 16)) + var6) + var5) >> 3)) if (1 if var3 > 0 else 0) else 0)))
    var3 = (i32_load8_u(var1 + 1) + ((var0 + var2) >> 3))
    var3 = ((i32_load8_u(var1 + 1) + ((var0 + var2) >> 3)) if (1 if var3 > 0 else 0) else 0)
    i32_store8(var1 + 1, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1 + 1) + ((var0 + var2) >> 3)) if (1 if var3 > 0 else 0) else 0)))
    var3 = (i32_load8_u(var1 + 2) + ((var2 - var0) >> 3))
    var3 = ((i32_load8_u(var1 + 2) + ((var2 - var0) >> 3)) if (1 if var3 > 0 else 0) else 0)
    i32_store8(var1 + 2, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1 + 2) + ((var2 - var0) >> 3)) if (1 if var3 > 0 else 0) else 0)))
    var2 = (i32_load8_u(var1 + 3) + ((var2 - var5) >> 3))
    var2 = ((i32_load8_u(var1 + 3) + ((var2 - var5) >> 3)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 3, (255 if (1 if var2 >= 255 else 0) else ((i32_load8_u(var1 + 3) + ((var2 - var5) >> 3)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (var6 - var7)
    var3 = (i32_load8_u(var1 + 64) + ((var5 + (var6 - var7)) >> 3))
    var3 = ((i32_load8_u(var1 + 64) + ((var5 + (var6 - var7)) >> 3)) if (1 if var3 > 0 else 0) else 0)
    i32_store8(var1 + 64, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1 + 64) + ((var5 + (var6 - var7)) >> 3)) if (1 if var3 > 0 else 0) else 0)))
    var3 = (i32_load8_u(var1 + 65) + ((var0 + var2) >> 3))
    var3 = ((i32_load8_u(var1 + 65) + ((var0 + var2) >> 3)) if (1 if var3 > 0 else 0) else 0)
    i32_store8(var1 + 65, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1 + 65) + ((var0 + var2) >> 3)) if (1 if var3 > 0 else 0) else 0)))
    var3 = (i32_load8_u(var1 + 66) + ((var2 - var0) >> 3))
    var3 = ((i32_load8_u(var1 + 66) + ((var2 - var0) >> 3)) if (1 if var3 > 0 else 0) else 0)
    i32_store8(var1 + 66, (255 if (1 if var3 >= 255 else 0) else ((i32_load8_u(var1 + 66) + ((var2 - var0) >> 3)) if (1 if var3 > 0 else 0) else 0)))
    var2 = (i32_load8_u(var1 + 67) + ((var2 - var5) >> 3))
    var2 = ((i32_load8_u(var1 + 67) + ((var2 - var5) >> 3)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 67, (255 if (1 if var2 >= 255 else 0) else ((i32_load8_u(var1 + 67) + ((var2 - var5) >> 3)) if (1 if var2 > 0 else 0) else 0)))
    var6 = (var6 - var4)
    var2 = (i32_load8_u(var1 + 96) + (((var6 - var4) + var5) >> 3))
    var2 = ((i32_load8_u(var1 + 96) + (((var6 - var4) + var5) >> 3)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 96, (255 if (1 if var2 >= 255 else 0) else ((i32_load8_u(var1 + 96) + (((var6 - var4) + var5) >> 3)) if (1 if var2 > 0 else 0) else 0)))
    var2 = (i32_load8_u(var1 + 97) + ((var0 + var6) >> 3))
    var2 = ((i32_load8_u(var1 + 97) + ((var0 + var6) >> 3)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 97, (255 if (1 if var2 >= 255 else 0) else ((i32_load8_u(var1 + 97) + ((var0 + var6) >> 3)) if (1 if var2 > 0 else 0) else 0)))
    var0 = (i32_load8_u(var1 + 98) + ((var6 - var0) >> 3))
    var0 = ((i32_load8_u(var1 + 98) + ((var6 - var0) >> 3)) if (1 if var0 > 0 else 0) else 0)
    i32_store8(var1 + 98, (255 if (1 if var0 >= 255 else 0) else ((i32_load8_u(var1 + 98) + ((var6 - var0) >> 3)) if (1 if var0 > 0 else 0) else 0)))
    var0 = (i32_load8_u(var1 + 99) + ((var6 - var5) >> 3))
    var0 = ((i32_load8_u(var1 + 99) + ((var6 - var5) >> 3)) if (1 if var0 > 0 else 0) else 0)
    i32_store8(var1 + 99, (255 if (1 if var0 >= 255 else 0) else ((i32_load8_u(var1 + 99) + ((var6 - var5) >> 3)) if (1 if var0 > 0 else 0) else 0)))


# ==========================================================
# $func1026
# ==========================================================
def func1026(var0):
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
    var2 = (i32_load(17088) - i32_load8_u((var0 - 33)))
    var1 = ((i32_load(17088) - i32_load8_u((var0 - 33))) + i32_load8_u((var0 - 1)))
    var11 = (var0 - 32)
    var3 = i32_load8_u((var0 - 32))
    i32_store8(var0, i32_load8_u((((i32_load(17088) - i32_load8_u((var0 - 33))) + i32_load8_u((var0 - 1))) + i32_load8_u((var0 - 32)))))
    var12 = (var0 - 31)
    var4 = i32_load8_u((var0 - 31))
    i32_store8(var0 + 1, i32_load8_u((var1 + i32_load8_u((var0 - 31)))))
    var13 = (var0 - 30)
    var5 = i32_load8_u((var0 - 30))
    i32_store8(var0 + 2, i32_load8_u((var1 + i32_load8_u((var0 - 30)))))
    var14 = (var0 - 29)
    var6 = i32_load8_u((var0 - 29))
    i32_store8(var0 + 3, i32_load8_u((var1 + i32_load8_u((var0 - 29)))))
    var15 = (var0 - 28)
    var7 = i32_load8_u((var0 - 28))
    i32_store8(var0 + 4, i32_load8_u((var1 + i32_load8_u((var0 - 28)))))
    var16 = (var0 - 27)
    var8 = i32_load8_u((var0 - 27))
    i32_store8(var0 + 5, i32_load8_u((var1 + i32_load8_u((var0 - 27)))))
    var17 = (var0 - 26)
    var9 = i32_load8_u((var0 - 26))
    i32_store8(var0 + 6, i32_load8_u((var1 + i32_load8_u((var0 - 26)))))
    var18 = (var0 - 25)
    var10 = i32_load8_u((var0 - 25))
    i32_store8(var0 + 7, i32_load8_u((var1 + i32_load8_u((var0 - 25)))))
    var1 = (var2 + i32_load8_u(var0 + 31))
    i32_store8(var0 + 32, i32_load8_u((var3 + (var2 + i32_load8_u(var0 + 31)))))
    i32_store8(var0 + 33, i32_load8_u((var1 + var4)))
    i32_store8(var0 + 34, i32_load8_u((var1 + var5)))
    i32_store8(var0 + 35, i32_load8_u((var1 + var6)))
    i32_store8(var0 + 36, i32_load8_u((var1 + var7)))
    i32_store8(var0 + 37, i32_load8_u((var1 + var8)))
    i32_store8(var0 + 38, i32_load8_u((var1 + var9)))
    i32_store8(var0 + 39, i32_load8_u((var1 + var10)))
    var1 = (var2 + i32_load8_u(var0 + 63))
    i32_store8(var0 + 64, i32_load8_u((var3 + (var2 + i32_load8_u(var0 + 63)))))
    i32_store8(var0 + 65, i32_load8_u((var1 + var4)))
    i32_store8(var0 + 66, i32_load8_u((var1 + var5)))
    i32_store8(var0 + 67, i32_load8_u((var1 + var6)))
    i32_store8(var0 + 68, i32_load8_u((var1 + var7)))
    i32_store8(var0 + 69, i32_load8_u((var1 + var8)))
    i32_store8(var0 + 70, i32_load8_u((var1 + var9)))
    i32_store8(var0 + 71, i32_load8_u((var1 + var10)))
    var1 = (var2 + i32_load8_u(var0 + 95))
    var3 = i32_load8_u(var11)
    i32_store8(var0 + 96, i32_load8_u(((var2 + i32_load8_u(var0 + 95)) + i32_load8_u(var11))))
    var4 = i32_load8_u(var12)
    i32_store8(var0 + 97, i32_load8_u((var1 + i32_load8_u(var12))))
    var5 = i32_load8_u(var13)
    i32_store8(var0 + 98, i32_load8_u((var1 + i32_load8_u(var13))))
    var6 = i32_load8_u(var14)
    i32_store8(var0 + 99, i32_load8_u((var1 + i32_load8_u(var14))))
    var7 = i32_load8_u(var15)
    i32_store8(var0 + 100, i32_load8_u((var1 + i32_load8_u(var15))))
    var8 = i32_load8_u(var16)
    i32_store8(var0 + 101, i32_load8_u((var1 + i32_load8_u(var16))))
    var9 = i32_load8_u(var17)
    i32_store8(var0 + 102, i32_load8_u((var1 + i32_load8_u(var17))))
    var10 = i32_load8_u(var18)
    i32_store8(var0 + 103, i32_load8_u((var1 + i32_load8_u(var18))))
    var1 = (var2 + i32_load8_u(var0 + 127))
    i32_store8(var0 + 128, i32_load8_u((var3 + (var2 + i32_load8_u(var0 + 127)))))
    i32_store8(var0 + 129, i32_load8_u((var1 + var4)))
    i32_store8(var0 + 130, i32_load8_u((var1 + var5)))
    i32_store8(var0 + 131, i32_load8_u((var1 + var6)))
    i32_store8(var0 + 132, i32_load8_u((var1 + var7)))
    i32_store8(var0 + 133, i32_load8_u((var1 + var8)))
    i32_store8(var0 + 134, i32_load8_u((var1 + var9)))
    i32_store8(var0 + 135, i32_load8_u((var1 + var10)))
    var1 = (var2 + i32_load8_u(var0 + 159))
    i32_store8(var0 + 160, i32_load8_u((var3 + (var2 + i32_load8_u(var0 + 159)))))
    i32_store8(var0 + 161, i32_load8_u((var1 + var4)))
    i32_store8(var0 + 162, i32_load8_u((var1 + var5)))
    i32_store8(var0 + 163, i32_load8_u((var1 + var6)))
    i32_store8(var0 + 164, i32_load8_u((var1 + var7)))
    i32_store8(var0 + 165, i32_load8_u((var1 + var8)))
    i32_store8(var0 + 166, i32_load8_u((var1 + var9)))
    i32_store8(var0 + 167, i32_load8_u((var1 + var10)))
    var1 = (var2 + i32_load8_u(var0 + 191))
    i32_store8(var0 + 192, i32_load8_u(((var2 + i32_load8_u(var0 + 191)) + i32_load8_u(var11))))
    i32_store8(var0 + 193, i32_load8_u((var1 + i32_load8_u(var12))))
    i32_store8(var0 + 194, i32_load8_u((var1 + i32_load8_u(var13))))
    i32_store8(var0 + 195, i32_load8_u((var1 + i32_load8_u(var14))))
    i32_store8(var0 + 196, i32_load8_u((var1 + i32_load8_u(var15))))
    i32_store8(var0 + 197, i32_load8_u((var1 + i32_load8_u(var16))))
    i32_store8(var0 + 198, i32_load8_u((var1 + i32_load8_u(var17))))
    i32_store8(var0 + 199, i32_load8_u((var1 + i32_load8_u(var18))))
    var2 = (var2 + i32_load8_u(var0 + 223))
    i32_store8(var0 + 224, i32_load8_u(((var2 + i32_load8_u(var0 + 223)) + i32_load8_u(var11))))
    i32_store8(var0 + 225, i32_load8_u((var2 + i32_load8_u(var12))))
    i32_store8(var0 + 226, i32_load8_u((var2 + i32_load8_u(var13))))
    i32_store8(var0 + 227, i32_load8_u((var2 + i32_load8_u(var14))))
    i32_store8(var0 + 228, i32_load8_u((var2 + i32_load8_u(var15))))
    i32_store8(var0 + 229, i32_load8_u((var2 + i32_load8_u(var16))))
    i32_store8(var0 + 230, i32_load8_u((var2 + i32_load8_u(var17))))
    i32_store8(var0 + 231, i32_load8_u((var2 + i32_load8_u(var18))))

