from flask import Flask, render_template, request
from models import initialize_database
import calendar
from datetime import datetime
from routes import blueprints
from models.__init__ import initialize_database

app = Flask(__name__)

# データベースの初期化
initialize_database()

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

    return render_template('home.html', year=year, month=month, month_days=month_days)


    
if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)