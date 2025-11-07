from faker import Faker
from sqlite_db import cur, conn

fake = Faker()

for _ in range(4):
    name = fake.name()
    dob = fake.date_of_birth()
    email = fake.email()
    city = fake.city()
    cur.execute("INSERT INTO users(name, date_of_birth, email, city) VALUES (?, ?, ?, ?)", (name, dob, email, city))

conn.commit()
conn.close()