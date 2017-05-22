import mysql.connector

class Custom:
    def getCustomSalaryData(employeeId, startDate, endDate):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        args = startDate, endDate, employeeId
        sql = "SELECT ROUND(((SUM(TIME_TO_SEC(timediff(exit_hour, entry_hour))))/60/60) * s.salary_value , 2) " \
              "AS 'Zarobek', salary_value FROM employees e JOIN working_time w USING(employee_id) JOIN salaries s " \
              "USING(employee_id) WHERE (%s < w.date) AND (%s > w.date) AND e.employee_id = %s"

        cursor.execute(sql, args)

        columns = cursor.description

        result = []
        for value in cursor.fetchall():
            tmp = {}
            for (index, column) in enumerate(value):
                tmp[columns[index][0]] = str(column)
            result.append(tmp)
        print(result)

        cursor.close()
        con.close()
        return result