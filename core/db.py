# core/db.py
import os
import sqlite3
from datetime import datetime

DB_PATH = os.path.join("data", "storage_sentinel.db")

def get_connection():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn

def initialize_db():
    conn = get_connection()
    cur = conn.cursor()

    # Create tables if not exists
    cur.execute("""
    CREATE TABLE IF NOT EXISTS snapshots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        snapshot_id INTEGER NOT NULL,
        path TEXT NOT NULL,
        size_bytes INTEGER,
        modified TEXT,
        type TEXT,
        FOREIGN KEY (snapshot_id) REFERENCES snapshots (id)
    )
    """)

    conn.commit()
    conn.close()

def insert_snapshot():
    """Insert a new snapshot record and return its ID."""
    conn = get_connection()
    cur = conn.cursor()
    timestamp = datetime.now().isoformat(timespec="seconds")
    cur.execute("INSERT INTO snapshots (timestamp) VALUES (?)", (timestamp,))
    conn.commit()
    snapshot_id = cur.lastrowid
    conn.close()
    return snapshot_id

def insert_file(snapshot_id, file_info):
    """Insert one file record linked to a snapshot."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO files (snapshot_id, path, size_bytes, modified, type)
        VALUES (?, ?, ?, ?, ?)
    """, (snapshot_id, file_info["path"], file_info["size_bytes"], file_info["modified"], file_info["type"]))
    conn.commit()
    conn.close()
