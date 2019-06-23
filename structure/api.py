from flask import Blueprint, render_template
from flask_login import login_required, current_user

api = Blueprint('api', __name__)

@api.route('/current')
def current():
    return render_template('current.html')

@api.route('/graph')
@login_required
def graph():
    return render_template('graph.html', name=current_user.name)

@api.route('/bill')
@login_required
def bill():
    return render_template('bill.html', name=current_user.name)