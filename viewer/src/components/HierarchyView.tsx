import React, { useMemo } from 'react';
import { GraphData, GraphNode } from '../types';
import { useTreeStructure } from '../hooks/useGraphData';
import { useStore } from '../hooks/useStore';

interface Props {
  data: GraphData;
}

export function HierarchyView({ data }: Props) {
  const treeData = useTreeStructure(data);
  const {
    currentDepth,
    setCurrentDepth,
    selectedNode,
    setSelectedNode,
    analyzedNodes,
    markAnalyzed,
    searchFilter,
  } = useStore();

  const levels = useMemo(() => {
    if (!treeData) return [];

    const result: { depth: number; nodes: GraphNode[]; analyzed: number }[] = [];

    for (let d = 0; d <= treeData.maxDepth; d++) {
      const nodesAtDepth = treeData.byDepth.get(d) ?? [];
      const analyzedCount = nodesAtDepth.filter(n => analyzedNodes.has(n.id)).length;
      result.push({
        depth: d,
        nodes: nodesAtDepth,
        analyzed: analyzedCount,
      });
    }

    return result;
  }, [treeData, analyzedNodes]);

  const filteredNodes = useMemo(() => {
    const level = levels.find(l => l.depth === currentDepth);
    if (!level) return [];

    let nodes = level.nodes;

    if (searchFilter) {
      const lowerFilter = searchFilter.toLowerCase();
      nodes = nodes.filter(n =>
        n.name.toLowerCase().includes(lowerFilter) ||
        n.id.toLowerCase().includes(lowerFilter)
      );
    }

    return nodes.sort((a, b) => b.inDegree - a.inDegree);
  }, [levels, currentDepth, searchFilter]);

  if (!treeData) return <div>Loading tree structure...</div>;

  return (
    <div style={styles.container}>
      {/* Depth Navigator */}
      <div style={styles.depthNav}>
        <h3 style={styles.title}>Analysis Depth</h3>
        <p style={styles.hint}>Start from bottom (leaves) and work up</p>

        <div style={styles.levels}>
          {levels.map((level, i) => (
            <button
              key={level.depth}
              style={{
                ...styles.levelBtn,
                ...(currentDepth === level.depth ? styles.levelBtnActive : {}),
              }}
              onClick={() => setCurrentDepth(level.depth)}
            >
              <span style={styles.levelLabel}>
                {level.depth === 0 ? '🍃 Leaves' : `Level ${level.depth}`}
              </span>
              <span style={styles.levelCount}>
                {level.analyzed}/{level.nodes.length}
              </span>
              <div
                style={{
                  ...styles.progressBar,
                  width: `${(level.analyzed / level.nodes.length) * 100}%`,
                }}
              />
            </button>
          ))}
        </div>
      </div>

      {/* Current Level Nodes */}
      <div style={styles.nodeList}>
        <h3 style={styles.title}>
          {currentDepth === 0 ? 'Leaf Functions' : `Depth ${currentDepth}`}
          <span style={styles.countBadge}>{filteredNodes.length}</span>
        </h3>

        <div style={styles.nodes}>
          {filteredNodes.map((node) => (
            <NodeCard
              key={node.id}
              node={node}
              isSelected={selectedNode?.id === node.id}
              isAnalyzed={analyzedNodes.has(node.id)}
              onSelect={() => setSelectedNode(node)}
              onMarkAnalyzed={() => markAnalyzed(node.id)}
              callers={treeData.callers.get(node.id)}
              callees={treeData.callees.get(node.id)}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

interface NodeCardProps {
  node: GraphNode;
  isSelected: boolean;
  isAnalyzed: boolean;
  onSelect: () => void;
  onMarkAnalyzed: () => void;
  callers?: Set<string>;
  callees?: Set<string>;
}

function NodeCard({
  node,
  isSelected,
  isAnalyzed,
  onSelect,
  onMarkAnalyzed,
  callers,
  callees,
}: NodeCardProps) {
  return (
    <div
      style={{
        ...styles.card,
        ...(isSelected ? styles.cardSelected : {}),
        ...(isAnalyzed ? styles.cardAnalyzed : {}),
      }}
      onClick={onSelect}
    >
      <div style={styles.cardHeader}>
        <span style={styles.nodeName}>{node.name}</span>
        {node.isImport && <span style={styles.badge}>import</span>}
        {node.isExport && <span style={styles.badgeExport}>export</span>}
        {isAnalyzed && <span style={styles.badgeAnalyzed}>✓</span>}
      </div>

      <div style={styles.cardMeta}>
        <span>↓ {callees?.size ?? 0} calls</span>
        <span>↑ {callers?.size ?? 0} callers</span>
      </div>

      {!isAnalyzed && (
        <button
          style={styles.analyzeBtn}
          onClick={(e) => {
            e.stopPropagation();
            onMarkAnalyzed();
          }}
        >
          Mark Analyzed
        </button>
      )}
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  container: {
    display: 'flex',
    height: '100%',
    gap: '1rem',
    padding: '1rem',
    overflow: 'hidden',
  },
  depthNav: {
    width: '250px',
    flexShrink: 0,
    background: '#161b22',
    borderRadius: '8px',
    padding: '1rem',
    overflowY: 'auto',
  },
  title: {
    fontSize: '14px',
    fontWeight: 600,
    color: '#c9d1d9',
    marginBottom: '8px',
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
  },
  hint: {
    fontSize: '12px',
    color: '#8b949e',
    marginBottom: '16px',
  },
  levels: {
    display: 'flex',
    flexDirection: 'column',
    gap: '4px',
  },
  levelBtn: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: '8px 12px',
    background: '#21262d',
    border: '1px solid #30363d',
    borderRadius: '6px',
    cursor: 'pointer',
    position: 'relative',
    overflow: 'hidden',
    color: '#c9d1d9',
    fontSize: '13px',
  },
  levelBtnActive: {
    background: '#388bfd20',
    borderColor: '#388bfd',
  },
  levelLabel: {
    zIndex: 1,
  },
  levelCount: {
    fontSize: '11px',
    color: '#8b949e',
    zIndex: 1,
  },
  progressBar: {
    position: 'absolute',
    left: 0,
    bottom: 0,
    height: '3px',
    background: '#238636',
    transition: 'width 0.3s ease',
  },
  nodeList: {
    flex: 1,
    background: '#161b22',
    borderRadius: '8px',
    padding: '1rem',
    overflowY: 'auto',
  },
  countBadge: {
    background: '#30363d',
    padding: '2px 8px',
    borderRadius: '10px',
    fontSize: '12px',
    color: '#8b949e',
  },
  nodes: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
    gap: '12px',
    marginTop: '12px',
  },
  card: {
    background: '#21262d',
    border: '1px solid #30363d',
    borderRadius: '8px',
    padding: '12px',
    cursor: 'pointer',
    transition: 'all 0.15s ease',
  },
  cardSelected: {
    borderColor: '#388bfd',
    background: '#388bfd15',
  },
  cardAnalyzed: {
    opacity: 0.7,
    borderColor: '#238636',
  },
  cardHeader: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    marginBottom: '8px',
  },
  nodeName: {
    fontFamily: 'monospace',
    fontSize: '13px',
    color: '#c9d1d9',
    flex: 1,
    overflow: 'hidden',
    textOverflow: 'ellipsis',
    whiteSpace: 'nowrap',
  },
  badge: {
    fontSize: '10px',
    padding: '2px 6px',
    borderRadius: '4px',
    background: '#1f6feb30',
    color: '#58a6ff',
  },
  badgeExport: {
    fontSize: '10px',
    padding: '2px 6px',
    borderRadius: '4px',
    background: '#23863630',
    color: '#3fb950',
  },
  badgeAnalyzed: {
    fontSize: '10px',
    padding: '2px 6px',
    borderRadius: '4px',
    background: '#238636',
    color: '#fff',
  },
  cardMeta: {
    display: 'flex',
    gap: '12px',
    fontSize: '11px',
    color: '#8b949e',
    marginBottom: '8px',
  },
  analyzeBtn: {
    width: '100%',
    padding: '6px',
    background: '#21262d',
    border: '1px solid #30363d',
    borderRadius: '4px',
    color: '#8b949e',
    fontSize: '11px',
    cursor: 'pointer',
  },
};
