
class WorkTime:

    def __init__(self, mysql):
        self.mysql = mysql

    def getOnePersonWorkTime(self, employee_id):
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

        args = employee_id, employee_id, employee_id, employee_id
        sql = "SELECT A.employee_id, A.date, ((SUM(TIME_TO_SEC(timediff(B.hour, A.hour))))/60/60) AS time_in_work " \
              "FROM (SELECT (@counter_a1 := @counter_a1 + 2) as counter, date, working_time_id, employee_id, hour, " \
              "type FROM working_time WHERE type = 1 AND employee_id = %s UNION " \
              "SELECT (@counter_a2 := @counter_a2 + 2) as counter, date, working_time_id, employee_id, hour, type " \
              "FROM working_time WHERE type = 2 AND employee_id = %s ORDER BY working_time_id) A " \
              "INNER JOIN (SELECT (@counter_b1 := @counter_b1 + 2) as counter, date, working_time_id, employee_id, " \
              "hour, type FROM working_time WHERE type = 1 AND employee_id = %s UNION " \
              "SELECT (@counter_b2 := @counter_b2 + 2) as counter, date, working_time_id, employee_id, hour, type " \
              "FROM working_time WHERE type = 2 AND employee_id = %s ORDER BY working_time_id) B " \
              "ON B.counter = (A.counter + 1) WHERE (mod(A.counter, 2) = 1) GROUP BY A.date"
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

    def getPresentList(self, date):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql = "SELECT employee_id, name, surname FROM employees JOIN working_time USING (employee_id) WHERE date = %s" \
              " GROUP BY employee_id"
        cursor.execute(sql, (date,))

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


