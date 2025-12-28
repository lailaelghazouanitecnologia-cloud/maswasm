"""
Auto-generated from WAT. Contains 6 functions.
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
# $func1027
# ==========================================================
def func1027(var0):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var2 = (i32_load(17088) - i32_load8_u((var0 - 33)))
    var1 = ((i32_load(17088) - i32_load8_u((var0 - 33))) + i32_load8_u((var0 - 1)))
    var3 = i32_load8_u((var0 - 32))
    i32_store8(var0, i32_load8_u((((i32_load(17088) - i32_load8_u((var0 - 33))) + i32_load8_u((var0 - 1))) + i32_load8_u((var0 - 32)))))
    var4 = i32_load8_u((var0 - 31))
    i32_store8(var0 + 1, i32_load8_u((var1 + i32_load8_u((var0 - 31)))))
    var5 = i32_load8_u((var0 - 30))
    i32_store8(var0 + 2, i32_load8_u((var1 + i32_load8_u((var0 - 30)))))
    var6 = i32_load8_u((var0 - 29))
    i32_store8(var0 + 3, i32_load8_u((var1 + i32_load8_u((var0 - 29)))))
    var1 = (var2 + i32_load8_u(var0 + 31))
    i32_store8(var0 + 32, i32_load8_u((var3 + (var2 + i32_load8_u(var0 + 31)))))
    i32_store8(var0 + 33, i32_load8_u((var1 + var4)))
    i32_store8(var0 + 34, i32_load8_u((var1 + var5)))
    i32_store8(var0 + 35, i32_load8_u((var1 + var6)))
    var1 = (var2 + i32_load8_u(var0 + 63))
    i32_store8(var0 + 64, i32_load8_u((var3 + (var2 + i32_load8_u(var0 + 63)))))
    i32_store8(var0 + 65, i32_load8_u((var1 + var4)))
    i32_store8(var0 + 66, i32_load8_u((var1 + var5)))
    i32_store8(var0 + 67, i32_load8_u((var1 + var6)))
    var2 = (var2 + i32_load8_u(var0 + 95))
    i32_store8(var0 + 96, i32_load8_u((var3 + (var2 + i32_load8_u(var0 + 95)))))
    i32_store8(var0 + 97, i32_load8_u((var2 + var4)))
    i32_store8(var0 + 98, i32_load8_u((var2 + var5)))
    i32_store8(var0 + 99, i32_load8_u((var2 + var6)))


# ==========================================================
# $func1028
# ==========================================================
def func1028(var0):
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
    var3 = (var0 - 17)
    var4 = (var0 - 18)
    var5 = (var0 - 19)
    var6 = (var0 - 20)
    var7 = (var0 - 21)
    var8 = (var0 - 22)
    var9 = (var0 - 23)
    var10 = (var0 - 24)
    var11 = (var0 - 25)
    var12 = (var0 - 26)
    var13 = (var0 - 27)
    var14 = (var0 - 28)
    var15 = (var0 - 29)
    var16 = (var0 - 30)
    var17 = (var0 - 31)
    var18 = (var0 - 32)
    var19 = (i32_load(17088) - i32_load8_u((var0 - 33)))
    while True:  # loop $label0
        var1 = (var19 + i32_load8_u((var0 - 1)))
        i32_store8(var0, i32_load8_u(((var19 + i32_load8_u((var0 - 1))) + i32_load8_u(var18))))
        i32_store8(var0 + 1, i32_load8_u((var1 + i32_load8_u(var17))))
        i32_store8(var0 + 2, i32_load8_u((var1 + i32_load8_u(var16))))
        i32_store8(var0 + 3, i32_load8_u((var1 + i32_load8_u(var15))))
        i32_store8(var0 + 4, i32_load8_u((var1 + i32_load8_u(var14))))
        i32_store8(var0 + 5, i32_load8_u((var1 + i32_load8_u(var13))))
        i32_store8(var0 + 6, i32_load8_u((var1 + i32_load8_u(var12))))
        i32_store8(var0 + 7, i32_load8_u((var1 + i32_load8_u(var11))))
        i32_store8(var0 + 8, i32_load8_u((var1 + i32_load8_u(var10))))
        i32_store8(var0 + 9, i32_load8_u((var1 + i32_load8_u(var9))))
        i32_store8(var0 + 10, i32_load8_u((var1 + i32_load8_u(var8))))
        i32_store8(var0 + 11, i32_load8_u((var1 + i32_load8_u(var7))))
        i32_store8(var0 + 12, i32_load8_u((var1 + i32_load8_u(var6))))
        i32_store8(var0 + 13, i32_load8_u((var1 + i32_load8_u(var5))))
        i32_store8(var0 + 14, i32_load8_u((var1 + i32_load8_u(var4))))
        i32_store8(var0 + 15, i32_load8_u((var1 + i32_load8_u(var3))))
        var0 = (var0 + 32)
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != 16 else 0):
            continue
        break  # end loop


# ==========================================================
# $func1030
# ==========================================================
def func1030(var0, var1, var2):
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
    var12 = (0 - var1)
    var11 = (var1 << 2)
    var6 = (var0 + (var1 << 2))
    var13 = (0 - (var1 << 1))
    var14 = ((var2 << 1) | 1)
    var0 = i32_load(17088)
    var2 = i32_load(16308)
    var15 = i32_load(16076)
    var10 = i32_load(17616)
    while True:  # loop $label0
        var3 = (var4 + var6)
        var7 = ((var4 + var6) + var12)
        var8 = i32_load8_u(((var4 + var6) + var12))
        var9 = i32_load8_u(var3)
        var5 = (i32_load8_u((var3 + var13)) - i32_load8_u((var1 + var3)))
        if (1 if var14 >= ((i32_load8_u((var10 + (i32_load8_u(((var4 + var6) + var12)) - i32_load8_u(var3)))) << 2) + i32_load8_u((var10 + (i32_load8_u((var3 + var13)) - i32_load8_u((var1 + var3)))))) else 0):
            var5 = (i32_load8_s((var5 + var15)) + ((var9 - var8) * 3))
            var16 = i32_load8_s((var2 + (((i32_load8_s((var5 + var15)) + ((var9 - var8) * 3)) + 4) >> 3)))
            i32_store8(var7, i32_load8_u((var0 + (i32_load8_s((var2 + ((var5 + 3) >> 3))) + var8))))
            i32_store8(var3, i32_load8_u((var0 + (var9 - var16))))
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != 16 else 0):
            continue
        break  # end loop
    var6 = (var6 + var11)
    var4 = 0
    while True:  # loop $label1
        var3 = (var4 + var6)
        var7 = ((var4 + var6) + var12)
        var8 = i32_load8_u(((var4 + var6) + var12))
        var9 = i32_load8_u(var3)
        var5 = (i32_load8_u((var3 + var13)) - i32_load8_u((var1 + var3)))
        if (1 if var14 >= ((i32_load8_u((var10 + (i32_load8_u(((var4 + var6) + var12)) - i32_load8_u(var3)))) << 2) + i32_load8_u((var10 + (i32_load8_u((var3 + var13)) - i32_load8_u((var1 + var3)))))) else 0):
            var5 = (i32_load8_s((var5 + var15)) + ((var9 - var8) * 3))
            var16 = i32_load8_s((var2 + (((i32_load8_s((var5 + var15)) + ((var9 - var8) * 3)) + 4) >> 3)))
            i32_store8(var7, i32_load8_u((var0 + (i32_load8_s((var2 + ((var5 + 3) >> 3))) + var8))))
            i32_store8(var3, i32_load8_u((var0 + (var9 - var16))))
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != 16 else 0):
            continue
        break  # end loop
    var8 = (var6 + var11)
    var4 = 0
    while True:  # loop $label2
        var3 = (var4 + var8)
        var9 = ((var4 + var8) + var12)
        var11 = i32_load8_u(((var4 + var8) + var12))
        var6 = i32_load8_u(var3)
        var7 = (i32_load8_u((var3 + var13)) - i32_load8_u((var1 + var3)))
        if (1 if var14 >= ((i32_load8_u((var10 + (i32_load8_u(((var4 + var8) + var12)) - i32_load8_u(var3)))) << 2) + i32_load8_u((var10 + (i32_load8_u((var3 + var13)) - i32_load8_u((var1 + var3)))))) else 0):
            var7 = (i32_load8_s((var7 + var15)) + ((var6 - var11) * 3))
            var5 = i32_load8_s((var2 + (((i32_load8_s((var7 + var15)) + ((var6 - var11) * 3)) + 4) >> 3)))
            i32_store8(var9, i32_load8_u((var0 + (i32_load8_s((var2 + ((var7 + 3) >> 3))) + var11))))
            i32_store8(var3, i32_load8_u((var0 + (var6 - var5))))
        var4 = (var4 + 1)
        if (1 if (var4 + 1) != 16 else 0):
            continue
        break  # end loop


# ==========================================================
# $func1031
# ==========================================================
def func1031(var0, var1, var2):
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
    var10 = (0 - var1)
    var11 = (0 - (var1 << 1))
    var12 = ((var2 << 1) | 1)
    var5 = i32_load(17088)
    var6 = i32_load(16308)
    var13 = i32_load(16076)
    var7 = i32_load(17616)
    while True:  # loop $label0
        var2 = (var0 + var3)
        var14 = ((var0 + var3) + var10)
        var8 = i32_load8_u(((var0 + var3) + var10))
        var9 = i32_load8_u(var2)
        var4 = (i32_load8_u((var2 + var11)) - i32_load8_u((var1 + var2)))
        if (1 if var12 >= ((i32_load8_u((var7 + (i32_load8_u(((var0 + var3) + var10)) - i32_load8_u(var2)))) << 2) + i32_load8_u((var7 + (i32_load8_u((var2 + var11)) - i32_load8_u((var1 + var2)))))) else 0):
            var4 = (i32_load8_s((var4 + var13)) + ((var9 - var8) * 3))
            var15 = i32_load8_s((var6 + (((i32_load8_s((var4 + var13)) + ((var9 - var8) * 3)) + 4) >> 3)))
            i32_store8(var14, i32_load8_u((var5 + (i32_load8_s((var6 + ((var4 + 3) >> 3))) + var8))))
            i32_store8(var2, i32_load8_u((var5 + (var9 - var15))))
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != 16 else 0):
            continue
        break  # end loop


# ==========================================================
# $func1032
# ==========================================================
def func1032(var0, var1, var2):
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
    var11 = (var0 + 4)
    var12 = ((var2 << 1) | 1)
    var2 = 0
    var8 = i32_load(17088)
    var9 = i32_load(16308)
    var13 = i32_load(16076)
    var10 = i32_load(17616)
    while True:  # loop $label0
        var3 = (var11 + (var1 * var2))
        var6 = ((var11 + (var1 * var2)) - 1)
        var5 = i32_load8_u(((var11 + (var1 * var2)) - 1))
        var7 = i32_load8_u(var3)
        var4 = (i32_load8_u((var3 - 2)) - i32_load8_u(var3 + 1))
        if (1 if var12 >= ((i32_load8_u((var10 + (i32_load8_u(((var11 + (var1 * var2)) - 1)) - i32_load8_u(var3)))) << 2) + i32_load8_u((var10 + (i32_load8_u((var3 - 2)) - i32_load8_u(var3 + 1))))) else 0):
            var4 = (i32_load8_s((var4 + var13)) + ((var7 - var5) * 3))
            var14 = i32_load8_s((var9 + (((i32_load8_s((var4 + var13)) + ((var7 - var5) * 3)) + 4) >> 3)))
            i32_store8(var6, i32_load8_u((var8 + (i32_load8_s((var9 + ((var4 + 3) >> 3))) + var5))))
            i32_store8(var3, i32_load8_u((var8 + (var7 - var14))))
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != 16 else 0):
            continue
        break  # end loop
    var11 = (var0 + 8)
    var2 = 0
    while True:  # loop $label1
        var3 = (var11 + (var1 * var2))
        var6 = ((var11 + (var1 * var2)) - 1)
        var5 = i32_load8_u(((var11 + (var1 * var2)) - 1))
        var7 = i32_load8_u(var3)
        var4 = (i32_load8_u((var3 - 2)) - i32_load8_u(var3 + 1))
        if (1 if var12 >= ((i32_load8_u((var10 + (i32_load8_u(((var11 + (var1 * var2)) - 1)) - i32_load8_u(var3)))) << 2) + i32_load8_u((var10 + (i32_load8_u((var3 - 2)) - i32_load8_u(var3 + 1))))) else 0):
            var4 = (i32_load8_s((var4 + var13)) + ((var7 - var5) * 3))
            var14 = i32_load8_s((var9 + (((i32_load8_s((var4 + var13)) + ((var7 - var5) * 3)) + 4) >> 3)))
            i32_store8(var6, i32_load8_u((var8 + (i32_load8_s((var9 + ((var4 + 3) >> 3))) + var5))))
            i32_store8(var3, i32_load8_u((var8 + (var7 - var14))))
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != 16 else 0):
            continue
        break  # end loop
    var7 = (var0 + 12)
    var2 = 0
    while True:  # loop $label2
        var0 = (var7 + (var1 * var2))
        var11 = ((var7 + (var1 * var2)) - 1)
        var3 = i32_load8_u(((var7 + (var1 * var2)) - 1))
        var5 = i32_load8_u(var0)
        var6 = (i32_load8_u((var0 - 2)) - i32_load8_u(var0 + 1))
        if (1 if var12 >= ((i32_load8_u((var10 + (i32_load8_u(((var7 + (var1 * var2)) - 1)) - i32_load8_u(var0)))) << 2) + i32_load8_u((var10 + (i32_load8_u((var0 - 2)) - i32_load8_u(var0 + 1))))) else 0):
            var6 = (i32_load8_s((var6 + var13)) + ((var5 - var3) * 3))
            var4 = i32_load8_s((var9 + (((i32_load8_s((var6 + var13)) + ((var5 - var3) * 3)) + 4) >> 3)))
            i32_store8(var11, i32_load8_u((var8 + (i32_load8_s((var9 + ((var6 + 3) >> 3))) + var3))))
            i32_store8(var0, i32_load8_u((var8 + (var5 - var4))))
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != 16 else 0):
            continue
        break  # end loop


# ==========================================================
# $func1033
# ==========================================================
def func1033(var0, var1, var2):
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
    var10 = ((var2 << 1) | 1)
    var5 = i32_load(17088)
    var6 = i32_load(16308)
    var11 = i32_load(16076)
    var7 = i32_load(17616)
    while True:  # loop $label0
        var2 = (var0 + (var1 * var3))
        var12 = ((var0 + (var1 * var3)) - 1)
        var8 = i32_load8_u(((var0 + (var1 * var3)) - 1))
        var9 = i32_load8_u(var2)
        var4 = (i32_load8_u((var2 - 2)) - i32_load8_u(var2 + 1))
        if (1 if var10 >= ((i32_load8_u((var7 + (i32_load8_u(((var0 + (var1 * var3)) - 1)) - i32_load8_u(var2)))) << 2) + i32_load8_u((var7 + (i32_load8_u((var2 - 2)) - i32_load8_u(var2 + 1))))) else 0):
            var4 = (i32_load8_s((var4 + var11)) + ((var9 - var8) * 3))
            var13 = i32_load8_s((var6 + (((i32_load8_s((var4 + var11)) + ((var9 - var8) * 3)) + 4) >> 3)))
            i32_store8(var12, i32_load8_u((var5 + (i32_load8_s((var6 + ((var4 + 3) >> 3))) + var8))))
            i32_store8(var2, i32_load8_u((var5 + (var9 - var13))))
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != 16 else 0):
            continue
        break  # end loop

