"""
Function: $func97
Name: atomic_wake_one
Category: memory
Depth: 1
Status: done

Calls: $func111 (atomic_notify)
Called by: 7 functions

Simple wrapper that calls atomic_notify with count=1.
Wakes up exactly one waiting thread.
"""

from tzar.memory.atomic_notify import atomic_notify


def atomic_wake_one(addr: int) -> None:
    """
    Wake up one waiter on the given address.

    Args:
        addr: Memory address to notify
    """
    atomic_notify(addr, 1)


# Alias for WASM function name
func97 = atomic_wake_one
