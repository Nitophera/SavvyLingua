from flask import Blueprint, request, jsonify, render_template, current_app, send_file
import os
import json
from models.model import (
    insert_document,
    insert_extracted_text,
    get_text_by_document_id,
    get_all_documents  # <-- make sure this exists
)
from ocr.ocr_api import call_ocr_api

document_blueprint = Blueprint('document_controller', __name__)

@document_blueprint.route('/')
def index():
    return render_template('index.html')

@document_blueprint.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'document' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['document']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file:
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            extracted_text = call_ocr_api(filepath)
            document_id = insert_document(file.filename)
            insert_extracted_text(document_id, extracted_text)

            return jsonify({"message": "Upload successful", "document_id": document_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@document_blueprint.route('/download/<int:document_id>', methods=['GET'])
def download_json(document_id):
    rows = get_text_by_document_id(document_id)
    data = [{"text": row[0]} for row in rows]

    json_filename = f'document_{document_id}.json'
    json_path = os.path.join(current_app.config['UPLOAD_FOLDER'], json_filename)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return send_file(json_path, as_attachment=True)

@document_blueprint.route('/public', methods=['GET'])
def public_documents():
    try:
        documents = get_all_documents()
        return render_template('public_documents.html', documents=documents)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
