from peewee import SqliteDatabase
from .db import db
from.Weight import Weight
from.Diary import Diary

MODELS = [
    Weight,
    Diary,
]

def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()