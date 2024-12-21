from flask import Blueprint, render_template

# Blueprintを作成
home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/')
def day_data():
    return render_template('Day_data.html')