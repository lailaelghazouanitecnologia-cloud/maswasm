#!/usr/bin/env python3
"""
Quick string extractor for Tzar WASM
Extracts readable strings from data sections
"""

import re
import json
import sys
from pathlib import Path
from collections import defaultdict

# RTS-specific categorization
CATEGORIES = {
    'terrain': ['desert', 'grass', 'summer', 'jungle', 'snow', 'water', 'mountain'],
    'faction': ['trenkorian', 'nehhon', 'european'],
    'unit': ['peasant', 'soldier', 'knight', 'archer', 'cavalry', 'worker'],
    'building': ['castle', 'barracks', 'tower', 'farm', 'mill', 'mine'],
    'resource': ['gold', 'wood', 'stone', 'food', 'iron'],
    'error': ['error', 'failed', 'invalid', 'null', 'assert', 'exception'],
    'webp': ['vp8', 'webp', 'huffman', 'decode', 'alpha', 'riff', 'predictor'],
    'path': ['.c', '.h', '.wat', 'src/', 'nh/'],
    'url': ['http', '://', 'tza.red'],
}

def extract_strings_from_wat(filepath: Path) -> list[dict]:
    """Extract strings from WAT file data sections."""
    content = filepath.read_text(encoding='utf-8', errors='ignore')
    strings = []

    # Find all quoted strings in data sections
    # Pattern: "..." with escape handling
    in_data = False
    current_offset = 0

    for line in content.split('\n'):
        if '(data' in line:
            in_data = True
            # Try to extract offset
            offset_match = re.search(r'i32\.const (\d+)', line)
            if offset_match:
                current_offset = int(offset_match.group(1))

        if in_data:
            # Extract quoted strings
            for match in re.finditer(r'"([^"\\]*(?:\\.[^"\\]*)*)"', line):
                raw = match.group(1)
                cleaned = clean_string(raw)
                if is_readable(cleaned) and len(cleaned) >= 3:
                    category = categorize(cleaned)
                    strings.append({
                        'value': cleaned,
                        'raw': raw[:100],  # Truncate raw
                        'category': category,
                        'offset': current_offset,
                    })

    return strings

def clean_string(s: str) -> str:
    """Clean escaped string to readable format."""
    result = []
    i = 0
    while i < len(s):
        if s[i] == '\\' and i + 1 < len(s):
            next_char = s[i + 1]
            if next_char == 'n':
                result.append('\n')
                i += 2
            elif next_char == 't':
                result.append('\t')
                i += 2
            elif next_char == '0':
                # Null terminator or hex
                if i + 2 < len(s) and s[i+2] == '0':
                    i += 3
                else:
                    i += 2
            elif next_char == '\\':
                result.append('\\')
                i += 2
            elif next_char == '"':
                result.append('"')
                i += 2
            elif next_char.isalnum():
                # Hex escape \xx
                i += 4 if i + 3 < len(s) and s[i+2:i+4].replace('\\','').isalnum() else 2
            else:
                i += 2
        else:
            if s[i].isprintable() or s[i] in ' \n\t':
                result.append(s[i])
            i += 1

    return ''.join(result).strip()

def is_readable(s: str) -> bool:
    """Check if string is human-readable."""
    if not s:
        return False

    alpha_count = sum(1 for c in s if c.isalpha())
    if len(s) == 0:
        return False

    ratio = alpha_count / len(s)
    return ratio > 0.4 or any(c in s for c in ['_', '/', '.', ':'])

def categorize(s: str) -> str:
    """Categorize string based on content."""
    lower = s.lower()

    for category, keywords in CATEGORIES.items():
        if any(kw in lower for kw in keywords):
            return category

    return 'unknown'

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_strings.py <wat_file> [output.json]")
        sys.exit(1)

    wat_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('output/strings.json')

    if not wat_file.exists():
        print(f"Error: {wat_file} not found")
        sys.exit(1)

    print(f"Extracting strings from {wat_file}...")
    strings = extract_strings_from_wat(wat_file)

    # Group by category
    by_category = defaultdict(list)
    for s in strings:
        by_category[s['category']].append(s)

    result = {
        'total': len(strings),
        'by_category': {k: len(v) for k, v in by_category.items()},
        'strings': strings,
    }

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(result, indent=2))

    print(f"\nExtracted {len(strings)} strings:")
    for cat, items in sorted(by_category.items(), key=lambda x: -len(x[1])):
        print(f"  {cat}: {len(items)}")
    print(f"\nSaved to {output_file}")

if __name__ == '__main__':
    main()
