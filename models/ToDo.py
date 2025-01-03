from peewee import Model, CharField, DateField
from.db import db

class ToDo(Model):
    todo = CharField()
    c_day = DateField()

    class Meta:
        database = db