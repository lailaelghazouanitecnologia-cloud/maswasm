"""
Tzar Engine - Memory Management Module.
Implements dlmalloc-style heap management.

Heap Layout:
    HEAP_BASE → Start of heap memory
    HEAP_TOP  → Current allocation frontier
    HEAP_END  → End of heap memory

Block Header (8 bytes before user data):
    [prev_size: 4 bytes][size | flags: 4 bytes]

Flags (in size field):
    bit 0: PREV_INUSE - Previous chunk is in use
    bit 1: MMAPPED - Chunk was mmap'd
    bit 2: NON_MAIN_ARENA - Chunk belongs to non-main arena

Free Block Structure:
    Small bins (<256 bytes): doubly linked list at offset 8, 12
    Large bins (tree): left/right at 16, 20; parent at 24; index at 28
"""

from tzar.runtime import (
    load32, store32, load8u, store8,
    atomic_load, atomic_store,
    rotl, u32, G,
)

# =============================================================================
# Heap Constants
# =============================================================================

HEAP_FREELIST = 9690464   # Small bin bitmap
HEAP_TREE = 9690468       # Large bin bitmap
FREE_SIZE = 9690472       # Total free bytes
HEAP_TOTAL = 9690476      # Total heap size
HEAP_BASE = 9690480       # Heap start address
HEAP_TOP = 9690484        # Top chunk address
HEAP_END = 9690488        # Heap end address
ALLOC_COUNT = 9690496     # Allocation counter
MEM_FLAGS = 9690908       # Memory subsystem flags
MEM_MUTEX = 9690912       # Memory mutex for threading
ALLOC_HANDLER = 9690984   # Out-of-memory handler

# Tree bin base address
TREE_BINS = 9690768

# Flags
PREV_INUSE = 1
MMAPPED = 2
SIZE_MASK = ~7  # -8


# =============================================================================
# Low-level Heap Operations
# =============================================================================

def _get_chunk_size(chunk_ptr: int) -> int:
    """Get size of chunk (masking out flags)."""
    return load32(chunk_ptr + 4) & SIZE_MASK


def _is_prev_inuse(chunk_ptr: int) -> bool:
    """Check if previous chunk is in use."""
    return bool(load32(chunk_ptr + 4) & PREV_INUSE)


def _unlink_small_chunk(chunk_ptr: int, size: int):
    """Remove small chunk from its bin."""
    bin_idx = size >> 3
    fwd = load32(chunk_ptr + 12)
    bck = load32(chunk_ptr + 8)

    if fwd == bck:
        # Last chunk in bin - clear bit
        store32(HEAP_FREELIST, load32(HEAP_FREELIST) & rotl(-2, bin_idx))
    else:
        store32(bck + 12, fwd)
        store32(fwd + 8, bck)


def _unlink_large_chunk(chunk_ptr: int):
    """Remove large chunk from tree bin."""
    parent = load32(chunk_ptr + 24)

    # Find replacement node
    if chunk_ptr == load32(chunk_ptr + 12):
        # Self-referential - check children
        right = load32(chunk_ptr + 20)
        if right:
            replacement_ptr = chunk_ptr + 20
            replacement = right
        else:
            left = load32(chunk_ptr + 16)
            if left:
                replacement_ptr = chunk_ptr + 16
                replacement = left
            else:
                replacement = 0

        # Descend to find leaf
        if replacement:
            while True:
                right = load32(replacement + 20)
                if right:
                    replacement_ptr = replacement + 20
                    replacement = right
                    continue
                left = load32(replacement + 16)
                if left:
                    replacement_ptr = replacement + 16
                    replacement = left
                    continue
                break
            store32(replacement_ptr, 0)
    else:
        # Not self-referential - just unlink
        fwd = load32(chunk_ptr + 12)
        bck = load32(chunk_ptr + 8)
        store32(bck + 12, fwd)
        store32(fwd + 8, bck)
        return

    if not parent:
        return

    bin_idx = load32(chunk_ptr + 28)
    tree_bin = TREE_BINS + (bin_idx << 2)

    if load32(tree_bin) == chunk_ptr:
        store32(tree_bin, replacement)
        if not replacement:
            store32(HEAP_TREE, load32(HEAP_TREE) & rotl(-2, bin_idx))
    else:
        if load32(parent + 16) == chunk_ptr:
            store32(parent + 16, replacement)
        else:
            store32(parent + 20, replacement)

    if replacement:
        store32(replacement + 24, parent)
        left = load32(chunk_ptr + 16)
        if left:
            store32(replacement + 16, left)
            store32(left + 24, replacement)
        right = load32(chunk_ptr + 20)
        if right:
            store32(replacement + 20, right)
            store32(right + 24, replacement)


