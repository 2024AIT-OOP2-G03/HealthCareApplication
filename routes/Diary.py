from flask import Blueprint, render_template, request, redirect, url_for
from models import Diary

diary_bp = Blueprint('diary',__name__, url_prefix='/diary')

@diary_bp.route('/', methods=['GET', 'POST'])
def diary():
    # 日付を取得
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')

    if request.method == 'POST':
        #入力からdiaryを取得
        diary = request.form['diary']

        if day:
            # データ取得
            record = Diary.get_or_none(Diary.day == day)
        
            try:
                if record:
                    # 更新処理
                    record.diary = diary
                    record.save()
                else:
                    # 新規作成
                    Diary.create(day=day, diary=diary)
            except Exception as e:
                print(f"日記の保存に失敗しました: {e}")
                return render_template('day_data.day_data', year=year, month=month, data=day)

        return redirect(url_for('day_data.day_data', year=year, month=month, data=day))
    else:
        if day:
            record = Diary.get_or_none(Diary.day == day)
            diary = record.diary if record else "データがありません"
        else:
            diary = "日付が指定されていません"

    return render_template('diary.html', day=day, diary=diary)
