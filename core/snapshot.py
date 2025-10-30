# core/snapshot.py
import os
from core.scanner import scan_directory
from core.db import initialize_db, insert_snapshot, insert_file

def save_snapshot_to_db(base_path="."):
    """Perform a scan and save results into SQLite database."""
    initialize_db()
    snapshot_id = insert_snapshot()

    file_count = 0
    total_size = 0

    for info in scan_directory(base_path):
        insert_file(snapshot_id, info)
        file_count += 1
        total_size += info["size_bytes"]

    print(f"\nSnapshot ID: {snapshot_id}")
    print(f"Scanned {file_count} files totaling {total_size/1024/1024:.2f} MB")

if __name__ == "__main__":
    folder = input("Enter directory to snapshot (blank = current): ").strip() or "."
    save_snapshot_to_db(folder)
