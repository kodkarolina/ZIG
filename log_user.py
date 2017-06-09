class LogUser:
    def __init__(self, mysql):
        self.mysql = mysql

    def is_password_ok(self, login, password):
        con = self.mysql.connect()
        cursor = con.cursor()
        sql = "SELECT * FROM users WHERE login = %s"
        cursor.execute(sql, (login,))

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

        pass_word = result[0]['password']

        if password == pass_word:
            return True
        else:
            return False

    def get_result(self, login):
        con = self.mysql.connect()
        cursor = con.cursor()
        sql = "SELECT * FROM users WHERE login = %s"
        cursor.execute(sql, (login,))

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

