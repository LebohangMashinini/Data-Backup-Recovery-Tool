import sqlite3

def create_db():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date_of_birth TEXT,
        email TEXT,
        city TEXT 
    )
    ''')
    conn.commit()
    conn.close()
    print("Database and table created.")

if __name__ == "__main__":
    create_db()
