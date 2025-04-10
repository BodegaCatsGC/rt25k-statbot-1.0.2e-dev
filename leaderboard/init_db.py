import sqlite3

def init_db():
    conn = sqlite3.connect("leaderboard.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            points INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()