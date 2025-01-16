from flask import Blueprint, render_template, request, redirect, url_for
from models import Sleep

sleep_bp = Blueprint ('sleep',__name__, url_prefix='/sleep')

@sleep_bp.route('/')
def sleep():
    # 日付を取得
    day = request.args.get('day')
    sleeps = Sleep.select().where(Sleep.date.day >= int(day))
    return render_template('sleep_list.html', title='睡眠データ', items = sleeps, day = day)

@sleep_bp.route('/edit/<int:sleep_id>', methods=['GET', 'POST'])
def edit():
    # 日付を取得
    day = request.args.get('day')
    sleep = Sleep.get_or_none(Sleep.id == sleep_id)

    if not sleep:# データが見つからなければ
        Sleep.create(wakeup="00:00", gotobed="00:00", sleeptime=0, date=day)

    if request.method == 'POST':
        sleep.wakeup = request.form['wakeup']
        sleep.gotobed = request.form['gotobed']
        sleep.sleeptime = calculate_sleeptime(sleep.wakeup, sleep.gotobed)  # 睡眠時間を計算する関数

        sleep.save()
        return redirect(url_for('sleep.sleep',day = day))
    
    return render_template('sleep_edit.html',sleep=sleep,day = day)

def calculate_sleeptime(wakeup, gotobed):
    """睡眠時間を計算する関数（例: 時間を分として計算）"""
    from datetime import datetime

    fmt = "%H:%M"
    wakeup_time = datetime.strptime(wakeup, fmt)
    gotobed_time = datetime.strptime(gotobed, fmt)
    delta = (wakeup_time - gotobed_time).total_seconds() / 3600  # 時間差を計算
    if delta < 0:  # 翌日を跨ぐ場合
        delta += 24
    return int(delta)
