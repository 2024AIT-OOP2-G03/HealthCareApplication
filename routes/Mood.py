from flask import Blueprint, render_template, request

mood_bp = Blueprint ('mood',__name__, url_prefix='/mood')

@mood_bp.route('/')
def mood():
    return render_template('Mood.html')