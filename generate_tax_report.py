import pandas as pd
import io

# Create a dictionary to hold the dataframes for each sheet
dfs = {}

# --- Sheet 1: Questão 1 - Lucro Presumido ---
# Reconstructing the logic from the "Gabarito" CSV
data_q1_dre = [
    ["RECEITA OPERACIONAL BRUTA", 2200000.00],
    ["  (+) Revenda de Mercadorias", 1950000.00],
    ["  (+) Receitas de Comissões", 250000.00],
    ["DEDUÇÕES DAS RECEITAS", -222563.79],
    ["  (-) ICMS", -162225.00],
    ["  (-) ISS", -12500.00],
    ["  (-) COFINS", -32333.25],
    ["  (-) PIS", -7005.54],
    ["  (-) Vendas Canceladas", -2500.00],
    ["  (-) Descontos Incondicionais", -6000.00],
    ["RECEITA OPERACIONAL LÍQUIDA", 1977436.21],
    ["CUSTOS DAS MERCADORIAS VENDIDAS", -1360070.21],
    ["LUCRO BRUTO", 617366.00],
    ["DESPESAS OPERACIONAIS", -146965.00],
    ["  (-) Despesas Vendas", -37410.00],
    ["  (-) Despesas Administrativas", -109555.00],
    ["OUTRAS RECEITAS/DESPESAS", 72729.00],
    ["  (+) Dividendos Recebidos", 30129.00],
    ["  (+) Reversão de Provisão", 8600.00],
    ["  (+) Ganho de Capital (Imobilizado)", 34000.00], # (60.000 - 26.000)
    ["RESULTADO FINANCEIRO LÍQUIDO", 42002.00], # (52100 + 6920 - 17018)
    ["  (+) Rendimentos Renda Fixa", 52100.00],
    ["  (+) Juros Ativos", 6920.00],
    ["  (-) Despesas Financeiras", -17018.00],
    ["RESULTADO DO TRIMESTRE (ANTES TRIBUTOS)", 585132.00]
]

data_q1_calculo = [
    ["DESCRIÇÃO", "BASE CÁLCULO (R$)", "IRPJ (R$)", "CSLL (R$)"],
    ["Receita Bruta Comércio (8% / 12%)", 1891500.00, 151320.00, 226980.00], # 1.950k - 50k (Gov) - Cancel - Desc
    ["Receita Bruta Serviços (32% / 32%)", 250000.00, 80000.00, 80000.00],
    ["(+) Ganho de Capital", 34000.00, 34000.00, 34000.00],
    ["(+) Renda Fixa", 52100.00, 52100.00, 52100.00],
    ["(+) Juros Ativos", 6920.00, 6920.00, 6920.00],
    ["BASE DE CÁLCULO TOTAL", "", 324340.00, 400000.00],
    ["Alíquota Básica (15% / 9%)", "", 48651.00, 36000.00],
    ["Adicional IRPJ (10% s/ excedente 60k)", "", 26434.00, 0.00],
    ["TOTAL DEVIDO", "", 75085.00, 36000.00],
    ["(-) Retenções (IRRF Renda Fixa)", "", -10420.00, 0.00],
    ["(-) Retenções (IRRF Comissões)", "", -3750.00, 0.00],
    ["SALDO A PAGAR", "", 60915.00, 36000.00]
]

df_q1_dre = pd.DataFrame(data_q1_dre, columns=["DRE", "Valor (R$)"])
df_q1_calc = pd.DataFrame(data_q1_calculo[1:], columns=data_q1_calculo[0])
dfs['Questão 1 - IRPJ e CSLL'] = pd.concat([df_q1_dre, pd.DataFrame([["", ""]], columns=["DRE", "Valor (R$)"]), df_q1_calc], axis=0)

# --- Sheet 2: Questão 2 - Distribuição de Lucros ---
data_q2 = [
    ["CÁLCULO DO LUCRO PASSÍVEL DE DISTRIBUIÇÃO ISENTA"],
    ["(+) Resultado do Trimestre antes dos Tributos", 585132.00],
    ["(-) Provisão CSLL", -36000.00],
    ["(-) Provisão IRPJ", -75085.00],
    ["(=) LUCRO LÍQUIDO CONTÁBIL", 474047.00],
    ["", ""],
    ["Resposta:", "O valor máximo possível de distribuição sem incidência é R$ 474.047,00"]
]
dfs['Questão 2 - Distr. Lucros'] = pd.DataFrame(data_q2, columns=["Descrição", "Valor"])

