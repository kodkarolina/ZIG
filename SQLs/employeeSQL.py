import mysql.connector

class Employee:
    def getEmpData(self):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
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

    def getOneEmpData(empId):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
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

    def updateEmpData(idEmployee, name, surname, email):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        args = name, surname, email, idEmployee
        sql = "UPDATE employees SET name = %s, surname = %s, email = %s WHERE employee_id = %s"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()

        return 1

    def addEmpData(userId, name, surname, email):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        args = userId, name, surname, email
        sql = "INSERT INTO employees(user_id, Name, Surname, email) VALUES (%s, %s, %s, %s)"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1

    def deleteEmpData(empId):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()
        sql = "DELETE FROM employees WHERE employee_id = %s"
        cursor.execute(sql, (empId,))

        con.commit()

        cursor.close()
        con.close()
        return 1