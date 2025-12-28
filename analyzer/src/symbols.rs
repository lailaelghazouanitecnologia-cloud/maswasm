//! Symbol Table - RTS-aware symbol naming and categorization

use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::path::Path;
use anyhow::Result;

use crate::sections::{Module, Function, FunctionCategory};
use crate::patterns::PatternMatcher;

/// Symbol table with suggested names
#[derive(Debug, Default, Serialize, Deserialize)]
pub struct SymbolTable {
    pub symbols: HashMap<String, Symbol>,
    pub categories: HashMap<FunctionCategory, Vec<String>>,
    pub stats: SymbolStats,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Symbol {
    pub original_name: String,
    pub suggested_name: String,
    pub category: FunctionCategory,
    pub confidence: f32,
    pub reasons: Vec<String>,
}

#[derive(Debug, Default, Serialize, Deserialize)]
pub struct SymbolStats {
    pub total_symbols: usize,
    pub named_symbols: usize,
    pub high_confidence: usize,  // > 0.8
    pub medium_confidence: usize, // 0.5 - 0.8
    pub low_confidence: usize,   // < 0.5
}

impl SymbolTable {
    /// Analyze module and generate symbol suggestions
    pub fn analyze(module: &Module) -> Self {
        let matcher = PatternMatcher::new();
        let mut table = SymbolTable::default();

        for func in &module.functions {
            let (suggested, category, confidence, reasons) = matcher.analyze_function(func);

            let symbol = Symbol {
                original_name: func.name.clone(),
                suggested_name: suggested.clone(),
                category: category.clone(),
                confidence,
                reasons,
            };

            table.symbols.insert(func.name.clone(), symbol);

            // Group by category
            table.categories
                .entry(category)
                .or_default()
                .push(func.name.clone());
        }

        // Calculate stats
        table.stats.total_symbols = table.symbols.len();
        table.stats.named_symbols = table.symbols.values()
            .filter(|s| s.suggested_name != s.original_name)
            .count();
        table.stats.high_confidence = table.symbols.values()
            .filter(|s| s.confidence > 0.8)
            .count();
        table.stats.medium_confidence = table.symbols.values()
            .filter(|s| s.confidence > 0.5 && s.confidence <= 0.8)
            .count();
        table.stats.low_confidence = table.symbols.values()
            .filter(|s| s.confidence <= 0.5)
            .count();

        table
    }

    /// Save symbol table to JSON
    pub fn save(&self, path: &Path) -> Result<()> {
        std::fs::create_dir_all(path.parent().unwrap_or(Path::new(".")))?;
        let json = serde_json::to_string_pretty(self)?;
        std::fs::write(path, json)?;
        Ok(())
    }

    /// Load symbol table from JSON
    pub fn load(path: &Path) -> Result<Self> {
        let json = std::fs::read_to_string(path)?;
        let table: SymbolTable = serde_json::from_str(&json)?;
        Ok(table)
    }

    /// Get suggested name for original name
    pub fn get_suggested(&self, original: &str) -> Option<&str> {
        self.symbols.get(original).map(|s| s.suggested_name.as_str())
    }

    /// Get all symbols in a category
    pub fn get_by_category(&self, category: &FunctionCategory) -> Vec<&Symbol> {
        self.categories.get(category)
            .map(|names| {
                names.iter()
                    .filter_map(|n| self.symbols.get(n))
                    .collect()
            })
            .unwrap_or_default()
    }

    /// Export as rename mapping (original -> suggested)
    pub fn export_rename_map(&self) -> HashMap<String, String> {
        self.symbols.iter()
            .filter(|(_, s)| s.suggested_name != s.original_name)
            .map(|(k, s)| (k.clone(), s.suggested_name.clone()))
            .collect()
    }
}

/// RTS-specific naming conventions
pub struct RtsNamer;

impl RtsNamer {
    /// Generate a descriptive name based on category and hints
    pub fn generate_name(
        category: &FunctionCategory,
        hints: &[&str],
        index: usize,
    ) -> String {
        let prefix = match category {
            FunctionCategory::GameLoop => "Game",
            FunctionCategory::Init => "Init",
            FunctionCategory::Update => "Update",
            FunctionCategory::Render => "Render",
            FunctionCategory::Unit => "Unit",
            FunctionCategory::Building => "Building",
            FunctionCategory::Resource => "Resource",
            FunctionCategory::Terrain => "Terrain",
            FunctionCategory::Pathfinding => "Path",
            FunctionCategory::AI => "AI",
            FunctionCategory::Combat => "Combat",
            FunctionCategory::Input => "Input",
            FunctionCategory::Audio => "Audio",
            FunctionCategory::Network => "Net",
            FunctionCategory::UI => "UI",
            FunctionCategory::WebP => "WebP",
            FunctionCategory::Sprite => "Sprite",
            FunctionCategory::Animation => "Anim",
            FunctionCategory::Memory => "Mem",
            FunctionCategory::Math => "Math",
            FunctionCategory::String => "Str",
            FunctionCategory::Unknown => "Func",
        };

        if hints.is_empty() {
            format!("{}_{}", prefix, index)
        } else {
            let hint = hints[0]
                .chars()
                .filter(|c| c.is_alphanumeric())
                .collect::<String>();
            format!("{}_{}", prefix, hint)
        }
    }
}
