from flask import Blueprint,render_template,request

meal_bp = Blueprint('meal',__name__,url_prefix='/meal')

@meal_bp.route('/')
def meal():
    return render_template('Meal.html')
