from datetime import datetime

def insert_ocr_text(file_path, language="Korean", is_public=True):
    try:
        db = get_db_connection()
        cursor = db.cursor()

        # Read OCR text from file
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        # Insert document metadata
        cursor.execute("""
            INSERT INTO Documents (FileName, Language, UploadDate, IsPublic)
            VALUES (%s, %s, %s, %s)
        """, (file_path, language, datetime.now(), is_public))

        document_id = cursor.lastrowid

        # Insert extracted OCR text
        cursor.execute("""
            INSERT INTO ExtractedTexts (DocumentID, OriginalText)
            VALUES (%s, %s)
        """, (document_id, text))

        db.commit()
        print(f"✅ Text inserted successfully for file '{file_path}'.")

    except mysql.connector.Error as err:
        print(f"❌ Database error: {err}")
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    insert_ocr_text("ParsedResult (1).txt")
