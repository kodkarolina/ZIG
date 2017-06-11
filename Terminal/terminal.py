class Terminal:

    def __init__(self, mysql):
        self.mysql = mysql

    def registerEvent(self, cardID, eventType):

        con = self.mysql.connect()
        cursor = con.cursor()
        sqlQuery = "SELECT employee_id FROM employees JOIN cards USING(user_id) WHERE card_number = %s;"#"SELECT user_id FROM cards WHERE card_number = %s"
        cursor.execute(sqlQuery, cardID)
        result = cursor.fetchall()


        #Brak karty w systemie
        if(len(result) == 0):
            cursor.close()
            con.close()
            return "{\"Access\":\"denied\",\"Error\":\"1\"}"

        sqlQuery = "INSERT INTO `working_time` (`employee_id`, `date`, `hour`, `type`) VALUES (%s, curdate(), curtime(), %s);"

        if(eventType == "enter"):
            cursor.execute(sqlQuery, [str(result[0][0]), "1"])
        elif(eventType == "exit"):
            cursor.execute(sqlQuery, [str(result[0][0]), "2"])
        else:
            cursor.close()
            con.close()
            return "{\"Access\":\"denied\",\"Error\":\"2\"}"

        con.commit()
        cursor.close()
        con.close()
        return "{\"Access\":\"granted\",\"Error\":\"0\"}"

