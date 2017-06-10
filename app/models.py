from ZIG.app import app
from App.config import DB_USER
from App.config import DB_PWD
from App.config import DB_NAME
from App.config import DB_HOST

#=====================SQLAlchemy DataBase==============================
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

#=====================MySQL DataBase==============================
from flaskext.mysql import MySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = DB_USER
app.config['MYSQL_DATABASE_PASSWORD'] = DB_PWD
app.config['MYSQL_DATABASE_DB'] = DB_NAME
app.config['MYSQL_DATABASE_HOST'] = DB_HOST
#MySQL init
mysql.init_app(app)


#===================== API ==============================
from flask_restful import Api
api = Api(app)