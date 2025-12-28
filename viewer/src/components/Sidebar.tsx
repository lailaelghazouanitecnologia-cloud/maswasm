import React from 'react';
import { GraphData } from '../types';
import { useStore } from '../hooks/useStore';
import { useTreeStructure } from '../hooks/useGraphData';

interface Props {
  data: GraphData;
}

export function Sidebar({ data }: Props) {
  const {
    viewMode,
    setViewMode,
    searchFilter,
    setSearchFilter,
    analyzedNodes,
    clearAnalyzed,
    currentDepth,
  } = useStore();

  const treeData = useTreeStructure(data);

  const progress = React.useMemo(() => {
    if (!treeData) return { total: 0, analyzed: 0, percent: 0 };
    const total = data.nodes.length;
    const analyzed = analyzedNodes.size;
    return {
      total,
      analyzed,
      percent: Math.round((analyzed / total) * 100),
    };
  }, [data, treeData, analyzedNodes]);

  return (
    <div style={styles.sidebar}>
      <div style={styles.header}>
        <h1 style={styles.title}>⚔️ Tzar Analyzer</h1>
        <p style={styles.subtitle}>WASM Static Analysis</p>
      </div>

      {/* Search */}
      <div style={styles.section}>
        <input
          type="text"
          placeholder="Search functions..."
          value={searchFilter}
          onChange={(e) => setSearchFilter(e.target.value)}
          style={styles.searchInput}
        />
      </div>

      {/* View Mode */}
      <div style={styles.section}>
        <h3 style={styles.sectionTitle}>View Mode</h3>
        <div style={styles.viewModes}>
          {(['hierarchy', 'graph', 'list'] as const).map((mode) => (
            <button
              key={mode}
              style={{
                ...styles.viewModeBtn,
                ...(viewMode === mode ? styles.viewModeBtnActive : {}),
              }}
              onClick={() => setViewMode(mode)}
            >
              {mode === 'hierarchy' && '🌲'}
              {mode === 'graph' && '🕸️'}
              {mode === 'list' && '📋'}
              {' '}{mode}
            </button>
          ))}
        </div>
      </div>

      {/* Progress */}
      <div style={styles.section}>
        <h3 style={styles.sectionTitle}>Analysis Progress</h3>
        <div style={styles.progressContainer}>
          <div style={styles.progressBar}>
            <div
              style={{
                ...styles.progressFill,
                width: `${progress.percent}%`,
              }}
            />
          </div>
          <div style={styles.progressText}>
            {progress.analyzed} / {progress.total} ({progress.percent}%)
          </div>
        </div>
        {analyzedNodes.size > 0 && (
          <button style={styles.clearBtn} onClick={clearAnalyzed}>
            Clear Progress
          </button>
        )}
      </div>

      {/* Stats */}
      <div style={styles.section}>
        <h3 style={styles.sectionTitle}>Module Stats</h3>
        <div style={styles.statsList}>
          <div style={styles.statItem}>
            <span>Total Functions</span>
            <span style={styles.statValue}>{data.stats.total_nodes}</span>
          </div>
          <div style={styles.statItem}>
            <span>Call Edges</span>
            <span style={styles.statValue}>{data.stats.total_edges}</span>
          </div>
          <div style={styles.statItem}>
            <span>Max Depth</span>
            <span style={styles.statValue}>{treeData?.maxDepth ?? 0}</span>
          </div>
          <div style={styles.statItem}>
            <span>Current Depth</span>
            <span style={styles.statValue}>{currentDepth}</span>
          </div>
          <div style={styles.statItem}>
            <span>Leaf Functions</span>
            <span style={styles.statValue}>{treeData?.leaves.length ?? 0}</span>
          </div>
        </div>
      </div>

      {/* Most Called */}
      <div style={styles.section}>
        <h3 style={styles.sectionTitle}>Most Called</h3>
        <div style={styles.funcList}>
          {data.stats.most_called.slice(0, 5).map(([name, count]) => (
            <div key={name} style={styles.funcItem}>
              <span style={styles.funcName}>{name.replace('$', '')}</span>
              <span style={styles.funcCount}>{count}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Instructions */}
      <div style={styles.section}>
        <h3 style={styles.sectionTitle}>How to Use</h3>
        <ol style={styles.instructions}>
          <li>Start with Depth 0 (leaves)</li>
          <li>Analyze simple functions first</li>
          <li>Mark as analyzed when understood</li>
          <li>Move up to higher depths</li>
          <li>Use context from callees</li>
        </ol>
      </div>
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  sidebar: {
    width: '280px',
    height: '100%',
    background: '#161b22',
    borderRight: '1px solid #30363d',
    display: 'flex',
    flexDirection: 'column',
    overflow: 'hidden',
  },
  header: {
    padding: '1rem',
    borderBottom: '1px solid #30363d',
  },
  title: {
    fontSize: '18px',
    fontWeight: 600,
    color: '#c9d1d9',
    margin: 0,
  },
  subtitle: {
    fontSize: '12px',
    color: '#8b949e',
    margin: '4px 0 0 0',
  },
  section: {
    padding: '1rem',
    borderBottom: '1px solid #30363d',
  },
  sectionTitle: {
    fontSize: '12px',
    fontWeight: 600,
    color: '#8b949e',
    textTransform: 'uppercase',
    marginBottom: '8px',
  },
  searchInput: {
    width: '100%',
    padding: '8px 12px',
    background: '#0d1117',
    border: '1px solid #30363d',
    borderRadius: '6px',
    color: '#c9d1d9',
    fontSize: '13px',
    outline: 'none',
  },
  viewModes: {
    display: 'flex',
    gap: '4px',
  },
  viewModeBtn: {
    flex: 1,
    padding: '8px',
    background: '#21262d',
    border: '1px solid #30363d',
    borderRadius: '6px',
    color: '#8b949e',
    fontSize: '11px',
    cursor: 'pointer',
    textTransform: 'capitalize',
  },
  viewModeBtnActive: {
    background: '#388bfd20',
    borderColor: '#388bfd',
    color: '#58a6ff',
  },
  progressContainer: {
    marginBottom: '8px',
  },
  progressBar: {
    height: '8px',
    background: '#21262d',
    borderRadius: '4px',
    overflow: 'hidden',
    marginBottom: '4px',
  },
  progressFill: {
    height: '100%',
    background: '#238636',
    transition: 'width 0.3s ease',
  },
  progressText: {
    fontSize: '11px',
    color: '#8b949e',
    textAlign: 'center',
  },
  clearBtn: {
    width: '100%',
    padding: '6px',
    background: '#21262d',
    border: '1px solid #30363d',
    borderRadius: '4px',
    color: '#f85149',
    fontSize: '11px',
    cursor: 'pointer',
    marginTop: '8px',
  },
  statsList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '6px',
  },
  statItem: {
    display: 'flex',
    justifyContent: 'space-between',
    fontSize: '12px',
    color: '#8b949e',
  },
  statValue: {
    color: '#c9d1d9',
    fontWeight: 500,
  },
  funcList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '4px',
  },
  funcItem: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '4px 8px',
    background: '#21262d',
    borderRadius: '4px',
    fontSize: '11px',
  },
  funcName: {
    fontFamily: 'monospace',
    color: '#c9d1d9',
    overflow: 'hidden',
    textOverflow: 'ellipsis',
    whiteSpace: 'nowrap',
    maxWidth: '180px',
  },
  funcCount: {
    color: '#8b949e',
    fontSize: '10px',
  },
  instructions: {
    fontSize: '11px',
    color: '#8b949e',
    paddingLeft: '16px',
    margin: 0,
    lineHeight: 1.6,
  },
};
