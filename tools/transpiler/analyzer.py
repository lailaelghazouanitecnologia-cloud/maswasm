"""
Static Analyzer for WAT functions.

Performs:
- Dependency graph construction
- Function categorization
- Pattern detection (struct access, SWAR, memory operations)
- Type inference
"""

from dataclasses import dataclass, field
from typing import Dict, List, Set, Optional, Tuple, Any
from enum import Enum
from collections import defaultdict

from wat_parser import WatModule, WatFunction, WatInstruction, WatType


class FunctionCategory(Enum):
    MEMORY = "memory"           # Memory allocation/management
    PLAYER = "player"           # Player-related functions
    ENTITY = "entity"           # Entity manipulation
    RENDER = "render"           # Rendering
    INPUT = "input"             # Input handling
    GAME = "game"               # Game logic
    MATH = "math"               # Math utilities
    ACCESSOR = "accessor"       # Simple getter/setter
    WRAPPER = "wrapper"         # Thin wrappers around other functions
    UNKNOWN = "unknown"


# Known memory addresses for pattern detection
KNOWN_ADDRESSES = {
    9142424: "game_state_base",
    9142872: "current_player_index",
    9142892: "player_count",
    9561692: "player_array_base",
    9568096: "entity_type_table",
    9671128: "entity_array_base",
    9690464: "heap_metadata",
    9690480: "heap_base",
    9690484: "heap_top",
    9690908: "memory_flags",
    9690912: "mutex",
    9690984: "handler_callback",
}

# Structure strides
PLAYER_STRIDE = 286704
ENTITY_STRIDE = 132
ENTITY_TYPE_STRIDE = 404


@dataclass
class FunctionAnalysis:
    """Analysis results for a single function."""
    name: str
    category: FunctionCategory
    depth: int = 0  # Call depth (0 = leaf)
    calls: Set[str] = field(default_factory=set)
    called_by: Set[str] = field(default_factory=set)

    # Statistics
    instruction_count: int = 0
    load_count: int = 0
    store_count: int = 0
    branch_count: int = 0
    loop_count: int = 0
    block_count: int = 0

    # Detected patterns
    is_leaf: bool = False
    is_wrapper: bool = False
    is_pure: bool = True  # No memory side effects
    uses_globals: bool = False

    # Memory access patterns
    known_addresses: Set[str] = field(default_factory=set)
    struct_access: List[Tuple[str, int]] = field(default_factory=list)  # (type, offset)

    # Complexity estimate
    complexity: int = 0


@dataclass
class DependencyGraph:
    """Function dependency graph."""
    functions: Dict[str, FunctionAnalysis]
    call_graph: Dict[str, Set[str]]  # func -> called functions
    reverse_graph: Dict[str, Set[str]]  # func -> calling functions
    depth_levels: Dict[int, List[str]]  # depth -> list of functions

    def get_topological_order(self) -> List[str]:
        """Get functions in topological order (leaves first)."""
        order = []
        for depth in sorted(self.depth_levels.keys()):
            order.extend(self.depth_levels[depth])
        return order


