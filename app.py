from flask import Flask, render_template
import calendar
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # 現在の年と月を取得
    now = datetime.now()
    year = now.year
    month = now.month

    # カレンダーを作成
    cal = calendar.Calendar(firstweekday=6)
    month_days = cal.monthdayscalendar(year, month)

    return render_template('test.html', year=year, month=month, month_days=month_days)

@app.route('/Day_data')
def contact():
    return render_template('Day_data.html')
if __name__ == '__main__':
    app.run(debug=True)