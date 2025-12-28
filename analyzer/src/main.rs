use anyhow::Result;
use clap::{Parser, Subcommand};
use indicatif::{ProgressBar, ProgressStyle};
use std::path::PathBuf;

use tzar_analyzer::{WatParser, CallGraph, SymbolTable};

#[derive(Parser)]
#[command(name = "tzar-analyze")]
#[command(about = "Static analyzer for Tzar RTS WASM engine", long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Parse WAT file and extract sections
    Parse {
        /// Input WAT file
        #[arg(short, long)]
        input: PathBuf,

        /// Output directory
        #[arg(short, long, default_value = "output")]
        output: PathBuf,
    },

    /// Extract all functions to separate files
    Extract {
        /// Input WAT file
        #[arg(short, long)]
        input: PathBuf,

        /// Output directory for functions
        #[arg(short, long, default_value = "output/functions")]
        output: PathBuf,
    },

    /// Build call graph
    Callgraph {
        /// Input WAT file
        #[arg(short, long)]
        input: PathBuf,

        /// Output JSON file
        #[arg(short, long, default_value = "output/graphs/callgraph.json")]
        output: PathBuf,
    },

    /// Analyze and rename symbols based on RTS patterns
    Rename {
        /// Input WAT file
        #[arg(short, long)]
        input: PathBuf,

        /// Symbol table output
        #[arg(short, long, default_value = "output/symbols.json")]
        output: PathBuf,
    },

    /// Extract strings and data sections
    Strings {
        /// Input WAT file
        #[arg(short, long)]
        input: PathBuf,

        /// Output JSON file
        #[arg(short, long, default_value = "output/strings.json")]
        output: PathBuf,
    },

    /// Full analysis pipeline
    Full {
        /// Input WAT file
        #[arg(short, long)]
        input: PathBuf,

        /// Output directory
        #[arg(short, long, default_value = "output")]
        output: PathBuf,
    },
}

fn main() -> Result<()> {
    let cli = Cli::parse();

    match cli.command {
        Commands::Parse { input, output } => {
            println!("Parsing {}...", input.display());
            let parser = WatParser::new(&input)?;
            let module = parser.parse()?;
            module.save_index(&output.join("index.json"))?;
            println!("Done! Index saved to {}/index.json", output.display());
        }

        Commands::Extract { input, output } => {
            println!("Extracting functions from {}...", input.display());
            let parser = WatParser::new(&input)?;
            let pb = ProgressBar::new(0);
            pb.set_style(ProgressStyle::default_bar()
                .template("{spinner:.green} [{elapsed_precise}] [{bar:40.cyan/blue}] {pos}/{len} ({eta})")?);
            parser.extract_functions(&output, Some(&pb))?;
            pb.finish_with_message("Done!");
        }

        Commands::Callgraph { input, output } => {
            println!("Building call graph...");
            let parser = WatParser::new(&input)?;
            let module = parser.parse()?;
            let callgraph = CallGraph::build(&module);
            callgraph.save_json(&output)?;
            println!("Call graph saved to {}", output.display());
        }

        Commands::Rename { input, output } => {
            println!("Analyzing symbols with RTS patterns...");
            let parser = WatParser::new(&input)?;
            let module = parser.parse()?;
            let symbols = SymbolTable::analyze(&module);
            symbols.save(&output)?;
            println!("Symbols saved to {}", output.display());
        }

        Commands::Strings { input, output } => {
            println!("Extracting strings...");
            let parser = WatParser::new(&input)?;
            let strings = parser.extract_strings()?;
            let json = serde_json::to_string_pretty(&strings)?;
            std::fs::write(&output, json)?;
            println!("Strings saved to {}", output.display());
        }

        Commands::Full { input, output } => {
            println!("Running full analysis pipeline...");
            // TODO: Implement full pipeline
            println!("Full pipeline not yet implemented");
        }
    }

    Ok(())
}
