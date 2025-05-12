from database import get_db_connection

def insert_document(filename):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO Documents (FileName, UploadDate) VALUES (%s, NOW())", (filename,))
    db.commit()
    document_id = cursor.lastrowid
    cursor.close()
    db.close()
    return document_id

def insert_extracted_text(document_id, text):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO ExtractedTexts (DocumentID, OriginalText, CreatedAt) VALUES (%s, %s, NOW())",
                   (document_id, text))
    db.commit()
    cursor.close()
    db.close()

def get_text_by_document_id(document_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT OriginalText FROM ExtractedTexts WHERE DocumentID = %s", (document_id,))
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    return rows

def get_all_documents():
    db = get_db_connection()  # Use MySQL connection
    cursor = db.cursor()
    cursor.execute("SELECT DocumentID, FileName FROM documents")  # Update column name if needed
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results
