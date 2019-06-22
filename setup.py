#!/usr/bin/env python3
""" Generates a new database for Mailroom Flask App """
# pylint: disable=E0401

import random
from passlib.hash import pbkdf2_sha256
from model import DB, Donor, Donation, User


def main():
    """ We Wuz Main """
    DB.drop_tables([Donor, Donation, User])
    DB.create_tables([Donor, Donation, User])

    alice = Donor(name="Alice")
    alice.save()

    bob = Donor(name="Bob")
    bob.save()

    charlie = Donor(name="Charlie")
    charlie.save()

    donors = [alice, bob, charlie]

    for _ in range(30):
        Donation(donor=random.choice(donors), value=random.randint(100, 10000)).save()

    User(name="admin", password=pbkdf2_sha256.hash("password")).save()
    User(name="doug", password=pbkdf2_sha256.hash("doug")).save()


if __name__ == "__main__":
    main()
