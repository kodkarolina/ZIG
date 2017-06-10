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

    def updateCardData(self, card_number, employee_id):
        con = self.mysql.connect()
        cursor = con.cursor()

        sql_1 = 'SELECT user_id, card_number FROM employees JOIN cards USING(user_id) WHERE employee_id =%s'
        cursor.execute(sql_1, (employee_id,))
        columns = cursor.description

        result_1 = []
        for value in cursor.fetchall():
            tmp = {}
            for (index, column) in enumerate(value):
                tmp[columns[index][0]] = column
            result_1.append(tmp)
        print(result_1)

        user_id = result_1[0]['user_id']
        card_number_to_null = result_1[0]['card_number']

        print(user_id, card_number_to_null)

        sql_2 = 'UPDATE cards SET user_id=null WHERE card_number =%s'
        cursor.execute(sql_2, (card_number_to_null,))
        con.commit()

        args_3 = user_id, card_number
        sql_3 = 'UPDATE cards SET user_id=(%s) WHERE card_number =%s'
        cursor.execute(sql_3, args_3)
        con.commit()

        cursor.close()
        con.close()
        return 1

