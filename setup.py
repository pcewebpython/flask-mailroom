import random

from model import db, Donor, Donation,Login

db.connect()

# This line will allow you "upgrade" an existing database by
# dropping all existing tables from it.
db.drop_tables([Donor, Donation,Login])

db.create_tables([Donor, Donation,Login])

user = Login(username='admin',password='123456')
user.save()

alice = Donor(name="Alice")
alice.save()

bob = Donor(name="Bob")
bob.save()

charlie = Donor(name="Charlie")
charlie.save()

donors = [alice, bob, charlie]

for x in range(30):
    Donation(donor=random.choice(donors), value=random.randint(100, 10000)).save()

