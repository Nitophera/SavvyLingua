# SavvyLingua

**SavvyLingua** is a Dockerized Flask web application that allows users to upload documents in underpreserved language (Jeju), extract text using **OCR.Space**, and store results in a **MySQL database**. The extracted text can be viewed and downloaded as JSON.

## Features

- Upload `.png`, `.jpg`, `.jpeg`, `.pdf` files
- Extract text using OCR.Space API
- Store files and OCR results in a MySQL database
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
### 2. Set up environment variables
Create a .env file with your OCR.Space API key (only if using the online API):

```bash
OCR_API_KEY=your_api_key_here
```

### 3. Run the app

```bash
docker-compose up --build
```

### 4. Visit http://localhost:5000