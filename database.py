import time
import mysql.connector
from mysql.connector import Error

def get_db_connection(retries=5, delay=3):
    for attempt in range(retries):
        try:
            return mysql.connector.connect(
                host="mysql",
                port=3306,
                user="root",
                password="",
                database="savvylingua"
            )
        except Error as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(delay)
    raise Exception("Could not connect to the database after several attempts.")

def initialize_tables():
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Documents (
            DocumentID INT AUTO_INCREMENT PRIMARY KEY,
            FileName VARCHAR(255),
            Language VARCHAR(50) DEFAULT 'Korean',
            UploadDate DATETIME DEFAULT CURRENT_TIMESTAMP,
            IsPublic BOOLEAN DEFAULT TRUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ExtractedTexts (
            TextID INT AUTO_INCREMENT PRIMARY KEY,
            DocumentID INT,
            OriginalText LONGTEXT,
            CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (DocumentID) REFERENCES Documents(DocumentID) ON DELETE CASCADE
        )
    """)

    db.commit()
    cursor.close()
    db.close()
