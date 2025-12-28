//! Call Graph - Build and analyze function call relationships

use petgraph::graph::{DiGraph, NodeIndex};
use petgraph::algo::{dominators, tarjan_scc};
use petgraph::visit::Dfs;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::path::Path;
use anyhow::Result;

use crate::sections::Module;

/// Call graph representation
pub struct CallGraph {
    graph: DiGraph<String, ()>,
    node_map: HashMap<String, NodeIndex>,
}

/// Serializable call graph for JSON export
#[derive(Debug, Serialize, Deserialize)]
pub struct CallGraphJson {
    pub nodes: Vec<NodeJson>,
    pub edges: Vec<EdgeJson>,
    pub stats: CallGraphStats,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct NodeJson {
    pub id: String,
    pub name: String,
    pub index: usize,
    pub is_import: bool,
    pub is_export: bool,
    pub in_degree: usize,
    pub out_degree: usize,
    pub category: Option<String>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct EdgeJson {
    pub source: String,
    pub target: String,
}

#[derive(Debug, Default, Serialize, Deserialize)]
pub struct CallGraphStats {
    pub total_nodes: usize,
    pub total_edges: usize,
    pub entry_points: Vec<String>,
    pub leaf_functions: Vec<String>,
    pub most_called: Vec<(String, usize)>,
    pub largest_callers: Vec<(String, usize)>,
    pub scc_count: usize,
    pub max_depth: usize,
}

impl CallGraph {
    /// Build call graph from module
    pub fn build(module: &Module) -> Self {
        let mut graph = DiGraph::new();
        let mut node_map = HashMap::new();

        // First pass: create all nodes
        for func in &module.functions {
            let idx = graph.add_node(func.name.clone());
            node_map.insert(func.name.clone(), idx);
        }

        // Second pass: add edges
        for func in &module.functions {
            if let Some(&caller_idx) = node_map.get(&func.name) {
                for called in &func.calls {
                    if let Some(&callee_idx) = node_map.get(called) {
                        graph.add_edge(caller_idx, callee_idx, ());
                    }
                }
            }
        }

        Self { graph, node_map }
    }

    /// Get entry points (functions with no callers, excluding imports)
    pub fn entry_points(&self) -> Vec<&str> {
        self.node_map.iter()
            .filter(|(name, &idx)| {
                self.graph.neighbors_directed(idx, petgraph::Direction::Incoming).count() == 0
                    && !name.contains(".")  // Skip imports like $a.b
            })
            .map(|(name, _)| name.as_str())
            .collect()
    }

    /// Get leaf functions (functions that don't call others)
    pub fn leaf_functions(&self) -> Vec<&str> {
        self.node_map.iter()
            .filter(|(_, &idx)| {
                self.graph.neighbors_directed(idx, petgraph::Direction::Outgoing).count() == 0
            })
            .map(|(name, _)| name.as_str())
            .collect()
    }

    /// Get most called functions
    pub fn most_called(&self, limit: usize) -> Vec<(&str, usize)> {
        let mut counts: Vec<_> = self.node_map.iter()
            .map(|(name, &idx)| {
                let count = self.graph.neighbors_directed(idx, petgraph::Direction::Incoming).count();
                (name.as_str(), count)
            })
            .collect();

        counts.sort_by(|a, b| b.1.cmp(&a.1));
        counts.truncate(limit);
        counts
    }

    /// Get functions that call the most others
    pub fn largest_callers(&self, limit: usize) -> Vec<(&str, usize)> {
        let mut counts: Vec<_> = self.node_map.iter()
            .map(|(name, &idx)| {
                let count = self.graph.neighbors_directed(idx, petgraph::Direction::Outgoing).count();
                (name.as_str(), count)
            })
            .collect();

        counts.sort_by(|a, b| b.1.cmp(&a.1));
        counts.truncate(limit);
        counts
    }

    /// Get all callers of a function
    pub fn callers_of(&self, name: &str) -> Vec<&str> {
        self.node_map.get(name)
            .map(|&idx| {
                self.graph.neighbors_directed(idx, petgraph::Direction::Incoming)
                    .filter_map(|caller_idx| self.graph.node_weight(caller_idx).map(|s| s.as_str()))
                    .collect()
            })
            .unwrap_or_default()
    }

    /// Get all functions called by a function
    pub fn callees_of(&self, name: &str) -> Vec<&str> {
        self.node_map.get(name)
            .map(|&idx| {
                self.graph.neighbors_directed(idx, petgraph::Direction::Outgoing)
                    .filter_map(|callee_idx| self.graph.node_weight(callee_idx).map(|s| s.as_str()))
                    .collect()
            })
            .unwrap_or_default()
    }

    /// Find strongly connected components (potential loops/recursion)
    pub fn find_scc(&self) -> Vec<Vec<&str>> {
        tarjan_scc(&self.graph)
            .into_iter()
            .filter(|scc| scc.len() > 1)  // Only keep non-trivial SCCs
            .map(|scc| {
                scc.into_iter()
                    .filter_map(|idx| self.graph.node_weight(idx).map(|s| s.as_str()))
                    .collect()
            })
            .collect()
    }

    /// Calculate max call depth from entry points
    pub fn max_depth(&self) -> usize {
        let entry_points = self.entry_points();
        let mut max_depth = 0;

        for entry in entry_points {
            if let Some(&start_idx) = self.node_map.get(entry) {
                let depth = self.calculate_depth(start_idx, &mut HashMap::new());
                max_depth = max_depth.max(depth);
            }
        }

        max_depth
    }

    fn calculate_depth(&self, idx: NodeIndex, memo: &mut HashMap<NodeIndex, usize>) -> usize {
        if let Some(&cached) = memo.get(&idx) {
            return cached;
        }

        let callees: Vec<_> = self.graph.neighbors_directed(idx, petgraph::Direction::Outgoing).collect();

        if callees.is_empty() {
            memo.insert(idx, 1);
            return 1;
        }

        // Prevent infinite recursion
        memo.insert(idx, 0);

        let max_child = callees.iter()
            .map(|&child_idx| self.calculate_depth(child_idx, memo))
            .max()
            .unwrap_or(0);

        let depth = 1 + max_child;
        memo.insert(idx, depth);
        depth
    }

    /// Export to JSON
    pub fn to_json(&self, module: &Module) -> CallGraphJson {
        let func_map: HashMap<_, _> = module.functions.iter()
            .map(|f| (f.name.clone(), f))
            .collect();

        let nodes: Vec<NodeJson> = self.node_map.iter()
            .map(|(name, &idx)| {
                let func = func_map.get(name);
                NodeJson {
                    id: name.clone(),
                    name: name.clone(),
                    index: func.map(|f| f.index).unwrap_or(0),
                    is_import: func.map(|f| f.is_import).unwrap_or(false),
                    is_export: func.map(|f| f.is_export).unwrap_or(false),
                    in_degree: self.graph.neighbors_directed(idx, petgraph::Direction::Incoming).count(),
                    out_degree: self.graph.neighbors_directed(idx, petgraph::Direction::Outgoing).count(),
                    category: func.and_then(|f| f.category.as_ref().map(|c| format!("{:?}", c))),
                }
            })
            .collect();

        let edges: Vec<EdgeJson> = self.graph.edge_indices()
            .filter_map(|edge_idx| {
                let (source, target) = self.graph.edge_endpoints(edge_idx)?;
                Some(EdgeJson {
                    source: self.graph.node_weight(source)?.clone(),
                    target: self.graph.node_weight(target)?.clone(),
                })
            })
            .collect();

        let stats = CallGraphStats {
            total_nodes: self.node_map.len(),
            total_edges: self.graph.edge_count(),
            entry_points: self.entry_points().iter().map(|s| s.to_string()).collect(),
            leaf_functions: self.leaf_functions().iter().take(20).map(|s| s.to_string()).collect(),
            most_called: self.most_called(10).iter().map(|(s, c)| (s.to_string(), *c)).collect(),
            largest_callers: self.largest_callers(10).iter().map(|(s, c)| (s.to_string(), *c)).collect(),
            scc_count: self.find_scc().len(),
            max_depth: self.max_depth(),
        };

        CallGraphJson { nodes, edges, stats }
    }

    /// Save to JSON file
    pub fn save_json(&self, path: &Path) -> Result<()> {
        // Need module for full export, use minimal version
        let nodes: Vec<NodeJson> = self.node_map.iter()
            .map(|(name, &idx)| NodeJson {
                id: name.clone(),
                name: name.clone(),
                index: 0,
                is_import: name.contains("."),
                is_export: false,
                in_degree: self.graph.neighbors_directed(idx, petgraph::Direction::Incoming).count(),
                out_degree: self.graph.neighbors_directed(idx, petgraph::Direction::Outgoing).count(),
                category: None,
            })
            .collect();

        let edges: Vec<EdgeJson> = self.graph.edge_indices()
            .filter_map(|edge_idx| {
                let (source, target) = self.graph.edge_endpoints(edge_idx)?;
                Some(EdgeJson {
                    source: self.graph.node_weight(source)?.clone(),
                    target: self.graph.node_weight(target)?.clone(),
                })
            })
            .collect();

        let stats = CallGraphStats {
            total_nodes: self.node_map.len(),
            total_edges: self.graph.edge_count(),
            entry_points: self.entry_points().iter().map(|s| s.to_string()).collect(),
            leaf_functions: self.leaf_functions().iter().take(20).map(|s| s.to_string()).collect(),
            most_called: self.most_called(10).iter().map(|(s, c)| (s.to_string(), *c)).collect(),
            largest_callers: self.largest_callers(10).iter().map(|(s, c)| (s.to_string(), *c)).collect(),
            scc_count: self.find_scc().len(),
            max_depth: 0, // Skip expensive calculation
        };

        let json_graph = CallGraphJson { nodes, edges, stats };

        std::fs::create_dir_all(path.parent().unwrap_or(Path::new(".")))?;
        let json = serde_json::to_string_pretty(&json_graph)?;
        std::fs::write(path, json)?;

        Ok(())
    }

    /// Export to DOT format for Graphviz
    pub fn to_dot(&self) -> String {
        let mut dot = String::from("digraph CallGraph {\n");
        dot.push_str("  rankdir=LR;\n");
        dot.push_str("  node [shape=box];\n\n");

        for (name, &idx) in &self.node_map {
            let in_degree = self.graph.neighbors_directed(idx, petgraph::Direction::Incoming).count();
            let out_degree = self.graph.neighbors_directed(idx, petgraph::Direction::Outgoing).count();

            let color = if name.contains(".") {
                "lightblue"  // Import
            } else if in_degree == 0 {
                "lightgreen"  // Entry point
            } else if out_degree == 0 {
                "lightyellow"  // Leaf
            } else {
                "white"
            };

            let label = name.replace("$", "").replace(".", "_");
            dot.push_str(&format!("  \"{}\" [label=\"{}\" fillcolor=\"{}\" style=filled];\n",
                name, label, color));
        }

        dot.push_str("\n");

        for edge_idx in self.graph.edge_indices() {
            if let Some((source, target)) = self.graph.edge_endpoints(edge_idx) {
                if let (Some(src), Some(tgt)) = (
                    self.graph.node_weight(source),
                    self.graph.node_weight(target)
                ) {
                    dot.push_str(&format!("  \"{}\" -> \"{}\";\n", src, tgt));
                }
            }
        }

        dot.push_str("}\n");
        dot
    }
}
