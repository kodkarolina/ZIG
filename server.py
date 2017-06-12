from App import app
from App.config import HOST_NAME
from App.config import HOST_PORT

if __name__ == "__main__":
    import sys
    if(len(sys.argv) >= 2 and sys.argv[1] == "-install"):
        print("Database initialization")
        print("This operation DROP tables in database if any exists and create empty ones! Are you sure you want this?")
        print("Write \"yes\" to start database initialization process or click any key to skip.")
        if(input(">") == "yes"):
            from scripts import dataBaseCreate
            dataBaseCreate.createTables()
        else:
            print("Database initialization skipped.")

    print("Server starting...")
    app.run(host=HOST_NAME, port=HOST_PORT)