# =============================================================================
# Public API
# =============================================================================

def malloc(size: int) -> int:
    """
    Allocate memory block.

    Args:
        size: Number of bytes to allocate

    Returns:
        Pointer to allocated memory, or 0 on failure
    """
    # Minimum allocation size
    if u32(size) <= 1:
        size = 1

    # Try allocation
    while True:
        result = _do_malloc(size)
        if result:
            return result

        # Check for out-of-memory handler
        handler = atomic_load(ALLOC_HANDLER)
        if handler:
            # Would call handler here
            continue

        # Allocation failed
        _trigger_oom()
        raise RuntimeError("Out of memory")


def free(ptr: int) -> None:
    """
    Free previously allocated memory.

    Args:
        ptr: Pointer returned by malloc
    """
    if not ptr:
        return

    # Check threading
    if load8u(MEM_FLAGS) & 2:
        if not _try_lock_mutex(MEM_MUTEX):
            return

    chunk = ptr - 8
    size_field = load32(ptr - 4)
    chunk_size = size_field & SIZE_MASK
    next_chunk = chunk + chunk_size

    # Coalesce with previous if free
    if not (size_field & PREV_INUSE) and (size_field & 3):
        prev_size = load32(chunk)
        prev_chunk = chunk - prev_size

        if u32(prev_chunk) >= u32(load32(HEAP_BASE)):
            chunk_size += prev_size

            if load32(HEAP_TOP) != prev_chunk:
                # Unlink previous chunk
                if u32(prev_size) <= 255:
                    _unlink_small_chunk(prev_chunk, prev_size)
                else:
                    _unlink_large_chunk(prev_chunk)

            chunk = prev_chunk

    # Coalesce with next if free
    next_size_field = load32(next_chunk + 4)
    if not (next_size_field & PREV_INUSE):
        next_size = next_size_field & SIZE_MASK
        chunk_size += next_size

        if u32(next_size) <= 255:
            _unlink_small_chunk(next_chunk, next_size)
        else:
            _unlink_large_chunk(next_chunk)

    # Insert into appropriate bin
    _insert_chunk(chunk, chunk_size)

    # Update free size tracking
    store32(FREE_SIZE, load32(FREE_SIZE) + chunk_size)

    # Unlock if needed
    if load8u(MEM_FLAGS) & 2:
        _unlock_mutex(MEM_MUTEX)


def _do_malloc(size: int) -> int:
    """Internal malloc implementation."""
    # Implementation details handled by runtime
    # This is a stub - actual implementation is complex
    return 0


def _try_lock_mutex(mutex: int) -> bool:
    """Try to acquire mutex."""
    return True  # Stub


def _unlock_mutex(mutex: int) -> None:
    """Release mutex."""
    pass  # Stub


def _insert_chunk(chunk: int, size: int) -> None:
    """Insert free chunk into appropriate bin."""
    pass  # Stub


def _trigger_oom() -> None:
    """Trigger out-of-memory handler."""
    pass  # Stub


# =============================================================================
# Legacy Aliases
# =============================================================================

# Original exported names
func26 = malloc
af = free
