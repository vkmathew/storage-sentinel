# core/compare.py
import os
import csv

def load_snapshot(path):
    """Read a snapshot CSV into a dictionary keyed by file path."""
    data = {}
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[row['path']] = row
    return data

def compare_snapshots(old_file, new_file):
    old = load_snapshot(old_file)
    new = load_snapshot(new_file)

    old_paths = set(old.keys())
    new_paths = set(new.keys())

    added = new_paths - old_paths
    removed = old_paths - new_paths
    common = old_paths & new_paths

    modified = []
    for path in common:
        if (old[path]['size_bytes'] != new[path]['size_bytes'] or
                old[path]['modified'] != new[path]['modified']):
            modified.append(path)

    return added, removed, modified

if __name__ == "__main__":
    data_dir = "data"
    snapshots = sorted(
        [f for f in os.listdir(data_dir) if f.startswith("snapshot_") and f.endswith(".csv")]
    )

    if len(snapshots) < 2:
        print("Need at least two snapshot CSVs to compare.")
        exit(1)

    old_file = os.path.join(data_dir, snapshots[-2])
    new_file = os.path.join(data_dir, snapshots[-1])

    print(f"Comparing:\n  OLD → {old_file}\n  NEW → {new_file}\n")

    added, removed, modified = compare_snapshots(old_file, new_file)

    print(f"New files: {len(added)}")
    print(f"Removed files: {len(removed)}")
    print(f"Modified files: {len(modified)}")

    if added:
        print("\n--- New files ---")
        for p in list(added)[:10]:
            print(p)
        if len(added) > 10:
            print(f"...and {len(added) - 10} more")

    if removed:
        print("\n--- Removed files ---")
        for p in list(removed)[:10]:
            print(p)
        if len(removed) > 10:
            print(f"...and {len(removed) - 10} more")

    if modified:
        print("\n--- Modified files ---")
        for p in list(modified)[:10]:
            print(p)
        if len(modified) > 10:
            print(f"...and {len(modified) - 10} more")
