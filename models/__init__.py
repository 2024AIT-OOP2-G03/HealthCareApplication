from peewee import SqliteDatabase
from .db import db
from .ToDo import ToDo
from .Weight import Weight
from .meal import Meal

MODELS = [
    ToDo,
    Weight,
    Meal
]

def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()