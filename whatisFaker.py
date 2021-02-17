from faker import Faker
fake = Faker()
print(type(fake))
print(isinstance(fake, Faker))
print(type(Faker()))
print(fake.name())