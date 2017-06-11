

from flask import jsonify, request, session

from App import app

from SQLs.addressSQL import Address
from SQLs.departmentSQL import Department
from SQLs.empdepSQL import Empdep
from SQLs.employeeSQL import Employee
from SQLs.salarySQL import Salary
from SQLs.userSQL import User
from SQLs.cardSQL import Card
from SQLs.worktimeSQL import WorkTime
from Terminal.terminal import Terminal

from App.models import mysql
from log_user import LogUser

# ==================================Definition of objects==========================================

employee = Employee(mysql)
user = User(mysql)
address = Address(mysql)
salary = Salary(mysql)
department = Department(mysql)
empdep = Empdep(mysql)
logUser = LogUser(mysql)
card = Card(mysql)
work_time = WorkTime(mysql)
terminal = Terminal(mysql)

# ======================================session test=================================================

# ==========================user_authorisation=====================================================


@app.route('/logging/', methods=['GET', 'POST'])
def logging():

    login = request.json['login']
    password = request.json['password']

    if request.method == 'POST':
        if logUser.is_password_ok(login, password) == False:
            data = {"message": "You are not logged in"}
        else:
            data = logUser.get_result(login)

        return jsonify(data)
    elif request.method == 'GET':
        return jsonify({"message": "You are not logged in"})


@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return 'you are logout'

# ===================================ROUTES FOR USERS==========================================


@app.route('/users/', methods=['GET'])
def getUser():
    return jsonify({user.getUserData()})


@app.route('/users/<string:user_id>', methods=['GET'])
def getOneUser(user_id):
    return jsonify(user.getOneUserData(user_id))


@app.route('/users/', methods=['POST'])
def addUser():
    login = request.json['login']
    password = request.json['password']
    permission = request.json['permission']
    return jsonify(user.addUserData(login, password, permission))


@app.route('/users_p/<string:user_id>', methods=['PUT'])
def updateUserPassword(user_id):
    password = request.json['password']
    return jsonify(user.updateUserPassword(user_id, password))


@app.route('/users/<string:user_id>', methods=['PUT'])
def updateUserData(user_id):
    login = request.json['login']
    password = request.json['password']
    permission = request.json['permission']
    return jsonify(user.updateUserData(user_id, login, password, permission))


@app.route('/users/<string:user_id>', methods=['DELETE'])
def deleteUserData(user_id):
    return jsonify(user.deleteUserData(user_id))

# ===================================ROUTES FOR EMPLOYEES==========================================


@app.route('/api/employee/', methods=['GET'])
def getEmp():
    return jsonify(employee.getEmpData())


@app.route('/api/employee/<string:emp_id>/', methods=['GET'])
def getOneEmployee(emp_id):
    return jsonify(employee.getOneEmpData(emp_id))


@app.route('/emp/<string:emp_id>', methods=['PUT'])
def updateEmployee(emp_id):
    name = request.json['name']
    surname = request.json['surname']
    email = request.json['email']
    return jsonify(employee.updateEmpData(emp_id, name, surname, email))


@app.route('/emp/', methods=['POST'])
def addEmp():
    user_id = request.json['user_id']
    name = request.json['name']
    surname = request.json['surname']
    email = request.json['email']
    hire_date = request.json['hire_date']
    return jsonify(employee.addEmpData(user_id, name, surname, email, hire_date))


@app.route('/emp/<string:emp_id>', methods=['DELETE'])
def deleteEmp(emp_id):
    return jsonify(employee.deleteEmpData(emp_id))

# ===================================ROUTES FOR ADDRESS==========================================


@app.route('/address/', methods=['GET'])
def getAddress():
    return jsonify({'addresses': address.getAddressData()})


@app.route('/address/<string:employee_id>', methods=['GET'])
def getOneAddress(employee_id):
    return jsonify(address.getOneAddressData(employee_id))


@app.route('/address/<string:employee_id>', methods=['PUT'])
def updateAddress(employee_id):
    country = request.json['country']
    city = request.json['city']
    address_v = request.json['address']
    postcode = request.json['postcode']
    phone = request.json['phone_number']
    return jsonify(address.updateAddressData(country, city, address_v, postcode, phone, employee_id))


@app.route('/address/', methods=['POST'])
def addAddress():
    employee_id = request.json['employee_id']
    country = request.json['country']
    city = request.json['city']
    address_v = request.json['address']
    postcode = request.json['postcode']
    phone = request.json['phone_number']
    return jsonify(address.addAddressData(employee_id, country, city, address_v, postcode, phone))

# ===================================ROUTES FOR SALARY===========================================


