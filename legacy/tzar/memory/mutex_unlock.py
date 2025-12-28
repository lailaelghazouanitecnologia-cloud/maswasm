"""
Function: $func54
Name: mutex_unlock
Category: memory
Depth: 2
Status: done

Calls: $func111 (atomic_notify), $func97 (atomic_wake_one)
Called by: 12 functions

Mutex unlock/release function with thread synchronization.
Handles various mutex types (recursive, contended, etc.)

Structure layout at $var0:
- offset 0:  flags/type
- offset 4:  state/owner
- offset 8:  saved state
- offset 12: linked list prev
- offset 16: linked list next
- offset 20: recursion count

Global addresses:
- 9689392: contention counter
- 9689396: waiter flag
- global3: thread local storage
"""

from tzar._runtime import (
    i32_load, i32_store, i32_load8_u, globals
)
from tzar.memory.atomic_notify import atomic_notify
from tzar.memory.atomic_wake_one import atomic_wake_one


def mutex_unlock(lock_ptr: int) -> None:
    """
    Release a mutex lock.

    Handles multiple mutex types:
    - Simple: just exchange state
    - Recursive: decrement count if owner matches
    - Contended: notify waiters

    Args:
        lock_ptr: Pointer to mutex structure
    """
    saved_state = i32_load(lock_ptr, offset=8)
    flags = i32_load(lock_ptr)

    state_ptr = lock_ptr + 4

    if (flags & 15) == 0:
        # Simple mutex - just clear state
        old_state = i32_load(state_ptr)
        i32_store(state_ptr, 0)

        # Wake if needed
        if saved_state == 0 and old_state >= 0:
            return
        atomic_wake_one(state_ptr)
        return

    # Thread local storage
    tls = globals['global3']
    thread_id = i32_load(tls, offset=24)

    state = i32_load(lock_ptr, offset=4)
    owner = state & 0x3FFFFFFF  # Mask off flags

    if owner != thread_id:
        return

    # Check if recursive
    if (flags & 3) == 1:
        recursion = i32_load(lock_ptr, offset=20)
        if recursion != 0:
            i32_store(lock_ptr, recursion - 1, offset=20)
            return

    # Handle contended mutex
    is_contended = (flags & 128) != 0

    if is_contended:
        i32_store(tls, lock_ptr + 16, offset=84)
        # Increment contention counter (atomic)
        # In single-threaded Python, just load and store
        cnt = i32_load(9689392)
        i32_store(9689392, cnt + 1)

    # Update linked list
    prev = i32_load(lock_ptr, offset=12)
    next_ptr = i32_load(lock_ptr, offset=16)
    i32_store(prev, next_ptr)

    if next_ptr != tls + 76:
        i32_store(next_ptr - 4, prev)

    # Calculate new state
    new_state = ((state << 1) & ((flags >> 29) << 31)) >> 31
    new_state &= 0x7FFFFFFF
    i32_store(state_ptr, new_state)
    old_state = state  # Previous value from exchange

    if is_contended:
        i32_store(tls, 0, offset=84)

        # Decrement contention counter
        cnt = i32_load(9689392)
        i32_store(9689392, cnt - 1)

        if cnt == 1:
            waiter_flag = i32_load(9689396)
            if waiter_flag != 0:
                atomic_notify(9689392, 0x7FFFFFFF)

    # Wake waiter if needed
    if saved_state != 0 or old_state < 0:
        atomic_wake_one(state_ptr)


# Alias for WASM function name
func54 = mutex_unlock
