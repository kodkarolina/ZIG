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
        print(pass_word)
        if password == pass_word:

            return result[0]['user_id']
        else:
            return 'logged failed'

    # def authenticate(self,result):
