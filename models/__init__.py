from peewee import SqliteDatabase
from .db import db
from.Mood import Mood
from .ToDo import ToDo
from .Weight import Weight
from .Sleep import Sleep

MODELS = [
    Mood,
    ToDo,
    Weight,
    Sleep
]

def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()