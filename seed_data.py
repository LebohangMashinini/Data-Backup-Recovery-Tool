import sqlite3
from faker import Faker

fake = Faker()

conn = sqlite3.connect('data.db')
cur = conn.cursor()

for _ in range(10):
    name = fake.name()
    dob = fake.date_of_birth()
    email = fake.email()
    city = fake.city()
    cur.execute(
        "INSERT INTO users(name, date_of_birth, email, city) VALUES (?, ?, ?, ?)",
        (name, dob, email, city)
    )

conn.commit()
conn.close()
print("Fake data inserted into database.")
