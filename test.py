import mysql.connector

try:
    db = mysql.connector.connect(
        host="127.0.0.1",  # localhost if MySQL is on the same machine
        port= 3306,  # Use the correct port (default is 3306)
        user="root",  # root user, change if needed
        password="",  # Your password for root (empty if none)
        database="SavvyLingua"  # Make sure this database exists
    )

    cursor = db.cursor()
    print("Connected to database")

except mysql.connector.Error as err:
    print(f"Error: {err}")
