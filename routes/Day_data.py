from flask import Blueprint, render_template ,request
from models import Diary

# Blueprintを作成
day_data_bp = Blueprint('day_data', __name__, url_prefix='/day_data')

@day_data_bp.route('/')
def day_data():
    # 日付を取得
    day = request.args.get('data')
    diary = None

    if day:
        record = Diary.get_or_none(Diary.day == day)

        if record:  #データが存在する場合
            diary = record.diary
        else:   #データが存在しない場合
            diary = "日記は未記入です"

    # Day_data.htmlにデータを渡す
    return render_template('Day_data.html', day=day, diary=diary)