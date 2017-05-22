from flask import Flask, jsonify, request

from SQLs.employeeSQL import Employee
from SQLs.userSQL import User
from SQLs.addressSQL import Address
from SQLs.salarySQL import Salary
from SQLs.departmentSQL import Department
from SQLs.empdepSQL import Empdep
from SQLs.customSQL import Custom

app = Flask(__name__)

#===================================ROUTES FOR USERS==========================================
@app.route('/users', methods=['GET'])
def getUser():
    userInfo = User()
    return jsonify({'users' : userInfo.getUserData()})

@app.route('/users/<string:userId>', methods=['GET'])
def getOneUser(userId):
    return jsonify(User.getOneUserData(userId))

@app.route('/users', methods=['POST'])
def addUser():
    login = request.json['login']
    password = request.json['password']
    permission = request.json['permission']
    return jsonify(User.addUserData(login, password, permission))

@app.route('/users_p/<string:userId>', methods=['PUT'])
def updateUserPassword(userId):
    password = request.json['password']
    return jsonify(User.updateUserPassword(userId, password))

@app.route('/users/<string:userId>', methods=['PUT'])
def updateUserData(userId):
    login = request.json['login']
    password = request.json['password']
    permission = request.json['permission']
    return jsonify(User.updateUserData(userId, login, password, permission))

@app.route('/users/<string:userId>', methods=['DELETE'])
def deleteUserData(userId):
    return jsonify(User.deleteUserData(userId))

#===================================ROUTES FOR EMPLOYEES==========================================
@app.route('/emp', methods=['GET'])
def getEmp():
    empInfo = Employee()
    return jsonify({'emps' : empInfo.getEmpData()})

@app.route('/emp/<string:empId>', methods=['GET'])
def getOneEmployee(empId):
    return jsonify(Employee.getOneEmpData(empId))

@app.route('/emp/<string:empId>', methods=['PUT'])
def updateEmployee(empId):
    name = request.json['Name']
    surname = request.json['Surname']
    email = request.json['Email']
    return jsonify(Employee.updateEmpData(empId, name, surname, email))

@app.route('/emp', methods=['POST'])
def addEmp():
    name = request.json['Name']
    surname = request.json['Surname']
    email = request.json['Email']
    return jsonify(Employee.addEmpData(name, surname, email))

@app.route('/emp/<string:empId>', methods=['DELETE'])
def deleteEmp(empId):
    return jsonify(Employee.deleteEmpData(empId))

#===================================ROUTES FOR ADDRESS==========================================
@app.route('/address', methods=['GET'])
def getAddress():
    addressInfo = Address()
    return jsonify({'addresses': addressInfo.getAddressData()})

@app.route('/address/<string:employeeId>', methods=['GET'])
def getOneAddress(employeeId):
    return jsonify(Address.getOneAddressData(employeeId))

@app.route('/address/<string:employeeId>', methods=['PUT'])
def updateAddress(employeeId):
    country = request.json['country']
    city = request.json['city']
    address = request.json['address']
    postcode = request.json['postcode']
    phone = request.json['phoneNumber']
    return jsonify(Address.updateAddressData(country, city, address, postcode, phone, employeeId))

@app.route('/address', methods=['POST'])
def addAddress():
    employeeId = request.json['employee_id']
    country = request.json['country']
    city = request.json['city']
    address = request.json['address']
    postcode = request.json['postcode']
    phone = request.json['phoneNumber']
    return jsonify(Address.addAddressData(employeeId, country, city, address, postcode, phone))

#===================================ROUTES FOR SALARY===========================================
@app.route('/salary', methods=['GET'])
def getSalary():
    salaryInfo = Salary()
    return jsonify({'salaries' : salaryInfo.getSalaryData()})

@app.route('/salary/<string:employeeId>', methods=['GET'])
def getOneSalary(employeeId):
    return jsonify(Salary.getOneSalaryDara(employeeId))

@app.route('/salary/<string:employeeId>', methods=['PUT'])
def updateSalary(employeeId):
    minHours = request.json['min_work_hours']
    salary = request.json['salary_value']
    startHour = request.json['start_hour']
    end_hour = request.json['end_hour']
    return jsonify(Salary.updateSalaryData(employeeId, minHours, salary, startHour, end_hour))

@app.route('/salary', methods=['POST'])
def addSalary():
    employeeId = request.json['employee_id']
    minHours = request.json['min_work_info']
    salary = request.json['salary_value']
    startHour = request.json['start_hour']
    end_hour = request.json['end_hour']
    return jsonify(Salary.updateSalaryData(employeeId, minHours, salary, startHour, end_hour))

#===================================ROUTES FOR DEPARTMENT=======================================
@app.route('/department', methods=['GET'])
def getDepartment():
    depInfo = Department()
    return jsonify({'deps' : depInfo.getDepartmentData()})

@app.route('/department/<string:departmentId>', methods=['GET'])
def getOneDepartment(departmentId):
    return jsonify(Department.getOneDepartmentData(departmentId))

@app.route('/department', methods=['POST'])
def addDepartment():
    depName = request.json['department_name']
    return jsonify(Department.addDepartmentData(depName))

@app.route('/department/<string:departmentId>', methods=['PUT'])
def updateDepartment(departmentId):
    depName = request.json['department_name']
    return jsonify(Department.updateDepartmentData(departmentId, depName))

@app.route('/department/<string:departmentId>', methods=['DELETE'])
def deleteDepartment(departmentId):
    return jsonify(Department.deleteDepartmentData(departmentId))

#===================================ROUTES FOR EMP_DEP==========================================
@app.route('/empdep', methods=['GET'])
def getEmpDep():
    empdepInfo = Empdep()
    return jsonify({'empdep' : empdepInfo.getEmpDepData()})

@app.route('/empdep', methods=['POST'])
def addEmpDep():
    departmentId = request.json['department_id']
    employeeId = request.json['employee_id']
    return  jsonify(Empdep.addEmpDepData(employeeId, departmentId))

#===================================ROUTES FOR CUSTOM==========================================
@app.route('/custom/<string:employeeId>', methods=['POST'])
def getCustomSalary(employeeId):
    startDate = request.json['start_date']
    endDate = request.json['end_date']
    return jsonify(Custom.getCustomSalaryData(employeeId, startDate, endDate))


if __name__ == '__main__':
    app.run(debug=True, port=8080)