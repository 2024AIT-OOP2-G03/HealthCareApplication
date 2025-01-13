from peewee import Model, IntegerField, CharField
from .db import db

class Diary(Model):
    day = IntegerField()
    diary = CharField()

    class Meta:
        database = db