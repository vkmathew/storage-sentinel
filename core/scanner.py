# core/scanner.py
import os
import mimetypes
from datetime import datetime

def scan_directory(base_path="."):
    """
    Walk through all sub-folders and yield file details.
    Each result is a dictionary with path, size (bytes),
    modified time (ISO string) and MIME type.
    """
    for root, _, files in os.walk(base_path):
        for f in files:
            full_path = os.path.join(root, f)
            try:
                stat = os.stat(full_path)
                size = stat.st_size
                mtime = datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds")
                mime, _ = mimetypes.guess_type(full_path)
                yield {
                    "path": full_path,
                    "size_bytes": size,
                    "modified": mtime,
                    "type": mime or "unknown"
                }
            except (PermissionError, FileNotFoundError):
                # Skip unreadable or transient files
                continue

if __name__ == "__main__":
    target = input("Enter directory to scan (leave blank for current): ").strip() or "."
    print(f"\nScanning: {os.path.abspath(target)}\n")
    print(f"{'File Path':60} {'Size (KB)':>12} {'Modified':>22} {'Type'}")
    print("-" * 110)

    for info in scan_directory(target):
        print(f"{info['path'][:58]:60} {info['size_bytes']/1024:12.2f} {info['modified']:>22} {info['type']}")

