import React, { useCallback } from 'react';
import { useGraphData, useTreeStructure } from './hooks/useGraphData';
import { useStore } from './hooks/useStore';
import { Sidebar } from './components/Sidebar';
import { HierarchyView } from './components/HierarchyView';
import { GraphView } from './components/GraphView';
import { DetailPanel } from './components/DetailPanel';

function App() {
  const { data, loading, error, setData } = useGraphData();
  const treeData = useTreeStructure(data);
  const { viewMode, selectedNode, showSidebar, showDetails } = useStore();

  // Handle file drop for loading data
  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    if (file && file.name.endsWith('.json')) {
      const reader = new FileReader();
      reader.onload = (event) => {
        try {
          const json = JSON.parse(event.target?.result as string);
          setData(json);
        } catch (err) {
          console.error('Failed to parse JSON:', err);
        }
      };
      reader.readAsText(file);
    }
  }, [setData]);

  const handleDragOver = useCallback((e: React.DragEvent) => {
    e.preventDefault();
  }, []);

  // Get callers/callees for selected node
  const callers = selectedNode && treeData?.callers.get(selectedNode.id);
  const callees = selectedNode && treeData?.callees.get(selectedNode.id);

  if (loading) {
    return (
      <div style={styles.loading}>
        <div style={styles.spinner} />
        <p>Loading analysis data...</p>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div
        style={styles.dropZone}
        onDrop={handleDrop}
        onDragOver={handleDragOver}
      >
        <div style={styles.dropContent}>
          <h1 style={styles.dropTitle}>⚔️ Tzar WASM Analyzer</h1>
          <p style={styles.dropText}>
            Drag and drop a callgraph-react.json file here
          </p>
          <p style={styles.dropHint}>
            Generate it with: python tools/build_callgraph.py mgame
          </p>
          {error && <p style={styles.error}>{error}</p>}
        </div>
      </div>
    );
  }

  return (
    <div
      style={styles.container}
      onDrop={handleDrop}
      onDragOver={handleDragOver}
    >
      {showSidebar && <Sidebar data={data} />}

      <main style={styles.main}>
        {viewMode === 'hierarchy' && <HierarchyView data={data} />}
        {viewMode === 'graph' && <GraphView data={data} />}
        {viewMode === 'list' && <ListView data={data} />}
      </main>

      {showDetails && (
        <DetailPanel
          node={selectedNode}
          callers={callers}
          callees={callees}
        />
      )}
    </div>
  );
}

// Simple list view for all functions
function ListView({ data }: { data: any }) {
  const { searchFilter, analyzedNodes, setSelectedNode } = useStore();
  const treeData = useTreeStructure(data);

  const filteredNodes = React.useMemo(() => {
    let nodes = data.nodes.map((n: any) => ({
      ...n,
      depth: treeData?.depths.get(n.id) ?? 0,
    }));

    if (searchFilter) {
      const lowerFilter = searchFilter.toLowerCase();
      nodes = nodes.filter((n: any) =>
        n.name.toLowerCase().includes(lowerFilter)
      );
    }

    return nodes.sort((a: any, b: any) => a.depth - b.depth);
  }, [data, treeData, searchFilter]);

  return (
    <div style={styles.listView}>
      <table style={styles.table}>
        <thead>
          <tr>
            <th style={styles.th}>Depth</th>
            <th style={styles.th}>Name</th>
            <th style={styles.th}>In</th>
            <th style={styles.th}>Out</th>
            <th style={styles.th}>Status</th>
          </tr>
        </thead>
        <tbody>
          {filteredNodes.map((node: any) => (
            <tr
              key={node.id}
              style={styles.tr}
              onClick={() => setSelectedNode(node)}
            >
              <td style={styles.td}>{node.depth}</td>
              <td style={{ ...styles.td, ...styles.funcName }}>
                {node.name}
                {node.isImport && <span style={styles.badge}>I</span>}
                {node.isExport && <span style={styles.badgeE}>E</span>}
              </td>
              <td style={styles.td}>{node.inDegree}</td>
              <td style={styles.td}>{node.outDegree}</td>
              <td style={styles.td}>
                {analyzedNodes.has(node.id) ? '✓' : '-'}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  container: {
    display: 'flex',
    width: '100vw',
    height: '100vh',
    overflow: 'hidden',
    background: '#0d1117',
  },
  main: {
    flex: 1,
    overflow: 'hidden',
  },
  loading: {
    width: '100vw',
    height: '100vh',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    background: '#0d1117',
    color: '#8b949e',
    gap: '1rem',
  },
  spinner: {
    width: '40px',
    height: '40px',
    border: '3px solid #30363d',
    borderTopColor: '#388bfd',
    borderRadius: '50%',
    animation: 'spin 1s linear infinite',
  },
  dropZone: {
    width: '100vw',
    height: '100vh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    background: '#0d1117',
  },
  dropContent: {
    textAlign: 'center',
    padding: '3rem',
    border: '2px dashed #30363d',
    borderRadius: '12px',
    maxWidth: '500px',
  },
  dropTitle: {
    fontSize: '28px',
    color: '#c9d1d9',
    marginBottom: '1rem',
  },
  dropText: {
    fontSize: '16px',
    color: '#8b949e',
    marginBottom: '0.5rem',
  },
  dropHint: {
    fontSize: '12px',
    color: '#6e7681',
    fontFamily: 'monospace',
  },
  error: {
    color: '#f85149',
    fontSize: '14px',
    marginTop: '1rem',
  },
  listView: {
    height: '100%',
    overflow: 'auto',
    padding: '1rem',
  },
  table: {
    width: '100%',
    borderCollapse: 'collapse',
    fontSize: '12px',
  },
  th: {
    textAlign: 'left',
    padding: '8px 12px',
    background: '#161b22',
    color: '#8b949e',
    fontWeight: 600,
    borderBottom: '1px solid #30363d',
    position: 'sticky',
    top: 0,
  },
  tr: {
    cursor: 'pointer',
    transition: 'background 0.1s',
  },
  td: {
    padding: '6px 12px',
    borderBottom: '1px solid #21262d',
    color: '#c9d1d9',
  },
  funcName: {
    fontFamily: 'monospace',
    display: 'flex',
    alignItems: 'center',
    gap: '6px',
  },
  badge: {
    fontSize: '9px',
    padding: '1px 4px',
    borderRadius: '3px',
    background: '#1f6feb30',
    color: '#58a6ff',
  },
  badgeE: {
    fontSize: '9px',
    padding: '1px 4px',
    borderRadius: '3px',
    background: '#23863630',
    color: '#3fb950',
  },
};

export default App;
