from flaskext.mysql import MySQL

class Empdep:

    def __init__(self, mysql):
        self.mysql = mysql

    def getEmpDepData(self):
        con = self.mysql.connect()
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

    def updateEmpDepData(self, employeeId, departmentId):
        con = self.mysql.connect()
        cursor = con.cursor()

        args = departmentId, employeeId
        sql = "UPDATE emp_dep SET department_id=%s WHERE employee_id=%s"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1

    def addEmpDepData(self, employeeId, departmentId):
        con = self.mysql.connect()
        cursor = con.cursor()

        args = employeeId, departmentId
        sql = "INSERT INTO emp_dep (employee_id, department_id) VALUES (%s, %s)"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1

    def updateEmpDepData(self, employeeId, departmentId):
        con = self.mysql.connect()
        cursor = con.cursor()

        args = departmentId, employeeId
        sql = "UPDATE emp_dep SET department_id= %s WHERE employee_id = %s"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1
