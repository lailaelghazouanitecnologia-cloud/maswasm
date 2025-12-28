#!/usr/bin/env python3
"""
Quick statistics for Tzar WASM module
Fast analysis without full parsing
"""

import re
import json
import sys
from pathlib import Path
from collections import Counter
from dataclasses import dataclass, asdict

@dataclass
class WatStats:
    total_lines: int = 0
    total_functions: int = 0
    imported_functions: int = 0
    exported_functions: int = 0
    local_functions: int = 0
    globals_count: int = 0
    data_sections: int = 0
    memory_pages: tuple = (0, 0)
    table_size: int = 0

    # Function size distribution
    tiny_funcs: int = 0    # < 10 lines
    small_funcs: int = 0   # 10-50 lines
    medium_funcs: int = 0  # 50-200 lines
    large_funcs: int = 0   # 200-500 lines
    huge_funcs: int = 0    # > 500 lines

    # Instruction stats
    call_count: int = 0
    call_indirect_count: int = 0
    load_count: int = 0
    store_count: int = 0

    # Named vs unnamed
    named_functions: list = None

def analyze_wat(filepath: Path) -> WatStats:
    """Analyze WAT file and collect statistics."""
    stats = WatStats()
    stats.named_functions = []

    content = filepath.read_text(encoding='utf-8', errors='ignore')
    lines = content.split('\n')
    stats.total_lines = len(lines)

    current_func_lines = 0
    in_function = False
    brace_depth = 0

    for line in lines:
        stripped = line.strip()

        # Count braces
        brace_depth += line.count('(') - line.count(')')

        # Detect function start
        if stripped.startswith('(func '):
            stats.total_functions += 1
            in_function = True
            current_func_lines = 1

            if '(import ' in stripped:
                stats.imported_functions += 1
            elif '(export ' in stripped:
                stats.exported_functions += 1
            else:
                stats.local_functions += 1

            # Extract name if not generic
            name_match = re.search(r'\$([A-Za-z][A-Za-z0-9_]*)', stripped)
            if name_match:
                name = name_match.group(1)
                if not name.startswith('func') and not name.startswith('a_'):
                    stats.named_functions.append(name)

        elif in_function:
            current_func_lines += 1

            # Check if function ended
            if brace_depth <= 1 and ')' in line:
                in_function = False

                # Categorize by size
                if current_func_lines < 10:
                    stats.tiny_funcs += 1
                elif current_func_lines < 50:
                    stats.small_funcs += 1
                elif current_func_lines < 200:
                    stats.medium_funcs += 1
                elif current_func_lines < 500:
                    stats.large_funcs += 1
                else:
                    stats.huge_funcs += 1

        # Count instructions
        if 'call ' in stripped and 'call_indirect' not in stripped:
            stats.call_count += stripped.count('call ')
        if 'call_indirect' in stripped:
            stats.call_indirect_count += 1
        if '.load' in stripped:
            stats.load_count += 1
        if '.store' in stripped:
            stats.store_count += 1

        # Other sections
        if stripped.startswith('(global '):
            stats.globals_count += 1
        if stripped.startswith('(data '):
            stats.data_sections += 1
        if '(memory ' in stripped:
            nums = re.findall(r'\d+', stripped)
            if len(nums) >= 2:
                stats.memory_pages = (int(nums[0]), int(nums[1]))
        if '(table ' in stripped:
            nums = re.findall(r'\d+', stripped)
            if nums:
                stats.table_size = int(nums[0])

    return stats

def print_stats(stats: WatStats):
    """Pretty print statistics."""
    print("\n" + "="*60)
    print("  TZAR WASM MODULE STATISTICS")
    print("="*60)

    print(f"\n📊 General:")
    print(f"   Total lines:        {stats.total_lines:,}")
    print(f"   Total functions:    {stats.total_functions:,}")
    print(f"   Globals:            {stats.globals_count}")
    print(f"   Data sections:      {stats.data_sections}")
    print(f"   Memory:             {stats.memory_pages[0]} - {stats.memory_pages[1]} pages")
    print(f"   Table size:         {stats.table_size}")

    print(f"\n📦 Functions breakdown:")
    print(f"   Imported:           {stats.imported_functions}")
    print(f"   Exported:           {stats.exported_functions}")
    print(f"   Local:              {stats.local_functions}")

    print(f"\n📏 Function sizes:")
    print(f"   Tiny (<10):         {stats.tiny_funcs}")
    print(f"   Small (10-50):      {stats.small_funcs}")
    print(f"   Medium (50-200):    {stats.medium_funcs}")
    print(f"   Large (200-500):    {stats.large_funcs}")
    print(f"   Huge (>500):        {stats.huge_funcs}")

    print(f"\n🔧 Instructions:")
    print(f"   Calls:              {stats.call_count:,}")
    print(f"   Indirect calls:     {stats.call_indirect_count}")
    print(f"   Memory loads:       {stats.load_count:,}")
    print(f"   Memory stores:      {stats.store_count:,}")

    if stats.named_functions:
        print(f"\n🏷️  Named functions ({len(stats.named_functions)}):")
        for name in stats.named_functions[:20]:
            print(f"   - {name}")
        if len(stats.named_functions) > 20:
            print(f"   ... and {len(stats.named_functions) - 20} more")

    print("\n" + "="*60)

def main():
    if len(sys.argv) < 2:
        print("Usage: python quick_stats.py <wat_file> [output.json]")
        sys.exit(1)

    wat_file = Path(sys.argv[1])

    if not wat_file.exists():
        print(f"Error: {wat_file} not found")
        sys.exit(1)

    print(f"Analyzing {wat_file}...")
    stats = analyze_wat(wat_file)
    print_stats(stats)

    if len(sys.argv) > 2:
        output_file = Path(sys.argv[2])
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Convert to dict for JSON
        data = asdict(stats)
        data['memory_pages'] = list(stats.memory_pages)

        output_file.write_text(json.dumps(data, indent=2))
        print(f"\nStats saved to {output_file}")

if __name__ == '__main__':
    main()
