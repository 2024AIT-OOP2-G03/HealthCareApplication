from flask import Blueprint, render_template, request

weight_bp = Blueprint ('weight',__name__, url_prefix='/weight')

@weight_bp.route('/')
def weight():
    return render_template('Weight.html')