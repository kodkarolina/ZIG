from flaskext.mysql import MySQL

class User:
    def getUserData(self):
        mysql= MySQL()
        conn = mysql.connect()
        cursor = conn.cursor()


        con = mysql.connector.connect(user='root', password='BazaDanychYolo94', host='localhost', database='rcp')
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

    def getOneUserData(userId):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
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

    def addUserData(login, password, permission):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        sql = "INSERT INTO users(login, password, permission) VALUES ('" + login + "','" + password + "','" + \
              permission + "')"
        cursor.execute(sql)

        con.commit()

        cursor.close()
        con.close()
        return 1

    def updateUserPassword(userId, password):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        sql = "UPDATE users SET password='" + password + "' WHERE user_id=" + userId

        cursor.execute(sql)

        con.commit()

        cursor.close()
        con.close()

        return 1

    def updateUserData(userId, login, password, permission):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()

        args = login, password, permission, userId
        sql = "UPDATE users SET login = %s, password = %s, permission = %s WHERE user_id = %s"

        #sql = "UPDATE users SET login='" + login + "', password='" + password + "', permission='" + permission +\
        #      "' WHERE user_id=" + userId

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()

        return 1

    def deleteUserData(userId):
        con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        cursor = con.cursor()
        sql = "DELETE FROM users WHERE user_id=" + userId
        cursor.execute(sql)

        con.commit()

        cursor.close()
        con.close()
        return 1