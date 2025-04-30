import mysql.connector

def get_db_connection():
    try:
        db = mysql.connector.connect(
            host="127.0.0.1", 
            port= 3307, 
            user="root",  
            password="",  
            database="savvylingua"  
        )

        cursor = db.cursor()
        print("Connected to database")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
if __name__ == "__main__":
    get_db_connection()