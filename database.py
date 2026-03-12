import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS matches(
INTEGER PRIMARY KEY AUTOINCREMENT,
League TEXT,
Team1 TEXT,
Team2 TEXT,
Match_date TEXT
)
""")

conn.commit()
conn.close()

print("Database Ready")