//! Pattern Matcher - RTS-specific pattern detection for Tzar engine

use crate::sections::{Function, FunctionCategory};
use std::collections::HashSet;

/// Pattern matcher for identifying function purposes
pub struct PatternMatcher {
    webp_functions: HashSet<&'static str>,
    memory_functions: HashSet<&'static str>,
    math_patterns: Vec<&'static str>,
}

impl PatternMatcher {
    pub fn new() -> Self {
        Self {
            webp_functions: [
                "VP8", "WebP", "Huffman", "Rescaler", "Alpha", "RIFF",
                "Predictor", "Upsample", "Filter", "Decode",
            ].into_iter().collect(),

            memory_functions: [
                "malloc", "free", "calloc", "realloc", "memcpy", "memset",
                "Allocate", "Deallocate",
            ].into_iter().collect(),

            math_patterns: vec![
                "sin", "cos", "tan", "sqrt", "pow", "floor", "ceil",
                "min", "max", "abs", "clamp",
            ],
        }
    }

    /// Analyze a function and suggest name/category
    pub fn analyze_function(&self, func: &Function) -> (String, FunctionCategory, f32, Vec<String>) {
        let mut reasons = Vec::new();
        let mut confidence = 0.3;

        // Check for WebP decoder functions (from data strings)
        if self.is_webp_related(&func.name, &func.body) {
            reasons.push("WebP decoder pattern detected".to_string());
            return (
                self.generate_webp_name(&func.name),
                FunctionCategory::WebP,
                0.9,
                reasons,
            );
        }

        // Check for memory functions
        if self.is_memory_function(&func.name, &func.body) {
            reasons.push("Memory management pattern".to_string());
            return (
                self.generate_memory_name(&func.name),
                FunctionCategory::Memory,
                0.85,
                reasons,
            );
        }

        // Analyze based on function signature and body patterns
        let category = self.detect_category(func, &mut reasons);
        confidence = self.calculate_confidence(&category, &reasons);

        let suggested_name = self.generate_name(func, &category, &reasons);

        (suggested_name, category, confidence, reasons)
    }

    fn is_webp_related(&self, name: &str, body: &str) -> bool {
        // Check name
        for pattern in &self.webp_functions {
            if name.to_uppercase().contains(pattern) {
                return true;
            }
        }

        // Check body for WebP-related calls
        let webp_indicators = ["VP8", "WebP", "Huffman", "bitreader", "alpha"];
        for indicator in webp_indicators {
            if body.contains(indicator) {
                return true;
            }
        }

        false
    }

    fn is_memory_function(&self, name: &str, body: &str) -> bool {
        for pattern in &self.memory_functions {
            if name.to_lowercase().contains(&pattern.to_lowercase()) {
                return true;
            }
        }

        // Check for typical memory patterns
        if body.contains("9690908") || body.contains("9690912") {
            // Memory allocator addresses from the WASM
            return true;
        }

        false
    }

