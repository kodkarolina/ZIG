from App import app

#=====================SQLAlchemy DataBase==============================
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy(App)

#=====================MySQL DataBase==============================
from flaskext.mysql import MySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'BazaDanychYolo94'
app.config['MYSQL_DATABASE_DB'] = 'rcp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#MySQL init
mysql.init_app(app)


#===================== API ==============================
from flask_restful import Api
api = Api(app)