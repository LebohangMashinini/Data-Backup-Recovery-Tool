import sqlite3

conn = sqlite3.connect('seed_data.db')
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

conn = sqlite3.connect('data.db')
cur = conn.cursor()
cur.execute('SELECT * FROM users LIMIT 10')
for row in cur.fetchall():
    print(row)

conn.close()