@app.route('/salary/', methods=['GET'])
def getSalary():
    return jsonify({salary.getSalaryData()})


@app.route('/salary/<string:employee_id>', methods=['GET'])
def getOneSalary(employee_id):
    return jsonify(salary.getOneSalaryDara(employee_id))


@app.route('/salary/<string:employee_id>', methods=['PUT'])
def updateSalary(employee_id):
    min_hours = request.json['min_work_hours']
    salary_v = request.json['salary_value']
    start_hour = request.json['start_hour']
    end_hour = request.json['end_hour']
    return jsonify(salary.updateSalaryData(employee_id, min_hours, salary_v, start_hour, end_hour))


@app.route('/salary/', methods=['POST'])
def addSalary():
    employee_id = request.json['employee_id']
    min_hours = request.json['min_work_hours']
    salary_v = request.json['salary_value']
    start_hour = request.json['start_hour']
    end_hour = request.json['end_hour']
    return jsonify(salary.addSalaryData(employee_id, min_hours, salary_v, start_hour, end_hour))


@app.route('/earnings/<string:employee_id>', methods=['POST'])
def countSalary(employee_id):
    start_date = request.json['start_date']
    end_date = request.json['end_date']
    return jsonify(salary.generateSalaryValue(employee_id, start_date, end_date))


# ===================================ROUTES FOR DEPARTMENT=======================================


@app.route('/department/', methods=['GET'])
def getDepartment():

    return jsonify(department.getDepartmentData())


@app.route('/department/<string:department_id>', methods=['GET'])
def getOneDepartment(department_id):
    return jsonify(department.getOneDepartmentData(department_id))


@app.route('/department/', methods=['POST'])
def addDepartment():
    dep_name = request.json['department_name']
    return jsonify(department.addDepartmentData(dep_name))


@app.route('/department/<string:department_id>', methods=['PUT'])
def updateDepartment(department_id):
    dep_name = request.json['department_name']
    return jsonify(department.updateDepartmentData(department_id, dep_name))


@app.route('/department/<string:department_id>', methods=['DELETE'])
def deleteDepartment(department_id):
    return jsonify(department.deleteDepartmentData(department_id))

# ===================================ROUTES FOR EMP_DEP==========================================


@app.route('/empdep/', methods=['GET'])
def getEmpDep():
    return jsonify(empdep.getEmpDepData())


@app.route('/empdep/', methods=['POST'])
def addEmpDep():
    department_id = request.json['department_id']
    employee_id = request.json['employee_id']
    return jsonify(empdep.addEmpDepData(employee_id, department_id))


@app.route('/empdep/', methods=['PUT'])
def updateEmpDep():
    department_id = request.json['department_id']
    employee_id = request.json['employee_id']
    return jsonify(empdep.updateEmpDepData(employee_id, department_id))


@app.route('/empdep/list/', methods=['GET'])
def getEmpDepList():
    return jsonify(empdep.getEmpDepList())


# ===================================ROUTES FOR CARDS==========================================


@app.route('/api/cards/', methods=["GET"])
def getCardsNumbers():
    return jsonify(card.getCardNummers())


@app.route('/api/empcard/', methods=["GET"])
def getCardInfo():
    return jsonify(card.getCardData())


@app.route('/api/empcard/', methods=['POST'])
def addCard():
    card_number = request.json['card_number']
    return jsonify(card.addNewCard(card_number))


@app.route('/api/empcard/<string:employee_id>', methods=['PUT'])
def updateCard(employee_id):
    card_number = request.json['card_number']
    return jsonify(card.updateCardData(card_number, employee_id))


@app.route('/api/addempcard/<string:user_id>', methods=['PUT'])
def addEmpCard(user_id):
    card_number = request.json['card_number']
    return jsonify(card.addNewEmpToCard(user_id,card_number))


# =============ROUTES FOR WORK TIME==========================================


@app.route('/timelist/<string:employee_id>', methods=['GET'])
def getWorkTime(employee_id):
    return jsonify(work_time.getOnePersonWorkTime(employee_id))


@app.route('/timelistall/<string:date>', methods=['GET'])
def getPresentList(date):
    return jsonify(work_time.getPresentList(date))

@app.route('/events/', methods=['GET'])
def getEventList():
    return jsonify(work_time.getEventList())

#===================================ROUTES FOR COMUNICATIONS WITH TERMINAL========================
@app.route('/RFIDterminal', methods=['POST'])
def checkCardID():
    cardID = request.json['CardID']
    eventMode = request.json['Mode']
    return terminal.registerEvent(cardID = cardID, eventType = eventMode)

