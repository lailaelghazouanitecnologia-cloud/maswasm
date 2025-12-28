"""
Import stubs - External functions imported from the host environment.

These functions are provided by the JavaScript/runtime host and cannot
be transpiled. They need to be implemented by the runtime.

Module "a" imports - typically memory/system functions:
- a.b: Memory allocation (malloc-like) - 162 callers
- a.c: Memory deallocation (free-like) - 69 callers
- a.d: Memory reallocation (realloc-like) - 65 callers
- a.e-a.z: Various system callbacks
"""

from typing import Any


# ============================================================================
# Memory Management Imports
# ============================================================================

def a_b(size: int) -> int:
    """
    $a.b: Memory allocation (malloc).

    Called by 162 functions. This is the primary memory allocator.

    Args:
        size: Number of bytes to allocate

    Returns:
        Pointer to allocated memory, or 0 on failure
    """
    raise NotImplementedError("Import $a.b (malloc) must be provided by runtime")


def a_c(ptr: int) -> None:
    """
    $a.c: Memory deallocation (free).

    Called by 69 functions. Frees previously allocated memory.

    Args:
        ptr: Pointer to memory to free
    """
    raise NotImplementedError("Import $a.c (free) must be provided by runtime")


def a_d(ptr: int, size: int) -> int:
    """
    $a.d: Memory reallocation (realloc).

    Called by 65 functions. Resizes allocated memory.

    Args:
        ptr: Pointer to existing allocation
        size: New size in bytes

    Returns:
        Pointer to reallocated memory
    """
    raise NotImplementedError("Import $a.d (realloc) must be provided by runtime")


# ============================================================================
# System Callback Imports
# ============================================================================

def a_e(*args: Any) -> Any:
    """$a.e: System callback (7 callers)."""
    raise NotImplementedError("Import $a.e must be provided by runtime")


def a_f(*args: Any) -> Any:
    """$a.f: System callback (4 callers)."""
    raise NotImplementedError("Import $a.f must be provided by runtime")


def a_g() -> None:
    """$a.g: Abort/unreachable handler (2 callers)."""
    raise NotImplementedError("Import $a.g (abort) must be provided by runtime")


def a_h(*args: Any) -> Any:
    """$a.h: System callback (1 caller)."""
    raise NotImplementedError("Import $a.h must be provided by runtime")


def a_i(*args: Any) -> Any:
    """$a.i: System callback (2 callers)."""
    raise NotImplementedError("Import $a.i must be provided by runtime")


def a_j(*args: Any) -> Any:
    """$a.j: System callback (1 caller)."""
    raise NotImplementedError("Import $a.j must be provided by runtime")


def a_k(*args: Any) -> Any:
    """$a.k: System callback (1 caller)."""
    raise NotImplementedError("Import $a.k must be provided by runtime")


def a_l(*args: Any) -> Any:
    """$a.l: System callback (1 caller)."""
    raise NotImplementedError("Import $a.l must be provided by runtime")


def a_m(*args: Any) -> Any:
    """$a.m: System callback (1 caller)."""
    raise NotImplementedError("Import $a.m must be provided by runtime")


def a_n(*args: Any) -> Any:
    """$a.n: System callback (1 caller)."""
    raise NotImplementedError("Import $a.n must be provided by runtime")


def a_o(*args: Any) -> Any:
    """$a.o: System callback (1 caller)."""
    raise NotImplementedError("Import $a.o must be provided by runtime")


def a_p(*args: Any) -> Any:
    """$a.p: System callback (1 caller)."""
    raise NotImplementedError("Import $a.p must be provided by runtime")


def a_q(*args: Any) -> Any:
    """$a.q: System callback (1 caller)."""
    raise NotImplementedError("Import $a.q must be provided by runtime")


def a_r(*args: Any) -> Any:
    """$a.r: System callback (1 caller)."""
    raise NotImplementedError("Import $a.r must be provided by runtime")


def a_s(*args: Any) -> Any:
    """$a.s: System callback (1 caller)."""
    raise NotImplementedError("Import $a.s must be provided by runtime")


def a_t(*args: Any) -> Any:
    """$a.t: System callback (1 caller)."""
    raise NotImplementedError("Import $a.t must be provided by runtime")


def a_u(*args: Any) -> Any:
    """$a.u: System callback (1 caller)."""
    raise NotImplementedError("Import $a.u must be provided by runtime")


def a_v(*args: Any) -> Any:
    """$a.v: System callback (1 caller)."""
    raise NotImplementedError("Import $a.v must be provided by runtime")


def a_w(*args: Any) -> Any:
    """$a.w: System callback (1 caller)."""
    raise NotImplementedError("Import $a.w must be provided by runtime")


def a_x(*args: Any) -> Any:
    """$a.x: System callback (1 caller)."""
    raise NotImplementedError("Import $a.x must be provided by runtime")


def a_y(*args: Any) -> Any:
    """$a.y: System callback (1 caller)."""
    raise NotImplementedError("Import $a.y must be provided by runtime")


def a_z(*args: Any) -> Any:
    """$a.z: System callback (1 caller)."""
    raise NotImplementedError("Import $a.z must be provided by runtime")


def a_A(*args: Any) -> Any:
    """$a.A: System callback (1 caller)."""
    raise NotImplementedError("Import $a.A must be provided by runtime")
