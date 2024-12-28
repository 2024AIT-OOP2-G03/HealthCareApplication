from peewee import Model, IntegerField
from .db import db
#データベース構築中
class Customer(Model):
    weight = IntegerField()
    day = IntegerField()

    class Meta:
        database = db