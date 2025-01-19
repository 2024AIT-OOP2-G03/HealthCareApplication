from flask import Blueprint,render_template,request,redirect,url_for
from models import Meal

meal_bp = Blueprint('meal',__name__,url_prefix='/meal')

@meal_bp.route('/')
def meal():
    # 日付を取得
    day = request.args.get('day')
    meals = Meal.select().where(Meal.day == day)
    return render_template('Meal_list.html', title='食べたもの', items = meals, day = day)

@meal_bp.route('/add', methods=['GET', 'POST'])
def add():
    # 日付を取得
    day = request.args.get('day')
    if request.method == 'POST':
        meal = request.form.get('meal')
        calorie = request.form.get('calorie')
        Meal.create(meal=meal, calorie=calorie, day=day)
        return redirect(url_for('meal.meal',day = day))
    
    return render_template('Meal_add.html',day = day)

@meal_bp.route('/edit/<int:Meal_id>/<string:day>', methods=['GET', 'POST'])
def edit(Meal_id, day):
    # 日付を取得
    day = request.args.get('day')

    meal = Meal.get_or_none(Meal.id == Meal_id)
    if not meal:
        return redirect(url_for('meal.meal',day = day))
    
    if request.method == 'POST':
        meal.meal = request.form['meal']
        meal.calorie = request.form['calorie']
        meal.save()
        return redirect(url_for('meal.meal',day=day))
    
    return render_template('meal_edit.html', meal=meal, day=day)