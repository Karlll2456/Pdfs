# Tax Report Generator

This repository contains a Python script to generate a comprehensive Excel file with Brazilian tax calculations (IRPJ, CSLL, Simples Nacional, and Lucro Presumido).

## Description

The script generates an Excel file named `Gabarito_Reconstruido_Imposto_Renda_2025.xlsx` containing 5 sheets:

1. **Questão 1 - IRPJ e CSLL**: Income Statement (DRE) and tax calculations for IRPJ and CSLL under "Lucro Presumido" regime
2. **Questão 2 - Distr. Lucros**: Profit distribution calculation (tax-exempt distribution)
3. **Questão 3 - Teoria**: True/False questions about Brazilian tax theory
4. **Questão 4 - Simples Nacional**: Tax calculations under the "Simples Nacional" regime
5. **Questão 5 - Múltipla Escolha**: Gas station tax calculation and multiple choice questions

## Requirements

- Python 3.7 or higher
- pandas
- xlsxwriter
- openpyxl

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Karlll2456/Pdfs.git
cd Pdfs
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script to generate the Excel file:

```bash
python generate_tax_report.py
```

The script will create `Gabarito_Reconstruido_Imposto_Renda_2025.xlsx` in the current directory and print the filename upon completion.

## Output

The generated Excel file includes:
- Formatted headers with gray background and borders
- Monetary values formatted with thousand separators and 2 decimal places
- Column widths adjusted for readability
- Multiple sheets with different tax calculations and scenarios

## License

This project is provided as-is for educational purposes.
