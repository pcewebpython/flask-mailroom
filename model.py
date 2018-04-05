import os

from peewee import Model, CharField, IntegerField, ForeignKeyField
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))

class Donor(Model):
    name = CharField(max_length=255, unique=True)

    class Meta:
        database = db

class Donation(Model):
    value = IntegerField()
    donor = ForeignKeyField(Donor, backref='donations')

    class Meta:
        database = db

