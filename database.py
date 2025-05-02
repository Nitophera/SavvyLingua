import mysql.connector
from datetime import datetime
import os

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3307,  
        user="root",
        password="",
        database="savvylingua"
    )

def insert_ocr_text(file_path, language="Korean", is_public=True):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        db = get_db_connection()
        cursor = db.cursor()

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read().strip()

        cursor.execute("""
            INSERT INTO Documents (FileName, Language, UploadDate, IsPublic)
            VALUES (%s, %s, %s, %s)
        """, (
            os.path.basename(file_path),
            language,
            datetime.now(),
            int(is_public)  
        ))

        document_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO ExtractedTexts (DocumentID, OriginalText)
            VALUES (%s, %s)
        """, (document_id, text))

        db.commit()
        print(f"Text inserted successfully for file '{file_path}'.")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    insert_ocr_text("OCR results.txt")
h