# routes/__init__.py
from .Day_data import day_data_bp
from .Diary import diary_bp
from .Meal import meal_bp
from .ToDo import todo_bp
from .Weight import weight_bp
from .Mood import mood_bp
from .Sleep import sleep_bp

# Blueprint をリストにまとめる
blueprints = [
    day_data_bp,
    diary_bp,
    meal_bp,
    todo_bp,
    weight_bp,
    mood_bp,
    sleep_bp,
]
