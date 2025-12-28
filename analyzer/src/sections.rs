//! Module sections - Data structures for WASM module components

use serde::{Deserialize, Serialize};
use std::path::Path;
use anyhow::Result;

/// Represents a parsed WASM module
#[derive(Debug, Default, Serialize, Deserialize)]
pub struct Module {
    pub functions: Vec<Function>,
    pub imports: Vec<Import>,
    pub exports: Vec<Export>,
    pub globals: Vec<Global>,
    pub data_sections: Vec<DataSection>,
    pub memory_size: Option<(u32, u32)>,
    pub table_size: Option<u32>,
    pub total_lines: usize,
}

impl Module {
    /// Save module index to JSON
    pub fn save_index(&self, path: &Path) -> Result<()> {
        let json = serde_json::to_string_pretty(self)?;
        std::fs::create_dir_all(path.parent().unwrap_or(Path::new(".")))?;
        std::fs::write(path, json)?;
        Ok(())
    }

    /// Get function by name
    pub fn get_function(&self, name: &str) -> Option<&Function> {
        self.functions.iter().find(|f| f.name == name)
    }

    /// Get function by index
    pub fn get_function_by_index(&self, index: usize) -> Option<&Function> {
        self.functions.iter().find(|f| f.index == index)
    }

    /// Get all exported functions
    pub fn exported_functions(&self) -> Vec<&Function> {
        self.functions.iter().filter(|f| f.is_export).collect()
    }

    /// Get all imported functions
    pub fn imported_functions(&self) -> Vec<&Function> {
        self.functions.iter().filter(|f| f.is_import).collect()
    }

    /// Get statistics
    pub fn stats(&self) -> ModuleStats {
        ModuleStats {
            total_functions: self.functions.len(),
            imported_functions: self.functions.iter().filter(|f| f.is_import).count(),
            exported_functions: self.functions.iter().filter(|f| f.is_export).count(),
            total_globals: self.globals.len(),
            data_sections: self.data_sections.len(),
            total_lines: self.total_lines,
        }
    }
}

#[derive(Debug, Serialize, Deserialize)]
pub struct ModuleStats {
    pub total_functions: usize,
    pub imported_functions: usize,
    pub exported_functions: usize,
    pub total_globals: usize,
    pub data_sections: usize,
    pub total_lines: usize,
}

/// Represents a WASM function
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Function {
    pub name: String,
    pub index: usize,
    pub params: Vec<String>,
    pub result: Option<String>,
    pub is_import: bool,
    pub is_export: bool,
    pub line_start: usize,
    pub line_end: usize,
    pub body: String,
    pub calls: Vec<String>,

    // Analysis results
    #[serde(skip_serializing_if = "Option::is_none")]
    pub suggested_name: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub category: Option<FunctionCategory>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub confidence: Option<f32>,
}

impl Function {
    /// Get the line count of this function
    pub fn line_count(&self) -> usize {
        self.line_end.saturating_sub(self.line_start) + 1
    }

    /// Check if function has any calls
    pub fn has_calls(&self) -> bool {
        !self.calls.is_empty()
    }

    /// Get a display name (suggested or original)
    pub fn display_name(&self) -> &str {
        self.suggested_name.as_deref().unwrap_or(&self.name)
    }
}

/// Function category based on RTS analysis
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub enum FunctionCategory {
    // Core game
    GameLoop,
    Init,
    Update,
    Render,

    // RTS specific
    Unit,
    Building,
    Resource,
    Terrain,
    Pathfinding,
    AI,
    Combat,

    // Systems
    Input,
    Audio,
    Network,
    UI,

    // Graphics
    WebP,
    Sprite,
    Animation,

    // Utility
    Memory,
    Math,
    String,

    // Unknown
    Unknown,
}

/// Represents an import declaration
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Import {
    pub module: String,
    pub name: String,
    pub local_name: String,
}

/// Represents an export declaration
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Export {
    pub name: String,
    pub kind: ExportKind,
}

#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub enum ExportKind {
    #[default]
    Function,
    Memory,
    Table,
    Global,
}

/// Represents a global variable
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Global {
    pub name: String,
    pub value_type: String,
    pub is_mutable: bool,
    pub initial_value: Option<i64>,
    pub line: usize,
}

/// Represents a data section
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct DataSection {
    pub offset: Option<u32>,
    pub content: Vec<u8>,
    pub strings: Vec<String>,
    pub line: usize,
    pub size_hint: usize,
}

impl DataSection {
    /// Extract readable strings from content
    pub fn extract_strings(&self) -> Vec<String> {
        let mut result = Vec::new();
        let mut current = String::new();

        for &byte in &self.content {
            if byte >= 32 && byte < 127 {
                current.push(byte as char);
            } else if !current.is_empty() {
                if current.len() >= 4 {
                    result.push(current.clone());
                }
                current.clear();
            }
        }

        if current.len() >= 4 {
            result.push(current);
        }

        result
    }
}
