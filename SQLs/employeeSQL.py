from flaskext.mysql import MySQL

class Employee:

    def __init__(self, mysql):
        self.mysql = mysql

    def getEmpData(self):
        con = self.mysql.connect()
        cursor = con.cursor()
        sql = "SELECT * FROM employees"
        cursor.execute(sql)

        columns = cursor.description

        result = []
        for value in cursor.fetchall():
            tmp = {}
            for (index, column) in enumerate(value):
                tmp[columns[index][0]] = column
            result.append(tmp)
        print(result)

        cursor.close()
        con.close()
        return result

    def getOneEmpData(self, empId):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql = "SELECT * FROM employees WHERE employee_id = %s"
        cursor.execute(sql, (empId,))

        columns = cursor.description

        result = []
        for value in cursor.fetchall():
            tmp = {}
            for (index, column) in enumerate(value):
                tmp[columns[index][0]] = column
            result.append(tmp)
        print(result)

        cursor.close()
        con.close()
        return result

    def updateEmpData(self, idEmployee, name, surname, email):
        con = self.mysql.connect()
        cursor = con.cursor()

        args = name, surname, email, idEmployee
        sql = "UPDATE employees SET name = %s, surname = %s, email = %s WHERE employee_id = %s"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()

        return 1

    def addEmpData(self, userId, name, surname, email, hire_date):
        con = self.mysql.connect()
        cursor = con.cursor()

        args = userId, name, surname, email, hire_date
        sql = "INSERT INTO employees(user_id, Name, Surname, email, hire_date) VALUES (%s, %s, %s, %s, %s)"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1

    def deleteEmpData(self, empId):
        con = self.mysql.connect()
        cursor = con.cursor()
        sql = "DELETE FROM employees WHERE employee_id = %s"
        cursor.execute(sql, (empId,))

        con.commit()

        cursor.close()
        con.close()
        return 1