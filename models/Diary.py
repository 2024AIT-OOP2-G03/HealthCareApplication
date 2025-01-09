from peewee import Model, IntegerField
from .db import db

class Diary(Model):
    day = IntegerField()

    class Meta:
        database = db