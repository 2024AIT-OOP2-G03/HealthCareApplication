from flask import Blueprint, render_template, request, redirect, url_for
from models.Weight import Weight

# Blueprint の定義
weight_bp = Blueprint('weight', __name__, url_prefix='/weight')

@weight_bp.route('/', methods=['GET', 'POST'])
def weight():
    # URL パラメータから 'data'（day）を取得
    day = request.args.get('data')

    # POST リクエストの処理
    if request.method == 'POST':
        # フォームデータから 'weight' を取得してデータベースに保存
        weight = request.form.get('weight')  
        Weight.create(day=day, weight=weight)
        return redirect(url_for('weight.weight', data=day))  # 'data' を再設定してリダイレクト
    
    # データベースからdayに対応するweight を取得
    if day:
        record = Weight.get_or_none(Weight.day == day)
        weight = record.weight if record else "データがありません"
    else:
        weight = "日付が指定されていません"

    # テンプレートをレンダリング
    return render_template('Weight.html', day=day, weight=weight)
