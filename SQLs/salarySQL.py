
class Salary:

    def __init__(self, mysql):
        self.mysql = mysql

    def getSalaryData(self):
        con = self.mysql.connect()
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

    def getOneSalaryDara(self, employeeId):
        con = self.mysql.connect()
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

    def updateSalaryData(self, employeeId, minHours, salary, startHour, endHour):
        con = self.mysql.connect()
        cursor = con.cursor()

        args = minHours, salary, startHour, endHour, employeeId
        sql = "UPDATE salaries SET min_work_hours=%s, salary_value=%s, start_hour=%s, end_hour=%s WHERE employee_id=%s"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1

    def addSalaryData(self, employeeId, minHours, salary, startHour, endHour):
        con = self.mysql.connect()
        cursor = con.cursor()

        args = employeeId, minHours, salary, startHour, endHour
        sql = "INSERT INTO salaries (employee_id, min_work_hours, salary_value, start_hour, end_hour) " \
              "VALUES (%s, %s, %s, %s, %s)"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1

    def generateSalaryValue(self, employe_id, start_date, end_date):
        con = self.mysql.connect()
        cursor = con.cursor()

        args = start_date, end_date, employe_id
        sql = "SELECT ROUND(((SUM(TIME_TO_SEC(timediff(exit_hour, entry_hour))))/60/60) * s.salary_value , 2)  " \
              "AS 'Zarobek', salary_value FROM employees e JOIN working_time w USING(employee_id) JOIN salaries s " \
              "USING(employee_id) WHERE (%s <= w.date) AND (%s>= w.date) AND e.employee_id = %s"
        cursor.execute(sql, args)

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

        zarobek = str(result[0]['Zarobek'])
        salary_value = result[0]['salary_value']

        result = [{"Zarobek": zarobek, 'salary_value': salary_value }]
        print(result)

        cursor.close()
        con.close()
        return result
