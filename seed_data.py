from faker import Faker

fake = Faker()

for _ in range(4):
    print(fake.name(), fake.date_of_birth(), fake.email(), fake.city())
