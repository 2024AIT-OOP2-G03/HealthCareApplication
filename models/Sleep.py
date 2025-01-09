from peewee import Model, IntegerField,TimeField
from.db import db

class ToDo(Model):
    wakeup = TimeField()
    gotobed = TimeField()
    sleeptime = IntegerField()

    class Meta:
        database = db