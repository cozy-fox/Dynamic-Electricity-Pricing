# main.py

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

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)