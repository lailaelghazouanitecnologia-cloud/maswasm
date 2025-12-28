import React, { useState } from 'react';
import { GraphNode } from '../types';
import { useStore } from '../hooks/useStore';

interface Props {
  node: GraphNode | null;
  callers?: Set<string>;
  callees?: Set<string>;
}

export function DetailPanel({ node, callers, callees }: Props) {
  const {
    analyzedNodes,
    markAnalyzed,
    markUnanalyzed,
    annotations,
    setAnnotation,
  } = useStore();

  const [notes, setNotes] = useState('');
  const [suggestedName, setSuggestedName] = useState('');
  const [category, setCategory] = useState('');

  const annotation = node ? annotations.get(node.id) : undefined;

  React.useEffect(() => {
    if (node && annotation) {
      setNotes(annotation.notes ?? '');
      setSuggestedName(annotation.suggestedName ?? '');
      setCategory(annotation.category ?? '');
    } else {
      setNotes('');
      setSuggestedName('');
      setCategory('');
    }
  }, [node, annotation]);

  if (!node) {
    return (
      <div style={styles.panel}>
        <div style={styles.empty}>
          <p>Select a function to view details</p>
        </div>
      </div>
    );
  }

  const isAnalyzed = analyzedNodes.has(node.id);

  const handleSave = () => {
    setAnnotation(node.id, {
      notes,
      suggestedName,
      category,
    });
    markAnalyzed(node.id);
  };

  return (
    <div style={styles.panel}>
      <div style={styles.header}>
        <h2 style={styles.title}>{node.name}</h2>
        <div style={styles.badges}>
          {node.isImport && <span style={styles.badge}>import</span>}
          {node.isExport && <span style={styles.badgeExport}>export</span>}
          {isAnalyzed && <span style={styles.badgeAnalyzed}>analyzed</span>}
        </div>
      </div>

      {/* Meta info */}
      <div style={styles.section}>
        <div style={styles.meta}>
          <div style={styles.metaItem}>
            <span>Index</span>
            <span style={styles.metaValue}>#{node.index ?? 0}</span>
          </div>
          <div style={styles.metaItem}>
            <span>Depth</span>
            <span style={styles.metaValue}>{node.depth ?? 0}</span>
          </div>
          <div style={styles.metaItem}>
            <span>In-degree</span>
            <span style={styles.metaValue}>{node.inDegree}</span>
          </div>
          <div style={styles.metaItem}>
            <span>Out-degree</span>
            <span style={styles.metaValue}>{node.outDegree}</span>
          </div>
        </div>
      </div>

      {/* Callees (functions this one calls) */}
      {callees && callees.size > 0 && (
        <div style={styles.section}>
          <h3 style={styles.sectionTitle}>
            Calls ({callees.size})
          </h3>
          <div style={styles.funcList}>
            {Array.from(callees).slice(0, 10).map((name) => (
              <div key={name} style={styles.funcItem}>
                {name.replace('$', '')}
              </div>
            ))}
            {callees.size > 10 && (
              <div style={styles.more}>+{callees.size - 10} more</div>
            )}
          </div>
        </div>
      )}

      {/* Callers (functions that call this one) */}
      {callers && callers.size > 0 && (
        <div style={styles.section}>
          <h3 style={styles.sectionTitle}>
            Called by ({callers.size})
          </h3>
          <div style={styles.funcList}>
            {Array.from(callers).slice(0, 10).map((name) => (
              <div key={name} style={styles.funcItem}>
                {name.replace('$', '')}
              </div>
            ))}
            {callers.size > 10 && (
              <div style={styles.more}>+{callers.size - 10} more</div>
            )}
          </div>
        </div>
      )}

      {/* Annotation form */}
      <div style={styles.section}>
        <h3 style={styles.sectionTitle}>Analysis</h3>

        <div style={styles.formGroup}>
          <label style={styles.label}>Suggested Name</label>
          <input
            type="text"
            value={suggestedName}
            onChange={(e) => setSuggestedName(e.target.value)}
            placeholder="e.g., Unit_Move"
            style={styles.input}
          />
        </div>

        <div style={styles.formGroup}>
          <label style={styles.label}>Category</label>
          <select
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            style={styles.select}
          >
            <option value="">Select...</option>
            <option value="Unit">Unit</option>
            <option value="Building">Building</option>
            <option value="Resource">Resource</option>
            <option value="Terrain">Terrain</option>
            <option value="Pathfinding">Pathfinding</option>
            <option value="AI">AI</option>
            <option value="Combat">Combat</option>
            <option value="Render">Render</option>
            <option value="WebP">WebP</option>
            <option value="Audio">Audio</option>
            <option value="Network">Network</option>
            <option value="UI">UI</option>
            <option value="Memory">Memory</option>
            <option value="Math">Math</option>
            <option value="Init">Init</option>
            <option value="Update">Update</option>
            <option value="Unknown">Unknown</option>
          </select>
        </div>

        <div style={styles.formGroup}>
          <label style={styles.label}>Notes</label>
          <textarea
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            placeholder="What does this function do?"
            style={styles.textarea}
            rows={4}
          />
        </div>

        <div style={styles.actions}>
          <button style={styles.saveBtn} onClick={handleSave}>
            {isAnalyzed ? 'Update' : 'Mark Analyzed'}
          </button>
          {isAnalyzed && (
            <button
              style={styles.unmarkBtn}
              onClick={() => markUnanalyzed(node.id)}
            >
              Unmark
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  panel: {
    width: '320px',
    height: '100%',
    background: '#161b22',
    borderLeft: '1px solid #30363d',
    display: 'flex',
    flexDirection: 'column',
    overflow: 'auto',
  },
  empty: {
    flex: 1,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    color: '#8b949e',
    fontSize: '13px',
  },
  header: {
    padding: '1rem',
    borderBottom: '1px solid #30363d',
  },
  title: {
    fontSize: '14px',
    fontWeight: 600,
    color: '#c9d1d9',
    fontFamily: 'monospace',
    margin: 0,
    wordBreak: 'break-all',
  },
  badges: {
    display: 'flex',
    gap: '6px',
    marginTop: '8px',
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
  section: {
    padding: '1rem',
    borderBottom: '1px solid #30363d',
  },
  sectionTitle: {
    fontSize: '11px',
    fontWeight: 600,
    color: '#8b949e',
    textTransform: 'uppercase',
    marginBottom: '8px',
  },
  meta: {
    display: 'grid',
    gridTemplateColumns: '1fr 1fr',
    gap: '8px',
  },
  metaItem: {
    display: 'flex',
    justifyContent: 'space-between',
    fontSize: '12px',
    color: '#8b949e',
    padding: '4px 8px',
    background: '#21262d',
    borderRadius: '4px',
  },
  metaValue: {
    color: '#c9d1d9',
    fontWeight: 500,
  },
  funcList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '4px',
  },
  funcItem: {
    padding: '4px 8px',
    background: '#21262d',
    borderRadius: '4px',
    fontSize: '11px',
    fontFamily: 'monospace',
    color: '#c9d1d9',
  },
  more: {
    fontSize: '11px',
    color: '#8b949e',
    textAlign: 'center',
    padding: '4px',
  },
  formGroup: {
    marginBottom: '12px',
  },
  label: {
    display: 'block',
    fontSize: '11px',
    color: '#8b949e',
    marginBottom: '4px',
  },
  input: {
    width: '100%',
    padding: '8px',
    background: '#0d1117',
    border: '1px solid #30363d',
    borderRadius: '4px',
    color: '#c9d1d9',
    fontSize: '12px',
    outline: 'none',
  },
  select: {
    width: '100%',
    padding: '8px',
    background: '#0d1117',
    border: '1px solid #30363d',
    borderRadius: '4px',
    color: '#c9d1d9',
    fontSize: '12px',
    outline: 'none',
  },
  textarea: {
    width: '100%',
    padding: '8px',
    background: '#0d1117',
    border: '1px solid #30363d',
    borderRadius: '4px',
    color: '#c9d1d9',
    fontSize: '12px',
    outline: 'none',
    resize: 'vertical',
    fontFamily: 'inherit',
  },
  actions: {
    display: 'flex',
    gap: '8px',
  },
  saveBtn: {
    flex: 1,
    padding: '8px',
    background: '#238636',
    border: 'none',
    borderRadius: '4px',
    color: '#fff',
    fontSize: '12px',
    fontWeight: 500,
    cursor: 'pointer',
  },
  unmarkBtn: {
    padding: '8px 12px',
    background: '#21262d',
    border: '1px solid #30363d',
    borderRadius: '4px',
    color: '#f85149',
    fontSize: '12px',
    cursor: 'pointer',
  },
};
