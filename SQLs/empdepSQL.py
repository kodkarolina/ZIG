import mysql.connector

class Empdep:
    def getEmpDepData(self):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        sql = "SELECT * FROM emp_dep"
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

    def updateEmpDepData(employeeId, departmentId):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        args = departmentId, employeeId
        sql = "UPDATE emp_dep SET department_id=%s WHERE employee_id=%s"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1

    def addEmpDepData(employeeId, departmentId):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        args = employeeId, departmentId
        sql = "INSERT INTO emp_dep (employee_id, department_id) VALUES (%s, %s)"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1