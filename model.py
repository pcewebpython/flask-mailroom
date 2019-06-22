# pylint: disable=E0401, R0903, C0111
""" Class definitions for Mailroom Flask App """

import os
from peewee import Model, CharField, IntegerField, ForeignKeyField
from playhouse.db_url import connect


DB = connect(os.environ.get("DATABASE_URL", "sqlite:///my_database.db"))


class Donor(Model):
    """ Donor class, inherits from peewee.Model """

    name = CharField(max_length=255, unique=True)

    class Meta:
        database = DB


class Donation(Model):
    """ Donation class, inherits from peewee.Model """

    value = IntegerField()
    donor = ForeignKeyField(model=Donor, null=True, backref="donations")

    class Meta:
        database = DB


class User(Model):
    """ User class, inherits from peewee.Model """

    name = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)

    class Meta:
        database = DB
