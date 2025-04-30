import requests

OCR_API_KEY = "your_ocr_space_api_key"

def call_ocr_api(filepath):
    with open(filepath, 'rb') as f:
        response = requests.post(
            'https://api.ocr.space/parse/image',
            files={"file": f},
            data={"language": "kor"},
            headers={"apikey": OCR_API_KEY}
        )
    result = response.json()
    return result['ParsedResults'][0]['ParsedText']
