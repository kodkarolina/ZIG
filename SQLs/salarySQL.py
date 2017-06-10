
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

    def generateSalaryValue(self, employee_id, start_date, end_date):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql_1 = "SET @counter_a1 = -1"
        cursor.execute(sql_1)
        sql_2 = "SET @counter_a2 = 0"
        cursor.execute(sql_2)
        sql_3 = "SET @counter_b1 = -1"
        cursor.execute(sql_3)
        sql_4 = "SET @counter_b2 = 0"
        cursor.execute(sql_4)

        args = employee_id, start_date, end_date, employee_id, start_date, end_date, employee_id, start_date, end_date,\
               employee_id, start_date, end_date

        sql = "SELECT A.employee_id, s.salary_value, ROUND(((SUM(TIME_TO_SEC(timediff(B.hour, A.hour))))/60/60) " \
              "* s.salary_value, 2) AS zarobek FROM (SELECT (@counter_a1 := @counter_a1 + 2) as counter, date, " \
              "working_time_id, employee_id, hour, type FROM working_time WHERE type = 1 AND employee_id = %s AND " \
              "(date BETWEEN %s AND %s) UNION SELECT (@counter_a2 := @counter_a2 + 2) as counter, date," \
              " working_time_id, employee_id, hour, type FROM working_time WHERE type = 2 AND employee_id = %s " \
              "AND (date BETWEEN %s AND %s) ORDER BY working_time_id) A INNER JOIN (SELECT (@counter_b1 := " \
              "@counter_b1 + 2) as counter, date, working_time_id, employee_id, hour, type FROM working_time " \
              "WHERE type = 1 AND employee_id = %s AND (date BETWEEN %s AND %s) UNION SELECT (@counter_b2 := " \
              "@counter_b2 + 2) as counter, date, working_time_id, employee_id, hour, type FROM working_time " \
              "WHERE type = 2 AND employee_id = %s AND (date BETWEEN %s AND %s) ORDER BY working_time_id) B ON " \
              "B.counter = (A.counter + 1) JOIN salaries s ON A.employee_id = s.employee_id " \
              "WHERE (mod(A.counter, 2) = 1)"

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

        zarobek = str(result[0]['zarobek'])
        salary_value = result[0]['salary_value']
        employee_id = result[0]['employee_id']

        result = [{"employee_id": employee_id, 'salary_value': salary_value, "zarobek": zarobek}]
        print(result)

        cursor.close()
        con.close()
        return result
