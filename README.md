# SavvyLingua

**SavvyLingua** is a Dockerized Flask web application that allows users to upload documents in underpreserved language (Jeju), extract text using Tesseract OCR, and store results in a database. The extracted text can be viewed and downloaded as JSON.

## Features

- Upload `.png`, `.jpg`, `.jpeg`, `.pdf` files
- Extract text using OCR
- Store files and OCR results in database
- View public documents
- Download OCR results as `.json`

---

## Running with Docker

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 1. Clone the repo

```bash
git clone https://github.com/Nitophera/SavvyLingua
cd SavvyLingua
```
### 2. Run the app

```bash
docker-compose up --build
```

### 4. Visit http://localhost:5000
