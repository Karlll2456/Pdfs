#!/usr/bin/env python3
"""
Script to read and extract text from PDF files.
Usage: python3 read_pdf.py [pdf_filename]
"""

import sys
import os
from PyPDF2 import PdfReader


def read_pdf(pdf_path):
    """
    Read and extract text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
    """
    # Open the PDF file
    reader = PdfReader(pdf_path)
    
    # Get the number of pages
    num_pages = len(reader.pages)
    print(f"\n{'='*80}")
    print(f"PDF: {os.path.basename(pdf_path)}")
    print(f"Total pages: {num_pages}")
    print(f"{'='*80}\n")
    
    # Extract text from all pages
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text.strip():
            print(f"\n--- Page {page_num} ---\n")
            print(text)


def main():
    """Main function to handle command-line execution."""
    # Default PDF file in the repository
    default_pdf = "Lei Ordinária 254 1993 de Sinop MT.pdf"
    
    # Get PDF path from command line argument or use default
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = default_pdf
    
    # Check if file exists
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' does not exist.")
        print(f"\nUsage: python3 read_pdf.py [pdf_filename]")
        print(f"If no filename is provided, it will read: {default_pdf}")
        sys.exit(1)
    
    # Read the PDF
    print(f"Reading PDF file: {pdf_path}\n")
    try:
        read_pdf(pdf_path)
        print(f"\n{'='*80}")
        print("PDF reading completed successfully!")
        print(f"{'='*80}")
    except FileNotFoundError:
        print(f"Error: File '{pdf_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
