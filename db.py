import sqlite3
from datetime import date

DB_NAME = "habits.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_name TEXT NOT NULL,
            status TEXT NOT NULL,
            log_date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_log(habit_name, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO habit_logs (habit_name, status, log_date) VALUES (?, ?, ?)",
        (habit_name.lower().strip(), status.lower().strip(), str(date.today()))
    )
    conn.commit()
    conn.close()

def get_logs(habit_name=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    if habit_name:
        cursor.execute(
            "SELECT habit_name, status, log_date FROM habit_logs WHERE habit_name = ? ORDER BY log_date",
            (habit_name.lower().strip(),)
        )
    else:
        cursor.execute("SELECT habit_name, status, log_date FROM habit_logs ORDER BY log_date")
    rows = cursor.fetchall()
    conn.close()
    return rows