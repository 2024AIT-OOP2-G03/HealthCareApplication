import os
from flask import Flask, render_template, request
from models import db, initialize_database
import calendar
from datetime import datetime
from routes import blueprints
from models import initialize_database
from models.ToDo import ToDo

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
    
    return render_template('home.html', year=year, month=month, month_days=month_days, Atodo=Atodo, Ctodo=Ctodo)


    
if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)