import os
from flask import Flask, render_template, request
import calendar
from datetime import datetime
from routes import blueprints
from models.__init__ import initialize_database
from models.Sleep import Sleep
from models.Home_sleep import Home_sleep
from models import ToDo
from models import Weight 

app = Flask(__name__)
app.secret_key = os.urandom(24)  # 24バイトのランダム文字列
# データベースの初期化
#initialize_database()

for blueprint in blueprints:
    app.register_blueprint(blueprint)

@app.route('/')
def index():
    # 現在の年と月を取得
    now = datetime.now()
    year = now.year
    month = now.month
    
    # カレンダーを作成
    cal = calendar.Calendar(firstweekday=6)
    month_days = cal.monthdayscalendar(year, month)
    #home.htmlに何かをを返したいのであれば、以下を編集すると良いかも


     # sleepグラフ用計算処理
    sleepdata = list()
  # ToDoを日付ごとにまとめる
    Atodo = {}
    Ctodo = {}
    for i in range(1, 32):
        try:
            today = datetime(year, month, i).date()
        except ValueError:
            continue  # 日付が無効な場合（例: 2月30日）、スキップする
        Atodo[i] = list(ToDo.select().where(ToDo.a_day == today))
        Ctodo[i] = list(ToDo.select().where(ToDo.c_day == today))
    
    #以下、wheightグラフを作成するためのコード
    days = []  
    weights = []        
    records = Weight.select().order_by(Weight.day.asc())
    for record in records:
        days.append(record.day)
        weights.append(record.weight)
        
    return render_template('home.html', year=year, month=month, month_days=month_days, days=days, Atodo=Atodo, Ctodo=Ctodo, weights=weights,sleepdata=sleepdata)

  
    

def list():
    # リスト初期化
    Home_sleep.delete().execute()
    # 各種データ取得
    sleeps = Sleep.select()
    #時間単位の睡眠時間
    sleeptime_h = {}
    calculate_sleeptime(sleeps,sleeptime_h)

      # sleeptime_hをhome_sleepテーブルに保存
    for sleep in sleeps:
        # sleep.date と sleeptime_h[sleep.date] が存在することを確認
        if sleep.date in sleeptime_h:
            Home_sleep.create(
                sleeptime=sleeptime_h[sleep.date],
                date=sleep.date,
            )

    # JSON変換用に辞書形式でデータを返す
    return [
        {"sleeptime": home_sleep.sleeptime, "date": home_sleep.date}
        for home_sleep in Home_sleep.select()
    ]

def calculate_sleeptime(sleeps,sleeptime_h):
    """
    HH:MMフォーマットの文字列を小数形式の時間に変換する関数
    :param sleeptime: str, HH:MM形式の睡眠時間
    :return: float, 小数形式の時間
    """
    fmt = "%H:%M"

     # 登録
    for sleep in sleeps:
        sleeptime_h[sleep.date] = 0
    
    for sleep in sleeps:
        sleeptime = sleep.sleeptime
        # 入力のフォーマットを検証
        print(sleeptime)
        if not validate_time_format(sleeptime, fmt):
            
            raise ValueError("フォーマットエラー: HH:MM形式で入力してください",sleeptime)

        # HH:MM形式を分に変換
        time_obj = datetime.strptime(sleeptime, fmt)
        hours = time_obj.hour
        minutes = time_obj.minute

        # 小数形式の時間を計算
        decimal_hours = hours + minutes / 60
        sleeptime_h[sleep.date]= round(decimal_hours, 2) # 小数点以下2桁で返す
 

def validate_time_format(time_str, fmt):
    """時刻文字列が指定のフォーマットに一致するか検証"""
    try:
        datetime.strptime(time_str, fmt)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)