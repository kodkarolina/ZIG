from flaskext.mysql import MySQL

class Address:

    def __init__(self, mysql):
        self.mysql = mysql

    def getAddressData(self):

        con = self.mysql.connect()
        cursor = con.cursor()
        # con = mysql.connector.connect(user='root', password='pw123', host='localhost', database='rcp')
        # cursor = con.cursor()
        sql = "SELECT * FROM addresses"
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

    def getOneAddressData(self, employeeId):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql = "SELECT * FROM addresses WHERE employee_id = %s"
        cursor.execute(sql, (employeeId,))

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

    def updateAddressData(self, country, city, address, postcode, phone, employeeId):
        con = self.mysql.connect()
        cursor = con.cursor()

        args = country, city, address, postcode, phone, employeeId
        sql = "UPDATE addresses SET country=%s, city=%s, address=%s, postcode=%s, phone_number=%s WHERE employee_id=%s"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1

    def addAddressData(self, employeeId, country, city, address, postcode, phone):
        con = self.mysql.connect()
        cursor = con.cursor()

        args = employeeId, country, city, address, postcode, phone
        sql = "INSERT INTO addresses (employee_id, country, city, address, postcode, phone_number) " \
              "VALUES (%s, %s, %s, %s, %s, %s)"

        cursor.execute(sql, args)

        con.commit()

        cursor.close()
        con.close()
        return 1