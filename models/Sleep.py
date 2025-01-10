from peewee import Model, IntegerField,TimeField,DateField
from.db import db

class Sleep(Model):
    wakeup = TimeField()
    gotobed = TimeField()
    sleeptime = IntegerField()
    date = DateField()

    class Meta:
        database = db