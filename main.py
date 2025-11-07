import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()
cur.execute('SELECT * FROM users LIMIT 10')
for row in cur.fetchall():
    print(row)
conn.close()
