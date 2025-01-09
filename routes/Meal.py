from flask import Blueprint,render_template,request,redirect,url_for
from models.meal import Meal

meal_bp = Blueprint('meal',__name__,url_prefix='/meals')

@meal_bp.route('/', methods=['GET', 'POST'])
def meal():
    # データ取得
    day = request.args.get('data')
    # POSTで送られてきたデータは登録
    if request.method == 'POST':
        name = request.form.get('name')
        calorie = request.form.get('calorie')
        Meal.create(day=day, name=name, calorie=calorie)
        return redirect(url_for('day_data.day_data', data=day))
    
    if day:
        record = Meal.get_or_none(Meal.day == day)
        meal = record.name if record else "データがありません"
    else:
        meal = "日付が指定されていません"

    return render_template('meal.html', day=day,meal=meal)