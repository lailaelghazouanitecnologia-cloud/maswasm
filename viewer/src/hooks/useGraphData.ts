import { useState, useEffect, useMemo } from 'react';
import { GraphData, GraphNode, TreeNode } from '../types';

// Sample data for development - will be replaced with file loading
const SAMPLE_DATA: GraphData = {
  nodes: [],
  links: [],
  stats: {
    total_nodes: 0,
    total_edges: 0,
    entry_points: [],
    leaf_functions: [],
    most_called: [],
    largest_callers: [],
  },
};

export function useGraphData(dataPath?: string) {
  const [data, setData] = useState<GraphData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadData() {
      try {
        setLoading(true);
        if (dataPath) {
          const response = await fetch(dataPath);
          const json = await response.json();
          setData(json);
        } else {
          // Try to load from default path
          try {
            const response = await fetch('/data/callgraph-react.json');
            const json = await response.json();
            setData(json);
          } catch {
            setData(SAMPLE_DATA);
          }
        }
      } catch (e) {
        setError(e instanceof Error ? e.message : 'Failed to load data');
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, [dataPath]);

  return { data, loading, error, setData };
}

export function useTreeStructure(data: GraphData | null) {
  return useMemo(() => {
    if (!data) return null;

    // Build adjacency maps
    const callers = new Map<string, Set<string>>();  // who calls this function
    const callees = new Map<string, Set<string>>();  // who this function calls

    for (const link of data.links) {
      if (!callers.has(link.target)) callers.set(link.target, new Set());
      if (!callees.has(link.source)) callees.set(link.source, new Set());

      callers.get(link.target)!.add(link.source);
      callees.get(link.source)!.add(link.target);
    }

    // Calculate depth (0 = leaf, higher = closer to entry points)
    const depths = new Map<string, number>();

    // First, find all leaves (functions that don't call others)
    const leaves: string[] = [];
    for (const node of data.nodes) {
      if (!callees.has(node.id) || callees.get(node.id)!.size === 0) {
        leaves.push(node.id);
        depths.set(node.id, 0);
      }
    }

    // BFS from leaves upward
    const queue = [...leaves];
    while (queue.length > 0) {
      const current = queue.shift()!;
      const currentDepth = depths.get(current) ?? 0;

      const parents = callers.get(current);
      if (parents) {
        for (const parent of parents) {
          const existingDepth = depths.get(parent) ?? -1;
          const newDepth = currentDepth + 1;

          if (newDepth > existingDepth) {
            depths.set(parent, newDepth);
            queue.push(parent);
          }
        }
      }
    }

    // Group by depth
    const byDepth = new Map<number, GraphNode[]>();
    let maxDepth = 0;

    for (const node of data.nodes) {
      const depth = depths.get(node.id) ?? 0;
      maxDepth = Math.max(maxDepth, depth);

      if (!byDepth.has(depth)) byDepth.set(depth, []);
      byDepth.get(depth)!.push({ ...node, depth });
    }

    return {
      depths,
      byDepth,
      maxDepth,
      leaves,
      callers,
      callees,
    };
  }, [data]);
}

export function useFilteredNodes(
  data: GraphData | null,
  treeData: ReturnType<typeof useTreeStructure>,
  filter: string,
  depthFilter: number | null,
  showAnalyzed: boolean
) {
  return useMemo(() => {
    if (!data || !treeData) return [];

    let nodes = data.nodes.map(n => ({
      ...n,
      depth: treeData.depths.get(n.id) ?? 0,
    }));

    // Filter by search
    if (filter) {
      const lowerFilter = filter.toLowerCase();
      nodes = nodes.filter(n =>
        n.name.toLowerCase().includes(lowerFilter) ||
        n.id.toLowerCase().includes(lowerFilter) ||
        n.suggestedName?.toLowerCase().includes(lowerFilter)
      );
    }

    // Filter by depth
    if (depthFilter !== null) {
      nodes = nodes.filter(n => n.depth === depthFilter);
    }

    // Filter by analyzed status
    if (!showAnalyzed) {
      nodes = nodes.filter(n => !n.analyzed);
    }

    return nodes;
  }, [data, treeData, filter, depthFilter, showAnalyzed]);
}
