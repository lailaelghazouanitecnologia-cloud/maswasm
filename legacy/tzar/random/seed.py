"""
Function: $C
Name: srand
Category: random
Depth: 0
Status: done

Calls: none
Called by: none (export entry point)

Seeds the XorShift128 random number generator.
Stores seed and derived values at addresses 9147312-9147324.

The magic constant 1515870810 (0x5A5A5A5A) creates initial state variety.
"""

from tzar._runtime import i32_store


# RNG state addresses
RNG_STATE_0 = 9147312
RNG_STATE_1 = 9147316
RNG_STATE_2 = 9147320
RNG_STATE_3 = 9147324


def srand(seed: int) -> None:
    """
    Seed the random number generator.

    Args:
        seed: Initial seed value
    """
    seed = seed & 0xFFFFFFFF
    i32_store(RNG_STATE_0, seed)
    i32_store(RNG_STATE_1, seed ^ 1515870810)
    i32_store(RNG_STATE_2, seed ^ 0xA5A5A5A5)  # -1515870811 as unsigned
    i32_store(RNG_STATE_3, seed ^ 0xFFFFFFFF)


# Alias
C = srand
