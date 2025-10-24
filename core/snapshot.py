# core/snapshot.py
import os
import csv
from datetime import datetime
from core.scanner import scan_directory

def save_snapshot(base_path=".", output_dir="data"):
    """Run a scan and save results to a timestamped CSV file."""
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = os.path.join(output_dir, f"snapshot_{timestamp}.csv")

    fieldnames = ["path", "size_bytes", "modified", "type"]
    count = 0
    total_size = 0

    with open(out_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for info in scan_directory(base_path):
            writer.writerow(info)
            count += 1
            total_size += info["size_bytes"]

    print(f"\nSnapshot saved: {out_path}")
    print(f"Total files scanned: {count}")
    print(f"Total size: {total_size/1024/1024:.2f} MB")

if __name__ == "__main__":
    folder = input("Enter directory to snapshot (blank = current): ").strip() or "."
    save_snapshot(folder)
