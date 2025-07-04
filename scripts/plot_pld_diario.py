import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

# Caminho do arquivo CSV local
csv_path = 'data/pld_horario_submercado_2024.csv'

# Criar pasta outputs caso não exista
os.makedirs('outputs', exist_ok=True)

# Ler CSV
df = pd.read_csv(csv_path, sep=';', encoding='latin1')

print(df.head())

# Converter MES_REFERENCIA para string
df['MES_REFERENCIA'] = df['MES_REFERENCIA'].astype(str)

# Extrair ano e mês
df['Ano'] = df['MES_REFERENCIA'].str[:4].astype(int)
df['Mes'] = df['MES_REFERENCIA'].str[4:6].astype(int)

# O PERIODO_COMERCIALIZACAO é o período horário dentro do mês (ex: 1, 2, 3 ...)
# Vamos criar uma data/hora a partir do primeiro dia do mês + (periodo - 1) horas
def periodo_para_datetime(row):
    dt = datetime(year=row['Ano'], month=row['Mes'], day=1) + timedelta(hours=row['PERIODO_COMERCIALIZACAO'] - 1)
    return dt

df['DataHora'] = df.apply(periodo_para_datetime, axis=1)

# Filtrar o submercado desejado (exemplo: NORDESTE)
submercado = 'NORDESTE'
df_sub = df[df['SUBMERCADO'] == submercado]

# Criar coluna só com a data para agrupar por dia
df_sub['Data'] = df_sub['DataHora'].dt.date

# Calcular média diária do PLD
media_diaria = df_sub.groupby('Data')['PLD'].mean().reset_index()

# Converter a coluna Data para datetime para o matplotlib
media_diaria['Data'] = pd.to_datetime(media_diaria['Data'])

# Plotar gráfico da média diária
plt.figure(figsize=(12,6))
plt.plot(media_diaria['Data'], media_diaria['PLD'], marker='o')
plt.title(f'Média Diária do PLD Horário - Submercado {submercado}')
plt.xlabel('Data')
plt.ylabel('PLD Médio Diário (R$/MWh)')
plt.grid(True)

# Salvar o gráfico
output_path = f'outputs/pld_medio_diario_{submercado}.png'
plt.savefig(output_path)
print(f"Gráfico salvo em {output_path}")

plt.show()
