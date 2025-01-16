from peewee import Model, IntegerField,DateField
from.db import db

class Home_sleep(Model):

    sleeptime = IntegerField()
    date = DateField()

    class Meta:
        database = db