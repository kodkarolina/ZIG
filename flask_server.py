#!/usr/bin/env PYTHON
# -*- coding: utf-8 -*-
from ZIG import app
from flask_restful import Api
from flaskext.mysql import MySQL
# from ZIG.models import db

mysql = MySQL()
#MySQL configuation
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'BazaDanychYolo94'
app.config['MYSQL_DATABASE_DB'] = 'rcp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#MySQL init
mysql.init_app(app)

api = Api(app)
