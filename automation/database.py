import sqlite3

DB_FILE = "instagram_accounts.db"

def init_db():
    """Initializes the database for storing Instagram accounts."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_account(username, password):
    """Adds an Instagram account to the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO accounts (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def get_accounts():
    """Retrieves all Instagram accounts."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM accounts")
    accounts = cursor.fetchall()
    conn.close()
    return accounts
