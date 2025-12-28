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
# $func446
# ==========================================================
def func446(var0, var1, var2, var3):
    var4 = 0
    var5 = 0
    if (1 if var3 <= 0 else 0):
        break
    var4 = (var3 & 3)
    if (1 if var3 >= 4 else 0):
        var5 = (var3 & -4)
        var3 = 0
        while True:  # loop $label1
            # call_indirect via table[i32_load(9687284)]
            var0 = (var0 + var1)
            # call_indirect via table[i32_load(9687284)]
            var0 = (var0 + var1)
            # call_indirect via table[i32_load(9687284)]
            var0 = (var0 + var1)
            # call_indirect via table[i32_load(9687284)]
            var0 = (var0 + var1)
            var3 = (var3 + 4)
            if (1 if (var3 + 4) != var5 else 0):
                continue
            break  # end loop
    if (1 if var4 == 0 else 0):
        break
    var3 = 0
    while True:  # loop $label2
        # call_indirect via table[i32_load(9687284)]
        var0 = (var0 + var1)
        var3 = (var3 + 1)
        if (1 if (var3 + 1) != var4 else 0):
            continue
        break  # end loop


# ==========================================================
# $func448
# ==========================================================
def func448():
    var0 = 0
    var0 = i32_load(52304)
    if (1 if i32_load(52304) != i32_load(52328) else 0):
        i32_store(9687856, 385)
        i32_store(9687852, 386)
        i32_store(9687836, 385)
        i32_store(9687828, 386)
        i32_store(9687864, 387)
        i32_store(9687860, 388)
        i32_store(9687848, 389)
        i32_store(9687844, 387)
        i32_store(9687840, 388)
        i32_store(9687832, 390)
        i32_store(9687824, 391)
        i32_store(52328, var0)


# ==========================================================
# $func453
# ==========================================================
def func453():
    var0 = 0
    var0 = i32_load(52304)
    if (1 if i32_load(52304) != i32_load(52316) else 0):
        i32_store(9687724, 344)
        i32_store(9687720, 344)
        i32_store(9687716, 345)
        i32_store(9687712, 346)
        i32_store(9687708, 347)
        i32_store(9687704, 348)
        i32_store(9687700, 349)
        i32_store(9687696, 350)
        i32_store(9687692, 351)
        i32_store(9687688, 352)
        i32_store(9687684, 353)
        i32_store(9687680, 354)
        i32_store(9687676, 355)
        i32_store(9687672, 356)
        i32_store(9687668, 357)
        i32_store(9687664, 344)
        i32_store(9687660, 358)
        i32_store(9687656, 358)
        i32_store(9687652, 359)
        i32_store(9687648, 360)
        i32_store(9687644, 361)
        i32_store(9687640, 362)
        i32_store(9687636, 363)
        i32_store(9687632, 364)
        i32_store(9687628, 365)
        i32_store(9687624, 366)
        i32_store(9687620, 367)
        i32_store(9687616, 368)
        i32_store(9687612, 369)
        i32_store(9687608, 370)
        i32_store(9687604, 371)
        i32_store(9687600, 358)
        i32_store(9687788, 358)
        i32_store(9687784, 358)
        i32_store(9687780, 359)
        i32_store(9687776, 360)
        i32_store(9687772, 361)
        i32_store(9687768, 362)
        i32_store(9687764, 363)
        i32_store(9687760, 364)
        i32_store(9687756, 365)
        i32_store(9687752, 366)
        i32_store(9687748, 367)
        i32_store(9687744, 368)
        i32_store(9687740, 369)
        i32_store(9687736, 370)
        i32_store(9687732, 371)
        i32_store(9687728, 358)
        i32_store(9687572, 372)
        i32_store(9687792, 373)
        i32_store(9687580, 374)
        i32_store(9687576, 375)
        i32_store(9687584, 376)
        i32_store(9687588, 377)
        i32_store(9687592, 378)
        i32_store(9687796, 379)
        i32_store(9687568, 380)
        i32_store(52316, var0)


