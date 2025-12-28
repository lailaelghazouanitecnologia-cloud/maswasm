//! WAT Parser - Streaming parser for large WAT files
//!
//! Designed to handle 400k+ line files incrementally.

use anyhow::{Result, Context};
use indicatif::ProgressBar;
use rayon::prelude::*;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader, Write};
use std::path::Path;

use crate::sections::{Function, DataSection, Global, Module, Import, Export};

/// Streaming WAT parser for large files
pub struct WatParser {
    content: String,
    lines: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ExtractedString {
    pub offset: usize,
    pub value: String,
    pub category: StringCategory,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum StringCategory {
    Terrain,
    Faction,
    Error,
    Path,
    Url,
    Debug,
    Unknown,
}

impl WatParser {
    /// Create a new parser from a file path
    pub fn new(path: &Path) -> Result<Self> {
        let content = std::fs::read_to_string(path)
            .with_context(|| format!("Failed to read file: {}", path.display()))?;
        let lines: Vec<String> = content.lines().map(|s| s.to_string()).collect();
        Ok(Self { content, lines })
    }

    /// Parse the entire module
    pub fn parse(&self) -> Result<Module> {
        let mut module = Module::default();

        let mut current_func: Option<FunctionBuilder> = None;
        let mut brace_depth = 0;
        let mut func_start_line = 0;

        for (line_num, line) in self.lines.iter().enumerate() {
            let trimmed = line.trim();

            // Count braces for depth tracking
            brace_depth += line.matches('(').count() as i32;
            brace_depth -= line.matches(')').count() as i32;

            // Detect function start
            if trimmed.starts_with("(func ") {
                let func = self.parse_func_header(trimmed, line_num)?;
                func_start_line = line_num;
                current_func = Some(FunctionBuilder {
                    func,
                    body_lines: vec![line.clone()],
                    start_depth: brace_depth,
                });
            } else if let Some(ref mut builder) = current_func {
                builder.body_lines.push(line.clone());

                // Check if function ended
                if brace_depth < builder.start_depth {
                    let mut func = builder.func.clone();
                    func.line_start = func_start_line;
                    func.line_end = line_num;
                    func.body = builder.body_lines.join("\n");

                    // Extract calls from body
                    func.calls = self.extract_calls(&func.body);

                    module.functions.push(func);
                    current_func = None;
                }
            }

            // Detect imports
            if trimmed.contains("(import ") {
                if let Some(import) = self.parse_import(trimmed) {
                    module.imports.push(import);
                }
            }

            // Detect exports
            if trimmed.contains("(export ") {
                if let Some(export) = self.parse_export(trimmed) {
                    module.exports.push(export);
                }
            }

            // Detect globals
            if trimmed.starts_with("(global ") {
                if let Some(global) = self.parse_global(trimmed, line_num) {
                    module.globals.push(global);
                }
            }

            // Detect data sections
            if trimmed.starts_with("(data ") {
                if let Some(data) = self.parse_data(trimmed, line_num) {
                    module.data_sections.push(data);
                }
            }

            // Detect memory
            if trimmed.contains("(memory ") {
                module.memory_size = self.parse_memory_size(trimmed);
            }

            // Detect table
            if trimmed.contains("(table ") {
                module.table_size = self.parse_table_size(trimmed);
            }
        }

        module.total_lines = self.lines.len();
        Ok(module)
    }

    /// Extract functions to individual files
    pub fn extract_functions(&self, output_dir: &Path, pb: Option<&ProgressBar>) -> Result<()> {
        std::fs::create_dir_all(output_dir)?;

        let module = self.parse()?;

        if let Some(pb) = pb {
            pb.set_length(module.functions.len() as u64);
        }

        for func in &module.functions {
            let filename = format!("{}.wat", sanitize_name(&func.name));
            let filepath = output_dir.join(&filename);

            let mut file = File::create(&filepath)?;
            writeln!(file, ";; Function: {}", func.name)?;
            writeln!(file, ";; Index: {}", func.index)?;
            writeln!(file, ";; Lines: {}-{}", func.line_start, func.line_end)?;
            writeln!(file, ";; Calls: {:?}", func.calls)?;
            writeln!(file, "")?;
            writeln!(file, "{}", func.body)?;

            if let Some(pb) = pb {
                pb.inc(1);
            }
        }

        // Also save index
        let index_path = output_dir.join("_index.json");
        let index: Vec<_> = module.functions.iter().map(|f| {
            serde_json::json!({
                "name": f.name,
                "index": f.index,
                "file": format!("{}.wat", sanitize_name(&f.name)),
                "lines": [f.line_start, f.line_end],
                "calls": f.calls,
            })
        }).collect();

        std::fs::write(index_path, serde_json::to_string_pretty(&index)?)?;

        Ok(())
    }

    /// Extract all readable strings from data sections
    pub fn extract_strings(&self) -> Result<Vec<ExtractedString>> {
        let mut strings = Vec::new();
        let mut in_data = false;
        let mut current_data = String::new();

        for line in &self.lines {
            if line.trim().starts_with("(data ") {
                in_data = true;
                current_data.clear();
            }

            if in_data {
                current_data.push_str(line);

                if line.contains("\")") {
                    // Extract strings from data section
                    let extracted = self.extract_strings_from_data(&current_data);
                    strings.extend(extracted);
                    in_data = false;
                }
            }
        }

        Ok(strings)
    }

    fn extract_strings_from_data(&self, data: &str) -> Vec<ExtractedString> {
        let mut result = Vec::new();

        // Find quoted strings
        let mut in_string = false;
        let mut current = String::new();
        let mut chars = data.chars().peekable();

        while let Some(c) = chars.next() {
            if c == '"' && !in_string {
                in_string = true;
                current.clear();
            } else if c == '"' && in_string {
                // Check for escape
                if current.ends_with('\\') {
                    current.push(c);
                } else {
                    // End of string - filter readable ones
                    let clean = self.clean_string(&current);
                    if clean.len() >= 3 && self.is_readable(&clean) {
                        let category = self.categorize_string(&clean);
                        result.push(ExtractedString {
                            offset: 0,
                            value: clean,
                            category,
                        });
                    }
                    in_string = false;
                }
            } else if in_string {
                current.push(c);
            }
        }

        result
    }

    fn clean_string(&self, s: &str) -> String {
        let mut result = String::new();
        let mut chars = s.chars().peekable();

        while let Some(c) = chars.next() {
            if c == '\\' {
                if let Some(&next) = chars.peek() {
                    match next {
                        'n' => { result.push('\n'); chars.next(); }
                        't' => { result.push('\t'); chars.next(); }
                        '0' => { result.push('\0'); chars.next(); }
                        '\\' => { result.push('\\'); chars.next(); }
                        '"' => { result.push('"'); chars.next(); }
                        _ => {
                            // Hex escape like \xx
                            chars.next();
                            if let Some(&hex2) = chars.peek() {
                                chars.next();
                            }
                        }
                    }
                }
            } else {
                result.push(c);
            }
        }

        // Filter to printable ASCII
        result.chars().filter(|c| c.is_ascii_graphic() || *c == ' ').collect()
    }

    fn is_readable(&self, s: &str) -> bool {
        let alpha_count = s.chars().filter(|c| c.is_alphabetic()).count();
        alpha_count as f32 / s.len() as f32 > 0.5
    }

    fn categorize_string(&self, s: &str) -> StringCategory {
        let lower = s.to_lowercase();

        if ["desert", "grass", "summer", "jungle", "snow"].iter().any(|t| lower.contains(t)) {
            StringCategory::Terrain
        } else if ["trenkorian", "nehhon"].iter().any(|t| lower.contains(t)) {
            StringCategory::Faction
        } else if lower.contains("error") || lower.contains("failed") || lower.contains("invalid") {
            StringCategory::Error
        } else if lower.contains("http") || lower.contains("://") {
            StringCategory::Url
        } else if lower.contains("/") || lower.contains(".") && lower.contains("/") {
            StringCategory::Path
        } else if lower.contains("debug") || lower.contains("assert") {
            StringCategory::Debug
        } else {
            StringCategory::Unknown
        }
    }

    fn parse_func_header(&self, line: &str, _line_num: usize) -> Result<Function> {
        // Parse: (func $name (;index;) ...)
        let mut func = Function::default();

        // Extract name
        if let Some(start) = line.find('$') {
            let rest = &line[start..];
            let end = rest.find(|c: char| c.is_whitespace() || c == '(').unwrap_or(rest.len());
            func.name = rest[..end].to_string();
        }

        // Extract index from comment (;index;)
        if let Some(start) = line.find("(;") {
            if let Some(end) = line[start..].find(";)") {
                let index_str = &line[start + 2..start + end];
                func.index = index_str.parse().unwrap_or(0);
            }
        }

        // Check if it's an import
        func.is_import = line.contains("(import ");

        // Check if it's an export
        func.is_export = line.contains("(export ");

        // Extract params
        let mut params = Vec::new();
        let mut rest = line;
        while let Some(start) = rest.find("(param ") {
            let param_start = start + 7;
            if let Some(end) = rest[param_start..].find(')') {
                let param_content = &rest[param_start..param_start + end];
                // Parse types like "i32" or "$var0 i32"
                for part in param_content.split_whitespace() {
                    if !part.starts_with('$') {
                        params.push(part.to_string());
                    }
                }
            }
            rest = &rest[start + 7..];
        }
        func.params = params;

        // Extract result
        if let Some(start) = line.find("(result ") {
            let result_start = start + 8;
            if let Some(end) = line[result_start..].find(')') {
                func.result = Some(line[result_start..result_start + end].trim().to_string());
            }
        }

        Ok(func)
    }

    fn extract_calls(&self, body: &str) -> Vec<String> {
        let mut calls = Vec::new();

        for word in body.split_whitespace() {
            if word.starts_with("$") && !word.starts_with("$var") && !word.starts_with("$label") {
                // Check if previous word was "call" or similar
                calls.push(word.trim_matches(|c| c == '(' || c == ')').to_string());
            }
        }

        // Also look for call and call_indirect patterns
        for line in body.lines() {
            let trimmed = line.trim();
            if trimmed.starts_with("call ") || trimmed.contains(" call ") {
                if let Some(target) = trimmed.split_whitespace()
                    .find(|w| w.starts_with('$'))
                {
                    let clean = target.trim_matches(|c| c == '(' || c == ')');
                    if !calls.contains(&clean.to_string()) {
                        calls.push(clean.to_string());
                    }
                }
            }
        }

        calls.sort();
        calls.dedup();
        calls
    }

    fn parse_import(&self, line: &str) -> Option<Import> {
        // (func $a.b (;0;) (import "a" "b") ...)
        let mut import = Import::default();

        if let Some(start) = line.find("(import ") {
            let rest = &line[start + 8..];
            let parts: Vec<&str> = rest.split('"').collect();
            if parts.len() >= 4 {
                import.module = parts[1].to_string();
                import.name = parts[3].to_string();
            }
        }

        if let Some(start) = line.find('$') {
            let rest = &line[start..];
            let end = rest.find(|c: char| c.is_whitespace() || c == '(').unwrap_or(rest.len());
            import.local_name = rest[..end].to_string();
        }

        Some(import)
    }

    fn parse_export(&self, line: &str) -> Option<Export> {
        // (export "name")
        let mut export = Export::default();

        if let Some(start) = line.find("(export ") {
            let rest = &line[start + 8..];
            if let Some(quote_start) = rest.find('"') {
                let after_quote = &rest[quote_start + 1..];
                if let Some(quote_end) = after_quote.find('"') {
                    export.name = after_quote[..quote_end].to_string();
                }
            }
        }

        Some(export)
    }

    fn parse_global(&self, line: &str, line_num: usize) -> Option<Global> {
        let mut global = Global::default();
        global.line = line_num;

        if let Some(start) = line.find('$') {
            let rest = &line[start..];
            let end = rest.find(|c: char| c.is_whitespace() || c == '(').unwrap_or(rest.len());
            global.name = rest[..end].to_string();
        }

        global.is_mutable = line.contains("(mut ");

        // Extract type
        if line.contains("i32") {
            global.value_type = "i32".to_string();
        } else if line.contains("i64") {
            global.value_type = "i64".to_string();
        } else if line.contains("f32") {
            global.value_type = "f32".to_string();
        } else if line.contains("f64") {
            global.value_type = "f64".to_string();
        }

        Some(global)
    }

    fn parse_data(&self, line: &str, line_num: usize) -> Option<DataSection> {
        let mut data = DataSection::default();
        data.line = line_num;

        // Just mark existence, actual parsing is expensive
        data.size_hint = line.len();

        Some(data)
    }

    fn parse_memory_size(&self, line: &str) -> Option<(u32, u32)> {
        // (memory $a.a (;0;) (import "a" "a") 880 65536 shared)
        let numbers: Vec<u32> = line
            .split_whitespace()
            .filter_map(|w| w.parse().ok())
            .collect();

        if numbers.len() >= 2 {
            Some((numbers[0], numbers[1]))
        } else if numbers.len() == 1 {
            Some((numbers[0], numbers[0]))
        } else {
            None
        }
    }

    fn parse_table_size(&self, line: &str) -> Option<u32> {
        let numbers: Vec<u32> = line
            .split_whitespace()
            .filter_map(|w| w.parse().ok())
            .collect();

        numbers.first().copied()
    }
}

struct FunctionBuilder {
    func: Function,
    body_lines: Vec<String>,
    start_depth: i32,
}

fn sanitize_name(name: &str) -> String {
    name.chars()
        .map(|c| if c.is_alphanumeric() || c == '_' { c } else { '_' })
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sanitize_name() {
        assert_eq!(sanitize_name("$func123"), "_func123");
        assert_eq!(sanitize_name("a.b"), "a_b");
    }
}
