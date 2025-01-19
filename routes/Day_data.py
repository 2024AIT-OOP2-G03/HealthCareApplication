from flask import Blueprint, render_template ,request
from models.Meal import Meal

# Blueprintを作成
day_data_bp = Blueprint('day_data', __name__, url_prefix='/day_data')

@day_data_bp.route('/')
def day_data():
    # 日付を取得
    day = request.args.get('data')


    if day:
        # レコードを取得（存在しない場合は None を返す）
        record = Meal.get_or_none(Meal.day == day)

        if record:  # レコードが存在する場合
            meal = record.meal
        else:  # レコードが存在しない場合
            meal = None

        # 日付をDay_data.htmlに渡す
        return render_template('Day_data.html', day = day, meal = meal)