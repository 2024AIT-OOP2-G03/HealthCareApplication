from peewee import SqliteDatabase
from .db import db
from .ToDo import ToDo
from .Weight import Weight
from .Diary import Diary
from .Sleep import Sleep

MODELS = [
    ToDo,
    Weight,
    Diary,
    Sleep
]

def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()