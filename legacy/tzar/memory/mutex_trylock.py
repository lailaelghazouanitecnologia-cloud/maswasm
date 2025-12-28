"""
Function: $func185
Name: mutex_trylock
Category: memory
Depth: 0
Status: done

Calls: none
Called by: 2 functions ($func393, $func55)

Mutex try-lock - attempts to acquire a lock without blocking.
Returns 0 on success, error code on failure.

Return codes:
- 0: Lock acquired successfully
- 6: Recursion limit exceeded
- 10: Lock is held by another thread
- 56: Lock is in invalid state
- 62: Lock acquired, was recursive

Structure layout at $var0:
- offset 0:  flags/type
- offset 4:  state/owner
- offset 8:  wait flag
- offset 12: linked list prev
- offset 16: linked list next
- offset 20: recursion count

Global3: thread local storage
- offset 24: thread ID
- offset 76: lock list head
- offset 80: priority
- offset 84: current lock
"""

from tzar._runtime import i32_load, i32_load8_u, i32_store, globals


def mutex_trylock(lock_ptr: int) -> int:
    """
    Try to acquire a mutex lock without blocking.

    Args:
        lock_ptr: Pointer to mutex structure

    Returns:
        0 on success, error code on failure
    """
    flags = i32_load8_u(lock_ptr)

    # Simple mutex type
    if (flags & 15) == 0:
        state_ptr = lock_ptr + 4
        old_state = i32_load(state_ptr)

        # Try to atomically set from 0 to 10
        if old_state == 0:
            i32_store(state_ptr, 10)
            return 0
        return old_state & 10

    # Complex mutex type
    lock_flags = i32_load(lock_ptr)
    tls = globals['global3']
    thread_id = i32_load(tls, offset=24)
    state = i32_load(lock_ptr, offset=4)
    owner = state & 0x3FFFFFFF

    # Check if we already own the lock
    if owner == thread_id:
        # Timed lock - reset timeout
        if (lock_flags & 8) != 0:
            recursion = i32_load(lock_ptr, offset=20)
            if recursion < 0:
                i32_store(lock_ptr, 0, offset=20)
                # Handle high bit
                new_state = state & 0x40000000
                # Continue to acquire
            else:
                pass

        # Recursive lock
        if (lock_flags & 3) == 1:
            recursion = i32_load(lock_ptr, offset=20)
            if recursion > 0x7FFFFFFE:
                return 6  # Recursion limit
            i32_store(lock_ptr, recursion + 1, offset=20)
            return 0

    # Lock is owned by someone else
    if owner == 0x3FFFFFFF:
        return 56  # Invalid state

    if owner != 0:
        # Check if uncontended lock is available
        if (lock_flags & 4) == 0 or state == 0:
            # Try to acquire
            state_ptr = lock_ptr + 4

            # Handle contended mutex
            if (lock_flags & 128) != 0:
                if i32_load(tls, offset=80) == 0:
                    i32_store(tls, -12, offset=80)
                wait_flag = i32_load(lock_ptr, offset=8)
                i32_store(tls, lock_ptr + 16, offset=84)
                new_owner = thread_id | 0x80000000 if wait_flag else thread_id
            else:
                new_owner = thread_id

            new_owner |= (state & 0x40000000)

            # Atomic compare and swap
            old_state = i32_load(state_ptr)
            if old_state == state:
                i32_store(state_ptr, new_owner)
                # Successfully acquired - update lock list
                list_head = i32_load(tls, offset=76)
                i32_store(lock_ptr, tls + 76, offset=12)
                i32_store(lock_ptr, list_head, offset=16)

                if list_head != tls + 76:
                    i32_store(list_head - 4, lock_ptr + 16)

                i32_store(tls, lock_ptr + 16, offset=76)
                i32_store(tls, 0, offset=84)

                if state == 0:
                    return 0

                i32_store(lock_ptr, 0, offset=20)
                return 62  # Acquired recursive

            i32_store(tls, 0, offset=84)

            if (lock_flags & 12) == 12:
                if i32_load(lock_ptr, offset=8) != 0:
                    return 56

        return 10  # Lock busy

    return 10


# Alias for WASM function name
func185 = mutex_trylock
