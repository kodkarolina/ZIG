
class User:

    def __init__(self, mysql):
        self.mysql = mysql

    def getUserData(self):
        con = self.mysql.connect()
        cursor = con.cursor()
        sql = "SELECT * FROM users"
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

    def getOneUserData(self, userId):
        con = self.mysql.connect()
        cursor = con.cursor()
        sql = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(sql, (userId,))

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

    def addUserData(self, login, password, permission):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql = "INSERT INTO users(login, password, permission) VALUES ('" + login + "','" + password + "','" + \
              permission + "')"
        cursor.execute(sql)

        con.commit()
        result = cursor.lastrowid

        cursor.close()
        con.close()
        return result

    def updateUserPassword(self, userId, password):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql = "UPDATE users SET password='" + password + "' WHERE user_id=" + userId

        cursor.execute(sql)

        con.commit()

        cursor.close()
        con.close()

        return 1

    def updateUserData(self, userId, login, password, permission):
        con = self.mysql.connect()
        cursor = con.cursor()

        args = login, password, permission, userId
        sql = "UPDATE users SET login = %s, password = %s, permission = %s WHERE user_id = %s"

        # sql = "UPDATE users SET login='" + login + "', password='" + password + "', permission='" + permission +\
        #      "' WHERE user_id=" + userId

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()

        return 1

    def deleteUserData(self, userId):
        con = self.mysql.connect()
        cursor = con.cursor()
        sql = "DELETE FROM users WHERE user_id=" + userId
        cursor.execute(sql)

        con.commit()

        cursor.close()
        con.close()
        return 1
