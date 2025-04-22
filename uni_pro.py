import pandas as pd
# Excel faila nosaukums
excel_file = 'piemers.xlsx'

# Iegūst lapu nosaukumus
sheet_names = pd.ExcelFile(excel_file).sheet_names

# Pārbauda, vai ir vismaz 1 lapa
if len(sheet_names) < 1:
    raise ValueError("Failā nav nevienas lapas!")

# Nolasa pirmo lapu
df = pd.read_excel(excel_file, sheet_name=sheet_names[0])

# Pārbauda, vai ir nepieciešamās kolonnas
required_cols = {'atslēga', 'vērtība'}
if not required_cols.issubset(df.columns):
    raise ValueError("Trūkst kolonnas 'atslēga' un/vai 'vērtība'.")