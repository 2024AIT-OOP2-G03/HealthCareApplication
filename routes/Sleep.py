from flask import Blueprint, render_template, request

sleep_bp = Blueprint ('sleep',__name__, url_prefix='/sleep')

@sleep_bp.route('/')
def sleep():
    return render_template('Sleep.html')