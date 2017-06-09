class Card:

    def __init__(self, mysql):
        self.mysql = mysql

    def getCardNummers(self):
        con = self.mysql.connect()
        cursor = con.cursor()
        sql = "SELECT card_number FROM cards WHERE isnull(user_id)"
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

    def getCardData(self):
        con = self.mysql.connect()
        cursor = con.cursor()
        sql = "SELECT employee_id, name, surname, card_number FROM employees LEFT JOIN cards USING(user_id)"
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

    def addNewCard(self, card_number):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql = "INSERT INTO cards (card_number) VALUES (%s)"

        cursor.execute(sql, (card_number,) )

        con.commit()

        cursor.close()
        con.close()
        return 1

# Pobranie listy kart
# get (/api/empcard)
# OK: lista wszystkich kart (employee_id, firstName, lastName, card_number)
