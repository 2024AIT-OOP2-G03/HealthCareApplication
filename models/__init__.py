from peewee import SqliteDatabase
from .db import db
from.Mood import Mood
from .ToDo import ToDo
from .Weight import Weight
from .Diary import Diary
from .Sleep import Sleep

MODELS = [
    Mood,
    ToDo,
    Weight,
    Diary,
    Sleep
]

def initialize_database():
    if not db.is_closed():  # 接続が開いている場合
        db.close()  # 接続を閉じる
        print("既存のデータベース接続を閉じました。")
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()