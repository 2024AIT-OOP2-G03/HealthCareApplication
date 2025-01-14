from flask import Blueprint, render_template, request, redirect, url_for
from models.Weight import Weight

weight_bp = Blueprint('weight', __name__, url_prefix='/weight')

@weight_bp.route('/', methods=['GET', 'POST'])
def weight():
    # 日付を取得してdayに保存
    day = request.args.get('data')

    # POSTリクエストの処理
    if request.method == 'POST':
        # 入力から weight を取得
        weight = request.form.get('weight')

        if day:
            # データベースで該当する日付のレコードを取得
            record = Weight.get_or_none(Weight.day == day)
            if record:
                # レコードが存在する場合は更新
                record.weight = weight
                record.save()
            else:
                # レコードが存在しない場合は新規作成
                Weight.create(day=day, weight=weight)
        return redirect(url_for('day_data.day_data', data=day))

    # データベースからdayに対応するweight を取得
    if day:
        record = Weight.get_or_none(Weight.day == day)
        weight = record.weight if record else "データがありません"
    else:
        weight = "日付が指定されていません"

    return render_template('Weight.html', day=day, weight=weight)
