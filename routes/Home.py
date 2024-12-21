from flask import Blueprint, render_template ,request

# Blueprintを作成
home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/')
def day_data():
    # 日付を取得
    day = request.args.get('data')
    if day:
        # 日付をDay_data.htmlに渡す
        return render_template('Day_data.html', day = day)
