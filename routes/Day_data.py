from datetime import datetime
from flask import Blueprint, render_template, request
from models import Diary
from models.ToDo import ToDo
from models.Weight import Weight

# Blueprintを作成
day_data_bp = Blueprint('day_data', __name__, url_prefix='/day_data')

@day_data_bp.route('/')
def day_data():
    # クエリパラメータから日付を取得
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('data') 
    today = year + "-" + month + "-" + day
    # 追加日(選択した日)
    Today = datetime.strptime(today, "%Y-%m-%d").date()
    diary = None
    weight = None
    
    if day:
        record = Diary.get_or_none(Diary.day == day)

        if record:  #データが存在する場合
            diary = record.diary
        else:   #データが存在しない場合
            diary = "日記は未記入です"
           
        #この日に表示されるToDoを取得
        todo = ToDo.select().where((ToDo.a_day <= Today) & (Today <= ToDo.c_day))  

        # レコードを取得（存在しない場合は None を返す）
        record = Weight.get_or_none(Weight.day == day)

        if record:  # レコードが存在する場合
            weight = record.weight
        else:  # レコードが存在しない場合
            weight = None
    
    # Day_data.html にデータを渡す
    return render_template('Day_data.html', year=year, month=month, day=day, diary=diary, todo=todo, weight=weight )
