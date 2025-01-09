from flask import Blueprint, render_template, request, redirect, url_for
from models.Weight import Weight

weight_bp = Blueprint('weight', __name__, url_prefix='/weight')

@weight_bp.route('/', methods=['GET', 'POST'])
def weight():
    # dataを取得してdayに保存
    day = request.args.get('data')

    # POSTリクエストの処理
    if request.method == 'POST':
        
        #入力からweightを取得してデータベースに保存
        weight = request.form.get('weight')  
        Weight.create(day=day, weight=weight)
        return redirect(url_for('day_data.day_data', data=day)) 
    
    # データベースからdayに対応するweightを取得
    if day:
        record = Weight.get_or_none(Weight.day == day)
        weight = record.weight if record else "データがありません"
    else:
        weight = "日付が指定されていません"
        
    return render_template('Weight.html', day=day, weight=weight)