# ==========================================================
# $func459
# ==========================================================
def func459(var0, var1):
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
    var31 = 0
    var3 = i32_load16_s(var0 + 10)
    var5 = i32_load16_s(var0 + 26)
    var17 = ((((i32_load16_s(var0 + 10) * 20091) >> 16) + var3) + ((i32_load16_s(var0 + 26) * 35468) >> 16))
    var8 = i32_load16_s(var0 + 18)
    var14 = i32_load16_s(var0 + 2)
    var18 = (i32_load16_s(var0 + 18) + i32_load16_s(var0 + 2))
    var2 = (((((i32_load16_s(var0 + 10) * 20091) >> 16) + var3) + ((i32_load16_s(var0 + 26) * 35468) >> 16)) + (i32_load16_s(var0 + 18) + i32_load16_s(var0 + 2)))
    var6 = i32_load16_s(var0 + 14)
    var7 = i32_load16_s(var0 + 30)
    var19 = ((((i32_load16_s(var0 + 14) * 20091) >> 16) + var6) + ((i32_load16_s(var0 + 30) * 35468) >> 16))
    var15 = i32_load16_s(var0 + 22)
    var9 = i32_load16_s(var0 + 6)
    var20 = (i32_load16_s(var0 + 22) + i32_load16_s(var0 + 6))
    var4 = (((((i32_load16_s(var0 + 14) * 20091) >> 16) + var6) + ((i32_load16_s(var0 + 30) * 35468) >> 16)) + (i32_load16_s(var0 + 22) + i32_load16_s(var0 + 6)))
    var21 = (((((((((i32_load16_s(var0 + 10) * 20091) >> 16) + var3) + ((i32_load16_s(var0 + 26) * 35468) >> 16)) + (i32_load16_s(var0 + 18) + i32_load16_s(var0 + 2))) * 20091) >> 16) + var2) + (((((((i32_load16_s(var0 + 14) * 20091) >> 16) + var6) + ((i32_load16_s(var0 + 30) * 35468) >> 16)) + (i32_load16_s(var0 + 22) + i32_load16_s(var0 + 6))) * 35468) >> 16))
    var10 = i32_load16_s(var0 + 8)
    var11 = i32_load16_s(var0 + 24)
    var22 = ((((i32_load16_s(var0 + 8) * 20091) >> 16) + var10) + ((i32_load16_s(var0 + 24) * 35468) >> 16))
    var23 = i32_load16_s(var0 + 16)
    var24 = i32_load16_s(var0)
    var25 = (i32_load16_s(var0 + 16) + i32_load16_s(var0))
    var26 = ((((((i32_load16_s(var0 + 8) * 20091) >> 16) + var10) + ((i32_load16_s(var0 + 24) * 35468) >> 16)) + (i32_load16_s(var0 + 16) + i32_load16_s(var0))) + 4)
    var12 = i32_load16_s(var0 + 12)
    var13 = i32_load16_s(var0 + 28)
    var27 = ((((i32_load16_s(var0 + 12) * 20091) >> 16) + var12) + ((i32_load16_s(var0 + 28) * 35468) >> 16))
    var28 = i32_load16_s(var0 + 20)
    var29 = i32_load16_s(var0 + 4)
    var30 = (i32_load16_s(var0 + 20) + i32_load16_s(var0 + 4))
    var0 = (((((i32_load16_s(var0 + 12) * 20091) >> 16) + var12) + ((i32_load16_s(var0 + 28) * 35468) >> 16)) + (i32_load16_s(var0 + 20) + i32_load16_s(var0 + 4)))
    var31 = (((((((i32_load16_s(var0 + 8) * 20091) >> 16) + var10) + ((i32_load16_s(var0 + 24) * 35468) >> 16)) + (i32_load16_s(var0 + 16) + i32_load16_s(var0))) + 4) + (((((i32_load16_s(var0 + 12) * 20091) >> 16) + var12) + ((i32_load16_s(var0 + 28) * 35468) >> 16)) + (i32_load16_s(var0 + 20) + i32_load16_s(var0 + 4))))
    var16 = (i32_load8_u(var1) + (((((((((((i32_load16_s(var0 + 10) * 20091) >> 16) + var3) + ((i32_load16_s(var0 + 26) * 35468) >> 16)) + (i32_load16_s(var0 + 18) + i32_load16_s(var0 + 2))) * 20091) >> 16) + var2) + (((((((i32_load16_s(var0 + 14) * 20091) >> 16) + var6) + ((i32_load16_s(var0 + 30) * 35468) >> 16)) + (i32_load16_s(var0 + 22) + i32_load16_s(var0 + 6))) * 35468) >> 16)) + (((((((i32_load16_s(var0 + 8) * 20091) >> 16) + var10) + ((i32_load16_s(var0 + 24) * 35468) >> 16)) + (i32_load16_s(var0 + 16) + i32_load16_s(var0))) + 4) + (((((i32_load16_s(var0 + 12) * 20091) >> 16) + var12) + ((i32_load16_s(var0 + 28) * 35468) >> 16)) + (i32_load16_s(var0 + 20) + i32_load16_s(var0 + 4))))) >> 3))
    var16 = ((i32_load8_u(var1) + (((((((((((i32_load16_s(var0 + 10) * 20091) >> 16) + var3) + ((i32_load16_s(var0 + 26) * 35468) >> 16)) + (i32_load16_s(var0 + 18) + i32_load16_s(var0 + 2))) * 20091) >> 16) + var2) + (((((((i32_load16_s(var0 + 14) * 20091) >> 16) + var6) + ((i32_load16_s(var0 + 30) * 35468) >> 16)) + (i32_load16_s(var0 + 22) + i32_load16_s(var0 + 6))) * 35468) >> 16)) + (((((((i32_load16_s(var0 + 8) * 20091) >> 16) + var10) + ((i32_load16_s(var0 + 24) * 35468) >> 16)) + (i32_load16_s(var0 + 16) + i32_load16_s(var0))) + 4) + (((((i32_load16_s(var0 + 12) * 20091) >> 16) + var12) + ((i32_load16_s(var0 + 28) * 35468) >> 16)) + (i32_load16_s(var0 + 20) + i32_load16_s(var0 + 4))))) >> 3)) if (1 if var16 > 0 else 0) else 0)
    i32_store8(var1, (255 if (1 if var16 >= 255 else 0) else ((i32_load8_u(var1) + (((((((((((i32_load16_s(var0 + 10) * 20091) >> 16) + var3) + ((i32_load16_s(var0 + 26) * 35468) >> 16)) + (i32_load16_s(var0 + 18) + i32_load16_s(var0 + 2))) * 20091) >> 16) + var2) + (((((((i32_load16_s(var0 + 14) * 20091) >> 16) + var6) + ((i32_load16_s(var0 + 30) * 35468) >> 16)) + (i32_load16_s(var0 + 22) + i32_load16_s(var0 + 6))) * 35468) >> 16)) + (((((((i32_load16_s(var0 + 8) * 20091) >> 16) + var10) + ((i32_load16_s(var0 + 24) * 35468) >> 16)) + (i32_load16_s(var0 + 16) + i32_load16_s(var0))) + 4) + (((((i32_load16_s(var0 + 12) * 20091) >> 16) + var12) + ((i32_load16_s(var0 + 28) * 35468) >> 16)) + (i32_load16_s(var0 + 20) + i32_load16_s(var0 + 4))))) >> 3)) if (1 if var16 > 0 else 0) else 0)))
    var2 = (((var2 * 35468) >> 16) - (var4 + ((var4 * 20091) >> 16)))
    var0 = (var26 - var0)
    var4 = (i32_load8_u(var1 + 1) + (((((var2 * 35468) >> 16) - (var4 + ((var4 * 20091) >> 16))) + (var26 - var0)) >> 3))
    var4 = ((i32_load8_u(var1 + 1) + (((((var2 * 35468) >> 16) - (var4 + ((var4 * 20091) >> 16))) + (var26 - var0)) >> 3)) if (1 if var4 > 0 else 0) else 0)
    i32_store8(var1 + 1, (255 if (1 if var4 >= 255 else 0) else ((i32_load8_u(var1 + 1) + (((((var2 * 35468) >> 16) - (var4 + ((var4 * 20091) >> 16))) + (var26 - var0)) >> 3)) if (1 if var4 > 0 else 0) else 0)))
    var0 = (i32_load8_u(var1 + 2) + ((var0 - var2) >> 3))
    var0 = ((i32_load8_u(var1 + 2) + ((var0 - var2) >> 3)) if (1 if var0 > 0 else 0) else 0)
    i32_store8(var1 + 2, (255 if (1 if var0 >= 255 else 0) else ((i32_load8_u(var1 + 2) + ((var0 - var2) >> 3)) if (1 if var0 > 0 else 0) else 0)))
    var0 = (i32_load8_u(var1 + 3) + ((var31 - var21) >> 3))
    var0 = ((i32_load8_u(var1 + 3) + ((var31 - var21) >> 3)) if (1 if var0 > 0 else 0) else 0)
    i32_store8(var1 + 3, (255 if (1 if var0 >= 255 else 0) else ((i32_load8_u(var1 + 3) + ((var31 - var21) >> 3)) if (1 if var0 > 0 else 0) else 0)))
    var5 = (((var3 * 35468) >> 16) - (var5 + ((var5 * 20091) >> 16)))
    var2 = (var14 - var8)
    var0 = ((((var3 * 35468) >> 16) - (var5 + ((var5 * 20091) >> 16))) + (var14 - var8))
    var6 = (((var6 * 35468) >> 16) - (var7 + ((var7 * 20091) >> 16)))
    var7 = (var9 - var15)
    var3 = ((((var6 * 35468) >> 16) - (var7 + ((var7 * 20091) >> 16))) + (var9 - var15))
    var4 = ((((((((var3 * 35468) >> 16) - (var5 + ((var5 * 20091) >> 16))) + (var14 - var8)) * 20091) >> 16) + var0) + ((((((var6 * 35468) >> 16) - (var7 + ((var7 * 20091) >> 16))) + (var9 - var15)) * 35468) >> 16))
    var10 = (((var10 * 35468) >> 16) - (var11 + ((var11 * 20091) >> 16)))
    var11 = (var24 - var23)
    var8 = (((((var10 * 35468) >> 16) - (var11 + ((var11 * 20091) >> 16))) + (var24 - var23)) + 4)
    var12 = (((var12 * 35468) >> 16) - (var13 + ((var13 * 20091) >> 16)))
    var13 = (var29 - var28)
    var14 = ((((var12 * 35468) >> 16) - (var13 + ((var13 * 20091) >> 16))) + (var29 - var28))
    var15 = ((((((var10 * 35468) >> 16) - (var11 + ((var11 * 20091) >> 16))) + (var24 - var23)) + 4) + ((((var12 * 35468) >> 16) - (var13 + ((var13 * 20091) >> 16))) + (var29 - var28)))
    var9 = (i32_load8_u(var1 + 32) + ((((((((((var3 * 35468) >> 16) - (var5 + ((var5 * 20091) >> 16))) + (var14 - var8)) * 20091) >> 16) + var0) + ((((((var6 * 35468) >> 16) - (var7 + ((var7 * 20091) >> 16))) + (var9 - var15)) * 35468) >> 16)) + ((((((var10 * 35468) >> 16) - (var11 + ((var11 * 20091) >> 16))) + (var24 - var23)) + 4) + ((((var12 * 35468) >> 16) - (var13 + ((var13 * 20091) >> 16))) + (var29 - var28)))) >> 3))
    var9 = ((i32_load8_u(var1 + 32) + ((((((((((var3 * 35468) >> 16) - (var5 + ((var5 * 20091) >> 16))) + (var14 - var8)) * 20091) >> 16) + var0) + ((((((var6 * 35468) >> 16) - (var7 + ((var7 * 20091) >> 16))) + (var9 - var15)) * 35468) >> 16)) + ((((((var10 * 35468) >> 16) - (var11 + ((var11 * 20091) >> 16))) + (var24 - var23)) + 4) + ((((var12 * 35468) >> 16) - (var13 + ((var13 * 20091) >> 16))) + (var29 - var28)))) >> 3)) if (1 if var9 > 0 else 0) else 0)
    i32_store8(var1 + 32, (255 if (1 if var9 >= 255 else 0) else ((i32_load8_u(var1 + 32) + ((((((((((var3 * 35468) >> 16) - (var5 + ((var5 * 20091) >> 16))) + (var14 - var8)) * 20091) >> 16) + var0) + ((((((var6 * 35468) >> 16) - (var7 + ((var7 * 20091) >> 16))) + (var9 - var15)) * 35468) >> 16)) + ((((((var10 * 35468) >> 16) - (var11 + ((var11 * 20091) >> 16))) + (var24 - var23)) + 4) + ((((var12 * 35468) >> 16) - (var13 + ((var13 * 20091) >> 16))) + (var29 - var28)))) >> 3)) if (1 if var9 > 0 else 0) else 0)))
    var0 = (((var0 * 35468) >> 16) - (var3 + ((var3 * 20091) >> 16)))
    var3 = (var8 - var14)
    var8 = (i32_load8_u(var1 + 33) + (((((var0 * 35468) >> 16) - (var3 + ((var3 * 20091) >> 16))) + (var8 - var14)) >> 3))
    var8 = ((i32_load8_u(var1 + 33) + (((((var0 * 35468) >> 16) - (var3 + ((var3 * 20091) >> 16))) + (var8 - var14)) >> 3)) if (1 if var8 > 0 else 0) else 0)
    i32_store8(var1 + 33, (255 if (1 if var8 >= 255 else 0) else ((i32_load8_u(var1 + 33) + (((((var0 * 35468) >> 16) - (var3 + ((var3 * 20091) >> 16))) + (var8 - var14)) >> 3)) if (1 if var8 > 0 else 0) else 0)))
    var0 = (i32_load8_u(var1 + 34) + ((var3 - var0) >> 3))
    var0 = ((i32_load8_u(var1 + 34) + ((var3 - var0) >> 3)) if (1 if var0 > 0 else 0) else 0)
    i32_store8(var1 + 34, (255 if (1 if var0 >= 255 else 0) else ((i32_load8_u(var1 + 34) + ((var3 - var0) >> 3)) if (1 if var0 > 0 else 0) else 0)))
    var0 = (i32_load8_u(var1 + 35) + ((var15 - var4) >> 3))
    var0 = ((i32_load8_u(var1 + 35) + ((var15 - var4) >> 3)) if (1 if var0 > 0 else 0) else 0)
    i32_store8(var1 + 35, (255 if (1 if var0 >= 255 else 0) else ((i32_load8_u(var1 + 35) + ((var15 - var4) >> 3)) if (1 if var0 > 0 else 0) else 0)))
    var0 = (var2 - var5)
    var3 = (var7 - var6)
    var5 = (((((var2 - var5) * 20091) >> 16) + var0) + (((var7 - var6) * 35468) >> 16))
    var2 = ((var11 - var10) + 4)
    var6 = (var13 - var12)
    var7 = (((var11 - var10) + 4) + (var13 - var12))
    var4 = (i32_load8_u(var1 + 64) + (((((((var2 - var5) * 20091) >> 16) + var0) + (((var7 - var6) * 35468) >> 16)) + (((var11 - var10) + 4) + (var13 - var12))) >> 3))
    var4 = ((i32_load8_u(var1 + 64) + (((((((var2 - var5) * 20091) >> 16) + var0) + (((var7 - var6) * 35468) >> 16)) + (((var11 - var10) + 4) + (var13 - var12))) >> 3)) if (1 if var4 > 0 else 0) else 0)
    i32_store8(var1 + 64, (255 if (1 if var4 >= 255 else 0) else ((i32_load8_u(var1 + 64) + (((((((var2 - var5) * 20091) >> 16) + var0) + (((var7 - var6) * 35468) >> 16)) + (((var11 - var10) + 4) + (var13 - var12))) >> 3)) if (1 if var4 > 0 else 0) else 0)))
    var0 = (((var0 * 35468) >> 16) - (var3 + ((var3 * 20091) >> 16)))
    var3 = (var2 - var6)
    var2 = (i32_load8_u(var1 + 65) + (((((var0 * 35468) >> 16) - (var3 + ((var3 * 20091) >> 16))) + (var2 - var6)) >> 3))
    var2 = ((i32_load8_u(var1 + 65) + (((((var0 * 35468) >> 16) - (var3 + ((var3 * 20091) >> 16))) + (var2 - var6)) >> 3)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 65, (255 if (1 if var2 >= 255 else 0) else ((i32_load8_u(var1 + 65) + (((((var0 * 35468) >> 16) - (var3 + ((var3 * 20091) >> 16))) + (var2 - var6)) >> 3)) if (1 if var2 > 0 else 0) else 0)))
    var0 = (i32_load8_u(var1 + 66) + ((var3 - var0) >> 3))
    var0 = ((i32_load8_u(var1 + 66) + ((var3 - var0) >> 3)) if (1 if var0 > 0 else 0) else 0)
    i32_store8(var1 + 66, (255 if (1 if var0 >= 255 else 0) else ((i32_load8_u(var1 + 66) + ((var3 - var0) >> 3)) if (1 if var0 > 0 else 0) else 0)))
    var0 = (i32_load8_u(var1 + 67) + ((var7 - var5) >> 3))
    var0 = ((i32_load8_u(var1 + 67) + ((var7 - var5) >> 3)) if (1 if var0 > 0 else 0) else 0)
    i32_store8(var1 + 67, (255 if (1 if var0 >= 255 else 0) else ((i32_load8_u(var1 + 67) + ((var7 - var5) >> 3)) if (1 if var0 > 0 else 0) else 0)))
    var0 = (var18 - var17)
    var3 = (var20 - var19)
    var5 = (((((var18 - var17) * 20091) >> 16) + var0) + (((var20 - var19) * 35468) >> 16))
    var2 = ((var25 - var22) + 4)
    var6 = (var30 - var27)
    var7 = (((var25 - var22) + 4) + (var30 - var27))
    var4 = (i32_load8_u(var1 + 96) + (((((((var18 - var17) * 20091) >> 16) + var0) + (((var20 - var19) * 35468) >> 16)) + (((var25 - var22) + 4) + (var30 - var27))) >> 3))
    var4 = ((i32_load8_u(var1 + 96) + (((((((var18 - var17) * 20091) >> 16) + var0) + (((var20 - var19) * 35468) >> 16)) + (((var25 - var22) + 4) + (var30 - var27))) >> 3)) if (1 if var4 > 0 else 0) else 0)
    i32_store8(var1 + 96, (255 if (1 if var4 >= 255 else 0) else ((i32_load8_u(var1 + 96) + (((((((var18 - var17) * 20091) >> 16) + var0) + (((var20 - var19) * 35468) >> 16)) + (((var25 - var22) + 4) + (var30 - var27))) >> 3)) if (1 if var4 > 0 else 0) else 0)))
    var0 = (((var0 * 35468) >> 16) - (var3 + ((var3 * 20091) >> 16)))
    var3 = (var2 - var6)
    var2 = (i32_load8_u(var1 + 97) + (((((var0 * 35468) >> 16) - (var3 + ((var3 * 20091) >> 16))) + (var2 - var6)) >> 3))
    var2 = ((i32_load8_u(var1 + 97) + (((((var0 * 35468) >> 16) - (var3 + ((var3 * 20091) >> 16))) + (var2 - var6)) >> 3)) if (1 if var2 > 0 else 0) else 0)
    i32_store8(var1 + 97, (255 if (1 if var2 >= 255 else 0) else ((i32_load8_u(var1 + 97) + (((((var0 * 35468) >> 16) - (var3 + ((var3 * 20091) >> 16))) + (var2 - var6)) >> 3)) if (1 if var2 > 0 else 0) else 0)))
    var0 = (i32_load8_u(var1 + 98) + ((var3 - var0) >> 3))
    var0 = ((i32_load8_u(var1 + 98) + ((var3 - var0) >> 3)) if (1 if var0 > 0 else 0) else 0)
    i32_store8(var1 + 98, (255 if (1 if var0 >= 255 else 0) else ((i32_load8_u(var1 + 98) + ((var3 - var0) >> 3)) if (1 if var0 > 0 else 0) else 0)))
    var0 = (i32_load8_u(var1 + 99) + ((var7 - var5) >> 3))
    var0 = ((i32_load8_u(var1 + 99) + ((var7 - var5) >> 3)) if (1 if var0 > 0 else 0) else 0)
    i32_store8(var1 + 99, (255 if (1 if var0 >= 255 else 0) else ((i32_load8_u(var1 + 99) + ((var7 - var5) >> 3)) if (1 if var0 > 0 else 0) else 0)))


# ==========================================================
# $ge
# Export: ge
# ==========================================================
def ge(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10):
    """Export: ge"""
    var11 = 0
    var5 = (i32_load(9561692) + (var0 * 286704))
    var4 = (100 if var4 else 0)
    i32_store((i32_load(9561692) + (var0 * 286704)) + 286688, (100 if var4 else 0))
    i32_store(var5 + 286684, var4)
    i32_store(var5 + 283908, var0)
    i32_store(var5 + 283868, i32_load(9561460))
    # Unknown: memory.copy []
    var0 = i32_load(9142424)
    i32_store((var5 + 284000), i32_load(i32_load(9142424) + 40))
    var0 = i32_load(var0 + 36)
    i32_store(var5 + 283960, 3)
    i32_store((var5 + 284136), var0)
    i32_store8((var5 + 283974), var3)
    i32_store8((var5 + 283973), var2)
    i32_store8(var5 + 283972, var1)
    i32_store((var5 + 283860), var9)
    i32_store((var5 + 283856), var8)
    i32_store((var5 + 283852), var7)
    i32_store(var5 + 283848, var6)
    if (1 if var10 == 0 else 0):
        break
    var0 = (var10 & 3)
    if (1 if var10 >= 4 else 0):
        var1 = (var10 & -4)
        var10 = 0
        while True:  # loop $label1
            i32_store16((var5 + (var11 << 1)), i32_load(((var11 << 2) + 9147392)))
            var2 = (var11 | 1)
            i32_store16((var5 + ((var11 | 1) << 1)), i32_load(((var2 << 2) + 9147392)))
            var2 = (var11 | 2)
            i32_store16((var5 + ((var11 | 2) << 1)), i32_load(((var2 << 2) + 9147392)))
            var2 = (var11 | 3)
            i32_store16((var5 + ((var11 | 3) << 1)), i32_load(((var2 << 2) + 9147392)))
            var11 = (var11 + 4)
            var10 = (var10 + 4)
            if (1 if (var10 + 4) != var1 else 0):
                continue
            break  # end loop
    if (1 if var0 == 0 else 0):
        break
    var10 = 0
    while True:  # loop $label2
        i32_store16((var5 + (var11 << 1)), i32_load(((var11 << 2) + 9147392)))
        var11 = (var11 + 1)
        var10 = (var10 + 1)
        if (1 if (var10 + 1) != var0 else 0):
            continue
        break  # end loop


# ==========================================================
# $wa
# Export: wa
# ==========================================================
def wa(var0, var1):
    """Export: wa"""
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var4 = i32_load(9561692)
    var5 = i32_load(9142892)
    if (1 if i32_load(9142892) < 2 else 0):
        break
    var2 = 1
    while True:  # loop $label1
        if (1 if var0 == i32_load((var4 + (var2 * 286704)) + 284616) else 0):
            var3 = var2
            break
        var2 = (var2 + 1)
        if (1 if (var2 + 1) != var5 else 0):
            continue
        break  # end loop
    i32_store((var4 + (var3 * 286704)) + 284604, var1)

