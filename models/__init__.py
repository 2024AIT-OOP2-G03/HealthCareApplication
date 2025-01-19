from peewee import SqliteDatabase
from .db import db
from .Diary import Diary
from.Mood import Mood
from .meal import Meal
from .ToDo import ToDo
from .Sleep import Sleep
from .Home_sleep import Home_sleep
from .Weight import Weight

MODELS = [
    Diary,
    Mood,
    Meal,
    ToDo,
    Sleep,
    Home_sleep,
    Weight
]

def initialize_database():
    db.connect()  # 新たに接続を開く
    db.create_tables(MODELS, safe=True)
    db.close()  # 接続を閉じる