from flask import Blueprint, render_template, request
from models.Mood import Mood
from models.Weight import Weight

# Blueprintを作成
day_data_bp = Blueprint('day_data', __name__, url_prefix='/day_data')

@day_data_bp.route('/')
def day_data():
    # クエリパラメータから日付を取得
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('data')
    if day:
         record =Mood.get_or_none(Mood.day==day)
         mood=record.mood if record else "データがありません"
    else:
         mood="日付が指定されていません"
        
    weight = None
    
    if day:  
        # レコードを取得（存在しない場合は None を返す）
        record = Weight.get_or_none(Weight.day == day)

        if record:  # レコードが存在する場合
            weight = record.weight
        else:  # レコードが存在しない場合
            weight = None

        # Day_data.html にデータを渡す
    return render_template('Day_data.html', year = year, month = month, day = day, mood = mood, weight = weight )
