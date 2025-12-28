#!/usr/bin/env python3
"""
Generate processing tree for bottom-up transpilation.

Creates:
- Topological order (leaves first)
- Cycle detection (SCCs)
- Dependency map for each function
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class FunctionNode:
    id: str
    name: str
    depth: int
    is_import: bool
    is_export: bool
    calls: list  # Functions this one calls
    called_by: list  # Functions that call this one
    scc_id: Optional[int]  # Strongly connected component ID (for cycles)
    status: str  # pending, wip, done

def load_callgraph(path: Path) -> dict:
    """Load the call graph JSON."""
    return json.loads(path.read_text())

def build_adjacency(data: dict) -> tuple[dict, dict]:
    """Build caller and callee adjacency lists."""
    callees = defaultdict(set)  # who does X call
    callers = defaultdict(set)  # who calls X

    # Handle both 'links' and 'edges' keys
    edges = data.get('links') or data.get('edges', [])
    for link in edges:
        src = link['source']
        tgt = link['target']
        callees[src].add(tgt)
        callers[tgt].add(src)

    return dict(callees), dict(callers)

def calculate_depths(nodes: list[str], callees: dict, callers: dict) -> dict:
    """Calculate depth for each node (0 = leaf, higher = closer to entry)."""
    depths = {}

    # Find leaves (no outgoing calls)
    leaves = [n for n in nodes if not callees.get(n)]
    for leaf in leaves:
        depths[leaf] = 0

    # BFS upward from leaves - but with visited check to avoid cycles
    queue = leaves[:]
    visited_count = defaultdict(int)
    max_iterations = len(nodes) * 10  # Safety limit

    iteration = 0
    while queue and iteration < max_iterations:
        iteration += 1
        current = queue.pop(0)
        current_depth = depths.get(current, 0)

        for caller in callers.get(current, []):
            visited_count[caller] += 1
            new_depth = current_depth + 1
            if depths.get(caller, -1) < new_depth:
                depths[caller] = new_depth
                # Only re-add if we haven't visited too many times
                if visited_count[caller] < 5:
                    queue.append(caller)

    # Assign depth 0 to any remaining (cycles or orphans)
    for n in nodes:
        if n not in depths:
            depths[n] = 0

    return depths

def find_cycles_simple(nodes: list[str], callees: dict) -> list[list[str]]:
    """Simple cycle detection using DFS."""
    cycles = []
    visited = set()
    rec_stack = set()

    def dfs(node, path):
        if node in rec_stack:
            # Found cycle
            cycle_start = path.index(node)
            cycle = path[cycle_start:]
            if len(cycle) > 1:
                cycles.append(cycle)
            return

        if node in visited:
            return

        visited.add(node)
        rec_stack.add(node)
        path.append(node)

        for callee in callees.get(node, []):
            if len(path) < 100:  # Limit depth
                dfs(callee, path.copy())

        rec_stack.discard(node)

    # Only check a subset to avoid long runtime
    for node in list(nodes)[:500]:
        if node not in visited:
            dfs(node, [])

    return cycles

def generate_tree(callgraph_path: Path, output_path: Path):
    """Generate the processing tree."""
    print("Loading callgraph...")
    data = load_callgraph(callgraph_path)

    nodes_data = {n['id']: n for n in data['nodes']}
    node_ids = list(nodes_data.keys())
    print(f"  {len(node_ids)} nodes")

    print("Building adjacency...")
    callees, callers = build_adjacency(data)

    print("Finding cycles...")
    cycles = find_cycles_simple(node_ids, callees)
    scc_map = {}
    for i, cycle in enumerate(cycles):
        for node in cycle:
            scc_map[node] = i
    print(f"  {len(cycles)} cycles found")

    print("Calculating depths...")
    depths = calculate_depths(node_ids, callees, callers)

    # Build processing order (sort by depth, then by name)
    print("Building processing order...")
    processing_order = sorted(node_ids, key=lambda n: (depths.get(n, 0), n))

    # Build function nodes
    functions = {}
    for node_id in node_ids:
        node_data = nodes_data.get(node_id, {})
        functions[node_id] = asdict(FunctionNode(
            id=node_id,
            name=node_id.replace('$', ''),
            depth=depths.get(node_id, 0),
            is_import=node_data.get('isImport', False) or '.' in node_id,
            is_export=node_data.get('isExport', False),
            calls=list(callees.get(node_id, [])),
            called_by=list(callers.get(node_id, [])),
            scc_id=scc_map.get(node_id),
            status='pending'
        ))

    # Group by depth
    by_depth = defaultdict(list)
    for node_id, info in functions.items():
        by_depth[info['depth']].append(node_id)

    max_depth = max(depths.values()) if depths else 0

    # Summary
    result = {
        'summary': {
            'total_functions': len(functions),
            'max_depth': max_depth,
            'leaf_count': len(by_depth.get(0, [])),
            'cycle_count': len(cycles),
            'import_count': sum(1 for f in functions.values() if f['is_import']),
            'export_count': sum(1 for f in functions.values() if f['is_export']),
        },
        'by_depth': {str(d): fns for d, fns in sorted(by_depth.items())},
        'cycles': [{'id': i, 'functions': c} for i, c in enumerate(cycles)],
        'processing_order': processing_order,
        'functions': functions,
    }

    print("Saving...")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2))

    # Print summary
    print(f"\n{'='*60}")
    print("  PROCESSING TREE GENERATED")
    print('='*60)
    print(f"\n📊 Summary:")
    print(f"   Total functions:  {result['summary']['total_functions']}")
    print(f"   Max depth:        {result['summary']['max_depth']}")
    print(f"   Leaf functions:   {result['summary']['leaf_count']}")
    print(f"   Cycles detected:  {result['summary']['cycle_count']}")
    print(f"   Imports:          {result['summary']['import_count']}")
    print(f"   Exports:          {result['summary']['export_count']}")

    print(f"\n📏 By Depth:")
    for depth in sorted(by_depth.keys())[:15]:
        count = len(by_depth[depth])
        bar = '█' * min(count // 5, 40)
        print(f"   Depth {depth:2d}: {count:4d} {bar}")
    if max_depth > 14:
        print(f"   ... (up to depth {max_depth})")

    if cycles:
        print(f"\n⚠️  Cycles (process as groups):")
        for cg in cycles[:3]:
            funcs = ', '.join(cg[:3])
            more = f"... +{len(cg)-3}" if len(cg) > 3 else ""
            print(f"   {funcs} {more}")

    print(f"\n✅ Saved to {output_path}")
    print('='*60)

def main():
    callgraph_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('output/graphs/callgraph.json')
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('tzar/_tree.json')

    if not callgraph_path.exists():
        print(f"Error: {callgraph_path} not found")
        print("Run: python tools/build_callgraph.py mgame first")
        sys.exit(1)

    generate_tree(callgraph_path, output_path)

if __name__ == '__main__':
    main()
