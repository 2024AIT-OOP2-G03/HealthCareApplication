from peewee import Model, CharField, DateField
from.db import db

class ToDo(Model):
    todo = CharField()
    a_day = DateField()
    c_day = DateField()

    class Meta:
        database = db