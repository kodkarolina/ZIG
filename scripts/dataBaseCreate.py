from App.models import mysql

def createTables():
    print("Initializing tables...")
    con = mysql.connect()
    cursor = con.cursor()

    filename = "scripts\dbInit.sql"
    sqlQuery = ""
    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        sqlQuery += line.replace("\\n","\n")

    cursor.execute(sqlQuery)
    con.commit()
    cursor.close()
    con.close()
    print("OK!")