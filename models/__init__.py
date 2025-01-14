from peewee import SqliteDatabase
from .db import db
from models.Weight import Weight
from.Mood import Mood

MODELS = [
    Weight,
    Mood
]

def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()