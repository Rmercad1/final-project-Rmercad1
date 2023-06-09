import pandas as pd

url = 'https://es.wikipedia.org/wiki/Elecciones_provinciales_de_San_Juan_de_2023'

# Specify header row index
header_row = 0

# Set decimal and thousands separators
decimal = ','
thousands = '.'

tables = pd.read_html(url, header=header_row, decimal=decimal, thousands=thousands)

# table on the page
df = tables[4]

# Rename columns
df.columns = ['Date', 'Pollster', 'Sample', 'Frente de Todos', 'Juntos por el Cambio',
             'Frente de Izquierda', 'La Libertad Avanza', 'Others',
             'Blank', 'Undecided', 'Lead']

# Filter out rows where Date is NaN
df = df[df['Date'].notna()]

# Drop duplicate header row by index
dup_idx = df[df['Date'].str.startswith('Fecha')].index
df = df.drop(dup_idx)

# Save to CSV
df.to_csv('san_juan_polls.csv', index=False)