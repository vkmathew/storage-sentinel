# core/stats.py
import sqlite3
import os

DB_PATH = os.path.join("data", "storage_sentinel.db")

def get_connection():
    if not os.path.exists(DB_PATH):
        print("No database found. Run a snapshot first.")
        exit(1)
    return sqlite3.connect(DB_PATH)

def query_db():
    conn = get_connection()
    cur = conn.cursor()

    # Total snapshots
    cur.execute("SELECT COUNT(*), MAX(timestamp) FROM snapshots")
    snapshot_count, latest_timestamp = cur.fetchone()

    # Total files
    cur.execute("SELECT COUNT(*), SUM(size_bytes) FROM files")
    total_files, total_size = cur.fetchone()
    total_size_mb = (total_size or 0) / (1024 * 1024)

    # Average file size
    avg_size = (total_size / total_files) if total_files else 0

    # Top file types by total size
    cur.execute("""
        SELECT type, COUNT(*) as count, SUM(size_bytes) as total_bytes
        FROM files
        GROUP BY type
        ORDER BY total_bytes DESC
        LIMIT 5
    """)
    top_types = cur.fetchall()

    conn.close()
    return {
        "snapshot_count": snapshot_count,
        "latest_timestamp": latest_timestamp,
        "total_files": total_files,
        "total_size_mb": total_size_mb,
        "avg_size": avg_size,
        "top_types": top_types
    }

def print_report(stats):
    print("\n📊 Storage Sentinel Report")
    print("=" * 40)
    print(f"Snapshots captured : {stats['snapshot_count']}")
    print(f"Last snapshot time : {stats['latest_timestamp']}")
    print(f"Total files tracked : {stats['total_files']}")
    print(f"Total size stored   : {stats['total_size_mb']:.2f} MB")
    print(f"Average file size   : {stats['avg_size']:.1f} bytes\n")

    print("Top file types by total size:")
    if not stats["top_types"]:
        print("  (No data yet)")
    else:
        for filetype, count, total_bytes in stats["top_types"]:
            mb = (total_bytes or 0) / (1024 * 1024)
            print(f"  {filetype or '(unknown)':15} → {count:4} files, {mb:8.2f} MB")

if __name__ == "__main__":
    stats = query_db()
    print_report(stats)
