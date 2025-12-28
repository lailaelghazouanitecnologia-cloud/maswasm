#!/usr/bin/env python3
"""
Progress tracker for manual transpilation.

Commands:
- status: Show overall progress
- mark <func> <status>: Mark function status
- category <func> <cat>: Change function category
- note <func> <note>: Add note to function
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Colors
class C:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

def load_progress(path: Path) -> dict:
    """Load progress file."""
    if not path.exists():
        print(f"{C.RED}Error: {path} not found{C.END}")
        print("Run: python tools/scaffold.py first")
        sys.exit(1)
    return json.loads(path.read_text())

def save_progress(progress: dict, path: Path):
    """Save progress file."""
    progress['updated'] = datetime.now().isoformat()
    path.write_text(json.dumps(progress, indent=2))

def update_counts(progress: dict):
    """Update status counts."""
    counts = {'pending': 0, 'stub': 0, 'wip': 0, 'done': 0, 'verified': 0}
    cat_counts = {}

    for func_id, func_info in progress['functions'].items():
        status = func_info['status']
        category = func_info['category']

        counts[status] = counts.get(status, 0) + 1

        if category not in cat_counts:
            cat_counts[category] = {'total': 0, 'done': 0}
        cat_counts[category]['total'] += 1
        if status in ('done', 'verified'):
            cat_counts[category]['done'] += 1

    progress['by_status'] = counts
    progress['by_category'] = cat_counts

def show_status(progress: dict):
    """Show overall progress."""
    update_counts(progress)

    total = progress['total']
    done = progress['by_status'].get('done', 0) + progress['by_status'].get('verified', 0)
    percent = (done / total * 100) if total > 0 else 0

    print(f"\n{'='*60}")
    print(f"{C.BOLD}  TRANSPILATION PROGRESS{C.END}")
    print(f"{'='*60}")

    # Overall progress bar
    bar_width = 40
    filled = int(bar_width * done / total) if total > 0 else 0
    bar = '█' * filled + '░' * (bar_width - filled)
    print(f"\n  [{bar}] {percent:.1f}%")
    print(f"  {done} / {total} functions transpiled")

    # By status
    print(f"\n{C.BOLD}📊 By Status:{C.END}")
    for status, count in sorted(progress['by_status'].items()):
        icon = {'pending': '⏳', 'stub': '📝', 'wip': '🔨', 'done': '✅', 'verified': '✓✓'}.get(status, '?')
        color = {'done': C.GREEN, 'verified': C.GREEN, 'wip': C.YELLOW, 'pending': C.DIM}.get(status, '')
        print(f"   {icon} {color}{status:10s}{C.END}: {count}")

    # By category
    print(f"\n{C.BOLD}📁 By Category:{C.END}")
    for cat, counts in sorted(progress['by_category'].items(), key=lambda x: -x[1]['done']):
        done_cat = counts['done']
        total_cat = counts['total']
        pct = (done_cat / total_cat * 100) if total_cat > 0 else 0
        bar_len = 20
        filled = int(bar_len * done_cat / total_cat) if total_cat > 0 else 0
        bar = '█' * filled + '░' * (bar_len - filled)
        color = C.GREEN if pct == 100 else C.YELLOW if pct > 0 else C.DIM
        print(f"   {color}{cat:15s}{C.END} [{bar}] {done_cat:3d}/{total_cat:3d}")

    # Recent activity
    print(f"\n{C.BOLD}🕐 Recent:{C.END}")
    done_funcs = [(fid, fi) for fid, fi in progress['functions'].items()
                  if fi['status'] in ('done', 'verified')]

    if done_funcs:
        for fid, fi in done_funcs[:5]:
            print(f"   ✅ {fid}")
    else:
        print(f"   {C.DIM}No functions completed yet{C.END}")

    # Suggestions
    print(f"\n{C.BOLD}💡 Suggestions:{C.END}")
    wip = [fid for fid, fi in progress['functions'].items() if fi['status'] == 'wip']
    if wip:
        print(f"   Finish in-progress: {', '.join(wip[:3])}")

    print(f"\n{'='*60}\n")

def mark_function(progress: dict, func_name: str, status: str):
    """Mark a function with a status."""
    if not func_name.startswith('$'):
        func_name = f'${func_name}'

    if func_name not in progress['functions']:
        print(f"{C.RED}Function {func_name} not found{C.END}")
        return False

    valid_statuses = ('pending', 'stub', 'wip', 'done', 'verified')
    if status not in valid_statuses:
        print(f"{C.RED}Invalid status. Use: {', '.join(valid_statuses)}{C.END}")
        return False

    old_status = progress['functions'][func_name]['status']
    progress['functions'][func_name]['status'] = status

    print(f"✅ {func_name}: {old_status} → {C.GREEN}{status}{C.END}")
    return True

def set_category(progress: dict, func_name: str, category: str):
    """Set function category."""
    if not func_name.startswith('$'):
        func_name = f'${func_name}'

    if func_name not in progress['functions']:
        print(f"{C.RED}Function {func_name} not found{C.END}")
        return False

    old_cat = progress['functions'][func_name]['category']
    progress['functions'][func_name]['category'] = category

    print(f"✅ {func_name}: {old_cat} → {C.BLUE}{category}{C.END}")
    return True

def add_note(progress: dict, func_name: str, note: str):
    """Add note to function."""
    if not func_name.startswith('$'):
        func_name = f'${func_name}'

    if func_name not in progress['functions']:
        print(f"{C.RED}Function {func_name} not found{C.END}")
        return False

    progress['functions'][func_name]['notes'] = note
    print(f"✅ Added note to {func_name}")
    return True

def list_by_status(progress: dict, status: str):
    """List functions by status."""
    funcs = [(fid, fi) for fid, fi in progress['functions'].items()
             if fi['status'] == status]

    print(f"\n{C.BOLD}Functions with status '{status}':{C.END}")
    for fid, fi in sorted(funcs, key=lambda x: x[1]['category']):
        cat = fi['category']
        print(f"  {fid:30s} [{cat}]")

    print(f"\nTotal: {len(funcs)}")

def list_by_category(progress: dict, category: str):
    """List functions by category."""
    funcs = [(fid, fi) for fid, fi in progress['functions'].items()
             if fi['category'] == category]

    print(f"\n{C.BOLD}Functions in category '{category}':{C.END}")
    for fid, fi in sorted(funcs, key=lambda x: x[1]['status']):
        status = fi['status']
        icon = {'done': '✅', 'verified': '✓✓', 'wip': '🔨', 'stub': '📝', 'pending': '⏳'}.get(status, '?')
        print(f"  {icon} {fid}")

    print(f"\nTotal: {len(funcs)}")

def main():
    progress_path = Path('tzar/_progress.json')

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python tools/progress.py status                    - Show progress")
        print("  python tools/progress.py mark <func> <status>      - Mark status")
        print("  python tools/progress.py category <func> <cat>     - Set category")
        print("  python tools/progress.py note <func> 'note text'   - Add note")
        print("  python tools/progress.py list <status>             - List by status")
        print("  python tools/progress.py list-cat <category>       - List by category")
        print("\nStatuses: pending, stub, wip, done, verified")
        sys.exit(1)

    progress = load_progress(progress_path)
    command = sys.argv[1]
    modified = False

    if command == 'status':
        show_status(progress)

    elif command == 'mark':
        if len(sys.argv) < 4:
            print("Usage: python tools/progress.py mark <func> <status>")
            sys.exit(1)
        modified = mark_function(progress, sys.argv[2], sys.argv[3])

    elif command == 'category':
        if len(sys.argv) < 4:
            print("Usage: python tools/progress.py category <func> <category>")
            sys.exit(1)
        modified = set_category(progress, sys.argv[2], sys.argv[3])

    elif command == 'note':
        if len(sys.argv) < 4:
            print("Usage: python tools/progress.py note <func> 'note text'")
            sys.exit(1)
        modified = add_note(progress, sys.argv[2], ' '.join(sys.argv[3:]))

    elif command == 'list':
        if len(sys.argv) < 3:
            print("Usage: python tools/progress.py list <status>")
            sys.exit(1)
        list_by_status(progress, sys.argv[2])

    elif command == 'list-cat':
        if len(sys.argv) < 3:
            print("Usage: python tools/progress.py list-cat <category>")
            sys.exit(1)
        list_by_category(progress, sys.argv[2])

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

    if modified:
        update_counts(progress)
        save_progress(progress, progress_path)
        print(f"{C.DIM}Progress saved.{C.END}")

if __name__ == '__main__':
    main()
