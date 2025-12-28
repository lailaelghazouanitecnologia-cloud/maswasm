"""
Miscellaneous utility functions - batch 24.

Simple wrapper and helper functions.
"""

from tzar._runtime import i32_load, i32_load8_u, i32_store, i64_load, i64_store


# ============================================================================
# func395: Identity function (leaf, 0 callers)
# ============================================================================

def func395(var0: int) -> int:
    """
    $func395: Identity function - returns input unchanged.

    Args:
        var0: Input value

    Returns:
        Same value as input
    """
    return var0


# ============================================================================
# ac: Export wrapper for func38 (0 callers)
# ============================================================================

def ac(var0: int, var1: int) -> None:
    """
    $ac: Export wrapper that calls func38.

    Note: var1 is passed but not used.

    Args:
        var0: Parameter passed to func38
        var1: Unused parameter
    """
    from tzar.unknown.func38 import func38
    func38(var0)


# ============================================================================
# func384: Global state update via func811 (1 caller)
# ============================================================================

def func384(var0: int) -> None:
    """
    $func384: Update global state at 9688092.

    Calls func811 with global address and var0, discards result.

    Args:
        var0: Value to pass to func811
    """
    from tzar.unknown.func811 import func811
    func811(9688092, var0)


# ============================================================================
# func378: Entity state update (0 callers)
# ============================================================================

def func378(var0: int, var1: int) -> None:
    """
    $func378: Update entity state via func29.

    Calculates entity pointer from index and calls func29.

    Args:
        var0: Entity index
        var1: Unused parameter
    """
    from tzar.unknown.func29 import func29

    entity_base = i32_load(9671128)
    entity_ptr = entity_base + var0 * 132
    func29(entity_ptr, 1)


# ============================================================================
# func392: Ring buffer read (leaf, 2 callers)
# ============================================================================

def func392(var0: int, var1: int) -> None:
    """
    $func392: Read from ring buffer structure.

    Copies 12 bytes from buffer entry to var0, advances read index.

    Structure at var1:
    - offset 36: buffer base pointer
    - offset 40: buffer size (modulo value)
    - offset 44: current read index

    Args:
        var0: Destination pointer (12 bytes)
        var1: Ring buffer structure
    """
    buffer_base = i32_load(var1 + 36)
    read_idx = i32_load(var1 + 44)
    entry_ptr = buffer_base + read_idx * 12

    # Copy 12 bytes (8 + 4)
    i64_store(var0, i64_load(entry_ptr))
    i32_store(var0 + 8, i32_load(entry_ptr + 8))

    # Advance read index with wrap-around
    buffer_size = i32_load(var1 + 40)
    new_idx = (read_idx + 1) % buffer_size
    i32_store(var1 + 44, new_idx)


# ============================================================================
# func437: Simple wrapper for func436 (batch 25)
# ============================================================================

def func437(var0: int) -> None:
    """
    $func437: Direct wrapper for func436.

    Args:
        var0: Parameter passed to func436
    """
    from tzar.unknown.func436 import func436
    func436(var0)


# ============================================================================
# func439: Wrapper for func149 with zero (batch 25)
# ============================================================================

def func439(var0: int, var1: int) -> None:
    """
    $func439: Call func149 with zero parameter.

    Args:
        var0: First parameter
        var1: Third parameter (second is always 0)
    """
    from tzar.unknown.func149 import func149
    func149(var0, 0, var1)


# ============================================================================
# func430: Initialize with atomic stores (batch 25)
# ============================================================================

def func430(var0: int) -> None:
    """
    $func430: Initialize structure with func393 and atomic stores.

    Stores result of func393 at offset 120, then atomically
    stores 1 at offset 124 and 0 at offset 128.

    Args:
        var0: Structure pointer
    """
    from tzar._runtime import i32_atomic_store
    from tzar.unknown.func393 import func393

    result = func393(var0)
    i32_store(var0 + 120, result)
    i32_atomic_store(var0 + 124, 1)
    i32_atomic_store(var0 + 128, 0)


# ============================================================================
# func452: Initialize buffer structure (batch 25)
# ============================================================================

def func452(var0: int, var1: int) -> int:
    """
    $func452: Initialize a buffer structure.

    Allocates buffer via func58 and sets up structure at var1.

    Structure at var1:
    - offset 0: buffer pointer
    - offset 4: buffer pointer (copy)
    - offset 8: cleared to 0
    - offset 12: capacity (var0)
    - offset 16: self pointer

    Args:
        var0: Buffer capacity
        var1: Structure pointer

    Returns:
        1 if allocation succeeded, 0 otherwise
    """
    from tzar.unknown.func58 import func58

    i32_store(var1 + 8, 0)
    i32_store(var1 + 16, var1)

    # Allocate buffer (var0 as i64, shift 4 = multiply by 16?)
    buffer = func58(var0, 4)

    if buffer:
        i32_store(var1 + 4, buffer)
        i32_store(var1 + 12, var0)
        var2 = 1
    else:
        i32_store(var1 + 12, 0)
        var2 = 0

    i32_store(var1, buffer)
    return var2


# ============================================================================
# func433: File/stream buffer init (leaf, batch 25)
# ============================================================================

def func433(var0: int) -> int:
    """
    $func433: Initialize file/stream buffer.

    Updates buffer state at offset 72, checks for errors,
    and initializes read/write pointers.

    Args:
        var0: Stream structure pointer

    Returns:
        0 on success, -1 on error
    """
    # Update offset 72 with special bit manipulation
    val72 = i32_load(var0 + 72)
    i32_store(var0 + 72, (val72 - 1) | val72)

    # Check for error flag (bit 3)
    val0 = i32_load(var0)
    if val0 & 8:
        i32_store(var0, val0 | 32)  # Set error bit
        return -1

    # Initialize buffer pointers
    i64_store(var0 + 4, 0)  # Clear 8 bytes at offset 4

    buffer_base = i32_load(var0 + 44)
    i32_store(var0 + 28, buffer_base)
    i32_store(var0 + 20, buffer_base)

    buffer_size = i32_load(var0 + 48)
    i32_store(var0 + 16, buffer_base + buffer_size)

    return 0


# ============================================================================
# Aliases
# ============================================================================

identity = func395
export_ac = ac
update_global_state = func384
update_entity_state = func378
ring_buffer_read = func392
simple_func436_wrapper = func437
func149_with_zero = func439
init_with_atomics = func430
init_buffer_struct = func452
stream_buffer_init = func433
