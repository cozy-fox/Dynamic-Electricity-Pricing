from flask import Blueprint, render_template
from flask_login import login_required, current_user
import mysql.connector

mysqltest=False
mydb = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='qwertyhigh',
	database='ministry'
)
if(mysqltest):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM base")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

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