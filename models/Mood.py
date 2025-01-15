from peewee import Model, CharField, SqliteDatabase,IntegerField
from .db import db

class Mood(Model):
    mood = CharField()
    day=IntegerField()

    class Meta:
        database = db