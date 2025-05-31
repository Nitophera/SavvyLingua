from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def call_ocr_api(file_input):
    """
    Accepts either a FileStorage object or a file path (image or PDF).
    Handles image OCR directly or converts PDFs to images for OCR.
    """
    # Save if it's an uploaded file
    if hasattr(file_input, 'filename') and hasattr(file_input, 'save'):
        if file_input.filename == "":
            return ""
        file_path = os.path.join(UPLOAD_FOLDER, file_input.filename)
        file_input.save(file_path)
    elif isinstance(file_input, str):
        file_path = file_input
        if not os.path.isfile(file_path):
            return "(Invalid file path)"
    else:
        return "(Unsupported input type)"

    # Check if it's a PDF
    if file_path.lower().endswith('.pdf'):
        try:
            images = convert_from_path(file_path)
            text = ""
            for img in images:
                text += pytesseract.image_to_string(img, lang="eng+kor") + "\n"
            return text.strip()
        except Exception as e:
            return f"(OCR error: failed to convert PDF - {str(e)})"
    else:
        try:
            image = Image.open(file_path)
            return pytesseract.image_to_string(image, lang="eng+kor")
        except Exception as e:
            return f"(OCR error: {str(e)})"
