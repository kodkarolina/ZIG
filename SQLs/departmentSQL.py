from flaskext.mysql import MySQL

class Department:

    def __init__(self, mysql):
        self.mysql = mysql

    def getDepartmentData(self):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql = "SELECT * FROM departments"
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

    def getOneDepartmentData(self, departmentId):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql = "SELECT * FROM departments WHERE department_id = %s"
        cursor.execute(sql, (departmentId,))

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

    def updateDepartmentData(self, departmentId, departmentName):
        con = self.mysql.connect()
        cursor = con.cursor()

        args = departmentName, departmentId
        sql = "UPDATE departments SET department_name=%s WHERE department_id=%s"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1

    def addDepartmentData(self, departmentName):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql = "INSERT INTO departments (department_name) " \
              "VALUES (%s)"

        cursor.execute(sql, departmentName)

        con.commit()

        cursor.close()
        con.close()
        return 1

    def deleteDepartmentData(self, departmentId):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql = "DELETE FROM departments WHERE department_id=%s"

        cursor.execute(sql, departmentId)

        con.commit()

        cursor.close()
        con.close()
        return 1