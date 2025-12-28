"""
Stub exports - Empty functions that are exported but do nothing.
These are likely callback placeholders or optional hooks.

$Ga (export): 3 params, no-op
$Se (export): 1 param, no-op
$Ba (export): no params, no-op - exported as Ba, Fa, Jb, he
"""


def Ga(var0: int, var1: int, var2: int) -> None:
    """Stub export - no operation."""
    pass


def Se(var0: int) -> None:
    """Stub export - no operation."""
    pass


def Ba() -> None:
    """
    Stub export - no operation.

    Exported with multiple names: Ba, Fa, Jb, he
    These may be different callback hooks that share the same no-op implementation.
    """
    pass


# Aliases for WASM function names
func109 = Ga  # Index 109
func110 = Se  # Index 110
Fa = Ba
Jb = Ba
he = Ba
