#!/usr/bin/env python3
"""
Call graph builder for Tzar WASM
Builds and exports call graph for visualization
"""

import re
import json
import sys
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, asdict
from typing import Optional

try:
    import networkx as nx
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False

@dataclass
class GraphNode:
    id: str
    name: str
    index: int
    is_import: bool
    is_export: bool
    in_degree: int = 0
    out_degree: int = 0
    category: Optional[str] = None

@dataclass
class GraphEdge:
    source: str
    target: str

def build_callgraph(filepath: Path) -> dict:
    """Build call graph from WAT file."""
    content = filepath.read_text(encoding='utf-8', errors='ignore')
    lines = content.split('\n')

    nodes = {}
    edges = []

    current_func = None
    func_body = []
    brace_depth = 0
    start_depth = 0

    for line in lines:
        stripped = line.strip()
        brace_depth += line.count('(') - line.count(')')

        if stripped.startswith('(func '):
            # Parse header
            name_match = re.search(r'\$([^\s(]+)', stripped)
            index_match = re.search(r'\(;(\d+);\)', stripped)

            name = '$' + name_match.group(1) if name_match else f'$func{len(nodes)}'
            index = int(index_match.group(1)) if index_match else len(nodes)

            current_func = name
            func_body = [line]
            start_depth = brace_depth

            nodes[name] = GraphNode(
                id=name,
                name=name,
                index=index,
                is_import='(import ' in stripped,
                is_export='(export ' in stripped,
            )

        elif current_func is not None:
            func_body.append(line)

            if brace_depth < start_depth:
                # Function ended - extract calls
                body = '\n'.join(func_body)
                calls = extract_calls(body)

                nodes[current_func].out_degree = len(calls)

                for target in calls:
                    edges.append(GraphEdge(source=current_func, target=target))
                    if target in nodes:
                        nodes[target].in_degree += 1

                current_func = None
                func_body = []

    # Calculate statistics
    entry_points = [n.id for n in nodes.values() if n.in_degree == 0 and not n.is_import]
    leaf_funcs = [n.id for n in nodes.values() if n.out_degree == 0]
    most_called = sorted(nodes.values(), key=lambda n: n.in_degree, reverse=True)[:10]
    largest_callers = sorted(nodes.values(), key=lambda n: n.out_degree, reverse=True)[:10]

    return {
        'nodes': [asdict(n) for n in nodes.values()],
        'edges': [asdict(e) for e in edges],
        'stats': {
            'total_nodes': len(nodes),
            'total_edges': len(edges),
            'entry_points': entry_points[:20],
            'leaf_functions': leaf_funcs[:20],
            'most_called': [(n.id, n.in_degree) for n in most_called],
            'largest_callers': [(n.id, n.out_degree) for n in largest_callers],
        }
    }

def extract_calls(body: str) -> list:
    """Extract function calls from body."""
    calls = set()

    for match in re.finditer(r'call\s+(\$[^\s)]+)', body):
        target = match.group(1)
        if not target.startswith('$var') and not target.startswith('$label'):
            calls.add(target)

    return sorted(list(calls))

def export_dot(graph: dict, output_path: Path):
    """Export graph to DOT format."""
    dot = ['digraph CallGraph {']
    dot.append('  rankdir=LR;')
    dot.append('  node [shape=box];')
    dot.append('')

    # Add nodes with colors
    for node in graph['nodes']:
        color = 'lightblue' if node['is_import'] else \
                'lightgreen' if node['in_degree'] == 0 else \
                'lightyellow' if node['out_degree'] == 0 else 'white'

        label = node['name'].replace('$', '').replace('.', '_')
        dot.append(f'  "{node["id"]}" [label="{label}" fillcolor="{color}" style=filled];')

    dot.append('')

    # Add edges
    for edge in graph['edges']:
        dot.append(f'  "{edge["source"]}" -> "{edge["target"]}";')

    dot.append('}')

    output_path.write_text('\n'.join(dot))

def export_for_react(graph: dict, output_path: Path):
    """Export graph in format optimized for React visualization."""
    # Transform for react-force-graph or similar
    react_graph = {
        'nodes': [
            {
                'id': node['id'],
                'name': node['name'].replace('$', ''),
                'val': max(1, node['in_degree']),  # Size by importance
                'group': 1 if node['is_import'] else 2 if node['is_export'] else 0,
                'isImport': node['is_import'],
                'isExport': node['is_export'],
                'inDegree': node['in_degree'],
                'outDegree': node['out_degree'],
            }
            for node in graph['nodes']
        ],
        'links': [
            {
                'source': edge['source'],
                'target': edge['target'],
            }
            for edge in graph['edges']
        ],
        'stats': graph['stats'],
    }

    output_path.write_text(json.dumps(react_graph, indent=2))

def main():
    if len(sys.argv) < 2:
        print("Usage: python build_callgraph.py <wat_file> [output.json]")
        sys.exit(1)

    wat_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('output/graphs/callgraph.json')

    if not wat_file.exists():
        print(f"Error: {wat_file} not found")
        sys.exit(1)

    print(f"Building call graph from {wat_file}...")
    graph = build_callgraph(wat_file)

    # Save JSON
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(graph, indent=2))
    print(f"Call graph saved to {output_file}")

    # Save DOT
    dot_file = output_file.with_suffix('.dot')
    export_dot(graph, dot_file)
    print(f"DOT graph saved to {dot_file}")

    # Save React format
    react_file = output_file.parent / 'callgraph-react.json'
    export_for_react(graph, react_file)
    print(f"React graph saved to {react_file}")

    # Print stats
    stats = graph['stats']
    print(f"\nGraph Statistics:")
    print(f"  Nodes: {stats['total_nodes']}")
    print(f"  Edges: {stats['total_edges']}")
    print(f"  Entry points: {len(stats['entry_points'])}")
    print(f"\nMost called functions:")
    for name, count in stats['most_called'][:5]:
        print(f"  {name}: {count} callers")

if __name__ == '__main__':
    main()
