//! Output module - Generate various output formats

use serde::Serialize;
use std::path::Path;
use anyhow::Result;

use crate::sections::Module;
use crate::callgraph::CallGraph;
use crate::symbols::SymbolTable;

/// Output generator for various formats
pub struct OutputGenerator {
    output_dir: std::path::PathBuf,
}

impl OutputGenerator {
    pub fn new(output_dir: &Path) -> Self {
        Self {
            output_dir: output_dir.to_path_buf(),
        }
    }

    /// Generate all outputs
    pub fn generate_all(&self, module: &Module) -> Result<()> {
        std::fs::create_dir_all(&self.output_dir)?;

        // Generate index
        self.generate_index(module)?;

        // Generate call graph
        self.generate_callgraph(module)?;

        // Generate symbol table
        self.generate_symbols(module)?;

        // Generate summary
        self.generate_summary(module)?;

        Ok(())
    }

    fn generate_index(&self, module: &Module) -> Result<()> {
        let path = self.output_dir.join("index.json");
        module.save_index(&path)?;
        Ok(())
    }

    fn generate_callgraph(&self, module: &Module) -> Result<()> {
        let callgraph = CallGraph::build(module);

        // JSON
        let json_path = self.output_dir.join("graphs/callgraph.json");
        std::fs::create_dir_all(json_path.parent().unwrap())?;
        callgraph.save_json(&json_path)?;

        // DOT
        let dot_path = self.output_dir.join("graphs/callgraph.dot");
        std::fs::write(&dot_path, callgraph.to_dot())?;

        Ok(())
    }

    fn generate_symbols(&self, module: &Module) -> Result<()> {
        let symbols = SymbolTable::analyze(module);
        let path = self.output_dir.join("symbols.json");
        symbols.save(&path)?;
        Ok(())
    }

    fn generate_summary(&self, module: &Module) -> Result<()> {
        let stats = module.stats();
        let summary = Summary {
            module_stats: stats,
            memory: module.memory_size,
            table_size: module.table_size,
            exported_functions: module.exports.iter().map(|e| e.name.clone()).collect(),
            import_modules: module.imports.iter().map(|i| i.module.clone()).collect::<std::collections::HashSet<_>>().into_iter().collect(),
        };

        let path = self.output_dir.join("summary.json");
        let json = serde_json::to_string_pretty(&summary)?;
        std::fs::write(&path, json)?;

        Ok(())
    }
}

#[derive(Serialize)]
struct Summary {
    module_stats: crate::sections::ModuleStats,
    memory: Option<(u32, u32)>,
    table_size: Option<u32>,
    exported_functions: Vec<String>,
    import_modules: Vec<String>,
}

/// Generate a reconstructed module with better organization
pub struct ModuleReconstructor;

impl ModuleReconstructor {
    /// Reconstruct module with organized structure
    pub fn reconstruct(module: &Module, symbols: &SymbolTable, output_dir: &Path) -> Result<()> {
        std::fs::create_dir_all(output_dir)?;

        // Group functions by category
        let mut by_category: std::collections::HashMap<String, Vec<&crate::sections::Function>> =
            std::collections::HashMap::new();

        for func in &module.functions {
            let category = symbols.symbols.get(&func.name)
                .map(|s| format!("{:?}", s.category))
                .unwrap_or_else(|| "Unknown".to_string());

            by_category.entry(category).or_default().push(func);
        }

        // Write each category to its own file
        for (category, funcs) in &by_category {
            let filename = format!("{}.wat", category.to_lowercase());
            let path = output_dir.join(&filename);

            let mut content = format!(";; {} functions\n;; Count: {}\n\n", category, funcs.len());

            for func in funcs {
                let suggested = symbols.get_suggested(&func.name).unwrap_or(&func.name);
                content.push_str(&format!(";; Original: {} -> Suggested: {}\n", func.name, suggested));
                content.push_str(&func.body);
                content.push_str("\n\n");
            }

            std::fs::write(&path, content)?;
        }

        // Write category index
        let index: Vec<_> = by_category.iter()
            .map(|(cat, funcs)| {
                serde_json::json!({
                    "category": cat,
                    "count": funcs.len(),
                    "file": format!("{}.wat", cat.to_lowercase()),
                    "functions": funcs.iter().map(|f| &f.name).collect::<Vec<_>>(),
                })
            })
            .collect();

        let index_path = output_dir.join("_categories.json");
        std::fs::write(&index_path, serde_json::to_string_pretty(&index)?)?;

        Ok(())
    }
}
