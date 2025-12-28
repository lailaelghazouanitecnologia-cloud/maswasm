"""
Function: $func111
Name: atomic_notify
Category: memory
Depth: 0
Status: done

Calls: none
Called by: 7 functions ($func54, $func811, $func266, $func97, $func438, $nc, $func432)

Atomic notification primitive for thread synchronization.
Uses compare-and-swap (cmpxchg) and memory.atomic.notify.

Global address:
- 9688024: atomic flag location

Args:
    $var0: Memory address (must be 4-byte aligned)
    $var1: Number of waiters to notify
"""

from tzar._runtime import memory, i32_load, i32_store

# Global atomic flag address
ATOMIC_FLAG_ADDR = 9688024


def atomic_notify(addr: int, count: int) -> None:
    """
    Notify waiting threads on an atomic location.

    This is a threading primitive that wakes up waiters.
    In single-threaded Python, this is effectively a no-op
    but maintains the structure for compatibility.

    Args:
        addr: Memory address (must be 4-byte aligned)
        count: Number of waiters to notify
    """
    # Validate parameters
    if addr == 0:
        return
    if count < 0:
        return
    if addr & 3:  # Must be 4-byte aligned
        return
    if count == 0:
        return

    # Compare and swap at global flag address
    # In Python we simulate this atomically (single-threaded)
    old_val = i32_load(ATOMIC_FLAG_ADDR)

    if old_val == 0:
        i32_store(ATOMIC_FLAG_ADDR, addr)
        old_val = 0
    else:
        old_val = i32_load(ATOMIC_FLAG_ADDR)

    # Notify logic
    if count != 2147483647:  # INT_MAX means infinite
        if addr == old_val:
            if count >= 2:
                count -= 1

    # In WASM this would notify waiters
    # In Python single-threaded context, this is a no-op
    # memory.atomic.notify(addr, count) -> no-op


# Alias for WASM function name
func111 = atomic_notify