    fn detect_category(&self, func: &Function, reasons: &mut Vec<String>) -> FunctionCategory {
        let name_lower = func.name.to_lowercase();
        let body_lower = func.body.to_lowercase();

        // Check exports for hints
        if func.is_export {
            reasons.push("Exported function".to_string());
            if name_lower.contains("init") {
                return FunctionCategory::Init;
            }
            if name_lower.contains("update") || name_lower.contains("tick") {
                return FunctionCategory::Update;
            }
            if name_lower.contains("render") || name_lower.contains("draw") {
                return FunctionCategory::Render;
            }
        }

        // Check imports
        if func.is_import {
            if func.name.starts_with("$a.") {
                reasons.push("System import".to_string());
                return self.categorize_import(&func.name);
            }
        }

        // Analyze by common patterns in body
        if body_lower.contains("pathfind") || body_lower.contains("astar") ||
           self.has_grid_access_pattern(&func.body) {
            reasons.push("Pathfinding algorithm pattern".to_string());
            return FunctionCategory::Pathfinding;
        }

        // Check for terrain-related
        if body_lower.contains("terrain") || body_lower.contains("tile") ||
           body_lower.contains("grass") || body_lower.contains("desert") {
            reasons.push("Terrain handling".to_string());
            return FunctionCategory::Terrain;
        }

        // Check for combat
        if body_lower.contains("damage") || body_lower.contains("attack") ||
           body_lower.contains("health") || body_lower.contains("armor") {
            reasons.push("Combat system".to_string());
            return FunctionCategory::Combat;
        }

        // Check for AI
        if body_lower.contains("enemy") || body_lower.contains("target") ||
           body_lower.contains("decision") || body_lower.contains("strategy") {
            reasons.push("AI system".to_string());
            return FunctionCategory::AI;
        }

        // Check for network
        if body_lower.contains("fetch") || body_lower.contains("http") ||
           body_lower.contains("sync") || body_lower.contains("packet") {
            reasons.push("Network related".to_string());
            return FunctionCategory::Network;
        }

        // Check for UI
        if body_lower.contains("button") || body_lower.contains("panel") ||
           body_lower.contains("click") || body_lower.contains("mouse") {
            reasons.push("UI related".to_string());
            return FunctionCategory::UI;
        }

        // Check for audio
        if body_lower.contains("sound") || body_lower.contains("audio") ||
           body_lower.contains("music") || body_lower.contains("volume") {
            reasons.push("Audio system".to_string());
            return FunctionCategory::Audio;
        }

        // Check call patterns for categorization
        let calls_set: std::collections::HashSet<_> = func.calls.iter().collect();

        // Functions that call many others are likely managers/updates
        if func.calls.len() > 10 {
            reasons.push("High call count - possible manager function".to_string());
            return FunctionCategory::Update;
        }

        // Check for math-heavy functions
        if self.is_math_heavy(&func.body) {
            reasons.push("Math-heavy computation".to_string());
            return FunctionCategory::Math;
        }

        // Default based on size
        let line_count = func.line_count();
        if line_count > 500 {
            reasons.push("Large function - possible complex system".to_string());
        } else if line_count < 10 {
            reasons.push("Small utility function".to_string());
        }

        FunctionCategory::Unknown
    }

    fn categorize_import(&self, name: &str) -> FunctionCategory {
        // Based on the import pattern $a.X
        let suffix = name.trim_start_matches("$a.");

        match suffix {
            "b" | "c" | "d" | "e" => FunctionCategory::Memory,  // Common memory ops
            "f" => FunctionCategory::Math,  // Returns f64, likely time/random
            "g" => FunctionCategory::Unknown,  // No return, no params
            _ => FunctionCategory::Unknown,
        }
    }

    fn has_grid_access_pattern(&self, body: &str) -> bool {
        // Look for patterns like: offset = y * width + x
        body.contains("i32.mul") &&
        body.contains("i32.add") &&
        body.lines().filter(|l| l.contains("i32.load") || l.contains("i32.store")).count() > 3
    }

    fn is_math_heavy(&self, body: &str) -> bool {
        let math_ops = ["f32.mul", "f32.div", "f32.add", "f32.sub", "f32.sqrt",
                        "f64.mul", "f64.div", "f64.add", "f64.sub", "f64.sqrt"];

        let count: usize = math_ops.iter()
            .map(|op| body.matches(op).count())
            .sum();

        count > 10
    }

    fn calculate_confidence(&self, category: &FunctionCategory, reasons: &[String]) -> f32 {
        let base = match category {
            FunctionCategory::Unknown => 0.2,
            _ => 0.5,
        };

        let bonus = (reasons.len() as f32) * 0.1;

        (base + bonus).min(0.95)
    }

    fn generate_webp_name(&self, original: &str) -> String {
        let clean = original.trim_start_matches('$');

        if clean.starts_with("func") {
            format!("WebP_{}", clean)
        } else {
            format!("WebP_{}", clean.replace(".", "_"))
        }
    }

    fn generate_memory_name(&self, original: &str) -> String {
        let clean = original.trim_start_matches('$');

        if original.contains("af") {
            "Mem_Free".to_string()
        } else if original.contains("func26") {
            "Mem_Alloc".to_string()
        } else {
            format!("Mem_{}", clean.replace(".", "_"))
        }
    }

    fn generate_name(&self, func: &Function, category: &FunctionCategory, reasons: &[String]) -> String {
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
            FunctionCategory::Unknown => return func.name.clone(),
        };

        // Extract number from original name if present
        let num: String = func.name.chars()
            .filter(|c| c.is_numeric())
            .collect();

        if !num.is_empty() {
            format!("{}_{}", prefix, num)
        } else {
            format!("{}_{}", prefix, func.index)
        }
    }
}

impl Default for PatternMatcher {
    fn default() -> Self {
        Self::new()
    }
}
