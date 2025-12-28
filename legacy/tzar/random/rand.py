"""
Function: $D
Name: rand
Category: random
Depth: 0
Status: done

Calls: none
Called by: 1 function ($func34)

XorShift128 random number generator.
Returns random value modulo the input parameter.

State stored at addresses 9147312-9147324 (4 x 32-bit words).
"""

from tzar._runtime import i32_load, i32_store, i64_load, i64_store


# RNG state addresses
RNG_STATE_0 = 9147312
RNG_STATE_1 = 9147316
RNG_STATE_2 = 9147320
RNG_STATE_3 = 9147324


def rand(modulo: int) -> int:
    """
    Generate random number using XorShift128.

    Args:
        modulo: Return value will be in range [0, modulo)

    Returns:
        Random integer
    """
    # Load state
    state_12 = i64_load(RNG_STATE_1)  # Load states 1 and 2 as 64-bit
    s0 = i32_load(RNG_STATE_0)
    s3 = i32_load(RNG_STATE_3)

    # Shift state
    i32_store(RNG_STATE_1, s0)
    i64_store(RNG_STATE_2, state_12)

    # XorShift algorithm
    t = s3 ^ (s3 << 11)
    t = t ^ (t >> 8)
    t = t ^ s0 ^ (s0 >> 19)

    i32_store(RNG_STATE_0, t & 0xFFFFFFFF)

    return (t & 0xFFFFFFFF) % modulo if modulo else 0


# Alias
D = rand
