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
    print("Initializing database...")
    if not db.is_closed():  # 接続が開いている場合
        db.close()  # 接続を閉じる
        print("既存のデータベース接続を閉じました。")
    try:
        db.connect()  # 新たに接続を開く
        db.create_tables(MODELS, safe=True)
        print("データベースの初期化が完了しました。")
    except Exception as e:
        print(f"データベース初期化中にエラーが発生しました: {e}")