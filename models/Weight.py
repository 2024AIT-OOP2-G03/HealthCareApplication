from peewee import Model,IntegerField,FloatField
from .db import db

class Weight(Model):
    day = IntegerField()
    weight = FloatField()

    class Meta:
        database = db
        