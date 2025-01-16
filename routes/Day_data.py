from datetime import datetime
from flask import Blueprint, render_template, request
from models import Diary
from models.Mood import Mood
from models.ToDo import ToDo
from models.Weight import Weight

# Blueprintを作成
day_data_bp = Blueprint('day_data', __name__, url_prefix='/day_data')

@day_data_bp.route('/')
def day_data():
    # 現在の年と月を取得
    now = datetime.now()
    year = now.year
    month = now.month
    # クエリパラメータから日付を取得
    day = request.args.get('data') 
    Today = datetime(year, month, int(day)).date()
    diary = None
    weight = None
    
    if day:
        record = Diary.get_or_none(Diary.day == day)

        if record:  #データが存在する場合
            diary = record.diary
        else:   #データが存在しない場合
            diary = "日記は未記入です"
        
        record =Mood.get_or_none(Mood.day==day)
        mood=record.mood if record else "データがありません"
        
        #この日に表示されるToDoを取得
        todo = ToDo.select().where((ToDo.a_day <= Today) & (Today <= ToDo.c_day))  

        # レコードを取得（存在しない場合は None を返す）
        record = Weight.get_or_none(Weight.day == day)

        if record:  # レコードが存在する場合
            weight = record.weight
        else:  # レコードが存在しない場合
            weight = None
    
    # Day_data.html にデータを渡す
    return render_template('Day_data.html', year=year, month=month, day=day, diary=diary, mood=mood, todo=todo, weight=weight )
