# Bioinformatics FASTA Parser

## Description

This project is a simple bioinformatics web application developed using Flask.

It accepts a FASTA sequence from the user and displays:

- FASTA Header
- Sequence Length
- GC Content

## Technologies Used

- Python
- Flask
- Docker
- Git
- GitHub

## Project Structure

bioinfo-tool/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md

## Installation

Install Flask

```bash
pip install -r requirements.txt
```

Run

```bash
python app.py
```

Open

```
http://localhost:5000
```

## Docker

Build Image

```bash
docker build -t bioinfo-tool .
```

Run Container

```bash
docker run -p 5000:5000 bioinfo-tool
```