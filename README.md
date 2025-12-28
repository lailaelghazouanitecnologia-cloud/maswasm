# TzarWASM Static Analyzer

Static analysis toolkit for the Tzar RTS game engine compiled to WebAssembly.

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TzarWASM Static Analyzer                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────────┐  │
│  │  Python      │    │  Rust        │    │  Bun + React         │  │
│  │  Quick Tools │───▶│  Core        │───▶│  Graph Viewer        │  │
│  │              │    │  Analyzer    │    │                      │  │
│  └──────────────┘    └──────────────┘    └──────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Project Structure

```
maswasm/
├── mgame                 # Original WAT file (11MB, 406K lines)
├── analyzer/             # Rust core analyzer
│   └── src/
│       ├── parser.rs     # WAT streaming parser
│       ├── sections.rs   # Module section types
│       ├── callgraph.rs  # Call graph builder
│       ├── patterns.rs   # RTS pattern matching
│       └── symbols.rs    # Symbol naming
├── tools/                # Python quick tools
│   ├── quick_stats.py    # Fast statistics
│   ├── extract_strings.py # String extraction
│   ├── extract_functions.py # Function extraction
│   └── build_callgraph.py # Call graph builder
├── viewer/               # React graph visualization
│   └── src/
│       ├── components/   # UI components
│       ├── hooks/        # React hooks
│       └── types/        # TypeScript types
└── output/               # Analysis output
    ├── functions/        # Extracted functions
    ├── graphs/           # Call graphs
    └── strings.json      # Extracted strings
```

## Quick Start

### 1. Generate Analysis Data

```bash
# Quick stats
python3 tools/quick_stats.py mgame

# Build call graph (required for viewer)
python3 tools/build_callgraph.py mgame

# Extract strings
python3 tools/extract_strings.py mgame
```

### 2. Start Viewer

```bash
cd viewer
bun install
bun run dev
```

### 3. Use Makefile (recommended)

```bash
# Full pipeline
make analyze

# Start viewer
make viewer

# Show leaf functions
make leaves

# Show functions at depth 0
make depth d=0
```

## Analysis Philosophy: Bottom-Up

This analyzer uses a **bottom-up** approach for understanding the codebase:

```
                    Entry Points (Game Loop)
                           ↑
                    Depth N: Managers
                           ↑
                    Depth 2: Systems
                           ↑
                    Depth 1: Helpers
                           ↑
    ──────────── Depth 0: Leaf Functions ────────────
                    (Start Here!)
```

### Why Bottom-Up?

1. **Leaf functions** (depth 0) don't call other functions
2. They are the **simplest** to understand
3. Once understood, they provide **context** for their callers
4. Work your way **up** the call tree

### Workflow

1. Start with Depth 0 (leaves)
2. Analyze each function's purpose
3. Name them based on RTS context (Unit_, Building_, etc.)
4. Mark as analyzed
5. Move to Depth 1 (functions that only call leaves)
6. Use leaf context to understand callers
7. Repeat until you reach entry points

## RTS-Specific Categories

The analyzer recognizes these Tzar-specific patterns:

| Category | Keywords | Examples |
|----------|----------|----------|
| Unit | move, attack, health | Unit_Move, Unit_Attack |
| Building | construct, train | Building_Train |
| Resource | gold, wood, gather | Resource_Collect |
| Terrain | grass, desert, tile | Terrain_GetType |
| Pathfinding | path, astar | Path_FindRoute |
| AI | enemy, decision | AI_SelectTarget |
| Combat | damage, armor | Combat_Calculate |
| Render | draw, sprite | Render_DrawUnit |
| WebP | VP8, decode | WebP_DecodeFrame |
| Audio | sound, music | Audio_PlayEffect |
| Network | fetch, sync | Net_SyncState |
| UI | button, panel | UI_HandleClick |
| Memory | alloc, free | Mem_Alloc |

## Viewer Features

- **Hierarchy View**: Bottom-up tree of functions by depth
- **Graph View**: Force-directed graph visualization
- **List View**: Sortable table of all functions
- **Search**: Filter by function name
- **Progress Tracking**: Mark functions as analyzed
- **Annotations**: Add names, categories, and notes

## Commands

```bash
# Analysis
make stats       # Quick statistics
make strings     # Extract strings
make callgraph   # Build call graph
make extract     # Extract functions to files

# Viewer
make viewer      # Start development server
make viewer-build # Build for production

# Inspection
make leaves      # List leaf functions
make entries     # List entry points
make hotspots    # List most-called functions
make search q=VP8 # Search by name
make progress    # Show depth distribution
make depth d=0   # Show functions at depth

# Cleanup
make clean       # Remove outputs
make clean-all   # Remove all generated files
```

## Known Patterns in Tzar WASM

### Terrains
- `desert`, `grass`, `summer`, `jungle`, `snow2`

### Factions
- `Trenkorian`, `Nehhon`

### Key Subsystems
- WebP image decoder (VP8L, VP8)
- Memory allocator (`$func26`, `$af`)
- Emscripten runtime (`$a.*` imports)

## License

Research and educational use only.
