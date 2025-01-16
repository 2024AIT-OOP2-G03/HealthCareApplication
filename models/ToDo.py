from peewee import Model, CharField, DateField
from.db import db

class ToDo(Model):
    todo = CharField()
    a_day = DateField() #追加日
    c_day = DateField() #締切日

    class Meta:
        database = db