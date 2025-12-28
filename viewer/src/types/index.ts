// Types for Tzar WASM Analyzer

export interface GraphNode {
  id: string;
  name: string;
  val: number;
  group: number;
  isImport: boolean;
  isExport: boolean;
  inDegree: number;
  outDegree: number;
  category?: string;
  depth?: number;  // Depth in call tree (0 = leaf)
  analyzed?: boolean;
  suggestedName?: string;
}

export interface GraphLink {
  source: string;
  target: string;
}

export interface GraphData {
  nodes: GraphNode[];
  links: GraphLink[];
  stats: GraphStats;
}

export interface GraphStats {
  total_nodes: number;
  total_edges: number;
  entry_points: string[];
  leaf_functions: string[];
  most_called: [string, number][];
  largest_callers: [string, number][];
}

export interface TreeNode {
  id: string;
  name: string;
  depth: number;
  children: TreeNode[];
  isLeaf: boolean;
  isImport: boolean;
  isExport: boolean;
  analyzed: boolean;
  category?: string;
}

export interface AnalysisProgress {
  total: number;
  analyzed: number;
  currentDepth: number;
  maxDepth: number;
}

export type ViewMode = 'graph' | 'tree' | 'list' | 'hierarchy';
export type FilterMode = 'all' | 'leaves' | 'entry' | 'analyzed' | 'unanalyzed';
