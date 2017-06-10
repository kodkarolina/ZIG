
class WorkTime:

    def __init__(self, mysql):
        self.mysql = mysql

    def getOnePersonWorkTime(self, employee_id):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql = "SELECT date, entry_hour, exit_hour, timediff(exit_hour, entry_hour) AS 'time_in_work' FROM " \
              "working_time JOIN employees USING (employee_id) WHERE employee_id = %s"
        cursor.execute(sql, (employee_id,))

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

