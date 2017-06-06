#!/usr/bin/env PYTHON
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, Request, json, request
from flask_restful import Api #, Resource, reqparse
from flaskext.mysql import MySQL
from flask_login import  LoginManager


from ZIG.log_user import LogUser

from ZIG.SQLs.employeeSQL import Employee
from ZIG.SQLs.userSQL import User
from ZIG.SQLs.addressSQL import Address
from ZIG.SQLs.salarySQL import Salary
from ZIG.SQLs.departmentSQL import Department
from ZIG.SQLs.empdepSQL import Empdep
from ZIG.SQLs.customSQL import Custom

app = Flask(__name__)
app.config.from_object('config')

mysql = MySQL()
login_manager = LoginManager()
login_manager.init_app(app)

#MySQL configuation
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'BazaDanychYolo94'
app.config['MYSQL_DATABASE_DB'] = 'rcp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

api = Api(app)

#==================================Definition of objects==========================================
employee = Employee(mysql)
user = User(mysql)
address = Address(mysql)
salary = Salary(mysql)
department = Department(mysql)
empdep = Empdep(mysql)
custom = Custom(mysql)
logUser = LogUser(mysql)
#==========================user_authorisation=====================================================

@app.route('/logging', methods=[ 'POST'])
def logging():

    login = request.json['login']
    password = request.json['password']

    return jsonify({"log_user": logUser.is_password_ok(login, password)})

#===================================ROUTES FOR USERS==========================================
@app.route('/users', methods=['GET'])
def getUser():
    return jsonify({'users': user.getUserData()})

@app.route('/users/<string:userId>', methods=['GET'])
def getOneUser(userId):
    return jsonify(user.getOneUserData(userId))

@app.route('/users', methods=['POST'])
def addUser():
    login = request.json['login']
    password = request.json['password']
    permission = request.json['permission']
    return jsonify(user.addUserData(login, password, permission))


@app.route('/users_p/<string:userId>', methods=['PUT'])
def updateUserPassword(userId):
    password = request.json['password']
    return jsonify(user.updateUserPassword(userId, password))

@app.route('/users/<string:userId>', methods=['PUT'])
def updateUserData(userId):
    login = request.json['login']
    password = request.json['password']
    permission = request.json['permission']
    return jsonify(user.updateUserData(userId, login, password, permission))

@app.route('/users/<string:userId>', methods=['DELETE'])
def deleteUserData(userId):
    return jsonify(user.deleteUserData(userId))

#===================================ROUTES FOR EMPLOYEES==========================================
@app.route('/emp', methods=['GET'])
def getEmp():
    return jsonify({'emps' : employee.getEmpData()})

@app.route('/emp/<string:empId>', methods=['GET'])
def getOneEmployee(empId):
    return jsonify(employee.getOneEmpData(empId))

@app.route('/emp/<string:empId>', methods=['PUT'])
def updateEmployee(empId):
    name = request.json['Name']
    surname = request.json['Surname']
    email = request.json['Email']
    return jsonify(employee.updateEmpData(empId, name, surname, email))

@app.route('/emp', methods=['POST'])
def addEmp():
    userId = request.json['userId']
    name = request.json['Name']
    surname = request.json['Surname']
    email = request.json['Email']
    return jsonify(employee.addEmpData(userId, name, surname, email))

@app.route('/emp/<string:empId>', methods=['DELETE'])
def deleteEmp(empId):
    return jsonify(employee.deleteEmpData(empId))

#===================================ROUTES FOR ADDRESS==========================================
@app.route('/address', methods=['GET'])
def getAddress():
    return jsonify({'addresses': address.getAddressData()})

@app.route('/address/<string:employeeId>', methods=['GET'])
def getOneAddress(employeeId):
    return jsonify(address.getOneAddressData(employeeId))

@app.route('/address/<string:employeeId>', methods=['PUT'])
def updateAddress(employeeId):
    country = request.json['country']
    city = request.json['city']
    address = request.json['address']
    postcode = request.json['postcode']
    phone = request.json['phoneNumber']
    return jsonify(address.updateAddressData(country, city, address, postcode, phone, employeeId))

@app.route('/address', methods=['POST'])
def addAddress():
    employeeId = request.json['employee_id']
    country = request.json['country']
    city = request.json['city']
    address = request.json['address']
    postcode = request.json['postcode']
    phone = request.json['phoneNumber']
    return jsonify(address.addAddressData(employeeId, country, city, address, postcode, phone))

#===================================ROUTES FOR SALARY===========================================
@app.route('/salary', methods=['GET'])
def getSalary():

    return jsonify({'salaries' : salary.getSalaryData()})

@app.route('/salary/<string:employeeId>', methods=['GET'])
def getOneSalary(employeeId):
    return jsonify(salary.getOneSalaryDara(employeeId))

@app.route('/salary/<string:employeeId>', methods=['PUT'])
def updateSalary(employeeId):
    minHours = request.json['min_work_hours']
    salary = request.json['salary_value']
    startHour = request.json['start_hour']
    end_hour = request.json['end_hour']
    return jsonify(salary.updateSalaryData(employeeId, minHours, salary, startHour, end_hour))

@app.route('/salary', methods=['POST'])
def addSalary():
    employeeId = request.json['employee_id']
    minHours = request.json['min_work_info']
    salary = request.json['salary_value']
    startHour = request.json['start_hour']
    end_hour = request.json['end_hour']
    return jsonify(salary.updateSalaryData(employeeId, minHours, salary, startHour, end_hour))

#===================================ROUTES FOR DEPARTMENT=======================================
@app.route('/department', methods=['GET'])
def getDepartment():

    return jsonify({'deps' : department.getDepartmentData()})

@app.route('/department/<string:departmentId>', methods=['GET'])
def getOneDepartment(departmentId):
    return jsonify(department.getOneDepartmentData(departmentId))

@app.route('/department', methods=['POST'])
def addDepartment():
    depName = request.json['department_name']
    return jsonify(department.addDepartmentData(depName))

@app.route('/department/<string:departmentId>', methods=['PUT'])
def updateDepartment(departmentId):
    depName = request.json['department_name']
    return jsonify(department.updateDepartmentData(departmentId, depName))

@app.route('/department/<string:departmentId>', methods=['DELETE'])
def deleteDepartment(departmentId):
    return jsonify(department.deleteDepartmentData(departmentId))

#===================================ROUTES FOR EMP_DEP==========================================
@app.route('/empdep', methods=['GET'])
def getEmpDep():

    return jsonify({'empdep' : empdep.getEmpDepData()})

@app.route('/empdep', methods=['POST'])
def addEmpDep():
    departmentId = request.json['department_id']
    employeeId = request.json['employee_id']
    return  jsonify(empdep.addEmpDepData(employeeId, departmentId))

#===================================ROUTES FOR CUSTOM==========================================
@app.route('/custom/<string:employeeId>', methods=['POST'])
def getCustomSalary(employeeId):
    startDate = request.json['start_date']
    endDate = request.json['end_date']
    return jsonify(custom.getCustomSalaryData(employeeId, startDate, endDate))


if __name__ == '__main__':
    app.run(debug=True)

