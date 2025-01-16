from flask import Blueprint, render_template, request, redirect, url_for
from models import Sleep

sleep_bp = Blueprint ('sleep',__name__, url_prefix='/sleep')

@sleep_bp.route('/')
def sleep():
    # 日付を取得（指定変数名がdayだからわかりにくいが中身は月日でdateと同じ型）
    day = request.args.get('day')
    sleeps = Sleep.select().where(Sleep.date >= int(day))
    return render_template('sleep_list.html', title='睡眠データ', items = sleeps, day = day)

@sleep_bp.route('/edit', methods=['GET', 'POST'])
def edit():
    # 日付を取得
    day = request.args.get('day')
    sleep = Sleep.get_or_none(Sleep.date == day)

    if not sleep:# データが見つからなければ
        Sleep.create(wakeup="00:00", gotobed="00:00", sleeptime=0, date=day)

    if request.method == 'POST':
        sleep.wakeup = del_second(request.form['wakeup']) #読み込んでsを消去
        sleep.gotobed = del_second(request.form['gotobed'])
        sleep.sleeptime = calculate_sleeptime(sleep.wakeup, sleep.gotobed)  # 睡眠時間を計算する関数
        
        sleep.save()
        # ただしデータベースがそもそもTimefieldのため、sは消えてくれない
        # html側でsを削除して表示する
        return redirect(url_for('sleep.sleep',day = day))
    
    return render_template('sleep_edit.html',sleep=sleep,day = day)

def calculate_sleeptime(wakeup, gotobed):
    """睡眠時間を計算する関数（例: 時間を分として計算）"""
    from datetime import datetime 

    fmt="%H:%M"
    if not validate_time_format(wakeup, fmt) or not validate_time_format(gotobed, fmt):
        raise ValueError("フォーマットエラーだよ")

    wakeup_time = datetime.strptime(wakeup, fmt)
    gotobed_time = datetime.strptime(gotobed, fmt)
    delta = (wakeup_time - gotobed_time).total_seconds()   # 秒単位で時間差を計算
    if delta < 0:  # 翌日を跨ぐ場合
        delta += 24*3600

     # 時間と分に変換
    hours = int(delta // 3600)  # 時間
    minutes = int((delta % 3600) // 60)  # 分

    # f文字列を使用
    formatted_hours = f"{hours:02}"
    formatted_minutes = f"{minutes:02}"


    return f"{formatted_hours}:{formatted_minutes}"

def validate_time_format(time_str, fmt="%H:%M"):
    """時刻フォーマットを検証"""
    from datetime import datetime
    try:
        datetime.strptime(time_str, fmt)
        return True
    except ValueError:
        return False


def del_second(whenSleep): #sを消す

    fmt = "%H:%M" # フォーマット
    # wakeup,gotobednには描画含まれている（フォームにはないけど）から削除する
    whenSleep_fmt = whenSleep.split(':')[0] + ':' + whenSleep.split(':')[1]  
    return whenSleep_fmt
