# The setup script
import random
from passlib.hash import pbkdf2_sha256

from model import db, Donor, Donation, User

db.connect()

# This line will allow you "upgrade" an existing database by
# dropping all existing tables from it.
db.drop_tables([Donor, Donation, User])

db.create_tables([Donor, Donation, User])

alice = Donor(name="Alice")
alice.save()

bob = Donor(name="Bob")
bob.save()

charlie = Donor(name="Charlie")
charlie.save()

donors = [alice, bob, charlie]

for x in range(30):
    Donation(donor=random.choice(donors), value=random.randint(100, 10000)).save()

admin = User(name='admin', password=pbkdf2_sha256.hash("password123"))
guest = User(name='guest', password=pbkdf2_sha256.hash("guest"))
users = [admin, guest]

for x in users:
    x.save()
