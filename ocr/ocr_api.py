import requests
from dotenv import load_dotenv
import os

load_dotenv()
OCR_API_KEY = os.getenv("OCR_API_KEY")

def call_ocr_api(filepath):
    with open(filepath, 'rb') as f:
        response = requests.post(
            'https://api.ocr.space/parse/image',
            files={"file": f},
            data={"language": "kor"},
            headers={"apikey": OCR_API_KEY}
        )

    try:
        result = response.json()
        print("OCR API raw response:", result)

        if result.get("IsErroredOnProcessing"):
            print("OCR API reported an error:", result.get("ErrorMessage"))
            return "(OCR API Error)"

        return result['ParsedResults'][0]['ParsedText']
    except Exception as e:
        print("Failed to parse OCR API response:", e)
        return "(OCR error)"
