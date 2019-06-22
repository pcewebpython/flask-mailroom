#!/usr/bin/env python3

import random
from model import db, Donor, Donation, User
from passlib.hash import pbkdf2_sha256


def main():
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

    User(name="admin", password=pbkdf2_sha256.hash("password")).save()
    User(name="doug", password=pbkdf2_sha256.hash("doug")).save()


if __name__ == "__main__":
    main()
