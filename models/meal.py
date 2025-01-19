from peewee import Model, CharField, IntegerField
from .db import db

class Meal(Model):
    meal = CharField()
    calorie = IntegerField()
    day = IntegerField()

    class Meta:
        database = db