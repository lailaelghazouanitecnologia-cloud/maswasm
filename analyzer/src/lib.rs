//! TzarWASM Static Analyzer
//!
//! Modular analyzer for the Tzar RTS game engine compiled to WebAssembly.
//! Designed for incremental analysis of large WASM modules.

pub mod parser;
pub mod sections;
pub mod symbols;
pub mod callgraph;
pub mod patterns;
pub mod output;

pub use parser::WatParser;
pub use sections::{Function, DataSection, Global, Module};
pub use symbols::SymbolTable;
pub use callgraph::CallGraph;
