from flask import Blueprint, render_template, request

todo_bp = Blueprint ('todo',__name__, url_prefix='/todo')

@todo_bp.route('/')
def todo():
    return render_template('ToDo.html')