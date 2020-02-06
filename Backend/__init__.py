#  set FLASK_APP=__init__.py
#  set APP_SETTINGS=config.cfg
#  FLASK run

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
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

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_envvar('APP_SETTINGS')

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app