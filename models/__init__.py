from peewee import SqliteDatabase
from .db import db
from .ToDo import ToDo
from .Weight import Weight
from .Sleep import Sleep
from .Home_sleep import Home_sleep

MODELS = [
    ToDo,
    Weight,
    Sleep,
    Home_sleep
]

def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()