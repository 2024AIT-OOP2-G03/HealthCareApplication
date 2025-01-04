from peewee import SqliteDatabase
from .db import db
from .ToDo import ToDo
from .Weight import Weight

MODELS = [
    ToDo,
    Weight
]

def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()