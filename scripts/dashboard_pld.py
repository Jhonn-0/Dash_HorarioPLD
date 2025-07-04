import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import os

# --- Funções ---
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path, sep=';', encoding='latin1')
    df['MES_REFERENCIA'] = df['MES_REFERENCIA'].astype(str)
    df['Ano'] = df['MES_REFERENCIA'].str[:4].astype(int)
    df['Mes'] = df['MES_REFERENCIA'].str[4:6].astype(int)

    def periodo_para_datetime(row):
        return datetime(year=row['Ano'], month=row['Mes'], day=1) + timedelta(hours=row['PERIODO_COMERCIALIZACAO'] - 1)

    df['DataHora'] = df.apply(periodo_para_datetime, axis=1)
    df['Data'] = df['DataHora'].dt.date
    return df

# --- Interface ---
st.title("📊 Dashboard PLD Horário")
    
# Carregar todos os arquivos juntos
arquivos = [
    'data/pld_horario_submercado_2023.csv',
    'data/pld_horario_submercado_2024.csv',
    'data/pld_horario_submercado_2025.csv',
]
df = pd.concat([load_data(f) for f in arquivos], ignore_index=True)

# Sidebar de seleção
anos_disponiveis = sorted(df['Ano'].unique())
submercados_disponiveis = sorted(df['SUBMERCADO'].unique())

ano = st.sidebar.selectbox("Selecione o ano", anos_disponiveis, index=len(anos_disponiveis)-1)
submercado = st.sidebar.selectbox("Selecione o submercado", submercados_disponiveis)

# Filtrar
df_filtrado = df[(df['Ano'] == ano) & (df['SUBMERCADO'] == submercado)]

# Média diária
media_diaria = df_filtrado.groupby('Data')['PLD'].mean().reset_index()
media_diaria['Data'] = pd.to_datetime(media_diaria['Data'])

# Gráfico
fig = px.line(media_diaria, x='Data', y='PLD',
              title=f'Média Diária do PLD Horário - {submercado} - {ano}',
              labels={'PLD': 'PLD Médio Diário (R$/MWh)', 'Data': 'Data'})

st.plotly_chart(fig, use_container_width=True)
