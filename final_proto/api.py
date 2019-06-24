from flask import Blueprint, render_template,jsonify
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

def extract_time(sector):
    mycursor = mydb.cursor()
    c=0
    store=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,3):
        for j in range (0,10):
            check= str(i)+str(j)
            if(check == '25'):
                break
            else:
                mycursor.execute(f"SELECT * FROM base WHERE SECTOR= '{sector}' AND TIME={check};")
                myresult = mycursor.fetchall()
                for x in myresult:
                    store[c]=store[c]+x[3]/100
                c+=1
    return store[:-1]

def extract_day(sector):
    mycursor = mydb.cursor()
    c=0
    store=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,3):
        for j in range (0,10):
            check= str(i)+str(j)
            if(check == '25'):
                break
            else:
                mycursor.execute(f"SELECT * FROM base WHERE SECTOR= '{sector}' AND TIME={check};")
                myresult = mycursor.fetchall()
                for x in myresult:
                    store[c]=store[c]+x[3]/100
                c+=1
    return store[:-1]

@api.route('/current/<string:sector>/<int:json>')
@api.route('/current/<string:sector>')
@api.route('/current')
def current(sector='AA',json=0):
    store=extract_time(sector)
    if(json==1):
        return jsonify(store)
    return render_template('current.html',store=store,sector=sector)

@api.route('/bar')
def bar():
    store=extract_day('AA')
    store2=extract_day('AB')
    return render_template('bar.html',store=store,store2=store2)

@api.route('/rate')
def rate():
    return render_template('rate.html')

@api.route('/graph')
@login_required
def graph():
    return render_template('graph.html', name=current_user.name)

@api.route('/bill')
@login_required
def bill():
    return render_template('bill.html', name=current_user.name)