from peewee import SqliteDatabase
from .db import db
from.Mood import Mood
from .ToDo import ToDo
from .Weight import Weight
from .Diary import Diary
from .Sleep import Sleep
from .Home_sleep import Home_sleep

MODELS = [
    Mood,
    ToDo,
    Weight,
    Sleep,
    Home_sleep,
    Diary,

]

def initialize_database():
    db.connect()  # 新たに接続を開く
    db.create_tables(MODELS, safe=True)
    db.close()  # 接続を閉じる