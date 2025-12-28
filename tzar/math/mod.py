"""
Tzar Engine - Math module.
Auto-generated from WebAssembly.
"""
from tzar.runtime import (
    load32, load64, load8u, load8s, load16u, load16s,
    loadf32, loadf64,
    store32, store64, store8, store16, storef32, storef64,
    atomic_load, atomic_store,
    i32, i64, u32, u64, f32,
    rotl, rotr, clz, ctz, popcnt,
    sqrt, abs, ceil, floor, trunc,
    G, mem_size, mem_grow, call_table,
)

# Known addresses
GAME_STATE = 9142424
CURRENT_PLAYER = 9142872
PLAYER_COUNT = 9142892
PLAYERS = 9561692
ENTITY_TYPES = 9568096
ENTITIES = 9671128
HEAP_FREELIST = 9690464
HEAP_TREE = 9690468
FREE_SIZE = 9690472
HEAP_TOTAL = 9690476
HEAP_BASE = 9690480
HEAP_TOP = 9690484
HEAP_END = 9690488
ALLOC_COUNT = 9690496
MEM_FLAGS = 9690908
MEM_MUTEX = 9690912
ALLOC_HANDLER = 9690984

class Unreachable(Exception):
    pass


# ----------------------------------------------------------
# $func75
# ----------------------------------------------------------
def func75(arg0):
    v1 = (arg0 * arg0)
    v2 = ((arg0 * arg0) * arg0)
    # TODO: f32.demote_f64
    return (((((arg0 * arg0) * arg0) * (v1 * v1)) * ((v1 * 2.718311493989822e-06) + -0.00019839334836096632)) + ((v2 * ((v1 * 0.008333329385889463) + -0.16666666641626524)) + arg0))

# ----------------------------------------------------------
# $func76
# ----------------------------------------------------------
def func76(arg0):
    arg0 = (arg0 * arg0)
    v1 = (arg0 * arg0)
    # TODO: f32.demote_f64
    return ((((arg0 * arg0) * (arg0 * arg0)) * ((arg0 * 2.439044879627741e-05) + -0.001388676377460993)) + ((v1 * 0.04166662332373906) + ((arg0 * -0.499999997251031) + 1.0)))

# ----------------------------------------------------------
# $func749
# ----------------------------------------------------------
def func749(arg0):