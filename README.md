# Storage Sentinel

**Storage Sentinel** is a modular, Python-based local storage monitoring tool that scans your directories, tracks file metadata over time, stores the data in SQLite, and provides interactive reports — all from a single command-line interface (CLI).

---

##  Features

✅ Scan directories and capture file statistics (size, modified time, type)  
✅ Store scan results in a persistent SQLite database  
✅ Compare snapshots to identify added, removed, or modified files  
✅ Generate visual reports of total files, size, and top file types  
✅ Run everything from one unified interactive menu  

---

##  Demo

### Launch Menu

python run.py

**Example output:**
╔════════════════════════════════════════╗
║ STORAGE SENTINEL MENU ║
╠════════════════════════════════════════╣
║ 1. Take Snapshot ║
║ 2. Compare Latest Snapshots ║
║ 3. Show Stats Report ║
║ 4. Exit ║
╚════════════════════════════════════════╝
Enter choice:

---

### Stats Report Example

After choosing option 3 (“Show Stats Report”):

📊 Storage Sentinel Report

Snapshots captured : 2
Last snapshot time : 2025-10-30T23:45:47
Total files tracked : 131
Total size stored : 0.18 MB
Average file size : 1410.8 bytes

Top file types by total size:
unknown → 100 files, 0.12 MB
application/x-python-code → 11 files, 0.02 MB
text/csv → 6 files, 0.02 MB
text/x-python → 12 files, 0.02 MB
text/markdown → 2 files, 0.00 MB


---

## 🧩 Project Architecture

storage-sentinel/
│
├── core/
│ ├── init.py
│ ├── scanner.py → walks directories, collects file metadata
│ ├── snapshot.py → saves snapshot data to SQLite
│ ├── compare.py → compares snapshots for changes
│ ├── db.py → handles SQLite connection and schema
│ └── stats.py → generates analytical reports
│
├── data/
│ ├── storage_sentinel.db → SQLite database
│ ├── snapshot_*.csv → CSV snapshots (legacy)
│ └── sentinel.log → (future) log file for actions
│
├── run.py → interactive CLI launcher
└── README.md




---

## ⚙️ Requirements

- **Python 3.8+** (tested on 3.14)
- No external dependencies required for basic features
- Optional (for Day 8+): `colorama` for colored output

---

## 🧩 How to Run

Clone the repo:

```bash
git clone https://github.com/vkmathew/storage-sentinel.git
cd storage-sentinel

Run the interactive menu:
python run.py
Take a snapshot, view stats, or compare snapshots — all within the same interface.