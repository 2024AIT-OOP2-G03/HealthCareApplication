from flask import Blueprint, render_template ,request
from models.Mood import Mood

# Blueprintを作成
day_data_bp = Blueprint('day_data', __name__, url_prefix='/day_data')

@day_data_bp.route('/')
def day_data():
    # 日付を取得
    day = request.args.get('data')
    if day:
         record =Mood.get_or_none(Mood.day==day)
         mood=record.mood if record else "データがありません"
    else:
         mood="日付が指定されていません"

        # 日付をDay_data.htmlに渡す
    return render_template('Day_data.html', day = day,mood=mood)