class StaticAnalyzer:
    """Static analyzer for WAT modules."""

    def __init__(self, module: WatModule):
        self.module = module
        self.analyses: Dict[str, FunctionAnalysis] = {}
        self.call_graph: Dict[str, Set[str]] = defaultdict(set)
        self.reverse_graph: Dict[str, Set[str]] = defaultdict(set)

    def analyze(self) -> DependencyGraph:
        """Analyze the entire module."""
        # First pass: collect basic stats and calls
        for name, func in self.module.functions.items():
            if func.is_import:
                continue
            self.analyses[name] = self._analyze_function(func)

        # Build call graphs
        self._build_call_graph()

        # Calculate depths
        self._calculate_depths()

        # Categorize functions
        self._categorize_functions()

        # Build depth levels
        depth_levels = defaultdict(list)
        for name, analysis in self.analyses.items():
            depth_levels[analysis.depth].append(name)

        return DependencyGraph(
            functions=self.analyses,
            call_graph=dict(self.call_graph),
            reverse_graph=dict(self.reverse_graph),
            depth_levels=dict(depth_levels)
        )

    def _analyze_function(self, func: WatFunction) -> FunctionAnalysis:
        """Analyze a single function."""
        analysis = FunctionAnalysis(
            name=func.name,
            category=FunctionCategory.UNKNOWN
        )

        # Collect statistics from instructions
        self._analyze_instructions(func.body, analysis)

        # Detect if it's a leaf function
        analysis.is_leaf = len(analysis.calls) == 0

        # Detect if it's a wrapper (single call with minimal logic)
        if len(analysis.calls) == 1 and analysis.instruction_count < 15:
            analysis.is_wrapper = True

        # Check purity
        if analysis.store_count > 0 or analysis.uses_globals:
            analysis.is_pure = False

        # Estimate complexity
        analysis.complexity = (
            analysis.instruction_count +
            analysis.branch_count * 2 +
            analysis.loop_count * 5 +
            len(analysis.calls) * 3
        )

        return analysis

    def _analyze_instructions(self, instructions: List[WatInstruction], analysis: FunctionAnalysis):
        """Recursively analyze instructions."""
        for instr in instructions:
            analysis.instruction_count += 1
            opcode = instr.opcode

            # Count instruction types
            if 'load' in opcode:
                analysis.load_count += 1
                analysis.is_pure = False
                # Check for known addresses
                self._check_memory_access(instr, analysis)
            elif 'store' in opcode:
                analysis.store_count += 1
                analysis.is_pure = False
            elif opcode.startswith('br'):
                analysis.branch_count += 1
            elif opcode == 'loop':
                analysis.loop_count += 1
            elif opcode == 'block':
                analysis.block_count += 1
            elif opcode.startswith('global'):
                analysis.uses_globals = True
            elif opcode.startswith('call'):
                # Extract call target
                if instr.operands:
                    target = instr.operands[0]
                    if isinstance(target, str) and target.startswith('$'):
                        analysis.calls.add(target)

            # Recurse into children
            if instr.children:
                self._analyze_instructions(instr.children, analysis)
            if instr.else_children:
                self._analyze_instructions(instr.else_children, analysis)

    def _check_memory_access(self, instr: WatInstruction, analysis: FunctionAnalysis):
        """Check if memory access uses known addresses."""
        for op in instr.operands:
            if isinstance(op, tuple) and op[0] == 'offset':
                offset = op[1]
                if offset in KNOWN_ADDRESSES:
                    analysis.known_addresses.add(KNOWN_ADDRESSES[offset])
                # Check for struct access patterns
                elif offset >= 9561692:  # Player array base
                    if offset < 9568096:
                        field_offset = (offset - 9561692) % PLAYER_STRIDE
                        analysis.struct_access.append(('player', field_offset))
                elif offset >= 9671128:  # Entity array base
                    field_offset = (offset - 9671128) % ENTITY_STRIDE
                    analysis.struct_access.append(('entity', field_offset))

    def _build_call_graph(self):
        """Build call and reverse call graphs."""
        for name, analysis in self.analyses.items():
            for target in analysis.calls:
                self.call_graph[name].add(target)
                self.reverse_graph[target].add(name)

    def _calculate_depths(self):
        """Calculate function depths (0 = leaf)."""
        # Start with leaves
        for name, analysis in self.analyses.items():
            if analysis.is_leaf:
                analysis.depth = 0

        # Iteratively calculate depths
        changed = True
        iterations = 0
        max_iterations = 100

        while changed and iterations < max_iterations:
            changed = False
            iterations += 1

            for name, analysis in self.analyses.items():
                if analysis.is_leaf:
                    continue

                # Depth is 1 + max depth of called functions
                max_child_depth = 0
                for target in analysis.calls:
                    if target in self.analyses:
                        max_child_depth = max(max_child_depth, self.analyses[target].depth)
                    else:
                        # Import or external - treat as depth 0
                        pass

                new_depth = max_child_depth + 1
                if new_depth != analysis.depth:
                    analysis.depth = new_depth
                    changed = True

        # Fill in called_by
        for name, analysis in self.analyses.items():
            analysis.called_by = self.reverse_graph.get(name, set())

    def _categorize_functions(self):
        """Categorize functions based on patterns."""
        for name, analysis in self.analyses.items():
            # Check for memory functions
            if 'heap' in str(analysis.known_addresses).lower() or \
               'memory' in str(analysis.known_addresses).lower():
                analysis.category = FunctionCategory.MEMORY
                continue

            # Check for player functions
            if any(t[0] == 'player' for t in analysis.struct_access) or \
               'player' in str(analysis.known_addresses).lower():
                analysis.category = FunctionCategory.PLAYER
                continue

            # Check for entity functions
            if any(t[0] == 'entity' for t in analysis.struct_access) or \
               'entity' in str(analysis.known_addresses).lower():
                analysis.category = FunctionCategory.ENTITY
                continue

            # Simple accessors (small, no loops, few branches)
            if analysis.instruction_count < 20 and \
               analysis.loop_count == 0 and \
               analysis.branch_count < 3:
                analysis.category = FunctionCategory.ACCESSOR
                continue

            # Wrappers
            if analysis.is_wrapper:
                analysis.category = FunctionCategory.WRAPPER
                continue

            # Math functions (pure, small)
            if analysis.is_pure and analysis.instruction_count < 50:
                analysis.category = FunctionCategory.MATH
                continue

            # Default to game logic
            analysis.category = FunctionCategory.GAME


def analyze_module(module: WatModule) -> DependencyGraph:
    """Analyze a WAT module and return the dependency graph."""
    analyzer = StaticAnalyzer(module)
    return analyzer.analyze()


def print_analysis_summary(graph: DependencyGraph):
    """Print a summary of the analysis."""
    print(f"Analyzed {len(graph.functions)} functions")

    # Category distribution
    categories = defaultdict(int)
    for analysis in graph.functions.values():
        categories[analysis.category] += 1

    print("\nCategory distribution:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat.value}: {count}")

    # Depth distribution
    print("\nDepth distribution:")
    for depth in sorted(graph.depth_levels.keys()):
        count = len(graph.depth_levels[depth])
        print(f"  Depth {depth}: {count} functions")

    # Most called functions
    most_called = sorted(
        [(name, len(a.called_by)) for name, a in graph.functions.items()],
        key=lambda x: -x[1]
    )[:10]

    print("\nMost called functions:")
    for name, count in most_called:
        print(f"  {name}: called by {count} functions")

    # Largest functions
    largest = sorted(
        [(name, a.instruction_count) for name, a in graph.functions.items()],
        key=lambda x: -x[1]
    )[:10]

    print("\nLargest functions:")
    for name, count in largest:
        print(f"  {name}: {count} instructions")


if __name__ == '__main__':
    import sys
    from wat_parser import parse_wat_file

    if len(sys.argv) > 1:
        module = parse_wat_file(sys.argv[1])
        graph = analyze_module(module)
        print_analysis_summary(graph)
