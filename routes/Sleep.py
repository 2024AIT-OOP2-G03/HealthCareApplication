from flask import Blueprint, render_template, request, redirect, url_for
from models import Sleep

sleep_bp = Blueprint ('sleep',__name__, url_prefix='/sleep')

@sleep_bp.route('/')
def sleep():
    # 日付を取得
    day = request.args.get('day')
    # データ取得
    sleeps = Sleep.select().where(Sleep.c_day.day >= int(day))
    return render_template('sleep_list.html', title='睡眠データ', items = sleeps, day = day)

@sleep_bp.route('/edit', methods=['GET', 'POST'])
def add():
    # 日付を取得
    day = request.args.get('day')
    if request.method == 'POST':
        wakeup = request.form['wakeup']
        gotobed = request.form['gotobed']
        ToDo.create(todo=todo, c_day=c_day)
        return redirect(url_for('todo.todo',day = day))
    
    return render_template('sleep_edit.html',day = day)
