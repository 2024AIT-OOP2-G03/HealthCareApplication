from flask import Blueprint, render_template, request, redirect, url_for
from models import ToDo

todo_bp = Blueprint ('todo',__name__, url_prefix='/todo')

@todo_bp.route('/')
def todo():
    # 日付を取得
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    # データ取得
    todoS = ToDo.select().where((ToDo.c_day.year > int(year)) | ((ToDo.c_day.month > int(month)) | (ToDo.c_day.day >= int(day))))
    return render_template('ToDo_list.html', title='ToDoリスト', items = todoS, year=year, month=month, day=day)

@todo_bp.route('/add', methods=['GET', 'POST'])
def add():
    # 日付を取得
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')

    if request.method == 'POST':
        todo = request.form['todo']
        c_day = request.form['c_day']
        ToDo.create(todo=todo, c_day=c_day)
        return redirect(url_for('todo.todo', year=year, month=month, day=day))
    
    return render_template('ToDo_add.html', year=year, month=month, day=day)

@todo_bp.route('/edit/<int:ToDo_id>', methods=['GET', 'POST'])
def edit(ToDo_id):
    # 日付を取得
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')

    todo = ToDo.get_or_none(ToDo.id == ToDo_id)
    if not todo:
        return redirect(url_for('todo.todo', year=year, month=month, day=day))
    
    if request.method == 'POST':
        todo.todo = request.form['todo']
        todo.c_day = request.form['c_day']
        todo.save()
        return redirect(url_for('todo.todo', year=year, month=month, day=day))
    
    return render_template('ToDo_edit.html', todo=todo, year=year, month=month, day=day)

@todo_bp.route('/completed/<int:ToDo_id>', methods=['GET', 'POST'])
def completed(ToDo_id):
    # 日付を取得
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')

    todo = ToDo.get_or_none(ToDo.id == ToDo_id)
    if not todo:
        return redirect(url_for('todo.todo', year=year, month=month, day=day))
    
    if request.method == 'POST':
        todo.delete_instance()  # データベースから削除
        return redirect(url_for('todo.todo', year=year, month=month, day=day))
    
    return render_template('ToDo_completed.html', todo=todo, year=year, month=month, day=day)