import mysql.connector

class Salary:
    def getSalaryData(self):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        sql = "SELECT * FROM salaries"
        cursor.execute(sql)

        columns = cursor.description

        result = []
        for value in cursor.fetchall():
            tmp = {}
            for (index, column) in enumerate(value):
                if columns[index][0] == "start_hour" or columns[index][0] == "end_hour":
                    tmp[columns[index][0]] = str(column)
                else:
                    tmp[columns[index][0]] = column

            result.append(tmp)
        print(result)

        cursor.close()
        con.close()
        return result

    def getOneSalaryDara(employeeId):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        sql = "SELECT * FROM salaries WHERE employee_id = %s"
        cursor.execute(sql, (employeeId,))

        columns = cursor.description

        result = []
        for value in cursor.fetchall():
            tmp = {}
            for (index, column) in enumerate(value):
                if columns[index][0] == "start_hour" or columns[index][0] == "end_hour":
                    tmp[columns[index][0]] = str(column)
                else:
                    tmp[columns[index][0]] = column
            result.append(tmp)
        print(result)

        cursor.close()
        con.close()
        return result

    def updateSalaryData(employeeId, minHours, salary, startHour, endHour):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        args = minHours, salary, startHour, endHour, employeeId
        sql = "UPDATE salaries SET min_work_hours=%s, salary_value=%s, start_hour=%s, end_hour=%s WHERE employee_id=%s"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1

    def addSalaryData(employeeId, minHours, salary, startHour, endHour):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        args = employeeId, minHours, salary, startHour, endHour
        sql = "INSERT INTO salaries (employee_id, min_work_hours, salary_value, start_hour, end_hour) " \
              "VALUES (%s, %s, %s, %s, %s)"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1