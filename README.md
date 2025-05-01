# SavvyLingua

This is a simple **Flask web application** that allows users to upload document in underpreserved languages, extract text using the **OCR.Space API**, and store the results in a **MySQL database**. Users can also download the extracted text as a JSON file.

## Features

- Upload documents in . format
- Extract text from images using OCR
- Store uploaded documents and extracted text in MySQL
- Download extracted text in `.json` format


## Prerequisites

- Python 3.8+
- MySQL (e.g., XAMPP or local MySQL server)
- An OCR.Space API key

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Nitophera/SavvyLingua
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create the MySQL database and tables:
    ```sql
    CREATE DATABASE SavvyLingua;

    USE SavvyLingua;

    CREATE TABLE Documents (
        DocumentID INT AUTO_INCREMENT PRIMARY KEY,
        FileName VARCHAR(255),
        Language VARCHAR(255),
        UploadDate DATETIME,
        IsPublic BOOLEAN
    );

    CREATE TABLE ExtractedTexts (
        TextID INT AUTO_INCREMENT PRIMARY KEY,
        DocumentID INT,
        OriginalText LONGTEXT,
        FOREIGN KEY (DocumentID) REFERENCES Documents(DocumentID)
    );
    ```

4. Set Up the `.env` File
    Create a file named .env in the root directory and add:
    ```python
    OCR_API_KEY=your_ocr_api_key_here
    ```

## Running the App

```bash
python app.py

Contributed
