import mysql.connector
import json
from datetime import datetime

def get_db_connection():
    """Establish connection to MySQL database"""
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3307,
        user="root",
        password="",
        database="savvylingua"
    )

def fetch_and_convert_to_json(output_file='ocr_data.json'):
    """
    Fetch data from database and convert to JSON format
    """
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        
        query = """
        SELECT 
            d.DocumentID,
            d.FileName,
            d.Language,
            d.UploadDate,
            d.IsPublic,
            e.TextID,
            e.OriginalText
        FROM Documents d
        JOIN ExtractedTexts e ON d.DocumentID = e.DocumentID
        ORDER BY d.UploadDate DESC
        """
        
        cursor.execute(query)
        results = cursor.fetchall()
        
        json_data = []
        for row in results:
           
            upload_date = row['UploadDate'].isoformat() if row['UploadDate'] else None
            
            document = {
                'document_id': row['DocumentID'],
                'file_name': row['FileName'],
                'language': row['Language'],
                'upload_date': upload_date,
                'is_public': bool(row['IsPublic']),
                'extracted_text': {
                    'text_id': row['TextID'],  
                    'content': row['OriginalText'],
                    'statistics': {
                        'characters': len(row['OriginalText']),
                        'words': len(row['OriginalText'].split()),
                        'lines': len(row['OriginalText'].splitlines())
                    }
                }
            }
            json_data.append(document)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        
        print(f"Successfully converted {len(json_data)} records to JSON in {output_file}")
        
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()

if __name__ == "__main__":
    fetch_and_convert_to_json()
    