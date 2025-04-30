import mysql.connector
from datetime import datetime

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3307,  
        user="root",
        password="",
        database="savvylingua"
    )

def insert_ocr_text(file_path, language="Korean", is_public=True):
    try:
        db = get_db_connection()
        cursor = db.cursor()

       
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        cursor.execute("""
            INSERT INTO Documents (FileName, Language, UploadDate, IsPublic)
            VALUES (%s, %s, %s, %s)
        """, (file_path, language, datetime.now(), is_public))

        document_id = cursor.lastrowid

       
        cursor.execute("""
            INSERT INTO ExtractedTexts (DocumentID, OriginalText)
            VALUES (%s, %s)
        """, (document_id, text))

        db.commit()
        print(f" Text inserted successfully for file '{file_path}'.")

    except mysql.connector.Error as err:
        print(f" Database error: {err}")
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    insert_ocr_text("ParsedResult (1).txt")
