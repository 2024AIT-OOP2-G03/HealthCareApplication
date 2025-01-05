from flask import Blueprint, render_template, request, redirect, url_for
from models.Weight import Weight

weight_bp = Blueprint('weight', __name__, url_prefix='/weight')

@weight_bp.route('/', methods=['GET', 'POST'])
def weight():
    day = request.args.get('data')
    
    if request.method == 'POST':
        weight = request.form.get('weight')  
        Weight.create(day=day, weight=weight)
        return redirect(url_for('weight.weight',data = day))
    
    return render_template('Weight.html', day = day)
