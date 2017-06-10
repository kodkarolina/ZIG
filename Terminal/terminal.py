
class Terminal:

    def __init__(self, mysql):
        self.mysql = mysql

    def registerEvent(self, cardID, eventType):
        if(cardID == "B5B607A5A1"):
            return "{\"Access\":\"granted\",\"Error\":\"0\"}"
        else:
            return "{\"Access\":\"denied\",\"Error\":\"0\"}"