# PDF Reader

This repository contains a Python script to read and extract text from PDF files.

## Files

- `Lei Ordinária 254 1993 de Sinop MT.pdf` - Brazilian law document (Lei Ordinária 254/1993 de Sinop, MT)
- `read_pdf.py` - Python script to read and extract text from PDF files
- `requirements.txt` - Python dependencies
- `pesquisa_adin_2975.md` - Legal research on ADIN 2975 and its application to Article 6, VII of the municipal law

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Read the default PDF file in the repository:

```bash
python3 read_pdf.py
```

### Read a specific PDF file:

```bash
python3 read_pdf.py "path/to/your/file.pdf"
```

## Features

- Extracts text from all pages of a PDF document
- Displays page numbers and content
- Handles errors gracefully
- Uses default PDF file if no argument is provided

## Example Output

The script will display:
- PDF filename
- Total number of pages
- Text content from each page
- Success/error messages
