from flask import Blueprint, render_template, request

diary_bp = Blueprint('diary',__name__, url_prefix='/diary')

@diary_bp.route('/')
def diary():
    return render_template('Diary.html')