import pandas as pd

url = 'https://es.wikipedia.org/wiki/Elecciones_provinciales_de_Buenos_Aires_de_2023'

# Specify header row index
header_row = 0

tables = pd.read_html(url, header=header_row)

# Ninth table on the page
df = tables[8]

# Rename columns
df.columns = ['Date', 'Pollster', 'Sample', 'Frente de Todos', 'Juntos por el Cambio',
             'Avanca Libertad', 'La Libertad Avanca', 'Frente de Izquierda', 'Others',
             'Blank', 'Undecided', 'Lead']

# Filter out rows where Date is NaN
df = df[df['Date'].notna()]

# Drop duplicate header row by index
dup_idx = df[df['Date'].str.startswith('Fecha')].index
df = df.drop(dup_idx)

# Save to CSV
df.to_csv('ba_prov_polls.csv', index=False)