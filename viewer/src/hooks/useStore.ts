import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { ViewMode, FilterMode, GraphNode } from '../types';

interface AnalyzerStore {
  // View state
  viewMode: ViewMode;
  setViewMode: (mode: ViewMode) => void;

  // Selection
  selectedNode: GraphNode | null;
  setSelectedNode: (node: GraphNode | null) => void;

  // Filter
  searchFilter: string;
  setSearchFilter: (filter: string) => void;
  depthFilter: number | null;
  setDepthFilter: (depth: number | null) => void;
  filterMode: FilterMode;
  setFilterMode: (mode: FilterMode) => void;

  // Analysis progress
  analyzedNodes: Set<string>;
  markAnalyzed: (nodeId: string) => void;
  markUnanalyzed: (nodeId: string) => void;
  clearAnalyzed: () => void;

  // Node annotations
  annotations: Map<string, NodeAnnotation>;
  setAnnotation: (nodeId: string, annotation: NodeAnnotation) => void;
  clearAnnotations: () => void;

  // Current depth level being analyzed
  currentDepth: number;
  setCurrentDepth: (depth: number) => void;

  // Panel visibility
  showSidebar: boolean;
  toggleSidebar: () => void;
  showDetails: boolean;
  toggleDetails: () => void;
}

interface NodeAnnotation {
  suggestedName?: string;
  category?: string;
  notes?: string;
  confidence?: number;
}

export const useStore = create<AnalyzerStore>()(
  persist(
    (set, get) => ({
      // View
      viewMode: 'hierarchy',
      setViewMode: (mode) => set({ viewMode: mode }),

      // Selection
      selectedNode: null,
      setSelectedNode: (node) => set({ selectedNode: node }),

      // Filter
      searchFilter: '',
      setSearchFilter: (filter) => set({ searchFilter: filter }),
      depthFilter: null,
      setDepthFilter: (depth) => set({ depthFilter: depth }),
      filterMode: 'all',
      setFilterMode: (mode) => set({ filterMode: mode }),

      // Analysis
      analyzedNodes: new Set(),
      markAnalyzed: (nodeId) => set((state) => {
        const newSet = new Set(state.analyzedNodes);
        newSet.add(nodeId);
        return { analyzedNodes: newSet };
      }),
      markUnanalyzed: (nodeId) => set((state) => {
        const newSet = new Set(state.analyzedNodes);
        newSet.delete(nodeId);
        return { analyzedNodes: newSet };
      }),
      clearAnalyzed: () => set({ analyzedNodes: new Set() }),

      // Annotations
      annotations: new Map(),
      setAnnotation: (nodeId, annotation) => set((state) => {
        const newMap = new Map(state.annotations);
        newMap.set(nodeId, annotation);
        return { annotations: newMap };
      }),
      clearAnnotations: () => set({ annotations: new Map() }),

      // Depth
      currentDepth: 0,
      setCurrentDepth: (depth) => set({ currentDepth: depth }),

      // Panels
      showSidebar: true,
      toggleSidebar: () => set((state) => ({ showSidebar: !state.showSidebar })),
      showDetails: true,
      toggleDetails: () => set((state) => ({ showDetails: !state.showDetails })),
    }),
    {
      name: 'tzar-analyzer-store',
      partialize: (state) => ({
        analyzedNodes: Array.from(state.analyzedNodes),
        annotations: Array.from(state.annotations.entries()),
        currentDepth: state.currentDepth,
      }),
    }
  )
);
