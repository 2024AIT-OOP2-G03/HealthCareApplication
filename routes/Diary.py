from flask import Blueprint, render_template, request
from models import Diary

diary_bp = Blueprint('diary',__name__, url_prefix='/diary')

@diary_bp.route('/')
def diary():
    # 日付を取得
    day = request.args.get('day')
    # データ取得
    diarys = Diary.select().where(Diary.c_day.day >= int(day))
    return render_template('Diary.html', title='日記', items = diarys, day = day)