# --- Sheet 3: Questão 3 - Verdadeiro ou Falso ---
data_q3 = [
    ["Afirmação", "Resposta"],
    ["Empresas de transporte de cargas e passageiros utilizam mesmo percentual (CSLL)?", "FALSO"],
    ["Simples Nacional: Valor a pagar é sempre superior ao mês anterior?", "FALSO"],
    ["Atividade parcial (4 meses) em 2024 pode optar pelo Presumido em 2025 (limite)?", "VERDADEIRO"],
    ["Locação de imóveis próprios pode optar pelo Simples (exceção ISS)?", "FALSO"]
]
dfs['Questão 3 - Teoria'] = pd.DataFrame(data_q3)

# --- Sheet 4: Questão 4 - Simples Nacional ---
# Reconstructing the table based on CSV logic
data_q4 = [
    ["Mês", "Receita Mensal", "RBT12 (Acumulada)", "Fator 'r'", "Anexo", "Alíquota Nominal", "Dedução", "Alíquota Efetiva", "Simples a Pagar"],
    ["Maio/2025", 0.0, 0.0, 0.0, "-", 0.0, 0.0, 0.0, 0.0],
    ["Junho/2025", 0.0, 0.0, 0.0, "-", 0.0, 0.0, 0.0, 0.0],
    ["Julho/2025", 85600.00, 513600.00, "0,2345 (23,45%)", "V", "19,50%", 9900.00, "17,57%", 15042.00],
    ["Agosto/2025", 0.0, 342400.00, 0.0, "-", 0.0, 0.0, 0.0, 0.0],
    ["Set/2025", 100000.00, 256800.00, "0,2912 (29,12%)", "III", "11,20%", 9360.00, "7,56%", 7555.14]
]
dfs['Questão 4 - Simples Nacional'] = pd.DataFrame(data_q4[1:], columns=data_q4[0])

# --- Sheet 5: Questão 5 - Posto e Múltipla Escolha ---
data_q5_calc = [
    ["Posto Tapajós LTDA - 3º Trimestre"],
    ["Receita Gasolina", 1800000.00],
    ["Receita Álcool", 650000.00],
    ["Receita Diesel", 1300000.00],
    ["RECEITA TOTAL", 3750000.00],
    ["Base de Cálculo Presumida (1,6%)", 60000.00],
    ["IRPJ (15%)", 9000.00],
    ["Adicional", 0.00],
    ["IRPJ Devido", 9000.00],
    ["(-) Retenção Órgão Público (0,24%)", -9000.00],
    ["SALDO A PAGAR", 0.00],
    ["", ""],
    ["Questão 5.1 (Status do Posto)", "( X ) O Posto Tapajós LTDA não tem imposto de renda a pagar no 3º trim./2025."],
    ["Questão 5.2 (Não integra base CSLL)", "( X ) Os Dividendos Recebidos de Investimentos Avaliados pela Equivalência Patrimonial."]
]
dfs['Questão 5 - Múltipla Escolha'] = pd.DataFrame(data_q5_calc, columns=["Item", "Valor/Resposta"])

# Write to Excel
output_file = 'Gabarito_Reconstruido_Imposto_Renda_2025.xlsx'
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    for sheet_name, df in dfs.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Formatting
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        money_fmt = workbook.add_format({'num_format': '#,##0.00'})
        header_fmt = workbook.add_format({'bold': True, 'bg_color': '#D3D3D3', 'border': 1})
        
        # Apply formats roughly (auto-width)
        for i, col in enumerate(df.columns):
            worksheet.set_column(i, i, 25)
            col_str = str(col)
            if "Valor" in col_str or "R$" in col_str or "Pagar" in col_str:
                worksheet.set_column(i, i, 20, money_fmt)
        
        # Highlight headers
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_fmt)

print(output_file)
