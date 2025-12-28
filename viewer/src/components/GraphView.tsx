import React, { useCallback, useRef, useEffect, useState } from 'react';
import ForceGraph2D, { ForceGraphMethods } from 'react-force-graph-2d';
import { GraphData, GraphNode } from '../types';
import { useStore } from '../hooks/useStore';
import { useTreeStructure } from '../hooks/useGraphData';

interface Props {
  data: GraphData;
}

export function GraphView({ data }: Props) {
  const graphRef = useRef<ForceGraphMethods>();
  const containerRef = useRef<HTMLDivElement>(null);
  const [dimensions, setDimensions] = useState({ width: 800, height: 600 });

  const {
    selectedNode,
    setSelectedNode,
    analyzedNodes,
    currentDepth,
    searchFilter,
  } = useStore();

  const treeData = useTreeStructure(data);

  // Handle resize
  useEffect(() => {
    const updateDimensions = () => {
      if (containerRef.current) {
        setDimensions({
          width: containerRef.current.clientWidth,
          height: containerRef.current.clientHeight,
        });
      }
    };

    updateDimensions();
    window.addEventListener('resize', updateDimensions);
    return () => window.removeEventListener('resize', updateDimensions);
  }, []);

  // Prepare graph data with depth info
  const graphData = React.useMemo(() => {
    if (!treeData) return data;

    const nodes = data.nodes.map(node => ({
      ...node,
      depth: treeData.depths.get(node.id) ?? 0,
    }));

    // Filter if searching
    let filteredNodes = nodes;
    if (searchFilter) {
      const lowerFilter = searchFilter.toLowerCase();
      const matchingIds = new Set(
        nodes
          .filter(n => n.name.toLowerCase().includes(lowerFilter))
          .map(n => n.id)
      );

      // Include connected nodes
      for (const link of data.links) {
        if (matchingIds.has(link.source as string) || matchingIds.has(link.target as string)) {
          matchingIds.add(link.source as string);
          matchingIds.add(link.target as string);
        }
      }

      filteredNodes = nodes.filter(n => matchingIds.has(n.id));
    }

    const filteredIds = new Set(filteredNodes.map(n => n.id));
    const links = data.links.filter(
      l => filteredIds.has(l.source as string) && filteredIds.has(l.target as string)
    );

    return { nodes: filteredNodes, links };
  }, [data, treeData, searchFilter]);

  const handleNodeClick = useCallback((node: any) => {
    setSelectedNode(node as GraphNode);

    // Center on node
    if (graphRef.current) {
      graphRef.current.centerAt(node.x, node.y, 500);
      graphRef.current.zoom(2, 500);
    }
  }, [setSelectedNode]);

  const getNodeColor = useCallback((node: any) => {
    const n = node as GraphNode & { depth?: number };

    if (selectedNode?.id === n.id) return '#388bfd';
    if (analyzedNodes.has(n.id)) return '#238636';
    if (n.isImport) return '#8b949e';
    if (n.isExport) return '#f0883e';

    // Color by depth
    const depth = n.depth ?? 0;
    const maxDepth = treeData?.maxDepth ?? 10;
    const hue = (depth / maxDepth) * 200 + 160; // Green to purple
    return `hsl(${hue}, 70%, 50%)`;
  }, [selectedNode, analyzedNodes, treeData]);

  const getNodeSize = useCallback((node: any) => {
    const n = node as GraphNode;

    // Larger if selected or at current depth
    if (selectedNode?.id === n.id) return 12;

    const depth = (n as any).depth ?? 0;
    if (depth === currentDepth) return 8;

    return 4 + Math.min(n.inDegree, 10);
  }, [selectedNode, currentDepth]);

  const getLinkColor = useCallback((link: any) => {
    const sourceId = typeof link.source === 'object' ? link.source.id : link.source;
    const targetId = typeof link.target === 'object' ? link.target.id : link.target;

    if (selectedNode?.id === sourceId || selectedNode?.id === targetId) {
      return '#388bfd80';
    }
    return '#30363d40';
  }, [selectedNode]);

  return (
    <div ref={containerRef} style={styles.container}>
      <ForceGraph2D
        ref={graphRef}
        graphData={graphData}
        width={dimensions.width}
        height={dimensions.height}
        nodeColor={getNodeColor}
        nodeVal={getNodeSize}
        linkColor={getLinkColor}
        linkDirectionalArrowLength={3}
        linkDirectionalArrowRelPos={1}
        onNodeClick={handleNodeClick}
        nodeLabel={(node: any) => `${node.name}\nDepth: ${node.depth ?? 0}`}
        cooldownTicks={100}
        d3AlphaDecay={0.02}
        d3VelocityDecay={0.3}
      />

      {/* Legend */}
      <div style={styles.legend}>
        <div style={styles.legendItem}>
          <span style={{ ...styles.dot, background: '#238636' }} /> Analyzed
        </div>
        <div style={styles.legendItem}>
          <span style={{ ...styles.dot, background: '#f0883e' }} /> Export
        </div>
        <div style={styles.legendItem}>
          <span style={{ ...styles.dot, background: '#8b949e' }} /> Import
        </div>
        <div style={styles.legendItem}>
          <span style={{ ...styles.dot, background: '#388bfd' }} /> Selected
        </div>
      </div>

      {/* Stats */}
      <div style={styles.stats}>
        <div>Nodes: {graphData.nodes.length}</div>
        <div>Edges: {graphData.links.length}</div>
      </div>
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  container: {
    width: '100%',
    height: '100%',
    background: '#0d1117',
    position: 'relative',
  },
  legend: {
    position: 'absolute',
    top: '1rem',
    left: '1rem',
    background: '#161b2290',
    padding: '8px 12px',
    borderRadius: '6px',
    display: 'flex',
    gap: '16px',
    fontSize: '11px',
    color: '#8b949e',
  },
  legendItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '6px',
  },
  dot: {
    width: '10px',
    height: '10px',
    borderRadius: '50%',
    display: 'inline-block',
  },
  stats: {
    position: 'absolute',
    bottom: '1rem',
    left: '1rem',
    background: '#161b2290',
    padding: '8px 12px',
    borderRadius: '6px',
    fontSize: '11px',
    color: '#8b949e',
    display: 'flex',
    gap: '16px',
  },
};
