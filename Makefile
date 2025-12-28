# TzarWASM Static Analyzer
# Makefile for building and running the analysis pipeline

.PHONY: all setup analyze extract callgraph strings viewer clean

# Default target
all: setup analyze viewer

# Configuration
WAT_FILE := mgame
OUTPUT_DIR := output

# ============================================
# Setup
# ============================================

setup: setup-rust setup-python setup-viewer

setup-rust:
	@echo "Setting up Rust analyzer..."
	cd analyzer && cargo build --release

setup-python:
	@echo "Setting up Python tools..."
	cd tools && pip install -r requirements.txt -q

setup-viewer:
	@echo "Setting up viewer..."
	cd viewer && bun install

# ============================================
# Analysis Pipeline
# ============================================

analyze: stats strings callgraph extract
	@echo "Full analysis complete!"

# Quick stats (Python - fast)
stats:
	@echo "Generating quick stats..."
	python3 tools/quick_stats.py $(WAT_FILE) $(OUTPUT_DIR)/stats.json

# Extract strings (Python - fast)
strings:
	@echo "Extracting strings..."
	python3 tools/extract_strings.py $(WAT_FILE) $(OUTPUT_DIR)/strings.json

# Build call graph (Python - fast, or Rust for large files)
callgraph:
	@echo "Building call graph..."
	@mkdir -p $(OUTPUT_DIR)/graphs
	python3 tools/build_callgraph.py $(WAT_FILE) $(OUTPUT_DIR)/graphs/callgraph.json

# Extract functions to separate files (Python)
extract:
	@echo "Extracting functions..."
	python3 tools/extract_functions.py $(WAT_FILE) $(OUTPUT_DIR)/functions

# Full analysis with Rust (slower but more complete)
analyze-rust:
	@echo "Running full Rust analysis..."
	cd analyzer && cargo run --release -- full -i ../$(WAT_FILE) -o ../$(OUTPUT_DIR)

# ============================================
# Viewer
# ============================================

viewer: callgraph
	@echo "Starting viewer..."
	@mkdir -p viewer/public/data
	@cp $(OUTPUT_DIR)/graphs/callgraph-react.json viewer/public/data/
	cd viewer && bun run dev

viewer-build:
	cd viewer && bun run build

# ============================================
# Individual Analysis Commands
# ============================================

# List leaf functions (no outgoing calls)
leaves:
	@python3 -c "import json; d=json.load(open('$(OUTPUT_DIR)/graphs/callgraph.json')); print('Leaf functions:'); [print(f'  {n[\"id\"]}') for n in d['nodes'] if n['out_degree']==0][:20]"

# List entry points (no incoming calls, not imports)
entries:
	@python3 -c "import json; d=json.load(open('$(OUTPUT_DIR)/graphs/callgraph.json')); print('Entry points:'); [print(f'  {n[\"id\"]}') for n in d['nodes'] if n['in_degree']==0 and not n['is_import']][:20]"

# List most called functions
hotspots:
	@python3 -c "import json; d=json.load(open('$(OUTPUT_DIR)/graphs/callgraph.json')); print('Most called:'); [print(f'  {name}: {count}') for name,count in d['stats']['most_called'][:10]]"

# Search for function by name
search:
	@test -n "$(q)" || (echo "Usage: make search q=pattern" && exit 1)
	@python3 -c "import json; d=json.load(open('$(OUTPUT_DIR)/graphs/callgraph.json')); [print(n['id']) for n in d['nodes'] if '$(q)'.lower() in n['name'].lower()]"

# ============================================
# Bottom-Up Analysis Workflow
# ============================================

# Show analysis progress by depth
progress:
	@python3 -c "\
import json;\
d=json.load(open('$(OUTPUT_DIR)/graphs/callgraph.json'));\
nodes={n['id']:n for n in d['nodes']};\
links=d['links'];\
callees={l['source']:set() for l in links};\
[callees[l['source']].add(l['target']) for l in links];\
depths={};\
leaves=[n['id'] for n in d['nodes'] if n['out_degree']==0];\
for l in leaves: depths[l]=0;\
queue=leaves[:];\
while queue:\
    c=queue.pop(0);\
    cd=depths.get(c,0);\
    callers=[l['source'] for l in links if l['target']==c];\
    for p in callers:\
        if depths.get(p,-1)<cd+1:\
            depths[p]=cd+1;\
            queue.append(p);\
by_depth={};\
for nid,d in depths.items(): by_depth.setdefault(d,[]).append(nid);\
print('Functions by depth (bottom-up):');\
for d in sorted(by_depth.keys()): print(f'  Depth {d}: {len(by_depth[d])} functions');\
"

# Show functions at specific depth
depth:
	@test -n "$(d)" || (echo "Usage: make depth d=0" && exit 1)
	@python3 tools/build_callgraph.py $(WAT_FILE) /tmp/cg.json 2>/dev/null
	@python3 -c "\
import json;\
data=json.load(open('/tmp/cg.json'));\
nodes={n['id']:n for n in data['nodes']};\
links=data['links'];\
depths={};\
leaves=[n['id'] for n in data['nodes'] if n['out_degree']==0];\
for l in leaves: depths[l]=0;\
queue=leaves[:];\
while queue:\
    c=queue.pop(0);\
    cd=depths.get(c,0);\
    callers=[l['source'] for l in links if l['target']==c];\
    for p in callers:\
        if depths.get(p,-1)<cd+1:\
            depths[p]=cd+1;\
            queue.append(p);\
print(f'Functions at depth $(d):');\
for nid,d in depths.items():\
    if d==$(d): print(f'  {nid}');\
"

# ============================================
# Cleanup
# ============================================

clean:
	rm -rf $(OUTPUT_DIR)/*
	rm -rf viewer/dist

clean-all: clean
	rm -rf analyzer/target
	rm -rf viewer/node_modules
