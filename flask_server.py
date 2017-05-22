#!/usr/bin/env PYTHON
# -*- coding: utf-8 -*-

from flask import Flask, json, jsonify, request
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)


#MySQL configuation
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'BazaDanychYolo94'
app.config['MYSQL_DATABASE_DB'] = 'rcp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

api = Api(app)

#Creating user in api
class CreateUser(Resource):
    def post(self):
        try:
            #parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('userName', type=str, help= 'User name to crate user')
            parser.add_argument('password', type=str, help='Password to crate user')
            parser.add_argument('email', type=str, help = 'Email to create user')
            args = parser.parse_args()

            _userName = args ['userName']
            _userPassword = args['password']
            _userEmail = args['email']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spCreateUser', (_userName, _userPassword, _userEmail))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': 'User creation success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}


        except Exception as e:
            return {'error' : str(e)}

#Class to authnticate user
class AuthenticateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('userName', type=str, help='User name to crate user')
            parser.add_argument('password', type=str, help='Password to crate user')
            args = parser.parse_args()

            _userName = args['userName']
            _userPassword = args['password']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_AuthenticateUser', (_userName, ))
            data = cursor.fetchall()

            if (len(data) > 0):
                if (str(data[0][2]) == _userPassword):
                    return {'status': 200, 'UserId': str(data[0][0])}
                else:
                    return {'status': 100, 'message': 'Authentication failure'}

        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/CreateUser')
api.add_resource(AuthenticateUser, '/AuthenticateUser')

if __name__=='__main__':
    app.run(debug= True)